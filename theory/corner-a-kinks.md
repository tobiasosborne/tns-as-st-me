# Corner A — the broken case: sectors, half-infinite strings, and kinks

**Revision r2** (2026-08-25), after [`verdicts/corner-a-r1.md`](verdicts/corner-a-r1.md)
= FAIL(WI,A1,A2,G0).  Disposition: [`corner-a-r1-response.md`](corner-a-r1-response.md).
Numerics: [`checks/corner_a_check.py`](checks/corner_a_check.py) (ALL PASS).

Proof shard for claim **A2**.  Companion shards: [`corner-a.md`](corner-a.md)
(Lemma IT, **WI**, **A1**), [`corner-a-goldstone.md`](corner-a-goldstone.md)
(Lemma SBP, **G0**), [`corner-a-pitfalls.md`](corner-a-pitfalls.md) (§5).
Definitions D1--D5, D9--D12 of [`definitions.md`](../definitions.md); symbols in
[`notation.md`](../notation.md).  Steps ⟨1⟩1--⟨1⟩7 live in the companion
shards; numbering continues.  Structure per L6b.

**Two r1 claims are retracted here.**
1. **A2(e) was false.** r1 said the `𝒜`-orbit is the set of vacuum pairs and
   that `[g_Lg_R^{-1}] ∈ 𝒜 = (G_L×G_R)/G_diag` is the diagonal-invariant label.
   The pair space is `(G/H_α)×(G/H_α)` — for M1, `S²×S²` (dim 4) versus
   `SU(2)` (dim 3) — and `g_Lg_R^{-1} ↦ hg_Lg_R^{-1}h^{-1}` under the diagonal
   action, so it is not invariant (check C7).  The correct complete invariant is
   the **double coset** in `H_α\backslash G/H_α`; ⟨1⟩9(e) is restated.
2. **"A kink is the contact term of a broken truncated symmetry" is a slogan,
   not a theorem.**  No contact term is defined anywhere in this repo, no
   distributional Ward identity is written, and no matrix element is shown to
   be supported at coincident insertions.  The phrase is demoted to a mnemonic
   (corner-a-pitfalls.md Flag 3) and does not appear in any PROVED row.

What is proved is a **sector jump**: the finite truncated symmetry never leaves
the vacuum sector; its half-infinite limit exists in the weak-* topology only,
with an explicit rate; and that limit is a kink state disjoint from the vacuum
folium.  The jump is invisible at every finite `|R|` and appears exactly in the
limit.

---

## ⟨1⟩8. LEMMA D (sector labels are superselected)

**ASSUME.** ⟨1⟩1 and D9(a).  Recall that membership `ϱ ∈ 𝒦_{αβ}` requires the
*factorised* asymptotics
`lim_{n→+∞} ϱ(D\,τ_n(O)) = ϱ(D)\,ω_β(O)` and
`lim_{n→−∞} ϱ(D\,τ_n(O)) = ϱ(D)\,ω_α(O)` for all `D,O ∈ 𝔄_loc`.

**PROVE.**
(i) Every state `ψ` normal with respect to some `ϱ ∈ 𝒦_{αβ}` again lies in
`𝒦_{αβ}`.
(ii) Hence `𝒦_{αβ} ∩ 𝒦_{α'β'} = ∅` and the states in them are mutually
disjoint whenever `(α,β) ≠ (α',β')`.
(iii) `ω_α ∈ 𝒦_{αα}`, and every MPS state decorated on finitely many sites and
bonds by tensors drawn from `{A_α}` with the *same* tensor at each end lies in
the corresponding `𝒦`; the convergence in the definition holds with rate
`λ_E` (D1(c)).

**⟨2⟩1. PROVE (i).**

**⟨3⟩1.** It suffices to treat a vector state `ψ = ⟨Ψ, π_ϱ(·)Ψ⟩`, `‖Ψ‖=1`: a
general normal state is a norm-convergent convex combination of such, and every
bound below is uniform in `‖O‖`, `‖D‖`.
Justification: normal states of `π_ϱ(𝔄)''` are countable convex combinations of
vector states.

