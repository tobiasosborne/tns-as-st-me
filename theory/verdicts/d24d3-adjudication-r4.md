<!-- ROLE: orchestrator-lane ADJUDICATION of corpus referral bd `tns-iu5`,
     repair round 4 (THE CLOSING ROUND), after the FAIL(F1,M1-M5) verdict
     theory/verdicts/d24d3-adjudication-r3-critic.md.
     Work orders: briefs/d24d3-adjudication.md (r1), briefs/d24d3-repair-r2.md,
     briefs/d24d3-repair-r3.md, briefs/d24d3-repair-r4.md.
     Writable files of this lane: this file,
     theory/verdicts/d24d3-repair-r4-response.md, and
     theory/checks/d24d3_normalization_check.py -- nothing else was edited.
     definitions.md, notation.md and claims/CLAIMS.md are NOT edited here;
     all shared-file text is quarantined in section 5 MERGE PROPOSALS, which
     is ONE coherent application and supersedes r3's section 5 exactly where
     marked (revised spans are reprinted IN FULL; spans the r3 critic ruled
     MERGE are incorporated verbatim, unchanged, and flagged as such).
     THIS DOCUMENT IS A DELTA on theory/verdicts/d24d3-adjudication-r3.md:
     it repairs the six failed items and the eight minors, supersedes the
     r3 steps named in section 0.2, and re-derives nothing the r3 critic
     fenced (X1-X15).  Read r3 first; read this second; the merged text of
     section 5 below is the ONLY text offered for the shared files. -->

# r4 adjudication — D24(d) clause 3, the closing round: which normalisation the residue is quoted in

**Verdict.  Unchanged in physics, repaired in one place that r3 could not
see until its own §5.0 existed.  The r3 convention normalised `M_2^O`'s
soft leg and said nothing about the soft leg inside clause (d)2's residue —
the object that actually fixes `𝔞_leg`.  r4 resolves that explicitly, by
the only honest reading available: clause (d)2's residue is quoted in the
CHARGE-CREATED normalisation — the corpus's own Ward normalisation, the one
`ml4-ward-reduction.md` (11) displays and D24N-C3 certifies — and NOT in
(b)'s asymptotic-leg normalisation; the two legs differ by exactly `√Z_ρ`
(r3-critic X1, X15), and that mismatch is part of what the clause (3b)
constant records.  The convention therefore has TWO anchors, stated as
displayed text in both places (§5.0′, §5.2′ clause 2), and the r3 preamble
sentence putting all five clauses in one normalisation is struck as false.
The price is paid in full in §1.4.  The `Q^-_k|Ω⟩ = √(Z_ρ)|k⟩` narrowing —
"the best thing in the round", conditional on this reading — SURVIVES,
because the reading now adopted explicitly is exactly the one under which
⟨1⟩4's computation was valid; it is no longer an accident of mixed
bookkeeping but the convention's own displayed structure.**

Four further things are closed this round.

1. **M1** — the convention's authority is scoped to where its referent
   exists: the fully polarised spin-`S` register, where D24N-C8 constructs
   the kernel.  The D12(b) citation is struck (D12(b) fixes no norm and
   withdraws the one norm claim it made); off that family the kernel's
   existence is claim `ML1` (CONJECTURE), and that gap is named in the
   definition and in the `𝔞_leg(ρ)` registry row (§2, §5.0′, §5.4a′).
2. **M4** — the `𝒮_W → 𝒮_W(ρ)` rename's blast radius is computed in full:
   18 live sites, enumerated in §3; 5 are renamed (TRIANGLE.md, as r3
   already proposed and the critic ruled MERGE) and 13 are made legal by a
   licensing clause in the `𝒮_W(ρ)` registry row (§5.4b′), the critic's own
   cheapest fix.
3. **M5** — the `AMP` row's quantifier is repaired: the value claim is
   scoped to densities where the class is nonempty AND the D24(b) kernel is
   constructed; "UNCONDITIONALLY — without assuming a class member" is
   struck (§4, §5.3c′).
4. **M2/M3** — the checker's false headline is retracted in all four
   layers and made true: `EXPONENT_FIT_BAND = 0.03` is DELETED and the
   exponent band is now DERIVED at runtime from the same quoted-error
   column as the acceptance band (`0.0432` on the shipped data), so a
   `−3.4 %` shift inside the data's stated uncertainty now PASSES; and the
   `0 ≡ 0` cross-momentum orthogonality gate — the fifth shipped no-op —
   is deleted together with its constant-true guard and replaced by a gate
   that can fail: the two-magnon SAME-total-momentum overlap
   `⟨(Q^-_{k})²Ω|(Q^-_{k+π})²Ω⟩ = −2N·Z_ρ`, exact, derived independently
   of the code, and moved by the ladder mutation (§6).

Certificate: `theory/checks/d24d3_normalization_check.py` (green `python3 -O`
exit 0; six red modes with exit *paths* in §6.5).  Both decision bands are
now derived at runtime from the data's own quoted error; the remaining
constants are the pre-registered `0.08`, machine tolerances on exact
identities, and one declared robustness-guard multiplier that can only
reject (§6.4).

---

## 0. What r4 did, and the fences honoured

### 0.1 Not churned (r3-critic §1, X1–X15 — certified, reproduced by the critic, untouched here)

The r1 `V*`, r2 `W*` and r3 `X*` fences all stand.  In particular, this
round does **not** re-derive: the exact identity `Q^-_k|Ω⟩ = √(Z_ρ)|k⟩`
with `|k⟩` an exact `H_S` eigenvector (X1); the refutation arithmetic and
its `5.2–12.5×` margins at the pre-registered band (X2); the derived
acceptance band `0.047854` (X3); the six red-mode exit paths (X4); the
appliability of the three `definitions.md` spans in descending order (X5);
the `notation.md` anchors and "13 is the next free rule number" (X6); the
`D24-VAL` plain-`PROVED` status call (X7); ML5-B's constant-agnostic
reparametrisation and the annotation-not-erratum decision on
`corpus-r2.md:174–178` (X8); the contact-route re-sourcing (X9); the
completeness of the "only place it can live" withdrawal (X10); C5's
two-sided subsumption by C4 (X11); the `1.69×` exponent-resolution figure
(X12); the declared data-mutant behaviour including `m6_shift30` passing
(X13); the closed ladder hole (X14); and `‖Q^-_q|h⟩‖² = Z_ρN − 2` (X15 —
which r4 promotes from the critic's verdict into the certificate itself,
§6.3).  Two rulings in this lane's favour are likewise final: the
`D24-VAL` status deviation was *required* by the CLAIMS header (X7), and
r1's M3(c)(iii) declination is accepted as correctly reasoned
(r3-critic §8).

### 0.2 Supersessions — exactly which r3 text this round replaces

r3 remains the record of the adjudication's architecture.  The following
r3 statements are SUPERSEDED by this document and must not be quoted as
live:

