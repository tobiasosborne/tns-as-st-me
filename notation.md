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
| `𝒜` | lattice asymptotic symmetry group (G_L × G_R)/G_diag | definitions.md D4 |
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
| `𝒱_b(M)`, `𝒱_b(g)` | bond-insertion implementer on bond `b`; `𝒱_b(V_α(g)^{-1})` | definitions.md D4 |
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

Conventions: chain sites x ∈ ℤ; momenta k ∈ (−π, π]; ħ = 1; the
Heisenberg FM uses the vacuum-energy shift fixed in D6; XXZ anisotropy
Δ = J_z/J_⊥.

Deliberate overload (one only, flagged): `ω` with a *momentum* argument, `ω(k)`,
is the magnon dispersion (D6, frozen); `ω` with *two group* arguments,
`ω_α(g,h)`, is the projective 2-cocycle (D2), whose class is the `[ω]` row
above.  The argument types never coincide.  All other symbols are unique.

(Anchors are added as definitions.md grows; a symbol used anywhere without an
entry here is a defect.)
