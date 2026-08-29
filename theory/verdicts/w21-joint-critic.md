<!-- ROLE: one-round joint hostile critic for bd tns-7pp.
     Targets: W1, W2, W3, W6.  Binding instruments: W4 and W5.
     No target is edited by this lane. -->

# 2+1 wave joint hostile critic

**W1 — `theory/soft-index-2d.md`: PASS with 0 FATAL / 0 MAJOR / 1 MINOR.**  The finite operator theorem is dimension-free, the full and highest-weight registers remain correctly separated, and the shard exhibits two natural nonzero 2D Hamiltonian/current instances.  The graph-cut paragraph needs one explicit perimeter bound and must reserve “zero mode” for the periodic directional sum.

**W2 — `theory/anyon-label-index.md`: PASS with 0 FATAL / 0 MAJOR / 1 MINOR.**  The finite toric-code endpoint-label, same-circle TPM-shift, and braiding-character theorem is proved by Pauli algebra and is promotable at `PROVED`; the deformation scope should be stated explicitly.  Doubled-Ising remains exact arithmetic and the model-general PEPS statement remains `SKETCH`.

**W3 — `theory/memory-index-2d.md`: FAIL(W3-O1) with 0 FATAL / 1 MAJOR / 1 MINOR.**  `M-INDEX-2D-fin` is proved and promotable at `PROVED`, and the conditional implication `M-INDEX-2D-spec` is mathematically correct.  The latter has no nonzero 2D model instance of `(LR2_2D)--(LR3_2D)` and therefore stays `SKETCH` under the binding W5 nonvacuity test; the finite `9x9` radiation calculation does not discharge that limit-law obligation.

**W6 — `theory/soft-2d-hunt.md`: FAIL(W6-O1) with 0 FATAL / 1 MAJOR / 1 MINOR.**  FUSION-SOFT and SHAPE-FLAT are correct conditional algebraic statements and the toric-code patch is nonvacuous, but their prose proofs are not yet the Lamport proofs required for a `PROVED` row.  NO-CAT-SOFT is sound only at its declared relation/data-insufficiency strength; its witnesses vary the probe family, not a pair of fully specified microscopic models.

**Joint count: 0 FATAL / 2 MAJOR / 4 MINOR.**  No target is refuted.  The single repair wave should be mechanical for W1, W2, and W6; W3's ordered-limit row is held at `SKETCH` rather than “repaired” by stronger prose.

## 1. Objections to W1

### W1-O1 — MINOR — the cut flux is a natural current map, but it is not canonically a zero-momentum mode and its W4-C1 bound is only implicit

**(a) Exact location.**  `theory/soft-index-2d.md` §2.1, lines 63--105, especially (2D.1)--(2D.3), and merge proposals 1--2 at lines 299--307.

**(b) Independent computation.**  Termwise invariance gives

`[h_Z,Q_S(Y)]=[h_Z,sum_{v in S cap Z}q_v(Y)]`

and hence

`||j_{partial S}(Y)|| <= 2 sum_{Z:Z cap S != empty, Z cap S^c != empty} ||h_Z|| |S cap Z| q_Y`,

where `q_Y=max_v||q_v(Y)||`.  On a bounded-degree, uniformly bounded finite-range lattice this is `C(Y,Phi)|partial_r S|`, not an `O(1)` endpoint bound.  Jacobi independently gives

`[Q(X),j_{partial S}(Y)]=j_{partial S}([X,Y])`,

so the cut supplies exactly the covariance used by the operator proof.  It does not supply a canonical momentum label on an arbitrary graph.  The periodic directional sum (2D.3) does.  The shard also supplies actual nonzero models rather than merely postulating the map: on the `2x3` SU(2) permutation ferromagnet its displayed horizontal current has `J_0(H_alpha)psi=2sqrt(3)i psi`; on the `2x2` SU(3) square its oriented-cycle current has `J_0(H_alpha)psi=4i psi`.

**(c) FIX DEMAND.**  Add the displayed norm bound above with its bounded-degree/uniform-interaction qualifiers; call (2D.1) a displayed cut-current map and reserve “directional zero-momentum flux” for (2D.3).  In the claim row use “displayed adjoint-covariant current map,” with the periodic zero-mode specialization in a subordinate clause.

