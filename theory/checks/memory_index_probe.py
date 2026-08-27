#!/usr/bin/env python3
"""Pre-registered falsifier probe for Theorem M-INDEX (Lane T1).

Target under test: `briefs/memory-campaign-target.md`, Lane T1 (G-IDX.0/2/3).
The claim is that the asymptotic OUTCOME DISTRIBUTION of the windowed
regularized wall charge Q_W sits on a fixed integer coset with NO channel
assumptions, so every memory outcome is an integer multiple of 1/(2s).

Model: the D16 frozen-boundary easy-axis spin-1/2 XXZ ferromagnet of
`numerics/docs/kink-sector-notes.md` sec. 1,

    H = - sum_{x=1}^{N-1} [ (Jperp/2)(S+_x S-_{x+1} + h.c.) + Jz S^z_x S^z_{x+1} ],
    Jperp = 1, Delta = Jz/Jperp = 2,  site 1 frozen UP, site N frozen DOWN.

Exact diagonalization in the conserved-S^z sector, sparse Chebyshev
propagation, numpy/scipy only.  Two sector spaces are used:
  * the FULL S^z sector (no truncation) -- exact, but N <= 22 is the ceiling,
    which is too short to hold a clean ballistic window (see below);
  * the <= dwmax domain-wall space P H P of kink-sector-notes sec. 2 --
    Hermitian, hence exactly unitary, and validated here against the full
    sector at N = 22 before being used at N = 37 and N = 50.

Conventions fixed once (D13-style calibration, time independent):

    rho_vac(x) = +1/2 for x <= b0,  -1/2 for x > b0      (b0 = t=0 wall bond)
    Q_W = sum_{x in W} ( S^z_x - rho_vac(x) )            (integer valued)
    delta_x(point) = Q_W / (2s) = Q_W  lattice sites     (s = 1/2)

S^z bookkeeping (kink-sector-notes sec. 4): the in-sector kink+magnon state has
n_down = N - b0.  A transmitted magnon leaves an up-bubble on the down side and
the wall moves to b0-2, so Q_W = -2.  A reflected magnon leaves Q_W = 0.  The
merged/absorbed 1-domain-wall state of the same sector sits at wall b0-1, i.e.
Q_W = -1; an outgoing bubble of width 2 sits at Q_W = -3.  Those extra integers
are ALLOWED by M-INDEX (they are other channels, not a violation) -- what would
falsify the theorem is mass OFF the integer lattice.

Labelling note (reported both ways).  The task text asks for support on
{nu = 0, nu = -1}; the brief's own formula delta_x = -(1/2s) sum nu p_nu
together with G-IDX.3 ("supported on {0,2} with p_2 = <N_T>") makes the
transmission point nu = +2 with nu := -Q_W.  Both name the same physics: two
points, transmission = wall displaced by -2 sites.  Tables below are indexed by
the convention-free Q_W value; predicted support Q_W in {0, -2}, equivalently
nu = -Q_W in {0, +2}, equivalently delta_x in {0, -2} lattice sites.

State preparation (kink-sector-notes sec. 3).  The in-state is the DRESSED
kink -- the exact ground state of the pure-kink S^z sector -- acted on by the
modulated lowering operator O = sum_y e^{i k0 y} g(y) S^-_y.  The cheaper SHARP
kink is kept as a labelled control: at Delta = 2 it carries |<sharp|K>|^2 =
0.923, i.e. a 7.7% excitation defect that radiates as near-threshold magnon
pairs and puts ~5% of the outcome mass on the extra integers Q_W = -1, -3.
That is a preparation artefact, not scattering, and the contrast between the
two rows below is the evidence.  Only dressed ASYMPTOTIC rows gate P3/P4.

Truncation caveat, stated because it is a trap: dwmax = 3 gives a spuriously
PERFECT two-point distribution.  A dressed kink already needs 3 walls, so a
dressed kink plus a magnon needs 5; the 3-wall space cannot host kink dressing
at all and therefore cannot produce any other outcome by construction.  It is
included below as an illustration, NOT as a convergence control.  The real
convergence control is dwmax = 5 against the exact full sector at N = 22.

Pre-registered PASS criteria:
  P1  t=0 sharpness + D13 calibration: >= 0.99 of the mass on ONE lattice
      point, and that point is Q_W = 0.                       [every geometry]
  P2  integrality (the actual M-INDEX content, G-IDX.0/2): at every reported
      time and every window, the mass further than 1e-9 from an integer is
      <= 1e-11.                                               [every geometry]
  P3  two-point concentration (the H-AD-G corollary G-IDX.3): at the latest
      good time the mass outside {Q_W = 0, Q_W = -2} is < 0.05 for the
      reference window.                             [gating geometries only]
  P4  mean match: delta_x read off {p_nu} and the direct wall-position
      estimator X1 (windowed gradient centroid, kink-sector-notes sec. 3)
      agree to < 0.1 lattice sites at the latest good time.
                                                    [gating geometries only]
  P5  truncation control: the <= 5 domain-wall space reproduces the full
      sector's p_nu at N = 22 to < 0.01 at every reported time.

A geometry gates P3/P4 iff it is ASYMPTOTIC -- its clean ballistic window
(t_clear .. t_back, both from group velocity) is at least 6 sites of travel
long -- AND its in-state is the dressed kink.  Both are properties of the
geometry known before any state is evolved, not a post-hoc selection.
Full-sector N = 22 gives only ~3 sites of travel: its transmitted product
bounces off the frozen right end back into the window, so it anchors P1/P2/P5
and reports P3/P4 as diagnostics only.

Exit codes: 0 PASS, 1 FAIL (and, under --red, 1 means the mutation was caught
-- "RED-OK"), 2 red mutation NOT caught (checker is not red-capable).
Explicit failures only, so ``python3 -O`` is equally strict.

Modes:  (default) full probe   --red  rho_vac += 0.3 everywhere, must fail
        --selftest  6-site smoke tests of the probe machinery
"""

