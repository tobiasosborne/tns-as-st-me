#!/usr/bin/env python3
"""Red-capable 2D ED certificate for theory/soft-index-2d.md.

Green:
    python3 -O theory/checks/soft_index_2d_check.py

Structural red mode (must exit 1):
    --red-scalar-full   replace the full-sector A^{-1} by 1/lambda

Instances:
  * spin-1/2 SU(2) permutation Heisenberg model on a 2x3 periodic lattice;
  * fundamental SU(3) permutation Heisenberg model on a 2x2 square cycle.

There are no bare asserts, so all gates remain active under python3 -O.
"""

from __future__ import annotations

import ast
from itertools import product
import math
from pathlib import Path
import sys

import numpy as np


TOL = 3.0e-10
RED_MODES = {"--red-scalar-full"}


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
    require(not bare, "SIDX2D-C0 bare assert found")
    print("SIDX2D-C0 PASS: optimization-safe require/fail checks; no bare assert")


def kron_at(operator: np.ndarray, site: int, number_sites: int,
            local_dimension: int) -> np.ndarray:
    result = np.array([[1.0 + 0.0j]])
    for position in range(number_sites):
        factor = operator if position == site else np.eye(local_dimension)
        result = np.kron(result, factor)
    return result


def global_sum(operator: np.ndarray, number_sites: int) -> np.ndarray:
    return sum(
        kron_at(operator, site, number_sites, operator.shape[0])
        for site in range(number_sites)
    )


def swap_operator(site: int, neighbour: int, number_sites: int,
                  local_dimension: int) -> np.ndarray:
    dimension = local_dimension ** number_sites
    shape = (local_dimension,) * number_sites
    swap = np.zeros((dimension, dimension), dtype=complex)
    for configuration in product(range(local_dimension), repeat=number_sites):
        output = list(configuration)
        output[site], output[neighbour] = output[neighbour], output[site]
        column = np.ravel_multi_index(configuration, shape)
        row = np.ravel_multi_index(tuple(output), shape)
        swap[row, column] = 1.0
    return swap


def make_model(local_dimension: int, number_sites: int,
               hamiltonian_edges: list[tuple[int, int]],
               flux_edges: list[tuple[int, int]], name: str) -> dict[str, object]:
    dimension = local_dimension ** number_sites
    identity = np.eye(dimension, dtype=complex)
    swaps: dict[tuple[int, int], np.ndarray] = {}

    def bond(first: int, second: int) -> np.ndarray:
        key = tuple(sorted((first, second)))
        if key not in swaps:
            swaps[key] = swap_operator(
                key[0], key[1], number_sites, local_dimension
            )
        return identity - swaps[key]

    hamiltonian = sum(
        (bond(first, second) for first, second in hamiltonian_edges),
        np.zeros((dimension, dimension), dtype=complex),
    )
    return {
        "name": name,
        "d": local_dimension,
        "N": number_sites,
        "dimension": dimension,
        "Hamil": hamiltonian,
        "flux_edges": flux_edges,
        "bond": bond,
    }


def su2_torus() -> tuple[dict[str, object], list[tuple[int, int]]]:
    length_x, length_y = 3, 2

    def site(x_coordinate: int, y_coordinate: int) -> int:
        return (x_coordinate % length_x) + length_x * (y_coordinate % length_y)

    hamiltonian_edges: list[tuple[int, int]] = []
    horizontal_edges: list[tuple[int, int]] = []
    phase_sites: list[tuple[int, int]] = []
    for y_coordinate in range(length_y):
        for x_coordinate in range(length_x):
            vertex = site(x_coordinate, y_coordinate)
            horizontal = (vertex, site(x_coordinate + 1, y_coordinate))
            vertical = (vertex, site(x_coordinate, y_coordinate + 1))
            hamiltonian_edges.extend((horizontal, vertical))
            horizontal_edges.append(horizontal)
            phase_sites.append((vertex, x_coordinate))
    model = make_model(
        2, length_x * length_y, hamiltonian_edges, horizontal_edges,
        "SU(2) spin-1/2 2x3 periodic Heisenberg",
    )
    return model, phase_sites


