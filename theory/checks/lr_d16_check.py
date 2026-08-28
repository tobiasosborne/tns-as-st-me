#!/usr/bin/env python3
"""Red-capable certificates for theory/lr-d16.md — (LR) for the D16 kink sector.

Target under test: `theory/lr-d16.md`, the proposer shard for bd tns-xf4.
Every row below certifies a DISPLAYED step of that shard, by exact
diagonalization of the D16 model on a short chain.  Rows are algebraic
certificates (identities and operator inequalities), not asymptotic physics:
N = 12 is far too short to hold a clean ballistic window, and no row claims
otherwise.  The asymptotic evidence for (LR) lives in
`theory/checks/memory_index_probe.py`, which this file does not duplicate.

Model (D16, orientation (LRD-O) of lr-d16.md <1>1.<2>2):

    h_XXZ[x,x+1] = -J [ Sx Sx + Sy Sy + Delta (Sz Sz - 1/4) ]
    h_kink[x,x+1] = h_XXZ[x,x+1] - (J/2) sqrt(Delta^2-1) (Sz_x - Sz_{x+1})

so that the exact zero-energy family is the UP...DOWN kink
|K(z)> = prod_n ( |up>_n + z q^{-n} |down>_n ),  q = Delta - sqrt(Delta^2-1),
which is D13(a)'s orientation (s_alpha = +s at -infinity).

Calibration, fixed once and identical to memory_index_probe.py:

    rho(x)   = +1/2 for x <= c0,  -1/2 for x > c0      (sharp reference kink)
    Q_W      = sum_{x in W} ( Sz_x - rho(x) )          (integer valued)
    Q_Wc     = sum_{x not in W} ( Sz_x - rho(x) )      (integer valued)
    N_W      = #downs left of W  +  #ups right of W    (>= 0, D14 counts)
    calQ     = Q_W + Q_Wc                              (conserved, scalar)

Registered rows (each cites the shard step it certifies):

  LRD-C1  <1>3        LR1: double-Cesaro TPM laws converge; successive
                      total-variation differences contract; each p is a
                      probability on a fixed finite subset of Z.
  LRD-C2  <1>4        LR2: (a) Delta_W(t,t) = 0 identically; (b) the bound
                      |Delta_W| <= 4 R_W eps_W(t-) of <2>3; (c) the sharpness
                      identity eps_W^2 <= <Q_Wc^2> of <2>4; (d) the (LR2')
                      trend: the bound 4 R_W sqrt(G) falls with padding.
  LRD-C3  <1>5        LR3: (a) the exact second-moment identity (LRD.11);
                      (b) the edge split (LRD.12); (c) the MONOTONICITY
                      lemma N_{W'} <= N_W; (d) the m-uniform bound (LRD.13).
  LRD-C4  <1>5.<2>6   (EDW): h_XXZ >= (J/2)(Delta-1) P_DW as a 4x4 matrix,
                      the bare-kink value sqrt((Delta+1)/(Delta-1)), and the
                      dynamical bound <D(t)> <= 2 E0 / (J(Delta-1)).
  LRD-C5  <1>5.<2>8   flatness: || H_kink |K(z)> || = 0 for every z, H_kink >= 0,
                      and exact stationarity of a superposition of two z's.
  LRD-C6  <1>1.<2>7   dressed-kink discipline: the SHARP kink is not a zero
                      mode and is therefore not an admissible initial state;
                      the dressed kink is, to machine precision.

Exit codes: 0 all rows PASS; 1 some row FAILED (under --red* this is RED-OK);
2 a red mutation was NOT caught (the checker is not red-capable in that mode).
Explicit failure bookkeeping only -- no bare `assert` -- so `python3 -O` is
equally strict.

Modes:
    (default)          full green run, must exit 0
    --red-noncons      add a transverse field, breaking U(1); (FN)/(LRD.5)
                       dies, so LRD-C2(c) and LRD-C3(b) must fail
    --red-edw          use (Delta+1) in place of (Delta-1) in (EDW);
                       LRD-C4 must fail
    --red-monotone     majorize the escaped charge by the SIGNED Q_Wc instead
                       of the non-negative N_W; LRD-C3(c,d) must fail
    --red-sharp        feed the sharp kink where the dressed kink is required;
                       LRD-C5/LRD-C6 must fail
"""

