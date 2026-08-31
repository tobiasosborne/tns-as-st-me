# G3-CONSTRUCT: the first non-Möbius mode does not yet lift to an operational charge

## 1. Result and scope

**Lane verdict: G3 is not solved.**  I do not exhibit an operator that meets
the definition of $Q[\epsilon_{2,c}]$.  The sharp surviving result is an
obstruction theorem about the stated hypotheses and the four allowed source
packages:

> **Theorem G3-O (source-closed obstruction).**  The G3 hypotheses determine
> the infinitesimal action of $\epsilon_{2,c}(\tau)=\cos 2\tau$ on formal
> infrared bilocal kernels, but they do not determine
>
> 1. a well-defined derivation of the physical regulated bilocal algebra;
> 2. a spatial implementation of that derivation in either
>    $\mathcal A_R^{\mathrm{JT}}$ or $\mathcal A_{LR}^{\mathrm{JT}}$; or
> 3. any finite-$N$, finite-coupling rate $r_N\to0$.
>
> In fact, item 3 cannot follow from the G3 hypotheses as stated: qualitative
> convergence of joint moments has no mathematical implication for a
> prescribed quantitative rate.  None of the four allowed sources supplies
> the missing estimate.  Consequently no parity-even microscopic
> $Q_N[\epsilon_{2,c}]$ with the required controlled Ward defect is licensed.

This is a failure of construction, not a theorem that such an operator is
impossible in every completion of SYK/JT.  The exact failure point is the lift

\[
 \boxed{
 \text{covariance of an IR collective saddle}
 \ \not\Longrightarrow\ 
 \text{a spatial derivation of a named physical algebra}
 \ \not\Longrightarrow\ 
 \text{a quantitatively convergent even-CAR sequence}.}
\tag{1.1}
\]

The mode is therefore classified here as **KINEMATIC ONLY**.  It is not an
exactly conserved charge.  It is also not called an approximately conserved
charge, because the available breaking functional is not accompanied by an
operator insertion and a finite-$N$, finite-coupling bound on regulated Ward
matrix elements.

This lane creates no campaign claim and changes no status.  All uses of
“observable,” “affiliated,” “exists,” and “commutator register” are those of
`theory/lanes/syk-jt/corner-a-precision.md:23-172`; the operational bedrock is
`theory/lanes/syk-jt/observables-spec.md:15-84`.

| object used below | operational layer/status |
|---|---|
| finite-$N$ even Majorana algebra $\mathfrak A_N$ | **Layer 0, OBSERVABLE bedrock** |
| regulated bilocal sequences and their limiting moments | **Layer 1, operational only through the finite-$N$ measurement sequences** |
| $\mathcal A_R^{\mathrm{JT}}$ and $\mathcal A_{LR}^{\mathrm{JT}}$ | **Layer 2, named mathematical homes** |
| $t(u)$, $f(u)$, collective $G,\Sigma,g$, and their mode coordinates | **GAUGE/EFT scaffolding unless lifted by an allowed operator** |
| $\delta_2$ in this lane | **KINEMATIC formal action; not itself an observable** |

## 2. Binding target, written as a proof checklist

Set

\[
 \epsilon_2(\tau):=\epsilon_{2,c}(\tau)=\cos 2\tau,
 \qquad \epsilon_2'(\tau)=-2\sin 2\tau .
\tag{2.1}
\]

For a primary bilocal of endpoint dimension $\Delta>0$, the requested
formal action is

\[
 \delta_2 B_\Delta(u,v)
 =\bigl[\cos(2u)\partial_u+\cos(2v)\partial_v
 -2\Delta\sin(2u)-2\Delta\sin(2v)\bigr]B_\Delta(u,v).
\tag{2.2}
\]

For a compactly supported smearing function $f$, integration by parts gives
the equivalent smeared rule

\[
 \delta_2 B_\Delta(f)=B_\Delta(\mathcal L_{2,\Delta}^*f),
 \qquad
 \mathcal L_{2,\Delta}^*f
 =-\epsilon_2(u)\partial_u f-\epsilon_2(v)\partial_v f
 +(\Delta-1)\bigl(\epsilon_2'(u)+\epsilon_2'(v)\bigr)f.
\tag{2.2s}
\]

This is a named elementary computation: expand
$-\partial_u(\epsilon_2f)-\partial_v(\epsilon_2f)$ and add the two endpoint
weight terms from (2.2).  Since multiplication by the smooth $\epsilon_2$
preserves smooth compact support, (2.2s) maps a smeared formal generator to
another smeared formal generator.  It does not address physical operator
relations.

Equation (2.2) is (4.2) of the binding problem specialized to (2.1).  Its
source is the reparametrized matter kernel in
`refs/arxiv-1606.01857/GravityReparametrizationsRevised.tex:645-675`.
The desired result is not merely (2.2).  It is the conjunction of the
following six propositions.

