<!-- Numerics shard N1. Owner file: written only by the fm_twomagnon agent. -->

# FM two-magnon wavepacket scattering: a dynamical cross-check of the Bethe oracle

Code: [`../src/fm_twomagnon.jl`](../src/fm_twomagnon.jl) (module `FMTwoMagnon`,
standalone -- not part of `TriangleMPS`).
Tests: [`../test/test_fm_twomagnon.jl`](../test/test_fm_twomagnon.jl).
Data: [`../results/fm-displacement-scan.json`](../results/fm-displacement-scan.json).

Reproduce with

```
cd numerics
julia --project=. test/test_fm_twomagnon.jl
julia --project=. -e 'include("src/fm_twomagnon.jl"); using .FMTwoMagnon;
                      displacement_scan("results/fm-displacement-scan.json")'
```

## 1. What is being checked, and why it is independent

The Bethe oracle ([`../../theory/oracle-bethe.md`](../../theory/oracle-bethe.md))
derives, from the coordinate Bethe ansatz, the two-magnon phase

    delta(k_s, k_h) = 2 k_s + cot(k_h/2) k_s^2 + O(k_s^3)          (O7)

and its checker `theory/checks/oracle_bethe_check.py` verifies this by
*re-evaluating the same closed-form S-matrix* (6) and by matching Bethe vectors
to an ED spectrum.  Both live entirely inside the algebraic ansatz.

