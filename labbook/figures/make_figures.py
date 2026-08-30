#!/usr/bin/env python3
"""Publication figures for the labbook numerics shard (labbook/sections/16_numerics.tex).

Reads the committed campaign data in ``numerics/results/*.json`` and writes one
PDF per figure into ``labbook/figures/``.  Paths are resolved relative to the
repository root, so the script runs correctly from any working directory:

    python3 labbook/figures/make_figures.py

Design rules (kept deliberately uniform):
  * single-panel figures, no baked-in titles -- the captions live in LaTeX;
  * axis labels use mathtext so they typeset like the surrounding LaTeX;
  * the Okabe-Ito colourblind-safe palette, with marker shape carrying the
    same information as colour wherever a reader may print in greyscale;
  * tight bounding boxes.

The quarantined record ``lambdaD-kink-memory.FAILED-NaN.json`` is deliberately
NOT plotted: its post-processing fit emitted NaN (open bug tns-kng).
"""

from __future__ import annotations

import json
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

# --------------------------------------------------------------------------
# Paths
# --------------------------------------------------------------------------
HERE = Path(__file__).resolve().parent            # labbook/figures
REPO = HERE.parent.parent                          # repository root
RESULTS = REPO / "numerics" / "results"
OUT = HERE

# --------------------------------------------------------------------------
# Style
# --------------------------------------------------------------------------
# Okabe-Ito: colourblind-safe, greyscale-separable.
OI = {
    "black": "#000000",
    "orange": "#E69F00",
    "skyblue": "#56B4E9",
    "green": "#009E73",
    "yellow": "#F0E442",
    "blue": "#0072B2",
    "vermillion": "#D55E00",
    "purple": "#CC79A7",
}

plt.rcParams.update(
    {
        "figure.figsize": (5.2, 3.4),
        "figure.dpi": 200,
        "savefig.bbox": "tight",
        "savefig.pad_inches": 0.02,
        "font.size": 9,
        "axes.labelsize": 10,
        "axes.titlesize": 10,
        "legend.fontsize": 8,
        "legend.frameon": False,
        "xtick.labelsize": 8.5,
        "ytick.labelsize": 8.5,
        "axes.grid": True,
        "grid.alpha": 0.25,
        "grid.linewidth": 0.5,
        "axes.axisbelow": True,
        "lines.linewidth": 1.3,
        "lines.markersize": 4.5,
        "axes.prop_cycle": plt.cycler(
            color=[OI["blue"], OI["vermillion"], OI["green"], OI["orange"],
                   OI["purple"], OI["skyblue"], OI["black"]]
        ),
        "mathtext.fontset": "cm",
    }
)

WRITTEN: list[str] = []


def load(name: str):
    with open(RESULTS / name, "r", encoding="utf-8") as fh:
        return json.load(fh)


def save(fig, stem: str) -> None:
    path = OUT / f"{stem}.pdf"
    fig.savefig(path)
    plt.close(fig)
    WRITTEN.append(path.name)
    print(f"  wrote {path.relative_to(REPO)}")


# ==========================================================================
# (a) lambda-D chain phase diagnostics
# ==========================================================================
CHI_STYLE = {16: dict(alpha=0.35, lw=0.9, ls=":"),
             32: dict(alpha=0.60, lw=1.0, ls="--"),
             48: dict(alpha=1.00, lw=1.4, ls="-")}


def _sweep_series(rows, xkey, ykey, chi):
    pts = [(r[xkey], r[ykey]) for r in rows if r["chi"] == chi and r[ykey] is not None]
    pts.sort()
    return np.array([p[0] for p in pts]), np.array([p[1] for p in pts])


