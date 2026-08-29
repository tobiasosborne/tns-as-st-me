<!-- ROLE: Lamport L6b proof shard for bd tns-fea.  The SU(2) shard
     theory/soft-index-r2.md is an input and is not modified here. -->

# S-IDX-fin for compact connected on-site symmetry

**STATUS: THEOREM (general compact connected `G`, root-wise).**
**Exact class:** every represented root of the semisimple part of
`Lie(G)_C`, on every positive coroot-weight sector of a finite periodic ring,
for a displayed complex-linear adjoint-covariant current zero mode.
The central torus has no roots and hence no root-ladder identity.
**Multiplicity verdict:** the theorem preserves the canonical isotypic
decomposition for the centralizer of the root `sl_2`, not irreducible-copy
blocks and not blocks for a general unbroken subgroup `H`; the latter premise
is false, but the full-sector identity survives because it never needs it.

The theorem below is finite-dimensional representation theory plus the D10
current covariance.  Symmetry breaking selects which root directions are
physically active; it is not used to prove the projection identity.  The two
registers are kept separate exactly as required by the `ML4-Ward` ERRATUM in
`claims/CLAIMS.md` and by `soft-index-r2.md` (FIN.1)--(FIN.2).

---

## 0. Scope and status

### ⟨1⟩1. Status theorem

**ASSUME.**  `G` is a compact connected Lie group, `u` is a
finite-dimensional unitary on-site representation, and a finite periodic
ring carries a finite-range `G`-invariant Hamiltonian.  In addition, the ring
is supplied with a complex-linear current zero mode `J_0` satisfying the
adjoint covariance (G.2).  This displayed covariance is the theorem
hypothesis; a chosen periodization of a termwise invariant D10 interaction is
an example supplying it.  A relevant vacuum or sector has closed stabilizer
`H` in the D2(a)/A2 sense.  Let `alpha` be a root of the complexified
semisimple Lie algebra whose root `sl_2` is represented nontrivially on the
ring.

**PROVE.**  The exact scope and the only obstruction are as follows.

**⟨2⟩1.**  For every such root, the two registered identities (GFIN.1)
and (GFIN.2) in ⟨1⟩3 hold on every positive coroot-weight sector.  They
require no integrability, MPS ansatz, wave operator, thermodynamic limit,
scattering completeness, transitivity hypothesis `(T)`, or assumption that
the root is broken.

*Justification.*  The proof in ⟨1⟩3 uses only complete reducibility of a
finite-dimensional unitary root-`sl_2` representation and the current
commutator proved in ⟨1⟩2.

**⟨2⟩2.**  Minimal breaking hypothesis: D2(a) supplies a selected
vacuum label `gamma` with stabilizer `H=H_gamma`.  Calling a root "broken"
means only that its compact root subgroup has a nonzero tangent in `G/H`
(equivalently its root `su(2)` is not wholly contained in `Lie(H)`).  If
`Lie(H)_C` is not stable under the chosen Cartan, individual roots are not an
intrinsic broken/unbroken partition; the theorem is then stated for all roots
and the vacuum-active directions are selected afterwards.  No stronger
vacuum hypothesis is used.

*Justification.*  D2(a) defines `H_gamma`; A2 records the sector jump made by
a broken half-string.  The finite ring proof contains neither a vacuum tensor
nor a half-string.

**⟨2⟩3.**  The phrase "`H` acts on the multiplicity spaces of the
root-`sl_2` decomposition" is false for general `H`.  The exact replacement is:
the centralizer `C_H(sl_2,alpha)` acts there, and the identity is block
diagonal over that action.  A general element of `H` transports the identity
to the conjugate root triple instead of acting within one fixed-root
multiplicity space.

*Justification.*  Proved in ⟨1⟩4 and exhibited for
`SU(3) -> S(U(1) x U(2))` in ⟨1⟩7.

**⟨2⟩4.**  The precise uncovered directions are central-torus
directions and killed simple factors.  A central torus has no `E_alpha,F_alpha`
ladder from which to form `D` and `A`; if the on-site representation kills a
simple factor, its root weights are all zero and no positive sector exists.
This is an obstruction only to a root-ladder statement, not a counterexample
to (GFIN.1)--(GFIN.2).

*Justification.*  `Lie(G)_C = z_C direct-sum [g_C,g_C]` is reductive.  Roots
belong only to the semisimple summand.  The theorem explicitly quantifies over
represented roots and positive weights.

**⟨2⟩5.**  The connection to Corner A is limited and exact.  Claim G0(e)
supplies current covariance/continuity, while claim A2 and D9(d) describe how
a Weyl representative can move the selected vacuum pair.  Neither the
center-of-`H` density register nor the double-coset wall label enters the
finite projection algebra.