| r3 location | r3 text (gist) | superseded by |
|---|---|---|
| §5 preamble + §5.2 preamble | "All amplitudes below are in the normalisation convention of (b)" | §1.1, §5.2′ — clause 2's residue is quoted in the charge-created normalisation |
| §2 ⟨1⟩0.⟨3⟩1 | "Clauses 1, 2, 4 and 5 are invariant" | §1.2 — clauses 1, 4, 5 are invariant; clause 2 transforms as `c′/c` |
| §2 ⟨1⟩0.⟨3⟩3 | convention cited to "the fixed-`k` reading of D12(b)" | §2 — D12(b) fixes no norm; the kernel is constructed only in the spin-`S` register (D24N-C8); off it, `ML1` |
| §2 ⟨1⟩4.⟨3⟩1 | "exact, `k`-independent, `N`-free per site" (unqualified) | §1.3 — exact on the vacuum leg; on the descendant leg `Z_ρ − 2/N` per site, exactly `√Z_ρ` only in the LSZ limit |
| §2 ⟨1⟩4.⟨3⟩3 | `Z_ρ^{-1/2}` presented as an independent "mechanism" | §1.3 — one step from the numerator/denominator normalisation mismatch |
| §0 (R3-d), §3, §7.5, H7 | "there is no acceptance constant in the file" (four layers) | §6.1 — false as written for r3's checker (`EXPONENT_FIT_BAND = 0.03`); made true in substance by deriving the exponent band, restated precisely |
| §0 (R3-d), §7.3, §7.4 | "a **real** cross-momentum orthogonality gate (kills `cB_onek`)"; "r2-critic m4, all three closed" | §6.2 — the gate was `0 ≡ 0` (fifth corpus no-op) and the kill was a constant-true `require`; m4(ii) was NOT closed in r3; it is closed now, differently |
| §0 (R3-d) | "every occupation `n ≤ 2S`" | §6.5 (m7) — the code's `n ≤ 2S−1` is right (`n = 2S` gives `S^-\|{-S}⟩ = 0`); the §0 prose was wrong by one |
| §7.4 | "Every gate is reachable" | §6.5 (m5) — every gate *offered as evidence* (C2, C3, C4, C6, C8) is reachable; C1, C5, C7 are GUARD/DISPLAY precisely because they are not |
| §5.3c | `AMP` row: "`𝔞_leg(ρ) = 1/Z_ρ` UNCONDITIONALLY — without … assuming a class member" | §4, §5.3c′ |
| §4.2/§5.5 | rename list of 5 sites | §3 — 18 sites |

### 0.3 Done this round (no new physics; one identity moved from the critic's verdict into the certificate)

* **(R4-a)** F1 resolved: the residue's normalisation stated in displayed
  text in clause (d)2 itself and in §5.0′; the preamble corrected; the
  invariance list corrected; ⟨1⟩4 re-derived in one step under the adopted
  reading; the cost stated (§1).
