# Q2: do D13, D26, and D27 discretize electromagnetic memory?

## 0. Scope and bottom line of the comparison

The comparison has to keep three continuum objects separate:

1. the electromagnetic memory field, the early/late change of the transverse
   gauge potential (equivalently the zero-frequency integral of the radiative
   electric field);
2. the velocity or momentum kick of a charged test particle produced by that
   field; and
3. the charged-matter flux which sources a Maxwell constraint.

They are related, but they are not the same observable.  The campaign's D13 is
a wall-position/regularised-matter-charge observable, D26 is a compact-circle
weight-spectrum condition, and D27 measures the change of that matter charge.
Consequently the honest overall answer is already constrained: D26 is the same
compact-
\(U(1)\) representation-theory statement that underlies integer electric flux
in compact lattice QED, but it is transplanted from a **link electric field**
to an **on-site matter charge**.  D13 and D27 do not become the electromagnetic
potential jump merely by taking a continuum limit.  They become a continuum
charge-transport/interface-displacement ledger unless an additional Gauss-law
and detector-response dictionary is supplied.

All claims below that use standard compact Hamiltonian lattice QED rather than
a result proved in this repository are marked **[textbook]**.  Continuum-limit
and detector-identification steps not supplied by a theorem in the campaign
are marked **[physical argument]**.  The statuses of the campaign claims are
reported, not changed.

## 1. The accepted continuum observable, from the local TeX

### 1.1 Memory field and DC potential jump

The assigned local source defines the outgoing zero mode by

> “\(\int_{-\infty}^{\infty}du\,F^{(0)}_{uz}\equiv N_z\)” and immediately
> identifies it as the \(\omega\to0\) limit of
> “\(\int_{-\infty}^{\infty}du\,F^{(0)}_{uz}e^{i\omega u}\).”
>
> — `refs/arxiv-1703.05448/soft_Arxiv_update.tex:711-721`

In the boundary gauge \(A_u^{(0)}=0\), the same TeX gives the endpoint
identity

> “\(e^2\partial_zN=\int_{-\infty}^{\infty}du\,F^{(0)}_{uz}
> =A_z^{(0)}|_{\mathcal I^+_+}-A_z^{(0)}|_{\mathcal I^+_-}\).”
>
> — `refs/arxiv-1703.05448/soft_Arxiv_update.tex:731-740`

Thus, componentwise and up to the source's sign/index convention,

\[
 \mathcal M_A:=\int_{-\infty}^{\infty}du\,F^{(0)}_{uA}
       =\Delta A_A^{(0)} .                                      \tag{1.1}
\]

This is the continuum field that a compact link angle must approximate.  It is
a real transverse one-form (modulo the ordinary endpoint gauge equivalence),
not an integer charged-particle count.  The source also says that finite energy
makes the endpoint potentials pure gauge and that the relative shift is itself
a gauge transformation (`soft_Arxiv_update.tex:741-743`).  Its operational
electromagnetic discussion is phase based: large gauge transformations “impart
distinct phases to charged particles,” giving an interference pattern for
electrons near null infinity
(`refs/arxiv-1703.05448/soft_Arxiv_update.tex:1232-1234`); the summary again
says that QED memory gives relative phases measurable by interference
(`refs/arxiv-1703.05448/soft_Arxiv_update.tex:2651-2655`).

There is a source-fidelity point.  The assigned 1703 TeX does **not** contain a
displayed \(\Delta v=(e/m)\int dt\,E\) formula.  It contains (1.1), from which
the kick follows.  A separate local TeX states the missing link directly:

> “\(E_A^{(1)}=-\partial_uA_A^{(1)}\)” and a nonzero
> “\(\int_{-\infty}^{\infty}du\,E_A^{(1)}\)” is the integrated force on a
> distant test particle, giving it a net momentum kick; it then defines
> “\(\Delta_A^{\rm out}:=-\int du\,E_A^{(1)}
> =A_A^{(1)}|_{+\infty}-A_A^{(1)}|_{-\infty}\).”
>
> — `refs/arxiv-2203.14334/IR_fin_scat_draft.tex:449-458`

**[physical argument]** For a nonrelativistic probe of physical charge
\(q_{\mathrm{p}}\) and mass \(m\), integrating the Lorentz equation during the
radiation epoch gives

\[
 m\,\Delta v_A=q_{\mathrm{p}}\int dt\,E_A,
 \qquad
 \Delta v_A=-\frac{q_{\mathrm{p}}}m\,\Delta A_A               \tag{1.2}
\]

in temporal gauge with \(E_A=-\partial_tA_A\).  Reversing the convention for
\(F_{tA}\) reverses both displayed signs, not the content.  The brief's
\(e/m\) formula is the unit-charge case \(q_{\mathrm{p}}=e\).

### 1.2 What “operational” means

