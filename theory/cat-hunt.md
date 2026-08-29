# RESULT — the categorical soft datum is a fusion channel, with an invertible or universal-grading index; the Ward operator theorem remains Lie

**One sentence.**  For an MPO phase described by a fusion category
`C` **and a chosen boundary/module register** `M`, a pure string endpoint is
labelled in the phase-dependent endpoint category
`D_M=Fun_C(M,M)` and can connect `a` to `b` only through a fusion channel
`Hom(b,x⊗a)`; when `x` is invertible this gives the group-valued index `x`,
while for non-invertible `x` its maximal functorial group shadow is the
universal-grading shift `|b||a|^{-1}=|x|`, but neither datum supplies the
Lie-current Ward relation or its Gram inverse.

**Landing.**  This belongs in a **companion paper** as a small theorem plus an
operator/categorical split, with at most a discussion paragraph in the present
campaign.  The Letter is full.  It is not a proposed replacement or relabelling
of `SPT-E'`, `SPT-T'`, or `SPT-D'`.

The positive content passes the binding non-artificial test in route (a):
§4 computes the non-invertible Ising fusion endpoint exactly, and the same
checker computes the `Rep(Q_8)` central-character grading and the pointed
`Vec_G`/electric-character reduction.  The Ising charge `σ` has a definite
odd index even though `σ⊗σ=1⊕ψ` has two fine targets.  No current row in
the present corpus covers that statement.

## 1. Hunt ledger

| candidate | verdict | decisive reason |
|---|---|---|
| 1. Subtract simple tube/Drinfeld-center labels | **DEAD as stated** | `Irr Z(C)` is a fusion set, not a group.  If `N_{xa}^b>0` for several `b`, there is no canonical quotient `b/a`; Ising gives the exact obstruction `σ⊗σ=1⊕ψ`.  A tube label is also a 2+1D bulk label; a 1D boundary can condense, identify, or split it, so `C` without boundary/module data is under-typed. |
| 2. Endpoint-module fusion channel | **RESULT (fine statement)** | Once a phase register `M` is fixed, an `x`-type endpoint has the exact selection rule `P_bT_xP_a=0` unless `Hom(b,x⊗a)≠0`.  The honest fine datum is `(x,a→b;μ)`, not a subtraction. |
| 3. Invertible endpoint index | **RESULT** | If `x` is invertible, `x⊗a` is simple and the target is unique.  The index is the supplied charge object `x∈Inv(D_M)`.  In the pointed group-MPO/electric register this is `χ∈Hom(G,U(1))`; for abelian `G` it is the full group character group (the torus extension is the usual character lattice). |
| 4. Universal-grading soft index | **RESULT (coarse statement)** | Every simple of a fusion category is homogeneous for its universal grading.  Hence every summand `b⊂x⊗a` obeys `|b|=|x||a|`, even when `x` is non-invertible.  This is the maximal group grading compatible with all fusion channels and reduces in `Rep(H)` to the central-character difference, restricted to `\widehat{Z(H)/K_u}` in the effective physical register. |
| 5. Tube idempotent / weak-Hopf integral as the Gram inverse | **DEAD as an operator replacement** | Tube central idempotents and weak-Hopf/Haar conditional expectations project superselection blocks.  They recover the categorical selection rule, but they do not relate two independent operators in the same block, do not imply `D†J=R`, and do not make `D†D` invertible. |
| 6. Jones--Wenzl projector as the descendant projector | **PARTIAL ONLY** | In categories admitting it, a Jones--Wenzl projector selects a fusion summand.  It may model a sector projector, but `P_{ran D}` can be strictly finer than the whole target summand and its normalization is not the root-`sl_2` ladder coefficient. |
| 7. Categorical finite-string Ward identity | **RESULT only for the endpoint-defect half** | For invertible on-site strings, locality gives the exact G5 endpoint defect.  General MPO pulling-through gives a defect/intertwiner equation after endpoint tensors are specified.  A non-invertible MPO has no conjugation `U_R†HU_R`, and neither identity differentiates to a current zero mode inside a finite fusion category. |
| 8. One theorem making S-IDX-G-label, G5-C2-FINITE, and SPT-E' full corollaries | **NO** | They share endpoint covariance/pulling-through, but have different extra inputs: central grading, Hamiltonian locality, and a fixed MPS transfer/edge register respectively.  Combining those hypotheses under one header would be packaging, not a new theorem. |