**(d) SURVIVING WEAKER STATEMENT.**  S-IDX-fin-G-LAT holds on every finite graph once any complex-linear adjoint-covariant map is supplied.  Natural termwise symmetric Hamiltonians supply cut-current maps, and periodic exchange Hamiltonians supply the advertised nonzero directional zero modes.  No geometry-independent boundary norm or canonical graph direction follows.

## 2. Objections to W2

### W2-O1 — MINOR — the same-circle shift is parity-stable under ribbon deformation, but the endpoint-partition condition must be explicit

**(a) Exact location.**  `theory/anyon-label-index.md` §1.3, lines 105--121; §1.4, lines 123--145; proof leaf ⟨1⟩1.⟨2⟩3, lines 220--226; and Theorem A-INDEX-TC-fin, lines 149--198.

**(b) Independent computation.**  For either active Pauli-string component, multiplication of the enclosed stabilizers counts its endpoints inside `D` modulo two.  A local deformation with endpoints fixed changes the number of crossings of `partial D` by an even number, so the commutation bit with `F_e(D)` or `F_m(D)` is unchanged and (A.10)--(A.12) still give `b=a+x`.  Dressing by a closed contractible stabilizer also leaves the boundary covariance unchanged.  If an endpoint is moved across `partial D`, the inside/outside parity changes and so does the measured label; if the second measurement uses a different circle, the same-register proof no longer applies.  The checker realizes the fixed-endpoint case exactly: all four shifts pass, and `--red wrong-sector` exits `1` at ANYON-C4 with “computed e, claimed m.”

**(c) FIX DEMAND.**  Add one sentence: the TPM shift is invariant under deformations preserving the endpoint partition (and arbitrary extra even crossings), but not under moving an endpoint across the circle or changing the circle between measurements.  Treat `x=1` as the empty/identity ribbon rather than as a physical endpoint.

**(d) SURVIVING WEAKER STATEMENT.**  For a fixed contractible boundary PVM and a pure ribbon with each active component having one endpoint inside and one outside, `P_bW_xP_a=delta_{b,a+x}W_xP_a`; the same-circle TPM increment is exactly `x`.  This statement is path-shape independent within that endpoint partition, not circle-independent.

## 3. Objections to W3

### W3-O1 — MAJOR — the conditional limit law has no W5 nonvacuity witness and must remain SKETCH

**(a) Exact location.**  `theory/memory-index-2d.md` ⟨1⟩8--⟨1⟩9, lines 300--394; the finite probe and its disclaimer, lines 490--547; proposed `M-INDEX-2D-spec` row, lines 573--590; and final status, lines 593--602.

**(b) Independent computation.**  The implication is correct: at fixed `W`, the TPM first moment is the pinched difference (2D.5); `(LR2_2D)` removes the dephasing defect; `(LR3_2D)` supplies tightness and uniform integrability, so a spatial subsequence retains total mass, integer support, and the first moment.  But the checker establishes none of `(LR2_2D)`, `(LR3_2D)`, or the ordered limit.  Its nonzero data are finite-volume and finite-time: on the disk `p(1)=0.8238117477584995` and integrated flux `0.8238117477584986` (residue `8.88e-16`); on the annulus `p(-1)=0.6912712054641632` and flux `-0.6912712054641587` (residue `4.55e-15`).  The `9x9` model has finite gap `0.06030737921409081`, while the text correctly uses the infinite-square quadratic dispersion only as a gapless-sector interpretation.  No displayed model is proved to satisfy both 2D limit hypotheses with a nonzero limiting law.  Thus the finite calculation defeats a finite `0=0` objection to `M-INDEX-2D-fin`, but it is not the W5 witness required to promote a realized 2D memory limit.

**(c) FIX DEMAND.**  Keep `M-INDEX-2D-spec` at `SKETCH` and state in its row that no nonzero model instance of `(LR2_2D)--(LR3_2D)` is known; do not present the `9x9` finite-time probe as that witness.  Promotion requires a model with the two hypotheses proved and `p != delta_0`, not another checker sentence.

**(d) SURVIVING WEAKER STATEMENT.**  `(2D-INT)+(LR1_2D)--(LR3_2D)` imply the charge-law conclusion (2D.4), conditional exactly as written.  `M-INDEX-2D-fin` is independently nonvacuous and promotable.  No unconditional or nonzero asymptotic 2D memory instance has been proved.