The other assigned source is explicitly gravitational, not electromagnetic,
but it states the before/after detector criterion that the brief asks us to
use.  Its abstract considers a radiation pulse passing detector arrays and
compares their relative positions and clock times before and after transit
(`refs/arxiv-1411.5745/memory_4.tex:460-466`).  The introduction is even more
direct:

> “The final positions of a pair of nearby detectors are generically displaced
> relative to the initial ones ... This effect is known as gravitational
> memory.”
>
> — `refs/arxiv-1411.5745/memory_4.tex:480-482`

It then says that the detector data supply “a concrete operational meaning” to
the asymptotic transformation
(`refs/arxiv-1411.5745/memory_4.tex:484-489`).  In its detector construction it
introduces fixed-angle and inertial detector families
(`refs/arxiv-1411.5745/memory_4.tex:581-595`) and computes the change in their
proper separation from the early and late metrics
(`refs/arxiv-1411.5745/memory_4.tex:597-612`).

For electromagnetism the corresponding operational datum is not necessarily a
position displacement: it can be the final probe velocity/momentum (1.2), or
the relative phase/interference readout named in the 1703 TeX.  The common
structure is

\[
  \text{prepare detector}\;\longrightarrow\;
  \text{radiation epoch}\;\longrightarrow\;
  \text{compare settled late data with early data}.             \tag{1.3}
\]

The quantity in (1.1) is continuous even when the charged matter that sources
it comes in integral charge units.  This distinction will be decisive below.

## 2. Compact Hamiltonian lattice QED and the D26 transplant

### 2.1 The honest link memory observable

**[textbook]** In compact Kogut--Susskind \(U(1)\) gauge theory, an oriented
spatial link \(\ell\) carries

\[
 \mathcal H_\ell=L^2(U(1)),\qquad
 U_\ell=e^{i\theta_\ell},\qquad
 n_\ell=-i\frac{\partial}{\partial\theta_\ell},
 \qquad [n_\ell,U_\ell]=U_\ell,                              \tag{2.1}
\]

with \(\theta_\ell\sim\theta_\ell+2\pi\) and
\(\operatorname{spec}n_\ell=\mathbb Z\) for periodic wavefunctions.  I write
\(n_\ell\) for the dimensionless lattice electric field so it is not confused
with the physical continuum field \(E_i\).  In one common 3+1-dimensional
normalisation,

\[
 H_{\rm KS}=\frac{e^2}{2a}\sum_\ell n_\ell^2
 +\frac{1}{e^2a}\sum_p(1-\cos\theta_p)+H_{\rm matter}.       \tag{2.2}
\]

Two qualifications are essential.

First, \(U_\ell\), not a globally defined self-adjoint \(\theta_\ell\), is the
fundamental compact operator.  For a classical link history the
branch-independent change is the circle element

\[
 M_\ell^{S^1}=e^{i\theta_\ell(t_f)}e^{-i\theta_\ell(t_i)}
              =e^{i[\theta_\ell(t_f)-\theta_\ell(t_i)]}.      \tag{2.3}
\]

A real \(\Delta\widetilde\theta_\ell\) exists only after lifting the dynamical
path to the universal cover; different lifts differ by \(2\pi w_\ell\),
\(w_\ell\in\mathbb Z\).  In a weak-field history confined to one chart the
lift is canonical.  Histories with winding retain extra integer information.
In the quantum theory the ordered product
\(U_\ell(t_f)U_\ell(t_i)^\dagger\) is well defined, but it is not generally
the exponential of a difference of commuting angle operators; its
interpretation as (2.3) is a coherent-state/semiclassical history statement.

Second, an open link is gauge covariant rather than gauge invariant:
\(U_{xy}\mapsto g_xU_{xy}g_y^{-1}\).  Hence a physically complete readout is
either gauge fixed (as in temporal/radiation gauge), closed into a Wilson
operator, or compared through the phase/kick of a charged probe.  This is the
lattice version of why the continuum source describes relative phases and a
detector response rather than an absolute local value of \(A\).

**[textbook]** In temporal gauge, on a chosen classical canonical chart and
with the normalisation (2.2), Hamilton's equation gives
\(\dot\theta_\ell=(e^2/a)n_\ell\) (up to the orientation sign), so

\[
 \Delta\widetilde\theta_\ell
   =\frac{e^2}{a}\int_{t_i}^{t_f}dt\,n_\ell(t).                \tag{2.4}
\]

The corresponding quantum statement is formulated with the ordered link
unitaries and reduces to (2.4) in a semiclassical packet.  With the continuum
matching \(\theta_\ell=aeA_i(x_\ell)+O(a^2e)\), the same semiclassical
statement is

\[
 \frac{\Delta\widetilde\theta_\ell}{ae}
       =\Delta A_i(x_\ell)+O(a)
       =-\int dt\,E_i(x_\ell,t)+O(a),                         \tag{2.5}
\]

again with the sign fixed by orientation and the definition of \(E_i\).
Equations (2.3)--(2.5), not an electric-flux eigenvalue by itself, are the
direct lattice discretisation of (1.1).

