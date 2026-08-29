<!-- ROLE: independent G2 proposer shard for bd tns-fea.  This file takes the
     intrinsic intertwiner route and does not use a root-sl2 reduction.
     Proposed register/CLAIMS text is quarantined in MERGE PROPOSALS. -->

# THEOREM(class) — compact-G finite soft index as an intrinsic intertwiner

Status: **THEOREM(class), proposer pass; not yet through the capped critic
loop.**  The class is stated in §1.  The theorem is exact and finite-volume;
its general projected-current coefficient is an operator on a multiplicity
space.  A scalar *coefficient* is governed by the exact map criterion
(C-SCAL) in §2; a one-dimensional nonzero selected source line is sufficient,
not necessary.  The normalized Ward index itself is exactly one whenever
defined.  No root-`sl_2` reduction is used.

## 0. Result and scope

Let `G` be a compact Lie group acting on a finite chain by the on-site
representation `U_N=u^{\otimes N}`.  Its disconnected quotient is allowed but
is a spectator to the Lie-algebra current.  Let `K\leq G` be a closed subgroup
(in the broken-vacuum application, one may take `K=H_\alpha`) and choose a
nonzero complex soft direction `b\in\mathfrak g_\mathbb C` whose line is
`K`-stable:

\[
 \operatorname{Ad}_k b=\chi_b(k)b,\qquad k\in K,              \tag{G2.1}
\]

for a unitary character `\chi_b`.  Write `b^\dagger` for the compact-real-form
adjoint, in the convention `dU_N(b)^\dagger=dU_N(b^\dagger)`, and put
`h_b=[b^\dagger,b]`; then `h_b` is `K`-fixed.  The charge and current zero
modes are packaged without choosing roots as

\[
 Q_b:=dU_N(b),\qquad J_b:=J_0(b),\qquad
 [dU_N(x),J_0(y)]=J_0([x,y]).                                \tag{G2.2}
\]

The last equality is the infinitesimal form of covariance of the D10 cut
current.  It is the only Ward input.

For an arbitrary irreducible `K`-summand `W\subset\mathfrak g_\mathbb C`, the
fully packaged charge and current maps already obey the universal block
identity

\[
 \boxed{P^W_{\mu\lambda}\widehat J^W_{\mu\lambda}
 =D^W_{\mu\lambda}(\mathbb 1_{V_\mu}\otimes A_{\mu;W\lambda}^+)
  R_{\mu;W\lambda}},
 \quad R=(D^W)^\dagger\widehat J^W.                         \tag{G2.BLOCK}
\]

This is the all-compact-`G` answer (take `K=G`, or `K=H_\alpha` in the broken
register).  Its coefficient is a canonical operator on the combined
Clebsch--Gordan/chain multiplicity space.  For the polarized line (G2.1), the
Ward identity evaluates the contraction `R` and sharpens (G2.BLOCK) to the
exact full-isotype identity

\[
 \boxed{P_{\lambda,b}J_b\psi
   =D_{\lambda,b}(\mathbb 1_{V_\lambda}\otimes
      A_{\lambda,b}^{+})J_{h_b}\psi},                       \tag{G2.FULL}
\]

for every polarized input `\psi\in\ker Q_{b^\dagger}` in the source
`K`-isotype.  Here `D_{\lambda,b}` is the soft-leg intertwiner,
`A_{\lambda,b}=d_{\lambda,b}^\dagger d_{\lambda,b}\geq0` is the canonical
operator on its **full multiplicity register**, `A^+` is the Moore--Penrose
inverse (the ordinary inverse when `D_{\lambda,b}` is injective), and
`P_{\lambda,b}` projects onto `\operatorname{ran}D_{\lambda,b}`.  Thus the
compact-`G` replacement of the SU(2) ladder norm is not generally a number:
it is `A_{\lambda,b}` on a multiplicity space.

In the separately restricted polarized register the correct formula is

\[
 \boxed{P_{\lambda,b}^{\rm pol}J_b\psi
   =D_{\lambda,b}^{\rm pol}
     (\mathbb 1_{V_\lambda}\otimes(A_{\lambda,b}^{\rm pol})^+)
     \Pi_{\rm pol}J_{h_b}\psi}.                             \tag{G2.POL}
\]

The projector `\Pi_{\rm pol}` is mandatory.  This is the intrinsic version of
the full-sector versus highest-weight register split in the `ML4-Ward`
ERRATUM.

## 1. Setup and minimal Clebsch--Gordan hypotheses

### ⟨1⟩1. Finite-chain and current register

