#!/usr/bin/env python3
"""Red-capable exact checks for ``theory/spt-rebuild.md``.

The checks are finite-dimensional transfer contractions.  They cover the
critic's D2 adjoint counterexample, an explicit injective chi=2 trivial tensor,
the deformability of a bulk soft-charge coefficient inside one non-trivial SPT
phase, and the simultaneous rigidity of the AKLT edge-charge residue.

Run ``python3 -O theory/checks/spt_rebuild_check.py``.  The ``--red`` mutant
reverses the predicted edge charge and must fail.  The ``--red-gauge`` mutant
uses an uncentered rephased U(1) virtual generator and must also fail.  No
Python ``assert`` is used, so optimization cannot disable a check.
"""

from __future__ import annotations

import argparse
import sys

import numpy as np


TOL_EXACT = 2.0e-12
TOL_LIMIT = 2.0e-7

I2 = np.eye(2, dtype=complex)
X = np.array([[0, 1], [1, 0]], dtype=complex)
Y = np.array([[0, -1j], [1j, 0]], dtype=complex)
Z = np.diag([1, -1]).astype(complex)

# Cartesian spin-one basis (|x>, |y>, |z>).  These are the three characters
# of D2.  Group order is e, Rx, Ry, Rz.
D2_PHYSICAL = [
    np.diag([1, 1, 1]).astype(complex),
    np.diag([1, -1, -1]).astype(complex),
    np.diag([-1, 1, -1]).astype(complex),
    np.diag([-1, -1, 1]).astype(complex),
]
def fail(message: str) -> None:
    print(f"FAIL: {message}", file=sys.stderr)
    raise SystemExit(1)


def require(condition: bool, message: str) -> None:
    if not condition:
        fail(message)


def transfer_matrix(tensors: list[np.ndarray]) -> np.ndarray:
    return sum(np.kron(a, a.conj()) for a in tensors)


def transfer_apply(tensors: list[np.ndarray], matrix: np.ndarray) -> np.ndarray:
    return sum(a @ matrix @ a.conj().T for a in tensors)


def inserted_transfer(
    tensors: list[np.ndarray], operator: np.ndarray, matrix: np.ndarray
) -> np.ndarray:
    return sum(
        operator[sp, s] * tensors[s] @ matrix @ tensors[sp].conj().T
        for sp in range(len(tensors))
        for s in range(len(tensors))
    )


def word_map(tensors: list[np.ndarray], length: int = 2) -> np.ndarray:
    words = tensors
    for _ in range(1, length):
        words = [left @ right for left in words for right in tensors]
    return np.stack([word.reshape(-1) for word in words])


def triv_tensor(t: float = 1.0) -> list[np.ndarray]:
    """Exact D2-linear, left-canonical, chi=2 tensor in (x,y,z) order."""
    require(0.0 < t <= 1.0, "trivial tensor path requires 0 < t <= 1")
    off = np.array(
        [[0.0, t * np.sqrt(3.0) / 2.0], [t / 2.0, 0.0]], dtype=complex
    )
    diag = np.diag(
        [np.sqrt(1.0 - t * t / 4.0), np.sqrt(1.0 - 3.0 * t * t / 4.0)]
    ).astype(complex)
    return [off, np.zeros((2, 2), dtype=complex), diag]


def aklt_tensor(b: float) -> list[np.ndarray]:
    """D2- and U(1)-symmetric anisotropic AKLT path in Cartesian basis."""
    require(0.0 < b < 1.0, "AKLT path requires 0 < b < 1")
    a = np.sqrt((1.0 - b * b) / 2.0)
    return [a * X, a * Y, b * Z]


def check_triv_tensor() -> tuple[np.ndarray, int, float, float]:
    tensors = triv_tensor()
    left_residue = np.linalg.norm(
        sum(a.conj().T @ a for a in tensors) - I2, ord=np.inf
    )
    rank = int(np.linalg.matrix_rank(word_map(tensors), tol=TOL_EXACT))
    eigenvalues = np.linalg.eigvals(transfer_matrix(tensors))
    sorted_moduli = np.sort(np.abs(eigenvalues))[::-1]
    gap = float(sorted_moduli[1])
    require(left_residue < TOL_EXACT, f"TRIV canonical residue {left_residue:.3e}")
    require(rank == 4, f"TRIV length-two word rank is {rank}, expected 4")
    require(
        abs(sorted_moduli[0] - 1.0) < TOL_EXACT and gap < 1.0 - 1.0e-10,
        f"TRIV transfer moduli {sorted_moduli}",
    )

    # theta is the character of the product state |z>.  V is the honest
    # representation 1 direct-sum chi with V(Rx)=V(Rz)=Z, V(Ry)=I.
    theta = np.array([1, -1, -1, 1], dtype=complex)
    virtual = [I2, Z, I2, Z]
    covariance_residue = 0.0
    for physical, phase, v in zip(D2_PHYSICAL, theta, virtual):
        for s in range(3):
            lhs = sum(physical[s, sp] * tensors[sp] for sp in range(3))
            rhs = phase * v.conj().T @ tensors[s] @ v
            covariance_residue = max(
                covariance_residue, float(np.linalg.norm(lhs - rhs, ord=np.inf))
            )
    require(
        covariance_residue < TOL_EXACT,
        f"TRIV D2 covariance residue {covariance_residue:.3e}",
    )
    return eigenvalues, rank, left_residue, covariance_residue


