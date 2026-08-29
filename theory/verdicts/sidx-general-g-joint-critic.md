**`theory/soft-index-g.md` (G1): MINOR — (GFIN.1)--(GFIN.2), the two-register split, positivity, centralizer equivariance, and Weyl transport survive; “canonical blocks” must be read and restated as canonical isotypic blocks.**

**`theory/soft-index-g2.md` (G2): MAJOR — the polar block identity, polarized Ward contraction, and normalized index one survive; the displayed scalar/rank-one boundary and the disconnected/full-`H` scope need repair.**

**`theory/soft-index-g4.md` (G4): MINOR — (G4.11)--(G4.14) and the strict projector-fineness result survive; the SU(3) computation proves strict inclusion, while the abstract witness—not that computation alone—proves underdetermination.**

Joint count: **0 FATAL / 2 independent MAJOR issues / 5 MINOR issues / 3 NOTE findings.**  There is no contradiction between the surviving operator identities.  G1's root theorem is promotable under the standard isotypic reading of its centralizer clause; G2's proposed row is not promotable because its scalar criterion and disconnected covariance are not yet correct.  The final joint row should wait for one coherent hybrid repair.

# Objections by artifact

## G1

### G1-O1 — MINOR — centralizer equivariance gives canonical **isotypic** blocks, not canonical irreducible-copy blocks

**Exact quoted target.**  G1 says in ⟨1⟩4:

> “The root identity is canonically block diagonal over this action”

and then:

> “Therefore both sides of (GFIN.1) and (GFIN.2) are `C_{H,alpha}`-intertwiners and split over its irreducible blocks in the multiplicity spaces.”

The same proof immediately says:

> “The current `J_0(H_alpha)` may mix different `n` and different isomorphic multiplicity copies while respecting `C_{H,alpha}`.”

The last sentence is correct and prevents the first two from being true under their literal “canonical irreducible blocks” reading.  If the total multiplicity register is decomposed under the compact centralizer as

\[
  \bigoplus_\tau V_\tau\otimes L_\tau,
\]

then a centralizer intertwiner has the form

\[
  \bigoplus_\tau \mathbb 1_{V_\tau}\otimes B_\tau.
\]

The isotypic summands labelled by `tau` are canonical.  Individual copies inside `L_tau` are not canonical, and `B_tau` may mix them.  It may also mix occurrences of the same centralizer type carried by different root-spin labels `n`.  G1's (G.14) does prove that `A` itself is scalar on each root-`sl_2` irrep and the identity on `M_{n,alpha}`; it does not make the *current identity* diagonal in a canonical choice of irreducible multiplicity copies.

**Verdict on the mathematical core.**  The correct statement is:

> Both registered maps are equivariant for the represented root-`sl_2` centralizer and hence preserve its canonical isotypic decomposition; arbitrary mixing among equivalent copies remains allowed.

This leaves (GFIN.1)--(GFIN.2) untouched.  “Block diagonal over a compact-group action” normally means exactly this isotypic decomposition, and G1's following sentence already permits equivalent-copy mixing.  The issue is therefore a precision repair, not a false theorem; the hybrid must make the intended reading unambiguous.

### G1-O2 — MINOR — the theorem hypothesis is the displayed current covariance, not an already-registered finite-ring D10 construction

**Exact quoted target.**  The proposed row says the current zero mode is

> “supplied by a standard periodized D10 interaction”

while ⟨1⟩2 correctly warns:

> “For a bare finite ring specified only by `[H_N,Q(X)]=0`, (G.2) must be supplied: a circle has no canonical half-line cut and global invariance alone does not select a current improvement.”

D10 defines the cut current on the infinite chain.  A finite periodic realization can certainly be displayed, as all three SU(3) checkers do, and covariance of that displayed realization is exact.  But “standard periodized” is not itself a frozen D10 definition.  The hybrid theorem should assume a displayed complex-linear current obeying (G.2), then state separately that a chosen periodization of a termwise invariant D10 interaction is an instance.  No proof step in G1 needs more.

### G1-O3 — NOTE — the Weyl-transport argument is correct and does not smuggle in simultaneous diagonalization

**Exact quoted target.**  G1 says:

> “Conjugating (GFIN.1)--(GFIN.2) by `U(n_w)` gives the corresponding identities for `w alpha` with the same singular values and residuals.”

Recomputation keeps the phase.  If

\[
 \operatorname{Ad}_{n_w}F_\alpha=\overline c_wF_{w\alpha},
 \qquad |c_w|=1,
\]

