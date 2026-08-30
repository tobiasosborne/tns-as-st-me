#!/usr/bin/env python3
"""Exact fixed-point toric-code PEPS and PT1--PT4 checker.

Green:
    python3 -O peps_pt_check.py
Registered red mutation:
    python3 -O peps_pt_check.py --red pt2-mix

The checker uses no bare assert.  The red mutation replaces the electric
endpoint by a coherent electric/magnetic mixture; PT2 must reject it.
"""

from __future__ import annotations

import argparse
import itertools
import sys

import numpy as np


TOL = 2.0e-12
Z2X2 = tuple(itertools.product(range(2), repeat=2))


def add_label(a: tuple[int, int], b: tuple[int, int]) -> tuple[int, int]:
    return (a[0] ^ b[0], a[1] ^ b[1])


def kron_all(items: list[np.ndarray]) -> np.ndarray:
    out = np.array([[1.0]], dtype=complex)
    for item in items:
        out = np.kron(out, item)
    return out


class Gates:
    def __init__(self) -> None:
        self.failed: list[str] = []

    def upper(self, name: str, value: float, bound: float = TOL) -> None:
        ok = bool(np.isfinite(value) and value <= bound)
        print(f"{name}: {'PASS' if ok else 'FAIL'} residual={value:.3e} bound={bound:.1e}")
        if not ok:
            self.failed.append(name)

    def lower(self, name: str, value: float, bound: float) -> None:
        ok = bool(np.isfinite(value) and value >= bound)
        print(f"{name}: {'PASS' if ok else 'FAIL'} value={value:.6f} lower={bound:.6f}")
        if not ok:
            self.failed.append(name)


def edge_tables(length: int) -> tuple[dict[tuple[str, int, int], int], list[tuple[int, int]]]:
    edge_id: dict[tuple[str, int, int], int] = {}
    endpoints: list[tuple[int, int]] = []

    def vertex(x: int, y: int) -> int:
        return (y % length) * length + (x % length)

    for y in range(length):
        for x in range(length):
            edge_id[("h", x, y)] = len(endpoints)
            endpoints.append((vertex(x, y), vertex(x + 1, y)))
            edge_id[("v", x, y)] = len(endpoints)
            endpoints.append((vertex(x, y), vertex(x, y + 1)))
    return edge_id, endpoints


def toric_fixed_point(length: int = 3) -> dict[str, object]:
    """Contract the explicit copy/difference tensor network by color summation."""
    edge_id, endpoints = edge_tables(length)
    vertices = length * length
    edges = len(endpoints)
    dimension = 1 << edges

    # Delta_{lurd}=1 iff all four virtual colors agree.
    copy4 = np.zeros((2, 2, 2, 2), dtype=int)
    copy4[(0, 0, 0, 0)] = 1
    copy4[(1, 1, 1, 1)] = 1

    # D^s_{ab}=delta_{s,a+b}; addition is in Z_2.
    difference = np.zeros((2, 2, 2), dtype=int)
    for s, a, b in itertools.product(range(2), repeat=3):
        difference[s, a, b] = int(s == (a ^ b))

    raw = np.zeros(dimension, dtype=complex)
    for colors in range(1 << vertices):
        configuration = 0
        for edge, (v0, v1) in enumerate(endpoints):
            c0 = (colors >> v0) & 1
            c1 = (colors >> v1) & 1
            configuration |= (c0 ^ c1) << edge
        raw[configuration] += 1.0
    state = raw / np.linalg.norm(raw)

    def star_mask(x: int, y: int) -> int:
        names = (("h", x, y), ("h", (x - 1) % length, y),
                 ("v", x, y), ("v", x, (y - 1) % length))
        return sum(1 << edge_id[name] for name in names)

    def plaquette_mask(x: int, y: int) -> int:
        names = (("h", x, y), ("v", (x + 1) % length, y),
                 ("h", x, (y + 1) % length), ("v", x, y))
        return sum(1 << edge_id[name] for name in names)

    return {
        "copy4": copy4,
        "difference": difference,
        "raw": raw,
        "state": state,
        "length": length,
        "edges": edges,
        "edge_id": edge_id,
        "star_mask": star_mask,
        "plaquette_mask": plaquette_mask,
    }


def apply_x(state: np.ndarray, mask: int) -> np.ndarray:
    indices = np.arange(state.size, dtype=np.int64)
    return state[indices ^ mask]


def parity_array(size: int, mask: int) -> np.ndarray:
    return np.fromiter(
        ((int(index & mask).bit_count() & 1) for index in range(size)),
        dtype=np.int8,
        count=size,
    )


def apply_z(state: np.ndarray, mask: int) -> np.ndarray:
    signs = 1 - 2 * parity_array(state.size, mask)
    return signs * state


def apply_pauli(state: np.ndarray, xmask: int, zmask: int) -> np.ndarray:
    # The possible global phase is immaterial to every sector test.
    return apply_x(apply_z(state, zmask), xmask)