### W3-O2 — MINOR — the boundary-flux interpretation needs termwise conservation and the explicit W4-C1 constant

**(a) Exact location.**  `theory/memory-index-2d.md` ⟨1⟩4, lines 130--140, and perimeter audit ⟨1⟩11, lines 416--430.

**(b) Independent computation.**  The displayed cancellation of every term wholly inside `W` follows directly if the interaction is represented with

`[Phi(Z),sum_{x in Z}q_x]=0`.

For such a decomposition,

`||d Qhat_W(t)/dt|| <= 2 q_* sum_{Z:Z cap W != empty, Z cap W^c != empty} |Z cap W| ||Phi(Z)|| <= C_{Phi,q,r}|partial_r W|`.

The W3 checker records the expected growth: disk boundary-edge counts `(12,20,28)` at radii `(1,2,3)` and annulus count `40`.  This agrees with W4-C1, where the `6x3`, width-two stripe has norm `3.000000=|partial W|/2`; a two-endpoint `O(1)` constant does not survive.  Global invariance alone does not justify the cancellation term by term for an arbitrary chosen decomposition, although a compact-group average can normally produce a symmetric local decomposition.

**(c) FIX DEMAND.**  Add the termwise-conservation hypothesis (or state that a symmetry-averaged local decomposition is chosen), print the norm inequality, and call `nu` the TPM two-readout charge change; identify only its dephased first moment with the current ledger unless an additional full-counting-statistics statement is supplied.

**(d) SURVIVING WEAKER STATEMENT.**  The finite integrality theorem and conditional probability theorem use no perimeter estimate and remain unchanged.  For a termwise charge-conserving finite-range interaction, the additive 0-form boundary current is perimeter-supported and its norm is `O(|partial_r W|)`.

## 4. Objections to W6

### W6-O1 — MAJOR — the positive general theorems have correct prose proofs but not the PRD-required Lamport proof form

**(a) Exact location.**  `theory/soft-2d-hunt.md` FUSION-SOFT, lines 73--99; SHAPE-FLAT, lines 101--128; honest status, lines 421--441; merge proposal 1, lines 443--450.

**(b) Independent computation.**  Both arguments are valid.  For FUSION-SOFT, `T_xP_a` decomposes only over `b` with `Hom(b,x tensor a) != 0`; left multiplication by `P_b`, Fourier summation, and windowing preserve each zero block; continuity preserves zero at every existing limit point.  For SHAPE-FLAT, each pulling-through move gives one equality, finite composition gives the path identification, and pentagon coherence removes contractible move-order dependence; a path around an insertion is outside the contractible hypothesis and may acquire braid holonomy.  The toric patch supplies a nonzero witness: `W_1|Omega>=W_2|Omega>=|chi>`, the endpoint gap is `4`, and the checker confirms the exact common syndrome.  However, the shard presents each proof as one unnumbered paragraph.  PRD.md permits a `PROVED` row only after a full Lamport-structured proof survives the critic loop.

**(c) FIX DEMAND.**  Convert each positive proof into a minimal ASSUME/PROVE Lamport ladder: typing and fusion decomposition; stability under Fourier/window linearity; stability under the declared topology; then, separately, one-move pulling-through, finite composition, coherence, and the noncontractible-holonomy fence.  Do not add hypotheses or new content.

**(d) SURVIVING WEAKER STATEMENT.**  FUSION-SOFT and SHAPE-FLAT are mathematically correct at their stated exact-intertwiner/fixed-point strength and remain `SKETCH` only until the required proof form is installed and mechanically verified.  They say nothing about a dressed generic-phase string or a gapless on-shell soft factor.

### W6-O2 — MINOR — NO-CAT-SOFT has a probe-family pair, not an AMP-grade full microscopic model pair

**(a) Exact location.**  `theory/soft-2d-hunt.md` NO-CAT-SOFT, lines 149--193; toric-code families (S2D.8)--(S2D.12), lines 231--293; honest status, lines 430--441.

