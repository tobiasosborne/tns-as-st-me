# run_lambdaD_phases.jl — wave-1 production runs for the anisotropic spin-1
# λ–D chain (bd tns-f5r).
#
#   julia --project=numerics numerics/scripts/run_lambdaD_phases.jl [stage...]
#
# Stages (default: all three):
#   points   representative point in each phase + the AKLT calibration,
#            at χ = 16, 32, 48, plus a U(1)-graded run for the S^z-resolved
#            entanglement spectrum.   -> results/lambdaD-phase-points.json
#   dsweep   D = 0 … 2 at Δ = 1, crossing the Haldane / large-D transition
#            (D_c ≈ 0.97), at χ = 16, 32, 48.  This is the raw material for
#            the paper's rigidity-dichotomy figure: the bulk string order
#            drifts continuously, the entanglement-spectrum degeneracy does
#            not.                       -> results/lambdaD-D-sweep.json
#   dsweep2  Δ = 0.6 … 3.0 at D = 0 on a TWO-site unit cell, crossing the
#            Haldane / Néel transition (Δ_c ≈ 1.19).
#                                       -> results/lambdaD-delta-sweep.json
#
# Every record is rewritten to disk after EVERY point, so a partial scan is
# still a usable artifact.  Nothing here is a pass/fail test — the assertions
# live in numerics/test/test_lambdaD_groundstate.jl.
#
# HONESTY NOTE.  Near a transition the correlation length is limited by χ, so
# `correlation_length` at χ = 16/32/48 is a finite-entanglement number, not a
# thermodynamic one.  The scan therefore records the SAME point at three bond
# dimensions and leaves the χ-dependence visible in the output rather than
# extrapolating it away.  `converged` and `galerkin` are recorded as measured.

using Printf
using Dates
using JSON

include(joinpath(@__DIR__, "..", "src", "lambdaD_model.jl"))
using .LambdaD

const RESULTS = joinpath(@__DIR__, "..", "results")
const SEED = 20260829
const CHIS = (16, 32, 48)
const RMAX = 64
const TOL = 1.0e-10
const MAXITER = 800

function write_json(path, payload)
    mkpath(dirname(path))
    open(path, "w") do io
        JSON.print(io, payload, 1)
    end
    return path
end

function envelope(question, extra = Dict{String, Any}())
    d = Dict{String, Any}(
        "generated" => string(now()),
        "issue" => "tns-f5r",
        "model" => "H = J Σ_x [Sx Sx + Sy Sy + Δ Sz Sz + K (S·S)^2] + D Σ_x (Sz_x)^2, spin-1, J = 1",
        "question" => question,
        "conventions" => "S^z eigenvalues {+1,0,-1}; string order O^α = − lim_r ⟨S^α_1 (∏ e^{iπ S^α}) S^α_{1+r}⟩, so the AKLT value is +4/9; `correlation_length` = largest sub-unimodular transfer-matrix eigenvalue, per site — the maximum over ALL channels, and null when `rank_deficient` (the state does not fill its bond space and the transfer matrix then has unphysical eigenvalues in the unsupported block); `xi_fit` = exponential fit to the measured connected ⟨S^z S^z⟩, i.e. the LONGITUDINAL channel only, with `xi_fit_r2` its goodness of fit — the two agree at the SU(2)-symmetric Haldane point and differ elsewhere (large-D: 2.8 vs 1.23) because the longest channel there is transverse; es_split1 = (s1−s2)/s1 of the entanglement spectrum.",
        "caveat" => "χ ∈ $(CHIS) on laptop hardware. Near a transition the correlation length and the string order are χ-limited; the same point is recorded at every χ so the drift is visible. `converged` means galerkin ≤ tol, nothing weaker.",
        "seed" => SEED, "tol" => TOL, "maxiter" => MAXITER, "rmax" => RMAX,
        "reference_values" => Dict(
            "AKLT_energy_density" => -2 / 3,
            "AKLT_correlation_length" => 1 / log(3),
            "AKLT_entropy" => log(2),
            "AKLT_string_order" => 4 / 9,
            "Heisenberg_energy_density_literature" => -1.401484038971,
            "Haldane_largeD_transition_D_c_at_Delta1" => 0.97,
            "Haldane_Neel_transition_Delta_c_at_D0" => 1.186,
        ),
    )
    merge!(d, extra)
    return d
end

function run_one(p; chi, unitcell = 1, symmetry = :none)
    res = LambdaD.find_gs(p; chi = chi, unitcell = unitcell,
                          symmetry = symmetry, seed = SEED, tol = TOL,
                          maxiter = MAXITER, rounds = 2)
    d = LambdaD.diagnose(res; rmax = RMAX)
    println(LambdaD.summary_line(d))
    flush(stdout)
    return LambdaD.record(d)
