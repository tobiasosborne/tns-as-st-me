# Finite-ℕ SYK ED rung: Layer-0 report

## Outcome

The prescribed main campaign is complete: (N_m=8,10,12),
βJ∈{5,10}, and seeds 1701–1705 (30 points), plus the allowed
(N_m=14,βJ=10), seed-1701 confirmation.  The claim-bearing pulse passes
the measured right-energy gate at every point.  The standalone suite is green
(141/141), and the complete per-time data are in
`numerics/results/syk_ed.json`.

The scientific result is negative but informative.  On (N_m=8), all ten
absolute differences select an exponential over a constant, and seven of ten
calibrated ratios select a constant: a small-size echo of JT-noplat-abs and
JT-B-susc.  That pattern does not survive increasing (N_m).  Every one of
the twenty (N_m=10,12) points, and the (N_m=14) confirmation, selects a
constant rather than a decaying absolute difference on the same accessible
window.  The calibrated magnitude and sometimes its sign vary strongly with
the disorder realization.  Thus the accessible finite-size result is a
**conflict**, not evidence for a microscopic plateau theorem and not a
refutation of the differently ordered large-(C)-first Schwarzian claims.

## Conventions and operational scope

1. **Clifford representation.**  On one dot,
   γ_{2a−1}=Z₁⋯Z_{a−1}X_a and
   γ_{2a}=Z₁⋯Z_{a−1}Y_a, with χ_i=γ_i/√2, so
   {χ_i,χ_j}=δ_ij.  One dot has dimension 2^{N_m/2}; the two-dot
   Clifford representation has dimension 2^{N_m}.  Right odd operators carry
   the left Klein/parity factor, so the measured cross bilinear is even.
2. **SYK normalization.**  With J=1,
   (H=i^{q/2}\sum_{i<j<k<l}J_{ijkl}\chi_i\chi_j\chi_k\chi_l), q=4, and
   independent real Gaussian couplings of mean zero and variance
   (3!J^2/N_m^3).  The dots use the same realization and
   (H_R=\overline{H_L}).
3. **TFD convention.**  Θ=exp(iπP/4)K, where K is computational-basis
   conjugation and P is one-dot fermion parity.  Thus
   ∣TFD⟩∝Σ_n exp(−βE_n/2)∣n⟩_L⊗Θ∣n⟩_R.  The parity twist is
   the fermionic Klein phase; it leaves both thermal marginals unchanged and
   makes the even Hermitian detector below nonzero.  In this convention
   ((H_L-H_R)|TFD\rangle=0) exactly.
4. **Allowed algebra.**  Only parity-even quantities are reported: (H_L),
   (H_R), parity, one-dot even bilinears, and the two-sided bilocal.  No
   reparametrization field, frame label, or microscopic SL(2) charge is used.
5. **Detector phase.**  The JSON reports the real Hermitian representative
   (G_{LR}=-iN_m^{-1}\sum_i\langle\chi_i^L\chi_i^R\rangle).  This differs
   from the brief's anti-Hermitian (N_m^{-1}\sum_i\langle\chi_i^L\chi_i^R\rangle)
   only by the fixed factor −i, which cancels in
   (Δu_{rel}=-δG_{LR}/∂_TG^{eq}_{LR}).
6. **Pulse operator.**  For each disorder seed,
   (O=\|\widetilde O\|^{-1}\widetilde O),
   (~O=Σ_{i<j}k_{ij}iχ_iχ_j), with a fixed seed-derived independent
   Gaussian coefficient stream.  The right source is its conjugate.
7. **Balanced profile.**  On support [0,1],
   (f(t)=A x e^{-x^2/2}), x=(t−0.5)/0.12, and f=0 outside.  Its
   coordinate area vanishes by antisymmetry.  Starting from A=0.1, A is
   halved until the measured post-pulse
   ∣ΔE_R∣/∣E_R∣<10^{−6} for both temperatures of that realization.
   The accepted A is 0.05 except for (8,1702) and (10,1705), where it is
   0.025.  The observed worst energy ratio is 5.7304×10^{−7}.
