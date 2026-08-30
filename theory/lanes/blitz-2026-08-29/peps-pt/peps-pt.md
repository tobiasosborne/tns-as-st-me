# Exact PEPS typing for the toric code

**Lane status:** **PROVED-candidate** for the exact toric-code PEPS instance,
before hostile review.  Section 5 is scoped separately; `SHAPE-FLAT` is untouched.

**Result.**  The fixed-point `Z_2` color-difference PEPS supplies (PT1)--(PT3)
exactly and its unitary ribbon also supplies (PT4).  Thus `A-INDEX-PEPS` has a
nonzero microscopic PEPS instance: on its annular tube register,

\[
 P_bT_xP_a=\delta_{b,a+x}T_xP_a,
 \qquad a,b,x\in Z_2^e\times Z_2^m.                 \tag{PTC.1}
\]

This is an exact selection theorem in a gapped topological model.  It is not a
radiative soft theorem, not a `2+1` displacement-memory claim, and not an
inference about `d=3` radiative/Coulombic fall-off.

## ⟨1⟩1. Canonical hypotheses and their proof roles

**ASSUME.**  Use (PT1)--(PT4) exactly as displayed in
`theory/anyon-label-index.md` §5 and as consumed by the claim row
`A-INDEX-PEPS`.

**PROVE.**  Record their exact content without strengthening them, and isolate
which conclusion consumes each one.

**⟨2⟩1. (PT1: tube PVM).**  A finite MPO-injective PEPS supplies an annular
representation of `Tub(C)` whose minimal central idempotents
`{P_a}_{a in Irr Z(C)}` are mutually orthogonal and sum to the identity on the
**chosen boundary-circle register**.

*Justification.*  PT1 is the measurement/register input.  It makes `P_b` a
genuine exhaustive sector measurement and lets orthogonality turn the
decomposition in PT3 into zero blocks.  “Chosen register” is load-bearing:
the sum need only be the identity on the tube/MPO-supported boundary space,
not on an unreduced raw virtual Hilbert space.  This is precisely the PT1
consumed by `A-INDEX-PEPS` and is checked here by `peps_pt_check.py`
`PEPS-PT-C4`.

**⟨2⟩2. (PT2: pure endpoint).**  A small-circle resolution of an endpoint
tensor `T_x` obeys

\[
 P_y^{\rm end}T_x=\delta_{y,x}T_x
\]

for one simple `x in Irr Z(C)`; a sum over distinct `x` is not pure.

*Justification.*  PT2 types the inserted endpoint before it meets the source
sector.  Without it, linearity would give a coherent sum of distinct fusion
rules rather than one categorical label.  This is the definite-label input of
`A-INDEX-PEPS`; both its virtual and microscopic toric realizations are checked
by `peps_pt_check.py` `PEPS-PT-C5` and `PEPS-PT-C3`.

**⟨2⟩3. (PT3: pulling-through module action).**  Exact zipper, associator,
and pulling-through equations identify the large-circle action of `T_x` on a
source sector `a` with

\[
 x\otimes a\cong\bigoplus_b
 \operatorname{Hom}(b,x\otimes a)\otimes b.       \tag{PTC.2}
\]

*Justification.*  PT3 is the selection-rule input.  It says which `b` blocks
exist and how a multiplicity label `mu` resolves them.  PT1 then annihilates
every absent block.  It is the only hypothesis that supplies the fusion
support in `A-INDEX-PEPS`; the pointed toric instance is checked by
`peps_pt_check.py` `PEPS-PT-C6`--`C8`.

**⟨2⟩4. (PT4: protocol instrument).**  The physical operation is either a
normalized channel-resolved Kraus family `T_{x,mu}`, or the protocol explicitly
postselects one displayed Kraus map and divides by its success probability.

*Justification.*  PT4 is not used to prove a zero block.  It is used only to
turn the nonnegative allowed weights into a normalized probability law (or a
conditional law).  Category data alone do not fix their values.  This is the
normalization fence in `A-INDEX-PEPS`; the toric ribbon supplies the stronger
unitary case at `peps_pt_check.py` `PEPS-PT-C9`.

