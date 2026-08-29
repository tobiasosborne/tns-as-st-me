#!/usr/bin/env python3
"""Red-capable finite certificate for theory/soft-index-r2.md.

Green:
    python3 -O theory/checks/soft_index_r2_check.py

Each registered red flag mutates one load-bearing finite identity and must
exit 1.  Red modes are mutually exclusive.  This checker deliberately does
not test D29 limit-point existence, D30 on a model, PROTO-LSZ, MATCH-S,
microscopic D24 membership, or the value of a_leg.
"""

from __future__ import annotations

import ast
import importlib.util
import math
from pathlib import Path
import subprocess
import sys

import numpy as np


ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
TOL = 2.0e-10
RED_MODES = {
    "--red-register-trap",
    "--red-ward-residue",
    "--red-adler-anchor",
    "--red-s2-value",
    "--red-lsz-factor",
    "--red-tgt-value",
    "--red-leg-power",
    "--red-limit-order",
}


def fail(message: str) -> None:
    print(f"FAIL: {message}", file=sys.stderr)
    raise SystemExit(1)


def require(condition: bool, message: str) -> None:
    if not condition:
        fail(message)


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    require(spec is not None and spec.loader is not None,
            f"cannot load module {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def code_shape_gate() -> None:
    source = Path(__file__).read_text(encoding="utf-8")
    tree = ast.parse(source)
    bare = [node for node in ast.walk(tree) if isinstance(node, ast.Assert)]
    require(not bare, "SIDXR2-C0 bare assert found")
    print("SIDXR2-C0 PASS: optimization-safe require/fail checks; no bare assert")


def run_process(arguments: list[str]) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        arguments,
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=False,
    )


def register_trap_gate(red: bool) -> None:
    certificate = HERE / "ml4_ward_n2_check.py"
    green = run_process([sys.executable, "-O", str(certificate)])
    require(green.returncode == 0,
            "SIDXR2-C1 standing ML4 certificate failed green:\n" + green.stdout)
    if red:
        # R2-O1 repair: the public red path executes the real standing
        # mutation and propagates its outcome. Exit 1 exactly when the
        # mutation is detected (child exit 1, trap coincidence forwarded);
        # return normally when it survives undetected, so main reports
        # RED SURVIVED UNDETECTED and exits 0.
        result = run_process(
            [sys.executable, "-O", str(certificate), "--red-register"])
        print(result.stdout, end="")
        if result.returncode == 1:
            fail("SIDXR2-C1 RED detected: standing --red-register mutation "
                 "fired; trap coincidence forwarded above")
        return
    required_reds = ("--red", "--red-register", "--red-chi")
    red_codes = {}
    for flag in required_reds:
        result = run_process([sys.executable, "-O", str(certificate), flag])
        red_codes[flag] = result.returncode
        require(result.returncode == 1,
                f"SIDXR2-C1 standing mutation {flag} did not exit 1:\n"
                + result.stdout)
    print("SIDXR2-C1 PASS: full/hw registers exact; scalar n>=2 and old (18) "
          f"rejected; standing reds {red_codes}")


def kron_at(operator: np.ndarray, site: int, number_sites: int,
            local_dimension: int) -> np.ndarray:
    result = np.array([[1.0 + 0.0j]])
    for position in range(number_sites):
        factor = operator if position == site else np.eye(local_dimension)
        result = np.kron(result, factor)
    return result


_SPIN_CACHE: dict[tuple[int, int], dict[str, object]] = {}


