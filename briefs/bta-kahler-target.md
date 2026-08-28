<!-- ROLE: campaign target specification for the B ⇒ A edge (memory ⇒
     asymptotic symmetry) via the Kähler / moment-map route, bd `tns-89h`.
     NOT a proof and NOT a greenlight: this file is the well-posed target a
     prover lane can be pointed at and a critic lane can attack.
     Read-order gate for every lane: CLAUDE.md -> HANDOFF_MPS_SOFT_THEOREM.md
     -> HANDOFF.md -> docs/framing.md -> definitions.md (esp. D1, D2, D4, D9,
     D13, D16, D17, D26) -> notation.md -> claims/CLAIMS.md (esp. A1, A2, B3,
     M-flux, M-quant-G, M-INDEX-fin/-spec, M-IDX-density, M-INDEX-LA-strong
     [REFUTED], M-INDEX-LA-folium) -> theory/TRIANGLE.md §1 and §6.3 ->
     theory/memory-index.md ⟨1⟩3, ⟨1⟩3b, ⟨1⟩9--⟨1⟩12 -> theory/corner-a.md
     ⟨1⟩4 -> theory/corner-a-kinks.md ⟨1⟩8--⟨1⟩10 -> THIS FILE. -->

# Campaign target — the B ⇒ A edge as a moment map (the Kähler route)

## §0. Provenance, scope, and two standing constraints (read before anything)

**(0.1) Provenance constraint — binding.**  bd memory
`provenance-tjo-2026-08-26-the-observation-that`: *the observation that TNS
variational classes carry a Kähler structure and that TDVP is the associated
Hamiltonian flow originated with Tobias Osborne, who communicated it to Jutho
Haegeman, who made it work.*  **Do not state this in any paper without TJO's
explicit sign-off.**  Repo shards may use it freely; `paper/` may not, and no
lane may write a paper sentence asserting it.  Carry this paragraph forward
into every artifact this campaign produces.

**(0.2) Paper-scope constraint — binding.**  bd `tns-89h` and bd memory
`tjo-2026-08-26-kaehler-moment-map-idea`: TJO has **explicitly not decided**
whether this belongs in the current Letter; the standing recommendation on
file is at most one outlook sentence in the paper, full development as a
companion.  **No lane may presume the current paper is the destination**, may
write into `paper/`, or may plan around a page budget.  If a lane's result is
strong enough to change that, it says so in its HONEST STATUS section and the
decision goes to TJO.

**(0.3) What this file is.**  A target, not a result.  Nothing below has any
L5 status.  Every statement in §3 is a *target*, i.e. a thing a prover is
asked to prove or refute; every definition in §4 is a *proposal*, quarantined
in the prover's shard until an L6 loop converges (the D29--D31 soft-index
proposals are still quarantined for exactly this reason — see §7.4).

---

## §1. Why this edge exists, and the one question that decides it

### 1.1 The objection to beat

`theory/TRIANGLE.md` §6.3 and `claims/CLAIMS.md` hold B ⇒ A at **SKETCH**.
Two things along the edge are already **PROVED** (B3): finite-time
vacuum-pair *label rigidity*, and the leg-charge ledger
`2s·δx + (q_out − q_in) = 0`.  The named HOLD reason is one sentence and it
is sharp:

> *What remains missing for B ⇒ A is a proof that measured memory
> reconstructs an asymptotic-symmetry **action** or classifying datum.*

That is: the corpus can currently *read off* the D9(d) vacuum-pair label and
*account for* charge, but it cannot show that the memory datum **generates**
anything.  A ledger is bookkeeping.  An edge needs an action.

`docs/framing.md` §1--§2 says exactly what "action" must mean, and the same
document is the reason the edge is not closed: a symmetry is asymptotic/
physical **iff it acts on the phase space with a well-defined symplectic
action**, and the charges must close under a Poisson bracket, possibly with a
central extension.  Corner A's own **SKETCH box S-A1** records that this
demand is *not met* at the operator level: it is not proved that the endpoint
algebra `𝔞_α` acts on the GNS Hilbert space rather than on finite-window
spaces `𝒲_{Λ,b}`.

### 1.2 The route (bd `tns-89h`)

The MPS variational manifold is Kähler; TDVP is the associated Hamiltonian
flow; the induced Poisson bracket is explicit in the ground truth
(`refs/arxiv-1810.07006/p4_tdvp.tex`, §"Time evolution on a manifold").
Symplectically reduce to the asymptotic degrees of freedom (kink position ×
endpoint torsor); show that the asymptotic charge is the **moment map** for
the selected circle action, with the memory coordinate conjugate.  Then
"charges generate asymptotic symmetries" is not a hope: it is the definition
of a moment map, and the Poisson bracket `{μ, ·}` *is* the action.

### 1.3 The playbook question — invert the burden

The memory corner became a theorem when someone noticed that **quantization
needs no scattering theory; scattering only computes the value**
(bd `session-3-strategic-record-2026-08-28-tjo`).  The analogous question
here, and the one this brief exists to force a lane to answer, is:

> **What does the symplectic structure give for free, and what must dynamics
> supply?**

The provisional answer this brief commits to, and which the prover must
confirm or destroy:

| given for free by geometry/symmetry | must be supplied by dynamics |
|---|---|
| the Poisson bracket on the reduced space, and the fact that `{μ_ϖ, ·}` generates the wall-translation flow — i.e. the **action** corpus-r2 demands | that the physical trajectory of a scattering event stays on (or asymptotically returns to) the variational family |
| the identification of the D13(a) memory observable with the moment map — *the memory datum is a moment-map value* | **which** value occurs, i.e. the weights `p_ν` / `⟨N_T⟩` of M-INDEX-spec and M-quant-G |
| the **normalisation** of the quantum: symplectic volume per lattice translation, hence `1/(2s)` per unit escaped charge (Duistermaat--Heckman) | existence of the asymptotic limits at all (D18 / H-AD-G / AC-EX) |
| the obstruction theory: whether a *global* moment map exists at all, and what obstructs it | the sign/orientation and the actual event's `ν` |

Note what this buys if it holds: the memory quantum `1/(2s)` would follow
from **symplectic volume alone**, with no scattering theory, no channel
inventory, and no wave operators — the same inversion that made
M-INDEX-fin/-spec possible, applied one corner over.  That is the prize.  It
is also, honestly, the part most likely to turn out to be a restatement (see
§8).

### 1.4 The register sentence for this campaign

*Symmetry quantizes; geometry generates; dynamics only picks the value.*

---

## §2. Standing setting (cite, never redefine — L4)

Everything below is already numbered.  No lane may restate any of it.

- **(H1)/(H2)/(H3)=(S)/(H4)** exactly as tabulated in `theory/TRIANGLE.md` §0
  (D1, D2(a), D2(e), D10).
- Injective canonical-form uniform MPS, transfer gap `λ_E`, the honest
  `λ̃`-rate discipline (`‖E^m − P‖ ≤ C_λ̃ λ̃^m`, never a bare `λ_E^m`): D1(c).
- Window vectors, bond insertions **including the two edge bonds**, decorated
  states `ω_A[T]`, `ω_A^{M@b}`, and **two-sided decorations** `ω_{α|β}^{(m)}[T]`
  with their positivity/consistency lemma: D1(e), D1(e′).
- (IT), the cocycles `θ_α`, `ω_α`, the class `[ω_α] ∈ H²(H_α,U(1))`, normal
  ordering `ǔ_α`, and the smoothness hypothesis **(S)** with `X_α(ξ)`: D2.
- Profile classes `𝔉_c ⊂ 𝔉_ec ⊂ 𝔉_{ℓ¹}` and the rule that a plane wave is
  admitted only inside a packet: D3(a).
- Bond implementers on **padded** windows `𝒱_b(M)`, `N_α`, `ρ_α : G → PGL(χ)`,
  `𝒜_eff = G/N_α`, the twisted algebra `𝔞_α = ℂ_{ω_α}[H_α]`, the asymptotic
  charges `𝔮_b(ξ)` and the **central-extension caveat** on `c_α(ξ,ζ)`: D4.
