#!/usr/bin/env python3
"""Certificate for the D24(d) clause-3 adjudication (bd tns-iu5, r5).

Full gate audit, red-mode table and mutation record: section 6 of
theory/verdicts/d24d3-adjudication-r5.md (r4: section 6 of
theory/verdicts/d24d3-adjudication-r4.md; r3 architecture: section 7 of
theory/verdicts/d24d3-adjudication-r3.md).  Summary:

D24N-C1  GUARD (symbolic, no runtime red mode): the frozen constant makes
         ML5-B(6) rho-free and v_h-free; the matched one gives jet chi/rho.
D24N-C2  the spin-S ladder four independent ways -- order-parameter residue;
         the occupation-basis element of ``ladder_element`` against the dense
         |m>-basis matrix of ``spin_matrices`` at EVERY n <= 2S-1; multi-
         quantum norms ||(S^-_x)^n|Om>||^2; the soft-leg norm by actual
         construction; and (NEW in r4, replacing the r3 cross-momentum
         orthogonality sub-gate, which was 0 == 0 for every input --
         r3-critic M3) the TWO-MAGNON SAME-total-momentum overlap
         <(Q^-_{k})^2 Om | (Q^-_{k+pi})^2 Om> = -2N*Z_rho, exact, against a
         closed form derived independently of the code, sensitive to the
         n >= 1 ladder elements.  Its ISOLATED error is reported on the
         C2 banner line beside the aggregate max (r4-critic m5), because
         the aggregate is set by sub-gate (iii) under ``--red-ladder``
         and so no red mode names (v) in its exit path.  What (v) adds
         over (ii) is COMPOSITION-path coverage (apply_charge o
         apply_charge, inner, the coincidence bookkeeping), NOT ladder
         coverage: (ii) already pins every ladder element exactly.  It is
         insensitive at 2S = 1, where the coincidence term carries
         2S - 1 = 0.  Red mode ``--red-ladder``.
D24N-C3  the Ward residue is exactly Z_rho-linear against the CHARGE-CREATED
         soft leg, <h|Q_0^dag J^-_0|h> = 2i v_S(h).  Red mode ``--red-ward``.
         A DISPLAY line prints the same residue in BOTH normalisations.
         (b)'s leg is the delta-normalised ASYMPTOTIC magnon, so the
         conversion is exactly sqrt(Z_rho) only in the LSZ limit: the line
         prints the LSZ-limit value C3/sqrt(Z_rho) AND the finite-N value
         C3/sqrt(Z_rho - 2/N) obtained by dividing by the MEASURED
         descendant-leg ratio ||Q^-_0|h>||/sqrt(N) (r4-critic M1: r4
         printed the first labelled as the second, 3.28% out at 2S=4,
         N=8).  Both are DISPLAY, never gated -- as gates they would be
         deductively subsumed by C3 and C8.
D24N-C4  ground truth: the ansatz-free ring slopes equal 1/S inside the
         PRE-REGISTERED 0.08 band; ``decision_band`` is a required key.  No
         code red mode by design -- C4 is exercised by DATA mutation.
D24N-C5  DISPLAY (deductively subsumed by C4): the frozen deviations.
D24N-C6  ACCEPTANCE (part 1) at the band DERIVED at runtime as
         max_rows |error| * S from the data's own quoted extrapolation
         error (0.0479 on the shipped data), plus the SYMBOLIC pin
         (2S)^p = 2S (part 2, gated).  The r3 fitted-exponent gate is
         REWORKED (r3-critic M2): r3 shipped a hand-chosen,
         post-registered EXPONENT_FIT_BAND = 0.03, TIGHTER than the
         derived band, while four document layers said "no acceptance
         constant in the file" -- that claim was false and is retracted.
         r4 derives the exponent band from the same error column,
         band_p = [sum log(2S) / sum log^2(2S)] * log(1/(1-band)) =
         0.0432 on the shipped data -- and the derivation PROVES the
         fitted-exponent comparison is deductively subsumed by part 1 at
         calibrated bands, so it is demoted to DISPLAY (the C5/X11
         treatment), never gated.  A uniform shift inside the data's
         quoted error now passes (m_shift34, m_shift40 pass; r3 rejected
         both).  The S = 1/2 degeneracy is PRINTED, never gated.  Red
         modes ``--red-frozen``, ``--red-power``, ``--red-halfpower``.
D24N-C7  DISPLAY, unfalsifiable on this data's N in [60,480] (r2-critic m5).
D24N-C8  the leg-conversion constant, now on BOTH legs (r3-critic m1: r3
         tested only the vacuum case): (i) vacuum -- Q^-_k|Om> =
         sqrt(Z_rho)|k>, with |k> verified an EIGENVECTOR of the one-magnon
         block of H_S (residual, not expectation); (ii) descendant --
         ||Q^-_q|h>||^2 = Z_rho*N - 2 exactly (r3-critic X15), i.e.
         Z_rho - 2/N per site: the conversion is exactly sqrt(Z_rho) ONLY in
         the LSZ limit.  Red modes ``--red-legfactor`` (Z_rho instead of
         sqrt(Z_rho)) and ``--red-descnorm`` (the r3 overclaim: "N-free per
         site" at finite N, i.e. ||Q^-_q|h>||^2 = Z_rho*N).

Constants remaining in the file, ALL declared (r3-critic M2 discipline —
the r3 claim "there is no acceptance constant in the file" was FALSE and is
retracted in all four layers; the honest statement is):
  * DECISION_BAND = 0.08     -- pre-registered in the data file, checked;
  * the C6 acceptance band and the DISPLAY exponent band -- DERIVED at
    runtime from the data's error column;
  * EXACT_TOL, 1e-10 in C8   -- machine tolerances on EXACT identities,
    where the nearest competing hypothesis differs at O(1) (r3-critic n3);
  * ROW_BAND_SANITY = 3.0    -- a declared robustness-GUARD multiplier
    (r3-critic m2): a single row whose quoted error exceeds 3x the median
    row error is rejected as corrupted.  It can only REJECT data, never
    accept it, so it is a guard, not an acceptance constant.  On the true
    data the worst row is 2.29x the median.  STRUCTURAL BLIND SPOT
    (r4-critic m4): the guard is a RATIO (max/median), so it cannot see a
    UNIFORM inflation of the whole error column, which loosens the derived
    acceptance band proportionally; the only backstop on that channel is
    the band < DECISION_BAND subsumption guard, and no conclusion is
    exposed because both refutations hold at the pre-registered 0.08 with
    5-37x margins and need no derived band at all.
No constant-true ``require`` remains: the r4 guard on the derived exponent
band and C5's two DISPLAY guards were deductively subsumed by earlier gates
and are deleted (r4-critic m3; r5-critic m3).

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
EXACT_TOL = 1.0e-12
SPINS = (0.5, 1.0, 1.5, 2.0)
LEGACY_R2_BAND = 0.02    # reported for continuity only; gates nothing
ROW_BAND_SANITY = 3.0    # declared GUARD multiplier (can only reject); see docstring
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


def apply_charge(state: dict, momentum: float, sites: int, two_s: int,
                 red_ladder: bool = False) -> dict:
    """Q^-_k acting on a sparse state: sum_x e^{ikx} S^-_x."""
    out: dict = {}
    for x in range(sites):
        phase = np.exp(1j * momentum * x)
        lowered = apply_lowering(state, x, two_s, red_ladder)
        out = combine(out, {c: phase * a for c, a in lowered.items()})
    return out


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
def check_order_parameter_residue(red_ladder: bool) -> tuple[float, float]:
    worst = 0.0
    worst_two_magnon = 0.0   # sub-gate (v) alone (r4-critic m5)
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
    # (iv) soft-leg norm by construction: ||Q^-_k|Om>||^2 / N = 2S at each k.
    # The r3 sub-gate that paired this loop with a cross-momentum
    # orthogonality test is DELETED: translation invariance makes those
    # overlaps identically zero for ANY ladder element (r3-critic M3(b)(i)
    # probed elements 1.0/3.7/-5.0/1e6 -- nothing moved), and the
    # require(len(momenta) >= 3) that killed cB_onek was constant-true.
    # Honest statement: a mutation that merely SHRINKS this loop reduces
    # coverage and is not detected by any gate; each retained momentum's
    # norm check is individually genuine (it moves under --red-ladder).
    for two_s in (1, 2, 3, 4):
        for sites in (6, 9):
            vacuum_state = {tuple([0] * sites): 1.0}
            for j in (0, 1, 2):
                momentum = 2.0 * np.pi * j / sites
                charged = apply_charge(vacuum_state, momentum, sites, two_s, red_ladder)
                norm_squared = inner(charged, charged).real
                worst = max(worst, abs(norm_squared / sites - two_s))
    # (v) NEW (r4, replacing the deleted no-op): two-magnon SAME-total-
    # momentum overlap.  For even N and k2 = k1 + pi, the states
    # (Q^-_{k1})^2|Om> and (Q^-_{k2})^2|Om> carry the SAME total momentum
    # 2*k1 (mod 2pi), so their overlap is NOT forced to vanish by
    # translation invariance; it is fixed by the ladder at n = 0 AND n = 1
    # plus the coincidence combinatorics.  Closed form, derived on paper
    # (r4 section 6.2), independent of this code:
    #   <(Q_{k1})^2 Om,(Q_{k2})^2 Om>
    #     = 4(2S)^2 sum_{x<y} (-1)^{x+y}  +  2*2S*(2S-1) * sum_x 1
    #     = 4(2S)^2 (-N/2) + 2*2S*(2S-1)*N  =  -2*N*2S .
    # This gate CAN fail: --red-ladder moves it at every 2S >= 2 (the
    # coincidence term scales with the n = 1 element squared); its
    # ISOLATED error is reported separately on the banner, because under
    # --red-ladder the aggregate max is set by sub-gate (iii), so no red
    # mode names (v) in its exit path (r4-critic m5).  What (v) adds over
    # (ii) is COMPOSITION-path coverage -- apply_charge o apply_charge,
    # inner, and the coincidence bookkeeping -- and NOT ladder coverage:
    # (ii) already pins every ladder element exactly at every n <= 2S-1.
    # At 2S = 1 it is insensitive (the coincidence term carries 2S-1 = 0).
    for two_s in (1, 2, 3, 4):
        for sites in (6, 8):
            vacuum_state = {tuple([0] * sites): 1.0}
            k1 = 2.0 * np.pi / sites
            k2 = k1 + np.pi
            two_a = apply_charge(
                apply_charge(vacuum_state, k1, sites, two_s, red_ladder),
                k1, sites, two_s, red_ladder)
            two_b = apply_charge(
                apply_charge(vacuum_state, k2, sites, two_s, red_ladder),
                k2, sites, two_s, red_ladder)
            overlap = inner(two_a, two_b)
            predicted = -2.0 * sites * two_s
            worst_two_magnon = max(worst_two_magnon, abs(overlap - predicted))
            worst = max(worst, abs(overlap - predicted))
    require(worst < EXACT_TOL, f"D24N-C2 ladder/soft-leg-norm error {worst:.3e}")
    return worst, worst_two_magnon


# --------------------------------------------------------------------------
# D24N-C3 : the Ward residue is exactly linear in Z_rho (charge-created leg)
# --------------------------------------------------------------------------
def check_ward_residue_scaling(red_ward: bool) -> tuple[float, float, float, float]:
    """Gate: <h|Q_0^dag J^-_0|h> = Z_rho * 2iJ sin h against the
    CHARGE-CREATED leg (the normalisation clause (d)2 is quoted in).

    Also returns, for the DISPLAY line, the same residue read against
    (b)'s leg in TWO scopes (r4-critic M1).  (b)'s leg is the
    delta-normalised ASYMPTOTIC magnon, and the charge-created leg here is
    the DESCENDANT one, Q^-_0|h>, whose norm is ||Q^-_0|h>||^2 =
    Z_rho*N - 2 (C8(ii)) and not Z_rho*N.  So:
      * LSZ-limit value   = |residue| / sqrt(Z_rho)          -- what the
        conversion becomes as N -> infinity, the register D24(b)
        amplitudes are defined in;
      * finite-N value    = |residue| / (||Q^-_0|h>|| / sqrt(N)), i.e.
        divided by the MEASURED leg ratio sqrt(Z_rho - 2/N).
    r4 printed the first labelled as the second (3.28% out at 2S = 4,
    N = 8: 2.828427 against 2.921187).  Both are DISPLAY only -- as gates
    they would be deductively subsumed by C3 + C8."""
    sites = 8
    coupling = 1.0
    worst = 0.0
    display_cc = 0.0
    display_lsz = 0.0
    display_finite = 0.0
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
            if two_s == 4 and index == 1:
                display_cc = abs(measured)
                display_lsz = abs(measured) / np.sqrt(float(two_s))
                # the MEASURED descendant-leg ratio, not the closed form:
                # ||Q^-_0|h>|| / sqrt(N) = sqrt(Z_rho - 2/N)  (C8(ii))
                leg_ratio = np.sqrt(inner(charged, charged).real / sites)
                display_finite = abs(measured) / leg_ratio
    require(worst < EXACT_TOL,
            f"D24N-C3 Ward residue Z-scaling error {worst:.3e}")
    return worst, display_cc, display_lsz, display_finite


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

    Guards (all can only REJECT): zero band; missing error column; a band
    so wide C4 would subsume C6; and (r4, r3-critic m2) a single corrupted
    row -- any row whose |error|*S exceeds ROW_BAND_SANITY x the median row
    value fails, so one inflated entry cannot silently loosen the gate
    (r3-critic's mutant: one S=1/2 error -> 0.1579 gave band 0.0790 and
    passed r3's one-sided guard; here it is 3.78x the median and dies).

    Declared blind spot (r4-critic m4): the corrupted-entry guard is a
    RATIO, max/median, hence invariant under multiplying the WHOLE error
    column by a constant -- a uniform inflation still loosens this band
    proportionally, up to the DECISION_BAND ceiling, and only the
    subsumption guard below stops it.  (A x1.6 uniform inflation combined
    with a -6% slope shift passes every gate.)  Nothing is exposed: both
    refutations hold at the pre-registered 0.08 with 5-37x margins and
    need no derived band at all.
    """
    row_bands = []
    for row in payload["A_ring_summary"]:
        spin = float(row["S"])
        require("error" in row, "D24N-C6 data row has no quoted error column")
        row_bands.append(abs(float(row["error"])) * spin)
    worst = max(row_bands)
    require(worst > 0.0, "D24N-C6 derived acceptance band is zero")
    median = float(np.median(row_bands))
    require(median > 0.0, "D24N-C6 median row error is zero")
    ratio = worst / median
    require(ratio <= ROW_BAND_SANITY,
            f"D24N-C6 corrupted error entry: worst row band {worst:.4f} is "
            f"{ratio:.2f}x the median row band {median:.4f} "
            f"(guard {ROW_BAND_SANITY}x)")
    require(worst < DECISION_BAND,
            f"D24N-C6 derived band {worst:.4f} is not tighter than the "
            f"pre-registered {DECISION_BAND}: C6 would be subsumed by C4")
    return worst


