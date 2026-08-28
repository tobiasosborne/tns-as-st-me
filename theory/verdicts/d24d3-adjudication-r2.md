<!-- ROLE: orchestrator-lane ADJUDICATION of corpus referral bd `tns-iu5`,
     repair round 2, after the FAIL(F1,F2,F3,M1–M7) verdict
     theory/verdicts/d24d3-adjudication-r1-critic.md.
     Work orders: briefs/d24d3-adjudication.md (r1), briefs/d24d3-repair-r2.md.
     Writable files of this lane: this file,
     theory/verdicts/d24d3-repair-r2-response.md, and
     theory/checks/d24d3_normalization_check.py — nothing else was edited.
     definitions.md, notation.md and claims/CLAIMS.md are NOT edited here;
     all shared-file text is quarantined in §5 MERGE PROPOSALS.
     STRUCTURAL PROVENANCE (r1-critic M1 correction, stated plainly): the
     bookkeeping home adopted here — density in a named soft-leg amputation
     constant, flux factor kept kinematic — is structurally lane B's split
     (soft-index-b.md B14), with lane B's factor now carried as a NAMED OPEN
     LEMMA instead of an undefended multiplication; the r1 artifact's
     structure (density folded inside the flux value) was structurally
     lane A's (soft-index.md:161–162), contrary to its own ROLE header.
     Neither lane's *justification* is imported; no lane derived the factor
     and this adjudication does not either. -->

# r2 adjudication — D24(d) clause 3, the external-flux normalisation

**Verdict.  The frozen clause 3 is REFUTED as a universal value claim
(conditional on the corpus's jet-identification bridge — unchanged from r1,
independently confirmed by the r1 critic, V4/V5/V7).  The repair is now
smaller than r1 attempted, and honest:**

* **Clause 3 is SPLIT.  (3a)** is the well-posed kinematic hypothesis —
  `L` defined as the descendant quotient for `k ≠ 0`, with the `C¹`
  extension to `k = 0` stated as part of the hypothesis (r1-critic V8 + M7).
* **(3b)** records the **normalisation split**: `L(0,h) = 𝔞_leg·(−iχ/v_h)`.
  The kinematic factor `−iχ/v_h` — the **frozen value** — is kept, because
  the corpus fixes `L`'s provenance as the reciprocal LSZ energy denominator
  in three places (`soft-current-recon.md` ⟨1⟩7, `paper/main.tex:524–527`,
  `soft-index-b.md:808`), and that construction *carries* `Z_ρ` through
  `v_h = Z_ρ J sin h` and cancels it against the residue's `Z_ρ`, leaving no
  room for a density inside `L` (r1-critic F2, adopted in full).  The
  density lives in the **soft-leg amputation constant `𝔞_leg`**, whose value
  is an OPEN lemma — **AMP**, `𝔞_leg = 1/(2ρ)`, already named at
  `theory/verdicts/soft-index-r1.md` F1(c)(i) — and is **NOT fixed by the
  definition**.
