#!/usr/bin/env python3
"""ML2 finite-ring completeness audit, including singular Bethe sectors.

The candidate basis is built momentum fiber by momentum fiber.  The full
two-down-spin Hamiltonian is assembled independently in the coordinate basis.
All checks use explicit failures so that ``python -O`` is equally strict.
"""

from __future__ import annotations

import itertools
import sys

import numpy as np


J = 1.271
SIZES = (6, 10, 11, 12, 13, 14, 16, 18, 20, 22, 26)
TOL = 3.0e-10


def fail(message: str) -> None:
    print(f"FAIL: {message}", file=sys.stderr)
    raise SystemExit(1)


def ring_hamiltonian(n_sites: int) -> tuple[np.ndarray, list[tuple[int, int]]]:
    basis = list(itertools.combinations(range(n_sites), 2))
    index = {state: column for column, state in enumerate(basis)}
    matrix = np.zeros((len(basis), len(basis)), dtype=float)
    for column, state in enumerate(basis):
        occupied = set(state)
        for x in range(n_sites):
            y = (x + 1) % n_sites
            if (x in occupied) == (y in occupied):
                continue
            moved = (occupied - {x, y}) | ({y} if x in occupied else {x})
            matrix[column, column] += J / 2.0
            matrix[index[tuple(sorted(moved))], column] -= J / 2.0
    return matrix, basis


def momentum_labels(n_sites: int) -> range:
    half = n_sites // 2
    if n_sites % 2 == 0:
        return range(-half + 1, half + 1)
    return range(-half, half + 1)


def fiber_matrix(n_sites: int, label: int) -> tuple[np.ndarray, float]:
    """Return the center-gauge relative Jacobi block divided by J."""
    momentum = 2.0 * np.pi * label / n_sites
    coupling = float(np.cos(momentum / 2.0))
    if n_sites % 2:
        length = (n_sites - 1) // 2
        block = np.diag([1.0] + [2.0] * (length - 1))
        for r in range(length - 1):
            block[r, r + 1] = block[r + 1, r] = -coupling
        block[-1, -1] -= ((-1) ** label) * coupling
        return block, coupling

    length = n_sites // 2
    if label % 2:
        block = np.diag([1.0] + [2.0] * (length - 2))
        for r in range(length - 2):
            block[r, r + 1] = block[r + 1, r] = -coupling
    else:
        block = np.diag([1.0] + [2.0] * (length - 1))
        for r in range(length - 2):
            block[r, r + 1] = block[r + 1, r] = -coupling
        block[-2, -1] = block[-1, -2] = -np.sqrt(2.0) * coupling
    return block, coupling


def full_vector(
    n_sites: int,
    label: int,
    reduced: np.ndarray,
    basis: list[tuple[int, int]],
) -> np.ndarray:
    """Embed a normalized relative vector into the full momentum sector."""
    momentum = 2.0 * np.pi * label / n_sites
    sigma = (-1) ** label
    half = n_sites // 2
    relative: dict[int, complex] = {}
    for offset, value in enumerate(reduced, start=1):
        if n_sites % 2 == 0 and label % 2 == 0 and offset == half:
            relative[offset] = np.sqrt(2.0) * value
        else:
            relative[offset] = value
        if n_sites - offset != offset:
            relative[n_sites - offset] = sigma * relative[offset]
    if n_sites % 2 == 0 and label % 2:
        relative[half] = 0.0
    vector = np.asarray(
        [
            np.exp(1j * momentum * (x + (y - x) / 2.0))
            * relative[y - x]
            / np.sqrt(n_sites)
            for x, y in basis
        ],
        dtype=complex,
    )
    norm = np.linalg.norm(vector)
    if abs(norm - 1.0) > 2.0e-12:
        fail(f"bad fiber embedding norm N={n_sites}, m={label}: {norm}")
    return vector


def pi_fiber_vectors(n_sites: int) -> list[tuple[str, float, np.ndarray]]:
    """Relative basis for K=pi: singular contact plus nonzero D7 waves."""
    length = n_sites // 2
    label = length
    dimension = length if label % 2 == 0 else length - 1
    contact = np.zeros(dimension)
    contact[0] = 1.0
    rows: list[tuple[str, float, np.ndarray]] = [("singular", 1.0, contact)]

    if label % 2 == 0:
        momenta = [(j + 0.5) * np.pi / (length - 1) for j in range(length - 1)]
    else:
        momenta = [j * np.pi / (length - 1) for j in range(1, length - 1)]
    for q in momenta:
        f = np.asarray(
            [-np.sin((r - 1) * q) / np.sin(q) for r in range(1, dimension + 1)]
        )
        if label % 2 == 0:
            f[-1] /= np.sqrt(2.0)
        f /= np.linalg.norm(f)
        kind = "descendant" if abs(q - np.pi / 2.0) < 2.0e-12 else "pi_degenerate"
        rows.append((kind, 2.0, f))
    if len(rows) != dimension:
        fail(f"wrong pi-fiber size N={n_sites}: {len(rows)} != {dimension}")
    return rows


