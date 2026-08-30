# O3 — boundary algebras and the campaign: local-source literature audit

*Supersession note: the previous source-blocked record is stale; the four required, title-verified TeX sources are now local and support the full audit below.*

## 0. Source control and bibliographic verification

No network source was used.  The brief's optional extras were dropped.  The
four source records, verified from the title and author commands in the local
TeX rather than from filenames or metadata, are:

| arXiv id | TeX-verified title and authors | main TeX |
|---|---|---|
| `2307.12552` | Corey Jones, Pieter Naaijkens, David Penneys, and Daniel Wallick, *Local topological order and boundary algebras*; appendix by Masaki Izumi | `refs/arxiv-2307.12552/LTO.tex` |
| `2410.21454` | Anupama Bhardwaj, Tristen Brisky, Chian Yeong Chuah, Kyle Kawagoe, Joseph Keslin, David Penneys, and Daniel Wallick, *Superselection sectors for posets of von Neumann algebras* | `refs/arxiv-2410.21454/PosetSuperselectionSectors.tex` |
| `2509.23734` | Yoshiko Ogata, David Pérez-García, and Alberto Ruiz-de-Alarcón, *Haag Duality for 2D Quantum Spin Systems* | `refs/arxiv-2509.23734/haagduality.tex` |
| `2510.23790` | Matthew Corbelli, *On Symmetry-Compatible Superselection Structures for Product States in 2D Quantum Spin Systems* | `refs/arxiv-2510.23790/aPaperFromChapter.tex` |

Source anchors: the first title/authors are literally declared at
`LTO.tex:233`--`:248`; the second at
`PosetSuperselectionSectors.tex:215`--`:216`; the third at
`haagduality.tex:114`--`:117`; and the fourth at
`aPaperFromChapter.tex:104`--`:109`.  For example, the first source says
“`\title{Local topological order and boundary algebras}`” and names Jones,
Naaijkens, Penneys, and Wallick on the following author lines; the other three
title/author blocks likewise exactly match the table.  These are the only
literature sources used in this audit.

## 1. What the four sources prove, precisely

### 1.1 Jones–Naaijkens–Penneys–Wallick (JNPW): projection nets to a boundary net

**Object and hypotheses.**  JNPW starts with a translation-invariant net of
local observable algebras on `Z^ell` and a reverse-isotone family of nonzero
local ground-state projections: “`Lambda subset Delta` implies
`p_Delta <= p_Lambda`” (`LTO.tex:531`--`:536`).  For a region touching an
outer boundary it forms the compressed algebra

`B(Lambda Subset_s Delta) = {x p_Delta : x in p_Lambda A(Lambda) p_Lambda, ...}`

with the displayed commutation/stability condition in
`LTO.tex:547`--`:554`.  Its strong LTO hypothesis consists of four exact
finite-region axioms (`LTO.tex:559`--`:624`):

1. bulk local indistinguishability,
   `p_Delta A(Lambda) p_Delta = C p_Delta` when `Lambda` is surrounded
   (`:561`--`:565`);
2. identification of the boundary-touching compression with the displayed
   `B(Lambda Subset_s Delta)` (`:567`--`:572`);
3. stability/surjectivity when the inner region is enlarged without changing
   the touched boundary (`:574`--`:578`); and
4. injectivity of further compression, explicitly “if
   `x in B(Lambda Subset_s Delta_1)` with `x p_Delta_2=0`, then `x=0`”
   (`:597`--`:603`).

These are axioms on physical local observable algebras and their local
ground-space projectors, not tensor injectivity.  The construction is
dimension-general: from a half-space in `Z^ell` it builds a codimension-one
net on `K = Z^(ell-1)` (`LTO.tex:1168`--`:1184`).  For intervals `I subset K`,
the local algebra is the stable corner `B(I)`, and the inclusions
`B(I) -> B(J)` are the injective maps `x -> x p_(Delta_J)`; their inductive
limit is the boundary quasi-local algebra `B` (`:1197`--`:1214`).

**Theorems.**

- The toric code satisfies all four axioms, with the rough or smooth boundary
  algebra according to the chosen edge (`LTO.tex:1945`--`:1949`).
- Every Levin–Wen string-net model in their stated fusion-category class
  satisfies all four with surrounding constant `s=1`
  (`LTO.tex:2511`--`:2518`).  The introduction summarizes both model results
  as: “The Toric Code and Levin-Wen models satisfy the LTO axioms ... [and]
  the boundary nets are fusion categorical nets over the lattice `Z`”
  (`:280`--`:284`).  Thus the proved nontrivial boundary nets are the
  one-dimensional boundaries of `(2+1)`-dimensional models; the abstract
  construction itself is not restricted to `ell=2`.
- Compression defines a canonical Heisenberg-picture channel
  `E : A_H -> B` by `p_Delta x p_Delta = E(x)p_Delta`
  (`LTO.tex:1172`--`:1193`).  Independence of `Delta` is proved at
  `:1234`--`:1261`, after which the local map extends uniquely to a unital
  completely positive map (`:1264`--`:1279`).  Consequently every boundary
  state `phi_B` gives the bulk-boundary state `phi_B o E`, equal to the
  canonical bulk ground state away from the boundary (`:1297`--`:1314`).
- For Levin–Wen input category `C`, the canonical boundary factor is type
  `II_1` iff every simple object is invertible and type `III` otherwise
  (`LTO.tex:304`--`:307`); correspondingly the bulk cone algebra is type
  `II_infinity` in the pointed case and type `III` otherwise
  (`:309`--`:317`, restated at `:3741`--`:3747`).  Here a cone algebra is the
  weak/strong closure of a cone's quasi-local algebra in the bulk-ground-state
  GNS representation (`:309`--`:310`).
