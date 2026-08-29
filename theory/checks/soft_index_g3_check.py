#!/usr/bin/env python3
"""Red-capable SU(3) ED certificate for ``soft-index-g3.md``.

Green mode verifies on a three-site fundamental SU(3) ring that a highest
weight ray and each nonzero simple-root-lowered ray have torus moment-map
values separated by exactly the corresponding integral root.  It also checks
the SU(3)-invariant permutation Hamiltonian by exact diagonalization and shows
that a coherent projective interpolation has a continuous, non-quantized
moment value.

``--red`` replaces the first simple-root lowering by a mixture of the two
simple-root lowerings while retaining the pure-root target.  The resulting
ray spans two weight spaces, so gate G3-C2 must catch the mutation and exit 1.

This checker certifies G3-MM-fin on one beyond-SU(2) instance only.  It does
not certify a general-G current Ward identity, a polar projection, a soft
limit, a memory protocol, or a fixed-bond-dimension MPS statement.
"""

from __future__ import annotations

import argparse
import ast
from pathlib import Path
import sys

import numpy as np


TOL = 2.0e-12


def fail(message: str) -> None:
    print(f"FAIL: {message}", file=sys.stderr)
    raise SystemExit(1)


def require(condition: bool, message: str) -> None:
    if not condition:
        fail(message)


def code_shape_gate() -> None:
    source = Path(__file__).read_text(encoding="utf-8")
    tree = ast.parse(source)
    bare_asserts = [node for node in ast.walk(tree) if isinstance(node, ast.Assert)]
    require(not bare_asserts, "G3-C0 bare assert found")
    print("G3-C0 PASS: optimization-safe checks; no bare assert")


def kron_at(operator: np.ndarray, site: int, number_sites: int = 3) -> np.ndarray:
    result = np.array([[1.0 + 0.0j]])
    for position in range(number_sites):
        factor = operator if position == site else np.eye(3, dtype=complex)
        result = np.kron(result, factor)
    return result


def total(operator: np.ndarray) -> np.ndarray:
    return sum(kron_at(operator, site) for site in range(3))


def basis_vector(labels: tuple[int, int, int]) -> np.ndarray:
    vector = np.zeros(27, dtype=complex)
    index = labels[0] * 9 + labels[1] * 3 + labels[2]
    vector[index] = 1.0
    return vector


def swap_sites(left: int, right: int) -> np.ndarray:
    swap = np.zeros((27, 27), dtype=complex)
    for a in range(3):
        for b in range(3):
            for c in range(3):
                source = (a, b, c)
                target = list(source)
                target[left], target[right] = target[right], target[left]
                source_index = a * 9 + b * 3 + c
                target_index = target[0] * 9 + target[1] * 3 + target[2]
                swap[target_index, source_index] = 1.0
    return swap


def matrix_unit(row: int, column: int) -> np.ndarray:
    result = np.zeros((3, 3), dtype=complex)
    result[row, column] = 1.0
    return result


def moment(vector: np.ndarray, charges: tuple[np.ndarray, np.ndarray]) -> np.ndarray:
    norm = np.vdot(vector, vector).real
    require(norm > TOL, "moment map received a zero ray")
    return np.array(
        [np.vdot(vector, charge @ vector).real / norm for charge in charges]
    )


def su3_data() -> dict[str, object]:
    identity = np.eye(27, dtype=complex)
    swaps = (swap_sites(0, 1), swap_sites(1, 2), swap_sites(2, 0))
    hamiltonian = sum(identity - swap for swap in swaps)

    h1_local = np.diag([1.0, -1.0, 0.0]).astype(complex)
    h2_local = np.diag([0.0, 1.0, -1.0]).astype(complex)
    e1_local = matrix_unit(0, 1)
    f1_local = matrix_unit(1, 0)
    e2_local = matrix_unit(1, 2)
    f2_local = matrix_unit(2, 1)

    # A standard Hermitian su(3) basis, used only for the invariance check.
    hermitian_generators = (
        matrix_unit(0, 1) + matrix_unit(1, 0),
        -1.0j * (matrix_unit(0, 1) - matrix_unit(1, 0)),
        h1_local,
        matrix_unit(0, 2) + matrix_unit(2, 0),
        -1.0j * (matrix_unit(0, 2) - matrix_unit(2, 0)),
        matrix_unit(1, 2) + matrix_unit(2, 1),
        -1.0j * (matrix_unit(1, 2) - matrix_unit(2, 1)),
        np.diag([1.0, 1.0, -2.0]).astype(complex),
    )

    psi = (basis_vector((0, 0, 1)) - basis_vector((0, 1, 0))) / np.sqrt(2.0)
    return {
        "H": hamiltonian,
        "charges": (total(h1_local), total(h2_local)),
        "E1": total(e1_local),
        "F1": total(f1_local),
        "E2": total(e2_local),
        "F2": total(f2_local),
        "generators": tuple(total(generator) for generator in hermitian_generators),
        "psi": psi,
    }


