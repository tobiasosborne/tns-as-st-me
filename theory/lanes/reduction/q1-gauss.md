# Q1: definitional audit against 3+1 lattice QED

## 0. Scope, status discipline, and the continuum target

This is a definitional reduction, not a promotion of any campaign claim.  The
campaign inputs used below retain their ledger statuses: **WI**, **A1**, and
**A2** are **PROVED** only in the registers stated in
`claims/CLAIMS.md:23-25`.  In particular, WI is an exact MPS window/state
identity, A1's linear endpoint action needs padded windows, and A2's broken
half-string limit is weak-* only.  Every use of those results in compact-U(1)
lattice gauge theory is a new [physical argument], not a consequence already
proved by those rows.

I use a spatial cubic lattice, so “3+1 lattice QED” means three spatial lattice
directions and continuous Hamiltonian time.  Compact Kogut--Susskind U(1) at
weak coupling has a Coulomb phase with a massless photon [textbook].  It is
therefore a meaningful regulator in which to ask for the Maxwell photon and
the leading Weinberg pole.  Treating its weak-coupling scaling regime as a
continuum QED regulator is a [physical argument], not a rigorous construction
of interacting QED as a UV-complete continuum theory.

### 0.1 Local-TeX definitions used in this audit

The gauge convention is quoted directly from the local canon:

> “The theory ... is invariant under the infinitesimal gauge transformations
> \(\delta_\varepsilon A=\mathrm d\varepsilon\),
> \(\delta_\varepsilon\Phi_k=i\varepsilon Q_k\Phi_k\),” with
> \(\varepsilon\sim\varepsilon+2\pi\) and finite matter action
> \(\Phi_k\to e^{iQ_k\varepsilon}\Phi_k\).

`refs/arxiv-1703.05448/soft_Arxiv_update.tex:463-473`.

The accepted asymptotic parameter is angle dependent but independent of
retarded time at leading order:

> \(\varepsilon=\varepsilon(z,\bar z)+O(1/r)\), and “the \(O(1)\) piece of
> \(\varepsilon\) cannot depend on \(u\).”

`refs/arxiv-1703.05448/soft_Arxiv_update.tex:1224-1232`.  The field and
potential falloffs used to make this statement are

> \(F_{uz}=O(1)\), \(F_{ur},F_{zr}=O(r^{-2})\), and
> \(A_z=O(1)\), \(A_r=O(r^{-2})\), \(A_u=O(r^{-1})\).

`refs/arxiv-1703.05448/soft_Arxiv_update.tex:1211-1222`.

The potential/field distinction used later is fixed by the canonical
definition

> \(\Omega_\Sigma=-\frac1{e^2}\int_\Sigma\delta(*F)\wedge\delta A\),
> which has the same value on three-surfaces with the same boundary.

`refs/arxiv-1703.05448/soft_Arxiv_update.tex:764-770`.  At null infinity the
same source explicitly finds that the radiative \(A_z^{(0)}\) modes pair
among themselves while the soft mode \(N\) pairs with the boundary potential
\(\phi\) (`refs/arxiv-1703.05448/soft_Arxiv_update.tex:776-805`).

The in/out identification is not equality at the same geometric angle.  In
the advanced/retarded angular convention of the TeX it is already antipodal:

> \(F_{ru}^{(2)}(z,\bar z)|_{\mathcal I^+_-}
> =F_{rv}^{(2)}(z,\bar z)|_{\mathcal I^-_+}\),

where the source defines \(F_{ru}^{(2)}\) as “the \(1/r^2\) term” and
evaluation at \(\mathcal I^+_-\) as \(u=-\infty\)
(`refs/arxiv-1703.05448/soft_Arxiv_update.tex:633-640`), together with

> \(\varepsilon(z,\bar z)|_{\mathcal I^+_-}
> =\varepsilon(z,\bar z)|_{\mathcal I^-_+}\).

`refs/arxiv-1703.05448/soft_Arxiv_update.tex:647-650`.  In ordinary common
spatial coordinates this is antipodal matching.

The full future charge is defined by the sphere flux,

> \(Q^+_\varepsilon=\frac1{e^2}\int_{\mathcal I^+_-}\varepsilon\,*F
> =\frac1{e^2}\int d^2z\,\gamma_{z\bar z}\varepsilon F_{ru}^{(2)}\),

`refs/arxiv-1703.05448/soft_Arxiv_update.tex:689-695`, and the constraint
rewrites **that same charge** as

> \(Q^+_\varepsilon=
> \underbrace{-\frac1{e^2}\int_{\mathcal I^+}du\,d^2z
> (\partial_z\varepsilon F_{u\bar z}^{(0)}+
> \partial_{\bar z}\varepsilon F_{uz}^{(0)})}_{Q_S^+}
> +\underbrace{\int_{\mathcal I^+}du\,d^2z\,
> \varepsilon\gamma_{z\bar z}j_u^{(2)}}_{Q_H^+}\).

`refs/arxiv-1703.05448/soft_Arxiv_update.tex:699-710`.  Thus the source's
normalisation is

\[
 Q_\varepsilon=Q_S+Q_H=\frac1{e^2}\oint\varepsilon F_{ru}^{(2)}d\Omega,
\tag{0.1}
\]

not “sphere flux plus a further hard part.”  Reading the shorthand in the
brief that latter way would double-count \(Q_H\).  The vanishing final-sphere
term used in this massless presentation is an assumption tied to the absence
of massive stable charged particles (`refs/arxiv-1703.05448/soft_Arxiv_update.tex:659-673`); the TeX
later treats massive hard particles at timelike infinity
(`refs/arxiv-1703.05448/soft_Arxiv_update.tex:1315-1327,1434-1440`).

