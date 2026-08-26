<!-- ROLE: the argument DAG (L5). One row per claim. Status upgrades only after
     the L6 proposer/critic loop converges; verdict files live in theory/.
     Authoritative L5 statuses: PROVED | SKETCH | CONJECTURE | REFUTED.
     Empirical, conditional, under-review, and future-work qualifiers belong
     in prose, never as additional status values.  Corpus-r3 promotions and
     the final narrow repairs are applied. -->

# Claims DAG

**SPT status annotation only.**  The SPT rows were rebuilt 2026-08-26 in
`theory/spt-rebuild.md`.  Corpus r3 promotes SPT-B', registered SPT-T' and
SPT-D', and the exactly scoped SPT-M' conditional implication to PROVED.
SPT-E' is PROVED per corpus-r4.md (final promotion); `SPT-B-mult` and the
equation-(4.1) `SPT-E-AKLT` split remain PROVED per r2.  The old rows
SPT-B/E/T/D/M are superseded by SPT-B'/-E'/-T'/-D'/-M' and SPT-M'-dyn; the
withdrawn pointwise bulk-blindness claim is recorded as REFUTED under
`SPT-B-r1`, and the all-orders/all-registers form of SPT-nogo stays REFUTED.
`definitions.md` D19--D23 were rebuilt in lockstep from the same merge
proposal.  This annotation does not demote the wanted SPT program.