**[physical argument]** A charged lattice wavepacket provides the second
natural observable.  Compare its mechanical momentum (or group velocity) at
times before and after the pulse.  In a smooth continuum packet,

\[
 \Delta p_i=q_{\rm p}\int dt\,E_i,
 \qquad \Delta v_i=\Delta p_i/m,                              \tag{2.6}
\]

which tends to (1.2).  Unlike \(n_\ell\), neither the link-angle change nor a
wavepacket momentum kick is forced to be integer.

### 2.2 D26 clause by clause

The compactness/spectrum correspondence can be made exact.  **[textbook]**
Allow a twisted rotor sector

\[
 \psi(\theta+2\pi)=e^{2\pi i\kappa}\psi(\theta),
 \qquad 0\leq\kappa<1 .                                      \tag{2.7}
\]

Then

\[
 n_\kappa=-i\partial_\theta,qquad
 \operatorname{spec}n_\kappa=\kappa+\mathbb Z,
 \qquad e^{2\pi in_\kappa}=e^{2\pi i\kappa}I.               \tag{2.8}
\]

The ordinary compact link is \(\kappa=0\).  A twisted boundary condition,
background electric flux, or equivalent theta/background datum supplies an
affine offset.  The offset is defined only modulo \(\mathbb Z\); changing the
origin of the integer label does not change the sector.

D26 assumes on one matter site

\[
 e^{2\pi iS_x^z}=cI,qquad c=e^{2\pi i\kappa},
 \qquad \operatorname{spec}S^z\subset\kappa+\mathbb Z.        \tag{2.9}
\]

The equivalence in (2.9) is the finite-dimensional spectral-calculus version
of (2.8).  The correspondence is therefore:

| compact-link statement | D26 statement | exactness / difference |
|---|---|---|
| \(U=e^{i\theta}\), \(\theta\in\mathbb R/2\pi\mathbb Z\) | selected on-site circle action generated by \(S^z\) | same compact group, but D26 does not define a gauge link or an angle |
| \(n=-i\partial_\theta\), \(\operatorname{spec}n=\mathbb Z\) | \(\operatorname{spec}S^z\subset\kappa+\mathbb Z\) | same weight-lattice theorem; link regular representation has equality and is infinite dimensional, while D26 only requires a finite subset |
| twisted rotor \(e^{2\pi in}=e^{2\pi i\kappa}I\) | \(e^{2\pi iS^z}=cI\) | exactly the same affine/coset statement |
| background electric-flux origin \(\kappa\) | projective scalar phase \(c\), hence on-site offset \(\kappa\) | analogous offset, not the memory field \(\Delta A\) |

So the answer to “is D26 exactly the compactness statement, transplanted?” is:
**yes at the level of the generator's affine weight spectrum; no at the level
of which physical observable carries it.**  In lattice QED (2.8) belongs to the
electric field conjugate to a link angle.  In D26 (2.9) belongs to an on-site
matter charge.  Compactness alone does not identify \(S_x^z\) with
\(\theta_\ell\), \(n_\ell\), \(\Delta A\), or a detector kick.

### 2.3 The finite-window coset and why the TPM increment is integral

Let \(L=|W|=b-a+1\).  Expanding D13(a) exactly gives

\[
 \widehat Q_{W,c_0}=2s(\mathfrak X_W-c_0)
 =\sum_{x=a}^bS_x^z+s(a+b-1-2c_0).                            \tag{2.10}
\]

Because the on-site terms commute and each spectrum lies in
\(\kappa+\mathbb Z\),

\[
 \operatorname{spec}\widehat Q_{W,c_0}
 \subset \kappa_{W,c_0}+\mathbb Z,
 \quad
 \kappa_{W,c_0}\equiv
 L\kappa+s(a+b-1-2c_0)\pmod{\mathbb Z}.                       \tag{2.11}
\]

This is precisely the coset recorded by **M-INDEX-fin — PROVED**.  Its two
offsets have different origins: \(L\kappa\) is the sum of the microscopic
circle-representation offsets, while the \(s\)-term is the chosen step-vacuum,
wall-coordinate, and cut background.  D26 alone imposes no arithmetic
condition on the real tail density \(s=\rho\); the campaign derives
\(2\rho\in\mathbb Z\) only after adding its tail hypothesis (S).

Time evolution is a \(C^*\)-automorphism, so the early and late Heisenberg
observables have the same spectrum and the same \(\kappa_{W,c_0}\).  In D27 a
run first returns \(q_-\in\kappa_{W,c_0}+\mathbb Z\), then
\(q_+\in\kappa_{W,c_0}+\mathbb Z\).  Therefore

\[
 \nu=q_--q_+\in\mathbb Z.                                    \tag{2.12}
\]

This does not treat \(\widehat Q(t_-) -\widehat Q(t_+)\) as an operator and
does not require the two observables to commute.  It is cancellation of the
same affine offset between two classical TPM outcomes at fixed \(W,c_0\).
That is exactly the scope of **M-INDEX-fin — PROVED**; it is arithmetic, not a
dynamical memory theorem.

