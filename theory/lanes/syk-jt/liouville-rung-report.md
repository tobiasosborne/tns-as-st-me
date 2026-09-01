# Large-p Liouville rung: what survives beyond the Schwarzian truncation

**Incremental status.**  COMPLETE.  The report was written as a standalone
partial deliverable after every section.  No numerical code is used.

## 0. Outcome and status register

The local corpus fixes the equilibrium large-p Liouville saddle and its
Schwarzian limit, but it does **not** fix the collective-field source or the
real-time contour boundary data for the prescribed right-dot pulse.  Net
right-energy balance is one scalar condition; it does not determine those data.
Consequently the requested truncation-lifting response is not a well-posed
computation from the stated inputs.  The honest rung outcome is therefore:

| question | strict leading large-p Liouville ruling | controlled statement |
|:--|:--|:--|
| Q1: calibrated plateau and DC identity | **HOLD / underdetermined** | The Schwarzian result is recovered as \(\delta v=1-v\to0\) in the separated soft window.  The full finite-\(v\) response needs the omitted source projection onto the finite-\(v\) soft eigenfunction and all hard modes. |
| Q2: first correction | **ORDER IDENTIFIED; coefficient and fate OPEN** | Lifting the Schwarzian truncation at leading large \(p\) starts relatively at \(\delta v=2/(\beta\mathcal J)+O((\beta\mathcal J)^{-2})\), before the independent \(1/p\) observable correction and the \(p^2/N\) saddle-loop correction.  The local source explicitly leaves finite-\(v\) soft/hard mixing unresolved. |
| Q3: butterfly register | **HOLD beyond the matching window** | In the \(\delta v\to0\) Schwarzian window the zero plateau and exponential transient of `JT-bfly-decay` are recovered.  At finite \(v\), the pure horizon translation does not determine a boundary-condition-preserving, sourced two-dot saddle, so there is no unique full-Liouville continuation whose late tail could be adjudicated. |

This does not downgrade any of `JT-B-susc`, `JT-bfly-decay`, or
`JT-noplat-abs`: all three rows are explicitly Schwarzian-EFT statements.  It
also does not promote a Liouville-level echo.  The result of this rung is the
precise missing datum and the order at which it first matters.

## 1. Conventions, algebra, and the equilibrium Liouville saddle

### 1.1 Operational and limit conventions

⟨1⟩1. **ASSUME (allowed algebra and protocol comparison).**  The detector is
the Layer-1 uniform, parity-even mixed bilocal

\[
 B_{LR}(t_1,t_2)=-{i\over N}\sum_{j=1}^{N}
 \psi_j^L(t_1)\psi_j^R(t_2),
 \tag{L.1}
\]

together with the separately measured \((E_L,E_R)\).  Pulsed and reference
preparations are comparable only when those exactly conserved final energies
agree.  The collective field is bookkeeping; only the expectation of (L.1)
is a detector.  This is exactly Layer 1 of
`theory/lanes/syk-jt/observables-spec.md` and the comparability clause of D33.

⟨1⟩2. **ASSUME (one synchronization event).**  A single event \(u_*\) fixes
the early two-sided clock convention.  No late resynchronization is allowed.
The claim-bearing pulse is compact, right-sided, and energy-balanced,
\(\Delta E_R=0\) at the declared response order; the comparator has the same
measured \((E_L,E_R)\).  This is the retained protocol of
`t1-analytic.md` ⟨1⟩1–⟨1⟩3 and claim `JT-B-susc`.

⟨1⟩3. **ASSUME (ordered limits).**  First take \(N\to\infty\), then
\(p\to\infty\) with

\[
 \lambda={2p^2\over N}\longrightarrow0,
 \tag{L.2}
\]

then use the large-\(C\)-first detector window

\[
 1\ll \kappa(T-u_*)\ll \kappa C,
 \qquad \kappa={2\pi\over\beta},
 \qquad C={N\over4p^2\mathcal J}.
 \tag{L.3}
\]

The first two limits and (L.2) are printed in
`refs/arxiv-2412.14799/Main.tex:149-154`; the stiffness follows from its
\(\alpha_S=1/(4p^2)\) at lines 59–68 and the physical-time Schwarzian
coefficient at lines 141–146.  In the inherited thermal-circle convention,
\(C_{\rm th}=C/\beta=N/(4p^2\beta\mathcal J)\), which is the map stated in
`theory/lanes/syk-jt/t1-analytic.md` (4.15).  The last ordering is the binding D33/
observable-spec convention.  At any finite large \(p\), the displayed
observable expansion below adds the overlap condition

\[
 \kappa(T-u_*)\ll p.
 \tag{L.4}
\]

Thus a finite-parameter realization of the rung requires
\(1\ll\kappa(T-u_*)\ll\min(\kappa C,p)\).  Equation (L.4) is the named
uniformity condition \(|g|/p\ll1\) applied to (L.12) below; taking \(p\to
\infty\) before the late limit makes it compatible with (L.3).

### 1.2 One-dot collective field and normalization

⟨1⟩4. **PROVE (leading large-p action and equation).**  In Euclidean
time define

\[
 G(\tau_1,\tau_2)={\operatorname{sgn}(\tau_1-\tau_2)\over2}
 \left[1+{g(\tau_1,\tau_2)\over p}+O(p^{-2})\right].
 \tag{L.5}
\]

The leading collective action is

\[
 I[g]={N\over4p^2}\int d\tau_1d\tau_2
 \left[-\mathcal J^2e^g+{1\over4}\partial_1g\,\partial_2g\right],
 \tag{L.6}
\]

