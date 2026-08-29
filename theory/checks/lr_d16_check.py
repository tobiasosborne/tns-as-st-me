#!/usr/bin/env python3
"""Mutation-complete certificates for theory/lr-d16.md, repair round 2.

The checker separates algebraic certificates from finite-volume diagnostics.
It does not claim asymptotic physics.  In particular, LRD-C2(d) and
LRD-C3(e) are *negative* diagnostics: they exhibit the O(1) escaped magnon
and the m-dependent pinched state which force the r2 withdrawals/repairs.

Green mode evaluates all 17 rows.  Every evidence row has one registered,
specific mutant.  Red modes evaluate the target row group directly, so no
earlier failure can make a later gate unreachable; all gates in a group are
evaluated without short-circuiting.

    python3 -O theory/checks/lr_d16_check.py
    python3 -O theory/checks/lr_d16_check.py --red MODE
    python3 -O theory/checks/lr_d16_check.py --red-all

Exit codes: green 0 on success; a caught individual/all-red run exits 1;
an uncaught or nonspecific red mutation exits 2.  There are no bare asserts.
"""

from __future__ import annotations

import argparse
import math
import sys
from itertools import combinations

import numpy as np

TOL_EXACT = 1.0e-11
TOL_IDENT = 1.0e-9
TOL_PSD = 1.0e-12
TOL_PROB = 1.0e-10

J = 1.0
DELTA = 2.5
NSITES = 12
C0 = 6
K0 = 0.5 * math.pi
Y0 = 3.0
SIG = 1.4
WINDOWS = [(4, 9), (3, 10), (2, 11)]

R_C1A = "LRD-C1(a) normalisation"
R_C1B = "LRD-C1(b) raw integer spectrum/support"
R_C2A = "LRD-C2(a) equal-time defect"
R_C2B = "LRD-C2(b) scalar sharpness bound"
R_C2C = "LRD-C2(c) escaped-charge inequality"
R_C2D = "LRD-C2(d) O(1) magnon; ESC fails"
R_C3A = "LRD-C3(a) independent matrix identity"
R_C3B = "LRD-C3(b) edge split"
R_C3C = "LRD-C3(c) observable monotonicity"
R_C3D = "LRD-C3(d) W_m-pinched majorant"
R_C3E = "LRD-C3(e) pinched state varies with m"
R_C4A = "LRD-C4(a) bond EDW inequality"
R_C4B = "LRD-C4(b) H_XXZ dynamical EDW bound"
R_C4C = "LRD-C4(c) finite-chain kink calibration"
R_C5A = "LRD-C5(a) K1-K2 local kernel"
R_C5B = "LRD-C5(b) kink-bond positivity"
R_C6A = "LRD-C6(a) sharp kink is not dressed"

RED_TARGETS = {
    "c1-nonunitary": R_C1A,
    "c1-noninteger": R_C1B,
    "c2-unequal-time": R_C2A,
    "c2-small-constant": R_C2B,
    "c2-mismatched-complement": R_C2C,
    "c2-delete-outside-data": R_C2D,
    "c3-perturb-final-evolution": R_C3A,
    "c3-mismatched-complement": R_C3B,
    "c3-signed-majorant": R_C3C,
    "c3-delete-majorant": R_C3D,
    "c3-freeze-pinching": R_C3E,
    "c4-wrong-gap": R_C4A,
    "c4-kink-propagator": R_C4B,
    "c4-sharp-calibration": R_C4C,
    "c5-wrong-root": R_C5A,
    "c5-overstrong-field": R_C5B,
    "c6-identify-sharp-dressed": R_C6A,
}

ROW_GROUP = {
    R_C1A: "c1", R_C1B: "c1",
    R_C2A: "c2", R_C2B: "c2", R_C2C: "c2", R_C2D: "c2",
    R_C3A: "c3", R_C3B: "c3", R_C3C: "c3", R_C3D: "c3", R_C3E: "c3",
    R_C4A: "c4", R_C4B: "c4", R_C4C: "c4",
    R_C5A: "c5", R_C5B: "c5", R_C6A: "c6",
}


