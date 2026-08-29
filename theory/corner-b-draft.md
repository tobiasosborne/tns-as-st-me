<!-- ROLE: Corner-B theory shard, repaired after L6 r1 FAIL.
     Definitions live only in definitions.md D13--D18; Bd labels below are
     historical cross-references, not active definitions. -->

# Corner B (draft) — the memory corner

**Status: repaired after `verdicts/corpus-r2.md`; adjudicated promotions
applied.**
Four stale citations tabulated in [`corner-a-pitfalls.md`](corner-a-pitfalls.md)
Flag 6 and in [`verdicts/oracle-bethe-r2.md`](verdicts/oracle-bethe-r2.md)
residue 4 have been repaired in place, each marked `(Reconciled at freeze …)`:
§0 item 4, §7 B3(i) and §7 B3(iv) no longer use a fixed `𝒜`-orbit point or the
`G_diag`-invariant label of `𝒜 = (G_L×G_R)/G_diag` (both cited `A2-orbit-r1`,
**REFUTED**; and in this shard's `χ=1` unbroken-`U(1)` setting A1 gives
`N_α = G`, so the endpoint-state orbit is a single point); §5.3 and §10 now
quote `O7` in its r2 form `δ_phys = 2 sgn(v_h−v_s)k_s + …`, with `2` flagged as
the D8 specialisation.  `𝒜`-data has been replaced by "asymptotic data"
throughout.  **D13--D18 are the sole definitions (L4).**  The old `Bd` labels
remain only to identify historical passages.  D18 now means the coherent
AD1--AD4 wave-operator/local-decay hypothesis; its former norm-mixture form is
superseded by the coherent-superposition counterexample recorded there.
[`memory-quantization.md`](memory-quantization.md) gives the current Lamport
argument.  Its projected Fano reduction is conditional on the all-volume
enumeration/isomorphism Mq-E, and the full-chain lift remains open (bd
`tns-d51`).

## 0. Summary of what this shard establishes

The 1D lattice memory observable is the permanent displacement `δx` of a
domain wall (kink) left behind by a magnon wavepacket that has traversed it.
This shard does four things.

1. It compares the three D13 representations of `δx` (dynamical, spectral,
   and windowed spatial), with explicit domains and limit orders.
2. It derives — conditional on D18 — the charge-bookkeeping law

   \[
   \boxed{\;\delta x \;=\; -\,\frac{1}{s}\,\langle N_T\rangle\;}
   \qquad\text{(spin-}s\text{ chain; }s=\tfrac12:\ \delta x=-2\langle N_T\rangle)
   \]

   where `N_T` is the transmitted magnon number.  The memory is
   **channel-quantised with spectrum `{0,-1/s}`**: a single magnon moves the
   wall by `-1/s` lattice sites if it transmits and by `0` if it reflects.
   The expectation `-⟨N_T⟩/s` is continuous.  The
   coefficient is fixed by `U(1)` charge conservation alone: it does not
   depend on `k`, on `Δ`, on the packet shape, or on any scattering phase.
3. Conditional on the all-volume sector reduction Mq-E, it reduces the
   spin-`1/2` `≤3`-wall kink–magnon problem to a single-channel Fano graph
   with transmission amplitude
   `t(k) = [1 + i J²/(4ω(k)v(k))]^{-1}`, hence `T(k)=|t|²` and a **memory
   Adler zero** `δx(k) ≈ −(2/s)\,·8(Δ−1)²k²` as `k→0`.
4. It records the `B ⇒ A` edge (claim **B3**) at PROVED status.  The surviving
   event statement is `2s·δx+(q_out-q_in)=0`, with explicit leg subtraction.

The headline honest finding is negative and important:

