<!-- REPAIR BRIEF r1, lane T2 (numeric). bd tns-62n.
     YOUR LANE: edit numerics/src/schwarzian_memory.jl,
     numerics/test/test_schwarzian_memory.jl,
     numerics/results/schwarzian_memory.json,
     theory/lanes/syk-jt/t2-numeric.md; create
     theory/lanes/syk-jt/repair-r1-t2-response.md. Nothing else.
     No bd operations. Work fully autonomously. -->

# Repair r1 for the numeric lane

Work order: `theory/verdicts/syk-jt-joint-critic-r1.md`, objections 4, 5,
and your half of 6. Red-green discipline: for O4 write the failing test
FIRST — a test that FAILS on the current circular implementation (e.g.
feed a synthetic response whose true DC differs from late_delta and
assert the transform recovers the truth, not the supplied tail), watch
it fail, then fix.

- **O4 (MAJOR, circular DC).** Remove the target-valued tail from the
  ω→0 test: obtain the tail coefficient independently (from the fitted
  post-pulse Möbius matrix, or by transforming the source/vertex
  response directly), vary the numerical horizon, extrapolate ω→0, and
  only then compare against the separately computed late detector.
  Report the repaired DC/late and DC/vertex columns for all eight rows;
  a changed number is a result, not a failure.
- **O5 (MINOR).** Un-hard-code Δ in the observable API (parameter with
  the value recorded in the JSON); keep the handshake Δ=1 path working.
- **O6 (window).** Add to report and JSON: the iterated-limit convention
  (C → ∞ first, 1 ≪ κT ≪ κC, per observables-spec.md), the maximum
  usable T at each parameter point under that convention, and the
  sample-cost estimate for the ratio detector at that T.

Rerun the full suite green (standalone: `julia --project=numerics
numerics/test/test_schwarzian_memory.jl`), regenerate the JSON through
the finiteness gate, update the report's results tables in place.
Output also `repair-r1-t2-response.md`: one row per objection,
id → FIXED / DOWNGRADED / RESIDUE, exact edit location, plus the RED
evidence for the new O4 test.
