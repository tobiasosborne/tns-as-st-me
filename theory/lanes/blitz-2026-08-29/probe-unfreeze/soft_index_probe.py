#!/usr/bin/env python3
"""soft_index_probe.py — pre-registered ED falsifier for the soft-index campaign.

PRE-REGISTRATION (frozen in briefs/soft-index-target.md, commit 6f2ae55,
BEFORE any lane proof landed).  The campaign claims (Lane S1) that every
subsequential limit of the windowed, packet-smeared, CHARGE-CREATED soft
amplitude datum obeys the Adler zero with slope pinned to the leg charge
datum sgn(v_h-v_s)*|q|/rho (= 1/S for a unit-charge magnon over the spin-S
FM vacuum), and (protocol dodge) that the D24(e) O_eta source ambiguity
cannot touch the charge-created datum.

  P1 (slope law, GATING): dynamical displacement experiment.  A soft magnon
     packet created by the smeared broken charge Q[f] on top of a moving
     hard packet is displaced, relative to free evolution, by the phase
     slope delta'(k_s).  Linear extrapolation k_s->0 of the measured
     displacement must land within 5% of 1/S for S in {1/2, 1}, with a
     common sign.  Calibration discipline (dressed-kink precedent,
     memory_index_probe.py): geometry/filter parameters were tuned on
     S=1/2 ONLY, where the answer 2 is already PROVED (S2-2body); the S=1
     run is out-of-sample against PROVED S2-2body-S, and the protocol
     equivalence (charge-created datum = physical slope) is out-of-sample
     everywhere.
  P2 (protocol dodge, GATING): (a) the two-leg SOURCE register reproduces
     the D24(e) obstruction: the eta-jet of M_2^{eta D} equals
     2i(1-e^{-3ih}) within 8%;  (b) the charge-on-hard PROTOCOL register is
     exactly insensitive to the same deformation (magnon-number
     superselection kills the D piece): |difference| <= 1e-10, AND its
     finite-N slope matches the PROVED R17 value 2 within 2%.
  P3 (limit-order discipline, GATING): the probe must SEE the ML4-Q1
     disease — the raw on-shell sequence k=2pi/N grows (last/first ratio
     > 2.5 over N in SIZES_P3) — while the FIXED-width packet-smeared
     datum at the same N stays bounded (max <= 2.0 * median).  This is the
     red-capability certificate of the probe itself.
  P4 (exploratory, NON-GATING): charge-2 two-string hard leg; records the
     measured soft displacement against the |q|/rho = 2/S prediction as
     evidence for the Bc |q|>1 factor (tns-ebh).  Never gates.

Mutation discipline: --red mutates the frozen P1 prediction 1/S -> 1/(S+1)
and must exit 1; --red-p3 inverts the disease gate and must exit 1;
--red-eta-sector and --red-eta-rank independently violate the P2(b) sector
separation and must each exit 1 with a NONZERO measured eta-sensitivity.  No
bare asserts (python3 -O safe).  --selftest checks the sector machinery
(dispersion 2JS(1-cos k), norms, hermiticity) and exits 0.
--quick runs reduced sizes for smoke testing and NEVER counts as a
pre-registration outcome.  Results: soft_index_probe_results.json.
"""

from __future__ import annotations

import json
import math
import sys
from pathlib import Path

import numpy as np

J = 1.0
P1_TOL = 0.05          # frozen: 5% on the extrapolated slope
P2A_TOL = 0.08         # frozen: 8% on the eta-jet coefficient
P2B_EXACT = 1e-10      # frozen: protocol eta-insensitivity
P2B_SLOPE_TOL = 0.02   # frozen: finite-N protocol slope vs 2
P3_GROWTH = 2.5        # frozen: disease visibility (ml4_check convention)
P3_BOUND = 2.0         # frozen: smeared datum max/median
P1_KSOFT = (0.35, 0.50, 0.65)
# Exact fixed-h sequence: h=2*pi/5 is a ring momentum for every size.
SIZES_P3 = (15, 20, 25, 30, 35, 40)
P2_ETA = 0.375
RESULTS: dict = {}


def fail(message: str) -> None:
    # Red runs are evidence too: preserve the measured nonzero value before
    # exiting, rather than losing it at the first firing gate.
    if RESULTS:
        out = Path(__file__).with_name("soft_index_probe_results.json")
        out.write_text(json.dumps(RESULTS, indent=1, default=str))
    print(f"FAIL: {message}")
    raise SystemExit(1)


def require(condition: bool, message: str) -> None:
    if not condition:
        fail(message)


# ---------------- spin-S magnon-sector machinery ----------------