**⟨3⟩2.** Fix `ε > 0`.  Since `π_ϱ(𝔄_loc)Ω_ϱ` is dense in `H_ϱ`, choose
`C ∈ 𝔄_loc` with `‖Ψ − π_ϱ(C)Ω_ϱ‖ < ε`.  Then for every `W ∈ 𝔄`,
`|ψ(W) − ϱ(C^†WC)| ≤ 2ε‖W‖(1+ε)`.
Justification: GNS density and Cauchy--Schwarz.

**⟨3⟩3.** For `|n|` large enough that `supp(τ_n(O))` is disjoint from
`supp(C) ∪ supp(D)`, `C^†D\,τ_n(O)\,C = C^†DC\,τ_n(O)`.
Justification: locality of `𝔄` (commuting algebras on disjoint supports).

**⟨3⟩4.** Hence `ϱ(C^†D\,τ_n(O)\,C) = ϱ(C^†DC\,τ_n(O)) → ϱ(C^†DC)\,ω_β(O)`
as `n→+∞`, by the factorised asymptotics of `ϱ`.
Justification: ⟨3⟩3 and D9(a).

**⟨3⟩5.** Combining ⟨3⟩2 and ⟨3⟩4,
`limsup_n |ψ(D\,τ_n(O)) − ψ(D)ω_β(O)| ≤ c\,ε\,‖D‖‖O‖` with `c` absolute.  As
`ε` was arbitrary, `ψ ∈ 𝒦_{αβ}` at `+∞`; the argument at `−∞` is identical.
Justification: ⟨3⟩2, ⟨3⟩4, and `|ϱ(C^†DC) − ψ(D)| ≤ 2ε‖D‖(1+ε)`.

**⟨3⟩6. QED.**

**⟨2⟩2. PROVE (ii).** A state has at most one limit along `τ_n`, and
`ω_β ≠ ω_{β'}` for `β ≠ β'` (D2(a): the `ω_α` are pairwise distinct), so some
`O` separates them and `𝒦_{αβ} ∩ 𝒦_{α'β'} = ∅`.  If two states in different
sectors were not disjoint, their GNS representations would share a
subrepresentation, producing a state normal with respect to both; by (i) that
state would lie in both sectors, contradiction.
Justification: ⟨2⟩1, D2(a), D9(a), and the definition of disjointness.
**⟨3⟩1. QED.**

**⟨2⟩3. PROVE (iii).** For a decorated MPS state (D1(e)) whose tensor is
`A_β` on `[m,∞)`, and for `O ∈ 𝔄_W`, `D ∈ 𝔄_{W'}`, contracting the window
between `W'` and `τ_n(W)` gives a factor `E_β^{\,n−const}` applied to a fixed
matrix; by D1(c), `E_β^m(Y) = tr(Y)\,r_β + O(λ_E^m‖Y‖)`.  The leading term
factorises the expectation into `ϱ(D)·ω_β(O)`, the remainder is
`O(λ_E^{n}\,‖D‖‖O‖)`.
Justification: D1(c), D1(d), D1(e), and the spectral decomposition of `E_β`.
**⟨3⟩1. QED.**

**⟨2⟩4. QED.** □

**⟨2⟩5. Remark.** (iii) is what makes D9(a) usable: the sector label of an MPS
state is read off from the tensor at `±∞`, and the reading is exponentially
fast.  Nothing here needs the split property or normality of endpoint states
(cf. corner-a.md ⟨1⟩4.⟨2⟩9).

---

## ⟨1⟩9. THEOREM A2 (broken truncated symmetry creates a kink)

**ASSUME.** ⟨1⟩1, ⟨1⟩3 (WI), ⟨1⟩8; a `G`-covariant vacuum family with
`|Ω_vac| ≥ 2`; fix `α` and `g ∈ G` with `β := g·α ≠ α`.

