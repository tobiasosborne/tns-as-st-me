# Work order — r2 adjudication (Opus critic, deltas only)

You are the ROUND-2 ADJUDICATOR for the memory-index campaign. Round 1
verdicts exist and are your priors; do NOT re-litigate what passed r1.
Adjudicate the deltas by fresh recomputation and issue explicit
PROMOTE/HOLD decisions per claim row. Your lane: exactly one file,
theory/verdicts/memory-index-r2.md (one verdict covering both shards).

## Priors and baselines

- theory/verdicts/memory-index-r1.md — PASS baseline for
  theory/memory-index.md at commit a67e61b; the current text is the
  round-2 synthesis. Scope your T1 audit to
  `git diff a67e61b -- theory/memory-index.md` plus the lane-B imports.
- theory/verdicts/memory-index-b-r1.md — FAIL(1-6); verify each claimed
  disposition in the synthesis report (the surviving-statement lines are
  the ONLY licensed strength for lane-B imports).
- theory/verdicts/ansatz-scattering-r1.md — FAIL(1,2,3,4); verify each row
  of the shard's §6 repair-response table by recomputation, and adjudicate
  the repairer's five self-flagged risks (two-sided D28-C pricing;
  truncation-radius uniformity in ACE-Gram; unverified ACE-C2 red
  scalings; the HΩ_γ=0 leaf; L2 length).

## Obligations

1. Recompute, don't referee: the ⟨1⟩8.⟨2⟩2 AD3-topology lemma, the
   ⟨1⟩9 density derivation (both tails; check no hidden use of D13's s),
   the ⟨1⟩11 characteristic-function formulas, the repaired T_M/T_K Cook
   majorant (verify the |t|^{-3} claim from the S(u) split), and the
   ⟨1⟩6.⟨2⟩1 four-cluster derivation (attack the truncation-radius
   uniformity specifically).
2. Lockstep audit: definitions.md D26/D27/D28, notation.md rows, and the
   seven new claims/CLAIMS.md rows must match the shards exactly — flag
   any silent strengthening in either direction. Check the AD3-ex row and
   the M-INDEX-LA-strong REFUTED row citations resolve.
3. Checkers: run `python3 -O` on theory/checks/memory_index_probe.py and
   theory/checks/memory_index_check.py, green and --red modes; mutation-
   test ONE additional hypothesis of your choosing on a COPY in /tmp.
4. Quantifier audit on the two theorem statements (M-INDEX-spec, AC-EX)
   as they appear in the DAG rows — the row text is what gets cited later;
   it must not exceed the shard.
5. L2: both shards exceed 200-500 lines (976 and 774) with proposed
   splits — rule on whether the splits are mandatory before promotion or
   post-promotion hygiene.

## Decisions required (explicit, one line each, with scoping sentence)

PROMOTE or HOLD (with the missing step named) for: M-INDEX-fin,
M-INDEX-spec, M-IDX-density, AC-EX. Confirm or reject the REFUTED status
of M-INDEX-LA-strong and the CONJECTURE registers of M-INDEX-LA-folium and
AD3-ex. For every PROMOTE, write the exact scoping sentence to be copied
into the DAG (the proposer applies it verbatim).

Verdict format: numbered objections (severity, location, your computation,
FIX DEMAND, SURVIVING WEAKER STATEMENT), then the decision table, then
PASS or FAIL(ids). Work fully autonomously; never ask questions.
