#!/usr/bin/env python3
"""Deterministic certificates for Theorem M-INDEX (theory/memory-index.md §7).

Companion to ``theory/checks/memory_index_probe.py``, which covers the
dynamical ED probe (P1--P5).  This file covers the symbolic / small-matrix
certificates IDX-C1 -- IDX-C8 of the consolidated checker spec, as ten
registered rows (see the red-mode note).  Every check
raises ``SystemExit(1)`` on violation, so all of them remain active under
``python3 -O``; there is not a single bare ``assert``.

    IDX-C1      finite-window coset offset and the TPM law  (<1>1, <1>5, <1>6)
    IDX-C2      two-time dephasing defect + the L1 landmine  (<1>6, §6 L1)
    IDX-C3      mechanism-A counterexample                   (<1>3, IDX-CE.4-.7)
    IDX-C4      weak limit does not give a first moment      (§6 L2)
    IDX-C5      M-quant-G reduction                          (<1>8)
    IDX-C6      IT phase slope = tail density                (<1>9, IDX-rho.1)
    IDX-C7(i)   exact conjugation and identically zero offset (<1>9--<1>11)
    IDX-C7(ii)  necessity of the antisymmetric tail pair     (<1>9.<2>4)
    IDX-C8      vacuum charge law and the nonscalar obstruction (<1>11, <1>12)
    IDX-C8rho   the IDX-rho.6 truncation inequality          (<1>11.<2>3)

Red mode
--------
Every row of the CHECK TABLE carries exactly ONE named mutation.  ``--red``
applies all of them at once, each *in place of* the premise it breaks, and
every row must then fail.  Where the spec attaches two mutations to one
certificate they are registered as two rows, so that each is independently
reachable in red: that is r2 objection 3(c)(i), which found IDX-C7's
mutation (ii) sitting as dead code behind mutation (i)'s eager failure, and
3(c)(iii), which found the IDX-rho.6 assertion vacuous inside IDX-C8.

    C1/C2      naive unmeasured difference <Q(t-)> - <Q(t+)> for (IDX.4)
    C3         eps_n -> (n+1)^{-1}, which makes V_N bounded
    C4         assert first-moment convergence from bare tightness
    C5         transmitted escaped charge 2 -> 1
    C6         one tensor entry moved to a forbidden charge slot
    C7(i)      counterterm rho -> rho + RED_SHIFT, RED_SHIFT irrational
    C7(ii)     the antisymmetric tail pair of <1>9.<2>4 withdrawn, with the
               counterterms held at the CORRECT (rho, -rho)
    C8         the limit |tr(V_theta r)|^2 replaced by |tr V_theta|^2/chi^2
    C8rho      the IDX-rho.6 truncation threshold 2/u -> 1/u

The red run prints RED-OK and exits 1 when every mutation was caught, and
exits 2 if any mutation survived (the checker would not be red-capable).

Spec deviations are recorded in the module-level list SPEC_NOTES and printed
at the end of a green run.
"""

from __future__ import annotations

import argparse
import sys

import numpy as np
import sympy as sp
from scipy.special import gammaln

# --------------------------------------------------------------- constants --
CHI = 2
SPIN32 = np.array([-1.5, -0.5, 0.5, 1.5])
SPIN2 = np.array([-2.0, -1.0, 0.0, 1.0, 2.0])
AKLT_SPINS = np.array([-1.0, 0.0, 1.0])
TOL_EXACT = 1.0e-12
TOL_CONJ = 1.0e-13
TOL_LIVE = 1.0e-6
MPS_SEED = 6
DRAW_SEED = 7
TPM_SEED = 20260828
RED_SHIFT = (np.sqrt(5.0) - 1.0) / 10.0     # irrational; see SPEC NOTE 7
KAPPA = np.sqrt(2.0) - 1.0                  # irrational charge shift
NC_SCALE = 0.8                              # forbidden-slot amplitude, C7(ii)

SPEC_NOTES = [
    "IDX-C7(i): for the symmetric windows [-n,n] of the spec the counterterm "
    "shift rho -> rho+delta gives |phi_W(2pi)-1| = Theta(1) but is "
    "n-INDEPENDENT -- the only window datum that survives is "
    "n_L - n_R = 2c+1, which carries no n.  The spec's 'drifting with n' is "
    "reproduced on the asymmetric family [-n,2n], where n_L - n_R = 1-n.",
    "IDX-C7(ii), the <1>9.<2>4 two-tail mutation, rebuilt in the form r2 "
    "objection 3(c)(i) demands: counterterms held at the CORRECT (rho,-rho), "
    "only the beta tail broken.  Two facts fix what is implementable.  (1) A "
    "charge-diagonal tensor of density -rho+0.2 does not exist in a fixed "
    "physical space: m = rho_b + w_j - w_i with w_j - w_i in Z forces "
    "rho_b = rho_a mod 1.  (2) Under D26(INT), phi_W(2pi) is tensor-"
    "INDEPENDENT: every physical charge has the same e^{2 pi i m} = c, so "
    "each twisted site factor is the scalar c e^{-2 pi i ct} times the plain "
    "one and phi_W(2pi) is a product of scalars -- perturbing the tensor "
    "alone can never move it.  The check therefore carries two prongs, both "
    "at the correct counterterm.  Prong (a), tensor-level and gauge "
    "invariant: the beta-tail twisted transfer at counterterm -rho has "
    "leading eigenvalue exactly 1 iff that tail is covariant with density "
    "-rho (E^{ct} = L_{V^-1} . E . L_V is then a similarity transform of E), "
    "run on three tails -- the true one, a non-covariant one of density "
    "-rho+0.2, and a non-covariant one of density EXACTLY -rho, which "
    "isolates covariance from the density.  Prong (b) withdraws the "
    "antisymmetry itself on a family where the conclusion 2 rho in Z fails: "
    "shifting the common on-site charge by kappa keeps (INT) and keeps both "
    "tails covariant under the same u, but the covariant partner realisable "
    "in that physical space has density -rho+2kappa, not -rho.  Then "
    "phi_W(2pi) = e^{4 pi i rho n_R} at the correct (rho,-rho): Theta(1), "
    "window-dependent, and exactly the failure of 2 rho in Z.",
    "IDX-C1: 'offset cancellation at irrational s' is implemented by shifting "
    "S^z by an irrational constant (kappa = sqrt(2)-1), which keeps D26(INT) "
    "and puts the window spectrum in an irrational coset; the TPM increments "
    "stay in Z.  The site spin itself is left half-integral.",
    "IDX-C8: the 'wrong environment' mutation is vacuous on AKLT (r = 1/chi) "
    "and is therefore registered on the charged chi=2 draw, where r is not "
    "proportional to the identity.",
    "IDX-C8 deep-shell kink test: as literally specified it is vacuous when "
    "the beta tail is the spin-flipped alpha, since then r_beta = r_alpha and "
    "the contraction converges for a trivial reason.  Resolved by an "
    "independently drawn beta with a seeded invertible junction insertion "
    "(kink_partners), behind the explicit anti-vacuity guard "
    "|r_beta - r_alpha| > 1e-3.  Printed here for the first time: it lived "
    "only as that in-code guard (r2 objection 3(c)(ii)).",
    "IDX-C4: the spec asks the checker to REJECT first-moment convergence, so "
    "there is no premise to perturb -- the laws are hand-written arithmetic "
    "exhibits.  The mutation is therefore an INSERTED false assertion (red "
    "asserts the first moment converges to 0), not a perturbed premise, and "
    "IDX-C4 is evidence about the implication only, not about any model.  "
    "Printed here for the first time (r2 objection 3(c)(ii)).",
    "IDX-C7(i) red shift -- the checker half of r2 objection 9.  The spec's "
    "rho -> rho+0.1 is resonant with round window arithmetic: 0.1 against a "
    "multiplier of 10 is an exact integer and would leave that window "
    "silent, which is the defect objection 9 found in the probe's "
    "RED_RHO_SHIFT (0.3 x 10 sites = 3.0 exactly).  RED_SHIFT is the "
    "irrational (sqrt(5)-1)/10, coprime to every window width and cut offset "
    "by construction; IDX-C7(i) certifies dist(k*RED_SHIFT, Z) > 0.1 for "
    "every multiplier k the battery uses, and that no (window, cut) pair is "
    "silent under the mutation.",
]