def d2_character_multiplicities(virtual: list[np.ndarray]) -> np.ndarray:
    """Multiplicity of the four D2 characters in conjugation on M2."""
    adjoint_character = np.array(
        [abs(np.trace(v)) ** 2 for v in virtual], dtype=float
    )
    character_table = np.array(
        [
            [1, 1, 1, 1],
            [1, 1, -1, -1],
            [1, -1, 1, -1],
            [1, -1, -1, 1],
        ],
        dtype=float,
    )
    return character_table @ adjoint_character / 4.0


def check_d2_counterexample() -> tuple[
    np.ndarray, np.ndarray, np.ndarray, float, float, float
]:
    projective = [I2, X, Y, Z]
    scalar_trivial = [I2, I2, I2, I2]
    tensor_trivial = [I2, Z, I2, Z]
    projective_mult = d2_character_multiplicities(projective)
    trivial_mult = d2_character_multiplicities(scalar_trivial)
    tensor_trivial_mult = d2_character_multiplicities(tensor_trivial)
    require(
        np.linalg.norm(projective_mult - np.ones(4), ord=np.inf) < TOL_EXACT,
        f"projective adjoint multiplicities {projective_mult}",
    )
    require(
        np.linalg.norm(trivial_mult - np.array([4, 0, 0, 0]), ord=np.inf)
        < TOL_EXACT,
        f"trivial adjoint multiplicities {trivial_mult}",
    )
    require(
        np.linalg.norm(tensor_trivial_mult - np.array([2, 0, 2, 0]), ord=np.inf)
        < TOL_EXACT,
        f"explicit TRIV adjoint multiplicities {tensor_trivial_mult}",
    )
    # Two actual closed-contraction scalars: characters Tr Ad(V(Rx)).
    projective_scalar = abs(np.trace(X)) ** 2
    trivial_scalar = abs(np.trace(I2)) ** 2
    tensor_trivial_scalar = abs(np.trace(tensor_trivial[2])) ** 2
    require(
        abs(projective_scalar) < TOL_EXACT and abs(trivial_scalar - 4.0) < TOL_EXACT,
        "closed adjoint-character contraction did not distinguish the lifts",
    )
    require(
        abs(tensor_trivial_scalar - 4.0) < TOL_EXACT,
        "explicit TRIV closed Ad(Ry) scalar is not 4",
    )
    return (
        projective_mult,
        trivial_mult,
        tensor_trivial_mult,
        projective_scalar,
        trivial_scalar,
        tensor_trivial_scalar,
    )


def structure_factor(tensors: list[np.ndarray], k: float) -> float:
    """Infinite-chain connected S^z structure factor for the AKLT path."""
    spin_z = np.array([[0, -1j, 0], [1j, 0, 0], [0, 0, 0]], dtype=complex)
    right = I2 / 2.0
    c0 = np.trace(right @ inserted_transfer(tensors, spin_z @ spin_z, I2)).real
    first = inserted_transfer(tensors, spin_z, I2)
    # The charge channel is one-dimensional.  Read its transfer eigenvalue and
    # first separated correlator directly, then sum the geometric series.
    propagated = transfer_apply(tensors, first)
    lam = float(np.vdot(first, propagated).real / np.vdot(first, first).real)
    c1 = np.trace(right @ inserted_transfer(tensors, spin_z, first)).real
    return float(c0 + 2.0 * c1 * np.real(np.exp(1j * k) / (1.0 - lam * np.exp(1j * k))))