def derive_exponent_band(accept_band: float) -> float:
    """The fitted-exponent band, DERIVED from the same quoted-error column
    (r4; r3-critic M2 fix demand, taken: "propagate the same error column
    through the log fit").

    A uniform relative slope shift delta moves the lstsq exponent by
    exactly [sum_s log(2S_s) / sum_s log^2(2S_s)] * log(1/(1-delta)) over
    the non-degenerate fit spins.  The worst shift the acceptance gate
    admits is delta = accept_band (in dev*S units, dev*S = |relative
    shift| to first order), and log(1/(1-b)) >= log(1+b), so this is the
    two-sided worst case.  On the shipped data: 0.8805 * 0.04904 = 0.0432
    -- WIDER than r3's hand-chosen 0.03, as calibration requires: no
    perturbation inside the data's own quoted error can fail this
    comparison.

    DERIVING the band PROVES the fitted-exponent comparison is
    deductively SUBSUMED by the acceptance gate at these calibrated
    bands: part 1 requires |1 - mean_s * s| <= b at every fit spin, hence
    |log(mean_s * s)| <= log(1/(1-b)), hence
    |p_fit - 1| = |sum x_s log(mean_s*s)| / sum x_s^2
                <= [sum x_s / sum x_s^2] * log(1/(1-b)) = this band.
    So a require() on it can never fire on data that reached it -- it is
    the C5 situation (r3-critic X11), and like C5 it is demoted to
    DISPLAY (r4 section 6.1; the standing checker obligations demand the
    subsumption be reported, not gated over).  r3's 0.03 gate did
    independent work precisely BECAUSE it was miscalibrated.  The
    symbolic pin (2S)^p = 2S remains the gated content of C6 part 2.
    This function contains no ``require``: the only one r4 had here could
    not fail on any input (r4-critic m3), and the quantity it guards gates
    nothing.
    """
    fit_spins = [s for s in SPINS if abs(2.0 * s - 1.0) > 1.0e-12]
    design = [np.log(2.0 * s) for s in fit_spins]
    ratio = sum(design) / sum(x * x for x in design)
    band = ratio * np.log(1.0 / (1.0 - accept_band))
    # r4's require(band > 0.0) is DELETED (r4-critic m3): by the guards in
    # derive_accept_band, accept_band lies in (0, DECISION_BAND) and ratio
    # is the fixed positive constant 0.880539 over SPINS, so band > 0
    # ALWAYS -- it was a constant-true guard shipped by the round that
    # deleted one for being constant-true.
    return float(band)


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
    """D24N-C5, DISPLAY: the frozen clause misses off rho=1/2, hits at 1/2.

    This function intentionally contains no gate: C4 already forces the
    displayed S=1/2 deviation below DECISION_BAND and every displayed
    off-S=1/2 deviation above it (r5-critic m3).
    """
    deviations = []
    for spin in SPINS:
        measured = float(np.mean(slopes[spin]))
        deviations.append(abs(predicted_jet(spin, None) - measured) * spin)
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