> **Conjecture M of the brief, read literally ("`δx` equals the zero-frequency
> limit of the soft factor `S` summed over the event"), is false in the
> easy-axis XXZ chain.**  The soft factor controls the *magnon's* Wigner
> shift and the transmission probability; it does *not* set the wall
> displacement, whose quantum `1/s` is a charge, not a phase.  The correct
> lattice Braginsky–Thorne statement is the **charge-flux relation** of
> §6, in which the soft data enters only through `T(k)`.

---

## 1. Setting, conventions, and the exact kink family

### 1.1 Model (M2)

Use the spin-`1/2`, `J>0`, `Δ>1` XXZ model, symmetry, vacua, dispersion, and
gap of D16.  D16 is the sole definition; this shard derives consequences.

### 1.2 Consequences for the D16 kink Hamiltonian and product family

**K1 (frustration-freeness; PROVED per corpus-r2 adjudication).  ASSUME** D16.  **PROVE**
`h^{\rm kink}_{x,x+1} ⪰ 0`, with
`spec = {0,0,0,JΔ}`; its kernel is
`span{|↑↑⟩, |↓↓⟩, |↑↓⟩+q^{-1}|↓↑⟩}`, with `q` fixed in D16.

**⟨1⟩1.** In the basis `(|↑↓⟩,|↓↑⟩)` the nontrivial block is
`[[Δ/2+C, −1/2],[−1/2, Δ/2−C]]` with `C=\tfrac12\sqrt{Δ²−1}`; its determinant
is zero and its trace is `Δ>0`.
*Justification:* D16 and named two-site computation **K1-2x2**.

**⟨1⟩2.** The other two basis vectors have zero diagonal entries; hence the
spectrum and kernel are the ones stated.
*Justification:* D16, ⟨1⟩1, and direct diagonalisation of **K1-2x2**.

**⟨1⟩3. QED.** □

**K2 (exact kink product states; PROVED per corpus-r2 adjudication).  ASSUME** D16 and K1.
**PROVE** that every D16 vector `|K(z)⟩`, `z∈ℂ\{0}`, lies in the kernel of
every `h^{\rm kink}_{x,x+1}`.

**⟨1⟩1.** Neighboring down-spin coefficients obey `b=zq^{n+1}=qa`, so each
two-site factor lies in K1's kernel.
*Justification:* D16 and claim K1.

**⟨1⟩2.** Therefore every bond term annihilates the product vector.
*Justification:* ⟨1⟩1 and D16's product construction.  **⟨1⟩3. QED.** □

**K3 (boundary-field invisibility; PROVED per corpus-r2 adjudication).  ASSUME** D16.
**PROVE** that `H_{\rm kink}` and `H_{\rm XXZ}` generate the same derivation
on `𝔄`.

**⟨1⟩1.** For
`O ∈ 𝔄_Λ`, `Σ_x [S^z_x − S^z_{x+1}, O]` telescopes to
`[S^z_{-M} − S^z_{M+1}, O] = 0` for any `M` with `Λ ⊂ (−M, M)`.  The field term
shifts the energy of each superselection sector by the constant
`\tfrac{J}{2}\sqrt{Δ²−1}\,(s_α − s_β)` and nothing else.
*Justification:* D10(a)'s finite-support register and D16's telescoping field.

**⟨1⟩2. QED.** □

*Consequence.* Every dynamical statement below is a statement about the pure
XXZ chain; `H_{\rm kink}` is used only to *normalise* the kink to zero energy
and thereby to motivate the flat-band Conjecture K4.

**Conjecture K4 (thermodynamic flatness/uniqueness; not a theorem).** Let
`𝒮_M` be the sector of fixed regularised magnetisation `M`
inside `𝒦_{↑↓}`.  Then `𝒮_M` contains exactly one zero-energy state of
`H_{\rm kink}`, and these states are degenerate across all `M`.  Hence the
kink has *no* dispersion, *no* effective mass, and *no* recoil velocity: its
translation modulus is rigidly locked to the conserved `U(1)` charge.

*Finite-volume evidence only.* Frustration-freeness (K1) gives `E ≥ 0`; K2 gives states of energy
`0`; uniqueness per sector verified by exact diagonalisation on `N = 12`,
`Δ = 3`, every `m = 0,…,12`: `E₀ = 0` to `10^{-13}`, `E₁ = 2.03407417` in every
sector (magnon gap `J(Δ−1)=2` plus finite-`N` boundary shift).  A proof of
uniqueness in the thermodynamic limit is an interface requirement (**R5**).
No no-recoil, unique-torsor, or all-`Δ` dynamical statement may cite K4 as
proved.

**Remark (why this matters).** On the lattice, translation is not a symmetry
*within* a magnetisation sector — translating a kink changes `S^z_{\rm reg}`.
Momentum conservation for the wall is therefore traded for charge
conservation.  Under D18, this gives channel-quantised displacement.  The
continuum (Lan–Xiao, arXiv:2107.05401) memory differs: there the wall
is inertial, its modulus is not locked to any charge, and the displacement
`ΔX = −Gm/v₀²` is a continuous function of packet intensity.

### 1.3 Function-space discipline (Giulini; active source D17)

`𝒦_{αβ}` is D9(a); its `ℓ¹` refinement and first-moment clause are D17.

`𝒦^{(1)}` is preserved by the dynamics on finite time intervals
(Lieb–Robinson).  It is *not* preserved by the `k → 0` limit: a plane-wave
magnon is not `ℓ¹`.  Every soft statement below must therefore fix the packet
first and take `k → 0` afterwards; the two limits do not commute (§9, P7).

### 1.4 Historical symbol crosswalk (active source: notation.md)

| symbol | meaning | active source |
|---|---|---|
| `q` | XXZ deformation parameter `Δ−√(Δ²−1)` | D16 |
| `x_0`, `φ` | kink centre and conjugate `U(1)` phase | D16 |
| `𝔛_W` | windowed wall-position observable | D13(a) |
| `N_T`, `N_R` | transmitted / reflected magnon number | D14 |
| `t(k)`, `r(k)`, `T(k)`, `δ_t(k)` | kink–magnon transmission/reflection data | D15 |
| `𝒦^{(1)}_{αβ}` | `ℓ¹` kink class | D17 |

---

## 2. D13 memory representations and the exact flux identity

D13(a)--(c) are the sole definitions.  D13(a) is the finite-window local
observable, D13(b) its spectral/DC dress, and D13(c) the first-moment dress
whose leg content must be subtracted using D18.  Their domains and orders of
limits are not restated here.

**Why D13(a) is the selected observable.** By the continuity equation D10(b),
\[
\frac{d}{dt}\,\varrho_t(\mathfrak X_W)
 =\frac{1}{2s}\Big[\varrho_t\big(j_{a-1|a}\big)-\varrho_t\big(j_{b|b+1}\big)\Big],
\tag{2.1}
\]
so `𝔛_W` changes *only* through the two **boundary bonds**, and
\[
\delta x^{\rm sp}=\frac{1}{2s}\int_{t_i}^{t_f}\!dt\;
\Big[\varrho_t(j_{a-1|a})-\varrho_t(j_{b|b+1})\Big]
=\frac{1}{2s}\Big[\tilde\jmath_{a-1|a}(0)-\tilde\jmath_{b|b+1}(0)\Big].
\tag{2.2}
\]
The memory is exactly the **DC component of the physical boundary current**.
Nothing in D10(d) identifies that current with the virtual bond potential
`𝒥_b`: D10(d) instead writes the *vacuum charge density* as a difference of
virtual insertions, in a different register.  The former claim that (2.2) is
a difference of virtual/bond data is withdrawn.  Extending the virtual
potential reading to a kink-sector dynamical theorem remains future work and
is not part of Mq-flux.

---

## 3. Which definitions agree, and where they part company

Write `P` for the equilibrium kink profile, `σ_k` for the packet momentum
width, `σ_x ≈ 1/σ_k` for its spatial width, `L := b − a`, `ξ_c` the kink width
`≈ 1/\log(1/q)`.

**(a) D13(b) = D13(a) identically.**  `Σ_{x∈W}D(x) = ϱ_{t_f}(2s\,𝔛_W) −
ϱ_{t_i}(2s\,𝔛_W)` by definition; the only content is the sum rule.  They are
the same observable in two Fourier dresses.  D13(b) is useful for reporting;
D13(a) is useful for proving.

**(b) D13(c) = D13(a) + (leg content) − (drift).**  Explicitly,
\[
X_1(t)
 =\underbrace{x_{\rm wall}(t)}_{\text{D13(a) in the }L\to\infty\text{ limit}}
 +\underbrace{\frac{1}{2s}\sum_{\rm legs}q_{\rm leg}(t)}_{\text{magnon charge}},
\qquad q_{\rm leg}=-1\ (\text{left}),\ +1\ (\text{right}),
\]
because `X_1` is the `W → ℤ` regularisation of `𝔛_W` and *is* the regularised
total magnetisation, which is **exactly conserved**.  Consequently:

* If one uses D13(c) with all legs included, `δx^{\rm dyn} ≡ 0` — the naive
  "asymptotic trajectory of the magnetisation centroid" has *no* memory at
  all.  This is a trap and must be said out loud.
* D13(c) becomes equal to D13(a) only after subtracting the asymptotic leg charges,
  i.e. only after invoking **H-AD** (§6).  D13(a) does the subtraction
  geometrically (by windowing) and needs no such hypothesis.

**(c) Finite `N`.** D13(a) is exact at finite `N` provided `W` is interior.  D13(c)
and D13(b) require `N → ∞` first (`X_1` and `D(x)` involve `t → ±∞`), and on a
ring they are meaningless (D1 Remark).

**(d) Finite wavepacket width.** Under D18, all three representations return
`−⟨N_T⟩/s` with `⟨N_T⟩ = ∫dk\,|φ(k)|²T(k)` — a *packet average of `T`*, not
`T(⟨k⟩)`.  The systematic error of reading `T(⟨k⟩)` off `δx` is
`\tfrac12 T''(\langle k\rangle)\sigma_k^2`, which is largest exactly in the
soft region where `T` bends (§9, P3).  D13(a) additionally has a
`C_{λ̃}λ̃^{d_W}` tail error for every `λ̃∈(λ_E,1)` and an `O(ε)` error from
residual packet weight inside `W`.

**(e) Drift.** Conjecture K4 would give `V_± = 0`; this has not been proved in
the thermodynamic dynamics.  If `U(1)` is broken (transverse field, easy-plane anisotropy,
DMI), the wall acquires a finite mass, `V_+ ≠ 0` whenever there is reflection,
and Bd1's intercept becomes ambiguous by `O(V_+ · T_{\rm obs})`.  In that
regime D13(a) also ceases to be quantised and the Lan–Xiao mechanism
(`ΔX ∝ −Gm/v_0²`, continuous in the magnon number) takes over.  **The
dichotomy "charge-locked ⇒ quantised memory / charge-free ⇒ continuous
memory" is the sharpest physical content of this shard.**

**(f) Distributional content.** Under D18, the asymptotic two-channel
*displacement operator* is `ΔX=-(1/s)N_T`.  The out-state is a coherent
superposition, so
\[
\langle\Delta X\rangle=-\tfrac1s\langle N_T\rangle,\qquad
\mathrm{Var}(\Delta X)=\tfrac1{s^2}\,\langle N_T\rangle(1-\langle N_T\rangle)
\;\;(=4T R \text{ at } s=\tfrac12).
\]
Identifying this with the one-time `Var(𝔛_W)` additionally requires a sharp
initial wall and a two-time measurement convention; neither is implicit.
D13(c), phrased as "the trajectory", presupposes one classical worldline and is
only meaningful post-selected on a channel.  The variance is the observable
that distinguishes channel quantisation from a smooth displacement,
and it is measurable (§9, P4).

**D13(a) remains the selected observable.**  It is an element of `𝔄_loc` (exists
without any asymptotic hypothesis); it is finite-`N` and finite-`t`
computable; (2.2) makes it a physical-boundary-current quantity.  D13(b) is
its Fourier dress and D13(c) reduces to it after D18 leg subtraction.

---

## 4. Historical definition crosswalk (do not cite the `Bd` labels)

| historical label | sole active source |
|---|---|
| Bd1--Bd3 | D13 |
| Bd4 | D14 |
| Bd5 | D15 |
| Bd6 | D16 |
| Bd7 | D17 |
| former norm-mixture H-AD | superseded; use D18(AD1--AD4) |

---

## 5. The kink–magnon scattering problem in the XXZ chain

This is the dynamical model computation.  Mq-E (`theory/mq-e.md`) proves the
all-volume sector enumeration/isomorphism for the projected incoming
component, so the Fano solution below is exact on that component.

### 5.1 The sector and its graph

Fix `𝒦_{↑↓}` and the magnetisation sector containing (kink at bond `m`) +
(one magnon).  In the `S^z` product basis, configurations are labelled by
domain-wall positions.  The XY term flips the wall indicators at bonds `n−1`
and `n+1` simultaneously, so it either creates two walls, destroys two, or
moves one wall by two sites.  Consequently:

**Theorem (Mq-E, proved).**  `theory/mq-e.md` §§1--6 proves, for every
admissible frozen-boundary volume and at infinite volume, that the connected
incoming `≤3`-wall component is exactly the left/right channel tails (magnon
at `x ≤ m−1` with wall at `m`; hole at `y ≥ m−1` with wall at `m−2`), one
shared junction, and one pure-kink side state `JΔ` below, with uniform Ising
energy `3JΔ/2` and every hopping `−J/2` — the Fano graph, with an explicit
all-volume unitary and local-observable map.

*Falsifier example (retained as a check, not as the basis of the claim).*
Direct enumeration, `N = 14`, wall at bond `6`: component of size `12` = 5
magnon + 6 hole + 1 kink states; degree histogram `{1:3, 2:8, 3:1}`; the
degree-3 vertex is the junction.  The `−2` is visible: wall at `m` incoming,
`m − 2` outgoing, with no free parameter.

### 5.2 Conditional Fano solution on the Mq-E graph

By Mq-E, the effective one-body problem is a *uniform* tight-binding chain
(hopping `−J/2`, uniform on-site energy) with a single **side-coupled level**
— the pure kink — attached at the junction with amplitude `−J/2` and detuning
`ω(k) = J(Δ − \cos k)`.  Eliminating the side level gives an energy-dependent
on-site potential at the junction,
\[
U(k)=\frac{(J/2)^2}{\omega(k)}=\frac{J^2}{4\,\omega(k)} .
\]
For a single-site potential `U` on a chain with hopping `−τ` and
`E = −2τ\cos k`, matching `ψ_n = e^{ikn}+re^{-ikn}` (`n ≤ 0`), `ψ_n = te^{ikn}`
(`n ≥ 0`) at the impurity gives `−2i\tau r\sin k + Ut = 0`, `t = 1+r`, hence
with `2τ\sin k = J\sin k = v(k)`:

\[
\boxed{\;t(k)=\Big[1+\frac{iJ^2}{4\,\omega(k)\,v(k)}\Big]^{-1},\qquad
r(k)=-\frac{iJ^2}{4\omega v}\,t(k),\qquad
T(k)=\Big[1+\Big(\frac{J^2}{4\omega(k)v(k)}\Big)^{2}\Big]^{-1}\;}
\tag{5.1}
\]
\[
\delta_t(k)=-\arctan\frac{J^{2}}{4\,\omega(k)\,v(k)} .
\tag{5.2}
\]

**Limits.**
* *Large `Δ` (Ising):* `J²/(4ωv) ≈ 1/(4Δ\sin k)`, so
  `R(k) ≈ 1/(16Δ²\sin^2 k)`: the wall is **transparent** to `O(1/Δ²)`, the
  lattice counterpart of the reflectionless continuum domain wall.
* *Soft limit `k → 0` at fixed `Δ`:* `v → 0`, `ω → J(Δ−1)`, hence
  \[
  \boxed{\,T(k)=16(\Delta-1)^2k^2+O(k^4),\qquad
  R(k)=1-16(\Delta-1)^2k^2+O(k^4)\,}
  \tag{5.3}
  \]
  — **total reflection of a soft magnon**, with a quadratic zero.  Equivalently
  in the frequency variable, with `ω−ω_{\rm gap} = J(1−\cos k) ≈ Jk²/2`,
  `T ≈ 32(Δ−1)^2(ω−ω_{\rm gap})/J`: *linear in the excess energy above the gap*.
  The crossover momentum is `k_* = 1/(4(Δ−1))`.

**Scope.** (5.1)–(5.3) are exact for the displayed Fano graph, because Mq-E
identifies that graph with the all-volume incoming component
(`theory/mq-e.md`).  They are not exact for the unprojected `H_{\rm XXZ}` because of
leakage into `≥5`-wall configurations.  That leakage is measured (full-sector ED, `N = 22`,
`k = π/2`, `σ = 2.6`, `0 ≤ Jt ≤ 13`) to be `P(≥5\text{ walls}) ≈`
`8·10^{-3}` at `Δ = 8`, `3·10^{-2}` at `Δ = 4`, `1·10^{-1}` at `Δ = 2`,
i.e. `O(Δ^{-2})`.  **It affects `T(k)`; it does not affect the memory law of
§6, which is a conservation law.**

### 5.3 Where the Wigner/soft-phase reading actually lives

`d\delta_t/dk` is the spatial shift of the **transmitted magnon** (a
Wigner–Eisenbud delay converted to a displacement).  It is a smooth,
non-quantised function of `k` and `Δ`.  It is *not* the wall displacement.
The soft phase-slope reading of the magnon–magnon oracle is the analogous
magnon-side statement in M1: **on D8's half-zone** (`k_h ∈ (0,π)`, so
`sgn(v_h−v_s) = +1`) `O7` reduces to `δ_phys = 2k_s + (|v_h|/ω_h)k_s² + R_δ`,
i.e. `dδ_phys/dk_s|_0 = 2`.  *(Reconciled at freeze 2026-08-26: `O7` was
re-stated in oracle round r2 as `δ_phys = 2 sgn(v_h−v_s)k_s + …`, and the
phrase "hard-independent linear coefficient" was removed; the `2` here is the
D8 specialisation, not the general coefficient — `verdicts/oracle-bethe-r2.md`
residue 4.)*  §10 records the conjecture that these two `2`'s have a common
origin; it is not proved here.

