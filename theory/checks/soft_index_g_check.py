#!/usr/bin/env python3
"""Finite red-capable certificate for theory/soft-index-g.md.

Green:
    python3 -O theory/checks/soft_index_g_check.py

Registered red modes mutate load-bearing theorem structure and must exit 1:
    --red-scalar-full         replace the full-sector A^{-1} by 1/lambda
    --red-drop-hw-projector   omit Pi_hw in the restricted register
    --red-drop-hw-factor      omit 1/lambda at lambda=2
    --red-force-h-block       pretend all of the unbroken H centralizes a root

The new instance is the N=4 SU(3) fundamental permutation ring.  The SU(2)
gate imports the same finite-ring constructor used by soft_index_r2_check.py
and verifies its SIDXR2-C2 numbers.  SIDXG-C6 imports the existing G4 SU(3)
helpers and checks the shared root/central overlap without adding a mutation.
No bare assert is used, so every gate remains active under python3 -O.
"""

from __future__ import annotations

import ast
import importlib.util
import math
from pathlib import Path
import sys

import numpy as np


HERE = Path(__file__).resolve().parent
TOL = 2.0e-11
RED_MODES = {
    "--red-scalar-full",
    "--red-drop-hw-projector",
    "--red-drop-hw-factor",
    "--red-force-h-block",
}


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
    require(not bare, "SIDXG-C0 bare assert found")
    print("SIDXG-C0 PASS: optimization-safe require/fail checks; no bare assert")


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    require(spec is not None and spec.loader is not None,
            f"cannot load module {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def kron_at(operator: np.ndarray, site: int, number_sites: int,
            local_dimension: int) -> np.ndarray:
    result = np.array([[1.0 + 0.0j]])
    for position in range(number_sites):
        factor = operator if position == site else np.eye(local_dimension)
        result = np.kron(result, factor)
    return result


def tensor_power(operator: np.ndarray, number_sites: int) -> np.ndarray:
    result = np.array([[1.0 + 0.0j]])
    for _position in range(number_sites):
        result = np.kron(result, operator)
    return result


def swap_operator(site: int, neighbour: int, number_sites: int,
                  local_dimension: int) -> np.ndarray:
    shape = (local_dimension,) * number_sites
    dimension = local_dimension ** number_sites
    swap = np.zeros((dimension, dimension), dtype=complex)
    for source_tuple in np.ndindex(*shape):
        target_tuple = list(source_tuple)
        target_tuple[site], target_tuple[neighbour] = (
            target_tuple[neighbour], target_tuple[site]
        )
        source = np.ravel_multi_index(source_tuple, shape)
        target = np.ravel_multi_index(tuple(target_tuple), shape)
        swap[target, source] = 1.0
    return swap


def local_root(first: int, second: int) -> tuple[np.ndarray, ...]:
    raising = np.zeros((3, 3), dtype=complex)
    raising[first, second] = 1.0
    lowering = raising.T.conj()
    coroot = np.zeros((3, 3), dtype=complex)
    coroot[first, first] = 1.0
    coroot[second, second] = -1.0
    return raising, lowering, coroot


def global_sum(operator: np.ndarray, number_sites: int) -> np.ndarray:
    return sum(
        kron_at(operator, site, number_sites, operator.shape[0])
        for site in range(number_sites)
    )


def su3_ring(number_sites: int = 4) -> dict[str, object]:
    local_dimension = 3
    dimension = local_dimension ** number_sites
    identity = np.eye(dimension, dtype=complex)
    bonds = []
    hamiltonian = np.zeros((dimension, dimension), dtype=complex)
    for site in range(number_sites):
        neighbour = (site + 1) % number_sites
        bond = identity - swap_operator(
            site, neighbour, number_sites, local_dimension
        )
        bonds.append(bond)
        hamiltonian += bond
    return {
        "N": number_sites,
        "dimension": dimension,
        "H": hamiltonian,
        "bonds": bonds,
    }


def current_zero_mode(ring: dict[str, object],
                      local_generator: np.ndarray) -> np.ndarray:
    number_sites = int(ring["N"])
    hamiltonian = ring["H"]
    current = np.zeros_like(hamiltonian)
    for site, bond in enumerate(ring["bonds"]):
        local = kron_at(local_generator, site, number_sites, 3)
        current -= bond @ local - local @ bond
    return current


def highest_weight_basis(raising: np.ndarray,
                         source_indices: np.ndarray) -> np.ndarray:
    _u, singular_values, vh = np.linalg.svd(
        raising[:, source_indices], full_matrices=True
    )
    rank = int(np.sum(singular_values > 1.0e-10))
    return vh[rank:].conj().T


