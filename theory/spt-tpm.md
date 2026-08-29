<!-- ROLE: blitz lane spt-tpm; proposed replacement register for SPT-M'.
     Donors: definitions.md D19--D22, D26--D27; claims SPT-E',
     M-INDEX-fin, M-INDEX-spec, LR1-GEN; theory/memory-index.md.
     No live definition or claim is edited in this lane.  PATCH.md gives
     anchored merge instructions.

     HONEST STATUS (2026-08-29): PROVED-candidate as two conditional
     implications.  The finite boundary-window TPM theorem is unconditional
     on relaxation.  The ordered theorem assumes (E-LR2)--(E-LR3); no AKLT or
     other nonzero instance of those two clauses is proved here.  The result
     removes every wave-operator/channel hypothesis from SPT-M' but does not
     prove SPT-M'-dyn or a nonzero edge-changing amplitude. -->

# SPT-TPM — a channel-free boundary charge-history register

## 0. Result and exact scope

The operational edge-memory outcome is the change between two projective
readouts of the **same finite boundary-window charge**.  It is not the spectrum
of the generally noncommuting operator difference and is not D22's existing
wave-operator expression `W_+^†Q_edgeW_+-W_-^†Q_edgeW_-`.

There are two results.

1. **`SPT-M'-TPM-fin` (finite theorem).**  Every outcome is an integer before
   any time or window limit.  This uses D19--D20, D26(INT), automorphic
   dynamics, and no relaxation, split, conservation, scattering, or channel
   hypothesis.
2. **`SPT-M'-TPM-spec` (ordered theorem).**  Under the explicitly displayed
   boundary relaxation clauses `(E-LR1)--(E-LR3)`, every ordered limiting law
   is a probability on `ℤ`; its first moment is the ordered change of the
   boundary-window charge.  `(E-LR1)` is supplied by the live PROVED claim
   **LR1-GEN**; the substantive assumptions are `(E-LR2)` and `(E-LR3)`.

Adding D21(H-split) and the live PROVED claim **SPT-E'** supplies the physical
SPT edge/module interpretation: the registered endpoint is an
`ω_C`-projective module with shifted charge lattice and protected capacity.
Neither input is used to prove TPM support.  In particular this shard does not
identify the full TPM law with the spectral law of D22's channel operator.

### Exact hypothesis set `(H-SPT-TPM)`

Fix the following data.

**(T1) Boundary charge and windows.**  Let `C` be the unbroken D1/D2 tensor and
choose a circle generator `ξ`.  Use D19's boundary profiles
`f_L^{edge}=1_[0,L-1]` and D20's Hermitian, normal-ordered local charge

`Q_L^∂ := Q^H[f_L^{edge};ξ] = -iQ[f_L^{edge};ξ]`.             **(E.1)**

`Q_L^∂` is only an abbreviation for the existing D19--D20 object, not a new
definition of charge.

**(T2) Integral circle.**  D26(INT) holds for the selected normal-ordered
Hermitian one-site charge `S^z_x=-iq_x(ξ)`: for some
`κ∈[0,1)`, `spec S^z_x⊂κ+ℤ`.

**(T3) Dynamics and preparation.**  The half-chain quasi-local dynamics
`α_t^+` is a strongly continuous one-parameter group of `*`-automorphisms,
and `Ψ` is a unit vector in a representation on which the two measurements are
performed.  D23's AKLT half-chain Hamiltonian is the intended continuous-
symmetry example; more generally one may use any half-chain dynamics meeting
the stated automorphism assumption.  Charge conservation is not needed for
the two theorems below.

**(T4) Boundary local relaxation `(E-LR)`.**  Let `E_{L,t}` be the spectral
resolution of `Q_L^∂(t):=α_t^+(Q_L^∂)`.  Fix one sequence `T_n→∞` common to
all `L`, and put

`ω^+_{L,n}(A):=T_n^{-1}∫_[T_n,2T_n]⟨Ψ,α_t^+(A)Ψ⟩dt`,

`ω^-_{L,n}(A):=T_n^{-1}∫_[-2T_n,-T_n]⟨Ψ,α_t^+(A)Ψ⟩dt`.       **(E.2)**

For finite `t_-<t_+`, define the escaped-charge and memory-change variables

`ν:=q_- - q_+`,                 `m:=q_+ - q_-=-ν`,             **(E.3)**

and the sequential two-projective-measurement law

