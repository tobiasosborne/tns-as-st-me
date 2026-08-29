#!/usr/bin/env python3
"""Finite corroboration for the scalar PROTO-LSZ witness.

The gates check only the exact spin-S multiplier algebra, its removable
scalar quotient, packet aggregation, and the non-uniqueness of an untyped
component split.  They do not certify D24 component provenance.
"""

from __future__ import annotations

import argparse
import cmath
import math
import sys


TOL = 2.0e-10


def fail(message: str) -> None:
    print(f"FAIL: {message}")
    raise SystemExit(1)


def require(condition: bool, message: str) -> None:
    if not condition:
        fail(message)


def velocity(spin: float, momentum: float) -> float:
    return 2.0 * spin * math.sin(momentum)


def s12(spin: float, soft: float, hard: float) -> complex:
    z1 = cmath.exp(1j * soft)
    z2 = cmath.exp(1j * hard)
    a = 1.0 + z1 * z2
    b = z1 + z2
    mu = (2.0 * spin - 1.0) * a + b
    numerator = spin * a * b - z1 * mu
    denominator = z2 * mu - spin * a * b
    require(abs(denominator) > 1.0e-8, "regular-domain denominator collapsed")
    return numerator / denominator


def physical_multiplier(spin: float, soft: float, hard: float) -> complex:
    raw = s12(spin, soft, hard)
    chi = 1.0 if velocity(spin, hard) > velocity(spin, soft) else -1.0
    return raw if chi > 0.0 else 1.0 / raw


def scalar_quotient(spin: float, soft: float, hard: float) -> complex:
    chi = 1.0 if velocity(spin, hard) > velocity(spin, soft) else -1.0
    vh = velocity(spin, hard)
    if soft == 0.0:
        return -1j * chi / (2.0 * spin * vh)
    return (physical_multiplier(spin, soft, hard) - 1.0) / (
        (cmath.exp(1j * soft) - 1.0) * (2j * vh)
    )


def normalized_weights(size: int) -> list[float]:
    raw = [1.0 + math.cos(math.pi * (j + 0.5) / size) ** 2 for j in range(size)]
    total = sum(raw)
    return [value / total for value in raw]


def c1_profile_gate(red_profile: bool) -> float:
    worst_scaled_error = 0.0
    for spin in (0.5, 1.0, 1.5, 2.0):
        for hard in (0.55, 1.1, 2.2, -0.8, -1.7):
            chi = 1.0 if velocity(spin, hard) > 0.0 else -1.0
            target = -1j * chi / (2.0 * spin * velocity(spin, hard))
            if red_profile:
                target *= 2.0
            for soft in (2.0e-4, 1.0e-4, 5.0e-5):
                signed_soft = soft if hard > 0.0 else -soft
                quotient = scalar_quotient(spin, signed_soft, hard)
                scaled_error = abs(quotient - target) / abs(signed_soft)
                worst_scaled_error = max(worst_scaled_error, scaled_error)
    require(worst_scaled_error < 25.0, "PLSZ-C1 removable profile failed")
    return worst_scaled_error


def exact_factor_gate(red_ward_factor: bool) -> float:
    worst = 0.0
    ward_factor = 1j if red_ward_factor else 2j
    for spin in (0.5, 1.0, 1.5, 2.0):
        for hard in (0.65, 1.25, 2.35, -0.75, -1.4):
            for soft in (0.003, 0.011, 0.027):
                signed_soft = soft if hard > 0.0 else -soft
                multiplier = physical_multiplier(spin, signed_soft, hard)
                quotient = scalar_quotient(spin, signed_soft, hard)
                reconstructed = (
                    (cmath.exp(1j * signed_soft) - 1.0)
                    * quotient
                    * ward_factor
                    * velocity(spin, hard)
                )
                worst = max(worst, abs((multiplier - 1.0) - reconstructed))
    require(worst < TOL, "PLSZ-C2 exact Ward/LSZ factor failed")
    return worst


