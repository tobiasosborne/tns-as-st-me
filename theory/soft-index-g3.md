# REPRODUCTION-ONLY — general-`G` soft index, G3 moment-map route

**STATUS: REPRODUCTION-ONLY.**  For every root of the identity component of a
compact on-site group, the Fubini--Study moment map proves the exact statement
`mu_T([F_alpha psi]) - mu_T([psi]) = -alpha` whenever `psi` is a weight vector
and `F_alpha psi != 0`.  It does **not** prove the current-projection identity
S-IDX-fin.  Recovering that identity requires importing exactly its algebraic
current-covariance and polar-projection inputs, so this route adds no
generality and stops here under PRD.md's negative-results rule.

The provenance constraint of `briefs/bta-kahler-target.md` section 0.1 is
binding: the TNS Kaehler/TDVP observation recorded there is not paper prose and
is not attributed here.  Nothing in this shard proposes an edit to `paper/`.

## 1. Setup — the finite projective state manifold

### <1>1. Standing finite-volume data

**ASSUME.**  Let `G` be a compact group, `G^0` its identity component, and
`U_N : G -> U(H_N)` the finite-dimensional unitary representation induced by
the on-site action on a finite periodic ring.  Let `H_N` be any finite-range
`G`-invariant Hamiltonian in the D10 register.  Fix a maximal torus
`T subset G^0`, its Lie algebra `t`, and the weight decomposition

`H_N = direct-sum_{lambda in Lambda_N} H_lambda`.

The proof below uses the Hamiltonian only in the final comparison with
S-IDX-fin.  The moment map and its quantized root step depend only on `U_N`.
Finite groups and the disconnected quotient `G/G^0` have no infinitesimal
moment map; they may permute the weights but supply no soft lowering operator.
Central torus factors of `G^0` have weights but no roots, hence no root soft
leg.  The nontrivial statement is therefore root-wise on the semisimple part
of `Lie(G^0)`.

*Justification.*  D2 fixes the compact on-site action and D10 the finite-range
invariant Hamiltonian/current register.  The finite ring makes `H_N`
finite-dimensional.  The component and torus qualifications are scope, not
additional dynamics.

### <1>2. Fubini--Study moment map and normalization

On `P(H_N)` use the Fubini--Study form.  For a nonzero vector `v`, define the
moment map by

`<mu([v]), xi> := <v, (-i dU_N(xi)) v>/<v,v>`,  `xi in Lie(G^0)`.       (G3.1)

Thus the torus component `mu_T` is measured in the same Hermitian-charge
normalization as the representation weights.  If
`v = sum_lambda v_lambda` is its orthogonal weight decomposition, then

`mu_T([v]) = sum_lambda p_lambda lambda`,
`p_lambda := ||v_lambda||^2 / sum_gamma ||v_gamma||^2`.                 (G3.2)

**PROVE.**  Equation (G3.2), and consequently
`mu_T(P(H_N)) = conv(Lambda_N)`.

**<2>1.**  Every Hermitian torus charge is diagonal on the mutually
orthogonal weight spaces.  Its normalized expectation in `v` is therefore
the probability-weighted sum in (G3.2).

*Justification.*  Finite-dimensional spectral theory applied simultaneously
to the commuting torus charges.

**<2>2.**  Equation (G3.2) puts every image point in `conv(Lambda_N)`.
Conversely, for probabilities `p_lambda`, choose unit vectors
`e_lambda in H_lambda` and `v=sum_lambda sqrt(p_lambda)e_lambda`; (G3.2)
returns the prescribed convex combination.

*Justification.*  <2>1.  This proves the needed convexity directly; no
Kirwan/Guillemin--Sternberg theorem is being imported from memory.

**<2>3. QED.**

### <1>3. Register warning: a sector is not a `G`-manifold

For a fixed weight `lambda`, the torus acts projectively trivially on
`P(H_lambda)`, so `mu_T` is the constant `lambda` there.  A root operator maps
`H_lambda` to another sector, and the full group generally does not preserve
`P(H_lambda)`.  Therefore the relevant Hamiltonian `G^0`-manifold is the full
`P(H_N)`, stratified by weights, **not** the projective space of one sector.
Likewise, a fixed-bond-dimension MPS family can replace `P(H_N)` only after one
proves it invariant under the required action; no such invariance follows from
D1--D5 or Corner A.

