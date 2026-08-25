<!-- ROLE: D2 of HANDOFF_MPS_SOFT_THEOREM.md §4 — the campaign's framework document.
     FROZEN 2026-08-26, after the three foundation L6 loops converged (oracle-bethe-r2.md,
     corner-a-r3.md, ml2-r2.md — all PASS) and the ML4/ML5/M-quant summit landed.
     Every statement is copied from a converged artifact; nothing is invented here.
     Changing a frozen statement requires reopening the relevant L6 loop. -->

# TRIANGLE.md — the 1D lattice infrared triangle

**Freeze 2026-08-26.**  Definitions are `definitions.md` D1--D24 and are never restated here; symbols are `notation.md`.
Every item carries an L5 status, its shard, and the executable check that guards it.  **Status labels:** `PROVED` —
complete argument in a shard that passed its L6 loop; `SKETCH` — argument with a named gap; `CONJECTURE` — no argument;
`REFUTED`/`RETRACTED` — carried as negative results so they are not rediscovered.  A statement conditional on a named
hypothesis is `PROVED given H`, never `PROVED`.

**Two standing TJO directives.**  *Generality* (bd `tns-9tt`): Corner A and the memory law are stated in their general
`(G, injective MPS, finite-range H)` form; M1 (isotropic Heisenberg FM, D6) and M2 (easy-axis XXZ, D16) are
*instantiations and oracles*, not the register of the theorems.  Generality is withheld in one place only — universality
of the soft coefficient, which after the ML4/ML5 summit is frozen *relative to the source class* `𝒮_W` (D24(d), §2.4).
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
| **(H-AD)** | asymptotic decomposition of the kink+magnon state at `t_i,t_f` (asymptotic completeness of that sector).  Unproved; isolated | D18 |

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

**Central-extension caveat (a genuine disanalogy with the continuum).**  The Lie-algebra cocycle `c_α ∈ H²(𝔥_α,ℝ)` of
D4(d) is only the local infinitesimal image of `[ω_α]` and generally loses it: for `𝔥_α` compact semisimple `H²(𝔥_α,ℝ) =
0` (Whitehead), so `c_α ≡ 0` while `[ω_α]` may be a nontrivial torsion class (AKLT).  **The lattice SPT anomaly is a
group-cohomological multiplier, not a Lie-algebra central charge**, and this must be said wherever `docs/framing.md` §2 is
invoked. *Shard:* `corner-a.md` ⟨1⟩4.  *Checks:* C6, C8, C8b.

**SKETCH box S-A1 (load-bearing).**  Not proved: that `ω_α^{M@b}` is a *normal* state of `π_α(𝔄)''`, i.e. that `𝔞_α` acts
on the GNS Hilbert space rather than on finite-window spaces `𝒲_{Λ,b}`; the expected route is the split property.  **This
is exactly `docs/framing.md` §1--§2's demand that the charge algebra act on the physical state space, and that demand is
NOT met.**  Anything phrased as "the charge algebra acting on `H_A`" — D21(a)'s `H_edge` included — inherits this status.
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

**Negative row `G0-soft-r1` — RETRACTED.**  `(e^{ik}−1)` is a *kinematic* factor from the profile alone.  It is **not** a
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

### 2.3 THEOREM S2-2body (two-body soft theorem, M1) — **PROVED, FROZEN**

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

**SCOPE — read before quoting.**  What is proved is the **exact two-body soft expansion of the physical scattering
multiplier**, with its remainder bounds, and the derivation of the coefficient `2` from the local current/contact
structure of M1.  It is **not** by itself a process-independent, symmetry-derived soft theorem: that additionally needs
ML3 (still OPEN), ML4 (PROVED at one hard magnon, §2.5) and membership in `𝒮_W` (D24(d)), outside which universality is
FALSE.  `soft-current-recon.md` ⟨1⟩6 boxes the corresponding conditional statement — `M_2 = 𝖲(k_s)M_1 + R_{S2}` with
`𝖲(k_s) = 2ik_s` and `‖R_{S2}(k_s,·)‖_{L²(I)} ≤ C_I|k_s|²‖M_1‖_{L²(I)}`, hence `o(|k_s|)` in hard-wave-packet norm — as
**EXPLORATION**, conditional on wave operators (ML1) and the amputation convention.  **That box is not frozen; the
expansion above is.**  *Shards:* `soft-current-recon.md` ⟨1⟩1--⟨1⟩5 (derivation) + `oracle-bethe.md`
⟨1⟩3 (verification) + `ml2-completeness.md` (completeness).  *Checkers:* `soft_current_recon_check.py` (max form-factor
residual `1.56·10^{-14}`, quadratic-phase fit error `2.17·10^{-10}`), `oracle_bethe_check.py`,
`ml2_completeness_check.py`, and the numerics-side fm-displacement-scan (`numerics/docs/fm-twomagnon-notes.md`: the
leading D8 coefficient `2` reproduced to `0.2%`).

### 2.4 CONJECTURE S-general (`n`-leg lattice soft theorem) — **CONJECTURE, FROZEN**

