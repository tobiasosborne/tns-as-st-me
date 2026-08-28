<!-- ROLE: ADVERSARIAL CRITIC verdict on theory/verdicts/d24d3-adjudication-r1.md
     and theory/checks/d24d3_normalization_check.py (bd tns-iu5, r1).
     Brief: briefs/d24d3-critic-r1.md; protocol: briefs/critic-protocol.md.
     Writable file of this lane: THIS FILE ONLY.  definitions.md,
     claims/CLAIMS.md, notation.md, the target verdict and its checker were
     read and executed, never edited.  No git commit. -->

# r1 critic verdict — D24(d)3 ρ-normalisation adjudication

**Headline.  The repair DIRECTION is right and the VALUE is right — I
re-derived both independently.  The repair's *status label* is wrong, its
*root-cause premise* is wrong, and the §5 merge text is not verbatim-
appliable to an L4 file.  `L(0,h) = −iχ/(2ρ v_h)` is not derived; it is
fixed by on-shell matching inside a class the same document declares
possibly empty, using a quotient that is `0/0` at exactly the point whose
value is asserted.  Merging §5.2's clause 3b as "derived and not
stipulated" would install into `definitions.md` a statement stronger than
anything in this corpus supports, and one that contradicts three corpus
statements of what `L` is.**

**Final line at the bottom.**

---

## 0. What I did (independent, nothing taken on the target's word)

All computations below are mine, written from scratch; none imports the
target's checker or either S1 shard.

* **(K-a)** Full-Hilbert-space sparse construction of the spin-`S` ring
  (`scipy.sparse` kron of first-principles ladder matrices, `N = 6`,
  `2S = 1,2,3,4`): `Z`, the soft-leg norm, `ω_S`, and the Ward residue
  `⟨h|Q_0^†J^-_0|h⟩` with `Q_0 = Σ_x S^-_x`,
  `J^-_0 = Σ_x −[h_{x,x+1},S^-_x]`, `h = −J(S_x·S_{x+1} − S²)`.  This is a
  *different construction* from the target's configuration-dictionary code.
* **(K-b)** Symbolic differentiation of `S2-2body-S` (T.2) —
  `∂_{k_s}\log S_{12}|_0 = i/S`, **exactly**, in `sympy`.
* **(K-c)** Ansatz-free two-magnon ED of my own: occupation basis
  (`N(N−1)/2` singles + `N` doubles), Bloch momentum blocks, `N = 60`,
  `2S = 1,2,3,4`; levels inverted through `E = ω_S(k_1)+ω_S(k_2)` and
  `δ_ED = Nk_1 − 2πI_1`.
* **(K-d)** Exhaustive grep for a definition of `L`, over the WHOLE repo
  including `notation.md`, `claims/`, `briefs/` and `paper/` (the target's
  grep covered `theory/`, `definitions.md`, `paper/` only, and only the
  literal strings `L(k,h)`/`L(0,h)`).
* **(K-e)** Checker: green + four reds under `python3 -O`; then seven
  mutants on copies in the scratchpad, plus two structural no-op probes and
  an exponent-resolution scan.
* **(K-f)** L3: `refs/arxiv-1203.0609/revision3.tex` read at the cited
  equations, title verified.

---

## 1. VERIFIED CORRECT — fence this, do not churn it

Everything in this section I reproduced independently; the repair lane must
not spend a round re-establishing it.

**V1.  `Z = 2ρ = 2S`, and the soft-leg norm.**  `[S^+,S^-] = 2S^z`;
`⟨Ω|[S^+_x,S^-_x]|Ω⟩ = 2S` at `2S = 1,2,3,4` (my (K-a), error `≤ 4·10^{-16}`);
and — computed properly, by actually applying `Σ_x e^{ikx}S^-_x` to the
vacuum, which the target's checker does **not** do (see M3) —
`‖Q^-_k|Ω⟩‖²/N = 2S` exactly, `k`-independent.  ⟨1⟩2 is TRUE.

**V2.  Dispersion and velocity.**  `ω_S(k) = 2JS(1−\cos k)` reproduced by ED
at `2S = 1..4` to `10^{-15}`; hence `v_S(h) = 2JS\sin h = ZJ\sin h`.

**V3.  The Ward residue.**  `⟨h|Q_0^†J^-_0|h⟩ = 2i\,v_S(h)` **exactly**, at
`2S = 1,2,3,4` and two hard momenta, by my independent construction (K-a).
D24(d) clause 2 is therefore CORRECT at every `Z`, not only at `Z = 1`.
(D24N-C3 is a real computation and I confirm its number.)

**V4.  The frozen clause is exactly density-blind.**  `(e^{ik}−1)(−iχ/v_h)
(2iv_h) = 2iχk + O(k²)`, with `∂_ρ = ∂_{v_h} = 0` identically.  D24N-C1 is
correct.  **The defect is real.**

**V5.  The exact slope is `1/S`.**  From `S2-2body-S` (T.2) I get
`∂_{k_s}\log S_{12}|_{k_s=0} = i/S` symbolically — not numerically, exactly
— for all `S`, and `|S_{12}| = 1` at `k_s = 0`.

**V6.  The frozen data is sound and my ED reproduces it.**  My independent
two-magnon ED at `2S=1`, `N=60`, `K = 2π·9/60` gives the level
`E = 0.33373055993019` against `numerics/results/spin1-bc-falsifier.json`
`A_ring_runs[0]`'s `0.33373055993` (Δ `1.9·10^{-13}`) and the same
`block_levels = 29`.  `δ_ED` matches the closed-form `arg S_{12}` to
`≤ 1·10^{-11}` at `2S = 1,2,3,4`.  The target's (A-d) claim is confirmed.

**V7.  The collision, and hence the emptiness *given the bridge*.**  Frozen
jet `2χ` at every `ρ` vs PROVED `S2-2body-S` jet `χ/S` ⇒ `S = 1/2`.  §1.3 is
correct as stated (subject to its own H5 bridge caveat, which I address in
O-F1(d) below).

**V8.  Defining `L` as the descendant quotient makes clause 3a NONVACUOUS.**
I checked the brief's worry directly: with `L := 𝔈^O/[(e^{ik}−1)2iv_hM_1^O]`,
"process independent" becomes the substantive requirement that the quotient
agree across all `O` in the class — a real constraint, not a tautology.  This
is a genuine improvement on the frozen text and should survive any repair.

**V9.  `v_h` is bounded away from zero on the hard window.**  On
`I = [a,b] ⋐ (0,π)`, `v_S(h) = 2JS\sin h ≥ 2JS\min(\sin a, \sin b) > 0`.
ML5-B ⟨2⟩1.⟨3⟩2 needs only that plus `Z > 0`, as §4.2 says.  (The other two
denominator factors are NOT bounded away from zero — see M7.)

**V10.  The L3 citation is accurate.**  `refs/arxiv-1203.0609/revision3.tex`
is Watanabe–Murayama, *Unified Description of Nambu–Goldstone Bosons without
Lorentz Invariance*; line 217 is `ρ_{ij} = −i⟨0|[Q_i,j^0_j]|0⟩`; line 338 is
"`m=\langle j^0_z\rangle` represents the magnetization of the ground state"
for `H=-J\sum s_i\cdot s_j` (line 319).  Quoted correctly.  (Its *force* is
overstated — see m6.)

