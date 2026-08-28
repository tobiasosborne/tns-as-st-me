#!/usr/bin/env python3
"""Deterministic certificates LD-C1..LD-C5 for the ACE-LD shard.

Spec: ``theory/ace-ld.md`` section 5 (CHECKER SPEC).  House style follows
``theory/checks/memory_index_check.py`` and ``ansatz_scattering_check.py``:
every violation raises ``CheckFailure``, so all checks stay active under
``python3 -O``; there is not a single bare ``assert``.  Nothing here is
random and no check depends on a seed.

Model (one copy, constants block below): a single particle on the ring
Z_N, H = nearest-neighbour hopping (dispersion 2 cos k, group velocity
-2 sin k), FFT propagation, no wavefront ever reaching the ring cut (a
guard check enforces this).  The particle position models the kink bond
coordinate; the window charge is the D13(a) clamp

    Qhat |x> = clamp_W(x) |x>,   clamp_W(x) = min(b, max(x, a-1)) - (a-1),

spectrum {0, 1, ..., |W|} -- one coset of Z, separation 1 (LD-C1 checks
this arithmetic, it does not assume it).  Channels are the exact momentum
sign projections P_+ (right-movers, sin k < 0) and P_- (left-movers,
sin k >= 0); both commute with H exactly and LD-C1 verifies it numerically.

    LD-C1  hypothesis audit (spectrum, coset, gap, commutation, resolution)
    LD-C2  first-moment escape eps_ch(t) -> 0          (ACE-LD-esc surface)
    LD-C3  the inequality (LD.1) WITH its constant, at every grid time
    LD-C4  spectral diagonality at the final time       (the (AD3-ex) form)
    LD-C5  obstruction arithmetic of <1>6.<2>2: two-time TPM nu-values are
           {-|W|, +|W|} and the D27(LR3) tail moment grows linearly in |W|

Red modes.  Each mutation is built as a FRESH model variant (the green
model objects are never mutated in place; "copies, not the original", per
the work order).  Each names, in REGISTRY below, the checks it MUST break
and the checks registered to survive; a red run reproduces that pattern
exactly or exits 2, so a surviving target and an unregistered casualty are
both failures.

    --red-coset    Qhat -> Qhat/10 with charges q/10 but the coset-lemma
                   constant d = 1 retained: the separation >= 1 supplied by
                   M-INDEX-fin is destroyed.  Breaks LD-C1 and LD-C3.
    --red-merged   channels merged into P_1 = P_+ + P_- with one claimed
                   charge: the channel charge is indefinite.  Breaks LD-C2
                   and LD-C4 (this is ACE-LD-nec's mechanism).
    --red-dup      both channels claimed at the SAME charge q_+ (the
                   same-side regime of <1>5.<2>3).  Breaks LD-C2 and LD-C4
                   for the '-' channel; LD-C3 survives BY DESIGN (each
                   single-q gap bound (LD.3) is still true; it is the
                   cross-term step of (LD.1) whose proof needs distinctness,
                   and the refutation surfaces in LD-C4, not LD-C3).
    --red          all three in sequence; exit 1 iff every mode reproduces
                   its registered pattern, else exit 2.

Green exits 0.  LD-C5 runs in green mode only (registered NOT-RUN in red).
"""

from __future__ import annotations

import argparse
import sys

import numpy as np

# --------------------------------------------------------------- constants --
N_RING = 8192
X_C = N_RING // 2
HALF_W = 16                       # window half-width: W = [X_C-16, X_C+16]
K0 = np.pi / 2                    # packet momentum magnitude
K_WIDTH = 0.6                     # momentum bump half-width
C_MINUS = 0.8                     # left-mover amplitude  (channel '-')
C_PLUS = 0.6                      # right-mover amplitude (channel '+')
TIMES = (4, 8, 16, 32, 64, 128, 256, 512, 1024)
TOL_CONV = 1e-6                   # final-time convergence tolerance
TOL_EXACT = 1e-9                  # machine-precision identities
TOL_INEQ = 1e-9                   # slack for the certified inequality
TPM_T = 256                       # two-time protocol half-span for LD-C5
TPM_HALF_WS = (8, 16, 32, 64)     # growing windows for LD-C5
TPM_M = 10                        # tail threshold M in the LR3 moment


class CheckFailure(Exception):
    """A certificate violation.  Never a bare assert (python3 -O safe)."""


def require(cond: bool, msg: str) -> None:
    if not cond:
        raise CheckFailure(msg)