**⟨2⟩5.**  Therefore PT1--PT3 are jointly load-bearing for the typed support
statement, whereas PT4 is load-bearing only for the instrument-normalization
clause.

*Justification.*  Remove PT1 and there is no exhaustive orthogonal register;
remove PT2 and no single `x` is selected; remove PT3 and no fusion support is
known.  Removing PT4 leaves the algebraic zeros unchanged but removes the
claim that weights sum to one.  This is exactly the dependency split in the
`A-INDEX-PEPS` claim row and is red-tested for PT2 by
`peps_pt_check.py --red pt2-mix`.

## ⟨1⟩2. Explicit fixed-point toric-code tensors

**ASSUME.**  Work on a finite connected square torus with one physical qubit
`s_e in Z_2` on every edge.  This is the same physical register as
`A-INDEX-TC-fin`.

**PROVE.**  Exhibit the fixed-point PEPS tensors and verify that their
contraction is a nonzero toric-code ground vector.

**⟨2⟩1.**  Put a virtual color in `Z_2` on each half-edge.  At every vertex use
the four-leg copy tensor and on every physical edge use the difference tensor

\[
 C_{lurd}=\begin{cases}1,&l=u=r=d,\\0,&\text{otherwise},\end{cases}
 \qquad
 D^s_{ab}=\delta_{s,a+b\ ({\rm mod}\ 2)}.          \tag{PTC.3}
\]

*Justification.*  These are explicit component arrays, not an implicit
diagrammatic convention.  After interchanging the square lattice with its
dual, they are the `Z_2` specialization of the standard dual-color quantum-
double PEPS (`refs/arxiv-2011.12127/TN-Review-main.tex`, lines 2452--2474).
Their component tables are checked by `peps_pt_check.py` `PEPS-PT-C0`.

**⟨2⟩2.**  Contracting every virtual half-edge gives

\[
 |\Omega_{\rm PEPS}\rangle
 =2^{-(|V|+1)/2}\sum_{g\in Z_2^V}
   \bigotimes_{e=(vw)}|g_v+g_w\rangle_e .          \tag{PTC.4}
\]

It is nonzero; on a `3 x 3` torus it has `2^8=256` nonzero computational-basis
amplitudes, all equal after normalization.

*Justification.*  The copy tensors force the four colors incident at `v` to
one value `g_v`; each difference tensor then forces
`s_e=g_v+g_w`.  The two colorings `g` and `g+1` give the same edge
configuration and are the only such pair on a connected graph.  The stated
normalization follows.  The full color sum is contracted by
`peps_pt_check.py` `PEPS-PT-C1`, which obtains 256 configurations with common
raw amplitude 2 and norm one.

**⟨2⟩3.**  The state (PTC.4) obeys every toric-code stabilizer

\[
 A_v|\Omega_{\rm PEPS}\rangle=|\Omega_{\rm PEPS}\rangle,
 \qquad B_p|\Omega_{\rm PEPS}\rangle=|\Omega_{\rm PEPS}\rangle. \tag{PTC.5}
\]

*Justification.*  `A_v` flips the four incident edge bits, which permutes the
summand indexed by `g` to the summand indexed by `g+delta_v`.  Around every
plaquette, the four differences telescope to zero, so every summand has
`B_p=+1`.  This is the fixed-point Hamiltonian register of
`A-INDEX-TC-fin`; `peps_pt_check.py` `PEPS-PT-C2` checks all 18 stabilizer
relations on the `3 x 3` vector with residual zero.

**⟨2⟩4.**  Hence (PTC.3) is an exact microscopic, nonzero fixed-point PEPS for
the toric code, not merely a four-sector abstract representation.

