#!/usr/bin/env python3
"""Certificate for the D24(d) clause-3 adjudication (bd tns-iu5, r3).

Full gate audit, red-mode table and mutation record: section 7 of
theory/verdicts/d24d3-adjudication-r3.md.  Summary:

D24N-C1  GUARD (symbolic, no runtime red mode): the frozen constant makes
         ML5-B(6) rho-free and v_h-free; the matched one gives jet chi/rho.
D24N-C2  the spin-S ladder four independent ways -- order-parameter residue;
         the occupation-basis element of ``ladder_element`` against the dense
         |m>-basis matrix of ``spin_matrices`` at EVERY n <= 2S-1; multi-
         quantum norms ||(S^-_x)^n|Om>||^2; and the soft-leg norm by actual
         construction plus CROSS-MOMENTUM ORTHOGONALITY.  r2 probed only the
         n = 0 element and its momentum loop was decorative (r2-critic
         m4(i)-(ii)); both holes are closed here, with red mode
         ``--red-ladder``.
D24N-C3  the Ward residue is exactly Z_rho-linear, <h|Q_0^dag J^-_0|h> =
         2i v_S(h).  Red mode ``--red-ward``.
D24N-C4  ground truth: the ansatz-free ring slopes equal 1/S inside the
         PRE-REGISTERED 0.08 band; ``decision_band`` is a required key.  No
         code red mode by design -- C4 is exercised by DATA mutation.
D24N-C5  DISPLAY (deductively subsumed by C4): the frozen deviations.
D24N-C6  ACCEPTANCE.  The band is NOT a constant here: it is DERIVED at
         runtime as max_rows |error| * S from the data's own quoted
         extrapolation error (0.0479 on the shipped data).  r2's 0.02 was
         post-registered and TIGHTER than that error, so it rejected data
         drawn inside its own error bars (r2-critic M3(b)(iii)); this cannot.
         Plus the fitted exponent and the SYMBOLIC pin (2S)^p = 2S.  The
         S = 1/2 degeneracy is PRINTED, never gated (r2-critic m4(iii)).
         Red modes ``--red-frozen``, ``--red-power``, ``--red-halfpower``.
D24N-C7  DISPLAY, unfalsifiable on this data's N in [60,480] (r2-critic m5).
D24N-C8  the r3 amputation convention's leg-conversion constant:
         Q^-_k|Om> = sqrt(Z_rho)|k>, with |k> verified to be an EIGENVECTOR
         of the one-magnon block of H_S (residual, not expectation value).
         Hence leg conversion alone predicts a_leg = Z_rho^(-1/2), which
         ``--red-halfpower`` falsifies at the PRE-REGISTERED band.  Red mode
         ``--red-legfactor``.

The definition D24(d)3b asserts NO value for ``a_leg`` (open lemma AMP); the
red modes falsify *candidates*, never the definition.  Every failure raises
SystemExit(1) through ``fail()``, whose message BEGINS with the gate name,
so the exit PATH is the first token of stderr; no bare ``assert``.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

import numpy as np
import sympy as sp

DECISION_BAND = 0.08     # pre-registered in spin1-bc-falsifier.json (C4/C5)
EXPONENT_FIT_BAND = 0.03
EXACT_TOL = 1.0e-12
SPINS = (0.5, 1.0, 1.5, 2.0)
LEGACY_R2_BAND = 0.02    # reported for continuity only; gates nothing
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


def ladder_element(occupation: int, two_s: int, red_ladder: bool = False) -> float:
    """<n+1|S^-|n> in the occupation (lowered-quanta) labelling.

    The honest formula is sqrt((n+1)(2S-n)).  --red-ladder scales every
    n >= 1 element (exact at n = 0), which is precisely the mutant that
    slipped past the r2 gate (r2-critic m4(i), mutant cA_deepladder).
    """
    element = np.sqrt((occupation + 1) * (two_s - occupation))
    if red_ladder and occupation >= 1:
        element *= 3.7
    return float(element)


def apply_lowering(state: dict, site: int, two_s: int, red_ladder: bool = False) -> dict:
    out: dict = {}
    for configuration, amplitude in state.items():
        occupation = configuration[site]
        if occupation >= two_s:
            continue
        element = ladder_element(occupation, two_s, red_ladder)
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
# D24N-C2 : the ladder, four independent ways
# --------------------------------------------------------------------------
def check_order_parameter_residue(red_ladder: bool) -> float:
    worst = 0.0
    # (i) order-parameter residue <Om|[S^+,S^-]|Om> = 2S from the dense matrices
    for two_s in range(1, 7):
        _, raising, lowering = spin_matrices(two_s)
        dimension = two_s + 1
        vacuum = np.zeros(dimension)
        vacuum[0] = 1.0
        residue = float(vacuum @ (raising @ lowering - lowering @ raising) @ vacuum)
        worst = max(worst, abs(residue - two_s))
    # (ii) two independently coded ladder formulas must agree at EVERY n
    for two_s in range(1, 7):
        _, _, lowering = spin_matrices(two_s)
        for occupation in range(two_s):
            dense = float(lowering[occupation + 1, occupation])
            occupied = ladder_element(occupation, two_s, red_ladder)
            worst = max(worst, abs(dense - occupied))
    # (iii) multi-quantum norms: ||(S^-_x)^n|Om>||^2 = prod_{j<n} (j+1)(2S-j)
    for two_s in (1, 2, 3, 4):
        for sites in (4,):
            state = {tuple([0] * sites): 1.0}
            expected = 1.0
            for quantum in range(two_s):
                state = apply_lowering(state, 0, two_s, red_ladder)
                expected *= (quantum + 1) * (two_s - quantum)
                worst = max(worst, abs(inner(state, state).real - expected))
    # (iv) soft-leg norm by construction + cross-momentum orthogonality
    for two_s in (1, 2, 3, 4):
        for sites in (6, 9):
            vacuum_state = {tuple([0] * sites): 1.0}
            momenta = [2.0 * np.pi * j / sites for j in (0, 1, 2)]
            require(len(momenta) >= 3,
                    "D24N-C2 fewer than three commensurate momenta: the "
                    "orthogonality gate would be vacuous")
            charged_states = []
            for momentum in momenta:
                charged: dict = {}
                for x in range(sites):
                    phase = np.exp(1j * momentum * x)
                    lowered = apply_lowering(vacuum_state, x, two_s, red_ladder)
                    charged = combine(charged,
                                      {c: phase * a for c, a in lowered.items()})
                charged_states.append(charged)
                norm_squared = inner(charged, charged).real
                worst = max(worst, abs(norm_squared / sites - two_s))
            for i in range(len(momenta)):
                for j in range(i + 1, len(momenta)):
                    overlap = inner(charged_states[i], charged_states[j])
                    worst = max(worst, abs(overlap) / sites)
    require(worst < EXACT_TOL, f"D24N-C2 ladder/soft-leg-norm error {worst:.3e}")
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
def load_payload(data_path: Path) -> dict:
    require(data_path.is_file(), f"D24N-C4 missing ground-truth file {data_path}")
    payload = json.loads(data_path.read_text())
    require("A_ring_summary" in payload, "D24N-C4 no A_ring_summary in the data file")
    require("decision_band" in payload,
            "D24N-C4 decision_band key missing from the data file")
    band = float(payload["decision_band"])
    require(abs(band - DECISION_BAND) < 1.0e-12,
            f"D24N-C4 decision band moved: {band}")
    return payload


def load_ring_slopes(payload: dict) -> dict[float, list[float]]:
    slopes: dict[float, list[float]] = {}
    for row in payload["A_ring_summary"]:
        slopes.setdefault(float(row["S"]), []).append(float(row["slope_extrapolated"]))
    for spin in SPINS:
        require(spin in slopes, f"D24N-C4 no ansatz-free rows at S={spin}")
    return slopes


def derive_accept_band(payload: dict) -> float:
    """C6's band, taken from the DATA's own quoted extrapolation error.

    r2-critic M3(b)(iii): a hand-chosen 0.02 was 1.2-2.4x tighter than the
    data's own ``error`` column at every spin, so it rejected perturbations
    inside the error bars.  This band is that column, in the checker's
    ``dev * S`` units -- no constant to tune.
    """
    worst = 0.0
    for row in payload["A_ring_summary"]:
        spin = float(row["S"])
        require("error" in row, "D24N-C6 data row has no quoted error column")
        worst = max(worst, abs(float(row["error"])) * spin)
    require(worst > 0.0, "D24N-C6 derived acceptance band is zero")
    require(worst < DECISION_BAND,
            f"D24N-C6 derived band {worst:.4f} is not tighter than the "
            f"pre-registered {DECISION_BAND}: C6 would be subsumed by C4")
    return worst


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
    """D24N-C5, DISPLAY: the frozen clause misses off rho=1/2, hits at 1/2."""
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
                     exponent: float | None, band: float) -> float:
    """D24N-C6 part 1: candidate vs data, at the data-derived band."""
    worst = 0.0
    offenders = []
    for spin in SPINS:
        measured = float(np.mean(slopes[spin]))
        deviation = abs(predicted_jet(spin, exponent) - measured) * spin
        if deviation > band:
            offenders.append(f"S={spin} dev={deviation:.4f}")
        worst = max(worst, deviation)
    require(not offenders,
            "D24N-C6 candidate flux misses the data-derived acceptance band "
            f"({band:.4f}) at " + "; ".join(offenders))
    return worst


def check_exponent(slopes: dict[float, list[float]]) -> tuple[float, str]:
    """D24N-C6 part 2: fitted exponent (non-degenerate spins) + symbolic pin."""
    fit_spins = [s for s in SPINS if abs(2.0 * s - 1.0) > 1.0e-12]
    design = np.array([[np.log(2.0 * s)] for s in fit_spins])
    target = np.array([np.log(2.0 / float(np.mean(slopes[s]))) for s in fit_spins])
    exponent = float(np.linalg.lstsq(design, target, rcond=None)[0][0])
    require(abs(exponent - 1.0) < EXPONENT_FIT_BAND,
            f"D24N-C6 fitted exponent {exponent:.6f} is not 1 "
            f"(band {EXPONENT_FIT_BAND})")
    p = sp.Symbol("p", real=True)
    for s in (1, sp.Rational(3, 2), 2):
        roots = sp.solve(sp.Eq((2 * s) ** p, 2 * s), p)
        require(roots == [1],
                f"D24N-C6 symbolic exact law (2S)^p = 2S at S={s} "
                f"gives roots {roots}, not [1]")
    # S = 1/2 degeneracy: REPORTED, never gated.  ``1**p - 1`` simplifies to 0
    # for every p, so a require() on it is a check that cannot fail
    # (r2-critic m4(iii)).
    note = f"S=1/2 degenerate: 1**p - 1 = {sp.simplify(sp.Integer(1) ** p - 1)}"
    return exponent, note


def resolving_interval(slopes: dict[float, list[float]],
                       band: float) -> tuple[float, float] | None:
    """The p-interval a given band admits (reported, not gated)."""
    passing = []
    for candidate in np.arange(0.80, 1.20001, 0.001):
        ok = all(
            abs(predicted_jet(s, float(candidate)) - float(np.mean(slopes[s]))) * s
            <= band
            for s in SPINS
        )
        if ok:
            passing.append(float(candidate))
    return (min(passing), max(passing)) if passing else None


# --------------------------------------------------------------------------
# D24N-C7 : DISPLAY -- the N-dependent half-power route
# --------------------------------------------------------------------------
def check_half_power_route(payload: dict) -> float:
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
# D24N-C8 : the r3 convention's leg-conversion constant
# --------------------------------------------------------------------------
def check_leg_conversion(red_legfactor: bool) -> tuple[float, float]:
    """<k|Q^-_k|Om> = sqrt(Z_rho * N), with |k> the true one-magnon state.

    |k> is not assumed: the one-magnon block of H_S is built from the raw
    bond matrix and the plane wave is verified to be an EIGENVECTOR with
    eigenvalue omega_S(k) = 2JS(1 - cos k) (residual norm, not expectation).
    """
    sites = 8
    coupling = 1.0
    worst_spectral = 0.0
    worst_overlap = 0.0
    for two_s in (1, 2, 3, 4):
        site_spin = two_s / 2.0
        bond = bond_matrix(two_s, coupling)
        basis = []
        for x in range(sites):
            configuration = [0] * sites
            configuration[x] = 1
            basis.append(tuple(configuration))
        index = {b: i for i, b in enumerate(basis)}
        hamiltonian = np.zeros((sites, sites))
        for column, configuration in enumerate(basis):
            image: dict = {}
            for site in range(sites):
                image = combine(image,
                                apply_bond({configuration: 1.0}, site, sites, two_s, bond))
            for key, value in image.items():
                if key in index:
                    hamiltonian[index[key], column] += float(np.real(value))
        vacuum_state = {tuple([0] * sites): 1.0}
        for j in (1, 2, 3):
            momentum = 2.0 * np.pi * j / sites
            wave = np.array([np.exp(1j * momentum * x) for x in range(sites)])
            wave /= np.sqrt(sites)
            energy = 2.0 * coupling * site_spin * (1.0 - np.cos(momentum))
            residual = hamiltonian @ wave - energy * wave
            worst_spectral = max(worst_spectral, float(np.linalg.norm(residual)))
            charged: dict = {}
            for x in range(sites):
                phase = np.exp(1j * momentum * x)
                lowered = apply_lowering(vacuum_state, x, two_s)
                charged = combine(charged, {c: phase * a for c, a in lowered.items()})
            vector = np.array([charged.get(b, 0.0) for b in basis])
            overlap = abs(np.vdot(wave, vector))
            power = 1.0 if red_legfactor else 0.5
            predicted = (float(two_s) ** power) * np.sqrt(sites)
            worst_overlap = max(worst_overlap, abs(overlap - predicted))
    require(worst_spectral < 1.0e-10,
            f"D24N-C8 plane wave is not an H_S one-magnon eigenvector "
            f"(residual {worst_spectral:.3e})")
    require(worst_overlap < 1.0e-10,
            f"D24N-C8 leg-conversion factor is not sqrt(Z_rho) "
            f"(error {worst_overlap:.3e})")
    return worst_spectral, worst_overlap


# --------------------------------------------------------------------------
def main() -> None:
    parser = argparse.ArgumentParser(description="D24(d)3 adjudication certificate (r3)")
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
    parser.add_argument("--red-ladder", action="store_true",
                        help="ladder element wrong at n >= 1; death: D24N-C2")
    parser.add_argument("--red-legfactor", action="store_true",
                        help="leg conversion = Z_rho not sqrt(Z_rho); death: D24N-C8")
    arguments = parser.parse_args()

    exponent: float | None = 1.0
    if arguments.red_frozen:
        exponent = None
    elif arguments.red_power:
        exponent = 2.0
    elif arguments.red_halfpower:
        exponent = 0.5

    frozen_jet, matched_jet = check_frozen_is_density_blind()
    ladder_error = check_order_parameter_residue(arguments.red_ladder)
    ward_error = check_ward_residue_scaling(arguments.red_ward)
    payload = load_payload(arguments.data)
    slopes = load_ring_slopes(payload)
    accept_band = derive_accept_band(payload)
    truth_error = check_ground_truth(slopes)
    defect_size, deviations = check_defect(slopes)
    accept_error = check_acceptance(slopes, exponent, accept_band)
    fitted_exponent, degeneracy_note = check_exponent(slopes)
    derived_interval = resolving_interval(slopes, accept_band)
    frozen_interval = resolving_interval(slopes, DECISION_BAND)
    legacy_interval = resolving_interval(slopes, LEGACY_R2_BAND)
    half_power_gap = check_half_power_route(payload)
    spectral_error, overlap_error = check_leg_conversion(arguments.red_legfactor)

    def show(interval: tuple[float, float] | None) -> str:
        return "empty" if interval is None else f"[{interval[0]:.3f}, {interval[1]:.3f}]"

    print(f"D24N-C1 GUARD frozen_jet_coefficient={frozen_jet} matched={matched_jet}")
    print(f"D24N-C2 ladder x4 (residue, dense/occupation cross-check, multi-quantum "
          f"norms, soft-leg norm + cross-momentum orthogonality), max_error="
          f"{ladder_error:.3e}")
    print(f"D24N-C3 Ward residue = Z_rho*2iJ sin h, max_error={ward_error:.3e}")
    print(f"D24N-C4 ansatz-free slopes vs 1/S: max_rel_dev={truth_error:.4f} "
          f"(pre-registered band {DECISION_BAND})")
    print("D24N-C5 DISPLAY frozen-clause relative deviations at S=1/2,1,3/2,2: "
          + ", ".join(f"{d:.3f}" for d in deviations)
          + f"  -> defect size {defect_size:.3f}")
    print(f"D24N-C6 candidate max_rel_dev={accept_error:.4f} vs acceptance band "
          f"{accept_band:.4f} DERIVED from the data's own quoted error "
          f"(< pre-registered {DECISION_BAND}, so C6 is not subsumed by C4); "
          f"fitted exponent={fitted_exponent:.4f} over 2S!=1 spins; symbolic "
          f"(2S)^p=2S root p=1 at S=1,3/2,2; {degeneracy_note}")
    print(f"D24N-C6 resolving intervals for p: at the derived band "
          f"{show(derived_interval)}; at the pre-registered band "
          f"{show(frozen_interval)}; at r2's retired 0.02 band "
          f"{show(legacy_interval)} (reported, gates nothing)")
    print(f"D24N-C7 DISPLAY N-dependent half-power route gap={half_power_gap:.3e}")
    print(f"D24N-C8 Q^-_k|Om> = sqrt(Z_rho)|k>: eigenvector residual="
          f"{spectral_error:.3e}, overlap error={overlap_error:.3e}; so leg "
          f"conversion alone gives a_leg = Z_rho^(-1/2), refuted by "
          f"--red-halfpower at the PRE-REGISTERED band")
    print("PASS: D24-VAL candidate a_leg = 1/(2 rho) matches; frozen a_leg = 1 and "
          "leg-conversion a_leg = Z_rho^(-1/2) both refuted; the D24(d)3b "
          "definition itself fixes no value (lemma AMP open)")


if __name__ == "__main__":
    main()
