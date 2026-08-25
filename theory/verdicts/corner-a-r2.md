<!-- ROLE: L6 critic verdict, round 2, on the revised Corner-A package.
     Critic: Codex. Date: 2026-08-25. -->

# Critic verdict r2 — Corner A (WI, A1, A2, G0)

Critic: Codex, adversarial pass under L6/L6b.  I treated
`theory/verdicts/corner-a-r1.md` as my own first-round verdict and audited the
revised `definitions.md`, `notation.md`, `claims/CLAIMS.md`, all four Corner-A
shards, the response, the numerical script, and the two named downstream
drafts.  I re-ran `python3 theory/checks/corner_a_check.py`; C0--C7 all pass.

The revision fixes most of r1.  WI, the endpoint-state bijection, the corrected
stabiliser/orbit, the Jordan-safe A2 limit, the double-coset classification,
the finite-range cut current, and the retraction of the soft theorem all
survive this pass.  The loop nevertheless has not reached a fixed point: A1's
finite-window twisted-algebra action is not a well-defined operator on the
declared vector space, G0(c)'s new exact finite-window formula omits a right
edge term, and the claims DAG still overstates several quantifiers and retains
the refuted `B3` orbit language.

## Independent checks

### Orientation (R3)

Starting only from D2(b),

`\mathcal U(g)A_\alpha=e^{i\theta}V_\alpha(g)^{-1}A_{g\cdot\alpha}V_\alpha(g)`,

the product over `R=[a,b]` is

`e^{i|R|\theta}V^{-1}A_{g\cdot\alpha}^{s_a}\cdots A_{g\cdot\alpha}^{s_b}V`.

Thus `V^{-1}` is on `\partial_-R` and `V` on `\partial_+R`.  The r1 `Z_2`
example really was blind because `Z=Z^{-1}`.  The revised `U(1)` example uses
`V(t)=e^{itZ/2}` with `V(t)\ne V(t)^{-1}` and satisfies (IT); direct enumeration
gives errors `5.6e-17` in the displayed orientation and `0.267` in the flipped
orientation.  This is conclusive.  R3 is accepted; the r1 conclusion was right,
but its numerical evidence for that incidental conclusion was inconclusive.

### Lemma SBP and the r1 value `0.5912426665717146`

Finite reindexing gives, coefficient by coefficient,

```
sum_n f(n)(AX-XA)@n
 = -sum_{m=a}^{b-1}(f(m+1)-f(m)) X@m
   + f(b)X@b - f(a)X@(a-1).
```

For `f(n)=e^{ikn}` and `N_k(X)=e^{ik}AX-XA`, this becomes exactly

`Phi_k^Lambda(N_k(X))=e^{ik(b+1)}X@b-e^{ika}X@(a-1)`.

The signs, phases, and endpoints match my r1 derivation.  Therefore, on the
same four-site tensor and boundary vectors used in r1, the norm of the new
right-hand side is exactly the previously measured
`0.5912426665717146`; C3b's `1.7714` merely uses different boundary vectors.
The new script verifies the coefficient identity to `3.5e-17`.  Lemma SBP
itself is correct.

### A countercheck omitted by C0--C7

For the exact finite-window display in G0(c), using the script's Pauli tensor,
boundaries, `L=4`, `k=0.37`, and `X=K`, I obtain

```
|| LHS - displayed RHS || = 0.4505862126399518,
|| (1-e^{ik})e^{ikb} |psi;X@b> || = 0.45058621263995174,
max coefficient mismatch after adding that term = 6.25e-17.
```

Thus the discrepancy is precisely the omitted `m=b` term identified in
objection 3 below.  C3/C3b test SBP, not this later application of it.

## Disposition of the twenty r1 objections