*Justification.*  G0 is a local current statement; A2 is a vacuum-sector
statement.  The separation is made explicit in ⟨1⟩5.

**⟨2⟩6. QED.**

---

## 1. Setup: the root and current registers

### ⟨1⟩2. Root normalization and current covariance

**ASSUME.**  The hypotheses of ⟨1⟩1.  Write `g_C` for the complexified
Lie algebra of `G`.  Choose a compact-compatible root triple

\[
 [E_\alpha,F_\alpha]=H_\alpha,\qquad
 [H_\alpha,E_\alpha]=2E_\alpha,\qquad
 [H_\alpha,F_\alpha]=-2F_\alpha,                    \tag{G.1}
\]

normalized in the ring representation so that
`Q(E_alpha)^dagger=Q(F_alpha)` and `Q(H_alpha)` is Hermitian.  Let
`J_0:g_C->End(H_N)` be the displayed complex-linear current zero mode.  Its
load-bearing hypothesis is

\[
 [Q(X),J_0(Y)]=J_0([X,Y]).                            \tag{G.2}
\]

For a periodized D10 interaction this is the periodization of the local D10
cut current.  For a bare finite ring specified only by `[H_N,Q(X)]=0`, (G.2)
must be supplied: a circle has no canonical half-line cut and global
invariance alone does not select a current improvement.

**PROVE.**  The current is an adjoint tensor and the relevant weights are
typed as follows.

**⟨2⟩1.**  On the ring, `Q(X):=sum_x q_x(X)` obeys
`[Q(X),Q(Y)]=Q([X,Y])` and `[Q(X),H_N]=0`.

*Justification.*  The on-site representation is a Lie-algebra
representation, different sites commute, and the Hamiltonian is
`G`-invariant.

**⟨2⟩2.**  The current hypothesis (G.2) is automatic in the D10
register before periodization: for the infinite interaction,
`j_b(Y)=-[H,Q_{(-infty,b]}(Y)]` obeys
`[Q(X),j_b(Y)]=j_b([X,Y])` by Jacobi, termwise local invariance, and
`[Q(X),H]=0`.  Since `j_b` has finite support, its standard finite-ring
periodization and the sum of its translates retain (G.2).

*Justification.*  D10(a), including its termwise finite-range invariance.
This is the adjoint-covariant content of claim G0(e), not its retracted
soft-factor over-read.  The abstract theorem takes (G.2) as a displayed
hypothesis so it does not use a half-line on a circle.

**⟨2⟩3.**  In particular,

\[
 [Q(E_\alpha),J_0(F_\alpha)]=J_0(H_\alpha),\quad
 [Q(H_\alpha),J_0(F_\alpha)]=-2J_0(F_\alpha),\quad
 [Q(H_\alpha),J_0(H_\alpha)]=0.                    \tag{G.3}
\]

*Justification.*  Substitute (G.1) into (G.2).

**⟨2⟩4.**  The spectrum of `Q(H_alpha)` is integral.  On an
irreducible root-`sl_2` module of highest weight `n in Z_{>=0}`, it is
`n,n-2,...,-n`.

*Justification.*  The compact-compatible triple integrates in every
finite-dimensional unitary representation to the usual root `SU(2)` algebra;
equivalently this is finite-dimensional `sl_2` representation theory.  A
non-simply-connected quotient can remove some `n`, but cannot change the
weights of the modules that occur.

**⟨2⟩5.**  For an integer `lambda>0`, define the full source and target
weight sectors

\[
 \mathcal H^\alpha_{\lambda,N}:=\ker(Q(H_\alpha)-\lambda),\qquad
 \mathcal H^\alpha_{\lambda-2,N}:=\ker(Q(H_\alpha)-(\lambda-2)). \tag{G.4}
\]

By (G.3), `J_0(H_alpha)` preserves the source sector and
`J_0(F_alpha)` maps it to the target sector.

*Justification.*  The last two commutators in (G.3).

**⟨2⟩6. QED.**

---

## 2. The ladder and the two noninterchangeable registers

### ⟨1⟩3. Theorem S-IDX-fin-G

**ASSUME.**  The setting of ⟨1⟩2 and a nonempty full sector
`mathcal H^alpha_{lambda,N}` with `lambda>0`.  Put

\[
 D_{\alpha,\lambda,N}
 :=Q(F_\alpha)|_{\mathcal H^\alpha_{\lambda,N}},\qquad
 A_{\alpha,\lambda,N}
 :=D_{\alpha,\lambda,N}^{\dagger}D_{\alpha,\lambda,N}
 \quad\hbox{on all of }\mathcal H^\alpha_{\lambda,N},          \tag{G.5}
\]

and let `P_{alpha,lambda,N}` be the orthogonal projection in the target
sector onto `ran D_{alpha,lambda,N}`.  Let

