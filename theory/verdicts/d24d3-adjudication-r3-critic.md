<!-- ROLE: ADVERSARIAL CRITIC verdict, round 3, on
     theory/verdicts/d24d3-adjudication-r3.md (1333 loc),
     theory/verdicts/d24d3-repair-r3-response.md (190 loc) and
     theory/checks/d24d3_normalization_check.py (559 loc), per
     briefs/critic-protocol.md + briefs/d24d3-critic-r3.md.
     Priors: -r1-critic.md (3F/7M/6m/4n), -r2-critic.md (1F/5M/8m/5n).
     WRITABLE FILE OF THIS LANE: this file only.  definitions.md,
     notation.md, claims/CLAIMS.md, the artifact and its checker were NOT
     edited; no git commit.  Everything below was recomputed. -->

# r3 critic verdict — D24(d)3 adjudication (round 3)

**Headline.  The round does what it was asked to do, and in doing it exposes
the next layer of the same defect.  All five r2 HOLD items and the r2 FATAL
are genuinely addressed *at the level at which they were raised*: a
convention now exists, the "only place it can live" argument is withdrawn
without residue, ML5-B's loss of its number is drawn and priced, the three
missed lockstep sites are added, the status labels are fixed, and the
`Q^-_k|Ω⟩ = √(Z_ρ)|k⟩` identity is exactly true — I reproduced it from
scratch at `2S = 1,2,3` on `N = 5,6` with residual `0.000e+00`.  But §5.0
normalises the **wrong half** of the object that determines `𝔞_leg`.  It
fixes the soft leg of `M_2^O` and says nothing about the soft leg inside
clause (d)2's residue — and the merged block certifies that residue with a
matrix element in the very normalisation (b) excludes.  Under the preamble's
own instruction ("All amplitudes below are in the normalisation convention
of (b)") clause 2 is false by exactly `√Z_ρ` at every `ρ ≠ 1/2`, which puts
`𝒮_W(ρ)` back to provably empty — the defect the round exists to remove,
one clause over.  Under the reading that makes ⟨1⟩4's `Z_ρ^{-1/2}` come out,
the preamble is false and ⟨1⟩0.⟨3⟩1's invariance list is wrong.  That is
F1.  It is newly surfaced, not an r2 survivor — the same shape as r2's own
FATAL.**

Secondary but load-bearing: the checker's headline claim, repeated in four
layers, that "there is **no acceptance constant** in the file", is false —
`EXPONENT_FIT_BAND = 0.03` is hand-chosen, post-registered, gates C6, and is
**strictly tighter than the derived band**: a `−3.4 %` uniform data shift,
comfortably inside the data's own quoted error, dies on it.  r2-critic
M3(b)(iii) is relocated, not fixed.  And the "real cross-momentum
orthogonality gate" is `0 ≡ 0` for every input — the fifth shipped no-op in
this corpus, shipped as the fix for the fourth.

**Trajectory.**  r1 `3/7/6/4` → r2 `1/5/8/5` → r3 `1/5/8/4`.  Flat on the
headline count, but the content moved a level down: five of r2's six items
are verified FIXED by fresh recomputation, and the r3 FATAL is a defect
r1 and r2 could not have reached because until §5.0 existed there was no
convention to be inconsistent with.

**Final line at the bottom.**

---

## 0.  What I did

Read `CLAUDE.md`, `definitions.md` D24 in full, `notation.md`,
`claims/CLAIMS.md`, the r1 and r2 critic verdicts, the r3 artifact and
response in full, the checker line by line.  Then, independently:

* built spin-`S` operators, `H_S = −JΣ_x(S_x·S_{x+1} − S²)` and the full
  Hilbert space from scratch (Kronecker products, no repo import) at
  `2S = 1,2,3`, `N = 5,6`, and tested `Q^-_k|Ω⟩ = √(Z_ρ)|k⟩` and
  `H_S|k⟩ = 2JS(1−\cos k)|k⟩`;
* computed `‖Q^-_q|h⟩‖²` analytically **and** by ED — it is `Z_ρN − 2`,
  which reproduces `ml4-ward-reduction.md` (11)'s `(N−2)` at `Z_ρ = 1`;
* computed the Ward residue against **both** soft-leg normalisations;
* recomputed every number in §3, §7, §7.5 by hand from the JSON;
* ran the checker green and all six red modes under `python3 -O`, recording
  exit paths; built 15 data mutants and 4 code mutants on copies;
* applied all three `definitions.md` REPLACE spans to a scratch copy in the
  prescribed descending order;
* grepped the whole repo for `𝒮_W`, `D24(b)`, `amputat`, and every corpus
  display of the coefficient `2`.

---

## 1.  VERIFIED CORRECT this round — fence this, do not churn it

Reproduced by me, independently.  The repair lane must not spend r4
re-establishing any of it.  (The r1 `V*` and r2 `W*` fences stand; nothing
below re-derives them.)

**X1.  `Q^-_k|Ω⟩ = √(Z_ρ)·|k⟩` is EXACT, and `|k⟩` is an exact `H_S`
one-magnon eigenvector.**  From-scratch full-Hilbert-space ED, independent
of the checker's sparse-dict code: at `2S = 1,2,3` and `N = 5,6`,
`‖Q^-_k|Ω⟩ − √(2S)|k⟩‖ = 0.000e+00` (exactly zero in floating point) and
`‖H_S|k⟩ − 2JS(1−\cos k)|k⟩‖ ≤ 3.2e-15`.  `‖S^-_x|Ω⟩‖ = √(2S)` to
`1e-16`.  D24N-C8's `1.799e-15 / 8.882e-16` reproduce.  **The identity is
not approximate.  The brief's "if the identity is only approximate the
narrowing evaporates" does not bite: it stands.**

**X2.  The refutation arithmetic, recomputed by hand from the JSON.**
Mean ansatz-free slopes `1.99914 / 0.99840 / 0.66490 / 0.49834`.
`𝔞_leg = Z_ρ^{-1/2}` ⇒ jet `2(2S)^{-1/2}`, deviations `|pred − mean|·S =
0.00043 / 0.41581 / 0.73470 / 1.00332` — margins `5.2×` and `12.5×` against
the **pre-registered** `0.08`, and `8.7×` against the worst quoted error
`0.0479`.  Frozen `𝔞_leg = 1`: `1.0016 / 2.0027 / 3.0033`, margins
`12.5–37.5×`.  Matched `1/Z_ρ`: `0.0004 / 0.0016 / 0.0027 / 0.0033`.  Every
figure in §3 and §7.1 is right.  **The refutation of the leg-normalisation
route needs no acceptance band and does not depend on any constant in the
checker.**

**X3.  The derived band.**  `max_rows |error|·S = 0.047854 → 0.0479`,
recomputed from `spin1-bc-falsifier.json` (`error ≡ pairwise_spread` in every
row).  §7.5's four-row table reproduces exactly
(`0.032025 / 0.024125 / 0.038772 / 0.047854`).

**X4.  Green and all six red modes.**  `python3 -O`, exit `0`, banner
**byte-identical** to §7.  `--red-frozen`/`--red-power`/`--red-halfpower`
exit `1` at **D24N-C6** (frozen failing first at `S = 1`, as the r1 work
order demanded); `--red-ward` at **D24N-C3** (`1.697e+01`); `--red-ladder`
at **D24N-C2** (`1.477e+06`); `--red-legfactor` at **D24N-C8**
(`5.657e+00`).  Every exit path in §7.1 is accurate.

**X5.  The three `definitions.md` spans apply cleanly.**  Anchors exact:
`923` = `**(b) Amputated amplitudes.**`, `929` = `waves are generalised
kernels …`, `931` = `**(c) The contact first jet.**`, `950` = `factorisation
with the same stated norm control.`, `952` = `**(d) The Ward-covariant
no-contact class \`𝒮_W\`.**`, `973` = `is part of the ML5-B future work.`.
Applied §5.2 → §5.1 → §5.0 to a scratch copy: **no overlap, no drift, no
hand-patching, and the result reads coherently through D24(e).**  The (b)
replacement preserves the original paragraph verbatim (header line aside),
so every corpus citation of D24(b)'s packet norm survives.

**X6.  `notation.md` anchors.**  `𝔞_α` = 55, rule 2 = 91–98, rule 8 =
123–130, rule 9 = 131–134, `𝖲` = 244, `𝒮_W` = 258, `χ(h,k)` = 261, `ρ` =
270.  Rule 12 is the last, so **13 is the next free number**.

**X7.  The `D24-VAL` status deviation is CORRECT.**  `claims/CLAIMS.md`
header, verbatim: "Authoritative L5 statuses: PROVED | SKETCH | CONJECTURE |
REFUTED.  Empirical, conditional, under-review, and future-work qualifiers
belong in prose, never as additional status values."  §5.3's refusal of my
r2 suggested label, with the qualifier moved to the statement column, is
required by L5 — my r2 wording was wrong and the lane is right to say so.
ML5-A = line 40, ML5-B = line 41.

**X8.  ML5-B survives reparametrisation, and the annotation-not-erratum call
is right.**  `ml5-universality.md` ⟨1⟩3 ⟨2⟩1.⟨3⟩2 uses only
`L(k,h) = 𝔞_leg(−iχ/v_h) + O_I(k)`, `e^{ik}−1 = ik+O(k²)` and `v_h` bounded
below; nothing evaluates `𝔞_leg`.  `corpus-r2.md:174–178`'s multiplication
`(e^{ik}−1)[−iχ/v_h][2iv_hM_1] → 2iχkM_1+O(k²)` goes through verbatim with
`𝔞_leg` carried.  So the number `2` really was a consequence of ML5-B **plus
the frozen stipulation**, PROVED correctly stays, and the promotion record
needs an annotation rather than an erratum.  This is the best-argued
decision in the round.

**X9.  The re-sourcing is real.**  `paper/main.tex:515–520` solves the
two-body contact equation `(2z_h−z_sz_h−1)s+(2z_s−z_sz_h−1)=0` directly for
a `k_s`-coefficient `2\ic` "all hard dependence cancelling"; it does not
mention D24(d).  `soft-current-recon.md` ⟨1⟩4.⟨2⟩4 gives the same `2` from
`S_{12}=e^{2ik_s+O(k_s²)}` before its Ward paraphrase.  §4.3 item 2's list
is accurate for every site it names.

**X10.  The withdrawal is complete.**  `grep` for "only place" / "must live"
/ "natural home" / "forces" over the r3 artifact returns only the
withdrawals themselves plus one legitimate symbolic "forces `p = 1`"
(⟨1⟩3.⟨3⟩3).  No downstream step leans on the retracted argument.

**X11.  C5 is subsumed by C4 in BOTH directions — stronger than the artifact
claims.**  C4 gives `|mean_S − 1/S|·S < 0.08`, which implies C5's first
`require`; and `|2 − mean_S|·S ≥ 2S − 1 − 0.08 > 0.08` for `S ≥ 1`, which
implies the second.  So C5 is unreachable for *any* data passing C4, not
merely "for the true data".  Labelling it DISPLAY is right.

**X12.  C6's exponent gain, and the correction of r2.**  Recomputed:
derived-band interval `[0.969, 1.037]` (width `0.068`), pre-registered
`[0.947, 1.062]` (width `0.115`) — ratio `1.69×`.  §7.4's "≈1.7×, smaller
than r2's claimed ≈3.5×, because that figure came from the over-tight band"
is accurate and the self-correction is to the lane's credit.

**X13.  The declared data mutants reproduce.**  `m6_shift30` (`−3 %`)
**passes** (`0.0332 < 0.0479`) exactly as §7.2 says and for exactly the
stated reason; `m2b_shift60` dies at the acceptance gate; `m7_noerror`,
`m8_errinflate`, `m9_errzero`, `m3_bandmoved`, `m4_noband`, `m5_absent`,
`m1_slope` all die at the stated gate with the stated message.

**X14.  The ladder hole is genuinely closed.**  `--red-ladder`
(`cA_deepladder`) dies at **C2**, killed by the two-independently-coded
formula cross-check at every `n ≤ 2S−1` and by the multi-quantum norms.  My
own `cE` mutant (every element `×3.7`) also dies at C2 (`2.023e+07`).
r2-critic m4(i) is answered.

**X15.  An independent confirmation of the corpus's own Ward
normalisation.**  I computed `‖Q^-_q|h⟩‖² = Z_ρN − 2` analytically and by ED
(`2S=1,2,3`; `N=5,6`; exact).  At `Z_ρ = 1` this is precisely the `(N−2)`
denominator of `ml4-ward-reduction.md` (11),
`P_{1,N}J^-_0|h⟩ = \frac{2iv(h)}{N-2}Q_0|h⟩`.  The corpus's Ward
bookkeeping is internally consistent; it is the *r3 convention* that does
not reach it (F1).

---

## 2.  FATAL

### F1.  §5.0 normalises `M_2^O`'s soft leg but not the soft leg inside clause (d)2's residue — the object that actually fixes `𝔞_leg`.  In the convention the merged preamble declares, clause (d)2 is false by exactly `√Z_ρ` at every `ρ ≠ 1/2`, so `𝒮_W(ρ)` is provably empty again; in the convention that makes ⟨1⟩4 work, the preamble and ⟨1⟩0.⟨3⟩1's invariance list are false

**(a) Location.**  Merged text §5.2, D24(d) preamble — "*All amplitudes
below are in the normalisation convention of (b); clause 3b is empty without
it.*" — against merged §5.2 clause **2** ("*Ward covariance* — the descendant
current residue factorises as `2i v_h M_1^O(h)`.  (This clause is correct at
every density: … `⟨h|Q_0^†J^-_0|h⟩ = 2i v_S(h)` … named computation
D24N-C3)") and against merged §5.0 (b) ("The soft leg enters `M_2^O` as one
additional `δ`-normalised asymptotic magnon … **not as a charge-created or
current-created vector**"; (b)(i) "`Q^-_k|Ω⟩ = √(Z_ρ)|k⟩` exactly, the two
coinciding only at `ρ = 1/2`").  Proof-side: §2 ⟨1⟩0.⟨3⟩1 ("clause 2's
residue is `2i v_h M_1^O(h)`, so it transforms with `c`.  … Clauses 1, 2, 4
and 5 are invariant (each is a homogeneous statement in one amplitude)") and
§2 ⟨1⟩4.⟨3⟩3.  Checker: `check_ward_residue_scaling`
(`d24d3_normalization_check.py` ll.242–276), whose `measured =
inner(charged, current)` uses `charged = Σ_site apply_lowering(one_magnon,
site)` — the **unnormalised charge-created** leg.

**(b) My computation.**  Two parts.

*(i) Clause 2's residue contains the soft leg, so it is not invariant.*  The
corpus defines the residue as the coefficient of `E^O_desc` **along a soft-leg
vector**: `ml4-ward-reduction.md` (11) reads
`P_{1,N}J^-_0|h⟩_N = \frac{2iv(h)}{N-2}\,Q_0|h⟩_N`, and
`ml5-universality.md` ⟨1⟩3 ⟨2⟩1.⟨3⟩1 justifies the bracket `[2iv_hM_1^O(h)]`
of (6) by "hypothesis 2 and **ML4 equation (11)**".  A coefficient along a
vector changes when the vector is renormalised.  I measured both readings at
`N = 8`, `J = 1`, `h = π/4` and `3π/4`, `2S = 1,2,3,4`:

| `2S` | `⟨Q_0h\|J^-_0\|h⟩` (charge-created leg) | `2i·Z_ρ·J\sin h` | same residue against the **(b)** leg `Q_0/√Z_ρ` | `2i·√Z_ρ·J\sin h` | `‖Q_0\|h⟩‖²` | `Z_ρN−2` |
|---|---|---|---|---|---|---|
| 1 | `+1.414214i` | `+1.414214i` | `+1.414214i` | `+1.414214i` | 6 | 6 |
| 2 | `+2.828427i` | `+2.828427i` | **`+2.000000i`** | `+2.000000i` | 14 | 14 |
| 3 | `+4.242641i` | `+4.242641i` | **`+2.449490i`** | `+2.449490i` | 22 | 22 |
| 4 | `+5.656854i` | `+5.656854i` | **`+2.828427i`** | `+2.828427i` | 30 | 30 |

So: **`⟨h|Q_0^†J^-_0|h⟩ = 2i v_S(h)` is `Z_ρ`-linear only against the
charge-created leg.  Against the `δ`-normalised asymptotic leg that §5.0
mandates, the same residue is `√Z_ρ`-linear, i.e. `2i v_h/√Z_ρ` — equal to
`2i v_h` only at `ρ = 1/2`.**  D24N-C3, which merged clause 2 cites as
certifying "this clause is correct at every density", is computed in the
normalisation §5.0 explicitly excludes.

Hence ⟨1⟩0.⟨3⟩1's "Clauses 1, 2, 4 and 5 are invariant (each is a
homogeneous statement in one amplitude)" is **false for clause 2**: clause 2
equates the residue of `E^O_desc ⊂ M_2` (scaling with `c′`) to the literal
`2i v_h M_1^O` (scaling with `c`), so it transforms as `c′/c` — it is the
one clause that is *not* homogeneous in one amplitude.

