<!-- ROLE: the argument DAG (L5). One row per claim. Status upgrades only after
     the L6 proposer/critic loop converges; verdict files live in theory/.
     Statuses: PROVED | SKETCH | CONJECTURE | REFUTED. -->

# Claims DAG

| id | statement (short) | status | depends on | proved in | tested in |
|---|---|---|---|---|---|
| WI | Truncated symmetry telescopes to two boundary-bond insertions: as **window vectors** `U_R(g)\|ψ_Λ⟩ = e^{i\|R\|θ_α(g)}\|ψ_Λ(T_R^{(g)})⟩` with `V_α(g)^{-1}` on `∂_-R`, `V_α(g)` on `∂_+R`, `A_{g·α}` inside `R` — requiring `Λ ⊇ [a−1,b+1]` **or** D1(e) edge-bond insertions; as **states**, the same with **no phase** | PROVED | D1–D3 | theory/corner-a.md ⟨1⟩3 | theory/checks/corner_a_check.py C1, C1b, C2, C2b |
| A1 | Unbroken case, normal ordered. (a) Half-infinite strings act on states **exactly** as single bond insertions; (b) they are implemented by **no** strongly convergent operator sequence **iff `V_α(g)` is non-scalar** (for scalar `V_α(g)` the strings stabilise exactly); (c) `ω^{M@b}=ω^{M'@b} ⟺ M'∈ℂ^×M`, so the endpoint space is a `PGL(χ)`-torsor; (d1) **on windows padded about the bond** (≥ `n_0` sites each side, `b_l,b_r≠0`) `𝔞_α=ℂ_{ω_α}[G]` acts linearly on window vectors — **padding is necessary**, the unpadded action is ill defined; (d2) the **state**-level action is the homomorphism `ρ_α: G→PGL(χ)`, `ker ρ_α = N_α`; (d3) `[ω_α]` obstructs **removing the multiplier**, i.e. lifting `ρ_α` to an honest `G→U(χ)` — it does **not** obstruct the projective window action, which always exists; (e) stabiliser `S_α ⊇ G_diag` (= `G_diag` iff `N_α={e}`), orbit `𝒜_eff = G/N_α`, **not** `𝒜` | PROVED (padded-window level + state level) | WI, D4, D12 | theory/corner-a.md ⟨1⟩4 | theory/checks/corner_a_check.py C6, C8, C8b |
| A2 | Broken case, per fixed `g ∉ H_α`: every finite `R` stays in `𝒦_{αα}`; the half-infinite limit exists **in weak-\* only**, rate `λ̃^{y−w}` for any `λ̃∈(λ_E,1)`, and lands in `𝒦_{α,g·α}`, disjoint from the vacuum folium (**sector jump**). **Under hypothesis (T)** (`G` transitive on `Ω_vac`; otherwise per `G`-orbit) vacuum pairs form `(G/H_α)×(G/H_α)` with stabiliser `H_α×H_β`, and the complete diagonal invariant is the **double coset** in `H_α\G/H_α` | PROVED | WI, D4, D5, D9, D1(e′) | theory/corner-a-kinks.md ⟨1⟩8–⟨1⟩9 | theory/checks/corner_a_check.py C7, C11 |
| G0 | (a),(b) **for `ξ ∈ 𝔥_α`, normal ordered**: `B_G(ξ)` is pure gauge at `k=0` **iff `ξ` is unbroken** (broken case = failure of *same-vacuum return*, **not** of (IT)); (c) the **exact finite-window** identity is `\|Φ_k^Λ(B_G)⟩ = (1−e^{ik})Σ_{m=a}^{b−1}e^{ikm}\|ψ;X@m⟩ + e^{ikb}\|ψ;X@b⟩ − e^{ika}\|ψ;X@(a−1)⟩`, and the clean form `(1−e^{ik})\|Φ_k(A_αX_α(ξ))⟩` holds **only** in the D12(b) δ-normalised sense; for decaying profiles the correct statement is the real-space SBP identity with `f ∈ ℓ¹∩BV` (D12(a′)), not a fixed-`k` equation; (d) lattice Noether `q_x▹ω_α = (𝒥_{x\|x+1}−𝒥_{x−1\|x})▹ω_α` exact (`ξ ∈ 𝔥_α`, normal ordered); (e) continuity equation `[H,Q[f;ξ]]=Σ_x(Δf)(x)j_{x\|x+1}(ξ)` for **any** `ξ ∈ 𝔤` and **finite range** `H` via the cut current | PROVED | D2, D5, D10, D11, D12 | theory/corner-a-goldstone.md ⟨1⟩5–⟨1⟩7 | oracle O1 rederived ⟨1⟩7.⟨2⟩3; checks C3, C3b, C4, C5, C9, C10 |
| A2-orbit-r1 | r1 form of A2(e): the `𝒜=(G_L×G_R)/G_diag` orbit is the set of vacuum pairs, labelled by `[g_Lg_R^{-1}]` | **REFUTED** | — | disproved: theory/corner-a-kinks.md ⟨1⟩9.⟨2⟩5.⟨3⟩3 | theory/checks/corner_a_check.py C7 |
| G0-soft-r1 | r1 form of G0(e): the factor `(e^{ik}−1)` is a **universal soft factor**, giving an Adler zero and forcing oracle O7/O9's hard-independent linear coefficient | **RETRACTED** (was overclaimed; hard data can enter at `O(k)` through `J_k`) | — | withdrawn: theory/corner-a-goldstone.md ⟨1⟩6.⟨2⟩7 | — |
| S | Lattice soft theorem (Conjecture S): M_{n+1}(k) = S(k;{q_i,v_i}) M_n + R(k), S universal, Adler zero S → 0 | CONJECTURE | G0, WI, A1 | — | — |
| S2 | Minimal core: S for M1 (Heisenberg FM) magnons, n = 2 | CONJECTURE | S | — | — |
| M | Lattice memory formula (Conjecture M): kink displacement δx = DC limit of soft factor summed over event | CONJECTURE | S, A2, D-δx | — | — |
| B3 | B ⇒ A edge: memory is valued in the vacuum-pair label of D9(d) — **under (T)**, a point of `(G/H_α)×(G/H_α)`, whose global-symmetry-invariant content is the double coset in `H_α\G/H_α`.  (Was: "valued in the 𝒜-orbit of vacua" — that phrasing cited `A2-orbit-r1`, now REFUTED, and is withdrawn.  Whether *memory* is this label, and in which topology, is not yet proved) | SKETCH | A2 | — | — |
| SPT | SPT-modified soft theorem (AKLT): soft expansion carries [ω] — OR proven vacuous | CONJECTURE | S, A1 | — | — |
| OR1 | Oracle: Bethe two-magnon S-matrix expansion matches predicted universal coefficient | CONJECTURE | S2 | — | — |
| OR2 | Oracle: Dyson k → 0 decoupling consistent with S | CONJECTURE | S | — | — |
| N1 | Numerics: excitation-ansatz magnon amplitudes reproduce Bethe S(k) as k → 0 | CONJECTURE | S2 | — | — |
| N2 | Numerics: wavepacket-through-kink δx matches Conjecture M (XXZ, Δ > 1) | CONJECTURE | M | — | numerics/results/memory-scan-1.json: δx = −2·T exact (0.004 sites); R ∝ 1/(Δk₀)², soft magnon → no memory; R·k₀² = 0.043(3) at Δ=2 |
| M-quant | Memory quantization (empirical, to be proved): δx = −2·T(k₀) exactly, from S^z bookkeeping; soft zero δx → 0 as k₀ → 0 with T ~ (Δk₀)² scaling | CONJECTURE (numerically established) | A2, N2 | — | ditto; refutes "opaque barrier at large Δ" intuition (T → 1 as Δ → ∞) |