1. **Descent.**  The Leibniz and *-extension of (2.2) preserves every operator
   relation of $\mathcal D_{X,\delta}^{\mathrm{biloc}}$, and hence defines a
   closable *-derivation there.
2. **Named home.**  That derivation is implemented on either the one-boundary
   algebra $\mathcal A_R^{\mathrm{JT}}$, or on
   $\mathcal A_{LR}^{\mathrm{JT}}$ after an explicit relational dressing.
3. **Affiliation and dynamics.**  There is a strongly continuous group
   $U_2(s)$ in that named algebra with $U_2(s)=e^{isQ_2}$; equivalently,
   the self-adjoint generator $Q_2$ is affiliated with it.
4. **Commutator register.**  A strongly dense *-algebra
   $\mathcal D$ and dense invariant Hilbert-space core $\mathscr C_2$ are
   specified, and
   \[
      i[Q_2,A]=\delta_2A,
      \qquad A\in\mathcal D_{X,\delta}^{\mathrm{biloc}},
   \tag{2.3}
   \]
   holds as a quadratic-form identity on $\mathscr C_2$.
5. **Microscopic lift.**  There are parity-even self-adjoint
   $Q_{2,N}\in\mathfrak A_N$ whose regulated commutator matrix elements
   converge to (2.3).
6. **Quantitative control.**  The convergence obeys
   \[
   \left|
    \langle\xi_N,
      \bigl(i[Q_{2,N},A_N]-(\delta_2A)_N\bigr)\eta_N
    \rangle
   \right|
   \le C_{A,\delta}\,r_N,
   \qquad r_N\longrightarrow0,
   \tag{2.4}
   \]
   with $C_{A,\delta}<\infty$ independent of $N$, and with $r_N$
   containing finite-$N$ **and** finite-coupling errors.

The regulated core is generated by

\[
 \Phi_{X,\delta}(f)
   =e^{-\delta H_X}\Phi_X(f)e^{-\delta H_X},
 \qquad
 \Phi_X(f)=\int dt\,f(t)\Phi_X(t),
\tag{2.5}
\]

together with the regulated primary bilocals, adjoints, products, and the
identity.  PW justify real-time and imaginary-time smearing, but also warn
that the unsmeared fields are operator-valued distributions
(`refs/arxiv-2301.07257/Paper.tex:817-835`).  Thus even the assertion that
(2.5) gives bounded elements of the proposed von Neumann algebra, rather
than affiliated unbounded operators with a common domain, requires the
regularity hypotheses advertised in the binding problem.  I do not silently
promote that candidate core to an already-proved commutator register.

## 3. What the sources actually construct

### 3.1 MSY: a correlator action and only the $SL(2)$ Noether triple

MSY call $t(u)$ the field variable of the Schwarzian action
(`refs/arxiv-1606.01857/GravityReparametrizationsRevised.tex:490-502`).  They
derive the dressed two-point kernel and say that higher point functions are
obtained by the same reparametrization and endpoint weights
(`refs/arxiv-1606.01857/GravityReparametrizationsRevised.tex:645-675`).  This
is exactly the source-backed content of (2.2).

The charge construction is much smaller.  MSY display three conserved
charges for the global $SL(2)$ acting on target time
(`refs/arxiv-1606.01857/GravityReparametrizationsRevised.tex:875-929`).  They
distinguish this gauged target-time action from transformations of physical
boundary time $u$: the Schwarzian breaks the latter, leaving only constant
translations as a symmetry
(`refs/arxiv-1606.01857/GravityReparametrizationsRevised.tex:1015-1018`).
Their conclusion is explicit that in two dimensions there are only the
finite $SL(2)$ charges, and that an associated larger algebra has not been
defined
(`refs/arxiv-1606.01857/GravityReparametrizationsRevised.tex:1158-1169`).

There is also a signature warning.  A full function of nearly-zero modes on
the Euclidean circle reduces in the Lorentzian fluctuation analysis to two
degrees of freedom
(`refs/arxiv-1606.01857/GravityReparametrizationsRevised.tex:875-882`).  The
binding mode $\cos2\tau$ is Euclidean, while the PW algebra and (2.5) use
real Lorentzian time.  No allowed source specifies whether the intended
Lorentzian vector field is periodic $\cos2t$, the Wick-rotated growing
field $\cosh2t$, or a compactly supported continuation.  These have
different domains and falloffs.  This ambiguity is not the main obstruction
below, but it must be fixed before (2.3) is a unique operator equation.

### 3.2 PW: the physical algebra, but no non-Möbius generator

PW quantize the four-dimensional pre-reduction boundary phase space and
construct the three self-adjoint $\widetilde{\mathrm{SL}}(2,\mathbb{R})$ generators
and their Lie algebra (`refs/arxiv-2301.07257/Paper.tex:486-505`).  The
physical Hilbert space is obtained by the diagonal constraint; its vectors are
annihilated by the total generators
(`refs/arxiv-2301.07257/Paper.tex:602-610`).  With matter the constraint is

