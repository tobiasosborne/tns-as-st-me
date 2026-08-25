#!/usr/bin/env python3
"""Finite-ring checks for theory/soft-current-recon.md.

The operator blocks are assembled directly from (J/2)(1-P), the lowering
charge, and its bond current.  No check relies on ``assert``, so ``python -O``
cannot disable a failure.
"""

from __future__ import annotations

import itertools
import sys

import numpy as np


N = 18
J = 1.37
TOL = 4.0e-11
SOFT_TOL = 2.0e-8


def fail(message: str) -> None:
    print(f"FAIL: {message}", file=sys.stderr)
    raise SystemExit(1)


def require(condition: bool, message: str) -> None:
    if not condition:
        fail(message)


ONE_BASIS = [(x,) for x in range(N)]
TWO_BASIS = list(itertools.combinations(range(N), 2))
ONE_INDEX = {state: column for column, state in enumerate(ONE_BASIS)}
TWO_INDEX = {state: column for column, state in enumerate(TWO_BASIS)}


def ring_hamiltonian(
    basis: list[tuple[int, ...]], index: dict[tuple[int, ...], int]
) -> np.ndarray:
    """Assemble a fixed-magnon-sector ring Hamiltonian bond by bond."""
    matrix = np.zeros((len(basis), len(basis)), dtype=complex)
    for column, state in enumerate(basis):
        occupied = set(state)
        for x in range(N):
            y = (x + 1) % N
            if (x in occupied) == (y in occupied):
                continue
            swapped = (occupied - {x, y}) | ({y} if x in occupied else {x})
            matrix[column, column] += J / 2.0
            matrix[index[tuple(sorted(swapped))], column] -= J / 2.0
    return matrix


H1 = ring_hamiltonian(ONE_BASIS, ONE_INDEX)
H2 = ring_hamiltonian(TWO_BASIS, TWO_INDEX)


def one_magnon(momentum: float) -> np.ndarray:
    return np.exp(1j * momentum * np.arange(N)) / np.sqrt(N)


def lowering_block(momentum: float) -> np.ndarray:
    """Matrix of Q_k from the one- to the two-magnon sector."""
    block = np.zeros((len(TWO_BASIS), N), dtype=complex)
    for hard_site in range(N):
        for added_site in range(N):
            if added_site == hard_site:
                continue
            pair = tuple(sorted((added_site, hard_site)))
            block[TWO_INDEX[pair], hard_site] += np.exp(
                1j * momentum * added_site
            )
    return block


def lowering_current_block(momentum: float) -> np.ndarray:
    """Matrix of sum_x e^(ikx) (J/2)(S^-_{x+1}-S^-_x)P_x."""
    block = np.zeros((len(TWO_BASIS), N), dtype=complex)
    for hard_site in range(N):
        for x in range(N):
            y = (x + 1) % N
            occupied = {hard_site}
            if x in occupied:
                swapped = (occupied - {x}) | {y}
            elif y in occupied:
                swapped = (occupied - {y}) | {x}
            else:
                swapped = occupied.copy()
            coefficient = (J / 2.0) * np.exp(1j * momentum * x)
            if y not in swapped:
                block[TWO_INDEX[tuple(sorted(swapped | {y}))], hard_site] += (
                    coefficient
                )
            if x not in swapped:
                block[TWO_INDEX[tuple(sorted(swapped | {x}))], hard_site] -= (
                    coefficient
                )
    return block


def z_current_zero_block() -> np.ndarray:
    """One-magnon block of sum_x (J/2)(S^z_{x+1}-S^z_x)P_x."""
    block = np.zeros((N, N), dtype=complex)
    for x in range(N):
        y = (x + 1) % N
        block[ONE_INDEX[(y,)], ONE_INDEX[(x,)]] -= J / 2.0
        block[ONE_INDEX[(x,)], ONE_INDEX[(y,)]] += J / 2.0
    return block