`p_{L;t_-,t_+}(ν):=Σ_q ||E_{L,t_+}({q-ν})E_{L,t_-}({q})Ψ||²`. **(E.4)**

Absent spectral values contribute zero.  The proposed D22 extension
`(E-LR)` consists of:

- **(E-LR1)** along the same `T_n`, both Cesàro states and every
  double-Cesàro average `p_{L,n}(ν)` of (E.4) converge for every fixed `L`;
- **(E-LR2)** with
  `𝒟_{L,t_-}(A):=Σ_qE_{L,t_-}({q})AE_{L,t_-}({q})`, the
  double-Cesàro average of
  `⟨Ψ,[𝒟_{L,t_-}(Q_L^∂(t_+))-Q_L^∂(t_+)]Ψ⟩` tends to zero for every fixed
  `L` along that same sequence;
- **(E-LR3)** writing `p_L` for the fixed-`L` time limit,
  `lim_{M→∞} sup_L Σ_{|ν|>M}(1+|ν|)p_L(ν)=0`.

The optional convenience clause is full-sequence weak convergence
`p_L⇒p` as `L→∞`.  Without it all conclusions are per `(E-LR3)` subsequence;
with it the stipulated limit law, hence its first moment, is unique.  The
order is D19's order: infinite-volume dynamics first, fixed-`L` time limits
second, then `L→∞`.

This is a proposed extension of D22, not a redefinition of live D27.  It is
D27's protocol with `W_m=[a_m,b_m]↑ℤ` replaced by the boundary windows
`[0,L-1]`, and with D13's wall-coordinate ledger replaced by a charge ledger.

---

## 1. Finite boundary-window theorem

### ⟨1⟩1. THEOREM `SPT-M'-TPM-fin`

**ASSUME.**  (T1)--(T3), a fixed `L<∞`, and finite times `t_-<t_+`.

**PROVE.**  There is `κ_L∈ℝ/ℤ` such that

`spec Q_L^∂(t) ⊂ κ_L+ℤ` for every `t`;                         **(E.5)**

(E.4) is a probability law; and every escaped-charge outcome `ν` and
edge-memory outcome `m=-ν` lies in `ℤ`.  No commutativity of
`Q_L^∂(t_-)` and `Q_L^∂(t_+)` is assumed.

**⟨2⟩1 (one-site lattice).**  Every eigenvalue `λ` of the selected Hermitian
one-site charge obeys `λ-κ∈ℤ`.

*Justification.*  D26(INT); equivalently the finite-dimensional spectral
calculation `e^{2πiλ}=e^{2πiκ}`.  This is donor computation **IDX-FW.1** in
`theory/memory-index.md` ⟨1⟩1.⟨2⟩1 and live claim **M-INDEX-fin**.

**⟨2⟩2 (boundary-window coset).**  One may take
`κ_L=Lκ (mod ℤ)` in (E.5) at `t=0`.

*Justification.*  By D19--D20 and (E.1),
`Q_L^∂=Σ_{x=0}^{L-1}S^z_x`.  Different-site terms commute, so finite spectral
addition and ⟨2⟩1 give `spec Q_L^∂⊂Lκ+ℤ`.  This is named arithmetic
**SPT-TPM-FW.1**, the boundary-window instance of donor computation
**IDX-FW.2** and claim **M-INDEX-fin**.

**⟨2⟩3 (same coset at both times).**  Equation (E.5) holds with that same
`κ_L` for all `t`.

*Justification.*  Spectrum is invariant under the `C*`-automorphism `α_t^+`
of (T3).  This is named computation **SPT-TPM-FW.2**, identical to donor
**IDX-FW.3** in `theory/memory-index.md` ⟨1⟩1.⟨2⟩4 and claim
**M-INDEX-fin**.

**⟨2⟩4 (positivity).**  Every weight in (E.4) is nonnegative.

*Justification.*  It is a sum of squared norms of sequential spectral
projections.  This is donor computation **IDX-TPM.1** in
`theory/memory-index.md` ⟨1⟩5.⟨2⟩1 and claim **M-INDEX-fin**.

**⟨2⟩5 (normalisation without commutativity).**  Summing over both readouts
gives

`Σ_{q_-,q_+}||E_{L,t_+}({q_+})E_{L,t_-}({q_-})Ψ||²=||Ψ||²=1`.

