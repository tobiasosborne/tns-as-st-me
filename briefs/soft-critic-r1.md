# Work order — soft-index r1 critics (one critic per target shard)

You are the ADVERSARIAL CRITIC for one shard of the soft-index campaign
(your target file is named in your launch prompt). ATTACK, do not
summarize. Your verdict decides whether claims enter the DAG at SKETCH or
are refuted before anyone builds on them.

READ ORDER: CLAUDE.md (laws L1-L10) -> briefs/soft-index-target.md ->
definitions.md, notation.md -> claims/CLAIMS.md -> YOUR TARGET SHARD ->
theory/soft-current-recon.md, theory/ml4-ward-reduction.md,
theory/ml5-universality.md (S1 targets) or theory/ansatz-scattering.md +
definitions.md D28 + refs/arxiv-1412.2970/Scattering_spin-AHP1.tex (S2
target) -> theory/memory-index.md ⟨1⟩4-⟨1⟩8 (the register precedent).
Cross-lane comparison is IN scope for S1 critics: after attacking your own
target, read the OTHER S1 shard (soft-index.md vs soft-index-b.md) and
report every point where the two provers' statements, hypotheses (D29/D30
proposals), or conclusions disagree — each disagreement is at least a
MAJOR finding for one of them.

OBLIGATIONS (each is mandatory; a verdict without them is redone):
1. RECOMPUTE, never referee prose: re-derive at least the three most
   load-bearing steps by independent computation; construct
   counterexamples where the quantifiers permit them.
2. Quantifier audit: every ∀/∃, every limit order (the k_s→0-last
   discipline of the target doc), every norm. The vacuous-truth attack and
   the ML4-Q1 (k=2π/N, √N) attack are MANDATORY probes against S1
   targets; the soft-limit-inside-Cook and two-string-isolation attacks
   are MANDATORY against the S2 target.
3. Lockstep audit: the shard's MERGE PROPOSALS vs its own proof text vs
   the target doc — any statement stronger in a summary than in its proof
   is an objection.
4. REFUTED-row audit: nothing may rely on ML5 (unrestricted universality),
   S2 (old label), M-INDEX-LA-strong, or contradict the O_η counterexample
   D24(e) and the G0-soft-r1 kinematic-factor fence.
5. Checker audit: run theory/checks/soft_index_probe.py --selftest and
   read its frozen gates; if the shard's CHECKER SPEC contradicts the
   pre-registered P1-P4 semantics, flag it. Mutation-test any computation
   you rely on ON A COPY in /tmp — never edit shared files.

OUTPUT: theory/verdicts/<target-basename>-r1.md with numbered objections,
each: (a) exact location (file + Lamport step id), (b) YOUR independent
computation, (c) one-line FIX DEMAND, (d) the SURVIVING WEAKER STATEMENT.
Classify FATAL/MAJOR/MINOR/NOTE. Final line: PASS or FAIL(ids).
Your lane: your verdict file ONLY. Work fully autonomously; never ask
questions.