def contact_vector(total_momentum: float) -> np.ndarray:
    vector = np.zeros(len(TWO_BASIS), dtype=complex)
    for x in range(N):
        pair = tuple(sorted((x, (x + 1) % N)))
        vector[TWO_INDEX[pair]] += np.exp(1j * total_momentum * x)
    return vector


def ordered_plane(k1: complex, k2: complex) -> np.ndarray:
    return np.asarray(
        [np.exp(1j * (k1 * x + k2 * y)) for x, y in TWO_BASIS]
    )


def triangular_sum_direct(a: complex, b: complex) -> complex:
    return sum(
        np.exp(1j * (a * x + b * y)) for x, y in TWO_BASIS
    )


def geometric_one_to_n_minus_one(angle: complex) -> complex:
    ratio = np.exp(1j * angle)
    if abs(ratio - 1.0) < 2.0e-12:
        return complex(N - 1)
    return ratio * (1.0 - ratio ** (N - 1)) / (1.0 - ratio)


def triangular_sum(a: complex, b: complex) -> complex:
    """Closed form for F_N(a,b)=sum_{0<=x<y<N} exp(i(ax+by))."""
    denominator = 1.0 - np.exp(1j * a)
    if abs(denominator) < 2.0e-12:
        return triangular_sum_direct(a, b)
    return (
        geometric_one_to_n_minus_one(b)
        - geometric_one_to_n_minus_one(a + b)
    ) / denominator


def bethe_vector(
    k1: complex, k2: complex, a12: complex, a21: complex
) -> np.ndarray:
    return a12 * ordered_plane(k1, k2) + a21 * ordered_plane(k2, k1)


def bethe_overlap_formula(
    soft: float, hard: float, k1: complex, k2: complex,
    a12: complex, a21: complex
) -> complex:
    """Exact coefficient <B|Q_soft|hard> for a normalized Bethe wave B."""
    vector = bethe_vector(k1, k2, a12, a21)
    norm = np.linalg.norm(vector)
    numerator = (
        np.conjugate(a12) * triangular_sum(soft - np.conjugate(k1), hard - np.conjugate(k2))
        + np.conjugate(a12) * triangular_sum(hard - np.conjugate(k1), soft - np.conjugate(k2))
        + np.conjugate(a21) * triangular_sum(soft - np.conjugate(k2), hard - np.conjugate(k1))
        + np.conjugate(a21) * triangular_sum(hard - np.conjugate(k2), soft - np.conjugate(k1))
    )
    return numerator / (np.sqrt(N) * norm)


def oracle_scattering(soft: float, hard: float) -> complex:
    zs, zh = np.exp(1j * soft), np.exp(1j * hard)
    return -(zs * zh - 2.0 * zs + 1.0) / (zs * zh - 2.0 * zh + 1.0)


def contact_scattering(soft: float, hard: float) -> complex:
    """Solve only the local contact equation, with A21=1."""
    zs, zh = np.exp(1j * soft), np.exp(1j * hard)
    c12 = 2.0 * zh - zs * zh - 1.0
    c21 = 2.0 * zs - zs * zh - 1.0
    return -c21 / c12