## 3. How compact/integer data become real/continuous

### 3.1 Decompactifying the link coordinate

At finite cutoff the continuum potential inferred from one link is only
defined modulo

\[
 A_{i,\ell}^{\rm lat}=\frac{\theta_\ell+2\pi k}{ae},
 \qquad
 A_{i,\ell}^{\rm lat}\sim A_{i,\ell}^{\rm lat}
                  +\frac{2\pi}{ae},\qquad k\in\mathbb Z.      \tag{3.1}
\]

Take a family of smooth physical fields with \(A_i\) and \(\Delta A_i\) fixed
while \(a\to0\), \(e\to0\), and hence \(ae\to0\).  On every fixed compact
field range, eventually \(|aeA_i|<\pi\), so there is a unique principal lift
and

\[
 \theta_\ell=aeA_i+O(a^2e),
 \qquad
 \frac{\Delta\widetilde\theta_\ell}{ae}
       \longrightarrow\Delta A_i\in\mathbb R,
 \qquad
 \frac{2\pi}{ae}\longrightarrow\infty.                       \tag{3.2}
\]

This is the precise kinematical decompactification: a fixed real interval of
\(A\)-space occupies an ever smaller arc of \(U(1)\), while the next compact
copy recedes to infinite \(A\).  A fixed physical memory has
\(\Delta\theta=ae\Delta A\to0\), not a finite circle jump.

**[physical argument]** Weak coupling additionally suppresses histories that
leave this chart through lattice monopoles or other compact winding events.
Without that dynamical restriction, (3.2) is only a local weak-field limit and
the integers \(w_\ell\) in the lift of (2.3) remain extra sectors.  Thus
\(ae\to0\) is enough to make the coordinate period diverge; using a single
real lift for the histories under study also requires a no-winding/weak-field
condition.

### 3.2 What happens to the integer electric field

The conjugate of the rescaled link coordinate \(A_\ell=\theta_\ell/(ae)\) is

\[
 P_{A,\ell}=-i\frac{\partial}{\partial A_\ell}
            =ae\,n_\ell,
 \qquad
 \operatorname{spec}P_{A,\ell}=ae(\kappa+\mathbb Z).          \tag{3.3}
\]

Therefore adjacent eigenvalues are separated by \(ae\), which vanishes.  A
fixed \(P_A\) is represented by integers
\(n\sim P_A/(ae)\to\infty\); the affine offset contributes only
\(ae\kappa\to0\).  Equations (3.1) and (3.3) are the standard circle/weight-
lattice pair becoming the real-line/canonical-momentum pair.

This step uses the **unbounded** one-link rotor spectrum
\(\kappa+\mathbb Z\).  D26 is weaker: on a fixed finite-dimensional matter
site, \(\operatorname{spec}S^z\) is only a finite subset of that coset.  Thus
\(aeS^z\to0\) at fixed on-site dimension; it does not fill \(\mathbb R\).
To obtain a nontrivial real limit from D26 data one must additionally let the
available weight range grow—through a growing local representation or a
many-site/window sum—with occupied weights of order \(1/(ae)\).  D26 states no
such representation-scaling limit.

There is a dimensional subtlety hidden by (3.3).  **[textbook]** With (2.2),
the electric flux through the dual plaquette is

\[
 \Phi_{E,\ell}=a^2E_i=e\,n_\ell,
 \qquad
 \Delta\Phi_E=e,
 \qquad
 \Delta E_i=\frac e{a^2}.                                    \tag{3.4}
\]

Thus weak coupling makes the **flux** quantum vanish.  A literal one-link
electric-field eigenvalue lattice becomes dense at fixed physical \(E_i\)
only if the simultaneous scaling has \(e/a^2\to0\), in which case
\(n\sim a^2E_i/e\to\infty\).  If one instead takes the usual continuum limit
at fixed renormalised charge, smooth classical fields are described by
superpositions/coherent states and by coarse fluxes across many links; one
must not claim that the spacing \(e/a^2\) of a single-link field eigenbasis
vanishes.  The coordinate decompactification (3.2), continuum expectation
values, and microscopic charge quantisation are compatible.

### 3.3 Escaped charge: two distinct continuum choices

D27's variable \(\nu\) is a dimensionless circle weight.  If one unit of that
weight carries physical charge \(q_0\), then

\[
 Q_{\rm esc}^{\rm phys}=q_0\nu,
 \qquad \nu\in\mathbb Z.                                     \tag{3.5}
\]

There are two different limits, and conflating them gives a false conclusion.

1. **Vanishing-unit/classical limit.**  If \(q_0=e\to0\) and one holds a
   macroscopic escaped charge fixed by taking
   \(\nu\sim Q_{\rm esc}^{\rm phys}/e\to\infty\), the spacing in (3.5)
   vanishes and the rescaled law can approach a probability law on
   \(\mathbb R\).  Fixed \(\nu\) instead carries vanishing physical charge.