8. **Unbalanced control.**  The control replaces the derivative Gaussian by
   (Ae^{-x^2/2}) at the same A.  Its energy ratios are
   3.10×10^{−5}–1.22×10^{−4}.  It is recorded only as a formal diagnostic;
   it licenses no same-energy detector or memory conclusion.
9. **Evolution and convergence.**  The time-dependent right unitary uses a
   unitary midpoint Strang step with dt=0.01.  Step halving at
   dt=0.04,0.02,0.01 gives minimum observed order 1.9556 (gate 1.75),
   fine differences below 2×10^{−5}, and maximum unitarity error
   1.3021×10^{−11}.
10. **Synchronization and window.**  There is one synchronization event,
    u_*=1 at pulse end, and no later resynchronization.  The absolute detector
    times are T=1.5,2.0,…,5.0, hence T−u_*=0.5,…,4.0 in J^{-1}.
    This is a short finite-N diagnostic; recurrences are not excluded.
11. **Reference and calibration.**  The reference is the same TFD evolved by
    (H_L+H_R) without a pulse.  The equilibrium derivative is evaluated
    analytically from ẊC=−i(HC+CH), not by differencing the two protocols.
12. **AIC.**  On the same eight-point grid, the constant model has one
    parameter and the decay model (ae^{-λ(T-T_0)}) has two.  For each,
    AIC=n log(RSS/Σy²)+2k.  `exp/con` below means exponential wins for
    ∣δG∣ and constant wins for Δu_rel.
13. **Shot cost.**  The exact pure-state variance is
    Var(G)=⟨G²⟩−⟨G⟩².  For independent pulsed and reference
    preparations, the reported 10% relative-error estimate is
    (n=(Var_p+Var_{eq})/[0.1^2(δG)^2]), before integer rounding.

There is no parametrically controlled near-conformal window here.  The usual
desideratum (1\ll\beta J\ll N_m) cannot be cleanly met by
βJ∈{5,10} at N_m≤14.  In particular, the eight detector times do not
implement the Schwarzian iterated limit (C→∞) first and then
κ(T−u_*)→∞ with (T−u_*)/C→0.  No permanence claim is made.

## Red-green TDD evidence

The test file was written and saved before the implementation existed.  The
first standalone run was RED with exit code 1; its output was:

```text
$ julia --project=numerics numerics/test/test_syk_ed.jl
ERROR: LoadError: SystemError: opening file "/home/tobias/Projects/tns-as-st-me/numerics/src/syk_ed.jl": No such file or directory
Stacktrace:
 [1] include(mapexpr::Function, mod::Module, _path::String)
   @ Base ./Base.jl:307
 [2] top-level scope
   @ ~/Projects/tns-as-st-me/numerics/test/test_syk_ed.jl:10
 [3] include(mod::Module, _path::String)
   @ Base ./Base.jl:306
 [4] exec_options(opts::Base.JLOptions)
   @ Base ./client.jl:317
 [5] _start()
   @ Base ./client.jl:550
in expression starting at /home/tobias/Projects/tns-as-st-me/numerics/test/test_syk_ed.jl:10
```

After implementation and repair, the same command is GREEN:

```text
Test Summary:                | Pass  Total   Time
finite-N two-dot SYK ED rung |  141    141  19.8s
```

The tests name three even TFD observables (H, P, and iχ₁χ₂), check
each marginal against Tr(ρ_β O) to 10^{−10}, and check the exact
energy-relation vector residual.  The unpulsed tests conserve E_L, E_R, and
parity to 10^{−10}.  For the analytic free check H=0, the parity-twisted
fermionic maximally entangled state gives (G_{LR}(T)=1/2) exactly.  The
largest measured left-reduced-state change in the campaign is
3.4947×10^{−13}.  Poisoned NaN, empty-window, energy-gate, and order-gate
child runs all exit nonzero and leave no requested JSON file.

## Q1 and Q3: per-point results

The tail band is the mean ± sample standard deviation over T=3.5,4,4.5,5.
`fit` is ∣δG∣/Δu_rel.  Variance and shot columns give the range over all
eight times; the JSON contains every time-resolved value.

