#!/usr/bin/env python3
"""Run the downgraded T0--T3 spin-1 lambda-D exact-diagonalization scan."""

from __future__ import annotations

import json
import time
from pathlib import Path

import numpy as np

from check_spt_dyn import (
    T0_HALDANE_MAX,
    T0_HALDANE_MIN,
    T0_TRIV_MAX,
    T1_HALDANE_MIN,
    T1_TRIV_MAX,
    T2_RELATIVE_TOL,
    T3_RATIO_MIN,
)
from spt_dyn_ed import (
    apply_raising,
    apply_sz,
    evolve,
    exclusive_channel,
    expectation_diagonal,
    gaussian_weights,
    ground_state,
    hamiltonian,
    hermiticity_residue,
    normalized,
    sector,
    sz2_profile,
    sz_profile,
)


HERE = Path(__file__).resolve().parent
STATIC_SIZES = (8, 10, 12)
T2_SIZES = (6, 8, 10, 12)
DYNAMIC_SIZE = 10
RIGHT_FIELD = 0.20
EDGE_WINDOW = 0.25


def complex_pair(value: complex) -> list[float]:
    return [float(value.real), float(value.imag)]


def edge_static(single_ion_D: float) -> tuple[dict, dict]:
    convergence = []
    max_hermiticity = 0.0
    final = None
    for length in STATIC_SIZES:
        sec0 = sector(length, 0)
        sec1 = sector(length, 1)
        h0 = hamiltonian(sec0, single_ion_D, right_field=RIGHT_FIELD)
        h1 = hamiltonian(sec1, single_ion_D, right_field=RIGHT_FIELD)
        max_hermiticity = max(max_hermiticity, hermiticity_residue(h0), hermiticity_residue(h1))
        e0, ga = ground_state(h0)
        e1, gb = ground_state(h1)

        left = np.zeros(length)
        left[: length // 2] = 1.0
        m_left_a = expectation_diagonal(sec0, ga, left)
        m_left_b = expectation_diagonal(sec1, gb, left)
        edge_gap = e1 - e0
        eligible = abs(edge_gap) < EDGE_WINDOW

        k_values = [0.0, 2 * np.pi / length, 4 * np.pi / length, 8 * np.pi / length]
        form_factors = []
        for momentum in k_values:
            weights = left.astype(complex) * np.exp(1j * momentum * np.arange(length))
            raised = apply_raising(sec0, sec1, ga, weights)
            form_factors.append(complex_pair(np.vdot(gb, raised)))
        raw_f0 = abs(complex(*form_factors[0]))
        projected_f0 = raw_f0 if eligible else 0.0
        entry = {
            "L": length,
            "dimensions": {"M=0": sec0.dim, "M=1": sec1.dim},
            "energies": {"M=0": e0, "M=1": e1, "edge_gap": edge_gap},
            "edge_partner_eligible": eligible,
            "m_left_a": m_left_a,
            "m_left_b": m_left_b,
            "edge_charge_difference": m_left_b - m_left_a,
            "momenta": k_values,
            "form_factors": form_factors,
            "raw_F0": raw_f0,
            "projected_F0": projected_f0,
            "ground_norm_error": abs(np.linalg.norm(ga) - 1.0),
            "edge_partner_norm_error": abs(np.linalg.norm(gb) - 1.0),
        }
        convergence.append(entry)
        final = entry
    assert final is not None
    model = {
        "T0": {"m_left": final["m_left_a"], "L": final["L"]},
        "T1": {
            "F0": final["projected_F0"],
            "raw_F0": final["raw_F0"],
            "edge_partner_eligible": final["edge_partner_eligible"],
            "edge_gap": final["energies"]["edge_gap"],
            "momenta": final["momenta"],
            "form_factors": final["form_factors"],
        },
        "static_convergence": convergence,
        "validation": {
            "ground_norm_error": final["ground_norm_error"],
            "edge_partner_norm_error": final["edge_partner_norm_error"],
        },
    }
    return model, {"hermiticity": max_hermiticity}


def bulk_t2(single_ion_D: float) -> tuple[dict, float]:
    rows = []
    max_hermiticity = 0.0
    for length in T2_SIZES:
        sec0 = sector(length, 0)
        matrix = hamiltonian(sec0, single_ion_D, periodic=True)
        max_hermiticity = max(max_hermiticity, hermiticity_residue(matrix))
        energy, ground = ground_state(matrix)
        momentum = 2.0 * np.pi / length
        weights = np.exp(1j * momentum * np.arange(length))
        charge_state, charge_norm = normalized(apply_sz(sec0, ground, weights))
        commutator_state = matrix @ apply_sz(sec0, ground, weights) - energy * apply_sz(
            sec0, ground, weights
        )
        form_factor = np.vdot(charge_state, commutator_state)
        quotient = form_factor / (np.exp(1j * momentum) - 1.0)
        coefficient = -float(quotient.imag)
        rows.append(
            {
                "L": length,
                "dimension": sec0.dim,
                "k": momentum,
                "ground_energy": energy,
                "charge_state_norm": charge_norm,
                "F": complex_pair(form_factor),
                "F_over_eik_minus_1": complex_pair(quotient),
                "soft_coefficient_minus_imag": coefficient,
            }
        )
    x = np.asarray([row["k"] ** 2 for row in rows])
    y = np.asarray([row["soft_coefficient_minus_imag"] for row in rows])
    intercept, slope = np.polynomial.polynomial.polyfit(x, y, 1)
    return {"points": rows, "k2_fit_intercept": float(intercept), "k2_fit_slope": float(slope)}, max_hermiticity


def local_channel_columns(length: int, source_sec, target_sec, source_state, kind: str) -> np.ndarray:
    columns = []
    for x in range(2, length - 2):
        weights = np.zeros(length, dtype=complex)
        weights[x] = 1.0
        if kind == "raise":
            column = apply_raising(source_sec, target_sec, source_state, weights)
        elif kind == "sz":
            column = apply_sz(source_sec, source_state, weights)
            column -= np.vdot(source_state, column) * source_state
        else:
            raise ValueError(kind)
        columns.append(column)
    return np.column_stack(columns)


def packet_center(
    sec, vector: np.ndarray, baseline_sz: np.ndarray, baseline_sz2: np.ndarray
) -> float:
    delta_sz = sz_profile(sec, vector) - baseline_sz
    delta_sz2 = sz2_profile(sec, vector) - baseline_sz2
    mass = np.abs(delta_sz) + np.abs(delta_sz2)
    return float(np.dot(np.arange(sec.length), mass) / np.sum(mass))


def dynamic_t3(single_ion_D: float) -> tuple[dict, float, float, float]:
    length = DYNAMIC_SIZE
    sec0 = sector(length, 0)
    sec1 = sector(length, 1)
    h0 = hamiltonian(sec0, single_ion_D, right_field=RIGHT_FIELD)
    h1 = hamiltonian(sec1, single_ion_D, right_field=RIGHT_FIELD)
    e0, ga = ground_state(h0)
    e1, gb = ground_state(h1)
    left = np.zeros(length)
    left[: length // 2] = 1.0
    m_a = expectation_diagonal(sec0, ga, left)
    m_b = expectation_diagonal(sec1, gb, left)
    edge_gap = e1 - e0
    eligible = abs(edge_gap) < EDGE_WINDOW

    primary = local_channel_columns(length, sec0, sec1, ga, "raise")
    candidate = local_channel_columns(length, sec1, sec1, gb, "sz")
    flip_basis = exclusive_channel(primary, candidate)
    baseline_sz = sz_profile(sec0, ga)
    baseline_sz2 = sz2_profile(sec0, ga)
    times = np.linspace(0.0, 12.0, 121)

    # Determine which phase convention sends the packet toward the left edge.
    trial = []
    for sign in (-1.0, 1.0):
        momentum = np.pi + sign * 0.60
        weights = gaussian_weights(length, 6.5, 1.35, momentum, support=(2, length - 2))
        initial, _ = normalized(apply_raising(sec0, sec1, ga, weights))
        short = evolve(h1, initial, np.asarray([0.0, 0.6]))
        velocity_proxy = packet_center(sec1, short[-1], baseline_sz, baseline_sz2) - packet_center(
            sec1, short[0], baseline_sz, baseline_sz2
        )
        trial.append((velocity_proxy, sign))
    incoming_sign = min(trial)[1]

    scans = []
    max_norm_drift = 0.0
    max_charge_residue = 0.0
    for offset in (0.45, 0.60, 0.75):
        momentum = np.pi + incoming_sign * offset
        weights = gaussian_weights(length, 6.5, 1.35, momentum, support=(2, length - 2))
        initial, source_norm = normalized(apply_raising(sec0, sec1, ga, weights))
        states = evolve(h1, initial, times)
        norms = np.linalg.norm(states, axis=1)
        max_norm_drift = max(max_norm_drift, float(np.max(np.abs(norms - 1.0))))
        profiles = np.asarray([sz_profile(sec1, state) for state in states])
        total_sz = profiles.sum(axis=1)
        max_charge_residue = max(max_charge_residue, float(np.max(np.abs(total_sz - 1.0))))
        centers = np.asarray(
            [packet_center(sec1, state, baseline_sz, baseline_sz2) for state in states]
        )
        edge_trace = profiles[:, : length // 2].sum(axis=1)
        flip_prob = np.sum(np.abs(states @ flip_basis.conj()) ** 2, axis=1)

        collision_i = int(np.argmin(centers[5:]) + 5)
        post_candidates = np.flatnonzero(
            (np.arange(len(times)) > collision_i)
            & (centers >= max(5.5, centers[collision_i] + 1.5))
        )
        post_i = int(post_candidates[0]) if len(post_candidates) else len(times) - 1
        post_separation_achieved = bool(len(post_candidates))
        pre_edge = float(edge_trace[0])
        post_edge = float(edge_trace[post_i])
        scans.append(
            {
                "k0": momentum,
                "source_norm_before_normalization": source_norm,
                "initial_center": float(centers[0]),
                "collision_time": float(times[collision_i]),
                "collision_center": float(centers[collision_i]),
                "post_time": float(times[post_i]),
                "post_center": float(centers[post_i]),
                "post_separation_achieved": post_separation_achieved,
                "reflection_turnaround": bool(centers[post_i] > centers[collision_i] + 1.0),
                "flip_probability_initial": float(flip_prob[0]),
                "flip_probability_post": float(flip_prob[post_i]),
                "flip_amplitude_post": float(np.sqrt(max(0.0, flip_prob[post_i]))),
                "edge_memory_unconditioned": post_edge - pre_edge,
                "norm_drift": float(np.max(np.abs(norms - 1.0))),
                "charge_sector_residue": float(np.max(np.abs(total_sz - 1.0))),
                "center_trace": centers.tolist(),
                "edge_trace": edge_trace.tolist(),
                "flip_probability_trace": flip_prob.tolist(),
            }
        )

    central = scans[1]
    raw_memory = abs(central["edge_memory_unconditioned"])
    effective_memory = raw_memory if eligible else 0.0
    result = {
        "L": length,
        "sigma": 1.35,
        "center": 6.5,
        "right_field": RIGHT_FIELD,
        "edge_gap": edge_gap,
        "edge_partner_eligible": eligible,
        "edge_charge_a": m_a,
        "edge_charge_b": m_b,
        "postselected_edge_change": m_b - m_a,
        "postselected_bulk_change": -1.0,
        "postselected_charge_budget_defect": abs((m_b - m_a) - 1.0),
        "exclusive_flip_basis_dimension": int(flip_basis.shape[1]),
        "incoming_sign": incoming_sign,
        "orientation_trials": [{"center_drift": x, "sign": sign} for x, sign in trial],
        "momentum_scan": scans,
        "central_flip_amplitude": central["flip_amplitude_post"] if eligible else 0.0,
        "central_flip_amplitude_raw": central["flip_amplitude_post"],
        "memory_signal": effective_memory,
        "memory_signal_raw": raw_memory,
    }
    return result, max(hermiticity_residue(h0), hermiticity_residue(h1)), max_norm_drift, max_charge_residue


def main() -> None:
    started = time.time()
    models = {}
    validation = {"max_hermiticity_residue": 0.0, "max_norm_drift": 0.0, "max_charge_sector_residue": 0.0}

    for label, single_ion_D in (("D=0", 0.0), ("D=3", 3.0)):
        print(f"static {label}", flush=True)
        models[label], static_validation = edge_static(single_ion_D)
        validation["max_hermiticity_residue"] = max(
            validation["max_hermiticity_residue"], static_validation["hermiticity"]
        )

    t2_models = {}
    for label, single_ion_D in (("D=0", 0.0), ("D=3", 3.0)):
        print(f"T2 periodic {label}", flush=True)
        t2_models[label], residue = bulk_t2(single_ion_D)
        validation["max_hermiticity_residue"] = max(validation["max_hermiticity_residue"], residue)
    intercept0 = t2_models["D=0"]["k2_fit_intercept"]
    intercept3 = t2_models["D=3"]["k2_fit_intercept"]
    relative = abs(intercept0 - intercept3) / max(abs(0.5 * (intercept0 + intercept3)), 1.0e-14)
    t2 = {"models": t2_models, "relative_intercept_difference": relative}

    dynamic = {}
    for label, single_ion_D in (("D=0", 0.0), ("D=3", 3.0)):
        print(f"T3 dynamics {label}", flush=True)
        dynamic[label], herm, norm, charge = dynamic_t3(single_ion_D)
        validation["max_hermiticity_residue"] = max(validation["max_hermiticity_residue"], herm)
        validation["max_norm_drift"] = max(validation["max_norm_drift"], norm)
        validation["max_charge_sector_residue"] = max(validation["max_charge_sector_residue"], charge)
    memory0 = dynamic["D=0"]["memory_signal"]
    memory3 = dynamic["D=3"]["memory_signal_raw"]
    ratio = memory0 / max(memory3, 1.0e-14)
    t3 = {
        "models": dynamic,
        "flip_amplitude_D0": dynamic["D=0"]["central_flip_amplitude"],
        "flip_amplitude_D3": dynamic["D=3"]["central_flip_amplitude"],
        "memory_D0": memory0,
        "memory_D3_raw": memory3,
        "memory_ratio_D0_over_D3": ratio,
    }

    d0 = models["D=0"]
    d3 = models["D=3"]
    gates = {
        "T0": T0_HALDANE_MIN <= abs(d0["T0"]["m_left"]) <= T0_HALDANE_MAX
        and abs(d3["T0"]["m_left"]) < T0_TRIV_MAX,
        "T1": abs(d0["T1"]["F0"]) > T1_HALDANE_MIN and abs(d3["T1"]["F0"]) < T1_TRIV_MAX,
        "T2": relative < T2_RELATIVE_TOL,
        "T3": ratio > T3_RATIO_MIN,
    }
    output = {
        "schema": "spt-dyn-ed-v1",
        "model": "spin-1 H(D)=sum S.S + D sum (Sz)^2",
        "scope_fence": "D=0 is Heisenberg-Haldane, not the exact D23 AKLT parent",
        "downgrade": {
            "requested_sizes": [32, 48, 64],
            "actual_sizes": sorted(set(STATIC_SIZES + T2_SIZES + (DYNAMIC_SIZE,))),
            "reason": "charge-sector ED used because a verified TDVP/DMRG setup at requested sizes did not fit the blitz wall clock",
            "dynamic_packet_width_requested": 10.0,
            "dynamic_packet_width_actual": 1.35,
        },
        "pre_registered_tolerances": {
            "T0_Haldane_interval": [T0_HALDANE_MIN, T0_HALDANE_MAX],
            "T0_trivial_max": T0_TRIV_MAX,
            "T1_Haldane_min": T1_HALDANE_MIN,
            "T1_trivial_max": T1_TRIV_MAX,
            "T2_relative_intercept": T2_RELATIVE_TOL,
            "T3_ratio": T3_RATIO_MIN,
            "edge_partner_energy_window": EDGE_WINDOW,
        },
        "models": models,
        "T2": t2,
        "T3": t3,
        "scientific_gates": gates,
        "validation": validation,
        "wall_seconds": time.time() - started,
    }
    (HERE / "results.json").write_text(json.dumps(output, indent=2) + "\n")
    print(json.dumps({"scientific_gates": gates, "validation": validation, "wall_seconds": output["wall_seconds"]}, indent=2))


if __name__ == "__main__":
    main()