**PROVE.**
(a) *(finite `R` never leaves the sector)* For every finite `R = [a,b]`,
`ω_α ∘ Ad(U_R(g)^†) ∈ 𝒦_{αα}`; explicitly it is the decorated state with
`A_α` outside `R`, `A_β` inside `R`, `V_α(g)^{-1}` on `∂_-R` and `V_α(g)` on
`∂_+R` — a kink at `∂_-R` and an antikink at `∂_+R`, of total topological
charge zero.
(b) *(the half-infinite limit exists, weak-* only)* For `O ∈ 𝔄_W`, `w := max W`
and `y > w`, and for **every** `λ̃ ∈ (λ_E,1)` there is `C_λ̃ < ∞` with
  `|ω_α(U_{[x,y]}(g)^† O\, U_{[x,y]}(g)) − ϱ_x^{(g)}(O)| ≤ C_λ̃\,‖O‖\,λ̃^{\,y−w}`,
where `ϱ_x^{(g)}` is the **two-sided decorated state** of D1(e′) with `A_α` on
`(−∞,x−1]`, `V_α(g)^{-1}` on bond `(x−1|x)`, and `A_β` on `[x,∞)`.  Hence
`1_{[x,∞)}g ⊳ ω_α = ϱ_x^{(g)}` in the weak-* topology of D3(c).
**Two r1 corrections:** the rate is `λ̃`, not `λ_E` — a bare `λ_E^{y−w}` is
false when `E` has a Jordan block at modulus `λ_E`; and `ϱ_x^{(g)}` is *not* a
D1(e) decorated state (it differs from any uniform tensor on a half-line), so
it is constructed by D1(e′), which supplies positivity, normalisation and
consistency, rather than imported.
The convergence is **not** in norm on `𝔄^*`, and the operators `U_{[x,y]}(g)`
have **no** strong limit on `H_{ω_α}` (a fortiori: by (d) the limit state is
not even normal).
(c) *(the limit is a kink)* `ϱ_x^{(g)} ∈ 𝒦_{αβ}`.
(d) *(the sector jump)* By (a) every finite-`R` state is normal with respect to
`ω_α`; by (c) and ⟨1⟩8(ii) the limit is disjoint from `ω_α`.  Thus the weak-*
limit of a path of vector states of `H_{ω_α}` leaves the folium of `ω_α`.  The
jump is invisible at every finite `|R|` and is created entirely by the
surviving end.  *(r1 called this "the contact term"; that is a name, not a
proved identity — see the header and corner-a-pitfalls.md Flag 3.)*
(e) *(vacuum-pair classification — corrected)* `G_L × G_R` acts componentwise on
`Ω_vac × Ω_vac`.  If `G` acts transitively on `Ω_vac` then
`Ω_vac × Ω_vac ≅ (G/H_α) × (G/H_α)`, transitively, with stabiliser of `(α',β')`
equal to `H_{α'} × H_{β'}`.  This is **not** `(G×G)/G_diag`.  The complete
invariant **modulo the global (diagonal) symmetry** is the double coset
  `𝔡(α_L,α_R) = H_α\, g_L^{-1}g_R\, H_α ∈ H_α \backslash G / H_α`   (D9(d)),
which for `G = SU(2)`, `H_α = U(1)` is the relative angle
`\cos θ = \hat n_L·\hat n_R`.  The r1 label `[g_Lg_R^{-1}] ∈ 𝒜` is **not**
diagonal-invariant and is withdrawn.
(f) *(inverse direction)* Every kink sector `𝒦_{αβ}` with `β ∈ G·α` is reached
this way: choose `g` with `g·α = β`.

**⟨2⟩1. PROVE (a).** WI (⟨1⟩3) gives the decoration exactly, for every finite
window and boundary vectors; the phase `e^{i|R|θ_α(g)}` cancels in the state.
The decoration equals `A_α` on `(−∞,a−1]` and on `[b+1,∞)`, so by ⟨1⟩8(iii)
both asymptotic labels are `α`.  Normality with respect to `ω_α` is immediate:
`U_R(g) ∈ 𝔄_loc` is unitary.
Justification: ⟨1⟩3.⟨2⟩4--⟨2⟩5, ⟨1⟩8(iii), D9(a).
**⟨3⟩1. QED.**

**⟨2⟩2. PROVE (b).**

**⟨3⟩1.** By WI, `ω_α ∘ Ad(U_{[x,y]}(g)^†)` is the decorated state with `A_α`
outside `[x,y]`, `A_β` inside, `V_α(g)^{-1}` on `(x−1|x)` and `V_α(g)` on
`(y|y+1)`.
Justification: corner-a.md ⟨1⟩3 (WI-state).