def ed_and_covariance_gate(data: dict[str, object]) -> None:
    hamiltonian = data["H"]
    psi = data["psi"]
    eigenvalues = np.linalg.eigvalsh(hamiltonian)
    rounded = np.rint(eigenvalues).astype(int)
    expected_multiplicities = {0: 10, 3: 16, 6: 1}
    measured_multiplicities = {
        value: int(np.count_nonzero(rounded == value)) for value in (0, 3, 6)
    }
    spectral_error = float(np.max(np.abs(eigenvalues - rounded)))
    invariance_error = max(
        float(np.linalg.norm(hamiltonian @ generator - generator @ hamiltonian))
        for generator in data["generators"]
    )
    energy_error = float(np.linalg.norm(hamiltonian @ psi - 3.0 * psi))
    highest_error = max(
        float(np.linalg.norm(data["E1"] @ psi)),
        float(np.linalg.norm(data["E2"] @ psi)),
    )
    require(spectral_error < TOL, f"G3-C1 ED spectrum error {spectral_error:.3e}")
    require(
        measured_multiplicities == expected_multiplicities,
        f"G3-C1 wrong SU(3) ring multiplicities {measured_multiplicities}",
    )
    require(invariance_error < TOL, f"G3-C1 SU(3) covariance error {invariance_error:.3e}")
    require(energy_error < TOL, f"G3-C1 selected-state energy error {energy_error:.3e}")
    require(highest_error < TOL, f"G3-C1 highest-weight error {highest_error:.3e}")
    print(
        "G3-C1 PASS: SU(3) ED spectrum (0^10,3^16,6^1), "
        f"covariance={invariance_error:.2e}, highest={highest_error:.2e}"
    )


def root_increment_gate(data: dict[str, object], red: bool) -> tuple[np.ndarray, np.ndarray]:
    psi = data["psi"]
    charges = data["charges"]
    initial = moment(psi, charges)
    first_lowering = data["F1"] + (0.25 * data["F2"] if red else 0.0)
    first = first_lowering @ psi
    second = data["F2"] @ psi
    first_moment = moment(first, charges)
    second_moment = moment(second, charges)
    alpha1 = np.array([2.0, -1.0])
    alpha2 = np.array([-1.0, 2.0])
    initial_error = float(np.linalg.norm(initial - np.array([1.0, 1.0])))
    first_error = float(np.linalg.norm((first_moment - initial) + alpha1))
    second_error = float(np.linalg.norm((second_moment - initial) + alpha2))
    require(initial_error < TOL, f"G3-C2 initial moment error {initial_error:.3e}")
    require(first_error < TOL, f"G3-C2 alpha1 increment error {first_error:.3e}")
    require(second_error < TOL, f"G3-C2 alpha2 increment error {second_error:.3e}")
    require(abs(np.vdot(first, second)) < TOL, "G3-C2 distinct root weights are not orthogonal")
    print(
        "G3-C2 PASS: moments "
        f"lambda={initial.tolist()}, F1={first_moment.tolist()}, F2={second_moment.tolist()}"
    )
    return first, alpha1


def continuous_curve_gate(data: dict[str, object], lowered: np.ndarray, alpha1: np.ndarray) -> None:
    psi = data["psi"]
    charges = data["charges"]
    parameter = 0.5
    curve = psi + parameter * lowered
    measured = moment(curve, charges)
    initial = moment(psi, charges)
    probability = (
        parameter**2 * np.vdot(lowered, lowered).real
        / (np.vdot(psi, psi).real + parameter**2 * np.vdot(lowered, lowered).real)
    )
    expected = initial - probability * alpha1
    formula_error = float(np.linalg.norm(measured - expected))
    endpoint_distance = float(np.linalg.norm((measured - initial) + alpha1))
    require(formula_error < TOL, f"G3-C3 continuous moment formula error {formula_error:.3e}")
    require(0.0 < probability < 1.0, f"G3-C3 interpolation probability {probability}")
    require(endpoint_distance > 0.5, "G3-C3 coherent curve accidentally has a quantized endpoint step")
    print(
        "G3-C3 PASS: coherent curve is continuous, "
        f"p={probability:.6f}, moment={measured.tolist()}"
    )


def weyl_and_lattice_gate(data: dict[str, object]) -> None:
    initial = moment(data["psi"], data["charges"])
    first = moment(data["F1"] @ data["psi"], data["charges"])
    second = moment(data["F2"] @ data["psi"], data["charges"])
    reflection1 = np.array([-initial[0], initial[0] + initial[1]])
    reflection2 = np.array([initial[0] + initial[1], -initial[1]])
    require(np.linalg.norm(first - reflection1) < TOL, "G3-C4 first Weyl reflection mismatch")
    require(np.linalg.norm(second - reflection2) < TOL, "G3-C4 second Weyl reflection mismatch")

    diagonal_weights = np.column_stack(
        (np.diag(data["charges"][0]).real, np.diag(data["charges"][1]).real)
    )
    lattice_error = float(np.max(np.abs(diagonal_weights - np.rint(diagonal_weights))))
    require(lattice_error < TOL, f"G3-C4 nonintegral tensor-product weight {lattice_error:.3e}")
    require(initial[0] > 0.0 and initial[1] > 0.0, "G3-C4 initial weight not inside dominant chamber")
    require(first[0] < 0.0 and second[1] < 0.0, "G3-C4 root steps did not cross simple walls")
    print("G3-C4 PASS: integral weights; both simple steps equal Weyl reflections at lambda=(1,1)")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--red",
        action="store_true",
        help="mix F1 with F2 while retaining the pure-alpha1 moment target",
    )
    arguments = parser.parse_args()
    code_shape_gate()
    data = su3_data()
    ed_and_covariance_gate(data)
    lowered, alpha1 = root_increment_gate(data, arguments.red)
    continuous_curve_gate(data, lowered, alpha1)
    weyl_and_lattice_gate(data)
    print("PASS: G3-MM-fin SU(3) finite-volume certificate")


if __name__ == "__main__":
    main()
