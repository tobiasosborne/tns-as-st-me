# Anchored patch for the D24N-C5 no-op gates

Target only `theory/checks/d24d3_normalization_check.py`.  Apply the following
two exact string replacements; do not change any other checker text.

## 1. Correct the module docstring

Unique old anchor/block:

```text
No constant-true ``require`` remains: the r4 guard on the derived exponent
band was structurally unreachable and is deleted (r4-critic m3).
```

Replace with:

```text
No constant-true ``require`` remains: the r4 guard on the derived exponent
band and C5's two DISPLAY guards were deductively subsumed by earlier gates
and are deleted (r4-critic m3; r5-critic m3).
```

## 2. Make `check_defect` genuinely DISPLAY-only

Unique old anchor/block:

```python
def check_defect(slopes: dict[float, list[float]]) -> tuple[float, list[float]]:
    """D24N-C5, DISPLAY: the frozen clause misses off rho=1/2, hits at 1/2."""
    deviations = []
    for spin in SPINS:
        measured = float(np.mean(slopes[spin]))
        deviations.append(abs(predicted_jet(spin, None) - measured) * spin)
    require(deviations[0] < DECISION_BAND,
            f"D24N-C5 frozen clause must match at S=1/2, deviation {deviations[0]:.4f}")
    for spin, deviation in zip(SPINS[1:], deviations[1:]):
        require(deviation > DECISION_BAND,
                f"D24N-C5 frozen clause unexpectedly matched at S={spin}")
    return max(deviations[1:]), deviations
```

Replace with:

```python
def check_defect(slopes: dict[float, list[float]]) -> tuple[float, list[float]]:
    """D24N-C5, DISPLAY: the frozen clause misses off rho=1/2, hits at 1/2.

    This function intentionally contains no gate: C4 already forces the
    displayed S=1/2 deviation below DECISION_BAND and every displayed
    off-S=1/2 deviation above it (r5-critic m3).
    """
    deviations = []
    for spin in SPINS:
        measured = float(np.mean(slopes[spin]))
        deviations.append(abs(predicted_jet(spin, None) - measured) * spin)
    return max(deviations[1:]), deviations
```

Mechanical evidence: `verify_repair.py` / `verify_repair.out`.  The complete
lane-copy diff is saved as `checker.diff`.