2. **Continuum QED at fixed renormalised elementary charge.**  If
   \(q_0=e_R\neq0\), charge quantisation survives:
   \(Q_{\rm esc}^{\rm phys}\in e_R\mathbb Z\).  This is not a lattice
   artefact.  The assigned local TeX itself defines
   \(Q_E=e^{-2}\int_{S^2}{*F}=\int_\Sigma *j\in\mathbb Z\) in units where the
   electron has charge one
   (`refs/arxiv-1703.05448/soft_Arxiv_update.tex:457-461`) and takes the gauge
   parameter periodic, \(\varepsilon\sim\varepsilon+2\pi\), with integer
   matter weights (`refs/arxiv-1703.05448/soft_Arxiv_update.tex:463-471`).

Charge quantisation surviving does not quantise \(\Delta A\).  A continuous
radiation profile and its coherent-state amplitude vary continuously even
when every charged particle has charge \(e_R\).  Maxwell's constraint relates
the divergence of the field memory to hard charged flux and endpoint Coulomb
data; it does not identify the transverse memory one-form with a single total
integer.

The campaign already respects the analogous distinction internally.  Under
**M-INDEX-spec — PROVED conditionally on H-MQG, D26, and D27(LR1--LR3)**,

\[
 \nu\in\mathbb Z\quad\hbox{run by run},
 \qquad
 \delta x=-\frac1{2s}\sum_{\nu\in\mathbb Z}\nu p_\nu .       \tag{3.6}
\]

The mean \(\delta x\) is generally real already at finite lattice spacing;
the claim does not say that the mean is quantised.  If \(\mathfrak X\) is
interpreted as a physical wall coordinate, \(X_{\rm phys}=a\mathfrak X\), an
individual history increment has spacing

\[
 \Delta X_{\rm phys}=\frac{a}{2s}\,\nu,                       \tag{3.7}
\]

which becomes continuous as \(a\to0\) at fixed \(s\).  This is an
interface-position continuum limit.  It still does not turn
\(X_{\rm phys}\) into \(A_i\): that would require an additional field
dictionary with dimensions, gauge transformation law, and response
normalisation.

### 3.4 What the limit does not supply

The continuum source itself separates soft field and hard matter terms.  Its
large-gauge charge contains both a term linear in
\(\int du\,F_{uA}^{(0)}\) and a term containing the matter current
(`refs/arxiv-1703.05448/soft_Arxiv_update.tex:700-715`).  D13/M-flux instead
gives the exact matter ledger

\[
 \delta x=\frac1{2s}
 \left[\widetilde j_{a-1|a}(0)-\widetilde j_{b|b+1}(0)\right], \tag{3.8}
\]

the **PROVED** DC weight of the two physical spin-current boundaries.  In QED
language (3.8) corresponds to charge transported out of a control volume,
divided by the background density jump: it is the one-dimensional moving-
interface/continuity-equation analogue of hard flux.  It is not (1.1), the
time integral of the electric field.

**[physical argument]** To reconstruct electromagnetic memory from a hard
charge history one must also impose Maxwell's constraint, specify the early
and late Coulombic data and boundary conditions, and invert the angular
differential operator.  Different angular radiation/current profiles can
have the same total integer escaped charge but different
\(\Delta A_A(z,\bar z)\).  No such reconstruction map is present in D13,
D26, D27, M-flux, M-INDEX-fin, or M-INDEX-spec.  Decompactification cannot
manufacture that missing observable map.

## 4. D27 versus a before/after detector measurement

### 4.1 What D27 actually measures

At fixed \(W,c_0\), D27 performs a sequential projective measurement of the
matter/wall charge (2.10).  For a particular early time \(t_-\) and late time
\(t_+\), its outcome law is

\[
 p_{W;t_-,t_+}(\nu)
 =\sum_q\left\|
 E_{W,t_+}(\{q-\nu\})E_{W,t_-}(\{q\})\Psi
 \right\|^2,
 \qquad \nu\in\mathbb Z.                                    \tag{4.1}
\]

It then averages \(t_-\in[-2T_n,-T_n]\) and
\(t_+\in[T_n,2T_n]\), takes \(n\to\infty\) at fixed \(W\), and only after
that exhausts \(W_m\uparrow\mathbb Z\).  LR2 makes the dephasing defect vanish
only in the averaged first moment, and LR3 supplies first-moment tightness in
the spatial exhaustion.  The result is the conditional theorem (3.6), not a
measurement of \(U_\ell(t_f)U_\ell(t_i)^\dagger\), \(\Delta A\), or a probe's
\(\Delta v\).

D27 nevertheless shares the **logical skeleton** (1.3): choose an early
record, allow the event to occur, choose a late record, and subtract.  Whether
it discretises the accepted operation depends on four extra identifications.

### 4.2 Cesaro endpoints are weaker than settled detector endpoints

Suppose an ordinary detector record \(f(t)\) has a pointwise late limit
\(f_+\).  Then

