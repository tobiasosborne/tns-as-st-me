# Corner A — response to critic verdict r1

Prover response (revision **r2**, 2026-08-25) to
[`verdicts/corner-a-r1.md`](verdicts/corner-a-r1.md), verdict
FAIL(WI,A1,A2,G0), objections 1--20.

**Method.** Every objection was re-derived independently before disposition; no
objection was accepted on authority and none was ignored.  The numerical
evidence is in [`checks/corner_a_check.py`](checks/corner_a_check.py)
(self-contained, numpy only, ALL PASS on 2026-08-25), whose checks C0--C7 are
cited by number below.  Where the critic is right, the repair is stated; where
the critic's *inference* overreaches, the rebuttal is a computation, not an
assertion.

**Summary:** 5 FATAL — all conceded and repaired (one with a partial rebuttal).
6 MAJOR — 5 conceded and repaired, 1 partially rebutted.  3 MINOR — conceded.
3 NOTEs — accepted; two of them (9, 17) confirm surviving results.
2 items are now **REFUTED** rather than repaired: r1's A2(e) and r1's claim that
G0(e) delivers an Adler zero / oracle O7--O9.

---

## Disposition table

| # | sev | subject | disposition | where repaired |
|---|---|---|---|---|
| 1 | MAJOR | WI's universal quantifier over `Λ ⊇ R` is false | **FIXED** | D1(e) admits edge-bond insertions; corner-a.md ⟨1⟩3 ASSUME (W1)/(W2), ⟨2⟩7 |
| 2 | MINOR | DAG row multiplies a state by a phase | **FIXED** | (WI-state) has no phase; CLAIMS row split vector/state |
| 3 | FATAL | D9(c) vacuous (`V(g)GL(χ)=GL(χ)`); stabiliser is not `G_diag` | **FIXED** | D9(c) endpoint torsor `E_b^α ≅ PGL(χ)`; D4(b) `N_α`, `ρ_α`, `𝒜_eff`; corner-a.md ⟨1⟩4(e),(f) |
| 4 | FATAL | wrong inverse/order in the twisted algebra; phases don't act on states | **FIXED + PARTIAL REBUTTAL** (R1) | D4(a) uses `V_α(g)`, left mult.; corner-a.md ⟨1⟩4(d1)/(d2)/(d3) |
| 5 | MAJOR | scalar lemma: normalisation ignored; multilinear extension missing | **FIXED** | corner-a.md ⟨1⟩4.⟨2⟩2, `MZM^†=γZ` + explicit multilinear step; check C6 |
| 6 | MINOR | Cauchy criterion stated as an iff | **FIXED** (stronger, correct form) | corner-a.md ⟨1⟩4.⟨2⟩3.⟨3⟩2 |
| 7 | MAJOR | `c_α` is not "exactly" the SPT index (Whitehead) | **FIXED** | D4(d) caveat; corner-a.md ⟨1⟩4.⟨2⟩10 |
| 8 | FATAL | A1's charge-algebra conclusion circular; normality load-bearing | **FIXED + PARTIAL REBUTTAL** (R2) | D4(d) made nominal; content moved to ⟨1⟩4(d); box ⟨2⟩9 retracted as "unused" |
| 9 | NOTE | sector-disjointness lemma survives | **ACCEPTED** (no change) | corner-a-kinks.md ⟨1⟩8 |
| 10 | MAJOR | limit object outside D1(e); `λ_E` rate unjustified (Jordan) | **FIXED** | D1(c) `λ̃` form; D1(e′) two-sided decorations; corner-a-kinks.md ⟨1⟩9.⟨2⟩2 |
| 11 | FATAL | A2(e) false for nonabelian broken symmetry | **CONCEDED — claim REFUTED**, replaced | D9(d) double coset; corner-a-kinks.md ⟨1⟩9(e); check C7 |
| 12 | MAJOR | "contact term" is a name, not a theorem | **CONCEDED — demoted** | corner-a-kinks.md header + status; pitfalls Flag 3 |
| 13 | FATAL | Lemma N drops finite-window boundary terms | **CONCEDED — claim REFUTED**, replaced by Lemma SBP | D5(b) warning; D12; corner-a-goldstone.md ⟨1⟩5; checks C3, C3b, C4, C5 |
| 14 | FATAL | "(IT) fails" contradicts D2 | **FIXED** (wording + logic) | corner-a-goldstone.md ⟨1⟩6(b), ⟨2⟩8; pitfalls Flag 5 |
| 15 | NOTE | tensor-level dichotomy survives | **ACCEPTED**; critic's phrasing adopted | corner-a-goldstone.md ⟨1⟩6(b) |
| 16 | MINOR | rank wording backwards; rank jump ≠ cause of the factor | **FIXED** | corner-a-goldstone.md ⟨1⟩5(vi), ⟨2⟩6.⟨3⟩3--⟨3⟩4 |
| 17 | NOTE | current identity + FM O1 correct | **ACCEPTED** | corner-a-goldstone.md ⟨1⟩7 |
| 18 | FATAL | current identity ⇏ Adler zero / universality / O7--O9 | **CONCEDED — claim RETRACTED** | corner-a-goldstone.md ⟨1⟩6.⟨2⟩7, ⟨1⟩7.⟨2⟩5; pitfalls §5.2(iv) |
| 19 | MAJOR | G0(e)'s quantifier exceeds its nearest-neighbour proof | **FIXED** (finite-range proof supplied) | D10(a) cut current; corner-a-goldstone.md ⟨1⟩6.⟨2⟩5 |
| 20 | MAJOR | both SKETCH boxes are load-bearing | **CONCEDED** | corner-a.md ⟨1⟩4.⟨2⟩9; corner-a-kinks.md ⟨1⟩10.⟨2⟩3; pitfalls Flag 4 |

