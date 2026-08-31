<!-- LANE BRIEF: finite-N ED rung of the microscopic ladder (bd tns-7wd).
     YOUR LANE (create/edit ONLY): numerics/src/syk_ed.jl (may split as
     syk_ed_*.jl), numerics/test/test_syk_ed.jl,
     numerics/results/syk_ed.json, theory/lanes/syk-jt/ed-rung-report.md.
     No bd operations; shared-file edits only as MERGE PROPOSALS in your
     report. Work fully autonomously; red-green TDD (L1): failing tests
     FIRST, show them failing. -->

# ED rung: the decisive computation at Layer 0 (finite-N, fixed realization)

This is the first computation in the MICROSCOPIC theory: two SYK dots,
exact states, the actual pulse, the actual detector — the Layer-0 bedrock
of `theory/lanes/syk-jt/observables-spec.md` (read it first; it is
binding). The Schwarzian-EFT results to structurally compare against are
the adjudicated claims JT-B-susc / JT-bfly-decay / JT-noplat-abs in
`claims/CLAIMS.md` (read the three rows + the verdict scoping in
`theory/verdicts/syk-jt-joint-critic-r2.md` §8). Inherit the settled
conventions: single synchronization event u_*, energy-balanced pulse as
the claim-bearing protocol, iterated-limit window language. You do NOT
have access to Schwarzian numerical values to fit against — your
independence at Layer 0 is the point; structural agreement/disagreement
is the result.

## Model and state

- Two identical SYK dots (same disorder realization): N_m Majoranas per
  dot, q=4 body random couplings, standard variance normalization (state
  yours explicitly with the J convention). N_m ∈ {8, 10, 12} for the
  main run (Hilbert dim 2^{N_m} via the standard Jordan–Wigner/Clifford
  representation of 2N_m Majoranas — document your rep); one N_m=14
  confirmation point if runtime allows.
- TFD at inverse temperature β: build from full ED of one dot,
  |TFD⟩ ∝ Σ_n e^{−βE_n/2}|n⟩_L ⊗ Θ|n⟩_R with your stated conjugation
  convention Θ. Choose βJ ∈ {5, 10} and DECLARE honestly how narrow the
  near-conformal window is at these sizes — no pretense of the
  Schwarzian regime; the test is structural.
- Fermion parity: respect the superselection of observables-spec Layer 0
  (only even observables measured).

## Protocols

- Pulse protocol: H(t) = H_L + H_R + f(t) O_R with O_R an even hermitian
  right-dot operator (e.g. a random 2-body bilinear; state it) and f(t)
  a compact balanced profile (derivative-Gaussian type) tuned so the
  measured net right-energy change is < 1e-6 · |E_R|; also one
  unbalanced control pulse (labeled formal diagnostic, per the r2
  Objection-9 scope discipline).
- Reference protocol: the unpulsed TFD evolved by H_L + H_R.
- Detector (Layer 0, exactly the allowed algebra): G_LR(T) =
  (1/N_m) Σ_i ⟨ψ_i^L(T) ψ_i^R(T)⟩ and its equal-time grid; report the
  absolute difference δG_LR(T) and the calibrated ratio
  Δu_rel(T) = −δG_LR/∂_T G^eq_LR on a late-T grid inside the declared
  window; ALSO one-sided checks (each side's reduced expectations must
  be pulse-blind for the left dot to 1e-10 — that is a theorem, test it).

## The three decisive questions

- **Q1 (structure).** At fixed single realization: does δG_LR(T) decay
  while Δu_rel(T) flattens within the accessible window — the Layer-0
  echo of JT-noplat-abs / JT-B-susc — or not? Both outcomes are results.
  Fit constant-vs-decay with the same AIC discipline as the Schwarzian
  lane. Beware: at these sizes, recurrences and finite-size fluctuations
  are physics — report the fluctuation band, not just the mean curve.
- **Q2 (self-averaging).** Repeat at ≥5 disorder seeds (list them): is
  the extracted plateau/decay verdict and its magnitude stable across
  realizations (report mean, spread, worst case)? This is the recon's
  disanalogy-5 check — single-realization operationality.
- **Q3 (cost).** Estimate the actual variance of the G_LR estimator at
  each T (shot count for relative error η) — the empirical version of
  the shot-cost formula in t1-analytic ⟨1⟩5.⟨2⟩5.

## Tests (write RED first)

- TFD correctness: one-sided expectations equal Tr(ρ_β ·) to 1e-10 for
  three named even observables; ⟨TFD|H_L−H_R|TFD⟩ small per your Θ
  convention (state the exact expected relation and test it).
- Unpulsed evolution: E_L, E_R, parity conserved to 1e-10; G_LR^eq
  matches its analytic free check where available (state one).
- Left-blindness: pulse on R changes no left-only expectation (1e-10).
- Balanced-pulse energy gate; integrator convergence (step-halving,
  order gate); finiteness/exit discipline — nonzero exit on NaN, empty
  windows, or violated gates; never write JSON on a failing run.

## Output

`theory/lanes/syk-jt/ed-rung-report.md`: conventions (every one stated),
RED evidence, results tables for Q1–Q3 per (N_m, βJ, seed), honest
window discussion, structural comparison to the three JT-* claim rows
(echo / partial echo / conflict, with the caveat that the Schwarzian
window and the ED window barely overlap), MERGE PROPOSALS if any. JSON
through the finiteness gate. Standalone green:
`julia --project=numerics numerics/test/test_syk_ed.jl`. Modules
200–500 loc each.
