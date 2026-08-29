#!/usr/bin/env python3
"""Red-capable finite checks for the compact-G memory scope shard.

SG-C1 samples covariant Hermitian Lie-algebra tensors and invariant density
tensors for the nonabelian compact group U(1) x SU(2).  It checks that the
vacuum functional vanishes on su(2) while it may survive on the centre.

SG-C2 samples a genuinely noncommuting two-time joint TPM protocol for three
commuting on-site circle charges.  It checks affine-offset cancellation and
Z^3 support.  ``--red`` biases the density tensor away from covariance and
changes the final TPM background; both registered gates must fail.
"""

from __future__ import annotations

import argparse
import sys

import numpy as np


TOL = 2.0e-11


class GateFailure(RuntimeError):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise GateFailure(message)


def block_diag(blocks: list[np.ndarray]) -> np.ndarray:
    size = sum(block.shape[0] for block in blocks)
    out = np.zeros((size, size), dtype=complex)
    offset = 0
    for block in blocks:
        width = block.shape[0]
        out[offset : offset + width, offset : offset + width] = block
        offset += width
    return out


def spin_generators(j: float) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    dim = int(round(2 * j + 1))
    ms = np.array([j - k for k in range(dim)], dtype=float)
    jp = np.zeros((dim, dim), dtype=complex)
    for col, m in enumerate(ms):
        if col > 0:
            jp[col - 1, col] = np.sqrt((j - m) * (j + m + 1))
    jm = jp.conj().T
    return (jp + jm) / 2, (jp - jm) / (2j), np.diag(ms)


def haar_unitary(rng: np.random.Generator, dim: int) -> np.ndarray:
    raw = rng.normal(size=(dim, dim)) + 1j * rng.normal(size=(dim, dim))
    qmat, rmat = np.linalg.qr(raw)
    diagonal = np.diag(rmat)
    phases = np.ones(dim, dtype=complex)
    nonzero = np.abs(diagonal) > 0
    phases[nonzero] = diagonal[nonzero] / np.abs(diagonal[nonzero])
    return qmat @ np.diag(phases.conj())


def invariant_sample(
    rng: np.random.Generator, red: bool
) -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    # (multiplicity, spin, central U(1) weight); the SU(2) part is nonabelian.
    sectors = [(3, 0.5, 1.0), (2, 1.0, -2.0), (2, 0.0, 4.0)]
    rho_blocks: list[np.ndarray] = []
    centre_blocks: list[np.ndarray] = []
    jx_blocks: list[np.ndarray] = []
    jy_blocks: list[np.ndarray] = []
    jz_blocks: list[np.ndarray] = []

    for multiplicity, spin, central_weight in sectors:
        jx, jy, jz = spin_generators(spin)
        irrep_dim = jx.shape[0]
        raw = rng.normal(size=(multiplicity, multiplicity)) + 1j * rng.normal(
            size=(multiplicity, multiplicity)
        )
        multiplicity_density = raw @ raw.conj().T + 0.4 * np.eye(multiplicity)
        rho_blocks.append(np.kron(multiplicity_density, np.eye(irrep_dim)))
        centre_blocks.append(central_weight * np.eye(multiplicity * irrep_dim))
        jx_blocks.append(np.kron(np.eye(multiplicity), jx))
        jy_blocks.append(np.kron(np.eye(multiplicity), jy))
        jz_blocks.append(np.kron(np.eye(multiplicity), jz))

    rho = block_diag(rho_blocks)
    centre = block_diag(centre_blocks)
    jx = block_diag(jx_blocks)
    jy = block_diag(jy_blocks)
    jz = block_diag(jz_blocks)
    rho /= np.trace(rho)

    change_basis = haar_unitary(rng, rho.shape[0])
    rho = change_basis @ rho @ change_basis.conj().T
    centre = change_basis @ centre @ change_basis.conj().T
    jx = change_basis @ jx @ change_basis.conj().T
    jy = change_basis @ jy @ change_basis.conj().T
    jz = change_basis @ jz @ change_basis.conj().T

    if red:
        # Positive but non-covariant density tensor: K rho K biases J_z.
        scale = max(1.0, np.linalg.norm(jz, ord=2))
        bias = np.eye(rho.shape[0]) + 0.18 * jz / scale
        rho = bias @ rho @ bias
        rho /= np.trace(rho)

    return rho, centre, jx, jy, jz