def spin_ring(two_s: int, number_sites: int = 4) -> dict[str, object]:
    key = (two_s, number_sites)
    if key in _SPIN_CACHE:
        return _SPIN_CACHE[key]
    site_spin = two_s / 2.0
    local_dimension = two_s + 1
    raising = np.zeros((local_dimension, local_dimension), dtype=complex)
    for occupation in range(1, local_dimension):
        raising[occupation - 1, occupation] = math.sqrt(
            occupation * (two_s - occupation + 1)
        )
    lowering = raising.T.conj()
    z_spin = np.diag(
        [site_spin - occupation for occupation in range(local_dimension)]
    ).astype(complex)
    x_spin = (raising + lowering) / 2.0
    y_spin = (raising - lowering) / (2.0j)
    dimension = local_dimension ** number_sites
    identity = np.eye(dimension, dtype=complex)
    site_lowerings = [
        kron_at(lowering, site, number_sites, local_dimension)
        for site in range(number_sites)
    ]
    total_raising = sum(
        kron_at(raising, site, number_sites, local_dimension)
        for site in range(number_sites)
    )
    total_lowering = total_raising.T.conj()
    total_z = sum(
        kron_at(z_spin, site, number_sites, local_dimension)
        for site in range(number_sites)
    )
    hamiltonian = np.zeros((dimension, dimension), dtype=complex)
    current_lowering = np.zeros_like(hamiltonian)
    current_z = np.zeros_like(hamiltonian)
    for site in range(number_sites):
        neighbour = (site + 1) % number_sites
        bond = -(
            kron_at(x_spin, site, number_sites, local_dimension)
            @ kron_at(x_spin, neighbour, number_sites, local_dimension)
            + kron_at(y_spin, site, number_sites, local_dimension)
            @ kron_at(y_spin, neighbour, number_sites, local_dimension)
            + kron_at(z_spin, site, number_sites, local_dimension)
            @ kron_at(z_spin, neighbour, number_sites, local_dimension)
            - site_spin * site_spin * identity
        )
        hamiltonian += bond
        local_lowering = site_lowerings[site]
        local_z = kron_at(z_spin, site, number_sites, local_dimension)
        current_lowering -= bond @ local_lowering - local_lowering @ bond
        current_z -= bond @ local_z - local_z @ bond
    vacuum = np.zeros(dimension, dtype=complex)
    vacuum[0] = 1.0
    one_site = [operator @ vacuum / math.sqrt(two_s)
                for operator in site_lowerings]
    data: dict[str, object] = {
        "S": site_spin,
        "N": number_sites,
        "H": hamiltonian,
        "Sp": total_raising,
        "Sm": total_lowering,
        "Sz": total_z,
        "Jm": current_lowering,
        "Jz": current_z,
        "Smx": site_lowerings,
        "vac": vacuum,
        "one_site": one_site,
    }
    _SPIN_CACHE[key] = data
    return data


def one_magnon(data: dict[str, object], momentum: float) -> np.ndarray:
    number_sites = int(data["N"])
    one_site = data["one_site"]
    return sum(
        np.exp(1.0j * momentum * site) * one_site[site]
        for site in range(number_sites)
    ) / math.sqrt(number_sites)


def sector_indices(data: dict[str, object], lowering_number: int) -> np.ndarray:
    number_sites = int(data["N"])
    site_spin = float(data["S"])
    total_z = data["Sz"]
    diagonal = np.rint(number_sites * site_spin - np.diag(total_z).real).astype(int)
    return np.where(diagonal == lowering_number)[0]


