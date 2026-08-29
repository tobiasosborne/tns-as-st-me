#!/usr/bin/env python3
"""Finite ED certificate for theory/soft-index-g2.md.

Green:
    python3 -O theory/checks/soft_index_g2_check.py

Structural red (must exit 1):
    python3 -O theory/checks/soft_index_g2_check.py --red-scalar-gram

The red mutation replaces the non-scalar SU(3) multiplicity Gram operator by
its scalar mean.  This is exactly the substitution excluded by G2.FULL.
"""

from __future__ import annotations

import ast
import importlib.util
import itertools
import math
from pathlib import Path
import sys

import numpy as np


ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
TOL = 2.0e-10
RED_MODES = {"--red-scalar-gram"}


def fail(message: str) -> None:
    print(f"FAIL: {message}", file=sys.stderr)
    raise SystemExit(1)


def require(condition: bool, message: str) -> None:
    if not condition:
        fail(message)


def code_shape_gate() -> None:
    source = Path(__file__).read_text(encoding="utf-8")
    tree = ast.parse(source)
    bare = [node for node in ast.walk(tree) if isinstance(node, ast.Assert)]
    require(not bare, "G2-C0 bare assert found")
    print("G2-C0 PASS: optimization-safe require/fail checks; no bare assert")


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    require(spec is not None and spec.loader is not None,
            f"cannot load reference checker {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def matrix_unit(row: int, column: int, dimension: int) -> np.ndarray:
    result = np.zeros((dimension, dimension), dtype=complex)
    result[row, column] = 1.0
    return result


def kron_at(operator: np.ndarray, site: int, number_sites: int,
            local_dimension: int) -> np.ndarray:
    result = np.array([[1.0 + 0.0j]])
    for position in range(number_sites):
        factor = operator if position == site else np.eye(local_dimension)
        result = np.kron(result, factor)
    return result


def total_operator(operator: np.ndarray, number_sites: int,
                   local_dimension: int) -> np.ndarray:
    dimension = local_dimension ** number_sites
    return sum(
        (kron_at(operator, site, number_sites, local_dimension)
         for site in range(number_sites)),
        start=np.zeros((dimension, dimension), dtype=complex),
    )


def swap_operator(first: int, second: int, number_sites: int,
                  local_dimension: int) -> np.ndarray:
    dimension = local_dimension ** number_sites
    result = np.zeros((dimension, dimension), dtype=complex)
    shape = (local_dimension,) * number_sites
    for state in itertools.product(range(local_dimension), repeat=number_sites):
        source = np.ravel_multi_index(state, shape)
        target_state = list(state)
        target_state[first], target_state[second] = (
            target_state[second], target_state[first]
        )
        target = np.ravel_multi_index(tuple(target_state), shape)
        result[target, source] = 1.0
    return result


def su3_ring() -> dict[str, object]:
    number_sites = 3
    local_dimension = 3
    dimension = local_dimension ** number_sites
    identity = np.eye(dimension, dtype=complex)
    e21 = matrix_unit(1, 0, local_dimension)
    soft = e21 + 2.0 * matrix_unit(2, 1, local_dimension)
    soft_adjoint = soft.conj().T
    bracket = soft_adjoint @ soft - soft @ soft_adjoint
    character_generator = np.diag((1.0, 0.0, -1.0)).astype(complex)
    charge_soft = total_operator(soft, number_sites, local_dimension)
    charge_adjoint = charge_soft.conj().T
    current_soft = np.zeros((dimension, dimension), dtype=complex)
    current_bracket = np.zeros_like(current_soft)
    hamiltonian = np.zeros_like(current_soft)
    for site in range(number_sites):
        neighbour = (site + 1) % number_sites
        bond = 0.5 * (
            identity
            - swap_operator(site, neighbour, number_sites, local_dimension)
        )
        hamiltonian += bond
        local_soft = kron_at(soft, site, number_sites, local_dimension)
        local_bracket = kron_at(
            bracket, site, number_sites, local_dimension
        )
        current_soft -= bond @ local_soft - local_soft @ bond
        current_bracket -= bond @ local_bracket - local_bracket @ bond

    local_weights = np.diag(character_generator).real
    total_weights = []
    for state in itertools.product(range(local_dimension), repeat=number_sites):
        total_weights.append(sum(local_weights[color] for color in state))
    source_indices = np.where(np.isclose(total_weights, 2.0))[0]
    target_indices = np.where(np.isclose(total_weights, 1.0))[0]

    vacuum = np.zeros(dimension, dtype=complex)
    vacuum[0] = 1.0
    momentum = 2.0 * math.pi / 3.0
    hard = sum(
        (np.exp(1.0j * momentum * site)
         * kron_at(e21, site, number_sites, local_dimension) @ vacuum
         for site in range(number_sites)),
        start=np.zeros(dimension, dtype=complex),
    ) / math.sqrt(number_sites)
    return {
        "N": number_sites,
        "soft": soft,
        "bracket": bracket,
        "Qb": charge_soft,
        "Qbd": charge_adjoint,
        "Jb": current_soft,
        "Jh": current_bracket,
        "H": hamiltonian,
        "source": source_indices,
        "target": target_indices,
        "hard": hard,
        "momentum": momentum,
    }


def su3_intertwiner_gate(red_scalar_gram: bool) -> None:
    data = su3_ring()
    source = data["source"]
    target = data["target"]
    hard = data["hard"]
    descendant = data["Qb"][np.ix_(target, source)]
    gram = descendant.conj().T @ descendant
    spectrum = np.linalg.eigvalsh(gram)
    current_vector = (data["Jb"] @ hard)[target]
    ward_vector = (data["Jh"] @ hard)[source]
    hard_source = hard[source]

    covariance_error = float(np.linalg.norm(
        data["Qbd"] @ data["Jb"]
        - data["Jb"] @ data["Qbd"] - data["Jh"]
    ))
    polarization_error = float(np.linalg.norm(data["Qbd"] @ hard))
    projection = descendant @ np.linalg.solve(
        gram, descendant.conj().T
    )
    projected_current = projection @ current_vector
    if red_scalar_gram:
        scalar = float(np.trace(gram).real / gram.shape[0])
        intrinsic = descendant @ (ward_vector / scalar)
    else:
        intrinsic = descendant @ np.linalg.solve(gram, ward_vector)
    projection_error = float(np.linalg.norm(projected_current - intrinsic))

    created = descendant @ hard_source
    residue = np.vdot(created, projected_current)
    ward_residue = np.vdot(hard_source, ward_vector)
    index_value = residue / ward_residue
    complement = float(np.linalg.norm(current_vector - projected_current))
    scalar_mean = float(np.trace(gram).real / gram.shape[0])
    scalar_mutant = descendant @ (ward_vector / scalar_mean)
    scalar_defect = float(np.linalg.norm(projected_current - scalar_mutant))
    double_bracket = data["bracket"] @ data["soft"] - (
        data["soft"] @ data["bracket"]
    )
    best_multiple = np.vdot(data["soft"], double_bracket) / np.vdot(
        data["soft"], data["soft"]
    )
    non_sl2_residual = float(np.linalg.norm(
        double_bracket - best_multiple * data["soft"]
    ))

    require(len(source) == 3 and len(target) == 6,
            f"G2-C1 wrong SU(3) isotype dimensions {len(source)}->{len(target)}")
    require(float(np.min(spectrum)) > 1.0,
            f"G2-C1 soft map is not injective: spectrum {spectrum}")
    require(float(np.max(spectrum) - np.min(spectrum)) > 2.0,
            f"G2-C1 multiplicity Gram unexpectedly scalar: {spectrum}")
    require(non_sl2_residual > 1.0,
            "G2-C1 chosen SU(3) soft line accidentally closes an sl2 triple")
    require(np.linalg.norm(spectrum - np.asarray((5.0, 5.0, 8.0))) < TOL,
            f"G2-C1 Gram spectrum {spectrum} != (5,5,8)")
    require(covariance_error < TOL,
            f"G2-C1 SU(3) Ward covariance error {covariance_error:.3e}")
    require(polarization_error < TOL,
            f"G2-C1 hard vector is not polarized: {polarization_error:.3e}")
    require(projection_error < TOL,
            f"G2-C1 projected intertwiner error {projection_error:.3e}")
    require(abs(index_value - 1.0) < TOL,
            f"G2-C1 normalized finite index {index_value} != 1")
    require(abs(ward_residue + 1.0j * math.sqrt(3.0)) < TOL,
            f"G2-C1 SU(3) Ward residue {ward_residue} is wrong")
    require(complement > 1.0,
            f"G2-C1 projection is structurally trivial: complement {complement}")
    require(abs(scalar_defect - 1.0 / math.sqrt(60.0)) < TOL,
            f"G2-C1 scalar-Gram defect {scalar_defect:.12f} is wrong")
    print(
        "G2-C1 PASS: SU(3) fundamental N=3; "
        f"spec(A)={spectrum.tolist()} covariance={covariance_error:.1e} "
        f"projection={projection_error:.2e} index={index_value:.12g} "
        f"orthogonal={complement:.12f} scalar-defect={scalar_defect:.12f} "
        f"non-sl2={non_sl2_residual:.12f}"
    )


def su2_reduction_gate() -> None:
    reference = load_module(
        "soft_index_r2_reference", HERE / "soft_index_r2_check.py"
    )
    maxima = {"projection": 0.0, "polarization": 0.0,
              "norm": 0.0, "velocity": 0.0, "residue": 0.0}
    measured_rows = []
    for two_s in (1, 2, 3):
        data = reference.spin_ring(two_s)
        number_sites = int(data["N"])
        site_spin = float(data["S"])
        momentum = math.pi / 2.0
        hard = reference.one_magnon(data, momentum)
        source = reference.sector_indices(data, 1)
        target = reference.sector_indices(data, 2)
        descendant = data["Sm"][np.ix_(target, source)]
        gram = descendant.conj().T @ descendant
        projection = descendant @ np.linalg.solve(
            gram, descendant.conj().T
        )
        current_vector = (data["Jm"] @ hard)[target]
        ward_vector = (2.0 * data["Jz"] @ hard)[source]
        projected = projection @ current_vector
        intrinsic = descendant @ np.linalg.solve(gram, ward_vector)
        created = descendant @ hard[source]
        measured_norm = float(np.vdot(created, created).real)
        measured_velocity = np.vdot(hard, data["Jz"] @ hard) / 1.0j
        measured_residue = np.vdot(created, projected)
        expected_velocity = 2.0 * site_spin * math.sin(momentum)
        expected_norm = 2.0 * (number_sites * site_spin - 1.0)
        expected_residue = 2.0j * expected_velocity

        maxima["projection"] = max(
            maxima["projection"], float(np.linalg.norm(projected - intrinsic))
        )
        maxima["polarization"] = max(
            maxima["polarization"], float(np.linalg.norm(data["Sp"] @ hard))
        )
        maxima["norm"] = max(
            maxima["norm"], abs(measured_norm - expected_norm)
        )
        maxima["velocity"] = max(
            maxima["velocity"], abs(measured_velocity - expected_velocity)
        )
        maxima["residue"] = max(
            maxima["residue"], abs(measured_residue - expected_residue)
        )
        measured_rows.append((measured_norm, measured_velocity.real,
                              measured_residue))

    for name, error in maxima.items():
        require(error < TOL, f"G2-C2 SU(2) {name} error {error:.3e}")
    certified = ((2.0, 1.0, 2.0j), (6.0, 2.0, 4.0j),
                 (10.0, 3.0, 6.0j))
    for measured, expected in zip(measured_rows, certified):
        require(max(abs(a - b) for a, b in zip(measured, expected)) < TOL,
                f"G2-C2 certified row mismatch {measured} != {expected}")
    print(
        "G2-C2 PASS: SU(2) reduction reproduces soft_index_r2_check.py "
        f"rows {measured_rows}; maxima "
        + " ".join(f"{key}={value:.2e}" for key, value in maxima.items())
    )


def main() -> None:
    arguments = sys.argv[1:]
    require(len(arguments) <= 1, "red modes are mutually exclusive")
    mode = arguments[0] if arguments else None
    require(mode is None or mode in RED_MODES, f"unknown mode: {mode}")
    code_shape_gate()
    if mode == "--red-scalar-gram":
        su3_intertwiner_gate(True)
        print("RED SURVIVED UNDETECTED: --red-scalar-gram")
        raise SystemExit(0)
    su3_intertwiner_gate(False)
    su2_reduction_gate()
    print("ALL SOFT-INDEX-G2 GATES PASS")


if __name__ == "__main__":
    main()
