# Verified Ogata map: split SPT index versus charge-history memory

**Status: VERIFIED SOURCE MAP / PARTIAL theorem interface.**  Every external
statement used below is quoted from the local TeX trees in `refs/`.  Line
numbers refer to those checked-in TeX files; section or theorem labels are
also given so the references survive line drift.  The local comparison uses
D21--D22, D26--D27 and the live claim rows cited in §3.

## 1. L3 quote bank and corrected literature ledger

### OGA-SURVEY — arXiv:2110.04671

Scope is finite on-site symmetry in the one-dimensional discussion:

> “we consider on-site finite group symmetry in one and two-dimensional
> quantum spin systems”

Source: `refs/arxiv-2110.04671/main.tex`, lines 1207--1214, §“Quantum spin
systems”.

The split input is exact:

> “Let ωΦ be a unique gapped … ground state … Then ωΦ satisfies the split
> property … πωΦ,R(𝒜R)'' is a type I factor.”

Source: the same file, lines 2270--2285, §“Split property of unique gapped
ground state in 1-d”, Theorem `matsuisplit`.  The survey's definition itself
says that a pure state is split when the relevant half-chain von Neumann
algebra is type I (lines 1368--1388, §“Split property”).

The half-chain projective implementer is also explicit:

> “there is a unitary u_R(g) … Ad(u_R(g))(x)=γ_g(x) … Because γ is a group
> action u_R … is a projective representation.”

Source: the same file, lines 2752--2772, §“H²(G,U(1))-index for SPT with
on-site symmetry”.  Its class is the phase invariant:

> “This second cohomology class hΦ:=h_R∈H²(G,U(1)) is an invariant of ∼β.”

Source: lines 2774--2783, Theorem `h2sta`.  The proof uses symmetry-preserving
left/right automorphisms and quasi-equivalence (lines 2881--2898,
Proposition `facinv`) and concludes that the two right implementers have “the
same second cohomology class” (lines 2959--2965).

The whole-chain/half-chain relation is exact:

> “V_g=u_L(g)⊗u_R(g)” and “σ_L(g,h)σ_R(g,h)=1”.

Source: lines 2813--2829, equation `Vuu` and following display.  Thus the two
half-chain multipliers are inverse, while the whole-chain representation is
genuine.  The relevant spectral-flow automorphism factorises as

> “α_s=inn∘(α_L⊗α_R)”.

Source: lines 2084--2098, §“Automorphic equivalence”, factorisation
proposition.

Finally, the survey's finite-group LSM statements are:

> “If the second cohomology class h of U is non-trivial, then there is no
> translation invariant interaction in 𝒫_{U.G.β}.”

and, for origin reflection,

> “h=2h_1 with some h_1∈H²(G,U(1)).”

Source: lines 3000--3032, §“Lieb-Schultz-Mattis (LSM) type theorems”.

**Verified verdict.**  The round-1 survey attribution is correct after adding
the load-bearing qualifier **finite `G`**.  The survey proves an `H²` class,
not a circle Stone spectrum, a TPM law, or a finite-dimensional physical edge
subspace.

### OGA-INDEX — arXiv:1810.01045

The paper's main theorem is about time reversal, not general on-site symmetry:

> “We introduce a Z₂-index for time reversal invariant Hamiltonians … We show
> this is an invariant of a C¹-classification.”

Source: `refs/arxiv-1810.01045/main.tex`, lines 246--260, abstract.  For pure
split states the exact stability theorem assumes a time-reversal-invariant,
factorisable automorphism (lines 660--700, Definitions `aet`, `adt`, Theorem
`aei`).  For paths it additionally assumes Condition B and concludes

> “the Z₂-index is invariant along the C¹-path of time reversal invariant
> gapped interactions, satisfying the Condition B.”

Source: lines 899--984, Definition `boundary`, Proposition `aep`, Theorem
`c1t`.