then both the transformed `J(F)` and the transformed lowering map `D` acquire the same factor `overline(c_w)`, while `A=D^dagger D`, the range projector, and the highest-weight projector are unitarily conjugated without a phase.  Thus the identity and every singular value are preserved.  G1 also explicitly keeps non-orthogonal-root projectors in separate registers.  The SU(3) color swap gives zero local and current conjugation error and `tr(H_01 H_02)=1`; no Weyl-wall or independent-scalar claim is inferred.  This part needs no mathematical repair.

## G2

### G2-O1 — MAJOR — the displayed “rank-one” scalar condition is neither a necessary-and-sufficient criterion nor correctly typed

**Exact quoted targets.**  G2 first says:

> “A **canonical scalar** statement then requires either `c^mu_{W,lambda}=1` plus a one-dimensional hard multiplicity, or an explicit choice of CG channel and hard line.”

It later says:

> “The projected-current coefficient in (G2.13) is a canonical multiplicity operator.  It becomes a scalar only on a one-dimensional selected hard line, or if `dA^+r` is separately proved scalar on the chosen multiplicity block.”

The proposed row condenses this to:

> “a scalar projected-current coefficient beyond the normalized index needs a rank-one hard/CG channel or a separately proved scalar reduced operator.”

There are three distinct notions here, and the shard conflates them.

1. The coefficient *relative to the charge map* is `B=A^+r` on the source multiplicity register, because
   \[
     P\widehat J=dA^+r=dB.
   \]
   The map `dA^+r` itself goes from source multiplicity to target multiplicity and is not intrinsically a “scalar operator” when those spaces differ.
2. On a fixed nonzero one-dimensional source line, a scalar relation is sufficient and automatic.  That is a useful sufficient condition, not a necessary one.
3. Higher-rank blocks can have a universal scalar coefficient.  For example, `d=I_2`, `A=I_2`, and `r=cI_2` give `P\widehat J=cD` on a two-dimensional multiplicity register.  Rank one is therefore not necessary.  Conversely, rank of `d` equal to one is not sufficient on a higher-dimensional source: with `d=(1\ 0)` and `j=(0\ 1)`, one has `A=diag(1,0)` and `dA^+d^dagger j=j`, but no scalar `c` obeys `j=cd`.

The exact map-level criterion is

\[
  P\widehat J=cD
  \quad\Longleftrightarrow\quad
  dA^+r=cd.                                                   \tag{C-SCAL}
\]

If `d` is injective, this is equivalent to `A^{-1}r=cI`, or `r=cA`.  For one selected vector `v`, the criterion is only `dA^+rv` proportional to `dv`.  The repair must state (C-SCAL), call a one-dimensional nonzero source line merely sufficient, and remove every “only under rank one” formulation.  The root highest-weight register provides the important higher-multiplicity example: `A_pol=lambda I` even when the root-highest multiplicity is twelve.

### G2-O2 — MINOR — `K=H_alpha` is unavailable for the polarized-line formula in the standing SU(3) overlap

**Exact quoted targets.**  G2 introduces `K` with:

> “(in the broken-vacuum application, one may take `K=H_alpha`)”

and calls the block theorem the all-compact answer:

> “take `K=G`, or `K=H_alpha` in the broken register”

The qualifier (G2.1) still requires the line `C b` to be `K`-stable.  That qualifier fails for the very nonabelian-unbroken-subgroup geometry used by G1/G5.  In the qutrit vacuum with

\[
 H_\alpha=S(U(1)\times U(2)),
\]

the unbroken `U(2)` rotates `F_01` and `F_02` as a doublet; in particular G1/G5 compute `[H_01,E_12]=-E_12`.  Thus `C F_01` is not an `H_alpha`-module.  With `K=H_alpha`, only G2's higher-dimensional `W` packaging applies, and (G2.BLOCK) leaves `R=D^dagger J` unevaluated.  It is polar algebra, not the root Ward identity.

On the actual overlap, take `K` to be the compact root circle generated by `H_alpha`, take `b=F_alpha`, and use the one-dimensional character of weight `-2`.  Then G2.FULL is exactly G1's GFIN.1.  Alternatively retain full `H_alpha` only as a transport/equivariance group for the complete broken module `W`, without claiming the line formula.  The hybrid must make this choice explicit.

### G2-O3 — MAJOR — infinitesimal covariance does not justify the disconnected-`K` Schur decomposition used by the proof

**Exact quoted targets.**  G2 says:

> “Its disconnected quotient is allowed but is a spectator to the Lie-algebra current.”

It displays only

> `[dU_N(x),J_0(y)]=J_0([x,y])`

and then proves the Schur form using

> “for `k in K`, `U_N(k)Q_bU_N(k)^dagger=chi_b(k)Q_b` and the identical formula for `J_b`.”

The displayed infinitesimal commutator integrates over the identity component.  It does not, by itself, imply covariance under disconnected elements of `K`.  Those elements are also not spectators to the claimed all-`K` theorem: they can permute Lie directions, combine root spaces into a higher-dimensional irreducible `W`, and alter the CG/isotypic labels.

For an on-site `G`-invariant D10 interaction, the missing global formula is true and easy to derive cut by cut:

\[
 U_N(k)J_0(y)U_N(k)^\dagger=J_0(\operatorname{Ad}_k y),
 \qquad k\in K.                                               \tag{C-GLOB}
\]

But (C-GLOB) must be a displayed hypothesis or derivation before Schur orthogonality is invoked for disconnected `K`.  After that repair, the generic block theorem really does cover compact disconnected `K`; this matters for the cross-consistency finding below.

### G2-O4 — NOTE — the normalized Ward index is exactly one and needs no scalar/rank-one hypothesis

For every polarized `psi` with nonzero denominator,

\[
 \langle D\psi,PJ_b\psi\rangle
 =\langle D\psi,J_b\psi\rangle
 =\langle\psi,D^\dagger J_b\psi\rangle
 =\langle\psi,J_{[b^\dagger,b]}\psi\rangle.
\]

This proves (G2.15) directly.  Neither injectivity, a CG multiplicity-one condition, nor scalarity of `A^+r` is used.  The SU(3) checker gives `1+6.49e-18 i`, and the shared four-qutrit overlap below gives `1-1.22e-17 i`.

## G4

### G4-O1 — NOTE — the label identity and integrality argument are correct

**Exact quoted target.**  G4 claims

> `ind_{Z_alpha}(X;gamma):=(gamma chi_X)gamma^{-1}=chi_X in Lambda_alpha^*`

and

> `Delta q_eta=n_eta(chi_X) in Z`.

Global covariance makes both `Q_X psi` and `J_X psi` transform by `gamma chi_X`.  Haar orthogonality then proves (G4.11)--(G4.12), and the affine offset on `K_u` cancels in the ratio.  Finally `chi_X circ eta` is a continuous character of `U(1)`, hence `e^{in theta}` for one integer `n`.  This is an implication from compact representation covariance, not an independent dynamical index.  The possible disconnected part of the effective center contributes a finite torsion character, not an integer circle coordinate.  No expectation value is claimed to be quantized.

### G4-O2 — MINOR — the `8`-in-`24` computation proves projector fineness, not the whole information-theoretic no-go

**Exact quoted targets.**  G4 computes

> `dim H_{5/3}=8, dim H_{2/3}=24, rank D=8`

and concludes:

> “Thus `P_D<Pi_{2/3}` strictly.”

It also calls the nonzero outside component

> “the promised physical realization of the abstract multiplicity witness (G4.19).”

The first conclusion is exact: rank `8<24` proves strict inclusion.  The measured

\[
 \|(\Pi_{2/3}-P_D)J_X|h;2\rangle\|=\sqrt{8/3}
\]

also proves that replacing `P_D` by the central-sector projector changes this actual current vector.  This is precisely the projector-fineness work the ED can do.

It does not, by itself, prove that the along-range coefficient cannot be reconstructed from *some additional* data.  The logical “superselection alone cannot determine it” conclusion is instead proved by (G4.19): keeping the same two character labels while varying `a,b` changes `P_DJ`.  The hybrid should attribute strict inclusion and the live replacement defect to the SU(3) computation, and attribute underdetermination to the abstract same-label/different-map witness.  With that attribution, G4-SPLIT is sound.

### G4-O3 — MINOR — state current covariance as part of the finite-ring register

**Exact quoted target.**  G4 defines

> “the zero-mode charge and zero-mode cut current, extended complex-linearly from D10”

on a periodic ring and derives its transformation by conjugating the cut identity.  As in G1-O2, D10's frozen cut is an infinite-chain object.  The label theorem only needs the displayed global covariance of `J_X`; it does not need a canonical finite-circle cut.  The hybrid should assume the displayed finite-ring current and its global `Z_alpha` covariance, then list a chosen D10 periodization as an instance.  This is a typing repair, not a defect in (G4.11)--(G4.14).