def root_certificate(ring: dict[str, object], first: int,
                     second: int, weight: int = 1) -> dict[str, object]:
    number_sites = int(ring["N"])
    local_e, local_f, local_h = local_root(first, second)
    raising = global_sum(local_e, number_sites)
    lowering = global_sum(local_f, number_sites)
    coroot = global_sum(local_h, number_sites)
    current_e = current_zero_mode(ring, local_e)
    current_f = current_zero_mode(ring, local_f)
    current_h = current_zero_mode(ring, local_h)

    weights = np.rint(np.diag(coroot).real).astype(int)
    source = np.where(weights == weight)[0]
    target = np.where(weights == weight - 2)[0]
    descendant_map = lowering[np.ix_(target, source)]
    gram = descendant_map.conj().T @ descendant_map
    projection = descendant_map @ np.linalg.solve(
        gram, descendant_map.conj().T
    )
    highest = highest_weight_basis(raising, source)
    current_f_block = current_f[np.ix_(target, source)]
    current_h_block = current_h[np.ix_(source, source)]

    full_lhs = projection @ current_f_block @ highest
    h_on_highest = current_h_block @ highest
    full_rhs = descendant_map @ np.linalg.solve(gram, h_on_highest)
    scalar_full_rhs = descendant_map @ h_on_highest

    restricted_map = descendant_map @ highest
    restricted_gram = restricted_map.conj().T @ restricted_map
    restricted_projection = restricted_map @ np.linalg.solve(
        restricted_gram, restricted_map.conj().T
    )
    restricted_lhs = restricted_projection @ current_f_block @ highest
    projected_h = highest @ (highest.conj().T @ h_on_highest)
    restricted_rhs = descendant_map @ projected_h / weight
    no_projector_rhs = descendant_map @ h_on_highest / weight
    no_factor_rhs = descendant_map @ projected_h

    return {
        "local": (local_e, local_f, local_h),
        "weight": weight,
        "global": (raising, lowering, coroot),
        "currents": (current_e, current_f, current_h),
        "source": source,
        "target": target,
        "highest": highest,
        "gram": gram,
        "restricted_gram": restricted_gram,
        "ward_error": float(np.linalg.norm(
            raising @ current_f - current_f @ raising - current_h
        )),
        "current_f_weight_error": float(np.linalg.norm(
            coroot @ current_f - current_f @ coroot + 2.0 * current_f
        )),
        "current_h_weight_error": float(np.linalg.norm(
            coroot @ current_h - current_h @ coroot
        )),
        "hamiltonian_error": float(np.linalg.norm(
            ring["H"] @ raising - raising @ ring["H"]
        )),
        "full_error": float(np.linalg.norm(full_lhs - full_rhs)),
        "restricted_error": float(np.linalg.norm(
            restricted_lhs - restricted_rhs
        )),
        "scalar_full_defect": float(np.linalg.norm(
            full_lhs - scalar_full_rhs
        )),
        "no_projector_defect": float(np.linalg.norm(
            restricted_lhs - no_projector_rhs
        )),
        "no_factor_defect": float(np.linalg.norm(
            restricted_lhs - no_factor_rhs
        )),
    }


def exact_diagonalization_gate(ring: dict[str, object],
                               certificates: list[dict[str, object]]) -> None:
    eigenvalues = np.linalg.eigvalsh(ring["H"])
    rounded = np.rint(eigenvalues).astype(int)
    expected = {0: 15, 2: 36, 4: 18, 6: 12}
    measured = {
        value: int(np.sum(rounded == value)) for value in expected
    }
    spectral_error = max(
        abs(float(value) - float(eigenvalue))
        for value, eigenvalue in zip(rounded, eigenvalues)
    )
    require(measured == expected,
            f"SIDXG-C1 SU(3) ED multiplicities {measured} != {expected}")
    require(spectral_error < TOL,
            f"SIDXG-C1 SU(3) ED spectral error {spectral_error:.3e}")
    for certificate in certificates:
        require(certificate["ward_error"] < TOL,
                f"SIDXG-C1 Ward error {certificate['ward_error']:.3e}")
        require(certificate["current_f_weight_error"] < TOL,
                "SIDXG-C1 lowering current has off-weight leakage")
        require(certificate["current_h_weight_error"] < TOL,
                "SIDXG-C1 coroot current has off-weight leakage")
        require(certificate["hamiltonian_error"] < TOL,
                "SIDXG-C1 root charge does not commute with Hamiltonian")
    print(f"SIDXG-C1 PASS: SU(3) ED {measured}; "
          f"spectral error={spectral_error:.2e}; root currents covariant")


