# OG-MEM-PHASE — verified attack and surviving theorem

**HONEST STATUS: PARTIAL.**  The round-1 statement is not proved at its full
compact-group scope.  A precise finite-detector-plus-circle version is a
Lamport PROVED-candidate below.  The missing general lemma is named in §4.

## 0. Exact target and imported objects

The round-1 target mixed three logically independent structures:

1. a symmetric gapped path and an Ogata half-chain cohomology class;
2. D21's finite registered endpoint module and circle charge;
3. a memory protocol, formerly expressed through D22(H-AD-edge).

After the proved `theory/spt-tpm.md` result, item 3 must be split again:
finite TPM integrality is claim **SPT-M'** and uses D19--D20 and D26, while the
channel ledger is the optional claim **SPT-M'-ch** and still uses D22's
H-AD-edge hypotheses.  The path result must also be split: the checked
general `H²` stability theorem is for a finite on-site group, whereas D21's
circle belongs to a compact group.

## 1. Precise surviving statement `OG-MEM-PHASE-FT`

**ASSUME.**

1. `s∈[0,1]↦Φ_s` is a one-dimensional symmetric uniformly gapped path in the
   precise equivalence class `∼_β` of
   `refs/arxiv-2110.04671/main.tex` lines 1265--1360.  Each `Φ_s` has a unique
   invariant ground state `ω_s`; hence it is pure and split.
2. A finite subgroup `F` of the preserved on-site symmetry acts at every
   path point.  Write `[ω_F(s)]∈H²(F,U(1))` for the right-half-chain Ogata
   class.  The factorised automorphic equivalence is `F`-equivariant exactly
   as in the survey's Proposition `facinv`, quoted in
   `ogata-map-verified.md` §1.
3. At every `s`, D21 supplies a registered endpoint module `E_s` and
   D21(H-split) identifies its restricted `F`-action with the physical
   half-chain action.  Put
   `d_F(s):=min{dim R:R is an [ω_F(s)]-projective F-irrep}`.
4. The same systems preserve a selected circle `T`; D26(INT) holds for its
   Hermitian one-site charge.  Whenever the registered circle edge charge is
   mentioned, D21's full-group/circle normalization holds.  Whenever a
   boundary charge-history protocol is mentioned, use the D19 boundary
   windows, D20 Hermitian normal-ordered charge, and the explicit D22 TPM law.
5. An ordered limiting boundary-memory law is asserted only when
   D22(E-LR2)--(E-LR3) hold; its common sequence is supplied by claim
   **LR1-GEN**.  A channel ledger is asserted only under the separate
   hypotheses of claim **SPT-M'-ch**.

**PROVE.**

(a) `[ω_F(s)]` and therefore the capacity floor `d_F(s)` are constant in `s`,
and `dim E_s≥d_F(0)` at every path point;

(b) at every fixed `s`, differences of two registered edge-charge
eigenvalues are integers, and every finite boundary-window TPM memory outcome
`m=q_+−q_-` is in `ℤ`;

(c) under ASSUME 5, every ordered limit-point boundary TPM law is supported on
`ℤ`; under the additional channel hypotheses,
`ΔQ_edge=−(Q_bulk,out−Q_bulk,in)` and the fixed-system channel differences are
integral;

(d) no constancy is asserted for the actual dimension of `E_s`, the centered
absolute offset, a TPM probability or mean, a transition amplitude, a
nonzero outcome, or D27 relaxation.

## 2. Lamport proof

**⟨1⟩1.**  The finite-subgroup half-chain class is constant:
`[ω_F(s)]=[ω_F(0)]` for every `s`.

*Justification.*  ASSUME 1--2 and the locally quoted OGA-SURVEY Theorem
`h2sta`: `refs/arxiv-2110.04671/main.tex` lines 2780--2783; its
factorisation input is Proposition `facinv`, lines 2886--2898.  D21 fixes the
local class name used here.

**⟨1⟩2.**  `d_F(s)=d_F(0)`.

