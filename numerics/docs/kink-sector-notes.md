<!-- ROLE: numerics-side definition choices for WP N2a (Corner B, magnon-through-kink
     memory). These are LOCAL choices made by the numerics agent; they are NOT
     yet reconciled with definitions.md / notation.md / claims/CLAIMS.md, which
     are owned by other agents. Reconcile later. Dated 2026-08-25. -->

# WP N2a — kink/magnon sector numerics: conventions, definitions, results

Code: `numerics/src/xxz_sector.jl` (336 loc), `xxz_dynamics.jl` (355 loc),
`memory_experiment.jl` (256 loc).
Tests: `numerics/test/test_xxz_{sector,dynamics,memory_experiment}.jl`
(+ `testutils.jl`, independent brute-force references).
Scan driver: `numerics/scripts/run_memory_scan.jl`.
Scan output: `numerics/results/memory-scan-1.json` (21 runs).

Status 2026-08-25: `julia --project=numerics -e 'using Pkg; Pkg.test()'` →
**1510 passed, 0 failed, 0 errored** (7 m 58 s wall for the whole package on a
heavily loaded machine; this shard's three test files account for ≈ 3.5 min of
that, the sibling `FMTwoMagnon` shard for the rest).

---

## 1. Hamiltonian and sign conventions (stated ONCE, used everywhere)

    H = − Σ_{x=1}^{N−1} [ (J_⊥/2)(S⁺_x S⁻_{x+1} + S⁻_x S⁺_{x+1}) + J_z S^z_x S^z_{x+1} ]
      = − J_⊥ Σ_x (S^x_x S^x_{x+1} + S^y_x S^y_{x+1}) − J_z Σ_x S^z_x S^z_{x+1},

with `J_⊥ > 0` and

    Δ := J_z / J_⊥ > 1     (easy axis z).

Both terms are ferromagnetic, so `|↑…↑⟩` and `|↓…↓⟩` are exact ground states and
the easy axis is `z`. This is the brief's `H = −J Σ_x [ (1/2)(S⁺S⁻+h.c.)·J_⊥/J +
Δ S^z S^z ]` with `J = J_⊥`. Energy unit: `J_⊥ = 1` throughout, so `J_z = Δ`.

**Boundary condition.** Sites `1` and `N` carry *frozen* classical spins (the
"fixed boundary spin" implementation of the boundary field): they contribute
their Ising bond to sites `2` and `N−1` but cannot flip. Hence:

* the hopping term acts only on bonds between two dynamical sites,
  `x = 2 … N−2`;
* the total `S^z` of the `L = N−2` dynamical sites is *exactly* conserved;
* `boundary = :kink` ⇒ `σ_1 = ↑`, `σ_N = ↓` (one-kink b.c.);
  `boundary = :up` ⇒ `σ_1 = σ_N = ↑` (ferromagnetic reference chain, used for
  the free-magnon calibration).

Freezing the ends is exactly equivalent to keeping sites `1, N` dynamical and
adding boundary fields `−(J_z/2) S^z_2 + (J_z/2) S^z_{N−1}` in the `:kink` case,
in the sector where the end spins are polarised. It is preferred here because
it makes the `S^z` conservation of the *dynamical* Hilbert space exact by
construction rather than only energetically.

**Magnon dispersion** (all-up chain, this convention):

    ω(k) = J_z − J_⊥ cos k,        v_g(k) = dω/dk = J_⊥ sin k.

Gapped for `Δ > 1`, gap `J_⊥(Δ−1)` at `k = 0`. `v_g > 0` for `k ∈ (0,π)`, so an
`e^{i k x}` packet moves to the **right**. Verified against the exact open-chain
eigenvalues `ω_m = J_z − J_⊥ cos(π m/(L+1))` to `1e−10`.

---

## 2. Sector structure — an important correction to the brief's framing

The brief's WP text says the one-kink sector "is spanned by N−1-ish kink-position
states". **That is only true in the Ising limit.** With `S^z` exactly conserved
and the kink boundary condition, the correct statement is:

* A single-domain-wall configuration `↑^a ↓^{L−a}` has `n_down = L − a`.
  Different kink positions therefore live in **different `S^z` sectors**.
* Consequently each `S^z` sector (fixed `n_down = n`) contains **exactly one**
  1-domain-wall configuration, namely the sharp kink at
  `X = L − n + 3/2` (physical bond coordinate, see §3).
  This is `kink_position_of_sector`. The sharp-kink position is *rigidly tied*
  to the sector label.
* The exact ground state of each sector is the (SU_q(2)) dressed kink — a
  superposition dominated by that sharp kink; the overlap → 1 as `Δ → ∞`
  (tested: `|⟨sharp|GS⟩|² > 1 − 3/Δ²`), and its energy → `E_FM + J_z/2`.
  Neighbouring sectors' kink ground states are degenerate up to `O(J_⊥²/J_z)`
  (tested).
* The **kink + one magnon** space is the `S^z` eigenspace with `n_down = n + 1`,
  restricted to configurations with **1 or 3 domain walls**. Its dimension is
  `1 + #{3-DW configs}` = `O(N²)` (bounded above by `1 + n(L−n)`; tested against
  brute-force enumeration).

