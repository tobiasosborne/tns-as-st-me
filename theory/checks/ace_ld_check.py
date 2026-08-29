#!/usr/bin/env python3
"""Deterministic certificates LD-C1..LD-C7 for the ACE-LD r4 shard.

Spec: ``theory/ace-ld.md`` section 5 (CHECKER SPEC), r4.  House style:
every violation raises ``CheckFailure`` (python3 -O safe, no bare assert);
nothing is random.  Rebuilt after theory/verdicts/ace-ld-r2.md M3/M4,
repaired after theory/verdicts/ace-ld-r3.md M2/M3/m8, per the standing
checker obligations of briefs/critic-protocol.md:

  * r2's LD-C6 (position-diagonal model) was a TAUTOLOGY (r2 M3): p_W =
    delta_0 for every state and every position-diagonal H.  It is
    REPLACED by a bounded-transport contrast on the D16 battery with one
    magnon added: the dynamics does NOT commute with Q_W (liveness gate),
    the TPM law is supported on a bounded nu-set, and the first moment
    stays bounded as |W| grows — against LD-C5's linear growth.
    r4 (r3 M3): the first-moment gate is evaluated BEFORE the support
    gate (so --red-c6-moving reaches it), its bound C6_MOM_BOUND is set
    above the recorded t_+-sweep maximum (the r3 value 1.0 was tuned to
    t_+ = 4: the GREEN model at t_+ = 20 gives 1.0712), and the sweep
    itself is gated; --red-c6-weaktransit arms the support gate, which
    the reorder would otherwise shadow.
  * LD-C5's identity gate (d) is IMPLIED by its concentration gate (a)
    (r2 M4: the gap is ~1e-11 and tracks the concentration defect) and
    its tail-floor gate (e) is IMPLIED by (b)+(c) (arithmetically 1>0.9).
    Both are DISCLOSED as consistency lines, not independent evidence.
    The genuinely two-branch content is certified separately (LD-C5b).
    r4 (r3 M2): LD-C5b's wedge at (t_-, t_+) = (0, 300) certifies ONLY
    that the pinching D acts; it is NOT the D27(LR2) quantity, which
    averages over t_+ in [T,2T] AND t_- in [-2T,-T] (the V0 = 0
    straddling packet has a LARGER t_-=0 defect, -8.3868, yet satisfies
    LR2 exactly — registered as --red-c5b-nobarrier).  The LR2-failure
    claim is now gated at D27's own double-Cesaro defect: measured
    -3.3592, stable in T, mechanism = the backward-evolved packet stays
    split across three window-charge branches (0.8563/0.0170/0.1267)
    forever.  (An identity-with-D gate is deliberately NOT shipped: it
    reduces to x = x against the same branch decomposition — the no-op
    pattern; refusal certified by ace-ld-r3 n6.)
  * LD-C1's orthogonality and resolution sub-gates each have a
    registered red mode (r2 M4/m4: previously no mode reached them).
  * LD-C7 gate (e): (K-TAIL) itself, measured site-by-site (r2 n5), in
    the Z2-flipped orientation of the ED ground state (r2 m2), red-armed
    by --red-c7-orientation.  By Cauchy-Schwarz on the self-adjoint D_x
    the on-site clause implies the off-diagonal clause, so (e) certifies
    (K-TAIL) in full (ace-ld-r3 n1).
  * NO blanket reachability claim is made.  The reachability TABLE and
    the complete unreached-gate list (r3 M3) live in the spec, section 5
    of theory/ace-ld.md; each unreached gate is listed with its
    shadowing gate named.

Batteries:

  FREE     one particle on Z_N, H = hopping (FFT), momentum-sign
           channels, clamp window charge.  Gates LD-C1..LD-C4.
  BARRIER  one particle on Z_N, H = hopping + barrier, dense eigh.
           Gate LD-C5 (obstruction-mechanism configuration) and
           LD-C5b (two-branch dephasing certificate).
  D16      exact diagonalisation of the D16 XXZ kink chain.
           Gate LD-C6 (kink+magnon bounded-transport contrast) and
           LD-C7 (epsilon-version decay + (K-TAIL) profile).

Red modes (all FRESH mutated variants; green objects never mutated in
place).  REGISTRY records, per mode, the battery and the gates that MUST
break / MUST pass; a surviving target or an unregistered casualty exits
2.  Exit paths (the firing gate + message) are printed per mode.

Green exits 0; --red exits 1 iff every registered mutation reproduces
its registered pattern, else 2; a green gate failure exits 3.
"""

from __future__ import annotations

import argparse
import sys
from itertools import combinations

import numpy as np

# --------------------------------------------------------------- constants --
# FREE battery
N_FREE = 8192
XC_FREE = N_FREE // 2
HALF_W = 16                    # window half-width: W = [XC-16, XC+16]
K0 = np.pi / 2                 # packet momentum magnitude (no detune)
K_WIDTH = 0.6                  # momentum bump half-width
C_MINUS = 0.8                  # left-mover amplitude  (channel '-')
C_PLUS = 0.6                   # right-mover amplitude (channel '+')
TIMES = (4, 8, 16, 32, 64, 128, 256, 512, 1024)
TOL_CONV = 1e-6                # final-time convergence tolerance
TOL_EXACT = 1e-9               # machine-precision identities
TOL_INEQ = 1e-9                # slack for the certified inequality
C3_RATIO_FLOOR = 0.10          # liveness floor for max lhs/rhs (green only;
                               # measured green value 0.168)
# BARRIER battery
N_BAR = 2048
XC_BAR = N_BAR // 2
BAR_V0 = 1.2                   # barrier height (one site)
BAR_X0_OFF = 300               # packet start: XC - 300
BAR_T = 300                    # protocol half-span: t_- = 0, t_+ = 300
BAR_KW = 0.5
BAR_HALF_WS = (8, 16, 32, 64)  # growing windows
BAR_M = 10                     # tail threshold M in the LR3 moment
# LD-C5b (two-branch dephasing-wedge certificate; straddling configuration)
C5B_HALF_W = 8                 # window |W| = 17
C5B_WEDGE_MIN = 1.0            # |sum nu p - (<Q>_- - <Q>_+)| must exceed
#                                this in the straddling configuration
#                                (measured green value ~6.08).  Certifies
#                                that D ACTS; NOT the D27(LR2) quantity
#                                (r3 M2: --red-c5b-nobarrier passes this
#                                gate at 8.3868 while satisfying LR2).
# LD-C5b double-Cesaro gate (r4, r3 M2 fix: D27(LR2)'s own quantity)
C5B_LR2_TS = (20.0, 40.0)      # Cesaro spans T; mean over t_+ in [T,2T],
#                                t_- in [-2T,-T], C5B_LR2_GRID^2 points
C5B_LR2_GRID = 9               # grid points per axis (matches r3 M2(b))
C5B_LR2_MIN = 3.0              # |double-Cesaro defect| floor, keyed to the
#                                measured -3.3592 (r3 M2: stable for
#                                T = 20..200; NOT the t_-=0 value 6.083)
C5B_LR2_STAB = 0.02            # |defect(T1) - defect(T2)| stability gate
#                                (measured ~3e-5)
# D16 battery
D16_L = 12
D16_DELTA = 2.5
D16_J = 1.0
D16_C0 = 5
D16_WINDOWS = ((4, 7), (3, 8), (2, 9), (1, 10))
D16_CLAIMED_Q = 0.208712       # Delta - sqrt(Delta^2-1) at Delta = 2.5
D16_RATE_RTOL = 0.02           # |ratio/claimed_q - 1| gate
D16_FLAT_TOL = 1e-10           # sector ground energy |E0| gate
D16_COSET_TOL = 1e-2           # |<Q_W> - nearest integer| gate
D16_CORE = (4, 7)              # (K-TAIL) core K for gate LD-C7(e)
D16_KTAIL_CBOUND = 0.30        # C_K gate: max ||D_x phi|| lam^-dist <= this
D16_KTAIL_RTOL = 0.02          # (K-TAIL) profile ratio gate
# LD-C6 (kink+magnon bounded transport; thresholds asserted, values logged)
C6_MAGNON_SITE = 10            # 1-indexed site where S^- is applied (up tail)
C6_TPLUS = 4.0                 # protocol time
C6_LIVE_MIN = 0.02             # 1 - p_0 at the LARGEST window must exceed
C6_NU_MAX = 3                  # support gate: mass at |nu| > this ...
C6_SUPPORT_TOL = 1e-9          # ... must be below this
C6_SWEEP = (4.0, 20.0, 40.0, 200.0)   # t_+ sweep for the first-moment gate
#                                (r4, r3 M3: the r3 bound 1.0 was tuned to
#                                t_+ = 4 — the green model fires it at
#                                t_+ = 20 with 1.0712)
C6_MOM_BOUND = 1.2             # sum |nu| p <= this at EVERY window and
#                                EVERY sweep time; set above the recorded
#                                green sweep maximum 1.0712 (t_+ = 20,
#                                W = [3,8]); sweep values logged