**(b) Independent computation.**  The proof fixes the categorical/channel/support/homogeneous-equation data and replaces the endpoint family by `c(k)T_x(k)`.  With `c(k)=exp(i alpha k^n)`, the zero-momentum operator and all lower jets are fixed while the `n`th derivative changes by `i alpha n! T_x(0)`.  On the patch, changing `lambda` changes the probe: the phase slope is `1.000i` versus `2.750i`; path-curvature and projected-rotation-curvature ratios are both `4.000000`.  These are genuine operator families in one toric-code Hamiltonian, but they do not keep a complete microscopic source protocol fixed while varying only the model.  This is the same distinction enforced in `theory/amp.md`: a relation-level witness proves underdetermination by the listed relations, not physical nonuniversality over a fully specified model class.

**(c) FIX DEMAND.**  Add the AMP-style sentence: “The witness varies the momentum-dependent probe family and is not a pair of fully specified Hamiltonian/PEPS models with one fixed normalized protocol.”  Keep NO-CAT-SOFT out of `claims/CLAIMS.md` under PRD's negative-result rule.

**(d) SURVIVING WEAKER STATEMENT.**  Category, sector, channel, support, `T_x(0)`, and homogeneous pulling-through data alone do not determine a positive-order probe jet.  The shard does not prove that a fixed normalized physical protocol has different coefficients in two microscopic models, nor that extra dynamics cannot fix one.

## 5. Independently verified correct — repair fence

The repair wave must not churn the following results.

1. **W1 operator algebra.**  Root positivity, `P=D A^{-1}D^dagger`, the Ward leaf `D^dagger J(F)psi=J(H)psi`, the full-register formula, the separately projected highest-weight formula, and normalized index one are exactly the existing S-IDX-fin-G proof on a finite tensor product.  No proof leaf uses order, dimension, a cut, momentum, or scattering.
2. **W1 models and registers.**  Fresh green execution gave SU(2) `spec(A)={4^5,10}`, `D_hw^dagger D_hw=4I_5`, Ward residue `3.46410161514i`, and index one.  SU(3) gave `spec(A)={1^12,4^4}` and `{2^9,6}`, restricted Grams `I_12` and `2I_9`, Ward residue `4i`, full error `1.31e-15`, highest error `2.21e-15`, and false scalar-full defect `sqrt(40)=6.324555320337`.
3. **W2 Pauli proof.**  Endpoint anticommutation parity proves (A.10), orthogonal PVM transport proves (A.11), sequential Parseval proves TPM normalization for arbitrary `rho`, and the symplectic pairing in (A.14) is nondegenerate.  The `4x4` torus checker gave stabilizer rank `30`, ground dimension `4`, all four definite endpoint syndromes, the complete `4x4` braiding table, and every TPM shift.
4. **W2 nonabelian arithmetic.**  In doubled Ising, `(sigma,bar 1) tensor (sigma,bar 1)=(1,bar 1) direct-sum (psi,bar 1)`.  Both targets have even first universal degree, so `|b|-|a|=(1,0)=|x|`; this is a coarse grading shadow, not a choice of channel or a probability.
5. **W3 finite theorem.**  One-site circle integrality, finite spectral addition, automorphic spectrum invariance, sequential positivity/Parseval, and same-window offset cancellation are geometry-free.  The independent seeded TPM law was `{p(-1),p(0),p(1)}={0.0971892004,0.8224412578,0.0803695418}`, with mass residue `0` and mean/dephasing residue `4.86e-17` despite the common irrational offset `sqrt(3)/11`.
6. **W3 donor transplant.**  LR1-GEN applies to `Z^2`: countability gives separability; weak-* sequential compactness extracts the two Cesaro states; finite spectra and a Cantor diagonal extraction give one subsequence for every finite window and TPM weight.  The conditional limit proof correctly uses LR2 for the first-moment defect and LR3 for mass/first-moment tightness.  It imports no kink coordinate or channel completeness.
7. **W6 algebra and patch.**  The fusion selection rule is the finite semisimple consequence of a pure endpoint intertwiner.  Exact pulling-through gives contractible path flatness.  On the four-edge patch the ground energy is `-5`, the endpoint-pair energy is `-1`, the excitation gap is `4`, and `W_1|Omega>=W_2|Omega>` exactly.  The patch is a nonzero witness for selection and shape-flatness, though not an energetic soft-particle example.

## 6. Cross-consistency

### 6.1 W1 versus W4-C5: the register trap agrees numerically