**Honest caveat (not in the brief).** The number of domain walls is *not*
conserved by `H`: the elementary XY move toggles the two bonds flanking a wall,
so `#DW` changes by `0` or `±2`. The `dwmax = 3` space is therefore a
*truncation*, not an exact sector. It is:

* controlled — states with `2k+1` walls sit `k J_z` above the one-kink energy,
  so the `5`-DW admixture is off-resonant by one magnon gap;
* Hermitian — `build_hamiltonian` returns `P H P`, so unitarity and energy
  conservation of the time evolution remain **exact** (verified to `1e−12` /
  `1e−10`);
* measurable — `truncation_leakage(basis)` returns the Frobenius norm of the
  discarded matrix elements, and `magnon_wavepacket_leakage` the weight the
  state-preparation projection removes.

The exact (untruncated) `S^z` sector is also implemented (`dwmax = nothing`) and
is what the `N ≤ 12` dense-ED comparison uses.

Measured sector dimensions (`L = N−2`, `n_down = ⌊L/2⌋ + 1`):

| `dwmax` | scaling | `N = 56` | `N = 200` |
|---|---|---|---|
| 1 | 1 | 1 | 1 |
| 3 | `≈ n(L−n) = O(N²)` | 729 | 9 802 |
| 5 | `O(N⁴)` | 123 579 | ~10⁷ (unusable) |
| full | `C(L,n)` | astronomical | astronomical |

So `dwmax = 3` is what makes `N ≈ 200` exact-diagonalisation-in-a-sector
possible at all; `dwmax = 5` is affordable only up to `N ≈ 56` and is used there
purely as the truncation-convergence control.

---

## 3. Observable definitions (Corner B)

**Coordinates.** Physical sites `x = 1…N`, frozen ends included. A kink
position `X` is the coordinate of the domain-wall **bond**: `X = x + 1/2` means
the wall sits between sites `x` and `x+1`. The sharp kink with `n` down spins
has `X = (N−2) − n + 3/2`.

**Measurement window** `W = [round(X_ref) − h, round(X_ref) + h]`, default
`h = 8`, centred on the *initial* kink. All position estimators are windowed:
a global estimator is useless here, because
`Σ_x x·(∂_x m)` telescopes to the total magnetisation, which is exactly
conserved — any unwindowed centroid gives `δx ≡ 0` identically.

Three estimators, all exact on a sharp kink:

* **X̂₁ — windowed gradient centroid** (`kink_position_centroid`)

      X̂₁ = Σ_{x∈W} (x + ½)[m(x) − m(x+1)] / Σ_{x∈W} [m(x) − m(x+1)],  m(x) = ⟨S^z_x⟩.