def sector_basis(n, ndown):
    states = []
    for pos in combinations(range(n), ndown):
        mask = 0
        for p in pos:
            mask |= 1 << p
        states.append(mask)
    states.sort()
    return states, {s: i for i, s in enumerate(states)}


def sz_table(states, n):
    out = np.empty((len(states), n))
    for i, state in enumerate(states):
        for x in range(n):
            out[i, x] = -0.5 if (state >> x) & 1 else 0.5
    return out


def hamiltonian(states, index, n, delta, kink_field, kink_scale=1.0):
    dim = len(states)
    h = np.zeros((dim, dim))
    cfield = (0.5 * J * math.sqrt(delta * delta - 1.0) * kink_scale
              if kink_field else 0.0)
    for i, state in enumerate(states):
        diag = 0.0
        for x in range(n - 1):
            a = -0.5 if (state >> x) & 1 else 0.5
            b = -0.5 if (state >> (x + 1)) & 1 else 0.5
            diag += -J * delta * (a * b - 0.25)
            diag += -cfield * (a - b)
            if ((state >> x) & 1) != ((state >> (x + 1)) & 1):
                moved = state ^ (1 << x) ^ (1 << (x + 1))
                h[index[moved], i] += -0.5 * J
        h[i, i] += diag
    return h


def rho_ref(n, c0):
    return np.array([0.5 if x + 1 <= c0 else -0.5 for x in range(n)])


def window_charges(sz, n, c0, a, b):
    delta_sz = sz - rho_ref(n, c0)[None, :]
    inside = np.array([a <= x + 1 <= b for x in range(n)])
    left = np.array([x + 1 < a for x in range(n)])
    right = np.array([x + 1 > b for x in range(n)])
    q_w = delta_sz[:, inside].sum(axis=1)
    q_wc = delta_sz[:, ~inside].sum(axis=1)
    n_w = ((0.5 - sz[:, left]).sum(axis=1)
           + (sz[:, right] + 0.5).sum(axis=1))
    return q_w, q_wc, n_w


def dw_number(sz):
    return (np.abs(np.diff(sz, axis=1)) > 1.0e-12).sum(axis=1).astype(float)


def kink_product_vector(states, n, q, z):
    amps = np.array([z * q ** (-(x + 1)) for x in range(n)])
    vec = np.empty(len(states))
    for i, state in enumerate(states):
        value = 1.0
        for x in range(n):
            if (state >> x) & 1:
                value *= amps[x]
        vec[i] = value
    norm = np.linalg.norm(vec)
    return vec / norm if norm else vec


def sharp_kink_vector(states, index, n, c0):
    mask = 0
    for x in range(n):
        if x + 1 > c0:
            mask |= 1 << x
    vec = np.zeros(len(states))
    vec[index[mask]] = 1.0
    return vec


def lower_packet(psi, states_from, index_to, n, k0, y0, sig):
    out = np.zeros(len(index_to), dtype=complex)
    envelope = np.array([
        math.exp(-((y + 1 - y0) ** 2) / (2.0 * sig * sig))
        for y in range(n)
    ])
    phase = np.array([np.exp(1j * k0 * (y + 1)) for y in range(n)])
    for i, state in enumerate(states_from):
        if psi[i] == 0:
            continue
        for y in range(n):
            if not (state >> y) & 1:
                out[index_to[state | (1 << y)]] += psi[i] * envelope[y] * phase[y]
    norm = np.linalg.norm(out)
    return out / norm if norm else out


class Propagator:
    def __init__(self, h):
        self.evals, self.vecs = np.linalg.eigh(h)

    def evolve(self, psi, t):
        coeff = self.vecs.T.conj() @ psi
        return self.vecs @ (np.exp(-1j * self.evals * t) * coeff)

    def evolve_many(self, psi, times):
        coeff = self.vecs.T.conj() @ psi
        phase = np.exp(-1j * self.evals[:, None] * np.asarray(times)[None, :])
        return self.vecs @ (coeff[:, None] * phase)

    def matrix(self, t):
        return self.vecs @ (np.exp(-1j * self.evals * t)[:, None]
                            * self.vecs.T.conj())


class ScaledPropagator:
    """Deliberately non-unitary data mutant for LRD-C1(a)."""

    def __init__(self, base, scale):
        self.base = base
        self.scale = scale

    def evolve(self, psi, t):
        return self.scale * self.base.evolve(psi, t)


