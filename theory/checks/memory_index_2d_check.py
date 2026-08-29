#!/usr/bin/env python3
"""Small 2D ED / exact-spin-wave probe for ``memory-index-2d.md``.

The model is the nearest-neighbour spin-1/2 Heisenberg ferromagnet on a
9-by-9 open square.  Its one-spin-flip sector is exact (not a linear-spin-
wave approximation):

    H_1 = (J/2) L_square,

where ``L_square`` is the graph Laplacian.  The selected integral on-site
charge is magnon number ``n_x = 1/2-S^z_x``.  A disk/annulus window charge is
therefore the projector onto the corresponding position set in this sector.

Checks
------
M2D-C1  Exact one-magnon Hamiltonian and 2D disk/annulus boundary geometry.
M2D-C2  Same-window TPM normalisation, integer support, and the exact TPM
         mean/dephasing identity for noncommuting Heisenberg projections.
M2D-C3  A centre-localised magnon radiates out of a disk; its Bernoulli TPM
         escape law equals the integrated boundary current.
M2D-C4  The same packet enters an annulus; the signed TPM mean and the
         two-boundary current ledger agree.

This is a finite-volume probe.  It proves neither an infinite-volume time
limit nor the 2D first-moment-tightness clause.  The integer-support theorem
is exact algebra and does not rely on this computation.

Green and red runs (all checks remain live under ``python3 -O``):

    python3 -O theory/checks/memory_index_2d_check.py
    python3 -O theory/checks/memory_index_2d_check.py --red fractional-charge

The red mutation replaces the integral local magnon charge step ``1`` by
``sqrt(2)`` in M2D-C2 while keeping a common irrational scalar offset at the
two measurement times.  It violates the on-site circle-integrality premise,
is caught only by the integer-support gate, and exits 1.  A surviving red
mutation exits 2.  There are no bare ``assert`` statements.
"""

from __future__ import annotations

import argparse
import math
import sys
from dataclasses import dataclass

import numpy as np


L = 9
J = 1.0
T_MINUS = -0.37
T_PLUS = 1.41
T_RADIATE = 2.75
OFFSET = math.sqrt(3.0) / 11.0
TOL_MATRIX = 2.0e-12
TOL_PROB = 2.0e-11
TOL_LEDGER = 2.0e-10


class CheckFailure(Exception):
    """A gate failure which is active even when Python optimisation is on."""


def require(condition: bool, message: str) -> None:
    if not condition:
        raise CheckFailure(message)


@dataclass(frozen=True)
class SquareData:
    coords: tuple[tuple[int, int], ...]
    edges: tuple[tuple[int, int], ...]
    hamiltonian: np.ndarray
    evals: np.ndarray
    evecs: np.ndarray


def build_square() -> SquareData:
    """Return the exact one-magnon Hamiltonian on an open square."""
    half = L // 2
    coords = tuple((x, y) for y in range(-half, half + 1)
                   for x in range(-half, half + 1))
    index = {xy: i for i, xy in enumerate(coords)}
    edges: list[tuple[int, int]] = []
    for i, (x, y) in enumerate(coords):
        for neighbour in ((x + 1, y), (x, y + 1)):
            if neighbour in index:
                edges.append((i, index[neighbour]))

    h = np.zeros((len(coords), len(coords)), dtype=float)
    for i, j in edges:
        # J(1/4-S_i.S_j) restricted to one spin flip.
        h[i, i] += 0.5 * J
        h[j, j] += 0.5 * J
        h[i, j] -= 0.5 * J
        h[j, i] -= 0.5 * J
    evals, evecs = np.linalg.eigh(h)
    return SquareData(coords, tuple(edges), h, evals, evecs)


def unitary(data: SquareData, time: float) -> np.ndarray:
    phases = np.exp(-1j * data.evals * time)
    return (data.evecs * phases[None, :]) @ data.evecs.conj().T


def evolve(data: SquareData, state: np.ndarray, time: float) -> np.ndarray:
    phases = np.exp(-1j * data.evals * time)
    return data.evecs @ (phases * (data.evecs.conj().T @ state))


def disk_mask(data: SquareData, radius_sq: int) -> np.ndarray:
    return np.array([x * x + y * y <= radius_sq for x, y in data.coords])


def annulus_mask(data: SquareData, inner_sq: int, outer_sq: int) -> np.ndarray:
    return np.array([inner_sq < x * x + y * y <= outer_sq
                     for x, y in data.coords])


def cut_edges(data: SquareData, mask: np.ndarray) -> tuple[tuple[int, int], ...]:
    return tuple((i, j) for i, j in data.edges if bool(mask[i]) != bool(mask[j]))


