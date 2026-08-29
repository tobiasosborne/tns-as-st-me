# Anchored patch for Fig. 2 caption

Target: `paper/main.tex`

Apply exactly one caption replacement.  The recommended edit is Option B from
`caption-options.md`; Option A is the shorter fallback.

## Replacement span

Start at the unique exact string anchor

```tex
\caption{%
The soft magnon theorem and its verification. (a)~The exact two-magnon
```

and end after the unique exact string anchor

```tex
magnon leaves a two-site footprint, whatever magnon it scatters
off---within two-body scattering; beyond is Conjecture~S, unproved.}
```

Replace that entire inclusive span with the following recommended text:

```tex
\caption{%
The exact two-magnon soft slope and its spin dependence. The panels show the
spin-$\frac12$ Heisenberg ferromagnet. (a)~Its exact phase with the linear
term removed, $\delta(k_s,k_h)-2k_s$, vanishes quadratically for hard
momentum $k_h$ in a compact subset of $(0,\pi)$. The hard leg first enters
through $(v_h/\omega_h)k_s^2$, where
$\omega_h=J(1-\cos k_h)$ and $v_h=J\sin k_h$,
Eq.~\eqref{eq:soft}; the plotted coefficient $2$ follows from the exact
spin-$\frac12$ contact equation, Eq.~\eqref{eq:contact}. More generally, for
the fully polarized bilinear isotropic ferromagnets
$H_S=-J\sum_x(\mathbf S_x\!\cdot\!\mathbf S_{x+1}-S^2)$,
$S\in\{\frac12,1,\frac32,\ldots\}$, the regular, unit-charge two-magnon
channel has
$\partial_{k_s}\delta_{\rm phys}|_0=\mathrm{sgn}(v_h-v_s)/S$ for fixed
$0<|k_h|<\pi$, locally uniformly on compact hard subsets with fixed channel.
(b)~On the plotted half-zone the exit displacement
$-\partial\delta/\partial k_s$ (curves, exact) passes through $-1/S$ sites,
here $-2$; circles are real-time
wavepacket measurements and agree with the exact spin-$\frac12$ curves. The
gray curve ($k_h=0.4$) indicates the non-uniform approach to $k_h=0$.
Within the stated family and channel the $1/S$ law is independent of hard
momentum and $J$, but its value depends on $S$. Band edges, equal velocities,
other hard charges, and processes beyond two-body scattering are not
included; the last remain Conjecture~S.}
```

If Option A is selected instead, use the same two anchors and the full Option
A block from `caption-options.md`.  Do not combine the alternatives.

## Post-application checks

- The old phrases `universal coefficient $2$`, `the universal $-2$ survives
  it`, and `Every soft magnon` must be absent from the caption.
- Every remaining caption occurrence of `2` must sit in an explicit
  spin-`1/2` statement tied to Eq. `contact`/Eq. `soft`.
- The caption must not attribute a numerical value to D24(d), `ML5-B`, or
  `\mathfrak{a}_{\mathrm{leg}}`.
