<!-- ROLE: ADVERSARIAL CRITIC verdict, round 2 (ADJUDICATION round), on
     theory/verdicts/d24d3-adjudication-r2.md,
     theory/verdicts/d24d3-repair-r2-response.md, and
     theory/checks/d24d3_normalization_check.py  (bd tns-iu5, r2).
     Brief: briefs/d24d3-critic-r2.md; protocol: briefs/critic-protocol.md
     (incl. its Standing checker obligations).  Priors:
     theory/verdicts/d24d3-adjudication-r1-critic.md FAIL(F1,F2,F3,M1–M7).
     Writable file of this lane: THIS FILE ONLY.  definitions.md,
     notation.md, claims/CLAIMS.md, the target verdicts and the checker were
     read, executed and mutated ON COPIES, never edited.  No git commit. -->

# r2 critic verdict — D24(d)3 ρ-normalisation adjudication (adjudication round)

**Headline.  The repair is a large, genuine improvement and it does NOT
relabel the stipulation: the number really is gone from `definitions.md`,
the repaired class is strictly larger than the frozen one, and the merge
therefore cannot install the r1 contradiction.  Seventeen of the twenty r1
dispositions I checked hold up under fresh recomputation, including the two
that mattered most — the `lstsq(x,x)` tautology and the `sites·two_s/sites −
two_s ≡ 0` no-op are genuinely gone, and I reproduced the −6% mutant that
passes C4 and dies at C6.  Three things stop it merging.**

1. **The split is well posed only as a RENAMING.**  `D24(b)` — which the
   proposition explicitly ASSUMEs — says "amputated one-hard amplitude" and
   never fixes an amputation convention.  With that convention unfixed,
   `𝔞_leg := i v_h L(0,h)/χ` is a name for an unknown ratio, not a physical
   factor; nothing forces the density into it rather than into `L`; and
   **AMP is not a well-posed lemma** — it has no statement independent of the
   missing convention.  §8 sends the next prover after an unstatable target.
2. **The merge text re-installs `𝔞_leg = 1` at `ρ = 1/2` by fiat.**  Three
   separate merge strings say the frozen clause "is recovered verbatim" at
   `ρ = 1/2`.  It is not.  After the repair *nothing in any L4 file supplies
   `𝔞_leg = 1` at any density, `ρ = 1/2` included* — that is the whole point
   of the retirement — so every D6 display of the coefficient `2` that traced
   to `D24(d)3` now depends on the OPEN lemma.  This is exactly the "does
   anything now implicitly require `𝔞_leg = 1`" failure the r2 work order was
   told to prevent, committed in the merge text itself.
3. **The acceptance gate is the same comparison as the ground-truth gate.**
   `predicted_jet(S, 1.0) = 1/S` *exactly* — I verified it: the C6 candidate
   target and the C4 ground-truth target are the identical function.  C6
   therefore tests C4's comparison with a different aggregation (mean, not
   per-row) and a 4× tighter band.  Non-subsumption is a pure band-width
   artifact — **any** band `< 0.08` produces it — and `ACCEPT_BAND = 0.02` is
   4–16× *tighter than the data's own quoted extrapolation error* (up to
   `0.048` in the same units).  The r1 critic's substantive M3(c)(iii) demand
   (build the jet from a constructed `E^O_desc` instead of the hardcoded
   `2.0/(2S)**p`) was declined without saying so.

**Final line at the bottom.**

---

## 0.  What I did (independent; nothing taken on the target's word)

* **(C-a)** Checker green + all four red modes under `python3 -O`; exit codes
  AND exit paths captured from stderr's first token.
* **(C-b)** Seven **data** mutants on copies in the scratchpad (`−6.0%`,
  `−7.99%`, `−3.0%`, `−2.5%` uniform shifts; `S=1` slope forced to `2.0`;
  `decision_band` moved; `decision_band` key deleted; data file absent).
* **(C-c)** Four **code** mutants on copies, two of them my own and not in
  the target's table: `c1_nosqrt`, `c2_wronglaw`, plus **`cA_deepladder`**
  (ladder element scaled by `3.7` at every occupation `n ≥ 1`, correct at
  `n = 0`) and **`cB_onek`** (momentum loop reduced to one value).
* **(C-d)** Two band-sensitivity mutants (`ACCEPT_BAND = 0.079` and `0.048`)
  to test whether the demonstrated non-subsumption is a property of the gate
  or of the number.
* **(C-e)** Absurd-input probes on the rebuilt C2 construction
  (`two_s = 3.7, −5.0, 10^6, 0.0`) and a symbolic simplification of every
  `require` in the file, hunting the shipped-no-op pattern.
* **(C-f)** Independent resolving-power computation: the exponent interval
  admitted by C4's band and per-row aggregation vs by C6's band and mean
  aggregation, over `p ∈ [0.5, 1.5]` at `5·10^{-4}` resolution; plus
  law-shaped data falsifications at `p' ∈ {0.95, 0.97, 1.03, 1.05, 1.10}`.
* **(C-g)** Direct extraction of the data's own `error` / `pairwise_spread`
  fields, converted into the checker's `dev·S` units, per row and per spin.
* **(C-h)** Objective provenance check of the "pre-registered" claim:
  `git log` on `numerics/results/spin1-bc-falsifier.json` and on the checker.
* **(C-i)** Exhaustive corpus grep for statements requiring `𝔞_leg = 1`,
  covering `definitions.md`, `notation.md`, `claims/CLAIMS.md`,
  `theory/**`, `paper/**`, and every verdict file, including the ones the
  target does not list.
* **(C-j)** Verbatim anchor and appliability check of every merge proposal
  against the current `definitions.md`, `notation.md` and `claims/CLAIMS.md`.

I did **not** re-derive the fourteen items fenced as VERIFIED CORRECT in §1
of the r1 verdict (`V1`–`V14`).  They stand; the r2 cites them correctly.

---

## 1.  VERIFIED CORRECT this round — fence this, do not churn it

Everything here I reproduced myself.  The repair lane must not spend a round
re-establishing any of it.

**W1.  Checker green and all four red modes reproduce exactly, with the
claimed exit paths.**  Green exit `0`, banner byte-identical to §7's.
`--red-frozen` / `--red-power` / `--red-halfpower` each exit `1` at
**D24N-C6**, `--red-ward` exits `1` at **D24N-C3**.  `--red-frozen` fails at
`S = 1` first, as the r1 work order demanded.

**W2.  The reachability pathology is genuinely resolved for hypothesis
mutants.**  I read `main()`: the candidate `exponent` is consumed at exactly
one call site (`check_acceptance`); `check_frozen_is_density_blind`,
`check_order_parameter_residue`, `check_ward_residue_scaling`,
`load_ring_slopes`, `check_ground_truth` and `check_defect` are all
candidate-independent (`check_defect` hardwires `predicted_jet(spin, None)`).
So every hypothesis mutant necessarily reaches C6.  r1's pathology — three
mutants dying at C4 with the acceptance test never exercised — is gone.

**W3.  The `−6%` data mutant reproduces, exactly as advertised.**  My own
copy: C4 max row deviation `0.0640 < 0.08` (passes), then
`FAIL: D24N-C6 candidate flux misses the acceptance band (0.02) at S=0.5
dev=0.0604; S=1.0 dev=0.0615; S=1.5 dev=0.0625; S=2.0 dev=0.0631`.  C6 is
**not deductively subsumed** by C4.  The claim is true as stated.

**W4.  The r2's correction of my r1 `−7.99%` finding is right and I was
wrong.**  On the rebuilt per-row C4 the `−7.99%` shift gives `0.0839` and
dies at **C4**, not C6.  I reproduced `0.0839`.  The r2 disclosed this
proactively rather than quietly; that is the right behaviour.

