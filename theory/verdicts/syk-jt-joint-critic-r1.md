# Joint adversarial critic r1 — SYK/JT decisive computation

## 0. Scope and independently reproduced baseline

I treated `theory/lanes/syk-jt/observables-spec.md` as binding.  Thus the
finite-\(N\) even algebra and its two-sided correlators and energies are the
observables; \(t(u)\), a fitted Möbius matrix, and the non-energy Schwarzian
charges are scaffolding until eliminated in favour of those observables.

The unmodified standalone command

```text
julia --project=numerics numerics/test/test_schwarzian_memory.jl
```

was rerun by this critic and returned `81/81` with exit code zero.  That is only
the green baseline.  The analytic formulas, the gates, and the cross-lane
handshake are recomputed below rather than inferred from that result.

The limit order used in this verdict is: first \(N\to\infty\), equivalently the
large-\(C\) tree limit with fixed compact source and fixed detector time; only
then \(T\to\infty\) inside the semiclassical/Schwarzian window.  A claim about a
literal \(T=\infty\) detector at fixed \(N\) is not licensed.

## 1. Analytic recomputation

Direct differentiation of the charges in T1 (0.5) gives

\[
 \dot Q^a=C\,{\operatorname{Sch}'(t,u)\over t'}(1,t,t^2)^a,
 \qquad \dot H=t'^2T_{tz}=:P,
\]

so, if positive injected right energy means \(P>0\), the sign used in both
implementations follows from the displayed sourced equation at
refs/arxiv-1606.01857/GravityReparametrizationsRevised.tex:611-623.  The
opposite prose sign at lines 957-965 is genuinely inconsistent and is followed
by the literal FIXSIGNS AND FACTORS comment.  I therefore use the equation, not
that prose, to orient the computation.

Substitution of \(g\cdot e^{\kappa u}\) reproduces T1 (2.2), its Casimir, the
one-parameter stabilizer missed by the three charges, and the endpoint formula
(2.6).  Multiplying the transfer matrices in (2.8) also reproduces all four
printed matrices and all 12 finite-time handshake targets.  The late expansion
is

\[
 \delta G_{LR}=\mathcal N_\Delta\kappa_f^{2\Delta}
 e^{-2\Delta\kappa_fT}(a^{-2\Delta}-1+O(e^{-\kappa_fT})),
\quad
 \Delta u_{\rm NL}\to-{\log a\over\kappa_f}.
\]

For the pure translation \(a=1,b=\alpha,c=0,d=1\), the next term instead gives
\(\Delta u_{\rm NL}=-\alpha e^{-\kappa_fT}/\kappa_f+O(e^{-2\kappa_fT})\).
At equal boundary times this is the same rate as the printed
\(\alpha e^{-R(t_L+t_R)/(2\ell^2)}\) factor in
refs/arxiv-1306.0622/shock.tex:223-234, with
\(\kappa_f=R/\ell^2\).  Those algebraic parts of T1 survive attack.

### Objection 1 — FATAL: the unbalanced subtraction changes an allowed exact charge

**Location.** theory/lanes/syk-jt/t1-analytic.md,
⟨1⟩1.⟨2⟩2–4 (especially (1.2)), ⟨1⟩3.⟨2⟩2 (3.2), and the protocol-(b)
verdict ⟨1⟩5.⟨2⟩2; compare theory/lanes/syk-jt/observables-spec.md, Layer 1
and “Consequences”.

**Independent computation.** A right-only source leaves the allowed measured
left energy at \(E_L=C\kappa_i^2/2\) and changes the right energy to
\(E_R=C\kappa_f^2/2\).  T1 (1.2) instead changes *both* reference clocks to
\(\kappa_f\), and (3.2) also inserts \(t_L=-e^{-\kappa_fT}\) into the pulsed
correlator.  Thus its protocol-(b) subtraction does not compare protocols with
the same pair \((E_L,E_R)\), even though those energies are allowed exact
charges.  With the untouched left clock, direct Möbius substitution gives