\[
 J_a=J_a^R+J_a^L+J_a^{\mathrm{matt}},
\tag{3.1}
\]

and the physical Hilbert space is the corresponding coinvariant space
(`refs/arxiv-2301.07257/Paper.tex:636-660`).  The boundary Hamiltonians do
descend and commute
(`refs/arxiv-2301.07257/Paper.tex:662-673`).

At operator level, imposing the constraint means retaining invariant
operators (`refs/arxiv-2301.07257/Paper.tex:751-760`).  With matter, PW name
$\mathcal A_R^{\mathrm{JT}}$ as the von Neumann algebra generated by bounded
functions of $H_R$ and suitably smeared boundary matter fields
(`refs/arxiv-2301.07257/Paper.tex:817-836`).  Under their hypotheses the
two sides are mutual commutants and type $\mathrm{II}_\infty$ factors
(`refs/arxiv-2301.07257/Paper.tex:838-852,1233-1240`).

PW do **not** extend their pre-reduction phase space by a mode $n=2$, do
not construct a Diff action on either physical boundary algebra, and do not
display a unitary whose derivative gives (2.2).  Their high-energy
crossed-product discussion concerns modular flow and is only a high-energy
identification (`refs/arxiv-2301.07257/Paper.tex:907-914`); it supplies
neither $U_2(s)$ nor $Q_2$.

### 3.3 LL: an emergent algebra, not this charge

LL define the large-$N$ GNS algebra at
`refs/arxiv-2110.05497/causal_connectability_PRD.tex:663-676`, but describe
its type-$\mathrm{III}_1$ property as a conjecture
(`refs/arxiv-2110.05497/causal_connectability_PRD.tex:685-697`).  Their new
unitaries are half-sided modular translations; at leading order the algebra
is generated by generalized free fields
(`refs/arxiv-2110.05497/causal_connectability_PRD.tex:814-892`).  The source
does not identify that modular generator with the circle mode
$\epsilon_{2,c}$, does not derive (2.2) from it, and does not put it in PW's
$\mathcal A_R^{\mathrm{JT}}$.  Therefore the LL construction cannot be relabeled
as the missing G3 unitary group.

### 3.4 Bucca--Mezei: controlled effective action is not a microscopic Ward bound

Bucca--Mezei begin with the annealed-disorder, large-$N$ collective action;
its saddle equations give the leading large-$N$ propagator
(`refs/arxiv-2412.14799/Main.tex:94-116`).  Dropping the microscopic
$\partial_\tau$ term yields the reparametrization-invariant IR equations,
and restoring it explicitly breaks that invariance
(`refs/arxiv-2412.14799/Main.tex:124-146`).  Their order of limits is
first $N\to\infty$, then large $p$; they expressly note that in the
double-scaled regime all collective modes fluctuate strongly and the
Schwarzian need not dominate
(`refs/arxiv-2412.14799/Main.tex:149-161`).

At leading order in the finite-coupling parameter $\delta v$, they derive
the Schwarzian by evaluating the displacement operator on a family of
collective saddles
(`refs/arxiv-2412.14799/Main.tex:291-311`).  The orthogonal hard directions
have action $O(N/p^2)$ and are set to their saddle values; their determinant
still contributes $O(1)$ to the free energy
(`refs/arxiv-2412.14799/Main.tex:309-311`).  The alternative embedding is
described as ad hoc, can in principle mix with hard modes at
$O((\delta v)^{1/2})$, and its finite-$f$ linearized check is left for
future work (`refs/arxiv-2412.14799/Main.tex:411-425`).  Even the displayed
cutoff cancellation beyond the calculated orders is stated as an
expectation, with verification through second order
(`refs/arxiv-2412.14799/Main.tex:491-509`).

These are meaningful controls on an effective action.  They are not:

* a self-adjoint operator on the finite-$N$ Majorana Hilbert space;
* a fixed-disorder concentration estimate;
* a bound on $i[Q_{2,N},A_N]-(\delta_2A)_N$;
* a proof uniform at $N_m=8,10,12$ and $\beta J=5,10$; or
* a map from the collective stress/displacement field to an affiliated
  operator of the PW algebra.

Calling the estimate “controlled” in the effective-action sense therefore
does not produce the $r_N$ demanded by (2.4).

## 4. Proof of Theorem G3-O

### 4.1 First obstruction: the Ward rule has not descended from words to operators

Let $\mathfrak F_\delta$ be the free unital *-algebra on symbols for the
regulated primary bilocals in (2.5), before imposing any operator relations.
Equation (2.2), complex linearity, the *-rule

\[
 \delta_2(x^*)=\delta_2(x)^*,
\tag{4.1}
\]

and the Leibniz rule

