# Anchored patch instructions

Apply only to `theory/checks/ace_ld_check.py` and `theory/ace-ld.md`.  The
fully edited copies are `ace_ld_check.py` and `ace-ld.md` in this lane.

## Target: `theory/checks/ace_ld_check.py`

1. At the unique docstring anchor beginning `* NO blanket reachability claim
   is made.  The reachability TABLE`, replace its three-line paragraph with:

```text
  * NO blanket reachability claim is made.  The reachability TABLE and
    the measured unreached-gate list (r3 M3, r4 M1) live in the spec,
    section 5 of theory/ace-ld.md; each listed unreached gate names its
    shadowing gate or protocol reason.  In particular, no registered
    mutation reaches LD-C5b's T-stability gate or LD-C6's t_+-sweep gate.
```

2. At the unique configuration anchor
   `C5B_LR2_TS = (20.0, 40.0)`, insert the following after its continuation
   comment and before `C5B_LR2_GRID = 9`:

```python
C5B_LR2_WRAP_CEILING = N_BAR / 8.0
# The hopping dispersion has max group speed 2, while the protocol reaches
# |t| = 2T.  Require 4T < N_BAR/2, equivalently T < N_BAR/8: at the ceiling
# the packet can wrap around the ring and re-enter the measurement window.


def _guard_c5b_spans_no_wrap(spans) -> None:
    """Reject empty, nonpositive, or ring-wrapping Cesaro span sets."""
    if (not spans
            or any(span <= 0.0 or span >= C5B_LR2_WRAP_CEILING
                   for span in spans)):
        raise ValueError(
            "C5B_LR2_TS violates the no-wrap protocol guard: require "
            f"0 < T < N_BAR/8 = {C5B_LR2_WRAP_CEILING:g}; "
            f"got {spans}")


_guard_c5b_spans_no_wrap(C5B_LR2_TS)
```

3. In `check_c5b`'s docstring, replace the exact content anchor
   `value out to T = 200).  Mechanism` with
   `value out to T = 200, below the ring-wrap horizon` followed on the next
   line by `T = N_BAR/8 = 256).  Mechanism` (matching the lane copy).

## Target: `theory/ace-ld.md`

1. In `## 4. HONEST STATUS`, replace the exact phrase
   ``variable `θ` of `notation.md` line 271 (r2 n2)`` with
   ``variable `θ` in notation.md's `μ_∞^α` row (r2 n2)``.

2. In the opening paragraph of `## 5. CHECKER SPEC`, replace the exact
   phrase `the unreached list completed below` with
   `the unreached list expanded below`.

3. In the BARRIER model-battery item, use the exact anchor
   `forward evolution of each branch to `t_+`.` and replace it with:

```text
forward evolution of each branch to `t_+`; an executable no-wrap guard
requires `4T < N/2`, equivalently `T < N/8 = 256`.
```

4. In LD-C5b gate (b), replace the exact anchor
   `` `~3e-5`; the critic finds the same value out to `T = 200`).`` with:

```text
`~3e-5`; the critic finds the same value out to `T = 200`, below the
ring-wrap horizon `T = N/8 = 256`).
```

5. Replace the bold paragraph beginning
   `**Honest unreached rows — COMPLETE enumeration` and ending
   ``those two r3 gaps are closed, not listed):**`` with:

```text
**Honest unreached rows — measured enumeration for the 23 registered
modes (r4, per ace-ld-r3 M3 and ace-ld-r4 M1: each row names the
shadowing gate or protocol reason).**  The r3 list stopped three
evidence-carrying items early; the two the critic fired on a copy are
items 4 and 5 below.  Post-reorder, LD-C6's first moment IS reached
(`--red-c6-moving`) and its support gate is armed
(`--red-c6-weaktransit`) — those two r3 gaps are closed, not listed.
```

6. Immediately after numbered item 10's final anchor
   `These gate green protocol integrity, not evidence.` and before
   `Design notes.`, insert:

```text
11. `LD-C5b`'s `T`-STABILITY gate is reached by no registered mutation:
    `--red-c5b-flat` and `--red-c5b-concentrated` die at the WEDGE, while
    `--red-c5b-nobarrier` passes the WEDGE but dies at the first-span
    Cesàro FLOOR.  Its teeth were re-confirmed on a copy at the shipped
    spans by tightening only `C5B_LR2_STAB` to `1e-6`: both floor checks
    pass at `−3.3592`, then STABILITY fires at measured spread
    `4.882e-05`.  The old `(20, 256)` teeth mutation from ace-ld-r4 M1
    is now rejected by the no-wrap guard at its `T = 256` endpoint.
12. `LD-C6`'s `t_+`-SWEEP gate is reached by no registered mutation:
    `--red-c6-moving`, `--red-c6-weaktransit`, and `--red-c6-static` die
    respectively at FIRST MOMENT, SUPPORT, and LIVENESS.  Moreover, the
    red-battery `C6BarrierAdapter` fixes its protocol time, so a reached
    sweep there would only repeat one cached law.  Its green-side teeth
    were confirmed on a copy with `C6_MOM_BOUND = 1.0`: gate (a) passes
    at `0.453`, then SWEEP fires at `1.0712` for `t_+ = 20`, `W = [3,8]`
    (ace-ld-r4 M1).
```

## Verification

Run from this lane directory:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 -O ace_ld_check.py
PYTHONDONTWRITEBYTECODE=1 python3 -O ace_ld_check.py --red
PYTHONDONTWRITEBYTECODE=1 python3 -O measure_reachability.py
PYTHONDONTWRITEBYTECODE=1 python3 -O measure_reachability.py --red-expected-stability
PYTHONDONTWRITEBYTECODE=1 python3 -O mutation_probes.py
```

Expected exits are respectively `0, 1, 0, 1, 0`.  Captured outputs are in
`logs/green.log`, `logs/full-red.log`, `logs/reachability-green.log`,
`logs/reachability-red.log`, and `logs/mutation-probes.log`.