# Cross-consistency

## Exact G1/G2 dictionary on the overlap

Take a represented root `alpha` of the semisimple Lie algebra of `G^0`.  In G2 choose the compact root circle `K_alpha` generated by the coroot and choose `b=F_alpha`.  Then the two statements identify as follows.

| G1 root register | G2 character-line register |
|---|---|
| root circle generated by `H_alpha` | `K=K_alpha` |
| `F_alpha`, `E_alpha=F_alpha^dagger` | `b`, `b^dagger` |
| coroot weight `lambda` | one-dimensional `K_alpha` irrep `V_lambda` |
| `H^alpha_{lambda,N}` | multiplicity register `M_{lambda,N}` |
| target weight `lambda-2` | character twist `chi_b lambda` |
| `D_alpha=Q(F_alpha)|_{H_lambda}` | `d_{lambda,b}` after suppressing the one-dimensional irrep factor |
| `A_alpha=D_alpha^dagger D_alpha` | `A_{lambda,b}=d^dagger d` |
| `K^alpha_{lambda,N}=ker Q(E_alpha)` | `K_{lambda,b}=ker Q_{b^dagger}` |
| `Pi_hw` | `Pi_pol` |
| `h_b=[b^dagger,b]=H_alpha` | `J_{h_b}=J_0(H_alpha)` |
| `P_alpha J(F)psi=D A^{-1}J(H)psi` | G2.FULL, with `A^+=A^{-1}` because `lambda>0` makes `D` injective |
| `A_hw=lambda I` and the projected restricted formula | G2.POL plus the root-`sl_2` norm calculation |

Thus G1 and G2 prove the *same* full-sector and restricted identities on their root-circle overlap.  G2's generic `W` block is a broader formal polar decomposition, but without a Ward evaluation of `R` it is not a broader root soft-index theorem.

## Shared SU(3) numbers

The lanes chose different showcase inputs: G1 uses an `N=4` single root, while G2 uses an `N=3` non-root character line `E_21+2E_32`.  Therefore the spectra `{1,4}` and `{5,5,8}` are not supposed to be equal.  The latter example lies outside G1's root class.  On the actual overlap the numbers agree exactly:

- Applying the G2 dictionary to G1's `N=4`, `lambda=1`, `alpha_01` block gives the same source dimension `16`, polarized dimension `12`, and
  \[
    \operatorname{spec}A=\{1^{(12)},4^{(4)}\}.
  \]
  It is literally the same `D`, `A`, `P`, and Ward contraction.  The full and restricted residuals are `1.59e-15` and `2.71e-15`; the forbidden scalar-full and no-projector defects are `sqrt(40)=6.324555320` and `8.432740427`.
- A direct joint recomputation on G4's `N=4` hard state `|h;2>` gives the sharper three-lane overlap.  Relative to the root `alpha_01`, the state is root-highest at `lambda=3`; the source/target dimensions are `4 -> 16`, the highest dimension is `4`, and
  \[
    \operatorname{spec}A=\{3,3,3,3\}.
  \]
  G1/G2 give the projected coefficient `2i/3`, denominator `2i`, and normalized index `1-1.22e-17 i`.  G4's coarser central block has dimensions `8 -> 24` and charge rank `8`.  Its projected vector agrees with the root projection to `6.94e-16`; the root Gram/Ward residual is `3.85e-17`.  This reproduces G4's diagnostic coefficient `2i/3` and residue `2i`.

There is therefore no numerical or register disagreement.  The central-sector projector is a coarser direct sum of root-weight blocks; it is not substituted for any one root range projector.

## SU(2) reduction

Both operator routes use

\[
 E_\alpha=S^+,
 \quad F_\alpha=S^-,
 \quad H_\alpha=2S^z,
 \quad \lambda=2m,
 \quad J(H_\alpha)=2J^z.
\]

Consequently the full formula is exactly

\[
 PJ^-_0\psi=2DA^{-1}J^z_0\psi,
\]

and the separately restricted formula is exactly

\[
 P_{hw}J^-_0\psi=Q_0\Pi_{hw}J^z_0\psi/m.
\]

At `N=4`, `h=pi/2`, and site spins `S=1/2,1,3/2`, G1, G2, G4, and S-IDX-fin-r2 all reproduce

| `S` | `v_S(h)` | `||Q_0|h>||^2` | residue |
|---:|---:|---:|---:|
| `1/2` | `1` | `2` | `2i` |
| `1` | `2` | `6` | `4i` |
| `3/2` | `3` | `10` | `6i` |