def fig_D_sweep():
    d = load("lambdaD-D-sweep.json")
    rows = d["rows"]
    Dc = d["reference_values"]["Haldane_largeD_transition_D_c_at_Delta1"]

    fig, ax = plt.subplots()
    spec = [("string_x", OI["blue"], "o", r"$\mathcal{O}^x$"),
            ("string_z", OI["green"], "s", r"$\mathcal{O}^z$"),
            ("es_split1", OI["vermillion"], "^",
             r"$(\lambda_1-\lambda_2)/\lambda_1$")]
    for key, colour, marker, label in spec:
        for chi in (16, 32, 48):
            x, y = _sweep_series(rows, "D", key, chi)
            st = CHI_STYLE[chi]
            ax.plot(x, y, color=colour, ls=st["ls"], lw=st["lw"], alpha=st["alpha"],
                    marker=marker if chi == 48 else None,
                    label=label if chi == 48 else None)

    ax.axvline(Dc, color=OI["black"], lw=0.8, ls="-.", alpha=0.7)
    ax.annotate(rf"$D_c \simeq {Dc:g}$", xy=(Dc, 0.04), xytext=(Dc + 0.05, 0.035),
                fontsize=8, color=OI["black"])
    ax.axhline(4 / 9, color=OI["black"], lw=0.7, ls=(0, (1, 3)), alpha=0.6)
    ax.annotate(r"AKLT $4/9$", xy=(0.02, 4 / 9 + 0.012), fontsize=7.5,
                color=OI["black"], alpha=0.8)

    ax.set_xlabel(r"single-ion anisotropy $D$  $(\Delta=1,\ J=1)$")
    ax.set_ylabel("string order / entanglement splitting")
    ax.set_xlim(-0.05, 2.05)
    ax.set_ylim(-0.03, 0.80)
    handles, labels = ax.get_legend_handles_labels()
    extra = plt.Line2D([], [], color=OI["black"], ls="-", lw=1.0,
                       alpha=0.5, label=r"$\chi=16,32,48$ (faint$\to$bold)")
    ax.legend(handles + [extra], labels + [extra.get_label()], loc="upper left",
              ncol=1)
    save(fig, "lambdaD-D-sweep")


def fig_delta_sweep():
    d = load("lambdaD-delta-sweep.json")
    rows = d["rows"]
    Dc = d["reference_values"]["Haldane_Neel_transition_Delta_c_at_D0"]

    fig, ax = plt.subplots()
    spec = [("string_x", OI["blue"], "o", r"$\mathcal{O}^x$"),
            ("string_z", OI["green"], "s", r"$\mathcal{O}^z$"),
            ("neel_order", OI["purple"], "D", r"$|m_{\mathrm{stag}}|$"),
            ("es_split1", OI["vermillion"], "^",
             r"$(\lambda_1-\lambda_2)/\lambda_1$")]
    for key, colour, marker, label in spec:
        for chi in (16, 32, 48):
            x, y = _sweep_series(rows, "Delta", key, chi)
            if key == "neel_order":
                y = np.abs(y)
            st = CHI_STYLE[chi]
            ax.plot(x, y, color=colour, ls=st["ls"], lw=st["lw"], alpha=st["alpha"],
                    marker=marker if chi == 48 else None,
                    label=label if chi == 48 else None)

    ax.axvline(Dc, color=OI["black"], lw=0.8, ls="-.", alpha=0.7)
    ax.annotate(rf"$\Delta_c \simeq {Dc:g}$", xy=(Dc, 0.05), xytext=(Dc + 0.05, 0.10),
                fontsize=8, color=OI["black"])

    ax.set_xlabel(r"Ising anisotropy $\Delta$  $(D=0,\ J=1)$")
    ax.set_ylabel("order parameters / entanglement splitting")
    ax.set_ylim(-0.03, 1.02)
    handles, labels = ax.get_legend_handles_labels()
    extra = plt.Line2D([], [], color=OI["black"], ls="-", lw=1.0, alpha=0.5,
                       label=r"$\chi=16,32,48$ (faint$\to$bold)")
    ax.legend(handles + [extra], labels + [extra.get_label()], loc="center right",
              ncol=1)
    save(fig, "lambdaD-delta-sweep")