with \(g(\tau,\tau)=0\), symmetry in its arguments, and the KMS
identifications.  Varying (L.6) and integrating both kinetic derivatives by
parts gives

\[
 \partial_1\partial_2g=-2\mathcal J^2e^g.
 \tag{L.7}
\]

Equations (L.5)–(L.6), including the boundary data, are printed at
`Main.tex:149-161`; (L.7) is the named Euler–Lagrange computation from
(L.6).  The two-time general solution is locally a pair of one-variable
functions modulo a common \(SL(2,\mathbb R)\):

\[
 e^{g(\tau_1,\tau_2)}=
 {h_1'(\tau_1)h_2'(\tau_2)\over
  \mathcal J^2[h_1(\tau_1)-h_2(\tau_2)]^2}.
 \tag{L.8}
\]

This normalization and the fact that boundary conditions determine the
functions are printed for the two-dot collective matrix in
`refs/arxiv-1804.00491/GlobalAdSDraftRevisedSubmitted.tex:1871-1889`.

⟨1⟩5. **PROVE (thermal saddle and the finite-coupling parameter).**  The
translation-invariant solution is

\[
 e^{g_*(\tau_1,\tau_2)}=
 \left\{{\cos(\pi v/2)\over
 \cos\!\left[\pi v\left({1\over2}-{|\tau_1-\tau_2|\over\beta}\right)\right]}
 \right\}^{\!2},
 \qquad
 \beta\mathcal J={\pi v\over\cos(\pi v/2)}.
 \tag{L.9}
\]

This is `Main.tex:162-170`.  Put \(v=1-\delta v\).  Expanding the second
relation at small \(\delta v\) gives

\[
 \delta v={2\over\beta\mathcal J}
 +O((\beta\mathcal J)^{-2}).
 \tag{L.10}
\]

This is a named Taylor inversion of the displayed equation (L.9), not a
matching assumption.

### 1.3 Two dots, the Layer-1 equal-time grid, and the Schwarzian map

⟨1⟩6. **ASSUME (decoupled post-pulse dynamics).**  The TFD prepares two
dots with the same disorder realization.  During the claim-bearing operation
only the right collective action is sourced; after its compact support the
action is \(I[g_L]+I[g_R]\).  No interdot Hamiltonian remains, so \(E_L\)
and \(E_R\) are separately conserved as required by ⟨1⟩1.  A bilinear
interdot coupling is useful for deriving the matrix Liouville action, but it
would impose a different diagonal boundary condition and is not silently
substituted for this protocol.  The coupled action and its source-dependent
boundary condition are printed at
`GlobalAdSDraftRevisedSubmitted.tex:1471-1483,2747-2761`.

⟨1⟩7. **PROVE (exact leading large-p equilibrium detector).**  Continue
the thermal saddle (L.9) through the half-circle separation that constructs
the TFD, and put equal Lorentzian detector times \(t_L=t_R=T-u_*\).  The
Hermitian representative (L.1) is

\[
 B^{\rm eq}_{LR}(T)=\frac12\left[1+{g^{\rm eq}_{LR}(T)\over p}
 +O(p^{-2})\right],
 \tag{L.11}
\]

\[
 g^{\rm eq}_{LR}(T)=2\log\cos{\pi v\over2}
 -2\log\cosh[v\kappa(T-u_*)],
 \qquad
 \partial_Tg^{\rm eq}_{LR}=-2v\kappa\tanh[v\kappa(T-u_*)].
 \tag{L.12}
\]

The continuation is also printed, in equivalent \(q=p\) notation, at
`GlobalAdSDraftRevisedSubmitted.tex:2769-2790`; (L.12) is the named
half-circle analytic continuation and differentiation of (L.9).  As
\(v\to1\), exponentiating the leading term gives
\(B_{LR}^{\rm eq}\propto\cosh^{-2/p}[\kappa(T-u_*)]\), precisely the
Schwarzian primary kernel with \(\Delta=1/p\).  No detector normalization is
fitted.

⟨1⟩8. **PROVE (large-p calibrated ratio).**  For a pulsed solution
write \(\delta g_{LR}=g^{\rm pulse}_{LR}-g^{\rm eq}_{LR}\).  From
(L.11),

\[
 \delta B_{LR}={\delta g_{LR}\over2p}+O(p^{-2}),\qquad
 \boxed{\quad
 \Delta u_{\rm rel}(T)=-{\delta B_{LR}\over\partial_TB^{\rm eq}_{LR}}
 =-{\delta g_{LR}(T,T)\over\partial_Tg^{\rm eq}_{LR}(T)}+O(p^{-1}).
 \quad}
 \tag{L.13}
\]

The same fixed phase multiplies numerator and denominator, so (L.13) is the
brief's Layer-1 detector.  It is finite in the strict ordered large-\(p\)
limit even though both uncalibrated changes are \(O(1/p)\).  This is direct
order counting from (L.11), and its operational status is D33.

**QED (equilibrium setup).**  Equations (L.5)–(L.13) fix the normalization,
known saddle, two-sided equal-time grid, Schwarzian matching, and allowed
detector without treating \(g\) or a frame label as an observable.  □

## 2. The pulse is not a determined Liouville boundary-value problem

### 2.1 What a microscopic pulse must specify

⟨1⟩9. **ASSUME (general collective source).**  A microscopic right-dot
operation has the form