\[
 K_{LR}(T)={\kappa_i\kappa_f e^{(\kappa_f-\kappa_i)T}\over
 [a e^{\kappa_fT}+b+c e^{(\kappa_f-\kappa_i)T}
       +d e^{-\kappa_iT}]^2},
\]

not T1 (3.2).  Its late ratio is still \(a^{-2\Delta}\), but the calibrated
linear denominator is \(\Delta(\kappa_i+\kappa_f)\), and the finite-time
numbers and nonlinear calibration change.  More importantly, T1's stated
comparison is in the wrong exact-charge sector and therefore fails the binding
operational algebra.

**FIX DEMAND.** Recompute protocol (b) with an explicitly implementable
reference having the same measured \((E_L,E_R)\), keeping
\(\kappa_L=\kappa_i\), and state how that reference state is prepared.

**SURVIVING WEAKER STATEMENT.** The balanced sector
\(\kappa_f=\kappa_i\), the Möbius transfer algebra, and the pure-translation
decay result are unaffected; no present T1 detector claim for an unbalanced
right-only pulse is licensed.

### Objection 2 — MAJOR: T1 uses two incompatible synchronization conventions

**Location.** theory/lanes/syk-jt/t1-analytic.md (1.2), which fixes the new
equilibrium origin at \(u=0\), versus (4.6)–(4.10) and the candidate sentence
⟨1⟩5.⟨2⟩6, which subtract \(\Delta E\,\delta(u-u_f)\).

**Independent computation.** Linearizing \(t=e^{\kappa u+\varepsilon}\) gives

\[
 {C\over\kappa}(\partial_u^4-\kappa^2\partial_u^2)\varepsilon=-P.
\]

For the comparator \(e^{\kappa_f u}\) actually stated in (1.2), matching the
retarded solution gives

\[
 a=1-{1\over2C\kappa}\int uP(u)\,du+O(C^{-2}),\qquad
 \Delta u_{\rm rel}={1\over2C\kappa^2}\int uP(u)\,du+O(C^{-2}).
\]

T1's fictitious endpoint subtraction instead gives
\(-[2C\kappa^2]^{-1}\int(u_f-u)P\), which is the answer for a comparator
synchronized at \(u_f\), not at zero.  The discrepancy is observable.  For
T2's \([0,0.5]\) top hat at linear order,
\(P=\epsilon e^{2u}\), so \(\int uP=\epsilon/4\).  At
\((C,\epsilon)=(10,0.01)\), the zero-origin prediction is
\(+1.25000\times10^{-4}\), agreeing with T2's
\(+1.24803\times10^{-4}\); T1's printed endpoint formula predicts
\(-8.97852\times10^{-5}\).  This is the origin of the apparent sign conflict.

**FIX DEMAND.** Declare one synchronization event \(u_*\) and use
\(+[2C\kappa^2]^{-1}\int(u-u_*)P(u)\,du\) consistently in the exact
comparator, the DC subtraction, and the candidate statement.

**SURVIVING WEAKER STATEMENT.** For balanced pulses \(\int P=0\), the answer is
independent of \(u_*\), and T1's formula equals the corrected one.

### Objection 3 — MINOR: “dwell-time moment iff” is only a linear-order statement

**Location.** theory/lanes/syk-jt/t1-analytic.md (3.7), (3.13), (4.9), and
the quantifiers in ⟨1⟩5.⟨2⟩1–2.

**Independent computation.** The exact criterion is \(a\ne1\).  A nonzero
first moment is exactly the criterion for a nonzero *\(O(C^{-1})\)
coefficient*, not for the full finite-amplitude plateau: T1's own endpoint
kick has zero first moment at that order but has the nonzero
\(O(C^{-2})\) value (3.13).  Conversely, higher moments can cancel the exact
matrix coefficient even when a truncated expansion appears nonzero.

**FIX DEMAND.** Reserve “iff” for \(a\ne1\); say “iff at leading
\(O(C^{-1})\)” whenever the moment replaces \(a\).