- For the explicitly identified toric-code and Levin–Wen boundary nets,
  `DHR(F) ~= Z(C)` (`LTO.tex:324`--`:333`).  The more general statement that
  every two-dimensional LTO Hamiltonian's bulk order equals the braided DHR
  category of its boundary net is expressly a **conjecture**, not a theorem
  (`:3996`--`:4003`).  Likewise weak algebraic Haag duality is sufficient for
  a canonical DHR braiding and is stable under bounded-spread isomorphism
  (`:3960`--`:3975`), but JNPW says it is not automatic from LTO (`:4001`--`:4002`).

> **Source quotation:** “The Toric Code and Levin-Wen models satisfy the LTO
> axioms ... The boundary nets are fusion categorical nets”
> (`refs/arxiv-2307.12552/LTO.tex:280`--`:284`).

### 1.2 Bhardwaj–Brisky–Chuah–Kawagoe–Keslin–Penneys–Wallick: sector categories from posets

**Object and exact-duality hypotheses.**  A `P`-net is a common separable
Hilbert space `H` and von Neumann algebras `A_p subset B(H)` indexed by a poset
with order-reversing involution, satisfying isotony, Haag duality
`A_(p')=A_p'`, and absorption of every normal separable representation
(`PosetSuperselectionSectors.tex:674`--`:688`; the poset structure is stated
at `:273`--`:284`).  A sector is a compatible family of normal
representations `pi_p` satisfying isotony, locality, and absorption—equivalently
faithfulness under their hypotheses (`:924`--`:939`).  Localization at `p`
means `pi_(p')=id`, so the sector is vacuum-like on the complement
(`:299`--`:300`).

If the poset obeys their geometric axioms, the localized sectors carry a
strict tensor product and unitary braiding
(`PosetSuperselectionSectors.tex:302`--`:309`).  This is an abstract theorem:
Haag duality and absorption are hypotheses on the von Neumann net, not
consequences of locality alone.

**Bounded-spread cone version and stability.**  For the cone poset in `R^2`
they replace equality by a uniform inclusion
`A_(Lambda^c)' subset A_(Lambda^(+s))`, add locality, absorption/proper
infiniteness, and the small-generation axiom
(`PosetSuperselectionSectors.tex:2995`--`:3035`).  Localized bounded-spread
sectors again have tensor product and braiding (`:326`--`:331`).  Two
intertwined nets have isomorphic `W*` sector categories (`:3332`--`:3335`) and,
after localization, a strict unitary braided equivalence
(`:3356`--`:3360`).

**Comparison theorem.**  For a planar spin system they assume a pure reference
state, bounded-spread Haag duality of its cone von Neumann algebras, and
infinite-factor cone algebras (`PosetSuperselectionSectors.tex:3674`--`:3686`).
Their Naaijkens sector is a representation satisfying the displayed local
unitary-equivalence criterion on every cone (`:3689`--`:3696`).  Under those
hypotheses the poset/Gabbiani–Fröhlich category is braided monoidally
equivalent to the Naaijkens category (`:3698`--`:3705`).  This proves
equivalence of two sector formalisms; it does not prove duality for an
arbitrary spin-system state.

> **Source quotation:** “the superselection sectors ... carries a strict
> tensor product and a unitary braiding”
> (`refs/arxiv-2410.21454/PosetSuperselectionSectors.tex:326`--`:331`); the
> Naaijkens comparison is “braided monoidally equivalent” (`:3702`--`:3705`).

### 1.3 Ogata–Pérez-García–Ruiz-de-Alarcón: Haag duality for a tensor-network class

**Object and hypotheses.**  The observable is the usual quasi-local
`C*`-inductive limit of finite matrix algebras on `Z^2`
(`haagduality.tex:193`--`:208`).  For a pure state's GNS representation,
Haag duality is the maximality equality

`pi(A_(Lambda^c))' = pi(A_Lambda)''`

for every cone (`haagduality.tex:238`--`:247`).  Approximate Haag duality
allows a fattened/translated cone and a unitary which is itself approximable
by increasingly well-localized unitaries (`:257`--`:296`).

The proved model class is not arbitrary PEPS: it is the renormalization-fixed-
point, weak-Hopf-injective tensor-network family introduced in the paper's
stated references (`haagduality.tex:172`--`:186`), with the corollaries stated
for **biconnected** `C*`-weak Hopf algebras.  The operator-algebraic reduction
assumes a pure, unique frustration-free state of a positive uniformly bounded
finite-range interaction (`:319`--`:335`, `:582`--`:635`).  Its finite-system
hypothesis uses the local zero-energy projections on a region and its
complement plus explicit approximation maps; if it holds, exact duality
follows (`:645`--`:655`).

**Theorems.**

- For every lattice-adapted cone-like region in their class,
  `pi(A_Gamma)'' = pi(A_(Gamma^c))'`
  (`haagduality.tex:2428`--`:2456`, `:2533`--`:2537`).
- Therefore two-dimensional biconnected `C*`-weak-Hopf tensor-network states
  satisfy approximate Haag duality (`haagduality.tex:2541`--`:2547`), and
  exact Haag duality after grouping disjoint four-site plaquettes into sites
  of a coarse lattice (`:2549`--`:2558`).