**ASSUME.**  `G` is a compact Lie group, `u:G\to U(V_{\rm site})` is
finite-dimensional, `\mathcal H_N=V_{\rm site}^{\otimes N}`, and the
finite-range Hamiltonian is `G`-invariant in the D10 register.  The zero-mode
current is complex-linear in `x\in\mathfrak g_\mathbb C`; use the adjoint
convention `Q_b^\dagger=Q_{b^\dagger}`.  Fix `K`, `b`, and `\chi_b` as in
(G2.1).

**DERIVE.**  Equation (G2.2) follows from D10 rather than being an extra
hypothesis.  If `Q(x)` is the total charge and
`j_m(y)=-[H,Q_{(-\infty,m]}(y)]`, then Jacobi and ` [Q(x),H]=0` give

\[
 [Q(x),j_m(y)]
 =-[H,[Q(x),Q_{(-\infty,m]}(y)]]
 =-[H,Q_{(-\infty,m]}([x,y])]=j_m([x,y]).                  \tag{G2.2a}
\]

Every sum is finite on the finite ring; summing the cuts gives (G2.2) for the
zero modes.  This also proves that the packaged maps below are intertwiners.

**TYPE.**  Restrict the finite `G`-module to `K` and decompose it unitarily:

\[
 \mathcal H_N\!\downarrow_K
   \cong\bigoplus_{\lambda\in\widehat K}V_\lambda\otimes M_{\lambda,N}.
                                                                    \tag{G2.3}
\]

`V_\lambda` is a fixed irreducible model and `M_{\lambda,N}` is its
multiplicity space.  Tensoring by the character gives another irreducible
`V_{\chi_b\lambda}:=\mathbb C_{\chi_b}\otimes V_\lambda`.  Covariance sends
the `\lambda` isotype to the `\chi_b\lambda` isotype.  With the canonical
identity on the irreducible factor suppressed, Schur orthogonality gives

\[
 D_{\lambda,b}:=Q_b|_{V_\lambda\otimes M_{\lambda,N}}
    =C_{b,\lambda}\otimes d_{\lambda,b},\qquad
 J_b|_{V_\lambda\otimes M_{\lambda,N}}
    =C_{b,\lambda}\otimes j_{\lambda,b},                    \tag{G2.4}
\]

where `C_{b,\lambda}:V_\lambda\to V_{\chi_b\lambda}` is the unitary
character-twist identification and
`d_{\lambda,b},j_{\lambda,b}:M_{\lambda,N}\to
M_{\chi_b\lambda,N}` are unique.  If the target isotype is absent these maps
are zero and the theorem says `P_{\lambda,b}J_b\psi=0`.

Define

\[
 A_{\lambda,b}:=d_{\lambda,b}^\dagger d_{\lambda,b}\geq0,
 \quad
 P_{\lambda,b}:=
 D_{\lambda,b}(\mathbb 1\otimes A_{\lambda,b}^+)
 D_{\lambda,b}^\dagger.                                    \tag{G2.5}
\]

The positive operator in (G2.5) is canonical after the unitary isotypic
identifications: changing those identifications conjugates `A` on
`M_{\lambda,N}` and leaves (G2.FULL) invariant.

### ⟨1⟩2. What Frobenius reciprocity does and does not force

For the one-dimensional soft module in (G2.1),

\[
 \dim\operatorname{Hom}_K(
 V_{\chi_b\lambda},\mathbb C_{\chi_b}\otimes V_\lambda)=1, \tag{G2.6}
\]

so no Clebsch--Gordan basis choice occurs in (G2.4).  The multiplicities in
the actual chain are

\[
 \dim M_{\lambda,N}
 =\int_K\overline{\chi_\lambda(k)}\,\chi_u(k)^N\,dk,         \tag{G2.7}
\]

with normalized Haar measure.  Formula (G2.7) decides presence of the source
and target isotypes, but it does **not** force `d_{\lambda,b}` to be injective,
surjective, or rank one.

If the broken directions instead form a higher-dimensional irreducible
`K`-module `W`, the relevant block is

\[
 V_\mu\otimes
 \bigl(\mathbb C^{c^\mu_{W,\lambda}}\otimes M_{\lambda,N}\bigr),
 \qquad
 c^\mu_{W,\lambda}:=\dim\operatorname{Hom}_K
 (V_\mu,W\otimes V_\lambda).                               \tag{G2.8}
\]

The same theorem holds with the CG-copy space included in the multiplicity
register.  A scalar statement is not characterized by the rank of either the
CG-copy space or the hard multiplicity: it is characterized by (C-SCAL) in
⟨1⟩10.  A nonzero one-dimensional selected source line is a sufficient
special case, while higher-rank blocks can also have a scalar coefficient.
Compactness alone supplies no instance of that criterion.