def packet_and_slope_gate(red_slope: bool) -> tuple[float, float]:
    worst_packet = 0.0
    worst_remainder_coefficient = 0.0
    u_grid = [0.35 + 0.5 * j / 16.0 for j in range(17)]
    h_grid = [0.7 + 1.15 * j / 12.0 for j in range(13)]
    wu = normalized_weights(len(u_grid))
    wh = normalized_weights(len(h_grid))
    for spin in (0.5, 1.0, 1.5, 2.0):
        slope = 1.0 / (spin + 1.0) if red_slope else 1.0 / spin
        for epsilon in (0.025, 0.0125, 0.00625):
            amplitude = 0j
            descendant = 0j
            mean = 0.0
            for iu, u in enumerate(u_grid):
                soft = epsilon * u
                for ih, hard in enumerate(h_grid):
                    weight = wu[iu] * wh[ih]
                    multiplier = physical_multiplier(spin, soft, hard)
                    quotient = scalar_quotient(spin, soft, hard)
                    amplitude += weight * (multiplier - 1.0)
                    descendant += weight * (
                        (cmath.exp(1j * soft) - 1.0)
                        * quotient
                        * (2j * velocity(spin, hard))
                    )
                    mean += weight * soft
            worst_packet = max(worst_packet, abs(amplitude - descendant))
            coefficient = abs(amplitude - 1j * slope * mean) / (epsilon * epsilon)
            worst_remainder_coefficient = max(worst_remainder_coefficient, coefficient)
    require(worst_packet < TOL, "PLSZ-C3 packet factorization failed")
    require(
        worst_remainder_coefficient < 10.0,
        "PLSZ-C3 first-jet remainder failed",
    )
    return worst_packet, worst_remainder_coefficient


def component_nonuniqueness_gate(red_split: bool) -> tuple[float, float]:
    """Show that an untyped split is not determined by its scalar sum."""
    maximum_sum_error = 0.0
    minimum_linear_ratio = math.inf
    for epsilon in (0.04, 0.02, 0.01, 0.005):
        total = complex(0.2 * epsilon * epsilon, epsilon)
        shift = complex(0.3, -0.2) * epsilon
        descendant = total + shift
        orthogonal = -shift
        if red_split:
            orthogonal = 0j
        reconstructed = descendant + orthogonal
        maximum_sum_error = max(maximum_sum_error, abs(total - reconstructed))
        minimum_linear_ratio = min(minimum_linear_ratio, abs(shift) / epsilon)
    require(maximum_sum_error < TOL, "PLSZ-C4 compensating component split failed")
    require(minimum_linear_ratio > 0.3, "PLSZ-C4 linear ambiguity was not live")
    return maximum_sum_error, minimum_linear_ratio


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--red-profile", action="store_true")
    parser.add_argument("--red-ward-factor", action="store_true")
    parser.add_argument("--red-slope", action="store_true")
    parser.add_argument("--red-split", action="store_true")
    args = parser.parse_args()
    red_count = sum(
        int(flag)
        for flag in (
            args.red_profile,
            args.red_ward_factor,
            args.red_slope,
            args.red_split,
        )
    )
    require(red_count <= 1, "select at most one registered red mutation")
    return args


def main() -> None:
    args = parse_args()
    c1 = c1_profile_gate(args.red_profile)
    c2 = exact_factor_gate(args.red_ward_factor)
    c3a, c3b = packet_and_slope_gate(args.red_slope)
    c4a, c4b = component_nonuniqueness_gate(args.red_split)
    print(f"PLSZ-C1 max scaled extension error = {c1:.6e}")
    print(f"PLSZ-C2 max exact factor error = {c2:.6e}")
    print(f"PLSZ-C3 max packet error = {c3a:.6e}")
    print(f"PLSZ-C3 max quadratic coefficient = {c3b:.6e}")
    print(f"PLSZ-C4 max invariant-sum error = {c4a:.6e}")
    print(f"PLSZ-C4 min live linear-shift ratio = {c4b:.6e}")
    print("PASS")


if __name__ == "__main__":
    main()