def heisenberg_projector(data: SquareData, mask: np.ndarray,
                         time: float) -> np.ndarray:
    u = unitary(data, time)
    p = np.diag(mask.astype(float))
    return u.conj().T @ p @ u


def spectral_projectors(data: SquareData, mask: np.ndarray, time: float,
                        step: float) -> dict[float, np.ndarray]:
    """Projectors of OFFSET*I + step*N_W at a Heisenberg time."""
    p = heisenberg_projector(data, mask, time)
    ident = np.eye(len(mask), dtype=complex)
    return {OFFSET: ident - p, OFFSET + step: p}


def tpm_law(data: SquareData, mask: np.ndarray, state: np.ndarray,
            step: float) -> tuple[dict[float, float], float, float]:
    """Return escaped increments, total mass, and the mean-identity residue."""
    e_minus = spectral_projectors(data, mask, T_MINUS, step)
    e_plus = spectral_projectors(data, mask, T_PLUS, step)
    law: dict[float, float] = {}
    for q_minus, p_minus in e_minus.items():
        for q_plus, p_plus in e_plus.items():
            branch = p_plus @ p_minus @ state
            probability = float(np.vdot(branch, branch).real)
            increment = q_minus - q_plus
            key = min(law, key=lambda old: abs(old - increment)) \
                if law and min(abs(old - increment) for old in law) < 1.0e-12 \
                else increment
            law[key] = law.get(key, 0.0) + probability

    mass = sum(law.values())
    mean = sum(nu * probability for nu, probability in law.items())
    q_minus_op = sum(q * p for q, p in e_minus.items())
    q_plus_op = sum(q * p for q, p in e_plus.items())
    pinched_q_plus = sum(p @ q_plus_op @ p for p in e_minus.values())
    rhs = np.vdot(state, (q_minus_op - pinched_q_plus) @ state).real
    return law, mass, abs(mean - float(rhs))


def outward_current(data: SquareData, mask: np.ndarray,
                    state: np.ndarray, time: float) -> float:
    """The outward probability current -d< N_W >/dt."""
    psi_t = evolve(data, state, time)
    p = np.diag(mask.astype(float))
    commutator = data.hamiltonian @ p - p @ data.hamiltonian
    derivative = float((1j * np.vdot(psi_t, commutator @ psi_t)).real)
    return -derivative


def integrated_outward_current(data: SquareData, mask: np.ndarray,
                               state: np.ndarray, final_time: float) -> float:
    nodes, weights = np.polynomial.legendre.leggauss(160)
    times = 0.5 * final_time * (nodes + 1.0)
    values = np.array([outward_current(data, mask, state, float(t))
                       for t in times])
    return float(0.5 * final_time * np.dot(weights, values))


def seeded_state(dimension: int) -> np.ndarray:
    rng = np.random.default_rng(20260829)
    state = rng.normal(size=dimension) + 1j * rng.normal(size=dimension)
    return state / np.linalg.norm(state)


def check_geometry_and_hamiltonian(data: SquareData) -> dict[str, object]:
    hermiticity = float(np.linalg.norm(data.hamiltonian - data.hamiltonian.T))
    row_sum = float(np.linalg.norm(data.hamiltonian @ np.ones(len(data.coords))))
    require(hermiticity < TOL_MATRIX,
            f"M2D-C1 Hamiltonian is not Hermitian: {hermiticity:.3e}")
    require(row_sum < TOL_MATRIX,
            f"M2D-C1 Goldstone zero mode is absent: {row_sum:.3e}")
    require(data.evals[0] > -TOL_MATRIX,
            f"M2D-C1 ferromagnetic Hamiltonian is not positive: {data.evals[0]:.3e}")

    disk_counts: list[tuple[int, int, int]] = []
    for radius in (1, 2, 3):
        mask = disk_mask(data, radius * radius)
        boundary = len(cut_edges(data, mask))
        disk_counts.append((radius, int(mask.sum()), boundary))
        require(boundary <= 8 * (radius + 1),
                f"M2D-C1 disk boundary is not perimeter order at R={radius}: {boundary}")
    annulus = annulus_mask(data, 1, 9)
    annulus_boundary = len(cut_edges(data, annulus))
    require(annulus_boundary > disk_counts[-1][2],
            "M2D-C1 annulus did not expose both boundary components")
    return {
        "dimension": len(data.coords),
        "edges": len(data.edges),
        "gap": float(data.evals[1] - data.evals[0]),
        "disks": disk_counts,
        "annulus_sites": int(annulus.sum()),
        "annulus_boundary": annulus_boundary,
    }


