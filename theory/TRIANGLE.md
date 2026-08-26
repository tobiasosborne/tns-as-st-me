<!-- ROLE: D2 of HANDOFF_MPS_SOFT_THEOREM.md §4 — the campaign framework.
     Post-corpus-r2 repair: adjudicated promotions are applied; parent SPT
     rows remain SKETCH awaiting focused critic r3. -->

# TRIANGLE.md — the 1D lattice infrared triangle

Definitions are `definitions.md` D1--D25 and symbols are `notation.md`.
**Authoritative L5 statuses:** `PROVED`, `SKETCH`, `CONJECTURE`, `REFUTED`.
Empirical, conditional, under-review, and future-work descriptions are prose
qualifiers, not extra status values.  `PROVED` requires an L6 promotion.  The
promotions below are exactly those in `verdicts/corpus-r2.md`; every HOLD
remains at its prior status with the named missing step recorded.

**Two standing TJO directives.**  *Generality*: Corner A is general.  The
present memory shard proves only conditional charge arithmetic and studies the
spin-`1/2` D16 model; the general `(G, injective MPS, finite-range H)` memory
theorem is a known gap tracked by bd `tns-zw2`, not asserted here.
Universality of the soft coefficient is scoped to `𝒮_W` (D24(d)).
*Integrability* (bd `tns-e50`): no theorem hypothesis mentions integrability.  Bethe is **verification only**:
`oracle-bethe.md` supplies O1--O10 as an oracle the derivations must match, and `ml2-completeness.md` proves two-body
completeness from the D6 swap algebra by direct Jacobi diagonalisation, not from assumed completeness.

## §0. Standing hypotheses (named once, cited by name)

| tag | statement | where |
|---|---|---|
| **(H1)** | infinite chain `ℤ`, quasi-local algebra `𝔄`, injective canonical-form uniform MPS family `{A_α}` of common bond dimension `χ` | D1 |
| **(H2)** | `G` compact (finite or compact Lie), on-site `u : G → U(ℂ^d)`; `G`-covariant vacuum family with action `g·α`, stabiliser `H_α := {g : g·α = α}` | D2(a) |
| **(H3) = (S)** | when `G`-derivatives are taken: `C¹` local sections `ε ↦ A_{exp(εξ)·α}`, `ε ↦ V_α(exp(εξ))`, `V_α(e)=𝟙` | D2(e) |
| **(H4)** | when a Hamiltonian appears: `H = Σ_x h_x`, translation invariant, **finite range `R_h`**, `G`-invariant on-site | D10 |
| **(T)** | `G` acts transitively on `Ω_vac`.  **Not implied by (H2)** — without it every classification holds *per `G`-orbit* | D9(d) |
| **(W1)/(W2)** | WI window hypothesis: `Λ ⊇ R` with D1(e) edge-bond insertions, **or** `Λ ⊇ [a−1,b+1]` | D1(e) |
| **padded** | `≥ n_0` sites each side of the bond, `b_l,b_r ≠ 0`: a **sufficient**, tensor-independent hypothesis for injectivity of `ι_{Λ,b}` — not necessary for every particular tensor (`corner-a-r3.md` residue 1) | D4(a1) |
| **(H-AD)** | coherent AD1--AD4 wave-operator/channel/local-decay hypothesis.  The old norm-mixture reading is superseded | D18 |

**Normal ordering.**  `ǔ_α(g) := e^{−iθ_α(g)}u(g)` is a unitary rep of `H_α` satisfying (IT) with phase `1` (D2(d)).
Statements labelled *normal ordered* are false without it: the WI phase `e^{i|R|θ_α(g)}` is extensive in `|R|`.

---

## §1. Corner A — the asymptotic symmetry (PROVED)

Shards `corner-a.md`, `corner-a-kinks.md`, `corner-a-goldstone.md`; pitfalls and terminology `corner-a-pitfalls.md`.
Checker `theory/checks/corner_a_check.py`, checks **C0--C11**, all pass.  L6 loop converged at r3
(`verdicts/corner-a-r3.md`, PASS).

### 1.1 Lemma IT — PROVED (`corner-a.md` ⟨1⟩2)

*Assume (H1),(H2).*  For all `g,h ∈ G`: (i) `θ_α(hg) = θ_α(g) + θ_{g·α}(h)` and `V_{g·α}(h)V_α(g) = e^{iω_α(h,g)}V_α(hg)`;
(ii) on `H_α`, `θ_α` is a homomorphism and `ω_α` a `U(1)`-valued 2-cocycle whose class `[ω_α] ∈ H²(H_α,U(1))` is
independent of the phase choice, the MPS gauge, and blocking; (iii) (unbroken) `ǔ_α` is a unitary rep of `H_α`; (iv)
(unbroken) `V_α(g)rV_α(g)^† = r` and `E ∘ Ad(V_α(g)) = Ad(V_α(g)) ∘ E`.  *Ground truth:* refs/arxiv-0802.0447 Lemma 1 +
C2; refs/arxiv-2011.12127 Eq. (eq:XAX=B).

### 1.2 Theorem WI (truncated-symmetry / "MPO Ward" identity) — PROVED

*Assume (H1),(H2), finite `R = [a,b]`, `g ∈ G`, and (W1) or (W2); boundary vectors arbitrary.*  Then **exactly**, as
window vectors, `U_R(g)|ψ_Λ(A_α;b_l,b_r)⟩ = e^{i|R|θ_α(g)}|ψ_Λ(T_R^{(g)};b_l,b_r)⟩`, where `T_R^{(g)}` carries `A_α` on
`Λ∖R`, `A_{g·α}` on `R`, and exactly two bond insertions — `V_α(g)^{-1}` on `∂_-R`, `V_α(g)` on `∂_+R`; and **as states,
with no phase**, `ω_α(U_R(g)^† O U_R(g)) = ω_α[T_R^{(g)}](O)` for all `O ∈ 𝔄`.

Two hypotheses are load-bearing.  (a) *Window*: for `Λ = R` with interior bonds only the identity is **false**
(discrepancy `1.658`, **C2**); D1(e)'s edge-bond insertions restore exactness (`0.0`, **C2b**). (b) *Orientation*:
`V^{-1}` on `∂_-R`, `V` on `∂_+R` — the **opposite** of `HANDOFF_MPS_SOFT_THEOREM.md` §1.2 line 42, a historical document
that is not edited.  A `ℤ₂` tensor with `V = Z = V^{-1}` is blind to the flip; **C1** uses `U(1)` with `V(t)=e^{itZ/2}`:
`5.6·10^{-17}` correct versus `0.267` flipped (**C1b**). *Shard:* `corner-a.md` ⟨1⟩3.  *Checks:* C0, C1, C1b, C1c, C2,
C2b.

### 1.3 Theorem A1 (endpoint torsor, charge algebra, `[ω_α]`) — PROVED

*Assume (H1),(H2), the **unbroken** case `H_α = G`, and normal ordering; every clause mentioning `𝒲_{Λ,b}` or `𝒱_b`
additionally assumes the window is padded about `b`.*

