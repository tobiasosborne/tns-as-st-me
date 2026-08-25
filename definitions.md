<!-- ROLE: single-source numbered definitions (L4). Theory shards and the paper
     reference D-numbers; nothing is redefined elsewhere.
     Status: D1-D5 and D9-D11 written 2026-08-25 (Corner A, P1); frozen after the
     L6 critic loop passes. D6-D8 belong to the Bethe oracle and are FROZEN --
     do not edit them. -->

# Definitions

Reading order: D1 fixes the setting and all limit conventions; D2--D5 and
D9--D11 build on it. D6--D8 are self-contained (Bethe oracle).

---

## D1 (setting; uniform injective MPS; window vectors and decorations)

**(a) The setting.** Fix `d ∈ ℕ` and let the one-dimensional lattice be `ℤ`.
The *quasi-local algebra* is `𝔄 := ⨂_{x∈ℤ} M_d(ℂ)`, the C*-inductive limit of
the window algebras `𝔄_Λ := ⨂_{x∈Λ} M_d(ℂ)` over finite `Λ ⊂ ℤ`; `𝔄_loc :=
⋃_Λ 𝔄_Λ` is the (norm-dense) local subalgebra.  `τ_x ∈ Aut(𝔄)` is the
translation by `x`.  A *state* is a normalised positive linear functional on
`𝔄`; states are compared in the weak-* topology, i.e. pointwise on `𝔄_loc`.
For a state `ϱ`, `(H_ϱ, π_ϱ, Ω_ϱ)` denotes its GNS triple.

**(b) Uniform MPS tensor and transfer matrix.** A *uniform MPS tensor* of bond
dimension `χ` is `A = (A^s)_{s=1}^{d}`, `A^s ∈ M_χ(ℂ)`.  Its *transfer matrix*
is the completely positive map `E: M_χ → M_χ`, `E(Y) := Σ_s A^s Y (A^s)^†`
(equivalently the `χ²×χ²` matrix `Σ_s A^s ⊗ conj(A^s)`).

**(c) Injectivity, canonical form, gap.** `A` is *injective* (*normal*) if `E`
has spectral radius `1`, the eigenvalue `1` is the unique eigenvalue of modulus
`1`, it is non-degenerate, and its left/right eigenmatrices `l, r` (i.e.
`E^*(l) = l`, `E(r) = r`) are positive definite.  We fix the *canonical form*
`l = 𝟙`, `r > 0`, `tr(r) = 1`; the residual MPS gauge freedom is then
`A^s ↦ Y^{-1} A^s Y` with `Y` unitary commuting with `r`, together with an
overall phase.  We write
`λ_E := max{ |μ| : μ ∈ spec(E), μ ≠ 1 } < 1`
for the *transfer gap*; `ξ_c := −1/log λ_E` is the correlation length.
Injectivity is equivalent to: there is `n_0` with
`span{ A^{s_1}⋯A^{s_{n}} : s_1…s_{n} } = M_χ(ℂ)` for all `n ≥ n_0`.

**(d) The MPS state.** For injective `A` in canonical form, `ω_A` is the unique
state on `𝔄` with
`ω_A(O) = tr[ r · E_O(𝟙) ]` reversed-order contraction, concretely
`ω_A(O) = Σ_{s,s'} ⟨s'|O|s⟩ · tr[ (A^{s'_{w}})^† ⋯ (A^{s'_{1}})^† · 𝟙 · A^{s_1} ⋯ A^{s_w} · r ]`
for `O ∈ 𝔄_{[1,w]}`, extended by translation invariance.  `ω_A` is pure,
translation invariant, and exponentially clustering with rate `λ_E`.  We write
`(H_A, π_A, Ω_A)` for its GNS triple and suppress `π_A` when harmless.