*Justification.*  The conclusion combines the explicit contraction of
⟨1⟩2.⟨2⟩2 with all Hamiltonian constraints in ⟨1⟩2.⟨2⟩3.  Its named
computation is `peps_pt_check.py` `PEPS-PT-C0`--`C2`, and its physical model
is the proved claim `A-INDEX-TC-fin`.

## ⟨1⟩3. Exact annular and endpoint registers

**ASSUME.**  Cut an annulus through `N>=1` virtual `Z_2` legs and use the
extended tube register

\[
 \mathcal H_{\partial,N}=(\mathbb C^2)^{\otimes N}\otimes\mathbb C^2_{\rm flux}.
\]

Write `Xbar=X^{otimes N}`.  The two components of a label
`a=(a_e,a_m)` are respectively the `Z_2` character and flux bits.

**PROVE.**  Supply PT1 and PT2, and identify the endpoint with the physical
ribbon of `A-INDEX-TC-fin`.

**⟨2⟩1.**  Define four annular operators

\[
 P_{(a_e,a_m)}={1\over2}
 \bigl(I+(-1)^{a_e}\overline X\bigr)
 \otimes |a_m\rangle\langle a_m| .                 \tag{PTC.6}
\]

They are precisely the normalized toric-code tube idempotents.

*Justification.*  The local source gives the unnormalized form
`(I^{otimes N} +/- X^{otimes N}) tensor |h><h|` for `h in {0,1}`
(`refs/arxiv-2011.12127/TN-Review-main.tex`, line 1637).  Equation (PTC.6)
adds the unique projector normalization.  This is the concrete toric
specialization of PT1 in `A-INDEX-PEPS` and is instantiated in
`peps_pt_check.py` `PEPS-PT-C4`.

**⟨2⟩2.**  The operators (PTC.6) are self-adjoint, obey
`P_aP_b=delta_{ab}P_a`, and sum to the identity of
`H_{partial,N}`.  Thus PT1 holds on the declared register.

*Justification.*  `Xbar` is a self-adjoint involution, so its two character
projectors are orthogonal and exhaustive.  The two flux rank-one projectors
are also orthogonal and exhaustive, and tensoring the two PVMs proves the
claim.  `peps_pt_check.py` `PEPS-PT-C4` checks every product and the complete
sum at `N=4`, all with residual zero; this is PT1 of `A-INDEX-PEPS`.

**⟨2⟩3.**  On `H_{partial,N}` define the ribbon crossing the circle by

\[
 T_{(x_e,x_m)}=Z_1^{x_e}\otimes X_{\rm flux}^{x_m}. \tag{PTC.7}
\]

For the vacuum cap

\[
 |t_0\rangle={|0^N\rangle+|1^N\rangle\over\sqrt2}\otimes|0\rangle,
 \qquad |t_x\rangle=T_x|t_0\rangle,                \tag{PTC.8}
\]

one has `P_y|t_x>=delta_{yx}|t_x>`.

*Justification.*  `Z_1` anticommutes with `Xbar` and therefore flips its
character eigenvalue; `X_flux` flips the flux bit.  The vacuum cap has
character `+1` and flux zero, so (PTC.8) has exactly label `x`.  This proves
PT2 in the virtual endpoint register of `A-INDEX-PEPS`; all 16 projection
relations are checked at `peps_pt_check.py` `PEPS-PT-C5`.

**⟨2⟩4.**  The virtual cap (PTC.8) is the boundary image of a microscopic pure
Pauli ribbon endpoint in the PEPS state (PTC.4).

*Justification.*  In the physical register, choose a one-cell disk and apply
`W_x=Z(gamma)^{x_e}X(gamma*)^{x_m}` with one endpoint of each active component
inside.  Claim `A-INDEX-TC-fin` gives
`P_y(D)W_x|Omega_PEPS>=delta_{yx}W_x|Omega_PEPS>` because (PTC.5) makes
`Omega_PEPS` a ground vector.  Independently, `peps_pt_check.py`
`PEPS-PT-C3` constructs the `3 x 3` state, applies a single-edge direct/dual
ribbon, and obtains all endpoint projection residuals equal to zero.  This
discharges PT2 microscopically rather than only naming an abstract tube vector.