def su3_square() -> tuple[dict[str, object], list[tuple[int, int]]]:
    # Coordinate ordering is (0,0),(1,0),(0,1),(1,1).  The displayed
    # circulation 0->1->3->2->0 is the oriented plaquette current zero mode.
    cycle = [0, 1, 3, 2]
    edges = list(zip(cycle, cycle[1:] + cycle[:1]))
    model = make_model(
        3, 4, edges, edges,
        "SU(3) fundamental 2x2 square permutation Heisenberg",
    )
    return model, list(zip(cycle, range(4)))


def root_generators(local_dimension: int) -> tuple[np.ndarray, ...]:
    raising = np.zeros((local_dimension, local_dimension), dtype=complex)
    raising[0, 1] = 1.0
    lowering = raising.T.conj()
    coroot = np.zeros_like(raising)
    coroot[0, 0] = 1.0
    coroot[1, 1] = -1.0
    return raising, lowering, coroot


def current_zero_mode(model: dict[str, object],
                      local_generator: np.ndarray) -> np.ndarray:
    number_sites = int(model["N"])
    local_dimension = int(model["d"])
    current = np.zeros_like(model["Hamil"])
    for tail, head in model["flux_edges"]:
        interaction = model["bond"](tail, head)
        charge = kron_at(local_generator, tail, number_sites, local_dimension)
        current -= interaction @ charge - charge @ interaction
    return current


def highest_weight_basis(raising: np.ndarray,
                         source_indices: np.ndarray) -> np.ndarray:
    _left, singular_values, right = np.linalg.svd(
        raising[:, source_indices], full_matrices=True
    )
    rank = int(np.sum(singular_values > 1.0e-10))
    return right[rank:].conj().T


def root_certificate(model: dict[str, object], weight: int) -> dict[str, object]:
    number_sites = int(model["N"])
    local_dimension = int(model["d"])
    local_e, local_f, local_h = root_generators(local_dimension)
    raising = global_sum(local_e, number_sites)
    lowering = global_sum(local_f, number_sites)
    coroot = global_sum(local_h, number_sites)
    current_e = current_zero_mode(model, local_e)
    current_f = current_zero_mode(model, local_f)
    current_h = current_zero_mode(model, local_h)

    weights = np.rint(np.diag(coroot).real).astype(int)
    source = np.where(weights == weight)[0]
    target = np.where(weights == weight - 2)[0]
    descendant = lowering[np.ix_(target, source)]
    gram = descendant.conj().T @ descendant
    projector = descendant @ np.linalg.solve(gram, descendant.conj().T)
    highest = highest_weight_basis(raising, source)
    current_f_block = current_f[np.ix_(target, source)]
    current_h_block = current_h[np.ix_(source, source)]

    h_on_highest = current_h_block @ highest
    full_lhs = projector @ current_f_block @ highest
    full_rhs = descendant @ np.linalg.solve(gram, h_on_highest)
    scalar_full_rhs = descendant @ h_on_highest / weight

    restricted_map = descendant @ highest
    restricted_gram = restricted_map.conj().T @ restricted_map
    restricted_projector = restricted_map @ np.linalg.solve(
        restricted_gram, restricted_map.conj().T
    )
    restricted_lhs = restricted_projector @ current_f_block @ highest
    projected_h = highest @ (highest.conj().T @ h_on_highest)
    restricted_rhs = descendant @ projected_h / weight

    return {
        "weight": weight,
        "source": source,
        "target": target,
        "highest": highest,
        "D": descendant,
        "A": gram,
        "P": projector,
        "raising": raising,
        "lowering": lowering,
        "coroot": coroot,
        "current_f": current_f,
        "current_h": current_h,
        "restricted_gram": restricted_gram,
        "covariance_error": max(
            float(np.linalg.norm(raising @ current_f - current_f @ raising
                                 - current_h)),
            float(np.linalg.norm(coroot @ current_f - current_f @ coroot
                                 + 2.0 * current_f)),
            float(np.linalg.norm(coroot @ current_h - current_h @ coroot)),
            float(np.linalg.norm(model["Hamil"] @ raising
                                 - raising @ model["Hamil"])),
        ),
        "full_error": float(np.linalg.norm(full_lhs - full_rhs)),
        "scalar_full_defect": float(np.linalg.norm(
            full_lhs - scalar_full_rhs
        )),
        "restricted_error": float(np.linalg.norm(
            restricted_lhs - restricted_rhs
        )),
    }