def ward_spin_gate(red: bool) -> None:
    maxima = {"comm": 0.0, "projection": 0.0, "velocity": 0.0,
              "norm": 0.0, "residue": 0.0}
    for two_s in (1, 2, 3):
        data = spin_ring(two_s)
        number_sites = int(data["N"])
        site_spin = float(data["S"])
        momentum = math.pi / 2.0
        hard = one_magnon(data, momentum)
        velocity = 2.0 * site_spin * math.sin(momentum)
        commutator = (data["Sp"] @ data["Jm"]
                      - data["Jm"] @ data["Sp"] - 2.0 * data["Jz"])
        maxima["comm"] = max(maxima["comm"], float(np.linalg.norm(commutator)))
        index_one = sector_indices(data, 1)
        index_two = sector_indices(data, 2)
        descendant_map = data["Sm"][np.ix_(index_two, index_one)]
        gram = descendant_map.conj().T @ descendant_map
        projection = descendant_map @ np.linalg.solve(
            gram, descendant_map.conj().T
        )
        lhs = projection @ (data["Jm"] @ hard)[index_two]
        z_hard = (data["Jz"] @ hard)[index_one]
        corrected = 2.0 * descendant_map @ np.linalg.solve(gram, z_hard)
        maxima["projection"] = max(
            maxima["projection"], float(np.linalg.norm(lhs - corrected))
        )
        maxima["velocity"] = max(
            maxima["velocity"],
            float(np.linalg.norm(data["Jz"] @ hard - 1.0j * velocity * hard)),
        )
        descendant = (data["Sm"] @ hard)[index_two]
        expected_norm = 2.0 * (number_sites * site_spin - 1.0)
        maxima["norm"] = max(
            maxima["norm"], abs(float(np.vdot(descendant, descendant).real)
                                 - expected_norm),
        )
        measured_residue = np.vdot(descendant, lhs)
        expected_residue = (1.0j if red else 2.0j) * velocity
        maxima["residue"] = max(
            maxima["residue"], abs(measured_residue - expected_residue)
        )
    require(maxima["comm"] < 2.0e-11,
            f"SIDXR2-C2 current commutator error {maxima['comm']:.3e}")
    require(maxima["projection"] < TOL,
            f"SIDXR2-C2 full projection error {maxima['projection']:.3e}")
    require(maxima["velocity"] < TOL,
            f"SIDXR2-C2 velocity error {maxima['velocity']:.3e}")
    require(maxima["norm"] < TOL,
            f"SIDXR2-C2 descendant norm error {maxima['norm']:.3e}")
    require(maxima["residue"] < TOL,
            f"SIDXR2-C2 Ward residue error {maxima['residue']:.3e}")
    print("SIDXR2-C2 PASS:", " ".join(f"{k}={v:.2e}" for k, v in maxima.items()))


def weighted_lowering(data: dict[str, object], momentum: float) -> np.ndarray:
    return sum(
        np.exp(1.0j * momentum * site) * operator
        for site, operator in enumerate(data["Smx"])
    )


def adler_anchor_gate(red: bool) -> None:
    data = spin_ring(2)
    hard_momentum = math.pi / 2.0
    soft_momentum = math.pi / 2.0 if red else 0.0
    hard = one_magnon(data, hard_momentum)
    created = weighted_lowering(data, soft_momentum) @ hard
    time = 0.73
    eigenvalues, eigenvectors = np.linalg.eigh(data["H"])
    interacting = eigenvectors @ (
        np.exp(-1.0j * eigenvalues * time)
        * (eigenvectors.conj().T @ created)
    )
    site_spin = float(data["S"])
    dispersion = lambda k: 2.0 * site_spin * (1.0 - math.cos(k))
    free = np.exp(
        -1.0j * (dispersion(soft_momentum) + dispersion(hard_momentum)) * time
    ) * created
    ratio = np.vdot(free, interacting) / np.vdot(free, free)
    require(abs(ratio - 1.0) < TOL,
            f"SIDXR2-C3 pure-Q0 anchor ratio {ratio} is not one")
    if not red:
        nonzero_created = weighted_lowering(data, math.pi / 2.0) @ hard
        nonzero_free = np.exp(
            -1.0j * (dispersion(math.pi / 2.0)
                     + dispersion(hard_momentum)) * time
        ) * nonzero_created
        nonzero_interacting = eigenvectors @ (
            np.exp(-1.0j * eigenvalues * time)
            * (eigenvectors.conj().T @ nonzero_created)
        )
        negative = np.vdot(nonzero_free, nonzero_interacting) / np.vdot(
            nonzero_free, nonzero_free
        )
        require(abs(negative - 1.0) > 0.1,
                "SIDXR2-C3 nonzero-Q mutation did not produce a defect")
        print(f"SIDXR2-C3 PASS: Q0 ratio error={abs(ratio-1):.2e}; "
              f"Qk negative-control defect={abs(negative-1):.3f}")


