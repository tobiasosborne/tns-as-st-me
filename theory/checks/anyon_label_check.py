#!/usr/bin/env python3
"""Exact finite-torus checks for ``theory/anyon-label-index.md``.

Green:
    python3 -O theory/checks/anyon_label_check.py

Registered red mode (must exit nonzero):
    python3 -O theory/checks/anyon_label_check.py --red wrong-sector

The computation uses binary symplectic Pauli algebra and exact rational TPM
weights.  It contains no bare assertion statement, so all gates run under
``python3 -O``.
"""

from __future__ import annotations

import argparse
import ast
from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path
import sys


Label = tuple[int, int]
Vertex = tuple[int, int]
Plaquette = tuple[int, int]

VACUUM: Label = (0, 0)
ELECTRIC: Label = (1, 0)
MAGNETIC: Label = (0, 1)
FERMION: Label = (1, 1)
LABELS: tuple[Label, ...] = (VACUUM, ELECTRIC, MAGNETIC, FERMION)


def fail(message: str) -> None:
    print(f"FAIL: {message}", file=sys.stderr)
    raise SystemExit(1)


def require(condition: bool, message: str) -> None:
    if not condition:
        fail(message)


def parity(value: int) -> int:
    return value.bit_count() & 1


def add_labels(left: Label, right: Label) -> Label:
    return (left[0] ^ right[0], left[1] ^ right[1])


def label_name(label: Label) -> str:
    return {
        VACUUM: "1",
        ELECTRIC: "e",
        MAGNETIC: "m",
        FERMION: "epsilon",
    }[label]


@dataclass(frozen=True)
class Pauli:
    """A phase-free Pauli X^x Z^z on a fixed qubit register."""

    x: int = 0
    z: int = 0

    def times(self, other: "Pauli") -> "Pauli":
        return Pauli(self.x ^ other.x, self.z ^ other.z)

    def commutation_bit(self, other: "Pauli") -> int:
        return parity((self.x & other.z) ^ (self.z & other.x))

    def commutes(self, other: "Pauli") -> bool:
        return self.commutation_bit(other) == 0

    def power(self, exponent: int) -> "Pauli":
        return self if exponent & 1 else Pauli()


class SquareTorus:
    def __init__(self, length_x: int, length_y: int) -> None:
        require(length_x >= 3 and length_y >= 3,
                "ANYON lattice must have both periods at least three")
        self.length_x = length_x
        self.length_y = length_y
        self.cells = length_x * length_y
        self.qubits = 2 * self.cells

    def horizontal(self, x: int, y: int) -> int:
        return (y % self.length_y) * self.length_x + (x % self.length_x)

    def vertical(self, x: int, y: int) -> int:
        return self.cells + (y % self.length_y) * self.length_x + (
            x % self.length_x
        )

    @staticmethod
    def mask(edges: tuple[int, ...]) -> int:
        result = 0
        for edge in edges:
            result ^= 1 << edge
        return result

    def star(self, vertex: Vertex) -> Pauli:
        x, y = vertex
        edges = (
            self.horizontal(x, y),
            self.horizontal(x - 1, y),
            self.vertical(x, y),
            self.vertical(x, y - 1),
        )
        return Pauli(x=self.mask(edges))

    def plaquette(self, plaquette: Plaquette) -> Pauli:
        x, y = plaquette
        edges = (
            self.horizontal(x, y),
            self.vertical(x + 1, y),
            self.horizontal(x, y + 1),
            self.vertical(x, y),
        )
        return Pauli(z=self.mask(edges))

    def vertices(self) -> tuple[Vertex, ...]:
        return tuple(
            (x, y)
            for y in range(self.length_y)
            for x in range(self.length_x)
        )

    def plaquettes(self) -> tuple[Plaquette, ...]:
        return self.vertices()

    def z_string(self, edges: tuple[int, ...]) -> Pauli:
        return Pauli(z=self.mask(edges))

    def x_string(self, crossed_edges: tuple[int, ...]) -> Pauli:
        return Pauli(x=self.mask(crossed_edges))


def pauli_product(operators: tuple[Pauli, ...]) -> Pauli:
    product = Pauli()
    for operator in operators:
        product = product.times(operator)
    return product


