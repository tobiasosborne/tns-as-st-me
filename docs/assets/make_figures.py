#!/usr/bin/env python3
"""make_figures.py -- README figures for tns-as-st-me, from real computed results.

Every number plotted here comes from a probe that lives in this repository.
Nothing is illustrative, smoothed, or invented.  Two data caches sit next to
this script so that a plain ``python3 docs/assets/make_figures.py`` redraws the
figures in a second; ``--recompute`` regenerates those caches from the probes
themselves and re-checks them against the committed probe output.

--------------------------------------------------------------------------
FIGURE 1  soft-slope-{light,dark}.svg      (the hero result)
--------------------------------------------------------------------------
Pre-registered falsifier P1 of the soft-index campaign.

  numbers on the page :  theory/checks/soft_index_probe_results.json
                         keys ``p1_two_s_1`` (S = 1/2) and ``p1_two_s_2`` (S = 1)
                         -> slope, predicted, relative_error, adler_residual, n
  the plotted rows    :  docs/assets/p1_phase_rows.json  (cache), produced by
                         calling ``phase_function`` and the through-origin cubic
                         least-squares fit of ``run_p1`` in
                         theory/checks/soft_index_probe.py with that function's
                         own parameters (k_hard = pi/2, k_centre = 0.25,
                         gap = 18, tail = 26, t_final = 1.7 (gap+tail)/dv,
                         x_soft = 0.55 N, sigma = 3), i.e. the identical
                         computation the probe gates on.
  regenerate          :  python3 docs/assets/make_figures.py --recompute
                         (~60 s: two dense eigendecompositions, 6216 x 6216 and
                         4656 x 4656).  The recomputed slopes are asserted equal
                         to the committed JSON to 1e-9 before anything is drawn.

  honesty notes.  The S = 1/2 run is CALIBRATION: the geometry and filter
  windows were tuned there, where the slope 2 is already PROVED (claim
  S2-2body-S, which gives 1/S for every S).  The S = 1 run reuses that frozen
  geometry untouched, so its agreement is OUT OF SAMPLE -- out of sample with
  respect to the tuning, not with respect to what the theory predicts.
  Both are single-N runs (N = 112 and N = 96); the k_s -> 0 value is a fit
  intercept, not a measured point, and the figure draws it as such.

--------------------------------------------------------------------------
FIGURE 2  memory-quantization-{light,dark}.svg
--------------------------------------------------------------------------
Pre-registered falsifier for M-INDEX (memory corner), geometry
``D-dw5-N50-dressed``: N = 50 easy-axis XXZ ferromagnet, Delta = 2, frozen
boundary spins, dressed kink + magnon packet, <= 5 domain walls, dim 76753.

  source              :  theory/checks/memory_index_probe.py, run unmodified
                         on a scratch COPY (it writes no files; stdout is the
                         result).  Its printed per-time table is parsed into
                         docs/assets/memory_probe_rows.json (cache).
  regenerate          :  python3 docs/assets/make_figures.py --recompute
                         (~90 s; the probe exits 0 = PASS)
  panel (a)           :  p(Q_W) at the latest good time t = 53.25 for the
                         gating dressed geometry and for the sharp-kink control
                         ``D-dw5-N50-sharp`` (same N, same window, non-gating:
                         it carries a 7.7% state-preparation defect).
  panel (b)           :  <Q_W> (= delta_x in sites, since 2s = 1) and the
                         independent windowed-gradient wall centroid X1.

  honesty notes.  Probabilities are read from the probe's own printout, which
  rounds to five decimals; entries that print as 0.00000 (mass < 5e-6) are not
  drawn and are declared on the page.  The off-lattice mass is the probe's
  exact 0.00e+00 at all ten sampled times in the reference window (the printed
  column), and <= 1e-11 in all three windows, which is what the probe's own
  gate checks -- that is the headline, and it is a certificate, not a fit.

--------------------------------------------------------------------------
FIGURE 3  ml4q1-disease-{light,dark}.svg
--------------------------------------------------------------------------
Pre-registered falsifier P3, the limit-order (ML4-Q1) discipline test.

  source              :  theory/checks/soft_index_probe_results.json, key ``p3``
                         -> raw_normalised, smeared, growth,
                            smeared_max_over_median
  ring sizes          :  SIZES_P3 read out of theory/checks/soft_index_probe.py
                         (12, 16, 20, 24, 28, 32), spin-1/2 two-magnon sector.

  honesty note / DELIBERATE SPEC DEVIATION.  The two series do NOT share a
  normalisation: in ``run_p3`` the raw fixed-N on-shell datum carries an extra
  1/k^2 = (N/2pi)^2 factor that the protocol-smeared datum does not.  Putting
  them on one y-axis would be a false comparison, so they are drawn as stacked
  small multiples with their own axes -- each judged against its own frozen
  gate (raw: last/first > 2.5; smeared: max/median <= 2.0).  No dual axes.

--------------------------------------------------------------------------
NOT PLOTTED, ON PURPOSE
--------------------------------------------------------------------------
The P2(b) "protocol eta-insensitivity" certificate of soft_index_probe.py is
known VOID (the deformation it applies is a code no-op; bd tns-9z4).  Its
``protocol_eta_diff = 0.0`` is therefore absent from every figure here, and P2
is quoted as P2(a)-only anywhere it is mentioned.  Project law L10.
"""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import math
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.lines import Line2D

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[1]
PROBE_SOFT = REPO / "theory" / "checks" / "soft_index_probe.py"
PROBE_SOFT_JSON = REPO / "theory" / "checks" / "soft_index_probe_results.json"
PROBE_MEM = REPO / "theory" / "checks" / "memory_index_probe.py"
CACHE_P1 = HERE / "p1_phase_rows.json"
CACHE_MEM = HERE / "memory_probe_rows.json"

