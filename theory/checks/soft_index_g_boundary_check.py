#!/usr/bin/env python3
"""Finite boundary/falsifier battery for a general-G soft-index claim.

Green command:
    python3 -O theory/checks/soft_index_g_boundary_check.py

Run one gate:
    python3 -O theory/checks/soft_index_g_boundary_check.py --gate G5-C1-ABELIAN

The negative gates deliberately require a nonzero residual.  Thus a future
change which accidentally makes a registered obstruction disappear is red,
not green.  No bare ``assert`` is used, so all checks survive ``python -O``.
Only NumPy and the Python standard library are required.
"""

from __future__ import annotations

import argparse
import ast
from functools import lru_cache
from itertools import product
import math
from pathlib import Path
import sys

import numpy as np


TOL = 2.0e-10
GATES = (
    "G5-C0-SHAPE",
    "G5-C1-ABELIAN",
    "G5-C2-FINITE",
    "G5-C3-GLOBAL-FORM",
    "G5-C4-SU3-H-MULT",
    "G5-C5-SU3-REGISTER",
)


def fail(message: str) -> None:
    print(f"FAIL: {message}", file=sys.stderr)
    raise SystemExit(1)


def require(condition: bool, message: str) -> None:
    if not condition:
        fail(message)


def max_abs(matrix: np.ndarray) -> float:
    return float(np.max(np.abs(matrix))) if matrix.size else 0.0


def matrix_rank(matrix: np.ndarray, tolerance: float = 1.0e-10) -> int:
    return int(np.sum(np.linalg.svd(matrix, compute_uv=False) > tolerance))


def matrix_unit(dimension: int, row: int, column: int) -> np.ndarray:
    result = np.zeros((dimension, dimension), dtype=complex)
    result[row, column] = 1.0
    return result


def spin_matrices(two_s: int) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    site_spin = two_s / 2.0
    dimension = two_s + 1
    raising = np.zeros((dimension, dimension), dtype=complex)
    for occupation in range(1, dimension):
        raising[occupation - 1, occupation] = math.sqrt(
            occupation * (two_s - occupation + 1)
        )
    lowering = raising.T.conj()
    z_spin = np.diag(
        [site_spin - occupation for occupation in range(dimension)]
    ).astype(complex)
    return raising, lowering, z_spin


def kron_at(operator: np.ndarray, site: int, number_sites: int,
            local_dimension: int) -> np.ndarray:
    result = np.array([[1.0 + 0.0j]])
    for position in range(number_sites):
        factor = operator if position == site else np.eye(local_dimension)
        result = np.kron(result, factor)
    return result


def global_operator(operator: np.ndarray, number_sites: int) -> np.ndarray:
    local_dimension = operator.shape[0]
    return sum(
        kron_at(operator, site, number_sites, local_dimension)
        for site in range(number_sites)
    )


def tensor_power(operator: np.ndarray, number_sites: int) -> np.ndarray:
    result = np.array([[1.0 + 0.0j]])
    for _ in range(number_sites):
        result = np.kron(result, operator)
    return result


@lru_cache(maxsize=None)
def digit_tuples(local_dimension: int, number_sites: int) -> tuple[tuple[int, ...], ...]:
    return tuple(product(range(local_dimension), repeat=number_sites))


def tuple_index(digits: tuple[int, ...], local_dimension: int) -> int:
    result = 0
    for digit in digits:
        result = local_dimension * result + digit
    return result


def swap_operator(local_dimension: int, number_sites: int,
                  first: int, second: int) -> np.ndarray:
    dimension = local_dimension ** number_sites
    result = np.zeros((dimension, dimension), dtype=complex)
    for old_index, digits in enumerate(digit_tuples(local_dimension, number_sites)):
        moved = list(digits)
        moved[first], moved[second] = moved[second], moved[first]
        result[tuple_index(tuple(moved), local_dimension), old_index] = 1.0
    return result


