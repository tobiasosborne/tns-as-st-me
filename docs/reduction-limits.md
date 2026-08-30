<!-- ROLE: working PHYSICS analysis, not a claims-DAG artifact and not a Lamport
     proof. Register: EFT matching, LSZ, stationary phase, perturbation theory,
     collective coordinates — the argument an experienced physicist would want
     before believing that the lattice triangle is the same object they already
     accept. Authored 2026-08-30 per TJO reduction directive (bd tns-
     reduction-program, R1-R4).

     GROUND TRUTH (L3): every continuum equation below is transcribed from
     local TeX under refs/arxiv-<id>/ with file+line. Every lattice input is
     cited by its claims/CLAIMS.md id together with its recorded status.
     Statements that are asserted on physical grounds only are marked inline
     with [PHYSICAL ARGUMENT] and are NOT claims. Nothing here upgrades,
     downgrades or creates a row in claims/CLAIMS.md. -->

# Reduction to the standard continuum setting

## 0. The question, and the four verdicts

> *The only general result that would be acceptable is one that reduces in the
> right limits back to what people actually currently accept as memory, soft
> theorem, asymptotic symmetries. It doesn't need to be rigorous, but should be
> justifiable using physical arguments, like perturbation theory.*
> (TJO, 2026-08-30.)

This document answers that question one corner at a time. It is written in the
physics register: expansions, matchings, and order-of-limits checks. It is not
a proof shard, it carries no `⟨1⟩`-anchors, and it must not be read as one.

| | reduction | verdict |
|---|---|---|
| **R1** | soft theorem (ferromagnet M1) | **REDUCES WITH CAVEATS** — the naive continuum limit is free (Dyson), but the *soft law* survives it intact: the lattice slope is exactly the inverse spin density, and it matches the accepted continuum magnon amplitude `M ∝ k₁·k₂` term by term. Caveat: the soft-scaling exponent is `σ = 1`, **not** `σ = 2`; the campaign digest's expectation was wrong. |
| **R2** | asymptotic symmetry | **DOES NOT REDUCE (as stated) / reduces only after correction** — the naive `S⁰` specialisation of the continuum construction gives exactly the group `(G_L×G_R)/G_diag` labelled by `g_L g_R⁻¹`, and that object is the campaign's own **REFUTED** row `A2-orbit-r1`. The correct lattice classifiers (`G/N_α`, `H_α\G/H_α`) have no continuum counterpart, and neither does the `H²(G,U(1))` class. The `Q^soft + Q^hard` split, by contrast, reduces cleanly. |
| **R3** | memory | **(a) REDUCES CLEANLY** — the lattice ledger `2s·δx + (q_out−q_in) = 0` becomes, with constants, the Yan–Wang–Xia magnonic spin-transfer-torque formula `V_DW = −(ρ²/2)V_g`. **(b) REDUCES WITH CAVEATS** for the Fourier-residue chain (the residue is zero; memory sits in subleading data, exactly as for the pion), and **DOES NOT REDUCE** for the kink-model transmission `T(k)`: the projection that makes `T(k)` exact is controlled at `Δ ≫ 1`, and the continuum wall lives at `Δ → 1⁺`. |
| **R4** | the edges | **REDUCES WITH CAVEATS** — the Ward-identity→LSZ→soft route is the 1709.05018 pattern and the lattice reproduces it *at two legs*; at `n` legs it is `S-general`, a CONJECTURE, and (PROTO-LSZ) has no instance. The soft→memory Fourier residue does **not** reduce, because on the lattice that edge is REFUTED (row `M`) for the reason the continuum itself predicts. |

---

## 1. R1 — the soft theorem: continuum limit of the exact magnon S-matrix

### 1.1 Lattice inputs

Two rows, both **PROVED**.

* `S2-2body-S`: for `H_S = −J Σ_x (S_x·S_{x+1} − S²)` and every `S ∈ {1/2,1,3/2,…}`,
  the exact regular-channel ratio is
  `S₁₂ = (Sab − z₁μ)/(z₂μ − Sab)`, `a = 1+z₁z₂`, `b = z₁+z₂`, `μ = (2S−1)a + b`,
  `z_j = e^{ik_j}`, and on D7's physical out/in channel with `0 < |k_h| < π` fixed,
  `∂_{k_s} δ_phys |₀ = sgn(v_h − v_s)/S`.
  (`theory/spin-s-twomagnon.md` (T.2), (T.4); verdict `theory/verdicts/spin-s-r1.md`.)
* `OR2` / oracle `O6`: `S₁₂(k_s,k_h) → 1` from either sign — "a plain limit weaker
  than an Adler-zero theorem" (`theory/oracle-bethe.md` ⟨1⟩3.⟨2⟩2, eq. (11)).
* At `S = 1/2` the rapidity form is exact: `S₁₂ = (λ₁−λ₂+i)/(λ₁−λ₂−i)` with
  `λ(k) = ½cot(k/2)` (`theory/oracle-bethe.md` eq. (8), D7).

### 1.2 The naive continuum limit is free — verified, not assumed

Put physical momenta `p = k/a` and let `a → 0` at fixed `p`. At `S = 1/2`,

```
λ(ap) = ½cot(ap/2) = 1/(ap) − ap/12 + O(a³p³),
λ₁ − λ₂ = (1/a)(1/p₁ − 1/p₂) + O(a) = (p₂ − p₁)/(a p₁p₂) + O(a),
```

so, exactly,

```
δ₁₂ = 2 arctan[ 1/(λ₁−λ₂) ] = 2 arctan[ a p₁p₂/(p₂ − p₁) ] ────────► 0.    (R1.1)
                                                             a→0
```

The rapidity diverges as `1/a`, the rapidity *difference* diverges as `1/a`, and
the S-matrix tends to the identity. **The hypothesis is confirmed: the naive
continuum theory of lattice magnons is free.** This is the one-dimensional face
of Dyson's vanishing ferromagnetic magnon scattering length, and the continuum
EFT literature says the same thing independently:

> "In the case of the ferromagnet system without external fields, the scattering
> length vanishes … This is a consequence of the derivative couplings of EFT, in
> accordance with the Goldstone theorem."
> — `refs/arxiv-1602.08692/spinwave.arXiv.final.tex` L.656.

### 1.3 The exact doubly-soft amplitude, for every spin

Expanding the `S2-2body-S` ratio to second order in both lattice momenta
(`z_j = 1 + ik_j − k_j²/2 + …`) gives, after the constant and linear parts of
numerator and denominator cancel identically,

```
N − D = −2k₁k₂ + O(k³),      D = 2iS(k₂ − k₁) + O(k²),
```

hence the **exact doubly-soft lattice amplitude**

```
S₁₂(k₁,k₂) = 1 − (i/S) · k₁k₂/(k₁ − k₂) + O(k³).                        (R1.2)
```

Two internal consistency checks. Setting `k₁ = k_s → 0` at fixed `k_h = k₂ > 0`
gives `S₁₂ = 1 + i k_s/S`, i.e. slope `1/S` — exactly `S2-2body-S` (T.4) on D8's
half-zone. At `S = 1/2`, (R1.2) is `1 − 2i k₁k₂/(k₁−k₂)`, whose soft slope is `2`,
exactly oracle `O7`/`O8`.

In physical momenta `k_j = a p_j`, (R1.2) becomes