MEM_GEOM = "D-dw5-N50-dressed"
MEM_CTRL = "D-dw5-N50-sharp"

# ---------------------------------------------------------------- design ---
# Fixed slot order, max three series per chart.  Status colours are reserved
# and are never used as a series colour; they always ship as swatch + label.
THEME = {
    "light": {
        "surface": "#ffffff",
        "series": ("#2a78d6", "#eb6834", "#1baf7a"),
        "ink": "#0b0b0b", "ink2": "#52514e", "muted": "#898781",
        "grid": "#e1e0d9", "axis": "#c3c2b7",
        "good": "#0ca30c", "bad": "#d03b3b",
    },
    "dark": {
        "surface": "#0d1117",
        "series": ("#3987e5", "#d95926", "#199e70"),
        "ink": "#ffffff", "ink2": "#c3c2b7", "muted": "#898781",
        "grid": "#2c2c2a", "axis": "#383835",
        "good": "#0ca30c", "bad": "#d03b3b",
    },
}

LW = 2.0        # 2px lines
MS = 8.0        # >= 8px markers


def rc(theme: dict) -> None:
    plt.rcParams.update({
        "font.family": "sans-serif",
        "font.sans-serif": ["DejaVu Sans", "Helvetica", "Arial",
                            "Liberation Sans", "sans-serif"],
        "svg.fonttype": "path",      # identical rendering off-machine
        "figure.facecolor": "none",
        "axes.facecolor": "none",
        "savefig.facecolor": "none",
        "axes.linewidth": 1.0,
        "axes.edgecolor": theme["axis"],
        "xtick.color": theme["muted"],
        "ytick.color": theme["muted"],
        "xtick.labelsize": 9,
        "ytick.labelsize": 9,
        "axes.labelsize": 10,
        "axes.labelcolor": theme["ink2"],
        "legend.frameon": False,
        "legend.fontsize": 9.5,
    })


def style_axes(ax, theme: dict, *, grid_axis: str = "y") -> None:
    """Recessive hairline grid behind the data; no top/right spines."""
    ax.set_axisbelow(True)
    ax.grid(True, axis=grid_axis, color=theme["grid"], linewidth=0.8,
            zorder=0)
    for side in ("top", "right"):
        ax.spines[side].set_visible(False)
    for side in ("left", "bottom"):
        ax.spines[side].set_color(theme["axis"])
    ax.tick_params(length=3, width=1.0, colors=theme["muted"])


def panel_title(ax, theme: dict, text: str) -> None:
    ax.set_title(text, color=theme["ink"], fontsize=11.5, weight="semibold",
                 loc="left", pad=9)


def badge(fig, x, y, colour, text, theme, *, size=9.6, weight="normal"):
    """Status swatch + label: state is never carried by colour alone."""
    fig.text(x, y, "■", color=colour, fontsize=size, va="center",
             ha="left")
    fig.text(x + 13.0 / 72.0 / fig.get_figwidth(), y, text,
             color=theme["ink"], fontsize=size, va="center", ha="left",
             weight=weight)


def num(value: float, spec: str = ".4f") -> str:
    """Format with a typographic minus, matching the axis tick labels."""
    return format(value, spec).replace("-", "−")


# ------------------------------------------------------------ provenance ---