\[
 \left|\frac1T\int_T^{2T}f(t)dt-f_+\right|
 \leq \sup_{t\in[T,2T]}|f(t)-f_+|\longrightarrow0.             \tag{4.2}
\]

The analogous statement holds at early times.  Thus pointwise local
relaxation, together with the corresponding control of the two-time
measurement correlator, implies the D27 Cesaro readout and makes it equal to
the usual before/after value.

The converse is false.  For example,

\[
 f(t)=\cos\omega t,
 \qquad
 \left|\frac1T\int_T^{2T}f(t)dt\right|
 =\left|\frac{\sin(2\omega T)-\sin(\omega T)}{\omega T}\right|
 \leq\frac2{|\omega|T}\longrightarrow0,                       \tag{4.3}
\]

although \(f(t)\) never settles.  D27 can therefore assign an averaged endpoint
to a persistent local oscillation for which the usual final detector reading
does not exist.  **LR1-GEN — PROVED** guarantees a common subsequence of such
Cesaro limits under very general hypotheses; it explicitly does not prove
pointwise relaxation.  LR2 and LR3 remain assumptions in
**M-INDEX-spec — PROVED conditionally**.

**[physical argument]** The continuum/cutoff limit does not repair (4.3): this
is a long-time infrared issue, not a spatial discretisation error.  Equality
with the operational memory requires a Tauberian/Abelian upgrade (for example,
integrable time derivatives or sufficient spectral/local-decay control), or
else the continuum protocol itself must be redefined as an averaged detector.
This is the known Tauberian gap recorded under tracker label `tns-94g`; no such
upgrade is proved by D27.

### 4.3 A charge TPM is not a link-angle, phase, or velocity readout

For (4.1), direct spectral algebra gives

\[
 \sum_\nu\nu p_{W;t_-,t_+}(\nu)
 =\langle\widehat Q(t_-)\rangle
  -\left\langle\mathcal D_{W,t_-}(\widehat Q(t_+))\right\rangle,
 \quad
 \mathcal D_{W,t_-}(A)=\sum_qE_{t_-}(q)AE_{t_-}(q).            \tag{4.4}
\]

LR2 says that the double-Cesaro average of the difference between the second
term in (4.4) and \(\langle\widehat Q(t_+)\rangle\) vanishes.  This is exactly
enough to identify the **mean** TPM increment with the difference of the two
charge means.  It says neither that the first measurement is nondemolition as
an operator nor that the full history law equals a classical two-time joint
law.

The mismatch with field memory is sharp for a rotor.  **[textbook]** If a
projective measurement resolves the integer electric field
\(n\), its dephasing map is
\(\mathcal D_n(\rho)=\sum_n|n\rangle\langle n|\rho|n\rangle\langle n|\).
Since the angle unitary shifts the weight,
\(U|n\rangle=|n+1\rangle\),

\[
 \operatorname{tr}[\mathcal D_n(\rho)U]=0                    \tag{4.5}
\]

for every trace-class \(\rho\).  A sharp conjugate-flux measurement erases the
one-link phase coherence used to read an angle.  D27 is even one step removed:
it measures on-site matter charge, not link electric flux.  Gauss's law may
relate a region's matter charge to its boundary flux, but it does not convert
that projective measurement into a measurement of \(\Delta\theta\).

By contrast, the accepted electromagnetic operation evolves a minimally
coupled probe and reads its final momentum/velocity, or interferes two charged
probes.  **[physical argument]** A weak-probe/macroscopic limit can make this
readout effectively nondestructive: take the probe's backreaction to zero
while keeping \(q_{\rm p}\int E/m\) resolvable, or coarse-grain a large charge
so relative fluctuations vanish.  D27 contains no weak-probe parameter and no
theorem establishing that limit.  LR2 is only the first-moment substitute.

### 4.4 A growing charge window is not a local test detector

D27's order is

\[
 \text{infinite-volume dynamics}
 \ \prec\ \text{fixed-}\!W\text{ time averages}
 \ \prec\ W_m\uparrow\mathbb Z .                              \tag{4.6}
\]

This is well adapted to escaped-charge bookkeeping: at each fixed window an
outgoing packet eventually leaves, and the later spatial exhaustion checks
that the sequence of integer laws does not lose probability or first moment.
It is not the geometry of a pointlike test charge or a fixed angular detector
at null infinity.

**[physical argument]** A control-volume continuum discretisation would choose
a cutoff-dependent window \(W(a)\) with \(aW(a)\to\Omega\), a fixed physical
region, and measure its charge before and after the pulse.  A local detector
would instead keep a small world-tube or angular patch fixed and read its
position, momentum, or phase.  D27 specifies neither joint \(a\to0\),
\(W\to\infty\) scaling.  Holding the number of sites fixed makes the physical
window shrink as \(a|W|\to0\); exhausting the whole chain makes it global.
Neither operation automatically becomes the local detector of section 1.