The surviving result is therefore a **proved split**: fusion-category data
control which endpoint sectors and fusion channels are allowed; the normalized
projected-current identity additionally consumes a differentiated continuous
symmetry and root-representation algebra.

## 2. Correct typing: the phase is `(C,M)`, not `C` alone

### 2.1 MPO and endpoint categories

Let `C` be a finite unitary fusion category represented by exact MPOs.  The
local tensor data include the fusion/zipper intertwiners and their associator.
The local-TeX source
`refs/arxiv-2011.12127/TN-Review-main.tex:1308`--`:1338` records precisely the
needed structure: MPO blocks have nonnegative integral fusion coefficients,
the zipper comes from the MPS fundamental theorem, and the physical/virtual
realisation is controlled by a bimodule category.

A phase or boundary register must also be chosen.  Denote it by the
indecomposable `C`-module category `M`.  The category of topological endpoint
charges on that register is the dual fusion category

`D_M := Fun_C(M,M)`.                                             **(CAT.1)**

For the regular module, `D_M` is `C^rev`.  For another module it can be a
different Morita representative.  Thus a statement assigning endpoint labels
from `C` alone is not invariantly typed.  This is not cosmetic: the local TeX
exhibits the group-element and irrep MPO descriptions as different bimodule
realisations of the same quantum-double data
(`refs/arxiv-2011.12127/TN-Review-main.tex:2465`--`:2480`).

In a finite endpoint register write `P_a` for the projector onto the simple
sector `a in Irr(D_M)`.  A **pure endpoint of type `x`** means an endpoint
intertwiner resolved into one simple `x in Irr(D_M)`.  A general endpoint is a
sum of such components and has no single index.  The purity hypothesis is the
categorical analogue of the hypothesis in `S-IDX-G-label` that the displayed
component spans a definite central-character line.

### 2.2 D1 scope

The statement is blockwise on D1-class MPS vacua and their exact MPO
intertwiners.  It does **not** assume that one injective MPS block is invariant
under every non-invertible MPO.  Indeed the local-TeX review explains that a
nontrivial MPO associator can obstruct such a uniform injective invariant MPS,
leaving criticality or a symmetry-broken ground-space representation
(`refs/arxiv-2011.12127/TN-Review-main.tex:1397`--`:1419`).  For a broken
phase, `M` and its simple objects keep track of the vacuum blocks and domain
walls.  The algebraic theorem below applies to that resolved register.

This clause matters for the Ising computation: it is an exact non-invertible
MPO/fusion-algebra instance, not a claim that the critical Ising ground state
is an injective finite-bond MPS.

### 2.3 Why the tube algebra is optional in 1D and native in 2+1D

The tube algebra is a finite `C*` algebra whose minimal central idempotents
label `Irr Z(C)`; this is the PEPS/topological-sector construction stated in
`refs/arxiv-2011.12127/TN-Review-main.tex:1588`--`:1600`.  One may therefore
apply the theorem below with `D=Z(C)` **after** projecting an operator with a
tube idempotent.  But this is a bulk 2+1D register.  On a chosen 1D boundary,
bulk labels can condense, identify, or split, and the boundary category
`D_M` is the correctly typed label set.  A bare Drinfeld-center label is not
automatically a 1D endpoint label.

## 3. The categorical soft-index theorem

### 3.1 Fine fusion-channel statement

**THEOREM CAT-SIDX (conditional physical theorem; algebraic core proved).**
Let `(C,M)` and `D=D_M` be as in §2.  Let `T_x` be a pure endpoint operator
of simple type `x in Irr(D)`, acting from a resolved source sector `a`.  Then

`P_b T_x P_a = 0 unless N_{x a}^b > 0`,                       **(CAT.2)**

and a nonzero block carries a fusion-channel vector

`μ in Hom_D(b,x⊗a)`.                                          **(CAT.3)**

Thus the fine categorical soft datum is

`Ind_cat(T_x;a→b) := (x,a,b;μ)`,                              **(CAT.4)**

with the basis of the multiplicity space suppressed only when it is
one-dimensional.  There is no subtraction operation on `Irr(D)` in general.