The maximum measured mismatch is `1.96e-15`.  Both general operator routes therefore reduce exactly to the authoritative PROVED row S-IDX-fin-r2.

## Is G4 implied on the overlap, and does it strictly exceed both operator lanes?

**Implied, not merely compatible.**  Where a G1 root line is also a `Z(H_alpha)` character line, global covariance gives

\[
 U(z)Q(F_\alpha)U(z)^\dagger=\chi_\alpha(z)Q(F_\alpha),
 \qquad
 U(z)J(F_\alpha)U(z)^\dagger=\chi_\alpha(z)J(F_\alpha).
\]

The G4 block selection follows by applying the central spectral projectors.  Evaluation of the same character on a cocharacter is integral.  In G2 this implication is even more explicit: take `K=Z(H_alpha)` and its character line (or the appropriate irreducible `W`); G2-SCHUR already says the charge and current maps have the same character twist.  G4.11--G4.14 are the corresponding central-isotype corollary.

**The requested strict-excess claim fails against G2 as currently stated.**  G4 strictly exceeds G1's *stated scope* because G1 assumes connected `G` and contains no finite/torsion central-sector theorem.  It does not strictly exceed a repaired G2 theorem that genuinely assumes global covariance for an arbitrary compact, possibly disconnected, `K`: that G2 representation-theoretic setup already retains disconnected isotypes and torsion characters, and it implies G4's selection rule.  G2 cannot simultaneously say “all compact `K`” and call the disconnected quotient a “spectator.”

The hybrid resolves this cleanly by assigning different headline jobs: the operator theorem is stated only root-wise on the connected semisimple part, while the separately named label theorem is stated for general compact `G`, including disconnected effective-center characters.  Relative to that deliberately scoped **operator theorem**, G4 strictly adds the disconnected/global-form label content; it is not advertised as logically independent of G2's generic Schur lemma.

## Excluded classes and G3 fences

- **Central torus / abelian factor.**  G1 correctly has no root row.  G2's generic polar identity may be written for a central direction, but `h_b=0`, the normalized denominator is zero, and this is not a nontrivial root soft index.  The hybrid must call the root theorem empty/degenerate there, exactly as G5-C1 requires.  An unbroken central torus may still *grade a noncentral broken component* in G4; this grading is not a root ladder for the central direction itself.
- **Finite groups.**  There is no nonzero Lie-algebra current component and hence no operator or integer-circle soft row.  G2.BLOCK is empty when `W subset g_C` is empty, and G4 may retain only a torsion sector label if supplied independently; neither replaces G5's finite-string endpoint statement.
- **Global form and disconnected elements.**  They restrict, pair, or permute admissible sectors and root rows; they do not modify the local Gram coefficient.  This agrees with G5-C3.
- **G3 §17.**  No surviving proof uses G3 for positivity/scalarity of `D^dagger D`, current covariance, removal of `Pi_hw`, a finite/central-torus leg, or identification with M-INDEX.  G1 supplies root-string positivity and Ward covariance directly; G2 supplies polar/Schur algebra under displayed covariance; G4 proves only the character label.  All five fences remain intact.

# Gate sweep

All commands were run under `python3 -O`.  Every discovered public red mode was run separately, including G1's `--red-force-h-block`, which is present in the checker but omitted from G1's displayed three-command contract.

## G5 standing battery

`python3 -O theory/checks/soft_index_g_boundary_check.py` exited `0` and ran every named gate:

- **G5-C1-ABELIAN:** charge-created rank `0`, magnon overlap `0`, magnon distance `1`, and broken-`U(1)` orbit-tangent norm `0.866025`.
- **G5-C2-FINITE:** cross-sector group-element rank `0`, Gram norm `0`, finite-string endpoint residual `0`.
- **G5-C3-GLOBAL-FORM:** spin-1 content `{0:1,1:9,2:10,3:7}`, spin-`1/2` content `{1/2:4,3/2:4}`, lifted-center errors `(7.35e-16,3.67e-16)`, and `O(2)` paired-spectrum error `8.88e-16`.
- **G5-C4-SU3-H-MULT:** full Gram error `1.42e-15`, false scalar error `6.155367` (relative `1.685717`), multiplicity scalar defect `6.666667`; the second-root control is `1.93e-16` in both forms.
- **G5-C5-SU3-REGISTER:** `spec A_full={1^5,4^4,9^1}`, `A_hw-I` error `1.38e-15`, full/restricted errors `(1.42e-15,1.40e-15)`, naive scalar error `6.155367`, cross-register error `2.051789`, current leakage `4.103578`.

