#!/usr/bin/env python3
"""Red-capable certificate for theory/amp.md.

Verdict certified: OBSTRUCTION.  D24(b)+(d) fix one inverse square root from
the charge-created/asymptotic-leg conversion but do not fix the remaining
nonzero scalar in D24(d)3b.

AMP-C1  Symbolic D24 relation packages exist for an arbitrary nonzero
        ``a_leg`` while the D24(b) convention, Ward residue, and zero
        reduced/contact terms are held fixed.  This is a relation-level
        witness, not a microscopic source construction.
AMP-C2  Recompute D24N-C8 on sparse spin-S states: the vacuum factor is
        sqrt(Z_rho), and the descendant norm is Z_rho*N-2.  The normalized
        descendant projector has coefficient R/sqrt(Z_rho*N-2), not
        R/(Z_rho*N-2).  ``--red-double-count`` makes precisely the latter
        substitution and must die at AMP-C2.
AMP-C3  The finite-N descendant conversion tends to Z_rho^(-1/2), not
        Z_rho^(-1); it supplies no surviving second factor.
AMP-C4  Against the pre-registered 0.08 band, the pure-leg prediction
        a_leg=Z_rho^(-1/2) is separated from the ansatz-free slopes at
        S=1,3/2,2.  ``--red-pure-leg`` registers a purported AMP proof whose
        only mechanism is that leg rescaling; it must die at AMP-C4.

Green exit is 0.  Every failure goes through SystemExit(1); there are no bare
asserts, so ``python3 -O`` cannot disable a gate.
"""

from __future__ import annotations

import argparse
import json
import math
import sys
from pathlib import Path

import sympy as sp


EXACT_TOL = 1.0e-10
DECISION_BAND = 0.08
SPINS = (0.5, 1.0, 1.5, 2.0)
DEFAULT_DATA = (
    Path(__file__).resolve().parents[2]
    / "numerics"
    / "results"
    / "spin1-bc-falsifier.json"
)


def fail(message: str) -> None:
    print(f"FAIL: {message}", file=sys.stderr)
    raise SystemExit(1)


def require(condition: bool, message: str) -> None:
    if not condition:
        fail(message)


def inner(first: dict[tuple[int, ...], complex],
          second: dict[tuple[int, ...], complex]) -> complex:
    return sum(
        complex(first[key]).conjugate() * second[key]
        for key in first
        if key in second
    )


def add_scaled(target: dict[tuple[int, ...], complex],
               source: dict[tuple[int, ...], complex],
               scale: complex) -> None:
    for key, value in source.items():
        target[key] = target.get(key, 0.0j) + scale * value


def lower_at(state: dict[tuple[int, ...], complex], site: int,
             z_rho: int) -> dict[tuple[int, ...], complex]:
    """Apply S^- at one site in the occupation basis n=0,...,2S."""
    out: dict[tuple[int, ...], complex] = {}
    for configuration, amplitude in state.items():
        occupation = configuration[site]
        if occupation >= z_rho:
            continue
        ladder = math.sqrt((occupation + 1) * (z_rho - occupation))
        updated = list(configuration)
        updated[site] += 1
        key = tuple(updated)
        out[key] = out.get(key, 0.0j) + ladder * amplitude
    return out


def apply_charge(state: dict[tuple[int, ...], complex], momentum: float,
                 sites: int, z_rho: int) -> dict[tuple[int, ...], complex]:
    out: dict[tuple[int, ...], complex] = {}
    for site in range(sites):
        phase = complex(math.cos(momentum * site), math.sin(momentum * site))
        add_scaled(out, lower_at(state, site, z_rho), phase)
    return out


def scaled(state: dict[tuple[int, ...], complex],
           factor: complex) -> dict[tuple[int, ...], complex]:
    return {key: factor * value for key, value in state.items()}


def difference_norm(first: dict[tuple[int, ...], complex],
                    second: dict[tuple[int, ...], complex]) -> float:
    keys = set(first) | set(second)
    return math.sqrt(sum(abs(first.get(key, 0.0j) - second.get(key, 0.0j)) ** 2
                         for key in keys))


