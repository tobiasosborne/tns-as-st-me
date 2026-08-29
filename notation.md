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
| `\|Φ_k(B)⟩` | excitation-ansatz state Σ_x e^{ikx}(…A B A…) | definitions.md D5 |
| `B ≃ B + e^{ik} A X − X A` | tangent-space gauge freedom (null directions) | definitions.md D5 |
| `S(k; ·)` | ~~soft factor in Conjecture S~~ **(SUPERSEDED at freeze 2026-08-26)** — the Corner-C soft factor is written `𝖲`; bare `S` with momentum arguments is reserved for the Bethe amplitudes `S_{12}`, `S_{21}`, `S_phys` | definitions.md D25 |
| `R(k)` | ~~soft-theorem remainder~~ **(SUPERSEDED at freeze 2026-08-26)** — soft-theorem remainders are **always subscripted** (`R_δ`, `R_S`, `R_{S2}`); bare `R(k)` with a momentum argument is the kink--magnon **reflection probability** `1 − T(k)` | definitions.md D15 (the D20 pointer lapsed with the 2026-08-26 SPT rebuild) |
| `δx` | kink collective-coordinate displacement (memory observable); the precise definition is the windowed bond charge `𝔛_W` of D13(a) | definitions.md D13(a) |
| `H`, `h_{x,x+1}`, `J`, `P_{x,x+1}` | shifted isotropic spin-1/2 Heisenberg-ferromagnet Hamiltonian, bond term, positive exchange, and spin swap | definitions.md D6 |
| `N` | number of sites when the chain is specialized to a periodic ring | definitions.md D6 |
| `\|Ω⟩`, `\|x⟩`, `\|x,y⟩` | all-up vacuum, one-down-spin basis, and ordered two-down-spin basis | definitions.md D6 |
| `\|k⟩_N` | normalized one-magnon momentum state on an `N`-site ring | definitions.md D6 |
| `k`, `z(k)` | lattice momentum in `(−π,π]` and `exp(ik)` | definitions.md D6 |
| `ω(k)`, `v(k)` | one-magnon energy and group velocity `dω/dk` | definitions.md D6 |
| `λ(k)` | Heisenberg rapidity `(1/2) cot(k/2)` | definitions.md D7 |
| `ψ(x,y)`, `A_{12}`, `A_{21}` | ordered-coordinate two-magnon wave and its Bethe coefficients | definitions.md D7 |
| `S_{12}`, `S_{21}` | coefficient ratios `A_{12}/A_{21}` and its inverse; generalized from D7's spin-`1/2` model to site spin `S` by Theorem S2-2body-S | definitions.md D7; theory/spin-s-twomagnon.md |
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
| `c_0(ℤ)` | profiles vanishing at infinity; the class in which the **gauge remainder** `𝔅_Λ` vanishes in norm — **not** a class in which either side of the SBP identity converges (that needs `ℓ¹∩BV`, D12(a′), and the SKETCH split-property box).  *(Corrected at freeze; `corner-a-r3.md` residue 3.)* | definitions.md D12(a) |
| `PGL(χ)`, `PU(χ)` | projective (unitary) group on the virtual space `ℂ^χ` | definitions.md D4(b) |

Conventions: chain sites x ∈ ℤ; momenta k ∈ (−π, π]; ħ = 1; the
Heisenberg FM uses the vacuum-energy shift fixed in D6; XXZ anisotropy
Δ = J_z/J_⊥.

**Deliberate overloads (flagged; L4 requires that each carry a disambiguation
rule that can be applied mechanically).**

1. `ω` with a *momentum* argument, `ω(k)`, is the magnon dispersion (D6, D16);
   `ω` with *two group* arguments, `ω_α(g,h)`, is the projective 2-cocycle
   (D2(c)), whose class is the `[ω]` row above.  Argument types never coincide.
2. **`χ`** — bond dimension (D1(b)) *versus* `χ := sgn(v_h − v_s)` in the
   oracle's soft expansion (`oracle-bethe.md` ⟨1⟩3.⟨2⟩1, frozen).  This is a
   genuine collision: both are bare symbols.  **Rule:** `χ` means the bond
   dimension **everywhere in this repo except inside `oracle-bethe.md` ⟨1⟩3**,
   where it is local to the derivation of (12)--(13).  Outside that step the
   sign is written `sgn(v_h − v_s)` in full — as O7, O8 and O9 already do — and
   `TRIANGLE.md` and the paper use only the spelled-out form.  Do not import
   `χ` as a sign into any other shard.
