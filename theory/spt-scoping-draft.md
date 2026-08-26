# SPT scoping draft — can the projective class `[ω]` modify a lattice soft theorem?

**SUPERSEDED by `theory/spt-rebuild.md` (2026-08-26) after critic r1 FAIL (`theory/verdicts/triangle-r1.md` S1--S8); retained as history.**  **Status: DRAFT, pre-critic — reconciled against claims DAG @ freeze,
2026-08-26.**  Three stale citations flagged in
[`corner-a-pitfalls.md`](corner-a-pitfalls.md) Flag 6 have been repaired in
place, each marked `(Reconciled at freeze …)`: ⟨1⟩2.⟨2⟩3 no longer calls
`(e^{ik}−1)` an "exact lattice Adler zero" (that cited `G0-soft-r1`,
**RETRACTED**); ⟨1⟩4.⟨2⟩2(a) no longer reads A1 as an action on an edge Hilbert
space (A1 gives a padded-window-vector action and a state-level `PGL(χ)` action
only; the edge realisation is the SKETCH box corner-a.md ⟨1⟩4.⟨2⟩9); and the
headline form, verdict item 2, and test **T2** are re-phrased accordingly.
Sd1--Sd10 were promoted to `definitions.md` **D19--D23** at the freeze; the
`Sd`-numbers are retained in this shard for readability, and the D-numbers are
the single source (L4).  The claim statuses live in
[`theory/TRIANGLE.md`](TRIANGLE.md) §5 and `claims/CLAIMS.md`.

Scoping study for claim **SPT** of [`claims/CLAIMS.md`](../claims/CLAIMS.md)
(status CONJECTURE), i.e. §5.4 of `HANDOFF_MPS_SOFT_THEOREM.md`.

**Standalone shard.** Per the conflict protocol this file introduces its own
definitions `Sd1…Sd10` and claim ids `SPT-B/E/T/D/M`. Nothing is written into
`definitions.md`, `notation.md` or `claims/CLAIMS.md`; merge proposals are in
§9. `D1–D5`, `D9–D11` and the PROVED claims `WI`, `A1`, `G0` are used as given
and never restated. Ground truth (L3): `refs/arxiv-0802.0447`,
`refs/arxiv-1412.5604`, `refs/arxiv-2405.00439`, `refs/arxiv-1509.07840`.
Structure per L6b.

**Bottom line up front.** The evidence points hard at a *dichotomy*, not a
uniform modification: `[ω]` is provably invisible in every bulk soft amplitude
and survives only where a symmetry string has an unpaired end — an open edge or
a twist. The surviving sensitivity is **not** a modification of the
soft-expansion *coefficients* (those are `[ω]`-blind even at an edge, because
for every Haldane-protecting group the Lie-algebra central extension vanishes);
it is a modification of the **representation type** of the soft factor.
Verdict, confidence, deciding computation: §8.

---

## ⟨1⟩1. Setup and the honest soft variable

### ⟨2⟩1. Sd1 (the comparison pair)

Fix `d = 3` (spin 1) and `G = D₂ = {e, R_x, R_y, R_z}`, `R_a := e^{iπS^a}`,
with `H²(D₂,U(1)) = ℤ₂`. Two members of D1/D2 (injective, `G`-covariant,
`H_α = G`, `Ω_vac = {α}` — unbroken, unique gapped ground state):

* **`𝔄KLT`** (`[ω] ≠ 0`). `χ = 2`, `A^0 = σ_z/√3`, `A^{±1} = √(2/3) σ_±`,
  `Λ = 𝟙`; for `u = e^{iπS^z}` the fundamental theorem gives `V = σ_z` and
  string order `−4/9` [`refs/arxiv-0802.0447`, "Example 1: AKLT state"]. By
  `SU(2)`-covariance `u = e^{iπS^x}` gives `V = σ_x`, so
  `V(R_x)V(R_z) = −V(R_z)V(R_x)`: `[ω] ≠ 0`.
* **`TRIV`** (`[ω] = 0`). Any injective spin-1 MPS with the same `G`, `χ = 2`,
  and `V` a *linear* `D₂`-rep (e.g. `V(R_x) = V(R_z) = diag(1,−1)`). The
  physical representative is the large-`D` phase, `|ψ⟩ ≈ ⊗_x |m=0⟩`, `V ≡ 1`.

Both have on-site, **non-anomalous** `G` (MPO bond dimension 1), a unique
ground state, and a gapped triplet magnon.

### ⟨2⟩2. Sd2 (magnon leg)

A *bulk magnon leg* is `|Φ_k(B)⟩` of D5(a) on `A_α`, D5 null directions
quotiented out. The Haldane one-magnon branch is gapped with minimum at
`k = π`: `ω(k) = Δ + (k−π)²/2m* + …`.

### ⟨2⟩3. Sd3 (edge leg and edge space)

The *half-infinite chain* `x ≥ 0` with one open virtual index. Its low-energy
space is `H_edge ⊗ (bulk Fock)`, where `H_edge` carries the uncontracted virtual
index with `G`-action `V_α(g)` (D2(b)). An *edge leg* is a state in `H_edge`.
For `𝔄KLT`, `H_edge ≅ ℂ²` carries the spin-1/2 projective irrep of `D₂`; for
`TRIV` it splits into one-dimensional linear characters.