General on-site symmetry occurs only in the appendix and is finite:

> “Let G be a finite group … Then there are … a projective unitary
> representation Uφ:G→𝒰(𝒦φ) …”

Source: lines 2751--2805, §“On-site group symmetry”.  The appendix stability
theorem assumes split pure `G`-invariant states and a symmetry-preserving
factorisation (lines 2806--2832); its path theorem says the associated
cohomology class does not change along a Condition-B `G`-invariant path
(lines 2833--2848).

**Verified verdict.**  Round 1 conflated the main time-reversal theorem with
the finite-group appendix.  The combined attribution is available in this
single source, but no compact-Lie/circle theorem is stated here.

### OGA-SPLIT-CLASS — arXiv:1908.08621

The scope and invariant are stated in the abstract:

> “pure split states … invariant under the on-site action τ of a finite group
> G … the second cohomology class c_{ω,R} is the complete invariant”.

Source: `refs/arxiv-1908.08621/main.tex`, lines 216--235, abstract.  The exact
equivalence is narrower than arbitrary product-half automorphic equivalence:
`Ξ_L,Ξ_R` must be asymptotically inner in the fixed-point algebras
(lines 711--735, definitions preceding the main theorem), and

> “ω₀∼_{split,τ}ω₁ if and only if c_{ω₁,R}=c_{ω₀,R}.”

Source: lines 737--747, Theorem `main`.  The source also proves that the
half-chain projective representation decomposes into irreducibles (lines
518--542, Lemma `pd`) and later notes that it contains all relevant
irreducible projective classes (lines 767--770).

**Verified verdict.**  Completeness is correct only for finite `G` and the
paper's specified asymptotically-inner, symmetry-fixed half-chain
equivalence.  It is not completeness for generic gapped Hamiltonian paths.

### OGA-AUTO — arXiv:1906.05479

The exact result is automorphic transport of unique bulk-gapped ground states:

> “Under the Assumption [assump], … φ_s=φ_0∘α_s”.

Source: `refs/arxiv-1906.05479/main.tex`, lines 617--623, Theorem `main`.
The assumptions include a unique ground state, a uniform bulk spectral gap,
and differentiability bounds for sub-exponentially localised expectations
(lines 458--517, Assumption `assump`).  The abstract stresses that no
finite-volume gap is required (lines 283--289).  The paper derives constancy
of the time-reversal and reflection `Z₂` indices by combining its theorem with
other results (lines 624--643).

**Verified verdict.**  Round 1 correctly identified bulk automorphic
equivalence, but this source alone does not state the one-dimensional
left/right factorisation or finite-group `H²` stability theorem and contains
no real-time scattering/TPM conclusion.

### OGA-PARENT — arXiv:1407.3924 and arXiv:1602.08839

Without symmetry, the result is restricted to the FNW parent-Hamiltonian
family:

> “Within this family … the number of edge modes … is the complete invariant.”

Source: `refs/arxiv-1407.3924/main.tex`, lines 80--96, title and abstract.
The main theorem says two members `H∈ℋ_k`, `H'∈ℋ_{k'}` are `C¹`-equivalent iff
`k=k'` (lines 489--525, Theorem `mainclass`).

With local symmetry, the theorem permits a general group `G`, but assumes
unitary equivalence of the entire virtual projective representations:

> “Assume that the projective representations … are unitary equivalent. Then
> H_{Φ_{m,v₀}}≃_{C¹,U,m}H_{Φ_{m,v₁}}.”

Source: `refs/arxiv-1602.08839/main.tex`, lines 546--565, Theorem `thm:gmain`;
the abstract gives the same scope at lines 235--253.  The path is
symmetry-preserving by Definition `def:phasec`, lines 368--390.