class CheckFailure(Exception):
    """A certificate violation.  Never a bare assert (python3 -O safe)."""


def require(cond: bool, msg: str) -> None:
    if not cond:
        raise CheckFailure(msg)


# ------------------------------------------------------------ FREE battery --
def _momenta(n: int) -> np.ndarray:
    return 2.0 * np.pi * np.fft.fftfreq(n)


def _bump(u: np.ndarray) -> np.ndarray:
    out = np.zeros_like(u)
    inside = np.abs(u) < 1.0
    out[inside] = np.exp(1.0 - 1.0 / (1.0 - u[inside] ** 2))
    return out


def _packet(n: int, x0: int, k_center: float, k_width: float) -> np.ndarray:
    k = _momenta(n)
    amp = _bump((k - k_center) / k_width) * np.exp(-1j * k * x0)
    psi = np.fft.ifft(amp)
    return psi / np.linalg.norm(psi)


class FreeModel:
    """Green FREE model; red variants are fresh instances with overrides."""

    def __init__(self, q_scale: float = 1.0, merged: bool = False,
                 dup_charge: bool = False, coset_shift: float = 0.0,
                 halfspace: bool = False, overlap: bool = False,
                 leak: bool = False, is_green: bool = True):
        self.is_green = is_green
        self.a = XC_FREE - HALF_W
        self.b = XC_FREE + HALF_W
        x = np.arange(N_FREE)
        qv = (np.minimum(self.b, np.maximum(x, self.a - 1))
              - (self.a - 1)).astype(float) * q_scale
        q_top = float(self.b - self.a + 1) * q_scale
        if coset_shift:
            qv = np.where(np.abs(qv - q_top) < 1e-12, q_top + coset_shift, qv)
            q_top = q_top + coset_shift
        self.qvals = qv
        self.spec = np.unique(self.qvals)
        k = _momenta(N_FREE)
        self.disp = 2.0 * np.cos(k)
        if halfspace:
            self.mask_plus = ("space", x >= XC_FREE)   # right half-line
            self.mask_minus = ("space", x < XC_FREE)
        elif overlap:
            # channel masks OVERLAP inside the left-mover packet support
            # (sin k in (0.825, 0.9)): arms LD-C1's ORTHOGONALITY sub-gate
            self.mask_plus = ("mom", np.sin(k) < 0.9)
            self.mask_minus = ("mom", np.sin(k) >= 0.0)
        elif leak:
            # channel masks LEAK: |sin k| <= 0.9 is claimed by neither
            # channel: arms LD-C1's RESOLUTION sub-gate
            self.mask_plus = ("mom", np.sin(k) < -0.9)
            self.mask_minus = ("mom", np.sin(k) > 0.9)
        else:
            mp = (np.sin(k) < 0.0)                     # right-movers
            self.mask_plus = ("mom", mp)
            self.mask_minus = ("mom", ~mp)
        self.phi_plus = _packet(N_FREE, XC_FREE, -K0, K_WIDTH)   # v > 0
        self.phi_minus = _packet(N_FREE, XC_FREE, +K0, K_WIDTH)  # v < 0
        self.psi0 = C_MINUS * self.phi_minus + C_PLUS * self.phi_plus
        self.psi0 = self.psi0 / np.linalg.norm(self.psi0)
        if merged:
            self.channels = [("1", None, q_top)]
        elif dup_charge:
            self.channels = [("+", self.mask_plus, q_top),
                             ("-", self.mask_minus, q_top)]
        else:
            self.channels = [("+", self.mask_plus, q_top),
                             ("-", self.mask_minus, 0.0)]
        # The claimed constant is ASSERTED at 1 per ace-ld.md <1>1.<2>3
        # (coset gap >= 1 via M-INDEX-fin); it is NOT computed from the
        # model spectrum (r1 verdict M6: computing it would defeat the
        # --red-gap mutation).  --red-gap keeps this while shrinking the
        # true gap — that IS the mutation.
        self.claimed_inv_gap = 1.0

    def evolve(self, psi: np.ndarray, t: float) -> np.ndarray:
        return np.fft.ifft(np.exp(-1j * self.disp * t) * np.fft.fft(psi))

    def project_channel(self, psi: np.ndarray, mask) -> np.ndarray:
        if mask is None:
            return psi.copy()
        kind, arr = mask
        if kind == "space":
            return psi * arr
        return np.fft.ifft(np.fft.fft(psi) * arr)

    def spectral_proj(self, psi: np.ndarray, q: float) -> np.ndarray:
        return psi * (np.abs(self.qvals - q) < 1e-9)

    def guard_no_wrap(self, psi: np.ndarray, label: str) -> None:
        cutmass = float(np.sum(np.abs(psi[:64]) ** 2)
                        + np.sum(np.abs(psi[-64:]) ** 2))
        require(cutmass < 1e-16,
                f"guard: wavefront reached the ring cut in {label} "
                f"(mass {cutmass:.3e})")


def check_c1(m: FreeModel, log) -> None:
    """Hypothesis audit: one coset, gap >= 1, [P,H]=0, orthogonal, resolving.

    Sub-gate order (each with its registered red mode — see REGISTRY):
    gap <- --red-gap; coset <- --red-coset (disclosure, r2 n4: the coset
    gate is arithmetic on the checker's own integer clamp — it can fail
    only if the observable's construction is corrupted, the same status
    memory_index_probe.py P2 carries); commutation <- --red-halfspace;
    orthogonality <- --red-c1-overlap; resolution <- --red-c1-leak.
    """
    gaps = np.diff(np.sort(m.spec))
    require(float(gaps.min()) >= 1.0 - 1e-12,
            f"LD-C1: spectral separation {float(gaps.min()):.3e} < 1")
    frac = np.mod(m.spec - m.spec[0], 1.0)
    frac = np.minimum(frac, 1.0 - frac)
    require(float(frac.max()) < 1e-12,
            "LD-C1: spectrum not in a single coset of Z "
            f"(max coset spread {float(frac.max()):.3e})")
    for name, mask, _ in m.channels:
        lhs = m.project_channel(
            np.fft.ifft(m.disp * np.fft.fft(m.psi0)), mask)
        rhs = np.fft.ifft(m.disp * np.fft.fft(m.project_channel(m.psi0, mask)))
        err = float(np.linalg.norm(lhs - rhs))
        require(err < TOL_EXACT, f"LD-C1: [P_{name}, H] != 0 ({err:.3e})")
    if len(m.channels) == 2:
        p1 = m.project_channel(m.psi0, m.channels[0][1])
        p12 = m.project_channel(p1, m.channels[1][1])
        err = float(np.linalg.norm(p12))
        require(err < TOL_EXACT,
                f"LD-C1: channel projections not orthogonal ({err:.3e})")
    total = sum(m.project_channel(m.psi0, mask) for _, mask, _ in m.channels)
    err = float(np.linalg.norm(total - m.psi0))
    require(err < TOL_EXACT, f"LD-C1: sum P_ch psi != psi ({err:.3e})")
    log("LD-C1 hypothesis audit: single coset, gap >= 1, [P,H]=0, "
        "orthogonal, resolving")


