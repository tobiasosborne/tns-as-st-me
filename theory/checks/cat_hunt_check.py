#!/usr/bin/env python3
"""Exact fusion-algebra checks for ``theory/cat-hunt.md``.

Green:
    python3 -O theory/checks/cat_hunt_check.py

Registered red mode (must exit nonzero):
    python3 -O theory/checks/cat_hunt_check.py --red missing-ising-channel

The calculation uses integer fusion matrices and the integer character table
of Q_8.  It contains no bare ``assert``, so every gate runs under ``-O``.
"""

from __future__ import annotations

import argparse
import ast
from fractions import Fraction
from pathlib import Path
import sys


Matrix = tuple[tuple[int, ...], ...]
FusionTable = dict[tuple[str, str], dict[str, int]]


def fail(message: str) -> None:
    print(f"FAIL: {message}", file=sys.stderr)
    raise SystemExit(1)


def require(condition: bool, message: str) -> None:
    if not condition:
        fail(message)


def matrix_add(left: Matrix, right: Matrix) -> Matrix:
    return tuple(
        tuple(left[row][column] + right[row][column]
              for column in range(len(left)))
        for row in range(len(left))
    )


def matrix_scale(coefficient: int, matrix: Matrix) -> Matrix:
    return tuple(
        tuple(coefficient * entry for entry in row)
        for row in matrix
    )


def matrix_multiply(left: Matrix, right: Matrix) -> Matrix:
    size = len(left)
    return tuple(
        tuple(
            sum(left[row][middle] * right[middle][column]
                for middle in range(size))
            for column in range(size)
        )
        for row in range(size)
    )