\[
 K^\alpha_{\lambda,N}:=
 \ker Q(E_\alpha)\cap\mathcal H^\alpha_{\lambda,N},\qquad
 \Pi^\alpha_{\rm hw}:\mathcal H^\alpha_{\lambda,N}
 \longrightarrow K^\alpha_{\lambda,N}                         \tag{G.6}
\]

be the root-highest-weight subspace and its orthogonal projector.
Finally, `D_{alpha,hw}` denotes `D_{alpha,lambda,N}` with domain restricted
to (G.6), and `P_{alpha,hw}` projects onto its range.

**PROVE.**  For every `psi in K^alpha_{lambda,N}`, the **full-sector
register** is

\[
 \boxed{
 P_{\alpha,\lambda,N}J_0(F_\alpha)\psi
 =D_{\alpha,\lambda,N}A_{\alpha,\lambda,N}^{-1}
   J_0(H_\alpha)\psi .}                                      \tag{GFIN.1}
\]

Here `A_{alpha,lambda,N}` is the generally non-scalar operator on the entire
source sector; it is not replaced by `lambda`.  In the separately restricted
**highest-weight register**,

\[
 D_{\alpha,\rm hw}^{\dagger}D_{\alpha,\rm hw}
 =\lambda\,\mathbb 1,
 \qquad
 \boxed{
 P_{\alpha,\rm hw}J_0(F_\alpha)\psi
 ={1\over\lambda}Q(F_\alpha)\Pi^\alpha_{\rm hw}
   J_0(H_\alpha)\psi .}                                      \tag{GFIN.2}
\]

The hybrid formula obtained by using the scalar `lambda` without first
projecting `J_0(H_alpha)psi` is not asserted and is false in the SU(3)
instance of ⟨1⟩7.

**⟨2⟩1. PROVE.**  `A_{alpha,lambda,N}` is strictly positive on the
full source sector.

**⟨3⟩1.**  Restrict the finite ring representation to the root
`sl_2`.  Complete reducibility gives

\[
 \mathcal H_N\cong
 \bigoplus_{n\ge0} V_n\otimes M_{n,\alpha},                  \tag{G.7}
\]

where `V_n` is the irreducible module of highest coroot weight `n` and
`M_{n,alpha}` is its multiplicity space.

*Justification.*  Finite-dimensional unitary representations of the compact
root `SU(2)` are completely reducible.

**⟨3⟩2.**  On the weight-`lambda` line in `V_n`,

\[
 Q(E_\alpha)Q(F_\alpha)
 ={(n+\lambda)(n-\lambda+2)\over4}\,\mathbb 1
 =:a_{n,\lambda}\mathbb 1,qquad a_{n,\lambda}\ge\lambda>0. \tag{G.8}
\]

*Justification.*  The standard `sl_2` ladder formula; occurrence of the
weight implies `n>=lambda` and matching parity.  The minimum is attained at
`n=lambda`, where `a_{n,lambda}=lambda`.

**⟨3⟩3.**  Since `Q(E_alpha)=Q(F_alpha)^dagger`, (G.8) is exactly the
block spectrum of `A_{alpha,lambda,N}` on (G.7).  Thus `A` is invertible.

*Justification.*  (G.5), (G.7), and (G.8).

**⟨3⟩4. QED.**

**⟨2⟩2. PROVE.**  The full target-range projector is

\[
 P_{\alpha,\lambda,N}
 =D_{\alpha,\lambda,N}A_{\alpha,\lambda,N}^{-1}
  D_{\alpha,\lambda,N}^{\dagger}.                            \tag{G.9}
\]

**⟨3⟩1.**  The right side is self-adjoint, is the identity on
`ran D`, and vanishes on `(ran D)^perp`.

*Justification.*  ⟨2⟩1 and finite-dimensional polar/projection algebra,
the same step as `soft-index-r2.md` (FIN.5).

**⟨3⟩2. QED.**

**⟨2⟩3. PROVE.**  On a root-highest input,

\[
 D_{\alpha,\lambda,N}^{\dagger}J_0(F_\alpha)\psi
 =J_0(H_\alpha)\psi .                                       \tag{G.10}
\]

**⟨3⟩1.**  Equation (G.3) gives
`Q(E_alpha)J_0(F_alpha)psi = J_0(H_alpha)psi
+ J_0(F_alpha)Q(E_alpha)psi`; the second term vanishes by (G.6).

*Justification.*  ⟨1⟩2.⟨2⟩3 and the highest-weight hypothesis.

**⟨3⟩2.**  Between the source and target sectors,
`Q(E_alpha)` is the adjoint of the map in (G.5), so (G.10) follows.

*Justification.*  Compact-compatible normalization in ⟨1⟩2.

**⟨3⟩3. QED.**