* **X̂₂ — windowed integrated magnetisation / half-crossing**
  (`kink_position_integrated`): the wall position of the sharp step carrying the
  same total magnetisation over the window,

      X̂₂ = Σ_{x∈W} m(x) + (x_a + x_b)/2.

  X̂₁ and X̂₂ are both *linear* in the state and both exact on sharp kinks and on
  mixtures of sharp kinks (both return the weight-averaged position), but they
  weight the window differently — uniformly vs. by the local gradient — so they
  disagree exactly when magnon density is still inside `W`. **`|X̂₁ − X̂₂|` is
  the systematic-error estimate reported with every result.**

* **X̂₃ — magnetisation zero-crossing** (`kink_position_crossing`), the point
  where `m(x)` changes sign, linearly interpolated. Deliberately *inequivalent*:
  on a two-branch mixture it is **quantised** and jumps discontinuously as the
  branch weights cross ½. Reported as a diagnostic; it must not be used
  interchangeably with X̂₁/X̂₂ at partial transmission.

**Transmission / reflection weights** (`magnon_weights`). With ↑ frozen on the
left and ↓ on the right, any *down*-spin density well to the left of the wall is
a magnon that stayed on the ↑ side, and any *up*-spin density well to the right
is a magnon that crossed to the ↓ side:

    R = Σ_{x ≤ X_ref − b} (½ − m(x)),   T = Σ_{x ≥ X_ref + b} (½ + m(x)),
    trapped = 1 − T − R,        (default buffer b = 8).

Both integrals vanish identically on a clean kink of *either* branch, so `T`
and `R` are unambiguous once `b` excludes the wall region. `trapped` measures
amplitude still bound to / dressing the wall. (`T + R + trapped = 1` is checked
to `1e−10`.)

**Memory `δx`.** Linear least-squares fit `X ≈ a + b t` on a pre-collision and a
post-collision time window, then

    δx = [a_post + b_post t_c] − [a_pre + b_pre t_c],

the asymptotic intercept difference at the collision time `t_c = standoff / v_g`.
Any ballistic drift of the kink during transit is removed by the slopes.  (In
this model the kink cannot drift ballistically at fixed `S^z` — the measured
slopes are `< 2 × 10⁻⁴` — so the fit is in practice a plateau difference, but
the slope subtraction is kept because it is what the Corner-B definition asks
for and because it makes the measurement robust to a residual dressing drift.)

The windows are chosen from the DATA: `pre` is the initial stretch and `post`
the final stretch over which `trapped < trapped_tol` (default `10⁻⁴`), i.e. over
which no magnon amplitude sits near the wall and the kink position is actually
meaningful.  A geometric fallback (`3σ` leading edge touching `W`) is used when
that criterion selects too few points.

**State-preparation recipe.** Take the exact ground state `|K_n⟩` of the
`n`-down-spin sector (dressed kink), and act with the modulated lowering
operator

    O = Σ_x e^{i k₀ x} e^{−(x−x₀)²/(4σ²)} S⁻_x ,

so that `| f |²` is a Gaussian of standard deviation `σ` in position and
`1/(2σ)` in momentum; then project onto the target basis (sector `n+1`,
`dwmax`) and normalise. `x₀` is placed `standoff` sites to the LEFT of the wall,
in the ↑ region, and `k₀ > 0` so the packet moves towards the kink. The option
`kink_state = :sharp` uses the sharp kink instead of the dressed one; at
`Δ = 2, 3` the two give δx and T agreeing to `< 1e−4` (see §5), while
`:sharp` has zero preparation leakage by construction.

---

## 4. What the numerics say (headline)

**S^z bookkeeping fixes the memory quantum.** Before the collision, the state is
"kink at `X`, one extra down spin (the magnon) in the ↑ region", so
`n_down = (L − a) + 1`. After full transmission, the magnon is an *up* bubble in
the ↓ region, so `n_down = (L − a′) − 1` with the same `n_down`, i.e.
`a′ = a − 2`:

> **A transmitted magnon displaces the kink by exactly −2 lattice sites; a
> reflected magnon displaces it by 0. Hence δx = −2·T, the memory is quantised
> and its size is carried entirely by the transmission probability.**

