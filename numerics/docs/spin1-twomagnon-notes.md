# spin-1 notes — the two Conjecture Bc falsifiers (bd `tns-8e9`)

Conventions and results for `src/spin1_twomagnon.jl`, `src/spin1_collision.jl`,
`src/spin1_memory.jl`, `src/spin1_memory_run.jl`, and the scan
`scripts/run_spin1_bc_falsifier.jl` → `results/spin1-bc-falsifier.json`.

Nothing in `theory/`, `claims/` or `paper/` is edited by this work package; the
numbers below are reported for the orchestrator to place in the DAG.

---

## 0. What is being decided

`theory/TRIANGLE.md` §4 records two independent `2`s:

* the soft Wigner phase-slope coefficient of the **frozen** Theorem S2-2body,
  `dδ_phys/dk_s|_0 = 2 sgn(v_h−v_s)`, which is `2` on D8;
* the memory quantum of Theorem M-quant, `1/s = 2` sites.

**Conjecture Bc** says both equal `|q_hard|/s`. Since a single magnon has
`|q_hard| = 1`, that predicts `1` and `−1` for the spin-1 chain. The falsifier
was stated in advance: *if the spin-1 phase slope is not `1`, the coincidence is
numerology and Bc must be dropped from the paper.*

---

## 1. The spin-`S` ferromagnet two-magnon problem

With `n_x := S − S^z_x` the on-site magnon number, `H = −J Σ_x (S_x·S_{x+1} − S²)`
reads, exactly,

    diagonal = 2JS Σ_x n_x − J Σ_bonds n_x n_{x+1}
    hop a→b  = −(J/2) √(n_a(2S−n_a+1)) · √((n_b+1)(2S−n_b))

so the free hop is `−JS`, the hop that creates or destroys a doubly occupied
site is `−Jg` with `g = √(S(2S−1))` (`g = 0` at `S = 1/2`: hard core), and the
adjacency energy is `−J`. One-magnon dispersion `ω(k) = 2JS(1 − cos k)`.

For `S ≥ 1` the two-magnon basis has `N(N−1)/2 + N` states: the extra `N` are the
doubly occupied sites, which are a genuine second channel, not a bookkeeping
device.

### 1.1 A wrong turn, recorded (L10)

The first attempt extended `ψ` to a **symmetric** `Ψ` on `ℤ²`, identified
`ψ_d(x) = cΨ(x,x)`, and obtained `c = g/(2S)` from the doubly occupied equation
and then

    Ψ(x,x+1) = (S − gc)[Ψ(x,x) + Ψ(x+1,x+1)] ,  gc = g²/(2S) = S − ½ ,

i.e. the **spin-independent** hard-core contact condition, hence the spin-1/2
S-matrix and slope `2` for every `S` — which would have falsified Bc.

It is wrong: `Ψ(x,y) = A z₁^x z₂^y + B z₂^x z₁^y` is *not* symmetric unless
`A = B`, so the free equation at `(x,x)` may not be collapsed using
`Ψ(x+1,x) = Ψ(x,x+1)`. The error was caught by the numerics before the algebra
was redone: the candidate vector is not an eigenvector at `S = 1`
(residual `0.93` at `N = 18`), and the ansatz-free ring extraction returned
`0.998`, not `2`.

### 1.2 The contact solution

Keep `Ψ` **unsymmetrised** (it solves the free equation everywhere on `ℤ²`),
identify `ψ = Ψ` only on the physical chamber `x < y`, and let `ψ_d(x) = ρ w^x`,
`w = z₁z₂`. Write `K = k₁+k₂`, `q = (k₁−k₂)/2`, `c = cos(K/2)`,
`P = A z₂ + B z₁`. Then `E − 4JS = −4JS·c·cos q`, and

* the doubly-occupied equation gives `ρ = g P e^{−iK/2}/(2S cos q)`;
* the adjacent-pair equation gives
  `(A e^{−iq} + B e^{iq})[(2S−1)c + cos q] = 2S c cos q (A+B)`.

Hence, with `n := 2Sc·cos q − e^{iq}[(2S−1)c + cos q]`,

    S₁₂ = A/B = n/(−n̄) ,     |S₁₂| = 1 ,   S₁₂(k₁,k₂)S₁₂(k₂,k₁) = 1 ,

and `δ = arg S₁₂ = 2 arg n − π`, so `∂δ/∂k_j = 2 Im(∂_j n / n)`. At `S = 1/2` the
`(2S−1)c` term vanishes and `S₁₂` collapses to the frozen oracle formula
`−(z₁z₂−2z₁+1)/(z₁z₂−2z₂+1)` (checked to `1e-12`).

### 1.3 The soft limit