def permutation_bonds(local_dimension: int, number_sites: int) -> list[np.ndarray]:
    dimension = local_dimension ** number_sites
    identity = np.eye(dimension, dtype=complex)
    return [
        identity - swap_operator(
            local_dimension, number_sites, site, (site + 1) % number_sites
        )
        for site in range(number_sites)
    ]


def highest_weight_basis(raising_operators: list[np.ndarray],
                         source_indices: np.ndarray) -> np.ndarray:
    stacked = np.vstack([
        operator[:, source_indices] for operator in raising_operators
    ])
    _left, singular_values, right_adjoint = np.linalg.svd(
        stacked, full_matrices=True
    )
    rank = int(np.sum(singular_values > 1.0e-10))
    return right_adjoint[rank:].conj().T


def code_shape_gate() -> None:
    tree = ast.parse(Path(__file__).read_text(encoding="utf-8"))
    bare = [node for node in ast.walk(tree) if isinstance(node, ast.Assert)]
    require(not bare, "G5-C0-SHAPE found a bare assert")
    print("G5-C0-SHAPE PASS bare_asserts=0 optimization_safe=1")


def abelian_gate() -> None:
    """U(1)^2: Cartan charges cannot create either one-colour excitation."""
    number_sites = 3
    local_dimension = 3
    dimension = local_dimension ** number_sites
    bonds = permutation_bonds(local_dimension, number_sites)
    hamiltonian = sum(bonds)
    cartan_local = (
        np.diag([1.0, -1.0, 0.0]).astype(complex),
        np.diag([0.0, 1.0, -1.0]).astype(complex),
    )
    charges = [
        global_operator(generator, number_sites) for generator in cartan_local
    ]
    vacuum = np.zeros(dimension, dtype=complex)
    vacuum[0] = 1.0
    identity = np.eye(dimension, dtype=complex)
    normal_ordered = [
        charge - np.vdot(vacuum, charge @ vacuum) * identity
        for charge in charges
    ]
    created = np.column_stack([charge @ vacuum for charge in normal_ordered])
    created_rank = matrix_rank(created)

    momentum = 2.0 * math.pi / number_sites
    one_colour = []
    for colour in (1, 2):
        vector = np.zeros(dimension, dtype=complex)
        for site in range(number_sites):
            digits = [0] * number_sites
            digits[site] = colour
            vector[tuple_index(tuple(digits), local_dimension)] = (
                np.exp(1.0j * momentum * site) / math.sqrt(number_sites)
            )
        one_colour.append(vector)
    magnon_gram_error = max_abs(
        np.column_stack(one_colour).conj().T @ np.column_stack(one_colour)
        - np.eye(2)
    )
    overlap = max_abs(created.conj().T @ np.column_stack(one_colour))
    conservation = max(
        max_abs(hamiltonian @ charge - charge @ hamiltonian)
        for charge in charges
    )
    bracket = max_abs(
        cartan_local[0] @ cartan_local[1]
        - cartan_local[1] @ cartan_local[0]
    )
    magnon_distance = min(float(np.linalg.norm(vector)) for vector in one_colour)

    # A genuinely broken abelian orbit is different rather than zero.  View
    # the spin-1/2 permutation ferromagnet only through its U(1)_z subgroup
    # and choose the exact equatorial coherent ground state |+x>^N.
    spin_half_hamiltonian = sum(permutation_bonds(2, number_sites))
    plus_x = np.array([1.0, 1.0], dtype=complex) / math.sqrt(2.0)
    broken_vacuum = plus_x
    for _ in range(number_sites - 1):
        broken_vacuum = np.kron(broken_vacuum, plus_x)
    z_charge = global_operator(
        np.diag([0.5, -0.5]).astype(complex), number_sites
    )
    charge_mean = np.vdot(broken_vacuum, z_charge @ broken_vacuum)
    orbit_tangent = z_charge @ broken_vacuum - charge_mean * broken_vacuum
    orbit_tangent_norm = float(np.linalg.norm(orbit_tangent))
    orbit_orthogonality = abs(np.vdot(broken_vacuum, orbit_tangent))
    orbit_energy_residual = float(np.linalg.norm(
        spin_half_hamiltonian @ orbit_tangent
    ))

    require(bracket < TOL, "G5-C1-ABELIAN Cartan bracket is nonzero")
    require(conservation < TOL, "G5-C1-ABELIAN charges are not conserved")
    require(created_rank == 0,
            "G5-C1-ABELIAN normal-ordered Cartan charge created a state")
    require(overlap < TOL,
            "G5-C1-ABELIAN Cartan-created span overlaps a colour magnon")
    require(magnon_gram_error < TOL and magnon_distance > 0.999999,
            "G5-C1-ABELIAN comparison magnons are not orthonormal")
    require(abs(orbit_tangent_norm - math.sqrt(0.75)) < TOL,
            "G5-C1-ABELIAN broken U(1) orbit tangent has wrong norm")
    require(orbit_orthogonality < TOL and orbit_energy_residual < TOL,
            "G5-C1-ABELIAN broken U(1) orbit tangent check failed")
    print(
        "G5-C1-ABELIAN PASS "
        f"cartan_bracket={bracket:.2e} conservation={conservation:.2e} "
        f"charge_created_rank={created_rank} magnon_overlap={overlap:.2e} "
        f"magnon_distance={magnon_distance:.6f} "
        f"broken_U1_tangent={orbit_tangent_norm:.6f} "
        f"tangent_energy={orbit_energy_residual:.2e}"
    )