This is the lattice analogue of "memory = DC weight of the soft factor": on the
lattice the collective coordinate can only shift in units of two sites, and the
continuous observable is the *weight* `T`, not the displacement.

The numerics confirm this over the whole scanned range (see §5): `δx₁` tracks
`−2T` to within the estimator systematics.

**Refuted prior expectation (recorded per L10).** Before running, we predicted
that at large `Δ` the kink would be an opaque barrier (`T → 0`), the transit
proceeding only through the energetically deep merged 1-DW state. **This is
false.** The numerics give `T → 1` as `Δ → ∞`. The mechanism, read off the
domain-wall algebra: the elementary XY move toggles the two bonds flanking a
wall, so from walls `{w−2, w−1, w}` (magnon adjacent to the kink on the ↑ side)
the move pivoting on `w` sends the wall at `w−1` to `w+1`, giving `{w−2, w, w+1}`
— i.e. the kink now sits at `w−2` and the magnon bubble sits on the ↓ side.
Transmission is a **first-order, energy-conserving process inside the 3-DW
manifold**; the *merge* channel into the 1-DW state is what produces reflection
and is off-resonant by one magnon gap, hence `R = O(Δ^{-2})`. The easy-axis kink
is nearly transparent to magnons, and *more* transparent the larger `Δ` is.

This is the numerical face of the soft/Adler statement in Corner C: the magnon
decouples from the kink's internal structure and couples only to its collective
coordinate — here, literally, by shifting it two sites and doing nothing else.

**Structural subtlety worth carrying into Corner B's definitions.** Inside a
fixed `S^z` sector the kink collective coordinate is *not independent of the
magnon's internal state*. Parameterise a 3-wall configuration by its walls
`w₁ < w₂ < w₃`; the `S^z` constraint reads

    (w₂ − w₁) + (N − 1 − w₃) = n,   i.e.   w₃ = (N − 1 − n) + (w₂ − w₁),

so the kink wall `w₃` is rigidly locked to the *width* `ℓ = w₂ − w₁` of the
magnon bubble. The kink is an `S^z` reservoir: widening the bubble by one site
displaces the wall by one site. On the ferromagnetic vacuum this cannot happen
(`S^z = 1` forces `ℓ = 1`), which is exactly why the memory is a kink-sector
phenomenon. The observed `δx ≃ −2` says the outgoing bubble is dominantly
`ℓ = 1`; the residual `|δx₁ + 2T| ~ 0.05–0.2` (§5) is the combined effect of
(i) the small `ℓ > 1` admixture, (ii) magnon tails inside the measurement
window/buffer, and (iii) the extrapolation of the pre-collision fit to `t_c`.
A sharper Corner-B observable would resolve the bubble-width distribution; that
is deliberately left as an open item (§6).

---

## 5. First physics scan (`numerics/results/memory-scan-1.json`)

Produced by `numerics/scripts/run_memory_scan.jl`, 2026-08-25. All runs:
`J_⊥ = 1`, kink at the chain centre, `dwmax = 3`, `dt = 0.4`,
`standoff = 36`, dressed (`:ground`) initial kink unless stated.
`X̂` positions in physical bond coordinates; `res₁ = |δx₁ + 2T|`.

### 5.1 Momentum scan, `N = 160` (σ = 8 at k₀ = 0.4, else σ = 6)