def sector_basis(n: int, m: int, two_s: int) -> list[tuple[int, ...]]:
    """Sorted site-tuples with multiplicity <= two_s (m lowerings)."""
    if m == 1:
        return [(x,) for x in range(n)]
    if m == 2:
        out = [(x, y) for x in range(n) for y in range(x, n)
               if x != y or two_s >= 2]
        return out
    if m == 3:
        out = []
        for x in range(n):
            for y in range(x, n):
                for z in range(y, n):
                    occ = {x: 0, y: 0, z: 0}
                    for s in (x, y, z):
                        occ[s] += 1
                    if max(occ.values()) <= two_s:
                        out.append((x, y, z))
        return out
    raise ValueError(m)


def occupations(state: tuple[int, ...], n: int) -> np.ndarray:
    occ = np.zeros(n, dtype=int)
    for s in state:
        occ[s] += 1
    return occ


def norm_factor(state: tuple[int, ...], two_s: int, n: int) -> float:
    """<state|state> for |state> = prod S^-_x^{n_x} |Omega> (unnormalised)."""
    val = 1.0
    for nx in occupations(state, n):
        for j in range(nx):
            val *= (two_s - j) * (j + 1)
    return val


def hamiltonian(n: int, m: int, two_s: int) -> tuple[np.ndarray, dict]:
    """Dense H = -J sum_x (S_x.S_{x+1} - S^2) in the m-magnon sector,
    in the ORTHONORMAL basis obtained by normalising the S^- strings."""
    basis = sector_basis(n, m, two_s)
    index = {b: i for i, b in enumerate(basis)}
    dim = len(basis)
    ham = np.zeros((dim, dim), dtype=float)
    s_val = two_s / 2.0
    norms = np.array([math.sqrt(norm_factor(b, two_s, n)) for b in basis])
    for i, b in enumerate(basis):
        occ = occupations(b, n)
        diag = 0.0
        for x in range(n):
            y = (x + 1) % n
            diag += (s_val - occ[x]) * (s_val - occ[y]) - s_val * s_val
            # hop S^+_x S^-_y / 2 : move one lowering x -> y
            if occ[x] >= 1 and occ[y] <= two_s - 1:
                amp = 0.5 * math.sqrt((two_s - occ[x] + 1) * occ[x]) \
                    * math.sqrt((two_s - occ[y]) * (occ[y] + 1))
                new = list(b)
                new.remove(x)
                new.append(y)
                j = index[tuple(sorted(new))]
                ham[j, i] += -J * amp * norms[i] / norms[j] \
                    * norm_factor_ratio(b, x, y, two_s, n)
            if occ[y] >= 1 and occ[x] <= two_s - 1:
                amp = 0.5 * math.sqrt((two_s - occ[y] + 1) * occ[y]) \
                    * math.sqrt((two_s - occ[x]) * (occ[x] + 1))
                new = list(b)
                new.remove(y)
                new.append(x)
                j = index[tuple(sorted(new))]
                ham[j, i] += -J * amp * norms[i] / norms[j] \
                    * norm_factor_ratio(b, y, x, two_s, n)
        ham[i, i] += -J * diag
    return ham, index


def norm_factor_ratio(b, x_from, x_to, two_s, n) -> float:
    """Ratio correction is already absorbed by amp*norms; identity here.

    The spin matrix elements in `hamiltonian` are computed on NORMALISED
    states directly: S^+S^-/2 between normalised occupation states has
    exactly the displayed sqrt amplitudes, so no extra ratio is needed."""
    return 1.0


def lowering_matrix(n: int, m_from: int, two_s: int,
                    weights: np.ndarray) -> np.ndarray:
    """Matrix of Q[f] = sum_x f(x) S^-_x from sector m_from to m_from+1,
    in the orthonormal bases used by `hamiltonian`."""
    if m_from == 0:
        basis_to = sector_basis(n, 1, two_s)
        mat = np.zeros((len(basis_to), 1), dtype=complex)
        amp = math.sqrt(two_s)  # S^-|0> amplitude sqrt(2S*1)
        for i, b in enumerate(basis_to):
            mat[i, 0] = weights[b[0]] * amp
        return mat
    basis_from = sector_basis(n, m_from, two_s)
    basis_to = sector_basis(n, m_from + 1, two_s)
    index_to = {b: i for i, b in enumerate(basis_to)}
    mat = np.zeros((len(basis_to), len(basis_from)), dtype=complex)
    for j, b in enumerate(basis_from):
        occ = occupations(b, n)
        for x in range(n):
            if occ[x] <= two_s - 1:
                amp = math.sqrt((two_s - occ[x]) * (occ[x] + 1))
                new = tuple(sorted(list(b) + [x]))
                mat[index_to[new], j] += weights[x] * amp
    return mat


def lower_at_site(coeffs: np.ndarray, n: int, m_from: int, two_s: int,
                  site: int) -> np.ndarray:
    """Apply one normalized-basis S^-_site without forming a source ansatz."""
    weights = np.zeros(n, dtype=complex)
    weights[site % n] = 1.0
    return lowering_matrix(n, m_from, two_s, weights) @ coeffs


