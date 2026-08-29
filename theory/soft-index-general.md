<!-- ROLE: the single general-G hybrid repair shard for bd tns-fea. -->

# General-`G` finite soft index — operator and sector-label theorems

**STATUS: THEOREM (post-critic hybrid repair).**  This is the sole hybrid
theorem candidate ordered by
`theory/verdicts/sidx-general-g-joint-critic.md`.  It supersedes
`theory/soft-index-g.md`, `theory/soft-index-g2.md`,
`theory/soft-index-g4.md`, and `theory/soft-index-g-boundary.md` for citation
purposes; those four files remain lane and boundary records.

The shard contains exactly two headline theorems:

1. a root-wise operator theorem on represented roots of the connected
   semisimple part, with distinct full-sector and root-highest registers; and
2. a sector-label/integrality theorem for general compact `G`, including
   disconnected effective-centre characters.

G2.BLOCK appears only as supporting polar algebra.  There is no third
all-compact G2 headline, scalar per-root theorem, finite-group soft row, or G3
moment-map strengthening.

## 0. Scope, current register, and exclusions

Let a finite periodic ring carry a finite-dimensional on-site unitary
representation `U_N=u^{\otimes N}` of a compact Lie group `G` and a
`G`-invariant finite-range Hamiltonian.  Put

\[
 Q(X):=\sum_x q_x(X),\qquad X\in\mathfrak g_{\mathbb C}.
\]

The theorem is supplied with a displayed complex-linear current zero mode
`J_0:\mathfrak g_{\mathbb C}\to\operatorname{End}(\mathcal H_N)`.  Its
load-bearing local hypothesis is

\[
 [Q(X),J_0(Y)]=J_0([X,Y]).                                  \tag{H.1}
\]

Whenever a possibly disconnected compact subgroup `K\leq G` is used for a
Schur or sector statement, the required global covariance is displayed:

\[
 U_N(k)J_0(Y)U_N(k)^\dagger
   =J_0(\operatorname{Ad}_kY),\qquad k\in K.                 \tag{H.2}
\]

Infinitesimal covariance alone is not used for disconnected elements.  A
chosen finite-ring periodization of a termwise invariant D10 interaction is
an example supplying (H.1)--(H.2); it is not part of the abstract theorem
hypotheses and no canonical half-line cut on a circle is asserted.

The operator theorem has rows only for represented roots of the semisimple
Lie algebra of `G^0`.  A central-torus direction has no root ladder.  A finite
group has no nonzero Lie-algebra current component and hence no Lie-current
soft row.  Global form and disconnected components restrict or transport
admissible sectors without changing the local Gram coefficient.  The precise
computed fences are G5-C1-ABELIAN, G5-C2-FINITE, and G5-C3-GLOBAL-FORM in
`theory/soft-index-g-boundary.md` §§1--3 and
`theory/checks/soft_index_g_boundary_check.py`.

## 1. Headline theorem I — root operator identity

### 1.1 Root normalization and registers

Choose a represented root `alpha` of the semisimple Lie algebra of `G^0` and
a compact-compatible triple

\[
 [E_\alpha,F_\alpha]=H_\alpha,\qquad
 [H_\alpha,E_\alpha]=2E_\alpha,\qquad
 [H_\alpha,F_\alpha]=-2F_\alpha,                            \tag{H.3}
\]

with `Q(E_alpha)^\dagger=Q(F_alpha)` and `Q(H_alpha)` Hermitian.  From (H.1),

\[
 [Q(E_\alpha),J_0(F_\alpha)]=J_0(H_\alpha),\quad
 [Q(H_\alpha),J_0(F_\alpha)]=-2J_0(F_\alpha),\quad
 [Q(H_\alpha),J_0(H_\alpha)]=0.                            \tag{H.4}
\]

For an occupied integer coroot weight `lambda>0`, define the full source and
target sectors