| N_m | βJ | seed | A | ∣ΔE_R/E_R∣ | tail ∣δG∣ | tail Δu_rel | fit | Q1 | Var_p range | 10% shots range |
|---:|---:|---:|---:|---:|---:|---:|:---:|:---|---:|---:|
| 8 | 5 | 1701 | .05 | 3.35e-7 | 1.10e-7 ± 4.20e-8 | 3.35e-6 ± 1.07e-6 | exp/con | echo | .0155–.0634 | 2.21e14–7.17e14 |
| 8 | 10 | 1701 | .05 | 3.70e-7 | 1.03e-7 ± 2.25e-8 | 3.16e-6 ± 4.66e-7 | exp/con | echo | .0240–.0628 | 4.81e14–9.39e14 |
| 8 | 5 | 1702 | .025 | 2.01e-7 | 5.24e-9 ± 6.24e-9 | 3.38e-8 ± 5.00e-7 | exp/exp | partial | .00995–.0626 | 2.00e15–2.62e18 |
| 8 | 10 | 1702 | .025 | 2.37e-7 | 1.61e-8 ± 3.40e-9 | 3.42e-6 ± 3.32e-6 | exp/con | echo | .0258–.0562 | 8.13e15–2.75e16 |
| 8 | 5 | 1703 | .05 | 3.09e-7 | 5.03e-8 ± 5.07e-8 | 2.01e-6 ± 1.02e-6 | exp/con | echo | .00136–.0631 | 1.94e14–1.09e16 |
| 8 | 10 | 1703 | .05 | 3.38e-7 | 5.59e-8 ± 3.53e-8 | 3.96e-6 ± 1.91e-6 | exp/con | echo | .00849–.0576 | 3.88e14–5.73e15 |
| 8 | 5 | 1704 | .05 | 4.22e-7 | 1.49e-8 ± 2.04e-8 | 6.08e-8 ± 1.16e-6 | exp/exp | partial | .0240–.0625 | 3.13e14–2.10e19 |
| 8 | 10 | 1704 | .05 | 4.35e-7 | 2.72e-8 ± 9.35e-9 | 1.08e-6 ± 5.31e-8 | exp/exp | partial | .0330–.0604 | 2.22e15–1.74e16 |
| 8 | 5 | 1705 | .05 | 2.11e-7 | 3.10e-8 ± 1.88e-8 | 3.26e-6 ± 1.76e-6 | exp/con | echo | .0216–.0637 | 5.97e14–1.46e16 |
| 8 | 10 | 1705 | .05 | 2.35e-7 | 5.06e-8 ± 6.94e-9 | 2.02e-6 ± 3.46e-7 | exp/con | echo | .0306–.0632 | 1.99e15–3.21e15 |
| 10 | 5 | 1701 | .05 | 3.99e-7 | 4.57e-7 ± 6.65e-9 | −7.46e-5 ± 6.60e-5 | con/con | conflict | .0189–.0433 | 1.79e13–3.44e14 |
| 10 | 10 | 1701 | .05 | 4.68e-7 | 6.46e-7 ± 5.18e-7 | 5.04e-5 ± 6.97e-5 | con/con | conflict | .0212–.0385 | 2.39e12–1.36e14 |
| 10 | 5 | 1702 | .05 | 5.04e-7 | 5.85e-7 ± 1.80e-7 | 4.45e-5 ± 2.18e-5 | con/con | conflict | .0263–.0447 | 8.17e12–6.66e14 |
| 10 | 10 | 1702 | .05 | 5.73e-7 | 6.87e-7 ± 1.46e-7 | 3.44e-5 ± 1.38e-5 | con/con | conflict | .0301–.0439 | 9.78e12–2.01e16 |
| 10 | 5 | 1703 | .05 | 4.78e-7 | 2.85e-6 ± 5.74e-7 | 8.55e-4 ± 7.30e-4 | con/con | conflict | .0221–.0433 | 3.61e11–3.25e13 |
| 10 | 10 | 1703 | .05 | 4.81e-7 | 1.93e-6 ± 1.32e-7 | 1.84e-4 ± 8.71e-5 | con/con | conflict | .0269–.0413 | 1.37e12–2.33e13 |
| 10 | 5 | 1704 | .05 | 4.80e-7 | 5.63e-6 ± 6.53e-7 | 6.48e-4 ± 3.35e-4 | con/con | conflict | .0205–.0437 | 1.14e11–3.94e14 |
| 10 | 10 | 1704 | .05 | 5.36e-7 | 8.19e-6 ± 1.49e-6 | 7.09e-4 ± 4.17e-4 | con/con | conflict | .0207–.0393 | 4.92e10–3.45e15 |
| 10 | 5 | 1705 | .025 | 2.61e-7 | 1.01e-6 ± 1.37e-7 | −4.99e-5 ± 1.64e-5 | con/con | conflict | .0258–.0469 | 4.43e12–2.12e15 |
| 10 | 10 | 1705 | .025 | 3.04e-7 | 6.11e-7 ± 3.79e-7 | 1.54e-5 ± 4.15e-5 | con/con | conflict | .0288–.0466 | 4.69e12–9.53e13 |
| 12 | 5 | 1701 | .05 | 3.31e-7 | 1.29e-6 ± 2.79e-7 | −4.90e-5 ± 1.94e-5 | con/con | conflict | .0278–.0348 | 2.67e12–1.01e15 |
| 12 | 10 | 1701 | .05 | 3.39e-7 | 1.48e-6 ± 2.66e-7 | −5.19e-5 ± 8.36e-6 | con/con | conflict | .0309–.0351 | 2.15e12–2.15e16 |
| 12 | 5 | 1702 | .05 | 3.63e-7 | 2.18e-6 ± 5.38e-7 | −8.42e-5 ± 4.02e-5 | con/con | conflict | .0292–.0348 | 8.86e11–3.63e15 |
| 12 | 10 | 1702 | .05 | 3.64e-7 | 3.85e-6 ± 1.07e-6 | −1.49e-4 ± 6.84e-5 | con/con | conflict | .0316–.0359 | 2.93e11–5.03e14 |
| 12 | 5 | 1703 | .05 | 3.82e-7 | 5.59e-7 ± 5.24e-7 | 3.08e-5 ± 5.05e-5 | con/con | conflict | .0316–.0360 | 4.03e12–2.91e17 |
| 12 | 10 | 1703 | .05 | 3.98e-7 | 5.63e-7 ± 3.79e-7 | −2.94e-6 ± 2.96e-5 | con/con | conflict | .0351–.0377 | 7.40e12–7.99e15 |
| 12 | 5 | 1704 | .05 | 3.98e-7 | 2.32e-6 ± 3.04e-7 | 8.74e-5 ± 3.40e-5 | con/con | conflict | .0288–.0350 | 8.35e11–2.77e15 |
| 12 | 10 | 1704 | .05 | 4.29e-7 | 3.02e-6 ± 5.62e-7 | 1.22e-4 ± 4.89e-5 | con/con | conflict | .0318–.0357 | 5.11e11–3.42e16 |
| 12 | 5 | 1705 | .05 | 4.77e-7 | 2.02e-6 ± 3.91e-7 | −1.16e-4 ± 8.10e-5 | con/con | conflict | .0280–.0348 | 1.06e12–3.34e14 |
| 12 | 10 | 1705 | .05 | 5.34e-7 | 4.02e-6 ± 1.97e-6 | −2.18e-4 ± 1.63e-4 | con/con | conflict | .0292–.0345 | 1.58e11–2.19e14 |

