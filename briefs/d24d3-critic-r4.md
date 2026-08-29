# Critic brief — D24(d)3, round 4 (the merge-clearance round)

Read `briefs/critic-protocol.md` first, including Standing checker obligations.

**TARGET:** `theory/verdicts/d24d3-adjudication-r4.md` (1127 loc, a delta on
r3), `theory/verdicts/d24d3-repair-r4-response.md`,
`theory/checks/d24d3_normalization_check.py` (727 loc, rewritten).
**VERDICT FILE (your only writable file):**
`theory/verdicts/d24d3-adjudication-r4-critic.md`.

**Priors:** `-r1-critic` (3 FATAL/7 MAJOR), `-r2-critic` (1/5), `-r3-critic`
(1/5).  Verify dispositions by fresh recomputation; attack what changed; do not
churn the fenced X1–X15 list or the r1/r2 fenced items.

**Stakes: this is the merge-clearance round.**  A PASS applies to
`definitions.md` AND `notation.md` — two L4 single sources — plus four
`claims/CLAIMS.md` row edits, **as one commit**.  Three prior attempts would
each have installed a defect.  The orchestrator will not hand-patch, so
appliability is part of the verdict.

## 1. The trilemma resolution — the round's central move

The lane took **none of your three horns**.  It adopted your own FIX DEMAND
instead: clause (d)2's residue is declared, in displayed text, to be quoted in
the **charge-created** normalisation (ml4-ward (11), D24N-C3), while `M_1^O`,
`M_2^O` and `E^O_desc` stay in (b)'s.  The mixed reading you identified as
forbidden is thereby promoted from accident to an explicit **two-anchor
convention** (§5.0′ fixes `c′(0)/c = 1`; clause 2 anchors the residue).

Costs the lane says it paid, in §1.4 — **verify each is actually paid, in the
merge text and not merely in prose**:
- the one-convention preamble is **struck as false**;
- the invariance list shrinks to clauses **1, 4, 5** — clause 2 transforms as
  `c′/c` and is convention-**constitutive**;
- `Z_ρ^{-1/2}` **stops being an independent mechanism** and is re-derived in
  one step as the numerator/denominator normalisation mismatch.

Attack: is a two-anchor convention *well posed*, or does it merely name the
inconsistency?  Does anything downstream still assume a single convention?
Does the `𝒮_W(ρ)` class remain non-empty **as a hypothesis class** under it,
and does `D24-VAL` remain contentful rather than tautological?

## 2. The Q-identity narrowing

The lane claims it now survives **unconditionally**, because your X2 fence was
conditional on exactly the reading now adopted, so the conditional discharges.
Check that the discharge is legitimate and not circular.  Its m1 soft spot is
claimed closed: `‖Q^-_q|h⟩‖² = Z_ρN − 2` is now a gate (error `7.1e-15`), and
the r3 "N-free per site" overclaim ships as red mode `--red-descnorm` (dying at
C8 with error exactly `2.000e+00`).

## 3. The checker — your two standing complaints

- **`EXPONENT_FIT_BAND` is DELETED**, the band derived from the same error
  column (`0.8805·log(1/(1−0.0479)) = 0.0432`), and **all four "no acceptance
  constant" layers retracted via a supersessions table**.  The derivation is
  claimed to double as a **subsumption proof** — a calibrated fitted-exponent
  gate can never fire on data passing the calibrated acceptance gate — so the
  comparison is demoted to DISPLAY.  Verify the subsumption argument; if it is
  right, that is the correct disposition and should be fenced.
- The `0 ≡ 0` orthogonality gate and its constant-true guard are **deleted**,
  replaced by a two-magnon same-total-momentum overlap `= −2N·Z_ρ` in derived
  closed form (moved by `--red-ladder` at `2S ≥ 2`; sign-flip mutant dies).
  **Verify the closed form independently** — a replacement for a no-op is
  exactly where a new no-op hides.
- `m_shift34`/`m_shift40` now pass; `m_shift45` dies at acceptance at **your
  own 0.0482**.
- One **stated deviation** (m2): a per-row 3×-median corrupted-entry guard
  instead of per-spin banding, because per-spin banding would reverse the
  X13-certified `m6_shift30` calibration; your exact mutant dies at 3.78×.
  Rule on it.

## 4. Merge appliability — verify, do not accept

The lane claims one-commit applicability **verified by actually applying every
span to scratch copies**: three `definitions.md` spans (descending, anchors
exact), `notation.md`'s six edits in a newly supplied order (b′, a′ at 258;
c at 244; f after 145; e at 123–130; d at 91–98), and four CLAIMS row edits,
with coherence checks passing.  **Do the same yourself, in your own scratch
copy**, and confirm the 18-site rename list is complete and correctly split
between renamed sites and those licensed bare by the §5.4b′ clause.

## Deliverable

Verdict line and trajectory `3/7/6/4 → 1/5/8/5 → 1/5/8/4 → ?`.
A clause-by-clause **MERGE / HOLD** on every proposal.  An explicit ruling on
whether **the merge may now proceed as one commit** — and if yes, the exact
ordered application recipe the orchestrator should follow.  Finally: whether
bd `tns-iu5` may close, or which of its four sub-tasks remain.
