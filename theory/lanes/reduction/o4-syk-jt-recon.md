# O4: does SYK/JT carry the one-species infrared triangle?

## 0. Scope, source control, and the standard of comparison

This is a reconnaissance memo, not a proof or a claim-status document.  No
network source and no literature identifier beyond the three specified local
sources was consulted.  Consequently, every statement below of the form "known"
means *exhibited or explicitly described in these three sources*, while every
novelty statement is qualified as "to our knowledge within this source-limited
reconnaissance."  It cannot establish a global absence theorem for the
literature.

The three titles and authors re-verify in the local TeX:

| local source | title verification |
|---|---|
| `refs/arxiv-1606.01857/GravityReparametrizationsRevised.tex` | “Conformal symmetry and its breaking in two dimensional Nearly Anti-de-Sitter space,” Juan Maldacena, Douglas Stanford, and Zhenbin Yang (`GravityReparametrizationsRevised.tex:141-158`). |
| `refs/arxiv-2412.14799/Main.tex` | “Nonlinear soft mode action for the large-$p$ SYK model,” Marta Bucca and Márk Mezei (`Main.tex:31-46`). |
| `refs/arxiv-1306.0622/shock.tex` | “Black holes and the butterfly effect,” Stephen H. Shenker and Douglas Stanford (`shock.tex:38-40`). |

I will call the three campaign tests **A**, **C**, and **B**.  **A** requires an
allowed boundary symmetry modulo transformations that act trivially, together
with its charges and—under the strongest campaign definition—their algebra and
extension.  **C** requires a universal symmetry-controlled soft limit, not just
the statement that one mode is light.  **B** requires a permanent *relational*
DC change left after an event, with a quantum-mechanical detector and a visible
zero-frequency relation to C.  A field coordinate by itself is not enough:
only a correlator, charge, response, or implementable protocol is operationally
meaningful.

**Headline.**  SYK/JT has a very strong A/C backbone and a physically compelling
B candidate.  It is not yet a completed infrared triangle by the strict tests
above: C is a universal soft-mode *dressing* rather than a demonstrated
external-soft-leg theorem, and the shock shift has not been tied to that dressing
by a derived DC Ward identity.  The opportunity is real precisely because the
missing statement is small and falsifiable.

## 1. Corner A — boundary reparametrizations and their charges

### 1.1 The broken orbit

The asymptotic variable is the map from physical boundary time $u$ to the
$AdS_2$ time $t$, not a propagating bulk graviton.  The source states the
boundary nature of the symmetry without qualification:

> “The asymptotic symmetries of $AdS_2$ are all the time reparametrizations of
> the boundary.”
>
> — `refs/arxiv-1606.01857/GravityReparametrizationsRevised.tex:190-195`

The distinct cutout geometries are $t(u)$ modulo the Möbius action

\[
t(u)\sim \frac{a\,t(u)+b}{c\,t(u)+d},\qquad ad-bc=1,
\]

because the two representatives make exactly the same cutout shape
(`GravityReparametrizationsRevised.tex:373-382`).  Thus the Euclidean thermal
soft configuration space is

\[
\mathcal M_{\rm soft}=\operatorname{Diff}(S^1)/SL(2,\mathbb R),
\]

with the line version in Lorentzian signature.  This is both the familiar
breaking notation $\operatorname{Diff}(S^1)\to SL(2,\mathbb R)$ and the
campaign's required quotient by transformations that act trivially.  Maldacena,
Stanford, and Yang are explicit that $t(u)$ labels the zero modes and that they
are Goldstone-like boundary gravitons:

> “the reparametrization symmetry is spontaneously broken by $AdS_2$. It is
> broken to $SL(2,R)$. The zero modes are characterized by the functions
> $t(u)$. These can be viewed as Goldstone bosons.”
>
> — `refs/arxiv-1606.01857/GravityReparametrizationsRevised.tex:401-404`

At nonzero departure from the conformal limit the breaking is also explicit,
so this is a pseudo-Goldstone.  With