* **(R4-b)** M1: convention scoped to the register where its kernel exists;
  D12(b) citation struck; `ML1` named as the gap; the same scope added to
  the `𝔞_leg(ρ)` registry row; m4's two `D24(b)` citation sites added to
  the blast radius with the honest sentence ("consistent with every
  existing corpus use of *amputated* only because every existing use sits
  at `ρ = 1/2`"), and §5.0′ now says it narrows the ML4-admissible class
  (§2).
* **(R4-c)** M4: all 18 rename sites enumerated; licensing clause adopted
  (§3, §5.4b′).
* **(R4-d)** M5: `AMP` requantified (§4, §5.3c′).
* **(R4-e)** Checker fourth pass (M2, M3, m1, m2): `EXPONENT_FIT_BAND`
  deleted and the exponent band derived from the data (§6.1); the `0 ≡ 0`
  orthogonality sub-gate and its constant-true guard deleted, replaced by
  the two-magnon same-total-momentum overlap gate with an independent
  closed form (§6.2); the descendant-leg norm `‖Q^-_q|h⟩‖² = Z_ρN − 2`
  added as a gate, so D24N-C8 no longer tests only the vacuum case (§6.3);
  a per-row corrupted-error guard added (§6.4); the residue printed in
  BOTH normalisations as a labelled DISPLAY line (§6.5).
* **(R4-f)** Merge mechanics completed: `notation.md`'s six edits given an
  explicit application order that keeps every stated anchor valid (m3,
  §5.4-order); §5.5 extended by the critic's four demanded items (M4
  licensing/rename, m4's two citation sites, m8's `TRIANGLE.md:216–218`,
  m3's ordering sentence), plus m6's H8 sentence and n2's warrant note
  (§5.5′, §7).

**Symbols of this round.**  None new.  `𝔞_leg(ρ)`, `Z_ρ`, `L(k,h)`,
`E^O_desc`, `𝒮_W(ρ)` exactly as r3 registered them, with the two registry
rows amended as §5.4a′/§5.4b′.

---

## 1. F1 — which normalisation clause (d)2's residue is quoted in

### 1.1 The trilemma, and the reading adopted

The r3 critic measured clause (d)2's residue in both normalisations
(r3-critic F1(b)(i), `N = 8`, `2S = 1,2,3,4`, exact): against the
**charge-created** soft leg `Q_0|h⟩` it is `2i·Z_ρ·J\sin h = 2i\,v_S(h)` —
what clause 2 displays and D24N-C3 certifies; against the `δ`-normalised
asymptotic leg that §5.0 mandates for `M_2^O` it is
`2i·√Z_ρ·J\sin h = 2i\,v_S(h)/√Z_ρ`.  A coefficient along a vector changes
when the vector is renormalised, so the r3 preamble's "All amplitudes below
are in the normalisation convention of (b)" made clause 2 false by exactly
`√Z_ρ` at every `ρ ≠ 1/2`, and ⟨1⟩0.⟨3⟩1's invariance list was wrong for
clause 2.  Three readings were on the table, each with a stated cost:

1. **Literal** (clause 2 read in (b)'s convention): clause 2 is
   unsatisfiable by `√Z_ρ` at every `ρ ≠ 1/2`; `𝒮_W(ρ)` is provably empty
   again — the defect this adjudication exists to remove, reinstated one
   clause over.  REFUSED.
2. **Shape** (clause 2 asserts only `residue ∝ v_h M_1^O`): the constant
   split between clause 2 and `𝔞_leg` is exactly the freedom §5.0 was
   built to remove; r2-critic F1 survives verbatim.  REFUSED.
3. **Normalisation-fixing** (clause 2 *defines* the soft-leg normalisation
   by demanding the residue be exactly `2i v_h M_1^O`): `𝔞_leg = 1` by
   construction, the frozen clause is restored, `D24-VAL` is refuted
   rather than open.  REFUSED.

**ADOPTED: the residue is quoted in the charge-created normalisation, and
this is stated as displayed text.**  Clause (d)2 is a statement about the
descendant current inside the Ward reduction — the coefficient in
`P_{1,N}J^-_0|h⟩ = \frac{2iv(h)}{N-2}\,Q_0|h⟩` (`ml4-ward-reduction.md`
(11), whose denominator `N−2` is exactly `‖Q_0|h⟩‖²` at `Z_ρ = 1`,
r3-critic X15) — quoted against the **charge-created** soft leg `Q_0|h⟩`,
not against (b)'s asymptotic leg.  So read, clause 2 involves no
asymptotic soft leg at all: it is well posed at every density, its
certificate (D24N-C3) is computed in exactly the normalisation it is
quoted in, and it is *satisfiable* — no emptiness is reinstated.  The
convention then has **two anchors**: §5.0 fixes `M_2^O`'s soft leg
(`δ`-normalised asymptotic magnon, unit weight, hence `c′(0)/c = 1` on
the amplitude side), and clause 2 anchors the residue display in the
model's own Ward normalisation.  The `√Z_ρ` between the two legs
(r3-critic X1; named computation D24N-C8) is not an inconsistency: it is
the exact, computed conversion between the two anchors, and it is part of
what the clause (3b) constant `𝔞_leg(ρ)` records.  This is the r3
critic's own "mixed reading", promoted from a forbidden accident to the
convention's displayed structure — which is the only way the round's
sharpest result (⟨1⟩4) states a truth rather than a bookkeeping slip.

The merged text changes (all reprinted in full in §5):

* the preamble sentence becomes: "*Amplitudes below (`M_1^O`, `M_2^O`,
  and the clause-1 summand `E^O_desc`) are in the normalisation convention
  of (b); clause 2's residue display is quoted in the charge-created
  normalisation of `ml4-ward-reduction.md` (11), as stated in that clause;
  clause 3b is empty without (b).*";
* clause 2 itself states its normalisation and the `√Z_ρ` mismatch, in
  displayed text (§5.2′ clause 2);
* §5.0′'s covariance paragraph carries the corrected invariance list
  (§1.2) and records that the mismatch is a one-step consequence of the
  two anchors (§1.3).

### 1.2 The corrected invariance list (supersedes r3 ⟨1⟩0.⟨3⟩1)

**⟨2⟩1. PROVE.**  Under a normalisation change `M_1^O ↦ c\,M_1^O`,
`M_2^O(k,·) ↦ c′(k)\,M_2^O(k,·)` (`c, c′(k) ≠ 0`, independent of `O` by
linearity), clauses (d)1, 4 and 5 are invariant; clause (d)2 transforms as
`c′/c`; and `L(k,h) ↦ (c′(k)/c)L(k,h)`, `𝔞_leg ↦ (c′(0)/c)𝔞_leg`.

**⟨3⟩1.**  Clauses 1, 4, 5 are each homogeneous statements in one
amplitude (a decomposition of `M_2^O`, an `O(k²)` bound, a bound by
`‖M_1^O‖`), so both sides scale together.  Justification: D24(d)1,4,5;
r3 ⟨1⟩0.⟨3⟩1 (this part unchanged).

**⟨3⟩2.**  Clause 2 equates the residue of `E^O_desc ⊂ M_2^O` along the
model-fixed vector `Q_0|h⟩` (which does not rescale — it is a state, not
an amplitude) to the literal `2i v_h M_1^O`.  The left side scales with
`c′`, the right with `c`; the clause transforms as `c′/c`.  It is the one
clause that is NOT homogeneous in a single amplitude, and — jointly with
§5.0's `c′(0)/c = 1` — it is the second half of the bookkeeping that
makes `𝔞_leg` a determined number.  Justification: r3-critic F1(b)(i) —
adopted in full; D24N-C3.

**⟨3⟩3. QED.**  r3's "clauses 1, 2, 4 and 5 are invariant" is struck.

### 1.3 ⟨1⟩4 re-derived under the adopted reading (supersedes r3 ⟨1⟩4.⟨3⟩1 and ⟨1⟩4.⟨3⟩3)

**⟨2⟩1. PROVE.**  On the charge-created reading of `E^O_desc` — the
reading the three corpus provenance sites display — the adopted
convention gives `𝔞_leg = Z_ρ^{-1/2}` in one step; the ansatz-free data
refutes that value at the pre-registered band; hence AMP, if true,
requires a second factor `Z_ρ^{-1/2}` from a mechanism that is not a leg
normalisation.

**⟨3⟩1.  The conversion factor, with its finite-`N` scope (m1 adopted).**
On the fully polarised spin-`S` tail, `Q^-_k|Ω⟩ = √(Z_ρ)·|k⟩` **exactly**
— on the *vacuum* leg the factor is exact, `k`-independent and `N`-free
per site (r3-critic X1; D24N-C8).  On the *descendant* leg the same
statement holds only asymptotically: `‖Q^-_q|h⟩‖² = Z_ρN − 2` exactly
(r3-critic X15; new gate, §6.3), i.e. `Z_ρ − 2/N` per site, so the
conversion factor there is `√Z_ρ·√(1 − 2/(Z_ρN))`, equal to `√Z_ρ` only
in the `N → ∞` LSZ limit.  The correction is `≤ 1/(Z_ρN) ≈ 10^{-2}` at
the data's smallest `N = 60`, against refutation margins of `5–12×`, so
no conclusion below moves.  Justification: D24N-C8 (both sub-gates,
§6.3); r3-critic X1, X15, m1.

**⟨3⟩2.  One step.**  The (3a) quotient is
`L(k,h) = E^O_desc(k,h)/[(e^{ik}−1)·2i v_h·M_1^O(h)]`.  Its
**denominator's** residue factor `2i v_h M_1^O` is clause 2's display,
quoted in the charge-created normalisation (§1.1).  Its **numerator**
`E^O_desc` is a clause-1 summand of `M_2^O`, measured in (b)'s
normalisation — against the `δ`-normalised asymptotic soft leg.  On the
charge-created reading of `E^O_desc` (the descendant term is exactly the
propagated charge-created leg, with no further dressing — the reading
under which the frozen computation gave `L(0,h) = −iχ/v_h`, i.e.
`𝔞_leg = 1`, when BOTH sides were taken charge-created), converting the
numerator's soft leg from charge-created to (b)'s divides it by `√Z_ρ`
(⟨3⟩1) while the denominator does not change (its normalisation is
anchored by clause 2, not by (b)).  Hence

    𝔞_leg^{leg-conv} = Z_ρ^{-1/2},

in one step, as the numerator/denominator normalisation mismatch — not as
an independent "mechanism".  At `ρ = 1/2` the two normalisations
coincide (`√Z_ρ = 1`), which is why the D6 corpus is internally
consistent and why three rounds could not see the defect.
Justification: ⟨3⟩1; §1.1; D24N-C1 (the frozen, both-sides-charge-created
computation is density-blind).

**⟨3⟩3.  Refuted, and the residue of AMP.**  Unchanged from r3
⟨1⟩4.⟨3⟩4–⟨3⟩6, which the critic verified (X2): `Z_ρ^{-1/2}` deviates by
`0.4158/0.7347/1.0033` at `S = 1, 3/2, 2` against the pre-registered
`0.08` — margins `5.2–12.5×`, needing no derived band — conditional on
the bridge (α), without which nothing is matched and nothing is refuted.
`1/Z_ρ = Z_ρ^{-1/2}·Z_ρ^{-1/2}`: the convention mismatch supplies the
first factor exactly, so AMP is true iff a second `Z_ρ^{-1/2}` arises
from something that is **not** a leg normalisation, and any proposed AMP
proof must be checked against D24N-C8 or it double-counts the leg.

**⟨3⟩4. QED.**

### 1.4 What the resolution costs, and what survives

**Costs, stated as losses (L10):**

1. **The one-convention selling point of r3 is dead.**  The definition now
   quotes one clause in a different normalisation than the others and must
   say so in displayed text forever.  A reader can no longer assume a
   single normalisation across D24(d); the two-anchor structure is the
   price of having both a satisfiable clause 2 and a determined `𝔞_leg`.
2. **Clause 2 is demoted from "invariant" to "convention-constitutive".**
   The invariance list shrinks to clauses 1, 4, 5.  Clause 2 now does two
   jobs at once — a substantive Ward-covariance membership condition
   (certified exactly at every density, D24N-C3) *and* the second anchor
   of the bookkeeping — and the definition says both.
3. **`𝔞_leg = Z_ρ^{-1/2}`-from-leg-conversion loses its status as an
   independent mechanism.**  It is the convention's own mismatch,
   computed.  What r3 called "the one proposed mechanism for AMP" is,
   under the adopted reading, the *default* value the convention assigns
   on the charge-created reading of `E^O_desc` — and the data refutes it
   (under (α)), which refutes that reading of `E^O_desc` for any actual
   class member, not merely one candidate constant.

**What survives, and why:**

* **The narrowing survives, now unconditionally on its reading.**  The r3
  critic's X2 fence: "IF clause 2's residue is read in the charge-created
  normalisation while `E^O_desc` is read in (b)'s, then
  `𝔞_leg = Z_ρ^{-1/2}` and the ansatz-free data refutes it at 5–12×."
  §1.1 adopts exactly that antecedent as the displayed convention, so the
  conditional discharges: AMP's residual content IS a second
  `Z_ρ^{-1/2}` from a non-leg mechanism.  The honest caveat carried
  forward from r3 ⟨1⟩4.⟨3⟩6 verbatim: this neither proves nor refutes
  AMP and exhibits no class member.
* **`𝒮_W(ρ)` does not become provably empty.**  Clause 2, read as
  adopted, is exactly the corpus's certified Ward identity; no `√Z_ρ`
  obstruction to membership exists at any density (that obstruction was
  an artifact of the literal reading, refused above).  Nonemptiness
  remains OPEN at every `ρ` (§4.4 of r3, unchanged; bd `tns-axg`).
* **`D24-VAL` and the exponent pin are untouched** — their arithmetic
  never referenced the residue's normalisation (X2, X12).

---

## 2. M1 — the convention's register, scoped to where its referent exists

**The finding, adopted in full.**  r3's §5.0 cited "the fixed-`k` reading
of D12(b)" as authority for `⟨k|k′⟩ = 2πδ(k−k′)`.  D12(b) is a statement
about the gauge remainder of the MPS tangent vector; it fixes **no inner
product and no state norm**, and it explicitly withdraws the one norm
claim it ever made (the r2 `‖bulk‖ = Θ(|Λ|^{1/2})` assertion, with a
`χ = 1` counterexample).  D3(a) and D12(a′) are packet-class statements.
The `δ`-normalised asymptotic one-magnon kernel is *constructed* in
exactly one place in this corpus: the fully polarised spin-`S` register,
by D24N-C8 (`|k⟩ = Σ_x e^{ikx}|x⟩`, `⟨k|k′⟩ = Nδ_{kk′}`, an exact `H_S`
eigenvector).  At any other density the existence of the asymptotic
one-magnon kernel is claim **ML1** (`claims/CLAIMS.md:33`, CONJECTURE,
future work, no shard, no test).

**The two citation fixes (r3-critic M1(c)):**

1. §5.0′ replaces the D12(b) citation with the honest construction: "*in
   the fully polarised spin-`S` register the kernel is
   `|k⟩ = Σ_x e^{ikx}|x⟩` (named computation D24N-C8); in any other
   register the existence of the asymptotic one-magnon kernel is claim
   `ML1` (CONJECTURE), and `𝔞_leg(ρ)` is defined only where that kernel
   is.*"  D3(a)/D12(a′) remain cited for what they do fix (the packet
   discipline).
