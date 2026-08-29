#!/usr/bin/env python3
"""Red-capable finite-Fock checker for the fcs blitz lane.

Green checks the exact D27 TPM characteristic function, its first two
moments, the quasifree determinant/phase-projection formula, and elementary
lattice-law constraints.  ``--red`` reverses the final-charge counting-field
sign in the determinant formula; the determinant gate must then fail.
"""

from __future__ import annotations

import argparse
from pathlib import Path

import numpy as np
from scipy.linalg import expm
from scipy.special import zeta


TOL = 2.0e-10


def annihilators(modes: int) -> list[np.ndarray]:
    dim = 1 << modes
    result: list[np.ndarray] = []
    for j in range(modes):
        a = np.zeros((dim, dim), dtype=complex)
        for bits in range(dim):
            if (bits >> j) & 1:
                parity = (bits & ((1 << j) - 1)).bit_count()
                a[bits ^ (1 << j), bits] = (-1) ** parity
        result.append(a)
    return result


def dgamma(matrix: np.ndarray, annih: list[np.ndarray]) -> np.ndarray:
    out = np.zeros_like(annih[0])
    for i, ai in enumerate(annih):
        for j, aj in enumerate(annih):
            out += matrix[i, j] * ai.conj().T @ aj
    return out


def spectral_groups(operator: np.ndarray) -> dict[int, np.ndarray]:
    vals, vecs = np.linalg.eigh(operator)
    groups: dict[int, np.ndarray] = {}
    for index, val in enumerate(vals):
        key = int(np.rint(val))
        if abs(val - key) > 1.0e-9:
            raise RuntimeError(f"noninteger spectral value {val}")
        col = vecs[:, index : index + 1]
        groups[key] = groups.get(key, np.zeros_like(operator)) + col @ col.conj().T
    return groups


def dephase(operator: np.ndarray, groups: dict[int, np.ndarray]) -> np.ndarray:
    return sum((proj @ operator @ proj for proj in groups.values()),
               np.zeros_like(operator))


def tpm_law(rho: np.ndarray, minus: dict[int, np.ndarray],
            plus: dict[int, np.ndarray]) -> dict[int, float]:
    law: dict[int, float] = {}
    for qminus, pminus in minus.items():
        for qplus, pplus in plus.items():
            weight = np.trace(pplus @ pminus @ rho @ pminus @ pplus).real
            nu = qminus - qplus
            law[nu] = law.get(nu, 0.0) + float(weight)
    return law


def char_from_law(law: dict[int, float], lam: float) -> complex:
    return sum(weight * np.exp(1j * lam * nu) for nu, weight in law.items())


def determinant_projected(corr: np.ndarray, pminus: np.ndarray,
                          pplus: np.ndarray, lam: float,
                          red: bool, nodes: int = 33) -> complex:
    ident = np.eye(corr.shape[0], dtype=complex)
    total = 0.0j
    final_sign = 1.0 if red else -1.0
    for theta in 2.0 * np.pi * np.arange(nodes) / nodes:
        one_body = (
            expm(1j * theta * pminus)
            @ expm(1j * final_sign * lam * pplus)
            @ expm(1j * (lam - theta) * pminus)
        )
        total += np.linalg.det(ident - corr + corr @ one_body)
    return total / nodes


def cumulants(support: np.ndarray, probs: np.ndarray) -> tuple[float, float, float, float]:
    mean = float(np.sum(probs * support))
    centered = support - mean
    k2 = float(np.sum(probs * centered**2))
    k3 = float(np.sum(probs * centered**3))
    k4 = float(np.sum(probs * centered**4) - 3.0 * k2**2)
    return mean, k2, k3, k4