def fig_phase_points():
    d = load("lambdaD-phase-points.json")
    # Highest bond dimension available per label; keep the documented order.
    order = ["Neel", "Haldane", "largeD", "AKLT"]
    pretty = {"Neel": u"Néel", "Haldane": "Haldane", "largeD": "large-$D$",
              "AKLT": "AKLT"}
    best = {}
    for r in d["rows"]:
        lab = r["label"]
        if lab not in order:
            continue
        if lab not in best or r["chi"] > best[lab]["chi"]:
            best[lab] = r

    keys = [("string_x", r"$\mathcal{O}^x$", OI["blue"]),
            ("string_z", r"$\mathcal{O}^z$", OI["green"]),
            ("neel_order", r"$|m_{\mathrm{stag}}|$", OI["purple"]),
            ("es_split1", r"$(\lambda_1-\lambda_2)/\lambda_1$", OI["vermillion"])]

    fig, ax = plt.subplots()
    n = len(keys)
    width = 0.8 / n
    xs = np.arange(len(order))
    for j, (key, label, colour) in enumerate(keys):
        vals = [abs(best[lab][key]) for lab in order]
        ax.bar(xs + (j - (n - 1) / 2) * width, vals, width=width * 0.92,
               color=colour, label=label, edgecolor="none")
    ax.set_xticks(xs)
    ax.set_xticklabels([pretty[o] for o in order])
    ax.set_ylabel("diagnostic value")
    ax.set_xlabel("reference point of the $\\lambda$--$D$ family")
    ax.set_ylim(0, 1.02)
    ax.legend(ncol=2, loc="upper right")
    ax.grid(axis="x", visible=False)
    save(fig, "lambdaD-phase-points")


# ==========================================================================
# (b) kink dispersion
# ==========================================================================
def fig_kink_dispersion():
    d = load("lambdaD-kink-dispersion.json")
    row = max(d["rows"], key=lambda r: r["chi_max"] if "chi_max" in r else r["chi"])
    k = np.array(row["k"])
    fig, ax = plt.subplots()
    ax.plot(k, row["omega_kink"], color=OI["blue"], marker="o",
            label=r"kink band $\omega(k)$")
    ax.plot(k, row["omega_kink_2nd"], color=OI["green"], marker="s", ls="--",
            label=r"second kink band")
    ax.plot(k, row["omega_trivial_sector"], color=OI["vermillion"], marker="^",
            ls=":", label=r"trivial-sector band")

    k0 = np.pi / 4
    w0 = row["omega_at_pi_over_4"]
    v0 = row["v_group_at_pi_over_4"]
    tang = np.linspace(k0 - 0.42, k0 + 0.42, 2)
    ax.plot(tang, w0 + v0 * (tang - k0), color=OI["black"], lw=1.0, ls="-",
            alpha=0.85)
    ax.plot([k0], [w0], marker="*", ms=9, color=OI["black"], ls="none")
    ax.annotate(rf"$v_g=\omega'(\pi/4)={v0:.4f}$",
                xy=(k0, w0), xytext=(-1.55, 3.02), fontsize=8,
                arrowprops=dict(arrowstyle="-", lw=0.7, color=OI["black"]))

    ax.set_xlabel(r"momentum per site $k$   (BZ $(-\pi/2,\pi/2]$)")
    ax.set_ylabel(r"excitation energy $\omega(k)$   $(J=1)$")
    ax.set_xticks([-np.pi / 2, -np.pi / 4, 0, np.pi / 4, np.pi / 2])
    ax.set_xticklabels([r"$-\pi/2$", r"$-\pi/4$", r"$0$", r"$\pi/4$", r"$\pi/2$"])
    ax.set_ylim(2.55, 5.85)
    ax.legend(loc="upper center", ncol=1)
    save(fig, "lambdaD-kink-dispersion")