2. §5.4a′ adds the same scoping clause to the `𝔞_leg(ρ)` registry row,
   beside "defined only when that class is nonempty".

**Consequence, stated at its true strength (r3-critic M1(d), adopted):**
fixing `c′(0)/c = 1` makes `𝔞_leg` a determined number exactly on the
fully polarised spin-`S` family — which is the register in which
`D24-VAL`, ⟨1⟩4 and the whole certificate live — and relocates the
remaining arbitrariness into the unconstructed kernel everywhere else.
The `ρ`-general reading of the convention is not available and is no
longer asserted anywhere (H2′, §7).  A residual phase freedom
`e^{iθ(k)}` on the kernel leaves only `|𝔞_leg|` pinned in general; in the
spin-`S` register the origin choice fixes `θ(0) = 0` (a lattice
translation multiplies `|k⟩` by `e^{ika} → 1` at `k = 0`); off that
register there is nothing to fix it against — this is folded into the
same scoping sentence.

**The two `D24(b)` citation sites (r3-critic m4, adopted), added to the
blast radius (§4.3 of r3 is extended by these; §5.5′ items 12–13):**

* `theory/ml4-ward-reduction.md:63–68` grants an "ML4-admissible analytic
  amputation at fixed `N`" — multiplication by any bounded `C¹` operator
  family for `|k| ≤ ε_I` — a freedom strictly **wider** than §5.0′, which
  forbids any soft-leg weight with `λ(0) ≠ 1`.  §5.0′ now says in
  displayed text that it **narrows** the ML4-admissible class, so a
  reader of the ML4 shard cannot draw a false conclusion about D24(b)
  amplitudes.
* `theory/ansatz-scattering-2m.md:614, 621–631` uses "the normalized
  multiplier amputation of D24(b)" — an amputation under which the
  amputated datum *is* the physical multiplier, i.e. the `S_phys`-valued
  convention r3 ⟨1⟩0.⟨3⟩6 says §5.0 refuses.  It is harmless only
  because that shard is D6 (`ρ = 1/2`), where the two conventions
  coincide.

The honest sentence, recorded in §5.5′ and quoted from the critic: **§5.0
is consistent with every existing corpus use of "amputated" only because
every existing use sits at `ρ = 1/2`.**

---

## 3. M4 — the `𝒮_W → 𝒮_W(ρ)` rename, at all 18 live sites

