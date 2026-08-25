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

Conventions: chain sites x ∈ ℤ; momenta k ∈ (−π, π]; ħ = 1; Heisenberg FM
H = −J Σ_x S_x·S_{x+1}, J > 0; XXZ anisotropy Δ = J_z/J_⊥.

(Anchors are added as definitions.md grows; a symbol used anywhere without an
entry here is a defect.)
