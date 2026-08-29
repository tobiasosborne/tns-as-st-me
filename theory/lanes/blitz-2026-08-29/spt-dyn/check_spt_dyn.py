#!/usr/bin/env python3
"""Pre-registered red-capable checks for the spt-dyn ED certificate.

The first run is intentionally red because ``results.json`` does not yet
exist.  Once the computation has been implemented, this checker validates the
stored observables, their honest T0--T3 dispositions, and exact algebraic
residues.  ``--red`` mutates a load-bearing Hermiticity datum and must fail.
"""

from __future__ import annotations

import argparse
import json
import math
from pathlib import Path

import numpy as np


HERE = Path(__file__).resolve().parent
RESULTS = HERE / "results.json"

# Frozen before the first numerical run.  T0/T1/T3 are inherited verbatim
# from spt-scoping-draft.md; T2's word "same" is operationalized as 10%
# relative agreement because the old table supplied no numerical tolerance.
T0_HALDANE_MIN = 0.45
T0_HALDANE_MAX = 0.50
T0_TRIV_MAX = 0.05
T1_HALDANE_MIN = 0.90
T1_TRIV_MAX = 0.05
T2_RELATIVE_TOL = 0.10
T3_RATIO_MIN = 10.0
ALGEBRA_TOL = 2.0e-12
NORM_TOL = 2.0e-10


def require(condition: bool, message: str) -> None:
    if not condition:
        raise SystemExit(f"FAIL: {message}")


def expected_dispositions(data: dict) -> dict[str, bool]:
    d0 = data["models"]["D=0"]
    d3 = data["models"]["D=3"]
    t2 = data["T2"]
    t3 = data["T3"]
    return {
        "T0": (
            T0_HALDANE_MIN <= abs(d0["T0"]["m_left"]) <= T0_HALDANE_MAX
            and abs(d3["T0"]["m_left"]) < T0_TRIV_MAX
        ),
        "T1": (
            abs(d0["T1"]["F0"]) > T1_HALDANE_MIN
            and abs(d3["T1"]["F0"]) < T1_TRIV_MAX
        ),
        "T2": t2["relative_intercept_difference"] < T2_RELATIVE_TOL,
        "T3": t3["memory_ratio_D0_over_D3"] > T3_RATIO_MIN,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--red", action="store_true",
        help="mutate the recorded Hamiltonian Hermiticity residue; must fail",
    )
    args = parser.parse_args()

    require(RESULTS.exists(), "results.json is absent (intentional first red run)")
    data = json.loads(RESULTS.read_text())
    require(data["schema"] == "spt-dyn-ed-v1", "unexpected result schema")
    require(data["downgrade"]["requested_sizes"] == [32, 48, 64], "size spec drift")
    require(max(data["downgrade"]["actual_sizes"]) < 32, "downgrade record is false")

    hermiticity = float(data["validation"]["max_hermiticity_residue"])
    if args.red:
        hermiticity += 1.0e-4
    require(hermiticity < ALGEBRA_TOL, f"Hamiltonian Hermiticity residue {hermiticity:.3e}")
    require(
        float(data["validation"]["max_norm_drift"]) < NORM_TOL,
        "time-evolution norm drift exceeded the frozen tolerance",
    )
    require(
        float(data["validation"]["max_charge_sector_residue"]) < ALGEBRA_TOL,
        "a state escaped its exact total-Sz sector",
    )

    # Reconstruct all derived T2 numbers from the raw complex form factor.
    intercepts = {}
    for model in ("D=0", "D=3"):
        points = data["T2"]["models"][model]["points"]
        for point in points:
            form_factor = complex(*point["F"])
            quotient = complex(*point["F_over_eik_minus_1"])
            rebuilt = form_factor / (np.exp(1j * point["k"]) - 1.0)
            require(abs(quotient - rebuilt) < 2.0e-11, f"{model} T2 quotient mismatch")
            require(
                abs(point["soft_coefficient_minus_imag"] + quotient.imag) < 2.0e-11,
                f"{model} T2 coefficient mismatch",
            )
        x = np.asarray([point["k"] ** 2 for point in points])
        y = np.asarray([point["soft_coefficient_minus_imag"] for point in points])
        intercept, _ = np.polynomial.polynomial.polyfit(x, y, 1)
        stored = data["T2"]["models"][model]["k2_fit_intercept"]
        require(abs(intercept - stored) < 2.0e-11, f"{model} T2 fit mismatch")
        intercepts[model] = intercept
    rebuilt_relative = abs(intercepts["D=0"] - intercepts["D=3"]) / abs(
        0.5 * (intercepts["D=0"] + intercepts["D=3"])
    )
    require(
        abs(rebuilt_relative - data["T2"]["relative_intercept_difference"]) < 2.0e-11,
        "T2 model-comparison mismatch",
    )

    # Check that T3's exclusive channel is red at t=0 and that its summaries
    # really are derived from the central momentum row.
    for model in ("D=0", "D=3"):
        dyn = data["T3"]["models"][model]
        scans = dyn["momentum_scan"]
        require(len(scans) == 3, f"{model} did not test three adjacent momenta")
        for scan in scans:
            require(scan["flip_probability_initial"] < 2.0e-12, f"{model} flip channel not exclusive")
            require(0.0 <= scan["flip_probability_post"] <= 1.0 + 2.0e-12, f"{model} invalid probability")
            require(scan["reflection_turnaround"], f"{model} packet did not turn around")
        central = scans[1]
        require(
            abs(dyn["central_flip_amplitude_raw"] ** 2 - central["flip_probability_post"]) < 2.0e-11,
            f"{model} central flip amplitude mismatch",
        )

    expected = expected_dispositions(data)
    observed = {key: bool(value) for key, value in data["scientific_gates"].items()}
    require(observed == expected, f"scientific disposition mismatch: {observed} != {expected}")

    for model in ("D=0", "D=3"):
        for key in ("ground_norm_error", "edge_partner_norm_error"):
            require(abs(data["models"][model]["validation"][key]) < NORM_TOL, f"{model} {key}")
    require(math.isfinite(data["T3"]["flip_amplitude_D0"]), "non-finite T3 amplitude")
    print("SPT-DYN ED VALIDATION PASS")
    print("scientific gates:", observed)


if __name__ == "__main__":
    main()
