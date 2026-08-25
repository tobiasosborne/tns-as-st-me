<!-- ROLE: the argument DAG (L5). One row per claim. Status upgrades only after
     the L6 proposer/critic loop converges; verdict files live in theory/.
     Statuses: PROVED | SKETCH | CONJECTURE | REFUTED. -->

# Claims DAG

| id | statement (short) | status | depends on | proved in | tested in |
|---|---|---|---|---|---|
| WI | `U_R(g)ω_α` = phase `e^{i\|R\|θ_α(g)}` × the state with `A_{g·α}` inside `R` and `V_α(g)^{-1}`, `V_α(g)` on the two boundary bonds (exact, all `R`, all windows) | PROVED | D1–D3 | theory/corner-a.md ⟨1⟩3 | — |
| A1 | Unbroken case: half-infinite strings act on states (weak-*, exactly) as single bond insertions, not by any strongly convergent operator; the bond implementers form the twisted group algebra `𝔞_α = ℂ_{ω_α}[G]` with central extension `[ω_α] ∈ H²(H_α,U(1))` = SPT index; `G_L×G_R` acts with stabiliser `G_diag`, orbit `𝒜 ≅ G` (a **group only if `G` is abelian**); `𝒜` relabels string-endpoint (twisted) sectors, not the `𝒦_{αβ}` label | PROVED | WI, D4, D9 | theory/corner-a.md ⟨1⟩4 (completeness of `[ω_α]` cited not proved; normality of endpoint states SKETCH in ⟨1⟩4.⟨2⟩9, unused) | — |
| A2 | Broken case: every finite `R` stays in `𝒦_{αα}`; the half-infinite limit exists **in weak-\* only**, with rate `λ_E^{y-w}`, and lands in `𝒦_{α,g·α}`, disjoint from the vacuum folium — the kink is the contact term. `G_L×G_R` acts transitively on `Ω_vac×Ω_vac`; the `G_diag`-invariant label is the relative twist in `𝒜` | PROVED (per fixed `g ∉ H_α`); uniformity over a continuous `Ω_vac` (M1) SKETCH | WI, D4, D5, D9 | theory/corner-a-kinks.md ⟨1⟩8–⟨1⟩9 (SKETCH box: ⟨1⟩10.⟨2⟩3) | — |
| G0 | **Corrected**: `B_G(ξ)` is pure gauge at `k=0` **iff `ξ` is unbroken** (then `B_G = A X_α(ξ) − X_α(ξ)A` after normal ordering, and exactly `\|Φ_k(B_G)⟩ = (1−e^{ik})\|Φ_k(A X_α(ξ))⟩`); for a genuinely broken (Goldstone) direction (IT) fails and `B_G ∉ ran 𝒩_0`. The universal, breaking-proof soft seed is `[H,Q_k(ξ)] = (e^{ik}−1)J_k(ξ)`, prefactor independent of `H`, `ξ`, vacuum, and all other legs — matching oracle O7/O9 (hard-independent linear coefficient) | PROVED | D2, D5, D10, D11 | theory/corner-a-goldstone.md ⟨1⟩5–⟨1⟩7 | oracle O1 re-derived, ⟨1⟩7.⟨2⟩3 |
| S | Lattice soft theorem (Conjecture S): M_{n+1}(k) = S(k;{q_i,v_i}) M_n + R(k), S universal, Adler zero S → 0 | CONJECTURE | G0, WI, A1 | — | — |
| S2 | Minimal core: S for M1 (Heisenberg FM) magnons, n = 2 | CONJECTURE | S | — | — |
| M | Lattice memory formula (Conjecture M): kink displacement δx = DC limit of soft factor summed over event | CONJECTURE | S, A2, D-δx | — | — |
| B3 | B ⇒ A edge: memory is valued in the 𝒜-orbit of vacua (superselection bookkeeping) | SKETCH | A2 | — | — |
| SPT | SPT-modified soft theorem (AKLT): soft expansion carries [ω] — OR proven vacuous | CONJECTURE | S, A1 | — | — |
| OR1 | Oracle: Bethe two-magnon S-matrix expansion matches predicted universal coefficient | CONJECTURE | S2 | — | — |
| OR2 | Oracle: Dyson k → 0 decoupling consistent with S | CONJECTURE | S | — | — |
| N1 | Numerics: excitation-ansatz magnon amplitudes reproduce Bethe S(k) as k → 0 | CONJECTURE | S2 | — | — |
| N2 | Numerics: wavepacket-through-kink δx matches Conjecture M (XXZ, Δ > 1) | CONJECTURE | M | — | — |

Edges of the triangle: A ⇒ C is (G0, WI, A1) → S; C ⇒ B is S → M; B ⇒ A is B3.

Corner A closed 2026-08-25 (P1). Two amendments the downstream claims must
absorb: (i) `𝒜 = (G_L×G_R)/G_diag` is a **coset space**, a group only for
abelian `G` — do not write "asymptotic symmetry group" for `G = SU(2)`;
(ii) the brief's mechanism "the `k=0` magnon is pure gauge" holds only on
**unbroken** directions, so the A ⇒ C edge must run through G0(e)
(`[H,Q_k] = (e^{ik}−1)J_k`), not through the pure-gauge statement. See
theory/corner-a.md §5 for the full pitfall list.