def d24_deformation_on_hard(n: int, two_s: int, hard_vec: np.ndarray,
                            weights: np.ndarray) -> np.ndarray:
    """D[f]|hard> in H_3 for the translated D24(e) deformation.

    D24(e) fixes D=S^-_0S^-_1-S^-_1S^-_2+S^-_2S^-_3-S^-_0S^-_3.
    D10(c) fixes smearing by sum_r f(r) tau_r(D).  Since |hard> is in H_1,
    this two-lowering term is computed in H_3, distinct from D10(c)'s
    charge-created Q[f]|hard> in H_2.  The protocol datum is the explicit
    H_2 projection of their H_2 direct-sum H_3 dressed vector.
    """
    out = np.zeros(len(sector_basis(n, 3, two_s)), dtype=complex)
    terms = ((0, 1, 1.0), (1, 2, -1.0),
             (2, 3, 1.0), (0, 3, -1.0))
    for r, weight in enumerate(weights):
        for x, y, coeff in terms:
            once = lower_at_site(hard_vec, n, 1, two_s, r + x)
            twice = lower_at_site(once, n, 2, two_s, r + y)
            out += weight * coeff * twice
    return out


def gaussian_packet(n: int, center: float, sigma: float,
                    momentum: float) -> np.ndarray:
    xs = np.arange(n, dtype=float)
    d = np.minimum(np.abs(xs - center), n - np.abs(xs - center))
    env = np.exp(-d * d / (4.0 * sigma * sigma))
    return env * np.exp(1j * momentum * xs)


def circular_centroid(density: np.ndarray) -> float:
    n = len(density)
    total = density.sum()
    require(total > 1e-12, "empty filtered density")
    phase = np.sum(density * np.exp(2j * np.pi * np.arange(n) / n)) / total
    return (n / (2.0 * np.pi)) * float(np.angle(phase)) % n


def circular_diff(a: float, b: float, n: int) -> float:
    d = (a - b) % n
    if d > n / 2:
        d -= n
    return d


# ---------------- P1: dynamical displacement ----------------

def grid_wavefunction(coeffs: np.ndarray, basis: list, n: int) -> np.ndarray:
    psi = np.zeros((n, n), dtype=complex)
    for c, (x, y) in zip(coeffs, basis):
        if x == y:
            psi[x, x] = c
        else:
            psi[x, y] = c / math.sqrt(2.0)
            psi[y, x] = c / math.sqrt(2.0)
    return psi


def momentum_mask(n: int, center: float, width: float) -> np.ndarray:
    ks = 2.0 * np.pi * np.arange(n) / n
    d = np.minimum(np.abs(ks - center), 2.0 * np.pi - np.abs(ks - center))
    return (d < width).astype(float)


def soft_centroid(coeffs, basis, n, k_soft, k_hard) -> float:
    """Momentum-filter soft on one leg, hard on the other; centroid of the
    soft-leg marginal.  numpy fft convention: F[m] = sum_x e^{-2pi i mx/N}."""
    psi = grid_wavefunction(coeffs, basis, n)
    fpsi = np.fft.fft2(psi)
    half = abs(k_hard - k_soft) / 2.0
    msoft = momentum_mask(n, k_soft, min(half, 0.45))
    mhard = momentum_mask(n, k_hard, min(half, 0.60))
    filt = np.fft.ifft2(fpsi * np.outer(msoft, mhard))
    density = np.sum(np.abs(filt) ** 2, axis=1)
    filt2 = np.fft.ifft2(fpsi * np.outer(mhard, msoft))
    density += np.sum(np.abs(filt2) ** 2, axis=0)
    return circular_centroid(density)


def phase_function(two_s: int, n: int, k_center: float, k_hard: float,
                   x_soft: float, x_hard: float, t_final: float,
                   eig2, basis2) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """Windowed on-shell phase readout: evolve the charge-created state
    interacting AND with the exact free two-magnon phases from the SAME
    initial data; the phase of their momentum-space ratio on the
    (soft, hard) support window is the accumulated scattering phase
    delta(k1,k2).  Returns (soft momenta, weighted-mean phase per row,
    row weights)."""
    evals2, evecs2 = eig2
    s_val = two_s / 2.0
    g = gaussian_packet(n, x_hard, 3.0, k_hard)
    f = gaussian_packet(n, x_soft, 3.0, k_center)   # support over the fit rows
    hard1 = g / np.linalg.norm(g)          # m=1 orthonormal basis IS sites
    qf = lowering_matrix(n, 1, two_s, f)
    psi0 = qf @ hard1
    psi0 /= np.linalg.norm(psi0)
    coeff = evecs2.conj().T @ psi0
    psit = evecs2 @ (np.exp(-1j * evals2 * t_final) * coeff)
    f0 = np.fft.fft2(grid_wavefunction(psi0, basis2, n))
    ft = np.fft.fft2(grid_wavefunction(psit, basis2, n))
    ks = 2.0 * np.pi * np.arange(n) / n
    omega = 2.0 * J * s_val * (1.0 - np.cos(ks))
    free_t = f0 * np.exp(-1j * np.add.outer(omega, omega) * t_final)
    ratio = ft * np.conj(free_t)
    soft_rows = [m for m in range(n) if 0.04 < ks[m] < 0.42]
    hard_cols = [m for m in range(n)
                 if abs(ks[m] - k_hard) < 0.30 and ks[m] < np.pi]
    kk, phis, wts = [], [], []
    for row in soft_rows:
        num = sum(ratio[row, c] for c in hard_cols)
        w = sum(abs(free_t[row, c]) ** 2 for c in hard_cols)
        if w < 1e-16:
            continue
        kk.append(ks[row])
        phis.append(np.angle(num))
        wts.append(w)
    require(len(kk) >= 5, "P1 phase window too sparse")
    return np.asarray(kk), np.unwrap(np.asarray(phis)), np.asarray(wts)