```
S₁₂ = 1 − (i/M₀) · p₁p₂/(p₁ − p₂) + O(a²),      M₀ := S/a.               (R1.3)
```

Numerically confirmed against the exact ratio: with `k₁ = 1.7ε`, `k₂ = −0.9ε`,
the residual `|S₁₂ − (R1.2)|` falls as `ε³` for every `S ∈ {1/2,1,3/2,2,3}`
(`6.9e−5 → 6.9e−7 → 6.9e−9` at `S=1/2` for `ε = 10⁻²,10⁻³,10⁻⁴`); the soft slope
at fixed `k_h = 0.7` returns `2.000003`, `1.000002`, `0.400001` for
`S = 1/2, 1, 5/2`; and (R1.1) is reproduced to six digits. (Direct evaluation of
the `S2-2body-S` formula; this is corroboration of an expansion, not a gate.)

**All microscopic data have dropped out except one number: `M₀ = S/a`, the spin
(magnetisation) density.** `J` is absent. This is the sharp form of the R1
answer: the continuum limit is free *in the sense that the interaction strength
vanishes with `a`*, but the interaction that survives is completely fixed by the
symmetry-breaking density, exactly as an EFT physicist would demand.

### 1.4 EFT matching

Write the magnon as a Schrödinger field `ψ` with `ω(p) = p²/2m`. From
`ω_S(k) = 2JS(1−cos k) ≈ JSk²`, `m = 1/(2JSa²)`. In one dimension the two-body
S-matrix for identical bosons at Born level is `S − 1 = i m M / (2|p₁ − p₂|)`,
where `M` is the on-shell `2→2` amplitude. Comparing with (R1.3),

```
M_lattice-matched(p₁,p₂) = − 2 p₁p₂ /(m M₀) = − 4 J a³ p₁ p₂.             (R1.4)
```

Two statements follow.

**(i) The contact (scattering-length) Wilson coefficient vanishes; the leading
operator has two derivatives.** Writing the leading interactions as
`L_int = −(g₀/2)(ψ†ψ)² − (g₂/4)[(∂_xψ†)²ψ² + h.c.] + …`, (R1.4) forces `g₀ = 0`
and `g₂ ∝ 1/(mM₀) = 2Ja³`. The vanishing of `g₀` is Dyson's theorem; it is not
an assumption, it is what (R1.2) says.

**(ii) The matched amplitude is the accepted continuum magnon amplitude.** The
independent continuum EFT computation gives, for the ferromagnet with
`ω = (F²/Σ)k²`,

```
M[π(k₁)+π(k₂) → π(k₃)+π(k₄)] = (2F²/Σ²) (k₁ · k₂)
```
— `refs/arxiv-1602.08692/spinwave.arXiv.final.tex` L.640 (dispersion) and L.649
(amplitude), "in accordance with Dyson's microscopic analysis" (L.653).

The functional form is identical: proportional to `k₁·k₂`, with **no** constant
piece. Identifying `F²/Σ = 1/2m = JSa²` (spin stiffness over magnetisation
density) and `Σ = M₀ = S/a`, the continuum coefficient is `2F²/Σ² = 2Ja³`,
against the lattice-matched `4Ja³` of (R1.4).

> **[GAP, flagged]** The two agree in form and in every parametric dependence
> (`J a³`, and independence of `S` once written through `M₀`), and differ by an
> overall factor `2`. That factor is a normalisation convention — the
> relation between `M` and `S₁₂ − 1` for identical particles, and the precise
> normalisation of `Σ` and of the NG fields in
> `refs/arxiv-1602.08692`, whose appendix I have not re-derived. I assert on
> physical grounds that no physics rides on it, but I have not checked it, and
> a referee is entitled to ask. Nothing else in this document depends on it.

### 1.5 In which units and at which order the slope `1/S` is recovered

* **Per lattice momentum**: `∂_{k_s} δ_phys|₀ = sgn(v_h − v_s)/S`, dimensionless
  (`S2-2body-S`, PROVED).
* **Per physical momentum**: `∂_{p_s} δ_phys|₀ = a·sgn(v_h − v_s)/S = sgn(v_h − v_s)/M₀`.
* **As a length** (the Wigner–Eisenbud reading of oracle `O9`, "two sites" at
  `S = 1/2`): the physical displacement of the hard magnon caused by the soft one is
  `ΔX = a ∂_{k_s}δ|₀ = a/S = 1/M₀`.

So the physical combination that stays finite is the **spin density `M₀ = S/a`**,
and the soft law reads

```
lim_{p_s→0}  δ_phys(p_s, p_h)/p_s  =  sgn(v_h − v_s)/M₀ .                (R1.5)
```

This is `a`-independent as a statement about a *material*: `M₀` is the
saturation magnetisation, a finite physical quantity. It goes to zero under a
literal `a → 0` at fixed `S` only because that limit sends `M₀ → ∞`, i.e.
describes an infinitely stiff magnet. The honest EFT reading is the standard
condensed-matter one: the magnon EFT is a low-energy expansion with a physical
cutoff `Λ ∼ 1/a`, not a continuum limit, and `1/M₀` is a perfectly good
dimensionful Wilson coefficient.

### 1.6 Do the soft limit and the continuum limit commute? Answer: yes — and the
### limit that genuinely fails to commute is a different one

Test on the exact `S = 1/2` function `F(a; p_s, p_h) := δ_phys` of (R1.1).

* `lim_{a→0} lim_{p_s→0} F = 0` and `lim_{p_s→0} lim_{a→0} F = 0`. **Commute.**
* The slopes also commute: `lim_{a→0} ∂_{p_s}F|₀ = lim_{a→0} 1/M₀ = 0`, and
  `∂_{p_s}[lim_{a→0}F]|₀ = 0`. **Commute.**

There is nothing to fail here, and the reason is structural: `a` enters the
exact S-matrix only through the change of variables `k = ap`. **The soft and
continuum limits commute on the exact S-matrix, in both orders, at every spin.**

What does *not* commute is the soft limit against the limit in which the *hard*
leg also becomes soft. From (R1.2),

```
lim_{k_h→0} [ ∂_{k_s} δ_phys |_{k_s=0} ] = 1/S ,
∂_{k_s} [ lim_{k_h→0} δ_phys ] |_{k_s=0} = 0 .                          (R1.6)
```

The two orders differ by the whole content of the theorem. This is the same
non-uniformity oracle `O9` already records ("non-uniform at `k_h → 0`") and that
D8 fences by holding `0 < |k_h| < π` fixed; the quadratic coefficient
`|v_h|/ω_h = cot(k_h/2) ≈ 2/k_h` diverges there. The physical content is that
"soft" is a statement about the **ratio** `k_s/k_h = p_s/p_h`, which is
`a`-independent. That is precisely why R1 survives the continuum limit: the
soft theorem constrains a scale-invariant ratio, and only the overall size of
the interaction carries the factor of `a`.

### 1.7 Where the type-B soft-scaling bound sits — and a correction

The relevant continuum machinery is the current-conservation pole cancellation.
From `refs/arxiv-2201.01393/manuscript.tex`:

```
⟨Ω|J^μ(x)|θ(p)⟩ = e^{−ip·x}[ i p^μ F₁(|p|) + i δ^{μ0} F₂(|p|) ]            (L.409-411)
ω²F₁ + ωF₂ − p²F₁ = 0                                                     (L.414, onshellcurrent)
⟨β|J^μ(0)|α⟩ = i/(p⁰ − ω(|p|)) ⟨Ω|J^μ(0)|θ(p)⟩⟨β+θ(p)|α⟩ + R^μ(p)          (L.420, polecurrent)
⟨β+θ(p)|α⟩ = [p⁰R₀(p) + p^r R_r(p)] / [ω(|p|)F₁ + F₂] |_{p⁰=ω(|p|)}       (L.430, NRAdler)
```

with the explicitly non-automatic hypothesis, quoted verbatim:

> "With the additional assumption that `R^μ(p)` is non-singular when `p^μ` is
> on-shell *and* the limit `p → 0` is taken, which does not automatically follow
> from standard polology rules, we obtain the Adler zero"
> — `refs/arxiv-2201.01393/manuscript.tex` L.433.

The bounds are

```
σ ≥ min(m,  n+1)   (d ≥ m+1)   for type A_m       (L.487, eq. A)
σ ≥ min(2m, n+1)               for type B_{2m}    (L.489, eq. B)
```

where `n` is the degree of the theory's *generalised spatial shift symmetry*
`α(x) = ε_{ν₁…ν_n} x^{ν₁}…x^{ν_n}` (L.470-473).

The ferromagnet magnon is type `B₂` (`m = 1`; the classification is at L.125-129
and the digest records it). Its broken generators `S^x, S^y` generate the
*ordinary* constant shift of the NG field, so `n = 0`. Equation (B) then reads

```
σ ≥ min(2·1, 0+1) = 1 .                                                  (R1.7)
```

The exact lattice amplitude (R1.2) vanishes **linearly** in either soft
momentum: `σ = 1` exactly. **The lattice saturates the ordinary Adler bound and
exhibits no enhancement.** Read through (NRAdler): with `ω ∝ p²`, the temporal
piece `p⁰R₀ = ωR₀ ∼ p²R₀(0)` is already `σ = 2`, but the spatial piece
`p^r R_r ∼ p R_r(0)` is only `σ = 1` unless a degree-`n ≥ 1` spatial shift
symmetry forces `R_r(0) = 0`. The Heisenberg ferromagnet has no such redundant
symmetry, so `R_r(0) ≠ 0`, and `σ = 1` is the correct answer.

> **[CORRECTION to `docs/continuum-antecedents.md`.]** That digest's §5
> translation obligation says "Conjecture S's `S(k)→0 linearly` claim must be
> shown to be the σ=2 bound of eq. (B) with m=1", and its Surprise 2 says
> "type-B enhancement needs no extra symmetry". Both are wrong as written.
> Linear vanishing *is* `σ = 1`. And 2201.01393 is explicit that its two type-`B₂`
> theories reach `σ = 2` *because* they "possess one layer of redundant
> generators, generating a linear spatial generalized shift symmetry with
> `α(x) = ε_r x^r`" — i.e. `n = 1` — "According to eq. (B) these theories must
> satisfy σ ≥ min(2m, n+1) = 2" (L.525-527). What is special about type B is
> that `n = 1` *suffices* to reach `σ = 2` (type `A₁` with `n = 1` gets only
> `min(1,2) = 1`, L.537), not that `n = 0` does. The lattice ferromagnet has
> `n = 0` and lands on `σ = 1`, in agreement with eq. (B) and with the exact
> two-magnon computation. Nothing about the campaign's proved rows changes;
> only the digest's expectation of an enhanced zero was mistaken.

### 1.8 R1 verdict

**REDUCES WITH CAVEATS.** The exact lattice soft law reduces to the accepted
continuum statement — the derivative-coupled type-`B₂` Goldstone with vanishing
scattering length, amplitude `∝ k₁·k₂`, ordinary Adler zero `σ = 1` — with the
lattice slope `1/S` per lattice momentum becoming `1/M₀` per physical momentum,
`M₀` the spin density. Caveats:

1. The literal continuum limit at fixed `S` is free; the physical statement
   requires a finite spin density, i.e. a finite lattice constant. This is
   standard EFT practice, but it must be said out loud.
2. The soft-scaling exponent is `σ = 1`, not `σ = 2`.
3. The overall factor-2 normalisation against `refs/arxiv-1602.08692` is
   unverified (§1.4).

---

## 2. R2 — asymptotic symmetry

### 2.1 The specialisation the continuum construction actually makes

In the continuum, asymptotic symmetries assign one charge per function on the
celestial sphere: `Q[f]`, `f ∈ C^∞(S²)`. In `1+1` dimensions the celestial
sphere is `S⁰` — two points, the left and right spatial infinities. A function
on two points is a pair `(g_L, g_R)`, and the global (diagonal) symmetry acts
trivially on the pair's physical content, so the naive specialisation is

```
𝒜 = (G_L × G_R)/G_diag ,   with complete invariant [g_L g_R⁻¹] .          (R2.1)
```

This is exactly the group written down in the campaign brief
(`HANDOFF_MPS_SOFT_THEOREM.md` L.85). It is the correct *guess*.

### 2.2 It is the campaign's own refuted row

`claims/CLAIMS.md` row `A2-orbit-r1`:

> "r1 form of A2(e): the `𝒜 = (G_L×G_R)/G_diag` orbit is the set of vacuum
> pairs, labelled by `[g_L g_R⁻¹]`" — **REFUTED**, disproved in
> `theory/corner-a-kinks.md` ⟨1⟩9.⟨2⟩5.⟨3⟩3, checker `corner_a_check.py` C7.

The lattice replaces it with two different objects, both **PROVED**:

* **Unbroken case** (`A1(e)`): the orbit is `𝒜_eff = G/N_α`, where
  `N_α = ker ρ_α` and `ρ_α: G → PGL(χ)` is the virtual representation; the
  stabiliser is `S_α ⊇ G_diag`, with equality iff `N_α = {e}`. The row states
  explicitly "**not** `𝒜`".
* **Broken case** (`A2(e)`): under transitivity, vacuum pairs form
  `(G/H_α) × (G/H_α)` with stabiliser `H_α × H_β`, and the complete diagonal
  invariant is the **double coset** in `H_α \ G / H_α`.

### 2.3 Where they agree and where the lattice adds structure

**Agree.** When `N_α = {e}` and `H_α = {e}` — a faithful virtual representation
and a completely broken symmetry — `G/N_α = G` and `H_α\G/H_α = G`, and both
lattice classifiers collapse to (R2.1). *The continuum answer is the lattice
answer in the generic, structureless case.* [PHYSICAL ARGUMENT: the collapse is
group theory, but the statement that this is the "right" continuum limit is a
matching claim, not a theorem.]

**Lattice adds, continuum has no counterpart.**

1. `N_α` is a *finite* normal subgroup of `G`, produced by the projective
   virtual representation on a `χ`-dimensional bond space. There is no bond
   space in the continuum construction and hence nothing that could produce it.
   When `N_α ≠ {e}` the continuum group over-counts: distinct `(g_L, g_R)` act
   identically on the lattice state.
2. The cohomology class `[ω_α] ∈ H²(G,U(1))` — the SPT index, and `A1(d3)`'s
   statement that it obstructs *removing the multiplier* (lifting `ρ_α` to an
   honest `G → U(χ)`), not the projective window action. This is a discrete
   invariant of the *representation*, not of the symmetry group, and it has no
   image at all in (R2.1).