SPEC_NOTE_LEDGER = (
    "Seven printed.  The a529a10 commit record claims six resolutions while "
    "four were printed; the audit of that file finds exactly six -- the four "
    "printed plus notes 5 and 6, which existed only as in-code devices (the "
    "deep-shell anti-vacuity guard and IDX-C4's inserted-assertion mutation) "
    "and are now printed.  Note 7 is new in the r3 repair."
)


class CheckFailure(Exception):
    """Raised by ``fail``; never caught outside ``run``, never optimised away."""


def fail(message: str) -> None:
    raise CheckFailure(message)


def require(condition: bool, message: str) -> None:
    if not condition:
        fail(message)


def exact_zero(expression: sp.Expr, message: str) -> None:
    residue = sp.simplify(expression)
    require(residue == 0, f"{message}: residue={residue}")


# ------------------------------------------------------------- MPS toolbox --

def transfer(tensors: list[np.ndarray]) -> np.ndarray:
    """Row-major vec matrix of E(Y) = sum_s A^s Y (A^s)^dag."""
    return sum(np.kron(a, a.conj()) for a in tensors)


def _top_fixed_point(matrix: np.ndarray) -> tuple[float, np.ndarray]:
    values, vectors = np.linalg.eig(matrix)
    index = int(np.argmax(np.abs(values)))
    block = vectors[:, index].reshape(CHI, CHI)
    trace = np.trace(block)
    require(abs(trace) > 1e-8, "fixed point is traceless; phase cannot be fixed")
    block = block / (trace / abs(trace))
    block = (block + block.conj().T) / 2
    if np.trace(block).real < 0:
        block = -block
    return float(values[index].real), block


def left_canonical(tensors: list[np.ndarray]) -> list[np.ndarray] | None:
    """Gauge to l = 1, i.e. sum_s (A^s)^dag A^s = 1."""
    lam, left = _top_fixed_point(transfer(tensors).conj().T)
    if np.linalg.eigvalsh(left).min() <= 1e-10 or lam <= 0:
        return None
    root = np.linalg.cholesky(left).conj().T
    inverse = np.linalg.inv(root)
    return [root @ a @ inverse / np.sqrt(lam) for a in tensors]


def right_environment(tensors: list[np.ndarray]) -> np.ndarray:
    _, right = _top_fixed_point(transfer(tensors))
    return right / np.trace(right).real


def transfer_gap(tensors: list[np.ndarray]) -> float:
    return float(np.sort(np.abs(np.linalg.eigvals(transfer(tensors))))[::-1][1])


def charge_diagonal(spins, rho, virtual, rng, forbidden=None):
    """Entry (i,j) is allowed only where the physical charge is rho+v_j-v_i."""
    tensors = [np.zeros((CHI, CHI), complex) for _ in spins]
    for i in range(CHI):
        for j in range(CHI):
            target = rho + virtual[j] - virtual[i]
            for k, charge in enumerate(spins):
                if abs(charge - target) < 1e-12:
                    tensors[k][i, j] = (rng.normal() + 1j * rng.normal()) / np.sqrt(2)
    if forbidden is not None:
        k, i, j, value = forbidden
        tensors[k][i, j] += value
    return tensors


def density(tensors, right, spins) -> float:
    return float(sum(m * np.trace(a @ right @ a.conj().T).real
                     for m, a in zip(spins, tensors)))


def word_rank(tensors) -> int:
    words = np.array([(p @ q).reshape(-1) for p in tensors for q in tensors])
    return int(np.linalg.matrix_rank(words, tol=1e-9))


def twisted_step(tensors, spins, theta, counterterm, block):
    return sum(np.exp(1j * theta * (m - counterterm)) * a @ block @ a.conj().T
               for m, a in zip(spins, tensors))


def virtual_unitary(theta: float, virtual=(0.0, 1.0)) -> np.ndarray:
    return np.diag(np.exp(1j * theta * np.array(virtual)))


def build_family(spins, rho, seed, forbidden=None):
    rng = np.random.default_rng(seed)
    tensors = left_canonical(charge_diagonal(spins, rho, (0.0, 1.0), rng, forbidden))
    require(tensors is not None, "left canonicalisation failed")
    return tensors, right_environment(tensors)


# ------------------------------------------------------- IDX-C1 and IDX-C2 --

def haar_unitary(dim: int, rng) -> np.ndarray:
    z = (rng.normal(size=(dim, dim)) + 1j * rng.normal(size=(dim, dim))) / np.sqrt(2)
    q, r = np.linalg.qr(z)
    return q * (np.diag(r) / np.abs(np.diag(r)))


def tpm_data(onsite: np.ndarray, spin: float, window=(-1, 1), cut=0):
    """Three-site window: Q, the two spectral resolutions and the TPM law."""
    dim_site = onsite.size
    sites = window[1] - window[0] + 1
    dim = dim_site ** sites
    charge = np.zeros(dim)
    for x in range(sites):
        charge = charge + np.kron(np.kron(np.ones(dim_site ** x), onsite),
                                  np.ones(dim_site ** (sites - 1 - x)))
    charge = charge + spin * (window[0] + window[1] - 1 - 2 * cut)

    rng = np.random.default_rng(TPM_SEED)
    u_minus = haar_unitary(dim, rng)
    u_plus = haar_unitary(dim, rng)
    psi = rng.normal(size=dim) + 1j * rng.normal(size=dim)
    psi = psi / np.linalg.norm(psi)

    ordered = np.sort(charge)                 # exact levels, no rounding
    levels, start = [], 0
    for i in range(1, ordered.size + 1):
        if i == ordered.size or ordered[i] - ordered[start] > 1e-7:
            levels.append(float(ordered[start:i].mean()))
            start = i
    levels = np.array(levels)
    projectors = [(v, (np.abs(charge - v) < 1e-7).astype(float)) for v in levels]
    res_minus = [(v, u_minus.conj().T @ (p[:, None] * u_minus)) for v, p in projectors]
    res_plus = [(v, u_plus.conj().T @ (p[:, None] * u_plus)) for v, p in projectors]

    law = []
    for q_minus, e_minus in res_minus:
        vec = e_minus @ psi
        for q_plus, e_plus in res_plus:
            weight = float(np.linalg.norm(e_plus @ vec) ** 2)
            if weight > 1e-15:
                law.append((q_minus - q_plus, weight))

    q_minus_op = u_minus.conj().T @ (charge[:, None] * u_minus)
    q_plus_op = u_plus.conj().T @ (charge[:, None] * u_plus)
    dephased = sum(e @ q_plus_op @ e for _, e in res_minus)
    exp_minus = float(np.vdot(psi, q_minus_op @ psi).real)
    exp_plus = float(np.vdot(psi, q_plus_op @ psi).real)
    exp_dephased = float(np.vdot(psi, dephased @ psi).real)
    return charge, levels, law, exp_minus, exp_plus, exp_dephased


def check_c1(red: bool) -> list[str]:
    """IDX-C1: coset integrality, TPM normalisation, integer increments, (IDX.4)."""
    lines = []
    for tag, shift in (("half-integer", 0.0), ("irrational", np.sqrt(2.0) - 1.0)):
        onsite = SPIN32 + shift
        charge, levels, law, exp_m, exp_p, exp_d = tpm_data(onsite, 1.5)

        offset = (3 * ((1.5 + shift) % 1.0) + 1.5 * (-1 + 1 - 1 - 0)) % 1.0
        residues = np.abs(((levels - offset) + 0.5) % 1.0 - 0.5)
        require(residues.max() < TOL_EXACT,
                f"IDX-C1 {tag}: spec Q_W is not in the coset kappa+Z "
                f"(max residue {residues.max():.3e})")

        total = sum(w for _, w in law)
        require(abs(total - 1.0) < TOL_EXACT,
                f"IDX-C1 {tag}: TPM normalisation residue {abs(total-1.0):.3e}")

        off_lattice = max(abs(round(nu) - nu) for nu, _ in law)
        require(off_lattice < TOL_EXACT,
                f"IDX-C1 {tag}: TPM increment off Z by {off_lattice:.3e}")

        mean = sum(nu * w for nu, w in law)
        rhs = exp_m - exp_p if red else exp_m - exp_d
        residue = abs(mean - rhs)
        require(residue < TOL_EXACT,
                f"IDX-C1 {tag}: (IDX.4) residue {residue:.3e}")
        lines.append(f"  {tag:12s} offset={offset:.9f} norm_res={abs(total-1.0):.2e} "
                     f"nu_off_Z={off_lattice:.2e} IDX.4_res={residue:.2e}")
    return lines