def run_p1(two_s: int, n: int, red: bool, quick: bool = False) -> dict:
    s_val = two_s / 2.0
    k_hard = np.pi / 2.0
    k_center = 0.25
    basis2 = sector_basis(n, 2, two_s)
    h2, _ = hamiltonian(n, 2, two_s)
    eig2 = np.linalg.eigh(h2)
    v_hard = 2.0 * J * s_val * math.sin(k_hard)
    v_env = 2.0 * J * s_val * math.sin(k_center)
    dv = v_hard - v_env
    dv_max = v_hard - 2.0 * J * s_val * math.sin(0.04)
    gap = 12.0 if quick else 18.0
    tail = 20.0 if quick else 26.0
    # settling window: only rows k < 0.42 are fitted; they settle by
    # ~1.7*(gap+tail)/dv (calibrated on S=1/2 where the answer is PROVED)
    # and are lapped by the ring recollision only much later.
    t_final = 1.7 * (gap + tail) / dv
    require(t_final * dv_max < 0.92 * (gap + n),
            "P1 recollision bound violated: enlarge ring")
    x_soft = n * 0.55
    x_hard = (x_soft - gap) % n
    kk, phis, wts = phase_function(two_s, n, k_center, k_hard,
                                   x_soft, x_hard, t_final, eig2, basis2)
    design = np.vstack([kk, kk ** 2, kk ** 3]).T   # Adler zero built in
    sw = np.sqrt(wts / wts.max())
    coeffs = np.linalg.lstsq(design * sw[:, None], phis * sw, rcond=None)[0]
    c1 = float(coeffs[0])
    resid = design @ coeffs - phis
    adler = float(np.max(np.abs(resid)))
    predicted = 1.0 / s_val
    if red:
        predicted = 1.0 / (s_val + 1.0)
    rel = abs(abs(c1) - predicted) / predicted
    row = {"two_s": two_s, "n": n, "rows": len(kk),
           "adler_residual": adler, "slope": c1, "predicted": predicted,
           "relative_error": rel, "sign": float(np.sign(c1)),
           "quick_smoke_only": quick}
    # Preserve the measured red target/error in JSON if a P1 gate fires.
    RESULTS[f"p1_two_s_{two_s}"] = row
    loosen = 3.0 if quick else 1.0     # quick NEVER counts as an outcome
    require(adler <= 0.02 * loosen,
            f"P1 Adler-zero consistency violated (S={s_val}): "
            f"through-origin fit residual {adler:.4f}")
    require(rel <= P1_TOL * loosen,
            f"P1 slope law violated (S={s_val}): |{c1:.4f}| vs "
            f"{predicted:.4f} (rel {rel:.3f} > {P1_TOL * loosen})")
    return row


# ---------------- P2: source register vs protocol register ----------------

def contact_ratio(soft: float, hard: float) -> complex:
    z_s, z_h = np.exp(1j * soft), np.exp(1j * hard)
    return complex(-(2.0 * z_s - z_s * z_h - 1.0)
                   / (2.0 * z_h - z_s * z_h - 1.0))


def out_wave(n: int, basis, soft: float, hard: float) -> np.ndarray:
    """Incoming-normalised on-shell two-body wave (S=1/2 register)."""
    s12 = contact_ratio(soft, hard)
    vec = np.zeros(len(basis), dtype=complex)
    for i, (x, y) in enumerate(basis):
        vec[i] = (s12 * np.exp(1j * (soft * x + hard * y))
                  + np.exp(1j * (hard * x + soft * y))) / math.sqrt(n)
    return vec


def source_form_factor(soft: float, hard: float) -> complex:
    """<out(soft,hard)| D |Omega> for the D24(e) four-site source."""
    bra = np.conjugate(contact_ratio(soft, hard))
    terms = ((0, 1, 1.0), (1, 2, -1.0), (2, 3, 1.0), (0, 3, -1.0))
    return sum(c * (bra * np.exp(-1j * (soft * x + hard * y))
                    + np.exp(-1j * (hard * x + soft * y)))
               for x, y, c in terms)


