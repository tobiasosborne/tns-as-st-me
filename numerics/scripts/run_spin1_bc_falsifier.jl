# run_spin1_bc_falsifier.jl — the two Conjecture Bc falsifiers (bd tns-8e9).
#
#   julia --project=numerics numerics/scripts/run_spin1_bc_falsifier.jl
#
# Writes numerics/results/spin1-bc-falsifier.json, rewriting after every block so
# a partial run is still a usable artifact.
#
# (A) spin-1 FM two-magnon soft phase slope  dδ/dk_s|_0.
#     Theorem S2-2body (FROZEN) gives 2 at s = 1/2.  Conjecture Bc says the
#     coefficient is |q_hard|/s, hence 1 at s = 1.  Measured two independent
#     ways: exact ring spectra (ansatz-free) and wavepacket displacement.
# (B) spin-1 easy-axis memory quantum  δx/N_T  (prediction P8: -1/s = -1).
#
# DECISION BAND, fixed in advance and identical to the criterion already used in
# numerics/results/memory-scan-1.json: 8% (relative for the memory ratio,
# absolute for the soft slope).  Bc SURVIVES if the s = 1 numbers sit at 1 and
# -1; Bc is FALSIFIED if they sit at 2 and -2.

using Printf
using Dates

include(joinpath(@__DIR__, "..", "src", "spin1_twomagnon.jl"))
include(joinpath(@__DIR__, "..", "src", "spin1_memory.jl"))
using .Spin1TwoMagnon
using .Spin1Memory

const OUT = joinpath(@__DIR__, "..", "results", "spin1-bc-falsifier.json")
const BAND = 0.08

jn(x::Real) = isfinite(x) ? @sprintf("%.12g", x) : "null"
jn(x::Integer) = string(x)
obj(ps) = "{" * join(["\"$k\": " * (v isa AbstractString ? "\"$v\"" : jn(v))
                      for (k, v) in ps], ", ") * "}"

const ring_rows = String[]
const ring_sum = String[]
const dyn_rows = String[]
const dyn_sum = String[]
const mem_rows = String[]

function write_results()
    mkpath(dirname(OUT))
    open(OUT, "w") do io
        println(io, "{")
        println(io, "\"generated\": \"", Dates.format(now(), "yyyy-mm-ddTHH:MM:SS"), "\",")
        println(io, "\"issue\": \"tns-8e9\",")
        println(io, "\"question\": \"Conjecture Bc (theory/TRIANGLE.md section 4): is the soft Wigner phase slope of Theorem S2-2body, and the memory quantum of Theorem M-quant, the same asymptotic-charge datum |q_hard|/s? Both are 2 at s=1/2; Bc predicts 1 and -1 at s=1.\",")
        println(io, "\"decision_band\": ", jn(BAND), ",")
        println(io, "\"A_model\": \"H = -J sum_x (S_x.S_{x+1} - S^2), spin-S isotropic Heisenberg ferromagnet, periodic ring; magnon number n_x = S - S^z_x\",")
        println(io, "\"A_convention\": \"delta = arg S_12(k_s,k_h) with argument 1 the SOFT leg (D7); Delta_s = -d(delta)/d k_s is the soft packet's spatial displacement\",")
        println(io, "\"A_analytic\": \"contact solution of the spin-S two-magnon problem gives S_12 = n/(-conj n) with n = 2S cos(K/2) cos q - e^{iq}[(2S-1)cos(K/2) + cos q], K = k1+k2, q = (k1-k2)/2; expanding at k_s = 0 gives d(delta)/dk_s|_0 = 1/S with all hard dependence cancelling\",")
        println(io, "\"A_ring_method\": \"ansatz-free: exact total-momentum-block spectra of the two-magnon sector, each continuum level inverted through E = omega(k1)+omega(k2), k1+k2 = K, then Bethe-Yang N k_s = 2 pi n_s + delta with n_s = 1\",")
        println(io, "\"A_ring_runs\": [\n  ", join(ring_rows, ",\n  "), "\n],")
        println(io, "\"A_ring_summary\": [\n  ", join(ring_sum, ",\n  "), "\n],")
        println(io, "\"A_dynamical_runs\": [\n  ", join(dyn_rows, ",\n  "), "\n],")
        println(io, "\"A_dynamical_summary\": [\n  ", join(dyn_sum, ",\n  "), "\n],")
        println(io, "\"B_model\": \"H = -sum_x [ (Jperp/2)(S+S- + h.c.) + Jz Sz Sz ], Delta = Jz/Jperp > 1, Jperp = 1, spin s, frozen boundary spins (S^z = +s on site 1, -s on site N)\",")
        println(io, "\"B_notes\": \"truncation is by D = sum_x max(0, n_x - n_{x+1}), the number of excitations above a pure wall (D = (domain walls - 1)/2 at s = 1/2, so dmax=1 reproduces dwmax=3 configuration for configuration); wall coordinate X2 = (sum_W <S^z>)/(2s) + (x_a+x_b)/2; T and R count magnon NUMBER; prediction P8: dx/N_T = -1/s\",")
        println(io, "\"B_runs\": [\n  ", join(mem_rows, ",\n  "), "\n]")
        println(io, "}")
    end