**SURVIVING WEAKER STATEMENT.** A nonzero dwell-time moment guarantees a
plateau at leading response, while zero moment leaves the nonlinear answer
undetermined.

## 2. Numerical code attack

The implemented fourth-order equation is correct: differentiating the
Schwarzian gives

\[
 t''''={4t''t'''\over t'}-{3t''^3\over t'^2}
       -{t'^3T_{tz}\over C},
\]

which is exactly numerics/src/schwarzian_memory.jl:84-89.  The charge formulas,
piecewise RK4 integration, and Möbius fit were recomputed.  The reported
three-period chart error, RK4 orders, outside-support charge drifts, and charge
jump residuals are reproduced by the green run.

Four separate copies under /tmp were then mutated one hypothesis at a time:

| mutation on isolated copy | exit | observed failure |
|---|---:|---|
| flip the source term sign | 1 | 68 pass, 10 fail, 1 error; all charge-jump orientations fail |
| remove the validator's charge-jump gate | 1 | 77 pass, 4 fail; poison validation and no-write checks fail |
| place NaN in every campaign displacement row | 1 | 78 pass, 1 error; campaign validation aborts before output |
| replace the fitted Möbius matrix by zero | 1 | 64 pass, 1 fail, 3 errors; fit/observable gates fail |

Thus the requested mutation battery is red-capable.  The NaN, empty-set, and
charge poison modes also independently exit nonzero and create no JSON.  The
finiteness/write-order contract survives.

The plateau-versus-decay comparison is not rigged in favour of the constant:
on the eight raw \(\delta G_{LR}\) rows the exponential wins every time.  The
AIC advantage over the constant ranges from \(75.6\) to \(107.0\), and the
ratio \({\rm RSS}_{\rm const}/{\rm RSS}_{\rm exp}\) ranges from
\(2.67\times10^8\) to \(6.89\times10^{11}\).  This directly establishes that
the constant model can and does lose.

### Objection 4 — MAJOR: DC/late is forced to one by the supplied tail

**Location.** numerics/src/schwarzian_memory.jl:294-325, especially the tail at
lines 306-320; theory/lanes/syk-jt/t2-numeric.md:136-142 and 165-190.

**Independent computation.** The routine is handed late_delta, then appends

\[
 -\,{\tt late\_delta}\,{e^{s(T_h-T_0)}\over s},\qquad
 s=i\omega-\omega^2,
\]

as the infinite tail and divides the resulting residue by the same
late_delta.  Irrespective of the computed transient, that tail dominates as
\(\omega\to0\), so DC/late tends to one by construction.  For a constant
response alone its reported real ratio is exactly
\(1/(1+\omega^2)\).  This is a numerical implementation of the final-value
identity being tested, not an independent test of it.

The finite-\(\omega\) residuals themselves are benign.  In the first top-hat
row, \((1-r)/\omega^2\) at \(\omega=(0.2,0.1,0.05)\) is
\((5.07,5.45,5.56)\); for a balanced row it is approximately
\((1.25,1.30,1.32)\).  Hence the value 0.985 at \(\omega=0.05\) is an
expected \(O(\omega^2)\) Abel/transient correction, not an unexplained 1.5%
tree error.  After factoring out that common finite-frequency residue, the
late/linear-soft mismatch ranges from \(0.00075\%\) to \(0.215\%\) and scales
with source amplitude divided by \(C\), as the expected nonlinear correction
does.  This supports, but does not replace, the analytic leading-order
identity.

**FIX DEMAND.** Remove the target-valued tail from the test: obtain the tail
coefficient independently from the fitted post-pulse matrix or transform the
source/vertex response directly, vary the numerical horizon, and extrapolate
\(\omega\to0\) before comparing with the separately computed late detector.

**SURVIVING WEAKER STATEMENT.** The finite-frequency transform is internally
consistent, and the independent linear-soft amplitude has the expected
\(1/C\) scaling; the numerical DC/late column is not evidence for the
zero-frequency equality.

## 3. Cross-examination at the T1 handshake points

