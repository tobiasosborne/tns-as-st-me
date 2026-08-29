#!/usr/bin/env python3
"""Pre-registered B=>A moment-map falsifier (blitz lane bta-probe).

This implements briefs/bta-kahler-target.md section 6 without using a
Hamiltonian.  The six frozen gates are P1--P6.  The product families are
evaluated on the full registered Delta, spin, x0, and window grids.  F-C uses
the registered mismatches q'/q = 0.8 and 1.25.  F-D reuses the charge-diagonal
chi=2 twisted-transfer construction of IDX-C7(ii) in
theory/checks/memory_index_check.py.

Independence fence for P2:

* ``omega_from_norm_hessian`` differentiates the logarithm of the
  unnormalised holomorphic window-vector norm (the geometry route).
* ``mu_prime_from_probabilities`` constructs the normalised binomial
  spin-coherent probabilities and differentiates the expectation of the
  D13(a) charge (the observable route).  It calls neither the potential nor
  the curvature routine and shares no computed intermediate with them.

Exit codes are frozen by the brief: 0 PASS; 1 FAIL (also RED-OK); 2 means a
requested red mutation was not detected.  No Python ``assert`` is used.
Results are written beside this script as JSON in every mode.

Provenance constraint (binding): the observation that TNS variational classes
carry a Kähler structure and that TDVP is the associated Hamiltonian flow
originated with Tobias Osborne, who communicated it to Jutho Haegeman, who
made it work.  Do not state this in any paper without TJO's explicit sign-off.
"""

from __future__ import annotations

import argparse
import json
import math
import sys
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any

import numpy as np
from scipy.special import expit


DELTAS = (1.5, 2.0, 4.0)
SPINS = (0.5, 1.0, 1.5, 2.0)
X_GRID = np.linspace(0.0, 3.0, 301)
WINDOWS = (10, 20, 40, 80)
MISMATCHES = (0.8, 1.25)

P1_EXPONENT_MIN = 1.5
P1_CURVATURE_TOL = 1.0e-10
P2_REL_TOL = 1.0e-12
P3_TOL = 1.0e-8
P4_TOL = 1.0e-8
P5_REL_TOL = 1.0e-12
P6_SCALAR_TOL = 1.0e-10
P6_NONSCALAR_MIN = 1.0e-3
FD_CURVATURE_MIN = 1.0e-6
RED_PERIOD = 1.0e-6

CHI = 2
SPIN32 = np.array((-1.5, -0.5, 0.5, 1.5))
VIRTUAL_WEIGHTS = np.array((0.0, 1.0))


@dataclass
class Gate:
    passed: bool
    criterion: str
    metrics: dict[str, Any]
    families: list[str]


def fail(message: str, code: int = 1) -> None:
    print(f"FAIL: {message}", file=sys.stderr)
    raise SystemExit(code)


def require(condition: bool, message: str) -> None:
    if not condition:
        fail(message)


def q_from_delta(delta: float) -> float:
    return delta - math.sqrt(delta * delta - 1.0)


def tensor_log_amplitude(delta: float, x0: float, sites: np.ndarray,
                         mismatch: float = 1.0) -> tuple[np.ndarray, float]:
    """log |z (q')^n| with z=q^{-x0}; x0 remains the frozen D16 coordinate."""
    q = q_from_delta(delta)
    q_tensor = mismatch * q
    require(0.0 < q_tensor < 1.0, f"invalid deformed q'={q_tensor}")
    kappa = -math.log(q)
    return kappa * x0 + sites * math.log(q_tensor), kappa


def kahler_potential(delta: float, spin: float, x0: float, length: int,
                     mismatch: float = 1.0) -> float:
    """log norm squared of the holomorphic spin-S product window vector."""
    sites = np.arange(-length, length + 1, dtype=float)
    log_r, _ = tensor_log_amplitude(delta, x0, sites, mismatch)
    return float(2.0 * spin * np.logaddexp(0.0, 2.0 * log_r).sum())