3. **`T`** — a *decoration tuple* only inside `|ψ_Λ(T;·)⟩` and `ω_A[T]`
   (D1(e)); the *transitivity hypothesis* only as the parenthesised `(T)`
   (D9(d)); the kink--magnon *transmission probability* only with a momentum
   argument, `T(k)` (D15).  No two of these share a syntactic position.
4. **`R`** — a finite *interval* `R = [a,b]` (D3(b)); the *range* of `H` as
   `R_h` (D10(a)); the *reflection probability* `R(k)` (D15).  Soft-theorem
   remainders are always subscripted (`R_δ`, `R_S`, `R_{S2}`) and never bare.
5. **`s`** — the *physical index* only as a tensor super/subscript or basis
   label (`A^s`, `|s⟩`, `s_x`, D1(b)); the *site spin* only as a standalone
   scalar with `d = 2s+1` (D13--D16).
6. **`q`** — the *charge density* only with a site subscript and a `𝔤`
   argument, `q_x(ξ)` (D10); the *XXZ deformation parameter* only bare,
   `q = Δ − \sqrt{Δ^2−1}` (D16); a *relative momentum* only inside
   `ml2-completeness.md` ⟨1⟩3--⟨1⟩5 and `oracle-bethe.md` ⟨1⟩3.⟨2⟩3.⟨3⟩3, where
   it is local to those steps.
7. **`X`** — `X_α(ξ)` and bare `X ∈ M_χ(ℂ)` are virtual/tangent matrices
   (D2(e), D5(b)); `X = \cos q` is local to `ml2-completeness.md` ⟨1⟩3;
   `X_1(t)` is the first-moment wall coordinate (D13(c)); `𝔛_W` (fraktur) is
   the windowed wall-position observable (D13(a)) and is a *different glyph*.

*Overloads 8--12 were introduced by the 2026-08-26 rebuild of D19--D23; the
rules below only record how the rebuilt text already uses each symbol, and are
part of what critic r2 should check.*

8. **`E`** — the transfer map and its contractions carry an *operator or
   tensor-content* subscript, `E`, `E_O`, or `E_b` for the transfer map of the
   tensor `A_b` (D1(b),(d), D19, D23).  The bound-pair energy is always the
   function `E_b(K)`, with its momentum argument displayed (D7); bare `E_b`
   occurs only in the local SPT transfer calculation.  The fixed endpoint
   **Schmidt/edge register space** `E_C := ℂ^χ` carries a tensor-label
   subscript and appears only in register positions such as `End(E_C)`,
   `→E_C`, or `E_C⊗E_C^*` (D19, D21).
9. **`X`, `Y`, `Z`** (extends 7) — bare `X, Y, Z` are the Pauli matrices
   inside the explicit D23 comparison tensors and the contractions built from
   them (`A_b^x = a_bX`, `V_T = (I,Z,I,Z)`, `ℜ_{A_b,L}(S^z) → −Z/2`); the
   virtual/tangent matrices of 7 keep their argument form `X_α(ξ)`, `X_C(ξ)`.
10. **`q`** (extends 6) — the *charge-lattice offset* `q_ω(ξ)` carries the
    cocycle-class subscript `ω` (D21); the charge density keeps its site
    subscript `q_x(ξ)` (D10).
11. **`r`** — bare `r` is the right fixed point of the transfer map (D1(c),
    D19, D23), except inside D7's ordered-coordinate bound-pair paragraph and
    its direct ML2/oracle descendants, where the explicitly local declaration
    `r:=y−x` makes it the integer relative separation.  The kink--magnon
    reflection *amplitude* always carries a momentum argument, `r(k)` (D15).
12. **`T`** (extends 3) — with physical superscripts and a family parameter,
    `T_t`, `T_t^x`, `T^z`, it is the D23 injective `χ=2` trivial comparison
    tensor (`TRIV₂`); no other reading of `T` takes that position.

All other symbols are unique.

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

---

## Rows appended at the freeze, 2026-08-26

