# EMCore physics notes and builder contract

## Conventions

`em-core.js` uses Gaussian natural units with (c=hbar=1), metric-independent
three-vector formulas, and a source field normalized per unit source charge.
For an elementary source charge (e), (e^2=alpha), with
(alpha=1/137.035999084). Consequently the field and memory functions return
the geometric answer per source charge (and, for a test-particle velocity
kick, per product of source and test charges), while the radiated spectrum and
photon number explicitly contain (alpha/(4pi^2)). Vectors are ordinary
Cartesian arrays. A hat denotes a unit vector,
(kappa=1-hat{mathbf n}mathbin{cdot}oldsymboleta), and
(mathbf P_perpmathbf a=mathbf a-hat{mathbf n}
(hat{mathbf n}mathbin{cdot}mathbf a)).

The kicked source is massive: both endpoint speeds must be strictly below
one. The separate scattering-particle helpers accept null legs
((|\boldsymbol\beta|=1)) away from their genuine collinear singularities.
The raised-cosine kick is centered on (t=0); thus the particle is at the
origin at (t=0), and the compact transition occupies
([-	au/2,	au/2]). For `tanh`, (	au/2) is the tanh scale rather than a
compact duration. `instant` sets (	au=0).

## 1. Trajectory

Write (Deltaoldsymboleta=oldsymboleta_f-oldsymboleta_i).
Every smooth profile has

\[
 \mathbf r(t)=\boldsymbol\beta_i t+\Delta\boldsymbol\beta J(t),\qquad
 \boldsymbol\beta(t)=\boldsymbol\beta_i+\Delta\boldsymbol\beta h(t),\qquad
 \dot{\boldsymbol\beta}(t)=\Delta\boldsymbol\beta\dot h(t),
\]