I drove T2's sourced ODE and Möbius fitter with flat windows of widths
\(w=(0.04,0.02,0.01)\).  For every window the amplitude was solved so that
\(\int P\,du\) equalled the corresponding T1 impulse energy exactly; the
three widths were then extrapolated quadratically to \(w=0\).  “Width error”
below is the difference between the last-two-width linear extrapolation and
the three-width quadratic extrapolation.  The observable was evaluated at
\(\Delta=1\), as the handshake requires.

| id | \(T\) | T1 \(\Delta u\) | T2 \(w\to0\) \(\Delta u\) | abs. diff / width err. | T1 \(\delta G\) | T2 \(w\to0\) \(\delta G\) | abs. diff / width err. |
|---|---:|---:|---:|---:|---:|---:|---:|
| A1 | 2 | -4.39168663063e-2 | -4.39168591705e-2 | 7.14e-9 / 1.00e-6 | -1.43615624490e-3 | -1.43615600126e-3 | 2.44e-10 / 3.18e-8 |
| A1 | 4 | -5.05127856135e-2 | -5.05127863929e-2 | 7.79e-10 / 3.62e-7 | -3.21934849346e-5 | -3.21934853865e-5 | 4.52e-13 / 2.20e-10 |
| A1 | 8 | -5.14967277827e-2 | -5.14967297124e-2 | 1.93e-9 / 2.68e-7 | -1.10134890247e-8 | -1.10134894162e-8 | 3.92e-16 / 5.44e-14 |
| A2 | 1 | -3.34367183536e-2 | -3.34366865394e-2 | 3.18e-8 / 3.33e-6 | -8.56539591783e-3 | -8.56538670581e-3 | 9.21e-9 / 8.17e-7 |
| A2 | 2 | -3.84152771109e-2 | -3.84152901547e-2 | 1.30e-8 / 1.47e-6 | -1.90891673143e-4 | -1.90891731066e-4 | 5.79e-11 / 6.78e-9 |
| A2 | 4 | -3.91547192603e-2 | -3.91547386932e-2 | 1.94e-8 / 1.20e-6 | -6.52569291811e-8 | -6.52569590266e-8 | 2.98e-14 / 1.85e-12 |
| B1 | 1 | -3.29831010648e-2 | -3.29831266661e-2 | 2.56e-8 / 2.39e-7 | -6.17931010335e-3 | -6.17931474618e-3 | 4.64e-9 / 5.55e-8 |
| B1 | 3 | -4.22674604349e-3 | -4.22674959921e-3 | 3.56e-9 / 1.37e-6 | -1.51531004613e-5 | -1.51531030938e-5 | 2.63e-12 / 5.30e-9 |
| B1 | 6 | -1.14966288269e-3 | -1.14966403627e-3 | 1.15e-9 / 1.49e-6 | -5.65638658713e-9 | -5.65637704982e-9 | 9.54e-15 / 7.91e-12 |
| B2 | 2 | -1.05063956171e-1 | -1.05063967632e-1 | 1.15e-8 / 2.82e-7 | -2.76776253804e-3 | -2.76776281756e-3 | 2.80e-10 / 1.03e-8 |
| B2 | 6 | -1.51914003817e-2 | -1.51914021277e-2 | 1.75e-9 / 1.26e-6 | -4.84087396276e-6 | -4.84087367573e-6 | 2.87e-13 / 4.65e-10 |
| B2 | 12 | -7.14189958382e-3 | -7.14190043099e-3 | 8.47e-10 / 1.35e-6 | -1.71236483051e-9 | -1.71236435018e-9 | 4.80e-16 / 3.73e-13 |

Every discrepancy is below the width-extrapolation uncertainty.  There is no
cross-lane numerical objection to T1's impulse transfer matrices or its
12-row table.

### The sign, adjudicated

With \(P=\dot H_R>0\), a small kick of energy \(\Delta E\) at \(u=s\), compared
with a final right thermal clock synchronized at \(u=0\), has

