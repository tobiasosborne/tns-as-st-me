# ACE-LD reachability and guard certificate

STATUS: PROVED-candidate (computational statement only)

⟨1⟩1. **ASSUME** the lane-local copy `ace_ld_check.py`, its 23-mode
`REGISTRY`, and the production dispatch order in `_run_battery`.

⟨2⟩1. The registered modes capable of entering `check_c5b` or `check_c6`
are the three `barrier2` modes and the three `c6` modes in the table below.

_Justification:_ `measure_reachability.py` executes these six registered
builders through `_run_battery`; `logs/full-red.log` records all 23 registry
entries and their battery-specific exits.

⟨1⟩2. **PROVE** the actual sub-gates evaluated before each relevant mutant
exits are exactly:

| registered mode | measured gates reached | dies at |
|---|---|---|
| `c5b-flat` | `C5b-WEDGE` | `C5b-WEDGE` |
| `c5b-concentrated` | `C5b-WEDGE` | `C5b-WEDGE` |
| `c5b-nobarrier` | `C5b-WEDGE`, `C5b-CESARO-FLOOR` | `C5b-CESARO-FLOOR` |
| `c6-static` | `C6-MOMENT`, `C6-SUPPORT`, `C6-LIVENESS` | `C6-LIVENESS` |
| `c6-moving` | `C6-MOMENT` | `C6-MOMENT` |
| `c6-weaktransit` | `C6-MOMENT`, `C6-SUPPORT` | `C6-SUPPORT` |

⟨2⟩1. Each passing or failing `require` call is tagged before the original
exception behavior is preserved, so a gate is counted when evaluated, not
only when it fails.

_Justification:_ named computation `measure_reachability.py`; measured output
`logs/reachability-green.log` (exit 0).

⟨2⟩2. A deliberately false expected row adding `C5b-STABILITY` to
`c5b-nobarrier` is rejected.

_Justification:_ named computation `measure_reachability.py
--red-expected-stability`; `logs/reachability-red.log` (intentional exit 1,
`RED-OK`).

⟨2⟩3. QED for ⟨1⟩2.

_Justification:_ ⟨2⟩1--⟨2⟩2 and named computation
`measure_reachability.py`.

⟨1⟩3. **PROVE** no registered mutation reaches `C5b-STABILITY` or
`C6-SWEEP`, and name the shadowing exits.

⟨2⟩1. `C5b-STABILITY` is shadowed by `C5b-WEDGE` for `c5b-flat` and
`c5b-concentrated`, and by `C5b-CESARO-FLOOR` for `c5b-nobarrier`.

_Justification:_ ⟨1⟩2 table; named computation `measure_reachability.py`.

⟨2⟩2. `C6-SWEEP` is shadowed respectively by `C6-LIVENESS`, `C6-MOMENT`,
and `C6-SUPPORT` for `c6-static`, `c6-moving`, and `c6-weaktransit`.

_Justification:_ ⟨1⟩2 table; named computation `measure_reachability.py`.

⟨2⟩3. Both shadowed gates nevertheless have teeth: tightening only
`C5B_LR2_STAB` to `1e-6` fires stability at measured spread `4.882e-05`,
and tightening only `C6_MOM_BOUND` to `1.0` passes the protocol-time gate
before firing the sweep at `1.0712`, `t_+=20`, `W=[3,8]`.

_Justification:_ named computation `mutation_probes.py` and
`logs/mutation-probes.log`.

⟨2⟩4. QED for ⟨1⟩3.

_Justification:_ ⟨2⟩1--⟨2⟩3, each backed by the named computations above.

⟨1⟩4. **PROVE** the shipped double-Cesàro spans satisfy an executable
no-wrap ceiling derived from `N_BAR`.

⟨2⟩1. The protocol reaches `|t|=2T` and the stated maximum group speed is
2, so the travel bound is `4T`; requiring `4T < N_BAR/2` gives
`T < N_BAR/8 = 256` at `N_BAR=2048`.

_Justification:_ named computation `mutation_probes.py` evaluates the derived
constant and the guard; `logs/mutation-probes.log`.

⟨2⟩2. The shipped spans `(20,40)` pass, while the boundary mutation
`(20,256)` is rejected before any wrapped double-Cesàro computation.

_Justification:_ named computation `mutation_probes.py` and its green/red
lines in `logs/mutation-probes.log`.

⟨2⟩3. QED for ⟨1⟩4.

_Justification:_ ⟨2⟩1--⟨2⟩2 and named computation `mutation_probes.py`.

⟨1⟩5. **PROVE** the repaired copy preserves the broader checker behavior.

⟨2⟩1. The unmutated checker exits 0 with LD-C1--LD-C7 green.

_Justification:_ named computation `ace_ld_check.py`; `logs/green.log`.

⟨2⟩2. The full 23-mode mutation battery exits 1 with `RED-OK` and every
registered pattern reproduced.

_Justification:_ named computation `ace_ld_check.py --red`;
`logs/full-red.log`.

⟨2⟩3. QED for ⟨1⟩5.

_Justification:_ ⟨2⟩1--⟨2⟩2 and the named checker computations.

⟨1⟩6. **QED.** The two gates belong in the measured unreached disclosure,
the unqualified completeness claim must be removed, and the configuration
must enforce `T < N_BAR/8`; these are precisely the edits in the copied
artifacts and `PATCH.md`.

_Justification:_ ⟨1⟩2--⟨1⟩5 and the named computations cited at every leaf.
