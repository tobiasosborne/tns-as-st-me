# RESULT — the intrinsic 2+1 soft theorem is fusion-block/isotopy, not an Adler factor

**One sentence.**  In a fully gapped 2+1D fusion-categorical phase, every
`k→0` limit point of a tube-resolved, charge-created string-endpoint form
factor remains in the allowed fusion space `Hom(b,x⊗a)` and is flat under
contractible string isotopy up to categorical parallel transport, but the
category fixes no Taylor coefficient within that space; a universal
Ward/Adler factor requires genuinely infrared data such as a continuous
current and a Goldstone mode, a specified gapless edge theory, or another
gapless field.

This is a negative **RESULT with a positive residual**.  The finite no-go in
§3 says exactly what “category alone fixes no coefficient” means, and §4
computes it on a four-edge toric-code patch.  It does not say that a particular
Hamiltonian, edge CFT, or symmetry-enriched topological phase cannot have an
additional soft theorem.  It says that such a theorem is not an invariant of
the fusion category/tube sector data.

## 1. Formulation ledger

| candidate | verdict | decisive reason |
|---|---|---|
| 1. Soft phase/tension modulation of a bulk string | **DEAD as a category-only soft factor** | A scalar modulation `c(k)W_γ` preserves the string, its endpoint charge, and all pulling-through relations while giving an arbitrary analytic scalar `c(k)`.  Even after quotienting an overall phase, a coherent sum of equivalent paths or a local polarization rotation gives an arbitrary first nonzero magnitude coefficient.  The exact toric-code calculation is in §4. |
| 2. Gapless-edge soft mode | **LIVE PROGRAM, but extra structure** | On a finite PEPS region the bulk-boundary isometry turns a boundary perturbation into an edge Hamiltonian on the MPO-projected boundary register.  Pulling-through supplies the fusion-block selection rule for an incident bulk string.  A Ward soft factor additionally requires a specified gapless edge fixed point and its current/OPE normalization; the bulk category does not select that edge Hamiltonian or normalization. |
| 3. Gapped means no intrinsic energetic soft leg | **RESULT in the stated scope** | For a massive anyon, `k→0` need not imply `E(k)→0`; it is a long-wavelength source limit, not an on-shell soft-particle limit.  Analyticity or clustering may regularize the response, but does not quantize its Taylor coefficients.  The finite no-go proves the stronger data-insufficiency statement without assuming a thermodynamic expansion. |
| 4. 2D SSB Goldstone route | **LIVE, separate from topological order** | The correct first datum is the directional derivative `dF_0`, a covector on the tangent space of the Brillouin zone.  The lattice continuity equation fixes only its longitudinal contraction with the soft momentum.  Point-group, parity, and hard-momentum data may reduce that covector to scalars, but this consumes continuous Lie symmetry and gapless Goldstone kinematics, not fusion-category data. |
| 5. Non-invertible soft theorem | **RESULT only as an intertwiner constraint** | The replacement for a zero-mode Ward identity is homogeneous pulling-through: the resolved endpoint map lies in `Hom(b,x⊗a)` (with a multiplicity label `μ`) for every `k`.  Since the relation is homogeneous, multiplying an endpoint tensor by `c(k)` preserves it.  There is no inverse string or derivative at the identity from which to manufacture a current pole or a normalized soft factor. |
| 6. Braiding/monodromy as a “soft phase” | **DEAD as soft; alive as topology** | Adiabatically winding one endpoint around an anyon gives an `R`/monodromy action fixed by the braided category.  Its parameter is a path class or braid, not a momentum tending to zero.  Calling the topological braid phase a soft factor would only rename already-understood sector theory. |
| 7. Contractible string-shape deformation | **RESULT, but exact rather than soft** | Exact pulling-through gives a flat categorical transport between homotopic paths that avoid other insertions.  In the toric patch `W_1|Ω⟩=W_2|Ω⟩` exactly.  This is the honest symmetry-controlled string deformation; it has no small parameter or Taylor coefficient. |

The ledger separates three layers which otherwise get conflated:

1. **topological:** tube idempotents, fusion spaces, pulling-through, and
   braiding;
2. **kinematic:** a window, Fourier transform, normalization, and an actual
   `k→0` topology for the endpoint datum;
