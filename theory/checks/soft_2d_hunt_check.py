#!/usr/bin/env python3
"""Exact finite checks for theory/soft-2d-hunt.md.

The Hilbert space is the 16-dimensional four-edge Z2 stabilizer patch.
No external packages are required.  All acceptance conditions remain active
under ``python3 -O``; this file intentionally contains no assert statements.
"""

from __future__ import annotations

import argparse
import ast
import cmath
import math
from pathlib import Path
from typing import Callable, Iterable, Sequence


DIM = 16
STAR_X_MASKS = (0b1001, 0b0011, 0b0110, 0b1100)
PLAQUETTE_Z_MASK = 0b1111
GAMMA_1 = 0b0011
GAMMA_2 = 0b1100
TOL = 2.0e-8


class CheckFailure(RuntimeError):
    """Raised by an optimization-safe acceptance gate."""


def require(condition: bool, message: str) -> None:
    if not condition:
        raise CheckFailure(message)


def popcount(value: int) -> int:
    return value.bit_count()


def inner(left: Sequence[complex], right: Sequence[complex]) -> complex:
    return sum(a.conjugate() * b for a, b in zip(left, right))


def norm(vector: Sequence[complex]) -> float:
    return math.sqrt(max(0.0, inner(vector, vector).real))


def add_vectors(
    terms: Iterable[tuple[complex, Sequence[complex]]],
) -> list[complex]:
    result = [0.0j] * DIM
    for coefficient, vector in terms:
        for index, value in enumerate(vector):
            result[index] += coefficient * value
    return result


def distance(left: Sequence[complex], right: Sequence[complex]) -> float:
    return norm([a - b for a, b in zip(left, right)])


def apply_pauli(
    vector: Sequence[complex], *, x_mask: int = 0, z_mask: int = 0
) -> list[complex]:
    """Apply X^x Z^z; all mixed uses below have disjoint masks."""

    result = [0.0j] * DIM
    for basis, amplitude in enumerate(vector):
        sign = -1.0 if popcount(basis & z_mask) % 2 else 1.0
        result[basis ^ x_mask] += sign * amplitude
    return result


def ground_state() -> list[complex]:
    amplitude = 1.0 / math.sqrt(8.0)
    return [
        complex(amplitude if popcount(basis) % 2 == 0 else 0.0)
        for basis in range(DIM)
    ]


def stabilizer_energy(vector: Sequence[complex]) -> float:
    star_sum = sum(
        inner(vector, apply_pauli(vector, x_mask=mask)).real
        for mask in STAR_X_MASKS
    )
    plaquette = inner(
        vector, apply_pauli(vector, z_mask=PLAQUETTE_Z_MASK)
    ).real
    return -star_sum - plaquette


def phase_amplitude(
    k_value: float, strength: float, origin: float, positions: Sequence[float]
) -> complex:
    phase = strength * sum(math.sin(k_value * (s + origin)) for s in positions)
    return cmath.exp(1.0j * phase)


def coherent_path_amplitude(
    omega: Sequence[complex],
    chi: Sequence[complex],
    gamma_2: int,
    k_value: float,
    strength: float,
    separation: float,
) -> complex:
    chi_2 = apply_pauli(omega, z_mask=gamma_2)
    relative_phase = cmath.exp(
        1.0j * strength * math.sin(k_value * separation)
    )
    state = add_vectors(((0.5, chi), (0.5 * relative_phase, chi_2)))
    return inner(chi, state)


def rotated_string_state(
    omega: Sequence[complex],
    k_value: float,
    strength: float,
    positions: Sequence[float],
) -> list[complex]:
    """Apply product_j (cos(theta_j) Z_j + sin(theta_j) X_j)."""

    require(len(positions) == 2, "the patch rotation expects two path edges")
    angles = [strength * math.sin(k_value * s) for s in positions]
    terms: list[tuple[complex, Sequence[complex]]] = []
    for choices in range(4):
        coefficient = 1.0
        x_mask = 0
        z_mask = 0
        for edge, angle in enumerate(angles):
            if choices & (1 << edge):
                coefficient *= math.sin(angle)
                x_mask |= 1 << edge
            else:
                coefficient *= math.cos(angle)
                z_mask |= 1 << edge
        terms.append(
            (coefficient, apply_pauli(omega, x_mask=x_mask, z_mask=z_mask))
        )
    return add_vectors(terms)


