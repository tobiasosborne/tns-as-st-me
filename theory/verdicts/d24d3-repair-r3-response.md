<!-- ROLE: PROPOSER's repair response, round 3, to
     theory/verdicts/d24d3-adjudication-r2-critic.md FAIL(F1,M1-M5).
     Companion to theory/verdicts/d24d3-adjudication-r3.md.
     Work order: briefs/d24d3-repair-r3.md.  Writable files of this lane:
     the r3 verdict, this file, theory/checks/d24d3_normalization_check.py.
     No shared file was edited; no git commit. -->

# r3 repair response — disposition of every r2-critic item

**Nineteen items: 1 FATAL, 5 MAJOR, 8 MINOR, 5 NOTE.  Disposition: 17
FIXED, 1 DECLINED WITH REASON (r1's M3(c)(iii), which the r2 round declined
silently), 1 ACCEPTED AND REFERRED OUT OF LANE (n4, a paper-lane ticket).
One fix deviates from the critic's suggested wording and says so (M5).**

Nothing in this response contradicts the r2 critic's §1 (W1–W18) or the r1
critic's §1 (V1–V14); those are fenced and were not re-derived.

---

## 1. Headline answers to the three questions the critic put

1. **Is `𝔞_leg` still a renaming?**  **No — the convention is fixed.**
   `definitions.md` D24(b) now carries an explicit amputation and
   leg-normalisation convention (r3 §5.0): `δ`-normalised asymptotic
   one-magnon kernels, the same amputation on the same hard leg in both
   amplitudes, and the soft leg entering `M_2^O` as one additional
   `δ`-normalised asymptotic magnon with unit leg weight.  The covariance
   the critic exhibited is displayed in the definition itself
   (`𝔞_leg ↦ (c′(0)/c)𝔞_leg`), together with the statement that fixing
   `c′(0)/c = 1` is what makes `𝔞_leg` a number.  **AMP is statable**, and
   it now has a DAG row (`AMP`, CONJECTURE) and a writable prover target.
2. **What about "the only place the density can live"?**  **Withdrawn, not
   defended.**  The critic was right that it was not proved, and the r3
   argument does not need it.  Under a fixed convention `𝔞_leg` is not a
   home for a factor; it is the value of a quantity that clauses 1–3a
   already determine.  Clause (3b)'s membership content is therefore the
   `h`-profile, and its value content is nil.  This also dissolves m3.
3. **What does the merge cost?**  **ML5-B predicts no number at any
   density.**  Drawn, stated in the row, in `§4.3`, and in a new honest
   status paragraph `H8`.  See §3 below for the decision and its reasoning.

---

## 2. Disposition table