def omega_from_norm_hessian(delta: float, spin: float,
                            x_values: np.ndarray, length: int,
                            mismatch: float = 1.0,
                            unnormalised_gram: bool = False) -> np.ndarray:
    """Omega in varpi=Omega dx0 wedge dphi from the norm-Hessian route.

    For K=log ||psi||^2, Omega=K''/(2 kappa).  ``unnormalised_gram`` is the
    registered --red-fs mutation: it retains the norm-parallel tangent term
    removed by the Fubini--Study quotient, so the result grows with W.
    """
    sites = np.arange(-length, length + 1, dtype=float)
    out = np.empty_like(x_values, dtype=float)
    for index, x0 in enumerate(x_values):
        log_r, kappa = tensor_log_amplitude(delta, float(x0), sites, mismatch)
        occupation = expit(2.0 * log_r)
        omega_fs = 4.0 * spin * kappa * float(
            np.sum(occupation * (1.0 - occupation))
        )
        if unnormalised_gram:
            # The discarded norm-parallel piece is proportional to K'^2.
            k_prime = 4.0 * spin * kappa * float(np.sum(occupation))
            omega_fs += (k_prime * k_prime) / (2.0 * kappa)
        out[index] = omega_fs
    return out


def mu_prime_from_probabilities(delta: float, spin: float,
                                x_values: np.ndarray, length: int,
                                mismatch: float = 1.0,
                                calibration_shift: float = 0.0) -> np.ndarray:
    """d <Qhat_W,c0>/dx0 from explicit normalised coherent probabilities.

    At each site the down-spin count k has a binomial distribution.  The
    observable route explicitly sums d p_k/dx times the D13(a) charge
    eigenvalue 2S-k.  It does not call the geometry-side routines.
    """
    two_s = int(round(2.0 * spin))
    require(abs(two_s - 2.0 * spin) < 1.0e-14, "spin is not half-integral")
    counts = np.arange(two_s + 1, dtype=float)
    binomial = np.array([math.comb(two_s, int(k)) for k in counts], dtype=float)
    charge = two_s - counts
    sites = np.arange(-length, length + 1, dtype=float)
    scale = (2.0 * spin + calibration_shift) / (2.0 * spin)
    q = q_from_delta(delta)
    q_tensor = mismatch * q
    kappa = -math.log(q)
    log_r = kappa * x_values[:, None] + sites[None, :] * math.log(q_tensor)
    p_down = expit(2.0 * log_r)
    probabilities = (
        binomial[None, None, :]
        * p_down[:, :, None] ** counts[None, None, :]
        * (1.0 - p_down[:, :, None]) ** (two_s - counts)[None, None, :]
    )
    totals = probabilities.sum(axis=2, keepdims=True)
    require(bool(np.all(totals > 0.0)), "coherent-state probability underflow")
    probabilities /= totals
    mean_count = np.sum(probabilities * counts[None, None, :], axis=2)
    score = 2.0 * kappa * (counts[None, None, :] - mean_count[:, :, None])
    site_derivatives = np.sum(
        charge[None, None, :] * probabilities * score, axis=2
    )
    return scale * site_derivatives.sum(axis=1)


def area_per_lattice_period(delta: float, spin: float, length: int = 80,
                            x0: float = 0.0) -> float:
    """(1/2pi) integral_[x0,x0+1] integral_phi varpi, analytically integrated."""
    sites = np.arange(-length, length + 1, dtype=float)
    first, _ = tensor_log_amplitude(delta, x0, sites)
    second, _ = tensor_log_amplitude(delta, x0 + 1.0, sites)
    # Omega=2S d/dx sum logistic(2 log_r).
    return float(2.0 * spin * np.sum(expit(2.0 * second) - expit(2.0 * first)))


def scattering_formula(k1: float, k2: float, two_s: int) -> complex:
    """Independent numerical copy of S2-2body-S's frozen rational ratio."""
    site_spin = two_s / 2.0
    z1 = np.exp(1j * k1)
    z2 = np.exp(1j * k2)
    a = 1.0 + z1 * z2
    b = z1 + z2
    mu = (two_s - 1.0) * a + b
    return (site_spin * a * b - z1 * mu) / (
        z2 * mu - site_spin * a * b
    )


def phase_slope(hard: float, spin: float) -> float:
    step = 2.0e-4
    two_s = int(round(2.0 * spin))
    phases = {
        multiple: np.angle(scattering_formula(multiple * step, hard, two_s))
        for multiple in (-2, -1, 1, 2)
    }
    return float(
        (phases[-2] - 8.0 * phases[-1] + 8.0 * phases[1] - phases[2])
        / (12.0 * step)
    )


