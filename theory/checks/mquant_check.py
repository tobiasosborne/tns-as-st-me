#!/usr/bin/env python3
"""Independent certificate for Theorem M-quant.

The frozen-boundary spin-1/2 XXZ sector Hamiltonian is assembled here from
spin configurations; no Julia module is imported.  Checks use explicit
failures, so ``python -O`` is equally strict.  ``--red`` deliberately reverses
the current and must fail, providing the red half of the certificate.
"""

from __future__ import annotations

import argparse
import itertools
import json
import sys
from pathlib import Path

import numpy as np


TOL_OPERATOR = 2.0e-13
TOL_TIME = 2.0e-12
HEADLINE_TOL = 4.5e-3
ROOT = Path(__file__).resolve().parents[2]
SCAN = ROOT / "numerics" / "results" / "memory-scan-1.json"


def fail(message: str) -> None:
    print(f"FAIL: {message}", file=sys.stderr)
    raise SystemExit(1)


def require(condition: bool, message: str) -> None:
    if not condition:
        fail(message)


def sector_basis(n_sites: int, n_down: int) -> list[tuple[int, ...]]:
    """Full-site bit strings with frozen up/down left/right endpoints."""
    basis = []
    for down_sites in itertools.combinations(range(1, n_sites - 1), n_down):
        bits = [0] * n_sites
        bits[-1] = 1
        for site in down_sites:
            bits[site] = 1
        basis.append(tuple(bits))
    return basis


def xxz_sector(
    n_sites: int, n_down: int, j_perp: float, delta: float
) -> tuple[np.ndarray, list[tuple[int, ...]], dict[tuple[int, ...], int]]:
    """Build H=-sum[J/2(S+S-+h.c.)+J*Delta SzSz] bond by bond."""
    basis = sector_basis(n_sites, n_down)
    index = {state: column for column, state in enumerate(basis)}
    hamiltonian = np.zeros((len(basis), len(basis)), dtype=complex)
    j_z = j_perp * delta
    for column, state in enumerate(basis):
        for x in range(n_sites - 1):
            sx = 0.5 - state[x]
            sy = 0.5 - state[x + 1]
            hamiltonian[column, column] -= j_z * sx * sy
            if x == 0 or x == n_sites - 2 or state[x] == state[x + 1]:
                continue
            moved = list(state)
            moved[x], moved[x + 1] = moved[x + 1], moved[x]
            hamiltonian[index[tuple(moved)], column] -= j_perp / 2.0
    return hamiltonian, basis, index


def charge_operator(
    basis: list[tuple[int, ...]], first: int, last: int
) -> np.ndarray:
    values = [sum(0.5 - state[x] for x in range(first, last + 1)) for state in basis]
    return np.diag(values).astype(complex)


def spin_current(
    basis: list[tuple[int, ...]],
    index: dict[tuple[int, ...], int],
    bond: int,
    j_perp: float,
) -> np.ndarray:
    """j=J/(2i)(S+_x S-_{x+1}-S-_x S+_{x+1})."""
    current = np.zeros((len(basis), len(basis)), dtype=complex)
    for column, state in enumerate(basis):
        if state[bond] == state[bond + 1]:
            continue
        moved = list(state)
        moved[bond], moved[bond + 1] = moved[bond + 1], moved[bond]
        # down-up is acted on by S+S-; up-down by -S-S+.
        coefficient = -0.5j * j_perp if state[bond] == 1 else 0.5j * j_perp
        current[index[tuple(moved)], column] += coefficient
    return current


def exact_time_integral(
    hamiltonian: np.ndarray,
    observable: np.ndarray,
    state: np.ndarray,
    t_initial: float,
    t_final: float,
) -> complex:
    """Integrate <observable>(t) analytically in the energy eigenbasis."""
    energies, vectors = np.linalg.eigh(hamiltonian)
    coefficients = vectors.conj().T @ state
    obs_energy = vectors.conj().T @ observable @ vectors
    frequency = energies[:, None] - energies[None, :]
    duration = t_final - t_initial
    factor = np.full(frequency.shape, duration, dtype=complex)
    nonzero = np.abs(frequency) > 2.0e-14
    factor[nonzero] = (
        np.exp(1j * frequency[nonzero] * t_final)
        - np.exp(1j * frequency[nonzero] * t_initial)
    ) / (1j * frequency[nonzero])
    weights = coefficients.conj()[:, None] * coefficients[None, :]
    return np.sum(weights * obs_energy * factor)


