#!/usr/bin/env python3
"""Mechanical verification for the lane-local C5 DISPLAY repair."""

from __future__ import annotations

import ast
import subprocess
import sys
from pathlib import Path


LANE = Path(__file__).resolve().parent
ROOT = Path(__file__).resolve().parents[4]
ORIGINAL = ROOT / "theory/checks/d24d3_normalization_check.py"
REPAIRED = LANE / "d24d3_normalization_check.py"
DATA = ROOT / "numerics/results/spin1-bc-falsifier.json"
BAND = 0.08
SPINS = (0.5, 1.0, 1.5, 2.0)
RED_MODES = (
    "--red-frozen",
    "--red-power",
    "--red-halfpower",
    "--red-ward",
    "--red-ladder",
    "--red-legfactor",
    "--red-descnorm",
)


def run_checker(checker: Path, *extra: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(checker), "--data", str(DATA), *extra],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )


def c5_require_count(source: str) -> int:
    tree = ast.parse(source)
    function = next(
        node for node in tree.body
        if isinstance(node, ast.FunctionDef) and node.name == "check_defect"
    )
    return sum(
        isinstance(node, ast.Call)
        and isinstance(node.func, ast.Name)
        and node.func.id == "require"
        for node in ast.walk(function)
    )


def main() -> None:
    original_source = ORIGINAL.read_text()
    repaired_source = REPAIRED.read_text()
    assert c5_require_count(original_source) == 2
    assert c5_require_count(repaired_source) == 0

    # Make the source audit red-capable with an in-memory mutant: put one
    # forbidden require back into C5 and verify that the audit rejects it.
    anchor = "    return max(deviations[1:]), deviations"
    assert repaired_source.count(anchor) == 1
    mutant_source = repaired_source.replace(
        anchor,
        "    require(True, 'MUTANT C5 no-op')\n" + anchor,
        1,
    )
    assert c5_require_count(mutant_source) == 1

    # C4 => the first old C5 predicate: at S=1/2 its prediction equals 1/S,
    # and averaging cannot increase the maximum row deviation.
    frozen_at_half = 2.0
    truth_at_half = 1.0 / SPINS[0]
    assert frozen_at_half == truth_at_half

    # C4 => every old off-half C5 predicate.  These are the sharp lower
    # bounds |2 - mean_S| S >= 2S - 1 - BAND.
    lower_bounds = {spin: 2.0 * spin - 1.0 - BAND for spin in SPINS[1:]}
    assert all(bound > BAND for bound in lower_bounds.values())

    original_green = run_checker(ORIGINAL)
    repaired_green = run_checker(REPAIRED)
    assert original_green.returncode == 0, original_green.stderr
    assert repaired_green.returncode == 0, repaired_green.stderr
    assert repaired_green.stdout == original_green.stdout
    assert repaired_green.stderr == original_green.stderr == ""

    # Existing red mutations prove the repaired checker still has real
    # failure paths; C5 itself is intentionally DISPLAY and has no red mode.
    repaired_red_runs = {}
    for red_mode in RED_MODES:
        original_red = run_checker(ORIGINAL, red_mode)
        repaired_red = run_checker(REPAIRED, red_mode)
        assert original_red.returncode == repaired_red.returncode == 1
        assert original_red.stdout == repaired_red.stdout
        assert original_red.stderr == repaired_red.stderr
        repaired_red_runs[red_mode] = repaired_red
    repaired_red = repaired_red_runs["--red-frozen"]
    assert repaired_red.stderr.startswith("FAIL: D24N-C6 "), repaired_red.stderr

    print("SOURCE AUDIT: original C5 require count=2; repaired count=0")
    print("MUTATION AUDIT: injected no-op require detected (count=1)")
    print(f"C4/C5 S=1/2 identity: frozen={frozen_at_half:.2f}, 1/S={truth_at_half:.2f}")
    print(
        "C4/C5 off-half lower bounds: "
        + ", ".join(f"S={spin:g}:{bound:.2f}" for spin, bound in lower_bounds.items())
        + f"; each exceeds band={BAND:.2f}"
    )
    print("GREEN REGRESSION: original and repaired stdout/stderr are byte-identical")
    print("RED REGRESSION: all seven original/repaired red paths are byte-identical")
    print(
        "RED CAPABILITY: --red-frozen exit=1, first stderr line="
        + repaired_red.stderr.splitlines()[0]
    )
    print("PASS: C5 is display-only and the rest of the checker is behavior-preserved")


if __name__ == "__main__":
    main()