def finite_group_gate() -> None:
    """Z2: group elements are sector diagonal; strings leave endpoints."""
    number_sites = 4
    local_dimension = 2
    x_pauli = np.array([[0.0, 1.0], [1.0, 0.0]], dtype=complex)
    z_pauli = np.diag([1.0, -1.0]).astype(complex)
    dimension = local_dimension ** number_sites
    identity = np.eye(dimension, dtype=complex)
    global_flip = tensor_power(x_pauli, number_sites)
    field = 0.37
    hamiltonian = np.zeros((dimension, dimension), dtype=complex)
    for site in range(number_sites):
        neighbour = (site + 1) % number_sites
        hamiltonian -= (
            kron_at(z_pauli, site, number_sites, local_dimension)
            @ kron_at(z_pauli, neighbour, number_sites, local_dimension)
        )
        hamiltonian -= field * kron_at(
            x_pauli, site, number_sites, local_dimension
        )
    plus = (identity + global_flip) / 2.0
    minus = (identity - global_flip) / 2.0
    attempted_descendant = minus @ global_flip @ plus
    attempted_gram = attempted_descendant.conj().T @ attempted_descendant

    region = (1, 2)
    string = np.eye(dimension, dtype=complex)
    for site in region:
        string = string @ kron_at(
            x_pauli, site, number_sites, local_dimension
        )
    endpoint_expected = 2.0 * (
        kron_at(z_pauli, 0, number_sites, local_dimension)
        @ kron_at(z_pauli, 1, number_sites, local_dimension)
        + kron_at(z_pauli, 2, number_sites, local_dimension)
        @ kron_at(z_pauli, 3, number_sites, local_dimension)
    )
    endpoint_residual = max_abs(
        string.conj().T @ hamiltonian @ string
        - hamiltonian - endpoint_expected
    )
    symmetry_residual = max_abs(
        hamiltonian @ global_flip - global_flip @ hamiltonian
    )
    cross_rank = matrix_rank(attempted_descendant)
    gram_norm = float(np.linalg.norm(attempted_gram))

    require(symmetry_residual < TOL,
            "G5-C2-FINITE global Z2 is not a symmetry")
    require(cross_rank == 0 and gram_norm < TOL,
            "G5-C2-FINITE a group element unexpectedly changes Z2 charge")
    require(endpoint_residual < TOL,
            "G5-C2-FINITE discrete string did not reduce to endpoints")
    print(
        "G5-C2-FINITE PASS "
        f"symmetry={symmetry_residual:.2e} cross_sector_rank={cross_rank} "
        f"gram_norm={gram_norm:.2e} endpoint_residual={endpoint_residual:.2e}"
    )