\[
 \mathcal H^\alpha_{\lambda,N}:=\ker(Q(H_\alpha)-\lambda),
 \qquad
 \mathcal H^\alpha_{\lambda-2,N}:=
   \ker(Q(H_\alpha)-(\lambda-2)),                            \tag{H.5}
\]

and the full-sector maps

\[
 D_\alpha:=Q(F_\alpha)|_{\mathcal H^\alpha_{\lambda,N}},
 \qquad A_\alpha:=D_\alpha^\dagger D_\alpha.              \tag{H.6}
\]

Let `P_alpha` be the orthogonal projector onto `ran D_alpha`.  Separately put

\[
 K^\alpha_{\lambda,N}:=\ker Q(E_\alpha)\cap
 \mathcal H^\alpha_{\lambda,N},\qquad
 \Pi^\alpha_{\rm hw}:\mathcal H^\alpha_{\lambda,N}
 \to K^\alpha_{\lambda,N},                                 \tag{H.7}
\]

let `D_hw` be `D_alpha` restricted to (H.7), and let `P_hw` project onto
`ran D_hw`.  These are two noninterchangeable registers.

### 1.2 Theorem S-IDX-fin-G

For every `psi in K^alpha_{lambda,N}`, `A_alpha` is strictly positive and

\[
 \boxed{
 P_\alpha J_0(F_\alpha)\psi
 =D_\alpha A_\alpha^{-1}J_0(H_\alpha)\psi .}               \tag{H.8}
\]

This is the **full-sector Gram-inverse register**.  In the separately
root-highest-restricted register,

\[
 D_{\rm hw}^\dagger D_{\rm hw}=\lambda\mathbb 1,
 \qquad
 \boxed{
 P_{\rm hw}J_0(F_\alpha)\psi
 ={1\over\lambda}Q(F_\alpha)\Pi^\alpha_{\rm hw}
 J_0(H_\alpha)\psi .}                                      \tag{H.9}
\]

When the denominator is nonzero, the normalized Ward index is

\[
 \boxed{
 {\langle D_\alpha\psi,P_\alpha J_0(F_\alpha)\psi\rangle
  \over
  \langle\psi,J_0(H_\alpha)\psi\rangle}=1 .}               \tag{H.10}
\]

#### Proof of positivity and the full register

Restrict the finite-dimensional unitary ring representation to the root
`sl_2`.  Complete reducibility gives

\[
 \mathcal H_N\cong\bigoplus_{n\geq0}V_n\otimes M_{n,\alpha},             \tag{H.11}
\]

where `V_n` has highest coroot weight `n`.  On its weight-`lambda` line,

\[
 Q(E_\alpha)Q(F_\alpha)
 ={(n+\lambda)(n-\lambda+2)\over4}\mathbb 1
 =:a_{n,\lambda}\mathbb 1,
 \qquad a_{n,\lambda}\geq\lambda>0.                       \tag{H.12}
\]

Thus `A_alpha>0` on the entire source sector, not merely on its highest
subspace, and

\[
 P_\alpha=D_\alpha A_\alpha^{-1}D_\alpha^\dagger.          \tag{H.13}
\]

For root-highest `psi`, (H.4) gives

\[
 D_\alpha^\dagger J_0(F_\alpha)\psi
 =Q(E_\alpha)J_0(F_\alpha)\psi
 =J_0(H_\alpha)\psi.                                       \tag{H.14}
\]

Substitution of (H.14) into (H.13) proves (H.8).  The inverse remains on the
full source sector: `J_0(H_alpha)psi` need not remain root-highest, so the
scalar `lambda` cannot replace `A_alpha` in (H.8).

#### Proof of the restricted register

For `phi in K^alpha_{lambda,N}`,

\[
 Q(E_\alpha)Q(F_\alpha)\phi
 =(Q(F_\alpha)Q(E_\alpha)+Q(H_\alpha))\phi
 =\lambda\phi.                                              \tag{H.15}
\]