**W5.  r1's two shipped no-ops are genuinely gone as code paths.**
(i) `c1_nosqrt` (ladder element `sqrt((n+1)(2S−n)) → (n+1)(2S−n)`) exits `1`
at **D24N-C2** with error `1.200e+01`; r1's gate could not see this.
(ii) `check_exponent`'s `target` is now built from `np.mean(slopes[s])`, i.e.
from the DATA, while `design` is `log(2S)` — they are no longer elementwise
identical, so `lstsq` is no longer `lstsq(x,x)`.  `c2_wronglaw`
(`(2S)^p = 2S → (2S)^p = 4S`) exits `1` at **D24N-C6** with
`gives roots [2], not [1]`.  Both M3(c)(i) and M3(c)(ii) are honoured.

**W6.  The remaining data-mutant exit paths reproduce.**  `decision_band`
moved → C4 `decision band moved: 0.5`; `decision_band` key deleted → C4
`decision_band key missing from the data file` (r1's silent-pass hole is
closed, M3(c)(iv) honoured); data file absent → C4 `missing ground-truth
file`; `S=1` slopes forced to `2.0` → C4 `deviates from 1/S by 1.0000`.

**W7.  The value arithmetic and the split identity.**  `𝖲 = (e^{ik}−1)·
𝔞_leg(−iχ/v_h)·2i v_h = 2iχ𝔞_leg k + O(k²)`; equating to `S2-2body-S`'s
`i(χ/S)k` gives `2𝔞_leg = 1/S`, `𝔞_leg = 1/(2S)`.  `L(0,h) = 𝔞_leg(−iχ/v_h)
⟺ 𝔞_leg = i v_h L(0,h)/χ` (since `1/(−i) = i`).  `2(2S)^{-p} = 1/S ⟺
(2S)^p = 2S ⟺ p = 1` for `2S ≠ 1`, degenerate at `2S = 1`.  All correct.

**W8.  F3 is genuinely fixed for `Z_ρ`.**  `notation.md` overload rule 9
reserves **bare** `X, Y, Z`; `Z_ρ` is subscripted and therefore clean.  I
grepped the whole repo: no existing `Z_ρ`.  `Z_ρ := 2ρ` with
`ρ := ω_α(S^z)` is state language and matches `notation.md:270` verbatim; no
D6 ket `|Ω⟩` appears in the merged clause; the su(2) reading is explicitly
marked "a special case, not a membership condition".  The sign-flip and
su(2)-smuggling halves of r1's F3 are both answered.

**W9.  The ANTISYMMETRY hypothesis is restored correctly.**  §2 ASSUME and
the §5.2 preamble both carry "`ω_β(S^z) = −ω_α(S^z) = −ρ`" and label it
load-bearing, matching `claims/CLAIMS.md` `M-IDX-density`'s verbatim scoping
sentence.  M4(ii) is honoured.

**W10.  M7 is honoured verbatim.**  §5.2 clause 3a (artifact ll.593–598)
reads exactly M7(c)'s text: `k ≠ 0` restored, the `C¹` extension displayed as
the hypothesis, and `L(0,h)` explicitly named as *the extension's* value.
⟨1⟩1.⟨3⟩1 additionally records the `L²`-vs-pointwise zero-set gap.  This is
the best thing in the artifact and I would merge it on its own.

**W11.  The `ρ = S` register move does NOT breach the standing fence.**  I
checked the fence text myself rather than taking r1's word.
`notation.md:208` (`s`-row) and `notation.md:270` (`ρ`-row) both say
"H-MQG(2) fixes the D13(a) calibration parameter to be the tail density,
`s = ρ`"; the fence forbids only importing the `d = 2s+1` gloss as a
constraint on `ρ`.  `claims/CLAIMS.md` `M-IDX-density` says the same.  The
r2 uses `ρ = S` only inside the *conditional* row, explicitly scoped to the
fully polarised spin-`S` register, with extension to other `ρ` labelled a
hypothesis — which is precisely what my r1 M5(d) allowed.  **M5 is complied
with, not repeated.**  §4.5 acknowledges both binding decisions of
`soft-index-adjudication-r1.md` §3.2/§3.5 by name.

**W12.  The `ml5-universality.md` blast radius is now COMPLETE.**  I grepped
the whole file for every constant-bearing string.  Every one of lines 51
(3), 68 (4), 81 (4b), 142–144 (hyp. 3), 155 (boxed (5)), 158 ("two-site"),
170–172, 183–184 and 324–327 appears in §4.2.  The only two other hits are
line 164 (`(e^{ik}-1)L(k,h)[2iv_hM_1^O(h)]`, the clause-2 residue — correctly
untouched) and line 190 ("fixes `χ` and the external flux orientation" —
orientation only, survives).  Nothing is missing here.  M6 is honoured for
this file.

**W13.  `TRIANGLE.md` is clean.**  Lines 24, 215, 254, 257, 528 reference
`𝒮_W`/D24(d) only and display no constant; the file's only `𝒮_W` hits are
those five.  The two-site statements at 439–442 are explicitly scoped
`In M1 … on D8` and `1/s`-parametric.  §4.2's "cross-reference refresh only"
is correct.

**W14.  `ml4_check.py` and D24(e) are `𝔞_leg`-blind, and I verified the
mechanism.**  `ml4_check.py` contains zero occurrences of `chi`/`sgn`.  Both
`𝔠_h` tests run on sources with `M_1^O = 0` (`M_1^{ηD} = 0` because
`M_1^{O_η}` is `η`-independent, `definitions.md:978`; `M_1^{V_int} = 0`
outright, `definitions.md:987`), so the `−2i𝔞_leg χ M_1^O` term vanishes
identically for **every** `𝔞_leg`.  No test moves; D24(e) needs no edit.

**W15.  §5.1 is internally consistent and verbatim-appliable.**  The (c)
span is exactly `definitions.md:931–950` (`931` = `**(c) The contact first
jet.**`; `950` = `factorisation with the same stated norm control.`) and the
(d) span exactly `952–973` (`952` = `**(d) The Ward-covariant no-contact
class `𝒮_W`.**`; `973` = `is part of the ML5-B future work.`).  Crucially,
§5.1's replacement carries `𝔞_leg` into **all three** constant-bearing
displays inside the (c) span — `933` (`𝔠_h`), `938` (the ML5-A iff) and
`945` (the `K_O` bound).  D24(c) does not become internally inconsistent.
`claims/CLAIMS.md` ML5-A is line 40 and ML5-B line 41, as claimed.

**W16.  The five-condition count and the paper survive.**  `main.tex:244`
contains `five-condition` verbatim; `main.tex:542–546` renders clause 3 as
"a process-independent `C^1` kinematic LSZ normalization" with **no
displayed value**, so it is compatible with `𝔞_leg` free and needs no edit.
`main.tex:208` (`thm:soft`), `:249`, `:336–342` and `:379` are all
`s`-scoped or explicitly exclude the constant `2`.  `claims/CLAIMS.md`
displays no numeric soft coefficient in any row.