from __future__ import annotations

import argparse
import itertools
import math
import sys
from dataclasses import dataclass

import numpy as np
import scipy.sparse as sparse
import scipy.sparse.linalg as splinalg
from scipy.special import jv

TOL_LATTICE = 1.0e-9
TOL_OFFMASS = 1.0e-11
TOL_NORM = 1.0e-9
TOL_ENERGY = 1.0e-7
TOL_EXACT = 1.0e-12
SHARP_MIN = 0.99
STRADDLE_MAX = 0.05
MEAN_TOL = 0.1
TRUNCATION_TOL = 0.01
LEAKAGE_TOL = 0.02
ASYMPTOTIC_TRAVEL = 6.0
RED_RHO_SHIFT = 0.3
SPIN_S = 0.5
PREDICTED_SUPPORT = (0, -2)


def fail(message: str) -> None:
    print(f"FAIL: {message}", file=sys.stderr)
    raise SystemExit(1)


def require(condition: bool, message: str) -> None:
    if not condition:
        fail(message)


@dataclass(frozen=True)
class Geometry:
    """Chain, wall bond, reference window and incoming packet."""

    name: str
    n_sites: int
    wall: int          # sites 1..wall UP, wall+1..n_sites DOWN at t = 0
    win_lo: int
    win_hi: int
    y0: int            # packet centre (physical site, in the UP region)
    sigma: float
    k0: float
    dwmax: int | None = None   # None = full S^z sector
    dressed: bool = False      # dressed (sector ground state) vs sharp kink
    delta: float = 2.0
    jperp: float = 1.0
    dt: float = 0.25


HALF_PI = 0.5 * math.pi
GEOMETRIES = (
    Geometry("A-full-N22-sharp", n_sites=22, wall=13, win_lo=9, win_hi=16,
             y0=5, sigma=1.0, k0=1.4, dwmax=None),
    Geometry("A-dw5-N22-sharp", n_sites=22, wall=13, win_lo=9, win_hi=16,
             y0=5, sigma=1.0, k0=1.4, dwmax=5),
    Geometry("C-dw5-N37-dressed", n_sites=37, wall=20, win_lo=16, win_hi=23,
             y0=8, sigma=1.6, k0=HALF_PI, dwmax=5, dressed=True),
    Geometry("D-dw5-N50-dressed", n_sites=50, wall=26, win_lo=22, win_hi=29,
             y0=10, sigma=1.6, k0=HALF_PI, dwmax=5, dressed=True),
    Geometry("D-dw5-N50-sharp", n_sites=50, wall=26, win_lo=22, win_hi=29,
             y0=10, sigma=1.6, k0=HALF_PI, dwmax=5),
    Geometry("D-dw3-N50-sharp", n_sites=50, wall=26, win_lo=22, win_hi=29,
             y0=10, sigma=1.6, k0=HALF_PI, dwmax=3),
)
TRUNCATION_PAIRS = (("A-full-N22-sharp", "A-dw5-N22-sharp"),)


# ---------------------------------------------------------------- sector ---