## ⟨1⟩4. Pulling-through module action and normalized protocol

**ASSUME.**  Use the exact projectors (PTC.6), ribbon maps (PTC.7), and the
pointed fusion category
`Irr Z(Vec_{Z_2}) = Z_2^e x Z_2^m` of `A-INDEX-TC-fin`.

**PROVE.**  Discharge PT3, prove (PTC.1) with nonzero allowed blocks, and
discharge PT4.

**⟨2⟩1.**  The virtual ribbon maps satisfy the exact zipper and associator
relations

\[
 T_xT_y=T_{x+y},\qquad (T_xT_y)T_z=T_x(T_yT_z).     \tag{PTC.9}
\]

*Justification.*  The `Z_1` factor and flux-register `X` factor act on
different tensor factors, each squares to the identity, and their exponents
add modulo two.  Thus the zipper is literal matrix multiplication and the
associator is the identity.  Locally, (PTC.3) also obeys
`C_{l+g,u+g,r+g,d+g}=C_{lurd}` and `D^s_{a+g,b+g}=D^s_{ab}`, so the group
string pulls through every copy/difference tensor.  These are the PT3 inputs
of `A-INDEX-PEPS`; `peps_pt_check.py` `C0` and `C6` check them exactly.

**⟨2⟩2.**  Moving `T_x` through the annular idempotents gives

\[
 P_bT_x=T_xP_{b-x}.                                    \tag{PTC.10}
\]

*Justification.*  If `x_e=1`, `Z_1 Xbar=-Xbar Z_1`, so the character bit is
shifted; if `x_m=1`, `X_flux|h><h|=|h+1><h|`, so the flux bit is shifted.
The two effects commute.  Equation (PTC.10) is checked blockwise by
`peps_pt_check.py` `PEPS-PT-C7` and is the toric realization of PT3 in
`A-INDEX-PEPS`.

**⟨2⟩3.**  Right multiplication of (PTC.10) by `P_a` proves

\[
 P_bT_xP_a=\delta_{b,a+x}T_xP_a.                       \tag{PTC.11}
\]

*Justification.*  PT1 gives `P_{b-x}P_a=delta_{b-x,a}P_a`.  In the pointed
center,
`dim Hom(b,x tensor a)=delta_{b,x+a}`, so (PTC.11) is exactly the semisimple
decomposition (PTC.2), including its one-dimensional channel.  This is the
selection statement of `A-INDEX-PEPS`; `peps_pt_check.py` `PEPS-PT-C7`
checks every allowed and forbidden block with zero residual.

**⟨2⟩4.**  Every allowed block in (PTC.11) is nonzero.

*Justification.*  `T_x` is invertible and `P_a` has rank `2^{N-1}` on the
declared tube register, so
`||T_xP_a||_F=sqrt(2^{N-1})>0`.  At `N=4`,
`peps_pt_check.py` `PEPS-PT-C8` obtains the minimum allowed norm
`sqrt(8)=2.828427`.  Together with the nonzero microscopic state in
`PEPS-PT-C1` and pure endpoint in `C3`, this defeats the nonvacuity trap for
the toric PEPS instance of `A-INDEX-PEPS`.

**⟨2⟩5.**  PT4 holds with a single normalized Kraus map `T_x` (and, in the
physical register, the single Pauli unitary `W_x`).

*Justification.*  Equation (PTC.7) is a tensor product of Pauli unitaries, so
`T_x^dagger T_x=I`.  Therefore the same-circle weights summed over the PT1
PVM are normalized for every density matrix.  The physical `W_x` is likewise
unitary by `A-INDEX-TC-fin`.  `peps_pt_check.py` `PEPS-PT-C9` checks
unitarity and the total instrument weight for a full-rank density matrix with
residual zero.