There is no cross-register conflict.  W1's `2x3` SU(2) source has full Gram spectrum `{4^5,10}` while its highest restriction is `4I_5`; its SU(3), `lambda=1` source has `{1^12,4^4}` while its highest restriction is `I_12`, and the forbidden scalar substitution misses by `sqrt(40)`.  W4-C5 uses a different `3x3`, two-magnon source and finds `A_hw=5I_27` with error `9.69e-15`, full residual `3.51e-16`, highest residual `5.11e-16`, cross-register difference `0.133914`, and refuted-display error `0.187479`.  Both computations make the same point: the scalar restricted Gram is exact only after inserting the highest-weight source projection; it cannot replace the full-sector inverse.

### 6.2 W2's TPM lattice and W3's boundary flux are not the same observable

They share only the **same-register-twice protocol pattern**.

| item | W2 anyon TPM | W3 charge-history TPM |
|---|---|---|
| measured PVM | joint eigenspaces of multiplicative closed boundary stabilizers `F_e,F_m` | spectral PVM of additive on-site charge `Qhat_W=sum_x q_x-b_W I` |
| outcome set | torsion fusion group `Z_2^e x Z_2^m` | affine real spectrum; differences in `Z` |
| shift mechanism | ribbon covariance `P_bW_xP_a=delta_{b,a+x}W_xP_a` | common scalar offset cancels between two readouts |
| flux meaning | enclosed topological/anyon sector detected by Wilson loops | net selected 0-form charge change, with additive current through `partial W` |
| W4-C3 register | multiplicative loop/endpoint law, allowed | ordinary 0-form current, not a one-form Wilson-loop current |

The hybrid should state this distinction once.  Neither theorem is a corollary of the other, and W2's finite group shift must not be inserted into W3's additive current ledger.

### 6.3 W6 and W2 use the same fusion selection rule in different vocabularies

| W2 | W6 | dictionary |
|---|---|---|
| `D=Z(C)` bulk tube register | `D=Z(C)` in the bulk, or a declared boundary excitation category | same bulk object only before boundary condensation |
| tube projectors `P_a,P_b` | sector projectors `P_a,P_b` | identical block resolution |
| pure endpoint Kraus map `T_{x,mu}` | translated/windowed endpoint `T_x(y;w)`, `T_x(k;w)` | W6 Fourier-sums W2-type pure endpoint intertwiners |
| `P_bT_{x,mu}P_a=0` unless `mu in Hom(b,x tensor a)` | `P_bT_x(k;w)P_a=0` unless `Hom(b,x tensor a)!=0` | the same selection rule before and after a linear Fourier/window sum |
| TPM weights and PT4 normalization/postselection | block form factor and conditional `k->0` limit | W2 adds an instrument; W6 adds kinematics/topology, not probabilities |

There should be one categorical selection claim, not duplicate A-INDEX-PEPS and FUSION-SOFT rows with different names.  W2 remains the canonical finite TPM/toric theorem; W6 contributes the Fourier-limit corollary and SHAPE-FLAT.

## 7. Gate sweep and executed checks

### 7.1 Target checkers: green and every registered red

All commands were run under `python3 -O`.

| target | green | registered red | observed red exit path |
|---|---|---|---|
| W1 | exit `0`; SIDX2D-C0--C3 PASS | `--red-scalar-full` | exit `1` at SIDX2D-C2; scalar `1/lambda` rejected |
| W2 | exit `0`; ANYON-C0--C4 PASS | `--red wrong-sector` | exit `1` at ANYON-C4; computed `e`, claimed `m` |
| W3 | exit `0`; M2D-C1--C4 PASS | `--red fractional-charge` | exit `1` at M2D-C2; live increments `+-sqrt(2)`, distance from `Z` `0.414214` |
| W6 | exit `0`; S2DH-C0--C5 PASS | `--red wrong-path` | exit `1` at C2 and dependent C4; non-equivalent path rejected |
| W6 | same green | `--red erase-probe-freedom` | exit `1` at C3, C4, and C5; all three coefficient-freedom gates reached |

The binding W4 battery exited `0` with all gates live.  The categorical reference checker exited `0`; its `--red missing-ising-channel` exited `1` at CATH-C2.  The general-G, G2, G4, general-G-boundary, and authoritative S-IDX-r2 reference checkers all exited `0`.  LR-D16 exited `0` with all 16 rows green.  The legacy one-dimensional memory checker initially crashed before C8 because the installed NumPy lacks `np.trapezoid`; under the runtime compatibility alias `np.trapezoid=np.trapz`, all ten registered rows IDX-C1--C8rho passed.  This is checker plumbing, not a target disagreement.