def range_bits(low: int, high: int, n_sites: int) -> int:
    """Mask bits for dynamical sites low..high (bit i is site 2+i)."""
    low = max(low, 2)
    high = min(high, n_sites - 1)
    if high < low:
        return 0
    return ((1 << (high - low + 1)) - 1) << (low - 2)


def full_sector_masks(n_sites: int, n_down: int) -> np.ndarray:
    n_bits = n_sites - 2
    total = math.comb(n_bits, n_down)
    return np.fromiter(
        (sum(1 << i for i in combo)
         for combo in itertools.combinations(range(n_bits), n_down)),
        dtype=np.int64,
        count=total,
    )


def domain_wall_masks(n_sites: int, n_down: int, dwmax: int) -> np.ndarray:
    """Configurations with at most dwmax domain walls, enumerated by walls.

    Wall w sits on the bond (w, w+1).  With site 1 UP and site N DOWN the wall
    count is odd; walls w_1<...<w_d give DOWN on (w_1,w_2], (w_3,w_4], ...,
    (w_d, N].
    """
    out: list[int] = []
    for count in range(1, dwmax + 1, 2):
        for walls in itertools.combinations(range(1, n_sites), count):
            total = n_sites - walls[-1]
            for i in range(0, count - 1, 2):
                total += walls[i + 1] - walls[i]
            if total - 1 != n_down:
                continue
            mask = range_bits(walls[-1] + 1, n_sites, n_sites)
            for i in range(0, count - 1, 2):
                mask |= range_bits(walls[i] + 1, walls[i + 1], n_sites)
            out.append(mask)
    require(bool(out), "empty domain-wall sector")
    return np.array(sorted(out), dtype=np.int64)


def sector_masks(geom: Geometry, n_down: int) -> np.ndarray:
    if geom.dwmax is None:
        return np.sort(full_sector_masks(geom.n_sites, n_down))
    return domain_wall_masks(geom.n_sites, n_down, geom.dwmax)


def locate(masks: np.ndarray, wanted: np.ndarray):
    """searchsorted lookup; returns (positions, validity)."""
    position = np.searchsorted(masks, wanted)
    position = np.clip(position, 0, masks.size - 1)
    return position, masks[position] == wanted


def domain_walls(masks: np.ndarray, n_sites: int) -> np.ndarray:
    full = (masks << 1) | (1 << (n_sites - 1))
    changes = full ^ (full >> 1)
    return np.bitwise_count(changes & ((1 << (n_sites - 1)) - 1))


def site_sz(masks: np.ndarray, geom: Geometry, site: int) -> np.ndarray:
    if site == 1:
        return np.full(masks.size, 0.5)
    if site == geom.n_sites:
        return np.full(masks.size, -0.5)
    return 0.5 - ((masks >> (site - 2)) & 1).astype(np.float64)


def hamiltonian(masks: np.ndarray, geom: Geometry) -> sparse.csr_matrix:
    """H bond by bond; hopping only between two dynamical sites."""
    diagonal = np.zeros(masks.size)
    previous = site_sz(masks, geom, 1)
    for site in range(1, geom.n_sites):
        current = site_sz(masks, geom, site + 1)
        diagonal -= geom.jperp * geom.delta * previous * current
        previous = current

    rows, cols = [], []
    index = np.arange(masks.size, dtype=np.int64)
    for i in range(geom.n_sites - 3):
        differ = ((masks >> i) & 1) != ((masks >> (i + 1)) & 1)
        moved = masks[differ] ^ ((1 << i) | (1 << (i + 1)))
        target, ok = locate(masks, moved)
        if geom.dwmax is None:
            require(bool(ok.all()), "hopping left the full S^z sector")
        rows.append(target[ok])
        cols.append(index[differ][ok])
    rows = np.concatenate(rows)
    cols = np.concatenate(cols)
    data = np.full(rows.size, -0.5 * geom.jperp)
    off = sparse.csr_matrix((data, (rows, cols)),
                            shape=(masks.size, masks.size))
    return (off + sparse.diags(diagonal)).tocsr()


def packet_amplitude(geom: Geometry, y: int) -> complex:
    envelope = math.exp(-((y - geom.y0) ** 2) / (4.0 * geom.sigma ** 2))
    return envelope * complex(math.cos(geom.k0 * y), math.sin(geom.k0 * y))