def multiplicity_gate(certificates: list[dict[str, object]],
                      weight_two: dict[str, object]) -> None:
    for certificate in certificates:
        source_dimension = len(certificate["source"])
        highest_dimension = certificate["highest"].shape[1]
        eigenvalues = np.linalg.eigvalsh(certificate["gram"])
        ones = int(np.sum(np.isclose(eigenvalues, 1.0, atol=TOL)))
        fours = int(np.sum(np.isclose(eigenvalues, 4.0, atol=TOL)))
        require(source_dimension == 16 and highest_dimension == 12,
                "SIDXG-C2 wrong lambda=1 sector/highest dimensions")
        require((ones, fours) == (12, 4),
                f"SIDXG-C2 full Gram spectrum counts {(ones, fours)}")
        restricted_error = np.linalg.norm(
            certificate["restricted_gram"] - np.eye(highest_dimension)
        )
        require(restricted_error < TOL,
                f"SIDXG-C2 restricted Gram not lambda*I: "
                f"{restricted_error:.3e}")
    eigenvalues_two = np.linalg.eigvalsh(weight_two["gram"])
    twos = int(np.sum(np.isclose(eigenvalues_two, 2.0, atol=TOL)))
    sixes = int(np.sum(np.isclose(eigenvalues_two, 6.0, atol=TOL)))
    highest_two = weight_two["highest"].shape[1]
    restricted_two_error = np.linalg.norm(
        weight_two["restricted_gram"] - 2.0 * np.eye(highest_two)
    )
    require(len(weight_two["source"]) == 10 and highest_two == 9,
            "SIDXG-C2 wrong lambda=2 sector/highest dimensions")
    require((twos, sixes) == (9, 1),
            f"SIDXG-C2 lambda=2 Gram spectrum counts {(twos, sixes)}")
    require(restricted_two_error < TOL,
            f"SIDXG-C2 lambda=2 restricted Gram error "
            f"{restricted_two_error:.3e}")
    print("SIDXG-C2 PASS: lambda=1 dim=16/hw=12, "
          "spec(A)={1^12,4^4}; lambda=2 dim=10/hw=9, "
          "spec(A)={2^9,6^1}, A_hw=lambda*I")


def identity_gate(certificates: list[dict[str, object]],
                  weight_two: dict[str, object], mode: str | None) -> None:
    all_certificates = certificates + [weight_two]
    maximum_full = max(float(c["full_error"]) for c in all_certificates)
    maximum_restricted = max(
        float(c["restricted_error"]) for c in all_certificates
    )
    minimum_scalar_defect = min(
        float(c["scalar_full_defect"]) for c in certificates
    )
    minimum_projector_defect = min(
        float(c["no_projector_defect"]) for c in certificates
    )
    normalization_defect = float(weight_two["no_factor_defect"])
    require(abs(minimum_scalar_defect - math.sqrt(40.0)) < 2.0e-10,
            f"SIDXG-C3 scalar mutation defect {minimum_scalar_defect:.12f}")
    require(minimum_projector_defect > 8.0,
            "SIDXG-C3 projector mutation is not live")
    require(abs(normalization_defect - math.sqrt(24.0)) < 2.0e-10,
            f"SIDXG-C3 1/lambda mutation defect {normalization_defect:.12f}")

    tested_full = (minimum_scalar_defect
                   if mode == "--red-scalar-full" else maximum_full)
    tested_restricted = (minimum_projector_defect
                         if mode == "--red-drop-hw-projector"
                         else maximum_restricted)
    if mode == "--red-drop-hw-factor":
        tested_restricted = normalization_defect
    require(tested_full < TOL,
            f"SIDXG-C3 full-sector identity error {tested_full:.3e}")
    require(tested_restricted < TOL,
            f"SIDXG-C3 highest-weight identity error {tested_restricted:.3e}")
    print(f"SIDXG-C3 PASS: full={maximum_full:.2e} "
          f"restricted={maximum_restricted:.2e}; scalar defect="
          f"{minimum_scalar_defect:.9f}; no-Pi defect="
          f"{minimum_projector_defect:.9f}; no-1/lambda defect="
          f"{normalization_defect:.9f}")


