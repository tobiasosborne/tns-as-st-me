#!/usr/bin/env python3
"""Standalone red/green oracle check: finite-ring ED and soft derivatives."""

from __future__ import annotations

import itertools

import numpy as np
from scipy.optimize import root


N = 18
J = 1.37
ED_TOL = 2.0e-11
BETHE_TOL = 2.0e-11
DERIVATIVE_TOL = 3.0e-9


def scattering(k1: float, k2: float) -> complex:
    """D7 ratio A12/A21."""
    z1, z2 = np.exp(1j * k1), np.exp(1j * k2)
    return -(z1 * z2 - 2.0 * z1 + 1.0) / (z1 * z2 - 2.0 * z2 + 1.0)


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
        inverse_error = max(inverse_error, abs(1.0 / scattering(k1, k2) - inverse))
    assert max(direct_error, inverse_error) < BETHE_TOL
    return direct_error, inverse_error


def ring_hamiltonian() -> tuple[np.ndarray, list[tuple[int, int]]]:
    basis = list(itertools.combinations(range(N), 2))
    index = {state: n for n, state in enumerate(basis)}
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


def quantized_pair(guess: tuple[int, int]) -> tuple[float, float]:
    def equations(momentum: np.ndarray) -> np.ndarray:
        k1, k2 = momentum
        smat = scattering(k1, k2)
        return np.array(
            [np.angle(np.exp(1j * N * k1) / smat),
             np.angle(np.exp(1j * N * k2) * smat)]
        )

    solution = root(equations, np.asarray(guess) * 2.0 * np.pi / N)
    assert solution.success, solution.message
    return float(solution.x[0]), float(solution.x[1])


def check_ed() -> list[tuple[float, ...]]:
    hamiltonian, basis = ring_hamiltonian()
    eigenvalues = np.linalg.eigvalsh(hamiltonian)
    rows = []
    for guess in [(1, 4), (2, 6), (-3, 4)]:
        k1, k2 = quantized_pair(guess)
        smat = scattering(k1, k2)
        bethe_1 = abs(np.exp(1j * N * k1) / smat - 1.0)
        bethe_2 = abs(np.exp(1j * N * k2) * smat - 1.0)
        vector = np.array(
            [smat * np.exp(1j * (k1 * x + k2 * y))
             + np.exp(1j * (k2 * x + k1 * y)) for x, y in basis]
        )
        vector /= np.linalg.norm(vector)
        energy = J * (2.0 - np.cos(k1) - np.cos(k2))
        residual = np.linalg.norm(hamiltonian @ vector - energy * vector)
        spectral_error = np.min(abs(eigenvalues - energy))
        assert max(bethe_1, bethe_2) < BETHE_TOL
        assert residual < ED_TOL
        assert spectral_error < ED_TOL
        rows.append((k1, k2, energy, residual, spectral_error))
    return rows


def check_soft_derivatives() -> list[tuple[float, ...]]:
    rows = []
    momenta = np.arange(-8, 9) * 2.0e-4
    for hard in [0.37, 1.10, 2.40, 3.00]:
        phases = np.unwrap(np.angle([scattering(soft, hard) for soft in momenta]))
        coefficients = np.polynomial.polynomial.polyfit(momenta, phases, 6)
        first, second = coefficients[1], coefficients[2]
        exact_second = 1.0 / np.tan(hard / 2.0)
        assert abs(first - 2.0) < DERIVATIVE_TOL
        assert abs(second - exact_second) < DERIVATIVE_TOL
        rows.append((hard, first, second, exact_second))
    return rows


def main() -> None:
    print(f"oracle_bethe_check: N={N}, dim={N * (N - 1) // 2}, J={J}")
    direct_error, inverse_error = check_rapidities()
    print(f"RAPIDITY S12_error={direct_error:.3e} S21_error={inverse_error:.3e}")
    for row in check_ed():
        print("ED k1=% .12f k2=% .12f E=%.12f residual=%.3e spectral=%.3e" % row)
    for row in check_soft_derivatives():
        print("SOFT kh=%.2f d1=%.12f c2=%.12f exact_c2=%.12f" % row)
    print("PASS: periodic Bethe vectors, ED spectrum, and soft coefficients")


if __name__ == "__main__":
    main()