**⟨3⟩2.** `ϱ_x^{(g)}` exists as a state: it is the two-sided decoration of
D1(e′), whose finite-window restrictions are positive, normalised and
consistent.  *(r1 used it before constructing it — objection 10.)*
Justification: D1(e′).

**⟨3⟩3.** For `O ∈ 𝔄_W` with `y > w := max W`, the two states carry identical
decorations on `(−∞,w]`; they differ only in the environment right of site `w`,
which is `E_β^{\,y−w}(V_α(g)r_αV_α(g)^†)` for the first and `r_β` for the
second.
Justification: ⟨3⟩1, D1(d), D1(e), D1(e′).

**⟨3⟩4.** `tr(V_α(g)r_αV_α(g)^†) = tr(r_α) = 1`, and by D1(c), for every
`λ̃ ∈ (λ_E,1)` there is `C_λ̃` with `‖E_β^m(Y) − tr(Y)r_β‖ ≤ C_λ̃λ̃^m‖Y‖`.  The
remaining window contraction is bounded by `const·‖O‖`.  This gives the stated
bound.
Justification: D1(c) in its `λ̃` form, D1(e).  *(A bare `O(λ_E^m)` would be
false for a defective subleading eigenvalue — objection 10.)*

**⟨3⟩5.** The transfer gaps agree along the orbit: by (IT),
`A_{g·α}^s = e^{-iθ_α(g)}V_α(g)(𝒰(g)A_α)^sV_α(g)^{-1}`, and unitarity of `u(g)`
gives `Σ_s(𝒰(g)A_α)^sW(𝒰(g)A_α)^{s†} = E_α(W)`; hence
`E_β = Ad_{V_α(g)} ∘ E_α ∘ Ad_{V_α(g)^{-1}}`, a similarity, so
`spec(E_β) = spec(E_α)` and `λ_{E_β} = λ_{E_α} = λ_E`.
Justification: D2(b), unitarity of `u(g)`.  *(r1 left this leaf implicit.)*

**⟨3⟩6.** The bound is uniform over `O ∈ 𝔄_W` for each fixed `W` but its
constant depends on `W` through `w`; so the limit is weak-*, not a norm limit
in `𝔄^*` — and it cannot be one, since by (c)/(d) the limit is outside the
folium of `ω_α` while every approximant is inside it.
Justification: ⟨3⟩4, ⟨2⟩3, ⟨1⟩8(ii).

**⟨3⟩7. QED.**

**⟨2⟩3. PROVE (c).** `ϱ_x^{(g)}` is a decorated MPS state with tensor `A_α` on
`(−∞,x−1]` and `A_β` on `[x,∞)`; by ⟨1⟩8(iii) its asymptotic labels are `α` at
`−∞` and `β` at `+∞`, i.e. `ϱ_x^{(g)} ∈ 𝒦_{αβ}`.
Justification: ⟨1⟩8(iii), D9(a).
**⟨3⟩1. QED.**

**⟨2⟩4. PROVE (d).** (a) gives normality of the approximants; (c) and
⟨1⟩8(ii) give disjointness of the limit from `ω_α ∈ 𝒦_{αα}`, since
`(α,β) ≠ (α,α)`.  A state disjoint from `ω_α` is not normal with respect to it.
Justification: ⟨2⟩1, ⟨2⟩3, ⟨1⟩8(ii).
**⟨3⟩1. QED.**

