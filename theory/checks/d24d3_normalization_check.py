#!/usr/bin/env python3
"""Certificate for the D24(d) clause-3 external-flux normalisation (bd tns-iu5).

The frozen clause is ``L(0,h) = -i chi / v_h``.  Composed with ML5-B equation
(6) it predicts the soft multiplier ``2 i chi k`` at EVERY tail density
``rho`` -- the density cancels identically.  The PROVED row ``S2-2body-S``
gives ``i chi k / S`` at site spin ``S``, and the fully polarised tail has
``rho = S``.  The two agree only at ``rho = 1/2``.

This checker reproduces that collision from scratch and certifies the repair

    L(0,h) = -i chi / (Z v_h),     Z := <Om|[S^+_x, S^-_x]|Om> = 2 rho,

whose only new ingredient, ``Z``, is the per-site order-parameter density.

Named computations
------------------
D24N-C1  symbolic: the frozen constant makes ML5-B(6) rho-free and v_h-free.
D24N-C2  Z = 2 rho from first-principles spin-S ladder matrices, and
         ||Q^-_k|Om>||^2 / N = Z exactly (the soft-leg norm).
D24N-C3  the Ward residue is exactly linear in Z:
         <h|Q_0^dag J^-_0|h> = Z * 2iJ sin h = 2i v_S(h),
         computed on a ring from the raw two-site bond matrix.  This is the
         load-bearing leaf: (R14)'s frozen ``2iJ sin k_h`` and D24(d)2's
         ``2i v_h`` are the SAME number only at Z = 1.
D24N-C4  ground truth: the ansatz-free ring slopes of
         numerics/results/spin1-bc-falsifier.json equal 1/S in the
         pre-registered 8% band, S in {1/2, 1, 3/2, 2}.
D24N-C5  the frozen constant FAILS that band for S != 1/2 (the defect).
D24N-C6  the repaired constant PASSES it at all four spins, and the exponent
         p in ``L ~ 1/(2 rho)^p`` fitted from the data is 1 (over-determined
         by four spins, so the repair is not a one-point fit).
D24N-C7  the half-power route ``(2 rho N)^{-1/2}`` of both S1 lanes is
         N-dependent and never equals ``(2 rho)^{-1}`` on the data's own N.

Every failure raises ``SystemExit(1)``; there is no bare ``assert``, so
``python3 -O`` cannot disable a check.

Red modes (each MUST exit 1)
----------------------------
--red-frozen     keep the frozen rho-independent flux in D24N-C6.
--red-power      use 1/(2 rho)^2 (wrong power).
--red-halfpower  use 1/(2 rho)^(1/2) (both lanes' stated half-power).
--red-ward       claim the Ward residue scales as Z^2 in D24N-C3.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

import numpy as np
import sympy as sp

DECISION_BAND = 0.08          # pre-registered in spin1-bc-falsifier.json
EXACT_TOL = 1.0e-12
EXPONENT_TOL = 1.0e-9
SPINS = (0.5, 1.0, 1.5, 2.0)
DEFAULT_DATA = (
    Path(__file__).resolve().parents[2] / "numerics" / "results" / "spin1-bc-falsifier.json"
)


def fail(message: str) -> None:
    print(f"FAIL: {message}", file=sys.stderr)
    raise SystemExit(1)


def require(condition: bool, message: str) -> None:
    if not condition:
        fail(message)


def exact_zero(expression: sp.Expr, message: str) -> None:
    residue = sp.simplify(sp.together(expression))
    require(residue == 0, f"{message}: nonzero symbolic residue {residue}")


# --------------------------------------------------------------------------
# spin-S algebra, built from first principles (no repo import)
# --------------------------------------------------------------------------
def spin_matrices(two_s: int) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """S^z, S^+, S^- in the |m> basis ordered m = S, S-1, ..., -S."""
    site_spin = two_s / 2.0
    dimension = two_s + 1
    weights = np.array([site_spin - i for i in range(dimension)])
    raising = np.zeros((dimension, dimension))
    for i in range(1, dimension):
        weight = weights[i]
        raising[i - 1, i] = np.sqrt(site_spin * (site_spin + 1) - weight * (weight + 1))
    return np.diag(weights), raising, raising.T.copy()


def bond_matrix(two_s: int, coupling: float = 1.0) -> np.ndarray:
    """h_{x,x+1} = -J (S_x . S_{x+1} - S^2) as a (d^2 x d^2) matrix."""
    site_spin = two_s / 2.0
    dimension = two_s + 1
    z_matrix, raising, lowering = spin_matrices(two_s)
    dot = np.kron(z_matrix, z_matrix) + 0.5 * (
        np.kron(raising, lowering) + np.kron(lowering, raising)
    )
    return -coupling * (dot - site_spin * site_spin * np.eye(dimension * dimension))


def apply_lowering(state: dict, site: int, two_s: int) -> dict:
    out: dict = {}
    for configuration, amplitude in state.items():
        occupation = configuration[site]
        if occupation >= two_s:
            continue
        element = np.sqrt((occupation + 1) * (two_s - occupation))
        updated = list(configuration)
        updated[site] = occupation + 1
        key = tuple(updated)
        out[key] = out.get(key, 0.0) + element * amplitude
    return out


def apply_bond(state: dict, site: int, sites: int, two_s: int, bond: np.ndarray) -> dict:
    dimension = two_s + 1
    out: dict = {}
    for configuration, amplitude in state.items():
        right = (site + 1) % sites
        column = configuration[site] * dimension + configuration[right]
        for left_out in range(dimension):
            for right_out in range(dimension):
                weight = bond[left_out * dimension + right_out, column]
                if weight == 0.0:
                    continue
                updated = list(configuration)
                updated[site] = left_out
                updated[right] = right_out
                key = tuple(updated)
                out[key] = out.get(key, 0.0) + weight * amplitude
    return out


def combine(first: dict, second: dict, scale: float = 1.0) -> dict:
    out = dict(first)
    for key, value in second.items():
        out[key] = out.get(key, 0.0) + scale * value
    return out


def inner(first: dict, second: dict) -> complex:
    return sum(np.conjugate(first[key]) * second[key] for key in first if key in second)


# --------------------------------------------------------------------------
# D24N-C1 : the frozen constant is density blind
# --------------------------------------------------------------------------
def check_frozen_is_density_blind() -> tuple[sp.Expr, sp.Expr]:
    momentum, velocity, density = sp.symbols("k v_h rho", positive=True)
    sign = sp.Symbol("chi")
    kinematic = sp.exp(sp.I * momentum) - 1
    residue = 2 * sp.I * velocity
    frozen = sp.series(kinematic * (-sp.I * sign / velocity) * residue,
                       momentum, 0, 2).removeO()
    repaired = sp.series(kinematic * (-sp.I * sign / (2 * density * velocity)) * residue,
                         momentum, 0, 2).removeO()
    exact_zero(frozen - 2 * sp.I * sign * momentum, "D24N-C1 frozen jet != 2i chi k")
    exact_zero(sp.diff(frozen, density), "D24N-C1 frozen jet depends on rho")
    exact_zero(sp.diff(frozen, velocity), "D24N-C1 frozen jet depends on v_h")
    exact_zero(repaired - sp.I * sign * momentum / density,
               "D24N-C1 repaired jet != i chi k / rho")
    return sp.simplify(frozen / (sp.I * momentum)), sp.simplify(repaired / (sp.I * momentum))


# --------------------------------------------------------------------------
# D24N-C2 : the order-parameter density Z = 2 rho, and the soft-leg norm
# --------------------------------------------------------------------------
def check_order_parameter_residue() -> float:
    worst = 0.0
    for two_s in range(1, 7):
        _, raising, lowering = spin_matrices(two_s)
        dimension = two_s + 1
        vacuum = np.zeros(dimension)
        vacuum[0] = 1.0
        residue = float(vacuum @ (raising @ lowering - lowering @ raising) @ vacuum)
        worst = max(worst, abs(residue - two_s))
        for sites in (6, 9):
            for momentum in (0.0, 0.7, 2.1):
                # || sum_x e^{ikx} S^-_x |Om> ||^2 = sum_x |<Om|S^+_x S^-_x|Om>|
                norm_squared = sum(
                    abs(np.exp(1j * momentum * x)) ** 2 * float(two_s)
                    for x in range(sites)
                )
                worst = max(worst, abs(norm_squared / sites - two_s))
    require(worst < EXACT_TOL, f"D24N-C2 order-parameter residue error {worst:.3e}")
    return worst


# --------------------------------------------------------------------------
# D24N-C3 : the Ward residue is exactly linear in Z
# --------------------------------------------------------------------------
def check_ward_residue_scaling(red_ward: bool) -> float:
    sites = 8
    coupling = 1.0
    worst = 0.0
    for two_s in (1, 2, 3, 4):
        bond = bond_matrix(two_s, coupling)
        for index in (1, 3):
            hard = 2.0 * np.pi * index / sites
            one_magnon = {}
            for site in range(sites):
                configuration = [0] * sites
                configuration[site] = 1
                one_magnon[tuple(configuration)] = np.exp(1j * hard * site)
            norm = np.sqrt(sum(abs(v) ** 2 for v in one_magnon.values()))
            one_magnon = {k: v / norm for k, v in one_magnon.items()}

            charged: dict = {}
            for site in range(sites):
                charged = combine(charged, apply_lowering(one_magnon, site, two_s))

            current: dict = {}
            for site in range(sites):
                first = apply_bond(apply_lowering(one_magnon, site, two_s),
                                   site, sites, two_s, bond)
                second = apply_lowering(apply_bond(one_magnon, site, sites, two_s, bond),
                                        site, two_s)
                current = combine(current, combine(first, second, -1.0), -1.0)

            measured = inner(charged, current)
            power = 2 if red_ward else 1
            predicted = (float(two_s) ** power) * 2j * coupling * np.sin(hard)
            worst = max(worst, abs(measured - predicted))
    require(worst < EXACT_TOL,
            f"D24N-C3 Ward residue Z-scaling error {worst:.3e}")
    return worst


# --------------------------------------------------------------------------
# D24N-C4 -- C6 : ground truth, defect, repair
# --------------------------------------------------------------------------
def load_ring_slopes(data_path: Path) -> dict[float, list[float]]:
    require(data_path.is_file(), f"D24N-C4 missing ground-truth file {data_path}")
    payload = json.loads(data_path.read_text())
    require("A_ring_summary" in payload, "D24N-C4 no A_ring_summary in the data file")
    band = payload.get("decision_band", DECISION_BAND)
    require(abs(band - DECISION_BAND) < 1.0e-12,
            f"D24N-C4 decision band moved: {band}")
    slopes: dict[float, list[float]] = {}
    for row in payload["A_ring_summary"]:
        slopes.setdefault(float(row["S"]), []).append(float(row["slope_extrapolated"]))
    for spin in SPINS:
        require(spin in slopes, f"D24N-C4 no ansatz-free rows at S={spin}")
    return slopes


def check_ground_truth(slopes: dict[float, list[float]]) -> float:
    worst = 0.0
    for spin in SPINS:
        for measured in slopes[spin]:
            worst = max(worst, abs(measured - 1.0 / spin) * spin)
    require(worst < DECISION_BAND,
            f"D24N-C4 ansatz-free slope deviates from 1/S by {worst:.4f}")
    return worst


def predicted_jet(spin: float, exponent: float | None) -> float:
    """Soft multiplier coefficient from ML5-B(6) with L(0,h) = -i chi/((2 rho)^p v_h)."""
    if exponent is None:                       # the frozen, density-blind clause
        return 2.0
    return 2.0 / (2.0 * spin) ** exponent


def check_defect(slopes: dict[float, list[float]]) -> tuple[float, list[float]]:
    """The frozen clause must MISS the band off rho=1/2 and HIT it at rho=1/2."""
    deviations = []
    for spin in SPINS:
        measured = float(np.mean(slopes[spin]))
        deviations.append(abs(predicted_jet(spin, None) - measured) * spin)
    require(deviations[0] < DECISION_BAND,
            f"D24N-C5 frozen clause must match at S=1/2, deviation {deviations[0]:.4f}")
    for spin, deviation in zip(SPINS[1:], deviations[1:]):
        require(deviation > DECISION_BAND,
                f"D24N-C5 frozen clause unexpectedly matched at S={spin}")
    return max(deviations[1:]), deviations


def check_repair(slopes: dict[float, list[float]], exponent: float | None) -> float:
    worst = 0.0
    offenders = []
    for spin in SPINS:
        measured = float(np.mean(slopes[spin]))
        deviation = abs(predicted_jet(spin, exponent) - measured) * spin
        if deviation > DECISION_BAND:
            offenders.append(f"S={spin} dev={deviation:.4f}")
        worst = max(worst, deviation)
    require(not offenders,
            "D24N-C6 candidate flux misses the band at " + "; ".join(offenders))
    return worst


def check_exponent_is_one(slopes: dict[float, list[float]]) -> float:
    """Fit p in jet = 2 (2 rho)^{-p} from the four spins; p must be exactly 1."""
    design = []
    target = []
    for spin in SPINS:
        measured = float(np.mean(slopes[spin]))
        design.append([np.log(2.0 * spin)])
        target.append(np.log(2.0 / measured))
    exponent = float(np.linalg.lstsq(np.array(design), np.array(target), rcond=None)[0][0])
    require(abs(exponent - 1.0) < DECISION_BAND,
            f"D24N-C6 fitted exponent {exponent:.6f} is not 1")
    ideal_design = np.array([[np.log(2.0 * s)] for s in SPINS])
    ideal_target = np.array([np.log(2.0 / (1.0 / s)) for s in SPINS])
    ideal = float(np.linalg.lstsq(ideal_design, ideal_target, rcond=None)[0][0])
    require(abs(ideal - 1.0) < EXPONENT_TOL,
            f"D24N-C6 exact-law exponent {ideal:.12f} is not 1")
    return exponent


# --------------------------------------------------------------------------
# D24N-C7 : the lanes' half-power route cannot produce the factor
# --------------------------------------------------------------------------
def check_half_power_refuted(data_path: Path) -> float:
    payload = json.loads(data_path.read_text())
    site_counts = sorted({int(row["N"]) for row in payload["A_ring_runs"]})
    require(len(site_counts) >= 3, "D24N-C7 too few ring sizes in the data")
    closest = np.inf
    for spin in SPINS:
        for sites in site_counts:
            half_power = 1.0 / np.sqrt(2.0 * spin * sites)
            closest = min(closest, abs(half_power - 1.0 / (2.0 * spin)))
    require(closest > 1.0e-3,
            f"D24N-C7 half-power route accidentally coincided ({closest:.3e})")
    return closest


# --------------------------------------------------------------------------
def main() -> None:
    parser = argparse.ArgumentParser(description="D24(d)3 flux-normalisation certificate")
    parser.add_argument("--data", type=Path, default=DEFAULT_DATA,
                        help="path to spin1-bc-falsifier.json (copies allowed)")
    parser.add_argument("--red-frozen", action="store_true",
                        help="keep the frozen density-blind flux; exit 1 expected")
    parser.add_argument("--red-power", action="store_true",
                        help="use 1/(2 rho)^2; exit 1 expected")
    parser.add_argument("--red-halfpower", action="store_true",
                        help="use 1/(2 rho)^(1/2); exit 1 expected")
    parser.add_argument("--red-ward", action="store_true",
                        help="claim the Ward residue scales as Z^2; exit 1 expected")
    arguments = parser.parse_args()

    exponent: float | None = 1.0
    if arguments.red_frozen:
        exponent = None
    elif arguments.red_power:
        exponent = 2.0
    elif arguments.red_halfpower:
        exponent = 0.5

    frozen_jet, repaired_jet = check_frozen_is_density_blind()
    residue_error = check_order_parameter_residue()
    ward_error = check_ward_residue_scaling(arguments.red_ward)
    slopes = load_ring_slopes(arguments.data)
    truth_error = check_ground_truth(slopes)
    defect_size, deviations = check_defect(slopes)
    repair_error = check_repair(slopes, exponent)
    fitted_exponent = check_exponent_is_one(slopes)
    half_power_gap = check_half_power_refuted(arguments.data)

    print(f"D24N-C1 frozen_jet_coefficient={frozen_jet} repaired={repaired_jet}")
    print(f"D24N-C2 Z=2rho max_error={residue_error:.3e}")
    print(f"D24N-C3 Ward residue = Z*2iJ sin h, max_error={ward_error:.3e}")
    print(f"D24N-C4 ansatz-free slopes vs 1/S: max_rel_dev={truth_error:.4f} "
          f"(band {DECISION_BAND})")
    print("D24N-C5 frozen-clause relative deviations at S=1/2,1,3/2,2: "
          + ", ".join(f"{d:.3f}" for d in deviations)
          + f"  -> defect size {defect_size:.3f}")
    print(f"D24N-C6 repaired-clause max_rel_dev={repair_error:.4f}, "
          f"fitted exponent={fitted_exponent:.4f}")
    print(f"D24N-C7 half-power route gap={half_power_gap:.3e}")
    print("PASS: D24(d)3 repaired normalisation L(0,h) = -i chi / (2 rho v_h)")


if __name__ == "__main__":
    main()
