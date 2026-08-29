#!/usr/bin/env python3
"""Finite checks for theory/proto-lsz-match.md.

These gates corroborate the finite charge map, separated-packet collision
decay, normalized readout, D7 multiplier orientation, and the frozen
P1+P2(a)-only probe evidence.  They do not test wave-operator existence,
Cook convergence, (PROTO-LSZ), or a D24 class member.
"""

from __future__ import annotations

import importlib.util
import json
import math
import sys
from pathlib import Path

import numpy as np


sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
PROBE_PATH = HERE / "soft_index_probe.py"
PROBE_RESULTS = HERE / "soft_index_probe_results.json"
RED_FLAGS = {
    "--red-charge-map",
    "--red-separation",
    "--red-readout",
    "--red-channel",
    "--red-probe",
}


def fail(message: str) -> None:
    print(f"FAIL: {message}")
    raise SystemExit(1)


def require(condition: bool, message: str) -> None:
    if not condition:
        fail(message)


def load_probe_module():
    spec = importlib.util.spec_from_file_location("frozen_soft_index_probe",
                                                  PROBE_PATH)
    require(spec is not None and spec.loader is not None,
            "PMLM-C0 cannot load frozen probe")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def charge_map_gate(probe, red: bool) -> dict:
    """PMLM-C1: Q[f]Q[g]/(2S) in the normalized occupation basis."""
    n = 11
    xs = np.arange(n, dtype=float)
    f = np.exp(-((xs - 2.2) / 2.0) ** 2) * np.exp(0.17j * xs)
    g = np.exp(-((xs - 7.1) / 2.3) ** 2) * np.exp(0.83j * xs)
    f = f / np.linalg.norm(f)
    g = g / np.linalg.norm(g)
    errors = []
    for two_s in (1, 2, 3, 4):
        qf = probe.lowering_matrix(n, 1, two_s, f)
        actual = (qf @ g) / math.sqrt(two_s)
        predicted = []
        for x, y in probe.sector_basis(n, 2, two_s):
            if x != y:
                predicted.append(f[x] * g[y] + f[y] * g[x])
            else:
                coefficient = math.sqrt(2.0 * (two_s - 1) / two_s)
                if red:
                    coefficient = math.sqrt(2.0)
                predicted.append(coefficient * f[x] * g[x])
        errors.append(float(np.max(np.abs(actual - np.asarray(predicted)))))
    return {"max_error": max(errors), "violated": max(errors) > 2e-13}


def smooth_bump(momentum: np.ndarray, center: float,
                width: float) -> np.ndarray:
    distance = (momentum - center + np.pi) % (2.0 * np.pi) - np.pi
    scaled = distance / width
    values = np.zeros_like(momentum, dtype=complex)
    mask = np.abs(scaled) < 1.0
    values[mask] = np.exp(-1.0 / (1.0 - scaled[mask] ** 2))
    return values


def collision_norm(f_k: np.ndarray, g_k: np.ndarray) -> float:
    f_x = np.fft.ifft(f_k, norm="ortho")
    g_x = np.fft.ifft(g_k, norm="ortho")
    return float(np.linalg.norm(f_x * g_x))


def separation_gate(red: bool) -> dict:
    """PMLM-C2: an allowed relative translation kills the collision row."""
    n = 8192
    momenta = 2.0 * np.pi * np.fft.fftfreq(n)
    f_k = smooth_bump(momenta, 0.25, 0.12)
    g_k = smooth_bump(momenta, 1.25, 0.18)
    f_k = f_k / np.linalg.norm(f_k)
    g_k = g_k / np.linalg.norm(g_k)
    baseline = collision_norm(f_k, g_k)
    separation = 160.0
    phase = np.ones(n, dtype=complex) if red else np.exp(-1j * momenta * separation)
    separated = collision_norm(f_k, g_k * phase)

    # The same packets after a time long enough to cross and separate again.
    velocity_gap = 2.0 * (math.sin(1.25) - math.sin(0.25))
    time = 2.0 * separation / velocity_gap
    omega = 2.0 * (1.0 - np.cos(momenta))
    evolved_f = f_k * np.exp(-1j * omega * time)
    evolved_g = g_k * phase * np.exp(-1j * omega * time)
    outgoing = collision_norm(evolved_f, evolved_g)
    ratio = separated / baseline
    violated = ratio >= 0.02 or outgoing >= 0.01
    return {"baseline": baseline, "separated": separated,
            "outgoing": outgoing, "ratio": ratio, "violated": violated}