\[
 H_R(t)=H_R+j(t){\cal O}_R,
 \qquad \operatorname{supp}j\subset[u_i,u_f],
 \tag{L.14}
\]

with a named parity-even operator \({\cal O}_R\).  After disorder averaging
on a Schwinger–Keldysh contour it produces a definite source functional
\(I_{\rm src}^{({\cal O},j)}[G_{ab},\Sigma_{ab}]\), contour gluing, and initial
data.  Denote its leading forcing of the large-\(p\) equation by
\({\mathfrak s}_{ab}(t_1,t_2)\).  The sourced equation schematically is

\[
 \partial_1\partial_2g_{ab}
 +2\sigma_{ab}\mathcal J^2e^{g_{ab}}
 =\mathfrak s_{ab},
 \tag{L.15}
\]

where the contour/sign matrix \(\sigma_{ab}\) and the matching data are fixed
by the operator and contour, not by the equilibrium action.  The explicit
two-dot example in
`refs/arxiv-1804.00491/GlobalAdSDraftRevisedSubmitted.tex:1842-1889`
shows this dependence: a time-dependent bilinear coupling appears as a local
self-energy source and changes the diagonal condition on \(g_{LR}\); the
four functions in the general Liouville solution are then determined by all
boundary data.

⟨1⟩10. **PROVE (the Schwarzian power profile is not that datum).**  The
settled EFT pulse supplies

\[
 P(t)={dE_R\over dt},\qquad
 \int_{u_i}^{u_f}P(t)dt=0,qquad
 M_1=\int_{u_i}^{u_f}(t-u_*)P(t)dt.
 \tag{L.16}
\]

It does not name \({\cal O}_R\), \(j(t)\), a contour source
\(I_{\rm src}\), or the two-time function \(\mathfrak s_{ab}\).  Equation
(L.16) constrains one zero-frequency energy functional and records one first
moment; equation (L.15) requires a function of two times plus contour and
matching data.  Therefore the map

\[
 (P,\ \int P=0)\ \not\Longrightarrow\
 (\mathfrak s_{ab},\text{ retarded contour data})
 \tag{L.17}
\]

is not defined.  This is a named domain/codomain determination check using
(L.14)–(L.16), not an assertion that a difficult equation lacks a solution.

⟨1⟩11. **PROVE (energy balance does not repair the omission).**  At
linear response, \(\Delta E_R\) is a single linear functional
\(L_E[\mathfrak s]\).  If \(L_E\ne0\), its balanced kernel has codimension
one in the infinite-dimensional source space; if \(L_E=0\) at first order,
every linearized source is balanced.  In either case there exist distinct
forcings with the same \(\Delta E_R=0\) and the same chosen synchronization
event.  A modulation of the random \(p\)-body coupling changes the Liouville
potential at two times, whereas a bilinear source enters the bare inverse
propagator and produces a local self-energy/boundary jump (the latter
mechanism is displayed at
`GlobalAdSDraftRevisedSubmitted.tex:1846-1855,1880-1889`).  Those forcings
are inequivalent even when their one scalar final-energy changes agree.
Hence D33 comparability is necessary but not sufficient to select a pulsed
saddle.  □

### 2.2 Linearized full-Liouville response and the missing projections

⟨1⟩12. **PROVE (response equation).**  Put
\(g=g_*+\phi\) in (L.15).  To first order,

\[
 {\cal L}_v\phi_{ab}:=
 \left(\partial_1\partial_2+2\sigma_{ab}\mathcal J^2e^{g_*}\right)
 \phi_{ab}=\mathfrak s_{ab},
 \qquad
 \delta g_{LR}(T,T)=
 \left[({\cal L}_v^{-1})_{\rm ret}\mathfrak s\right]_{LR}(T,T).
 \tag{L.18}
\]

This is the named Fréchet linearization of (L.15).  It displays all three
objects needed by (L.13): the forcing, the retarded inverse (including
contour conditions), and its equal-time mixed component.  None is fixed by
(L.16).

⟨1⟩13. **PROVE (finite-\(v\) mode content).**  Around the finite-\(v\)
thermal saddle, the local source describes separated modes
\(\psi_m(\delta\tau)e^{-in\bar\tau}\) with eigenvalue proportional to
\(n^2-m^2\).  The softest root obeys

\[
 m(n)=n[1-\delta v+O(\delta v^2)],
 \tag{L.19}
\]

while the remaining directions are hard.  This is printed in
`refs/arxiv-2412.14799/Main.tex:427` (the note and its footnote).  Expanding
the forcing gives coefficients

\[
 c_m(n)=\int d\delta\tau\,
 \psi_m^*(\delta\tau)\,\mathfrak s_n(\delta\tau).
 \tag{L.20}
\]

Energy balance can constrain a particular zero-frequency energy projection;
it fixes neither the finite-\(v\) soft coefficient nor the hard coefficients
in (L.20).  The desired \(\delta g_{LR}(T,T)\), including its zero-frequency
residue, therefore cannot be evaluated from \(M_1\) alone.  This is the named
spectral projection of (L.18) using the source's mode statement (L.19).

### 2.3 What Bucca–Mezei actually embed

⟨1⟩14. **PROVE (scope of the quoted embedding).**  With conformal ZZ
boundary conditions, Bucca–Mezei give the reparametrized saddle family

\[
 e^{\gamma^{(f)}}={f'(\tau_1)f'(\tau_2)\over
 \sin^2([f(\tau_1)-f(\tau_2)]/2)}.
 \tag{L.21}
\]