# ------------------------------------------------------------------- model --
def momenta() -> np.ndarray:
    return 2.0 * np.pi * np.fft.fftfreq(N_RING)


def bump(u: np.ndarray) -> np.ndarray:
    """C_c^infinity mollifier profile on |u| < 1."""
    out = np.zeros_like(u)
    inside = np.abs(u) < 1.0
    out[inside] = np.exp(1.0 - 1.0 / (1.0 - u[inside] ** 2))
    return out


def packet(k_center: float) -> np.ndarray:
    """Unit-norm packet, momentum bump about k_center, centred at X_C."""
    k = momenta()
    amp = bump((k - k_center) / K_WIDTH) * np.exp(-1j * k * X_C)
    psi = np.fft.ifft(amp)
    return psi / np.linalg.norm(psi)


class Model:
    """The green model; red variants are fresh instances with overrides."""

    def __init__(self, half_w: int = HALF_W, q_scale: float = 1.0,
                 merged: bool = False, dup_charge: bool = False):
        self.a = X_C - half_w
        self.b = X_C + half_w
        self.size_w = self.b - self.a + 1
        x = np.arange(N_RING)
        self.qvals = (np.minimum(self.b, np.maximum(x, self.a - 1))
                      - (self.a - 1)).astype(float) * q_scale
        self.spec = np.unique(self.qvals)
        k = momenta()
        self.disp = 2.0 * np.cos(k)
        self.mask_plus = (np.sin(k) < 0.0)          # right-movers
        self.mask_minus = ~self.mask_plus           # left-movers (incl. 0, pi)
        self.phi_plus = packet(-K0)                 # v = +2 sin(K0) > 0
        self.phi_minus = packet(+K0)                # v < 0
        self.psi0 = C_MINUS * self.phi_minus + C_PLUS * self.phi_plus
        self.psi0 = self.psi0 / np.linalg.norm(self.psi0)
        self.w_minus = abs(np.vdot(self.phi_minus, self.psi0))
        self.w_plus = abs(np.vdot(self.phi_plus, self.psi0))
        q_top = float(self.size_w) * q_scale
        if merged:
            # one channel, everything, one claimed charge: indefinite.
            self.channels = [("1", None, q_top)]
        elif dup_charge:
            self.channels = [("+", self.mask_plus, q_top),
                             ("-", self.mask_minus, q_top)]
        else:
            self.channels = [("+", self.mask_plus, q_top),
                             ("-", self.mask_minus, 0.0)]
        # claimed gap constant: 1/d with d = 1, the coset separation the
        # abstract lemma certifies via M-INDEX-fin.  Red mode 1 keeps this
        # while shrinking the true separation -- that is the mutation.
        self.claimed_inv_gap = 1.0

    # -- linear algebra ------------------------------------------------------
    def evolve(self, psi: np.ndarray, t: float) -> np.ndarray:
        return np.fft.ifft(np.exp(-1j * self.disp * t) * np.fft.fft(psi))

    def project_channel(self, psi: np.ndarray, mask) -> np.ndarray:
        if mask is None:
            return psi.copy()
        return np.fft.ifft(np.fft.fft(psi) * mask)

    def spectral_proj(self, psi: np.ndarray, q: float) -> np.ndarray:
        return psi * (np.abs(self.qvals - q) < 1e-9)

    def apply_q(self, psi: np.ndarray) -> np.ndarray:
        return self.qvals * psi

    def guard_no_wrap(self, psi: np.ndarray, label: str) -> None:
        cutmass = float(np.sum(np.abs(psi[:64]) ** 2)
                        + np.sum(np.abs(psi[-64:]) ** 2))
        require(cutmass < 1e-16,
                f"guard: wavefront reached the ring cut in {label} "
                f"(mass {cutmass:.3e})")