\[
 \delta_2(xy)=\delta_2(x)y+x\delta_2(y)
\tag{4.2}
\]

define a formal derivation $\delta_2^{\mathrm{free}}$ on
$\mathfrak F_\delta$.  Let $I_{\mathrm{op}}$ be the *-ideal of words that
vanish in the physical representation, so that the represented bilocal
algebra is a quotient $\mathfrak F_\delta/I_{\mathrm{op}}$.

> **Lemma 4.1 (elementary quotient criterion).**  The rule
> $[x]\mapsto[\delta_2^{\mathrm{free}}x]$ is a well-defined derivation of
> $\mathfrak F_\delta/I_{\mathrm{op}}$ if and only if
> \[
>       \delta_2^{\mathrm{free}}(I_{\mathrm{op}})\subset I_{\mathrm{op}}.
> \tag{4.3}
> \]

**Proof.**  If $x-y\in I_{\mathrm{op}}$, well-definedness requires
$\delta_2^{\mathrm{free}}x-\delta_2^{\mathrm{free}}y\in I_{\mathrm{op}}$, which is
exactly (4.3).  Conversely, (4.3) makes the value independent of the chosen
representative; (4.1)--(4.2) then descend to the quotient.  $\square$

G3 assumes a *-preserving **linear** moment-preserving map $\iota$ from the
Layer-1 bilocal core to the regulated JT core.  It does not assume that
$\iota$ is a *-homomorphism, is injective modulo the common GNS null ideal,
is onto the stated JT bilocal core, or intertwines $\delta_2$.  In particular
it does not imply

\[
 \delta_2(\ker\iota)\subset\ker\iota.
\tag{4.4}
\]

Without (4.4), the prescription
$\delta_2\iota(x):=\iota(\delta_2x)$ depends on the preimage $x$.
Preservation of the finitely declared TFD joint moments does not repair this:
those moments can identify vectors only modulo their protocol GNS null
spaces, whereas (4.3) concerns **all** operator relations in the represented
algebra.  No cited passage in MSY, PW, LL, or Bucca--Mezei proves (4.3) or
(4.4).

Even if descent were granted, algebraic descent would not prove closability.
For a densely represented derivation $\delta$, closability requires that

\[
 A_k\to0,\quad \delta(A_k)\to B
 \quad\Longrightarrow\quad B=0
\tag{4.5}
\]

in the chosen operator topology.  Neither the topology nor an estimate
implying (4.5) is part of the moment-preserving hypothesis.  Thus item 1 of
the checklist fails before one asks for a charge.

This distinction is not cosmetic.  The microscopic Majorana bilocal has a
fixed contact condition following from the CAR algebra, while the conformal
primary rule comes from equations obtained after dropping the microscopic
$\partial_\tau$ term.  Bucca--Mezei impose the short-time CAR condition on
their collective field (`refs/arxiv-2412.14799/Main.tex:101-122`) and then
state that omission/restoration of $\partial_\tau$ is precisely what
restores/breaks reparametrization invariance
(`refs/arxiv-2412.14799/Main.tex:124-146`).  A proof of (4.3) therefore has
to control the regulated contact region; it cannot be inferred from the
separated-point conformal kernel.

### 4.2 Second obstruction: no spatial implementation is constructed

Suppose, for comparison, that the desired charge existed in the exact sense
of G3.  Affiliation with a named von Neumann algebra $\mathcal N$ would give

\[
 U_2(s)=e^{isQ_2}\in\mathcal N,
 \qquad
 \alpha_s(A)=U_2(s)AU_2(s)^*,
\tag{4.6}
\]

and hence an **inner**, strongly continuous automorphism group.  On its
differentiable elements, its generator would automatically preserve every
operator relation.  On a common invariant Hilbert-space core it would obey

\[
 {d\over ds}\bigg|_{s=0}
 \langle\xi,\alpha_s(A)\eta\rangle
 =\langle\xi,i[Q_2,A]\eta\rangle.
\tag{4.7}
\]

Equations (4.6)--(4.7) are the missing bridge, not consequences of (2.2).
MSY integrate over reparametrized kernels; PW define the physical algebra;
LL construct a different modular flow; Bucca--Mezei evaluate a collective
action.  None gives (4.6) for $\epsilon_2$.

The tempting PW pre-reduction extension also fails the gauge-invariance test.
For circle vector fields use the binding bracket

\[
 [\epsilon,\eta]_{\mathrm{vf}}=\epsilon\eta'-\eta\epsilon'.
\tag{4.8}
\]

An elementary computation with the Möbius rotation
$\epsilon_0=1$ gives

\[
 [\epsilon_0,\epsilon_{2,c}]_{\mathrm{vf}}
   =-2\sin2\tau=-2\epsilon_{2,s}\ne0.
\tag{4.9}
\]

Thus a right-only mode-2 generator would not commute even with the diagonal
rotation constraint.  Nor does the naive relative combination cure this:
if $L_n^X$ denotes a hypothetical side-$X$ mode, then

