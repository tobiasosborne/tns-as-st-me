# Ogata map: split SPT index versus charge-history memory

**Status: PARTIAL/SKETCH.**  The local `refs/` tree contains no TeX source
attributed to Yoshiko Ogata.  Therefore every literature attribution below is
marked **UNVERIFIED-NEEDS-FETCH** with an arXiv identifier, even when official
arXiv metadata/HTML was used to identify the source.  No quotation from those
sources is treated as L3 ground truth.  The local side of every comparison is
grounded in D26--D27 and the live claim rows named below.

## 1. Executive answer

1. The memory index is **strictly different** from Ogata's SPT index.  The
   overlap is only at the edge: under a split/physical-edge identification,
   Ogata's half-chain projective implementer is the operator-algebraic version
   of the `V_C(g)` appearing in SPT-E'.  Its circle generator is the physical
   counterpart of the registered `Q_edge`, not of the finite-window
   `Qhat_{W,c_0}` in M-INDEX-fin.
2. Stability of the SPT class under symmetric gapped automorphic equivalence
   does **not** remove D27(LR).  It concerns a parameter path of ground states
   and preserves a half-chain cohomology class.  D27(LR2)--(LR3) concern a
   real-time excited-state TPM protocol, measurement back-action, and uniform
   first-moment tightness.  None is a conclusion of index stability.
3. Operator-algebraic LSM is an **admission gate only when** the proposed
   memory substrate is also required to be a translation-invariant, pure split
   (in particular unique gapped) state invariant under the full on-site
   symmetry.  A nontrivial projective class per unit cell then forbids that
   substrate.  The present kink/broken-vacuum memory setting does not satisfy
   those hypotheses, so it is not forbidden.

The shortest witness that the two indices are unequal is already local.  For
the spin-one AKLT register, D26 has `c=1` and microscopic offset `kappa=0`,
while SPT-E-AKLT has edge residue spectrum `{ -1/2,+1/2 }`.  Nevertheless
M-INDEX-fin sees integer *differences* because the same finite-window offset
cancels in the TPM protocol.  **Justification:** D26; claims M-INDEX-fin,
SPT-E-AKLT and SPT-E'; named computation S-C4.
The lane-local numerical witness is `ogata_separation_check.py`; its green and
red records are `ogata-separation-green.txt` and `ogata-separation-red.txt`.

## 2. Literature ledger (all non-local)

| tag | attribution used here | L3 status |
|---|---|---|
| OGA-SURVEY | Split unique gapped 1D ground states have type-I half-chain structure; the half-chain symmetry is implemented projectively and defines an `H^2(G,U(1))` class; symmetric gapped automorphic equivalence preserves that class; the survey also states the LSM cut-shift argument. | **UNVERIFIED-NEEDS-FETCH arXiv:2110.04671** |
| OGA-INDEX | Original on-site/time-reversal SPT-index stability result referred to by OGA-SURVEY. | **UNVERIFIED-NEEDS-FETCH arXiv:1810.01045** |
| OGA-SPLIT-CLASS | Completeness of the `H^2` class for symmetry-preserving product-half automorphic equivalence of pure split states. | **UNVERIFIED-NEEDS-FETCH arXiv:1908.08621** |
| OGA-AUTO | Bulk automorphic equivalence along a smooth gapped path. | **UNVERIFIED-NEEDS-FETCH arXiv:1906.05479** |
| OGA-PARENT | `C^1` classification of gapped parent Hamiltonians, with/without local symmetry. | **UNVERIFIED-NEEDS-FETCH arXiv:1407.3924; arXiv:1602.08839** |
| OGA-LSM | Projective-representation LSM no-go for translation/reflection invariant chains and pure split states. | **UNVERIFIED-NEEDS-FETCH arXiv:2004.06458; arXiv:1808.08740** |
| OGA-TYPEIII | General operator-algebraic results on normal states of type-III factors; this is not the split-SPT half-chain theorem. | **UNVERIFIED-NEEDS-FETCH arXiv:1301.5737** |