**⟨2⟩6.**  PT1--PT4 are therefore simultaneously realized by the explicit
fixed-point toric-code PEPS, and the conditional theorem `A-INDEX-PEPS`
applies to it without an uninstantiated PEPS-typing premise.

*Justification.*  PT1 is ⟨1⟩3.⟨2⟩1--2, microscopic PT2 is
⟨1⟩3.⟨2⟩3--4, PT3 is ⟨1⟩4.⟨2⟩1--4, and PT4 is
⟨1⟩4.⟨2⟩5.  All are exercised in one implementation by
`peps_pt_check.py` `PEPS-PT-C0`--`C9`.  **QED for the toric-code PEPS
instance.**

## ⟨1⟩5. Generality: RFP string nets and finite-group G-injective PEPS

### ⟨2⟩1. Standard exact RFP string-net PEPS

**ASSUME.**  “RFP string-net PEPS” means the standard exact Levin--Wen/string-
net PEPS constructed from a finite unitary fusion category `C`, with its
faithful MPO-supported boundary map, unitary `F` symbols, zipper/pentagon
intertwiners, and exact pulling-through equation.  It does **not** mean an
arbitrary PEPS conjectured to be an RG fixed point.

**PROVE.**  PT1--PT3 hold for the canonical central-idempotent-resolved
endpoint construction; PT4 is extra protocol data.

**⟨3⟩1.**  PT1 holds on the MPO-supported annular register.

*Justification.*  The finite tube algebra is a finite-dimensional
`C*`-algebra.  In its faithful regular annular representation its minimal
central idempotents are nonzero, mutually orthogonal, and sum to its unit;
their simple labels are `Irr Z(C)`.  The local source states these algebraic
facts at `refs/arxiv-2011.12127/TN-Review-main.tex` lines 1587--1600.  This is
exactly PT1 as scoped in `A-INDEX-PEPS`, with the same supported-register
fence tested in the `Z_2` instance by `peps_pt_check.py` `PEPS-PT-C4`.

**⟨3⟩2.**  PT2 holds existentially and canonically for every simple `x`:
terminate the corresponding open MPO string with an endpoint in the nonzero
range of the minimal central idempotent `P_x`.

*Justification.*  Orthogonality gives `P_yP_x=delta_{yx}P_x`; hence every
nonzero endpoint vector/tensor in `ran P_x` is pure.  Faithfulness and
MPO-injectivity keep that supported endpoint nonzero under the PEPS boundary
map.  The standard source identifies these same idempotents with elementary
bulk excitations and attached virtual strings at
`refs/arxiv-2011.12127/TN-Review-main.tex` lines 1642--1666.  This supplies
the canonical PT2 required by `A-INDEX-PEPS`; it does not say that an
arbitrary user-chosen microscopic operator is pure.

**⟨3⟩3.**  PT3 holds for these canonical endpoints.

*Justification.*  The string-net MPO labels have nonnegative integral fusion,
the zipper tensors implement their products, pentagon is their associativity,
and exact pulling-through moves the attached string through every PEPS tensor.
The output anyon category is the Drinfeld center and its endpoint fusion is
therefore the decomposition (PTC.2); the local source records the zipper and
pentagon data at lines 1308--1338 and the output fusion at lines 1664--1669.
These are precisely the three structural inputs named by PT3 in
`A-INDEX-PEPS`; the component-level pointed specialization is independently
checked by `peps_pt_check.py` `PEPS-PT-C6`--`C8`.

**⟨3⟩4.**  PT4 does not follow from `C`, its `F` symbols, or the tube algebra.

*Justification.*  Fusion fixes the zero/nonzero channel pattern but not the
norms of microscopic preparation maps or their success probabilities.  A
particular finite endpoint map can be rescaled and used with explicit
postselection, but a deterministic normalized instrument is additional
physical data.  This is the explicit PT4 fence of `A-INDEX-PEPS`, illustrated
by the stronger unitary toric instance at `peps_pt_check.py` `PEPS-PT-C9`.