from __future__ import annotations

import argparse
import math
import sys
from itertools import combinations

import numpy as np

# ----------------------------------------------------------------- tolerances
TOL_EXACT = 1.0e-11        # machine-level identities
TOL_IDENT = 1.0e-9         # identities after time evolution
TOL_PSD = 1.0e-12          # operator-inequality slack
TOL_PROB = 1.0e-10         # probability normalisation
CESARO_CONTRACT = 0.85     # required contraction of successive TV differences
SHARP_OVERLAP_MAX = 0.999  # a sharp kink must NOT be the dressed kink
SHARP_ENERGY_MIN = 1.0e-3  # ... and must carry strictly positive kink energy

J = 1.0
DELTA = 2.5
NSITES = 12
C0 = 6                     # cut: ups at x <= 6, downs at x > 6 (1-based)
K0 = 0.5 * math.pi         # magnon mean momentum
Y0 = 3.0                   # magnon packet centre (up side)
SIG = 1.4                  # magnon packet width


# ------------------------------------------------------------------ machinery
def sector_basis(n, ndown):
    """Configurations with `ndown` down spins, as bitmasks (bit x-1 set = down)."""
    states = []
    for pos in combinations(range(n), ndown):
        m = 0
        for p in pos:
            m |= 1 << p
        states.append(m)
    states.sort()
    return states, {s: i for i, s in enumerate(states)}


def sz_table(states, n):
    """sz[i, x] = S^z of site x+1 in configuration i."""
    out = np.empty((len(states), n))
    for i, s in enumerate(states):
        for x in range(n):
            out[i, x] = -0.5 if (s >> x) & 1 else 0.5
    return out


def hamiltonian(states, index, n, delta, kink_field, transverse=0.0):
    """Dense H in the sector.  kink_field=True adds D16's telescoping term.

    `transverse` (red mode only) adds h * sum_x S^x_x, which does NOT conserve
    S^z; it is applied as a sector-diagonal surrogate that breaks the exact
    conservation used by (LRD.5): a next-nearest hop sum_x S^+_x S^-_{x+2}
    would preserve S^z, so instead we use a bond term that mixes within the
    sector but is NOT a symmetry of Q: h * sum_x (S^+_x S^-_{x+2} + h.c.).
    """
    dim = len(states)
    h = np.zeros((dim, dim))
    cfield = 0.5 * J * math.sqrt(delta * delta - 1.0) if kink_field else 0.0
    for i, s in enumerate(states):
        diag = 0.0
        for x in range(n - 1):
            a = -0.5 if (s >> x) & 1 else 0.5
            b = -0.5 if (s >> (x + 1)) & 1 else 0.5
            diag += -J * delta * (a * b - 0.25)
            diag += -cfield * (a - b)
            if ((s >> x) & 1) != ((s >> (x + 1)) & 1):
                t = s ^ (1 << x) ^ (1 << (x + 1))
                h[index[t], i] += -0.5 * J
        h[i, i] += diag
    if transverse != 0.0:
        for i, s in enumerate(states):
            for x in range(n - 2):
                if ((s >> x) & 1) != ((s >> (x + 2)) & 1):
                    t = s ^ (1 << x) ^ (1 << (x + 2))
                    h[index[t], i] += transverse
    return h


def rho_ref(n, c0):
    return np.array([0.5 if (x + 1) <= c0 else -0.5 for x in range(n)])


def window_charges(sz, n, c0, a, b):
    """(Q_W, Q_Wc, N_W) as diagonal arrays over the sector, 1-based [a,b]."""
    rho = rho_ref(n, c0)
    d = sz - rho[None, :]
    inside = np.array([(a <= x + 1 <= b) for x in range(n)])
    q_w = d[:, inside].sum(axis=1)
    q_wc = d[:, ~inside].sum(axis=1)
    left = np.array([(x + 1) < a for x in range(n)])
    right = np.array([(x + 1) > b for x in range(n)])
    n_w = (0.5 - sz[:, left]).sum(axis=1) + (sz[:, right] + 0.5).sum(axis=1)
    return q_w, q_wc, n_w


