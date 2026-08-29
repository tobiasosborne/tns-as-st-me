#!/usr/bin/env python3
"""Derive the compact, auditable scientific ledger from results.json."""

from __future__ import annotations

import json
from pathlib import Path

import numpy as np


HERE = Path(__file__).resolve().parent
data = json.loads((HERE / "results.json").read_text())

t2_sensitivity = {}
for model in ("D=0", "D=3"):
    rows = data["T2"]["models"][model]["points"]
    fits = []
    for start in range(3):
        subset = rows[start:]
        x = np.asarray([row["k"] ** 2 for row in subset])
        y = np.asarray([row["soft_coefficient_minus_imag"] for row in subset])
        intercept, slope = np.polynomial.polynomial.polyfit(x, y, 1)
        fits.append(
            {
                "minimum_L": subset[0]["L"],
                "number_of_points": len(subset),
                "intercept": float(intercept),
                "slope": float(slope),
            }
        )
    t2_sensitivity[model] = fits

relative_by_fit = []
for index in range(3):
    c0 = t2_sensitivity["D=0"][index]["intercept"]
    c3 = t2_sensitivity["D=3"][index]["intercept"]
    relative_by_fit.append(abs(c0 - c3) / abs(0.5 * (c0 + c3)))

ledger = {
    "T0": {
        model: [
            {"L": row["L"], "m_left": row["m_left_a"]}
            for row in data["models"][model]["static_convergence"]
        ]
        for model in ("D=0", "D=3")
    },
    "T1": {
        model: [
            {"L": row["L"], "F0": row["projected_F0"], "raw_F0": row["raw_F0"]}
            for row in data["models"][model]["static_convergence"]
        ]
        for model in ("D=0", "D=3")
    },
    "T2": {
        "fit_sensitivity": t2_sensitivity,
        "relative_difference_by_minimum_L": relative_by_fit,
    },
    "T3": {
        model: {
            "flip_amplitudes": [
                row["flip_amplitude_post"]
                for row in data["T3"]["models"][model]["momentum_scan"]
            ],
            "post_separation_achieved": [
                row["post_separation_achieved"]
                for row in data["T3"]["models"][model]["momentum_scan"]
            ],
            "unconditioned_memory": data["T3"]["models"][model]["memory_signal_raw"],
            "postselected_budget_defect": data["T3"]["models"][model][
                "postselected_charge_budget_defect"
            ],
        }
        for model in ("D=0", "D=3")
    },
}
(HERE / "analysis.json").write_text(json.dumps(ledger, indent=2) + "\n")
print(json.dumps(ledger, indent=2))