Hence `D_hw^dagger D_hw=lambda I`.  The adjoint of the restricted-domain map
contains the source projector, and therefore

\[
 D_{\rm hw}^\dagger J_0(F_\alpha)\psi
 =\Pi^\alpha_{\rm hw}J_0(H_\alpha)\psi.                    \tag{H.16}
\]

The polar formula for `P_hw`, followed by (H.15)--(H.16), proves (H.9).

#### Proof of the normalized index

Because `D_alpha psi` lies in `ran D_alpha`,

\[
 \begin{aligned}
 \langle D_\alpha\psi,P_\alpha J_0(F_\alpha)\psi\rangle
 &=\langle D_\alpha\psi,J_0(F_\alpha)\psi\rangle\\
 &=\langle\psi,D_\alpha^\dagger J_0(F_\alpha)\psi\rangle\\
 &=\langle\psi,J_0(H_\alpha)\psi\rangle.
 \end{aligned}                                              \tag{H.17}
\]

Division by the displayed nonzero denominator proves (H.10), without
injectivity beyond the already proved root positivity, rank one, or scalarity
of a reduced operator.  This completes the operator theorem.

### 1.3 Centralizer isotypic equivariance

Let `C_alpha` be the represented centralizer of the root triple and
`C_{H,alpha}:=H_alpha\cap C_alpha`.  The objects `D_alpha`, `A_alpha`,
`P_alpha`, and `Pi_hw`, and both registered identities, are equivariant for
this compact centralizer.  If the total multiplicity register decomposes as

\[
 \bigoplus_\tau V_\tau\otimes L_\tau,
 \qquad
 T=\bigoplus_\tau\mathbb 1_{V_\tau}\otimes B_\tau,         \tag{H.18}
\]

the isotypic summands labelled by `tau` are canonical.  Individual equivalent
copies inside `L_tau` are not.  The maps `B_tau` may mix them, including
occurrences of the same centralizer type carried by different root-spin
labels `n`.  No simultaneous diagonalization or canonical irreducible-copy
decomposition is asserted.

The Gram operator itself retains the sharper root decomposition

\[
 A_\alpha=\bigoplus_{n\geq\lambda}
 a_{n,\lambda}\mathbb 1_{(V_n)_\lambda}
 \otimes\mathbb 1_{M_{n,\alpha}},                           \tag{H.19}
\]

but the weight-zero current may mix `n` and equivalent multiplicity copies;
the full `A_alpha^{-1}` in (H.8) accounts for that mixing.

## 2. Supporting algebra — typed G2 block and scalar boundary

This section is a supporting lemma, not a headline soft-index theorem.  Let
`K` be a compact subgroup, possibly disconnected, let
`W\subset\mathfrak g_{\mathbb C}` be an irreducible `K`-module, and assume
the displayed global covariance

\[
 U_N(k)Q(Y)U_N(k)^\dagger=Q(\operatorname{Ad}_kY),\qquad
 U_N(k)J_0(Y)U_N(k)^\dagger=J_0(\operatorname{Ad}_kY)        \tag{H.20}
\]

for every `k in K`.  This hypothesis precedes all use of Haar or Schur
orthogonality and covers disconnected elements; (H.1) alone would cover only
the identity component.

Package the tensor maps

\[
 \widehat Q_W:W\otimes\mathcal H_N\to\mathcal H_N,
 \quad Y\otimes\psi\mapsto Q(Y)\psi,
 \qquad
 \widehat J_W:Y\otimes\psi\mapsto J_0(Y)\psi.              \tag{H.21}
\]

On a fixed output isotype `V_mu`, Schur coordinates suppress the irreducible
factor and give the typed multiplicity maps

\[
 d:M_{\rm dom}\longrightarrow M_{\rm out},qquad
 j:M_{\rm dom}\longrightarrow M_{\rm out},                 \tag{H.22}
\]