More explicitly, package the tensor operators as

\[
 \widehat Q_W:W\otimes\mathcal H_N\to\mathcal H_N,
 \quad x\otimes\psi\mapsto Q_x\psi,
 \qquad
 \widehat J_W:x\otimes\psi\mapsto J_x\psi.                 \tag{G2.8a}
\]

On the `\mu`-isotypic domain block of (G2.8), let
`D^W_{\mu\lambda}` and `\widehat J^W_{\mu\lambda}` be the restrictions of
these maps to the output `\mu` isotype.  Schur coordinates identify them as

\[
 D^W_{\mu\lambda}=\mathbb 1_{V_\mu}\otimes d_{\mu;W\lambda},
 \qquad
 \widehat J^W_{\mu\lambda}=\mathbb 1_{V_\mu}\otimes
 j_{\mu;W\lambda}.                                        \tag{G2.8b}
\]

Put `A_{\mu;W\lambda}=d^\dagger d` and
`R_{\mu;W\lambda}=(D^W)^\dagger\widehat J^W
=\mathbb 1_{V_\mu}\otimes(d^\dagger j)`.  These are the objects in
(G2.BLOCK).  Equivalently, without choosing a basis of `V_\mu`, their
multiplicity operators are the normalized Schur contractions

\[
 A_{\mu;W\lambda}
 ={1\over\dim V_\mu}\operatorname{Tr}_{V_\mu}[(D^W)^\dagger D^W],
 \qquad
 r_{\mu;W\lambda}
 ={1\over\dim V_\mu}\operatorname{Tr}_{V_\mu}[(D^W)^\dagger\widehat J^W].
                                                                    \tag{G2.8c}
\]

Thus `R=\mathbb 1_{V_\mu}\otimes r`.  No CG multiplicity-one hypothesis is
needed for the identity.

### ⟨1⟩3. Two registers that must not be mixed

The full register is all of `V_\lambda\otimes M_{\lambda,N}` and uses
`A_{\lambda,b}` from (G2.5).  Define instead

\[
 K_{\lambda,b}:=\ker Q_{b^\dagger}\cap
 (V_\lambda\otimes M_{\lambda,N}),\qquad
 \Pi_{\rm pol}:\mathcal H_{\lambda,N}\to K_{\lambda,b},    \tag{G2.9}
\]

and `D_{\lambda,b}^{\rm pol}:=D_{\lambda,b}|_{K_{\lambda,b}}`, with
`K_{\lambda,b}=V_\lambda\otimes M_{\lambda,b}^{\rm pol}` and
`D_{\lambda,b}^{\rm pol}=C_{b,\lambda}\otimes
d_{\lambda,b}^{\rm pol}`.  Put
`A_{\lambda,b}^{\rm pol}:=(d_{\lambda,b}^{\rm pol})^\dagger
d_{\lambda,b}^{\rm pol}` on the restricted multiplicity space.  The adjoint
of the physical restricted map is

\[
 (D_{\lambda,b}^{\rm pol})^\dagger
   =\Pi_{\rm pol}D_{\lambda,b}^\dagger,                    \tag{G2.10}
\]

not `D_{\lambda,b}^\dagger`.  Therefore a scalar value of
`A^{\rm pol}` may never be substituted into (G2.FULL) unless
`J_{h_b}\psi\in K_{\lambda,b}` has separately been proved.

## 2. L6b proof ladder — intrinsic projected-current identity

### ⟨1⟩4. Lemma G2-SCHUR (the canonical multiplicity operator)

**ASSUME.**  The register of ⟨1⟩1.  First take arbitrary `W,\lambda,\mu` and
the block (G2.8); then specialize to the soft line (G2.1).

**PROVE.**  Equations (G2.8b), (G2.4), and (G2.5) are intrinsic; in particular

\[
 D_{\lambda,b}^\dagger D_{\lambda,b}
   =\mathbb 1_{V_\lambda}\otimes A_{\lambda,b}.             \tag{G2.11}
\]

**⟨2⟩1.**  The packaged maps (G2.8a) are `K`-intertwiners.  Restricted to the
`\mu`-isotypic domain and output blocks, they therefore have (G2.8b)'s form.

*Justification.*  Covariance in (G2.2), complete reducibility for compact
`K`, and Schur orthogonality.  The CG-copy space is part of the multiplicity
register, so repeated Clebsch--Gordan channels cause no ambiguity.

**⟨2⟩2.**  For the soft line, equation (G2.1) and current covariance give, for `k\in K`,
`U_N(k)Q_bU_N(k)^\dagger=\chi_b(k)Q_b` and the identical formula for `J_b`.