def second_difference(function: Callable[[float], float], step: float) -> float:
    return (function(step) - 2.0 * function(0.0) + function(-step)) / step**2


def gate_shape() -> str:
    source = Path(__file__).read_text(encoding="utf-8")
    tree = ast.parse(source)
    bare_asserts = sum(isinstance(node, ast.Assert) for node in ast.walk(tree))
    require(bare_asserts == 0, f"found {bare_asserts} bare assert statement(s)")
    return f"bare_asserts={bare_asserts} optimized={int(not __debug__)}"


def gate_ground(omega: Sequence[complex]) -> str:
    require(abs(norm(omega) - 1.0) < TOL, "ground state is not normalized")
    for index, mask in enumerate(STAR_X_MASKS):
        require(
            distance(apply_pauli(omega, x_mask=mask), omega) < TOL,
            f"ground state fails star {index}",
        )
    require(
        distance(apply_pauli(omega, z_mask=PLAQUETTE_Z_MASK), omega) < TOL,
        "ground state fails plaquette",
    )
    energy = stabilizer_energy(omega)
    require(abs(energy + 5.0) < TOL, f"ground energy {energy} is not -5")
    return f"dim={DIM} stabilizers=4+1 E0={energy:.1f}"


def gate_endpoint(
    omega: Sequence[complex], gamma_2: int
) -> tuple[str, list[complex]]:
    chi_1 = apply_pauli(omega, z_mask=GAMMA_1)
    chi_2 = apply_pauli(omega, z_mask=gamma_2)
    require(
        distance(chi_1, chi_2) < TOL,
        "the two alleged paths do not create the same endpoint state",
    )
    syndromes = [
        round(inner(chi_1, apply_pauli(chi_1, x_mask=mask)).real)
        for mask in STAR_X_MASKS
    ]
    require(syndromes == [-1, 1, -1, 1], f"wrong star syndromes {syndromes}")
    plaquette = inner(
        chi_1, apply_pauli(chi_1, z_mask=PLAQUETTE_Z_MASK)
    ).real
    require(abs(plaquette - 1.0) < TOL, "endpoint pair has a flux violation")
    energy = stabilizer_energy(chi_1)
    require(abs(energy + 1.0) < TOL, f"pair energy {energy} is not -1")
    return "paths=B-equivalent syndrome=-,+,-,+ gap=4", chi_1


def gate_phase_freedom(probe_erased: bool) -> str:
    positions = (0.25, 1.25)
    origin = 0.5
    strength_1 = 0.4
    strength_2 = strength_1 if probe_erased else 1.1
    step = 1.0e-6
    derivatives: list[complex] = []
    for strength in (strength_1, strength_2):
        numerical = (
            phase_amplitude(step, strength, origin, positions)
            - phase_amplitude(-step, strength, origin, positions)
        ) / (2.0 * step)
        exact = 1.0j * strength * sum(s + origin for s in positions)
        require(abs(numerical - exact) < 2.0e-9, "phase derivative mismatch")
        derivatives.append(numerical)
    require(
        abs(derivatives[0] - derivatives[1]) > 0.5,
        "probe variation did not change the phase slope",
    )
    return (
        "same_channel=1 slopes="
        f"{derivatives[0].imag:.3f}i,{derivatives[1].imag:.3f}i"
    )