*Justification.*  The weight decomposition in <1>1 and D5's warning that
finite-dimensional ansatz families carry their own gauge/register
conditions.  This is the finite-volume version of the family-invariance fence
in `briefs/bta-kahler-target.md` sections 5.3 and 5.5.

## 2. Ladder — what geometry proves and where it stops

### <1>4. THEOREM G3-MM-fin — the quantized postselected root step

**ASSUME.**  In <1>1, let `alpha` be a root, let `F_alpha` be a nonzero
complexified root-lowering operator normalized so that

`F_alpha H_lambda subset H_{lambda-alpha}`,

and take nonzero `psi in H_lambda` with `F_alpha psi != 0`.

**PROVE.**

`boxed(mu_T([F_alpha psi]) - mu_T([psi]) = -alpha)`.          (G3.3)

The increment is an exactly quantized element of the root lattice, independent
of the weight multiplicity, `H_N`, volume, and normalization of `psi` or
`F_alpha`.

**<2>1.**  Applying (G3.2) to the one-weight vector `psi` gives
`mu_T([psi])=lambda`.

*Justification.*  <1>2.

**<2>2.**  By the defining root-weight property in the ASSUME block,
`F_alpha psi` lies wholly in `H_{lambda-alpha}`.  Applying (G3.2) again gives
`mu_T([F_alpha psi])=lambda-alpha`.

*Justification.*  <1>2 and `F_alpha psi != 0`.

**<2>3.**  Subtraction proves (G3.3).  Multiplicity never entered: every
vector in `H_lambda`, and its entire nonzero `F_alpha` image, has the same
torus moment value.

*Justification.*  <2>1--<2>2.

**<2>4. QED.**

### <1>5. The increment is not a Hamiltonian symmetry translation

The exact step (G3.3) concerns the **postselected vector** `F_alpha psi`.
`F_alpha` lies in the complexified Lie algebra and is not, by itself, an
anti-Hermitian generator of the compact `G^0` action.  Along the normalized
projective curve

`[psi_t] := [psi + t F_alpha psi]`,

orthogonality of distinct weights gives

`mu_T([psi_t]) = lambda - p(t) alpha`,
`p(t) = |t|^2 ||F_alpha psi||^2 /
        (||psi||^2 + |t|^2 ||F_alpha psi||^2)`.               (G3.4)

For finite nonzero `t`, `p(t)` is generally strictly between `0` and `1`.
Thus the moment map changes continuously, not in quanta, along the geometric
curve.  The quantized value appears only after selecting the pure lowered
weight component.  A compact group orbit instead obeys coadjoint covariance
`mu(g.[psi])=Ad_g^*mu([psi])`; it does not translate `mu` by a root.

*Justification.*  Apply (G3.2) to the two orthogonal weight components.  The
last statement follows directly from (G3.1) and
`dU(g) dU(xi) dU(g)^{-1}=dU(Ad_g xi)`.

### <1>6. The S-IDX rung and the exact missing inputs

To compare with S-IDX-fin, fix `lambda` and define, in its **full-sector
register**,

`D_alpha := F_alpha|_{H_lambda}`,
`A_alpha := D_alpha^dagger D_alpha` on all of `H_lambda`,
`P_alpha := projection onto ran(D_alpha)`.                         (G3.5)

At a single ray `[psi]`, the complexified root-orbit tangent is only
`C F_alpha psi`.  By contrast, `ran(D_alpha)` contains `F_alpha phi` for
**every** `phi in H_lambda`; it can include arbitrary representation and
multiplicity directions.  Therefore `P_alpha` is not the Fubini--Study
projection onto the `G_C`-orbit tangent at `[psi]` except in a special
one-dimensional source sector.

Two inputs, neither contained in (G3.1)--(G3.4), would be needed:

1. **(ALG-POS)** `A_alpha` is invertible on the full weight sector, so
   `P_alpha=D_alpha A_alpha^{-1}D_alpha^dagger`.
2. **(ALG-WARD)** for the root-current component `J_{-alpha}` and
   `psi in K_{lambda,alpha}:=ker(E_alpha) intersect H_lambda`,

   `D_alpha^dagger J_{-alpha} psi = J_{H_alpha} psi`,             (G3.6)

   where `E_alpha=F_alpha^dagger`, `H_alpha=[E_alpha,F_alpha]`, and
   `J_{H_alpha}` uses the same Chevalley normalization.

If these algebraic inputs are imported, one line gives

`P_alpha J_{-alpha}psi
 =D_alpha A_alpha^{-1}J_{H_alpha}psi`.                        (G3.7)