\[
 [L_0^L+L_0^R,L_2^R-L_2^L]
 \ \propto\ L_2^R-L_2^L\ne0.
\tag{4.10}
\]

The proportionality sign in (4.10) avoids choosing a complex-mode sign
convention; nonvanishing is fixed by (4.9).  The candidate is
GAUGE-bookkeeping, not an operator on the PW coinvariant Hilbert space.  A
matter-clock dressing or another relational dressing could in principle
repair this, but it would have to be explicit, gauge invariant, and affiliated
with $\mathcal A_{LR}^{\mathrm{JT}}$.  No such dressing is present in the
allowed sources.  Averaging over the noncompact diagonal group is not a
substitute: convergence, domain preservation, and nontriviality of that
average would each need proof.

This establishes item 2 of Theorem G3-O.  It does **not** establish that the
derivation is outer on every possible completion; there is not yet a
well-defined physical derivation to classify as inner or outer.

### 4.3 Third obstruction: qualitative convergence cannot supply $r_N$

> **Lemma 4.2 (no rate from convergence).**  Fix any positive sequence
> $r_N\to0$.  Qualitative convergence $a_N\to0$ does not imply
> $|a_N|\le C r_N$ for an $N$-independent constant $C$.

**Proof.**  Set $a_N=r_N^{1/2}$.  Then $a_N\to0$, but
$a_N/r_N=r_N^{-1/2}\to\infty$.  $\square$

Apply the lemma to any one regulated matrix element of the Ward defect in
(2.4).  The G3 hypothesis says that Layer-1 bilocal **moments converge**.  It
does not give a rate, concentration inequality, uniform integrable
majorant, spectral gap for the collective Hessian, or remainder estimate.
Therefore it cannot imply (2.4) at any advertised scale.

There is an independent two-parameter issue.  Write the prospective error
honestly as

\[
 r(N,\beta J,p,\delta;A)
 =r_{1/N}+r_{\mathrm{fc}}+r_{\mathrm{hard}}+r_{\mathrm{map}}.
\tag{4.11}
\]

At fixed finite $\beta J$, the omitted microscopic derivative explicitly
breaks reparametrization invariance.  Sending $N\to\infty$ does not by
itself send that breaking to zero.  Thus a statement $r_N\to0$ requires a
declared joint schedule such as $\beta J=\beta J(N)\to\infty$, plus a
uniform estimate along it.  No such schedule occurs in G3, and the numerical
points $\beta J\in\{5,10\}$ are fixed finite coupling.  Conversely,
Bucca--Mezei's large-$p$ analysis is taken only after large $N$, and
does not give a finite-$N$ remainder.  The two controls cannot simply be
added as powers guessed from the Schwarzian.  The exact large-$p$ relation
between their parameter $v=1-\delta v$ and $\beta\mathcal J$ is displayed at
`refs/arxiv-2412.14799/Main.tex:163-170`; it does not turn a fixed
$\beta J$ into a vanishing error as $N$ grows.

Finally, their collective action is disorder averaged, whereas Layer 0 fixes
one microscopic disorder realization.  Passing from an annealed saddle to
(2.4) for that realization requires a concentration or high-probability
theorem.  No allowed source supplies one.  This proves item 3 of Theorem
G3-O.

### 4.4 Consequence for self-adjointness and the core

There are two legitimate ways to finish the analytic part of G3:

* construct the strongly continuous group (4.6), then invoke the elementary
  Stone theorem to obtain its self-adjoint generator; or
* first define a symmetric operator on an explicit invariant core and prove
  essential self-adjointness there, for example with analytic vectors or
  deficiency-index control.

Neither route can begin here.  There is no physical $U_2(s)$, and there is
no densely defined physical operator whose deficiency indices could be
studied.  Naming the algebraic span of heat-regulated insertions does not
prove that it is invariant under an unknown generator.  Accordingly I do
not claim essential self-adjointness, affiliation, strong density of the
commutator register, or a quadratic-form identity.  This completes the proof
of Theorem G3-O.  $\square$

## 5. Route triage

### 5.1 PW phase space extended to $n=2$: rejected before reduction

One can formally write a canonical transformation of a boundary coordinate
whose first component is $\delta T=\cos2T$.  That is not yet a Dirac
observable.  PW's constructed pre-reduction charges form only the
three-dimensional isometry algebra, and physical operators must commute with
the diagonal constraints.  Equations (4.9)--(4.10) show that a bare mode-2
extension fails that test.  The route would become viable only after an
explicit relational clock/dressing is given and its group is shown to act
inside $\mathcal A_{LR}^{\mathrm{JT}}$.  That additional construction is absent.
In pure JT the obstruction is sharper: PW prove that the one-boundary algebra
is commutative and generated only by the Hamiltonian
(`refs/arxiv-2301.07257/Paper.tex:751-769`), so a nontrivial action on matter
bilocals requires the matter-extended algebra from the outset.

