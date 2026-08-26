# run_spin1_bc_crosscheck.jl — independent cross-check of the Conjecture Bc
# falsifier (bd tns-8e9), theory/TRIANGLE.md §4.
#
#   julia --project=numerics numerics/scripts/run_spin1_bc_crosscheck.jl
#
# Writes numerics/results/spin1-bc-crosscheck.json, rewriting after EVERY run so
# a partial scan is still a usable artifact.
#
# This scan is deliberately METHOD-INDEPENDENT of the primary falsifier scan in
# numerics/results/spin1-bc-falsifier.json:
#
#   (A) soft phase slope   — here: wavepacket COLLISION DYNAMICS on a ring, the
#       soft packet's centroid displacement against a free single-magnon
#       reference, symmetrised in ±k_s and extrapolated in packet width and in
#       k_s².  No S-matrix, no Bethe ansatz, no quantisation enters the
#       measurement.  The analytic spin-S contact algebra of
#       numerics/src/spins_twomagnon.jl is reported alongside as the prediction.
#   (B) memory quantum     — here: a general-spin-S sparse sector truncated by
#       the UP-VARIATION D (numerics/src/spins_memory_sector.jl), with the
#       spin-1/2 case cross-validated against the frozen TriangleMPS shard, and
#       a spin-1/2 control run in the same code path.
#
# PASS CRITERIA ARE FIXED IN THIS FILE BEFORE THE SCAN IS RUN:
#   VERDICT_TOL  = 0.05  absolute, for the soft slope against {1/s, 2}
#   RATIO_TOL    = 0.08  relative, for δx/N_T against −1/s (the 8% criterion
#                        already fixed for the spin-1/2 scan)

using Printf
using Dates

include(joinpath(@__DIR__, "..", "src", "spins_twomagnon.jl"))
include(joinpath(@__DIR__, "..", "src", "spins_memory.jl"))
using .SpinSTwoMagnon
using .SpinSMemory

const OUT = joinpath(@__DIR__, "..", "results", "spin1-bc-crosscheck.json")
const VERDICT_TOL = 0.05
const RATIO_TOL   = 0.08

const analytic = Any[]
const slopes   = Any[]
const memory   = Any[]

_n(x) = isfinite(x) ? @sprintf("%.12g", x) : "null"
_n(x::Integer) = string(x)
_obj(ps) = "{" * join(["\"$k\": " * (v isa AbstractString ? "\"$v\"" : _n(v))
                       for (k, v) in ps], ", ") * "}"

function verdict_slope(measured, twoS)
    bc = 2 / twoS                      # |q_hard|/s
    alt = 2.0                          # spin-independent (the s = 1/2 value)
    abs(measured - bc) < VERDICT_TOL && return twoS == 1 ? "CONSISTENT (s=1/2 control)" :
                                               "Bc SURVIVES"
    abs(measured - alt) < VERDICT_TOL && return "Bc FALSIFIED"
    return "INCONCLUSIVE"
end

function verdict_ratio(ratio, twoS)
    s = twoS / 2
    bc = -1 / s
    abs(ratio - bc) <= RATIO_TOL * abs(bc) && return twoS == 1 ? "CONSISTENT (s=1/2 control)" :
                                                     "Bc SURVIVES"
    abs(ratio + 2.0) <= RATIO_TOL * 2.0 && return "Bc FALSIFIED"
    return "INCONCLUSIVE"
end