def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_soft_json() -> dict:
    return json.loads(PROBE_SOFT_JSON.read_text())


def import_probe(path: Path):
    spec = importlib.util.spec_from_file_location(path.stem, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)          # constants + pure functions only
    return module


# ------------------------------------------------------- P1: recompute ----

def recompute_p1() -> dict:
    """Re-run the exact P1 readout of soft_index_probe.run_p1 and keep the rows.

    run_p1 throws its (k, phase) rows away and reports only the fitted slope,
    so the rows are regenerated here with that function's own parameters and
    the fitted slope is asserted equal to the committed probe output.
    """
    probe = import_probe(PROBE_SOFT)
    committed = load_soft_json()
    out = {"_provenance": {
        "source": "theory/checks/soft_index_probe.py :: phase_function + run_p1",
        "probe_sha256": sha256(PROBE_SOFT),
        "results_json_sha256": sha256(PROBE_SOFT_JSON),
        "note": "rows recomputed with run_p1's own parameters; the fitted "
                "slope is checked against soft_index_probe_results.json",
    }, "rows": {}}
    for two_s, n in ((1, 112), (2, 96)):
        s_val = two_s / 2.0
        k_hard = np.pi / 2.0
        k_centre = 0.25
        basis2 = probe.sector_basis(n, 2, two_s)
        h2, _ = probe.hamiltonian(n, 2, two_s)
        eig2 = np.linalg.eigh(h2)
        v_hard = 2.0 * probe.J * s_val * math.sin(k_hard)
        v_env = 2.0 * probe.J * s_val * math.sin(k_centre)
        dv = v_hard - v_env
        gap, tail = 18.0, 26.0                      # run_p1, non-quick
        t_final = 1.7 * (gap + tail) / dv
        x_soft = n * 0.55
        x_hard = (x_soft - gap) % n
        kk, phis, wts = probe.phase_function(
            two_s, n, k_centre, k_hard, x_soft, x_hard, t_final, eig2, basis2)
        design = np.vstack([kk, kk ** 2, kk ** 3]).T   # Adler zero built in
        sw = np.sqrt(wts / wts.max())
        coeffs = np.linalg.lstsq(design * sw[:, None], phis * sw,
                                 rcond=None)[0]
        adler = float(np.max(np.abs(design @ coeffs - phis)))
        ref = committed[f"p1_two_s_{two_s}"]
        assert abs(float(coeffs[0]) - ref["slope"]) < 1e-9, (
            f"recomputed P1 slope {coeffs[0]!r} disagrees with the committed "
            f"probe result {ref['slope']!r}")
        assert abs(adler - ref["adler_residual"]) < 1e-9
        out["rows"][str(two_s)] = {
            "two_s": two_s, "n": n, "t_final": float(t_final),
            "k": [float(x) for x in kk],
            "phase": [float(x) for x in phis],
            "weight": [float(x) for x in wts],
            "fit_coeffs": [float(c) for c in coeffs],
            "adler_residual": adler,
        }
        print(f"  P1 S={s_val}: slope {coeffs[0]:.10f} matches committed "
              f"{ref['slope']:.10f}, {len(kk)} rows")
    CACHE_P1.write_text(json.dumps(out, indent=1) + "\n")
    return out


# ------------------------------------------------- memory: recompute ------

ROW_RE = re.compile(
    r"^\s*(-?\d+\.\d+)\s+(-?\d+\.\d+)\s+(-?\d+\.\d+)\s+(-?\d+\.\d+)\s+"
    r"(-?\d+\.\d+)\s+(-?\d+\.\d+)\s+(-?\d+\.\d+)\s+(-?[\d.]+e[+-]\d+)\s+(.*)$")
POINT_RE = re.compile(r"\[(-?\d+)\]=([\d.]+)")