**V11.  Checker green/red reproduce.**  `python3 -O` exit 0 with the printed
banner verbatim; `--red-frozen`, `--red-power`, `--red-halfpower` each exit 1
at D24N-C6, `--red-ward` exits 1 at D24N-C3.  `--red-frozen` does fail at
`S = 1` as the work order demanded.

**V12.  Every §4.3 "does not change" claim that I could check is TRUE.**
`theory/checks/ml4_check.py` lines 213/216/220 hardwire `2j*velocity` with
`velocity = J*sin(hard)`, i.e. the D6 `Z=1` reading (correct); its `O_η`
(l.299) and `V_int` (ll.310–332) obstructions never touch D24(c)'s constant
(`M_1^D = M_1^{V_int} = 0`), so D24(e) survives verbatim — I re-derived
`𝔠_h(ηD) = 2iη(1−e^{-3ih})` independence of the constant.  `oracle-bethe.md`
299/303/320/470 and `soft-current-recon.md` (R14)/(R17)/(R18) are D6
(`definitions.md:348`, `S_x = σ_x/2`) ⇒ `ρ = 1/2`, `Z = 1`, every displayed
`2` correct.  `paper/main.tex:208` likewise.  `spin_s_slope_check.py` exists
and is green (exit 0).

**V13.  Line anchors and the five-condition count.**  §5.1's REPLACE span is
exactly `definitions.md:931–950`; §5.2's is exactly `952–973`; `CLAIMS.md`
ML5-A is line 40 and ML5-B line 41.  The split keeps ONE numbered clause, so
`paper/main.tex:244` "five-condition" and `main.tex:542–546`'s prose list of
five conditions both stay correct.  The `𝖲 = 2ik_s` at `main.tex:249` is the
`ρ=1/2` member and survives.

**V14.  The VALUE.**  `2·(2ρ)^{-1} = 1/ρ`, `ρ = S`, matching `1/S` at
`S ∈ {1/2,1,3/2,2}` and `2` at `ρ=1/2`; and, within the family
`L_p = −iχ/((2ρ)^p v_h)`, the exact law `2(2S)^{-p} = 1/S` for two distinct
half-integer `S` forces `p = 1`.  The arithmetic is right and agrees with
`soft-index-r1.md`'s own surviving weaker statement
(`L(0,h) = −i\,sgn/(2ρ v_h)`).

---

## 2. FATAL

### F1.  `L(0,h)` is **not defined** by (D24N.3) at `k = 0`, and the matching that supplies its value quantifies over a class this document declares possibly empty.  "Derived and not stipulated" is false.

**(a) Location.**  `theory/verdicts/d24d3-adjudication-r1.md`
⟨1⟩1.⟨2⟩1 (l.180) and ⟨1⟩1.⟨2⟩1.⟨3⟩3 (ll.198–203); ⟨1⟩4.⟨2⟩1.⟨3⟩1
(ll.285–290); merge text §5.2 clause 3b (ll.544–553); HONEST STATUS H2
(ll.603–610).

**(b) My computation.**  Two independent failures, both at the same point.

