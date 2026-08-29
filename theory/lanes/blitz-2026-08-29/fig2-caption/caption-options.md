# Fig. 2 caption replacements

The alternatives below are mutually exclusive full replacements for the
current `\caption{% ... }` block of Fig. 2.  Both keep the numeral `2` on the
spin-`1/2` contact/oracle route and make no use of D24(d) to assign its value.

## Option A — spin-`1/2` register

```tex
\caption{%
The soft magnon theorem in the spin-$\frac12$ Heisenberg ferromagnet.
(a)~The exact two-magnon phase with its linear term removed:
$\delta(k_s,k_h)-2k_s$ vanishes quadratically for hard momentum $k_h$ in a
compact subset of $(0,\pi)$. The hard leg first enters through
$(v_h/\omega_h)k_s^2$, where $\omega_h=J(1-\cos k_h)$ and
$v_h=J\sin k_h$, Eq.~\eqref{eq:soft}. The coefficient $2$ is the
spin-$\frac12$ value fixed by the exact contact equation,
Eq.~\eqref{eq:contact}. (b)~The corresponding exit displacement
$-\partial\delta/\partial k_s$ (curves, exact) passes through $-2$ sites at
$k_s=0$; circles are real-time wavepacket measurements and agree with the
exact curves. The gray curve ($k_h=0.4$) indicates the non-uniform approach
to the band edge $k_h=0$. The two-site footprint therefore refers to the
regular spin-$\frac12$ two-magnon channel at fixed hard momentum away from
the band edges. Other site spins and processes beyond two-body scattering
are not included; the latter remain Conjecture~S.}
```

This version makes the smallest repair.  Each occurrence of `2` is explicitly
the spin-`1/2` value and is tied in the caption to the exact contact equation
and Eq. `soft`; the band-edge sentence no longer suggests a uniform
`k_h -> 0` limit.

## Option B — exact universality class

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

This version states the largest presently proved class rather than calling
`2` universal without qualification.  It identifies the universal statement
as the `1/S` law on the fully polarized bilinear isotropic family's regular,
unit-charge two-magnon channel; the panel's `2` remains explicitly the
spin-`1/2` contact/oracle value.

## Source audit

- `definitions.md` D6--D8 and `theory/oracle-bethe.md` O7--O9 give the
  spin-`1/2` expansion, Wigner displacement, compact-hard domain, and
  non-uniform endpoint behavior.  In `paper/main.tex`, the derivation anchored
  by `the single contact bond imposes` and `whose unique analytic solution`
  traces the coefficient `2` to Eq. `contact` and hence Eq. `soft`.
- PROVED claim `S2-2body-S` gives
  `partial_{k_s} delta_phys|_0 = sgn(v_h-v_s)/S` precisely for the fully
  polarized bilinear isotropic spin-`S` family, on the regular unit-charge
  two-magnon channel, with fixed hard momentum away from endpoints and a
  fixed physical channel.  This is the class statement used only in Option B.
  Its checker was rerun under `python3 -O`: `spin_s_slope_green.log` records
  `dlog=I/S` and the spin-`1/2` value `2*I`; the prescribed mutation is
  detected with exit 1 in `spin_s_slope_red.log`.
- D24(d)3b and PROVED conditional claim `ML5-B` fix a factorization profile
  with the open constant `a_leg(rho)`; they fix no numerical coefficient, even
  at `rho=1/2`.  Neither option cites them as the source of `2`.

## Recommendation

Use **Option B**.  It costs a few lines but states the proved result that a
reader is most likely to infer from the word “universal”: the coefficient is
`1/S` on the specified spin family and two-body channel, not `2` across site
spins or source classes.  It also makes the plotted specialization and its
contact/oracle provenance explicit.  Option A is suitable only if caption
length forces the figure to describe the spin-`1/2` panel and nothing more.