**Verified verdict.**  Round 1's short description was directionally right
but hid two important restrictions: both papers concern a special parent
family, and the symmetric theorem is a sufficient path construction from
unitary equivalence of virtual representations, not a general completeness or
phase-invariance theorem.  This second theorem is nevertheless the one local
source that directly supports a compact/general-`G` **parent-model** repair of
OG-MEM-PHASE.

### OGA-LSM — arXiv:2004.06458 and arXiv:1808.08740

The later OTT theorem is stated at the pure-split-state level.  For finite
`G`,

> “let ρ be a pure split state that is G-invariant and translation invariant.
> Then one inevitably has c=0.”

Source: `refs/arxiv-2004.06458/OgataTachikawaTasaki.tex`, lines 844--859,
Theorem `T:trans`.  Reflection gives only the divisibility condition

> “c₀=2c with some c∈𝒞”.

Source: lines 863--879, Theorem `T:ref`.  Unique gapped ground states enter as
examples because short-range unique gapped states are split (lines 776--790).
For compact connected semisimple `G`, the appendix proves the translation
version: the on-site central character of `H=π₁(G)` must be trivial (lines
1322--1342).  For a general compact Lie group the authors give only an
indication (“should be able to attach” the classes; lines 1466--1479).

For `U(1)` the same paper is explicit:

> “Our approach does not say anything nontrivial when G=U(1), since
> H²(U(1),U(1))={0} … [the] filling factor ν mod 1” belongs to a different
> classifying-space formulation.

Source: lines 1481--1496, §“Comment on the case G=U(1)”.

The earlier paper is narrower:

> “Suppose that S is a half-odd-integer. Then a model with a translation and
> time-reversal [respectively Z₂×Z₂] invariant finite range interaction … does
> not have a unique gapped ground state.”

Source: `refs/arxiv-1808.08740/main.tex`, lines 455--463, Theorems `main1`,
`main2`.  Its stronger state-level remark says there is no translation-
invariant pure split state with either symmetry (lines 482--499).

**Verified verdict.**  Round 1 was right that the no-go targets a symmetric,
translation-invariant pure split substrate.  But only arXiv:2004.06458 has the
reflection theorem; arXiv:1808.08740 does not.  Conversely, round 1 understated
arXiv:2004.06458 by omitting its proved compact-connected-semisimple extension
and its explicit separation of projective-class LSM from `U(1)` filling LSM.

### OGA-TYPEIII — arXiv:1301.5737

The paper studies normal-state matching and embeddings in type-III factors:

> “Let M be a factor of type III … Let A be a finite dimensional C*-algebra …
> there exists a unital injective homomorphism π:A→M with φ_i∘π=ρ.”

Source: `refs/arxiv-1301.5737/main.tex`, lines 160--172, Theorem `ma`.  Its
abstract likewise concerns matching finitely many normal states on a finite
subalgebra by an inner unitary (lines 80--93).

**Verified verdict.**  Round 1 was correct: this is not a split-SPT theorem,
does not turn a type-III half-chain into a type-I split factor, and supplies no
SPT index, edge module, or memory law.

## 2. Explicit discrepancy register against round 1

1. `UNVERIFIED-NEEDS-FETCH` is obsolete for all nine sources; `refs/LEDGER.md`
   batch 5 title-verifies all of them.
2. The general on-site `H²` statements in arXiv:2110.04671, 1810.01045, and
   1908.08621 are finite-group statements.  Round 1 left a compact-circle
   extension as an obligation; the checked sources do not discharge it.
3. arXiv:1810.01045 is primarily a time-reversal `Z₂` theorem.  Its general
   on-site result is a finite-group appendix, not the main theorem.
4. The completeness equivalence of arXiv:1908.08621 uses half-chain
   automorphisms asymptotically inner in the fixed-point algebras.  “Product-
   half automorphic equivalence” without this qualifier was too broad.
5. arXiv:1906.05479 proves automorphic transport under its bulk-gap and
   smoothness assumptions.  The one-dimensional factorisation and `H²`
   comparison come from the survey/earlier index result, not that theorem by
   itself.