def su2_reduction_gate() -> None:
    r2 = load_module("soft_index_r2_for_g", HERE / "soft_index_r2_check.py")
    expected_rows = {
        1: (1.0, 2.0, 2.0j),
        2: (2.0, 6.0, 4.0j),
        3: (3.0, 10.0, 6.0j),
    }
    maximum = 0.0
    rows = []
    for two_s, expected in expected_rows.items():
        data = r2.spin_ring(two_s, number_sites=4)
        hard = r2.one_magnon(data, math.pi / 2.0)
        source = r2.sector_indices(data, 1)
        target = r2.sector_indices(data, 2)
        descendant_map = data["Sm"][np.ix_(target, source)]
        gram = descendant_map.conj().T @ descendant_map
        projection = descendant_map @ np.linalg.solve(
            gram, descendant_map.conj().T
        )
        lhs = projection @ (data["Jm"] @ hard)[target]
        descendant = (data["Sm"] @ hard)[target]
        velocity = 2.0 * float(data["S"])
        norm = float(np.vdot(descendant, descendant).real)
        residue = np.vdot(descendant, lhs)
        measured = (velocity, norm, residue)
        maximum = max(
            maximum,
            abs(measured[0] - expected[0]),
            abs(measured[1] - expected[1]),
            abs(measured[2] - expected[2]),
        )
        rows.append((float(data["S"]), velocity, norm, residue))
    require(maximum < TOL,
            f"SIDXG-C4 SU(2) reduction mismatch {maximum:.3e}")
    print(f"SIDXG-C4 PASS: SIDXR2-C2 rows {rows}; max error={maximum:.2e}")


def centralizer_weyl_gate(ring: dict[str, object],
                          certificates: list[dict[str, object]],
                          mode: str | None) -> None:
    e01, f01, h01 = certificates[0]["local"]
    e02, f02, h02 = certificates[1]["local"]
    central = np.diag([1.0, 1.0, -2.0]).astype(complex)
    central_error = max(
        float(np.linalg.norm(central @ operator - operator @ central))
        for operator in (e01, f01, h01)
    )
    h_generator = np.zeros((3, 3), dtype=complex)
    h_generator[1, 2] = 1.0
    full_h_defect = float(np.linalg.norm(
        h01 @ h_generator - h_generator @ h01
    ))

    weyl = np.zeros((3, 3), dtype=complex)
    weyl[0, 0] = 1.0
    weyl[2, 1] = 1.0
    weyl[1, 2] = -1.0
    weyl_error = max(
        float(np.linalg.norm(weyl @ source @ weyl.conj().T - target))
        for source, target in zip((e01, f01, h01), (e02, f02, h02))
    )
    global_weyl = tensor_power(weyl, int(ring["N"]))
    current_weyl_error = max(
        float(np.linalg.norm(
            global_weyl @ source @ global_weyl.conj().T - target
        ))
        for source, target in zip(
            certificates[0]["currents"], certificates[1]["currents"]
        )
    )
    nonorthogonal = float(np.trace(h01 @ h02).real)

    require(central_error < TOL,
            f"SIDXG-C5 centralizer commutator {central_error:.3e}")
    tested_h = 0.0 if mode != "--red-force-h-block" else full_h_defect
    require(tested_h < TOL,
            f"SIDXG-C5 full-H block mutation detected: {tested_h:.3e}")
    require(full_h_defect > 0.9,
            "SIDXG-C5 full-H obstruction is not live")
    require(weyl_error < TOL and current_weyl_error < TOL,
            f"SIDXG-C5 Weyl errors local={weyl_error:.3e}, "
            f"current={current_weyl_error:.3e}")
    require(abs(nonorthogonal - 1.0) < TOL,
            f"SIDXG-C5 root inner product {nonorthogonal}")
    print(f"SIDXG-C5 PASS: centralizer={central_error:.1e}; "
          f"full-H defect={full_h_defect:.3f}; Weyl="
          f"{max(weyl_error, current_weyl_error):.1e}; "
          f"tr(H01 H02)={nonorthogonal:.1f}")


