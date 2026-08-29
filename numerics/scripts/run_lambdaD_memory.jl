# run_lambdaD_memory.jl — wave-2 production runs for the λ–D showcase
# (bd tns-f5r): kink transport / memory in the Néel phase, and the Haldane vs
# large-D edge-memory contrast.
#
#   julia --project=numerics numerics/scripts/run_lambdaD_memory.jl [stage...]
#
# Stages (default: all three):
#   dispersion  the domain-wall band ω(k) in the TOPOLOGICAL sector
#               (left_gs = ψ_A, right_gs = ψ_B) over the Brillouin zone
#               (−π/2, π/2], at several χ, together with the trivial-sector
#               excitation at the same momenta for contrast.
#                                     -> results/lambdaD-kink-dispersion.json
#   converge    the same protocol at three TDVP2 truncation ranks, so that the
#               χ-dependence of the memory numbers is visible.
#                             -> results/lambdaD-kink-memory-convergence.json
#   transport   the λD-KINK-MEM protocol: a dressed kink wavepacket carried
#               across a fixed measurement window by window-TDVP, with the
#               windowed staggered-charge history and three wall estimators.
#               Also runs the SHARP-junction control at the same geometry.
#                                     -> results/lambdaD-kink-memory.json
#   edge        λD-EDGE-MEM at the Haldane and large-D points: a boundary field
#               is switched off at t = 0 and the left-half magnetisation is
#               followed.                -> results/lambdaD-edge-memory.json
#
# Every record is rewritten to disk as soon as it exists, so a partial run is
# still a usable artifact.  Nothing here is a pass/fail test — the assertions
# live in numerics/test/test_lambdaD_memory.jl.
#
# HONESTY NOTES carried into the JSON.
#  * The TDVP window has frozen infinite environments.  `edge_leak` is the
#    wall-density weight within `edge_guard` sites of either end; readout times
#    are only taken where it is below 1e-3.
#  * The recorded charge law is the exact SINGLE-TIME law of Q̂_{W,c₀} at each
#    sample.  The ordered TPM law of D27, with a genuine first projective
#    measurement, is not computed here; the mean escaped charge coincides with
#    the TPM first moment only if D27(LR2) holds.
#  * `s` is the MEASURED tail density m_stag ≈ 0.9603, not 1 and not a
#    half-integer.  Every coefficient in the record uses the measured value.

using Printf
using Dates
using JSON

include(joinpath(@__DIR__, "..", "src", "lambdaD_memory.jl"))
using .LambdaDMemory
include(joinpath(@__DIR__, "..", "src", "lambdaD_edge.jl"))
using .LambdaDEdge

const LDM = LambdaDMemory.LambdaD
const LDE = LambdaDEdge.LambdaD
const RESULTS = joinpath(@__DIR__, "..", "results")

using MPSKit: excitations, QuasiparticleAnsatz

function write_json(name, payload)
    mkpath(RESULTS)
    path = joinpath(RESULTS, name)
    open(path, "w") do io
        JSON.print(io, payload, 2)
    end
    @printf("wrote %s\n", path)
    return path
end

const CAVEATS = [
    "window-TDVP with FROZEN infinite environments; readouts only where edge_leak < 1e-3",
    "charge_law is the exact single-time law of Q_hat at each sample, NOT the ordered TPM law of D27",
    "mean escaped charge = <Q>(t_-) - <Q>(t_+) equals the TPM first moment only under D27(LR2)",
    "s is the measured tail density m_stag, not 1 and not a half-integer",
    "chi is the vacuum bond dimension; chi_max is the TDVP2 truncation rank in the window",
]