*(i) The `0/0`.*  ⟨1⟩1.⟨2⟩1 defines
`L(k,h) := 𝔈^O(k,h)/[(e^{ik}−1)·2i v_h·M_1^O(h)]` and states — its own
words — that it "is well defined wherever `M_1^O ≠ 0` **and `k ≠ 0`**".
`e^{ik}−1 = 0` at `k = 0`.  So (D24N.3) defines `L` on `k ≠ 0` and assigns
*nothing* at `k = 0`.  Every value statement in the document —
(D24N.1), ⟨1⟩4.⟨2⟩1, §5.2 clause 3b, H2 — is about `L(0,h)`.  The step
⟨1⟩1.⟨2⟩1.⟨3⟩3 ("`L(0,h)` is an **output** of any model in the class, not a
free input") is therefore unsupported at the one argument it is invoked for.
`L(0,h)` exists only as `\lim_{k\to0}` of the quotient, and the existence of
that limit is *precisely* clause 3a's `C¹` hypothesis — i.e. the value is
an output **only after** assuming 3a, which is a hypothesis on membership,
not a model computation.  The chain "define, therefore compute, therefore
derive" breaks at its first link.

*(ii) The matching quantifies over a possibly empty class.*  ⟨1⟩4.⟨3⟩1 reads:
"By ⟨1⟩1 the value is an output.  Compute it in `H_S`: ML5-B (6) with the
quotient definition gives `𝖲 = (e^{ik}−1)L(0,h)2iv_h`, and `S2-2body-S`
(T.3) gives `𝖲 = i(χ/S)k`."  Nothing in this step computes `𝔈^O` in `H_S`.
It equates the **descendant term alone** to the **full physical two-body
jet**, which requires (α) a source `O ∈ 𝒮_W(ρ)` to exist in `H_S`, and
(β) clauses 1, 4, 5 to hold for it.  §4.4 of the same document states:
"no source has been exhibited satisfying clauses 1, 4 and 5 at any density"
and "nonemptiness stays open at every `ρ`".  So the "derivation" runs
`∀O∈𝒮_W(ρ): …` over a class whose inhabitation is open — and `briefs/
critic-protocol.md` §5 forbids exactly this ("no step may rely … on the
class `𝒮_W` being nonempty at `ρ≠1/2` while bd `tns-iu5` is open").

The two directions are **not** symmetric, and this is the crux.  §1.3's
emptiness argument uses the same premise legitimately, as a *reductio*
(assume a member, derive `S = 1/2`, conclude no member off `ρ=1/2`).
⟨1⟩4.⟨3⟩1 uses it *positively*, to fix a number.  If the class is empty the
reductio still refutes the frozen clause, but the "derivation" fixes
nothing — a universally quantified equation over the empty set determines no
constant.  The repair therefore chooses the one value that makes the §1.3
contradiction disappear.  That is a definitional choice made to dissolve a
refutation, which is a legitimate and honest thing to do — but it is
stipulation-with-a-reason, not derivation.

*(iii) It is a stipulation in kind, not merely in degree.*  Clause 3b sits
inside a **definition** of a class.  A clause of a definition cannot be
"derived": it is a membership condition.  The most that can be true is
"this is the only value consistent with PROVED `S2-2body-S` in the one
register the corpus can compute in".  §5.2 instead ships the words "derived
and not stipulated" into `definitions.md`.

**(c) FIX DEMAND.**  In §5.2 clause 3b replace "its value at zero, derived
and not stipulated" with "its value at zero, **fixed by on-shell matching**
(not derived from clauses 1–2)", add "`L(0,h) := \lim_{k\to0}` of the (3a)
quotient, whose existence is part of (3a)", and append the conditional
displayed in full: "conditional on (i) the identification of the D24(d)
multiplier's jet with the two-body physical phase jet, which is not a PROVED
row, and (ii) `𝒮_W(ρ)` being nonempty in `H_S`, which is open (bd
`tns-axg`)".

**(d) SURVIVING WEAKER STATEMENT.**  *Given clause 3a and the corpus's
jet-identification bridge, `L(0,h) = −iχ/(2ρ v_h)` is the unique value in the
family `−iχ/((2ρ)^p v_h)` compatible with PROVED `S2-2body-S` at
`ρ = S ∈ {1/2,1,3/2,2}`, and it reproduces the frozen clause at `ρ = 1/2`.
The frozen value `−iχ/v_h` is refuted as a universal statement.  Neither the
new value nor the old one is derived from D24(d)1–2.*

**(d′) The third horn the brief asked for.**  §1.4's dilemma is incomplete.
Horn 3: *the bridge holds AND `𝒮_W(ρ)` is empty at every `ρ`* — a state §4.4
itself admits is possible.  Under horn 3 the matching in ⟨1⟩4.⟨3⟩1 is
vacuous, the repaired value is exactly as stipulated as the frozen one, and
the honest disposition is the one the work order explicitly prefers: **retire
the value from the definition**, keep 3a as the whole of clause 3, and carry
the `ρ`-matching as a conditional CLAIMS row rather than a definitional
clause.  That option is never considered.

---

### F2.  The load-bearing premise — "`L` is never defined anywhere in the corpus" — is FALSE in substance, and the corpus's actual construction of `L` **forces the frozen value**.

**(a) Location.**  §1.5 (ll.138–149), the whole of which licenses the repair
strategy; echoed in H2 (l.604) and in §8's instruction to bd `tns-v44`.

**(b) My computation (exhaustive grep, K-d).**  Two findings, one narrow and
one substantive.

*Narrow — the target's grep is itself incomplete.*  §1.5 asserts its grep
"returns only clause D24(d)3, `ml5-universality.md` ⟨1⟩3 hyp. 3 / (6) /
⟨2⟩1.⟨3⟩2, and the two S1 shards transplanting them".  It does not return
`theory/soft-index.md:161–162`, which reads:

> **⟨2⟩4.**  D29's canonical flux factor
> `L_\lambda(0,h) = -i\,sgn(v_h-v_s)/(2ρ_\lambda v_h)`

That is a **named definition of the flux factor**, in `theory/`, carrying the
*exact value the adjudication re-derives*.  The pattern `L(k,h)\|L(0,h)`
cannot match the subscripted `L_λ(0,h)`, so the grep was blind to it.  The
sentence "the grep returns only …" is factually wrong.

*Narrow, in the target's favour — one part DOES hold.*  I confirm by my own
exhaustive grep, **including `notation.md`, which the target's grep omitted**
(and which is the L4 single source for symbols): there is **no `notation.md`
row for `L`**, and no `L :=` anywhere in `definitions.md`, `notation.md`,
`claims/`, `theory/` or `paper/`.  As a *symbol-registry* complaint, §1.5 is
right, and it is a genuine L4 defect.

*Substantive — the object's provenance IS fixed, three times, and it fixes
the value.*  A definition need not use the letter `L`:

1. `theory/soft-current-recon.md` ⟨1⟩7, ML4 plan: "The pole denominator is
   `ω(k_h+k_s)−ω(k_h) = v_h k_s + O(k_s²)`; combine it with (R14) and
   `e^{ik_s}−1`."
2. `paper/main.tex:524–527`: "`\braket{k_h|Q_0^\dagger J^-_0|k_h}=2\ic v_h`;
   **dividing a hard external-leg reduction by the energy shift `v_h k_s`
   cancels the velocity and leaves the `2`**."
3. `theory/soft-index-b.md:808`: "the `1/v_h` is the on-shell pole residue
   `[ω(h+k_s)−ω(h)]^{-1}·k_s`".

All three say the same thing: the `1/v_h` in `L` **is the reciprocal LSZ
energy denominator**.  Now compute (my V2): `v_h = ZJ\sin h`, so the energy
denominator already carries one power of `Z`, and the residue (my V3) carries
one power of `Z`; they cancel exactly, giving jet `2χ` at every `Z`.  In
other words the corpus's own construction of `L` **reproduces the defect and
leaves no room for an extra `1/Z`**.  The extra factor is not something
clause 3 "lost"; it is a factor neither clause 2 nor clause 3 has a home for.
`soft-index-r1.md` F1(c)(i) already located its true home and named it as an
open lemma: "charge-created soft-leg amputation contributes the per-site leg
density `2ρ` to the external flux".  That lemma is still unproved, and the
adjudication does not prove it (its only argument, ⟨1⟩3.⟨3⟩4, is
self-declared not-a-proof — see M2).

**Consequence for the merge.**  Merging §5.2 clause 3b verbatim writes into
the L4 file a value for `L` that contradicts `soft-current-recon.md` ⟨1⟩7,
`paper/main.tex:525` and `soft-index-b.md:808`, none of which is listed in
§4.2 or §4.3.  The merge would *create* an L4 inconsistency while claiming to
remove one.

**(c) FIX DEMAND.**  Either (i) put the `1/(2ρ)` where the corpus says it
belongs — a soft-leg amputation/normalisation factor, stated as an explicit
sixth ingredient of the decomposition (clause 1 or 2), leaving D24(d)3's
`L(0,h) = −iχ/v_h` intact as the reciprocal energy denominator — or
(ii) keep it inside `L` **and** add `paper/main.tex:524–527`,
`soft-current-recon.md` ⟨1⟩7 and `soft-index-b.md:808` to §4.2's lockstep
table with the corrected reading; and add a `notation.md` row for `L`.

**(d) SURVIVING WEAKER STATEMENT.**  *The symbol `L` has no `notation.md`
row and no `L :=` in the corpus — a real L4 defect worth fixing.  But its
provenance is fixed in three places as the reciprocal LSZ energy denominator
`[ω(h+k_s)−ω(h)]^{-1}k_s`, which forces `L(0,h) = −iχ/v_h`; the missing
`1/(2ρ)` therefore belongs to the soft-leg amputation, an unproved lemma,
not to the flux.  The bookkeeping choice between the two homes is not
determined by anything currently in the corpus.*

---

### F3.  §5.2's `Z := 2ρ = ⟨Ω|[S^+_x,S^-_x]|Ω⟩` is not correct as written, and `Z` collides with a registered overload rule.  Not verbatim-mergeable.

**(a) Location.**  §5.2, merged D24(d) preamble, ll.516–522 (the sentence
"…so the order-parameter density `Z := 2ρ = ⟨Ω|[S^+_x,S^-_x]|Ω⟩` is a
positive integer"); reused in merged clause 2 (ll.533–538) and clause 3b
(l.545).

**(b) My computation.**  Three independent problems in one sentence.

*(i) `|Ω⟩` is a D6 object.*  `notation.md:23` registers
"`|Ω⟩`, `|x⟩`, `|x,y⟩` | all-up vacuum, one-down-spin basis, ordered
two-down-spin basis | **definitions.md D6**", and `definitions.md:348` fixes
D6 as `S_x = σ_x/2`, spin-`1/2`.  Read against the single source, the merged
clause says `Z = 2·(1/2) = 1` **always**, which collapses the entire repair
back to the frozen clause.  Read as a new general object, it silently
overloads a registered D6 symbol inside D24(d) — an L4 break.

*(ii) It is site-dependent and sign-flipping in the setting where `ρ` lives.*
`ρ` is defined (`notation.md:270`) by the antisymmetric tail pair
`ω_α(S^z) = +ρ = −ω_β(S^z)`.  In that setting `⟨[S^+_x,S^-_x]⟩ = 2⟨S^z_x⟩`
is `+2ρ` at the α tail and `−2ρ` at the β tail, and is `x`-dependent across
the kink — which is the campaign's actual object (D13's wall).  Then
`L(0,h) = −iχ/(Zv_h)` flips sign between tails.  The clause needs an explicit
"`Z := ω_α([S^+_x,S^-_x]) = 2ρ` at the α tail" in GNS/state language, not a
ket.

*(iii) Bare `Z` is reserved.*  `notation.md:131`, overload rule 9: "bare
`X, Y, Z` are the Pauli matrices inside the explicit D23 comparison tensors
and the contractions built from them".  §5.2 introduces bare `Z` as the
order-parameter density in `definitions.md` with no `notation.md` row and no
amendment to rule 9.  The adjudication's own diagnosis was an unregistered
symbol; the merge adds two more (`Z`, and `𝔈^O` — see m1).

*(iv) su(2) is smuggled in.*  D24(d) previously needed only a `U(1)` circle
charge (`S^z` via D26).  `[S^+,S^-] = 2S^z` needs the full su(2), which the
general class does not have.  As written, the merge silently narrows
`𝒮_W(ρ)` to su(2)-covariant models.

**(c) FIX DEMAND.**  Replace with: "`Z := 2ρ`, where `ρ := ω_α(S^z) > 0` is
the α-tail density of `notation.md`'s `ρ`-row; in an su(2) model with a fully
polarised α tail, `Z = ω_α([S^+_x,S^-_x])`" — and add `notation.md` rows for
`Z`, `L`, `𝔈^O` and the renamed `𝒮_W(ρ)` in the same commit.

**(d) SURVIVING WEAKER STATEMENT.**  *`Z = 2ρ` is a correct and useful
identity for a uniform, fully polarised su(2) tail (I verified `Z = 2S` at
`2S = 1..6`), and the intended content of the clause is right; only its
displayed form is wrong for the general class and clashes with the symbol
table.*

---

## 3. MAJOR

### M1.  ⟨1⟩5 refutes a strawman: lane B's operative factor **is** the adjudication's own `1/Z`, the `(2ρN)^{-1/2}` route is a *critic's* counter-analysis, and the ROLE header's "neither lane's workaround was imported" is false.

**(a) Location.**  ⟨1⟩5.⟨2⟩1 (ll.322–324), ⟨1⟩5.⟨3⟩1 (ll.326–331), H4(ii)
(ll.625–629), §8's instruction to bd `tns-v44` (ll.709–711); ROLE header l.4.

**(b) My computation (reading the artifacts it claims to refute).**

*Lane B.*  `theory/soft-index-b.md:802–811` (B14 bullet 2) reads: "the
charge-created leg has squared norm `‖Q_{k_s}|Ω⟩‖²=2ρN` …, so one
unit-normalized soft magnon carries `(2ρN)^{-1/2}` of the charge-created
datum, **and the multiplier normalization divides by the per-volume leg
density `2ρ`**."  The displayed product two lines later is
`(e^{ik_s}−1)·L(k_s,h)·[2i v_h]·\frac{1}{2ρ}`.  The operative factor is
`1/(2ρ) = 1/Z`, `N`-free.  Lane B's chain does **not** terminate in an
uncancelled `N^{±1/2}`, so ⟨1⟩5.⟨3⟩1's argument ("no chain that terminates in
an uncancelled `N^{±1/2}` can yield it") does not touch it.  Worse,
⟨1⟩5.⟨3⟩3 — "The `N`-free invariant that *is* available … is
`Z = ‖Q^-_k|Ω⟩‖²/N`, and it enters once" — is *verbatim lane B's own move*.

*Lane A.*  `soft-index-r1.md` F1(b)4 is the **critic's** objection against
lane A: "'Normalizing the Goldstone leg by this `2ρ_λ` norm' cannot produce
`1/(2ρ)`. … normalising it to a unit external magnon divides by
`‖Q_k|Ω⟩‖=(2ρN)^{1/2}` — **one** power of `(2ρ)^{1/2}`, not `2ρ`."  The
`(2ρN)^{-1/2}` is the critic's computation of what lane A's rationale *would*
give; lane A asserted `1/(2ρ_λ)` directly (`soft-index.md:161–162`).  So
⟨1⟩5 attributes to both lanes a route neither asserted, assembled out of a
prior critic's counter-analysis, and then refutes it.

*The header.*  `soft-index.md:161–162` defines the "canonical flux factor"
`L_λ(0,h) = −i\,sgn(v_h−v_s)/(2ρ_λ v_h)` — **identical to (D24N.1)**, and
structurally identical: density folded *inside* the flux, definitionally.
`soft-index-b-r1.md:589–597` (X2) already named the two structures and said
they are "numerically identical and structurally incompatible".  The
adjudication adopts lane A's structure while its ROLE header states "neither
S1-A nor S1-B owns this edit and neither lane's workaround was imported".
(Folding it in is *permitted* here — binding §3.3 delegates the resolution to
`tns-iu5` — but the header and H4(ii) must stop claiming otherwise.)

**(c) FIX DEMAND.**  Rewrite ⟨1⟩5 and H4(ii) to say what is true: "lane B's
displayed factor is the per-volume density `1/(2ρ)`, i.e. the same invariant
used here, with the `(2ρN)^{-1/2}` sentence a stray parenthetical; lane A's
`L_λ(0,h)` (`soft-index.md:161`) is this same value with this same
structure; the `(2ρN)^{-1/2}` route was the S1-A *critic's* refutation, not a
lane's claim"; and correct the ROLE header and §8's `tns-v44` instruction.

**(d) SURVIVING WEAKER STATEMENT.**  *What is refuted is the S1-A critic's
diagnosis that a bare unit-normalisation of the soft leg supplies the factor
(it gives `Z^{-1/2}`); what is NOT refuted is either lane's arithmetic or
lane B's per-volume-density bookkeeping, which is this adjudication's own.
Neither lane derived the factor and neither does this adjudication.*

### M2.  ⟨1⟩3 is advertised as "the load-bearing step … where the density actually lives" and carries no load; its only structural argument (⟨3⟩4) gives `Z^{-1/2}` on its own terms and contradicts ⟨1⟩5.⟨3⟩2.

**(a) Location.**  ⟨1⟩3 preamble (ll.240–241), ⟨1⟩3.⟨3⟩3 (ll.259–265),
⟨1⟩3.⟨3⟩4 (ll.266–277); against ⟨1⟩5.⟨2⟩1.⟨3⟩2 (ll.333–338) and H4(ii).

**(b) My computation.**  (K-a) gives, at `2S = 1,2,3,4`, printed side by
side: `residue = Z·2iJ\sin h = 2i v_S(h)` — the two expressions are the
*same number at every `S`*, because `v_S = ZJ\sin h`.  So:

* (D24N.4) is an identity once V2 is known; it adds no information beyond
  the dispersion.  What ⟨3⟩3 calls "the `Z`-carrying reading" and "the
  `Z`-free kinematic number" differ only in whether one has substituted
  `v_h = ZJ\sin h`.  D24(d)2's `2i v_h` is CORRECT at every `Z` (my V3);
  only (R14)'s *intermediate string* `2iJ\sin k_h` is `Z=1`-specific, and
  (R14) is a D6 statement, as §4.3 itself says.
* Hence "D24(d)3's `−iχ/v_h` … cancels it in full.  **That single
  cancellation is the entire defect**" is a narrative overlay.  The
  cancellation is real (my V4) but it is the *correct* cancellation of a
  correct residue against a correct reciprocal energy denominator (F2).
  Nothing is "lost" in ⟨1⟩3; the `1/Z` is an *addition* with no source there.
* ⟨3⟩4, the only structural argument for the power, is self-inconsistent on
  its own bookkeeping: with `S^-_x = \sqrt{Z}a^\dagger_x(1+O(n/Z))`, the
  residue pairs two insertions and carries `Z`; normalising the **one**
  external soft leg divides by `\sqrt{Z}` — leaving `\sqrt{Z}`, i.e. the
  half-power.  Dividing by `Z` requires normalising *both* insertions, and
  the current `J^-_0` is not an external leg.  ⟨3⟩4 is precisely a
  leg-normalisation argument, and ⟨1⟩5.⟨3⟩2 / H4(ii) declare that "a leg
  normalisation cannot in any case generate the factor".  The document
  refutes its own ⟨3⟩4.

Consequently the entire load is carried by ⟨1⟩4.⟨3⟩1's matching (see F1), and
⟨1⟩5's "for a reason stronger than 'wrong power'" is overclaimed: once the
"generate the jet" / "fix the coefficient" distinction is drawn (it is drawn
nowhere), ⟨1⟩5 reduces to "wrong power".

**(c) FIX DEMAND.**  Demote ⟨1⟩3 from "load-bearing" to "consistency check of
clause 2 at every `Z`", strike "That single cancellation is the entire
defect", and either delete ⟨3⟩4 or restate it as an open question — "the
power is `1` empirically; a `\sqrt{Z}` leg normalisation would give `1/2`, so
the mechanism is not a leg normalisation" — which is what the corpus already
believes (`soft-index-r1.md` F1(b)5).

**(d) SURVIVING WEAKER STATEMENT.**  *`⟨h|Q_0^†J^-_0|h⟩ = 2i v_S(h)` exactly
at every `S` (verified) — so clause 2 is correct at every density and needs
no repair.  The exponent `p=1` is fixed by matching, not by any structural
count of order-parameter insertions.*

### M3.  The certificate contains two no-op gates, and its acceptance test is deductively subsumed by its ground-truth gate: "the acceptance test is not self-fulfilling" is unsupported.

**(a) Location.**  `theory/checks/d24d3_normalization_check.py` ll.183–190
(the "soft-leg norm" half of D24N-C2) and ll.309–313 (the "exact-law
exponent" of `check_exponent_is_one`); §7's mutation table
(ll.685–693) and the sentence "confirming the acceptance test is not
self-fulfilling"; §0 (A-b) and ⟨1⟩2.⟨2⟩1.⟨3⟩2's justification "named
computation D24N-C2"; ⟨1⟩4.⟨2⟩1.⟨3⟩2 "to the exact law `p = 1` to
`< 10^{-9}`".

**(b) My computation (mutants on copies, scratchpad).**

*No-op 1 — the soft-leg norm.*  Lines 185–190 compute
`sum(abs(exp(1j*k*x))**2 * float(two_s) for x in range(sites))` and then
check `norm_squared/sites − two_s ≈ 0`.  Since `|e^{ikx}|² = 1`, this is
`sites·two_s/sites − two_s ≡ 0` **by construction**.  It never calls
`apply_lowering` or `spin_matrices`; it never builds `Q^-_k|Ω⟩`.  I ran the
expression for `two_s = 3.7`, `−5.0` and `10^6` — non-existent
representations, one with negative "spin" — and it returns error
`≤ 4.4·10^{-16}` in every case.  This is the exact shipped-no-op pattern the
protocol names.  (The *statement* is true — I verified `‖Q^-_k|Ω⟩‖²/N = 2S`
properly in V1 — but the certificate for it is void.)

*No-op 2 — the "exact-law" exponent.*  Lines 309–311 build
`ideal_design[i] = log(2S_i)` and `ideal_target[i] = log(2/(1/S_i)) =
log(2S_i)`.  Design and target are **elementwise identical**; `lstsq(x,x)`
returns `1.0` for any spins.  I ran it with `SPINS = (0.3,7.1,100.0)` and
`(10^{-3},10^3)`: exponent `1.0` and `1.0000000000000002`, `design==target`
`True` in every case.  The "`p = 1` to `< 10^{-9}`" cited in ⟨1⟩4.⟨3⟩2 is
`y = x` fitted to itself.

*Subsumption — no data can kill the acceptance test.*  `check_ground_truth`
(D24N-C4) requires, for every row, `|m_r − 1/S|·S < 0.08`.  `check_repair`
(D24N-C6, `p=1`) requires `|1/S − \bar m|·S < 0.08` with `\bar m` the row
mean; since `|mean| ≤ max`, **C6 passes whenever C4 passes** — deductively.
For the exponent half: `p − 1 = −Σ_i x_i\log(1+ε_i)/Σ_i x_i²` with
`x = (0, \log2, \log3, \log4)`, `Σx² = 3.6079`, `|\log(1+ε)| ≤ 0.0834`, so
`|p−1| ≤ 0.0834·3.178/3.6079 = 0.0735 < 0.08`.  The whole of D24N-C6 is
implied by D24N-C4.  Empirically: I shifted **every** summary row by
`−7.99%` (`m7_adv`) — C4 passes at `0.0799`, and the checker exits **0** with
`fitted exponent = 1.0733`.  The three mutants reported in §7 all "died at
D24N-C4" — the ground-truth gate — and none reached the acceptance test.
That observation does not license the conclusion drawn from it; the correct
conclusion is the opposite.

*Bonus hole.*  `band = payload.get("decision_band", DECISION_BAND)` (l.242).
Moving the band is caught; **deleting the key is not**.  My `m1_noband` copy
(key removed) exits **0**.  §3's parenthetical "read from the data file, and
the checker fails if that band is moved" is true only for "moved".

*Resolving power.*  Scanning `p` against the real data, every
`p ∈ [0.950, 1.060]` passes D24N-C6.  The certificate pins the exponent to
`±5%`, not to `1`.

**(c) FIX DEMAND.**  (i) Replace the D24N-C2 norm block with an actual
construction of `Q^-_k|Ω⟩` from the ladder matrices; (ii) delete the
`lstsq(x,x)` "exact-law" block or replace it with a symbolic solve of
`2(2S)^{-p} = 1/S`; (iii) add an acceptance test that can fail independently
of D24N-C4 — e.g. compute the jet from a *constructed* `𝔈^O` rather than
from the hardcoded `predicted_jet = 2.0/(2S)**p`; (iv) `require` the
`decision_band` key to be present; (v) restate §7 as "all data mutants die at
the ground-truth gate; the acceptance test has no independent failure mode".

**(d) SURVIVING WEAKER STATEMENT.**  *The checker correctly certifies two
things: the frozen constant misses the `1/S` band at `S = 1, 3/2, 2` and hits
it at `S = 1/2` (D24N-C5, real), and the Ward residue is `Z`-linear (D24N-C3,
real, and I reproduce it independently).  It certifies nothing about `L`,
`𝔈^O`, or the LSZ decomposition, and its four red modes mutate the
hypothesis, never the evidence.*

### M4.  Quantifier over-reach in `ρ`, and the merged preamble drops a load-bearing hypothesis of the PROVED row it cites.

**(a) Location.**  §5.2 preamble ll.516–521 and clause 3b ll.544–550;
⟨1⟩2.⟨2⟩1.⟨3⟩3 (ll.223–226); against `claims/CLAIMS.md:72` M-IDX-density.

**(b) My computation.**  (i) The merged clause asserts
`L(0,h) = −iχ/(2ρ v_h)` for **every real `ρ > 0`**.  The matching covers
`ρ = S ∈ {1/2,1,3/2,2}` in ONE model family (`H_S`).  Even granting the exact
law for all half-integers, `M-IDX-density`'s own adjudicated scoping says
"`ρ` is a **free real parameter** of the vacuum pair", and `2ρ ∈ ℤ` only
under (INT).  At non-half-integer `ρ` — admitted whenever D26(INT) fails —
nothing in the corpus fixes the value.  Statement, proof and merge text are
at three different strengths.

(ii) `M-IDX-density`'s adjudicated scoping sentence lists as hypotheses "D1
injective tensors, D2(a) covariance with a common unbroken circle direction,
D2(b)'s uniqueness clause, (S) of D2(e) at both tails, D26(INT), **and the
ANTISYMMETRY `ω_β(S^z) = −ω_α(S^z) =: −ρ`.  The antisymmetry is
load-bearing:** one tail alone gives only `ρ ∈ κ+ℤ` and a general tail pair
only `ρ_α−ρ_β ∈ ℤ`."  §5.2 cites the row as "under (S) at both tails and
D26(INT), claim `M-IDX-density` gives `2ρ ∈ ℤ`" — **antisymmetry omitted**.
Under-stating the hypotheses of a PROVED row, verbatim, in the L4 file.

**(c) FIX DEMAND.**  In §5.2 restore "and the antisymmetric tail pair
`ω_β(S^z) = −ρ`" to the `2ρ∈ℤ` citation, and fence clause 3b: "the value is
fixed by matching at `ρ = S ∈ {1/2,1,3/2,2}` in the fully polarised
spin-`S` register and is *hypothesised* to hold at other `ρ` by clause 3a's
process independence; process independence is over sources `O`, not over
models or densities".

**(d) SURVIVING WEAKER STATEMENT.**  *`L(0,h) = −iχ/(2ρ v_h)` is
matching-fixed at four half-integer densities of one model family and
extended to other `ρ` by hypothesis; `2ρ ∈ ℤ` requires the antisymmetric
tail pair, not merely (S)+(INT).*

### M5.  The adjudication reverses two binding decisions of `soft-index-adjudication-r1.md` §3 without acknowledging either.

**(a) Location.**  ASSUME (ll.156–160) and §5.2's preamble; H2 (ll.603–610);
against `theory/verdicts/soft-index-adjudication-r1.md` §3.2 (ll.99–108) and
§3.5 (ll.126–130).

**(b) My computation (reading the binding text).**  §3.5: "**Sector register:
S1-A's `m_λ` (actual magnetization, `m_λ/N→ρ`) wins** for the free-`ρ`
discipline; S1-B's `M=ρN−n` presupposes `ρ=S∈½ℤ` **through the fully-
polarized vacuum — exactly what the target forbade**."  The adjudication's
ASSUME is "the fully polarised ferromagnetic register `H_S` …, in which
`ρ = S`", and §5.2 writes a fully-polarised-vacuum object (`⟨Ω|[S^+,S^-]|Ω⟩`)
into the general D24(d).  That is the struck register, promoted from a shard
into `definitions.md`.  §3.2: "the r2 statement takes the value from on-shell
input … The slope-law theorem is therefore **conditional on an on-shell
matching hypothesis, named and displayed**, or it is a theorem about the
descendant-projected datum only."  §5.2 instead ships "derived and not
stipulated".  Neither reversal is flagged anywhere in §§1–8.

**(c) FIX DEMAND.**  Add a subsection acknowledging both, and either honour
§3.2 (name and display the matching hypothesis in the clause — the F1(c) fix
does this) or state explicitly that `tns-iu5` supersedes §3.2/§3.5 and why.

**(d) SURVIVING WEAKER STATEMENT.**  *Using the fully polarised register as
the computation site is legitimate and unavoidable — it is the only register
where the corpus can compute — provided the conclusion is scoped to it and
the extension to general `ρ` is labelled a hypothesis.*

### M6.  Missed lockstep sites, including two in the OTHER L4 single source.

**(a) Location.**  §4.1/§4.2/§4.3, which claim "Every address below was
obtained by grep, not by recall."

**(b) My computation (grep).**

| Missed site | Content | Why it moves |
|---|---|---|
| `notation.md:258` | "`𝒮_W` \| the five-condition Ward/LSZ/no-contact source class …" | the merge renames the object `𝒮_W(ρ)`, a `ρ`-indexed family |
| `notation.md:244` | "`𝖲(k_s;{q_i,v_i})` \| … on the D24(d) class `𝒮_W`" | same rename |
| `ml5-universality.md:158` | "The coefficient is the signed **two-site** Wigner displacement" | after the repair the displacement is `χ/ρ` sites, not two |
| `soft-current-recon.md` ⟨1⟩7 (ML4 plan), `paper/main.tex:524–527`, `soft-index-b.md:808` | the flux's provenance as reciprocal energy denominator | F2 |
| `theory/soft-index.md:161–162` | `L_λ(0,h)` "canonical flux factor" | F2, M1 |

`notation.md` is not mentioned once in the entire blast radius.  Under L4 it
is a co-equal single source with `definitions.md`.  (I checked the sites the
document *does* list: `TRIANGLE.md:24,215,254,257,528` display no constant —
confirmed; `ml5-universality.md` lines 51/68/81/142–144/155/170–172/183–184/
324–327 are all correct addresses; `definitions.md:933/938/945/960–961` are
correct; `ml4_check.py` 213/220/299/312–330 are correct.)

**(c) FIX DEMAND.**  Add the five rows above to §4.2, and add a §4.2b for
`notation.md` (rows for `𝒮_W(ρ)`, `L`, `Z`, `𝔈^O`, and an amendment to
overload rule 9).

**(d) SURVIVING WEAKER STATEMENT.**  *The blast radius is right about every
site it lists, and right that `D24(c)` must move in lockstep with `(d)3`; it
is incomplete, and its omissions are concentrated exactly where the "L is
undefined" premise made it stop looking.*

### M7.  Merged clause 3a drops the `k ≠ 0` well-definedness caveat, and asserts uniform `C¹` for a function defined only off the zero set of `M_1^O`.

**(a) Location.**  ⟨1⟩1.⟨2⟩1 (l.182: "well defined wherever `M_1^O ≠ 0` and
`k ≠ 0`") vs §5.2 clause 3a (ll.540–543: "well defined by clauses 1--2
wherever `M_1^O ≠ 0`").

**(b) My computation.**  Two gaps, one textual and one analytic.
(i) The `k ≠ 0` restriction is present in the Lamport step and absent in the
text destined for `definitions.md`.  This is the exact divergence F1(b)(i)
turns on, and the merge silently repairs it by deletion.
(ii) `M_1^O ∈ L²(I)` and `M_1^O ≠ 0` (as an `L²` element) does **not** give
`M_1^O(h) ≠ 0` pointwise; `M_1^O` may vanish on a nonempty closed set inside
`I`.  `L` is then defined off that set only, and "uniformly `C¹`" on a domain
with holes is not a hypothesis one can state as written.  Denominator
boundedness (brief item 2): `v_h` yes (V9); `M_1^O(h)` no; `(e^{ik}−1)` no,
and it vanishes precisely at the point of evaluation.

**(c) FIX DEMAND.**  Clause 3a: "…well defined for `k ≠ 0` at every `h` with
`M_1^O(h) ≠ 0`; the hypothesis is that it extends to a process-independent,
uniformly `C¹` function on `{|k| ≤ ε} × I`, and `L(0,h)` denotes that
extension's value at `k = 0`."

**(d) SURVIVING WEAKER STATEMENT.**  *With the extension hypothesis stated,
3a is a coherent and nonvacuous condition (V8); without it, `L(0,h)` names
nothing.*

---

## 4. MINOR

**m1.  `𝔈^O` is a new unregistered symbol that collides with an existing
one.**  §5.2 clause 1 introduces "`𝔈^O`"; `definitions.md:121–124` already
uses `𝔈_W`, `𝔈_{A_α}`, `𝔈_{A_β}` for the window CP map.  No `notation.md`
row is proposed for either.  *Fix:* use a non-fraktur name (`E^O_{desc}`) or
register the sub/superscript discipline in `notation.md`.  *Surviving:*
naming the descendant term is a real improvement over the frozen clause 1,
which names no symbol at all.

**m2.  The merged clause 2 imports a model-specific dispersion into a
model-general definition.**  §5.2 clause 2 adds "`⟨h|Q_0^†J^-_0|h⟩ =
Z·(2iJ\sin h) = 2i v_h`, because `v_h = ZJ\sin h`" — true only for the
nearest-neighbour isotropic spin-`S` ferromagnet, and it puts a coupling
constant `J` into a clause quantified over an unspecified model class.
*Fix:* keep clause 2 as `2i v_h M_1^O(h)` (which V3 shows is correct at every
`Z`) and move the spin-`S` verification to a footnote citing D24N-C3.
*Surviving:* the identity itself, in the spin-`S` register.

**m3.  D24(c) becomes model-dependent.**  §5.1 makes `𝔠_h(O)` depend on `ρ`,
so `𝔠_h` — and with it PROVED ML5-A's criterion — is undefined for any model
without a broken-symmetry tail pair, where before it was model-agnostic.
Also a forward reference `(c) → (d)`.  *Fix:* state "for a model with a
tail density `ρ > 0` in the sense of (d); at `ρ = 1/2` this is the frozen
form".  *Surviving:* the lockstep requirement B3 is correct — if `(d)3b`
moves and `(c)` does not, ML5-A becomes a criterion for a factorisation
nobody claims.  I verified ML5-A's proof (`ml5-universality.md` ⟨1⟩2)
evaluates at `k=0` and differentiates once and never uses the value, so the
iff survives the substitution.

**m4.  The "four-density over-determination" is weaker than advertised.**
The four densities are four points of ONE analytic curve `1/S` from ONE
PROVED theorem, not four independent measurements; and in
`check_exponent_is_one` the `S = 1/2` row has design entry `\log(2·0.5) = 0`,
so it contributes nothing to the least-squares — the fit is over three
points.  *Fix:* say "over-determined by the exact law `2(2S)^{-p} = 1/S`
holding at two or more distinct half-integer `S`" (which is true and
sufficient) rather than "four densities".  *Surviving:* the exponent IS
uniquely `p = 1` within the family `(2ρ)^{-p}`, given the exact law.

**m5.  The Watanabe–Murayama corroboration fixes the invariant, not the
factor 2.**  Their type-B density for the Heisenberg ferromagnet is
`m = ⟨j^0_z⟩ = ρ` (l.338), not `2ρ`; `Z = 2ρ` is the complexified-basis
restatement.  Using WM's own normalisation in ⟨1⟩3.⟨3⟩4's structural argument
would give jet `2χ/ρ`, not `χ/ρ`.  The factor of 2 is fixed by the matching
alone.  *Fix:* label ⟨1⟩2.⟨3⟩4 "consistent with", not "exactly".
*Surviving:* the identification of `Z` as *the* type-B symplectic density is
sound and is a genuinely good observation.

**m6.  Mis-citation at §1.3.**  "`ml5-universality.md` ⟨1⟩4.⟨3⟩4 uses exactly
that `s'(0,h) = 2i` as the number ML5-B (5) reproduces" — ⟨1⟩4.⟨3⟩4 uses
`s'(0,h)=2i` to compute the *bra coefficient in the `O_η` counterexample*
(ll.259–262), not as ML5-B's constant.  The bridge §1.3 asserts is real as a
numerical coincidence at `ρ=1/2` but this step is not evidence for it.
*Fix:* cite `soft-current-recon.md` (R17) and `oracle-bethe.md` O9 only.
*Surviving:* the bridge is still the corpus's working identification, and
H5 already flags it as unproved — which is the honest position.

---

## 5. NOTE

**n1.**  Address slip: §⟨1⟩4.⟨3⟩4 cites `paper/main.tex:338–339` for "the
hard particle's `U(1)` charge in units of the vacuum spin density"; the
phrase is at ll.340–341.

**n2.**  §4.3 does not enumerate `paper/main.tex:542–546` (Appendix B's prose
list of the five conditions).  I checked it: it names "a process-independent
`C^1` kinematic LSZ normalization" without a value, so it survives.  Listing
it would have been cheap.

**n3.**  After the merge, `theory/soft-index-b.md:757–758, 808` and
`theory/soft-index.md:161–162` will display a D24(d)3 that `definitions.md`
no longer holds.  They are failed-lane records, so an ERRATUM pointer rather
than an edit is probably right — but §5.4's ADVISORY covers only
`ml5-universality.md`.

**n4.**  Pre-existing, not this artifact's fault: `notation.md:91–96`
overload rule 2 says `χ` means the bond dimension "everywhere in this repo
except inside `oracle-bethe.md` ⟨1⟩3" and "Do not import `χ` as a sign into
any other shard", yet D24(c)/(d) already use `χ` as the sign.  The merge
multiplies the usage (five new occurrences).  Worth folding into the same
`notation.md` pass demanded by F3(c)/M6(c).

---

## 6. Register comparison against the nearest PROVED rows

The nearest PROVED rows are **`S2-2body-S`** (the input) and
**`M-IDX-density`** (the source of `ρ`).  Their adjudicated scoping
sentences are models of the register this artifact should be claiming in:

* `S2-2body-S`: "PROVED per spin-s-r1.md adjudication: **proves the
  unit-charge exact two-body slope only**; it does not prove endpoint or
  equal-velocity limits, spin-`S` Bethe completeness, S-general, the memory
  half, the `|q_hard|>1` factor, or Conjecture Bc."
* `M-IDX-density`: "**Adjudicated scoping (verbatim):** Hypotheses in full:
  … and the ANTISYMMETRY … **The antisymmetry is load-bearing** … `ρ` is a
  free real parameter … and **no step assumes any relation between `ρ` and
  the on-site dimension `d`**."

**Verdict on register.**  §6's HONEST STATUS (H1–H7) *is* in that register —
H2 says "derived by matching … *not* a first-principles derivation", H3 says
"structural identification, not proof", H5 names the bridge and invites the
push, H6 separates evidence from proof.  H1–H7 are exemplary and I would pass
them on their own.

**But the artifact is not in lockstep with its own honest section.**  The
strength rises monotonically as you move outward from H2 to the merge text:

| Layer | What it says |
|---|---|
| H2 (l.603) | "**DERIVED BY MATCHING** … *not* a first-principles derivation" |
| H3 (l.612) | ⟨1⟩3.⟨3⟩4 is "**not** a derivation" |
| §2 THEOREM D24N (l.155) | "**THEOREM** … PROVE … `L(0,h) = −iχ/(Zv_h)`" |
| §5.2 clause 3b (l.544) | "its value at zero, **derived and not stipulated**" |
| §5.3 CLAIMS row (l.576) | "3b **DERIVES** `L(0,h) = −iχ/(2ρ v_h)`" |
| §1 headline (l.15) | "a surviving hypothesis (3a) and a **derived value** (3b)" |

The two layers that leave this file — the `definitions.md` text and the DAG
row — are the two that overstate.  That is the divergence this method exists
to catch, and it is why the merge cannot go through as written.  On the
`ρ`-vs-`s` fence specifically (brief item 4): the artifact does **not** breach
it — `⟨1⟩4.⟨3⟩4` uses H-MQG(2)'s sanctioned `s = ρ`, never the `d = 2s+1`
gloss, and `notation.md:208/270` explicitly sanction that identification.
What it does instead is execute the entire derivation *inside* the fully
polarised special case the fence exists to prevent generalising from, and
then state the conclusion for all `ρ > 0`.  **Legitimate for the fully
polarised tail; illegitimate as a general-`ρ` statement.**

---

## 7. MERGE / HOLD, clause by clause

| § | Clause | Decision | Missing step |
|---|---|---|---|
| 5.1 | `definitions.md:931–950` — D24(c) `𝔠_h` and the ML5-A criterion | **HOLD** (conditional MERGE) | The lockstep logic is correct (B3/B4 verified) and the replacement is verbatim-appliable at the stated anchors; but it inherits `ρ` from (d), so it cannot merge before 5.2 is fixed, and it needs m3's model-scoping sentence. Merge *only* in the same commit as a repaired 5.2. |
| 5.2 | D24(d) preamble (`𝒮_W(ρ)`, `ρ>0`, `Z`) | **HOLD** | F3 (`Z := ⟨Ω\|[S^+,S^-]\|Ω⟩` wrong as written; bare `Z` collides with overload rule 9; su(2) smuggled in); M4(ii) (antisymmetry hypothesis dropped from the `M-IDX-density` citation); M6 (`notation.md:244,258` unaddressed). |
| 5.2 | clause 2 (the added `Z`-linearity sentence) | **HOLD** | m2 — model-specific dispersion (`J`, `\sin h`) inside a model-general clause. The identity is true (V3); it belongs in a footnote, not the clause. |
| 5.2 | clause **3a** (hypothesis, `L` as quotient) | **MERGE after one edit** | The best thing in the artifact: it makes clause 3 nonvacuous (V8). Edit required: restore `k ≠ 0` and state the `C¹` extension (M7(c)). |
| 5.2 | clause **3b** (the value) | **HOLD** | F1 (`0/0`; matching over a possibly empty class; "derived" false), F2 (contradicts the corpus's three statements of what `L` is), M4(i) (asserted for all real `ρ>0`), M5 (reverses binding §3.2). The *number* is right; the *status word* and the *quantifier* are not. |
| 5.2 | clauses 1, 4, 5 and the closing "no nontrivial microscopic class…" paragraph | **MERGE** | Verified unchanged in substance; the "five-condition" count is preserved (V13) and `paper/main.tex:244` stays correct. `𝔈^O` needs m1's rename or a `notation.md` row. |
| 5.3 | `claims/CLAIMS.md:41` ML5-B row | **HOLD** | Says "3b **DERIVES**"; must say "3b **fixes by on-shell matching**, conditional on the jet-identification bridge (not a PROVED row) and on `𝒮_W(ρ)` nonemptiness (open)". Status **PROVED** for the implication is correct and should stay; adding `S2-2body-S` to depends-on is correct in substance, though the dependency is really D24(d)'s. |
| 5.4 | ADVISORY (`ml5-universality.md` in the same commit) | **MERGE, and it is not optional** | Correct as far as it goes; extend it with M6's five missed sites and a `notation.md` pass. |

**Verbatim-appliability.**  Both REPLACE anchors are exact
(`definitions.md:931–950` begins `**(c) The contact first jet.**` and ends
`factorisation with the same stated norm control.`; `952–973` begins
`**(d) The Ward-covariant no-contact class` and ends `is part of the ML5-B
future work.`).  The "five-condition" count survives the split, and
`paper/main.tex:244` and `main.tex:542–546` remain correct.  So the mechanics
are sound; it is the content of 5.2's preamble and 3b that must not ship.

---

## 8. `𝒮_W` nonemptiness, and bd `tns-axg`

**I concur with §4.4: nonemptiness remains OPEN, at every `ρ` including
`ρ = 1/2`.**  I verified the two halves independently:

* *Before* the repair, the frozen clause forces jet `2χ` at every density
  (my V4) against PROVED `S2-2body-S`'s `χ/S` (my V5) — so, **given the
  bridge**, `𝒮_W` is provably empty for `ρ ≠ 1/2` in the spin-`S`
  ferromagnet register.
* *After* the repair the contradiction is gone, but no source satisfying
  clauses 1, 4, 5 is exhibited at any density.  `definitions.md`'s own
  sentence "no nontrivial microscopic class has been proved to satisfy all
  five conditions" is untouched and is retained verbatim in §5.2.

**bd `tns-axg` stays open**, exactly as §8 says.  I add one consequence the
adjudication does not draw: because clause 3b's value is fixed by a matching
that presupposes a member (F1(b)(ii)), **`tns-axg` and `tns-iu5` are now
coupled** — the value cannot be upgraded from "matched" to "derived" until
`tns-axg` produces a member, or until the soft-leg amputation lemma
(`soft-index-r1.md` F1(c)(i)) is proved.  `tns-iu5` should therefore **not**
be closed on merge; it should be re-scoped to "clause 3 split and the value
matching-fixed; the amputation lemma remains open".

---

## 9. Disposition

1. **Do not apply §5.2's preamble or clause 3b as written.**  Apply clause 3a
   (with the `k ≠ 0` / `C¹`-extension edit) and clauses 1/4/5 if the
   orchestrator wants partial progress; 5.1 must wait for 5.2.
2. **r2 work order (small, and mostly rewriting, not recomputing).**  The
   physics is done and I have fenced it in §1: the r2 lane needs (i) F1(c)'s
   status rewrite, (ii) F2(c)'s bookkeeping decision — flux vs amputation —
   made explicitly and propagated, (iii) F3(c)'s `Z` restatement plus a
   `notation.md` pass, (iv) M3(c)'s three checker repairs, (v) M4/M5/M6/M7's
   text fixes.  No new computation is required except the D24N-C2 rebuild.
3. **Retain the honest sections verbatim.**  H1–H7 and §4.4 are the strongest
   part of the artifact and should survive the repair unchanged.
4. **Empirical position unchanged and strong.**  I independently reproduced
   the frozen ground truth (`A_ring_runs[0]` to `2·10^{-13}`, `δ_ED` vs
   closed form to `10^{-11}` at four spins) and the exact `1/S` law
   symbolically.  Nothing in this verdict weakens the physics; it constrains
   what may be written down as *proved*.

---

**FAIL(F1, F2, F3, M1, M2, M3, M4, M5, M6, M7)**
