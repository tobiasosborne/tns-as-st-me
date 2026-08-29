<!-- ROLE: blitz-lane proposer shard for the compact-G memory scope theorem.
     No repository definition or status row is edited here. -->

# Compact-`G` memory scope: central weights, circlewise calibration, and Weyl pairs

## 0. Status and exact register

**Proposer status:** **PROVED-candidate**, awaiting the capped L6 critic pass;
the handoff status is recorded in `SUMMARY.md`.  The finite joint-torus statement below is unconditional on
the displayed finite hypotheses.  Its ordered asymptotic extension is
conditional on the joint-PVM version of D27; this shard neither derives D27 nor
claims that H-AD-G implies it.  As in M-INDEX-spec, the asymptotic mean
displacement is not itself quantized: the TPM outcome is.

Let `G` be a compact on-site symmetry as in D2, fix a vacuum `α`, and write
`H_α` and `𝔥_α` as in D2/D11.  For the local proof only, abbreviate the real
vacuum-density functional by

\[
 d_α(ξ):=\omega_α(-i q(ξ)),\qquad ξ\in\mathfrak h_α,
\tag{SG.1}
\]

where `q` is D10's anti-Hermitian differential.  This is only an abbreviation
for existing D2/D10 objects, not a new definition in the L4 register.

The intrinsic lattice used below is the already-recorded effective-central
character lattice of S-IDX-G-label,

\[
 \Lambda_α^*=\operatorname{Hom}(Z_{α,\mathrm{eff}},U(1)),\qquad
 Z_{α,\mathrm{eff}}=Z(H_α)/K_u .                           \tag{SG.2}
\]

Choosing `r` primitive cocharacters of its connected torus writes the free
part of `Λ_α^*` as `ℤ^r`.  No basis-independent assertion is attached to this
coordinate choice.

## 1. New lemma: the vacuum density has central support

### ⟨1⟩1. LEMMA SG-CENTRE (zero density on semisimple directions)

**ASSUME.**  D2(a) for the compact unbroken subgroup `H_α`, and D10's
differential `q`.

**PROVE.**  The map `ξ↦ω_α(q(ξ))` is `Ad(H_α)`-invariant and annihilates
`[𝔥_α,𝔥_α]`.  With an `Ad(H_α)`-invariant inner product, its representing
vector lies in
`𝔥_α^{H_α}=Lie(Z(H_α)^0)`.  In particular every semisimple unbroken direction
has zero vacuum density.

**⟨2⟩1.**  For `h∈H_α`,

`d_α(Ad_hξ)=ω_α(-iu(h)q(ξ)u(h)^†)=d_α(ξ)`.

*Justification.*  D2(a) makes `ω_α` invariant under every `h∈H_α`; the
differentiated on-site representation is D10's `q`.  The same equality for
`ω_α(q(ξ))` differs only by the scalar factor `i`.

**⟨2⟩2.**  Differentiating ⟨2⟩1 at `h=exp(tη)` gives
`d_α([η,ξ])=0`; hence `d_α([𝔥_α,𝔥_α])=0`.

*Justification.*  D2(a), D10, and linearity of the state; the finite
nonabelian realization is independently exercised by named computation
`scope_g_check.py` **SG-C1**.

**⟨2⟩3.**  Compact reductivity gives
`𝔥_α=𝔷(𝔥_α)⊕[𝔥_α,𝔥_α]`.  Under an `Ad(H_α)`-invariant inner product,
⟨2⟩1 makes the vector representing `d_α` fixed by every component of `H_α`,
so it lies in `Lie(Z(H_α)^0)`; ⟨2⟩2 kills the complementary semisimple
summand.

*Justification.*  The compact-group and stabilizer hypotheses are D2(a);
the semisimple/central split and the absence of a central root row are the
scope separation already recorded in claim S-IDX-fin-G.  **⟨2⟩4. QED.**