Edges of the triangle: A ⇒ C is (G0, WI, A1) → S; C ⇒ B is S → M; B ⇒ A is B3.

Corner A: r1 critic FAIL → **r2 revision** 2026-08-25.  Disposition of all 20
objections: theory/corner-a-r1-response.md.  Numerical backing:
theory/checks/corner_a_check.py (C0–C7, ALL PASS).  Four amendments the
downstream claims MUST absorb:
(i) **`𝒜` is not the classifying object.** Unbroken: the orbit is `𝒜_eff = G/N_α`
    (a group); broken, **under hypothesis (T)** (`G` transitive on `Ω_vac`;
    otherwise per `G`-orbit): vacuum pairs form `(G/H_α)×(G/H_α)` and the
    diagonal invariant is the double coset in `H_α\G/H_α`.  `𝒜 = (G_L×G_R)/G_diag`
    is a group only for abelian `G` and is never the orbit unless `N_α = {e}`.
(ii) **The A ⇒ C edge is NOT supplied by Corner A.** G0(e) is a lattice
    continuity equation; it gives no Adler zero, no universality, and does not
    rederive O7/O9.  Corner C must supply regularity of `⟨out|J_k|in⟩` at `k=0`,
    an LSZ reduction, and a Ward identity for `J_0`.
(iii) **The brief's "k=0 magnon is pure gauge" holds only on unbroken
    directions**; on a broken direction (IT) still holds (target `A_{g·α}`) but
    the same-vacuum return fails.
(iv) **The ansatz gauge identity is not a finite-window identity** — it carries
    two `Θ(1)` boundary terms and holds only in the D12 limits.
Two SKETCH boxes are load-bearing and may not be used silently: the split
property (blocks framing.md's state-space charge algebra) and A2's
continuum-`Ω_vac` uniformity (blocks Corner B on M1).  Full pitfall list:
theory/corner-a-pitfalls.md.  Two drafts (`theory/spt-scoping-draft.md`,
`theory/corner-b-draft.md`) still cite the two retracted/refuted rows; the exact
line references are tabulated in theory/corner-a-pitfalls.md Flag 6, as input
for freeze reconciliation.  Round-2 critic residue and its disposition:
theory/corner-a-r2-response.md.

Corner A L6 loop: CONVERGED at r3 — PASS (theory/verdicts/corner-a-r3.md, 4 MINOR wording notes only). Rows WI/A1/A2/G0 statuses are final as stated.