def run(red: bool) -> tuple[bool, str]:
    rng = np.random.default_rng(20260829)
    modes = 4
    annih = annihilators(modes)
    ident1 = np.eye(modes, dtype=complex)

    raw_h = rng.normal(size=(modes, modes)) + 1j * rng.normal(size=(modes, modes))
    h0 = 0.45 * (raw_h + raw_h.conj().T)
    corr = np.linalg.inv(ident1 + expm(h0))
    rho = expm(-dgamma(h0, annih))
    rho /= np.trace(rho)

    pminus = np.diag([1.0, 1.0, 0.0, 0.0]).astype(complex)
    raw_dyn = rng.normal(size=(modes, modes)) + 1j * rng.normal(size=(modes, modes))
    h_dyn = 0.5 * (raw_dyn + raw_dyn.conj().T)
    evolution = expm(-0.73j * h_dyn)
    pplus = evolution.conj().T @ pminus @ evolution
    qminus = dgamma(pminus, annih)
    qplus = dgamma(pplus, annih)
    minus_groups = spectral_groups(qminus)
    plus_groups = spectral_groups(qplus)
    law = tpm_law(rho, minus_groups, plus_groups)
    rho_dephased = dephase(rho, minus_groups)

    lambdas = np.linspace(-np.pi, np.pi, 17)
    direct = np.array([char_from_law(law, lam) for lam in lambdas])
    trace_fcs = np.array([
        np.trace(expm(-1j * lam * qplus) @ expm(1j * lam * qminus) @ rho_dephased)
        for lam in lambdas
    ])
    determinant = np.array([
        determinant_projected(corr, pminus, pplus, lam, red)
        for lam in lambdas
    ])
    trace_residue = float(np.max(np.abs(direct - trace_fcs)))
    determinant_residue = float(np.max(np.abs(direct - determinant)))

    h_commuting = np.diag([-0.7, 0.2, 0.9, 1.4]).astype(complex)
    corr_commuting = np.linalg.inv(ident1 + expm(h_commuting))
    rho_commuting = expm(-dgamma(h_commuting, annih))
    rho_commuting /= np.trace(rho_commuting)
    law_commuting = tpm_law(rho_commuting, minus_groups, plus_groups)
    direct_commuting = np.array([
        char_from_law(law_commuting, lam) for lam in lambdas
    ])
    simple_determinant = np.array([
        np.linalg.det(
            ident1 - corr_commuting
            + corr_commuting @ expm(-1j * lam * pplus) @ expm(1j * lam * pminus)
        )
        for lam in lambdas
    ])
    simple_determinant_residue = float(np.max(np.abs(
        direct_commuting - simple_determinant
    )))

    mean_law = sum(nu * weight for nu, weight in law.items())
    m2_law = sum(nu * nu * weight for nu, weight in law.items())
    mean_operator = np.trace(
        rho @ (qminus - dephase(qplus, minus_groups))
    ).real
    delta = qplus - qminus
    m2_operator = np.trace(rho @ dephase(delta @ delta, minus_groups)).real
    mean_residue = float(abs(mean_law - mean_operator))
    m2_residue = float(abs(m2_law - m2_operator))

    sample_lambdas = np.array([-2.3, -0.8, 0.4, 1.7])
    toeplitz = np.array([
        [char_from_law(law, x - y) for y in sample_lambdas]
        for x in sample_lambdas
    ])
    toeplitz_min = float(np.linalg.eigvalsh(toeplitz).min())
    periodic_residue = float(np.max(np.abs(
        direct - np.array([char_from_law(law, lam + 2 * np.pi) for lam in lambdas])
    )))

    variance = m2_law - mean_law**2
    frac = mean_law - np.floor(mean_law)
    variance_floor = frac * (1.0 - frac)

    support = np.array([0.0, 1.0, 2.0, 3.0])
    probs_a = np.array([0.20, 0.65, 0.10, 0.05])
    probs_b = np.array([0.12, 0.78, 0.08, 0.02])
    cumulants_a = cumulants(support, probs_a)
    cumulants_b = cumulants(support, probs_b)

    cutoffs = np.array([10, 100, 1000, 10000], dtype=int)
    heavy_rows = []
    for cutoff in cutoffs:
        n = np.arange(1, cutoff + 1, dtype=float)
        mass = np.sum(n**-3) / float(zeta(3.0))
        abs_first = np.sum(n**-2) / float(zeta(3.0))
        second = np.sum(n**-1) / float(zeta(3.0))
        heavy_rows.append((cutoff, mass, abs_first, second))

    checks = {
        "FCS-C1 TPM trace identity": trace_residue < TOL,
        "FCS-C2 quasifree determinant": determinant_residue < TOL,
        "FCS-C2b commuting-state determinant": simple_determinant_residue < TOL,
        "FCS-C3 first moment": mean_residue < TOL,
        "FCS-C4 second moment": m2_residue < TOL,
        "FCS-C5 integer periodicity": periodic_residue < TOL,
        "FCS-C6 positive definiteness": toeplitz_min > -TOL,
        "FCS-C7 lattice variance floor": variance + TOL >= variance_floor,
        "FCS-C8 same support/mean, different higher cumulants": (
            abs(cumulants_a[0] - cumulants_b[0]) < TOL
            and abs(cumulants_a[1] - cumulants_b[1]) > 1.0e-3
            and abs(cumulants_a[2] - cumulants_b[2]) > 1.0e-3
        ),
        "FCS-C9 finite first/infinite second witness": (
            heavy_rows[-1][2] < 1.5 and heavy_rows[-1][3] > heavy_rows[0][3] + 1.5
        ),
    }

    lines = [
        f"mode={'RED(sign-flip)' if red else 'GREEN'}",
        f"TPM law={{{', '.join(f'{k}: {v:.12f}' for k, v in sorted(law.items()))}}}",
        f"normalization={sum(law.values()):.15f}",
        f"trace_residue={trace_residue:.3e}",
        f"determinant_residue={determinant_residue:.3e}",
        f"simple_determinant_residue={simple_determinant_residue:.3e}",
        f"mean={mean_law:.12f} mean_residue={mean_residue:.3e}",
        f"second_raw={m2_law:.12f} second_residue={m2_residue:.3e}",
        f"variance={variance:.12f} lattice_floor={variance_floor:.12f}",
        f"periodicity_residue={periodic_residue:.3e}",
        f"toeplitz_min_eigenvalue={toeplitz_min:.3e}",
        f"law_A_cumulants={cumulants_a}",
        f"law_B_cumulants={cumulants_b}",
        "heavy_tail cutoff,mass,abs_first,second_raw:",
    ]
    lines.extend(
        f"  {cutoff:5d} {mass:.12f} {abs_first:.12f} {second:.12f}"
        for cutoff, mass, abs_first, second in heavy_rows
    )
    lines.extend(f"{'PASS' if ok else 'FAIL'} {name}" for name, ok in checks.items())
    ok = all(checks.values())
    lines.append(f"RESULT={'PASS' if ok else 'FAIL'}")
    return ok, "\n".join(lines) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--red", action="store_true")
    parser.add_argument("--report", type=Path)
    args = parser.parse_args()
    ok, report = run(args.red)
    print(report, end="")
    if args.report is not None:
        args.report.write_text(report, encoding="utf-8")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