- The same models have a commuting parent Hamiltonian whose local ground
  space is precisely the tensor-network space (`haagduality.tex:2200`--`:2203`)
  and satisfy local topological quantum order for rectangular bulk regions
  (`:2212`--`:2222`).  This latter TQO theorem is not, by itself, a verification
  of all four stronger JNPW LTO axioms.

The proof deliberately projects local observable algebras onto inside/outside
zero-energy spaces rather than assuming toric-code string operators; the
authors identify efficient entanglement of those zero-energy spaces as the
sufficient mechanism (`haagduality.tex:188`--`:191`).

> **Source quotation:** “Approximate Haag duality holds for two-dimensional
> biconnected `C*`-weak Hopf algebras tensor network states”
> (`refs/arxiv-2509.23734/haagduality.tex:2541`--`:2543`); on the coarse-grained
> lattice, “Haag duality holds” (`:2554`--`:2558`).

### 1.4 Corbelli: symmetry-compatible sectors of product representations

**Object and hypotheses.**  Corbelli works on a two-dimensional Delone
lattice with finite-dimensional on-site Hilbert spaces and an on-site action
of a **compact abelian** group `G` (`aPaperFromChapter.tex:156`--`:193`,
`:299`).  A `G`-covariant representation carries a strongly continuous
unitary representation implementing the automorphisms (`:224`--`:232`).  The
ordinary selection criterion requires unitary equivalence to a reference
representation on the complement of every cone (`:245`--`:248`); the refined
criterion requires those local identifying unitaries also to intertwine the
global `G` actions (`:252`--`:258`).

The reference representation is a literal tensor product of irreducible
representations on a cone and its complement.  The Naaijkens–Ogata theorem
quoted and specialized in the source says every irreducible sector satisfying
the ordinary criterion is unitarily equivalent to that product reference
(`aPaperFromChapter.tex:998`--`:1004`).

**Theorem.**  With irreducible `G`-covariant factors on the cone and its
complement, each irreducible representation satisfying the `G`-equivariant
criterion has a unique grade `phi in G-hat`; this classifies the refined
sectors up to `G`-equivariant unitary equivalence
(`aPaperFromChapter.tex:1020`--`:1031`).  In particular the statement holds
for the GNS representation of a pure `G`-invariant product state
(`:1062`--`:1073`).  Thus symmetry compatibility can refine an ordinarily
trivial sector set into `G-hat`, exactly as the abstract says
(`:117`--`:119`).  The paper does **not** prove an `H^2(G,U(1))` classification,
a projective endpoint action, broken-vacuum double-coset sectors, or a braided
fusion theorem.

> **Source quotation:** “there exists a unique `phi in G-hat`” and the refined
> sectors “are classified by `G-hat` up to `G`-equivariant unitary
> equivalence”
> (`refs/arxiv-2510.23790/aPaperFromChapter.tex:1020`--`:1031`).

## 2. Operational grounding and the injective-MPS cut

### 2.1 What is operational in the boundary-net school

At its `C*` entry point, JNPW gives almost exactly the operational foundation
requested by the campaign directive.  Its primitives are:

- finite-support spin observables in `A(Lambda)`;
- spectral projections `p_Lambda` onto finite-region zero-energy spaces;
- compression, multiplication, inclusion, and norm completion; and
- states and a ucp map, hence ordinary preparation/measurement probabilities.

The decisive statement is not merely that a virtual tensor carries an edge
index.  It is the physical compression identity
`p_Delta x p_Delta = E(x)p_Delta` for `x in A(Lambda)`
(`LTO.tex:1184`--`:1192`), followed by the proved claim that **every** state of
the resulting boundary algebra extends through `E` to a bulk-boundary state
which agrees with the canonical ground state in the deep bulk
(`LTO.tex:1297`--`:1314`).  The model thus supplies an algebra generated from
things that can, in principle, be measured or imposed as ground-space
constraints, plus an operational channel from bulk observables to boundary
data.  In this strong sense the JNPW construction vindicates the directive
“boundary information must be grounded in observables/implementable
operations, not merely in a representation label.”

There are three qualifications.

1. Exact local ground projections are idealized spectral operations.  In the
   commuting-projector examples they are especially concrete; for a generic
   Hamiltonian, preparing or measuring the exact `p_Lambda` may itself be a
   demanding protocol.  This affects feasibility, not the observable status
   of the object.
2. The inductive-limit boundary algebra is generally an abstract corner, not
   a literal unital subalgebra of the original quasi-local algebra.  JNPW says
   exactly: “`B` is not a unital subalgebra of `A`,” and therefore `E` is only
   conditional-expectation-like (`LTO.tex:1281`--`:1295`).  Its operational
   meaning is fixed by the compatible finite compressions and by the channel,
   not by pretending that every boundary element is a microscopic operator
   with the original unit.
3. Cone von Neumann algebras, GNS closures, absorbing representations, DHR
   correspondences, braidings, and category equivalences are mathematical
   organization of observable response, not themselves laboratory
   observables.  Bhardwaj et al.'s absorption and Haag-duality assumptions
   (`PosetSuperselectionSectors.tex:674`--`:688`) and Corbelli's covariant
   representation labels are therefore scaffolding.  They become operational
   only when tied back to local algebras, state restrictions, intertwiners, or
   a stated instrument.  Ogata–Pérez-García–Ruiz-de-Alarcón makes precisely
   such a tie for duality by deriving the von Neumann equality from finite
   zero-energy projections (`haagduality.tex:582`--`:655`).

So the answer is **yes at the boundary-observable layer, no if one tries to
call all of its representation/category layer directly operational**.

### 2.2 What the campaign's MPS construction actually supplies