3. `H_α`, the vacuum stabiliser, and with it the double-coset (rather than
   single-coset) structure. The continuum `S⁰` construction has no notion of a
   vacuum manifold with nontrivial stabilisers built into the charge labels.

**Continuum has, lattice does not.** The logarithmic celestial-Goldstone CFT of
`refs/arxiv-2504.10577` (discrete-series representation theory of the massless
little group) has no lattice analogue and should not be sought — this was
already recorded as Surprise 3 in the digest and remains correct.

### 2.4 The `Q^soft + Q^hard` split does reduce

The continuum construction, quoted from `refs/arxiv-1709.05018/draft1004.tex`:

```
Q^soft(q̂) := −(i/4π) lim_{ω→0} ( a†_{ωq̂} − a_{ωq̂} )                       (L.360-362)
⟨out| ( Q(q̂) S − S Q(q̂) ) |in⟩ = 0,   Q = Q^soft + Q^hard                 (L.377-386)
Q^hard(q̂) := (y/8πm²) ∫ d³p/((2π)³ 2E_p) Σ_{s,r}( ū^r γ⁵ [q^μp^νγ_{μν}/(p·q)] u^s a†a + … )   (L.387-389)
```

The lattice mirror is structurally exact and uses only PROVED machinery.

* **The modulated charge.** `Q[f;ξ] = Σ_x f(x) q_x(ξ)` with the continuity
  equation `[H, Q[f;ξ]] = Σ_x (Δf)(x) j_{x|x+1}(ξ)` for any `ξ ∈ 𝔤` and any
  finite-range `H` (row `G0(e)`, PROVED). This is the lattice
  `∂_μ j^μ = 0` and it is exact, with the second difference `Δf` playing the
  role of the derivative of the celestial profile.
* **The soft part.** Acting with `Q[f;ξ]` on the vacuum creates a magnon at the
  momentum content of `f`; the exact finite-window identity `G0(c)` gives
  `|Φ_k^Λ(B_G)⟩ = (1−e^{ik}) Σ_{m=a}^{b−1} e^{ikm}|ψ; X@m⟩ + (two boundary
  terms)`, so as `k → 0` the created state is a soft magnon of amplitude
  `O(k)`. This is `Q^soft`, and the lattice version keeps the boundary terms
  *explicitly* rather than assuming them away.
* **The hard part.** Acting with the same charge on a prepared hard magnon
  deforms the hard leg. Row `AC-EX-2M-D29` records the exact two-body
  statement
  `Q_{k_s}|k_h⟩ − |B^in⟩ = (1 − S₁₂)|P₁₂⟩ = −2i k_s |P₁₂⟩ + O(k_s²)` at
  `S = 1/2`, which is the lattice `[Q^soft + Q^hard, S] = 0` with a computable
  defect: the *failure* of the soft charge to be absorbed by the hard leg is
  precisely the soft factor. This is the same bookkeeping as 1709.05018's
  L.377-389, with `sgn(v_h − v_s)/S` in place of the fermion spin-rotation
  kernel `q^μ p^ν γ_{μν}/(p·q)`.