# ==========================================================================
# (c) kink-memory truncation-rank convergence
# ==========================================================================
def fig_kink_memory_convergence():
    d = load("lambdaD-kink-memory-convergence.json")
    rows = sorted(d["rows"], key=lambda r: r["chi_max"])
    chi = np.array([r["chi_max"] for r in rows], dtype=float)
    coeff = np.array([r["coefficient_measured"] for r in rows])
    pred = rows[0]["coefficient_predicted_2s"]

    fig, ax = plt.subplots()
    ax.axhline(pred, color=OI["black"], ls="--", lw=1.0,
               label=rf"$2s = {pred:.6f}$")
    ax.plot(chi, coeff, color=OI["blue"], marker="o",
            label=r"measured coefficient")
    for c, y in zip(chi, coeff):
        ax.annotate(f"{y:.6f}", xy=(c, y), xytext=(0, -12),
                    textcoords="offset points", fontsize=7.5,
                    ha="center", color=OI["blue"])
    rel = 100 * abs(coeff[-1] - pred) / pred
    ax.annotate(rf"residual $ {rel:.2f}\,\%$ at $\chi_{{\max}}=64$",
                xy=(0.04, 0.72), xycoords="axes fraction", fontsize=8)

    ax.set_xlabel(r"TDVP2 truncation rank $\chi_{\max}$ in the window")
    # coefficient_measured = -nu / dx(X2), compared against 2s.
    ax.set_ylabel(r"memory coefficient  $-\nu\,/\,\delta x$")
    ax.set_xticks(chi)
    ax.set_xlim(chi[0] - 6, chi[-1] + 6)
    ax.set_ylim(1.9175, 1.9215)
    ax.legend(loc="center right")
    save(fig, "lambdaD-kink-memory-convergence")


# ==========================================================================
# (d) edge memory
# ==========================================================================
def fig_edge_memory():
    d = load("lambdaD-edge-memory.json")
    rows = {r["label"]: r for r in d["rows"]}
    hal, big = rows["Haldane"], rows["largeD"]
    L = hal["L"]

    fig, ax = plt.subplots()
    ax.plot(hal["times"], np.abs(hal["mL"]), color=OI["blue"], marker="o",
            label=rf"Haldane $(D=0)$, $|m_L(0)|={abs(hal['mL_initial']):.4f}$")
    ax.plot(big["times"], np.abs(big["mL"]), color=OI["vermillion"], marker="s",
            ls="--", label=rf"large-$D$ $(D={big['D']:g})$")

    # Honest readout window (bug tns-nkf): a bulk magnon front of speed v ~ 2.5
    # reaches the window edge at t ~ L/(2v); the diagnostic runs observe the
    # crossing at t ~ 6, so only t <~ 5 is a clean edge-memory readout.  Later
    # times, including the record's t = 20 "retention", are front-contaminated.
    t_clean = 5.0
    ax.axvspan(0, t_clean, color=OI["skyblue"], alpha=0.18, lw=0)
    ax.annotate("clean readout\n" rf"$t \lesssim {t_clean:.0f}$"
                "\n(front crosses at $t\\approx 6$)",
                xy=(t_clean / 2, 1e-4), ha="center", fontsize=7.5,
                color=OI["black"])
    ax.axhline(0.5, color=OI["black"], lw=0.7, ls=(0, (1, 3)), alpha=0.7)
    ax.annotate(r"$1/2$", xy=(0.4, 0.56), fontsize=8)

    ax.set_yscale("log")
    ax.set_ylim(3e-9, 1.2)
    ax.set_xlabel(r"time $t$ after the boundary field is switched off  $(J=1)$")
    ax.set_ylabel(r"$|m_L(t)| = |\sum_{x\leq L/2}\langle S^z_x\rangle|$")
    ax.legend(loc="lower right")
    save(fig, "lambdaD-edge-memory")


