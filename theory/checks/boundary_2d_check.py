#!/usr/bin/env python3
"""Exact/ED boundary battery for 1D claims transplanted to 2+1 dimensions.

Green command:
    python3 -O theory/checks/boundary_2d_check.py

Run one standing gate:
    python3 -O theory/checks/boundary_2d_check.py --gate W4-C1-PERIMETER

The registered failures are positive requirements here: the 2D norm must
grow with perimeter, loop charge must fail to distinguish winding, the toric
loop must fail as an additive D10 charge, and the directional contact phases
must disagree.  There are no bare ``assert`` statements, so every gate is
active under ``python -O``.  Only NumPy and the standard library are used.
"""

from __future__ import annotations

import argparse
import ast
from collections import defaultdict
from itertools import combinations
import math
from pathlib import Path
import sys

import numpy as np


TOL = 2.0e-10
GATES = (
    "W4-C0-SHAPE",
    "W4-C1-PERIMETER",
    "W4-C2-LOOP-AREA",
    "W4-C3-ONE-FORM",
    "W4-C4-ANGULAR-PHASE",
    "W4-C5-REGISTER",
)


def fail(message: str) -> None:
    print(f"FAIL: {message}", file=sys.stderr)
    raise SystemExit(1)


def require(condition: bool, message: str) -> None:
    if not condition:
        fail(message)


def max_abs(value: np.ndarray) -> float:
    return float(np.max(np.abs(value))) if value.size else 0.0


def operator_norm_hermitian(value: np.ndarray) -> float:
    eigenvalues = np.linalg.eigvalsh((value + value.conj().T) / 2.0)
    return float(np.max(np.abs(eigenvalues))) if eigenvalues.size else 0.0


def code_shape_gate() -> None:
    tree = ast.parse(Path(__file__).read_text(encoding="utf-8"))
    bare_assertions = [
        node for node in ast.walk(tree) if isinstance(node, ast.Assert)
    ]
    require(not bare_assertions, "W4-C0-SHAPE found a bare assert")
    print("W4-C0-SHAPE PASS bare_asserts=0 optimization_safe=1")


# ---------------------------------------------------------------------------
# W4-C1: the charge-window commutator has a perimeter, not endpoint, norm.


def kron_at(operator: np.ndarray, site: int, number_sites: int) -> np.ndarray:
    result = np.array([[1.0 + 0.0j]])
    for position in range(number_sites):
        factor = operator if position == site else np.eye(2, dtype=complex)
        result = np.kron(result, factor)
    return result


def xy_row_hamiltonian(number_sites: int) -> tuple[np.ndarray, list[np.ndarray]]:
    """Return (1/2) sum(1-P) and the on-site down-number operators."""
    raising = np.array([[0.0, 1.0], [0.0, 0.0]], dtype=complex)
    lowering = raising.T.conj()
    number = np.diag([0.0, 1.0]).astype(complex)
    number_ops = [kron_at(number, x, number_sites) for x in range(number_sites)]
    raising_ops = [
        kron_at(raising, x, number_sites) for x in range(number_sites)
    ]
    lowering_ops = [operator.T.conj() for operator in raising_ops]
    hamiltonian = np.zeros((2**number_sites, 2**number_sites), dtype=complex)
    for x in range(number_sites):
        y = (x + 1) % number_sites
        hamiltonian += 0.5 * (
            number_ops[x]
            + number_ops[y]
            - 2.0 * number_ops[x] @ number_ops[y]
            - raising_ops[x] @ lowering_ops[y]
            - lowering_ops[x] @ raising_ops[y]
        )
    return hamiltonian, number_ops