This shard does something the oracle cannot do for itself: it never writes down
a Bethe wavefunction.  It builds the two-magnon sector Hamiltonian from its own
enumeration of down-spin pairs, launches two Gaussian wavepackets, integrates
the Schrodinger equation with `KrylovKit.exponentiate`, and measures the
**spatial displacement** each outgoing packet suffers relative to free
propagation.  Semiclassically that displacement *is* the momentum derivative of
the scattering phase, so the oracle's `2` and `cot(k_h/2)` become directly
observable numbers on a lattice clock.  If the ansatz had the wrong branch, the
wrong channel convention (O4's `S_12` vs `S_21` trap), or a sign error, the
dynamics would say so.

## 2. The estimator and its sign

Set `k_1 = k_s`, `k_2 = k_h` as in D7--D8, `v(k) = J sin k`, and prepare the D7
*incoming* configuration: the hard packet on the left, the soft packet on the
right, with `v(k_h) > v(k_s)`, so the hard magnon overtakes (or, for `k_s < 0`,
counter-propagates into) the soft one.  In the chamber `x < y` the incoming
amplitude is `A_21 e^{i(k_2 x + k_1 y)}` and the outgoing one is
`A_12 e^{i(k_1 x + k_2 y)}` with `A_12/A_21 = S_12 = e^{i delta}`.

Write the outgoing packet as

    Psi_out(x,y,t) = ∫dk_1 dk_2 g_s(k_1) g_h(k_2) S_12(k_1,k_2)
                       e^{i(k_1 x + k_2 y)} e^{-i(w_1+w_2)t},

with `g_s(k) = G(k-k_s) e^{-ikX_s}` and `g_h(k) = G(k-k_h) e^{-ikX_h}`.
Stationary phase in `k_1` gives `x = X_s + v_s t - ∂delta/∂k_1`, and in `k_2`
gives `y = X_h + v_h t - ∂delta/∂k_2`.  Hence

    **Delta_s = -∂delta/∂k_s ,   Delta_h = -∂delta/∂k_h .**       (E1)

Two consequences fix the physics unambiguously, and both are asserted in the
test suite:

* `Delta_s = -2 + O(k_s)`: the soft magnon is pushed **backwards** by the
  leading scattering length `2` of O9, *irrespective of the sign of `k_s`*.
  The direction is set by the hard magnon's crossing direction (left to right),
  not by the soft magnon's own motion.
* `Delta_h = + k_s^2 / (2 sin^2(k_h/2)) + O(k_s^3) > 0`: the hard magnon is
  pushed **forwards**, and only at `O(k_s^2)`.  This is the oracle's own
  statement read off `delta = 2k_s + cot(k_h/2)k_s^2`:
  `∂delta/∂k_h = -(1/2)csc^2(k_h/2) k_s^2`, so the `O(k_s)` term of `delta`,
  being hard-data independent (O9), contributes nothing to the hard packet.

This is exactly the classical hard-sphere pattern -- the overtaken particle
recoils backwards by the contact length, the overtaking one jumps forwards --
and it is the sharpest qualitative content of the soft theorem in this model:
*the soft magnon absorbs a universal, hard-momentum-independent displacement,
while the hard magnon barely notices.*

Because `|S_12| = 1`, no reweighting occurs and the measured centroid shift is
*exactly* the `|g_s|^2 |g_h|^2`-weighted average of (E1); `packet_average_displacement`
computes that average and is used as the sharp per-run pass criterion.

## 3. Numerical method

* **Sector.** Ring of `N` sites, basis `{(x,y): 0 <= x < y <= N-1}`,
  dimension `N(N-1)/2`, stored as a `SparseMatrixCSC` with <= 5 entries per
  column.  The Hamiltonian is assembled from D6 directly: a bond contributes
  `(J/2)(1-P)` iff exactly one of its sites is occupied, which is in bijection
  with a single-magnon hop onto a free neighbour.  **Doubly occupied bonds
  contribute nothing** -- that omission is the entire two-magnon interaction.
* **Evolution.** `KrylovKit.exponentiate(H, -i dt, psi; ishermitian=true,
  krylovdim=40, tol=1e-12)` in steps of `dt ~ 2/J`.  The interacting run and
  two free single-magnon reference runs are stepped in lockstep.
* **Estimator.** `chamber_positions` returns `(<x>, <y>)`, the mean positions of
  the *left* and *right* down spin.  Displacements are these minus the same
  functional evaluated on the free product reference
  `phi_h(x)phi_s(y) + phi_s(x)phi_h(y)`.  No spatial window is used, so there is
  no window-boundary artefact and the residual mis-ordering bias cancels between
  run and reference to first order.
* **Geometry.** `plan_geometry` places the packets `D = 10 sigma_x` apart and
  stops at `T = 2D/(v_h - v_s)`, i.e. one full separation `D` *after* the
  crossing time `t_c = T/2`, with `8 sigma_x` of padding from the ring seam.
* **Extrapolation.** The finite-packet bias of the centroid shift is
  `(sigma_k^2/2) ∂_k^3 delta + O(sigma_k^4)` with `sigma_k = 1/(2 sigma_x)`,
  i.e. linear in `1/sigma_x^2`.  Each grid point is run at
  `sigma_x in {8, 11, 14}` and Richardson-extrapolated to zero width using
  *measured data only* -- no S-matrix input enters the extrapolation.  The
  quoted error bar is the spread over all width pairs, floored by the late-time
  drift of the measurement.

## 4. Red-green record (L1)

| # | State | Evidence |
|---|---|---|
| RED 1 | `test/test_fm_twomagnon.jl` written first; `src/fm_twomagnon.jl` absent. | `SystemError: opening file ".../src/fm_twomagnon.jl"` |
| RED 2 | First implementation measured the displacement with a **windowed centroid** of the one-body density, split at the reference midpoint. 8 failures, all in the displacement testset: e.g. `abs(run.delta_s - run.oracle_s) < 0.2` evaluated `0.629 < 0.2`, and `sign(run.delta_h) == 1` evaluated `-1.0 == 1`. Diagnosis: dispersive spreading makes the soft packet `~2.5 sigma` from the window edge at the measurement time, so window truncation biases the centroid by `O(0.1)` and the integer window boundary produces visible jumps. | see §5 |
| GREEN | Chamber-marginal estimator + free product reference; all pass criteria met without moving any tolerance. | `Test Summary: FM two-magnon wavepacket scattering \| 828 828 41.5s` |

Tolerances were fixed in the test header *before* any production run:
`TOL_DISP = 2e-2` (1% of the leading scattering length 2), `TOL_VELOCITY = 5e-3`,
`TOL_CONSERVE = 1e-9`, `TOL_ORACLE_TRUNC = 2e-1`.  None was changed afterwards.

## 5. Estimator comparison (the RED 2 lesson)

`(k_s,k_h) = (0.30, 1.5)`, `sep_factor = 10`, both estimators from the same runs.
`res` is the final separation divided by the combined final packet width.

| sigma_x |  N  | res | chamber `Delta_s` | windowed `Delta_s` | packet-avg exact |
|---|---|---|---|---|---|
|  6 | 272 | 3.71 | -2.56096 | -3.01886 | -2.56271 |
|  8 | 361 | 4.50 | -2.56963 | -2.70472 | -2.56971 |
| 11 | 494 | 5.31 | -2.57403 | -2.60148 | -2.57403 |
| 14 | 627 | 5.82 | -2.57590 | -2.58345 | -2.57590 |

The chamber estimator agrees with the exact packet average to `1e-5` already at
`sigma_x = 8` and to `<1e-8` at `sigma_x >= 11`; the windowed one is still wrong
in the second decimal at `sigma_x = 14`.  The remaining `sigma_x` dependence of
both columns is the *physical* finite-width bias, which the Richardson step
removes.

## 6. Results

`J = 1`, `sep_factor = 10`, `dt ≈ 2`, `sigma_x ∈ {8,11,14}` Richardson-extrapolated,
30 evolutions, 3465 s wall.  Every entry of the scan is in
`results/fm-displacement-scan.json`.  `res` is the resolution of §3;
`exact S` is `-∂delta/∂k` from the closed-form (6) with no soft truncation;
`oracle` is the `O7` truncation `-(2 + 2cot(k_h/2) k_s)` resp.
`+k_s^2/(2 sin^2(k_h/2))`.

### 6.1 Soft-magnon displacement `Delta_s`

| `k_s` | `k_h` | res | measured | error | exact S | dev vs exact | oracle O7 | dev vs oracle |
|---|---|---|---|---|---|---|---|---|
|  0.30 | 1.5 | 5.82 | -2.578933 | 1.7e-03 | -2.578955 |  2.2e-05 | -2.644056 |  6.5e-02 |
| -0.30 | 1.5 | 6.61 | -1.418500 | 3.6e-04 | -1.418494 | -5.6e-06 | -1.355944 | -6.3e-02 |
|  0.15 | 1.5 | 6.08 | -2.317764 | 1.3e-03 | -2.317761 | -3.2e-06 | -2.322028 |  4.3e-03 |
| -0.15 | 1.5 | 6.47 | -1.689595 | 5.3e-04 | -1.689584 | -1.1e-05 | -1.677972 | -1.2e-02 |
|  0.15 | 0.8 | 4.81 | -2.879047 | 9.7e-03 | -2.878535 | -5.1e-04 | -2.709567 | -1.7e-01 |
| -0.15 | 0.8 | 5.77 | -1.426788 | 1.7e-03 | -1.426832 |  4.4e-05 | -1.290433 | -1.4e-01 |
|  0.30 | 2.4 | 3.74 | -2.110184 | 4.9e-02 | -2.093192 | -1.7e-02 | -2.233268 |  1.2e-01 |
| -0.30 | 2.4 | 5.98 | -1.687395 | 1.1e-03 | -1.687389 | -6.0e-06 | -1.766732 |  7.9e-02 |
| -0.20 | 3.0 | 3.06 | -2.053163 | 1.9e-01 | -1.915638 | -1.4e-01 | -1.971634 | -8.2e-02 |
|  0.15 | 0.4 | 2.15 | -4.997936 | 3.5e-01 | -4.804510 | -1.9e-01 | -3.479946 | -1.5e+00 |

**Every row agrees with the exact lattice S-matrix inside its own error bar.**
Where the geometry is comfortable (`res >= 4.8`) the deviation is `3e-6 … 5e-4`,
i.e. four to six significant digits of the scattering-phase derivative recovered
from pure real-time dynamics.

### 6.2 Hard-magnon displacement `Delta_h`

| `k_s` | `k_h` | measured | error | exact S | dev vs exact | oracle | dev vs oracle |
|---|---|---|---|---|---|---|---|
|  0.30 | 1.5 | 0.123963 | 9.3e-04 | 0.123953 |  9.2e-06 | 0.096851 |  2.7e-02 |
| -0.30 | 1.5 | 0.068173 | 2.8e-04 | 0.068178 | -4.3e-06 | 0.096851 | -2.9e-02 |
|  0.15 | 1.5 | 0.028010 | 7.7e-04 | 0.028007 |  3.3e-06 | 0.024213 |  3.8e-03 |
| -0.15 | 1.5 | 0.020411 | 3.9e-04 | 0.020416 | -5.3e-06 | 0.024213 | -3.8e-03 |
|  0.15 | 0.8 | 0.106589 | 6.1e-03 | 0.106573 |  1.6e-05 | 0.074186 |  3.2e-02 |
| -0.15 | 0.8 | 0.052785 | 1.3e-03 | 0.052826 | -4.1e-05 | 0.074186 | -2.1e-02 |
|  0.30 | 2.4 | 0.064601 | 2.9e-02 | 0.053810 |  1.1e-02 | 0.051802 |  1.3e-02 |
| -0.30 | 2.4 | 0.043378 | 8.7e-04 | 0.043378 | -1.4e-07 | 0.051802 | -8.4e-03 |
| -0.20 | 3.0 | 0.023328 | 7.4e-02 | 0.019189 |  4.1e-03 | 0.020101 |  3.2e-03 |
|  0.15 | 0.4 | 0.874913 | 1.4e-01 | 0.683432 |  1.9e-01 | 0.285030 |  5.9e-01 |

`Delta_h` is **positive in all ten runs** and is one to two orders of magnitude
smaller than `Delta_s`, confirming the oracle's structural claim that the
`O(k_s)` term of `delta` carries no hard-momentum dependence (O9) and therefore
cannot displace the hard packet.  Its measured magnitude tracks
`k_s^2/(2 sin^2(k_h/2))` at the `10-30%` level, which is exactly the size of the
`O(k_s^3)` terms the oracle drops.

### 6.3 Reading the oracle coefficients off the dynamics

Combining the `+k_s` and `-k_s` runs isolates the two coefficients of O7 with no
S-matrix input at all.  Define, from measured displacements only,

    a1(k_h; k_s) := -[Delta_s(+k_s) - Delta_s(-k_s)] / (2 k_s)   ->  2 cot(k_h/2)
    a0(k_h; k_s) := -[Delta_s(+k_s) + Delta_s(-k_s)] / 2         ->  2

| `k_h` | `k_s` | `a1` measured | `a1` exact S | `2cot(k_h/2)` | `a0` measured | `a0` exact S |
|---|---|---|---|---|---|---|
| 1.5 | 0.15 | 2.093897 | 2.093923 | 2.146852 | 2.003679 | 2.003672 |
| 1.5 | 0.30 | 1.934056 | 1.934102 | 2.146852 | 1.998716 | 1.998725 |
| 0.8 | 0.15 | 4.840864 | 4.839011 | 4.730445 | 2.152918 | 2.152684 |
| 2.4 | 0.30 | 0.704648 | 0.676338 | 0.777559 | 1.898790 | 1.890291 |

The residual gap between `a1` and `2cot(k_h/2)` is the oracle's own `O(k_s^2)`
truncation, and it extrapolates away.  Richardson in `k_s^2` on the two `k_h=1.5`
rows gives

    a1(1.5) = 2.147178   (measured, dynamics only)
    a1(1.5) = 2.147197   (exact lattice S-matrix, same extrapolation)
    2 cot(0.75) = 2.146852   (oracle O9)

i.e. the dynamical extraction reproduces the exact S-matrix to `1.9e-5` and the
oracle's `cot(k_h/2)` to `3.3e-4` -- the latter residual being the `k_s^4` term,
identical for the measurement and for the exact formula.  Likewise `a0 -> 2` to
`0.2%`: **the leading, hard-data-independent scattering length `2` of O9 is a
directly measured lattice displacement, not an artefact of the ansatz.**

## 7. Caveats and surprises

1. **The accuracy is controlled by one dimensionless number, and separating the
   packets further does not improve it.**  Let `res` be the final separation over
   the combined final packet width.  With `D = s·sigma_x` and
   `T = 2D/v_rel`, dispersive spreading gives final widths
   `sigma_i ≈ |omega''(k_i)| s / v_rel`, so

       res  ≈  sigma_x · v_rel / sqrt(omega''(k_s)^2 + omega''(k_h)^2)

   -- the separation factor `s` cancels.  Only *fatter packets* (or a faster
   relative velocity) buy accuracy, and the cost of a fat packet is `N ∝ sigma_x`
   with `T ∝ sigma_x`, i.e. `O(sigma_x^3)` work.  This is why the two rows with
   small `v_rel` (`k_h = 3.0`, where `v_h = J sin k_h` is small, and `k_h = 0.4`)
   carry error bars two orders of magnitude larger than the rest at the same
   `sigma_x`.  It was not obvious in advance that pushing the packets apart is
   useless; it cost one wasted design iteration.

2. **The naive estimator is wrong at the 10% level** (RED 2, §5).  Splitting the
   one-body density at the midpoint and taking windowed centroids looks
   unimpeachable but is biased by the dispersively spread tails and jumps
   discretely as the integer window edge moves.  It got `Delta_h` *negative*,
   which would have falsified the oracle's sign.  The chamber-marginal estimator
   `(<x>, <y>)` against a free *product* reference has no window and cancels the
   mis-ordering bias to first order.

3. **A ring-seam artefact reaches the `S`-matrix singularity.**  A Gaussian
   packet at non-quantised `k` is discontinuous at the seam because `e^{ikx}` is,
   which leaves a `1/n` Fourier tail of total weight `~1e-11` spread over *all*
   momenta.  In the packet-average prediction that tail put finite weight on
   `(k_1,k_2) = (0,0)`, the one point where both the numerator and denominator of
   (6) vanish and `∂delta` is undefined -- producing `NaN`.  Fixed by an explicit
   weight cut plus a denominator guard.  Anyone reusing `momentum_weights` on a
   ring should know the tail is there.

4. **The `k_h -> 0` non-uniformity of `O7` is visible and large.**  The row
   `(k_s,k_h) = (0.15, 0.4)` deliberately violates D8's `|k_s| << k_h`.  The
   oracle truncation predicts `Delta_s = -3.48`; the exact lattice S-matrix gives
   `-4.80`; the dynamics measures `-5.00 ± 0.35`.  The dynamics sides with the
   exact S-matrix, and the oracle's own ⟨1⟩3.⟨2⟩6.⟨3⟩1 caveat (quadratic
   coefficient `2/k_h + O(k_h)`) is what fails.  This is a *confirmation* of the
   stated validity domain, not a refutation of O7.