| | statement |
|---|---|
| **(a)** *charges live on one bond* | The half-infinite operations of D3(c) exist **as maps on states**, `1_{[x,∞)}g ⊳ ω_α = ω_α^{V_α(g)^{-1}@(x−1\|x)}`, and the convergence is *exact* — eventually constant on each `𝔄_W` — not asymptotic |
| **(b)** *non-implementability, as an iff* | `(U_{[x,y]}(ǔ_α(g))Ω_A)_y` fails to be Cauchy in `H_A` **iff** `V_α(g) ∉ ℂ^×𝟙`; for scalar `V_α(g)` the strings stabilise exactly.  So the half-infinite symmetry is implemented on states but by **no** strongly convergent operator sequence |
| **(c)** *endpoint bijection* | `ω_α^{M@b} = ω_α^{M'@b}` **iff** `M' ∈ ℂ^×M`; hence `[M] ↦ ω^{M@b}` is a canonical bijection `PGL(χ) → E_b^α` and `E_b^α` is a `PGL(χ)`-**torsor** (check **C6**) |
| **(d1)** *window register* | On a **padded** window `ι_{Λ,b}` is injective, so `𝒱_b(M) := ι ∘ L_M ∘ ι^{-1}` is a well-defined linear operator and `𝒱_b(h)𝒱_b(g) = e^{iω_α(h,g)}𝒱_b(hg)` — a linear rep of the twisted group algebra `𝔞_α = ℂ_{ω_α}[G]` in which the multiplier acts **nontrivially**.  Without padding, injectivity is not guaranteed and the rule can fail to define an operator at all: an injective `ℤ₂`-symmetric counterexample has `ι(N)=0` while `‖ι(ZN)‖_∞ = 4` (**C8**, **C8b**) |
| **(d2)** *state register* | The induced action on **states** kills the multiplier and is the genuine homomorphism `ρ_α : G → PGL(χ)`, `ker ρ_α = N_α` |
| **(d3)** *what `[ω_α]` obstructs* | **Removing the multiplier**, i.e. lifting `ρ_α` to an honest `G → U(χ)`.  It does **not** obstruct the projective window action of (d1), which exists for every `[ω_α]` |
| **(e)** *stabiliser and orbit* | `S_α = {(g_L,g_R) : g_Lg_R^{-1} ∈ N_α} ⊇ G_diag`, equal **iff** `N_α = {e}`; the orbit is `𝒜_eff = G/N_α`, a genuine group.  `𝒜 = (G_L×G_R)/G_diag` is a group only for abelian `G` and is **never** the orbit unless `N_α = {e}` |
| **(f)** *what acts on what* | `𝒜_eff` acts simply transitively on `ρ_α(G) ⊆ E_b^α` and does not move the sector label `(α,α)`.  Any scalar `V_α` gives a **one-point** orbit; AKLT with `G = ℤ₂×ℤ₂` a **four-point** orbit |
| **(g)** *invariance* | `[ω_α]` is constant along any continuous path of `G`-symmetric injective canonical-form tensors, provided `H²(G,U(1))` is discrete |

**Central-extension caveat (a genuine disanalogy with the continuum).**  The Lie-algebra cocycle of
D4(d) is only the local infinitesimal image of `[ω_α]` and generally loses it:
for `𝔥_α` compact semisimple, Whitehead says its cohomology class is trivial,
so the central cocycle can be gauged away by a phase-section choice but need
not vanish in every section; `[ω_α]` may still be a nontrivial torsion class
(AKLT).  **The lattice SPT anomaly is a
group-cohomological multiplier, not a Lie-algebra central charge**, and this must be said wherever `docs/framing.md` §2 is
invoked. *Shard:* `corner-a.md` ⟨1⟩4.  *Checks:* C6, C8, C8b.

**SKETCH box S-A1 (load-bearing).**  Not proved: that `ω_α^{M@b}` is a *normal* state of `π_α(𝔄)''`, i.e. that `𝔞_α` acts
on the GNS Hilbert space rather than on finite-window spaces `𝒲_{Λ,b}`; the expected route is the split property.  **This
is exactly `docs/framing.md` §1--§2's demand that the charge algebra act on the physical state space, and that demand is
NOT met.**  Anything phrased as "the charge algebra acting on `H_A`" — D21's `H_edge`, i.e. its hypothesis **(H-split)**, included — inherits this status.
(`corner-a.md` ⟨1⟩4.⟨2⟩9.)

### 1.4 Theorem A2 (broken case: sector jump; vacuum-pair classification) — PROVED

*Assume (H1),(H2), WI, `|Ω_vac| ≥ 2`; fix `α` and `g ∈ G` with `β := g·α ≠ α`.*

| | statement |
|---|---|
| **(a)** *finite `R` never leaves the sector* | For every finite `R`, `ω_α ∘ Ad(U_R(g)^†) ∈ 𝒦_{αα}` — a kink at `∂_-R` and an antikink at `∂_+R`, total topological charge zero |
| **(b)** *weak-\* limit, with rate* | For `O ∈ 𝔄_W`, `w := max W`, `y > w`, and for **every** `λ̃ ∈ (λ_E,1)` there is `C_λ̃ < ∞` with `\|ω_α(U_{[x,y]}(g)^†OU_{[x,y]}(g)) − ϱ_x^{(g)}(O)\| ≤ C_λ̃‖O‖λ̃^{y−w}`, with `ϱ_x^{(g)}` the **two-sided** decorated state of D1(e′).  The rate is `λ̃`, **not** `λ_E` — a bare `λ_E^{y−w}` is false when `E` has a Jordan block at modulus `λ_E`.  No norm convergence in `𝔄^*`; no strong operator limit |
| **(c),(d)** *the sector jump* | `ϱ_x^{(g)} ∈ 𝒦_{α,g·α}`, disjoint from the vacuum folium: every approximant is a vector state of `H_{ω_α}`, the limit is not normal with respect to it.  **The jump is invisible at every finite `\|R\|` and is created entirely by the surviving end** |
| **(e)** *vacuum-pair classification, **under (T)*** | `G_L × G_R` acts componentwise on `Ω_vac × Ω_vac`.  Under **(T)**, `Ω_vac ≅ G/H_α` and `Ω_vac × Ω_vac ≅ (G/H_α) × (G/H_α)`, transitively, with stabiliser of `(α',β')` equal to `H_{α'} × H_{β'}`; the complete invariant **modulo the global (diagonal) symmetry** is the **double coset** `𝔡(α_L,α_R) = H_α g_L^{-1}g_R H_α ∈ H_α\G/H_α`.  For `G = SU(2)`, `H_α = U(1)`: the relative polar angle `cos θ = n̂_L·n̂_R`, pair space `S²×S²` (dim 4), **not** `(G×G)/G_diag ≅ SU(2)` (dim 3).  Verified: the relative angle is diagonal-invariant to `1.4·10^{-16}` while `‖g_Lg_R^{-1} − hg_Lg_R^{-1}h^{-1}‖ = 1.364` (**C7**) |
| **(f)** *inverse direction* | Every kink sector `𝒦_{αβ}` with `β ∈ G·α` is reached this way |

