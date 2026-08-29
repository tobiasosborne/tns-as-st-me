#!/usr/bin/env python3
"""Red-capable certificate for the D16 finite-window moment-map identity.

Green mode compares two independently implemented routes on the spin-1/2
D16 family:

* geometry: the mixed Wirtinger derivative of the norm of the holomorphic
  window lift, converted to the coefficient of ``dx0 wedge dphi``;
* observable: a complex-step derivative of the D13(a)/(IDX.1) expectation,
  assembled directly from the site-normalised one-spin probabilities.

``--red`` mutates the outer D13(a) calibration ``2s`` to ``2s+1``.  Since
``s=1/2`` in D16, this changes the multiplier from one to two while leaving
the geometry untouched.  Exit 1 in red mode means the mutation was caught;
exit 2 means the checker lacked teeth.  There are no ``assert`` statements,
so ``python3 -O`` follows the same paths.

This is a finite-grid falsifier/certificate, not the analytic proof.  The
proof is in ``ba-mm-fin.md``.
"""

from __future__ import annotations

import argparse
import math
import sys

import numpy as np


DELTAS = (1.05, 1.5, 2.0, 4.0)
WINDOWS = ((-10, 10, 0), (-7, 13, 2), (0, 9, 4), (-3, 2, -1))
X0_GRID = np.linspace(-2.25, 3.25, 221)
COMPLEX_STEP = 1.0e-30
RTOL = 2.0e-12
ATOL = 2.0e-13


def require(condition: bool, message: str) -> None:
    if not condition:
        print(f"FAIL: {message}", file=sys.stderr)
        raise SystemExit(1)


def d16_parameters(delta: float) -> tuple[float, float]:
    """Return D16's q and kappa, checking their frozen range."""
    q = delta - math.sqrt(delta * delta - 1.0)
    kappa = -math.log(q)
    require(0.0 < q < 1.0, f"D16 range failed at Delta={delta}")
    require(kappa > 0.0, f"kappa positivity failed at Delta={delta}")
    return q, kappa


def omega_geometry(delta: float, x0: float, a: int, b: int) -> float:
    """Geometry route: i d dbar log ||Psi_W(z)||^2.

    For the holomorphic lift, K_{z,zbar} is accumulated in the first loop.
    Only afterwards is i dz wedge dzbar converted to dx0 wedge dphi.  This
    routine never calls the observable route and shares no intermediate with
    it.
    """
    q, kappa = d16_parameters(delta)
    abs_z_squared = q ** (-2.0 * x0)
    kahler_mixed = 0.0
    for n in range(a, b + 1):
        q_to_2n = q ** (2 * n)
        denominator = 1.0 + abs_z_squared * q_to_2n
        kahler_mixed += q_to_2n / (denominator * denominator)
    return 2.0 * kappa * abs_z_squared * kahler_mixed


def mu_observable(
    delta: float,
    x0: complex,
    a: int,
    b: int,
    cut: int,
    calibration: float,
) -> complex:
    """Observable route: D13(a)/(IDX.1) from normalised site probabilities."""
    _, kappa = d16_parameters(delta)
    up_count = 0.0j
    for n in range(a, b + 1):
        # Analytic continuation of |z q^n|^2 = exp(2*kappa*(x0-n)).
        ratio = np.exp(2.0 * kappa * (x0 - n))
        up_count += 1.0 / (1.0 + ratio)
    # In D16, 2s=1.  The red mutation replaces it by 2s+1=2.
    return calibration * (a - 1 - cut + up_count)


def dmu_observable(
    delta: float,
    x0: float,
    a: int,
    b: int,
    cut: int,
    calibration: float,
) -> float:
    """Complex-step derivative of the independently assembled expectation."""
    value = mu_observable(
        delta, x0 + 1.0j * COMPLEX_STEP, a, b, cut, calibration
    )
    return float(value.imag / COMPLEX_STEP)


def sweep(calibration: float) -> tuple[float, float, float, int]:
    max_scaled_residual = 0.0
    max_absolute_residual = 0.0
    min_omega = math.inf
    cases = 0
    for delta in DELTAS:
        for a, b, cut in WINDOWS:
            require(a <= cut <= b, f"cut {cut} is outside [{a},{b}]")
            for x0 in X0_GRID:
                omega = omega_geometry(delta, float(x0), a, b)
                dmu = dmu_observable(delta, float(x0), a, b, cut, calibration)
                residual = abs(dmu + omega)
                scale = ATOL + RTOL * max(1.0, abs(omega), abs(dmu))
                max_scaled_residual = max(max_scaled_residual, residual / scale)
                max_absolute_residual = max(max_absolute_residual, residual)
                min_omega = min(min_omega, omega)
                cases += 1
    return max_scaled_residual, max_absolute_residual, min_omega, cases


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--red",
        action="store_true",
        help="mutate 2s to 2s+1; exit 1 means the mutation was caught",
    )
    args = parser.parse_args()

    calibration = 2.0 if args.red else 1.0
    max_scaled_residual, max_absolute_residual, min_omega, cases = sweep(calibration)
    identity_holds = max_scaled_residual <= 1.0
    positivity_holds = min_omega > 0.0

    print(f"mode={'RED' if args.red else 'GREEN'}")
    print(f"cases={cases}")
    print(f"calibration={calibration:.1f}")
    print(f"max_absolute_residual={max_absolute_residual:.6e}")
    print(f"max_scaled_residual={max_scaled_residual:.6e}")
    print(f"min_omega={min_omega:.6e}")

    if args.red:
        if (not identity_holds) and positivity_holds:
            print("RED-OK: mutated calibration was caught")
            return 1
        print("RED-NOT-CAUGHT: mutation did not isolate the identity gate")
        return 2

    if not positivity_holds:
        print("FAIL: geometry route produced a nonpositive coefficient")
        return 1
    if not identity_holds:
        print("FAIL: dmu + Omega exceeded the registered tolerance")
        return 1
    print("PASS: dmu = i_(d/dphi) omega on the registered D16 grid")
    return 0


if __name__ == "__main__":
    sys.exit(main())
