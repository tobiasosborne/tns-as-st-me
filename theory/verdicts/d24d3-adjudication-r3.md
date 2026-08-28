<!-- ROLE: orchestrator-lane ADJUDICATION of corpus referral bd `tns-iu5`,
     repair round 3, after the FAIL(F1,M1-M5) verdict
     theory/verdicts/d24d3-adjudication-r2-critic.md.
     Work orders: briefs/d24d3-adjudication.md (r1), briefs/d24d3-repair-r2.md,
     briefs/d24d3-repair-r3.md.  Writable files of this lane: this file,
     theory/verdicts/d24d3-repair-r3-response.md, and
     theory/checks/d24d3_normalization_check.py -- nothing else was edited.
     definitions.md, notation.md and claims/CLAIMS.md are NOT edited here;
     all shared-file text is quarantined in section 5 MERGE PROPOSALS, which
     is ONE coherent application (5.0 is new this round and 5.1/5.2 do not
     stand without it).
     STRUCTURAL PROVENANCE (unchanged from r2, r1-critic M1): the bookkeeping
     adopted here is structurally lane B's split (soft-index-b.md B14); no
     lane derived the factor and this adjudication does not either.
     WHAT CHANGED IN r3 (r2-critic F1): D24(b)'s missing amputation and
     leg-normalisation convention is supplied as displayed text, so `a_leg`
     is convention-independent and AMP is a statable lemma.  The r2 framing
     that `a_leg` is a "home" the density "must" live in is WITHDRAWN: under
     a fixed convention `a_leg` is not a home, it is a determined datum of a
     nonempty class. -->

# r3 adjudication — D24(d) clause 3, the external-flux normalisation

**Verdict.  Unchanged in physics, repaired in three places.  The frozen
clause 3 is REFUTED as a universal value claim (conditional on the corpus's
jet-identification bridge; r1-critic V4/V5/V7).  Clause 3 is SPLIT; the
value is RETIRED from `definitions.md`; and — new this round —
`definitions.md` D24(b) is given the amputation and leg-normalisation
convention it never had, without which the split was a change of variable
rather than a statement.**

Three things are settled this round that were not settled in r2.

1. **The convention (r2-critic F1) is FIXED, as displayed text in the
   D24(b) merge proposal (§5.0).**  Both amplitudes are matrix elements
   against `δ`-normalised asymptotic magnon kernels (D3(a), D12(a′),
   D12(b)); the hard leg is amputated identically in both; the soft leg
   enters `M_2^O` as **one additional `δ`-normalised asymptotic magnon**,
   with unit leg weight.  Under that convention `𝔞_leg` is invariant, and
   **AMP is statable** — it is the proposition `𝔞_leg = 1/Z_ρ` about a
   determined number, and it can be false.
2. **The r2 argument that the density "must live in `𝔞_leg`" is
   WITHDRAWN** (r2-critic F1(b)(ii), M2).  It is not needed and it was not
   sound.  With the convention fixed, `𝔞_leg := i v_h L(0,h)/χ` is not a
   *place* for a factor; it is the **value of a determined quantity** —
   determined by any member of the class, if one exists.  The substantive
   content of clause (3b) is therefore the **`h`-profile** claim (that
   `v_h L(0,h)/χ` does not depend on `h`), not a value and not a choice of
   bookkeeping.  This dissolves r2-critic F1(b)(i)–(ii) and m3 together.
3. **After the merge, ML5-B (PROVED) predicts no number at any density,
   `ρ = 1/2` included** (r2-critic M1(b)(ii)).  This round draws that
   consequence and states its price: the status PROVED is correct and
   stays, the row's *conclusion* is a factorisation **shape** with a class
   constant, and every corpus display of the soft coefficient `2` is
   re-sourced to the contact/oracle route, which is independent of D24(d)
   and unaffected.  Nothing in the corpus now derives a numerical soft
   coefficient from D24(d) at any density.  That is a real loss of reach
   and it is recorded as one (§4.3, H8).