def check_arbitrary_d24_constant() -> tuple[sp.Expr, sp.Expr, float]:
    """AMP-C1: D24's displayed relations leave a_leg as a free symbol."""
    momentum, velocity, hard_amplitude = sp.symbols(
        "k v_h M_1", nonzero=True
    )
    channel_sign = sp.symbols("chi", nonzero=True)
    a_leg = sp.symbols("a_leg", nonzero=True)

    ward_residue = 2 * sp.I * velocity * hard_amplitude
    flux = a_leg * (-sp.I * channel_sign / velocity)
    descendant = (sp.exp(sp.I * momentum) - 1) * flux * ward_residue
    recovered_flux = sp.simplify(
        descendant
        / ((sp.exp(sp.I * momentum) - 1) * ward_residue)
    )
    recovered_constant = sp.simplify(
        sp.I * velocity * recovered_flux / channel_sign
    )
    leading_jet = sp.simplify(sp.diff(descendant, momentum).subs(momentum, 0))

    require(sp.simplify(recovered_flux - flux) == 0,
            "AMP-C1 descendant quotient did not recover L")
    require(sp.simplify(recovered_constant - a_leg) == 0,
            "AMP-C1 D24(d)3b did not leave a_leg symbolic")
    require(sp.simplify(leading_jet
                        - 2 * sp.I * a_leg * channel_sign * hard_amplitude) == 0,
            "AMP-C1 descendant jet has the wrong coefficient")
    require(a_leg in recovered_constant.free_symbols,
            "AMP-C1 a_leg was accidentally fixed by the displayed relations")

    # Two fixed-convention relation packages: identical hard amplitude and
    # Ward residue, different physical L/E_desc.  This is not a rescaling of
    # the D24(b) leg; the convention and both anchors are held fixed.
    trial_constants = (0.37, 0.91)
    worst_anchor_change = 0.0
    for hard in (0.45, 0.8, 1.1):
        v_h = 2.0 * math.sin(hard)
        m_1 = 1.0 + 0.2 * math.cos(hard)
        reference_residue = 2.0j * v_h * m_1
        for trial in trial_constants:
            l_value = trial * (-1.0j / v_h)
            e_desc = (complex(math.cos(0.07), math.sin(0.07)) - 1.0) \
                * l_value * reference_residue
            quotient = e_desc / (
                (complex(math.cos(0.07), math.sin(0.07)) - 1.0)
                * reference_residue
            )
            require(abs(quotient - l_value) < EXACT_TOL,
                    "AMP-C1 numerical quotient failed for an arbitrary constant")
            recovered = 1.0j * v_h * quotient
            require(abs(recovered - trial) < EXACT_TOL,
                    "AMP-C1 numerical D24(d)3b profile failed")
            worst_anchor_change = max(
                worst_anchor_change,
                abs(reference_residue - 2.0j * v_h * m_1),
            )
    return recovered_constant, leading_jet, worst_anchor_change


def check_leg_and_projection(red_double_count: bool) -> tuple[float, float, float]:
    """AMP-C2: exact C8 factors and the normalized-projector coefficient."""
    sites = 8
    worst_vacuum = 0.0
    worst_descendant = 0.0
    worst_projector = 0.0

    for z_rho in (1, 2, 3, 4):
        vacuum_configuration = tuple([0] * sites)
        vacuum = {vacuum_configuration: 1.0 + 0.0j}
        for momentum_index in (1, 2):
            momentum = 2.0 * math.pi * momentum_index / sites
            charged_vacuum = apply_charge(vacuum, momentum, sites, z_rho)
            vacuum_norm_squared = inner(charged_vacuum, charged_vacuum).real
            worst_vacuum = max(
                worst_vacuum,
                abs(vacuum_norm_squared / sites - z_rho),
            )

        hard = 2.0 * math.pi / sites
        soft = 4.0 * math.pi / sites
        hard_state: dict[tuple[int, ...], complex] = {}
        for site in range(sites):
            configuration = [0] * sites
            configuration[site] = 1
            phase = complex(math.cos(hard * site), math.sin(hard * site))
            hard_state[tuple(configuration)] = phase / math.sqrt(sites)
        descendant = apply_charge(hard_state, soft, sites, z_rho)
        descendant_norm_squared = inner(descendant, descendant).real
        expected_norm_squared = z_rho * sites - 2.0
        worst_descendant = max(
            worst_descendant,
            abs(descendant_norm_squared - expected_norm_squared),
        )

        # Exact rank-one projection.  The coefficient on the normalized
        # vector is R/sqrt(n), although the coefficient on the unnormalized
        # vector is R/n.  The red mutation confuses those two registers.
        probe = dict(descendant)
        first_key = next(iter(descendant))
        probe[first_key] += 0.37 - 0.19j
        residue = inner(descendant, probe)
        projected = scaled(descendant, residue / descendant_norm_squared)
        normalized_descendant = scaled(
            descendant, 1.0 / math.sqrt(descendant_norm_squared)
        )
        normalized_coefficient = residue / math.sqrt(descendant_norm_squared)
        if red_double_count:
            normalized_coefficient = residue / descendant_norm_squared
        reconstructed = scaled(normalized_descendant, normalized_coefficient)
        worst_projector = max(
            worst_projector,
            difference_norm(projected, reconstructed),
        )

    require(worst_vacuum < EXACT_TOL,
            f"AMP-C2 vacuum leg is not sqrt(Z_rho), error {worst_vacuum:.3e}")
    require(worst_descendant < EXACT_TOL,
            "AMP-C2 descendant norm is not Z_rho*N-2, "
            f"error {worst_descendant:.3e}")
    require(worst_projector < EXACT_TOL,
            "AMP-C2 PURE-LEG DOUBLE COUNT: the inverse norm-squared "
            "coefficient was used as the coefficient of the normalized leg; "
            f"projector error {worst_projector:.3e}")
    return worst_vacuum, worst_descendant, worst_projector