class Context:
    def __init__(self):
        n, c0 = NSITES, C0
        nd_kink = n - c0
        nd_event = nd_kink + 1
        q = DELTA - math.sqrt(DELTA * DELTA - 1.0)
        st_k, ix_k = sector_basis(n, nd_kink)
        st_e, ix_e = sector_basis(n, nd_event)
        hk_k = hamiltonian(st_k, ix_k, n, DELTA, True)
        hk_e = hamiltonian(st_e, ix_e, n, DELTA, True)
        hx_e = hamiltonian(st_e, ix_e, n, DELTA, False)
        dressed = kink_product_vector(st_k, n, q, 1.0)
        psi0 = lower_packet(dressed.astype(complex), st_k, ix_e,
                            n, K0, Y0, SIG)
        self.env = dict(
            n=n, c0=c0, q=q, st_k=st_k, ix_k=ix_k, st_e=st_e, ix_e=ix_e,
            hk_k=hk_k, hk_e=hk_e, hx_e=hx_e,
            sz_k=sz_table(st_k, n), sz_e=sz_table(st_e, n),
            dressed=dressed, psi0=psi0,
        )
        self._pk = None
        self._px = None

    @property
    def pk(self):
        if self._pk is None:
            self._pk = Propagator(self.env["hk_e"])
        return self._pk

    @property
    def px(self):
        if self._px is None:
            self._px = Propagator(self.env["hx_e"])
        return self._px


class Ledger:
    def __init__(self, quiet=False):
        self.rows = []
        self.quiet = quiet

    def add(self, row, ok, msg):
        self.rows.append((row, bool(ok), msg))
        if not self.quiet:
            print(f"  [{'PASS' if ok else 'FAIL'}] {row}: {msg}")

    def failed(self):
        return [row for row, ok, _ in self.rows if not ok]


def spectral_blocks(qvals):
    return [(q, np.where(np.abs(qvals - q) < 1.0e-9)[0])
            for q in np.unique(qvals)]


def tpm_law(prop, psi_tm, q_w, blocks, tau):
    law, etas = {}, []
    for q, idx in blocks:
        xi = np.zeros_like(psi_tm)
        xi[idx] = psi_tm[idx]
        if np.linalg.norm(xi) < 1.0e-14:
            continue
        eta = prop.evolve(xi, tau)
        etas.append((q, eta))
        weights = np.abs(eta) ** 2
        for qp, jdx in blocks:
            weight = float(weights[jdx].sum())
            if weight > 0.0:
                nu = float(q - qp)
                law[nu] = law.get(nu, 0.0) + weight
    return law, etas


def charges(env, a, b):
    return window_charges(env["sz_e"], env["n"], env["c0"], a, b)


def two_site_operators(delta, field_scale=1.0):
    sz_l = np.diag([0.5, 0.5, -0.5, -0.5])
    sz_r = np.diag([0.5, -0.5, 0.5, -0.5])
    flip = np.zeros((4, 4))
    flip[1, 2] = flip[2, 1] = 1.0
    h_xxz = -J * (0.5 * flip + delta * (sz_l @ sz_r - 0.25 * np.eye(4)))
    cfield = 0.5 * J * math.sqrt(delta * delta - 1.0) * field_scale
    h_kink = h_xxz - cfield * (sz_l - sz_r)
    p_dw = np.diag([0.0, 1.0, 1.0, 0.0])
    return h_xxz, h_kink, p_dw


def row_c1(ctx, led, mode):
    env = ctx.env
    q_w, _, _ = charges(env, 4, 9)
    if mode == "c1-noninteger":
        q_w = q_w + 0.3
    blocks = spectral_blocks(q_w)
    prop = (ScaledPropagator(ctx.pk, 1.37)
            if mode == "c1-nonunitary" else ctx.pk)
    psi_tm = prop.evolve(env["psi0"], -8.0)
    law, _ = tpm_law(prop, psi_tm, q_w, blocks, 11.0)
    norm_err = abs(sum(law.values()) - 1.0)
    led.add(R_C1A, norm_err < TOL_PROB,
            f"|sum p - 1| = {norm_err:.2e}")

    raw_err = float(np.max(np.abs(q_w - np.rint(q_w))))
    nu_err = max(abs(nu - round(nu)) for nu in law)
    allowed = [x - y for x, _ in blocks for y, _ in blocks]
    supp_ok = all(any(abs(nu - candidate) < TOL_EXACT for candidate in allowed)
                  for nu in law)
    led.add(R_C1B, raw_err < TOL_EXACT and nu_err < TOL_EXACT and supp_ok,
            f"max dist(spec Q_W,Z) = {raw_err:.2e}; "
            f"max dist(nu,Z) = {nu_err:.2e}; |support| = {len(law)}")