def heisenberg_chain(two_s: int, number_sites: int) -> dict[str, np.ndarray]:
    raising, lowering, z_spin = spin_matrices(two_s)
    local_dimension = two_s + 1
    x_spin = (raising + lowering) / 2.0
    y_spin = (raising - lowering) / (2.0j)
    total_x = global_operator(x_spin, number_sites)
    total_y = global_operator(y_spin, number_sites)
    total_z = global_operator(z_spin, number_sites)
    dimension = local_dimension ** number_sites
    hamiltonian = np.zeros((dimension, dimension), dtype=complex)
    for site in range(number_sites):
        neighbour = (site + 1) % number_sites
        for generator in (x_spin, y_spin, z_spin):
            hamiltonian -= (
                kron_at(generator, site, number_sites, local_dimension)
                @ kron_at(generator, neighbour, number_sites, local_dimension)
            )
    casimir = total_x @ total_x + total_y @ total_y + total_z @ total_z
    return {"H": hamiltonian, "Sz": total_z, "S2": casimir}


def spin_content(casimir: np.ndarray) -> dict[float, int]:
    labels: dict[float, int] = {}
    for eigenvalue in np.linalg.eigvalsh(casimir):
        spin = (-1.0 + math.sqrt(max(0.0, 1.0 + 4.0 * float(eigenvalue)))) / 2.0
        rounded = round(2.0 * spin) / 2.0
        labels[rounded] = labels.get(rounded, 0) + 1
    return labels


def o2_comparator() -> tuple[float, float, float]:
    number_sites = 3
    raising, lowering, z_spin = spin_matrices(2)
    x_spin = (raising + lowering) / 2.0
    y_spin = (raising - lowering) / (2.0j)
    local_dimension = 3
    dimension = local_dimension ** number_sites
    hamiltonian = np.zeros((dimension, dimension), dtype=complex)
    anisotropy = 0.71
    single_ion = 0.23
    for site in range(number_sites):
        neighbour = (site + 1) % number_sites
        hamiltonian += (
            kron_at(x_spin, site, number_sites, local_dimension)
            @ kron_at(x_spin, neighbour, number_sites, local_dimension)
            + kron_at(y_spin, site, number_sites, local_dimension)
            @ kron_at(y_spin, neighbour, number_sites, local_dimension)
            + anisotropy
            * kron_at(z_spin, site, number_sites, local_dimension)
            @ kron_at(z_spin, neighbour, number_sites, local_dimension)
            + single_ion
            * kron_at(z_spin @ z_spin, site, number_sites, local_dimension)
        )
    reflection_local = np.array(
        [[0.0, 0.0, 1.0], [0.0, 1.0, 0.0], [1.0, 0.0, 0.0]],
        dtype=complex,
    )
    reflection = tensor_power(reflection_local, number_sites)
    charge = global_operator(z_spin, number_sites)
    symmetry = max(
        max_abs(hamiltonian @ charge - charge @ hamiltonian),
        max_abs(hamiltonian @ reflection - reflection @ hamiltonian),
    )
    reflection_flip = max_abs(reflection @ charge @ reflection + charge)
    charge_diagonal = np.rint(np.diag(charge).real).astype(int)
    paired_mismatch = 0.0
    for value in range(1, number_sites + 1):
        positive = np.where(charge_diagonal == value)[0]
        negative = np.where(charge_diagonal == -value)[0]
        if len(positive) == 0:
            continue
        spectrum_positive = np.linalg.eigvalsh(hamiltonian[np.ix_(positive, positive)])
        spectrum_negative = np.linalg.eigvalsh(hamiltonian[np.ix_(negative, negative)])
        require(len(spectrum_positive) == len(spectrum_negative),
                "G5-C3-GLOBAL-FORM O(2) paired sectors have different sizes")
        paired_mismatch = max(
            paired_mismatch,
            max_abs(spectrum_positive - spectrum_negative),
        )
    return symmetry, reflection_flip, paired_mismatch