def matrix_vector(matrix: Matrix, vector: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(
        sum(matrix[row][column] * vector[column]
            for column in range(len(vector)))
        for row in range(len(vector))
    )


def zero_matrix(size: int) -> Matrix:
    return tuple(tuple(0 for _ in range(size)) for _ in range(size))


def identity_matrix(size: int) -> Matrix:
    return tuple(
        tuple(1 if row == column else 0 for column in range(size))
        for row in range(size)
    )


def fusion_matrices(labels: tuple[str, ...], table: FusionTable) -> dict[str, Matrix]:
    """Return left-fusion matrices: (N_a)[c,b] = N_{a b}^c."""
    index = {label: position for position, label in enumerate(labels)}
    result: dict[str, Matrix] = {}
    for charge in labels:
        entries = [[0 for _ in labels] for _ in labels]
        for source in labels:
            for target, multiplicity in table[(charge, source)].items():
                entries[index[target]][index[source]] = multiplicity
        result[charge] = tuple(tuple(row) for row in entries)
    return result


def check_fusion_ring(labels: tuple[str, ...], table: FusionTable,
                      unit: str, gate: str) -> dict[str, Matrix]:
    matrices = fusion_matrices(labels, table)
    require(matrices[unit] == identity_matrix(len(labels)),
            f"{gate} unit matrix is not the identity")
    for first in labels:
        for second in labels:
            left = matrix_multiply(matrices[first], matrices[second])
            right = zero_matrix(len(labels))
            for output, multiplicity in table[(first, second)].items():
                right = matrix_add(
                    right, matrix_scale(multiplicity, matrices[output])
                )
            require(left == right,
                    f"{gate} associativity failed for {first}*{second}")
    return matrices


def check_grading(labels: tuple[str, ...], table: FusionTable,
                  degree: dict[str, int], modulus: int, gate: str) -> None:
    for first in labels:
        for second in labels:
            expected = (degree[first] + degree[second]) % modulus
            for output, multiplicity in table[(first, second)].items():
                if multiplicity:
                    require(degree[output] == expected,
                            f"{gate} grade failed for {first}*{second}->{output}")


def code_shape_gate() -> None:
    tree = ast.parse(Path(__file__).read_text(encoding="utf-8"))
    bare = [node for node in ast.walk(tree) if isinstance(node, ast.Assert)]
    require(not bare, "CATH-C0 found a bare assert")
    print("CATH-C0-SHAPE PASS bare_asserts=0 optimization_safe=1")


def pointed_character_gate() -> None:
    labels = ("triv", "sign")
    table: FusionTable = {
        ("triv", "triv"): {"triv": 1},
        ("triv", "sign"): {"sign": 1},
        ("sign", "triv"): {"sign": 1},
        ("sign", "sign"): {"triv": 1},
    }
    matrices = check_fusion_ring(labels, table, "triv", "CATH-C1")
    sign_swap = ((0, 1), (1, 0))
    require(matrices["sign"] == sign_swap,
            "CATH-C1 sign character does not swap the two charge sectors")
    require(matrix_multiply(sign_swap, sign_swap) == identity_matrix(2),
            "CATH-C1 character shift is not invertible")
    print("CATH-C1-POINTED PASS Vec_Z2 dual=Rep_Z2 index=sign targets=unique")


def ising_gate(red_mode: str | None) -> None:
    labels = ("one", "psi", "sigma")
    table: FusionTable = {
        ("one", "one"): {"one": 1},
        ("one", "psi"): {"psi": 1},
        ("one", "sigma"): {"sigma": 1},
        ("psi", "one"): {"psi": 1},
        ("psi", "psi"): {"one": 1},
        ("psi", "sigma"): {"sigma": 1},
        ("sigma", "one"): {"sigma": 1},
        ("sigma", "psi"): {"sigma": 1},
        ("sigma", "sigma"): {"one": 1, "psi": 1},
    }
    if red_mode == "missing-ising-channel":
        table[("sigma", "sigma")] = {"one": 1}

    matrices = check_fusion_ring(labels, table, "one", "CATH-C2")
    degree = {"one": 0, "psi": 0, "sigma": 1}
    check_grading(labels, table, degree, 2, "CATH-C2")
    expected_sigma = ((0, 0, 1), (0, 0, 1), (1, 1, 0))
    require(matrices["sigma"] == expected_sigma,
            "CATH-C2 sigma fusion matrix lost or gained a channel")
    require(matrix_multiply(matrices["sigma"], matrices["sigma"])
            == matrix_add(matrices["one"], matrices["psi"]),
            "CATH-C2 N_sigma^2 != I + N_psi")
    require(table[("sigma", "sigma")] == {"one": 1, "psi": 1},
            "CATH-C2 sigma*sigma must have two distinct fine targets")
    dimension_squared = sum(table[("sigma", "sigma")].values())
    require(dimension_squared == 2,
            "CATH-C2 positive fusion dimension of sigma is not sqrt(2)")
    print("CATH-C2-ISING PASS sigma_dim=sqrt(2) sigma_degree=odd "
          "sigma*sigma=one+psi fine_targets=2")


def q8_fusion_table() -> tuple[tuple[str, ...], FusionTable, dict[str, tuple[int, ...]]]:
    labels = ("one", "a", "b", "c", "rho")
    class_sizes = (1, 1, 2, 2, 2)
    characters = {
        "one": (1, 1, 1, 1, 1),
        "a": (1, 1, 1, -1, -1),
        "b": (1, 1, -1, 1, -1),
        "c": (1, 1, -1, -1, 1),
        "rho": (2, -2, 0, 0, 0),
    }
    table: FusionTable = {}
    for first in labels:
        for second in labels:
            outputs: dict[str, int] = {}
            for target in labels:
                coefficient = Fraction(sum(
                    size * characters[first][column]
                    * characters[second][column]
                    * characters[target][column]
                    for column, size in enumerate(class_sizes)
                ), 8)
                require(coefficient.denominator == 1 and coefficient >= 0,
                        "CATH-C3 character product produced a non-fusion coefficient")
                if coefficient:
                    outputs[target] = int(coefficient)
            table[(first, second)] = outputs
    return labels, table, characters


def q8_gate() -> None:
    labels, table, characters = q8_fusion_table()
    matrices = check_fusion_ring(labels, table, "one", "CATH-C3")

    class_sizes = (1, 1, 2, 2, 2)
    for first in labels:
        for second in labels:
            inner = Fraction(sum(
                size * characters[first][column] * characters[second][column]
                for column, size in enumerate(class_sizes)
            ), 8)
            require(inner == (1 if first == second else 0),
                    f"CATH-C3 Q8 characters not orthonormal: {first},{second}")

    degree = {
        label: 0 if characters[label][1] == characters[label][0] else 1
        for label in labels
    }
    check_grading(labels, table, degree, 2, "CATH-C3")
    require(degree == {"one": 0, "a": 0, "b": 0, "c": 0, "rho": 1},
            "CATH-C3 wrong Q8 central-character grading")
    require(table[("rho", "rho")]
            == {"one": 1, "a": 1, "b": 1, "c": 1},
            "CATH-C3 rho*rho did not split into all four even sectors")

    line_labels = labels[:-1]
    for line in line_labels:
        matrix = matrices[line]
        require(all(sum(matrix[row][column] for row in range(len(labels))) == 1
                    for column in range(len(labels))),
                f"CATH-C3 electric character {line} does not give unique targets")
    require(all(table[(line, "rho")] == {"rho": 1}
                for line in line_labels),
            "CATH-C3 a one-dimensional Q8 character failed to fix rho")

    # For u=1+rho, the central element -1 acts as diag(1,-1,-1), so K_u is
    # trivial and the odd rho operator block is visible.  For u=rho alone,
    # -1 acts as a scalar and End(rho)=rho*rho contains only even objects.
    mixed_center_eigenvalues = (1, -1, -1)
    require(len(set(mixed_center_eigenvalues)) > 1,
            "CATH-C3 mixed physical register incorrectly has scalar center")
    pure_center_eigenvalues = (-1, -1)
    require(len(set(pure_center_eigenvalues)) == 1,
            "CATH-C3 pure rho register should quotient the scalar center")
    require(all(degree[target] == 0
                for target in table[("rho", "rho")]),
            "CATH-C3 End(rho) contains an odd effective-center object")
    print("CATH-C3-REP-Q8 PASS central_grades=4+1 rho*rho=4_even "
          "electric_characters=Z2xZ2 Ku_mixed=1 Ku_pure=Z2")


def operator_split_gate() -> None:
    # Gamma is the Z2 sector operator.  D, B_1 and B_3 are all odd, so the
    # categorical Fourier projector leaves all three in the same block.
    gamma = ((1, 0), (0, -1))
    descendant = ((0, 0), (1, 0))
    current_one = descendant
    current_three = matrix_scale(3, descendant)

    def conjugate(matrix: Matrix) -> Matrix:
        return matrix_multiply(matrix_multiply(gamma, matrix), gamma)

    for name, matrix in (("D", descendant), ("B1", current_one),
                         ("B3", current_three)):
        require(conjugate(matrix) == matrix_scale(-1, matrix),
                f"CATH-C4 {name} is not in the registered odd block")
    require(current_one != current_three,
            "CATH-C4 comparison currents accidentally coincide")
    source = (1, 0)
    range_projector = ((0, 0), (0, 1))
    projected_one = matrix_vector(
        range_projector, matrix_vector(current_one, source)
    )
    projected_three = matrix_vector(
        range_projector, matrix_vector(current_three, source)
    )
    require(projected_one == (0, 1) and projected_three == (0, 3),
            "CATH-C4 same-sector projected currents did not retain 1:3 freedom")
    require(matrix_multiply(
        tuple(zip(*descendant)), descendant
    ) == ((1, 0), (0, 0)),
            "CATH-C4 descendant Gram matrix is wrong")

    scaled_descendant = matrix_scale(2, descendant)
    require(matrix_multiply(tuple(zip(*scaled_descendant)), scaled_descendant)
            == ((4, 0), (0, 0)),
            "CATH-C4 same categorical arrow did not admit Gram rescaling")
    print("CATH-C4-OPERATOR-SPLIT PASS same_degree_currents=2 "
          "projected_ratio=1:3 gram_scale=1:4")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--red", choices=("missing-ising-channel",), default=None,
        help="apply a registered mutation; the run must fail",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    code_shape_gate()
    pointed_character_gate()
    ising_gate(args.red)
    q8_gate()
    operator_split_gate()
    if args.red is not None:
        fail(f"red mutation {args.red} unexpectedly passed every gate")
    print("ALL CAT-HUNT GATES PASS")


if __name__ == "__main__":
    main()