def _channel_data(m: FreeModel, t: float):
    psi_t = m.evolve(m.psi0, t)
    m.guard_no_wrap(psi_t, f"t={t}")
    rows = []
    for name, mask, q in m.channels:
        pch = m.project_channel(psi_t, mask)
        eps = float(np.linalg.norm(m.qvals * pch - q * pch))
        rows.append((name, q, pch, eps))
    return psi_t, rows


def check_c2(m: FreeModel, log) -> None:
    """First-moment escape eps_ch(t) -> 0."""
    first, final = {}, {}
    for t in TIMES:
        _, rows = _channel_data(m, t)
        for name, _, _, eps in rows:
            first.setdefault(name, eps)
            final[name] = eps
    for name in final:
        require(final[name] < TOL_CONV,
                f"LD-C2: eps_{name}(t_final) = {final[name]:.3e} "
                f">= {TOL_CONV} (no first-moment escape)")
        require(final[name] < first[name],
                f"LD-C2: eps_{name} did not decrease "
                f"({first[name]:.3e} -> {final[name]:.3e})")
    log("LD-C2 first-moment escape: " + ", ".join(
        f"eps_{n}(final)={v:.2e}" for n, v in final.items()))


def check_c3(m: FreeModel, log) -> None:
    """(LD.1) at the ASSERTED constant, every grid time; ratio reported.

    Honesty note (r1 verdict M6): this gate certifies that the inequality
    holds at the asserted constant and that a 10x-optimistic constant is
    detected (--red-gap).  It does NOT certify sharpness: the measured
    max lhs/rhs on the green model is ~0.168, so constants down to ~6x
    smaller would also pass.  The ratio floor below is a green-only
    liveness gate (it catches a silently dead lhs), not a sharpness gate,
    and is by design reached by no red mode (skipped on mutants so
    registered patterns stay exact) — disclosed in the spec table.
    """
    max_ratio = 0.0
    for t in TIMES:
        psi_t, rows = _channel_data(m, t)
        rhs = sum(eps for _, _, _, eps in rows) * m.claimed_inv_gap
        for name, q, pch, _ in rows:
            lhs = float(np.linalg.norm(m.spectral_proj(psi_t, q) - pch))
            require(lhs <= rhs + TOL_INEQ * (1.0 + rhs),
                    f"LD-C3: (LD.1) violated at t={t}, channel {name}: "
                    f"lhs {lhs:.6e} > rhs {rhs:.6e}")
            if rhs > 1e-12:
                max_ratio = max(max_ratio, lhs / rhs)
    if m.is_green:
        require(max_ratio >= C3_RATIO_FLOOR,
                f"LD-C3: liveness floor: max lhs/rhs = {max_ratio:.3f} "
                f"< {C3_RATIO_FLOOR} (lhs suspiciously dead)")
    log(f"LD-C3 inequality (LD.1) holds at all times at the asserted "
        f"constant (max lhs/rhs = {max_ratio:.3f}; not a sharpness test)")


def check_c4(m: FreeModel, log) -> None:
    """Spectral diagonality at the final time (the collapsed-form surface).

    Near-subsumption disclosure: with C2's eps < 1e-6 per channel, C3's
    inequality already gives lhs <= ~2e-6; C4's independent value is that
    it tests the diagonality NORM directly at threshold 1e-6 and is the
    surface --red-merged / --red-dup break.
    """
    t = TIMES[-1]
    psi_t, rows = _channel_data(m, t)
    for name, q, pch, _ in rows:
        lhs = float(np.linalg.norm(m.spectral_proj(psi_t, q) - pch))
        require(lhs < TOL_CONV,
                f"LD-C4: ||E({{q_{name}}})psi_t - P_{name} psi_t|| "
                f"= {lhs:.3e} >= {TOL_CONV} at t={t}")
    log(f"LD-C4 diagonality at t={t}: all channels < {TOL_CONV}")


# --------------------------------------------------------- BARRIER battery --
_EIGH_CACHE: dict = {}          # v0 -> (evals, evecs_complex); the H is
#                                 identical across instances at fixed v0, so
#                                 sharing its eigendecomposition is a pure
#                                 speed-up (states are never shared)


def _barrier_eigh(v0: float):
    key = round(float(v0), 12)
    if key not in _EIGH_CACHE:
        H = np.zeros((N_BAR, N_BAR))
        for i in range(N_BAR):
            H[i, (i + 1) % N_BAR] = 1.0
            H[i, (i - 1) % N_BAR] = 1.0
        H[XC_BAR, XC_BAR] += v0
        evals, evecs = np.linalg.eigh(H)
        _EIGH_CACHE[key] = (evals, evecs.astype(complex))
    return _EIGH_CACHE[key]


class BarrierModel:
    """Hopping + barrier on Z_N (dense eigh), or flat (position-diagonal)."""

    def __init__(self, v0: float = BAR_V0, flat: bool = False,
                 mean_shift: float = 0.0, in_window: bool = False,
                 r2_shift: float = 0.0, fixed_windows: bool = False):
        self.flat = flat
        self.mean_shift = mean_shift        # data mutation: identity gate
        self.in_window = in_window          # packet starts inside W
        self.r2_shift = r2_shift            # data mutation: weight gate
        self.fixed_windows = fixed_windows  # mutation: degenerate exhaustion
        x = np.arange(N_BAR)
        self.x = x
        diag = np.zeros(N_BAR)
        diag[XC_BAR] += v0
        if flat:
            self.diag = diag                # H diagonal: evolution = phases
            self.evecs = None
        else:
            self.evals, self.evecs = _barrier_eigh(v0)
        if flat or in_window:
            self.psi0 = _packet(N_BAR, XC_BAR, -K0, BAR_KW)   # inside W
        else:
            self.psi0 = _packet(N_BAR, XC_BAR - BAR_X0_OFF, -K0, BAR_KW)

    def half_widths(self):
        if self.fixed_windows:
            return (BAR_HALF_WS[0],) * len(BAR_HALF_WS)
        return BAR_HALF_WS

    def evolve(self, psi: np.ndarray, t: float) -> np.ndarray:
        if self.flat:
            return np.exp(-1j * self.diag * t) * psi
        return self.evecs @ (np.exp(-1j * self.evals * t)
                             * (self.evecs.conj().T @ psi))

    def clamp(self, half_w: int) -> np.ndarray:
        a, b = XC_BAR - half_w, XC_BAR + half_w
        return (np.minimum(b, np.maximum(self.x, a - 1)) - (a - 1)).astype(float)

    def tpm_law(self, half_w: int, psi_early: np.ndarray):
        """Two-time TPM law {nu: p}, nu = q_- - q_+ (frozen convention)."""
        qv = self.clamp(half_w)
        spec = np.arange(0.0, 2 * half_w + 2.0)
        law: dict[float, float] = {}
        for q in spec:
            branch = psi_early * (np.abs(qv - q) < 1e-9)
            if float(np.linalg.norm(branch)) ** 2 < 1e-14:
                continue
            late = self.evolve(branch, BAR_T)
            for qp in spec:
                p = float(np.linalg.norm(late * (np.abs(qv - qp) < 1e-9))) ** 2
                if p > 1e-12:
                    nu = float(q - qp)
                    law[nu] = law.get(nu, 0.0) + p
        return law