def s2_packet_gate(red: bool) -> None:
    spin_checker = load_module(
        "spin_s_slope_r2", HERE / "spin_s_slope_check.py"
    )
    profile = np.asarray((0.2, 0.5, 0.8))
    weights = np.asarray((0.2, 0.5, 0.3))
    weights /= weights.sum()
    epsilon = 1.0e-5
    hard = 1.1
    maximum = 0.0
    for two_s in (1, 2, 3, 4):
        multiplier = sum(
            weight * spin_checker.physical_scattering(
                epsilon * u, hard, two_s
            )
            for weight, u in zip(weights, profile)
        )
        mean_momentum = epsilon * float(np.dot(weights, profile))
        measured = float(np.angle(multiplier) / mean_momentum)
        expected = 1.0 / (two_s / 2.0 + 1.0) if red else 2.0 / two_s
        maximum = max(maximum, abs(measured - expected))
    require(maximum < 2.0e-5,
            f"SIDXR2-C4 packet phase-slope error {maximum:.3e}")
    print(f"SIDXR2-C4 PASS: max packet slope error={maximum:.3e}")


def lsz_factor_gate(red: bool) -> None:
    profile = np.asarray((0.2, 0.5, 0.8))
    weights = np.asarray((0.2, 0.5, 0.3))
    weights /= weights.sum()
    epsilon = 1.0e-6
    momenta = epsilon * profile
    mean_momentum = float(np.dot(weights, momenta))
    a_leg = 0.4
    ell_h = 1.3
    velocity = 0.7
    channel_sign = 1.0
    flux = a_leg * (-1.0j * channel_sign / velocity)
    ward_factor = (1.0j if red else 2.0j) * velocity * ell_h
    datum = sum(
        weight * (np.exp(1.0j * momentum) - 1.0) * flux * ward_factor
        for weight, momentum in zip(weights, momenta)
    )
    coefficient = datum / mean_momentum
    expected = 2.0j * a_leg * channel_sign * ell_h
    phase_jet = float(np.angle(1.0 + datum) / mean_momentum)
    expected_phase = 2.0 * a_leg * channel_sign * ell_h
    require(abs(coefficient - expected) < 2.0e-6,
            f"SIDXR2-C5 LSZ coefficient error {abs(coefficient-expected):.3e}")
    require(abs(phase_jet - expected_phase) < 2.0e-6,
            f"SIDXR2-C5 phase-jet error {abs(phase_jet-expected_phase):.3e}")
    print(f"SIDXR2-C5 PASS: coefficient error={abs(coefficient-expected):.2e} "
          f"phase error={abs(phase_jet-expected_phase):.2e}")


def tgt_mobius_gate(red: bool) -> None:
    epsilon = 1.0e-7
    base_linear = 0.2 + 0.3j
    curvature = -0.1 + 0.05j
    arbitrary_shift = 1.7
    datum = base_linear * epsilon + curvature * epsilon * epsilon
    transformed = (1.0 + datum) * np.exp(1.0j * arbitrary_shift * epsilon) - 1.0
    before = float(np.angle(1.0 + datum) / epsilon)
    after = float(np.angle(1.0 + transformed) / epsilon)
    measured_shift = after - before
    expected_shift = 0.0 if red else arbitrary_shift
    require(abs(measured_shift - expected_shift) < 2.0e-7,
            f"SIDXR2-C6 TGT phase shift {measured_shift:.9f} vs "
            f"{expected_shift:.9f}")
    print(f"SIDXR2-C6 PASS: arbitrary regular phase shift={measured_shift:.9f}")