The campaign's D1/D4/D9 construction also passes the directive, but in its
carefully scoped register:

- D1 begins with the physical quasi-local spin algebra and physical finite
  window vectors.
- On a window padded by at least the injectivity length on both sides of a
  cut, the map `iota_(Lambda,b): M_chi(C) -> W_(Lambda,b)` from a virtual bond
  insertion to a physical vector is injective (`definitions.md`, D4(a1)--(a2)).
  Thus left multiplication by `M_chi` is a genuine finite-window linear
  operation, not an action on redundant tensor coordinates.
- A1 proves that endpoint **states** satisfy
  `omega^(M@b)=omega^(M'@b)` iff `M'` is a nonzero scalar multiple of `M`.
  Hence the invertible endpoint-state locus is a `PGL(chi)` torsor
  (`theory/corner-a.md`, A1(c)), and the symmetry acts on it through the
  honest homomorphism `rho_alpha:G -> PGL(chi)`.

This operational success should not be overstated.  `E_b^alpha` is a space of
states, not a `C*`-algebra; `PGL(chi)` is its label torsor, not its observable
algebra; and the twisted group algebra `a_alpha` is proved to act on padded
finite-window vectors.  Corner A explicitly leaves **unproved** the normal
GNS realization of every bond-insertion state and an action of `a_alpha` on
the infinite-volume physical Hilbert space (`theory/corner-a.md`,
A1 `⟨2⟩9`).  JNPW's boundary algebra, by contrast, is a full local net of
compressed observables with an inductive limit and all states on it.

### 2.3 Precise bridge: a candidate specialization, not an established equivalence

There is a natural bridge, but neither the four papers nor Corner A proves it.

**[physical argument]** Start from the frustration-free parent Hamiltonian of
an injective MPS and its interval ground-space projections `p_[a,b]`.  Apply
the JNPW compression construction to a half-chain.  If one proves the four
strong LTO axioms for these projections and fixes the remote boundary
environment, MPS injectivity should identify the stable cut corner with the
virtual edge matrix algebra (or the appropriate corner of it).  Under that
identification, a bond insertion `M` is a boundary-module vector/state
preparation, left multiplication is the boundary-algebra action, and A1's
`GL(chi)/C^times = PGL(chi)` is the projectivized invertible orbit in that
module—not the whole boundary `C*`-algebra.

Three proof obligations prevent promotion of this bridge:

1. construct the parent ground-projection net in exactly JNPW's geometry and
   verify LTO1--LTO4, rather than importing ordinary MPS tensor injectivity;
2. compute the resulting stable compressed corner, including which opposite
   edge/environment has been fixed, and prove the claimed matrix-algebra
   identification; and
3. match JNPW boundary states/representations to D1(e)'s bond-insertion states
   and close Corner A's missing GNS-normality step.

Because a one-dimensional bulk has a zero-dimensional boundary, this would be
the `ell=1`, `Z^0` degeneration of JNPW's construction, not a one-dimensional
boundary **net** like the `ell=2` toric-code/Levin–Wen examples.  The correct
classification is therefore:

> **same operational principle; plausible zero-dimensional specialization;
> presently different mathematical objects, with no proved equivalence.**

## 3. DHR/sector comparison with Corner A

### 3.1 Three distinct uses of “sector”

| construction | what is held fixed outside the excitation | label/equivalence | structure actually proved |
|---|---|---|---|
| A1 endpoint state | the same injective MPS vacuum on both tails | `[M] in PGL(chi)` inside `K_(alpha,alpha)` | torsor and projective symmetry action; **not** a new vacuum superselection sector |
| A2 kink | vacuum `alpha` at left infinity and `beta` at right infinity | ordered tail pair `(alpha,beta)`; under transitivity and diagonal `G`, the double coset `H_alpha\G/H_alpha` | disjoint folia and a weak-* sector jump; no fusion/braiding category claimed |
| DHR/Naaijkens/poset sector | equivalence to one reference vacuum on the complement of a localization region | normal representation/intertwiner class, transportable between regions | `W*` category, tensor product and braiding under duality/geometric hypotheses |

The distinction is load-bearing.  Bhardwaj et al. localizes a sector by making
its complementary representation the identity
(`PosetSuperselectionSectors.tex:299`--`:306`), while the Buchholz–Fredenhagen
form is both localized outside a cone and transportable to every cone
(`:3451`--`:3461`).  Their spin-system comparison then assumes local
equivalence to the vacuum representation on every cone
(`:3674`--`:3696`).

A1 does not compete with this: its endpoint states all retain sector label
`(alpha,alpha)`.  A2 is superselection theory in the precise disjoint-folium
sense, but of a different kind.  A kink changes the asymptotic vacuum on one
side, and that change cannot be hidden in a bounded interval relative to a
single vacuum.  **[physical argument]** It should therefore not be identified
with a DHR-localized charge without first changing the reference net or
adopting a solitonic/half-line sector criterion.  None of the four audited
papers proves that translation.  In particular, A2's complete double coset is
global-symmetry orbit bookkeeping for ordered tail vacua; it is not an object
label in the braided category of cone-localized anyons.

The weak-* statement is also extra data rather than a rival classification.
A2 gives an explicit net of normal, finite-string states in the vacuum folium
whose pointwise limit is disjoint and lies in `K_(alpha,g.alpha)`.  The poset
and Naaijkens formalisms organize the resulting inequivalent representations,
but the theorems quoted above do not supply this MPS transfer-matrix limit,
its `lambda-tilde^(y-w)` rate, or the finite-to-infinite sector jump.