*Shard:* `corner-a-kinks.md` ⟨1⟩8--⟨1⟩9 (Lemma D supplies sector disjointness). *Checks:* C7, C11.

**SKETCH box S-A2 (load-bearing).**  A2 is closed only *pointwise in `g`*.  For `Ω_vac` a continuum (M1, `Ω_vac ≅ S²`) it
produces an uncountable family of mutually disjoint sectors with **no uniform separation**: the kink creation energy tends
to zero as `g → e`, so the sectors are algebraically superselected but not energetically separated.  Missing: a
`g`-uniform statement, and a selection criterion cutting the continuum down. **Consequence: M1's kinks must not be used as
superselection sectors in Conjecture S.  M1 is the magnon model; M2 is the kink model.**  (`corner-a-kinks.md`
⟨1⟩10.⟨2⟩3.)

### 1.5 Theorem G0 (Goldstone tensor, kinematic factor, continuity equation) — PROVED

*Assume (H1)--(H4).*

| | statement |
|---|---|
| **(a)** | For `ξ ∈ 𝔥_α`, normal ordered: `B_G(ξ) = 𝒩_0(X_α(ξ))` |
| **(b)** *the dichotomy, quantified over **all** `ξ ∈ 𝔤`* | `B_G(ξ) ∈ ran 𝒩_0 + ℂA_α` **iff** `ξ ∈ 𝔥_α`.  For a broken direction it is **not** that (IT) fails — D2(b) gives (IT) for every `g`, with target `A_{g·α}`; what fails is the **same-vacuum return** |
| **(c)** *exact finite-window identity* | For `ξ ∈ 𝔥_α`, normal ordered, on `Λ = [a,b]`, with `X := X_α(ξ)`: `\|Φ_k^Λ(B_G(ξ))⟩ = (1−e^{ik})Σ_{m=a}^{b−1}e^{ikm}\|ψ;X@m⟩ + e^{ikb}\|ψ;X@b⟩ − e^{ika}\|ψ;X@(a−1)⟩` — it carries **two `Θ(1)` boundary terms**.  The clean form `(1−e^{ik})\|Φ_k(A_αX_α(ξ))⟩` holds **only** in the D12(b) δ-normalised sense; for decaying profiles the correct statement is the real-space SBP identity with `f ∈ ℓ¹∩BV` (D12(a′)), never a fixed-`k` equation with a `c_0` hypothesis (**C9**: the truncated display is off by `0.4506`, the corrected forms by `5.9·10^{-17}`) |
| **(d)** *lattice Noether / the bond potential* | Exactly on the vacuum, no limit, no boundary term, `ξ ∈ 𝔥_α` normal ordered: `q_x(ξ) ▹ ω_α = (𝒥_{x\|x+1}(ξ) − 𝒥_{x−1\|x}(ξ)) ▹ ω_α`.  *The physical charge density acting on the vacuum is the lattice divergence of a purely virtual (bond) quantity* — `docs/framing.md` §4's "the potential is the fundamental object", as a theorem |
| **(e)** *continuity equation, any `ξ ∈ 𝔤`, finite range* | With the cut current `j_{m\|m+1}(ξ) := −[H, Σ_{y≤m}q_y(ξ)] ∈ 𝔄_loc` (D10(a)): `[H,q_x(ξ)] = j_{x−1\|x}(ξ) − j_{x\|x+1}(ξ)`; for every `f ∈ 𝔉_c(ξ)`, `[H,Q[f;ξ]] = Σ_x (Δf)(x)\,j_{x\|x+1}(ξ)`; in the wave-packet sense `[H,Q_k(ξ)] = (e^{ik}−1)J_k(ξ)` |

*Supporting:* **Lemma SBP** (⟨1⟩5) — the exact master identity *with* its two boundary terms, the uniform bound
`‖𝔅_Λ[f,X]‖ ≤ 2C_∂‖X‖max(|f(a)|,|f(b)|)`, and the rank drop `rank 𝒩_k = χ²` for `k≠0`, `χ²−1` at `k=0`. **Proposition FM**
(⟨1⟩7) — for M1: `H_α = U(1)`, `[ω_α] = 0`, the type-B count `2 → 1`, and `ω(k) = J(1−cos k)` **rederived from G0(e)**,
matching oracle **O1**. *Shard:* `corner-a-goldstone.md`.  *Checks:* C3, C3b, C4, C5, C9, C10.

**Negative row `G0-soft-r1` — REFUTED (withdrawn overclaim).**  `(e^{ik}−1)` is a *kinematic* factor from the profile alone.  It is **not** a
soft factor: no Adler zero, no universality, no rederivation of O7/O9.  In a matrix element the identity says only
`⟨out|[H,Q_k]|in⟩ = (e^{ik}−1)⟨out|J_k|in⟩`; if `⟨out|J_k|in⟩ = C_hard + O(k)` then hard data enters at `O(k)`, and if it
has a `1/k` singularity there is no zero at all.  The factor is convention-dependent (`e^{−ikx}` gives `e^{−ik}−1`).
**Negative row `A2-orbit-r1` — REFUTED.** `[g_Lg_R^{-1}] ∈ 𝒜` is not diagonal-invariant; the double coset of A2(e)
replaces it.

---

## §2. Corner C — the soft theorem

### 2.1 Oracle facts O1--O10 — PROVED (verification role only)

`oracle-bethe.md`; L6 converged at r2 (`verdicts/oracle-bethe-r2.md`, PASS); checker `oracle_bethe_check.py`.  Every
formula follows from the D6 bond permutation.  Used downstream: **O1** (`ω(k)=J(1−cos k)`, `v(k)=J sin k`), **O5** (unique
two-magnon bound state, `E_b(K)=J sin²(K/2)`, canonical `0<|K|≤π`), **O6** (`S_{12} → 1`), **O7/O8/O9** (the two-body soft
expansion), **O10** (the energy-coordinate Puiseux series `δ_{12} = 2σ√(2ω_s/J) + O(ω_s)` — which is *why* every soft
statement in this campaign is an expansion in `k`, not in `ω`).

### 2.2 Theorem ML2 (complete two-magnon resolution) — PROVED

*Assume D6--D8, `J>0`, and `N>3` in finite volume.*  (1) On the `N`-site ring every nonzero two-magnon Bethe vector is a
real-pair, complex-pair, or descendant vector; for even `N` one further **singular** vector `|χ_π⟩` completes the `K≡π`
fiber; the coincident solutions are zero vectors; the physical vectors number exactly `N(N−1)/2` and form an orthonormal
eigenbasis.  (2) On the infinite chain the two-magnon space is the orthogonal sum of the D7 scattering representation and
one bound-magnon band, with resolution of the identity (21). (3) Consequently the finite-volume expansion (R6) of
`soft-current-recon.md`, with the singular class and coefficient separated as in (23)--(24), is **unconditional**. The
proof diagonalises each total-momentum relative Jacobi matrix directly; it does **not** assume Bethe completeness, and a
formal zero Bethe vector is never counted as a state — which is what makes the two-body statement integrability-free per
`tns-e50`. *Shard:* `ml2-completeness.md`.  *Verdict:* `ml2-r2.md` PASS (10/10 mutants killed). *Checker:*
`ml2_completeness_check.py`, `SIZES = (6,10,11,12,13,14,16,18,20,22,26)`.