*Justification.*  Apply Parseval first to the final spectral resolution and
then to the initial one; no interchange of projections occurs.  This is
donor computation **IDX-TPM.2** in `theory/memory-index.md`
⟨1⟩5.⟨2⟩2 and live claim **M-INDEX-fin**.

**⟨2⟩6 (offset cancellation).**  Every nonzero history branch has
`q_-,q_+∈κ_L+ℤ`, whence `ν=q_- -q_+∈ℤ` and `m=-ν∈ℤ`.

*Justification.*  ⟨2⟩3 and (E.3).  The *same* `L`, profile, normal ordering,
and observable are used in both measurements, so the common `κ_L` cancels
before any limit.  This is named arithmetic **SPT-TPM-FW.3**, identical to
`theory/memory-index.md` ⟨1⟩5.⟨2⟩3 and claim **M-INDEX-fin**; it is not
spectral arithmetic for a difference of noncommuting operators.

**⟨2⟩7. QED.**

### ⟨1⟩2. Donor-leaf transplant ledger

**ASSUME.**  The hypotheses of ⟨1⟩1.

**PROVE.**  Every donor leaf used by the finite theorem survives with only
the window geometry changed.

| donor leaf | M-INDEX datum | boundary replacement | logical change |
|---|---|---|---|
| ⟨1⟩1.⟨2⟩1 | `spec S^z⊂κ+ℤ` | same D26 charge | none |
| ⟨1⟩1.⟨2⟩2--⟨2⟩3 | interval sum and scalar offset | D19 window sum, offset `Lκ` | scalar bookkeeping only |
| ⟨1⟩1.⟨2⟩4 | automorphic spectrum invariance | half-chain automorphism | none |
| ⟨1⟩5.⟨2⟩1--⟨2⟩2 | TPM positivity/normalisation | (E.4) | none |
| ⟨1⟩5.⟨2⟩3 | same-window offset cancellation | same boundary window at both times | none |

**⟨2⟩1.**  The table follows row by row from ⟨1⟩1.⟨2⟩1--⟨2⟩6.

*Justification.*  Live claim **M-INDEX-fin**, D19--D20, and D26.

**⟨2⟩2. QED.**

---

## 2. Ordered boundary-memory theorem

### ⟨1⟩3. LEMMA (finite-window TPM mean)

**ASSUME.**  The hypotheses of ⟨1⟩1.  Define
`𝒟_{L,t_-}` as in (E-LR2).

**PROVE.**

`Σ_ν ν p_{L;t_-,t_+}(ν)
 =⟨Q_L^∂(t_-)⟩-⟨𝒟_{L,t_-}(Q_L^∂(t_+))⟩`.       **(E.6)**

Equivalently for `r_{L;t_-,t_+}(m):=p_{L;t_-,t_+}(-m)`,

`Σ_m m r_{L;t_-,t_+}(m)
 =⟨𝒟_{L,t_-}(Q_L^∂(t_+))⟩-⟨Q_L^∂(t_-)⟩`.       **(E.7)**

**⟨2⟩1.**  Expanding the first measured value gives
`Σ_q q⟨E_{L,t_-}({q})⟩=⟨Q_L^∂(t_-)⟩`.

*Justification.*  Spectral functional calculus; donor computation
**IDX-TPM.3** in `theory/memory-index.md` ⟨1⟩6 and live claim
**M-INDEX-spec**.

**⟨2⟩2.**  Expanding the final measured value after the initial projection
gives `⟨𝒟_{L,t_-}(Q_L^∂(t_+))⟩`.

*Justification.*  Sum over the final spectral resolution inside (E.4), then
use the displayed definition of `𝒟_{L,t_-}`.  This is donor computation
**IDX-TPM.4** in `theory/memory-index.md` ⟨1⟩6 and claim
**M-INDEX-spec**.

**⟨2⟩3.**  Subtraction proves (E.6), and the change of variable `m=-ν`
proves (E.7).

*Justification.*  ⟨2⟩1--⟨2⟩2 and (E.3); named arithmetic
**SPT-TPM-MEAN.1**.

**⟨2⟩4. QED.**

### ⟨1⟩4. THEOREM `SPT-M'-TPM-spec`

**ASSUME.**  `(H-SPT-TPM)`, including `(E-LR1)--(E-LR3)`.

**PROVE.**  Every `(E-LR3)`-subsequential ordered limit `p` of the escaped
charge laws is a probability supported on `ℤ`; the reflected edge-memory law
`r(m):=p(-m)` is likewise supported on `ℤ`; and, along that same subsequence,