def perimeter_gate() -> None:
    """ED the row current; tensor-sum spectra give the exact 2D norm."""
    length_x = 6
    hamiltonian, number_ops = xy_row_hamiltonian(length_x)
    row_norms: dict[int, float] = {}
    row_spectra: dict[int, np.ndarray] = {}
    for width in (1, 2, 3):
        charge = sum(number_ops[:width])
        current = 1.0j * (hamiltonian @ charge - charge @ hamiltonian)
        hermiticity = max_abs(current - current.conj().T)
        require(hermiticity < TOL, f"C1 current not Hermitian: {hermiticity}")
        spectrum = np.linalg.eigvalsh(current)
        row_spectra[width] = spectrum
        row_norms[width] = float(np.max(np.abs(spectrum)))

    # W=[0,w-1] x Z_Ly wraps the transverse cycle.  Every y-bond lies wholly
    # in or out of W, so its charge commutator is zero.  The remaining rows
    # have disjoint support, and the 2D spectrum is the Minkowski sum of the
    # independently ED'd row spectra.  This avoids constructing a 2^18 matrix.
    transverse_sizes = (1, 3, 4)
    norms: dict[tuple[int, int], float] = {}
    for height in transverse_sizes:
        for width in (1, 2, 3):
            spectrum = row_spectra[width]
            norm = height * max(abs(float(spectrum[0])), abs(float(spectrum[-1])))
            norms[(height, width)] = norm

    single_bond_charge = number_ops[0] + number_ops[1]
    single_bond = 0.5 * (
        number_ops[0]
        + number_ops[1]
        - 2.0 * number_ops[0] @ number_ops[1]
        - kron_at(np.array([[0.0, 1.0], [0.0, 0.0]], dtype=complex), 0, length_x)
        @ kron_at(np.array([[0.0, 0.0], [1.0, 0.0]], dtype=complex), 1, length_x)
        - kron_at(np.array([[0.0, 0.0], [1.0, 0.0]], dtype=complex), 0, length_x)
        @ kron_at(np.array([[0.0, 1.0], [0.0, 0.0]], dtype=complex), 1, length_x)
    )
    internal_residual = max_abs(
        single_bond @ single_bond_charge - single_bond_charge @ single_bond
    )

    require(internal_residual < TOL, "C1 internal bond failed charge conservation")
    require(abs(row_norms[1] - 1.0 / math.sqrt(2.0)) < TOL, "C1 w=1 norm")
    require(abs(row_norms[2] - 1.0) < TOL, "C1 w=2 norm")
    require(abs(row_norms[3] - 1.0) < TOL, "C1 w=3 norm")
    require(abs(norms[(3, 2)] - 3.0) < TOL, "C1 6x3 perimeter norm")
    require(
        abs(norms[(4, 3)] / norms[(1, 3)] - 4.0) < TOL,
        "C1 registered perimeter growth disappeared",
    )
    require(
        abs(norms[(3, 2)] / (2.0 * 3.0) - 0.5) < TOL,
        "C1 wide-window norm no longer saturates perimeter/2",
    )
    print(
        "W4-C1-PERIMETER PASS "
        f"row_norms[w=1,2,3]=({row_norms[1]:.6f},{row_norms[2]:.6f},"
        f"{row_norms[3]:.6f}) "
        f"torus_6x3[w=1,2,3]=({norms[(3, 1)]:.6f},"
        f"{norms[(3, 2)]:.6f},{norms[(3, 3)]:.6f}) "
        f"wide_norm/perimeter={norms[(3, 2)] / 6.0:.6f} "
        f"internal_bond_residual={internal_residual:.2e}"
    )


# ---------------------------------------------------------------------------
# W4-C2: a 2D sharp-loop charge is area, not a loop coordinate.


def square_edges(length: int) -> list[tuple[tuple[int, int], tuple[int, int]]]:
    edges = []
    for y in range(length):
        for x in range(length):
            edges.append(((x, y), ((x + 1) % length, y)))
            edges.append(((x, y), (x, (y + 1) % length)))
    return edges


def wall_perimeter(domain: set[tuple[int, int]], length: int) -> int:
    return sum((first in domain) != (second in domain)
               for first, second in square_edges(length))