| r1 # | r2 assessment |
|---|---|
| 1 | **FIXED.** D1(e) now admits the two edge bonds and WI states the alternative padded-window hypothesis. |
| 2 | **FIXED.** The vector and state identities are separated and the state carries no phase. |
| 3 | **FIXED in substance.** `E_b^alpha` is no longer a vacuous `V(g)GL(chi)` family; the state orbit is `G/N_alpha`, and `S_alpha`, not `G_diag`, is the stabiliser.  D9's theorem/definition layering still has the minor defect in objection 7 below. |
| 4 | **INCOMPLETE.** The inverse/order convention and the invisibility of phases on states are fixed, but the proposed operator on `W_{Lambda,b}` is not well defined (objection 1), and the lift language conflates a twisted action with an honest lift (objection 2). |
| 5 | **FIXED.** The proof introduces the normalisation scalar, uses independent word blocks and multilinear extension, and reduces the general `M,M'` case correctly. |
| 6 | **FIXED.** Only the valid implication `Cauchy => rho_n=1` for every `n` is now used. |
| 7 | **FIXED.** The Lie-algebra cocycle is explicitly only a possibly lossy infinitesimal image of the group SPT class. |
| 8 | **FIXED as to derivation, incomplete as to realisation.** Lemma IT derives the multiplier, so that part is not circular.  The finite-window realisation still fails as stated by objection 1; the GNS realisation is honestly left SKETCH. |
| 9 | **ACCEPTED.** Lemma D remains sound. |
| 10 | **FIXED in substance.** The half-chain state is constructed separately and the rate is any `lambda_tilde>lambda_E`.  D1(e') has only the minor presentation defect in objection 8. |
| 11 | **CONCEDED and correctly replaced in the theorem.** The pair space and double-coset result are right under the stated transitivity hypothesis; that hypothesis is lost in the DAG row (objection 5). |
| 12 | **CONCEDED.** The contact-term slogan is no longer PROVED content. |
| 13 | **FIXED at the lemma level.** SBP has the correct boundary terms.  Its later use in G0(c) has a new endpoint omission (objection 3). |
| 14 | **FIXED.** Broken directions are now described as failure of same-vacuum return, not failure of (IT). |
| 15 | **ACCEPTED.** The tensor-level dichotomy survives. |
| 16 | **FIXED.** The rank drops as `k->0`, and the text no longer makes the rank jump cause the kinematic factor. |
| 17 | **ACCEPTED.** The nearest-neighbour current calculation and O1 check remain correct. |
| 18 | **CONCEDED/RETRACTED in Corner A.** The Corner-C obligations are now explicit.  The retracted inference is nevertheless used in `spt-scoping-draft.md` (objection 6). |
| 19 | **FIXED.** The cut-current definition and proof cover the finite-range quantifier. |
| 20 | **CONCEDED.** Both boxes are now labelled load-bearing.  The downstream SPT draft nevertheless reads A1 as an edge-Hilbert-space action without supplying the missing split/GNS step (objection 6). |

## Rebuttals R1--R4

### R1 — partly accepted, but not established as written

R1 is right about the conceptual separation: the multiplier already lives on
the finite virtual matrices, and no split property is needed to exhibit the
projective relation `V(h)V(g)=e^{iomega(h,g)}V(hg)`.  Normality/split is needed
only to realise that virtual action in the infinite-volume GNS Hilbert space.

It does not follow that D4(a)'s action on the *physical window-vector space* is
well defined.  A linear rule on decorated representatives must preserve every
linear relation between the resulting physical vectors.  It does not; the
explicit injective symmetric counterexample in objection 1 disproves it.  The
H2 class therefore has a perfectly good formal/virtual home without normality,
but the claimed home on every `W_{Lambda,b}` has not been constructed.

### R2 — accepted on the cocycle and non-circular core

The cocycle law is genuinely derived in Lemma IT from composition and MPS
uniqueness.  The scalar lemma, `rho_alpha`, `N_alpha`, corrected stabiliser, and
endpoint-state orbit are also theorem content, not definitions in disguise.
This rebuts the broad version of r1 objection 8.  It does not repair R1's
well-definedness problem, and D9(c) should stop stating its own A1 consequences
as part of a definition (objection 7).

### R3 — accepted

The r1 `Z_2` numerical test could not distinguish the flip.  The revised U(1)
test can, and agrees with the independent algebraic derivation above.  The
orientation is conclusively pinned.

### R4 — accepted

The old sentence could be read in the away-from-zero direction, in which it
was true.  The new wording removes the ambiguity, and it correctly separates
the rank drop from the algebraic origin of `1-e^{ik}`.

## Numbered r2 objections

### 1. MAJOR — D4(a)'s finite-window multiplier action is not well defined

**Locations:** D4(a), A1(d1), the A1 claims row; R1.

`W_{Lambda,b}` is a space of *physical vectors*, so the rule "replace the bond
insertion `M'` by `MM'`" must be independent of the decorated representative.
No injectivity of the map from a bond matrix to a window vector is assumed.
In fact its kernel need not be invariant under left multiplication, even for
an injective symmetric tensor and even when the multiplier is the actual
virtual symmetry.

Take

```
A^0 = diag(1,2),       A^1 = X,       V = Z,
u(g) = diag(1,-1),     b_l = (sqrt(2),1),  b_r = (1,0).
```

The length-two words span `M_2` (rank `4`), and the transfer map has a unique
largest eigenvalue, so after the standard scale/canonical gauge this is a D1
injective canonical tensor.  Conjugation by `Z` fixes `A^0` and negates `A^1`,
so it satisfies (IT) with the displayed `u,V`.  On a two-site window with the
insertion at the middle bond, let

```
F(M)_{st} = b_l^dagger A^s M A^t b_r,
N = [[-sqrt(2),0],[1,0]].
```

Directly, `F(N)=0` while `max|F(ZN)|=4`.  Since `I+0.1N` is invertible,
`F(I+0.1N)=F(I)` represents the same physical window vector, but the proposed
action gives `F(Z(I+0.1N)) != F(ZI)`.  Canonical gauging conjugates all of
`A,N,Z` and transforms the boundary vectors, preserving this relation.

Thus `V_b(Z)` is not an operator on the declared `W_{Lambda,b}`.  A repair can
require enough sites on both sides of the cut (and fixed nonzero boundaries)
so the bond-matrix map is injective, or work on a formal decorated-vector
space and then prove the relevant kernel invariant.  Until then A1(d1) and
the A1 PROVED row are false.

### 2. MAJOR — A1(d3) calls the twisted action the lift that `[omega]` obstructs

**Locations:** A1(d1)--(d3), D9(c), the A1 claims row.

The standard correct statement is: `[omega_alpha]` obstructs lifting the
homomorphism `rho_alpha:G->PU(chi)` to an **honest homomorphism**
`G->U(chi)`.  But (d1) satisfies
`V_b(h)V_b(g)=e^{iomega(h,g)}V_b(hg)`; it is a projective `G` action, or a
linear module for the *twisted* group algebra, not an honest linear
representation of `G`.  It exists precisely when the multiplier is retained,
including when `[omega]` is nontrivial.  Therefore `[omega]` does not obstruct
"lifting (d2) to (d1)" as the theorem and D9 say; it obstructs removing the
multiplier from such a lift.  This convention slip matters to the advertised
meaning of A1 even after objection 1 is repaired.

### 3. MAJOR — G0(c)'s new exact finite-window equation still drops an edge term

**Locations:** `corner-a-goldstone.md` G0(c), proof step <2>3, G0 claims row.

From

`B_G=N_k(X)+(1-e^{ik})AX`

and Lemma SBP(ii), the exact result is

```
Phi_k^Lambda(B_G)
 = (1-e^{ik}) sum_{m=a}^{b} e^{ikm}|psi;X@m>
   + e^{ik(b+1)}|psi;X@b> - e^{ika}|psi;X@(a-1)>.
```

Equivalently, after combining the right-edge coefficient,

```
 = (1-e^{ik}) sum_{m=a}^{b-1} e^{ikm}|psi;X@m>
   + e^{ikb}|psi;X@b> - e^{ika}|psi;X@(a-1)>.
```

The theorem instead truncates the bulk sum at `b-1` while retaining the
uncombined SBP boundary coefficient `e^{ik(b+1)}`.  It therefore omits
`(1-e^{ik})e^{ikb}|psi;X@b>`.  The independent Pauli-tensor value is
`0.4505862126399518`, with agreement to `6.25e-17` after adding that term.
The missing term disappears in either intended D12 asymptotic regime, so the
thermodynamic quotient statement is repairable; the displayed *exact*
finite-window identity is nevertheless false.

### 4. MAJOR — D12's two regimes are over-quantified and conflated in G0

**Locations:** D12(a)--(b), Lemma SBP(v), G0(c), G0 claims row.

The estimate proves only that the **difference/remainder** has vanishing norm
for `f in c_0`.  It does not make either side a norm-convergent GNS vector for
an arbitrary `c_0` profile; `c_0` is not contained in `ell^2`, and excitation
sums with, for example, `f(n)=(1+|n|)^{-1/4}` generally have divergent norm.
The safe wave-packet statement needs a summability class (the cited smooth
momentum packet has rapidly decreasing Fourier coefficients) or an explicitly
defined quotient of finite-window sequences.  No such quotient is defined.

Likewise, D12(b)'s universal `Theta(sqrt(|Lambda|))` bulk claim is false.  For
the `chi=1` product MPS, `AX` is proportional to the vacuum tensor, so at
`k != 0` its plane-wave sum is a bounded geometric sum, not `Theta(sqrt L)`,
even though `N_k` is injective.  The desired conclusion
`|Lambda|^{-1/2}Phi_k(N_k(X))->0` follows directly from the boundary **upper**
bound and does not need this false lower/growth claim.

Finally, the G0 row writes a fixed-momentum formula `Phi_k(...)` and then calls
it exact "for `c_0` profiles".  A plane wave is not in `c_0`; for a decaying
wave packet the correct statement is the Fourier superposition of the
`k`-dependent identities (or the real-space SBP identity), not the displayed
fixed-`k` equation.  These quantifiers/topologies must be separated before G0
can remain PROVED as written.

### 5. MAJOR — the claims DAG still does not match the proved quantifiers

**Locations:** `claims/CLAIMS.md` rows A1, A2, G0, B3.

* A1 says half-infinite strings have "no strongly convergent operator"
  without the theorem's condition `V_alpha(g)` non-scalar.  For a normal-
  ordered product vacuum on which `g` fixes the vacuum site vector, the finite
  strings do strongly stabilise on the dense finite-excitation subspace.  The
  row also includes the invalid window action of objection 1.
* A2 asserts `(G/H_alpha)^2` and the double-coset classification without the
  theorem's hypothesis that `G` acts transitively on the vacuum family.  D2
  permits several `G`-orbits.  The correct unconditional statement is per
  orbit, or the row must state transitivity.
* G0 contains the false/ill-typed D12 formulation of objections 3--4 and omits
  the unbroken/normal-ordering qualifier on its kinematic identity.
* B3 still says "memory is valued in the `A`-orbit of vacua", exactly the old
  classifying language that A2-orbit-r1 now marks REFUTED.  The amendment
  immediately below the table contradicts this row.

The WI row and the two new REFUTED/RETRACTED rows accurately report their
results.

### 6. MAJOR — retracted content is silently used in both named drafts

**Locations:** read-only audit; no edits made to either draft.

* `theory/spt-scoping-draft.md:132` calls `(e^{ik}-1)` an "exact lattice Adler
  zero", says its coefficient is already established by G0, and concludes
  every bulk soft amplitude vanishes linearly.  That is precisely
  G0-soft-r1, now RETRACTED: regularity/LSZ/current matrix elements are absent.
  Its edge claim at lines 236--252 also rereads A1 as an action on an edge
  Hilbert space, silently using the load-bearing split/GNS box that remains
  SKETCH.
* `theory/corner-b-draft.md:39,569,594--597` still uses a fixed `A`-orbit point
  and identifies memory with the `G_diag`-invariant label in
  `(G_L x G_R)/G_diag`.  In its `chi=1` unbroken `U(1)` product-vacuum setting,
  the repaired A1 has `N_alpha=G` and a one-point endpoint-state orbit, so the
  old `A ~= U(1)` state-orbit interpretation cannot be imported from A1.  A
  separately defined charge-transfer torsor may be viable, but it is not the
  retracted A2/A1 orbit claim.

These are drafts, so this objection does not disprove the repaired local A2
theorem; it does show that the retractions have not propagated through the
declared DAG/campaign.

### 7. MINOR — D9(c) mixes a definition with the A1 theorem it depends on

**Locations:** D9(c), A1 ASSUME/PROVE, A1 DAG dependencies.

The non-vacuous core is sound: define `E_b^alpha` as the endpoint-state set,
prove in A1(c) that it is `PGL(chi)`, and then derive the `G/N_alpha` orbit.
But D9(c) itself states the bijection, torsor theorem, extension pullback, and
obstruction while citing A1; A1 in turn lists D9 notation among its assumptions
and the DAG lists D9 as a dependency.  The proof does not actually rely on the
asserted consequences, so this is not fatal circularity.  Split D9(c) into the
bare definition/action and explicitly derived corollaries to make the DAG
acyclic.

### 8. MINOR — D1(e')'s positivity justification is not literally the stated vector

**Locations:** D1(e'), A2(b).

With full-rank matrix environments `l_alpha` and `r_beta`, a finite restriction
is generally a positive density-matrix contraction (or a vector only after
purifying the environments), not `⟨v|.|v⟩` for a window vector with the D1(e)
rank-one boundary vectors.  The construction can be made rigorous by writing
the CP contraction and its common normalisation, or by purification.  Its
consistency under enlarging the uniform left/right tails is otherwise correct,
and A2's weak-* limit also supplies positivity independently.  Thus the r1
limit-object objection is substantively fixed.

### 9. MINOR — `notation.md` retains the inverse convention that r2 rejected

**Locations:** `notation.md` rows for `V_b` and `A`.

The symbol table still defines `V_b(g)` as `V_b(V_alpha(g)^{-1})`, while D4(a)
and A1(d1) explicitly changed it to `V_b(V_alpha(g))`.  It also still calls
`A=(G_L x G_R)/G_diag` the lattice asymptotic symmetry group without the
abelian/faithful restriction, even though the appended rows and revision note
supersede it.  These are the exact inverse/group convention hazards r2 is
meant to remove, not harmless duplicate prose.

### 10. NOTE — the endpoint torsor and D1(e') do not repeat r1's vacuity

`E_b^alpha` is a genuine `PGL(chi)`-torsor once A1(c)'s scalar lemma is proved,
and the symmetry orbit `rho_alpha(G)` can range from one point (`chi=1`) to a
faithful finite orbit (the `Z_2 x Z_2` AKLT example).  The group dependence now
lives in the action rather than in the vacuous coset `V(g)GL(chi)`.  Similarly,
D1(e') is a separately constructed mixed-tail state rather than an illicit
finite decoration.  Apart from objections 7--8, neither new definition has
the r1 disease.

## Surviving r2 result

The repaired package now proves WI with the correct boundary/window
quantifier; the endpoint-state bijection and corrected `G/N_alpha` orbit; the
pointwise broken half-string sector jump with Jordan-safe rate; the
double-coset classification on each transitive vacuum orbit; the exact SBP
identity with boundary terms; the unbroken/broken tensor dichotomy; and the
finite-range continuity equation plus O1.  It still does not prove a physical
GNS charge algebra or a soft theorem, as the revision correctly concedes.

FAIL(A1,A2,G0,B3)
