<!-- ROLE: the argument DAG (L5). One row per claim. Status upgrades only after
     the L6 proposer/critic loop converges; verdict files live in theory/.
     Authoritative L5 statuses: PROVED | SKETCH | CONJECTURE | REFUTED.
     Empirical, conditional, under-review, and future-work qualifiers belong
     in prose, never as additional status values.  Foundation rows with PASS
     verdicts remain frozen; r1-affected rows are pre-r2 and not frozen. -->

# Claims DAG

**SPT status annotation only.**  The SPT rows were **rebuilt 2026-08-26 in
`theory/spt-rebuild.md`; SKETCH pending critic r2** (r1 verdict
`triangle-r1.md` S1--S8).  The old rows SPT-B/E/T/D/M are superseded by
SPT-B'/-E'/-T'/-D'/-M' and SPT-M'-dyn; the withdrawn pointwise bulk-blindness
claim is recorded as REFUTED under `SPT-B-r1`, and the all-orders/all-registers
form of SPT-nogo stays REFUTED.  `definitions.md` D19--D23 were rebuilt in
lockstep from the same merge proposal.  This annotation does not demote the
wanted SPT program.

| id | statement (short) | status | depends on | proved in | tested in |
|---|---|---|---|---|---|
| WI | Truncated symmetry telescopes to two boundary-bond insertions: as **window vectors** `U_R(g)\|ψ_Λ⟩ = e^{i\|R\|θ_α(g)}\|ψ_Λ(T_R^{(g)})⟩` with `V_α(g)^{-1}` on `∂_-R`, `V_α(g)` on `∂_+R`, `A_{g·α}` inside `R` — requiring `Λ ⊇ [a−1,b+1]` **or** D1(e) edge-bond insertions; as **states**, the same with **no phase** | PROVED | D1–D3 | theory/corner-a.md ⟨1⟩3 | theory/checks/corner_a_check.py C1, C1b, C2, C2b |
| A1 | Unbroken case, normal ordered. (a) Half-infinite strings act on states **exactly** as single bond insertions; (b) they are implemented by **no** strongly convergent operator sequence **iff `V_α(g)` is non-scalar** (for scalar `V_α(g)` the strings stabilise exactly); (c) `ω^{M@b}=ω^{M'@b} ⟺ M'∈ℂ^×M`, so the endpoint space is a `PGL(χ)`-torsor; (d1) **on windows padded about the bond** (≥ `n_0` sites each side, `b_l,b_r≠0`) `𝔞_α=ℂ_{ω_α}[G]` acts linearly on window vectors — **padding is necessary**, the unpadded action is ill defined; (d2) the **state**-level action is the homomorphism `ρ_α: G→PGL(χ)`, `ker ρ_α = N_α`; (d3) `[ω_α]` obstructs **removing the multiplier**, i.e. lifting `ρ_α` to an honest `G→U(χ)` — it does **not** obstruct the projective window action, which always exists; (e) stabiliser `S_α ⊇ G_diag` (= `G_diag` iff `N_α={e}`), orbit `𝒜_eff = G/N_α`, **not** `𝒜`.  Scope qualifier: padded-window and state registers as stated. | PROVED | WI, D4, D12 | theory/corner-a.md ⟨1⟩4 | theory/checks/corner_a_check.py C6, C8, C8b |
| A2 | Broken case, per fixed `g ∉ H_α`: every finite `R` stays in `𝒦_{αα}`; the half-infinite limit exists **in weak-\* only**, rate `λ̃^{y−w}` for any `λ̃∈(λ_E,1)`, and lands in `𝒦_{α,g·α}`, disjoint from the vacuum folium (**sector jump**). **Under hypothesis (T)** (`G` transitive on `Ω_vac`; otherwise per `G`-orbit) vacuum pairs form `(G/H_α)×(G/H_α)` with stabiliser `H_α×H_β`, and the complete diagonal invariant is the **double coset** in `H_α\G/H_α` | PROVED | WI, D4, D5, D9, D1(e′) | theory/corner-a-kinks.md ⟨1⟩8–⟨1⟩9 | theory/checks/corner_a_check.py C7, C11 |
| G0 | (a),(b) **for `ξ ∈ 𝔥_α`, normal ordered**: `B_G(ξ)` is pure gauge at `k=0` **iff `ξ` is unbroken** (broken case = failure of *same-vacuum return*, **not** of (IT)); (c) the **exact finite-window** identity is `\|Φ_k^Λ(B_G)⟩ = (1−e^{ik})Σ_{m=a}^{b−1}e^{ikm}\|ψ;X@m⟩ + e^{ikb}\|ψ;X@b⟩ − e^{ika}\|ψ;X@(a−1)⟩`, and the clean form `(1−e^{ik})\|Φ_k(A_αX_α(ξ))⟩` holds **only** in the D12(b) δ-normalised sense; for decaying profiles the correct statement is the real-space SBP identity with `f ∈ ℓ¹∩BV` (D12(a′)), not a fixed-`k` equation; (d) lattice Noether `q_x▹ω_α = (𝒥_{x\|x+1}−𝒥_{x−1\|x})▹ω_α` exact (`ξ ∈ 𝔥_α`, normal ordered); (e) continuity equation `[H,Q[f;ξ]]=Σ_x(Δf)(x)j_{x\|x+1}(ξ)` for **any** `ξ ∈ 𝔤` and **finite range** `H` via the cut current | PROVED | D2, D5, D10, D11, D12 | theory/corner-a-goldstone.md ⟨1⟩5–⟨1⟩7 | oracle O1 rederived ⟨1⟩7.⟨2⟩3; checks C3, C3b, C4, C5, C9, C10 |
| A2-orbit-r1 | r1 form of A2(e): the `𝒜=(G_L×G_R)/G_diag` orbit is the set of vacuum pairs, labelled by `[g_Lg_R^{-1}]` | **REFUTED** | — | disproved: theory/corner-a-kinks.md ⟨1⟩9.⟨2⟩5.⟨3⟩3 | theory/checks/corner_a_check.py C7 |
| G0-soft-r1 | r1 form of G0(e): the factor `(e^{ik}−1)` is a **universal soft factor**, giving an Adler zero and forcing oracle O7/O9's hard-independent linear coefficient.  Withdrawn overclaim: hard data can enter at `O(k)` through `J_k`. | REFUTED | — | withdrawn: theory/corner-a-goldstone.md ⟨1⟩6.⟨2⟩7 | — |
| S-general | Lattice soft theorem, `n` legs: `M_{n+1}(k_s) = 𝖲(k_s;{q_i,v_i})M_n + R_{S2}`, universal only on the repaired class `𝒮_W` of D24(d).  Unrestricted universality is REFUTED by ML5.  Live obligations: ML1, ML3, ML6, packet-smeared infinite-volume ML4, ML4 at `n≥2`, exhaustive LSZ, and microscopic `𝒮_W` membership. | CONJECTURE | S2-2body, ML1, ML3, ML4, ML5-B, ML6 | — | — |
| S2 | Superseded label for the minimal `n=2` core; use S2-2body.  The old label is withdrawn to prevent duplicate status. | REFUTED | S2-2body | — | — |
| S2-2body | For D6 with fixed `0<\|k_h\|<π` and signed `k_s→0`, the displayed `δ_phys`/`S_phys` expansion and cubic remainders follow from the local current/contact route plus the passed oracle/ML2 inputs.  **Under repair:** `triangle-r1.md` T1 found no dedicated PASS verdict for `soft-current-recon.md`; positive promotion awaits r2. | SKETCH | ML2, O7, O8, O9, D6--D8 | theory/soft-current-recon.md ⟨1⟩1--⟨1⟩5 + theory/oracle-bethe.md ⟨1⟩3 | soft_current_recon_check.py, oracle_bethe_check.py, ml2_completeness_check.py, numerics fm-displacement-scan |
| ML1 | Conjectured two-magnon wave operators and channel norm on packets away from equal velocities and endpoints (future work). | CONJECTURE | D6--D8 | — | — |
| ML2 | Complete two-magnon resolution: finite ring `N(N−1)/2` physical vectors incl. the singular `\|χ_π⟩`; infinite chain = D7 scattering ⊕ one bound band; hence (R6)/(24) is unconditional.  Proved by direct Jacobi diagonalisation — **no assumed Bethe completeness** (MEDIUM) | **PROVED** | D6--D8 | theory/ml2-completeness.md (verdict: theory/verdicts/ml2-r2.md PASS) | theory/checks/ml2_completeness_check.py |
| ML3 | Conjectured packet-smeared infinite-volume current-form-factor regularity; must control `k=Θ(1/N)` and exclude physical `1/k_s` poles (future work bd `tns-7ut`). | CONJECTURE | ML1, ML2 | — | — |
| ML4 | The exact Ward projection and abstract ML4-A cancellation survive.  For one hard FM magnon the orthogonal trace is `O_N(k_s²)` at every fixed `N`, and `lim_{N→∞}lim_{k_s→0}𝒜_{⊥,N}/k_s=0`.  The former volume-uniform claim is REFUTED by `k_s=2π/N`; the two-hard/three-magnon channel is also future work.  **Under repair: `mquant-ml45-r1.md` objection 1.** | SKETCH | ML2, D6--D8, D12(a′) | theory/ml4-ward-reduction.md ⟨1⟩2--⟨1⟩5 | theory/checks/ml4_check.py (fixed-volume exponents; ML4-Q1 scaling probe; `--red-uniform` fails) |
| ML4-A | Abstract matching-plus-`C¹` cancellation lemma; algebra survived r1, but positive status awaits r2 with its shard.  **Under repair: `mquant-ml45-r1.md`.** | SKETCH | D12(a′) | theory/ml4-ward-reduction.md ⟨1⟩2 | theory/checks/ml4_check.py fixed-volume probes |
| ML5 | Unrestricted local/quasi-local universality is REFUTED by `O_η`; this negative row does not assert the repaired conditional implication. | REFUTED | D24(e) | theory/ml5-universality.md ⟨1⟩4 | theory/checks/ml4_check.py O_eta obstruction |
| ML5-A | Repaired iff: `M_2^O(0)=0` and `𝔠_h(O)=0`, with source-wise remainder controlled by `K_O` and the relative bound separately assumed.  **Under repair: `mquant-ml45-r1.md` objection 2.** | SKETCH | D24(c) | theory/ml5-universality.md ⟨1⟩2 | theory/checks/ml4_check.py ML5-I1 |
| ML5-B | Conditional implication on the five-condition D24(d) class, including the exhaustive normed LSZ decomposition.  Microscopic membership is future work bd `tns-axg`.  **Under repair: `mquant-ml45-r1.md` objection 3.** | SKETCH | ML4-A, ML5-A, D24(d) | theory/ml5-universality.md ⟨1⟩3 | theory/checks/ml4_check.py local obstructions only |
| ML6 | Conjectured control of `N→∞`, packet-width and `k_s→0` limit order and bound/off-shell channels (future work). | CONJECTURE | ML1, ML2 | — | — |
| M | The brief's literal Conjecture M (`δx` = DC limit of the soft factor) is REFUTED.  The surviving candidates are M-flux (physical boundary-current DC weight only) and conditional M-quant, into which soft data enter through `T(k)`.  No virtual/bond-data reading is claimed. | REFUTED | D10(b), D13 | theory/memory-quantization.md §1; theory/corner-b-draft.md §§2,6,10 | mquant_check.py tests flux plus empirical scan only |
| M-flux | `δx=(1/2s)[ȷ̃_{a−1\|a}(0)−ȷ̃_{b\|b+1}(0)]`, exactly the finite-time DC weight of the **physical** boundary current.  **Under repair: `mquant-ml45-r1.md`/`triangle-r1.md`; positive status awaits r2.** | SKETCH | D10(b), D13 | theory/memory-quantization.md §1 | theory/checks/mquant_check.py (operator and finite-time flux residues) |
| B3 | Under stationary vacua and finite-range dynamics, the repaired Lamport argument aims to fix the D9(a) vacuum-pair label at finite time.  For a D18-separated event with explicit cut `c∈W` and leg-subtracted charges, the surviving bookkeeping is `2s·δx+(q_out−q_in)=0`.  The raw half-line formula is REFUTED; the `ℤ`-torsor/flatness reading is a separate Conjecture K4.  **Under repair, `triangle-r1.md` B1--B4 cited.** | SKETCH | D9, D10, D13, D14, D18 | theory/corner-b-draft.md §7 | — |
| SPT-B-r1 | Old claim that `Ad(V)`-only closed contractions are pointwise `[ω]`-blind | **REFUTED**: Pauli-projective `Ad` has four distinct `D₂` characters, scalar-trivial `Ad` has four trivial copies; closed `Tr Ad(R_x)=0` vs `4` | — | disproved in theory/spt-rebuild.md ⟨1⟩3.⟨2⟩3 | spt_rebuild_check.py S-C2 |
| SPT-nogo | Old all-orders claim that `[ω]` cannot appear in any coefficient, including an edge residue | **REFUTED** (Whitehead removes only a Lie central term; edge weights/dimension remain) | — | theory/spt-rebuild.md ⟨1⟩4 | S-C4 |
| SPT-B' | Closed-bulk multiplier no-go and rigidity: paired on-site endpoint multipliers cancel exactly; normalized bulk coefficients are continuous under common-gap symmetric injective paths and are topological only if separately proved locally constant; class-correlated `Ad(V)` data are allowed | **SKETCH** (complete proposer proof; L6 critic pending) | WI, A1(g), D19-D23 | theory/spt-rebuild.md ⟨1⟩3 | spt_rebuild_check.py S-C2,S-C3 |
| SPT-E' | Registered half-chain residue is `V(g)` / `Q_edge=-iX`; endpoint modules have dimension `≥d_ω` and charge weights in `q_ω+ℤ`; AKLT-family residue is exactly `-½[1-(2b²-1)^L]Z→-Z/2`, while the `O(2)` trivial product residue is `0` | **SKETCH** in transfer register (complete proposer proof; L6 pending); **CONJECTURE conditional on H-split** as a physical edge-Hilbert statement | A1(d1,g), D19-D23 | theory/spt-rebuild.md ⟨1⟩4 | spt_rebuild_check.py S-C4,S-C5 |
| SPT-T' | At a registered twist endpoint, `V(h)V(g)V(h)^{-1}` is proportional to `V(hgh^{-1})`; for commuting `g,h` the phase is `e^{i[ω(h,g)-ω(g,h)]}`; the second endpoint compensates, so the observable is relative and requires H-dress | **SKETCH** registered (L6 pending); physical observable conditional on H-split/H-dress | SPT-E', WI, D22 | theory/spt-rebuild.md ⟨1⟩5.⟨2⟩1 | — |
| SPT-D' | Ordered endpoint-soft operators satisfy `𝕊(h)𝕊(g)=e^{iω(h,g)}𝕊(hg)` in the fixed register; for semisimple Lie groups the infinitesimal bracket has no central term, while the global module remains projective | **SKETCH** registered (L6 pending); physical edge statement conditional on H-split | SPT-E', D22 | theory/spt-rebuild.md ⟨1⟩5.⟨2⟩2 | S-C5 |
| SPT-M' | Given H-split and H-AD-edge, channel charge bookkeeping is `ΔQ_edge=-(Q_bulk,out-Q_bulk,in)` and channel outcomes are quantised; `[ω]` protects memory capacity/module, not a nonzero amplitude | **SKETCH conditional theorem** (L6 pending) | SPT-E', D22, M-quant bookkeeping | theory/spt-rebuild.md ⟨1⟩6.⟨2⟩1 | dynamical follow-on tns-cpq |
| SPT-M'-dyn | For the specified AKLT parent/boundary coupling, an edge-changing magnon reflection amplitude is nonzero on an open momentum interval and leaves the post-selected charge memory of SPT-M' | **CONJECTURE**; missing half-chain wave operators, on-shell reflection matrix, and nonvanishing proof | SPT-M', H-AD-edge | theory/spt-rebuild.md ⟨1⟩6.⟨2⟩2 | tns-cpq follow-on |
| OR1 | Oracle cross-check: (R17)--(R18) coincide term by term with passed oracle O7/O8 on D8's half-zone.  This proves the equality of the two formulas, not process universality. | PROVED | S2-2body, O7, O8 | theory/soft-current-recon.md ⟨1⟩5.⟨2⟩1 | oracle_bethe_check.py, soft_current_recon_check.py |
| OR2 | Oracle fact O6: `S_{12}(k_s,k_h)→1` from either sign, a plain limit weaker than an Adler-zero theorem. | PROVED | O6 | theory/oracle-bethe.md ⟨1⟩3.⟨2⟩2 | oracle_bethe_check.py (`limit = 2.966e-16`) |
| N1 | Numerics conjecture (not yet run): excitation-ansatz magnon amplitudes reproduce the Bethe `S(k)` as `k → 0`. | CONJECTURE | S2-2body | — | — |
| N2 | Empirical XXZ wavepacket scan matches the spin-`1/2` conditional M-quant expectation at the recorded precision; this is evidence, not a spectral proof. | SKETCH | M-quant | — | numerics/results/memory-scan-1.json: `δx≈−2T` within 0.004 sites |
| K1 | D16's kink bond is positive with the stated kernel.  **Under repair with the Corner-B package: `triangle-r1.md`.** | SKETCH | D16 | theory/corner-b-draft.md §1.2 | recorded finite-matrix computation |
| K2 | The D16 product family is annihilated bondwise by the kink Hamiltonian.  **Under repair: `triangle-r1.md`.** | SKETCH | K1, D16 | theory/corner-b-draft.md §1.2 | recorded local residual computation |
| K3 | The D16 boundary field telescopes and does not change the quasi-local derivation.  **Under repair: `triangle-r1.md`.** | SKETCH | D10, D16 | theory/corner-b-draft.md §1.2 | direct finite-support telescoping |
| K4 | Thermodynamic uniqueness/flatness: one zero-energy kink state per regularised-charge sector, with no recoil.  Only finite-volume evidence exists. | CONJECTURE | K1, K2 | theory/corner-b-draft.md §1.2 | finite `N=12` evidence only |
| Mq-E | All-volume/infinite-volume enumeration plus an explicit unitary from the incoming `≤3`-wall component to the Fano graph, preserving leg labels, charges, and local observables.  The current `N=14` enumeration is evidence only (bd `tns-00l`). | CONJECTURE | D14, D16 | — | finite `N=14` evidence only |
| Mq-AD3 | Assuming all-volume enumeration/isomorphism Mq-E, the projected Fano graph satisfies D18 by Kato--Rosenblum, Feshbach/Weyl analysis, and local decay.  Mq-E itself is unproved (bd `tns-00l`).  **Under repair: `mquant-ml45-r1.md` objection 5.** | SKETCH | D18, D16, Mq-E | theory/memory-quantization.md §3 | no checker proves Mq-E or wave-operator completeness |
| M-quant | For D16's spin-`1/2` model **assuming D18**, charge conservation gives `ΔX=−(1/s)N_T`, `spec(ΔX)⊆{−1/s,0}`, `δx=−⟨N_T⟩/s`, and `Var(ΔX)=s^{-2}⟨N_T⟩(1−⟨N_T⟩)`.  The abstract arithmetic is only `2s·δx+(q_out−q_in)=0`.  The projected spectral instantiation uses Mq-AD3; full-chain and general `(G,MPS,H)` lifts are future work (`tns-d51`, `tns-zw2`).  **Under repair: `mquant-ml45-r1.md` objections 4--8.** | SKETCH | A2(a,c,d,f), D13, D14, D16, D17, D18, Mq-AD3, G0(e) | theory/memory-quantization.md; theory/corner-b-draft.md §6 | mquant_check.py tests flux and empirical scan only; it does not test wave operators/spectrum |
| M-tk | Conditional on Mq-E, the displayed Fano graph has `t(k)=[1+iJ²/(4ωv)]^{-1}`, `T=|t|²`, and the quadratic soft zero.  `O(Δ^{-2})` leakage is measured; universality and the graph identification are not established.  **Under repair: `triangle-r1.md` T1/T6.** | SKETCH | D15, D16, Mq-AD3 | theory/corner-b-draft.md §5; theory/memory-quantization.md §3 | crosscheck_corner_b_tk.py is an empirical cross-check only |
| Bc | Conjecture Bc (“the two 2s”): the D8 soft phase slope and the spin-`1/2` conditional memory channel quantum may be the same charge datum.  Spin-1 is a falsifier, not a proved extension. | CONJECTURE | S2-2body, M-quant | — | not yet computed |