Let `|Φ⟩` be an `n`-particle excitation-ansatz scattering state whose legs carry asymptotic data `{q_i, v_i}` (charge
relative to their vacuum, group velocity) — for kink legs additionally the vacuum pair `(α,β)` of A2(e) and the
collective-coordinate data of D16 — and adjoin an `(n+1)`-th Goldstone leg of momentum `k_s`.  Then, in the wave-packet
norm of D3(a), as `k_s → 0`,

  `M_{n+1}(k_s; p_1…p_n) = 𝖲(k_s; {q_i,v_i}) · M_n(p_1…p_n) + R_{S2}(k_s)`,

with `𝖲` **universal** — a function of the legs' asymptotic data alone, independent of the microscopic tensors `B_i` —
obeying the Adler zero `𝖲 → 0` as `k_s → 0` with leading term linear in `k_s`, and `R_{S2} = o(𝖲)` in that norm. At `n =
1` in M1, `𝖲(k_s) = 2ik_s` by §2.3.

**The universality class is part of the frozen statement.**  Universality over *unrestricted* local sources is **FALSE**:
`ml5-universality.md` ⟨1⟩4 exhibits a four-site local `D` such that `O_η = S^-_0 + ηD` leaves `M_1` untouched while
shifting the linear soft coefficient by `2iη(1−e^{-3ih})` (D24(e); checked, `ml4_check.py`).  What is frozen is therefore:
**`𝖲` is universal on the Ward-covariant, no-contact class `𝒮_W` of D24(d), and by ML5-A that class is sharp** —
universality holds **iff** the amputated contact term has zero first jet, `𝔠_h(O) = 0` (D24(c)).  The counterexample is a
*stated feature* of the conjecture: it is what makes hypothesis 4 of `𝒮_W` necessary rather than cosmetic.

**Status CONJECTURE.**  Corner A does not supply this edge (§6.1).  Its **exact** outstanding obligations are the six
missing lemmas of `soft-current-recon.md` ⟨1⟩7, as adjudicated at the freeze below.  Nothing may be asserted about
S-general that is not derivable from what those rows say is PROVED.

| id | obligation | difficulty | status |
|---|---|---|---|
| **ML1** | Two-magnon wave operators and channel norm: construct the infinite-chain one- and two-magnon scattering spaces and prove existence and isometry of the incoming/outgoing maps on packets supported away from equal velocities and the endpoints.  *Plan:* fiber by total momentum; each relative-coordinate fiber is a half-line Jacobi operator with one boundary defect; explicit spectral measure or Cook estimates; isolate the single bound eigenvalue. | MEDIUM | **OPEN** |
| **ML2** | Complete charge-created resolution: the family used in (R6) contains every regular scattering root, the two-string, and all `SU(2)` descendants, with no missing exceptional finite-ring vector. | MEDIUM | **PROVED** (`ml2-completeness.md`; verdict `ml2-r2.md`) |
| **ML3** | Uniform current-form-factor regularity: upgrade the finite-volume regularity after (R15) to a bound uniform in volume and in `k_s→0` after wave-packet smearing; show the delta/principal-value pieces in (R5) are distributional normalisation effects and that **no physical `1/k_s` current pole survives**. | MEDIUM--HIGH | **OPEN** |
| **ML4** | Ward/LSZ external-leg reduction: show that the descendant piece (R15), and **only** that piece, supplies the leading on-shell connected amplitude, while the orthogonal contact vector contributes `O(k_s²)`. | HIGH | **PROVED for one hard magnon** (`ml4-ward-reduction.md`; see §2.5).  **OPEN** for two hard magnons into a genuine three-magnon channel — `EXPLORATION ML4-3`, bd `tns-axg` |
| **ML5** | Process-independent factorization: specify the class of quasi-local hard sources for which `M_1` and `M_2` are related by the same external-leg factor, with no source-dependent contact term at order `k_s`. | HIGH | **REFUTED for unrestricted local sources** (counterexample D24(e)) **and PROVED conditionally** on `𝒮_W` (D24(d), Theorem ML5-B), with ML5-A giving the sharp iff.  **OPEN:** deriving `𝒮_W`-membership for a nontrivial microscopic source class — bd `tns-axg` |
| **ML6** | Finite/infinite and bound-channel remainder: control the order of `N→∞`, packet width `→0`, and `k_s→0`, and prove that the bound state and off-shell coefficients in (R5) do not contaminate the leading real scattering channel.  Non-uniformity as `k_h→0` is excluded exactly as in D8/O7. | MEDIUM | **OPEN** |

### 2.5 THEOREM ML4 (Ward/LSZ reduction) and THEOREM ML5-B (conditional universality)