def charge_created_vector(
    n_sites: int,
    soft: float,
    hard: float,
    basis: list[tuple[int, int]],
) -> np.ndarray:
    """Construct Q_soft|hard> directly from (R3)."""
    return np.asarray(
        [
            (
                np.exp(1j * (soft * x + hard * y))
                + np.exp(1j * (hard * x + soft * y))
            )
            / np.sqrt(n_sites)
            for x, y in basis
        ]
    )


def singular_contact_vector(
    n_sites: int, basis: list[tuple[int, int]]
) -> np.ndarray:
    """Construct the separately normalized singular vector (12)."""
    vector = np.zeros(len(basis), dtype=complex)
    index = {state: column for column, state in enumerate(basis)}
    for x in range(n_sites):
        pair = tuple(sorted((x, (x + 1) % n_sites)))
        vector[index[pair]] += (-1) ** x / np.sqrt(n_sites)
    return vector


def coincident_zero_audit(
    n_sites: int, basis: list[tuple[int, int]]
) -> tuple[int, float]:
    """Build each formal coincident D7 wave and count the zero vectors."""
    zero_count = 0
    maximum_error = 0.0
    for root_number in range(n_sites):
        momentum = (2 * root_number + 1) * np.pi / n_sites
        k_1 = momentum
        k_2 = momentum
        z = np.exp(1j * momentum)
        incoming_amplitude = 1.0
        outgoing_amplitude = -(z * z - 2.0 * z + 1.0) / (
            z * z - 2.0 * z + 1.0
        )
        coordinate_wave = np.asarray(
            [
                outgoing_amplitude * np.exp(1j * (k_1 * x + k_2 * y))
                + incoming_amplitude * np.exp(1j * (k_2 * x + k_1 * y))
                for x, y in basis
            ]
        )
        periodic_error = abs(z**n_sites + 1.0)
        wave_norm = np.linalg.norm(coordinate_wave)
        maximum_error = max(maximum_error, periodic_error, wave_norm)
        if periodic_error <= TOL and wave_norm <= TOL:
            zero_count += 1
    return zero_count, maximum_error


