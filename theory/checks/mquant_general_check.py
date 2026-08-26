#!/usr/bin/env python3
"""Arithmetic certificate for Theorem M-quant-G.

The checks are exact SymPy identities and remain active under ``python3 -O``.
They cover the general charge subtraction, an SU(2) vacuum pair with unbroken
U(1), a rank-two abelian factor, and the frozen spin-1/2 XXZ values.

``--red`` changes the transmitted primitive charge from +1 to -1 while the
theorem target remains ``-1/s``.  The general-law check must then exit 1.
This is a deliberate charge-label mutation, not a floating-point tolerance.
"""

from __future__ import annotations

import argparse
import sys

import sympy as sp


def fail(message: str) -> None:
    print(f"FAIL: {message}", file=sys.stderr)
    raise SystemExit(1)


def require(condition: bool, message: str) -> None:
    if not condition:
        fail(message)


def exact_zero(expression: sp.Expr, message: str) -> None:
    residue = sp.simplify(expression)
    require(residue == 0, f"{message}: residue={residue}")


def displacement(s: sp.Symbol | sp.Rational, q_in: sp.Expr, q_out: sp.Expr) -> sp.Expr:
    """Solve 2*s*delta + (q_out-q_in) = 0 exactly."""
    return sp.cancel(-(q_out - q_in) / (2 * s))


def check_window_calibration() -> sp.Expr:
    """Check the scalar terms in the exact finite-window identity (G.3)."""
    a, b, cut = sp.symbols("a b cut", integer=True)
    s = sp.symbols("s", positive=True, finite=True, nonzero=True)
    left_scalar = -s * (cut - a + 1) + s * (b - cut)
    d13_scalar = 2 * s * (a - 1 - cut) + s * (b - a + 1)
    residue = sp.expand(left_scalar - d13_scalar)
    exact_zero(residue, "D13 finite-window charge calibration")
    return residue


def check_general_arithmetic(red: bool) -> tuple[sp.Expr, sp.Expr, sp.Expr]:
    s = sp.symbols("s", positive=True, finite=True, nonzero=True)
    transmission = sp.symbols("T", real=True)
    q_in = sp.Integer(-1)
    q_reflected = sp.Integer(-1)
    q_transmitted = sp.Integer(-1) if red else sp.Integer(1)

    dx_reflected = displacement(s, q_in, q_reflected)
    dx_transmitted = displacement(s, q_in, q_transmitted)
    exact_zero(dx_reflected, "reflected channel should have zero displacement")
    exact_zero(dx_transmitted + 1 / s, "transmitted quantum is not -1/s")

    mean = sp.expand((1 - transmission) * dx_reflected + transmission * dx_transmitted)
    second_moment = sp.expand(
        (1 - transmission) * dx_reflected**2 + transmission * dx_transmitted**2
    )
    variance = sp.factor(second_moment - mean**2)
    exact_zero(mean + transmission / s, "two-channel expectation law")
    exact_zero(
        variance - transmission * (1 - transmission) / s**2,
        "two-channel variance law",
    )

    m_initial, cut = sp.symbols("m_initial cut", integer=True)
    total_in = 2 * s * (m_initial - cut) + q_in
    total_transmitted = (
        2 * s * (m_initial + dx_transmitted - cut) + q_transmitted
    )
    exact_zero(total_transmitted - total_in, "regularised total charge conservation")
    return dx_reflected, dx_transmitted, mean