### ⟨2⟩4. Sd4 (twist leg)

A *`g`-twist at bond `b`* is the state `1_{[b,∞)}·g ⊳ ω_α` of D3(c) — the
weak-* limit of half-infinite strings, by WI/A1 the vacuum decorated by the
single bond insertion `𝒱_b(g)`. It is a localised excitation of the
`G`-symmetric Hamiltonian and a *string-endpoint sector* in the sense of A1.

### ⟨2⟩5. Sd5 (the soft expansion variable — stated honestly)

Settled first, because it is the first thing a referee attacks. Three
inequivalent candidates; only one supports a symmetry-based soft theorem.

| candidate | definition | frequency reached | Ward identity? | verdict |
|---|---|---|---|---|
| `σ1` | `k → 0` at fixed magnon branch | `ω(0) = ` *top* of the band, **not** small | yes — `k = 0` operator **is** the charge `Q(ξ)` | **use this** |
| `σ2` | `κ := k − π → 0` (band bottom) | `ω → Δ`, the minimum | no — the `k = π` operator is not a symmetry generator | reject |
| `σ3` | `1/L`, `L` = width of a modulated profile `f(x/L) ∈ 𝔉_ec` | mixed | yes, exactly (D3, D10(c)) | equivalent to `σ1`; use as the rigorous carrier |

**Sd5.** The *soft variable* is `k` (equivalently the inverse profile width
`1/L`), and "soft" means **zero momentum transfer**: the emitted quantum's
vertex degenerates to the conserved charge. It does **not** mean zero
frequency — above a gap no on-shell one-particle state has `ω → 0`, and the
`k → 0` magnon of a Haldane chain sits at the *top* of its band. §5.4 of the
brief ("soft = low-frequency about the gap") is therefore imprecise; the
correct statement is *"soft = zero momentum, i.e. the Adler/current limit; the
frequency stays `≥ Δ` throughout — a genuine departure from the continuum
triangle."* The zero-*frequency* object in a gapped chain is not a particle at
all; it is the DC/memory observable of Sd10.

### ⟨2⟩6. Sd6 (soft form factor)

With no massless pole, the LSZ residue extraction of the continuum
(`refs/arxiv-1509.07840` §2.1, `⟨α|J^μ|β⟩ = iq^μF/q² · M + N^μ`) has no lattice
analogue; the amplitude must be the *form factor itself*. For `ξ ∈ 𝔤` (or, for
finite `G`, `g ∈ G`), a profile `f`, and states `|α⟩, |β⟩`:

```
  F_f(ξ; β,α) := ⟨β| Q[f;ξ] |α⟩            (Lie case,  D10(c))
  F_f(g; β,α) := ⟨β| U[f·g]  |α⟩            (finite case, D3(b,c))
```

Sd6(a) *bulk soft amplitude*: `f ∈ 𝔉_c` or a wave packet with
`f(−∞) = f(+∞)`, all legs bulk magnons.
Sd6(b) *edge/twist soft amplitude*: `f ∈ 𝔉_ec` with **net jump**
`f(−∞) ≠ f(+∞)`, at least one leg an edge (Sd3) or twist (Sd4) leg.

### ⟨2⟩7. Sd7 (soft factor and its value group)

The *soft factor* is `S := lim_{k→0} F` in the sense of Sd6. Sd7 asserts only
its *type*: `S` is an element of `ℂ_{ω_α}[G] = 𝔞_α` (D4(d)) represented on the
legs' virtual data. The `[ω]`-content of a soft theorem is by definition the
class of that twisted group algebra.

---

## ⟨1⟩2. Which amplitude can carry `[ω]`? — the one-line mechanism

Settled by Abel summation against the already-proved lattice Noether identity.

**⟨2⟩1.** By D10(d) / G0(d) (`corner-a-goldstone.md ⟨1⟩6`), on the vacuum the
charge density is an exact lattice divergence of a **virtual** (bond) quantity:
`q_x(ξ) ▹ ω_α = (𝒥_{x|x+1}(ξ) − 𝒥_{x−1|x}(ξ)) ▹ ω_α`.

**⟨2⟩2.** Hence for any profile `f`, with `(Δf)(x) := f(x+1) − f(x)`,
```
      Q[f;ξ] ▹ ω_α  =  −Σ_x (Δf)(x) · 𝒥_{x|x+1}(ξ) ▹ ω_α  +  boundary terms.
```
**The soft factor is weighted by the total variation of the profile, never by
the profile itself.** Everything follows.

