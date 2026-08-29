#!/usr/bin/env python3
"""Red-capable ED certificate for theory/soft-index-g4.md.

Green:
    python3 -O theory/checks/soft_index_g4_check.py

Registered red modes:
    --red-shift                mutate the SU(3) central character -1 -> -2
    --red-projector-collapse   identify the central block with ran(Q_X)

The non-SU(2) instance is the four-site fundamental SU(3) permutation
ferromagnet.  G4-C4 imports the exact finite-ring helpers from
soft_index_r2_check.py and reproduces its SIDXR2-C2 norm/residue numbers.
"""

from __future__ import annotations

import ast
import importlib.util
from itertools import product
import math
from pathlib import Path
import sys

import numpy as np


HERE = Path(__file__).resolve().parent
TOL = 3.0e-10
RED_MODES = {"--red-shift", "--red-projector-collapse"}


def fail(message: str) -> None:
    print(f"FAIL: {message}", file=sys.stderr)
    raise SystemExit(1)


def require(condition: bool, message: str) -> None:
    if not condition:
        fail(message)


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    require(spec is not None and spec.loader is not None,
            f"cannot load module {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def code_shape_gate() -> None:
    source = Path(__file__).read_text(encoding="utf-8")
    tree = ast.parse(source)
    bare = [node for node in ast.walk(tree) if isinstance(node, ast.Assert)]
    require(not bare, "G4-C0 bare assert found")
    print("G4-C0 PASS: optimization-safe require/fail checks; no bare assert")


def kron_at(operator: np.ndarray, site: int, number_sites: int) -> np.ndarray:
    local_dimension = operator.shape[0]
    result = np.array([[1.0 + 0.0j]])
    for position in range(number_sites):
        factor = operator if position == site else np.eye(local_dimension)
        result = np.kron(result, factor)
    return result


def swap_matrix(site: int, neighbour: int, number_sites: int,
                local_dimension: int) -> np.ndarray:
    dimension = local_dimension ** number_sites
    swap = np.zeros((dimension, dimension), dtype=complex)
    shape = (local_dimension,) * number_sites
    for configuration in product(range(local_dimension), repeat=number_sites):
        output = list(configuration)
        output[site], output[neighbour] = output[neighbour], output[site]
        column = np.ravel_multi_index(configuration, shape)
        row = np.ravel_multi_index(tuple(output), shape)
        swap[row, column] = 1.0
    return swap


def su3_ring(number_sites: int = 4) -> dict[str, object]:
    local_dimension = 3
    dimension = local_dimension ** number_sites
    identity = np.eye(dimension, dtype=complex)
    central = np.diag((2.0 / 3.0, -1.0 / 3.0, -1.0 / 3.0)).astype(complex)
    x_component = np.zeros((local_dimension, local_dimension), dtype=complex)
    x_component[1, 0] = 1.0
    hard_component = np.zeros_like(x_component)
    hard_component[2, 0] = 1.0
    central_total = sum(
        kron_at(central, site, number_sites) for site in range(number_sites)
    )
    x_sites = [
        kron_at(x_component, site, number_sites)
        for site in range(number_sites)
    ]
    hard_sites = [
        kron_at(hard_component, site, number_sites)
        for site in range(number_sites)
    ]
    charge = sum(x_sites)
    hamiltonian = np.zeros((dimension, dimension), dtype=complex)
    current = np.zeros_like(hamiltonian)
    for site in range(number_sites):
        neighbour = (site + 1) % number_sites
        bond = identity - swap_matrix(
            site, neighbour, number_sites, local_dimension
        )
        hamiltonian += bond
        current -= bond @ x_sites[site] - x_sites[site] @ bond
    vacuum = np.zeros(dimension, dtype=complex)
    vacuum[0] = 1.0
    return {
        "N": number_sites,
        "C_site": central,
        "C": central_total,
        "Q": charge,
        "J": current,
        "H": hamiltonian,
        "hard_sites": hard_sites,
        "vac": vacuum,
    }


def su3_hard(data: dict[str, object], momentum: float) -> np.ndarray:
    number_sites = int(data["N"])
    return sum(
        np.exp(1.0j * momentum * site)
        * (data["hard_sites"][site] @ data["vac"])
        for site in range(number_sites)
    ) / math.sqrt(number_sites)


def su3_covariance_gate(data: dict[str, object], red_shift: bool) -> None:
    central_site = data["C_site"]
    scalar_period = np.diag(np.exp(2.0j * math.pi * np.diag(central_site)))
    scalar = np.exp(-2.0j * math.pi / 3.0) * np.eye(3)
    scalar_error = float(np.linalg.norm(scalar_period - scalar))
    invariance_error = float(np.linalg.norm(
        data["H"] @ data["Q"] - data["Q"] @ data["H"]
    ))
    expected_shift = -2.0 if red_shift else -1.0
    q_character_error = float(np.linalg.norm(
        data["C"] @ data["Q"] - data["Q"] @ data["C"]
        - expected_shift * data["Q"]
    ))
    j_character_error = float(np.linalg.norm(
        data["C"] @ data["J"] - data["J"] @ data["C"]
        - expected_shift * data["J"]
    ))
    eigenvalues = np.linalg.eigvalsh(data["C"])
    offset = 2.0 / 3.0
    coset_error = float(np.max(np.abs(
        np.mod(eigenvalues - offset + 0.5, 1.0) - 0.5
    )))
    require(scalar_error < TOL,
            f"G4-C1 scalar-period error {scalar_error:.3e}")
    require(invariance_error < TOL,
            f"G4-C1 [H,Q_X] error {invariance_error:.3e}")
    require(coset_error < TOL,
            f"G4-C1 affine-coset error {coset_error:.3e}")
    require(q_character_error < TOL,
            f"G4-C1 Q_X character error {q_character_error:.3e}")
    require(j_character_error < TOL,
            f"G4-C1 J_X character error {j_character_error:.3e}")
    print(
        "G4-C1 PASS: SU(3) scalar/coset/covariance "
        f"errors=({scalar_error:.2e},{coset_error:.2e},"
        f"{q_character_error:.2e},{j_character_error:.2e}); [H,Q]={invariance_error:.2e}"
    )


def su3_sector_gate(data: dict[str, object]) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    hard = su3_hard(data, math.pi / 2.0)
    charge_created = data["Q"] @ hard
    current_created = data["J"] @ hard
    dimension = hard.size
    identity = np.eye(dimension)
    source_label = 5.0 / 3.0
    target_label = 2.0 / 3.0
    source_error = float(np.linalg.norm(
        (data["C"] - source_label * identity) @ hard
    ))
    charge_target_error = float(np.linalg.norm(
        (data["C"] - target_label * identity) @ charge_created
    ))
    current_target_error = float(np.linalg.norm(
        (data["C"] - target_label * identity) @ current_created
    ))
    require(abs((target_label - source_label) + 1.0) < TOL,
            "G4-C2 label difference is not -1")
    require(source_error < TOL,
            f"G4-C2 hard-sector error {source_error:.3e}")
    require(charge_target_error < TOL,
            f"G4-C2 charge-created target error {charge_target_error:.3e}")
    require(current_target_error < TOL,
            f"G4-C2 current-created target error {current_target_error:.3e}")
    print(
        "G4-C2 PASS: SU(3) labels 5/3 -> 2/3, shift=-1; "
        f"residuals=({source_error:.2e},{charge_target_error:.2e},"
        f"{current_target_error:.2e})"
    )
    return hard, charge_created, current_created


def su3_split_gate(data: dict[str, object], hard: np.ndarray,
                   charge_created: np.ndarray, current_created: np.ndarray,
                   red_collapse: bool) -> None:
    hard_energy = 2.0
    energy_error = float(np.linalg.norm(data["H"] @ hard - hard_energy * hard))
    time = 0.73
    eigenvalues, eigenvectors = np.linalg.eigh(data["H"])
    interacting = eigenvectors @ (
        np.exp(-1.0j * eigenvalues * time)
        * (eigenvectors.conj().T @ charge_created)
    )
    free = np.exp(-1.0j * hard_energy * time) * charge_created
    anchor = np.vdot(free, interacting) / np.vdot(free, free)

    diagonal = np.diag(data["C"]).real
    source_indices = np.where(np.isclose(diagonal, 5.0 / 3.0, atol=TOL))[0]
    target_indices = np.where(np.isclose(diagonal, 2.0 / 3.0, atol=TOL))[0]
    descendant_map = data["Q"][np.ix_(target_indices, source_indices)]
    rank = int(np.linalg.matrix_rank(descendant_map, tol=TOL))
    if red_collapse:
        require(rank == target_indices.size,
                "G4-C3 RED detected: central target block is larger than ran(Q_X)")
    else:
        require(rank < target_indices.size,
                "G4-C3 target block unexpectedly equals ran(Q_X)")
    range_projector = descendant_map @ np.linalg.pinv(descendant_map, rcond=TOL)
    target_current = current_created[target_indices]
    inside = range_projector @ target_current
    outside = (np.eye(target_indices.size) - range_projector) @ target_current
    inside_norm = float(np.linalg.norm(inside))
    outside_norm = float(np.linalg.norm(outside))
    coefficient_error = float(np.linalg.norm(
        inside - (2.0j / 3.0) * charge_created[target_indices]
    ))
    residue = np.vdot(charge_created[target_indices], inside)

    require(energy_error < TOL,
            f"G4-C3 hard-energy error {energy_error:.3e}")
    require(abs(anchor - 1.0) < TOL,
            f"G4-C3 zero-mode anchor {anchor} is not one")
    require(source_indices.size == 8 and target_indices.size == 24 and rank == 8,
            "G4-C3 unexpected SU(3) sector/range dimensions "
            f"({source_indices.size},{target_indices.size},{rank})")
    require(abs(inside_norm - math.sqrt(4.0 / 3.0)) < TOL,
            f"G4-C3 inside-current norm {inside_norm:.12f}")
    require(abs(outside_norm - math.sqrt(8.0 / 3.0)) < TOL,
            f"G4-C3 outside-current norm {outside_norm:.12f}")
    require(coefficient_error < TOL,
            f"G4-C3 diagnostic projected coefficient error {coefficient_error:.3e}")
    require(abs(residue - 2.0j) < TOL,
            f"G4-C3 diagnostic residue {residue}")
    print(
        "G4-C3 PASS: E=2 anchor=1; dims=(8,24), rank(Q)=8; "
        f"||P_D J||={inside_norm:.12f}, ||(Pi-P_D)J||={outside_norm:.12f}, "
        f"projected-coefficient error={coefficient_error:.2e}"
    )


def su2_reduction_gate() -> None:
    r2 = load_module("soft_index_r2_for_g4", HERE / "soft_index_r2_check.py")
    momentum = math.pi / 2.0
    maximum_label_error = 0.0
    maximum_norm_error = 0.0
    maximum_residue_error = 0.0
    measured_rows: list[tuple[float, float, float, float]] = []
    for two_s in (1, 2, 3):
        data = r2.spin_ring(two_s)
        number_sites = int(data["N"])
        site_spin = float(data["S"])
        hard = r2.one_magnon(data, momentum)
        source_label = number_sites * site_spin - 1.0
        descendant = data["Sm"] @ hard
        current_created = data["Jm"] @ hard
        maximum_label_error = max(
            maximum_label_error,
            float(np.linalg.norm((data["Sz"] - source_label * np.eye(hard.size)) @ hard)),
            float(np.linalg.norm(
                (data["Sz"] - (source_label - 1.0) * np.eye(hard.size))
                @ descendant
            )),
            float(np.linalg.norm(
                (data["Sz"] - (source_label - 1.0) * np.eye(hard.size))
                @ current_created
            )),
        )
        source_indices = r2.sector_indices(data, 1)
        target_indices = r2.sector_indices(data, 2)
        descendant_map = data["Sm"][np.ix_(target_indices, source_indices)]
        gram = descendant_map.conj().T @ descendant_map
        range_projector = descendant_map @ np.linalg.solve(
            gram, descendant_map.conj().T
        )
        projected_current = range_projector @ current_created[target_indices]
        target_descendant = descendant[target_indices]
        measured_norm = float(np.vdot(target_descendant, target_descendant).real)
        expected_norm = 2.0 * source_label
        residue = np.vdot(target_descendant, projected_current)
        velocity = 2.0 * site_spin * math.sin(momentum)
        expected_residue = 2.0j * velocity
        maximum_norm_error = max(maximum_norm_error, abs(measured_norm - expected_norm))
        maximum_residue_error = max(
            maximum_residue_error, abs(residue - expected_residue)
        )
        measured_rows.append(
            (site_spin, source_label, measured_norm, float((-1.0j * residue).real))
        )
    require(maximum_label_error < TOL,
            f"G4-C4 SU(2) label-shift error {maximum_label_error:.3e}")
    require(maximum_norm_error < TOL,
            f"G4-C4 SIDXR2-C2 norm mismatch {maximum_norm_error:.3e}")
    require(maximum_residue_error < TOL,
            f"G4-C4 SIDXR2-C2 residue mismatch {maximum_residue_error:.3e}")
    expected_rows = [(0.5, 1.0, 2.0, 2.0),
                     (1.0, 3.0, 6.0, 4.0),
                     (1.5, 5.0, 10.0, 6.0)]
    row_error = max(
        abs(measured - expected)
        for row, expected_row in zip(measured_rows, expected_rows)
        for measured, expected in zip(row, expected_row)
    )
    require(row_error < TOL,
            f"G4-C4 unexpected SU(2) rows {measured_rows}")
    print(
        "G4-C4 PASS: soft_index_r2_check.py SIDXR2-C2 rows "
        f"{measured_rows}; label/norm/residue errors="
        f"({maximum_label_error:.2e},{maximum_norm_error:.2e},"
        f"{maximum_residue_error:.2e})"
    )


def main() -> None:
    arguments = sys.argv[1:]
    require(len(arguments) <= 1, "red modes are mutually exclusive")
    mode = arguments[0] if arguments else None
    require(mode is None or mode in RED_MODES, f"unknown mode: {mode}")
    code_shape_gate()
    data = su3_ring()
    su3_covariance_gate(data, mode == "--red-shift")
    hard, charge_created, current_created = su3_sector_gate(data)
    su3_split_gate(
        data, hard, charge_created, current_created,
        mode == "--red-projector-collapse",
    )
    su2_reduction_gate()
    if mode is not None:
        print(f"RED SURVIVED UNDETECTED: {mode}")
        raise SystemExit(0)
    print("ALL G4 GATES PASS")


if __name__ == "__main__":
    main()