---

## 6. The `C ⇒ B` edge: the memory law (Lamport outline)

### Statement

> **M′ (conditional lattice memory implication; PROVED conditional on D18 per
> corpus-r2 adjudication).**
>
> **ASSUME.**
> (A1) D16's spin-`1/2` easy-axis XXZ dynamics, with conserved `U(1)` charge;
> `Ω_vac = {α,β}` with densities `s_α=+s`, `s_β=-s` (`s=1/2` here).
> (A2) `ϱ_t` lies in `𝒦^{(1)}_{αβ}` (D17) and is the selected scattering
> vector of D18.
> (A3) **(H-AD)** in the coherent AD1--AD4 sense of D18, with incoming charge
> `q_in=-1`, reflected charge `q_out=-1`, and transmitted charge `q_out=+1`.
> (A4) The kink core is padded from both window edges by distance `d_W`.
>
> **PROVE.**
> \[
> \delta x^{\rm sp}
> =\varrho_{t_f}(\mathfrak X_W)-\varrho_{t_i}(\mathfrak X_W)
> =-\frac{1}{s}\,\langle N_T\rangle+O(C_{\tilde\lambda}\tilde\lambda^{d_W}),
> \qquad
> \langle N_T\rangle=\int_{-\pi}^{\pi}\!\frac{dk}{2\pi}\,|\varphi(k)|^2\,T(k).
> \]