## 3. Claim-by-claim correspondence

| local object / claim | nearest Ogata-side object | exact relation in this corpus | verdict |
|---|---|---|---|
| D26(INT) | Microscopic on-site circle representation before passing to the half-chain action | D26 says one-site charge eigenvalues occupy `kappa+Z`.  It does not construct a half-chain implementer and contains no `H^2` datum. | **Strictly different.** |
| M-INDEX-fin | None needed | Finite-window spectrum and same-window TPM offset cancellation use only D26 and automorphic spectral invariance.  Gap, split property, a ground state, and an SPT class are absent. | **Independent of Ogata's index.** |
| M-INDEX-spec | None in the SPT stability theorem | Adds D27's real-time Cesaro/TPM and first-moment-tightness hypotheses.  The conclusion is a probability law on `Z`, not a cohomology class. | **Neither corollary nor equivalent.** |
| M-INDEX-LA-folium | Spatial implementation of symmetry in a fixed GNS representation | Ogata's construction suggests an implementer when the state is invariant and split, but it is a half-chain implementer in a type-I factor.  M-INDEX-LA-folium asks for a strongly continuous implementer in one fixed kink GNS folium. | **Possible bridge, not proved here.**  Concurrent lane `la-folium` now records a PROVED-candidate scoped to the fixed bare A2 kink; this lane neither duplicates nor adjudicates that proof. |
| M-INDEX-LA-strong | No analogue | Strong-resolvent convergence of regularised window charges is refuted both off and on the A2 folium.  Ogata's route is spatial implementation, not convergence of window-charge operators. | **Refuted local route remains refuted.** |
| M-IDX-density | LSM/filling compatibility | `2rho in Z` follows from two antisymmetric covariant MPS tails plus D26.  It is an arithmetic selection rule and assumes neither translation-invariant full-symmetry uniqueness nor a no-go conclusion. | **LSM-flavoured, not an LSM theorem.** |
| SPT-E' | Right/left half-chain projective implementer | Under H-split, the registered `V_C(g)` is the MPS/transfer representative of the half-chain implementer.  Its cocycle/module is the same kind of `H^2` datum; the centered Lie residue and shifted charge weights are extra circle-restriction data. | **Corollary-shaped under H-split, not yet locally sourced to Ogata.** |
| SPT-T', SPT-D' | Projective multiplication of the half-chain implementer | Both expose the same cocycle through ordered endpoint products.  Physical use still needs H-split/H-dress. | **Same projective algebra, different observable packaging.** |
| SPT-M' | No SPT-index theorem supplies scattering | Adds H-AD-edge and charge conservation to turn edge weights into channel bookkeeping.  Ogata protects the module/class, not a nonzero edge-changing amplitude. | **Strict extension by dynamical hypotheses.** |
| SPT-M'-dyn | None | Half-chain wave operators, an on-shell reflection matrix, and nonvanishing remain open. | **Not supplied by phase classification.** |
| SPT-B-mult / SPT-B' | Whole-chain genuine action and phase stability | Left/right projective multipliers cancel in the whole-chain action, while the individual half-chain class survives.  Stability of the class does not quantise arbitrary bulk coefficients. | **Consistent, not equivalent.** |
| A-INDEX-TC-fin / A-INDEX-PEPS | Higher-dimensional endpoint/anyon selection, not the 1D split index | These rows concern 2D annular/ribbon or categorical registers. | **Outside the 1D Ogata comparison.** |

**Literature premise for the Ogata-side column:** OGA-SURVEY and OGA-LSM,
both **UNVERIFIED-NEEDS-FETCH** as listed in section 2.  **Local
justification:** D26--D27; claims M-INDEX-fin, M-INDEX-spec,
M-INDEX-LA-folium, M-INDEX-LA-strong, M-IDX-density, SPT-B-mult, SPT-B',
SPT-E', SPT-T', SPT-D', SPT-M', SPT-M'-dyn, A-INDEX-TC-fin and
A-INDEX-PEPS.