**⟨2⟩3 (bulk).** For `f(x) = e^{ikx}` (wave-packet sense, D3(a)),
`Δf = (e^{ik} − 1) e^{ikx}`, so
`Q_k(ξ) ▹ ω_α = −(e^{ik} − 1) Σ_x e^{ikx} 𝒥_x(ξ) ▹ ω_α`.
The prefactor `(e^{ik} − 1) = ik + O(k²)` is a **kinematic** factor coming from
the profile alone.  *(Reconciled at freeze 2026-08-26.  This step previously
called it "the exact lattice Adler zero" with a leg-independent coefficient
"already recorded in G0", and concluded that every bulk soft amplitude vanishes
linearly in `k`.  That reading cited claim `G0-soft-r1`, which is **RETRACTED**:
`(e^{ik}−1)` implies no Adler zero, no universality, and does not rederive
O7/O9 — in a matrix element the identity gives only
`⟨out|[H,Q_k]|in⟩ = (e^{ik}−1)⟨out|J_k|in⟩`, so if `⟨out|J_k|in⟩ = C_hard+O(k)`
hard data enters at `O(k)`, and if it has a `1/k` singularity there is no zero
at all.  See corner-a-goldstone.md ⟨1⟩6.⟨2⟩7 and corner-a-pitfalls.md §5.2(iv);
supplying regularity of `⟨out|J_k|in⟩`, an LSZ reduction and a Ward identity for
`J_0` is Corner C's obligation, ML3--ML5 of theory/TRIANGLE.md §2.4.)*

**What survives, and is all that ⟨1⟩5 actually needs.**  For a bulk profile the
insertions are **paired**: every `V_α(g)` is contracted against a
`V_α(g)^{-1}`, so the amplitude and every coefficient of its `k`-expansion are
functions of `Ad(V_α)` alone, and its coefficient is a *closed* contraction of
`A`'s, `B`'s and one `X_α(ξ)`.  SPT-B is a statement about **`[ω]`-independence
of the coefficients**, not about their vanishing, and it does not depend on the
retracted Adler-zero reading.

**⟨2⟩4 (edge / twist).** For `f = 1_{[0,∞)}` (`∈ 𝔉_ec`, state statements only,
D3(c)), `Δf = δ_{x,−1}` and the sum collapses to the **single unpaired bond
insertion** `−𝒥_{−1|0}(ξ)`; exponentiated, to `𝒱_b(g)`, i.e. `V_α(g)` acting
once with no partner `V_α(g)^{-1}`. This is precisely the regime in which the
twisted group algebra `𝔞_α = ℂ_{ω_α}[G]` (A1, D4(d)) is seen.

**⟨2⟩5.** So the three candidate amplitudes of the brief sort as follows.

| amplitude | virtual structure | `[ω]` visible? |
|---|---|---|
| (c) magnon–magnon, bulk | closed network; every `V` paired as `V ⊗ V̄` (condition **C3** of `refs/arxiv-0802.0447`: `[E, V⊗V̄] = 0`) | **no — provably cancels** |
| (a) magnon off an open edge | one uncontracted virtual index; `V(g)` acts once on `H_edge` | **yes**, as the projective type of `H_edge` |
| (b) magnon off a `g`-twist / string endpoint | one unpaired `𝒱_b(g)` | **yes**, as the `𝔞_α`-module structure of the endpoint sector |

**⟨2⟩6 (why the trace structure kills it — precise version).** In a closed
contraction each `V(g)` appears with a `V(g)^{-1}`, i.e. only through
`Ad(V(g)) := V(g)(·)V(g)^{-1}`. Two facts:
(i) `Ad(V(g))` is independent of the `U(1)` phase of `V(g)`, so no cocycle
*representative* can appear;
(ii) `Ad(V(g))Ad(V(h)) = Ad(ω(g,h)V(gh)) = Ad(V(gh))`, so `g ↦ Ad(V(g))` is an
honest **linear** representation and no cocycle *class* can appear either.
The same statement in the transfer-matrix language is condition C3 of
`refs/arxiv-0802.0447`, `[E, V ⊗ V̄] = 0`: the object that acts on the doubled
virtual space is `V ⊗ V̄`, whose cocycle is `ω · ω̄ = 1`.

---

## ⟨1⟩3. A no-go that must be stated, or the claim will be overclaimed

**⟨2⟩1 (vanishing infinitesimal shadow).** D4(d) records a Lie-algebra central
extension `c_α` with `[c_α] ∈ H²(𝔥_α, ℝ)` called "the infinitesimal shadow of
`[ω_α]`". For every group that protects the Haldane phase that shadow is
**zero**: `H²(so(3), ℝ) = 0` (semisimple, Whitehead), and `D₂` and `ℤ₂ × ℤ₂`
have no Lie algebra at all. Yet `H²(SO(3),U(1)) = ℤ₂` and
`H²(ℤ₂×ℤ₂,U(1)) = ℤ₂` are nontrivial.

**⟨2⟩2 (consequence — the sharp restriction).** Every coefficient of the
`k`-expansion of a soft amplitude is built from finitely many derivatives of
`V` at the identity, i.e. from `𝔥_α` data. Therefore:

> **`[ω]` cannot appear in any coefficient of the soft expansion, at any
> order, at an edge or in the bulk.** It appears only in the *global*
> (exponentiated, "large") soft charge — i.e. in the projective representation
> `V_α : G → U(H_edge)` itself.

This is the single most important honesty item in this shard. A draft that
claims "the `O(k)` Adler coefficient is shifted by the SPT class" is **wrong**.

**⟨2⟩3 (what therefore survives).** The `[ω]`-content of the soft theorem is
the *representation type* of the soft factor: its matrix dimension, its
degeneracies, and its selection rules. Concretely, with `d_ω` the minimal
dimension of an `ω`-projective irrep of `G` (`d_ω = 2` for `[ω] ≠ 0` on `D₂`,
`d_ω = 1` for `[ω] = 0`):

* the soft factor at an edge is an operator on a space of dimension `≥ d_ω`;
* for `[ω] ≠ 0` it necessarily has a nonzero **off-diagonal (edge-label
  changing)** component; for `[ω] = 0` it can be, and generically is, a scalar;
* this cannot be removed by any `G`-symmetric local deformation of the
  boundary, because `[ω]` is a bulk invariant.

**⟨2⟩4 (a second trap, recorded so it is not rediscovered).**
`refs/arxiv-2405.00439/MPU-DW.tex` states explicitly, for on-site symmetries,
that `(U^{[i₂,j₂]})† (U^{[i₁,j₁]})† U^{[i₂,j₂]} U^{[i₁,j₁]} = 𝟙`, hence
expectation value `+1`. Our `G` **is** on-site. Therefore **no commutator of
truncated symmetry operators can detect our `[ω]`** — that route is closed
before it is attempted. Relatedly, for spin 1 the physical operators
`u(R_x), u(R_z)` commute (they anticommute only in the `SU(2)` lift), and the
`−1` obtained by conjugating a single `σ_z` bond insertion by `σ_x` is
compensated by the string's far end. Every `[ω]`-observable here must be
either (i) a degeneracy/selection-rule statement, or (ii) a **two-endpoint**
(string-order) statement with dressed endpoints — precisely the condition
`tr(V Λ A_n A_m^†) ≠ 0` of Theorem 1 of `refs/arxiv-0802.0447`.

---

## ⟨1⟩4. The sharpest falsifiable statements

### ⟨2⟩1. Sd8 + **Claim SPT-B** (bulk no-go) — the theorem that will survive

**ASSUME** (H1) D1 injective uniform MPS `ω_α`; (H2) D2 on-site `G`-covariance
with class `[ω_α]`; (H3) legs `B_1,…,B_n` bulk magnon legs (Sd2); (H4) profile
`f` admissible with `f(−∞) = f(+∞)` (Sd6(a)).
**PROVE** The soft amplitude `F_f` and every coefficient of its `k`-expansion
are functions of `Ad(V_α)`-covariant data only; consequently they are unchanged
under `V_α(g) ↦ λ(g)V_α(g)` for any `λ : G → U(1)` and are identical for any
two `G`-covariant injective MPS with the same `Ad(V_α)` data. In particular

> **`[ω]` drops out of all bulk `n`-point soft amplitudes.**

*Confidence 0.90.* This is a genuine theorem, it is short, and it is the
"clean negative" the brief asks for. It is also the exact lattice counterpart
of the continuum observation in `refs/arxiv-1509.07840/Draft5.tex` that "if the
initial and final states `α,β` are such that `⟨α|δΓ|β⟩ = 0`, then the soft
theorem is not modified" — with the difference that here the *bulk* Ward
identity (WI) is **exact**, so there is no anomaly term at all to begin with.

### ⟨2⟩2. Sd9 + **Claim SPT-E** (edge modification) — the positive result

**ASSUME** (H1)–(H2) as above; (H3′) the half-infinite chain of Sd3 with a
`G`-symmetric, gapped boundary Hamiltonian; (H4′) `f = 1_{[0,∞)}` (Sd6(b)).
**PROVE**
(a) the soft factor is `V_α(g)` acting on `H_edge`, so
    `S(g)S(h) = e^{iω_α(g,h)} S(gh)` — the soft-charge algebra is the twisted
    group algebra `𝔞_α = ℂ_{ω_α}[G]`.
    *(Reconciled at freeze 2026-08-26.  This clause previously read "(this is
    A1, re-read as a statement about soft factors)".  **It is not.**  A1(d1)
    proves a twisted-algebra action on **padded window vectors** (D4(a1)) and
    A1(d2) a **state**-level `PGL(χ)` action with kernel `N_α`; on states the
    multiplier is invisible.  That `𝔞_α` acts on an edge **Hilbert space** is
    the SKETCH box corner-a.md ⟨1⟩4.⟨2⟩9 (split property / normality), which is
    **not proved** — see corner-a-pitfalls.md Flag 4 and definitions.md D21(a).
    (a) therefore inherits that box's status and may not be quoted as a
    corollary of A1.)*