3. **infrared dynamical:** a gapless on-shell leg or edge mode, a current Ward
   identity, and the normalization that turns it into a number.

Fusion-category data determine layer 1.  They can constrain every limit point
once layer 2 is supplied.  They do not supply layer 3.

## 2. The right object and the surviving theorem

### 2.1 Tube-resolved endpoint form factor

Fix an MPO-injective PEPS phase with input category `C`.  For a bulk anyon
register use the tube/Drinfeld-center category `D=Z(C)`; for an endpoint on a
chosen physical boundary replace `D` by the corresponding boundary excitation
category.  This choice is part of the type of the statement.

Let `P_a` and `P_b` be the appropriate tube or boundary-sector projectors and
let `T_x(y;w)` be a windowed string-endpoint insertion of pure type
`x∈Irr(D)`, with endpoint position `y` along a chosen direction and with all
microscopic smearing data collected in `w`.  On a finite periodic boundary of
length `L`, define

`T_x(k;w)=Σ_{y=0}^{L-1} e^{iky} T_x(y;w)`, `k∈(2π/L)ℤ`,

and resolve a fusion basis

`F^{x,μ}_{ba}(k;w)=P_b T_x(k;w) P_a`,

where `μ` labels `Hom_D(b,x⊗a)`.  In an infinite-volume protocol, “soft” must
mean a declared sequence of windows and momenta together with a declared
operator, weak, or matrix-element topology.  A bare `k→0` before this choice
is under-specified.

This is the 2+1 analogue of the charge-created datum in the 1D playbook: the
string endpoint is pinned to the supplied charge type `x`, while `μ` records
the fusion channel.  It does not subtract anyon labels.

### 2.2 FUSION-SOFT, the positive residual

**THEOREM FUSION-SOFT (finite algebraic statement; limit conditional on
existence).**  Suppose the endpoint tensor is an exact pure `x` intertwiner.
Then, at every finite lattice momentum and for every window,

`P_b T_x(k;w) P_a=0` unless `Hom_D(b,x⊗a)≠0`.              **(S2D.1)**

Consequently every limit point of these blocks, in any topology in which the
fixed finite-sector projectors act continuously, obeys the same zero-block
constraint.

*Proof.*  Pulling-through makes each translated endpoint tensor a morphism in
the `x` action on the endpoint register.  Semisimplicity decomposes its
`(b,a)` block into `Hom_D(b,x⊗a)`, so a forbidden block vanishes.  Fourier
summing and windowing are linear and cannot create a forbidden block.  If a
net of forbidden blocks is identically zero, each of its limit points is zero.
□

The local TeX review supplies exactly the background used here: pulling-through
represents the tensor category and emerging anyons
(`refs/arxiv-2011.12127/TN-Review-main.tex:405`--`:408`), tube minimal central
idempotents give orthogonal topological sectors (`:1588`--`:1600`), and bulk
anyon pairs carry movable virtual MPO strings (`:1642`--`:1667`).  No quotation
from those sources is needed for (S2D.1); the theorem is the finite
semisimple-algebra consequence already isolated in `theory/cat-hunt.md`, now
applied before taking the soft limit.

### 2.3 SHAPE-FLAT, the actual string-deformation law

**THEOREM SHAPE-FLAT (conditional fixed-point/pulling-through statement).**
Let `γ` and `γ'` be string paths with the same resolved endpoints, related by
a finite sequence of contractible local pulling-through moves in a disk
containing no other insertion.  After identifying the endpoint fusion spaces
by the associator maps supplied by those moves, their code-projected endpoint
morphisms agree.  A closed path of moves can act nontrivially only when it has
nontrivial topological holonomy, for example by braiding around another anyon.

*Proof.*  One exact pulling-through equation identifies the two tensor
networks across one local move.  Compose these identities along the finite
move sequence.  Pentagon coherence makes two contractible compositions the
same categorical identification.  Moves around another insertion are not
contractible in its complement and instead compose to the corresponding
braid/monodromy action.  □

This is the clean answer to “what is the soft deformation of a charge-created
string?” at the topological fixed point: its intrinsic deformation is
categorical parallel transport under isotopy, and it is exactly flat rather
than asymptotically flat.  Momentum modulation is a different operation: it
chooses coefficients for microscopic string representatives or rotates their
local operator content.  Those coefficients are not fixed by SHAPE-FLAT.