def gate_path_curvature(
    omega: Sequence[complex],
    chi: Sequence[complex],
    gamma_2: int,
    probe_erased: bool,
) -> str:
    separation = 1.75
    strength_1 = 0.7
    strength_2 = strength_1 if probe_erased else 1.4
    step = 7.0e-4
    curvatures: list[float] = []
    for strength in (strength_1, strength_2):
        amplitude = lambda k_value: abs(
            coherent_path_amplitude(
                omega, chi, gamma_2, k_value, strength, separation
            )
        )
        require(abs(amplitude(0.0) - 1.0) < TOL, "path sum is not normalized at k=0")
        numerical = second_difference(amplitude, step)
        exact = -(strength * separation) ** 2 / 4.0
        require(abs(numerical - exact) < 2.0e-6, "path curvature mismatch")
        curvatures.append(numerical)
    require(
        abs(curvatures[1] / curvatures[0] - 4.0) < 2.0e-5,
        "path curvature did not respond quadratically to probe strength",
    )
    return f"normalized=1 curvature_ratio={curvatures[1] / curvatures[0]:.6f}"


def gate_rotation_curvature(
    omega: Sequence[complex], chi: Sequence[complex], probe_erased: bool
) -> str:
    positions = (0.5, 1.5)
    strength_1 = 0.6
    strength_2 = strength_1 if probe_erased else 1.2
    step = 6.0e-4
    curvatures: list[float] = []
    for strength in (strength_1, strength_2):
        def amplitude(k_value: float) -> float:
            rotated = rotated_string_state(omega, k_value, strength, positions)
            require(abs(norm(rotated) - 1.0) < TOL, "rotated string is not unitary")
            computed = inner(chi, rotated).real
            expected = math.prod(
                math.cos(strength * math.sin(k_value * s)) for s in positions
            )
            require(abs(computed - expected) < TOL, "channel projection mismatch")
            return computed

        require(abs(amplitude(0.0) - 1.0) < TOL, "rotation is not anchored at k=0")
        numerical = second_difference(amplitude, step)
        exact = -(strength**2) * sum(s * s for s in positions)
        require(abs(numerical - exact) < 2.0e-6, "rotation curvature mismatch")
        curvatures.append(numerical)
    require(
        abs(curvatures[1] / curvatures[0] - 4.0) < 2.0e-5,
        "rotation leakage did not respond quadratically to probe strength",
    )
    return f"unitary=1 projected_curvature_ratio={curvatures[1] / curvatures[0]:.6f}"


def run_gate(name: str, function: Callable[[], str], failures: list[str]) -> None:
    try:
        detail = function()
        print(f"{name} PASS {detail}")
    except CheckFailure as error:
        failures.append(name)
        print(f"{name} FAIL {error}")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--red",
        choices=("wrong-path", "erase-probe-freedom"),
        help="run a registered mutant that must fail an advertised gate",
    )
    args = parser.parse_args()

    gamma_2 = 0b0100 if args.red == "wrong-path" else GAMMA_2
    probe_erased = args.red == "erase-probe-freedom"
    omega = ground_state()
    chi = apply_pauli(omega, z_mask=GAMMA_1)
    failures: list[str] = []

    run_gate("S2DH-C0-SHAPE", gate_shape, failures)
    run_gate("S2DH-C1-GROUND", lambda: gate_ground(omega), failures)

    def endpoint_detail() -> str:
        detail, _ = gate_endpoint(omega, gamma_2)
        return detail

    run_gate("S2DH-C2-ENDPOINT", endpoint_detail, failures)
    run_gate(
        "S2DH-C3-PHASE-FREEDOM",
        lambda: gate_phase_freedom(probe_erased),
        failures,
    )
    run_gate(
        "S2DH-C4-PATH-CURVATURE",
        lambda: gate_path_curvature(
            omega, chi, gamma_2, probe_erased
        ),
        failures,
    )
    run_gate(
        "S2DH-C5-ROTATION-CURVATURE",
        lambda: gate_rotation_curvature(omega, chi, probe_erased),
        failures,
    )

    if failures:
        print("SOFT-2D-HUNT CHECK FAILED gates=" + ",".join(failures))
        return 1
    if args.red:
        print("SOFT-2D-HUNT RED MODE UNEXPECTEDLY PASSED")
        return 1
    print("ALL SOFT-2D-HUNT GATES PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