# ------------------------------------------------------------ certificates --
def check_c1(m: Model, log) -> None:
    """Hypothesis audit."""
    frac = np.abs(m.spec - np.round(m.spec))
    require(float(frac.max()) < 1e-12,
            "LD-C1: spectrum is not integer (coset broken): "
            f"max frac {float(frac.max()):.3e}")
    gaps = np.diff(np.sort(m.spec))
    require(float(gaps.min()) >= 1.0 - 1e-12,
            f"LD-C1: spectral separation {float(gaps.min()):.3e} < 1")
    # commutation [P_ch, H] = 0 on the fixed test vector psi0
    for name, mask, _ in m.channels:
        lhs = m.project_channel(np.fft.ifft(m.disp * np.fft.fft(m.psi0)), mask)
        rhs = np.fft.ifft(m.disp * np.fft.fft(m.project_channel(m.psi0, mask)))
        err = float(np.linalg.norm(lhs - rhs))
        require(err < TOL_EXACT, f"LD-C1: [P_{name}, H] != 0 ({err:.3e})")
    # mutual orthogonality and resolution of psi0
    if len(m.channels) == 2:
        p1 = m.project_channel(m.psi0, m.channels[0][1])
        p12 = m.project_channel(p1, m.channels[1][1])
        require(float(np.linalg.norm(p12)) < TOL_EXACT,
                "LD-C1: channel projections not orthogonal")
    total = sum(m.project_channel(m.psi0, mask) for _, mask, _ in m.channels)
    err = float(np.linalg.norm(total - m.psi0))
    require(err < TOL_EXACT, f"LD-C1: sum P_ch psi != psi ({err:.3e})")
    log("LD-C1 hypothesis audit: spectrum integer, gap >= 1, "
        "[P,H]=0, orthogonal, resolving")


def channel_data(m: Model, t: float):
    """Return per-channel (name, P_ch psi_t, eps_ch) and psi_t."""
    psi_t = m.evolve(m.psi0, t)
    m.guard_no_wrap(psi_t, f"t={t}")
    rows = []
    for name, mask, q in m.channels:
        pch = m.project_channel(psi_t, mask)
        eps = float(np.linalg.norm(m.apply_q(pch) - q * pch))
        rows.append((name, q, pch, eps))
    return psi_t, rows


def check_c2(m: Model, log) -> None:
    """First-moment escape."""
    first, final = {}, {}
    for t in TIMES:
        _, rows = channel_data(m, t)
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


def check_c3(m: Model, log) -> None:
    """The inequality (LD.1) with its claimed constant, at every time."""
    worst = -np.inf
    for t in TIMES:
        psi_t, rows = channel_data(m, t)
        rhs = sum(eps for _, _, _, eps in rows) * m.claimed_inv_gap
        for name, q, pch, _ in rows:
            lhs = float(np.linalg.norm(m.spectral_proj(psi_t, q) - pch))
            slack = rhs + TOL_INEQ * (1.0 + rhs) - lhs
            worst = max(worst, lhs - rhs)
            require(slack >= 0.0,
                    f"LD-C3: (LD.1) violated at t={t}, channel {name}: "
                    f"lhs {lhs:.6e} > rhs {rhs:.6e}")
    log(f"LD-C3 inequality (LD.1) holds at all times "
        f"(worst lhs-rhs margin {worst:.2e})")


def check_c4(m: Model, log) -> None:
    """Spectral diagonality at the final time (the (AD3-ex) form)."""
    t = TIMES[-1]
    psi_t, rows = channel_data(m, t)
    for name, q, pch, _ in rows:
        lhs = float(np.linalg.norm(m.spectral_proj(psi_t, q) - pch))
        require(lhs < TOL_CONV,
                f"LD-C4: ||E({{q_{name}}})psi_t - P_{name} psi_t|| "
                f"= {lhs:.3e} >= {TOL_CONV} at t={t}")
    log(f"LD-C4 diagonality at t={t}: all channels < {TOL_CONV}")