**(e) Window vectors and decorations.** For a finite window `Λ = [a,b]`, a
*decoration* is a tuple `T = (T_a,…,T_b)` of tensors `T_x = (T_x^s)`, together
with *bond insertions* `M_{x|x+1} ∈ GL(χ)` on a finite set of bonds, and
boundary vectors `b_l, b_r ∈ ℂ^χ`.  The *window vector* is

  `|ψ_Λ(T; b_l, b_r)⟩ := Σ_{s_a…s_b} ⟨b_l| T_a^{s_a} M_{a|a+1} T_{a+1}^{s_{a+1}} ⋯ T_b^{s_b} |b_r⟩ |s_a…s_b⟩`.

A *decorated state* `ω_A[T]` is the state on `𝔄` obtained from a decoration
that differs from the uniform `A` only on finitely many sites and bonds, by the
prescription of (d) with the modified string and with `l, r` as the two
infinite environments; it is well defined because `E^n(Y) → tr(Y) r`
exponentially with rate `λ_E`, uniformly for `‖Y‖ ≤ 1`.  We write
`ω_A^{M@b}` for the state decorated by a single bond insertion `M` on bond `b`.

**(f) Register.** Every identity below is first an *exact algebraic identity
between window vectors* at finite `Λ`, and only then a statement about states
on `𝔄` obtained by an explicitly rated limit.  No manipulation of "the
infinite-chain wave function" is performed.

**Remark (why this setting).** Three alternatives were weighed: (i) finite
periodic rings with `N → ∞`; (ii) finite open chains with boundary vectors;
(iii) the infinite chain with the quasi-local algebra and GNS.  We choose
(iii).  Rings hide exactly the object of study — the two spatial infinities and
the boundary bonds that carry the asymptotic charge — and force kinks to appear
in pairs (cf. arXiv:1810.07006, §on topological sectors).  Open chains keep the
boundaries but make the boundary vectors physical parameters, so "asymptotic
symmetry" would degenerate into a statement about an arbitrary choice.  The
infinite chain with `𝔄` and weak-* limits gives (1) two genuine infinities,
(2) a sharp notion of superselection sector (D9) in which the kink statement
A2 has content, and (3) the disjointness of symmetry-broken vacua, which is the
entire mechanism of Corner A.  Its only cost is that half-infinite symmetry
strings are not elements of `𝔄`; this is a feature, not a bug — the failure of
strong convergence is precisely the content of A1(c) and A2.

---

## D2 (on-site symmetry; covariant vacuum family; intertwining relation)

Let `G` be a compact group (finite or a compact Lie group) with a unitary
representation `u: G → U(ℂ^d)` on one site, and let `U_Λ(g) := ⨂_{x∈Λ} u_x(g)`.
Write `𝒰(g)` for the induced linear map on tensors,
`(𝒰(g)A)^s := Σ_{s'} u(g)_{s s'} A^{s'}`, `u(g)_{ss'} := ⟨s|u(g)|s'⟩`;
`𝒰(g)𝒰(h) = 𝒰(gh)`.

**(a) Covariant vacuum family.** A *`G`-covariant vacuum family* is a finite or
compact set `Ω_vac` of labels, injective canonical-form tensors `{A_α}_{α∈Ω_vac}`
of common bond dimension `χ`, generating pairwise distinct states `ω_α := ω_{A_α}`,
together with a `G`-action `(g,α) ↦ g·α` on `Ω_vac` such that
`U_Λ(g)` maps `ω_α` to `ω_{g·α}` for every finite `Λ`, in the sense
`ω_α ∘ Ad(U_Λ(g)^†) = ω_{g·α}` on `𝔄_Λ` for all `Λ`.
`H_α := { g ∈ G : g·α = α }` is the *stabiliser* (the *unbroken subgroup*).
The family is *unbroken at `α`* if `H_α = G` (then `|Ω_vac|` may be `1`).

**(b) Intertwining relation (IT).** For every `α ∈ Ω_vac` and `g ∈ G` there
exist a phase `θ_α(g) ∈ ℝ/2πℤ` and `V_α(g) ∈ U(χ)` with

  `Σ_{s'} u(g)_{s s'} A_α^{s'} = e^{i θ_α(g)} V_α(g)^{-1} A_{g·α}^{s} V_α(g)`  for all `s`.   **(IT)**