* **Both continuum factors are `O(1)`, not `O(1/ω)`.** 1709.05018's soft pion
  theorem starts at subleading order (its footnote at L.700-702: "the soft pion
  theorem starts from subleading order while the soft photon and graviton
  theorems start from the leading order"). Ours does too: `S₁₂ → 1`, no pole.
  The lattice is in the *pion* universality class, not the photon/graviton one.

### 2.5 R2 verdict

**DOES NOT REDUCE, as stated** — with a precise and constructive reading. The
naive `S⁰` specialisation of the continuum asymptotic-symmetry group is
literally the campaign's REFUTED row. The correct lattice objects reduce *to*
it in the structureless case `N_α = H_α = {e}`, and the difference is exactly
the structure the continuum construction cannot see: a finite kernel `N_α`, a
vacuum stabiliser `H_α`, and an `H²(G,U(1))` class. The charge-split half of
Corner A (`Q^soft + Q^hard`, Ward identity, continuity equation) **reduces
cleanly** and is the piece the referee will recognise. For the Letter this
means: present Corner A as a *correction* of the naive `1+1` specialisation, not
as its confirmation.

---

## 3. R3 — memory

### 3.1 (a) The magnonics reduction, with constants

**Continuum statement** (`refs/arxiv-1106.4382/swstt.tex`, Yan–Wang–Xia,
PRL 107, 177207; verified title, see `refs/LEDGER.md`):

* the spin wave passes a transverse (Walker) domain wall **without reflection**,
  `φ(ξ) = ρ(tanh ξ − iq)/(−iq−1) e^{iqξ}` solving
  `q²φ = [−d²/dξ² − 2 sech²ξ]φ`, `ξ = z/Δ_W`, `q² = ω/K − 1` (L.163-172);
* "A magnon changes its spin by `2ħ` (the magnon spin flips from `−ħ` to `ħ`)
  after passing through the DW … This angular momentum is absorbed by the DW"
  (L.81-84);
* the spin current reverses, `J_z = −Aρ²k` on the far left and `+Aρ²k` on the
  far right (L.213-217);
* "in order to absorb this torque, the DW must propagate to the left with the
  velocity `V_DW = −(ρ²/2) V_g ẑ`, where `V_g = ∂ω/∂k = 2Ak`" (L.219-222).

**Lattice statement.** `M-quant-G` (PROVED, conditional on H-AD-G) and
`M-quant` (PROVED, conditional on D18) give, with the frozen windowed wall
coordinate `𝔛_W := a−1 + (1/2s) Σ_{x=a}^b (S^z_x + s)` of D13(a),

```
ΔX = −N_T/s ,      δx = −⟨N_T⟩/s ,      2s·δx + (q_out − q_in) = 0 ,      (R3.1)
```

with the channel charges fixed as `q_in = q_L = −1`, `q_T = +1`.

**The reduction.** These are the same equation. The charge arithmetic
`q_out − q_in = (+1) − (−1) = 2` *is* Yan–Wang–Xia's "the magnon spin flips from
`−ħ` to `ħ`": in the up-domain the magnon is a `−1` flip of `S^z`, in the
down-domain a `+1` flip, and the difference `2ħ` is deposited on the wall.

Translate to physical units. Let `a` be the lattice constant, `M₀ = s/a` the
spin density (this is the same `M₀` that appeared in R1), and `δX = a·δx` the
physical wall displacement. Then `2s·δx = 2(M₀a)(δX/a) = 2M₀ δX`, so (R3.1) is

```
2 M₀ δX + (q_out − q_in) = 0    ⟹    δX = −1/M₀  per transmitted magnon.   (R3.2)
```

Differentiating with a transmitted-magnon flux `Φ` (magnons per unit time),

```
V_DW = −Φ/M₀ .                                                            (R3.3)
```

Now evaluate `Φ` for Yan–Wang–Xia's spin wave. Their `m` is a unit vector with
transverse amplitude `|φ| = ρ` in the asymptotic domains (L.180-182), so
`m_z = √(1−ρ²) ≈ 1 − ρ²/2`; each magnon reduces `S^z` by one unit, so the magnon
number density is `n = M₀ ρ²/2`. The wall is reflectionless (`T = 1`), so
`Φ = n V_g = M₀ ρ² V_g /2`, and (R3.3) gives

```
V_DW = −(ρ²/2) V_g ,                                                      (R3.4)
```

which is **exactly** `refs/arxiv-1106.4382/swstt.tex` L.220-222, constants
included. Independently of `J`, of `Δ`, of the wall profile, and of the magnon
momentum.

Note also that (R3.2) is numerically the same physical length as the R1 Wigner
displacement `ΔX = 1/M₀` of §1.5. That coincidence is Conjecture `Bc` ("the two
2s") given a continuum reading: both quantities are one inverse spin density.
[PHYSICAL ARGUMENT — `Bc` remains CONJECTURE; this observation identifies a
common continuum unit and proves nothing.]

**Verdict R3(a): REDUCES CLEANLY.** One caveat, and it is a caveat about scope,
not correctness: the lattice statement is conditional on D18 / H-AD-G
(asymptotic completeness with definite channel charges), which the continuum
derivation replaces with the reflectionless closed-form solution. The lattice
therefore *assumes* what the continuum *computes*. Full-chain D18 is open
(bd `tns-d51`).

### 3.2 (b) The Strominger–Zhiboedov Fourier-residue chain

**The continuum chain** (`refs/arxiv-1411.5745/memory_4.tex`):

```
h^TT_{μν}(ω,k) = 4πi lim_{r→∞} r ∫du e^{iωu} h^TT_{μν}(u, r k)             (L.687-690)
Δh^TT_{μν}(k) = (1/4πi r₀) lim_{ω→0} ( −i ω h^TT_{μν}(ω,k) )               (L.693-695)
lim_{ω→0} ω h^TT_{μν} ε^{μν} = √(8πG) ε^{μν} ( Σ p p/(k·p) − Σ p'p'/(k·p') )^TT   (L.697-701)
```

with the falloff assumption stated in words at L.691-692:

> "Assuming that `h^TT_{μν}(u, r k)` approaches finite but different values at
> `u → ±∞` and large `r = r₀` it then follows … that [the Braginsky–Thorne
> memory] is proportional to the coefficient of the pole in `ω`"

and, in the footnote attached to that sentence,

> "In the formulas above we assume that `ω r ≫ 1` when taking the limits."

**The lattice image.** Row `M-flux` (PROVED, unconditional):

```
δx = (1/2s)[ ȷ̃_{a−1|a}(0) − ȷ̃_{b|b+1}(0) ]                                (R3.5)
```

— exactly the finite-time zero-frequency weight of the **physical boundary
current**, from the exact telescoping of `d𝔛_W/dt = j_{a−1|a} − j_{b|b+1}`
(`theory/memory-quantization.md` §1, Lemma Mq-flux). And D13(b) writes the same
number as a genuine DC residue: with `D(x) = lim_{ω→0} ∫dt e^{iωt} ṁ_x(t)
= m_x(+∞) − m_x(−∞)`, `δx^spec = (1/2s) Σ_{x∈W} D(x)`.

So the *Fourier-residue structure* reduces correctly: memory is a zero-frequency
weight, and "the Fourier transform of a pole in frequency space is a step
function in time" (`refs/arxiv-1703.05448/soft_Arxiv_update.tex` L.333) is
realised on the lattice by (R3.5). **What does not reduce is the identification
of that residue with the soft factor.**

The continuum chain works because `lim_{ω→0} ω h^TT` is *finite and nonzero* —
there is a genuine `1/ω` pole, supplied by Weinberg's `p_μ p_ν/(k·p)`. The
lattice soft factor has no pole: `S₁₂ → 1` (row `OR2`), `σ = 1` (§1.7). Applying
the same chain to it gives `lim_{ω→0} ω × (regular) = 0`. Row `M` records
exactly this outcome:

> "The brief's literal Conjecture M (`δx` = DC limit of the soft factor) is
> **REFUTED**. The surviving candidates are `M-flux` (physical boundary-current
> DC weight only) and conditional `M-quant`, into which soft data enter through
> `T(k)`."

This is not a lattice pathology. It is precisely the continuum situation for a
derivative-coupled Goldstone, and 1709.05018 warns of it in advance: because the
soft pion theorem starts at subleading order, the pion memory lives in the
*subleading* falloff coefficient,

```
π^{(2)}_{ℐ⁺}(u = ∞, θ) = ¼ Δ_{S²} Q^hard(q̂(θ))                            (L.810-812)
```

with the footnote at L.700-702 giving the reason ("This pion memory effect is
small compared with that of QED and QG where the leading effect is `O(1/r)`.
This corresponds to the fact that the soft pion theorem starts from subleading
order").

**Which lattice observable is which falloff coefficient.** The dictionary, at
physics level:

| continuum (1709.05018) | lattice |
|---|---|
| leading radiative coefficient `π^{(1)}` (the `1/r` term) | the outgoing one-magnon wave amplitudes on the two legs, `t(k)`, `r(k)` (D15). Carries the phase; carries **no** DC shift. |
| subleading coefficient `π^{(2)}` (the `1/r²` term), where the memory lives | the **integrated** asymptotic tail content `Σ_{x>b}(ϱ(S^z_x)+s) = 2s N_T` (D14). |
| `Q^hard(q̂)`, the escaped hard charge | `q_out − q_in = 2 N_T` per transmitted magnon (row `M-quant-G`) |
| `π^{(2)}(u=∞) = ¼Δ_{S²}Q^hard` | `δx = −⟨N_T⟩/s`, a linear functional of the escaped charge (R3.1) |

Both sides say the same thing: **memory is a linear functional of the integrated
hard charge that escaped, not the residue of a soft pole.**

**What plays the role of the falloff assumption.** The continuum needs
"`h^TT` approaches finite but different values at `u → ±∞`". The lattice named
hypotheses are:

* **D17**, the `ℓ¹` kink class: `Σ_{x<0}|ϱ(S^z_x) − s_α| + Σ_{x>0}|ϱ(S^z_x) − s_β| < ∞`
  (plus a first-moment condition when D13(c) is used). This is the lattice
  "approaches finite but different values", made a function-space condition.
* **D18 (H-AD)**: wave operators, channels, and local decay — the lattice
  "the radiation has left" condition.
* **D13(b)**: `ṁ_x ∈ L¹(dt)` for each `x ∈ W`, which is what makes the DC
  residue exist at all.

And the lattice records its *own* order-of-limits fence in D17, in words that
are a direct counterpart of Strominger–Zhiboedov's `ωr ≫ 1` footnote:

> "`𝒦^{(1)}` … is **not** preserved by the `k → 0` limit — a plane-wave magnon
> is not `ℓ¹`. **Every soft statement about memory must fix the packet first and
> take `k → 0` afterwards; the two limits do not commute.**" (D17)

and, in D13(b), "The `ω→0` limit must be taken at fixed `x` and fixed `W`,
*after* the thermodynamic limit; interchanging `ω→0` with `|W|→∞` destroys it."
These are the lattice's `ωr ≫ 1`. The correspondence is exact and it is to the
lattice's credit that both fences are stated in the definitions rather than in a
footnote.

**Verdict R3(b): REDUCES WITH CAVEATS.** The DC-weight structure reduces; the
falloff assumptions have named lattice counterparts; the soft-factor-residue
identification does *not* reduce and must not be claimed — for the reason the
continuum pion literature itself gives.

### 3.3 (c) The kink model at `Δ → 1⁺`, and `T(k)`

**Lattice input.** Row `M-tk` (PROVED, projected, unconditional): on D16's
projected incoming `≤3`-wall component,

```
t(k) = [1 + iJ²/(4ω v)]⁻¹ ,   T(k) = [1 + (J²/(4ωv))²]⁻¹ ,                (R3.6)
T(k) = 16(Δ−1)²k² + O(k⁴)  as k → 0,     k_* = 1/(4(Δ−1)) .
```

**What continuum theory does D16 approach as `Δ → 1⁺`?** The easy-axis
Landau–Lifshitz ferromagnet of Yan–Wang–Xia. The wall width is set by
`q = Δ − √(Δ²−1)`; writing `Δ = 1 + ε`, `q ≈ 1 − √(2ε)`, so
`ξ_DW = 1/ln(1/q) ≈ 1/√(2ε)` lattice sites. Compare the continuum
`Δ_W = √(A/K)` with `A ∼ Ja²` and `K ∼ J(Δ−1)`: `Δ_W/a = 1/√(Δ−1)`. The two
agree up to `√2`. The dispersions agree exactly in this scaling limit:

```
ω(k) = J(Δ − cos k) ≈ J(Δ−1)[1 + k²/(2(Δ−1))] = ω_gap (1 + q_c²),
q_c := k ξ_DW ,                                                           (R3.7)
```

which is precisely Yan–Wang–Xia's `q² = ω/K − 1` (L.166). **So D16's magnon
sector reduces cleanly to the continuum Landau–Lifshitz magnon on a wide wall,
in the scaling limit `Δ → 1⁺`, `k → 0`, `q_c = k ξ_DW` fixed.** That part is
clean.

**But `T(k)` does not.** In the same scaling limit, `ω ≈ Jε(1+q_c²)`,
`v = J sin k ≈ J q_c √(2ε)`, so

```
J²/(4ωv) ≈ 1/(4√2 · ε^{3/2} q_c (1+q_c²))  ────────►  ∞ ,
                                            ε→0
T ≈ [4√2 ε^{3/2} q_c (1+q_c²)]²            ────────►  0 .                 (R3.8)
                                            ε→0
```

The projected Fano wall becomes **totally reflecting** exactly where the
continuum wall is **exactly reflectionless**. This is a hard mismatch, and it
must be reported as one.

**Why, physically.** The `Δ → 1⁺` kink is a *wide* object: the exact zero-energy
product family `|K(z)⟩ = ⊗_n (|↑⟩_n + z q^n |↓⟩_n)` with `q → 1` is, in the
`S^z` product basis, a broad superposition over configurations with *many*
domain walls. The Mq-E projection that makes (R3.6) exact keeps only the
`≤3`-wall component, and the measured leakage into `≥5`-wall configurations is
`O(Δ^{-2})`: `8·10⁻³` at `Δ = 8`, `3·10⁻²` at `Δ = 4`, `1·10⁻¹` at `Δ = 2`
(`theory/corner-b-draft.md` §5.2). Extrapolated to `Δ → 1⁺` the leakage is
`O(1)`. **The projection is controlled in the Ising regime and uncontrolled in
the continuum regime; the two regimes are disjoint.** Equivalently: the
continuum reflectionlessness comes from the `−2 sech²` Pöschl–Teller potential
having its bound state exactly at threshold (`φ = ½ sech ξ` at `q = −i`, `ω = 0`,
L.174-176) — the wall's translational zero mode sitting at the band edge. The
projected Fano graph does have a side-coupled kink level, but its detuning
`ω(k) = J(Δ − cos k)` stays finite as `k → 0`, so the threshold cancellation that
produces `T = 1` is absent from the truncated model.

**Where the two *do* agree.** At `Δ ≫ 1`, (R3.6) gives
`R(k) ≈ 1/(16Δ² sin²k)` — the wall is transparent to `O(Δ⁻²)`, the crossover
momentum `k_* ≈ 1/(4Δ)` is small, and for all `k ≫ k_*` the lattice wall
reproduces the continuum reflectionless result. The residual `T → 0` at `k → 0`
is a band-edge effect (a slow particle cannot cross a finite barrier) with no
counterpart in the reflectionless continuum calculation.

**Verdict R3(c): DOES NOT REDUCE.** The dispersion does; `T(k) = 16(Δ−1)²k²`
does not, because the projection making it exact and the continuum wide-wall
limit are controlled in opposite regimes. **What this means for the paper:**
`T(k)` must not be presented as "the lattice version of magnon-driven wall
motion". The memory law (R3.1) is that; it is a conservation law and is
independent of `T` (`theory/corner-b-draft.md` §5.2 says so explicitly: the
leakage "affects `T(k)`; it does not affect the memory law of §6, which is a
conservation law"). `T(k)` sets only the *size* `⟨N_T⟩` of the effect in the
Ising regime. The continuum-regime transmission is an open computation.

---

## 4. R4 — the edges

### 4.1 `A ⇒ C`: Ward identity plus LSZ gives the soft theorem

The cleanest continuum precedent is 1709.05018 §4.3, which proves that the
"exotic" asymptotic-symmetry derivation and the textbook broken-Ward–Takahashi
derivation coincide. From `refs/arxiv-1709.05018/draft1004.tex`:

```
j^μ_π := δL/δ∂_μπ = −∂^μπ − (2λ/m_φ φ + λ²/m_φ² φ²)∂^μπ + (iy/2m) ψ̄ γ^μ γ⁵ ψ   (L.444-448)
⟨∂_μ j^μ_π(x) Π_i π(x_i) Π_a O(x_a)⟩ = −i Σ_i δ⁴(x−x_i)⟨Π_{j≠i} π(x_j) Π_a O(x_a)⟩  (L.451-453)
```

and the recipe, quoted:

> "First, we perform the Fourier transformation from `x^μ` to massless on-shell
> momentum `ωq^μ` and apply the LSZ reduction to the remaining fields. Then, if
> we take the soft limit `ω → 0`, the right-hand side of the identity vanishes,
> and furthermore in the left-hand side, the first term … gives the amplitude
> with one soft pion, the second term does not contribute in the soft limit and
> the last term gives the amplitude with soft factors. Thus, the soft pion
> theorem is obtained from the Ward–Takahashi identity." (L.455-461)
>
> "Therefore, the Ward–Takahashi identities discussed in section 4.2 are
> included in the Ward–Takahashi identity for the broken `U(1)_A` symmetry."
> (L.463)

**Lattice mirror, step by step.**

1. *Current.* `G0(e)`, PROVED: `[H, Q[f;ξ]] = Σ_x (Δf)(x) j_{x|x+1}(ξ)`, exact,
   any `ξ ∈ 𝔤`, any finite-range `H`. This is the lattice `∂_μ j^μ_π = 0` and
   needs no boundary at infinity — matching De Luca–Khoury–Wong's local
   programme (`refs/arxiv-2412.01910`) rather than a null-infinity construction.
2. *Ward identity.* `WI`, PROVED: the truncated symmetry telescopes to exactly
   two boundary-bond insertions. This is the lattice `δ⁴(x−x_i)` contact term,
   and the lattice version is *finite and computed*, with the two boundary terms
   retained (the D5 warning records that discarding them is false at finite
   window: measured `‖·‖ = 1.77` at `χ=2`, `k = 0.37`).
3. *Fourier + LSZ.* The lattice replaces the plane-wave Fourier transform by the
   momentum-superposition of window vectors (`G0(c)`, D12) and LSZ by the
   Haag–Ruelle / excitation-ansatz wave-operator construction (D31, `AC-EX-2M`).
4. *Soft limit.* At two legs the endpoint is PROVED:
   `S-IDX-MATCH-HS-SEP` and `S-IDX-D29-value-HS-SEP` give
   `A_*(ε) = i sgn(v_h − v_s) k̄_*(ε)/S + O(ε²)`, phase slope `sgn(v_h−v_s)/S`,
   on the separated-preparation subclass.

**Caveat, and it is the load-bearing one.** At `n` legs this is `S-general`,
**CONJECTURE**, with the hypothesis `(PROTO-LSZ)` *uninstantiated*
(`S-IDX-spec-struct-r2`, SKETCH; `AC-EX-2M-D29` records two named missing steps).
The lattice therefore reproduces the 1709.05018 pattern *as a template* and
*as a theorem at two legs*, not as an `n`-leg theorem.

### 4.2 `C ⇒ B`: soft to memory by Fourier residue

Covered in §3.2. The residue *structure* reduces (`M-flux`, PROVED); the
*content* — memory equals the residue of the soft factor — is **REFUTED** on the
lattice (row `M`), because there is no pole. The correct lattice edge runs
through charge conservation (`M-quant-G`), which is the pion-memory pattern of
1709.05018 (memory = a linear functional of the escaped hard charge), not the
graviton pattern of 1411.5745.

### 4.3 The two-column correspondence of silent assumptions

Stated as fact. Left column: an assumption the continuum derivation makes and
does not prove. Right column: the named lattice hypothesis that occupies the
same slot, with its status.

| continuum assumption (source, line) | lattice hypothesis | lattice status |
|---|---|---|
| `R^μ(p)` non-singular on-shell as `p → 0`; "does not automatically follow from standard polology rules" (2201.01393 L.433) | the remainder bounds of `(PROTO-LSZ)` and D24(d) clause 3a (`C¹`-extension of the descendant quotient `L(k,h)`); `(WI)`-telescoping is the mechanism intended to *prove* rather than assume it | `(PROTO-LSZ)` **uninstantiated**; `ML5-B` PROVED only as a conditional implication; `S-general` CONJECTURE. **This is the campaign's advertised technical advantage and it is not yet cashed.** |
| no additional singularities besides the NG pole; no bilinear current insertions on external legs (2201.01393 L.437-439) | `G0-soft-r1` — the r1 claim that `(e^{ik}−1)` is a *universal* soft factor — was **REFUTED**: "hard data can enter at `O(k)` through `J_k`" | REFUTED; the lattice found the loophole rather than assuming it shut |
| `h^TT` approaches finite but different values as `u → ±∞` (1411.5745 L.691-692) | D17 (`ℓ¹` kink class), D18 (H-AD: wave operators, channels, local decay), D13(b) (`ṁ_x ∈ L¹`) | D17, D13(b) definitions; D18 **open** at full chain (bd `tns-d51`) |
| `ωr ≫ 1` when taking the limits (1411.5745, footnote at L.692) | D17: "every soft statement about memory must fix the packet first and take `k → 0` afterwards; the two limits do not commute"; D13(b): `ω→0` after the thermodynamic limit | frozen in the definitions |
| no `O(r⁰)` term; stationary-phase mode expansion at large `r` for the Bondi expansion (1709.05018 L.506, L.515-526) | Haag–Ruelle wavepacket construction (D31), `AC-EX-2M`; velocity-support separation D31(4) | `AC-EX-2M` established; `AC-EX-2M-D29` SKETCH with named gaps |
| no surface terms in the Ward identity (generic) | `WI` (PROVED) keeps the two boundary-bond insertions **explicitly**; the D5 r2 warning records that setting them to zero is *false* at finite window | PROVED, with the surface terms computed |
| hyperbolic foliation / `τ^{−3/2}`, `τ^{−3}` falloff to make `Q^hard` a finite integral (1709.05018 L.559-576, L.649-654) | D13(a) windowing: `𝔛_W ∈ 𝔄_loc` unconditionally, "so `δx` exists on all of `𝔄^*` and at finite `N`, with no asymptotic hypothesis and no order-of-limits clause" | definition; this slot the lattice *removes* rather than assumes |
| "physical mode condition" and transversality/adiabaticity, "imposed by hand" (2412.01910 L.358-361) | the admissible-profile condition on `f` in `Q[f;ξ]`: D12(a′) `f ∈ ℓ¹ ∩ BV` for real-space identities, D12(b) `δ`-normalisation for fixed-`k` identities, with the "type discipline" fence | frozen in D12; the fence explicitly calls unlabelled "exact" quotations defects |

### 4.4 R4 verdict

**REDUCES WITH CAVEATS.** Every silent continuum assumption has a named lattice
counterpart, and in two slots (windowed memory, surface terms) the lattice
*eliminates* the assumption rather than renaming it. The caveats: the `A ⇒ C`
edge is a theorem only at two legs; the `C ⇒ B` edge does not run through a
Fourier residue of the soft factor and must not be advertised as doing so; and
the regularity slot — the one the campaign claims as its chief contribution
relative to the continuum — is still occupied by an uninstantiated hypothesis.

---

## 5. Every gap, listed

Asserted on physical grounds, not proved, and flagged inline above:

1. **§1.4** — the factor-2 mismatch between the lattice-matched amplitude
   `4Ja³p₁p₂` and `refs/arxiv-1602.08692`'s `2F²/Σ² (k₁·k₂) = 2Ja³p₁p₂` under the
   identification `Σ = S/a`, `F² = JS²a`. Asserted to be a normalisation
   convention; not verified against that paper's appendix.
2. **§1.4** — the claim that `g₀ = 0` exactly (not merely at leading order in
   `a`) is read off the leading doubly-soft expansion (R1.2); higher orders in
   `a` are not computed and could in principle generate a contact term at
   `O(a²)`. Not checked.
3. **§2.3** — that `N_α = H_α = {e}` is the correct "continuum-like" corner of
   the lattice classification is a matching assertion. There is no theorem
   saying the continuum construction *is* the `N_α = {e}` case.
4. **§3.1** — the magnon number density `n = M₀ρ²/2` used to convert
   Yan–Wang–Xia's `ρ` into a magnon flux is the standard linear-spin-wave
   identification. It is exact to `O(ρ²)`; the match (R3.4) is therefore a
   leading-order match, as is their own derivation.
5. **§3.1** — (R3.1) is conditional on D18 / H-AD-G, which is open at full chain.
   The continuum derivation does not need it because it solves the scattering
   problem in closed form. A referee may reasonably say the lattice has assumed
   the physics content and derived the bookkeeping.
6. **§3.3** — the extrapolation "leakage is `O(1)` at `Δ → 1⁺`" is an
   extrapolation of three measured points at `Δ = 8, 4, 2`. It is not a bound.
7. **§3.3** — the threshold/zero-mode explanation of why the projected Fano wall
   is not reflectionless is a physical reading, not a computation. What is
   established is only that the two computations disagree in the limit.
8. **§1.7** — the assignment `n = 0` to the Heisenberg ferromagnet (no redundant
   generalised spatial shift symmetry) is asserted from the structure of the
   broken generators. I have not run a Lie-algebraic classification in the sense
   of 2201.01393 §2 to exclude one.

Two housekeeping corrections generated by this work:

* The `σ = 2` expectation in `docs/continuum-antecedents.md` §5 and Surprise 2
  is wrong; see the correction box in §1.7. The correct statement is `σ = 1`,
  saturating eq. (B) at `n = 0`.
* The reduction directive named arXiv:1108.5570 for Yan–Wang–Xia. That id is a
  mathematics paper on submanifolds; the correct id is **arXiv:1106.4382**,
  fetched, title-verified and ledgered.

## 6. The single most referee-dangerous gap

Not any of the above individually. It is this: **the memory corner is proved
where the continuum computes, and computed where the continuum is proved.** The
lattice memory law (R3.1) — the piece that reduces cleanly — is conditional on
D18/H-AD-G, an asymptotic-completeness hypothesis that is open on the full
chain; and the only lattice quantity that is *unconditionally* computed in the
kink model, `T(k)`, is computed in a regime (`Δ ≫ 1`, `≤3`-wall projection)
disjoint from the regime where the continuum comparison lives (`Δ → 1⁺`, wide
wall). A referee who accepts the reduction in §3.1 will immediately ask what is
actually being computed on the lattice that is not either assumed or restricted
to a projection, and the honest answer today is: the two-magnon soft slope
(R1), and nothing else in the memory corner.

---

## Q: the definitional audit (2026-08-30)

Sections 1–6 above ask whether the campaign's *results* reduce. A second
directive (TJO, 2026-08-30: *"I am suspicious of the definitions"*) asked the
prior question — whether the **definitions** denote the objects whose names they
borrow — and fixed the test bed: 3+1 compact Hamiltonian (Kogut–Susskind)
lattice QED, a regulator in which the Maxwell photon and the Weinberg pole
demonstrably exist. Four lanes were run, Q4 hostile and blind to Q1–Q3. They
concur on every overlapping item.

One-record rule: **the lane files hold the detail**, this is only the index.

| lane | file | question | verdict |
|---|---|---|---|
| Q1 | `theory/lanes/reduction/q1-gauss.md` | D3/D4/D10/(WI) vs the Gauss law and the asymptotic charge | (WI) **DOES** match the constant-profile Gauss telescope on `H_phys`, exactly at finite spacing; D3, D4, D10 **DO NOT** reduce as written |
| Q2 | `theory/lanes/reduction/q2-memory-defs.md` | do D13/D26/D27 discretize electromagnetic memory? | D26 is the *same* compact-U(1) coset theorem, transplanted from link flux to on-site matter charge; D13 and D27 are a **different object** — a charge-transport/interface ledger |
| Q3 | `theory/lanes/reduction/q3-soft-defs.md` | fixed-time insertions vs asymptotic soft legs | D24(b) **IS** the accepted LSZ-type definition; D29 is pre-asymptotic and coincides with it (zero remainder) only on `D29-HS-SEP`, differing at `O(k_s)=O(ε)` otherwise |
| Q4 | `theory/lanes/reduction/q4-adversarial-defs.md` | hostile correspondence hunt | as adjudicated at r1a: TWO fatal continuum-facing identification failures (`S_W`, D26+D27), four MAJORs, two minors; the D4-QED rat is WITHDRAWN as a category error (see amendment); every definition survives as internally exact lattice mathematics |

Adjudication: `theory/verdicts/reduction-defs-adjudication-r1.md` (bd `tns-1gf`),
including **amendment r1a (TJO ruling)**: the asymptotic-symmetry corner is
the accepted definitional SCHEME (boundary implementers modulo trivially
acting, charge algebra + extension), correctly instantiated on both theories;
the finite-`χ` spectral complaint tested the spin-chain algebra against a job
(being QED's edge algebra) no one assigned it, and the limit lives in the
THEORY, where the scheme commutes with it. The adjudication classifies N1–N5
as genuinely new, records the already-fenced items, and issues the action
list. **No claim status changed; none needed changing.**

### The nucleus that survives (Q1)

On the physical subspace, with `W_R(α)=exp(iα Σ_{x∈R} ρ_x)` the *matter-only*
regional rotation (not the local gauge transformation `Γ[ε]`, which is the
identity there):

    W_R(α) P_phys = Π_{ℓ∈∂R} e^{iα σ_Rℓ E_ℓ} P_phys,

with the same orientation as the campaign's two bond insertions. Weighted by a
profile, `Q^∂[ε] P = (Q^H[ε] + Q^∇[ε]) P`, and under the ordered limits
(`a→0`, then `L→∞`, then `R→∞` at fixed `u=t−R`, then `u→−∞`) these become
`Q^+_ε = Q^+_H + Q^+_S` — a **[PHYSICAL ARGUMENT]**, and the last arrow only
after the spacelike-to-null deformation. At finite spacing `Q^∇` is a *gradient*
term, not a soft-photon operator. Caveat that must travel with it: the
modulated matter rotation alone is **not** boundary-only when `dε ≠ 0`.

### The fatal identification failures (Q4, as amended at r1a)

1. **`S_W` / D24(d).** Source-dependent class, selected by conditions that
   substantially restate the desired factorization, with no proved microscopic
   member. `ML5-B` stays a correct conditional implication; it is not a
   nonvacuous continuum-style soft theorem, and raises the stakes of `tns-axg`.
2. **[WITHDRAWN at r1a] D4 as a QED boundary charge.** The original fatal
   grading was a category error: no campaign statement identified the
   spin-chain bond algebra with QED's edge algebra, and the definitional
   scheme of corner A instantiates correctly on both theories (the nucleus
   above). What survives is a scope note: the two theories' asymptotic
   algebras are non-isomorphic (state-level `PGL` kernel vs allowed/trivial
   quotient; virtual insertion vs boundary-link observable; two endpoints vs
   a function group on `S²`; finite spectrum vs the rotor's `[E,U]=U`) and
   must not be identified.
3. **D26+D27 as generic radiative memory.** A separated free Maxwell radiative
   sector can carry `∫du F_uz^(0) = ΔA_z ≠ 0` while its matter-charge TPM law is
   `δ_0`; replacing the observable by the field shift destroys (INT); photon
   number changes the charge and can break LR3 tightness; gravitational `ΔC_zz`
   is continuous. Missing bridge: a **reconstruction theorem** (charge ledger ↔
   field-side memory).

Majors: D13(a) charged-dressing masquerade (centring amendment owed); D13(c)'s
undefined leg subtraction (the recorded conserved-coordinate trap); D5 as
"particle"; D26 read as an asymptotic QED charge.

### Naming discipline (binding on the Letter and every external presentation)

Safe names: **collective-coordinate charge ledger**; **finite-window Fourier
response**; **compact-charge measurement statistics**; **conditional exact-band
scattering**. "Memory" is defensible in the **magnonics sense only** — §3.1's
clean `δx = −N_T/s → V_DW = −(ρ²/2)V_g` reduction is what licenses it. Without
the missing bridges: no generic radiative/gravitational memory language, and
no nonvacuous continuum-style soft theorem from `ML5-B`. Per amendment r1a,
"asymptotic symmetry" remains the correct, unrestricted name for corner A —
the only rule there is not to identify the spin-chain algebra with a gauge
theory's edge algebra, a claim never made.

### Owed

1. Reconstruction theorem (charge ledger ↔ bond/potential-side memory), P1.
2. An exhibited member of `S_W` (`tns-axg`) — now framing-critical, not
   nice-to-have.
3. D13(a) centring amendment, P2, in lockstep with labbook shard 5.

Absorbed into the labbook at `labbook/sections/18_continuum_reduction.tex`,
subsection "The definitional audit".