### 3.2 The closest overlap: symmetry-compatible equivalence

Corbelli is the closest conceptual antecedent.  It makes both the selection
criterion and inter-sector equivalence commute with an on-site compact
abelian symmetry (`aPaperFromChapter.tex:240`--`:258`).  Ordinary product-state
sector theory is trivial (`:998`--`:1004`), but the symmetry-compatible
version is labelled by `G-hat` (`:1020`--`:1031`).  Hence the general lesson

> symmetry-respecting equivalence can retain charge information which
> ordinary unitary equivalence erases

is already explicit in this literature.

It does not subsume Corner A.  Corbelli's `G-hat` is a character grade of the
unitary identifying an irreducible two-dimensional product representation
with its reference representation.  A1's datum is instead the multiplier
class `[omega_alpha] in H^2(G,U(1))` of an injective-MPS virtual action and the
associated extension problem for the **asymptotic** state action
`rho_alpha:G -> PGL(chi)`.  Correctly stated, `[omega_alpha]` obstructs removal
of the multiplier—an honest unitary lift of `rho_alpha`—and is not in general
a Lie-algebra central charge.  A2 further permits broken vacua, nonabelian
`G`, double cosets, and weak-* folium change.  None of that is in Corbelli's
theorem.

The campaign also adds the proposed connections to soft limits and memory.
No audited source relates a DHR/boundary sector, a `G-hat` grade, or a Haag
duality statement to a lattice soft theorem or a domain-wall memory law.

### 3.3 The folium implementer row

`M-INDEX-LA-folium` asks whether one selected common-unbroken circle acts
spatially and strongly continuously in the GNS representation of one fixed
bare A2 kink, yielding a Stone generator with spectrum in one affine integer
coset.  This is adjacent to, but not supplied by, the sector papers:

- Bhardwaj et al. assumes normal representations of each local von Neumann
  algebra and studies localization/intertwiners; it does not construct the
  global circle implementer in a kink folium.
- Corbelli recalls the standard implementer for the GNS representation of a
  **`G`-invariant** state (`aPaperFromChapter.tex:201`--`:219`) and then assumes
  covariant representations.  The campaign row instead proves spatiality for
  a fixed symmetry-compatible kink folium at its stated scope; it is not a
  product-reference corollary of Corbelli.
- Approximate Haag duality controls localization and phase stability of cone
  sectors, not convergence of bare window charges.  It therefore does not
  undo the campaign's fence that `M-INDEX-LA-folium` is an implementer theorem,
  not a strong-resolvent limit of window-charge operators.

### 3.4 What Corner A should import

Haag duality is the rigorous version of “the region algebra is all there is at
the cut.”  In the spin-system notation it says that locality's automatic
inclusion is saturated:
`pi(A_Lambda)'' = pi(A_(Lambda^c))'`
(`haagduality.tex:238`--`:247`).  Thus every bounded operator invisible to the
complement is already in the region von Neumann algebra.  Bounded-spread or
approximate duality supplies the phase-robust softened version; the poset
theorem then turns it into transportable fusion and braiding.

Corner A should import this as a **missing theorem schema**, not cite it as a
completed MPS proof:

1. form the left/right or half-chain von Neumann algebras in the injective-MPS
   GNS representation;
2. prove the appropriate cut duality (or a precisely stated split/twisted
   variant);
3. identify the resulting cut corner/module with the virtual matrix data; and
4. only then claim exhaustiveness of the boundary algebra and a physical GNS
   action of the charge algebra.

JNPW demonstrates how ground projections can construct the boundary algebra;
Bhardwaj et al. demonstrates what duality buys categorically; and
Ogata–Pérez-García–Ruiz-de-Alarcón demonstrates that duality can be derived
from zero-energy subspaces for a substantial tensor-network class.  But JNPW
warns that even its strong LTO axioms do not automatically give weak
algebraic Haag duality (`LTO.tex:4001`--`:4002`), and the 2025 Haag theorem is
two-dimensional and weak-Hopf/MPO-injective, not the required one-dimensional
injective-MPS cut theorem.  The import is therefore a rigorous target and a
proof strategy, not a closed Corner A gap.

## 4. Operational restatement of the `(2+1)`-dimensional `(PT)` hypotheses

### 4.1 What is wrong with `(PT)` operationally

The current `A-INDEX-PEPS` implication is mathematically clean: PT1 assumes a
tube-algebra representation and its minimal central idempotents; PT2 assumes a
tensor of one pure Drinfeld-center type; PT3 assumes zipper/associator/pulling-
through data realizing fusion; and PT4 supplies an actual Kraus instrument.
The selection proof then projects the assumed fusion decomposition.  The
problem identified by the directive is not the implication.  It is that
PT1--PT3 are mostly representation/tensor typing data.  Until related to
physical finite-region observables and an implementable operation, they do not
say how an experiment prepares `x`, measures `P_a,P_b`, or realizes the
channel `mu`.

PT4 already has the right operational form.  `A-INDEX-TC-fin` also already has
it: the same finite physical boundary PVM is measured twice, and a microscopic
ribbon unitary is inserted between the measurements.  The question is whether
the other three PT clauses can be replaced by physical-algebra hypotheses.

### 4.2 A ground-projection/boundary-net replacement

The following is the strongest honest restatement suggested by the audited
literature.  It is a proposal, not a theorem of the four sources.