The theorem is conditional on an exact MPO/string representation.  In a
generic Hamiltonian in the same phase, a quasi-adiabatically dressed string
and finite-correlation-length corrections require additional control; no
uniform error estimate is claimed here.

### 2.4 What (S2D.1) and SHAPE-FLAT do not say

It gives support, not a coefficient.  In a one-dimensional fusion space one
may write an allowed block as

`F^{x}_{ba}(k;w)=f^{x}_{ba}(k;w) I^{x}_{ba}`.              **(S2D.2)**

The intertwiner `I` is categorical; the scalar form factor `f` depends on the
endpoint tensor, window, Hamiltonian, external states, and normalization.  In
a higher-dimensional fusion space (S2D.2) becomes a vector of such functions,
and basis/gauge choices add another layer.  The category constrains how that
vector transforms under associators and braids, but not its momentum germ.

Thus the honest topological “soft theorem” is a selection theorem on every
limit point.  An Adler zero, pole, or universal derivative would be an
additional theorem about `f`.

## 3. A sharp category-only no-go

**THEOREM NO-CAT-SOFT.**  Fix any endpoint type `x`, source and target sectors
`a,b`, fusion channel `μ`, support geometry, and exact homogeneous
pulling-through/intertwiner equations.  Suppose a nonzero analytic family
`T_x(k)` satisfies those data near `k=0` and `T_x(0)≠0`.  Then those data, even
together with the fixed value `T_x(0)`, do not determine any positive-order
Taylor coefficient of its allowed form factor.

More precisely, for every analytic scalar `c(k)` with `c(0)=1`,

`\widetilde T_x(k)=c(k)T_x(k)`                            **(S2D.3)**

has the same endpoint type, sectors, channel, support, zero-momentum operator,
and homogeneous pulling-through equations.  Its `n`-jet can differ from that
of `T_x` for any chosen `n≥1`.  If norm preservation is imposed, the family
`c(k)=exp(if(k))` with real analytic `f(0)=0` leaves an arbitrary phase jet.

*Proof.*  Sector projection and every pulling-through/intertwiner equation are
linear and homogeneous in the endpoint tensor.  Multiplication by a scalar
therefore preserves them.  Taking `c(k)=exp(iαk^n)` preserves the norm and all
lower derivatives while changing the order-`n` derivative by
`iα n! T_x(0)`.  Since `α` is arbitrary, no positive-order coefficient follows
from the listed data.  □

Without fixing `T_x(0)`, the conclusion is stronger but simpler: both
`I^x_{ba}` and `kI^x_{ba}` obey the same homogeneous categorical equations in
an allowed one-dimensional channel.  Thus fusion data alone force an exact
zero only in the forbidden blocks of (S2D.1); they force neither an Adler zero
nor a nonzero constant in an allowed block.

This is deliberately a data-insufficiency theorem, not a theorem about every
possible normalization convention.  A convention can remove the scalar
freedom in (S2D.3), but then the convention is extra kinematic data and still
does not fix a measurable magnitude response.  Section 4 gives two explicit
ways to see the latter: interference between stabilizer-equivalent paths and
leakage under a unitary local rotation.  Both are normalized at `k=0` and have
arbitrary curvature in the same endpoint channel.

The theorem also explains why a bulk energy gap matters conceptually.  A
massive anyon remains separated from the ground register by a positive energy
as `k→0`, so this is not an energetic soft-particle limit.  It is a
long-wavelength limit of the chosen source.  The absent ingredient is
precisely the one that gives ordinary soft theorems their force: a gapless
on-shell state together with a Ward identity or factorization statement.
Neither a finite tube algebra nor its non-invertible pulling-through relation
contains a current zero mode.

## 4. Exact toric-code patch computation

The smallest useful calculation is one plaquette with four edge qubits.  It is
a finite `Z_2` quantum-double stabilizer patch, sufficient to retain path
independence and a resolved endpoint pair without thermodynamic assumptions.
The checker reproduces every value below directly in the sixteen-dimensional
Hilbert space.

### 4.1 Patch, ground state, and endpoint channel

Label the cyclic edges `(0,1,2,3)` and vertices so that

`A_0=X_0X_3`, `A_1=X_0X_1`, `A_2=X_1X_2`, `A_3=X_2X_3`,