**Lemma ML4-A — PROVED, and it is the decisive mechanism.**  Let `U : ℋ → 𝒦` be an isometry, `P = UU^†`, `Γ : (−ε,ε) →
B(ℋ,𝒦)` with `Γ(0) = U` and `sup‖∂_kΓ(k)‖ ≤ C_Γ`, `R = (1−P)J`, and `b ∈ C¹` with `b(0)=0`, `|b(k)| ≤ C_b|k|`. Then
`‖b(k)Γ(k)^†R‖ ≤ C_bC_Γ‖J‖\,k²`, and `O(ε²)` in the rescaled soft-packet norm. **The Ward identity is *not* what kills the
orthogonal `O(k)` term** — it computes `P J`.  What kills it is the pair *(energy-shell channel matching `Γ(0)=U`) + (`C¹`
on-shell trace regularity)*; the sign `sgn(v_h−v_s)` merely labels which continuous wave is called outgoing and supplies
no zero.

**Exact Ward projection in every finite sector — PROVED.**  On `ℋ_{n,N}`, `D_{n,N}^†J^-_0 = 2J^z_0 + J^-_0S^+`; on
`ker S^+` (`n < N/2`), `D_{n,N}^†D_{n,N} = (N−2n)𝟙` and `P_{n,N}J^-_0 = \frac{2}{N−2n}Q_0J^z_0`.  For one hard magnon
this gives `P_{1,N}J^-_0|h⟩_N = \frac{2iv(h)}{N−2}Q_0|h⟩_N` — equation (R15), upgraded from one momentum vector to the
whole hard packet space.  The complementary vector remains nonzero, which is precisely why ML4-A is needed.

**ML4 for one hard magnon — PROVED.**  For `h ∈ I ⋐ (0,π)` and arbitrary `f,g ∈ C_c^∞(I)`, ML2's complete two-body
resolution supplies both ML4-A hypotheses (`B_N(0,h) = Q_0|h⟩_N`; a unique `C¹` energy-shell branch by the
implicit-function theorem with `∂_qE = v(h)` bounded below; the bound band separated by `J sin²(a/2)`; the singular `K=π`
class excluded), whence `|𝒜_{⊥,N}(k;f,g)| ≤ C'_I k²‖f‖_{I,N}‖g‖_{I,N}` **uniformly in `N`**, surviving `N→∞`, with
`O(ε²)` soft remainder.  *Checker:* `ml4_check.py`, `N = 12…20`: fitted amplitude exponent `1.99700--1.99988`; the
built-in red mutation (omit the projection) returns `0.9999`; max Ward/projection residuals `8.9e-16`, `3.5e-15`.
**OPEN (bd `tns-axg`):** two hard magnons into a genuine three-magnon channel — ML2 is *input* completeness, not
three-body *channel* completeness, and a degenerate open channel could contribute at `O(k)`.

**Theorem ML5-B — PROVED conditionally.**  Every `O ∈ 𝒮_W` (D24(d)) obeys `M_2^O(k,h) = 2iχ k\,M_1^O(h) + O_{L²(I)}(k²)`,
with `χ = sgn(v_h−v_s)`: the descendant external leg contributes `(e^{ik}−1)L(k,h)[2iv_hM_1^O(h)] = 2iχ k M_1^O + O(k²)`,
ML4-A removes the orthogonal current, and hypothesis 4 removes the only remaining process-dependent first jet.  The
coefficient is the **signed two-site Wigner displacement**.  Charge algebra plus kinematics fixes the descendant term but
does **not** prove hypothesis 4 — that is the open half (`EXPLORATION ML5-W`).

---

## §3. Corner B — the memory package

Shards `memory-quantization.md` and `corner-b-draft.md` (the latter reconciled against the claims DAG at freeze);
definitions D13--D18; checkers `mquant_check.py`, `crosscheck_corner_b_tk.py`; numerics
`numerics/results/memory-scan-1.json`, `numerics/docs/kink-sector-notes.md`.

### 3.1 Proposition M-flux (the flux / DC identity) — **PROVED, unconditional**

*Assume (H4) with `G ⊇ U(1)` generated by `S^z`, and `W = [a,b]` finite.*  `𝔛_W ∈ 𝔄_loc` (D13(a)) and, by the exact
continuity equation D10(b),

  `d/dt ϱ_t(𝔛_W) = (1/2s)[ ϱ_t(j_{a−1|a}) − ϱ_t(j_{b|b+1}) ]`,
  `δx = (1/2s)∫_{t_i}^{t_f} dt [ ϱ_t(j_{a−1|a}) − ϱ_t(j_{b|b+1}) ] = (1/2s)[ ȷ̃_{a−1|a}(0) − ȷ̃_{b|b+1}(0) ]`.

**The memory is the DC component of the boundary current**; by G0(d) that current is a lattice divergence of the bond
potential `𝒥_b`, so memory is a difference of virtual/bond data at the two ends of the window — `docs/framing.md` §4's
"memory lives in the bond data" as a theorem rather than an analogy.  No hypothesis beyond `𝔛_W ∈ 𝔄_loc`.  `Bd2 ≡ Bd3`
(D13(b)) is the same statement in a Fourier dress. *Guard:* numerics prediction **P6** — must hold to `10^{-6}` for *any*
`W` and *any* times; a failure is a bug, not physics.

