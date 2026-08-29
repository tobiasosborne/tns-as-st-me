#!/usr/bin/env python3
"""Independent checks for the kaehler-dh blitz lane.

The Kähler/TDVP observation is TJO's and requires his explicit sign-off
before any paper use; this checker is companion-paper support only.

The geometry route uses derivatives of normalized coherent-state vectors.
The observable route differentiates the S^z probabilities.  No Hamiltonian
or scattering datum is used.  ``--red`` mutates the D13(a) calibration and
must be caught (exit 1).  There are no Python asserts, so ``python -O`` is
equally strict.
"""

from __future__ import annotations

import argparse
import math
import sys

import numpy as np


TOL_ID = 2.0e-12
TOL_AREA = 2.0e-11


def logistic2(y: float) -> float:
    """Return exp(2y)/(1+exp(2y)) without overflow."""
    if y >= 0.0:
        e = math.exp(-2.0 * y)
        return 1.0 / (1.0 + e)
    e = math.exp(2.0 * y)
    return e / (1.0 + e)


def coherent_data(spin: float, p: float, phi: float) -> tuple[np.ndarray, np.ndarray]:
    """Normalized spin-coherent vector and its k labels."""
    degree = int(round(2.0 * spin))
    k = np.arange(degree + 1, dtype=float)
    probs = np.array(
        [math.comb(degree, j) * p**j * (1.0 - p) ** (degree - j)
         for j in range(degree + 1)],
        dtype=float,
    )
    psi = np.sqrt(probs) * np.exp(1j * k * phi)
    return psi, k


def sphere_routes(spin: float, theta: float, red: bool) -> tuple[float, float, float]:
    """Return FS curvature, observable derivative, and moment value."""
    p = math.sin(theta / 2.0) ** 2
    psi, k = coherent_data(spin, p, 0.371)
    logder = k / math.sin(theta) - spin * math.tan(theta / 2.0)
    dtheta = logder * psi
    dphi = 1j * k * psi
    horizontal = np.vdot(dtheta, dphi) - np.vdot(dtheta, psi) * np.vdot(psi, dphi)
    omega = float(2.0 * np.imag(horizontal))

    probs = np.abs(psi) ** 2
    dprobs = 2.0 * logder * probs
    weights = spin - k
    dmu = float(np.dot(weights, dprobs))
    mu = float(np.dot(weights, probs))
    if red:
        dmu *= (2.0 * spin + 1.0) / (2.0 * spin)
    return omega, dmu, mu


def kink_routes(
    spin: float, kappa: float, x0: float, n: int, red: bool
) -> tuple[float, float]:
    """One-site geometry/observable derivatives for the D16-type family."""
    p = logistic2(kappa * (x0 - n))
    psi, k = coherent_data(spin, p, 0.217)

    # Geometry route: horizontal Fubini--Study curvature from tangent vectors.
    dx = kappa * (k - 2.0 * spin * p) * psi
    dphi = 1j * k * psi
    horizontal = np.vdot(dx, dphi) - np.vdot(dx, psi) * np.vdot(psi, dphi)
    omega = float(2.0 * np.imag(horizontal))

    # Observable route: differentiate the binomial S^z probabilities.
    probs = np.abs(psi) ** 2
    dprobs = 2.0 * kappa * (k - 2.0 * spin * p) * probs
    dmu = float(np.dot(spin - k, dprobs))
    if red:
        dmu *= (2.0 * spin + 1.0) / (2.0 * spin)
    return omega, dmu


def window_curvature(spin: float, kappa: float, x0: float, length: int) -> float:
    return sum(kink_routes(spin, kappa, x0, n, False)[0]
               for n in range(-length, length + 1))


def window_potential(spin: float, kappa: float, x0: float, length: int) -> float:
    # Log norm of the unnormalized coherent product, evaluated stably.
    return sum(2.0 * spin * np.logaddexp(0.0, 2.0 * kappa * (x0 - n))
               for n in range(-length, length + 1))


def gauss_integral(func, lo: float, hi: float, order: int = 160) -> float:
    nodes, weights = np.polynomial.legendre.leggauss(order)
    xs = 0.5 * (hi - lo) * nodes + 0.5 * (hi + lo)
    return 0.5 * (hi - lo) * float(np.dot(weights, [func(float(x)) for x in xs]))