\[
 g=H_\kappa(s)B(\kappa,\kappa_f)H_{\kappa_f}(s)^{-1},\qquad
 \Delta u_{\rm rel}={s\,\Delta E\over2C\kappa^2}+O(C^{-2}).
\]

Thus positive energy deposited after the synchronization event makes the
right clock lag in the convention
\(\delta G=-\Delta u_{\rm rel}\partial_TG_{\rm eq}\), giving positive
\(\Delta u_{\rm rel}\).  An impulse exactly at \(s=0\) has no linear term and
retains T1's negative quadratic term.  T1's balanced raise-at-zero,
lower-at-\(L\) profile has \(\int uP=-\Delta E L\) and hence a negative
plateau.  T2's derivative Gaussian has the opposite ordering: it removes
energy before its centre and restores it afterwards, so its plateau is
positive.  The lanes' signs are therefore internally consistent for their
different profiles; only T1's finite-duration *unbalanced* endpoint
subtraction is inconsistent with its declared synchronization, as Objection 2
shows.

For T2's balanced profile, writing \(x=(u-0.25)/0.05\) gives at leading order

\[
 P_0(u)=0.05\,e^{0.5}x e^{-x^2/2},\quad
 \int_0^{0.5}P_0=0,\quad
 \int_0^{0.5}uP_0=5.16583442836\times10^{-4}.
\]

The resulting predictions are \(2.5829172\times10^{-5}\) at \(C=10\) and
\(2.5829172\times10^{-6}\) at \(C=100\), versus T2's
\(2.5830294\times10^{-5}\) and \(2.5829284\times10^{-6}\).  Its fitted
\(a\)'s are 0.9999741704 and 0.9999974171, explicitly \(a\ne1\).
Accordingly, zero net energy and nonzero dwell-time moment are perfectly
compatible.  T1 and T2 have the same theorem shape in the balanced sector:
the calibrated ratio plateaus while the absolute correlator difference
decays.

### Objection 5 — MINOR: the T2 observable API hard-codes the wrong handshake dimension

**Location.** numerics/src/schwarzian_memory.jl:199-224 and
theory/lanes/syk-jt/t2-numeric.md:127-134; JSON records
operator_dimension \(=1/2\), whereas T1 ⟨1⟩6 fixes \(\Delta=1\).

**Independent computation.** The private bilocal accepts a Delta keyword, but
observable_series never exposes it and always uses the default \(1/2\).
Consequently the prescribed \(\Delta=1\) cross-check cannot be performed
through T2's reported observable path; I had to use the fitted matrix and
re-evaluate the same kernel at \(\Delta=1\).  The table above shows that the
dynamics is sound, but the interface does not encode the handshake contract.

**FIX DEMAND.** Thread Delta through observable_series, campaign metadata, and
tests, and add the four T1 protocols as regression rows.

**SURVIVING WEAKER STATEMENT.** T2's \(\Delta=1/2\) campaign results are
self-consistent, and its trajectory/Möbius output reproduces the independent
\(\Delta=1\) targets.

## 4. Operational razor and detector cost

At every finite \(T\), the quantity

\[
 \Delta u_{\rm rel}(T)=-{\delta G_{LR}(T)\over
 \partial_TG^{\rm eq}_{LR}(T)}
\]

is an allowed *detector functional*: its numerator is a difference of two
Layer-1 two-sided expectations and its denominator can be calibrated by a
finite difference of equilibrium expectations.  It is not itself a new
operator or a measurement of \(g_{\rm rel}\).  T1's use of \(a\) to calculate
it is admissible scaffolding only because (3.2)-(3.6) eliminate \(a\) in favour
of the correlator.  T2's phrase “permanent relative-frame parameter” must
likewise be read only as shorthand for this finite-time statistic.

The conditioning is severe.  For bounded single-shot observables and
\(G,\delta G,\partial_TG=O(e^{-2\Delta\kappa T})\), obtaining fixed absolute
error \(\eta\) in \(\Delta u_{\rm rel}\) by repeated independent preparations
costs

