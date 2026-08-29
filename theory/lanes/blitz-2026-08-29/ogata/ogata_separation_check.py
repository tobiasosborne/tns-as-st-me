#!/usr/bin/env python3
"""Red-capable arithmetic check for the D26/SPT-edge separation witness."""

from __future__ import annotations

import argparse
import cmath
import math


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--red", action="store_true")
    args = parser.parse_args()

    onsite_weights = (-1.0, 0.0, 1.0)
    onsite_circle_residual = max(
        abs(cmath.exp(2j * math.pi * weight) - 1.0)
        for weight in onsite_weights
    )

    b = 1.0 / math.sqrt(3.0)
    transfer_eigenvalue = 2.0 * b * b - 1.0
    window_length = 24
    prefactor = 1.0 if args.red else 0.5
    edge_magnitude = prefactor * (1.0 - transfer_eigenvalue**window_length)
    edge_limit_error = abs(edge_magnitude - 0.5)

    onsite_ok = onsite_circle_residual < 1.0e-12
    edge_ok = edge_limit_error < 2.0e-11

    print(f"onsite_2pi_residual={onsite_circle_residual:.3e}")
    print(f"aklt_L={window_length}")
    print(f"aklt_edge_magnitude={edge_magnitude:.15f}")
    print(f"edge_limit_error={edge_limit_error:.3e}")

    if onsite_ok and edge_ok:
        print("PASS: microscopic offset 0 coexists with half-edge limit")
        return 0
    if args.red:
        print("RED-OK: wrong edge prefactor was detected")
    else:
        print("FAIL: registered separation witness did not pass")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