### 7.2 Every target versus every W4 gate

| target | W4-C1 perimeter | W4-C2 loop/area | W4-C3 one-form | W4-C4 angular phase | W4-C5 register |
|---|---|---|---|---|---|
| W1 | **PASS with W1-O1 text fix.** Cut support is a finite-range collar; no `O(1)` claim.  W4 has `||i[H,Q_W]||=3.000000=|partial W|/2`. | **PASS.** No wall-coordinate statement. | **PASS.** Root Lie current is an additive 0-form current; no Wilson loop is put in D10. | **PASS.** No 2D scalar scattering slope is claimed; the ED chooses a displayed direction/cycle only. | **PASS.** W1's `sqrt(40)` scalar defect agrees with W4's cross-register error `0.133914` and refuted error `0.187479`. |
| W2 | **PASS/N.A.** No additive boundary-current norm estimate. | **PASS.** The PVM measures enclosed anyon parity, not a domain-wall coordinate, area, shape, or winding. | **PASS.** Uses the allowed multiplicative loop/endpoint law.  W4 independently has `||[H,W_loop]||=0`, additive-loop norm `8`, open-string norm `4`, and cross rank `0`. | **PASS/N.A.** No scattering slope. | **PASS/N.A.** No descendant Gram claim. |
| W3 | **PASS with W3-O2 text fix.** Explicitly says `O(|partial W|)`; measured disk counts are `12,20,28`, annulus `40`. | **PASS.** Explicitly rejects a unique kink/displacement coordinate and retains charge only. | **PASS.** Restricts itself to selected on-site 0-form charge and excludes topological/one-form statements. | **PASS.** Makes no soft-factor or scalar-slope claim. | **PASS/N.A.** No Gram projection. |
| W6 | **PASS/N.A.** No boundary-current norm theorem. | **PASS.** SHAPE-FLAT is isotopy of a string morphism, not charge-as-wall-position. | **PASS.** Pulling-through is kept separate from D10/current algebra. | **PASS.** The speculative Goldstone datum is the covector `dF_0`; it does not extrapolate a scalar slope.  W4's axial slopes are `(2,0)` and `(0,2)`, channel rank `9`, mixing `2/7`. | **PASS/N.A.** The shard explicitly denies a categorical Gram inverse. |

No target crosses a W4 negative gate.  In particular, W2/W6 use the multiplicative/categorical replacement demanded by C3, W3 carries the C1 perimeter factor, and W1 preserves C5's register fence.

### 7.3 Every target versus the three W5 warnings

| target | no displacement-memory claim | gapped `0=0` trap/nonvacuity | no d=3 fall-off extrapolation |
|---|---|---|---|
| W1 | **PASS.** No memory observable. | **PASS at finite-operator strength.** Nonzero denominators are `2sqrt(3)i` and `4i`; the theorem makes no energetic `k->0` claim. | **PASS.** No continuum fall-off order appears. |
| W2 | **PASS.** `b-a=x` is a torsion sector shift, not spatial displacement. | **PASS for A-INDEX-TC-fin.** From any torus ground state `p_x(1,x)=1`; the label theorem is nonzero in a gapped phase and is not advertised as a radiative soft theorem.  The model-general PEPS instrument remains SKETCH. | **PASS.** No radiative/Coulombic extrapolation. |
| W3 | **PASS.** Defines charge memory and explicitly rejects a universal scalar displacement. | **PASS for the finite theorem; HOLD for the ordered limit.** Finite nonzero escape is `0.8238117478`, but no model proves LR2/LR3 with a nonzero limiting law; this is W3-O1. | **PASS.** No `1/r` statement; no use of the d>=4 analysis at d=3. |
| W6 | **PASS.** No memory claim. | **PASS at categorical-selection/shape strength.** The toric endpoint amplitude is nonzero and the gap is `4`; the shard explicitly says this is not an energetic soft leg.  No Ward/Adler factor is promoted in the gapped bulk. | **PASS.** The 2D Goldstone discussion uses lattice momentum and is labelled speculative, with no continuum fall-off inference. |

### 7.4 Reduction checks

