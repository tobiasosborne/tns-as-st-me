#!/usr/bin/env python3
"""Red-capable certificate for AC-EX-2M's MPS-2M-cluster computation.

A2M-C1a checks the connected AKLT two-point function by a raw contraction and
by the fixed-point-subtracted transfer formula.  A2M-C1b checks block-support
independence for product observables of lengths one through three.  The three
registered mutations must be run separately and must exit with status one.

No Python ``assert`` is used, so every gate remains live under ``python3 -O``.
"""

from __future__ import annotations

import argparse
import sys
from dataclasses import dataclass

import numpy as np


VALUE_TOL = 1.0e-12
RATIO_TOL = 1.0e-8
BLOCK_TOL = 1.0e-12
BLOCK_CAP = 0.1
LAMBDA_TILDE = 0.5


def fail(message: str, code: int = 2) -> "None":
    print(f"FAIL: {message}", file=sys.stderr)
    raise SystemExit(code)


def pauli_matrices() -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    sx = np.array([[0.0, 1.0], [1.0, 0.0]], dtype=complex)
    sy = np.array([[0.0, -1.0j], [1.0j, 0.0]], dtype=complex)
    sz = np.array([[1.0, 0.0], [0.0, -1.0]], dtype=complex)
    return sx, sy, sz


def cartesian_spin_z() -> np.ndarray:
    """Return (S^z)_{bc}=-i epsilon_{zbc} in the (x,y,z) basis."""

    return np.array(
        [[0.0, -1.0j, 0.0], [1.0j, 0.0, 0.0], [0.0, 0.0, 0.0]],
        dtype=complex,
    )


AKLT = tuple(matrix / np.sqrt(3.0) for matrix in pauli_matrices())
IDENTITY_VIRTUAL = np.eye(2, dtype=complex)
RIGHT_FIXED = IDENTITY_VIRTUAL / 2.0
PHYSICAL_C = np.eye(3, dtype=complex) + cartesian_spin_z()


def transfer(y: np.ndarray) -> np.ndarray:
    return sum(a @ y @ a.conj().T for a in AKLT)


def observable_transfer(observable: np.ndarray, y: np.ndarray) -> np.ndarray:
    out = np.zeros((2, 2), dtype=complex)
    for s, a_s in enumerate(AKLT):
        for sp, a_sp in enumerate(AKLT):
            out += observable[sp, s] * (a_s @ y @ a_sp.conj().T)
    return out


def iterate(function, y: np.ndarray, count: int) -> np.ndarray:
    out = y
    for _ in range(count):
        out = function(out)
    return out


def fixed_projection(y: np.ndarray) -> np.ndarray:
    return np.trace(y) * RIGHT_FIXED


def vacuum_expectation(y: np.ndarray) -> complex:
    return np.trace(y)


def block_transfer(y: np.ndarray, width: int) -> np.ndarray:
    return iterate(lambda value: observable_transfer(PHYSICAL_C, value), y, width)


def block_operator_norm(width: int) -> float:
    operator = np.array([[1.0 + 0.0j]])
    for _ in range(width):
        operator = np.kron(operator, PHYSICAL_C)
    return float(np.linalg.svd(operator, compute_uv=False)[0])


@dataclass(frozen=True)
class C1aResult:
    direct_errors: tuple[float, ...]
    route_errors: tuple[float, ...]
    ratio_errors: tuple[float, ...]


def check_c1a(red_c1a: bool) -> C1aResult:
    direct_values: list[complex] = []
    route_values: list[complex] = []
    direct_errors: list[float] = []
    route_errors: list[float] = []

    one_point = vacuum_expectation(observable_transfer(PHYSICAL_C, RIGHT_FIXED))
    for distance in range(1, 13):
        right = observable_transfer(PHYSICAL_C, RIGHT_FIXED)
        propagated = iterate(transfer, right, distance - 1)
        raw = vacuum_expectation(observable_transfer(PHYSICAL_C, propagated))
        direct_connected = raw - one_point * one_point

        if red_c1a:
            middle = propagated
        else:
            middle = propagated - fixed_projection(right)
        route_connected = vacuum_expectation(observable_transfer(PHYSICAL_C, middle))

        expected = (4.0 / 3.0) * ((-1.0 / 3.0) ** distance)
        direct_values.append(direct_connected)
        route_values.append(route_connected)
        direct_errors.append(float(abs(direct_connected - expected)))
        route_errors.append(float(abs(route_connected - expected)))

    ratio_errors = [
        float(abs((route_values[index] / route_values[index - 1]) + 1.0 / 3.0))
        for index in range(1, len(route_values))
    ]
    return C1aResult(tuple(direct_errors), tuple(route_errors), tuple(ratio_errors))


@dataclass(frozen=True)
class C1bResult:
    agreement_error: float
    max_ratio: float
    max_ratio_location: tuple[int, int, int]
    support_profile_error: float
    support_profile_location: tuple[int, int, int]
    monotonicity_excess: float
    monotonicity_location: tuple[int, int, int]


