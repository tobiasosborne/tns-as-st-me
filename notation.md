<!-- ROLE: single-source symbol table (L4). Every symbol defined exactly once.
     Theory shards, code docstrings, and the paper cite entries here by anchor. -->

# Notation

| Symbol | Meaning | First fixed in |
|---|---|---|
| `A^s_{ij}` | uniform-MPS tensor; physical index s (dim d), virtual i,j (dim χ) | definitions.md D1 |
| `E` | transfer matrix Σ_s A^s ⊗ conj(A^s) | definitions.md D1 |
| `G`, `u(g)` | on-site symmetry group and its physical unitary | definitions.md D2 |
| `V(g)` | virtual (projective) representation from the fundamental theorem | definitions.md D2 |
| `[ω]` | class of V in H²(G,U(1)); the SPT index | definitions.md D2 |
| `U_R(g)` | truncated symmetry string Π_{x∈R} u_x(g) on interval R | definitions.md D3 |
| `𝒜` | ~~lattice asymptotic symmetry group~~ **(SUPERSEDED r2/r3)** — the coset *space* `(G_L×G_R)/G_diag`; a **group** only for abelian `G`, and **never** the vacuum orbit unless `N_α = {e}`.  The object that acts is `𝒜_eff = G/N_α` (unbroken) or `(G/H_α)²` with double-coset invariant (broken).  Do not use `𝒜` as a classifying object | definitions.md D4(b), D9(d) |
| `|Φ_k(B)⟩` | excitation-ansatz state Σ_x e^{ikx}(…A B A…) | definitions.md D5 |
| `B ≃ B + e^{ik} A X − X A` | tangent-space gauge freedom (null directions) | definitions.md D5 |
| `S(k; ·)` | soft factor in Conjecture S | claims/CLAIMS.md S |
| `R(k)` | soft-theorem remainder, o(S(k)) in the stated norm | claims/CLAIMS.md S |
| `δx` | kink collective-coordinate displacement (memory observable) | claims/CLAIMS.md M |
| `H`, `h_{x,x+1}`, `J`, `P_{x,x+1}` | shifted isotropic spin-1/2 Heisenberg-ferromagnet Hamiltonian, bond term, positive exchange, and spin swap | definitions.md D6 |
| `N` | number of sites when the chain is specialized to a periodic ring | definitions.md D6 |
| `|Ω⟩`, `|x⟩`, `|x,y⟩` | all-up vacuum, one-down-spin basis, and ordered two-down-spin basis | definitions.md D6 |
| `|k⟩_N` | normalized one-magnon momentum state on an `N`-site ring | definitions.md D6 |
| `k`, `z(k)` | lattice momentum in `(−π,π]` and `exp(ik)` | definitions.md D6 |
| `ω(k)`, `v(k)` | one-magnon energy and group velocity `dω/dk` | definitions.md D6 |
| `λ(k)` | Heisenberg rapidity `(1/2) cot(k/2)` | definitions.md D7 |
| `ψ(x,y)`, `A_{12}`, `A_{21}` | ordered-coordinate two-magnon wave and its Bethe coefficients | definitions.md D7 |
| `S_{12}`, `S_{21}` | coefficient ratios `A_{12}/A_{21}` and its inverse | definitions.md D7 |
| `E(k_1,k_2)` | two-magnon scattering energy | definitions.md D7 |
| `δ(k_1,k_2)` | continuous phase branch of `S_{12}=exp(iδ)` fixed at a stated base point | definitions.md D7 |
| `K`, `r`, `f_r`, `t`, `η`, `E_b(K)` | bound-pair total momentum, separation, relative wave, decay data, and energy | definitions.md D7 |
| `k_s`, `k_h`, `ω_s`, `σ` | signed soft momentum, fixed hard momentum, soft energy, and soft-direction sign | definitions.md D8 |