*(ii) The trilemma.*  With that established, exactly one of three readings
must be chosen, and the merged text picks none of them:

- **Literal, per the preamble** (clause 2 holds *in the (b) convention*):
  then in the fully polarised spin-`S` register a candidate member's residue
  is `2iv_hM_1^O/√Z_ρ ≠ 2iv_hM_1^O`, by an `O`-**independent** factor, so no
  source can satisfy clause 2 at `ρ ≠ 1/2`.  **`𝒮_W(ρ)` is provably empty at
  every `ρ ≠ 1/2` again** — the exact defect `tns-iu5` exists to remove,
  reinstated one clause over, and this time *without* needing the bridge
  (α), because it is a failure of a membership condition rather than a jet
  collision.
- **Shape** (clause 2 asserts only `residue ∝ v_h M_1^O`, overall constant
  absorbed into `L`): then the split between clause 2's constant and
  `𝔞_leg` is exactly the freedom §5.0 was supposed to remove, `𝔞_leg` is
  again fixed only relative to a choice, and **r2-critic F1 survives
  verbatim** — a soft-leg convention cannot pin a ratio whose denominator is
  also convention-relative.
- **Normalisation-fixing** (clause 2 *defines* the leg normalisation by
  demanding the residue be exactly `2i v_h M_1^O`): then `𝔞_leg = 1` by
  construction, `D24-VAL` is refuted rather than open, and the frozen clause
  is restored.