| id | severity | disposition | where |
|---|---|---|---|
| **F1** | FATAL | **FIXED** — convention supplied as displayed text; PROVE (ii) restated; "forces"/"only place it can live" withdrawn; ⟨1⟩2.⟨3⟩1's prose-only justification replaced by D-number/named-computation leaves; AMP statable and given a row | r3 §5.0; ⟨1⟩0; ⟨1⟩2; §5.3c; §8 |
| **M1** | MAJOR | **FIXED** — all five "recovered verbatim" strings struck and replaced with the critic's text; the consequence drawn (ML5-B predicts no number at any density); the false D24(e)/`ml4_check.py` clause struck in both places | r3 §4.3; H8; §5.1; §5.2 clause 3b; §5.3a; §5.3d |
| **M2** | MAJOR | **FIXED, and further than demanded** — "at every density" rescoped to the fully polarised `ρ = S` family; "forces" **withdrawn** rather than downgraded to "natural home", because ⟨1⟩0 shows even the weaker claim is not available | r3 ⟨1⟩2.⟨3⟩3–⟨3⟩4; §1.2 |
| **M3** | MAJOR | **FIXED** (i)–(iii); (iv) declined with reason, recorded | r3 §7.4, §7.5, §7.6; checker rebuilt |
| **M4** | MAJOR | **FIXED** — all three sites added; `corpus-r2.md:174–178` **annotated**, not erratum'd, because it is a promotion record; the r2 response's "M6: FIXED" is downgraded here (§4 below) | r3 §4.2; §5.5 items 4–6 |
| **M5** | MAJOR | **FIXED with a stated deviation** — `D24-VAL` becomes status `PROVED`; CONJECTURE moves to a new `AMP` row; where-tested rewritten.  Deviation: the critic's label "PROVED (conditional implication; currently vacuous-or-unknown)" is **not** used as a status value, because `claims/CLAIMS.md`'s own header forbids qualifier-bearing statuses; the qualifier is in the statement column, as ML5-B already does | r3 §5.3 preamble; §5.3b; §5.3c |
| **m1** | MINOR | **FIXED** — symbol is `𝔞_leg(ρ)`; the false rationale ("bare `𝔞` is `𝔞_α`") struck — `𝔞_α` is itself subscripted; new overload rule 13 records the real disambiguator (subscript *type*: Greek tail label vs word label) | r3 §5.4a; §5.4f |
| **m2** | MINOR | **FIXED** — overload rule 8 amended for `E^O_desc`.  Line correction: the critic cited `ansatz-scattering-2m.md:141`; the live `E_O` is at `:146` | r3 §5.4e |
| **m3** | MINOR | **FIXED (dissolved)** — "the whole of the value this clause asserts" struck; (3b) restated as the `h`-profile with `𝔞_leg(ρ)` "a datum of the class, not of the source"; the preamble no longer implies a per-source test for 3b | r3 §5.2 clause 3b; ⟨1⟩2.⟨3⟩2 |
| **m4** | MINOR | **FIXED, all three** — (i) C2 now cross-checks two independently coded ladder formulas at every `n ≤ 2S−1` and adds multi-quantum norms; the critic's `cA_deepladder` is shipped as `--red-ladder` and dies **at C2**; (ii) the momentum loop now carries cross-momentum orthogonality and a three-momenta requirement, so `cB_onek` dies at C2; (iii) `require(1**p − 1 == 0)` deleted, degeneracy printed | checker C2, `check_exponent`; r3 §7.1, §7.3, §7.4 |
| **m5** | MINOR | **FIXED** — C7 labelled DISPLAY in the banner and in the docstring; the substantive `N`-free half power is falsified at C6 instead | checker; r3 §7.4 |
| **m6** | MINOR | **FIXED** — the resolving power is quoted as an interval, never as a `±`; three intervals are printed (derived band, pre-registered band, r2's retired band) | checker banner; r3 §3, §7.4 |
| **m7** | MINOR | **FIXED by removal** — the disclosure arithmetic is withdrawn and the constant it described no longer exists; the band is derived from the data's `error` column at run time | r3 §7.5 |
| **m8** | MINOR | **FIXED** — `soft-index-r1.md:170` added to the ERRATUM list | r3 §5.5 item 4 |
| **n1** | NOTE | **FIXED** — "for each such `S` separately" in the PROVE line and in the row | r3 ⟨1⟩3; §5.3b |
| **n2** | NOTE | **FIXED** — `𝒮_W(ρ)\|_{ρ=S}` everywhere, never `𝒮_W(S)` | r3 ⟨1⟩3; §5.3b |
| **n3** | NOTE | **FIXED** — one clause in the `D24-VAL` row distinguishes the D24(d) tail density `ρ` from the file-local double-occupancy `ρ` of `spin-s-twomagnon.md` | r3 §5.3b |
| **n4** | NOTE | **ACCEPTED, REFERRED** — Fig-2 caption is out of this lane; recorded as a bd to be filed by the orchestrator, with the §4.3 re-sourcing as its motivation | r3 §5.5 item 9; §8 |
| **n5** | NOTE | **FIXED** — §7.4 states plainly that C6's reachability is automatic (one call site) and is evidence that r1's pathology is gone, not that C6 is strong | r3 §7.4 |

---

## 3. The M1 decision, in full: what "ML5-B predicts no number" means

The critic's M1(b)(ii) is correct and the r2 artifact never drew it.  The
decision taken, and why:

* **ML5-B keeps status `PROVED`.**  What ML5-B proves is an implication from
  the five conditions to a factorisation; the number `2` was never among its
  consequences.  It came from ML5-B **plus** the frozen clause 3's
  stipulation `𝔞_leg = 1`.  Retiring the stipulation removes the number from
  the conclusion without touching the proof, which multiplies through by a
  nonzero constant.
* **The row's strength is honestly reduced, in the row.**  Its conclusion is
  now labelled a factorisation **shape** — linear in `k`, proportional to
  `M_1^O`, with a class constant — and the row says in bold that it contains
  no number at any density, `ρ = 1/2` included.
* **The promotion record is annotated, not reopened.**
  `theory/verdicts/corpus-r2.md:174–178` certified the `𝔞_leg = 1`
  arithmetic.  The same multiplication with `𝔞_leg` carried is
  `(e^{ik}−1)·𝔞_leg(−iχ/v_h)·(2i v_h M_1) = 2i𝔞_leg χ k M_1 + O(k²)` — the
  certified implication survives verbatim under reparametrisation.  So the
  where-proved column may keep pointing there, provided the annotation of
  §5.5 item 5 ships in the same commit.  Without that annotation the column
  would point at a document certifying a different conclusion, which is
  exactly the critic's M4 objection.
* **The corpus's `2` is re-sourced, not deleted.**  Every display traces to
  the contact/oracle route (`paper/main.tex:515–520` solves the contact
  equation directly for `2i`; `oracle-bethe.md` O7–O9), which does not use
  D24(d).  §4.3 lists the sites and says which of the two dispositions each
  gets.
* **The loss is recorded as a loss.**  H8: after the merge, a reader who
  wants a number out of the five-condition class will not find one until
  `tns-axg` or AMP closes.  Per L10 this is stated, not managed.

---

## 4. Corrections to the r2 response's own claims

* The r2 response table said **"M6: FIXED — all five missed sites added"**.
  Downgraded here to **"FIXED for the five r1 sites; two further sites found
  by the r2 critic (`corpus-r2.md:174–178`, `main.tex:524–527`) and one
  minor (`soft-index-r1.md:170`), all added at r3"**.
* The r2 response table said **"M3: FIXED (all five demands)"**.  Downgraded
  here: four of the five were met; r1's M3(c)(iii) (constructed `E^O_desc`)
  was **not** met and was not disclosed.  It is declined at r3 §7.6 with its
  reason, and a partial substitute (D24N-C8) is offered and labelled partial.
* The r2 response said the merged definition **"agrees with"** the three
  provenance sites.  Withdrawn: it is *consistent* with them at `𝔞_leg = 1`,
  and they are `ρ = 1/2` statements that fix the `h`-profile, not the value
  (r3 ⟨1⟩2.⟨3⟩3).
* r2 §7.4's "the **evidential** gates of C6 … independent of C4" is
  withdrawn (r3 §7.4).  r2 §3's "`±1.2%`" / §7.4's "`±1.7%`" are withdrawn
  in favour of printed intervals (m6).

---

## 5. Disclosures (volunteered, in the r2 spirit)

1. **The convention is a choice.**  §5.0 is not derived from anything in the
   corpus.  A different admissible convention rescales `𝔞_leg` by a known
   constant and every numerical statement about it moves accordingly.  The
   r3 verdict says so at ⟨1⟩0.⟨3⟩6, in H2, and inside the merged
   `definitions.md` text itself.  The specific alternative deliberately
   refused — defining the D24 ratio to *be* the physical soft factor, which
   would make `D24-VAL` a tautology — is named.
2. **⟨1⟩4 is new content in an adjudication round.**  It adds a computed
   constant (`√Z_ρ`) and a refutation (`Z_ρ^{-1/2}`) that no earlier round
   contains.  It was added because F1's fix makes the question well posed
   for the first time, and because a convention that cannot be used to
   falsify anything would be decoration.  A critic should attack ⟨1⟩4.⟨3⟩2
   first: the claim that the three provenance sites compute with a
   charge-created soft leg is a *reading* of their notation, not a theorem
   about them.  If that reading is wrong, ⟨1⟩4.⟨3⟩3's `Z_ρ^{-1/2}` is not
   the leg-normalisation prediction and the fence on AMP weakens (nothing
   else in the round depends on it).
3. **⟨1⟩4's refutation rests on the bridge (α).**  It compares a D24
   prediction against two-magnon phase data.  Without (α) nothing is
   refuted — and nothing is matched either.  H6 now records that the bridge
   carries more weight than it did in r2.
4. **The checker is 559 loc, 59 over the L2 guideline.**  Flagged in §7 with
   the reason (the C8 one-magnon block plus two extra C2 routes) and a
   suggested later split.  Not hidden.
5. **C2's worst error rose to `1.14·10^{-13}`** (from `8.9·10^{-16}`) because
   the multi-quantum norms at `2S = 4` are `O(10^2)` in magnitude.  The gate
   tolerance is unchanged at `10^{-12}`; the margin is one decade, not four.
6. **`m6_shift30` now PASSES.**  That is deliberate and is the point of the
   band change: a `−3%` perturbation is inside the data's own quoted error at
   every spin, and a gate that rejected it was mis-calibrated.  A critic who
   wants a tighter gate must first argue that the data's `error` column
   overstates the uncertainty.
7. **`D24-VAL` gains `D24(b)` in its depends-on**, and so does `AMP`; both
   are meaningless without the convention.  `S2-2body-S` remains excluded
   from ML5-B's depends-on, as in r2 (the r2 critic endorsed that reasoning).
8. **Line-anchor drift risk.**  §5.0/§5.1/§5.2 replace three adjacent
   `definitions.md` blocks, so they must be applied in descending line order
   or matched on their quoted first/last lines.  The r3 §5 preamble says so.
   All anchors were re-verified against the current files this round
   (`definitions.md` 923/929/931/950/952/973; `claims/CLAIMS.md` 40/41;
   `notation.md` 55/91/123/131/244/258/261/270).

---

## 6. What a fourth critic round should attack first

In order of expected yield:

1. **⟨1⟩4.⟨3⟩2** — the charge-created reading of the three provenance sites
   (disclosure 2).  This is the least-supported new step.
2. **§5.0's convention text as it will read in `definitions.md`** — is it
   self-contained for a reader who has only D24, D3(a), D12? Does
   "`δ`-normalised asymptotic one-magnon kernel" have a unique meaning in
   this corpus at general `ρ`, where the asymptotic one-magnon state is not
   constructed anywhere?  (The r3 verdict computes it only in the fully
   polarised spin-`S` family, D24N-C8.)
3. **The `AMP` row's unconditional quantifier** — it asserts
   `𝔞_leg(ρ) = 1/Z_ρ` at every `ρ`, while everything that motivates it lives
   at `ρ = S ∈ ½ℤ`.  Is the row scoped correctly, or is it the M2 quantifier
   defect moved into a new row?
4. **Whether `D24-VAL` at status `PROVED` plus `AMP` at CONJECTURE is one
   claim split in two** — and if so, whether the DAG now double-counts.
5. **The checker's C2 tolerance margin** (disclosure 5) and whether C8's
   `10^{-10}` thresholds are loose enough to hide a small systematic.