This is the general-root analogue of FIN.1.  But (ALG-POS) is the root-string
positivity statement, (ALG-WARD) is adjoint covariance of the D10 current,
and (G3.7) is the Moore--Penrose/polar projection.  Calling `A_alpha` a
pullback Fubini--Study Gram form changes no premise and proves no new case.

*Justification.*  Equation (G3.7) follows by substituting (G3.6) into the
projector in (ALG-POS).  Conversely, the moment map contains only normalized
expectations of the symmetry generators; it contains neither the
Hamiltonian-dependent current vector `J_{-alpha}psi` nor the operator-valued
Gram form on the entire multiplicity sector.  Scaling or changing the
`G`-invariant Hamiltonian changes the current while leaving (G3.1)--(G3.4)
unchanged.  Thus these inputs cannot be recovered from the moment image.

### <1>7. The highest-weight-restricted register does not repair G3

Define `D_hw:=F_alpha|_{K_{lambda,alpha}}` and let `Pi_hw` be the orthogonal
projection onto `K_{lambda,alpha}`.  Importing the further algebraic identity

`D_hw^dagger D_hw = lambda(H_alpha) I`                       (G3.8)

and remembering that the adjoint of a restricted-domain map contains the
source projection gives

`P_hw J_{-alpha}psi
 = [1/lambda(H_alpha)] F_alpha Pi_hw J_{H_alpha}psi`.          (G3.9)

Equation (G3.9), not the hybrid expression with `Pi_hw` omitted, is the
general geometric restatement of FIN.2.  The ML4-Ward ERRATUM remains fully
active: `J_{H_alpha}psi` need not be in `K_{lambda,alpha}` when other hard
content is present.  The moment-map value `lambda` is scalar on the whole
sector and therefore cannot detect this register leakage.

*Justification.*  The restricted projector is
`D_hw(D_hw^dagger D_hw)^{-1}D_hw^dagger`, while
`D_hw^dagger J_{-alpha}psi=Pi_hw E_alpha J_{-alpha}psi
=Pi_hw J_{H_alpha}psi` under (ALG-WARD).  This is exactly the
restricted-adjoint mechanism in S-IDX-fin <1>3.<2>5 and the corrected
ML4-Ward CLAIMS row.

### <1>8. Weyl walls and rank greater than one

Equation (G3.2) makes the finite torus moment image the convex hull of the
weights.  In a chosen dominant chamber, the simple-root walls are
`lambda(H_alpha)=0`, and Weyl covariance permutes the weights and the root
steps.  For a simple reflection,

`s_alpha(lambda)=lambda-lambda(H_alpha)alpha`.                (G3.10)

Consequently a **single** lowering step equals a Weyl reflection only when
`lambda(H_alpha)=1`; in general the reflection is the far endpoint of a
multi-step root string.  Non-orthogonal roots give different edges from the
same weight and are not one scalar index.  The moment polytope organizes
these possibilities but does not relate the distinct current projections
(G3.7).

*Justification.*  The reflection formula is the definition of the Weyl
action in coroot normalization.  The convex-hull statement was proved in
<1>2.  No rank-one reduction or multiplicity decomposition is used here.

**Source audit.**  The work order points to “Weyl-wall rows” in
`theory/corner-a.md`.  In the present workspace that file contains no literal
`Weyl`, `wall`, `weight`, or `polytope` row.  Its usable general-`G` results
are instead the endpoint action/charge algebra A1 and D10/G0 current
registers; neither supplies (G3.6).  This shard therefore proves (G3.10)
directly and proposes no nonexistent Corner-A citation.

### <1>9. Comparison with M-INDEX-fin

The resemblance to M-INDEX-fin is exact only at the level “integral charge
data give an integral difference.”  The objects and protocols differ:

- M-INDEX-fin compares two outcomes of the same self-adjoint finite-window
  wall charge.  Its one-coset offsets cancel in a TPM protocol even though the
  two Heisenberg-time operators need not commute.
- G3-MM-fin compares two pure projective rays, `[psi]` and
  `[F_alpha psi]`, after a nonunitary complexified lowering and no time
  evolution or measurement protocol.
- M-INDEX-fin's increment is an integer in a selected circle normalization;
  G3-MM-fin's increment is a root in `t^*`.  Equating them needs a chosen
  circle/coroot pairing and a physical identification of the two protocols.

Thus “memory quantum = moment-map increment” is a useful target phrase but is
not a consequence of either theorem in this finite soft-index register.