### 3.2 Theorem M-quant (memory quantisation) — **THEOREM for the projected dynamics; PROVED given (H-AD) for the full chain**

*Assume:* (A1) D1, D2 with `G ⊇ U(1)` generated by `S^z_x`, `[H,S^z_reg] = 0`, `Ω_vac = {α,β}` with densities `s_α = +s`,
`s_β = −s`; (A2) `ϱ_t` a one-parameter family in `𝒦^{(1)}_{αβ}` (D17) solving the Heisenberg equations of `H_XXZ` (D16);
(A3) **(H-AD)** with data `(t_i,t_f,W,ε)` (D18); (A4) `b − a ≫ ξ_c`.

**PROVE.**  `δx = −(1/s)·⟨N_T⟩` up to `O(ε)` and `O(e^{-(b−a)/ξ_c})`, with `⟨N_T⟩ = ∫ (dk/2π) |φ(k)|² T(k)` (D14). Per
channel: a single magnon moves the wall by **exactly** `−1/s` sites if it transmits and by **exactly** `0` if it reflects;
for a superposed event `Var(𝔛_W) = s^{-2}⟨N_T⟩(1−⟨N_T⟩)` (`= 4T(1−T)` at `s = 1/2`).

**The coefficient is fixed by `U(1)` charge conservation alone**: it does not depend on `k`, on `Δ`, on the packet shape,
or on any scattering phase.  The structural reason: on the lattice translation is *not* a symmetry within a magnetisation
sector — translating a kink changes `S^z_reg` — so momentum conservation for the wall is traded for charge conservation.
The kink band is exactly flat (frustration-freeness plus the exact product family of D16), so the wall has no effective
mass, no dispersion, and **no recoil**.