**(O-PT1: observable annular register).**  Start with the finite local
observable algebras and local ground projections of a JNPW LTO net.  For each
chosen circle/annulus, take the stable compressed boundary algebra obtained
from `p_Delta A(Lambda) p_Delta`, with the JNPW injective inclusion maps.  Require
its relevant finite-dimensional center to have a complete minimal central PVM
`{P_a}`.  Define sector outcomes by this physical PVM; only afterwards identify
their stable labels with `Irr DHR(B)` or `Irr Z(C)`.

**(O-PT2: physical pure-endpoint instrument).**  Supply a localized CP/Kraus
operation `K_(x,mu)` made from microscopic observables in a disk/ribbon.  A
small enclosing instance of the same central PVM must return `x` with
probability one.  “Pure endpoint” is thereby a repeatable finite measurement
statement, not a declaration about a virtual tensor.

**(O-PT3: observable gluing/fusion).**  Require the stable nested-boundary
correspondence generated by `K_x` to compose with the source sector through
the boundary net's physical inclusion/gluing maps.  Under a proved
identification `DHR(B) ~= Z(C)`, its decomposition must be the Connes/DHR
fusion decomposition

`X_x tensor_B X_a ~= direct-sum_b Hom(b,x tensor a) tensor X_b`.

Equivalently at the finite operational level, every nonzero joint block of the
measured PVM and the supplied operation must lie in an allowed fusion
incidence.  This does not require every allowed block to be nonzero.  The
categorical correspondence is scaffolding; the quantities
`P_b K_(x,mu) P_a` are physical matrix blocks.

**(O-PT4: normalization).**  Keep PT4 unchanged: `{K_(x,mu)}` is a normalized
instrument, or the displayed experiment is explicitly postselected and its
success probability reported.  Neither LTO nor a DHR category fixes Kraus
normalization or probabilities.

Under O-PT1--O-PT4, the current proof becomes operational verbatim:

`P_b K_(x,mu) P_a = 0` unless `mu in Hom(b,x tensor a)`.

The zero is now a block of a physical compressed observable/instrument between
two outcomes of a physical boundary PVM.  **[physical argument]** The value of
the restatement is that a tensor-network calculation may be used to *prove*
O-PT1--O-PT3 for a model, while the theorem's hypotheses and conclusion remain
statements about finite observables, ground-space projections, and CP maps.

### 4.3 What the four sources actually discharge

**JNPW supplies most of O-PT1's architecture.**  Its boundary local algebras
are compressed physical observable algebras; LTO3/LTO4 make their inclusions
stable; and the ucp channel gives all boundary states a bulk-boundary meaning
(`LTO.tex:1197`--`:1230`, `:1264`--`:1314`).  For the toric code and Levin–Wen
models it further proves that the boundary DHR category is `Z(C)`
(`:324`--`:333`).  Thus for those models it supplies the observable boundary
net and the abstract sector/fusion target.

It does **not** by itself supply the chosen annular central PVM, a microscopic
pure-endpoint Kraus map, its multiplicity resolution, or its normalization.
Nor does it prove the general LTO-to-DHR identification: that is the conjecture
at `LTO.tex:3996`--`:4003`, and the required weak Haag duality is not automatic.

**Bhardwaj et al. supplies the categorical robustness of O-PT3 once its
hypotheses hold.**  Bounded-spread Haag duality and small generation yield a
braided sector category, and intertwined nets have braided-equivalent
categories (`PosetSuperselectionSectors.tex:3011`--`:3059`,
`:3329`--`:3360`).  Its equivalence to the Naaijkens construction prevents an
ambiguity of sector formalism.  It still begins with von Neumann net/duality
hypotheses and contains no finite PVM/Kraus protocol.

**Ogata–Pérez-García–Ruiz-de-Alarcón supplies maximality for a broad fixed-
point tensor-network class.**  Exact/approximate Haag duality means no
additional cone observable can commute with the complement while lying
outside the cone algebra.  Their proof uses local zero-energy projections,
and they also prove local TQO (`haagduality.tex:188`--`:191`,
`:2212`--`:2222`, `:2533`--`:2558`).  This is a powerful observable consequence
of the tensor presentation.  But the paper neither verifies JNPW LTO2--LTO4
for the whole weak-Hopf class nor constructs the O-PT2/O-PT4 instrument.

**Corbelli does not discharge `(PT)`.**  Its `G-hat` labels refine global-
symmetry-compatible product sectors, not Drinfeld-center anyons or annular
tube measurements.

### 4.4 Missing theorem package

To replace the current PEPS typing hypotheses rather than merely rename them,
one still needs:

1. a theorem deriving JNPW's four LTO axioms—or an equally strong stable
   annular compression theorem—from the chosen PEPS parent Hamiltonian;
2. a calculation of the stable compressed annular centers and a proof that
   their minimal projections are the desired anyon PVM;
3. Haag or weak algebraic Haag duality for that boundary/cone net, plus the
   identification of its DHR fusion with `Z(C)`;
4. a microscopic, localized, channel-resolved pure-endpoint instrument and a
   proof that its nested-boundary correspondence is the simple object `x`;
5. instrument normalization/postselection; and
6. for momentum limits, existence in the declared topology.  The boundary
   literature preserves sector blocks under appropriate limits; it does not
   construct the campaign's soft limit.

The first three items would operationalize PT1/PT3.  Items 4--5 are the still
load-bearing PT2/PT4 obligations.  The audited sources therefore make an
operational reformulation credible and prove important model pieces, but do
not discharge `A-INDEX-PEPS` as a microscopic general theorem.

### 4.5 Consequences for the live `(2+1)` rows