def audit(n_sites: int) -> dict[str, float | int]:
    hamiltonian, basis = ring_hamiltonian(n_sites)
    candidates: list[np.ndarray] = []
    energies: list[float] = []
    counts = {
        "descendant": 0,
        "bound": 0,
        "real": 0,
        "singular": 0,
        "pi_degenerate": 0,
    }
    secular_error = 0.0
    singular_overlap_error = 0.0

    for label in momentum_labels(n_sites):
        block, coupling = fiber_matrix(n_sites, label)
        if abs(coupling) < 5.0e-14:
            rows = pi_fiber_vectors(n_sites)
        else:
            values, vectors = np.linalg.eigh(block)
            rows = []
            descendant_energy = 2.0 * (1.0 - coupling * coupling)
            descendant_index = int(np.argmin(abs(values - descendant_energy)))
            if abs(values[descendant_index] - descendant_energy) > 2.0e-11:
                fail(f"missing descendant N={n_sites}, m={label}")
            edge = 2.0 - 2.0 * coupling
            for index, value in enumerate(values):
                if index == descendant_index:
                    kind = "descendant"
                elif value < edge - 2.0e-11:
                    kind = "bound"
                else:
                    kind = "real"
                rows.append((kind, float(value), vectors[:, index]))

                # The contact recurrence is the finite Bethe secular equation.
                x = (2.0 - value) / (2.0 * coupling)
                f = vectors[:, index].copy()
                if n_sites % 2 == 0 and label % 2 == 0:
                    f[-1] *= np.sqrt(2.0)
                extended = np.concatenate(([f[0] / coupling], f))
                local = [
                    extended[r + 1] - 2.0 * x * extended[r] + extended[r - 1]
                    for r in range(1, len(f))
                ]
                secular_error = max(
                    secular_error,
                    abs(f[0] - coupling * extended[0]),
                    max((abs(item) for item in local), default=0.0),
                )

        for kind, energy_over_j, relative in rows:
            counts[kind] += 1
            candidates.append(full_vector(n_sites, label, relative, basis))
            energies.append(J * energy_over_j)

    vectors = np.column_stack(candidates)
    energies_array = np.asarray(energies)
    dimension = n_sites * (n_sites - 1) // 2
    if vectors.shape != (dimension, dimension):
        fail(f"basis has shape {vectors.shape}, expected {(dimension, dimension)}")

    residual = np.linalg.norm(
        hamiltonian @ vectors - vectors * energies_array[np.newaxis, :]
    )
    orthogonality = np.linalg.norm(vectors.conj().T @ vectors - np.eye(dimension))
    projector = np.linalg.norm(vectors @ vectors.conj().T - np.eye(dimension))
    exact_spectrum = np.linalg.eigvalsh(hamiltonian)
    spectral = float(np.max(abs(np.sort(energies_array) - exact_spectrum)))
    if max(residual, orthogonality, projector, spectral, secular_error) > TOL:
        fail(
            f"N={n_sites} residual={residual:.3e} orth={orthogonality:.3e} "
            f"projector={projector:.3e} spectrum={spectral:.3e} "
            f"secular={secular_error:.3e}"
        )
    expected_singular = 1 if n_sites % 2 == 0 else 0
    if (
        counts["descendant"] != n_sites
        or counts["singular"] != expected_singular
    ):
        fail(f"exceptional inventory mismatch N={n_sites}: {counts}")
    if sum(counts.values()) != dimension:
        fail(f"class count mismatch N={n_sites}: {counts}")
    expected_bound = sum(
        1
        for label in momentum_labels(n_sites)
        if 0 < abs(label) < n_sites / 2
        and (
            label % 2 == 0
            or n_sites * (1.0 - np.cos(np.pi * abs(label) / n_sites)) > 2.0
        )
    )
    length = n_sites // 2
    expected_pi_degenerate = 0
    if n_sites % 2 == 0:
        expected_pi_degenerate = length - 2 if length % 2 == 0 else length - 3
    expected_real = (
        dimension
        - n_sites
        - expected_bound
        - expected_singular
        - expected_pi_degenerate
    )
    if (
        counts["bound"] != expected_bound
        or counts["pi_degenerate"] != expected_pi_degenerate
        or counts["real"] != expected_real
    ):
        fail(
            f"analytic class formula mismatch N={n_sites}: {counts}, "
            f"expected real={expected_real}, bound={expected_bound}, "
            f"pi_degenerate={expected_pi_degenerate}"
        )
    coincident_zero_count, coincident_error = coincident_zero_audit(n_sites, basis)
    if coincident_zero_count != n_sites:
        fail(
            f"coincident zero-vector count N={n_sites}: "
            f"{coincident_zero_count} != {n_sites}"
        )
    if coincident_error > TOL:
        fail(f"coincident zero-vector check failed N={n_sites}: {coincident_error}")

    if n_sites % 2 == 0:
        singular = singular_contact_vector(n_sites, basis)
        if abs(np.linalg.norm(singular) - 1.0) > TOL:
            fail(f"singular normalization failed N={n_sites}")
        half = n_sites // 2
        for hard_label in range(1, half):
            soft_label = half - hard_label
            hard = 2.0 * np.pi * hard_label / n_sites
            soft = 2.0 * np.pi * soft_label / n_sites
            overlap = np.vdot(
                singular, charge_created_vector(n_sites, soft, hard, basis)
            )
            expected = 2j * np.cos((hard - soft) / 2.0)
            singular_overlap_error = max(
                singular_overlap_error, abs(overlap - expected)
            )

            off_fiber_soft = 2.0 * np.pi * ((soft_label + 1) % n_sites) / n_sites
            off_fiber_overlap = np.vdot(
                singular,
                charge_created_vector(n_sites, off_fiber_soft, hard, basis),
            )
            singular_overlap_error = max(
                singular_overlap_error, abs(off_fiber_overlap)
            )
        if singular_overlap_error > TOL:
            fail(
                f"singular Q overlap failed N={n_sites}: "
                f"{singular_overlap_error}"
            )

    print(
        f"N={n_sites:2d} dim={dimension:3d} "
        f"real={counts['real']:3d} bound={counts['bound']:2d} "
        f"desc={counts['descendant']:2d} singular={counts['singular']} "
        f"pi-deg={counts['pi_degenerate']:2d} "
        f"coincident-zero={coincident_zero_count:2d}"
    )
    print(
        f"  spectrum={spectral:.3e} residual={residual:.3e} "
        f"orth={orthogonality:.3e} projector={projector:.3e} "
        f"secular={secular_error:.3e} coincident={coincident_error:.3e} "
        f"singular-overlap={singular_overlap_error:.3e}"
    )
    return {**counts, "dimension": dimension, "projector": projector}


def main() -> None:
    for n_sites in SIZES:
        audit(n_sites)
    print("PASS: ML2 finite-ring spectrum, exceptional inventory, and completeness")


if __name__ == "__main__":
    main()