Edges of the triangle (post-r1, full statements in theory/TRIANGLE.md §6):
**A ⇒ C — CONJECTURE.**  Corner A supplies only G0(e).  Live obligations are
ML1, ML3, ML6, infinite-volume packet-smeared ML4 including `k=Θ(1/N)`, ML4
at `n≥2`, the exhaustive LSZ decomposition, and microscopic `𝒮_W` membership.
Unrestricted universality is REFUTED.
**C ⇒ B — SKETCH.**  The physical-current flux identity and conditional charge
bookkeeping survive; the Fano zero is conditional on Mq-E and its universality
is a CONJECTURE.
**B ⇒ A — SKETCH.**  Repaired B3 consists of finite-time label rigidity plus
`2s·δx+(q_out−q_in)=0`; positive promotion awaits r2.

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
theory/corner-a-pitfalls.md.  Two drafts (`theory/spt-scoping-draft.md`, now
SUPERSEDED by `theory/spt-rebuild.md` and retained as history, and
`theory/corner-b-draft.md`) still cite the two retracted/refuted rows; the exact
line references are tabulated in theory/corner-a-pitfalls.md Flag 6, as input
for freeze reconciliation.  Round-2 critic residue and its disposition:
theory/corner-a-r2-response.md.

Corner A L6 loop: CONVERGED at r3 — PASS (theory/verdicts/corner-a-r3.md, 4 MINOR wording notes only). Rows WI/A1/A2/G0 statuses are final as stated.