| id | statement (short) | status | depends on | proved in | tested in |
|---|---|---|---|---|---|
| WI | Truncated symmetry telescopes to two boundary-bond insertions: as **window vectors** `U_R(g)\|ψ_Λ⟩ = e^{i\|R\|θ_α(g)}\|ψ_Λ(T_R^{(g)})⟩` with `V_α(g)^{-1}` on `∂_-R`, `V_α(g)` on `∂_+R`, `A_{g·α}` inside `R` — requiring `Λ ⊇ [a−1,b+1]` **or** D1(e) edge-bond insertions; as **states**, the same with **no phase** | PROVED | D1–D3 | theory/corner-a.md ⟨1⟩3 | theory/checks/corner_a_check.py C1, C1b, C2, C2b |
| A1 | Unbroken case, normal ordered. (a) Half-infinite strings act on states **exactly** as single bond insertions; (b) they are implemented by **no** strongly convergent operator sequence **iff `V_α(g)` is non-scalar** (for scalar `V_α(g)` the strings stabilise exactly); (c) `ω^{M@b}=ω^{M'@b} ⟺ M'∈ℂ^×M`, so the endpoint space is a `PGL(χ)`-torsor; (d1) **on windows padded about the bond** (≥ `n_0` sites each side, `b_l,b_r≠0`) `𝔞_α=ℂ_{ω_α}[G]` acts linearly on window vectors — **padding is necessary**, the unpadded action is ill defined; (d2) the **state**-level action is the homomorphism `ρ_α: G→PGL(χ)`, `ker ρ_α = N_α`; (d3) `[ω_α]` obstructs **removing the multiplier**, i.e. lifting `ρ_α` to an honest `G→U(χ)` — it does **not** obstruct the projective window action, which always exists; (e) stabiliser `S_α ⊇ G_diag` (= `G_diag` iff `N_α={e}`), orbit `𝒜_eff = G/N_α`, **not** `𝒜`.  Scope qualifier: padded-window and state registers as stated. | PROVED | WI, D4, D12 | theory/corner-a.md ⟨1⟩4 | theory/checks/corner_a_check.py C6, C8, C8b |
| A2 | Broken case, per fixed `g ∉ H_α`: every finite `R` stays in `𝒦_{αα}`; the half-infinite limit exists **in weak-\* only**, rate `λ̃^{y−w}` for any `λ̃∈(λ_E,1)`, and lands in `𝒦_{α,g·α}`, disjoint from the vacuum folium (**sector jump**). **Under hypothesis (T)** (`G` transitive on `Ω_vac`; otherwise per `G`-orbit) vacuum pairs form `(G/H_α)×(G/H_α)` with stabiliser `H_α×H_β`, and the complete diagonal invariant is the **double coset** in `H_α\G/H_α` | PROVED | WI, D4, D5, D9, D1(e′) | theory/corner-a-kinks.md ⟨1⟩8–⟨1⟩9 | theory/checks/corner_a_check.py C7, C11 |
| G0 | (a),(b) **for `ξ ∈ 𝔥_α`, normal ordered**: `B_G(ξ)` is pure gauge at `k=0` **iff `ξ` is unbroken** (broken case = failure of *same-vacuum return*, **not** of (IT)); (c) the **exact finite-window** identity is `\|Φ_k^Λ(B_G)⟩ = (1−e^{ik})Σ_{m=a}^{b−1}e^{ikm}\|ψ;X@m⟩ + e^{ikb}\|ψ;X@b⟩ − e^{ika}\|ψ;X@(a−1)⟩`, and the clean form `(1−e^{ik})\|Φ_k(A_αX_α(ξ))⟩` holds **only** in the D12(b) δ-normalised sense; for decaying profiles the correct statement is the real-space SBP identity with `f ∈ ℓ¹∩BV` (D12(a′)), not a fixed-`k` equation; (d) lattice Noether `q_x▹ω_α = (𝒥_{x\|x+1}−𝒥_{x−1\|x})▹ω_α` exact (`ξ ∈ 𝔥_α`, normal ordered); (e) continuity equation `[H,Q[f;ξ]]=Σ_x(Δf)(x)j_{x\|x+1}(ξ)` for **any** `ξ ∈ 𝔤` and **finite range** `H` via the cut current | PROVED | D2, D5, D10, D11, D12 | theory/corner-a-goldstone.md ⟨1⟩5–⟨1⟩7 | oracle O1 rederived ⟨1⟩7.⟨2⟩3; checks C3, C3b, C4, C5, C9, C10 |
| A2-orbit-r1 | r1 form of A2(e): the `𝒜=(G_L×G_R)/G_diag` orbit is the set of vacuum pairs, labelled by `[g_Lg_R^{-1}]` | **REFUTED** | — | disproved: theory/corner-a-kinks.md ⟨1⟩9.⟨2⟩5.⟨3⟩3 | theory/checks/corner_a_check.py C7 |
| G0-soft-r1 | r1 form of G0(e): the factor `(e^{ik}−1)` is a **universal soft factor**, giving an Adler zero and forcing oracle O7/O9's hard-independent linear coefficient.  Withdrawn overclaim: hard data can enter at `O(k)` through `J_k`. | REFUTED | — | withdrawn: theory/corner-a-goldstone.md ⟨1⟩6.⟨2⟩7 | — |
| S-general | Lattice soft theorem, `n` legs: `M_{n+1}(k_s) = 𝖲(k_s;{q_i,v_i})M_n + R_{S2}`, with `𝖲` defined in D25 and universal only on the repaired class `𝒮_W` of D24(d).  Unrestricted universality is REFUTED by ML5.  Live obligations: ML1, ML3, ML6, packet-smeared infinite-volume ML4, ML4 at `n≥2`, exhaustive LSZ, and microscopic `𝒮_W` membership. | CONJECTURE | D25, S2-2body, ML1, ML3, ML4, ML5-B, ML6 | — | — |
| S2 | Superseded label for the minimal `n=2` core; use S2-2body.  The old label is withdrawn to prevent duplicate status. | REFUTED | S2-2body | — | — |
| S2-2body | For D6 with fixed `0<\|k_h\|<π` and signed `k_s→0`, the displayed `δ_phys`/`S_phys` expansion and cubic remainders follow from the local current/contact equation with a compact-hard uniform remainder and match the passed oracle/ML2 inputs.  This does not promote S-general or process independence. | PROVED | ML2, O7, O8, O9, D6--D8 | theory/soft-current-recon.md ⟨1⟩1--⟨1⟩5 + theory/oracle-bethe.md ⟨1⟩3; PROVED per corpus-r2.md adjudication | soft_current_recon_check.py, oracle_bethe_check.py, ml2_completeness_check.py, numerics fm-displacement-scan |
| ML1 | Conjectured two-magnon wave operators and channel norm on packets away from equal velocities and endpoints (future work). | CONJECTURE | D6--D8 | — | — |
| ML2 | Complete two-magnon resolution: finite ring `N(N−1)/2` physical vectors incl. the singular `\|χ_π⟩`; infinite chain = D7 scattering ⊕ one bound band; hence (R6)/(24) is unconditional.  Proved by direct Jacobi diagonalisation — **no assumed Bethe completeness** (MEDIUM) | **PROVED** | D6--D8 | theory/ml2-completeness.md (verdict: theory/verdicts/ml2-r2.md PASS) | theory/checks/ml2_completeness_check.py |
| ML3 | Conjectured packet-smeared infinite-volume current-form-factor regularity; must control `k=Θ(1/N)` and exclude physical `1/k_s` poles (future work bd `tns-7ut`). | CONJECTURE | ML1, ML2 | — | — |
| ML4 | For one hard FM magnon, formulas (15)--(17) give an `O_N(k_s²)` **off-shell analytic interpolation** at fixed periodic `N`, not an on-shell ring soft limit.  The first physical sequence `k_s=2π/N` refutes volume uniformity.  HOLD at SKETCH: the on-shell packet-smeared infinite-volume estimate remains open (`tns-7ut`), as does the two-hard/three-magnon channel. | SKETCH | ML2, ML4-A, ML4-Ward, D6--D8, D12(a′) | theory/ml4-ward-reduction.md ⟨1⟩4--⟨1⟩5; HOLD per corpus-r2.md N3 | theory/checks/ml4_check.py (off-shell fixed-volume exponents; ML4-Q1 scaling probe; `--red-uniform` fails) |
| ML4-A | Abstract matching-plus-`C¹` cancellation lemma: `Γ(0)=U`, `R=(1-UU†)J`, and `b(k)=O(k)` imply `\|b(k)Γ(k)†R\|=O(k²)` in operator and rescaled packet norm. | PROVED | D12(a′) | theory/ml4-ward-reduction.md ⟨1⟩2; PROVED per corpus-r2.md adjudication | theory/checks/ml4_check.py fixed-volume probes |
| ML4-Ward | Exact finite-sector Ward projection (8)--(11): on `ker S^+`, `D_{n,N}†D_{n,N}=(N-2n)I` and `P_{n,N}J^-_0=2Q_0J^z_0/(N-2n)`, with the stated general-sector polar formula and one-hard packet consequence. | PROVED | D6--D8 | theory/ml4-ward-reduction.md ⟨1⟩3; PROVED per corpus-r2.md adjudication | theory/checks/ml4_check.py Ward/projection residuals |
| ML5 | Unrestricted local/quasi-local universality is REFUTED by `O_η`; this negative row does not assert the repaired conditional implication. | REFUTED | D24(e) | theory/ml5-universality.md ⟨1⟩4 | theory/checks/ml4_check.py O_eta obstruction |
| ML5-A | Repaired iff: `M_2^O(0)=0` and `𝔠_h(O)=0`, with source-wise remainder controlled by `K_O` and the relative bound separately assumed. | PROVED | D24(c) | theory/ml5-universality.md ⟨1⟩2; PROVED per corpus-r2.md adjudication | theory/checks/ml4_check.py ML5-I1 |
| ML5-B | Conditional implication on the five-condition D24(d) class, including the exhaustive normed LSZ decomposition.  The implication is proved; nonemptiness and microscopic membership remain CONJECTURE/future work bd `tns-axg`. | PROVED | ML4-A, ML5-A, D24(d) | theory/ml5-universality.md ⟨1⟩3; PROVED per corpus-r2.md adjudication (conditional implication) | theory/checks/ml4_check.py local obstructions only |
| ML6 | Conjectured control of `N→∞`, packet-width and `k_s→0` limit order and bound/off-shell channels (future work). | CONJECTURE | ML1, ML2 | — | — |
| M | The brief's literal Conjecture M (`δx` = DC limit of the soft factor) is REFUTED.  The surviving candidates are M-flux (physical boundary-current DC weight only) and conditional M-quant, into which soft data enter through `T(k)`.  No virtual/bond-data reading is claimed. | REFUTED | D10(b), D13 | theory/memory-quantization.md §1; theory/corner-b-draft.md §§2,6,10 | mquant_check.py tests flux plus empirical scan only |
| M-flux | `δx=(1/2s)[ȷ̃_{a−1\|a}(0)−ȷ̃_{b\|b+1}(0)]`, exactly the finite-time DC weight of the **physical** boundary current. | PROVED | D10(b), D13 | theory/memory-quantization.md §1; PROVED per corpus-r2.md adjudication | theory/checks/mquant_check.py (operator and finite-time flux residues) |
| B3 | Under stationary vacua and finite-range dynamics, the Lamport/Lieb--Robinson argument fixes the D9(a) vacuum-pair label at finite time, including norm-local approximation of both evolved local factors.  For a D18-separated event with explicit cut `c∈W` and leg-subtracted charges, `2s·δx+(q_out−q_in)=0`.  The raw half-line formula is REFUTED; the `ℤ`-torsor/flatness reading remains Conjecture K4. | PROVED | D9, D10, D13, D14, D18 | theory/corner-b-draft.md §7; PROVED per corpus-r2.md adjudication with N9 sweep | — |
| SPT-B-r1 | Old claim that `Ad(V)`-only closed contractions are pointwise `[ω]`-blind; Pauli-projective and scalar-trivial adjoint characters disprove it. | REFUTED | — | disproved in theory/spt-rebuild.md ⟨1⟩3.⟨2⟩3 | spt_rebuild_check.py S-C2 |
| SPT-nogo | Old all-orders claim that `[ω]` cannot appear in any coefficient, including an edge residue; Whitehead trivialises only the infinitesimal cocycle class, while global edge weights/dimension remain. | REFUTED | — | theory/spt-rebuild.md ⟨1⟩4 | S-C4 |
| SPT-B-mult | For ordered closed on-site symmetry insertions, the endpoint action is `V(g)⊗\bar V(g)` and the projective multipliers cancel exactly; the closed register is invariant under rephasing the lift. | PROVED | WI, D2, D19--D20 | theory/spt-rebuild.md ⟨1⟩3.⟨2⟩1; PROVED per corpus-r2.md adjudication | spt_rebuild_check.py S-C2 |
| SPT-B' | Under the common-gap path and the newly continuous/`C^p` external data, normalized finite/thermodynamic/soft coefficients are continuous (with H-soft-p for derivative limits) and become topological only after a separate local-constancy proof; class-correlated `Ad(V)` data are allowed. | PROVED | SPT-B-mult, A1(g), D19--D23 | theory/spt-rebuild.md ⟨1⟩3.⟨2⟩2--⟨2⟩3; PROVED per corpus-r3.md adjudication | spt_rebuild_check.py S-C2,S-C3 |
| SPT-E-AKLT | For the anisotropic AKLT family, equation (4.1) gives the Hermitian registered partial-charge compression exactly as `ℜ_{A_b,L}(S^z)=-½[1-(2b²-1)^L]Z`, with AKLT-family limit `-Z/2`. | PROVED | D19--D21, D23 | theory/spt-rebuild.md ⟨1⟩4.⟨2⟩4; PROVED per corpus-r2.md adjudication | spt_rebuild_check.py S-C4 |
| SPT-E' | In the fixed Schmidt/edge register `E_C`, the compensated group residue is `V(g)` and the Hermitian Lie residue is the centered, phase-gauge-invariant `Q_edge=-iX_C^∘`, with the fixed-tensor congruence `spec Q_edge⊂q_{ω,C}^∘+ℤ` and irreducible dimension `≥d_ω`.  The padded module is `𝓜_χ(C)≅E_C⊗E_C^*`, i.e. `χ` copies.  A physical edge statement is conditional on H-split.  No deformation constancy of the centered offset is claimed. | PROVED | D19--D23, SPT-E-AKLT | theory/spt-rebuild.md ⟨1⟩4; PROVED per corpus-r4.md adjudication | spt_rebuild_check.py S-C4,S-C5, phase-gauge red |
| SPT-T' | In the registered endpoint, (5.1) follows by eliminating `V(hg)` and (5.2) follows for commuting `g,h`; the second endpoint compensates.  A physical observable remains conditional on H-split and H-dress. | PROVED | SPT-E', WI, D22 | theory/spt-rebuild.md ⟨1⟩5.⟨2⟩1; PROVED per corpus-r3.md adjudication | — |
| SPT-D' | Ordered registered endpoint products realise the cocycle; for compact semisimple Lie algebra the infinitesimal cocycle is a coboundary and is removed only in the stated phase section.  Physical edge use remains conditional on H-split and H-dress. | PROVED | SPT-E', D22, H-split, H-dress | theory/spt-rebuild.md ⟨1⟩5.⟨2⟩2; PROVED per corpus-r3.md adjudication | S-C5 |
| SPT-M' | Given H-split, H-AD-edge, charge conservation, and definite channel charges, `ΔQ_edge=-(Q_bulk,out-Q_bulk,in)` and fixed-system channel differences are integral.  This uses only the valid fixed-tensor congruence, not deformation constancy of the centered offset.  Protection is capacity/module protection, not nonzero amplitude. | PROVED | SPT-E', D22, M-quant bookkeeping | theory/spt-rebuild.md ⟨1⟩6.⟨2⟩1; PROVED per corpus-r3.md adjudication as a conditional implication | dynamical follow-on tns-cpq |
| SPT-M'-dyn | For D23's specific `H_{A,+}^{dyn}=Σ_{x≥0}P^{(S=2)}_{x,x+1}`, with boundary-magnon coupling `P^{(S=2)}_{0,1}`, an edge-changing magnon reflection amplitude is nonzero on an open momentum interval and leaves the post-selected charge memory of SPT-M'.  HOLD: half-chain wave operators, H-AD-edge, the on-shell reflection matrix, and nonvanishing remain missing. | CONJECTURE | SPT-M', H-AD-edge, D23 | theory/spt-rebuild.md ⟨1⟩6.⟨2⟩2; HOLD per corpus-r2.md | tns-cpq follow-on |
| OR1 | Oracle cross-check: (R17)--(R18) coincide term by term with passed oracle O7/O8 on D8's half-zone.  This proves the equality of the two formulas, not process universality. | PROVED | S2-2body, O7, O8 | theory/soft-current-recon.md ⟨1⟩5.⟨2⟩1 | oracle_bethe_check.py, soft_current_recon_check.py |
| OR2 | Oracle fact O6: `S_{12}(k_s,k_h)→1` from either sign, a plain limit weaker than an Adler-zero theorem. | PROVED | O6 | theory/oracle-bethe.md ⟨1⟩3.⟨2⟩2 | oracle_bethe_check.py (`limit = 2.966e-16`) |
| N1 | Numerics conjecture (not yet run): excitation-ansatz magnon amplitudes reproduce the Bethe `S(k)` as `k → 0`. | CONJECTURE | S2-2body | — | — |
| N2 | Empirical XXZ wavepacket scan matches the spin-`1/2` conditional M-quant expectation at the recorded precision; this remains SKETCH because it is numerical evidence, not a theorem. | SKETCH | M-quant | HOLD per corpus-r2.md: empirical scan only | numerics/results/memory-scan-1.json: `δx≈−2T` within 0.004 sites |
| K1 | D16's kink bond is positive with the stated kernel by direct positive `2×2` block diagonalisation. | PROVED | D16 | theory/corner-b-draft.md §1.2; PROVED per corpus-r2.md adjudication | recorded finite-matrix computation |
| K2 | Every neighboring factor of the D16 product family lies in K1's kernel, so the family is annihilated bondwise. | PROVED | K1, D16 | theory/corner-b-draft.md §1.2; PROVED per corpus-r2.md adjudication | recorded local residual computation |
| K3 | The D16 boundary field telescopes outside every local observable and leaves the quasi-local derivation unchanged. | PROVED | D10, D16 | theory/corner-b-draft.md §1.2; PROVED per corpus-r2.md adjudication | direct finite-support telescoping |
| K4 | Thermodynamic uniqueness/flatness: one zero-energy kink state per regularised-charge sector, with no recoil.  Only finite-volume evidence exists. | CONJECTURE | K1, K2 | theory/corner-b-draft.md §1.2 | finite `N=12` evidence only |
| Mq-E | All-volume/infinite-volume enumeration plus an explicit unitary from the incoming `≤3`-wall component to the Fano graph, preserving leg labels, charges, and local observables.  The current `N=14` enumeration is evidence only (bd `tns-00l`). | CONJECTURE | D14, D16 | — | finite `N=14` evidence only |
| Mq-AD3 | Assuming all-volume enumeration/isomorphism Mq-E, the projected Fano graph satisfies D18 by Kato--Rosenblum, Feshbach/Weyl analysis, and local decay.  The implication is proved; Mq-E itself remains CONJECTURE (bd `tns-00l`). | PROVED | D18, D16, Mq-E | theory/memory-quantization.md §3; PROVED per corpus-r2.md adjudication conditional on Mq-E | no checker proves Mq-E itself |
| M-quant | For D16's spin-`1/2` model **assuming D18**, charge conservation gives `ΔX=−(1/s)N_T`, `spec(ΔX)⊆{−1/s,0}`, `δx=−⟨N_T⟩/s`, and `Var(ΔX)=s^{-2}⟨N_T⟩(1−⟨N_T⟩)`.  The abstract arithmetic is only `2s·δx+(q_out−q_in)=0`.  Full-chain D18 remains open (`tns-d51`).  **Generalized by M-quant-G (PROVED conditional, mquant-g-r2.md).** | PROVED | A2(a,c,d,f), D13, D14, D16, D17, D18, G0(e) | theory/memory-quantization.md; theory/corner-b-draft.md §6; PROVED per corpus-r2.md adjudication conditional on D18 | mquant_check.py tests flux and empirical scan only; D18 is an assumption |
| M-quant-G | For compact `G`, a D2(a) covariant family of injective MPS vacua of arbitrary finite `χ`, a fixed pair `β=g·α` with a common unbroken circle direction, finite-range `G`-invariant `H`, vacuum charge densities `(+s,-s)`, a D17 kink packet in `𝒦_{αβ}`, and the exact D13(a) coordinate, **H-AD-G := D18(AD1--AD4) with definite charges `q_in=q_L=-1`, `q_T=+1` implies** `ΔX=−N_T/s`, `δx=−⟨N_T⟩/s`, spectrum `{0,−1/s}` at most, and the Bernoulli variance.  `(T)` is optional and only supplies D9(d)'s fixed double-coset label.  PROVED per mquant-g-r2.md adjudication: **PROVED only as the conditional implication** H-MQG(1--4) + H-AD-G (exactly D18(AD1--AD4) for the fixed packet, with `q_in=q_L=-1`, `q_T=+1`, no other propagating channel, and no bound-state component) implies (G.1)--(G.2); H-AD-G itself, Mq-E, full-chain D18, any soft zero, and all packet/model/soft-limit uniformity remain unproved.  No general proof of H-AD-G, soft zero, or uniformity over a continuous vacuum manifold is claimed. | **PROVED** (conditional, per mquant-g-r2.md) | D1, D2(a), A2(a,c,d,e,f), D9(d), D10, D13(a), D17, D18, G0(d,e), B3, M-flux | theory/memory-quantization-general.md | theory/checks/mquant_general_check.py (symbolic arithmetic only; `--red` mutates `q_T`) |
| M-tk | Conditional on Mq-E, the displayed Fano graph has `t(k)=[1+iJ²/(4ωv)]^{-1}`, `T=|t|²`, and the quadratic soft zero.  `O(Δ^{-2})` full-chain leakage is measured; full-chain accuracy and universality of the zero/coefficient remain CONJECTURE. | PROVED | D15, D16, Mq-E, Mq-AD3 | theory/corner-b-draft.md §5; theory/memory-quantization.md §3; PROVED per corpus-r2.md adjudication conditional on Mq-E for the displayed graph | crosscheck_corner_b_tk.py is an empirical full-chain cross-check only |
| Bc | Conjecture Bc (“the two 2s”): the D8 soft phase slope and the spin-`1/2` conditional memory channel quantum may be the same charge datum.  Spin-1 is a falsifier, not a proved extension. | CONJECTURE — **falsifier SURVIVED 2026-08-26**: slope `= 1/s` and `δx/N_T = −1/s` measured across `s ∈ {1/2,1,3/2,2}` (pre-registered 8% criteria; ansatz-free ring + dynamics + Bethe residual `≤1.1e−14`); the `\|q_hard\|` factor is UNTESTED (all legs `\|q\|=1`) — charge-2 bound-state leg is the next falsifier | S2-2body, M-quant | — | numerics/results/spin1-bc-falsifier.json (84 ring + 16 dyn + 22 memory rows); numerics/test/test_spins_twomagnon.jl, test_spins_memory.jl (decision tests, fixed criteria) |

