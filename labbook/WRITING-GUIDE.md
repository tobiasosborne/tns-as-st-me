<!-- ROLE: binding style contract for every labbook shard. TJO directive
     2026-08-30: "I want it to be truly easy to read, so err on the side of
     more definitions. No verbatim markdown! Completely faithful to all the
     results of the campaign, actual latex equations, no verbatim text
     environments." Every writer (human or agent) reads this FIRST. -->

# Labbook writing guide (binding)

## Audience and register

The reader is a professional theoretical physicist (TJO) who has NOT
memorised any campaign jargon. The document must be readable front to back
without ever consulting `claims/CLAIMS.md`, `definitions.md`, or a theory
shard. Register: calm, plain scientific prose, as in a good lecture-notes
chapter. No hype, no process narrative (no "the critic found...", no lane
history) except where an erratum or refutation is itself the content.

## The ten rules

1. **Human names first, campaign ids as metadata only.** Every definition,
   theorem, and conjecture gets a DESCRIPTIVE ENGLISH NAME, e.g.
   "Theorem (Windowed memory is quantized without scattering theory)".
   The campaign id (`M-INDEX-fin`, `D26`, ...) appears ONLY in the
   `\provenance` block after the statement and in the dictionary shard.
   Body prose NEVER says "by S-IDX-fin-r2"; it says "by the finite soft-index
   theorem (Theorem \ref{...})".

2. **No verbatim environments.** No `verbatim`, `lstlisting`, `alltt`,
   `minted`, no pasted markdown, no code blocks. File paths are typeset
   inline with `\texttt{...}` inside provenance blocks only. Checker names
   likewise. Everything else is prose and mathematics.

3. **Real mathematics.** Every formula from the sources is typeset as actual
   LaTeX math (`equation`, `align`, inline `$...$`). Translate the sources'
   Unicode/markdown math faithfully: `⟨1⟩3`-style Lamport anchors are cited
   in provenance as e.g. "step (1.3)", `\|ψ⟩` becomes `\ket{\psi}`, `Σ_x`
   becomes `\sum_x`, etc. Never paste source text raw.

4. **Faithful statements, full hypotheses.** A theorem statement carries ALL
   its hypotheses and its exact scope. The "NOT claimed" material of a
   CLAIMS.md row becomes a `\begin{scope}...\end{scope}` environment right
   after the theorem — readable prose, not a defensive list dump. Statuses
   must match `claims/CLAIMS.md` EXACTLY; a conditional PROVED row is
   `\statusProvedConditional` with the condition displayed in the statement.
   Never strengthen, never drop a qualifier, never round a status up.

5. **Definitions are restated in full**, not pointed to. Where a definition
   has frozen clauses (D6–D8), reproduce them faithfully. Where a definition
   is long (D24), structure it with named clauses. Err on the side of MORE
   definitional material: if a term is used, it is defined in this document.

6. **Every statement gets provenance.** Immediately after each definition /
   theorem / conjecture body (and its scope remark), place
   `\provenance{<ids>}{<proved in>}{<tested by>}{<reviewed in>}` with the
   repo file, step anchor, checker script, and verdict file from the
   CLAIMS.md row. Use `---` for empty fields.

7. **Proof ideas, not proof transcripts.** After a PROVED theorem give a
   short paragraph ("Idea of proof.") conveying the mechanism in prose +
   key displayed equations. The Lamport shard remains the ground-truth
   proof; the labbook must make the reader understand WHY it is true.
   For SKETCH rows, say precisely what is proved and what is missing.

8. **Refutations are content.** Every REFUTED row is presented as a
   `refutedclaim` environment: the withdrawn statement, the counterexample
   or mechanism that killed it, and the surviving weaker statement with a
   cross-reference. Same for errata (e.g. the two-magnon Ward projection
   erratum).

9. **Cross-reference by `\label`/`\cref`.** Labels: `def:` prefix for
   definitions (`def:window-charge`), `thm:`/`conj:`/`ref:` for results,
   chosen as readable slugs. Never refer to "row 37 of the table".

10. **Shard hygiene.** One `\section` per shard file, opened by a header
    comment block:
    ```
    % SHARD-ID: LB-NN-<LABEL>
    % SHARD-TITLE: <human title>
    % SHARD-SOURCES: <the repo files this shard is faithful to>
    % SHARD-CLAIMS: <the CLAIMS.md ids and D-numbers this shard owns>
    ```
    Compile-clean standalone LaTeX (it is `\include`d by `main.tex`; do not
    add `\documentclass` or `\begin{document}`). Use only the macros of
    `main.tex`'s preamble plus standard amsmath. If you need a new semantic
    macro, define it at the top of your shard with a comment.

## Status legend (matches claims/CLAIMS.md)

- `\statusProved` — Lamport proof survived the capped hostile loop.
- `\statusProvedConditional` — proved as a conditional implication; the
  condition is displayed in the statement, never hidden.
- `\statusSketch` — argument exists, named gaps remain; the gaps are stated.
- `\statusConjecture` — precise statement, no proof; evidence is described.
- `\statusRefuted` — false as stated; the killing mechanism is presented.

## Lockstep maintenance rule

Any commit that changes a claim status, adds a claim, or edits a definition
MUST update the owning shard in the same commit. `scripts/check-labbook.sh`
greps every CLAIMS.md id and D-number against `labbook/sections/` and fails
if one is missing. The labbook may never go stale: this is enforced at
session close alongside the git-push rule.