*Proof.*  The zipper/pulling-through tensor makes the endpoint register a
module over the fusion algebra of `D`.  Its `(b,a)` multiplicity for the
action of `x` is, by semisimplicity,
`dim Hom_D(b,x⊗a)=N_{xa}^b`.  A block outside that direct-sum support is
zero, proving (CAT.2); a nonzero resolved block is exactly a choice in (CAT.3).
This proves (CAT.4).  The physical antecedent is the declared exact MPO
intertwiner and sector resolution; the conclusion is finite semisimple
algebra, not a thermodynamic or scattering assertion.  □

### 3.2 Invertible and universal-grading shadows

Let `Inv(D)` be the group of invertible simple objects.  If `x in Inv(D)`,
tensoring by `x` is an equivalence with inverse `x*`.  Hence it takes a simple
`a` to a simple `x⊗a`; the target in (CAT.2) is unique.  In this case define

`Ind_inv(T_x;a) := x in Inv(D)`.                                  **(CAT.5)**

The operator type `x` is part of the datum.  It need not be reconstructible
from the ordered pair `(a,b)` if the `Inv(D)` action has a stabilizer.

For arbitrary, possibly non-invertible `x`, define the universal grading group
`U(D)` by generators `[a]` for `a in Irr(D)` and relations

`[1]=e`, `[a*]=[a]^{-1}`, and `[c]=[a][b]` whenever `N_{ab}^c>0`.

Write `|a|` for the resulting degree.  Every nonzero channel in (CAT.2)
satisfies

`|b|=|x||a|`, and hence

`Ind_U(T_x;a→b):=|b||a|^{-1}=|x| in U(D)`.                 **(CAT.6)**

*Proof.*  The first equality is one of the defining relations because
`N_{xa}^b>0`; right multiplication by `|a|^{-1}` proves (CAT.6).  If `q(a)` is
any other group-valued assignment satisfying
`N_{ab}^c>0 => q(c)=q(a)q(b)`, the displayed presentation gives a unique
homomorphism `U(D)→G_q` taking `|a|` to `q(a)`.  Therefore (CAT.6) is the
maximal **grading-valued** quotient that survives every fusion channel.  It
does not claim that `U(D)` replaces the finer invertible-object label (CAT.5).
□

This two-level answer is necessary.  Invertible electric charges can remain
distinct even when their universal degree agrees, whereas a non-invertible
charge is not itself an element of any fusion group.  The Q8 computation in
§4.3 displays both facts in one algebra.

### 3.3 Exact reduction to `S-IDX-G-label`

Take `D=Rep(H)` first for finite `H`.  If `V` is irreducible and
`z in Z(H)`, Schur's lemma gives a central character `γ_V(z)` by

`V(z)=γ_V(z) I`.

If `W` is a summand of `X⊗V`, then

`γ_W(z)=γ_X(z)γ_V(z)`.                                  **(CAT.7)**

The central-character decomposition is faithful: restricting the regular
representation of `H` to `Z(H)` contains every character of `Z(H)`, so every
central character occurs in some `H`-irrep.  Its neutral component is
`Rep(H/Z(H))`, generated by summands of `V⊗V*`.

For completeness, maximality can be seen without guessing a grading.  In any
fusion category, a character of `U(D)` acts by its scalar on every homogeneous
simple and thereby gives a tensor automorphism of the identity functor; the
converse follows from simplicity and monoidality.  Hence
`Aut_⊗(id_D)=\widehat{U(D)}`.  For `D=Rep(H)`, Tannaka reconstruction identifies
tensor automorphisms of the identity with central group elements: `z` acts on
every representation by `V(z)`, while naturality and monoidality force every
such family to arise this way.  Finite Pontryagin duality now gives the
universal grading, in the superselection-label convention,

`U(Rep(H)) = \widehat{Z(H)}`                                    **(CAT.8)**

Some mathematical sources report the abstract (generally noncanonical)
isomorphism type as `Z(H)`; (CAT.8) is the canonical character label that acts
on superselection sectors and is the one required here.

Now let the on-site representation be `u` and

`K_u={z in Z(H):u(z) in U(1)I}`.

Every operator object in the conjugation representation is trivial on `K_u`.
Thus its degree belongs to the annihilator

`K_u^⊥={χ in \widehat{Z(H)}:χ|_{K_u}=1}`
` ≅ \widehat{Z(H)/K_u}`.                                      **(CAT.9)**

