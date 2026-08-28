# Work order — ML4-Ward n≥2 downstream audit (bd tns-uxr, P0)

A PROVED row was found defective.  Requirements (1) confirmation and (2)
row-scoping are already DONE.  You execute requirement (3): the downstream
audit.  This is an AUDIT, not a repair — you report, the orchestrator edits.

## THE DEFECT (confirmed three independent ways)

`theory/ml4-ward-reduction.md`, equation (9), **second display**:
`P_{n,N} J^-_0 = 2 Q_0 J^z_0/(N−2n)` on `ker S^+`.
- EXACT at `n=1` (error 1.2e-16) — dies by momentum conservation.
- **FALSE for `n≥2`**: errors 0.26 / 1.11 against lhs norms 0.91 / 1.39 at
  `n=2,3`, `N=8`.
- Mechanism: `⟨3⟩4` applies the scalar `(N−2n)^{-1}` to `2J^z_0ψ`, which is
  NOT in `ker S^+` for `n≥2`, because `[S^+,J^z_0]=−J^+_0` and
  `||J^+_0ψ|| = 0 / 0.66 / 1.36` at `n=1/2/3`.
- CORRECT replacement, verified `≤2.4e-15` at every `n`:
  `P J^-_0 = 2D(D^†D)^{-1} J^z_0`.
- Certificate: `theory/checks/ml4_ward_n2_check.py` (green exit 0, `--red`
  exit 1).  The `n=1` consequence (11)/(R15) is UNTOUCHED.

## THE TASK

Find **every** place in the corpus that consumes ML4-Ward (9) or (18), and
classify each one.

1. `grep` exhaustively — the whole repo: `theory/`, `claims/`, `definitions.md`,
   `notation.md`, `docs/`, `briefs/`, `paper/`, `theory/checks/`.  Search for
   the equation numbers, for the identity's shape (`J^-_0`, `J^z_0`, `Q_0`,
   `P_{n,N}`, `N−2n`, `ker S^+`), and for the claim ids that depend on
   ML4-Ward in the DAG.  Do not rely on the CLAIMS depends-on column alone —
   walk the DAG transitively AND grep the prose, because shards cite each
   other in text without DAG edges.
2. For each hit, determine the **sector index `n` actually in play**.  This is
   the whole audit: a use at `n=1` is SAFE; a use at general `n` or `n≥2` is
   DAMAGED.  Read enough surrounding context to be certain — quantifiers
   matter, and "for all n" hiding in a preamble counts as `n≥2`.
3. Classify each site: **SAFE (n=1 only)** / **DAMAGED (n≥2, needs the
   corrected form)** / **DAMAGED-BUT-REPAIRABLE-BY-SUBSTITUTION** (the
   corrected `2D(D^†D)^{-1}J^z_0` form goes straight in and the downstream
   conclusion survives — say so, and say whether any constant changes) /
   **UNCLEAR** (say exactly what you could not determine).

Known starting point, already confirmed, which you must verify and extend:
`theory/ml4-ward-reduction.md` ⟨1⟩5 ⟨3⟩2 feeds `n=2` into (9) — the
**two-hard-magnon Ward part is damaged**.  Find the rest.

## READ FIRST

CLAUDE.md; `theory/ml4-ward-reduction.md` IN FULL (including the ERRATUM
block at ⟨1⟩3); `claims/CLAIMS.md` (the scoped ML4-Ward row with its ERRATUM,
and every row whose depends-on reaches it); `theory/checks/ml4_ward_n2_check.py`
(run it — green and `--red` — and confirm the numbers yourself);
`theory/verdicts/soft-index-b-r1.md` F1 (the original refutation).

## YOUR LANE (writable — nothing else)

- `theory/verdicts/ml4-ward-n2-audit.md` (create)

Do NOT repair any shard, do NOT edit `claims/CLAIMS.md`, do NOT edit
`definitions.md`.  Repairs are the orchestrator's, informed by your report.

## DELIVERABLE

A table with one row per site: file, step address (⟨i⟩j.⟨k⟩l or line),
the `n` in play, verdict, and — for DAMAGED rows — the one-line fix demand
and the **surviving weaker statement**.  Then:
- a **DAG section**: for each claim row that transitively depends on
  ML4-Ward, state whether its status survives as-is, needs scoping, or must
  be demoted, and name the step that decides it;
- a **blast-radius verdict**: one paragraph, is the damage contained to the
  two-hard-magnon Ward part or does it reach a headline claim?
- an explicit statement of what you checked and found CLEAN (negative
  results matter — they stop the next session re-auditing).

Be exhaustive and be precise about addresses.  Understate conclusions you
cannot verify by computation; mark them UNCLEAR rather than guessing.

Work fully autonomously.  Do not ask questions.
