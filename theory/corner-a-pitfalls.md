# Corner A — §5: pitfalls, scope, and terminology discipline

**Revision r2**, after [`verdicts/corner-a-r1.md`](verdicts/corner-a-r1.md).
Campaign-level list, referenced by [`corner-a.md`](corner-a.md),
[`corner-a-goldstone.md`](corner-a-goldstone.md), and
[`corner-a-kinks.md`](corner-a-kinks.md).  Sharded out of `corner-a.md` under
L2.  Definitions D1--D12 of [`definitions.md`](../definitions.md).

---

### 5.1 Normalizability, the vacuum manifold, boosts, and *which* symmetry is broken

**(P1) Three different objects at `k = 0`.**  These must never be conflated:
1. *The momentum-`k` ansatz vector* `|Φ_k(B_G(ξ))⟩ = Q_k(ξ)Ω_α`.  For the
   ferromagnet and `ξ = ξ_x` this is `\tfrac{i}{2}Σ_x e^{ikx}S^-_x|Ω⟩`, with
   `⟨Φ_k(B_G)|Φ_{k'}(B_G)⟩ = \tfrac14·2πδ(k−k')` for **every** `k`, including
   `k = 0` (from `⟨Ω|S^+_yS^-_x|Ω⟩ = δ_{xy}`).  So it is a δ-normalised
   generalised vector, never an element of `H_A`, and `k = 0` is **not** special
   in that respect.  Assertions that "the `k=0` magnon fails to be normalisable
   while `k ≠ 0` is fine" are simply wrong.
2. *The smeared charge* `Q_Λ(ξ)Ω_α` (profile `1_Λ ∈ 𝔉_ec(ξ)`, D3(a)).  Here
   `k = 0` **is** special, and it is the sharp discriminator between broken and
   unbroken directions:
   - `ξ ∈ 𝔥_α` (normal ordered): by G0(d) the sum telescopes,
     `Q_Λ(ξ)Ω_α = (𝒥_{maxΛ}(ξ) − 𝒥_{minΛ−1}(ξ))Ω_α`, whose window norm is
     bounded **uniformly in `Λ`** (it is two bond insertions, norm² `≤ 4‖X_α(ξ)‖²`).
     The charge is implementable.
   - `ξ ∈ 𝔪_α` (broken): no such telescoping exists (that is exactly G0(b)),
     and for the ferromagnet `‖Q_Λ(ξ_x)Ω_α‖² = |Λ|/4 → ∞` (generator convention:
     corner-a-goldstone.md ⟨1⟩7).  The broken charge is **not** implementable;
     only the derivation `O ↦ ω_α([Q_Λ(ξ),O])`, `Λ ⊇ supp(O)`, survives.
     This is the lattice form of the Goldstone non-implementability theorem and
     the sharp analogue of the soft-photon zero-mode subtlety.
3. *The finite vacuum rotation* `ω_{g·α}`, `g ∉ H_α`: a state **disjoint** from
   `ω_α` (corner-a-kinks.md ⟨1⟩8), macroscopically different, in no sense a
   vector in `H_A`.  Exponentiating (2) does not give (1), and neither is (3).

**(P2) No boosts.** Nothing here uses Galilean or Lorentz covariance; the
kinematic factor of G0(e) is `(e^{ik}−1)`, a lattice difference operator, not a
covariant object (and see §5.2(iv): it is *not* by itself a soft factor).  Any soft factor derived from Corner A will depend on lattice
momenta and group velocities `v(k)` and cannot be recast covariantly.

**(P3) The ferromagnet is type B.** corner-a-goldstone.md ⟨1⟩7(iii) derives the
`2 → 1` Goldstone count from the tensor data, and ibid. ⟨1⟩7(iv) derives
`ω ∼ k²` (matching oracle O1).  Consequently
the soft expansion must be organised in **`k`**, not in `ω`: by oracle O10 the
energy variable produces a direction-labelled Puiseux series
`δ = 2σ\sqrt{2ω_s/J} + O(ω_s)`.  Every soft statement in this campaign is an
expansion in `k`.

**(P4) Which symmetry is broken — FM versus Ising/XXZ.**  These are *not* the
same situation and must never be conflated:
- *M1, isotropic FM.* `G = SU(2)` is **fully broken** in the ground state; the
  stabiliser `H_α = U(1)` survives.  `Ω_vac ≅ S²` is a **continuum**.  The
  Goldstone (magnon) belongs to the broken directions `𝔪_α`, so G0's
  pure-gauge statement does **not** apply to it (corner-a-goldstone.md ⟨1⟩6(b);
  note that what fails for a broken direction is the *same-vacuum return*, not
  (IT) itself — see Flag 5).  There are no gapped kinks: the "kinks" produced by A2 interpolate between infinitesimally
  different vacua and cost arbitrarily little energy.  The `U(1)` that survives
  is *not* the Goldstone direction, and `[ω_α]=0` for it.