*Justification.*  Differentiate the on-site `G` action for `Q_b`; use (G2.2)
for `J_b`.

**⟨2⟩3.**  Thus both maps in (G2.4), after the unitary twist
`C_{b,\lambda}` is removed, commute with the irreducible `K` action on
`V_\lambda`.

*Justification.*  ⟨2⟩2 and the definition
`V_{\chi_b\lambda}=\mathbb C_{\chi_b}\otimes V_\lambda`.

**⟨2⟩4.**  Haar averaging, equivalently Schur orthogonality, says that every
such map is the identity on `V_\lambda` tensored with a unique map between
multiplicity spaces.  Hence (G2.4) holds.

*Justification.*  Finite-dimensional complete reducibility for compact `K`
and Schur's lemma.  This is the step replacing the SU(2) ladder-norm
calculation.

**⟨2⟩5.**  Since `C_{b,\lambda}` is unitary,
`D^\dagger D=\mathbb 1\otimes d^\dagger d`, proving (G2.11).  Under a unitary
change of multiplicity coordinates, `d^\dagger d` is conjugated; its spectrum,
support, pseudoinverse, and the resulting physical operators are unchanged.

*Justification.*  (G2.4) and elementary tensor-product algebra.

**⟨2⟩6. QED.**

### ⟨1⟩5. Lemma G2-POLAR (range projection)

**ASSUME.**  G2-SCHUR.  No injectivity hypothesis is imposed.

**PROVE.**  `P_{\lambda,b}` in (G2.5) is the orthogonal projection onto
`\operatorname{ran}D_{\lambda,b}`.

**⟨2⟩1.**  Take a singular-value decomposition `d=W\Sigma V^\dagger`.  Then
`d(d^\dagger d)^+d^\dagger=W\,1_{\{\Sigma>0\}}W^\dagger`.

*Justification.*  The Moore--Penrose inverse replaces each nonzero
`\sigma^2` by `\sigma^{-2}` and leaves zero singular values at zero.

**⟨2⟩2.**  Tensoring ⟨2⟩1 with the identity on `V_{\chi_b\lambda}` gives
(G2.5), which is self-adjoint, idempotent, and has range
`\operatorname{ran}D_{\lambda,b}`.

*Justification.*  G2-SCHUR and ⟨2⟩1.

**⟨2⟩3.**  If `d_{\lambda,b}` is injective then
`A_{\lambda,b}>0` and `A^+=A^{-1}`.  Injectivity is an optional channel
hypothesis, not a consequence of compactness or (G2.7).

*Justification.*  `\ker(d^\dagger d)=\ker d` and ⟨1⟩2.

**⟨2⟩4.**  The identical SVD calculation on the arbitrary block (G2.8b)
gives (G2.BLOCK), with
`P^W_{\mu\lambda}=\mathbb 1_{V_\mu}\otimes d(d^\dagger d)^+d^\dagger`.

*Justification.*  G2-SCHUR ⟨2⟩1 and ⟨2⟩1--⟨2⟩2 above.

**⟨2⟩5. QED.**

### ⟨1⟩6. Lemma G2-WARD (polarized contraction)

**ASSUME.**  G2-SCHUR and
`\psi\in K_{\lambda,b}=\ker Q_{b^\dagger}\cap\mathcal H_{\lambda,N}`.

**PROVE.**

\[
 D_{\lambda,b}^\dagger J_b\psi=J_{h_b}\psi,
 \qquad h_b=[b^\dagger,b].                                 \tag{G2.12}
\]

**⟨2⟩1.**  Current covariance gives
`[Q_{b^\dagger},J_b]=J_{[b^\dagger,b]}=J_{h_b}`.

*Justification.*  Put `x=b^\dagger`, `y=b` in (G2.2).

**⟨2⟩2.**  Therefore
`Q_b^\dagger J_b\psi=J_{h_b}\psi+J_bQ_{b^\dagger}\psi
=J_{h_b}\psi`.

*Justification.*  The adjoint convention in ⟨1⟩1 and the polarized-input
hypothesis.

**⟨2⟩3.**  The left side of ⟨2⟩2 already starts and ends in the source
`\lambda` isotype: `J_b` twists it by `\chi_b` and `Q_b^\dagger` twists it
back.  Also `h_b` is `K`-fixed, so `J_{h_b}` preserves that isotype.
Consequently the restricted equality is exactly (G2.12).

*Justification.*  (G2.1), (G2.4), and
`\operatorname{Ad}_k h_b=[\overline{\chi_b(k)}b^\dagger,
\chi_b(k)b]=h_b`.

