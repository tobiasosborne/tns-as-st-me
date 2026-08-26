#!/usr/bin/env python3
"""Independent certificate for Theorem S2-2body-S.

The checker has four deliberately separate inputs:

1. the theorem's rational ``S_12``;
2. the independently derived ``n/(-conj(n))`` form;
3. the frozen spin-1/2 oracle ratio and Taylor coefficients; and
4. a two-magnon ring Hamiltonian assembled directly from spin ladder matrix
   elements, with no call to either closed-form implementation in numerics/.

Every failure raises ``SystemExit(1)`` and therefore remains active under
``python3 -O``.  There are no optimization-sensitive checks.

Red mode
--------
``python3 theory/checks/spin_s_slope_check.py --red`` replaces ``(2S-1)``
in ``mu`` by ``(2S+1)`` while all independent targets remain frozen.  The
Laurent-polynomial identity must fail and the process must exit with status 1.
"""

from __future__ import annotations

import argparse
import sys

import numpy as np
import sympy as sp


GRID_TOL = 3.0e-13
SLOPE_TOL = 2.0e-9
RING_TOL = 5.0e-11


def fail(message: str) -> None:
    print(f"FAIL: {message}", file=sys.stderr)
    raise SystemExit(1)


def require(condition: bool, message: str) -> None:
    if not condition:
        fail(message)


def exact_zero(expression: sp.Expr, message: str) -> None:
    residue = sp.factor(sp.together(expression))
    require(residue == 0, f"{message}: nonzero symbolic residue")


def scattering_formula(k1: float, k2: float, two_s: int, red: bool = False) -> complex:
    """Theorem ratio A12/A21; red mode mutates the coefficient in mu."""
    site_spin = two_s / 2.0
    z1 = np.exp(1j * k1)
    z2 = np.exp(1j * k2)
    a = 1.0 + z1 * z2
    b = z1 + z2
    shift = 2 if red else 0
    mu = (two_s - 1 + shift) * a + b
    return (site_spin * a * b - z1 * mu) / (
        z2 * mu - site_spin * a * b
    )


def scattering_independent(k1: float, k2: float, two_s: int) -> complex:
    """Independent contact result n/(-conj(n)) from center/relative momenta."""
    site_spin = two_s / 2.0
    total = k1 + k2
    relative = (k1 - k2) / 2.0
    center_cosine = np.cos(total / 2.0)
    relative_cosine = np.cos(relative)
    numerator = (
        2.0 * site_spin * center_cosine * relative_cosine
        - np.exp(1j * relative)
        * ((2.0 * site_spin - 1.0) * center_cosine + relative_cosine)
    )
    return numerator / (-np.conjugate(numerator))


def frozen_half_scattering(k1: float, k2: float) -> complex:
    """Frozen D7/oracle spin-1/2 ratio, written independently."""
    z1 = np.exp(1j * k1)
    z2 = np.exp(1j * k2)
    return -(z1 * z2 - 2.0 * z1 + 1.0) / (
        z1 * z2 - 2.0 * z2 + 1.0
    )


def velocity(momentum: float, two_s: int) -> float:
    """Set J=1; its positive factor cancels from velocity ordering."""
    return two_s * np.sin(momentum)


def physical_scattering(soft: float, hard: float, two_s: int) -> complex:
    ratio = scattering_formula(soft, hard, two_s)
    if velocity(hard, two_s) > velocity(soft, two_s):
        return ratio
    return 1.0 / ratio


def check_symbolic_identities(red: bool) -> tuple[sp.Expr, sp.Expr]:
    """Prove the independent Laurent identity and the exact soft derivative."""
    u, r, site_spin = sp.symbols("u r S", nonzero=True)
    z1 = u * r
    z2 = u / r
    a = 1 + z1 * z2
    b = z1 + z2
    shift = 2 if red else 0
    mu = (2 * site_spin - 1 + shift) * a + b
    rational = (site_spin * a * b - z1 * mu) / (
        z2 * mu - site_spin * a * b
    )

    center_cosine = (u + 1 / u) / 2
    relative_cosine = (r + 1 / r) / 2
    n_value = (
        2 * site_spin * center_cosine * relative_cosine
        - r * ((2 * site_spin - 1) * center_cosine + relative_cosine)
    )
    n_conjugate = n_value.xreplace({u: 1 / u, r: 1 / r})
    independent = n_value / (-n_conjugate)
    exact_zero(rational - independent, "SS-C3 independent closed forms")

    x, y = sp.symbols("x y", nonzero=True)
    a_xy = 1 + x * y
    b_xy = x + y
    mu_xy = (2 * site_spin - 1 + shift) * a_xy + b_xy
    ratio_xy = (site_spin * a_xy * b_xy - x * mu_xy) / (
        y * mu_xy - site_spin * a_xy * b_xy
    )
    derivative = sp.I * x * sp.diff(ratio_xy, x) / ratio_xy
    derivative_at_zero = sp.factor(derivative.subs(x, 1))
    exact_zero(
        derivative_at_zero - sp.I / site_spin,
        "SS-C4 exact logarithmic slope",
    )
    return sp.Integer(0), sp.simplify(derivative_at_zero)