def physical_projector(
    state: np.ndarray,
    label: tuple[int, int],
    electric_loop: int,
    magnetic_loop: int,
) -> np.ndarray:
    out = state + ((-1) ** label[0]) * apply_x(state, electric_loop)
    out = out + ((-1) ** label[1]) * apply_z(out, magnetic_loop)
    return 0.25 * out


def check_peps_and_physical_endpoint(gates: Gates) -> dict[str, float]:
    data = toric_fixed_point(3)
    copy4 = data["copy4"]
    difference = data["difference"]
    raw = data["raw"]
    state = data["state"]
    length = int(data["length"])
    edges = int(data["edges"])
    edge_id = data["edge_id"]
    star_mask = data["star_mask"]
    plaquette_mask = data["plaquette_mask"]

    local_error = 0.0
    for l, u, r, d in itertools.product(range(2), repeat=4):
        expected = int(l == u == r == d)
        local_error = max(local_error, abs(int(copy4[l, u, r, d]) - expected))
        local_error = max(
            local_error,
            abs(int(copy4[l ^ 1, u ^ 1, r ^ 1, d ^ 1]) - int(copy4[l, u, r, d])),
        )
    for s, a, b in itertools.product(range(2), repeat=3):
        expected = int(s == (a ^ b))
        local_error = max(local_error, abs(int(difference[s, a, b]) - expected))
        local_error = max(
            local_error,
            abs(int(difference[s, a ^ 1, b ^ 1]) - int(difference[s, a, b])),
        )
    gates.upper("PEPS-PT-C0-explicit-tensors", local_error)

    nonzero = np.flatnonzero(np.abs(raw) > TOL)
    contraction_error = max(
        abs(len(nonzero) - (1 << (length * length - 1))),
        float(np.max(np.abs(raw[nonzero] - 2.0))),
        abs(float(np.vdot(state, state).real) - 1.0),
    )
    gates.upper("PEPS-PT-C1-exact-contraction", float(contraction_error))

    stabilizer_error = 0.0
    for y in range(length):
        for x in range(length):
            stabilizer_error = max(
                stabilizer_error,
                float(np.linalg.norm(apply_x(state, star_mask(x, y)) - state)),
                float(np.linalg.norm(apply_z(state, plaquette_mask(x, y)) - state)),
            )
    gates.upper("PEPS-PT-C2-toric-stabilizers", stabilizer_error)

    # A one-cell disk register.  A single direct/dual edge has one endpoint
    # in the selected vertex/plaquette and the other endpoint outside.
    electric_loop = star_mask(0, 0)
    magnetic_loop = plaquette_mask(0, 0)
    crossing_edge = int(edge_id[("h", 0, 0)])
    endpoint_error = 0.0
    for x in Z2X2:
        endpoint = apply_pauli(
            state,
            (1 << crossing_edge) if x[1] else 0,
            (1 << crossing_edge) if x[0] else 0,
        )
        for y in Z2X2:
            projected = physical_projector(endpoint, y, electric_loop, magnetic_loop)
            target = endpoint if y == x else np.zeros_like(endpoint)
            endpoint_error = max(endpoint_error, float(np.linalg.norm(projected - target)))
    gates.upper("PEPS-PT-C3-microscopic-pure-endpoint", endpoint_error)

    print(
        "PEPS witness: L=3, E=18, nonzero amplitudes="
        f"{len(nonzero)}, common raw amplitude=2, state norm={np.linalg.norm(state):.12f}"
    )
    return {
        "stabilizer_error": stabilizer_error,
        "physical_endpoint_error": endpoint_error,
        "edges": float(edges),
    }


def tube_data(boundary_length: int = 4) -> dict[str, object]:
    one = np.eye(2, dtype=complex)
    x_pauli = np.array([[0.0, 1.0], [1.0, 0.0]], dtype=complex)
    z_pauli = np.array([[1.0, 0.0], [0.0, -1.0]], dtype=complex)
    identity_boundary = np.eye(1 << boundary_length, dtype=complex)
    global_shift = kron_all([x_pauli] * boundary_length)
    z_on_cut = kron_all([z_pauli] + [one] * (boundary_length - 1))
    flux_zero = np.array([[1.0, 0.0], [0.0, 0.0]], dtype=complex)
    flux_one = np.array([[0.0, 0.0], [0.0, 1.0]], dtype=complex)

    projectors: dict[tuple[int, int], np.ndarray] = {}
    ribbons: dict[tuple[int, int], np.ndarray] = {}
    for q, h in Z2X2:
        character = 0.5 * (identity_boundary + ((-1) ** q) * global_shift)
        flux = flux_zero if h == 0 else flux_one
        projectors[(q, h)] = np.kron(character, flux)
        ribbons[(q, h)] = np.kron(
            z_on_cut if q else identity_boundary,
            x_pauli if h else one,
        )

    cat_plus = np.zeros(1 << boundary_length, dtype=complex)
    cat_plus[0] = 1.0 / np.sqrt(2.0)
    cat_plus[-1] = 1.0 / np.sqrt(2.0)
    vacuum_endpoint = np.kron(cat_plus, np.array([1.0, 0.0], dtype=complex))
    return {
        "projectors": projectors,
        "ribbons": ribbons,
        "vacuum_endpoint": vacuum_endpoint,
        "dimension": 2 * (1 << boundary_length),
    }