where `M_dom` includes the Clebsch--Gordan copy space and the source chain
multiplicity, while `M_out` is the output chain multiplicity.  Thus

\[
 D^W_{\mu\lambda}=\mathbb 1_{V_\mu}\otimes d,qquad
 \widehat J^W_{\mu\lambda}=\mathbb 1_{V_\mu}\otimes j.     \tag{H.23}
\]

Put, with every type retained,

\[
 A:=d^\dagger d\in\operatorname{End}(M_{\rm dom}),
 \qquad
 r:=d^\dagger j\in\operatorname{End}(M_{\rm dom}),
 \qquad
 B:=A^+r\in\operatorname{End}(M_{\rm dom}).                \tag{H.24}
\]

Finite-dimensional polar algebra gives the supporting block identity

\[
 \boxed{
 P^W_{\mu\lambda}\widehat J^W_{\mu\lambda}
 =D^W_{\mu\lambda}
  (\mathbb 1_{V_\mu}\otimes A^+)R_{\mu;W\lambda},}
 \qquad
 R=\mathbb 1_{V_\mu}\otimes r,                             \tag{H.25}
\]

or, after suppressing the common irreducible factor,

\[
 P\widehat J=dA^+r=dB.                                      \tag{H.26}
\]

Indeed, an SVD of `d` gives
`P=d(d^dagger d)^+d^dagger`; substituting `r=d^dagger j` proves
(H.25)--(H.26).  No injectivity or multiplicity-one hypothesis is used.

The exact scalar boundary is

\[
 \boxed{
 P\widehat J=cD
 \quad\Longleftrightarrow\quad
 dA^+r=cd.}                                                  \tag{C-SCAL}
\]

If `d` is injective, this is equivalent to `A^{-1}r=cI`, equivalently
`r=cA`.  On a selected vector `v`, only `dA^+rv` proportional to `dv` is
required.  A nonzero one-dimensional selected source line is sufficient, but
not necessary; higher-rank blocks can obey (C-SCAL), and rank one of `d` is
not sufficient on a higher-dimensional source.

## 3. Root-circle overlap, full `H_alpha`, and Weyl transport

For the overlap between the root theorem and the character-line form of the
G2 algebra, choose the compact root circle `K_alpha` generated by `H_alpha`
and take `b=F_alpha`.  The line `C F_alpha` then has weight `-2`, and the
dictionary is

| Root register | Character-line register |
|---|---|
| root circle generated by `H_alpha` | `K=K_alpha` |
| `F_alpha`, `E_alpha=F_alpha^dagger` | `b`, `b^dagger` |
| coroot weight `lambda` | one-dimensional root-circle irrep `V_lambda` |
| `H^alpha_{lambda,N}` | source multiplicity register |
| `D_alpha=Q(F_alpha)` | `d_{lambda,b}` after suppressing the circle factor |
| `A_alpha=D_alpha^dagger D_alpha` | `A_{lambda,b}=d^dagger d` |
| `ker Q(E_alpha)` and `Pi_hw` | polarized kernel and `Pi_pol` |
| `J_0(H_alpha)` | `J_[b^dagger,b]` |
| (H.8) | G2.FULL with `A^+=A^{-1}` |
| (H.9) | G2.POL plus `A_hw=lambda I` |

Thus the two routes give the same full and restricted identities on their
root-circle overlap.  Full `H_alpha` supports the line formula only when it
preserves the root line.  Otherwise one must use the whole broken module `W`
for equivariance, or use conjugate-root transport:

\[
 U_N(h)Q(Y)U_N(h)^\dagger=Q(\operatorname{Ad}_hY),\qquad
 U_N(h)J_0(Y)U_N(h)^\dagger=J_0(\operatorname{Ad}_hY).       \tag{H.27}
\]