Evaluating the displacement operator on this family yields

\[
 I_{\rm soft}[f]=-{N\pi\delta v\over4p^2}
 \int d\bar\tau\,
 \operatorname{Sch}[\tan(f/2),\bar\tau],
 \tag{L.22}
\]

with \(1/\mathcal J=\pi\delta v+O(\delta v^2)\) in their \(\beta=2\pi\)
units.  These are exactly `refs/arxiv-2412.14799/Main.tex:291-309`.  Their
concluding scope sentence says that the orthogonal "hard directions" have
action \(O(N/p^2)\), whereas the soft action is smaller by \(\delta v\)
(`Main.tex:311`).  Thus (L.22) is an evaluation on the soft family, not a
solution of (L.18) for an arbitrary real-time source.

⟨1⟩15. **PROVE (the omitted effect is the requested effect).**  The
finite-\(v\), boundary-condition-preserving field configuration used for the
second derivation is an Ansatz.  The source states that it is accurate at
linear order in the \(v\to1\) reparametrization, that finite-\(v\) soft/hard
mixing can start at \(O(\delta v)\), and that checking its nonlinear zero-mode
direction is left for future work
(`refs/arxiv-2412.14799/Main.tex:411-427`).  Since Q1 asks precisely for the
terms obtained by lifting this soft-family restriction, inserting (L.21) or
that Ansatz into the Schwarzian result would assume the conclusion.  It is
not a full-Liouville derivation.

**QED (well-posedness obstruction).**  The data in the brief determine the
equilibrium operator \({\cal L}_v\), the scalar energy-balance condition, and
the soft limiting action.  They do not determine the forcing and contour data
needed on the right side of (L.18), and the cited embedding explicitly leaves
the relevant finite-\(v\) mixing unresolved.  Q1–Q3 therefore have no unique
strict-Liouville answer without an additional microscopic source
specification.  □

## 3. Q1 — conditional survival theorem and the scale-separation failure

### 3.1 What would be sufficient for a plateau

⟨1⟩16. **ASSUME (a completed microscopic problem and phase relaxation).**
For this subsection only, supplement the brief by specifying
\((\mathcal O_R,j)\), its Schwinger–Keldysh source, and retarded initial data.
Assume the resulting linearized solution has, after the pulse and within
(L.3)–(L.4),

\[
 g^{\rm pulse}_{LR}(T,T)=
 g^{\rm eq}_{LR}(T-\sigma,T-\sigma)+r(T),
 \qquad r(T),\ \partial_T r(T)\longrightarrow0,
 \tag{L.23}
\]

where \(\sigma=O(j)\).  Equation (L.23) is a dynamical relaxation hypothesis,
not a consequence of energy balance.  It is displayed so that the exact
missing condition is auditable.

⟨1⟩17. **PROVE (conditional plateau).**  Taylor expansion of (L.23)
and substitution in (L.13) give

\[
 \delta g_{LR}(T,T)=-\sigma\,\partial_Tg^{\rm eq}_{LR}(T)+r(T)+O(j^2),
 \qquad
 \Delta u_{\rm rel}(T)=\sigma-
 {r(T)\over\partial_Tg^{\rm eq}_{LR}(T)}+O(j^2,p^{-1}).
 \tag{L.24}
\]

Since (L.12) has
\(\partial_Tg^{\rm eq}_{LR}\to-2v\kappa\ne0\),

\[
 \boxed{\lim\Delta u_{\rm rel}=\sigma}
 \tag{L.25}
\]

at leading large \(p\), provided (L.23) holds.  This is a named Taylor and
late-limit computation from (L.12)–(L.13), and is a conditional D33
susceptibility rather than D32 memory.

⟨1⟩18. **PROVE (conditional DC identity).**  Extend the post-pulse
readout retardedly by \(\delta u_{\rm rel}(t)=0\) before the operation.  If the
remainder in (L.24) is integrable after subtracting the step, the elementary
final-value theorem gives

\[
 \lim_{T\to\text{late}}\Delta u_{\rm rel}(T)
 =\lim_{\omega\to0}[-i\omega\,
 \widetilde{\Delta u}_{\rm rel}(\omega)]=\sigma.
 \tag{L.26}
\]

Thus equality of a plateau with the DC residue of the **same full bilocal
response** is automatic once the plateau and retarded regularity exist.  What
is dynamical, and what D33 additionally demands, is the existence and
nonzero value of \(\sigma\) and its normalization by the measured pulse with
nothing fitted.  Those require the missing projections (L.20).  Equation
(L.26) therefore cannot be used to infer (L.23).

### 3.2 Recovery of `JT-B-susc`, and where the derivation stops

⟨1⟩19. **PROVE (Schwarzian matching window).**  In the joint limit
\(\delta v\to0\) at fixed, contact-separated bilocal arguments, the
finite-coupling saddle approaches the reparametrized ZZ family (L.21).  The
boundary-condition-preserving Ansatz has

\[
 e^{\gamma_f}=e^{\gamma_*}
 \left[1+{\delta\tau^2\over6}
 \operatorname{Sch}[\tan(f/2),\bar\tau]+O(\delta\tau^3)\right]
 \quad (\delta\tau\gg\delta v),
 \tag{L.27}
\]

as printed at `refs/arxiv-2412.14799/Main.tex:416-423`.  Evaluating the action
gives (L.22), with the stiffness in (L.3).  Hence the already adjudicated
one-soft result is recovered:

\[
 \sigma_{\rm Sch}={1\over2C\kappa^2}
 \int_{u_i}^{u_f}(t-u_*)P(t)dt+O(C^{-2}),
 \tag{L.28}
\]

and (L.26) becomes claim `JT-B-susc` in its accepted scope.  This is a named
EFT matching using (L.22), (L.27), and the proved Schwarzian response
`t1-analytic.md` (4.9), (4.13).

⟨1⟩20. **PROVE (finite-\(v\) remainder is not fixed).**  At the next
order the most that follows from the corpus is the schematic expansion

\[
 \kappa\sigma=\kappa\sigma_{\rm Sch}
 +\delta v\,\mathcal F_1[\mathfrak s_{ab};\text{contour}]
 +O(\delta v^2)+O(p^{-1})+O(p^2/N)+O((\kappa C)^{-2}),
 \tag{L.29}
\]

where \(\mathcal F_1\) contains the correction to the finite-\(v\) soft
eigenfunction and its source overlap, plus soft/hard mixing.  Equations
(L.19)–(L.20) prove that this functional depends on data not contained in
\(P\) or \(M_1\); `Main.tex:411-427` confirms that the relevant mixing is not
computed in the cited embedding.  No sign, coefficient, or late-time
relaxation law for \(\mathcal F_1\) may therefore be assigned.  In particular,
(L.29) does **not** prove drift, decay, or preservation.

### 3.3 The absolute detector has a second, non-overlapping late scale

⟨1⟩21. **ASSUME [physical argument] (standard exponential
reorganization).**  For diagnosing the absolute correlator only, reorganize
the known leading large-\(p\) saddle as

\[
 B^{\rm eq}_{LR}(T)\simeq {1\over2}
 \left[{\cos(\pi v/2)\over
 \cosh[v\kappa(T-u_*)]}\right]^{2/p}.
 \tag{L.30}
\]

Its expansion reproduces (L.11)–(L.12).  The analogous exponential
reorganization is used at
`refs/arxiv-1804.00491/GlobalAdSDraftRevisedSubmitted.tex:1539-1547`, whose
footnote explicitly cautions that only the first \(1/p\) term is directly
controlled.  Accordingly, no all-orders theorem is attached to (L.30).

⟨1⟩22. **PROVE [physical argument] (conditional absolute decay).**  If
(L.23) holds, then at linear order

\[
 \delta B_{LR}(T)=-\sigma\partial_TB^{\rm eq}_{LR}(T)+o(\partial_TB^{\rm eq})
 \sim {\sigma v\kappa\over p}
 \left[2\cos{\pi v\over2}\right]^{2/p}
 e^{-2v\kappa(T-u_*)/p}.
 \tag{L.31}
\]

At every fixed finite \(p\), the reorganized expression has no nonzero
absolute plateau, consistent in shape with `JT-noplat-abs`.  But its decay
time is

\[
 T_{\rm abs}\sim {p\over2v\kappa}.
 \tag{L.32}
\]

Reaching \(T\gg T_{\rm abs}\) violates the leading-expansion control
condition (L.4).  Conversely, in the controlled coefficient window
\(1\ll\kappa(T-u_*)\ll p\), (L.31) is approximately a constant of order
\(1/p\), while the strict \(p\to\infty\) absolute difference vanishes.  The
limits do not commute:

\[
 \lim_{p\to\infty}\lim_{T/p\to\infty}\delta B_{LR}=0,
 \qquad
 \lim_{T/p\to0}p\,\delta B_{LR}=\sigma v\kappa
 \quad\text{under (L.23)}.
 \tag{L.33}
\]

Thus the leading Liouville rung does not furnish a controlled late-time test
of the fixed-\(\Delta>0\) absolute-decay row.  This is a parametric window
non-overlap, analogous in logic (not in mechanism) to the ED rung's
\(1\ll\beta J\ll N_m\) failure.

⟨1⟩23. **PROVE [physical argument] (sample cost).**  A bounded
single-shot estimator of (L.1) has \(O(1)\) variance.  Resolving the ratio
(L.13) to fixed absolute error \(\eta\) requires resolving \(\delta B\) at
scale \(\eta|\partial_TB^{\rm eq}|\).  Equation (L.30) gives

\[
 M_{\rm shots}=O\!\left(
 {p^2\over(v\kappa\eta)^2}
 e^{4v\kappa(T-u_*)/p}
 \right),
 \tag{L.34}
\]

up to the fixed thermal normalization and protocol-dependent variance.
This is D33's required cost statement.  It diverges at least as \(p^2\) in
the strict large-\(p\) sequence, so (L.13) is an allowed finite-parameter
functional but not a practically permanent record.

**Q1 VERDICT.**  The Schwarzian plateau and its normalized DC identity are
recovered from the full collective action only in the controlled
\(\delta v\to0\) matching described by (L.27)–(L.28).  At finite \(v\), a
plateau would survive under the explicit relaxation hypothesis (L.23), and
then its equality to the DC residue of the same response follows by (L.26).
The local inputs neither prove (L.23) nor determine its coefficient because
the pulse forcing and the projections (L.20) are absent.  Q1 is therefore
**HOLD**, not YES or NO.  Independently, the absolute-decay scale lies outside
the controlled leading-\(1/p\) late window.  **QED.**  □

## 4. Q2 — correction order and ordered limits

⟨1⟩24. **PROVE (hierarchy in the collective action).**  The hard
Liouville directions carry action

\[
 I_{\rm hard}=O(N/p^2),
 \tag{L.35}
\]