def leg_normalisation_gate(red: bool) -> None:
    probe = load_module("soft_index_probe_r2", HERE / "soft_index_probe.py")
    number_sites = 8
    hard_momentum = 2.0 * math.pi * 2 / number_sites
    soft_momentum = 2.0 * math.pi / number_sites
    maximum_vacuum = 0.0
    maximum_descendant = 0.0
    wrong_full_power_error = 0.0
    for two_s in (1, 2, 3, 4):
        weights = np.exp(1.0j * soft_momentum * np.arange(number_sites))
        vacuum_map = probe.lowering_matrix(number_sites, 0, two_s, weights)
        vacuum_leg = vacuum_map[:, 0]
        measured_vacuum = float(np.vdot(vacuum_leg, vacuum_leg).real)
        maximum_vacuum = max(
            maximum_vacuum, abs(measured_vacuum - two_s * number_sites)
        )
        hard = np.exp(
            1.0j * hard_momentum * np.arange(number_sites)
        ) / math.sqrt(number_sites)
        descendant_map = probe.lowering_matrix(
            number_sites, 1, two_s, weights
        )
        descendant_leg = descendant_map @ hard
        measured_descendant = float(np.vdot(descendant_leg, descendant_leg).real)
        maximum_descendant = max(
            maximum_descendant,
            abs(measured_descendant - (two_s * number_sites - 2.0)),
        )
        measured_ratio = math.sqrt(measured_descendant / number_sites)
        wrong_full_power_error = max(
            wrong_full_power_error, abs(measured_ratio - two_s)
        )
    require(maximum_vacuum < TOL,
            f"SIDXR2-C7 vacuum leg norm error {maximum_vacuum:.3e}")
    require(maximum_descendant < TOL,
            f"SIDXR2-C7 descendant leg norm error {maximum_descendant:.3e}")
    if red:
        require(wrong_full_power_error < TOL,
                "SIDXR2-C7 full-power mutation detected: measured leg ratio "
                "is a square root, not Z_rho")
    else:
        require(wrong_full_power_error > 0.2,
                "SIDXR2-C7 full-power negative control too weak")
    print(f"SIDXR2-C7 PASS: vacuum={maximum_vacuum:.2e} "
          f"descendant={maximum_descendant:.2e} "
          f"full-power defect={wrong_full_power_error:.3f}")


def sample_set(number_sites: int, epsilon: float,
               c_one: float, c_two: float) -> list[float]:
    return [
        2.0 * math.pi * index / number_sites
        for index in range(1, number_sites)
        if c_one * epsilon < 2.0 * math.pi * index / number_sites
        < c_two * epsilon
    ]


def limit_order_gate(red: bool) -> None:
    number_sites = 32
    c_one, c_two = 0.2, 0.8
    forbidden_epsilon = 0.5 * 2.0 * math.pi / (c_two * number_sites)
    forbidden = sample_set(number_sites, forbidden_epsilon, c_one, c_two)
    if red:
        require(len(forbidden) > 0,
                "SIDXR2-C8 fixed-N soft-sample mutation detected: set is empty")
    else:
        require(len(forbidden) == 0,
                "SIDXR2-C8 forbidden fixed-N sample unexpectedly nonempty")
    admissible_epsilon = 1.1 * 2.0 * math.pi / (
        number_sites * (c_two - c_one)
    )
    admissible = sample_set(number_sites, admissible_epsilon, c_one, c_two)
    require(len(admissible) > 0,
            "SIDXR2-C8 interval longer than grid spacing is empty")
    print(f"SIDXR2-C8 PASS: forbidden rows={len(forbidden)} "
          f"admissible rows={len(admissible)}")


def main() -> None:
    arguments = sys.argv[1:]
    require(len(arguments) <= 1, "red modes are mutually exclusive")
    mode = arguments[0] if arguments else None
    require(mode is None or mode in RED_MODES, f"unknown mode: {mode}")
    code_shape_gate()
    gates = {
        "--red-register-trap": register_trap_gate,
        "--red-ward-residue": ward_spin_gate,
        "--red-adler-anchor": adler_anchor_gate,
        "--red-s2-value": s2_packet_gate,
        "--red-lsz-factor": lsz_factor_gate,
        "--red-tgt-value": tgt_mobius_gate,
        "--red-leg-power": leg_normalisation_gate,
        "--red-limit-order": limit_order_gate,
    }
    if mode is not None:
        gates[mode](True)
        print(f"RED SURVIVED UNDETECTED: {mode}")
        raise SystemExit(0)
    register_trap_gate(False)
    ward_spin_gate(False)
    adler_anchor_gate(False)
    s2_packet_gate(False)
    lsz_factor_gate(False)
    tgt_mobius_gate(False)
    leg_normalisation_gate(False)
    limit_order_gate(False)
    print("ALL SIDXR2 GATES PASS")


if __name__ == "__main__":
    main()