In the standing qutrit vacuum,
`H_alpha=S(U(1)\times U(2))` rotates `F_01,F_02` as a doublet, so
`C F_01` is not an `H_alpha`-module.  This is exactly the case requiring
`W` or transport, not a full-`H_alpha` line formula.

If a Weyl representative obeys

\[
 \operatorname{Ad}_{n_w}(E_\alpha,F_\alpha,H_\alpha)
 =(c_wE_{w\alpha},\overline c_wF_{w\alpha},H_{w\alpha}),
 \qquad |c_w|=1,                                           \tag{H.28}
\]

then conjugation transports (H.8)--(H.10), their projectors, and singular
values to the `w alpha` row.  The common phase on the lowering map and current
cancels in the identity.  Disconnected elements may likewise transport or
permute root rows; they do not change the local Gram coefficient.  Projectors
for non-orthogonal roots remain separate registers.

## 4. Headline theorem II — general compact sector label and integrality

### 4.1 Effective centre and displayed global covariance

Now let `G` be general compact, possibly disconnected.  Fix a D2 vacuum label
`alpha`, its unbroken subgroup `H_alpha`, and

\[
 Z_\alpha:=Z(H_\alpha),\qquad
 K_u:=\{z\in Z_\alpha:u(z)\in U(1)\mathbb 1\},\qquad
 Z_{\alpha,\mathrm{eff}}:=Z_\alpha/K_u.                    \tag{H.29}
\]

All occupied `Z_alpha` characters have the same restriction to `K_u`, so
they form an affine torsor whose differences lie in

\[
 \Lambda_\alpha^*:=\widehat{Z_{\alpha,\mathrm{eff}}}
 =\operatorname{Hom}(Z_{\alpha,\mathrm{eff}},U(1)).         \tag{H.30}
\]

This character group has the free lattice of the connected central torus and
may also have a finite torsion part from disconnected components.

Let a nonzero represented Lie component `X in g_C` span a `Z_alpha` character
line with character `chi_X in Lambda_alpha^*`.  Put `Q_X=Q(X)` and let `J_X`
be the displayed finite-ring current component.  The global current
covariance is a hypothesis:

\[
 U_N(z)Q_XU_N(z)^\dagger=\chi_X(z)Q_X,qquad
 U_N(z)J_XU_N(z)^\dagger=\chi_X(z)J_X,qquad z\in Z_\alpha. \tag{H.31}
\]

The first formula follows from the on-site representation; the second is the
specialization of the displayed current register (H.2).  A chosen D10
periodization is again only an example supplying it.

### 4.2 Theorem S-IDX-G-label

Let `Pi_gamma` be the projector onto an occupied central character `gamma`.
Then

\[
 \boxed{
 \Pi_\delta Q_X\Pi_\gamma
 =\delta_{\delta,\gamma\chi_X}Q_X\Pi_\gamma,\qquad
 \Pi_\delta J_X\Pi_\gamma
 =\delta_{\delta,\gamma\chi_X}J_X\Pi_\gamma.}              \tag{H.32}
\]

Consequently the finite sector-label index is

\[
 \boxed{
 \operatorname{ind}_{Z_\alpha}(X;\gamma)
 :=(\gamma\chi_X)\gamma^{-1}=\chi_X\in\Lambda_\alpha^*.}   \tag{H.33}
\]

For every cocharacter
`eta:U(1)->Z_{alpha,eff}^0`,

\[
 \chi_X(\eta(e^{i\theta}))=e^{in_\eta(\chi_X)\theta},
 \qquad \Delta q_\eta=n_\eta(\chi_X)\in\mathbb Z.         \tag{H.34}
\]

A disconnected effective centre may additionally contribute the finite
torsion label retained in (H.33); it does not create an integer circle
coordinate.

#### Proof

If `psi=Pi_gamma psi`, (H.31) gives

\[
 U_N(z)Q_X\psi=\gamma(z)\chi_X(z)Q_X\psi,
 \qquad
 U_N(z)J_X\psi=\gamma(z)\chi_X(z)J_X\psi.                  \tag{H.35}
\]