function write_results()
    open(OUT, "w") do io
        println(io, "{")
        println(io, "\"generated\": \"", Dates.format(now(), "yyyy-mm-ddTHH:MM:SS"), "\",")
        println(io, "\"issue\": \"tns-8e9\",")
        println(io, "\"role\": \"INDEPENDENT CROSS-CHECK of numerics/results/spin1-bc-falsifier.json, by different methods (wavepacket collision dynamics for A, up-variation-truncated spin-S sector for B)\",")
        println(io, "\"question\": \"Conjecture Bc (theory/TRIANGLE.md section 4): are the S2-2body soft Wigner phase slope and the M-quant memory quantum the same asymptotic-charge datum |q_hard|/s? Both equal 2 at s=1/2; Bc predicts 1 and -1 at s=1, the competing hypothesis predicts 2 and -2 at every s.\",")
        println(io, "\"verdict_tol_slope_absolute\": ", _n(VERDICT_TOL), ",")
        println(io, "\"ratio_tol_relative\": ", _n(RATIO_TOL), ",")
        println(io, "\"A_model\": \"H = -J sum_x (S_x.S_{x+1} - S^2), spin-S isotropic Heisenberg ferromagnet, periodic ring; magnon number n_x = S - S^z_x\",")
        println(io, "\"A_convention\": \"delta = arg S_12(k_s,k_h), argument 1 the SOFT leg (D7); Delta_s = -d(delta)/dk_s is the soft packet's spatial displacement; slope := -Delta_s\",")
        println(io, "\"A_analytic_derivation\": \"free extension Psi(x,y) = A e^{i(k1 x + k2 y)} + B e^{i(k2 x + k1 y)} (NOT symmetrised) plus psi_d(x) = gamma P^x on the doubly occupied configurations. The (x,x) equation gives gamma = (g/t) W / b and the (x,x+1) equation gives g gamma (1+P) = t Sigma (1+P) - J W, with t = JS, g = J sqrt(S(2S-1)), a = 1+z1 z2, b = z1+z2, W = A z2 + B z1, Sigma = A + B. Eliminating gamma: W[(2S-1)a + b] = S Sigma a b, hence S_12 = (S a b - z1 mu)/(z2 mu - S a b) with mu = (2S-1)a + b, and d(delta)/dk_s|_0 = 1/S for every S and every k_h.\",")
        println(io, "\"A_analytic_crosscheck\": \"identical to machine precision (1.1e-15) to the closed form n/(-conj n) reported independently in spin1-bc-falsifier.json\",")
        println(io, "\"A_dynamics_method\": \"two spatially disjoint Gaussian packets on a ring, hard behind soft (D7 incoming configuration); the interacting two-magnon state and two free single-magnon references are evolved in lockstep with KrylovKit; the soft packet's chamber-marginal displacement against the free reference is Delta_s. Symmetrised over +-k_s (kills the O(k_s) term exactly), Richardson-extrapolated in 1/sigma_x^2, then extrapolated to k_s = 0 in k_s^2.\",")
        println(io, "\"A_analytic\": [\n    ", join(analytic, ",\n    "), "\n],")
        println(io, "\"A_dynamics\": [\n    ", join(slopes, ",\n    "), "\n],")
        println(io, "\"B_model\": \"H = -sum_x [ (Jperp/2)(S+S- + h.c.) + Jz Sz Sz ] on N sites, Delta = Jz/Jperp > 1, Jperp = 1, spin S; sites 1 and N frozen at S^z = +S and -S (kink boundary condition)\",")
        println(io, "\"B_truncation\": \"up-variation D = sum_j max(0, n_j - n_{j+1}) <= dmax; D = 0 is exactly the monotone wall manifold of any width, D <= 1 adds one magnon on either side. At S = 1/2, D = (#domain walls - 1)/2, so dmax = 1 is the frozen shard's dwmax = 3 (checked in test_spins_memory.jl).\",")
        println(io, "\"B_estimators\": \"X1 = windowed gradient centroid; X2 = (1/2S) sum_W m(x) + (x_a+x_b)/2 (windowed integrated magnetisation, the Bd3 charge estimator); T = sum_{x >= X+buf}(S + m(x)), R = sum_{x <= X-buf}(S - m(x)). dx from the pre/post trajectory fits differenced at the collision time.\",")
        println(io, "\"B_protocol_note\": \"memory_experiment_s enforces standoff >= buffer + 4 sigma. Without it the packet overlaps the reflected-weight region at t=0, the data-driven pre-window degenerates to a 3-point geometric fallback, and the trajectory fit extrapolates a spurious slope to t_c (an earlier N=72/sigma=3/standoff=14 run read -1.104 for a raw displacement of -1.02).\",")
        println(io, "\"B_runs\": [\n    ", join(memory, ",\n    "), "\n]")
        println(io, "}")
    end
end

