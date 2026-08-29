# BLITZ LANE RULES (2026-08-29) — read fully before your task

You are ONE codex lane of ~20 running IN PARALLEL in this repo. Race safety is absolute:

- WRITE ONLY inside your lane dir `theory/lanes/blitz-2026-08-29/<lane>/` (named in your brief). Create anything there: proof shards, scripts, patched copies, logs, data.
- NEVER edit or create any file anywhere else in the repo. If your task requires changing an existing file: COPY it into your lane dir, edit the copy, and write `PATCH.md` listing exact anchored edits (string anchors, not line numbers — lines drift under concurrent edits) for the orchestrator to apply.
- NEVER run: `bd`, `git commit`, `git add`, `git push`, or anything touching `.beads/` or `.git/`.
- You may READ everything and RUN computations (python3, julia) with outputs only into your lane dir.

Process (PRD.md governs — read it):
- Read gate: CLAUDE.md, PRD.md, then the files your brief names.
- Rigorous arguments in Lamport structured style (L6b): numbered steps <1>1, <1>2, sub-proofs <2>*, explicit ASSUME/PROVE, terminal QED; every leaf cites a D-number (definitions.md), a claim id (claims/CLAIMS.md), or a named computation script in your lane dir.
- Notation/definitions are NEVER redefined — cite notation.md / definitions.md (L4).
- Write your main output file INCREMENTALLY, section by section (long monolithic outputs get truncated).
- Any numeric claim: script it, run it, save the output file. Checkers must be red-capable: demonstrate a mutation that makes them fail.
- HONEST LABELS (PRD goal 2): never a status stronger than the evidence. A sharp partial or a clean negative with a named forward attack is a good outcome.
- You have a hard wall-clock limit (~25 minutes; you may be killed at any time): produce a complete partial result rather than an incomplete grand one. Write SUMMARY.md EARLY and update it as you go.

Required final artifact: `SUMMARY.md` in your lane dir with:
- STATUS: one of {PROVED-candidate, SKETCH, PARTIAL, NEGATIVE, BLOCKED}
- <=10 lines: what you established, what remains, which existing files PATCH.md targets (if any).