## 4. The implementer map, without conflating the objects

The map has four levels.  Only the middle two are Ogata/SPT objects.

| level | object | what its `2pi` information means |
|---|---|---|
| microscopic site | D26's `exp(2pi i S^z_x)=c I` | All one-site charge eigenvalues lie in one coset `kappa+Z`.  The scalar disappears in the adjoint action. |
| whole-chain GNS | A spatial implementer of the selected circle, if it exists in the chosen folium | In an irreducible representation its `2pi` unitary is scalar, so its Stone generator has spectrum in one integer coset.  This is the implementer route of M-INDEX-LA-folium. |
| split half-chain | Ogata's right implementer `u_R(g)` | It is projective; its multiplier gives the `H^2` SPT class.  The left implementer carries the inverse multiplier so the whole-chain action is genuine.  **UNVERIFIED-NEEDS-FETCH arXiv:2110.04671, arXiv:1810.01045.** |
| MPS edge register | D21/SPT-E' `V_C(g)` and `Q_edge=-iX_C^circ` | Under H-split this is the finite-dimensional representative of the preceding half-chain action.  Restricting the full projective action to the selected circle gives the shifted edge weights, subject to D21's full-group normalization. |

Thus the proposed identification is

`Ogata u_R(g)` --(MPS/split intertwiner)--> `V_C(g)`
`                                  ` --(circle derivative and centering)--> `Q_edge`,

not `Ogata u_R(g) = exp(i theta Qhat_{W,c_0})`.  The latter is a local
finite-window observable and need not converge to any total-charge operator;
claim M-INDEX-LA-strong is already REFUTED.

The type of the half-chain factor is a gate, not extra topological data.  In
the split SPT construction it is type I by definition/the unique-gapped-state
input (**UNVERIFIED-NEEDS-FETCH arXiv:2110.04671**).  A genuinely type-III
half-chain factor is therefore outside that split construction and cannot be
used to discharge H-split.  M-INDEX-fin remains valid there because it never
uses a half-chain factor.  OGA-TYPEIII concerns general type-III factor
flexibility, not an alternative derivation of the 1D split SPT index.

### Structured comparison proof

**ASSUME.** D26, D21--D22, and the live claims named below.  For the
literature-side map, assume OGA-SURVEY exactly at its
**UNVERIFIED-NEEDS-FETCH** strength.

**PROVE.** The SPT edge-charge quantization is a restriction/shadow of the
half-chain projective implementation under H-split, while M-INDEX-fin and
M-INDEX-spec are not Ogata-index corollaries.

**⟨1⟩1.** D26 fixes the one-site spectral coset and hence the finite-window
coset used by the TPM law.  It supplies no cocycle or split representation.
**Justification:** D26; claim M-INDEX-fin.

**⟨1⟩2.** The half-chain implementer instead implements the symmetry on a
type-I half-chain factor and is defined only up to phase; its multiplication
phases form the SPT cocycle.  **Justification:** assumed OGA-SURVEY,
**UNVERIFIED-NEEDS-FETCH arXiv:2110.04671**.

**⟨1⟩3.** Under H-split, D21 identifies the physical half-chain action with
the registered `V_C(g)`, and SPT-E' identifies its centered circle generator
with `Q_edge`.  **Justification:** D21; claims SPT-E' and SPT-E-AKLT.

**⟨1⟩4.** The two data cannot be equal: the AKLT instance has microscopic
`kappa=0` but edge weights `+/-1/2`.  **Justification:** D26; claim
SPT-E-AKLT; named computations S-C4 and lane-local
`ogata_separation_check.py` (green exit 0; wrong-prefactor mutation exit 1).

**⟨1⟩5.** M-INDEX-fin depends only on the microscopic coset and same-window
offset cancellation; M-INDEX-spec additionally depends on D27, not on D21 or
an `H^2` class.  **Justification:** D26--D27; claims M-INDEX-fin and
M-INDEX-spec.

