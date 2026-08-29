#!/usr/bin/env python3
"""Data and ED checks for ``theory/dh-semiclassical.md``.

Green:
    python3 -O theory/checks/dh_semiclassical_check.py

Registered red modes (each must exit nonzero):
    python3 -O theory/checks/dh_semiclassical_check.py --red wrong-leading
    python3 -O theory/checks/dh_semiclassical_check.py --red drop-fluctuation

The positive statement checked here concerns the spin-S two-magnon PHASE
envelope, not the exact support of a memory law.  DHSC-C1 and DHSC-C2 read
frozen data.  DHSC-C3 records the limited memory comparison without treating
transmission probabilities as DH volumes.  DHSC-C4 builds a periodic
two-magnon Hamiltonian independently, diagonalises a fixed total-momentum
block, and extracts its phase from Bethe--Yang level displacement.

There are no bare asserts, so all gates remain active under ``python3 -O``.
"""

from __future__ import annotations

import argparse
import ast
import json
import math
from pathlib import Path
import sys

import numpy as np


ROOT = Path(__file__).resolve().parents[2]
FALSIFIER = ROOT / "numerics" / "results" / "spin1-bc-falsifier.json"
SOFT_RESULTS = ROOT / "theory" / "checks" / "soft_index_probe_results.json"
MEMORY_RESULTS = ROOT / "docs" / "assets" / "memory_probe_rows.json"

EXACT_TOL = 2.0e-10
RING_SIZE = 18
MOMENTUM_INTEGER = 5
BETHE_DIFFERENCE = -3
TWO_SPINS = (1, 2, 3, 4, 6, 8, 12, 16)


def fail(message: str) -> None:
    print(f"FAIL: {message}", file=sys.stderr)
    raise SystemExit(1)


def require(condition: bool, message: str) -> None:
    if not condition:
        fail(message)


def load_json(path: Path) -> dict:
    require(path.is_file(), f"missing frozen data: {path}")
    with path.open("r", encoding="utf-8") as handle:
        value = json.load(handle)
    require(isinstance(value, dict), f"top-level JSON object required: {path}")
    return value


def code_shape_gate() -> None:
    tree = ast.parse(Path(__file__).read_text(encoding="utf-8"))
    bare = [node for node in ast.walk(tree) if isinstance(node, ast.Assert)]
    require(not bare, "DHSC-C0 found a bare assert")
    print("DHSC-C0-SHAPE PASS bare_asserts=0 optimization_safe=1")


def phase_coefficients(k_soft: float, k_hard: float) -> tuple[float, float, float]:
    """Return F,G,H in delta=F/S+G/S^2+H/S^3+O(S^-4)."""
    p_value = 0.5 * (k_soft + k_hard)
    q_value = 0.5 * (k_soft - k_hard)
    cos_p = math.cos(p_value)
    cos_q = math.cos(q_value)
    sin_q = math.sin(q_value)
    require(abs(cos_p * sin_q) > 1.0e-12,
            "phase coefficient evaluated outside the regular chamber")
    leading = cos_q * (cos_p - cos_q) / (cos_p * sin_q)
    denominator_shift = -1.0 + cos_q / cos_p
    first_fluctuation = -0.5 * leading * denominator_shift
    next_coefficient = (0.25 * leading * denominator_shift ** 2
                        - leading ** 3 / 12.0)
    return leading, first_fluctuation, next_coefficient


def numerical_derivative(index: int, k_soft: float, k_hard: float) -> float:
    step = 2.0e-6
    plus = phase_coefficients(k_soft + step, k_hard)[index]
    minus = phase_coefficients(k_soft - step, k_hard)[index]
    return (plus - minus) / (2.0 * step)


def slope_prediction(spin: float, red_mode: str | None) -> float:
    if red_mode == "wrong-leading":
        return 2.0 / spin
    return 1.0 / spin


