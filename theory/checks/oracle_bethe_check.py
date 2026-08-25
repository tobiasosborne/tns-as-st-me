#!/usr/bin/env python3
"""Standalone red/green checks for the exact Bethe oracle O1--O10.

The finite-ring Hamiltonians and momentum projectors are assembled directly
from (J/2)(1-P). No check relies on ``assert``, so ``python -O`` cannot
disable a failure.
"""

from __future__ import annotations

import itertools
import sys
from collections.abc import Callable

import numpy as np
from scipy.optimize import root


N = 18
J = 1.37
ED_TOL = 2.0e-11
BETHE_TOL = 2.0e-11
BOUND_TOL = 2.0e-11
DERIVATIVE_TOL = 3.0e-9
PUISSEUX_TOL = 4.0e1


def fail(message: str) -> None:
    print(f"FAIL: {message}", file=sys.stderr)
    raise SystemExit(1)


def require(condition: bool, message: str) -> None:
    if not condition:
        fail(message)


def dispersion(momentum: float) -> float:
    return J * (1.0 - np.cos(momentum))


def velocity(momentum: float) -> float:
    return J * np.sin(momentum)


def scattering(k1: float, k2: float) -> complex:
    """D7 algebraic ratio A12/A21."""
    z1, z2 = np.exp(1j * k1), np.exp(1j * k2)
    return -(z1 * z2 - 2.0 * z1 + 1.0) / (
        z1 * z2 - 2.0 * z2 + 1.0
    )


def physical_scattering(soft: float, hard: float) -> complex:
    """Outgoing/incoming ratio selected by the relative velocity."""
    ratio = scattering(soft, hard)
    if velocity(hard) > velocity(soft):
        return ratio
    return 1.0 / ratio


def ring_hamiltonian(
    magnons: int,
) -> tuple[np.ndarray, list[tuple[int, ...]]]:
    """Assemble a fixed-magnon-sector Hamiltonian bond by bond."""
    basis = list(itertools.combinations(range(N), magnons))
    index = {state: number for number, state in enumerate(basis)}
    hamiltonian = np.zeros((len(basis), len(basis)))
    for column, state in enumerate(basis):
        occupied = set(state)
        for x in range(N):
            y = (x + 1) % N
            if (x in occupied) == (y in occupied):
                continue
            swapped = (occupied - {x, y}) | ({y} if x in occupied else {x})
            row = index[tuple(sorted(swapped))]
            hamiltonian[column, column] += J / 2.0
            hamiltonian[row, column] -= J / 2.0
    return hamiltonian, basis


def check_one_magnon() -> tuple[float, float]:
    """Check O1 against the independently assembled one-magnon block."""
    hamiltonian, basis = ring_hamiltonian(1)
    sites = np.asarray([state[0] for state in basis])
    residual_error = 0.0
    velocity_error = 0.0
    step = 2.0e-4
    for number in [-5, 1, 7]:
        momentum = 2.0 * np.pi * number / N
        vector = np.exp(1j * momentum * sites) / np.sqrt(N)
        residual_error = max(
            residual_error,
            np.linalg.norm(
                hamiltonian @ vector - dispersion(momentum) * vector
            ),
        )
        central_velocity = (
            dispersion(momentum + step) - dispersion(momentum - step)
        ) / (2.0 * step)
        half_step_velocity = (
            dispersion(momentum + step / 2.0)
            - dispersion(momentum - step / 2.0)
        ) / step
        numerical_velocity = (4.0 * half_step_velocity - central_velocity) / 3.0
        velocity_error = max(
            velocity_error, abs(numerical_velocity - velocity(momentum))
        )
    require(residual_error < ED_TOL, f"O1 one-magnon residual: {residual_error}")
    require(velocity_error < 1.0e-10, f"O1 velocity derivative: {velocity_error}")
    return residual_error, velocity_error


def check_rapidities() -> tuple[float, float]:
    direct_error = 0.0
    inverse_error = 0.0
    for k1, k2 in [(0.23, 1.17), (-0.61, 2.20), (2.80, 0.74)]:
        lambda_1 = 0.5 / np.tan(k1 / 2.0)
        lambda_2 = 0.5 / np.tan(k2 / 2.0)
        difference = lambda_1 - lambda_2
        direct = (difference + 1j) / (difference - 1j)
        inverse = (difference - 1j) / (difference + 1j)
        direct_error = max(direct_error, abs(scattering(k1, k2) - direct))
        inverse_error = max(
            inverse_error, abs(1.0 / scattering(k1, k2) - inverse)
        )
    require(
        max(direct_error, inverse_error) < BETHE_TOL,
        f"O4 rapidity identities: direct={direct_error}, inverse={inverse_error}",
    )
    return direct_error, inverse_error