def covariant_product_mps_sample(
    rng: np.random.Generator, red: bool
) -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    """Random chi=1 covariant MPS tensor for U(1) x SU(2).

    The physical representation has four singlets of central weight 2 and one
    spin-1 multiplet of central weight -1.  A random vector in the singlet
    multiplicity space is an injective chi=1 tensor and an H-character line.
    A random basis change makes all displayed tensors dense.
    """
    spin_x, spin_y, spin_z = spin_generators(1.0)
    zero_singlets = np.zeros((4, 4), dtype=complex)
    jx = block_diag([zero_singlets, spin_x])
    jy = block_diag([zero_singlets, spin_y])
    jz = block_diag([zero_singlets, spin_z])
    centre = block_diag([2.0 * np.eye(4), -1.0 * np.eye(3)])

    tensor = np.zeros(7, dtype=complex)
    tensor[:4] = rng.normal(size=4) + 1j * rng.normal(size=4)
    tensor /= np.linalg.norm(tensor)
    if red:
        # Add a highest-weight triplet component: the tensor leaves the
        # invariant character line and acquires a semisimple density.
        tensor[4] += 0.22
        tensor /= np.linalg.norm(tensor)

    change_basis = haar_unitary(rng, 7)
    tensor = change_basis @ tensor
    centre = change_basis @ centre @ change_basis.conj().T
    jx = change_basis @ jx @ change_basis.conj().T
    jy = change_basis @ jy @ change_basis.conj().T
    jz = change_basis @ jz @ change_basis.conj().T
    return tensor, centre, jx, jy, jz


def check_c1(red: bool) -> dict[str, float]:
    rng = np.random.default_rng(20260829)
    max_covariance = 0.0
    max_lie_residue = 0.0
    max_semisimple_density = 0.0
    max_ad_invariance = 0.0
    max_central_density = 0.0
    max_mps_covariance = 0.0
    max_mps_semisimple_density = 0.0
    max_mps_central_residue = 0.0

    for _ in range(24):
        rho, centre, jx, jy, jz = invariant_sample(rng, red)
        generators = (jx, jy, jz)
        for generator in generators:
            max_covariance = max(
                max_covariance, np.linalg.norm(rho @ generator - generator @ rho)
            )
            max_semisimple_density = max(
                max_semisimple_density, abs(np.trace(rho @ generator))
            )
        max_lie_residue = max(
            max_lie_residue, np.linalg.norm(jx @ jy - jy @ jx - 1j * jz)
        )
        max_central_density = max(max_central_density, abs(np.trace(rho @ centre)))

        axis = rng.normal(size=3)
        axis /= np.linalg.norm(axis)
        theta = rng.uniform(-np.pi, np.pi)
        rotation_generator = axis[0] * jx + axis[1] * jy + axis[2] * jz
        values, vectors = np.linalg.eigh(rotation_generator)
        unitary = (vectors * np.exp(1j * theta * values)) @ vectors.conj().T
        probe_coefficients = rng.normal(size=3)
        probe = sum(c * g for c, g in zip(probe_coefficients, generators))
        transformed = unitary @ probe @ unitary.conj().T
        max_ad_invariance = max(
            max_ad_invariance,
            abs(np.trace(rho @ transformed) - np.trace(rho @ probe)),
        )

        tensor, mps_centre, mps_jx, mps_jy, mps_jz = covariant_product_mps_sample(
            rng, red
        )
        for generator in (mps_jx, mps_jy, mps_jz):
            max_mps_covariance = max(max_mps_covariance, np.linalg.norm(generator @ tensor))
            max_mps_semisimple_density = max(
                max_mps_semisimple_density, abs(np.vdot(tensor, generator @ tensor))
            )
        max_mps_central_residue = max(
            max_mps_central_residue,
            np.linalg.norm((mps_centre - 2.0 * np.eye(7)) @ tensor),
        )

    require(
        max(max_semisimple_density, max_mps_semisimple_density) < TOL,
        "SG-C1 semisimple-density gate: "
        f"density={max(max_semisimple_density, max_mps_semisimple_density):.3e}, "
        f"state_covariance={max_covariance:.3e}, mps_covariance={max_mps_covariance:.3e}",
    )
    require(max_covariance < TOL, f"SG-C1 covariance residue={max_covariance:.3e}")
    require(
        max_mps_covariance < TOL,
        f"SG-C1 random MPS covariance residue={max_mps_covariance:.3e}",
    )
    require(
        max_mps_central_residue < TOL,
        f"SG-C1 random MPS central-character residue={max_mps_central_residue:.3e}",
    )
    require(max_lie_residue < TOL, f"SG-C1 Lie residue={max_lie_residue:.3e}")
    require(
        max_ad_invariance < TOL,
        f"SG-C1 Ad-invariance residue={max_ad_invariance:.3e}",
    )
    require(
        max_central_density > 5.0e-2,
        f"SG-C1 central direction was accidentally silent: {max_central_density:.3e}",
    )
    return {
        "covariance": max_covariance,
        "lie": max_lie_residue,
        "semisimple_density": max_semisimple_density,
        "ad_invariance": max_ad_invariance,
        "central_density": max_central_density,
        "mps_covariance": max_mps_covariance,
        "mps_semisimple_density": max_mps_semisimple_density,
        "mps_central_character": max_mps_central_residue,
    }