**⟨2⟩4. PROVE.**  Equation (GFIN.1).

**⟨3⟩1.**  Substitute (G.10) into (G.9):
`P J_0(F_alpha)psi=D A^{-1}D^dagger J_0(F_alpha)psi
=D A^{-1}J_0(H_alpha)psi`.

*Justification.*  ⟨2⟩2--⟨2⟩3.

**⟨3⟩2.**  The inverse remains to the left of
`J_0(H_alpha)psi`.  Although `psi` is highest weight,
`J_0(H_alpha)psi` need not be; (G.8) can therefore take more than one value
on that vector.

*Justification.*  The `ML4-Ward` ERRATUM identifies precisely this register
trap.  The SU(3) spectrum `{1,4}` and the scalar-mutation defect in ⟨1⟩7
show it is present beyond SU(2), not an artifact of rank one.

**⟨3⟩3. QED.**

**⟨2⟩5. PROVE.**  Equation (GFIN.2) in the separately restricted
register.

**⟨3⟩1.**  If `phi in K^alpha_{lambda,N}`, then
`Q(E_alpha)Q(F_alpha)phi=(Q(F_alpha)Q(E_alpha)+Q(H_alpha))phi
=lambda phi`.  Hence `D_hw^dagger D_hw=lambda I`.

*Justification.*  (G.1), (G.4), and (G.6).

**⟨3⟩2.**  The adjoint of the restricted-domain map includes the
source projector:

\[
 D_{\alpha,\rm hw}^{\dagger}J_0(F_\alpha)\psi
 =\Pi^\alpha_{\rm hw}Q(E_\alpha)J_0(F_\alpha)\psi
 =\Pi^\alpha_{\rm hw}J_0(H_\alpha)\psi .                    \tag{G.11}
\]

*Justification.*  ⟨2⟩3 and the definition of the adjoint of a
restricted-domain map.

**⟨3⟩3.**  Insert (G.11) and `D_hw^dagger D_hw=lambda I` into the
polar formula for `P_{alpha,hw}`.  This is (GFIN.2).

*Justification.*  Finite-dimensional projection algebra.

**⟨3⟩4. QED.**

**⟨2⟩6. PROVE.**  The optional primitive-root residue and pure
zero-mode anchor require more than the root triple, and exactly what they
require is visible.

**⟨3⟩1.**  If a normalized scalar one-particle root band vector
`psi_h` additionally obeys

\[
 \Pi^\alpha_{\rm hw}J_0(H_\alpha)\psi_h
 =J_0(H_\alpha)\psi_h=2i v_\alpha(h)\psi_h,                  \tag{G.12}
\]

then (GFIN.2) and `||Q(F_alpha)psi_h||^2=lambda` give

\[
 \langle Q(F_\alpha)\psi_h,
 P_{\alpha,\rm hw}J_0(F_\alpha)\psi_h\rangle
 =2i v_\alpha(h).                                            \tag{G.13}
\]

*Justification.*  Direct substitution.  Unlike (GFIN.1)--(GFIN.2), (G.12)
uses a scalar isolated band, its dispersion, translation covariance, and
highest-weight preservation.  Those are the facts consumed by
`soft-index-r2.md` (FIN.7), not consequences of an abstract root triple.
Under (G.12), (GFIN.1) has the same right-hand side because `A^{-1}` acts as
`1/lambda` on the highest component; hence `P_{alpha,lambda,N}` may replace
`P_{alpha,hw}` in (G.13), as it does in (FIN.3).

**⟨3⟩2.**  Independently, global symmetry gives
`[H_N,Q(F_alpha)]=0`.  Thus a pure zero-mode-created row
`Q(F_alpha)psi_h` has the same energy as `psi_h`; whenever the interacting
and reference readouts use that identical row, their ratio is exactly one.

*Justification.*  ⟨1⟩2.⟨2⟩1.  This is the group-independent
algebra behind `soft-index-r2.md` (FIN.8), with the same warning that it says
nothing about a running nonzero-momentum protocol family.

**⟨3⟩3. QED.**

**⟨2⟩7. QED.**  The core theorem is (GFIN.1)--(GFIN.2); (G.13) and
the zero-mode anchor are conditional corollaries with their extra inputs
displayed.

---

## 3. Multiplicity spaces: exact equivariance and the full-`H` obstruction

### ⟨1⟩4. Multiplicity theorem

**ASSUME.**  The decomposition (G.7).  Let
`C_alpha:=C_G(Q(E_alpha),Q(F_alpha),Q(H_alpha))` be the represented
centralizer of the root triple and `C_{H,alpha}:=H intersect C_alpha`.

**PROVE.**  The registered maps preserve the canonical isotypic decomposition
over this action; no canonical decomposition into individual equivalent
copies, no general full-`H` block statement, and no exclusion of accidental
larger commutants is asserted.