### 2.3 S2-2body (two-body soft expansion, M1) — **PROVED**

Promoted per `corpus-r2.md` adjudication.  The narrow exact two-body
multiplier/phase expansion follows from the local contact equation with the
uniform compact-hard remainder and matches the passed oracle.  This does not
promote S-general or process independence.

**ASSUME.**  (i) D6: the isotropic spin-1/2 Heisenberg ferromagnet `H = Σ_x (J/2)(1−P_{x,x+1})`, `J>0`, on `ℤ` or on an
`N`-site ring with `N>3`. (ii) D7's ordered-coordinate convention and channel reading.  (iii) A hard momentum `k_h` with
`0 < |k_h| < π` held fixed and a signed `k_s → 0`; for the uniform statement `k_h` in a compact `[a,b] ⊂ (0,π)` and
`(k_s,k_h) ∈ D_{ab}` (`ε_{ab}`, `D_{ab}` as in `oracle-bethe.md` ⟨1⟩3.⟨2⟩3).  (iv) Plane waves occur only after smearing
by `C_c^∞` packets (D3(a)).  **No integrability hypothesis is assumed.**  What is used: the exact current `j^-_{x,x+1} =
(J/2)(S^-_{x+1}−S^-_x)P_{x,x+1}` (R1); that a two-magnon scattering eigenwave is a sum of two free plane waves away from
contact; and ML2's completeness.

**PROVE.**  With `S_phys` the physical out/in ratio and `δ_phys` its continuous phase branch vanishing at `k_s = 0`,

  `δ_phys = 2 sgn(v_h−v_s) k_s + (|v_h|/ω_h) k_s² + R_δ`,
  `S_phys = 1 + 2i sgn(v_h−v_s) k_s + [ i|v_h|/ω_h − 2 ] k_s² + R_S`,

with `|R_δ| ≤ C_δ(a,b)|k_s|³` and `|R_S| ≤ C_S(a,b)|k_s|³` uniformly on `D_{ab}`, and `C = Θ(a^{-2})` as `a ↓ 0`. The
quadratic coefficient is the **even invariant** `|v_h|/ω_h = (2J−ω_h)/|v_h| = √((2J−ω_h)/ω_h)`, reducing to `cot(k_h/2)`
on D8's half-zone. On D8, `sgn(v_h−v_s) = +1` and the linear coefficient is `2`.

**Where the `2` comes from — the FM-derived route, not the Bethe formula.**  Normalise the incoming coefficient to `1`
and call the unknown outgoing coefficient `s(k_s,k_h)`.  The contact bond imposes the single algebraic equation
`(2z_h − z_sz_h − 1)s + (2z_s − z_sz_h − 1) = 0` (R16); since `z_h ≠ 1` the analytic implicit-function theorem gives a
unique solution near `k_s = 0` whose `k_s`-coefficient is `2i`, **with all hard dependence cancelling** (R17)--(R18).
Independently, the Ward interpretation of the same equation is `⟨k_h|Q_0^† J^-_0|k_h⟩ = 2iJ sin k_h = 2i v_h` (R14),
with descendant reduction (R15); dividing a hard external-pole reduction by the energy shift `v_h k_s` cancels the hard
velocity and leaves `2`.  The exact mismatch between the charge-created state and the on-shell scattering state is the
single ordered-branch factor `(1−S_{12})|P_{12}⟩` (R8), and **ML2 makes the expansion (R6)/(24) unconditional**.

**Bethe's role: strictly verification.**  (R17)--(R18) match O7/O8 term by term; two checkers enforce them numerically.

**SCOPE — read before quoting.**  The shard derives the **exact two-body soft expansion of the physical scattering
multiplier**, with its remainder bounds, and the derivation of the coefficient `2` from the local current/contact
structure of M1.  It is **not** by itself a process-independent, symmetry-derived soft theorem: that additionally needs
ML3, repaired ML4 (§2.5), and membership in `𝒮_W` (D24(d)), outside which universality is
FALSE.  `soft-current-recon.md` ⟨1⟩6 boxes the corresponding conditional statement — `M_2 = 𝖲(k_s)M_1 + R_{S2}` with
`𝖲(k_s) = 2ik_s` and `‖R_{S2}(k_s,·)‖_{L²(I)} ≤ C_I|k_s|²‖M_1‖_{L²(I)}`, hence `o(|k_s|)` in hard-wave-packet norm — as
**SKETCH**, conditional on wave operators (ML1) and the amputation convention.  The
exact S2-2body row is PROVED; this broader factorisation is not.  *Shards:* `soft-current-recon.md` ⟨1⟩1--⟨1⟩5 (derivation) + `oracle-bethe.md`
⟨1⟩3 (verification) + `ml2-completeness.md` (completeness).  *Checkers:* `soft_current_recon_check.py` (max form-factor
residual `1.56·10^{-14}`, quadratic-phase fit error `2.17·10^{-10}`), `oracle_bethe_check.py`,
`ml2_completeness_check.py`, and the numerics-side fm-displacement-scan (`numerics/docs/fm-twomagnon-notes.md`: the
leading D8 coefficient `2` reproduced to `0.2%`).

### 2.4 S-general (`n`-leg lattice soft theorem) — **CONJECTURE**

Let `|Φ⟩` be an `n`-particle excitation-ansatz scattering state whose legs carry asymptotic data `{q_i, v_i}` (charge
relative to their vacuum, group velocity) — for kink legs additionally the vacuum pair `(α,β)` of A2(e) and the
collective-coordinate data of D16 — and adjoin an `(n+1)`-th Goldstone leg of momentum `k_s`.  Then, in the wave-packet
norm of D3(a), as `k_s → 0`,

  `M_{n+1}(k_s; p_1…p_n) = 𝖲(k_s; {q_i,v_i}) · M_n(p_1…p_n) + R_{S2}(k_s)`,

with `𝖲` defined in D25 and conjectured **universal** — a function of the legs' asymptotic data alone, independent of the microscopic tensors `B_i` —
obeying the Adler zero `𝖲 → 0` as `k_s → 0` with leading term linear in `k_s`, and `R_{S2} = o(𝖲)` in that norm. At `n =
1` in M1, `𝖲(k_s) = 2ik_s` by §2.3.

**The universality class is part of the conjecture.**  Universality over *unrestricted* local sources is **REFUTED**:
`ml5-universality.md` ⟨1⟩4 exhibits a four-site local `D` such that `O_η = S^-_0 + ηD` leaves `M_1` untouched while
shifting the linear soft coefficient by `2iη(1−e^{-3ih})` (D24(e); checked, `ml4_check.py`).  What is frozen is therefore:
**`𝖲` is conjectured universal on the Ward-covariant, no-contact class `𝒮_W` of D24(d)**.  Repaired ML5-A requires both
`M_2^O(0)=0` and `𝔠_h(O)=0`, with D24(c)'s second-derivative norm control.  The counterexample is a
*stated feature* of the conjecture: it is what makes the reduced-channel and
no-contact conditions 4--5 of `𝒮_W` necessary rather than cosmetic.