Equations (CAT.7)--(CAT.9) say exactly that an `X`-type operator sends
`γ` to `γχ_X`, and that the quotient of target and source labels is
`χ_X`.  This is `S-IDX-G-label` (H.32)--(H.34), including its effective
centre; it applies separately to `Q_X` and `J_X` once their displayed global
covariance makes both pure objects of the same type.  The proof extends
directly to the central-character decomposition of a compact group
representation; connected central tori give the integer
character lattice and disconnected components give torsion.  A compact Lie
representation category is not a finite fusion category, so this last sentence
is a rigid-tensor-category extension, not a misuse of the word “fusion.”

Nothing here upgrades the descendant projector:

`P_{ran T_x P_a} <= sum_{b:N_{xa}^b>0} P_b`.                    **(CAT.10)**

This is the categorical version of the strict fence (H.37).

### 3.4 Pointed `Vec_G` reduction and the character group

For an untwisted pointed MPO category `C=Vec_G`, choose the rank-one symmetric
module `M=Vec`.  Its dual endpoint category is

`D_M=Fun_{Vec_G}(Vec,Vec) ≅ Rep(G)`.                         **(CAT.11)**

An invertible pure-electric endpoint is a one-dimensional representation
`η:G→U(1)`.  Tensoring sends every sector `a` to the unique sector
`η⊗a`, so (CAT.5) becomes

`Ind_inv=η in Hom(G,U(1))`.                                 **(CAT.12)**

This is the requested group character group.  When `G` is finite abelian, all
electric simple sectors are one-dimensional and (CAT.12) is the complete
pointed answer `\widehat G`; for a compact torus the same argument gives its
character lattice.  When `G` is nonabelian, only the invertible electric
subsector is `Hom(G,U(1))`.  A non-invertible electric irrep instead obeys the
fusion-channel statement and its universal degree is its central character.

That last distinction is binding.  For example,
`Hom(S_3,U(1))=Z_2` while `Z(S_3)` is trivial.  Therefore no single
unqualified phrase “the character group” can simultaneously mean the
invertible endpoint label (CAT.12) and the `Rep(G)` universal grading
(CAT.8) for nonabelian `G`.

If one instead chooses the regular module for `C=Rep(G)`, then
`D_M≅Rep(G)^rev`, and (CAT.8)--(CAT.9) give the effective-centre characters.
Thus both reductions requested in the work order hold, but only after the
module/Morita register is displayed.

## 4. Exact computed instances

All values in this section are reproduced by
`theory/checks/cat_hunt_check.py` using integer fusion matrices and the integer
character table of `Q_8`.

### 4.1 Pointed anchor: `Vec_{Z/2}`

The rank-one module has dual endpoint category `Rep(Z/2)` with simples
`1,ε`.  In the ordered basis `(1,ε)`, the nontrivial electric character has
left-fusion matrix

`N_ε = [[0,1],[1,0]]`, `N_ε^2=I`.                         **(CAT.13)**

It swaps the two endpoint sectors uniquely.  Hence its finite endpoint index is
the nontrivial character `ε in \widehat{Z/2}`, exactly as (CAT.12) requires.

### 4.2 Non-invertible anchor: Ising fusion

Use simples `(1,ψ,σ)` and exact fusion rules

`ψ⊗ψ=1`, `ψ⊗σ=σ`, `σ⊗σ=1⊕ψ`.                  **(CAT.14)**

Left multiplication by `σ` is

`N_σ = [[0,0,1], [0,0,1], [1,1,0]]`,
`N_σ^2=I+N_ψ`.                                            **(CAT.15)**

The positive fusion dimension obeys `d_σ^2=2`.  The universal grading is
`Z_2` with

`|1|=|ψ|=0`, `|σ|=1`.                                     **(CAT.16)**

Every fusion channel respects addition mod two.  In particular, a `σ` endpoint
acting on a `σ` source has **two** fine targets, `1` and `ψ`, so the proposed
simple-label difference does not exist.  Both targets are even, however, and

`|target|-|σ|=1 mod 2=|σ|`.                                **(CAT.17)**

This is actual non-invertible content: the categorical soft index is odd while
the tube/simple-sector readout branches.  The local-TeX review ties these exact
fusion rules to the transverse-field Ising MPO symmetry
(`refs/arxiv-2011.12127/TN-Review-main.tex:1386`--`:1397`).

### 4.3 `Rep(Q_8)`: character index and effective-centre index are different