The (N_m=14,βJ=10), seed-1701 confirmation has
∣δG∣=(1.290±0.763)×10^{−6},
Δu_rel=(4.458±3.147)×10^{−5}, constant/constant AIC winners, and
therefore the same conflict verdict.  Its energy ratio is 4.102×10^{−7}
and observed integrator order is 1.9584.

For concreteness, the actual per-time estimator entries at the first point
(8,5,1701) are:

| T | Var_p(G) | Var_eq(G) | shots for 10% δG |
|---:|---:|---:|---:|
| 1.5 | .0606560 | .0606560 | 2.863e14 |
| 2.0 | .0633972 | .0633972 | 2.320e14 |
| 2.5 | .0583607 | .0583607 | 2.210e14 |
| 3.0 | .0478796 | .0478796 | 2.343e14 |
| 3.5 | .0360623 | .0360623 | 2.734e14 |
| 4.0 | .0261953 | .0261952 | 3.523e14 |
| 4.5 | .0195049 | .0195049 | 4.959e14 |
| 5.0 | .0154980 | .0154980 | 7.165e14 |

Across all 240 main-grid time samples, Var_p ranges from 1.364×10^{−3}
to 6.374×10^{−2}, while the 10% δG shot estimate ranges from
4.916×10^{10} to 2.098×10^{19}.  This cost is part of the result: imposing
the microscopic energy-balance gate makes the two-protocol difference far
smaller than the intrinsic single-shot fluctuations.