def check_c2(red: bool) -> list[str]:
    """IDX-C2: the dephasing defect is real, and the L1 lattice landmine."""
    _, _, law, exp_m, exp_p, exp_d = tpm_data(SPIN32, 1.5)
    mean = sum(nu * w for nu, w in law)
    naive_gap = abs(mean - (exp_m - exp_p))
    defect = abs(exp_p - exp_d)
    if red:
        require(naive_gap < TOL_EXACT,
                f"IDX-C2 red: naive two-time arithmetic residue {naive_gap:.3e}")
    require(naive_gap > TOL_LIVE,
            f"IDX-C2: the naive unmeasured difference is NOT wrong "
            f"({naive_gap:.3e}); the mutation is dead")
    require(defect > TOL_LIVE, f"IDX-C2: dephasing defect vanished ({defect:.3e})")

    ket0 = sp.Matrix([1, 0])
    plus = sp.Matrix([1, 1]) / sp.sqrt(2)
    q_minus = ket0 * ket0.T
    q_plus = plus * plus.T
    for name, op in (("Q-", q_minus), ("Q+", q_plus)):
        spectrum = sorted(sp.Matrix(op).eigenvals().keys(), key=sp.re)
        require([sp.simplify(v) for v in spectrum] == [sp.Integer(0), sp.Integer(1)],
                f"IDX-C2: {name} spectrum is not {{0,1}}")
    diff = sorted(sp.Matrix(q_plus - q_minus).eigenvals().keys(), key=sp.re)
    target = [-1 / sp.sqrt(2), 1 / sp.sqrt(2)]
    for got, want in zip(diff, target):
        exact_zero(got - want, "IDX-C2: L1 landmine spectrum")
    return [f"  TPM mean={mean:.12f} naive={exp_m-exp_p:.12f} "
            f"gap={naive_gap:.4e} dephasing defect={defect:.4e}",
            "  L1 landmine spec(Q+ - Q-) = {-1/sqrt2, +1/sqrt2}, both spectra {0,1}"]


# ------------------------------------------------------------------ IDX-C3 --

def _phi_mechanism_a(n_sites: int, grid: int, red: bool) -> np.ndarray:
    """Characteristic function of L_N = sum_n (S^z_{-n} - 1/2), IDX-CE.4."""
    theta = 2 * np.pi * np.arange(grid) / grid
    u = 1.0 - np.cos(theta)
    if red:                                   # eps_n^2 = (n+1)^{-2}
        w = np.sqrt(u)
        return np.exp(gammaln(n_sites + 2 - w) + gammaln(n_sites + 2 + w)
                      - gammaln(2 - w) - gammaln(2 + w)
                      - 2 * gammaln(n_sites + 2))
    values = np.exp(gammaln(n_sites + 2 - u) - gammaln(2 - u)
                    - gammaln(n_sites + 2))   # prod_{m=2}^{N+1} (1 - u/m)
    values[np.isclose(u, 2.0)] = 0.0
    return values