No surviving identity crosses the matrix-Gram or register gates.  G2's broad headline wording, not its formula, is what needs the abelian/disconnected fence.

## Lane checkers

- **G1:** green exit `0`; full/restricted maximum residuals `(1.59e-15,2.71e-15)`; SU(3) forbidden defects `(6.324555320,8.432740427,4.898979486)`; full-`H` commutator defect `1.000`; SU(2) maximum error `1.96e-15`.  All four reds—`--red-scalar-full`, `--red-drop-hw-projector`, `--red-drop-hw-factor`, `--red-force-h-block`—exited `1` at the intended gate.
- **G2:** green exit `0`; SU(3) `spec A=(5,5,8)`, full residual `1.50e-16`, normalized index `1+6.49e-18i`, orthogonal current norm `2.323790007724`, scalar defect `0.129099444874`; SU(2) maximum residue mismatch `1.96e-15`.  `--red-scalar-gram` exited `1` with residual `0.1291`.
- **G3:** green exit `0`; moment values `lambda=(1,1)`, lowered values `(-1,2)` and `(2,-1)`, coherent-curve probability `0.2`.  `--red` exited `1` with mixed-root increment error `0.2496`.  This corroborates only G3's reproduction-only moment statement.
- **G4:** green exit `0`; label `5/3 -> 2/3`, dimensions `(8,24)`, rank `8`, inside/outside current norms `(sqrt(4/3),sqrt(8/3))`, coefficient error `7.01e-16`; SU(2) residue mismatch `1.96e-15`.  `--red-shift` and `--red-projector-collapse` both exited `1` at their intended gates.
- **S-IDX-fin-r2:** green exit `0`; C2 projection/residue maxima `(5.74e-16,1.96e-15)` and pure-`Q_0` ratio error `6.84e-16`.  All eight public reds—register, Ward residue, Adler anchor, S2 value, LSZ factor, TGT value, leg power, and limit order—exited `1`.  The green path also ran the three standing ML4 child reds and observed exit `1` for each.

Passing these computations is corroboration only.  The analytic polar/Ward and character proofs carry the status decisions.

# PROMOTABLE NOW

1. **S-IDX-G-label is promotable now to PROVED**, in the exact narrowed row proposed below: displayed global current covariance is part of the hypotheses; the result is the selection/integrality theorem plus the scoped pure-zero-mode anchor; the finite-group and trivial-character cases are explicitly empty/zero.  G4 has completed its proposer/one-critic loop with no FATAL or MAJOR against that statement.
2. **G1's root operator theorem is promotable now under the binding isotypic reading of its centralizer clause.**  Its equations GFIN.1 and GFIN.2 are proved, and G2 supplies the proved root normalized index.  Do not merge the lane-local row separately: the single hybrid operator row below should replace it after the mechanical wording/current-register consolidation.
3. **G2.BLOCK is a valid supporting polar-decomposition lemma**, not a Letter headline and not a separate promoted soft-index row.  G2's proposed all-compact row is not promotable until G2-O1--O3 are repaired; the hybrid makes the separate row unnecessary.

# HYBRIDIZATION DESIGN / REPAIR ORDER

## Single shard

Create one replacement theorem candidate, `theory/soft-index-g-hybrid.md`.  Do not concatenate the three lanes.  Use the following provenance.