1. **W1 to S-IDX-fin-r2.**  The authoritative r2 checker passed.  The general-G references reproduce site-spin rows with residues `(2i,4i,6i)` and maximum mismatch `1.96e-15`.  W1 changes only the finite carrier and does not import the 1D scalar phase-slope statement.
2. **W3 to M-INDEX-fin/LR1-GEN.**  The finite arithmetic is the same coset/automorphism/Parseval/offset-cancellation proof.  LR-D16's donor checker passed; the legacy M-INDEX checker passed under the NumPy compatibility alias.  W3 does not import the 1D identity `Qhat=2s(X-c)` or its displacement conclusion.
3. **W2/W6 to CAT-SIDX.**  The cat-hunt green checker reproduced `sigma tensor sigma=1 direct-sum psi`, `sigma` odd, and the pointed `Vec_Z2` unique shift; the registered missing-channel red died.  The 2D statements use the same fusion-channel rule while correctly changing the bulk label category to `Z(C)`.

## 8. PROMOTABLE NOW

The following are the three copy-ready cells certified at `PROVED` strength.  W1-O1 and W2-O1 are sentence-level scope fixes and do not change these statements.

| id | statement | status | depends on | proved in | tested in |
|---|---|---|---|---|---|
| S-IDX-fin-G | Let a finite graph or finite periodic lattice carry a finite-dimensional on-site unitary representation of a compact Lie group `G` and a displayed complex-linear adjoint-covariant current map `J_0`, `[Q(X),J_0(Y)]=J_0([X,Y])`; on a periodic lattice `J_0` may be the displayed directional zero-momentum flux.  For every represented root `alpha` of the semisimple Lie algebra of `G^0`, every occupied positive coroot-weight sector `H^alpha_{lambda,V}`, and every `psi in ker Q(E_alpha) intersect H^alpha_{lambda,V}`, put `D_alpha=Q(F_alpha)|_{H^alpha_{lambda,V}}`, `A_alpha=D_alpha^dagger D_alpha`, and let `P_alpha` project onto `ran D_alpha`.  Then `A_alpha>0` and `P_alpha J_0(F_alpha)psi=D_alpha A_alpha^{-1}J_0(H_alpha)psi`; in the separately root-highest-restricted register, `D_hw^dagger D_hw=lambda I` and `P_hwJ_0(F_alpha)psi=lambda^{-1}Q(F_alpha)Pi_hwJ_0(H_alpha)psi`.  When `langle psi,J_0(H_alpha)psi rangle` is nonzero, the normalized Ward index `langle D_alpha psi,P_alpha J_0(F_alpha)psi rangle/langle psi,J_0(H_alpha)psi rangle` is exactly one.  The full-sector Gram inverse and highest-weight scalar register are not interchangeable.  Central-torus directions have no root row, finite groups have no Lie-current row, and an arbitrary graph supplies no canonical direction or zero mode. | **PROVED** | D10, ML4-Ward, S-IDX-fin-r2, S-IDX-fin-G | `theory/soft-index-general.md` §§1--2; `theory/soft-index-2d.md` §§1--2 | `theory/checks/soft_index_2d_check.py` SIDX2D-C0--C3 and `--red-scalar-full`; general-G and S-IDX-r2 reference gates |
| A-INDEX-TC-fin | On a finite square-lattice toric-code torus with periods at least three, fix a proper contractible disk `D` and its joint electric/magnetic boundary PVM `{P_a(D)}`.  For a pure open ribbon `W_x` of type `x in Z_2^e x Z_2^m` whose active direct/dual components each have one endpoint inside `D` and one outside, `P_bW_xP_a=delta_{b,a+x}W_xP_a`.  Hence the enclosed endpoint has definite label `x`, the two-projective-measurement protocol using the same PVM twice is a probability law supported on `b-a=x`, and a closed probe `y` returns the nondegenerate braiding character `(-1)^(x_e y_m+x_m y_e)`.  The shift is invariant under ribbon deformations preserving the endpoint partition, but not under moving an endpoint across the circle or changing the measured circle. | **PROVED** | finite toric-code Pauli algebra | `theory/anyon-label-index.md` §§1--3 | `theory/checks/anyon_label_check.py` ANYON-C0--C4 and `--red wrong-sector` |
| M-INDEX-2D-fin | Let a selected Hermitian on-site circle charge obey D26/(2D-INT), `spec q_x subset kappa+Z`.  For any finite disk or annulus `W`, real scalar background `b_W`, and `Qhat_W=sum_{x in W}q_x-b_W I`, one has `spec Qhat_W(t) subset (|W|kappa-b_W)+Z` for every automorphic time.  The explicit two-projective-measurement protocol using this same `W` and background at both times is a probability law whose escaped increment `nu=q_- - q_+` lies in `Z`, without assuming that the two Heisenberg observables commute.  This is a finite additive 0-form charge theorem; it implies no displacement, 1-form/topological charge, channel inventory, or ordered limit. | **PROVED** | D26, M-INDEX-fin | `theory/memory-index-2d.md` ⟨1⟩5--⟨1⟩6 | `theory/checks/memory_index_2d_check.py` M2D-C2 and `--red fractional-charge`; donor M-INDEX/LR1 checks |