def frozen_phase_gate(falsifier: dict, soft_results: dict,
                      red_mode: str | None) -> None:
    rows = falsifier.get("A_ring_summary")
    require(isinstance(rows, list) and rows,
            "DHSC-C1 missing frozen A_ring_summary")
    seen_spins: set[float] = set()
    worst_sigma = 0.0
    for row in rows:
        spin = float(row["S"])
        seen_spins.add(spin)
        measured = float(row["slope_extrapolated"])
        reported_error = float(row["error"])
        predicted = slope_prediction(spin, red_mode)
        require(abs(measured - predicted) <= reported_error + 1.0e-12,
                f"DHSC-C1 frozen ring slope misses envelope at S={spin}, "
                f"kh={row['k_h_target']}: {measured} vs {predicted} "
                f"with error {reported_error}")
        if reported_error > 0.0:
            worst_sigma = max(worst_sigma,
                              abs(measured - predicted) / reported_error)
    require(seen_spins == {0.5, 1.0, 1.5, 2.0},
            f"DHSC-C1 wrong frozen spin set: {sorted(seen_spins)}")

    p1_rows = [value for key, value in soft_results.items()
               if key.startswith("p1_two_s_")]
    require(len(p1_rows) == 2, "DHSC-C1 expected exactly two frozen P1 rows")
    worst_p1_relative = 0.0
    for row in p1_rows:
        spin = float(row["two_s"]) / 2.0
        measured = float(row["slope"])
        predicted = slope_prediction(spin, red_mode)
        relative = abs(measured / predicted - 1.0)
        worst_p1_relative = max(worst_p1_relative, relative)
        require(relative <= 0.05,
                f"DHSC-C1 soft-probe P1 slope misses 5% band at S={spin}")

    # Deliberately credit P2(a) only.  P2(b) is not read or reported here.
    p2a_errors = soft_results.get("p2", {}).get("jet_errors")
    require(isinstance(p2a_errors, list) and len(p2a_errors) == 2,
            "DHSC-C1 missing soft-probe P2(a) jet errors")
    require(max(float(value) for value in p2a_errors) <= 0.08,
            "DHSC-C1 soft-probe P2(a) misses its frozen 8% band")
    print("DHSC-C1-FROZEN-SLOPES PASS "
          f"spins=1/2,1,3/2,2 ring_worst_error_fraction={worst_sigma:.6f} "
          f"P1_worst_relative={worst_p1_relative:.6f} "
          "probe_scope=P1+P2(a)-only")


def frozen_finite_k_gate(falsifier: dict, red_mode: str | None) -> None:
    rows = [row for row in falsifier.get("A_dynamical_runs", [])
            if row.get("window") == "soft-window"]
    require(len(rows) == 8,
            f"DHSC-C2 expected eight frozen soft-window rows, got {len(rows)}")
    worst_relative = 0.0
    improvement_floor = math.inf
    for row in rows:
        spin = float(row["S"])
        k_soft = float(row["k_s"])
        k_hard = float(row["k_h"])
        measured = float(row["minus_delta_s_extrapolated"])
        leading_derivative = numerical_derivative(0, k_soft, k_hard)
        fluctuation_derivative = numerical_derivative(1, k_soft, k_hard)
        if red_mode == "wrong-leading":
            leading_derivative *= 2.0
        if red_mode == "drop-fluctuation":
            fluctuation_derivative = 0.0
        first_order = leading_derivative / spin
        second_order = first_order + fluctuation_derivative / spin ** 2
        first_error = abs(measured - first_order)
        second_error = abs(measured - second_order)
        relative = second_error / abs(measured)
        worst_relative = max(worst_relative, relative)
        if first_error > 0.0:
            improvement_floor = min(improvement_floor,
                                    1.0 - second_error / first_error)
        require(relative <= 0.03,
                f"DHSC-C2 second-order envelope misses 3% at "
                f"S={spin}, ks={k_soft}: {second_order} vs {measured}")
        require(second_error < first_error,
                f"DHSC-C2 fluctuation term did not improve S={spin}, ks={k_soft}")
    print("DHSC-C2-FROZEN-FINITE-K PASS rows=8 ksoft<=0.12 "
          f"worst_relative={worst_relative:.6f} "
          f"minimum_error_reduction={improvement_floor:.6f}")