def sharp_initial_state(masks: np.ndarray, geom: Geometry) -> np.ndarray:
    """Sharp kink at `wall` tensored with a Gaussian right-moving magnon."""
    base = range_bits(geom.wall + 1, geom.n_sites, geom.n_sites)
    psi = np.zeros(masks.size, dtype=complex)
    for y in range(2, geom.wall + 1):
        amplitude = packet_amplitude(geom, y)
        if abs(amplitude) < 1.0e-18:
            continue
        position, ok = locate(masks, np.array([base | (1 << (y - 2))]))
        require(bool(ok[0]), f"magnon basis state at y={y} missing")
        psi[position[0]] = amplitude
    return psi


def dressed_initial_state(masks: np.ndarray, geom: Geometry):
    """O|K> with |K> the pure-kink sector ground state (the dressed wall).

    O = sum_y e^{i k0 y} g(y) S^-_y, kink-sector-notes sec. 3.  Returns the
    projected vector, the sharp-kink overlap and an incoherent estimate of the
    weight the dwmax projection removes.
    """
    kink_masks = sector_masks(geom, geom.n_sites - 1 - geom.wall)
    values, vectors = splinalg.eigsh(hamiltonian(kink_masks, geom), k=1,
                                     which="SA")
    ground = vectors[:, 0].astype(complex)
    sharp = range_bits(geom.wall + 1, geom.n_sites, geom.n_sites)
    where, ok = locate(kink_masks, np.array([sharp]))
    require(bool(ok[0]), "sharp kink missing from the pure-kink sector")
    overlap = float(abs(ground[where[0]]) ** 2)

    psi = np.zeros(masks.size, dtype=complex)
    kept = dropped = 0.0
    for y in range(2, geom.wall + 1):
        amplitude = packet_amplitude(geom, y)
        if abs(amplitude) < 1.0e-18:
            continue
        bit = 1 << (y - 2)
        source = np.nonzero((kink_masks & bit) == 0)[0]   # S^-_y needs UP
        target, alive = locate(masks, kink_masks[source] | bit)
        weight = (abs(amplitude) ** 2) * np.abs(ground[source]) ** 2
        kept += float(weight[alive].sum())
        dropped += float(weight[~alive].sum())
        np.add.at(psi, target[alive], amplitude * ground[source[alive]])
    leakage = dropped / (kept + dropped) if kept + dropped > 0.0 else 1.0
    return psi, overlap, leakage, float(values[0])


def initial_state(masks: np.ndarray, geom: Geometry):
    if geom.dressed:
        psi, overlap, leakage, energy = dressed_initial_state(masks, geom)
        note = (f"dressed kink (pure-kink GS E={energy:.6f}, "
                f"|<sharp|K>|^2={overlap:.5f}, projection leakage="
                f"{leakage:.2e})")
        require(leakage < LEAKAGE_TOL,
                f"{geom.name}: projection leakage {leakage:.3e} too large")
    else:
        psi = sharp_initial_state(masks, geom)
        note = "sharp kink (control: carries the kink's excitation defect)"
    norm = np.linalg.norm(psi)
    require(norm > 0.0, "empty initial packet")
    return psi / norm, note


# ----------------------------------------------------------- observables ---

def rho_vac(geom: Geometry, shift: float) -> np.ndarray:
    """Time-independent vacuum density profile, calibrated on the t=0 wall."""
    sites = np.arange(1, geom.n_sites + 1)
    return np.where(sites <= geom.wall, 0.5, -0.5) + shift


def qw_values(masks: np.ndarray, geom: Geometry, window: tuple[int, int],
              rho: np.ndarray) -> np.ndarray:
    values = np.zeros(masks.size)
    for site in range(window[0], window[1] + 1):
        values += site_sz(masks, geom, site) - rho[site - 1]
    return values


def bin_distribution(values: np.ndarray, probs: np.ndarray):
    keys = np.rint(values).astype(np.int64)
    deviation = np.abs(values - keys)
    off_lattice = float(probs[deviation > TOL_LATTICE].sum())
    low = int(keys.min())
    counts = np.bincount(keys - low, weights=probs)
    points = {low + i: float(c) for i, c in enumerate(counts) if c > 0.0}
    return points, off_lattice, float(probs @ values)


def magnetisation(masks: np.ndarray, probs: np.ndarray,
                  geom: Geometry) -> np.ndarray:
    profile = np.empty(geom.n_sites)
    for site in range(1, geom.n_sites + 1):
        profile[site - 1] = float(probs @ site_sz(masks, geom, site))
    return profile


def x1_estimator(profile: np.ndarray, window: tuple[int, int]) -> float:
    """Windowed gradient centroid X1 (kink-sector-notes sec. 3)."""
    numerator = 0.0
    denominator = 0.0
    for site in range(window[0], window[1] + 1):
        gradient = profile[site - 1] - profile[site]
        numerator += (site + 0.5) * gradient
        denominator += gradient
    require(abs(denominator) > 1.0e-6, "X1 denominator vanished")
    return numerator / denominator


