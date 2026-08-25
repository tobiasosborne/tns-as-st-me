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
- **L7 — Model policy.** No Fable subagents. Opus for cognition-heavy work;
  Sonnet for search/mechanical; codex for proofs.
- **L8 — Cross-session state → bd** (prefix `tns-`). Insights → HANDOFF.md.
- **L9 — The paper is the product.** apsrev4-2, 4 pages main text, prose in
  the register of arXiv:1305.2176; exactly 3 main-text figures that tell the
  story in captions; full rigour in appendices/supplement. No overclaiming:
  every statement in the Letter traces to a PROVED claim or is labelled a
  conjecture.
- **L10 — Honest verdicts.** A sharp refutation with the surviving weaker
  statement beats a pile of analogies. Structural tensions in §5 of the brief
  are respected, not papered over.

## Layout

    refs/         fetched TeX ground truth (+ LEDGER.md)
    notation.md   symbol table (single source)
    definitions.md numbered definitions (single source)
    claims/       CLAIMS.md — the argument DAG
    theory/       TRIANGLE.md + proof shards + critic verdicts
    numerics/     Julia (TensorKit-first), tests in numerics/test/
    paper/        main.tex, appendices, figures/
    docs/         framing.md, novelty-sweep.md, worklog.md