def memory_scope_gate(falsifier: dict, memory_results: dict) -> None:
    decision_band = float(falsifier["decision_band"])
    selected = []
    for row in falsifier.get("B_runs", []):
        label = str(row.get("label", ""))
        if not label.startswith(("s05-D", "s1-D", "s15-D")):
            continue
        result = row["result"]
        if float(result["trapped"]) >= 1.0e-2:
            continue
        selected.append(row)
    require(selected, "DHSC-C3 selected no frozen memory rows")
    seen_spins: set[float] = set()
    worst_relative = 0.0
    for row in selected:
        result = row["result"]
        spin = float(result["params"]["spin"])
        seen_spins.add(spin)
        ratio = float(result["ratio_dx2_over_T"])
        predicted = -1.0 / spin
        relative = abs(ratio / predicted - 1.0)
        worst_relative = max(worst_relative, relative)
        require(relative <= decision_band,
                f"DHSC-C3 memory calibration misses frozen band: {row['label']}")
    require(seen_spins == {0.5, 1.0, 1.5},
            "DHSC-C3 must not manufacture an absent S=2 memory row")

    geometries = memory_results.get("geometries", {})
    gating = [value for value in geometries.values()
              if value.get("meta", {}).get("gating")]
    require(len(gating) == 2,
            "DHSC-C3 expected two gating memory-probe geometries")
    minimum_main_mass = 1.0
    maximum_off_lattice = 0.0
    for geometry in gating:
        final = geometry["rows"][-1]
        mass = float(final["p"].get("-2", 0.0))
        minimum_main_mass = min(minimum_main_mass, mass)
        maximum_off_lattice = max(maximum_off_lattice,
                                   float(final["off_lattice"]))
        require(mass >= 0.99,
                "DHSC-C3 gating memory law did not concentrate at Q_W=-2")
        require(float(final["off_lattice"]) == 0.0,
                "DHSC-C3 frozen memory output gained off-lattice mass")
    print("DHSC-C3-MEMORY-SCOPE PASS "
          f"calibration_rows={len(selected)} spins=1/2,1,3/2 "
          f"worst_relative={worst_relative:.6f} S2_memory_row=absent "
          f"probe_min_p_Qminus2={minimum_main_mass:.5f} "
          f"probe_max_off_lattice={maximum_off_lattice:.1f} "
          "interpretation=kinematic_not_DH-weight")


def pair_basis(size: int, two_spin: int) -> list[tuple[int, int]]:
    return [(first, second)
            for first in range(size)
            for second in range(first, size)
            if first < second or two_spin >= 2]


def occupations(pair: tuple[int, int], size: int) -> np.ndarray:
    result = np.zeros(size, dtype=int)
    result[pair[0]] += 1
    result[pair[1]] += 1
    return result


def pair_from_occupations(values: np.ndarray) -> tuple[int, int]:
    sites = np.repeat(np.arange(len(values)), values)
    require(len(sites) == 2, "DHSC-C4 hopping left the two-magnon sector")
    return int(sites[0]), int(sites[1])