Finally, the continuum quotient being compared with D4 is explicitly

> \({\rm ASG}=\{\text{allowed gauge symmetries}\}/
> \{\text{trivial gauge symmetries}\}\), where allowed transformations
> preserve the boundary conditions and trivial ones act trivially on the
> physical data.

`refs/arxiv-1703.05448/soft_Arxiv_update.tex:1194-1204`.

## 1. The three-column dictionary at finite lattice spacing

### 1.1 Hamiltonian gauge-theory register

Let \(\Lambda_{a,L}\subset a\mathbb Z^3\) be a finite cubic lattice and orient
every link once.  A link \(\ell\) carries
\(L^2(U(1))\), with multiplication operator \(U_\ell=e^{i\theta_\ell}\)
and integer electric flux

\[
 E_\ell=-i\frac{\partial}{\partial\theta_\ell},\qquad
 [E_\ell,U_{\ell'}]=\delta_{\ell\ell'}U_\ell .
\tag{1.1}
\]

Matter of integral charge lives on vertices, with charge operator \(\rho_x\).
In one standard normalisation the compact-U(1) Hamiltonian is

\[
 H_{a,L}=\frac{e_0^2}{2a}\sum_\ell E_\ell^2
 +\frac{1}{2e_0^2a}\sum_p(2-U_p-U_p^\dagger)
 +H_{\rm matt}[U,\Phi] .
\tag{1.2}
\]

Equations (1.1)--(1.2), including normalisation conventions that can move
powers of \(e_0\) between \(E\), \(\rho\), and the Hamiltonian, are
[textbook].  Write \(s_{x\ell}=+1\) when \(x\) is the tail of \(\ell\),
\(-1\) when it is the head, and zero otherwise.  The Gauss operator is

\[
 G_x=(\operatorname{div}E)_x-\rho_x,qquad
 (\operatorname{div}E)_x:=\sum_\ell s_{x\ell}E_\ell,qquad
 G_xP_{\rm phys}=0 .
\tag{1.3}
\]

The local gauge transformation is

\[
 \Gamma[\varepsilon]
 =\exp\!\left(i\sum_x\varepsilon_xG_x\right),
\qquad
 \Gamma[\varepsilon]U_{x\to y}\Gamma[\varepsilon]^{-1}
 =e^{i(\varepsilon_x-\varepsilon_y)}U_{x\to y},
\tag{1.4}
\]

up to the harmless simultaneous reversal of all sign conventions
[textbook].  The literal operator (1.4) is a redundancy:
\(\Gamma[\varepsilon]P_{\rm phys}=P_{\rm phys}\).  Consequently it cannot be
the nontrivial transplant of the campaign's \(U_R(g)\).  The correct object
to compare is the **matter-only regional rotation**

\[
 W_R(\alpha):=\exp\!\left(i\alpha\sum_{x\in R}\rho_x\right),
\tag{1.5}
\]

or its modulated version.  It is the gauged descendant of an on-site global
matter symmetry; Gauss's law says how it is represented on the physical
subspace.  This distinction is load-bearing.

### 1.2 Exact constant-profile telescope

For an oriented link crossing the boundary of a vertex region \(R\), put

\[
 \sigma_{R\ell}=
 \begin{cases}
 +1,&\text{tail in }R,\ \text{head outside }R,\\
 -1,&\text{tail outside }R,\ \text{head in }R.
 \end{cases}
\tag{1.6}
\]

The finite-graph divergence theorem is an operator identity,

\[
 \sum_{x\in R}(\operatorname{div}E)_x
 =\sum_{\ell\in\partial R}\sigma_{R\ell}E_\ell,
\tag{1.7}
\]

because every internal link occurs once with each sign.  Applying (1.3), and
using that all U(1) electric fluxes and charges commute, gives the exact
physical-subspace identity

\[
 \boxed{
 W_R(\alpha)P_{\rm phys}
 =\prod_{\ell\in\partial R}
   e^{\,i\alpha\sigma_{R\ell}E_\ell}P_{\rm phys}.}
\tag{1.8}
\]

This is the gauge-theory avatar of WI.  In one spatial dimension the left
boundary link enters \(R\) and contributes \(e^{-i\alpha E}\), while the
right boundary link exits and contributes \(e^{+i\alpha E}\).  The
orientation is exactly the WI orientation
\(V_\alpha(g)^{-1}\) on \(\partial_-R\) and \(V_\alpha(g)\) on
\(\partial_+R\) (`theory/corner-a.md:119-151`).  Thus the single-cut
dictionary is

\[
 \boxed{\quad V_\alpha(e^{i\alpha})^{\sigma_{R\ell}}
 \quad\longleftrightarrow\quad
 e^{\,i\alpha\sigma_{R\ell}E_\ell}.\quad}
\tag{1.9}
\]

Equation (1.8) is exact, but only after projection to the Gauss-law physical
subspace.  WI instead follows as a tensor identity before any local
constraint is imposed.  The matching algebra is exact; its mechanism is not.

### 1.3 A nonconstant profile: boundary = gradient + hard

Let \(\varepsilon_x\) be real on \(R\), and for an internal oriented link
\(\ell=(x\to y)\) define
\((d_a\varepsilon)_\ell:=\varepsilon_y-\varepsilon_x\).  Weighted summation
by parts gives

\[
 \sum_{x\in R}\varepsilon_x(\operatorname{div}E)_x
 =\sum_{\ell\in\partial R}\sigma_{R\ell}
       \varepsilon_{x_{\rm in}(\ell)}E_\ell
  -\sum_{\ell=(x\to y)\subset R}(d_a\varepsilon)_\ell E_\ell .
\tag{1.10}
\]

Define

\[
 \begin{aligned}
 Q^{\partial,a}_{R}[\varepsilon]
   &:=\sum_{\ell\in\partial R}\sigma_{R\ell}
          \varepsilon_{x_{\rm in}(\ell)}E_\ell,\\
 Q^{H,a}_{R}[\varepsilon]
   &:=\sum_{x\in R}\varepsilon_x\rho_x,\\
 Q^{\nabla,a}_{R}[\varepsilon]
   &:=\sum_{\ell=(x\to y)\subset R}
          (d_a\varepsilon)_\ell E_\ell .
 \end{aligned}
\tag{1.11}
\]

Then Gauss's law implies

\[
 \boxed{Q^{\partial,a}_{R}[\varepsilon]P_{\rm phys}
  =\bigl(Q^{H,a}_{R}[\varepsilon]
       +Q^{\nabla,a}_{R}[\varepsilon]\bigr)P_{\rm phys}.}
\tag{1.12}
\]

This is the quantitative finite-lattice soft/hard dictionary.  The matter
term is the hard charge.  The discrete-gradient electric term becomes the
field-dependent term after continuum integration by parts [physical
argument].  At finite spacing it should be called a **gradient term**, not
yet a soft-photon operator: softness requires the later null and
zero-frequency limits.  For constant \(\varepsilon\),
\(Q^{\nabla,a}=0\) and (1.12) reduces to (1.8).  Conversely, the modulated
matter rotation alone obeys

\[
 e^{iQ^{H,a}_R[\varepsilon]}P_{\rm phys}
 =e^{i(Q^{\partial,a}_R[\varepsilon]-Q^{\nabla,a}_R[\varepsilon])}
  P_{\rm phys};
\tag{1.13}
\]

it is **not** boundary-only when \(d_a\varepsilon\ne0\).  Therefore a direct
claim that every D3 modulated on-site operation telescopes purely to the
boundary would be false.

### 1.4 Endpoint group and the precise quotient

At fixed \(a,R\), boundary parameters form

\[
 \mathcal G_{\partial R,a}
 :=\operatorname{Maps}(V_{\partial R,a},U(1))
 \cong U(1)^{|V_{\partial R,a}|} .
\tag{1.14}
\]

Bulk lattice gauge maps modulo maps equal to the identity on the boundary
restrict to (1.14).  That first quotient removes the genuinely small gauge
redundancies.  To reproduce D4's state-level quotient one must then remove
the kernel in the chosen boundary register,

\[
 N_{\partial R,a}:=\{g\in\mathcal G_{\partial R,a}:
 g\text{ acts trivially on all physical boundary data/states in the
 declared register}\},
\qquad
 \mathcal A^{\rm QED}_{\rm eff}(a,R)
 =\mathcal G_{\partial R,a}/N_{\partial R,a}.
\tag{1.15}
\]

This, not an automatic quotient by constant maps, is the exact analogue of
\(G/N_\alpha\).  Constants generate ordinary electric charge when charged
sectors are retained and so are generally nontrivial.  They can fall into the
kernel after restriction to a neutral, fixed-charge, gauge-invariant
register; the kernel is register dependent.  “Zero expectation value in one
state” is not enough for membership in \(N_{\partial R,a}\); the action must
be trivial on the entire declared physical register.

### 1.5 The requested three-column dictionary

| Campaign definition, instantiated | Finite compact-U(1) lattice QED | Accepted continuum object |
|---|---|---|
| D1 quasi-local finite-\(d\) spin chain, MPS windows, and virtual bond decorations | Replace the 1D spin algebra by the 3D link-plus-matter algebra of (1.1).  The Gauss-law physical algebra does not factorise across a cut without an extended-Hilbert-space/edge-mode choice [textbook], and \(L^2(U(1))\) is not finite \(d\).  No MPS ansatz is required. | Gauge-field phase space with boundary data and the symplectic form quoted in section 0; this is not a continuum MPS limit. |
| D2 global on-site \(u(g)\), vacuum covariance, and MPS intertwiner \(V_\alpha(g)\) | Matter has the on-site phase in (1.5), but gauging also transforms adjacent links as in (1.4).  Local gauge maps are constraints; there is no standard-QED analogue of the finite-\(\chi\) IT relation. | \(\delta_\varepsilon A=d\varepsilon\), \(\delta_\varepsilon\Phi=iQ\varepsilon\Phi\), quoted in section 0.  Boundary-nonzero parameters can act physically. |
| D3(b) \(U_R(g)=\prod_{x\in R}u_x(g)\) | The nontrivial transplant is the matter rotation \(W_R(\alpha)\), not the constraint transformation \(\Gamma_R\).  For constant \(\alpha\), (1.8) leaves only cut-link operators. | Constant \(\varepsilon\) gives ordinary electric charge; the soft term vanishes (`refs/arxiv-1703.05448/soft_Arxiv_update.tex:675-685,707-715`). |
| D3(a,c) compactly supported, eventually constant, and finite-total-variation profiles | At finite \(a,L\), compact support gives a bona fide operator.  A large transformation is approached by radial cutoffs whose boundary value is \(\varepsilon_a(\hat x)\).  Nonconstant profiles obey (1.12), not pure telescoping. | \(\varepsilon=\varepsilon(z,\bar z)+O(r^{-1})\), \(\partial_u\varepsilon=0\), with antipodal in/out matching (quoted in section 0). |
| WI: regional on-site symmetry leaves oriented virtual residues | On \(\mathcal H_{\rm phys}\), (1.8) leaves \(e^{-i\alpha E}\) on entering links and \(e^{+i\alpha E}\) on exiting links. | Gauss's law equates charge in a region to outward electric flux; angle weighting gives total = gradient/soft + hard. |
| D4(a) bond implementer \(\mathcal V_b(V_\alpha(g))\) | On each cut link the counterpart is \(e^{i\varepsilon E_\ell}\), which translates the boundary link potential.  The product over the cut is generated by \(Q^{\partial,a}\). | \(Q_\varepsilon\) generates \([Q^+_\varepsilon,A_z^{(0)}]=i\partial_z\varepsilon\), quoted at `refs/arxiv-1703.05448/soft_Arxiv_update.tex:839-860`. |
| D4(b,c) \(\mathcal A_{\rm eff}=G/N_\alpha\) and two endpoint copies | Boundary maps modulo the trivial-action subgroup, (1.15).  A 3D region has an extensive 2D boundary, not two copies. | \({\rm ASG}=\text{allowed}/\text{trivial}\); in the limit the numerator is a suitable smooth \(\operatorname{Maps}(S^2,U(1))\), with antipodally matched past/future copies. |
| D4(d) twisted group algebra and infinitesimal bond charges | Pure electric U(1) fluxes commute, so the finite electric boundary algebra has no MPS/SPT multiplier.  Possible magnetic sectors or boundary extensions would be additional physics, not D4's \([\omega_\alpha]\). | The electric large-gauge algebra is abelian in this target.  The ASG definition does not manufacture the campaign's group-cohomological cocycle. |
| D10(c) \(Q[f;\xi]=\sum f q_x\) | With \(q_x=i\rho_x\) (anti-Hermitian campaign convention), it is the **hard matter term**.  The asymptotic charge also requires \(Q^{\nabla,a}\), equivalently the boundary flux. | \(Q_H^+=\int\varepsilon j_u\), while \(Q_S^+\) is linear in the radiative field; their sum is the sphere charge (`refs/arxiv-1703.05448/soft_Arxiv_update.tex:699-715`). |
| D10(a,b,d) cut current, continuity equation, and virtual bond “potential” | Matter continuity has the usual lattice Noether form [textbook], but Gauss uses electric flux \(E\).  The relevant link potential is \(U=e^{iaA}\), canonically conjugate to \(E\); it is not the campaign's finite-dimensional virtual insertion. | Maxwell constraint plus matter-current conservation.  The symplectic form pairs \(F\) with \(A\), `refs/arxiv-1703.05448/soft_Arxiv_update.tex:764-805`. |

### 1.6 Exact mismatches that the dictionary must not hide

1. **Constraint versus global symmetry.**  Campaign WI begins with a genuine
   global on-site symmetry and has no local Gauss constraint.  Equation
   (1.8) begins with a gauged matter rotation and holds only on
   \(\mathcal H_{\rm phys}\).  The full local gauge transformation is the
   identity there.

2. **Virtual bond versus gauge edge mode.**  \(V_\alpha(g)\in U(\chi)\) is
   MPS gauge data.  A cut link is a physical regulator degree of freedom with
   Hilbert space \(L^2(U(1))\); after subregion factorisation it can support an
   edge-mode algebra.  It also lies outside D1's finite one-site dimension
   without a further electric-flux truncation.  No canonical isomorphism
   identifies these spaces.

3. **Potential versus flux.**  The operator in (1.9) is generated by electric
   flux \(E\), while the lattice gauge potential is the link angle in \(U\).
   Since \(E\) translates \(U\), the pair has the right canonical action, but
   D10(d)'s statement “bond insertion = potential” does not literally become
   the Maxwell identification \(A=\) potential.  The framing in
   `docs/framing.md:25-30` is an analogy, not an equality of variables.

4. **Two endpoints versus a celestial sphere.**  D4 has one finite group at
   each of two ends of a one-dimensional cut.  A 3D lattice boundary has
   \(O(R^2/a^2)\) independent boundary samples and tends to a function group
   on \(S^2\).  This enlargement is not contained in D4 as written.

5. **Padding.**  D4's \(n_0\)-site padding makes the MPS insertion map
   injective (`definitions.md:231-260`).  Gauge-theory boundary flux is
   already a well-defined link operator; it needs no such injectivity
   theorem.  A regulator collar is useful for separating a boundary algebra
   from bulk observables, but that is only a [physical argument] and not the
   reason for D4 padding.

## 2. Explicit sequence of limits

### 2.1 Choice of spheres and profiles

Let \(B_{a,R}\) be the set of lattice vertices inside the Euclidean ball of
physical radius \(R\), and let \(\Sigma_{a,R}\) be the union of dual
plaquettes pierced by \(\partial B_{a,R}\).  Thus every term in
\(Q^{\partial,a}_{B_R}\) is the electric flux through one oriented dual
plaquette.

Fix first

\[
 \varepsilon_\infty\in C^2(S^2,\mathbb R/2\pi\mathbb Z).
\tag{2.1}
\]

This is a convenient sufficient class, not a claim that the accepted charge
exists only for \(C^2\) parameters.  Indeed, the TeX says there is

> “one [conservation law] for every function \(\varepsilon\),” and gives
> \(\varepsilon=Y_{\ell m}\) as a basis.

`refs/arxiv-1703.05448/soft_Arxiv_update.tex:647-657`.  The \(C^2\) choice
here is what makes the Riemann estimate and integration by parts below
ordinary rather than distributional.  The TeX also uses the singular
\(\varepsilon(w,\bar w)=1/(z-w)\) distributionally through
\(\partial_{\bar z}(z-w)^{-1}=2\pi\delta^2(z-w)\)
(`refs/arxiv-1703.05448/soft_Arxiv_update.tex:927-940`); that is analogous to D3 admitting a plane
wave only as a distributional kernel.

Choose a smooth bulk extension \(\bar\varepsilon(r,\hat x)\) that is
\(\varepsilon_\infty(\hat x)\) for \(r\ge R_0\), and sample or cell-average it
on lattice vertices.  Denote the result by
\(\varepsilon^{a,R}_x\).  On every fixed annulus about \(S_R\), require

\[
 \begin{aligned}
 \sup_x|\varepsilon^{a,R}_x-\bar\varepsilon(x)|&\longrightarrow0,\\
 \sup_{\ell=(x\to y)}
 \left|\frac{(d_a\varepsilon^{a,R})_\ell}{a}
       -\hat e_\ell\!\cdot\nabla\bar\varepsilon(x)\right|
 &\longrightarrow0
 \qquad(a\to0).
 \end{aligned}
\tag{2.2}
\]

Near a large sphere,
\((d_a\varepsilon)_\ell=O(a/R)\) for tangential links.  At every finite
\(a,L\), multiply the extension by a radial cutoff equal to one on
\(B_{a,R+\delta}\) and zero before the outer box.  This makes the operation
compactly supported.  The cutoff is removed only after observables at
\(S_R\) have been fixed.

### 2.2 Riemann sum to electric flux

In the canonical continuum matching, define the electric-field convention
\(\mathcal E_r:=F_{ru}=F_{rt}\), as in the local TeX.  A positively oriented
link in direction \(i\) has

\[
 E_{x,i}
 =\frac{a^2}{e^2}\mathcal E_i(t,x+\tfrac a2\hat e_i)
   +O\!\left(\frac{a^3}{e^2}\,\partial\mathcal E\right),
\tag{2.3}
\]

where \(e\) is the renormalised infrared coupling.  The leading canonical
normalisation is [textbook]; uniform operator/matrix-element control of
(2.3) in the interacting scaling limit is a [physical argument].
Using the oriented vector area \(a^2\sigma_{R\ell}\hat e_\ell\) of each dual
face, (1.11) becomes

\[
 \begin{aligned}
 Q^{\partial,a}_{B_R}[\varepsilon^{a,R}](t)
 &=\frac1{e^2}\sum_{\ell\in\partial B_{a,R}}
    a^2\,\varepsilon^{a,R}_{x_{\rm in}(\ell)}
    \mathcal E_{i_\ell}(t,x_\ell)\sigma_{R\ell}+o_a(1)\\
 &\longrightarrow
 \frac1{e^2}\int_{S_R}dS\,
       \varepsilon_\infty(\hat x)\mathcal E_r(t,R,\hat x).
 \end{aligned}
\tag{2.4}
\]

For a \(C^1\) field in an \(O(a)\) shell about \(S_R\), the standard
finite-volume quadrature estimate has the useful scaling form

\[
 \left|Q^{\partial,a}_{B_R}
 -\frac1{e^2}\int_{S_R}\varepsilon_\infty\mathcal E_r\,dS\right|
 \le \frac{C a}{e^2}
 \left[
 R^2\|\nabla(\varepsilon_\infty\mathcal E)\|_{\infty,\rm shell}
 +R\|\varepsilon_\infty\mathcal E\|_{\infty,\rm shell}
 \right]+o_{\rm ren}(1).
\tag{2.5}
\]

Equation (2.5) is a [physical argument] estimate for matrix elements or
classical configurations; no operator-norm continuum limit of the
unbounded \(E_\ell\) is asserted.  With
\(\mathcal E_r=O(R^{-2})\), \(\nabla\mathcal E=O(R^{-3})\), and a smooth angular profile,
its displayed geometric error is \(O(a/R)\).

The TeX defines retarded time by \(u=t-r\)
(`refs/arxiv-1703.05448/soft_Arxiv_update.tex:525-528`).  Approach future
null infinity along

\[
 t_R=R+u,\qquad
 F_{ru}(u,R,\hat x)
 =R^{-2}F_{ru}^{(2)}(u,\hat x)+O(R^{-2-\eta}),
 \quad \eta>0 .
\tag{2.6}
\]

Then (2.4) gives

\[
 \lim_{R\to\infty}\lim_{a\to0}
 Q^{\partial,a}_{B_R}[\varepsilon^{a,R}](R+u)
 =\frac1{e^2}\int_{S^2}d^2z\,\gamma_{z\bar z}\,
   \varepsilon_\infty(z,\bar z)F_{ru}^{(2)}(u,z,\bar z)
\tag{2.7}
\]

in the stated matrix-element/classical sense [physical argument].  Taking
\(u\to-\infty\) yields precisely the full \(Q^+_\varepsilon\) in (0.1).

### 2.3 The ordered limit, including volume and null time

A sequence that does not conflate ultraviolet, thermodynamic, and null
limits is

\[
 \boxed{
 Q^+_{\varepsilon_\infty}
 =
 \lim_{u\to-\infty}
 \lim_{R\to\infty}
 \lim_{L\to\infty}
 \lim_{\substack{a\to0\\ e_{\rm ren}(e_0(a),a)\to e}}
 Q^{\partial,a}_{B_R}
   [\varepsilon^{a,R}](t=R+u),
 \qquad R+\delta<L/2 .}
\tag{2.8}
\]

The meanings of the four stages are:

1. At fixed physical \(R,L,u,\delta\), send \(a\to0\), tune within the weak
   Coulomb scaling regime, and impose (2.2).  The angular mesh
   \(a/R\to0\).
2. Send the box size \(L\to\infty\) with the charge sphere fixed, so the
   outer regulator and radial profile cutoff cannot affect it.
3. Send \(R\to\infty\) at fixed retarded time \(u=t-R\), using (2.6).
4. Send \(u\to-\infty\) to reach \(\mathcal I^+_-\).  For the past charge use
   \(t=-R+v\), then \(v\to+\infty\), and relate the sampled past profile by
   the antipodal matching quoted in section 0.

The last null-time limit is indispensable: \(R\to\infty\) at fixed ordinary
time approaches spatial infinity, not a cut of \(\mathcal I^+\).  Likewise,
taking \(R\to\infty\) in a fixed finite box is meaningless.  Other joint
sequences can work if they have

\[
 a/R\to0,\qquad R/L\to0,\qquad
 \|\varepsilon^{a,R}-\varepsilon_\infty\|_\infty\to0,
\tag{2.9}
\]

and uniform versions of (2.3), (2.5), and (2.6); (2.8) is the clean iterated
statement.

### 2.4 The same limit gives the hard/soft decomposition

At fixed \(R\), the continuum scaling of the two terms in (1.12) is

\[
 \rho_x=a^3j^0(x)+o(a^3),\qquad
 (d_a\varepsilon)_\ell=a\,\partial_i\varepsilon(x)+o(a),
\tag{2.10}
\]

as a [physical argument] matching of lattice matrix elements, and hence

\[
 Q^{H,a}_{B_R}\to\int_{B_R}d^3x\,\varepsilon j^0,\qquad
 Q^{\nabla,a}_{B_R}\to
 \frac1{e^2}\int_{B_R}d^3x\,(\nabla\varepsilon)\!\cdot\mathbf E.
\tag{2.11}
\]

This is exactly the continuum weighted Gauss identity

\[
 \frac1{e^2}\oint_{S_R}\varepsilon\mathbf E\!\cdot d\mathbf S
 =\int_{B_R}\varepsilon j^0\,d^3x
 +\frac1{e^2}\int_{B_R}\nabla\varepsilon\!\cdot\mathbf E\,d^3x.
\tag{2.12}
\]

Passing from a spacelike slice to \(\mathcal I^+\), the continuum constraint
used by the TeX is quoted as

> \(\partial_uF_{ru}^{(2)}+D^zF_{uz}^{(0)}
> +D^{\bar z}F_{u\bar z}^{(0)}+e^2j_u^{(2)}=0\).

`refs/arxiv-1703.05448/soft_Arxiv_update.tex:699-705`.  Integrating it over
\(u\) and the sphere, and using the stated final-boundary assumption, turns
(2.12) into the quoted \(Q_S^++Q_H^+\) formula.  Hence

\[
 Q^{H,a}\longrightarrow Q_H^+,\qquad
 Q^{\nabla,a}\longrightarrow Q_S^+,\qquad
 Q^{\partial,a}\longrightarrow Q_\varepsilon^+
\tag{2.13}
\]

only after the spacelike-to-null deformation and infrared limit
[physical argument].  At finite \(a\), the second arrow is not an
identification of \(Q^{\nabla,a}\) with a zero-energy photon.

The arrows in (2.13) use the massless-matter null-infinity decomposition
quoted in section 0.  For massive QED, the hard charge does not all cross
\(\mathcal I^+\).  The canon instead resolves \(i^+\) by a hyperboloid and
quotes the one-particle action

> \(Q_\varepsilon^{+H}|\vec p\rangle
> =Q\,\varepsilon(|\vec p|/m,\hat p)|\vec p\rangle\).

`refs/arxiv-1703.05448/soft_Arxiv_update.tex:1426-1440`.  On the lattice,
the corresponding part of \(Q^{H,a}\) must be followed with
\(t\to+\infty\) at fixed asymptotic velocity (equivalently fixed
\(\rho=r/\sqrt{t^2-r^2}\)), after the continuum and volume limits
[physical argument].  The surface-flux limit (2.8) is unchanged, but its
hard/soft decomposition is then “null hard + timelike hard + soft,” not just
the two null integrals in (2.13).

The continuum source defines that zero-energy step explicitly:

> \(N_z:=\int_{-\infty}^{\infty}du\,F_{uz}^{(0)}\), obtained as the
> \(\omega\to0\) limit of
> \(\int du\,F_{uz}^{(0)}e^{i\omega u}\).

`refs/arxiv-1703.05448/soft_Arxiv_update.tex:711-721`.  Thus the scattering
time/infinite-volume limits precede the soft-frequency limit.  They are not
contained merely in \(a\to0\).

### 2.5 Which campaign clauses shadow which continuum conditions

The matches are limited but explicit:

- **D3 compact support** is the finite-regulator radial cutoff used before
  \(L\to\infty\).  It supplies a genuine finite operator.
- **D3 eventual constancy** shadows existence of limiting data at infinity
  along a one-dimensional end.  In 3D it must be replaced by radial
  constancy with freely angle-dependent boundary value
  \(\varepsilon_\infty(\hat x)\).  D3 as written has only two ends and cannot
  encode this angular function.
- **D3 finite total variation** shadows the need to control summation by
  parts and profile gradients.  It is not the correct 3D norm: a radially
  constant nonconstant angular map generally has a divergent naive sum
  \(\sum_{\ell}|d_a\varepsilon_\ell|\) as the number of links grows.  The
  appropriate sufficient replacement used here is angular \(C^2\)
  regularity, (2.2), and the falloff-weighted bounds (2.5)--(2.6).
- **D3's distributional plane-wave rule** has a genuine continuum analogue:
  singular celestial kernels such as \(1/(z-w)\) are used only under
  distributional differentiation/integration.
- **D4 padding has no continuum falloff counterpart.**  A collar
  \(a\ll\delta\ll R\) can separate boundary and bulk observables
  [physical argument], but D4 requires padding for injectivity of an MPS
  insertion map.  With fixed \(n_0\), its physical thickness \(n_0a\) even
  vanishes as \(a\to0\).  It neither implies
  \(F_{ur}=O(r^{-2})\) nor the smoothness of \(\varepsilon_\infty\).

### 2.6 What this limit does and does not establish about the Weinberg pole

The charge Ward identity in the canon is

> \(\langle{\rm out}|(Q_\varepsilon^+\mathcal S
> -\mathcal S Q_\varepsilon^-)|{\rm in}\rangle=0\).

`refs/arxiv-1703.05448/soft_Arxiv_update.tex:882-894`.  The corresponding
soft theorem is quoted there as

> \(\langle{\rm out}|a_+^{\rm out}(\vec q)\mathcal S|{\rm in}\rangle
> =e[\sum_{\rm out}Q_k\,p_k\!\cdot\varepsilon^+/(p_k\!\cdot q)
> -\sum_{\rm in}Q_k\,p_k\!\cdot\varepsilon^+/(p_k\!\cdot q)]
> \langle{\rm out}|\mathcal S|{\rm in}\rangle+O(q^0)\).

`refs/arxiv-1703.05448/soft_Arxiv_update.tex:1074-1083`.  The TeX states that
the standard soft formula reduces to the large-gauge Ward identity and that
the two are mathematically equivalent (`refs/arxiv-1703.05448/soft_Arxiv_update.tex:1055-1066`).

In the weak Coulomb regime, expanding the plaquette term gives a photon with

\[
 \omega_a(\mathbf k)
 =\frac2a\left(\sum_i\sin^2\frac{ak_i}{2}\right)^{1/2}
 =|\mathbf k|+O(a^2|\mathbf k|^3)
\tag{2.14}
\]

[textbook], so a massless lattice mode can converge to the external photon.
After a scattering construction and LSZ limit, a nearly on-shell external
charged propagator can then yield
\((p+q)^2+m^2=2p\!\cdot q+O(q^2)\) and hence the Weinberg
\(1/(p\!\cdot q)\) pole [physical argument].  None of D3, D4, D10, WI, or
the Riemann limit proves that scattering/LSZ assertion.  What has been shown
here is that their finite-region charge has the correct continuum candidate
and normalisation; the pole remains a meaningful but additional dynamical
target.

## 3. Verdict per campaign definition

### 3.1 D3 — **DO NOT say the same thing as written**

D3 gets three pieces of discipline right:

1. a compactly supported finite-lattice profile defines an operator;
2. a non-decaying profile must be defined by a limiting action rather than
   silently treated as quasi-local; and
3. distributional kernels are not themselves admissible operators.

Those principles survive (2.8).  The literal classes do not.  D3 specifies
maps on \(\mathbb Z\) with two ends.  Its
\(\mathcal F_{\ell^1}\) condition is one-dimensional total variation, whereas
the continuum charge needs an angle-dependent function on \(S^2\).  A
nonconstant radially constant angular function generally fails the naive
three-dimensional analogue of that \(\ell^1\) condition.  D3 also contains
neither \(\partial_u\varepsilon_\infty=0\) nor antipodal matching.

A sufficient replacement for this QED audit is

\[
 \begin{aligned}
 \mathfrak F_{\rm op}^{\rm QED}
   &=\{\varepsilon:\Lambda_{a,L}\to\mathbb R/2\pi\mathbb Z
        \text{ with finite support}\},\\
 \mathfrak F_{\rm as}^{\rm QED}
   &=\{\varepsilon:
      \varepsilon(r,u,\hat x)=\varepsilon_\infty(\hat x)+O(r^{-1}),\
      \partial_u\varepsilon_\infty=0,\
      \varepsilon_\infty\in C^2(S^2)\},
 \end{aligned}
\tag{3.1}
\]

with the past and future boundary values antipodally matched and with a
separate distributional completion when desired.  Equation (3.1) is a
[physical argument] regulator class chosen to implement the quoted
continuum conditions; it is not D3.  Moreover, A1/A2's existence of MPS
weak-* half-string limits does not prove existence of the corresponding
large-gauge action in lattice QED.  **Verdict: structural discipline YES;
definition-level equality NO.**

### 3.2 D4 — **DO NOT say the same thing as written**

There is a genuine quotient-level match:

\[
 G/N_\alpha
 \quad\leftrightarrow\quad
 \mathcal G_{\partial R,a}/N_{\partial R,a}
 \ \xrightarrow[\ a/R\to0\ ]{\rm physical\ argument}\
 C^2(S^2,U(1))/N_\infty ,
\tag{3.2}
\]

where \(N_\infty\) is the subgroup acting trivially on the declared
continuum physical phase space.  This is precisely the logic of the quoted
continuum “allowed/trivial” quotient.  The oriented implementer action also
matches quantitatively through (1.9).

But D4 itself fixes one compact global group \(G\), a finite-dimensional
virtual space, a projective \(V_\alpha(g)\), and a one-bond insertion.  None
of those data becomes the \(O(R^2/a^2)\)-sample boundary group without
changing the definition.  The electric U(1) cut-link implementers commute
[textbook] and carry no D4 SPT multiplier.  D4 padding has no falloff
meaning.  Finally,
large-gauge transformations act on the actual boundary potential:

> \([Q_\varepsilon^+,A_z^{(0)}]=i\partial_z\varepsilon\) and
> \([Q_\varepsilon^+,\phi]=i\varepsilon\).

`refs/arxiv-1703.05448/soft_Arxiv_update.tex:839-860`.  That canonical
edge action is not supplied by an abstract MPS \(PGL(\chi)\)-torsor.

A1 therefore remains a **PROVED** statement about its padded-window and
state registers, but it is not a proof of (3.2).  **Verdict: quotient pattern
and orientation YES; D4 as the QED endpoint algebra NO.**

### 3.3 D10 — **DO NOT define the full continuum asymptotic charge**

With the campaign's anti-Hermitian convention,

\[
 q_x=i\rho_x,\qquad
 Q[f]=iQ_R^{H,a}[f].
\tag{3.3}
\]

D10(a,b)'s finite-range continuity equation is then the lattice matter
Noether equation and reduces to \(\partial_\mu j^\mu=0\) under the usual
continuum scaling [physical argument].  This is the correct hard-current
part.

The full large-gauge charge is instead (1.12):

\[
 Q_{\varepsilon}^{\rm gauge,a}
 :=Q_R^{H,a}[\varepsilon]+Q_R^{\nabla,a}[\varepsilon]
 =Q_R^{\partial,a}[\varepsilon]
\quad\text{on }\mathcal H_{\rm phys}.
\tag{3.4}
\]

D10(c) contains only the first term.  D10(d)'s relation between a physical
charge insertion and a virtual difference is a theorem about one MPS vacuum,
not an operator constraint on the entire Hilbert space; it cannot replace
\(G_x=0\).  Its virtual \(X_\alpha\) is also not the Maxwell potential \(A\)
or its conjugate flux \(E\), as section 1.6 explains.

Thus D10 has the correct discrete Noether continuity law for the matter
subsystem, but it neither defines the soft electromagnetic term nor the
surface generator.  Adding (3.4), gauge-field phase space, and the null limit
is a substantive extension.  **Verdict: hard Noether pair YES; full
asymptotic-charge definition NO.**

### 3.4 WI treated as a definitional criterion — **DO, but only in the
constant-profile physical-subspace sense**

WI is a **PROVED theorem**, not formally one of the numbered definitions.
If “WI-as-definition” means the criterion

> a symmetry restricted to a region has no independent bulk action and is
> represented by oppositely oriented operators on the cut,

then (1.8) is an exact QED realization for constant U(1) matter rotations on
\(\mathcal H_{\rm phys}\).  Under (2.8) it becomes the constant-\(\varepsilon\)
Gauss relation between total charge and sphere flux.  In that precise sense,
the discrete and continuous statements **DO** say the same thing.

The restrictions are essential:

- the QED equality uses a local constraint, while WI uses the MPS
  intertwiner;
- the QED equality is after \(P_{\rm phys}\), while WI is a window-vector
  identity and separately a state identity;
- a nonconstant angular profile obeys (1.12), with a bulk gradient term,
  rather than the pure endpoint formula (1.8); and
- WI by itself supplies neither the celestial function group, antipodal
  matching, the symplectic boundary action, nor the soft-frequency limit.

The continuum statement that large gauge symmetry is spontaneously broken
also does not promote A2 into a QED theorem.  The canon says

> because \(A_z=0\) is not invariant, the symmetries are spontaneously broken
> and the vacuum is infinitely degenerate,

`refs/arxiv-1703.05448/soft_Arxiv_update.tex:859-860`, but A2 proves a
weak-* sector jump for a broken **global** MPS symmetry with its own vacuum
and double-coset hypotheses.  The mechanisms and state spaces differ.

### 3.5 Overall answer

The campaign has a compelling quantitative Gauss-law nucleus:

\[
 \boxed{
 \text{regional matter charge}
 \xleftrightarrow[\ G_x=0\ ]{}
 \text{oriented cut-link electric flux},\qquad
 Q_\partial[\varepsilon]=Q_H[\varepsilon]+Q_\nabla[\varepsilon]
 \longrightarrow Q_H+Q_S.}
\tag{3.5}
\]

The first equality is exact at finite lattice spacing on the physical
subspace; the last arrow is a [physical argument] under (2.8), the falloffs,
and the null-boundary assumptions.  This is a real connection to accepted
continuum QED, not merely a pictorial analogy.

It is not, however, a full instantiation of D3, D4, and D10 as currently
written.  Achieving that would require a 3D boundary-profile definition,
Gauss-constrained/edge-mode state spaces, the boundary function group and
its physical kernel, and a charge definition that includes both matter and
electromagnetic terms.  It would still require a separate scattering/LSZ
argument to reach the Weinberg pole.  No campaign status is changed by this
audit.

| item | campaign status retained | audit verdict |
|---|---|---|
| D3 | definition | **DO NOT** literally reduce; its function-space discipline survives after (3.1). |
| D4 / A1 | definition / **PROVED** in the stated MPS registers | **DO NOT** literally reduce; only the oriented implementer and quotient pattern match. |
| D10 | definition, with its cited G0 consequences unchanged | **DO NOT** give the full QED charge; it gives the hard matter Noether part. |
| WI | **PROVED** in its window/state registers | **DO** match the constant-profile Gauss telescope on \(\mathcal H_{\rm phys}\), with the stated residual gaps. |
| A2 | **PROVED** in its weak-* broken-MPS register | no QED promotion; continuum large-gauge vacuum degeneracy is a separate construction. |
