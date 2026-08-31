# Repair r1 response — SYK/JT numeric lane T2

## Failing-first evidence for O4

Before changing `numerics/src/schwarzian_memory.jl`, I added a regression that
runs the same response twice while changing only the supplied late-detector
comparison from `late` to `2late`.  The absolute Fourier residue must be
invariant.  The unmodified circular implementation failed:

```text
$ julia --project=numerics numerics/test/test_schwarzian_memory.jl
bilocal model comparison and DC convergence: Test Failed
  isapprox(decoy_residue, residue; rtol = 0.01)
  Evaluated: isapprox(5.067586228816479e-5,
                      0.00012306912331812398; rtol = 0.01)
Test Summary: sourced two-sided Schwarzian memory | 81 pass, 1 fail, 82 total
exit code: 1
```

This is a targeted circular-DC RED: the trajectory and fitted post-pulse
matrix are unchanged, so only illicit use of the supplied detector in the
tail can move the residue.

## Disposition

| objection | disposition | exact repair location |
|---|---|---|
| O4 | **FIXED** | `numerics/test/test_schwarzian_memory.jl:100-132` (decoy RED/regression, horizon and intercept gates); `numerics/src/schwarzian_memory.jl:296-338` (tail from fitted Möbius matrix, horizons 20/40/80, low-frequency `omega^2` intercept); `theory/lanes/syk-jt/t2-numeric.md:99-114,158-216`; every JSON row under `dc` |
| O5 | **FIXED** | `numerics/src/schwarzian_memory.jl:200-227,268-294,397-500` (`Delta` threaded through observable, vertex, DC, point, and campaign APIs); `numerics/test/test_schwarzian_memory.jl:135-149` (`Delta=1` A1 correlator handshake and invalid-Delta gate); JSON `operator_dimension` |
| O6 (T2 half) | **FIXED** | `numerics/src/schwarzian_memory.jl:397-457,471-498`; `numerics/test/test_schwarzian_memory.jl:171-180`; `theory/lanes/syk-jt/t2-numeric.md:218-253`; JSON `limit_convention` and each row's `detector_window` |

## Repair results

- The transform tail is now
  `(|det(M)/M_11^2|^Delta-1)/(Delta*(1+k_f))`, obtained from the fitted
  post-pulse matrix.  The separately evaluated `Delta u_rel(40)` is used only
  after the `omega -> 0` extrapolation.  The eight repaired `DC/late` values
  span `0.999795--0.999975`; `DC/vertex` spans
  `0.997668--1.000110`.
- The three horizons are `20,40,80`; the largest relative change between the
  last two horizon intercepts is `3.65e-8`.
- The finite-C proxy declares `kappa=(1+k_f)/2` and
  `kappa*T_max=sqrt(kappa*C)`, which obeys the required iterated scaling as
  `C -> infinity`.  It is explicitly labeled a convention rather than a
  uniform error theorem.  Each row records `T_max`, `kappa*T_max`, `T_max/C`,
  `Delta u(T_max)`, the exponential shot factor, and the estimated shots for
  `eta=0.1|Delta u_fit|`.  The report flags that `C=10` has no broad
  parametric late-time window and that the `C=100` cost is already
  `10^18--10^21` shots under this estimate.

Final standalone result:

```text
$ julia --project=numerics numerics/test/test_schwarzian_memory.jl
Test Summary:                       | Pass  Total   Time
sourced two-sided Schwarzian memory |   96     96  15.8s
exit code: 0
```

The green run regenerated `numerics/results/schwarzian_memory.json` only after
the finiteness, nonempty-sample, and charge-ledger gates passed.