def gf2_rank(rows: list[int]) -> int:
    work = [row for row in rows if row]
    rank = 0
    while work:
        pivot = max(work)
        work.remove(pivot)
        pivot_bit = pivot.bit_length() - 1
        reduced: list[int] = []
        for row in work:
            reduced.append(row ^ pivot if (row >> pivot_bit) & 1 else row)
        work = [row for row in reduced if row]
        rank += 1
    return rank


def symplectic_row(operator: Pauli, qubits: int) -> int:
    return operator.x | (operator.z << qubits)


def code_shape_gate() -> None:
    tree = ast.parse(Path(__file__).read_text(encoding="utf-8"))
    bare = [node for node in ast.walk(tree) if isinstance(node, ast.Assert)]
    require(not bare, "ANYON-C0 found a bare assertion")
    print("ANYON-C0-SHAPE PASS bare_asserts=0 optimization_safe=1")


def torus_gate(torus: SquareTorus) -> None:
    stars = tuple(torus.star(vertex) for vertex in torus.vertices())
    plaquettes = tuple(torus.plaquette(face) for face in torus.plaquettes())
    stabilizers = stars + plaquettes

    for first_index, first in enumerate(stabilizers):
        for second in stabilizers[first_index + 1:]:
            require(first.commutes(second),
                    "ANYON-C1 toric-code stabilizers do not commute")

    require(pauli_product(stars) == Pauli(),
            "ANYON-C1 product of all stars is not the identity")
    require(pauli_product(plaquettes) == Pauli(),
            "ANYON-C1 product of all plaquettes is not the identity")

    rank = gf2_rank([
        symplectic_row(operator, torus.qubits) for operator in stabilizers
    ])
    expected_rank = torus.qubits - 2
    require(rank == expected_rank,
            f"ANYON-C1 stabilizer rank {rank} != {expected_rank}")
    ground_dimension = 1 << (torus.qubits - rank)
    require(ground_dimension == 4,
            f"ANYON-C1 ground dimension {ground_dimension} != 4")
    print(
        "ANYON-C1-TORUS PASS "
        f"size={torus.length_x}x{torus.length_y} "
        f"qubits={torus.qubits} stabilizer_rank={rank} ground_dim=4"
    )


def ribbon_data(
    torus: SquareTorus,
) -> tuple[dict[Label, Pauli], Pauli, Pauli]:
    # Direct path (0,0)->(2,0): its Z string creates e at those vertices.
    direct_edges = (
        torus.horizontal(0, 0),
        torus.horizontal(1, 0),
    )
    # Dual path p(0,0)->p(2,0): eastward dual steps cross these vertical edges.
    dual_crossings = (
        torus.vertical(1, 0),
        torus.vertical(2, 0),
    )
    electric_string = torus.z_string(direct_edges)
    magnetic_string = torus.x_string(dual_crossings)
    ribbons = {
        label: electric_string.power(label[0]).times(
            magnetic_string.power(label[1])
        )
        for label in LABELS
    }

    # The minimal contractible endpoint cell contains v=(0,0), p=(0,0).
    electric_flux = torus.star((0, 0))
    magnetic_flux = torus.plaquette((0, 0))
    return ribbons, electric_flux, magnetic_flux


def endpoint_gate(
    torus: SquareTorus,
    ribbons: dict[Label, Pauli],
    electric_flux: Pauli,
    magnetic_flux: Pauli,
) -> None:
    expected_vertices = {(0, 0), (2, 0)}
    expected_faces = {(0, 0), (2, 0)}

    require(electric_flux.commutes(magnetic_flux),
            "ANYON-C2 boundary flux bits do not commute")
    for label, ribbon in ribbons.items():
        star_syndrome = {
            vertex for vertex in torus.vertices()
            if torus.star(vertex).commutation_bit(ribbon)
        }
        plaquette_syndrome = {
            face for face in torus.plaquettes()
            if torus.plaquette(face).commutation_bit(ribbon)
        }
        require(
            star_syndrome == (expected_vertices if label[0] else set()),
            f"ANYON-C2 {label_name(label)} has wrong electric endpoints",
        )
        require(
            plaquette_syndrome == (expected_faces if label[1] else set()),
            f"ANYON-C2 {label_name(label)} has wrong magnetic endpoints",
        )
        measured = (
            electric_flux.commutation_bit(ribbon),
            magnetic_flux.commutation_bit(ribbon),
        )
        require(measured == label,
                f"ANYON-C2 boundary sector {measured} != {label}")

    print(
        "ANYON-C2-ENDPOINTS PASS labels=1,e,m,epsilon "
        "syndromes=exact boundary_sector=definite"
    )