def window_excitation(profile: np.ndarray, geom: Geometry,
                      window: tuple[int, int]) -> float:
    """|magnon| density still inside W, wall displacement removed.

    Sums |m(x) - m_ref(x)| over W against the FINAL (transmitted) wall at
    b0-2, so the two flipped wall sites do not masquerade as excitation.
    """
    reference = np.where(np.arange(1, geom.n_sites + 1) <= geom.wall - 2,
                         0.5, -0.5)
    return float(sum(abs(profile[x - 1] - reference[x - 1])
                     for x in range(window[0], window[1] + 1)))


# ------------------------------------------------------------ propagator ---

def spectral_radius(matrix: sparse.csr_matrix) -> float:
    rows = np.asarray(abs(matrix).sum(axis=1)).ravel()
    return float(rows.max()) * 1.000001


def chebyshev_step(matrix: sparse.csr_matrix, psi: np.ndarray, time: float,
                   radius: float) -> np.ndarray:
    """exp(-i H t) psi by Chebyshev expansion on [-radius, radius]."""
    if time <= 0.0:
        return psi
    scaled = radius * time
    order = max(8, int(scaled) + 40)
    coeff = jv(np.arange(order + 1), scaled)
    keep = np.nonzero(np.abs(coeff) > 1.0e-18)[0]
    order = int(keep[-1]) if keep.size else 8
    previous = psi
    current = matrix.dot(psi) / radius
    result = coeff[0] * previous + 2.0 * (-1j) * coeff[1] * current
    for k in range(2, order + 1):
        nxt = 2.0 * (matrix.dot(current) / radius) - previous
        result = result + 2.0 * ((-1j) ** k) * coeff[k] * nxt
        previous, current = current, nxt
    return result


# ----------------------------------------------------------- the schedule ---

def ballistic_schedule(geom: Geometry, window: tuple[int, int]):
    """Group-velocity estimates: collision, product clearance, wall bounce."""
    velocity = geom.jperp * math.sin(geom.k0)
    clearance = 2.0 * geom.sigma + 1.0
    t_collide = (geom.wall - geom.y0) / velocity
    reach_t = (window[1] + clearance) - geom.wall
    reach_r = geom.wall - (window[0] - clearance)
    room_right = (geom.n_sites - 1) - geom.wall
    room_left = geom.wall - 2
    t_clear = t_collide + max(reach_t, reach_r) / velocity
    t_back = t_collide + min(2.0 * room_right - reach_t,
                             2.0 * room_left - reach_r) / velocity
    return velocity, t_collide, t_clear, t_back


def report_times(geom: Geometry, t_collide: float, t_clear: float,
                 t_back: float) -> list[float]:
    raw = [0.0, 0.5 * t_collide, t_collide, t_collide + 2.0]
    span = t_back - t_clear
    raw += [t_clear + span * f for f in (0.0, 0.2, 0.4, 0.6, 0.8, 0.95)]
    snapped = sorted({round(t / geom.dt) * geom.dt for t in raw if t >= 0.0})
    return [t for t in snapped if t <= t_back + 0.5 * geom.dt]


# ----------------------------------------------------------------- probe ---