**⟨3⟩5.**  Consequently PT1--PT3 are structural for the standard exact RFP
string-net construction with its canonical resolved endpoints; PT4 is not.

*Justification.*  This is the conjunction of ⟨1⟩5.⟨2⟩1.⟨3⟩1--4 under the
displayed meaning of RFP string-net.  Extending it to **all** PEPS RG fixed
points is blocked: the local source explicitly says that a full intrinsic
characterization of PEPS RG fixed points has not been realized
(`refs/arxiv-2011.12127/TN-Review-main.tex`, lines 1020--1023).  The proved
conditional conclusion remains `A-INDEX-PEPS`.

### ⟨2⟩2. Finite-group G-injective PEPS

**ASSUME.**  Let `G` be finite and let the PEPS be `G`-injective in the
standard sense: exact regular virtual action and injectivity on the invariant
boundary support.  The PEPS may be away from the G-isometric fixed point; an
invertible physical filter may change norms and correlations while retaining
the exact virtual symmetry.

**PROVE.**  PT1--PT3 hold for the canonical `D(G)` central-idempotent-resolved
virtual endpoints; PT4 and purity of an arbitrary physical ribbon do not
follow.

**⟨3⟩1.**  PT1 holds with sectors `(C,pi)`, where `C` is a conjugacy class of
`G` and `pi` an irreducible representation of the centralizer of a
representative of `C`.

*Justification.*  Exact virtual pulling-through makes the enlarged MPO algebra
the Drinfeld double `D(G)`.  Its normalized minimal central idempotents form an
orthogonal PVM on the supported annular representation.  The explicit group
formula and label set occur at `refs/arxiv-2011.12127/TN-Review-main.tex`
lines 1600--1637.  This is PT1 of `A-INDEX-PEPS`; (PTC.6) and
`peps_pt_check.py` `PEPS-PT-C4` are its `G=Z_2` instance.

**⟨3⟩2.**  PT2 holds for the canonical resolved endpoint obtained by applying
one `D(G)` central idempotent to an endpoint of its attached virtual group
string.

*Justification.*  The central-idempotent equation gives
`P_y T_x=delta_{yx}T_x`, and `G`-injectivity prevents a nonzero vector in the
supported range from being killed by the physical boundary map.  The source's
`G`-injective anyon construction is recorded at lines 1642--1664.  This is
the PT2 input of `A-INDEX-PEPS`; `peps_pt_check.py` `PEPS-PT-C3` and `C5`
give both physical and virtual `G=Z_2` realizations.

**⟨3⟩3.**  PT3 holds for the canonical endpoint, with fusion in
`Rep D(G) congruent Z(Vec_G)`.

*Justification.*  Pulling-through gives the `D(G)` action on the annular
module; tensoring a simple endpoint representation with source representation
`a` decomposes semisimply into `Hom(b,x tensor a) tensor b`.  The source
identifies the enlarged algebra as `D(G)` at lines 1600--1637 and its anyon
fusion as the Drinfeld-center output at lines 1664--1669.  This is PT3 of
`A-INDEX-PEPS`; its pointed matrix form is checked by `peps_pt_check.py`
`PEPS-PT-C6`--`C8`.

**⟨3⟩4.**  Neither a deterministic PT4 instrument nor purity of an arbitrary
microscopic physical ribbon follows from `G`-injectivity alone.

*Justification.*  An invertible physical filter preserves exact virtual
sector zeros but changes endpoint norms; fusion data do not repair those
norms.  Moreover a generic physical operator can be a coherent sum of several
central-idempotent-resolved endpoints and then violates PT2.  A chosen
canonical endpoint can be physically implemented with a displayed
postselection protocol, but that protocol must be supplied.  This is the PT2
and PT4 scope of `A-INDEX-PEPS`, and the coherent-sum failure is detected by
`peps_pt_check.py --red pt2-mix`.