def check_charge_and_overlap() -> tuple[float, float, float, float]:
    soft = 2.0 * np.pi / N
    hard = 8.0 * np.pi / N
    vacuum_created = np.exp(1j * soft * np.arange(N))
    vacuum_error = np.linalg.norm(vacuum_created - np.sqrt(N) * one_magnon(soft))
    q_soft = lowering_block(soft)
    hard_state = one_magnon(hard)
    source = q_soft @ hard_state
    coordinate = (
        ordered_plane(soft, hard) + ordered_plane(hard, soft)
    ) / np.sqrt(N)
    coordinate_error = max(np.linalg.norm(source - coordinate), vacuum_error)
    norm_error = abs(np.vdot(source, source) - (N - 2))

    overlap_error = 0.0
    waves = [
        (0.41, 1.23, np.exp(0.37j), 0.71 - 0.29j),
        (0.73 - 0.18j, 0.73 + 0.18j, 0.42 + 0.11j, 1.0 + 0.0j),
    ]
    for k1, k2, a12, a21 in waves:
        bethe = bethe_vector(k1, k2, a12, a21)
        direct_overlap = np.vdot(bethe / np.linalg.norm(bethe), source)
        overlap_error = max(
            overlap_error,
            abs(
                direct_overlap
                - bethe_overlap_formula(soft, hard, k1, k2, a12, a21)
            ),
        )

    k1, k2 = 0.405359200715, 1.339970051280
    a12, a21 = oracle_scattering(k1, k2), 1.0 + 0.0j
    bethe = bethe_vector(k1, k2, a12, a21)
    direct_contact = np.vdot(
        bethe / np.linalg.norm(bethe), contact_vector(k1 + k2)
    )
    contact_formula = N * (
        np.conjugate(a12) * np.exp(-1j * np.conjugate(k2))
        + np.conjugate(a21) * np.exp(-1j * np.conjugate(k1))
    ) / np.linalg.norm(bethe)
    overlap_error = max(overlap_error, abs(direct_contact - contact_formula))

    smat = oracle_scattering(soft, hard)
    incoming_bethe = (
        smat * ordered_plane(soft, hard) + ordered_plane(hard, soft)
    ) / np.sqrt(N)
    mismatch = (1.0 - smat) * ordered_plane(soft, hard) / np.sqrt(N)
    mismatch_error = np.linalg.norm(source - incoming_bethe - mismatch)

    require(coordinate_error < TOL, f"Q_k coordinate state: {coordinate_error}")
    require(norm_error < TOL, f"Q_k state norm: {norm_error}")
    require(overlap_error < TOL, f"closed Bethe overlap: {overlap_error}")
    require(mismatch_error < TOL, f"Bethe/source mismatch: {mismatch_error}")
    return coordinate_error, norm_error, overlap_error, mismatch_error


def check_current_blocks() -> tuple[float, float, float]:
    max_commutator = 0.0
    max_action = 0.0
    max_form_factor = 0.0
    eigenvalues, eigenvectors = np.linalg.eigh(H2)
    for soft_number, hard_number in [(1, 4), (-2, 5), (0, 3)]:
        soft = 2.0 * np.pi * soft_number / N
        hard = 2.0 * np.pi * hard_number / N
        zs, zh = np.exp(1j * soft), np.exp(1j * hard)
        q_soft = lowering_block(soft)
        current = lowering_current_block(soft)
        commutator = H2 @ q_soft - q_soft @ H1 - (zs - 1.0) * current
        max_commutator = max(max_commutator, np.linalg.norm(commutator))

        hard_state = one_magnon(hard)
        source = q_soft @ hard_state
        coefficient = (
            0.0
            if soft_number == 0
            else J * (1.0 - np.cos(soft)) / (zs - 1.0)
        )
        predicted = coefficient * source + (
            J * (zh - 1.0) / np.sqrt(N)
        ) * contact_vector(soft + hard)
        max_action = max(max_action, np.linalg.norm(current @ hard_state - predicted))

        overlaps_q = eigenvectors.conj().T @ source
        overlaps_j = eigenvectors.conj().T @ (current @ hard_state)
        energy_hard = J * (1.0 - np.cos(hard))
        form_residual = (eigenvalues - energy_hard) * overlaps_q - (
            zs - 1.0
        ) * overlaps_j
        max_form_factor = max(max_form_factor, np.linalg.norm(form_residual))

    require(max_commutator < TOL, f"current commutator block: {max_commutator}")
    require(max_action < TOL, f"exact current action: {max_action}")
    require(max_form_factor < TOL, f"all ED current form factors: {max_form_factor}")
    return max_commutator, max_action, max_form_factor