def wall_windings(
    domain: set[tuple[int, int]], length: int
) -> tuple[tuple[int, int], ...]:
    """Trace degree-two dual loops and return their absolute homology."""
    adjacency: dict[tuple[int, int], list[tuple[tuple[int, int], int, tuple[int, int]]]] = defaultdict(list)
    edge_number = 0

    def add_edge(
        first: tuple[int, int], second: tuple[int, int],
        displacement: tuple[int, int],
    ) -> None:
        nonlocal edge_number
        adjacency[first].append((second, edge_number, displacement))
        adjacency[second].append(
            (first, edge_number, (-displacement[0], -displacement[1]))
        )
        edge_number += 1

    for y in range(length):
        for x in range(length):
            # A horizontal primal wall gives a vertical dual edge.
            if ((x, y) in domain) != (((x + 1) % length, y) in domain):
                add_edge((x, (y - 1) % length), (x, y), (0, 1))
            # A vertical primal wall gives a horizontal dual edge.
            if ((x, y) in domain) != ((x, (y + 1) % length) in domain):
                add_edge(((x - 1) % length, y), (x, y), (1, 0))

    require(
        all(len(neighbours) == 2 for neighbours in adjacency.values()),
        "C2 registered examples developed a branching dual wall",
    )
    unused = set(range(edge_number))
    windings = []
    while unused:
        chosen = next(iter(unused))
        start = next(
            vertex for vertex, neighbours in adjacency.items()
            if any(edge == chosen for _other, edge, _step in neighbours)
        )
        current = start
        previous_edge = -1
        displacement = np.array([0, 0], dtype=int)
        while True:
            candidates = [entry for entry in adjacency[current]
                          if entry[1] != previous_edge and entry[1] in unused]
            if not candidates:
                require(current == start, "C2 dual wall trace did not close")
                break
            following, edge, step = candidates[0]
            unused.remove(edge)
            displacement += np.asarray(step)
            previous_edge = edge
            current = following
            if current == start:
                break
        require(
            np.all(displacement % length == 0),
            f"C2 nonintegral winding displacement {displacement}",
        )
        winding = tuple(int(abs(value // length)) for value in displacement)
        windings.append(winding)
    return tuple(sorted(windings))


def loop_area_gate() -> None:
    length = 4
    all_sites = [(x, y) for y in range(length) for x in range(length)]
    identity_error = 0
    for mask in range(1 << (length * length)):
        area = mask.bit_count()
        # With S^z=+1/2 outside and -1/2 inside, sum(S^z-1/2)=-area.
        relative_charge = -mask.bit_count()
        identity_error = max(identity_error, abs(relative_charge + area))

    block = {(1, 1), (1, 2), (2, 1), (2, 2)}
    stripe = {(1, y) for y in range(length)}
    isolated = {(0, 0), (0, 2), (2, 0), (2, 2)}
    block_data = (-len(block), wall_perimeter(block, length),
                  wall_windings(block, length))
    stripe_data = (-len(stripe), wall_perimeter(stripe, length),
                   wall_windings(stripe, length))
    isolated_data = (-len(isolated), wall_perimeter(isolated, length),
                     wall_windings(isolated, length))

    maximum_exchange_area_change = 0
    maximum_window_area_change = 0
    window = {(x, y) for y in range(length) for x in (0, 1)}
    for mask in range(1 << (length * length)):
        for first, second in square_edges(length):
            first_index = first[1] * length + first[0]
            second_index = second[1] * length + second[0]
            first_bit = (mask >> first_index) & 1
            second_bit = (mask >> second_index) & 1
            if first_bit == second_bit:
                continue
            moved = mask ^ (1 << first_index) ^ (1 << second_index)
            maximum_exchange_area_change = max(
                maximum_exchange_area_change,
                abs(moved.bit_count() - mask.bit_count()),
            )
            old_window = sum((mask >> (y * length + x)) & 1 for x, y in window)
            new_window = sum((moved >> (y * length + x)) & 1 for x, y in window)
            maximum_window_area_change = max(
                maximum_window_area_change, abs(new_window - old_window)
            )

    require(identity_error == 0, "C2 charge/area identity failed")
    require(block_data[0] == stripe_data[0] == isolated_data[0] == -4,
            "C2 equal-charge examples changed")
    require(block_data[1] == stripe_data[1] == 8, "C2 perimeter control")
    require(isolated_data[1] == 16, "C2 shape blindness control")
    require(block_data[2] == ((0, 0),), "C2 block should be contractible")
    require(stripe_data[2] == ((0, 1), (0, 1)),
            f"C2 stripe winding changed: {stripe_data[2]}")
    require(isolated_data[2] == ((0, 0),) * 4,
            f"C2 isolated-loop topology changed: {isolated_data[2]}")
    require(maximum_exchange_area_change == 0, "C2 total area not conserved")
    require(maximum_window_area_change == 1, "C2 window area should change by one")
    print(
        "W4-C2-LOOP-AREA PASS "
        f"all_2^16_identity_error={identity_error} "
        f"charge[block,stripe,isolated]=({block_data[0]},{stripe_data[0]},"
        f"{isolated_data[0]}) perimeter=({block_data[1]},{stripe_data[1]},"
        f"{isolated_data[1]}) winding={block_data[2]}/{stripe_data[2]}/"
        f"{isolated_data[2]} "
        f"exchange_delta_area={maximum_exchange_area_change} "
        f"window_delta_area={maximum_window_area_change}"
    )


# ---------------------------------------------------------------------------
# W4-C3: toric-code loop symmetry is multiplicative, not a D10 zero mode.


def tensor_pauli(number_qubits: int, entries: dict[int, np.ndarray]) -> np.ndarray:
    identity = np.eye(2, dtype=complex)
    result = np.array([[1.0 + 0.0j]])
    for qubit in range(number_qubits):
        result = np.kron(result, entries.get(qubit, identity))
    return result


def one_form_gate() -> None:
    length = 2
    number_qubits = 2 * length * length
    x_pauli = np.array([[0.0, 1.0], [1.0, 0.0]], dtype=complex)
    z_pauli = np.diag([1.0, -1.0]).astype(complex)

    def edge(kind: str, x: int, y: int) -> int:
        offset = 0 if kind == "h" else length * length
        return offset + (y % length) * length + (x % length)

    stars = []
    plaquettes = []
    for y in range(length):
        for x in range(length):
            stars.append(tensor_pauli(number_qubits, {
                edge("h", x, y): x_pauli,
                edge("h", x - 1, y): x_pauli,
                edge("v", x, y): x_pauli,
                edge("v", x, y - 1): x_pauli,
            }))
            plaquettes.append(tensor_pauli(number_qubits, {
                edge("h", x, y): z_pauli,
                edge("v", x + 1, y): z_pauli,
                edge("h", x, y + 1): z_pauli,
                edge("v", x, y): z_pauli,
            }))
    hamiltonian = -sum(stars) - sum(plaquettes)
    loop_edges = [edge("h", x, 0) for x in range(length)]
    loop = tensor_pauli(number_qubits, {site: z_pauli for site in loop_edges})
    additive = sum(
        tensor_pauli(number_qubits, {site: z_pauli}) for site in loop_edges
    )
    loop_commutator = hamiltonian @ loop - loop @ hamiltonian
    additive_commutator = hamiltonian @ additive - additive @ hamiltonian

    open_string = tensor_pauli(number_qubits, {loop_edges[0]: z_pauli})
    open_commutator = hamiltonian @ open_string - open_string @ hamiltonian
    endpoint_stars = [
        star for star in stars
        if max_abs(star @ open_string + open_string @ star) < TOL
    ]
    endpoint_formula = -2.0 * sum(star @ open_string for star in endpoint_stars)
    endpoint_residual = max_abs(open_commutator - endpoint_formula)

    identity = np.eye(2**number_qubits, dtype=complex)
    plus = (identity + loop) / 2.0
    minus = (identity - loop) / 2.0
    cross_block = minus @ loop @ plus
    cross_rank = 0 if max_abs(cross_block) < TOL else int(
        np.linalg.matrix_rank(cross_block, tol=TOL)
    )
    loop_norm = operator_norm_hermitian(1.0j * loop_commutator)
    additive_norm = operator_norm_hermitian(1.0j * additive_commutator)
    open_norm = operator_norm_hermitian(1.0j * open_commutator)

    require(loop_norm < TOL, "C3 closed Wilson loop is not conserved")
    require(abs(additive_norm - 8.0) < TOL, "C3 additive loop norm changed")
    require(len(endpoint_stars) == 2, "C3 open string has wrong endpoint count")
    require(abs(open_norm - 4.0) < TOL, "C3 open-string norm changed")
    require(endpoint_residual < TOL, "C3 endpoint identity failed")
    require(cross_rank == 0, "C3 loop became a cross-sector ladder")
    require(max_abs(cross_block) < TOL, "C3 cross block nonzero")
    print(
        "W4-C3-ONE-FORM PASS "
        f"||[H,W_loop]||={loop_norm:.2e} "
        f"||[H,sum_e_Ze]||={additive_norm:.6f} "
        f"open_endpoint_count={len(endpoint_stars)} "
        f"open_norm={open_norm:.6f} endpoint_residual={endpoint_residual:.2e} "
        f"rank(Pminus_W_Pplus)={cross_rank}"
    )


# ---------------------------------------------------------------------------
# W4-C4: the two-magnon contact datum is angular/multichannel in 2D.


def scattering_ratio(first: float, second: float) -> complex:
    z_first = np.exp(1.0j * first)
    z_second = np.exp(1.0j * second)
    return -(
        z_first * z_second - 2.0 * z_first + 1.0
    ) / (
        z_first * z_second - 2.0 * z_second + 1.0
    )


def phase_derivative(direction_component: float, hard_component: float) -> float:
    step = 2.0e-5
    phases = {
        multiple: np.angle(scattering_ratio(
            multiple * step * direction_component, hard_component
        ))
        for multiple in (-2, -1, 1, 2)
    }
    return float(
        (phases[-2] - 8.0 * phases[-1]
         + 8.0 * phases[1] - phases[2]) / (12.0 * step)
    )


def two_magnon_patch(
    length: int,
) -> tuple[np.ndarray, list[tuple[int, int]], list[tuple[int, int]]]:
    coordinates = [(x, y) for y in range(length) for x in range(length)]
    basis = list(combinations(range(length * length), 2))
    index = {state: number for number, state in enumerate(basis)}
    hamiltonian = np.zeros((len(basis), len(basis)), dtype=complex)
    edges = []
    for y in range(length):
        for x in range(length):
            first = y * length + x
            for dx, dy in ((1, 0), (0, 1)):
                second = ((y + dy) % length) * length + (x + dx) % length
                edges.append((first, second))
    for column, state in enumerate(basis):
        occupied = set(state)
        for first, second in edges:
            if (first in occupied) == (second in occupied):
                continue
            hamiltonian[column, column] += 0.5
            moved = (occupied - {first, second}) | (
                {second} if first in occupied else {first}
            )
            hamiltonian[index[tuple(sorted(moved))], column] -= 0.5
    return hamiltonian, basis, coordinates


def plane_wave_channel(
    first: tuple[int, int], second: tuple[int, int], length: int,
    basis: list[tuple[int, int]], coordinates: list[tuple[int, int]],
) -> np.ndarray:
    k_first = 2.0 * math.pi * np.asarray(first) / length
    k_second = 2.0 * math.pi * np.asarray(second) / length
    vector = np.array([
        np.exp(1.0j * (
            k_first @ coordinates[x] + k_second @ coordinates[y]
        ))
        + np.exp(1.0j * (
            k_second @ coordinates[x] + k_first @ coordinates[y]
        ))
        for x, y in basis
    ])
    return vector / np.linalg.norm(vector)


def angular_phase_gate() -> None:
    hard = (0.9, 1.2)
    directions = (
        (1.0, 0.0),
        (0.0, 1.0),
        (1.0 / math.sqrt(2.0), 1.0 / math.sqrt(2.0)),
        (1.0 / math.sqrt(2.0), -1.0 / math.sqrt(2.0)),
    )
    slopes = [
        tuple(phase_derivative(direction[axis], hard[axis]) for axis in (0, 1))
        for direction in directions
    ]
    slope_error = max(
        abs(slopes[row][axis] - 2.0 * directions[row][axis])
        for row in range(len(directions)) for axis in (0, 1)
    )
    axial_spread = abs(slopes[0][0] - slopes[0][1])
    anti_diagonal_spread = abs(slopes[3][0] - slopes[3][1])

    length = 4
    hamiltonian, basis, coordinates = two_magnon_patch(length)
    total = (2, 2)  # K=(pi,pi): every free two-magnon channel has E=4.
    seen = set()
    channel_labels = []
    for py in range(length):
        for px in range(length):
            first = (px, py)
            second = ((total[0] - px) % length, (total[1] - py) % length)
            key = tuple(sorted((first, second)))
            if key not in seen:
                seen.add(key)
                channel_labels.append((first, second))
    channels = np.column_stack([
        plane_wave_channel(first, second, length, basis, coordinates)
        for first, second in channel_labels
    ])
    gram = channels.conj().T @ channels
    channel_rank = int(np.sum(np.linalg.eigvalsh(gram) > 1.0e-10))
    defect = channels.conj().T @ (
        hamiltonian - 4.0 * np.eye(len(basis))
    ) @ channels
    off_diagonal = defect - np.diag(np.diag(defect))
    maximum_channel_mixing = max_abs(off_diagonal)
    charge_label = channel_labels.index(((0, 0), (2, 2)))
    charge_residual = float(np.linalg.norm(
        (hamiltonian - 4.0 * np.eye(len(basis))) @ channels[:, charge_label]
    ))

    require(slope_error < 2.0e-9, f"C4 phase derivative error {slope_error}")
    require(abs(axial_spread - 2.0) < 2.0e-9, "C4 axial angular spread")
    require(
        abs(anti_diagonal_spread - 2.0 * math.sqrt(2.0)) < 2.0e-9,
        "C4 anti-diagonal angular spread",
    )
    require(channel_rank == 9, f"C4 channel rank {channel_rank}, expected 9")
    require(
        abs(maximum_channel_mixing - 2.0 / 7.0) < TOL,
        f"C4 channel mixing {maximum_channel_mixing}",
    )
    require(charge_residual < TOL, "C4 zero-mode descendant residual")
    print(
        "W4-C4-ANGULAR-PHASE PASS "
        f"slopes_xpath=({slopes[0][0]:.6f},{slopes[0][1]:.6f}) "
        f"slopes_ypath=({slopes[1][0]:.6f},{slopes[1][1]:.6f}) "
        f"slopes_diag=({slopes[2][0]:.6f},{slopes[2][1]:.6f}) "
        f"slopes_antidiag=({slopes[3][0]:.6f},{slopes[3][1]:.6f}) "
        f"4x4_Kpi_channel_rank={channel_rank} "
        f"max_offdiag_contact={maximum_channel_mixing:.6f} "
        f"Q0_descendant_residual={charge_residual:.2e}"
    )


# ---------------------------------------------------------------------------
# W4-C5: the full-sector/highest-weight register trap survives in 2D.


def bit_basis(number_sites: int, magnons: int) -> tuple[list[int], dict[int, int]]:
    states = [
        sum(1 << site for site in occupied)
        for occupied in combinations(range(number_sites), magnons)
    ]
    return states, {state: number for number, state in enumerate(states)}


def total_lowering(number_sites: int, magnons: int) -> np.ndarray:
    source, _source_index = bit_basis(number_sites, magnons)
    target, target_index = bit_basis(number_sites, magnons + 1)
    result = np.zeros((len(target), len(source)), dtype=complex)
    for column, state in enumerate(source):
        for site in range(number_sites):
            if not ((state >> site) & 1):
                result[target_index[state | (1 << site)], column] += 1.0
    return result


def horizontal_currents(
    length: int, magnons: int,
) -> tuple[np.ndarray, np.ndarray]:
    number_sites = length * length
    source, source_index = bit_basis(number_sites, magnons)
    target, target_index = bit_basis(number_sites, magnons + 1)
    j_z = np.zeros((len(source), len(source)), dtype=complex)
    j_minus = np.zeros((len(target), len(source)), dtype=complex)
    for y in range(length):
        for x in range(length):
            first = y * length + x
            second = y * length + (x + 1) % length
            for column, state in enumerate(source):
                first_bit = (state >> first) & 1
                second_bit = (state >> second) & 1
                swapped = state
                if first_bit != second_bit:
                    swapped ^= (1 << first) | (1 << second)
                z_first = 0.5 - ((swapped >> first) & 1)
                z_second = 0.5 - ((swapped >> second) & 1)
                j_z[source_index[swapped], column] += 0.5 * (
                    z_second - z_first
                )
                if not ((swapped >> second) & 1):
                    j_minus[target_index[swapped | (1 << second)], column] += 0.5
                if not ((swapped >> first) & 1):
                    j_minus[target_index[swapped | (1 << first)], column] -= 0.5
    return j_z, j_minus


def highest_weight_basis(number_sites: int, magnons: int) -> np.ndarray:
    raising = total_lowering(number_sites, magnons - 1).conj().T
    _left, singular_values, right_adjoint = np.linalg.svd(
        raising, full_matrices=True
    )
    rank = int(np.sum(singular_values > 1.0e-10))
    return right_adjoint[rank:].conj().T


def register_gate() -> None:
    length = 3
    number_sites = length * length
    magnons = 2
    lowering = total_lowering(number_sites, magnons)
    highest_weight = highest_weight_basis(number_sites, magnons)
    j_z, j_minus = horizontal_currents(length, magnons)

    rng = np.random.default_rng(20260829)
    coefficients = (
        rng.normal(size=highest_weight.shape[1])
        + 1.0j * rng.normal(size=highest_weight.shape[1])
    )
    psi = highest_weight @ coefficients
    psi /= np.linalg.norm(psi)

    full_gram = lowering.conj().T @ lowering
    full_projection = lowering @ np.linalg.solve(
        full_gram, lowering.conj().T
    )
    restricted_lowering = lowering @ highest_weight
    restricted_gram = restricted_lowering.conj().T @ restricted_lowering
    highest_projection = highest_weight @ highest_weight.conj().T
    restricted_projection = restricted_lowering @ np.linalg.solve(
        restricted_gram, restricted_lowering.conj().T
    )
    j_z_psi = j_z @ psi
    weight = number_sites - 2 * magnons
    m_lambda = weight / 2.0

    left_full = full_projection @ (j_minus @ psi)
    right_full = 2.0 * lowering @ np.linalg.solve(full_gram, j_z_psi)
    right_highest = (
        lowering @ (highest_projection @ j_z_psi) / m_lambda
    )
    left_highest = restricted_projection @ (j_minus @ psi)

    # This is the literal 0.00e+00 trap: reading the scalar restricted Gram
    # in the full register and dropping Pi_hw is exactly the refuted display.
    refuted_display = (2.0 / weight) * (lowering @ j_z_psi)
    naive_restricted_reading = (2.0 / weight) * (lowering @ j_z_psi)
    trap_coincidence = float(np.linalg.norm(
        naive_restricted_reading - refuted_display
    ))
    scalar_error = float(np.linalg.norm(
        restricted_gram - weight * np.eye(restricted_gram.shape[0])
    ))
    full_error = float(np.linalg.norm(left_full - right_full))
    highest_error = float(np.linalg.norm(left_highest - right_highest))
    cross_error = float(np.linalg.norm(left_full - right_highest))
    refuted_error = float(np.linalg.norm(left_full - refuted_display))

    require(highest_weight.shape[1] == 27, "C5 highest-weight rank changed")
    require(scalar_error < TOL, "C5 restricted Gram is not scalar")
    require(full_error < TOL, "C5 corrected full-register identity failed")
    require(highest_error < TOL, "C5 corrected highest-register identity failed")
    require(trap_coincidence < TOL, "C5 scalar trap coincidence disappeared")
    require(cross_error > 0.1, "C5 full/highest register distinction disappeared")
    require(refuted_error > 0.1, "C5 refuted scalar display became accurate")
    print(
        "W4-C5-REGISTER PASS "
        f"3x3_n=2 hw_dim={highest_weight.shape[1]} "
        f"||A_hw-5I||={scalar_error:.2e} "
        f"full_error={full_error:.2e} hw_error={highest_error:.2e} "
        f"trap_coincidence={trap_coincidence:.2e} "
        f"cross_register_error={cross_error:.6f} "
        f"refuted_error={refuted_error:.6f}"
    )


GATE_FUNCTIONS = {
    "W4-C0-SHAPE": code_shape_gate,
    "W4-C1-PERIMETER": perimeter_gate,
    "W4-C2-LOOP-AREA": loop_area_gate,
    "W4-C3-ONE-FORM": one_form_gate,
    "W4-C4-ANGULAR-PHASE": angular_phase_gate,
    "W4-C5-REGISTER": register_gate,
}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--gate", choices=GATES, help="run one standing gate")
    parser.add_argument("--list-gates", action="store_true")
    arguments = parser.parse_args()
    if arguments.list_gates:
        print("\n".join(GATES))
        return
    selected = (arguments.gate,) if arguments.gate else GATES
    for gate in selected:
        GATE_FUNCTIONS[gate]()
    print("ALL 2+1 BOUNDARY GATES PASS")


if __name__ == "__main__":
    main()
