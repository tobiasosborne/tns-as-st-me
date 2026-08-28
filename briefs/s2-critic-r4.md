# Critic brief — AC-EX-2M round 4 (adjudication round)

Read `briefs/critic-protocol.md` first — **including its "Standing checker
obligations" section** — everything there binds.

**TARGET:** `theory/ansatz-scattering-2m.md`,
`theory/ansatz-scattering-2m-r3-response.md`,
`theory/checks/ansatz_scattering_2m_check.py`.
**VERDICT FILE (your only writable file):**
`theory/verdicts/ansatz-scattering-2m-r4.md`.

**ADJUDICATION round.**  Priors: `ansatz-scattering-2m-r1.md`, `-r2.md`,
`-r3.md`.  Trajectory so far **6 → 2 → 1 MAJOR, 0 FATAL throughout**.  Scope
with `git diff`; verify the 15 claimed dispositions (R3-O1…O7, R3-N1…N8) by
fresh recomputation; attack what changed; do NOT re-litigate settled text, and
do not churn r3 §7's fenced VERIFIED CORRECT list.  A fourth round should
reach 0 MAJOR — but only if it has actually earned it.

## What the prover claims

It took **branch (ii)**: the r3 MAJOR is answered by DOWNGRADE, not by proof.
The shard now states that the theorem does not apply to the adjudicated D29,
preserves the Haag--Ruelle creator-independence theorem as a theorem about HR
creator families, and claims **byte-for-byte lockstep** with the `AC-EX-2M`
row the orchestrator merged into `claims/CLAIMS.md` at SKETCH (that row's
scoping sentence is the r3 critic's own words, applied verbatim).

## Attack these, in priority order

1. **Is the downgrade complete, or only announced?**  The quarantine sentence
   appears six times in the shard.  Saying it six times is not the same as
   *obeying* it.  Walk every step that uses `(ACE2M-LSZ)` or `(A2M.3)`'s
   channel identification and check that none of them still reads the D29
   identification as available — in particular anywhere Lane S1 would consume
   it.  A downgrade that leaves one load-bearing step unchanged is worse than
   no downgrade, because the row now advertises the fence.
2. **Lockstep, byte-for-byte.**  The prover claims an exact match to the
   merged CLAIMS row.  Diff them yourself, character by character.  Any drift
   — including "adding a true statement" — is silent strengthening and is
   reportable at MAJOR.
3. **THE CHECKER — R3-O2 RECURRENCE RISK, treat as the round's centre of
   gravity.**  Last round I found the profile-agreement gate was a *rescaled
   duplicate* of the agreement gate: folding `w_Cw_D` into the constant in
   BOTH routes passed every gate.  The prover has replaced it with a
   `ratio_route` gate.  **Determine whether the replacement is a genuine
   independent test or the same defect in new clothes.**  Apply every standing
   obligation: simplify the new gate symbolically; feed it absurd inputs;
   redo the two-sided support-fold mutation on a copy and confirm it now
   FAILS; report the **exit path** for each red mode (which gate killed it),
   not merely the exit code; and check whether `ratio_route` is deductively
   subsumed by the agreement or monotonicity gates.
4. **The preserved HR theorem.**  It survived r3 with every citation
   resolving.  Confirm it is unchanged and that its hypotheses are still
   owned — the downgrade must not have quietly widened it to compensate for
   the lost D29 application.
5. **The six MINORs and eight NOTEs.**  Verify each disposition; R3-O5 (the
   isolated-mass-shell hypothesis un-owned on D6, rescued only by an
   undisplayed `S^z`-sector relativization) and R3-O6 (filter transparency)
   are the two most likely to have been answered with words rather than a
   displayed step.

## Deliverable beyond the standard format

- The r4 MAJOR count against the trajectory (6 → 2 → 1 → ?), with an explicit
  statement of whether severity is still falling monotonically.
- A **PROMOTE / HOLD** decision for `(A2M.3)`'s interface clause (HELD at r3,
  missing step named there) and for `AC-EX-2M` as a whole.  The row currently
  sits at SKETCH.  If you judge it should move, supply the exact replacement
  scoping sentence verbatim — the orchestrator applies it without paraphrase.
  If it should stay at SKETCH, say what would move it and what remains open.
