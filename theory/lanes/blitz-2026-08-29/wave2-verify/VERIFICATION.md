# Wave-2 verification report

## WIP inventory

`git show --stat` identifies these files:

| File | Commit action |
|---|---|
| `numerics/src/lambdaD_edge.jl` | added by `e235db1` |
| `numerics/src/lambdaD_memory.jl` | added by `e235db1` |
| `numerics/src/lambdaD_memory_run.jl` | added by `e235db1` |
| `numerics/scripts/run_lambdaD_memory.jl` | added by `e235db1` |
| `numerics/test/test_lambdaD_memory.jl` | added by `e235db1` |
| `numerics/results/lambdaD-kink-dispersion.json` | added by `e235db1` |
| `numerics/results/lambdaD-kink-memory-convergence.json` | added by `e235db1`, then extended by `4be259a` |

Commit `4be259a` adds the `chi_max=48` convergence row and changes the timestamp;
it touches no code.  The intended `chi_max=64` third row is absent.

## Requested executions

| Command | Result | Evidence |
|---|---|---|
| `julia --project=numerics ... numerics/test/runtests.jl` | **BLOCKED**, not a test verdict: 828 passed before the loader reached `test_lambdaD_groundstate.jl`, then `using MPSKit` errored | `full-suite.log` |
| `julia --project=numerics ... numerics/test/test_lambdaD_memory.jl` | **BLOCKED** before its module loaded: `MPSKit ... does not seem to be installed` | `wave2-specific.log` |
| lane-local `Pkg.instantiate()` | **BLOCKED**: `MPSKit` is a direct dependency but is absent from the committed manifest | `instantiate.log` |
| lane-local copied-environment `Pkg.resolve(); Pkg.instantiate()` | **BLOCKED**: DNS/network cannot reach Julia package server or GitHub | `resolve-instantiate.log` |

Thus neither the historical 3,787-green baseline nor any wave-2 assertion was
confirmed in this environment.  Parsing all five new Julia files with Julia's
parser succeeds (`parse_wave2.jl`, `parse-wave2.log`), but parsing is not a test.

## Wave-2 assertion audit

The shard contains 50 source `@test` expressions.  The two predicates inside
`for r in (rh, rd)` execute twice, so a successful run should record 52 wave-2
assertions.  Every source test has a falsifiable Boolean predicate; none merely
calls code and passes when no exception occurs.  The expensive `SEC`, `EK0`,
`PHI0`, and `PSI0` construction is global setup outside the testsets, so setup
failure appears as an error rather than as a failed assertion.

| Testset | Source / executed assertions | Classification | What can turn it red |
|---|---:|---|---|
| two Néel vacua and calibration | 6 / 6 | REAL ASSERTIONS | wrong orientation, tail density, or vacuum energy |
| topological-sector dispersion | 7 / 7 | REAL ASSERTIONS | wrong sector, sign/order, symmetry, or trivial-sector separation |
| dressed packet vs sharp junction | 4 / 4 | REAL ASSERTIONS, including an explicit negative control | off-band dressed packet, on-band sharp control, or malformed wall |
| LD-ID and probability law | 4 / 4 | REAL ASSERTIONS | identity, normalization, positivity, or first-moment defect |
| integer support vs nonquantized position | 4 / 4 | REAL ASSERTIONS, including two explicit negative controls | wrong coset phase/modulus or loss of the signed-measure contrast |
| transport, velocity, coefficient | 10 / 10 | REAL ASSERTIONS | norm/energy drift, nonfinite readout, velocity/coefficient disagreement, estimator mismatch |
| Haldane vs large-D edge memory | 9 / 11 | REAL ASSERTIONS | DMRG/TDVP defect, lost Haldane moment, insufficient relaxation, or large-D moment |
| JSON records | 6 / 6 | REAL BUT SHALLOW SCHEMA ASSERTIONS | missing keys, wrong dressing tag, or nonfinite top-level value |

Static classification does not replace red/green execution.  In particular,
the coefficient predicate is not a no-op, but it is closely related to the
separate `dx_X1`/`dx_X2` agreement gate through the exact LD-ID identity; a pass
would validate this numerical realization, not independently prove the law.

## Independent arithmetic check of 1.9184

`check_results.py` ignores each stored coefficient and recomputes it from the
stored raw quantities as `-nu_mean_escaped_charge / dx_X2_centroid`.  It also
gets `s` independently from the matching `chi=16` dispersion row and recomputes
`2s`.  Results (`check-results.log`):

| `chi_max` | recomputed `-nu/dx` | recomputed `2s` | relative difference |
|---:|---:|---:|---:|
| 32 | 1.918387433219214 | 1.920679955492809 | 0.119359931% |
| 48 | 1.918400884963647 | 1.920679955492809 | 0.118659568% |

This confirms the committed row arithmetic and the stated “1.9184 vs 1.9207
(0.12%)” description.  It is not an independent TDVP recomputation; that is
blocked by the unavailable dependency.  The same checker validates the three
dispersion rows' schema, positivity, reflection symmetry, gap, bandwidth, and
cross-row calibration.  Its `--mutate` mode corrupts the first coefficient by
`+0.1` and exits 1 (`check-results-mutation.log`), demonstrating red capability.

## File verdict

| File | Verdict | Reason |
|---|---|---|
| `lambdaD-kink-memory-convergence.json` | **BROKEN (incomplete)** | only ranks 32 and 48 of declared 32/48/64 exist; the two present rows are internally consistent |
| `lambdaD-kink-dispersion.json` | **UNTESTED** | strong internal consistency checks pass, but no independent solver run was possible |
| `test_lambdaD_memory.jl` | **UNTESTED** | 50 real source assertions parse, but zero executed here |
| `lambdaD_memory.jl` | **UNTESTED** | parses and has assertion coverage on paper; dynamic coverage unavailable |
| `lambdaD_memory_run.jl` | **UNTESTED** | parses and has assertion coverage on paper; dynamic coverage unavailable |
| `lambdaD_edge.jl` | **UNTESTED** | parses and has assertion coverage on paper; dynamic coverage unavailable |
| `run_lambdaD_memory.jl` | **UNTESTED** | parses, but no production stage was rerun; expected transport/edge result files are absent |

No WIP file reaches **TRUSTWORTHY** on the evidence available in this lane.

## Exact wave-2 relaunch instruction

Relaunch `tns-f5r` wave 2 in an environment with network access or a populated
Julia depot, and do not promote any WIP file until all commands below succeed:

```bash
cd /home/tobias/Projects/tns-as-st-me/numerics
julia --project=. --startup-file=no -e 'using Pkg; Pkg.resolve(); Pkg.instantiate()'
julia --project=. --startup-file=no --color=no test/test_lambdaD_memory.jl
julia --project=. --startup-file=no --color=no test/runtests.jl
julia --project=. --startup-file=no --color=no scripts/run_lambdaD_memory.jl dispersion
julia --project=. --startup-file=no --color=no scripts/run_lambdaD_memory.jl converge
julia --project=. --startup-file=no --color=no scripts/run_lambdaD_memory.jl transport
julia --project=. --startup-file=no --color=no scripts/run_lambdaD_memory.jl edge
```

Acceptance requires 52 wave-2 assertions green, the full prior 3,787 plus those
52 green if no other tests changed, convergence ranks exactly `[32,48,64]`, and
fresh transport and edge JSONs.  Recompute `-nu/dx` from fresh raw fields rather
than trusting the serialized coefficient.