def check_c5(m: BarrierModel, log) -> None:
    """ACE-LD-obst' mechanism configuration on a scattering model.

    Evidence gates: (a) incoming concentration; (b) BOTH atoms present —
    including the nu=0 atom r1's LD-C5 never produced; (c) atom weights
    match the independently measured |r|^2, |t|^2 (red mode
    --red-c5-weights falsifies that ground truth).
    Consistency lines, DISCLOSED as subsumed (r2 M4 — not independent
    evidence): (d) the first-moment identity sum nu p = <Q>_- - <Q>_+ —
    given gate (a) the incoming state is a single spectral branch, so the
    two sides are the same expression up to the concentration defect (the
    measured gap ~1e-11 tracks it); its red mode --red-c5-meanshift is a
    data mutation proving the comparison live, no more.  (e) the LR3 tail
    moment and its floor 0.9(1+|W|)|t|^2 — given (b)+(c) this is
    arithmetically 1 > 0.9; the growth clause is armed by
    --red-c5-fixedwin (degenerate exhaustion), the floor clause is
    unreachable in-class (subsumed) and is listed as such in the table.
    The two-branch dephasing content that (d) cannot certify in this
    configuration is exhibited by LD-C5b's wedge.
    """
    psiT = m.evolve(m.psi0, BAR_T)
    edge = float(np.sum(np.abs(psiT[:32]) ** 2) + np.sum(np.abs(psiT[-32:]) ** 2))
    require(edge < 1e-12, f"LD-C5: wavefront reached ring cut ({edge:.3e})")
    r2 = float(np.sum(np.abs(psiT[:XC_BAR]) ** 2)) + m.r2_shift
    t2 = float(np.sum(np.abs(psiT[XC_BAR:]) ** 2))
    moments = []
    for half_w in m.half_widths():
        qv = m.clamp(half_w)
        size_w = 2 * half_w + 1
        ldin = float(np.linalg.norm(m.psi0 * (np.abs(qv) > 1e-9)))
        require(ldin < 1e-4,
                f"LD-C5: incoming state not concentrated at q=0 "
                f"(defect {ldin:.3e}, |W|={size_w})")
        law = m.tpm_law(half_w, m.psi0)
        p0 = sum(p for nu, p in law.items() if abs(nu) < 0.5)
        ptr = sum(p for nu, p in law.items() if abs(nu + size_w) < 0.5)
        other = 1.0 - p0 - ptr
        require(p0 > 0.05,
                f"LD-C5: nu=0 (reflected) atom absent (p0={p0:.4f}, "
                f"|W|={size_w}) — the atom r1's certificate never produced")
        require(ptr > 0.05,
                f"LD-C5: nu=-|W| (transit) atom absent (p={ptr:.4f})")
        require(abs(other) < 1e-4,
                f"LD-C5: unexpected TPM mass off the two atoms "
                f"({other:.3e} at |W|={size_w})")
        require(abs(p0 - r2) < 1e-3,
                f"LD-C5: nu=0 weight {p0:.4f} != measured |r|^2 {r2:.4f}")
        require(abs(ptr - t2) < 1e-3,
                f"LD-C5: transit weight {ptr:.4f} != measured |t|^2 {t2:.4f}")
        smom = sum(nu * p for nu, p in law.items())
        mean_early = float((m.psi0.conj() @ (qv * m.psi0)).real) + m.mean_shift
        mean_late = float((psiT.conj() @ (qv * psiT)).real)
        ident = mean_early - mean_late
        require(abs(smom - ident) < 1e-4,
                f"LD-C5: first-moment identity violated at |W|={size_w}: "
                f"sum nu p = {smom:+.4f} vs <Q>_- - <Q>_+ = {ident:+.4f} "
                "(consistency line, subsumed by gate (a) — disclosed)")
        tail = sum((1.0 + abs(nu)) * p for nu, p in law.items()
                   if abs(nu) > BAR_M)
        moments.append((size_w, tail))
    for (w1, t1), (w2, t2m) in zip(moments, moments[1:]):
        require(t2m > t1,
                f"LD-C5: LR3 tail moment not growing: {t1:.3f} (|W|={w1}) "
                f"-> {t2m:.3f} (|W|={w2})")
    w_last, t_last = moments[-1]
    floor = 0.9 * (1.0 + w_last) * t2
    require(t_last > floor,
            f"LD-C5: tail moment {t_last:.3f} below linear floor {floor:.3f} "
            "(consistency line, subsumed by (b)+(c) — disclosed)")
    log(f"LD-C5 obstruction configuration: |r|^2={r2:.4f}, |t|^2={t2:.4f}; "
        "two-atom law {0, -|W|} incl. nu=0 atom; identity/tail consistency "
        "lines pass (disclosed as subsumed); LR3 tail "
        + " -> ".join(f"{tv:.2f}(|W|={w})" for w, tv in moments))


def _c5b_cesaro_defect(m: BarrierModel, span: float) -> float:
    """The D27(LR2) double-Cesaro dephasing defect on m.psi0 (state at t=0):

        mean over t_+ in [T, 2T], t_- in [-2T, -T]  of
        <D_{W,t_-}(Q_W(t_+))> - <Q_W(t_+)>,   T = span,

    on a C5B_LR2_GRID x C5B_LR2_GRID grid — the quantity D27(LR2) demands
    to vanish as T -> infinity (r3 M2: the t_- = 0 defect is NOT it).
    D_{W,t_-} dephases in the eigenbasis of Q_W(t_-): decompose the
    backward-evolved state into clamp-charge branches at t_-, evolve each
    branch to t_+, and sum the branch expectations of Q_W.
    """
    qv = m.clamp(C5B_HALF_W)
    spec = np.arange(0.0, 2 * C5B_HALF_W + 2.0)
    tms = np.linspace(-2.0 * span, -1.0 * span, C5B_LR2_GRID)
    tps = np.linspace(1.0 * span, 2.0 * span, C5B_LR2_GRID)
    total = 0.0
    if m.evecs is not None:                      # eigenbasis fast path
        V, E = m.evecs, m.evals
        c0 = V.conj().T @ m.psi0
        unp = {}
        for tp in tps:
            psi_p = V @ (np.exp(-1j * E * tp) * c0)
            unp[tp] = float((psi_p.conj() @ (qv * psi_p)).real)
        for tm in tms:
            psi_m = V @ (np.exp(-1j * E * tm) * c0)
            branches = [psi_m * (np.abs(qv - q) < 1e-9) for q in spec]
            bmat = np.stack([b for b in branches
                             if float(np.linalg.norm(b)) ** 2 > 1e-14],
                            axis=1)
            cb = V.conj().T @ bmat
            for tp in tps:
                bt = V @ (np.exp(-1j * E * (tp - tm))[:, None] * cb)
                pinched = float(np.sum((np.abs(bt) ** 2) * qv[:, None]))
                total += pinched - unp[tp]
    else:                                        # flat model: evolve() cheap
        for tm in tms:
            psi_m = m.evolve(m.psi0, tm)
            for tp in tps:
                psi_p = m.evolve(m.psi0, tp)
                unp = float((psi_p.conj() @ (qv * psi_p)).real)
                pinched = 0.0
                for q in spec:
                    br = psi_m * (np.abs(qv - q) < 1e-9)
                    if float(np.linalg.norm(br)) ** 2 < 1e-14:
                        continue
                    brt = m.evolve(br, tp - tm)
                    pinched += float((brt.conj() @ (qv * brt)).real)
                total += pinched - unp
    return total / (len(tms) * len(tps))