def run_geometry(geom: Geometry, shift: float):
    problems: list[str] = []
    n_down = geom.n_sites - geom.wall
    masks = sector_masks(geom, n_down)
    matrix = hamiltonian(masks, geom)
    require(abs(matrix - matrix.T).max() < TOL_EXACT, "H is not symmetric")
    psi, prep_note = initial_state(masks, geom)
    radius = spectral_radius(matrix)

    reference = (geom.win_lo, geom.win_hi)
    windows = [(geom.win_lo + 1, geom.win_hi - 1), reference,
               (geom.win_lo - 1, geom.win_hi + 1)]
    rho = rho_vac(geom, shift)
    charges = {w: qw_values(masks, geom, w, rho) for w in windows}

    velocity, t_collide, t_clear, t_back = ballistic_schedule(geom, reference)
    travel = (t_back - t_clear) * velocity
    asymptotic = travel >= ASYMPTOTIC_TRAVEL
    gating = asymptotic and geom.dressed
    space = "full S^z sector" if geom.dwmax is None else f"<= {geom.dwmax} domain walls"
    print(f"\n=== geometry {geom.name}: N={geom.n_sites} wall bond b0={geom.wall}"
          f" (X0={geom.wall + 0.5})  {space}  dim={masks.size}  n_down={n_down}")
    print(f"    Delta={geom.delta} Jperp={geom.jperp} packet y0={geom.y0}"
          f" sigma={geom.sigma} k0={geom.k0:.4f}"
          f"  reference window W=[{reference[0]},{reference[1]}]"
          f" ({reference[1] - reference[0] + 1} sites)")
    print(f"    v_g = Jperp sin k0 = {velocity:.5f};  t_collide = {t_collide:.3f};"
          f"  products clear W at t = {t_clear:.3f};"
          f"  first boundary re-entry at t = {t_back:.3f}")
    print(f"    in-state: {prep_note}")
    reason = ("gates P3/P4" if gating
              else ("control: window too short" if not asymptotic
                    else "control: sharp-kink preparation"))
    print(f"    clean ballistic window = {travel:.2f} sites of travel"
          f"  -> role: {reason}")
    require(t_clear < t_back,
            f"{geom.name}: no clean ballistic window ({t_clear:.2f} >= {t_back:.2f})")

    times = report_times(geom, t_collide, t_clear, t_back)
    good = [t for t in times if t_clear - 1.0e-9 <= t <= t_back + 1.0e-9]
    require(bool(good), f"{geom.name}: no sampled time inside the clean window")
    latest = good[-1]
    print(f"    sampled times: {[round(t, 2) for t in times]}"
          f"   latest good time = {latest}")

    energy0 = float(np.real(np.vdot(psi, matrix.dot(psi))))
    records = {}
    clock = 0.0
    for target in times:
        psi = chebyshev_step(matrix, psi, target - clock, radius)
        clock = max(clock, target)
        norm = float(np.linalg.norm(psi))
        require(abs(norm - 1.0) < TOL_NORM,
                f"{geom.name}: norm drift {norm - 1.0:.2e} at t={target}")
        energy = float(np.real(np.vdot(psi, matrix.dot(psi))))
        require(abs(energy - energy0) < TOL_ENERGY,
                f"{geom.name}: energy drift {energy - energy0:.2e} at t={target}")
        probs = np.abs(psi) ** 2
        row = {"profile": magnetisation(masks, probs, geom)}
        for window in windows:
            row[window] = bin_distribution(charges[window], probs)
        records[target] = row
    print(f"    unitarity |norm-1| < {TOL_NORM:.0e} and |E-E0| < {TOL_ENERGY:.0e}"
          f" at every reported time (E0 = {energy0:.6f})")

    # ---- P1: t=0 sharpness and D13 calibration --------------------------
    points0, off0, _ = records[0.0][reference]
    top_point = max(points0, key=points0.get)
    top_mass = points0[top_point]
    print(f"\n    t=0 sharp point Q_W={top_point} mass={top_mass:.6f}"
          f"  off-lattice mass={off0:.3e}   full t=0 row: "
          + " ".join(f"[{k}]={v:.6f}" for k, v in sorted(points0.items())
                     if v > 1.0e-9))
    if top_mass < SHARP_MIN:
        problems.append(f"{geom.name} P1: t=0 mass {top_mass:.4f} < {SHARP_MIN}")
    if top_point != 0:
        problems.append(
            f"{geom.name} P1: D13 calibration broken, t=0 sharp point is "
            f"Q_W={top_point}, expected 0")

    # ---- per-time tables -------------------------------------------------
    x1_zero = x1_estimator(records[0.0]["profile"], reference)
    print("\n      t      <Q_W>   dx_p    X1      dx_X1  inW    straddle  "
          "offlat    p(Q_W) ...")
    for target in times:
        points, off, mean = records[target][reference]
        profile = records[target]["profile"]
        x1_now = x1_estimator(profile, reference)
        straddle = 1.0 - sum(points.get(k, 0.0) for k in PREDICTED_SUPPORT)
        table = " ".join(f"[{k}]={v:.5f}" for k, v in sorted(points.items())
                         if v > 1.0e-6)
        print(f"    {target:6.2f} {mean:8.4f} {mean / (2 * SPIN_S):7.3f}"
              f" {x1_now:7.3f} {x1_now - x1_zero:7.3f}"
              f" {window_excitation(profile, geom, reference):5.3f}"
              f" {straddle:9.5f} {off:9.2e}  {table}")
        if off > TOL_OFFMASS:
            problems.append(
                f"{geom.name} P2: off-lattice mass {off:.3e} at t={target}")

    # ---- padding scan ----------------------------------------------------
    print("\n    straddle (= 1 - p(0) - p(-2)) vs window padding:")
    print("      t     " + "".join(f"  W=[{w[0]},{w[1]}]" for w in windows))
    for target in times:
        cells = []
        for window in windows:
            points, off, _ = records[target][window]
            cells.append(
                f"{1.0 - sum(points.get(k, 0.0) for k in PREDICTED_SUPPORT):11.5f}")
            if off > TOL_OFFMASS:
                problems.append(
                    f"{geom.name} P2: off-lattice mass {off:.3e} at t={target}"
                    f" window {window}")
        print(f"    {target:6.2f} " + "".join(cells))

    # ---- P3 / P4 at the latest good time --------------------------------
    points, _, mean = records[latest][reference]
    straddle = 1.0 - sum(points.get(k, 0.0) for k in PREDICTED_SUPPORT)
    dx_p = mean / (2.0 * SPIN_S)
    dx_direct = x1_estimator(records[latest]["profile"], reference) - x1_zero
    print(f"\n    t={latest} {'GATING' if gating else 'diagnostic only'}:"
          f" straddle={straddle:.5f}"
          f" (limit {STRADDLE_MAX})  dx_p={dx_p:.5f}  dx_X1={dx_direct:.5f}"
          f"  |diff|={abs(dx_p - dx_direct):.5f} (limit {MEAN_TOL})")
    if gating:
        if straddle >= STRADDLE_MAX:
            problems.append(
                f"{geom.name} P3: mass outside {{0,-2}} is {straddle:.4f} "
                f">= {STRADDLE_MAX} at t={latest}")
        if abs(dx_p - dx_direct) >= MEAN_TOL:
            problems.append(
                f"{geom.name} P4: |dx_p - dx_X1| = {abs(dx_p - dx_direct):.4f} "
                f">= {MEAN_TOL} at t={latest}")
    summary = {t: records[t][reference][0] for t in times}
    return problems, summary, gating