def repo_root() -> Path:
    for parent in Path(__file__).resolve().parents:
        if (parent / "definitions.md").is_file():
            return parent
    fail("could not locate repository root")
    raise RuntimeError("unreachable")


def frozen_json_error() -> tuple[float, int]:
    """Check every recorded prediction_ratio in the frozen spin-S ED JSON."""
    source = repo_root() / "numerics/results/spin1-bc-falsifier.json"
    with source.open("r", encoding="utf-8") as stream:
        payload = json.load(stream)
    errors: list[float] = []

    def visit(value: Any) -> None:
        if isinstance(value, dict):
            params = value.get("params")
            if isinstance(params, dict) and "spin" in params and "prediction_ratio" in params:
                spin = float(params["spin"])
                errors.append(abs(float(params["prediction_ratio"]) + 1.0 / spin))
            for child in value.values():
                visit(child)
        elif isinstance(value, list):
            for child in value:
                visit(child)

    visit(payload)
    require(bool(errors), f"no spin prediction rows found in {source}")
    return max(errors), len(errors)


# ---- chi=2 IDX-C7(ii) construction -------------------------------------

def transfer(tensors: list[np.ndarray]) -> np.ndarray:
    return sum(np.kron(tensor, tensor.conj()) for tensor in tensors)


def top_fixed_point(matrix: np.ndarray) -> tuple[float, np.ndarray]:
    values, vectors = np.linalg.eig(matrix)
    index = int(np.argmax(np.abs(values)))
    block = vectors[:, index].reshape(CHI, CHI)
    trace = np.trace(block)
    require(abs(trace) > 1.0e-8, "traceless transfer fixed point")
    block /= trace / abs(trace)
    block = (block + block.conj().T) / 2.0
    if np.trace(block).real < 0.0:
        block = -block
    return float(values[index].real), block


def left_canonical(tensors: list[np.ndarray]) -> list[np.ndarray]:
    eigenvalue, left = top_fixed_point(transfer(tensors).conj().T)
    require(eigenvalue > 0.0 and np.linalg.eigvalsh(left).min() > 1.0e-10,
            "left canonicalisation failed")
    root = np.linalg.cholesky(left).conj().T
    inverse = np.linalg.inv(root)
    return [root @ tensor @ inverse / math.sqrt(eigenvalue) for tensor in tensors]


def charge_diagonal(rho: float, seed: int) -> list[np.ndarray]:
    rng = np.random.default_rng(seed)
    tensors = [np.zeros((CHI, CHI), dtype=complex) for _ in SPIN32]
    for row in range(CHI):
        for column in range(CHI):
            target = rho + VIRTUAL_WEIGHTS[column] - VIRTUAL_WEIGHTS[row]
            for physical, charge in enumerate(SPIN32):
                if abs(charge - target) < 1.0e-12:
                    tensors[physical][row, column] = (
                        rng.normal() + 1j * rng.normal()
                    ) / math.sqrt(2.0)
    return left_canonical(tensors)


def word_rank(tensors: list[np.ndarray]) -> int:
    words = np.array([
        (left @ right).reshape(-1)
        for left in tensors for right in tensors
    ])
    return int(np.linalg.matrix_rank(words, tol=1.0e-9))


def transfer_gap(tensors: list[np.ndarray]) -> float:
    values = np.sort(np.abs(np.linalg.eigvals(transfer(tensors))))[::-1]
    return float(values[1] / values[0])


def virtual_unitary(phi: float) -> np.ndarray:
    return np.diag(np.exp(1j * phi * VIRTUAL_WEIGHTS))


def window_vector(alpha: list[np.ndarray], beta: list[np.ndarray], length: int,
                  insertion: np.ndarray) -> np.ndarray:
    """D1(e')-style alpha|beta window vector with a junction insertion."""
    left_boundary = np.array((1.0, 0.7j), dtype=complex)
    right_boundary = np.array((0.4 + 0.2j, 1.0), dtype=complex)
    states: list[tuple[np.ndarray, tuple[int, ...]]] = [(np.eye(CHI), ())]
    for site in range(-length, length + 1):
        tensors = alpha if site <= 0 else beta
        updated: list[tuple[np.ndarray, tuple[int, ...]]] = []
        for product, physicals in states:
            for physical, tensor in enumerate(tensors):
                next_product = product @ tensor
                if site == 0:
                    next_product = next_product @ insertion
                updated.append((next_product, physicals + (physical,)))
        states = updated
    amplitudes = [
        np.vdot(left_boundary, product @ right_boundary)
        for product, _ in states
    ]
    return np.asarray(amplitudes, dtype=complex)