Grep of the whole repo this round (excluding verdict files and this
lane's own documents), reproducing the critic's table exactly.  The
rename is live at **18 sites**; r3 listed 5.  Full enumeration and
disposition:

| # | site | disposition |
|---|---|---|
| 1 | `theory/TRIANGLE.md:24` | RENAME (r3 §5.5 item 2, ruled MERGE — unchanged) |
| 2 | `theory/TRIANGLE.md:215` | RENAME (same) |
| 3 | `theory/TRIANGLE.md:254` | RENAME (same) |
| 4 | `theory/TRIANGLE.md:257` | RENAME (same) |
| 5 | `theory/TRIANGLE.md:528` | RENAME (same) |
| 6 | `definitions.md:916` (D24 section header) | LICENSED bare (§5.4b′) |
| 7 | `definitions.md:1004` (D25) | LICENSED bare |
| 8 | `claims/CLAIMS.md:29` (S-general row, twice in the row) | LICENSED bare |
| 9 | `claims/CLAIMS.md:82` (corner-implication prose) | LICENSED bare |
| 10 | `theory/ml5-universality.md:133` | LICENSED bare |
| 11 | `theory/ml5-universality.md:141` | LICENSED bare |
| 12 | `theory/ml5-universality.md:152` | LICENSED bare |
| 13 | `theory/ml5-universality.md:159` | LICENSED bare |
| 14 | `theory/ml5-universality.md:197` | LICENSED bare |
| 15 | `paper/main.tex:245` (`\mathcal{S}_W`) | LICENSED bare |
| 16 | `paper/main.tex:252` | LICENSED bare |
| 17 | `paper/main.tex:542` | LICENSED bare |
| 18 | `paper/main.tex:556` | LICENSED bare |

(The two `notation.md` occurrences at lines 244 and 258 are registry
rows, not live uses; they are edited by §5.4c and §5.4b′ respectively and
are not counted above, matching the critic's count of 18.)

**Disposition rationale.**  The critic offered two fixes and endorsed the
cheaper: one clause in the `𝒮_W(ρ)` registry row licensing the bare form
"*where the density is fixed or immaterial*".  Adopted (§5.4b′), because
(i) it makes all 13 non-TRIANGLE sites legal without touching five more
files in the same commit, (ii) every one of those sites either quantifies
over the class at an unspecified density (CLAIMS, ml5-universality, the
Letter's Conjecture S) or names the class as an object (headers, D25),
where the index is immaterial, and (iii) it mirrors exactly the mechanism
already adopted for `𝔞_leg` (bare inside a fixed-`ρ` display, overload
rule 13).  The TRIANGLE.md sites stay renamed because that edit is
already ruled MERGE and TRIANGLE is the triangle's index document, where
the `ρ`-indexed form earns its keep.  After this commit `definitions.md`,
`notation.md` and every live site are mutually consistent under
`notation.md`'s closing rule ("a symbol used anywhere without an entry
here is a defect") — the entry now covers both forms.

---

## 4. M5 — the `AMP` row, requantified

**The finding, adopted in full.**  r3's row asserted
`∀ρ: 𝔞_leg(ρ) = 1/Z_ρ` "UNCONDITIONALLY — without the D24-VAL bridge and
without assuming a class member", while the same merge defines
`𝔞_leg(ρ)` as a partial function — undefined when `𝒮_W(ρ) = ∅` (open at
every `ρ`) and, per M1, undefined wherever the (b) kernel is not
constructed.  The row asserted an equation whose sides may both lack
referents, and advertised the missing hypothesis as a strength.  That is
r2-critic M2's quantifier defect, re-installed in a new DAG row —
exactly what the r3 response's own §6 item 3 predicted.

**The repair (§5.3c′), following the critic's (c) verbatim in substance:**
the statement becomes "*for every `ρ` at which `𝒮_W(ρ) ≠ ∅` **and** the
D24(b) asymptotic one-magnon kernel exists (currently: the fully
polarised spin-`S` family, D24N-C8), `𝔞_leg(ρ) = 1/Z_ρ`, **without the
(α) bridge***", plus the same vacuous-or-unknown sentence `D24-VAL`
already carries.  What distinguishes AMP from `D24-VAL` is retained and
stated: AMP drops (α) — the critic's own record confirms the two rows are
not a double count.  The ⟨1⟩4 fence inside the row survives verbatim (the
critic asked that it should), updated only to cite §1.3's one-step
derivation alongside r3 ⟨1⟩4.  Status stays CONJECTURE; where-tested
stays as r3 wrote it (the critic verified both).

---

## 5. MERGE PROPOSALS (r4-final — supersedes r3 §5 exactly where marked)

*This lane edited no shared file.  The orchestrator applies the following
as **ONE commit**.  Spans marked ′ are REVISED this round and reprinted in
full; spans marked "r3 verbatim" are incorporated unchanged from
`theory/verdicts/d24d3-adjudication-r3.md` §5, where the r3 critic ruled
them MERGE (or MERGE-after-F1, which §1 discharges).  A partial
application is not offered: §5.1's `𝔞_leg` and §5.2′'s clause 3b are
meaningless without §5.0′'s convention, and §5.3's rows quote both.*

**Mechanics — `definitions.md`.**  All three spans are REPLACEments of
adjacent blocks; apply them in **descending line order** — §5.2′
(952–973), then §5.1 (931–950), then §5.0′ (923–929) — or match on the
quoted first and last lines.  Anchors unchanged since the r3 critic
re-verified and test-applied them (X5): `:923` begins
`**(b) Amputated amplitudes.**`, the (b) span ends at `:929` (`waves are
generalised kernels inside \`C_c^∞\` packets (D3(a), D12(a′)).`); `:931`
begins `**(c) The contact first jet.**`, ends `:950` (`factorisation with
the same stated norm control.`); `:952` begins `**(d) The Ward-covariant
no-contact class`, ends `:973` (`is part of the ML5-B future work.`).

**Mechanics — `notation.md` (m3, the missing ordering, supplied).**
Apply the six §5.4 edits in **this order**, which is descending in line
number, so that no stated anchor drifts:

1. §5.4b′ — REPLACE the `𝒮_W` row (line 258);
2. §5.4a′ — ADD the four new rows immediately after line 258;
3. §5.4c — one-string replacement in the `𝖲(k_s;{q_i,v_i})` row (line 244);
4. §5.4f — INSERT new overload rule 13 after rule 12's last line
   (line 145), keeping the blank line before `All other symbols are
   unique.` (line 147);
5. §5.4e — APPEND to overload rule 8 (block at lines 123–130);
6. §5.4d — APPEND to overload rule 2 (block at lines 91–98).

Alternatively match each edit on its quoted first line.  (The r3 text
listed the same six edits with no order; applying them in the r3 written
order a→f moves rule 8 to 127–134 after the rule-2 append and breaks two
stated anchors — r3-critic m3.  The order above is the fix.)

**Mechanics — `claims/CLAIMS.md`.**  ML5-A is line 40, ML5-B line 41
(unchanged).  Apply §5.3a (REPLACE line 41), then §5.3b (ADD after it),
then §5.3c′ (ADD after that), then §5.3d (REPLACE line 40) — or match on
the row labels, which are unique.

### 5.0′ `definitions.md` — D24(b), lines 923–929 (REVISED: F1 invariance list, M1 citation, m1 descendant-leg scope, m4 ML4-narrowing)

**REPLACE** (from `**(b) Amputated amplitudes.**` through
`waves are generalised kernels inside \`C_c^∞\` packets (D3(a), D12(a′)).`):

```
**(b) Amputated amplitudes, and the normalisation they are measured in.**
For a source `O`, `M_1^O(h)` is its amputated one-hard amplitude and
`M_2^O(k,h)` its connected hard-plus-soft amplitude in the physical channel;
both are linear in `O`, and both are measured as multipliers in `L²(I,dh)`
for a fixed hard window `I = [a,b] ⋐ (0,π)`.  Remainders are measured in
`‖R_{S2}(k)‖_{L²(I)} ≤ C_I|k|²‖M_1^O‖_{L²(I)}`, or, for
`f_ε(k) = ε^{-1/2}f(k/ε)`, as `O(ε²)` in the product packet norm.  Plane
waves are generalised kernels inside `C_c^∞` packets (D3(a), D12(a′)).

*Amputation and leg-normalisation convention.*  Both amplitudes are taken
against asymptotic one-magnon kernels normalised by `⟨k|k′⟩ = 2πδ(k−k′)`,
inside the corpus's packet discipline (D3(a); the `ℓ¹∩BV` packet class of
D12(a′)).  That kernel is *constructed* in the fully polarised spin-`S`
register, where it is `|k⟩ = Σ_x e^{ikx}|x⟩` (named computation D24N-C8 in
`theory/checks/d24d3_normalization_check.py`, an exact one-magnon
eigenvector of `H_S`); in any other register the existence of the
asymptotic one-magnon kernel is claim `ML1` (CONJECTURE), and every
statement about the (d)3b constant `𝔞_leg(ρ)` is scoped to a register
where the kernel exists.  The **same** amputation is applied to the
**same** hard leg in both.  The soft leg enters `M_2^O` as **one
additional `δ`-normalised asymptotic magnon of momentum `k`, carrying
unit leg weight** — not as a charge-created or current-created vector.
This convention is strictly *narrower* than the ML4-admissible analytic
amputation of `theory/ml4-ward-reduction.md` (which admits any bounded
`C¹` multiplier family at fixed `N`): here every soft-leg envelope `λ(k)`
must have `λ(0) = 1`.

This is a *convention*, not a theorem, and it is load-bearing.  A change of
normalisation `M_1^O ↦ c\,M_1^O`, `M_2^O(k,·) ↦ c′(k)\,M_2^O(k,·)` with
`c, c′(k) ≠ 0` (necessarily independent of `O`, by linearity above) leaves
clauses (d)1, 4 and 5 invariant — each is a homogeneous statement in one
amplitude — while clause (d)2, whose residue is quoted against the
charge-created soft leg (see (d)2), transforms as `c′/c`, and the (d)3a
external flux factor and the (d)3b amputation constant transform as
`L(k,h) ↦ (c′(k)/c)L(k,h)` and `𝔞_leg ↦ (c′(0)/c)\,𝔞_leg`.  Fixing
`c′(0)/c = 1` as above, jointly with clause (d)2's residue anchor, is what
makes `𝔞_leg` a number rather than a name: without them, "`𝔞_leg = 1`" and
"`𝔞_leg = 1/Z_ρ`" are statements about a convention and not about a model.
What remains free does not move `𝔞_leg`: rescaling the source (both
amplitudes are linear in `O`); any hard-leg amputation convention applied
identically in both (it cancels in the (d)3a quotient); and any soft-leg
envelope `λ(k)` with `λ(0) = 1`.

Two consequences are recorded because they are used below.  (i) In the
fully polarised spin-`S` ferromagnet the **charge-created** soft leg is
*not* this convention's soft leg: `S^-_x|Ω⟩ = √(Z_ρ)\,|x⟩` on normalised
one-flip states, hence `Q^-_k|Ω⟩ = √(Z_ρ)\,|k⟩` exactly on the vacuum
(named computation D24N-C8, verified against the Hamiltonian's own
one-magnon eigenvector), the two legs coinciding only at `ρ = 1/2`; on a
descendant (one-hard-magnon) state the same conversion holds per site
only up to `O(1/(Z_ρN))` — `‖Q^-_q|h⟩‖² = Z_ρN − 2` exactly (D24N-C8) —
becoming exactly `√Z_ρ` in the LSZ limit.  (ii) Because clause (d)2's
residue is quoted against the charge-created leg while the (d)1 summand
`E^O_desc` is measured against this convention's asymptotic leg, a
soft-leg normalisation argument alone contributes exactly that conversion
mismatch, `Z_ρ^{-1/2}`, to `𝔞_leg` — not `Z_ρ^{-1}`; see the fence on
lemma AMP in (d)3b.
```

### 5.1 `definitions.md` — D24(c), lines 931–950  (r3 verbatim — ruled MERGE-after-F1, F1 now discharged)

Apply `theory/verdicts/d24d3-adjudication-r3.md` §5.1 unchanged, byte for
byte.  (The r3 critic verified it verbatim-appliable at the exact anchors
and carrying `𝔞_leg` into all three displays; nothing in the F1
resolution touches D24(c).)

### 5.2′ `definitions.md` — D24(d), lines 952–973 (REVISED: preamble sentence, clause 2, clause 3b scope; all else byte-identical to r3 §5.2)

**REPLACE** (from `**(d) The Ward-covariant no-contact class` through
`is part of the ML5-B future work.`):

```
**(d) The Ward-covariant no-contact class `𝒮_W(ρ)`.**  Fix a broken-symmetry
tail density `ρ := ω_α(S^z) > 0` (`notation.md`'s `ρ`-row), and write
`Z_ρ := 2ρ` for the order-parameter density (`notation.md`'s `Z_ρ`-row; in
an su(2) model with a fully polarised α tail, `Z_ρ = ω_α([S^+_x, S^-_x])` —
a special case, not a membership condition).  Under (S) at both tails,
D26(INT), and the antisymmetric tail pair `ω_β(S^z) = −ω_α(S^z) = −ρ` —
the load-bearing hypothesis of claim `M-IDX-density` — `2ρ ∈ ℤ`, so `Z_ρ`
is then a positive integer.  `ρ = 0` is excluded: D26 admits it, but there
is then no broken order parameter and no type-B soft leg.  In the fully
polarised spin-`S` ferromagnet `ρ = S`.  Amplitudes below (`M_1^O`,
`M_2^O`, and the clause-1 summand `E^O_desc`) are in the normalisation
convention of (b); clause 2's residue display is quoted in the
charge-created normalisation of `ml4-ward-reduction.md` (11), as stated in
that clause; clause 3b is empty without (b).  `𝒮_W(ρ)` is the class of
sources satisfying all five of (clause 3 has two parts; the *count* of
conditions is deliberately unchanged, so `paper/main.tex:244`
"five-condition" and the audit rows that quote it stay correct):
1. *Exhaustive normed LSZ decomposition* — in `L²(I)`, `M_2^O` is exactly
   the sum of the descendant external-leg term `E^O_desc`, the
   orthogonal-current term, and the direct source/contact term named below;
   there is no additional reduced term, and the equality holds in the same
   packet norm as (b).
2. *Ward covariance* — the descendant current residue, **quoted against
   the charge-created soft leg `Q_0|h⟩` — the normalisation of
   `ml4-ward-reduction.md` (11) — and not against (b)'s asymptotic
   leg**, factorises as `2i v_h M_1^O(h)`.  The two legs differ by
   exactly `√Z_ρ` ((b)(i)), and that mismatch is part of what clause
   3b's constant records: against (b)'s asymptotic leg the same residue
   reads `2i v_h M_1^O(h)/√Z_ρ`, the two readings coinciding only at
   `ρ = 1/2`.  (This clause is correct at every density: on the fully
   polarised spin-`S` tail the charge-created residue is exactly
   `Z_ρ`-linear, `⟨h|Q_0^†J^-_0|h⟩ = 2i v_S(h)` with
   `v_S(h) = Z_ρ J\sin h`; frozen `soft-current-recon.md` (R14) is its
   `Z_ρ = 1` reading — named computation D24N-C3 in
   `theory/checks/d24d3_normalization_check.py`, which displays the
   residue in both normalisations.)
3. *Kinematic LSZ normalisation*, in two parts:
   **(3a) hypothesis** — the external flux factor
   `L(k,h) := E^O_desc(k,h)/[(e^{ik}−1)\,2i v_h\,M_1^O(h)]` is well
   defined by clauses 1--2 for `k ≠ 0` at every `h` with `M_1^O(h) ≠ 0`;
   the hypothesis is that it extends to a process-independent, uniformly
   `C¹` function on `{|k| ≤ ε} × I`, and `L(0,h)` denotes that extension's
   value at `k = 0`.
   **(3b) the profile of `L(0,h)`, and the OPEN amputation constant** —
   `v_h\,L(0,h)/χ(h,0)` does not depend on `h` on `I`; equivalently
   `L(0,h) = 𝔞_leg(ρ)·(−iχ(h,0)/v_h)` for some nonzero constant
   `𝔞_leg(ρ)`.  **What this clause asserts is that `h`-profile — the
   reciprocal LSZ energy denominator `[ω(h+k)−ω(h)]^{-1}k`, the corpus's
   fixed provenance for `L` (`soft-current-recon.md` ⟨1⟩7,
   `paper/main.tex:524--527`, `soft-index-b.md:808`) — and no value.**  By
   (3a) `L` is a single class-level function, so `𝔞_leg(ρ)` is a datum of
   the class `𝒮_W(ρ)` and not of any individual source; it is defined
   only when that class is nonempty, and only in a register where the (b)
   asymptotic one-magnon kernel is constructed (currently the fully
   polarised spin-`S` family, D24N-C8; off that family, kernel existence
   is claim `ML1`, CONJECTURE).  **This definition fixes no value of
   `𝔞_leg(ρ)` at any density, `ρ = 1/2` included.**  As frozen, this clause
   stipulated `𝔞_leg = 1`, which under the corpus's jet-identification
   bridge contradicts PROVED `S2-2body-S` at every `ρ ≠ 1/2` (bd
   `tns-iu5`); that stipulation is withdrawn.  Two candidate readings are
   carried in `claims/CLAIMS.md` and neither is part of this definition:
   the conditional matched value `𝔞_leg(ρ) = 1/Z_ρ` (row `D24-VAL`,
   proved as an implication from the bridge plus class membership), and
   the open lemma **AMP** of the same value from a soft-leg amputation
   mechanism (row `AMP`, CONJECTURE).  Fence on AMP: by (b)(ii) a leg
   normalisation alone contributes `Z_ρ^{-1/2}` — the exact conversion
   between clause 2's charge-created residue normalisation and (b)'s
   asymptotic leg — and that value is refuted against the ansatz-free
   two-magnon data at the pre-registered band, so AMP requires a second
   factor `Z_ρ^{-1/2}` from a different mechanism
   (`theory/verdicts/d24d3-adjudication-r3.md` ⟨1⟩4; one-step form
   `theory/verdicts/d24d3-adjudication-r4.md` §1.3).  At `ρ = 1/2` the two
   candidate readings and the retired stipulation all coincide at `1`, so
   the D6 displays of the soft coefficient `2` remain numerically
   consistent with this clause; those displays rest on the contact/oracle
   route (`oracle-bethe.md` O7–O9; `paper/main.tex:515–520`), not on this
   clause;
4. *Reduced-channel regularity* — the orthogonal current channel is
   `O_{L²(I)}(k²)` in the stated target limit, with the relative norm
   bound of (b).  Fixed-volume ML4 does not by itself supply a
   volume-uniform bound;
5. **No direct soft contact** — the amputated source commutator/contact
   term is bounded by `C_I|k|²‖M_1^O‖_{L²(I)}`.

Hypotheses 1 and 5 are the extra LSZ/contact content beyond the fixed-volume
Ward reduction, and by (c) the zero-intercept and zero-first-jet conditions
are necessary, not cosmetic.  Symmetry-generated external-leg insertions are
the intended seed, but **no nontrivial microscopic class has been proved to
satisfy all five conditions**; nonemptiness in the target scattering
register is part of the ML5-B future work.  The `tns-iu5` adjudication of
clause 3 removed a *proof* that `𝒮_W(ρ)` is empty for `ρ ≠ 1/2` — as frozen,
clause 3 forced soft slope `2` at every density, contradicting PROVED
`S2-2body-S` given the jet-identification bridge — but it supplies no member
and fixes no value of `𝔞_leg(ρ)`, so nonemptiness stays open at every `ρ`
(bd `tns-axg`).
```

*(Diff against r3 §5.2, for the reviewer: the preamble sentence
"All amplitudes below are in the normalisation convention of (b); clause
3b is empty without it." is replaced; clause 2 gains its displayed
normalisation statement and the both-normalisations parenthesis; clause
3b gains the kernel-existence scope and the (b)(ii)-mismatch gloss on the
AMP fence with the r4 §1.3 pointer.  Every other line is byte-identical
to r3 §5.2, including clauses 1, 3a, 4, 5 and the closing paragraph,
which the critic ruled MERGE.)*

### 5.3 `claims/CLAIMS.md`

* **5.3a — ML5-B row (line 41): r3 verbatim** (ruled MERGE-after-F1;
  discharged).
* **5.3b — new row `D24-VAL`: r3 verbatim** (ruled MERGE-after-F1;
  discharged).
* **5.3d — ML5-A row (line 40): r3 verbatim** (ruled MERGE).

**5.3c′ — ADD a new row `AMP` (immediately after the `D24-VAL` row) —
REVISED (M5):**

```
| AMP | Soft-leg amputation lemma: for every `ρ` at which `𝒮_W(ρ) ≠ ∅` AND the D24(b) asymptotic one-magnon kernel exists (currently: the fully polarised spin-`S` family, named computation D24N-C8; off that family kernel existence is claim ML1, CONJECTURE), charge-created soft-leg amputation contributes the per-site order-parameter density `Z_ρ = 2ρ` to the external flux, i.e. `𝔞_leg(ρ) = 1/Z_ρ` — WITHOUT the D24-VAL bridge (α); dropping (α) is what distinguishes this row from D24-VAL, so the DAG does not double-count.  Like D24-VAL it is currently VACUOUS-OR-UNKNOWN: nonemptiness is open at every `ρ` (bd `tns-axg`), so the row constrains future work — any member ever exhibited must have this value if AMP holds — rather than supplying evidence now.  Originally named at theory/verdicts/soft-index-r1.md F1(c)(i).  Statable only relative to D24(b)'s convention: a change of normalisation rescales `𝔞_leg`, so before that convention the statement had no truth value (bd `tns-iu5` r2 critic F1).  **Quantitative fence (theory/verdicts/d24d3-adjudication-r3.md ⟨1⟩4; one-step form theory/verdicts/d24d3-adjudication-r4.md §1.3):** the leg-conversion factor is computed exactly — `Q^-_k|Ω⟩ = √(Z_ρ)|k⟩`, D24N-C8 — and is the exact mismatch between clause (d)2's charge-created residue normalisation and (b)'s asymptotic leg, so a leg normalisation alone supplies only `Z_ρ^{-1/2}`, a value the ansatz-free data refutes at the PRE-REGISTERED band (`--red-halfpower`, deviations 0.42/0.73/1.00 vs band 0.08).  AMP is therefore true only if a second factor `Z_ρ^{-1/2}` arises from a mechanism that is NOT a leg normalisation; any proposed proof must be checked against D24N-C8 or it double-counts the leg. | CONJECTURE | D24(b), D24(d) | — | theory/checks/d24d3_normalization_check.py D24N-C8 (the leg-conversion constant, vacuum and descendant legs); D24N-C6 `--red-halfpower` (the leg-normalisation-only value refuted) |
```

### 5.4 `notation.md` (the L4 symbol registry)

**5.4a′ — ADD to the ML4/ML5/M-quant symbol table (after the `𝒮_W(ρ)` row
at line 258) — the `𝔞_leg(ρ)` row is REVISED (M1); the other three rows
are byte-identical to r3 §5.4a:**

```
| `L(k,h)`, `L(0,h)` | D24(d)3a external flux factor: the descendant quotient `E^O_desc/[(e^{ik}−1)·2iv_h·M_1^O(h)]`, defined for `k ≠ 0` where `M_1^O(h) ≠ 0`; `L(0,h)` is the value at `k=0` of the hypothesised `C¹` extension.  D24(d)3b asserts its `h`-profile — the reciprocal LSZ energy denominator, whose provenance in the corpus (`soft-current-recon.md` ⟨1⟩7; `paper/main.tex:524–527`; `soft-index-b.md:808`) is written in the D6 register `ρ = 1/2` and fixes the profile, not the constant.  `L(0,h) = 𝔞_leg(ρ)·(−iχ(h,0)/v_h)`.  Normalisation-dependent: `L ↦ (c′/c)L` under D24(b)'s rescalings | definitions.md D24(d)3 |
| `Z_ρ` | order-parameter density `2ρ`; for an su(2) model with a fully polarised α tail, `Z_ρ = ω_α([S^+_x, S^-_x])`.  Subscripted deliberately: bare `Z` stays Pauli-reserved (overload rule 9, unchanged) | definitions.md D24(d) |
| `𝔞_leg(ρ)` | soft-leg amputation constant of D24(d)3b, `𝔞_leg(ρ) := i v_h L(0,h)/χ(h,0)`; a datum of the class `𝒮_W(ρ)`, defined only when that class is nonempty AND only in a register where the D24(b) asymptotic one-magnon kernel is constructed (currently the fully polarised spin-`S` family, D24N-C8; off it, kernel existence is claim ML1, CONJECTURE); constant in `k`, `h` and `O` but NOT in `ρ`.  Meaningful only in the D24(b) normalisation convention, which rescales it.  Value OPEN: conditionally matched `= 1/Z_ρ` by claim D24-VAL; asserted `= 1/Z_ρ` by the CONJECTURE row AMP (scoped, without the bridge); `= 1` as frozen (withdrawn).  Written bare `𝔞_leg` inside a fixed-`ρ` display (overload rule 13) | definitions.md D24(d)3b |
| `E^O_desc` | descendant external-leg term of the D24(d)1 decomposition (fraktur `𝔈` avoided: `𝔈_W`, `𝔈_{A_α}`, `𝔈_{A_β}` are the window CP maps); not a transfer map — see overload rule 8 | definitions.md D24(d)1 |
```

**5.4b′ — REPLACE the `𝒮_W` row (line 258) — REVISED (M4 licensing
clause):**

```
| `𝒮_W(ρ)` | the ρ-indexed five-condition Ward/LSZ/no-contact source class in the repaired conditional ML5-B implication; `ρ := ω_α(S^z) > 0`.  Written bare `𝒮_W` where the density is fixed or immaterial — the D24 section header, D25, the CLAIMS rows quantifying over the class (`S-general` and the corner-implication prose), `ml5-universality.md`, and the Letter (`\mathcal{S}_W`) | definitions.md D24(d) |
```

* **5.4c — `𝖲(k_s;{q_i,v_i})` row (line 244): r3 verbatim** (ruled MERGE).
* **5.4d — overload rule 2 amendment: r3 verbatim** (ruled MERGE).
* **5.4e — overload rule 8 amendment: r3 verbatim** (ruled MERGE).
* **5.4f — new overload rule 13: r3 verbatim** (ruled MERGE; 13 confirmed
  the next free number, X6).

### 5.5′ ADVISORY — same-commit obligations (NOT optional; r3 items 1–9 plus five new)

Items 1–9: as r3 §5.5, unchanged (the critic ruled §5.5 MERGE "and NOT
optional", instructing that it be extended).  New items:

10. **(M4)** The 18-site rename disposition of §3: TRIANGLE.md's five
    sites renamed (this is item 2, unchanged); the other 13 sites are
    left untouched and are legal under §5.4b′'s licensing clause — no
    edit to `definitions.md:916/1004`, `claims/CLAIMS.md:29/82`,
    `ml5-universality.md`, or `paper/main.tex` on account of the rename.
11. **(m3)** Apply the `notation.md` edits in the order given under
    Mechanics above (b′, a′, c, f, e, d) — descending line order.
12. **(m4)** ERRATUM-free citation notes at the two `D24(b)` sites, in
    the same commit: at `theory/ml4-ward-reduction.md:63–68` append the
    one-sentence note "*(bd `tns-iu5` r4: D24(b)'s leg-normalisation
    convention is strictly narrower than this ML4-admissible class —
    D24(b) soft-leg envelopes must have `λ(0) = 1`; conclusions drawn
    here about ML4-admissible amputations do not transfer to D24(b)
    amplitudes unless they respect that restriction.)*"; at
    `theory/ansatz-scattering-2m.md:621–631` (the ⟨2⟩5 step using "the
    normalized multiplier amputation of D24(b)") append "*(bd `tns-iu5`
    r4: this `S_phys`-valued amputation coincides with the D24(b)
    convention only in this shard's D6 register `ρ = 1/2`; it is not the
    D24(b) convention in general.)*"
13. **(m8)** One-clause scoping edit at `theory/TRIANGLE.md:216–218`, in
    the same commit: after "`𝖲(k_s) = 2ik_s`" and its "**SKETCH**,
    conditional on wave operators (ML1) and the amputation convention"
    label, append "*(the D24(b) convention, now displayed; in this D6
    register the coefficient is `2`; on the general class the same
    statement carries `2𝔞_leg(ρ)` with `𝔞_leg(ρ)` OPEN, D24(d)3b)*".
14. **(m6)** One sentence added to the H8 paragraph when r3's §5.5 item 8
    updates `HANDOFF.md`, and recorded here for the record (see §7):
    after the merge, for every source with `M_1^O ≠ 0` the ML5-A
    membership test through `𝔠_h` is undecidable until AMP or `tns-axg`
    closes, because `𝔠_h` contains the open constant `𝔞_leg`; D24(e)'s
    counterexamples remain decidable (`M_1^O = 0`, W14).

---