`Σ_m m r(m)
 = lim_j[ω^+_{L_j}(Q_{L_j}^∂)-ω^-_{L_j}(Q_{L_j}^∂)]`.          **(E.8)**

Under the optional full-sequence convergence clause, `p`, `r`, and the value
in (E.8) are unique.

**⟨2⟩1 (common time subsequence).**  `(E-LR1)` can be satisfied along a
subsequence of every prescribed sequence, simultaneously for all `L`.

*Justification.*  Live PROVED claim **LR1-GEN** applies because the half-chain
lattice is countable, its quasi-local algebra is separable, `α_t^+` is
strongly continuous by (T3), and every local `Q_L^∂` has finite spectrum by
D19--D20.  LR1-GEN supplies only this binder; it supplies neither (E-LR2) nor
(E-LR3).

**⟨2⟩2 (remove the dephasing defect).**  At every fixed `L`, double-Cesàro
averaging of (E.6) along the common sequence gives

`Σ_ννp_L(ν)=ω^-_L(Q_L^∂)-ω^+_L(Q_L^∂)`.                       **(E.9)**

*Justification.*  (E-LR1) gives the three fixed-window limits and (E-LR2)
sets the averaged difference between the dephased and unmeasured final first
moments to zero.  This is the boundary instance of
`theory/memory-index.md` ⟨1⟩7.⟨2⟩1 and live claim **M-INDEX-spec**.

**⟨2⟩3 (integer support before exhaustion).**  Each `p_L` is a probability
on `ℤ`.

*Justification.*  ⟨1⟩1.⟨2⟩4--⟨2⟩6; fixed-`L` convergence in (E-LR1) occurs
on the fixed finite difference set `spec Q_L^∂-spec Q_L^∂⊂ℤ`.  This is also
the fixed-window conclusion of live claims **M-INDEX-fin** and **LR1-GEN**.

**⟨2⟩4 (spatial compactness and first moments).**  Every subsequence of
`{p_L}` has a further subsequence `p_{L_j}⇒p` for which `p` is a probability
on `ℤ` and `Σ_ννp_{L_j}(ν)→Σ_ννp(ν)`.

*Justification.*  (E-LR3) is tightness plus uniform integrability of the
first moment.  Prokhorov compactness on the closed set `ℤ` prevents loss of
mass; uniform integrability passes the first moment.  Since every `p_L` is
supported on the closed set `ℤ`, every weak limit is.  This is verbatim the
argument of `theory/memory-index.md` ⟨1⟩7.⟨2⟩3 and live claim
**M-INDEX-spec**, with boundary windows replacing padded two-tail windows.

**⟨2⟩5 (memory ledger).**  Reflecting by `m=-ν` and taking the same
subsequence in (E.9) gives (E.8).

*Justification.*  ⟨2⟩2, ⟨2⟩4, and the sign convention (E.3); named
arithmetic **SPT-TPM-MEAN.2**.

**⟨2⟩6 (no channels hidden in the proof).**  No step introduced wave
operators, asymptotic completeness, bulk/edge channel projections, definite
channel charges, or a scattering matrix.

*Justification.*  The complete dependency list of leaves ⟨2⟩1--⟨2⟩5 is
D19--D20, D26, **LR1-GEN**, **M-INDEX-fin**, **M-INDEX-spec**, and the stated
(E-LR2)--(E-LR3) hypotheses.

**⟨2⟩7. QED.**

### ⟨1⟩5. COROLLARY (optional conservation interpretation)

**ASSUME.**  The hypotheses of ⟨1⟩4 and, additionally, D10's local
charge-conservation law for the half-chain interaction, including a
charge-preserving physical boundary term.

**PROVE.**  The right side of (E.8) may be called the ordered mean charge
stored in the boundary window; its negative is the ordered mean charge that
crossed the remote cut.  This interpretation adds no restriction to the
integer support of `r`.

**⟨2⟩1.**  The Heisenberg derivative of the sum over `[0,L-1]` telescopes to
the current across `(L-1|L)` because there is no exterior bond at the physical
left boundary and the boundary Hamiltonian preserves the selected charge.

*Justification.*  D10(a)--(b), applied to D19's boundary window, and the
additional boundary-term hypothesis in this corollary.

**⟨2⟩2.**  The quantized support was already proved without this assumption.

