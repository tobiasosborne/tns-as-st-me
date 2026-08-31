<!-- JOINT CRITIC BRIEF r1 — SYK/JT decisive computation (bd tns-62n).
     You are the adversarial critic. ATTACK, do not summarize.
     YOUR LANE: write ONLY theory/verdicts/syk-jt-joint-critic-r1.md
     (plus scratch under /tmp). You may RUN code, including the lane's
     Julia module, and mutation-test COPIES in /tmp — never edit lane
     files, numerics files, CLAIMS, definitions, or briefs. No bd
     operations. Work fully autonomously; do not ask questions. -->

# Joint critic r1: attack T1 (analytic) and T2 (numeric), cross-examine

## Read order

1. `theory/lanes/syk-jt/observables-spec.md` — the BINDING observable
   algebra (TJO directive). Any frame/label statement in either lane
   that does not reduce to the specified algebra is a FATAL-class
   objection by orchestrator instruction.
2. `theory/lanes/syk-jt/BRIEF-t1-analytic.md`, `BRIEF-t2-numeric.md` —
   what each lane was ordered to do.
3. The targets: `theory/lanes/syk-jt/t1-analytic.md`,
   `theory/lanes/syk-jt/t2-numeric.md`,
   `numerics/src/schwarzian_memory.jl`,
   `numerics/test/test_schwarzian_memory.jl`,
   `numerics/results/schwarzian_memory.json`.
4. Ground truth TeX (quote file+line):
   `refs/arxiv-1606.01857/GravityReparametrizationsRevised.tex`,
   `refs/arxiv-2412.14799/Main.tex`, `refs/arxiv-1306.0622/shock.tex`.
5. Context only: `theory/lanes/reduction/o4-syk-jt-recon.md` §5.2.

## Obligations (recompute, never referee prose)

1. **T1 core recomputation.** Independently re-derive: the relative
   Möbius data from injected charges (T1 ⟨1⟩2); the plateau criterion
   (its eq (3.7), the a≠1 / dwell-time-moment iff); the decay rate
   (3.15) vs the printed Shenker–Stanford geodesic factor
   (shock.tex:223-234); the DC identity (4.13) at O(1/C). Audit every
   Lamport leaf: does it cite a real file+line or displayed equation,
   and does the quoted source actually say it? Quantifier audit on the
   verdict block ⟨1⟩5 (especially "generically", "iff", limit orders).
2. **T2 code attack.** Run the suite yourself
   (`julia --project=numerics numerics/test/test_schwarzian_memory.jl`).
   Mutation-test on COPIES in /tmp: break one hypothesis at a time
   (flip the source sign; disable the charge-jump check; inject a NaN
   into the results path; zero the Möbius fit) and confirm nonzero
   exit each time. Verify the finiteness/exit discipline claims in the
   report. Check the AIC plateau-vs-decay fit is not rigged (constant
   model must be able to LOSE — verify it loses on the raw δG rows).
3. **Cross-examination (your unique job).** The lanes did not share
   parameter points. Drive T2's module at T1's handshake protocols
   A1/A2/B1/B2 (T1 ⟨1⟩6: delta-impulse kicks with explicit
   coefficients, Δ=1, matching conditions T1 (2.8)/(2.9) — a narrow
   top-hat of equal integrated power kick is an acceptable
   approximation IF you demonstrate convergence as the width shrinks)
   and compare against T1's 12-row finite-time target table
   (⟨1⟩6.⟨2⟩2) entry by entry. Quantify agreement; any unexplained
   relative discrepancy beyond the width-extrapolation error is MAJOR.
4. **The sign.** T1 and T2 report opposite signs of the relative delay,
   and T2 documents a genuine source ambiguity: the MSY TeX prints
   opposite derivative signs between the sourced equation
   (GravityReparametrizationsRevised.tex:611-623) and the charge
   equation region (:957-964), with a literal "FIXSIGNS AND FACTORS"
   comment. Adjudicate the physical sign from first principles (energy
   injected into the right boundary ⟹ which way does the right clock
   shift relative to the left?) and state which lane's convention is
   correct, or that both are internally consistent under stated
   conventions.
5. **Razor enforcement.** Audit both lanes against
   `observables-spec.md`: is every reported quantity an allowed
   observable or a declared-scaffolding intermediate? Specifically
   adjudicate whether Δu_rel := −δG_LR/∂_T G^eq_LR is an allowed
   detector functional (a ratio of two measurable expectations) and
   state the sample-complexity cost of measuring it at late T given
   both numerator and denominator decay exponentially. State the limit
   order (N→∞ / large C first, then T) wherever a lane left it
   implicit.
6. **Consistency of the two verdicts.** T1: plateau in calibrated
   relative-clock readout iff dwell-time moment nonzero; absolute
   δG_LR → 0 always. T2: Δu_rel ratio plateaus at all eight points
   (balanced pulse included), absolute δG_LR decays everywhere, DC
   ratios ≈ 0.985–0.997 at ω=0.05. Are these the SAME theorem-shape?
   Reconcile T2's nonzero balanced-pulse plateau with T1's criterion
   (zero net energy vs nonzero dwell-time moment — check T2's balanced
   profile against T1's a≠1 condition explicitly). Attack the DC
   ratios: is 0.985 "agreement at O(1/C)" or an unexplained 1.5%?
   Compute the expected finite-ω and finite-amplitude corrections and
   say whether the residuals match them.

## Output spec

`theory/verdicts/syk-jt-joint-critic-r1.md`: numbered objections, each
with (a) exact location (file + step/line id), (b) YOUR independent
computation, (c) a one-line FIX DEMAND, (d) the SURVIVING WEAKER
STATEMENT; severity FATAL/MAJOR/MINOR/NOTE. Include your
cross-examination table (T2-at-T1-points vs T1 targets). End with one
line: PASS (no FATAL/MAJOR) or FAIL(ids). Also give an explicit
PROMOTE/HOLD recommendation for the single candidate statement in T1
⟨1⟩5.⟨2⟩6 (recommendation only — you change no statuses and no CLAIMS
rows exist for this yet).
