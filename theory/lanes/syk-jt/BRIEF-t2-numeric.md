<!-- LANE BRIEF T2 (numeric): sourced Schwarzian ODE — red-green TDD.
     bd tns-62n. YOUR LANE (create/edit ONLY these files):
       numerics/src/schwarzian_memory.jl
       numerics/test/test_schwarzian_memory.jl
       numerics/results/schwarzian_memory.json
       theory/lanes/syk-jt/t2-numeric.md   (your lane report)
     Do NOT edit numerics/test/runtests.jl, TriangleMPS.jl, CLAIMS,
     definitions, LEDGER, or any other file — put any proposed edits to
     shared files in a MERGE PROPOSALS section of your report. No bd
     operations. Work fully autonomously; do not ask questions. -->

# T2: numerical solve of the sourced two-sided Schwarzian problem

## Context

Read `theory/lanes/reduction/o4-syk-jt-recon.md` §5.2: you are the
numerical half of the decisive computation (T.1)–(T.3). Ground truth for
every equation is local TeX:
`refs/arxiv-1606.01857/GravityReparametrizationsRevised.tex` — sourced
Schwarzian equation C (Sch(t,u))'/t' = − t' T_tz at lines 611–623; SL(2)
charges at 889–900; two-sided state 902–909; bilocal dressing 662–675.
Quote file+line for every equation you implement. A parallel analytic
lane is deriving closed forms; you do NOT have access to its output —
your independence is the point. You will be cross-checked against it.

## The task (red-green TDD, law L1 — failing test FIRST, watch it fail)

Julia, in the existing `numerics/` project (deps available: LinearAlgebra,
Statistics, JSON, Printf, Test — NO new packages; hand-roll RK4/RK45 with
a step-halving convergence gate).

1. **Integrator for (T.1).** State variable: t(u) on the right boundary
   (left boundary unsourced). Rewrite the 4th-order sourced equation as a
   first-order system; integrate through a compactly supported pulse
   T_tz(u) (top-hat and narrow Gaussian profiles, parameterized).
   RED tests first:
   - unsourced thermal saddle t(u) = tan(π u/β) reproduced to 1e-10 over
     several periods (regression against the exact map);
   - SL(2) charges (file lines 889–900) conserved to 1e-8 OUTSIDE the
     pulse support, and their jump across the pulse equals
     ∫ du t' T_tz (1, t, t²) to 1e-6 (quadrature cross-check);
   - integrator order verified by step-halving (measured convergence
     order ≥ expected − 0.2).
2. **Relative frame extraction.** From the post-pulse trajectory, fit the
   late solution to a Möbius transform of a thermal map (new energy E_f);
   extract the relative SL(2) element and Δu_rel. Gauge discipline: fix
   the simultaneous two-sided SL(2) explicitly; only the RELATIVE
   left/right data enters observables. Test: a pure gauge (simultaneous)
   Möbius move changes Δu_rel by < 1e-8.
3. **Observable (T.2).** Two-sided bilocal G_LR(T,T) in the geodesic/
   dressed approximation (dressing rule at file lines 662–675), pulse vs
   equilibrium-at-E_f. δG_LR(T) and Δu_rel(T) on a grid of late T; test
   for plateau vs decay: fit both models (constant; decaying exponential)
   and report which wins, with residuals. NO prejudged answer — a clean
   decay is as valuable as a plateau.
4. **DC identity (T.3).** Discrete Fourier transform of the retarded
   response; compare lim_{ω→0}[−iω δu_rel(ω)] against the late-time
   Δu_rel and against the vertex-normalized soft response (normalization
   from the measured injected charge — nothing fitted). Report the ratio
   and its convergence as ω→0.
5. **Finiteness/exit discipline** (campaign has been burned here): every
   result written to `numerics/results/schwarzian_memory.json` must pass
   an isfinite gate; the test file must FAIL (nonzero exit) on NaN, on
   empty sample sets, and on charge-conservation violation. Never write
   the JSON on a failing run.

Runnable standalone: `julia --project=numerics numerics/test/test_schwarzian_memory.jl`
must exit 0 green / nonzero red. Keep modules 200–500 loc (L2); split the
src file if needed but stay inside your lane's filename prefix
(`schwarzian_memory*.jl`).

## Parameter points (use EXACTLY these, so lanes can be cross-checked)

β = 2π (so the thermal map is tan(u/2)), C ∈ {10, 100}; top-hat pulse
T_tz = ε on u ∈ [0, 0.5] with ε ∈ {0.01, 0.1}; Gaussian pulse
T_tz = ε exp(−(u−0.25)²/(2·0.05²)) with ε = 0.05; late-time grid
T ∈ {2, 5, 10, 20, 40}. Also one balanced (zero-net-energy) pulse:
derivative-of-Gaussian profile, same width, ε = 0.05.

## Output spec

Lane report `theory/lanes/syk-jt/t2-numeric.md`: what was implemented
(file+line quotes for each source equation), test inventory with RED
evidence (the failing-first output), the results table (Δu_rel(T),
plateau-vs-decay verdict per parameter point, T.3 ratio), honest caveats,
MERGE PROPOSALS section (e.g. the runtests.jl include line). Then the
JSON. This lane creates NO claims and changes NO statuses.