def quantized_pair(guess: tuple[int, int]) -> tuple[float, float]:
    def equations(momentum: np.ndarray) -> np.ndarray:
        k1, k2 = momentum
        smat = scattering(k1, k2)
        return np.array(
            [
                np.angle(np.exp(1j * N * k1) / smat),
                np.angle(np.exp(1j * N * k2) * smat),
            ]
        )

    solution = root(equations, np.asarray(guess) * 2.0 * np.pi / N)
    require(solution.success, f"Bethe root solve: {solution.message}")
    return float(solution.x[0]), float(solution.x[1])


def check_scattering_ed(
    hamiltonian: np.ndarray, basis: list[tuple[int, ...]]
) -> list[tuple[float, ...]]:
    """Check O2--O4 against periodic Bethe vectors and the full ED spectrum."""
    eigenvalues = np.linalg.eigvalsh(hamiltonian)
    rows = []
    for guess in [(1, 4), (2, 6), (-3, 4)]:
        k1, k2 = quantized_pair(guess)
        smat = scattering(k1, k2)
        bethe_1 = abs(np.exp(1j * N * k1) / smat - 1.0)
        bethe_2 = abs(np.exp(1j * N * k2) * smat - 1.0)
        vector = np.array(
            [
                smat * np.exp(1j * (k1 * x + k2 * y))
                + np.exp(1j * (k2 * x + k1 * y))
                for x, y in basis
            ]
        )
        vector /= np.linalg.norm(vector)
        energy = dispersion(k1) + dispersion(k2)
        residual = np.linalg.norm(hamiltonian @ vector - energy * vector)
        spectral_error = np.min(abs(eigenvalues - energy))
        require(
            max(bethe_1, bethe_2) < BETHE_TOL,
            f"O3 periodic Bethe equations: {bethe_1}, {bethe_2}",
        )
        require(residual < ED_TOL, f"O2/O3 Bethe-vector residual: {residual}")
        require(spectral_error < ED_TOL, f"O2 ED spectral error: {spectral_error}")
        rows.append((k1, k2, energy, residual, spectral_error))
    return rows


def translation_matrix(basis: list[tuple[int, ...]]) -> np.ndarray:
    index = {state: number for number, state in enumerate(basis)}
    translation = np.zeros((len(basis), len(basis)), dtype=complex)
    for column, state in enumerate(basis):
        shifted = tuple(sorted((site + 1) % N for site in state))
        translation[index[shifted], column] = 1.0
    return translation


def momentum_sector(
    hamiltonian: np.ndarray,
    translation: np.ndarray,
    momentum: float,
) -> tuple[np.ndarray, float]:
    """Resolve the eigenvalue exp(-iK) of one-site translation."""
    projector = np.zeros_like(translation)
    power = np.eye(len(translation), dtype=complex)
    for shift in range(N):
        projector += np.exp(1j * momentum * shift) * power
        power = translation @ power
    projector /= N
    projector = (projector + projector.conj().T) / 2.0
    projector_error = max(
        np.linalg.norm(projector @ projector - projector),
        np.linalg.norm(hamiltonian @ projector - projector @ hamiltonian),
    )
    eigenvalues, eigenvectors = np.linalg.eigh(projector)
    frame = eigenvectors[:, eigenvalues > 0.5]
    require(frame.shape[1] > 0, f"empty momentum sector K={momentum}")
    sector = frame.conj().T @ hamiltonian @ frame
    return np.linalg.eigvalsh(sector), projector_error


def check_bound_states(
    hamiltonian: np.ndarray, basis: list[tuple[int, ...]]
) -> list[tuple[float, ...]]:
    """Momentum-resolved ED check of O5 at localized finite-ring strings."""
    translation = translation_matrix(basis)
    rows = []
    for momentum_number in [8, 9]:
        momentum = 2.0 * np.pi * momentum_number / N
        levels, projector_error = momentum_sector(
            hamiltonian, translation, momentum
        )
        exact = J * np.sin(momentum / 2.0) ** 2
        level = levels[np.argmin(abs(levels - exact))]
        error = abs(level - exact)
        continuum = 2.0 * J * (1.0 - np.cos(momentum / 2.0))
        require(projector_error < ED_TOL, f"O5 momentum projector: {projector_error}")
        require(error < BOUND_TOL, f"O5 bound energy K={momentum}: {error}")
        require(
            abs(level - levels[0]) < ED_TOL,
            f"O5 matched level is not the sector ground state K={momentum}",
        )
        require(level < continuum, f"O5 level not below continuum K={momentum}")
        rows.append((momentum, level, exact, error, projector_error))
    return rows


def richardson_derivatives(
    function: Callable[[float], float], step: float
) -> tuple[float, float]:
    f0 = function(0.0)

    def first(h: float) -> float:
        return (function(h) - function(-h)) / (2.0 * h)

    def second(h: float) -> float:
        return (function(h) - 2.0 * f0 + function(-h)) / h**2

    first_value = (4.0 * first(step / 2.0) - first(step)) / 3.0
    second_value = (4.0 * second(step / 2.0) - second(step)) / 3.0
    return first_value, second_value / 2.0