def row_c2(ctx, led, mode):
    env, prop = ctx.env, ctx.pk
    a, b = WINDOWS[0]
    q_w, q_wc, _ = charges(env, a, b)
    blocks = spectral_blocks(q_w)
    r_w = max(env["c0"] - a + 1, b - env["c0"])
    calq0 = float(q_w[0] + q_wc[0])

    eq_worst = 0.0
    for t in (-9.0, -2.0, 5.0):
        psi_t = prop.evolve(env["psi0"], t)
        tau = 0.25 if mode == "c2-unequal-time" else 0.0
        _, etas = tpm_law(prop, psi_t, q_w, blocks, tau)
        defect = sum(float(np.vdot(eta, q_w * eta).real) for _, eta in etas)
        defect -= float(np.vdot(psi_t, q_w * psi_t).real)
        eq_worst = max(eq_worst, abs(defect))
    led.add(R_C2A, eq_worst < TOL_IDENT,
            f"max |Delta_W(t,t)| = {eq_worst:.2e}")

    bound_factor = 0.05 if mode == "c2-small-constant" else 4.0
    bound_worst = -1.0e9
    for tm in (-9.0, -5.0, -2.0):
        psi_tm = prop.evolve(env["psi0"], tm)
        weights = np.abs(psi_tm) ** 2
        eps2 = 1.0 - float(weights[np.abs(q_w - calq0) < 1.0e-9].sum())
        eps = math.sqrt(max(eps2, 0.0))
        for tp in (2.0, 6.0, 11.0):
            _, etas = tpm_law(prop, psi_tm, q_w, blocks, tp - tm)
            defect = sum(float(np.vdot(eta, q_w * eta).real)
                         for _, eta in etas)
            psi_tp = prop.evolve(env["psi0"], tp)
            defect -= float(np.vdot(psi_tp, q_w * psi_tp).real)
            bound_worst = max(bound_worst,
                              abs(defect) - bound_factor * r_w * eps)
    led.add(R_C2B, bound_worst <= TOL_IDENT,
            f"max slack = {bound_worst:+.3e} (factor {bound_factor:g})")

    if mode == "c2-mismatched-complement":
        _, q_wc, _ = charges(env, a - 1, b + 1)
    sharp_worst = -1.0e9
    for tm in (-9.0, -5.0, -2.0):
        psi_tm = prop.evolve(env["psi0"], tm)
        weights = np.abs(psi_tm) ** 2
        eps2 = 1.0 - float(weights[np.abs(q_w - calq0) < 1.0e-9].sum())
        qwc2 = float((weights * q_wc ** 2).sum())
        sharp_worst = max(sharp_worst, eps2 - qwc2)
    led.add(R_C2C, sharp_worst <= TOL_IDENT,
            f"max [eps^2-<Q_Wc^2>] = {sharp_worst:+.3e}")

    times = np.linspace(-40.0, 40.0, 201)
    evolved = prop.evolve_many(env["psi0"], times)
    probs = np.abs(evolved) ** 2
    profile, etas = [], []
    for (wa, wb) in WINDOWS:
        _, _, n_w = charges(env, wa, wb)
        if mode == "c2-delete-outside-data":
            n_w = np.zeros_like(n_w)
        g_m = float(np.max(((n_w ** 2)[:, None] * probs).sum(axis=0)))
        radius = max(env["c0"] - wa + 1, wb - env["c0"])
        profile.append(g_m)
        etas.append(4.0 * radius * math.sqrt(g_m))
    order_ok = all(etas[i + 1] > etas[i] + 1.0 for i in range(len(etas) - 1))
    led.add(R_C2D, min(profile) > 0.90 and order_ok,
            "G = " + ", ".join(f"{x:.3f}" for x in profile)
            + "; eta = " + ", ".join(f"{x:.1f}" for x in etas))