**Consequence.**  D13(a)/H-MQG(2) calibrates a wall coordinate only when its
tail-density jump `2s` is nonzero.  SG-CENTRE therefore rules out calibrated
memory on the semisimple part of the common unbroken algebra.  This does not
rule out its distinct root-current identities: those belong to
S-IDX-fin-G, not to the D13 memory register.

*Justification.*  D13(a) contains the factor `(2s)^{-1}` with `s>0` in
H-MQG(2); claim S-IDX-fin-G supplies the separate semisimple root register.

## 2. New corollary: joint-torus TPM, one circle at a time

### ⟨1⟩2. COROLLARY SG-TORUS-TPM

**ASSUME.**

1. D2(a) supplies a vacuum pair `(α,β)` and a common connected torus contained
   in `Z(H_α)^0∩Z(H_β)^0`.  Quotient its on-site scalar kernel exactly as in
   S-IDX-G-label and choose `r` primitive cocharacters of the resulting
   effective torus.  Its free character lattice is thereby written `ℤ^r`.
2. For the corresponding Hermitian on-site generators
   `C_j=-iq(ξ_j)`, `j=1,…,r`, impose D26(INT) separately.  For every
   **active** direction impose H-MQG(2) with
   `ω_α(C_j)=+s_j`, `ω_β(C_j)=-s_j`, `s_j>0`, and use D13(a) with
   `(S^z,s)=(C_j,s_j)`.  Directions with zero density jump are omitted from
   the calibrated list.
3. Fix one window `W=[a,b]`, one cut `c_0∈W`, and use the same window, cut,
   and backgrounds at both TPM times.
4. Only for the ordered asymptotic conclusion, assume H-MQG(1),(3),(4) and
   the following joint-PVM strengthening of D27 on one common sequence: the
   joint TPM laws have the D27(LR1) limits; joint initial dephasing has
   vanishing first-moment defect for every `C_j` as in D27(LR2); and the
   laws are first-moment tight with `|ν|` replaced by `‖ν‖_1` as in
   D27(LR3).  The optional full-sequence weak convergence has exactly D27's
   convenience role.

**PROVE.**  At finite times the joint TPM escaped-charge vector is supported
on the effective central weight lattice, hence on `ℤ^r` in the chosen
primitive-circle coordinates.  Under item 4, every ordered subsequential
limit is a probability `p` on that lattice and, componentwise,

\[
 \delta x_j=-{1\over 2s_j}\sum_{\nu\in\mathbb Z^r}\nu_jp(\nu),
 \qquad j=1,\ldots,r .                                     \tag{SG.3}
\]

Thus an individual calibrated history outcome is
`(-ν_1/(2s_1),…, -ν_r/(2s_r))`; `δx_j` is its mean and need not lie on that
lattice.  No single scalar wall displacement is inferred unless the event
separately makes these component values compatible.

#### Finite-window proof

**⟨2⟩1.**  The `C_j` commute on one site, so all finite-window charges

\[
 \widehat Q^{(j)}_{W,c_0}
 :=2s_j(\mathfrak X_W^{(j)}-c_0)
 =\sum_{x=a}^b C_{j,x}+s_j(a+b-1-2c_0)\mathbb 1           \tag{SG.4}
\]

commute and have a joint spectral resolution.  Their common Heisenberg
translates also commute at each fixed time.

*Justification.*  The generators belong to one abelian torus in D2(a), so
their differentials commute; (SG.4) is M-quant-G (G.3), equivalently D13(a),
applied separately under H-MQG(2).  Automorphisms preserve commutators by
H-MQG(3).

**⟨2⟩2.**  The joint on-site spectral labels form an affine torsor over the
effective central character lattice; evaluation on the chosen primitive
cocharacters puts every difference in `ℤ^r`.  Summing over `W` and adding
the scalar terms in (SG.4) changes only the common affine offset.

*Justification.*  Claim S-IDX-G-label gives the effective-center quotient,
the affine character torsor, and integral evaluation on each cocharacter;
D26 and claim M-INDEX-fin give the same one-circle affine-coset arithmetic.