def global_form_gate() -> None:
    """SO(3)/SU(2) centre and O(2) component tests."""
    number_sites = 3
    so3 = heisenberg_chain(2, number_sites)
    su2_only = heisenberg_chain(1, number_sites)
    so3_content = spin_content(so3["S2"])
    su2_content = spin_content(su2_only["S2"])
    so3_dimension = so3["H"].shape[0]
    su2_dimension = su2_only["H"].shape[0]
    so3_center = np.diag(
        np.exp(2.0j * math.pi * np.diag(so3["Sz"]).real)
    )
    su2_center = np.diag(
        np.exp(2.0j * math.pi * np.diag(su2_only["Sz"]).real)
    )
    so3_center_error = max_abs(so3_center - np.eye(so3_dimension))
    su2_center_error = max_abs(su2_center + np.eye(su2_dimension))
    casimir_commutator = max(
        max_abs(so3["H"] @ so3["S2"] - so3["S2"] @ so3["H"]),
        max_abs(
            su2_only["H"] @ su2_only["S2"]
            - su2_only["S2"] @ su2_only["H"]
        ),
    )
    o2_symmetry, o2_reflection_flip, o2_pairing = o2_comparator()

    require(so3_content == {0.0: 1, 1.0: 9, 2.0: 10, 3.0: 7},
            f"G5-C3-GLOBAL-FORM unexpected spin-1 content {so3_content}")
    require(su2_content == {0.5: 4, 1.5: 4},
            f"G5-C3-GLOBAL-FORM unexpected spin-1/2 content {su2_content}")
    require(casimir_commutator < TOL,
            "G5-C3-GLOBAL-FORM Heisenberg chain is not symmetric")
    require(so3_center_error < TOL and su2_center_error < TOL,
            "G5-C3-GLOBAL-FORM centre action has the wrong sign")
    require(o2_symmetry < TOL and o2_reflection_flip < TOL and o2_pairing < TOL,
            "G5-C3-GLOBAL-FORM O(2) disconnected-component test failed")
    print(
        "G5-C3-GLOBAL-FORM PASS "
        f"SO3_spins={so3_content} SU2only_spins={su2_content} "
        f"center_errors=({so3_center_error:.2e},{su2_center_error:.2e}) "
        f"casimir_commutator={casimir_commutator:.2e} "
        f"O2_symmetry={o2_symmetry:.2e} O2_FQFplusQ={o2_reflection_flip:.2e} "
        f"O2_paired_spectrum={o2_pairing:.2e}"
    )