def parse_memory_stdout(text: str) -> dict:
    """Parse the per-time tables the M-INDEX probe prints for each geometry."""
    geoms: dict[str, dict] = {}
    name = None
    in_table = False
    for line in text.splitlines():
        if line.startswith("=== geometry "):
            head = line[len("=== geometry "):]
            name = head.split(":")[0].strip()
            geoms[name] = {"header": head.strip(), "rows": [], "meta": {}}
            in_table = False
            continue
        if name is None:
            continue
        if "<Q_W>" in line and "dx_p" in line:
            in_table = True
            continue
        if in_table:
            match = ROW_RE.match(line)
            if match is None:
                in_table = False
            else:
                t, mean, dx_p, x1, dx_x1, in_w, straddle, off, table = \
                    match.groups()
                geoms[name]["rows"].append({
                    "t": float(t), "mean_QW": float(mean),
                    "dx_p": float(dx_p), "X1": float(x1),
                    "dx_X1": float(dx_x1), "excitation_in_W": float(in_w),
                    "straddle": float(straddle), "off_lattice": float(off),
                    "p": {int(k): float(v)
                          for k, v in POINT_RE.findall(table)},
                })
                continue
        if line.strip().startswith("v_g ="):
            for key, pat in (("t_collide", r"t_collide = ([\d.]+)"),
                             ("t_clear", r"clear W at t = ([\d.]+)"),
                             ("t_back", r"re-entry at t = ([\d.]+)"),
                             ("v_g", r"v_g = Jperp sin k0 = ([\d.]+)")):
                hit = re.search(pat, line)
                if hit:
                    geoms[name]["meta"][key] = float(hit.group(1))
        if "GATING:" in line or "diagnostic only:" in line:
            geoms[name]["meta"]["gating"] = "GATING:" in line
            for key, pat in (("final_straddle", r"straddle=([\d.]+)"),
                             ("final_dx_p", r"dx_p=(-?[\d.]+)"),
                             ("final_dx_X1", r"dx_X1=(-?[\d.]+)")):
                hit = re.search(pat, line)
                if hit:
                    geoms[name]["meta"][key] = float(hit.group(1))
    return geoms


def recompute_memory() -> dict:
    """Run memory_index_probe.py unmodified, on a scratch copy, and parse it."""
    with tempfile.TemporaryDirectory() as tmp:
        copy = Path(tmp) / PROBE_MEM.name
        shutil.copy2(PROBE_MEM, copy)
        print(f"  running {PROBE_MEM.name} (read-only copy in {tmp}) ...")
        proc = subprocess.run([sys.executable, str(copy)], cwd=tmp,
                              capture_output=True, text=True)
    assert proc.returncode == 0, (
        f"memory_index_probe.py exited {proc.returncode}:\n{proc.stderr}")
    geoms = parse_memory_stdout(proc.stdout)
    for wanted in (MEM_GEOM, MEM_CTRL):
        assert wanted in geoms and geoms[wanted]["rows"], \
            f"geometry {wanted} missing from the probe output"
    payload = {"_provenance": {
        "source": "theory/checks/memory_index_probe.py (unmodified, run on a "
                  "scratch copy; the probe writes no files)",
        "probe_sha256": sha256(PROBE_MEM),
        "command": "python3 memory_index_probe.py",
        "exit_code": proc.returncode,
        "verdict": proc.stdout.strip().splitlines()[-1],
        "note": "probabilities are the probe's own printout, 5 decimals; "
                "entries printing as 0.00000 are omitted",
    }, "geometries": geoms}
    CACHE_MEM.write_text(json.dumps(payload, indent=1) + "\n")
    print(f"  {payload['_provenance']['verdict']}")
    return payload


# ------------------------------------------------------------- figure 1 ---

PANEL_L = 0.2685      # x-centre of the left panel of the 2-up layouts
PANEL_R = 0.7784      # x-centre of the right panel


def two_up(theme: dict):
    fig = plt.figure(figsize=(11.2, 5.9))
    gs = fig.add_gridspec(1, 2, left=0.062, right=0.985, top=0.735,
                          bottom=0.185, wspace=0.235)
    ax1, ax2 = fig.add_subplot(gs[0]), fig.add_subplot(gs[1])
    style_axes(ax1, theme)
    style_axes(ax2, theme)
    return fig, ax1, ax2


def header(fig, theme: dict, title: str, lines: tuple[str, ...]) -> None:
    fig.text(0.062, 0.963, title, color=theme["ink"], fontsize=16.5,
             weight="semibold", va="top")
    for y, line in zip((0.895, 0.850), lines):
        fig.text(0.062, y, line, color=theme["ink2"], fontsize=9.6, va="top")


def footnotes(fig, theme: dict, lines: tuple[str, ...], x: float = 0.062,
              y0: float = 0.058, dy: float = 0.032) -> None:
    for i, line in enumerate(lines):
        fig.text(x, y0 - i * dy, line, color=theme["muted"], fontsize=8.6,
                 ha="left", va="center")