*Justification.*  `d_F(s)` is a function only of the cohomology class in
ASSUME 3; apply ⟨1⟩1.  This is D21's `d_ω` construction restricted to `F`.

**⟨1⟩3.**  `dim E_s≥d_F(0)` at every path point.

*Justification.*  D21 says the registered module carries the relevant
projective action and defines `d_ω` as the minimal projective-irrep dimension;
live claim **SPT-E'** gives the irreducible-dimension lower bound.  ASSUME 3
and ⟨1⟩2 identify the physical half-chain `F` class and make the floor
path-independent.

**⟨1⟩4.**  At a fixed `s`, any two eigenvalues of the registered circle edge
charge differ by an integer.

*Justification.*  D21 places `spec Q_edge(s)` in one coset
`q^∘_{ω,E_s}+ℤ`; subtracting two values in the same coset eliminates the
offset.  Live claim **SPT-E'** states the same fixed-tensor congruence and
explicitly refuses deformation constancy of the offset.

**⟨1⟩5.**  At a fixed `s`, every finite boundary-window TPM outcome is an
integer without H-split, H-AD-edge, a channel inventory, or a cohomology
class.

*Justification.*  D19--D20 and D26; live claim **SPT-M'** (finite clause).
The two measurements use the same finite-window offset, which cancels.

**⟨1⟩6.**  Under D22(E-LR2)--(E-LR3), every ordered limit-point law is a
probability on `ℤ` with the first moment stated in SPT-M'.

*Justification.*  D22(E-LR), claim **LR1-GEN**, and live claim **SPT-M'**
(conditional ordered clause).  None of these inputs is supplied by ⟨1⟩1.

**⟨1⟩7.**  Under the optional asymptotic channel hypotheses, charge
conservation gives the displayed channel ledger and fixed-system integral
differences.

*Justification.*  D22(H-AD-edge) and live claim **SPT-M'-ch**.  Protection
does not force a nonzero matrix element by D22 and claim **SPT-M'-dyn**.

**⟨1⟩8.**  The proof gives no cross-path identification of the offsets,
probabilities, means, or amplitudes.

*Justification.*  ⟨1⟩1 preserves only the finite-group cohomology class;
D21 and claim **SPT-E'** explicitly make the charge congruence fixed-system;
D22 and claims **SPT-M'**, **SPT-M'-ch**, **SPT-M'-dyn** separate arithmetic,
conditional channel bookkeeping, and nonvanishing dynamics.

**⟨1⟩9. QED.**  Clauses (a)--(d) follow from ⟨1⟩1--⟨1⟩8.

## 3. What the proved folium implementer changes

### ⟨1⟩10. COROLLARY/FENCE (one fixed bare A2 kink)

**ASSUME.**  The exact hypotheses of claim **M-INDEX-LA-folium**: the fixed
bare A2/D1(e′) kink, a common-unbroken selected circle satisfying D2(e)(S) at
both tails, and D26(INT).

**PROVE.**  The kink GNS representation has a strongly continuous circle
implementer with integer-coset Stone spectrum, but this removes no hypothesis
from the phase or ordered-memory parts of `OG-MEM-PHASE-FT`.

**⟨2⟩1.**  There is `U(θ)=e^{iθQ̂}` with
`spec Q̂⊂q_0+ℤ`.

*Justification.*  Live claim **M-INDEX-LA-folium**; its proof is
`theory/folium-implementer.md` ⟨1⟩6, lines 305--343, using D1, D2, D26 and A2.

**⟨2⟩2.**  This gives a genuine operator-level fixed-kink integer-coset
statement independently of D21(H-split).

*Justification.*  Claim **M-INDEX-LA-folium** constructs the implementer from
folium equivalence of the rotated junction, not from the half-chain type-I
factor or the registered `E_s` module.

**⟨2⟩3.**  It does not identify `Q̂` with a strong/resolvent limit of the
finite window charges.