⟨1⟩4's `𝔞_leg = Z_ρ^{-1/2}` follows **only** from the *mixed* reading —
clause 2's residue in the charge-created normalisation, `E^O_desc` in (b)'s
— which is the one the preamble's own sentence forbids.  So the round's
sharpest result and its FATAL repair are in direct tension, and the tension
is invisible at `ρ = 1/2`, where `√Z_ρ = Z_ρ = 1`.

**(c) FIX DEMAND.**  In merged clause (d)2, state the normalisation the
residue is measured in — "*the residue is quoted against the charge-created
soft leg `Q_0|h⟩`, not against (b)'s asymptotic leg; the two differ by
`√Z_ρ` (b)(i), and that mismatch is what the (d)3b constant records*" —
delete the preamble's blanket "All amplitudes below are in the normalisation
convention of (b)", correct ⟨1⟩0.⟨3⟩1's invariance list to "clauses 1, 4, 5
are invariant; clause 2 transforms as `c′/c` and is the second half of the
convention", and derive `𝔞_leg = Z_ρ^{-1/2}` in one step from the
numerator/denominator mismatch instead of presenting it as an independent
"mechanism".

**(d) SURVIVING WEAKER STATEMENT.**  *The (3a) quotient with its **literal**
denominator `(e^{ik}−1)·2iv_h·M_1^O(h)` is well posed and covariant exactly
as ⟨1⟩0.⟨3⟩1 says (that part is unaffected: `v_h` and `M_1^O` carry no soft
leg).  `Q^-_k|Ω⟩ = √(Z_ρ)|k⟩` is exact (X1).  And IF clause 2's residue is
read in the charge-created normalisation while `E^O_desc` is read in (b)'s,
then `𝔞_leg = Z_ρ^{-1/2}` and the ansatz-free data refutes it at 5–12×
(X2).  What does not survive is the claim that §5.0 as written makes
`𝔞_leg` a determined number, the claim that clause 2 is normalisation
invariant, and the preamble sentence that puts all five clauses in one
convention.*

---

## 3.  MAJOR

### M1.  The convention's referent does not exist off the fully polarised family, and D12(b) — the authority cited for it — explicitly declines to supply the normalisation it is cited for

**(a) Location.**  Merged §5.0, (b) convention paragraph 1: "Both amplitudes
are taken against asymptotic one-magnon kernels normalised by
`⟨k|k′⟩ = 2πδ(k−k′)`, inside the corpus's packet discipline (D3(a); the
`ℓ¹∩BV` packet class of D12(a′); **the fixed-`k` reading of D12(b)**)."
Echoed at §2 ⟨1⟩0.⟨3⟩3 and in H2.

**(b) My computation.**  I read `definitions.md` D12(b) in full.  It is a
statement about the **gauge remainder** of the MPS tangent vector
`|Φ_f^Λ(B)⟩ = Σ_n f(n)|ψ_Λ(…B@n…)⟩` at `f(n) = e^{ikn}`: `‖𝔅_Λ‖ = O(1)`
uniformly, hence `‖|Λ|^{-1/2}𝔅_Λ‖ → 0`.  It fixes **no inner product and no
state norm**, and it goes out of its way to withdraw the only norm statement
it ever made: "*No claim is made, or needed, about how the bulk term grows;
the r2 assertion `‖bulk‖ = Θ(|Λ|^{1/2})` is withdrawn*", with an explicit
counterexample at `χ = 1`.  So D12(b) is cited as the authority for
`⟨k|k′⟩ = 2πδ(k−k′)` and is precisely the definition that refuses to say it.
D3(a) and D12(a′) are packet-class statements and fix no normalisation
either.

