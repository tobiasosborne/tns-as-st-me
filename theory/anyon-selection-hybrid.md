<!-- ROLE: final W21 categorical hybrid for bd tns-7pp.
     Canonical typing: theory/anyon-label-index.md (PT1)--(PT4).
     Imported from theory/soft-2d-hunt.md only: T_x(k;w), its linear
     Fourier/window corollary, and SHAPE-FLAT. -->

# A-INDEX-PEPS — categorical selection with the FUSION-SOFT corollary

**Citation disposition.**  This is the single citation carrier for the
overlapping model-general selection statements called `A-INDEX-PEPS` in
`anyon-label-index.md` and `FUSION-SOFT` in `soft-2d-hunt.md`.  Those files
remain lane records.  `A-INDEX-TC-fin` and its finite Pauli proof remain
canonical in `anyon-label-index.md`; SHAPE-FLAT is carried here separately
from the selection statement.

**Status.**  The implication from the displayed exact PEPS data is proved
below.  Supplying `(PT2)--(PT4)` for a particular microscopic PEPS/ribbon is
still a model-specific obligation; this hybrid does not assert that every
topological-phase representative supplies them.

## 1. Canonical PEPS typing: (PT1)--(PT4)

Let `C` be a finite unitary fusion category and let a finite MPO-injective
PEPS lattice model supply all of the following exact data.

1. **(PT1: tube PVM)** An annular representation of `Tub(C)` whose minimal
   central idempotents `{P_a}_(a in Irr Z(C))` are mutually orthogonal and sum
   to the identity on the chosen boundary-circle register.
2. **(PT2: pure endpoint)** A small-circle resolution of the endpoint tensor
   `T_x` such that

   `P_y^end T_x=delta_(y,x) T_x`

   for one simple `x in Irr Z(C)`.  A sum over `x` is not called a pure
   endpoint.
3. **(PT3: pulling-through module action)** Exact zipper, associator, and
   pulling-through equations identify the large-circle action of `T_x` on a
   source sector `a` with the semisimple decomposition

   `x tensor a ~= direct-sum_b Hom(b,x tensor a) tensor b`.       **(H.1)**

4. **(PT4: protocol instrument)** The physical charge-creation operation is
   supplied either as a normalized family of channel-resolved Kraus maps
   `T_(x,mu)`, or the experiment is explicitly conditioned on the success of
   one displayed Kraus map.  Category data alone do not provide its
   normalization or probabilities.

These are hypotheses, not consequences of the theorem.  In particular,
PT4 is the only normalization input.

## 2. Fourier/window notation

Let `T_x(y;w)` be a translated, windowed representative of the same pure
endpoint data, with endpoint position `y` along a chosen direction and all
microscopic smearing data collected in `w`.  On a finite periodic boundary
of length `L`, define

`T_x(k;w)=sum_(y=0)^(L-1) exp(iky) T_x(y;w)`,
`k in (2pi/L)Z`.                                             **(H.2)**

Resolve `P_b T_x(k;w)P_a` in a basis labelled by
`mu in Hom(b,x tensor a)`.  In an infinite-volume protocol, a limit means a
declared sequence of windows and momenta in a declared operator, weak, or
matrix-element topology in which multiplication by the fixed finite-sector
projectors is continuous.

## 3. Lamport proof of the single selection statement and its linear corollary

### ⟨1⟩1. THEOREM `A-INDEX-PEPS`

**ASSUME.**  (PT1)--(PT3), and for the momentum form the notation and declared
topology of §2.  Assume PT4 only for the instrument-normalization clause.

**PROVE.**  On the finite annular register,

`P_b T_(x,mu) P_a=0` unless
`mu in Hom(b,x tensor a)` and `N_(xa)^b>0`.                 **(H.3)**

Consequently the same-circle instrument weight

`p_x(a,b,mu)=Tr(P_b T_(x,mu) P_a rho P_a`
`                         T_(x,mu)^dagger P_b)`             **(H.4)**

is supported only on the fusion events in (H.3), and is normalized or
postselected exactly as stipulated by PT4.

**FUSION-SOFT corollary.**  Moreover,

`P_b T_x(k;w) P_a=0 unless Hom(b,x tensor a) != 0`           **(H.5)**

at every finite momentum and window, and every existing limit point in the
declared topology obeys the same zero-block constraint.

**⟨2⟩1 (typing and fusion decomposition).**  For each translated endpoint,
`T_x(y;w)P_a` has components only in the direct sum in (H.1).

*Justification.*  PT2 selects one simple endpoint type `x`.  PT3 identifies
its action on source sector `a` with the displayed semisimple decomposition;
there is no summand labelled by `b` when `Hom(b,x tensor a)=0`.

**⟨2⟩2 (finite block selection).**  Left multiplication by `P_b` kills every
component of `T_x(y;w)P_a` except its `b` summand, proving (H.3) after the
multiplicity space is resolved by `mu`.