def fig_soft_slope(theme_name: str) -> None:
    theme = THEME[theme_name]
    rc(theme)
    soft = load_soft_json()
    cache = json.loads(CACHE_P1.read_text())["rows"]
    s_half, s_one = soft["p1_two_s_1"], soft["p1_two_s_2"]

    fig, ax1, ax2 = two_up(theme)
    header(fig, theme,
           "The charge-created soft phase obeys the 1/S slope law",
           ("Pre-registered falsifier P1, theory/checks/soft_index_probe.py "
            "— windowed on-shell phase readout, exact diagonalisation of the "
            "two-magnon sector.",
            "The geometry and filters were tuned on S = 1/2 alone, where the "
            "slope 2 is already proved (claim S2-2body-S); the S = 1 run "
            "reuses them untouched."))
    badge(fig, 0.062, 0.800, theme["good"],
          "P1 gate PASS — both slopes inside the frozen 5% tolerance, with a "
          "common sign", theme, weight="semibold")

    labels = {1: "S = 1/2   (calibration, N = 112)",
              2: "S = 1   (out of sample, N = 96)"}
    handles = []
    for slot, two_s in enumerate((1, 2)):
        colour = theme["series"][slot]
        row = cache[str(two_s)]
        k = np.asarray(row["k"])
        phase = np.asarray(row["phase"])
        c1, c2, c3 = row["fit_coeffs"]
        grid = np.linspace(0.0, k.max() * 1.045, 300)

        # (a) the measurement itself
        ax1.plot(grid, c1 * grid + c2 * grid ** 2 + c3 * grid ** 3,
                 color=colour, linewidth=LW, zorder=3)
        ax1.plot(k, phase, marker="o", markersize=MS, linestyle="none",
                 color=colour, markeredgecolor=theme["surface"],
                 markeredgewidth=1.6, zorder=4)

        # (b) the slope law: delta/k -> 1/S as k -> 0
        ax2.plot(grid, c1 + c2 * grid + c3 * grid ** 2, color=colour,
                 linewidth=LW, zorder=3)
        ax2.plot(k, phase / k, marker="o", markersize=MS, linestyle="none",
                 color=colour, markeredgecolor=theme["surface"],
                 markeredgewidth=1.6, zorder=4)
        ax2.plot([0.0], [c1], marker="D", markersize=MS + 1.5,
                 linestyle="none", color=theme["surface"],
                 markeredgecolor=colour, markeredgewidth=2.2, zorder=5)
        handles.append(Line2D([], [], color=colour, linewidth=LW, marker="o",
                              markersize=MS - 1, label=labels[two_s]))

    # ---- panel (a)
    panel_title(ax1, theme, "a   Measured scattering phase δ(kₛ)")
    ax1.set_xlabel("soft momentum  kₛ")
    ax1.set_ylabel("phase  δ   (rad)")
    ax1.set_xlim(-0.004, 0.432)
    ax1.set_ylim(0.0, 1.04)
    ax1.legend(handles=handles, loc="upper left", labelcolor=theme["ink"],
               handletextpad=0.7, borderaxespad=0.7)
    ax1.text(0.245, 0.725, "S = 1/2", color=theme["ink"], fontsize=9.6,
             ha="left", va="center")
    ax1.text(0.258, 0.250, "S = 1", color=theme["ink"], fontsize=9.6,
             ha="left", va="center")

    # ---- panel (b)
    panel_title(ax2, theme, "b   Local slope δ(kₛ)/kₛ extrapolates to 1/S")
    ax2.set_xlabel("soft momentum  kₛ")
    ax2.set_ylabel("δ(kₛ) / kₛ")
    ax2.set_xlim(-0.022, 0.442)
    ax2.set_ylim(0.86, 2.62)
    ax2.set_xticks([0.0, 0.1, 0.2, 0.3, 0.4])
    ax2.set_yticks([1.0, 1.5, 2.0, 2.5])
    for level in (2.0, 1.0):
        ax2.plot([-0.015, 0.075], [level, level], color=theme["axis"],
                 linewidth=1.2, linestyle=(0, (5, 4)), zorder=1)
        ax2.text(0.087, level, f"predicted  1/S = {level:.0f}", ha="left",
                 va="center", color=theme["ink2"], fontsize=9.2)
    ax2.annotate(f"{s_half['slope']:.4f} at kₛ → 0\n"
                 f"{100 * s_half['relative_error']:.2f}% below 2  "
                 f"(calibration)",
                 xy=(0.006, s_half["slope"] - 0.01), xytext=(0.202, 1.800),
                 color=theme["ink"], fontsize=9.4, ha="left", va="center",
                 linespacing=1.55,
                 arrowprops=dict(arrowstyle="-", color=theme["axis"],
                                 linewidth=1.0, shrinkA=6, shrinkB=6))
    ax2.annotate(f"{s_one['slope']:.4f} at kₛ → 0\n"
                 f"{100 * s_one['relative_error']:.1f}% above 1  "
                 f"(out of sample)",
                 xy=(0.006, s_one["slope"] + 0.01), xytext=(0.214, 1.098),
                 color=theme["ink"], fontsize=9.4, ha="left", va="center",
                 linespacing=1.55,
                 arrowprops=dict(arrowstyle="-", color=theme["axis"],
                                 linewidth=1.0, shrinkA=6, shrinkB=6))
    footnotes(fig, theme, (
        "a: through-origin cubic fit — the Adler zero is imposed, not "
        f"fitted; worst phase residual {s_half['adler_residual']:.4f} rad at "
        f"S = 1/2 and {s_one['adler_residual']:.4f} rad at S = 1.",
        "b: the diamonds are kₛ → 0 fit intercepts, not measured points — "
        "the smallest momentum either ring resolves is 2π/N."))

    save(fig, f"soft-slope-{theme_name}.svg")