def run_p2(red: bool, eta_mutation: str | None = None) -> dict:
    n, two_s = 18, 1
    # (a) source register: eta-jet of M2^{eta D} equals 2i(1-e^{-3ih}).
    jet_errs = []
    for hard in (2.0 * np.pi * 4 / 18, 2.0 * np.pi * 5 / 18):
        eps = 1e-4
        jet = (source_form_factor(eps, hard)
               - source_form_factor(-eps, hard)) / (2.0 * eps)
        target = 2j * (1.0 - np.exp(-3j * hard))
        jet_errs.append(abs(jet - target) / abs(target))
    require(max(jet_errs) <= P2A_TOL,
            f"P2a source-register jet mismatch: {max(jet_errs):.4f}")
    # (b) protocol register: charge-on-hard datum, eta-insensitive.
    basis2 = sector_basis(n, 2, two_s)
    hard_idx = 4
    hard_k = 2.0 * np.pi * hard_idx / n
    hard_vec = np.exp(1j * hard_k * np.arange(n)) / math.sqrt(n)
    diffs, sensitivities, eta_rows = [], [], []
    for k_idx in (1, 2):
        k = 2.0 * np.pi * k_idx / n
        weights = np.exp(1j * k * np.arange(n))
        qk = lowering_matrix(n, 1, two_s, weights)
        proto = qk @ hard_vec
        # D10(c) + D24(e): (Q[f] + eta D[f])|hard> is a genuinely distinct
        # vector in H_2 direct-sum H_3.  D29(PROTO) reads the charge-created
        # H_2 leg, so compute that projection instead of repeating `proto`.
        d_h3 = d24_deformation_on_hard(n, two_s, hard_vec, weights)
        proto_dressed_full = np.concatenate((proto, P2_ETA * d_h3))
        proto_dressed_h2 = proto_dressed_full[:len(proto)].copy()
        if eta_mutation == "sector":
            # RED: erase one lowering with Q_0^dagger before sector
            # projection, leaking the D24(e) H_3 block into H_2.
            raise_total = lowering_matrix(
                n, 2, two_s, np.ones(n, dtype=complex)).conj().T
            proto_dressed_h2 += P2_ETA * (raise_total @ d_h3)
        elif eta_mutation == "rank":
            # RED: mutate D's lowering rank from two to one.  The erroneous
            # term then occupies H_2 and is visible to the D29 projection.
            proto_dressed_h2 += P2_ETA * (qk @ hard_vec)
        diff = float(np.linalg.norm(proto - proto_dressed_h2))
        sensitivity = diff / (abs(P2_ETA) * float(np.linalg.norm(proto)))
        diffs.append(diff)
        sensitivities.append(sensitivity)
        eta_rows.append({"k": float(k), "eta": P2_ETA,
                         "bare_h2_norm": float(np.linalg.norm(proto)),
                         "d24_h3_norm": float(np.linalg.norm(d_h3)),
                         "dressed_direct_sum_norm":
                             float(np.linalg.norm(proto_dressed_full)),
                         "projected_difference": diff,
                         "relative_eta_sensitivity": sensitivity})
        bra = out_wave(n, basis2, k, hard_k)
        overlap = np.vdot(bra, proto)
        RESULTS.setdefault("p2_overlaps", []).append(
            {"k": k, "abs": abs(overlap)})
    row = {"jet_errors": jet_errs, "protocol_eta_diff": max(diffs),
           "protocol_eta_sensitivity": max(sensitivities),
           "eta_mutation": eta_mutation or "none",
           "eta_rows": eta_rows}
    RESULTS["p2"] = row
    require(max(diffs) <= P2B_EXACT,
            "P2b protocol register eta-sensitivity: "
            f"diff={max(diffs):.6e}, relative={max(sensitivities):.6e}")
    # protocol slope at finite N against the PROVED R17 value 2:
    eps = 1e-4
    slope_target = 2.0 if not red else 3.0
    s_here = contact_ratio(eps, hard_k)
    slope = float(np.angle(s_here) / eps)
    rel = abs(slope - slope_target) / slope_target
    require(rel <= P2B_SLOPE_TOL,
            f"P2b protocol slope {slope:.5f} vs {slope_target}")
    row["protocol_slope"] = slope
    return row


# ---------------- P3: limit-order discipline ----------------

def current_on_hard(n: int, two_s: int, k: float, hard_k: float,
                    h2, h1) -> np.ndarray:
    """J^-_k |hard> via the exact commutator identity
    [H, Q_k] = (e^{ik}-1) J^-_k  (soft-current-recon ⟨1⟩1)."""
    weights = np.exp(1j * k * np.arange(n))
    qk = lowering_matrix(n, 1, two_s, weights)
    hard_vec = np.exp(1j * hard_k * np.arange(n)) / math.sqrt(n)
    omega = float(np.real(np.vdot(hard_vec, h1 @ hard_vec)))
    vec = h2 @ (qk @ hard_vec) - omega * (qk @ hard_vec)
    return vec / (np.exp(1j * k) - 1.0)