**⟨1⟩6. QED.** The only corollary-shaped relation is
`half-chain projective implementer -> SPT edge module` under H-split.  The
charge-history index is strictly different.

## 5. Why automorphic phase stability does not remove (LR)

**ASSUME.** OGA-AUTO/OGA-INDEX at their
**UNVERIFIED-NEEDS-FETCH** strength, D27, and the exact statement of
M-INDEX-spec.

**PROVE.** Ogata stability gives no free derivation of D27(LR2)--(LR3).

**⟨1⟩1.** The parameter in automorphic phase equivalence labels a smooth path
of symmetric gapped interactions and its ground states.  Its relevant
conclusion is preservation of the half-chain projective class after a
symmetry-preserving left/right factorization.  **Justification:** assumed
OGA-AUTO and OGA-INDEX, **UNVERIFIED-NEEDS-FETCH arXiv:1906.05479,
arXiv:1810.01045**.

**⟨1⟩2.** The parameter in D27 is real time for one fixed excited/kink vector.
D27(LR2) is a first-moment statement about the dephased two-time observable,
not a statement about a ground-state representation.  **Justification:**
D27(LR2); claim M-INDEX-spec.

**⟨1⟩3.** D27(LR3) is a uniform-integrability statement for a spatial family
of TPM laws.  An `H^2` label contains neither those laws nor their first
moments.  **Justification:** D27(LR3); claim M-INDEX-spec; the permanent
mean-escape landmine in `theory/memory-index.md` section 6.

**⟨1⟩4.** Even D27(LR1), now available by a general subsequence argument, does
not imply LR2 or LR3.  **Justification:** claim LR1-GEN; D27.

**⟨1⟩5.** Therefore using phase automorphisms can preserve the SPT label of
the substrate, but removing `(LR)` still needs separate dynamical estimates:
asymptotic nondemolition/local decay for LR2 and a uniform first-moment bound
for LR3.  **Justification:** D27; claims M-INDEX-spec and AD3-ex.

**⟨1⟩6. QED.** No implication from Ogata index stability to D27(LR2)--(LR3)
is established.  This is a hypothesis/conclusion mismatch, not a claim that
such estimates can never be proved for a particular model.

## 6. LSM constraint on calibrated memory

**Literature premise (not local):** a translation-invariant chain whose
on-site symmetry action carries a nontrivial projective class per unit cell
admits no translation-invariant pure split state of the relevant kind, hence
no unique gapped symmetric ground state in that class.
**UNVERIFIED-NEEDS-FETCH arXiv:2004.06458; arXiv:1808.08740.**

The consequence for this corpus is sharply scoped:

| proposed substrate | LSM effect |
|---|---|
| Unique, gapped, translation-invariant and fully `G`-invariant split tail with nontrivial projective class per cell | Forbidden by the literature premise.  One must enlarge the unit cell until the cell class cancels, or give up at least one of translation, full symmetry, purity/split, uniqueness, or the gap. |
| D9/D17 kink between a covariant broken-vacuum pair | Not forbidden by that premise: the kink state is not a translation-invariant unique fully `G`-invariant ground state. |
| M-INDEX-fin on an arbitrary finite window | Unaffected: it is finite charge arithmetic under D26. |
| M-IDX-density with antisymmetric tails | Independently requires `2rho in Z`; this is a positive arithmetic compatibility condition, not a no-go theorem. |

In particular, D26's scalar `c` or microscopic offset `kappa` alone is not
the LSM obstruction for an arbitrary `G`.  The LSM datum is the projective
class of the **full physical on-site symmetry action per translation cell**.
For a quotient symmetry such as the spin-rotation group, the scalar acquired
by a lifted `2pi` path may help identify that class, but the identification is
group-dependent and must not be inferred from D26 alone.  **Justification:**
D26; claims M-IDX-density and SPT-E'; literature premise OGA-LSM at the marked
unverified strength.