The five irreducible characters of `Q_8` are four lines
`1,a,b,c` and one two-dimensional irrep `ρ`.  On the conjugacy classes
`(1,-1,{±i},{±j},{±k})`, with sizes `(1,1,2,2,2)`, the exact character
table used by the checker is

| irrep | `1` | `-1` | `±i` | `±j` | `±k` |
|---|---:|---:|---:|---:|---:|
| `1` | 1 | 1 | 1 | 1 | 1 |
| `a` | 1 | 1 | 1 | -1 | -1 |
| `b` | 1 | 1 | -1 | 1 | -1 |
| `c` | 1 | 1 | -1 | -1 | 1 |
| `ρ` | 2 | -2 | 0 | 0 | 0 |

Character orthogonality gives

`ρ⊗ρ=1⊕a⊕b⊕c`, `η⊗ρ=ρ` for every line `η`.   **(CAT.18)**

There are now two different correct indices:

1. The invertible electric endpoints form
   `Inv(Rep(Q_8))=Hom(Q_8,U(1))≅Z_2×Z_2`.  Their action has a unique
   target, even though all four fix the sector `ρ`; the operator label `η`, not
   the pair `(ρ,ρ)`, retains the character index.
2. The universal/effective-centre grading is `Z_2`: the four lines have
   central character `+1` on `-1`, while `ρ` has `-1`.  Thus the
   non-invertible `ρ` endpoint is odd and `ρ⊗ρ` branches into four even
   fine targets, exactly as (CAT.6) predicts.

For the physical representation `u=1⊕ρ`, the central action is
`diag(1,-1,-1)`, so `K_u={1}` and the odd operator blocks
`Hom(1,ρ)` are visible.  For `u=ρ` alone, `-1` acts as the scalar `-I`, so
`K_u=Z(Q_8)` and the effective centre is trivial; correspondingly
`End(ρ)=ρ⊗ρ*` contains only the four even lines.  This is an exact check of
the effective-centre quotient, not merely an abstract character-table example.

## 5. The operator half: exact split from the Lie theorem

### 5.1 What is category-independent

For any finite-dimensional linear map `D`, with Moore--Penrose inverse on its
support,

`P_{ran D}=D(D†D)^+D†`.                                        **(CAT.19)**

Therefore, if an **additional** Ward relation supplies

`D†Jψ=Rψ`,                                                   **(CAT.20)**

then

`P_{ran D}Jψ=D(D†D)^+Rψ`.                                  **(CAT.21)**

This polar identity is ordinary Hilbert-space algebra.  Calling `P_{ran D}` a
categorical projector does not make (CAT.20) categorical.

In `S-IDX-fin-G`, (CAT.20) is the differentiated Ward relation

`Q(E_α)J(F_α)ψ=J(H_α)ψ`,

using both `[Q(E_α),J(F_α)]=J(H_α)` and `Q(E_α)ψ=0`.  The root
`sl_2` decomposition then proves positivity of `D†D` and, in the separately
highest-weight register, the scalar ladder value.  A fusion category contains
neither a derivative at the identity nor the primitive/root commutator that
produces `R`.

### 5.2 Why the three proposed categorical replacements stop short

**Conditional expectation / weak-Hopf integral.**  Haar averaging in a group
or its weak-Hopf analogue gives idempotent Fourier projections onto invariant
or charged blocks.  Tube central idempotents do the same for `Z(C)`.  These
objects prove (CAT.2) and its tube version.  They do not constrain two
independent morphisms `D` and `J` inside the same block, hence do not imply
(CAT.20).

**Jones--Wenzl projector.**  Where defined, it removes lower fusion channels or
selects a simple summand.  It can realise one `P_b` in (CAT.10).  It is not the
range projector of an arbitrary microscopic charge-created map, and its
categorical trace/quantum dimension is not the eigenvalue of `D†D` on a hard
state.

**Weak-Hopf integral as a ladder.**  An integral is an averaging/idempotent
object, not a primitive infinitesimal generator.  Rescaling a nonzero endpoint
intertwiner leaves its simple label and every fusion coefficient unchanged but
rescales `D†D`.  Likewise two current operators in the same homogeneous block
can differ by an arbitrary scalar.  `CATH-C4` checks the two-dimensional
`Z_2` register explicitly: `D`, `J_1=D`, and `J_3=3D` all have the same odd
categorical covariance, but their projected vectors differ by `1:3`; replacing
`D` by `2D` changes the Gram value by `1:4` without changing any category data.