No fourth row is promotable now.  The following status ceilings are binding:

- `M-INDEX-2D-spec`: **SKETCH** — the conditional proof is correct, but no nonzero `(LR2_2D)--(LR3_2D)` model instance is exhibited.
- `A-INDEX-PEPS`: **SKETCH** — retain PT1--PT4 and the model-specific microscopic pure-endpoint/instrument obligation.
- `FUSION-SOFT` and `SHAPE-FLAT`: **SKETCH pending the single Lamport repair**; eligible for orchestrator promotion after mechanical verification.
- `NO-CAT-SOFT`: no CLAIMS row.  Retain as a relation-level scope fence/negative lane record under PRD.md.

## 9. HYBRIDIZATION / REPAIR ORDER

The one repair wave should execute this order and nothing broader.

1. **W1 current wording.**  Insert the explicit `C_{Phi,q,r}|partial_rS|` cut-current bound with termwise invariance; distinguish an arbitrary graph current map from the periodic directional zero mode.  Apply the copy-ready S-IDX-fin-G carrier cell without changing either Gram register.
2. **W2 deformation sentence.**  State endpoint-partition invariance, changing-circle failure, and the empty-ribbon reading at `x=1`.  Promote only A-INDEX-TC-fin.
3. **W3 scope and perimeter.**  Insert the termwise-current hypothesis/norm bound and say explicitly that the finite ED is not an LR2/LR3 witness.  Promote M-INDEX-2D-fin; retain M-INDEX-2D-spec at SKETCH.  Do not add displacement language.
4. **One categorical hybrid, not two selection rows.**  Use W2's `(PT1)--(PT4)` register as the canonical PEPS typing.  Import from W6 only `T_x(k;w)`, the linear Fourier/window corollary, and SHAPE-FLAT.  Add the dictionary of §6.3 once.  Do not duplicate the rule as both A-INDEX-PEPS and FUSION-SOFT in CLAIMS.
5. **Lamportize W6 positives.**  Restructure FUSION-SOFT and SHAPE-FLAT exactly as W6-O1 demands; add no new hypotheses or prose program.  The orchestrator then verifies the cited steps and may promote the single hybrid selection row plus SHAPE-FLAT.
6. **Fence NO-CAT-SOFT.**  Add the one AMP-style relation-level sentence from W6-O2.  Do not seek or advertise a full-model counterexample and do not promote the negative result.
7. **Checker plumbing only.**  If the old donor checker is mentioned in the merged record, replace `np.trapezoid` compatibly or record the required NumPy version; this is not a theorem repair and must not headline the wave.

### Artifact disposition

- `theory/anyon-label-index.md` remains the canonical proof carrier for A-INDEX-TC-fin.
- `theory/memory-index-2d.md` remains the proof carrier for M-INDEX-2D-fin and the lane record for the uninstantiated conditional limit program.
- `theory/soft-index-2d.md` remains a dimension-audit/check pointer after its finite-carrier content is folded into the existing S-IDX-fin-G row and D10 graph clause.
- `theory/soft-2d-hunt.md` remains a lane record after its positive selection/shape content is imported into the categorical hybrid; NO-CAT-SOFT and the speculative edge/Goldstone programs stay there.
- Doubled-Ising microscopic endpoint identification and A-INDEX-PEPS remain lane records at SKETCH; only the displayed fusion arithmetic is certified exact.

**Final line: FAIL(W3-O1, W6-O1).  Zero FATALs; no target refuted; three finite claims are promotable at PROVED strength.**