def check_tube_pt(gates: Gates, red: str | None) -> dict[str, float]:
    data = tube_data(4)
    projectors = data["projectors"]
    ribbons = data["ribbons"]
    vacuum_endpoint = data["vacuum_endpoint"]
    dimension = int(data["dimension"])
    identity = np.eye(dimension, dtype=complex)

    pt1_error = float(np.linalg.norm(sum(projectors.values()) - identity))
    for a in Z2X2:
        for b in Z2X2:
            target = projectors[a] if a == b else np.zeros_like(identity)
            pt1_error = max(
                pt1_error,
                float(np.linalg.norm(projectors[a] @ projectors[b] - target)),
                float(np.linalg.norm(projectors[a] - projectors[a].conj().T)),
            )
    gates.upper("PEPS-PT-C4-PT1-tube-PVM", pt1_error)

    pt2_error = 0.0
    for x in Z2X2:
        endpoint = ribbons[x] @ vacuum_endpoint
        if red == "pt2-mix" and x == (1, 0):
            endpoint = (
                ribbons[(1, 0)] @ vacuum_endpoint
                + ribbons[(0, 1)] @ vacuum_endpoint
            ) / np.sqrt(2.0)
        for y in Z2X2:
            target = endpoint if y == x else np.zeros_like(endpoint)
            pt2_error = max(
                pt2_error,
                float(np.linalg.norm(projectors[y] @ endpoint - target)),
            )
    gates.upper("PEPS-PT-C5-PT2-pure-endpoint", pt2_error)

    zipper_error = 0.0
    selection_error = 0.0
    minimum_allowed_block = float("inf")
    for x in Z2X2:
        for y in Z2X2:
            zipper_error = max(
                zipper_error,
                float(np.linalg.norm(ribbons[x] @ ribbons[y] - ribbons[add_label(x, y)])),
            )
        for a in Z2X2:
            expected_b = add_label(x, a)
            for b in Z2X2:
                block = projectors[b] @ ribbons[x] @ projectors[a]
                if b == expected_b:
                    selection_error = max(
                        selection_error,
                        float(np.linalg.norm(block - ribbons[x] @ projectors[a])),
                    )
                    minimum_allowed_block = min(minimum_allowed_block, float(np.linalg.norm(block)))
                else:
                    selection_error = max(selection_error, float(np.linalg.norm(block)))
    gates.upper("PEPS-PT-C6-PT3-zipper-associator", zipper_error)
    gates.upper("PEPS-PT-C7-PT3-fusion-module", selection_error)
    gates.lower("PEPS-PT-C8-PT3-allowed-liveness", minimum_allowed_block, 1.0)

    pt4_error = 0.0
    weights = np.arange(1, dimension + 1, dtype=float)
    rho = np.diag(weights / np.sum(weights)).astype(complex)
    for x in Z2X2:
        pt4_error = max(
            pt4_error,
            float(np.linalg.norm(ribbons[x].conj().T @ ribbons[x] - identity)),
        )
        probability = 0.0
        for a in Z2X2:
            for b in Z2X2:
                block = projectors[b] @ ribbons[x] @ projectors[a]
                probability += float(np.trace(block @ rho @ block.conj().T).real)
        pt4_error = max(pt4_error, abs(probability - 1.0))
    gates.upper("PEPS-PT-C9-PT4-unitary-instrument", pt4_error)

    print(
        "Tube witness: boundary N=4, dimension=32, four D(Z2) projectors, "
        f"minimum allowed block Frobenius norm={minimum_allowed_block:.6f}"
    )
    return {
        "pt1_error": pt1_error,
        "pt2_error": pt2_error,
        "pt3_error": max(zipper_error, selection_error),
        "pt4_error": pt4_error,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--red", choices=("pt2-mix",), default=None)
    args = parser.parse_args()

    print(f"MODE: {'RED ' + args.red if args.red else 'GREEN'}")
    gates = Gates()
    check_peps_and_physical_endpoint(gates)
    check_tube_pt(gates, args.red)
    if gates.failed:
        print("FAILED GATES: " + ", ".join(gates.failed))
        if args.red:
            print("RED MUTATION DETECTED")
        return 1
    if args.red:
        print("RED SURVIVED UNDETECTED")
        return 2
    print("ALL PEPS-PT GATES PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
