<!-- ROLE: the argument DAG (L5). One row per claim. Status upgrades only after
     the L6 proposer/critic loop converges; verdict files live in theory/.
     Statuses: PROVED | SKETCH | CONJECTURE | REFUTED. -->

# Claims DAG

| id | statement (short) | status | depends on | proved in | tested in |
|---|---|---|---|---|---|
| WI | Truncated symmetry acts as two boundary virtual insertions (exact) | SKETCH | D1–D3 | — | — |
| A1 | 𝒜 = (G_L×G_R)/G_diag acts on superselection sectors; unbroken case: relabels charge sectors; class [ω] = SPT index is the central extension of the charge algebra | SKETCH | WI, D4 | — | — |
| A2 | Broken case: 𝒜-orbit = vacuum pairs (α_L, α_R); half-infinite truncated symmetry creates a kink (kink = contact term of broken truncated symmetry) | SKETCH | WI, D4, D5 | — | — |
| G0 | k = 0 magnon tensor B_G = d/dε [u·A] is pure gauge (B = AX − XA, X = V′(0)) | SKETCH | D2, D5 | — | — |
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