*Justification.*  Claim M-INDEX-fin, especially its adjudicated statement
that integrality comes from fixed-window offset cancellation rather than the
spectrum of a difference operator; <1>4--<1>5 above.

## 3. SU(2) reduction

### <1>10. Moment-map reduction

Take `G=SU(2)`, `F_alpha=S^-`, `E_alpha=S^+`, and
`H_alpha=[S^+,S^-]=2S^z`.  A spin-weight-`m` vector has
`lambda(H_alpha)=2m`; the positive root obeys `alpha(H_alpha)=2`.  Therefore
(G3.3) says

`mu_{S^z}([S^-psi])-mu_{S^z}([psi])=-1`,                  (G3.11)

or equivalently `Delta mu_{H_alpha}=-2`.  This is precisely the unit
zero-mode magnon charge.  It is weaker than every displayed current identity
FIN.1--FIN.3.

*Justification.*  Substitute the SU(2) normalization into <1>4.

### <1>11. Algebraic reconstruction gives FIN.1 and FIN.2, not a new proof

Under the SU(2) identifications,
`J_{H_alpha}=2J^z_0`, `J_{-alpha}=J^-_0`, and (G3.7) becomes

`P J^-_0 psi = 2D A^{-1}J^z_0 psi`,

which is FIN.1.  Equation (G3.9) becomes

`P_hw J^-_0 psi
 = [1/(2m)]S^- Pi_hw(2J^z_0)psi
 = (1/m)S^- Pi_hw J^z_0psi`,

which is FIN.2.  FIN.3 additionally needs the D10 continuity equation and the
model-specific one-magnon statement `J^z_0|h>=iv_S(h)|h>`; neither is encoded
in `mu`.  The cancellation of `m` in the residue also uses the descendant norm
`||S^-|h>||^2=2m`, i.e. (G3.8).

*Justification.*  S-IDX-fin <1>3, especially <2>5--<2>8, and the ML4-Ward
ERRATUM.  This calculation explicitly demonstrates reproduction rather than
an independent route.

## 4. A genuinely beyond-SU(2) instance: the fundamental SU(3) ring

### <1>12. Exact finite instance

Let `H_N=(C^3)^{tensor 3}` with basis labels `1,2,3`, and take the periodic
SU(3)-invariant permutation Hamiltonian

`H=sum_{x=1}^3 (I-P_{x,x+1})`,  with `x+1` periodic.             (G3.12)

Use the two Hermitian Cartan charges

`H_1=diag(1,-1,0)`,  `H_2=diag(0,1,-1)`,

summed over the three sites, and simple lowerings
`F_1=sum_x |2><1|_x`, `F_2=sum_x |3><2|_x`.  Put

`psi=(|112>-|121>)/sqrt(2)`.                                  (G3.13)

Then

`(H_1,H_2)psi=(1,1)psi`, `E_1psi=E_2psi=0`, `H psi=3psi`,

and direct application gives

`F_1psi=(|212>-|221>)/sqrt(2)`,  moment `(-1,2)`,
`F_2psi=(|113>-|131>)/sqrt(2)`,  moment `(2,-1)`.               (G3.14)

Thus the increments are
`-alpha_1=(-2,1)` and `-alpha_2=(1,-2)` exactly.  Since the Dynkin labels of
`psi` are `(1,1)`, these one-step descendants also equal the two simple Weyl
reflections `s_1(1,1)=(-1,2)` and `s_2(1,1)=(2,-1)`.  This equality with a
reflection is special to label `1`; <1>8 records the general distinction.

**<2>1.**  The three-site Hamiltonian diagonalizes with eigenvalues and
multiplicities `0^10`, `3^16`, `6^1`.  The vector (G3.13) lies in the
energy-three eigenspace and is killed by both positive simple-root operators.

*Justification.*  Named computation **G3-C1**.

**<2>2.**  Independent expectation-value contractions give the three moment
values in (G3.14), and the two descendant weights are orthogonal.

*Justification.*  Named computation **G3-C2**.

**<2>3.**  Along `[psi+tF_1psi]` at `t=1/2`, the moment is `(0.6,1.2)`, with
`p(t)=0.2`, so the interpolation is visibly not an integral jump even though
its postselected endpoint is.

*Justification.*  Equation (G3.4); named computation **G3-C3**.

**<2>4. QED.**

## 5. Checker

### <1>13. Scope and red mode