def check_zero_current_ward() -> tuple[float, float, float, float]:
    hard = 6.0 * np.pi / N
    hard_state = one_magnon(hard)
    q_zero = lowering_block(0.0)
    current_zero = lowering_current_block(0.0)
    descendant = q_zero @ hard_state
    current_state = current_zero @ hard_state
    velocity = J * np.sin(hard)
    descendant_energy_error = np.linalg.norm(
        H2 @ descendant - J * (1.0 - np.cos(hard)) * descendant
    )

    norm_error = abs(np.vdot(descendant, descendant) - (N - 2))
    ward_error = max(
        abs(np.vdot(descendant, current_state) - 2j * velocity),
        descendant_energy_error,
    )
    z_current = z_current_zero_block()
    diagonal_error = abs(np.vdot(hard_state, z_current @ hard_state) - 1j * velocity)
    su2_error = abs(
        np.vdot(hard_state, q_zero.conj().T @ current_state) - 2j * velocity
    )

    projection = (2j * velocity / (N - 2)) * descendant
    orthogonal = current_state - projection
    orthogonality_error = abs(np.vdot(descendant, orthogonal))
    require(np.linalg.norm(orthogonal) > 0.25, "J_0 falsely reduced to descendant only")
    require(norm_error < TOL, f"descendant norm: {norm_error}")
    require(ward_error < TOL, f"lowering Ward residue: {ward_error}")
    require(diagonal_error < TOL, f"diagonal current/velocity: {diagonal_error}")
    require(su2_error < TOL, f"SU(2) current Ward identity: {su2_error}")
    require(orthogonality_error < TOL, f"projected-current orthogonality: {orthogonality_error}")
    return norm_error, ward_error, diagonal_error, orthogonality_error


def check_contact_soft_expansion() -> tuple[float, float, float, float]:
    oracle_error = 0.0
    first_error = 0.0
    second_error = 0.0
    series_error = 0.0
    momenta = np.arange(-8, 9) * 2.0e-4
    for hard in [0.37, 1.10, 2.40, 3.00]:
        for soft in [-0.13, -0.01, 0.02, 0.16]:
            oracle_error = max(
                oracle_error,
                abs(contact_scattering(soft, hard) - oracle_scattering(soft, hard)),
            )
        phases = np.unwrap(
            np.angle([contact_scattering(soft, hard) for soft in momenta])
        )
        coefficients = np.polynomial.polynomial.polyfit(momenta, phases, 6)
        first_error = max(first_error, abs(coefficients[1] - 2.0))
        second_error = max(
            second_error, abs(coefficients[2] - 1.0 / np.tan(hard / 2.0))
        )
        for soft in [-0.004, -0.002, 0.002, 0.004]:
            expected = 1.0 + 2j * soft + (
                1j / np.tan(hard / 2.0) - 2.0
            ) * soft**2
            series_error = max(
                series_error,
                abs(contact_scattering(soft, hard) - expected) / abs(soft) ** 3,
            )

    require(oracle_error < TOL, f"contact/oracle S comparison: {oracle_error}")
    require(first_error < SOFT_TOL, f"contact linear coefficient: {first_error}")
    require(second_error < SOFT_TOL, f"contact quadratic phase: {second_error}")
    require(series_error < 90.0, f"contact Taylor remainder/k^3: {series_error}")
    return oracle_error, first_error, second_error, series_error


def main() -> None:
    print(f"soft_current_recon_check: N={N}, dim2={len(TWO_BASIS)}, J={J}")
    charge = check_charge_and_overlap()
    print(
        "CHARGE coordinate=%.3e norm=%.3e overlap=%.3e mismatch=%.3e" % charge
    )
    current = check_current_blocks()
    print("CURRENT commutator=%.3e action=%.3e form_factors=%.3e" % current)
    ward = check_zero_current_ward()
    print(
        "WARD descendant_norm=%.3e residue=%.3e diagonal=%.3e orthogonal=%.3e"
        % ward
    )
    soft = check_contact_soft_expansion()
    print(
        "SOFT oracle=%.3e linear=%.3e quadratic=%.3e remainder_ratio=%.3e"
        % soft
    )
    print("PASS: charge expansion, current form factors, Ward residue, and contact soft phase")


if __name__ == "__main__":
    main()