**W17.  M1 is properly retracted.**  r1's ⟨1⟩5 strawman is deleted, not
patched; ⟨1⟩4.⟨2⟩2 states what is true (lane B's factor is the `N`-free
`1/(2ρ)`; the `(2ρN)^{-1/2}` route was the S1-A critic's counter-analysis);
the ROLE header now says plainly that the adopted bookkeeping is
structurally lane B's and that r1's was lane A's.  M2 is properly
downgraded: the "load-bearing" and "entire defect" sentences are struck and
the Holstein–Primakoff count is deleted and restated as the negative open
question ("whatever mechanism AMP names, it is not a leg normalisation").

**W18.  The HONEST STATUS section H1–H7 is exemplary and, unlike r1, the
outward layers are almost in lockstep with it.**  The `definitions.md` text
asserts no value; the `D24-VAL` row displays both conditions; ⟨1⟩3.⟨3⟩4
states in terms the vacuity risk that `briefs/soft-index-target.md` makes a
MAJOR *if left silent*.  It is not left silent.  **The R2-O2 pattern is not
repeated.**

---

## 2.  FATAL

### F1.  The normalisation split is well posed only as a RENAMING: `D24(b)` — which the proposition ASSUMEs — fixes no amputation convention, so `𝔞_leg` carries no independent content, AMP is not a statable lemma, and nothing "forces" the density out of `L`

**(a) Location.**  `theory/verdicts/d24d3-adjudication-r2.md` §2 ASSUME
(l.197: "`D24(a)–(b)`"); ⟨1⟩2 **PROVE (ii)** (ll.205–208: "…the residual
constant `𝔞_leg := i v_h L(0,h)/χ` is the **only place it can live**");
⟨1⟩2.⟨3⟩3 (ll.259–268: "**no bookkeeping internal to clauses 2 and 3's
kinematics can produce a density dependence.**  Any density factor is an
*addition*, and its named home is the soft-leg amputation");
⟨1⟩2.⟨3⟩4 (ll.270–279); §1.3 ll.163–178 ("Because the corpus's construction
of `L` **forces** the frozen value…"); merge text §5.2 clause 3b
(ll.599–620); §8's AMP prover target (ll.881–885).

**(b) My computation.**  I read `definitions.md:923–929` in full.  D24(b)
reads, verbatim:

> **(b) Amputated amplitudes.**  For a source `O`, `M_1^O(h)` is its
> **amputated** one-hard amplitude and `M_2^O(k,h)` its connected
> hard-plus-soft amplitude in the physical channel; both are linear in `O`,
> and both are measured as multipliers in `L²(I,dh)` …

That is the entire treatment of amputation in D24.  **No amputation
convention is fixed anywhere in D24(a)–(e), in `notation.md`, or in
`claims/CLAIMS.md`** (I grepped all three).  Now trace the consequences.

*(i) `𝔞_leg` is a name for an unknown, not a factor.*  D24(d)3a defines
`L(k,h) := E^O_desc/[(e^{ik}−1)·2i v_h·M_1^O(h)]`.  Both `E^O_desc` and
`M_1^O` are D24(b) objects.  Rescale the amputation convention by a
constant `c` (any LSZ residue-normalisation choice does exactly this):
`M_1^O ↦ cM_1^O`, `E^O_desc ↦ c'E^O_desc`, and `L ↦ (c'/c)L`, hence
`𝔞_leg ↦ (c'/c)𝔞_leg`.  **`𝔞_leg` is not convention-independent.**  So the
statement "`𝔞_leg = 1/(2ρ)`" is not a statement about physics until the
convention is fixed — and D24(b) does not fix it.  ⟨1⟩2.⟨3⟩4's definition
`𝔞_leg := i v_h L(0,h)/χ` is therefore, at present, exactly a change of
variable: it renames the unknown `L(0,h)` as `𝔞_leg` times a known function
of `h`.  Nothing has been *decomposed*; a symbol has been introduced.

*(ii) Therefore PROVE (ii)'s "only place it can live" is not proved.*  With
the convention free, the density can be put in `L` (r1's route), in `𝔞_leg`
(this route), or split between them — the three are related by a rescaling
that D24(b) does not exclude.  ⟨1⟩2.⟨3⟩1's justification cites three prose
sentences (`soft-current-recon.md` ⟨1⟩7, `paper/main.tex:524–527`,
`soft-index-b.md:808`) — **none of which is a D-number, a claim id, or a
named computation**, which is what L6b requires of a leaf.  ⟨1⟩2.⟨3⟩3 then
*assumes* `L_kin(0,h) = −iχ/v_h` and observes the product is density-blind;
that is a consistency check of the assumed value, not a derivation of it.

*(iii) Therefore AMP is not a well-posed lemma.*  `soft-index-r1.md` F1(c)(i)
states AMP as "charge-created soft-leg **amputation** contributes the
per-site leg density `2ρ` to the external flux".  That statement
presupposes a fixed amputation convention and says what it contributes.
With no convention in D24(b), the lemma has no truth value.  §8 nominates
AMP as "the natural next prover target"; as things stand a prover cannot
even write down what is to be proved.  **This is the load-bearing defect of
the round**, because the entire honesty of the third horn rests on the value
having a real home to move to.

*(iv) What this does NOT damage.*  The split is still a *harmless and
strictly weakening* reparametrisation: the merged clause 3b asserts less
than the frozen clause (see W-note in §6), so no contradiction can be
installed.  Everything the round is trying to achieve survives.  What does
not survive is the word "forces" and the status of AMP as a lemma.

**(c) FIX DEMAND.**  Add to the §5.2 merge, in D24(b) or as the first
sentence of 3b: "*amputation convention*: `M_1^O` and `E^O_desc` are
normalised by ⟨the named convention⟩; `𝔞_leg` is defined relative to it, and
a change of convention rescales `𝔞_leg`" — and restate PROVE (ii) as "with
that convention fixed, `𝔞_leg` is the residual; which of `L` and `𝔞_leg`
carries the density is a bookkeeping choice, made here in favour of
`𝔞_leg` because the three D6 provenance sites read the `1/v_h` as the
reciprocal energy denominator."  Until the convention exists, §8 must name
"fix D24(b)'s amputation convention" as a prerequisite sub-task of AMP.

**(d) SURVIVING WEAKER STATEMENT.**  *Writing `L(0,h) = 𝔞_leg·(−iχ/v_h)` is
a legitimate change of variable that strictly weakens D24(d)3 and removes
the refuted value from the L4 file; the three D6 provenance sites make
`𝔞_leg` the more natural of the two homes.  But the choice is not forced,
`𝔞_leg` is convention-dependent, and AMP is not a statable lemma until
D24(b) fixes an amputation convention.*

---

## 3.  MAJOR

### M1.  The merge text re-installs `𝔞_leg = 1` at `ρ = 1/2` by fiat — three times, in both L4 files and in two DAG rows.  This is the exact defect the round exists to remove

**(a) Location.**  Artifact l.48 (headline: "At `ρ = 1/2`, `1/(2ρ) = 1` and
the frozen clause is **recovered verbatim** under either reading; the D6
corpus … is untouched"); **merge text** §5.2 clause 3b l.618 ("At `ρ = 1/2`
both readings give `𝔞_leg = 1` and the frozen clause is **recovered
verbatim**") — this string goes into `definitions.md`; §5.3a ML5-B row l.647
("at `ρ = 1/2` (`𝔞_leg = 1`) this is the frozen `2iχ k M_1^O` / `2χ` sites")
— goes into `claims/CLAIMS.md`; §5.3c ML5-A row l.663 ("at `𝔞_leg = 1`
(`ρ = 1/2`, D6) is the frozen form **in which D24(e) and `ml4_check.py` test
it**") — same; §5.1 merge text ll.8–11 and l.34 (same sentence into
`definitions.md`).

**(b) My computation.**  Three separate errors in one recurring sentence.

*(i) The frozen clause is NOT recovered at `ρ = 1/2`.*  Frozen clause 3:
`L(0,h) = −iχ/v_h`.  Repaired clause 3b: `L(0,h) = 𝔞_leg·(−iχ/v_h)` with
`𝔞_leg` "a nonzero constant … **NOT fixed by this definition**" (the merge
text's own bold, l.606).  Set `ρ = 1/2` and read the repaired clause: it
still says `𝔞_leg` is free.  Nothing in `definitions.md`, `notation.md` or
`claims/CLAIMS.md` fixes it at `1` there.  What IS true is the much weaker
"the two *candidate* values (the retired stipulation `1`, and AMP's
`1/(2ρ)`) coincide at `ρ = 1/2`".  The published sentence asserts a
recovery of the *clause*, which is false, and it is the sentence a later
reader will consume when they need `𝔞_leg = 1`.

*(ii) Consequence, which the artifact does not draw.*  After the merge,
**ML5-B — a PROVED row — predicts no number at any density, `ρ = 1/2`
included.**  Its conclusion becomes `2i𝔞_leg χ k M_1^O` with `𝔞_leg` OPEN.
Every corpus display of the coefficient `2` that traced its justification to
`D24(d)3` now depends on the open lemma.  Grepping for them: the paper's
Appendix B `main.tex:525–527` ("dividing a hard external-leg reduction by
the energy shift `v_h k_s` cancels the velocity and **leaves the `2`**"),
`soft-current-recon.md:361–363` ("leaving the root coefficient `2`"),
`oracle-bethe.md:351` and O9 (l.470) ("its magnitude is two sites"),
`ml5-universality.md` 155/158/183–184/326.  §4.3's "the D6 corpus … is
untouched" is right that none of these becomes *false* — they are
independently derived from the Bethe/contact route (`main.tex:520` solves
the contact equation directly for `2i`) — but it is wrong that nothing
changes: they lose their D24(d) justification and now stand on the oracle
alone.  §4.3 must say which of the two.

*(iii) The `ml4_check.py`/`D24(e)` half is affirmatively false.*  §5.1 l.34
and the ML5-A row l.663 both say `𝔞_leg = 1` is "the form in which D24(e)
and `ml4_check.py` test it".  I audited both (W14): `ml4_check.py` contains
zero occurrences of `chi`/`sgn`, and both `𝔠_h` counterexamples have
`M_1^O = 0`, so the `𝔞_leg` term vanishes identically for **every** `𝔞_leg`.
Neither D24(e) nor `ml4_check.py` tests `𝔞_leg` at all.  The sentence
manufactures a dependency on `𝔞_leg = 1` where none exists — into an L4 file
and into a PROVED DAG row.

**(c) FIX DEMAND.**  Replace all five occurrences with: "at `ρ = 1/2` the two
candidate readings of `𝔞_leg` (the retired stipulation `1`, and AMP's
`1/(2ρ)`) coincide, so the D6 displays of the coefficient `2` remain
numerically consistent with this clause; **this definition still fixes no
value of `𝔞_leg` at any density, `ρ = 1/2` included**, and the D6 displays
rest on the oracle route (`oracle-bethe.md` O7–O9; `paper/main.tex:520`),
not on this clause" — and strike "in which D24(e) and `ml4_check.py` test
it", replacing it with "D24(e)'s counterexamples have `M_1^O = 0`, so `𝔠_h`
is `𝔞_leg`-independent for them and neither D24(e) nor `ml4_check.py` needs
an edit."

**(d) SURVIVING WEAKER STATEMENT.**  *At `ρ = 1/2` the retired stipulation
and AMP agree, so the merge introduces no numerical conflict with the D6
corpus; but the repaired definition supplies `𝔞_leg = 1` nowhere, and after
the merge ML5-B's coefficient is open at every density.*

---

### M2.  ⟨1⟩2 PROVE (ii) quantifies "at **every** density" over three D6 sentences and one fully-polarised-spin-`S` computation

**(a) Location.**  Artifact ll.205–207 ("(ii) the corpus's fixed provenance
of `L` gives the kinematic value `−iχ/v_h` at **every** density"); the
supporting leaves ⟨1⟩2.⟨3⟩1 (ll.249–253) and ⟨1⟩2.⟨3⟩3 (ll.259–268); echoed
in §1.2's "jet `2χ` at **every** density" and in the merge text's "is the
whole of the value this clause asserts" (l.605).

**(b) My computation.**  Check the provenance of each cited leaf.
`theory/soft-current-recon.md` ⟨1⟩7 is a D6 shard (r1-critic V12: "(R14),
(R17), (R18) are D6, `definitions.md:348`, `S_x = σ_x/2` ⇒ `ρ = 1/2`");
`paper/main.tex:524–527` sits inside Appendix B's spin-`1/2` ferromagnet
discussion; `soft-index-b.md:808` is a failed lane's D6 transplant.  **All
three are `ρ = 1/2` statements.**  The only general-density input in ⟨1⟩2 is
⟨3⟩1's `ω_S(k) = 2JS(1−\cos k) ⟹ v_h = Z_ρ J\sin h`, which holds in the
**fully polarised spin-`S` ferromagnet** and nowhere else in the corpus.
So what ⟨1⟩2 can support is: "*in the fully polarised spin-`S` family*, the
reciprocal-energy-denominator reading of `L` gives `−iχ/v_h` at every
`ρ = S`, and the two powers of `Z_ρ` cancel."  It cannot support "at every
density", which quantifies over the free real `ρ` of `notation.md:270` — the
same over-reach my r1 M4(i) caught in the opposite direction, now committed
in a PROVE line.  This matters because ⟨1⟩2 is the step that decides the
bookkeeping home, and §1.3 escalates it to "**forces**" (l.165).

**(c) FIX DEMAND.**  In PROVE (ii) and §1.2/§1.3 replace "at every density"
with "at every `ρ = S` of the fully polarised spin-`S` family, the one
register in which the corpus computes; the three provenance sites are D6
statements and do not by themselves extend to general `ρ`", and downgrade
§1.3's "forces" to "makes `𝔞_leg` the natural home" (which is what F1 leaves
standing).

**(d) SURVIVING WEAKER STATEMENT.**  *In the fully polarised spin-`S`
register the energy-denominator reading of `L` is exactly density-blind,
because `v_h` and the Ward residue carry the same single power of `Z_ρ`;
this is verified at `2S = 1,2,3,4` (r1-critic V2/V3, D24N-C1/C3) and is
strong evidence that the density is not internal to clauses 2–3 there.  It
is not established for general `ρ`.*

---

### M3.  The acceptance gate C6 is the SAME comparison as the ground-truth gate C4 against the SAME target; its "independent failure mode" is a pure band-width artifact; and `ACCEPT_BAND = 0.02` is 4–16× tighter than the data's own quoted error

**(a) Location.**  `theory/checks/d24d3_normalization_check.py` l.83
(`ACCEPT_BAND = 0.02`), ll.309–313 (`predicted_jet`), ll.330–344
(`check_acceptance`), ll.299–306 (`check_ground_truth`); artifact §7.4
ll.849–856 ("The **evidential** gates of C6 are the acceptance comparison
(independent of C4 — `m2b_shift60`)"), §3 ll.390–392 ("acceptance band `0.02`,
tighter than **and independent of** D24N-C4's pre-registered `0.08`");
repair response M3 row disposition "**FIXED** (all five demands)" and
disclosure note 1.

**(b) My computation.**  Four prongs.

*(i) The two gates compare the same numbers to the same target.*  I
evaluated `predicted_jet(S, 1.0) = 2.0/(2.0*S)**1.0` and `1.0/S` at
`S ∈ {0.5, 1, 1.5, 2}`: the difference is **exactly `0.0`** at all four.
So `check_acceptance` at the true candidate is
`|1/S − mean_S|·S ≤ 0.02` and `check_ground_truth` is
`max_r |m_r − 1/S|·S < 0.08`.  Identical target `1/S`, identical units.  C6
tests C4's comparison with (a) mean instead of per-row maximum and (b) a 4×
tighter band.  **It measures no new quantity** — in particular it never
touches `L`, `E^O_desc`, `𝔞_leg`, or any member of `𝒮_W`.

*(ii) Non-subsumption is bought by the band, not by the gate.*  Since a mean
is a convex combination, `|1/S − mean|·S ≤ max_r|m_r−1/S|·S`.  So C4 ⇒ C6
holds **iff** `ACCEPT_BAND ≥ DECISION_BAND`.  Any band `< 0.08` breaks
subsumption.  I confirmed this constructively: with `ACCEPT_BAND = 0.079`
(mutant `cC_band079`) the green run still passes and the gate is still not
implied by C4 — yet that band would *not* catch `m2b_shift60`
(dev `0.060–0.063`).  The demonstration in §7.2 therefore establishes
"`0.02 < 0.08`", not a property of the acceptance test.

*(iii) The band is post-hoc, and it is tighter than the evidence.*  Objective
provenance (`git log`): `numerics/results/spin1-bc-falsifier.json` was
generated `2026-08-26T13:33:24` and committed the same day at `0fdcc7e`,
whose message says "**Pre-registered 8% criteria**".  The checker carrying
`ACCEPT_BAND = 0.02` was committed `2026-08-29` at `65a6d32`.  So the `0.08`
band is genuinely pre-registered and the `0.02` band is genuinely not — the
disclosure is accurate.  But now compare `0.02` with the data's own quoted
uncertainty, converted to the checker's `dev·S` units (`error` ×`S`):

| `S` | `|1/S−mean|·S` | max row dev·S | **max quoted `error`·S** |
|---|---|---|---|
| 1/2 | 0.000428 | 0.001071 | **0.032025** |
| 1   | 0.001604 | 0.002784 | **0.024125** |
| 3/2 | 0.002651 | 0.003283 | **0.038772** |
| 2   | 0.003321 | 0.004341 | **0.047854** |

**At every spin the acceptance band `0.02` is 1.2–2.4× tighter than the
data's own reported extrapolation error, and up to 16× tighter than the
worst row's.**  I made a `−3.0%` uniform data mutant — a perturbation
comfortably *inside* the data's own error bars at all four spins — and the
checker rejects it at C6 (`dev = 0.0304…0.0332 > 0.02`).  A gate that
rejects data drawn within its own stated uncertainty is not calibrated to
the evidence; it is calibrated to the observed residual bias (`0.0033`),
which was known when the band was chosen.  Fitting the band to the residual
is what "tuned after seeing the data" means, even though there is a 6×
margin and even though the author did not tune it to a specific mutant.
Note also the disclosure's arithmetic: `0.02 / 0.0043 = 4.6`, which is not
"one order above", and `0.0043` is a *bias*, not the *scatter* — the scatter
is the `error`/`pairwise_spread` column above.

*(iv) The substantive M3(c)(iii) demand was declined without saying so.*  The
r1 demand was: "add an acceptance test that can fail independently of
D24N-C4 — e.g. compute the jet from a **constructed** `𝔈^O` rather than from
the hardcoded `predicted_jet = 2.0/(2S)**p`".  `predicted_jet` is unchanged
(ll.309–313, still `2.0/(2.0*spin)**exponent`); no `E^O_desc` is ever
constructed anywhere in the file.  The letter of the demand ("can fail
independently") is met by tightening a constant; its substance is not.  The
response table's "**FIXED** (all five demands)" is therefore overstated.

*(v) What C6 DOES buy, stated fairly.*  I computed the exponent interval each
gate admits (scan `p ∈ [0.5,1.5]`, step `5·10^{-4}`): C4's per-row `0.08`
admits `p ∈ [0.947, 1.061]`; C6's mean-`0.02` admits `p ∈ [0.9885, 1.017]`.
So C6 genuinely tightens the exponent by ≈3.5×, and law-shaped data
falsifications at `p' ∈ {0.95, 0.97, 1.03, 1.05}` all pass C4 and die at C6.
That is real added resolving power on the exponent.  It is *not* independent
evidence about `𝔞_leg`, and it is not what §7.4's "evidential gates" claims.

**(c) FIX DEMAND.**  (i) Restate §3/§7.4 as: "C6 is C4's comparison at a
tighter band and mean aggregation; it adds resolving power on the exponent
(`p ∈ [0.989,1.017]` vs C4's `[0.947,1.061]`) and no independent evidence
about `𝔞_leg`; the `m2b_shift60` demonstration shows only that
`ACCEPT_BAND < DECISION_BAND`."  (ii) Either raise `ACCEPT_BAND` to the
data's own worst quoted error (`0.05`) and say so, or keep `0.02` and label
it explicitly "post-registered `2026-08-29`, chosen against the residual
bias, tighter than the data's quoted `error` column".  (iii) Record in the
response table that M3(c)(iii)'s constructed-`E^O_desc` route was **not**
taken, and why.

**(d) SURVIVING WEAKER STATEMENT.**  *The certificate honestly establishes:
the ansatz-free slopes match `1/S` to `≤ 0.0043` (C4, pre-registered `0.08`);
the frozen `𝔞_leg = 1` misses by `1.00 / 2.00 / 3.00` at `S = 1, 3/2, 2` and
hits at `S = 1/2` (C5); within the family `(2ρ)^{-p}` the data admit
`p ∈ [0.989, 1.017]` and the exact law pins `p = 1` symbolically.  That is a
20–900× margin against the refuted hypothesis and needs no post-hoc band at
all.  Nothing in the certificate bears on `L`, `E^O_desc`, `𝔞_leg`, or
membership.*

---

### M4.  Missed lockstep sites, again — and one of them is the PROMOTION RECORD of the PROVED row being re-scoped

**(a) Location.**  §4.1/§4.2/§4.2b/§4.3, which claim "Every address below was
obtained by grep this round"; response table M6 row, "**FIXED** — All five
missed sites added".

**(b) My computation (grep, whole repo, verdicts included).**  Two sites are
missing, and the first is worse than any of the five I found in r1.

| Missed site | Verbatim | Why it moves |
|---|---|---|
| `theory/verdicts/corpus-r2.md:174–178` | "* **ML5-B.** Multiplying `(e^{ik}-1)[-i chi/v_h][2iv_hM_1]` gives `2i chi kM_1+O(k^2)`.  Hypothesis 1 now says explicitly that the two bounded remainders are exhaustive.  This is a valid conditional implication" | This is **the adjudication that promoted ML5-B to PROVED**, and it verifies the `𝔞_leg = 1` arithmetic explicitly.  §5.3a keeps `PROVED per corpus-r2.md adjudication` in the where-proved column while changing the displayed conclusion to `2i𝔞_leg χ k M_1^O`.  After the merge the where-proved column points at a document certifying a **different** conclusion. |
| `paper/main.tex:524–527` | "`\braket{k_h|Q_0^\dagger J^-_0|k_h}=2\ic v_h`; dividing a hard external-leg reduction by the energy shift `v_h k_s` cancels the velocity and leaves the `$2$`." | Cited **three times** in §1.2/⟨1⟩2.⟨3⟩1/§5.2 as the authority for keeping the kinematic value — and listed in **neither** §4.2 (must change) **nor** §4.3 (does not change).  As written it says the division leaves exactly `2`, i.e. `𝔞_leg = 1`, with no density or leg-norm factor; after the merge `definitions.md` says the product is `2𝔞_leg`. |

Minor third: `theory/verdicts/soft-index-r1.md:170` states the class-level
slope as `2χ` for **every** model in the class; it is a failed-lane verdict
record and belongs in §5.5.2's ERRATUM list with `soft-index.md` and
`soft-index-b.md`.

Note in the r2's favour, and please do not churn it: `definitions.md:938` and
`:945` (the other two `2iχ` displays inside the (c) span) **are** covered —
§5.1's replacement carries `𝔞_leg` into all three (W15).  `ml5-universality`
and `TRIANGLE.md` are complete (W12, W13).

**(c) FIX DEMAND.**  Add `theory/verdicts/corpus-r2.md:174–178` to §4.2 with
an ERRATUM pointer (it is a promotion record, not a failed-lane record, so
it must be annotated rather than left stale), add `paper/main.tex:524–527`
to §4.2 with a one-clause scoping edit ("…leaves the `2`; in the general
class the same division leaves `2𝔞_leg`, and `𝔞_leg = 1` in this spin-`1/2`
register"), add `soft-index-r1.md:170` to §5.5.2, and downgrade the response
table's M6 row from "FIXED" to "FIXED for the five r1 sites; two further
sites found in r2".

**(d) SURVIVING WEAKER STATEMENT.**  *The blast radius is right about every
site it lists and is now complete for `ml5-universality.md`, `TRIANGLE.md`,
`notation.md`, `definitions.md` and `ml4_check.py` — a real advance on r1.
Its two omissions are concentrated where the artifact's own provenance
argument made it stop looking: the sentence it cites as authority, and the
adjudication that promoted the row it re-scopes.*

---

### M5.  `D24-VAL`'s status is CONJECTURE for a reason that is a category error, and it contradicts the corpus's own convention for conditional implications

**(a) Location.**  §5.3b, the `D24-VAL` row: "…the row is **CONJECTURE**
because (α) is unproved and (β) is open at every `ρ`"; status field
`CONJECTURE`; against §5.3a's ML5-B row ("Conditional implication … The
implication is proved" | **PROVED**) and against ⟨1⟩3.⟨3⟩4 (l.314), which asserts
"⟨3⟩1–⟨3⟩3 **prove** a *conditional implication*".

**(b) My computation.**  `D24-VAL` is stated as `(α) ∧ (β) ⇒ 𝔞_leg = 1/(2S)`.
The unprovedness of an antecedent never downgrades an implication: if the
antecedent fails the implication is vacuously **true**, and if it holds
⟨1⟩3 derives the consequent.  Either way the row is a theorem, provided
⟨1⟩3 is a proof — and ⟨1⟩3.⟨3⟩4 says it is.  So the stated justification for
`CONJECTURE` is invalid, and the label collides with the corpus's own
convention: `ML5-B` and `M-INDEX-spec` are both conditional implications
with open or unproved hypotheses and both carry **PROVED**.  Installing
`D24-VAL` as CONJECTURE with that justification puts two incompatible
status conventions for the same logical shape side by side in the DAG (L5).

There is a defensible reading under which CONJECTURE is right: that (α) is
not a *stated hypothesis* but a *silently used bridge*, so the row is really
asserting `𝔞_leg = 1/(2ρ)` and merely flagging its conditions.  The artifact
must choose.  Note that if it chooses PROVED-as-implication then, exactly as
the brief warns, the row is currently **vacuous-or-unknown at all four
points** (§4.4 keeps nonemptiness open at every `ρ`, `ρ = 1/2` included) —
which is honest, disclosed at ⟨1⟩3.⟨3⟩4, and not the R2-O2 pattern, but
means the row's *content* is a constraint on future work, not evidence.

Secondary, same row: the **where-tested** column names `D24N-C4–C6`.  Those
gates test neither antecedent nor the implication; they test the numerical
consistency of the *consequent* with the ansatz-free slopes, which per M3(b)
is the C4 comparison.  A where-tested column that names gates which cannot
test the row is this campaign's signature defect moved up to the DAG layer.

**(c) FIX DEMAND.**  Either (i) set the status to **PROVED (conditional
implication; currently vacuous-or-unknown because (β) is open at every `ρ`)**
and move `CONJECTURE` to the AMP lemma, or (ii) keep CONJECTURE and restate
the row as the *unconditional* assertion it then is ("`𝔞_leg = 1/(2ρ)`;
CONJECTURE; the evidence is on-shell matching under the unproved bridge and
open membership") — and in either case rewrite where-tested as "numerical
consistency of the consequent with the ansatz-free two-magnon slopes
(D24N-C4/C6); neither antecedent is tested by any gate."

**(d) SURVIVING WEAKER STATEMENT.**  *Retiring the value into a conditional
row with both conditions displayed is the right architecture and is the
third horn honestly taken; the row's arithmetic is correct (W7) and its
vacuity risk is disclosed, not hidden.  Only its status label, its stated
justification for that label, and its where-tested column are wrong.*

---

## 4.  MINOR

**m1.  `𝔞_leg` is unindexed but takes four different values, and its
registry rationale is factually false.**  §5.4a's row reads "Subscripted
deliberately: bare `𝔞` is the twisted group algebra `𝔞_α` of the SPT
corner".  `𝔞_α` is **not** bare — it is subscripted (`notation.md:55`,
`definitions.md:288`).  So subscripting `𝔞_leg` does not disambiguate it the
way subscripting `Z_ρ` disambiguates bare `Z` under rule 9; the actual
disambiguator is the subscript *type* (Greek tail label vs the word `leg`),
and no overload rule records it.  Separately: clause 3b says `𝔞_leg` is
"independent of `k`, `h`, and `O`" — not of `ρ` — and AMP/`D24-VAL` assert
four different values at four `ρ`.  Under L4 the symbol must be `𝔞_leg(ρ)`,
or the row must say "a function of the class index `ρ`, constant within
`𝒮_W(ρ)`".  *Fix:* index it and add a real overload rule.  *Surviving:*
registering the symbol at all is the right move and the `Z_ρ` half of the
same repair is correct (W8).

**m2.  `E^O_desc` violates overload rule 8, which the merge does not
amend.**  `notation.md:124`, rule 8: "the transfer map and its contractions
carry an *operator or tensor-content* subscript, `E`, `E_O`, or `E_b`" —
`E_O` is live at `definitions.md:67`, `theory/spt-rebuild.md:183`,
`theory/ansatz-scattering-2m.md:141`.  `E^O_desc` is roman `E` with a
tensor-content-shaped subscript and is not a transfer map.  §5.4a's row
addresses only the fraktur `𝔈_W` collision that r1's m1 raised.  *Fix:*
append one sentence to rule 8 ("`E^O_desc` with the literal subscript `desc`
is the D24(d)1 descendant external-leg term, not a transfer map"), or use a
glyph outside the `E` family.  *Surviving:* the rename away from `𝔈` was the
right call and was my own r1 suggestion.

**m3.  Clause 3b's merge text asserts a value in a clause that asserts none,
and is not a per-source membership condition.**  (i) l.605: "…and is **the
whole of the value this clause asserts**" — the clause asserts
`L(0,h) = 𝔞_leg·(−iχ/v_h)` with `𝔞_leg` free, i.e. no value; what it asserts
is an *`h`-profile*.  (ii) ⟨1⟩2.⟨3⟩4 (ll.270–279) calls `𝔞_leg`'s
`k,h,O`-independence "the (3b) membership condition", and concedes
"`O`-independence already follows from (3a)".  But by 3a, `L` is a single
class-level function, so `𝔞_leg = i v_h L(0,h)/χ` is a property of the
*class*, not of any source: **no individual `O` can satisfy or fail 3b.**
The merged preamble still reads "`𝒮_W(ρ)` is the class of sources satisfying
all five of…", which no longer parses for 3b.  *Fix:* "…and there is a
nonzero constant `𝔞_leg` (a datum of the class, not of the source) with
`L(0,h) = 𝔞_leg(−iχ(h,0)/v_h)`; this clause asserts the `h`-profile, not a
value."  *Surviving:* the content is right and strictly weaker than frozen;
only its logical type and one clause of prose are wrong.

**m4.  Three residual no-ops in the rebuilt checker.**  (i) **C2(ii) is still
an algebraic identity in `two_s`.**  `apply_lowering` at occupation `0`
returns `sqrt((0+1)(2S−0)) = sqrt(2S)`, and the `x`-states are orthogonal, so
`norm²/N ≡ two_s` for any real `two_s ≥ 0`.  My probes: `two_s = 3.7` →
error `4.4e-16`; `two_s = 1e6` → error `0.0`; `two_s = 0.0` → error `0.0`.
The gate now *does* exercise the ladder formula (that is the real advance,
W5), but it probes **exactly one matrix element**, at `n = 0`.  My mutant
`cA_deepladder` (element scaled by `3.7` at every `n ≥ 1`, exact at `n = 0`)
**passes C2 with `max_error = 8.882e-16`** and is caught only downstream at
C3 (`1.841e+02`).  §7.3's "this is the genuine matrix element … not a
tautology" overstates.  (ii) **The momentum loop is decorative**: `k` cannot
change the answer by orthogonality; my `cB_onek` mutant (one momentum
instead of three) is green with an *identical* `max_error`.  (iii)
**`require(sp.simplify(sp.Integer(1)**p − 1) == 0)` (ll.368–370) is a gate
that cannot fail** — sympy simplifies `1**p` to `1` for every `p`.  This is
the shipped-no-op pattern in new clothes, honestly intended as a statement
of degeneracy but coded as a check.  *Fix:* extend C2's construction to a
two-magnon state so `n ≥ 1` elements are probed; delete the momentum loop or
make it test something; demote the degeneracy line from `require` to
`print`.  *Surviving:* C2's rebuild is a genuine and substantial improvement
over r1's `sites·two_s/sites − two_s`.

**m5.  C7 is unfalsifiable on this data yet is listed as having an
independent failure mode.**  `check_half_power_refuted` requires
`min_{S,N}|1/\sqrt{2SN} − 1/(2S)| > 10^{-3}`; the data's `N ∈ {60,…,480}`, so
the gate fails only if `N ≈ 2S`, i.e. `N ≲ 4`.  §7.4 l.861 lists C7 among
gates with "pairwise-independent failure modes".  Separately, a mechanism
that produces an `N`-dependent factor is refuted by `N`-independence of the
physical answer, not by a numerical near-coincidence check.  *Fix:* label C7
"display, not evidence", as C5 and the exponent fit already are.
*Surviving:* the underlying point — the S1-A critic's half-power route gives
`Z_ρ^{-1/2}`, the wrong power — is correct and is properly stated at
⟨1⟩4.⟨2⟩2.

**m6.  Resolving-power numbers are not in lockstep across three layers.**
§3 l.403 says "`±1.2%` resolving band"; §7.4 l.857 says "`±1.7%`"; the
printed interval (which I reproduce) is `[0.989, 1.017]`, i.e. `−1.1%` /
`+1.7%`, asymmetric.  *Fix:* quote the interval, not a `±`.  *Surviving:*
the interval itself is correct — I recomputed it independently as
`[0.9885, 1.0170]`.

**m7.  The disclosure's own arithmetic for the band is off.**  Response note
1 says `0.02` was "chosen as one order above the measurement scatter (max
rel. dev. `0.0043`)".  `0.02/0.0043 = 4.6`, not an order; and `0.0043` is the
residual *bias*, whereas the data's `error`/`pairwise_spread` columns give a
scatter of up to `0.048` in the same units (M3(b)(iii)).  *Fix:* state both
numbers.  *Surviving:* volunteering the post-registration at all was the
right call and is why this could be adjudicated rather than discovered.

**m8.  `theory/verdicts/soft-index-r1.md:170`** states "for **every** model
in the class, `M_2 = 2iχ k M_1 + O(k²)`, i.e. phase slope `2χ`" — a
class-level, density-free display that the merge supersedes.  Not in
§5.5.2's ERRATUM list.  *Fix:* add it.  *Surviving:* it is a verdict record,
so a pointer suffices; no edit of its content is warranted.

---

## 5.  NOTE

**n1.**  Quantifier slip between layers: ⟨1⟩3's ASSUME (β) is "**for some**
`S ∈ {1/2,1,3/2,2}`"; the `D24-VAL` row compresses this to "THEN
`𝔞_leg = 1/(2S)` … at `ρ = S ∈ {1/2,1,3/2,2}`", which reads as a universal.
One word ("for each such `S`") fixes it.

**n2.**  `𝒮_W(S)` (merge text §5.2 clause 3b, and the `D24-VAL` row) writes
the site spin into an object the same merge defines as `ρ`-indexed.  Legal
in the fully polarised register where `ρ = S` (W11), but `𝒮_W(ρ)|_{ρ=S}`
would be cleaner and would keep the fence visible at the point of use.

**n3.**  `notation.md:201` registers `ρ` as **file-local** to
`theory/spin-s-twomagnon.md` ⟨1⟩1–⟨1⟩2 (the double-occupancy coefficient) —
and that is the shard `S2-2body-S` lives in.  `D24-VAL` cites both `ρ` (as
density) and `S2-2body-S` in one row.  Pre-existing, registered, harmless
here; worth one clause in the row so a reader does not chase the wrong `ρ`.

**n4.**  Outside this lane's scope but found while grepping: the paper's
Fig-2 caption (`paper/main.tex:179, 181–182`) says "the **universal**
coefficient `2`" and "**Every** soft magnon leaves a two-site footprint,
whatever magnon it scatters off—within two-body scattering", with the model
named only as "the Heisenberg ferromagnet" and no `s`/`ρ` qualifier in the
caption.  It is unaffected by this repair (it rests on `S2-2body` via the
contact route at `main.tex:520`, not on D24(d)), and `main.tex:70–71` and
`:341` scope the constant correctly elsewhere.  A paper-lane ticket, not an
objection to this artifact.

**n5.**  §7.1's "All three hypothesis mutants now die at the **acceptance
gate**, which they reach" is true but weaker than it sounds: the candidate
exponent is consumed at exactly one call site, so reaching C6 is automatic
(W2).  It shows r1's pathology is fixed; it is not evidence that C6 is
strong.

---

## 6.  Register comparison against the nearest PROVED rows

The nearest PROVED rows are **`S2-2body-S`** (the input) and
**`M-IDX-density`** (the source of `ρ`).  `M-IDX-density`'s adjudicated
scoping sentence is the model register: hypotheses listed in full, the
load-bearing one flagged as load-bearing, `ρ` declared a free real
parameter, and an explicit fence against importing the fully polarised
gloss.

**Verdict on register: the artifact is now claiming in that register almost
everywhere, and this is the biggest single advance over r1.**  H1–H7 are
exemplary; the `definitions.md` text asserts *less* than the honest section
(it asserts no value at all), which is the correct direction and the exact
inversion of r1's monotone-strength defect.  I checked the strength profile
again layer by layer:

| Layer | What it says | Strength |
|---|---|---|
| H2 (l.734) | "MATCHED, CONDITIONAL, and RETIRED from the definition … not derived, not stipulated into the L4 file" | correct |
| ⟨1⟩3.⟨3⟩4 (l.314) | "a *conditional implication* … if (β) fails at every `S` … vacuous and fixes nothing" | correct |
| §5.2 clause 3b (l.606) | "**`𝔞_leg` is NOT fixed by this definition**" | correct |
| §5.3b `D24-VAL` | conditions displayed, both named | correct, wrong status label (M5) |
| §5.2 clause 3b (l.618) | "the frozen clause is **recovered verbatim**" at `ρ = 1/2` | **overstates (M1)** |
| ⟨1⟩2 PROVE (ii) (l.206) | "at **every** density" | **overstates (M2)** |
| §7.4 (l.852) | C6's "**evidential** gates … independent of C4" | **overstates (M3)** |

Three residual overstatements, all local, all one-sentence fixes — against
six in r1, two of which were in the text destined for `definitions.md`.  The
`ρ`-vs-`s` fence is **not** breached (W11): the artifact uses the
H-MQG(2)-sanctioned `s = ρ`, never the `d = 2s+1` gloss, and confines the
fully polarised register to the conditional row.  My r1 M5 is complied with.

---

## 7.  MERGE / HOLD, clause by clause

Apply nothing before F1 and M1 are answered; F1 needs one new sentence and
M1 needs five string replacements, so this is a work order of hours.

| § | Clause | Decision | Missing step |
|---|---|---|---|
| 5.1 | `definitions.md:931–950` — D24(c), `𝔠_h` and the ML5-A criterion | **MERGE after one edit**, in the same commit as 5.2 | Verbatim-appliable at the exact anchors; carries `𝔞_leg` into **all three** displays (933/938/945) so (c) stays internally consistent (W15); m3 genuinely dissolved — (c) mentions no `ρ`.  **Edit:** strike "the form in which D24(e) and `ml4_check.py` test it" (M1(b)(iii): both are `𝔞_leg`-blind because `M_1^O = 0`). |
| 5.2 | D24(d) preamble (`𝒮_W(ρ)`, `ρ > 0`, `Z_ρ`, ANTISYMMETRY) | **MERGE after one edit** | `Z_ρ` is correct, collision-free and in state language (W8); the `M-IDX-density` citation is complete (W9); the five-condition count is preserved and `main.tex:244` stays correct (W16).  **Edit:** add F1's amputation-convention sentence, since 3b's `𝔞_leg` is meaningless without it. |
| 5.2 | clause 1 (`E^O_desc`) | **MERGE after one edit** | m2 — amend `notation.md` overload rule 8 in the same pass, or rename outside the `E` family. |
| 5.2 | clause 2 (`Z_ρ`-linearity parenthetical) | **MERGE** | m2 of r1 is honoured: the membership condition is the model-general `2i v_h M_1^O(h)`; the `J`/`\sin h` verification is a clearly-marked parenthetical scoped to "the fully polarised spin-`S` tail" and cited to D24N-C3. |
| 5.2 | clause **3a** | **MERGE** — unconditionally, and it is the best thing in the round | M7(c) verbatim; `k ≠ 0` and the `C¹` extension both present at the point of use; nonvacuity per r1-critic V8 (W10). |
| 5.2 | clause **3b** | **HOLD** | **F1** (amputation convention undefined ⇒ `𝔞_leg` is a renaming and AMP is unstatable); **M1** ("recovered verbatim"); **m3** ("the whole of the value this clause asserts"; not a per-source membership condition). |
| 5.2 | clauses 4, 5 and the closing "no nontrivial microscopic class…" paragraph | **MERGE** | Unchanged in substance; the closing paragraph's new sentence about `tns-iu5` removing a *proof of emptiness* while supplying no member is accurate and well put. |
| 5.3a | `claims/CLAIMS.md:41` ML5-B row | **HOLD** | **M1** (the "at `ρ = 1/2` (`𝔞_leg = 1`) this is the frozen `2iχ k M_1^O` / `2χ` sites" parenthetical) and **M4** (where-proved still cites `corpus-r2.md`, which certifies the `𝔞_leg = 1` arithmetic).  Status **PROVED** is right and should stay; the deliberate exclusion of `S2-2body-S` from depends-on is correct and well-reasoned. |
| 5.3b | new `D24-VAL` row | **HOLD** | **M5** (status label, its stated justification, and the where-tested column); **n1** (∃/∀ slip). |
| 5.3c | `claims/CLAIMS.md:40` ML5-A row | **HOLD** | **M1(b)(iii)** — the false `D24(e)`/`ml4_check.py` dependency.  The "constant-agnostic" sentence is correct and I verified the proof route (evaluate at `k=0`, differentiate once, `𝔞_leg ≠ 0` suffices). |
| 5.4a | `notation.md` rows for `L(k,h)`, `Z_ρ`, `𝔞_leg`, `E^O_desc` | **`Z_ρ`: MERGE.  `L`: MERGE after one edit** (scope "Kinematic provenance: the reciprocal LSZ energy denominator" to the D6 register where the three cited sites sit — M2).  **`𝔞_leg`: HOLD** (m1).  **`E^O_desc`: MERGE after one edit** (m2). | — |
| 5.4b/c | `𝒮_W(ρ)` row (l.258) and the `𝖲` row (l.244) | **MERGE** | Both line anchors verified this round; the rename is exactly right and closes r1's M6 for `notation.md`. |
| 5.4d | overload rule 2 amendment for `χ` | **MERGE** | Correct minimal handling of a pre-existing tension; the `χ(h,k)` row at `notation.md:261` is the right authority. |
| 5.5 | ADVISORY (same-commit obligations) | **MERGE, and it is NOT optional** | Extend with M4's three sites: `theory/verdicts/corpus-r2.md:174–178`, `paper/main.tex:524–527`, `theory/verdicts/soft-index-r1.md:170`. |

**Verbatim-appliability.**  Confirmed: both REPLACE spans are exact
(`definitions.md:931`/`950` and `952`/`973`, first and last lines quoted in
W15); `claims/CLAIMS.md` ML5-A `= 40`, ML5-B `= 41`; `notation.md` `𝒮_W`
`= 258`, `𝖲` `= 244`.  The "five-condition" count survives the split and
`paper/main.tex:244` and `:542–546` both stay correct (W16).  The mechanics
are sound; it is F1's missing sentence and M1's five strings that must not
ship.

---

## 8.  `𝒮_W` nonemptiness, and the bd disposition

**`𝒮_W(ρ)` nonemptiness remains OPEN at every `ρ`, `ρ = 1/2` included.**  I
concur with §4.4 and I verified both halves: before the repair the frozen
clause forced jet `2χ` at every density (r1 V4, D24N-C1) against PROVED
`S2-2body-S`'s `χ/S` (r1 V5), so — given the bridge — the frozen class was
provably empty off `ρ = 1/2`; after the repair that proof is gone, because
the class now predicts `2χ𝔞_leg` with `𝔞_leg` free, and no source satisfying
clauses 1, 4, 5 is exhibited at any density.  The merged text retains the
"no nontrivial microscopic class has been proved…" sentence verbatim.

* **bd `tns-axg`: stays OPEN**, unchanged, and the coupling §4.4 draws to
  `D24-VAL`'s upgrade path is correct.
* **bd `tns-v44` (unified S1 r2): MAY BE UNBLOCKED on this axis**, with §5.5
  item 3's corrected instruction — the r2 shard must display `𝔞_leg` as the
  open constant citing D24(d)3b and cite `D24-VAL` for the matched value.
  That is what binding `soft-index-adjudication-r1.md` §3.3 ordered, and the
  correction of r1's instruction is right.  One rider from F1: the shard
  must not describe `𝔞_leg` as *derivable* until D24(b)'s amputation
  convention exists.
* **bd `tns-iu5`: MUST STAY OPEN — and its scope must GROW, not shrink.**  It
  cannot close on AMP alone: per F1, AMP is not yet a statable lemma.  Re-
  scope it to: "(1) fix D24(b)'s amputation convention so `𝔞_leg` is
  convention-independent; (2) then prove or refute AMP (`𝔞_leg = 1/(2ρ)`);
  (3) `D24-VAL` cannot move past its conditional status until (2) closes or
  `tns-axg` exhibits a member."  Sub-task (1) is new this round and is the
  reason a PASS is not available.

---

## 9.  Disposition and the three questions the brief asked

1. **Is the split honest, or does it relabel the stipulation?**  **Honest —
   with one string that relabels.**  The value is genuinely retired: no L4
   file will assert any value of `𝔞_leg`, the repaired class strictly
   contains the frozen one, and the merge therefore cannot install r1's
   contradiction.  That is the third horn taken in earnest.  The relabelling
   is confined to (i) the recurring "at `ρ = 1/2` the frozen clause is
   recovered verbatim" (M1), which restores `𝔞_leg = 1` by assertion at the
   one density the entire published corpus lives at, and (ii) the response
   table's "the merged definition now *agrees with* all three provenance
   sites" — it does not agree with them (they say the division leaves `2`);
   it is *consistent* with them at `𝔞_leg = 1`.  Underneath both sits F1:
   the density was moved into a constant that is not yet a well-defined
   object, so "the corpus forces this bookkeeping" is not established.
2. **Is `D24-VAL` contentful or vacuous?**  **Currently vacuous-or-unknown,
   and honestly labelled as such** — ⟨1⟩3.⟨3⟩4, §4.4 and the row itself all
   say so, so the R2-O2 pattern (which is a MAJOR only *if left silent*) is
   not repeated.  Its content is a genuine constraint on future work: any
   member of `𝒮_W(S)`, if one is ever exhibited, must have `𝔞_leg = 1/(2S)`.
   What is wrong is the status label and its justification (M5), and the
   where-tested column, which names gates that cannot test it.
3. **Was `ACCEPT_BAND = 0.02` chosen after seeing the data?**  **Yes,
   objectively** — the data was committed `2026-08-26` with "Pre-registered
   8% criteria", the band `2026-08-29` — and the disclosure of this is
   accurate and to the repair's credit.  It is **not** tuned to barely pass
   (6× margin against the `0.0033` residual) and **not** tuned to the
   discriminating mutant (any band `< 0.060` kills it).  But it **is**
   calibrated to the observed residual rather than to the evidence: it is
   1.2–2.4× tighter than the data's own quoted extrapolation error at every
   spin, so a `−3%` data perturbation well inside those error bars is
   rejected.  And the non-subsumption it buys is structurally free — any
   band below `0.08` produces it.  The acceptance test is not self-fulfilling
   in the r1 sense, but neither is it independent evidence about `𝔞_leg`;
   the substantive M3(c)(iii) demand was declined without saying so.

**Trajectory.**  r1: 3 FATAL, 7 MAJOR, 6 MINOR, 4 NOTE.  r2: 1 FATAL, 5
MAJOR, 8 MINOR, 5 NOTE — with the FATAL a newly surfaced definitional gap
(D24(b)) rather than a surviving r1 objection, and with all three r1 FATALs
and five of seven r1 MAJORs verified fixed by fresh recomputation.  The
physics is unchanged and strong; nothing in this verdict weakens it.  What
remains is one missing definitional sentence, five overstated strings, two
lockstep sites, and a certificate that should say plainly what it pins.

---

**FAIL(F1, M1, M2, M3, M4, M5)**