*Closes `verdicts/oracle-bethe-r2.md` residue 2 (the oracle's soft-expansion
symbols) and covers definitions D13--D23.  Nothing was renumbered or deleted;
two rows above are marked SUPERSEDED in place (`S(k;·)`, `R(k)`).*

**Bethe-oracle soft-expansion residue (oracle-r2 MINOR 2).**

| Symbol | Meaning | First fixed in |
|---|---|---|
| `ω_h`, `v_h` | hard-magnon energy `ω(k_h)` and group velocity `v(k_h)` | definitions.md D8 |
| `v_s` | soft-magnon group velocity `v(k_s)` | definitions.md D8 |
| `sgn(v_h−v_s)` | channel sign selecting the physical out/in ratio; written `χ` **only** inside `oracle-bethe.md` ⟨1⟩3 (see overload 2 above) | oracle-bethe.md ⟨1⟩3.⟨2⟩1 |
| `S_phys` | the physical channel amplitude: `S_{12}` if `sgn(v_h−v_s)=+1`, else `S_{21}` | oracle-bethe.md ⟨1⟩3.⟨2⟩1 |
| `δ_phys` | the continuous phase branch of `S_phys` vanishing at `k_s = 0` | oracle-bethe.md ⟨1⟩3.⟨2⟩1 |
| `Δλ` | rapidity difference `λ(k_s) − λ(k_h)`; `S_{12} = (Δλ+i)/(Δλ−i)` | definitions.md D7, oracle-bethe.md (8) |
| `R_δ`, `R_S` | remainders of the `δ_phys` and `S_phys` expansions, bounded by `C_δ(a,b)\|k_s\|³`, `C_S(a,b)\|k_s\|³` on `D_{ab}` | oracle-bethe.md ⟨1⟩3.⟨2⟩3 |
| `C_δ(a,b)`, `C_S(a,b)`, `D_δ(a,b)`, `D_S(a,b)` | explicit Taylor--Lagrange remainder constants; `C = Θ(a^{-2})` as `a↓0` | oracle-bethe.md ⟨1⟩3.⟨2⟩3, ⟨2⟩5 |
| `ε_{ab}`, `D_{ab}`, `Ω_{ab}` | the compactum on which O7--O10's remainders are uniform | oracle-bethe.md ⟨1⟩3.⟨2⟩3 |
| `j^-_{x,x+1}`, `J^-_k`, `Q_k` (FM) | complexified broken-direction current and charge, `q_x = S^-_x` | soft-current-recon.md ⟨1⟩1 |
| `\|C_K⟩` | adjacent-pair contact vector `Σ_x e^{iKx}\|x,x+1⟩` | soft-current-recon.md (R9) |
| `\|χ_π⟩` | the singular (compactified-rapidity) `K=π` completion state, even `N` | ml2-completeness.md (12) |
| `\mathscr B_K^{D7}`, `\mathscr X_K`, `\mathscr E_K` | the D7-representable fiber family, its singular completion, and their union | ml2-completeness.md (23) |
| `ML1`--`ML6` | the six missing lemmas of the general soft theorem | soft-current-recon.md ⟨1⟩7 |

**Spin-`S` two-magnon theorem (proposer shard `S2-2body-S`).**