Haar orthogonality of distinct characters proves (H.32).  Dividing the
target label `gamma chi_X` by the source label `gamma` proves (H.33); the
common affine restriction on `K_u` cancels.  Finally, every continuous
character of `U(1)` is `e^{i theta}->e^{in theta}` for a unique integer `n`,
which proves (H.34).  This is compact representation covariance, not an
expectation-value quantization statement.

If `psi_h` is an exact hard eigenvector and `Q_X psi_h` is nonzero, then
`[H_N,Q_X]=0` gives the separately scoped pure-zero-mode anchor

\[
 \mathcal R_{Q_X\psi_h}(0)=1                                \tag{H.36}
\]

whenever its FIN.8 denominator is nonzero.  Equation (H.36) says nothing
about a running nonzero-momentum protocol family.

### 4.3 Descendant projector is strictly finer

Put

\[
 D_\gamma:=Q_X\Pi_\gamma,
 \qquad P_{D,\gamma}:=P_{\operatorname{ran}D_\gamma}.
\]

Equation (H.32) implies only

\[
 \operatorname{ran}D_\gamma\subseteq
 \operatorname{ran}\Pi_{\gamma\chi_X},
 \qquad P_{D,\gamma}\leq\Pi_{\gamma\chi_X}.               \tag{H.37}
\]

The SU(3) four-qutrit computation proves strict inclusion in its instance:

\[
 \dim\mathcal H_{5/3}=8,qquad
 \dim\mathcal H_{2/3}=24,qquad
 \operatorname{rank}D=8,                                  \tag{H.38}
\]

and the live replacement defect is

\[
 \|(\Pi_{2/3}-P_D)J_X|h;2\rangle\|=\sqrt{8/3}.             \tag{H.39}
\]

These ED facts prove projector fineness and show that substituting the
central-sector projector changes this current vector.  They do not alone
prove information-theoretic underdetermination.  That conclusion is supplied
by G4's abstract same-label/different-map witness (G4.19): for one source line
and a two-dimensional target of the same character,

\[
 D\psi=e_1,qquad J\psi=a e_1+b e_2,                        \tag{H.40}
\]

all choices of `a,b` have the same source and target labels while
`P_DJ\psi=a e_1` varies.  Thus sector labels alone do not determine the
operator coefficient.

If `X` is central, its adjoint character is trivial and the label (H.33) is
zero; this remains distinct from a root row, because a central direction has
no ladder.  If `G` is finite, no nonzero `X` exists and (H.32)--(H.36) have no
Lie-current instance.  An independently supplied finite torsion sector label
or G5's finite-string endpoint identity is a different statement.

## 5. Exact reductions and shared checks

### 5.1 SU(2) reduction

Use the authoritative S-IDX-fin-r2 dictionary

\[
 E_\alpha=S^+,qquad F_\alpha=S^-,\qquad H_\alpha=2S^z,
 \qquad \lambda=2m,qquad J_0(H_\alpha)=2J^z_0.             \tag{H.41}
\]

Then (H.8) and (H.9) become exactly

\[
 PJ^-_0\psi=2DA^{-1}J^z_0\psi,
 \qquad
 P_{\rm hw}J^-_0\psi=Q_0\Pi_{\rm hw}J^z_0\psi/m.          \tag{H.42}
\]

At `N=4`, `h=pi/2`, and site spins `S=1/2,1,3/2`, all operator and label
routes reproduce S-IDX-fin-r2:

| `S` | `v_S(h)` | `||Q_0|h>||^2` | residue |
|---:|---:|---:|---:|
| `1/2` | `1` | `2` | `2i` |
| `1` | `2` | `6` | `4i` |
| `3/2` | `3` | `10` | `6i` |

The maximum measured mismatch is `1.96e-15`.  This is the exact reduction to
the authoritative PROVED row S-IDX-fin-r2, not a new dynamical claim.