@lru_cache(maxsize=1)
def su3_experiment() -> dict[str, object]:
    """N=5 fundamental SU(3) permutation ferromagnet, weight (3,2,0)."""
    number_sites = 5
    local_dimension = 3
    dimension = local_dimension ** number_sites
    digits = digit_tuples(local_dimension, number_sites)
    counts = tuple(
        tuple(site_tuple.count(colour) for colour in range(local_dimension))
        for site_tuple in digits
    )

    def sector_indices(sector_counts: tuple[int, int, int]) -> np.ndarray:
        return np.asarray([
            index for index, value in enumerate(counts)
            if value == sector_counts
        ], dtype=int)

    local_units = {
        (row, column): matrix_unit(local_dimension, row, column)
        for row in range(local_dimension)
        for column in range(local_dimension)
    }
    global_units = {
        key: global_operator(value, number_sites)
        for key, value in local_units.items()
    }
    bonds = permutation_bonds(local_dimension, number_sites)
    hamiltonian = sum(bonds)

    def current(local_generator: np.ndarray) -> np.ndarray:
        return sum(
            -(
                bond @ kron_at(
                    local_generator, site, number_sites, local_dimension
                )
                - kron_at(
                    local_generator, site, number_sites, local_dimension
                ) @ bond
            )
            for site, bond in enumerate(bonds)
        )

    source_counts = (3, 2, 0)
    source = sector_indices(source_counts)
    raising = [
        global_units[(0, 1)], global_units[(0, 2)], global_units[(1, 2)]
    ]
    highest = highest_weight_basis(raising, source)
    highest_projector = highest @ highest.conj().T
    source_lookup = {int(full_index): offset
                     for offset, full_index in enumerate(source)}
    translation_source = np.zeros((len(source), len(source)), dtype=complex)
    for old_offset, full_index in enumerate(source):
        old_digits = digits[int(full_index)]
        translated_digits = old_digits[-1:] + old_digits[:-1]
        translated_index = tuple_index(translated_digits, local_dimension)
        translation_source[source_lookup[translated_index], old_offset] = 1.0
    momentum = -4.0 * math.pi / 5.0
    momentum_projector = sum(
        np.exp(-1.0j * momentum * power)
        * np.linalg.matrix_power(translation_source, power)
        for power in range(number_sites)
    ) / number_sites
    raw = np.zeros(len(source), dtype=complex)
    raw[0] = 1.0
    source_vector = momentum_projector @ highest_projector @ raw
    projected_norm = float(np.linalg.norm(source_vector))
    require(projected_norm > 1.0e-8,
            "SU3 deterministic source has zero highest-weight projection")
    source_vector /= projected_norm
    psi = np.zeros(dimension, dtype=complex)
    psi[source] = source_vector
    highest_error = max(
        float(np.linalg.norm(operator @ psi)) for operator in raising
    )
    translation_error = float(np.linalg.norm(
        translation_source @ source_vector
        - np.exp(1.0j * momentum) * source_vector
    ))
    hamiltonian_source = hamiltonian[np.ix_(source, source)]
    energy = float(np.vdot(
        source_vector, hamiltonian_source @ source_vector
    ).real)
    energy_error = float(np.linalg.norm(
        hamiltonian_source @ source_vector - energy * source_vector
    ))
    symmetry_error = max(
        max_abs(hamiltonian @ generator - generator @ hamiltonian)
        for key, generator in global_units.items() if key[0] != key[1]
    )
    vacuum = np.zeros(dimension, dtype=complex)
    vacuum[0] = 1.0
    unbroken_tangent = max(
        float(np.linalg.norm(global_units[(1, 2)] @ vacuum)),
        float(np.linalg.norm(global_units[(2, 1)] @ vacuum)),
        float(np.linalg.norm(
            (global_units[(1, 1)] - global_units[(2, 2)]) @ vacuum
        )),
    )
    broken_tangent = min(
        float(np.linalg.norm(global_units[(1, 0)] @ vacuum)),
        float(np.linalg.norm(global_units[(2, 0)] @ vacuum)),
    )

    root_results: dict[str, dict[str, object]] = {}
    root_data = (
        ("alpha12", (1, 0), (0, 1), (2, 3, 0), 1.0),
        ("alpha13", (2, 0), (0, 2), (2, 2, 1), 3.0),
    )
    for name, lower_key, raise_key, target_counts, root_weight in root_data:
        target = sector_indices(target_counts)
        lowering = global_units[lower_key]
        raising_root = global_units[raise_key]
        local_lowering = local_units[lower_key]
        root_cartan = local_units[(0, 0)] - local_units[(lower_key[0], lower_key[0])]
        lowering_current = current(local_lowering)
        cartan_current = current(root_cartan)
        descendant_map = lowering[np.ix_(target, source)]
        gram_full = descendant_map.conj().T @ descendant_map
        projection_full = descendant_map @ np.linalg.solve(
            gram_full, descendant_map.conj().T
        )
        current_source = (cartan_current @ psi)[source]
        lhs_full = projection_full @ (lowering_current @ psi)[target]
        rhs_full = descendant_map @ np.linalg.solve(gram_full, current_source)
        rhs_scalar = descendant_map @ current_source / root_weight

        descendant_highest = descendant_map @ highest
        gram_highest = descendant_highest.conj().T @ descendant_highest
        projection_highest = descendant_highest @ np.linalg.solve(
            gram_highest, descendant_highest.conj().T
        )
        lhs_highest = projection_highest @ (lowering_current @ psi)[target]
        rhs_highest = descendant_highest @ np.linalg.solve(
            gram_highest, highest.conj().T @ current_source
        )
        compressed_current = (
            highest.conj().T
            @ cartan_current[np.ix_(source, source)]
            @ highest
        )
        scalar_part = np.trace(compressed_current) / highest.shape[1]
        multiplicity_scalar_defect = float(np.linalg.norm(
            compressed_current - scalar_part * np.eye(highest.shape[1])
        ))
        commutator_error = max_abs(
            raising_root @ lowering_current
            - lowering_current @ raising_root - cartan_current
        )
        full_error = float(np.linalg.norm(lhs_full - rhs_full))
        scalar_error = float(np.linalg.norm(lhs_full - rhs_scalar))
        scalar_relative = scalar_error / max(float(np.linalg.norm(lhs_full)), 1.0e-30)
        restricted_error = float(np.linalg.norm(lhs_highest - rhs_highest))
        cross_register_error = float(np.linalg.norm(lhs_full - rhs_highest))
        current_leakage = float(np.linalg.norm(
            (np.eye(len(source)) - highest_projector) @ current_source
        ))
        root_results[name] = {
            "commutator_error": commutator_error,
            "full_error": full_error,
            "scalar_error": scalar_error,
            "scalar_relative": scalar_relative,
            "restricted_error": restricted_error,
            "cross_register_error": cross_register_error,
            "current_leakage": current_leakage,
            "multiplicity_scalar_defect": multiplicity_scalar_defect,
            "gram_full_eigenvalues": np.linalg.eigvalsh(gram_full),
            "gram_highest_error": float(np.linalg.norm(
                gram_highest - root_weight * np.eye(highest.shape[1])
            )),
            "lhs_norm": float(np.linalg.norm(lhs_full)),
        }

    return {
        "source_dimension": len(source),
        "highest_dimension": highest.shape[1],
        "highest_error": highest_error,
        "translation_error": translation_error,
        "momentum": momentum,
        "energy": energy,
        "energy_error": energy_error,
        "symmetry_error": symmetry_error,
        "unbroken_tangent": unbroken_tangent,
        "broken_tangent": broken_tangent,
        "projected_norm": projected_norm,
        "roots": root_results,
    }