**⟨2⟩3.**  Let `E_{W,t}` be the joint spectral resolution.  In the joint TPM
law, every nonzero atom has the form

\[
 \bigl\|E_{W,t_+}(\{\lambda-\nu\})
            E_{W,t_-}(\{\lambda\})\Psi\bigr\|^2,
 \qquad \nu\in\mathbb Z^r                                  \tag{SG.5}
\]

The affine offset cancels because both measurements use the same data.
Neither (SG.5) nor its normalization requires commutation between the two
times.

*Justification.*  This is the joint spectral version of claim M-INDEX-fin
and `memory-index.md` ⟨1⟩5; simultaneous on-site and same-time commutation,
affine cancellation, and noncommuting cross-time TPM normalization are
exercised by named computation `scope_g_check.py` **SG-C2**.

**⟨2⟩4.**  Therefore the finite joint outcome vector lies in the effective
central weight lattice, or in `ℤ^r` after the chosen cocharacter basis.

*Justification.*  ⟨2⟩2--⟨2⟩3, claim S-IDX-G-label, and claim M-INDEX-fin.
**⟨2⟩5. QED.**

#### Ordered-limit proof

**⟨2⟩6.**  For the joint initial dephasing map, the `j`th first moment of
(SG.5) is the initial expectation of `Q̂^{(j)}` minus the jointly dephased
final expectation of `Q̂^{(j)}`.

*Justification.*  The spectral-expansion computation is exactly
`memory-index.md` ⟨1⟩6 componentwise; item 4 supplies its joint-PVM D27(LR2)
premise.

**⟨2⟩7.**  After the fixed-window common-sequence limit, item 4 removes the
joint dephasing defect and (SG.4) gives

\[
 \sum_\nu\nu_jp_W(\nu)
 =-2s_j\,[\omega_W^+(\mathfrak X_W^{(j)})
                -\omega_W^-(\mathfrak X_W^{(j)})].         \tag{SG.6}
\]

*Justification.*  D27(LR1--LR2), (SG.4), and the scalar proof in claim
M-INDEX-spec (`memory-index.md` ⟨1⟩7.⟨2⟩1--⟨2⟩2).

**⟨2⟩8.**  Vector first-moment tightness yields subsequential probabilities
supported on the closed lattice and passes every component first moment to
the limit.  Taking the padded spatial exhaustion in (SG.6) proves (SG.3).

*Justification.*  Item 4 is D27(LR3) with `‖ν‖_1`, which dominates every
`|ν_j|`; claim M-INDEX-spec supplies the scalar Prokhorov/first-moment step,
and H-MQG(4) fixes the packet and limit order.  **⟨2⟩9. QED.**

**Scope fence.**  Applying scalar D27 separately proves the `r` marginal
statements of M-INDEX-spec, but it does not by itself prove that the finer
joint dephasing defect vanishes.  The finite joint-lattice conclusion needs
no relaxation assumption; the joint ordered law needs item 4.  Under (S) at
both tails, M-IDX-density additionally gives `2s_j∈ℤ` separately for every
antisymmetric active circle, but that density arithmetic is a conclusion,
not an assumption.

*Justification.*  D27 is written for one selected scalar charge; claim
M-INDEX-spec explicitly treats D27 as assumed, while claim M-IDX-density
proves the final circlewise density statement under its antisymmetric-tail
hypotheses.

## 3. The recorded Weyl criterion and the finite-group boundary

### ⟨1⟩3. COROLLARY SG-WEYL-PAIR (conditional source of kink pairs)

**ASSUME.**  Let `n_w` represent an ambient Weyl element normalizing a torus,
let `β=n_w·α≠α`, and let an unbroken central direction `ξ` obey
`Ad_{n_w^{-1}}ξ=-ξ`.  Assume `d_α(ξ)=s>0`.