def packet_coefficient(b: float, length: int = 2048, kappa: float = 1.3) -> float:
    """Direct Sd3' bump-packet variance divided by its gradient norm."""
    x = np.arange(-length + 1, length)
    scaled = x / length
    bump = np.exp(-1.0 / (1.0 - scaled * scaled))
    packet = bump * np.exp(1j * kappa * x / length)
    packet /= np.linalg.norm(packet)
    gradient_norm = np.sum(np.abs(np.diff(np.r_[0.0, packet, 0.0])) ** 2)

    c0 = 1.0 - b * b
    lam = 2.0 * b * b - 1.0
    c1 = -(1.0 - b * b) ** 2
    variance = c0
    for separation in range(1, len(packet)):
        correlator = c1 * lam ** (separation - 1)
        if abs(correlator) < 1.0e-18:
            break
        overlap = np.vdot(packet[:-separation], packet[separation:])
        variance += 2.0 * np.real(correlator * overlap)
    return float(variance / gradient_norm)


def check_bulk_deformability() -> tuple[float, float, float, float, float, float]:
    b0 = 1.0 / np.sqrt(3.0)
    b1 = 0.7
    coefficients = []
    numerical = []
    packets = []
    k = 1.0e-3
    for b in (b0, b1):
        tensors = aklt_tensor(b)
        rank = np.linalg.matrix_rank(word_map(tensors), tol=TOL_EXACT)
        require(rank == 4, f"AKLT-path word rank {rank} at b={b}")
        # Exact coefficient C_bulk = lim S_zz(k)/[2(1-cos k)].
        exact = b * b / (4.0 * (1.0 - b * b))
        measured = structure_factor(tensors, k) / (2.0 * (1.0 - np.cos(k)))
        require(
            abs(measured - exact) < TOL_LIMIT,
            f"bulk coefficient at b={b}: measured {measured}, exact {exact}",
        )
        packet = packet_coefficient(b)
        require(
            abs(packet - exact) < TOL_LIMIT,
            f"packet coefficient at b={b}: measured {packet}, exact {exact}",
        )
        coefficients.append(exact)
        numerical.append(measured)
        packets.append(packet)
    require(
        abs(coefficients[1] - coefficients[0]) > 0.1,
        "bulk coefficient failed to vary inside the fixed projective class",
    )
    return (
        coefficients[0], coefficients[1], numerical[0], numerical[1],
        packets[0], packets[1]
    )


def edge_charge_operator(tensors: list[np.ndarray], length: int) -> np.ndarray:
    """Normalized left-register compression of sum_{x=0}^{length-1} S^z_x."""
    spin_z = np.array([[0, -1j, 0], [1j, 0, 0], [0, 0, 0]], dtype=complex)
    right = I2 / 2.0
    insertion = inserted_transfer(tensors, spin_z, right)
    accumulated = np.zeros((2, 2), dtype=complex)
    term = insertion
    for _ in range(length):
        accumulated += term
        term = transfer_apply(tensors, term)
    # The identity compression is r=I/2, so canonical register normalization
    # is r^{-1/2} accumulated r^{-1/2} = 2 accumulated.
    return 2.0 * accumulated


def check_edge_residue(red: bool) -> tuple[float, float, float]:
    max_formula_error = 0.0
    max_limit_error = 0.0
    final_eigenvalues = np.zeros(2)
    for b in (1.0 / np.sqrt(3.0), 0.7):
        tensors = aklt_tensor(b)
        lam = 2.0 * b * b - 1.0
        for length in (1, 2, 4, 8, 24):
            measured = edge_charge_operator(tensors, length)
            expected_sign = 1.0 if red else -1.0
            expected = expected_sign * 0.5 * (1.0 - lam**length) * Z
            max_formula_error = max(
                max_formula_error, float(np.linalg.norm(measured - expected, ord=np.inf))
            )
        final = edge_charge_operator(tensors, 64)
        final_eigenvalues = np.linalg.eigvalsh(final)
        max_limit_error = max(
            max_limit_error,
            float(np.linalg.norm(final + 0.5 * Z, ord=np.inf)),
        )
    require(
        max_formula_error < TOL_EXACT,
        f"finite-window edge-residue formula error {max_formula_error:.3e}",
    )
    require(
        max_limit_error < TOL_EXACT,
        f"edge residue did not converge to -Z/2: {max_limit_error:.3e}",
    )
    spin_z = np.array([[0, -1j, 0], [1j, 0, 0], [0, 0, 0]], dtype=complex)
    product = [
        np.zeros((1, 1), dtype=complex),
        np.zeros((1, 1), dtype=complex),
        np.ones((1, 1), dtype=complex),
    ]
    product_residue = inserted_transfer(product, spin_z, np.ones((1, 1)))
    require(
        np.linalg.norm(product_residue, ord=np.inf) < TOL_EXACT,
        f"O(2)-trivial product edge charge {product_residue}",
    )
    return max_formula_error, max_limit_error, float(np.max(np.abs(final_eigenvalues)))