**⟨3⟩5.**  Thus finite-group `G`-injectivity supplies PT1--PT3 for the
canonical virtual `D(G)` endpoint construction, but not PT4 and not a claim
about every microscopic ribbon.

*Justification.*  This is the conjunction of ⟨1⟩5.⟨2⟩2.⟨3⟩1--4.  Mere
virtual `G`-symmetry without injectivity/faithfulness is insufficient: some
central blocks may be absent or mapped to zero, breaking the PT1 completeness
or PT2 nonzero-endpoint clauses.  The surviving conditional selection theorem
is exactly `A-INDEX-PEPS`.

### ⟨2⟩3. Scope table

| PEPS class and endpoint choice | PT1 | PT2 | PT3 | PT4 |
|---|---|---|---|---|
| Exact toric-code PEPS (PTC.3), Pauli/central-resolved ribbon | yes, explicit | yes, physical and virtual | yes, explicit pointed module | yes, unitary |
| Standard exact RFP string net, canonical tube-resolved endpoint | yes on MPO support | yes, existential for every simple | yes, zipper/pentagon/pull-through | not categorical; supply/postselect |
| Finite-`G` G-injective PEPS, canonical `D(G)` endpoint | yes on invariant support | yes for resolved endpoint | yes, exact virtual `D(G)` module | not automatic |
| Arbitrary physical endpoint operator in either general class | same PVM | **not necessarily**; may mix simples | only after resolving its simple components | not automatic |

*Justification.*  Each entry is the conclusion proved in ⟨1⟩4,
⟨1⟩5.⟨2⟩1, or ⟨1⟩5.⟨2⟩2.  The only unconditional microscopic row in this
shard is the toric-code row, exercised by `peps_pt_check.py` `PEPS-PT-C0`--
`C9`; the general rows retain exactly the canonical-endpoint and supported-
register scope of `A-INDEX-PEPS`.

## ⟨1⟩6. Binding `2+1` fences

**ASSUME.**  Retain the warnings in `theory/boundary-2d.md` and
`docs/2p1-antecedents.md`.

**PROVE.**  This is only categorical anyon selection/nonvacuity.

**⟨2⟩1.**  The shift `b=a+x` is fusion in the finite torsion group
`Z_2^e x Z_2^m`, not spatial displacement, domain-wall position, or memory;
the 2D charge/area warning remains intact.  Nonzero endpoint blocks in a
gapped toric code supply no radiative particle, Ward limit, or soft Taylor
coefficient, so the gapped `0=0` warning also remains intact.  Finally the
finite computation has no radial coordinate and draws no conclusion from the
inverted `d=3` radiative/Coulombic fall-offs.

*Justification.*  These exclusions are the three binding warnings, while the
positive content is exactly (PTC.11), `A-INDEX-PEPS`, and
`peps_pt_check.py` `PEPS-PT-C7`--`C8`.  **QED for the scoped claim.**

## ⟨1⟩7. Checker and registered mutation

Green: `python3 -O theory/lanes/blitz-2026-08-29/peps-pt/peps_pt_check.py`.
The saved `green.log` ends in `ALL PEPS-PT GATES PASS`; `C0`--`C9` have zero
residual except the positive liveness gate, whose allowed-block norm is
`2.828427`.

Red: append `--red pt2-mix` to that command.

It replaces the electric endpoint by an electric/magnetic coherent sum.
`C5-PT2-pure-endpoint` fails with residual `0.7071` and exit 1 while every
unrelated gate stays green; see `red-pt2-mix.log`.  There is no bare `assert`.

## ⟨1⟩8. Proposed claim-row disposition

Retain `A-INDEX-PEPS` at **PROVED** conditionally and, after hostile review,
add the exact toric PEPS discharge, making it unconditional on this instance.
`A-INDEX-TC-fin` needs no status change.  Do not yet promote a class-wide
RFP/G-injective statement: §5 has canonical-endpoint/supported-register scope
and PT4 is extra data.  `SHAPE-FLAT` and memory/soft rows remain untouched.