Where *is* the referent constructed?  Only in the fully polarised spin-`S`
ferromagnet, by D24N-C8 itself: `|k⟩ = Σ_x e^{ikx}|x⟩`, `⟨k|k′⟩ = Nδ_{kk′}`.
At general `ρ` the corpus has no asymptotic one-magnon state at all —
`claims/CLAIMS.md` ML1 ("Conjectured two-magnon wave operators and channel
norm on packets") is **CONJECTURE, future work, no shard, no test**.

So the answer to the brief's question is: **fixing `c′(0)/c = 1` makes
`𝔞_leg` a number exactly where the `δ`-normalised asymptotic one-magnon
kernel is constructed — the fully polarised spin-`S` family — and relocates
the arbitrariness into the unconstructed kernel everywhere else.**  It is
real progress on the register where the corpus computes, and it is not the
`ρ`-general statement H2 and the merged text assert.  (A residual phase
freedom `e^{iθ(k)}` on the kernel also leaves only `|𝔞_leg|` pinned; in the
spin-`S` register the origin choice fixes it, `θ(0) = 0`, because a lattice
translation multiplies `|k⟩` by `e^{ika} → 1` at `k = 0`.  Off that register
there is nothing to fix it against.)

**(c) FIX DEMAND.**  Replace the D12(b) citation with an honest one — "*in
the fully polarised spin-`S` register the kernel is `|k⟩ = Σ_x e^{ikx}|x⟩`
(D24N-C8); in any other register the existence of the asymptotic one-magnon
kernel is claim `ML1` (CONJECTURE), and `𝔞_leg(ρ)` is defined only where
that kernel is*" — and add the same scoping clause to the `𝔞_leg(ρ)` row of
§5.4a beside "defined only when that class is nonempty".

**(d) SURVIVING WEAKER STATEMENT.**  *In the fully polarised spin-`S`
family the convention is fully explicit, the kernel is exhibited, and
`𝔞_leg(S)` is a determined number given a class member — which is exactly
the register in which `D24-VAL`, ⟨1⟩4 and the whole certificate live.  The
convention's `ρ`-general reading is not available and should not be
asserted.*

---

### M2.  "There is no acceptance constant in the file" is false.  `EXPONENT_FIT_BAND = 0.03` is hand-chosen, post-registered, GATES C6, and is strictly TIGHTER than the derived band — so r2-critic M3(b)(iii) is relocated, not fixed

**(a) Location.**  `theory/checks/d24d3_normalization_check.py` l.57
(`EXPONENT_FIT_BAND = 0.03`) and ll.374–376
(`require(abs(exponent − 1.0) < EXPONENT_FIT_BAND, …)`) — a `require`, i.e.
`SystemExit(1)`, inside `check_exponent`, which the banner prints as
"D24N-C6 part 2".  Against: artifact §0 (R3-d) "*there is no acceptance
constant left in the file — §7.5*"; §3 "***the acceptance band is derived at
runtime … there is no hand-chosen band in the file***"; §7.5 "*There is now
**no acceptance constant in the file**.*"; H7 "*the acceptance band is now
that error rather than a chosen number*"; response §5 disclosure 6.

**(b) My computation.**  For a uniform data shift by `(1−δ)`:

* the derived acceptance gate fires at `δ > 0.0479` (dev`·S = δ` exactly);
* the exponent gate fires at `0.8806·\log\frac1{1-δ} > 0.03`, i.e.
  `δ > 0.0335` (design `Σ\log 2S = 3.178`, `Σ\log²2S = 3.609`).

So the hand-chosen constant binds first.  Verified by data mutants on
copies:

| mutant | exit | died at |
|---|---|---|
| `m_shift30` (`−3.0 %`) | 0 | passes, as §7.2 says |
| **`m_shift34` (`−3.4 %`)** | **1** | **`D24N-C6 fitted exponent 1.032853 is not 1 (band 0.03)`** |
| **`m_shift40` (`−4.0 %`)** | **1** | **`D24N-C6 fitted exponent 1.038339 is not 1 (band 0.03)`** |
| `m_shift45` (`−4.5 %`) | 1 | `D24N-C6 … acceptance band (0.0479) at S=2.0 dev=0.0482` |

A `−4 %` uniform shift is **inside the data's own quoted extrapolation error
at `S = 2`** (`0.0479` in the checker's units) and is rejected — which is
verbatim r2-critic M3(b)(iii) ("a gate that rejects data drawn within its own
stated uncertainty is not calibrated to the evidence").  The band that does
the rejecting was committed this round and is not derived from anything.

Worse, the constant is doing the *load-bearing* work: my combined mutant
`m_errwide_shift60` (one `S = 1/2` error entry raised to `0.1579`, so the
derived band becomes `0.0790 < 0.08` and the subsumption guard stays silent,
plus a `−6 %` shift) passes the *derived* gate and dies at
`fitted exponent 1.056878 is not 1 (band 0.03)`.  The checker's advertised
"no constant" architecture is being rescued by the constant it says it does
not have.

**(c) FIX DEMAND.**  Either derive the exponent band from the data too
(propagate the same `error` column through the `\log` fit, giving a band
`≈ 0.88·\log(1+0.0479) ≈ 0.042`), or keep `0.03` and declare it in §7.5 and
H7 as "*a hand-chosen, post-registered exponent band, currently the tightest
gate in the file and tighter than the data's own quoted error*" — and strike
"there is no acceptance constant in the file" from all four layers.

**(d) SURVIVING WEAKER STATEMENT.**  *Replacing `ACCEPT_BAND` with a
data-derived band is a genuine improvement and it does fix the specific
`−3 %` mis-calibration; the guards for zero and missing error columns are
real (X13).  But the file still contains a hand-chosen acceptance constant,
it still rejects perturbations inside the data's own error bars, and every
substantive conclusion — the two refutations — needs neither band, at
`5–37×` margins against the pre-registered `0.08` (X2).*

---

### M3.  The "real cross-momentum orthogonality gate" is `0 ≡ 0` for every input, and `cB_onek` is killed only by `require(len([a,b,c]) >= 3)` — a constant-true assertion.  Fifth shipped no-op, shipped as the fix for the fourth

**(a) Location.**  `d24d3_normalization_check.py` ll.211–241, sub-gate
C2(iv); the guard at ll.216–218; artifact §0 (R3-d) "*the decorative momentum
loop replaced by a **real** cross-momentum orthogonality gate (kills
`cB_onek`)*"; §7.3 row `cB_onek`; §7.4 "*Residual no-op audit (r2-critic m4,
**all three closed**)*"; response table m4(ii) "*so `cB_onek` dies at C2*".

**(b) My computation.**  Two probes on copies.

*(i) The orthogonality term is zero by construction.*  The `|x⟩` states are
orthonormal for distinct `x`, so
`⟨charged_i|charged_j⟩ = |element|²Σ_x e^{i(k_j−k_i)x} = 0` for any distinct
commensurate momenta and **any** ladder element whatsoever.  I re-ran the
sub-gate with the element scaled by `1.0, 3.7, −5.0, 10⁶`:

```
scale=1.0      orthogonality residual = 1.093e-15
scale=3.7      orthogonality residual = 1.431e-14
scale=-5.0     orthogonality residual = 2.562e-14
scale=1e6      orthogonality residual = 1.202e-03   (float overflow only)
```

Nothing moves.  It is the r1 `sites·two_s/sites − two_s ≡ 0` pattern in new
clothes.

*(ii) The guard is a compile-time constant.*  `momenta` is the literal
`[2πj/sites for j in (0,1,2)]`; `require(len(momenta) >= 3, …)` is
`3 >= 3` — it cannot fail on any input, only on an edit of the literal it
asserts about.  Mutant `cD_onek_noguard` (one momentum **and** the guard
deleted) exits **0** with `D24N-C2 … max_error=1.137e-13` — *identical to
green*.  So the entire kill of `cB_onek` is the self-referential length
assertion.

**(c) FIX DEMAND.**  Delete the orthogonality sub-gate and the length
`require`, and state in §7.4 that `cB_onek` is not caught by C2 at all
(it changes no measured quantity) — or replace it with a test that can fail:
overlaps of **two-magnon** charged states, where the ladder at `n ≥ 1` and
the coincidence term make orthogonality a real constraint.

**(d) SURVIVING WEAKER STATEMENT.**  *r2-critic m4(i) and m4(iii) ARE closed
— the two-formula ladder cross-check at every `n ≤ 2S−1` and the
multi-quantum norms are genuine and `--red-ladder` proves it (X14), and the
`1**p − 1` non-gate is deleted.  Only m4(ii) is unclosed, and §7.4 must say
"two of three" rather than "all three".*

---

### M4.  The `𝒮_W → 𝒮_W(ρ)` rename is a lockstep obligation at 18 sites; §4.2/§5.5 list 5.  Two of the 13 omissions are inside `definitions.md` itself, and after the merge that L4 file uses a symbol `notation.md` no longer registers

**(a) Location.**  §5.4b (replaces the `𝒮_W` row at `notation.md:258` with
`𝒮_W(ρ)`); §4.2 and §5.5 item 2, which list only `TRIANGLE.md:24, 215, 254,
257, 528`; §4's opening "*Every address below was obtained by grep this
round*".

**(b) My computation (grep, whole repo, excluding this round's own
verdicts).**  `𝒮_W` is live at:

| file | lines | in §4.2/§5.5? |
|---|---|---|
| `definitions.md` | **916** (the D24 section header), **1004** (D25) | **no** |
| `claims/CLAIMS.md` | **29** (S-general row), **82** | **no** |
| `theory/ml5-universality.md` | **133, 141, 152, 159, 197** | **no** |
| `paper/main.tex` | **245, 252, 542, 556** | **no** |
| `theory/TRIANGLE.md` | 24, 215, 254, 257, 528 | yes |
| `notation.md` | 244, 258 | yes (§5.4b/c) |

W12 fenced `ml5-universality.md` for **constant-bearing** strings only and
W13 fenced five specific `TRIANGLE.md` lines; neither fences the rename.  So
this is new, not churn.  After the merge `definitions.md` contains bare
`𝒮_W` twice while `notation.md`'s only row is `𝒮_W(ρ)`, and `notation.md`'s
own closing rule reads "*a symbol used anywhere without an entry here is a
defect*".  Unlike `𝔞_leg`, whose bare form is licensed by the new overload
rule 13, nothing licenses bare `𝒮_W`.  This is a merge-mechanics MAJOR, not
a truth MAJOR: nothing becomes false, but the orchestrator has said they
will not hand-patch an L4 file, and this commit leaves that file
self-inconsistent.

**(c) FIX DEMAND.**  Cheapest: add one clause to §5.4b's row — "*written
bare `𝒮_W` where the density is fixed or immaterial (D24 header, D25,
`ml5-universality.md`, the Letter)*" — which makes all 13 sites legal
untouched; otherwise add the 13 sites to §5.5 as same-commit edits.

**(d) SURVIVING WEAKER STATEMENT.**  *Indexing the class by `ρ` is the right
move and the `notation.md` row text is correct; W12/W13's completeness
findings stand for what they covered.  Only the rename's own blast radius
was not computed.*

---

### M5.  The new `AMP` row asserts a value for a quantity its own definition leaves undefined, at densities where its subject has no referent

**(a) Location.**  §5.3c, the `AMP` row: "*charge-created soft-leg
amputation contributes the per-site order-parameter density `Z_ρ = 2ρ` to
the external flux, i.e. `𝔞_leg(ρ) = 1/Z_ρ` **UNCONDITIONALLY** — without the
D24-VAL bridge and **without assuming a class member***".  Against §5.2
clause 3b ("*`𝔞_leg(ρ)` is a datum of the class `𝒮_W(ρ)` … **defined only
when that class is nonempty***"), §5.4a's `𝔞_leg(ρ)` row (same), and §2
⟨1⟩2.⟨3⟩5 ("*If `𝒮_W(ρ) = ∅` … `𝔞_leg(ρ)` is undefined, not free*").

**(b) My computation.**  Straight quantifier audit.  `AMP` is
`∀ρ : 𝔞_leg(ρ) = 1/Z_ρ`.  Its subject term `𝔞_leg(ρ)` is, by the same
merge, a partial function: undefined when `𝒮_W(ρ) = ∅` (open at every `ρ`,
§4.4) and — per M1 — additionally undefined wherever the (b) kernel is not
constructed, i.e. everywhere except the fully polarised spin-`S` family.
So the row asserts an equation both of whose sides may be undefined, at
densities where one of them provably has no referent, and it says
"without assuming a class member" *as though that were a strength*.
Everything that motivates it — ⟨1⟩4, D24N-C8, `soft-index-r1.md` F1(c)(i) —
lives at `ρ = S ∈ ½ℤ`.  **This is r2-critic M2's quantifier defect,
rescoped out of ⟨1⟩2 and re-installed in a new DAG row.**  The lane's own
response §6 item 3 predicted exactly this and it is what happened.

(For the record, on the response's item 4: `D24-VAL` and `AMP` are **not**
one claim split in two and the DAG does not double-count — `AMP` drops (α),
which is a real difference.  It is only the quantifier and the
"without assuming a class member" clause that are wrong.)

**(c) FIX DEMAND.**  Restate: "*for every `ρ` at which `𝒮_W(ρ) ≠ ∅` and the
D24(b) asymptotic one-magnon kernel exists (currently: the fully polarised
spin-`S` family, D24N-C8), `𝔞_leg(ρ) = 1/Z_ρ`, without the (α) bridge*", and
add the same vacuous-or-unknown sentence `D24-VAL` already carries.

**(d) SURVIVING WEAKER STATEMENT.**  *Giving AMP its own row, with the
⟨1⟩4 fence quoted in it, is the round's best structural move and is exactly
where the open content belongs; the row's `CONJECTURE` status and its
where-tested column are right.  Only its quantifier and its
"without assuming a class member" clause overreach.*

---

## 4.  MINOR

**m1.  ⟨1⟩4.⟨3⟩1's "exact, `k`-independent, `N`-free per site" is true of
the vacuum leg and not of the leg it is applied to.**  ⟨1⟩4.⟨3⟩3 converts
`M_2^O` and (implicitly) clause 2's residue, whose soft leg is `Q_0` acting
on the **one-magnon** state, not on `|Ω⟩`.  I computed, analytically and by
ED (`2S = 1,2,3`; `N = 5,6`; exact): `‖Q^-_q|h⟩‖² = Z_ρN − 2`, so per site
`Z_ρ − 2/N` — the conversion factor there is `√Z_ρ\sqrt{1 − 1/(SN)}`, not
`√Z_ρ`.  It is exactly `√Z_ρ` only in the `N → ∞` LSZ limit, and D24N-C8
tests only the vacuum case.  *Fix:* say "exact on the vacuum leg; on the
descendant leg the same factor holds up to `O(1/(Z_ρN))`, vanishing in the
LSZ limit (`‖Q^-_q|h⟩‖² = Z_ρN − 2`)".  *Surviving:* the conclusion is
unaffected — the correction is `≤ 1/(2SN) ≈ 10^{-2}` at the data's smallest
`N = 60`, against a refutation margin of `5–12×`.

**m2.  The over-wide-error guard is one-sided, and the band statistic is the
loosest available.**  `derive_accept_band` only refuses a band `≥ 0.08`.  My
mutant `m_errwide` (one `S = 1/2` row's `error → 0.1579`) yields band
`0.0790`, exits **0**, and still prints "*so C6 is not subsumed by C4*" — a
single corrupted entry silently loosens the acceptance gate by `1.65×` to
within `1 %` of C4.  Separately, the band is `max` over **all rows and all
spins**, gating a **per-spin mean**: with three rows per spin the mean's
uncertainty is smaller than the worst row's by `≈√3`, and the `S = 2`
row sets the band that gates `S = 1/2`.  Deriving the band from the data
replaced a hand-chosen *constant* with a hand-chosen *statistic*, and it is
the loosest of the natural ones.  *Fix:* per-spin band from the rows at that
spin, aggregated to match the gated statistic; and cap or flag any band more
than (say) `2×` the median.  *Surviving:* the direction is right and the
zero/missing guards are real (X13); no conclusion changes, because the true
`max_rel_dev` is `0.0033`.

**m3.  `notation.md`'s merge mechanics are not stated and the written order
breaks its own anchors.**  §5's Mechanics paragraph gives descending-line-
order only for `definitions.md`, then lists `notation.md` anchors (`rule 2 at
91–98, rule 8 at 123–130, rule 9 at 131–134`) as if stable.  §5.4d appends
`≈4` lines at rule 2 (l.98), after which rule 8 is at `127–134` and §5.4e's
stated anchor is wrong; §5.4f's "after rule 12" (l.145) drifts likewise.
*Fix:* one sentence — "apply §5.4 in descending line order: a/b (258), c
(244), f (after 143), e (123–130), d (91–98) — or match on quoted first
lines".  *Surviving:* every individual anchor is correct **before** any edit
(X6); only the ordering instruction is missing.

**m4.  The D24(b) blast radius was never computed.**  §4.3 corrects "D24(a),
(b) untouched" but lists no site that cites D24(b).  Two matter.  (i)
`theory/ml4-ward-reduction.md:63–68`: "*An **ML4-admissible analytic
amputation at fixed `N`** may multiply (3), on either side, by operator
families bounded and `C¹` for `|k| ≤ ε_I`*" — a freedom strictly **wider**
than §5.0, which forbids any `λ(0) ≠ 1`.  Post-merge a reader of that shard
draws a false conclusion about D24(b) amplitudes.  (ii)
`theory/ansatz-scattering-2m.md:614, 621–631`: "*D24(b)'s normalized packet
multiplier convention … the packet-amputated datum is
`A(ε)(h)=∫dμ_f(u)S_phys(εu,h)` … **the normalized multiplier amputation of
D24(b)***" — an amputation under which the amputated datum **is** the
physical multiplier, i.e. precisely the convention ⟨1⟩0.⟨3⟩6 says §5.0
refuses.  It is harmless only because that shard is D6, where the two
coincide.  So the honest answer to "is §5.0 consistent with every existing
corpus use of *amputated*?" is: **yes, but only because every existing use
sits at `ρ = 1/2`.**  *Fix:* add both to §4.3 with that sentence, and note
in §5.0 that it narrows the ML4-admissible class.  *Surviving:* no existing
site becomes false and the (b) replacement preserves the packet-norm
paragraph verbatim (X5), so every `D24(b)` citation for the norm survives.

**m5.  §7.4's "Every gate is reachable" contradicts its own first bullet.**
C1 is declared unreachable by any runtime mutation two bullets earlier; C5
is unreachable for *all* data passing C4 (X11); C7 is declared unfalsifiable
on this data.  Three of the eight gates cannot fire.  *Fix:* "every gate
that is offered as evidence (C2, C3, C4, C6, C8) is reachable; C1, C5 and C7
are labelled GUARD/DISPLAY precisely because they are not".  *Surviving:*
the substantive claim — that r1's reachability pathology is gone and the
candidate exponent is consumed at exactly one call site — is true (W2, and I
re-read `main()`).

**m6.  H8's price list is incomplete: `𝔠_h` itself becomes untestable.**
After §5.1, `𝔠_h(O) := ∂_kM_2^O|_0 − 2i𝔞_leg χ M_1^O(h)` contains an open
constant, so for **every** source with `M_1^O ≠ 0` the ML5-A membership test
is undecidable until AMP or `tns-axg` closes.  §4.3/H8 record only that
ML5-B predicts no number; they do not record that D24(c)'s obstruction
becomes unevaluable.  *Fix:* one sentence in H8.  *Surviving:* the
`𝔞_leg`-blindness of D24(e) and `ml4_check.py` is real and W14-fenced — those
counterexamples have `M_1^O = 0` — so no existing test breaks.

**m7.  Off-by-one across layers on the C2 ladder range.**  §0 (R3-d): "*to
every occupation `n ≤ 2S`*".  Code (l.198): `for occupation in
range(two_s)`, i.e. `n ≤ 2S−1`; the docstring says `2S-1`.  `n = 2S` would be
`S^-|m=−S⟩ = 0`, so the code is right and §0 is wrong.  *Fix:* one
character.  *Surviving:* the gate is correct as coded.

**m8.  §4.2's "`TRIANGLE.md` … no constant displayed (W13)" over-reads
W13.**  W13 fenced lines 24/215/254/257/528.  The SCOPE paragraph at
`TRIANGLE.md:212–219` displays `𝖲(k_s) = 2ik_s` and labels it "**SKETCH**,
conditional on wave operators (ML1) and **the amputation convention**" —
a constant, and a condition that §5.0 now partly discharges in a way that
changes what the conditional says off `ρ = 1/2`.  *Fix:* add
`TRIANGLE.md:216–218` to §4.3's re-sourced list with the one-clause scoping
the paper's `:524–527` gets.  *Surviving:* the site is D6 and stays
numerically correct; W13's five lines are exactly as fenced.

---

## 5.  NOTE

**n1.**  D24N-C8's content beyond fenced r1-critic V1 (`‖Q^-_k|Ω⟩‖²/N = 2S`)
is the *direction* — that the vector is proportional to `|k⟩`, not merely of
that norm — plus the standard fact that `|k⟩` diagonalises the one-magnon
block.  Both are true and both are one-liners.  "The sharpest thing in the
round" is generous, though the *use* made of it is genuinely new.

**n2.**  `paper/main.tex:244–249` identifies `thm:soft` as "*its proved
two-body instance, `𝖲 = 2\ic k_s`*" of the class-level conjecture on `𝒮_W`.
Post-merge that identification silently needs `𝔞_leg(1/2) = 1`, which no L4
file supplies.  The Letter stays correct because `thm:soft` rests on the
contact route (X9), but §4.3 item 3 should say so rather than only that the
warrant "moves".

**n3.**  Response disclosure 5's worry about C8's `1e-10` thresholds is
unfounded: the true residuals are `1e-15`, and the nearest competing
hypothesis (`Z_ρ` vs `√Z_ρ`) differs by `O(1)` — `--red-legfactor` reports
`5.657e+00`.  Nothing can hide there.

**n4.**  `m6_shift30` passing is correct and *is* the calibration fix, as
claimed — but see M2: its neighbour at `−3.4 %` dies on the undeclared
constant, so the demonstration proves less than §7.2 says it does.

---

## 6.  Register comparison

Nearest PROVED row: **`S2-2body-S`**, whose adjudicated scoping sentence is
the corpus standard — "*PROVED per spin-s-r1.md adjudication: proves the
unit-charge exact two-body slope only; it does not prove endpoint or
equal-velocity limits, spin-`S` Bethe completeness, S-general, the memory
half, the `|q_hard|>1` factor, or Conjecture Bc*": say exactly what is
proved, then enumerate by name what is not.

**Verdict on register: H1–H9 are in that register, and H8 (the loss) and
⟨1⟩4.⟨3⟩6 (the honest fence on the new result) are the two best paragraphs
this campaign has produced on a repair round.**  Four localised departures,
three of which land in text destined for an L4 file:

| Layer | What it says | Strength |
|---|---|---|
| H8 / §4.3 | "ML5-B predicts no number at any density, `ρ = 1/2` included" | correct, and volunteered |
| ⟨1⟩4.⟨3⟩6 | "does not prove AMP, does not refute it, does not exhibit a member" | correct |
| §5.2 preamble | "All amplitudes below are in the normalisation convention of (b)" | **false for clause 2 (F1)** |
| §5.0 / H2 | `δ`-normalised kernel "of D12(b)"; "makes `𝔞_leg` a number" | **overstates (M1)** |
| §3 / §7.5 / H7 / §0 | "no acceptance constant in the file" | **false (M2)** |
| §5.3c `AMP` | `𝔞_leg(ρ) = 1/Z_ρ` unconditionally at every `ρ` | **overstates (M5)** |

Reliance audit: **clean.**  No REFUTED row; no use of ML4-Ward's `n ≥ 2`
second display (the artifact's only ML4 contact is via ML5-B hypothesis 2 at
one hard magnon, i.e. eq. (11)); Bethe enters only as the declared-unproved
bridge (α) built on `S2-2body-S`, which is PROVED without integrability; and
`𝒮_W(ρ)` nonemptiness is never assumed — it is a displayed hypothesis
`(β_S)` and §4.4 keeps it open.

---

## 7.  MERGE / HOLD, clause by clause

Apply nothing until F1 is answered: F1 is one sentence to delete, one
sentence to add to clause 2, and one corrected list in ⟨1⟩0.⟨3⟩1 — hours,
not a round.

| § | Clause | Decision | Missing step |
|---|---|---|---|
| **5.0** | D24(b) — the convention | **HOLD** | **F1** (the convention does not reach clause 2's residue) and **M1** (D12(b) mis-cited; no referent off the spin-`S` family).  Paragraph 1 is byte-preserving and correct (X5); the covariance display `𝔞_leg ↦ (c′(0)/c)𝔞_leg` is correct; (b)(i)'s `Q^-_k\|Ω⟩ = √(Z_ρ)\|k⟩` is exact (X1). |
| 5.1 | D24(c), 931–950 | **MERGE after F1** | Verbatim-appliable at the exact anchors; carries `𝔞_leg` into all three displays (W15); the false D24(e)/`ml4_check.py` clause is struck (M1(b)(iii) honoured).  Cannot ship before 5.0 — see m6 for the one sentence H8 owes it. |
| 5.2 | D24(d) preamble | **HOLD** | **F1** (strike "All amplitudes below are in the normalisation convention of (b)"); **M4** (`𝒮_W` rename).  `Z_ρ`, `ρ > 0`, ANTISYMMETRY and the five-condition count are correct and W8/W9/W16-fenced. |
| 5.2 | clause 1 (`E^O_desc`) | **MERGE** with §5.4e | m2 of r2 honoured. |
| 5.2 | clause **2** | **HOLD** | **F1** — the displayed residue and its D24N-C3 certification are in the charge-created normalisation, which (b) excludes; state the normalisation in the clause. |
| 5.2 | clause **3a** | **MERGE — unconditionally** | Unchanged; M7(c) verbatim; W10-fenced; the best text in the file. |
| 5.2 | clause **3b** | **HOLD** | **F1** (the constant it names is not determined by §5.0 alone) and **M1** (definedness).  The `h`-profile restatement is right and dissolves r2's m3 (X10); "recovered verbatim" is gone; "this definition fixes no value at any density, `ρ = 1/2` included" is correct and is the round's central honest sentence. |
| 5.2 | clauses 4, 5, closing paragraph | **MERGE** | Unchanged in substance; the closing `tns-iu5` sentence is accurate. |
| 5.3a | ML5-B row | **MERGE after F1** | Status PROVED is right; the reparametrisation argument is correct and I verified it at the shard (X8); the `S2-2body-S` exclusion from depends-on is right; the `corpus-r2.md` annotation pointer is the correct disposition. |
| 5.3b | new `D24-VAL` row | **MERGE after F1** | M5 of r2 honoured in the only way L5 permits (X7); n1/n2/n3 honoured; where-tested now names what the gates can and cannot do — and is accurate, including "neither antecedent is tested by any gate". |
| 5.3c | new `AMP` row | **HOLD** | **M5** (unconditional `ρ`-quantifier; "without assuming a class member").  The ⟨1⟩4 fence inside the row is excellent and should survive the rewrite verbatim. |
| 5.3d | ML5-A row | **MERGE** | Constant-agnostic sentence verified at the shard; the false D24(e)/`ml4_check.py` dependency is struck. |
| 5.4a | `L(k,h)` row | **MERGE after F1** | Correct, including "Normalisation-dependent: `L ↦ (c′/c)L`" and the D6-scoping of the provenance. |
| 5.4a | `Z_ρ` row | **MERGE** | W8-fenced; collision-free. |
| 5.4a | `𝔞_leg(ρ)` row | **HOLD** | **M1** — add "and only in a register where the D24(b) kernel is constructed" beside "defined only when that class is nonempty". |
| 5.4a | `E^O_desc` row | **MERGE** with §5.4e | m2 of r2 honoured. |
| 5.4b | `𝒮_W(ρ)` row | **HOLD** | **M4** — one clause licensing bare `𝒮_W`, or 13 same-commit edits. |
| 5.4c | `𝖲` row cross-ref | **MERGE** | Anchor 244 verified. |
| 5.4d | overload rule 2 amendment | **MERGE** | Correct minimal handling; see **m3** for ordering. |
| 5.4e | overload rule 8 amendment | **MERGE** | The `:146` line correction is right (I re-verified: `ansatz-scattering-2m.md:146`). |
| 5.4f | new overload rule 13 | **MERGE** | 13 is the next free number (X6); the correction of r2's false rationale ("`𝔞_α` is itself subscripted") is right and is my error, correctly caught. |
| 5.5 | ADVISORY items 1–9 | **MERGE, and NOT optional; EXTEND** | Add M4's 13 rename sites (or the licensing clause), m4's two `D24(b)` citation sites, m8's `TRIANGLE.md:216–218`, and m3's `notation.md` ordering sentence.  Item 5's `corpus-r2.md` annotation text is correct as written (X8); item 6's `main.tex` edit compiles (`amssymb` is loaded, `\mathfrak` already used 4×). |

**May the merge proceed as ONE commit?**  **Not yet — and when it does, it
must still be one commit.**  The lane is right that §5.0/§5.1/§5.2/§5.3 are
inseparable; the mechanics are sound and I verified them by applying them
(X5).  What blocks the commit is F1 (three sentences), M1 (two citations),
M4 (one clause) and M5 (one row).  M2 and M3 are checker/verdict repairs and
do not touch shared files, but they must land in the same round because §3,
§7.4, §7.5 and H7 currently assert things the checker does not do.

---

## 8.  `𝒮_W(ρ)` nonemptiness, `tns-axg`, `tns-iu5`

**`𝒮_W(ρ)` nonemptiness remains OPEN at every `ρ`, `ρ = 1/2` included.**  I
concur with §4.4 for the same reasons as r2, with one addition: under F1's
*literal* reading the merge would make it provably **empty** at `ρ ≠ 1/2`
again, which is a second reason F1 must be answered before anything is
applied.

* **bd `tns-axg`: stays OPEN, and MAY NOT move.**  Nothing here exhibits a
  member; §7.6's declination of r1's M3(c)(iii) is correct and correctly
  reasoned — a checker cannot construct `E^O_desc` without settling
  `tns-axg`, and D24N-C8 is honestly labelled a partial substitute.  The
  declination is **accepted**.
* **bd `tns-v44`: unblocked on this axis**, with §5.5 item 7 and its rider
  (do not describe `𝔞_leg` as derivable; do not use the leg-normalisation
  mechanism).  Add one more rider from F1: the shard must not assume clause
  (d)2's residue and `E^O_desc` are in the same normalisation.
* **bd `tns-iu5`: MUST STAY OPEN.  Sub-task (1) is PARTIALLY done, not
  done.**  Re-scope to four:
  1. *(partially done)* D24(b)'s amputation and **soft-leg** convention —
     supplied at §5.0 for `M_2^O`, and correct in the fully polarised
     spin-`S` register;
  2. **NEW, and the reason this round fails:** fix the normalisation in
     which clause (d)2's Ward residue is quoted, and make clauses 1–3
     consistent about it (F1);
  3. supply, or scope away, the `δ`-normalised asymptotic one-magnon kernel
     off the fully polarised family — this is `ML1` (CONJECTURE) and it is
     what `𝔞_leg(ρ)`'s definedness at general `ρ` rests on (M1);
  4. then prove or refute **AMP**, with the ⟨1⟩4 fence: leg conversion
     supplies exactly `Z_ρ^{-1/2}` (X1, X2), so a second, non-leg-normalisation
     factor of the same size is required; `D24-VAL` stays
     vacuous-or-unknown until (4) closes or `tns-axg` exhibits a member.

---

## 9.  The four questions the brief asked

1. **The amputation convention.**  It is *well defined* only in the fully
   polarised spin-`S` register, where D24N-C8 constructs its kernel; the
   D12(b) citation does not support it and no other register has the object
   (M1).  It is *consistent with existing corpus uses of "amputated"* only
   because every existing use sits at `ρ = 1/2`, where it coincides with the
   wider ML4-admissible class and with `ansatz-scattering-2m` ⟨2⟩5's
   `S_phys`-valued amputation — which is the convention ⟨1⟩0.⟨3⟩6 says it
   refuses (m4).  It *does* keep `D24-VAL` contentful: fixing the soft leg
   by the state normalisation rather than by the soft factor is the right
   choice and ⟨1⟩0.⟨3⟩6's refusal of the tautologising alternative is
   correct and well argued.  And fixing `c′(0)/c = 1` **does not by itself
   make `𝔞_leg` a number**: it fixes the numerator's leg and leaves the
   residue in the denominator's clause unfixed (F1), and it relocates the
   remaining arbitrariness into an unconstructed kernel off the spin-`S`
   family (M1).
2. **The new sharp result.**  `Q^-_k|Ω⟩ = √(Z_ρ)|k⟩` is **exact** — I
   reproduced it at `0.000e+00` by independent ED, and `|k⟩` is an exact
   `H_S` one-magnon eigenvector (X1).  The refutation numbers are exact and
   need no band (X2).  So the narrowing is real **conditional on F1's mixed
   reading being the intended one**: given that reading, AMP is true only if
   a second `Z_ρ^{-1/2}` comes from something that is not a leg
   normalisation, and that is a genuinely useful fencing of an open lemma.
   It is the best thing in the round.  Its one soft spot is not the identity
   but the object it is applied to (m1: the descendant leg carries
   `Z_ρ − 2/N` per site, exact only in the LSZ limit).
3. **The checker.**  Deriving the band from the data is *not*
   self-fulfilling in the r1 sense — the two refutations survive at the
   pre-registered band with `5–37×` margins.  But the claim that no
   acceptance constant remains is **false**, and the surviving constant is
   both undeclared and binding (M2).  Guards: zero ✓, missing ✓, over-wide
   only above `0.08` ✗ (m2).  The self-declared gap list is **accurate on
   all five items it declares** — C1's absent runtime red mode, C5/C7 as
   display, C6 = C4 at a tighter band with `1.7×` exponent gain (I
   recomputed `1.69×`), no gate touching `L`/`E^O_desc`/membership, C2's
   one-decade margin (`1.137e-13` vs `1e-12`) — and **incomplete on three**:
   `EXPONENT_FIT_BAND`, the `0 ≡ 0` orthogonality gate with its constant-true
   guard, and the one-sided band guard.  The correction of its own r2
   overclaim about C6's resolving power is exactly the behaviour that makes
   this adjudicable.
4. **Merge coherence.**  The three `definitions.md` spans **do** apply
   cleanly, in the prescribed descending order, without overlap — I applied
   them (X5).  `notation.md`'s six edits do **not** carry the same
   instruction and the written order breaks two of their anchors (m3).  The
   commit is otherwise mechanically ready.

**Trajectory.**  r1 `3 FATAL / 7 MAJOR / 6 MINOR / 4 NOTE`; r2 `1/5/8/5`; r3
`1/5/8/4`.  The count is flat and the content is not: five of r2's six items
verified FIXED by fresh recomputation, the sixth (M3) fixed in direction and
relocated in substance, and the new FATAL reachable only *because* §5.0
exists.  The physics is unchanged and stronger than it was: the leg-conversion
identity is exact, the two refutations are exact, and the corpus's `2` is
correctly re-sourced.  What remains is one normalisation the convention did
not reach, one referent that does not exist off the spin-`S` family, one
undeclared constant, one no-op, one rename, and one quantifier.

---

**FAIL(F1, M1, M2, M3, M4, M5)**