## Q2: disorder self-averaging

The plateau column is the across-seed mean of each row's tail mean.  Magnitude
statistics use the absolute tail means and therefore do not hide sign changes.

| N_m | βJ | stable Q1? | seed verdicts | mean Δu | sd Δu | mean ∣Δu∣ | sd ∣Δu∣ | worst ∣Δu∣ | decay fraction |
|---:|---:|:---:|:---|---:|---:|---:|---:|---:|---:|
| 8 | 5 | no | echo, partial, echo, partial, echo | 1.74e-6 | 1.64e-6 | 1.74e-6 | 1.64e-6 | 3.35e-6 | 1.0 |
| 8 | 10 | no | echo, echo, echo, partial, echo | 2.73e-6 | 1.16e-6 | 2.73e-6 | 1.16e-6 | 3.96e-6 | 1.0 |
| 10 | 5 | yes | conflict ×5 | 2.85e-4 | 4.35e-4 | 3.34e-4 | 3.88e-4 | 8.55e-4 | 0.0 |
| 10 | 10 | yes | conflict ×5 | 1.98e-4 | 2.93e-4 | 1.98e-4 | 2.93e-4 | 7.09e-4 | 0.0 |
| 12 | 5 | yes | conflict ×5 | −2.62e-5 | 8.38e-5 | 7.35e-5 | 3.36e-5 | 1.16e-4 | 0.0 |
| 12 | 10 | yes | conflict ×5 | −5.99e-5 | 1.32e-4 | 1.09e-4 | 8.39e-5 | 2.18e-4 | 0.0 |

The AIC verdict is qualitatively stable only after the apparent (N_m=8)
echo disappears.  The extracted magnitude is not self-averaging on these
sizes: spreads are comparable to means, and the N_m=12 calibrated ratio
changes sign across realizations.  This directly fails the desired
single-realization stability check, even though every listed realization is
itself an operational Layer-0 experiment.

## Structural comparison with the adjudicated JT rows

| JT row | finite-N classification | reason |
|:---|:---|:---|
| JT-B-susc | **partial echo** | A constant Δu_rel wins often (including every N_m=10,12 point), but it is paired with nondecaying ∣δG∣ at N_m≥10, has large fluctuation bands, changes sign, and is not self-averaging.  No stable microscopic susceptibility is extracted. |
| JT-bfly-decay | **partial echo / protocol mismatch** | N_m=8 exhibits transient exponential ∣δG∣, but the pure Shenker–Stanford horizon translation is not the microscopic protocol implemented here and the decay disappears at N_m≥10.  This is not a test of the row's coefficient or exponent. |
| JT-noplat-abs | **conflict in the accessible ED window** | The N_m=8 no-absolute-plateau echo fails at all N_m=10,12 points and at N_m=14; the constant model wins instead.  At fixed finite N, neither a permanent plateau nor asymptotic decay is inferred from this short quasiperiodic window. |

These labels compare shapes only.  They do not alter the PROVED
Schwarzian-EFT scopes, whose large-C-first window barely overlaps—in a
parametric sense, does not overlap—the present finite-N window.  Conversely,
the EFT rows do not predict that N_m=8–14 must already show their asymptotic
shape.

## Merge proposals

None.  The finite-N computation should remain linked as Layer-0 evidence, but
its conflict/partial-echo outcome does not justify changing any of the three
adjudicated Schwarzian claim rows.
