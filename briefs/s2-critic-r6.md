# Critic brief — AC-EX-2M round 6 (convergence check)

Read `briefs/critic-protocol.md` first, including Standing checker obligations.

**TARGET:** `theory/ansatz-scattering-2m.md`,
`theory/ansatz-scattering-2m-r5-response.md`,
`theory/checks/ansatz_scattering_2m_check.py`.
**VERDICT FILE (your only writable file):**
`theory/verdicts/ansatz-scattering-2m-r6.md`.

**Priors:** `-r1` … `-r5`.  Trajectory `6 → 2 → 1 → 1 → 1` MAJOR, 0 FATAL
throughout.  **The row is already PROMOTED**: `claims/CLAIMS.md` carries
`AC-EX-2M` at PROVED (conditional, A2M.1--A2M.2) and `AC-EX-2M-D29` at SKETCH,
both cells written by the r5 critic and applied verbatim.  The orchestrator has
also now applied **r5 §9 condition 2**, simplifying the `where-proved` cell to
`⟨1⟩2--⟨1⟩7′` now that the hoist has landed.

This is a **convergence check**.  Scope tightly with `git diff`; do not
re-litigate anything settled in r1–r5, and do not churn r5's verified list.
The question is narrow: **is this artifact now at 0 MAJOR, and is the promoted
row's certificate sound?**

## What to verify

1. **The hoist.**  `⟨1⟩7′` now sits between `⟨1⟩7` and `⟨1⟩8`, outside
   `⟨1⟩9`'s D29 ASSUME.  The lane claims its body is the old `⟨1⟩9.⟨2⟩4`
   **byte-for-byte** (checked against `433f0b3`), that `⟨1⟩3--⟨1⟩7` are
   **byte-identical** (10577 bytes), and that the only edit inside the frozen
   range is the one sentence r5 mandated.  **Verify all three claims yourself
   with `git diff` / `cmp`** — a byte-identity claim is trivially checkable and
   must not be taken on trust.  Then confirm `⟨1⟩7′` genuinely consumes no D29
   clause and that the promoted row's certificate now lives where the row
   points.
2. **The deliberate deviation (RESIDUE-1).**  The lane did **not** renumber
   `⟨1⟩9`'s remaining sub-steps, reasoning that renumbering would falsify two
   pointers in the applied, un-editable `AC-EX-2M-D29` cell.  Judge that
   reasoning, and — now that condition 2 is applied — **rule on whether the
   renumbering may proceed, and if so supply the exact replacement text for
   any CLAIMS pointer that must move with it.**
3. **The G8 decision.**  The lane implemented your option (α), measured it, and
   **rejected it**: by linearity of `block_transfer`/`fixed_projection` the
   proposed "numerical" form is *also* identically zero (residual `8.3e−17`
   baseline; `8.8e−17` / `1.0e−16` / `2.9e−16` under three mutants), so it
   would have been a sixth identically-zero gate wearing a numerical name.  It
   took option (β) instead — relabelling G8 a **code-shape guard** across four
   advertising sites, ending "No round may cite G8 as numerical evidence".
   **Verify the linearity claim independently.**  If it holds, say so plainly:
   a proposer that tested your suggested fix and refused it on measurement did
   the right thing, and the finding should be fenced so no future round
   re-proposes it.
4. **Lockstep.**  §7 now carries an "Applied `claims/CLAIMS.md` lockstep
   mirror" reproducing both rows (claimed 4467 and 3465 bytes, six columns
   each).  `cmp` them against the live file.  Note the `where-proved` cell has
   just changed, so the mirror must match the CURRENT file, not the one the
   lane saw.
5. **Dispositions**: 19 rows — 9 FIXED, 1 SUPERSEDED, 9 RESIDUE.  Nine
   residues is a lot for a convergence round; check each is genuinely a
   deferral rather than an unaddressed objection wearing a label.
6. **Checker.**  Claimed green 0 and seven reds exit 1 with exit paths matching
   your own §4.1 table, nine gates, seven pairwise-distinct violation sets,
   zero bare asserts, mutants on copies at exit 2, and the λ̃ battery closed.
   Apply the standing obligations once more.

## Deliverable

Verdict line and the r6 MAJOR count against `6 → 2 → 1 → 1 → 1 → ?`.  If **0
MAJOR**, say so explicitly and state whether `AC-EX-2M` should stay at PROVED
(conditional) with its current sentence or needs any adjustment.  For
`AC-EX-2M-D29`, restate the named missing steps.  And give the renumbering
ruling with any pointer text it requires.
