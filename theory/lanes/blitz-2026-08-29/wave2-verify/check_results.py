#!/usr/bin/env python3
"""Independent arithmetic/schema check for the two committed wave-2 JSONs.

Use --mutate to corrupt one recorded coefficient in memory.  The same checks
must then fail, demonstrating that this checker is red-capable.
"""

import argparse
import copy
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[4]
CONVERGENCE = ROOT / "numerics/results/lambdaD-kink-memory-convergence.json"
DISPERSION = ROOT / "numerics/results/lambdaD-kink-dispersion.json"


def close(a: float, b: float, tol: float = 1.0e-12) -> bool:
    return abs(a - b) <= tol * max(1.0, abs(a), abs(b))


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--mutate", action="store_true")
    args = parser.parse_args()

    convergence = json.loads(CONVERGENCE.read_text())
    dispersion = json.loads(DISPERSION.read_text())
    rows = copy.deepcopy(convergence["rows"])
    if args.mutate:
        rows[0]["coefficient_measured"] += 0.1
        print("MUTATION: first coefficient_measured += 0.1")

    assert convergence["stage"] == "converge"
    assert dispersion["stage"] == "dispersion"
    assert [row["chi"] for row in dispersion["rows"]] == [16, 24, 32]
    s_by_chi = {row["chi"]: row["s_tail_density"] for row in dispersion["rows"]}

    for row in dispersion["rows"]:
        ks = row["k"]
        omega = row["omega_kink"]
        assert len(ks) == len(omega) == 13
        assert all(value > 0.0 for value in omega)
        assert all(close(omega[i], omega[-i - 1], 1.0e-9) for i in range(len(omega)))
        assert close(row["gap_kink"], min(omega), 1.0e-12)
        assert close(row["bandwidth_kink"], max(omega) - min(omega), 1.0e-12)
        assert close(row["omega_at_pi_over_4"], omega[3], 1.0e-8)
        print(
            f"dispersion chi={row['chi']} s={row['s_tail_density']:.15f} "
            f"gap={row['gap_kink']:.15f} symmetry=PASS"
        )

    for index, row in enumerate(rows, 1):
        derived = -row["nu_mean_escaped_charge"] / row["dx_X2_centroid"]
        predicted = 2.0 * s_by_chi[row["chi"]]
        rel = abs(derived - predicted) / predicted
        assert close(derived, row["coefficient_measured"]), (
            index,
            derived,
            row["coefficient_measured"],
        )
        assert close(predicted, row["coefficient_predicted_2s"], 1.0e-9), (
            index,
            predicted,
            row["coefficient_predicted_2s"],
        )
        print(
            f"row={index} chi_max={row['chi_max']} "
            f"-nu/dx={derived:.15f} 2s={predicted:.15f} "
            f"relative_error={100.0 * rel:.9f}%"
        )

    ranks = [row["chi_max"] for row in rows]
    print(f"recorded_ranks={ranks}")
    print(f"expected_ranks=[32, 48, 64] complete={ranks == [32, 48, 64]}")
    assert ranks == sorted(set(ranks))
    print("CHECK: PASS")


if __name__ == "__main__":
    main()