def fig_edge_profile():
    d = load("lambdaD-edge-memory.json")
    rows = {r["label"]: r for r in d["rows"]}
    fig, ax = plt.subplots()
    x = np.arange(1, rows["Haldane"]["L"] + 1)
    ax.plot(x, rows["Haldane"]["profile_initial"], color=OI["blue"], marker="o",
            ms=3, label=r"Haldane, $t=0$")
    ax.plot(x, rows["Haldane"]["profile_final"], color=OI["skyblue"], marker="o",
            ms=3, ls="--", label=r"Haldane, $t=20$")
    ax.plot(x, rows["largeD"]["profile_initial"], color=OI["vermillion"],
            marker="s", ms=3, label=r"large-$D$, $t=0$")
    ax.plot(x, rows["largeD"]["profile_final"], color=OI["orange"], marker="s",
            ms=3, ls="--", label=r"large-$D$, $t=20$")
    ax.set_xlabel(r"site $x$")
    ax.set_ylabel(r"local magnetisation $\langle S^z_x\rangle$")
    ax.legend(loc="lower center", ncol=2)
    save(fig, "lambdaD-edge-profile")


# ==========================================================================
# (e) spin-s falsifier battery
# ==========================================================================
def fig_bc_slope():
    f = load("spin1-bc-falsifier.json")
    x = load("spin1-bc-crosscheck.json")

    fig, ax = plt.subplots()
    ss = np.linspace(0.42, 2.12, 300)
    ax.plot(ss, 1.0 / ss, color=OI["black"], lw=1.0, ls="--",
            label=r"prediction $1/s$")

    kh_style = {0.8: ("o", OI["blue"]), 1.5: ("s", OI["green"]),
                2.4: ("^", OI["vermillion"])}
    for kh, (marker, colour) in kh_style.items():
        rows = [r for r in f["A_ring_summary"] if abs(r["k_h_target"] - kh) < 1e-9]
        rows.sort(key=lambda r: r["S"])
        sx = [r["S"] for r in rows]
        sy = [r["slope_extrapolated"] for r in rows]
        se = [r["error"] for r in rows]
        ax.errorbar(sx, sy, yerr=se, marker=marker, color=colour, ls="none",
                    capsize=2.5, label=rf"ring spectra, $k_h={kh:g}$")

    dyn = [r for r in f["A_dynamical_summary"] if r["window"] == "soft-window"]
    ax.errorbar([r["S"] for r in dyn], [r["slope_extrapolated"] for r in dyn],
                yerr=[r["error"] for r in dyn], marker="P", ls="none",
                color=OI["purple"], capsize=2.5, mfc="none",
                label=r"wavepacket dynamics")

    cx = x["A_dynamics"]
    ax.errorbar([r["s"] for r in cx], [r["slope_measured"] for r in cx],
                yerr=[r["slope_error"] for r in cx], marker="X", ls="none",
                color=OI["orange"], capsize=2.5, mfc="none",
                label=r"independent cross-check")

    ax.set_xlabel(r"site spin $s$")
    ax.set_ylabel(r"soft phase slope $\partial\delta/\partial k_s|_{k_s=0}$")
    ax.set_xticks([0.5, 1.0, 1.5, 2.0])
    ax.set_xticklabels([r"$1/2$", r"$1$", r"$3/2$", r"$2$"])
    ax.set_xlim(0.38, 2.15)
    ax.legend(loc="upper right", ncol=1)
    save(fig, "bc-soft-slope")