`B=Z_0Z_1Z_2Z_3`, `H=-Σ_v A_v-B`.                         **(S2D.4)**

The star relation `A_0A_1A_2A_3=1` leaves four independent stabilizers in
four qubits, so the ground state is unique:

`|Ω⟩=8^{-1/2} Σ_{z: |z| even}|z⟩`, `H|Ω⟩=-5|Ω⟩`.          **(S2D.5)**

Take the two paths between opposite vertices

`γ_1={0,1}`, `γ_2={2,3}`, `W_i=∏_{e∈γ_i}Z_e`.              **(S2D.6)**

Their product is the plaquette stabilizer, `W_1W_2=B`.  Hence

`|χ⟩:=W_1|Ω⟩=W_2|Ω⟩`.                                    **(S2D.7)**

This state has star syndromes `(-,+,-,+)`, no plaquette violation, and energy
`-1`, i.e. two electric endpoint charges with excitation energy `4`.  The two
paths therefore realize the same one-dimensional fusion channel
`e⊗e→1`.  This is the finite stabilizer version of the movable virtual string
described in the local review at
`refs/arxiv-2011.12127/TN-Review-main.tex:1642`--`:1645`.

### 4.2 A slowly varying phase is arbitrary scalar dressing

Put coordinates `s_0,s_1` on the two edges of `γ_1` and define the wavelength
`1/k` phase profile

`W_1^{ph}(k;λ,c)=∏_{j=0}^1 exp[iλ sin(k(s_j+c))] Z_j`.

Since the phases are scalars,

`⟨χ|W_1^{ph}(k;λ,c)|Ω⟩`
`=exp{iλ[sin(k(s_0+c))+sin(k(s_1+c))]}`,                  **(S2D.8)**

and therefore

`∂_k A_ph(0)=iλ(s_0+s_1+2c)`.                             **(S2D.9)**

The endpoint syndrome, fusion channel, and amplitude magnitude are unchanged,
while the slope changes with the modulation strength and even with the origin
used to describe the same string.  Thus (S2D.9) is not an Adler coefficient;
it is probe convention.

### 4.3 Path interference leaves arbitrary magnitude curvature

To remove the objection that (S2D.9) is only an overall phase, coherently
modulate two stabilizer-equivalent strings:

`O_{λ,d}(k)=[W_1+exp(iλ sin(kd))W_2]/2`.                    **(S2D.10)**

It is normalized so that `O_{λ,d}(0)|Ω⟩=|χ⟩`.  Equation (S2D.7) gives the exact
endpoint amplitude

`A_{λ,d}(k)=[1+exp(iλ sin(kd))]/2`,

`|A_{λ,d}(k)|=|cos[(λ/2)sin(kd)]|`
`=1-(λ²d²/8)k²+O(k⁴)`.                                   **(S2D.11)**

Both route representatives, their endpoints, and their fusion channel are
topologically identical.  Yet the first phase-insensitive response coefficient
varies continuously with `λd`.  Setting `λ=0` also removes it completely.

### 4.4 A unitary local rotation gives the same verdict without path sums

On edge `j` replace `Z_j` by the Hermitian unitary

`Z_j(θ_j)=cos θ_j Z_j+sin θ_j X_j`,
`θ_j(k)=λ sin(ks_j)`,

and let `R_γ(k)=Z_0(θ_0)Z_1(θ_1)`.  Projection back onto the fixed electric
endpoint channel kills the three Pauli words containing at least one `X`, by
their different stabilizer syndromes.  Hence exactly

`⟨χ|R_γ(k)|Ω⟩=∏_{j=0}^1 cos[λ sin(ks_j)]`
`=1-(λ²/2)(s_0²+s_1²)k²+O(k⁴)`.                            **(S2D.12)**

This deformation is edge-local and norm-preserving before channel projection.
The channel amplitude, and therefore also its survival probability, has an
arbitrary leakage curvature.  Fusion says which channel was projected; it
does not fix the leakage rate.

Equations (S2D.8)--(S2D.12) kill candidate 1 in both of its natural readings.
An unprojected scalar phase gives convention-dependent linear response; a
phase-insensitive or locally rotated observable gives model/probe-dependent
quadratic response.  None has an Adler zero forced by the sector datum.

## 5. Edge soft modes: the finite statement and the missing input