def spectrum_counts(matrix: np.ndarray) -> dict[int, int]:
    rounded = np.rint(np.linalg.eigvalsh(matrix)).astype(int)
    return {value: int(np.sum(rounded == value)) for value in sorted(set(rounded))}


def ed_and_covariance_gate(models: list[dict[str, object]],
                           certificates: list[dict[str, object]]) -> None:
    ground_dimensions = []
    for model, expected_ground in zip(models, (7, 15)):
        energies = np.linalg.eigvalsh(model["Hamil"])
        ground_dimension = int(np.sum(np.abs(energies) < TOL))
        hermiticity_error = float(np.linalg.norm(
            model["Hamil"] - model["Hamil"].conj().T
        ))
        require(hermiticity_error < TOL,
                f"SIDX2D-C1 {model['name']} Hamiltonian is not Hermitian")
        require(ground_dimension == expected_ground,
                f"SIDX2D-C1 {model['name']} ground dimension "
                f"{ground_dimension} != {expected_ground}")
        ground_dimensions.append(ground_dimension)
    maximum_covariance = max(float(c["covariance_error"]) for c in certificates)
    require(maximum_covariance < TOL,
            f"SIDX2D-C1 covariance/invariance error {maximum_covariance:.3e}")
    print("SIDX2D-C1 PASS: ED ground multiplets SU(2)=7, SU(3)=15; "
          f"max covariance/invariance error={maximum_covariance:.2e}")


def register_gate(su2: dict[str, object], su3_one: dict[str, object],
                  su3_two: dict[str, object], red_scalar: bool) -> None:
    expected = (
        (su2, 6, 5, {4: 5, 10: 1}),
        (su3_one, 16, 12, {1: 12, 4: 4}),
        (su3_two, 10, 9, {2: 9, 6: 1}),
    )
    for certificate, source_dimension, highest_dimension, gram_spectrum in expected:
        measured = spectrum_counts(certificate["A"])
        restricted_error = float(np.linalg.norm(
            certificate["restricted_gram"]
            - certificate["weight"] * np.eye(highest_dimension)
        ))
        require(len(certificate["source"]) == source_dimension,
                "SIDX2D-C2 wrong source-sector dimension")
        require(certificate["highest"].shape[1] == highest_dimension,
                "SIDX2D-C2 wrong highest-sector dimension")
        require(measured == gram_spectrum,
                f"SIDX2D-C2 Gram spectrum {measured} != {gram_spectrum}")
        require(restricted_error < TOL,
                f"SIDX2D-C2 restricted Gram error {restricted_error:.3e}")

    maximum_full = max(float(c["full_error"]) for c in expected_certificates(expected))
    maximum_restricted = max(
        float(c["restricted_error"]) for c in expected_certificates(expected)
    )
    scalar_defect = float(su3_one["scalar_full_defect"])
    require(abs(scalar_defect - math.sqrt(40.0)) < TOL,
            f"SIDX2D-C2 structural scalar defect {scalar_defect:.12f}")
    if red_scalar:
        require(scalar_defect < TOL,
                "SIDX2D-C2 RED detected: scalar 1/lambda cannot replace "
                "the full-sector Gram inverse")
        return
    require(maximum_full < TOL,
            f"SIDX2D-C2 full-register error {maximum_full:.3e}")
    require(maximum_restricted < TOL,
            f"SIDX2D-C2 restricted-register error {maximum_restricted:.3e}")
    print("SIDX2D-C2 PASS: SU(2) spec(A)={4^5,10}; "
          "SU(3) spec(A)={1^12,4^4} and {2^9,6}; "
          f"full/hw errors=({maximum_full:.2e},{maximum_restricted:.2e}); "
          f"scalar mutation defect={scalar_defect:.12f}")


def expected_certificates(expected: tuple[tuple[object, ...], ...]):
    return (row[0] for row in expected)