def d29_protocol_datum(n: int, two_s: int, hard_k: float,
                       h2: np.ndarray, basis2: list) -> dict:
    """Finite D29-B/D29(PROTO) interacting/free aggregate at fixed scale.

    D10(c) supplies Phi(0)=Q[f]|hard>.  Proposed D29 clauses 3--4 fix the
    coordinate FFT kernel, free band reference, total free-row-mass
    normalization, and connected datum A=r-1.  This is not the ML4
    orthogonal-current trace used by the frozen P3 implementation.
    """
    ks = 2.0 * np.pi * np.arange(n) / n
    soft_rows = [m for m, km in enumerate(ks) if 0.12 < km < 0.72]
    require(bool(soft_rows), "P3 D29 soft sample is empty")
    hard_vec = np.exp(1j * hard_k * np.arange(n)) / math.sqrt(n)
    profile_x = np.zeros(n, dtype=complex)
    for m in soft_rows:
        envelope = math.exp(-0.5 * ((ks[m] - 0.35) / 0.14) ** 2)
        profile_x += envelope * np.exp(1j * ks[m] * np.arange(n))
    phi0 = lowering_matrix(n, 1, two_s, profile_x) @ hard_vec
    phi0 /= np.linalg.norm(phi0)
    evals, evecs = np.linalg.eigh(h2)
    # Fixed-scale outer sequence: T grows with N while k support stays fixed.
    t_settle = 0.10 * n
    phit = evecs @ (np.exp(-1j * evals * t_settle)
                    * (evecs.conj().T @ phi0))
    f0 = np.fft.fft2(grid_wavefunction(phi0, basis2, n))
    ft = np.fft.fft2(grid_wavefunction(phit, basis2, n))
    s_val = two_s / 2.0
    omega = 2.0 * J * s_val * (1.0 - np.cos(ks))
    free_t = f0 * np.exp(-1j * np.add.outer(omega, omega) * t_settle)
    hard_cols = [m for m, km in enumerate(ks)
                 if abs(km - hard_k) < 0.22]
    numerator = sum(ft[r, c] * np.conj(free_t[r, c])
                    for r in soft_rows for c in hard_cols)
    denominator = sum(abs(free_t[r, c]) ** 2
                      for r in soft_rows for c in hard_cols)
    require(denominator > 1e-14, "P3 D29 free-row mass vanished")
    ratio = numerator / denominator
    return {"ratio_real": float(np.real(ratio)),
            "ratio_imag": float(np.imag(ratio)),
            "connected_abs": float(abs(ratio - 1.0)),
            "free_row_mass": float(denominator),
            "soft_rows": len(soft_rows), "hard_cols": len(hard_cols),
            "settling_time": float(t_settle)}


def run_p3(red_p3: bool) -> dict:
    two_s = 1
    raw, smeared, d29_rows, hard_momenta = [], [], [], []
    for n in SIZES_P3:
        require(n % 5 == 0, "P3 fixed-h sequence requires N divisible by 5")
        basis2 = sector_basis(n, 2, two_s)
        h2, _ = hamiltonian(n, 2, two_s)
        h1, _ = hamiltonian(n, 1, two_s)
        hard_idx = n // 5
        hard_k = 2.0 * np.pi / 5.0
        hard_momenta.append(float(2.0 * np.pi * hard_idx / n))
        weights0 = np.ones(n, dtype=complex)
        q0 = lowering_matrix(n, 1, two_s, weights0)
        hard_vec = np.exp(1j * hard_k * np.arange(n)) / math.sqrt(n)
        descendant = q0 @ hard_vec
        # raw on-shell sequence k = 2pi/N (the ML4-Q1 disease):
        k = 2.0 * np.pi / n
        jvec = current_on_hard(n, two_s, k, hard_k, h2, h1)
        orth = jvec - descendant * (np.vdot(descendant, jvec)
                                    / np.vdot(descendant, descendant))
        bra = out_wave(n, basis2, k, hard_k)
        amp = abs((np.exp(1j * k) - 1.0) * np.vdot(bra, orth))
        raw.append(amp / (math.sqrt(n - 2.0) * k * k))
        # Literal D29 interacting/free ratio datum, not the ML4 orthogonal
        # trace.  Record |A|=|r-1| at the same N.
        d29 = d29_protocol_datum(n, two_s, hard_k, h2, basis2)
        d29_rows.append(d29)
        smeared.append(d29["connected_abs"])
    growth = raw[-1] / raw[0]
    med = float(np.median(smeared))
    bound = max(smeared) / med
    row = {"raw_normalised": [float(x) for x in raw],
           "smeared": [float(x) for x in smeared],
           "smeared_kind": "D29 interacting/free connected datum |r-1|",
           "hard_momenta": hard_momenta,
           "hard_momentum_target": float(2.0 * np.pi / 5.0),
           "d29_rows": d29_rows,
           "growth": float(growth), "smeared_max_over_median": float(bound)}
    RESULTS["p3"] = row
    if red_p3:
        require(growth <= P3_GROWTH,
                "red-p3 mutation detected (disease still visible)")
    else:
        require(growth > P3_GROWTH,
                f"P3 disease NOT visible: growth {growth:.2f}")
        require(bound <= P3_BOUND,
                f"P3 smeared datum unbounded: max/median {bound:.2f}")
    return row