For a PEPS on a finite region `R`, let `P_R` project onto the PEPS boundary
support and let `U_R` be the bulk-boundary isometry.  A weak boundary
perturbation `V_R` induces the low-energy edge Hamiltonian

`h_{∂R}=ε U_R V_R U_R†`                                    **(S2D.13)**

on that support.  This is the finite-lattice construction in the local TeX
review (`refs/arxiv-2011.12127/TN-Review-main.tex:822`--`:875`).  In a
topological phase the support is an MPO-projected subspace, and allowed edge
Hamiltonians retain the corresponding nonlocal superselection constraint.

Insert a bulk string of type `x` ending at boundary site `y` and Fourier sum
along a cylinder circumference.  The exact finite statement is still
(S2D.1): its matrix element between boundary sectors `a,b` vanishes unless
`Hom(b,x⊗a)` is nonzero.  If `h_{∂R}` is gapped, there is no sequence of
nonzero edge-energy eigenstates tending to zero at fixed Hamiltonian.  If it
is tuned to a gapless edge, a genuine soft problem exists, but its answer
depends on that one-dimensional edge theory.

For an edge with a continuous charge density `q_y` and current `j_y`, the
additional finite identity would have the ordinary lattice form

`[h_{∂R},q(k)]=(e^{ik}-1)j(k)`.                             **(S2D.14)**

After specifying edge states, amputation, and a controlled limit, (S2D.14)
can yield a Ward soft factor for the tube-resolved endpoint amplitude.  The
tube algebra tells which blocks of that identity are allowed; it does not
produce `q`, `j`, their normalization, the edge dispersion, or the limiting
matrix element.  In particular, pulling-through alone is not (S2D.14).

This is why “the soft theorem lives on a gapless edge” is a useful program but
not a theorem of the bulk category.  The review explicitly notes that varying
boundary perturbations can realize different edge phases without changing the
gapped bulk (`refs/arxiv-2011.12127/TN-Review-main.tex:855`).

## 6. SPECULATIVE — the 2D Goldstone and non-invertible programs

### 6.1 Goldstone route

For a two-dimensional ferromagnet, let `q=(q_1,q_2)` be the soft magnon
momentum and `p` the hard momentum.  If a charge-created, amputated form factor
`F(q;p)` is differentiable at `q=0`, its first soft datum is

`dF_0(p)=Σ_{i=1}^2 [∂_{q_i}F(0;p)] dq_i`,                  **(S2D.15)**

a covector in `T_0^*BZ`, not a scalar “slope” and not generically a coefficient
of `|q|`.  The vector lattice continuity equation

`[H,Q(q)]=Σ_i(e^{iq_i}-1)J_i(q)`                            **(S2D.16)**

controls the contraction of current form factors with `q_i`.  It does not by
itself determine both components of (S2D.15).  With rotations/reflections and
a single hard vector `p`, covariance can reduce the parity-even piece to a
coefficient multiplying `p·dq`; a parity-odd medium also permits
`ε_{ij}p_jdq_i`.  A small-patch two-magnon calculation should therefore test
these longitudinal and transverse coefficients separately.  An angular
average would discard the datum before the Ward identity acts.

This route is promising but is not the fusion-categorical answer: it restores
exactly the continuous broken charge and Goldstone leg absent from a gapped
topological phase.

### 6.2 Non-invertible route

For a genuine non-invertible `x`, the natural object is the vector

`F^x_{ba}(k)∈Hom_D(b,x⊗a)⊗K_{ba}(k)`,                     **(S2D.17)**

where `K` contains the ordinary kinematic/microscopic multiplicity.  `F` must
obey the associator/pulling-through coherence equations when several defects
are fused or moved.  Those equations can relate different channel components
and braid orderings.  They are the surviving replacement constraint.

They are not a soft factorization theorem: (S2D.17) admits multiplication by
an arbitrary scalar germ, as NO-CAT-SOFT shows, and fusion multiplicities can
admit additional vector freedom.  A non-invertible edge CFT may impose
crossing or defect-bootstrap relations on the remaining functions, but its
scaling spectrum and OPE coefficients are additional conformal data.  The
precise obstruction is therefore:

`no infinitesimal current + homogeneous defect relations`
`⇒ fusion-channel covariance, but no normalized momentum-soft coefficient`.