def check_c3(red: bool) -> list[str]:
    """IDX-C3: V_N -> infinity, local CLT bound, and the resolvent decay."""
    direct = np.ones(128)
    grid = 2 * np.pi * np.arange(128) / 128
    for n in range(1, 17):
        eps2 = 1.0 / (n + 1) ** 2 if red else 1.0 / (n + 1)
        direct = direct * (1.0 - eps2 * (1.0 - np.cos(grid)))
    closed = np.abs(_phi_mechanism_a(16, 128, red) - direct).max()
    require(closed < 1e-12, f"IDX-C3: closed form disagrees with the product "
                            f"IDX-CE.4 by {closed:.3e}")

    rows, previous_r = [], None
    for j in range(4, 17):
        n_sites = 2 ** j
        grid_size = 1 << (j + 2)
        law = np.fft.ifft(_phi_mechanism_a(n_sites, grid_size, red)).real
        index = np.arange(grid_size)
        support = np.where(index <= grid_size // 2, index, index - grid_size)
        variance = float(sum(1.0 / (n + 1) ** (2 if red else 1)
                             for n in range(1, n_sites + 1)))
        peak = float(law.max())
        resolvent = complex(np.sum(law / (support - 1j)))
        require(abs(law.sum() - 1.0) < 1e-10,
                f"IDX-C3: mass {law.sum():.12f} at N={n_sites}")
        require(peak * np.sqrt(variance) < 1.0,
                f"IDX-C3: local CLT bound violated at N={n_sites}")
        require(variance >= np.log(n_sites) - 0.5,
                f"IDX-C3: registered V_N -> infinity test fails at N={n_sites} "
                f"(V_N={variance:.4f}, log N - 0.5 = {np.log(n_sites)-0.5:.4f}; "
                f"V_N = H_(N+1) - 1 ~ log N + gamma - 1)")
        if previous_r is not None:
            require(abs(resolvent) < previous_r,
                    f"IDX-C3: |r_N| not decreasing at N={n_sites}")
        previous_r = abs(resolvent)
        rows.append((j, n_sites, variance, peak, abs(resolvent)))

    return [f"  j={j:2d} N={n:6d} V_N={v:8.4f} maxP={p:.5f} "
            f"maxP*sqrt(V_N)={p*np.sqrt(v):.5f} |r_N|={r:.6f}"
            for j, n, v, p, r in rows[::4]]


# ------------------------------------------------------------------ IDX-C4 --

def check_c4(red: bool) -> list[str]:
    """IDX-C4: tightness never upgrades to first-moment convergence."""
    lines = []
    for m in (10, 100, 1000, 10000):
        law = {0: 1.0 - 1.0 / m, m: 1.0 / m}
        moment = sum(nu * w for nu, w in law.items())
        require(abs(law[0] - 1.0) < 2.0 / m,
                f"IDX-C4: p_m does not converge weakly to delta_0 at m={m}")
        cutoff = m // 2
        require(sum(w for nu, w in law.items() if abs(nu) > cutoff) <= 1.0 / m,
                f"IDX-C4: bare tightness fails at m={m}")
        weighted = sum((1 + abs(nu)) * w for nu, w in law.items() if abs(nu) > cutoff)
        if red:
            require(abs(moment) < TOL_LIVE,
                    f"IDX-C4 red: first moment {moment} does not converge to 0")
        require(abs(moment - 1.0) < TOL_EXACT,
                f"IDX-C4: p_m first moment is {moment}, not 1")
        require(weighted >= 1.0,
                f"IDX-C4: (1+|nu|)-tight at m={m}; D27(LR3) would be free")
        lines.append(f"  p_m m={m:6d} weak_limit_mass={law[0]:.6f} "
                     f"first_moment={moment:.6f} (1+|nu|)-tail={weighted:.6f}")

    for width in (10, 100, 1000):
        law = {0: 1.0 - 1.0 / width, width: 0.5 / width, -width: 0.5 / width}
        signed = sum(nu * w for nu, w in law.items())
        require(abs(signed) < TOL_EXACT,
                f"IDX-C4: mu_W signed first moment {signed} is not 0")
        for radius in (1, width // 2, width - 1):
            absolute = sum(abs(nu) * w for nu, w in law.items() if abs(nu) > radius)
            require(absolute >= 1.0 - TOL_EXACT,
                    f"IDX-C4: mu_W absolute tail {absolute} < 1 at R={radius}")
    lines.append("  mu_W exhibit: signed first moment 0, |nu|-tail >= 1 for every R")
    return lines


# ------------------------------------------------------------------ IDX-C5 --

def check_c5(red: bool) -> list[str]:
    """IDX-C5: the two-point law reduces to M-quant-G (G.1)--(G.2)."""
    spin, prob = sp.symbols("s P", positive=True)
    escaped = sp.Integer(1) if red else sp.Integer(2)
    law = {sp.Integer(0): 1 - prob, escaped: prob}
    total = sp.simplify(sum(law.values()))
    exact_zero(total - 1, "IDX-C5: the two-point law is not normalised")

    mean_nu = sp.expand(sum(nu * w for nu, w in law.items()))
    second = sp.expand(sum(nu ** 2 * w for nu, w in law.items()))
    displacement = sp.cancel(-mean_nu / (2 * spin))
    variance = sp.cancel((second - mean_nu ** 2) / (2 * spin) ** 2)
    mean_residue = sp.simplify(displacement + prob / spin)
    variance_residue = sp.simplify(variance - prob * (1 - prob) / spin ** 2)
    require(mean_residue == 0 and variance_residue == 0,
            f"IDX-C5: the mutation must break BOTH -- (G.1) residue "
            f"{mean_residue}, (G.2) residue {variance_residue}")
    return [f"  p_0=1-P, p_{escaped}=P: delta x = {displacement}, "
            f"Var = {sp.factor(variance)}"]


# ------------------------------------------------------------------ IDX-C6 --

def check_c6(red: bool) -> list[str]:
    """IDX-C6: omega(S^z) = rho for every draw of the covariant families."""
    lines = []
    for name, spins, rho, slot in (
            ("spin-3/2", SPIN32, 0.5, (2, 0, 1, 0.8 + 0.3j)),
            ("spin-2", SPIN2, 1.0, (3, 0, 1, 0.8 + 0.3j))):
        for mutated in ((True,) if red else (False, True)):
            rng = np.random.default_rng(DRAW_SEED)
            measured, worst_canon, ranks = [], 0.0, set()
            for _ in range(50):
                raw = charge_diagonal(spins, rho, (0.0, 1.0), rng,
                                      slot if mutated else None)
                tensors = left_canonical(raw)
                require(tensors is not None, f"IDX-C6 {name}: canonicalisation failed")
                worst_canon = max(worst_canon, float(np.linalg.norm(
                    sum(a.conj().T @ a for a in tensors) - np.eye(CHI))))
                right = right_environment(tensors)
                require(np.linalg.eigvalsh(right).min() > 1e-8,
                        f"IDX-C6 {name}: r is not positive definite")
                require(transfer_gap(tensors) < 1.0 - 1e-6,
                        f"IDX-C6 {name}: transfer eigenvalue 1 is degenerate")
                ranks.add(word_rank(tensors))
                measured.append(density(tensors, right, spins))
            measured = np.array(measured)
            deviation = float(np.abs(measured - rho).max())
            spread = float(measured.max() - measured.min())
            require(ranks == {CHI ** 2},
                    f"IDX-C6 {name}: length-2 word rank {ranks}, injectivity lost")
            require(worst_canon < 1e-12,
                    f"IDX-C6 {name}: left-canonical residue {worst_canon:.3e}")
            if mutated and not red:
                require(spread > TOL_LIVE,
                        f"IDX-C6 {name}: forbidden-slot mutation is dead "
                        f"(density spread {spread:.3e})")
                lines.append(f"  {name:8s} MUTANT forbidden slot: density spread "
                             f"{spread:.6f}, max |rho-target| {deviation:.6f}")
            else:
                require(deviation < TOL_EXACT,
                        f"IDX-C6 {name}: |omega(S^z)-rho| = {deviation:.3e} "
                        f"over 50 draws")
                lines.append(f"  {name:8s} rho={rho}: 50 draws, "
                             f"max |omega(S^z)-rho| = {deviation:.3e}, "
                             f"left-canon residue {worst_canon:.2e}, word rank 4")
    return lines


# ------------------------------------------------------------------ IDX-C7 --

def two_sided_phi(alpha, beta, right_beta, spins, theta, window, cut,
                  counterterms, junction=0, insertion=None):
    """phi_W(theta) for the D1(e') alpha|beta contraction with l_alpha = 1.

    ``insertion`` is the optional D1(e) bond insertion on the junction bond.
    """
    left_ct, right_ct = counterterms
    a, b = window
    twisted = right_beta.copy()
    plain = right_beta.copy()
    for x in range(b, a - 1, -1):
        if insertion is not None and x == junction:
            twisted = insertion @ twisted @ insertion.conj().T
            plain = insertion @ plain @ insertion.conj().T
        tensors = alpha if x <= junction else beta
        term = left_ct if x <= cut else right_ct
        twisted = twisted_step(tensors, spins, theta, term, twisted)
        plain = sum(t @ plain @ t.conj().T for t in tensors)
    return complex(np.trace(twisted) / np.trace(plain))


def kink_partners(rho, seed):
    """Independent beta of density -rho, plus a seeded junction insertion."""
    beta, right_beta = build_family(SPIN32, -rho, seed)
    rng = np.random.default_rng(seed + 1)
    insertion = rng.normal(size=(CHI, CHI)) + 1j * rng.normal(size=(CHI, CHI))
    require(abs(np.linalg.det(insertion)) > 1e-3,
            "kink junction insertion is not invertible")
    return beta, right_beta, insertion


def twisted_transfer(tensors, spins, theta, counterterm) -> np.ndarray:
    """Matrix of X -> sum_m e^{i theta (m - ct)} A^m X (A^m)^dag."""
    return sum(np.exp(1j * theta * (m - counterterm)) * np.kron(a, a.conj())
               for m, a in zip(spins, tensors))


def covariance_defect(tensors, spins, counterterm, thetas=None) -> float:
    """max_theta |1 - lambda_max(E_theta^{ct})|, gauge invariant and V-free.

    For a tail covariant under the on-site u with density equal to
    ``counterterm``, E_theta^{ct} = L_{V^-1} . E . L_V is a SIMILARITY
    transform of E (<1>11.<2>1), so its leading eigenvalue is exactly 1 at
    every theta; a tail that is non-covariant, or covariant at a different
    density, is strictly contractive.  This is the tensor-level fingerprint
    of <1>9.<2>4's hypothesis, read at the counterterm the theorem fixes.
    """
    if thetas is None:
        thetas = np.linspace(0.3, 3.0, 10)
    worst = 0.0
    for theta in thetas:
        values = np.linalg.eigvals(twisted_transfer(tensors, spins, theta,
                                                    counterterm))
        top = values[int(np.argmax(np.abs(values)))]
        worst = max(worst, float(abs(1.0 - top)))
    return worst


def noncovariant_partner(beta, spins, target):
    """Injective NON-covariant tail of density exactly ``target``.

    Two forbidden slots of opposite charge, mixed by a bisection on their
    ratio: the covariance break is Theta(1) at every mixing, and the mixing
    is what pins the density -- so the resulting tail differs from the true
    one in covariance ALONE, not in density.
    """
    up = np.zeros((CHI, CHI), complex)
    up[0, 0] = 1.0
    down = np.zeros((CHI, CHI), complex)
    down[1, 1] = 1.0
    top, bottom = len(spins) - 1, 0

    def build(ratio):
        tensors = [b.copy() for b in beta]
        tensors[top] = tensors[top] + NC_SCALE * ratio * up
        tensors[bottom] = tensors[bottom] + NC_SCALE * (1.0 - ratio) * down
        return left_canonical(tensors)

    lo, hi = 0.0, 1.0
    for _ in range(90):
        mid = 0.5 * (lo + hi)
        mixed = build(mid)
        if mixed is None:
            fail("IDX-C7(ii): the non-covariant partner left the injective family")
        if density(mixed, right_environment(mixed), spins) < target:
            lo = mid
        else:
            hi = mid
    mixed = build(hi)
    return mixed, right_environment(mixed)


def _interpolated_beta(alpha, beta, spins, target):
    lo, hi = 0.0, 1.0
    for _ in range(80):
        mid = 0.5 * (lo + hi)
        mixed = left_canonical([(1 - mid) * b + mid * a for a, b in zip(alpha, beta)])
        if mixed is None:
            fail("IDX-C7: beta interpolation left the injective family")
        if density(mixed, right_environment(mixed), spins) < target:
            lo = mid
        else:
            hi = mid
    mixed = left_canonical([(1 - hi) * b + hi * a for a, b in zip(alpha, beta)])
    return mixed, right_environment(mixed)


def check_c7_i(red: bool) -> list[str]:
    """IDX-C7(i): exact conjugation, 2 rho in Z, and phi_W(2 pi) = 1."""
    lines = []
    rho = 0.5
    alpha, right_alpha = build_family(SPIN32, rho, MPS_SEED)

    # (a) one-site twisted map equals L_{V^-1} . E . L_V, and the density law.
    worst = 0.0
    for theta in np.linspace(0.1, 6.2, 20):
        unitary = virtual_unitary(theta)
        inverse = np.linalg.inv(unitary)
        for m, tensor in zip(SPIN32, alpha):
            lhs = np.exp(1j * theta * (m - rho)) * tensor
            worst = max(worst, float(np.abs(lhs - inverse @ tensor @ unitary).max()))
    require(worst < TOL_CONJ, f"IDX-C7(i)(a): conjugation residue {worst:.3e}")

    for name, spins, target in (("spin-3/2", SPIN32, 0.5), ("spin-2", SPIN2, 1.0)):
        scalar = np.exp(2j * np.pi * spins)
        require(np.abs(scalar - scalar[0]).max() < TOL_EXACT,
                f"IDX-C7(i)(a): D26(INT) fails for {name}")
        require(abs(np.exp(2j * np.pi * target) - scalar[0]) < TOL_EXACT,
                f"IDX-C7(i)(a): e^(2 pi i rho) != c for {name}")
        require(abs(np.exp(-2j * np.pi * target) - scalar[0]) < TOL_EXACT,
                f"IDX-C7(i)(a): the beta tail relation e^(-2 pi i rho) = c fails")
        require(abs(2 * target - round(2 * target)) < TOL_EXACT,
                f"IDX-C7(i)(a): 2 rho is not an integer for {name}")
    lines.append(f"  conjugation residue over 20 thetas = {worst:.3e}; "
                 f"e^(2 pi i rho) = c = -1 (spin-3/2), +1 (spin-2), 2 rho in Z")

    # (b) two-sided zero offset.
    beta = [alpha[len(SPIN32) - 1 - k] for k in range(len(SPIN32))]
    right_beta = right_environment(beta)
    require(abs(density(beta, right_beta, SPIN32) + rho) < TOL_EXACT,
            "IDX-C7(i)(b): the spin-flipped partner does not have density -rho")

    multipliers = sorted({abs(2 * c + 1) for c in range(-2, 3)}
                         | {abs(1 - n) for n in range(2, 9)})
    resonance = min(abs(k * RED_SHIFT - round(k * RED_SHIFT))
                    for k in multipliers)
    require(resonance > 0.1,
            f"IDX-C7(i): RED_SHIFT resonates with a window multiplier -- "
            f"closest approach to Z is {resonance:.4f} at multipliers "
            f"{multipliers}; see SPEC NOTE 7")

    shift = RED_SHIFT if red else 0.0
    terms = (rho + shift, -(rho + shift))
    worst_sym, drift = 0.0, []
    for n in range(2, 13):
        row = [abs(two_sided_phi(alpha, beta, right_beta, SPIN32, 2 * np.pi,
                                 (-n, n), c, terms) - 1.0) for c in range(-2, 3)]
        worst_sym = max(worst_sym, max(row))
    for n in range(2, 9):
        drift.append(abs(two_sided_phi(alpha, beta, right_beta, SPIN32, 2 * np.pi,
                                       (-n, 2 * n), 0, terms) - 1.0))
    require(worst_sym < TOL_EXACT,
            f"IDX-C7(i)(b): |phi_W(2 pi) - 1| = {worst_sym:.3e} over n=2..12, "
            f"cuts -2..2")
    require(max(drift) < TOL_EXACT,
            f"IDX-C7(i)(b): asymmetric windows give |phi_W(2 pi)-1| = {max(drift):.3e}")
    beta_ind, right_ind, insertion = kink_partners(rho, MPS_SEED + 11)
    worst_dec = max(abs(two_sided_phi(alpha, beta_ind, right_ind, SPIN32,
                                      2 * np.pi, (-n, n), c, terms,
                                      insertion=insertion) - 1.0)
                    for n in range(2, 13) for c in range(-2, 3))
    require(worst_dec < TOL_EXACT,
            f"IDX-C7(i)(b): decorated kink gives |phi_W(2 pi)-1| = {worst_dec:.3e}")
    lines.append(f"  zero offset: max |phi_W(2 pi)-1| = {worst_sym:.3e} "
                 f"(n=2..12, c=-2..2); asymmetric [-n,2n] max = {max(drift):.3e}; "
                 f"independent decorated kink max = {worst_dec:.3e}")

    if not red:
        mut_terms = (rho + RED_SHIFT, -(rho + RED_SHIFT))
        mut_sym = [abs(two_sided_phi(alpha, beta, right_beta, SPIN32, 2 * np.pi,
                                     (-n, n), c, mut_terms) - 1.0)
                   for n in range(2, 13) for c in range(-2, 3)]
        mut_drift = [abs(two_sided_phi(alpha, beta, right_beta, SPIN32, 2 * np.pi,
                                       (-n, 2 * n), 0, mut_terms) - 1.0)
                     for n in range(2, 9)]
        require(min(mut_sym) > TOL_LIVE,
                f"IDX-C7(i): some (window, cut) pair is SILENT under the "
                f"counterterm mutation (smallest deviation {min(mut_sym):.3e}) "
                f"-- the shift resonates with the window arithmetic")
        require(min(mut_drift) > TOL_LIVE,
                f"IDX-C7(i): some asymmetric window is silent under the "
                f"counterterm mutation ({min(mut_drift):.3e})")
        require(max(mut_drift) - min(mut_drift) > 0.1,
                "IDX-C7(i): the asymmetric family shows no n-drift")
        lines.append(f"  MUTANT rho->rho+{RED_SHIFT:.9f} (irrational, coprime "
                     f"to every multiplier {multipliers}; closest approach to "
                     f"Z {resonance:.4f}): symmetric deviations in "
                     f"[{min(mut_sym):.4f}, {max(mut_sym):.4f}], all live and "
                     f"n-independent; asymmetric [-n,2n] n=2..8 = "
                     f"{np.round(mut_drift, 4).tolist()}")
    return lines


def check_c7_ii(red: bool) -> list[str]:
    """IDX-C7(ii): the antisymmetric tail pair of <1>9.<2>4 is necessary.

    Both prongs hold the counterterms at the CORRECT (rho, -rho); nothing
    here is driven by a counterterm mismatch (r2 objection 3(c)(i)).  Why
    the literal instruction -- break the tensor, watch phi_W(2 pi) move at
    the correct counterterm -- is unimplementable is SPEC NOTE 2.
    """
    lines = []
    rho = 0.5
    alpha, _ = build_family(SPIN32, rho, MPS_SEED)
    beta = [alpha[len(SPIN32) - 1 - k] for k in range(len(SPIN32))]
    right_beta = right_environment(beta)

    # (a) tensor level, gauge invariant, counterterm held at the correct -rho.
    true_defect = covariance_defect(beta, SPIN32, -rho)
    require(true_defect < TOL_CONJ,
            f"IDX-C7(ii)(a): the true beta tail is not covariant at density "
            f"-rho (twisted-transfer defect {true_defect:.3e})")
    beta_bad, right_bad = _interpolated_beta(alpha, beta, SPIN32, -rho + 0.2)
    measured = density(beta_bad, right_bad, SPIN32)
    require(abs(measured - (-rho + 0.2)) < 1e-9,
            f"IDX-C7(ii)(a): mutated beta density {measured:.9f} != {-rho+0.2}")
    bad_defect = covariance_defect(beta_bad, SPIN32, -rho)
    beta_nc, right_nc = noncovariant_partner(beta, SPIN32, -rho)
    nc_density = density(beta_nc, right_nc, SPIN32)
    require(abs(nc_density + rho) < 1e-9,
            f"IDX-C7(ii)(a): the covariance-only partner has density "
            f"{nc_density:.12f}, not -rho -- it does not isolate covariance")
    require(word_rank(beta_nc) == CHI ** 2,
            "IDX-C7(ii)(a): the covariance-only partner is not injective")
    require(np.linalg.eigvalsh(right_nc).min() > 1e-8,
            "IDX-C7(ii)(a): the covariance-only partner has a singular r")
    nc_defect = covariance_defect(beta_nc, SPIN32, -rho)

    # (b) withdraw the antisymmetry on a family where 2 rho leaves Z.
    spins = SPIN32 + KAPPA
    rho_k = rho + KAPPA
    shifted, _ = build_family(spins, rho_k, MPS_SEED)
    partner = [shifted[len(spins) - 1 - k] for k in range(len(spins))]
    right_partner = right_environment(partner)
    scalar = np.exp(2j * np.pi * spins)
    require(np.abs(scalar - scalar[0]).max() < TOL_EXACT,
            "IDX-C7(ii)(b): D26(INT) fails on the charge-shifted family")
    require(abs(np.exp(2j * np.pi * rho_k) - scalar[0]) < TOL_EXACT,
            "IDX-C7(ii)(b): <1>9.<2>3 (e^(2 pi i rho) = c) must still hold")
    require(word_rank(shifted) == CHI ** 2 and word_rank(partner) == CHI ** 2,
            "IDX-C7(ii)(b): the charge-shifted family is not injective")
    rho_partner = density(partner, right_partner, spins)
    require(abs(rho_partner - (-rho_k + 2 * KAPPA)) < TOL_EXACT,
            f"IDX-C7(ii)(b): the covariant partner has density "
            f"{rho_partner:.12f}, not -rho+2kappa")
    difference = rho_k - rho_partner
    require(abs(difference - round(difference)) < TOL_EXACT,
            f"IDX-C7(ii)(b): the general-pair relation rho_a - rho_b in Z "
            f"fails ({difference:.12f})")
    require(abs(np.exp(-2j * np.pi * rho_k) - scalar[0]) > TOL_LIVE,
            "IDX-C7(ii)(b): <1>9.<2>4 still holds on the shifted family; the "
            "withdrawal is dead")
    slack = abs(2 * rho_k - round(2 * rho_k))
    require(slack > TOL_LIVE,
            f"IDX-C7(ii)(b): 2 rho stays in Z on the shifted family "
            f"({slack:.3e}); the counterexample is dead")

    deviations, worst_closed = [], 0.0
    for n in range(2, 13):
        for cut in range(-2, 3):
            value = abs(two_sided_phi(shifted, partner, right_partner, spins,
                                      2 * np.pi, (-n, n), cut,
                                      (rho_k, -rho_k)) - 1.0)
            closed = abs(np.exp(4j * np.pi * rho_k * (n - cut)) - 1.0)
            worst_closed = max(worst_closed, abs(value - closed))
            deviations.append(value)
    require(worst_closed < 1e-9,
            f"IDX-C7(ii)(b): phi_W(2 pi) departs from the closed form "
            f"e^(4 pi i rho n_R) by {worst_closed:.3e}")
    control = max(abs(two_sided_phi(alpha, beta, right_beta, SPIN32, 2 * np.pi,
                                    (-n, n), cut, (rho, -rho)) - 1.0)
                  for n in range(2, 13) for cut in range(-2, 3))
    require(control < TOL_EXACT,
            f"IDX-C7(ii)(b): the antisymmetric half-integer control is not "
            f"identically 1 ({control:.3e})")

    if red:
        require(max(bad_defect, nc_defect, max(deviations)) < TOL_EXACT,
                f"IDX-C7(ii) red: with the counterterms held at the CORRECT "
                f"(rho,-rho), withdrawing <1>9.<2>4 leaves twisted-transfer "
                f"defects {bad_defect:.4f} (density -rho+0.2) and "
                f"{nc_defect:.4f} (density exactly -rho, covariance alone), "
                f"and |phi_W(2 pi)-1| up to {max(deviations):.4f}")
    require(bad_defect > TOL_LIVE,
            f"IDX-C7(ii)(a): the density mutation is dead ({bad_defect:.3e})")
    require(nc_defect > TOL_LIVE,
            f"IDX-C7(ii)(a): the covariance-only mutation is dead "
            f"({nc_defect:.3e})")
    require(max(deviations) > TOL_LIVE,
            f"IDX-C7(ii)(b): the antisymmetry withdrawal is dead "
            f"({max(deviations):.3e})")
    lines.append(f"  (a) twisted-transfer defect at the CORRECT ct=-rho: true "
                 f"tail {true_defect:.2e}; density -rho+0.2 {bad_defect:.4f}; "
                 f"density exactly {nc_density:+.12f} but non-covariant "
                 f"{nc_defect:.4f} -- covariance alone moves it")
    lines.append(f"  (b) charge shift kappa={KAPPA:.9f}: (INT) holds, both "
                 f"tails covariant, rho_a={rho_k:.9f}, rho_b={rho_partner:.9f}, "
                 f"rho_a-rho_b={difference:.1f} in Z but rho_a+rho_b={2*KAPPA:.9f}"
                 f" -- <1>9.<2>4 unavailable, 2 rho off Z by {slack:.4f}")
    lines.append(f"  (b) at the CORRECT (rho,-rho): |phi_W(2 pi)-1| up to "
                 f"{max(deviations):.4f}, window-dependent, matching "
                 f"|e^(4 pi i rho n_R)-1| to {worst_closed:.1e}; the "
                 f"antisymmetric control is {control:.1e}")
    return lines


# ------------------------------------------------------------------ IDX-C8 --

def tail_characteristic(tensors, spins, rho, right, thetas, longest):
    """phi_I(theta) = tr[E_theta^n(r)] for |I| = 1..longest, vectorised in theta."""
    blocks = np.array([np.kron(a, a.conj()) for a in tensors])
    phases = np.exp(1j * np.outer(thetas, np.asarray(spins) - rho))
    twisted = np.einsum("md,dij->mij", phases, blocks)
    state = np.tile(right.reshape(-1), (thetas.size, 1))
    trace = np.eye(CHI).reshape(-1)
    out = np.empty((longest, thetas.size), complex)
    for n in range(longest):
        state = np.einsum("mij,mj->mi", twisted, state)
        out[n] = state @ trace
    return out


def check_c8(red: bool) -> list[str]:
    """IDX-C8: vacuum charge law, quantified tightness, AKLT, obstruction."""
    lines = []
    rho = 0.5
    alpha, right = build_family(SPIN32, rho, MPS_SEED)
    gap = transfer_gap(alpha)
    grid = np.linspace(-np.pi, np.pi, 513)
    phis = tail_characteristic(alpha, SPIN32, rho, right, grid, 40)

    limit = np.array([abs(np.trace(virtual_unitary(t) @ right)) ** 2 for t in grid])
    wrong = np.array([abs(np.trace(virtual_unitary(t))) ** 2 / CHI ** 2 for t in grid])
    target = wrong if red else limit
    distances = np.abs(phis - target).max(axis=1)
    require(np.abs(limit - wrong).max() > TOL_LIVE,
            "IDX-C8: r is proportional to the identity; the mutation is dead")
    require(distances[39] < TOL_EXACT,
            f"IDX-C8: sup|phi_I - G| = {distances[39]:.3e} at |I|=40")
    window = np.arange(2, 13)
    slope = np.polyfit(window, np.log(distances[window - 1]), 1)[0]
    require(np.exp(slope) < gap + 1e-9,
            f"IDX-C8: fitted rate {np.exp(slope):.4f} exceeds lambda_E {gap:.4f}")
    if not red:
        stalled = np.abs(phis - wrong).max(axis=1)
        require(stalled[39] > 1e-3 and stalled[39] > 1e3 * distances[39],
                f"IDX-C8: wrong-environment mutation is dead ({stalled[39]:.3e})")
        require(abs(stalled[39] - stalled[19]) < 1e-9,
                f"IDX-C8: the wrong-environment distance is still moving "
                f"({stalled[19]:.6f} -> {stalled[39]:.6f}), not stalled")
        lines.append(f"  MUTANT G -> |tr V_theta|^2/chi^2: sup-distance stalls at "
                     f"{stalled[39]:.6f} (|I|=20 and |I|=40 agree), against "
                     f"{distances[39]:.1e} for the true limit")
    lines.append(f"  sup|phi_I - |tr(V r)|^2|: |I|=2 {distances[1]:.3e}, "
                 f"|I|=10 {distances[9]:.3e}, |I|=40 {distances[39]:.3e}; "
                 f"fitted rate {np.exp(slope):.4f} <= lambda_E {gap:.4f}")

    fft_grid = 2 * np.pi * np.arange(1024) / 1024
    limit_fft = np.array([abs(np.trace(virtual_unitary(t) @ right)) ** 2
                          for t in fft_grid])
    law = np.fft.fft(limit_fft).real / 1024
    require(abs(law.sum() - 1.0) < 1e-10,
            f"IDX-C8: |sum mu_inf - 1| = {abs(law.sum()-1.0):.3e}")
    require(law.min() > -1e-12, f"IDX-C8: mu_inf has negative mass {law.min():.3e}")

    sigma_plus = np.array([[0, 1], [0, 0]], complex)
    aklt = [np.sqrt(2 / 3) * sigma_plus.conj().T,
            np.diag([1.0, -1.0]).astype(complex) / np.sqrt(3),
            np.sqrt(2 / 3) * sigma_plus]
    require(float(np.linalg.norm(sum(a.conj().T @ a for a in aklt) - np.eye(CHI)))
            < TOL_EXACT, "IDX-C8: the D23 AKLT tensor is not left canonical")
    right_aklt = right_environment(aklt)
    require(abs(density(aklt, right_aklt, AKLT_SPINS)) < TOL_EXACT,
            "IDX-C8: AKLT density is not zero")
    aklt_limit = np.array([abs(np.trace(virtual_unitary(t) @ right_aklt)) ** 2
                           for t in fft_grid])
    aklt_law = np.fft.fft(aklt_limit).real / 1024
    for nu, want in ((0, 0.5), (1, 0.25), (-1, 0.25), (2, 0.0), (-2, 0.0)):
        require(abs(aklt_law[nu] - want) < TOL_EXACT,
                f"IDX-C8: AKLT limit law mu({nu}) = {aklt_law[nu]}, want {want}")
    lines.append(f"  AKLT (D23): mu(-1),mu(0),mu(+1) = {aklt_law[-1]:.6f}, "
                 f"{aklt_law[0]:.6f}, {aklt_law[1]:.6f}; mu(+-2) = "
                 f"{abs(aklt_law[2]):.2e}")

    obstruction = 2 * (1 - abs(np.trace(virtual_unitary(np.pi) @ right)) ** 2)
    require(obstruction > 0.1, f"IDX-C8: obstruction {obstruction:.6f} is not > 0")
    at_pi = tail_characteristic(alpha, SPIN32, rho, right,
                                np.array([np.pi]), 40)[:, 0]
    shells = 2 * (1 - at_pi.real)
    require(abs(shells[39] - obstruction) < TOL_EXACT,
            f"IDX-C8: shell limit {shells[39]:.9f} != {obstruction:.9f}")

    # <1>12.<2>2: shell of length 12 at distance d from a DECORATED kink
    # junction, with an independently drawn beta so that r_beta != r_alpha.
    beta, right_beta, insertion = kink_partners(rho, MPS_SEED + 11)
    require(float(np.abs(right_beta - right).max()) > 1e-3,
            "IDX-C8: r_beta = r_alpha, the deep-shell test would be vacuous")
    kink = []
    for distance in (4, 8, 16, 32):
        block = insertion @ right_beta @ insertion.conj().T
        block = block / np.trace(block).real
        for _ in range(distance):
            block = sum(t @ block @ t.conj().T for t in alpha)
        for _ in range(12):
            block = twisted_step(alpha, SPIN32, np.pi, rho, block)
        kink.append(abs(complex(np.trace(block)).real - at_pi[11].real))
    require(kink[-1] < 1e-9 and kink[-1] < kink[0],
            f"IDX-C8: the deep-shell kink contraction does not converge to the "
            f"pure tail ({['%.1e' % k for k in kink]})")

    product = [np.ones((1, 1), complex) if abs(m - rho) < 1e-12
               else np.zeros((1, 1), complex) for m in SPIN32]
    block = np.ones((1, 1), complex)
    for _ in range(12):
        block = twisted_step(product, SPIN32, np.pi, rho, block)
    comparator = 2 * (1 - complex(np.trace(block)).real)
    require(abs(comparator) < TOL_EXACT,
            f"IDX-C8: chi=1 comparator obstruction {comparator:.3e} is not zero")
    lines.append(f"  obstruction 2(1-|tr(V_pi r)|^2) = {obstruction:.6f} > 0; "
                 f"pure-tail shells |I|=40 give {shells[39]:.6f}; kink shell "
                 f"residues at d=4,8,16,32 {['%.1e' % k for k in kink]}; "
                 f"chi=1 comparator {abs(comparator):.1e}")
    return lines


# --------------------------------------------------------------- IDX-C8rho --

def check_c8_rho(red: bool) -> list[str]:
    """IDX-rho.6 (<1>11.<2>3): the truncation inequality and its constant.

    The r2 adjudicator's mutation (memory-index-r2.md section 2): the
    threshold 2/u -> 1/u.  It is a real test because the stated constant is
    nearly sharp -- min over |x| >= 2 of 2(1-sinc x) = 1.0907, with the
    sharp threshold at x* = 1.8955, so 2 carries only about 5% of slack.
    """
    lines = []
    cutoff = 1.0 if red else 2.0
    unit = 1.0

    # (a) the adjudicator's exhibit: mu = (delta_-1 + delta_+1)/2 at u = 1.
    exhibit = {-1: 0.5, 1: 0.5}
    integral = sum(w * 2.0 * (1.0 - np.sinc(unit * nu / np.pi))
                   for nu, w in exhibit.items())
    mass = sum(w for nu, w in exhibit.items() if abs(nu) >= cutoff / unit)
    require(mass <= integral + 1e-12,
            f"IDX-rho.6: the truncation inequality FAILS at threshold "
            f"{cutoff:g}/u on mu = (delta_-1 + delta_+1)/2 at u=1 -- it claims "
            f"{mass:.4f} <= {integral:.4f}")

    # (b) the weight floor and how little slack the constant 2 has.
    grid = np.linspace(cutoff, 400.0, 400001)
    floor = float(np.min(2.0 * (1.0 - np.sinc(grid / np.pi))))
    require(floor >= 1.0,
            f"IDX-rho.6: min over |x| >= {cutoff:g} of 2(1-sinc x) is "
            f"{floor:.4f} < 1, so the truncation inequality has no constant")
    lo, hi = 1.0, 2.0
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        if 2.0 * (1.0 - np.sinc(mid / np.pi)) < 1.0:
            lo = mid
        else:
            hi = mid
    sharp = 0.5 * (lo + hi)
    require(abs(sharp - 1.8955) < 1e-3,
            f"IDX-rho.6: the sharp threshold is {sharp:.4f}, not 1.8955")
    require(2.0 * (1.0 - np.sinc(1.8 / np.pi)) < 1.0,
            "IDX-rho.6: the threshold could be lowered to 1.8 after all")
    if not red:
        mutated = sum(w for nu, w in exhibit.items() if abs(nu) >= 1.0 / unit)
        require(mutated > integral + TOL_LIVE,
                f"IDX-rho.6: the 2/u -> 1/u mutation is dead on the exhibit "
                f"({mutated:.4f} vs {integral:.4f})")
        lines.append(f"  MUTANT threshold 2/u -> 1/u on mu = "
                     f"(delta_-1+delta_+1)/2 at u=1: claims {mutated:.3f} <= "
                     f"{integral:.4f}, false; the stated 2/u claims "
                     f"{mass:.3f} <= {integral:.4f}, true")
    lines.append(f"  weight floor min_(|x|>=2) 2(1-sinc x) = {floor:.4f} >= 1; "
                 f"sharp threshold x* = {sharp:.4f}, so the stated 2 carries "
                 f"{100.0*(2.0-sharp)/2.0:.1f}% slack")

    # (c) exhibits with mass BEYOND the cutoff: both sides strictly positive.
    positive = []
    for support in (2, 3, 5):
        for weight_out in (0.1, 0.5, 1.0):
            law = {0: 1.0 - weight_out,
                   -support: weight_out / 2.0, support: weight_out / 2.0}
            value = sum(w * 2.0 * (1.0 - np.sinc(unit * nu / np.pi))
                        for nu, w in law.items())
            out = sum(w for nu, w in law.items() if abs(nu) >= cutoff / unit)
            require(out > 0.0,
                    f"IDX-rho.6: the |nu|={support} exhibit is vacuous")
            require(out <= value + 1e-12,
                    f"IDX-rho.6: inequality fails at |nu|={support}, "
                    f"p={weight_out}: {out:.6f} > {value:.6f}")
            positive.append(value / out)
    require(1.0 <= min(positive) < 1.10,
            f"IDX-rho.6: the tightest exhibit has slack {min(positive):.4f}, "
            f"not the near-sharp 1.0907")
    lines.append(f"  exhibits with mass beyond the cutoff (|nu|=2,3,5, "
                 f"p=0.1,0.5,1): inequality holds with worst ratio "
                 f"integral/tail = {min(positive):.4f}")

    # (d) the chi=2 family: the identity, the tightness bound, and the ledger.
    rho = 0.5
    alpha, right = build_family(SPIN32, rho, MPS_SEED)
    fft_grid = 2 * np.pi * np.arange(1024) / 1024
    lengths = [2, 5, 10, 20, 40]
    window_phis = tail_characteristic(alpha, SPIN32, rho, right, fft_grid,
                                      max(lengths))
    index = np.arange(fft_grid.size)
    nus = np.where(index <= fft_grid.size // 2, index, index - fft_grid.size)
    measures = {n: np.fft.fft(window_phis[n - 1]).real / fft_grid.size
                for n in lengths}
    for n, measure in measures.items():
        require(abs(measure.sum() - 1.0) < 1e-10,
                f"IDX-rho.6: mu_I has mass {measure.sum():.12f} at |I|={n}")
        require(measure.min() > -1e-10,
                f"IDX-rho.6: mu_I has negative mass {measure.min():.3e} "
                f"at |I|={n}")
    bounds, family_mass = [], 0.0
    for u in (1.0, 0.5, 0.25, 0.125):
        theta_u = np.linspace(-u, u, 4001)
        weight = 2 * (1 - np.sinc(u * nus / np.pi))
        require(weight[np.abs(nus) >= cutoff / u].min() >= 1.0,
                f"IDX-rho.6: 2(1-sinc(u nu)) < 1 somewhere on "
                f"|nu| >= {cutoff:g}/u, u={u}")
        worst_bound, worst_identity = 0.0, 0.0
        for n in lengths:
            values = tail_characteristic(alpha, SPIN32, rho, right,
                                         theta_u, n)[n - 1]
            area = float(np.trapezoid(1.0 - values.real, theta_u) / u)
            series = float(np.sum(measures[n] * weight))
            worst_identity = max(worst_identity, abs(series - area))
            out = float(np.sum(measures[n][np.abs(nus) >= cutoff / u]))
            family_mass = max(family_mass, out)
            require(out <= area + 1e-9,
                    f"IDX-rho.6: inequality fails on the chi=2 family at "
                    f"u={u}, |I|={n}")
            worst_bound = max(worst_bound, area)
        require(worst_identity < 1e-6,
                f"IDX-rho.6: identity residue {worst_identity:.3e} at u={u}")
        bounds.append((u, worst_bound))
    for (u_a, b_a), (u_b, b_b) in zip(bounds, bounds[1:]):
        require(b_b < b_a, f"IDX-rho.6: tightness bound not decreasing "
                           f"({u_a}->{u_b}: {b_a:.4e}->{b_b:.4e})")
    require(bounds[-1][1] < 0.05,
            f"IDX-rho.6: quantified tightness bound {bounds[-1][1]:.4e} at "
            f"u=0.125")
    require(family_mass < 1e-12,
            f"IDX-rho.6: the chi=2 family now carries mass {family_mass:.3e} "
            f"beyond the cutoff, so the vacuity ledger below is stale and the "
            f"exhibits of (a) and (c) must be redrawn")
    lines.append(f"  chi=2 family: identity residue < 1e-6 and tightness "
                 f"sup_I u^-1 int(1-Re phi) = "
                 + ", ".join(f"u={u}: {b:.4e}" for u, b in bounds))
    lines.append(f"  VACUITY LEDGER: mu_I is supported on {{-1,0,+1}} for "
                 f"every |I|, so the family's own mass beyond 2/u is exactly "
                 f"{family_mass:.1e} -- that instantiation certifies nothing "
                 f"and the content is carried by (a)-(c) (r2 objection "
                 f"3(c)(iii))")
    return lines


# -------------------------------------------------------------------- main --

CHECKS = [
    ("IDX-C1", "finite-window offset and TPM law", check_c1),
    ("IDX-C2", "two-time dephasing defect, L1 landmine", check_c2),
    ("IDX-C3", "mechanism-A counterexample", check_c3),
    ("IDX-C4", "weak limit does not give a first moment", check_c4),
    ("IDX-C5", "M-quant-G reduction", check_c5),
    ("IDX-C6", "IT phase slope = tail density", check_c6),
    ("IDX-C7(i)", "exact conjugation and zero offset", check_c7_i),
    ("IDX-C7(ii)", "necessity of the antisymmetric tail pair", check_c7_ii),
    ("IDX-C8", "vacuum charge law and obstruction", check_c8),
    ("IDX-C8rho", "IDX-rho.6 truncation inequality", check_c8_rho),
]


def run(red: bool) -> list[tuple[str, str, bool, list[str], str]]:
    results = []
    for name, title, function in CHECKS:
        try:
            results.append((name, title, True, function(red), ""))
        except CheckFailure as exc:
            results.append((name, title, False, [], str(exc)))
    return results


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--red", action="store_true",
                        help="apply every named mutation; all checks must fail")
    args = parser.parse_args()
    results = run(args.red)

    if args.red:
        survivors = [name for name, _, ok, _, _ in results if ok]
        print("RED MUTATION TABLE")
        for name, title, ok, _, why in results:
            verdict = "SURVIVED" if ok else "caught  "
            print(f"  {name}  {verdict}  {title}")
            if why:
                print(f"            {why}")
        if survivors:
            print(f"FAIL: mutations survived in {', '.join(survivors)} -- "
                  "the checker is not red-capable", file=sys.stderr)
            raise SystemExit(2)
        print("RED-OK: every named mutation broke its check")
        raise SystemExit(1)

    for name, title, ok, lines, why in results:
        print(f"{name}  {title}")
        for line in lines:
            print(line)
        if why:
            print(f"  FAILED: {why}")
    print()
    print("CHECK TABLE")
    for name, title, ok, _, _ in results:
        print(f"  {name}  {'PASS' if ok else 'FAIL'}  {title}")
    broken = [name for name, _, ok, _, _ in results if not ok]
    if broken:
        print(f"FAIL: {', '.join(broken)}", file=sys.stderr)
        raise SystemExit(1)
    print()
    print("SPEC NOTES (closest faithful readings, reported not improvised)")
    for number, note in enumerate(SPEC_NOTES, start=1):
        print(f"  {number}. {note}")
    print(f"  COUNT: {SPEC_NOTE_LEDGER}")
    print()
    print("PASS: M-INDEX symbolic and small-matrix certificates IDX-C1--IDX-C8, "
          "ten registered rows")


if __name__ == "__main__":
    main()
