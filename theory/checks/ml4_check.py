#!/usr/bin/env python3
"""Red-capable finite-ring checks for ML4 and the ML5 source obstruction.

The current and charge blocks are assembled directly from ``(J/2)(1-P)``.
The outgoing two-body wave is obtained by solving its one contact equation;
no closed Bethe S-matrix is inserted.  Every failure is an explicit
``SystemExit``, so optimized mode cannot disable a test.
"""

from __future__ import annotations

import itertools
import sys

import numpy as np


J = 1.37
SIZES = (12, 14, 16, 18, 20)
SOFT_STEPS = 2.0e-5 * 2.0 ** np.arange(5)
ALGEBRA_TOL = 8.0e-11
EXPONENT_TOL = 1.5e-2
COEFFICIENT_TOL = 3.0e-4


def fail(message: str) -> None:
    print(f"FAIL: {message}", file=sys.stderr)
    raise SystemExit(1)


def require(condition: bool, message: str) -> None:
    if not condition:
        fail(message)


def one_magnon(n_sites: int, momentum: float) -> np.ndarray:
    return np.exp(1j * momentum * np.arange(n_sites)) / np.sqrt(n_sites)


def lowering_zero_block(
    n_sites: int,
    basis: list[tuple[int, int]],
    index: dict[tuple[int, int], int],
) -> np.ndarray:
    """Matrix of Q_0 from the one- to the two-magnon sector."""
    block = np.zeros((len(basis), n_sites), dtype=complex)
    for hard_site in range(n_sites):
        for added_site in range(n_sites):
            if added_site == hard_site:
                continue
            pair = tuple(sorted((hard_site, added_site)))
            block[index[pair], hard_site] += 1.0
    return block


def lowering_current_zero_block(
    n_sites: int,
    basis: list[tuple[int, int]],
    index: dict[tuple[int, int], int],
) -> np.ndarray:
    """Matrix of sum_x (J/2)(S^-_{x+1}-S^-_x)P_{x,x+1}."""
    block = np.zeros((len(basis), n_sites), dtype=complex)
    for hard_site in range(n_sites):
        for x in range(n_sites):
            y = (x + 1) % n_sites
            if hard_site == x:
                swapped_site = y
            elif hard_site == y:
                swapped_site = x
            else:
                swapped_site = hard_site
            coefficient = J / 2.0
            if swapped_site != y:
                block[index[tuple(sorted((swapped_site, y)))], hard_site] += (
                    coefficient
                )
            if swapped_site != x:
                block[index[tuple(sorted((swapped_site, x)))], hard_site] -= (
                    coefficient
                )
    return block


def z_current_zero_block(n_sites: int) -> np.ndarray:
    """One-magnon block of sum_x (J/2)(S^z_{x+1}-S^z_x)P."""
    block = np.zeros((n_sites, n_sites), dtype=complex)
    for x in range(n_sites):
        y = (x + 1) % n_sites
        block[y, x] -= J / 2.0
        block[x, y] += J / 2.0
    return block


def contact_ratio(soft: float, hard: float) -> complex:
    """Solve the local contact equation with incoming coefficient one."""
    z_soft = np.exp(1j * soft)
    z_hard = np.exp(1j * hard)
    outgoing_coefficient = 2.0 * z_hard - z_soft * z_hard - 1.0
    incoming_coefficient = 2.0 * z_soft - z_soft * z_hard - 1.0
    matrix = np.asarray([[outgoing_coefficient]], dtype=complex)
    rhs = np.asarray([-incoming_coefficient], dtype=complex)
    return complex(np.linalg.solve(matrix, rhs)[0])


def transported_outgoing_wave(
    n_sites: int,
    basis: list[tuple[int, int]],
    soft: float,
    hard: float,
) -> np.ndarray:
    """Incoming-normalized on-shell wave, parallel-transported to K=hard.

    Removing the changing centre phase identifies nearby total-momentum
    fibers.  At soft=0 this vector is exactly Q_0|hard>.
    """
    relative = (hard - soft) / 2.0
    outgoing = contact_ratio(soft, hard)
    return np.asarray(
        [
            np.exp(1j * hard * (x + y) / 2.0)
            * (
                outgoing * np.exp(1j * relative * (y - x))
                + np.exp(-1j * relative * (y - x))
            )
            / np.sqrt(n_sites)
            for x, y in basis
        ]
    )


def log_slope(arguments: np.ndarray, values: np.ndarray) -> float:
    require(np.all(values > 0.0), "zero encountered in exponent fit")
    return float(np.polyfit(np.log(arguments), np.log(values), 1)[0])


def source_counterexample_form_factor(soft: float, hard: float) -> complex:
    """<out|D|Omega> for the four-bond local ML5 counterexample."""
    outgoing_bra = np.conjugate(contact_ratio(soft, hard))
    terms = ((0, 1, 1.0), (1, 2, -1.0), (2, 3, 1.0), (0, 3, -1.0))
    return sum(
        coefficient
        * (
            outgoing_bra * np.exp(-1j * (soft * x + hard * y))
            + np.exp(-1j * (hard * x + soft * y))
        )
        for x, y, coefficient in terms
    )