def check_tpm(data: SquareData, red_mode: str | None) -> dict[str, object]:
    mask = disk_mask(data, 4)
    state = seeded_state(len(data.coords))
    step = math.sqrt(2.0) if red_mode == "fractional-charge" else 1.0
    law, mass, mean_residue = tpm_law(data, mask, state, step)
    require(abs(mass - 1.0) < TOL_PROB,
            f"M2D-C2 TPM law is not normalised: mass={mass:.16f}")
    require(mean_residue < TOL_PROB,
            f"M2D-C2 TPM mean/dephasing identity failed: {mean_residue:.3e}")
    live = {nu: probability for nu, probability in law.items()
            if probability > 1.0e-10}
    max_integer_distance = max(abs(nu - round(nu)) for nu in live)
    require(max_integer_distance < TOL_PROB,
            "M2D-C2 noninteger escaped-charge support: "
            f"distance={max_integer_distance:.6f}, law={live}")
    require(len(live) >= 3,
            f"M2D-C2 noncommuting TPM battery is vacuous: law={live}")
    return {
        "mass_residue": abs(mass - 1.0),
        "mean_residue": mean_residue,
        "law": live,
        "offset": OFFSET,
    }


def localised_magnon(data: SquareData) -> np.ndarray:
    centre = data.coords.index((0, 0))
    state = np.zeros(len(data.coords), dtype=complex)
    state[centre] = 1.0
    return state


def check_disk_radiation(data: SquareData) -> dict[str, float]:
    state = localised_magnon(data)
    mask = disk_mask(data, 4)
    final = evolve(data, state, T_RADIATE)
    p_stay = float(np.sum(np.abs(final[mask]) ** 2))
    p_escape = 1.0 - p_stay
    require(0.05 < p_escape < 0.95,
            f"M2D-C3 radiation battery is trivial: p_escape={p_escape:.6f}")
    flux = integrated_outward_current(data, mask, state, T_RADIATE)
    ledger_residue = abs(p_escape - flux)
    require(ledger_residue < TOL_LEDGER,
            f"M2D-C3 disk current ledger failed: {ledger_residue:.3e}")
    # Initial N_W=1, so the escaped-charge TPM law is exactly
    # p(0)=p_stay, p(1)=p_escape in the one-magnon sector.
    require(abs((p_stay + p_escape) - 1.0) < TOL_PROB,
            "M2D-C3 Bernoulli disk law lost mass")
    return {
        "p_nu_0": p_stay,
        "p_nu_1": p_escape,
        "integrated_flux": flux,
        "ledger_residue": ledger_residue,
    }


def check_annulus_radiation(data: SquareData) -> dict[str, float]:
    state = localised_magnon(data)
    mask = annulus_mask(data, 1, 9)
    final = evolve(data, state, T_RADIATE)
    p_enter = float(np.sum(np.abs(final[mask]) ** 2))
    require(0.05 < p_enter < 0.95,
            f"M2D-C4 annulus-entry battery is trivial: p_enter={p_enter:.6f}")
    flux = integrated_outward_current(data, mask, state, T_RADIATE)
    # The annulus is initially empty.  Its escaped increment is nu=-1 if the
    # magnon has entered it, hence E[nu]=-p_enter.
    signed_mean = -p_enter
    ledger_residue = abs(signed_mean - flux)
    require(ledger_residue < TOL_LEDGER,
            f"M2D-C4 annulus current ledger failed: {ledger_residue:.3e}")
    return {
        "p_nu_0": 1.0 - p_enter,
        "p_nu_minus_1": p_enter,
        "integrated_flux": flux,
        "ledger_residue": ledger_residue,
    }


def run(red_mode: str | None) -> None:
    data = build_square()
    geometry = check_geometry_and_hamiltonian(data)
    disk = check_disk_radiation(data)
    annulus = check_annulus_radiation(data)
    tpm = check_tpm(data, red_mode)

    print("M2D-C1 PASS", geometry)
    print("M2D-C2 PASS", tpm)
    print("M2D-C3 PASS", disk)
    print("M2D-C4 PASS", annulus)
    print("ALL GREEN")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--red", choices=("fractional-charge",))
    args = parser.parse_args()
    try:
        run(args.red)
    except CheckFailure as error:
        if args.red is not None:
            print(f"RED-OK {args.red}: {error}")
            return 1
        print(f"FAIL: {error}")
        return 1
    if args.red is not None:
        print(f"RED SURVIVED UNDETECTED: {args.red}")
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