This is a data-insufficiency proof, not a claim that no model-specific
categorical Hamiltonian can enjoy an extra Ward identity.  Such an identity
must be supplied as extra algebra/dynamics; it is not a theorem of fusion data.

### 5.3 Relation to the finite-string endpoint identity

For an invertible on-site group string, `U_R` is unitary and locality permits

`U_R†HU_R-H = (left endpoint defect)+(right endpoint defect)`.        **(CAT.22)**

G5-C2-FINITE computes (CAT.22) exactly for `Z_2`.  It is the group-like
endpoint-defect theorem.

For a non-invertible MPO `O_x`, the expression `O_x† H O_x-H` is not a
conjugation and is not fixed by the fusion category.  Pulling-through can still
give an intertwining equation whose bulk terms cancel and whose unzipped ends
carry defect tensors.  That equation depends on the chosen MPO representation,
fusion channel, and Hamiltonian.  It is the categorical continuation of the
**string endpoint** half, not of the current-zero-mode derivative.

The final split is therefore:

| ingredient | categorical? | surviving statement |
|---|---|---|
| sector/tube projector | yes | (CAT.2), (CAT.6), or a tube-idempotent block |
| finite invertible string endpoint | yes, with locality and an MPO realisation | endpoint defect (CAT.22) |
| polar range formula | no special symmetry needed | (CAT.19) |
| Ward relation `D†Jψ=Rψ` | **not from fusion data** | extra continuous-symmetry/dynamical input |
| invertibility and scalar ladder value of `D†D` | **Lie/root representation data** | `S-IDX-fin-G` only |

Thus `S-IDX-G-label` is the categorical half of the campaign.  The normalized
Gram-inverse/current theorem is genuinely Lie under the hypotheses presently
known.

## 6. Relation to the existing SPT endpoint rows

The common mechanism is exact endpoint intertwining, not a common numerical
soft theorem.  In `SPT-E'`, pulling a finite group string through a fixed MPS
and cancelling the remote endpoint leaves the virtual action `V_C(g)`; its Lie
derivative, when there is a Lie group and the declared limit exists, yields the
centered edge operator.  `SPT-T'` and `SPT-D'` then retain the projective
composition law.  The group-MPO literature likewise identifies edge degrees
of freedom and anomalous edge actions
(`refs/arxiv-1412.5604/SPT.tex:81`--`:86`).

CAT-SIDX may be applied **after** those endpoint operators are resolved into
simple/homogeneous charge components.  It then supplies their fusion selection
rule.  It does not supply any of the following inputs of `SPT-E'`:

- the fixed transfer compression and operator-norm endpoint limit;
- the projective multiplier or shifted charge offset;
- (H-split) from the Schmidt register to a physical half-chain edge;
- (H-dress) or a nonzero matrix element;
- deformation constancy of the centered offset, which `SPT-E'` explicitly does
  not claim.

Conversely, `SPT-E'` does not turn a non-invertible fusion relation into label
subtraction.  This is why the hunt does not relabel or restate any SPT row.

There is also no honest one-theorem unification of all three signal artifacts.
The common diagram is a string with endpoints, but:

- `S-IDX-G-label` uses covariance and superselection;
- G5-C2-FINITE uses Hamiltonian locality and invertibility of the string;
- `SPT-E'` uses a fixed MPS transfer register, compensation, and a limiting
  endpoint contraction.

Putting those hypotheses into one omnibus statement would make three clauses
under one name, not make any clause a corollary of the other two.

## 7. SPECULATIVE — visible 2+1D lift

In an MPO-injective PEPS/string-net phase, use the tube category
`Z(C)` for bulk anyons or the appropriate boundary excitation category after a
boundary/condensate is chosen.  A charge insertion of type `x` incident on an
anyon `a` can exit in `b` only with

`V_{x a}^b := Hom(b,x⊗a) != 0`.                              **(CAT.23)**

The proposed 2+1D “soft index” should therefore be the resolved fusion event
`(x,a→b;μ)`, or a probability distribution on the fusion space if the process
does not resolve `μ`.  For an abelian anyon `x`, this collapses to the ordinary
group-valued shift.  For a nonabelian anyon it does not; the universal degree
`|x|` is only a conserved coarse label.  Tube-algebra central idempotents give
the native projectors, and boundary conditional expectations give their
condensed images.  These ingredients survive the lift without inventing a
global group.