**Route verdict:** useful GAUGE-bookkeeping; no affiliated charge.

### 5.2 Frequency-filtered microscopic even bilinears: underdetermined

A real-time smear of products of two Heisenberg Majoranas can certainly be
made parity even and self-adjoint at every finite $N$.  The difficulty is
not membership in $\mathfrak A_N$; it is choosing the kernel so that one
and the same operator implements (2.2) on every regulated bilocal product.
That is an inverse commutator problem.  It requires, at minimum,

\[
 K_N\longmapsto
 \left\{i[Q_N[K_N],A_N]-(\delta_2A)_N:
       A\in\mathcal D_{X,\delta}^{\mathrm{biloc}}\right\}
\tag{5.1}
\]

to have a solution with a uniformly controlled inverse on the selected
matrix elements.  No source defines such a kernel, proves that the target is
in the range, bounds the smallest relevant singular value, or controls the
growth of the high-body terms generated by interacting Heisenberg evolution.
A least-squares fit on finitely many correlators would define an ED-dependent
estimator, not a proof of a common algebra derivation.  Promoting that fit to
$Q_{2,N}$ would make the numerical output define the charge rather than
test a preregistered construction.

There is a useful exact finite-dimensional reduction.  The parity-even CAR
algebra is a finite direct sum of full matrix algebras, and the elementary
finite-dimensional inner-derivation theorem says that every *-derivation of
it is

\[
 \delta_N(A)=i[Q_N,A]
\tag{5.2}
\]

for a parity-even self-adjoint $Q_N$, unique up to the center.  Hence finite
dimensional self-adjointness is not the obstruction.  The obstruction is
proving that the prescribed bilocal assignment extends to a *-derivation of
the even CAR algebra and that the resulting implementers satisfy a uniform
version of (2.4).  Equation (5.2) gives no such extension or estimate.

**Route verdict:** an implementable search space, but no selected approximant
and no $r_N$ theorem.

### 5.3 Collective-field/large-$p$ route: action derived, operator lift absent

This route most cleanly derives why the $n=2$ fluctuation is soft relative
to hard collective directions.  It nevertheless lives after disorder
averaging and after the large-$N$ collective rewrite.  The displacement
operator used to obtain the Schwarzian is an operator of the auxiliary
Liouville BCFT evaluated on collective saddles; the source does not identify
it with an even-CAR operator or with an affiliated PW boundary operator.
The admitted hard-mode mixing issue and the order of limits prevent a
finite-$N$, finite-coupling remainder estimate.

**Route verdict:** establishes the EFT kinematic mode and its explicit
breaking action; does not establish the G3 charge.

## 6. Sharpest surviving statement

### 6.1 Unconditional statement

The following is fully established within this lane.

> **Proposition 6.1 (formal mode-2 Ward operator).**  For any fixed choice of
> Lorentzian continuation of (2.1), equations (2.2), (4.1), and (4.2) define
> a *-derivation on the **free** regulated bilocal word algebra
> $\mathfrak F_\delta$.  This derivation descends to the represented
> physical algebra exactly when the relation ideal satisfies (4.3).

**Proof.**  Existence on the free algebra is the recursive definition
(4.1)--(4.2); the descent statement is Lemma 4.1.  $\square$

This is the maximal unqualified construction.  Its operational status is
**GAUGE/EFT-bookkeeping** at the collective level and **KINEMATIC correlator
action** at Layer 1.  It is not an observable or implementable operation at
Layer 0, and it is not an affiliated generator at Layer 2.

### 6.2 One clean lemma that would turn the formal rule into the G3 construction

For clarity, all missing analytic and microscopic work can be exposed as one
precise bridge rather than dispersed among power-counting slogans.

> **Unproved Lemma UI2 (uniform inner implementation of mode 2).**  Fix:
> a Lorentzian continuation of $\epsilon_2$; a joint scaling schedule
> $(N,\beta J,p)\to(\infty,\infty,p_*)$; a named physical algebra
> $\mathcal N\in\{\mathcal A_R^{\mathrm{JT}},\mathcal A_{LR}^{\mathrm{JT}}\}$; and
> representing vectors $\xi_N,\eta_N$ for a dense protocol-generated set.
> There are parity-even strongly continuous unitary groups
> $U_{2,N}(s)\in\mathfrak A_N$, a strongly continuous group
> $U_2(s)\in\mathcal N$, and an explicitly proved $r_N\to0$ such that:
>
> 1. $U_{2,N}(s)$ converges to $U_2(s)$ in all regulated joint matrix
>    elements, locally uniformly in $s$;
> 2. $\mathcal D_{X,\delta}^{\mathrm{JT}}$ is strongly dense in $\mathcal N$,
>    $U_2(s)$ preserves its bilocal subalgebra, and there is a dense
>    $U_2$-smooth core $\mathscr C_2$ for its Stone generator that is
>    invariant under both $U_2(s)$ and every element of
>    $\mathcal D_{X,\delta}^{\mathrm{JT}}$;
> 3. for every $A$ in that bilocal core and $|s|\le s_0$,
>    \[
>    \left|
>     \left\langle\xi_N,
>      \left(
>       {U_{2,N}(s)A_NU_{2,N}(s)^*-A_N\over s}
>       -(\delta_2A)_N
>      \right)\eta_N
>     \right\rangle
>    \right|
>    \le C_{A,\delta}\bigl(r_N+|s|\bigr),
>    \tag{6.1}
>    \]
>    where the estimate includes finite size, fixed-disorder, finite
>    coupling, hard-mode, and Layer-1-to-JT map errors.