*Justification.*  Claim **M-INDEX-LA-strong** remains REFUTED; the explicit
fence is `theory/folium-implementer.md` ⟨1⟩7, lines 347--390.

**⟨2⟩4.**  It supplies neither D22(E-LR2)--(E-LR3) nor constancy in the path
parameter `s`.

*Justification.*  The hypotheses and conclusion of
**M-INDEX-LA-folium** concern one fixed state and one strongly continuous
circle parameter.  D22(E-LR2)--(E-LR3) concern two-time measurement
back-action and first-moment tightness; no such clause occurs in that claim.

**⟨2⟩5. QED.**  The new implementer closes the fixed-kink kinematic existence
question only.  It does not upgrade phase stability into relaxation or
scattering.

## 4. Sharp boundary of the result

The missing lemma for the original all-compact-group wording is:

> **`OG-COMPACT-STAB`.**  Let `K` be a compact (possibly disconnected) on-site
> symmetry group and let a symmetric uniformly gapped path satisfy the bulk
> hypotheses needed for automorphic equivalence.  For the pure split ground
> states, the continuous half-chain homomorphism `K→PU(ℋ_R)` has a
> Mackey--Moore/Borel class in `H²(K,U(1))`; the spectral-flow automorphism has
> a `K`-equivariant left/right factorisation; and that class, including D21's
> class-invariant central character on the universal-cover kernel, is constant
> along the path.

No checked TeX source states this lemma at that scope.  The closest source,
`refs/arxiv-2004.06458/OgataTachikawaTasaki.tex` §“Generalization to compact
Lie groups”, proves the finite-subgroup reduction for compact connected
semisimple groups (lines 1322--1433), but for a general compact Lie group says
only that one “should be able to attach” the classes and that the crucial
lemma goes “mostly unchanged” (lines 1466--1479).  Therefore the original
compact/disconnected candidate cannot be labelled proved.

There are two honest scoped repairs:

1. `OG-MEM-PHASE-FT` above uses a finite symmetry `F` to protect capacity and
   the circle `T` to quantise within-system differences.  It does not assert a
   full compact-group class is stable.
2. In the special parent-Hamiltonian family of arXiv:1602.08839, Theorem
   `thm:gmain` constructs a symmetric `C¹` path when the entire
   finite-dimensional virtual projective representations are unitarily
   equivalent (`main.tex` lines 546--565).  This is stronger input than equal
   cohomology class, but it gives a compact/general-`G` parent-model version
   with a fixed virtual module.  It is not a generic phase theorem.

For compact connected semisimple `K`, a further source-composition is
available: OTT's finite subgroups detect the central character
(`OgataTachikawaTasaki.tex` lines 1408--1433), and restriction of a `K`-
symmetric path to each detector invokes the finite-group stability theorem.
Thus the semisimple central character is constant, subject to the same
path/factorisation hypotheses.  This still does not cover the central-torus
or disconnected compact groups most relevant to a simultaneously active
calibration circle.

## 5. Ruling on D27 hypothesis reduction

### ⟨1⟩11. THEOREM `OG-NO-LR-REDUCTION`

**ASSUME.**  OGA-AUTO at its verified strength, D27, and live claims
**LR1-GEN**, **M-INDEX-spec**, and **SPT-M'**.

**PROVE.**  Ogata/Moon automorphic equivalence removes no D27 hypothesis.
Independently, D27(LR1) is already a local theorem; the substantive D27
assumptions LR2--LR3 remain untouched.

**⟨2⟩1.**  The automorphic-equivalence parameter `s` labels a path of
interactions and ground states, and its conclusion is
`φ_s=φ_0∘α_s`.

*Justification.*  Local TeX quote: `refs/arxiv-1906.05479/main.tex`, Theorem
`main`, lines 617--623; its assumptions are at lines 458--517.  D27 does not
define this parameter.

**⟨2⟩2.**  D27(LR2) is a double-Cesàro first-moment nondemolition condition
for sequential measurements in one fixed excited/kink vector.