def check_grid(red: bool) -> tuple[float, float, float]:
    """Compare independent forms, unitarity, and exchange on a real grid."""
    pairs = (
        (-1.30, 0.40),
        (0.17, 1.20),
        (-0.35, -2.10),
        (2.40, -0.70),
        (0.60, 2.20),
    )
    form_error = 0.0
    unitary_error = 0.0
    exchange_error = 0.0
    for two_s in range(1, 9):
        for k1, k2 in pairs:
            subject = scattering_formula(k1, k2, two_s, red=red)
            independent = scattering_independent(k1, k2, two_s)
            exchanged = scattering_formula(k2, k1, two_s, red=red)
            form_error = max(form_error, abs(subject - independent))
            unitary_error = max(unitary_error, abs(abs(subject) - 1.0))
            exchange_error = max(exchange_error, abs(subject * exchanged - 1.0))
    require(form_error < GRID_TOL, f"SS-C3 grid closed-form error {form_error:.3e}")
    require(
        unitary_error < GRID_TOL,
        f"SS-C3 grid unitarity error {unitary_error:.3e}",
    )
    require(
        exchange_error < GRID_TOL,
        f"SS-C3 grid exchange error {exchange_error:.3e}",
    )
    return form_error, unitary_error, exchange_error


def five_point_phase_derivative(hard: float, two_s: int) -> float:
    """Differentiate the phase branch through one using a five-point stencil."""
    step = 2.0e-4
    phases = {
        multiple: np.angle(physical_scattering(multiple * step, hard, two_s))
        for multiple in (-2, -1, 1, 2)
    }
    return (
        phases[-2] - 8.0 * phases[-1] + 8.0 * phases[1] - phases[2]
    ) / (12.0 * step)


def check_physical_slope() -> float:
    """Check sgn(v_h-v_s)/S on both hard half-zones."""
    slope_error = 0.0
    for two_s in range(1, 9):
        site_spin = two_s / 2.0
        for hard in (-2.40, -1.10, -0.37, 0.37, 1.10, 2.40):
            measured = five_point_phase_derivative(hard, two_s)
            sign = np.sign(velocity(hard, two_s) - velocity(0.0, two_s))
            expected = sign / site_spin
            slope_error = max(slope_error, abs(measured - expected))
    require(slope_error < SLOPE_TOL, f"SS-C4 physical slope error {slope_error:.3e}")
    return slope_error


def check_half_spin_freeze() -> tuple[float, sp.Expr, sp.Expr, sp.Expr]:
    """Recover the frozen ratio, slope 2, and both quadratic coefficients."""
    ratio_error = 0.0
    for k1, k2 in ((0.13, 0.70), (-0.21, 1.40), (0.31, 2.60)):
        ratio_error = max(
            ratio_error,
            abs(scattering_formula(k1, k2, 1) - frozen_half_scattering(k1, k2)),
        )
    require(ratio_error < GRID_TOL, f"SS-C5 frozen ratio error {ratio_error:.3e}")

    x, y = sp.symbols("x y", nonzero=True)
    a = 1 + x * y
    b = x + y
    site_spin = sp.Rational(1, 2)
    mu = b
    ratio = (site_spin * a * b - x * mu) / (
        y * mu - site_spin * a * b
    )

    def momentum_derivative(expression: sp.Expr) -> sp.Expr:
        return sp.I * x * sp.diff(expression, x)

    first_log = momentum_derivative(ratio) / ratio
    second_log = momentum_derivative(first_log)
    second_ratio = momentum_derivative(momentum_derivative(ratio))
    slope = sp.factor(first_log.subs(x, 1))
    phase_quadratic_times_i = sp.factor(second_log.subs(x, 1) / 2)
    amplitude_quadratic = sp.factor(second_ratio.subs(x, 1) / 2)

    cotangent = sp.I * (1 + y) / (y - 1)
    exact_zero(slope - 2 * sp.I, "SS-C5 frozen slope 2")
    exact_zero(
        phase_quadratic_times_i - sp.I * cotangent,
        "SS-C5 frozen phase quadratic cot(k_h/2)",
    )
    exact_zero(
        amplitude_quadratic - (sp.I * cotangent - 2),
        "SS-C5 frozen amplitude quadratic",
    )
    return ratio_error, slope, phase_quadratic_times_i, amplitude_quadratic