---

## Rebuttals (computations, not assertions)

### R1 (objection 4, second half) — partial rebuttal

The critic writes: "`𝒱_b` is defined on **states**.  Multiplying a ket bond
insertion by `exp(iω)` has no effect on the normalised state … The multiplier
lives on virtual vectors/edge Hilbert spaces, not on the state orbit as
presently defined.  Constructing such an action is exactly where the
split/normality issue in ⟨1⟩4.⟨2⟩9 enters; it cannot be declared unused."

The first two sentences are **correct and conceded** — check C6 confirms
`fid(𝟙, c𝟙) = 1.000000` exactly, so phases and positive scalars are invisible
to states.  D4(a) and A1(d) are rewritten accordingly.

The final inference is **rebutted**.  Two distinct objects are being conflated:

- the twisted-algebra action **on window vectors**, and
- its realisation **on the GNS Hilbert space `H_A`**.

The first needs no split property whatever.  `𝒲_{Λ,b}` is a
finite-dimensional linear space of explicit window vectors (D1(e)); left
multiplication of the bond-`b` insertion is a linear operator on it; and by
Lemma IT
`𝒱_b(V_α(h))𝒱_b(V_α(g)) = 𝒱_b(V_α(h)V_α(g)) = e^{iω_α(h,g)}𝒱_b(V_α(hg))`,
with the phase acting nontrivially because these are *vectors*, not states.
This is corner-a.md ⟨1⟩4(d1), and it is elementary and complete.

Only the second object needs the split property, and that is exactly what the
box now says.  The correct statement of the situation is the three-level one
now in A1: the multiplier is visible on `𝒲_{Λ,b}` (d1), invisible on states
(d2), and `[ω_α]` is precisely the obstruction to lifting (d2) back to (d1)
(d3).  So the multiplier is *not* homeless, and the box is not needed to give
it a home — it is needed only to move that home into `H_A`.

The critic is nevertheless right that the box "cannot be declared unused": it is
load-bearing for `docs/framing.md`'s demand of a charge algebra acting on the
*physical state space*.  That concession is objection 20 and is recorded.

### R2 (objection 8) — partial rebuttal

The critic writes: "A1 lists D4 and D9 among its assumptions, but D4(d) already
**defines** the asymptotic charge algebra to be `C_omega[H_alpha]`, while D9(c)
already defines the endpoint modules that A1 claims to identify.  The theorem
therefore does not establish the symplectic/physical action … it repeats a
definition."

**Conceded** for the packaging: r1's D4(d) and D9(c) did smuggle in the
conclusion, and both are rewritten (D4(d) is now explicitly nominal; D9(c) is
now a torsor statement whose content is proved in A1(c)).