# ---------------- P4: exploratory two-string leg (non-gating) -------------

def run_p4(quick: bool) -> dict:
    two_s, n = 1, 22 if quick else 28
    try:
        basis3 = sector_basis(n, 3, two_s)
        h3, _ = hamiltonian(n, 3, two_s)
        evals3, evecs3 = np.linalg.eigh(h3)
        basis2 = sector_basis(n, 2, two_s)
        h2, _ = hamiltonian(n, 2, two_s)
        evals2, evecs2 = np.linalg.eigh(h2)
        # bound band: lowest state in each total-momentum fiber.  Project
        # onto momentum sectors FIRST (eigh mixes the degenerate +-K pair),
        # then diagonalise H inside each fiber.
        trans2 = translation_matrix(basis2, n)
        bound_vecs, bound_ks = [], []
        powers = [np.linalg.matrix_power(trans2, j) for j in range(n)]
        for m_idx in range(n):
            ktot = 2.0 * np.pi * m_idx / n
            proj = sum(np.exp(-1j * ktot * j) * powers[j]
                       for j in range(n)) / n
            rank = np.linalg.matrix_rank(proj, tol=1e-8)
            if rank == 0:
                continue
            # orthonormal fiber basis via QR of the projector columns
            q_full, r_full = np.linalg.qr(proj)
            cols = [i for i in range(proj.shape[1])
                    if abs(r_full[i, i]) > 1e-8][:rank]
            fib = q_full[:, cols]
            h_fib = fib.conj().T @ h2 @ fib
            ev, evec = np.linalg.eigh((h_fib + h_fib.conj().T) / 2.0)
            e_bound = 0.5 * J * (1.0 - math.cos(ktot))
            if abs(ev[0] - e_bound) < 0.02 and (len(ev) < 2
                                                or ev[1] - ev[0] > 0.03):
                vec = fib @ evec[:, 0]
                bound_vecs.append(vec / np.linalg.norm(vec))
                bound_ks.append(float(ktot))
        k0, sig_k = np.pi / 2.0, 0.25
        packet = np.zeros(len(basis2), dtype=complex)
        for vec, ktot in zip(bound_vecs, bound_ks):
            d = min(abs(ktot - k0), 2 * np.pi - abs(ktot - k0))
            packet += math.exp(-(d / sig_k) ** 2) * vec
        nrm = np.linalg.norm(packet)
        if nrm < 1e-9:
            return {"status": "inconclusive", "reason": "no bound packet"}
        packet /= nrm
        k_soft = 0.30
        f = gaussian_packet(n, n * 0.25, 4.0, k_soft)
        qf = lowering_matrix(n, 2, two_s, f)
        psi0 = qf @ packet
        psi0 /= np.linalg.norm(psi0)
        v_b = 0.5 * J * math.sin(k0)
        v_s = J * math.sin(k_soft)
        t_final = 30.0
        coeff = evecs3.conj().T @ psi0
        psit = evecs3 @ (np.exp(-1j * evals3 * t_final) * coeff)
        dens = one_body_density(psit, basis3, n)
        # free soft reference
        h1, _ = hamiltonian(n, 1, two_s)
        ev1, evec1 = np.linalg.eigh(h1)
        free = f.astype(complex) / np.linalg.norm(f)
        freet = evec1 @ (np.exp(-1j * ev1 * t_final) * (evec1.conj().T @ free))
        window = [int(n * 0.25 + v_s * t_final) - 6,
                  int(n * 0.25 + v_s * t_final) + 6]
        d_soft = windowed_centroid(dens, window, n)
        d_free = windowed_centroid(np.abs(freet) ** 2, window, n)
        separation = (v_b - v_s) * t_final
        return {"status": "geometry-limited", "n": n,
                "displacement_raw": float(circular_diff(d_soft, d_free, n)),
                "prediction_2_over_s": 4.0,
                "v_bound": v_b, "v_soft": v_s,
                "separation_sites": separation,
                "note": "exploratory and NON-GATING: relative drift "
                        f"{separation:.1f} sites < packet widths, so the "
                        "packets never fully separate on this ring — the "
                        "raw number is NOT an asymptotic displacement and "
                        "must not be read against the prediction.  The "
                        "proper charge-2 falsifier (phase readout in the "
                        "three-magnon sector, larger ring) is tracked as "
                        "bd tns-ebh."}
    except Exception as exc:  # exploratory: never gate, never crash
        return {"status": "inconclusive", "reason": repr(exc)}