def two_magnon_hamiltonian(size: int, two_spin: int
                           ) -> tuple[list[tuple[int, int]], np.ndarray]:
    """Independent occupation-basis ED for H=-sum(S.S-S^2), J=1."""
    spin = two_spin / 2.0
    basis = pair_basis(size, two_spin)
    index = {pair: position for position, pair in enumerate(basis)}
    matrix = np.zeros((len(basis), len(basis)), dtype=float)
    for column, pair in enumerate(basis):
        occ = occupations(pair, size)
        adjacent = sum(occ[site] * occ[(site + 1) % size]
                       for site in range(size))
        matrix[column, column] = 4.0 * spin - adjacent
        for site in range(size):
            neighbor = (site + 1) % size
            for source, target in ((site, neighbor), (neighbor, site)):
                n_source = int(occ[source])
                n_target = int(occ[target])
                if n_source == 0 or n_target == two_spin:
                    continue
                amplitude = -0.5 * math.sqrt(
                    n_source * (two_spin - n_source + 1)
                ) * math.sqrt(
                    (n_target + 1) * (two_spin - n_target)
                )
                moved = occ.copy()
                moved[source] -= 1
                moved[target] += 1
                row = index[pair_from_occupations(moved)]
                matrix[row, column] += amplitude
    require(np.linalg.norm(matrix - matrix.T) <= EXACT_TOL,
            "DHSC-C4 two-magnon Hamiltonian is not Hermitian")
    return basis, matrix


def translate(pair: tuple[int, int], size: int) -> tuple[int, int]:
    moved = sorted(((pair[0] + 1) % size, (pair[1] + 1) % size))
    return int(moved[0]), int(moved[1])


def momentum_block(basis: list[tuple[int, int]], matrix: np.ndarray,
                   size: int, momentum_integer: int) -> np.ndarray:
    index = {pair: position for position, pair in enumerate(basis)}
    seen: set[tuple[int, int]] = set()
    columns: list[np.ndarray] = []
    momentum = 2.0 * math.pi * momentum_integer / size
    for pair in basis:
        if pair in seen:
            continue
        orbit: list[tuple[int, int]] = []
        current = pair
        while current not in orbit:
            orbit.append(current)
            seen.add(current)
            current = translate(current, size)
        orbit_size = len(orbit)
        if (momentum_integer * orbit_size) % size != 0:
            continue
        vector = np.zeros(len(basis), dtype=complex)
        for power, translated in enumerate(orbit):
            vector[index[translated]] = (
                np.exp(-1.0j * momentum * power) / math.sqrt(orbit_size)
            )
        columns.append(vector)
    require(columns, "DHSC-C4 empty momentum block")
    isometry = np.stack(columns, axis=1)
    gram_error = np.linalg.norm(isometry.conj().T @ isometry
                                - np.eye(len(columns)))
    require(gram_error <= EXACT_TOL,
            "DHSC-C4 orbit vectors are not orthonormal")
    block = isometry.conj().T @ matrix @ isometry
    require(np.linalg.norm(block - block.conj().T) <= EXACT_TOL,
            "DHSC-C4 momentum block is not Hermitian")
    return block


def phase_remainder_bound(leading: float, denominator_shift: float,
                          spin: float) -> float:
    """Rigorous bound after F/S+G/S^2 for the exact arctan envelope.

    It combines the exact geometric-series remainder of
    2F/(2S+d) with |atan(x)-x| <= |x|^3/3 for |x|<=1.
    """
    inverse_spin = 1.0 / spin
    t_value = 0.5 * denominator_shift * inverse_spin
    require(1.0 + t_value > 0.0,
            "DHSC-C4 phase expansion crossed its denominator pole")
    x_value = leading * inverse_spin / (2.0 + denominator_shift * inverse_spin)
    require(abs(x_value) <= 1.0,
            "DHSC-C4 arctan remainder used outside |x|<=1")
    denominator_part = (
        abs(leading) * denominator_shift ** 2 * inverse_spin ** 3
        / (4.0 * abs(1.0 + t_value))
    )
    arctan_part = 2.0 * abs(x_value) ** 3 / 3.0
    return denominator_part + arctan_part