def _c5b_branch_weights(m: BarrierModel, tm: float):
    """(left q=0, inside-W, right q=|W|) clamp-branch weights at time tm."""
    qv = m.clamp(C5B_HALF_W)
    psi_m = m.evolve(m.psi0, tm)
    wl = float(np.sum(np.abs(psi_m[np.abs(qv) < 0.5]) ** 2))
    wr = float(np.sum(
        np.abs(psi_m[np.abs(qv - (2 * C5B_HALF_W + 1)) < 0.5]) ** 2))
    return wl, 1.0 - wl - wr, wr


def check_c5b(m: BarrierModel, log) -> None:
    """Two-branch dephasing certificate (r2 M4; re-anchored per r3 M2).

    Green configuration: the packet centred ON the barrier, inside the
    |W|=17 window — the incoming state is spread over many window
    charges, so the D27(LR2) pinching D_{t_-} genuinely acts.

    Two gates, certifying two DIFFERENT things (r3 M2):

    (a) WEDGE, at the single pair (t_-, t_+) = (0, 300): the two
        genuinely independent computations LD-C5(d) compares —
        sum nu p (TPM law) vs <Q>_{t_-} - <Q>_{t_+} (unpinched) — must
        disagree by more than C5B_WEDGE_MIN (measured ~6.08).  This
        certifies that D ACTS on a two-branch state, hence that
        LD-C5(d)'s agreement in the concentrated configuration is due to
        gate (a) there.  It does NOT certify that D27(LR2) fails: LR2
        averages over t_+ AND t_-, and --red-c5b-nobarrier (the V0 = 0
        straddling packet) passes this gate at 8.3868 while satisfying
        LR2 exactly (r3 M2(b)).
    (b) D27(LR2) DOUBLE-CESARO DEFECT (the corrected LR2-failure gate):
        |mean defect| must exceed C5B_LR2_MIN at every span in
        C5B_LR2_TS, and be stable across spans within C5B_LR2_STAB
        (measured: -3.3592 at T = 20 and 40; r3 M2(b) finds the same
        value out to T = 200).  Mechanism (logged, r3 M2(b)): under
        backward evolution the packet stays split across three
        window-charge branches (left/in/right ~ 0.8563/0.0170/0.1267),
        so the pinching never becomes trivial; the barrier bound state
        is NOT the cause (projecting it out leaves -3.4116, r3 M2(b)).

    Deliberately NOT shipped: an identity-with-D gate — the exact
    identity sum nu p = <Q>_{t_-} - <D_{t_-}(Q(t_+))> is ALGEBRA, and
    gating it against the same branch decomposition would be the
    campaign's no-op pattern (x = x); refusal certified by r3 n6.
    Also NOT claimed: MI <1>7.<2>2's averaged identity on any two-branch
    state — on this one its LR2 hypothesis fails (now measured at LR2's
    own quantity), which is the honest finding.
    """
    qv = m.clamp(C5B_HALF_W)
    law = m.tpm_law(C5B_HALF_W, m.psi0)
    smom = sum(nu * p for nu, p in law.items())
    psiT = m.evolve(m.psi0, BAR_T)
    mean_early = float((m.psi0.conj() @ (qv * m.psi0)).real)
    mean_late = float((psiT.conj() @ (qv * psiT)).real)
    naive = mean_early - mean_late
    wedge = abs(smom - naive)
    require(wedge > C5B_WEDGE_MIN,
            f"LD-C5b: dephasing wedge absent: sum nu p = {smom:+.4f} vs "
            f"<Q>_- - <Q>_+ = {naive:+.4f} (|gap| = {wedge:.3e} <= "
            f"{C5B_WEDGE_MIN}) — the pinching does not act, so this is "
            "not a two-branch configuration")
    defects = []
    for span in C5B_LR2_TS:
        d = _c5b_cesaro_defect(m, span)
        require(abs(d) > C5B_LR2_MIN,
                f"LD-C5b: D27(LR2) holds at its own quantity: double-Cesaro "
                f"mean defect {d:+.3e} within {C5B_LR2_MIN} at T={span:.0f} "
                "— 'D acts' does not imply 'LR2 fails' (r3 M2), and this "
                "state is not an LR2-failure witness")
        defects.append(d)
    spread = max(defects) - min(defects)
    require(spread < C5B_LR2_STAB,
            f"LD-C5b: double-Cesaro defect not T-stable: values "
            + ", ".join(f"{d:+.4f}" for d in defects)
            + f" spread {spread:.3e} >= {C5B_LR2_STAB}")
    w1 = _c5b_branch_weights(m, -2.0 * C5B_LR2_TS[-1])
    w2 = _c5b_branch_weights(m, -400.0)
    log(f"LD-C5b (straddling config, |W|={2*C5B_HALF_W+1}): wedge at "
        f"(t_-,t_+)=(0,300): sum nu p = {smom:+.4f} vs unpinched "
        f"{naive:+.4f}, wedge {wedge:.4f} > {C5B_WEDGE_MIN} — D genuinely "
        "acts (not the LR2 quantity); D27(LR2) double-Cesaro defect "
        + ", ".join(f"{d:+.4f} (T={t:.0f})"
                    for d, t in zip(defects, C5B_LR2_TS))
        + f", |defect| > {C5B_LR2_MIN} and T-stable — LR2 fails at its own "
        "quantity (r3 M2 corrected number); mechanism: backward branch "
        "weights left/in/right = "
        f"{w1[0]:.4f}/{w1[1]:.4f}/{w1[2]:.4f} at t_-={-2*C5B_LR2_TS[-1]:.0f}, "
        f"{w2[0]:.4f}/{w2[1]:.4f}/{w2[2]:.4f} at t_-=-400 — the split "
        "persists; the bound state is not the cause (r3 M2(b))")