end

# ===========================================================================
# (A1) ansatz-free ring extraction
# ===========================================================================

println("=== (A1) ring spectra, ansatz-free soft slope ===")
const RING_NS = (60, 90, 120, 180, 240, 360, 480)
for S in (0.5, 1.0, 1.5, 2.0), kh in (0.8, 1.5, 2.4)
    res = soft_slope_rings(S; kh_target = kh, Ns = RING_NS, J = 1.0)
    for r in res.rows
        push!(ring_rows, obj(["S" => r.S, "k_h_target" => kh, "N" => r.N, "m" => r.m,
                              "K" => r.K, "E" => r.E, "k_s" => r.ks, "k_h" => r.kh,
                              "delta" => r.delta, "delta_over_ks" => r.slope,
                              "delta_analytic" => soft_phase(r.ks, r.kh, r.S),
                              "block_levels" => r.nlevels]))
    end
    push!(ring_sum, obj(["S" => S, "k_h_target" => kh,
                         "slope_extrapolated" => res.slope, "error" => res.err,
                         "fit_slope_in_ks" => res.fit_slope,
                         "fit_residual" => res.resid,
                         "pairwise_spread" => res.spread,
                         "prediction_1_over_S" => 1 / S,
                         "deviation_from_1_over_S" => res.slope - 1 / S,
                         "N_values" => "$(RING_NS)"]))
    @printf("S=%.1f k_h=%.2f  slope=%.6f +- %.6f   (1/S = %.4f)\n",
            S, kh, res.slope, res.err, 1 / S)
    flush(stdout)
end
write_results()

# ===========================================================================
# (A2) wavepacket displacement
# ===========================================================================

println("\n=== (A2) wavepacket collisions, dynamical soft slope ===")
# Two k_s windows.  `hard` is the window used by the frozen spin-1/2 scan; over
# it -∂δ/∂k_s is strongly curved, so a straight-line extrapolation to k_s = 0
# undershoots by a few percent.  `soft` sits inside the soft region proper.  Both
# are reported; the sharper, extrapolation-free statement is the per-k_s
# agreement with the analytic derivative, recorded as `max_rel_dev_pointwise`.
const DYN_GRIDS = (("hard-window", (0.10, 0.15, 0.20, 0.30)),
                   ("soft-window", (0.03, 0.05, 0.08, 0.12)))
for S in (1.0, 0.5), (glabel, grid) in DYN_GRIDS
    t = @elapsed res = soft_slope_dynamical(; S = S, J = 1.0, kh = 1.5,
                                            ks_values = grid,
                                            sigmas = (8.0, 11.0, 14.0),
                                            sep_factor = 10.0, dt = 1.0)
    reldev = 0.0
    for r in res.rows
        reldev = max(reldev, abs(r.minus_delta_s + r.pred_exact) / abs(r.pred_exact))
        push!(dyn_rows, obj(["S" => r.S, "window" => glabel, "k_s" => r.ks,
                             "k_h" => r.kh,
                             "minus_delta_s_extrapolated" => r.minus_delta_s,
                             "error" => r.err,
                             "raw_sigma8" => r.raw[1], "raw_sigma11" => r.raw[2],
                             "raw_sigma14" => r.raw[3],
                             "packet_avg_prediction" => r.pred_avg,
                             "pointwise_prediction" => r.pred_exact,
                             "precollision_control" => r.pre_control,
                             "N" => r.N, "dim" => r.dim,
                             "norm_drift" => r.norm_drift,
                             "energy_drift" => r.energy_drift]))
    end
    push!(dyn_sum, obj(["S" => S, "window" => glabel, "k_h" => 1.5,
                        "k_s_values" => "$(grid)",
                        "slope_extrapolated" => res.slope, "error" => res.err,
                        "fit_slope_in_ks" => res.fit_slope,
                        "fit_residual" => res.resid,
                        "max_rel_dev_pointwise" => reldev,
                        "prediction_1_over_S" => 1 / S,
                        "deviation_from_1_over_S" => res.slope - 1 / S,
                        "seconds" => t]))
    @printf("S=%.1f %-12s dynamical slope=%.6f +- %.6f  (1/S = %.4f)  max pointwise dev %.2e  [%.0f s]\n",
            S, glabel, res.slope, res.err, 1 / S, reldev, t)
    flush(stdout)
    write_results()
end