def run_probe(shift: float) -> None:
    problems: list[str] = []
    summaries: dict[str, dict] = {}
    gating_seen = False
    for geom in GEOMETRIES:
        found, summary, gating = run_geometry(geom, shift)
        problems.extend(found)
        summaries[geom.name] = summary
        gating_seen = gating_seen or gating
    require(gating_seen, "no gating (asymptotic + dressed) geometry in the run")

    for first, second in TRUNCATION_PAIRS:
        left, right = summaries[first], summaries[second]
        worst = 0.0
        for target in sorted(set(left) & set(right)):
            keys = set(left[target]) | set(right[target])
            worst = max(worst, max(abs(left[target].get(k, 0.0)
                                       - right[target].get(k, 0.0))
                                   for k in keys))
        print(f"\n=== P5 truncation control {first} vs {second}: "
              f"max |delta p_nu| = {worst:.2e} (limit {TRUNCATION_TOL})")
        if worst >= TRUNCATION_TOL:
            problems.append(
                f"P5: {first} vs {second} shifts p_nu by {worst:.4f}")

    if problems:
        for problem in problems:
            print(f"    VIOLATION: {problem}", file=sys.stderr)
        fail("M-INDEX probe pre-registered criteria violated "
             f"({len(problems)} violation(s))")


# -------------------------------------------------------------- selftest ---