# ------------------------------------------------------------- D16 battery --
class D16Model:
    """Open XXZ kink chain, exact diagonalisation in S^z sectors."""

    def __init__(self, delta: float = D16_DELTA, mixed: bool = False,
                 claimed_q: float = D16_CLAIMED_Q, product: bool = False,
                 no_boundary: bool = False, unflipped: bool = False):
        self.delta = delta
        self.mixed = mixed
        self.claimed_q = claimed_q
        self.product = product              # kink-free product sector
        self.no_boundary = no_boundary      # boundary field switched off
        self.unflipped = unflipped          # (K-TAIL) read WITHOUT the Z2
        #                                     conjugation (mutation: the ED
        #                                     ground state is the Z2-image
        #                                     of D13(a)'s orientation)
        self.L = D16_L

    @staticmethod
    def _sz(bit: int) -> float:
        return -0.5 if bit else 0.5

    def sector(self, ndown: int):
        L, J, delta = self.L, D16_J, self.delta
        states = [sum(1 << i for i in c)
                  for c in combinations(range(L), ndown)]
        idx = {s: i for i, s in enumerate(states)}
        n = len(states)
        H = np.zeros((n, n))
        bf = 0.0 if self.no_boundary else 0.5 * J * np.sqrt(delta ** 2 - 1.0)
        for s in states:
            i = idx[s]
            bits = [(s >> x) & 1 for x in range(L)]
            diag = 0.0
            for x in range(L - 1):
                szx, szx1 = self._sz(bits[x]), self._sz(bits[x + 1])
                diag += -J * delta * (szx * szx1 - 0.25) + bf * (szx - szx1)
                if bits[x] != bits[x + 1]:
                    H[idx[s ^ (1 << x) ^ (1 << (x + 1))], i] += -J * 0.5
            H[i, i] = diag
        return states, H

    def ground(self, ndown: int):
        states, H = self.sector(ndown)
        w, v = np.linalg.eigh(H)
        return states, w[0], v[:, 0]

    def window_stats(self, states, psi, a: int, b: int):
        """(<Q_W>, Var(Q_W)) for Q_W = sum_{x=a}^b S^z_x + s(a+b-1-2c0)."""
        scal = 0.5 * (a + b - 1 - 2 * D16_C0)
        qw = np.array([sum(self._sz((s >> (x - 1)) & 1)
                           for x in range(a, b + 1)) for s in states]) + scal
        mean = float(psi @ (qw * psi))
        var = float(psi @ ((qw - mean) ** 2 * psi))
        return mean, var

    def ktail_profile(self, states, psi):
        """||D_x phi|| for x outside the core K = D16_CORE.

        Green reading uses the Z2-FLIPPED tail assignment (down at -inf,
        up at +inf — the ED ground state's actual orientation, r2 m2);
        the --red-c7-orientation mutation uses D13(a)'s literal one.
        """
        lo, hi = D16_CORE
        rows = []       # (side, dist, ||D_x phi||)
        for x in range(1, self.L + 1):
            if lo <= x <= hi:
                continue
            left = x < lo
            if self.unflipped:
                s_tail = +0.5 if left else -0.5
            else:
                s_tail = -0.5 if left else +0.5
            dev2 = np.array([(self._sz((s >> (x - 1)) & 1) - s_tail) ** 2
                             for s in states])
            val = float(np.sqrt(psi @ (dev2 * psi)))
            dist = (lo - x) if left else (x - hi)
            rows.append(("L" if left else "R", dist, val))
        return rows

    def magnon_state(self):
        """S^-_site applied to the half-filled sector ground state."""
        nd = self.L // 2
        states6, _, psi6 = self.ground(nd)
        bit = C6_MAGNON_SITE - 1
        states7 = [sum(1 << i for i in c)
                   for c in combinations(range(self.L), nd + 1)]
        idx7 = {s: i for i, s in enumerate(states7)}
        psi7 = np.zeros(len(states7))
        for amp, s in zip(psi6, states6):
            if not (s >> bit) & 1:              # site is up: S^- acts
                psi7[idx7[s | (1 << bit)]] += amp
        n = float(np.linalg.norm(psi7))
        require(n > 0.5, f"LD-C6: magnon creation nearly annihilated the "
                         f"state (norm {n:.3e})")
        return states7, psi7 / n

    def c6_laws(self, tplus: float = C6_TPLUS):
        """TPM laws of the kink+magnon state at every D16 window, at
        protocol time tplus (default C6_TPLUS; the LD-C6 first-moment
        sweep passes the other C6_SWEEP times — r4, r3 M3)."""
        nd = self.L // 2
        states7, psi7 = self.magnon_state()
        _, H7 = self.sector(nd + 1)
        evals, evecs = np.linalg.eigh(H7)

        def evolve(v):
            return evecs @ (np.exp(-1j * evals * tplus)
                            * (evecs.T @ v.astype(complex)))

        out = []
        for (a, b) in D16_WINDOWS:
            scal = 0.5 * (a + b - 1 - 2 * D16_C0)
            qw = np.array([sum(self._sz((s >> (x - 1)) & 1)
                               for x in range(a, b + 1))
                           for s in states7]) + scal
            qs = np.unique(np.round(qw * 2) / 2)
            law: dict[float, float] = {}
            for q in qs:
                branch = psi7 * (np.abs(qw - q) < 1e-9)
                if float(np.linalg.norm(branch)) ** 2 < 1e-14:
                    continue
                late = evolve(branch)
                for qp in qs:
                    p = float(np.linalg.norm(
                        late * (np.abs(qw - qp) < 1e-9))) ** 2
                    if p > 1e-14:
                        nu = float(q - qp)
                        law[nu] = law.get(nu, 0.0) + p
            out.append((f"[{a},{b}]", b - a + 1, law))
        return out


class C6BarrierAdapter:
    """Runs the LD-C6 gates on a BARRIER-battery configuration.

    Used only by red modes: --red-c6-static (position-diagonal H — the r2
    tautology; must die at the LIVENESS gate), --red-c6-moving (the
    transiting scattering model; must die at the FIRST-MOMENT gate after
    the r4 reorder — measured 12.4024 at |W|=17, r3 M1(b)/M3), and
    --red-c6-weaktransit (v0 = 10, |t|^2 ~ 0.037: the first moment passes
    at |W|=17 so the SUPPORT gate is reached — arming the gate the r4
    reorder would otherwise shadow, r3 M3).

    The adapter's scattering protocol time is fixed (tpm_law uses BAR_T),
    so the LD-C6 t_+ sweep re-checks the same cached laws on this
    battery; every registered c6 mutant dies before the sweep anyway.
    """

    def __init__(self, flat: bool, v0: float = BAR_V0):
        self.base = BarrierModel(v0=v0, flat=flat, in_window=flat)
        self._laws = None

    def c6_laws(self, tplus: float = C6_TPLUS):
        del tplus                       # protocol time fixed; see docstring
        if self._laws is None:
            out = []
            for half_w in BAR_HALF_WS:
                law = self.base.tpm_law(half_w, self.base.psi0)
                out.append((f"|W|={2 * half_w + 1}", 2 * half_w + 1, law))
            self._laws = out
        return self._laws


def check_c6(m, log) -> None:
    """Bounded-transport contrast (r2 M3 rebuild: the r2 position-diagonal
    LD-C6 was a tautology — p_W = delta_0 for EVERY state under EVERY
    position-diagonal H — and is replaced.  r4, r3 M3: gate order and
    the first-moment bound repaired — see below).

    Green model: the D16 battery with ONE MAGNON added (S^- on the up
    tail of the half-filled kink ground state), evolved in its S^z
    sector.  The dynamics does NOT commute with Q_W.  Gates, in order:
    (a) BOUNDED FIRST MOMENT (evaluated FIRST — r4 reorder per r3 M3,
        so --red-c6-moving reaches it): sum |nu| p <= C6_MOM_BOUND at
        every window — non-extensive in |W| (the LR3 tail moment beyond
        BAR_M is then 0 at every window by (b), since C6_NU_MAX < BAR_M:
        stated, not separately gated — it is implied);
    (b) SUPPORT: TPM mass at |nu| > C6_NU_MAX below C6_SUPPORT_TOL at
        every window — one magnon transports a bounded charge, in
        contrast to LD-C5's transit atom at nu = -|W| (reached by
        --red-c6-weaktransit, whose first moment passes);
    (c) LIVENESS at the largest window: 1 - p_0 >= C6_LIVE_MIN — mass
        genuinely moves, so this battery CANNOT pass the way the r2
        tautology did;
    (d) t_+ SWEEP of the first moment (r4, r3 M3: the r3 bound 1.0 was
        calibrated to t_+ = 4 and the GREEN model fired it at t_+ = 20
        with 1.0712 — a time-tuned constant certifies nothing about
        bounded transport): sum |nu| p <= C6_MOM_BOUND at every window
        at EVERY t_+ in C6_SWEEP, with the sweep maximum logged;
        C6_MOM_BOUND sits above the recorded sweep maximum.  (The
        support and liveness gates stay at the protocol time t_+ = 4;
        the sweep extends the MOMENT claim only — disclosed in spec.)
    """
    rows = m.c6_laws()
    live = None
    for label, _, law in rows:
        mom = sum(abs(nu) * p for nu, p in law.items())
        require(mom <= C6_MOM_BOUND,
                f"LD-C6: first moment {mom:.4f} > {C6_MOM_BOUND} at "
                f"W={label}")
        mass_out = sum(p for nu, p in law.items() if abs(nu) > C6_NU_MAX)
        require(mass_out < C6_SUPPORT_TOL,
                f"LD-C6: TPM support not bounded at W={label}: mass "
                f"{mass_out:.3e} at |nu| > {C6_NU_MAX} (transit-scale "
                "transport — this is the LD-C5 side of the dichotomy)")
        p0 = sum(p for nu, p in law.items() if abs(nu) < 0.25)
        live = 1.0 - p0
    require(live is not None and live >= C6_LIVE_MIN,
            f"LD-C6: dynamics looks Q_W-commuting: 1 - p_0 = "
            f"{0.0 if live is None else live:.3e} < {C6_LIVE_MIN} at the "
            "largest window (the r2 tautology mode — a position-diagonal "
            "H gives p_W = delta_0 for every state)")
    sweep_max, sweep_arg = 0.0, ""
    for tplus in C6_SWEEP:
        rows_t = rows if tplus == C6_TPLUS else m.c6_laws(tplus)
        for label, _, law in rows_t:
            mom = sum(abs(nu) * p for nu, p in law.items())
            require(mom <= C6_MOM_BOUND,
                    f"LD-C6: first moment {mom:.4f} > {C6_MOM_BOUND} at "
                    f"W={label}, t_+={tplus:g} (sweep gate — the bound "
                    "must hold across the recorded protocol times, r3 M3)")
            if mom > sweep_max:
                sweep_max, sweep_arg = mom, f"t_+={tplus:g}, W={label}"
    parts = []
    for label, _, law in rows:
        p0 = sum(p for nu, p in law.items() if abs(nu) < 0.25)
        mom = sum(abs(nu) * p for nu, p in law.items())
        parts.append(f"{label}: 1-p0={1 - p0:.3f}, sum|nu|p={mom:.3f}")
    log("LD-C6 bounded-transport contrast (kink+magnon, [H,Q_W] != 0): "
        + "; ".join(parts)
        + f"; t_+ sweep {C6_SWEEP}: max sum|nu|p = {sweep_max:.4f} "
        f"({sweep_arg}) <= {C6_MOM_BOUND}")


