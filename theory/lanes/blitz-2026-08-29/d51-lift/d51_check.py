#!/usr/bin/env python3
"""D51-CHECK: red-capable finite graph check for the 3/5-wall coupling.

This is a falsifier for the combinatorial constants, not a proof of the
infinite-volume spectral statements in D51-LIFT.md.
"""

from __future__ import annotations

import argparse
import math


def walls(bits: tuple[int, ...]) -> int:
    # Opposite frozen tails enforce the kink sector and retain both neighbours
    # of every dynamical swap in the wall count.
    extended = (0,) + bits + (1,)
    return sum(extended[i] != extended[i + 1] for i in range(len(extended) - 1))


def swap_moves(bits: tuple[int, ...]):
    for i in range(len(bits) - 1):
        if bits[i] == bits[i + 1]:
            continue
        moved = list(bits)
        moved[i], moved[i + 1] = moved[i + 1], moved[i]
        yield i, tuple(moved)


def all_bits(n: int):
    for raw in range(1 << n):
        yield tuple((raw >> i) & 1 for i in range(n))


def scan(n: int) -> tuple[int, int, set[int], int]:
    p_rows: dict[tuple[int, ...], int] = {}
    q_cols: dict[tuple[int, ...], int] = {}
    changes: set[int] = set()
    cross_edges = 0
    for bits in all_bits(n):
        before = walls(bits)
        for _, moved in swap_moves(bits):
            after = walls(moved)
            changes.add(after - before)
            if before in (1, 3) and after >= 5:
                if not (before == 3 and after == 5):
                    raise AssertionError(f"illegal cross edge {before}->{after}")
                p_rows[bits] = p_rows.get(bits, 0) + 1
                q_cols[moved] = q_cols.get(moved, 0) + 1
                cross_edges += 1
    return max(p_rows.values(), default=0), max(q_cols.values(), default=0), changes, cross_edges


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--red", action="store_true", help="mutate row bound 3 to 2")
    args = parser.parse_args()

    row_bound = 2 if args.red else 3
    global_row = 0
    global_col = 0
    total_edges = 0
    for n in range(6, 13):
        row, col, changes, edges = scan(n)
        if changes - {-2, 0, 2}:
            raise AssertionError(f"n={n}: unexpected wall changes {changes}")
        if row > row_bound:
            raise AssertionError(f"n={n}: P-to-Q row degree {row} exceeds {row_bound}")
        if col > 3:
            raise AssertionError(f"n={n}: Q-to-P column degree {col} exceeds 3")
        global_row = max(global_row, row)
        global_col = max(global_col, col)
        total_edges += edges

    if global_row != 3:
        raise AssertionError(f"test battery did not saturate row degree 3: {global_row}")
    beta = math.sqrt(3 * 3) / 2
    print("D51-CHECK PASS")
    print(f"sizes=6..12 max_row={global_row} max_col={global_col} cross_edges={total_edges}")
    print(f"wall_changes=[-2, 0, 2] schur_beta_over_J={beta:.12f}")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except AssertionError as exc:
        print(f"D51-CHECK FAIL: {exc}")
        raise SystemExit(1)