# ---------------------------------------------------------------------------
# (A0) the analytic soft slope, all spins, all hard momenta
# ---------------------------------------------------------------------------
println("=== (A0) analytic soft slope d(delta)/dk_s|_0 ===")
for twoS in (1, 2, 3, 4), kh in (0.37, 0.8, 1.1, 1.5, 2.4, 3.0)
    sl = soft_slope_exact(kh, twoS)
    push!(analytic, _obj(["twoS" => twoS, "s" => twoS / 2, "k_h" => kh,
                          "slope_exact" => sl, "one_over_s" => 2 / twoS,
                          "deviation" => sl - 2 / twoS]))
end
@printf("  slope = 1/s to %.2e over 2S = 1..4, k_h in [0.37, 3.0]\n",
        maximum(abs(soft_slope_exact(kh, twoS) - 2 / twoS)
                for twoS in (1, 2, 3, 4), kh in (0.37, 0.8, 1.1, 1.5, 2.4, 3.0)))
write_results()

# ---------------------------------------------------------------------------
# (A) soft slope from pure collision dynamics
# ---------------------------------------------------------------------------
println("=== (A) soft slope from wavepacket collision dynamics ===")
for (twoS, kh) in ((1, 1.5), (2, 0.8), (2, 1.5), (2, 2.4), (3, 1.5))
    t = @elapsed r = soft_slope(; J = 1.0, twoS = twoS, kss = (0.30, 0.20), kh = kh,
                                sigmas = (8.0, 11.0), sep_factor = 10.0, dt = 1.0)
    v = verdict_slope(r.slope, twoS)
    push!(slopes, _obj(["twoS" => twoS, "s" => twoS / 2, "k_h" => kh,
                        "slope_measured" => r.slope, "slope_error" => r.err,
                        "slope_exact_limit" => r.exact_limit,
                        "deviation" => r.slope - r.exact_limit,
                        "bc_prediction" => 2 / twoS, "alt_prediction" => 2.0,
                        "slope_at_ks_0.30" => r.slopes_at[1],
                        "slope_at_ks_0.20" => r.slopes_at[2],
                        "exact_at_ks_0.30" => r.exact_at[1],
                        "exact_at_ks_0.20" => r.exact_at[2],
                        "sigma_x" => "8.0, 11.0", "sep_factor" => 10.0,
                        "N_max" => r.points[end].N, "dim_max" => r.points[end].dim,
                        "norm_drift" => maximum(p.norm_drift for p in r.points),
                        "energy_drift" => maximum(p.energy_drift for p in r.points),
                        "precollision_control" => maximum(p.pre_control for p in r.points),
                        "verdict" => v]))
    @printf("  2S=%d k_h=%.2f  slope = %+.5f +- %.5f  (exact %+.5f, Bc %.4f)  %s  (%.0f s)\n",
            twoS, kh, r.slope, r.err, r.exact_limit, 2 / twoS, v, t)
    flush(stdout)
    write_results()
end

# ---------------------------------------------------------------------------
# (B) memory quantum
# ---------------------------------------------------------------------------
println("=== (B) memory quantum dx/N_T ===")
function memrun(label; twoS, kw...)
    t = @elapsed r = memory_experiment_s(; twoS = twoS, kw...)
    ratio1 = r.dx1 / r.T_final
    ratio2 = r.dx2 / r.T_final
    v = verdict_ratio(ratio1, twoS)
    push!(memory, _obj(["label" => label, "twoS" => twoS, "s" => twoS / 2,
                        "N" => r.params.N, "Delta" => r.params.Delta,
                        "k0" => r.params.k0, "sigma" => r.params.sigma,
                        "standoff" => r.params.standoff, "dmax" => r.params.dmax,
                        "halfwidth" => r.params.halfwidth, "buffer" => r.params.buffer,
                        "dt" => r.params.dt, "tmax" => r.params.tmax, "dim" => r.dim,
                        "transmission" => r.T_final, "reflection" => r.R_final,
                        "trapped" => r.trapped_final,
                        "dx1" => r.dx1, "dx2" => r.dx2, "dx3" => r.dx3,
                        "dx1_over_T" => ratio1, "dx2_over_T" => ratio2,
                        "prediction_minus_one_over_s" => -2 / twoS,
                        "relative_deviation_dx1" => abs(ratio1 / (-2 / twoS) - 1),
                        "relative_deviation_dx2" => abs(ratio2 / (-2 / twoS) - 1),
                        "estimator_spread" => abs(r.dx1 - r.dx2),
                        "momentum_spread_over_k0" => 1 / (2 * r.params.sigma * r.params.k0),
                        "kink_slope_pre" => r.slope_pre1,
                        "kink_slope_post" => r.slope_post1,
                        "norm_drift" => maximum(abs.(r.norms .- 1)),
                        "energy_drift" => maximum(abs.(r.energies .- r.energies[1])),
                        "init_truncation_leakage" => r.leakage_init,
                        "H_truncation_leakage" => r.leakage_H,
                        "verdict" => v]))
    @printf("  %-22s 2S=%d dim=%6d T=%.5f  dx1/T=%+.5f dx2/T=%+.5f  (pred %+.1f)  %s  (%.0f s)\n",
            label, twoS, r.dim, r.T_final, ratio1, ratio2, -2 / twoS, v, t)
    flush(stdout)
    write_results()
    return r