def fig_bc_memory_ratio():
    f = load("spin1-bc-falsifier.json")
    x = load("spin1-bc-crosscheck.json")

    fig, ax = plt.subplots()
    ss = np.linspace(0.42, 1.62, 300)
    ax.plot(ss, -1.0 / ss, color=OI["black"], lw=1.0, ls="--",
            label=r"prediction $-1/s$")

    clean, dirty = [], []
    for r in f["B_runs"]:
        res = r["result"]
        s = res["params"]["spin"]
        rec = (s, res["ratio_dx2_over_T"])
        (clean if res["trapped"] < 1e-2 else dirty).append(rec)

    if clean:
        cs, cy = zip(*clean)
        ax.plot(cs, cy, ls="none", marker="o", color=OI["blue"], mfc="none",
                label=r"kink memory, trapped $<10^{-2}$")
    if dirty:
        ds, dy = zip(*dirty)
        ax.plot(ds, dy, ls="none", marker="x", color=OI["vermillion"],
                label=r"kink memory, trapped $\geq 10^{-2}$")

    cross = [(r["s"], r["dx2_over_T"]) for r in x["B_runs"]]
    xs, xy = zip(*cross)
    ax.plot(xs, xy, ls="none", marker="^", color=OI["green"], mfc="none",
            label=r"independent cross-check")

    # 8 per cent pre-registered decision band around the prediction
    band = np.linspace(0.42, 1.62, 300)
    ax.fill_between(band, -1.08 / band, -0.92 / band, color=OI["skyblue"],
                    alpha=0.18, lw=0, label=r"pre-registered $8\,\%$ band")

    ax.set_xlabel(r"site spin $s$")
    ax.set_ylabel(r"memory ratio $\delta x / N_T$   (lattice sites)")
    ax.set_xticks([0.5, 1.0, 1.5])
    ax.set_xticklabels([r"$1/2$", r"$1$", r"$3/2$"])
    ax.set_xlim(0.38, 1.68)
    ax.legend(loc="lower right")
    save(fig, "bc-memory-ratio")


# ==========================================================================
# (f) ferromagnet displacement scan and the XXZ memory scan
# ==========================================================================
def _fm_panel(key_meas, key_err, key_exact, key_oracle, ylabel, stem, diag_pad):
    d = load("fm-displacement-scan.json")
    rows = d["summary"]
    ex = np.array([r[key_exact] for r in rows])
    me = np.array([r[key_meas] for r in rows])
    er = np.array([r[key_err] for r in rows])
    orc = np.array([r[key_oracle] for r in rows])
    res = np.array([r["resolution"] for r in rows])

    lo = min(ex.min(), me.min(), orc.min()) - diag_pad
    hi = max(ex.max(), me.max(), orc.max()) + diag_pad

    fig, ax = plt.subplots()
    ax.plot([lo, hi], [lo, hi], color=OI["black"], lw=0.9, ls="--",
            label=r"exact lattice $S$-matrix")
    good = res >= 4.8
    ax.errorbar(ex[good], me[good], yerr=er[good], ls="none", marker="o",
                color=OI["blue"], capsize=2.5,
                label=r"measured, resolution $\geq 4.8$")
    ax.errorbar(ex[~good], me[~good], yerr=er[~good], ls="none", marker="s",
                color=OI["vermillion"], capsize=2.5, mfc="none",
                label=r"measured, resolution $< 4.8$")
    ax.plot(ex, orc, ls="none", marker="+", color=OI["green"],
            label=r"soft (Bethe-oracle) truncation")
    ax.set_xlabel(r"exact $S$-matrix prediction")
    ax.set_ylabel(ylabel)
    ax.set_xlim(lo, hi)
    ax.set_ylim(lo, hi)
    ax.legend(loc="best")
    save(fig, stem)


def fig_fm_soft():
    _fm_panel("displacement_soft_measured", "displacement_soft_error",
              "displacement_soft_exact_S", "displacement_soft_oracle",
              r"measured soft displacement $\Delta_s$", "fm-displacement-soft",
              0.35)


def fig_fm_hard():
    _fm_panel("displacement_hard_measured", "displacement_hard_error",
              "displacement_hard_exact_S", "displacement_hard_oracle",
              r"measured hard displacement $\Delta_h$", "fm-displacement-hard",
              0.09)