# ---------------------------------------------------------------------------
function stage_dispersion(; chis = (16, 24, 32), nk = 13)
    ks = collect(range(-pi / 2, pi / 2; length = nk))
    rows = Any[]
    for chi in chis
        sec = kink_sector(LDM.NEEL_POINT; chi = chi)
        Es, _ = kink_dispersion(sec, ks; num = 2)
        # trivial sector at the same momenta, for contrast.  It is not the
        # object of this run and it can stall on a Z₂-broken vacuum, so a failure
        # is recorded as `null` rather than allowed to kill the scan.
        triv = Union{Float64, Nothing}[]
        for k in ks
            try
                E, _ = excitations(sec.H, QuasiparticleAnsatz(), Float64(k),
                                   sec.psiA, sec.envA; num = 1)
                push!(triv, real(E[1]))
            catch err
                @warn "trivial-sector excitation failed" k err
                push!(triv, nothing)
            end
        end
        v, w0 = group_velocity(sec, pi / 4)
        push!(rows, Dict{String, Any}(
            "chi" => chi, "s_tail_density" => sec.s,
            "e_bond_vacuum" => sec.e_bond,
            "k" => ks,
            "omega_kink" => [E[1] for E in Es],
            "omega_kink_2nd" => [length(E) > 1 ? E[2] : nothing for E in Es],
            "omega_trivial_sector" => triv,
            "gap_kink" => minimum(E[1] for E in Es),
            "bandwidth_kink" => maximum(E[1] for E in Es) - minimum(E[1] for E in Es),
            "v_group_at_pi_over_4" => v, "omega_at_pi_over_4" => w0,
        ))
        @printf("chi=%d  s=%.6f  gap=%.6f  bw=%.6f  v(pi/4)=%.6f\n",
                chi, sec.s, rows[end]["gap_kink"], rows[end]["bandwidth_kink"], v)
        write_json("lambdaD-kink-dispersion.json", Dict{String, Any}(
            "stage" => "dispersion", "issue" => "tns-f5r", "wave" => 2,
            "generated" => string(now()),
            "model" => "H = J Σ [SxSx + SySy + Δ SzSz] , spin-1, J = 1, Δ = 2.5, D = 0",
            "sector" => "topological: left_gs = ψ_A (staggered +s), right_gs = ψ_B (−s)",
            "momentum_convention" => "per SITE; ω(k) = ω(k+π), BZ = (−π/2, π/2]",
            "caveats" => CAVEATS, "rows" => rows))
    end
    return rows
end

# ---------------------------------------------------------------------------
function stage_transport(; chi = 16, L = 72, W = 14:58, c0 = 36, x0 = 22.0,
                         sigma = 5.0, k0 = pi / 4, dt = 0.1, nsteps = 140,
                         sample_every = 5, chi_max = 48)
    sec = kink_sector(LDM.NEEL_POINT; chi = chi)
    rows = Any[]
    for dressing in (:qp, :sharp)
        @printf("--- transport, dressing = %s ---\n", dressing)
        r = memory_experiment(sec; L = L, W = W, c0 = c0, x0 = x0, sigma = sigma,
                              k0 = k0, dt = dt, nsteps = nsteps,
                              sample_every = sample_every, chi_max = chi_max,
                              dressing = dressing, verbose = true)
        push!(rows, memory_record(r))
        @printf("  omega(k0)=%.6f  E_packet=%.6f  v_th=%.5f  v_meas=%.5f\n",
                r.omega0, r.packet_energy, r.v_theory, r.v_measured)
        @printf("  dx: X1=%.4f X2=%.4f X3=%.4f   nu=%.4f   coeff=%.5f (2s=%.5f)\n",
                r.dx_X1, r.dx_X2, r.dx_X3, r.nu_mean, r.coefficient_measured, 2 * sec.s)
        write_json("lambdaD-kink-memory.json", Dict{String, Any}(
            "stage" => "transport", "issue" => "tns-f5r", "wave" => 2,
            "generated" => string(now()),
            "protocol" => "λD-KINK-MEM: dressed kink wavepacket carried across a fixed " *
                          "measurement window by window-TDVP",
            "prediction_tested" => "M-INDEX-spec: escaped-charge outcomes on ℤ, and " *
                                   "δx = −(2s)^{-1} Σ_ν ν p_ν with s the measured tail density",
            "caveats" => CAVEATS, "rows" => rows))
    end
    return rows
end