The pair `(θ_α(g), V_α(g))` is unique up to `V_α(g) ↦ e^{iφ} V_α(g)`.
*Ground truth:* this is the fundamental theorem of MPS.  For the existence,
refs/arxiv-0802.0447 (`StringOrder-v10.tex`), Lemma 1: `ρ(E_u) ≤ 1` with
equality iff there are a unitary `V` and `θ` with
`V^† Ã_j = e^{i(θ−θ_j)} Ã_j V^†`, together with condition C1
`(u⊗𝟙)B = (𝟙⊗V) B V^†`; and refs/arxiv-2011.12127 (`TN-Review-main.tex`),
which for `U(g)^{⊗N}|ψ_N⟩ ≃ |ψ_N⟩` states
`Σ_j U_{ij}(g) A^j = e^{iφ(g)} X^†(g) A^i X(g)`.
For the uniqueness, refs/arxiv-2011.12127 Eq. (eq:XAX=B):
`X^{-1}A^i X = e^{iχ} Y^{-1} A^i Y ⟹ χ = 0 ∧ ∃φ: X = e^{iφ}Y`.

**(c) Cocycles.** Composition of (IT) (proved in corner-a.md ⟨1⟩2) gives, for
all `g,h ∈ G`,
  `θ_α(hg) = θ_α(g) + θ_{g·α}(h)`,   `V_{g·α}(h) V_α(g) = e^{i ω_α(h,g)} V_α(hg)`.
Restricted to `g,h ∈ H_α` these say that `θ_α|_{H_α}: H_α → U(1)` is a
homomorphism and that `ω_α: H_α × H_α → U(1)` is a 2-cocycle.  Its class
`[ω_α] ∈ H²(H_α, U(1))` is the *SPT index* of `A_α`.  (Notation hazard: `ω`
with two group arguments is this cocycle; `ω(k)` with a momentum argument is
the magnon dispersion of D6.  The two never occur with the same argument type.)

**(d) Normal ordering.** `ǔ_α(g) := e^{−iθ_α(g)} u(g)` for `g ∈ H_α` is again a
unitary representation of `H_α` (because `θ_α|_{H_α}` is a homomorphism), and
satisfies (IT) with phase `1`.  All charges below are those of `ǔ_α` unless
stated otherwise; physically this is the charge measured from its vacuum value.

**(e) Smoothness hypothesis (S).** When `G` is a Lie group we assume, and state
whenever used, that `ε ↦ A_{exp(εξ)·α}` and `ε ↦ V_α(exp(εξ))` admit
`C¹` local sections with `V_α(e) = 𝟙`.  We then write
`X_α(ξ) := d/dε V_α(exp(εξ))|_{ε=0}` (anti-Hermitian) and
`θ'_α(ξ) := d/dε θ_α(exp(εξ))|_{ε=0}`.

---

## D3 (admissible profiles; truncated and modulated symmetry operations)

**(a) Profile classes (the function-space discipline).** Let
`𝔉_c := { f: ℤ → G : f(x) = e for all but finitely many x }`,
`𝔉_ec := { f: ℤ → G : f is constant on some (−∞,−n] and on some [n,∞) }`,
and for a Lie algebra element `ξ ∈ 𝔤` let
`𝔉_c(ξ) := { f: ℤ → ℝ finitely supported }`,
`𝔉_ec(ξ) := { f: ℤ → ℝ : f constant near ±∞ }`,
`𝔉_{ℓ¹}(ξ) := { f: ℤ → ℝ : Σ_x |f(x+1) − f(x)| < ∞ }`  (finite total variation).
`𝔉_c ⊂ 𝔉_ec` and `𝔉_ec(ξ) ⊂ 𝔉_{ℓ¹}(ξ)`.  A profile is *admissible* for an
operator statement iff it lies in `𝔉_c` (then the operator is in `𝔄_loc`); it
is admissible for a *state* statement iff it lies in `𝔉_ec` (then the operator
is a weak-* limit of elements of `𝔄_loc`, cf. A1(c), A2).  The plane wave
`f(x) = e^{ikx}` lies in none of these for `k ≠ 0`; it is admitted only inside
a Fourier transform, i.e. as the distributional kernel of a wave packet
`Σ_k φ(k) f_k` with `φ ∈ C_c^∞((−π,π])`.  Every soft statement must say which
class it uses.