**Rebutted** for the core: the cocycle law is *not* a definition.  Lemma IT
(corner-a.md ⟨1⟩2), which the critic did not challenge, derives
`V_{g·α}(h)V_α(g) = e^{iω_α(h,g)}V_α(hg)` from the fundamental theorem of MPS
plus the uniqueness clause of refs/arxiv-2011.12127 Eq. (eq:XAX=B).  Neither
`V_α` nor `ω_α` is posited; both are produced.  What r2 adds on top — and what
is genuinely new content rather than restatement — is:

1. `ω_α^{M@b} = ω_α^{M'@b} ⟺ M' ∈ ℂ^×M` (A1(c), check C6).  This is a theorem
   about states, proved from injectivity by multilinear extension; it is what
   makes `E_b^α ≅ PGL(χ)` and rescues D9(c) from vacuity.
2. `ρ_α : G → PGL(χ)` is a genuine homomorphism with kernel `N_α`, and the
   stabiliser of the vacuum is `S_α`, not `G_diag` (A1(e)).
3. `[ω_α]` is the obstruction to lifting `ρ_α` (A1(d3)).

None of these is contained in any definition.

### R3 (objection 1, method) — rebuttal of an incidental claim

The critic's four-site check concludes: "also confirms that there is no silent
`V`/`V^{-1}` flip in that repaired form."  That inference does **not** follow
from the example used.  The critic's tensor has `V(g) = Z`, and `Z² = 𝟙`, so
`V = V^{-1}`: the test is *blind* to the orientation it claims to confirm.

Check C1c reproduces the critic's `ℤ₂` result and records the blindness
(`‖V − V^{-1}‖ = 0.0`).  Checks C0/C1/C1b therefore use a `U(1)` symmetry with
`V(t) = e^{itZ/2}`, `‖V − V^{-1}‖ = 0.686`, for which the D2 orientation
(`V^{-1}` on `∂_-R`, `V` on `∂_+R`) gives error `5.6·10^{-17}` and the flipped
one gives `0.267`.  The orientation is thus genuinely pinned for the first time,
and HANDOFF line 42 is confirmed to be the wrong way round (recorded in
corner-a.md ⟨1⟩3.⟨2⟩8 and pitfalls Flag 2; the brief itself is historical and is
not edited).

### R4 (objection 16, first half) — wording, not error

The critic reads "the gauge-orbit dimension jumps from `χ²−1` to `χ²`" as a
statement about `k → 0` and calls it backwards.  It was written as a statement
about moving *away* from `k = 0`, in which direction it is correct.  The wording
was genuinely ambiguous and is fixed (⟨1⟩5(vi): the rank **drops** as `k → 0`).
The critic's second point — that the rank discontinuity does not *cause* the
`(1−e^{ik})` factor — is correct, conceded, and now stated explicitly
(⟨2⟩6.⟨3⟩4).

---

## What the critic established that r2 keeps

Objections 9, 15 and 17 are NOTEs recording survivals, and r2 relies on them:

- **Lemma D** (sector disjointness under factorised boundary conditions) is
  unchanged and is the backbone of A2.
- The **tensor-level dichotomy** `B_G = 𝒩_0(X)` for unbroken directions versus
  `min_c‖B_G − cA‖ = 1/2` for the broken FM direction is confirmed by the
  critic's own `χ=2` and `χ=1` computations.
- The **continuity equation** and the **O1 rederivation** are confirmed,
  including an independent `N=7` ring calculation (residual `1.1·10^{-16}`,
  energy agreeing to 15 digits).

## Residual gaps after r2 (not repaired, flagged)

1. Normality/split property for `ω_α^{M@b}` — blocks `docs/framing.md`'s
   state-space charge algebra (corner-a.md ⟨1⟩4.⟨2⟩9).
2. Uniformity of A2 over a continuous `Ω_vac` — blocks Corner B on M1
   (corner-a-kinks.md ⟨1⟩10.⟨2⟩3).
3. Everything in objection 18: the passage from the continuity equation to a
   soft theorem.  This is Corner C's whole content and is now explicitly listed
   as such (corner-a-goldstone.md ⟨1⟩6.⟨2⟩7).
4. Completeness of `[ω_α]` as a phase invariant — cited, not proved (A1(g)
   proves invariance only).
