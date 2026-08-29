#!/usr/bin/env python3
"""Red-capable arithmetic checks for ML1/ML6's explicit D6 fiber formulas.

This checks only the scattering modulus, bound overlap/geometric sum, its
soft derivative, and the continuum/bound gap.  It does not test wave-operator
existence or a limit interchange.
"""

import argparse
import cmath
import math


def bound_overlap_formula(k: float, h: float, mutate: bool = False) -> float:
    K = h + k
    q = (h - k) / 2.0
    c = math.cos(K / 2.0)
    numerator_core = math.cos(q) + c if mutate else math.cos(q) - c
    return (
        2.0
        * math.sqrt(max(0.0, 1.0 - c * c))
        * numerator_core
        / (1.0 - 2.0 * c * math.cos(q) + c * c)
    )


def bound_overlap_sum(k: float, h: float, rmax: int = 6000) -> complex:
    K = h + k
    q = (h - k) / 2.0
    c = math.cos(K / 2.0)
    prefactor = math.sqrt(max(0.0, 1.0 - c * c))
    return prefactor * sum(
        (c ** (r - 1)) * (cmath.exp(1j * q * r) + cmath.exp(-1j * q * r))
        for r in range(1, rmax + 1)
    )


def scattering(K: float, q: float, mutate: bool = False) -> complex:
    c = math.cos(K / 2.0)
    denominator = cmath.exp(1j * q) + c if mutate else cmath.exp(1j * q) - c
    return (c - cmath.exp(-1j * q)) / denominator


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--red-bound", action="store_true")
    parser.add_argument("--red-unitarity", action="store_true")
    args = parser.parse_args()

    failures = []
    hard_grid = [0.4, 0.7, 1.1, 1.6, 2.1, 2.5]

    beta_zero = max(
        abs(bound_overlap_formula(0.0, h, mutate=args.red_bound)) for h in hard_grid
    )
    if beta_zero > 2.0e-12:
        failures.append("G1 bound overlap at k=0")

    sum_error = 0.0
    for h in hard_grid:
        for k in (-0.03, 0.02):
            exact = bound_overlap_formula(k, h, mutate=args.red_bound)
            direct = bound_overlap_sum(k, h)
            sum_error = max(sum_error, abs(exact - direct))
    if sum_error > 2.0e-10:
        failures.append("G2 geometric-series overlap")

    slope_error = 0.0
    step = 1.0e-6
    for h in hard_grid:
        derivative = (
            bound_overlap_formula(step, h, mutate=args.red_bound)
            - bound_overlap_formula(-step, h, mutate=args.red_bound)
        ) / (2.0 * step)
        slope_error = max(slope_error, abs(derivative - 2.0))
    if slope_error > 2.0e-7:
        failures.append("G3 soft bound-overlap derivative")

    unitarity_error = 0.0
    min_gap = float("inf")
    for h in hard_grid:
        for k in (-0.04, 0.01, 0.04):
            K = h + k
            q = (h - k) / 2.0
            c = math.cos(K / 2.0)
            s_value = scattering(K, q, mutate=args.red_unitarity)
            unitarity_error = max(unitarity_error, abs(abs(s_value) - 1.0))
            gap = abs(cmath.exp(1j * q) - c) ** 2
            min_gap = min(min_gap, gap)
    if unitarity_error > 2.0e-12:
        failures.append("G4 scattering unitarity")
    if min_gap <= 0.0:
        failures.append("G5 positive bound/continuum gap")

    print(f"beta_zero={beta_zero:.3e}")
    print(f"geometric_sum_error={sum_error:.3e}")
    print(f"soft_slope_error={slope_error:.3e}")
    print(f"unitarity_error={unitarity_error:.3e}")
    print(f"sample_min_gap_over_J={min_gap:.6e}")
    if failures:
        print("FAIL: " + "; ".join(failures))
        return 1
    print("PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