*Justification.*  ⟨1⟩1 and ⟨1⟩4, whose ASSUME lists do not contain charge
conservation.

**⟨2⟩3. QED.**

---

## 3. Exact comparison with the current `SPT-M'`

The live claim row and `theory/spt-rebuild.md` ⟨1⟩6.⟨2⟩1 currently assume,
in order: `(H-split)`, `(H-AD-edge)`, conservation of the chosen `U(1)`
charge, and asymptotic channels with definite bulk and edge charges.  The
comparison is one line per current hypothesis.

| current `SPT-M'` hypothesis | role in the current proof | TPM replacement | disposition |
|---|---|---|---|
| D21 `(H-split)` | turns the registered `E_C` edge operator into a physical half-chain edge operator | none for (E.5)--(E.8); retain only when interpreting the protocol in the protected SPT edge module | removed from arithmetic; retained as optional interpretation |
| D22 `(H-AD-edge)` | supplies `W_±`, separated bulk packets, and `Q_tot=Q_edge+Q_bulk` on each channel | no channel object; directly measure D20's local `Q_L^∂` twice | removed completely from `SPT-M'` |
| charge conservation | rearranges the channel equality into `ΔQ_edge=-(Q_bulk,out-Q_bulk,in)` | not needed for same-coset subtraction; D10 conservation only gives the optional current reading in ⟨1⟩5 | removed from quantization; optional for transport semantics |
| definite bulk and edge channel charges | lets the current proof subtract channel eigenvalues | the projective measurements themselves return `q_-` and `q_+`; their common finite-window offset cancels | removed completely |

The TPM theorem adds three explicit items absent from the current statement:
D26(INT) for the physical on-site circle charge, the two-measurement protocol
(E.4), and the local-relaxation clauses `(E-LR2)--(E-LR3)` (with the common
sequence supplied by **LR1-GEN**).  These are measurement/limit hypotheses,
not disguised scattering hypotheses.

This is an improvement in **channel independence**, but no unproved logical
implication `(H-AD-edge)⇒(E-LR)` or `(E-LR)⇒(H-AD-edge)` is asserted.  The new
conclusion also has a different honest scope:

| current conclusion | channel-free TPM conclusion |
|---|---|
| per-channel operator bookkeeping (6.1) | operational two-readout history law and its dephased first-moment ledger (E.8) |
| integral fixed-system channel differences | every measured memory outcome is in `ℤ` |
| AKLT edge-doublet support contained in `{-1,0,+1}` after restricting the channel edge multiplet | support contained in `ℤ`; no finite support bound without an additional edge-subspace confinement hypothesis |
| expectations are convex combinations and need not be integers | `Σ_mmr(m)` is an arbitrary probability average and need not be an integer |
| topology protects module/capacity, not amplitude | unchanged |

### ⟨1⟩6. THEOREM (dependency improvement)

**ASSUME.**  `(H-SPT-TPM)`.

**PROVE.**  The quantized outcome and ordered-law conclusions of ⟨1⟩1 and
⟨1⟩4 hold without `(H-split)`, `(H-AD-edge)`, charge conservation, definite
channel charges, or `(H-dress)`.

**⟨2⟩1.**  Finite-time outcome support uses only (T1)--(T3).

*Justification.*  The exhaustive leaves ⟨1⟩1.⟨2⟩1--⟨2⟩6 cite only
D19--D20, D26, automorphic spectrum invariance, and live claim
**M-INDEX-fin**.

**⟨2⟩2.**  The ordered-law conclusion adds only `(E-LR1)--(E-LR3)`.

*Justification.*  The exhaustive leaves ⟨1⟩4.⟨2⟩1--⟨2⟩5 cite only
**LR1-GEN**, **M-INDEX-fin**, **M-INDEX-spec**, and the clauses explicitly
displayed in (T4).

**⟨2⟩3.**  None of the five excluded hypotheses can be hidden in a cited
donor claim.

*Justification.*  The adjudicated scope of **M-INDEX-fin** expressly uses
finite-window offset cancellation; **M-INDEX-spec** expressly assumes D27
and states that H-AD-G is needed only for its separate channel reduction;
**LR1-GEN** expressly consumes no scattering or completeness input.  These
are the live rows in `claims/CLAIMS.md`.

**⟨2⟩4. QED.**

### ⟨1⟩7. COROLLARY (SPT meaning, kept separate from arithmetic)

**ASSUME.**  The hypotheses of ⟨1⟩4 and, additionally, D21(H-split) and the
live PROVED claim **SPT-E'** for the same tensor, full group, and circle.

**PROVE.**  The protocol lives at a physical boundary supporting the
`ω_C`-projective edge module and its measured memory outcomes remain integral;
nontrivial `[ω_C]` protects memory capacity but does not force a nonzero
outcome or transition amplitude.

**⟨2⟩1.**  The registered endpoint module is `ω_C`-projective, has irreducible
dimension at least `d_ω`, and its centered charge spectrum lies in
`q_{ω,C}^∘+ℤ`.

*Justification.*  D21 and live PROVED claim **SPT-E'**.

**⟨2⟩2.**  Under `(H-split)` the registered endpoint has the stated physical
half-chain interpretation.

*Justification.*  D21(H-split) and **SPT-E'**.  No equality between the full
TPM law and the spectral law of D22's channel operator is inferred.

**⟨2⟩3.**  The actual boundary-window memory outcomes are integral.

*Justification.*  ⟨1⟩4; this conclusion was proved independently of
`[ω_C]`, `(H-split)`, and the shifted absolute edge offset.  The SPT-specific
content is protected capacity/selection structure, not the bare arithmetic.

**⟨2⟩4.**  Neither a nonzero atom away from `m=0` nor permanence follows.

*Justification.*  D22's protected-memory terminology and the live
**SPT-M'-dyn** CONJECTURE; the latter still lacks its dynamical scattering and
nonvanishing proof.

**⟨2⟩5. QED.**

---

## 4. Honest claim text proposed for merge

> **`SPT-M'` (replacement).**  Select the D19 boundary windows
> `f_L^{edge}=1_[0,L-1]` and D20 Hermitian normal-ordered charge
> `Q_L^∂=Q^H[f_L^{edge};ξ]`.  Under D26(INT), strongly continuous
> half-chain automorphic dynamics, and a unit preparation, the explicit TPM
> protocol measuring this same `Q_L^∂` at both times has memory change
> `m=q_+-q_-∈ℤ` at every finite `L`, without commutativity of the two
> Heisenberg observables.  Under additionally `(E-LR2)--(E-LR3)`, with the
> common sequence supplied by LR1-GEN, every ordered limit-point law is a
> probability on `ℤ` and obeys
> `Σ_m m r(m)=lim_j[ω^+_{L_j}(Q_{L_j}^∂)-ω^-_{L_j}(Q_{L_j}^∂)]` along its
> subsequence.  D21(H-split)+SPT-E' add the physical projective-edge/capacity
> interpretation only.  No H-AD-edge, wave operator, channel inventory,
> definite channel charge, nonzero amplitude, or permanence is assumed or
> proved; charge conservation is needed only to interpret the mean as current
> flow.  The finite theorem is `SPT-M'-TPM-fin`; the ordered conditional
> theorem is `SPT-M'-TPM-spec`.