def su3_h_multiplicity_gate() -> None:
    data = su3_experiment()
    alpha12 = data["roots"]["alpha12"]
    alpha13 = data["roots"]["alpha13"]
    require(data["source_dimension"] == 10 and data["highest_dimension"] == 5,
            "G5-C4-SU3-H-MULT wrong SU(3) multiplicity dimensions")
    require(data["highest_error"] < TOL,
            "G5-C4-SU3-H-MULT source is not SU(3) highest weight")
    require(data["translation_error"] < TOL and data["energy_error"] < TOL,
            "G5-C4-SU3-H-MULT source is not an exact momentum/energy state")
    require(data["symmetry_error"] < TOL
            and data["unbroken_tangent"] < TOL
            and abs(data["broken_tangent"] - math.sqrt(5.0)) < TOL,
            "G5-C4-SU3-H-MULT broken/unbroken SU(3) model check failed")
    require(alpha12["commutator_error"] < TOL
            and alpha13["commutator_error"] < TOL,
            "G5-C4-SU3-H-MULT adjoint-current covariance failed")
    require(alpha12["full_error"] < TOL and alpha13["full_error"] < TOL,
            "G5-C4-SU3-H-MULT exact Gram-inverse identity failed")
    require(alpha12["scalar_relative"] > 1.0,
            "G5-C4-SU3-H-MULT alpha12 scalar obstruction disappeared")
    require(alpha13["scalar_relative"] < TOL,
            "G5-C4-SU3-H-MULT alpha13 control is no longer exact")
    require(alpha12["multiplicity_scalar_defect"] > 6.0,
            "G5-C4-SU3-H-MULT multiplicity action became scalar")
    print(
        "G5-C4-SU3-H-MULT PASS "
        f"source_dim={data['source_dimension']} hw_multiplicity={data['highest_dimension']} "
        f"hw_error={data['highest_error']:.2e} "
        f"symmetry={data['symmetry_error']:.2e} "
        f"H_tangent={data['unbroken_tangent']:.2e} "
        f"broken_tangent={data['broken_tangent']:.6f} "
        f"momentum={data['momentum'] / math.pi:.1f}pi energy={data['energy']:.6f} "
        f"energy_error={data['energy_error']:.2e} "
        f"alpha12_full={alpha12['full_error']:.2e} "
        f"alpha12_scalar={alpha12['scalar_error']:.6f} "
        f"alpha12_relative={alpha12['scalar_relative']:.6f} "
        f"alpha13_full={alpha13['full_error']:.2e} "
        f"alpha13_scalar={alpha13['scalar_error']:.2e} "
        f"multiplicity_scalar_defect={alpha12['multiplicity_scalar_defect']:.6f}"
    )