**⟨2⟩4. QED.**

### ⟨1⟩7. Theorem S-IDX-fin-G2 (full-isotype register)

**ASSUME.**  ⟨1⟩1--⟨1⟩6.

**PROVE.**  For every `\psi\in K_{\lambda,b}`, equation (G2.FULL) holds.  In
Schur coordinates it is the explicit intertwiner

\[
 P_{\lambda,b}J_b\psi
 =\bigl(C_{b,\lambda}\otimes
 d_{\lambda,b}A_{\lambda,b}^{+}r_{\lambda,b}\bigr)\psi,
                                                                    \tag{G2.13}
\]

where `J_{h_b}|_{\mathcal H_{\lambda,N}}
=\mathbb 1_{V_\lambda}\otimes r_{\lambda,b}`.

**⟨2⟩1.**  Since `h_b` is `K`-fixed, Schur orthogonality gives the displayed
factorization of `J_{h_b}`.

*Justification.*  G2-WARD ⟨2⟩3 and the same argument as G2-SCHUR.

**⟨2⟩2.**  Apply G2-POLAR and then G2-WARD:

`P J_b\psi=D(\mathbb 1\otimes A^+)D^\dagger J_b\psi
=D(\mathbb 1\otimes A^+)J_{h_b}\psi`.

*Justification.*  (G2.5) and (G2.12).

**⟨2⟩3.**  Substitute (G2.4) and ⟨2⟩1 into ⟨2⟩2 to obtain (G2.13).  If `d`
is injective, replace `A^+` by the ordinary inverse.

*Justification.*  G2-SCHUR and G2-POLAR ⟨2⟩3.

**⟨2⟩4.**  No scalar eigenvalue of `A` on a smaller subspace has been applied
to `J_{h_b}\psi`; the latter need not be polarized.

*Justification.*  `Q_{b^\dagger}J_{h_b}\psi
=[Q_{b^\dagger},J_{h_b}]\psi` need not vanish.  This is precisely the
register mechanism in the `ML4-Ward` ERRATUM.

**⟨2⟩5. QED.**

### ⟨1⟩8. Corollary S-IDX-fin-G2-pol (restricted register)

**ASSUME.**  The hypotheses of S-IDX-fin-G2, but regard
`D^{\rm pol}:K_{\lambda,b}\to\mathcal H_{\chi_b\lambda,N}` as the domain map.

**PROVE.**  Equation (G2.POL) holds.

**⟨2⟩1.**  By (G2.10) and G2-WARD,

\[
 (D^{\rm pol})^\dagger J_b\psi
 =\Pi_{\rm pol}D^\dagger J_b\psi
 =\Pi_{\rm pol}J_{h_b}\psi.                               \tag{G2.14}
\]

*Justification.*  The adjoint of a restricted-domain map and (G2.12).

**⟨2⟩2.**  Apply G2-POLAR to `D^{\rm pol}` and substitute (G2.14).  This is
(G2.POL).

*Justification.*  G2-POLAR is finite-dimensional and does not require the
domain to be the full multiplicity register.

**⟨2⟩3. QED.**

### ⟨1⟩9. Corollary S-IDX-fin-G2-index (the normalized finite index)

**ASSUME.**  `\psi\in K_{\lambda,b}` and
`\langle\psi,J_{h_b}\psi\rangle\ne0`.

**PROVE.**  The charge-created row has exact index

\[
 \boxed{\mathcal I^{\rm fin}_{\lambda,b}(\psi):=
 {\langle D_{\lambda,b}\psi,
    P_{\lambda,b}J_b\psi\rangle
  \over
  \langle\psi,J_{h_b}\psi\rangle}=1.}                     \tag{G2.15}
\]

**⟨2⟩1.**  `D\psi\in\operatorname{ran}D`, so
`\langle D\psi,PJ_b\psi\rangle=\langle D\psi,J_b\psi\rangle`.

*Justification.*  G2-POLAR.

**⟨2⟩2.**  Move `D` to the other leg and use G2-WARD:
`\langle D\psi,J_b\psi\rangle
=\langle\psi,D^\dagger J_b\psi\rangle
=\langle\psi,J_{h_b}\psi\rangle`.

*Justification.*  (G2.12).

**⟨2⟩3.**  Divide by the assumed nonzero denominator.

*Justification.*  ⟨2⟩1--⟨2⟩2.  If the denominator vanishes, the vector
identity (G2.FULL) remains valid but the ratio is deliberately undefined.

**⟨2⟩4. QED.**

### ⟨1⟩10. Scalar-coefficient boundary of the theorem