**Status CONJECTURE.**  Corner A does not supply this edge (§6.1).  Its **exact** outstanding obligations are the six
missing lemmas of `soft-current-recon.md` ⟨1⟩7, as adjudicated at the freeze below.  Nothing may be asserted about
S-general that is not derivable from what those rows say is PROVED.

| id | obligation | difficulty | status |
|---|---|---|---|
| **ML1** | Two-magnon wave operators and channel norm: construct the infinite-chain one- and two-magnon scattering spaces and prove existence and isometry of the incoming/outgoing maps on packets supported away from equal velocities and the endpoints.  *Plan:* fiber by total momentum; each relative-coordinate fiber is a half-line Jacobi operator with one boundary defect; explicit spectral measure or Cook estimates; isolate the single bound eigenvalue. | MEDIUM | **CONJECTURE** |
| **ML2** | Complete charge-created resolution: the family used in (R6) contains every regular scattering root, the two-string, and all `SU(2)` descendants, with no missing exceptional finite-ring vector. | MEDIUM | **PROVED** (`ml2-completeness.md`; verdict `ml2-r2.md`) |
| **ML3** | Packet-smeared infinite-volume regularity, including the `k=Θ(1/N)` regime exposed by r1; exclude a physical `1/k_s` pole. | MEDIUM--HIGH | **CONJECTURE** |
| **ML4** | Fixed-volume formulas are an off-shell analytic interpolation only; an on-shell packet-smeared infinite-volume one-hard estimate and the two-hard/three-body statement remain future work. | HIGH | **SKETCH** |
| **ML5** | Unrestricted universality is refuted.  Repaired conditional ML5-A/B require zero intercept, zero first jet, explicit norm control, and an exhaustive LSZ decomposition; microscopic membership is future work. | HIGH | **REFUTED** |
| **ML6** | Control finite/infinite, packet-width, soft, bound, and off-shell limit orders. | MEDIUM | **CONJECTURE** |

### 2.5 ML4 and ML5-B repairs

**Lemma ML4-A — PROVED per corpus-r2 adjudication.**  Let `U : ℋ → 𝒦` be an isometry, `P = UU^†`, `Γ : (−ε,ε) →
B(ℋ,𝒦)` with `Γ(0) = U` and `sup‖∂_kΓ(k)‖ ≤ C_Γ`, `R = (1−P)J`, and `b ∈ C¹` with `b(0)=0`, `|b(k)| ≤ C_b|k|`. Then
`‖b(k)Γ(k)^†R‖ ≤ C_bC_Γ‖J‖\,k²`, and `O(ε²)` in the rescaled soft-packet norm. **The Ward identity is *not* what kills the
orthogonal `O(k)` term** — it computes `P J`.  What kills it is the pair *(energy-shell channel matching `Γ(0)=U`) + (`C¹`
on-shell trace regularity)*; the sign `sgn(v_h−v_s)` merely labels which continuous wave is called outgoing and supplies
no zero.

**Exact Ward projection in every finite sector — PROVED per corpus-r2
adjudication.**  On `ℋ_{n,N}`, `D_{n,N}^†J^-_0 = 2J^z_0 + J^-_0S^+`; on
`ker S^+` (`n < N/2`), `D_{n,N}^†D_{n,N} = (N−2n)𝟙` and `P_{n,N}J^-_0 = \frac{2}{N−2n}Q_0J^z_0`.  For one hard magnon
this gives `P_{1,N}J^-_0|h⟩_N = \frac{2iv(h)}{N−2}Q_0|h⟩_N` — equation (R15), upgraded from one momentum vector to the
whole hard packet space.  The complementary vector remains nonzero, which is precisely why ML4-A is needed.

**ML4 for one hard magnon — HOLD at SKETCH.**  At each fixed `N`, formulas
(15)--(17) give only an **off-shell analytic interpolation**:
`|𝒜_{⊥,N}(k;f,g)|≤C'_{I,N}k²‖f‖_{I,N}‖g‖_{I,N}`.  A periodic ring has no
nonzero on-shell sequence `k→0` at fixed `N`, so the formal iterated limit is
not a physical on-shell ring statement.  The old `N`-uniform constant is REFUTED:
for `h=2π/5`, `k=2π/N`, the normalized amplitude divided by `k²` grows as
`√N`.  `ml4_check.py` now includes named probe ML4-Q1 and a failing
`--red-uniform` mutation.  A genuinely packet-smeared infinite-volume bound
is future work bd `tns-7ut`; the two-hard/three-magnon channel remains future
work bd `tns-axg`.

**ML5-A and ML5-B — PROVED conditional implications per corpus-r2.**  ML5-B
explicitly assumes the exhaustive `L²(I)` LSZ decomposition into descendant,
orthogonal-current, and direct-contact terms, plus the other four D24(d)
conditions.  Repaired ML5-A requires `M_2^O(0)=0` and `𝔠_h(O)=0`, with
`K_O=(1/2)sup‖∂_k²M_2^O‖` controlling the remainder; a relative bound also
requires `K_O≤C_I‖M_1^O‖`.  `V_int` (D24(e)) is the red guard against the old
first-jet-only criterion.  Microscopic membership remains future work.

---

## §3. Corner B — the memory package

Shards `memory-quantization.md` and `corner-b-draft.md` (the latter reconciled against the claims DAG at freeze);
definitions D13--D18; checkers `mquant_check.py`, `crosscheck_corner_b_tk.py`; numerics
`numerics/results/memory-scan-1.json`, `numerics/docs/kink-sector-notes.md`.

### 3.1 M-flux (the flux / DC identity) — **PROVED**

*Assume (H4) with `G ⊇ U(1)` generated by `S^z`, and `W = [a,b]` finite.*  `𝔛_W ∈ 𝔄_loc` (D13(a)) and, by the exact
continuity equation D10(b),

  `d/dt ϱ_t(𝔛_W) = (1/2s)[ ϱ_t(j_{a−1|a}) − ϱ_t(j_{b|b+1}) ]`,
  `δx = (1/2s)∫_{t_i}^{t_f} dt [ ϱ_t(j_{a−1|a}) − ϱ_t(j_{b|b+1}) ] = (1/2s)[ ȷ̃_{a−1|a}(0) − ȷ̃_{b|b+1}(0) ]`.

The mathematical identity is exactly the DC component of the **physical
boundary current**.  G0(d) does not make that current a divergence of the
virtual bond potential `𝒥_b`; the former virtual/bond-data reading is
deleted.  D13(b) is the Fourier dress.  Promoted per `corpus-r2.md`
adjudication. *Guard:* numerics prediction **P6** — must hold to `10^{-6}` for *any*
`W` and *any* times; a failure is a bug, not physics.

### 3.2 M-quant (conditional memory bookkeeping) — **PROVED conditional on D18**