def check_soft_oracle() -> tuple[float, ...]:
    """Check O6--O9, including both physical signs and the even invariant."""
    limit_error = 0.0
    first_error = 0.0
    second_error = 0.0
    invariant_error = 0.0
    parity_error = 0.0
    remainder_ratio = 0.0
    for hard in [-3.00, -2.40, -1.10, -0.37, 0.37, 1.10, 2.40, 3.00]:
        omega_h = dispersion(hard)
        velocity_h = velocity(hard)
        sign = np.sign(velocity_h)
        curvature = abs(velocity_h) / omega_h
        phase = lambda soft: float(np.angle(physical_scattering(soft, hard)))
        first, second = richardson_derivatives(phase, 2.0e-3)
        limit_error = max(
            limit_error,
            abs(physical_scattering(0.0, hard) - 1.0),
            abs(phase(0.0)),
        )
        first_error = max(first_error, abs(first - 2.0 * sign))
        second_error = max(second_error, abs(second - curvature))
        invariant_error = max(
            invariant_error,
            abs(curvature - np.sqrt((2.0 * J - omega_h) / omega_h)),
            abs(curvature - 1.0 / np.tan(abs(hard) / 2.0)),
        )
        for soft in [-0.004, -0.002, 0.002, 0.004]:
            expected = 1.0 + 2j * sign * soft + (
                1j * curvature - 2.0
            ) * soft**2
            remainder_ratio = max(
                remainder_ratio,
                abs(physical_scattering(soft, hard) - expected) / abs(soft) ** 3,
            )
            parity_error = max(
                parity_error,
                abs(phase(soft) - np.angle(physical_scattering(-soft, -hard))),
            )
    require(limit_error < BETHE_TOL, f"O6 soft limit/intercept: {limit_error}")
    require(first_error < DERIVATIVE_TOL, f"O7 signed linear phase: {first_error}")
    require(second_error < DERIVATIVE_TOL, f"O7 quadratic phase: {second_error}")
    require(invariant_error < BETHE_TOL, f"O9 invariant identity: {invariant_error}")
    require(parity_error < BETHE_TOL, f"O9 physical parity: {parity_error}")
    require(remainder_ratio < 1.0e2, f"O8 compact cubic remainder: {remainder_ratio}")
    return (
        limit_error,
        first_error,
        second_error,
        invariant_error,
        parity_error,
        remainder_ratio,
    )


def check_puiseux() -> tuple[float, float]:
    """Check both O10 remainders after division by omega_s^(3/2)."""
    phase_ratio = 0.0
    scattering_ratio = 0.0
    for hard in [0.37, 1.10, 2.40, 3.00]:
        omega_h = dispersion(hard)
        velocity_h = velocity(hard)
        for sigma in [-1.0, 1.0]:
            for magnitude in [0.002, 0.004, 0.008, 0.016]:
                soft = sigma * magnitude
                omega_s = dispersion(soft)
                root_energy = np.sqrt(2.0 * omega_s / J)
                phase_expected = (
                    2.0 * sigma * root_energy
                    + 2.0 * velocity_h * omega_s / (J * omega_h)
                )
                scattering_expected = (
                    1.0
                    + 2j * sigma * root_energy
                    + (-4.0 + 2j * velocity_h / omega_h) * omega_s / J
                )
                phase_ratio = max(
                    phase_ratio,
                    abs(np.angle(scattering(soft, hard)) - phase_expected)
                    / omega_s**1.5,
                )
                scattering_ratio = max(
                    scattering_ratio,
                    abs(scattering(soft, hard) - scattering_expected)
                    / omega_s**1.5,
                )
    require(phase_ratio < PUISSEUX_TOL, f"O10 phase remainder: {phase_ratio}")
    require(
        scattering_ratio < PUISSEUX_TOL,
        f"O10 S-matrix remainder: {scattering_ratio}",
    )
    return phase_ratio, scattering_ratio


def main() -> None:
    print(f"oracle_bethe_check: N={N}, dim={N * (N - 1) // 2}, J={J}")
    one = check_one_magnon()
    print("ONE residual=%.3e velocity=%.3e" % one)
    direct_error, inverse_error = check_rapidities()
    print(f"RAPIDITY S12_error={direct_error:.3e} S21_error={inverse_error:.3e}")
    hamiltonian, basis = ring_hamiltonian(2)
    for row in check_scattering_ed(hamiltonian, basis):
        print("ED k1=% .12f k2=% .12f E=%.12f residual=%.3e spectral=%.3e" % row)
    for row in check_bound_states(hamiltonian, basis):
        print("BOUND K=%.12f level=%.12f exact=%.12f error=%.3e projector=%.3e" % row)
    soft = check_soft_oracle()
    print(
        "SOFT limit=%.3e linear=%.3e quadratic=%.3e invariant=%.3e "
        "parity=%.3e remainder_ratio=%.3e" % soft
    )
    puiseux = check_puiseux()
    print("PUISEUX phase_ratio=%.3e S_ratio=%.3e" % puiseux)
    print("PASS: oracle facts O1--O10")


if __name__ == "__main__":
    main()