whereas the soft-family action (L.22) is

\[
 I_{\rm soft}=O(N\delta v/p^2).
 \tag{L.36}
\]

Bucca–Mezei state (L.35) at `Main.tex:311` and derive (L.36) at
`Main.tex:291-309`.  Their finite-\(v\) eigenfunction differs from the
conformal reparametrization by (L.19), and their Ansatz analysis bounds the
unresolved mixing at order \(\delta v\) (`Main.tex:411-427`).  Therefore the
first correction that **lifts the Schwarzian truncation while retaining the
leading large-\(p\) collective theory** is relative order

\[
 \boxed{\epsilon_{\rm lift}=\delta v
 ={2\over\beta\mathcal J}+O((\beta\mathcal J)^{-2}).}
 \tag{L.37}
\]

It is not a \(1/p\) correction: (L.37) changes the saddle and mode shape
already in the coefficient \(g\) retained at order \(1/p\) in (L.5).

⟨1⟩25. **PROVE (independent correction parameters).**  The next
expansions answer different questions:

| parameter | origin | effect on this rung |
|:--|:--|:--|
| \(\delta v\sim(\beta\mathcal J)^{-1}\) | finite-coupling boundary condition inside leading Liouville theory | first Schwarzian-truncation-lifting correction; unknown functional (L.29) |
| \(1/p\) | terms beyond (L.5) in the microscopic bilocal | correction to the calibrated ratio and control of the \(T\sim p/\kappa\) absolute tail |
| \(p^2/N\) | inverse saddle stiffness \(N/p^2\) | collective-field loops; removed by (L.2) before the detector limit |
| \(1/C\) at fixed pulse scaling | Schwarzian loops/nonlinear multi-soft response | separate from finite-\(v\) hard-mode mixing; `JT-B-susc` retains only its declared \(O(C^{-1})\) response |

This table is direct order counting from (L.2), (L.5), and (L.35)–(L.37).
Unless a hierarchy between \(\delta v\), \(1/p\), and \(p^2/N\) is declared,
the phrase "first correction" is ambiguous.  For this brief the intended
truncation lift selects the first row.

⟨1⟩26. **ASSUME (ordering used for the ruling).**  Use

\[
 N\to\infty
 \ \prec\ p\to\infty\ (p^2/N\to0,\ C\to\infty)
 \ \prec\ \delta v\downarrow0\text{ expansion}
 \ \prec\ \kappa(T-u_*)\to\infty,
 \tag{L.38}
\]

with \((T-u_*)/C\to0\) and, for a finite-\(p\) approximant,
\(\kappa(T-u_*)/p\to0\).  Here \(C\to\infty\) is achieved through
\(N/p^2\to\infty\) at fixed \(\mathcal J\); it is taken before the detector
time exactly as demanded by the observable spec.  One may keep a small fixed
\(\delta v\) after the first three limits to define the Liouville correction,
then expand it.  Thus (L.38) is compatible with, rather than a replacement
for, the campaign's \(C\)-first convention.

⟨1⟩27. **PROVE (the known kinematic correction).**  Even before a
pulse is specified, (L.12) shows that finite coupling changes the equilibrium
clock rate as

\[
 \kappa\longmapsto v\kappa
 =\kappa\left[1-{2\over\beta\mathcal J}
 +O((\beta\mathcal J)^{-2})\right].
 \tag{L.39}
\]

This correction must appear in the calibration denominator.  It changes the
approach scale but, by itself, neither creates nor destroys the constant
\(\sigma\) in the conditional theorem (L.25).

⟨1⟩28. **PROVE (no licensed erosion verdict).**  Drift, decay, or
preservation is a statement about the retarded spectrum and source overlaps
in (L.18).  The cited Liouville source gives Euclidean saddle modes and their
action, but no retarded Schwinger–Keldysh solution for (L.14), no damping law
for the hard projections, and no coefficient \(\mathcal F_1\).  A
conservative classical Liouville continuation may retain oscillatory hard
components, while a correctly completed large-\(N\) retarded problem may
dephase them; choosing either without contour data would be an extra physical
assumption.  Therefore Q2 identifies (L.37) as the leading correction but
must classify its effect on the plateau as **OPEN**.

**Q2 VERDICT.**  The first truncation-lifting parameter is
\(1/(\beta\mathcal J)\), equivalently \(\delta v\), in the ordering (L.38).
The calculable equilibrium effect is the rate change (L.39).  The correction
to the pulse plateau and its fate are source- and contour-dependent and are
not determined by the local inputs.  **QED.**  □

## 5. Q3 — the butterfly register

⟨1⟩29. **PROVE (Schwarzian endpoint).**  In the conformal soft chart
put

\[
 g_{\rm shock}=\begin{pmatrix}1&\alpha\\0&1\end{pmatrix},
 \qquad x=e^{\kappa(T-u_*)},
 \qquad D_{\rm shock}=x+x^{-1}+\alpha.
 \tag{L.40}
\]

The exact Schwarzian equal-time readout gives

\[
 \Delta u_{\rm shock}(T)
 =-\alpha\kappa^{-1}e^{-\kappa(T-u_*)}
 +O(e^{-2\kappa(T-u_*)}),
 \tag{L.41}
\]

so its plateau is zero.  This is claim `JT-bfly-decay`, proved at
`theory/lanes/syk-jt/t1-analytic.md` (3.14)–(3.15) and matched to the local
Shenker–Stanford geodesic at
`refs/arxiv-1306.0622/shock.tex:188-234`.