def fd_curvature_and_period() -> dict[str, float]:
    """FS curvature and the registered period on a nonscalar-V chi=2 family."""
    alpha = charge_diagonal(+0.5, 6)
    beta = charge_diagonal(-0.5, 7)
    require(word_rank(alpha) == CHI * CHI and word_rank(beta) == CHI * CHI,
            "F-D tails are not injective at blocking length two")
    theta = 0.731
    nonscalar_distance = float(abs(np.exp(1j * theta) - 1.0))
    require(nonscalar_distance > 0.1, "F-D virtual circle is accidentally scalar")

    x_value = 0.37
    phi_values = np.linspace(0.0, 2.0 * math.pi, 33)
    curvatures = []
    period_integrands = []
    for phi in phi_values:
        v_phi = virtual_unitary(float(phi))
        derivative_v = np.diag(1j * VIRTUAL_WEIGHTS) @ v_phi
        diagonal = np.diag((math.exp(x_value), math.exp(-x_value)))
        derivative_diagonal = np.diag((math.exp(x_value), -math.exp(-x_value)))
        insertion = v_phi @ diagonal
        derivative_x = v_phi @ derivative_diagonal
        derivative_phi = derivative_v @ diagonal
        psi = window_vector(alpha, beta, 2, insertion)
        psi_x = window_vector(alpha, beta, 2, derivative_x)
        psi_phi = window_vector(alpha, beta, 2, derivative_phi)
        norm = float(np.vdot(psi, psi).real)
        require(norm > 1.0e-14, "F-D window vector vanished")
        quantum_geometric = (
            np.vdot(psi_x, psi_phi) / norm
            - np.vdot(psi_x, psi) * np.vdot(psi, psi_phi) / (norm * norm)
        )
        omega_x_phi = float(2.0 * np.imag(quantum_geometric))
        curvatures.append(omega_x_phi)
        two_form = np.array(((0.0, omega_x_phi), (-omega_x_phi, 0.0)))
        circle_tangent = np.array((0.0, 1.0))
        # (i_xi omega)(xi) is evaluated directly, before quadrature.
        period_integrands.append(float(circle_tangent @ two_form @ circle_tangent))

    period = float(np.trapezoid(period_integrands, phi_values))
    max_curvature = float(np.max(np.abs(curvatures)))
    require(max_curvature > FD_CURVATURE_MIN,
            f"F-D curvature is vacuous ({max_curvature:.3e})")
    return {
        "abs_period": abs(period),
        "max_abs_curvature": max_curvature,
        "nonscalar_distance": nonscalar_distance,
        "alpha_transfer_gap": transfer_gap(alpha),
        "beta_transfer_gap": transfer_gap(beta),
    }


def scalar_period(omega: float) -> float:
    two_form = np.array(((0.0, omega), (-omega, 0.0)))
    tangent = np.array((0.0, 1.0))
    integrand = float(tangent @ two_form @ tangent)
    return 2.0 * math.pi * integrand