def check_phase_gauge_centering(red_gauge: bool) -> tuple[float, float]:
    """The Hermitian partial charge sees the centered, not raw, U(1) lift."""
    tensors = aklt_tensor(1.0 / np.sqrt(3.0))
    measured = edge_charge_operator(tensors, 64)

    # Build D10's partial charge independently from its anti-Hermitian one-site
    # generator -i S^z.  The declared dual-left register reverses the endpoint
    # Lie-algebra orientation relative to this bulk insertion.
    spin_z = np.array([[0, -1j, 0], [1j, 0, 0], [0, 0, 0]], dtype=complex)
    right = I2 / 2.0
    term = inserted_transfer(tensors, -1j * spin_z, right)
    accumulated = np.zeros((2, 2), dtype=complex)
    for _ in range(64):
        accumulated += term
        term = transfer_apply(tensors, term)
    antihermitian_partial = -2.0 * accumulated
    require(
        np.linalg.norm(
            antihermitian_partial.conj().T + antihermitian_partial,
            ord=np.inf,
        )
        < TOL_EXACT,
        "D10 partial charge was not anti-Hermitian",
    )
    require(
        np.linalg.norm(antihermitian_partial - 1j * measured, ord=np.inf)
        < TOL_EXACT,
        "D10 partial-charge compression did not equal i times the measured charge",
    )
    require(
        np.linalg.norm(-1j * antihermitian_partial - measured, ord=np.inf)
        < TOL_EXACT,
        "-iQ did not reproduce the Hermitian registered charge",
    )

    base_generator = -0.5j * Z
    phase_slope = 0.37
    rephased_generator = base_generator + 1j * phase_slope * I2
    centered_generator = rephased_generator - np.trace(
        right @ rephased_generator
    ) * I2
    centered_prediction = -1j * centered_generator
    uncentered_prediction = -1j * rephased_generator
    uncentered_defect = float(
        np.linalg.norm(uncentered_prediction - centered_prediction, ord=np.inf)
    )
    require(
        uncentered_defect > 0.3,
        "U(1) phase-gauge mutation was too small to test centering",
    )

    predicted = uncentered_prediction if red_gauge else centered_prediction
    error = float(np.linalg.norm(measured - predicted, ord=np.inf))
    require(
        error < TOL_EXACT,
        "phase-gauge endpoint error {:.3e}; the uncentered convention is invalid".format(
            error
        ),
    )
    return error, uncentered_defect