*Justification.*  D27(LR2), definitions.md lines 1223--1227; claims
**M-INDEX-spec** and **SPT-M'**.

**⟨2⟩3.**  D27(LR3) is uniform first-moment tightness of the spatial family of
fixed-window TPM laws.

*Justification.*  D27(LR3), definitions.md lines 1228--1234; claims
**M-INDEX-spec** and **SPT-M'**.

**⟨2⟩4.**  Neither observable, measurement protocol, back-action term, nor
uniform first-moment bound of ⟨2⟩2--⟨2⟩3 occurs in the verified OGA-AUTO
hypotheses or conclusion.

*Justification.*  Compare ⟨2⟩1 with D27(LR2)--(LR3).  Claim
**M-INDEX-spec** explicitly treats D27 as assumed, not derived.

**⟨2⟩5.**  D27(LR1) is already available, but not because of automorphic
phase stability.

*Justification.*  Live claim **LR1-GEN** derives the common subsequence from
separability, strong continuity of the physical time automorphism, and finite
fixed-window spectra; it explicitly proves nothing about LR2 or LR3.

**⟨2⟩6. QED.**  The round-1 “no reduction” verdict is **confirmed**, with the
clarification that LR1's restriction has independently disappeared by
LR1-GEN.  Ogata stability buys no additional D27 reduction.

## 6. Ruling on OTT LSM versus calibrated kink memory

### 6.1 Exact theorem overlap

The local TeX theorem is state-level and precise:

> “let ρ be a pure split state that is G-invariant and translation invariant.
> Then one inevitably has c=0.”

Source: `refs/arxiv-2004.06458/OgataTachikawaTasaki.tex`, lines 844--859,
Theorem `T:trans`.  Here `c` is the degree-two class of the **on-site
projective representation per translation cell**, not the half-chain SPT
class and not D26's scalar by itself.  Reflection instead gives `c_0=2c`
(same file, lines 863--879, Theorem `T:ref`).

### ⟨1⟩12. PROPOSITION `OG-LSM-KINK-SCOPE`

**ASSUME.**  A genuine D9 kink `ϱ∈𝒦_{αβ}` with `α≠β`, and the OTT theorems at
the quoted strength.

**PROVE.**  The full kink state is outside both OTT geometric no-go theorems;
the translation theorem can nevertheless constrain either homogeneous tail
separately.

**⟨2⟩1.**  `ϱ` cannot be translation invariant.

*Justification.*  If it were, `ϱ(τ_n(O))` would be independent of `n` for
every local `O`.  D9(a) sends the same expression to `ω_α(O)` as `n→−∞` and
to `ω_β(O)` as `n→+∞`; hence `ω_α=ω_β`, contrary to `α≠β` and D9's distinct
vacuum labels.

**⟨2⟩2.**  Unless every symmetry element fixes both tails, `ϱ` is not invariant
under the full on-site group either.

*Justification.*  D2(a) sends the boundary labels to
`(g·α,g·β)`, and D9(b) makes different label pairs disjoint.  At most the
common stabiliser `H_α∩H_β` acts within the same sector.

**⟨2⟩3.**  Plain reflection exchanges the two asymptotic labels, so a genuine
`αβ` kink is not a reflection-invariant state of the kind assumed in OTT
Theorem `T:ref`.

*Justification.*  D9(a)'s left/right factorised limits are exchanged by
reflection; for `α≠β`, D9(b) separates the resulting `βα` sector.  A combined
reflection/internal transformation would require a separately recast
symmetry theorem and is not the quoted `T:ref` hypothesis.

**⟨2⟩4.**  A homogeneous tail falls under the translation theorem only if,
in addition to D1's purity and translation invariance, it is split and is
invariant under an unbroken subgroup `F≤H_α` (and similarly at `β`).  If its
physical on-site action per chosen cell has nontrivial projective class
`c_F`, no such tail exists.