where (J'(t)=h(t)) and (J(0)=0). For the compact raised cosine, with
(s=t/	au+1/2),

\[
 h=\begin{cases}0&s\leq0\\(1-\cos\pi s)/2&0<s<1\\1&s\geq1,
 \end{cases}\quad
 J=\tau\left({s\over2}-{\sin\pi s\over2\pi}\right)-J(0)
\]

inside the transition and continued linearly outside. Both velocity and
acceleration join continuously, so the trajectory is (C^2) (and therefore
at least the requested (C^1)). For `tanh`,

\[
 h={1+\tanh(t/a)\over2},\quad
 \dot h={\operatorname{sech}^2(t/a)\over2a},\quad
 J={1\over2}\left[t+a\log\cosh(t/a)\right],\quad a={\tau\over2}.
\]

The logarithm is evaluated with a stable large-argument expression. The
instantaneous position is (oldsymboleta_i t) before zero and
(oldsymboleta_f t) after zero.

## 2. Retardation, Lienard-Wiechert field, and the Purcell shell

The solver finds the unique causal root

\[
 f(s)=t-s-|\mathbf x-\mathbf r(s)|=0,
\]

starting with the upper endpoint (s=t), doubling a past-directed interval
until it brackets the root, and then using safeguarded Newton steps
(f'(s)=-[1-\hat{\mathbf n}\cdot\boldsymbol\beta(s)]). A secant step and
bisection are fallbacks if Newton leaves the bracket. The absolute residual
tolerance is (10^{-13}).

At the returned time, with
(mathbf R=mathbf x-mathbf r(t_{\rm ret})), (R=|\mathbf R|), and
(hat{mathbf n}=mathbf R/R), the exact field per unit charge is

\[
 \mathbf E_{\rm vel}={
 (1-\beta^2)(\hat{\mathbf n}-\boldsymbol\beta)
 \over \kappa^3R^2},\qquad
 \mathbf E_{\rm rad}={
 \hat{\mathbf n}\times[(\hat{\mathbf n}-\boldsymbol\beta)
 \times\dot{\boldsymbol\beta}]
 \over\kappa^3R},\qquad
 \mathbf B=\hat{\mathbf n}\times\mathbf E.
\]

For constant motion through the origin this is equivalently the boosted
Coulomb field

\[
 \mathbf E_\beta(\mathbf x,t)={
 (1-\beta^2)(\mathbf x-\boldsymbol\beta t)
 \over\left[(\mathbf x-\boldsymbol\beta t)^2-
 |\boldsymbol\beta\times\mathbf x|^2\right]^{3/2}}.
\]

For an instantaneous kick at the origin and (t>0), this old field applies
for (|\mathbf x|>t) and the new field for (|\mathbf x|<t). On the sphere
(r=t), define

\[
 \mathbf h_\beta(\hat{\mathbf n})={\boldsymbol\beta\over
 1-\hat{\mathbf n}\cdot\boldsymbol\beta},\qquad
 \mathbf M(\hat{\mathbf n})=
 \hat{\mathbf n}\times\left[\hat{\mathbf n}\times
 (\mathbf h_f-\mathbf h_i)\right].
\]

The radiation field is the distribution

\[
 \mathbf E_{\rm shell}(\mathbf x,t)={\mathbf M(\hat{\mathbf n})\over r}
 \delta(t-r).
\]

`fieldAt` reports the ordinary old/new field and, exactly on the shell, puts
(mathbf M/r) in `shell.transverseCoefficient`. It does **not** invent a
finite value for a delta function.

There is no finite, regulator-independent (E_\perp/E_r) ratio on an ideal
delta shell. If the page deliberately resolves the delta function as a
top-hat of observer-time thickness (Delta), the exact regulated,
side-dependent readout is

\[
 {\mathbf E_{\rm shell}\cdot\mathbf e_A\over E_{r,i/f}}
 ={r\over\Delta}\,{\mathbf M\cdot\mathbf e_A\over C_{i/f}},\qquad
 C_\beta={1-\beta^2\over(1-\hat{\mathbf n}\cdot\boldsymbol\beta)^2}.
\]

For collinear velocities along (z), this reduces to
(M_\theta=\sin\theta[\beta_f/(1-\beta_f\cos\theta)-
\beta_i/(1-\beta_i\cos\theta)]). The page must label (Delta); without it,
the requested ratio is not a number. For a smooth kick the page may instead
print the literal ratio obtained from `fieldAt`, with its chosen (	au).

## 3. Field lines and flux labels

`fieldLine` traces the normalized exact fixed-time electric field in both
directions with classical fourth-order Runge-Kutta, fixed spatial step
`step`, and at most `maxSteps` steps each way.

`purcellLines` uses an exact flux label. If (oldsymbol\ell) is a uniformly
distributed rest-sphere direction and (gamma=(1-eta^2)^{-1/2}), its
aberrated direction is

\[
 \mathcal A_\beta(\boldsymbol\ell)=
 {\boldsymbol\ell+left[\gamma+{(\gamma-1)
 (\boldsymbol\beta\cdot\boldsymbol\ell)\over\beta^2}\right]
 \boldsymbol\beta
 \over\gamma(1+\boldsymbol\beta\cdot\boldsymbol\ell)}.
\]

The Jacobian and Coulomb profile obey

\[
 d\Omega_n={d\Omega_\ell\over
 \gamma^2(1+\boldsymbol\beta\cdot\boldsymbol\ell)^2},\qquad
 C_\beta(\mathcal A_\beta\boldsymbol\ell),d\Omega_n=d\Omega_\ell.
\]

Thus a common label (oldsymbol\ell) maps exactly to the old and new shell
angles (mathcal A_{\beta_i}\boldsymbol\ell) and
(mathcal A_{\beta_f}\boldsymbol\ell), conserving flux. Inner and outer
segments are the exact straight boosted-Coulomb rays. The zero-thickness
shell does not define a unique ordinary three-dimensional connector curve;
the returned great-circle connector is a rendering representative between
the exact flux-matched endpoints, not an extra physical claim. A resolved
shell should use `fieldLine` instead. The tests show its tangent approaches
the Purcell inner/outer tangent linearly as (	au\to0).

## 4. Frequency domain and the soft coefficient

The implemented Jackson-style radiation amplitude is

\[
 \mathbf J(\omega,\hat{\mathbf n})=
 \int ds\,{\hat{\mathbf n}\times[(\hat{\mathbf n}-\boldsymbol\beta)
 \times\dot{\boldsymbol\beta}]\over(1-\hat{\mathbf n}\cdot
 \boldsymbol\beta)^2}
 e^{i\omega[s-\hat{\mathbf n}\cdot\mathbf r(s)]}.
\]

This is the Fourier transform of the exact leading (1/r) radiation field;
the factor changing from (kappa^{-3}) to (kappa^{-2}) is
(dt_{\rm obs}=kappa,ds). Composite eight-node Gauss-Legendre quadrature
is used. The default number of panels is
(max(24,\lceil24+2\omega\tau\rceil)). The raised-cosine support is exact.
For tanh, the spectral integral uses ([-10\tau,10\tau]), where the omitted
endpoint fraction is below (10^{-17}); this is a controlled truncation, not
compact support.

With the Fourier convention in the code,

\[
 {d^2I\over d\omega,d\Omega}={\alpha\over4\pi^2}|\mathbf J|^2.
\]

For the instantaneous kick, (mathbf J=mathbf M), independent of
(omega). The current/potential soft-pole coefficient for transverse
(oldsymbol\epsilon) is

\[
 S_{\rm cl}=\left({\boldsymbol\beta_f\over\kappa_f}-
 {\boldsymbol\beta_i\over\kappa_i}\right)\cdot\boldsymbol\epsilon.
\]

The electric-field convention has
(mathbf M\cdot\boldsymbol\epsilon=-S_{\rm cl}); the sign disappears in
the spectrum. `photonNumber` computes

\[
 N={\alpha\over4\pi^2}\int_{\omega_{\min}}^{\omega_{\max}}
 {d\omega\over\omega}|\mathbf J(\omega)|^2.
\]

It uses GL8 in (log\omega) (48 panels by default). For `instant`, this is
exactly (alpha|\mathbf M|^2\log(\omega_{\max}/\omega_{\min})/(4\pi^2)):
a pure number proportional to (alpha).

The source theorem is `soft_Arxiv_update.tex` lines 1075--1082: the leading
outgoing-photon matrix element is the hard matrix element multiplied by the
out-minus-in sum (eQ_k,p_k\cdot\epsilon/(p_k\cdot q)), plus (O(q^0)).

**Builder-safe sentence (classical/quantum):** “For
(q^\mu=\omega(1,\hat{\mathbf n})),
(p^\mu=m\gamma(1,\boldsymbol\beta)), and transverse polarization,
(p\cdot\epsilon/(p\cdot q)=\boldsymbol\beta\cdot\boldsymbol\epsilon/
[\omega(1-\hat{\mathbf n}\cdot\boldsymbol\beta)]); therefore the kicked
charge’s classical (1/\omega) coefficient is exactly the single-emitter
kinematic factor in Weinberg’s leading soft theorem (out minus in), with the
displayed charge and coupling.”

This sentence uses the polarization/sign convention requested by the lane
brief. If a four-vector convention gives both scalar products an overall
relative minus sign, that convention must be propagated consistently rather
than changing only one side.

## 5. Celestial sphere

For external legs `{Q, beta, eta}`, with (eta=+1) outgoing and (-1)
incoming, define

\[
 \mathbf H(\hat{\mathbf n})=\sum_k {\eta_kQ_k\boldsymbol\beta_k\over
 1-\hat{\mathbf n}\cdot\boldsymbol\beta_k}.
\]

`spherePattern` returns
(|\hat{\mathbf n}\times(\hat{\mathbf n}\times\mathbf H)|^2). Completeness
of two orthonormal transverse polarizations gives the same result as
(sum_{a=1}^2|\mathbf H\cdot\boldsymbol\epsilon_a|^2), which is tested.

Gauge invariance of the soft factor requires
(sum_k\eta_kQ_k=0). `chargeConservation` reports the sum and a Boolean.
The builder should **display the violation and suspend the claim that the
pattern is a physical, gauge-invariant scattering event**; it should not
silently change a user's charges. A massive leg produces a finite beaming
peak because (kappa>0). A true collinear pole occurs only for a null leg,
which the helpers accept away from the singular pixel.

## 6. Memory and Coulomb drift

The memory identity implemented is specifically the leading radiation-order
quantity at future null infinity,

\[
 \Delta\mathbf v_{\rm rad}^{(1/r)}(\mathbf x)
 ={1\over r}\int ds\,
 {\hat{\mathbf n}\times[(\hat{\mathbf n}-\boldsymbol\beta)
 \times\dot{\boldsymbol\beta}]\over\kappa^2}
 ={\mathbf M(\hat{\mathbf n})\over r}.
\]

`memoryKickQuadrature` evaluates the left route with composite GL8;
`memoryKickClosedForm` evaluates the endpoint route. For tanh memory only,
the exact substitution (y=h(s)) maps the infinite interval to ([0,1])
and uses (dot{\boldsymbol\beta},ds=Delta\boldsymbol\beta,dy). This is
why no tanh tail is omitted in the memory identity.

**Builder-safe sentence (two routes):** “These two numbers are the same
(1/r) radiation memory: GL8 quadrature of the retarded radiation field and
the (omega\to0) endpoint formula agree to the displayed residual; the
finite-window integral of the full electric field also contains a separate
Coulomb drift and is not being equated here.”

To print “agree to 12 digits,” the builder must compare these two functions,
use at least the tested default 16 GL8 panels, and print a relative residual.
It must not compare `memoryKickClosedForm` to a finite-window integral of
`fieldAt(...).E`.

For completeness, the regular Coulomb background has a closed antiderivative
on a uniform segment. Write (b=|\boldsymbol\beta|),
(hat{\mathbf b}=\boldsymbol\beta/b),
(mathbf x=x_\parallel\hat{\mathbf b}+\mathbf x_\perp),
(y=x_\parallel-bt), and
(D=[y^2+(1-b^2)x_\perp^2]^{1/2}). Then

\[
 \int^t\mathbf E_\beta dt=
 {1-b^2\over bD}\hat{\mathbf b}
 -{y\over b x_\perp^2D}\mathbf x_\perp.
\]

The continuous limits for (b=0) and (mathbf x_\perp=0) are implemented.
For the instant Purcell field, `coulombDrift` splits the interval at the shell
arrival (t=r), using the old primitive before and the new primitive after.
That is the exact regular-field drift. For a genuinely smooth accelerated
trajectory the velocity part during the transition has no comparable
endpoint-only closed form, so the function rejects that case rather than
mislabeling a numerical integral as closed form.

## 7. One conservation equation per angle

The angular Coulomb coefficient is

\[
 C_\beta(\hat{\mathbf n})={1-\beta^2\over
 (1-\hat{\mathbf n}\cdot\boldsymbol\beta)^2},\qquad
 E_r={C_\beta\over r^2}.
\]

The same angular dependence appears in `soft_Arxiv_update.tex` lines
541--550. The TeX normalization there is (e^2Q/(4\pi)), while this library
returns the per-unit-charge geometric coefficient.

The relevant Maxwell constraint is located at TeX lines 699--704:

\[
 \partial_uF_{ru}^{(2)}+D^AF_{uA}^{(0)}+e^2j_u^{(2)}=0.
\]

The integrated transverse soft mode is identified at lines 712--721. In the
present three-vector convention (F_{uA}^{(0)}=-rE_A), so its integrated
value is (-M_A). Direct spherical differentiation gives

\[
 D_A\left[\hat{\mathbf n}\times
 (\hat{\mathbf n}\times\mathbf h_\beta)\right]^A
 =C_\beta-1.
\]

The constants cancel between endpoints, yielding

\[
 C_f(\hat{\mathbf n})-C_i(\hat{\mathbf n})
 =D_A M^A(\hat{\mathbf n}).
\]

The kicked charge is massive and ends at timelike infinity, not future null
infinity, so (j_u^{(2)}=0) in this local (mathcal I^+) constraint. Its
Coulomb field remains in the endpoint term. If a charged null particle
crossed (mathcal I^+), the integrated (e^2j_u^{(2)}) term would have to
be restored.

`sphereDivergence` independently evaluates
((\sin\theta)^{-1}\partial_\theta(\sin\theta M_\theta)+
(\sin\theta)^{-1}\partial_\phi M_\phi) with centered five-point derivatives.
It selects a safe polar axis automatically.

**Builder-safe sentence (per angle):** “At every angle on future null
infinity, (C_f-C_i=D_AM^A): the change in the (1/r^2) Coulomb profile is
the sphere divergence of the DC transverse radiation field, not that field
itself; no null charge-flux term appears here because the kicked source is
massive.”

For context, antipodal field matching is stated at TeX lines 568--573 and in
the (F_{ru}^{(2)}=F_{rv}^{(2)}) form at lines 633--641.

## 8. Penrose and antipodal geometry

The compactification is

\[
 u=t-r,\quad v=t+r,\quad U=\arctan u,\quad V=\arctan v,
 \quad T=U+V,\quad R=V-U.
\]

For a free line (mathbf x(t)=mathbf x_0+mathbf vt), (mathbf v\ne0),
the limiting spatial directions are (-\hat{\mathbf v}) in the far past
and (+\hat{\mathbf v}) in the far future. The coordinate and antipodal
geometry in the source is described at TeX lines 598--623.

**Builder-safe sentence (antipodes):** “A nonzero straight velocity has
limiting directions (-\hat{\mathbf v}) as (t\to-\infty) and
(+\hat{\mathbf v}) as (t\to+\infty), an antipodal pair; this geometry
motivates the angular identification, but does not by itself derive the
antipodal matching condition on fields across spatial infinity.”

## Achieved residuals

Command: `node docs/outreach/auditions/prologue/em-core.test.mjs` (exit 0).
Random tests use the fixed seed `0x5eed1234`.

| Check | Achieved residual |
|---|---:|
| Position derivative | (2.147\times10^{-11}) |
| Acceleration derivative | (9.021\times10^{-12}) |
| Raised-cosine join | (1.963\times10^{-17}) |
| Tanh endpoint | (0) at binary64 precision |
| Uniform retarded time | (1.634\times10^{-13}) absolute |
| LW (E=E_{\rm vel}+E_{\rm rad}) | (0) |
| LW (B=n\times E) | (0) |
| Shell coefficient radial component | (0) |
| Uniform RK4 line straightness | (1.617\times10^{-15}) |
| Purcell flux/Jacobian identity | (8.882\times10^{-16}) |
| Instant spectrum plateau/formula | (4.066\times10^{-20}) absolute |
| Classical soft vs Weinberg factor | (1.110\times10^{-16}) |
| Instant photon-number logarithm | (3.795\times10^{-19}) |
| Polarization sum | (0) |
| Random two-route memory (30 cases) | (1.204\times10^{-15}) relative |
| Boosted-Coulomb radial profile | (2.498\times10^{-16}) absolute |
| Analytic angular ledger | (5.551\times10^{-17}) |
| Numerical five-point sphere divergence | (1.417\times10^{-11}) absolute |
| Penrose tan map | (3.553\times10^{-15}) |
| Free-particle antipodes | (0) |

Tau-to-zero field-line convergence:

| (	au) | Max inner/outer tangent residual |
|---:|---:|
| 0.200000 | (1.522\times10^{-2}) |
| 0.050000 | (3.798\times10^{-3}) |
| 0.012500 | (9.491\times10^{-4}) |
| 0.003125 | (2.373\times10^{-4}) |

Radiation-spectrum GL8 convergence (reference: 64 panels):

| Panels | Absolute residual |
|---:|---:|
| 1 | (1.549\times10^{-11}) |
| 2 | (3.045\times10^{-16}) |
| 4 | (2.541\times10^{-21}) |
| 8 | (5.082\times10^{-21}) |
| 16 | (2.965\times10^{-21}) |

Photon-number log-GL8 convergence (reference: 40 panels):

| Panels | Absolute residual |
|---:|---:|
| 2 | (4.678\times10^{-13}) |
| 4 | (3.646\times10^{-16}) |
| 8 | (0) at binary64 precision |
| 16 | (0) at binary64 precision |
| 24 | (1.084\times10^{-19}) |

Memory GL8 convergence:

| Panels | Relative residual |
|---:|---:|
| 1 | (1.119\times10^{-11}) |
| 2 | (1.980\times10^{-16}) |
| 4 | (1.948\times10^{-16}) |
| 8 | (2.113\times10^{-16}) |
| 16 | (2.362\times10^{-16}) |

Coulomb-drift validation GL8 convergence:

| Panels | Relative residual |
|---:|---:|
| 1 | (5.646\times10^{-11}) |
| 2 | (9.065\times10^{-16}) |
| 4 | (4.268\times10^{-16}) |
| 8 | (2.666\times10^{-16}) |
| 16 | (5.655\times10^{-16}) |

## Things the page must not say

- Do not say “the DC field is the whole time integral of (E).” The soft/DC
  identity is the leading (1/r) transverse radiation integral. A finite
  window of the full field includes Coulomb drift.
- Do not say “the Coulomb-profile difference equals the DC radiation field.”
  It equals the **sphere divergence** of that transverse field.
- Do not print an unregulated instantaneous-shell (E_\perp/E_r) as a finite
  number. The transverse field is a delta distribution; show its integrated
  coefficient, name a shell thickness, or use a smooth kick.
- Do not call the great-circle shell connector a uniquely observable field
  line. Only the endpoint flux map is invariant in the zero-thickness model.
- Do not call `tanh` compactly supported or claim that its `tau` is an exact
  start-to-finish duration.
- Do not claim every massive hard particle creates a literal angular pole.
  Subluminal legs create finite beaming peaks; collinear poles require null
  legs.
- Do not present a charge-nonconserving `spherePattern` as a gauge-invariant
  scattering event merely because the function can display it.
- Do not say the elementary straight-line antipode argument derives the
  field matching condition. It illustrates only the geometry.
- Do not multiply field/memory output by (alpha/(4pi^2)). That prefactor
  belongs to spectrum and photon number under the conventions above.

## End report

Verified: all eight numbered capabilities, the analytic trajectory joins,
uniform-motion retarded time, the LW split, the distributional shell
coefficient, RK4 behavior and the (	au\to0) limit, exact flux-label
Jacobian, instantaneous spectral plateau, smooth spectral and photon-number
quadratures, the classical/Weinberg single-emitter identity, polarization
completeness, charge checking including null legs, 30 fixed-seed random
memory identities, the closed Coulomb drift, the boosted Coulomb angular
profile, the analytic and independently differentiated per-angle ledger, and
Penrose/antipodal geometry. The final harness exits zero.

Could not honestly turn two distributional/asymptotic statements into the
finite ordinary quantities suggested by the parent brief. First, an ideal
instantaneous shell has no regulator-independent finite transverse/radial
ratio or unique connector curve; the library supplies the exact delta
coefficient and flux-matched endpoints. Second, the exact two-route soft
memory identity concerns the (1/r) radiation coefficient, not the complete
finite-radius, finite-window integral of (E). The regular Coulomb part is
therefore separate. Also, a closed endpoint formula for Coulomb drift during
a general smooth acceleration does not exist in the form requested;
`coulombDrift` is exact for the instantaneous Purcell construction (and for
uniform motion) and rejects a nontrivial smooth kick.

The imprecise statements in `BRIEF-why-prologue.md` should be repaired before
publication: W6's “DC field component” must be qualified as the leading
transverse radiation component; W7's claim that the Coulomb-profile change
“equals the DC radiation content” must say **sphere divergence**; W2's shell
ratio requires a regulator or smooth (	au); and W4's “every hard particle
drags its own pole” is literally true only for null hard legs, while massive
legs produce finite peaks. These are physics qualifications, not numerical
limitations.