| Hybrid section | Source to retain | Required change |
|---|---|---|
| Scope and exclusions | G1 ⟨1⟩1, G5 §6 | State the operator part on represented roots of the connected semisimple part; central torus has no root row; finite groups have no Lie-current row; global form is sector-lattice input. |
| Root setup and two operator registers | G1 ⟨1⟩2--⟨1⟩3 | Retain the positivity, polar projector, Ward contraction, full `A^{-1}`, and restricted `Pi_hw/lambda` proofs essentially verbatim.  Make displayed current covariance the hypothesis. |
| Multiplicity language | G1 ⟨1⟩4 plus G2 ⟨1⟩2, ⟨1⟩4--⟨1⟩5 | Say “canonical centralizer-isotypic decomposition,” never “canonical irreducible blocks.”  Include the typed generic `W` polar lemma as supporting algebra, with global `K` covariance displayed. |
| Scalar boundary and normalized index | G2 ⟨1⟩9--⟨1⟩10 | Keep index `1`; replace the rank-one prose by (C-SCAL).  A nonzero one-dimensional selected source line is sufficient, not necessary. |
| Root/full-`H` and Weyl relation | G1 ⟨1⟩4--⟨1⟩5 | Root circle gives the line formula; full `H` acts internally only if it centralizes/normalizes the root line, otherwise it transports the root row or acts on the whole broken module `W`. |
| General compact label/integrality theorem | G4 ⟨1⟩1--⟨1⟩4 | Retain the effective-center quotient, affine character torsor, exact block shift, cocharacter integrality, possible finite torsion, and pure-zero-mode anchor.  State global current covariance explicitly. |
| Projector fence | G4 ⟨1⟩5 and ⟨1⟩7, G5 | Retain `P_D<=Pi_target`, the `8<24` strict-inclusion computation, and the nonzero outside norm.  Credit the abstract witness for underdetermination. |
| Reductions | G1 ⟨1⟩6, the joint recomputation above, G4 ⟨1⟩6 | Print the exact SU(2) dictionary/numbers and the shared SU(3) `lambda=3`, `2i/3`, index-one cross-check. |
| G3 | G3 §17 only | At most one interpretive sentence about a primitive root step.  Import none of the five fenced claims. |

## Unified theorem set

The hybrid contains exactly two headline theorems.

1. **Operator theorem.**  For a represented root of the semisimple Lie algebra of `G^0`, a positive coroot sector, a root-highest input, and a displayed adjoint-covariant current, prove both the full-sector Gram-inverse identity and the separately root-highest-restricted identity.  Add the normalized Ward index one.  State centralizer **isotypic equivariance**, not irreducible-copy diagonalization.  Disconnected elements may transport root rows but do not change the local coefficient.
2. **Integrality theorem.**  For general compact `G`, including disconnected groups, and a nonzero represented Lie component spanning a character line of the effective unbroken center, prove the common charge/current sector shift, its character-lattice value, integer components on connected cocharacters, and possible finite torsion label.  Keep the descendant-range projector strictly finer than the sector projector.

The shared exclusions are explicit: a central Lie direction has no root ladder (and has trivial adjoint character), while a finite group has no Lie-current soft row.  Point both exclusions to G5; do not turn either into a zero-valued instance of the root theorem.

## Verbatim proposed CLAIMS rows

The first row below is the **post-repair** row authorized for promotion to PROVED after the mechanical work list is satisfied.  Until then, the present G1/G2 proposals remain unmerged.  The second row is promotable now.