### Proof outline

**⟨1⟩1.** `𝔛_W ∈ 𝔄_loc` and
`\dot{\mathfrak X}_W = \tfrac{1}{2s}(j_{a-1|a}-j_{b|b+1})`.
*Justification:* D13(a), D10(a)–(b) with `ξ = ` the `U(1)` generator; the bulk
terms of `Σ_{x∈W}\dot S^z_x` telescope.

**⟨1⟩2.** Hence `2s\,\delta x^{\rm sp} = Q_W(t_f) − Q_W(t_i)`, with
`Q_W := Σ_{x∈W}S^z_x`, and this equals the DC weight of the boundary current,
Eq. (2.2).
*Justification:* ⟨1⟩1 and the fundamental theorem of calculus.

**⟨1⟩3.** Under D18(AD3), `Q_W(t) = 2s\,x_{\rm wall}(t) + \text{const}(W)` at
the separated in/out limits up to `C_{λ̃}λ̃^{d_W}` for every
`λ̃∈(λ_E,1)`.
*Justification:* for a configuration with the wall at bond `m` and no magnon
in `W`, `Σ_{x=a}^{b}(S^z_x+s) = 2s(m−a+1)`; kink-core dressing contributes the
Jordan-safe transfer tail by D1(c) and D13(a).