def readout_gate(red: bool) -> dict:
    """PMLM-C3: complex normalized-pairing identity and error bound."""
    rng = np.random.default_rng(290829)
    packet = rng.normal(size=13) + 1j * rng.normal(size=13)
    packet = packet / np.linalg.norm(packet)
    energy_phase = np.exp(-1j * np.linspace(0.13, 2.17, packet.size))
    translation_phase = np.exp(1j * np.linspace(-1.1, 0.7, packet.size))
    multiplier = np.exp(1j * np.linspace(0.03, 0.41, packet.size))
    free = energy_phase * translation_phase * packet
    ideal = energy_phase * translation_phase * multiplier * packet
    error = 2e-3 * (rng.normal(size=13) + 1j * rng.normal(size=13))
    denominator = float(np.vdot(free, free).real)
    actual = ideal + error
    if red:
        observed = np.dot(free, actual) / denominator
    else:
        observed = np.vdot(free, actual) / denominator
    expected_ideal = np.sum(np.abs(packet) ** 2 * multiplier)
    expected_delta = np.vdot(free, error) / denominator
    identity_error = abs(observed - expected_ideal - expected_delta)
    bound_slack = abs(observed - expected_ideal) - np.linalg.norm(error) / math.sqrt(denominator)
    violated = identity_error > 2e-13 or bound_slack > 2e-13
    return {"identity_error": float(identity_error),
            "bound_slack": float(bound_slack), "violated": violated}


def exact_s12(site_spin: float, soft: float, hard: float) -> complex:
    z_1 = np.exp(1j * soft)
    z_2 = np.exp(1j * hard)
    a = 1.0 + z_1 * z_2
    b = z_1 + z_2
    mu = (2.0 * site_spin - 1.0) * a + b
    return complex((site_spin * a * b - z_1 * mu)
                   / (z_2 * mu - site_spin * a * b))


def channel_gate(red: bool) -> dict:
    """PMLM-C4: physical multiplier orientation and S2 packet arithmetic."""
    hard = 1.2
    epsilon = 1e-5
    scaled_soft = np.asarray([0.6, 0.9, 1.3])
    weights = np.asarray([0.2, 0.5, 0.3])
    mean_soft = epsilon * float(np.dot(weights, scaled_soft))
    errors = []
    unity_errors = []
    for site_spin in (0.5, 1.0, 1.5, 2.0):
        multiplier = np.asarray([
            exact_s12(site_spin, epsilon * u, hard)
            for u in scaled_soft
        ])
        unity_errors.append(float(np.max(np.abs(np.abs(multiplier) - 1.0))))
        if red:
            multiplier = 1.0 / multiplier
        connected = np.dot(weights, multiplier - 1.0)
        measured = connected / (1j * mean_soft)
        errors.append(abs(measured - 1.0 / site_spin))
    violated = max(errors) > 5e-5 or max(unity_errors) > 2e-13
    return {"max_jet_error": float(max(errors)),
            "max_unitarity_error": max(unity_errors), "violated": violated}


def frozen_probe_gate(red: bool) -> dict:
    """PMLM-C5: consume only frozen P1 and P2(a) result fields."""
    data = json.loads(PROBE_RESULTS.read_text())
    p1_errors = []
    p1_signs = []
    for two_s in (1, 2):
        row = data[f"p1_two_s_{two_s}"]
        site_spin = two_s / 2.0
        target = 1.0 / site_spin
        if red:
            target = 1.0 / (site_spin + 1.0)
        p1_errors.append(abs(abs(float(row["slope"])) - target) / target)
        p1_signs.append(float(row["sign"]))

    # Deliberately read only P2(a)'s source-jet errors.  The P2(b) fields in
    # this JSON are outside this gate because that frozen code path is a no-op.
    p2a_errors = [float(value) for value in data["p2"]["jet_errors"]]
    if red:
        p2a_errors[0] += 0.2
    violated = (max(p1_errors) > 0.05 or len(set(p1_signs)) != 1
                or max(p2a_errors) > 0.08)
    return {"p1_errors": p1_errors, "p1_signs": p1_signs,
            "p2a_errors": p2a_errors, "violated": violated}


def main() -> None:
    args = sys.argv[1:]
    require(len(args) <= 1, "combined flags are not allowed")
    require(not args or args[0] in RED_FLAGS,
            f"unknown flag: {args[0] if args else ''}")
    red_flag = args[0] if args else None
    probe = load_probe_module()

    gates = {
        "PMLM-C1": charge_map_gate(probe, red_flag == "--red-charge-map"),
        "PMLM-C2": separation_gate(red_flag == "--red-separation"),
        "PMLM-C3": readout_gate(red_flag == "--red-readout"),
        "PMLM-C4": channel_gate(red_flag == "--red-channel"),
        "PMLM-C5": frozen_probe_gate(red_flag == "--red-probe"),
    }
    violated = [name for name, row in gates.items() if row["violated"]]
    for name, row in gates.items():
        metrics = {key: value for key, value in row.items() if key != "violated"}
        print(name, json.dumps(metrics, sort_keys=True))

    if red_flag is None:
        require(not violated, f"green violations: {violated}")
        print("PMLM PASS")
        return

    if violated:
        fail(f"RED DETECTED {red_flag}: {violated}")
    print(f"RED SURVIVED UNDETECTED {red_flag}")


if __name__ == "__main__":
    main()