- *M2, easy-axis XXZ (`Δ>1`) / Ising.* The broken group is the **discrete**
  `ℤ₂` spin flip; `Ω_vac = {↑,↓}`; kinks are genuine gapped domain walls; the
  continuous `U(1)` about `z` remains unbroken and *is* where (IT), WI and A1
  apply with `H_α = U(1)`.  There is no Goldstone; "soft" means a low-frequency
  expansion **about the magnon gap**, and this must be said explicitly wherever
  M2 is used.
- Consequently the phrase "the broken symmetry" is ambiguous in this project
  and is banned: every statement names its group (`G`, `H_α`, or the broken
  complement `𝔪_α`) explicitly.
- The *classifying* data also differ: M1 has a continuum `Ω_vac ≅ S²`, so A2
  produces uncountably many mutually disjoint sectors with no uniform
  separation (corner-a-kinks.md ⟨1⟩10.⟨2⟩3, SKETCH); M2 has `Ω_vac = {↑,↓}` and
  two genuinely gapped sectors.  **M1 is the magnon model, M2 is the kink
  model**; M1 kinks must not be used as superselection sectors in Conjecture S.

### 5.2 Exact, exact-in-a-limit, or about the true model?

Three distinctions, all of which r1 blurred and the r1 critic attacked.

**(i) Exact finite-window identities, unconditional.**  Lemma IT
(corner-a.md ⟨1⟩2); **WI** (⟨1⟩3) — but only with the window hypothesis (W1)
or (W2), *not* for every `Λ ⊇ R`; **A1**(a),(c),(d1),(d2),(e),(f),(g);
**G0**(a),(b),(d); **Lemma SBP** (corner-a-goldstone.md ⟨1⟩5) *including its two
boundary terms*; **A2**(a),(c),(d),(f).  These hold for any injective covariant
family, ground state or not.

**(ii) Exact only in a named limit — always say which.**
- The ansatz **gauge/null identity** `|Φ_k(𝒩_k(X))⟩ = 0` and hence
  **G0(c)** are *false* as finite-window statements: the remainder is two
  boundary vectors of norm `Θ(1)`.  They hold (D12(a)) exactly in norm for
  decaying (`c_0`, wave-packet) profiles, and (D12(b)) only after
  `|Λ|^{-1/2}` normalisation for a plane wave.
- **A1(a)** half-infinite limits: weak-*, in fact eventually constant on each
  `𝔄_W`.  **A2(b)**: weak-*, rate `λ̃^{y−w}` for any `λ̃ ∈ (λ_E,1)` — **not**
  `λ_E^{y−w}`, which is false when `E` has a Jordan block at modulus `λ_E`.
- Nothing converges in operator norm or strongly: A1(b), A2(⟨2⟩8).

**(iii) About the true model, versus about the ansatz manifold.**
- **G0(e)** (`[H,Q[f;ξ]] = Σ_x(f(x+1)−f(x))j_{x|x+1}(ξ)`) is an operator
  identity in `𝔄_loc`.  It is true of the *true* model, whatever its ground
  state, and needs no MPS at all.  This is why it, and not G0(b), is the only
  candidate seed for Corner C.
- **Everything else** in Corner A is a statement about `ω_{A_α}` and the linear
  ansatz space.  It becomes a statement about a true ground state only when the
  MPS is exact — which for M1 (isotropic FM, `χ=1`, exact product vacuum, exact
  one-magnon eigenvectors) it is, and for M2 kinks at generic `Δ` it is not.
- If `ω_A` only approximates a ground state with local error `ε` on windows of
  size `w`, WI and A1 hold for `ω_{gs}` up to `O(ε)` on such windows.  No claim
  currently relies on this; if one does, the `ε` must be tracked explicitly.
- **Not established anywhere:** that the excitation-ansatz S-matrix equals the
  true S-matrix.

**(iv) What Corner A does NOT give (r1 objection 18, conceded).**  G0(e) alone
implies **no** Adler zero, **no** universal soft coefficient, and **no**
rederivation of oracle O7/O9.  In a matrix element it says only
`⟨out|[H,Q_k]|in⟩ = (e^{ik}−1)⟨out|J_k|in⟩`; if `⟨out|J_k|in⟩ = C_hard + O(k)`
then hard data enters at `O(k)`, and if `⟨out|J_k|in⟩` has a `1/k` singularity
there is no zero at all.  The factor is also convention-dependent (kernel
`e^{−ikx}` gives `e^{−ik}−1`; reversing the current orientation flips the
sign).  Its Hamiltonian-independence is the tautology that a discrete
difference was factored out *after* defining an `H`-dependent current.  Corner C
must supply: regularity of `⟨out|J_k|in⟩` at `k=0`, an LSZ/scattering
reduction, and a Ward identity relating `J_0` to the external charges.  Only
**O1** is rederived (corner-a-goldstone.md ⟨1⟩7), in the one-magnon sector,
where the FM current happens to supply a second lattice difference.

### 5.3 Terminology discipline (coinages flagged)