def independent_matrix_identity(mode):
    """Compute (LRD.11) by a route independent of tpm_law's regrouping."""
    n, c0, nd_kink = 8, 4, 4
    st_k, _ = sector_basis(n, nd_kink)
    st_e, ix_e = sector_basis(n, nd_kink + 1)
    q = DELTA - math.sqrt(DELTA * DELTA - 1.0)
    dressed = kink_product_vector(st_k, n, q, 1.0)
    psi0 = lower_packet(dressed.astype(complex), st_k, ix_e,
                        n, K0, 2.5, 1.1)
    h = hamiltonian(st_e, ix_e, n, DELTA, True)
    prop = Propagator(h)
    sz = sz_table(st_e, n)
    q_w, _, _ = window_charges(sz, n, c0, 3, 6)
    blocks = spectral_blocks(q_w)
    tm, tp = -4.0, 3.0
    psi_tm = prop.evolve(psi0, tm)
    law, _ = tpm_law(prop, psi_tm, q_w, blocks, tp - tm)
    lhs = sum(nu * nu * weight for nu, weight in law.items())

    u_m, u_p = prop.matrix(tm), prop.matrix(tp)
    q_diag = np.diag(q_w)
    q_tm = u_m.T.conj() @ q_diag @ u_m
    q_tp = u_p.T.conj() @ q_diag @ u_p
    if mode == "c3-perturb-final-evolution":
        q_tp = q_tp + 0.25 * np.diag(np.linspace(-1.0, 1.0, len(q_w)))
    delta_q = q_tp - q_tm
    rhs = 0.0
    for _, idx in blocks:
        mask = np.zeros(len(q_w))
        mask[idx] = 1.0
        p_tm = u_m.T.conj() @ np.diag(mask) @ u_m
        xi = p_tm @ psi0
        rhs += float(np.vdot(delta_q @ xi, delta_q @ xi).real)
    return lhs, rhs


def pinched_terms(env, prop, tm, tp, freeze=False):
    _, _, n_w1 = charges(env, *WINDOWS[0])
    psi_tm = prop.evolve(env["psi0"], tm)
    saved = None
    out = []
    for a, b in WINDOWS:
        q_w, _, _ = charges(env, a, b)
        _, etas = tpm_law(prop, psi_tm, q_w, spectral_blocks(q_w), tp - tm)
        if saved is None:
            saved = etas
        used = saved if freeze else etas
        out.append(2.0 * sum(float((np.abs(eta) ** 2 * n_w1 ** 2).sum())
                             for _, eta in used))
    return out