def check_finite_n_route() -> float:
    """AMP-C3: finite-N mismatch has the same half-power LSZ limit."""
    worst_scaled_error = 0.0
    for z_rho in (1.0, 2.0, 3.0, 4.0):
        limit = 1.0 / math.sqrt(z_rho)
        for sites in (40, 80, 160, 320):
            finite = 1.0 / math.sqrt(z_rho - 2.0 / sites)
            # N*(finite-limit) remains bounded; there is no O(1) residue.
            worst_scaled_error = max(
                worst_scaled_error,
                sites * abs(finite - limit),
            )
        require(abs(1.0 / math.sqrt(z_rho - 2.0 / 100000.0) - limit)
                < 3.0e-5,
                "AMP-C3 finite-N factor does not tend to Z_rho^(-1/2)")
    return worst_scaled_error


def check_pure_leg_fence(data_path: Path,
                         red_pure_leg: bool) -> tuple[float, list[float], list[float]]:
    """AMP-C4: pre-registered rejection of the pure-leg-only candidate."""
    require(data_path.is_file(), f"AMP-C4 missing data file {data_path}")
    payload = json.loads(data_path.read_text())
    require("decision_band" in payload,
            "AMP-C4 data file has no pre-registered decision_band")
    band = float(payload["decision_band"])
    require(abs(band - DECISION_BAND) < EXACT_TOL,
            f"AMP-C4 decision band moved from 0.08 to {band}")
    require("A_ring_summary" in payload,
            "AMP-C4 data file has no A_ring_summary")

    grouped: dict[float, list[float]] = {}
    for row in payload["A_ring_summary"]:
        grouped.setdefault(float(row["S"]), []).append(
            float(row["slope_extrapolated"])
        )
    deviations: list[float] = []
    margins: list[float] = []
    offenders: list[str] = []
    for spin in SPINS:
        require(spin in grouped, f"AMP-C4 missing slope rows at S={spin}")
        measured = sum(grouped[spin]) / len(grouped[spin])
        pure_leg_jet = 2.0 / math.sqrt(2.0 * spin)
        deviation = abs(pure_leg_jet - measured) * spin
        deviations.append(deviation)
        margins.append(deviation / band)
        if deviation > band:
            offenders.append(f"S={spin} dev={deviation:.4f}")

    require(deviations[0] < band,
            "AMP-C4 pure-leg route should coincide at the degenerate S=1/2 point")
    require(all(value > band for value in deviations[1:]),
            "AMP-C4 pure-leg route was not rejected off S=1/2 at the "
            f"pre-registered band {band}")
    if red_pure_leg:
        require(not offenders,
                "AMP-C4 PURE-LEG PROPOSAL: a mechanism reducing to the exact "
                "D24N-C8 leg rescaling cannot establish AMP at the "
                f"pre-registered band {band:.2f}; " + "; ".join(offenders))
    return band, deviations, margins


def main() -> None:
    parser = argparse.ArgumentParser(description="AMP obstruction certificate")
    parser.add_argument("--data", type=Path, default=DEFAULT_DATA,
                        help="path to spin1-bc-falsifier.json (copies allowed)")
    parser.add_argument(
        "--red-double-count",
        action="store_true",
        help="use R/(Z*N-2) as a normalized-leg coefficient; death AMP-C2",
    )
    parser.add_argument(
        "--red-pure-leg",
        action="store_true",
        help="claim AMP using only D24N-C8 leg rescaling; death AMP-C4",
    )
    arguments = parser.parse_args()

    free_constant, jet, anchor_error = check_arbitrary_d24_constant()
    vacuum_error, descendant_error, projector_error = check_leg_and_projection(
        arguments.red_double_count
    )
    finite_n_bound = check_finite_n_route()
    band, deviations, margins = check_pure_leg_fence(
        arguments.data, arguments.red_pure_leg
    )

    print("AMP-C1 arbitrary-constant D24 packages: recovered "
          f"a_leg={free_constant}, jet={jet}; fixed-anchor error={anchor_error:.3e}; "
          "this certifies relation-level underdetermination, not microscopic "
          "source existence")
    print("AMP-C2 D24N-C8 reconstruction: vacuum per-site factor-squared "
          f"error={vacuum_error:.3e}; descendant Z_rho*N-2 error="
          f"{descendant_error:.3e}; normalized-projector error="
          f"{projector_error:.3e}; exactly one inverse square root survives")
    print("AMP-C3 finite-N route: N*|a_N-Z_rho^(-1/2)| bounded by "
          f"{finite_n_bound:.3e}; limit is the half-power, not 1/Z_rho")
    print("AMP-C4 pure-leg-only deviations at S=1/2,1,3/2,2: "
          + "/".join(f"{value:.4f}" for value in deviations)
          + f" against PRE-REGISTERED band {band:.2f}; margins off the "
          "degenerate point "
          + "/".join(f"{value:.1f}x" for value in margins[1:]))
    print("PASS: OBSTRUCTION — D24 fixes one leg factor Z_rho^(-1/2), "
          "admits an arbitrary nonzero residual class scalar, and supplies no "
          "independent second mechanism fixing a_leg=1/Z_rho")


if __name__ == "__main__":
    main()