# ------------------------------------------------------------- figure 2 ---

def fig_memory(theme_name: str) -> None:
    theme = THEME[theme_name]
    rc(theme)
    cache = json.loads(CACHE_MEM.read_text())["geometries"]
    dressed = cache[MEM_GEOM]
    sharp = cache[MEM_CTRL]
    rows = dressed["rows"]
    last = rows[-1]
    meta = dressed["meta"]

    fig, ax1, ax2 = two_up(theme)
    header(fig, theme,
           "Memory outcomes are exactly integer, and the wall lands two "
           "sites back",
           ("Pre-registered falsifier for M-INDEX, "
            "theory/checks/memory_index_probe.py, geometry D-dw5-N50-dressed "
            "— easy-axis XXZ ferromagnet, Δ = 2, N = 50,",
            "frozen boundary spins, dressed kink struck by a magnon packet, "
            "≤ 5 domain walls (dim 76753), Chebyshev propagation."))
    badge(fig, 0.062, 0.800, theme["good"],
          "off-lattice mass = 0.00e+00 exactly at all 10 sampled times, and "
          "≤ 1e−11 in all 3 windows — the probe exits 0 = PASS",
          theme, weight="semibold")

    # ---- panel (a): the outcome distribution on the integer lattice
    panel_title(ax1, theme,
                "a   Every outcome sits on an integer   (t = 53.25)")
    floor = 8e-6
    series = ((0, dressed, "dressed kink   (gating)"),
              (1, sharp, "sharp-kink control   (non-gating)"))
    handles = []
    for slot, geom, label in series:
        colour = theme["series"][slot]
        points = {int(q): p for q, p in geom["rows"][-1]["p"].items()
                  if p > 0.0}
        offset = -0.09 if slot == 0 else 0.09
        for q, p in sorted(points.items()):
            ax1.plot([q + offset, q + offset], [floor, p], color=colour,
                     linewidth=LW, solid_capstyle="butt", zorder=3)
        ax1.plot([q + offset for q in sorted(points)],
                 [points[q] for q in sorted(points)], marker="o",
                 markersize=MS, linestyle="none", color=colour,
                 markeredgecolor=theme["surface"], markeredgewidth=1.6,
                 zorder=4)
        handles.append(Line2D([], [], color=colour, linewidth=LW, marker="o",
                              markersize=MS - 1, label=label))
    ax1.set_yscale("log")
    ax1.set_ylim(floor, 9.0)
    ax1.set_xlim(-5.7, 3.7)
    ax1.set_xticks(range(-5, 4))
    ax1.set_yticks([1e-5, 1e-4, 1e-3, 1e-2, 1e-1, 1e0])
    ax1.set_xlabel("escaped wall charge  Q_W    (= δx in lattice sites, "
                   "since 2s = 1)")
    ax1.set_ylabel("outcome probability")
    ax1.grid(True, axis="x", color=theme["grid"], linewidth=0.8, zorder=0)
    ax1.legend(handles=handles, loc="upper left", labelcolor=theme["ink"],
               handletextpad=0.7, borderaxespad=0.5)
    p_trans = last["p"]["-2"]
    ax1.annotate(f"p(−2) = {p_trans:.5f}\nthe magnon went through",
                 xy=(-1.99, 0.60), xytext=(-1.62, 0.185),
                 color=theme["ink"], fontsize=9.4, ha="left", va="center",
                 linespacing=1.55,
                 arrowprops=dict(arrowstyle="-", color=theme["axis"],
                                 linewidth=1.0, shrinkA=8, shrinkB=6))

    # ---- panel (b): displacement vs time, two independent estimators
    panel_title(ax2, theme,
                "b   Two independent estimators land on δx = −2")
    times = [r["t"] for r in rows]
    ax2.axvspan(meta["t_collide"], meta["t_clear"], color=theme["grid"],
                alpha=0.55, linewidth=0, zorder=0)
    for level in (0.0, -2.0):
        ax2.axhline(level, color=theme["axis"], linewidth=1.2,
                    linestyle=(0, (5, 4)), zorder=1)
    ax2.plot(times, [r["mean_QW"] for r in rows], color=theme["series"][0],
             linewidth=LW, marker="o", markersize=MS,
             markeredgecolor=theme["surface"], markeredgewidth=1.6, zorder=4,
             label="escaped-charge law   δx = ⟨Q_W⟩/2s")
    ax2.plot(times, [r["dx_X1"] for r in rows], color=theme["series"][1],
             linewidth=LW, marker="s", markersize=MS - 0.5,
             markeredgecolor=theme["surface"], markeredgewidth=1.6, zorder=3,
             label="wall centroid X₁   (independent estimator)")
    ax2.set_xlim(-2.0, 64.0)
    ax2.set_ylim(-2.78, 0.45)
    ax2.set_xlabel("time  t    (J⊥ = 1)")
    ax2.set_ylabel("wall displacement  δx   (lattice sites)")
    ax2.set_yticks([0.0, -0.5, -1.0, -1.5, -2.0])
    ax2.legend(loc="lower left", labelcolor=theme["ink"], handletextpad=0.7,
               borderaxespad=0.6)
    ax2.text((meta["t_collide"] + meta["t_clear"]) / 2, 0.32,
             "collision", ha="center", va="center", color=theme["muted"],
             fontsize=9.0)
    ax2.text(62.5, 0.13, "reflection outcome  0", ha="right", va="center",
             color=theme["ink2"], fontsize=9.0)
    ax2.text(62.5, -2.15, "transmission outcome  −2", ha="right",
             va="center", color=theme["ink2"], fontsize=9.0)
    ax2.text(28.0, -1.30,
             f"at t = 53.25:  δx = {num(last['mean_QW'])} and "
             f"{num(last['dx_X1'], '.3f')}\n"
             f"|difference| = "
             f"{abs(meta['final_dx_p'] - meta['final_dx_X1']):.3f} sites "
             f"(gate 0.1)",
             color=theme["ink"], fontsize=9.4, ha="left", va="center",
             linespacing=1.55)
    footnotes(fig, theme, (
        "a: probabilities as the probe prints them, to five decimals; entries "
        "below 1e−5 are not resolved and are not drawn; the control carries "
        "a 7.7% preparation defect.",
        "b: mass outside the two-point support {0, −2} is "
        f"{last['straddle']:.5f} at t = 53.25 (gate < 0.05); the window is "
        "clean from t = 24.2 until the boundary re-entry at t = 54.8."))

    save(fig, f"memory-quantization-{theme_name}.svg")