end

# Packet quality.  The frozen S = 1/2 scan already requires the packet's
# momentum spread 1/(2 sigma) to stay well below k0 itself, or the slow
# small-k components never leave the wall.  A first pass at sigma = 2.5 for
# BOTH momenta gave 1/(2 sigma k0) = 0.25 at k0 = 0.8 and read dx1/T = -1.099
# with dx2/T = -0.927 (the two estimators bracketing -1 with a 0.17 spread) --
# a packet-quality artifact, and it appears identically in the S = 1/2 control.
# The slower momentum therefore gets its own, wider-packet geometry, which
# forces a longer standoff (>= buffer + 4 sigma) and a longer chain.
const GEOM = Dict(0.8 => (N = 120, sigma = 5.0, standoff = 26.0, obs_every = 4),
                  1.5 => (N =  80, sigma = 2.5, standoff = 18.0, obs_every = 2))

# main spin-1 grid: two anisotropies x two momenta
for Δ in (3.0, 6.0), k0 in (0.8, 1.5)
    g = GEOM[k0]
    memrun("main-S1-D$(Δ)-k$(k0)"; twoS = 2, N = g.N, Delta = Δ, k0 = k0,
           sigma = g.sigma, standoff = g.standoff, dt = 0.2, halfwidth = 6,
           buffer = 6, obs_every = g.obs_every)
end
# spin-1/2 control through exactly the same code path: must return -2
for Δ in (3.0, 6.0), k0 in (0.8, 1.5)
    g = GEOM[k0]
    memrun("control-Shalf-D$(Δ)-k$(k0)"; twoS = 1, N = g.N, Delta = Δ, k0 = k0,
           sigma = g.sigma, standoff = g.standoff, dt = 0.2, halfwidth = 6,
           buffer = 6, obs_every = g.obs_every)
end
# N-convergence at fixed physics
for N in (72, 80, 88)
    memrun("Nconv-$(N)"; twoS = 2, N = N, Delta = 6.0, k0 = 1.5, sigma = 2.5,
           standoff = 18.0, dt = 0.2, halfwidth = 6, buffer = 6, obs_every = 2)
end
# time-step convergence
memrun("dtconv-0.1"; twoS = 2, N = 80, Delta = 6.0, k0 = 1.5, sigma = 2.5,
       standoff = 18.0, dt = 0.1, halfwidth = 6, buffer = 6, obs_every = 4)
# truncation convergence D <= 1 vs D <= 2 on the smallest workable geometry
for dm in (1, 2)
    try
        memrun("trunc-dmax$(dm)"; twoS = 2, N = 40, Delta = 6.0, k0 = 1.5, sigma = 1.25,
               standoff = 8.0, dt = 0.25, halfwidth = 3, buffer = 3, dmax = dm,
               obs_every = 2)
    catch e
        @warn "trunc-dmax$dm skipped" e
    end
end

@printf("\nwrote %s  (%d analytic, %d slope runs, %d memory runs)\n",
        OUT, length(analytic), length(slopes), length(memory))