def check_exponent(slopes: dict[float, list[float]],
                   exponent_band: float) -> tuple[float, str]:
    """D24N-C6 part 2: fitted exponent (non-degenerate spins) + symbolic pin.

    The fitted-exponent comparison is DISPLAY, not a gate: at the derived
    band it is deductively subsumed by the acceptance gate (proof in
    ``derive_exponent_band``), so a require() here could never fire on
    data that reached it.  r3's hand-chosen EXPONENT_FIT_BAND = 0.03 is
    deleted (r3-critic M2); the SYMBOLIC pin below is the gated content."""
    fit_spins = [s for s in SPINS if abs(2.0 * s - 1.0) > 1.0e-12]
    design = np.array([[np.log(2.0 * s)] for s in fit_spins])
    target = np.array([np.log(2.0 / float(np.mean(slopes[s]))) for s in fit_spins])
    exponent = float(np.linalg.lstsq(design, target, rcond=None)[0][0])
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
# D24N-C8 : the leg-conversion constant, vacuum AND descendant legs
# --------------------------------------------------------------------------
def check_leg_conversion(red_legfactor: bool,
                         red_descnorm: bool) -> tuple[float, float, float]:
    """(i) vacuum: <k|Q^-_k|Om> = sqrt(Z_rho * N), with |k> the true
    one-magnon state -- |k> is not assumed: the one-magnon block of H_S is
    built from the raw bond matrix and the plane wave is verified to be an
    EIGENVECTOR with eigenvalue omega_S(k) = 2JS(1 - cos k) (residual norm,
    not expectation).

    (ii) descendant (NEW in r4, r3-critic m1/X15): ||Q^-_q|h>||^2 =
    Z_rho*N - 2 exactly, for q != h commensurate -- the conversion factor
    on the leg the adjudication actually applies it to is sqrt(Z_rho) only
    up to O(1/(Z_rho*N)), i.e. only in the LSZ limit.  ``--red-descnorm``
    is the r3 overclaim ("exact, N-free per site" on every leg): predicted
    Z_rho*N, off by exactly 2, dies here.
    """
    sites = 8
    coupling = 1.0
    worst_spectral = 0.0
    worst_overlap = 0.0
    worst_descendant = 0.0
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
            charged = apply_charge(vacuum_state, momentum, sites, two_s)
            vector = np.array([charged.get(b, 0.0) for b in basis])
            overlap = abs(np.vdot(wave, vector))
            power = 1.0 if red_legfactor else 0.5
            predicted = (float(two_s) ** power) * np.sqrt(sites)
            worst_overlap = max(worst_overlap, abs(overlap - predicted))
        # (ii) descendant leg: ||Q^-_q |h>||^2 = Z_rho*N - 2 (q != h)
        for hard_index, soft_index in ((1, 3), (1, 2)):
            hard = 2.0 * np.pi * hard_index / sites
            soft = 2.0 * np.pi * soft_index / sites
            one_magnon = {b: np.exp(1j * hard * x) / np.sqrt(sites)
                          for x, b in enumerate(basis)}
            descendant = apply_charge(one_magnon, soft, sites, two_s)
            norm_squared = inner(descendant, descendant).real
            predicted_norm = (float(two_s) * sites) if red_descnorm \
                else (float(two_s) * sites - 2.0)
            worst_descendant = max(worst_descendant,
                                   abs(norm_squared - predicted_norm))
    require(worst_spectral < 1.0e-10,
            f"D24N-C8 plane wave is not an H_S one-magnon eigenvector "
            f"(residual {worst_spectral:.3e})")
    require(worst_overlap < 1.0e-10,
            f"D24N-C8 leg-conversion factor is not sqrt(Z_rho) "
            f"(error {worst_overlap:.3e})")
    require(worst_descendant < 1.0e-10,
            f"D24N-C8 descendant-leg norm is not Z_rho*N - 2 "
            f"(error {worst_descendant:.3e})")
    return worst_spectral, worst_overlap, worst_descendant