### 5.2 Shared SU(3) overlap calculation

On G4's `N=4` hard state `|h;2>`, relative to the root `alpha_01`, the state
is root-highest and has `lambda=3`.  The shared calculation is:

| overlap datum | value |
|---|---:|
| root `lambda` | `3` |
| root source/target dimensions | `4 -> 16` |
| root-highest dimension | `4` |
| `spec A` | `{3^4}` |
| root/central projected-vector mismatch | `6.94e-16` |
| projected coefficient | `2i/3` |
| denominator | `2i` |
| normalized index | `1-1.22e-17 i` |
| index error | `1.22e-17` |
| root Gram/Ward residual | `3.85e-17` |

G4's coarser central block has dimensions `8 -> 24` and charge rank `8`.
The central projector is a direct sum of root-weight blocks; it is not
substituted for the `alpha_01` descendant-range projector.  The coefficient
`2i/3` and residue `2i` are the same diagnostic values recorded in G4.

The values required verbatim by repair step 8 are therefore: root `lambda=3`,
`spec A={3^4}`, root/central projected-vector mismatch `6.94e-16`,
coefficient `2i/3`, denominator `2i`, and index error `1.22e-17`.

### 5.3 Checker table

| gate | retained check |
|---|---|
| `soft_index_g_check.py` SIDXG-C1--C3 | SU(3) root covariance, Gram spectra, full/restricted identities, and existing structural mutations |
| `soft_index_g_check.py` SIDXG-C4 | exact S-IDX-fin-r2 SU(2) rows |
| `soft_index_g_check.py` SIDXG-C5 | centralizer/full-`H` fence and Weyl transport |
| `soft_index_g_check.py` SIDXG-C6 | shared `lambda=3` root/central overlap and every number in §5.2; green-only, with no new mutation mode |
| `soft_index_g2_check.py` G2-C1--C2 | typed non-scalar polar block, normalized index one, and SU(2) reduction |
| `soft_index_g4_check.py` G4-C1--C4 | global central covariance, label shift, `8<24` projector split, outside norm, and SU(2) reduction |
| `soft_index_g_boundary_check.py` G5-C1--C5 | abelian, finite, global-form, multiplicity, and register exclusions |
| `soft_index_r2_check.py` SIDXR2-C1--C3 | authoritative SU(2) two-register identity, residues, and pure-zero-mode anchor |

Passing these finite checks is corroboration only; the root polar/Ward proof
and the character proof carry the status.

## 6. Exclusion pointers

- Central-torus/abelian directions: no root row, not a zero-valued root
  instance; see `theory/soft-index-g-boundary.md` §1 and G5-C1-ABELIAN.
- Finite groups: no Lie-current row; the finite-string endpoint is a
  different statement; see the boundary shard §2 and G5-C2-FINITE.
- Global form and disconnected elements: sector-lattice restriction,
  torsion labels, pairing, or root transport; see the boundary shard §3 and
  G5-C3-GLOBAL-FORM.
- Nonabelian multiplicity and the two-register trap: retain the full Gram
  inverse or the separately projected highest-weight formula; see the
  boundary shard §§4--5 and G5-C4--C5.

## 7. MERGE PROPOSALS

The following two CLAIMS rows are reproduced verbatim from the critic's
PROMOTABLE/design section, as ordered.  In particular, their internal
`theory/soft-index-g-hybrid.md` pointer is not normalized to this work order's
delivery filename `theory/soft-index-general.md`.