def check_c7(m: D16Model, log) -> None:
    """The epsilon-version's measured decay on D16, and (K-TAIL) itself.

    Gates: (a) sector ground energies all 0 (certifies ONLY that — the
    theta = 0 fence rests on K1+K2 with K4 CONJECTURE, not on this gate;
    r2 M5); (b) min_q||(Q_W - q)Psi|| strictly positive at every window —
    the exact (AD3-ex) display is UNAVAILABLE at fixed W in D16 (r2 M6:
    this state is a magnon-free zero mode, not an (AD3-ex) vector, so
    this is not an in-class refutation); (c) successive defect ratios
    equal the claimed rate q within 2 percent — the lambda^{d_W} law of
    (LD.4)'s CONCLUSION; (d) <Q_W> on the integer coset; (e) NEW (r2 n5):
    (K-TAIL) itself — the one-site deviations ||D_x phi|| outside the
    core K, in the Z2-flipped orientation (r2 m2), fall at rate q per
    site with a bounded constant: the HYPOTHESIS, measured directly.
    """
    e0s = []
    for ndown in range(m.L + 1):
        _, H = m.sector(ndown)
        e0s.append(float(np.linalg.eigvalsh(H)[0]))
    worst = max(abs(e) for e in e0s)
    require(worst < D16_FLAT_TOL,
            f"LD-C7: sector ground energies not zero: max |E0| = {worst:.3e}")
    nd = 0 if m.product else m.L // 2
    states, e0, psi = m.ground(nd)
    if m.mixed:
        states_b, _, psi_b = m.ground(nd - 1)
    defects = []
    for (a, b) in D16_WINDOWS:
        mean, var = m.window_stats(states, psi, a, b)
        if m.mixed:
            mean_b, var_b = m.window_stats(states_b, psi_b, a, b)
            mu = 0.5 * (mean + mean_b)
            var = 0.5 * (var + (mean - mu) ** 2) \
                + 0.5 * (var_b + (mean_b - mu) ** 2)
            mean = mu
        defect = float(np.sqrt(var))
        require(defect > 1e-6,
                f"LD-C7: defect vanished at W=[{a},{b}] ({defect:.3e}) — "
                "an exact Q_W eigenvector, contradicting the D16 record")
        require(abs(mean - round(mean)) < D16_COSET_TOL,
                f"LD-C7: <Q_W> = {mean:+.6f} off the integer coset "
                f"at W=[{a},{b}]")
        defects.append(defect)
    ratios = [defects[i + 1] / defects[i] for i in range(len(defects) - 1)]
    for i, r in enumerate(ratios):
        require(abs(r / m.claimed_q - 1.0) < D16_RATE_RTOL,
                f"LD-C7: decay ratio {r:.4f} (step {i}) != claimed rate "
                f"q = {m.claimed_q:.6f} within {D16_RATE_RTOL:.0%}")
    # gate (e): (K-TAIL) itself (the hypothesis, not the conclusion)
    prof = m.ktail_profile(states, psi)
    cmax = 0.0
    for side, dist, val in prof:
        cmax = max(cmax, val * m.claimed_q ** (-dist))
    require(cmax <= D16_KTAIL_CBOUND,
            f"LD-C7: (K-TAIL) fails: max ||D_x phi|| lam^-dist = "
            f"{cmax:.3f} > {D16_KTAIL_CBOUND} (tail deviations not "
            "exponentially clustered at the claimed rate/orientation)")
    for side in ("L", "R"):
        vals = sorted([(d, v) for s, d, v in prof if s == side])
        for (d1, v1), (d2, v2) in zip(vals, vals[1:]):
            if v1 < 1e-12:
                continue
            r = v2 / v1
            require(abs(r / m.claimed_q - 1.0) < D16_KTAIL_RTOL,
                    f"LD-C7: (K-TAIL) profile ratio {r:.4f} on side {side} "
                    f"(dist {d1}->{d2}) != q = {m.claimed_q:.6f} "
                    f"within {D16_KTAIL_RTOL:.0%}")
    log("LD-C7 epsilon-version on D16: sector energies (max |E0| "
        f"{worst:.1e}); defects "
        + ", ".join(f"{d:.2e}" for d in defects)
        + "; ratios " + ", ".join(f"{r:.4f}" for r in ratios)
        + f" vs q = {m.claimed_q:.6f}; (K-TAIL) profile C_K = {cmax:.3f}, "
        "per-site ratio = q on both sides (Z2-flipped orientation)")


# --------------------------------------------------------------- red modes --
FREE_CHECKS = ("LD-C1", "LD-C2", "LD-C3", "LD-C4")