`theory/checks/soft_index_g3_check.py` is an optimization-safe NumPy exact-
diagonalization certificate.  Run

```text
python3 -O theory/checks/soft_index_g3_check.py
python3 -O theory/checks/soft_index_g3_check.py --red
```

The first command exits `0`.  The second mixes `F_1` with `F_2` while keeping
the pure `-alpha_1` target and exits `1`; the mixed descendant occupies two
weight spaces and its moment is a strict convex combination, so this mutation
tests the purity condition that makes (G3.3) quantized.

The gates are:

| gate | content | evidence scope |
|---|---|---|
| **G3-C0** | no bare Python `assert`; strict under `python3 -O` | checker shape only |
| **G3-C1** | SU(3) invariance, ED spectrum, selected energy/highest-weight residuals | instance (G3.12)--(G3.13) |
| **G3-C2** | both simple-root moment increments and root-weight orthogonality | G3-MM-fin on the instance |
| **G3-C3** | continuous nonquantized coherent interpolation | fence against “Hamiltonian-flow quantum” |
| **G3-C4** | integral tensor weights, Weyl reflections, wall crossings | rank-two geometry on the instance |

The checker does **not** test (ALG-POS), (ALG-WARD), (G3.7), a soft limit, a
memory TPM law, or a general theorem.  Its green run is evidence for the
explicit SU(3) instance only; the proof of G3-MM-fin is <1>4.

*Justification.*  Named computations **G3-C0--C4** and the registered
`--red` mutation.

## 6. MERGE PROPOSALS

### <1>14. Claims row — optional narrow positive row

If the hybrid adjudication wants to retain the geometric fact, append this
row at **SKETCH** (this reproduction-only shard does not request promotion):

> | G3-MM-fin | On the finite projective state space of a unitary
> representation of compact `G`, for every root `alpha`, weight vector
> `psi in H_lambda`, and nonzero postselected descendant `F_alpha psi`, the
> torus Fubini--Study moment map obeys
> `mu_T([F_alpha psi])-mu_T([psi])=-alpha`.  The statement is independent of
> multiplicity and the Hamiltonian.  It is not S-IDX-fin: the lowering is a
> complexified nonunitary direction, a coherent interpolation has continuous
> moment value, and the current projection still requires root-current
> covariance plus full-sector polar algebra. | SKETCH | D2, D10 |
> theory/soft-index-g3.md <1>4--<1>9 |
> soft_index_g3_check.py G3-C0--C4 (SU(3) instance only; `--red` mixes roots) |

No S-IDX-fin general-`G` row is proposed from G3.

### <1>15. Notation proposals

Only if G3-MM-fin is retained, append rows for:

- `mu_T`: torus component of the finite-volume Fubini--Study moment map,
  normalized by Hermitian on-site charges as in (G3.1);
- `F_alpha,E_alpha,H_alpha`: complex root lowering/raising and coroot triple
  local to a selected root; these symbols must not overwrite D2's vacuum
  label `alpha` or the D28 Hamiltonian symbols;
- `Lambda_N`: the finite-ring weight set.

No definition-number proposal is needed: all three are local finite-
representation notation, and promoting them to `definitions.md` would make a
reproduction-only route look load-bearing.

### <1>16. Brief/source correction proposal

The parent brief should not cite “`theory/corner-a.md` (Weyl-wall rows)” in
this checkout.  Replace that pointer with the actual future source if another
parallel lane creates one, or say that Weyl-wall language is campaign context
and must be proved locally.  This shard used the latter discipline in <1>8.

### <1>17. Hybridization rule

A surviving algebraic general-`G` proof may use G3 only for the interpretation
that primitive root lowering moves the torus moment value by one root.  It may
not cite G3 for:

1. invertibility or scalarity of `D_alpha^dagger D_alpha`;
2. current covariance or the coefficient in (G3.6);
3. omission of `Pi_hw`;
4. a finite-group or central-torus soft leg;
5. identification with M-INDEX-fin or a memory observable.

Those five fences are the material output of this route.

### <1>18. Terminal assessment

**REPRODUCTION-ONLY.**  G3 proves an exact and genuinely rank-two-tested
weight/moment statement, but the statement is strictly weaker than
S-IDX-fin.  Once the missing inputs are imported, the “geometric proof” is
the same Moore--Penrose Ward proof in Fubini--Study vocabulary.  Since it adds
no covered group, no multiplicity control, and no current identity, the route
ends here and receives no critic/repair round under PRD.md.