**(b) Truncated symmetry.** For finite `R = [a,b] ⊂ ℤ`,
`U_R(g) := Π_{x∈R} u_x(g) ∈ 𝔄_loc`.  Its *boundary bonds* are
`∂_-R := (a−1|a)` and `∂_+R := (b|b+1)`; `|R| = b−a+1`.
More generally for `f ∈ 𝔉_c`, `U[f] := Π_x u_x(f(x)) ∈ 𝔄_loc`.

**(c) Half-infinite strings.** For `f ∈ 𝔉_ec` the product `U[f]` is *not* an
element of `𝔄`.  It is used only through the induced maps on states:
`ϱ ↦ w*-lim_{n→∞} ϱ ∘ Ad(U[f_n]^†)`, where `f_n ∈ 𝔉_c` agrees with `f` on
`[−n,n]` and is `e` outside.  Existence of this limit is a theorem, not a
definition (A1(c), A2); when it exists the limit state is written `f ⊳ ϱ`.
The canonical case is `f = 1_{[x,∞)}·g`, written `U_{[x,∞)}(g)`.

---

## D4 (lattice asymptotic symmetry `𝒜`; charge algebra)

Fix a bond `b`, a vacuum label `α`, and work in the unbroken case `H_α = G`
(the broken case is D9/A2).

**(a) Bond implementers.** For `M ∈ GL(χ)` let `𝒱_b(M)` denote the operation
"insert `M` on bond `b`" on decorated states (D1(e)):
`ω_A[T] ↦ ω_A[T with M_b ↦ M · M_b]`.  Write `𝒱_b(g) := 𝒱_b(V_α(g)^{-1})`.

**(b) The two asymptotic copies.** `G_L` and `G_R` denote the two copies of `G`
acting through half-infinite strings on `(−∞,b]` and `[b+1,∞)` respectively
(D3(c)).  By WI (corner-a.md ⟨1⟩3) the left string leaves `V_α(g_L)` on bond
`b` (it is the `∂_+R` insertion of `R = [x',b]`, `x' → −∞`) and the right string
leaves `V_α(g_R)^{-1}` on bond `b` (the `∂_-R` insertion of `R = [b+1,y]`,
`y → +∞`).  Their composite is `𝒱_b(V_α(g_L)V_α(g_R)^{-1})`, which is trivial
for `g_L = g_R`, consistently with the global symmetry `U_ℤ(g)` fixing `ω_α`.
`G_diag ⊂ G_L × G_R` is the diagonal subgroup, realised by `U_ℤ(g)`.

**(c) The asymptotic symmetry space.** `𝒜 := (G_L × G_R)/G_diag`, the quotient
*set* of the left coset space, with the residual `G_L × G_R`-action
`(g_L,g_R)·[a] = [g_L a g_R^{-1}]` under the bijection
`(G×G)/G_diag ≅ G`, `[(g_L,g_R)] ↦ g_L g_R^{-1}`.
**`𝒜` is a group iff `G` is abelian** (`G_diag` is normal in `G × G` iff `G` is
abelian); in general it is a homogeneous `G_L×G_R`-space.  We say
"asymptotic symmetry *group*" only when `G` is abelian, and otherwise speak of
the asymptotic symmetry *space* and of the `G_L × G_R` charge algebra.

**(d) Charge algebra.** The *asymptotic charge algebra at `α`* is the twisted
group algebra `𝔞_α := ℂ_{ω_α}[H_α]`, i.e. the algebra with basis `{ v_g }_{g∈H_α}`
and product `v_h v_g = e^{i ω_α(h,g)} v_{hg}`.  Its defining representation on
the virtual space `ℂ^χ` is `v_g ↦ V_α(g)`.  For a Lie group, with (S) of D2(e),
the *asymptotic charges* are `𝔮_b(ξ) := 𝒱_b`-generator of `X_α(ξ)`, and they
obey
  `[𝔮_b(ξ), 𝔮_b(ζ)] = 𝔮_b([ξ,ζ]) + c_α(ξ,ζ) · 𝟙`,
