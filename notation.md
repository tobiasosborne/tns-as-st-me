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

Conventions: chain sites x ∈ ℤ; momenta k ∈ (−π, π]; ħ = 1; the
Heisenberg FM uses the vacuum-energy shift fixed in D6; XXZ anisotropy
Δ = J_z/J_⊥.

(Anchors are added as definitions.md grows; a symbol used anywhere without an
entry here is a defect.)