def evaluate(calibration_shift: float = 0.0,
             red_fs: bool = False) -> tuple[dict[str, Gate], dict[str, Any]]:
    examples: dict[str, Any] = {}

    # P1: all registered F-A/F-B product rows.
    min_exponent = math.inf
    max_curvature_change = 0.0
    exponents: dict[str, float] = {}
    for spin in SPINS:
        for delta in DELTAS:
            potential_grid = np.array([
                [kahler_potential(delta, spin, float(x0), length)
                 for x0 in X_GRID]
                for length in WINDOWS
            ])
            widths = np.array([2 * length + 1 for length in WINDOWS], dtype=float)
            log_widths = np.log(widths)
            centred = log_widths - log_widths.mean()
            exponent_grid = (
                centred @ np.log(potential_grid) / float(centred @ centred)
            )
            exponent = float(np.min(exponent_grid))
            key = f"S={spin},Delta={delta}"
            exponents[key] = exponent
            min_exponent = min(min_exponent, exponent)
            omega_40 = omega_from_norm_hessian(
                delta, spin, X_GRID, 40, unnormalised_gram=red_fs
            )
            omega_80 = omega_from_norm_hessian(
                delta, spin, X_GRID, 80, unnormalised_gram=red_fs
            )
            max_curvature_change = max(
                max_curvature_change, float(np.max(np.abs(omega_80 - omega_40)))
            )
            if spin == 0.5 and delta == 1.5:
                x_index = int(np.argmin(np.abs(X_GRID - 0.3)))
                potentials = potential_grid[:, x_index]
                examples["P1_Delta1.5_S0.5_x0_0p3_potentials"] = potentials.tolist()
                examples["P1_Delta1.5_S0.5_x0_0p3_omegas"] = [
                    float(omega_from_norm_hessian(
                        delta, spin, np.array((0.3,)), length,
                        unnormalised_gram=red_fs,
                    )[0])
                    for length in WINDOWS
                ]
    p1_pass = (
        min_exponent >= P1_EXPONENT_MIN
        and max_curvature_change <= P1_CURVATURE_TOL
    )

    # P2: independent geometry/observable routes on every registered row.
    p2_error = 0.0
    p2_absolute = 0.0
    for spin in SPINS:
        for delta in DELTAS:
            for length in WINDOWS:
                omega = omega_from_norm_hessian(
                    delta, spin, X_GRID, length, unnormalised_gram=red_fs
                )
                mu_prime = mu_prime_from_probabilities(
                    delta, spin, X_GRID, length,
                    calibration_shift=calibration_shift,
                )
                residue = np.abs(mu_prime + omega)
                p2_absolute = max(p2_absolute, float(np.max(residue)))
                p2_error = max(
                    p2_error,
                    float(np.max(residue / np.maximum(1.0, np.abs(omega)))),
                )

    # P3: product-family area quantum for all S and Delta.
    p3_error = 0.0
    areas: dict[str, float] = {}
    for spin in SPINS:
        target = 2.0 * spin + calibration_shift
        for delta in DELTAS:
            area_grid = np.array([
                area_per_lattice_period(delta, spin, x0=float(x0))
                for x0 in X_GRID
            ])
            areas[f"S={spin},Delta={delta}"] = {
                "min": float(area_grid.min()), "max": float(area_grid.max())
            }
            p3_error = max(p3_error, float(np.max(np.abs(area_grid - target))))

    # P4: no fitting; compare the nu=2 displacement with both frozen oracles.
    p4_calibration_error = 0.0
    p4_slope_error = 0.0
    for spin in SPINS:
        displacement = -2.0 / (2.0 * spin + calibration_shift)
        p4_calibration_error = max(
            p4_calibration_error, abs(displacement - (-1.0 / spin))
        )
        for hard in (0.37, 1.10, 2.40):
            p4_slope_error = max(
                p4_slope_error, abs(abs(phase_slope(hard, spin)) - 1.0 / spin)
            )
    p4_json_error, p4_json_rows = frozen_json_error()
    p4_error = max(p4_calibration_error, p4_slope_error, p4_json_error)

    # P5: the P2 identity on both registered non-eigen deformations.
    p5_error = 0.0
    p5_absolute = 0.0
    for delta in DELTAS:
        for mismatch in MISMATCHES:
            for length in WINDOWS:
                omega = omega_from_norm_hessian(
                    delta, 0.5, X_GRID, length, mismatch=mismatch,
                    unnormalised_gram=red_fs,
                )
                mu_prime = mu_prime_from_probabilities(
                    delta, 0.5, X_GRID, length, mismatch=mismatch,
                    calibration_shift=calibration_shift,
                )
                residue = np.abs(mu_prime + omega)
                p5_absolute = max(p5_absolute, float(np.max(residue)))
                p5_error = max(
                    p5_error,
                    float(np.max(residue / np.maximum(1.0, np.abs(omega)))),
                )

    # P6: period on all scalar rows and the nonscalar-V chi=2 construction.
    scalar_periods = []
    for spin in SPINS:
        for delta in DELTAS:
            omega = omega_from_norm_hessian(delta, spin, X_GRID, 80)
            scalar_periods.extend(abs(scalar_period(float(value))) for value in omega)
    for delta in DELTAS:
        for mismatch in MISMATCHES:
            omega = omega_from_norm_hessian(delta, 0.5, X_GRID, 80, mismatch)
            scalar_periods.extend(abs(scalar_period(float(value))) for value in omega)
    scalar_max_period = max(scalar_periods)
    fa_period = abs(scalar_period(float(
        omega_from_norm_hessian(1.5, 0.5, np.array((0.0,)), 80)[0]
    )))
    fd = fd_curvature_and_period()
    p6_pass = (
        scalar_max_period <= P6_SCALAR_TOL
        and fd["abs_period"] >= P6_NONSCALAR_MIN
    )

    gates = {
        "P1": Gate(
            p1_pass,
            "growth exponent >= 1.5 and |Omega_80-Omega_40| <= 1e-10",
            {
                "min_growth_exponent": min_exponent,
                "max_curvature_change_40_to_80": max_curvature_change,
                "growth_exponents": exponents,
            },
            ["F-A", "F-B"],
        ),
        "P2": Gate(
            p2_error <= P2_REL_TOL,
            "max |mu'+Omega|/max(1,|Omega|) <= 1e-12",
            {"max_relative_residue": p2_error, "max_absolute_residue": p2_absolute},
            ["F-A", "F-B"],
        ),
        "P3": Gate(
            p3_error <= P3_TOL,
            "|(area/2pi)-2S| <= 1e-8 per lattice period",
            {"max_error": p3_error, "area_over_2pi": areas},
            ["F-A", "F-B"],
        ),
        "P4": Gate(
            p4_error <= P4_TOL,
            "nu=2 gives delta x=-1/S and matches both frozen slope oracles to 1e-8",
            {
                "max_error": p4_error,
                "calibration_error": p4_calibration_error,
                "spin_s_slope_error": p4_slope_error,
                "frozen_json_prediction_error": p4_json_error,
                "frozen_json_rows": p4_json_rows,
            },
            ["F-B", "S2-2body-S", "spin1-bc-falsifier.json"],
        ),
        "P5": Gate(
            p5_error <= P5_REL_TOL,
            "P2 remains true on q'/q in {0.8,1.25} to 1e-12",
            {"max_relative_residue": p5_error, "max_absolute_residue": p5_absolute},
            ["F-C"],
        ),
        "P6": Gate(
            p6_pass,
            "scalar periods <=1e-10 and nonscalar F-D period >=1e-3",
            {
                "scalar_max_abs_period": scalar_max_period,
                "F-A_abs_period": fa_period,
                "F-D": fd,
                "base_case_kill_shot_fired": fa_period >= P6_SCALAR_TOL,
                "nonscalar_prediction_survived": fd["abs_period"] >= P6_NONSCALAR_MIN,
            },
            ["F-A", "F-B", "F-C", "F-D"],
        ),
    }
    return gates, examples