## 7. Single best new theorem candidate

### CANDIDATE OG-MEM-PHASE — phase-stable edge-memory capacity and difference lattice

**HONEST STATUS: SKETCH.**  It is a clean composition of local proved rows
with an Ogata stability premise, but the latter has no local TeX, and the
finite-group-to-compact-circle scope must be checked before promotion.

**ASSUME.**

1. A symmetric uniformly gapped path of one-dimensional interactions whose
   pure invariant ground states are split, with half-chain projective class
   constant under the corresponding factorized automorphic equivalence
   (OGA-INDEX/OGA-AUTO, **UNVERIFIED-NEEDS-FETCH arXiv:1810.01045,
   arXiv:1906.05479**).
2. D21's full-group/circle normalization at every path point, and H-split
   identifying the physical half-chain action with the registered edge
   module.  If Ogata's theorem is used beyond finite `G`, assume the required
   compact-group extension explicitly.
3. Wherever a memory protocol is asserted, H-AD-edge, conserved selected
   circle charge, and definite channel charges, exactly as in SPT-M'.

**PROVE (candidate).** Along the path:

(a) the protected edge-module class and the lower bound `d_omega` on memory
capacity are constant;

(b) at every path point, post-selected edge-charge changes lie in `Z` and obey
`Delta Q_edge=-(Q_bulk,out-Q_bulk,in)`;

(c) neither the centered absolute offset, a transition matrix element, nor a
nonzero memory probability is asserted constant.

### Proof sketch in Lamport form

**⟨1⟩1.** The half-chain cohomology class is constant along the symmetric
gapped path.  **Justification:** ASSUME 1 (OGA-INDEX/OGA-AUTO),
**UNVERIFIED-NEEDS-FETCH** as marked.

**⟨1⟩2.** The minimal projective-irrep dimension depends only on that class,
so the protected module at each path point has dimension at least the same
`d_omega`.  **Justification:** D21; claim SPT-E'(ii); ⟨1⟩1.

**⟨1⟩3.** At each fixed path point, D21 and SPT-E'(iii) put all edge weights
in one shifted integer lattice.  Subtracting two weights of that same system
eliminates its offset, even if the centered offset varies with the path.
**Justification:** D21; claim SPT-E'.

**⟨1⟩4.** Under ASSUME 3, charge conservation converts those within-system
integer differences into the channel ledger in clause (b).
**Justification:** D22; claim SPT-M'.

**⟨1⟩5.** SPT-E' explicitly does not assert deformation constancy of its
centered offset, and SPT-M' explicitly does not force a nonzero amplitude.
Therefore clause (c) is required.  **Justification:** claims SPT-E', SPT-M'
and SPT-M'-dyn.

**⟨1⟩6. QED (conditional sketch).** Clauses (a)--(c) follow once the external
stability premise and the compact-group/circle scope are locally verified.

This is the useful theorem Ogata suggests: **topology stabilizes the memory
module and the integer difference rule across a phase, not the memory
probability and not D27 relaxation.**

## 8. Exact forward obligations

1. Fetch and title-verify TeX for arXiv:2110.04671, 1810.01045, 1908.08621,
   1906.05479, 2004.06458 and 1808.08740 before using any attribution in a
   promoted claim or the paper.
2. Check the precise symmetry scope of the `H^2` stability theorem (finite
   versus compact/continuous `G`) and prove or state the extension needed by
   D21's circle.
3. Keep the M-INDEX-LA-folium existence attack in lane `la-folium`; its current
   PROVED-candidate is scoped to the fixed bare A2 kink.  Do not duplicate it
   here or replace the broader kink-folium problem by the easier invariant
   split-ground-state implementer.
4. Prove H-AD-edge/model scattering separately.  Ogata stability supplies no
   wave operators, no LR2/LR3, and no nonvanishing reflection amplitude.

No existing repository file is targeted; no `PATCH.md` is needed.