\[
\operatorname{Sch}(t,u)
=-\frac12\frac{t''{}^2}{t'{}^2}
  +\left(\frac{t''}{t'}\right)',
\]

the JT boundary action is

\[
I_{\rm Sch}[t]
=-\frac{1}{8\pi G}\int du\,\phi_r(u)\operatorname{Sch}(t,u).
\tag{A.1}
\]

Both the definition and the action are the displayed equations in
`GravityReparametrizationsRevised.tex:490-500`; the source then identifies
$t(u)$ as the field variable and $\phi_r$ as the external coupling
(`GravityReparametrizationsRevised.tex:501-508`).  Equation (A.1) is invariant
under the Möbius redundancy, but it explicitly lifts the other Diff directions.
Accordingly, full Diff is an exact asymptotic/conformal-limit statement and an
approximate emergent symmetry at finite coupling.

### 1.2 What “low dimensional” does and does not imply

**[physical argument]**  There is no conflict with the campaign's finite
endpoint group in a one-dimensional chain.  Spatial infinity of a $1+1$-dimensional
chain has celestial sphere $S^0$, hence only a left and a right endpoint.  The
JT asymptotic coordinate is instead *time*: an allowed transformation is a
function $t\mapsto \widetilde t(t)$ on the boundary line or thermal circle.  A
function space remains infinite-dimensional even when the bulk has only two
dimensions.  “Two endpoints” and “one time-dependent boundary function” are
different asymptotic problems, not rival counts of the same group.

### 1.3 Charges—and the precise missing part of A

The source explicitly constructs the three conserved $SL(2)$ charges of the
Schwarzian.  Writing primes for Lorentzian boundary-time derivatives and using
$C=\bar\phi_r/(8\pi G)$, they are

\[
\begin{aligned}
Q^-&=C\left(\frac{t'''}{t'^2}-\frac{t''^2}{t'^3}\right),\\
Q^0&=C\left(\frac{t t'''}{t'^2}-\frac{t t''^2}{t'^3}-\frac{t''}{t'}\right),\\
Q^+&=C\left(\frac{t^2 t'''}{t'^2}-\frac{t^2t''^2}{t'^3}
             -\frac{2tt''}{t'}+2t'\right).
\end{aligned}
\tag{A.2}
\]

This is the charge equation at
`refs/arxiv-1606.01857/GravityReparametrizationsRevised.tex:889-900`.  The
Hamiltonian is their quadratic Casimir,

\[
H=\frac{-Q^+Q^-+(Q^0)^2}{2C},
\tag{A.3}
\]

as given at `GravityReparametrizationsRevised.tex:921-929`.  In the two-sided
state $Q_L^a=-Q_R^a$, so the total gauge charge vanishes while a one-sided
charge need not (`GravityReparametrizationsRevised.tex:902-909`).  With matter,

\[
Q_T^a=Q^a[t]+q_M^a,
\qquad
\partial_u(Q^-,Q^0,Q^+)=T_{tz}\,t'(1,t,t^2),
\tag{A.4}
\]

and the total is conserved (`GravityReparametrizationsRevised.tex:957-964`).
This is already the soft/hard charge ledger needed for an A-to-C Ward identity.

The qualification is load-bearing.  Equations (A.2) are the charges of the
unbroken/gauged $SL(2)$, not an exhibited charge $Q[\varepsilon]$ for every
asymptotic Diff generator.  Nor do the three allowed sources derive the
asymptotic charge algebra or a central extension.  The 2016 source itself says:

> “Here we have mentioned neither the algebra nor the central charge. It would
> be nice to see whether and how it can be defined.”
>
> — `refs/arxiv-1606.01857/GravityReparametrizationsRevised.tex:1167-1172`

One may expect (A.2) to realize the ordinary $\mathfrak{sl}_2$ brackets, but
that expectation is not the missing Diff charge algebra.  Under the campaign's
strong definition “boundary implementers modulo trivial action, charge algebra
and extension,” corner A is therefore **structurally present but not fully closed**.
The symmetry, quotient, pseudo-Goldstone, invariant action, finite constraint
charges, and matter/soft split are literature-known here; an operational Diff
charge algebra and its extension, tied to microscopic SYK observables, would be
additional work rather than a result to import from these sources.

## 2. Corner C — universal soft-mode dressing, but not yet an LSZ soft theorem

### 2.1 The microscopic and nonlinear control

For a member of the SYK ensemble, the microscopic degrees of freedom are $N$
Majorana fermions with random $p$-body couplings,

\[
H=\sum_{i_1<\cdots<i_p}J_{i_1\cdots i_p}
  \Psi_{i_1}\cdots\Psi_{i_p},
\]

with the Gaussian coupling variance displayed in
`refs/arxiv-2412.14799/Main.tex:84-96`.  After dropping the UV kinetic term, the
bilocal Schwinger-Dyson equations are invariant under $\tau\mapsto f(\tau)$,
with

\[
G(\tau_1,\tau_2)\mapsto
[f'(\tau_1)f'(\tau_2)]^{1/p}
G(f(\tau_1),f(\tau_2)),
\tag{C.1}
\]

and the corresponding transformation of the self-energy
(`Main.tex:124-140`).  Restoring the discarded $\partial_\tau$ term explicitly
breaks this invariance (`Main.tex:141-146`).  The resulting thermal action is

\[
S[f]=-\frac{N\alpha_S}{\beta\mathcal J}
\int_0^{2\pi}du\,
\operatorname{Sch}\!\left[\tan\frac{f}{2},u\right],
\qquad \alpha_S=\frac{1}{4p^2}\quad(p\gg1).
\tag{C.2}
\]

This equation and the definition of its variables are at
`Main.tex:59-64`.  Bucca and Mezei do more than linear matching: they derive
the full nonlinear functional and its coefficient from the large-$p$
collective theory.  Their separation between the soft direction and the rest
is explicit:

> “the orthogonal ‘hard directions’ have an action that is $O(N/p^2)$ ...
> Fluctuations in the reparametrisation direction in field space are enhanced
> by their small action.”
>
> — `refs/arxiv-2412.14799/Main.tex:311`

The same calculation evaluates the microscopic deformation on the full family
of reparametrized saddles and obtains the nonlinear thermal Schwarzian
(`Main.tex:291-309`).  This makes the “soft mode dominates” statement a
controlled large-$N$, then large-$p$, low-temperature result rather than a
name attached to a guessed collective coordinate.

### 2.2 The factor that dresses the hard insertions

The universal ingredient is most transparent on the gravity side.  A primary
matter correlator is evaluated at the reparametrized times and receives one
$t'(u_i)^{\Delta_i}$ factor per insertion.  The source emphasizes the
all-correlator scope:

> “Though we did this for the two point function, the same is true for any
> $n$ point function.”
>
> — `refs/arxiv-1606.01857/GravityReparametrizationsRevised.tex:662-668`

The physical correlator is then obtained by integrating this dressed matter
functional over $t(u)$ with the Schwarzian action
(`GravityReparametrizationsRevised.tex:669-675`).  Around the thermal saddle,
$t=u+\varepsilon$, the linear vertex attached to a bilocal hard pair is

\[
\mathcal B_{12}[\varepsilon]
=\varepsilon'(u_1)+\varepsilon'(u_2)
-\frac{\varepsilon(u_1)-\varepsilon(u_2)}
       {\tan(u_{12}/2)}.
\tag{C.3}
\]

Thus, for two hard bilocals $V_1V_2$ and $W_3W_4$, the leading connected
piece is

\[
\frac{\langle V_1V_2W_3W_4\rangle_{\rm grav}}
     {\langle V_1V_2\rangle\langle W_3W_4\rangle}
=\Delta_V\Delta_W
  \langle\mathcal B_{12}\mathcal B_{34}\rangle_{\rm Sch},
\tag{C.4}
\]

with the equal-dimension version, including its $1/(2\pi C)$ coefficient,
given in `GravityReparametrizationsRevised.tex:729-753`.  The source also notes
that $\mathcal B$ is $SL(2)$-invariant
(`GravityReparametrizationsRevised.tex:737-740`).

This gives the requested dictionary at C:

- the **hard legs** are microscopic fermion insertions in SYK, or matter-primary
  insertions/bilocal pairs on the JT side;
- the **universal soft factor** is the reparametrization vertex (C.3) on each
  hard object, contracted with the Schwarzian soft-mode propagator; and
- the **hard-data dependence** is reduced to representation data such as
  $\Delta_i$, insertion times, and the background $\beta$, while the soft
  sector enters through the single stiffness $C$ (or $N\alpha_S/\mathcal J$).

This is universal within the nearly-CFT$_1$/Schwarzian class, not literally
state-independent over the whole Hilbert space.  The thermal saddle, $\beta$,
the final energy sector, and irrelevant corrections matter.  The functional
dressing rule is universal; its numerical realization is state- and
model-dependent through those few parameters.

### 2.3 Pole, zero, and the terminology fence

The quadratic thermal action is

\[
I^{(2)}_\varepsilon=\frac{C}{2}\int du
\left[(\varepsilon'')^2-(\varepsilon')^2\right],
\tag{C.5}
\]

and its $n=0,\pm1$ modes are precisely the $SL(2)$ redundancies that must be
gauge-fixed (`GravityReparametrizationsRevised.tex:680-706`).  The remaining
propagator is enhanced as the explicit-breaking scale becomes small
(`GravityReparametrizationsRevised.tex:710-719`).  In microscopic language, the
strict-IR fermion ladder sum diverges because the spontaneously broken
reparametrization mode has zero action; moving away from the strict IR makes it
a pseudo-Goldstone and regulates the divergence
(`refs/arxiv-2412.14799/Main.tex:66-68`).

**[physical argument]**  That enhanced propagator/ladder divergence is what
plays the role of the *soft pole*.  In a zero-temperature continuous-frequency
expansion, (C.5) reduces schematically to $C\omega^4|\varepsilon(\omega)|^2$,
so the undressed collective propagator is more IR-singular than a Weinberg
$1/\omega$ pole.  At finite temperature this language must be handled with
care: frequency is discrete, and the exact $n=0,\pm1$ zero modes are removed
as gauge.

There is no demonstrated Adler zero here.  The closest zero is that the
invariant vertex (C.3) annihilates the three pure-$SL(2)$ directions.  That is
decoupling of a gauge redundancy, not a theorem that an on-shell amplitude with
one external pseudo-Goldstone vanishes as its energy tends to zero.  SYK in
$0+1$ dimensions has neither spatial asymptotic scattering states nor an LSZ
soft-particle limit of the campaign's magnon type.

The right assessment is therefore:

- **literature-known here:** nonlinear Schwarzian action and coefficient at
  large $p$, soft/hard separation, arbitrary-correlator reparametrization
  dressing, enhanced four-point exchange, and its chaotic continuation;
- **structurally a soft theorem:** yes—the same symmetry-fixed vertex and soft
  propagator dress every hard correlator in the low-energy class;
- **a soft theorem in the campaign's strict sense:** not yet—there is no
  exhibited external soft leg, Ward/LSZ factorization statement, controlled
  remainder, or DC identity to B.  Producing that response-theory analogue,
  rather than renaming (C.4), is the genuinely additional part of corner C.

## 3. Corner B — is the shockwave frame shift memory?

### 3.1 The candidate

Shenker and Stanford perturb one side of a thermofield double by a small early
energy pulse.  Its large boost makes the backreaction a null shock.  Matching
the BTZ regions immediately before and after the shell gives

\[
\widetilde v=v+\alpha,
\qquad
\alpha=\frac{E}{4M}e^{Rt_w/\ell^2},
\tag{B.1}
\]

in the controlled limit $E/M\to0$, $t_w\to\infty$ at fixed $\alpha$
(`refs/arxiv-1306.0622/shock.tex:188-200`).  In discontinuous shock coordinates
$U=u$, $V=v+\alpha\theta(u)$, the metric contains the impulsive term
$4\ell^2\alpha\delta(U)dU^2$ (`shock.tex:202-205`).  Geometrically, the two
horizons miss by the finite amount $\alpha$ after the shell
(`shock.tex:206-215`).

This is an unusually clean memory candidate: a compact event leaves a step in a
reference frame.  In the reparametrization description, the corresponding
piecewise change is a displacement of the boundary-time frame.  Maldacena,
Stanford, and Yang make the relational nature of exactly this kind of change
explicit:

> “We can always make an $SL(2)$ gauge transformation to remove this effect on
> either the portion of the contour before $V$ or the portion after, but not
> both.”
>
> — `refs/arxiv-1606.01857/GravityReparametrizationsRevised.tex:1122`

The absolute coordinate shift is scaffolding; the mismatch between the two
portions of the contour is the physical datum.  Although a global $SL(2)$
move is trivial, a *piecewise* move with a charge-carrying insertion between its
two pieces is not removable by one gauge choice.  It is therefore sensible to
regard the relative frame change as valued in the reparametrization orbit—the
same collective manifold that carries the pseudo-Goldstone—rather than as a
new bulk species.

### 3.2 The detector: the second side is the ruler

The clean detector is not $v$ itself.  Prepare two copies in the thermofield
double, apply $W_L$ to create the pulse, and measure the joint two-sided
correlator

\[
\langle\varphi_L\varphi_R\rangle_W
=\frac{\langle\Psi|W^\dagger\varphi_L\varphi_RW|\Psi\rangle}
       {\langle\Psi|W^\dagger W|\Psi\rangle}.
\tag{B.2}
\]

This is the source's explicit matrix element (`shock.tex:275-280`), and in the
geodesic regime it becomes

\[
\langle\varphi_L\varphi_R\rangle_W
\sim\left(1+\frac{E}{8M}e^{Rt_w/\ell^2}\right)^{-2m\ell}.
\tag{B.3}
\]

Equation (B.3) is quoted from `shock.tex:288-293`.  The two-sided mutual
information gives an independent detector with the same $\alpha$-dependence
(`shock.tex:243-268`).  In a microscopic two-copy SYK experiment, (B.2) is an
ordinary joint fermion/bilinear correlation protocol; no measurement of the
collective coordinate $f$ is required.  This realizes the campaign maxim
that memory needs a probe: the untouched right copy supplies the reference
clock against which the left frame shift is meaningful.

### 3.3 Permanence and DC: what is present, and what is not

There are two distinct meanings of “permanent,” and the sources establish only
the first.

1. **Geometric step permanence.**  In the ideal shock solution,
   $\delta V(U)=\alpha\theta(U)$ is constant everywhere after the shell.  With
   the Fourier convention $\widetilde x(\omega)=\int dU\,e^{i\omega U}x(U)$,
   
   \[
   \widetilde{\delta V}(\omega)
   =\alpha\left[\pi\delta(\omega)+i\,\mathrm{PV}\frac1\omega\right],
   \qquad
   \partial_U\delta V=\alpha\delta(U).
   \tag{B.4}
   \]
   
   **[physical argument]**  Equation (B.4) is the kinematic DC/zero-mode
   identity expected of any step response.  It follows directly from the
   sourced metric at `shock.tex:198-205`; it is not a dynamical soft theorem.

2. **Operational late-time permanence.**  The source varies how far in the past
   the perturbation is inserted while measuring at a fixed reference time.  It
   does not hold a finite pulse fixed and prove that a stationary-subtracted
   detector remains shifted as the detector time tends to $+\infty$.  Indeed,
   the general geodesic answer contains
   $\alpha e^{-R(t_L+t_R)/(2\ell^2)}$
   (`shock.tex:223-234`), so the shock correction seen by equal late-time
   boundary probes can decay even though the null-coordinate matching retains
   its step.  A permanent coordinate matching is not automatically a permanent
   operational record.

The A/C/B connection visible in the sources is consequently close but not
closed.  Matter flux changes the Schwarzian $SL(2)$ charges while preserving
the total charge, as in (A.4).  An early hard insertion changes $Q^-$; its
conserved value produces the exponentially growing reparametrization effect,
and an out-of-time-order four-point function detects both sides of the insertion
(`GravityReparametrizationsRevised.tex:1116-1122`).  The same source says that
the result ordinarily attributed to shock scattering can be moved entirely
into the boundary variable $t(u)$
(`GravityReparametrizationsRevised.tex:794-798`).

What is *not* in the three sources is an equation identifying the residue or DC
coefficient in (B.4) with the zero-frequency coefficient of the universal
Schwarzian dressing in C.  The shock paper is a BTZ calculation, not an exact
large-$p$ SYK/JT response calculation; its $\alpha$ is boost-enhanced hard
backreaction, not by itself the $\omega\to0$ limit of (C.3).  Nor does (B.3)
establish a non-decaying late detector after subtracting the changed final
energy/temperature.

Corner B is therefore **a strong, operationally accessible memory candidate,
not yet a demonstrated memory effect in the campaign's strict sense**.
Literature-known here are the shock step, its charge/frame interpretation, and
two-sided detection.  To our knowledge within this source-limited
reconnaissance, the new contribution would be (i) the explicit memory framing,
(ii) a late-time stationary-subtracted observable, and (iii) its derived
DC/soft-mode identity.  Failure of either (ii) or (iii) would demote the effect
to a transient chaos/time-delay response rather than complete corner B.

## 4. The microscopic dictionary to the campaign

The most useful correspondence is operational rather than geometric:

| role | SYK/JT | campaign spin chain |
|---|---|---|
| microscopic system | $N$ Majoranas with random $p$-body couplings; in the chain, one such cluster per site | local spins with fixed local couplings |
| infrared collective mode | one time reparametrization $f(u)$ per SYK cluster/boundary, modulo $SL(2)$ | magnon Goldstone field; kink collective coordinate in the broken discrete sector |
| broken symmetry | emergent $\operatorname{Diff}(S^1)\to SL(2,\mathbb R)$, explicitly broken at finite $\beta\mathcal J$ | microscopic internal $G\to H$, exact unless the Hamiltonian is explicitly deformed |
| soft effective theory | Schwarzian, with stiffness $N\alpha_S/\mathcal J$ | low-momentum magnon EFT/exact lattice scattering data |
| hard objects | fermion or matter-primary insertions, naturally grouped into bilocals | hard magnons and kinks |
| candidate memory carrier | relative boundary/Kruskal-frame shift, or piecewise relative $SL(2)$ frame | permanent kink displacement / changed vacuum sector |
| operational detector | microscopic fermion bilocals, two-sided correlators, mutual information, charge/energy response | local spin measurements, kink-position window, interferometric scattering phase |
| gauge-like scaffolding | a representative $f$, including its three $SL(2)$ zero modes | excitation-ansatz tensor and null/gauge datum |

The last row is an exact analogy at the level of *operational logic*, not an
identification of the two gauge structures.  Two $f$'s related by $SL(2)$
represent the same JT cutout, and the $SL(2)$ terms in the soft propagator
cancel from gauge-invariant bilocals
(`refs/arxiv-1606.01857/GravityReparametrizationsRevised.tex:703-715`).  Hence an
absolute plotted $f(u)$ is not an observable.  Its invariant orbit, charge
jump, and effect on a fermion correlator are.  Likewise, the campaign's ansatz
gauge coordinate is not measurable although the scattering phase inferred
with it is.  Importantly, not *all* of $f$ is gauge: the
$\operatorname{Diff}/SL(2)$ fluctuations have physical effects.  The gauge
statement concerns the representative and the $SL(2)$ directions, not the
whole soft sector.

There is also a literal lattice bridge.  Bucca and Mezei derive a large-$p$
SYK chain whose site variable is $f_x$.  Its action is a sum of on-site
Schwarzians plus a nearest-neighbour term built from reparametrized bilocals
(`refs/arxiv-2412.14799/Main.tex:72-79`); the microscopic nearest-neighbour
Majorana Hamiltonian is displayed at `Main.tex:524-534`.  This is a
“Schwarzian chain,” but it should not be conflated with the campaign's magnon
chain.  Each site still carries a function of *time*, and the inter-site term is
nonlocal in time.  What it offers is an explicit spatial lattice on which a
frame-shift response and its propagation can be computed microscopically.

### Honest disanalogies and scope conditions

1. **No spatial infinity in a single SYK dot.**  SYK is $0+1$-dimensional;
   its asymptotics and softness concern time and the low-frequency limit.  It
   has no Haag-Ruelle/LSZ spatial scattering problem.  The SYK chain adds space,
   but not the campaign's internal-symmetry Goldstone mechanism.

2. **No local graviton.**  Two-dimensional dilaton gravity has no propagating
   bulk degrees of freedom
   (`GravityReparametrizationsRevised.tex:234-240`).  “One-species pure
   gravity” means a single *boundary collective field* $f$, not a single
   on-shell graviton species.  Matter is still required to make the event and
   read the result; “pure” describes the universal carrier sector, not an empty
   experiment.

3. **Pseudo- rather than exact Goldstone.**  The UV kinetic term or finite
   radial cutoff explicitly breaks Diff.  Soft statements therefore have a
   regime $\omega,T\ll\mathcal J$ and calculable $1/(\beta\mathcal J)$,
   $1/p$, and $1/N$ corrections.  A theorem without this error hierarchy
   would overstate the source.  Very light additional fields can even outrun
   the Schwarzian breaking term
   (`GravityReparametrizationsRevised.tex:1137-1141`).

4. **Thermal/chaotic rather than vacuum scattering kinematics.**  The key hard
   observable is normally a thermal four-point or two-sided correlator.  Its
   exponential OTO continuation is not an Adler limit, and its late-time decay
   is part of the physics rather than a removable nuisance.

5. **Disorder and the single realization.**  The SYK model is an ensemble, and
   the large-$N$ collective action used here is obtained with annealed disorder
   averaging (`refs/arxiv-2412.14799/Main.tex:84-106`).  An ensemble average is
   operational as a repeated protocol over programmed coupling samples.  A
   particular laboratory Hamiltonian, however, is one realization.  A genuinely
   operational triangle must either demonstrate the DC/soft identity sample by
   sample or give a quantitative self-averaging statement for the measured
   correlator.  None of the three sources supplies that memory-specific check.

6. **The second boundary is substantive.**  The two-sided reference makes an
   otherwise gauge-like time-frame displacement observable.  A one-sided
   formulation would need an explicit clock/detector degree of freedom; an
   absolute $f(+\infty)-f(-\infty)$ is not a substitute.

## 5. What would actually be new, and the cheapest decisive computation

### 5.1 Corner-by-corner novelty ledger

The novelty bar is not met by putting three familiar words around the same
four-point function.  Within the deliberately restricted three-source window,
the honest ledger is:

| corner | already in the sources | genuinely additional result | result that would kill the proposed identification |
|---|---|---|---|
| **A** | asymptotic time reparametrizations; $\operatorname{Diff}/SL(2)$ soft orbit; Schwarzian pseudo-Goldstone action; $SL(2)$ boundary and matter-charge ledger | an operational $Q[\varepsilon]$ algebra (and extension, if any) for the asymptotic Diff action on microscopic correlators, with a Ward identity that reduces to the finite charge ledger | all candidate Diff charges beyond $SL(2)$ are either non-observable redundancies or explicitly broken with no controlled approximate Ward identity |
| **C** | nonlinear large-$p$ action and prefactor; soft-mode dominance; universal all-$n$-point reparametrization dressing; $e^{2\pi t/\beta}$ OTO response | a precisely normalized low-frequency response/factorization theorem with a hard-source insertion, a controlled finite-$\beta\mathcal J,p,N$ remainder, and a statement of which zero replaces LSZ | the low-frequency coefficient depends on hard microscopic data beyond dimensions, charges, and thermodynamic parameters, or no source-independent limit exists |
| **B** | BTZ shock shift; piecewise charge/frame change; two-sided correlator and mutual-information probes | a nonzero late-time, final-state-subtracted relative-clock displacement in Schwarzian/large-$p$ SYK, plus equality of that displacement with the C coefficient | after subtracting the final equilibrium state the measurable shift decays to zero, or its DC coefficient is unrelated to the soft response |
| **edges** | charge conservation explains the reparametrization response; the same boundary mode computes four-point chaos and shock-like effects | one common Ward identity yielding A$\to$C and, by its zero-frequency limit, C$\to$B | A$\to$C and the shock response require unrelated limits or noncommuting state preparations |

The $e^{2\pi t/\beta}$ growth itself is explicit in
`refs/arxiv-1606.01857/GravityReparametrizationsRevised.tex:784-792`.  Calling it
“chaos-bound saturation” uses standard context, but the bound is not derived in
the three allowed sources; the local evidence is the exponent, Schwarzian
dominance, and shock scrambling time.  Likewise, “the memory framing is not
packaged elsewhere” can only be a source-limited assessment here.  What would
make the work genuinely new is not the label but the operational plateau and
the shared coefficient.

### 5.2 Cheapest decisive computation: a sourced two-sided Schwarzian ODE

The cheapest calculation is classical/tree-level Schwarzian response at large
$C$, before attempting the full large-$p$ collective-field path integral.  It
uses equations already present in the sources and is only a one-dimensional
sourced boundary-value problem.

1. **Prepare and perturb.**  Prepare two Schwarzian boundaries in the
   thermofield-double saddle.  Apply a compactly supported right-boundary matter
   source $J_R(u)$, or equivalently a specified flux $T_{tz}(u)$, during
   $u\in[u_i,u_f]$.  Record the final ADM energy.  Either use a balanced source
   with zero net energy or compare against the equilibrium saddle at that same
   final energy; otherwise a permanent temperature change will masquerade as
   frame memory.

2. **Solve the exact soft equation.**  Integrate

   \[
   C\,\frac{\partial_u\operatorname{Sch}(t,u)}{t'(u)}
   =-t'(u)T_{tz}(u),
   \tag{T.1}
   \]

   which is the sourced Schwarzian equation at
   `refs/arxiv-1606.01857/GravityReparametrizationsRevised.tex:611-623`.
   Outside the compact source the charges are constant, so the before and after
   solutions are thermal maps related by definite Möbius data.  Fix the one
   simultaneous $SL(2)$ redundancy and retain only the *relative* transform
   between the right and left clocks.

3. **Read only an observable.**  Insert that solution into a two-sided invariant
   bilocal and compute

   \[
   \delta G_{LR}(T)
   =G^{\rm pulse}_{LR}(T,T)
    -G^{\rm eq}_{LR}(T,T;E_f).
   \tag{T.2}
   \]

   Fit (T.2), when possible, to a relative time displacement
   $\delta G_{LR}\simeq-\Delta u_{\rm rel}\,\partial_TG^{\rm eq}_{LR}$.
   The memory test is whether $\Delta u_{\rm rel}$ approaches a nonzero
   constant as $T-u_f\to\infty$, not whether a chosen representative $t(u)$
   contains a step.

4. **Do the zero-mode comparison in the same calculation.**  Fourier transform
   the retarded response before taking the late-time limit and test

   \[
   \Delta u_{\rm rel}
   =\lim_{\omega\to0}\big[-i\omega\,\delta u_{\rm rel}(\omega)\big]
   \stackrel{?}{=}
   \lim_{\omega\to0}\mathcal S_{\rm Sch}
       (\omega;\text{same hard source}),
   \tag{T.3}
   \]

   where $\mathcal S_{\rm Sch}$ is obtained by attaching the invariant vertex
   (C.3) to the same hard insertion and using the retarded continuation of the
   Schwarzian propagator.  The normalization is fixed by (T.1) and the measured
   hard charge, not fitted independently.

This computation is decisive in both directions.  A nonzero plateau in (T.2)
with the equality (T.3) gives a genuine operational B and the C$\to$B edge.  A
vanishing stationary-subtracted plateau says that the butterfly shift is a
transient relational time delay, not memory in the campaign's sense, even
though the ideal Kruskal metric contains $\alpha\theta(U)$.  A plateau without
(T.3) gives memory but not a triangle.

Only after this tree-level test passes is the more expensive calculation
justified: repeat (T.1)–(T.3) directly in the large-$p$ Liouville collective
theory, using the nonlinear embedding and coefficient derived in
`refs/arxiv-2412.14799/Main.tex:291-311`, and then in a fixed disorder
realization.  The Schwarzian-chain version can subsequently test spatial
propagation and whether the record survives diffusion; it is not needed for the
first yes/no decision.

## 6. Verdict

1. **Triangle?**  Yes as a one-soft-species, pure-boundary-gravity *candidate*; no as an already established A/C/B triangle, because the Diff charge algebra, external-soft/response theorem, and operationally permanent B–C identity are missing.
2. **Cheapest decisive computation?**  Solve the compactly sourced two-sided Schwarzian equation (T.1), measure the final-energy-subtracted correlator plateau (T.2), and compare its DC residue with the independently normalized soft response (T.3).
3. **Effect on the campaign?**  It strengthens the opportunity reading: low dimension does not force a finite asymptotic group, gauge-like collective coordinates are acceptable when relational correlators detect them, and a failure of the plateau would sharpen—rather than threaten—the rule that a coordinate shift without a persistent probe record is not memory.