- **`A-INDEX-TC-fin`: unchanged and already operational.**  JNPW independently
  puts the toric-code boundary in a projection-net/DHR framework, but the
  campaign's finite Pauli proof already supplies the actual PVM, ribbon,
  two-measurement law, and braiding readout.  The literature is a conceptual
  citation, not a missing premise.
- **`A-INDEX-PEPS`: still conditional.**  PT1/PT3 can be replaced by the
  O-PT1/O-PT3 package above for models where the needed boundary-net and DHR
  identifications are proved.  PT2/PT4 and the microscopic model match remain
  open exactly as the live row says.
- **`SHAPE-FLAT`: not implied by LTO or Haag duality alone.**  Bounded-spread
  equivalence preserves a sector category, not equality of two particular
  code-projected path morphisms.  An operational replacement for tensor
  pulling-through would be a ground-space cleaning/flat-transport identity
  `p_Delta T_gamma p_Delta = p_Delta T_(gamma') p_Delta` for each contractible
  local deformation, with coherent endpoint identifications.  That additional
  local-move theorem is still needed; noncontractible braiding remains fenced.
- **`M-INDEX-2D-fin`: orthogonal to this literature.**  It is an additive
  on-site `0`-form charge TPM theorem.  Cone/tube sector categories neither
  strengthen nor threaten its integer spectral arithmetic, and the campaign
  must not infer topological/anyon content from it.

## 5. Novelty and citation audit

### 5.1 What is anticipated, and what is not

**Boundary-algebra operationality is anticipated directly.**  A broad claim
that the campaign is the first to ground a lattice boundary algebra in
physical observables is untenable.  JNPW constructs such a net from local
observable algebras and local ground-state projections, together with a ucp
bulk-to-boundary channel and a parametrization of bulk-boundary states
(`LTO.tex:251`--`:256`, `:1172`--`:1314`).  Ogata–Pérez-García–Ruiz-de-Alarcón
likewise derives a maximal cone-observable algebra from finite zero-energy
spaces for a large fixed-point tensor-network class.  These works should be
presented as the operator-algebraic foundation which the campaign's
operational directive selects, not as something discovered by the campaign.

**Generic sector bookkeeping is also prior art.**  Local equivalence to a
vacuum, transportability, intertwiners, fusion, braiding, bounded-spread
duality, and equivalence between poset and Naaijkens sector categories are the
content of Bhardwaj et al. (`PosetSuperselectionSectors.tex:302`--`:347`,
`:3417`--`:3705`).  JNPW already uses a boundary DHR category to recover
`Z(C)` in the toric code and Levin–Wen cases.  Corbelli further shows that
requiring symmetry-compatible equivalence can turn an ordinarily trivial
product sector theory into a nontrivial `G-hat` classification
(`aPaperFromChapter.tex:998`--`:1031`).  The campaign cannot advertise
“symmetry makes otherwise invisible sectors nontrivial” or “boundary sectors
encode bulk anyons” as new principles.

**The endpoint-label claim splits into prior principle and narrower campaign
content.**

- For a `(2+1)`-dimensional topological boundary, the principle that boundary
  algebra sectors carry the bulk anyon labels is already explicit in JNPW's
  `DHR(F) ~= Z(C)` theorem (`LTO.tex:324`--`:333`).  Thus a bare categorical
  anyon-label claim is not novel.
- None of the four sources gives the campaign's exact same-circle finite TPM
  law `P_b W_x P_a = delta_(b,a+x) W_x P_a`, its explicit two-bit toric-code
  braiding readout, or the stated finite-protocol distinction between a fine
  fusion event and its universal-grading shadow.  Those narrower results are
  not preempted by this corpus.
- None gives A1's injective-MPS theorem that the bond-insertion endpoint-state
  locus is a `PGL(chi)` torsor, the state action is
  `rho_alpha:G -> PGL(chi)`, and the virtual multiplier class is the obstruction
  to an honest unitary lift.  JNPW's boundary `C*`-algebra is a different
  object; Corbelli's label is `G-hat`, not `H^2(G,U(1))`.

**A2's specific bookkeeping is not found here.**  The four sources do not
state the ordered tail-vacuum classification, the diagonal-symmetry double
coset `H_alpha\G/H_alpha`, or the explicit weak-* escape from a vacuum folium
under a half-infinite MPS symmetry string.  They supply the mature DHR sector
language against which A2 must be distinguished.  Accordingly the honest
novelty claim is the explicit injective-MPS solitonic construction and limit,
not the use of the words “sector” or “superselection.”

**No audited source closes the infrared triangle.**  There is no soft theorem,
soft momentum limit, domain-wall displacement/memory theorem, or identification
of either with a boundary DHR category, `G-hat`, or an MPS `H^2` multiplier.
The core narrow novelty conclusion of `docs/novelty-sweep.md`—the absence of a
lattice/MPS infrared-triangle synthesis—is therefore not contradicted by this
audit.  The affected novelty claims are the auxiliary ones about boundary
observables and sector organization.

### 5.2 What the original novelty sweep missed

The original sweep was organized around six soft/asymptotic-symmetry/memory
search lenses.  It did not cover the operator-algebraic boundary-observable
school represented by any of these four sources.  That omission matters in
four places:

1. JNPW is **close/direct prior art** for operational boundary algebras and for
   extracting bulk anyon categories from a boundary net.
2. Bhardwaj et al. is **foundational prior art** for the exact distinction
   between localizable/transportable DHR sectors and the campaign's looser use
   of sector language, and for stability under bounded-spread/intertwined
   nets.
3. Ogata–Pérez-García–Ruiz-de-Alarcón is **close prior art** for turning
   tensor-network ground-space structure into the observable maximality
   statement needed by the campaign's `(2+1)` program.