Put `k₁ = k_s → 0`, `k₂ = k_h` fixed, `h := k_h/2`, `γ = cos h`, `σ = sin h`.
Then `q₀ = −h`, `c₀ = cos q₀ = γ`, and

    n(0)  = 2Sγ · iσ ,
    n'(0) = −σγ + i[ σ²(1−S) − Sγ² ] ,
    Im(n'/n) = σγ/(2Sγσ) = 1/(2S) .

    ⟹  dδ/dk_s|_0 = 1/S ,  all hard dependence cancelling.

`S = 1/2` gives `2` — the frozen Theorem S2-2body value — and `S = 1` gives `1`.
The cancellation of the hard velocity is the same structural feature the `s=1/2`
argument turns on; what changes with `S` is only the overall normalisation.

---

## 2. Measurements (A)

Three independent routes, all in `test_spin1_twomagnon.jl` and the scan.

| route | what it uses | what it does not use |
|---|---|---|
| exact eigenvector | `bethe_vector` residual `‖H₂ψ − Eψ‖` at Bethe--Yang momenta | — |
| ring spectra | exact momentum-block eigenvalues, `ω(k)`, `k₁+k₂ = K`, `N k_s = 2πn_s + δ` | any wavefunction ansatz, any S-matrix |
| wavepacket | Krylov evolution of a two-packet in-state, chamber-marginal displacement vs a free reference | any S-matrix |

The sector Hamiltonian itself is validated against a brute-force dense `(2S+1)^N`
ED of the ring (`N = 6, S = 1`; `N = 8, S = 1/2`), and the momentum blocks against
the full sector spectrum.

**Caveat on `bethe_vector`.** For degenerate quantum numbers `n₁ = n₂` the
Bethe--Yang fixed point lands on the singular pair and the vector is not an
eigenvector *at any `S`*, `s = 1/2` with the frozen oracle S-matrix included.
That is a property of the ansatz, not of the contact derivation; the tests use
non-degenerate quantum numbers and say so.

---

## 3. The spin-`s` memory experiment (B)

`src/spin1_memory.jl` generalises `xxz_sector.jl`/`xxz_dynamics.jl` in `s`.

**Truncation.** Domain-wall counting is a spin-1/2 notion. The invariant
replacement is the number of excitations above a pure wall,

    D(n) := Σ_x max(0, n_x − n_{x+1})    (frozen ends included),

the total upward variation of `S^z`. Monotone (pure wall) ⇒ `D = 0`; kink plus
one magnon on either side ⇒ `D = 1`; a doubly flipped site counts as two magnons.
At `s = 1/2`, `D = (domain walls − 1)/2`, so `dmax = 1 ≡ dwmax = 3` and
`dmax = 2 ≡ dwmax = 5`. The tests check that the enumerated bases agree with the
frozen spin-1/2 ones **configuration for configuration**, and that the operators
have the same spectra.

**Wall coordinate.** `X̂₂ = (Σ_{x∈W} ⟨S^z_x⟩)/(2s) + (x_a+x_b)/2`, the wall of the
sharp step carrying the same windowed magnetisation. Linear in the state, exact
on every monotone wall — sharp or with intermediate `S^z` sites, which is what a
spin-1 wall actually looks like (in the Ising limit the `+1|−1` bond costs `2J_z`
and so does `+1|0|−1`, so the wall is one or two sites wide).

**Weights.** `R = Σ_{x ≤ X−b}(s − m(x))`, `T = Σ_{x ≥ X+b}(s + m(x))`: magnon
*number*, not magnetisation, for every `s`.

**Why the law is `−1/s`.** `S^z` bookkeeping on the whole chain: an incoming
magnon on the ↑ side carries `ΔS^z = −1`, a transmitted one on the ↓ side carries
`+1`, and `R + T = 1`, so `Σ_W ⟨S^z⟩` changes by `−2T` and
`δx = −2T/(2s) = −N_T/s`. This is a *charge* statement, exactly as the refutation
of Conjecture M in `corner-b-draft.md` §10 says it must be; it is the soft phase
slope, not the memory quantum, that carries the dynamical information.

**Cost.** `dmax = 1` grows like `L²` (`dim = 78 498` at `N = 100`, `136 998` at
`N = 120` for `s = 1`); `dmax = 2` grows like `L⁴` (`4.07·10⁶` already at
`N = 60` for `s = 1`), so the truncation-convergence check is run on the longest
chain that still fits, `N = 46`. The `s = 3/2` sector grows faster still
(`nmax = 3` admits more wall shapes): `2.33·10⁵` at `N = 60`, `4.36·10⁵` at
`N = 70`; an `N = 100` attempt was OOM-killed at 24 GB, so `s = 3/2` runs at
`N = 64`.

**Reading `H_truncation_leakage` (it is NOT an error bar).** The function returns
the Frobenius norm of the matrix elements that `P H P` discards, summed over the
*whole basis*. It is extensive — it grows with the basis size and with the
number of boundary hops per configuration — and it carries no normalisation, so
it cannot be compared to 1 or read as a relative error. Measured against the
kept hopping operator:

| run | dim | `‖P H P‖_F` (hopping) | leak | leak / total |
|---|---|---|---|---|
| `s = 1`, `N = 120`, `dmax = 1` | 136 998 | 165.5 | 4016.8 | 0.9992 |
| `s = 1/2`, `N = 120`, `dmax = 1` | 3 481 | 7.6 | 50.2 | 0.9886 |

The second row is the **frozen, accepted** spin-1/2 truncation (`dmax = 1 ≡
dwmax = 3`) behind `results/memory-scan-1.json`, which agrees with the exact
`≤3`-wall reference values to 0.9–5.8%. So a leak ratio near 1 is *normal* for
this class of truncation and says nothing about accuracy: the Frobenius norm
weights every configuration equally, whereas the physical state lives on a
localized wall plus one magnon, and every discarded process creates an extra
interface costing `~J_z`. The spin-1 number is larger than the spin-1/2 one only
because the basis is 40× larger and a spin-1 wall has `n = 1` interior sites,
each of which contributes boundary hops.

What *does* bound the error is state-level and physical: the initial-state
leakage (2.5% at `s = 1`, versus 7.4% in the frozen `s = 1/2` scan — the spin-1
preparation is the cleaner of the two), exact norm/energy conservation (`P H P`
is Hermitian), `N`-convergence, the `dmax = 1` vs `dmax = 2` comparison, and
above all the `s = 1/2` control run on the *same code path with the same
truncation*, which returns `−1.998`.

**Baseline for `T` and `R`.** At `dmax = 1` the initial weights are exactly
`(T,R) = (0,1)`, so `δx/N_T` is unambiguous. At `dmax ≥ 2` the dressed kink
carries virtual pairs and starts with `T,R` slightly off `(0,1)`; the results
record therefore also carries `ratio_dx2_over_deltaT`, which subtracts the
initial weights and is identical to `ratio_dx2_over_T` whenever `dmax = 1`.

---

## 4. Results

See `results/spin1-bc-falsifier.json` for every number and every parameter.
Decision band 8%, fixed before the first run; the two hypotheses were `1` and
`−1` (Bc survives) against `2` and `−2` (Bc falsified).

### (A) soft phase slope `dδ/dk_s|_0`

Ansatz-free ring extraction, `N ∈ {60,90,120,180,240,360,480}`:

| `S` | `k_h = 0.8` | `k_h = 1.5` | `k_h = 2.4` | `1/S` |
|---|---|---|---|---|
| 1/2 | `1.9979 ± 0.0640` | `1.9985 ± 0.0149` | `2.0010 ± 0.0104` | 2 |
| **1** | `0.9972 ± 0.0241` | **`0.9985 ± 0.0044`** | `0.9995 ± 0.0234` | **1** |
| 3/2 | `0.6645 ± 0.0144` | `0.6654 ± 0.0042` | `0.6648 ± 0.0258` | 0.6667 |
| 2 | `0.4982 ± 0.0101` | `0.4989 ± 0.0037` | `0.4978 ± 0.0239` | 0.5 |

Across all 84 ring rows the extracted `δ` agrees with the analytic spin-`S`
phase to `8·10⁻¹³`.  Wavepacket dynamics (`k_h = 1.5`): `0.9921 ± 0.0022` at
`S = 1` and `2.0010 ± 0.0010` at `S = 1/2` on the soft `k_s` window, with the
measured displacement matching the analytic `∂δ/∂k_s` pointwise to `5·10⁻⁶`.
(The `k_s ∈ [0.1,0.3]` window gives `0.9358 ± 0.0112`; that 6% shortfall is
curvature of `∂δ/∂k_s`, not a discrepancy — the pointwise agreement there is
`1.6·10⁻⁵`.)

### (B) memory quantum `δx/N_T`

`s = 1`, `N = 120`, `dmax = 1`, nine `(Δ,k₀)` points; `s = 1/2` controls and an
`s = 3/2` point on the same code path.  Spin-1 values fall in `−0.919 … −0.996`
(mean `≈ −0.98`), spin-1/2 controls in `−1.958 … −1.998`, `s = 3/2` at `−0.660`
against `−0.6667`.  The single 8%-edge case is `Δ = 2, k₀ = 1.8`, which has
`trapped = 5.5·10⁻²`: amplitude still bound at the wall, i.e. the asymptotic
condition behind the law is not yet met there, and the deviation shrinks with
`Δ` exactly as that reading predicts.

**Verdict: Conjecture Bc SURVIVES both falsifiers.**

**What is and is not tested.** The runs vary `s` over `{1/2, 1, 3/2, 2}` and so
test the `1/s` factor of `|q_hard|/s` sharply.  They do **not** test the
`|q_hard|` factor: every leg in every run carries `|q| = 1`.  A hard leg of
charge 2 — the two-magnon bound state — would predict slope `2/s` and is the
obvious next falsifier.