**⟨2⟩5. PROVE (e).**
**⟨3⟩1.** The componentwise action is well defined by D2(a); transitivity and
the stabiliser `H_{α'}×H_{β'}` are orbit--stabiliser for `G` acting on
`Ω_vac ≅ G/H_α` in each factor.  The stabiliser is **not** `G_diag`.
Justification: D2(a), D9(d), orbit--stabiliser.
**⟨3⟩2.** Writing `α_L = g_L·α`, `α_R = g_R·α`, the quantity `g_L^{-1}g_R` is
invariant under the diagonal `g_i ↦ hg_i`, and changes to
`h_1^{-1}(g_L^{-1}g_R)h_2` under `g_L ↦ g_Lh_1`, `g_R ↦ g_Rh_2` (`h_i ∈ H_α`),
i.e. it is well defined and complete precisely as a double coset in
`H_α\backslash G/H_α`.
Justification: D9(d), direct computation.
**⟨3⟩3.** By contrast `g_Lg_R^{-1}` transforms as `hg_Lg_R^{-1}h^{-1}` under
the diagonal action and is therefore **not** invariant; and `(G×G)/G_diag ≅ G`
has the wrong dimension for `Ω_vac×Ω_vac` whenever `H_α ≠ {e}` (M1: `3` versus
`4`).  Verified numerically: the relative angle is invariant to `1.4·10^{-16}`
while `‖g_Lg_R^{-1} − h g_Lg_R^{-1} h^{-1}‖ = 1.364`.
Justification: check C7; r1 objection 11.
**⟨3⟩4. QED.**

**⟨2⟩6. PROVE (f).** Immediate from (b)--(c) with a chosen `g`.
Justification: ⟨2⟩2, ⟨2⟩3.  **⟨3⟩1. QED.**

**⟨2⟩7. QED.** A2 is proved. □

