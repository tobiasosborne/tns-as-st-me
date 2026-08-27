# Work orders — round-1 critics for the memory-index campaign

Two independent critic runs, cross-family per rk-light (decorrelated blind
spots). Critic A (Fable) attacks theory/memory-index.md (codex T1 shard)
and theory/ansatz-scattering.md (codex T2 shard). Critic B (codex) attacks
theory/memory-index-b.md (Fable T1 shard). Each critic's lane is its
verdict file(s) ONLY:
  Critic A -> theory/verdicts/memory-index-r1.md and
              theory/verdicts/ansatz-scattering-r1.md
  Critic B -> theory/verdicts/memory-index-b-r1.md

## Role

You are the ADVERSARIAL CRITIC. Attack; do not summarize, do not referee
prose. Your obligations: independently RECOMPUTE the key steps, construct
counterexamples, audit quantifiers, audit lockstep with the single sources,
and never rely on a REFUTED DAG row.

## Read order

CLAUDE.md -> briefs/memory-campaign-target.md -> definitions.md ->
notation.md -> claims/CLAIMS.md -> theory/memory-quantization-general.md
-> your target shard(s) -> (Critic A also: refs/arxiv-1412.2970 TeX for
every claimed port; refs/arxiv-1810.07351 for any claimed BBDF technique).

## Mandatory attack surfaces (T1 shards — both critics)

1. **The two-time landmine.** Does the proof anywhere use "difference of
   lattice-valued observables is lattice-valued"? Q̂_W(t) and Q̂_W(-t) do
   not commute. Construct the 2x2 counterexample if the shard elides this.
2. **Weak-limit smearing.** Does the quantization step exchange a weak-*
   limit with a support statement without tightness? Exhibit the failure
   mode if the (LR) clause used is too weak to block it.
3. **Offset bookkeeping.** Recompute the lattice coset through the double
   limit (t first, W second) on an explicit small example (4-6 sites,
   s=1/2 AND an irrational s, e.g. s=0.37 — nothing may assume s ∈ ½ℤ).
4. **(LR) audit.** Is the proposed (LR)/D27 secretly equivalent to channel
   structure or completeness? If yes that guts the campaign — FATAL. Is it
   so weak the quantization step doesn't actually follow? Also FATAL.
   State the weakest (LR) under which the shard's own proof survives.
5. **Lemma L-A** (sector charge integrality): verify the claimed
   self-adjointness/existence of Q̂ on its stated domain, the scalarity of
   e^{2πiQ̂} (where exactly does D17 summability enter? where does A2
   covariance enter?), and that PURE POINT spectrum genuinely follows.
6. **(G-IDX.3) reduction.** Recompute the reduction to M-quant-G
   (G.1)-(G.2) line by line against theory/memory-quantization-general.md.
   Any mismatch of constants, conventions (D7/D8, D13(a) calibration), or
   quantifiers is FATAL.
7. **Quantifier + lockstep audit.** Every leaf must cite a D-number, claim
   id, named computation, or refs/ file+location; flag every leaf that
   cites from memory. Flag every place the shard's MERGE PROPOSALS would
   silently strengthen an existing DAG row.

## Mandatory attack surfaces (T2 shard — Critic A additionally)

8. For every lemma ported from refs/arxiv-1412.2970: open the TeX, find
   the original, and determine whether the port RE-DERIVES or ANALOGIZES.
   Identify each use of vacuum translation invariance in the original and
   check the shard's kink-sector substitute actually does the work
   (fibering of the A2 translation action, Arveson spectrum arguments).
9. Threshold inequalities: are the inelastic-exclusion inequalities stated
   purely in band data, and are they USED where claimed (Cook integral
   convergence)? Construct the absorption counterexample if the kink
   bandwidth condition is missing.
10. Confirm NO soft-limit (k->0) claim survives anywhere; velocity
    separation is a standing hypothesis.

## Verdict format (rk-light; a verdict without (c)+(d) is invalid)

Numbered objections, each: severity FATAL/MAJOR/MINOR/NOTE + (a) exact
location (file + Lamport step id), (b) YOUR independent computation or
counterexample, (c) one-line FIX DEMAND, (d) the SURVIVING WEAKER
STATEMENT. Final line: PASS (no FATAL/MAJOR) or FAIL(ids). If the shard's
CHECKER SPEC is implementable, say whether its mutation would actually
fail; do not implement it.

Work fully autonomously; never ask questions. Do not edit anything except
your verdict file(s).