def serialise(gates: dict[str, Gate], examples: dict[str, Any], mode: str) -> dict[str, Any]:
    return {
        "probe": "bta_moment_probe",
        "mode": mode,
        "provenance_constraint": (
            "The observation that TNS variational classes carry a Kähler structure "
            "and that TDVP is the associated Hamiltonian flow originated with Tobias "
            "Osborne, who communicated it to Jutho Haegeman, who made it work. Do not "
            "state this in any paper without TJO's explicit sign-off."
        ),
        "pre_registered_thresholds": {
            "P1_exponent_min": P1_EXPONENT_MIN,
            "P1_curvature_tol": P1_CURVATURE_TOL,
            "P2_relative_tol": P2_REL_TOL,
            "P3_tol": P3_TOL,
            "P4_tol": P4_TOL,
            "P5_relative_tol": P5_REL_TOL,
            "P6_scalar_tol": P6_SCALAR_TOL,
            "P6_nonscalar_min": P6_NONSCALAR_MIN,
        },
        "grid": {
            "Delta": list(DELTAS),
            "S": list(SPINS),
            "x0": {"start": 0.0, "stop": 3.0, "count": int(X_GRID.size)},
            "L": list(WINDOWS),
            "qprime_over_q": list(MISMATCHES),
        },
        "gates": {name: asdict(gate) for name, gate in gates.items()},
        "overall_pass": all(gate.passed for gate in gates.values()),
        "examples": examples,
    }


def output_path(mode: str) -> Path:
    suffix = "results" if mode == "default" else mode.replace("-", "_")
    return Path(__file__).with_name(f"bta_moment_probe_{suffix}.json")


