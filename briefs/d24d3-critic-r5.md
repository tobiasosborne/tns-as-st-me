# Critic brief — D24(d)3, round 5 (final merge clearance)

Read `briefs/critic-protocol.md` first, including Standing checker obligations.

**TARGET:** `theory/verdicts/d24d3-adjudication-r5.md`,
`theory/verdicts/d24d3-repair-r5-response.md`,
`theory/checks/d24d3_normalization_check.py`.
**VERDICT FILE (your only writable file):**
`theory/verdicts/d24d3-adjudication-r5-critic.md`.

**Priors:** r1 (3 FATAL/7 MAJOR), r2 (1/5), r3 (1/5), r4 (**0 FATAL**/3 MAJOR).
Trajectory `3/7/6/4 → 1/5/8/5 → 1/5/8/4 → 0/3/8/5 → ?`.  Do not churn any
fenced list; verify the 16 dispositions by fresh recomputation.

**Stakes: this is the last gate.**  A PASS merges into `definitions.md` AND
`notation.md` — two L4 single sources — plus four `claims/CLAIMS.md` rows, as
ONE commit.  Four prior attempts would each have installed a defect.

## 1. M1 — verify the both-options fix

The lane took **both** of your offered options, on the reasoning that a DISPLAY
printing one number under two possible readings is what created the defect.
Clause 2 now reads `√Z_ρ` **in the LSZ limit**, with the finite-`N`
descendant-leg value `√(Z_ρ − 2/N)` displayed and justified by
`‖Q^-_q|h⟩‖² = Z_ρN − 2`, cited to `(b)(i)` and C8(ii) — citation and cited
sentence now agreeing.  The C3 DISPLAY prints **both** scopes, the finite-`N`
one computed by dividing by the **measured** leg ratio rather than a closed
form: **2.921187**, not 2.828427.

The lane ran red-green on its own repair: an independent from-scratch
two-quantum-sector probe (no repo import) measured `‖Q^-_0|h⟩‖² = 30.0000000000`
and leg ratio `1.9364916731`, reproducing your 3.28 % exactly, and **exited 1
against r4's checker and 0 against r5's**.  Verify that probe and that
red-green transition — a repair that is itself red-green tested is the standard
this campaign wants, and it should be confirmed rather than assumed.

## 2. M2 and M3

- **M2**: both hypotheses restored in `definitions.md` 3b *and* the `AMP` row —
  the charge-created reading of `E^O_desc` **and** bridge `(α)` — with `(α)`
  now **labelled at its first appearance in the same paragraph**, which is what
  removes the asymmetry you found.  Check the label is at the first appearance
  and that no reading is now over-restored.
- **M3**: both where-proved columns point at r4 §0.2, r5 §0.2 **and r5 §5 as
  "the merged text of record"**.  Judge whether naming the merged *section*
  (rather than only the superseding rounds) actually stops the recurrence —
  this defect has now travelled from r2 to r4 to r5, one document each time.

## 3. String anchors — and a live vindication you should record

Every §5 anchor is now a quoted string; line numbers are parenthesised hints
only and no application step depends on one.  **Your own correction `82 → 83`
went stale before it could be applied**: `claims/CLAIMS.md` gained the
`LR1-GEN` and `LR-D16-EDW` rows at `137f922` and that site is now at **85**.
Confirm this, and confirm the four addresses are fixed as strings, including
`HANDOFF.md` as the **nineteenth** licensing site.

## 4. Merge integrity — re-verify independently

The lane applied all thirteen edits to scratch copies of the
post-`5349ee5`/`137f922` files with an `assert` on every string anchor:
**13/13 in one pass**, `definitions.md` descending, `notation.md` in the
verified **b′ → a′ → c → f → e → d** order, CLAIMS by row label; results
`1349 / 313 / 146` lines, overload rules 2/8/13 correct, all four CLAIMS rows
6-column and correctly statused.  It also built the two revised blocks
**programmatically** from r4's, so "every other line byte-identical" is
mechanically true (§5.0″ differs in exactly 2 hunks, §5.2″ in exactly 4).
**Do the application yourself against the CURRENT files** — the tree has moved
again since the lane finished.

**One thing you must confirm before I commit:** the lane reports that another
lane's commit already swept its **checker changes** into `HEAD`, so the checker
half must **not** be re-applied and only the three shared-file edits remain
owed.  Verify that claim against `git`, because acting on it wrongly either
double-applies or drops a change.

## Deliverable

Verdict line and trajectory.  **A clause-by-clause MERGE/HOLD, and an explicit
GO / NO-GO on committing the merge**, with the exact ordered recipe if GO.
State whether `tns-iu5` may now close or which of its four sub-tasks remain.