*Justification.*  D1(d) gives purity and translation invariance; D2 defines
the unbroken group.  Split is retained as a separate load-bearing hypothesis,
for example D21(H-split) or the unique-gapped input of the quoted Matsui
theorem.  OGA-LSM Theorem `T:trans` is quoted above.  This is a tail admission
gate, not a theorem about the inhomogeneous kink.

**⟨2⟩5.**  The class `c_F` in ⟨2⟩4 is not the tail's half-chain SPT class
`[ω_α]`.

*Justification.*  OTT's cut identity is
`σ_R^x=c_x+σ_R^{x+1}`
(`OgataTachikawaTasaki.tex` lines 732--744), so translation invariance forces
the *cell* class `c_x` to vanish while allowing a nontrivial constant
half-chain class.  D2(c) and D21 name the latter.  The AKLT-type possibility
is therefore not excluded.

**⟨2⟩6.**  For the symmetry group literally frozen in D2, the one-site map
`u:G→U(ℂ^d)` is a genuine representation, so its per-cell projective class is
already trivial.  A nontrivial OTT datum arises only after specifying a
physical quotient whose on-site action is represented projectively (or an
equivalent adjoint-action formulation).

*Justification.*  D2(a), definitions.md lines 132--138; compare the OTT
on-site projective datum in the local TeX quote above.  D26's scalar endpoint
of a lifted `2π` path does not by itself select that quotient or determine its
full projective class.

**⟨2⟩7. QED.**  The OTT no-go is disjoint from the full kink protocol but can
exclude a proposed homogeneous tail before the kink is built.

### 6.2 Exact filling ruling

OTT expressly states that its projective-class method gives nothing
nontrivial for `G=U(1)` because its Borel `H²(U(1),U(1))` is trivial, and
separately recalls the nonintegral-filling LSM theorem
(`OgataTachikawaTasaki.tex` lines 1481--1496).  Therefore:

- D26's one-site scalar/coset and the derived claim **M-IDX-density** are not
  OTT's projective class `c`.
- The full D9 kink is not translation invariant, so neither the projective nor
  the filling LSM theorem applies directly to the memory event.
- A translation-invariant, `U(1)`-invariant unique-gapped tail must separately
  pass the usual filling condition once a model-specific filling `ν` is
  identified.  No checked source identifies that `ν` with this corpus's `ρ`
  or `κ`; making that identification without a model would be an overclaim.
- The local result that is available without that identification is stronger
  and cleaner for the registered MPS tails: under D1, D2, D26 and the stated
  antisymmetric common-circle hypotheses, claim **M-IDX-density** gives one-
  tail coset compatibility and `2ρ∈ℤ` for the pair.  H-MQG additionally fixes
  the calibration `s=ρ>0`.

Thus the exact admission rule for calibrated kink memory is: the full kink is
not OTT-forbidden; each pure split translation-invariant tail must have
trivial per-cell projective class for every unbroken OTT symmetry (or use a
larger cell whose summed class cancels), and any `U(1)` filling condition must
be checked independently.  The real TeX imposes **no further restriction on
the calibrated values `ρ`** beyond the local D26/M-IDX-density conditions.

## 7. Claim-row suggestions

1. **`OG-MEM-PHASE-FT` — SKETCH initially.**  Record the exact conditional
   theorem of §§1--2: finite-subgroup class/capacity floor stable; fixed-system
   circle differences and finite TPM outcomes integral; ordered/channel
   conclusions only under their named hypotheses.  The proof here is a
   PROVED-candidate, but a live row should enter at SKETCH pending the capped
   review.
2. **`OG-NO-LR-REDUCTION` — no new row needed.**  This is a dependency-scope
   ruling already expressed by D27, LR1-GEN, M-INDEX-spec and SPT-M'.
3. **`OG-LSM-KINK-SCOPE` — no new row needed.**  It is a literature boundary
   statement: no-go on qualifying tails, no direct no-go on the D9 kink.

No shared repository file is targeted, so no `PATCH.md` is proposed.