**PROVE.**  The same circle is unbroken on both tails, its densities are
`(+s,-s)`, and A2 supplies the corresponding fixed kink sector.  Thus this
Weyl-flip criterion supplies an H-MQG(1)--(2) vacuum pair; it does not supply
H-AD-G or D27.

**⟨2⟩1.**  Covariance of the vacuum family gives

\[
 d_β(ξ)=d_α(\operatorname{Ad}_{n_w^{-1}}ξ)=-d_α(ξ)=-s .    \tag{SG.7}
\]

*Justification.*  D2(a) gives
`ω_{g·α}(C_ξ)=ω_α(C_{Ad_{g^{-1}}ξ})`; the exact fixed-point obstruction and
the Weyl-flip realization are already recorded in claim M-quant-G and
`memory-quantization-general.md` §3.

**⟨2⟩2.**  Since `ξ∈Lie Z(H_α)` and `Ad_{n_w^{-1}}ξ=-ξ`, the conjugate
stabilizer `H_β=n_wH_αn_w^{-1}` also contains the same circle; hence it is a
common unbroken direction.

*Justification.*  Stabilizers are D2(a)'s `H_γ`; Weyl conjugation of root and
torus rows is the recorded criterion (H.28) in `soft-index-general.md`, also
summarized by claim S-IDX-fin-G.

**⟨2⟩3.**  For `β≠α`, A2(a,c,d,f) supplies and superselects
`𝒦_{αβ}`.  No channel or relaxation hypothesis follows from this group
construction.

*Justification.*  Claim A2 and D9(a,b); the non-implication to H-AD-G is the
explicit status fence in claim M-quant-G, and the non-implication to D27 is
the explicit fence in claim M-INDEX-spec.  **⟨2⟩4. QED.**

**Existence fence.**  A Weyl element supplies a calibrated pair only on a
direction in its `-1` eigenspace and only when it moves `α` to a distinct
vacuum.  There is no assertion that every compact group, every central
circle, or every Weyl orbit has such an element.  Directions fixed by the
element have equal tail densities and are spectators, as in M-quant-G's
rank-two semidirect-product example.

*Justification.*  Equation (SG.7) and claim M-quant-G; its §3 checker records
one flipped and one fixed circle.

### ⟨1⟩4. COROLLARY SG-NO-CALIBRATION

**ASSUME.**  Either (i) the selected unbroken direction lies in the
semisimple summand of `𝔥_α`, or (ii) the compact on-site symmetry is finite.

**PROVE.**  Case (i) has zero vacuum density and cannot furnish D13(a)'s
nonzero calibration.  Case (ii) has no Lie-algebra circle, D10 current, or
real D13 displacement calibration.  A finite torsion character or string
endpoint may remain, but it is a different observable.

**⟨2⟩1.**  In case (i), `d_α(ξ)=0`, so no positive `s` can satisfy
H-MQG(2) for that direction.

*Justification.*  SG-CENTRE ⟨1⟩1 and D13(a)/H-MQG(2).

**⟨2⟩2.**  In case (ii), `Lie(G)=0`; hence D10 has no nonzero `q(ξ)` or cut
current to integrate and D26 has no circle coordinate to calibrate.

*Justification.*  D10 and D26; claims S-IDX-fin-G and S-IDX-G-label explicitly
record that finite groups have no Lie-current instance, while the latter
allows only a finite torsion label.

**⟨2⟩3.**  Finite strings can instead leave exact endpoint operators, but
that group-valued endpoint statement is not an additive memory law.

*Justification.*  The finite-group exclusion and endpoint replacement are
recorded by `soft-index-g-boundary.md` G5-C2-FINITE and claim S-IDX-G-label.
**⟨2⟩4. QED.**

## 4. Scope theorem

### ⟨1⟩5. THEOREM SG-SCOPE

**ASSUME.**  A compact on-site symmetry `G` and the hypotheses of the relevant
parts above.