**⟨2⟩8. Summary of topologies (the question "in what sense does the limit
exist?").**

| object | finite `R` | half-infinite limit |
|---|---|---|
| operator `U_R(g)` | in `𝔄_loc`, unitary | **does not exist** in `𝔄`; no strong limit on `H_{ω_α}` (unbroken case: corner-a.md ⟨1⟩4(b); broken case: a fortiori, by (d)) |
| state `ω_α∘Ad(U_R^†)` | vector state in `H_{ω_α}` | **exists in weak-\***, rate `λ̃^{\,y−w}` for any `λ̃ ∈ (λ_E,1)` on each `𝔄_W` (b) |
| sector label `(α_L,α_R)` | `(α,α)` | `(α,g·α)` — jumps only in the limit (d); classified by the double coset (e) |
| norm distance in `𝔄^*` | — | **does not converge**: approximants are normal, limit is not |

---

## ⟨1⟩10. Instantiations, and one honest gap

**⟨2⟩1. M2 (Ising / easy-axis XXZ, `Δ > 1`).** `G ⊇ ℤ₂` (global spin flip),
`Ω_vac = {↑,↓}`, `A_↑ = (1,0)`, `A_↓ = (0,1)` at `χ = 1` in the Ising limit,
`H_↑ = ℤ₂`-trivial, `V ≡ 1`.  A2(b) then reads: the half-infinite flip
`Π_{y≥x}σ^x_y` applied to `|↑↑⋯⟩` produces `|⋯↑↑↓↓⋯⟩`, a sharp domain wall at
`x`, and A2(d) says that this state is disjoint from the ferromagnetic vacuum —
a genuine gapped topological sector.  This is the model in which "kink" carries
its usual meaning and in which A2's superselection language is sharp.  The
*continuous* `U(1)` about `z` is unbroken here and is where WI/A1 apply with
`H_α = U(1)`, `[ω_α] = 0`.
Justification: D6-type direct computation; ⟨1⟩9.

**⟨2⟩2. M1 (isotropic ferromagnet).** `G = SU(2)`, `Ω_vac ≅ S²`, `H_α = U(1)`,
`χ = 1`, `λ_E = 0` (the estimate in ⟨1⟩9(b) is *exact* at every `y > w`).
A2 applies verbatim for every `g ∉ H_α`: the half-infinite rotation
`U_{[x,∞)}(g)` maps `|↑↑⋯⟩` to the sharp domain wall `|⋯↑↑\,\hat n\hat n⋯⟩`,
which is disjoint from the vacuum.  Its infinitesimal version,
`d/dε\,U_{[x,∞)}(e^{εS^y})|_0 ∝ Σ_{z≥x}S^-_z`, is the half-infinite Goldstone
cloud — this object, not any local operator, is what Corner B's memory
observable must be paired with (docs/framing.md §4: memory lives in the bond
data).
Justification: D6, ⟨1⟩9, corner-a-goldstone.md ⟨1⟩7.

**⟨2⟩3. SKETCH (uniformity over a continuous vacuum manifold) — LOAD-BEARING.**

> **BOXED — what is missing, and what it is load-bearing for.** For `Ω_vac` a continuum (M1), A2 produces an
> *uncountable* family of mutually disjoint sectors `𝒦_{α,g·α}`, hence a
> non-separable direct-sum representation, and the separating observable of
> ⟨1⟩8(ii) degrades as `g → e`: there is no `ε > 0` with
> `|ω_α(O) − ω_{g·α}(O)| ≥ ε` uniformly for `g` outside a neighbourhood of
> `H_α` of fixed size.  Equivalently, the kink creation energy tends to zero as
> `g → e`, so A2's sectors are *algebraically* superselected but not
> *energetically* separated.  Missing: (i) a statement of A2 uniform in `g`,
> with the separation quantified by `d(g·α, α)`; (ii) a selection criterion
> (finite energy? a fixed reference vacuum at `−∞` plus a `L¹` condition on the
> profile, cf. D3(a)?) that cuts the continuum down to a physically meaningful
> family.  This is exactly the "careful selection of function spaces" of
> docs/framing.md §3, and it is unresolved.  **Consequence for the campaign:**
> M1's kinks must not be used as superselection sectors in Conjecture S; M1 is
> the *Goldstone/magnon* model and M2 is the *kink* model.  Nothing in A2(a)--(f)
> is affected — they are proved for each fixed `g ∉ H_α`.

**⟨2⟩4. Remark (relation to the literature).** The mixed-vacuum ansatz used to
*describe* these sectors variationally is the topological excitation ansatz of
refs/arxiv-1810.07006 (`p5_excitations.tex`, Eq. (eq:kink)): "the domain wall
interpolates between the two ground states", with the mixed transfer matrix
`Ẽ` whose "spectral radius [is] smaller than one -- otherwise the two ground
states would not be orthogonal".  That spectral-radius statement is the
variational shadow of ⟨1⟩8(ii); A2 supplies the sector-theoretic content that
the ansatz presupposes, and additionally states *how* such a state is created
(by a broken truncated symmetry) — which the ansatz literature does not.
Note also the momentum ambiguity of a single kink recorded there
(`Ã_R ← Ã_R e^{iφ}` shifts `p ← p + φ`): it is a genuine caveat for any
soft/memory statement about single kink legs, and Corner C must fix the
convention by working with kink pairs.

---

## Claim status produced by this shard (r2)

| item | status | where |
|---|---|---|
| **A2(a)**, **(c)**, **(d)**, **(f)** — finite `R` stays in `𝒦_{αα}`; the weak-* half-string limit is a kink state in `𝒦_{α,g·α}`, disjoint from the vacuum folium (sector jump) | **PROVED**, for each fixed `g ∉ H_α` | ⟨1⟩9.⟨2⟩1, ⟨2⟩3, ⟨2⟩4, ⟨2⟩6 |
| **A2(b)** — existence of the weak-* limit with rate `λ̃^{y−w}`, `λ̃ ∈ (λ_E,1)`, limit object constructed by D1(e′) | **PROVED** (r1's `λ_E^{y−w}` rate and its undeclared limit object are retracted) | ⟨1⟩9.⟨2⟩2 |
| **A2(e)** — r1 form (`𝒜`-orbit = vacuum pairs; label `[g_Lg_R^{-1}]`) | **REFUTED** | ⟨1⟩9.⟨2⟩5.⟨3⟩3, check C7 |
| **A2(e′)** — pair space `(G/H_α)×(G/H_α)`; complete diagonal invariant = double coset in `H_α\backslash G/H_α` | **PROVED** (replacement) | ⟨1⟩9.⟨2⟩5 |
| "kink = contact term of a broken truncated symmetry" | **NOT A CLAIM** — mnemonic only; demoted to corner-a-pitfalls.md Flag 3 | — |
| A2 uniformity over a continuous `Ω_vac` (M1) | **SKETCH, load-bearing** for Corner B on M1 | ⟨1⟩10.⟨2⟩3 |
| supporting **Lemma D** (sector disjointness) | **PROVED** — survived the r1 attack unchanged (objection 9) | ⟨1⟩8 |