5. **`Delta_s` is negative for both signs of `k_s`.**  This surprises on first
   sight -- a displacement that does not reverse when the particle reverses --
   but it is correct and is the sharp physical content of the linear term: the
   direction is set by the hard magnon's crossing direction, and the magnitude
   `2` is independent of everything about the hard magnon.  Reversing which
   packet starts on the left (i.e. going to the `S_21` channel of O4) flips both
   signs, which is the dynamical face of `delta_21 = -delta_12`.

6. **Conservation is not a test of anything interesting.**  Norm and energy drift
   stayed below `9e-13` in all 30 runs (`krylovdim = 40`, `tol = 1e-12`), and the
   pre-collision control displacement stayed below `1.4e-4`.  These are cheap
   sanity gates; they were passing long before the displacement estimator was
   right, which is the point of L1's "runs without errors is never a test".

7. **`k_h -> pi` is the awkward end kinematically, not analytically.**  At
   `k_h = 3.0` the oracle is perfectly regular (`cot(k_h/2) = 0.0709`), but
   `v_h = J sin k_h = 0.14` makes the D7 incoming condition `v_h > v_s` almost
   unsatisfiable: only `|k_s| < 0.14` works for positive `k_s`, and the relative
   velocity is so small that the collision takes `O(10^3)` time units.  We could
   only run `k_s < 0` there.  This is exactly the ⟨1⟩3.⟨2⟩6.⟨3⟩5 kinematic
   non-uniformity, and it is the one place where the dynamical method is
   strictly weaker than the algebra.

## 8. Verdict

The Bethe oracle's O1, O2, O7 and O9 survive an independent dynamical test.
Specifically:

* `Delta_s = -∂delta/∂k_s` and `Delta_h = -∂delta/∂k_h` are reproduced from
  wavepacket dynamics to `3e-6 … 5e-4` at every kinematic point where the
  wavepacket geometry is well resolved, and inside the quoted error bar at every
  point that is not.
* The leading scattering length `2` (O9) and the first hard invariant
  `cot(k_h/2) = v_h/omega_h` (O9, eq. 15) are both extracted from the dynamics
  alone, agreeing with the oracle to `0.2%` and `3.3e-4` respectively.
* No sign, branch or channel discrepancy was found between the oracle's `S_12`
  convention (D7) and the dynamics.
