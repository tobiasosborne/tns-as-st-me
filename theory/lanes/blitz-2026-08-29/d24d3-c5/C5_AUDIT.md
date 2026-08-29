# C5 gate-subsumption audit

**ASSUME** the execution order and formulas in the lane-local copy
`d24d3_normalization_check.py`.  **PROVE** that C4 deductively implies both
old C5 predicates, so deleting their `require()` calls makes C5 honestly
DISPLAY without changing checker acceptance.

⟨1⟩1. **ASSUME** execution reaches `check_defect`. **PROVE** the old
`S=1/2` C5 predicate is true.

⟨2⟩1. C4 has already returned, hence every row at spin `S` obeys
`|measured - 1/S| S < 0.08`.  (Named computation: `verify_repair.py`.)

⟨2⟩2. The mean at a fixed spin obeys the same strict bound because the
absolute deviation of a mean is at most the maximum absolute row deviation.
(Named computation: `verify_repair.py`.)

⟨2⟩3. At `S=1/2`, the frozen prediction and C4 target coincide:
`predicted_jet(0.5, None) = 2 = 1/0.5`; therefore the displayed C5 deviation
is strictly below `0.08`.  (Named computation: `verify_repair.py`.)

⟨2⟩4. QED.

⟨1⟩2. **ASSUME** execution reaches `check_defect`. **PROVE** every old
off-`S=1/2` C5 predicate is true.

⟨2⟩1. By ⟨1⟩1/⟨2⟩2, the mean satisfies
`|mean_S - 1/S| S < 0.08`.  (Named computation: `verify_repair.py`.)

⟨2⟩2. The reverse triangle inequality gives
`|2 - mean_S| S > 2S - 1 - 0.08`.  (Named computation:
`verify_repair.py`.)

⟨2⟩3. For `S=1, 3/2, 2`, those lower bounds are respectively
`0.92, 1.92, 2.92`, each strictly above `0.08`; hence all three old C5
predicates hold.  (Named computation: `verify_repair.py`, saved output
`verify_repair.out`.)

⟨2⟩4. QED.

⟨1⟩3. **PROVE** deletion of the two C5 guards does not change checker
acceptance.

⟨2⟩1. If C4 fails, `fail()` exits before `check_defect` is called; if C4
passes, ⟨1⟩1 and ⟨1⟩2 show that every deleted guard is true.  (Named
computation: `verify_repair.py`.)

⟨2⟩2. A true `require()` has no side effect, and the original and repaired
checkers have byte-identical stdout/stderr on the shipped green data.  (Named
computation: `verify_repair.py`, saved output `verify_repair.out`.)

⟨2⟩3. QED.

⟨1⟩4. **PROVE** C5 remains observable as DISPLAY.

⟨2⟩1. `check_defect` still computes and returns all four deviations and the
defect size; `main` still prints them on the `D24N-C5 DISPLAY` line.  (Named
computation: `verify_repair.py`.)

⟨2⟩2. QED.

⟨1⟩5. **PROVE** the repaired checker remains red-capable.

⟨2⟩1. The existing `--red-frozen` mutant exits `1` through D24N-C6, while an
in-memory mutant restoring a no-op C5 `require()` is rejected by the source
audit.  (Named computation: `verify_repair.py`, saved output
`verify_repair.out`.)

⟨2⟩2. QED.

⟨1⟩6. QED.
