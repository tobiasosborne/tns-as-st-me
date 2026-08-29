#!/usr/bin/env python3
"""Exercise the wrap guard and the two otherwise-shadowed gates."""

from __future__ import annotations

import ace_ld_check as checker


def require_probe(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def main() -> int:
    checker._guard_c5b_spans_no_wrap(checker.C5B_LR2_TS)
    print(
        "GREEN wrap guard: shipped spans "
        f"{checker.C5B_LR2_TS} satisfy T < N_BAR/8 = "
        f"{checker.C5B_LR2_WRAP_CEILING:g}."
    )
    try:
        checker._guard_c5b_spans_no_wrap((20.0, 256.0))
    except ValueError as exc:
        print(f"RED-OK wrap guard: {exc}")
    else:
        raise RuntimeError("wrap mutation T=256 escaped the configuration guard")

    old_stability = checker.C5B_LR2_STAB
    checker.C5B_LR2_STAB = 1e-6
    try:
        checker.check_c5b(checker.BarrierModel(in_window=True), lambda _: None)
    except checker.CheckFailure as exc:
        require_probe(
            "double-Cesaro defect not T-stable" in str(exc),
            f"wrong C5b mutation exit path: {exc}",
        )
        print(f"RED-OK C5b-STABILITY: {exc}")
    else:
        raise RuntimeError("C5b stability-threshold mutation escaped detection")
    finally:
        checker.C5B_LR2_STAB = old_stability

    old_bound = checker.C6_MOM_BOUND
    checker.C6_MOM_BOUND = 1.0
    try:
        checker.check_c6(checker.D16Model(), lambda _: None)
    except checker.CheckFailure as exc:
        require_probe(
            "sweep gate" in str(exc) and "t_+=20" in str(exc),
            f"wrong C6 mutation exit path: {exc}",
        )
        print(f"RED-OK C6-SWEEP: {exc}")
    else:
        raise RuntimeError("C6 moment-bound mutation escaped the sweep gate")
    finally:
        checker.C6_MOM_BOUND = old_bound

    print("GREEN: all three deliberate mutations were rejected at their target.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