Suppress the irreducible factor and type the multiplicity maps as
`d:M_dom->M_out` and `j:M_dom->M_out`.  Put
`A=d^dagger d`, `r=d^dagger j`, and `B=A^+r` on `M_dom`.  Then
`P\widehat J=dA^+r=dB`, and the exact map-level scalar criterion is

\[
 P\widehat J=cD
 \quad\Longleftrightarrow\quad
 dA^+r=cd.                                                   \tag{C-SCAL}
\]

If `d` is injective, (C-SCAL) is equivalent to `A^{-1}r=cI`, equivalently
`r=cA`.  On one selected vector `v`, the criterion is only that `dA^+rv` be
proportional to `dv`.  A nonzero one-dimensional selected source line is
therefore sufficient, but it is not necessary: higher-rank blocks can obey
(C-SCAL).  Conversely, rank one of `d` is not sufficient on a
higher-dimensional source.  Neither the character integral (G2.7) nor
Frobenius reciprocity implies (C-SCAL).  Thus (G2.15) remains the universal
scalar **normalized index**, while a scalar formula for `P J_b\psi` itself
requires the displayed criterion.  This is a scope boundary, not an
obstruction to S-IDX-fin-G2.

## 3. Reduction to the certified SU(2) theorem

### ⟨1⟩11. Register identification

Take `G=SU(2)`, `K=U(1)_z`, `b=S^-`, and
`b^\dagger=S^+`.  The `K`-isotype of character `e^{imt}` is the weight space
`\mathcal H_{m,N}`.  Since every irreducible `U(1)` model is one-dimensional,
the whole weight space is its multiplicity register:

\[
 V_m=\mathbb C_m,\quad M_{m,N}=\mathcal H_{m,N},\quad
 D_{m,b}=S^-|_{\mathcal H_{m,N}}=D_{\lambda,N}.              \tag{G2.16}
\]

Moreover `h_b=[S^+,S^-]=2S^z`, so linearity of the current gives
`J_{h_b}=2J^z_0`.  Thus (G2.FULL), with the ordinary inverse in the
positive-weight sectors certified by S-IDX-fin, is exactly

\[
 P_{\lambda,N}J^-_0\psi
 =2D_{\lambda,N}A_{\lambda,N}^{-1}J^z_0\psi,                \tag{G2.17}
\]

with `A_{\lambda,N}=D_{\lambda,N}^\dagger D_{\lambda,N}` on the **full**
weight sector.  This is (FIN.1), not a new derivation by root reduction.

### ⟨1⟩12. Highest-weight register and the ERRATUM

Here `K_{\lambda,b}=\ker S^+\cap\mathcal H_{m,N}` and
`\Pi_{\rm pol}=\Pi_{\rm hw}`.  The separately certified SU(2) norm identity
is `A^{\rm pol}=2m\mathbb 1`; substituting it in (G2.POL), not in
(G2.FULL), gives

\[
 P_{\rm hw}J^-_0\psi
 ={1\over m}Q_0\Pi_{\rm hw}J^z_0\psi,                       \tag{G2.18}
\]

which is (FIN.2).  Dropping `\Pi_{\rm hw}` would repeat the `ML4-Ward`
ERRATUM for `n\ge2`.

For the nonzero-momentum one-magnon hard vector,
`J^z_0|h\rangle_N=iv_S(h)|h\rangle_N` and
`\|Q_0|h\rangle_N\|^2=2(NS-1)`.  Equations (G2.15) and (G2.18) therefore give

\[
 \langle h|Q_0^\dagger P J^-_0|h\rangle_N=2iv_S(h),
 \qquad \mathcal I^{\rm fin}_{m,S^-}(|h\rangle_N)=1,        \tag{G2.19}
\]

which is (FIN.3) and its finite charge-created row ratio.

### ⟨1⟩13. Numerical reduction check

The checker in §5 imports `theory/checks/soft_index_r2_check.py` and evaluates
its `N=4`, `h=\pi/2`, `S=1/2,1,3/2` cases through (G2.FULL).  It reproduces
the certified triples

\[
 (\|Q_0h\|^2,\ v_S(h),\ \langle Q_0h,PJ^-_0h\rangle)
 =(2,1,2i),(6,2,4i),(10,3,6i),                              \tag{G2.20}
\]

and the full-register projection residual is below `2\times10^{-10}` under
`python3 -O`.

## 4. A non-SU(2) instance: the SU(3) fundamental ring

### ⟨1⟩14. Model and intrinsic polarization

Let `G=SU(3)`, `V_{\rm site}=\mathbb C^3`, `N=3`, and