def check_su2_broken_to_u1() -> sp.Expr:
    """Fundamental SU(2): north/south vacua share the diagonal U(1)."""
    imaginary = sp.I
    sigma_x = sp.Matrix([[0, 1], [1, 0]])
    sigma_z = sp.Matrix([[1, 0], [0, -1]])
    charge = sigma_z / 2
    up = sp.Matrix([1, 0])
    down = sp.Matrix([0, 1])
    broken_rotation = -imaginary * sigma_x

    require(
        broken_rotation * up == -imaginary * down,
        "SU(2) element does not map vacua",
    )
    q_up = (up.T.conjugate() * charge * up)[0]
    q_down = (down.T.conjugate() * charge * down)[0]
    exact_zero(q_up - sp.Rational(1, 2), "SU(2) north-vacuum charge")
    exact_zero(q_down + sp.Rational(1, 2), "SU(2) south-vacuum charge")

    theta = sp.symbols("theta", real=True)
    u1 = sp.diag(sp.exp(imaginary * theta / 2), sp.exp(-imaginary * theta / 2))
    require(
        sp.simplify(u1 * up - sp.exp(imaginary * theta / 2) * up) == sp.zeros(2, 1),
        "north vacuum is not U(1)-stable",
    )
    require(
        sp.simplify(u1 * down - sp.exp(-imaginary * theta / 2) * down) == sp.zeros(2, 1),
        "south vacuum is not U(1)-stable",
    )

    dx = displacement(sp.Rational(1, 2), sp.Integer(-1), sp.Integer(1))
    exact_zero(dx + 2, "SU(2)->U(1) memory quantum")
    return dx


def check_rank_two_abelian_factor() -> tuple[sp.Expr, sp.Expr]:
    """T^2=U(1)xU(1): first component moves the wall; second is spectator."""
    s = sp.symbols("s", positive=True, finite=True, nonzero=True)
    q_in = sp.Matrix([-1, 2])
    q_out = sp.Matrix([1, 2])
    vacuum_jump = sp.Matrix([2 * s, 0])
    dx = displacement(s, q_in[0], q_out[0])

    residue = sp.simplify(vacuum_jump * dx + (q_out - q_in))
    require(residue == sp.zeros(2, 1), f"T^2 vector conservation residue={residue}")
    exact_zero(dx + 1 / s, "T^2 selected-component quantum")
    return dx, sp.simplify(q_out[1] - q_in[1])


def check_xxz_instantiation() -> tuple[sp.Expr, sp.Expr, sp.Expr, sp.Expr]:
    transmission, delta = sp.symbols("T Delta", real=True)
    s = sp.Rational(1, 2)
    dx_reflected = displacement(s, sp.Integer(-1), sp.Integer(-1))
    dx_transmitted = displacement(s, sp.Integer(-1), sp.Integer(1))
    mean = sp.expand((1 - transmission) * dx_reflected + transmission * dx_transmitted)
    variance = sp.factor(
        (1 - transmission) * dx_reflected**2
        + transmission * dx_transmitted**2
        - mean**2
    )
    soft_memory_coefficient = sp.simplify(-16 * (delta - 1) ** 2 / s)

    exact_zero(dx_reflected, "XXZ reflected displacement")
    exact_zero(dx_transmitted + 2, "XXZ transmitted displacement")
    exact_zero(mean + 2 * transmission, "XXZ expectation -2T")
    exact_zero(variance - 4 * transmission * (1 - transmission), "XXZ variance")
    exact_zero(
        soft_memory_coefficient + 32 * (delta - 1) ** 2,
        "XXZ frozen soft-memory coefficient",
    )
    return dx_reflected, dx_transmitted, mean, variance


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--red",
        action="store_true",
        help="mutate q_T from +1 to -1; the general-law check must fail",
    )
    args = parser.parse_args()

    window_residue = check_window_calibration()
    reflected, transmitted, mean = check_general_arithmetic(args.red)
    su2_dx = check_su2_broken_to_u1()
    torus_dx, spectator_change = check_rank_two_abelian_factor()
    xxz_reflected, xxz_transmitted, xxz_mean, xxz_variance = check_xxz_instantiation()

    print("WINDOW D13 calibration residue=%s" % window_residue)
    print(
        "GENERAL reflected=%s transmitted=%s mean=%s"
        % (reflected, transmitted, mean)
    )
    print("SU2->U1 s=1/2 transmitted=%s" % su2_dx)
    print(
        "TORUS U1xU1 transmitted=%s spectator_delta=%s"
        % (torus_dx, spectator_change)
    )
    print(
        "XXZ reflected=%s transmitted=%s mean=%s variance=%s"
        % (xxz_reflected, xxz_transmitted, xxz_mean, xxz_variance)
    )
    print("PASS: M-quant-G symbolic charge arithmetic and frozen XXZ values")


if __name__ == "__main__":
    main()