def audit_size(n_sites: int) -> tuple[float, float, float, float, float]:
    basis = list(itertools.combinations(range(n_sites), 2))
    index = {pair: row for row, pair in enumerate(basis)}
    charge = lowering_zero_block(n_sites, basis, index)
    current = lowering_current_zero_block(n_sites, basis, index)
    z_current = z_current_zero_block(n_sites)

    max_ward = 0.0
    max_projection = 0.0
    raw_exponents: list[float] = []
    amplitude_exponents: list[float] = []
    mutant_exponents: list[float] = []

    # Labels 2 and 3 stay away from both soft and zone-edge singularities.
    for label in (2, 3):
        hard = 2.0 * np.pi * label / n_sites
        hard_state = one_magnon(n_sites, hard)
        descendant = charge @ hard_state
        current_state = current @ hard_state
        velocity = J * np.sin(hard)

        ward = abs(np.vdot(descendant, current_state) - 2j * velocity)
        ward = max(
            ward,
            abs(np.vdot(hard_state, z_current @ hard_state) - 1j * velocity),
        )
        max_ward = max(max_ward, ward)

        expected_projection = 2j * velocity * descendant / (n_sites - 2)
        projection = descendant * (
            np.vdot(descendant, current_state) / np.vdot(descendant, descendant)
        )
        orthogonal = current_state - projection
        projection_error = max(
            np.linalg.norm(projection - expected_projection),
            abs(np.vdot(descendant, orthogonal)),
            np.linalg.norm(
                transported_outgoing_wave(n_sites, basis, 0.0, hard)
                - descendant
            ),
        )
        max_projection = max(max_projection, projection_error)

        raw_values = []
        amplitude_values = []
        mutant_values = []
        for soft in SOFT_STEPS:
            outgoing = transported_outgoing_wave(
                n_sites, basis, soft, hard
            )
            orthogonal_trace = np.vdot(outgoing, orthogonal)
            raw_values.append(abs(orthogonal_trace))
            difference = np.expm1(1j * soft)
            amplitude_values.append(abs(difference * orthogonal_trace))

            # Deliberately omit the descendant projection.  A meaningful
            # checker must see the exponent fall from two to one.
            mutant_values.append(abs(difference * np.vdot(outgoing, current_state)))

        raw_exponents.append(
            log_slope(SOFT_STEPS, np.asarray(raw_values))
        )
        amplitude_exponents.append(
            log_slope(SOFT_STEPS, np.asarray(amplitude_values))
        )
        mutant_exponents.append(
            log_slope(SOFT_STEPS, np.asarray(mutant_values))
        )

    require(max_ward < ALGEBRA_TOL, f"N={n_sites} Ward residue: {max_ward}")
    require(
        max_projection < ALGEBRA_TOL,
        f"N={n_sites} descendant projection: {max_projection}",
    )
    for exponent in raw_exponents:
        require(
            abs(exponent - 1.0) < EXPONENT_TOL,
            f"N={n_sites} orthogonal trace exponent: {exponent}",
        )
    for exponent in amplitude_exponents:
        require(
            abs(exponent - 2.0) < EXPONENT_TOL,
            f"N={n_sites} ML4 amplitude exponent: {exponent}",
        )
    for exponent in mutant_exponents:
        require(
            abs(exponent - 1.0) < EXPONENT_TOL,
            f"N={n_sites} red mutant was not detected: {exponent}",
        )

    return (
        max_ward,
        max_projection,
        min(raw_exponents),
        min(amplitude_exponents),
        max(mutant_exponents),
    )


def audit_counterexample() -> tuple[float, float]:
    max_zero = 0.0
    max_coefficient_error = 0.0
    for hard in (0.70, 1.20, 2.00):
        max_zero = max(
            max_zero, abs(source_counterexample_form_factor(0.0, hard))
        )
        numerical = source_counterexample_form_factor(1.0e-6, hard) / 1.0e-6
        exact = 2j * (1.0 - np.exp(-3j * hard))
        max_coefficient_error = max(
            max_coefficient_error, abs(numerical - exact)
        )
    require(max_zero < ALGEBRA_TOL, f"counterexample soft zero: {max_zero}")
    require(
        max_coefficient_error < COEFFICIENT_TOL,
        f"counterexample linear coefficient: {max_coefficient_error}",
    )
    return max_zero, max_coefficient_error


def main() -> None:
    for n_sites in SIZES:
        result = audit_size(n_sites)
        print(
            "N=%2d ward=%.3e projection=%.3e "
            "trace_p=%.5f amplitude_p=%.5f red_p=%.5f" % (
                n_sites,
                *result,
            )
        )
    counterexample = audit_counterexample()
    print(
        "SOURCE soft_zero=%.3e coefficient_error=%.3e" % counterexample
    )
    print("PASS: ML4 orthogonal suppression and ML5 source obstruction")


if __name__ == "__main__":
    main()