**⟨2⟩1.**  On the full weight sector, (G.7)--(G.8) give

\[
 A_{\alpha,\lambda,N}
 =\bigoplus_{n\ge\lambda}a_{n,\lambda},
   \mathbb 1_{(V_n)_\lambda}\otimes\mathbb 1_{M_{n,\alpha}}. \tag{G.14}
\]

Thus `A` and `A^{-1}` never mix multiplicity vectors; their only non-scalar
dependence is the root-spin label `n`.

*Justification.*  (G.7)--(G.8).  Each weight space `(V_n)_lambda` is one
dimensional.

**⟨2⟩2.**  Every `c in C_alpha` commutes with `D`, `A`, `P`, and
`Pi_hw`; current covariance also gives
`U(c)J_0(X)U(c)^dagger=J_0(X)` for
`X in {E_alpha,F_alpha,H_alpha}`.  Therefore both sides of
(GFIN.1) and (GFIN.2) are `C_{H,alpha}`-intertwiners and split over its
canonical isotypic summands.  If the total multiplicity register is written

\[
 \bigoplus_\tau V_\tau\otimes L_\tau,
 \qquad
 T=\bigoplus_\tau\mathbb 1_{V_\tau}\otimes B_\tau,          \tag{G.14a}
\]

then the `tau`-summands are canonical, while `B_tau` may mix equivalent
copies in `L_tau`, including occurrences carried by different root-spin
labels `n` when their centralizer type agrees.

*Justification.*  Definition of the centralizer, (G.2), (G.5)--(G.6), and
functional calculus for `A^{-1}`.

**⟨2⟩3.**  The current `J_0(H_alpha)` may mix different `n` and
different isomorphic multiplicity copies while respecting
`C_{H,alpha}`.  Formula (GFIN.1) remains valid because the full operator
`A^{-1}` assigns the correct `a_{n,lambda}^{-1}` after that mixing.  This is
where replacing `A` by the highest-weight scalar fails.

*Justification.*  Current covariance makes `J_0(H_alpha)` the weight-zero
component of an adjoint tensor, not an element of the root-`sl_2` commutant.
The proof of (GFIN.1) did not assume it preserved `n` or `M_{n,alpha}`.

**⟨2⟩4.**  A general `h in H` need not commute with the root triple.
Instead,

\[
 U(h)Q(X)U(h)^\dagger=Q(Ad_hX),\qquad
 U(h)J_0(X)U(h)^\dagger=J_0(Ad_hX).                          \tag{G.15}
\]

It therefore transports the entire registered identity for the triple
`(E_alpha,F_alpha,H_alpha)` to the identity for its conjugate triple.  It
does not define an action on fixed-`alpha` multiplicity spaces unless it
normalizes that root `sl_2`; it acts only on the multiplicity factor if it
centralizes it.

*Justification.*  On-site covariance and (G.2).  Conjugation transports
weight sectors, kernels, ranges, adjoints, inverses, and orthogonal
projectors, so it transports every object in (GFIN.1)--(GFIN.2).

**⟨2⟩5.**  Consequently the proposed full-`H` multiplicity premise is
an obstruction to an `H`-block-diagonal strengthening, but not to
S-IDX-fin-G itself.  The surviving stronger class is
`H subseteq C_G(sl_2,alpha)`; for that named class, ⟨2⟩2 is a genuine
full-`H` block decomposition.

*Justification.*  ⟨2⟩2--⟨2⟩4.

**⟨2⟩6. QED.**

---

## 4. Rank greater than one and Weyl covariance

### ⟨1⟩5. Root-orbit theorem

**ASSUME.**  A maximal torus `T subset G`, its root system `Delta`, and the
family of identities ⟨1⟩3 for represented roots.  When a vacuum is
mentioned, use the D2(a) label `gamma` and stabilizer `H_gamma`; use A2's
`(T)` hypothesis only if a global vacuum-pair double-coset classification is
also asserted.

**PROVE.**  Weyl-related identities are conjugate constraints, while
non-orthogonal roots do not admit a common multiplicity reduction.

**⟨2⟩1.**  If `w in W_G=N_G(T)/T` has representative `n_w`, phases can
be chosen so that

\[
 Ad_{n_w}(E_\alpha,F_\alpha,H_\alpha)
 =(c_wE_{w\alpha},\overline{c_w}F_{w\alpha},H_{w\alpha}),
 \qquad |c_w|=1.                                             \tag{G.16}
\]

Conjugating (GFIN.1)--(GFIN.2) by `U(n_w)` gives the corresponding identities
for `w alpha` with the same singular values and residuals.

*Justification.*  Standard Weyl action on compact-compatible root vectors,
(G.15), and invariance of polar projections under unitary conjugation.