> | id | statement | status | depends on | proved in | tested in |
> |---|---|---|---|---|---|
> | S-IDX-fin-G | Let a finite periodic ring carry a compact Lie on-site symmetry `G` and a displayed complex-linear current zero mode satisfying `[Q(X),J_0(Y)]=J_0([X,Y])`.  For every represented root `alpha` of the semisimple Lie algebra of `G^0`, every occupied positive coroot-weight sector `H^alpha_{lambda,N}`, and every `psi in ker Q(E_alpha) intersect H^alpha_{lambda,N}`, put `D_alpha=Q(F_alpha)|_{H^alpha_{lambda,N}}`, `A_alpha=D_alpha^dagger D_alpha`, and let `P_alpha` project onto `ran D_alpha`.  Then `A_alpha>0` and `P_alpha J_0(F_alpha)psi=D_alpha A_alpha^{-1}J_0(H_alpha)psi`; in the separately root-highest-restricted register, `D_hw^dagger D_hw=lambda I` and `P_hwJ_0(F_alpha)psi=lambda^{-1}Q(F_alpha)Pi_hwJ_0(H_alpha)psi`.  When `langle psi,J_0(H_alpha)psi rangle` is nonzero, the normalized Ward index `langle D_alpha psi,P_alpha J_0(F_alpha)psi rangle/langle psi,J_0(H_alpha)psi rangle` is exactly one.  The maps preserve the canonical isotypic decomposition of the represented root-`sl_2` centralizer, while equivalent copies may mix; a general unbroken `H` instead transports conjugate-root rows unless it normalizes the root line.  At `G=SU(2)` the two registers and the residues `(2i,4i,6i)` reduce exactly to S-IDX-fin-r2.  Central-torus directions have no root row, finite groups have no Lie-current row, and disconnected/global-form data enter through the separate sector-label theorem. | **PROVED** (after the single mechanical hybrid repair ordered in `theory/verdicts/sidx-general-g-joint-critic.md`) | D10, ML4-Ward, S-IDX-fin-r2 | theory/soft-index-g-hybrid.md, operator theorem | theory/checks/soft_index_g_check.py SIDXG-C1--C5; theory/checks/soft_index_g2_check.py G2-C1--C2; theory/checks/soft_index_r2_check.py SIDXR2-C1--C3; theory/checks/soft_index_g_boundary_check.py G5-C1--C5 |
> | S-IDX-G-label | Let a finite periodic ring carry a compact Lie on-site symmetry `G`, possibly disconnected, a vacuum label `alpha` with unbroken subgroup `H_alpha`, and the effective unbroken centre `Z_{alpha,eff}=Z(H_alpha)/K_u`, where `K_u={z in Z(H_alpha):u(z) in U(1)I}`.  Let a nonzero represented Lie-algebra component `X` span a `Z(H_alpha)`-character line of character `chi_X in Hom(Z_{alpha,eff},U(1))`, and let the displayed charge and current components be globally `Z(H_alpha)`-covariant.  For every occupied central character `gamma`, `Pi_delta Q_X Pi_gamma=delta_{delta,gamma chi_X}Q_XPi_gamma` and `Pi_delta J_X Pi_gamma=delta_{delta,gamma chi_X}J_XPi_gamma`; hence the finite sector-label index is the difference `chi_X`.  Its value on every cocharacter of `Z_{alpha,eff}^0` is an integer, while a disconnected effective centre may additionally give a finite torsion label.  The descendant-range projector satisfies `P_{Q_XPi_gamma}<=Pi_{gamma chi_X}` and need not equal it, so this theorem does not imply the projected-current operator identity.  For an exact hard eigenvector, the pure `Q_X`-created FIN.8 readout is one when its denominator is nonzero.  If `X` is central then `chi_X` is trivial and this label is zero; finite groups have no nonzero `X` and no Lie-current instance. | **PROVED** | D2, D10, D26 | theory/soft-index-g4.md ⟨1⟩1--⟨1⟩7; to be restated in theory/soft-index-g-hybrid.md | theory/checks/soft_index_g4_check.py G4-C0--C4; theory/checks/soft_index_g_boundary_check.py G5-C1--C3; theory/checks/soft_index_r2_check.py SIDXR2-C2--C3 |

## Exact repair-wave work list

1. Create only the single hybrid theorem candidate `theory/soft-index-g-hybrid.md`; leave G1/G2/G4 as lane records.
2. Copy G1's root normalization, positivity, polar projection, Ward contraction, and two-register proofs.  Replace “standard periodized D10 supplies” in the theorem statement by a displayed current-covariance hypothesis; give periodized D10 only as an example.
3. Replace every “canonical irreducible centralizer block” phrase by the isotypic formula `oplus_tau I_{V_tau} tensor B_tau`; explicitly permit mixing in `B_tau` and across root-spin `n` when the centralizer type agrees.
4. Insert G2.BLOCK as a typed supporting lemma with `d:M_dom->M_out`, `A=d^dagger d`, `r=d^dagger j`, and coefficient `B=A^+r` on `M_dom`.  Display global `K` covariance for disconnected `K` before invoking Schur orthogonality.
5. Replace G2's scalar/rank-one paragraphs by (C-SCAL).  State that a nonzero one-dimensional selected source line is sufficient; do not call rank one necessary.  Keep the normalized index-one proof unchanged.
6. In the overlap dictionary choose the root circle for G2.FULL.  Say that full `H_alpha` supports a line formula only when it preserves that line; otherwise use the whole broken module `W` for equivariance or use G1's conjugate-root transport.
7. Import G4's effective-center label theorem with displayed global current covariance.  Preserve finite torsion, the trivial-character case, and the distinction `P_D<=Pi_target`.  Attribute underdetermination to (G4.19), not solely to the `8`-in-`24` ED count.
8. Add the shared SU(3) overlap calculation to the hybrid's check table: root `lambda=3`, `spec A={3^4}`, root/central projected-vector mismatch `6.94e-16`, coefficient `2i/3`, denominator `2i`, index error `1.22e-17`.  Reuse the existing checkers; no new scalar mutation is needed.
9. End with the two verbatim CLAIMS rows above and the G5 exclusion pointers.  Do not propose a third all-compact G2 headline row, a scalar per-root row, a finite-group soft row, or any G3 moment-map strengthening.

After those nine mechanical changes, promote `S-IDX-fin-G` to PROVED without another hostile round, as required by PRD.md's capped loop.  `S-IDX-G-label` is already promotable; its restatement in the hybrid is consolidation, not a new proof obligation.