def fig_xxz_memory():
    d = load("memory-scan-1.json")
    runs = [r for r in d["runs"]]

    def get(r, k):
        return r["result"][k]

    prod = [r for r in runs if get(r, "params")["dwmax"] == 3
            and get(r, "params")["N"] >= 120]
    trunc = [r for r in runs if get(r, "params")["N"] == 56]

    fig, ax = plt.subplots()
    tt = np.linspace(-0.02, 1.02, 200)
    ax.plot(tt, -2 * tt, color=OI["black"], lw=1.0, ls="--",
            label=r"$\delta x = -2T$")

    T = np.array([get(r, "transmission") for r in prod])
    ax.plot(T, [get(r, "dx1") for r in prod], ls="none", marker="o",
            color=OI["blue"], label=r"$\hat X_1$ (gradient centroid), $N\geq 120$")
    ax.plot(T, [get(r, "dx2") for r in prod], ls="none", marker="s",
            color=OI["green"], mfc="none",
            label=r"$\hat X_2$ (integrated magnetisation), $N\geq 120$")
    Tt = np.array([get(r, "transmission") for r in trunc])
    ax.plot(Tt, [get(r, "dx2") for r in trunc], ls="none", marker="^",
            color=OI["vermillion"], mfc="none",
            label=r"$\hat X_2$, truncation study $N=56$")

    ax.set_xlabel(r"transmission probability $T$")
    ax.set_ylabel(r"kink displacement $\delta x$   (lattice sites)")
    ax.set_xlim(-0.03, 1.03)
    ax.set_ylim(-2.45, 0.15)
    ax.legend(loc="lower left")
    save(fig, "xxz-memory-dx-vs-T")


def fig_xxz_threshold():
    d = load("memory-scan-1.json")
    by_label = {r["label"]: r["result"] for r in d["runs"]}

    fig, ax = plt.subplots()
    style = {2: ("o", OI["blue"]), 3: ("s", OI["vermillion"])}
    for Delta, (marker, colour) in style.items():
        ks, Rs = [], []
        for lab, res in by_label.items():
            p = res["params"]
            if lab.startswith("main-") and p["Delta"] == Delta:
                ks.append(p["k0"])
                Rs.append(res["reflection"])
        order = np.argsort(ks)
        ks = np.array(ks)[order]
        Rs = np.array(Rs)[order]
        ax.plot(ks, Rs, ls="none", marker=marker, color=colour,
                label=rf"measured $R$, $\Delta={Delta}$")
        C = float(np.mean(Rs * ks ** 2))
        kk = np.linspace(0.3, 2.0, 200)
        ax.plot(kk, C / kk ** 2, color=colour, lw=1.0, ls="--",
                label=rf"$C/k_0^2$, $C={C:.4f}$")

    ax.set_xscale("log")
    ax.set_yscale("log")
    ax.set_xlabel(r"incoming magnon momentum $k_0$")
    ax.set_ylabel(r"reflection probability $R = 1 - T$")
    ax.legend(loc="lower left")
    save(fig, "xxz-reflection-threshold")


# ==========================================================================
def main() -> None:
    print(f"repository root: {REPO}")
    print(f"reading         : {RESULTS}")
    print(f"writing         : {OUT}")
    for fn in (
        fig_D_sweep,
        fig_delta_sweep,
        fig_phase_points,
        fig_kink_dispersion,
        fig_kink_memory_convergence,
        fig_edge_memory,
        fig_edge_profile,
        fig_bc_slope,
        fig_bc_memory_ratio,
        fig_fm_soft,
        fig_fm_hard,
        fig_xxz_memory,
        fig_xxz_threshold,
    ):
        fn()
    print(f"\n{len(WRITTEN)} figures written:")
    for name in WRITTEN:
        print(f"  {name}")
    print("\nskipped: lambdaD-kink-memory.FAILED-NaN.json "
          "(quarantined; NaN post-processing fit, bug tns-kng)")


if __name__ == "__main__":
    main()