\[
 M_{\rm shots}=O\!\left({e^{4\Delta\kappa T}\over\eta^2}\right)
\]

up to protocol-dependent variance and finite-difference constants.  For T2's
\(\Delta=1/2,\kappa\simeq1\), this is \(O(e^{2T}/\eta^2)\); at \(T=40\), the
exponential factor alone is about \(5.5\times10^{34}\).  Measuring numerator
and denominator rather than calibrating the denominator analytically does not
improve that exponent.  Hence the ratio is operationally allowed at finite
time but is not a robust late-time record: the formal plateau is a ratio of
two exponentially vanishing signals.

### Objection 6 — MAJOR: neither lane supplies the mandated quantitative late-time window

**Location.** theory/lanes/syk-jt/t1-analytic.md ⟨1⟩0.⟨2⟩1,
⟨1⟩3.⟨2⟩5, and ⟨1⟩5.⟨2⟩5; theory/lanes/syk-jt/t2-numeric.md:188-196;
theory/lanes/syk-jt/observables-spec.md, final “permanent” bullet.

**Independent computation.** The cited MSY source establishes the expansion
parameter \(\beta/C\) at
refs/arxiv-1606.01857/GravityReparametrizationsRevised.tex:680-719, but neither
lane proves an error bound uniform in \(T\), accounts for the exponentially
growing shot cost, or gives a finite-\(N\) maximum detector time.  No
quantitative upper endpoint can be certified from the cited sources.  This
verdict therefore uses the conservative iterated scaling convention

\[
 C\to\infty\ {\rm first},\qquad
 1\ll\kappa T\ll\kappa C
\]

(more invariantly, take \(\kappa T\to\infty\) while \(T/C\to0\)), followed by
any claim about the formal tree limit.  This convention is not a derived
finite-\(C\) error bound; it only prevents the unsupported reverse order.
Taking \(T\to\infty\) first at fixed \(C\) or fixed \(N\) is not supported.

**FIX DEMAND.** State the iterated limit in both verdicts and provide a
finite-\(N\)/finite-\(C\) error or a maximum usable \(T\), including the
detector's exponential sample cost.

**SURVIVING WEAKER STATEMENT.** The ratio plateau is a well-defined
large-\(C\)-first susceptibility; the absolute allowed observable always
decays, and practical permanence is not established.

## 5. Leaf-by-leaf source and algebra audit

- **T1 ⟨1⟩0.⟨2⟩1-6.** The MSY statements about the coupling, Möbius
  redundancy, bilocal dressing, charges, and sourced equation occur at the
  cited lines, and the quotient-rule identities recompute.  One Hamiltonian
  pointer is incomplete (Objection 7).
- **T1 ⟨1⟩1.⟨2⟩1-4.** The thermal-map and two-sided-charge quotations are
  real.  The synchronization is explicitly marked as a physical argument,
  but its implementation fails Objections 1-2.
- **T1 ⟨1⟩2.⟨2⟩1-8.** Every leaf is a displayed-prior or elementary
  Schwarzian/matrix computation; (2.2)-(2.11) were independently multiplied
  and survive.  The quotation at MSY lines 1116-1122 really does say that the
  charge effect can be removed on either side of an insertion but not both.
- **T1 ⟨1⟩3.⟨2⟩1-8.** Equations (3.2)-(3.9) and (3.11)-(3.15) recompute.
  The Shenker-Stanford line range really contains the stated equal-time decay
  factor and says that it becomes insignificant at late summed time.  Equation
  (3.10) has a typographical mathematical error (Objection 8).
- **T1 ⟨1⟩4.⟨2⟩1-9.** The quadratic action, homogeneous modes, bilocal vertex,
  \(1/(2\pi C)\) coefficient, and large-\(p\) stiffness statements all occur
  at the cited local lines.  The low-frequency residue recomputes for the
  chosen subtracted response, but that choice inherits Objection 2.  The
  real-axis \(i0\) formula does not by itself specify how the
  \(e^{\pm\kappa u}\) gauge modes are projected; the endpoint/Möbius conditions,
  not the cited source, supply that extra prescription.