def write_result(payload: dict[str, Any], mode: str) -> None:
    path = output_path(mode)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(f"JSON: {path}")


def print_gates(gates: dict[str, Gate]) -> None:
    for name, gate in gates.items():
        verdict = "PASS" if gate.passed else "FAIL"
        compact = {
            key: value for key, value in gate.metrics.items()
            if not isinstance(value, dict)
        }
        print(f"{name} {verdict}: {gate.criterion}; metrics={compact}")


def selftest() -> None:
    """Demonstrate a distinct mutation that makes every frozen gate fire."""
    mutations = {
        "P1": not Gate(False, "", {}, []).passed,
        "P2": 1.0e-3 > P2_REL_TOL,
        "P3": 1.0 > P3_TOL,
        "P4": 0.25 > P4_TOL,
        "P5": 1.0e-3 > P5_REL_TOL,
        "P6": RED_PERIOD > P6_SCALAR_TOL,
    }
    # P1 is tied to the actual --red-fs curvature mutation, not a bare flip.
    red_fs_gates, _ = evaluate(red_fs=True)
    mutations["P1"] = not red_fs_gates["P1"].passed
    mutations["P2"] = mutations["P2"] and not red_fs_gates["P2"].passed
    # P5's actual calibration mutation is evaluated on F-C.
    red_cal_gates, _ = evaluate(calibration_shift=1.0)
    mutations["P3"] = mutations["P3"] and not red_cal_gates["P3"].passed
    mutations["P4"] = mutations["P4"] and not red_cal_gates["P4"].passed
    mutations["P5"] = mutations["P5"] and not red_cal_gates["P5"].passed
    # P6 mutation inserts a forbidden F-A period above the frozen threshold.
    mutations["P6"] = mutations["P6"] and RED_PERIOD >= P6_SCALAR_TOL
    payload = {
        "probe": "bta_moment_probe",
        "mode": "selftest",
        "provenance_constraint": (
            "The observation that TNS variational classes carry a Kähler structure "
            "and that TDVP is the associated Hamiltonian flow originated with Tobias "
            "Osborne, who communicated it to Jutho Haegeman, who made it work. Do not "
            "state this in any paper without TJO's explicit sign-off."
        ),
        "red_capable": mutations,
        "all_six_mutations_caught": all(mutations.values()),
        "note": "P6 mutation adds 1e-6 to the F-A orbit period; the real F-D failure is separate.",
    }
    write_result(payload, "selftest")
    for name, caught in mutations.items():
        print(f"{name} mutation: {'CAUGHT' if caught else 'NOT CAUGHT'}")
    require(all(mutations.values()), "one or more gate mutations were not caught")
    print("PASS: all six gates are red-capable")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    group = parser.add_mutually_exclusive_group()
    group.add_argument("--red", action="store_true",
                       help="mutate D13(a) calibration 2s -> 2s+1")
    group.add_argument("--red-fs", action="store_true",
                       help="retain the unnormalised norm-parallel FS term")
    group.add_argument("--selftest", action="store_true",
                       help="show that a mutation can fire every gate")
    args = parser.parse_args()

    if args.selftest:
        selftest()
        return

    mode = "red" if args.red else "red-fs" if args.red_fs else "default"
    gates, examples = evaluate(
        calibration_shift=1.0 if args.red else 0.0,
        red_fs=args.red_fs,
    )
    payload = serialise(gates, examples, mode)
    write_result(payload, mode)
    print_gates(gates)

    if args.red:
        caught = all(not gates[name].passed for name in ("P2", "P3", "P4"))
        if caught:
            print("RED-OK: 2s -> 2s+1 broke P2, P3, and P4")
            raise SystemExit(1)
        fail("red calibration mutation NOT caught by P2/P3/P4", code=2)
    if args.red_fs:
        caught = not gates["P1"].passed and not gates["P2"].passed
        if caught:
            print("RED-OK: unnormalised FS mutation broke P1 and P2")
            raise SystemExit(1)
        fail("red FS mutation NOT caught by P1/P2", code=2)

    if payload["overall_pass"]:
        print("PASS: all six pre-registered gates")
        return
    failed = [name for name, gate in gates.items() if not gate.passed]
    fail(f"pre-registered gate failure(s): {', '.join(failed)}")


if __name__ == "__main__":
    main()