**⟨2⟩2.**  Hence identities in one Weyl orbit are one covariant
constraint, not independent numerical laws.  In a non-simply-laced group,
long and short roots form distinct Weyl orbits; the theorem applies to each,
with its own coroot normalization (G.1).

*Justification.*  ⟨2⟩1 and the Weyl-orbit decomposition of a root
system.

**⟨2⟩3.**  For non-orthogonal roots `alpha,beta`, the two root
`sl_2` algebras generally do not commute: root-string brackets such as
`[E_alpha,F_beta]` can be nonzero.  Their weight sectors, highest-weight
projectors, and multiplicity decompositions are therefore separate
registers.  Both identities hold, but they cannot in general be simultaneously
diagonalized or multiplied as independent scalar constraints.

*Justification.*  The root-space bracket
`[g_alpha,g_{-beta}] subseteq g_{alpha-beta}` when that root exists.  Nothing
in ⟨1⟩3 asserts commutation between different-root projectors.

**⟨2⟩4.**  The Corner-A/Weyl-wall connection is real only at the
covariance level.  If `n_w in H_gamma`, the representative preserves the
selected vacuum and relates roots inside the same sector.  If
`n_w notin H_gamma`, it moves the vacuum to `n_w dot gamma`; A2 gives the
corresponding sector transport, and under `(T)` D9(d) records the vacuum-pair
double coset.  The finite identity itself neither detects nor classifies that
wall.

*Justification.*  Claims A2 and D9(d), together with (G.15)--(G.16).

**⟨2⟩5.**  Center-of-`H` charge densities and root ladders play
complementary, not interchangeable, roles.  A central direction of
`Lie(H)` is useful for a calibrated abelian charge but has no root ladder;
a broken coroot supports (GFIN.1) but need not lie in the center of `H`.
No center-density or memory-quantization statement follows from this shard.

*Justification.*  ⟨1⟩1.⟨2⟩4 and the scope separation in claims
G0/A2.  The open bead `tns-pwl` is not imported as a proved premise.

**⟨2⟩6. QED.**

---

## 5. Exact reduction to the SU(2) shard

### ⟨1⟩6. SU(2) register check

**ASSUME.**  `G=SU(2)` and use the conventions of
`soft-index-r2.md` ⟨1⟩3:

\[
 E_\alpha=S^+,qquad F_\alpha=S^-,qquad H_\alpha=2S^z,qquad
 \lambda=2m_{\lambda,N},qquad J_0(H_\alpha)=2J^z_0.          \tag{G.17}
\]

**PROVE.**  Every finite statement made here reduces to the corresponding
S-IDX-fin statement, with no normalization residue.

**⟨2⟩1.**  Under (G.17), (GFIN.1) becomes

\[
 P_{\lambda,N}J^-_0\psi
 =2D_{\lambda,N}A_{\lambda,N}^{-1}J^z_0\psi,
\]

which is exactly `soft-index-r2.md` (FIN.1), with `A` on the full sector.

*Justification.*  Substitute `J_0(H_alpha)=2J^z_0` in (GFIN.1).

**⟨2⟩2.**  Equation (GFIN.2) becomes

\[
 D_{\rm hw}^{\dagger}D_{\rm hw}=2m_{\lambda,N}\mathbb1,
 \qquad
 P_{\rm hw}J^-_0\psi
 ={1\over m_{\lambda,N}}Q_0\Pi_{\rm hw}J^z_0\psi,
\]

exactly `soft-index-r2.md` (FIN.2).

*Justification.*  Substitute `lambda=2m` and `J_0(H_alpha)=2J^z_0` in
(GFIN.2).  The projector survives.

**⟨2⟩3.**  On the primitive spin-`S` one-magnon band,
`J^z_0|h>_N=i v_S(h)|h>_N`; hence (G.12)--(G.13) give the two statements in
(FIN.3), including the residue `2i v_S(h)`.

*Justification.*  The extra band input is exactly
`soft-index-r2.md` ⟨1⟩3.⟨2⟩6--⟨2⟩8.  The root theorem does not
reprove that dynamical input for a general group.

**⟨2⟩4.**  The pure-root-zero-mode observation in
⟨1⟩3.⟨2⟩6 becomes the ADLER-Q0 anchor (FIN.8), with its original
scope warning unchanged.

*Justification.*  `F_alpha=S^- = Q_0` and `[H_N,Q_0]=0`.

**⟨2⟩5.**  At `N=4`, `h=pi/2`, `J=1`, the checker reproduces the
numbers certified by `soft_index_r2_check.py` SIDXR2-C2:

| site spin `S` | `v_S(h)` | `||S^-|h>||^2` | Ward residue |
|---:|---:|---:|---:|
| `1/2` | `1` | `2` | `2i` |
| `1` | `2` | `6` | `4i` |
| `3/2` | `3` | `10` | `6i` |