def check_c1b(red_c1b: bool, red_supportfold: bool) -> C1bResult:
    agreement_error = 0.0
    ratios: dict[tuple[int, int, int], float] = {}
    direct_ratios: dict[tuple[int, int, int], float] = {}

    for width_c in (1, 2, 3):
        one_c = vacuum_expectation(block_transfer(RIGHT_FIXED, width_c))
        norm_c = block_operator_norm(width_c)
        for width_d in (1, 2, 3):
            right = block_transfer(RIGHT_FIXED, width_d)
            one_d = vacuum_expectation(right)
            norm_d = block_operator_norm(width_d)
            for separation in (2, 4, 6):
                propagated = iterate(transfer, right, separation)
                raw = vacuum_expectation(block_transfer(propagated, width_c))
                direct_connected = raw - one_c * one_d
                subtracted = propagated - fixed_projection(right)
                fixed_connected = vacuum_expectation(block_transfer(subtracted, width_c))
                agreement_error = max(
                    agreement_error, float(abs(direct_connected - fixed_connected))
                )

                exponent = separation
                if red_c1b:
                    exponent += 2 * (width_c + width_d)
                ratio = float(
                    abs(fixed_connected)
                    / (norm_c * norm_d * (LAMBDA_TILDE**exponent))
                )
                direct_ratio = float(
                    abs(direct_connected)
                    / (norm_c * norm_d * (LAMBDA_TILDE**exponent))
                )
                if red_supportfold:
                    ratio *= width_c * width_d
                ratios[(width_c, width_d, separation)] = ratio
                direct_ratios[(width_c, width_d, separation)] = direct_ratio

    max_location, max_ratio = max(ratios.items(), key=lambda item: item[1])
    support_location, support_profile_error = max(
        (
            (location, abs(ratio - direct_ratios[location]))
            for location, ratio in ratios.items()
        ),
        key=lambda item: item[1],
    )

    monotonicity_excess = -np.inf
    monotonicity_location = (1, 1, 2)
    for separation in (2, 4, 6):
        baseline = ratios[(1, 1, separation)]
        for width_c in (1, 2, 3):
            for width_d in (1, 2, 3):
                varied = ratios[(width_c, width_d, separation)]
                excess = varied - baseline
                if excess > monotonicity_excess:
                    monotonicity_excess = excess
                    monotonicity_location = (width_c, width_d, separation)

    return C1bResult(
        agreement_error,
        max_ratio,
        max_location,
        float(support_profile_error),
        support_location,
        float(monotonicity_excess),
        monotonicity_location,
    )


def violations(c1a: C1aResult, c1b: C1bResult) -> list[str]:
    found: list[str] = []
    direct_error = max(c1a.direct_errors)
    route_error = max(c1a.route_errors)
    ratio_error = max(c1a.ratio_errors)
    if direct_error > VALUE_TOL:
        found.append(f"C1a direct value error {direct_error:.6e} > {VALUE_TOL:.1e}")
    if route_error > VALUE_TOL:
        found.append(f"C1a route value error {route_error:.6e} > {VALUE_TOL:.1e}")
    if ratio_error > RATIO_TOL:
        found.append(f"C1a ratio error {ratio_error:.6e} > {RATIO_TOL:.1e}")
    if c1b.agreement_error > BLOCK_TOL:
        found.append(
            f"C1b contraction disagreement {c1b.agreement_error:.6e} > {BLOCK_TOL:.1e}"
        )
    if c1b.max_ratio > BLOCK_CAP:
        found.append(
            "C1b cap "
            f"{c1b.max_ratio:.6f} at {c1b.max_ratio_location} > {BLOCK_CAP:.1f}"
        )
    if c1b.support_profile_error > BLOCK_TOL:
        found.append(
            "C1b support-profile disagreement "
            f"{c1b.support_profile_error:.6e} at {c1b.support_profile_location}"
        )
    if c1b.monotonicity_excess > BLOCK_TOL:
        found.append(
            "C1b support monotonicity excess "
            f"{c1b.monotonicity_excess:.6e} at {c1b.monotonicity_location}"
        )
    return found


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    mutations = parser.add_mutually_exclusive_group()
    mutations.add_argument("--red-c1a", action="store_true")
    mutations.add_argument("--red-c1b", action="store_true")
    mutations.add_argument("--red-supportfold", action="store_true")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    c1a = check_c1a(args.red_c1a)
    c1b = check_c1b(args.red_c1b, args.red_supportfold)
    found = violations(c1a, c1b)

    print(
        "A2M-C1a "
        f"direct={max(c1a.direct_errors):.3e} "
        f"route={max(c1a.route_errors):.3e} "
        f"ratio={max(c1a.ratio_errors):.3e}"
    )
    print(
        "A2M-C1b "
        f"agreement={c1b.agreement_error:.3e} "
        f"max_ratio={c1b.max_ratio:.6f}@{c1b.max_ratio_location} "
        f"profile={c1b.support_profile_error:.3e}@{c1b.support_profile_location} "
        f"monotonicity_excess={c1b.monotonicity_excess:.3e}"
        f"@{c1b.monotonicity_location}"
    )

    red_mode = args.red_c1a or args.red_c1b or args.red_supportfold
    if red_mode:
        if not found:
            fail("registered mutation unexpectedly passed all gates")
        print("RED-OK: " + " | ".join(found))
        raise SystemExit(1)
    if found:
        fail(" | ".join(found))
    print("PASS: A2M-C1a/C1b")


if __name__ == "__main__":
    main()