**PROVE.**  Every vacuum-density calibration functional factors through the
connected center of the common unbroken subgroup, and its nonzero density
jump descends through the scalar kernel to the connected effective center.
Canonical independent calibrated coordinates may therefore be chosen on that
effective central torus.  Their finite TPM
charge outcome is a weight-lattice element, equivalently an integer vector
after choosing primitive circles, and D13 converts that vector one active
circle at a time to the outcome `-ν_j/(2s_j)`.  Under the joint D27 hypothesis
the ordered law and its component means obey (SG.3).  A Weyl representative
obeying SG-WEYL-PAIR supplies a compatible opposite-density kink pair.
Semisimple unbroken directions and finite groups supply no calibrated memory.

**⟨2⟩1.**  Each tail density is supported on the group center.  A direction
whose on-site action is scalar has the same density in every state, so every
nonzero tail-density jump descends to the effective center.

*Justification.*  SG-CENTRE ⟨1⟩1; D2(a) makes a scalar on-site generator
state-independent, and claim S-IDX-G-label records the scalar-kernel quotient.

**⟨2⟩2.**  The finite and ordered joint outcome statements are respectively
the two conclusions of SG-TORUS-TPM.

*Justification.*  SG-TORUS-TPM ⟨1⟩2, claims M-INDEX-fin and M-INDEX-spec,
and D13/D26/D27.

**⟨2⟩3.**  Compatible flipped pairs and the two exclusions have exactly the
scope stated in the theorem.

*Justification.*  SG-WEYL-PAIR ⟨1⟩3 and SG-NO-CALIBRATION ⟨1⟩4, whose
load-bearing inputs are D2, D9, D10, D13, D26 and claims A2,
S-IDX-fin-G, and S-IDX-G-label.
**⟨2⟩4. QED.**

**Interpretation fence.**  “For any compact `G`” classifies the only possible
location and lattice of a memory effect; it does not assert that every `G`
has an active center, a flipping Weyl element, a kink, scattering channels,
or relaxation.  An ambient semisimple group may still exhibit memory after
breaking to a subgroup with a central circle (for example `SU(2)→U(1)`); what
vanishes is density along the semisimple part of the **unbroken** algebra.

*Justification.*  D2(a), claim M-quant-G's `SU(2)→U(1)` example and
conditionality fence, and SG-CENTRE.

## 5. Checker and red capability

Run:

```text
python3 -O theory/lanes/blitz-2026-08-29/scope-g/scope_g_check.py
python3 -O theory/lanes/blitz-2026-08-29/scope-g/scope_g_check.py --red
```

Named computation **SG-C1** makes 24 deterministic random covariant
`χ=1` MPS tensors and 24 invariant density-tensor samples for nonabelian
`H=U(1)×SU(2)`, all after random basis changes.  The MPS tensors are random
vectors in a fourfold singlet multiplicity inside a representation that also
contains a nontrivial spin-one multiplet; as nonzero `χ=1` tensors they are
injective by construction.  The gate checks their covariance, the central
character, the `su(2)` brackets, state
covariance, `Ad(H)` invariance, zero density on all three semisimple
generators, and a permitted nonzero central density.  The red mutation adds a
highest-weight triplet component to each MPS tensor and also biases the
positive density tensor by `J_z`; covariance breaks and semisimple density is
nonzero.

Named computation **SG-C2** constructs three commuting on-site Cartan charges,
two random same-time joint eigenbases with noncommuting cross-time charge
observables, and the full 625-atom TPM law.  It checks normalization and
affine-offset cancellation into `ℤ^3`.  The red mutation changes the final
background by `√2/10` and the lattice gate fails.  Recorded outputs are
`scope_g_check.out` (exit `0`) and `scope_g_check.red.out` (expected exit `1`).
These finite checks test the algebraic premises and mutation sensitivity; they
do not prove D27, H-AD-G, or existence of a Weyl-flipped vacuum pair.

*Justification.*  Named computations `scope_g_check.py` **SG-C1--SG-C2**;
their scope matches D2/D10 and M-INDEX-fin, not D18 or D27.