6. arXiv:1602.08839 allows a general group, but gives a parent-model path when
   the full finite-dimensional virtual projective representations are
   unitarily equivalent.  It is neither generic phase stability nor
   completeness from equality of cohomology classes.
7. arXiv:1808.08740 contains translation no-go theorems only.  The reflection
   statement belongs to arXiv:2004.06458.
8. arXiv:2004.06458 proves more than round 1 recorded for compact connected
   semisimple groups, but explicitly says its projective-class method is
   trivial for `U(1)`; filling is a different LSM datum.
9. Since round 1, **M-INDEX-LA-folium is PROVED** for the fixed bare A2 kink:
   `theory/folium-implementer.md` lines 305--343 constructs the circle
   implementer and its integer-coset Stone spectrum.  This is a whole-kink
   folium theorem, not Ogata's invariant-state half-chain implementer.
10. Since round 1, **SPT-M' is a channel-free TPM theorem**: D22 and claim
    SPT-M' no longer require H-AD-edge for finite integer outcomes.  H-AD-edge
    remains only in optional claim SPT-M'-ch for a channel ledger/nonzero-
    scattering interpretation.

## 3. Corrected claim-by-claim correspondence

| local object / claim | verified nearest literature object | corrected relation | verdict |
|---|---|---|---|
| D26(INT) | On-site action before cutting the chain | D26 fixes a microscopic one-site circle coset.  OGA-SURVEY instead starts from a finite-group action and obtains a half-chain multiplier after split.  OTT explicitly says its projective-class method is trivial for `U(1)` (§1, OGA-LSM). | **Different data.** |
| M-INDEX-fin | None | Its finite-window spectrum and same-window TPM offset cancellation use D26 and automorphic spectral invariance only.  None of the quoted Ogata theorems is needed. | **Independent.** |
| M-INDEX-spec | None | Its conclusion is a probability law on `ℤ` under D27(LR1--LR3).  OGA-AUTO transports ground states in the path parameter; it says nothing about D27's long-time excited-state TPM protocol. | **Neither corollary nor equivalent.** |
| M-INDEX-LA-folium | Whole-GNS implementation for an invariant state; half-chain implementation for a split invariant ground state | The survey's elementary GNS theorem requires state invariance (`main.tex` 586--613).  The proved local row instead treats a fixed bare A2 kink whose circle orbit stays in one folium and constructs a whole-kink implementer.  It yields an integer-coset Stone spectrum but no half-chain `H²` class. | **Now PROVED locally, but not by Ogata stability.** |
| M-INDEX-LA-strong | No analogue | Neither spatial implementation nor split factorisation says that bare window-charge operators converge strongly/resolvently.  The local refutation therefore survives unchanged. | **Still REFUTED.** |
| M-IDX-density | Original `U(1)` filling LSM, not OTT's projective-class theorem | Local `2ρ∈ℤ` follows from two antisymmetric covariant MPS tails plus D26.  OTT says its `H²(G,U(1))` method is trivial for `G=U(1)` and distinguishes the filling invariant (§1). | **LSM-flavoured arithmetic, not an OTT consequence.** |
| SPT-E' | OGA-SURVEY/OGA-INDEX right half-chain projective implementer | Both carry a projective action and cohomology class.  D21(H-split) is still required to embed the finite registered `E_C` module into a physical half-chain edge.  Ogata's half-chain Hilbert space is not identified with the finite MPS register by the quoted theorem. | **Same class-shaped datum under H-split; no unconditional equality of modules.** |
| SPT-T', SPT-D' | Projective multiplication of `u_R` and inverse left multiplier | The verified formulas `u_L⊗u_R=V` and `σ_Lσ_R=1` match the registered endpoint multiplication/cancellation.  Physical endpoint observables still require D21--D22's H-split/H-dress. | **Same algebra, different observable packaging.** |
| SPT-M' | No Ogata memory theorem | D26 gives its finite TPM integer support; D22(E-LR2--E-LR3) gives its conditional ordered law.  Ogata adds only the physical projective-edge/capacity interpretation under H-split. | **Arithmetic independent; topology interpretive.** |
| SPT-M'-ch / SPT-M'-dyn | No analogue | Ogata stability supplies no H-AD-edge, wave operators, channel inventory, charge transfer amplitude, or nonvanishing. | **Strict dynamical extension / still open where marked.** |
| SPT-B-mult / SPT-B' | Whole-chain genuine action and phase invariant | The inverse half multipliers explain exact whole-chain cancellation.  Constancy of the class does not make arbitrary normalised soft coefficients topological; SPT-B' correctly requires a separate local-constancy result. | **Consistent, not equivalent.** |
| A-INDEX-TC-fin / A-INDEX-PEPS | None in these one-dimensional sources | The local rows concern two-dimensional annular/ribbon/categorical registers. | **Outside scope.** |