def defect_wave(model: dict[str, object],
                phase_sites: list[tuple[int, int]], momentum: float) -> np.ndarray:
    number_sites = int(model["N"])
    local_dimension = int(model["d"])
    _local_e, local_f, _local_h = root_generators(local_dimension)
    vacuum = np.zeros(int(model["dimension"]), dtype=complex)
    vacuum[0] = 1.0
    return sum(
        np.exp(1.0j * momentum * phase)
        * (kron_at(local_f, site, number_sites, local_dimension) @ vacuum)
        for site, phase in phase_sites
    ) / math.sqrt(len(phase_sites))


def ward_vector_gate(model: dict[str, object], certificate: dict[str, object],
                     phase_sites: list[tuple[int, int]], momentum: float,
                     expected_energy: float, expected_current: complex,
                     label: str) -> tuple[complex, complex]:
    vector = defect_wave(model, phase_sites, momentum)
    source = certificate["source"]
    target = certificate["target"]
    source_vector = vector[source]
    highest_error = float(np.linalg.norm(certificate["raising"] @ vector))
    energy_error = float(np.linalg.norm(
        model["Hamil"] @ vector - expected_energy * vector
    ))
    current_h_vector = certificate["current_h"] @ vector
    current_error = float(np.linalg.norm(
        current_h_vector - expected_current * vector
    ))
    projected_current = certificate["P"] @ (
        certificate["current_f"] @ vector
    )[target]
    descendant = certificate["D"] @ source_vector
    numerator = np.vdot(descendant, projected_current)
    denominator = np.vdot(vector, current_h_vector)
    ratio = numerator / denominator
    require(highest_error < TOL,
            f"SIDX2D-C3 {label} vector is not root-highest")
    require(energy_error < TOL,
            f"SIDX2D-C3 {label} ED energy error {energy_error:.3e}")
    require(current_error < TOL,
            f"SIDX2D-C3 {label} current eigenvalue error {current_error:.3e}")
    require(abs(denominator - expected_current) < TOL,
            f"SIDX2D-C3 {label} denominator {denominator}")
    require(abs(ratio - 1.0) < TOL,
            f"SIDX2D-C3 {label} Ward ratio {ratio}")
    return numerator, denominator


def ward_residue_gate(su2_model: dict[str, object], su2: dict[str, object],
                      su2_phases: list[tuple[int, int]],
                      su3_model: dict[str, object], su3: dict[str, object],
                      su3_phases: list[tuple[int, int]]) -> None:
    su2_current = 4.0j * math.sin(2.0 * math.pi / 3.0)
    su2_values = ward_vector_gate(
        su2_model, su2, su2_phases, 2.0 * math.pi / 3.0,
        3.0, su2_current, "SU(2) 2x3",
    )
    su3_values = ward_vector_gate(
        su3_model, su3, su3_phases, math.pi / 2.0,
        2.0, 4.0j, "SU(3) 2x2",
    )
    print("SIDX2D-C3 PASS: Ward residues numerator=denominator: "
          f"SU(2)={su2_values[0]:.12g}, SU(3)={su3_values[0]:.12g}; "
          "both normalized indices=1")


def main() -> None:
    arguments = sys.argv[1:]
    require(len(arguments) <= 1, "red modes are mutually exclusive")
    mode = arguments[0] if arguments else None
    require(mode is None or mode in RED_MODES,
            f"unknown mode {mode}; choose from {sorted(RED_MODES)}")
    code_shape_gate()

    su2_model, su2_phases = su2_torus()
    su3_model, su3_phases = su3_square()
    su2 = root_certificate(su2_model, 4)
    su3_one = root_certificate(su3_model, 1)
    su3_two = root_certificate(su3_model, 2)
    certificates = [su2, su3_one, su3_two]

    ed_and_covariance_gate([su2_model, su3_model], certificates)
    register_gate(su2, su3_one, su3_two, mode == "--red-scalar-full")
    if mode is not None:
        print("RED SURVIVED UNDETECTED")
        return
    ward_residue_gate(
        su2_model, su2, su2_phases, su3_model, su3_two, su3_phases
    )
    print("PASS: finite-lattice S-IDX operator theorem survived both 2D ED instances")


if __name__ == "__main__":
    main()