*Concrete scope:* D16's spin-`1/2` easy-axis XXZ model, a selected D18
scattering vector in `𝒦^{(1)}_{↑↓}` (D17), and the D13(a) core-to-edge padding
`d_W`.  For every `λ̃∈(λ_E,1)` the tail error is
`C_{λ̃}λ̃^{d_W}`.

**Conditional implication, promoted per corpus-r2.**  `δx = −(1/s)·⟨N_T⟩`, with `s=1/2` and
`⟨N_T⟩=∫(dk/2π)|φ(k)|²T(k)` (D14). Per
channel: a single magnon moves the wall by **exactly** `−1/s` sites if it transmits and by **exactly** `0` if it reflects;
for a superposed event
`Var(ΔX)=s^{-2}⟨N_T⟩(1−⟨N_T⟩)`.  This is not `Var(𝔛_W)` without a sharp
initial wall and two-time protocol.

The algebraic statement is
`2s·δx+(q_out−q_in)=0`, under D18's explicitly stated vacuum jump, channel
charges, and local decay.  It is independent of scattering phase once those
channels exist.  This is not a higher-spin channel theorem and not the general
MPS memory theorem; the latter is tracked by bd `tns-zw2`.

**Projected spectral scope.**  Mq-AD3 is PROVED conditional on Mq-E per
`corpus-r2.md`: the Kato--Rosenblum/Feshbach argument is sound
for the displayed Fano operator, but identifying the incoming `≤3`-wall
component with that operator is now explicit hypothesis Mq-E.  The repository
has one `N=14` enumeration, not an all-volume proof.  Thus projected H-AD is
conditional on Mq-E; full-chain D18 additionally requires control of
`P_3H(1-P_3)≠0` (bd `tns-d51`).

*Checker scope:* `mquant_check.py` tests M-flux and an empirical spin-`1/2`
scan only.  It does not construct wave operators, prove Mq-E, exclude
singular-continuous spectrum, or test `spec(ΔX)`.

### 3.3 Fano `t(k)` — **PROVED conditional on Mq-E for the displayed graph**

Under Mq-E the kink+magnon component reduces to a uniform tight-binding chain with a single **side-coupled
level** (the pure kink) attached at a junction — a Fano problem.  Eliminating the side level gives the junction potential
`U(k) = J²/(4ω(k))` and

  `t(k) = [1 + iJ²/(4 ω(k) v(k))]^{-1}`,  `T(k) = [1 + (J²/(4ω(k)v(k)))²]^{-1}`,
  `δ_t(k) = −arctan( J²/(4 ω(k) v(k)) )`.

Leakage into `≥5`-wall configurations is **measured**: `P(≥5) ≈ 8·10^{-3} / 3·10^{-2} / 1·10^{-1}` at `Δ = 8/4/2`, i.e.
`O(Δ^{-2})`.  It affects `T(k)`; it does **not** affect §3.1 or §3.2, which are conservation laws.  *Independent
verification:* `crosscheck_corner_b_tk.py` compares `R(k;Δ) = x/(1+x)`, `x = J⁴/(16ω²v²)`, against the independent
sparse-sector scan `numerics/results/memory-scan-1.json` on all `main-*`/`Dscan-*` runs, pass criterion fixed in advance
at 8%.  **Measured agreement 0.9%--5.8% (ratios 1.009--1.058) across `Δ ∈ {1.5,2,3,6,12}`, `k_0 ∈ [0.4,1.8]` — all pass.**

### 3.4 The soft memory zero — **PROVED conditional on Mq-E for the displayed graph; universality CONJECTURE**

On the Fano graph, as `k → 0` at fixed `Δ > 1`: `v → 0`, `ω → J(Δ−1)`, hence `T(k) = 16(Δ−1)²k² + O(k⁴)`, `R(k) = 1 − 16(Δ−1)²k² + O(k⁴)` — **total
reflection of a soft magnon, with a quadratic zero** — and by §3.2, `δx(k) = −(1/s)T(k)`.  In the frequency variable
`T ≈ 32(Δ−1)²(ω−ω_gap)/J`, *linear in the excess energy above the gap*; crossover momentum `k_* = 1/(4(Δ−1))`.  **Not
established:** that the quadratic zero and its coefficient `16(Δ−1)²` are **universal**, i.e. functions of the kink's
asymptotic data (vacuum pair, `U(1)` charge, gap) and not of the microscopic `B`-tensor — the actual `C ⇒ B` obligation
(§6.2).  *Guard:* numerics P2 — slope `2.00 ± 0.05`, prefactor `32(Δ−1)²` to `±15%` over `k_0 ∈ [0.03,0.2]`, `Δ = 2,4`.

### 3.5 Conjecture M of the brief — **REFUTED as literally stated**

"`δx` equals the zero-frequency limit of the soft factor summed over the event" is **false in the easy-axis XXZ chain**.
Two independent reasons: (a) conditional charge bookkeeping fixes the same coefficient once D18's channels exist, whereas any
soft-factor expression varies with them; (b) `δx` is insensitive to `δ_t(k)` entirely — a purely transmitting wall with
`δ_t ≡ 0` still displaces by exactly `−1/s`.  **The soft factor is a phase; the memory quantum is a charge.**  The
surviving candidate is §3.1 + §3.2: *memory is the DC weight of the boundary current, and the
soft data enter only through `T(k)`.*

---

## §4. Conjecture Bc — "the two `2`s" — **CONJECTURE**

Two independent `2`s appear.  (i) In M1, the soft Wigner phase-slope coefficient of S2-2body: on D8,
`dδ_phys/dk_s|_0 = 2 sgn(v_h−v_s) = 2`, a two-site spatial shift of the soft packet off a hard magnon.  (O9 is emphatic
that this is a **phase slope, not a scattering length**: the FM's relative-momentum scattering length is zero, since
`δ_{12}/ε → 2xy/(y−x)` in the joint soft limit.)  (ii) In M2, the conditional memory channel quantum: `1/s = 2` sites.

**Conjecture Bc.**  Both equal `|q_hard|/s`, with `q_hard` the hard leg's `U(1)` charge relative to its vacuum — i.e.
*the soft phase coefficient and the memory quantum are the same asymptotic-charge datum*.  **Falsifier, cheapest
first:** the spin-1 ferromagnet two-magnon Bethe phase should give `dδ/dk_s = 1`, not `2`; independently the spin-1
easy-axis chain should give `δx/N_T = −1/s = −1` (numerics P8).  **If the spin-1 phase slope is not `1`, the coincidence
is numerology and must be dropped from the paper.**  *Shard:* `corner-b-draft.md` §10; bd issue filed at freeze.

---

## §5. SPT soft rigidity — bulk deformability versus endpoint quantisation

Rebuilt shard: `theory/spt-rebuild.md`; definitions D19--D23.  After the r2
repairs, the parent SPT rows remain SKETCH awaiting focused critic r3.  The
narrow closed-multiplier cancellation and exact AKLT-family contraction are
PROVED per `corpus-r2.md`.  The old pointwise bulk-blindness theorem and the
all-orders edge no-go are REFUTED.

