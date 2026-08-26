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
SCALED_SIZES = (40, 80, 120, 160)
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


def intercept_counterexample_form_factor(soft: float, hard: float) -> complex:
    """Four-site ML5-A counterexample with zero first jet, nonzero intercept."""
    outgoing_bra = np.conjugate(contact_ratio(soft, hard))
    terms = (
        (0, 2, 9.0 / 4.0),
        (0, 3, -3.0 / 2.0),
        (1, 2, -3.0 / 2.0),
        (1, 3, 1.0),
    )
    return sum(
        coefficient
        * (
            outgoing_bra * np.exp(-1j * (soft * x + hard * y))
            + np.exp(-1j * (hard * x + soft * y))
        )
        for x, y, coefficient in terms
    )


def lowering_current_state(n_sites: int, hard: float) -> tuple[list[tuple[int, int]], np.ndarray]:
    """Apply J^-_0 to one momentum state without allocating its full matrix."""
    basis = list(itertools.combinations(range(n_sites), 2))
    index = {pair: row for row, pair in enumerate(basis)}
    hard_state = one_magnon(n_sites, hard)
    result = np.zeros(len(basis), dtype=complex)
    for hard_site, amplitude in enumerate(hard_state):
        for x in range(n_sites):
            y = (x + 1) % n_sites
            if hard_site == x:
                swapped_site = y
            elif hard_site == y:
                swapped_site = x
            else:
                swapped_site = hard_site
            if swapped_site != y:
                result[index[tuple(sorted((swapped_site, y)))]] += (J / 2.0) * amplitude
            if swapped_site != x:
                result[index[tuple(sorted((swapped_site, x)))]] -= (J / 2.0) * amplitude
    return basis, result


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


def audit_intercept_counterexample() -> tuple[float, float]:
    """Guard the repaired ML5-A condition M2(0)=0 AND contact jet=0."""
    min_intercept = float("inf")
    max_first_jet = 0.0
    step = 1.0e-5
    for hard in (0.70, 1.20, 2.00):
        intercept = intercept_counterexample_form_factor(0.0, hard)
        derivative = (
            intercept_counterexample_form_factor(step, hard)
            - intercept_counterexample_form_factor(-step, hard)
        ) / (2.0 * step)
        min_intercept = min(min_intercept, abs(intercept))
        max_first_jet = max(max_first_jet, abs(derivative))
    require(
        min_intercept > 5.0e-2,
        f"ML5-A intercept counterexample vanished: {min_intercept}",
    )
    require(
        max_first_jet < 2.0e-8,
        f"ML5-A intercept counterexample first jet: {max_first_jet}",
    )
    return min_intercept, max_first_jet


def audit_scaled_nonuniformity(red_uniform: bool) -> tuple[float, float, float]:
    """ML4-Q1: k=2pi/N must refute the retracted uniform trace bound."""
    hard = 2.0 * np.pi / 5.0
    traces: list[float] = []
    normalized_ratios: list[float] = []
    for n_sites in SCALED_SIZES:
        soft = 2.0 * np.pi / n_sites
        basis, current_state = lowering_current_state(n_sites, hard)
        phases = one_magnon(n_sites, hard)
        descendant = np.asarray(
            [phases[x] + phases[y] for x, y in basis], dtype=complex
        )
        projection = descendant * (
            np.vdot(descendant, current_state) / np.vdot(descendant, descendant)
        )
        orthogonal = current_state - projection
        outgoing = transported_outgoing_wave(n_sites, basis, soft, hard)
        trace = abs(np.vdot(outgoing, orthogonal))
        amplitude = abs(np.expm1(1j * soft) * np.vdot(outgoing, orthogonal))
        traces.append(trace)
        normalized_ratios.append(amplitude / (np.sqrt(n_sites - 2) * soft**2))

    expected_limit = 2.0 * abs(J * np.sin(hard)) * (1.0 - 4.0 / np.pi**2)
    require(
        abs(traces[-1] - expected_limit) < 1.5e-1,
        f"ML4-Q1 trace limit: got {traces[-1]}, expected {expected_limit}",
    )
    if red_uniform:
        require(
            normalized_ratios[-1] < 1.5 * normalized_ratios[0],
            "red uniform-ML4 mutation was detected by k=2pi/N scaling",
        )
    else:
        require(
            normalized_ratios[-1] > 2.5 * normalized_ratios[0],
            "ML4-Q1 did not detect the nonuniform k=2pi/N growth",
        )
    return traces[-1], normalized_ratios[0], normalized_ratios[-1]


def main() -> None:
    allowed = {"--red-uniform"}
    unknown = set(sys.argv[1:]) - allowed
    require(not unknown, f"unknown arguments: {sorted(unknown)}")
    red_uniform = "--red-uniform" in sys.argv[1:]
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
    intercept = audit_intercept_counterexample()
    print(
        "INTERCEPT min_abs=%.3e first_jet=%.3e" % intercept
    )
    scaled = audit_scaled_nonuniformity(red_uniform)
    print(
        "ML4-Q1 trace_last=%.6f ratio_first=%.6f ratio_last=%.6f" % scaled
    )
    print("PASS: fixed-volume ML4, nonuniform scaling, and ML5 obstructions")


if __name__ == "__main__":
    main()