| term used here | status | established name / correction |
|---|---|---|
| "MPO Ward identity", **(WI)** | **coinage** of HANDOFF §1.2 | pulling-through; symmetry action on the virtual level; string-order structure of refs/arxiv-0802.0447 |
| "lattice asymptotic symmetry group `𝒜`" | **coinage, and misleading** — see flags below | no established name; the effective object is `𝒜_eff = G/N_α ≅ ρ_α(G) ⊆ PGL(χ)` (D4(b)) |
| "asymptotic charge algebra `𝔞_α`" | **coinage**; realised on window vectors only (A1 ⟨2⟩9) | twisted group algebra `ℂ_ω[G]` of the projective edge representation |
| "bond current potential `𝒥`" | **coinage** (from docs/framing.md §4) | none; the virtual/tangent data `X` of the MPS |
| "kink = contact term of a broken truncated symmetry" | **coinage, slogan only — NOT a theorem** (see flag 3) | domain wall; topological sector of the excitation ansatz (refs/arxiv-1810.07006) |
| "SPT index `[ω_α]`" | **established** | second cohomology class classifying 1D SPT phases (refs/arxiv-1412.5604, refs/arxiv-2011.12127) |
| "intertwining relation (IT)" | **established** | fundamental theorem of MPS / intertwiner (refs/arxiv-0802.0447 Lemma 1, C1) |
| "soft factor / Adler zero" for G0(e) | **not yet earned** — see §5.2(iv) | G0(e) is a lattice continuity equation, nothing more |

**Flag 1 — `𝒜` is neither a group nor the classifying object.**  HANDOFF §2 and
r1 called `𝒜 = (G_L×G_R)/G_diag` the lattice asymptotic symmetry *group* and
used it to classify both endpoint sectors and vacuum pairs.  Both uses are
wrong:
- It is a group only when `G` is abelian (`G_diag ⊴ G×G` iff `G` abelian).
- *Unbroken case*: the orbit of the vacuum is `G/N_α = 𝒜_eff`, not `𝒜`; the
  stabiliser is `S_α ⊇ G_diag`, equal to `G_diag` only when the projective
  action is faithful.  A `χ=1` `ℤ₂`-symmetric product vacuum has `N_α = G` and
  a **one-point** orbit (corner-a.md ⟨1⟩4(e)).
- *Broken case*: the vacuum-pair space is `(G/H_α)×(G/H_α)`, **not**
  `(G×G)/G_diag` — for M1 that is `S²×S²` (dim 4) versus `SU(2)` (dim 3) — and
  the diagonal-invariant label is the **double coset** in `H_α\backslash G/H_α`
  (the relative angle `\hat n_L·\hat n_R` for M1), not `[g_Lg_R^{-1}]`, which
  is not diagonal-invariant at all (checks C7).
**The paper must not write "asymptotic symmetry group" without saying which of
`𝒜_eff`, `(G/H_α)×(G/H_α)`, or `H_α\backslash G/H_α` is meant.**

**Flag 2 — WI orientation.**  HANDOFF §1.2 line 42 puts `V(g)` on the left
boundary bond and `V(g)^{-1}` on the right.  Under the (IT) convention of D2(b)
the correct assignment is the **opposite**: `V^{-1}` on `∂_-R`, `V` on `∂_+R`
(corner-a.md ⟨1⟩3.⟨2⟩8; check C1 vs C1b, errors `5.6·10^{-17}` vs `0.267`).
The brief is a historical document and is not edited; the correction lives here.
Note that a `ℤ₂` test tensor with `V = Z = V^{-1}` cannot detect this and must
not be used to "confirm" the orientation.

**Flag 3 — "contact term" is a name, not a result.**  What A2 proves is a
*sector jump*: finite strings give kink--antikink decorations inside
`𝒦_{αα}`, and the weak-* half-string limit lies in `𝒦_{α,g·α}`.  No contact
term is defined in `notation.md` or `definitions.md`, no distributional Ward
identity is written, and no matrix element is shown to be supported at
coincident insertions.  The slogan may be used as a mnemonic in prose; it may
**not** appear as the content of a PROVED claim.

**Flag 4 — two SKETCH boxes, both load-bearing.**
- corner-a.md ⟨1⟩4.⟨2⟩9 (split property / normality): load-bearing for
  docs/framing.md's demand that the charge algebra act on the physical state
  space.  That demand is **not met**.
- corner-a-kinks.md ⟨1⟩10.⟨2⟩3 (uniformity over a continuous `Ω_vac`):
  load-bearing for any `g → e` limit, Goldstone-cloud, or continuum-vacuum
  memory construction in M1.  A2 is closed only pointwise in `g`.
Neither may be silently used downstream.

**Flag 5 — "(IT) fails for broken directions" is wrong.**  r1's G0 said this;
it contradicts D2(b), which asserts (IT) for *every* `α` and `g`, with target
tensor `A_{g·α}`.  In the all-up FM with a broken `x`-rotation, (IT) holds
exactly with `χ=1`, `V ≡ 1`, `θ ≡ 0`, and target `A_{g·α}`.  What fails is the
**same-vacuum return** `g·α = α`; that is why `B_G(ξ)` is not a same-vacuum
tangent and the pure-gauge conclusion does not apply.  The corrected wording is
used throughout r2 (corner-a-goldstone.md ⟨1⟩6(b), ⟨2⟩7).
