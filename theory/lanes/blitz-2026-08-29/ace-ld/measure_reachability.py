#!/usr/bin/env python3
"""Measure LD-C5b/LD-C6 sub-gate reachability on registered mutations.

The probe wraps ``require``: because every call eagerly constructs its failure
message, a tag is recorded whether the condition passes or fails.  The first
failed condition still raises normally, preserving the production exit path.
"""

from __future__ import annotations

import argparse

import ace_ld_check as checker


TARGET_GATES = {
    "C5b-WEDGE",
    "C5b-CESARO-FLOOR",
    "C5b-STABILITY",
    "C6-MOMENT",
    "C6-SUPPORT",
    "C6-LIVENESS",
    "C6-SWEEP",
}

EXPECTED = {
    "c5b-flat": {"C5b-WEDGE"},
    "c5b-concentrated": {"C5b-WEDGE"},
    "c5b-nobarrier": {"C5b-WEDGE", "C5b-CESARO-FLOOR"},
    "c6-static": {"C6-MOMENT", "C6-SUPPORT", "C6-LIVENESS"},
    "c6-moving": {"C6-MOMENT"},
    "c6-weaktransit": {"C6-MOMENT", "C6-SUPPORT"},
}


def tag(message: str) -> str | None:
    if "dephasing wedge absent" in message:
        return "C5b-WEDGE"
    if "D27(LR2) holds at its own quantity" in message:
        return "C5b-CESARO-FLOOR"
    if "double-Cesaro defect not T-stable" in message:
        return "C5b-STABILITY"
    if "sweep gate" in message:
        return "C6-SWEEP"
    if "first moment" in message and message.startswith("LD-C6"):
        return "C6-MOMENT"
    if "TPM support not bounded" in message:
        return "C6-SUPPORT"
    if "dynamics looks Q_W-commuting" in message:
        return "C6-LIVENESS"
    return None


def measure(mode: str) -> tuple[set[str], str]:
    reached: set[str] = set()
    original_require = checker.require

    def traced_require(condition: bool, message: str) -> None:
        gate = tag(message)
        if gate is not None:
            reached.add(gate)
        original_require(condition, message)

    checker.require = traced_require
    try:
        registration = checker.REGISTRY[mode]
        results = checker._run_battery(
            registration["battery"], registration["build"](), lambda _: None
        )
    finally:
        checker.require = original_require

    failures = [tag(message) or message.split(":", 1)[0]
                for ok, message in results.values() if not ok]
    return reached, ", ".join(failures) if failures else "PASS"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--red-expected-stability",
        action="store_true",
        help="mutate the expected table; success means the probe rejects it",
    )
    args = parser.parse_args()

    expected = {mode: set(gates) for mode, gates in EXPECTED.items()}
    if args.red_expected_stability:
        expected["c5b-nobarrier"].add("C5b-STABILITY")

    actual: dict[str, set[str]] = {}
    exits: dict[str, str] = {}
    for mode in EXPECTED:
        actual[mode], exits[mode] = measure(mode)

    print("| registered mode | measured gates reached | dies at |")
    print("|---|---|---|")
    for mode in EXPECTED:
        gates = ", ".join(sorted(actual[mode]))
        print(f"| `{mode}` | {gates} | {exits[mode]} |")

    union = set().union(*actual.values())
    unreached = sorted(TARGET_GATES - union)
    print("Measured unreached target gates: " + ", ".join(unreached))

    mismatches = {
        mode: (expected[mode], actual[mode])
        for mode in EXPECTED
        if actual[mode] != expected[mode]
    }
    if args.red_expected_stability:
        if mismatches:
            print("RED-OK: the expected-table mutation was rejected.")
            return 1
        print("RED FAILURE: the expected-table mutation escaped detection.")
        return 2
    if mismatches:
        for mode, (want, got) in mismatches.items():
            print(f"MISMATCH {mode}: expected {sorted(want)}, got {sorted(got)}")
        return 2
    print("GREEN: measured reachability matches the registered expectation.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