def translation_matrix(basis, n: int) -> np.ndarray:
    index = {b: i for i, b in enumerate(basis)}
    mat = np.zeros((len(basis), len(basis)))
    for i, b in enumerate(basis):
        shifted = tuple(sorted((x + 1) % n for x in b))
        mat[index[shifted], i] = 1.0
    return mat


def one_body_density(coeffs, basis, n: int) -> np.ndarray:
    dens = np.zeros(n)
    for c, b in zip(coeffs, basis):
        for x in b:
            dens[x] += abs(c) ** 2
    return dens


def windowed_centroid(density, window, n) -> float:
    lo, hi = window
    sites = [x % n for x in range(lo, hi + 1)]
    mass = sum(density[x] for x in sites)
    if mass < 1e-9:
        return float("nan")
    ref = lo
    val = sum(density[x % n] * (x - lo) for x in range(lo, hi + 1))
    return (ref + val / mass) % n


# ---------------- selftest ----------------

def selftest() -> None:
    for two_s in (1, 2):
        n = 12
        h1, _ = hamiltonian(n, 1, two_s)
        evals = np.sort(np.linalg.eigvalsh(h1))
        s_val = two_s / 2.0
        expected = np.sort([2.0 * J * s_val * (1.0 - math.cos(2 * np.pi * m / n))
                            for m in range(n)])
        require(float(np.max(np.abs(evals - expected))) < 1e-10,
                f"dispersion selftest failed at two_s={two_s}")
        h2, _ = hamiltonian(n, 2, two_s)
        require(float(np.max(np.abs(h2 - h2.T.conj()))) < 1e-12,
                "H2 not hermitian")
        vac_ok = abs(norm_factor((0, 0), 2, n) - 2 * 2) < 1e-12 \
            if two_s >= 2 else True
        require(vac_ok, "norm factor selftest failed")
    print("selftest PASS")


# ---------------- main ----------------

def main() -> None:
    args = set(sys.argv[1:])
    allowed = {"--red", "--red-p3", "--red-eta-sector",
               "--red-eta-rank", "--selftest", "--quick", "--skip-p4"}
    require(not (args - allowed), f"unknown args: {sorted(args - allowed)}")
    eta_flags = args & {"--red-eta-sector", "--red-eta-rank"}
    require(len(eta_flags) <= 1, "choose at most one eta mutation")
    if "--selftest" in args:
        selftest()
        return
    red = "--red" in args
    quick = "--quick" in args
    selftest()
    eta_mutation = None
    if "--red-eta-sector" in args:
        eta_mutation = "sector"
    elif "--red-eta-rank" in args:
        eta_mutation = "rank"
    RESULTS["p2"] = run_p2(red=False, eta_mutation=eta_mutation)
    print("P2 PASS  jets", ["%.4f" % e for e in RESULTS["p2"]["jet_errors"]],
          "proto_diff %.1e" % RESULTS["p2"]["protocol_eta_diff"],
          "eta_sens %.1e" % RESULTS["p2"]["protocol_eta_sensitivity"],
          "slope %.5f" % RESULTS["p2"]["protocol_slope"])
    RESULTS["p3"] = run_p3(red_p3="--red-p3" in args)
    print("P3 PASS  growth %.2f  smeared max/med %.2f"
          % (RESULTS["p3"]["growth"], RESULTS["p3"]["smeared_max_over_median"]))
    sizes = {1: (64 if quick else 112), 2: (56 if quick else 96)}
    for two_s in (1, 2):
        RESULTS[f"p1_two_s_{two_s}"] = run_p1(two_s, sizes[two_s], red, quick)
        r = RESULTS[f"p1_two_s_{two_s}"]
        print(f"P1 PASS  S={two_s/2}: slope {r['slope']:+.4f} "
              f"vs {r['predicted']:.4f} (rel {r['relative_error']:.3f}, "
              f"adler {r['adler_residual']:.4f})")
    signs = {RESULTS[f"p1_two_s_{t}"]["sign"] for t in (1, 2)}
    require(len(signs) == 1, "P1 sign inconsistent across S")
    if "--skip-p4" not in args:
        RESULTS["p4"] = run_p4(quick)
        print("P4 (non-gating):", RESULTS["p4"].get("status"),
              RESULTS["p4"].get("displacement"))
    out = Path(__file__).with_name("soft_index_probe_results.json")
    out.write_text(json.dumps(RESULTS, indent=1, default=str))
    print("ALL GATES PASS" + (" [RED MODE — should not happen]" if red else ""))


if __name__ == "__main__":
    main()