Edges of the triangle (post-r1, full statements in theory/TRIANGLE.md §6):
**A ⇒ C — CONJECTURE.**  Corner A supplies only G0(e).  Live obligations are
ML1, ML3, ML6, infinite-volume packet-smeared ML4 including `k=Θ(1/N)`, ML4
at `n≥2`, the exhaustive LSZ decomposition, and microscopic `𝒮_W` membership.
Unrestricted universality is REFUTED.
**C ⇒ B — SKETCH.**  The physical-current flux identity and conditional charge
bookkeeping survive; the Fano zero is conditional on Mq-E and its universality
is a CONJECTURE.
**B ⇒ A — SKETCH.**  B3 itself is PROVED: finite-time label rigidity plus
`2s·δx+(q_out−q_in)=0`.  The edge remains SKETCH because measured memory has
not been shown to reconstruct an asymptotic-symmetry action or classifying
datum (the critic's named HOLD reason).

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

**Post-r4 rule.**  Promotions are exactly those adjudicated in
`theory/verdicts/corpus-r3.md` and `corpus-r4.md` (PASS, fixed point):
SPT-B', registered SPT-T'/SPT-D', the scoped SPT-M' conditional implication,
and SPT-E' are PROVED; `SPT-B-mult` and equation-(4.1) `SPT-E-AKLT` retain
their r2 PROVED status.  M-quant-G is PROVED (conditional) per
`mquant-g-r2.md`.  D19--D23 remain in lockstep and
`theory/spt-scoping-draft.md` remains superseded.