with `c_α` the Lie-algebra 2-cocycle obtained from `ω_α`; `[c_α] ∈ H²(𝔥_α, ℝ)`
is the *central extension* of the charge algebra and is the infinitesimal
shadow of `[ω_α]`.

---

## D5 (excitation ansatz; kink sectors; null directions)

**(a) Ansatz.** For injective canonical-form tensors `A_α, A_β`, a tensor
`B = (B^s)`, `B^s ∈ M_χ`, and `k ∈ (−π,π]`, the *excitation-ansatz vector* is
defined on windows by

  `|Φ_k(B; A_α, A_β)⟩_Λ := Σ_{n∈Λ} e^{ikn} |ψ_Λ( …A_α A_α B A_β A_β… ; b_l, b_r)⟩`,

with `B` at site `n`, `A_α` at all sites `< n` and `A_β` at all sites `> n`.
For `α = β` we write `|Φ_k(B)⟩` and call it the *trivial* (local) sector; for
`α ≠ β` it is the *kink* (topological) sector.  The convention matches
refs/arxiv-1103.2286 (`dispersionrelation_final.tex`):
`|Φ_κ(B)⟩ = Σ_n e^{iκn} T^n v_L^†(⋯A^{s_{-1}} B^{s_0} Ã^{s_1}⋯)v_R |s⟩`,
and refs/arxiv-1810.07006 (`p5_excitations.tex`, Eq. (eq:kink)).
On the infinite chain these are δ-normalised generalised vectors:
`⟨Φ_k(B)|Φ_{k'}(B')⟩ = 2π δ(k−k') · B^† N_k B'`.

**(b) Null directions.** For `X ∈ M_χ` set
  `𝒩_k^{αβ}(X) := e^{ik} A_α X − X A_β`,  i.e. `𝒩_k(X)^s = e^{ik} A_α^s X − X A_β^s`.
Then `|Φ_k(𝒩_k(X); A_α, A_β)⟩ = 0` identically (exact telescoping;
corner-a-goldstone.md ⟨1⟩5).  This is the *gauge freedom* `B ≃ B + e^{ik} A X − X A` of the brief;
ground truth refs/arxiv-1103.2286: "the choice `B^s = e^{iκ} A^s X − X Ã^s`
results in `|Φ_κ(B)⟩ = 0`", and refs/arxiv-1810.07006 Eq. (eq:gaugeexcitations)
`B → B + Y A_R − e^{ip} A_L Y` (the same map with `Y = −X`).
The rank of `X ↦ 𝒩_k(X)` is `χ²` for `k ≠ 0` and `χ² − 1` for `k = 0, α = β`
(corner-a-goldstone.md ⟨1⟩5); the missing direction is `A_α` itself.

---

**D6 (Heisenberg-ferromagnet oracle model and bases).** On the infinite chain,
or on a periodic ring of `N` sites when finite volume is stated, let
`S_x=σ_x/2`, `J>0`, and
`H=Σ_x h_{x,x+1}=−JΣ_x(S_x·S_{x+1}−1/4)`.
Equivalently, `h_{x,x+1}=(J/2)(1−P_{x,x+1})`, where `P` swaps the two
spins.  The vacuum is `|Ω⟩=|↑↑⋯⟩`, the coordinate bases are
`|x⟩=S_x^-|Ω⟩` and `|x,y⟩=S_x^-S_y^-|Ω⟩` with `x<y`, lattice
momenta lie in `(−π,π]`, `z(k)=exp(ik)`, and
`|k⟩_N=N^{−1/2}Σ_{x=0}^{N−1}e^{ikx}|x⟩` for `k=2πn/N`.  On the
infinite chain the same sum denotes the delta-normalized generalized state.
The symbols `ω(k)` and `v(k)=dω/dk` denote the one-magnon energy and
group velocity derived from this `H`.

