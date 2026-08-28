#!/usr/bin/env python3
"""Deterministic certificates ACE-C1 and ACE-C2 for claim AC-EX.

Spec: ``theory/ansatz-scattering.md`` section 4 (CHECKER SPEC), frozen at
commit ``b53809a``.  Written to clear the AC-EX HOLD of
``theory/verdicts/memory-index-r2.md`` section 4, whose missing step is
exactly "the two specified certificates ACE-C1 and ACE-C2 are not
implemented".  House style follows ``theory/checks/memory_index_check.py``:
every violation raises ``CheckFailure``, so all checks stay active under
``python3 -O``; there is not a single bare ``assert``.

    ACE-C1a  band data, velocity separation, Remark D28-R fence
    ACE-C1b  propagation and contact-defect decay      (ACE-SP, ACE-Cook cone)
    ACE-C2a  the literal theta-commutator defect        (<1>5.<2>2, as specced)
    ACE-C2b  the Cook cone majorant, kernel decay       (<1>5.<2>4 regime (i))

The model is the spec's, unmodified; the constants block below is its only
copy.  Nothing here is random and no check depends on a seed.

Red modes.  Each mutation names, in MUTATIONS below, the checks it MUST
break and the checks it is registered to leave standing; a red run
reproduces that pattern exactly or exits 2, so a surviving target and an
unregistered casualty are both failures.

    --red-equal-velocity  equal dispersions and momentum packets: the cone
                          separation of D28(4) is destroyed.  Breaks all four.
    --red-slow-kernel     h -> h_slow(m) = c<m>^-2 at equal l^1 norm.  Breaks
                          ACE-C2b; ACE-C2a survives BY DESIGN, SPEC NOTE 2.
    --red-absorption      Delta_M -> 0.2.  Breaks ACE-C1a and nothing else.
                          FENCE REGRESSION GUARD ONLY: Remark D28-R's
                          thresholds are used in no step of <1>3--<1>7 (r1
                          objection 2, r2 R9 row 2), so this mutation can
                          catch no error in the proof and must NOT be
                          reported as a red test of AC-EX.
    --red                 all three at once; every check must then break.

A red run prints RED-OK and exits 1 when the registered pattern is
reproduced, and exits 2 otherwise.  Green exits 0.  Spec deviations are
recorded in SPEC_NOTES and printed at the end of a green run.  L2 is
self-reported: 572 lines, ~70 over the band, the overrun being the four
checks' printed evidence and the two registered mutation ledgers.
"""

from __future__ import annotations

import argparse
import sys
from collections import namedtuple

import numpy as np

# --------------------------------------------------------------- constants --
N_LATTICE = 8192
TIMES = (128, 256, 512, 1024, 2048, 4096)
KINK_AMP = 0.16
MAGNON_AMP = 0.6
MAGNON_GAP = 1.0
ABSORPTION_GAP = 0.2
PACKET_P = (0.05, 0.15)
PACKET_K = (0.65, 0.75)
FILTER_KNOTS = (0.5, 0.6, 0.8, 0.9)
DEFECT_REACH = 3
STEP_WIDTH = 4.0
THRESHOLD_INEL = 2.0

GATE_W_K = 0.32
GATE_GAP = 1.0
GATE_ENERGY_SUP = 1.163
GATE_VELOCITY_SEP = 0.33
GATE_EXPONENT = -2.0
GATE_RATIO = 0.30
GATE_LAST_CONTRIB = 0.26

C1_REFERENCE = (0.1888, 0.0844, 0.0166, 0.00241, 0.000228, 0.0000105)
REF_TOLERANCE = 0.02
CHUNK = 256