**Dichotomy.**  A closed on-site bulk string has two virtual endpoints.  Their
projective multipliers cancel, so no projective multiplication anomaly can be
extracted from a closed bulk soft insertion.  This does not erase the honest
adjoint representation: Pauli-projective conjugation and scalar-trivial
conjugation are distinguishable (`Tr Ad(R_x)=0` versus `4`).  Normalized bulk
coefficients are continuous transfer data under a common-gap symmetric MPS
path and become topological only after a separate local-constancy proof.

An unpaired half-chain endpoint instead carries the fixed Schmidt/edge register
`E_C=ℂ^χ`, distinct from the padded-window module
`𝓜_χ(C)≅E_C⊗E_C^*` (exactly `χ` copies under left multiplication).  The
Hermitian partial-charge compression `-iQ` equals the centered,
phase-gauge-invariant endpoint charge `Q_edge=-iX_C^∘`, whose spectrum lies in
`q_{ω,C}^∘+ℤ`.  On the
anisotropic AKLT path,
`C_bulk(b)=b²/[4(1-b²)]` changes from `1/8` to `0.240196...`, while
`ℜ_L(S^z)=-½[1-(2b²-1)^L]Z→-Z/2` is unchanged.  This is the rigid topological
content.  A physical edge-Hilbert interpretation carries hypothesis H-split.

| id | rebuilt statement | honest status |
|---|---|---|
| SPT-B-mult | Closed-bulk endpoint multipliers cancel exactly under ordered multiplication and lift rephasing | PROVED per corpus-r2 adjudication |
| SPT-B' | With external tensors, embeddings, gauge fixes, Gram normalizations, and differentiated profiles continuous/`C^p`, coefficients are continuous/deformable and may retain class-correlated `Ad(V)` data | SKETCH; N2 repaired, awaiting critic r3 |
| SPT-E-AKLT | Hermitian AKLT-family residue is exactly `-½[1-(2b²-1)^L]Z→-Z/2`; trivial `O(2)` product residue is `0` | PROVED per corpus-r2 adjudication |
| SPT-E' | Centered registered charge in the `ω`-projective Schmidt/edge register, `dim≥d_ω`, `spec Q_edge⊂q_{ω,C}^∘+ℤ`; padded module has `χ` copies | SKETCH; N1/N4 repaired, physical statement conditional on H-split, awaiting r3 |
| SPT-T' | For commuting `g,h`, one twist endpoint carries the slant/commutator phase and the other compensates | SKETCH; physical statement conditional on H-split/H-dress; endpoint-convention repair awaits r3 |
| SPT-D' | Ordered endpoint-soft products realise the cocycle globally; the infinitesimal central cocycle is cohomologically trivial and gauged away in the stated phase convention | SKETCH; physical statement conditional on H-split/H-dress; N5/N6 repair awaits r3 |
| SPT-M' | Conditional channel bookkeeping quantises edge-charge changes and the projective module protects memory capacity; topology does not force a nonzero amplitude | SKETCH given H-split/H-AD-edge; centered-charge input awaits r3 |
| SPT-M'-dyn | Nonzero edge-changing reflection for D23's exact open AKLT parent `H_{A,+}^{dyn}` with boundary coupling `P^{(S=2)}_{0,1}` | CONJECTURE; half-chain wave operators, H-AD-edge, on-shell matrix, and nonvanishing missing |

**Exact deciding computation.** `spt_rebuild_check.py` fixes all tensors and
tolerances.  It verifies the explicit injective `χ=2` TRIV tensor, the critic's
`D₂` adjoint decomposition, the varying bulk coefficient, and the rigid AKLT
edge residue; its sign and uncentered U(1) phase-gauge red mutants fail.  The remaining `tns-cpq` work is the
half-chain scattering calculation.  A zero AKLT edge-changing amplitude would
refute only SPT-M'-dyn, not the registered endpoint theorem.

**Closed route.**  The commuting/order-two truncated-symmetry commutator used
to diagnose the MPU anomaly is the identity for an on-site symmetry (a
noncommuting group can retain only its ordinary group commutator).  SPT
information here is therefore a projective endpoint module, a relative dressed
two-endpoint response, or a quantised edge residue—not an anomalous closed-bulk
commutator phase.

## §6. The three edges

### 6.1 A ⇒ C (asymptotic symmetry ⇒ soft theorem) — **CONJECTURE**

**Not supplied by Corner A.**  This is the campaign's core proof obligation and it is not discharged. Corner A supplies
G0(e) — an exact operator continuity equation in `𝔄_loc`, true of the *true* model whatever its ground state, needing no
MPS at all — and, in M1 only, the Ward residue (R14)/(R15).  It supplies **no** Adler zero, **no** universality and **no**
rederivation of O7/O9 (the REFUTED row, §1.5).  Abstract ML4-A's decisive
mechanism is matching plus `C¹` regularity; the fixed-volume FM formulas are
only an off-shell interpolation, and r1 refutes their former volume-uniform
application.  **Settled negatively:** process independence over unrestricted local sources is **REFUTED** by the four-site source `O_η`
of D24(e), which leaves `M_1` fixed and shifts the linear soft coefficient — so any A ⇒ C statement must carry a
source-class hypothesis. **Live obligations:** ML1; ML3 including a
packet-smeared infinite-volume estimate that controls `k=Θ(1/N)`; ML4 for two
hard magnons into a three-magnon channel; repaired ML5-B's exhaustive LSZ
decomposition; microscopic `𝒮_W` membership; and ML6 remainder/limit control.
No `n=1` process-independent edge is currently closed.  Only G0(e)'s oracle
O1 consequence is PROVED along this edge.

### 6.2 C ⇒ B (soft theorem ⇒ memory) — **SKETCH**

Not the shape the brief conjectured (§3.5).  Its true shape is: Corner C (soft behaviour of `t(k)`) ⟶ `T(k) → 0` as `k→0`
(memory Adler zero) ⟶ `δx(k) = −T(k)/s` (conditional M-quant).  The physical
flux identity is PROVED and the D18 charge bookkeeping is PROVED conditional
on D18.  The Fano
middle step is conditional on Mq-E, and the full chain on D18 (bd `tns-d51`).
For the displayed graph the zero and coefficient are exact conditional on
Mq-E; **whether the zero and coefficient are universal remains CONJECTURE**.
C ⇒ B therefore stays at conditional bookkeeping scope.  The ML5
counterexample (D24(e)) is a warning here too: any universality statement is
relative to a named source class.

### 6.3 B ⇒ A (memory ⇒ asymptotic symmetry) — **SKETCH edge; B3 PROVED**

**(i) Finite-time label rigidity — PROVED.**  Under stationary
vacua, translation covariance, and finite-range Lieb--Robinson dynamics, the
factorised D9(a) boundary conditions remain `ω_α,ω_β`.  The proof uses
norm-local approximants for both `α_t(D)` and `α_t(τ_n(O))` before the D9(a)
limit.  This fixes the labels; mere preservation of disjointness was
insufficient.

**(ii) Charge bookkeeping — PROVED for a D18-separated event.**  Fix `c∈W`, take D18's
separated in/out limits, and subtract the kink charge from each asymptotic
leg.  Conservation gives exactly