def check_projective_and_boundary_register() -> tuple[float, float]:
    projective_commutator = np.linalg.norm(X @ Z + Z @ X, ord=np.inf)
    triv_virtual = [I2, Z, I2, Z]
    # The chosen list order is (e,Rx,Ry,Rz), with Rx*Ry=Rz.
    linear_residue = max(
        np.linalg.norm(Z @ I2 - Z, ord=np.inf),
        np.linalg.norm(I2 @ Z - Z, ord=np.inf),
        np.linalg.norm(Z @ Z - I2, ord=np.inf),
    )
    require(
        projective_commutator < TOL_EXACT,
        f"AKLT Pauli anticommutator residue {projective_commutator:.3e}",
    )
    require(
        linear_residue < TOL_EXACT,
        f"TRIV virtual representation multiplication residue {linear_residue:.3e}",
    )
    # The allowed trivial-edge splitting K commutes with the linear D2 action.
    boundary_k = np.diag([0.0, 1.0]).astype(complex)
    boundary_residue = max(
        np.linalg.norm(boundary_k @ v - v @ boundary_k, ord=np.inf)
        for v in triv_virtual
    )
    require(
        boundary_residue < TOL_EXACT,
        f"TRIV boundary Hamiltonian symmetry residue {boundary_residue:.3e}",
    )

    # Verify the explicit physical two-site parent and boundary terms (2.3)--
    # (2.5), not just the abstract register penalty.
    tensors = triv_tensor()
    gamma = np.stack(
        [(tensors[s] @ tensors[t]).reshape(-1) for s in range(3) for t in range(3)]
    )
    gram_values, gram_vectors = np.linalg.eigh(gamma.conj().T @ gamma)
    require(
        np.min(gram_values) > TOL_EXACT,
        f"TRIV Gamma_2 Gram minimum {np.min(gram_values):.3e}",
    )
    inverse_sqrt = (
        gram_vectors
        @ np.diag(gram_values ** -0.5)
        @ gram_vectors.conj().T
    )
    isometry = gamma @ inverse_sqrt
    parent = np.eye(9, dtype=complex) - isometry @ isometry.conj().T
    boundary = isometry @ np.kron(boundary_k, I2) @ isometry.conj().T
    physical_residue = 0.0
    for physical in D2_PHYSICAL:
        physical_two = np.kron(physical, physical)
        physical_residue = max(
            physical_residue,
            float(np.linalg.norm(physical_two @ parent - parent @ physical_two, ord=np.inf)),
            float(
                np.linalg.norm(
                    physical_two @ boundary - boundary @ physical_two, ord=np.inf
                )
            ),
        )
    require(
        physical_residue < TOL_EXACT,
        f"physical parent/boundary D2 residue {physical_residue:.3e}",
    )

    # A finite AKLT symmetry string needs its remote WI endpoint compensated.
    # With V(Rz)^-1 at the cut the registered contraction is exactly Z; without
    # it the scalar overlap decays as (-1/3)^L.
    aklt = aklt_tensor(1.0 / np.sqrt(3.0))
    right = I2 / 2.0
    compensated = Z @ right
    uncompensated = right
    compensated_residue = 0.0
    for _ in range(8):
        compensated = inserted_transfer(aklt, D2_PHYSICAL[3], compensated)
        uncompensated = inserted_transfer(aklt, D2_PHYSICAL[3], uncompensated)
        compensated_residue = max(
            compensated_residue,
            float(np.linalg.norm(2.0 * compensated - Z, ord=np.inf)),
        )
    require(
        compensated_residue < TOL_EXACT,
        f"compensated endpoint residue {compensated_residue:.3e}",
    )
    require(
        np.linalg.norm(2.0 * uncompensated, ord=np.inf) < 2.0e-3,
        "uncompensated AKLT string failed to decay in the endpoint test",
    )
    return projective_commutator, max(
        boundary_residue, physical_residue, compensated_residue
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--red", action="store_true", help="reverse the edge-residue sign; must fail"
    )
    parser.add_argument(
        "--red-gauge",
        action="store_true",
        help="use the uncentered rephased U(1) generator; must fail",
    )
    args = parser.parse_args()

    eigenvalues, rank, canonical, covariance = check_triv_tensor()
    (
        projective_mult,
        trivial_mult,
        tensor_trivial_mult,
        closed_projective,
        closed_trivial,
        tensor_closed_trivial,
    ) = (
        check_d2_counterexample()
    )
    c0, c1, n0, n1, p0, p1 = check_bulk_deformability()
    edge_formula, edge_limit, edge_abs = check_edge_residue(args.red)
    gauge_error, uncentered_defect = check_phase_gauge_centering(args.red_gauge)
    projective_residue, boundary_residue = check_projective_and_boundary_register()

    print("SPT rebuild exact-check certificate")
    print(
        "TRIV: rank={}, transfer={}, canonical={:.3e}, covariance={:.3e}".format(
            rank,
            np.array2string(np.sort(np.real_if_close(eigenvalues))),
            canonical,
            covariance,
        )
    )
    print(
        "D2 Ad multiplicities: projective={}, scalar-trivial={}; "
        "Tr Ad(Rx)={:.1f} vs {:.1f}".format(
            projective_mult.astype(int),
            trivial_mult.astype(int),
            closed_projective,
            closed_trivial,
        )
    )
    print(
        "explicit TRIV Ad multiplicities={}; Tr Ad(Ry)={:.1f} vs projective 0.0".format(
            tensor_trivial_mult.astype(int), tensor_closed_trivial
        )
    )
    print(
        "bulk C: {:.12f} -> {:.12f} (k=1e-3: {:.12f}, {:.12f})".format(
            c0, c1, n0, n1
        )
    )
    print("packet L=2048: {:.12f}, {:.12f}".format(p0, p1))
    print(
        "edge: finite formula={:.3e}, limit={:.3e}, |q_edge|={:.12f}".format(
            edge_formula, edge_limit, edge_abs
        )
    )
    print(
        "U(1) phase gauge: centered error={:.3e}, uncentered defect={:.3e}".format(
            gauge_error, uncentered_defect
        )
    )
    print(
        "multiplication/boundary residues: {:.3e}, {:.3e}".format(
            projective_residue, boundary_residue
        )
    )
    print("ALL SPT REBUILD CHECKS PASS")


if __name__ == "__main__":
    main()