SPEC_NOTES = [
    "ACE-C1/C2 model arithmetic is the spec's, unmodified: the six reference "
    "values of ACE-C1 are reproduced to better than 0.4% by the normalised "
    "C_c^inf bumps exp(-1/(1-u^2)), which fixes the packet convention the "
    "spec left implicit.",
    "ACE-C2 SPLIT (the one substantive deviation).  The spec's C_theta(t) is "
    "the EXACT l^2(x,y) defect norm; run red-first, its --red-slow-kernel "
    "mutation is DEAD there -- c<m>^-2 reproduces the green doubling "
    "exponents to two decimals and only rescales C_theta by a constant 0.29, "
    "so both gates still pass.  Mechanism: on a fixed pair of separating "
    "C_c^inf packets the kernel is a bounded Fourier multiplier and the rate "
    "is set by the packets' off-cone tail, not the kernel -- the phase "
    "cancellation the proof's triangle inequality discards.  What "
    "<1>5.<2>4 (i) integrates is the cone majorant of "
    "S(u) = sum_m |h(m)||theta(u)-theta(u+m)| against an O(1) packet norm "
    "(r1 objection 1(ii)'s own formula).  Both are implemented: ACE-C2a "
    "carries the literal object with the dead mutation REGISTERED and "
    "asserted, ACE-C2b the majorant and the working red test.",
    "ACE-C2b evaluates S(u) on the true integer lattice (theta is the step, "
    "not its periodisation) while ACE-C2a convolves circularly on Z_N.  The "
    "finite lattice truncates the c<m>^-2 tail at |m| = N/2, which "
    "UNDERSTATES the slow kernel at the largest times: conservative in the "
    "direction that matters.",
    "--red-absorption is retained only as a fence regression guard and is "
    "registered as such (r1 objection 2 / r2 R9 row 2); it is not counted as "
    "a red test of AC-EX.  Neither certificate touches (D28-C), which the "
    "spec leaves to a separate certificate on an explicit kink frame.",
]

Mutations = namedtuple("Mutations", "equal_velocity absorption slow_kernel")
GREEN = Mutations(False, False, False)


class CheckFailure(Exception):
    """Raised by ``fail``; never caught outside ``run``, never optimised away."""


def fail(message: str) -> None:
    raise CheckFailure(message)


def require(condition: bool, message: str) -> None:
    if not condition:
        fail(message)


# ------------------------------------------------------------ band toolbox --

def smooth_bump(grid: np.ndarray, lo: float, hi: float) -> np.ndarray:
    """C_c^inf bump exp(-1/(1-u^2)), support exactly [lo, hi]."""
    u = (2.0 * grid - (lo + hi)) / (hi - lo)
    out = np.zeros_like(u)
    inside = np.abs(u) < 1.0
    out[inside] = np.exp(-1.0 / (1.0 - u[inside] ** 2))
    return out


def _ramp(u: np.ndarray) -> np.ndarray:
    """C^inf monotone 0 -> 1 transition on [0,1]."""
    def psi(v):
        out = np.zeros_like(v)
        good = v > 0.0
        out[good] = np.exp(-1.0 / v[good])
        return out
    a, b = psi(u), psi(1.0 - u)
    total = a + b
    return np.where(total > 0.0, a / np.where(total > 0.0, total, 1.0), 0.0)


def plateau(grid: np.ndarray, k0: float, k1: float, k2: float,
            k3: float) -> np.ndarray:
    """C_c^inf, identically 1 on [k1,k2], supported in [k0,k3]."""
    out = np.zeros_like(grid)
    up = (grid >= k0) & (grid < k1)
    out[up] = _ramp((grid[up] - k0) / (k1 - k0))
    out[(grid >= k1) & (grid <= k2)] = 1.0
    down = (grid > k2) & (grid <= k3)
    out[down] = _ramp((k3 - grid[down]) / (k3 - k2))
    return out