def su3_register_gate() -> None:
    data = su3_experiment()
    alpha12 = data["roots"]["alpha12"]
    eigenvalues = np.asarray(alpha12["gram_full_eigenvalues"])
    rounded = np.rint(eigenvalues).astype(int)
    spectrum_counts = {
        int(value): int(np.sum(rounded == value)) for value in np.unique(rounded)
    }
    full_scalar_defect = float(np.linalg.norm(eigenvalues - 1.0))
    require(spectrum_counts == {1: 5, 4: 4, 9: 1},
            f"G5-C5-SU3-REGISTER wrong full Gram spectrum {spectrum_counts}")
    require(abs(full_scalar_defect - 10.0) < TOL,
            "G5-C5-SU3-REGISTER full Gram unexpectedly scalar")
    require(alpha12["gram_highest_error"] < TOL,
            "G5-C5-SU3-REGISTER restricted Gram is not scalar")
    require(alpha12["full_error"] < TOL
            and alpha12["restricted_error"] < TOL,
            "G5-C5-SU3-REGISTER a corrected register is not exact")
    require(alpha12["scalar_error"] > 5.0,
            "G5-C5-SU3-REGISTER naive scalar substitution no longer fails")
    require(alpha12["cross_register_error"] > 1.0,
            "G5-C5-SU3-REGISTER cross-register mismatch disappeared")
    require(alpha12["current_leakage"] > 3.0,
            "G5-C5-SU3-REGISTER Cartan current no longer leaves hw space")
    print(
        "G5-C5-SU3-REGISTER PASS "
        f"A_full_spectrum={spectrum_counts} A_full_scalar_defect={full_scalar_defect:.6f} "
        f"A_hw_error={alpha12['gram_highest_error']:.2e} "
        f"full_error={alpha12['full_error']:.2e} "
        f"restricted_error={alpha12['restricted_error']:.2e} "
        f"naive_scalar_error={alpha12['scalar_error']:.6f} "
        f"cross_register_error={alpha12['cross_register_error']:.6f} "
        f"current_leakage={alpha12['current_leakage']:.6f}"
    )


GATE_FUNCTIONS = {
    "G5-C0-SHAPE": code_shape_gate,
    "G5-C1-ABELIAN": abelian_gate,
    "G5-C2-FINITE": finite_group_gate,
    "G5-C3-GLOBAL-FORM": global_form_gate,
    "G5-C4-SU3-H-MULT": su3_h_multiplicity_gate,
    "G5-C5-SU3-REGISTER": su3_register_gate,
}


def parse_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--gate", choices=GATES, help="run one named gate")
    return parser.parse_args()


def main() -> None:
    arguments = parse_arguments()
    selected = (arguments.gate,) if arguments.gate else GATES
    for name in selected:
        GATE_FUNCTIONS[name]()
    if arguments.gate:
        print(f"SELECTED GATE PASS: {arguments.gate}")
    else:
        print("ALL GENERAL-G BOUNDARY GATES PASS")


if __name__ == "__main__":
    main()
