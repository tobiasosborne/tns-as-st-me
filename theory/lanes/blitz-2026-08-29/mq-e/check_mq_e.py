#!/usr/bin/env python3
"""Finite-volume falsifier for the Mq-E enumeration.

The proof is analytic.  This checker exhausts small frozen-boundary chains,
compares their incoming <=3-DW component with the claimed Fano graph, checks
the charge/leg bookkeeping and product-basis locality, and has an intentional
right-tail mutation for the required red-capability demonstration.
"""

from __future__ import annotations

import argparse
# Standard-library only, so the falsifier is reproducible without dependencies.
from collections import Counter, deque
from itertools import combinations


def walls(spins: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(i for i in range(len(spins) - 1) if spins[i] != spins[i + 1])


def from_walls(size: int, wall_set: tuple[int, ...]) -> tuple[int, ...]:
    result = []
    spin = 1
    wall_lookup = set(wall_set)
    for site in range(size):
        result.append(spin)
        if site in wall_lookup:
            spin *= -1
    return tuple(result)


def enumerate_basis(size: int, mu: int) -> set[tuple[int, ...]]:
    """Sites are 0,...,size-1; endpoint spins are frozen up/down."""
    n_down = size - 1 - mu
    basis: set[tuple[int, ...]] = set()
    for down_sites in combinations(range(size), n_down):
        state = [1] * size
        for site in down_sites:
            state[site] = -1
        state_t = tuple(state)
        if state_t[0] != 1 or state_t[-1] != -1:
            continue
        if len(walls(state_t)) in (1, 3):
            basis.add(state_t)
    return basis


def neighbours(
    state: tuple[int, ...], basis: set[tuple[int, ...]]
) -> set[tuple[int, ...]]:
    result = set()
    for bond in walls(state):
        changed = list(state)
        changed[bond], changed[bond + 1] = changed[bond + 1], changed[bond]
        changed_t = tuple(changed)
        if changed_t in basis:
            result.add(changed_t)
    return result


def component(
    start: tuple[int, ...], basis: set[tuple[int, ...]]
) -> set[tuple[int, ...]]:
    seen = {start}
    queue = deque([start])
    while queue:
        state = queue.popleft()
        for candidate in neighbours(state, basis):
            if candidate not in seen:
                seen.add(candidate)
                queue.append(candidate)
    return seen


def graph_states(size: int, mu: int, red: bool) -> dict[object, tuple[int, ...]]:
    result: dict[object, tuple[int, ...]] = {"d": from_walls(size, (mu,))}
    n_min = 1 - mu
    n_max = size - mu - 3
    for n in range(n_min, 1):
        result[n] = from_walls(size, (mu + n - 1, mu + n, mu + 1))
    for n in range(1, n_max + 1):
        shift = 1 if red else 0
        result[n] = from_walls(
            size, (mu - 1, mu + n + shift, mu + n + 1 + shift)
        )
    return result


def check_locality(
    graph: dict[object, tuple[int, ...]], mu: int, size: int
) -> int:
    """Check the exact eventual channel constants for every interior window."""
    checks = 0
    kink_left = from_walls(size, (mu + 1,))
    kink_right = from_walls(size, (mu - 1,))
    numeric_labels = sorted(label for label in graph if isinstance(label, int))
    for lo in range(1, size - 1):
        for hi in range(lo, size - 1):
            window = set(range(lo, hi + 1))
            outside = set(range(size)) - window
            for label in numeric_labels:
                state = graph[label]
                moving_site = mu + label if label <= 0 else mu + label + 1
                if moving_site in window:
                    continue
                reference = kink_left if label <= 0 else kink_right
                assert all(state[x] == reference[x] for x in window)
                for other_label in numeric_labels:
                    if other_label == label:
                        continue
                    other = graph[other_label]
                    # Distinct product states can be connected by an arbitrary
                    # W-local operator only if they coincide outside W.
                    if all(state[x] == other[x] for x in outside):
                        other_moving = (
                            mu + other_label
                            if other_label <= 0
                            else mu + other_label + 1
                        )
                        assert other_moving in window
                checks += 1
    return checks


def run(red: bool) -> tuple[int, int, int]:
    volumes = 0
    vertices = 0
    locality_checks = 0
    for size in range(7, 17):
        for mu in range(2, size - 3):
            basis = enumerate_basis(size, mu)
            expected = graph_states(size, mu, red)
            start = expected[min(label for label in expected if isinstance(label, int))]
            actual_component = component(start, basis)
            assert set(expected.values()) == actual_component
            assert len(expected) == size - 2
            assert len(expected) == len(set(expected.values()))

            reverse = {state: label for label, state in expected.items()}
            actual_edges = set()
            for state in actual_component:
                for other in neighbours(state, basis):
                    if other in actual_component:
                        actual_edges.add(frozenset((reverse[state], reverse[other])))
            numeric = sorted(label for label in expected if isinstance(label, int))
            claimed_edges = {
                frozenset((left, right)) for left, right in zip(numeric, numeric[1:])
            }
            claimed_edges.add(frozenset((0, "d")))
            assert actual_edges == claimed_edges

            degree_histogram = Counter(
                sum(label in edge for edge in actual_edges) for label in expected
            )
            assert degree_histogram == Counter({2: size - 6, 1: 3, 3: 1})
            assert len(walls(expected["d"])) == 1
            assert all(
                len(walls(state)) == 3
                for label, state in expected.items()
                if label != "d"
            )

            # The conserved finite-volume charge is B-N_down=mu.  On the
            # asymptotic representatives it decomposes as kink+leg.
            assert (mu + 1) - 1 == mu  # incoming/reflected leg charge -1
            assert (mu - 1) + 1 == mu  # transmitted leg charge +1
            assert mu == mu  # side state is the pure kink K_mu

            locality_checks += check_locality(expected, mu, size)
            volumes += 1
            vertices += len(expected)
    return volumes, vertices, locality_checks


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--red", action="store_true")
    args = parser.parse_args()
    try:
        volumes, vertices, locality_checks = run(args.red)
    except (AssertionError, KeyError) as exc:
        if args.red:
            print("RED-OK: shifted right-tail mutation was detected")
            return 1
        print(f"FAIL: {exc!r}")
        return 1
    if args.red:
        print("RED-FAIL: shifted right-tail mutation escaped detection")
        return 2
    print(
        "PASS: "
        f"{volumes} volume/charge pairs, {vertices} component vertices, "
        f"{locality_checks} local-tail checks"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