| Δ | k₀ | dim | δx₁ | δx₂ | δx₃ | T | R | trapped | res₁ |
|---|---|---|---|---|---|---|---|---|---|
| 2 | 0.4 | 6241 | −1.5115 | −1.4255 | −1.8066 | 0.72612 | 0.26955 | 4.3e−3 | 0.059 |
| 2 | 0.8 | 6241 | −1.9018 | −1.8407 | −1.9626 | 0.93043 | 0.06929 | 2.9e−4 | 0.041 |
| 2 | 1.2 | 6241 | −1.9508 | −1.9455 | −1.9863 | 0.97333 | 0.02667 | 7.7e−7 | 0.004 |
| 2 | 1.8 | 6241 | −1.9778 | −1.9723 | −1.9933 | 0.98676 | 0.01324 | 8.4e−8 | 0.004 |
| 3 | 0.4 | 6241 | −1.8829 | −1.7439 | −1.9431 | 0.90372 | 0.09207 | 4.2e−3 | 0.075 |
| 3 | 0.8 | 6241 | −1.9965 | −1.9320 | −1.9880 | 0.97658 | 0.02316 | 2.6e−4 | 0.043 |
| 3 | 1.2 | 6241 | −1.9833 | −1.9780 | −1.9947 | 0.98960 | 0.01040 | 7.1e−7 | 0.004 |
| 3 | 1.8 | 6241 | −1.9916 | −1.9861 | −1.9968 | 0.99366 | 0.00634 | 8.4e−8 | 0.004 |

### 5.2 Δ scan at k₀ = 1.2, `N = 160`

| Δ | δx₁ | δx₂ | T | R | R·Δ² |
|---|---|---|---|---|---|
| 1.5 | −1.8960 | −1.8905 | 0.94587 | 0.05413 | 0.122 |
| 2 | −1.9508 | −1.9455 | 0.97333 | 0.02667 | 0.107 |
| 3 | −1.9833 | −1.9780 | 0.98960 | 0.01040 | 0.094 |
| 6 | −1.9995 | −1.9943 | 0.99771 | 0.00229 | 0.082 |
| 12 | −2.0030 | −1.9978 | 0.99946 | 0.00054 | 0.078 |

### 5.3 Controls

* **N-convergence** (Δ = 2, k₀ = 1.2, standoff 30): `N = 120, 160, 200` give
  `δx₁ = −1.98577`, `δx₂ = −1.93242`, `T = 0.973333` — **identical to six
  significant figures**. The observable is completely N-independent once the
  packet is asymptotically free at both ends; the residual `res₁ = 0.039` here
  vs `0.004` at standoff 36 is a *measurement-geometry* systematic, not a
  finite-size one.
* **State preparation**: `prep-sharp` (sharp initial kink, zero projection
  leakage) reproduces `main-D2.0-k1.2` (dressed kink, 7.4 % projection leakage
  at Δ = 2, 14.5 % at Δ = 1.5, 0.17 % at Δ = 12) to all printed digits. The
  dressing of the initial kink is irrelevant to δx. This matters: it means the
  7–15 % state-preparation leakage of the `dwmax = 3` projection does **not**
  contaminate the observable.
* **Ising limit** `J_⊥ = 10⁻⁸`: `T = 0`, `R = 1`, `δx₁ = δx₂ = δx₃ = 0` exactly.
* **Unitarity / energy**: across the whole scan, `max|‖ψ‖−1| ≤ 1.8×10⁻¹²` and
  `max|E−E₀| ≤ 6.1×10⁻¹⁰` (accumulated over up to ~550 Krylov steps at
  `tol = 10⁻¹⁴`; the `dwmax` projection is Hermitian, so the only error is the
  Krylov tolerance). The shard tests assert the tighter `10⁻¹²` / `10⁻¹⁰` on
  the shorter trajectories they run.
* **Truncation, `dwmax = 3` vs `5`** at `N = 56` (the largest size where the
  `dwmax = 5` space, dim 123 579, is affordable), Δ = 2, k₀ = 1.2:
  `δx₂ = −1.8675` (dw 3) vs `−1.8579` (dw 5), a **0.5 % shift**, while
  `δx₁ = −2.1341` vs `−2.3113`, an 8 % shift. Two lessons: (i) the `dwmax = 3`
  truncation is accurate at the half-percent level for the *integrated*
  estimator; (ii) **X̂₂ is the robust estimator, X̂₁ is not** — its gradient
  weighting amplifies the two-magnon admixture. Caveat: at `dwmax = 5` the
  operational `T` and `R` are no longer normalised (`T + R = 1.069`, "trapped"
  goes negative) because virtual magnon *pairs* contribute their own up/down
  density; the T/R definitions of §3 presuppose the one-magnon sector. Also note
  `N = 56` carries much larger geometric systematics than `N = 160`
  (`res₁ ≈ 0.20` vs `0.004`).