UI2 is deliberately stated for unitaries.  If it were proved, the remainder
of G3 would be elementary.  Stone's theorem would give self-adjoint
generators

\[
 U_{2,N}(s)=e^{isQ_{2,N}},
 \qquad U_2(s)=e^{isQ_2}.
\tag{6.2}
\]

Finite-dimensionality makes each $Q_{2,N}$ a bounded parity-even
self-adjoint member of $\mathfrak A_N$.  Since every $U_2(s)$ lies in
$\mathcal N$, $Q_2$ is affiliated with $\mathcal N$.  Taking $s\to0$ in
(6.1) at fixed $N$ gives (2.4) at rate $r_N$; then taking $N\to\infty$ on
the common core gives (2.3) as a quadratic-form identity.
The strong-density and common-domain parts of the commutator register are
exactly item 2 of UI2.

UI2 is not advertised as progress by assumption: its third item is exactly
the missing microscopic theorem, expressed in a form that is independently
falsifiable.  The allowed sources establish none of its three items for
$n=2$.  The value of recording it is to identify the single bridge a future
proof must supply.

## 7. Conservation classification

The three permitted labels have different meanings here.

| classification | verdict for $\epsilon_{2,c}$ | reason |
|---|---|---|
| **Conserved** | **NO** | MSY's conserved target-time charges are the three global $SL(2)$ charges (`refs/arxiv-1606.01857/GravityReparametrizationsRevised.tex:875-929`), while transformations of physical time beyond translations are broken (`refs/arxiv-1606.01857/GravityReparametrizationsRevised.tex:1015-1018`). |
| **Approximately conserved with controlled breaking insertion** | **NOT ESTABLISHED** | Bucca--Mezei identify finite-coupling breaking by the boundary condition/displacement deformation and derive the leading Schwarzian (`refs/arxiv-2412.14799/Main.tex:253-309`), but do not construct the charge or bound a microscopic breaking insertion in regulated commutator matrix elements. |
| **Kinematic only** | **YES** | Equation (2.2) acts on reparametrized IR kernels, and Proposition 6.1 makes that action precise on free bilocal words.  It has no proved spatial or microscopic implementation. |

The phrase “pseudo-Goldstone mode” does not alter this classification.  MSY
say the reparametrization symmetry is both spontaneously and explicitly
broken (`refs/arxiv-1606.01857/GravityReparametrizationsRevised.tex:1127-1138`),
and Bucca--Mezei say a nontrivial quantum mechanics cannot possess exact time
reparametrization symmetry (`refs/arxiv-2412.14799/Main.tex:55-64`).  A soft
coordinate with a small effective action is not automatically an
approximately conserved operational charge.

## 8. NUMERIC HANDSHAKE

### 8.1 Status: not activated

This lane defines **no** finite-$N$ approximant $Q_{2,N}$.  Therefore the
conditional requirement in the brief—an exact ED definition and three to
five predicted Ward-defect matrix elements—is not triggered.  There are no
scientifically licensed numbers to hand to the numerical lane at

\[
 N_m\in\{8,10,12\},
 \qquad \beta J\in\{5,10\}.
\tag{8.1}
\]

Here $N_m$ is the number of Majoranas per dot (the $N$ used in the analytic
sections).  Any future handshake must also declare the interaction order
$p$, Majorana normalization, disorder variance, time units, and whether each
entry is per realization or disorder averaged.

In particular, I do not call an after-the-fact least-squares solution an
“approximant,” and I do not predict a $1/N_m$ or $1/(\beta J)$ law from
Schwarzian power counting.  Both moves would evade the decisive part of G3.

### 8.2 Minimum handoff contract for any future candidate

If a future analytic lane supplies an explicit $Q_{2,N}$ before seeing ED
data, the independent numerical lane should report at least the following
five **held-out** defects, without refitting $Q_{2,N}$:

\[
 D_N(A;\xi,\eta)
 :=\langle\xi,
   \bigl(i[Q_{2,N},A]-(\delta_2A)_N\bigr)\eta\rangle.
\tag{8.2}
\]