# ===========================================================================
# (B) spin-1 easy-axis memory quantum
# ===========================================================================

println("\n=== (B) magnon through a spin-1 kink ===")
function memrun!(label; kwargs...)
    # Guard: the s = 3/2, dmax = 1 sector grows fast enough in L that an
    # unguarded N = 100 run needs ~24 GB.  Skip rather than die, and say so.
    local r
    try
        t0 = @elapsed r = memory_experiment(; kwargs...)
        return _record!(label, r, t0)
    catch e
        @printf("%-22s SKIPPED: %s\n", label, sprint(showerror, e))
        flush(stdout)
        return nothing
    end
end

function _record!(label, r, t)
    push!(mem_rows, "{\"label\": \"$label\", \"seconds\": " * jn(t) *
                    ", \"result\": " * Spin1Memory.to_json(r; trajectory = false) * "}")
    @printf("%-22s N=%3d s=%.1f D=%5.2f k0=%.2f dmax=%d dim=%7d dx2=%+8.5f T=%.5f trap=%.2e  dx2/T=%+8.5f  dx2/dT=%+8.5f  (pred %+.1f) [%.0f s]\n",
            label, r.params.N, r.params.spin, r.params.Delta, r.params.k0,
            r.params.dmax, r.dim, r.dx2, r.T_final, r.trapped_final, r.ratio2,
            r.ratio2_sub, r.params.prediction_ratio, t)
    flush(stdout)
    write_results()
    return r
end

# main spin-1 grid: three anisotropies x three momenta
for Δ in (2.0, 3.0, 6.0), k0 in (0.8, 1.2, 1.8)
    memrun!("s1-D$(Δ)-k$(k0)"; N = 120, s = 1.0, Delta = Δ, k0 = k0, sigma = 5.0,
            standoff = 30.0, dmax = 1, dt = 0.4, obs_every = 2)
end

# spin-1/2 control on exactly the same code path
for Δ in (2.0, 3.0), k0 in (0.8, 1.2)
    memrun!("s05-D$(Δ)-k$(k0)"; N = 120, s = 0.5, Delta = Δ, k0 = k0, sigma = 5.0,
            standoff = 30.0, dmax = 1, dt = 0.4, obs_every = 2)
end

# spin-3/2: the law -1/s should continue.  N is small because the dmax = 1
# sector grows much faster at nmax = 3 (232k at N = 60, 436k at N = 70, and an
# N = 100 attempt was OOM-killed at 24 GB).
memrun!("s15-D3.0-k1.2"; N = 64, s = 1.5, Delta = 3.0, k0 = 1.2, sigma = 2.5,
        standoff = 13.0, dmax = 1, dt = 0.25, halfwidth = 4, buffer = 4,
        trapped_tol = 1e-3, obs_every = 1)

# N-convergence at fixed physics
for N in (100, 120, 140)
    memrun!("s1-Nconv-$(N)"; N = N, s = 1.0, Delta = 3.0, k0 = 1.2, sigma = 4.0,
            standoff = 24.0, dmax = 1, dt = 0.4, obs_every = 2)
end

# truncation convergence.  dmax = 1 grows like L^2, dmax = 2 like L^4 (4.1e6
# already at N = 60 for s = 1), so the s = 1 comparison is run on the longest
# chain that still fits: N = 46, Delta = 6, where the dmax = 1 run separates
# cleanly (trapped = 4e-4).  The cheap s = 1/2 comparison is run at the
# production geometry.  Note dmax = 2 admits virtual pairs, so its dressed kink
# starts with T,R slightly off (0,1); `ratio_dx2_over_deltaT` is the
# baseline-subtracted number, identical to `ratio_dx2_over_T` at dmax = 1.
for dm in (1, 2)
    memrun!("s05-trunc-dmax$(dm)"; N = 56, s = 0.5, Delta = 3.0, k0 = 1.2, sigma = 2.5,
            standoff = 14.0, dmax = dm, dt = 0.25, halfwidth = 5, buffer = 5,
            kink_state = :sharp, trapped_tol = 1e-3, obs_every = 1)
end
for dm in (1, 2)
    memrun!("s1-trunc-dmax$(dm)"; N = 46, s = 1.0, Delta = 6.0, k0 = 1.5, sigma = 2.0,
            standoff = 11.0, dmax = dm, dt = 0.25, halfwidth = 4, buffer = 4,
            trapped_tol = 1e-3, obs_every = 1)
end

# state-preparation check: sharp (monotone) vs dressed initial wall
memrun!("s1-prep-sharp"; N = 120, s = 1.0, Delta = 3.0, k0 = 1.2, sigma = 5.0,
        standoff = 30.0, dmax = 1, dt = 0.4, obs_every = 2, kink_state = :sharp)

@printf("\nwrote %s\n", OUT)