*Justification.*  `v_S(pi/2)=2S`,
`||S^-|h>||^2=2(NS-1)`, and (FIN.3).  Named gate **SIDXG-C4** imports the
same ring constructor and verifies these values under `python3 -O`.

**⟨2⟩6. QED.**

---

## 6. New sanity instance: the `SU(3)` qutrit permutation ring

### ⟨1⟩7. Exact `N=4` instance and the multiplicity obstruction

**ASSUME.**  Put one fundamental qutrit `C^3` at each of `N=4` sites and take

\[
 H_N=\sum_{x=0}^{3}(\mathbb1-P_{x,x+1}),                    \tag{G.18}
\]

with periodic indices.  Select the ferromagnetic vacuum ray
`gamma=[|0>^{tensor 4}]`, whose ray stabilizer is
`H_gamma=S(U(1) times U(2))`.  For `b in {1,2}` use

\[
 E_{0b}=|0><b|,\qquad F_{0b}=|b><0|,\qquad
 H_{0b}=|0><0|-|b><b|.                                      \tag{G.19}
\]

The two roots `alpha_01,alpha_02` are broken and non-orthogonal; the root
`alpha_12` belongs to the unbroken `U(2)` algebra.

**PROVE.**  This model realizes the general theorem, the non-scalar full
register, the failure of full-`H` multiplicity action, and Weyl covariance.

**⟨2⟩1.**  The permutation Hamiltonian (G.18) is `SU(3)`-invariant.
With the exact D10 current

\[
 J_0(X):=\sum_x-[\mathbb1-P_{x,x+1},X_x],                   \tag{G.20}
\]

dense exact diagonalization gives

\[
 spec(H_N)=\{0^{(15)},2^{(36)},4^{(18)},6^{(12)}\},qquad
 [Q(E_{0b}),J_0(F_{0b})]=J_0(H_{0b}).                        \tag{G.21}
\]

*Justification.*  `P(U tensor U)=(U tensor U)P`; (G.21) is also evaluated
directly by named gate **SIDXG-C1**.

**⟨2⟩2.**  For either broken root, the local restriction is
`C^3 downarrow sl_2 = V_1 direct-sum V_0` in coroot-highest-weight notation.
Consequently

\[
 (V_1\oplus V_0)^{\otimes4}
 \cong V_0^{\oplus9}\oplus V_1^{\oplus12}
 \oplus V_2^{\oplus9}\oplus V_3^{\oplus4}\oplus V_4.       \tag{G.22}
\]

*Justification.*  Expand by the number of doublet factors and use the
ordinary four-spin-`1/2` Clebsch--Gordan decomposition.  Dimensions give
`9+24+27+16+5=81`.

**⟨2⟩3.**  On the `lambda=1` source sector,

\[
 dim\mathcal H^{0b}_{1,4}=16,\qquad
 dim K^{0b}_{1,4}=12,\qquad
 spec A_{0b,1,4}=\{1^{(12)},4^{(4)}\}.                       \tag{G.23}
\]

Thus the full-sector `A` is manifestly non-scalar.

*Justification.*  In (G.22), weight `1` occurs in `V_1` and `V_3`; only the
`V_1` copies are highest.  Formula (G.8) gives respectively `1` and `4`.

**⟨2⟩4.**  Exact matrix evaluation on all twelve `lambda=1`
highest-weight basis vectors gives, for both `alpha_01` and `alpha_02`,

\[
 ||P J_0(F)K-D A^{-1}J_0(H)K||<2.0\times10^{-14},\qquad
 ||P_{hw}J_0(F)K-D\Pi_{hw}J_0(H)K||<2.0\times10^{-14}.       \tag{G.24}
\]

Replacing `A^{-1}` by the scalar `1/lambda` in the full register has defect
`sqrt(40)=6.324555...`; omitting `Pi_hw` in the restricted register has
defect `8.432740...`.  A separate `alpha_01`, `lambda=2` block has source
dimension `10`, highest-weight dimension `9`,
`spec(A)={2^(9),6^(1)}`; the correct restricted `1/lambda` identity has
residual below $2.0\times10^{-14}$, while omitting `1/lambda` has defect
`sqrt(24)=4.898979...`.

*Justification.*  Named gates **SIDXG-C2--C3**.  The exact structural
mutation is available as `--red-scalar-full`, and the independent projector
mutation as `--red-drop-hw-projector`.  The nonunit-weight normalization is
mutated by `--red-drop-hw-factor`; each exits `1` under `python3 -O`.