def shared_su3_overlap_gate(ring: dict[str, object]) -> None:
    g4 = load_module("soft_index_g4_for_g", HERE / "soft_index_g4_check.py")
    data = g4.su3_ring()
    hard = g4.su3_hard(data, math.pi / 2.0)

    local_e, local_f, local_h = local_root(0, 1)
    raising = global_sum(local_e, int(ring["N"]))
    lowering = global_sum(local_f, int(ring["N"]))
    coroot = global_sum(local_h, int(ring["N"]))
    current_f = current_zero_mode(ring, local_f)
    current_h = current_zero_mode(ring, local_h)

    weights = np.rint(np.diag(coroot).real).astype(int)
    source = np.where(weights == 3)[0]
    target = np.where(weights == 1)[0]
    descendant_map = lowering[np.ix_(target, source)]
    gram = descendant_map.conj().T @ descendant_map
    root_projection = descendant_map @ np.linalg.solve(
        gram, descendant_map.conj().T
    )
    root_projected = np.zeros(hard.size, dtype=complex)
    root_projected[target] = root_projection @ (current_f @ hard)[target]

    central_diagonal = np.diag(data["C"]).real
    central_source = np.where(
        np.isclose(central_diagonal, 5.0 / 3.0, atol=TOL)
    )[0]
    central_target = np.where(
        np.isclose(central_diagonal, 2.0 / 3.0, atol=TOL)
    )[0]
    central_map = data["Q"][np.ix_(central_target, central_source)]
    central_projection = central_map @ np.linalg.pinv(central_map, rcond=TOL)
    central_projected = np.zeros(hard.size, dtype=complex)
    central_projected[central_target] = central_projection @ (
        data["J"] @ hard
    )[central_target]

    charge_created = lowering @ hard
    coefficient = np.vdot(charge_created, root_projected) / np.vdot(
        charge_created, charge_created
    )
    denominator = np.vdot(hard, current_h @ hard)
    index = np.vdot(charge_created, root_projected) / denominator
    root_rhs = np.zeros(hard.size, dtype=complex)
    root_rhs[target] = descendant_map @ np.linalg.solve(
        gram, (current_h @ hard)[source]
    )

    gram_error = float(np.linalg.norm(gram - 3.0 * np.eye(source.size)))
    overlap_error = float(np.linalg.norm(root_projected - central_projected))
    coefficient_error = abs(coefficient - 2.0j / 3.0)
    denominator_error = abs(denominator - 2.0j)
    index_error = abs(index - 1.0)
    ward_error = float(np.linalg.norm(root_projected - root_rhs))
    highest_error = float(np.linalg.norm(raising @ hard))
    current_match_error = float(np.linalg.norm(current_f - data["J"]))

    require((source.size, target.size) == (4, 16),
            "SIDXG-C6 wrong root source/target dimensions")
    require(gram_error < TOL,
            f"SIDXG-C6 spec(A) != {{3^4}}: {gram_error:.3e}")
    require(highest_error < TOL,
            f"SIDXG-C6 hard state is not root-highest: {highest_error:.3e}")
    require(current_match_error < TOL,
            f"SIDXG-C6 G1/G4 current mismatch {current_match_error:.3e}")
    require(overlap_error < TOL,
            f"SIDXG-C6 root/central projection mismatch {overlap_error:.3e}")
    require(coefficient_error < TOL,
            f"SIDXG-C6 coefficient mismatch {coefficient_error:.3e}")
    require(denominator_error < TOL,
            f"SIDXG-C6 denominator mismatch {denominator_error:.3e}")
    require(index_error < TOL,
            f"SIDXG-C6 normalized-index mismatch {index_error:.3e}")
    require(ward_error < TOL,
            f"SIDXG-C6 root Gram/Ward residual {ward_error:.3e}")
    print(
        "SIDXG-C6 PASS: lambda=3, spec(A)={3^4}; root/central mismatch="
        f"{overlap_error:.2e}; coefficient={coefficient}; "
        f"denominator={denominator}; index={index}; Ward={ward_error:.2e}"
    )


def main() -> None:
    arguments = sys.argv[1:]
    require(len(arguments) <= 1, "red modes are mutually exclusive")
    mode = arguments[0] if arguments else None
    require(mode is None or mode in RED_MODES, f"unknown mode: {mode}")

    code_shape_gate()
    ring = su3_ring()
    certificates = [
        root_certificate(ring, 0, 1),
        root_certificate(ring, 0, 2),
    ]
    weight_two = root_certificate(ring, 0, 1, weight=2)
    exact_diagonalization_gate(ring, certificates)
    multiplicity_gate(certificates, weight_two)
    identity_gate(certificates, weight_two, mode)
    su2_reduction_gate()
    centralizer_weyl_gate(ring, certificates, mode)
    shared_su3_overlap_gate(ring)

    if mode is not None:
        print(f"RED SURVIVED UNDETECTED: {mode}")
        raise SystemExit(0)
    print("ALL SIDXG GATES PASS")


if __name__ == "__main__":
    main()