This respects the `cat-hunt` fence: no current zero mode has been smuggled out
of a tube idempotent, weak-Hopf integral, or non-invertible MPO.

## 7. Checker, status, and landing

Green command:

```bash
python3 -O theory/checks/soft_2d_hunt_check.py
```

Recorded green output:

```text
S2DH-C0-SHAPE PASS bare_asserts=0 optimized=1
S2DH-C1-GROUND PASS dim=16 stabilizers=4+1 E0=-5.0
S2DH-C2-ENDPOINT PASS paths=B-equivalent syndrome=-,+,-,+ gap=4
S2DH-C3-PHASE-FREEDOM PASS same_channel=1 slopes=1.000i,2.750i
S2DH-C4-PATH-CURVATURE PASS normalized=1 curvature_ratio=4.000000
S2DH-C5-ROTATION-CURVATURE PASS unitary=1 projected_curvature_ratio=4.000000
ALL SOFT-2D-HUNT GATES PASS
```

Registered red commands:

```bash
python3 -O theory/checks/soft_2d_hunt_check.py --red wrong-path
python3 -O theory/checks/soft_2d_hunt_check.py --red erase-probe-freedom
```

The first replaces `γ_2` by a non-equivalent one-edge path and exits `1` at
the endpoint/path gate (and at the dependent interference gate).  The second
removes the probe variation and exits `1` at all three advertised coefficient-
freedom gates.  These modes reach the content they are designed to mutate.
The checker contains no bare assertions.

Passing the checker establishes only the sixteen-dimensional stabilizer and
modulation arithmetic in §4.  The proofs in §§2--3 establish the finite
algebraic statements; the checker does not certify a thermodynamic endpoint
limit or a microscopic MPO-purity hypothesis.

**Honest status.**

- FUSION-SOFT is **PROVED as finite semisimple algebra**, conditional on a
  correctly typed pure endpoint intertwiner.  Its statement about limit
  points is conditional on their existence in the declared topology.
- SHAPE-FLAT is **PROVED from exact pulling-through/coherence**, conditional
  on the displayed fixed-point string representation and a deformation that
  avoids other insertions.  No dressed-string error bound away from the fixed
  point is claimed.
- NO-CAT-SOFT is **PROVED as a data-insufficiency theorem**.  It rules out a
  Taylor coefficient derived from category, channel, support, and homogeneous
  pulling-through data alone.  It does not rule out coefficients fixed by
  extra microscopic normalization or dynamics.
- The toric-code patch computation is **exact** and red-checked.
- The edge Ward construction and the two-dimensional Goldstone covector are
  **SPECULATIVE PROGRAMS**.  No edge CFT or 2D two-magnon coefficient is
  claimed here.
- No claim is made that every gapped response starts at `O(k)`.  A constant
  term, an arbitrary analytic correction, or a convention-dependent phase is
  compatible with the categorical data.  The conclusion is absence of a
  category-universal soft coefficient, not a universal order of vanishing.

### MERGE PROPOSALS

1. **2+1 corner map (recommended).**  Add a companion-paper `FUSION-SOFT`
   SKETCH row: tube-resolved endpoint form factors have support only in
   `Hom(b,x⊗a)` at every momentum and hence at every existing soft limit
   point; contractible path moves give exact categorical parallel transport;
   category data do not fix the scalar germ within an allowed block.  Cite
   §§2--4 and checker gates S2DH-C1--C5.
2. **Cat-hunt continuation.**  Extend the proposed 2+1 program seed of
   `theory/cat-hunt.md` by naming `F^{x,μ}_{ba}(k;w)` as the observable and
   NO-CAT-SOFT as the normalization obstruction.  Preserve its statement that
   the fusion event, not label subtraction, is the categorical datum.
3. **Gapless-edge work order.**  Treat a specified edge Hamiltonian and its
   current algebra as new input.  The first target should be the finite Ward
   identity (S2D.14) projected into tube/boundary sectors, followed by a thin-
   cylinder scaling test.  Do not advertise this as determined by the bulk
   category.
4. **No 1D claim changes.**  Nothing in this file alters any 1D CLAIMS row,
   and the 2D Goldstone covector in (S2D.15) is not evidence for the existing
   one-dimensional scalar-slope conjecture.

No merge is performed by this lane.