⟨1⟩30. **PROVE [physical argument] (formal finite-\(v\) diagnostic).**
If one merely replaces the equilibrium exponential in (L.40) by its exact
leading-large-\(p\) rate, \(x_v=e^{v\kappa(T-u_*)}\), while retaining the
same parabolic matrix, the same algebra gives

\[
 \Delta u_{\rm shock}^{\rm formal}(T)
 =-\frac{\alpha}{v\kappa}e^{-v\kappa(T-u_*)}
 +O(e^{-2v\kappa(T-u_*)}),
 \tag{L.42}
\]

and the reorganized fundamental bilocal has

\[
 \delta B_{LR}^{\rm formal}
 =O\!\left({\alpha\over p}
 e^{-(1+2/p)v\kappa(T-u_*)}\right).
 \tag{L.43}
\]

Thus the naive continuation has no plateau and its first kinematic correction
is exactly the rate renormalization (L.39).  Equations (L.42)–(L.43) are
named large-\(x_v\) expansions; their `formal` label is load-bearing.

⟨1⟩31. **PROVE (why the diagnostic is not the requested lift).**  The
finite-\(v\) reparametrized one-dot saddle
`refs/arxiv-2412.14799/Main.tex:327-346` violates the microscopic
non-conformal boundary condition before an additional correction is made.
The corrected configuration is an Ansatz whose finite-\(v\) soft/hard mixing
is unresolved (`Main.tex:411-427`).  Moreover, that one-dot construction
does not provide the two-dot Schwinger–Keldysh source that physically creates
a **relative** parabolic transformation while returning \((E_L,E_R)\) to the
reference values.  The bulk label (L.40) alone therefore does not select a
solution of (L.18).  Promoting (L.42) would repeat the truncation the brief
asks this rung to lift.

⟨1⟩32. **PROVE (no evidence for a major reversal).**  In the only
controlled overlap, \(\delta v\to0\) followed by the late window, (L.42)
reduces to the proved decay (L.41).  The local finite-\(v\) data contain no
zero-frequency pole or boundary solution that forces a constant term for the
parabolic source.  Hence there is no positive evidence that
`JT-bfly-decay` fails.  Absence of such evidence is not a proof that the
finite-\(v\) continuation decays; the missing sourced saddle prevents both
directions.

**Q3 VERDICT.**  `JT-bfly-decay` persists in the Schwarzian matching window,
and the formal finite-\(v\) substitution (L.42) also decays with rate
\(v\kappa\).  Beyond that window the verdict is **HOLD**, because the
physical large-\(p\) pulse and its relative-shock boundary data have not been
specified.  No major reversal is found or claimed.  **QED.**  □

## 6. Structural comparison and window ledger

⟨1⟩33. **PROVE (comparison to the adjudicated rows).**  The three
claim rows and this rung occupy the following scopes:

| registered row | what that row proves | Liouville-rung relation |
|:--|:--|:--|
| `JT-B-susc` | At leading one-soft/tree \(O(C^{-1})\), a compact balanced pulse has the first-moment plateau (L.28), equal to the invariant soft DC residue, in the large-\(C\)-first window. | **Recovered** as \(\delta v\to0\).  **Not yet lifted:** the first finite-\(v\) term is \(\delta v\mathcal F_1\), and the source needed to calculate it is absent. |
| `JT-bfly-decay` | A pure parabolic horizon translation has zero plateau and the decay (L.41) in the Schwarzian future chart. | **Recovered** as \(\delta v\to0\); the formal rate replacement (L.42) also decays.  A physical sourced finite-\(v\) two-dot continuation remains open. |
| `JT-noplat-abs` | For every fixed \(\Delta>0\), the balanced Schwarzian absolute correlator decays while its calibrated ratio may plateau. | **No controlled test:** the microscopic fermion has \(\Delta=1/p\to0\), and the absolute decay becomes visible only at \(\kappa T=O(p)\), outside (L.4).  The formal resummation is consistent, not evidentiary. |

The entries follow respectively from (L.28)–(L.29), (L.41)–(L.43), and
(L.30)–(L.33).  Since every registered row already says
"Schwarzian-EFT scope," a Liouville HOLD is not a contradiction or a
downgrade.

⟨1⟩34. **PROVE (comparison to the ED rung).**  The ED computation has
finite \(N_m=8,10,12,14\), \(\beta J=5,10\), and detector times no later than
four inverse couplings after its single synchronization event.  It reports
no clean \(1\ll\beta J\ll N_m\) window, non-self-averaging calibrated ratios,
and constant absolute differences at the larger accessible sizes
(`theory/lanes/syk-jt/ed-rung-report.md`, Outcome, Conventions 10, and the
three-row comparison).  This Liouville rung instead takes \(N\to\infty\) and
\(p\to\infty\), but encounters:

\[
 \text{ED: no }1\ll\beta J\ll N_m,
 \qquad
 \text{Liouville: no controlled absolute tail at }
 \kappa T\gtrsim p,
 \tag{L.44}
\]

plus the missing microscopic source for the calibrated response.  These are
different window failures.  Neither rung is a limiting check on the other's
observed shape, and neither licenses a microscopic plateau theorem.

⟨1⟩35. **PROVE (declared usable window).**  Combining all controlled
inequalities gives

\[
 \boxed{
 \beta\mathcal J\gg1,
 \quad N/p^2\gg1,
 \quad 1\ll\kappa(T-u_*)\ll\min(\kappa C,p),
 \quad {\delta v\over\ell}\ll1
 }
 \tag{L.45}
\]