- **T1 ⟨1⟩5.⟨2⟩1-6.** These are restatements of prior displays.  Their only
  new failures are the exact-versus-leading quantifier in Objection 3 and the
  candidate's synchronization/charge-sector defects.
- **T1 ⟨1⟩6.⟨2⟩1-2.** All four matrices, four plateaux, and 12 finite-time
  values independently reproduce, and the T2 width extrapolation above
  reaches them.
- **T1 ⟨1⟩7.⟨2⟩1-3.** Every literature pointer is real and says what the
  honesty ledger attributes to it.  No claim of literature priority is
  smuggled in.
- **T2 source pointers.** The Schwarzian, source equation, charges,
  Lorentzian exponential coordinate, bilocal dressing, and two-sided charge
  constraint all occur at the reported MSY lines.  The report's “472-line”
  count is stale (the inspected module is 475 lines) but remains inside the
  200-500 line bound.

### Objection 7 — MINOR: the Hamiltonian citation omits half the asserted equality

**Location.** theory/lanes/syk-jt/t1-analytic.md
⟨1⟩0.⟨2⟩6, lines 117-130.

**Independent computation.** MSY lines 921-929 print
\(H=[-Q^+Q^-+(Q^0)^2]/(2C)\), as T1 says, but they do not print
\(H=-C\operatorname{Sch}(t,u)\).  The latter is instead the Lorentzian part of
the ADM equation at MSY lines 586-592.  The identity itself is correct.

**FIX DEMAND.** Add the 586-592 pointer to (0.9).

**SURVIVING WEAKER STATEMENT.** Equation (0.9) is algebraically and
source-correct after that citation repair.

### Objection 8 — MINOR: equation (3.10) is missing a plus sign

**Location.** theory/lanes/syk-jt/t1-analytic.md (3.10), lines 491-496.

**Independent computation.** Expanding (3.8) gives
\[
 -\kappa^{-1}\log a_{\rm bal}
 =-{\delta\kappa\,L\over2\kappa}+O(\delta\kappa^2).
\]
The displayed T1 equation instead juxtaposes the leading term and
\(O(\delta\kappa^2)\), which denotes multiplication rather than an asymptotic
remainder.

**FIX DEMAND.** Insert “\(+\)” before \(O(\delta\kappa^2)\).

**SURVIVING WEAKER STATEMENT.** The intended Taylor coefficient is correct.

## 6. Joint verdict and recommendation

The two lanes agree on the genuinely recomputed core:

1. a post-pulse Möbius coefficient \(a\ne1\) produces a plateau in the
   calibrated correlator ratio while \(\delta G_{LR}\) itself decays;
2. the balanced T2 profile has zero net energy but a nonzero first moment, so
   its nonzero plateau is exactly of T1's leading balanced type;
3. the pure Shenker-Stanford translation has \(a=1\) and only the printed
   exponentially decaying geodesic effect;
4. after a consistent subtraction, the leading balanced response and the
   invariant bilocal soft attachment have the same DC residue.

They do **not** yet establish the candidate statement as written.  The
unbalanced comparator changes or fails to define the full allowed energy
sector, T1's stated and implemented synchronization events disagree, T2's
DC/late number inserts its target as an analytic tail, and neither lane
quantifies the finite-\(N\)/finite-\(C\) detector window.  These are
claim-licensing failures, not disagreements with the exact impulse algebra.

**Recommendation for T1 ⟨1⟩5.⟨2⟩6: HOLD.**  A promotable replacement would
restrict first to balanced pulses (or specify and implement a common
\(u_*\)-synchronized reference with matching measured energies), call
\(\Delta u_{\rm rel}\) a large-\(C\)-first calibrated susceptibility, retain
the \(O(C^{-2})\) and finite-width errors, and state separately that the
absolute allowed correlator has no late plateau.  The butterfly-decay clause
can be promoted independently.

FAIL(1,2,4,6)