def independent_ed_gate(red_mode: str | None) -> None:
    size = RING_SIZE
    momentum_integer = MOMENTUM_INTEGER
    bethe_difference = BETHE_DIFFERENCE
    total_momentum = 2.0 * math.pi * momentum_integer / size
    target_q = abs(math.pi * bethe_difference / size)
    results = []
    for two_spin in TWO_SPINS:
        spin = two_spin / 2.0
        basis, matrix = two_magnon_hamiltonian(size, two_spin)
        block = momentum_block(basis, matrix, size, momentum_integer)
        eigenvalues = np.linalg.eigvalsh(block)
        candidates = []
        for energy in eigenvalues:
            cosine_q = ((1.0 - float(energy) / (4.0 * spin))
                        / math.cos(total_momentum / 2.0))
            if -1.0 <= cosine_q <= 1.0:
                q_abs = math.acos(cosine_q)
                candidates.append((abs(q_abs - target_q), q_abs, float(energy)))
        require(candidates, f"DHSC-C4 no scattering level at 2S={two_spin}")
        _, q_abs, energy = min(candidates)
        q_value = -q_abs
        k_soft = total_momentum / 2.0 + q_value
        k_hard = total_momentum / 2.0 - q_value
        delta_ed = size * q_value - math.pi * bethe_difference

        leading, fluctuation, _ = phase_coefficients(k_soft, k_hard)
        p_value = 0.5 * (k_soft + k_hard)
        q_check = 0.5 * (k_soft - k_hard)
        denominator_shift = -1.0 + math.cos(q_check) / math.cos(p_value)
        if red_mode == "wrong-leading":
            leading *= 2.0
        if red_mode == "drop-fluctuation":
            fluctuation = 0.0
        first_order = leading / spin
        second_order = first_order + fluctuation / spin ** 2
        first_error = abs(delta_ed - first_order)
        second_error = abs(delta_ed - second_order)
        bound = phase_remainder_bound(leading, denominator_shift, spin)
        require(second_error <= bound + 5.0e-12,
                f"DHSC-C4 ED phase left the analytic remainder bound at S={spin}: "
                f"error={second_error}, bound={bound}")
        require(second_error < first_error,
                f"DHSC-C4 fluctuation correction did not improve S={spin}")
        results.append((spin, delta_ed, first_error, second_error,
                        bound, energy, k_soft, k_hard))

    require(all(results[index + 1][3] < results[index][3]
                for index in range(len(results) - 1)),
            "DHSC-C4 second-order ED error does not decrease along large S")
    maximum_scaled_error = max(spin ** 3 * second_error
                               for spin, _, _, second_error, _, _, _, _
                               in results)
    require(maximum_scaled_error <= 0.01,
            "DHSC-C4 ED error is not compatible with the O(S^-3) model")
    first = results[0]
    last = results[-1]
    print("DHSC-C4-INDEPENDENT-ED PASS "
          f"N={size} K_index={momentum_integer} Bethe_difference={bethe_difference} "
          f"spins={','.join(str(value / 2) for value in TWO_SPINS)} "
          f"delta_Shalf={first[1]:.9f} delta_S8={last[1]:.9f} "
          f"max_S3_error={maximum_scaled_error:.9f} "
          f"last_error={last[3]:.3e} last_bound={last[4]:.3e}")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--red",
        choices=("wrong-leading", "drop-fluctuation"),
        default=None,
        help="apply a registered mutation; the run must fail",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    code_shape_gate()
    falsifier = load_json(FALSIFIER)
    soft_results = load_json(SOFT_RESULTS)
    memory_results = load_json(MEMORY_RESULTS)
    frozen_phase_gate(falsifier, soft_results, args.red)
    frozen_finite_k_gate(falsifier, args.red)
    memory_scope_gate(falsifier, memory_results)
    independent_ed_gate(args.red)
    if args.red is not None:
        fail(f"red mutation {args.red} unexpectedly passed every gate")
    print("ALL DH-SEMICLASSICAL GATES PASS")


if __name__ == "__main__":
    main()