- Kink sectors `𝒦_{αβ}`, disjointness, the endpoint space `E_b^α` as a
  `PGL(χ)`-torsor, the double-coset label `𝔡(α_L,α_R)`, hypothesis **(T)**: D9.
- Lattice Noether pair, cut current, continuity equation: D10, G0(d),(e).
- Memory observables: the **frozen** windowed wall coordinate `𝔛_W` and
  `δx = ϱ_{t_f}(𝔛_W) − ϱ_{t_i}(𝔛_W)`, with the two dresses and the D13(c)
  trap: D13.  The `ℓ¹` class `𝒦^{(1)}_{αβ}`: D17.
- The D16 model with its **exact zero-energy kink family**
  `|K(z)⟩ = ⊗_n(|↑⟩_n + z q^n|↓⟩_n)`, `q = Δ − √(Δ²−1)`, and the frozen
  coordinates `z = q^{−x_0}e^{iφ}` with `(x_0, φ)` named a conjugate pair:
  D16 (and `notation.md`, row `q, x_0, φ, |K(z)⟩`).  **`(x_0,φ)` being called
  conjugate in D16 is a name, not a theorem — proving it is rung L1.**
- The circle-integrality hypothesis **(INT)**: D26.  The relaxation
  hypothesis **(LR)**: D27.  Ansatz band data **(H-ACE)**: D28.
- Claims you may use at their DAG status and must not reprove: **WI**, **A1**
  (a)--(g), **A2** (a)--(f), **G0** (a)--(e), **M-flux**, **B3**,
  **M-quant-G** (conditional), **M-INDEX-fin**, **M-INDEX-spec**
  (conditional), **M-IDX-density**, **AC-EX** (conditional).
- **Claims you must not contradict and must explicitly survive:**
  **M-INDEX-LA-strong is REFUTED** (§5.2 below); **M** (the brief's literal
  Conjecture M) is REFUTED; **A2-orbit-r1** is REFUTED (`𝒜` is not the
  classifying object; the double coset is); **G0-soft-r1** is REFUTED.
- **Load-bearing SKETCH boxes** you may not use silently: **S-A1** (the split
  property; `𝔞_α` on the GNS space is *not* established) and **S-A2** (no
  `g`-uniformity over a continuum `Ω_vac`; M1's kinks are therefore not
  usable as superselection sectors).

**Ground truth for the Kähler/TDVP structure (L3).**  Only
`refs/arxiv-1810.07006`:
- `p2_tangent.tex` — tangent vectors, the gauge freedom `B ↦ B + A X − X A`,
  the left gauge-fixing condition, and the two facts this campaign turns on:
  the overlap `⟨Ψ(Ā)|Φ(B;A)⟩` and the tangent-tangent overlap both carry the
  prefactor written `2πδ(0)`, of which the source says *"The factor corresponds
  to the system size, which diverges in the thermodynamic limit"*; and, after
  left gauge fixing, *"the Gram matrix … for the tangent space as parametrized
  by the matrix `X` reduces to the unit matrix"* (i.e. **only after that
  divergent factor is divided out**).
- `p4_tdvp.tex` — the TDVP projection `i ∂_t|Ψ(A(t))⟩ = P_{A(t)}H|Ψ(A(t))⟩`;
  the explicit Poisson bracket
  `{f,g} = −(∂_{A_i}f)(G^{-1})^{ij}(∂_{Ā_j}g) + (∂_{A_i}g)(G^{-1})^{ij}(∂_{Ā_j}f)`;
  `∂_t f = i{f,h}`; and the conservation criterion for a symmetry generator
  `K`: `P_A K|Ψ(A)⟩ = K|Ψ(A)⟩`, which the source states holds *"for all
  symmetries which act as a tensor product of one-site gates, i.e. when the
  generator is a sum of one-site operators"*.
Any other statement about Kähler geometry, moment maps, symplectic reduction,
or Duistermaat--Heckman must be **proved in the shard**, not cited from
memory.  A citation without a `refs/` file and location is a FATAL objection
(L3).

---

## §3. THE STATEMENT LADDER

Five rungs, increasing in strength and generality.  Each is stated so that it
is true or false.  Ids follow the campaign convention (`M-INDEX-fin`,
`AC-EX`, `S-IDX-spec`).

---

### L1 — `BA-MM-fin` (finite-window moment-map identity on the exact kink family)

*The rung that is provable now, exactly, with no hypotheses beyond frozen
definitions.  Its purpose is to make the edge's central object concrete and
to give every higher rung an anchor it must reduce to.*

**ASSUME.**  (i) D16 verbatim: `J>0`, `Δ>1`, `q = Δ−√(Δ²−1) ∈ (0,1)`, the
exact zero-energy product family `|K(z)⟩`, `z = q^{−x_0}e^{iφ}`, and
`κ := −log q > 0`.  (ii) The site-normalised form of the family (each factor
divided by its own norm), so that the family is a smooth map
`ℳ_1 := {(x_0,φ) ∈ ℝ × (ℝ/2πℤ)} → 𝔖(𝔄)`, states, not vectors.
(iii) A finite window `W = [a,b]` and a cut `c_0 ∈ W`.  (iv) D13(a)'s frozen
coordinate `𝔛_W` and the M-INDEX identity `Q̂_{W,c_0} := 2s(𝔛_W − c_0)`
(IDX.1), with `s = 1/2` in D16.  **No Hamiltonian is used anywhere in L1**;
`H_kink` enters only to say which family is being differentiated.

**PROVE.**  Write `𝔨_W(x_0) := log‖·‖²`-potential of D32(b) below, evaluated
on the window, and `ϖ_W := i∂∂̄𝔨_W` its Kähler form (D32(c)), and
`μ_W(x_0,φ) := ⟨K(z)|Q̂_{W,c_0}|K(z)⟩` the moment-map candidate (D34(a)).
Then, with `ξ^♯ = ∂_φ` the fundamental vector field of the selected circle:

1. **(L1.a) `ϖ_W` is a symplectic (indeed Kähler) form on `ℳ_1`**, `U(1)`-
   invariant, with `ϖ_W = Ω_W(x_0)\,dx_0 ∧ dφ` and `Ω_W > 0`.
2. **(L1.b) Exact moment-map identity, at finite `W`, with no error term:**
   `dμ_W = ι_{ξ^♯}ϖ_W` **identically on `ℳ_1`**, i.e.
   `μ_W'(x_0) = −Ω_W(x_0)` for every `x_0`, every `Δ>1`, and every `W`.
   *(This is an identity between two independently defined sums over the same
   window; there is no `λ̃`-remainder.  A throwaway numerical check gave
   `1.8·10^{-15}` over `S ∈ {1/2,1,3/2,2}` × `Δ ∈ {1.5,2,4}` × 301 values of
   `x_0` — but that check evaluated both sides from a shared closed form and
   is therefore weak evidence; §6 requires two independent routes.  The prover
   must supply the two-line analytic proof, not the numbers.)*
3. **(L1.c) `(x_0,φ)` is a conjugate pair in the sense D16 only names:**
   `{x_0, μ_W}_{ϖ_W} = 1` up to the D1(c) `λ̃^{d_W}` window-edge terms of
   D13(a), and exactly `{φ, μ_W} = 0`.
4. **(L1.d) Period normalisation (the DH seed):** the symplectic area of one
   lattice period is
   `∫_{x_0}^{x_0+1}∫_0^{2π} ϖ_W = 2π·2s` for every `x_0`, exactly, and the
   moment map advances by `Δμ_W = 2s` per unit lattice translation, up to the
   same `λ̃^{d_W}` edge terms.  *(Provable in two lines: `∫_0^1 Ω_W(x)dx` is a
   sum of complete integrals of one bump function.)*

**What it buys the DAG.**  A new PROVED row `BA-MM-fin` establishing, for the
frozen D16 model, that **the memory observable is a moment map** and that the
D16 name "conjugate pair" is a theorem.  It converts §6.3's missing
"symmetry action" from an aspiration into a computed object *in one model*.
It does **not** close the edge, and a lane that lands only L1 has **failed**
the campaign — say so honestly if it happens.