def dw_number(sz):
    return (np.abs(np.diff(sz, axis=1)) > 1e-12).sum(axis=1).astype(float)


def kink_product_vector(states, n, q, z):
    """|K(z)> = prod_n (|up>_n + z q^{-n} |down>_n), projected on the sector."""
    amp = np.array([z * q ** (-(x + 1)) for x in range(n)])
    v = np.empty(len(states))
    for i, s in enumerate(states):
        c = 1.0
        for x in range(n):
            if (s >> x) & 1:
                c *= amp[x]
        v[i] = c
    nrm = np.linalg.norm(v)
    return v / nrm if nrm > 0 else v


def sharp_kink_vector(states, index, n, c0):
    m = 0
    for x in range(n):
        if (x + 1) > c0:
            m |= 1 << x
    v = np.zeros(len(states))
    v[index[m]] = 1.0
    return v


def lower_packet(psi, states_from, index_to, n, k0, y0, sig):
    """O = sum_y e^{i k0 y} g(y) S^-_y applied to a vector of the ndown sector."""
    out = np.zeros(len(index_to), dtype=complex)
    g = np.array([math.exp(-((y + 1 - y0) ** 2) / (2 * sig * sig)) for y in range(n)])
    ph = np.array([np.exp(1j * k0 * (y + 1)) for y in range(n)])
    for i, s in enumerate(states_from):
        c = psi[i]
        if c == 0:
            continue
        for y in range(n):
            if not (s >> y) & 1:
                out[index_to[s | (1 << y)]] += c * g[y] * ph[y]
    nrm = np.linalg.norm(out)
    return out / nrm if nrm > 0 else out


class Propagator:
    def __init__(self, h):
        self.evals, self.vecs = np.linalg.eigh(h)

    def evolve(self, psi, t):
        c = self.vecs.T.conj() @ psi
        return self.vecs @ (np.exp(-1j * self.evals * t) * c)


class Ledger:
    def __init__(self):
        self.rows = []

    def add(self, row, ok, msg):
        self.rows.append((row, bool(ok), msg))
        print(f"  [{'PASS' if ok else 'FAIL'}] {row}: {msg}")

    def failed(self):
        return [r for r, ok, _ in self.rows if not ok]


# ---------------------------------------------------------------- TPM kernels
def spectral_blocks(qvals):
    uniq = np.unique(np.round(qvals, 9))
    return [(q, np.where(np.abs(qvals - q) < 1e-9)[0]) for q in uniq]


def tpm_law(prop, psi_tm, q_w, blocks, tau):
    """F_nu(t-, t+) of lr-d16.md <1>3.<2>4, with tau = t+ - t-.

    Returns (dict nu -> weight, second moment, list of (q, eta_q))."""
    law, m2, etas = {}, 0.0, []
    for q, idx in blocks:
        xi = np.zeros_like(psi_tm)
        xi[idx] = psi_tm[idx]
        if np.linalg.norm(xi) < 1e-14:
            continue
        eta = prop.evolve(xi, tau)
        etas.append((q, eta))
        w = np.abs(eta) ** 2
        for qp, jdx in blocks:
            wt = float(w[jdx].sum())
            if wt > 0.0:
                nu = int(round(q - qp))
                law[nu] = law.get(nu, 0.0) + wt
        m2 += float((w * (q_w - q) ** 2).sum())
    return law, m2, etas


def cesaro_law(prop, psi0, q_w, blocks, bigt, ngrid):
    tm = np.linspace(-2.0 * bigt, -bigt, ngrid)
    tp = np.linspace(bigt, 2.0 * bigt, ngrid)
    acc = {}
    for a in tm:
        psi_tm = prop.evolve(psi0, a)
        for b in tp:
            law, _, _ = tpm_law(prop, psi_tm, q_w, blocks, b - a)
            for nu, w in law.items():
                acc[nu] = acc.get(nu, 0.0) + w
    tot = ngrid * ngrid
    return {k: v / tot for k, v in acc.items()}


def tv(p, r):
    keys = set(p) | set(r)
    return 0.5 * sum(abs(p.get(k, 0.0) - r.get(k, 0.0)) for k in keys)