def check_c5(log) -> None:
    """Obstruction arithmetic: TPM nu in {-|W|,+|W|}, LR3 moment grows."""
    moments = []
    for half_w in TPM_HALF_WS:
        m = Model(half_w=half_w)
        psi_early = m.evolve(m.psi0, -TPM_T)
        m.guard_no_wrap(psi_early, f"t=-{TPM_T}")
        law = {}
        for q in m.spec:
            branch = m.spectral_proj(psi_early, q)
            wgt = float(np.linalg.norm(branch)) ** 2
            if wgt < 1e-14:
                continue
            late = m.evolve(branch, 2 * TPM_T)
            for qp in m.spec:
                p = float(np.linalg.norm(m.spectral_proj(late, qp))) ** 2
                if p > 1e-14:
                    nu = float(q - qp)          # MI <1>5 convention nu=q_- - q_+
                    law[nu] = law.get(nu, 0.0) + p
        size_w = float(m.size_w)
        expected = {-size_w: m.w_plus ** 2, +size_w: m.w_minus ** 2}
        for nu, p in law.items():
            near = [e for e in expected if abs(e - nu) < 0.5]
            require(bool(near) or p < 1e-6,
                    f"LD-C5: unexpected TPM outcome nu={nu} (p={p:.3e}) "
                    f"at |W|={int(size_w)}")
        for nu_e, p_e in expected.items():
            got = sum(p for nu, p in law.items() if abs(nu - nu_e) < 0.5)
            require(abs(got - p_e) < 1e-4,
                    f"LD-C5: TPM weight at nu={nu_e} is {got:.6f}, "
                    f"expected {p_e:.6f}")
        tail = sum((1.0 + abs(nu)) * p for nu, p in law.items()
                   if abs(nu) > TPM_M)
        moments.append((int(size_w), tail))
    for (w1, t1), (w2, t2) in zip(moments, moments[1:]):
        require(t2 > t1,
                f"LD-C5: LR3 tail moment not growing: {t1:.3f} (|W|={w1}) "
                f"-> {t2:.3f} (|W|={w2})")
    w_last, t_last = moments[-1]
    floor = 0.9 * (1.0 + w_last) * min(C_MINUS, C_PLUS) ** 2
    require(t_last > floor,
            f"LD-C5: tail moment {t_last:.3f} below linear floor {floor:.3f}")
    log("LD-C5 obstruction: TPM nu-support {-|W|,+|W|}, LR3 tail moment "
        + " -> ".join(f"{t:.2f}(|W|={w})" for w, t in moments))


# --------------------------------------------------------------- red modes --
GREEN_CHECKS = ("LD-C1", "LD-C2", "LD-C3", "LD-C4")

REGISTRY = {
    "coset": {"build": lambda: Model(q_scale=0.1),
              "must_break": {"LD-C1", "LD-C3"},
              "must_pass": {"LD-C2", "LD-C4"}},
    "merged": {"build": lambda: Model(merged=True),
               "must_break": {"LD-C2", "LD-C4"},
               "must_pass": {"LD-C1", "LD-C3"}},
    "dup": {"build": lambda: Model(dup_charge=True),
            "must_break": {"LD-C2", "LD-C4"},
            "must_pass": {"LD-C1", "LD-C3"}},
}

CHECK_FNS = {"LD-C1": check_c1, "LD-C2": check_c2,
             "LD-C3": check_c3, "LD-C4": check_c4}


def run_battery(m: Model, log):
    """Run LD-C1..C4 on model m; return dict name -> (ok, message)."""
    results = {}
    for name in GREEN_CHECKS:
        try:
            CHECK_FNS[name](m, log)
            results[name] = (True, "pass")
        except CheckFailure as exc:
            results[name] = (False, str(exc))
    return results


def run_red(modes, log) -> int:
    """Exit 1 iff every requested mutation reproduces its pattern."""
    all_ok = True
    for mode in modes:
        reg = REGISTRY[mode]
        log(f"--- red mode '{mode}' (fresh mutated model copy) ---")
        results = run_battery(reg["build"](), lambda s: None)
        for name in GREEN_CHECKS:
            ok, msg = results[name]
            if name in reg["must_break"]:
                if ok:
                    log(f"  {name}: SURVIVED but registered to break "
                        f"-- mutation not detected")
                    all_ok = False
                else:
                    log(f"  {name}: broken as registered ({msg[:90]})")
            else:
                if ok:
                    log(f"  {name}: survives as registered")
                else:
                    log(f"  {name}: UNREGISTERED CASUALTY: {msg[:90]}")
                    all_ok = False
        log("  LD-C5: not run in red modes (registered NOT-RUN)")
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
                    help="run all three registered mutations")
    ap.add_argument("--red-coset", action="store_true")
    ap.add_argument("--red-merged", action="store_true")
    ap.add_argument("--red-dup", action="store_true")
    args = ap.parse_args(argv)

    def log(msg: str) -> None:
        print(msg)

    modes = []
    if args.red:
        modes = ["coset", "merged", "dup"]
    else:
        if args.red_coset:
            modes.append("coset")
        if args.red_merged:
            modes.append("merged")
        if args.red_dup:
            modes.append("dup")
    if modes:
        return run_red(modes, log)

    m = Model()
    try:
        check_c1(m, log)
        check_c2(m, log)
        check_c3(m, log)
        check_c4(m, log)
        check_c5(log)
    except CheckFailure as exc:
        log(f"GREEN FAILURE: {exc}")
        return 3
    log("GREEN: LD-C1..LD-C5 all pass; exit 0.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