**Fence (do not skip).**  D16 has `χ = 1`, so `V_α(g)` is scalar for every
`g` and `N_α = G`.  L1 therefore sits on the **benign side** of both
refutation mechanisms of `M-INDEX-LA-strong` (§5.2) and of A1(b): it is
precisely the case where nothing obstructs.  **L1 supplies no evidence
whatsoever about `χ > 1`.**  Any shard that suggests otherwise earns a MAJOR.

---

### L2 — `BA-MM-mps` (regularised Kähler form and moment map on a general MPS kink family)

**ASSUME.**  (H1),(H2),(S) at both tails, D26(INT), and a fixed vacuum pair
`β = g·α` with a common unbroken circle direction `ξ ∈ 𝔥_α ∩ 𝔥_β` (exactly
H-MQG(1)--(2)).  A smooth finite-dimensional family
`ℳ ∋ m ↦ ϱ_m ∈ 𝒦^{(1)}_{αβ}` of D1(e′) two-sided decorated states of common
bond dimension `χ`, with the D16 family as the `χ=1` special case.  Plus the
two new hypotheses proposed as D32(d)/D33(c):
- **(FS-conv)** the windowed Kähler forms `ϖ_W` converge as `W ↑ ℤ` at a
  D1(c) `λ̃`-rate, uniformly on compacta of `ℳ`;
- **(FOL)** `ℳ` lies inside a single folium, i.e. all `ϱ_m` are mutually
  normal (see §5.3 — this is a real hypothesis, not a formality).

**PROVE.**
1. **(L2.a)** `ϖ := lim_{W↑ℤ} ϖ_W` exists, is a closed `U(1)`-invariant
   2-form on `ℳ`, and is **independent of the window sequence and of the cut
   `c_0`** — even though the potential `𝔨_W` diverges (§5.1).
2. **(L2.b)** The selected circle acts on `ℳ`, and its fundamental vector
   field `ξ^♯` satisfies `L_{ξ^♯}ϖ = 0`; `ι_{ξ^♯}ϖ` is closed.
3. **(L2.c) Dichotomy (this is the honest form — do not assume the good
   branch).**  Either `ι_{ξ^♯}ϖ` is **exact**, in which case the moment map
   `μ_ϖ` exists globally on `ℳ`, is unique up to a constant, and equals the
   `W ↑ ℤ` limit of `μ_W` on the D13(a) calibration; **or** it is closed and
   not exact, in which case **no global moment map exists** and the action is
   only locally Hamiltonian.  The prover must *decide the dichotomy* in terms
   of MPS data, and the pre-registered expectation to be confirmed or
   destroyed is: **exactness holds iff `V_α(e^{θξ})` is scalar for all `θ`**,
   i.e. exactly the dichotomy of `theory/memory-index.md` ⟨1⟩12 and A1(b).
4. **(L2.d)** On the good branch, `μ_ϖ` is the `ℓ¹`-regularised charge in the
   sense of D13(a)/D17: `μ_ϖ(m) = lim_W 2s(ϱ_m(𝔛_W) − c_0)`, and this limit
   is **not** an operator statement (§5.2).

**What it buys.**  A conditional PROVED row generalising L1 off `χ=1`, and —
whichever branch of (L2.c) holds — a *classical* shadow of the REFUTED
sector-wide charge operator.  Confirming the pre-registered expectation would
be a strong structural result: it would say the obstruction to a charge
operator and the obstruction to a moment map are the same obstruction, seen
twice.  Refuting it is equally publishable and must be reported as such (L10).

---

### L3 — `BA-ACT` (reduction, and the symmetry ACTION — the edge itself)

*This is the rung the corpus-r2 objection actually asks for.*

**ASSUME.**  L2 on its good branch, plus the reduction hypothesis proposed as
D33: `μ_ϖ` is proper on the relevant level sets, the circle action is free on
a neighbourhood of the level set, and the reduced space
`ℳ_red := μ_ϖ^{-1}(ν)/U(1)` is a smooth symplectic manifold (Marsden--Weinstein).

**PROVE.**
1. **(L3.a) Reduced description.**  `ℳ_red` is the asymptotic phase space:
   its points are (kink position) × (endpoint datum in the `PGL(χ)`-torsor
   `E_b^α` of A1(c)/D9(c′)), modulo the residual circle; the induced Poisson
   bracket `{·,·}_ϖ` is the one of `refs/arxiv-1810.07006/p4_tdvp.tex`
   restricted to `ℳ`.
2. **(L3.b) The action statement.**  The Hamiltonian flow of `μ_ϖ` on `ℳ` is
   **equal** to the endpoint action of A1(d2)/(f) restricted to `ℳ` — i.e.
   `exp(t{μ_ϖ,·})` acts on the endpoint datum as left translation by
   `ρ_α(e^{tξ}) ∈ 𝒜_eff = G/N_α`, and on the wall coordinate by translation.
   Hence **the asymptotic charge generates the asymptotic symmetry, by
   construction and not by analogy.**
3. **(L3.c) The B ⇒ A reconstruction.**  A measured memory datum `δx`
   (D13(a), the *frozen* observable, with the D17 order of limits) determines
   the asymptotic-symmetry element `ρ_α(e^{2s·δx·ξ}) ∈ 𝒜_eff` that carries
   the in-state's endpoint datum to the out-state's.  This is the sentence
   `theory/TRIANGLE.md` §6.3 names as missing, and it must be proved in
   exactly that form — *reconstruction of an action element*, not a relabelling.
4. **(L3.d) Consistency with B3.**  On the D18-separated event of B3, L3.c
   must reproduce `2s·δx + (q_out − q_in) = 0` identically.  **Any mismatch
   is a FATAL bug in the shard**, not a new result.

**What it buys.**  The edge.  `B ⇒ A` would move from SKETCH to a conditional
PROVED implication with its hypotheses (FS-conv), (FOL), free-and-proper
reduction, and `ℳ`-invariance all *named and checkable*.  This is the only
rung that changes the triangle's status table.

---

### L4 — `BA-DH` (Duistermaat--Heckman: the memory quantum from symplectic volume)

*The sharp number.  This is the rung with a falsifier attached (§6).*

**ASSUME.**  L2 (good branch) and, for the general clause, L3.