Also new, and the sharpest thing in the round: with the convention fixed,
the **one mechanism anybody has proposed** for AMP — converting the
charge-created soft leg into the convention's asymptotic soft leg — is
computed exactly, `Q^-_k|Ω⟩ = √(Z_ρ)·|k⟩` (named computation **D24N-C8**,
verified against the Hamiltonian's own one-magnon eigenvector), and it
supplies `𝔞_leg = Z_ρ^{-1/2}`, which the ansatz-free data refutes **at the
pre-registered `0.08` band** with a 5–12× margin.  AMP's residual content
is exactly a second factor `Z_ρ^{-1/2}` that no proposed mechanism
supplies.  That makes AMP a sharper prover target than r2 left it, and it
is stated as an open problem with a quantitative fence, not as a promise.

Certificate: `theory/checks/d24d3_normalization_check.py` (green `python3 -O`
exit 0; six red modes with exit *paths* in §7).  The acceptance band is no
longer a post-hoc constant: it is derived from the data's own quoted
extrapolation error (§7.5, r2-critic M3(b)(iii)).

---

## 0. What this round did, and what it did not touch

**Fenced by the r1 critic (V1–V14) and by the r2 critic (W1–W18) — certified
by two independent recomputations, not re-derived here.**

* r1-critic §1 V1–V14: `Z_ρ = 2ρ = 2S`; `‖Q^-_k|Ω⟩‖²/N = 2S`;
  `ω_S(k) = 2JS(1−cos k)`, `v_S(h) = Z_ρ J sin h`; the exact Ward residue
  `⟨h|Q_0^†J^-_0|h⟩ = 2i v_S(h)`; the frozen clause's exact
  density-blindness; the exact slope `∂_{k_s}log S_{12}|_0 = i/S`; the
  frozen data and its independent ED reproduction; the collision and hence
  emptiness-given-the-bridge; nonvacuity of the quotient definition of `L`;
  `v_h` bounded below on `I`; the L3 Watanabe–Murayama quotation; every
  §4.3 "does not change" claim; the line anchors and the five-condition
  count; the VALUE arithmetic and the exponent forcing.
* r2-critic §1 W1–W18, in particular: the checker's green and four red exit
  **paths** (W1); reachability of the acceptance gate (W2); the `−6%`
  mutant that passes C4 and dies at C6 (W3); the `−7.99%` correction (W4);
  **both r1 no-ops genuinely gone** (W5); the data-mutant exit paths (W6);
  the value arithmetic and the split identity (W7); `Z_ρ` collision-free
  (W8); ANTISYMMETRY restored (W9); clause 3a is M7(c) verbatim (W10); the
  `ρ = S` register move does not breach the standing fence (W11);
  `ml5-universality.md` blast radius COMPLETE (W12); `TRIANGLE.md` clean
  (W13); `ml4_check.py` and D24(e) are `𝔞_leg`-blind (W14); §5.1 internally
  consistent and verbatim-appliable (W15); the five-condition count and the
  paper survive (W16); r1's M1/M2 properly retracted (W17); the HONEST
  STATUS section in lockstep (W18).

None of that is re-litigated below.  Leaves cite it as `r1-critic V*` /
`r2-critic W*`.

**Done this round (no new physics beyond one measured constant):**

* **(R3-a)** D24(b)'s amputation and leg-normalisation convention supplied
  (§2 ⟨1⟩0, §5.0) — the r2-critic F1 fix demand, taken rather than
  declined.  `𝔞_leg` becomes convention-independent; **AMP becomes
  statable**; the r2 "only place it can live" argument is withdrawn and
  replaced by the correct one (⟨1⟩2).
* **(R3-b)** The five "recovered verbatim at `ρ = 1/2`" strings are struck
  from every layer, and the consequence r2 never drew is drawn: after the
  merge ML5-B predicts no number at any density (§4.3, §5.3a, H8).  The
  false "the form in which D24(e) and `ml4_check.py` test it" clause is
  struck (r2-critic M1(b)(iii), W14).
* **(R3-c)** Quantifiers rescoped (r2-critic M2): "at **every** density" →
  "at every `ρ = S` of the fully polarised spin-`S` family"; "**forces**"
  → withdrawn entirely, not merely downgraded; the ⟨1⟩2.⟨3⟩1 leaf, whose
  r2 justification was three prose sentences, is restated as a hypothesis
  leaf citing D-numbers with the prose demoted to a load-free corroboration
  note (L6b).
* **(R3-d)** Checker third pass (r2-critic M3, m4, m5, n5): the acceptance
  band is **derived at run time from the data's own quoted error**
  (`0.0479`; there is no acceptance constant left in the file — §7.5); C2's
  ladder gate extended to a two-route cross-check and to every occupation
  `n ≤ 2S` (kills `cA_deepladder` at C2); the decorative momentum loop
  replaced by a real cross-momentum orthogonality gate (kills `cB_onek`);
  the `1**p − 1` non-gate demoted to a print; C5 and C7 labelled display;
  the new named computation **D24N-C8** added with its own red mode;
  r1's M3(c)(iii) declination **recorded, with its reason** (§7.6).
* **(R3-e)** Blast radius extended by r2-critic M4's three sites:
  `theory/verdicts/corpus-r2.md:174–178` (the ML5-B **promotion record**),
  `paper/main.tex:524–527`, `theory/verdicts/soft-index-r1.md:170`.
* **(R3-f)** DAG statuses repaired (r2-critic M5): `D24-VAL` becomes
  **PROVED (conditional implication; currently vacuous-or-unknown)**,
  matching the corpus convention that ML5-B and M-INDEX-spec already carry
  for the same logical shape; `CONJECTURE` moves to a new **AMP** row,
  which is where the open content actually lives; `where-tested` rewritten
  to name what the gates can test.

**Symbols of this round.**  Unchanged from r2 (`Z_ρ`, `𝔞_leg`, `E^O_desc`,
`L(k,h)`), except that `𝔞_leg` is now written **`𝔞_leg(ρ)`** — it is a
datum of the class `𝒮_W(ρ)` and the corpus asserts four different candidate
values at four densities (r2-critic m1).  `𝔞_leg` bare is retained as the
abbreviation inside a fixed-`ρ` display, registered as such.

---

## 1. The defect, and its root cause

### 1.1 The defect (unchanged; fenced twice)

The frozen clause 3 value `L(0,h) = −iχ/v_h` makes ML5-B (6)'s jet
identically `2χ`, with `∂_ρ[jet] = ∂_{v_h}[jet] = 0` (r1-critic V4, named
computation D24N-C1).  PROVED `S2-2body-S` gives jet `χ/S`, exactly, at
every `S` (r1-critic V5).  Under the corpus's jet-identification bridge
(H5; **not** a PROVED row) these collide except at `S = 1/2`, so the frozen
`𝒮_W` is provably empty in the spin-`S` ferromagnet register at every
`ρ ≠ 1/2` (r1-critic V7).  The frozen clause cannot stand.

### 1.2 Root cause — restated at its true strength

r1 said the root cause was that `L` is never defined.  r2 replaced that
with "the corpus's construction of `L` **forces** the frozen value, so the
density must live elsewhere".  Both are withdrawn.  The root cause has two
parts, and the second is the one r2 missed.

* **(i) A symbol-registry gap (narrow, real).**  There is no `notation.md`
  row for `L` and no `L :=` anywhere in `definitions.md`, `notation.md`,
  `claims/`, `theory/` or `paper/` (r1-critic F2; the pattern
  `L(k,h)|L(0,h)` also misses lane A's subscripted `L_λ` at
  `theory/soft-index.md:161–162`).  §5.4 repairs it.
* **(ii) A missing convention (the real defect, r2-critic F1).**  D24(b)
  calls `M_1^O` the "**amputated** one-hard amplitude" and `M_2^O` the
  "connected hard-plus-soft amplitude in the physical channel" and fixes
  **no amputation or leg-normalisation convention** anywhere in D24(a)–(e),
  `notation.md`, or `claims/CLAIMS.md`.  The wording is asymmetric — one
  amplitude is described as amputated, the other is not — and that
  asymmetry is exactly the unfixed degree of freedom.  A rescaling
  `M_1^O ↦ c M_1^O`, `M_2^O ↦ c' M_2^O` (and with it its D24(d)1 summand
  `E^O_desc ↦ c' E^O_desc`) sends `L ↦ (c'/c)L` and `𝔞_leg ↦ (c'/c)𝔞_leg`,
  while leaving clauses 1, 2, 4, 5 invariant.  So **before §5.0, every
  numerical statement about `𝔞_leg` — the frozen `1`, AMP's `1/Z_ρ`, and
  `D24-VAL`'s matched value alike — is a statement about a convention and
  not about a model.**  That is the r2-critic's F1 and it is correct.

The three corpus provenance sites for `L` — `soft-current-recon.md` ⟨1⟩7,
`paper/main.tex:524–527`, `soft-index-b.md:808` — construct the `1/v_h` as
the reciprocal LSZ energy denominator `[ω(h+k)−ω(h)]^{-1}k`.  What they fix
is the **`h`-profile** of `L(0,h)`, and, in the D6 register they are
written in (`ρ = 1/2`), its value.  They are `ρ = 1/2` statements
(r2-critic M2(b): `soft-current-recon.md` ⟨1⟩7 is a D6 shard;
`main.tex:524–527` sits inside Appendix B's spin-`1/2` discussion;
`soft-index-b.md:808` is a failed lane's D6 transplant), and they do not
determine `𝔞_leg` at any other density.  The word "forces" is struck from
this document.

### 1.3 Consequence for the shape of the repair

The repair is therefore three moves, in this order, and the third does not
make sense without the first:

1. **Fix the convention** (§5.0, §2 ⟨1⟩0).  Without it `𝔞_leg` is a name.
2. **Split clause 3** into the well-posed kinematic hypothesis (3a) and the
   normalisation statement (3b), whose content is the **`h`-profile**:
   `v_h L(0,h)/χ(h,0)` is independent of `h`.  Its value, `𝔞_leg(ρ)`, is
   then a determined datum of the class — determined whenever the class is
   nonempty, undefined when it is empty.
3. **Retire the value from `definitions.md`** (the r1 critic's third horn,
   F1(d′)).  The matching that would supply it quantifies over a class
   whose inhabitation is open at every `ρ` (§4.4), and
   `briefs/critic-protocol.md` §5 forbids relying on `𝒮_W` nonemptiness at
   `ρ ≠ 1/2` while `tns-iu5` is open.  What the matching does support is a
   conditional implication, carried as claim row `D24-VAL` (§5.3b), with
   both of its conditions displayed.

The price of move 3 is stated in full at §4.3 and H8: after it, no L4 file
asserts a value of `𝔞_leg` at **any** density, `ρ = 1/2` included, and
ML5-B's conclusion contains no number.

---

## 2. The adjudication (Lamport)

Nothing here is called a derivation of the value.  The proposition is
smaller than r1's "THEOREM D24N" and differently shaped from r2's: it now
opens with the convention, because without it steps ⟨1⟩2–⟨1⟩4 have no
subject matter.

**PROPOSITION D24N″ (repaired clause-3 architecture).**

**ASSUME.**  D24(a)–(b) **together with the amputation and leg-normalisation
convention displayed at §5.0**; D24(d) clauses 1 and 2 (with the descendant
external-leg term named `E^O_desc`); a broken-symmetry tail density
`ρ := ω_α(S^z) > 0` in the sense of `notation.md`'s `ρ`-row.  Where
`2ρ ∈ ℤ` is used, additionally (S) at both tails, D26(INT), **and the
antisymmetric tail pair `ω_β(S^z) = −ω_α(S^z) = −ρ`** (the load-bearing
hypothesis of PROVED `M-IDX-density`; r1-critic M4(ii)).

**PROVE.**

* **(i)** Clause (3a) as stated in §5.2 is well posed and nonvacuous.
* **(ii)** Under the §5.0 convention, `𝔞_leg(ρ) := i v_h L(0,h)/χ(h,0)` is
  invariant under every residual normalisation freedom D24(b) leaves open,
  and is a **determined datum** of `𝒮_W(ρ)` whenever that class is
  nonempty.  The membership content of clause (3b) is the **`h`-profile**
  statement — `v_h L(0,h)/χ(h,0)` does not depend on `h` — and not a value.
* **(iii)** *Conditionally* — given the jet-identification bridge — for
  **each** `S ∈ {1/2, 1, 3/2, 2}` at which `𝒮_W(ρ)|_{ρ=S}` is nonempty in the
  fully polarised spin-`S` register, `𝔞_leg(S) = 1/(2S)`; and within the
  one-parameter family `𝔞_leg = Z_ρ^{-p}` the exponent is `p = 1`.
* **(iv)** On the charge-created reading of `E^O_desc` — the reading the
  three corpus provenance sites display — conversion of the soft leg to the
  §5.0 convention supplies exactly `𝔞_leg = Z_ρ^{-1/2}`, which the
  ansatz-free data refutes at the **pre-registered** `0.08` band.  Hence
  AMP, if true, requires a second factor `Z_ρ^{-1/2}` from a mechanism that
  is not a leg normalisation.

### ⟨1⟩0.  The amputation and leg-normalisation convention, and what it buys

**⟨2⟩1. PROVE.**  With the §5.0 convention in force, `𝔞_leg` is invariant
under the residual freedom of D24(b), and the propositions "`𝔞_leg = 1`"
(frozen) and "`𝔞_leg = 1/Z_ρ`" (**AMP**) are statable and falsifiable.

**⟨3⟩1.  The freedom, exactly.**  D24(b) determines `M_1^O` and `M_2^O` only
up to normalisation.  Write a normalisation change as
`M_1^O ↦ c·M_1^O`, `M_2^O(k,·) ↦ c'(k)·M_2^O(k,·)`, with `c, c'(k) ≠ 0`
independent of `O` (D24(b) requires linearity in `O`, so a normalisation may
not depend on the source).  Clause 1 decomposes `M_2^O` into three summands,
so `E^O_desc ↦ c'(k)E^O_desc`; clause 2's residue is `2i v_h M_1^O(h)`, so
it transforms with `c`.  By the (3a) quotient,
`L(k,h) ↦ (c'(k)/c)·L(k,h)`, hence
`𝔞_leg ↦ (c'(0)/c)·𝔞_leg`.  Clauses 1, 2, 4 and 5 are invariant (each is a
homogeneous statement in one amplitude).
Justification: D24(b); D24(d)1–2; the (3a) quotient of ⟨1⟩1.

**⟨3⟩2.  Therefore, before §5.0, `𝔞_leg` is a name.**  `c'(0)/c` is an
arbitrary nonzero number and may be chosen `ρ`-dependent; so any prescribed
`𝔞_leg(ρ)` — `1`, `Z_ρ^{-1/2}`, `Z_ρ^{-1}` — is reachable by a convention
choice alone.  The r2 assertion that the density "can only live in `𝔞_leg`"
is therefore **withdrawn**: with `c'(0)/c` free, the density can be moved
between `L` and `𝔞_leg` at will, and the r2 argument for the contrary was a
consistency check of an assumed value, not a derivation.
Justification: ⟨3⟩1; r2-critic F1(b)(i)–(ii) — adopted in full.

**⟨3⟩3.  The convention (§5.0), stated here in the form used below.**  Both
amplitudes are matrix elements of `O` taken against `δ`-normalised
asymptotic magnon kernels in the corpus's own packet discipline — plane
waves admitted only as distributional kernels inside `C_c^∞` packets
(D3(a)), packets in `ℓ¹ ∩ BV` (D12(a′)), fixed-`k` statements quoted with
the `δ`-normalised plane wave (D12(b)).  The **same** hard-leg amputation is
applied in `M_1^O` and in `M_2^O`; the soft leg enters `M_2^O` as **one
additional `δ`-normalised asymptotic magnon of momentum `k`, with unit leg
weight** — not as a charge-created or current-created vector.  This fixes
`c'(0)/c = 1`.
Justification: D24(b) as amended at §5.0; D3(a); D12(a′); D12(b).

**⟨3⟩4.  Invariance of `𝔞_leg` under what remains.**  Three freedoms survive
§5.0 and none of them moves `𝔞_leg`.  (a) An overall rescaling of the source,
`O ↦ tO`: both amplitudes are linear in `O` (D24(b)), so the ratio is
unchanged.  (b) Any hard-leg amputation convention, provided it is the same
in both amplitudes: it enters `M_1^O` and `E^O_desc` identically and cancels
in the (3a) quotient.  (c) Any soft-leg weight `λ(k)` with `λ(0) = 1`
(for instance a packet-envelope convention): it multiplies `L(k,h)` by
`λ(k)` and leaves `L(0,h)` fixed.  A freedom with `λ(0) ≠ 1` is exactly what
§5.0 forbids.
Justification: ⟨3⟩1; D24(b) linearity; ⟨1⟩1's quotient.

**⟨3⟩5.  Therefore AMP is statable.**  `soft-index-r1.md` F1(c)(i) states
AMP as "charge-created soft-leg amputation contributes the per-site leg
density `Z_ρ` to the external flux", i.e. `𝔞_leg(ρ) = 1/Z_ρ`.  Under ⟨3⟩3
that is a proposition about a determined number (⟨1⟩2) and it has a truth
value: it is true at `ρ = 1/2` (⟨1⟩3, D6), and at `ρ ≠ 1/2` it is open.  It
is also **refutable**: ⟨1⟩4 exhibits a competing mechanism, computes its
prediction exactly, and refutes that prediction against data.  A prover can
now write down what is to be proved.
Justification: ⟨3⟩3–⟨3⟩4; `theory/verdicts/soft-index-r1.md` F1(c)(i).

**⟨3⟩6.  What ⟨1⟩0 does NOT establish.**  §5.0 is a **choice**, not a
theorem.  It is the choice under which the D24 amplitudes are normalised
like the asymptotic amplitudes of D25's soft multiplier `𝖲`, so that the
jet-identification bridge (α) compares two objects in one normalisation.
Any other admissible choice rescales `𝔞_leg` by a known constant, and the
statements below transform with it.  In particular a convention chosen so
that the D24 ratio *is by definition* the physical soft factor would make
`D24-VAL` a tautology; §5.0 deliberately does not do that — it fixes the
soft leg by the state normalisation (D12(b)), independently of any soft
factor, which is why (α) remains a substantive hypothesis and ⟨1⟩4's
refutation has content.
Justification: ⟨3⟩1; D25; H5.

**⟨3⟩7. QED.**

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
the domain may have holes.  Both restrictions are therefore part of the
displayed hypothesis, and `L(0,h)` names an extension value, never a
quotient value.
Justification: D24(d)1–2; r1-critic F1(b)(i), M7 — adopted; fenced verbatim
by r2-critic W10.

**⟨3⟩2.**  Nonvacuity: with `L` so defined, "process independent" is the
substantive requirement that the extension agree across all `O` in the
class — a real constraint, not a tautology.
Justification: r1-critic V8 (checked directly by the r1 critic).

**⟨3⟩3. QED.**  This step is unchanged from r2 and was fenced by the r2
critic as "the best thing in the round" (W10); it is reproduced, not
re-argued.

### ⟨1⟩2.  What clause (3b) says: an `h`-profile, and a determined number

**⟨2⟩1. PROVE.**  Under §5.0, `𝔞_leg(ρ) := i v_h L(0,h)/χ(h,0)` is a
determined datum of `𝒮_W(ρ)` whenever that class is nonempty, and the
membership content of (3b) is that `𝔞_leg` does not depend on `h`.

**⟨3⟩1.  The split is a factorisation, not a choice of home.**  Fix `ρ` and
suppose `O ∈ 𝒮_W(ρ)` with `M_1^O ≠ 0`.  By ⟨1⟩1, `L` is *determined* by
`E^O_desc`, `v_h` and `M_1^O` — all three are D24(b)/D24(d)1–2 objects, and
by §5.0 all three are normalised.  Write `L(0,h) = 𝔞_leg·(−iχ(h,0)/v_h)`;
this is a definition of `𝔞_leg` by division, legitimate because `v_h > 0` on
`I` and `χ(h,0) = ±1`.  Nothing is being placed anywhere: `𝔞_leg` is the
value of the determined quantity `i v_h L(0,h)/χ(h,0)`.
Justification: ⟨1⟩1 (D24N.3′); §5.0 (⟨1⟩0.⟨3⟩3); `v_h` bounded below on `I`
by r1-critic V9; `notation.md`'s `χ(h,k)` row (l.261).

**⟨3⟩2.  Therefore (3b)'s only membership content is the `h`-profile.**  The
displayed clause asserts that the determined quantity of ⟨3⟩1 is
**independent of `h`** on `I` — equivalently that `L(0,h)` has exactly the
reciprocal-velocity profile `1/v_h` times the channel sign.  It asserts no
value.  `k`-independence is not an extra condition (`𝔞_leg` is defined at
`k = 0`), and `O`-independence already follows from (3a)'s
process-independence hypothesis, so the `h`-profile is the whole of it.
This is a property of the **class**, not of an individual source: no single
`O` can satisfy or fail (3b) on its own.
Justification: ⟨3⟩1; D24(d)3a; r2-critic m3 — adopted in full.

**⟨3⟩3.  What the corpus's provenance sites do and do not supply.**  The
three sites construct the `1/v_h` as the reciprocal LSZ energy denominator
`[ω(h+k)−ω(h)]^{-1}k`.  That is a statement about the **`h`-profile**, and
it is exactly ⟨3⟩2's content; it is corroboration for (3b) as a membership
condition.  It is **not** a determination of `𝔞_leg`, because all three
sites are written in the D6 register `ρ = 1/2`
(`soft-current-recon.md` ⟨1⟩7 is a D6 shard; `paper/main.tex:524–527` sits
inside Appendix B's spin-`1/2` discussion; `soft-index-b.md:808` is a failed
lane's D6 transplant).  Off `ρ = 1/2` they say nothing about the value.
Justification: r2-critic M2(b) — adopted; the three sites re-read this
round.  *(Corroboration note, carrying no load: the same three sentences are
the source of the frozen clause's implicit `𝔞_leg = 1`; ⟨1⟩4 identifies why
that reading is `ρ = 1/2`-specific.)*

**⟨3⟩4.  The density is not internal to clauses 2 and 3's kinematics — in
the fully polarised spin-`S` family.**  On the spin-`S` tail
`ω_S(k) = 2JS(1−\cos k)`, so `v_h = Z_ρ J\sin h` carries one power of
`Z_ρ`; the Ward residue carries the same power,
`⟨h|Q_0^†J^-_0|h⟩ = 2i v_S(h) = Z_ρ·2iJ\sin h`, exactly at `2S = 1,2,3,4`;
and in the product `(e^{ik}−1)·(−iχ/v_h)·[2i v_h M_1^O]` the two powers
cancel exactly, giving `2iχ k M_1^O` with `∂_ρ = ∂_{v_h} = 0`.  So in that
family a density dependence in `𝔞_leg` is not produced by the residue and
the reciprocal-velocity profile: it must come from the soft-leg
normalisation (⟨1⟩4) or from a mechanism beyond it.  **This is asserted for
`ρ = S` in the fully polarised spin-`S` family only** — the one register in
which the corpus computes — and not for the free real `ρ` of
`notation.md:270`.
Justification: r1-critic V2, V3, V4; named computations D24N-C1 and D24N-C3
in `theory/checks/d24d3_normalization_check.py`; quantifier scoped per
r2-critic M2(c).

**⟨3⟩5.  `𝔞_leg` is a partial datum.**  If `𝒮_W(ρ) = ∅` there is no
`E^O_desc` and `𝔞_leg(ρ)` is undefined, not free.  So "the value of
`𝔞_leg`" presupposes nonemptiness, which is open at every `ρ` (§4.4).  This
is the same fact that makes `D24-VAL` vacuous-or-unknown, seen at the level
of the symbol.
Justification: ⟨3⟩1; §4.4; bd `tns-axg`.

**⟨3⟩6. QED.**

### ⟨1⟩3.  The conditional matching (the content of claim `D24-VAL`)

**⟨2⟩1. ASSUME.**  (α) the jet-identification bridge — the jet of the
D24(d) soft multiplier equals the jet of the two-body physical phase
(corpus identification via `soft-current-recon.md` (R17) and
`oracle-bethe.md` O9; **NOT** a PROVED row — H5); (β) for a given
`S ∈ {1/2, 1, 3/2, 2}`, a member `O ∈ 𝒮_W(ρ)|_{ρ=S}` exists in the fully polarised
spin-`S` register `H_S = −JΣ_x(S_x·S_{x+1} − S²)` with `M_1^O ≠ 0`.

**PROVE.**  `𝔞_leg(S) = 1/(2S)`, **for each such `S` separately** (r2-critic
n1: (β) is an existence hypothesis per `S`, and the conclusion is drawn per
`S`; nothing here is a single universal statement over the four values).

**⟨3⟩1.**  By (β), ⟨1⟩1–⟨1⟩2 and §5.0, the ML5-B multiplier of that member
is `𝖲(k;h) = (e^{ik}−1)·𝔞_leg·(−iχ/v_h)·2i v_h = 2iχ 𝔞_leg k + O(k²)`.
Justification: ML5-B (6); ⟨1⟩2.⟨3⟩1; r2-critic W7 (arithmetic verified).

**⟨3⟩2.**  By (α), and because §5.0 normalises the D24 amplitudes like the
asymptotic amplitudes the physical phase is defined from (⟨1⟩0.⟨3⟩6), the
same jet equals the PROVED two-body physical jet `i(χ/S)k` of
`S2-2body-S` (T.3) with `ρ = S`.  Equating coefficients: `2𝔞_leg = 1/S`,
i.e. `𝔞_leg = 1/(2S) = 1/Z_ρ`.
Justification: `S2-2body-S` (PROVED; slope `i/S` exact, r1-critic V5);
assumption (α); ⟨1⟩0.⟨3⟩3.

**⟨3⟩3.**  Exponent uniqueness, at its true strength: within the family
`𝔞_leg = Z_ρ^{-p}`, the exact law `2(2S)^{-p} = 1/S`, i.e. `(2S)^p = 2S`,
forces `p = 1` at **any single** `S` with `2S ≠ 1`; the `S = 1/2` point is
degenerate (`1^p = 1` for every `p`) and contributes nothing.  So the
exponent is pinned by one non-degenerate density, and the four densities
are four points of one analytic curve from one PROVED theorem — not four
independent measurements.  The numerical fit to the ansatz-free data is
corroboration, not the pin.
Justification: symbolic solve, named computation D24N-C6; r1-critic m4.

**⟨3⟩4. QED — and the status boundary.**  ⟨3⟩1–⟨3⟩3 prove a *conditional
implication*: for each `S`, `(α) ∧ (β_S) ⇒ 𝔞_leg(S) = 1/(2S)`.  The
implication is a theorem; its antecedents are not.  If (β_S) fails at every
`S` (possible: §4.4) the implication is vacuous and fixes nothing; if (α)
fails, it has no contact with any PROVED row.  Therefore the value is
**not** installed in `definitions.md`; it is carried as claim `D24-VAL`
(§5.3b), whose status is **PROVED as an implication, currently
vacuous-or-unknown** (r2-critic M5(c)(i) — adopted), with the open content
moved to the separate `AMP` row (CONJECTURE).  This complies with binding
`soft-index-adjudication-r1.md` §3.2 — the value is taken from on-shell
input, conditional on a named and displayed matching hypothesis (§4.5).

### ⟨1⟩4.  The one proposed mechanism, computed and refuted (NEW)

**⟨2⟩1. PROVE.**  On the charge-created reading of `E^O_desc`, conversion of
the soft leg to §5.0's normalisation supplies exactly `𝔞_leg = Z_ρ^{-1/2}`;
that prediction is refuted by the ansatz-free data at the pre-registered
band; hence AMP's residual content is a second factor `Z_ρ^{-1/2}` from a
non-leg-normalisation mechanism.

**⟨3⟩1.  The conversion factor is exactly `√Z_ρ`.**  On the fully polarised
spin-`S` tail, `S^-_x|Ω⟩ = √(2S)\,|x⟩` with `|x⟩` the normalised one-flip
state, so

    Q^-_k|Ω⟩ = Σ_x e^{ikx} S^-_x|Ω⟩ = √(Z_ρ) · Σ_x e^{ikx}|x⟩ ,

and `Σ_x e^{ikx}|x⟩` is the `δ`-normalised asymptotic magnon of D12(b) — it
is an exact eigenvector of `H_S` in the one-magnon sector with eigenvalue
`ω_S(k) = 2JS(1−\cos k)`.  The identity is exact, `k`-independent, and
`N`-free per site.
Justification: named computation **D24N-C8** (one-magnon block of `H_S` on a
ring diagonalised from the raw bond matrix; eigenvalue and overlap
reproduced to machine precision at `2S = 1,2,3,4`); r1-critic V1, V2.

**⟨3⟩2.  What the three provenance sites compute.**  They display
`⟨k_h|Q_0^†J^-_0|k_h⟩ = 2i v_h` and divide by the energy shift `v_h k_s`
(`paper/main.tex:524–527`; `soft-current-recon.md` ⟨1⟩7;
`soft-index-b.md:808`).  The soft leg there is the **charge insertion**, not
a `δ`-normalised asymptotic magnon.  This is a reading of those sites, and
it is the reading their own notation displays.
Justification: the three sites, quoted; `main.tex:524–527` verbatim.

**⟨3⟩3.  Therefore leg conversion alone predicts `Z_ρ^{-1/2}`.**  Under
⟨3⟩2's reading the frozen computation delivers `𝔞_leg^{Ward} = 1`
(density-blind, D24N-C1).  By ⟨3⟩1 the convention's soft leg is `Q^-_k|Ω⟩`
divided by `√Z_ρ`, so `M_2^O` in §5.0's normalisation is the Ward one
divided by `√Z_ρ`, giving `𝔞_leg = Z_ρ^{-1/2}`.  At `ρ = 1/2`, `Z_ρ = 1`
and the two conventions coincide exactly — which is why the D6 corpus is
internally consistent and why the frozen clause is right there and only
there.
Justification: ⟨3⟩1–⟨3⟩2; ⟨1⟩0.⟨3⟩1; named computation D24N-C1.

**⟨3⟩4.  The half-power prediction is refuted, and not by a post-hoc band.**
Against the ansatz-free `A_ring_summary` extrapolations, `Z_ρ^{-1/2}` gives
relative deviations `0.0004 / 0.4158 / 0.7347 / 1.0033` at
`S = 1/2, 1, 3/2, 2` — a 5–12× margin against the **pre-registered** `0.08`
decision band, and a `≥ 8×` margin against the data's own worst quoted
extrapolation error (`0.048`).  The refutation needs no acceptance band at
all.  Its one hypothesis is the bridge (α): it compares a D24 prediction
with the two-magnon phase data, which is exactly what (α) licenses.  Without
(α), nothing here is refuted and nothing is matched.
Justification: named computation D24N-C6 red mode `--red-halfpower`
(§7.1); the data's `error` column (§7.5); H5.

**⟨3⟩5.  Consequence for AMP.**  `1/Z_ρ = Z_ρ^{-1/2}·Z_ρ^{-1/2}`.  Leg
conversion supplies the first factor exactly.  AMP is therefore true iff a
second factor `Z_ρ^{-1/2}` arises from something that is **not** a leg
normalisation.  This strengthens r2's negative statement ("whatever
mechanism AMP names, it is not a leg normalisation") from a rebuttal into a
quantitative accounting: the missing mechanism is not of unknown size, it is
of exactly the size already computed.  It also fences the next prover: any
proposed AMP mechanism must be checked against ⟨3⟩1, or it will
double-count the leg.
Justification: ⟨3⟩1–⟨3⟩4; r2-critic W17 (the `√Z_ρ` arithmetic of r2's
⟨1⟩4.⟨2⟩3, fenced).

**⟨3⟩6.  Honest fence on ⟨1⟩4.**  This step does **not** prove AMP, does not
refute it, and does not exhibit a class member.  It converts one open
question into one sharper open question and kills one candidate answer.  In
particular it does not license writing `Z_ρ^{-1/2}` anywhere as a value:
under (α) that value is refuted, and without (α) it is unfalsified only
because nothing is falsifiable.

**⟨3⟩7. QED.**

### ⟨1⟩5.  Demotions and corrections (consistency material, carrying no load)

**⟨2⟩1.  The residue's `Z_ρ`-linearity is a consistency check of clause 2,
not the load-bearing step.**  `⟨h|Q_0^†J^-_0|h⟩ = 2i v_S(h)` is an identity
once the dispersion is known; D24(d)2's `2i v_h` is correct at every `Z_ρ`.
r1's "this is the load-bearing step" and "that single cancellation is the
entire defect" are struck.  What D24N-C3 certifies is that clause 2 needs no
repair.
Justification: r1-critic M2, V3 — adopted; r2-critic W17.

**⟨2⟩2.  What the S1 lanes actually said (r1's ⟨1⟩5 strawman withdrawn).**
Lane B's operative factor (`soft-index-b.md:802–811`, B14 bullet 2) is the
per-volume leg density `1/Z_ρ` — `N`-free, the same invariant used here.
Lane A asserted `L_λ(0,h) = −i\,sgn(v_h−v_s)/(2ρ_λ v_h)` directly
(`soft-index.md:161–162`).  The `(2ρN)^{-1/2}` route r1 refuted was the
**S1-A critic's counter-analysis** (`soft-index-r1.md` F1(b)4), not either
lane's claim; it is `N`-dependent and separately refuted (D24N-C7, display).
Neither lane derived the factor; neither does this adjudication; lane B's
*bookkeeping* is the one adopted, now as the named open lemma AMP with the
quantitative fence of ⟨1⟩4.
Justification: r1-critic M1 — adopted; r2-critic W17.

**⟨2⟩3.  Watanabe–Murayama fixes the invariant, not the factor 2.**  The
type-B symplectic density `ρ_{ij} = −i⟨0|[Q_i, j^0_j]|0⟩` identifies `Z_ρ`
(in the complexified basis) as the natural per-site density of the broken
pair — "consistent with", not "exactly" the AMP factor: WM's own
normalisation is `m = ρ`, not `2ρ`.  The factor of 2 is fixed only by the
matching of ⟨1⟩3.
Justification: r1-critic m5, V10 — adopted; L3 quotation fenced.

**⟨2⟩4. QED.**

---

## 3. Acceptance check

The acceptance arithmetic certifies claim `D24-VAL` (the conditional matched
value) and refutes two candidates.  It certifies **no definitional clause**.
Predicted jet `2·𝔞_leg`, `ρ = S`, against the ansatz-free `A_ring_summary`
extrapolations (unchanged data; fenced as r1-critic V6/V14):

| `S = ρ` | measured (ansatz-free) | `1/S` | frozen `𝔞_leg = 1` | leg-conversion `𝔞_leg = Z_ρ^{-1/2}` (⟨1⟩4) | matched `𝔞_leg = Z_ρ^{-1}` |
|---|---|---|---|---|---|
| 1/2 | 1.9991 | 2.0000 | 0.000 ✅ | 0.000 ✅ | 0.000 ✅ |
| 1   | 0.9984 | 1.0000 | 1.002 ❌ | 0.416 ❌ | 0.002 ✅ |
| 3/2 | 0.6649 | 0.6667 | 2.003 ❌ | 0.735 ❌ | 0.003 ✅ |
| 2   | 0.4983 | 0.5000 | 3.003 ❌ | 1.003 ❌ | 0.003 ✅ |

(Deviations are `|predicted − measured|·S`, the checker's units.)

* reproduces `1/S` at `S ∈ {1/2,1,3/2,2}` — ✅ (D24N-C6; **the acceptance
  band is derived at runtime from the data's own quoted extrapolation error,
  `max_rows |error|·S = 0.0479`; there is no hand-chosen band in the file**).
* refutes the frozen `𝔞_leg = 1` off `ρ = 1/2` — ✅, at the **pre-registered**
  `0.08` band, margin 12–37×.
* refutes the leg-conversion prediction `Z_ρ^{-1/2}` off `ρ = 1/2` — ✅, at
  the **pre-registered** band, margin 5–12× (⟨1⟩4.⟨3⟩4).  This is new this
  round and is the round's one substantive addition to the evidence.
* leaves clauses 1, 2, 4, 5 intact — ✅.  **D24(c) must move in lockstep**
  (§4.1 B2), parametrically in `𝔞_leg` rather than in `ρ`.

**What the certificate does NOT show.**  The two anchor conditions are not
independent (`ρ = 1/2` *is* the `S = 1/2` member), and the four densities are
four points of one analytic curve (⟨1⟩3.⟨3⟩3), not four independent
measurements.  Nothing in the certificate bears on `L`, `E^O_desc`, or class
membership; the acceptance comparison is the C4 comparison at a tighter band
with mean rather than per-row aggregation, and its genuine gain is resolving
power on the exponent — `p ∈ [0.969, 1.037]` at the derived band versus
`[0.947, 1.062]` at the pre-registered one (§7.4).  The r2 claim that C6 is
"independent of C4" is **struck** (r2-critic M3(b)(i)–(ii), adopted).

---

## 4. Blast radius

Every address below was obtained by grep this round.  The r1 list is retained
where the r1 critic verified it (V12, V13); the r2 list is retained where the
r2 critic verified it **complete** (W12 `ml5-universality.md`, W13
`TRIANGLE.md`, W14 `ml4_check.py`/D24(e), W16 `notation.md`/paper) — those
files are **not churned this round**.  The three sites the r2 critic found
missing (M4) are added.

### 4.1 Text that MUST change (merge proposals in §5)

| # | Address | What changes | Why |
|---|---|---|---|
| B0 | `definitions.md:923–929` — D24(b) | **NEW this round.**  Append the amputation and leg-normalisation convention as displayed text | r2-critic F1: without it `𝔞_leg` is a name, AMP is unstatable, and B1's (3b) has no subject |
| B1 | `definitions.md:952–973` — D24(d) | preamble `𝒮_W → 𝒮_W(ρ)`, `ρ > 0` fence, `Z_ρ` in state language, ANTISYMMETRY in the `M-IDX-density` citation; clause 1 summand named `E^O_desc`; clause 3 split into (3a) hypothesis and (3b) `h`-profile with `𝔞_leg(ρ)` OPEN | the referral; r1 F1/F3/M4/M7; r2-critic F1, M1, m1, m3 |
| B2 | `definitions.md:931–950` — D24(c) | `2iχ M_1^O → 2i𝔞_leg χ M_1^O` in `𝔠_h`, in the ML5-A criterion display, and in the `K_O` bound; **strike** the false clause about D24(e)/`ml4_check.py` | lockstep (r2-critic W15 verified all three displays are covered); r2-critic M1(b)(iii) |
| B3 | `claims/CLAIMS.md:41` — ML5-B | status stays **PROVED**; conclusion `2i𝔞_leg χ k M_1^O`; the "at `ρ = 1/2` (`𝔞_leg = 1`)" parenthetical **struck**; where-proved annotated with the `corpus-r2.md` reparametrisation pointer | r2-critic M1(b)(ii), M4 row 1 |
| B4 | `claims/CLAIMS.md` — NEW row **D24-VAL** | the conditional matched value, **PROVED as an implication, currently vacuous-or-unknown**; where-tested rewritten | r2-critic M5 |
| B5 | `claims/CLAIMS.md` — NEW row **AMP** | the open lemma `𝔞_leg(ρ) = 1/Z_ρ`, CONJECTURE, with ⟨1⟩4's fence | r2-critic M5(c)(i) ("move CONJECTURE to the AMP lemma"); §8 needs a DAG home for the prover target |
| B6 | `claims/CLAIMS.md:40` — ML5-A | add the constant-agnostic sentence; **strike** "the form in which D24(e) and `ml4_check.py` test it" | r1 B6; r2-critic M1(b)(iii) |
| B7 | `notation.md` — rows | NEW `L(k,h)`, `Z_ρ`, `𝔞_leg(ρ)`, `E^O_desc`; `𝒮_W` row (l.258) → `𝒮_W(ρ)`; `𝖲` row (l.244) cross-reference; overload rule 2 amendment; **overload rule 8 amendment** for `E^O_desc`; **new overload rule for `𝔞`** | r1 F2 (narrow), F3(c), M6; r2-critic m1, m2 |

### 4.2 Shard steps to re-typeset in lockstep (not this lane's files)

**Verified COMPLETE by the r2 critic and reproduced here by reference — do
not re-grep:**

`theory/ml5-universality.md` (W12): ⟨1⟩2 eqs. (3), (4), (4b); ⟨1⟩3 hypothesis
3 (ll.142–144); ⟨1⟩3 eq. (5) boxed (l.155); l.158 (the "two-site" Wigner
sentence → "signed `2𝔞_leg`-site; `two-site` is the `𝔞_leg = 1`, `ρ = 1/2`
register"); ⟨1⟩3 ⟨2⟩1.⟨3⟩2 (ll.170–172, needs only `𝔞_leg ≠ 0` and `v_h`
bounded below — r1-critic V9); ⟨1⟩3 ⟨2⟩3 (ll.183–184); ⟨1⟩6 item 3
(ll.324–327); shard-header ERRATUM pointer.  Line 164 and line 190 do not
move (W12).

`theory/TRIANGLE.md:24, 215, 254, 257, 528` — `𝒮_W → 𝒮_W(ρ)` cross-reference
refresh only; no constant displayed (W13).

**ADDED THIS ROUND (r2-critic M4), and the first is the serious one:**

| Site | Verbatim | Disposition |
|---|---|---|
| `theory/verdicts/corpus-r2.md:174–178` | "**ML5-B.** Multiplying `(e^{ik}-1)[-i chi/v_h][2iv_hM_1]` gives `2i chi kM_1+O(k^2)`. … This is a valid conditional implication" | This is the **promotion record** that made ML5-B PROVED, and it verifies the `𝔞_leg = 1` arithmetic.  It is a promotion record, not a failed-lane record, so it gets an **annotation**, not an erratum-and-forget: append "*(bd `tns-iu5` r3: the same multiplication with the D24(d)3b constant carried gives `2i𝔞_leg χ k M_1 + O(k²)`; `𝔞_leg` enters as a nonzero constant factor and no step of this adjudication uses its value, so the implication certified here survives verbatim under reparametrisation.  Its displayed conclusion in `claims/CLAIMS.md` is updated accordingly; the promotion is not reopened.)*"  §5.5 item 5. |
| `paper/main.tex:524–527` | "`\braket{k_h\|Q_0^\dagger J^-_0\|k_h}=2\ic v_h`; dividing a hard external-leg reduction by the energy shift `v_h k_s` cancels the velocity and leaves the `$2$`." | One-clause scoping edit: "…leaves the `$2$` in this spin-$1/2$ register, where the charge-created soft leg and the asymptotic soft leg coincide; in the general class the same division leaves `$2\mathfrak{a}_{\mathrm{leg}}$` (D24(d)3b)."  §5.5 item 6.  This is also the sentence ⟨1⟩4.⟨3⟩2 reads as the charge-created convention, so the edit and the step must ship together. |
| `theory/verdicts/soft-index-r1.md:170` | "D24(d)3 + ML5-B(6) give, for **every** model in the class, `M_2 = 2iχ k M_1 + O(k²)`, i.e. phase slope `2χ`" | Failed-lane verdict record: ERRATUM pointer only, added to §5.5.2's list beside `soft-index.md` and `soft-index-b.md` (r2-critic m8). |

**Failed-lane records:** `theory/soft-index.md:161–162` and
`theory/soft-index-b.md:757–758, 808` display flux/leg-density text the
merged D24(d) supersedes.  ERRATUM pointer at each shard head, not an edit
of their content.

### 4.3 Text that does NOT change — and the price of that

r1's §4.3 list was verified item by item (r1-critic V12) and is retained by
reference: `oracle-bethe.md` O7/O8/O9, `soft-current-recon.md`
(R14)/(R17)/(R18), `paper/main.tex:208, 244–252`, `main.tex:542–546`,
D24(a),(d)1,2,4,5, (e), D25, `ml4_check.py`, `spin_s_slope_check.py`, the
results JSONs, and the CLAIMS rows ML5, S2-2body, S2-2body-S, M-IDX-density,
Bc, S-general.  D24(b) now *does* change (B0), so the r2 statement that
"D24(a),(b)" are untouched is **corrected**.

**The consequence r2 never drew (r2-critic M1(b)(ii)), stated plainly.**
After this merge **no L4 file asserts a value of `𝔞_leg` at any density,
`ρ = 1/2` included.**  Therefore:

1. **ML5-B (PROVED) predicts no number at any density.**  Its conclusion is
   `M_2^O(k,h) = 2i𝔞_leg χ k M_1^O(h) + O_{L²(I)}(k²)` — a factorisation
   **shape** (linear in `k`, proportional to `M_1^O`, with a class constant),
   not a value.  Its *status* is unaffected, because the number was never a
   consequence of ML5-B: it was a consequence of ML5-B **plus** the frozen
   clause 3's stipulation, and that stipulation is what is being retired.
   §5.3a says this in the row.
2. **Every corpus display of the soft coefficient `2` that traced to
   `D24(d)3` loses that justification and is re-sourced.**  None becomes
   false: they are independently derived from the contact/oracle route —
   `paper/main.tex:515–520` solves the two-body contact equation directly
   for a `k_s`-coefficient `2i` with all hard dependence cancelling, and
   `oracle-bethe.md` O7–O9 is the same statement in the oracle's language.
   That route does not use D24(d) at all.  The sites are:
   `paper/main.tex:249` (`𝖲 = 2ik_s`), `:524–527` (Appendix B's Ward
   reading — the one that needs the scoping edit of §4.2),
   `soft-current-recon.md:361–363`, `oracle-bethe.md:351` and O9 (l.470),
   `ml5-universality.md` 155/158/183–184/326.
3. **The Letter is unaffected in substance** but its warrant moves: Theorem
   `thm:soft` and `main.tex:249` stand on the contact route, and
   `main.tex:542–546` renders clause 3 with no displayed value (r2-critic
   W16), so it stays correct as written.  `main.tex:244`'s "five-condition"
   count survives the split (r1-critic V13).
4. **This is a real loss of reach and is recorded as one.**  Before the
   merge, D24(d) + ML5-B produced a number on the class (the wrong number
   off `ρ = 1/2`, but a number).  After it, they produce a shape.  The number
   returns only when AMP closes or a class member is exhibited (§4.4).  The
   Letter loses nothing because it never rested on D24(d) for the constant;
   the *programme* loses a derivation it did not have.

### 4.4 Is `𝒮_W(ρ)` nonempty after the repair?

**No — nonemptiness remains OPEN at every `ρ`, `ρ = 1/2` included** (r1 §4.4;
concurred by the r1 critic §8 and the r2 critic §8; retained in substance).

* *Before*: given the bridge, provably empty off `ρ = 1/2` (r1-critic V7).
* *After*: that proof of emptiness is gone — with `𝔞_leg` open the class
  predicts jet `2χ𝔞_leg` and no PROVED row refutes membership — but no
  source satisfying clauses 1, 4, 5 is exhibited at any density.
* **Coupling:** `tns-axg` and `tns-iu5` are coupled.  `D24-VAL` is a theorem
  but stays **vacuous-or-unknown** until `tns-axg` produces a member; `AMP`
  stays CONJECTURE until the second `Z_ρ^{-1/2}` of ⟨1⟩4.⟨3⟩5 is supplied or
  refuted.  `tns-iu5` is **re-scoped on merge, not closed** (§8).

### 4.5 Compliance with the binding soft-index adjudication

* **§3.2 (value-fixing by hypothesis is DEAD; value from on-shell input,
  conditional on a named, displayed matching hypothesis).**  Complied with:
  the value is taken from on-shell input (`S2-2body-S`), the matching
  hypothesis is named and displayed as `D24-VAL`'s two conditions, and it is
  kept out of the definition entirely.  No layer says "derived".
* **§3.5 (the fully polarised register `M = ρN − n` was struck for
  presupposing `ρ = S ∈ ½ℤ`).**  Complied with: the merged D24(d) contains no
  fully-polarised-vacuum object; `Z_ρ := 2ρ` is defined from `notation.md`'s
  `ρ`-row (a GNS/state datum), with the su(2) fully polarised reading marked
  a special case.  The fully polarised register appears only inside the
  *conditional* row and inside ⟨1⟩4, both explicitly scoped (r1-critic M5(d);
  r2-critic W11 — the `ρ`-vs-`s` fence is not breached).
* **New this round:** ⟨1⟩0.⟨3⟩6 records that §5.0 is a **choice** and names
  the alternative it deliberately refuses (a convention under which the D24
  ratio is by definition the physical soft factor, which would make
  `D24-VAL` a tautology).  That is the §3.2 discipline applied to a
  convention rather than to a value.

---

## 5. MERGE PROPOSALS

*This lane edited no shared file.  The orchestrator applies §5.0–§5.5 as
**one commit**: §5.1's `𝔞_leg` and §5.2's clause 3b are meaningless without
§5.0's convention, and §5.3's rows quote both.  A partial application is
**not** offered.*

**Mechanics.**  All three `definitions.md` spans are REPLACEments of adjacent
blocks, so apply them in **descending line order** — §5.2 (952–973), then
§5.1 (931–950), then §5.0 (923–929) — or match on the quoted first and last
lines.  Anchors re-verified this round against the current files:
`definitions.md:923` begins `**(b) Amputated amplitudes.**`, the (b) span
ends at `929` (`waves are generalised kernels inside \`C_c^∞\` packets
(D3(a), D12(a′)).`); `:931` begins `**(c) The contact first jet.**`, the (c)
span ends at `950` (`factorisation with the same stated norm control.`);
`:952` begins `**(d) The Ward-covariant no-contact class`, the (d) span ends
at `973` (`is part of the ML5-B future work.`).  `claims/CLAIMS.md` ML5-A is
line 40, ML5-B line 41.  `notation.md`: `𝒮_W` row `= 258`, `𝖲` row `= 244`,
`χ(h,k)` row `= 261`, overload rule 2 at `91–98`, rule 8 at `123–130`,
rule 9 at `131–134`, `𝔞_α` row at `55`.

### 5.0 `definitions.md` — D24(b), lines 923–929  (NEW; r2-critic F1)

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
D12(a′); the fixed-`k` reading of D12(b)).  The **same** amputation is
applied to the **same** hard leg in both.  The soft leg enters `M_2^O` as
**one additional `δ`-normalised asymptotic magnon of momentum `k`, carrying
unit leg weight** — not as a charge-created or current-created vector.

This is a *convention*, not a theorem, and it is load-bearing.  A change of
normalisation `M_1^O ↦ c\,M_1^O`, `M_2^O(k,·) ↦ c′(k)\,M_2^O(k,·)` with
`c, c′(k) ≠ 0` (necessarily independent of `O`, by linearity above) leaves
clauses (d)1, 2, 4, 5 invariant, while the (d)3a external flux factor and
the (d)3b amputation constant transform as
`L(k,h) ↦ (c′(k)/c)L(k,h)` and `𝔞_leg ↦ (c′(0)/c)\,𝔞_leg`.  Fixing
`c′(0)/c = 1` as above is exactly what makes `𝔞_leg` a number rather than a
name: without it, "`𝔞_leg = 1`" and "`𝔞_leg = 1/Z_ρ`" are statements about a
convention and not about a model.  What remains free does not move `𝔞_leg`:
rescaling the source (both amplitudes are linear in `O`); any hard-leg
amputation convention applied identically in both (it cancels in the (d)3a
quotient); and any soft-leg envelope `λ(k)` with `λ(0) = 1`.

Two consequences are recorded because they are used below.  (i) In the fully
polarised spin-`S` ferromagnet the **charge-created** soft leg is *not* this
convention's soft leg: `S^-_x|Ω⟩ = √(Z_ρ)\,|x⟩` on normalised one-flip
states, hence `Q^-_k|Ω⟩ = √(Z_ρ)\,|k⟩` exactly, the two coinciding only at
`ρ = 1/2` (named computation D24N-C8 in
`theory/checks/d24d3_normalization_check.py`, verified against the
Hamiltonian's own one-magnon eigenvector).  (ii) Consequently a soft-leg
normalisation argument alone contributes `Z_ρ^{-1/2}` to `𝔞_leg`, not
`Z_ρ^{-1}`; see the fence on lemma AMP in (d)3b.
```

### 5.1 `definitions.md` — D24(c), lines 931–950

**REPLACE** (from `**(c) The contact first jet.**` through
`factorisation with the same stated norm control.`):

```
**(c) The contact first jet.**  With `χ(h,k) := sgn(v(h) − v(k))` and
`𝔞_leg` the soft-leg amputation constant of (d)3b below (the forward
reference is deliberate: `𝔠_h` is by definition the obstruction to the
factorisation (d) predicts),

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
value of `𝔞_leg` (`𝔞_leg ≠ 0` suffices).  The counterexamples of (e) are
likewise `𝔞_leg`-blind: both have `M_1^O = 0`, so the `𝔞_leg`-dependent term
vanishes identically for every `𝔞_leg`, and neither (e) nor
`theory/checks/ml4_check.py` needs an edit (bd `tns-iu5`).
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
polarised spin-`S` ferromagnet `ρ = S`.  All amplitudes below are in the
normalisation convention of (b); clause 3b is empty without it.  `𝒮_W(ρ)` is
the class of sources satisfying all five of (clause 3 has two parts; the
*count* of conditions is deliberately unchanged, so `paper/main.tex:244`
"five-condition" and the audit rows that quote it stay correct):
1. *Exhaustive normed LSZ decomposition* — in `L²(I)`, `M_2^O` is exactly
   the sum of the descendant external-leg term `E^O_desc`, the
   orthogonal-current term, and the direct source/contact term named below;
   there is no additional reduced term, and the equality holds in the same
   packet norm as (b).
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
   **(3b) the profile of `L(0,h)`, and the OPEN amputation constant** —
   `v_h\,L(0,h)/χ(h,0)` does not depend on `h` on `I`; equivalently
   `L(0,h) = 𝔞_leg(ρ)·(−iχ(h,0)/v_h)` for some nonzero constant
   `𝔞_leg(ρ)`.  **What this clause asserts is that `h`-profile — the
   reciprocal LSZ energy denominator `[ω(h+k)−ω(h)]^{-1}k`, the corpus's
   fixed provenance for `L` (`soft-current-recon.md` ⟨1⟩7,
   `paper/main.tex:524--527`, `soft-index-b.md:808`) — and no value.**  By
   (3a) `L` is a single class-level function, so `𝔞_leg(ρ)` is a datum of
   the class `𝒮_W(ρ)` and not of any individual source, and it is defined
   only when that class is nonempty.  **This definition fixes no value of
   `𝔞_leg(ρ)` at any density, `ρ = 1/2` included.**  As frozen, this clause
   stipulated `𝔞_leg = 1`, which under the corpus's jet-identification
   bridge contradicts PROVED `S2-2body-S` at every `ρ ≠ 1/2` (bd
   `tns-iu5`); that stipulation is withdrawn.  Two candidate readings are
   carried in `claims/CLAIMS.md` and neither is part of this definition:
   the conditional matched value `𝔞_leg(ρ) = 1/Z_ρ` (row `D24-VAL`,
   proved as an implication from the bridge plus class membership), and
   the open lemma **AMP** of the same value from a soft-leg amputation
   mechanism (row `AMP`, CONJECTURE).  Fence on AMP: by (b)(ii) a leg
   normalisation alone contributes `Z_ρ^{-1/2}`, and that value is refuted
   against the ansatz-free two-magnon data at the pre-registered band, so
   AMP requires a second factor `Z_ρ^{-1/2}` from a different mechanism
   (`theory/verdicts/d24d3-adjudication-r3.md` ⟨1⟩4).  At `ρ = 1/2` the two
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

### 5.3 `claims/CLAIMS.md`

*L5 compliance note.*  The file header fixes the authoritative statuses as
`PROVED | SKETCH | CONJECTURE | REFUTED` and says that "empirical,
conditional, under-review, and future-work qualifiers belong in prose, never
as additional status values".  So the r2 critic's suggested label "PROVED
(conditional implication; currently vacuous-or-unknown)" is taken as
**status `PROVED`** with the qualifier moved into the statement column,
exactly as ML5-B already does.

**5.3a — REPLACE the ML5-B row (line 41) with:**

```
| ML5-B | Conditional implication on the five-condition D24(d) class `𝒮_W(ρ)`, including the exhaustive normed LSZ decomposition.  The implication is proved; its displayed conclusion is `M_2^O(k,h) = 2i𝔞_leg(ρ) χ k M_1^O(h) + O_{L²(I)}(k²)`, with `𝔞_leg(ρ)` the D24(d)3b soft-leg amputation constant.  **This conclusion contains no number at any density, `ρ = 1/2` included:** D24(d)3b fixes no value of `𝔞_leg`, so ML5-B predicts a factorisation SHAPE — linear in `k`, proportional to `M_1^O`, with a class constant — and not a coefficient.  The number `2` was never a consequence of this row; it was a consequence of this row plus the frozen D24(d)3 stipulation `𝔞_leg = 1`, which is withdrawn.  Corpus displays of the soft coefficient `2` rest on the contact/oracle route (`oracle-bethe.md` O7–O9, `paper/main.tex:515–520`), which does not use D24(d).  **Re-scoped 2026-08-29 (bd `tns-iu5` r3):** the frozen clause forced soft slope `2` at EVERY tail density, contradicting PROVED `S2-2body-S` (`1/S`) given the jet-identification bridge — frozen `𝒮_W` provably empty for `ρ ≠ 1/2`.  Clause 3 is now split: 3a keeps the process-independence/`C¹`-extension hypothesis with `L` DEFINED as the descendant quotient (`k ≠ 0`); 3b asserts only the `h`-profile of `L(0,h)` and leaves `𝔞_leg(ρ)` open.  The two candidate values are carried as rows D24-VAL (conditional, proved as an implication) and AMP (CONJECTURE).  The proof of the implication is unchanged apart from carrying `𝔞_leg` as a nonzero constant factor (⟨2⟩1.⟨3⟩2 needs only `𝔞_leg ≠ 0` and `v_h` bounded below on `I`), so the corpus-r2 promotion is reparametrised, not reopened.  Nonemptiness and microscopic membership remain CONJECTURE/future work bd `tns-axg`, at every `ρ`. | PROVED | ML4-A, ML5-A, D24(d) | theory/ml5-universality.md ⟨1⟩3; PROVED per corpus-r2.md adjudication (conditional implication) — see the r3 annotation appended at corpus-r2.md:174–178, which records that the multiplication certified there survives verbatim with `𝔞_leg` carried; clause-3 repair adjudicated in theory/verdicts/d24d3-adjudication-r3.md (bd tns-iu5 r3) | theory/checks/ml4_check.py local obstructions only (`𝔞_leg`-blind: both D24(e) counterexamples have `M_1^O = 0`); theory/checks/d24d3_normalization_check.py D24N-C1–C3 test the kinematics of the conclusion, not its constant |
```

*(Note: `S2-2body-S` is deliberately NOT added to ML5-B's depends-on — with
the value retired, ML5-B's conclusion does not reference it; the dependency
belongs to `D24-VAL`.  The r2 critic verified this reasoning, §7.)*

**5.3b — ADD a new row `D24-VAL` (immediately after the ML5-B row):**

```
| D24-VAL | Conditional matched value of the D24(d)3b amputation constant, in the D24(b) normalisation convention.  GIVEN (α) the jet-identification bridge — the D24(d) soft multiplier's jet equals the two-body physical phase jet (corpus identification via soft-current-recon.md (R17) and oracle-bethe.md O9; NOT a PROVED row) — and (β_S) existence of a member `O ∈ 𝒮_W(ρ)|_{ρ=S}` with `M_1^O ≠ 0` in the fully polarised spin-`S` register (written `𝒮_W(ρ)|_{ρ=S}`, not `𝒮_W(S)`, to keep the `ρ`-vs-`s` fence visible at the point of use; and note that the `ρ` here is the D24(d) tail density of `notation.md`'s `ρ`-row, NOT the file-local double-occupancy coefficient `ρ` of theory/spin-s-twomagnon.md ⟨1⟩1–⟨1⟩2, which is the shard `S2-2body-S` lives in): THEN, for each such `S` separately, `𝔞_leg(S) = 1/(2S) = 1/Z_ρ`, i.e. `L(0,h) = −iχ/(2ρ v_h)` and ML5-B jet `χ/ρ`, at `S ∈ {1/2, 1, 3/2, 2}`.  Within the family `𝔞_leg = Z_ρ^{-p}` the exact law `(2S)^p = 2S` forces `p = 1` at any single `2S ≠ 1` (the `S = 1/2` point is degenerate; the four densities are four points of one analytic curve, not four independent measurements).  **The implication is a theorem; its antecedents are not.**  It is currently VACUOUS-OR-UNKNOWN: (β_S) is open at every `S` (bd `tns-axg`) and (α) is unproved, so the row constrains future work — any member ever exhibited must have this value — rather than supplying evidence now.  It cannot be upgraded past that reading until `tns-axg` exhibits a member or AMP closes.  Extension to non-half-integer `ρ` is hypothesis, not consequence. | PROVED | D24(b), D24(d), S2-2body-S, ML5-B | theory/verdicts/d24d3-adjudication-r3.md §2 ⟨1⟩3 | theory/checks/d24d3_normalization_check.py D24N-C6 tests the numerical consistency of the CONSEQUENT with the ansatz-free two-magnon slopes, at a band derived from the data's own quoted error; neither antecedent is tested by any gate, and no gate bears on `L`, `E^O_desc` or membership |
```

**5.3c — ADD a new row `AMP` (immediately after the `D24-VAL` row):**

```
| AMP | Soft-leg amputation lemma: in the D24(b) normalisation convention, charge-created soft-leg amputation contributes the per-site order-parameter density `Z_ρ = 2ρ` to the external flux, i.e. `𝔞_leg(ρ) = 1/Z_ρ` UNCONDITIONALLY — without the D24-VAL bridge and without assuming a class member.  Originally named at theory/verdicts/soft-index-r1.md F1(c)(i).  Statable only relative to D24(b)'s convention: a change of normalisation rescales `𝔞_leg`, so before that convention the statement had no truth value (bd `tns-iu5` r2 critic F1).  **Quantitative fence (theory/verdicts/d24d3-adjudication-r3.md ⟨1⟩4):** the leg-conversion mechanism is computed exactly — `Q^-_k|Ω⟩ = √(Z_ρ)|k⟩`, D24N-C8 — and supplies only `Z_ρ^{-1/2}`, a value the ansatz-free data refutes at the PRE-REGISTERED band (`--red-halfpower`, deviations 0.42/0.73/1.00 vs band 0.08).  AMP is therefore true only if a second factor `Z_ρ^{-1/2}` arises from a mechanism that is NOT a leg normalisation; any proposed proof must be checked against D24N-C8 or it double-counts the leg. | CONJECTURE | D24(b), D24(d) | — | theory/checks/d24d3_normalization_check.py D24N-C8 (the leg-conversion constant); D24N-C6 `--red-halfpower` (the leg-normalisation-only value refuted) |
```

**5.3d — REPLACE the ML5-A row (line 40) with:**

```
| ML5-A | Repaired iff: `M_2^O(0)=0` and `𝔠_h(O)=0`, with source-wise remainder controlled by `K_O` and the relative bound separately assumed.  The criterion is constant-agnostic: its proof evaluates at `k=0` and differentiates once and never uses the value; since bd `tns-iu5` (r3) it is stated with D24(c)'s constant `2i𝔞_leg χ`, and `𝔞_leg ≠ 0` suffices.  D24(e)'s counterexamples are `𝔞_leg`-blind (both have `M_1^O = 0`), so neither D24(e) nor ml4_check.py tests `𝔞_leg` or needs an edit. | PROVED | D24(c) | theory/ml5-universality.md ⟨1⟩2; PROVED per corpus-r2.md adjudication | theory/checks/ml4_check.py ML5-I1 |
```

### 5.4 `notation.md` (the L4 symbol registry)

**5.4a — ADD to the ML4/ML5/M-quant symbol table (after the `𝒮_W` row):**

```
| `L(k,h)`, `L(0,h)` | D24(d)3a external flux factor: the descendant quotient `E^O_desc/[(e^{ik}−1)·2iv_h·M_1^O(h)]`, defined for `k ≠ 0` where `M_1^O(h) ≠ 0`; `L(0,h)` is the value at `k=0` of the hypothesised `C¹` extension.  D24(d)3b asserts its `h`-profile — the reciprocal LSZ energy denominator, whose provenance in the corpus (`soft-current-recon.md` ⟨1⟩7; `paper/main.tex:524–527`; `soft-index-b.md:808`) is written in the D6 register `ρ = 1/2` and fixes the profile, not the constant.  `L(0,h) = 𝔞_leg(ρ)·(−iχ(h,0)/v_h)`.  Normalisation-dependent: `L ↦ (c′/c)L` under D24(b)'s rescalings | definitions.md D24(d)3 |
| `Z_ρ` | order-parameter density `2ρ`; for an su(2) model with a fully polarised α tail, `Z_ρ = ω_α([S^+_x, S^-_x])`.  Subscripted deliberately: bare `Z` stays Pauli-reserved (overload rule 9, unchanged) | definitions.md D24(d) |
| `𝔞_leg(ρ)` | soft-leg amputation constant of D24(d)3b, `𝔞_leg(ρ) := i v_h L(0,h)/χ(h,0)`; a datum of the class `𝒮_W(ρ)`, defined only when that class is nonempty, constant in `k`, `h` and `O` but NOT in `ρ`.  Meaningful only in the D24(b) normalisation convention, which rescales it.  Value OPEN: conditionally matched `= 1/Z_ρ` by claim D24-VAL; asserted `= 1/Z_ρ` unconditionally by the CONJECTURE row AMP; `= 1` as frozen (withdrawn).  Written bare `𝔞_leg` inside a fixed-`ρ` display (overload rule 13) | definitions.md D24(d)3b |
| `E^O_desc` | descendant external-leg term of the D24(d)1 decomposition (fraktur `𝔈` avoided: `𝔈_W`, `𝔈_{A_α}`, `𝔈_{A_β}` are the window CP maps); not a transfer map — see overload rule 8 | definitions.md D24(d)1 |
```

**5.4b — REPLACE the `𝒮_W` row (line 258) with:**

```
| `𝒮_W(ρ)` | the ρ-indexed five-condition Ward/LSZ/no-contact source class in the repaired conditional ML5-B implication; `ρ := ω_α(S^z) > 0` | definitions.md D24(d) |
```

**5.4c — In the `𝖲(k_s;{q_i,v_i})` row (line 244), replace** "on the D24(d)
class `𝒮_W`" **with** "on the D24(d) class `𝒮_W(ρ)`".

**5.4d — APPEND to overload rule 2** (the pre-existing bare-`χ` tension;
minimal amendment, not a resolution):

```
   Recorded exception (2026-08-29, bd `tns-iu5` r3): D24(c)/(d) and the ML5
   shards use the *argumented* channel sign `χ(h,k)` (registered below) and
   abbreviate it `χ` inside their own displays; the bare-`χ` =
   bond-dimension rule is unchanged everywhere else.
```

**5.4e — APPEND to overload rule 8** (r2-critic m2: `E_O` is live at
`definitions.md:67`, `theory/spt-rebuild.md:183`,
`theory/ansatz-scattering-2m.md:146` (the r2 critic wrote `:141`; the live line is `:146`, re-verified this round), so `E^O_desc` collides with the rule as
written):

```
   Exception (bd `tns-iu5` r3): `E^O_desc`, with the literal word subscript
   `desc` and an operator superscript, is the D24(d)1 descendant
   external-leg term and is NOT a transfer map or a contraction of one.  It
   is the only member of the `E` family carrying a word subscript.
```

**5.4f — ADD overload rule 13** (r2-critic m1: the r2 rationale "bare `𝔞` is
the twisted group algebra `𝔞_α`" is **false** — `𝔞_α` is itself subscripted,
so subscripting does not disambiguate; the actual disambiguator is the
subscript *type*, and no rule recorded it):

```
13. **`𝔞`** — the fraktur `𝔞` carries a *Greek tail label* for the twisted
    group algebra `𝔞_α`, `𝔞_β` of the asymptotic charge algebra (D4,
    `notation.md`'s `𝔞_α` row), and a *word label* for the D24(d)3b soft-leg
    amputation constant `𝔞_leg`.  There is no bare `𝔞`.  `𝔞_leg` is written
    `𝔞_leg(ρ)` wherever more than one density is in play, and bare inside a
    fixed-`ρ` display.
```

### 5.5 ADVISORY — same-commit obligations (NOT optional)

1. Apply §4.2's `ml5-universality.md` edits (constant `2i𝔞_leg χ`, the
   line-158 Wigner sentence, header ERRATUM pointer) in the SAME commit as
   §5.0–§5.4, or add the ERRATUM-block alternative.  Do not ship §5.0–§5.4
   alone.
2. Apply §4.2's `TRIANGLE.md` cross-reference refresh (`𝒮_W → 𝒮_W(ρ)` at
   lines 24, 215, 254, 257, 528).
3. ERRATUM pointers (not edits) at the heads of `theory/soft-index.md`
   (`:161–162`) and `theory/soft-index-b.md` (`:757–758, 808`), pointing at
   this verdict.
4. **NEW (r2-critic m8):** ERRATUM pointer at
   `theory/verdicts/soft-index-r1.md:170` — "for every model in the class …
   phase slope `2χ`" is superseded; a verdict record, so a pointer suffices.
5. **NEW (r2-critic M4, the serious one):** append the r3 **annotation** to
   `theory/verdicts/corpus-r2.md:174–178` given verbatim in §4.2.  This is a
   promotion record, not a failed-lane record: it must be annotated, not
   erratum'd, and the annotation must say that the certified implication
   survives reparametrisation so that ML5-B's where-proved column does not
   point at a document certifying a different conclusion.
6. **NEW (r2-critic M4):** the one-clause scoping edit at
   `paper/main.tex:524–527` given verbatim in §4.2.  This sentence is cited
   by ⟨1⟩4.⟨3⟩2 as the charge-created reading, so the edit and this verdict
   must ship together or the paper and the definition disagree about what
   the division leaves.
7. bd `tns-v44` (unified S1 r2) instruction: the r2 shard must carry the
   factor as the displayed OPEN constant `𝔞_leg(ρ)` citing D24(d)3b, with
   the matched value cited as `D24-VAL` and the unconditional lemma as
   `AMP`.  **Rider (r2-critic §8):** the shard must not describe `𝔞_leg` as
   *derivable*, and must not use the leg-normalisation mechanism, which
   ⟨1⟩4 refutes.
8. `HANDOFF.md` corpus-damage line "(3) Frozen `𝒮_W` empty for `ρ≠1/2`"
   becomes "repaired by retirement: clause 3 split, D24(b) convention fixed,
   `𝔞_leg(ρ)` OPEN (rows `D24-VAL` conditional, `AMP` CONJECTURE); ML5-B now
   predicts no number at any density; `𝒮_W(ρ)` nonemptiness open at every
   `ρ`".
9. Paper-lane ticket (r2-critic n4, outside this lane): `paper/main.tex:179,
   181–182` (Fig-2 caption) says "the **universal** coefficient `2`" and
   "**Every** soft magnon…" with no `s`/`ρ` qualifier.  It is unaffected by
   this repair (it rests on `S2-2body` via the contact route at
   `main.tex:515–520`), but §4.3's re-sourcing makes the caption's warrant
   worth restating.  File it; do not fix it here.

---

## 6. HONEST STATUS

**H1 — PROVED (fenced twice; r1-critic V1–V6, r2-critic W7).**
`Z_ρ = 2ρ = 2S`; `‖Q^-_k|Ω⟩‖²/N = Z_ρ` for all `k`; `v_S(h) = Z_ρ J sin h`;
`⟨h|Q_0^†J^-_0|h⟩ = 2i v_S(h)` exactly at `2S = 1,2,3,4`; the frozen
`𝔞_leg = 1` makes ML5-B's jet identically `2χ`; the exact spin-`S` phase
slope is `1/S`.  **New and PROVED this round:** `Q^-_k|Ω⟩ = √(Z_ρ)|k⟩`
exactly, with `|k⟩` an eigenvector of the one-magnon block of `H_S`
(D24N-C8; residual `1.8·10^{-15}`, overlap error `8.9·10^{-16}`).

**H2 — CONVENTIONAL, and declared so.**  The D24(b) normalisation convention
of §5.0 is a **choice**, not a theorem.  It is the choice under which the
D24 amplitudes are normalised like the asymptotic amplitudes the physical
phase is defined from; ⟨1⟩0.⟨3⟩6 names the alternative it refuses and why.
Every numerical statement about `𝔞_leg` in this corpus is relative to it,
and that relativity is now displayed in `definitions.md` rather than silent.

**H3 — MATCHED, CONDITIONAL, and RETIRED from the definition.**
`𝔞_leg(ρ) = 1/Z_ρ` is fixed by on-shell matching against PROVED
`S2-2body-S` — conditional on the jet-identification bridge (unproved, H6)
*and* on membership (open, §4.4).  It is not derived, not stipulated into
any L4 file, and not a fitted constant: within the family `Z_ρ^{-p}` the
exponent is pinned symbolically at any single `2S ≠ 1` (⟨1⟩3.⟨3⟩3).  Its DAG
home is `D24-VAL`, whose *implication* is a theorem and whose *content* is
currently vacuous-or-unknown.

**H4 — OPEN LEMMA, now with a quantitative fence.**  AMP is the
unconditional statement of the same value.  It is statable only relative to
H2's convention.  What is known about its mechanism is negative and now
quantitative: leg conversion supplies exactly `Z_ρ^{-1/2}` (D24N-C8) and
`Z_ρ^{-1/2}` is refuted against data at the pre-registered band, so AMP
needs a second factor of the same size from something else (⟨1⟩4.⟨3⟩5).
Watanabe–Murayama fixes the natural invariant `Z_ρ`, not the factor 2
(⟨1⟩5.⟨2⟩3).

**H5 — REFUTED.**  (i) The frozen clause 3 as a universal value claim, given
the bridge (r1-critic V4/V5/V7).  (ii) The soft-leg **normalisation**
mechanism for AMP, in both its forms: the `N`-dependent `(2ρN)^{-1/2}` route
of the S1-A critic (D24N-C7, display) and — new, and the sharper of the two
— the `N`-free `Z_ρ^{-1/2}` route that the fixed convention actually implies
(D24N-C6 `--red-halfpower`, margin 5–12× at the pre-registered band).  NOT
refuted: either S1 lane's arithmetic, or lane B's per-volume bookkeeping,
which is the bookkeeping adopted here.

**H6 — CONDITIONAL, and the one place a critic should push.**  The bridge —
the D24(d) soft multiplier's jet equals the two-body physical phase jet — is
the corpus's working identification ((R17), O9), not a PROVED row.  It now
carries *more* weight than in r2, because ⟨1⟩4's refutation of the
half-power route also rests on it: without the bridge, nothing in §3 is
matched and nothing is refuted.  Citation note: the bridge evidence is (R17)
and O9 only; `ml5-universality.md` ⟨1⟩4.⟨3⟩4's `s′(0,h) = 2i` is the `O_η`
bra coefficient, not ML5-B's constant, and is not cited as bridge evidence.

**H7 — EVIDENCE, not proof.**  The acceptance table is numerical
(ansatz-free ED, extrapolated); H1's exactness claims are machine-precision
identities at finite `N`, not `N → ∞` theorems; the `S2-2body-S` input is
exact and PROVED; the extrapolation carries the residual error, and the
acceptance band is now that error rather than a chosen number.

**H8 — WHAT THIS MERGE COSTS.**  After it, no L4 file fixes `𝔞_leg` at any
density and **ML5-B predicts no number at any density, `ρ = 1/2` included**
(§4.3).  The corpus keeps every display of the coefficient `2`, but on the
contact/oracle warrant, not on D24(d).  A reader who wants a number from the
five-condition class will not find one until `tns-axg` or AMP closes.  This
is stated as a loss, not managed as a footnote (L10).

**H9 — NOT claimed.**  Nothing here promotes `S-general`, `Bc`, `M-quant`,
`S-INDEX`, or AMP; nothing supplies a member of `𝒮_W(ρ)`; nothing touches
`tns-ebh` or `tns-uxr`.  Additionally not claimed: any value of `𝔞_leg` in
`definitions.md`; any statement at non-half-integer `ρ`; any mechanism for
AMP; and — new this round — any claim that the §5.0 convention is forced.

---

## 7. Certificate

`theory/checks/d24d3_normalization_check.py`, **559 loc** (L2 disclosure: 59
over the 500-loc guideline; the excess is the new D24N-C8 one-magnon block
and the two extra C2 routes, both demanded by r2-critic F1/m4 — flagged
rather than hidden, and a candidate for a later split into an algebra module
and a data module).  No bare `assert`; every failure raises `SystemExit(1)`
with the gate name as the first token of the message, so the **exit path** is
always identified.

Green (`python3 -O`, exit **0**):

```
D24N-C1 GUARD frozen_jet_coefficient=2*chi matched=chi/rho
D24N-C2 ladder x4 (residue, dense/occupation cross-check, multi-quantum norms, soft-leg norm + cross-momentum orthogonality), max_error=1.137e-13
D24N-C3 Ward residue = Z_rho*2iJ sin h, max_error=4.814e-15
D24N-C4 ansatz-free slopes vs 1/S: max_rel_dev=0.0043 (pre-registered band 0.08)
D24N-C5 DISPLAY frozen-clause relative deviations at S=1/2,1,3/2,2: 0.000, 1.002, 2.003, 3.003  -> defect size 3.003
D24N-C6 candidate max_rel_dev=0.0033 vs acceptance band 0.0479 DERIVED from the data's own quoted error (< pre-registered 0.08, so C6 is not subsumed by C4); fitted exponent=1.0024 over 2S!=1 spins; symbolic (2S)^p=2S root p=1 at S=1,3/2,2; S=1/2 degenerate: 1**p - 1 = 0
D24N-C6 resolving intervals for p: at the derived band [0.969, 1.037]; at the pre-registered band [0.947, 1.062]; at r2's retired 0.02 band [0.989, 1.017] (reported, gates nothing)
D24N-C7 DISPLAY N-dependent half-power route gap=1.855e-01
D24N-C8 Q^-_k|Om> = sqrt(Z_rho)|k>: eigenvector residual=1.799e-15, overlap error=8.882e-16; so leg conversion alone gives a_leg = Z_rho^(-1/2), refuted by --red-halfpower at the PRE-REGISTERED band
PASS: D24-VAL candidate a_leg = 1/(2 rho) matches; frozen a_leg = 1 and leg-conversion a_leg = Z_rho^(-1/2) both refuted; the D24(d)3b definition itself fixes no value (lemma AMP open)
```

### 7.1 Red modes — exit PATH, not just exit code (six, up from four)

| mode | exit | died at (gate named in first stderr token) |
|---|---|---|
| `--red-frozen` (`𝔞_leg = 1`) | 1 | **D24N-C6** `at S=1.0 dev=1.0016; S=1.5 dev=2.0027; S=2.0 dev=3.0033` — fails at `S = 1` first, as the r1 work order demanded |
| `--red-power` (`Z_ρ^{-2}`) | 1 | **D24N-C6** `at S=1.0 dev=0.4984; S=1.5 dev=0.6640; S=2.0 dev=0.7467` |
| `--red-halfpower` (`Z_ρ^{-1/2}` — now the **leg-conversion prediction**, ⟨1⟩4) | 1 | **D24N-C6** `at S=1.0 dev=0.4158; S=1.5 dev=0.7347; S=2.0 dev=1.0033` |
| `--red-ward` (residue `∼ Z_ρ²`) | 1 | **D24N-C3** `Ward residue Z-scaling error 1.697e+01` |
| `--red-ladder` (**NEW**; ladder element `×3.7` at every `n ≥ 1`, exact at `n = 0` — the r2 critic's `cA_deepladder`) | 1 | **D24N-C2** `ladder/soft-leg-norm error 1.477e+06` — r2's C2 passed this mutant at `8.9·10^{-16}` and it died only downstream at C3 |
| `--red-legfactor` (**NEW**; leg conversion `Z_ρ` instead of `√Z_ρ`) | 1 | **D24N-C8** `leg-conversion factor is not sqrt(Z_rho) (error 5.657e+00)` |

### 7.2 Data mutants (copies in the scratchpad; the DATA falsified)

| mutant (copy of `spin1-bc-falsifier.json`) | exit | died at |
|---|---|---|
| `m1_slope` — `S=1` summary slopes forced to `2.0` | 1 | **D24N-C4** `slope deviates from 1/S by 1.0000` |
| `m2_shift799` — every summary slope `×(1−0.0799)` | 1 | **D24N-C4** `0.0839` |
| `m2b_shift60` — every summary slope `×(1−0.060)` | 1 | **D24N-C6** `at S=0.5 dev=0.0604 … S=2.0 dev=0.0631` — **passes C4 (max row dev 0.064 < 0.08) and dies at the acceptance gate**, so C6 is still not subsumed by C4 with the *derived* band |
| **`m6_shift30` — every summary slope `×(1−0.030)`** | **0 (PASSES, and must)** | a `−3%` perturbation is *inside* the data's own quoted error at every spin; r2's `0.02` band **rejected** it (r2-critic M3(b)(iii)).  The derived band accepts it: `max_rel_dev = 0.0332 < 0.0479`.  This is the calibration fix, demonstrated |
| `m3_bandmoved` — `decision_band` `0.08 → 0.5` | 1 | **D24N-C4** `decision band moved: 0.5` |
| `m4_noband` — `decision_band` key deleted | 1 | **D24N-C4** `decision_band key missing` |
| `m5_absent` — data file missing | 1 | **D24N-C4** `missing ground-truth file` |
| **`m7_noerror` — the `error` column deleted from every row** | 1 | **D24N-C6** `data row has no quoted error column` — the derived band cannot silently default |
| **`m8_errinflate` — `error` column `×4`** | 1 | **D24N-C6** `derived band 0.1914 is not tighter than the pre-registered 0.08: C6 would be subsumed by C4` — the checker refuses to run a gate that C4 would imply |
| **`m9_errzero` — `error` column set to `0`** | 1 | **D24N-C6** `derived acceptance band is zero` |

### 7.3 Code mutants (copies in the scratchpad)

| mutant | result |
|---|---|
| `c1_nosqrt` — ladder element `sqrt((n+1)(2S−n)) → (n+1)(2S−n)` | exit 1 at **D24N-C2** `error 3.312e+05` |
| `c2_wronglaw` — symbolic law `(2S)^p = 2S → (2S)^p = 4S` | exit 1 at **D24N-C6** `gives roots [2], not [1]` |
| **`cB_onek`** — momentum loop reduced to one value (the r2 critic's mutant, which r2's checker passed with an *identical* error) | exit 1 at **D24N-C2** `fewer than three commensurate momenta: the orthogonality gate would be vacuous` |
| **`c3_wrongdispersion`** — C8's predicted one-magnon energy `ω_S(k) → ω_S(2k)` | exit 1 at **D24N-C8** `plane wave is not an H_S one-magnon eigenvector (residual 4.000e+00)` |

### 7.4 Gate audit (standing obligation, applied to this file)

* **C1** is a symbolic **guard** with no candidate-dependent input: no runtime
  mutation reaches it; only a code edit moves it.  Declared as a guard in the
  banner (`D24N-C1 GUARD`), not offered as evidence.
* **C5 is deductively subsumed by C4** for the true data and is labelled
  DISPLAY in the banner.
* **C7 is unfalsifiable on this data** (`N ∈ [60,480]`, so `|1/√(2SN) −
  1/2S| > 10^{-3}` always) and is labelled DISPLAY (r2-critic m5, adopted).
  The half-power route that *matters* is the `N`-free one, and it is
  falsified at C6, not here.
* **C6 is C4's comparison at a tighter band with mean rather than per-row
  aggregation.**  It measures no new quantity, and `predicted_jet(S,1.0) =
  1/S` exactly, so the two gates compare to the identical target (r2-critic
  M3(b)(i) — accepted without reservation).  It is not deductively subsumed
  **only** because the derived band `0.0479 < 0.08`, and the file now
  *asserts that ordering as a gate* (`m8_errinflate` dies on it) instead of
  claiming independence.  r2's "independent of C4" and "evidential gates"
  language is struck from this document.  C6's real gain is resolving power
  on the exponent: `p ∈ [0.969, 1.037]` versus C4's `[0.947, 1.062]`, a
  factor `≈1.7` — smaller than r2's claimed `≈3.5`, because that figure came
  from the over-tight band.  Quoted as an interval, never as a `±`
  (r2-critic m6).
* **C2, C3, C6, C8 have dedicated red modes; C4 is exercised by data
  mutation by design.**  Every gate is reachable: the candidate exponent is
  consumed at exactly one call site, and C8's inputs are independent of the
  data file, so no earlier gate short-circuits it.
* **Residual no-op audit (r2-critic m4, all three closed).**  (i) C2's
  ladder is now probed at every `n ≤ 2S−1` against a second, independently
  coded formula, and in multi-quantum norms — `--red-ladder` proves it moves.
  (ii) The momentum loop now carries a cross-momentum orthogonality test and
  a minimum-momenta requirement — `cB_onek` proves it moves.  (iii) The
  `require(1**p − 1 == 0)` non-gate is deleted; the degeneracy is printed.

### 7.5 The acceptance band: what changed and why (r2-critic M3(b)(iii))

r2's `ACCEPT_BAND = 0.02` was, objectively, post-registered (data committed
`2026-08-26` "Pre-registered 8% criteria"; the band `2026-08-29`), and — the
substantive complaint — **1.2–2.4× tighter than the data's own quoted
extrapolation error at every spin**, so a `−3%` perturbation drawn from
inside the error bars was rejected.  There is now **no acceptance constant in
the file**.  The band is computed at run time as `max_rows |error|·S` over
`A_ring_summary`, in the checker's own `dev·S` units:

| `S` | `\|1/S − mean\|·S` | max row dev·S | **max quoted `error`·S** |
|---|---|---|---|
| 1/2 | 0.000428 | 0.001071 | **0.032025** |
| 1   | 0.001604 | 0.002784 | **0.024125** |
| 3/2 | 0.002651 | 0.003283 | **0.038772** |
| 2   | 0.003321 | 0.004341 | **0.047854** |

so the derived band is `0.0479`.  It is guarded on both sides: zero or
missing `error` fails, and an `error` column so wide that `C4 ⇒ C6` fails
(`m8_errinflate`).  The r2 figure `0.02` is still *printed*, labelled "r2's
retired band … gates nothing", purely so the resolving intervals of the two
rounds can be compared.  r2's disclosure arithmetic ("one order above the
scatter, `0.0043`") is withdrawn: `0.02/0.0043 = 4.6`, and `0.0043` was the
residual *bias*, not the scatter (r2-critic m7).

**Consequence for the headline numbers.**  Every substantive conclusion of
the certificate survives at the **pre-registered** `0.08` band and needs no
acceptance band at all: the frozen `𝔞_leg = 1` misses by `1.00/2.00/3.00`,
and the leg-conversion `Z_ρ^{-1/2}` by `0.42/0.73/1.00`.  Only the exponent
interval uses the derived band.

### 7.6 Declination recorded (r1 M3(c)(iii), silently declined in r2)

r1 demanded an acceptance test that builds the jet from a **constructed**
`E^O_desc` rather than from `predicted_jet = 2.0/(2S)**p`.  r2 did not do it
and did not say so; the r2 critic caught that.  **It is declined here, with
its reason: constructing `E^O_desc` requires a member of `𝒮_W(ρ)`, and
exhibiting one would settle bd `tns-axg`.**  A checker cannot supply what the
open problem is about; a fabricated `E^O_desc` would be a gate testing its
own construction.  What is offered instead is the part that *can* be built
without a member: **D24N-C8** constructs the descendant soft leg
(`Q^-_k|Ω⟩`) and the asymptotic soft leg (the `H_S` one-magnon eigenvector)
from first principles and measures the conversion between them — the one
factor in `L` that is model-computable without membership.  That is a
partial substitute and is labelled as one.

---

## 8. Disposition

* **Merge**: §5.0 + §5.1 + §5.2 + §5.3 + §5.4 in one commit, in descending
  line order for the `definitions.md` spans, together with §5.5's nine
  same-commit obligations.  §5.0 is not optional and not separable: without
  it, §5.2's clause 3b and §5.3's three rows are statements about a
  convention that does not exist.
* bd `tns-iu5`: **re-scope, do not close.**  Its scope **grows**, per the r2
  critic §8, and sub-task (1) is now *done*: "(1) D24(b)'s amputation and
  leg-normalisation convention — **FIXED at r3 §5.0**; (2) prove or refute
  AMP (`𝔞_leg(ρ) = 1/Z_ρ`), now statable, with the ⟨1⟩4 fence: the leg
  normalisation supplies `Z_ρ^{-1/2}` and is refuted, so a second mechanism
  of the same size is required; (3) `D24-VAL` stays vacuous-or-unknown until
  (2) closes or `tns-axg` exhibits a member."
* bd `tns-axg`: stays open, unchanged; explicitly coupled to `D24-VAL`'s
  content and to `𝔞_leg`'s very definedness (⟨1⟩2.⟨3⟩5).
* bd `tns-v44`: unblocked on this axis, with the §5.5 item 7 instruction and
  its rider.
* **New bd (paper lane), to be filed by the orchestrator:** Fig-2 caption
  warrant, §5.5 item 9.
* **The next prover target is AMP**, and it is now writable: *in the D24(b)
  convention, compute the LSZ amputation of the charge-created soft leg for
  a descendant external-leg insertion, and decide whether the total is
  `Z_ρ^{-1}`; D24N-C8 fixes the leg-conversion factor at `Z_ρ^{-1/2}`, so the
  proof must exhibit a second, independent `Z_ρ^{-1/2}` or refute AMP.*  In
  the `m_λ` register per binding `soft-index-adjudication-r1.md` §3.5.