class Model:
    """The spec's lattice, bands, packets, step and kernels under a mutation."""

    def __init__(self, mut: Mutations):
        self.mut = mut
        n = N_LATTICE
        index = np.arange(n)
        self.k = 2.0 * np.pi * index / n
        self.x = np.where(index < n // 2, index, index - n).astype(float)
        self.order = np.argsort(self.x)

        self.gap = ABSORPTION_GAP if mut.absorption else MAGNON_GAP
        self.omega = self.gap + MAGNON_AMP * (1.0 - np.cos(self.k))
        if mut.equal_velocity:
            self.kink_band = self.omega
            self.packet_p = PACKET_K
        else:
            self.kink_band = KINK_AMP * (1.0 - np.cos(self.k))
            self.packet_p = PACKET_P

        self.fhat = self._normalised(self.packet_p)
        self.ghat = self._normalised(PACKET_K)
        self.filter = plateau(self.k, *FILTER_KNOTS)
        self.h_symbol = self.omega * self.filter
        self.h_gamma = np.fft.ifft(self.h_symbol)
        scale = float(np.sum(np.abs(self.h_gamma)))
        slow = 1.0 / (1.0 + self.x ** 2)
        self.h_slow = slow * (scale / float(np.sum(slow)))
        self.h_slow_symbol = np.fft.fft(self.h_slow)

        density = smooth_bump(self.x, -STEP_WIDTH, STEP_WIDTH)
        cumulative = np.zeros(n)
        cumulative[self.order] = np.cumsum(density[self.order])
        step = cumulative / cumulative.max()
        self.theta = np.where(self.x <= -STEP_WIDTH, 0.0,
                              np.where(self.x >= STEP_WIDTH, 1.0, step))
        self._packets: dict[int, tuple[np.ndarray, np.ndarray]] = {}

    def _normalised(self, window) -> np.ndarray:
        hat = smooth_bump(self.k, *window).astype(complex)
        return hat / np.linalg.norm(np.fft.ifft(hat))

    def packets(self, t: float) -> tuple[np.ndarray, np.ndarray]:
        if t not in self._packets:
            self._packets[t] = (
                np.fft.ifft(self.fhat * np.exp(-1j * t * self.kink_band)),
                np.fft.ifft(self.ghat * np.exp(-1j * t * self.omega)))
        return self._packets[t]

    def relative_law(self, t: float) -> np.ndarray:
        """P_t(u) = sum_x |f_t(x)|^2 |g_t(x+u)|^2, a probability on Z_N."""
        f, g = self.packets(t)
        fa, ga = np.abs(f) ** 2, np.abs(g) ** 2
        return np.fft.ifft(np.conj(np.fft.fft(fa)) * np.fft.fft(ga)).real

    def kernel_symbol(self, slow: bool) -> np.ndarray:
        return self.h_slow_symbol if slow else self.h_symbol

    def kernel(self, slow: bool) -> np.ndarray:
        return self.h_slow.astype(complex) if slow else self.h_gamma

    def s_profile(self, slow: bool) -> np.ndarray:
        """S(u) = sum_m |h(m)| |theta(u) - theta(u+m)| on the integer lattice."""
        weights = np.abs(self.kernel(slow))[self.order]
        positions = self.x[self.order]
        theta = self.theta[self.order]
        partial = np.concatenate(([0.0], np.cumsum(weights)))
        total = partial[-1]
        values = np.empty(positions.size)
        for i, u in enumerate(positions):
            above = int(np.searchsorted(positions, STEP_WIDTH - u, "left"))
            below = int(np.searchsorted(positions, -STEP_WIDTH - u, "right"))
            here = theta[i]
            value = (1.0 - here) * (total - partial[above]) + here * partial[below]
            if above > below:
                middle = positions[below:above]
                inner = np.interp(u + middle, positions, theta)
                value += float(np.sum(weights[below:above] * np.abs(here - inner)))
            values[i] = value
        out = np.empty(positions.size)
        out[self.order] = values
        return out

    def defect_norm(self, t: float, slow: bool) -> float:
        """C_theta(t), the exact l^2(x,y) norm of the theta-commutator defect."""
        symbol = self.kernel_symbol(slow)
        f, g = self.packets(t)
        weight = np.abs(f) ** 2
        smoothed = np.fft.ifft(np.fft.fft(g) * symbol)
        rows = np.arange(N_LATTICE)
        total = 0.0
        for start in range(0, N_LATTICE, CHUNK):
            xs = rows[start:start + CHUNK]
            shifted = self.theta[(rows[None, :] - xs[:, None]) % N_LATTICE]
            cut = 1.0 - shifted
            carried = np.fft.ifft(
                np.fft.fft(cut * g[None, :], axis=1) * symbol[None, :], axis=1)
            defect = cut * smoothed[None, :] - carried
            total += float(np.dot(weight[xs],
                                  np.sum(np.abs(defect) ** 2, axis=1)))
        return float(np.sqrt(total))


# ------------------------------------------------------------- gate toolbox --

def gate_verdict(values) -> tuple[bool, bool, list[float], list[float],
                                  list[float]]:
    """(decay gate, Cook-tail gate, exponents, contributions, ratios)."""
    span = range(len(values) - 1)
    exponents = [float(np.log2(values[i + 1] / values[i])) for i in span]
    contributions = [0.5 * (values[i] + values[i + 1])
                     * (TIMES[i + 1] - TIMES[i]) for i in span]
    ratios = [contributions[i + 1] / contributions[i]
              for i in range(len(contributions) - 1)]
    decay = all(e < GATE_EXPONENT for e in exponents[-3:])
    tail = all(r < GATE_RATIO for r in ratios[-2:])
    return decay, tail, exponents, contributions, ratios


def fmt(values, spec="%.3f") -> str:
    return "[" + ", ".join(spec % v for v in values) + "]"


# ----------------------------------------------------------------- ACE-C1a --

def check_c1_bands(model: Model) -> list[str]:
    """Band data, the cone separation of D28(4), and the Remark D28-R fence."""
    bandwidth = float(model.kink_band.max() - model.kink_band.min())
    gap = float(model.omega.min())
    _, hi_p = model.packet_p
    lo_k, hi_k = PACKET_K
    # both bands are increasing on the packet windows, so the extrema are the
    # window endpoints; taken analytically, not off the momentum grid.
    if model.mut.equal_velocity:
        kink_top = model.gap + MAGNON_AMP * (1.0 - np.cos(hi_p))
        kink_velocity = MAGNON_AMP * np.sin(hi_p)
    else:
        kink_top = KINK_AMP * (1.0 - np.cos(hi_p))
        kink_velocity = KINK_AMP * np.sin(hi_p)
    energy_sup = float(kink_top + model.gap
                       + MAGNON_AMP * (1.0 - np.cos(hi_k)))
    magnon_velocity = float(MAGNON_AMP * np.sin(lo_k))
    separation = magnon_velocity - float(kink_velocity)

    if not model.mut.equal_velocity:
        require(abs(bandwidth - GATE_W_K) < 1e-12,
                f"ACE-C1a: kink bandwidth W_K = {bandwidth:.6f}, want {GATE_W_K}")
        require(energy_sup < GATE_ENERGY_SUP,
                f"ACE-C1a: packet energy sup {energy_sup:.6f} is not "
                f"< {GATE_ENERGY_SUP}")
        require(energy_sup < THRESHOLD_INEL,
                f"ACE-C1a: packet energy sup {energy_sup:.6f} reaches the "
                f"two-magnon threshold {THRESHOLD_INEL}")
    require(separation > GATE_VELOCITY_SEP,
            f"ACE-C1a: velocity separation {separation:.6f} is not "
            f"> {GATE_VELOCITY_SEP} (D28(4) cone separation)")
    require(abs(gap - GATE_GAP) < 1e-12,
            f"ACE-C1a: magnon gap Delta_M = {gap:.6f}, want {GATE_GAP}")
    require(gap - bandwidth > 0.0,
            f"ACE-C1a: Remark D28-R fence Delta_M - W_K = {gap-bandwidth:.6f} "
            f"is not > 0 (FENCE ARITHMETIC ONLY -- used in no proof step)")
    return [f"  W_K = {bandwidth:.6f}, Delta_M = {gap:.6f}, "
            f"packet energy sup = {energy_sup:.7f} < {GATE_ENERGY_SUP} "
            f"< Theta_inel = {THRESHOLD_INEL}",
            f"  velocity separation eps_v = {separation:.6f} > "
            f"{GATE_VELOCITY_SEP} (magnon {magnon_velocity:.6f}, kink "
            f"{kink_velocity:.6f})",
            f"  Remark D28-R fence Delta_M - W_K = {gap-bandwidth:.4f} > 0 "
            f"-- fence arithmetic, consumed by no step of <1>3--<1>7"]


# ----------------------------------------------------------------- ACE-C1b --

def check_c1_decay(model: Model) -> list[str]:
    """C(t) = || V exp(-i t H_0)(f x g) ||_2 and the Cook tail (ACE-SP)."""
    reach = np.abs(model.x) <= DEFECT_REACH
    values = []
    for t in TIMES:
        law = model.relative_law(t)
        require(abs(law.sum() - 1.0) < 1e-9,
                f"ACE-C1b: relative law has mass {law.sum():.12f} at t={t}")
        contact = float(np.sqrt(max(np.sum(law[reach]), 0.0)))
        f, g = model.packets(t)
        direct = float(np.sqrt(sum(
            np.dot(np.abs(f) ** 2, np.roll(np.abs(g) ** 2, -d))
            for d in range(-DEFECT_REACH, DEFECT_REACH + 1))))
        require(abs(contact - direct) < 1e-12,
                f"ACE-C1b: FFT and direct contact norms disagree by "
                f"{abs(contact-direct):.3e} at t={t}")
        values.append(contact)

    if model.mut == GREEN:
        drift = max(abs(v - r) / r for v, r in zip(values, C1_REFERENCE))
        require(drift < REF_TOLERANCE,
                f"ACE-C1b: worst relative departure from the spec's reference "
                f"values is {drift:.4f}")
    decay, tail, exponents, contributions, ratios = gate_verdict(values)
    require(decay,
            f"ACE-C1b: last three doubling exponents {fmt(exponents[-3:])} "
            f"are not all < {GATE_EXPONENT}")
    require(contributions[-1] < GATE_LAST_CONTRIB,
            f"ACE-C1b: last Cook interval contributes {contributions[-1]:.4f}, "
            f"not < {GATE_LAST_CONTRIB}")
    require(tail,
            f"ACE-C1b: last two Cook contribution ratios {fmt(ratios[-2:])} "
            f"are not both < {GATE_RATIO}")
    return [f"  C(t) at t=128..4096: " + fmt(values, "%.6e"),
            f"  doubling exponents {fmt(exponents)}; Cook contributions "
            + fmt(contributions, "%.4e"),
            f"  last contribution {contributions[-1]:.4f} < "
            f"{GATE_LAST_CONTRIB}, last two ratios {fmt(ratios[-2:])} < "
            f"{GATE_RATIO}"]


# ----------------------------------------------------------------- ACE-C2a --

def check_c2_defect(model: Model) -> list[str]:
    """The literal spec object: the exact l^2 theta-commutator defect."""
    slow = model.mut.slow_kernel
    values = [model.defect_norm(t, slow) for t in TIMES]
    decay, tail, exponents, _, ratios = gate_verdict(values)
    require(decay,
            f"ACE-C2a: last three doubling exponents {fmt(exponents[-3:])} "
            f"are not all < {GATE_EXPONENT}")
    require(tail,
            f"ACE-C2a: last two Cook contribution ratios {fmt(ratios[-2:])} "
            f"are not both < {GATE_RATIO}")
    lines = [f"  C_theta(t) at t=128..4096: " + fmt(values, "%.6e"),
             f"  doubling exponents {fmt(exponents)}, last two Cook ratios "
             + fmt(ratios[-2:])]

    if model.mut == GREEN:
        mutated = [model.defect_norm(t, True) for t in TIMES]
        m_decay, m_tail, m_exp, _, m_ratio = gate_verdict(mutated)
        require(m_decay and m_tail,
                "ACE-C2a: the --red-slow-kernel mutation is LIVE on the exact "
                "defect after all; SPEC NOTE 2 registers it as dead and must "
                "be revisited")
        drift = max(abs(a - b) for a, b in zip(exponents, m_exp))
        require(drift < 0.1,
                f"ACE-C2a: registered exponent agreement broken, worst "
                f"difference {drift:.4f}")
        ratio = [m / v for m, v in zip(mutated, values)]
        lines.append(
            f"  REGISTERED DEAD MUTATION (SPEC NOTE 2): c<m>^-2 gives "
            + fmt(mutated, "%.4e"))
        lines.append(
            f"  exponents {fmt(m_exp)} agree to {drift:.3f}; the kernel only "
            f"rescales by " + fmt(ratio, "%.3f"))
    return lines


# ----------------------------------------------------------------- ACE-C2b --

def check_c2_majorant(model: Model) -> list[str]:
    """The Cook cone majorant of <1>5.<2>4 (i) -- kernel decay is load-bearing."""
    slow = model.mut.slow_kernel
    profile = model.s_profile(slow)
    radii = (256, 512, 1024, 2048)
    tails = [float(np.sum(np.abs(model.kernel(slow))[np.abs(model.x) >= r]))
             for r in radii]
    slope = float(np.polyfit(np.log(radii), np.log(tails), 1)[0])

    values = []
    for t in TIMES:
        law = model.relative_law(t)
        values.append(float(np.sqrt(np.sum(profile ** 2 * law))))
    decay, tail, exponents, contributions, ratios = gate_verdict(values)
    require(decay,
            f"ACE-C2b: last three doubling exponents {fmt(exponents[-3:])} "
            f"are not all < {GATE_EXPONENT}; kernel tail slope {slope:.3f}")
    require(tail,
            f"ACE-C2b: last two Cook contribution ratios {fmt(ratios[-2:])} "
            f"are not both < {GATE_RATIO}; kernel tail slope {slope:.3f}")
    require(slope < -4.0,
            f"ACE-C2b: the filtered kernel's tail slope is {slope:.3f}, not "
            f"< -4 -- h_gamma = omega*chit is not rapidly decreasing")
    lines = [f"  kernel tail sum_{{|m|>=R}}|h| at R=256..2048 "
             + fmt(tails, "%.4e") + f", fitted slope {slope:.3f} < -4",
             f"  M(t) at t=128..4096: " + fmt(values, "%.6e"),
             f"  doubling exponents {fmt(exponents)}, last two Cook ratios "
             + fmt(ratios[-2:]) + f" < {GATE_RATIO}"]

    if model.mut == GREEN:
        mutated_profile = model.s_profile(True)
        mutated = [float(np.sqrt(np.sum(mutated_profile ** 2
                                        * model.relative_law(t))))
                   for t in TIMES]
        m_decay, m_tail, m_exp, _, m_ratio = gate_verdict(mutated)
        m_tails = [float(np.sum(np.abs(model.kernel(True))
                                [np.abs(model.x) >= r])) for r in radii]
        m_slope = float(np.polyfit(np.log(radii), np.log(m_tails), 1)[0])
        require(not m_decay and not m_tail,
                f"ACE-C2b: the --red-slow-kernel mutation is DEAD -- decay "
                f"gate {m_decay}, Cook tail gate {m_tail}, exponents "
                f"{fmt(m_exp)}")
        require(-1.8 < m_exp[-1] < -1.0,
                f"ACE-C2b: mutated last doubling exponent {m_exp[-1]:.3f} is "
                f"not on its way to the predicted -1")
        require(m_ratio[-1] > 0.6,
                f"ACE-C2b: mutated last Cook ratio {m_ratio[-1]:.3f} is not on "
                f"its way to the predicted 1")
        require(-1.4 < m_slope < -0.9,
                f"ACE-C2b: the c<m>^-2 tail slope is {m_slope:.3f}, not the "
                f"predicted -1")
        lines.append(f"  MUTANT c<m>^-2: tail slope {m_slope:.3f} (predicted "
                     f"-1), M(t) " + fmt(mutated, "%.4e"))
        lines.append(f"  MUTANT exponents {fmt(m_exp)} -> -1 and Cook ratios "
                     + fmt(m_ratio) + " -> 1: BOTH gates fail, as specified")
    return lines


# -------------------------------------------------------------------- main --

CHECKS = [
    ("ACE-C1a", "band data, cone separation, D28-R fence", check_c1_bands),
    ("ACE-C1b", "propagation and contact-defect decay", check_c1_decay),
    ("ACE-C2a", "exact theta-commutator defect (literal spec object)",
     check_c2_defect),
    ("ACE-C2b", "Cook cone majorant: kernel decay is load-bearing",
     check_c2_majorant),
]

ALL_CHECKS = tuple(name for name, _, _ in CHECKS)

MUTATIONS = {
    "equal-velocity": (
        Mutations(True, False, False), ALL_CHECKS,
        "cone separation of D28(4) destroyed"),
    "slow-kernel": (
        Mutations(False, False, True), ("ACE-C2b",),
        "h -> c<m>^-2 at equal l^1 norm; ACE-C2a survives by design "
        "(SPEC NOTE 2)"),
    "absorption": (
        Mutations(False, True, False), ("ACE-C1a",),
        "FENCE REGRESSION GUARD ONLY -- not a red test of AC-EX"),
}


def run(mut: Mutations) -> list[tuple[str, str, bool, list[str], str]]:
    model = Model(mut)
    results = []
    for name, title, function in CHECKS:
        try:
            results.append((name, title, True, function(model), ""))
        except CheckFailure as exc:
            results.append((name, title, False, [], str(exc)))
    return results


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--red", action="store_true",
                        help="apply every mutation at once; all checks fail")
    for flag in MUTATIONS:
        parser.add_argument(f"--red-{flag}", action="store_true",
                            help=MUTATIONS[flag][2])
    args = parser.parse_args()
    chosen = [name for name in MUTATIONS
              if getattr(args, f"red_{name.replace('-', '_')}")]
    if args.red:
        chosen = list(MUTATIONS)

    if chosen:
        mut = Mutations(*(any(MUTATIONS[c][0][i] for c in chosen)
                          for i in range(3)))
        targets = set()
        for name in chosen:
            targets.update(MUTATIONS[name][1])
        results = run(mut)
        print(f"RED MUTATION TABLE  ({', '.join(chosen)})")
        wrong = []
        for name, title, ok, _, why in results:
            expected = name in targets
            verdict = ("caught  " if not ok else "SURVIVED") if expected else \
                      ("standing" if ok else "COLLAPSED")
            print(f"  {name}  {verdict}  {title}")
            if why:
                print(f"              {why}")
            if ok == expected:
                wrong.append(name)
        if wrong:
            print(f"FAIL: registration not reproduced by {', '.join(wrong)} -- "
                  "a surviving target or an unregistered casualty",
                  file=sys.stderr)
            raise SystemExit(2)
        print("RED-OK: every registered target broke, every registered "
              "survivor stood")
        raise SystemExit(1)

    results = run(GREEN)
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
    for note in SPEC_NOTES:
        print(f"  - {note}")
    print()
    print("PASS: AC-EX propagation certificates ACE-C1 and ACE-C2")


if __name__ == "__main__":
    main()