# --------------------------------------------------------------------------
def main() -> None:
    parser = argparse.ArgumentParser(description="D24(d)3 adjudication certificate (r4)")
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
    parser.add_argument("--red-descnorm", action="store_true",
                        help="descendant-leg norm = Z_rho*N ('N-free per site' at "
                             "finite N, the r3 overclaim); death: D24N-C8")
    arguments = parser.parse_args()

    exponent: float | None = 1.0
    if arguments.red_frozen:
        exponent = None
    elif arguments.red_power:
        exponent = 2.0
    elif arguments.red_halfpower:
        exponent = 0.5

    frozen_jet, matched_jet = check_frozen_is_density_blind()
    ladder_error, two_magnon_error = check_order_parameter_residue(arguments.red_ladder)
    ward_error, residue_cc, residue_lsz, residue_finite = \
        check_ward_residue_scaling(arguments.red_ward)
    payload = load_payload(arguments.data)
    slopes = load_ring_slopes(payload)
    accept_band = derive_accept_band(payload)
    exponent_band = derive_exponent_band(accept_band)
    truth_error = check_ground_truth(slopes)
    defect_size, deviations = check_defect(slopes)
    accept_error = check_acceptance(slopes, exponent, accept_band)
    fitted_exponent, degeneracy_note = check_exponent(slopes, exponent_band)
    derived_interval = resolving_interval(slopes, accept_band)
    frozen_interval = resolving_interval(slopes, DECISION_BAND)
    legacy_interval = resolving_interval(slopes, LEGACY_R2_BAND)
    half_power_gap = check_half_power_route(payload)
    spectral_error, overlap_error, descendant_error = check_leg_conversion(
        arguments.red_legfactor, arguments.red_descnorm)

    def show(interval: tuple[float, float] | None) -> str:
        return "empty" if interval is None else f"[{interval[0]:.3f}, {interval[1]:.3f}]"

    print(f"D24N-C1 GUARD frozen_jet_coefficient={frozen_jet} matched={matched_jet}")
    print(f"D24N-C2 ladder x4 (residue, dense/occupation cross-check, multi-quantum "
          f"norms, soft-leg norm + two-magnon same-momentum overlap = -2N*Z_rho), "
          f"max_error={ladder_error:.3e}; sub-gate (v) alone (the two-magnon "
          f"overlap, composition-path coverage) error={two_magnon_error:.3e}")
    print(f"D24N-C3 Ward residue = Z_rho*2iJ sin h against the CHARGE-CREATED leg, "
          f"max_error={ward_error:.3e}")
    print(f"D24N-C3 DISPLAY both normalisations at 2S=4, h=pi/4 (gates nothing; "
          f"deductively C3 / C8): charge-created |residue|={residue_cc:.6f} "
          f"(= Z_rho*2J sin h); against (b)'s asymptotic leg the same residue "
          f"is {residue_lsz:.6f} (= sqrt(Z_rho)*2J sin h) in the LSZ LIMIT, and "
          f"{residue_finite:.6f} at this finite N, where the measured "
          f"descendant-leg ratio is sqrt(Z_rho - 2/N), not sqrt(Z_rho) "
          f"(C8(ii)); the two normalisations coincide only at Z_rho = 1")
    print(f"D24N-C4 ansatz-free slopes vs 1/S: max_rel_dev={truth_error:.4f} "
          f"(pre-registered band {DECISION_BAND})")
    print("D24N-C5 DISPLAY frozen-clause relative deviations at S=1/2,1,3/2,2: "
          + ", ".join(f"{d:.3f}" for d in deviations)
          + f"  -> defect size {defect_size:.3f}")
    print(f"D24N-C6 candidate max_rel_dev={accept_error:.4f} vs acceptance band "
          f"{accept_band:.4f} DERIVED from the data's own quoted error "
          f"(< pre-registered {DECISION_BAND}, so C6 is not subsumed by C4); "
          f"symbolic (2S)^p=2S root p=1 at S=1,3/2,2; {degeneracy_note}")
    print(f"D24N-C6 DISPLAY fitted exponent={fitted_exponent:.4f} vs 1, derived "
          f"exponent band {exponent_band:.4f} (0.8805*log(1/(1-band)), same error "
          f"column; gates nothing -- at calibrated bands this comparison is "
          f"deductively subsumed by the acceptance gate, proof in "
          f"derive_exponent_band; r3's 0.03 gate did independent work only "
          f"because it was miscalibrated)")
    print(f"D24N-C6 resolving intervals for p: at the derived band "
          f"{show(derived_interval)}; at the pre-registered band "
          f"{show(frozen_interval)}; at r2's retired 0.02 band "
          f"{show(legacy_interval)} (reported, gates nothing)")
    print(f"D24N-C7 DISPLAY N-dependent half-power route gap={half_power_gap:.3e}")
    print(f"D24N-C8 vacuum leg Q^-_k|Om> = sqrt(Z_rho)|k>: eigenvector residual="
          f"{spectral_error:.3e}, overlap error={overlap_error:.3e}; descendant leg "
          f"||Q^-_q|h>||^2 = Z_rho*N - 2: error={descendant_error:.3e} (so the "
          f"conversion is sqrt(Z_rho) exactly on the vacuum, and only in the LSZ "
          f"limit on the descendant leg); leg conversion alone gives "
          f"a_leg = Z_rho^(-1/2), refuted by --red-halfpower at the "
          f"PRE-REGISTERED band")
    print("PASS: D24-VAL candidate a_leg = 1/(2 rho) matches; frozen a_leg = 1 and "
          "leg-conversion a_leg = Z_rho^(-1/2) both refuted; the D24(d)3b "
          "definition itself fixes no value (lemma AMP open)")


if __name__ == "__main__":
    main()