*Justification.*  By PT1 the `P_b` are mutually orthogonal central
idempotents resolving the annular register.  The multiplicity of the retained
summand is `dim Hom(b,x tensor a)=N_(xa)^b`.

**⟨2⟩3 (instrument support and normalization).**  A forbidden block makes
the corresponding Kraus operator in (H.4) zero.  Hence its weight vanishes.
For the allowed blocks, PT4 supplies either a normalized Kraus family, whose
sequential weights sum to one, or the displayed success probability by which
the postselected weights are divided.

*Justification.*  Positivity and support follow directly from the Kraus form
of (H.4); normalization is used only in the form explicitly supplied by PT4.

**⟨2⟩4 (Fourier/window linearity).**  For a forbidden pair `(b,a)`, every
summand `P_bT_x(y;w)P_a` in (H.2) is zero by ⟨2⟩2.  Fourier summation and
windowing are linear, so their finite linear combination is zero.  This is
(H.5).

**⟨2⟩5 (declared topology).**  A net of forbidden blocks is identically
zero.  Continuity of multiplication by the fixed projectors in the declared
topology therefore makes every existing limit block zero.

*Justification.*  The limit of the zero net is zero.  This asserts neither
existence nor uniqueness of a soft limit.

**⟨2⟩6. QED.**

The fine retained datum is `(x,a -> b;mu)`.  If `x` is invertible the target
is uniquely `b=x tensor a` and the supplied index is
`x in Inv(Z(C))`.  For general `x`, every allowed event has the universal
grading shadow `|b||a|^(-1)=|x|`; this shadow neither selects `b` nor fixes a
probability.

## 4. Lamport proof of SHAPE-FLAT

### ⟨1⟩2. THEOREM `SHAPE-FLAT`

**ASSUME.**  An exact fixed-point MPO/string representation with its
pulling-through and associator equations.  Let `gamma` and `gamma'` have the
same resolved endpoints and be related by a finite sequence of contractible
local pulling-through moves in a disk containing no other insertion.

**PROVE.**  After identifying the endpoint fusion spaces by the associator
maps supplied by the moves, the code-projected endpoint morphisms for
`gamma` and `gamma'` agree.  A path around another insertion is outside this
contractible hypothesis and may carry braid or monodromy holonomy.

**⟨2⟩1 (one move).**  One local pulling-through move gives equality of the
two code-projected tensor networks across that move, with the endpoint fusion
spaces identified by its supplied associator map.

*Justification.*  This is exactly the assumed local pulling-through equation.

**⟨2⟩2 (finite composition).**  Compose the equalities from ⟨2⟩1 along the
finite move sequence.  The first network is thereby identified with the last
network.

*Justification.*  Equality and the supplied associator identifications are
stable under finite composition.

**⟨2⟩3 (coherence).**  Two contractible move sequences with the same ends
give the same categorical identification.

*Justification.*  Pentagon coherence relates the two finite compositions of
associators.

**⟨2⟩4 (noncontractible-holonomy fence).**  A move sequence winding around
another insertion is not contractible in its complement, so ⟨2⟩3 does not
identify it with the trivial path.  Its composition may instead be the
corresponding braid or monodromy action.

**⟨2⟩5. QED.**

## 5. W2/W6 dictionary

| W2 register | W6 register | identification |
|---|---|---|
| `D=Z(C)` bulk tube register | `D=Z(C)` in the bulk, or a declared boundary excitation category | the same bulk object only before boundary condensation |
| tube projectors `P_a,P_b` | sector projectors `P_a,P_b` | identical block resolution |
| pure endpoint Kraus map `T_(x,mu)` | translated/windowed endpoint `T_x(y;w)`, `T_x(k;w)` | the Fourier/window operation linearly sums W2-type pure endpoint intertwiners |
| `P_bT_(x,mu)P_a=0` unless `mu in Hom(b,x tensor a)` | `P_bT_x(k;w)P_a=0` unless `Hom(b,x tensor a)!=0` | the same selection rule before and after a linear Fourier/window sum |
| TPM weights and PT4 normalization/postselection | block form factor and conditional `k->0` limit | W2 adds an instrument; W6 adds kinematics/topology, not probabilities |

## 6. Existing gates

No new checker or mutation mode is introduced.

| existing gate | role here |
|---|---|
| `theory/checks/anyon_label_check.py` `ANYON-C0`--`ANYON-C4`; `--red wrong-sector` | pointed toric-code endpoint, same-circle instrument, and selection instance |
| `theory/checks/cat_hunt_check.py` `CATH-C1`--`CATH-C2`; `--red missing-ising-channel` | pointed and branching fusion arithmetic |
| `theory/checks/soft_2d_hunt_check.py` `S2DH-C0`--`S2DH-C2`; `--red wrong-path` | exact toric-code path-equivalence witness for SHAPE-FLAT |

These finite gates do not establish PT2--PT4 for an arbitrary microscopic
PEPS and do not establish existence of an infinite-volume momentum limit.