**⟨1⟩4. PROVE.** Charge bookkeeping over the event.
> **⟨2⟩1.** `S^z_{\rm reg}` is exactly conserved.
> *Justification:* (A1); `[H_{\rm XXZ}, S^z_x]` is a lattice divergence
> (D10(b)) and the sum telescopes on `𝒦^{(1)}`.
> **⟨2⟩2.** In the *in* state the total is
> `2s\,m_i + q_{\rm in}` with `q_{\rm in} = −1` (one magnon on the `α` vacuum).
> *Justification:* D18(AD3) and D14.
> **⟨2⟩3.** In the *out* state the total is `2s\,m_{\rm out} + q_{\rm out}`
> with `q_{\rm out} = +1` on the transmitted branch and `−1` on the reflected
> branch.
> *Justification:* D18(AD3); a magnon on the `β = ↓` vacuum has `ΔS^z = +1`.
> **⟨2⟩4.** Equating: on the transmitted branch
> `m_{\rm out} − m_i = −2/(2s) = −1/s`; on the reflected branch `0`.
> *Justification:* ⟨2⟩1–⟨2⟩3.
> **⟨2⟩5. QED.**

**⟨1⟩5.** D18(AD2) packages the channel weights into the projection
`N_T`; conjugating the branch displacements gives
`ΔX=-(1/s)N_T`, hence `δx=-⟨N_T⟩/s` and
`Var(ΔX)=s^{-2}⟨N_T⟩(1-⟨N_T⟩)`.
*Justification:* ⟨1⟩3--⟨1⟩4, D18(AD2), and `N_T²=N_T`.  This is not a claim
about one-time `Var(𝔛_W)` without a sharp initial state/two-time protocol.

**⟨1⟩6. QED.**

### Status of each ingredient (honest)

| ingredient | status |
|---|---|
| ⟨1⟩1, ⟨1⟩2 (flux form, Eq. 2.2) | **PROVED per corpus-r2 adjudication.** |
| ⟨1⟩3 (window ⇒ wall position) | **PROVED conditional on D18**, with the D1(c) `C_{λ̃}λ̃^{d_W}` error. |
| ⟨1⟩4 (charge bookkeeping) | **PROVED conditional on D18 per corpus-r2 adjudication.** |
| **H-AD** | **CONJECTURE** for the full XXZ chain.  D18 is the sole definition. |
| `T(k)` from (5.1) | **PROVED for the projected incoming component by Mq-E** (`theory/mq-e.md`; blitz-mq-e-r1); `O(Δ^{-2})` leakage measured beyond the projection. |
| `δx = ` DC limit of the *soft factor* | **REFUTED as stated** (see §10). |

### What the soft theorem is actually needed for

The conditional M′ implication fixes the channel displacement with no
scattering-phase input.
The soft data enter in exactly one place: the value of `T(k)`, and in
particular its `k → 0` behaviour.  The `C ⇒ B` edge is therefore