\[
 H={1\over2}\sum_{x\in\mathbb Z/3\mathbb Z}(\mathbb 1-P_{x,x+1}).
                                                                    \tag{G2.21}
\]

This is the SU(3)-invariant fundamental ferromagnet.  Use matrix units
`E_{ij}=|i\rangle\langle j|`, with colors numbered `1,2,3`, and choose

\[
 b=E_{21}+2E_{32},\quad b^\dagger=E_{12}+2E_{23},\quad
 h_b=[b^\dagger,b]=\operatorname{diag}(1,3,-4).             \tag{G2.22}
\]

For `k_0:=\operatorname{diag}(1,0,-1)` and
`K=\{e^{itk_0}:t\in\mathbb R\}\cong U(1)`,
the whole line `\mathbb Cb` has character `e^{-it}`.  It is a sum of two
SU(3) root spaces, not a single-root reduction; decisively,
`[h_b,b]=2E_{21}-14E_{32}` is not proportional to `b`, so
`(b^\dagger,h_b,b)` is not an `sl_2` triple.  The proof above uses only this
character line, current covariance, and Schur orthogonality.

Let

\[
 |h,2\rangle={1\over\sqrt3}\sum_{x=0}^2e^{ihx}E_{21}^{(x)}|111\rangle,
 \qquad h={2\pi\over3}.                                    \tag{G2.23}
\]

It lies in the total-`k_0` weight-2 source isotype and obeys
`Q_{b^\dagger}|h,2\rangle=0` by Fourier orthogonality.

### ⟨1⟩15. Exact ED data

The weight-2 and weight-1 isotypes have dimensions `3` and `6`.  On them the
soft map `D=Q_b` has

\[
 \operatorname{spec}(A=D^\dagger D)=\{5,5,8\}.             \tag{G2.24}
\]

Thus the intrinsic positive operator is invertible and decisively
**non-scalar**.  With D10's nearest-neighbour current
`J_y=-\sum_x[h_{x,x+1},y_x]`, direct ED gives

\[
 [Q_{b^\dagger},J_b]-J_{h_b}=0,\qquad
 J_{h_b}|h,2\rangle=-2i\sin(2\pi/3)|h,2\rangle,           \tag{G2.25}
\]

and

\[
 \begin{aligned}
 \|P J_b|h,2\rangle-D A^{-1}J_{h_b}|h,2\rangle\|
     &<2\times10^{-15},\\
 \langle Q_bh, P J_bh\rangle
     &=-i\sqrt3,\\
 \mathcal I^{\rm fin}_{2,b}(|h,2\rangle)&=1.
 \end{aligned}                                             \tag{G2.26}
\]

The orthogonal current component is genuinely present:
`\|(1-P)J_b|h,2\rangle\|=\sqrt{27/5}`.  Hence the test does not pass by
making the projection trivial.  Replacing (G2.24) by its scalar mean
`6\mathbb 1` produces residual `1/\sqrt{60}\simeq0.129099`; this is the
structural red mode.

## 5. Checker contract and result

The standalone checker is
`theory/checks/soft_index_g2_check.py`.  It contains no bare `assert`, is
safe under optimization, and has the following gates.

| gate | statement checked | green datum |
|---|---|---|
| **G2-C0** | source parses with no `ast.Assert` | PASS under `python3 -O` |
| **G2-C1** | SU(3) covariance, polarization, non-scalar multiplicity Gram, G2.FULL, G2.15, and a nonzero orthogonal current channel | `spec(A)=(5,5,8)`; projection residual `1.50e-16`; index `1+6.49e-18i`; `\|(1-P)J_bh\|=2.323790007724` |
| **G2-C2** | specialization through the imported certified SU(2) construction | rows `(2,1,2i)`, `(6,2,4i)`, `(10,3,6i)`; maximal projection residual `5.74e-16` |

Green command:

```bash
python3 -O theory/checks/soft_index_g2_check.py
```

It exits `0` and prints `ALL SOFT-INDEX-G2 GATES PASS`.

Structural red command:

```bash
python3 -O theory/checks/soft_index_g2_check.py --red-scalar-gram
```

It replaces `A` by its scalar mean on the SU(3) multiplicity register and
exits `1` at G2-C1 with projected-intertwiner residual
`1.291e-01`.  This mutation reaches the identity it is meant to test; it is
not a text, duplicated-expression, or zero-by-construction gate.  As required
by PRD.md, the green computation is a falsifier only: the L6b ladder in §2 is
the proof.

## 6. MERGE PROPOSALS

Nothing in this section has been applied to an existing file.

### 6.1 Proposed `notation.md` rows