* **The value `L(0,h) = −iχ/(2ρ v_h)` is RETIRED from `definitions.md`**
  (the r1 critic's third horn, F1(d′), is ADOPTED).  It survives as the
  **conditional claim row `D24-VAL`** (CONJECTURE): given the
  jet-identification bridge, on-shell matching against PROVED `S2-2body-S`
  forces `𝔞_leg = 1/(2ρ)` at `ρ = S ∈ {1/2, 1, 3/2, 2}` in the fully
  polarised spin-`S` register, for any member of the class in that register.
  No step in this document asserts, or needs, that such a member exists.
* At `ρ = 1/2`, `1/(2ρ) = 1` and the frozen clause is recovered verbatim
  under either reading; the D6 corpus (O7–O9, (R14), (R17), Theorem
  `thm:soft`) is untouched.

**`𝒮_W(ρ)` nonemptiness stays OPEN at every `ρ` (bd `tns-axg`), and
`tns-axg` and `tns-iu5` are coupled: the matched value cannot be upgraded
past CONJECTURE until either a member is exhibited or AMP is proved.**

Certificate: `theory/checks/d24d3_normalization_check.py`, rebuilt per
r1-critic M3 (green `python3 -O` exit 0; red modes `--red-frozen`,
`--red-power`, `--red-halfpower` die at **D24N-C6**, `--red-ward` dies at
**D24N-C3** — exit *paths*, not just codes, in §7).

---

## 0. What this round did, and what it did not touch

**Fenced (r1-critic §1, V1–V14 — certified, not re-derived here).**
`Z_ρ = 2ρ = 2S` and the soft-leg norm `‖Q^-_k|Ω⟩‖²/N = 2S` (V1);
`ω_S(k) = 2JS(1−cos k)`, `v_S(h) = Z_ρ J sin h` (V2); the exact Ward residue
`⟨h|Q_0^†J^-_0|h⟩ = 2i v_S(h)` at every `Z_ρ` (V3); the frozen clause's
exact density-blindness (V4); the exact slope `∂_{k_s}log S_{12}|_0 = i/S`
(V5); the frozen data and its independent ED reproduction (V6); the
collision and hence emptiness-given-the-bridge (V7); nonvacuity of the
quotient definition of `L` (V8); `v_h` bounded below on `I` (V9); the L3
Watanabe–Murayama quotation (V10); checker green/red reproduction (V11);
every §4.3 "does not change" claim (V12); the line anchors and the
five-condition count (V13); the VALUE arithmetic `2·(2ρ)^{-1} = 1/ρ` and
the exponent forcing (V14).  None of these is re-litigated below; leaves
cite them as `r1-critic V*`.

**Done this round (no new physics — the physics was done and fenced):**

* **(R2-a)** The status architecture rebuilt: value retired from the
  definition (F1, third horn), density relocated to the named open
  amputation lemma AMP (F2), `Z_ρ` defined in state language without the
  D6 ket `|Ω⟩` and without bare-`Z` collision (F3).
* **(R2-b)** The strawman refutation of the S1 lanes withdrawn and replaced
  by what is true (M1); the "load-bearing" narrative of r1's ⟨1⟩3 demoted
  to a consistency check of clause 2 (M2); the Holstein–Primakoff structural
  argument restated as an open question (M2).
* **(R2-c)** Checker rebuilt (M3): the tautological soft-leg-norm gate
  replaced by an actual construction of `Q^-_k|Ω⟩`; the `lstsq(x,x)`
  exact-law gate replaced by a symbolic solve of `2(2S)^{-p} = 1/S`; the
  acceptance gate D24N-C6 given an **independent failure mode** (band
  `0.02`, not deductively implied by D24N-C4's pre-registered `0.08` —
  demonstrated by a data mutant that passes C4 and dies at C6); the
  `decision_band` key made mandatory; exit paths and resolving power
  reported (§7).
* **(R2-d)** Quantifiers fenced (M4): the matching claim is stated at
  `ρ = S ∈ {1/2,1,3/2,2}` in one model family, extension to other `ρ` by
  hypothesis; the `M-IDX-density` citation carries its load-bearing
  ANTISYMMETRY hypothesis.
* **(R2-e)** The two binding decisions of `soft-index-adjudication-r1.md`
  §3.2/§3.5 acknowledged and complied with (M5) — §4.5.
* **(R2-f)** Blast radius completed (M6): the five missed sites added,
  including the two in `notation.md`, and a full `notation.md` merge pass
  proposed (§4.2b, §5.4).  Clause 3a restored to its `k ≠ 0` form with the
  extension hypothesis displayed (M7).

**Symbols of this round (all registered in §5.4; none exists yet in
`notation.md`):** `Z_ρ := 2ρ` (order-parameter density; bare `Z` is
Pauli-reserved by overload rule 9); `𝔞_leg` (soft-leg amputation constant;
bare `𝔞` would collide with the twisted group algebra `𝔞_α` of the SPT
corner); `E^O_desc` (descendant external-leg term; r1's `𝔈^O` collided with
the `𝔈_W` CP maps, r1-critic m1); `L(k,h)` itself (the genuine L4 gap —
no `notation.md` row existed, r1-critic F2 narrow finding).

---

## 1. The defect, and its root cause — corrected

### 1.1 The defect (unchanged from r1; fenced)

The frozen clause 3 value `L(0,h) = −iχ/v_h` makes ML5-B (6)'s jet
identically `2χ`, with `∂_ρ[jet] = ∂_{v_h}[jet] = 0` (r1-critic V4, named
computation D24N-C1).  PROVED `S2-2body-S` gives jet `χ/S`, exactly, at
every `S` (r1-critic V5).  Under the corpus's jet-identification bridge
(§1.3 of r1; the bridge is NOT a PROVED row — HONEST STATUS H5) these
collide except at `S = 1/2`, so the frozen `𝒮_W` is provably empty in the
spin-`S` ferromagnet register at every `ρ ≠ 1/2` (r1-critic V7).  The
frozen clause cannot stand.

### 1.2 Root cause — CORRECTED (r1's §1.5 premise was false in substance)

r1 claimed "`L` is never defined anywhere in the corpus".  That claim is
**withdrawn**.  The truth has two parts (r1-critic F2, verified against the
cited lines this round):

* **Narrow (the real L4 gap).**  There is no `notation.md` row for `L` and
  no `L :=` anywhere in `definitions.md`, `notation.md`, `claims/`,
  `theory/`, or `paper/`.  As a symbol-registry defect this is genuine, and
  §5.4 repairs it.  r1's grep also missed `theory/soft-index.md:161–162`,
  where lane A's D29 names a "canonical flux factor"
  `L_λ(0,h) = −i sgn(v_h−v_s)/(2ρ_λ v_h)` — the exact value r1 re-derived;
  the pattern `L(k,h)|L(0,h)` cannot match the subscripted `L_λ`.
* **Substantive (the object's provenance IS fixed, three times, and it
  forces the frozen value).**  The corpus constructs the `1/v_h` in `L` as
  the **reciprocal LSZ energy denominator**:
  1. `theory/soft-current-recon.md` ⟨1⟩7 (ML4 plan): "The pole denominator
     is `ω(k_h+k_s)−ω(k_h) = v_h k_s + O(k_s²)`; combine it with (R14) and
     `e^{ik_s}−1`."
  2. `paper/main.tex:524–527`: "dividing a hard external-leg reduction by
     the energy shift `v_h k_s` cancels the velocity and leaves the `2`."
  3. `theory/soft-index-b.md:808`: "the `1/v_h` is the on-shell pole
     residue `[ω(h+k_s)−ω(h)]^{-1}·k_s`."

  Now compute (r1-critic V2/V3): `v_h = Z_ρ J sin h` carries one power of
  `Z_ρ`, the Ward residue `2i v_h` carries the same power, and the
  reciprocal-denominator construction cancels them exactly — jet `2χ` at
  **every** density.  So the corpus's own construction of `L` *reproduces
  the frozen value and the defect with it*.  The missing `1/(2ρ)` is not a
  factor clause 3 "lost"; it is a factor **neither clause 2 nor the
  kinematic part of clause 3 has a home for**.  Its true home was already
  named, as an open lemma, at `theory/verdicts/soft-index-r1.md` F1(c)(i):
  *"charge-created soft-leg amputation contributes the per-site leg density
  `2ρ` to the external flux."*  That lemma — **AMP** below — is unproved,
  and nothing in this adjudication proves it (r1's only structural argument
  for it, ⟨1⟩3.⟨3⟩4, gave `Z^{-1/2}` on its own terms and is restated as an
  open question in §2 ⟨1⟩4).

### 1.3 Consequence for the shape of the repair

Because the corpus's construction of `L` forces the frozen value, putting
`1/(2ρ)` *inside* `L` (r1's §5.2 clause 3b) would install into the L4 file
a value contradicting three corpus statements of what `L` is — creating an
L4 inconsistency while claiming to remove one (r1-critic F2, consequence
paragraph).  The repair therefore takes the critic's option (i): the
kinematic value `−iχ/v_h` stays with `L`; the density moves to the named
amputation constant `𝔞_leg`; and — taking the third horn (F1(d′))
seriously — the *matched* value `𝔞_leg = 1/(2ρ)` is retired from the
definition entirely, because the matching that supplies it quantifies over
a class whose inhabitation is open (`briefs/critic-protocol.md` §5 forbids
relying on `𝒮_W` nonemptiness at `ρ ≠ 1/2` while `tns-iu5` is open, and
§4.4 keeps nonemptiness open at every `ρ`).  A universally quantified
matching over a possibly empty class determines no constant; what it does
support is a **conditional implication** — any member must have
`𝔞_leg = 1/(2ρ)` — and that implication, with its two conditions displayed,
is exactly claim `D24-VAL` (§5.3).

---

## 2. The adjudication (Lamport)

The claim proved this round is deliberately smaller than r1's "THEOREM
D24N".  Nothing here is called a derivation of the value.

**PROPOSITION D24N′ (repaired clause-3 architecture).**

**ASSUME.**  D24(a)–(b); D24(d) clauses 1 and 2 (with the descendant
external-leg term named `E^O_desc`); a broken-symmetry tail density
`ρ := ω_α(S^z) > 0` in the sense of `notation.md`'s `ρ`-row.  Where
`2ρ ∈ ℤ` is used, additionally (S) at both tails, D26(INT), **and the
antisymmetric tail pair `ω_β(S^z) = −ω_α(S^z) = −ρ`** (the load-bearing
hypothesis of PROVED `M-IDX-density`; r1-critic M4(ii)).

**PROVE.**  (i) Clause (3a) as stated in §5.2 is well posed and nonvacuous;
(ii) the corpus's fixed provenance of `L` gives the kinematic value
`−iχ/v_h` at **every** density, so the density cannot enter through `L`'s
kinematic part, and the residual constant `𝔞_leg := i v_h L(0,h)/χ` is the
only place it can live; (iii) *conditionally* — given the
jet-identification bridge — every member of `𝒮_W(S)` in the fully polarised
spin-`S` register has `𝔞_leg = 1/(2S)`, `S ∈ {1/2, 1, 3/2, 2}`, and within
the family `𝔞_leg = (2ρ)^{-p}` the exponent is `p = 1`.

### ⟨1⟩1.  Clause (3a) is well posed and nonvacuous

**⟨2⟩1. PROVE.**  Under D24(d)1–2 the quotient

    L(k,h) := E^O_desc(k,h) / [ (e^{ik}−1) · 2i v_h · M_1^O(h) ]   (D24N.3′)

is well defined **for `k ≠ 0`, at every `h` with `M_1^O(h) ≠ 0`**; the
(3a) hypothesis is that it extends to a process-independent, uniformly
`C¹` function on `{|k| ≤ ε} × I`, and `L(0,h)` denotes that extension's
value at `k = 0`.

**⟨3⟩1.**  `E^O_desc` is a named summand of clause 1's exhaustive
decomposition, and clause 2 factorises its residue as `2i v_h M_1^O(h)`;
`(e^{ik}−1)` is the kinematic factor of ML5-B (6).  So the quotient is
exactly what clauses 1–2 leave over.  It is undefined at `k = 0`
(`e^{ik}−1 = 0`) and on the zero set of `M_1^O` — `M_1^O ∈ L²(I)` with
`M_1^O ≠ 0` as an `L²` element does *not* give pointwise nonvanishing, so
the domain may have holes (r1-critic M7(b)(ii)).  Both restrictions are
therefore part of the displayed hypothesis, and `L(0,h)` names an
extension value, never a quotient value.
Justification: D24(d)1–2; r1-critic F1(b)(i), M7 — adopted.

**⟨3⟩2.**  Nonvacuity: with `L` so defined, "process independent" is the
substantive requirement that the extension agree across all `O` in the
class — a real constraint, not a tautology.
Justification: r1-critic V8 (checked directly by the critic).

**⟨3⟩3. QED.**

### ⟨1⟩2.  The kinematic value, and why the density cannot live in `L`

**⟨2⟩1. PROVE.**  The corpus's construction of `L` — the reciprocal LSZ
energy denominator — evaluates to `−iχ/v_h` at every tail density, and the
residual constant `𝔞_leg := i v_h L(0,h)/χ` is dimensionless,
`h`-independent under (3b), and is where any density dependence must sit.

**⟨3⟩1.**  Provenance: the three corpus sites quoted in §1.2 all construct
the `1/v_h` as `[ω(h+k)−ω(h)]^{-1} k`.  On the spin-`S` tail
`ω_S(k) = 2JS(1−cos k)`, so `v_h = Z_ρ J sin h`: the denominator carries
one power of `Z_ρ`.
Justification: `soft-current-recon.md` ⟨1⟩7; `paper/main.tex:524–527`;
`soft-index-b.md:808`; r1-critic V2.

**⟨3⟩2.**  The Ward residue in the numerator carries the same power:
`⟨h|Q_0^†J^-_0|h⟩ = 2i v_S(h) = Z_ρ · 2iJ sin h`, exactly, at
`2S = 1,2,3,4`.
Justification: r1-critic V3; named computation D24N-C3.

**⟨3⟩3.**  In the product `(e^{ik}−1) · L_kin · [2i v_h M_1^O]` with
`L_kin(0,h) = −iχ/v_h`, the two powers of `Z_ρ` cancel exactly: the jet is
`2iχ k M_1^O` at every density.  This is the *correct* cancellation of a
correct residue against a correct reciprocal energy denominator — nothing
is "lost" here (r1's contrary narrative is struck; see ⟨1⟩4.⟨2⟩1).  The
consequence is structural: **no bookkeeping internal to clauses 2 and 3's
kinematics can produce a density dependence.**  Any density factor is an
*addition*, and its named home is the soft-leg amputation.
Justification: ⟨3⟩1–⟨3⟩2; r1-critic V4, F2 (adopted); named computation
D24N-C1.

**⟨3⟩4.**  Definition of the residual: `𝔞_leg := i v_h L(0,h)/χ`, i.e.
`L(0,h) = 𝔞_leg · (−iχ/v_h)`.  The (3b) membership condition is that
`𝔞_leg` is a nonzero constant independent of `k`, `h`, and `O`
(`O`-independence already follows from (3a); `h`-independence is a genuine
additional membership hypothesis).  The frozen clause is the stipulation
`𝔞_leg = 1`.  The open lemma **AMP** (`soft-index-r1.md` F1(c)(i)) asserts
`𝔞_leg = 1/(2ρ) = 1/Z_ρ`; at `ρ = 1/2` the two agree.
Justification: definition; ⟨3⟩3 for why the split is exhaustive.

**⟨3⟩5. QED.**

### ⟨1⟩3.  The conditional matching (the content of claim `D24-VAL`)

**⟨2⟩1. ASSUME.**  (α) the jet-identification bridge — the jet of the
D24(d) soft multiplier equals the jet of the two-body physical phase
(corpus identification via (R17), `oracle-bethe.md` O9; NOT a PROVED row —
H5); (β) a member `O ∈ 𝒮_W(S)` exists in the fully polarised spin-`S`
register `H_S = −JΣ_x(S_x·S_{x+1} − S²)` with `M_1^O ≠ 0`, for some
`S ∈ {1/2, 1, 3/2, 2}`.

**PROVE.**  `𝔞_leg = 1/(2S)`.

**⟨3⟩1.**  By (β) and ⟨1⟩1–⟨1⟩2, the ML5-B multiplier of that member is
`𝖲(k;h) = (e^{ik}−1)·𝔞_leg·(−iχ/v_h)·2i v_h = 2iχ 𝔞_leg k + O(k²)`.
Justification: ML5-B (6); ⟨1⟩2.⟨3⟩4.

**⟨3⟩2.**  By (α), the same jet equals the PROVED two-body physical jet
`i(χ/S) k` of `S2-2body-S` (T.3) with `ρ = S`.  Equating coefficients:
`2𝔞_leg = 1/S`, i.e. `𝔞_leg = 1/(2S) = 1/(2ρ)`.
Justification: `S2-2body-S` (PROVED); assumption (α).

**⟨3⟩3.**  Exponent uniqueness, stated at its true strength (r1-critic m4):
within the family `𝔞_leg = (2ρ)^{-p}`, the exact law `2(2S)^{-p} = 1/S`,
i.e. `(2S)^p = 2S`, forces `p = 1` at **any single** `S` with `2S ≠ 1`; the
`S = 1/2` point is degenerate (`1^p = 1` for every `p`) and contributes
nothing.  So the exponent is pinned by two or more distinct half-integer
`S`, not "four independent measurements" — the four densities are four
points of one analytic curve from one PROVED theorem.  The numerical fit to
the ansatz-free data (`p̂ = 1.0024`, §7) is corroboration, not the pin.
Justification: symbolic solve, named computation D24N-C6 (rebuilt); the
data fit D24N-C6.

**⟨3⟩4. QED — and the status boundary.**  ⟨3⟩1–⟨3⟩3 prove a *conditional
implication*: (α) ∧ (β) ⇒ `𝔞_leg = 1/(2S)`.  If (β) fails at every `S`
(possible: §4.4), the implication is vacuous and fixes nothing; if (α)
fails, it has no contact with any PROVED row.  Therefore the value is
**not** installed in `definitions.md` — it is carried as claim `D24-VAL`
(CONJECTURE, conditions displayed, §5.3).  This complies with binding
`soft-index-adjudication-r1.md` §3.2 ("the r2 statement takes the value
from on-shell input … conditional on an on-shell matching hypothesis,
named and displayed") — see §4.5.

### ⟨1⟩4.  Demotions and corrections (consistency material, carrying no load)

**⟨2⟩1.  The residue's `Z_ρ`-linearity is a consistency check of clause 2,
not the load-bearing step.**  (D24N.4)'s `⟨h|Q_0^†J^-_0|h⟩ = 2i v_S(h)` is
an identity once the dispersion is known; "the `Z`-carrying reading" and
"the `Z`-free kinematic number" differ only by substituting
`v_h = Z_ρ J sin h`, and D24(d)2's `2i v_h` is correct at every `Z_ρ`.
r1's sentences "this is the load-bearing step: it is where the density
actually lives" and "that single cancellation is the entire defect" are
**struck**.  What D24N-C3 certifies is that clause 2 needs no repair.
Justification: r1-critic M2, V3 — adopted.

**⟨2⟩2.  What the S1 lanes actually said (r1's ⟨1⟩5 strawman withdrawn).**
Lane B's operative factor (`soft-index-b.md:802–811`, B14 bullet 2) is the
per-volume leg density `1/(2ρ)` — `N`-free, and *the same invariant this
adjudication uses*; its `(2ρN)^{-1/2}` sentence is a stray parenthetical,
and its displayed product does not terminate in an uncancelled `N^{±1/2}`.
Lane A asserted `L_λ(0,h) = −i sgn(v_h−v_s)/(2ρ_λ v_h)` directly
(`soft-index.md:161–162`); the `(2ρN)^{-1/2}` route r1 refuted was the
**S1-A critic's counter-analysis** (`soft-index-r1.md` F1(b)4), not either
lane's claim.  What survives of r1's ⟨1⟩5: a bare unit-normalisation of the
single soft leg gives `Z_ρ^{-1/2}`, not `Z_ρ^{-1}` — so the S1-A critic's
proposed mechanism cannot be the mechanism.  Neither lane derived the
factor; neither does this adjudication; lane B's *bookkeeping home* (a
separate per-volume density factor) is the one adopted here, now as the
named open lemma AMP.
Justification: r1-critic M1 — adopted; the cited lines re-read this round.

**⟨2⟩3.  The mechanism is an open question, stated as such.**  r1's
⟨1⟩3.⟨3⟩4 (Holstein–Primakoff two-insertion count) is deleted, not
demoted: on its own bookkeeping, normalising the one external soft leg
divides by `√Z_ρ` and leaves `√Z_ρ` — the half-power — contradicting the
conclusion it was written to support (r1-critic M2(b)).  The honest state:
the matched power is `1` (⟨1⟩3, conditional); a `√Z_ρ` leg normalisation
would give `1/2`; **so whatever mechanism AMP names, it is not a leg
normalisation** — consistent with `soft-index-r1.md` F1(b)5.  Proving AMP
(an LSZ amputation computation for the charge-created soft leg) is the open
lemma; it is coupled to `tns-axg` (§4.4).
Justification: r1-critic M2(c) — the restatement it demanded.

**⟨2⟩4.  Watanabe–Murayama fixes the invariant, not the factor 2.**  The
type-B symplectic density `ρ_{ij} = −i⟨0|[Q_i, j^0_j]|0⟩` identifies `Z_ρ`
(in the complexified basis) as *the* natural per-site density of the broken
pair — "consistent with", not "exactly" the AMP factor: WM's own
normalisation is `m = ρ`, not `2ρ`, and using it in a structural count
would give jet `2χ/ρ`.  The factor of 2 is fixed only by the matching.
Justification: r1-critic m5 — adopted; L3 quotation fenced as V10.

**⟨2⟩5. QED.**

---

## 3. Acceptance check (fixed in advance by the r1 work order)

The acceptance arithmetic now certifies claim `D24-VAL` (the conditional
matched value), NOT a definitional clause.  Predicted jet `2·𝔞_leg` with
`𝔞_leg = (2ρ)^{-p}`, `ρ = S`, against the ansatz-free `A_ring_summary`
extrapolations (unchanged data; table fenced as r1-critic V6/V14 and r1 §3):

| `S = ρ` | measured (ansatz-free) | `1/S` | frozen `𝔞_leg=1` | rel. dev. | matched `p=1` | rel. dev. |
|---|---|---|---|---|---|---|
| 1/2 | 1.9991 | 2.0000 | 2.0000 | 0.000 ✅ | 2.0000 | 0.000 ✅ |
| 1   | 0.9984 | 1.0000 | 2.0000 | 1.002 ❌ | 1.0000 | 0.002 ✅ |
| 3/2 | 0.6649 | 0.6667 | 2.0000 | 2.003 ❌ | 0.6667 | 0.003 ✅ |
| 2   | 0.4983 | 0.5000 | 2.0000 | 3.003 ❌ | 0.5000 | 0.003 ✅ |

* reproduces **`1/S`** at `S ∈ {1/2,1,3/2,2}` — ✅ (D24N-C6, acceptance
  band `0.02`, tighter than and independent of D24N-C4's pre-registered
  `0.08`; §7)
* reproduces **`2`** at `ρ = 1/2` — ✅ (exactly; `𝔞_leg = 1` under AMP)
* leaves every other clause of D24(d) intact — ✅ for clauses 1, 2, 4, 5
  (clause 1's summand renamed `E^O_desc`, clause 2 unchanged in content);
  **D24(c) must move in lockstep** (§4.1 B3–B4), now parametrically in
  `𝔞_leg` rather than in `ρ` — which also removes r1-critic m3's
  model-dependence: (c) no longer mentions `ρ` at all.

The two anchor conditions are not independent (`ρ = 1/2` *is* the
`S = 1/2` member), and the four densities are one analytic curve
(⟨1⟩3.⟨3⟩3).  What makes the matched value non-fitted is the symbolic
exponent pin at any single `2S ≠ 1` plus the `±1.2%` resolving band of the
rebuilt D24N-C6 (§7) — stated as corroboration of a CONJECTURE row, not as
a derivation.

---

## 4. Blast radius

Every address below was obtained by grep this round; r1's list is retained
where the r1 critic verified it (V12, V13, M6 parenthetical) and extended
by the five sites M6 found missing.

### 4.1 Text that MUST change (merge proposals in §5)

| # | Address | What changes | Why |
|---|---|---|---|
| B1 | `definitions.md:952–973` — D24(d) | preamble: `𝒮_W` → `𝒮_W(ρ)`, `ρ > 0` fence, `Z_ρ` in state language, ANTISYMMETRY restored to the `M-IDX-density` citation; clause 1: summand named `E^O_desc`; clause 3: split into (3a) hypothesis (`k ≠ 0`, `C¹` extension) + (3b) normalisation split with `𝔞_leg` OPEN | the referral; F1, F3, M4, M7, m1 |
| B2 | `definitions.md:931–950` — D24(c) | `2i χ(h,0) M_1^O` → `2i 𝔞_leg χ(h,0) M_1^O` in `𝔠_h` and in the ML5-A criterion display and `K_O` bound (parametric in `𝔞_leg`, no `ρ`) | lockstep: `𝔠_h` is by definition the obstruction to the factorisation (d) predicts; r1 B3/B4, m3 dissolved |
| B3 | `claims/CLAIMS.md:41` — row ML5-B | status stays PROVED; displayed conclusion `2i 𝔞_leg χ k M_1^O`, with the AMP/`D24-VAL` readings noted | the implication survives verbatim with `𝔞_leg ≠ 0` carried (its proof never uses the value) |
| B4 | `claims/CLAIMS.md` — NEW row **D24-VAL** | the conditional matched value (CONJECTURE) | ⟨1⟩3; the retirement home of the value |
| B5 | `claims/CLAIMS.md:40` — row ML5-A | add the constant-agnostic sentence | r1 B6; r1-critic §7 |
| B6 | `notation.md` — NEW rows | `L(k,h)`, `Z_ρ`, `𝔞_leg`, `E^O_desc`; `𝒮_W` row updated to `𝒮_W(ρ)` (lines 244, 258) | F2 (narrow), F3(c), M6, m1 |

### 4.2 Shard steps to re-typeset in lockstep (not this lane's files)

`theory/ml5-universality.md` (r1's §4.2 table stands, with the constant now
`2i𝔞_leg χ` instead of `iχ/ρ`; verified addresses fenced as r1-critic M6
parenthetical):
⟨1⟩2 eqs. (3), (4), (4b); ⟨1⟩3 hypothesis 3 (lines 142–144: `L` as the
(3a) quotient, `L(0,h) = 𝔞_leg(−iχ/v_h)` with `𝔞_leg` open); ⟨1⟩3 eq. (5)
boxed (line 155); ⟨1⟩3 ⟨2⟩1.⟨3⟩2 (lines 170–172: needs only
`𝔞_leg ≠ 0` and `v_h` bounded below — r1-critic V9); **line 158** ("the
coefficient is the signed **two-site** Wigner displacement" → "signed
`2𝔞_leg`-site Wigner displacement; `two-site` is the `𝔞_leg = 1`, `ρ = 1/2`
register" — M6 row 3); ⟨1⟩3 ⟨2⟩3 (lines 183–184); ⟨1⟩6 item 3 (lines
324–327); shard header ERRATUM pointer.

`theory/TRIANGLE.md:24, 215, 254, 257, 528` — `𝒮_W` → `𝒮_W(ρ)`
cross-reference refresh only (no constant displayed; r1-critic V12).

**Failed-lane records (n3):** `theory/soft-index.md:161–162` and
`theory/soft-index-b.md:757–758, 808` display flux/leg-density text that
the merged D24(d) supersedes.  They are failed-lane records: an ERRATUM
pointer at each shard head (style of `ml4-ward-reduction.md`) pointing at
this verdict, not an edit of their content.

### 4.2b `notation.md` (the OTHER L4 single source — absent from r1 entirely)

Rows to add and update are given verbatim in §5.4.  Affected existing rows:
line 244 (`𝖲(k_s;{q_i,v_i})` "on the D24(d) class `𝒮_W`" → `𝒮_W(ρ)`), line
258 (`𝒮_W` row itself), overload rule 9 (untouched — `Z_ρ` avoids bare
`Z`), overload rule 2 / n4 (`χ` as sign: D24(c)/(d) and ML5 shards use the
*argumented* `χ(h,k)` registered at `notation.md:261`; the pre-existing
tension between rule 2's "do not import `χ` as a sign" and D24's usage is
recorded in §5.4 as a one-sentence amendment proposal, not resolved here).

### 4.3 Text that does NOT change

r1's §4.3 list was verified item-by-item by the r1 critic (V12) and is
retained verbatim by reference: `oracle-bethe.md` O7/O8/O9,
`soft-current-recon.md` (R14)/(R17)/(R18), `paper/main.tex:208, 244–252`
(the five-condition count survives the split — r1-critic V13; also
`main.tex:542–546`, checked by the critic at n2), D24(a),(b),(d)1,2,4,5,
(e), D25, `ml4_check.py`, `spin_s_slope_check.py`, the results JSONs, and
the CLAIMS rows ML5, S2-2body, S2-2body-S, M-IDX-density, Bc, S-general.
Additionally unchanged **because of the retirement** (r1 would have changed
them): nothing in `definitions.md` now displays `−iχ/(2ρ v_h)`, so no
future corpus statement can contradict the three provenance sites of §1.2.

### 4.4 Is `𝒮_W(ρ)` nonempty after the repair?

**No — nonemptiness remains OPEN, at every `ρ` including `ρ = 1/2`** (r1
§4.4, concurred with by the r1 critic §8; retained verbatim in substance):

* *Before*: given the bridge, provably empty off `ρ = 1/2` (V7).
* *After*: the proof of emptiness is gone — with `𝔞_leg` open, the class
  predicts jet `2χ𝔞_leg` and no PROVED row refutes membership — but no
  source satisfying clauses 1, 4, 5 has been exhibited at any density.
* **Coupling (r1-critic §8, adopted):** `tns-axg` and `tns-iu5` are
  coupled.  `D24-VAL` cannot move past CONJECTURE until either `tns-axg`
  produces a member (making the matching non-vacuous) or AMP is proved
  (making the value derived).  Accordingly `tns-iu5` should be **re-scoped
  on merge, not closed**: "clause 3 split; kinematic value kept; density
  in OPEN lemma AMP; matched value carried as conditional row D24-VAL".

### 4.5 Compliance with the binding soft-index adjudication (M5)

r1 silently reversed two binding decisions; this round acknowledges both
and complies with both:

* **§3.2 (value-fixing by hypothesis is DEAD; value from on-shell input,
  conditional on a named, displayed matching hypothesis).**  Complied with,
  strictly: the value is taken from on-shell input (`S2-2body-S`) *and*
  the matching hypothesis (the bridge, plus membership) is named and
  displayed as the two conditions of `D24-VAL` — which is moreover kept
  out of the definition entirely.  No layer of this artifact says
  "derived".
* **§3.5 (the fully polarised register `M = ρN − n` was struck for
  presupposing `ρ = S ∈ ½ℤ`).**  Complied with: the merged D24(d) contains
  no fully-polarised-vacuum object — `Z_ρ := 2ρ` is defined from the
  `notation.md` `ρ`-row (a GNS/state datum, `ω_α(S^z)`), with the su(2)
  fully-polarised reading `Z_ρ = ω_α([S^+_x, S^-_x])` marked as a special
  case, not a membership condition.  The fully polarised register `H_S`
  appears only where it is legitimate (r1-critic M5(d)): as the one
  register the corpus can compute in, inside the *conditional* claim
  `D24-VAL`, scoped to `ρ = S ∈ {1/2,1,3/2,2}` with extension to other `ρ`
  labelled a hypothesis (AMP).

---

## 5. MERGE PROPOSALS

*The orchestrator applies these, only after a critic clears this round.
This lane did not edit any shared file.  Anchors re-verified this round:
`definitions.md:931` begins `**(c) The contact first jet.**`;
`definitions.md:952` begins `**(d) The Ward-covariant no-contact class`;
the (c) span ends at line 950 `factorisation with the same stated norm
control.` and the (d) span ends at line 973 `is part of the ML5-B future
work.`  Apply 5.1 and 5.2 in the SAME commit (B2 references (d)3b), with
5.3–5.4 and the §4.2 lockstep/erratum edits.*

### 5.1 `definitions.md` — D24(c), lines 931–950

**REPLACE** (from `**(c) The contact first jet.**` through
`factorisation with the same stated norm control.`):

```
**(c) The contact first jet.**  With `χ(h,k) := sgn(v(h) − v(k))` and
`𝔞_leg` the soft-leg amputation constant of (d)3b below (the forward
reference is deliberate: `𝔠_h` is by definition the obstruction to the
factorisation (d) predicts; in the register in which this clause was frozen
and is tested — D6, `ρ = 1/2` — `𝔞_leg = 1`),

  `𝔠_h(O) := ∂_k M_2^O(k,h)|_{k=0} − 2i\,𝔞_leg\,χ(h,0)\,M_1^O(h)`.

**Criterion (ML5-A; status in the claims DAG).**  On a linear source class
with `M_1^O ∈ L²(I)` and `M_2^O(k,·)` `C²` at `k=0` as an `L²(I)`-valued map,
the factorisation
`M_2^O(k,h) = 2i𝔞_leg χ k M_1^O(h) + O_{L²(I)}(k²)` holds **if and only if
both**

  `M_2^O(0,·) = 0`  and  `𝔠_h(O) = 0`

in `L²(I)`.  With
`K_O(ε) := (1/2)sup_{|q|≤ε}‖∂_q²M_2^O(q,·)‖_{L²(I)}`, Taylor's theorem gives
the exact control
`‖M_2^O(k,·) − 2i𝔞_leg χ kM_1^O‖_{L²(I)} ≤ K_O(ε)|k|²`.
The stronger relative bound used in D24(b) requires the additional uniform
hypothesis `K_O(ε) ≤ C_I‖M_1^O‖_{L²(I)}`; it does not follow from `C²`
regularity alone.  On an affine class both displayed zero conditions must
hold on every source difference, and the base source must obey the full
factorisation with the same stated norm control.
**The criterion is constant-agnostic** — its proof (`ml5-universality.md`
⟨1⟩2) evaluates at `k = 0` and differentiates once, and never uses the
value of `𝔞_leg` (`𝔞_leg ≠ 0` suffices).  At `𝔞_leg = 1` this is the
frozen form, the form in which D24(e) and `theory/checks/ml4_check.py`
test it (bd `tns-iu5`).
```

### 5.2 `definitions.md` — D24(d), lines 952–973

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
polarised spin-`S` ferromagnet `ρ = S`.  `𝒮_W(ρ)` is the class of sources
satisfying all five of (clause 3 has two parts; the *count* of conditions
is deliberately unchanged, so `paper/main.tex:244` "five-condition" and the
audit rows that quote it stay correct):
1. *Exhaustive normed LSZ decomposition* — in `L²(I)`, `M_2^O` is exactly
   the sum of the descendant external-leg term `E^O_desc`, the
   orthogonal-current term, and the direct source/contact term named below;
   there is no additional reduced term, and the equality holds in the same
   packet norm as D24(b).
2. *Ward covariance* — the descendant current residue factorises as
   `2i v_h M_1^O(h)`.  (This clause is correct at every density: on the
   fully polarised spin-`S` tail the residue is exactly `Z_ρ`-linear,
   `⟨h|Q_0^†J^-_0|h⟩ = 2i v_S(h)` with `v_S(h) = Z_ρ J\sin h`; frozen
   `soft-current-recon.md` (R14) is its `Z_ρ = 1` reading — named
   computation D24N-C3 in `theory/checks/d24d3_normalization_check.py`.)
3. *Kinematic LSZ normalisation*, in two parts:
   **(3a) hypothesis** — the external flux factor
   `L(k,h) := E^O_desc(k,h)/[(e^{ik}−1)\,2i v_h\,M_1^O(h)]` is well
   defined by clauses 1--2 for `k ≠ 0` at every `h` with `M_1^O(h) ≠ 0`;
   the hypothesis is that it extends to a process-independent, uniformly
   `C¹` function on `{|k| ≤ ε} × I`, and `L(0,h)` denotes that extension's
   value at `k = 0`.
   **(3b) normalisation split — the kinematic value, and the OPEN
   amputation constant** — `L(0,h) = 𝔞_leg·(−iχ(h,0)/v_h)`, with `𝔞_leg`
   a nonzero constant independent of `k`, `h`, and `O`.  The factor
   `−iχ/v_h` is the reciprocal LSZ energy denominator
   `[ω(h+k)−ω(h)]^{-1}k` — the corpus's fixed provenance for `L`
   (`soft-current-recon.md` ⟨1⟩7, `paper/main.tex:524--527`,
   `soft-index-b.md:808`) — and is the whole of the value this clause
   asserts.  **The soft-leg amputation constant `𝔞_leg` is NOT fixed by
   this definition.**  The lemma that would fix it — "charge-created
   soft-leg amputation contributes the per-site leg density `Z_ρ = 2ρ` to
   the external flux", i.e. `𝔞_leg = 1/(2ρ)` (**AMP**,
   `theory/verdicts/soft-index-r1.md` F1(c)(i)) — is OPEN.  As frozen,
   this clause stipulated `𝔞_leg = 1`, which under the corpus's
   jet-identification bridge contradicts PROVED `S2-2body-S` at every
   `ρ ≠ 1/2` (bd `tns-iu5`).  Conditional on that bridge, on-shell
   matching forces `𝔞_leg = 1/(2ρ)` at `ρ = S ∈ {1/2, 1, 3/2, 2}` in the
   fully polarised spin-`S` register for any member of `𝒮_W(S)` there —
   carried as the conditional claim row `D24-VAL` in `claims/CLAIMS.md`
   (CONJECTURE), not as part of this definition.  At `ρ = 1/2` both
   readings give `𝔞_leg = 1` and the frozen clause is recovered verbatim
   (adjudicated in `theory/verdicts/d24d3-adjudication-r2.md`; certificate
   `theory/checks/d24d3_normalization_check.py`);
4. *Reduced-channel regularity* — the orthogonal current channel is
   `O_{L²(I)}(k²)` in the stated target limit, with the relative norm
   bound of D24(b).  Fixed-volume ML4 does not by itself supply a
   volume-uniform bound;
5. **No direct soft contact** — the amputated source commutator/contact
   term is bounded by `C_I|k|²‖M_1^O‖_{L²(I)}`.

Hypotheses 1 and 5 are the extra LSZ/contact content beyond the fixed-volume
Ward reduction, and by (c) the zero-intercept and zero-first-jet conditions
are necessary, not cosmetic.  Symmetry-generated external-leg insertions are
the intended seed, but **no nontrivial microscopic class has been proved to
satisfy all five conditions**; nonemptiness in the target scattering
register is part of the ML5-B future work.  The `tns-iu5` adjudication of
clause 3 removed a *proof* that `𝒮_W(ρ)` is empty for `ρ ≠ 1/2` — as
frozen, clause 3 forced soft slope `2` at every density, contradicting
PROVED `S2-2body-S` given the jet-identification bridge — but it supplies
no member and fixes no value of `𝔞_leg`, so nonemptiness stays open at
every `ρ` (bd `tns-axg`), and the matched value stays conditional
(`D24-VAL`).
```

### 5.3 `claims/CLAIMS.md`

**5.3a — REPLACE the ML5-B row (line 41) with:**

```
| ML5-B | Conditional implication on the five-condition D24(d) class `𝒮_W(ρ)`, including the exhaustive normed LSZ decomposition.  The implication is proved; its displayed conclusion is `M_2^O(k,h) = 2i𝔞_leg χ k M_1^O(h) + O_{L²(I)}(k²)`, with `𝔞_leg` the D24(d)3b soft-leg amputation constant (value OPEN — lemma AMP; conditionally matched to `1/(2ρ)` by claim D24-VAL); at `ρ = 1/2` (`𝔞_leg = 1`) this is the frozen `2iχ k M_1^O` / `2χ` sites.  **Re-scoped 2026-08-29 (bd `tns-iu5` r2):** the frozen D24(d)3 stipulated `𝔞_leg = 1`, forcing soft slope `2` at EVERY tail density and contradicting PROVED `S2-2body-S` (`1/S`) given the jet-identification bridge — frozen `𝒮_W` provably empty for `ρ ≠ 1/2`.  Clause 3 is now split: 3a keeps the process-independence/`C¹`-extension hypothesis with `L` DEFINED as the descendant quotient (`k ≠ 0`); 3b keeps the kinematic value `−iχ/v_h` (the reciprocal LSZ energy denominator — the corpus's fixed provenance for `L`) and carries the density in the OPEN amputation constant `𝔞_leg`.  The matched value `𝔞_leg = 1/(2ρ)` is RETIRED from the definition and carried as conditional row D24-VAL.  The proof of the implication is unchanged apart from carrying `𝔞_leg` (⟨2⟩1.⟨3⟩2 needs only `𝔞_leg ≠ 0` and `v_h` bounded below on `I`).  Nonemptiness and microscopic membership remain CONJECTURE/future work bd `tns-axg`, at every `ρ`. | PROVED | ML4-A, ML5-A, D24(d) | theory/ml5-universality.md ⟨1⟩3; PROVED per corpus-r2.md adjudication (conditional implication); clause-3 repair adjudicated in theory/verdicts/d24d3-adjudication-r2.md (bd tns-iu5 r2) | theory/checks/ml4_check.py local obstructions only; theory/checks/d24d3_normalization_check.py (D24N-C1–C7; green exit 0; `--red-frozen`/`--red-power`/`--red-halfpower` die at D24N-C6, `--red-ward` at D24N-C3) |
```

*(Note: `S2-2body-S` is deliberately NOT added to ML5-B's depends-on — with
the value retired, ML5-B's conclusion no longer references it; the
dependency belongs to `D24-VAL`.)*

**5.3b — ADD a new row `D24-VAL` (immediately after the ML5-B row):**

```
| D24-VAL | Conditional matched value of the D24(d)3b amputation constant.  GIVEN (α) the jet-identification bridge — the D24(d) soft multiplier's jet equals the two-body physical phase jet (corpus identification via soft-current-recon.md (R17) and oracle-bethe.md O9; NOT a PROVED row) — and (β) existence of a member `O ∈ 𝒮_W(S)` with `M_1^O ≠ 0` in the fully polarised spin-`S` register: THEN `𝔞_leg = 1/(2S) = 1/(2ρ)`, i.e. `L(0,h) = −iχ/(2ρ v_h)` and ML5-B jet `χ/ρ`, at `ρ = S ∈ {1/2, 1, 3/2, 2}`.  Within the family `𝔞_leg = (2ρ)^{-p}` the exact law `(2S)^p = 2S` forces `p = 1` at any single `2S ≠ 1` (the `S = 1/2` point is degenerate; the four densities are one analytic curve, not four independent measurements).  Extension to other `ρ` is hypothesis (open lemma AMP: soft-leg amputation contributes `1/Z_ρ`; theory/verdicts/soft-index-r1.md F1(c)(i)).  The implication's arithmetic is machine-checked (D24N-C6); the row is CONJECTURE because (α) is unproved and (β) is open at every `ρ` — coupled to bd `tns-axg` and to AMP, and cannot be upgraded until one of them closes. | CONJECTURE | D24(d), S2-2body-S, ML5-B | theory/verdicts/d24d3-adjudication-r2.md §2 ⟨1⟩3 | theory/checks/d24d3_normalization_check.py D24N-C4–C6 (green exit 0; `--red-frozen`/`--red-power`/`--red-halfpower` die at D24N-C6) |
```

**5.3c — REPLACE the ML5-A row (line 40) with:**

```
| ML5-A | Repaired iff: `M_2^O(0)=0` and `𝔠_h(O)=0`, with source-wise remainder controlled by `K_O` and the relative bound separately assumed.  The criterion is constant-agnostic: its proof evaluates at `k=0` and differentiates once and never uses the value; since bd `tns-iu5` (r2) it is stated with D24(c)'s constant `2i𝔞_leg χ`, which at `𝔞_leg = 1` (`ρ = 1/2`, D6) is the frozen form in which D24(e) and ml4_check.py test it. | PROVED | D24(c) | theory/ml5-universality.md ⟨1⟩2; PROVED per corpus-r2.md adjudication | theory/checks/ml4_check.py ML5-I1 |
```

### 5.4 `notation.md` (the L4 symbol registry — F2 narrow, F3(c), M6, m1, n4)

**5.4a — ADD to the ML4/ML5/M-quant symbol table (after the `𝒮_W` row):**

```
| `L(k,h)`, `L(0,h)` | D24(d)3a external flux factor: the descendant quotient `E^O_desc/[(e^{ik}−1)·2iv_h·M_1^O(h)]`, defined for `k ≠ 0` where `M_1^O(h) ≠ 0`; `L(0,h)` is the value at `k=0` of the hypothesised `C¹` extension.  Kinematic provenance: the reciprocal LSZ energy denominator (`soft-current-recon.md` ⟨1⟩7; `paper/main.tex:524–527`; `soft-index-b.md:808`); `L(0,h) = 𝔞_leg·(−iχ(h,0)/v_h)` | definitions.md D24(d)3 |
| `Z_ρ` | order-parameter density `2ρ`; for an su(2) model with a fully polarised α tail, `Z_ρ = ω_α([S^+_x, S^-_x])`.  Subscripted deliberately: bare `Z` stays Pauli-reserved (overload rule 9, unchanged) | definitions.md D24(d) |
| `𝔞_leg` | soft-leg amputation constant of D24(d)3b, `𝔞_leg := i v_h L(0,h)/χ(h,0)`; value OPEN (lemma AMP: `𝔞_leg = 1/Z_ρ`, soft-index-r1.md F1(c)(i)); conditionally matched `= 1/(2ρ)` by claim D24-VAL; `= 1` as frozen (`ρ = 1/2`).  Subscripted deliberately: bare `𝔞` is the twisted group algebra `𝔞_α` of the SPT corner | definitions.md D24(d)3b |
| `E^O_desc` | descendant external-leg term of the D24(d)1 decomposition (fraktur `𝔈` avoided: `𝔈_W`, `𝔈_{A_α}`, `𝔈_{A_β}` are the window CP maps) | definitions.md D24(d)1 |
```

**5.4b — REPLACE the `𝒮_W` row (line 258) with:**

```
| `𝒮_W(ρ)` | the ρ-indexed five-condition Ward/LSZ/no-contact source class in the repaired conditional ML5-B implication; `ρ := ω_α(S^z) > 0` | definitions.md D24(d) |
```

**5.4c — In the `𝖲(k_s;{q_i,v_i})` row (line 244), replace** "on the
D24(d) class `𝒮_W`" **with** "on the D24(d) class `𝒮_W(ρ)`".

**5.4d — (n4, pre-existing tension, minimal amendment) APPEND to overload
rule 2:**

```
   Recorded exception (2026-08-29, bd `tns-iu5` r2): D24(c)/(d) and the ML5
   shards use the *argumented* channel sign `χ(h,k)` (registered below) and
   abbreviate it `χ` inside their own displays; the bare-`χ` =
   bond-dimension rule is unchanged everywhere else.
```

### 5.5 ADVISORY (same-commit obligations; orchestrator's call on mechanics)

1. Apply §4.2's `ml5-universality.md` edits (constant `2i𝔞_leg χ`, line-158
   Wigner sentence, header ERRATUM pointer) in the SAME commit as 5.1–5.4,
   or add the ERRATUM block alternative — do not ship 5.1–5.4 alone.
2. Add ERRATUM pointers (not edits) at the heads of `theory/soft-index.md`
   and `theory/soft-index-b.md` for their displayed flux/leg-density values
   (`soft-index.md:161–162`; `soft-index-b.md:757–758, 808`), pointing at
   this verdict (n3).
3. bd `tns-v44` (unified S1 r2) instruction, correcting r1 §8: the r2 shard
   must carry the factor as the displayed OPEN constant `𝔞_leg` citing
   D24(d)3b, with the matched value cited as `D24-VAL` (CONJECTURE) — not
   "cite D24(d)3b for `1/(2ρ)`", which is no longer what the definition
   says.  This is also what binding `soft-index-adjudication-r1.md` §3.3
   ordered ("the r2 prover states the factor as an explicit displayed
   hypothesis pending tns-iu5").
4. `HANDOFF.md` corpus-damage line "(3) Frozen `𝒮_W` empty for `ρ≠1/2`"
   becomes "repaired by retirement: clause 3 split, `𝔞_leg` OPEN (AMP),
   matched value conditional (D24-VAL); `𝒮_W(ρ)` nonemptiness open at
   every `ρ`".

---

## 6. HONEST STATUS

The r1 critic passed H1–H7 "on their own" and faulted the artifact for not
being in lockstep with them (§6 of the verdict: the two layers that leave
the file — the definitions.md text and the DAG row — were the two that
overstated).  This round's outward-facing layers (§5.2 clause 3b, the
`D24-VAL` row) now claim *less* than the honest section, not more: the
definition asserts no value at all.

**H1 — PROVED (fenced; r1-critic V1–V6).**  `Z_ρ = 2ρ = 2S`;
`‖Q^-_k|Ω⟩‖² = Z_ρ N` for all `k`; `v_S(h) = Z_ρ J sin h`;
`⟨h|Q_0^†J^-_0|h⟩ = 2i v_S(h)` exactly at `2S = 1,2,3,4`; the frozen
`𝔞_leg = 1` makes ML5-B's jet identically `2χ`; the exact spin-`S` phase
slope is `1/S`.

**H2 — MATCHED, CONDITIONAL, and RETIRED from the definition.**
`𝔞_leg = 1/(2ρ)`, equivalently `L(0,h) = −iχ/(2ρ v_h)`, is fixed by
on-shell matching against PROVED `S2-2body-S` — *conditional on* the
jet-identification bridge (unproved, H5) *and* on membership (open, §4.4).
It is not derived, it is not stipulated into the L4 file, and it is not a
fitted constant in the r1 sense: within the family `(2ρ)^{-p}` the exponent
is pinned symbolically at any single `2S ≠ 1` (⟨1⟩3.⟨3⟩3), with the data
resolving `p ∈ [0.989, 1.017]` at the `0.02` acceptance band (§7).  Its
DAG home is `D24-VAL` (CONJECTURE).

**H3 — OPEN LEMMA, not structural identification.**  The mechanism — why
the amputation contributes `1/Z_ρ` — is the open lemma AMP.  r1's
Holstein–Primakoff two-insertion count is deleted (it produced `Z^{-1/2}`
on its own terms, r1-critic M2); what is known about the mechanism is
negative: it is *not* a leg normalisation (a `√Z_ρ` argument gives the
wrong power — ⟨1⟩4.⟨2⟩3).  Watanabe–Murayama fixes the natural invariant
(`Z_ρ` as the type-B symplectic density), not the factor 2 (⟨1⟩4.⟨2⟩4).

**H4 — REFUTED.**  (i) The frozen clause 3 as a universal value claim,
given the bridge (V4/V5/V7).  (ii) The S1-A critic's proposed mechanism
(bare unit-normalisation of the soft leg): gives `Z_ρ^{-1/2}` (D24N-C7 and
⟨1⟩4.⟨2⟩2).  NOT refuted, correcting r1 H4(ii): either S1 lane's
arithmetic, or lane B's per-volume-density bookkeeping — which is the
bookkeeping adopted here.  (iii) r1's own §1.5 root-cause premise ("`L` is
never defined anywhere") — withdrawn at §1.2.

**H5 — CONDITIONAL, and the one place a critic should push (retained from
r1 verbatim in substance).**  The bridge — the D24(d) soft multiplier's jet
equals the two-body physical phase jet — is the corpus's working
identification ((R17), O9), not a PROVED row.  Both horns of r1 §1.4 still
condemn the frozen clause; the third horn (bridge holds AND class empty) is
now *accommodated* rather than missed: under it, `D24-VAL` is vacuous and
the definition — which asserts no value — is untouched.  Citation note
(r1-critic m6): the bridge evidence is (R17) and O9 only;
`ml5-universality.md` ⟨1⟩4.⟨3⟩4's `s'(0,h) = 2i` is the `O_η` bra
coefficient, not ML5-B's constant, and is not cited here as bridge
evidence.

**H6 — EVIDENCE, not proof (retained).**  The acceptance table is
numerical (ansatz-free ED, extrapolated); the exactness claims of H1 are
machine-precision identities at finite `N`, not `N → ∞` theorems; the
`S2-2body-S` input is exact and PROVED; the extrapolation carries the
residual error.

**H7 — NOT claimed (retained and extended).**  Nothing here promotes
`S-general`, `Bc`, `M-quant`, `S-INDEX`, or AMP; nothing supplies a member
of `𝒮_W(ρ)`; nothing touches `tns-ebh` or `tns-uxr`.  Additionally NOT
claimed this round: any value of `𝔞_leg` in `definitions.md`; any
statement at non-half-integer `ρ` (extension is hypothesis, M4); any
mechanism for AMP.

---

## 7. Certificate

`theory/checks/d24d3_normalization_check.py`, 459 loc, rebuilt per
r1-critic M3; no bare `assert`, every failure `SystemExit(1)` with the
gate name as the first token of the message, so the **exit path** is
always identified.

Green (`python3 -O`, exit **0**):

```
D24N-C1 frozen_jet_coefficient=2*chi matched=chi/rho
D24N-C2 Z_rho=2rho and constructed soft-leg norm, max_error=8.882e-16
D24N-C3 Ward residue = Z_rho*2iJ sin h, max_error=4.814e-15
D24N-C4 ansatz-free slopes vs 1/S: max_rel_dev=0.0043 (pre-registered band 0.08)
D24N-C5 frozen-clause relative deviations at S=1/2,1,3/2,2: 0.000, 1.002, 2.003, 3.003  -> defect size 3.003
D24N-C6 candidate max_rel_dev=0.0033 (acceptance band 0.02, independent of C4); fitted exponent=1.0024 over 2S!=1 spins; symbolic (2S)^p=2S root p=1 at S=1,3/2,2 (S=1/2 degenerate); resolving interval p in [0.989, 1.017]
D24N-C7 half-power route gap=1.855e-01
PASS: D24-VAL candidate a_leg = 1/(2 rho) matches; frozen a_leg = 1 refuted; the D24(d)3b definition itself fixes no value (lemma AMP open)
```

### 7.1 Red modes — exit PATH, not just exit code

| mode | exit | died at (gate named in first stderr token) |
|---|---|---|
| `--red-frozen` (`𝔞_leg = 1`) | 1 | **D24N-C6** `candidate flux misses the acceptance band (0.02) at S=1.0 dev=1.0016; S=1.5 dev=2.0027; S=2.0 dev=3.0033` — fails at `S = 1` first, as the r1 work order demanded |
| `--red-power` (`(2ρ)^{-2}`) | 1 | **D24N-C6** `at S=1.0 dev=0.4984; S=1.5 dev=0.6640; S=2.0 dev=0.7467` |
| `--red-halfpower` (`(2ρ)^{-1/2}`) | 1 | **D24N-C6** `at S=1.0 dev=0.4158; S=1.5 dev=0.7347; S=2.0 dev=1.0033` |
| `--red-ward` (residue `∼ Z_ρ²`) | 1 | **D24N-C3** `Ward residue Z-scaling error 1.697e+01` |

All three hypothesis mutants now die at the **acceptance gate**, which they
reach (C1–C5 do not depend on the candidate).  r1's pathology — every
reported mutant dying at the ground-truth gate C4, with the acceptance test
never exercised — is resolved by construction.

### 7.2 Data mutants (copies in the scratchpad; the DATA falsified, not the code)

| mutant (copy of `spin1-bc-falsifier.json`) | exit | died at |
|---|---|---|
| `m1_slope` — `S=1` summary slopes forced to `2.0` | 1 | **D24N-C4** `slope deviates from 1/S by 1.0000` |
| `m2_shift799` — every summary slope `× (1−0.0799)` | 1 | **D24N-C4** `0.0839` (rows already sit ≈0.4% below `1/S`, so the critic's −7.99% shift lands just outside C4 here) |
| `m2b_shift60` — every summary slope `× (1−0.060)` | 1 | **D24N-C6** `at S=0.5 dev=0.0604; S=1.0 dev=0.0615; S=1.5 dev=0.0625; S=2.0 dev=0.0631` — **passes C4 (max row dev 0.064 < 0.08) and dies at the acceptance gate**: D24N-C6 is demonstrably NOT subsumed by D24N-C4 |
| `m3_bandmoved` — `decision_band` `0.08 → 0.5` | 1 | **D24N-C4** `decision band moved: 0.5` |
| `m4_noband` — `decision_band` key deleted | 1 | **D24N-C4** `decision_band key missing` (r1's silent-pass hole closed: the key is now required) |
| `m5_absent` — data file missing | 1 | **D24N-C4** `missing ground-truth file` |

### 7.3 Code mutants and absurd-input probes (copies in the scratchpad)

| mutant / probe | result |
|---|---|
| `c1_nosqrt` — ladder element `sqrt((n+1)(2S−n)) → (n+1)(2S−n)` | exit 1 at **D24N-C2** `error 1.200e+01` — the rebuilt soft-leg-norm gate actually exercises the construction (r1's gate was `sites·two_s/sites − two_s ≡ 0` and could not see this) |
| `c2_wronglaw` — symbolic law `(2S)^p = 2S → (2S)^p = 4S` | exit 1 at **D24N-C6** `symbolic exact law … at S=1 gives roots [2], not [1]` — the symbolic gate replaces r1's `lstsq(x,x)` tautology and can fail |
| absurd input `two_s = −5.0` into the C2 construction | constructed norm `0.0 ≠ −5.0` — the gate would fail; r1's no-op returned `0` error for the same input |
| absurd input `two_s = 3.7` into the C2 construction | constructed norm `= 3.7` — this is the genuine matrix element `⟨Ω|S^+S^-|Ω⟩ = 2S` of the formal highest-weight module, not a tautology: the `c1_nosqrt` mutation moves it (row above), which r1's gate could not |

### 7.4 Gate subsumption audit (standing obligation, applied to MYSELF)

* **D24N-C5 is deductively subsumed by D24N-C4** for the true data: if
  every row is within `0.08` of `1/S`, the frozen prediction's deviation is
  `≥ |2S−1| − 0.08 > 0.08` at `S ≥ 1` and `< 0.08` at `S = 1/2` —
  automatically.  C5 is therefore **display, not evidence**: it prints the
  defect sizes for the record.  What would add independent evidence for
  the defect: nothing at this data — the defect IS a corollary of C4 plus
  arithmetic, and is honestly so labelled.
* **The C6 exponent FIT is implied by the C6 acceptance gate** (devs
  `≤ 0.02` force `|p̂ − 1| ≤ 0.018 < 0.03`): also display.  The evidential
  gates of C6 are the acceptance comparison (independent of C4 —
  `m2b_shift60`) and the symbolic solve (independent of the data —
  `c2_wronglaw`).
* **Resolving power, stated:** the acceptance band pins
  `p ∈ [0.989, 1.017]` (printed every run).  The certificate pins the
  exponent to `±1.7%` from data; exactness of `p = 1` comes from the
  symbolic law, and is conditional exactly as `D24-VAL` is.
* No other gate pair is in an implication relation: C1 (symbolic), C2/C3
  (constructions), C4 (data vs law), C6 (candidate vs data + law), C7
  (route gap) have pairwise-independent failure modes, witnessed by the
  mutant table: six distinct mutants die at four distinct gates.

---

## 8. Disposition

* **Merge**: §5.1 + §5.2 + §5.3 + §5.4 in one commit, together with §4.2's
  `ml5-universality.md` lockstep edits (or its ERRATUM alternative) and
  §5.5's soft-index ERRATUM pointers.  Nothing merges before a critic
  clears this round.
* bd `tns-iu5`: **re-scope, do not close** (r1-critic §8, adopted):
  "clause 3 split; kinematic value kept; density in OPEN lemma AMP;
  matched value carried as conditional row D24-VAL; coupled to `tns-axg`
  and to AMP."
* bd `tns-axg`: stays open, unchanged; now explicitly coupled to the
  upgrade path of `D24-VAL`.
* bd `tns-v44`: unblocked on this axis, with the corrected instruction of
  §5.5 item 3 (display `𝔞_leg` as the open constant; cite `D24-VAL` for
  the matched value; this is what binding §3.3 ordered).
* The open lemma AMP is the natural next prover target if the orchestrator
  wants the value upgraded: an LSZ amputation computation for the
  charge-created soft leg, in the `m_λ` register per binding §3.5, with
  the negative result of ⟨1⟩4.⟨2⟩3 (not a leg normalisation) as its
  fence.