**(H-AD) is PROVED for the projected dynamics.**  `memory-quantization.md` §3 proves H-AD *unconditionally* for `H_3 =
P_3HP_3`, the `≤3`-domain-wall projection: by the domain-wall enumeration S1 that Hamiltonian is `H_0 = [E_c −
(J/2)(T+T^*)] ⊕ E_d` plus a **rank-≤2, trace-class** junction coupling `−(J/2)(|0⟩⟨d| + |d⟩⟨0|)`, so **Kato--Rosenblum**
gives wave operators `W_±` with `Ran W_± = ℋ_ac(H_3)`; a Feshbach/Weyl-function computation with `m_0(z) = [(z−E_c)² −
J²]^{-1/2}` shows the denominator `z − E_d − (J²/4)m_0(z)` has no real zero inside the band and finitely many isolated
zeros outside, so there is **no singular-continuous spectrum** and `ℋ = ℋ_b ⊕ Ran W_±` with `dim ℋ_b < ∞`; stationary
phase gives AD3's local decay.  `N_T` is thereby an honest *operator* `W_+P_TW_+^*`, so `ΔX = −(1/s)N_T` with `spec(ΔX) ⊆
{−1/s, 0}` — **the channel outcomes, not every expectation value, are quantised.**

**What is still a hypothesis.**  `P_3H(1−P_3) ≠ 0`: five-wall and higher configurations are real.  Lifting H-AD to the
full chain needs a uniform-in-time scattering estimate (Feshbach/Mourre over all open channels); the measured `O(Δ^{-2})`
leakage (`≈ 0.10, 0.03, 0.008` at `Δ = 2,4,8`) is evidence, **not** that estimate — bd `tns-d51`.  §3.1 and the charge
arithmetic use no hypothesis at all.  *Shards:* `memory-quantization.md`; `corner-b-draft.md` §6 (Theorem M′).
*Checker:* `mquant_check.py` — independent frozen-boundary construction, operator residue `0`, finite-time residue
`3.37·10^{-16}`; on the nine clean scan rows `max|δx_1+2T| = 0.004330`, `max|δx_2+2T| = 0.001233`, inside the scan's own
budget `0.005563`.  *Guards:* numerics P1, P4, P5, P8; exact-projection runs give `δx/(−2N_T) = 1.0000000`, `Δ = 8,4,2`.

### 3.3 Proposition t(k) — **COMPUTED, exact in the ≤3-wall projection**

In that projection the kink+magnon sector reduces exactly to a uniform tight-binding chain with a single **side-coupled
level** (the pure kink) attached at a junction — a Fano problem.  Eliminating the side level gives the junction potential
`U(k) = J²/(4ω(k))` and

  `t(k) = [1 + iJ²/(4 ω(k) v(k))]^{-1}`,  `T(k) = [1 + (J²/(4ω(k)v(k)))²]^{-1}`,
  `δ_t(k) = −arctan( J²/(4 ω(k) v(k)) )`.

Leakage into `≥5`-wall configurations is **measured**: `P(≥5) ≈ 8·10^{-3} / 3·10^{-2} / 1·10^{-1}` at `Δ = 8/4/2`, i.e.
`O(Δ^{-2})`.  It affects `T(k)`; it does **not** affect §3.1 or §3.2, which are conservation laws.  *Independent
verification:* `crosscheck_corner_b_tk.py` compares `R(k;Δ) = x/(1+x)`, `x = J⁴/(16ω²v²)`, against the independent
sparse-sector scan `numerics/results/memory-scan-1.json` on all `main-*`/`Dscan-*` runs, pass criterion fixed in advance
at 8%.  **Measured agreement 0.9%--5.8% (ratios 1.009--1.058) across `Δ ∈ {1.5,2,3,6,12}`, `k_0 ∈ [0.4,1.8]` — all pass.**

### 3.4 The soft memory zero — **COMPUTED; universality OPEN**

As `k → 0` at fixed `Δ > 1`: `v → 0`, `ω → J(Δ−1)`, hence `T(k) = 16(Δ−1)²k² + O(k⁴)`, `R(k) = 1 − 16(Δ−1)²k²` — **total
reflection of a soft magnon, with a quadratic zero** — and by §3.2, `δx(k) = −(1/s)T(k)`.  In the frequency variable
`T ≈ 32(Δ−1)²(ω−ω_gap)/J`, *linear in the excess energy above the gap*; crossover momentum `k_* = 1/(4(Δ−1))`.  **Not
established:** that the quadratic zero and its coefficient `16(Δ−1)²` are **universal**, i.e. functions of the kink's
asymptotic data (vacuum pair, `U(1)` charge, gap) and not of the microscopic `B`-tensor — the actual `C ⇒ B` obligation
(§6.2).  *Guard:* numerics P2 — slope `2.00 ± 0.05`, prefactor `32(Δ−1)²` to `±15%` over `k_0 ∈ [0.03,0.2]`, `Δ = 2,4`.

### 3.5 Conjecture M of the brief — **REFUTED as literally stated**

"`δx` equals the zero-frequency limit of the soft factor summed over the event" is **false in the easy-axis XXZ chain**.
Two independent reasons: (a) `δx = −⟨N_T⟩/s` holds with the *same* coefficient for every `k`, `Δ` and packet, whereas any
soft-factor expression varies with them; (b) `δx` is insensitive to `δ_t(k)` entirely — a purely transmitting wall with
`δ_t ≡ 0` still displaces by exactly `−1/s`.  **The soft factor is a phase; the memory quantum is a charge.**  The
surviving — and strictly stronger — statement is §3.1 + §3.2: *memory is the DC weight of the boundary current, and the
soft data enter only through `T(k)`.*

---

## §4. Conjecture Bc — "the two `2`s" — **CONJECTURE, FROZEN**

Two independent `2`s appear.  (i) In M1, the soft Wigner phase-slope coefficient of Theorem S2-2body: on D8,
`dδ_phys/dk_s|_0 = 2 sgn(v_h−v_s) = 2`, a two-site spatial shift of the soft packet off a hard magnon.  (O9 is emphatic
that this is a **phase slope, not a scattering length**: the FM's relative-momentum scattering length is zero, since
`δ_{12}/ε → 2xy/(y−x)` in the joint soft limit.)  (ii) In M2, the memory quantum of Theorem M-quant: `1/s = 2` sites.

**Conjecture Bc.**  Both equal `|q_hard|/s`, with `q_hard` the hard leg's `U(1)` charge relative to its vacuum — i.e.
*the soft phase coefficient and the memory quantum are the same asymptotic-charge datum*.  **Falsifier, cheapest
first:** the spin-1 ferromagnet two-magnon Bethe phase should give `dδ/dk_s = 1`, not `2`; independently the spin-1
easy-axis chain should give `δx/N_T = −1/s = −1` (numerics P8).  **If the spin-1 phase slope is not `1`, the coincidence
is numerology and must be dropped from the paper.**  *Shard:* `corner-b-draft.md` §10; bd issue filed at freeze.

---

## §5. The SPT dichotomy — **DRAFT status, not frozen**

Scoping shard `spt-scoping-draft.md` (reconciled at freeze); definitions D19--D23. **Nothing in this section has been
through an L6 loop.**  It is recorded at honest draft status, with the draft's own confidences, because it is what the
deciding computation must decide.

**The mechanism, in one line.**  By G0(d), `Q[f;ξ] ▹ ω_α = −Σ_x (Δf)(x) 𝒥_{x|x+1}(ξ) ▹ ω_α + boundary` — *the soft factor
is weighted by the total variation of the profile, never by the profile itself*.  A bulk profile (`f(−∞)=f(+∞)`) gives
paired insertions; a net-jump profile (`f = 1_{[0,∞)}`) collapses to a **single unpaired** bond insertion, which is
exactly where `𝔞_α = ℂ_{ω_α}[G]` is seen — a *dichotomy*, not a uniform modification.

**No-go to concede up front (draft confidence 0.90).**  Every coefficient of the `k`-expansion of a soft amplitude is
built from finitely many derivatives of `V` at the identity, i.e. from `𝔥_α` data; and for every Haldane-protecting group
the Lie-algebra shadow of `[ω]` vanishes (`H²(so(3),ℝ) = 0`; `D₂`, `ℤ₂×ℤ₂` have no Lie algebra).  Therefore **`[ω]`
cannot appear in any coefficient of the soft expansion, at any order, at an edge or in the bulk.**

| id | statement | draft status |
|---|---|---|
| **SPT-B** | *(bulk no-go)* Under (H1),(H2), all legs bulk magnon legs, profile with `f(−∞)=f(+∞)`: `F_f` and every coefficient of its `k`-expansion depend on `V_α` only through `Ad(V_α)`, an honest **linear** representation; hence **`[ω]` drops out of all bulk `n`-point soft amplitudes**.  Equivalently `[E, V⊗V̄] = 0` with cocycle `ω·ω̄ = 1` (condition C3, refs/arxiv-0802.0447). | **SKETCH** (⟨1⟩5; confidence 0.90).  Obligations `N1` (covariance of the tangent-space gauge fixing), `N2` (wave-packet reading in a multi-leg amplitude), `N3` (a bulk magnon leg is genuinely in `𝒦_{αα}`, not a two-endpoint sector in disguise).  **`N3` is the only place SPT-B could fail.** |
| **SPT-E** | *(edge modification)* Half-infinite chain, `G`-symmetric gapped boundary, `f = 1_{[0,∞)}`: (a) the soft factor is `V_α(g)` on `H_edge`, so `𝖲(g)𝖲(h) = e^{iω_α(g,h)}𝖲(gh)`; (b) `dim H_edge ≥ d_ω`, `d_ω>1 ⟺ [ω_α]≠0`; (c) an unpaired endpoint insertion survives `k→0` where a bulk profile leaves only paired ones, residue = edge charge; (d) that residue lies in the `[ω]`-twisted charge lattice (`𝒜KLT`: half-integral edge `S^z`; `TRIV`: integral). | **CONJECTURE** (0.85).  **(a) is not A1 re-read**: A1 gives a padded-window-vector action and a state-level `PGL(χ)` action; the edge-Hilbert-space register is SKETCH box S-A1 (D21(a) caveat). |
| **SPT-T** | *(twist)* The soft factor for an `h`-rotation at a `g`-twist endpoint is `V(h)V(g)V(h)^{-1} = [ω(h,g)/ω(g,h)] V(g)` — the **slant product** of `[ω]`, the 1D `H²` shadow of the 2D `H³` monodromy-defect statement of refs/arxiv-1412.5604. | **CONJECTURE** (0.75).  Risk: on an infinite chain the slant phase at one endpoint is compensated at the other, so the observable is necessarily the *relative* charge of the two endpoints (a string-order statement). |
| **SPT-D** | *(double soft)* The continuum pattern inverts: single-soft *coefficients* are unmodified, and the cocycle lives in the **ordered double-soft limit** at an edge, `𝖲(g)𝖲(h) = e^{iω(g,h)}𝖲(gh)`. | **CONJECTURE** (0.60).  The gauge-invariant residue is again a degeneracy statement, not a measurable phase. |
| **SPT-M** | *(edge memory — the payoff)* For `[ω]≠0` the reflection matrix has a nonzero edge-label-changing channel at all momenta including `k→0`, so `Δm_L` (D22) is a protected, quantised, permanent shift; for `[ω]=0` every such channel is gappable by a symmetric boundary perturbation and `Δm_L → 0`. | **CONJECTURE** (0.55).  Protection of the *channel* is solid; **quantisation of `Δm_L` is not argued.** |

**A closed route, recorded so it is not reattempted.**  For on-site `G`, refs/arxiv-2405.00439 states
`(U^{[i₂,j₂]})†(U^{[i₁,j₁]})† U^{[i₂,j₂]} U^{[i₁,j₁]} = 𝟙`; our `G` **is** on-site, so **no commutator of truncated
**A closed route, recorded so it is not reattempted.**  For on-site `G`, refs/arxiv-2405.00439 states
`(U^{[i₂,j₂]})†(U^{[i₁,j₁]})† U^{[i₂,j₂]} U^{[i₁,j₁]} = 𝟙`; our `G` **is** on-site, so **no commutator of truncated
symmetry operators can detect our `[ω]`** — every `[ω]`-observable must be a degeneracy/selection-rule statement or a
**two-endpoint** (string-order) statement with dressed endpoints.
`𝒜KLT` and `TRIV` tensors of D23, for `f ∈ 𝔉_c` and for `f = 1_{[0,∞)}`.  If the bulk contraction returns an `Ad(V)`-only
**The one deciding computation** (draft ⟨1⟩8; hours, exact transfer algebra, no DMRG).  Contract `Q[f;ξ]` against the
`𝒜KLT` and `TRIV` tensors of D23, for `f ∈ 𝔉_c` and for `f = 1_{[0,∞)}`.  If the bulk contraction returns an `Ad(V)`-only
coefficient in **both** models and the half-infinite contraction returns a single unpaired `X(ξ)` generating a 2-dim
projective `D₂`-rep for `𝒜KLT` and a 1-dim linear one for `TRIV`, SPT-B+SPT-E are established and claim SPT rises to
SKETCH.  If the half-infinite contraction also collapses to `Ad(V)`, **claim SPT is REFUTED** and the surviving
publishable statement is the clean no-go SPT-B.  Either outcome is a result.

## §6. The three edges

### 6.1 A ⇒ C (asymptotic symmetry ⇒ soft theorem) — **OPEN**

**Not supplied by Corner A.**  This is the campaign's core proof obligation and it is not discharged. Corner A supplies
G0(e) — an exact operator continuity equation in `𝔄_loc`, true of the *true* model whatever its ground state, needing no
MPS at all — and, in M1 only, the Ward residue (R14)/(R15).  It supplies **no** Adler zero, **no** universality and **no**
rederivation of O7/O9 (the RETRACTED row, §1.5). **Closed at the freeze:** the LSZ/Ward reduction for one hard magnon —
ML4 (§2.5), whose decisive content is Lemma ML4-A: the orthogonal current is `O(k²)` because the zero-soft channel
*matches* the descendant range and the on-shell trace is `C¹`, **not** because of the Ward identity itself.  **Also
settled, negatively:** process independence over unrestricted local sources is **REFUTED** by the four-site source `O_η`
of D24(e), which leaves `M_1` fixed and shifts the linear soft coefficient — so any A ⇒ C statement must carry a
source-class hypothesis, and `𝒮_W` (D24(d)) is the sharp one (ML5-A). **Still missing:** regularity of `⟨out|J_k|in⟩`
uniform in volume and in `k_s→0` (ML3); ML4 for two hard magnons into a three-magnon channel (`ML4-3`, bd `tns-axg`);
`𝒮_W`-membership for a nontrivial microscopic source class (bd `tns-axg`); remainder control in a stated norm (ML1, ML6).
**Proved along this edge:** Theorem S2-2body (§2.3) and Theorem ML5-B (§2.5); and, from G0(e), oracle **O1** in the
one-magnon sector only.

### 6.2 C ⇒ B (soft theorem ⇒ memory) — **PARTLY PROVED**

Not the shape the brief conjectured (§3.5).  Its true shape is: Corner C (soft behaviour of `t(k)`) ⟶ `T(k) → 0` as `k→0`
(memory Adler zero) ⟶ `δx(k) = −T(k)/s` (Theorem M-quant). **Proved:** the right-hand implication — §3.1 unconditionally,
and §3.2 *unconditionally for the projected dynamics*, where Kato--Rosenblum applied to the rank-two Fano perturbation
supplies H-AD outright; for the full chain it stays conditional on H-AD (bd `tns-d51`). **Computed:** the middle step in
the `≤3`-wall projection, §3.4, where the soft zero is unconditional for `H_3`. **Open:** that the quadratic zero of `T`
and its coefficient are *universal* functions of the kink's asymptotic data.  The ML5 counterexample (D24(e)) is a warning
here too: universality is a statement *relative to a source class*, and that class must be named.

### 6.3 B ⇒ A (memory ⇒ asymptotic symmetry) — **SKETCH (claim B3)**

**(i) Sector rigidity — PROVED.**  For all `t`, `ϱ_t ∈ 𝒦_{αβ}` with the *same* pair `(α,β)`: `e^{iHt}` is a quasi-local
automorphism (Lieb--Robinson) and D9(b) disjointness is preserved by automorphisms of `𝔄`.  **No memory event can change
the vacuum-pair label**; it is read off, not shifted.

**(ii) Memory = transported asymptotic charge — PROVED given D17.** `δx = (1/2s)[ϱ_{t_f}(𝔮^R_c) − ϱ_{t_i}(𝔮^R_c)] =
−(1/2s)[ϱ_{t_f}(𝔮^L_c) − ϱ_{t_i}(𝔮^L_c)]` for any cut `c` outside the support of the leg content at `t_i,t_f`, since
`𝔮^L_c + 𝔮^R_c + (S^z_c − (s_α+s_β)/2)` is the conserved regularised magnetisation.

**(iii) Torsor — SKETCH.**  Within a fixed pair `(α,β)` the kink states of definite charge form a **`ℤ`-torsor** under
lattice translation, and `state ↦ 𝔮^R_c/2s` is the moment map of that `ℤ`-action.  Memory is valued in that torsor: `δx ∈
ℤ` post-selected on a channel, and in `(1/s)·conv{0,−1}` for a superposed event. (Conditional on thermodynamic-limit
flatness of the kink band, draft item R5.)

**(iv) What measuring `δx` identifies — SKETCH, corrected at freeze.**  The **topological** content is the vacuum-pair
label of D9(d): under (T), a point of `(G/H_α)×(G/H_α)`, whose global-symmetry-invariant content is the double coset in
`H_α\G/H_α`.  That label is *rigid* by (i).  What `δx` measures is the **charge transferred between the two spatial
infinities** within the fixed label — a separate `U(1)` datum.  *(The earlier reading — memory valued in the `𝒜`-orbit of
vacua, `δx` the `G_diag`-invariant label of `𝒜 = (G_L×G_R)/G_diag` — cited `A2-orbit-r1` and is withdrawn; and in this
model's `χ=1` unbroken-`U(1)` product-vacuum setting A1 gives `N_α = G`, so the endpoint-state orbit is a **single
point**.  The charge-transfer torsor of (iii) is viable, but it is not that claim.)*  *Shard:* `corner-b-draft.md` §7.

---

## §7. Freeze index

| item | status | shard | checker |
|---|---|---|---|
| Lemma IT, WI | PROVED | corner-a.md ⟨1⟩2--⟨1⟩3 | corner_a_check.py C0--C2b |
| A1 (a)--(g) | PROVED (padded windows for (d1)) | corner-a.md ⟨1⟩4 | C6, C8, C8b |
| S-A1 (GNS/edge realisation) | SKETCH, load-bearing | corner-a.md ⟨1⟩4.⟨2⟩9 | — |
| A2 (a)--(f); (e) under (T) | PROVED | corner-a-kinks.md ⟨1⟩8--⟨1⟩9 | C7, C11 |
| S-A2 (continuum-`Ω_vac` uniformity) | SKETCH, load-bearing | corner-a-kinks.md ⟨1⟩10.⟨2⟩3 | — |
| G0 (a)--(e); Lemma SBP; Prop FM | PROVED | corner-a-goldstone.md ⟨1⟩5--⟨1⟩7 | C3--C5, C9, C10 |
| A2-orbit-r1 / G0-soft-r1 | REFUTED / RETRACTED | §1.4, §1.5 | C7 / — |
| O1--O10 | PROVED | oracle-bethe.md | oracle_bethe_check.py |
| ML2 | PROVED | ml2-completeness.md | ml2_completeness_check.py |
| **S2-2body** | **PROVED, FROZEN** | soft-current-recon.md + oracle-bethe.md | soft_current_recon_check.py + 2 others + fm-displacement-scan |
| **S-general** | **CONJECTURE, FROZEN** on the class `𝒮_W` (D24(d)); FALSE without it; obligations ML1, ML3, ML6 | §2.4 | — |
| ML4-A + exact Ward projection | PROVED | ml4-ward-reduction.md ⟨1⟩2--⟨1⟩3 | ml4_check.py |
| **ML4** | **PROVED** (one hard magnon, all `C_c^∞(I)` packets, uniform in `N`); **OPEN** for `n≥2` hard into a 3-magnon channel (`tns-axg`) | ml4-ward-reduction.md ⟨1⟩4--⟨1⟩5 | ml4_check.py (exponent 1.997--1.9999; red mutant 0.9999) |
| **ML5** | **REFUTED** unrestricted (counterexample D24(e)); **PROVED** conditionally on `𝒮_W` (ML5-B), with ML5-A the sharp iff; `𝒮_W`-membership OPEN (`tns-axg`) | ml5-universality.md | ml4_check.py (coefficient error `9.96·10^{-6}`) |
| M-flux | PROVED | corner-b-draft.md §2, §6 | numerics P6 |
| **M-quant** | **THEOREM** for the projected dynamics `H_3` (H-AD proved there via Kato--Rosenblum + Feshbach); **PROVED given (H-AD)** for the full chain (`tns-d51`) | memory-quantization.md | mquant_check.py; numerics P1, P4, P5, P8 |
| t(k), T(k), δ_t(k) | COMPUTED (≤3-wall exact; `O(Δ^{-2})` leakage measured) | corner-b-draft.md §5 | crosscheck_corner_b_tk.py (0.9--5.8%) |
| soft memory zero `T = 16(Δ−1)²k²` | COMPUTED; universality OPEN | corner-b-draft.md §5.2 | numerics P2 |
| Conjecture M (brief's literal form) | REFUTED | corner-b-draft.md §10 | — |
| **Bc** ("the two 2s") | **CONJECTURE, FROZEN**; spin-1 falsifier | §4 | not yet computed |
| SPT-B | SKETCH (draft); obligations N1--N3 | spt-scoping-draft.md ⟨1⟩5 | not yet run |
| SPT-E / -T / -D / -M | CONJECTURE (draft) | spt-scoping-draft.md ⟨1⟩4 | not yet run |
| A ⇒ C | OPEN; closed at `n=1` (S2-2body + ML4 + ML5-B); unrestricted universality REFUTED | §6.1 | ml4_check.py |
| C ⇒ B | PROVED for `H_3`; PROVED given (H-AD) for the full chain; universality of `T`'s zero OPEN | §6.2 | mquant_check.py |
| B ⇒ A (B3) | (i),(ii) PROVED; (iii),(iv) SKETCH | §6.3 | — |

**Freeze rule.**  Changing any statement above requires reopening the relevant L6 loop and recording a new verdict next
to the artifact; `claims/CLAIMS.md` carries the same rule in its footer.