**D7 (ordered-coordinate Bethe and scattering convention).** In the chamber
`x<y`, the two-magnon coordinate Bethe wave is
`ψ(x,y)=A_{12}e^{i(k_1x+k_2y)}+A_{21}e^{i(k_2x+k_1y)}` and
`S_{12}(k_1,k_2):=A_{12}/A_{21}`; `S_{21}:=A_{21}/A_{12}`; and
`E(k_1,k_2)` denotes the corresponding scattering energy.  For real wave packets with
`v(k_2)>v(k_1)` and the `k_2` packet initially on the left, `A_{21}` is the
incoming coefficient and `A_{12}` the outgoing coefficient.  Reversing the
channel convention gives `S_{21}=S_{12}^{−1}`.  The rapidity
is `λ(k):=(1/2)cot(k/2)`.  Whenever `S_{12}=e^{iδ}` is expanded at a point
where `S_{12}=1`, `δ` is the unique continuous real branch with `δ=0` at
that point.  For a two-magnon bound state, `K:=k_1+k_2`, `r:=y−x`, `f_r`
is the relative-coordinate wave, `t` its geometric decay factor,
`η:=−log|t|`, and `E_b(K)` its energy.

**D8 (Bethe-oracle soft limit).** The hard momentum `k_h∈(0,π)` is held
fixed while the signed soft momentum `k_s→0`; `ω_s:=ω(k_s)` and
`σ:=sgn(k_s)` when a one-sided energy expansion is used.  A simultaneous
limit of `k_h` and `k_s` is not included unless explicitly stated.

---

## D9 (vacuum and kink superselection sectors)

Let `{ω_α}_{α∈Ω_vac}` be a `G`-covariant vacuum family (D2(a)).

**(a) Sector labels.** For `α, β ∈ Ω_vac` the *kink sector* `𝒦_{αβ}` is the set
of states `ϱ` on `𝔄` obeying the *factorised* boundary conditions at infinity
  `lim_{n→−∞} ϱ(D·τ_n(O)) = ϱ(D)·ω_α(O)`  and  `lim_{n→+∞} ϱ(D·τ_n(O)) = ϱ(D)·ω_β(O)`
for all `D, O ∈ 𝔄_loc`.  (Taking `D = 𝟙` gives the plain conditions
`ϱ(τ_n(O)) → ω_{α/β}(O)`; the factorised form is what makes the label stable
under normal perturbations, corner-a-kinks.md ⟨1⟩8, and it holds with rate
`λ_E` for every decorated MPS state, ibid. ⟨1⟩8(iii).)
`𝒦_{αα}` is the *vacuum sector of `α`*; it contains
`ω_α` and every state of the form `ω_α ∘ Ad(W^†)` with `W ∈ 𝔄` unitary, and
every decorated state `ω_{A_α}[T]` of D1(e).  A state in `𝒦_{αβ}` with `α ≠ β`
is a *kink state* (equivalently a domain-wall or topological state).

**(b) Disjointness.** States in `𝒦_{αβ}` and `𝒦_{α'β'}` with `(α,β) ≠ (α',β')`
are disjoint (mutually non-normal); proved in corner-a-kinks.md ⟨1⟩8.  Hence
"superselection sector" is used here in the precise sense: the label `(α,β)` is
a classical observable at infinity, unchangeable by any element of `𝔄`.

**(c) Twisted (endpoint) sectors.** In the unbroken case `H_α = G` the label is
always `(α,α)`, and the sector carries no information.  The nontrivial data are
then the *`g`-twisted endpoint sectors*: for `g ∈ G` the family of states
`{ ω_{A_α}^{M@b} : M ∈ V_α(g)·GL(χ) }`, which is a module over the charge
algebra `𝔞_α` of D4(d).  When "`𝒜` relabels charge superselection sectors" is
asserted (claim A1) it is asserted about these endpoint sectors and about the
`𝔞_α`-module structure of `ℂ^χ`, never about `𝒦_{αβ}`, which is trivial in the
unbroken case.