def check_c2(red: bool) -> dict[str, float]:
    rng = np.random.default_rng(29082026)
    weights = np.array(
        [[0, 0, 0], [1, -1, 2], [-2, 1, 1], [3, 2, -1], [-1, -2, 0]],
        dtype=float,
    )
    kappa = np.array([0.5, 0.25, -0.2])
    site_charges = [np.diag(kappa[j] + weights[:, j]) for j in range(3)]
    onsite_commutator = max(
        np.linalg.norm(a @ b - b @ a)
        for a in site_charges
        for b in site_charges
    )

    dim_site = weights.shape[0]
    identity = np.eye(dim_site)
    background = np.array([0.31, -1.17, 0.73])
    window_charges = [
        np.kron(charge, identity)
        + np.kron(identity, charge)
        - background[j] * np.eye(dim_site**2)
        for j, charge in enumerate(site_charges)
    ]
    same_time_commutator = max(
        np.linalg.norm(a @ b - b @ a)
        for a in window_charges
        for b in window_charges
    )

    basis_weights = np.array(
        [weights[a] + weights[b] for a in range(dim_site) for b in range(dim_site)]
    )
    affine_offset = 2 * kappa - background
    eigenvalues_minus = basis_weights + affine_offset
    eigenvalues_plus = eigenvalues_minus.copy()
    if red:
        # Measuring a different final background violates the same-window premise.
        eigenvalues_plus[:, 0] += np.sqrt(2.0) / 10.0

    dimension = dim_site**2
    u_minus = haar_unitary(rng, dimension)
    u_plus = haar_unitary(rng, dimension)
    psi = rng.normal(size=dimension) + 1j * rng.normal(size=dimension)
    psi /= np.linalg.norm(psi)
    initial_weights = np.abs(u_minus.conj().T @ psi) ** 2
    transitions = np.abs(u_plus.conj().T @ u_minus) ** 2
    joint_probabilities = transitions * initial_weights[np.newaxis, :]

    probability_residue = abs(np.sum(joint_probabilities) - 1.0)
    max_lattice_residue = 0.0
    active_atoms = 0
    for final_index in range(dimension):
        for initial_index in range(dimension):
            if joint_probabilities[final_index, initial_index] <= 1.0e-14:
                continue
            active_atoms += 1
            escaped = (
                eigenvalues_minus[initial_index] - eigenvalues_plus[final_index]
            )
            max_lattice_residue = max(
                max_lattice_residue, np.max(np.abs(escaped - np.rint(escaped)))
            )

    cross_time_commutator = np.linalg.norm(
        u_minus @ window_charges[0] @ u_minus.conj().T
        @ (u_plus @ window_charges[0] @ u_plus.conj().T)
        - (u_plus @ window_charges[0] @ u_plus.conj().T)
        @ (u_minus @ window_charges[0] @ u_minus.conj().T)
    )
    require(onsite_commutator < TOL, f"SG-C2 on-site commutator={onsite_commutator:.3e}")
    require(
        same_time_commutator < TOL,
        f"SG-C2 same-time joint-PVM commutator={same_time_commutator:.3e}",
    )
    require(probability_residue < TOL, f"SG-C2 probability residue={probability_residue:.3e}")
    require(active_atoms > 0, "SG-C2 TPM law has no active atoms")
    require(
        max_lattice_residue < TOL,
        f"SG-C2 affine-offset cancellation residue={max_lattice_residue:.3e}",
    )
    require(
        cross_time_commutator > 1.0e-3,
        f"SG-C2 cross-time noncommutation was not exercised: {cross_time_commutator:.3e}",
    )
    return {
        "onsite_commutator": onsite_commutator,
        "same_time_commutator": same_time_commutator,
        "probability": probability_residue,
        "lattice": max_lattice_residue,
        "cross_time_commutator": cross_time_commutator,
        "active_atoms": float(active_atoms),
    }


def format_metrics(name: str, metrics: dict[str, float]) -> str:
    body = ", ".join(f"{key}={value:.3e}" for key, value in metrics.items())
    return f"{name} PASS: {body}"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--red", action="store_true")
    args = parser.parse_args()

    checks = (("SG-C1", check_c1), ("SG-C2", check_c2))
    caught = 0
    for name, check in checks:
        try:
            metrics = check(args.red)
            print(format_metrics(name, metrics))
        except GateFailure as exc:
            if args.red:
                caught += 1
                print(f"RED-CAUGHT {name}: {exc}")
            else:
                print(f"FAIL {name}: {exc}", file=sys.stderr)
                return 1

    if args.red:
        if caught != len(checks):
            print(f"FAIL: red mutation caught by {caught}/{len(checks)} gates", file=sys.stderr)
            return 1
        print(f"RED-OK: {caught}/{len(checks)} registered mutations failed")
        return 1

    print("PASS: compact-G scope checks")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