for a Euclidean bilocal smearing a fixed dimensionless distance \(\ell>0\)
from contact before continuation.  The first three conditions are
(L.2)–(L.4) and (L.10); the last is the near-boundary nonuniformity at
`refs/arxiv-2412.14799/Main.tex:443-458`.  The full retarded continuation
would additionally need its own uniformity bound.  No such bound is in the
local corpus; the older matrix-action derivation also explicitly neglects
possible long-time determinant contributions
(`refs/arxiv-1804.00491/GlobalAdSDraftRevisedSubmitted.tex:1471-1477`).
This report therefore makes no \(T=\infty\) statement at fixed
\((N,p,C)\).

**QED (comparison).**  The Liouville rung neither echoes nor conflicts with
the ED shapes in a common parametric window.  It recovers all three
Schwarzian statements where their derivation applies and finds that the
strict truncation lift is presently underdetermined.  □

## 7. Minimal data for the genuinely decisive Liouville computation

⟨1⟩36. **PROVE (completion criterion).**  A future calculation would
be well posed if and only if it adds, at minimum:

1. a named parity-even microscopic \(\mathcal O_R\), its normalization, and a
   compact waveform \(j(t)\);
2. the disorder-averaged two-dot Schwinger–Keldysh action and the induced
   \(\mathfrak s_{ab}(t_1,t_2)\), gluing conditions, and retarded initial data;
3. a measured energy gate \(\Delta E_R=0\) at the same perturbative order and
   a reference preparation with the identical final \((E_L,E_R)\);
4. the finite-\(v\) solution of (L.18), including the soft coefficient and
   every hard projection capable of reaching the equal-time \(LR\) grid;
5. a uniform remainder in (L.45), followed by the detector (L.13), its DC
   transform, and the shot cost.

Necessity follows from (L.14)–(L.20), D33, and the window proof (L.45).
Sufficiency follows because these data determine the retarded inverse and
source in (L.18), after which (L.13), (L.25), and (L.26) are direct
computations.  This criterion does not prescribe which pulse operator must be
chosen; different choices are different physical protocols and need not have
the same finite-\(v\) correction.

**QED (completion criterion).**  Merely supplying \(P(t)\) or imposing
\(\int P=0\) does not meet items 1–2.  Merely inserting a reparametrized
Ansatz does not meet item 4.  □

## 8. Merge proposals and honesty ledger

### Merge proposals

**None.**  Do not edit the three `CLAIMS.md` rows.  Their explicit
Schwarzian-EFT scopes remain correct, and an underdetermined Liouville lift
does not warrant a status change.  This report should be linked as the
large-\(p\) ladder rung and as the specification of the missing microscopic
input, not promoted as positive evidence for or against a finite-\(v\)
plateau.

### Source and novelty ledger

- **Local-source facts.**  The large-\(p\) action, equilibrium saddle,
  \(v\)-to-\(\beta\mathcal J\) relation, reparametrized ZZ saddles,
  displacement-operator derivation, stiffness hierarchy, finite-\(v\) mode
  note, and Ansatz caveat come from
  `refs/arxiv-2412.14799/Main.tex:149-195,223-253,291-311,327-348,411-427`.
  The two-dot matrix action, source-dependent boundary condition, two-time
  equations, general solution, and thermal-double continuation come from
  `refs/arxiv-1804.00491/GlobalAdSDraftRevisedSubmitted.tex:1453-1489`,
  `:1842-1889`, and `:2763-2790`.  The Schwarzian and shock endpoints come
  from the
  already adjudicated local shards and their cited local TeX.
- **Derived here.**  Equations (L.10)–(L.13) put the exact finite-\(v\)
  equilibrium bilocal on the campaign's equal-time grid.  Equations
  (L.17)–(L.20) prove that energy moments do not define the sourced
  Liouville problem.  Equations (L.23)–(L.26) isolate the precise conditional
  survival theorem.  Equations (L.30)–(L.34) expose the noncommuting
  \(T/p\) limit and cost.  Equations (L.37)–(L.39) identify the first
  truncation-lifting order without inventing its coefficient.
- **Physical arguments, explicitly flagged.**  The exponential
  reorganization (L.30), its absolute-decay/cost consequences, and the formal
  finite-\(v\) shock diagnostic (L.42)–(L.43) are not promoted as exact
  finite-\(p\) results.
- **Open.**  The microscopic pulse operator, contour forcing, finite-\(v\)
  retarded soft/hard projections, late relaxation, correction coefficient,
  and a uniform finite-parameter detector window remain uncomputed.

## 9. Final theorem

⟨1⟩37. **PROVE (Liouville-rung adjudication).**  Under the operational
specification D33 and conventions (L.1)–(L.4), the local large-\(p\) sources
prove the equilibrium detector (L.11)–(L.13), the Schwarzian recovery
(L.27)–(L.28), and the correction order (L.37).  They do not specify the
right side or retarded inverse in (L.18).  Therefore they determine neither
the existence nor the value of a finite-\(v\) plateau, nor the physical
finite-\(v\) continuation of the butterfly shift.  If a completed sourced
problem satisfies the displayed relaxation condition (L.23), then the
plateau survives and equals the DC residue by (L.25)–(L.26); that implication
does not establish its hypothesis.  The absolute detector's decay scale
\(T\sim p/\kappa\) does not overlap the controlled leading-\(1/p\) window.

**QED.**  □