\[
\underbrace{\text{Corner C}}_{\text{soft behaviour of }t(k)}
\;\longrightarrow\;
\underbrace{T(k)\to 0 \text{ as } k\to0}_{\text{memory Adler zero}}
\;\longrightarrow\;
\underbrace{\delta x(k)=-\tfrac1s T(k)}_{\text{Theorem M}'} .
\]

Equation (5.3) supplies the middle step *in the easy-axis projection*; what a
genuine Corner-C theorem must supply is that the quadratic zero of `T` and its
coefficient `16(Δ−1)²` are **universal** — functions of the kink's asymptotic data
(vacuum pair, `U(1)` charge, gap) only, not of the microscopic `B`-tensor.
That universality is *not* established here and is the real C ⇒ B obligation.

---

## 7. The `B ⇒ A` edge (claim **B3**)

**CLAIM B3 (PROVED per corpus-r2 adjudication, with N9 density leaf below).**
Assume a translation-invariant finite-range
dynamics whose two asymptotic vacua are stationary, a state initially in
`𝒦_{αβ}` (D9(a)), and, for the event-specific charge statement, D18 with a
window `W=[a,b]`.  Then the intended surviving clauses are:

1. finite-time dynamics fixes the vacuum-pair label `(α,β)`; and
2. after subtracting the kink charge and fixing the cut geometry, total-charge
   conservation gives `2s·δx+(q_out-q_in)=0`.

The former raw half-line formula
`δx=(2s)^{-1}Δ𝔮_c^R=-(2s)^{-1}Δ𝔮_c^L` is **REFUTED**.  In the transmitted
spin-`1/2` channel it predicts `+1` (or `-1`) while D18 charge bookkeeping
gives `-2`.

**⟨1⟩1. PROVE (sector rigidity at finite time).**

**⟨2⟩1.**  Let `α_t` be the finite-range Heisenberg automorphism.  For every
local pair `D,O`, fixed `t`, and `ε>0`, Lieb--Robinson quasi-locality supplies
local observables `D_ε,O_ε`, independent of `n`, such that
`||α_t(D)-D_ε||<ε` and `||α_t(O)-O_ε||<ε`.  Translation covariance then gives
`||α_t(τ_n(O))-τ_n(O_ε)||<ε`.
*Justification:* named Lieb--Robinson quasi-locality theorem for D10(a)'s
finite-range dynamics.

**⟨2⟩2.**  Translation covariance gives
`α_t(τ_n(O))=τ_n(α_t(O))`, and stationarity of the vacua gives
`ω_{α/β}(α_t(O))=ω_{α/β}(O)`.
*Justification:* the assumptions of B3 and D9(a)'s vacuum functionals.

**⟨2⟩3.**  Apply D9(a) to the local pair `D_ε,O_ε`.  The state norm and
submultiplicativity give the explicit two-factor estimate

`|ϱ(α_t(D)α_t(τ_n(O)))-ϱ(D_ετ_n(O_ε))|
 ≤ ε||O||+(||D||+ε)ε`,

with analogous one-factor bounds for `ϱ(α_t(D))` and
`ω_{α/β}(α_t(O))`.  First taking `n→∓∞` in the local factorised limit and then
`ε↓0`, using stationarity from ⟨2⟩2, reproduces the same left/right
functionals `ω_α,ω_β`.
*Justification:* D9(a), norm density/quasi-locality, ⟨2⟩1, and ⟨2⟩2.

**⟨2⟩4.**  Hence `ϱ_t∈𝒦_{αβ}` for every finite `t`; the argument fixes the
labels rather than merely preserving disjointness.
*Justification:* D9(a) and ⟨2⟩3.  **⟨2⟩5. QED.**

**⟨1⟩2. PROVE (event-specific charge bookkeeping with explicit cut).**

**⟨2⟩1.**  Fix `c∈W` and take the D18 in/out limits with the kink localised
in `W` and every propagating leg outside `W`.  Define `q_in,q_out` as the
charges of those separated legs relative to the vacuum on which each leg
sits.  These are **leg-subtracted** charges, not raw half-line charges.
*Justification:* D18(AD3)--(AD4) and D14.

**⟨2⟩2.**  A kink at coordinate `m` contributes `2s(m-c)` to the regularised
total charge, so the in/out totals are
`2s(m_i-c)+q_in` and `2s(m_f-c)+q_out`.
*Justification:* D13(a) and the direct charge sum in M-quant ⟨1⟩2.

**⟨2⟩3.**  D10(b) conserves the regularised total charge.  Subtracting the two
expressions in ⟨2⟩2 gives

`2s·δx+(q_out-q_in)=0`.

*Justification:* D10(b), D13(a), and ⟨2⟩2.

**⟨2⟩4.**  Reflection has `q_out=q_in=-1` and therefore `δx=0`;
transmission has `(q_in,q_out)=(-1,+1)` and therefore `δx=-1/s`.
*Justification:* D18(AD3) and ⟨2⟩3.  **⟨2⟩5. QED.**

**⟨1⟩3. QED.** □

**Honest residue.**  The proof above is PROVED per corpus-r2 adjudication after
the N9 density leaf was supplied.  The proposed `ℤ`-torsor/unique-flat-kink statement depends on
Conjecture K4/R5 and is therefore a `CONJECTURE`, not a B3 consequence.  The
vacuum-pair label of D9(d) is rigid under ⟨1⟩1 and is read off, not shifted;
`δx` records the leg-charge transfer of ⟨1⟩2 within that fixed label.  It is
not an element of the refuted `A2-orbit-r1` object and is not identified with
virtual bond data.

---

## 8. Interface requirements (what Corner A / `definitions.md` must supply)

| id | requirement | needed for |
|---|---|---|
| **R1** | Optional future theorem extending D10(d)'s virtual potential to a broken kink sector.  It is **not** used by Mq-flux or repaired B3. | future virtual/bond interpretation only |
| **R2** | D17 now supplies the `ℓ¹` refinement; B3 ⟨1⟩1 states the finite-time Lieb--Robinson label argument. | PROVED per corpus-r2 after N9 density sweep |
| **R3** | Optional future kink-sector half-line implementation theorem.  Raw half-line charge is **not** used as memory. | future virtual interpretation only |
| **R4** | Prove D18 for the full spin-`1/2` XXZ chain and prove the projected all-volume enumeration/isomorphism Mq-E before invoking the Fano spectral argument. | M′, Mq-AD3; bd `tns-d51` |
| **R5** | A thermodynamic-limit proof of Conjecture K4 (one zero-energy kink state per magnetisation sector; exact flatness). | torsor/no-drift conjectures |
| **R6** | Connect D5(a)'s kink ansatz to D13(a) through mixed-transfer contractions.  This would make `δx` MPS-native but would still not identify physical current with `𝒥_b`. | MPS-native formulation |
| **R7** | A (WI)-form identity for `U_{[c,∞)}(e^{iθS^z})` acting on a kink state: what the half-infinite `U(1)` string does to `(x_0,φ)` of Lemma K2. Expected: it shifts `φ`, not `x_0` — which is why the *soft* (`k=0`) magnon produces no displacement. | The `k→0` end of §6, P7 |
| **R8** | A definition of lattice momentum for the kink+magnon state and of "recoil", to state P5 sharply. Note translation is not a symmetry within a magnetisation sector (§1.2 Remark), so this needs care. | P5 |
| **R9** | D16 fixes the `Δ=J_z/J_⊥` convention. | repaired |

---

## 9. Predictions for the XXZ numerics agent

Conventions: `H_{\rm XXZ}` of §1.1 with `J = 1`, `Δ > 1`, `s = 1/2`; initial
state = kink at bond `m_i` plus a Gaussian magnon packet
`φ_x ∝ e^{ik_0x}e^{-(x-x_0)^2/σ^2}` (the arXiv:2012.07243 convention), `k_0 ∈
(0,π)`, launched from the `↑` side.  Window `W = [m_i − L, m_i + L]` with
core-to-edge padding `d_W` chosen so the D1(c) bound
`C_{λ̃}λ̃^{d_W}` is below tolerance.  Observables: `𝔛_W` (D13(a)), `N_T`,
`N_R` (D14).  All tolerances are
for converged MPS (`χ` chosen so the truncation error per step `< 10^{-10}`).

**P1 — the ratio test (SHARPEST).**
\[
\boxed{\;\frac{\varrho_{t_f}(\mathfrak X_W)-\varrho_{t_i}(\mathfrak X_W)}{N_T(t_f)}
= -\frac1s = -2\;}
\]
*independently of* `k_0`, `σ`, `Δ`, `m_i`, and of `R(k)`.  Tolerance: the ratio
must equal `−2` to `1·10^{-3}` once `N_W(t_f) < 10^{-4}` (packet clear of the
window).  A deviation larger than that at converged `χ` falsifies H-AD or the
identification of the leg charges — not the continuity equation.
*Reference values from the finite Fano-graph simulation (the Mq-E graph model,
`N=2200`, `σ=40`, packet travelling `620` sites):*

| `Δ` | `k_0` | `N_T` | `δx` | `δx/(-2N_T)` |
|---|---|---|---|---|
| 8 | `π/2` | 0.999024 | −1.998048 | 1.0000000 |
| 4 | `π/2` | 0.996106 | −1.992212 | 1.0000000 |
| 4 | 0.35 | 0.945564 | −1.891129 | 1.0000000 |
| 2 | 0.25 | 0.507536 | −1.015083 | 1.0000100 |
| 8 | 0.15 | 0.926504 | −1.853658 | 1.0003510 |

**P2 — Adler zero of the memory.** For `k_0 ≪ k_* = 1/(4(Δ−1))`,
\[
\delta x(k_0) = -\frac{2}{s}\,8(\Delta-1)^2k_0^2\big[1+O(k_0^2)+O(\Delta^{-2})\big]
\;\;\Big(s=\tfrac12:\ \delta x \simeq -32(\Delta-1)^2k_0^2\Big).
\]
Test: log–log fit of `|δx|` vs `k_0` over `k_0 ∈ [0.03, 0.2]` at `Δ = 2` and
`Δ = 4` must give slope `2.00 ± 0.05` and prefactor `32(Δ−1)²` to `±15 %`
(the tolerance absorbs the `O(Δ^{-2})` leakage and `O(σ_k²)` packet averaging).
Equivalent frequency form: `|δx| ≃ 64(Δ−1)²(ω−ω_{\rm gap})/J`, *linear in the
excess energy above the gap*.

**P3 — the full transmission curve.** `N_T(k_0)` must match
`∫ dk\,|φ(k)|²T(k)` with `T` from (5.1), to `2 %` at `Δ ≥ 4` and `10 %` at
`Δ = 2`.  Do **not** compare to `T(k_0)` unless `σ_k^2 T''(k_0) ≪ T(k_0)`;
in the soft region the packet average is the leading systematic.

**P4 — channel quantisation (the discriminating test).** The final magnetisation
profile must be a **two-component mixture**, not a rigid shift:
\[
\varrho_{t_f}(S^z_x)\;=\;T\,P(x-m_i+1/s)\;+\;(1-T)\,P(x-m_i)\;+\;O(\varepsilon),
\]
`P` the equilibrium kink profile of Lemma K2 (`⟨S^z_n⟩ = \tfrac12
\tanh[(x_0-n)\log(1/q)]` at `χ=1`).  Fit the two-component model and a
one-component rigid-shift model; the two-component fit must win with residual
ratio `> 5` whenever `0.2 < T < 0.8` (achievable at `Δ = 2`, `k_0 ≈ 0.25`).
Equivalently a two-time displacement measurement with a sharp initial wall
should give `Var(ΔX) = 4T(1−T)` to `2 %`; this is not an unconditional
one-time `Var(𝔛_W)` identity.  *Reference:* the finite projected computation
run gives `Var = 0.9998` vs `4TR = 0.9998` at `Δ = 2, k_0 = 0.25`.
**This is the test that separates a quantised lattice memory from the
continuous Lan–Xiao displacement.**

**P5 — conjectural no-drift test (depends on K4/R5).** After the packet has left `W`,
`|d\varrho_t(𝔛_W)/dt| < 10^{-4}` per unit `Jt` for `Jt` up to the
Lieb–Robinson horizon.  The conjectured outcome is no recoil even when
`R≈1`; this is a numerical target, not a theorem quantified over all
`k_0,Δ`.  A measured drift `∝Rk_0` falsifies Conjecture K4/R5.

**P6 — the flux identity (code check).**
`ϱ_{t_f}(𝔛_W) − ϱ_{t_i}(𝔛_W) = \tfrac{1}{2s}\int dt\,[ϱ_t(j_{a-1|a}) −
ϱ_t(j_{b|b+1})]` must hold to `10^{-6}` for *any* `W` and *any* times.  It is
an identity (Eq. 2.1); a failure is a bug, not physics.  Use it to validate
the current operator before trusting anything else.

**P7 — order of limits (the soft trap).** `lim_{k_0→0} δx = 0` at fixed packet,
but `lim_{σ→∞} δx` at fixed small `k_0` is `−1/s·T(k_0)` and is *not* `0`.
Numerically: at fixed `k_0 = 0.1`, `|δx|` must be independent of `σ` (to `5 %`)
for `σ ≫ 1/k_0`; while at fixed `σ`, `|δx| → 0` as `k_0 → 0`.  Verifying both
branches pins the non-commutativity that D17 predicts.

**P8 — conjectural higher-spin charge bookkeeping (if the code supports `s = 1`).**
`δx/N_T = −1/s = −1` for the spin-1 easy-axis chain.  Tolerance `2 %`.
A clean falsification target for the unproved higher-spin channel extension;
the D16/projected scope is spin `1/2`.

---

## 10. Honest post-r2 status and open items

**PROVED per corpus-r2, with the displayed conditions.**
* The physical-current flux/DC calculation, Eq. (2.2), is exact algebraically;
  no virtual/bond-potential reading is attached.
* D13(b) and D13(a) are the same finite-window expectation difference;
  unsubtracted D13(c) includes the leg charge and has the recorded trap.
* M′ is a conditional D18 implication with channel spectrum `{0,-1/s}`; its
  expectation is not integer-quantised.
* B3 consists only of the repaired finite-time label argument and
  `2s·δx+(q_out-q_in)=0`; the false half-line formula is retracted.
* K1--K3 and B3 are PROVED; M′ is PROVED conditional on D18; the Fano formula
  and soft zero are PROVED conditional on Mq-E for the displayed graph.

**SKETCH calculations/evidence.**
* The measured `O(Δ^{-2})` leakage beyond the displayed Fano projection is
  supporting evidence only.  Full-chain accuracy remains SKETCH, and
  universality of the quadratic zero and its coefficient remains CONJECTURE.

**What is conjecture.**
* **H-AD** for the full chain (D18) and the all-volume projected reduction
  Mq-E.
* Conjecture K4 in the thermodynamic limit (R5).
* **Conjecture Bc (the two `2`'s).** The magnon–magnon oracle gives
  `dδ_phys/dk_s|_0 = 2 sgn(v_h−v_s)`, which **on D8** is `2` (`O7`; see the
  freeze note in §5.3), i.e. a soft Wigner shift of `2` sites off a hard
  magnon; the kink memory quantum is `1/s = 2` sites.  Conjecture: both equal
  `|q_{\rm hard}|/s` with `q_{\rm hard}` the hard leg's `U(1)` charge relative
  to its vacuum, so that the *soft phase coefficient* and the *memory quantum*
  are the same asymptotic-charge datum.  **Status: CONJECTURE.**  Cheapest
  test: the spin-1 ferromagnet two-magnon Bethe phase should give
  `dδ/dk_s = 1`, not `2`.  If that fails, the coincidence is numerology and
  must be dropped from the paper.

**What is refuted.**
* **Conjecture M as written in the brief** ("`δx` equals the zero-frequency
  limit of the soft factor `S` summed over the event; the lattice
  Braginsky–Thorne relation") is **false in M2 as literally stated**.  The
  soft factor is a phase; the memory quantum is a charge.  Two independent
  reasons: (a) conditional charge bookkeeping fixes the same coefficient for
  every `k`, `Δ`, and packet once D18's channels exist, whereas any soft-factor expression varies with them;
  (b) `δx` is insensitive to `δ_t(k)` entirely — a purely transmitting wall
  with `δ_t ≡ 0` still displaces by exactly `−1/s`.  The surviving true
  statement is Eq. (2.2) + conditional M′: *memory is the DC weight of the
  **boundary current**, and the soft data enter only through `T(k)`*.  M-flux
  and conditional M-quant are PROVED per corpus-r2.

**Relation to prior art (novelty-sweep rows 2, 8).**
Lan–Xiao (arXiv:2107.05401) obtain, for a continuum easy-*plane* ferromagnet,
`ΔX = −(m/M)Δχ = −Gm/v_0^2` with `m = n\hbarω_0/c^2` — a displacement
*linear in the magnon number `n`*, quadratic-inverse in velocity, and
continuous: their spin wave is linearly polarised and carries **no angular
momentum**, and their wall is inertial, so no conservation law constrains the
answer.  The present easy-*axis* lattice result is the opposite regime: the
magnon carries `ΔS^z = ∓1`; conditional on D18, charge bookkeeping gives the
channel displacement `−1/s`, independent of `k` and phase.  Conjecture K4 is
the separate unproved flatness/locking statement.  Kim–Tserkovnyak–Tchernyshyov (arXiv:1406.6051)
report that magnons pass a *static* wall with no force; that is consistent
with P5 (no recoil) and orthogonal to P1 (charge-transfer displacement).
The post-r1 candidate is therefore: *channel displacement follows from charge
conservation, while its expectation is controlled by a transmission
probability*; universality of the computed Fano soft zero remains open.

**Scratch cross-checks recorded (not repo artifacts).**
`K1/K2`: `max‖h^{kink}v‖ ≤ 1.2·10^{-11}` for `Δ∈{1.5,2,4,8}`.
`K4`: `N=12`, `Δ=3`, every `m`: `E₀=0` (`10^{-13}`), unique, `E₁=2.03407417`.
`S1`: `N=14` enumeration, component size `12`, degrees `{1:3,2:8,3:1}`.
`M′/P1/P4`: finite Fano-graph computation, `N=2200`, `σ=40`;
`δx/(−2N_T)=1.000000`
and `Var = 4TR` to 4 digits across `Δ∈{2,4,8}`, `k∈[0.15,2.4]`.
`(5.1)`: `P_T` vs `T_{\rm Fano}` agree to `≤3·10^{-3}`, residual dominated by
packet averaging.
Leakage: `P(≥5\text{ walls})` `= 8·10^{-3}/3·10^{-2}/1·10^{-1}` at
`Δ = 8/4/2`.