A plausible memory statement is then: after an anyon crosses or terminates on
a gapped boundary, the boundary superselection sector changes through an
allowed module-fusion channel, and the retained record is the final boundary
sector (or its universal degree).  Nonzero transition probabilities, their
soft scaling, and persistence still require dynamics.

The following parts of the present 1D construction are genuinely 1D-only and
must not be silently lifted:

- the division of the chain into two ordered half-lines and cancellation of a
  single remote cut endpoint;
- the MPS transfer-channel compression and its one-dimensional ordering;
- the derivative-before-window current-zero-mode limit;
- the root-`sl_2` ladder and Gram inverse;
- any two-body left/right scattering interpretation.

In 2+1D these must be replaced by boundary fusion/condensation data, tube
idempotents, and a separately specified spacetime scattering or adiabatic
protocol.  The categorical selection theorem survives; the present operator
soft theorem does not automatically do so.

## 8. Checker

Green command:

```bash
python3 -O theory/checks/cat_hunt_check.py
```

Recorded green output:

```text
CATH-C0-SHAPE PASS bare_asserts=0 optimization_safe=1
CATH-C1-POINTED PASS Vec_Z2 dual=Rep_Z2 index=sign targets=unique
CATH-C2-ISING PASS sigma_dim=sqrt(2) sigma_degree=odd sigma*sigma=one+psi fine_targets=2
CATH-C3-REP-Q8 PASS central_grades=4+1 rho*rho=4_even electric_characters=Z2xZ2 Ku_mixed=1 Ku_pure=Z2
CATH-C4-OPERATOR-SPLIT PASS same_degree_currents=2 projected_ratio=1:3 gram_scale=1:4
ALL CAT-HUNT GATES PASS
```

Registered red command:

```bash
python3 -O theory/checks/cat_hunt_check.py --red missing-ising-channel
```

It deletes the `ψ` output from `σ⊗σ`.  The run exits `1` at the independent
associativity check (`psi*sigma`), before it can pass the advertised
two-target gate.  The checker contains no bare assertions.

Passing this checker proves only the displayed finite fusion/character
arithmetic.  CAT-SIDX's algebraic proof carries the theorem; no finite check
proves that an arbitrary microscopic endpoint tensor is pure or that a
thermodynamic endpoint limit exists.

## 9. Honest status and MERGE PROPOSALS

**Status split.**

- CAT-SIDX's fusion-channel and universal-grading implications are **PROVED
  here as finite semisimple algebra**, conditional on the displayed exact MPO
  endpoint/module representation.
- The identification of a given microscopic D1 model's operator with a pure
  `x` endpoint remains a **model-specific obligation**.
- The Ising, pointed `Z_2`, and `Rep(Q_8)` fusion computations are **exact**.
- The 2+1D subsection is **SPECULATIVE**.
- No claim is made that category data imply a current, scattering limit, or
  nonzero amplitude.

Because this artifact has not undergone the campaign's capped hostile review,
any corpus row should enter at **SKETCH**, despite the elementary proof and
red-capable checker.

### MERGE PROPOSALS

1. **Companion-paper theorem (recommended).**  Add a `CAT-SIDX` SKETCH row:
   for a resolved MPO phase `(C,M)`, a pure endpoint `x` connects `a` to `b`
   only through `Hom(b,x⊗a)`; invertible `x` gives an `Inv(D_M)` index and
   general `x` gives the universal-grading index
   `|b||a|^{-1}=|x|`.  Cite this file §§3--4 and checker CATH-C1--C4.
2. **General-`G` discussion paragraph.**  Say that `S-IDX-G-label` is the
   `D=Rep(H)` universal-grading/central-character reduction, whereas
   `S-IDX-fin-G` additionally requires a differentiated symmetry and root
   ladder.  Do not place this in the full Letter unless space is reopened.
3. **SPT cross-reference only.**  In a companion discussion, point from the
   compensated `SPT-E'` endpoint register to CAT-SIDX for categorical selection
   rules.  Make no change to the status, hypotheses, or deformation scope of
   `SPT-E'`, `SPT-T'`, or `SPT-D'`.
4. **2+1D program seed.**  Register the resolved fusion event (CAT.23), not a
   difference of anyon names, as the proposed PEPS/anyon observable.  Require a
   chosen boundary/condensate before converting bulk tube labels to endpoint
   labels.

No existing file is edited by this work order, and no merge is performed here.