There is also a uniformity requirement for a continuous probability law.  If
the physical readout is \(y=q_0\nu\), its law is

\[
 \mu_{q_0}=\sum_{\nu\in\mathbb Z}p_\nu\,\delta_{q_0\nu}.       \tag{4.7}
\]

For \(q_0\to0\), a nontrivial real-valued limit needs probability at
\(|\nu|=O(q_0^{-1})\) and tightness/uniform integrability in **physical** units,
for example

\[
 \lim_{M\to\infty}\sup_{q_0,m}
 \sum_{|q_0\nu|>M}(1+|q_0\nu|)p_{W_m,q_0}(\nu)=0.             \tag{4.8}
\]

D27(LR3) is a fixed-model condition in the unscaled variable \(\nu\); it is
not the cutoff-uniform statement (4.8).  If \(p_\nu\) stays fixed as
\(q_0\to0\), (4.7) simply collapses to a point mass at zero.  A continuous
memory law therefore needs an additional scaling family and uniform bound.

### 4.5 Clause-by-clause operational verdict for D27

| D27 component | accepted before/after operation | when they agree | remaining difference |
|---|---|---|---|
| LR1 common-sequence double Cesaro limits | fixed early and late detector records after fields settle | pointwise two-time relaxation implies the Cesaro values | converse fails by (4.3); only a subsequence is required |
| projective \(\widehat Q_{W,c_0}\) at both times | read probe momentum/velocity or relative phase | only after an observable dictionary and negligible-backreaction/classical limit | charge is Fourier-conjugate to angle; (4.5) shows sharp measurement destroys phase coherence |
| LR2 first-moment dephasing condition | detector readout should not materially alter the field/history being inferred | sufficient for the mean charge ledger (4.4) | does not identify full laws or prove operator nondemolition |
| LR3 first-moment-tight exhaustion | keep a physical detector/patch and retain finite data at late time | can model a control-volume charge measurement with a specified joint scaling | D27 exhausts the chain after time averaging and has no cutoff-uniform physical tightness |
| D27 \(\delta x\) | \(\Delta A\), \(\Delta v\), or phase difference | only if a separate response/Gauss-law reconstruction equates the observables | as defined it is the mean wall displacement/escaped hard charge |

Therefore D27 is a defensible **discretisation of the abstract phrase
“measure something before and after an event.”**  It is not, on the definitions
alone, a discretisation of the accepted electromagnetic detector observable.

## 5. Verdict per definition

### 5.1 D13 — different object

**Verdict: DIFFERENT OBJECT.**  D13(a) is a finite-window wall position,

\[
 \mathfrak X_W=a-1+\frac1{2s}\sum_{x=a}^b(S_x^z+s),
 \qquad \delta x=\langle\mathfrak X_W\rangle_f
                 -\langle\mathfrak X_W\rangle_i.              \tag{5.1}
\]

Its continuum object is a collective interface coordinate
\(X_{\rm phys}=a\mathfrak X_W\).  Through **M-flux — PROVED**, its change is
the time-integrated **spin/matter current through the two window boundaries**,
divided by the magnetisation jump \(2s\).  In QED language this is a hard
charged-matter control-volume ledger or moving-boundary conservation law.

D13(b) has the same endpoint/DC algebra as accepted memory—integrate a time
derivative to obtain a late-minus-early value—but its integrand is
\(\dot{\langle S_x^z\rangle}\), not the electric field, and its endpoint is a
wall coordinate, not \(\Delta A\).  D13(c)'s conserved-total-charge trap makes
the difference still clearer: before asymptotic leg subtraction its dynamical
dress is identically zero because the regularised total magnetisation is
conserved.  Electromagnetic memory is instead a change of the gauge potential
whose constraint contains both soft field and hard current data.

Taking \(a,e\to0\) can make (5.1) a continuous physical displacement as in
(3.7); it cannot by itself change its transformation law or turn a matter
current into \(E_i\).  D13 would become an electromagnetic-memory detector
only after adding a model-specific theorem that the wall is a calibrated
charged probe and that its measured late response equals (1.2), or an emergent
duality that maps \(\mathfrak X\) to a gauge holonomy.  No such theorem is in
the audited definitions or claims.

### 5.2 D26 — same compactness theorem, transplanted to a different operator

**Verdict: SAME ABSTRACT COMPACTNESS/COSET STATEMENT; DIFFERENT PHYSICAL
OPERATOR, and insufficient by itself for the decompactification limit.**

The equations

\[
 e^{2\pi iQ}=e^{2\pi i\kappa}I
 \quad\Longleftrightarrow\quad
 \operatorname{spec}Q\subset\kappa+\mathbb Z                 \tag{5.2}
\]

are exactly the representation-theoretic content of a compact circle,
whether \(Q=n_\ell\) is link electric flux or \(Q=S_x^z\) is the campaign's
on-site charge.  The coset/background structure and its cancellation in a
fixed-window TPM are quantitatively identical, (2.8)--(2.12).