| Symbol | Meaning | First fixed in |
|---|---|---|
| `S`, `H_S` | site spin `S∈{1/2,1,3/2,…}` (uppercase local alias of D13's `s`) and the shifted isotropic spin-`S` ferromagnet | theory/spin-s-twomagnon.md Statement |
| `ω_S(k)`, `v_S(k)` | spin-`S` one-magnon dispersion `2JS(1−cos k)` and group velocity `2JS sin k` | theory/spin-s-twomagnon.md Statement |
| `zeta` | local momentum product `z_1z_2` (renamed from bare `P`, which is reserved for the spin swap/product comparator) | theory/spin-s-twomagnon.md ⟨1⟩2 |
| `d(x)` | double-occupancy amplitude on the normalized doubly occupied occupation vector at `x` (`S≥1` only) | theory/spin-s-twomagnon.md ⟨1⟩1.⟨2⟩1 |
| `a`, `b`, `μ` | contact polynomials `1+z_1z_2`, `z_1+z_2`, and `(2S−1)a+b` | theory/spin-s-twomagnon.md Statement |
| `g`, `ρ`, `Σ`, `W` | local contact variables `√[S(2S−1)]`, double-occupancy coefficient, `A+B`, and `Az_2+Bz_1` | theory/spin-s-twomagnon.md ⟨1⟩1--⟨1⟩2 |
| `q_rel`, `c_K`, `n` | relative half-momentum, `cos(K/2)`, and the independent closed-form numerator with `S_{12}=n/(−conj n)` | theory/spin-s-twomagnon.md ⟨1⟩3 |

**Corner B (memory), D13--D18.**

| Symbol | Meaning | First fixed in |
|---|---|---|
| `s` | site spin, `d = 2s+1`; magnetisation jump across a wall is `2s` (overload 5).  **Fence (r2 objection 1):** H-MQG(2) fixes the D13(a) calibration parameter to be the tail density, `s=ρ`; `notation.md`'s `s`-row gloss `d=2s+1` is the fully polarised special case and is NOT a constraint on `ρ` — M-IDX-density (⟨1⟩9) assumes no relation between `ρ` and the on-site dimension | definitions.md D13 |
| `𝔛_W` | windowed wall-position observable, `∈ 𝔄_loc`; the frozen memory observable | definitions.md D13(a) |
| `δx` | wall displacement `ϱ_{t_f}(𝔛_W) − ϱ_{t_i}(𝔛_W)` (supersedes the informal row above) | definitions.md D13(a) |
| `D(x)`, `X_1(t)`, `V_±` | DC weight at site `x`; first-moment wall coordinate; its asymptotic velocities | definitions.md D13(b),(c) |
| `N_T`, `N_R`, `N_W`, `⟨N_T⟩` | transmitted / reflected / in-window magnon number; packet average `∫\frac{dk}{2π}\|φ(k)\|²T(k)` | definitions.md D14 |
| `t(k)`, `r(k)`, `T(k)`, `R(k)`, `δ_t(k)` | kink--magnon transmission/reflection amplitudes, probabilities, transmission phase | definitions.md D15 |
| `h^{XXZ}`, `h^{\rm kink}`, `H_{\rm kink}` | easy-axis bond term, its kink-normalised form, and the summed Hamiltonian | definitions.md D16 |
| `ω_{\rm gap}`, `k_*` | magnon gap `J(Δ−1)`; crossover momentum `1/(4(Δ−1))` | definitions.md D16 |
| `q`, `x_0`, `φ`, `\|K(z)⟩` | XXZ deformation parameter `Δ−\sqrt{Δ²−1}`; kink centre; conjugate `U(1)` phase; exact kink product family (overload 6) | definitions.md D16 |
| `𝒦^{(1)}_{αβ}` | the `ℓ¹` refinement of `𝒦_{αβ}` on which half-line charges converge | definitions.md D17 |
| `(H-AD)` | coherent wave-operator/channel/local-decay hypothesis AD1--AD4 for the selected kink+magnon sector; the former norm-mixture reading is superseded | definitions.md D18 |
| `𝔮^L_c`, `𝔮^R_c` | half-line regularised charges `Σ_{x<c}(S^z_x−s_α)`, `Σ_{x>c}(S^z_x−s_β)` | definitions.md D17, claim B3 |
| `σ_k`, `σ_x` | wave-packet momentum and spatial width | definitions.md D14 |

**SPT, D19--D23** *(rebuilt 2026-08-26 from `theory/spt-rebuild.md`; these rows
follow the rebuilt definitions, and the pre-rebuild symbols are marked
SUPERSEDED in place rather than deleted).*

| Symbol | Meaning | First fixed in |
|---|---|---|
| `𝒞_C^{(n)}`, `E_C` | normalized boundary transfer compression `r^{-1/2}E_O(r)r^{-1/2}`, and the fixed finite Schmidt/edge register `ℂ^χ` it acts on | definitions.md D19 |
| `𝓜_χ(C)` | padded-window matrix module `M_χ(ℂ)≅E_C⊗E_C^*`; under left multiplication it is `χ` copies of the `E_C` projective action | definitions.md D21 |
| `f_{L,κ}^{bulk}`, `f_L^{edge}`, `g_L^{edge}`, `ǔ_C(g)` | bulk packet, edge profile, finite-group endpoint profile, and the normal-ordered on-site operator `e^{-iθ_C(g)}u(g)` | definitions.md D19 |
| `𝔉_{N,L}^{bulk}(ξ)` | operator-valued bulk soft insertion between the fixed channel registers | definitions.md D20 |
| `Q^{H}[f;ξ]`, `X_C^∘(ξ)` | Hermitian modulated charge `-iQ[f;ξ]`, and the phase-gauge-invariant centered virtual generator `X_C-tr(rX_C)I` | definitions.md D20--D21 |
| `ℜ_{C,L}(ξ)`, `𝕊_{C,L}^{comp}(g)`; `ℜ_C`, `𝕊_C` | registered Hermitian edge (Lie) residue and compensated endpoint group residue, and their operator-norm limits | definitions.md D20 |
| `F_{C,L}^{edge}(e',e;ξ)` | scalar edge form factor — a matrix element of `ℜ_{C,L}`, never itself algebra-valued | definitions.md D20 |
| `(H-soft-p)` | uniformity of the soft limit through `p` derivatives, required before a coefficient of order `p` exists | definitions.md D20 |
| `H_{\rm edge}`, `J_C`, **(H-split)** | physical half-chain edge space, the intertwining isometry `E_C → H_edge`, and the hypothesis that supplies them — **register caveat**: this is still the SKETCH split-property box, corner-a.md ⟨1⟩4.⟨2⟩9 | definitions.md D21 |
| `d_ω` | minimal dimension of an `ω`-projective irrep of `G`; a nontrivial class has `d_ω>1` | definitions.md D21 |
| `ν_ω`, `q_ω(ξ)`, `q_{ω,C}^∘(ξ)`, `Q_edge(ξ)` | central character, the lift-dependent raw offset, the gauge-invariant centered offset, and the Hermitian centered endpoint charge `-iX_C^∘(ξ)` with spectrum in `q_{ω,C}^∘(ξ)+ℤ` | definitions.md D21 |
| `ΔQ_edge`, **(H-dress)**, **(H-AD-edge)** | edge memory operator `W_+^†Q_edgeW_+ - W_-^†Q_edgeW_-`, and the dressed-endpoint / asymptotic-decomposition hypotheses it requires | definitions.md D22 |
| `A_b`, `T_t`, `P` | the symmetric AKLT path (`A^a=σ_a/√3` at `b=1/√3`), the injective `χ=2` `D₂`-trivial tensor, and the `χ=1` `O(2)` product comparator | definitions.md D23 |
| `Γ_2^C`, `W_2^C`, `h_C`, `h_{∂,C}`, `H_{C,+}` | length-two range map, its isometry, the parent bond term, the boundary term, and the half-chain parent Hamiltonian | definitions.md D23 |
| `Ad(V_α(g))` | conjugation action `V(·)V^{-1}`; it carries no projective multiplier, but is **not** `[ω]`-blind as a representation (SPT-B'(iii)) | corner-a.md ⟨1⟩4.⟨2⟩4; theory/spt-rebuild.md ⟨1⟩3.⟨2⟩3 |
| `𝖲` (SPT sense), `F_f(ξ;β,α)`, `F_f(g;β,α)`, `m_L`, `Δm_L` | **(SUPERSEDED by the 2026-08-26 rebuild)** the pre-rebuild SPT soft factor, soft form factor, and edge memory observable; the rebuilt objects are `𝕊_C`/`ℜ_C`, `F_{C,L}^{edge}`, and `ΔQ_edge`.  `𝖲(k_s;{q_i,v_i})` in the **Corner-C** sense (claim `S-general`) is a different object and is unaffected | definitions.md D20--D22 (rebuilt); Corner-C `𝖲`: definitions.md D25 |
| `𝖲(k_s;{q_i,v_i})` | Corner-C proposed soft multiplier on the D24(d) class `𝒮_W`; existence and universality remain claim `S-general` (CONJECTURE) | definitions.md D25 |

**ML4 / ML5 / M-quant (added at the freeze with the summit shards).**

| Symbol | Meaning | First fixed in |
|---|---|---|
| `I = [a,b] ⋐ (0,π)`, `ε_I` | the hard-momentum window and its soft radius (`h+k ∈ (0,π)`, `v(h)>v(k)`, `h+k ≠ π`) | ml4-ward-reduction.md ⟨1⟩1 |
| `‖g‖_{I,N}`, `f_ε(k)=ε^{-1/2}f(k/ε)` | discrete hard-packet norm; rescaled soft packet | ml4-ward-reduction.md (1) |
| `D_{n,N}`, `P_{n,N}`, `R_{n,N}` | `Q_0` restricted to `ℋ_{n,N}`; the orthogonal projection onto its range; the orthogonal current `(1−P_{n,N})J^-_0` | ml4-ward-reduction.md (2) |
| `Γ_N(k)`, `𝒜_{⊥,N}(k;f,g)` | off-shell analytic interpolation at fixed periodic `N`, transported to the `k=0` fiber; the orthogonal contribution to the Ward-reduced numerator | ml4-ward-reduction.md (3), (12) |
| **ML4-A** | the standalone cancellation lemma: `Γ(0)=U` (energy-shell channel matching) + `C¹` trace regularity ⟹ `‖b(k)Γ(k)^†R‖ ≤ C_bC_Γ‖J‖k²` | ml4-ward-reduction.md ⟨1⟩2 |
| `J^z_0`, `S^±` | the `z`-current and global raising/lowering operators of the exact Ward projection.  **The scalar form `P_{n,N}J^-_0 = \frac{2}{N-2n}Q_0J^z_0` holds ONLY at `n=1`** (ERRATUM 2026-08-28, bd `tns-uxr`): for `n≥2` it is REFUTED, because `J^z_0ψ ∉ ker S^+` when `‖J^+_0ψ‖≠0`.  The form valid at every `n` is `P_{n,N}J^-_0 = 2D_{n,N}A_n^{-1}J^z_0` with **`A_n := D_{n,N}^†D_{n,N}` on the FULL sector `ℋ_{n,N}`** (where `A_n` is non-scalar); in the highest-weight-restricted register `D_λ=Q_0|_{ker S^+}` one has `A_λ=(N-2n)𝟙` and the same string collapses back to the refuted display unless `J^z_0` is first projected, the correct hw-register form being `(1/m_λ)Q_0Π_{hw}J^z_0`, `m_λ=(N-2n)/2` | ml4-ward-reduction.md (8)--(11); `theory/checks/ml4_ward_n2_check.py`; `theory/verdicts/ml4-ward-n2-audit.md` §1.2 |
| `‖O‖_μ`, `M_1^O`, `M_2^O` | exponentially-quasi-local source norm; amputated one-hard and hard-plus-soft amplitudes | definitions.md D24(a),(b) |
| `𝔠_h(O)` | the contact first jet; ML5-A requires both `M_2^O(0)=0` and `𝔠_h(O)=0`, with the D24(c) second-derivative norm control | definitions.md D24(c) |
| `𝒮_W` | the five-condition Ward/LSZ/no-contact source class in the repaired conditional ML5-B implication | definitions.md D24(d) |
| `D`, `O_η` | the four-site refuting source; `M_1` fixed, linear soft coefficient shifted | definitions.md D24(e) |
| `V_int` | four-site ML5-A intercept counterexample: `M_1=0`, zero first jet, nonzero `M_2(0)` | definitions.md D24(e) |
| `χ(h,k)` | `sgn(v(h)−v(k))` — the *spelled-out* channel sign (see overload 2) | ml5-universality.md ⟨1⟩1 |
| `W_±`, `ℋ_as`, `ℋ_b`, `ℋ_sc`, `P_L`, `P_T` | Møller wave operators; channel space; bound and scattering subspaces; reflected/transmitted channel projections | definitions.md D18, memory-quantization.md §2 |
| `N_T` (operator), `ΔX` | the transmitted-channel projection `W_+P_TW_+^*`, and the displacement operator `0·P_L − (1/s)P_T` conjugated to `ℋ_sc` | memory-quantization.md (Mq.6), §4 |
| `P_3`, `H_3 = P_3HP_3` | the `≤3`-domain-wall projection and the projected kink+magnon dynamics | memory-quantization.md §3 |
| `m_0(z)` | the free half-line Jacobi Weyl function `[(z−E_c)²−J²]^{-1/2}` used in the Feshbach spectral analysis of `H_3` | memory-quantization.md ⟨1⟩3.⟨2⟩2 |
| `ε_AD`, `ε_num` | the charge-decomposition defect and the numerical error in the finite-window memory budget (Mq.11) | memory-quantization.md §5 |
| `Q̂_{W,c}` | regularised fixed-window wall charge `2s(𝔛_W-c)`; a bounded local observable | definitions.md D27; theory/memory-index.md (IDX.1) |
| `E_{W,t}`, `𝒟_{W,t}` | spectral resolution of `Q̂_{W,c}(t)` and its nonselective spectral-dephasing map | definitions.md D27 |
| `p_{W;t_-,t_+}`, `p_ν`, `ΔQ_W` | finite-window TPM escaped-charge law, its ordered D27 limit, and the measured window-charge increment; convention fixed once: `ν=-ΔQ_W=q_--q_+` | definitions.md D27; theory/memory-index.md §0, ⟨1⟩5--⟨1⟩7 |
| `ρ` (density) | common unbroken-circle tail density `ω_α(S^z)=+ρ=-ω_β(S^z)`; a real parameter, deliberately distinct from D13's site-spin `s`.  H-MQG(2) fixes the D13(a) calibration parameter to be the tail density, `s=ρ`; `notation.md`'s `s`-row gloss `d=2s+1` is the fully polarised special case and is NOT a constraint on `ρ` — M-IDX-density (⟨1⟩9) assumes no relation between `ρ` and the on-site dimension.  Overload note: `ρ` is file-local to theory/spin-s-twomagnon.md ⟨1⟩1--⟨1⟩2 as the double-occupancy coefficient; `κ_{W,c_0}` is the finite-window coset offset | theory/memory-index.md ⟨1⟩9 |
| `Q_W^α`, `Q_W^β`, `μ_∞^α` | tail-specific vacuum-normal-ordered window charges `Σ_{x∈W}(S^z_x∓ρ)` and the limiting vacuum charge law `(2π)^{-1}∫e^{-iθν}\|tr(V_θr)\|²dθ` | theory/memory-index.md ⟨1⟩11 |
| `δx` (asymptotic) | the D27-defined ordered asymptotic value of D13(a)'s observable; the finite-time `δx` of D13(a) is unchanged (overload flagged per memory-index-r1 NOTE 5) | definitions.md D27 |
| `Γ_K`, `Γ_{M,γ}` | **(D28 sense)** exact Gram-normalized kink and tail-magnon band maps assumed by H-ACE | definitions.md D28 |
| `Γ_M` | **(D31 sense, distinct from `Γ_{M,γ}` above)** the exact Gram-normalized translation-covariant scalar magnon band map over the single D31 vacuum, `Γ_M:L²(𝕋;ℂ^m)→H_A` with `HΓ_M=Γ_M(ω⊗1_m)`; no `γ` tail index and no kink sector.  Overload registered 2026-08-29 per ansatz-scattering-2m-r6.md R6-O1 | definitions.md D31(2) |
| `E_K`, `K_-`, `K_+`, `W_K`, `Δ_M` | kink dispersion, its extrema and bandwidth, and the selected magnon gap | definitions.md D28 |
| `χ_K,χ_γ,χ̃_K,χ̃_γ` | momentum filters and their companions fixing the filtered frames and kernels | definitions.md D28(3),(4) |
| `h_K,h_γ` | filtered hopping kernels (Fourier coefficients of `E_Kχ̃_K`, `ω_γχ̃_γ`); rapidly decreasing | definitions.md D28(4) |
| `κ_a(x)`, `κ_a^{(0)}(x)` | filtered and unfiltered exact kink Wannier vectors | theory/ansatz-scattering.md (C2) |
| `θ_c` | fixed smooth monotone channel cutoff, transition width `w` | theory/ansatz-scattering.md ⟨1⟩5.⟨2⟩1 |
| `ε_v`, `d_abs`, `Θ_inel`, `η_inel` | **(D28 sense)** velocity gap, same-kink absorption gap, known inelastic threshold, and its margin (last three: fence only, Remark D28-R).  `ε_v`, `Θ_inel`, `η_inel` are re-bound in the **D31 sense** in the D31 rows below — the two senses are distinct and must be read from the citing definition (overload resolved 2026-08-29 per ansatz-scattering-2m-r6.md R6-O1) | definitions.md D28 |
| `D_-^L`, `D_+^L`, `D_+^T` | incoming-left, outgoing-left, and outgoing-transmitted fixed-packet domains | definitions.md D28 |
| `H_out^{ex}`, `N_T^{ex}` | constructed outgoing range and its transmitted-channel projection; no completeness implied | theory/ansatz-scattering.md ACE.2 |
| `ℋ_{0,12}`, `H_{0,12}`, `𝒟_{12}` | labeled two-packet free magnon channel, sum Hamiltonian, and smooth product core.  **Pointer referred (orchestrator, 2026-08-29):** the merged D31 text does not itself introduce these three symbols — they are fixed in the shard only.  Recorded for adjudication rather than silently re-pointed; see bd `tns-uz8` | theory/ansatz-scattering-2m.md (D31 pointer under review) |
| `K_i`, `V_i`, `a_{i,b}(n)`, `χ_i`, `χ̃_i`, `h_i` | fixed packet supports, velocity supports, exact filtered creators, filters/companions, and rapidly decaying filtered symbols | definitions.md D31 |
| `I_2`, `𝓡_inel`, `Θ_inel`, `η_inel`, `E_{B,j}`, `d_B`, `P_B` | selected two-magnon joint energy--momentum set, inventoried alternative channels and threshold/margin, bound bands, their fiberwise separation, and bound projection | definitions.md D31 |
| `d_sep` | number of uniform transfer sites separating two local/almost-local clusters in D31-C2/C4 | definitions.md D31 |
| `ε_v`, `ε_0`, `s_N(F)` | D31 packet-velocity separation, distance of each packet velocity from zero (unused by A2M.1--A2M.2), and fixed-packet Schwartz seminorm | definitions.md D31(4); theory/ansatz-scattering-2m.md ⟨1⟩2 |
| `V_w`, `Ψ_O` | block Stinespring isometry and block-to-virtual contraction used in MPS-2M-cluster | theory/ansatz-scattering-2m.md ⟨1⟩3.⟨2⟩2 |
| `f_ε`, `Q[f̂_ε;ξ^-]`, `a_{2,b}[f_ε]`, `a_{Q,2,b,t}[f_{ε,t}]` | rescaled momentum packet, D10(c) fixed-time charge with its position-space Fourier profile, exact filtered packet creator, and separate asymptotic charge HR creator (not the adjudicated D29 object) | theory/ansatz-scattering-2m.md ⟨1⟩2, ⟨1⟩8 |
| `𝒜_α`, `𝒝_α`, `𝒟_α`, `d_I`, `C_I` | D29 full-index amputated datum, numerator, hard denominator, and its selected-packet lower/numerator bounds | theory/ansatz-scattering-2m.md ⟨1⟩8(3) |
| `A_j(ε)`, `ε_★` | post-`N,t` D29 datum along the joint `(W_j,σ_j)` exhaustion and its soft-scale interval endpoint | theory/ansatz-scattering-2m.md ⟨1⟩8 `(ACE2M-SR)` |
| `(ACE2M-LSZ)` | theorem that fixed-`ε` connected on-shell pairings are independent of the asymptotic soft creator when (2M-1P) and cross-velocity separation hold; it does not apply to the adjudicated D29 | theory/ansatz-scattering-2m.md ⟨1⟩8.⟨2⟩2 |
| `(SR)[X]`, `(ACE2M-SR)` | the three-clause schema (`C¹` extension to `ε=0`, relatively compact jet, uniform equicontinuity) applied to an arbitrary `L²(I)`-valued `ε`-family `X`; `(ACE2M-SR)` is `(SR)[A_j]` for the adjudicated D29 datum together with existence of its `N,t` limits — a genuine non-Cook soft-uniformity hypothesis.  `(SR)[A]` for the one-element constructed-channel datum is not an instance of `(ACE2M-SR)` | theory/ansatz-scattering-2m.md ⟨1⟩8 |
| `P^{DW}_x`, `N_{DW}` | the domain-wall bond projection onto `span{\|↑↓⟩,\|↓↑⟩}_{x,x+1}`, and the domain-wall **number** `N_{DW}:=Σ_xP^{DW}_x`.  Written `D` in `theory/lr-d16.md`; renamed here because `D(x)` is already D13(b)'s DC weight (L4).  Distinct from `P_3`, the `≤3`-domain-wall projection of `memory-quantization.md` | claims `LR-D16-EDW`; theory/lr-d16.md ⟨1⟩5.⟨2⟩6 (entry owed by lr-d16-r2.md m4, supplied by the orchestrator with the row) |
