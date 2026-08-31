<!-- ADJUDICATION BRIEF r2 — SYK/JT (bd tns-62n). You are the same
     critic role as r1; treat theory/verdicts/syk-jt-joint-critic-r1.md
     as your prior. ADJUDICATE DELTAS: verify each claimed disposition
     by fresh recomputation; attack only text/code that changed since
     the r1 verdict (git diff 769bb8e..HEAD -- theory/lanes/syk-jt
     numerics/); do NOT re-litigate what already passed.
     YOUR LANE: write ONLY theory/verdicts/syk-jt-joint-critic-r2.md
     (+ scratch in /tmp; you may run code, mutation-test COPIES only).
     No bd operations. Work fully autonomously. -->

# Critic r2: adjudicate the r1 repairs

Read order: your r1 verdict → the two response tables
(`theory/lanes/syk-jt/repair-r1-t1-response.md`,
`repair-r1-t2-response.md`) → the diffs of the repaired artifacts →
`theory/lanes/syk-jt/observables-spec.md` (note the amended
"Permanent" bullet).

For each r1 objection (1,2,3,4,5,6,7,8): verify the claimed disposition
by recomputation, not by reading the table. Specifically:

- **O1/O2 (T1).** Confirm protocol (b) is actually retracted everywhere
  (grep for surviving unbalanced detector claims, including the verdict
  block and candidate sentence); confirm the single u_* is used
  consistently in (1.2), (3.x), (4.6)-(4.14), (5.3) — recompute the
  balanced plateau formula once with u_* shifted and check covariance.
- **O3.** Confirm the criterion is now stated at leading order with the
  a≠1 exact version separated.
- **O4 (T2).** Run the decoy RED yourself on a COPY with the repair
  reverted (re-introduce the circular tail) and confirm it fails; run
  the repaired suite; check the tail formula against the fitted matrix
  independently; verify the horizon-intercept convergence numbers.
- **O5.** Check Δ threading and the Δ=1 handshake path.
- **O6.** Check both lanes now state the iterated limit and cost; check
  the T_max convention obeys 1 ≪ κT ≪ κC as C → ∞; flag any place
  where the shot-cost numbers are used to claim more than they support.
- **O7/O8.** Verify pointers/typo.

Then rule: per-statement PROMOTE/HOLD for (i) the repaired T1 candidate
sentence (balanced-sector calibrated susceptibility + DC identity),
(ii) the butterfly-decay clause, (iii) the absolute-correlator
no-plateau statement — each with the exact scoping sentence you would
accept in a claims row (the proposer will copy it VERBATIM). Any NEW
objection found in changed text gets the full r1 format (location,
independent computation, fix demand, surviving statement, severity).
End with PASS or FAIL(ids).