def row_c3(ctx, led, mode):
    env, prop = ctx.env, ctx.pk
    lhs_m, rhs_m = independent_matrix_identity(mode)
    matrix_err = abs(lhs_m - rhs_m)
    led.add(R_C3A, matrix_err < TOL_IDENT,
            f"TPM = {lhs_m:.10f}, pinched matrix = {rhs_m:.10f}, "
            f"|diff| = {matrix_err:.2e}")

    _, q_wc1, n_w1 = charges(env, *WINDOWS[0])
    mono_majorant = q_wc1 if mode == "c3-signed-majorant" else n_w1
    mono_worst = -1.0e9
    for i in range(len(WINDOWS) - 1):
        _, qci, nwi = charges(env, *WINDOWS[i])
        _, qcj, nwj = charges(env, *WINDOWS[i + 1])
        left = qci if mode == "c3-signed-majorant" else nwi
        right = qcj if mode == "c3-signed-majorant" else nwj
        mono_worst = max(mono_worst, float(np.max(right - left)))
    dominance = float(np.max(np.abs(q_wc1) - mono_majorant))
    led.add(R_C3C, mono_worst <= TOL_PSD and dominance <= TOL_PSD,
            f"max next-prev = {mono_worst:+.3f}; max |Q_Wc|-majorant = {dominance:+.3f}")

    split_worst, majorant_worst = -1.0e9, -1.0e9
    for tm in (-8.0, -3.0):
        psi_tm = prop.evolve(env["psi0"], tm)
        w_tm = np.abs(psi_tm) ** 2
        majorant = (np.zeros_like(n_w1)
                    if mode == "c3-delete-majorant" else n_w1)
        fixed_first = 2.0 * float((w_tm * majorant ** 2).sum())
        for tp in (3.0, 9.0):
            for a, b in WINDOWS:
                q_w, q_wc, _ = charges(env, a, b)
                if mode == "c3-mismatched-complement":
                    _, q_wc, _ = charges(env, a - 1, b + 1)
                law, etas = tpm_law(prop, psi_tm, q_w,
                                    spectral_blocks(q_w), tp - tm)
                second_moment = sum(nu * nu * weight for nu, weight in law.items())
                first = 2.0 * float((w_tm * q_wc ** 2).sum())
                second = 2.0 * sum(float((np.abs(eta) ** 2 * q_wc ** 2).sum())
                                   for _, eta in etas)
                fixed_second = 2.0 * sum(
                    float((np.abs(eta) ** 2 * majorant ** 2).sum())
                    for _, eta in etas)
                split_worst = max(split_worst, second_moment - first - second)
                majorant_worst = max(majorant_worst,
                                      second_moment - fixed_first - fixed_second)
    led.add(R_C3B, split_worst <= TOL_IDENT,
            f"max slack = {split_worst:+.3e}")
    led.add(R_C3D, majorant_worst <= TOL_IDENT,
            f"max slack = {majorant_worst:+.3e}")

    terms = pinched_terms(env, prop, -8.0, 9.0,
                          freeze=(mode == "c3-freeze-pinching"))
    spread = max(terms) - min(terms)
    increasing = all(terms[i + 1] > terms[i] + 0.03
                     for i in range(len(terms) - 1))
    led.add(R_C3E, spread > 0.40 and increasing,
            "2 sum ||N_W1 eta_q^(m)||^2 = "
            + " / ".join(f"{x:.3f}" for x in terms)
            + f"; spread = {spread:.3f}")


def row_c4(ctx, led, mode):
    env = ctx.env
    h_xxz, _, p_dw = two_site_operators(DELTA)
    constant = 0.5 * J * ((DELTA + 1.0)
                          if mode == "c4-wrong-gap" else (DELTA - 1.0))
    min_eig = float(np.linalg.eigvalsh(h_xxz - constant * p_dw).min())
    led.add(R_C4A, min_eig >= -TOL_PSD,
            f"min eig = {min_eig:+.3e}; constant = {constant:.4f}")

    prop = ctx.pk if mode == "c4-kink-propagator" else ctx.px
    dvals = dw_number(env["sz_e"])
    e0 = float(np.vdot(env["psi0"], env["hx_e"] @ env["psi0"]).real)
    bound = e0 / (0.5 * J * (DELTA - 1.0))
    energy_drift, inequality_slack, dmax = 0.0, -1.0e9, 0.0
    for t in np.linspace(-12.0, 12.0, 17):
        psi_t = prop.evolve(env["psi0"], t)
        energy = float(np.vdot(psi_t, env["hx_e"] @ psi_t).real)
        dcount = float((np.abs(psi_t) ** 2 * dvals).sum())
        energy_drift = max(energy_drift, abs(energy - e0))
        inequality_slack = max(inequality_slack, dcount - bound)
        dmax = max(dmax, dcount)
    led.add(R_C4B, energy_drift < TOL_IDENT and inequality_slack <= TOL_PSD,
            f"max energy drift = {energy_drift:.3e}; max <D> = {dmax:.3f} "
            f"<= {bound:.3f}; slack = {inequality_slack:+.3e}")

    vector = (sharp_kink_vector(env["st_k"], env["ix_k"], env["n"], env["c0"])
              if mode == "c4-sharp-calibration" else env["dressed"])
    hx_k = hamiltonian(env["st_k"], env["ix_k"], env["n"], DELTA, False)
    energy = float(vector @ hx_k @ vector)
    c_k = 0.5 * J * math.sqrt(DELTA * DELTA - 1.0)
    calibration_err = abs(energy - c_k)
    led.add(R_C4C, calibration_err < 5.0e-7,
            f"<K|H_XXZ|K> = {energy:.10f}; C_K = {c_k:.10f}; "
            f"|diff| = {calibration_err:.2e}")


