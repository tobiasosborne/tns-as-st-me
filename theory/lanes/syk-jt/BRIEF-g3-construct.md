<!-- LANE BRIEF G3-CONSTRUCT (bd tns-cru). YOUR LANE:
     theory/lanes/syk-jt/g3-construct.md ONLY. No bd operations, no
     CLAIMS/definitions edits. Work fully autonomously. A separate
     adversarial lane is independently attacking this problem; you do
     not have access to its output. Write incrementally. -->

# G3-construct: build Q[ε_{2,c}] on an operational core

Execute problem **G3** of `theory/lanes/syk-jt/corner-a-precision.md`
(read §0, §2, §4.1, G3 in full first — the problem statement there is
binding, including the test objects (4.1)–(4.3), the layer definitions,
and the meaning of "exists"). Binding frame:
`theory/lanes/syk-jt/observables-spec.md`. Ground truth TeX (quote
file+line): refs/arxiv-1606.01857 (MSY), refs/arxiv-2301.07257
(Penington–Witten, Paper.tex), refs/arxiv-2110.05497 (Leutheusser–Liu),
refs/arxiv-2412.14799 (Bucca–Mezei). NO network; no other ids.

Goal, verbatim from G3: exhibit a self-adjoint Q[ε_{2,c}] (ε_{2,c} =
cos 2τ) affiliated with a NAMED algebra (one-boundary A_R^JT or
explicitly relational A_LR^JT), a dense invariant core with the
quadratic-form Ward identity (G3a) i[Q,A] = δ^biloc_ε A on the regulated
bilocal core, parity-even finite-N approximants Q_N with commutator
matrix elements converging at an explicitly PROVED error scale r_N
(finite-N AND finite-coupling; not assumed from Schwarzian power
counting), essential self-adjointness on the core (or construction via
the unitary group), and a final classification: conserved / approximately
conserved with controlled breaking insertion / kinematic only.

Strategy latitude is yours (candidate routes to consider and honestly
triage: the pre-reduction PW phase-space route extended to n=2 with
gauge-invariance repaired relationally; a frequency-filtered microscopic
family Q_N[ε] built from Heisenberg-smeared even bilinears; the
collective-field route via the large-p action with the hard-mode
corrections bounded, using Bucca–Mezei's controlled separation). Partial
results are results: a construction conditional on ONE cleanly stated
unproved lemma beats a vague full claim — Lamport structure (L6b),
every leaf a file+line quote, a displayed prior equation, or a named
elementary computation; [physical argument] flags where rigor drops.
If the construction FAILS, say precisely where and produce the sharpest
surviving statement — that is a success of the lane, not a failure.

Output `theory/lanes/syk-jt/g3-construct.md`: the construction (or its
sharp failure point), the r_N theorem or its obstruction, the
conserved/kinematic classification, an honesty ledger, and a NUMERIC
HANDSHAKE section: if you define finite-N approximants Q_N, give their
exact operator definition (explicit enough to implement in a 2^{N_m}
ED code) and 3–5 predicted Ward-defect matrix elements at N_m ∈
{8,10,12}, βJ ∈ {5,10}, for an independent numerical lane to check.
This lane creates NO claims and changes NO statuses.