> | Symbol | Meaning | First fixed in |
> |---|---|---|
> | `K`, `b`, `\chi_b`, `h_b` (S-IDX-fin-G register) | closed compact polarization subgroup; nonzero `K`-stable complex soft direction; its unitary character; the `K`-fixed bracket `[b^\dagger,b]`.  These symbols are local to the finite general-`G` index theorem and never denote D7's bound-pair `b` or a lattice site | theory/soft-index-g2.md (G2.1)--(G2.2) |
> | `\widehat Q_W`, `\widehat J_W` | charge and current tensor intertwiners `W\otimes\mathcal H_N\to\mathcal H_N` for an irreducible `K`-summand `W\subset\mathfrak g_\mathbb C` | theory/soft-index-g2.md (G2.8a) |
> | `D^W_{\mu\lambda}`, `A_{\mu;W\lambda}`, `R_{\mu;W\lambda}`, `P^W_{\mu\lambda}` | an isotypic soft-leg block, its canonical positive operator `d^\dagger d` on the combined CG/chain multiplicity space, the Schur contraction `(D^W)^\dagger\widehat J^W`, and the range projection | theory/soft-index-g2.md (G2.8b), (G2.BLOCK) |
> | `D_{\lambda,b}`, `A_{\lambda,b}`, `K_{\lambda,b}`, `\Pi_{\rm pol}` | character-line soft map, its **full-isotype multiplicity** Gram operator, polarized kernel `\ker Q_{b^\dagger}` in the source isotype, and its orthogonal projector.  The full and polarized-restricted registers are distinct | theory/soft-index-g2.md (G2.4)--(G2.10) |
> | `\mathcal I^{\rm fin}_{\lambda,b}(\psi)` | normalized finite Ward index `\langle D\psi,PJ_b\psi\rangle/\langle\psi,J_{[b^\dagger,b]}\psi\rangle`, equal to one when the denominator is nonzero | theory/soft-index-g2.md (G2.15) |

### 6.2 Proposed `claims/CLAIMS.md` row

> | S-IDX-fin-G | For every compact Lie on-site symmetry and finite `G`-invariant chain, the charge/current tensor maps obey the isotypic block identity `P^W\widehat J^W=D^W(1\otimes A^+)R`, with `A=d^\dagger d` canonical on the combined CG/chain multiplicity space.  If a closed `K\leq G` has a `K`-stable soft line `\mathbb Cb` and `Q_{b^\dagger}\psi=0`, then `P J_b\psi=D(1\otimes A^+)J_{[b^\dagger,b]}\psi`; the separately restricted register contains `\Pi_{pol}`, and the normalized finite index is exactly one when defined.  At `G=SU(2)`, `K=U(1)_z`, `b=S^-`, these are FIN.1--FIN.3 with the full-sector/highest-weight split of the ML4-Ward ERRATUM.  Finite groups have no Lie-current instance; a scalar projected-current coefficient beyond the normalized index is governed by `dA^+r=cd`, with a nonzero one-dimensional selected source line sufficient but not necessary. | SKETCH | D10, ML4-Ward, S-IDX-fin-r2 | theory/soft-index-g2.md §§1--4 | theory/checks/soft_index_g2_check.py G2-C0--C2; `--red-scalar-gram` |

The proposed status is **SKETCH**, despite the complete proposer proof,
because this new headline generalization has not yet passed PRD.md's capped
critic loop.  The existing SU(2) `ML4-Ward` and S-IDX-fin statuses are not
changed by this proposal.

### 6.3 Proposed replacement scope for the finite theorem in the Letter

Replace “SU(2)” in the finite index headline only by the block statement
(G2.BLOCK), followed by the polarized-line formula (G2.FULL) and normalized
index (G2.15).  Keep the SU(2) formula as the explicit corollary (G2.17)--
(G2.19).  Print a scalar general-`G` coefficient only after verifying
(C-SCAL); a nonzero one-dimensional selected source line is merely one
sufficient route.  Do not suppress `\Pi_{\rm pol}` in the restricted
register.

### 6.4 Final honest status

**THEOREM(class), proposer pass.**  The all-compact-`G` block theorem is
exact and operator-valued.  The sharper Ward evaluation and scalar normalized
index require the displayed `K`-stable soft-line and polarized-input
hypotheses; injectivity is needed only to write an ordinary inverse instead of
`A^+`.  The SU(3) instance verifies a genuinely non-scalar, non-`sl_2` block,
and the SU(2) specialization reproduces the certified S-IDX-fin numbers.  No
claim about D29, an infinite-volume soft limit, LSZ matching, integrability,
or a scalar coefficient on arbitrary multiplicity is made.