But D26 contains only \(S^z\).  It does not contain the conjugate compact
coordinate \(U=e^{i\theta}\), the gauge covariance/Gauss law of a link, or the
memory \(\Delta\theta/(ae)=\Delta A\).  Calling D26 itself a discretisation of
electromagnetic memory would exchange a coordinate for its conjugate momentum
and exchange a gauge link for matter charge.  The correct statement is that
D26 imports the **arithmetic kinematics** that compact lattice QED also has.

For the full link rotor, \(P_A=ae n_\ell\) has vanishing level spacing and may
tend to a real canonical momentum.  For D26's fixed finite on-site spectrum,
\(aeS^z\) instead collapses to zero unless a growing-weight or collective
scaling is added.  If \(S^z\) labels physical matter charge at fixed
renormalised elementary charge, its integer lattice survives in continuum
QED.  All three facts are compatible with a continuous \(\Delta A\).

### 5.3 D27 — same before/after skeleton, different detector and weaker time limit

**Verdict: DIFFERENT OBJECT AS DEFINED; SAME UP TO LISTED GAPS only after an
additional detector/field dictionary is assumed.**

D27 is genuinely operational in the limited sense that it specifies an actual
two-measurement history law, includes measurement backaction in (4.1), and
states its order of limits.  This is stronger and more honest than merely
subtracting two noncommuting charge operators.  It is also a plausible lattice
protocol for escaped matter charge.

It differs from accepted electromagnetic memory in four load-bearing ways:

1. Cesaro/subsequential endpoints can exist without pointwise settled detector
   data; closing this needs the named Tauberian upgrade.
2. It projectively measures windowed matter charge, whereas accepted QED
   memory reads \(\Delta A\), a relative phase, or a probe kick.  LR2 matches
   only the first moment and (4.5) demonstrates the conjugate-phase
   disturbance.
3. It exhausts a spatial charge window after the time limit, whereas the
   accepted detector is local or lives in a fixed angular patch.  A joint
   cutoff/physical-window scaling is absent.
4. A nontrivial continuous limit of the integer law requires a rescaling such
   as (4.7) plus cutoff-uniform physical tightness such as (4.8), neither of
   which D27 asserts.

Even if all four procedural gaps are supplied, one still needs Maxwell's
constraint and boundary data to map escaped hard charge to the field memory,
or a calibrated probe-response theorem to map \(\delta x\) to \(\Delta v\).
With those extra inputs D27 could discretise a particular operational
reconstruction.  Without them it is a charge-history protocol, not the
accepted electromagnetic-memory protocol.

## 6. Compact summary and status boundary

The exact sequence of correspondences is

\[
 \boxed{
 \begin{array}{rcl}
 e^{i\theta_\ell},\ \theta_\ell\in S^1
   &\xrightarrow[ae\to0]{\text{lift}/(ae)}& A_i\in\mathbb R,\\[2mm]
 n_\ell\in\kappa+\mathbb Z
   &\xrightarrow[ae\to0]{\times ae}& P_A\in\mathbb R,\\[2mm]
 \nu\in\mathbb Z
   &\xrightarrow[q_0\to0]{\times q_0}& Q_{\rm esc}^{\rm phys}\in\mathbb R
       \quad\text{(only with a scaling family)},\\[2mm]
 \nu\in\mathbb Z
   &\xrightarrow[q_0=e_R\ne0]{}& Q_{\rm esc}^{\rm phys}\in e_R\mathbb Z
       \quad\text{(charge quantisation survives).}
 \end{array}}
 \tag{6.1}
\]

The first line is the discretisation of the accepted memory field.  The second
line is its conjugate compactness kinematics.  The third and fourth lines
describe charge, not memory, and show why “continuous memory” does not mean
“unquantised electric charge.”

The campaign's proved statements remain exactly as scoped:

- **M-flux — PROVED:** D13 is the finite-time DC boundary **spin-current**
  ledger (3.8).
- **M-INDEX-fin — PROVED:** D26 gives one affine integer coset at fixed window,
  and D27 TPM increments are integral by offset cancellation, not by
  commutativity.
- **M-INDEX-spec — PROVED conditionally:** assuming H-MQG, D26, and
  D27(LR1--LR3), every ordered subsequential TPM law is supported on
  \(\mathbb Z\) and obeys (3.6); the optional convenience clause supplies the
  unique full-sequence value/law.  D27 itself, LR2--LR3, a pointwise limit,
  and the continuum scaling are not thereby proved.

None of those rows proves that \(\mathfrak X_W\), \(\widehat Q_{W,c_0}\), or
their TPM law equals \(\Delta A\) or the charged-probe kick.  The defensible
paper-level conclusion is narrower: the campaign has an exact compact-
\(U(1)\) charge-index/transport memory with the same circle-weight arithmetic
as compact lattice QED, while accepted electromagnetic memory is recovered
from the **link angle (or a calibrated probe response)**, not from D13/D27
without an additional reconstruction theorem.