**(d) `𝒜`-orbit.** `G_L × G_R` acts on the label set `Ω_vac × Ω_vac` by
`(g_L,g_R)·(α,β) := (g_L·α, g_R·β)`.  If `G` acts transitively on `Ω_vac` this
action is transitive with stabiliser `H_α × H_β`; the *relative twist*
`[g_L g_R^{-1}] ∈ 𝒜` is the `G_diag`-invariant content, and `𝒜 ≅ Ω_vac` as a
`G`-set when `Ω_vac ≅ G/H_α` with `H_α` normal.

---

## D10 (lattice Noether pair: charge density, current, modulated charge)

Let `H = Σ_x h_{x,x+1}` be a translation-invariant nearest-neighbour
Hamiltonian (the definition extends verbatim to finite range `R_h`), let
`𝔤 = Lie(G)`, and for `ξ ∈ 𝔤` let `q(ξ) := d/dε u(exp(εξ))|_{ε=0}`
(anti-Hermitian on `ℂ^d`), with `q_x(ξ)` its copy at site `x`.  Assume `H` is
`G`-invariant on-site: `[h_{x,x+1}, q_x(ξ) + q_{x+1}(ξ)] = 0`.

**(a) Current.** `j_{x,x+1}(ξ) := −[h_{x,x+1}, q_x(ξ)] = [h_{x,x+1}, q_{x+1}(ξ)]`.

**(b) Continuity equation.** `[H, q_x(ξ)] = j_{x-1,x}(ξ) − j_{x,x+1}(ξ)`
(proved in corner-a-goldstone.md ⟨1⟩6); this is the exact lattice conservation law.

**(c) Modulated charge and current.** For `f ∈ 𝔉_c(ξ)`,
`Q[f;ξ] := Σ_x f(x) q_x(ξ) ∈ 𝔄_loc` and `J[f;ξ] := Σ_x f(x) j_{x,x+1}(ξ)`.
For `f(x) = e^{ikx}` we write `Q_k(ξ)`, `J_k(ξ)`, understood in the
wave-packet sense of D3(a).

**(d) Bond current potential (the "potential" of docs/framing.md).** In the
unbroken case with (IT) and normal ordering (D2(d)), `𝒥_b(ξ)` denotes the
operation "insert `X_α(ξ)` on bond `b`" (D4(a)).  Theorem G0(d)
(corner-a-goldstone.md ⟨1⟩6) states `q_x(ξ) ▹ ω_α = (𝒥_{x|x+1}(ξ) − 𝒥_{x-1|x}(ξ)) ▹ ω_α`: the
physical charge density acting on the vacuum is the lattice divergence of a
purely virtual (bond) quantity.  `𝒥` is the lattice analogue of the gauge
potential; `q` is the field strength.

---

## D11 (Goldstone tensor; broken and unbroken directions)

Assume (S) of D2(e).  Fix `α ∈ Ω_vac`, write `𝔥_α := Lie(H_α)`, and choose an
`Ad(H_α)`-invariant complement `𝔪_α` with `𝔤 = 𝔥_α ⊕ 𝔪_α` (the *broken
directions*).

**(a) Goldstone tensor.** `B_G(ξ) := d/dε [ 𝒰(exp(εξ)) A_α ]|_{ε=0}` for
`ξ ∈ 𝔤`.  Equivalently `B_G(ξ)^s = Σ_{s'} q(ξ)_{s s'} A_α^{s'}`.

**(b) Soft insertion.** `|Φ_k(B_G(ξ))⟩ = Q_k(ξ) ▹ ω_α` in the sense of D5(a)
and D10(c): replacing `A_α` by `B_G(ξ)` at site `n` is exactly the action of
`q_n(ξ)`.

**(c) Goldstone count.** The number of independent Goldstone tensors at `α` is
`dim_ℂ span_ℂ{ B_G(ξ) : ξ ∈ 𝔪_α } mod 𝒩_0(·)`, which may be strictly smaller
than `dim_ℝ 𝔪_α`.  The deficiency is the *type-B* phenomenon; the isotropic
ferromagnet realises `dim_ℝ 𝔪_α = 2 → 1` Goldstone mode (corner-a-goldstone.md ⟨1⟩7).