# ---------------------------------------------------------------------------
# Truncation-convergence check: the SAME geometry at three TDVP2 ranks.  The
# numbers that matter (δx from the s-free centroid, the memory coefficient, the
# velocity) are reported at each rank so the χ-dependence is visible rather than
# extrapolated away.
function stage_converge(; chi = 16, L = 48, W = 10:37, c0 = 23, x0 = 18.0,
                        sigma = 3.5, k0 = pi / 4, dt = 0.1, nsteps = 60,
                        sample_every = 5, ranks = (32, 48, 64))
    sec = kink_sector(LDM.NEEL_POINT; chi = chi)
    rows = Any[]
    for cm in ranks
        r = memory_experiment(sec; L = L, W = W, c0 = c0, x0 = x0, sigma = sigma,
                              k0 = k0, dt = dt, nsteps = nsteps,
                              sample_every = sample_every, chi_max = cm)
        push!(rows, Dict{String, Any}(
            "chi" => chi, "chi_max" => cm, "L" => L,
            "dx_X2_centroid" => r.dx_X2, "dx_X1_D13a" => r.dx_X1,
            "nu_mean_escaped_charge" => r.nu_mean,
            "coefficient_measured" => r.coefficient_measured,
            "coefficient_predicted_2s" => 2 * sec.s,
            "v_measured" => r.v_measured, "v_theory_dwdk" => r.v_theory,
            "energy_drift_readout" => r.energy_drift_readout,
            "norm_drift" => maximum(abs.([sm.norm for sm in r.samples] .- 1)),
            "t_minus" => r.t_minus, "t_plus" => r.t_plus))
        @printf("chi_max=%3d  dx_X2=%.5f  coeff=%.6f (2s=%.6f)  v=%.5f  Edrift=%.2e\n",
                cm, r.dx_X2, r.coefficient_measured, 2 * sec.s, r.v_measured,
                r.energy_drift_readout)
        write_json("lambdaD-kink-memory-convergence.json", Dict{String, Any}(
            "stage" => "converge", "issue" => "tns-f5r", "wave" => 2,
            "generated" => string(now()),
            "purpose" => "TDVP2 truncation-rank convergence of the memory numbers",
            "caveats" => CAVEATS, "rows" => rows))
    end
    return rows
end

# ---------------------------------------------------------------------------
function stage_edge(; L = 40, chi = 48, hL = 0.5, hR = -0.5, dt = 0.1,
                    nsteps = 200, sample_every = 10, chi_max = 64)
    rows = Any[]
    for p in (LDE.HALDANE_POINT, LDE.LARGED_POINT)
        @printf("--- edge memory, %s ---\n", p.label)
        r = edge_experiment(p; L = L, chi = chi, hL = hL, hR = hR, dt = dt,
                            nsteps = nsteps, sample_every = sample_every,
                            chi_max = chi_max, verbose = true)
        push!(rows, edge_record(r))
        @printf("  mL(0)=%+.6f  mL(end)=%+.6f  |mL|max=%.6f  sz1: %+.5f -> %+.5f  Edrift=%.2e\n",
                r.mL[1], r.mL[end], maximum(abs, r.mL), r.sz1[1], r.sz1[end],
                maximum(abs.(r.energy .- r.energy[1])))
        write_json("lambdaD-edge-memory.json", Dict{String, Any}(
            "stage" => "edge", "issue" => "tns-f5r", "wave" => 2,
            "generated" => string(now()),
            "protocol" => "λD-EDGE-MEM: ground state with a left boundary field, " *
                          "field switched off at t = 0, left-half magnetisation followed",
            "contrast" => "Haldane has a protected edge spin-½ and keeps the polarisation; " *
                          "large-D has no edge mode and the induced moment decays",
            "caveats" => ["finite open chain: Haldane retention is exact only up to the " *
                          "edge-edge splitting time ~ e^{L/xi}",
                          "the right edge is pinned by a permanent field h_R for the whole run",
                          "h_R = -h_L, so BOTH phases sit in S^z_total = 0 and m_L is a " *
                          "measurement, not half of a conserved total (h_R = +h_L would make " *
                          "m_L = S^z_total/2 identically, a symmetry artifact)",
                          "the large-D RELATIVE retention is a ratio of numerical zeros and is " *
                          "meaningless; quote mL_initial / mL_final / mL_absmax instead",
                          "S^z_total is conserved, so m_L can only change by transport"],
            "rows" => rows))
    end
    return rows
end

# ---------------------------------------------------------------------------
function main(args)
    stages = isempty(args) ? ["dispersion", "converge", "transport", "edge"] : args
    for st in stages
        st == "dispersion" && stage_dispersion()
        st == "converge" && stage_converge()
        st == "transport" && stage_transport()
        st == "edge" && stage_edge()
        st in ("dispersion", "converge", "transport", "edge") ||
            @warn "unknown stage, skipped" stage = st
    end
    return nothing
end

main(ARGS)