def evolved_expectation(
    hamiltonian: np.ndarray, observable: np.ndarray, state: np.ndarray, time: float
) -> complex:
    energies, vectors = np.linalg.eigh(hamiltonian)
    coefficients = vectors.conj().T @ state
    evolved = vectors @ (np.exp(-1j * energies * time) * coefficients)
    return np.vdot(evolved, observable @ evolved)


def check_flux(red: bool) -> tuple[float, float]:
    rng = np.random.default_rng(20260825)
    max_operator_error = 0.0
    max_time_error = 0.0
    for n_sites, n_down, first, last in [(7, 2, 2, 3), (8, 3, 2, 5)]:
        hamiltonian, basis, index = xxz_sector(n_sites, n_down, 1.17, 2.3)
        require(
            np.linalg.norm(hamiltonian - hamiltonian.conj().T) < TOL_OPERATOR,
            "independent XXZ Hamiltonian is not Hermitian",
        )
        window_charge = charge_operator(basis, first, last)
        boundary_flux = spin_current(basis, index, first - 1, 1.17) - spin_current(
            basis, index, last, 1.17
        )
        if red:
            boundary_flux = -boundary_flux
        derivative = 1j * (hamiltonian @ window_charge - window_charge @ hamiltonian)
        operator_error = np.linalg.norm(derivative - boundary_flux, ord=np.inf)
        max_operator_error = max(max_operator_error, operator_error)

        state = rng.normal(size=len(basis)) + 1j * rng.normal(size=len(basis))
        state /= np.linalg.norm(state)
        t_initial, t_final = 0.137, 0.913
        delta_charge = evolved_expectation(
            hamiltonian, window_charge, state, t_final
        ) - evolved_expectation(hamiltonian, window_charge, state, t_initial)
        integrated_flux = exact_time_integral(
            hamiltonian, boundary_flux, state, t_initial, t_final
        )
        time_error = abs(delta_charge - integrated_flux)
        max_time_error = max(max_time_error, time_error)

    require(
        max_operator_error < TOL_OPERATOR,
        f"finite-N operator continuity residue {max_operator_error:.3e}",
    )
    require(
        max_time_error < TOL_TIME,
        f"finite-time flux integral residue {max_time_error:.3e}",
    )
    return max_operator_error, max_time_error


def check_scan() -> tuple[int, float, float, float, float]:
    with SCAN.open(encoding="utf-8") as handle:
        data = json.load(handle)
    rows = []
    for entry in data["runs"]:
        result = entry["result"]
        params = result["params"]
        if not (
            params["N"] == 160
            and params["standoff"] == 36
            and params["dwmax"] == 3
            and params["Jperp"] == 1
            and abs(result["trapped"]) < 1.0e-6
        ):
            continue
        residual_x1 = abs(result["dx1"] + 2.0 * result["transmission"])
        residual_x2 = abs(result["dx2"] + 2.0 * result["transmission"])
        # X2 is the integrated-magnetisation proxy for Bd3.  The committed
        # X1-X2 spread is the scan's own geometry/estimator systematic.
        budget = (
            result["dx_estimator_spread"]
            + 2.0 * abs(result["trapped"])
            + 1.0e-9
        )
        require(
            residual_x1 <= budget and residual_x2 <= budget,
            f"{entry['label']} exceeds committed estimator budget",
        )
        rows.append((residual_x1, residual_x2, budget, abs(result["trapped"])))

    require(len(rows) == 9, f"expected 9 clean committed scan rows, found {len(rows)}")
    max_x1 = max(row[0] for row in rows)
    max_x2 = max(row[1] for row in rows)
    max_budget = max(row[2] for row in rows)
    max_trapped = max(row[3] for row in rows)
    require(max_x1 < HEADLINE_TOL, f"headline |dx1+2T|={max_x1:.6f}")
    return len(rows), max_x1, max_x2, max_budget, max_trapped


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--red", action="store_true", help="inject the wrong current sign (must fail)"
    )
    args = parser.parse_args()
    operator_error, time_error = check_flux(args.red)
    n_rows, x1_error, x2_error, budget, trapped = check_scan()
    print(
        "FLUX operator=%.3e finite_time=%.3e (independent frozen-boundary sector)"
        % (operator_error, time_error)
    )
    print(
        "SCAN rows=%d max|dx1+2T|=%.6f (~0.004) "
        "max|dx2+2T|=%.6f budget=%.6f trapped=%.3e"
        % (n_rows, x1_error, x2_error, budget, trapped)
    )
    print("PASS: M-quant flux identity and committed numerical certificate")


if __name__ == "__main__":
    main()