`2s·δx+(q_out−q_in)=0`.

The old half-line formula is REFUTED by sign and factor two.  Reflection gives
`δx=0`; transmission gives `δx=-1/s`.

**Residue/HOLD reason for the edge.**  The thermodynamic
`ℤ`-torsor/unique-flat-kink statement remains
a CONJECTURE (K4/R5).  The D9(d) vacuum-pair label is read off and not shifted;
`δx` records leg-charge transport inside it.  Neither virtual bond data nor
the refuted `A2-orbit-r1` object is used.  What remains missing for B ⇒ A is a
proof that measured memory reconstructs an asymptotic-symmetry action or
classifying datum.  *Shard:* `corner-b-draft.md` §7.

---

## §7. Status index

| item | status | shard | checker |
|---|---|---|---|
| Lemma IT, WI | PROVED | corner-a.md ⟨1⟩2--⟨1⟩3 | corner_a_check.py C0--C2b |
| A1 (a)--(g), padded windows for (d1) | PROVED | corner-a.md ⟨1⟩4 | C6, C8, C8b |
| S-A1 (GNS/edge realisation; load-bearing) | SKETCH | corner-a.md ⟨1⟩4.⟨2⟩9 | — |
| A2 (a)--(f); (e) under (T) | PROVED | corner-a-kinks.md ⟨1⟩8--⟨1⟩9 | C7, C11 |
| S-A2 (continuum-`Ω_vac` uniformity; load-bearing) | SKETCH | corner-a-kinks.md ⟨1⟩10.⟨2⟩3 | — |
| G0 (a)--(e); Lemma SBP; Prop FM | PROVED | corner-a-goldstone.md ⟨1⟩5--⟨1⟩7 | C3--C5, C9, C10 |
| A2-orbit-r1 / G0-soft-r1 (second withdrawn) | REFUTED | §1.4, §1.5 | C7 / — |
| O1--O10 | PROVED | oracle-bethe.md | oracle_bethe_check.py |
| ML2 | PROVED | ml2-completeness.md | ml2_completeness_check.py |
| S2-2body | PROVED | soft-current-recon.md + oracle-bethe.md; corpus-r2 adjudication | soft_current_recon_check.py + oracle + ML2 checks |
| S-general (repaired D24 class; live obligations in §2.4) | CONJECTURE | §2.4 | — |
| ML4-A + exact Ward projection | PROVED | ml4-ward-reduction.md ⟨1⟩2--⟨1⟩3; corpus-r2 adjudication | ml4_check.py |
| ML4 fixed-volume off-shell interpolation; on-shell infinite-volume result open | SKETCH | ml4-ward-reduction.md ⟨1⟩4--⟨1⟩5; HOLD N3 | ml4_check.py incl. ML4-Q1 |
| ML5 unrestricted universality | REFUTED | ml5-universality.md | ml4_check.py O_eta |
| ML5-A/B repaired conditional implications | PROVED | ml5-universality.md; corpus-r2 adjudication | ml4_check.py ML5-I1 |
| M-flux physical-current identity | PROVED | memory-quantization.md §1; corpus-r2 adjudication | mquant_check.py flux only |
| K1 / K2 / K3 | PROVED | corner-b-draft.md §1.2; corpus-r2 adjudication | finite-matrix, local residual, and telescoping checks |
| B3 finite-time label rigidity + leg-charge bookkeeping | PROVED | corner-b-draft.md §7; corpus-r2 adjudication with N9 sweep | — |
| Mq-AD3 conditional on Mq-E | PROVED | memory-quantization.md §3; corpus-r2 adjudication | Mq-E itself untested |
| M-quant conditional on D18 | PROVED | memory-quantization.md; corpus-r2 adjudication | mquant_check.py is flux/empirical only |
| Fano `t,T,δ_t` and soft zero, conditional on Mq-E for displayed graph | PROVED | corner-b-draft.md §5; corpus-r2 adjudication | crosscheck is empirical full-chain evidence only |
| Conjecture M (brief's literal form) | REFUTED | corner-b-draft.md §10 | — |
| Bc ("the two 2s"; spin-1 falsifier) | CONJECTURE | §4 | not yet computed |
| SPT-B-mult closed multiplier cancellation | PROVED | spt-rebuild.md ⟨1⟩3.⟨2⟩1; corpus-r2 adjudication | spt_rebuild_check.py S-C2 |
| SPT-B' coefficient continuity/deformability with continuous/`C^p` external data | SKETCH | spt-rebuild.md ⟨1⟩3; HOLD awaiting r3 | spt_rebuild_check.py S-C2, S-C3 |
| SPT-E-AKLT exact Hermitian centered contraction | PROVED | spt-rebuild.md ⟨1⟩4.⟨2⟩4; corpus-r2 adjudication | spt_rebuild_check.py S-C4 |
| SPT-E' centered endpoint residue and shifted charge lattice; physical edge statement conditional on H-split | SKETCH | spt-rebuild.md ⟨1⟩4; HOLD awaiting r3 | spt_rebuild_check.py S-C4, S-C5, phase-gauge red |
| SPT-T' registered twist endpoint/slant phase; physical observable conditional on H-split/H-dress | SKETCH | spt-rebuild.md ⟨1⟩5.⟨2⟩1; HOLD awaiting r3 | — |
| SPT-D' ordered endpoint-soft products; physical edge statement conditional on H-split/H-dress | SKETCH | spt-rebuild.md ⟨1⟩5.⟨2⟩2; HOLD awaiting r3 | spt_rebuild_check.py S-C5 |
| SPT-M' conditional channel bookkeeping given H-split/H-AD-edge | SKETCH | spt-rebuild.md ⟨1⟩6.⟨2⟩1; HOLD awaiting r3 | dynamical follow-on tns-cpq |
| SPT-M'-dyn nonzero reflection for D23's exact open AKLT parent | CONJECTURE | spt-rebuild.md ⟨1⟩6.⟨2⟩2; missing wave operators/on-shell matrix/nonvanishing | tns-cpq follow-on |
| SPT-B-r1 pointwise bulk `[ω]`-blindness | REFUTED | spt-rebuild.md ⟨1⟩3.⟨2⟩3 | spt_rebuild_check.py S-C2 |
| SPT-nogo all-orders/all-registers form | REFUTED | spt-rebuild.md ⟨1⟩4 | spt_rebuild_check.py S-C4 |
| A ⇒ C | CONJECTURE | §6.1 | fixed-volume/negative probes only |
| C ⇒ B | SKETCH | §6.2 | flux/empirical checks only |
| B ⇒ A (B3 proved; reconstruction step open) | SKETCH | §6.3; HOLD per corpus-r2 | — |

**Freeze rule.**  The corpus-r2 promotions are frozen exactly as recorded
above.  Parent SPT rows stay SKETCH until focused critic r3; no unlisted claim
is promoted.  SPT content lives only in `theory/spt-rebuild.md`, with
`definitions.md` D19--D23, `claims/CLAIMS.md`, and §5 in lockstep;
`theory/spt-scoping-draft.md` is superseded history.