def row_c5(ctx, led, mode):
    q = (DELTA + math.sqrt(DELTA * DELTA - 1.0)
         if mode == "c5-wrong-root" else ctx.env["q"])
    _, h_kernel, _ = two_site_operators(DELTA)
    _, h_psd, _ = two_site_operators(
        DELTA, field_scale=(1.10 if mode == "c5-overstrong-field" else 1.0))
    residuals = []
    for z in (0.4, 1.0, 2.0):
        left = z * q ** -4
        right = z * q ** -5
        local = np.array([1.0, right, left, left * right])
        residuals.append(float(np.linalg.norm(h_kernel @ local)
                               / np.linalg.norm(local)))
    led.add(R_C5A, max(residuals) < TOL_EXACT,
            f"max normalised local residual = {max(residuals):.2e}")
    min_eig = float(np.linalg.eigvalsh(h_psd).min())
    led.add(R_C5B, min_eig >= -TOL_PSD,
            f"min eig h_kink = {min_eig:+.3e}")


def row_c6(ctx, led, mode):
    env = ctx.env
    dressed = env["dressed"]
    sharp = sharp_kink_vector(env["st_k"], env["ix_k"], env["n"], env["c0"])
    if mode == "c6-identify-sharp-dressed":
        sharp = dressed.copy()
    overlap = abs(float(np.dot(dressed, sharp))) ** 2
    energy = float(sharp @ env["hk_k"] @ sharp)
    led.add(R_C6A, overlap < 0.999 and energy > 1.0e-3,
            f"|<sharp|dressed>|^2 = {overlap:.4f}; E_kink(sharp) = {energy:.4f}")


ROW_FUNCS = {
    "c1": row_c1,
    "c2": row_c2,
    "c3": row_c3,
    "c4": row_c4,
    "c5": row_c5,
    "c6": row_c6,
}


def run(ctx, mode="green", group=None, quiet=False):
    led = Ledger(quiet=quiet)
    groups = [group] if group else list(ROW_FUNCS)
    for name in groups:
        ROW_FUNCS[name](ctx, led, mode)
    return led


def red_result(ctx, mode, quiet=False):
    target = RED_TARGETS[mode]
    led = run(ctx, mode=mode, group=ROW_GROUP[target], quiet=quiet)
    failed = led.failed()
    exact = failed == [target]
    return exact, failed


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--red", choices=sorted(RED_TARGETS))
    parser.add_argument("--red-all", action="store_true")
    args = parser.parse_args(argv)

    print(f"lr_d16_check r2: J={J}, Delta={DELTA}, N={NSITES}, c0={C0}")
    ctx = Context()
    if args.red_all:
        all_ok = True
        print("red reachability table (each mode evaluates its target group directly):")
        for mode, target in RED_TARGETS.items():
            exact, failed = red_result(ctx, mode, quiet=True)
            all_ok = all_ok and exact
            path = ", ".join(failed) if failed else "NONE"
            print(f"  {mode:29s} -> {path}"
                  + ("" if exact else f" (EXPECTED exactly {target})"))
        if all_ok:
            print(f"\nRED-OK: {len(RED_TARGETS)}/{len(RED_TARGETS)} specific "
                  "mutants reached exactly their registered rows.")
            return 1
        print("\nRED-MISSED: at least one target was unreachable or nonspecific.")
        return 2

    if args.red:
        exact, failed = red_result(ctx, args.red)
        path = ", ".join(failed) if failed else "NONE"
        if exact:
            print(f"\nRED-OK ({args.red}): exit path = {path}")
            return 1
        print(f"\nRED-MISSED ({args.red}): exit path = {path}; expected exactly "
              f"{RED_TARGETS[args.red]}")
        return 2

    led = run(ctx)
    failed = led.failed()
    if failed:
        print(f"\nFAIL: {len(failed)} row(s): {', '.join(failed)}")
        return 1
    print(f"\nPASS: all {len(led.rows)} rows green; every row has a registered mutant.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