(b) `dim H_edge ≥ d_ω`, and `d_ω > 1 ⟺ [ω_α] ≠ 0`;
(c) `lim_{k→0} F^edge(k) = ⟨e′| 𝔮_edge(ξ) |e⟩`, the matrix element of the
    asymptotic charge on the edge multiplet — **nonzero**, i.e. an unpaired
    endpoint insertion survives the `k → 0` limit where a bulk profile leaves
    only paired ones, with residue the edge charge.  *(Reconciled at freeze:
    previously phrased as "the bulk Adler zero of SPT-B is lifted at the edge".
    SPT-B is a `[ω]`-independence statement, not a vanishing statement, and the
    bulk Adler zero it was leaning on is the RETRACTED `G0-soft-r1`.)*
(d) the residue lies in the `[ω]`-shifted charge lattice: for `𝔄KLT` with the
    residual `U(1)` (rotations about `z`) the edge charge is **half-integral**
    (`S^z_edge = ±1/2`) while every bulk excitation carries integral charge;
    for `TRIV` the edge charge is integral.

> **Headline form** *(reconciled at freeze 2026-08-26: "the lattice Adler zero
> is exact in the bulk" is withdrawn — it cited the RETRACTED `G0-soft-r1`).*
> *In the bulk every symmetry insertion is paired and the soft amplitude is
> `Ad(V_α)`-valued, hence `[ω]`-blind; at a boundary or a symmetry twist a
> single insertion is unpaired and survives the `k → 0` limit, with residue the
> asymptotic charge of the endpoint; that residue is valued in the
> `[ω]`-twisted charge lattice and is a bulk topological invariant.*

*Confidence in truth 0.85. Confidence that it is new enough to headline 0.50*
— see §7.

### ⟨2⟩3. **Claim SPT-T** (twist)

Same as SPT-E with the edge replaced by a `g`-twist (Sd4). The soft factor for
an `h`-rotation at a `g`-twist endpoint is `V(h)V(g)V(h)^{-1} =
[ω(h,g)/ω(g,h)] V(g)`, i.e. the **slant product** of `[ω]`. This is the exact
1D, `H²` shadow of the 2D `H³` statement proved in
`refs/arxiv-1412.5604/SPT.tex` §"Projective symmetry transformation of
monodromy defects": `ω^g(k,h) ∼ α(g,k,h)α(k,h,g)/α(k,g,h)`. **Caveat
(⟨1⟩3.⟨2⟩4):** on an infinite chain the slant phase at one endpoint is
compensated at the other, so the observable is necessarily the *relative*
charge of the two endpoints — the Pollmann–Turner string-order pattern, i.e.
which dressed endpoint operators satisfy `tr(V Λ A_n A_m^†) ≠ 0`.
*Confidence 0.75; the risk is the endpoint-compensation subtlety.*

### ⟨2⟩4. **Claim SPT-D** (double soft) — the structural contrast worth having

`refs/arxiv-1509.07840` §2.2 italicises: *"if the spontaneously broken symmetry
is in fact anomalous, while the single soft limit is modified, the double soft
theorem is not."* Here the pattern **inverts**: single-soft *coefficients* are
unmodified (⟨1⟩3.⟨2⟩2), and the cocycle `ω(g,h)` lives in the **ordered
double-soft limit** at an edge, `S(g)S(h) = e^{iω(g,h)}S(gh)`. If it holds up,
a clean quotable contrast with the continuum anomaly story. *Confidence 0.60* —
the gauge-invariant residue is again a degeneracy statement, not a measurable
phase (⟨1⟩3.⟨2⟩4); check before asserting.

### ⟨2⟩5. Sd10 + **Claim SPT-M** (edge memory) — the campaign payoff

*Edge memory observable*: `m_L := Σ_x w(x) ⟨S^z_x⟩`, `w` an exponentially
decaying left-edge window, evaluated before and after a magnon wave packet
reflects off the edge; `Δm_L` is the memory.
**Claim.** For `[ω] ≠ 0` the reflection matrix has a nonzero edge-label-changing
channel at all momenta including `k → 0`, so `Δm_L` is a **protected,
quantised, permanent** shift; for `[ω] = 0` every such channel is gappable by a
symmetric boundary perturbation and `Δm_L → 0`. This is corner B for the SPT
case and is the genuinely new physical content: *SPT edges have a protected
magnon memory.* *Confidence 0.55* — protection of the *channel* is solid,
*quantisation* of `Δm_L` is not yet argued.

---

## ⟨1⟩5. Lamport proof outline for SPT-B (the branch the evidence favours)

**THEOREM SPT-B.** Under (H1)–(H4) of ⟨1⟩4.⟨2⟩1, `F_f` is `[ω_α]`-independent.

⟨1⟩1. *The bulk soft amplitude is a closed tensor network.*
  ⟨2⟩1. Every leg is a bulk magnon leg (H3), hence D5(a) with `A_α` on both
        sides; no virtual index is left uncontracted. **Justification:** D5(a).
  ⟨2⟩2. `f` has no net jump (H4), hence by ⟨1⟩2.⟨2⟩2 the insertion
        `Σ_x (Δf)(x) 𝒥_x` is a sum of *interior* bond insertions with
        `Σ_x (Δf)(x) = 0`. **Justification:** Abel summation; D10(d).
  ⟨2⟩3. QED(⟨1⟩1).

⟨1⟩2. *Under `g ∈ G` every tensor in the network transforms by conjugation.*
  ⟨2⟩1. `A_α`: `𝒰(g)A_α = e^{iθ_α(g)} V_α(g)^{-1} A_α V_α(g)` — (IT), D2(c).
  ⟨2⟩2. `B`: the tangent space at `A_α` is `𝒰(g)`-covariant with the same
        `V_α(g)`; the D5(c) null directions are mapped to null directions.
        **Obligation N1:** prove covariance of the gauge-fixing condition.
  ⟨2⟩3. `𝒥_b(ξ)`: `Ad(V_α(g))X_α(ξ) = X_α(Ad(g)ξ)` — D2(e), D4(a).

⟨1⟩3. *Only `Ad(V_α)` enters.* By ⟨1⟩1 each `V_α(g)` produced in ⟨1⟩2 is
  contracted against a `V_α(g)^{-1}` from the neighbouring tensor.
  **Justification:** ⟨1⟩1.⟨2⟩1 + associativity of the contraction.

⟨1⟩4. *`Ad(V_α)` is `[ω_α]`-free.*
  ⟨2⟩1. `Ad(λ(g)V) = Ad(V)` for any `λ : G → U(1)`: representative-free.
  ⟨2⟩2. `Ad(V(g))Ad(V(h)) = Ad(V(g)V(h)) = Ad(e^{iω(g,h)}V(gh)) = Ad(V(gh))`:
        `Ad∘V` is a linear representation, so no class survives.
  ⟨2⟩3. Equivalently `[E, V ⊗ V̄] = 0` with cocycle `ω·ω̄ = 1`.
        **Justification:** condition C3, `refs/arxiv-0802.0447`.

⟨1⟩5. *The residual normal-ordering ambiguity is a coboundary, not a class.*
  `V ↦ λV` shifts `X_α(ξ) ↦ X_α(ξ) + iλ′(ξ)𝟙`; normal ordering (D2(d),
  `θ′_α = 0`) fixes it. This shift is the *linear* (coboundary) part of the
  cocycle. **Justification:** D2(b,d).

⟨1⟩6. **QED.** By ⟨1⟩3–⟨1⟩5 `F_f` depends on `V_α` only through `Ad(V_α)`,
  which by ⟨1⟩4 is a linear representation; hence `F_f` is a function of
  `[ω_α]`-independent data. ∎

**Proof obligations before this can be raised above SKETCH.**
`N1` (⟨1⟩2.⟨2⟩2) covariance of the tangent-space gauge fixing;
`N2` legitimacy of the wave-packet reading of `e^{ikx}` in a *multi-leg*
amplitude (D3(a) states it only for single insertions);
`N3` that "bulk magnon leg" excludes hidden string endpoints — i.e. that the
one-magnon sector of a Haldane chain is genuinely in `𝒦_{αα}` (A1) and not a
two-endpoint sector in disguise. **`N3` is the only place where SPT-B could
fail**, and it is exactly the Haldane-chain subtlety (the magnon of a Haldane
chain is *not* a domain wall, but this must be said, not assumed).

The mirror outline for SPT-E is the same tree with ⟨1⟩1.⟨2⟩2 negated: `Δf`
has total mass 1, one bond insertion survives uncontracted, `Ad` is never
formed, and `V_α` acts on `H_edge` directly — whence A1's `ℂ_{ω_α}[G]`.

---

## ⟨1⟩6. Minimal numerical test (spec for a later WP)

**Model family (one Hamiltonian, one knob, both sides of the SPT transition):**
`H(D) = Σ_i S_i·S_{i+1} + D Σ_i (S^z_i)²`, spin 1, open BC, symmetry `D₂` (plus
`U(1)` about `z`). `D = 0` → Haldane, `[ω] ≠ 0`; `D = 3` → large-`D`,
`[ω] = 0`; both gapped, transition at `D_c ≈ 1`. `L ∈ {32,48,64}`;
`ξ_AKLT = 1/ln3 ≈ 0.91`, `Δ_Haldane ≈ 0.41 J`.

| id | observable | prediction `[ω]≠0` | prediction `[ω]=0` | pass/fail (fixed in advance) |
|---|---|---|---|---|
| **T0** | edge charge: polarise the right edge with a weak field, measure `m_L = Σ_x w(x)⟨S^z_x⟩` | `\|m_L\| → 1/2` (half-integral) | `\|m_L\| → 0` (integral) | pass iff `\|m_L\|_{D=0} ∈ [0.45,0.5]` and `\|m_L\|_{D=3} < 0.05` at `L=48` |
| **T1** | edge soft form factor `F⁺(k) = ⟨G_b\| Σ_x w(x)e^{ikx}S⁺_x \|G_a⟩` on the quasi-degenerate edge multiplet, `k = 0, 2π/L, 4π/L, 8π/L` | `\|F⁺(0)\| = O(1)`, off-diagonal in the edge doublet | `\|F⁺(0)\| = O(e^{−L/ξ})` | pass iff `\|F⁺(0)\|_{D=0} > 0.9` and `< 0.05` at `D=3` |
| **T2** | *control*: bulk soft amplitude on a periodic chain, excitation ansatz | `F(k)/(e^{ik}−1)` bounded and smooth as `k→0`; same functional form at `D=0` and `D=3` | identical | pass iff `F(k)/(e^{ik}−1)` has the **same** `k→0` limit at `D=0` and `D=3`, confirming SPT-B.  *(Reconciled at freeze: the criterion was "the Adler zero is order `k`", which presupposed the RETRACTED `G0-soft-r1`.  SPT-B is a `[ω]`-independence test, so the discriminator is model-to-model **agreement**, not the power of `k`.)* |
| **T3** | *payoff*: TDVP wave packet, `k₀ ≈ π ± 0.3`, width ≈ 10 sites, incident on the left edge; measure `Δm_L` | nonzero edge-flip channel, `Δm_L` persistent | `Δm_L → 0` up to `e^{−L/ξ}` | pass iff `\|Δm_L\|_{D=0} > 10 × \|Δm_L\|_{D=3}` |

**Zero-cost pre-check (minutes, exact, no DMRG).** Do T1/T2 analytically at the
`𝔄KLT` point using `A^0 = σ_z/√3`, `A^{±1} = √(2/3)σ_±` against the explicit
`TRIV` MPS of Sd1: contract by hand/transfer matrix with (i) `f ∈ 𝔉_c`
(expect the exact `(e^{ik}−1)` prefactor and an `Ad(V)`-only coefficient) and
(ii) `f = 1_{[0,∞)}` (expect a single unpaired `X(ξ) = iσ_ξ/2` on the open
index, generating a 2-dim projective `D₂`-rep for `𝔄KLT` and a 1-dim linear
one for `TRIV`). **This is the deciding computation** — see §8.

**Signal sizes are `O(1)`, not perturbative.** `1/2` vs `0`; a `2×2`
off-diagonal matrix vs a scalar. There is no small parameter to fight, which
is why this test is cheap and why a negative result would be unambiguous.

---

## ⟨1⟩7. Prior art and the daylight

### ⟨2⟩1. `refs/arxiv-2405.00439` (Garre-Rubio et al.) — the closest work

**What they actually do.** Gapped spin chains with a finite symmetry group
represented by **matrix product unitaries**, i.e. possibly **anomalous**
(non-on-site) symmetries. Anomalous ⇒ the ground state must break the symmetry
⇒ the lowest excitations are **domain walls**. They build DW creation operators
`O^{[i]}_x` by cutting a truncated MPU string and dressing its ends with fusion
tensors, prove the *equal-time* exchange relation `O^{[j]}_x O^{[i]}_y |ψ_A⟩ =
c_AB · O^{[i]}_x O^{[j]}_y |ψ_A⟩` (`i > j`), and show double exchange gives
`ω = c_AB c_BA` — **semionic** statistics for the `CZX`-type anomalous `ℤ₂`.
Detection operator: `⟨ψ_A| (U^{[i₂,j₂]})†(U^{[i₁,j₁]})† U^{[i₂,j₂]}
U^{[i₁,j₁]} |ψ_A⟩ = ω`; general `G` via `Π_i B^g_{g^i x, g^{i−1}x}`.

| axis | 2405.00439 | claim SPT here |
|---|---|---|
| symmetry | MPU, **anomalous**, non-on-site, finite `G` | **on-site, non-anomalous**, `D₂`/`SO(3)` |
| invariant | MPU anomaly (`H³`-type) + Garre22 classification | 1D SPT class `[ω] ∈ H²(G,U(1))` |
| phase | necessarily **symmetry-broken**, degenerate ground space | **unbroken SPT**, unique gapped ground state |
| excitations | domain walls (topological sectors) | magnons (trivial sector) + edge/endpoint modes |
| observable | **static** exchange phase; equal-time commutator of truncated MPUs | **dynamical** soft/`k→0` limit of a scattering form factor; memory |
| soft limit | absent | central |
| on-site case | they state it explicitly: the commutator is `𝟙`, value `+1` | consistent — we prove our effect lives elsewhere (⟨1⟩3.⟨2⟩4) |

Their on-site remark is not a nuisance, it is *support*: it says our effect
cannot be their effect, so the two results do not collide. The honest framing
in the paper: *"the anomalous/SSB counterpart of this dichotomy is the domain-
wall exchange statistics of [2405.00439]; we treat the non-anomalous/SPT case
and find that the invariant migrates from statistics to soft amplitudes at
edges and twists."*

### ⟨2⟩2. `refs/arxiv-1509.07840` — continuum soft theorems from anomalies

They modify the single-soft limit **additively**,
`M_{α,β,π}|_{q→0} = (i/F)(−⟨α|δΓ|β⟩ + q·N_{α,β})`, because an anomaly makes the
current non-conserved; and they prove the double-soft limit is **unmodified**.
Daylight: our lattice current is *exactly* conserved (D10(b) is an exact
identity), so there is no `δΓ`, no additive term, and no `1/q²` pole to LSZ
against. Our modification is **multiplicative/representation-theoretic** and,
per SPT-D, appears in the *double*-soft rather than the single-soft structure —
the opposite pattern. That contrast is quotable.

### ⟨2⟩3. `refs/arxiv-1412.5604` (2D PEPS, `H³`) and `refs/arxiv-0802.0447`

From 1412.5604, two things only: (i) the edge argument — a symmetric injective
MPS *cannot* be invariant under a single blocked MPO group representation with
nontrivial class, hence the edge is degenerate or gapless; (ii) the slant
product `ω^g(k,h) ∼ α(g,k,h)α(k,h,g)/α(k,g,h)` for monodromy defects, whose 1D
dimensional reduction is SPT-T. From 0802.0447: Lemma 1
(`V†Ã_j = e^{i(θ−θ_j)}Ã_j V†`), condition **C3** `[E, V⊗V̄] = 0` — the
technical heart of SPT-B — and Theorem 1's endpoint condition
`tr(VΛA_nA_m†) ≠ 0`, the technical heart of the two-endpoint caveat
(⟨1⟩3.⟨2⟩4).

---

## ⟨1⟩8. Verdict, confidence, and the one deciding computation

**Verdict: a dichotomy, tilted to the modified-at-edges branch — but the
modification is weaker than §5.4 of the brief assumes.**

1. **Bulk: total cancellation.** `[ω]` drops out of every bulk `n`-point soft
   amplitude. *Confidence 0.90.* Provable in one page (⟨1⟩5); the only real
   risk is obligation `N3`.
2. **Edge/twist: genuine modification, of the *type* of the soft factor.**
   An unpaired endpoint insertion survives the `k → 0` limit, the residue is
   the endpoint charge, that charge lives in the `[ω]`-twisted
   lattice/algebra, and the resulting multiplet structure is a bulk invariant.
   *Confidence 0.85.*  *(Reconciled at freeze: "the Adler zero is lifted" is
   withdrawn as a premise — the bulk zero it contrasted against was the
   RETRACTED `G0-soft-r1`.  Whether a genuine bulk Adler zero exists is Corner
   C's ML3--ML5 question, not this shard's.  The **contrast** — paired versus
   unpaired insertions — is unaffected and is the real content.)*
3. **But: no `[ω]` in any soft-expansion coefficient**, at any order, anywhere
   (⟨1⟩3.⟨2⟩2) — the Lie-algebra shadow of `[ω]` vanishes for every Haldane-
   protecting group. *Confidence 0.90.* This is the piece that must be
   conceded up front; conceding it is what makes the rest defensible.
4. **Novelty risk, not truth risk.** Items 1–2 are true; the danger is a
   referee reading item 2 as "SPT edges carry projective representations,
   restated in soft language". The load-bearing new content is the
   *combination*: (bulk no-go) + (an unpaired endpoint insertion surviving
   `k → 0`, with topologically quantised residue) + (SPT-M: protected magnon
   memory at an SPT edge). *Confidence that this suffices for the headline:
   0.50.* If SPT-M
   fails, the SPT section should be demoted to a corollary of corner A rather
   than the headline, and the paper's headline reverts to the M1 triangle.

**The single computation that decides it fastest** — the zero-cost pre-check of
⟨1⟩6, at the `𝔄KLT` point, by exact transfer-matrix algebra, no DMRG, hours
not days:

> Contract the modulated-charge insertion `Q[f;ξ]` against the `𝔄KLT` tensors
> and against the `TRIV` tensors of Sd1, for the two profiles
> `f ∈ 𝔉_c` (bulk) and `f = 1_{[0,∞)}` (edge), and read off the soft factor.
> **Decision rule.** If (i) the bulk contraction returns the exact prefactor
> `(e^{ik}−1)` with an `Ad(V)`-only coefficient in *both* models, and (ii) the
> half-infinite contraction returns a single unpaired `X(ξ)` acting on the open
> index, generating a **2-dimensional projective** `D₂`-representation for
> `𝔄KLT` and a **1-dimensional linear** one for `TRIV` — then branch 1+2 is
> established and claim SPT is upgraded to SKETCH with the statement of
> ⟨1⟩4.⟨2⟩1–⟨2⟩2. If instead the half-infinite contraction also collapses to
> `Ad(V)` data (e.g. because the boundary term is compensated as in
> ⟨1⟩3.⟨2⟩4), then `[ω]` drops out everywhere, claim SPT is **REFUTED**, and
> the surviving statement to publish is the clean no-go of SPT-B.

Either outcome is a result. The computation is small enough that it should be
done before any further prose is written on this claim.

---

## ⟨1⟩9. Merge proposals (for whoever owns the shared DBs — not applied here)

* `notation.md`: `d_ω`, `H_edge`, `m_L`, `Λ_ω`, `Δf`.
* `definitions.md`: promote Sd5 (soft variable), Sd6 (soft form factor —
  needed because no LSZ pole exists), Sd7 (soft factor valued in `𝔞_α`),
  Sd10 (edge memory).
* `definitions.md` D4(d) — **correction**: "`[c_α] ∈ H²(𝔥_α,ℝ)` … is the
  infinitesimal shadow of `[ω_α]`" must record that this shadow **vanishes**
  for every semisimple `𝔥_α` and every finite `G`, so `[ω_α]` is *not*
  recoverable from the Lie-level extension. Load-bearing for ⟨1⟩3.⟨2⟩2.
* `claims/CLAIMS.md` claim `SPT`: split into `SPT-B/E/T/D/M`, all CONJECTURE
  pending the ⟨1⟩8 computation; `depends on: WI, A1, G0, D10`.
* `HANDOFF_MPS_SOFT_THEOREM.md` §5.4 — "*magnons = the triplet mode, gapped, so
  'soft' = low-frequency about the gap*" is imprecise; see Sd5.