# ------------------------------------------------------------- figure 3 ---

def fig_ml4q1(theme_name: str) -> None:
    theme = THEME[theme_name]
    rc(theme)
    soft = load_soft_json()
    p3 = soft["p3"]
    sizes = list(import_probe(PROBE_SOFT).SIZES_P3)
    raw = p3["raw_normalised"]
    smeared = p3["smeared"]
    assert len(sizes) == len(raw) == len(smeared)
    median = float(np.median(smeared))

    fig = plt.figure(figsize=(8.8, 6.9))
    gs = fig.add_gridspec(2, 1, left=0.115, right=0.978, top=0.720,
                          bottom=0.135, hspace=0.36)
    ax1, ax2 = fig.add_subplot(gs[0]), fig.add_subplot(gs[1])
    style_axes(ax1, theme)
    style_axes(ax2, theme)

    fig.text(0.115, 0.967, "The order of limits is the whole story",
             color=theme["ink"], fontsize=16.5, weight="semibold", va="top")
    for y, line in ((0.903, "Pre-registered falsifier P3, "
                            "theory/checks/soft_index_probe.py — spin-1/2 "
                            "two-magnon sector, exact ED."),
                    (0.865, "The raw fixed-N on-shell datum at k = 2π/N runs "
                            "away; the protocol-smeared datum does not.")):
        fig.text(0.115, y, line, color=theme["ink2"], fontsize=9.6, va="top")
    fig.text(0.115, 0.827,
             "Separate axes on purpose: the two data carry different "
             "normalisations, so one shared scale would mislead.",
             color=theme["muted"], fontsize=8.8, va="top")
    badge(fig, 0.115, 0.787, theme["good"],
          "P3 gate PASS — the disease is visible and the smeared datum stays "
          "bounded", theme, weight="semibold")

    # ---- top: the disease
    panel_title(ax1, theme, "raw on-shell datum  k = 2π/N  —  diverges")
    ax1.plot(sizes, raw, color=theme["series"][0], linewidth=LW, marker="o",
             markersize=MS, markeredgecolor=theme["surface"],
             markeredgewidth=1.6, zorder=4)
    ax1.set_xlim(10.2, 34.0)
    ax1.set_ylim(0.0, 1.26)
    ax1.set_xticks(sizes)
    ax1.set_ylabel("amplitude / (√(N−2) k²)")
    ax1.text(32.0, 1.165, f"{raw[-1] / raw[0]:.1f}× its N = 12 value",
             color=theme["ink"], fontsize=9.6, ha="right", va="center")
    ax1.annotate("■", xy=(0.030, 0.885), xycoords="axes fraction",
                 color=theme["bad"], fontsize=9.6, va="center", ha="left")
    ax1.annotate("the ML4-Q1 disease: this sequence has no limit",
                 xy=(0.030, 0.885), xycoords="axes fraction",
                 xytext=(13, 0), textcoords="offset points",
                 color=theme["ink"], fontsize=9.6, va="center", ha="left",
                 weight="semibold")
    ax1.annotate("the gate wanted growth > 2.5, so that the probe can see it",
                 xy=(0.030, 0.775), xycoords="axes fraction",
                 xytext=(13, 0), textcoords="offset points",
                 color=theme["ink2"], fontsize=9.0, va="center", ha="left")

    # ---- bottom: the cure
    panel_title(ax2, theme,
                "protocol-smeared datum, fixed window  —  bounded")
    ax2.axhspan(0.0, 2.0 * median, color=theme["grid"], alpha=0.45,
                linewidth=0, zorder=0)
    for level in (median, 2.0 * median):
        ax2.axhline(level, color=theme["axis"], linewidth=1.2,
                    linestyle=(0, (5, 4)), zorder=1)
    ax2.plot(sizes, smeared, color=theme["series"][1], linewidth=LW,
             marker="s", markersize=MS - 0.5,
             markeredgecolor=theme["surface"], markeredgewidth=1.6, zorder=4)
    ax2.set_xlim(10.2, 34.0)
    ax2.set_ylim(0.0, 0.138)
    ax2.set_xticks(sizes)
    ax2.set_xlabel("ring size  N")
    ax2.set_ylabel("amplitude / √(N−2)")
    ax2.text(33.6, median + 0.004, "median", ha="right", va="bottom",
             color=theme["ink2"], fontsize=9.0)
    ax2.text(33.6, 2.0 * median - 0.004, "gate ceiling  2 × median",
             ha="right", va="top", color=theme["ink2"], fontsize=9.0)
    ax2.annotate(f"max / median = {p3['smeared_max_over_median']:.2f}",
                 xy=(16.2, smeared[1] * 1.02), xytext=(21.4, 0.098),
                 color=theme["ink"], fontsize=9.6, ha="left", va="center",
                 arrowprops=dict(arrowstyle="-", color=theme["axis"],
                                 linewidth=1.0, shrinkA=6, shrinkB=6))
    footnotes(fig, theme, (
        "N = 12 is under-resolved: the fixed-width smearing window holds only "
        "two momentum modes there, six by N = 32.",), x=0.115, y0=0.028)

    save(fig, f"ml4q1-disease-{theme_name}.svg")


# ------------------------------------------------------------------ run ---

def save(fig, name: str) -> None:
    path = HERE / name
    fig.savefig(path, format="svg", transparent=True)
    plt.close(fig)
    print(f"  wrote {path.relative_to(REPO)}")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--recompute", action="store_true",
                        help="regenerate the data caches from the repo probes "
                             "(~2.5 min) instead of reading them")
    args = parser.parse_args()

    if args.recompute:
        print("recomputing P1 phase rows from soft_index_probe.py ...")
        recompute_p1()
        print("re-running memory_index_probe.py ...")
        recompute_memory()
    for cache in (CACHE_P1, CACHE_MEM):
        if not cache.exists():
            print(f"missing data cache {cache}; run with --recompute",
                  file=sys.stderr)
            return 1

    print("drawing figures ...")
    for theme_name in ("light", "dark"):
        fig_soft_slope(theme_name)
        fig_memory(theme_name)
        fig_ml4q1(theme_name)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
