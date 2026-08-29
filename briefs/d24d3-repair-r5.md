# Work order — D24(d)3, repair round 5 (three sentences from merge)

**FAIL(M1,M2,M3)** — **0 FATAL**, 3 MAJOR, 8 MINOR, 5 NOTE.
Trajectory `3/7/6/4 → 1/5/8/5 → 1/5/8/4 → 0/3/8/5`.

**This is the first round with no FATAL and the first in which every prior
item is FIXED rather than relocated.**  The critic confirms:
- the **two-anchor convention is WELL POSED** — it carried the `(c,c′)`
  covariance algebra through the (3a) quotient with the hard-leg factor
  explicit; it cancels, clause 2 read charge-created is hard-leg-invariant,
  `(b)` pins `𝔞_leg` exactly once, and clause 2 acts as a cross-normalisation
  **membership** condition, not a second covariance anchor;
- the **X2 discharge is legitimate, not circular**;
- **all three claimed costs are actually paid in the merge text**, and the
  "every other line byte-identical" claim is exactly true;
- **both checker complaints are genuinely discharged** — the subsumption proof
  is correct and the demotion to DISPLAY is the right disposition; the
  two-magnon replacement is **not** a new no-op (`−2N·Z_ρ` derived on paper and
  confirmed by independent full-Hilbert-space ED at `2S=1..4`, `N=4,6,8`);
- the **m2 deviation is ACCEPTED**, both halves of its reason checked.

Do not redesign anything.  All three MAJORs are **sentence-level**.

## READ FIRST
`CLAUDE.md`; `theory/verdicts/d24d3-adjudication-r4-critic.md` **IN FULL**,
its fenced/verified list first; `theory/verdicts/d24d3-adjudication-r4.md`;
priors r2/r3 critic verdicts.

## M1 — the m1 repair stops one span short

Merged clause 2 says the two legs differ by "**exactly** `√Z_ρ`" and cites
`(b)(i)` — which is the sentence saying they do **not**, on the *descendant*
leg at finite `N`.  The new C3 DISPLAY prints `2.828427` as the
"(b)-asymptotic residue" at `N=8`; the true value against a δ-normalised
descendant leg is `2.921187` — **3.28 % out**, and it is disproved **by this
round's own new gate C8(ii)**.  Fix the sentence and the DISPLAY label so they
agree with your own certificate.

## M2 — the AMP fence overstates

It ships the refutation of `Z_ρ^{-1/2}` **unconditionally** into
`definitions.md` 3b and the `AMP` row, dropping the `(α)` qualifier **three
sentences after the same paragraph names the bridge for the frozen
refutation**, and dropping the charge-created reading of `E^O_desc` that your
own §1.4 cost 3 says is refuted for any class member.  Restore both.

## M3 — the where-proved columns are stale, and this is a repeat

`ML5-B` and `D24-VAL` point only at r3, whose §5 merge text and invariance
list **r4 supersedes**.  The critic notes this is **verbatim the r2-critic's
M4 — "the serious one" — one document over**.  Point them at r4.

## The MINORs, and four address corrections you must carry

The critic verified one-commit appliability by applying all thirteen edits to
scratch copies with an `assert` on every anchor, and confirms your
`notation.md` order **b′ → a′ → c → f → e → d is correct**.  But four
addresses are wrong and must be fixed **in the merge text**, since the
orchestrator applies it verbatim:
- item 12's second note belongs at `ansatz-scattering-2m.md:692`, not
  `:621–631` (that file is under concurrent edit and your address is stale by
  ~50 lines) — **string-match it, do not line-number it**;
- §5.4e's rationale should read `:170`, not `:146`;
- `claims/CLAIMS.md`'s second bare `𝒮_W` is at line **83**, not 82;
- **`HANDOFF.md:40` is a 19th live site** absent from your licensing clause's
  enumerated list — add it.

Prefer string anchors over line numbers throughout; three of these four errors
are line-number drift under concurrent edits.

## LANE (writable, nothing else)
`theory/verdicts/d24d3-adjudication-r5.md`,
`theory/verdicts/d24d3-repair-r5-response.md`,
`theory/checks/d24d3_normalization_check.py`.  MERGE PROPOSALS only; the merge
must remain applicable as ONE commit.  No commits.

**Target: PASS.**  Three sentences, four addresses, and the merge lands.

Work fully autonomously.  Do not ask questions.  ONE section per response.