Oracle L6 loop: CONVERGED at r2 — PASS (theory/verdicts/oracle-bethe-r2.md, MINOR/NOTE residue only).
ML2 L6 loop: CONVERGED at r2 — PASS (theory/verdicts/ml2-r2.md, 10/10 mutants killed).
Historical freeze reconciliation, 2026-08-26: the two drafts were reconciled
against corner-a-pitfalls.md Flag 6 and oracle-bethe-r2.md residue 4 (stale
`A2-orbit-r1` / `G0-soft-r1` citations, the A1 edge-Hilbert-space over-read, and the superseded O7/O9
wording); both headers now carry "reconciled against claims DAG @ freeze, 2026-08-26".  Their definitions
were promoted to `definitions.md` D13--D23, and `theory/ml5-universality.md`'s source class to D24.
Swept residue: oracle-r2 MINOR 1 (numerical record relabelled a summary; tolerance sentence corrected),
MINOR 2 (notation rows added), MINOR 3 (definitions.md header: D6--D7 FROZEN, D8 FROZEN-AS-AMENDED),
MINOR 4 (sibling shards re-worded to quote O7/O9 in their r2 form); ML2 m12 and m14 (Justification lines
supplied for the three ⟨1⟩6.⟨2⟩2 leaves, both wrap-pair sign flips named).

**Post-r1 rule.**  Only rows backed by a PASS verdict (Corner A, oracle facts,
and ML2) remain frozen.  Rows attacked by `mquant-ml45-r1.md` or
`triangle-r1.md` are at most SKETCH until r2 passes.  The SPT rows were rebuilt
2026-08-26 in `theory/spt-rebuild.md` and are SKETCH pending critic r2;
D19--D23 were rebuilt in lockstep and `theory/spt-scoping-draft.md` is
superseded.