| `𝔄`, `𝔄_Λ`, `𝔄_loc` | quasi-local algebra, window algebra, local subalgebra | definitions.md D1 |
| `τ_x` | translation automorphism by x sites | definitions.md D1 |
| `ω_A`, `(H_A, π_A, Ω_A)` | MPS state on `𝔄` and its GNS triple | definitions.md D1 |
| `l`, `r` | left/right fixed matrices of `E`; canonical form `l = 𝟙`, `tr r = 1` | definitions.md D1 |
| `λ_E`, `ξ_c` | transfer gap (second-largest modulus) and correlation length | definitions.md D1 |
| `Λ`, `W` | finite windows in ℤ | definitions.md D1 |
| `\|ψ_Λ(T; b_l, b_r)⟩` | decorated window vector (tensors + bond insertions + boundary vectors) | definitions.md D1 |
| `ω_A[T]`, `ω_A^{M@b}` | decorated MPS state; single bond insertion `M` on bond `b` | definitions.md D1 |
| `𝒰(g)` | action of `u(g)` on a tensor's physical index | definitions.md D2 |
| `Ω_vac`, `α`, `A_α`, `ω_α` | vacuum label set, label, tensor, and state | definitions.md D2 |
| `g·α` | `G`-action on vacuum labels | definitions.md D2 |
| `H_α`, `𝔥_α`, `𝔪_α` | stabiliser (unbroken subgroup), its Lie algebra, broken complement | definitions.md D2, D11 |
| `θ_α(g)` | phase 1-cocycle in (IT); homomorphism on `H_α` | definitions.md D2 |
| `ω_α(g,h)` | 2-cocycle `V(h)V(g) = e^{iω(h,g)}V(hg)`; class `[ω_α] ∈ H²(H_α,U(1))` | definitions.md D2 |
| `ǔ_α(g)` | normal-ordered symmetry `e^{−iθ_α(g)}u(g)` | definitions.md D2 |
| `X_α(ξ)`, `θ'_α(ξ)` | derivatives `dV_α/dε`, `dθ_α/dε` at the identity (hypothesis (S)) | definitions.md D2 |
| `𝔉_c`, `𝔉_ec`, `𝔉_{ℓ¹}` | admissible profile classes: finite support / eventually constant / finite total variation | definitions.md D3 |
| `U[f]`, `f ⊳ ϱ` | modulated symmetry operation; induced map on states (half-infinite limit) | definitions.md D3 |
| `∂_-R`, `∂_+R` | left and right boundary bonds of an interval `R` | definitions.md D3 |
| `𝒱_b(M)`, `𝒱_b(g)` | bond-insertion implementer on bond `b`, defined on **padded** windows only (D4(a1)); `𝒱_b(g) := 𝒱_b(V_α(g))` — **the r2 inverse convention `V_α(g)^{-1}` is superseded**, it reverses the cocycle law | definitions.md D4(a) |
| `G_L`, `G_R`, `G_diag` | left/right asymptotic copies of `G` and the diagonal (global) subgroup | definitions.md D4 |
| `𝔞_α = ℂ_{ω_α}[H_α]` | asymptotic charge algebra (twisted group algebra) | definitions.md D4 |
| `𝔮_b(ξ)`, `c_α(ξ,ζ)` | asymptotic charge on bond `b`; Lie-algebra central-extension cocycle | definitions.md D4 |
| `\|Φ_k(B; A_α, A_β)⟩` | kink-sector excitation ansatz (mixed vacua) | definitions.md D5 |
| `𝒩_k^{αβ}(X)` | null-direction map `e^{ik}A_α X − X A_β` | definitions.md D5 |
| `𝒦_{αβ}` | kink superselection sector (vacuum `α` at −∞, `β` at +∞) | definitions.md D9 |
| `𝔤`, `ξ`, `ζ` | Lie algebra of `G` and its elements | definitions.md D10 |
| `q_x(ξ)`, `j_{x,x+1}(ξ)` | on-site charge density and bond current (anti-Hermitian convention) | definitions.md D10 |
| `Q[f;ξ]`, `J[f;ξ]`, `Q_k`, `J_k` | modulated charge and current; plane-wave (wave-packet) versions | definitions.md D10 |
| `𝒥_b(ξ)` | bond current potential — insertion of `X_α(ξ)` on bond `b` | definitions.md D10 |
| `B_G(ξ)` | Goldstone tensor `d/dε[𝒰(e^{εξ})A_α]` | definitions.md D11 |
| `λ̃` | any rate in `(λ_E,1)`; honest transfer-decay bound `‖E^m−P‖ ≤ C_λ̃ λ̃^m` (Jordan-safe) | definitions.md D1(c) |
| `C_∂` | uniform bound on window-vector norms, independent of `\|Λ\|` | definitions.md D1(e) |
| `ω_{α\|β}^{(m)}[T]` | two-sided (half-line) decorated state: `A_α` on `(−∞,m]`, `A_β` on `[m+1,∞)` | definitions.md D1(e′) |
| `𝒲_{Λ,b}` | linear space of window vectors carrying one insertion on bond `b` | definitions.md D4(a) |
| `N_α` | `{g : V_α(g) ∈ ℂ^×𝟙}`, the kernel of the state-level asymptotic action | definitions.md D4(b) |
| `ρ_α` | homomorphism `G → PGL(χ)`, `g ↦ [V_α(g)]`; `ker ρ_α = N_α` | definitions.md D4(b) |
| `𝒜_eff` | effective asymptotic symmetry **group** `G/N_α ≅ ρ_α(G) ⊆ PGL(χ)` | definitions.md D4(b) |
| `S_α` | true stabiliser `{(g_L,g_R) : g_Lg_R^{-1} ∈ N_α} ⊇ G_diag` | definitions.md D4(c) |
| `E_b^α` | endpoint space `{ω_{A_α}^{M@b}}`, a `PGL(χ)`-torsor | definitions.md D9(c) |
| `𝔡(α_L,α_R)` | double-coset label `H_α g_L^{-1}g_R H_α ∈ H_α\G/H_α`; complete diagonal invariant of a vacuum pair | definitions.md D9(d) |
| `j_{m\|m+1}(ξ)` | **cut current** `−[H, Σ_{y≤m}q_y(ξ)]`, finite range; supersedes the nearest-neighbour `j_{x,x+1}` row above | definitions.md D10(a) |
| `𝔅_Λ[f,X]` | gauge remainder: the two boundary window vectors left by summation by parts | definitions.md D12, corner-a-goldstone.md ⟨1⟩5 |
| `(Δf)(m)` | forward difference `f(m+1) − f(m)` of a profile | corner-a-goldstone.md ⟨1⟩5 |
| `c_0(ℤ)` | profiles vanishing at infinity; the class in which the gauge identity is exact | definitions.md D12(a) |
| `PGL(χ)`, `PU(χ)` | projective (unitary) group on the virtual space `ℂ^χ` | definitions.md D4(b) |