The round-1 local separation witness remains valid and needs no literature
premise: in the spin-one AKLT register D26 has microscopic `κ=0`, while claim
SPT-E-AKLT gives edge eigenvalues `±1/2`; claim M-INDEX-fin nevertheless gives
integer same-window TPM differences by offset cancellation.  Thus the
microscopic/window index and the SPT edge offset cannot be the same datum.

## 4. Structured correspondence conclusion

**ASSUME.**  D21--D22 and D26--D27; live claims M-INDEX-fin,
M-INDEX-spec, M-INDEX-LA-folium, M-INDEX-LA-strong, M-IDX-density,
SPT-B-mult, SPT-B', SPT-E', SPT-T', SPT-D', SPT-M', SPT-M'-ch, and
SPT-M'-dyn; and only the local-TeX quotations in §1.

**PROVE.**  Ogata's split index can protect the projective edge class but does
not supply the charge-history law or D27 relaxation.

**⟨1⟩1.**  In the verified finite-group setting, a unique gapped invariant
ground state is split, the right half-chain symmetry is implemented
projectively, and its cohomology class is invariant under the stated symmetric
gapped equivalence.

*Justification.*  OGA-SURVEY quotations in §1 (`matsuisplit`, the `u_R`
construction, and Theorem `h2sta`); D21; claim SPT-E'.

**⟨1⟩2.**  The whole-chain action is genuine because the left and right
multipliers cancel.

*Justification.*  OGA-SURVEY equation `Vuu` and `σ_Lσ_R=1` quoted in §1;
claims SPT-B-mult, SPT-T', SPT-D'.

**⟨1⟩3.**  The finite charge-history increment is integral without any split
state, gap, cohomology class, or half-chain implementer.

*Justification.*  D26; claims M-INDEX-fin and SPT-M'.

**⟨1⟩4.**  The ordered limiting law additionally needs first-moment
nondemolition and first-moment tightness.  None is among the hypotheses or
conclusions of the quoted phase-equivalence statements.

*Justification.*  D27(LR2)--(LR3); claims M-INDEX-spec and SPT-M';
OGA-AUTO Theorem `main` quoted in §1.

**⟨1⟩5.**  The newly proved fixed-kink folium implementer gives a distinct
operator-level integer-coset statement, but neither constructs the D27 TPM
limits nor identifies its Stone generator with the half-chain `u_R` generator
or with a strong limit of window charges.

*Justification.*  claim M-INDEX-LA-folium; REFUTED claim
M-INDEX-LA-strong; D27.

**⟨1⟩6. QED.**  The only licensed bridge is: under D21(H-split), Ogata's
projective half-chain class supplies the physical meaning and protected
capacity of the registered SPT edge module.  Finite integer outcomes come
from D26, ordered memory from D22/D27, and dynamical channel transfer from the
additional hypotheses of SPT-M'-ch.