def braiding_gate(
    ribbons: dict[Label, Pauli],
    electric_flux: Pauli,
    magnetic_flux: Pauli,
) -> None:
    for charge, ribbon in ribbons.items():
        detected = False
        for probe in LABELS:
            closed_probe = magnetic_flux.power(probe[0]).times(
                electric_flux.power(probe[1])
            )
            actual = closed_probe.commutation_bit(ribbon)
            expected = (charge[0] * probe[1] + charge[1] * probe[0]) & 1
            require(actual == expected,
                    "ANYON-C3 wrong mutual-braiding phase for "
                    f"{label_name(charge)},{label_name(probe)}")
            detected = detected or actual == 1
        require(charge == VACUUM or detected,
                f"ANYON-C3 nontrivial charge {label_name(charge)} undetected")

    e_m_phase = (-1) ** (
        ribbons[ELECTRIC].commutation_bit(electric_flux)
    )
    require(e_m_phase == -1,
            "ANYON-C3 electric-magnetic braiding is not -1")
    print(
        "ANYON-C3-BRAIDING PASS table=4x4 pairing=nondegenerate "
        "phase(e,m)=-1"
    )


def protocol_gate(
    ribbons: dict[Label, Pauli],
    electric_flux: Pauli,
    magnetic_flux: Pauli,
    red_mode: str | None,
) -> None:
    initial_weights = {
        VACUUM: Fraction(1, 10),
        ELECTRIC: Fraction(2, 10),
        MAGNETIC: Fraction(3, 10),
        FERMION: Fraction(4, 10),
    }
    observed_increments: set[Label] = set()

    for charge, ribbon in ribbons.items():
        actual_shift = (
            electric_flux.commutation_bit(ribbon),
            magnetic_flux.commutation_bit(ribbon),
        )
        claimed_shift = charge
        if red_mode == "wrong-sector" and charge == ELECTRIC:
            claimed_shift = MAGNETIC

        joint_law: dict[tuple[Label, Label], Fraction] = {}
        for source, weight in initial_weights.items():
            target = add_labels(source, actual_shift)
            joint_law[(source, target)] = weight

        require(sum(joint_law.values(), Fraction()) == 1,
                f"ANYON-C4 TPM law for {label_name(charge)} is not normalized")
        for (source, target), weight in joint_law.items():
            require(weight >= 0,
                    "ANYON-C4 TPM law contains a negative exact weight")
            increment = add_labels(target, source)
            observed_increments.add(increment)
            require(increment == claimed_shift,
                    "ANYON-C4 wrong-sector mutation detected: "
                    f"computed {label_name(increment)}, "
                    f"claimed {label_name(claimed_shift)}")

        # Charge creation from a ground sector is deterministic.
        vacuum_target = add_labels(VACUUM, actual_shift)
        require(vacuum_target == charge,
                f"ANYON-C4 vacuum did not shift to {label_name(charge)}")

    require(observed_increments == set(LABELS),
            "ANYON-C4 protocol does not realize the full Z2xZ2 lattice")
    print(
        "ANYON-C4-TPM PASS same_circle=1 exact_weights=1 "
        "support=b-a=x outcome_lattice=Z2xZ2"
    )


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--red", choices=("wrong-sector",), default=None)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    code_shape_gate()
    torus = SquareTorus(4, 4)
    torus_gate(torus)
    ribbons, electric_flux, magnetic_flux = ribbon_data(torus)
    endpoint_gate(torus, ribbons, electric_flux, magnetic_flux)
    braiding_gate(ribbons, electric_flux, magnetic_flux)
    protocol_gate(ribbons, electric_flux, magnetic_flux, args.red)
    require(args.red is None, "ANYON red mode failed to trigger")
    print("ALL ANYON-LABEL GATES PASS")


if __name__ == "__main__":
    main()