end

# ===========================================================================
# Stage 1: representative points
# ===========================================================================

function stage_points()
    path = joinpath(RESULTS, "lambdaD-phase-points.json")
    rows = Any[]
    payload = envelope(
        "Does one Hamiltonian family carry all three corners — Néel (Z2 SSB), Haldane (SPT), large-D (trivial) — with the diagnostics that separate them?",
        Dict("stage" => "points",
             "expected" => Dict(
                 "Neel" => "|m_stag| ≈ 0.96, O^x = 0, O^z ≠ 0, es_split1 = O(1)",
                 "Haldane" => "m_stag = 0, O^z ≈ O^x ≈ 0.374, es_split1 ≈ 0 (protected doublet)",
                 "largeD" => "m_stag = 0, O^z = O^x = 0, es_split1 = O(1)",
                 "AKLT" => "closed form: e = −2/3, ξ = 1/log 3, S = log 2, O = 4/9")))

    specs = [(LambdaD.NEEL_POINT, 2), (LambdaD.HALDANE_POINT, 1),
             (LambdaD.LARGED_POINT, 1), (LambdaD.AKLT_POINT, 1)]
    for (p, n) in specs, chi in CHIS
        push!(rows, run_one(p; chi = chi, unitcell = n))
        payload["rows"] = rows
        write_json(path, payload)
    end
    # U(1)-graded runs: S^z-resolved entanglement spectrum
    for (p, n) in specs
        push!(rows, run_one(p; chi = 32, unitcell = n, symmetry = :u1))
        payload["rows"] = rows
        write_json(path, payload)
    end
    # the control that shows the Néel SSB is real: a one-site cell cannot
    # represent it and must fail to converge
    push!(rows, run_one(LambdaD.NEEL_POINT; chi = 32, unitcell = 1))
    payload["rows"] = rows
    payload["control"] = "the last row is the Néel point forced onto a ONE-site unit cell: it cannot represent the broken state and is expected NOT to converge; that failure is the evidence that the Z2 breaking is physical."
    write_json(path, payload)
    println("wrote ", path)
    return path
end

# ===========================================================================
# Stage 2: D sweep across Haldane / large-D at Δ = 1
# ===========================================================================

function stage_dsweep()
    path = joinpath(RESULTS, "lambdaD-D-sweep.json")
    rows = Any[]
    payload = envelope(
        "Across the Haldane → large-D transition at Δ = 1, does the bulk string order drift continuously to zero while the entanglement-spectrum degeneracy stays exact until it breaks? (rigidity dichotomy)",
        Dict("stage" => "dsweep", "Delta" => 1.0, "unitcell" => 1,
             "D_values" => collect(0.0:0.1:2.0)))
    for D in 0.0:0.1:2.0, chi in CHIS
        p = LambdaDPoint(; Delta = 1.0, D = D, label = @sprintf("D=%.2f", D))
        push!(rows, run_one(p; chi = chi))
        payload["rows"] = rows
        write_json(path, payload)
    end
    println("wrote ", path)
    return path
end

# ===========================================================================
# Stage 3: Δ sweep across Haldane / Néel at D = 0, two-site cell
# ===========================================================================

function stage_dsweep2()
    path = joinpath(RESULTS, "lambdaD-delta-sweep.json")
    rows = Any[]
    deltas = collect(0.6:0.1:3.0)
    payload = envelope(
        "Across the Haldane → Néel transition at D = 0 (two-site unit cell, so the broken state is representable), where does the staggered magnetisation switch on and the entanglement doublet break?",
        Dict("stage" => "dsweep2", "D" => 0.0, "unitcell" => 2,
             "Delta_values" => deltas))
    for Δ in deltas, chi in CHIS
        p = LambdaDPoint(; Delta = Δ, D = 0.0, label = @sprintf("Δ=%.2f", Δ))
        push!(rows, run_one(p; chi = chi, unitcell = 2))
        payload["rows"] = rows
        write_json(path, payload)
    end
    println("wrote ", path)
    return path
end

# ===========================================================================

function main(args)
    stages = isempty(args) ? ["points", "dsweep", "dsweep2"] : args
    for s in stages
        println("\n=== stage: ", s, " ===")
        s == "points"  && stage_points()
        s == "dsweep"  && stage_dsweep()
        s == "dsweep2" && stage_dsweep2()
    end
end

main(ARGS)