**PROVE.**
1. **(L4.a) Pushforward.**  The pushforward `(μ_ϖ)_*` of the Liouville
   measure of `(ℳ,ϖ)` is absolutely continuous with piecewise-polynomial
   density on the complement of the critical values of `μ_ϖ`, with jumps
   exactly at those critical values.  (For `dim ℳ = 2` the density is
   piecewise constant; the general statement needs `dim ℳ > 2` and is where
   the reduced space's second factor earns its keep — §5.6.)
2. **(L4.b) The Archimedes normalisation.**  The symplectic volume per
   lattice translation of the wall is `2π·2s`; equivalently, in
   Bohr--Sommerfeld/prequantum units of `2π` per state, **one lattice
   translation carries exactly `2s` quanta**, so the position quantum per
   unit escaped charge is `1/(2s)`.  The primordial example is exact and must
   be exhibited: a single spin-`s` coherent-state sphere, `μ = ⟨S^z⟩ = s\cosθ`,
   Liouville pushforward uniform on `[−s,s]` — Archimedes' hat-box theorem —
   giving `2s` quanta over the full range.
3. **(L4.c) The memory staircase.**  In the sharp-kink limit `Δ → ∞`
   (`κ → ∞`) the moment map `x_0 ↦ μ_ϖ` degenerates to a staircase with step
   `2s` per site and plateaus at integer `x_0`; the *pushforward* stays flat.
   The "memory staircase" is therefore the moment map itself, **not** the DH
   density — a distinction the shard must make explicitly, because getting it
   backwards is the obvious way to write a wrong sentence here.
4. **(L4.d) Cross-check against the corpus (mandatory).**  The quantum
   produced by (L4.b) must equal, with no fitting, the value already carried
   by three independent PROVED/conditional rows: M-quant-G's
   `spec(ΔX) ⊆ {0,−1/s}`; M-INDEX-spec's `δx = −(2s)^{-1}Σ_ν ν p_ν` on `ℤ`;
   and S2-2body-S's slope `1/S`.  A mismatch refutes the identification of
   `μ_ϖ`, not the corpus.

**What it buys.**  The strategic prize of §1.3: *the memory quantum from
symplectic volume, with no scattering theory*.  If L4.b is proved and L4.d
matches, the campaign has a second instance of the inversion that made the
memory corner work, and the DH picture becomes a genuine explanation rather
than a coincidence of numbers.

**Honest warning, pre-registered.**  In the `dim ℳ_red = 2` case, (L4.a) is
*equivalent* to (L1.b)/(L2.c) and carries no independent content; and (L4.b)
follows from (L1.d) plus lattice-translation covariance of the D13(a)
calibration.  The prover must say plainly whether DH is doing work or is a
restatement.  A shard that dresses a two-line computation in DH language and
claims a new mechanism earns a FATAL.  The place DH could do real work is
`dim ℳ_red > 2` — a kink with internal/torsor degrees of freedom, `χ > 1` —
and that is where the lane should push if L2 survives.

---

### L5 — `BA-COC` (the class `[ω_α]` in the symplectic picture — the full program claim)

*Stated as the program states it, and then stated in the form this brief
believes is the true one.  The prover's job is to decide which.*

**Program form (bd `tns-89h`, to be tested):** the A1 central extension
`[ω_α]` reappears as a classical symplectic cocycle of the moment map, i.e.
as the Souriau non-equivariance cocycle
`Σ(g,m) := μ_ϖ(g·m) − Ad^*_g μ_ϖ(m)`.

**Corrected form this brief proposes instead:** the program form is **empty**
wherever it is testable, and the surviving statement is a *prequantum-lift*
(Mackey-type) obstruction.  Reasons, all already in the corpus:
- The Souriau cocycle is an infinitesimal object, i.e. a Lie-algebra
  2-cocycle.  D4(d)'s **caveat is already PROVED-scoped**: for `𝔥_α` compact
  semisimple, Whitehead's second lemma trivialises the class in
  `H²(𝔥_α,ℝ)`, so the displayed central cocycle is a coboundary; and
  `theory/TRIANGLE.md` §1.3 states the conclusion in the sharpest available
  form: *"The lattice SPT anomaly is a group-cohomological multiplier, not a
  Lie-algebra central charge."*
- For the selected circle `H_α = U(1)`, which is the only case in which this
  campaign has a current, a ledger, and a moment map at all, `[ω_α]` is
  trivial: there is no SPT class to recover.
- The cases where `[ω_α] ≠ 0` in this corpus are **finite** groups (AKLT,
  `G = ℤ₂×ℤ₂`, four-point orbit, D9(c′) sanity check).  Finite groups have no
  Lie algebra, no current, no moment map — and the session-3 strategic record
  already flags them as *"a hard fence: no circle, no current, no ledger"*.

**PROVE (either direction, honestly).**  Exactly one of:
- **(L5.a)** an explicit `(G, {A_α}, ℳ)` with connected `G`, non-trivial
  `[ω_α]`, and a non-vanishing Souriau cocycle of `μ_ϖ` — which would refute
  this brief's reading; or
- **(L5.b)** the corrected statement: `[ω_α]` is exactly the obstruction to
  lifting the `𝒜_eff = G/N_α` action on `(ℳ_red, ϖ_red)` to the prequantum
  line bundle of `ϖ_red`, i.e. it lives in `H²(𝒜_eff, U(1))` and appears as a
  *multiplier of the lifted action*, never as a Lie-algebra central charge;
  together with the no-go that the Souriau route is empty for connected
  compact `G` by Whitehead + D4(d).

**What it buys.**  Either way, a clean row, and the removal of a piece of
program folklore before it reaches a paper.  (L5.b) also connects the Kähler
route back to Corner A's `[ω_α]` in the only way the corpus permits, and
would be the correct one-sentence outlook if TJO ever wants one.

---

## §4. DEFINITIONS THAT MUST BE ADDED (D-number proposals)

**Numbering warning.**  `definitions.md` is merged through **D28**.  D29--D31
exist as *quarantined proposals* in the soft-index shards and were **not
merged** (`theory/verdicts/soft-index-adjudication-r1.md`).  This campaign
therefore proposes **D32--D35** and must renumber at merge time if the
soft-index r2 round lands D29--D31 first.  Nothing here may be written into
`definitions.md` by a prover lane; it lives in the shard's MERGE PROPOSALS
section until an L6 loop converges (§7.4).

The drafts below are in the register of D26--D28: lettered clauses, explicit
"definition, not a theorem" fences, named hypotheses in bold parentheses,
and an explicit statement of what is *not* included.

---

> ## D32 (windowed Kähler structure on a decorated-MPS family)
>
> Let `ℳ` be a finite-dimensional smooth manifold and `m ↦ T(m)` a smooth
> family of D1(e′) two-sided decorations with fixed tail tensors `A_α, A_β`
> and fixed bond dimension `χ`, all of whose states `ϱ_m := ω_{α|β}^{(m_0)}[T(m)]`
> lie in `𝒦^{(1)}_{αβ}` (D17).  Fix a finite window `W = [a,b]` and boundary
> vectors `b_l,b_r ≠ 0` with `W` padded about the junction in the sense of
> D4(a1).
>
> **(a) Window vector family.**  `|ψ_W(m)⟩ := |ψ_W(T(m); b_l,b_r)⟩` is the
> D1(e) window vector; it is nonzero for every `m` by D4(a2).
>
> **(b) Windowed Kähler potential.**
> `𝔨_W(m) := log⟨ψ_W(m)|ψ_W(m)⟩`.  This is the pullback of the Fubini--Study
> potential along `m ↦ [|ψ_W(m)⟩]`.  It is finite for every finite `W` and, in
> general, **has no `W ↑ ℤ` limit**: on the D16 family it grows like `|W|²`
> (measured: `𝔨_W = 113.0, 417.2, 1602.9, 6284.1` at `|W|/2 = 10,20,40,80`,
> `Δ = 1.5`, `s = 1/2`).  This divergence is the lattice avatar of the
> `2πδ(0)` prefactor of `refs/arxiv-1810.07006/p2_tangent.tex`, of which the
> source says *"The factor corresponds to the system size, which diverges in
> the thermodynamic limit"*.
>
> **(c) Windowed Kähler form.**  `ϖ_W := i∂∂̄𝔨_W`, a real, closed `(1,1)`-form
> on `ℳ` (closed because it is locally exact by construction).  Unlike (b),
> `ϖ_W` is **expected** to converge: on the D16 family it is constant to 14
> digits already at `|W|/2 = 20`.  *Definition, not a theorem:* convergence is
> hypothesis (d), and positivity/nondegeneracy is a claim (L1.a/L2.a), not
> part of this definition.
>
> **(d) Hypothesis (FS-conv).**  There are `C < ∞` and `λ̃ ∈ (λ_E,1)` (D1(c))
> such that `‖ϖ_{W'} − ϖ_W‖_{K} ≤ C λ̃^{d(W,K)}` for all nested padded windows
> `W ⊆ W'` and every compact `K ⊂ ℳ`, where `d(W,K)` is the minimum
> junction-to-edge distance over `K`.  Then `ϖ := lim_{W↑ℤ} ϖ_W` exists and is
> closed.  **(FS-conv) is a hypothesis about the family, not about the model,
> and is not implied by D1(c) alone**: `ϖ_W` involves second derivatives in the
> family parameters, which D1(c) does not control.
>
> **(e) What is deliberately excluded.**  No claim that `𝔨_W` has a limit; no
> claim that the Fubini--Study *metric* or *distance* on `ℳ` converges (it need
> not — §5.3); no claim that `ℳ` is a submanifold of any Hilbert space; and no
> use of the tangent-space Gram matrix `G` of
> `refs/arxiv-1810.07006/p2_tangent.tex` without first dividing out its
> divergent prefactor, which the source performs only after left gauge fixing.

---

> ## D33 (reduced asymptotic phase space and induced Poisson bracket)
>
> Assume D32 with (FS-conv), so that `(ℳ,ϖ)` is a manifold with a closed
> `U(1)`-invariant 2-form for the selected circle `{exp(θξ)}`, `ξ ∈ 𝔥_α∩𝔥_β`.
>
> **(a) Hypothesis (FOL).**  All `ϱ_m`, `m ∈ ℳ`, are mutually normal (they
> generate the same folium).  Without (FOL) the family is a set of states with
> no common Hilbert-space home and the Fubini--Study *distance* between
> distinct points is maximal, so "smooth manifold of states" is a name without
> content.  D9(b) proves disjointness *across* labels `(α,β)`, and proves
> nothing *within* a label; (FOL) is therefore a genuine hypothesis.
>
> **(b) Nondegeneracy and the Poisson bracket.**  Where `ϖ` is nondegenerate,
> `{f,g}_ϖ := ϖ(X_f,X_g)` with `ι_{X_f}ϖ = df` is the induced Poisson bracket.
> On a uniform-MPS family it agrees with the bracket of
> `refs/arxiv-1810.07006/p4_tdvp.tex`,
> `{f,g} = −(∂_{A_i}f)(G^{-1})^{ij}(∂_{Ā_j}g) + (∂_{A_i}g)(G^{-1})^{ij}(∂_{Ā_j}f)`,
> **after** the divergent prefactor of D32(b) is divided out; the agreement is
> a claim to be proved, not a definition.
>
> **(c) Hypothesis (RED).**  The circle action on `ℳ` is free and proper on a
> neighbourhood of the level set `μ_ϖ^{-1}(ν)` (D34), and `μ_ϖ` is proper
> there.  The *reduced asymptotic phase space* is then
> `ℳ_red(ν) := μ_ϖ^{-1}(ν)/U(1)` with the unique `ϖ_red` pulling back to the
> restriction of `ϖ` (Marsden--Weinstein).  **Freeness fails exactly at
> configurations fixed by the circle** — e.g. a `φ`-independent point — and
> those are the critical values that D34/L4 must track, not hide.
>
> **(d) The intended factors, as a name only.**  When `ℳ_red` is
> two-dimensional the intended reading is *(wall position) × (endpoint datum
> in `E_b^α`)*.  `E_b^α` is a `PGL(χ)`-torsor by A1(c); **that it carries any
> symplectic structure is not asserted here and does not follow from A1** — it
> is a claim of L3 and, for `χ > 1`, an open one (§5.6).
>
> **(e) Excluded.**  No claim that the true Heisenberg dynamics preserves
> `ℳ`; no claim that the TDVP flow on `ℳ` approximates it; no claim about
> `𝒦_{αβ}` as a whole — `ℳ` is one finite-dimensional family inside one
> folium of it.

---

> ## D34 (moment map for the selected circle; equivariance; the two obstructions)
>
> Assume D32(d) and D33(a).  Let `ξ ∈ 𝔥_α ∩ 𝔥_β` be the selected unbroken
> circle direction of H-MQG(2), `S^z := −i q(ξ)` the D26 on-site charge, and
> `ξ^♯` the fundamental vector field of the circle action on `ℳ`.
>
> **(a) Moment-map candidate (the memory observable).**  For a finite window
> `W` and cut `c_0 ∈ W`, `μ_W(m) := ϱ_m(Q̂_{W,c_0}) = 2s(ϱ_m(𝔛_W) − c_0)`,
> using D13(a)'s frozen coordinate and (IDX.1).  **This is the memory
> observable of the corpus, not a new object**; the content of the definition
> is that it is *offered* as a moment map, and whether it is one is L1.b/L2.c.
>
> **(b) Moment map.**  `μ_ϖ : ℳ → ℝ` is a *moment map for the circle action*
> if `dμ_ϖ = ι_{ξ^♯}ϖ` on `ℳ`.  It exists iff the closed 1-form `ι_{ξ^♯}ϖ` is
> **exact**; it is then unique up to an additive constant, which the D13(a)
> calibration fixes.  For a circle action the relevant obstruction is the class
> `[ι_{ξ^♯}ϖ] ∈ H^1_{dR}(ℳ)`, computed concretely as the period around the
> `φ`-circle.
>
> **(c) Obstruction I — the period.**  `Per(ℳ) := ∮_{φ\text{-circle}} ι_{ξ^♯}ϖ`.
> `Per(ℳ) = 0` iff a global `μ_ϖ` exists.  *Pre-registered expectation, to be
> proved or refuted:* `Per(ℳ) = 0` iff `V_α(e^{θξ}) ∈ ℂ^×𝟙` for all `θ` —
> i.e. the moment map exists exactly on the branch where
> `theory/memory-index.md` ⟨1⟩12 does **not** obstruct the charge operator, and
> where A1(b)'s strings stabilise exactly.
>
> **(d) Obstruction II — equivariance (Souriau).**  For nonabelian `G` acting
> on `ℳ`, `Σ(g,m) := μ_ϖ(g·m) − Ad^*_g μ_ϖ(m)`; when `Σ` is `m`-independent it
> is the Souriau 2-cocycle and its class lies in `H²(𝔤,ℝ)`.  **Fence, binding:**
> by D4(d)'s caveat and `TRIANGLE.md` §1.3, this class is *not* `[ω_α]` and
> cannot represent it for compact semisimple `𝔥_α` (Whitehead), and is trivial
> for the circle.  Any shard identifying `Σ` with `[ω_α]` without proving
> L5.a earns a FATAL.
>
> **(e) Excluded — the hard fence against the REFUTED row.**  `μ_ϖ` is a
> **function on `ℳ`**.  Nothing in D34 asserts, implies, or may be used to
> assert the existence of a self-adjoint operator on any GNS space:
> `M-INDEX-LA-strong` is **REFUTED** by two independent mechanisms, and
> `theory/memory-index.md` ⟨1⟩12 refutes the strong-resolvent route on the
> A2 folium itself.  Any step of the form "the moment map exists, hence the
> charge operator exists" is FATAL.  The only permitted operator-level
> statement remains the CONJECTURE `M-INDEX-LA-folium` (implementer route),
> which this campaign neither uses nor proves.

---

> ## D35 (the precise sense of "generates asymptotic symmetries")
>
> Assume D32--D34 with a global moment map `μ_ϖ`.
>
> **(a) Generation.**  The charge *generates* the asymptotic symmetry if the
> time-`t` Hamiltonian flow of `μ_ϖ` with respect to `{·,·}_ϖ`,
> `Φ_t := exp(t\{μ_ϖ,·\}_ϖ)`, exists on `ℳ` and coincides with the endpoint
> action of A1(d2)/(f) restricted to `ℳ`: for every `m ∈ ℳ` the endpoint datum
> of `Φ_t(m)` in `E_b^α` is `ρ_α(e^{tξ})` applied to that of `m`, with
> `ρ_α : G → PGL(χ)` the *state-level* homomorphism (never the projective
> window action of A1(d1), where the multiplier is visible and the register is
> different).
>
> **(b) Reconstruction (the B ⇒ A statement).**  Memory *reconstructs* the
> asymptotic symmetry if the D13(a) datum `δx` of an event determines the
> element `ρ_α(e^{2s·δx·ξ}) ∈ 𝒜_eff = G/N_α` carrying the in-endpoint datum to
> the out-endpoint datum, with the D17 order of limits (infinite volume, then
> `t → ±∞` at fixed window, then `W ↑ ℤ`) and never with a `k → 0` interchange.
>
> **(c) What this is not.**  It is **not** the claim that `𝒜 = (G_L×G_R)/G_diag`
> is the classifying object (REFUTED, `A2-orbit-r1`; the double coset of A2(e)
> is).  It is **not** a statement about `𝒦_{αβ}` as a whole, nor about the GNS
> space (S-A1 is open).  It is **not** a claim that the true dynamics preserves
> `ℳ`.  And it is not a claim about a continuum vacuum manifold: S-A2 forbids
> using M1's kinks as superselection sectors, so `ℳ` must be built on M2/D16-type
> discretely-broken data.

---

## §5. THE HARD PARTS (obstructions, not tasks)

### 5.1 The Fubini--Study potential diverges; only the curvature survives

The ground truth is explicit that the tangent-space overlaps on a uniform MPS
carry a prefactor equal to the system size
(`refs/arxiv-1810.07006/p2_tangent.tex`: *"The factor corresponds to the
system size, which diverges in the thermodynamic limit"*), and that the Gram
matrix becomes the identity only **after** that factor is divided out.  For a
*translation-invariant* family this is a harmless common prefactor.  For the
kink family it is worse and better at once: on D16 the Kähler potential grows
like `|W|²` (measured: `113.0 → 417.2 → 1602.9 → 6284.1`) while the Kähler
form converges to 14 digits by `|W|/2 = 20`.  So there is **no global Kähler
potential in the thermodynamic limit**, and every construction must be done at
the level of the two-form (curvature), or relatively — differences of
potentials between nearby family points, which is what `i∂∂̄` computes anyway.
This is `docs/framing.md` §4 again in a new dress: *the potential is the
fundamental object* is true locally and false globally; what survives at
infinity is a curvature, i.e. exactly a symplectic form.  A shard that writes
`ϖ = i∂∂̄𝔨` with `𝔨` a function on `ℳ` in the thermodynamic limit is wrong.

### 5.2 Surviving the REFUTED sector-wide charge operator

`M-INDEX-LA-strong` is **REFUTED** by two independent mechanisms
(`theory/memory-index.md` ⟨1⟩3 and ⟨1⟩12): a log-divergent-fluctuation
counterexample off every A2 folium, and — on the A2 folium, with perfectly
tame boundary-law fluctuations — the nonscalar-`V_θ` obstruction, which shows
`{e^{iθQ̂_{W,c_0}}}_W` is not strongly Cauchy whenever `V_{θ_0}` is nonscalar.

Three consequences this campaign must respect, in order of severity.

1. **The moment map evades the refutation only because it is a function.**
   `μ_ϖ` is a real function on a finite-dimensional manifold of states.  It
   never has to converge as an operator, and the campaign's whole reason for
   preferring it is that A1(b) already tells us the *operator* does not exist
   while the *action on states* does.  This is the honest evasion and it must
   be stated in the shard exactly this way — not as "we avoid the problem"
   but as "the problem is that the object was of the wrong type".
2. **The refutation nevertheless has a classical shadow, and it may bite.**
   The nonscalar-`V_θ` mechanism is a statement about the *same* family of
   window charges whose expectation values define `μ_W`.  D34(c) pre-registers
   the expectation that the shadow is exactly `Per(ℳ) ≠ 0` — no global moment
   map.  If that is right, **L2/L3 close only on the scalar-`V_θ` branch**,
   which contains D16 (`χ=1`) and excludes every SPT-interesting family.  That
   would be a real, publishable, and disappointing result, and it must be
   reported as one (L10).
3. **The forbidden step.**  Any argument of the shape "we have a moment map,
   therefore geometric quantization gives a self-adjoint charge on the sector"
   re-derives a REFUTED row and is FATAL.  Prequantization here produces a
   line bundle over `ℳ` (finite-dimensional), never an operator on `H_{ϱ}`.

### 5.3 Is the moment map even defined on a folium rather than a Hilbert space?

`ℳ` is a family of **states on `𝔄`**, not of vectors in one Hilbert space.
The Fubini--Study construction needs a common Hilbert space, and D9(b) proves
only that *different* `(α,β)` labels are disjoint — it says nothing about two
kinks at different positions with the same labels.  Three sub-obstructions:

- **(a)** Mutual normality within `ℳ` — hypothesis (FOL), D33(a) — is
  unproved.  For the D16 family the tails are exponentially close and the
  expectation is that (FOL) holds, but "expected" is not "proved", and the
  campaign has been burned before by exactly this kind of gap (S-A1).
- **(b)** Even under (FOL), the FS *distance* can degenerate while the FS
  *form* converges.  The measured D16 behaviour (`𝔨_W ~ |W|²`, `ϖ_W`
  convergent) is precisely this situation.  So the right statement is not
  "`ℳ` is a Kähler submanifold of Hilbert space" but "`ℳ` carries a
  well-defined Kähler *form* obtained as a convergent limit of windowed
  pullbacks".  The prover must build the theory on the second statement.
- **(c)** The GNS objection of `theory/memory-index.md` ⟨1⟩2.⟨2⟩8 applies
  verbatim: `𝒦_{αβ}` is a *set of states*, and "the GNS representation of
  `𝒦_{αβ}`" has no canonical meaning without a folium choice.  Every
  statement of this campaign must therefore be indexed by a chosen family
  `ℳ`, never by a sector.

### 5.4 The class `[ω_α]` almost certainly does not appear where the program says

See L5.  Compressed: the Souriau cocycle is infinitesimal; D4(d)'s
already-scoped caveat plus Whitehead kill it for compact semisimple `𝔥_α`;
for `H_α = U(1)` — the only case with a current, a ledger, and a moment map —
`H²(U(1),U(1))` is trivial, so there is no class to recover; and the corpus's
nontrivial-`[ω_α]` examples are **finite** groups, which have no moment map
at all.  **The set where the program's cocycle statement is testable and the
set where it could be nonzero appear to be disjoint.**  I rate this the
single hardest obstruction in the brief, because it is not a gap to be
filled: it says a headline piece of the program is probably vacuous, and the
correct replacement (prequantum-lift obstruction, L5.b) is a *different*
theorem in a *different* cohomology group.

*Leaf discipline for this obstruction:* the two cohomological steps —
Whitehead's second lemma for `𝔥_α` compact semisimple (already carried by
D4(d)'s caveat, so citable as such) and the vanishing of `H²(H_α,U(1))` for
`H_α = U(1)` — must be **proved in the shard**, not asserted.  The second is
standard but this campaign does not cite standard facts from memory (L3), and
it is load-bearing for the whole of L5.

### 5.5 The variational manifold is not dynamically invariant

D16's kink family is an exact zero-energy eigenmanifold, so the *static* kink
is safe.  A scattering event is not: a magnon impinging on the wall takes the
state off `ℳ` immediately.  TDVP gives a Hamiltonian flow *on* `ℳ`
(`refs/arxiv-1810.07006/p4_tdvp.tex`), but TDVP is a projection of the true
dynamics and the projection error is exactly the quantity nobody controls.
So L3/L4 as stated are theorems about `(ℳ,ϖ)`, and the bridge to a physical
memory event requires one of: (i) restricting to asymptotic times, where the
in/out configurations are back on (a product of) the manifold — this is the
natural route and it re-imports D18/H-AD-G/AC-EX through the back door; or
(ii) a quantitative TDVP error bound, which nobody in this corpus has.  The
shard must choose one and label it.  **This is the campaign's version of
`HANDOFF_MPS_SOFT_THEOREM.md` §5.2: distinguish sharply between statements
exact on the ansatz manifold and statements about the model.**

### 5.6 The second factor of the reduced space is missing for `χ > 1`

D33(d) names the intended reduced space as *(wall position) × (endpoint
datum)*.  For D16, `χ = 1`, the endpoint torsor is a point, and the second
factor is the residual `U(1)` phase `φ` — which is exactly the circle being
reduced out, so `ℳ_red` is **zero-dimensional** and the DH statement is
degenerate.  For `χ > 1` the endpoint space is a `PGL(χ)`-torsor (A1(c)), and
**nothing in the corpus gives it a symplectic structure**.  Constructing it —
presumably as a coadjoint-orbit-like object attached to `ρ_α(G) ⊆ PGL(χ)`, or
as the reduction at a fixed moment value of a larger family — is unfinanced
work, and it is exactly the work that would make L4 non-trivial (see the
honest warning under L4).

### 5.7 Which `δx` — three ways to get this wrong

D13 freezes (a) and warns explicitly about (c): the first-moment coordinate
`X_1` is the regularised total magnetisation, exactly conserved, so
`δx^{dyn} ≡ 0` unless leg charges are subtracted first.  A moment-map shard
that reaches for "the natural conserved quantity" will land on `X_1` and
prove `0 = 0`.  Use D13(a).  Likewise `dδ_t/dk` (D15) is the transmitted
magnon's Wigner--Eisenbud shift, is smooth and unquantised, and is **not**
the wall displacement.  And `δx` itself is never claimed quantized — it is a
`{p_ν}`-average (M-INDEX-spec's binding register discipline); only the
outcome spectrum is.

---

## §6. THE PRE-REGISTERED FALSIFIER

**Discipline.**  Written, committed, and **run green before any prover lane
starts** — the memory-index and soft-index campaigns both showed this is
cheap and decisive (a probe shaped the `ν`-convention and killed a fake 5%
violation before any critic saw it; the soft-index probe passed
out-of-sample before the proof was attempted and the proof then failed while
the law survived).  Style models: `theory/checks/memory_index_probe.py` and
`theory/checks/soft_index_probe.py` — read at least one before writing.

**File:** `theory/checks/bta_moment_probe.py`.  numpy/scipy only.  Exit codes
`0` PASS, `1` FAIL (and, under `--red`, `1` means the mutation was caught —
RED-OK), `2` red mutation NOT caught.  Explicit failures only, so `python3 -O`
is equally strict.  Modes: default, `--red`, `--red-fs`, `--selftest`.

### 6.1 What is computed

Families (all defined by tensors alone; **no Hamiltonian is needed for
P1--P4**, which is the point):

- **F-A (the frozen D16 family, `χ=1`).**  Site-normalised
  `|K(z)⟩ = ⊗_n(|↑⟩_n + z q^n|↓⟩_n)`, `z = q^{-x_0}e^{iφ}`, `q = Δ−√(Δ²−1)`.
  Grid `Δ ∈ {1.5, 2.0, 4.0}`, `x_0 ∈ [0,3]` on 301 points, windows
  `W = [−L,L]`, `L ∈ {10,20,40,80}`, cut `c_0 = 0`.
- **F-B (spin-`S` product generalisation, `χ=1`).**  Same with per-site
  spin-`S` coherent states, `S ∈ {1/2,1,3/2,2}`.  **Declared as a variational
  family only**: that it is an exact kink ground family for some spin-`S` XXZ
  chain is *not* assumed and may not be asserted without a `refs/` citation
  (L3).
- **F-C (the risky one: a non-eigen deformation).**  F-A with a mismatched
  decay `q' ≠ q` in the tensor (`q'/q ∈ {0.8, 1.25}`), i.e. a family that is
  *not* an eigenfamily of any `H_kink` in the frozen model.  Purpose: decide
  whether the moment-map identity is geometry (survives) or an accident of
  exactness (dies).
- **F-D (`χ = 2`, nonscalar `V_θ`).**  A `U(1)`-covariant injective `χ=2`
  two-sided decorated family whose `V_θ` is nonscalar — reuse the twisted-
  transfer construction already registered as `IDX-C7(ii)` in
  `theory/checks/memory_index_check.py` rather than inventing one.

Computed on each family, by two independent numerical routes each:
`𝔨_W` (windowed FS potential), `ϖ_W = Ω_W\,dx_0∧dφ` (from `i∂∂̄𝔨_W`),
`μ_W = ϱ(Q̂_{W,c_0})` (from D13(a)), and `Per_W = ∮ι_{∂_φ}ϖ_W`.

**Independence requirement (binding, and the reason the thresholds below are
tight).**  `Ω_W` must come from the *geometry* side — second derivatives of
the window-vector norm — and `μ_W'` from the *observable* side — the
derivative of a window expectation value of `Q̂_{W,c_0}` — with no shared
intermediate.  Derivatives must be analytic or complex-step (machine exact);
a real central difference at `h = 10^{-4}` already carries `~10^{-10}` error
and would make P2's threshold unreachable for reasons having nothing to do
with the physics.  A probe that computes both sides from one closed form is
testing nothing and earns a FATAL from the critic.

### 6.2 Pre-registered gates (thresholds FIXED IN ADVANCE)

| gate | statement | criterion | families |
|---|---|---|---|
| **P1** | *Potential diverges, curvature converges* (§5.1 as a measurement) | `𝔨_W` grows with `|W|` with fitted growth exponent `≥ 1.5`, AND `|Ω_{W'} − Ω_W| ≤ 10^{-10}` for `L = 40 → 80` | F-A, F-B |
| **P2** | **Moment-map identity** `dμ_W = ι_{∂_φ}ϖ_W` | `max_{x_0,Δ,S} |μ_W'(x_0) + Ω_W(x_0)| ≤ 10^{-12}·max(1,Ω_W)` | F-A, F-B |
| **P3** | **The quantum** (DH/Archimedes normalisation) | `|(1/2π)∮∮ϖ_W − 2S| ≤ 10^{-8}` per unit lattice translation, for every `S`; equivalently position quantum `= 1/(2S)` per unit escaped charge | F-A, F-B |
| **P4** | **Corpus cross-check, no fitting** | the `ν = 2` transmission event predicted by P3 gives `δx = −1/S`, matching M-quant-G's `spec(ΔX) ⊆ {0,−1/s}` and S2-2body-S's slope `1/S` to `10^{-8}` | F-B vs `theory/checks/spin_s_slope_check.py`, `numerics/results/spin1-bc-falsifier.json` |
| **P5** | **The real falsifier: geometry or accident?** | P2 must still hold on F-C to `10^{-12}`.  **If P2 fails on F-C, the identification `μ_ϖ = ⟨Q̂⟩` is an artefact of exactness and rungs L2--L4 are dead as stated.** | F-C |
| **P6** | **The `[ω]`/nonscalar-`V_θ` obstruction test** | compute `Per_W`.  Pre-registered prediction: `|Per_W| ≤ 10^{-10}` on F-A/F-B/F-C (scalar `V_θ`) and `|Per_W| ≥ 10^{-3}` on F-D (nonscalar).  **Either outcome is informative; the falsifier is `|Per_W| ≥ 10^{-10}` on F-A**, which would kill the picture at its base case. | all |

**Red modes (must fail, i.e. exit 1):**
`--red` mutates the D13(a) calibration `2s → 2s+1` (must break P2, P3, P4);
`--red-fs` computes `ϖ` from the *unnormalised* window vectors, i.e. keeps
the divergent part (must break P1 and P2).
A checker that cannot be made to fail is not a checker (L1).

**Already-measured values, for the probe author to reproduce and for a critic
to attack.**  On F-A/F-B by an independent throwaway script during the
writing of this brief: `max|Ω_W + μ_W'| = 1.8·10^{-15}` over
`S ∈ {1/2,1,3/2,2}` × `Δ ∈ {1.5,2,4}` × 301 values of `x_0`;
`(1/2π)·(area per lattice period) = 1.000000000000, 2.000000000000,
3.000000000000, 4.000000000000` for `S = 1/2,1,3/2,2` (i.e. `2S`, exactly);
`𝔨_W = 113.03, 417.16, 1602.86, 6284.09` at `L = 10,20,40,80` (`Δ=1.5,
S=1/2`) against `Ω_W = 0.99955394152379, 0.99955394489022, 0.99955394489022,
0.99955394489022` (converged at 14 digits by `L = 20`).  **These are
throwaway numbers with no L5 status; the probe must recompute them from
scratch, and a critic should assume they are wrong until reproduced.**

### 6.3 What would actually refute the moment-map picture

In descending order of how much it would cost the campaign:
1. **P6 fails on F-A** (nonzero period at `χ=1`): no moment map even in the
   benign case; the route is dead.
2. **P5 fails**: the identity is an artefact of the exact family; L2--L4 must
   be restated for exact families only, which makes the edge model-specific
   and probably not worth a companion paper.
3. **P3/P4 disagree**: the DH normalisation does not reproduce the corpus's
   independently established `1/s`; then either `μ_ϖ ≠ ⟨Q̂⟩` or the
   Bohr--Sommerfeld counting is being done wrong — in either case the
   "quantum from symplectic volume" headline is gone.
4. **P1 fails** (curvature does not converge): (FS-conv) is false and D32(d)
   must be replaced by a relative construction; recoverable but expensive.

---

## §7. THE LANE PLAN

### 7.1 Order (strict; do not parallelise across the gate)

```
  step 0  probe        write + commit theory/checks/bta_moment_probe.py,
                       green before any prover starts.  Owner: Sonnet or Opus.
                       GATE: if P6 fails on F-A, STOP and report; do not
                       spend a prover.
  step 1  prover P-1   L1 (BA-MM-fin) + the D32/D34(a,b) drafts.
                       codex xhigh ("rottweiler" register — exhaustively
                       specified goal, per the standing TJO note).
  step 2  critic C-1   Opus, adversarial, on the L1 shard.  Lens: is the
                       identity exact or is a window term being hidden; is
                       the chi=1 fence stated; is D13(a) (not D13(c), not
                       D15) the observable.
  step 3  prover P-2   L2 + L5 (BA-MM-mps, BA-COC) with D32(d)/D33/D34(c,d).
                       Cross-family: if P-1 was codex, P-2 is Opus.
                       L5 is deliberately paired with L2 because both turn on
                       scalar-vs-nonscalar V_theta.
  step 4  critic C-2   Opus or codex (whichever P-2 was not).  Lens 1: the
                       REFUTED-row fence of D34(e) - hunt for any step that
                       manufactures an operator.  Lens 2: (FOL) and folium
                       discipline.  Lens 3: recompute the Whitehead/H^2(U(1))
                       argument of L5 independently and try to build the
                       L5.a counterexample.
  step 5  adjudicate   orchestrator (Opus) writes
                       theory/verdicts/bta-kahler-r1.md, recomputing every
                       disputed point independently.
  step 6  prover P-3   L3 (BA-ACT) only if L2 landed on the good branch;
                       L4 (BA-DH) only if 5.6 got a second factor.
                       If neither, STOP: the honest outcome is a fenced
                       conjecture + the L5 negative (see 8).
```

Rationale for the order: L1 is cheap and de-risks the vocabulary; L2 and L5
share the single structural question (scalar `V_θ`), so one prover should own
both; L3 and L4 are worthless if L2 lands on the bad branch, so they are
budget-gated behind it.

### 7.2 Prover contract

Writable files: **one shard only**, `theory/bta-kahler.md`, plus (step 0 only)
the probe.  Lamport structured proofs (L6b): `⟨1⟩1, ⟨2⟩3, …`, explicit
ASSUME/PROVE per nontrivial step, terminal QED steps, **every leaf justified
by a D-number, a claim id, a named computation, or a `refs/` file+location**.
Final sections, mandatory: (i) MERGE PROPOSALS — exact replacement text for
`definitions.md` D32--D35, `claims/CLAIMS.md` rows at status SKETCH,
`notation.md` rows (see 7.3); (ii) CHECKER SPEC — a machine-checkable
certificate for at least one load-bearing step, with a mutation that must
fail; (iii) HONEST STATUS — what was proved, what was assumed, what broke.
Self-status is SKETCH; only the L6 loop promotes.  Do not edit any shared
file.  Do not touch `paper/`.  Do not touch `numerics/`.  Work autonomously.

If a prover is a Fable subagent (L7 permits it only for paper prose, so this
should not arise here), the one-Lamport-section-per-response discipline that
rescued S1-B is mandatory.

### 7.3 Notation proposals (new rows only; nothing existing may be redefined)

`ℳ`, `ℳ_red` (the family and its reduction, D32/D33); `𝔨_W` (windowed Kähler
potential — note `𝔨` is fresh; do **not** reuse `𝒦`, which is the kink
sector); `ϖ_W`, `ϖ` (Kähler/symplectic form — do **not** use `ω`, which is
already the cocycle `ω_α(g,h)`, the dispersion `ω(k)`, and the states `ω_α`);
`μ_ϖ` (moment map — subscripted because bare `μ` is already the spin-`S`
contact polynomial `(2S−1)a+b` and the source-norm index `‖O‖_μ`; the shard
must add an overload note in the register `notation.md` already uses);
`ξ^♯` (fundamental vector field); `Per(ℳ)` (the D34(c) period);
`{·,·}_ϖ`; hypotheses `(FS-conv)`, `(FOL)`, `(RED)`.

### 7.4 Merge discipline

No shared-file merge until the L6 loop converges on the shard concerned —
this is the rule the soft-index round enforced when no lane converged and
D29--D31 stayed quarantined.  Concretely: `definitions.md`, `notation.md`,
`claims/CLAIMS.md`, `theory/TRIANGLE.md` are **orchestrator-only**, edited in
lockstep in a single commit after adjudication, with the verbatim adjudicated
scoping copied into the CLAIMS row (the pattern used for M-INDEX-fin/-spec).
Renumber D32--D35 if the soft-index D29--D31 land first.  Edge-status changes
in `TRIANGLE.md` §6.3 and §7 require an adjudicated verdict file, never a
prover's self-assessment.  Parallel repair lanes get a reconciliation pass
before adjudication (session-3 ops note: lane A's doc edits went stale when
lane B landed later).

### 7.5 bd

`tns-89h` is the parent (P3, OPEN).  File children per rung
(`bta-L1`…`bta-L5`) and one for the probe; block L3/L4 on L2.  Record the
outcome of P5/P6 as a bd memory whatever it is — a negative here is a real
result and the campaign has a habit of forgetting negatives that were only
ever in a log.

---

## §8. HONEST ASSESSMENT

My assessment is that this edge is **partially reachable, and that the honest
outcome is a narrow theorem plus a well-fenced conjecture plus one sharp
negative — i.e. a companion paper, not a section of the current Letter.**
L1 is genuinely provable now, exactly and unconditionally, and it is a real
if modest result: it turns D16's *name* "conjugate pair" into a theorem and
identifies the frozen memory observable as a moment map.  L2 and L3 are
reachable at the campaign's rigour standard **only on the scalar-`V_θ`
branch**, which is `χ = 1` product vacua — and there the reduced space is
zero-dimensional, so L4's Duistermaat--Heckman content collapses to a
restatement of L1.d, and the "memory quantum from symplectic volume"
headline, while true, is a two-line computation wearing a large hat.  On the
nonscalar branch — every SPT-interesting family — I expect the period
obstruction of D34(c) to be nonzero, mirroring the mechanism that already
REFUTED the sector-wide charge operator, so that there is no global moment
map and L3 does not close.  And L5, the piece of the program with the most
rhetorical appeal, I expect to come back negative: the Souriau cocycle is
infinitesimal and dies by Whitehead exactly where `[ω_α]` is interesting,
`[ω_α]` is trivial for the circle where the machinery works, and the
nontrivial cases are finite groups with no moment map at all — so the
program's "central extension reappears as a classical symplectic cocycle" is
probably vacuous and must be replaced by a prequantum-lift obstruction, which
is a different theorem.  Against all of that: the edge *is* currently held at
SKETCH by a one-sentence objection, and L3.b/L3.c would answer that sentence
in precisely its own terms, which is worth a real attempt even at these odds.

**What would change my mind, specifically.**  (i) If P5 passes and the
prover proves L2 *unconditionally* — with (FS-conv) derived from D1(c) rather
than assumed — then the construction is geometry, not accident, and L3 for
general `χ` becomes a live target rather than a hope.  (ii) If the second
factor of §5.6 is constructed, so that `dim ℳ_red > 2` and DH has actual
piecewise-polynomial content with jumps at genuine critical values, then L4
stops being a restatement and the "quantum from volume" claim earns its
headline.  (iii) If P6 comes back with `Per(ℳ) = 0` on a nonscalar-`V_θ`
family, my central structural expectation is wrong in the campaign's favour
and L2/L3 close in generality.  (iv) If someone exhibits L5.a — a connected
`G`, nontrivial `[ω_α]`, nonvanishing Souriau cocycle — the whole §5.4
pessimism is wrong and the program's most attractive claim is back.  Any one
of (i)+(ii) together, or (iii), would move my recommendation from "companion
paper" to "reopen the question of whether this belongs in the Letter" — a
question that is TJO's to answer, not this brief's, and that §0.2 forbids any
lane from pre-empting.
