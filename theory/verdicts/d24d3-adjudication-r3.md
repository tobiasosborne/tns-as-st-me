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
  band is **derived from the data's own quoted error** (`0.05`, §7.5); C2's
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
  **each** `S ∈ {1/2, 1, 3/2, 2}` at which `𝒮_W(S)` is nonempty in the
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
`S ∈ {1/2, 1, 3/2, 2}`, a member `O ∈ 𝒮_W(S)` exists in the fully polarised
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