**Status proposed for the live row:** `SKETCH`, the allowed live-DAG label.
The lane proof classification is PROVED-candidate pending the capped L6
review.  This does not downgrade the already PROVED old channel implication;
PATCH.md retains that implication as an optional `SPT-M'-ch` corollary instead
of silently deleting it.

---

## 5. Fences

- The TPM support theorem is generic circle-charge arithmetic; it does not by
  itself diagnose an SPT phase.  D21/SPT-E' carry the SPT content.
- `(E-LR2)` and `(E-LR3)` are assumed, not derived, and no nonzero model
  instance is supplied here.
- A projective measurement history is not the spectral measure of
  `Q_L^∂(t_+)-Q_L^∂(t_-)`.
- The ordered mean is generally not integer even though every outcome is.
- The support is `ℤ`, not `{-1,0,+1}`, unless an additional invariant
  edge-doublet confinement theorem is supplied.
- `SPT-M'-dyn` remains CONJECTURE.  This shard neither constructs wave
  operators nor proves an edge-changing reflection amplitude.

## 6. Status

`SPT-M'-TPM-fin`: **PROVED-candidate** by ⟨1⟩1.

`SPT-M'-TPM-spec`: **PROVED-candidate as the displayed conditional
implication** by ⟨1⟩3--⟨1⟩4.  Promotion awaits the capped review; absent a
verified `(E-LR2)--(E-LR3)` model instance, the theorem is useful as a
channel-free protocol theorem rather than an AKLT dynamical result.