Conventions: chain sites x ∈ ℤ; momenta k ∈ (−π, π]; ħ = 1; the
Heisenberg FM uses the vacuum-energy shift fixed in D6; XXZ anisotropy
Δ = J_z/J_⊥.

Deliberate overload (one only, flagged): `ω` with a *momentum* argument, `ω(k)`,
is the magnon dispersion (D6, frozen); `ω` with *two group* arguments,
`ω_α(g,h)`, is the projective 2-cocycle (D2), whose class is the `[ω]` row
above.  The argument types never coincide.  All other symbols are unique.

(Anchors are added as definitions.md grows; a symbol used anywhere without an
entry here is a defect.)

| `ι_{Λ,b}` | `M ↦` window vector with `M` inserted on bond `b`; injective **iff** the window is padded (D4(a1)--(a2)) | definitions.md D4(a) |
| `⋆` | endpoint action on representatives, `g ⋆ M := V_α(g)M` (D9(c), definition only) | definitions.md D9(c) |
| `(T)` | hypothesis "`G` acts transitively on `Ω_vac`"; required by the vacuum-pair classification | definitions.md D9(d) |
| `ℓ¹ ∩ BV` | summable profiles of bounded variation — the class for norm-convergent wave-packet statements | definitions.md D12(a′) |

Revision r2/r3 (2026-08-25): rows were appended after the r1 and r2 critic
verdicts; nothing was renumbered or deleted.  **Three earlier rows are marked
SUPERSEDED in place** rather than left to mislead (r2 objection 9): the
`𝒱_b(V_α(g)^{-1})` inverse convention, the description of `𝒜` as a group, and
`j_{x,x+1}` (superseded by the cut current `j_{m|m+1}`, D10(a)).  The
superseded forms remain correct only in their original restricted settings
(nearest-neighbour `H`; abelian `G` with faithful `ρ_α`).