def selftest() -> None:
    geom = Geometry("smoke-N6", n_sites=6, wall=3, win_lo=2, win_hi=4,
                    y0=2, sigma=1.0, k0=1.0)
    rho = rho_vac(geom, 0.0)

    kink_masks = sector_masks(geom, geom.n_sites - 1 - geom.wall)
    require(kink_masks.size == 6, f"pure-kink sector dim {kink_masks.size} != 6")
    kink_q = qw_values(kink_masks, geom, (2, 4), rho)
    where = int(np.nonzero(kink_masks == ((1 << 2) | (1 << 3)))[0][0])
    require(abs(kink_q[where]) < TOL_EXACT,
            f"D13 calibration: sharp kink has Q_W={kink_q[where]}, expected 0")

    masks = sector_masks(geom, geom.n_sites - geom.wall)
    require(masks.size == 4, f"magnon sector dim {masks.size} != 4")
    values = qw_values(masks, geom, (2, 4), rho)
    expected = np.array([-2.0, -1.0, -1.0, -1.0])
    got = np.sort(values)
    require(float(np.abs(got - expected).max()) < TOL_EXACT,
            f"Q_W spectrum {got.tolist()} != {expected.tolist()}")
    require(float(np.abs(values - np.rint(values)).max()) < TOL_LATTICE,
            "Q_W spectrum is not on the integer lattice")

    two = int(locate(masks, np.array([0b0111]))[0][0])
    one = int(locate(masks, np.array([0b1011]))[0][0])
    require(abs(values[two] + 2.0) < TOL_EXACT, "expected a Q_W=-2 basis state")
    require(abs(values[one] + 1.0) < TOL_EXACT, "expected a Q_W=-1 basis state")
    psi = np.zeros(masks.size, dtype=complex)
    psi[two] = math.sqrt(0.3)
    psi[one] = math.sqrt(0.7)
    points, off, mean = bin_distribution(values, np.abs(psi) ** 2)
    require(off < TOL_EXACT, f"off-lattice mass {off} on an exact superposition")
    require(abs(points.get(-2, 0.0) - 0.3) < TOL_EXACT
            and abs(points.get(-1, 0.0) - 0.7) < TOL_EXACT,
            f"two-point distribution {points} != {{-2: 0.3, -1: 0.7}}")
    require(abs(mean + 1.3) < TOL_EXACT, f"<Q_W> = {mean}, expected -1.3")

    red_values = qw_values(masks, geom, (2, 4), rho_vac(geom, RED_RHO_SHIFT))
    _, red_off, _ = bin_distribution(red_values, np.abs(psi) ** 2)
    require(red_off > 1.0 - TOL_EXACT,
            f"integrality test is vacuous: red off-lattice mass {red_off}")

    matrix = hamiltonian(masks, geom)
    require(abs(matrix - matrix.T).max() < TOL_EXACT, "smoke H not symmetric")
    radius = spectral_radius(matrix)
    energy0 = float(np.real(np.vdot(psi, matrix.dot(psi))))
    moved = chebyshev_step(matrix, psi, 0.7, radius)
    require(abs(np.linalg.norm(moved) - 1.0) < TOL_EXACT,
            "Chebyshev propagator is not unitary")
    require(abs(float(np.real(np.vdot(moved, matrix.dot(moved)))) - energy0)
            < 1.0e-10, "energy is not conserved by the propagator")

    # domain-wall enumeration must agree with brute force on the full sector
    big = Geometry("smoke-N10", n_sites=10, wall=6, win_lo=4, win_hi=7,
                   y0=3, sigma=1.0, k0=1.0)
    exact = sector_masks(big, big.n_sites - big.wall)
    for dwmax in (3, 5):
        brute = np.sort(exact[domain_walls(exact, big.n_sites) <= dwmax])
        enumerated = domain_wall_masks(big.n_sites, big.n_sites - big.wall, dwmax)
        require(brute.size == enumerated.size
                and bool((brute == enumerated).all()),
                f"domain-wall enumeration mismatch at dwmax={dwmax}: "
                f"{brute.size} vs {enumerated.size}")

    print("SELFTEST N=6 wall=3 W=[2,4]: kink sector dim 6, magnon sector dim 4")
    print(f"  D13 calibration: sharp kink Q_W = {kink_q[where]:.1f}")
    print(f"  Q_W spectrum (magnon sector) = {got.tolist()}  (integer lattice)")
    print(f"  superposition 0.3|Q=-2> + 0.7|Q=-1> -> {points}, <Q_W> = {mean:.4f}")
    print(f"  red rho_vac shift +{RED_RHO_SHIFT}: off-lattice mass = {red_off:.6f}")
    print("  propagator unitary and energy conserving on the smoke chain")
    print("  domain-wall enumeration == brute-force filter at N=10, dwmax=3,5")
    print("PASS: memory-index probe selftest")


# ------------------------------------------------------------------ main ---

def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--red", action="store_true",
                        help="shift rho_vac by +0.3 on every site; must fail")
    parser.add_argument("--selftest", action="store_true",
                        help="6-site smoke tests of the probe machinery")
    args = parser.parse_args()

    if args.selftest:
        selftest()
        return

    if args.red:
        try:
            run_probe(RED_RHO_SHIFT)
        except SystemExit as exc:
            if exc.code:
                print(f"RED-OK: rho_vac shift +{RED_RHO_SHIFT} broke the D13 "
                      "calibration and the probe failed as required")
                raise SystemExit(1) from None
        print("FAIL: red mutation NOT detected -- checker is not red-capable",
              file=sys.stderr)
        raise SystemExit(2)

    run_probe(0.0)
    print("\nPASS: M-INDEX outcome distribution is exactly on the integer coset"
          " and concentrates on {Q_W = 0, Q_W = -2}")


if __name__ == "__main__":
    main()