REGISTRY = {
    "gap": {"battery": "free",
            "build": lambda: FreeModel(q_scale=0.1, is_green=False),
            "must_break": {"LD-C1", "LD-C3"},
            "must_pass": {"LD-C2", "LD-C4"}},
    "coset": {"battery": "free",
              "build": lambda: FreeModel(coset_shift=np.sqrt(2.0) - 1.0,
                                         is_green=False),
              "must_break": {"LD-C1"},
              "must_pass": {"LD-C2", "LD-C3", "LD-C4"}},
    "halfspace": {"battery": "free",
                  "build": lambda: FreeModel(halfspace=True, is_green=False),
                  "must_break": {"LD-C1"},
                  "must_pass": {"LD-C2", "LD-C3", "LD-C4"}},
    "c1-overlap": {"battery": "free",
                   "build": lambda: FreeModel(overlap=True, is_green=False),
                   "must_break": {"LD-C1", "LD-C2", "LD-C4"},
                   "must_pass": {"LD-C3"}},
    "c1-leak": {"battery": "free",
                "build": lambda: FreeModel(leak=True, is_green=False),
                # measured pattern: the hard momentum cutoff leaves
                # position-space ringing at small qv, so LD-C2 breaks too
                # and LD-C3 survives (its rhs inflates with eps); the
                # LD-C1 exit path is the RESOLUTION sub-gate
                "must_break": {"LD-C1", "LD-C2", "LD-C4"},
                "must_pass": {"LD-C3"}},
    "merged": {"battery": "free",
               "build": lambda: FreeModel(merged=True, is_green=False),
               "must_break": {"LD-C2", "LD-C4"},
               "must_pass": {"LD-C1", "LD-C3"}},
    "dup": {"battery": "free",
            "build": lambda: FreeModel(dup_charge=True, is_green=False),
            "must_break": {"LD-C2", "LD-C4"},
            "must_pass": {"LD-C1", "LD-C3"}},
    "c5-nobarrier": {"battery": "barrier",
                     "build": lambda: BarrierModel(v0=0.0),
                     "must_break": {"LD-C5"}, "must_pass": set()},
    "c5-meanshift": {"battery": "barrier",
                     "build": lambda: BarrierModel(mean_shift=1.0),
                     "must_break": {"LD-C5"}, "must_pass": set()},
    "c5-inwindow": {"battery": "barrier",
                    "build": lambda: BarrierModel(in_window=True),
                    "must_break": {"LD-C5"}, "must_pass": set()},
    "c5-weights": {"battery": "barrier",
                   "build": lambda: BarrierModel(r2_shift=0.05),
                   "must_break": {"LD-C5"}, "must_pass": set()},
    "c5-fixedwin": {"battery": "barrier",
                    "build": lambda: BarrierModel(fixed_windows=True),
                    "must_break": {"LD-C5"}, "must_pass": set()},
    "c5b-flat": {"battery": "barrier2",
                 "build": lambda: BarrierModel(flat=True),
                 "must_break": {"LD-C5b"}, "must_pass": set()},
    "c5b-concentrated": {"battery": "barrier2",
                         "build": lambda: BarrierModel(),
                         "must_break": {"LD-C5b"}, "must_pass": set()},
    "c5b-nobarrier": {"battery": "barrier2",
                      # r3 M2's separator state: the V0 = 0 straddling
                      # packet PASSES the wedge gate (8.3868 at t_-=0,
                      # LARGER than green's 6.0832) yet satisfies
                      # D27(LR2) exactly — it must die at the
                      # double-Cesaro gate, proving the corrected gate
                      # separates 'D acts' from 'LR2 fails'
                      "build": lambda: BarrierModel(v0=0.0, in_window=True),
                      "must_break": {"LD-C5b"}, "must_pass": set()},
    "c6-static": {"battery": "c6",
                  "build": lambda: C6BarrierAdapter(flat=True),
                  "must_break": {"LD-C6"}, "must_pass": set()},
    "c6-moving": {"battery": "c6",
                  # post-reorder (r4, r3 M3) the exit path is the
                  # FIRST-MOMENT gate: 12.4024 at |W|=17
                  "build": lambda: C6BarrierAdapter(flat=False),
                  "must_break": {"LD-C6"}, "must_pass": set()},
    "c6-weaktransit": {"battery": "c6",
                       # v0 = 10: |t|^2 ~ 0.037, so the first moment
                       # passes at |W|=17 (0.6361 <= 1.2) and the
                       # SUPPORT gate is reached (mass 3.742e-02 at
                       # |nu| > 3) — arms the gate the r4 reorder
                       # shadows on every large-transit mutant (r3 M3)
                       "build": lambda: C6BarrierAdapter(flat=False,
                                                         v0=10.0),
                       "must_break": {"LD-C6"}, "must_pass": set()},
    "c7-delta": {"battery": "d16",
                 "build": lambda: D16Model(delta=3.0),
                 "must_break": {"LD-C7"}, "must_pass": set()},
    "c7-mixed": {"battery": "d16",
                 "build": lambda: D16Model(mixed=True),
                 "must_break": {"LD-C7"}, "must_pass": set()},
    "c7-product": {"battery": "d16",
                   "build": lambda: D16Model(product=True),
                   "must_break": {"LD-C7"}, "must_pass": set()},
    "c7-noboundary": {"battery": "d16",
                      "build": lambda: D16Model(no_boundary=True),
                      "must_break": {"LD-C7"}, "must_pass": set()},
    "c7-orientation": {"battery": "d16",
                       "build": lambda: D16Model(unflipped=True),
                       "must_break": {"LD-C7"}, "must_pass": set()},
}

FREE_FNS = {"LD-C1": check_c1, "LD-C2": check_c2,
            "LD-C3": check_c3, "LD-C4": check_c4}


def _run_battery(battery: str, model, log):
    """Return dict gate -> (ok, message)."""
    results = {}
    if battery == "free":
        for name in FREE_CHECKS:
            try:
                FREE_FNS[name](model, log)
                results[name] = (True, "pass")
            except CheckFailure as exc:
                results[name] = (False, str(exc))
    elif battery == "barrier":
        try:
            check_c5(model, log)
            results["LD-C5"] = (True, "pass")
        except CheckFailure as exc:
            results["LD-C5"] = (False, str(exc))
    elif battery == "barrier2":
        try:
            check_c5b(model, log)
            results["LD-C5b"] = (True, "pass")
        except CheckFailure as exc:
            results["LD-C5b"] = (False, str(exc))
    elif battery == "c6":
        try:
            check_c6(model, log)
            results["LD-C6"] = (True, "pass")
        except CheckFailure as exc:
            results["LD-C6"] = (False, str(exc))
    elif battery == "d16":
        try:
            check_c7(model, log)
            results["LD-C7"] = (True, "pass")
        except CheckFailure as exc:
            results["LD-C7"] = (False, str(exc))
    return results


def run_red(modes, log) -> int:
    """Exit 1 iff every requested mutation reproduces its pattern.

    Reports the EXIT PATH per mode: which gate fired, with its message
    (standing checker obligation: report the path, not only the code).
    """
    all_ok = True
    for mode in modes:
        reg = REGISTRY[mode]
        log(f"--- red mode '{mode}' (fresh mutated {reg['battery']} model) ---")
        results = _run_battery(reg["battery"], reg["build"](), lambda s: None)
        for name, (ok, msg) in sorted(results.items()):
            if name in reg["must_break"]:
                if ok:
                    log(f"  {name}: SURVIVED but registered to break "
                        "-- mutation not detected")
                    all_ok = False
                else:
                    log(f"  {name}: broken as registered — exit path: "
                        f"{msg[:160]}")
            else:
                if ok:
                    log(f"  {name}: survives as registered")
                else:
                    log(f"  {name}: UNREGISTERED CASUALTY — exit path: "
                        f"{msg[:160]}")
                    all_ok = False
    if all_ok:
        log("RED-OK: every mutation reproduced its registered pattern; "
            "exit 1 signals red-capability.")
        return 1
    log("RED-MISMATCH: pattern not reproduced; exit 2.")
    return 2


# --------------------------------------------------------------------- main --
def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--red", action="store_true",
                    help="run all registered mutations")
    for mode in REGISTRY:
        ap.add_argument(f"--red-{mode}", action="store_true")
    args = ap.parse_args(argv)

    def log(msg: str) -> None:
        print(msg)

    modes = list(REGISTRY) if args.red else [
        m for m in REGISTRY if getattr(args, f"red_{m.replace('-', '_')}")]
    if modes:
        return run_red(modes, log)

    try:
        m_free = FreeModel()
        check_c1(m_free, log)
        check_c2(m_free, log)
        check_c3(m_free, log)
        check_c4(m_free, log)
        check_c5(BarrierModel(), log)
        check_c5b(BarrierModel(in_window=True), log)
        check_c6(D16Model(), log)
        check_c7(D16Model(), log)
    except CheckFailure as exc:
        log(f"GREEN FAILURE: {exc}")
        return 3
    log("GREEN: LD-C1..LD-C7 all pass; exit 0.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
