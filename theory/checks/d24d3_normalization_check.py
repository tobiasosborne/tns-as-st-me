#!/usr/bin/env python3
"""Certificate for the D24(d) clause-3 adjudication (bd tns-iu5, r2).

What is certified (matching theory/verdicts/d24d3-adjudication-r2.md):

* the DEFECT: the frozen clause (amputation constant a_leg = 1) is exactly
  density-blind and misses the PROVED/measured ``1/S`` law at every
  ``S != 1/2`` while hitting it at ``S = 1/2``;
* clause 2's residue is exactly ``Z_rho``-linear (no repair needed there);
* the CONDITIONAL matched value of claim D24-VAL: ``a_leg = 1/(2 rho)``,
  i.e. ``L(0,h) = -i chi/(2 rho v_h)``, reproduces the ansatz-free data at
  ``rho = S in {1/2, 1, 3/2, 2}``, and the exponent ``p`` in
  ``a_leg = (2 rho)^{-p}`` is pinned to 1 symbolically by the exact law
  ``(2S)^p = 2S`` at any single ``2S != 1``.

The definition D24(d)3b itself asserts NO value for ``a_leg`` (it is the
OPEN lemma AMP); the red modes below falsify the D24-VAL *candidate*, not
the definition.

Named computations
------------------
D24N-C1  symbolic: the frozen constant makes ML5-B(6) rho-free and v_h-free;
         the matched constant gives jet chi/rho.
D24N-C2  Z_rho = 2 rho from first-principles spin-S ladder matrices, and the
         soft-leg norm ||Q^-_k|Om>||^2 / N = 2 rho by ACTUAL CONSTRUCTION of
         Q^-_k|Om> = sum_x e^{ikx} S^-_x |Om> from the ladder matrix
         elements (r1-critic M3(c)(i): the r1 gate was the algebraic no-op
         ``sites*two_s/sites - two_s``; this one moves when the
         construction is mutated).
D24N-C3  the Ward residue is exactly linear in Z_rho:
         <h|Q_0^dag J^-_0|h> = Z_rho * 2iJ sin h = 2i v_S(h), computed on a
         ring from the raw two-site bond matrix.
D24N-C4  ground truth: the ansatz-free ring slopes of
         numerics/results/spin1-bc-falsifier.json equal 1/S within the
         PRE-REGISTERED 8% band (the ``decision_band`` key is REQUIRED to be
         present and equal to 0.08; deleting it fails — r1-critic M3(b)
         bonus hole closed).
D24N-C5  the frozen constant FAILS that band for S != 1/2 and passes at
         S = 1/2 (the defect).
D24N-C6  ACCEPTANCE (independent failure mode): the candidate constant must
         match the data within the r2 acceptance band 0.02.  This is NOT
         deductively implied by D24N-C4's 0.08 band (r1-critic M3(b)
         subsumption finding): a uniform -6% shift of every summary row
         passes C4 (max row dev 0.064 < 0.08) and dies HERE
         (dev ~0.06 > 0.02) — mutant m2b_shift60, exit path recorded in
         theory/verdicts/d24d3-adjudication-r2.md section 7.  Also:
         the exponent fitted from the non-degenerate spins (2S != 1) must
         be 1 within 0.03, and the SYMBOLIC exact law (2S)^p = 2S is solved
         with sympy at S in {1, 3/2, 2} (unique root p = 1), replacing the
         r1 ``lstsq(x, x)`` tautology (r1-critic M3(c)(ii)); the S = 1/2
         point is reported as degenerate (1^p = 1 for every p, r1-critic
         m4).  The resolving interval of p under the acceptance band is
         printed, so the certificate states what it actually pins.
D24N-C7  the (2 rho N)^{-1/2} half-power route is N-dependent and never
         equals (2 rho)^{-1} on the data's own N (refutes the S1-A critic's
         proposed mechanism; see r2 adjudication ⟨1⟩4.⟨2⟩2).

Exit paths
----------
Every failure raises ``SystemExit(1)`` through ``fail()``, whose message
BEGINS with the gate name (D24N-Cn) — the exit path is in the first token
of stderr.  No bare ``assert``; ``python3 -O`` cannot disable a check.

Red modes (each MUST exit 1; expected death gate in parentheses)
----------------------------------------------------------------
--red-frozen     a_leg = 1, the frozen density-blind flux      (D24N-C6)
--red-power      a_leg = 1/(2 rho)^2, wrong power              (D24N-C6)
--red-halfpower  a_leg = 1/(2 rho)^(1/2), the half-power       (D24N-C6)
--red-ward       claim the residue scales as Z_rho^2           (D24N-C3)
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

import numpy as np
import sympy as sp

DECISION_BAND = 0.08     # pre-registered in spin1-bc-falsifier.json (C4/C5)
ACCEPT_BAND = 0.02       # r2 acceptance band for the D24-VAL candidate (C6);
                         # tighter than DECISION_BAND on purpose: C6 must be
                         # able to fail on data that C4 accepts.
EXPONENT_FIT_BAND = 0.03
EXACT_TOL = 1.0e-12
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
    """S^-_site applied to a configuration-dictionary state.

    The matrix element sqrt((n+1)(2S-n)) is the first-principles ladder
    element <n+1|S^-|n> in the occupation (lowered-quanta) labelling.
    """
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
# D24N-C1 : the frozen constant is density blind; the matched one is not
# --------------------------------------------------------------------------
def check_frozen_is_density_blind() -> tuple[sp.Expr, sp.Expr]:
    momentum, velocity, density = sp.symbols("k v_h rho", positive=True)
    sign = sp.Symbol("chi")
    kinematic = sp.exp(sp.I * momentum) - 1
    residue = 2 * sp.I * velocity
    frozen = sp.series(kinematic * (-sp.I * sign / velocity) * residue,
                       momentum, 0, 2).removeO()
    matched = sp.series(kinematic * (-sp.I * sign / (2 * density * velocity)) * residue,
                        momentum, 0, 2).removeO()
    exact_zero(frozen - 2 * sp.I * sign * momentum, "D24N-C1 frozen jet != 2i chi k")
    exact_zero(sp.diff(frozen, density), "D24N-C1 frozen jet depends on rho")
    exact_zero(sp.diff(frozen, velocity), "D24N-C1 frozen jet depends on v_h")
    exact_zero(matched - sp.I * sign * momentum / density,
               "D24N-C1 matched jet != i chi k / rho")
    return sp.simplify(frozen / (sp.I * momentum)), sp.simplify(matched / (sp.I * momentum))


# --------------------------------------------------------------------------
# D24N-C2 : Z_rho = 2 rho, and the soft-leg norm by actual construction
# --------------------------------------------------------------------------
def check_order_parameter_residue() -> float:
    worst = 0.0
    # (i) the order-parameter residue from the ladder matrices
    for two_s in range(1, 7):
        _, raising, lowering = spin_matrices(two_s)
        dimension = two_s + 1
        vacuum = np.zeros(dimension)
        vacuum[0] = 1.0
        residue = float(vacuum @ (raising @ lowering - lowering @ raising) @ vacuum)
        worst = max(worst, abs(residue - two_s))
    # (ii) the soft-leg norm ||Q^-_k|Om>||^2 / N = 2S, k-independent, by
    # CONSTRUCTING Q^-_k|Om> = sum_x e^{ikx} S^-_x |Om> from apply_lowering.
    # (The r1 gate summed |e^{ikx}|^2 * two_s directly — an algebraic no-op
    # that accepted two_s = 3.7, -5.0, 1e6.  This one exercises the actual
    # ladder element sqrt((n+1)(2S-n)) and dies if it is mutated.)
    for two_s in (1, 2, 3, 4):
        for sites in (6, 9):
            vacuum_state = {tuple([0] * sites): 1.0}
            for momentum in (0.0, 0.7, 2.1):
                charged: dict = {}
                for x in range(sites):
                    phase = np.exp(1j * momentum * x)
                    lowered = apply_lowering(vacuum_state, x, two_s)
                    charged = combine(
                        charged, {c: phase * a for c, a in lowered.items()}
                    )
                norm_squared = inner(charged, charged).real
                worst = max(worst, abs(norm_squared / sites - two_s))
    require(worst < EXACT_TOL, f"D24N-C2 order-parameter/soft-leg-norm error {worst:.3e}")
    return worst


# --------------------------------------------------------------------------
# D24N-C3 : the Ward residue is exactly linear in Z_rho
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
# D24N-C4 -- C6 : ground truth, defect, conditional matched value
# --------------------------------------------------------------------------
def load_ring_slopes(data_path: Path) -> dict[float, list[float]]:
    require(data_path.is_file(), f"D24N-C4 missing ground-truth file {data_path}")
    payload = json.loads(data_path.read_text())
    require("A_ring_summary" in payload, "D24N-C4 no A_ring_summary in the data file")
    require("decision_band" in payload,
            "D24N-C4 decision_band key missing from the data file")
    band = float(payload["decision_band"])
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
    """ML5-B(6) jet with a_leg = 1/(2 rho)^p (None = frozen a_leg = 1)."""
    if exponent is None:
        return 2.0
    return 2.0 / (2.0 * spin) ** exponent


def check_defect(slopes: dict[float, list[float]]) -> tuple[float, list[float]]:
    """The frozen clause must MISS the C4 band off rho=1/2, HIT it at 1/2."""
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


def check_acceptance(slopes: dict[float, list[float]],
                     exponent: float | None) -> float:
    """D24N-C6 part 1: candidate vs data, ACCEPT_BAND (independent of C4)."""
    worst = 0.0
    offenders = []
    for spin in SPINS:
        measured = float(np.mean(slopes[spin]))
        deviation = abs(predicted_jet(spin, exponent) - measured) * spin
        if deviation > ACCEPT_BAND:
            offenders.append(f"S={spin} dev={deviation:.4f}")
        worst = max(worst, deviation)
    require(not offenders,
            "D24N-C6 candidate flux misses the acceptance band "
            f"({ACCEPT_BAND}) at " + "; ".join(offenders))
    return worst


def check_exponent(slopes: dict[float, list[float]]) -> tuple[float, list]:
    """D24N-C6 part 2: fitted exponent (non-degenerate spins) + symbolic pin."""
    # data fit over the spins with 2S != 1 (the S = 1/2 row has design entry
    # log(1) = 0 and contributes nothing — r1-critic m4; drop it openly)
    fit_spins = [s for s in SPINS if abs(2.0 * s - 1.0) > 1.0e-12]
    design = np.array([[np.log(2.0 * s)] for s in fit_spins])
    target = np.array([np.log(2.0 / float(np.mean(slopes[s]))) for s in fit_spins])
    exponent = float(np.linalg.lstsq(design, target, rcond=None)[0][0])
    require(abs(exponent - 1.0) < EXPONENT_FIT_BAND,
            f"D24N-C6 fitted exponent {exponent:.6f} is not 1 "
            f"(band {EXPONENT_FIT_BAND})")
    # symbolic pin: (2S)^p = 2S has the unique root p = 1 at each 2S != 1
    p = sp.Symbol("p", real=True)
    roots_per_spin = []
    for s in (1, sp.Rational(3, 2), 2):
        roots = sp.solve(sp.Eq((2 * s) ** p, 2 * s), p)
        require(roots == [1],
                f"D24N-C6 symbolic exact law (2S)^p = 2S at S={s} "
                f"gives roots {roots}, not [1]")
        roots_per_spin.append((s, roots))
    # S = 1/2 degeneracy, stated rather than hidden: 1^p - 1 == 0 identically
    degenerate = sp.simplify(sp.Integer(1) ** p - 1)
    require(degenerate == 0,
            f"D24N-C6 expected S=1/2 exact law to be degenerate, got {degenerate}")
    return exponent, roots_per_spin


def resolving_interval(slopes: dict[float, list[float]]) -> tuple[float, float]:
    """The p-interval the acceptance band actually pins (reported, not gated)."""
    passing = []
    for candidate in np.arange(0.80, 1.20001, 0.001):
        ok = all(
            abs(predicted_jet(s, float(candidate)) - float(np.mean(slopes[s]))) * s
            <= ACCEPT_BAND
            for s in SPINS
        )
        if ok:
            passing.append(float(candidate))
    require(bool(passing), "D24N-C6 resolving scan found no passing exponent")
    return min(passing), max(passing)


# --------------------------------------------------------------------------
# D24N-C7 : the S1-A critic's half-power route cannot produce the factor
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
    parser = argparse.ArgumentParser(description="D24(d)3 adjudication certificate (r2)")
    parser.add_argument("--data", type=Path, default=DEFAULT_DATA,
                        help="path to spin1-bc-falsifier.json (copies allowed)")
    parser.add_argument("--red-frozen", action="store_true",
                        help="a_leg = 1 (frozen); expected death: D24N-C6")
    parser.add_argument("--red-power", action="store_true",
                        help="a_leg = 1/(2 rho)^2; expected death: D24N-C6")
    parser.add_argument("--red-halfpower", action="store_true",
                        help="a_leg = 1/(2 rho)^(1/2); expected death: D24N-C6")
    parser.add_argument("--red-ward", action="store_true",
                        help="residue ~ Z_rho^2; expected death: D24N-C3")
    arguments = parser.parse_args()

    exponent: float | None = 1.0
    if arguments.red_frozen:
        exponent = None
    elif arguments.red_power:
        exponent = 2.0
    elif arguments.red_halfpower:
        exponent = 0.5

    frozen_jet, matched_jet = check_frozen_is_density_blind()
    residue_error = check_order_parameter_residue()
    ward_error = check_ward_residue_scaling(arguments.red_ward)
    slopes = load_ring_slopes(arguments.data)
    truth_error = check_ground_truth(slopes)
    defect_size, deviations = check_defect(slopes)
    accept_error = check_acceptance(slopes, exponent)
    fitted_exponent, _ = check_exponent(slopes)
    p_low, p_high = resolving_interval(slopes)
    half_power_gap = check_half_power_refuted(arguments.data)

    print(f"D24N-C1 frozen_jet_coefficient={frozen_jet} matched={matched_jet}")
    print(f"D24N-C2 Z_rho=2rho and constructed soft-leg norm, max_error={residue_error:.3e}")
    print(f"D24N-C3 Ward residue = Z_rho*2iJ sin h, max_error={ward_error:.3e}")
    print(f"D24N-C4 ansatz-free slopes vs 1/S: max_rel_dev={truth_error:.4f} "
          f"(pre-registered band {DECISION_BAND})")
    print("D24N-C5 frozen-clause relative deviations at S=1/2,1,3/2,2: "
          + ", ".join(f"{d:.3f}" for d in deviations)
          + f"  -> defect size {defect_size:.3f}")
    print(f"D24N-C6 candidate max_rel_dev={accept_error:.4f} "
          f"(acceptance band {ACCEPT_BAND}, independent of C4); "
          f"fitted exponent={fitted_exponent:.4f} over 2S!=1 spins; "
          f"symbolic (2S)^p=2S root p=1 at S=1,3/2,2 (S=1/2 degenerate); "
          f"resolving interval p in [{p_low:.3f}, {p_high:.3f}]")
    print(f"D24N-C7 half-power route gap={half_power_gap:.3e}")
    print("PASS: D24-VAL candidate a_leg = 1/(2 rho) matches; frozen a_leg = 1 refuted; "
          "the D24(d)3b definition itself fixes no value (lemma AMP open)")


if __name__ == "__main__":
    main()
