<!-- ROLE: how we work in this repo. UPDATE POLICY: amend on felt failure or TJO directive, dated. -->

# CLAUDE.md — tns-as-st-me

Campaign: formulate and PROVE the 1D lattice infrared triangle (soft theorem /
asymptotic symmetry / memory effect) in MPS language, and write a top-quality
4-page PRL. The brief is `HANDOFF_MPS_SOFT_THEOREM.md` (read it). Live state is
`HANDOFF.md`. North star: **theorem + Bethe verification + MPS numerics on a
serious model illustrating the memory effect**.

## Read order (gate)

1. This file.
2. `HANDOFF_MPS_SOFT_THEOREM.md` — the brief (definitions, conjectures, oracles).
3. `HANDOFF.md` — current state, next steps.
4. `docs/framing.md` — background viewpoint (symplectic actions, Poisson charge
   algebras, function spaces). Informs, is not cited.

## Laws (rk-light)

- **L1 — Red-green TDD** for all numerics. Failing test first, watch it fail,
  make it pass. "Runs without errors" is never a test.
- **L2 — Shards 200–500 loc.** One module/one job; same for theory shards
  (one lemma-cluster per file under `theory/`).
- **L3 — Ground truth is local TeX.** Quote references from `refs/arxiv-<id>/`
  TeX sources, never from memory. Every fetched id verified against its title;
  mismatches recorded in `refs/LEDGER.md`.
- **L4 — Notation and definitions are deduped.** Every symbol/definition lives
  exactly once, in `notation.md` / `definitions.md`; theory shards and the
  paper reference these, never redefine.
- **L5 — Claims DAG.** `claims/CLAIMS.md` holds every claim: id, statement,
  status ∈ {PROVED, SKETCH, CONJECTURE, REFUTED}, depends-on, where-proved,
  where-tested. Status upgrades only after the L6 loop converges. Markdown
  only — no CI machinery.
- **L6 — Proposer/critic to fixed point** on every artifact (result, lemma,
  argument, code). Proofs: prover = `codex exec` GPT-5.6 Sol xhigh; critic =
  Opus (or cross: Opus proposes, codex attacks). Iterate until a critic pass
  yields no fatal/major objections. Verdicts recorded next to the artifact.
- **L6b — Lamport structured proofs** (TJO directive 2026-08-25). Every
  rigorous argument in `theory/` is written in Lamport's hierarchical style:
  numbered steps ⟨1⟩1, ⟨1⟩2, …, sub-proofs ⟨2⟩1…, explicit ASSUME/PROVE for
  each nontrivial step, terminal QED steps, every leaf justified by a
  definition (D-number), a prior claim id, or a named computation. The paper's
  appendices may linearize, but the repo proof shard is the ground truth and
  stays structured.
- **L7 — Model policy.** No Fable subagents, NO exceptions (TJO directive
  2026-08-31, revoking the 2026-08-25 prose exception: "Fable is not good
  at prose"). NO model drafts paper prose; paper skeletons are produced at
  bullet-point level only, and final prose authorship is TJO's to do or
  assign. Register for skeletons and all writing that does occur: good
  simple communication, no arrogant tone, cautious scientific optimism
  (docs/prose-guide.md, 1305.2176 target). Otherwise: Opus for
  cognition-heavy work; Sonnet for search/mechanical; codex for proofs.
- **L8 — Cross-session state → bd** (prefix `tns-`). Insights → HANDOFF.md.
- **L9 — The paper is the product.** apsrev4-2, 4 pages main text, prose in
  the register of arXiv:1305.2176; exactly 3 main-text figures that tell the
  story in captions; full rigour in appendices/supplement. No overclaiming:
  every statement in the Letter traces to a PROVED claim or is labelled a
  conjecture.
- **L10 — Honest verdicts.** A sharp refutation with the surviving weaker
  statement beats a pile of analogies. Structural tensions in §5 of the brief
  are respected, not papered over.
- **L11 — Labbook lockstep** (TJO directive 2026-08-30). `labbook/` is the
  complete human-readable LaTeX record of the campaign: all definitions
  restated in full, every result with a descriptive name, full hypotheses,
  honest status, provenance, and numerics figures. NO campaign acronyms may
  be load-bearing in its prose; NO verbatim environments. Any commit that
  changes `claims/CLAIMS.md`, `definitions.md`, or lands a numerics result
  MUST update the owning labbook shard in the same commit.
  `scripts/check-labbook.sh` is the gate; it runs at session close. Style
  contract: `labbook/WRITING-GUIDE.md`.

## Layout

    refs/         fetched TeX ground truth (+ LEDGER.md)
    notation.md   symbol table (single source)
    definitions.md numbered definitions (single source)
    claims/       CLAIMS.md — the argument DAG
    theory/       TRIANGLE.md + proof shards + critic verdicts
    numerics/     Julia (TensorKit-first), tests in numerics/test/
    paper/        main.tex, appendices, figures/
    labbook/      sharded LaTeX labbook — the readable record (L11 lockstep)
    docs/         framing.md, novelty-sweep.md, worklog.md


<!-- BEGIN BEADS INTEGRATION v:1 profile:minimal hash:ca08a54f -->
## Beads Issue Tracker

This project uses **bd (beads)** for issue tracking. Run `bd prime` to see full workflow context and commands.

### Quick Reference

```bash
bd ready              # Find available work
bd show <id>          # View issue details
bd update <id> --claim  # Claim work
bd close <id>         # Complete work
```

### Rules

- Use `bd` for ALL task tracking — do NOT use TodoWrite, TaskCreate, or markdown TODO lists
- Run `bd prime` for detailed command reference and session close protocol
- Use `bd remember` for persistent knowledge — do NOT use MEMORY.md files

## Session Completion

**When ending a work session**, you MUST complete ALL steps below. Work is NOT complete until `git push` succeeds.

**MANDATORY WORKFLOW:**

1. **File issues for remaining work** - Create issues for anything that needs follow-up
2. **Run quality gates** (if code changed) - Tests, linters, builds; ALWAYS
   `scripts/check-labbook.sh` + `cd labbook && make` if claims/definitions/
   numerics changed (L11)
3. **Update issue status** - Close finished work, update in-progress items
4. **PUSH TO REMOTE** - This is MANDATORY:
   ```bash
   git pull --rebase
   bd dolt push
   git push
   git status  # MUST show "up to date with origin"
   ```
5. **Clean up** - Clear stashes, prune remote branches
6. **Verify** - All changes committed AND pushed
7. **Hand off** - Provide context for next session

**CRITICAL RULES:**
- Work is NOT complete until `git push` succeeds
- NEVER stop before pushing - that leaves work stranded locally
- NEVER say "ready to push when you are" - YOU must push
- If push fails, resolve and retry until it succeeds
<!-- END BEADS INTEGRATION -->