**⟨2⟩5.**  The root centralizer contains
`Y=diag(1,1,-2)` for `alpha_01`, and `[Y,E_01]=[Y,F_01]=[Y,H_01]=0`.
But the unbroken `SU(2)` on colors `1,2` contains `E_12`, with
`[H_01,E_12]=-E_12 !=0`.  Therefore the full unbroken `H_gamma` does not act
on the fixed-`alpha_01` multiplicity spaces.

*Justification.*  Direct `3x3` commutators, named gate **SIDXG-C5**.  This is
the promised precise obstruction to the stronger block claim.

**⟨2⟩6.**  The determinant-one color swap
`n|0>=|0>`, `n|1>=|2>`, `n|2>=-|1>` lies in `H_gamma` and conjugates the
`alpha_01` triple and every object in (GFIN.1)--(GFIN.2) to the
`alpha_02` triple.  Since
`tr(H_01 H_02)=1` while `tr(H_01^2)=tr(H_02^2)=2`, these are genuinely
non-orthogonal roots in one unbroken Weyl orbit, hence one covariant
constraint rather than two independent numerical laws.

*Justification.*  Direct conjugation, named gate **SIDXG-C5**, and ⟨1⟩5.

**⟨2⟩7. QED.**

---

## 7. Checker contract

### ⟨1⟩8. Red-green finite certificate

Run

```text
python3 -O theory/checks/soft_index_g_check.py
python3 -O theory/checks/soft_index_g_check.py --red-scalar-full
python3 -O theory/checks/soft_index_g_check.py --red-drop-hw-projector
python3 -O theory/checks/soft_index_g_check.py --red-drop-hw-factor
```

Green must exit `0`; each red mode must exit `1`.  The checker contains no
bare `assert` and its code-shape gate verifies that optimization cannot erase
a check.  SIDXG-C1 diagonalizes (G.18) and checks current covariance;
SIDXG-C2 checks (G.23) and the `lambda=2` block; SIDXG-C3 checks both
registered identities, including the `1/lambda` factor, and the three live
mutations; SIDXG-C4 reproduces the SU(2) SIDXR2-C2 table using the
existing checker's ring constructor; SIDXG-C5 checks the centralizer/full-`H`
distinction and the Weyl conjugation.  It tests finite matrix algebra only;
it proves no thermodynamic, vacuum-existence, scattering, or soft-limit claim.

---

## 8. MERGE PROPOSALS

### ⟨1⟩9. Proposed notation and CLAIMS rows

No existing registry is edited in this lane.  Proposed additions are:

The contracted critic round returned `0 FATAL, 2 MAJOR`; the single repair
wave made the finite-ring current register explicit, added the nonunit-weight
`1/lambda` gate, completed the current-covariance gates, and narrowed the
centralizer wording.  All repairs are mechanically verified in ⟨1⟩8.

> **Notation rows.**  `Q(E_alpha),Q(F_alpha),Q(H_alpha)` are the global
> represented compact-compatible root triple; `J_0(E_alpha),J_0(F_alpha),
> J_0(H_alpha)` its complex-linear D10 zero-mode current triple;
> `H^alpha_{lambda,N}`, `K^alpha_{lambda,N}`, `Pi^alpha_hw`,
> `D_{alpha,lambda,N}`, `A_{alpha,lambda,N}`, `P_{alpha,lambda,N}` are the
> full coroot-weight sector, its root-highest subspace/projector, the root
> lowering map, its full-sector Gram operator, and its target-range projector.

> | id | statement | status | depends on | proved in | tested in |
> |---|---|---|---|---|---|
> | S-IDX-fin-G | For a finite periodic ring with compact connected on-site `G`, finite-dimensional unitary on-site representation, finite-range `G`-invariant Hamiltonian, and a displayed complex-linear adjoint-covariant current zero mode, every represented semisimple root and every positive coroot-weight sector obey the full-sector identity `P_alpha J_0(F_alpha)psi=D_alpha A_alpha^{-1}J_0(H_alpha)psi` for root-highest `psi`, with `A_alpha=D_alpha^dagger D_alpha` on the full sector; in the separately highest-weight-restricted register `D_hw^dagger D_hw=lambda I` and `P_hwJ_0(F_alpha)psi=lambda^{-1}Q(F_alpha)Pi_hwJ_0(H_alpha)psi`.  A chosen periodization of a termwise invariant D10 interaction is an example supplying the displayed current covariance.  The identity preserves the canonical isotypic decomposition over the root-`sl_2` centralizer, with equivalent copies allowed to mix; it does not give blocks for a general unbroken `H`, which instead transports conjugate-root identities.  Central-torus directions have no root analogue. | PROVED | D10, G0, ML4-Ward | theory/soft-index-g.md ⟨1⟩3--⟨1⟩5 | theory/checks/soft_index_g_check.py SIDXG-C1--C5 |

**⟨2⟩1. QED.**  This proposals block changes no authoritative L4 or
L5 row.

---