4. Corbelli is **close conceptual prior art** for symmetry-compatible
   superselection refinements of otherwise trivial product sectors.

These additions would change the sweep's threat/citation tables, but not its
zero finding for “MPS/tensor network × soft theorem/asymptotic symmetry/memory
triangle.”  In particular, Corbelli studies global covariance of sector
equivalences, not asymptotic half-string symmetries; JNPW studies boundary DHR
bimodules, not soft charges; and neither establishes the campaign's proposed
soft/SPT/memory links.

### 5.3 Citation debt, by campaign corner

The following are citations now owed by the labbook and by any Letter passage
making the corresponding claim.  “Owed” means cite and distinguish; it does
not mean import the cited theorem as a premise where its hypotheses have not
been verified.

| campaign location | citations now owed | what the text must say |
|---|---|---|
| **Corner A / A1: boundary algebra and asymptotic endpoint action** | Jones–Naaijkens–Penneys–Wallick, arXiv:`2307.12552`; Corbelli, arXiv:`2510.23790` | JNPW is the direct observable/ground-projection boundary-algebra antecedent.  Corbelli is the symmetry-compatible-sector antecedent.  Distinguish JNPW's compressed `C*` net and Corbelli's `G-hat` grades from A1's finite-window `M_chi` action, `PGL(chi)` state torsor, and `H^2` lifting obstruction. |
| **Corner A / A2: kink sectors and double cosets** | Bhardwaj et al., arXiv:`2410.21454`; Corbelli, arXiv:`2510.23790` | State that DHR/Naaijkens sectors are complement-localized and transportable, whereas A2 is a solitonic tail-vacuum sector with weak-* folium escape.  State that symmetry-compatible sector refinement is prior, while the double-coset/tail classification is not supplied there. |
| **`M-INDEX-LA-folium`** | Corbelli, arXiv:`2510.23790`; Bhardwaj et al., arXiv:`2410.21454` | Cite the covariant-representation and normal-sector frameworks, then say explicitly that neither constructs the campaign's common-unbroken-circle implementer in a fixed A2 kink folium or a window-charge limit. |
| **`A-INDEX-TC-fin`** | Jones–Naaijkens–Penneys–Wallick, arXiv:`2307.12552` | Cite the toric-code LTO boundary net and `DHR(F) ~= Z(fdHilb(Z/2))` as the infinite/operator-algebraic counterpart; retain the campaign's finite Pauli PVM/ribbon proof as the operational theorem. |
| **`A-INDEX-PEPS` / anyon-label row** | Jones–Naaijkens–Penneys–Wallick, arXiv:`2307.12552`; Bhardwaj et al., arXiv:`2410.21454`; Ogata–Pérez-García–Ruiz-de-Alarcón, arXiv:`2509.23734` | Cite respectively: ground-projection boundary nets and model `DHR=Z(C)`; abstract/bounded-spread sector categories and Naaijkens equivalence; exact/approximate Haag duality for the biconnected weak-Hopf fixed-point tensor-network class.  Preserve the fence that none supplies PT2/PT4 for an arbitrary microscopic endpoint. |
| **`SHAPE-FLAT`** | Jones–Naaijkens–Penneys–Wallick, arXiv:`2307.12552`; Bhardwaj et al., arXiv:`2410.21454` | Cite bounded-spread invariance as the categorical stability backdrop, while stating that it does not prove equality of specific code-projected path morphisms; the local cleaning/flat-transport identity remains separate. |
| **`M-INDEX-2D-fin`** | no theorem-level citation debt to these four | Add, at most, a scope sentence separating additive on-site TPM charge from DHR/tube topological charge.  Do not imply that this boundary literature proves the row. |

For the **Letter**, the minimum defensible placement is: JNPW in the first
paragraph that calls the MPS cut a boundary algebra; Bhardwaj et al. and the
Haag-duality paper wherever “all observables at the cut,” DHR sectors, or
phase-stable anyon categories are invoked; and Corbelli wherever the Letter
says that enforcing global-symmetry compatibility refines a trivial sector
theory.  The labbook should carry the fuller distinctions in the table.

### 5.4 Status and threat disposition

No live campaign status changes.  The audit narrows novelty and creates
citation obligations; it does not refute A1, A2, `M-INDEX-LA-folium`,
`A-INDEX-TC-fin`, `A-INDEX-PEPS`, `SHAPE-FLAT`, or `M-INDEX-2D-fin`.  The only
threat is to broad prose claiming originality for observable boundary
algebras, DHR-style sector bookkeeping, boundary recovery of anyon labels, or
symmetry-compatible refinement as general ideas.  The campaign's scoped
finite-MPS constructions, explicit weak-* limit, finite instrument laws, and
soft/memory connections remain distinct within the audited corpus.

## 6. Verdict

**Import —** the ground-projection boundary-net/channel construction and Haag/approximate-Haag duality as the observable foundation and missing exhaustiveness theorem for a cut.<br>
**Cite —** JNPW for boundary observables and `DHR=Z(C)`, Bhardwaj et al. for poset/Naaijkens sector equivalence, Ogata–Pérez-García–Ruiz-de-Alarcón for tensor-network Haag duality, and Corbelli for symmetry-compatible sector refinement.<br>
**Threat —** broad originality claims about boundary operationality and sector bookkeeping are preempted; no audited source threatens the scoped `PGL(chi)`/`H^2` endpoint result, A2 weak-* double-coset kink result, finite TPM selections, or their proposed soft/memory links.