### 5.4 The two headline numbers

**(i) The memory is quantised and equals −2T.** Over the whole scan
`|δx₁ + 2T| ≤ 0.075`, and at the cleanest geometries (`trapped < 10⁻⁶`)
`|δx₁ + 2T| = 0.004`. The lattice memory formula is

    δx = −2 · T(k₀, Δ)   lattice sites,

with `−2` the exact `S^z`-bookkeeping quantum and all the physics in `T`.

**(ii) The memory has an Adler-type zero at small k₀.** The reflection
probability obeys, in the perturbative regime,

    R(k₀, Δ) ≈ C(Δ) / k₀² ,     C(2) ≈ 0.043,  C(3) ≈ 0.0148,

fitted from the k₀ scan: `R·k₀²` = 0.0431, 0.0444, 0.0384, 0.0429 at Δ = 2 and
0.0147, 0.0148, 0.0150, 0.0205 at Δ = 3 for k₀ = 0.4, 0.8, 1.2, 1.8. This is the
standard 1D low-energy threshold law `R → 1` as the group velocity
`v_g = J_⊥ sin k₀ → 0`. Hence

    T → 0  and  δx → 0  as k₀ → 0 :

**a soft magnon leaves no memory.** In the same regime `C(Δ) ∝ Δ^{−2}`
(`C·Δ²` = 0.078–0.12, drifting to ≈ 0.11 at large Δ, so
`R ≈ 0.11/(Δ k₀)²` asymptotically), i.e. the kink becomes *more* transparent
and the memory *closer to its quantum* the deeper the easy axis.

Both statements are exactly what Conjectures S and M predict qualitatively:
a universal soft factor vanishing as k → 0, and a memory equal to its DC weight.
Making the `k₀²` coefficient a *prediction* of the soft theorem — rather than
a fitted number — is the obvious next theory task.

---

## 6. Open items / reconciliation notes

1. `definitions.md` should absorb: the frozen-boundary kink chain, the
   `X = x + ½` bond convention for the kink collective coordinate, the three
   position estimators, and the operational `T`/`R` integrals.
2. The claim "δx = −2T exactly, up to `O(Δ^{-2})` dressing" is a candidate
   entry in `claims/CLAIMS.md` (status: numerically SUPPORTED at the level of
   the `dwmax = 3` truncation; a proof from `S^z` conservation plus asymptotic
   completeness of the two branches looks straightforward and should be
   written).
3. The `dwmax = 3` truncation is the only uncontrolled approximation in the
   large-`N` runs. §5 records the `dwmax = 3` vs `dwmax = 5` comparison at
   `N = 56`.
4. `X̂₃` (zero-crossing) is quantised on mixtures. If the paper wants a single
   "kink position", it must say which estimator; the honest statement is that
   the *linear* estimators measure `−2T` and the *crossing* estimator measures
   the majority branch. Of the two linear estimators, **X̂₂ is the one to
   quote** (§5.3): it is 16× less sensitive to the `dwmax` truncation.
5. The `T`/`R` integrals of §3 are normalised only in the one-magnon
   (`dwmax = 3`) space. At `dwmax = 5` virtual magnon pairs contribute their own
   up/down density and `T + R > 1`. A `dwmax`-independent definition would have
   to subtract the vacuum-dressing density; not needed for the present runs but
   required if the two-magnon sector is ever the object of study.
6. A sharper Corner-B observable resolving the outgoing bubble-width
   distribution (§4) would remove the largest remaining systematic in `δx`.
7. Package hygiene: `TriangleMPS` and the sibling shard `FMTwoMagnon`
   (`src/fm_twomagnon.jl`) both wanted the name `evolve`. This shard's version
   is therefore exported as **`krylov_evolve`**; `test/runtests.jl` auto-
   discovers `test_*.jl` so the two shards share one `Main` and any further
   export collisions will show up as errors there.