The future analytic candidate must specify two separated-time heat-regulated
one-sided bilocals $B_1,B_2$ by giving their exact smearing functions and
$\delta$ before diagonalization.  Let $|\Omega_{\beta,N}\rangle$ be the
normalized finite-$N$ TFD and set

\[
 |1_N\rangle
 := {B_1|\Omega_{\beta,N}\rangle\over
       \|B_1|\Omega_{\beta,N}\rangle\|}.
\tag{8.3}
\]

The five entries are

\[
\begin{array}{ll}
 D_N(B_1;\Omega,\Omega),
 &D_N(B_2;\Omega,\Omega),\\[2mm]
 D_N(B_1;1,\Omega),
 &D_N(B_1B_2;\Omega,\Omega),\\[2mm]
 D_N(B_1^*B_1;\Omega,\Omega).
\end{array}
\tag{8.4}
\]

The candidate theorem must predict each of (8.4) to be bounded by its stated
$C_{A,\delta}r(N_m,\beta J,p,\delta)$ at all six parameter pairs in (8.1),
with disorder averaging and failure probability declared.  A fit on the
first two entries followed by success on those same entries is circular; the
product and transition entries are required because a derivation is a
single operator action, not a one-correlator response kernel.

Equation (8.4) is a test protocol, not a numerical prediction from this lane.
The absence of predicted values is itself the handshake outcome: analytics
has not produced a candidate that numerics can honestly validate.

## 9. Honesty ledger

| G3 obligation | status | exact reason |
|---|---|---|
| Binding mode and bilocal variation | **DONE, formal** | Equations (2.1)--(2.2), sourced to MSY's reparametrized kernel. |
| Action on free regulated words | **DONE** | Proposition 6.1; elementary Leibniz/* construction. |
| Respect for physical operator relations | **OPEN** | Criterion (4.3) is proved, but its hypothesis is not; the assumed map $\iota$ need not preserve products or the derivation kernel. |
| Closability | **OPEN** | No topology/domain estimate of the form (4.5). |
| Named one-boundary affiliated generator | **ABSENT** | PW name $\mathcal A_R^{\mathrm{JT}}$ but construct no mode-2 unitary. |
| Explicit relational two-boundary generator | **ABSENT** | Bare right and right-minus-left modes fail the diagonal constraint test (4.9)--(4.10); no dressing is supplied. |
| Dense invariant Hilbert-space core | **ABSENT** | The heat-regulated algebra is a candidate algebraic domain, not a proved invariant core for an unknown operator. |
| Essential self-adjointness/unitary construction | **ABSENT** | There is neither a candidate symmetric operator nor a candidate unitary group. |
| Parity-even finite-$N$ approximants | **NOT DEFINED** | The filtered-bilinear search space has no source-backed kernel or uniform inverse estimate. |
| Explicit finite-$N$ and finite-coupling $r_N$ | **OBSTRUCTED BY THE HYPOTHESES** | Lemma 4.2; additionally, fixed finite coupling leaves explicit breaking and no joint limit schedule is declared. |
| Exactly conserved | **REFUTED for this mode in the EFT** | Only translations survive as physical-time symmetries; the non-Möbius direction is explicitly broken. |
| Approximately conserved with controlled insertion | **NOT ESTABLISHED** | Effective breaking action exists; microscopic operator insertion and bound do not. |
| Kinematic classification | **ESTABLISHED** | Formal correlator/word action only. |
| Outer/nonimplementable no-go on every candidate algebra | **NOT CLAIMED** | Descent and closability are unresolved, so there is not yet a physical derivation whose outerness could be proved. |
| Numerical predictions | **NOT LICENSED** | No preregistered $Q_{2,N}$; section 8 records the future test contract without inventing values. |

## 10. Final answer to G3

There is no construction, in the allowed sources or from the stated
hypotheses, of a self-adjoint
$Q[\epsilon_{2,c}]$ affiliated with $\mathcal A_R^{\mathrm{JT}}$ or an explicitly
relational $\mathcal A_{LR}^{\mathrm{JT}}$, no invariant commutator core on which
(G3a) is proved, and no parity-even microscopic sequence with an explicit
finite-$N$/finite-coupling rate.  The first sharp failure is algebraic
descent, (4.3); the second is spatial/gauge-invariant implementation,
(4.6)--(4.10); the independently decisive third is the missing rate,
Lemma 4.2 and (4.11).

What survives is the kinematic derivation (2.2) on free infrared bilocal
words and the large-$p$ derivation of its explicit-breaking effective action.
Neither is an operational charge.  Thus the requested final classification
is:

\[
 \boxed{
 Q[\epsilon_{2,c}]\text{ as an operational charge: NOT CONSTRUCTED};
 \qquad
 \epsilon_{2,c}\text{ action: KINEMATIC ONLY}.}
\tag{10.1}
\]
