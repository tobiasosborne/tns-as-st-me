<!-- ROLE: single-source numbered definitions (L4). Theory shards and the paper
     reference D-numbers; nothing is redefined elsewhere. Status: stubs D1–D5
     seeded from the brief; each gets its precise form during P1 and is frozen
     only after the L6 critic loop passes. -->

# Definitions

**D1 (uniform MPS, injectivity).** [stub — brief §1.1] Uniform MPS |ψ(A)⟩,
injective ⇔ transfer matrix E has unique top eigenvalue; normalization and
fixed points (l|, |r).

**D2 (on-site symmetry, intertwiner).** [stub — brief §1.1, eq. (IT)]
Σ_{s'} u(g)_{ss'} A^{s'} = e^{iθ(g)} V(g)^{-1} A^s V(g); projective class
[ω] ∈ H²(G,U(1)).

**D3 (truncated symmetry / Ward identity).** [stub — brief §1.2, eq. (WI)]
U_R(g)|ψ(A)⟩ = phase × state with V(g), V(g)^{-1} inserted on the two boundary
bonds of R.

**D4 (lattice asymptotic symmetry group 𝒜).** [stub — brief §2.A]
𝒜 = (G_L × G_R)/G_diag, realized by virtual insertions at ±∞; charge algebra
with central extension class [ω] (framing.md discipline: state as a charge
algebra with explicit admissible-profile function space).

**D5 (excitation ansatz, kink sectors).** [stub — brief §1.3]
|Φ_k(B)⟩ = Σ_x e^{ikx}|ψ(…A B A…)⟩; gauge freedom B ≃ B + e^{ik}AX − XA;
mixed-vacuum (A_α, A_β) kink sectors.

Definitions D9+ (soft factor, memory observable δx, admissible state classes,
norms for R(k)) are added during P1/P2.

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