def ring_hamiltonian(number_sites: int, two_s: int) -> tuple[np.ndarray, list[tuple[int, int]]]:
    """Assemble the two-magnon ring block solely from occupation transitions."""
    site_spin = two_s / 2.0
    basis = [
        (x, y)
        for x in range(number_sites)
        for y in range(x, number_sites)
        if x != y or two_s >= 2
    ]
    index = {pair: position for position, pair in enumerate(basis)}
    hamiltonian = np.zeros((len(basis), len(basis)), dtype=float)

    def occupation(site: int, pair: tuple[int, int]) -> int:
        return int(site == pair[0]) + int(site == pair[1])

    def raising(number: int) -> float:
        return np.sqrt(number * (two_s - number + 1))

    def lowering(number: int) -> float:
        return np.sqrt((number + 1) * (two_s - number))

    for column, pair in enumerate(basis):
        x, y = pair
        adjacent = x != y and (
            (y - x) % number_sites == 1 or (x - y) % number_sites == 1
        )
        hamiltonian[column, column] = 4.0 * site_spin - float(adjacent)
        occupied_sites = ((x, 2),) if x == y else ((x, 1), (y, 1))
        for source, source_number in occupied_sites:
            for direction in (-1, 1):
                target = (source + direction) % number_sites
                target_number = occupation(target, pair)
                if target_number >= two_s:
                    continue
                amplitude = (
                    -0.5 * raising(source_number) * lowering(target_number)
                )
                other = x if x == y else (y if source == x else x)
                moved_pair = tuple(sorted((other, target)))
                hamiltonian[index[moved_pair], column] += amplitude
    hermiticity = np.linalg.norm(hamiltonian - hamiltonian.T)
    require(hermiticity < 1.0e-14, f"SS-C6 ring Hermiticity {hermiticity:.3e}")
    return hamiltonian, basis


def quantized_pair(number_sites: int, n1: int, n2: int, two_s: int) -> tuple[float, float]:
    """Solve the two Bethe-Yang seam equations by contractive iteration."""
    k1 = 2.0 * np.pi * n1 / number_sites
    k2 = 2.0 * np.pi * n2 / number_sites
    change = np.inf
    for _ in range(1000):
        phase = np.angle(scattering_formula(k1, k2, two_s))
        next_k1 = (2.0 * np.pi * n1 + phase) / number_sites
        next_k2 = (2.0 * np.pi * n2 - phase) / number_sites
        change = max(abs(next_k1 - k1), abs(next_k2 - k2))
        k1, k2 = next_k1, next_k2
        if change < 1.0e-14:
            break
    require(change < 1.0e-12, f"SS-C6 Bethe-Yang iteration {change:.3e}")
    return k1, k2


def check_ring_residual() -> float:
    """Check the full periodic eigenvalue residual for four site spins."""
    number_sites = 11
    maximum_residual = 0.0
    for two_s in (1, 2, 3, 4):
        k1, k2 = quantized_pair(number_sites, 1, 3, two_s)
        ratio = scattering_formula(k1, k2, two_s)
        z1 = np.exp(1j * k1)
        z2 = np.exp(1j * k2)
        if two_s == 1:
            double_amplitude = 0.0j
        else:
            site_spin = two_s / 2.0
            double_amplitude = (
                np.sqrt((two_s - 1) / site_spin)
                * (ratio * z2 + z1)
                / (z1 + z2)
            )

        hamiltonian, basis = ring_hamiltonian(number_sites, two_s)
        total_momentum = k1 + k2
        vector = np.asarray(
            [
                double_amplitude * np.exp(1j * total_momentum * x)
                if x == y
                else ratio * np.exp(1j * (k1 * x + k2 * y))
                + np.exp(1j * (k2 * x + k1 * y))
                for x, y in basis
            ],
            dtype=complex,
        )
        energy = two_s * (
            (1.0 - np.cos(k1)) + (1.0 - np.cos(k2))
        )
        residual = np.linalg.norm(hamiltonian @ vector - energy * vector) / np.linalg.norm(vector)
        maximum_residual = max(maximum_residual, residual)
    require(
        maximum_residual < RING_TOL,
        f"SS-C6 full-ring eigenvalue residual {maximum_residual:.3e}",
    )
    return maximum_residual


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--red",
        action="store_true",
        help="mutate (2S-1) to (2S+1); an exit status of 1 is expected",
    )
    arguments = parser.parse_args()

    _, symbolic_slope = check_symbolic_identities(arguments.red)
    form_error, unitary_error, exchange_error = check_grid(arguments.red)
    slope_error = check_physical_slope()
    half_error, half_slope, half_phase2, half_amplitude2 = check_half_spin_freeze()
    ring_residual = check_ring_residual()

    print(f"SYMBOLIC independent=0 dlog={symbolic_slope}")
    print(
        "GRID "
        f"closed={form_error:.3e} unitary={unitary_error:.3e} "
        f"exchange={exchange_error:.3e}"
    )
    print(f"SLOPE physical_sign_error={slope_error:.3e}")
    print(
        "HALF "
        f"ratio={half_error:.3e} slope={half_slope} "
        f"phase2={half_phase2} amplitude2={half_amplitude2}"
    )
    print(f"RING max_residual={ring_residual:.3e}")
    print("PASS: Theorem S2-2body-S")


if __name__ == "__main__":
    main()