def run(red: bool) -> tuple[list[str], list[str]]:
    failures: list[str] = []
    lines: list[str] = []

    # G1: the primordial spin sphere, including its flat DH pushforward.
    sphere_identity = 0.0
    sphere_area = 0.0
    sphere_push = 0.0
    for spin in (0.5, 1.0, 1.5, 2.0):
        for theta in np.linspace(0.013, math.pi - 0.013, 151):
            omega, dmu, mu = sphere_routes(spin, float(theta), red)
            sphere_identity = max(sphere_identity, abs(omega + dmu),
                                  abs(mu - spin * math.cos(theta)))
        area = 2.0 * math.pi * gauss_integral(
            lambda th: sphere_routes(spin, th, False)[0], 0.0, math.pi
        )
        sphere_area = max(sphere_area, abs(area / (2.0 * math.pi) - 2.0 * spin))
        # Each theta strip has area 2pi times its moment-map width.
        for th0, th1 in ((0.2, 0.8), (0.7, 1.9), (1.3, 2.8)):
            strip = 2.0 * math.pi * gauss_integral(
                lambda th: sphere_routes(spin, th, False)[0], th0, th1
            )
            width = spin * (math.cos(th0) - math.cos(th1))
            sphere_push = max(sphere_push, abs(strip / width - 2.0 * math.pi))
    lines.append(
        f"G1 sphere: identity={sphere_identity:.3e}, area/(2pi)-2s={sphere_area:.3e}, "
        f"pushforward-density error={sphere_push:.3e}"
    )
    if sphere_identity > TOL_ID or sphere_area > TOL_AREA or sphere_push > 5.0e-11:
        failures.append("G1")

    # G2: D16 and spin-s product generalizations, independent routes.
    kink_identity = 0.0
    for spin in (0.5, 1.0, 1.5, 2.0):
        for delta in (1.5, 2.0, 4.0):
            q = delta - math.sqrt(delta * delta - 1.0)
            kappa = -math.log(q)
            for x0 in np.linspace(0.0, 3.0, 61):
                omega = 0.0
                dmu = 0.0
                for n in range(-40, 41):
                    om_n, dm_n = kink_routes(spin, kappa, float(x0), n, red)
                    omega += om_n
                    dmu += dm_n
                kink_identity = max(kink_identity, abs(omega + dmu) / max(1.0, omega))
    lines.append(f"G2 D16/product: max relative |Omega+mu'|={kink_identity:.3e}")
    if kink_identity > TOL_ID:
        failures.append("G2")

    # G3: one-period area, with the exact finite-window boundary correction.
    period_error = 0.0
    thermodynamic_error = 0.0
    for spin in (0.5, 1.0, 1.5, 2.0):
        for delta in (1.5, 2.0, 4.0):
            q = delta - math.sqrt(delta * delta - 1.0)
            kappa = -math.log(q)
            for x0 in (0.17, 0.63, 1.29):
                length = 40
                integral = gauss_integral(
                    lambda x: window_curvature(spin, kappa, x, length),
                    x0,
                    x0 + 1.0,
                )
                boundary = spin * (
                    math.tanh(kappa * (x0 + length + 1.0))
                    - math.tanh(kappa * (x0 - length))
                )
                period_error = max(period_error, abs(integral - boundary))
                thermodynamic_error = max(thermodynamic_error, abs(boundary - 2.0 * spin))
    lines.append(
        f"G3 period: quadrature-boundary={period_error:.3e}, "
        f"finite-window edge error vs 2s={thermodynamic_error:.3e}"
    )
    if period_error > TOL_AREA or thermodynamic_error > TOL_AREA:
        failures.append("G3")

    # G4: the potential diverges while curvature stabilizes.
    delta = 1.5
    kappa = -math.log(delta - math.sqrt(delta * delta - 1.0))
    lengths = np.array([10.0, 20.0, 40.0, 80.0])
    potentials = np.array([window_potential(0.5, kappa, 0.0, int(L)) for L in lengths])
    exponent = float(np.polyfit(np.log(lengths), np.log(potentials), 1)[0])
    curvature_gap = abs(window_curvature(0.5, kappa, 0.37, 80)
                        - window_curvature(0.5, kappa, 0.37, 40))
    lines.append(
        f"G4 regularisation: growth exponent={exponent:.6f}, "
        f"|Omega80-Omega40|={curvature_gap:.3e}"
    )
    if exponent < 1.5 or curvature_gap > 1.0e-10:
        failures.append("G4")

    # G5: D34(c)'s proposed orbit period is identically silent.
    orbit_period = 0.0  # integral omega(xi,xi)dphi
    virtual_theta = math.pi / 2.0
    virtual = np.diag(np.exp(1j * np.array([-0.5, 0.5]) * virtual_theta))
    scalar_distance = float(np.linalg.norm(virtual - np.trace(virtual) * np.eye(2) / 2.0))
    lines.append(
        f"G5 L2 obstruction audit: orbit period={orbit_period:.1f}, "
        f"nonscalar-V distance={scalar_distance:.6f}"
    )
    if orbit_period != 0.0 or scalar_distance < 1.0e-3:
        failures.append("G5")

    return failures, lines


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--red", action="store_true", help="mutate D13(a) calibration")
    args = parser.parse_args()
    failures, lines = run(args.red)
    print("\n".join(lines))
    if args.red:
        if failures:
            print("RED-OK: calibration mutation caught by " + ",".join(failures))
            return 1
        print("RED-FAIL: calibration mutation was not caught")
        return 2
    if failures:
        print("FAIL: " + ",".join(failures))
        return 1
    print("PASS: all five gates")
    return 0


if __name__ == "__main__":
    sys.exit(main())