> | id | statement | status | depends on | proved in | tested in |
> |---|---|---|---|---|---|
> | S-IDX-fin-G | Let a finite periodic ring carry a compact Lie on-site symmetry `G` and a displayed complex-linear current zero mode satisfying `[Q(X),J_0(Y)]=J_0([X,Y])`.  For every represented root `alpha` of the semisimple Lie algebra of `G^0`, every occupied positive coroot-weight sector `H^alpha_{lambda,N}`, and every `psi in ker Q(E_alpha) intersect H^alpha_{lambda,N}`, put `D_alpha=Q(F_alpha)|_{H^alpha_{lambda,N}}`, `A_alpha=D_alpha^dagger D_alpha`, and let `P_alpha` project onto `ran D_alpha`.  Then `A_alpha>0` and `P_alpha J_0(F_alpha)psi=D_alpha A_alpha^{-1}J_0(H_alpha)psi`; in the separately root-highest-restricted register, `D_hw^dagger D_hw=lambda I` and `P_hwJ_0(F_alpha)psi=lambda^{-1}Q(F_alpha)Pi_hwJ_0(H_alpha)psi`.  When `langle psi,J_0(H_alpha)psi rangle` is nonzero, the normalized Ward index `langle D_alpha psi,P_alpha J_0(F_alpha)psi rangle/langle psi,J_0(H_alpha)psi rangle` is exactly one.  The maps preserve the canonical isotypic decomposition of the represented root-`sl_2` centralizer, while equivalent copies may mix; a general unbroken `H` instead transports conjugate-root rows unless it normalizes the root line.  At `G=SU(2)` the two registers and the residues `(2i,4i,6i)` reduce exactly to S-IDX-fin-r2.  Central-torus directions have no root row, finite groups have no Lie-current row, and disconnected/global-form data enter through the separate sector-label theorem. | **PROVED** (after the single mechanical hybrid repair ordered in `theory/verdicts/sidx-general-g-joint-critic.md`) | D10, ML4-Ward, S-IDX-fin-r2 | theory/soft-index-g-hybrid.md, operator theorem | theory/checks/soft_index_g_check.py SIDXG-C1--C5; theory/checks/soft_index_g2_check.py G2-C1--C2; theory/checks/soft_index_r2_check.py SIDXR2-C1--C3; theory/checks/soft_index_g_boundary_check.py G5-C1--C5 |
> | S-IDX-G-label | Let a finite periodic ring carry a compact Lie on-site symmetry `G`, possibly disconnected, a vacuum label `alpha` with unbroken subgroup `H_alpha`, and the effective unbroken centre `Z_{alpha,eff}=Z(H_alpha)/K_u`, where `K_u={z in Z(H_alpha):u(z) in U(1)I}`.  Let a nonzero represented Lie-algebra component `X` span a `Z(H_alpha)`-character line of character `chi_X in Hom(Z_{alpha,eff},U(1))`, and let the displayed charge and current components be globally `Z(H_alpha)`-covariant.  For every occupied central character `gamma`, `Pi_delta Q_X Pi_gamma=delta_{delta,gamma chi_X}Q_XPi_gamma` and `Pi_delta J_X Pi_gamma=delta_{delta,gamma chi_X}J_XPi_gamma`; hence the finite sector-label index is the difference `chi_X`.  Its value on every cocharacter of `Z_{alpha,eff}^0` is an integer, while a disconnected effective centre may additionally give a finite torsion label.  The descendant-range projector satisfies `P_{Q_XPi_gamma}<=Pi_{gamma chi_X}` and need not equal it, so this theorem does not imply the projected-current operator identity.  For an exact hard eigenvector, the pure `Q_X`-created FIN.8 readout is one when its denominator is nonzero.  If `X` is central then `chi_X` is trivial and this label is zero; finite groups have no nonzero `X` and no Lie-current instance. | **PROVED** | D2, D10, D26 | theory/soft-index-g4.md ⟨1⟩1--⟨1⟩7; to be restated in theory/soft-index-g-hybrid.md | theory/checks/soft_index_g4_check.py G4-C0--C4; theory/checks/soft_index_g_boundary_check.py G5-C1--C3; theory/checks/soft_index_r2_check.py SIDXR2-C2--C3 |
