# Joint adversarial critic r2 — SYK/JT r1 repairs

## 0. Scope and recomputation protocol

I treated `theory/verdicts/syk-jt-joint-critic-r1.md` as the prior and attacked
only text or code changed in
`git diff 769bb8e..HEAD -- theory/lanes/syk-jt numerics`.  The amended
“Permanent” clause of `theory/lanes/syk-jt/observables-spec.md` is binding:
every late statement uses the large-\(C\)-first iterated limit, and a formal
ratio of vanishing correlators is not promoted as a practical finite-\(C\)
memory record.

All numerical mutation tests in this adjudication are performed on isolated
copies under `/tmp`; the repository sources and tests are not mutated.

This verdict is written incrementally.  Each r1 objection is closed only after
fresh algebra, code, or numerical recomputation below, rather than from either
repair response table.

## 1. O1/O2 — charge sector and synchronization

### O1 disposition: RETRACTION VERIFIED for T1

A fresh search of the repaired analytic shard finds protocol (b) only in
explicit retractions or in algebra labelled non-operational.  In particular,
⟨1⟩1.⟨2⟩2–4 retain an operational reference only for
\(\kappa_f=\kappa_i=\kappa\); ⟨1⟩3.⟨2⟩7 calls (3.11)–(3.13) an algebraic
diagnostic and says that it is not an allowed detector claim; ⟨1⟩5.⟨2⟩2
retracts the protocol-(b) verdict; the candidate sentence (5.3) is explicitly
balanced; and the B1/B2 detector handshakes are retracted at
⟨1⟩6.⟨2⟩1–2.  The surviving exact one-kick formula is not used to assert an
unbalanced plateau.  This is the downgrade licensed by r1 O1.

### O2 disposition: FIX VERIFIED

The same event \(u_*\) occurs in the early representatives (0.2), retained
reference (1.2), \(\bar T=T-u_*\) throughout (3.2)–(3.15), the subtraction
\(P_{\rm sub}=P-\Delta E\,\delta(u-u_*)\) in (4.6), the first-moment formulas
(4.7), (4.9), (4.10), and (4.14), the bilocal vertex (4.11), the limit in
(4.13), and the candidate (5.3).  No surviving formula substitutes \(u_f\)
for that synchronization event.

I also recomputed the covariance rather than relying on the matching symbols.
For the A1 balanced pair \((\kappa,\kappa_1,L)=(1,1.1,1)\), direct matrix
multiplication gives

\[
 a_{\rm bal}=1.052865035801626,\qquad
 -\kappa^{-1}\log a_{\rm bal}=-0.0515150538086572.
\]

Shifting the synchronization origin to \(u_*=0.37\) or \(-1.2\) conjugates the
centered transfer matrix by the appropriate diagonal thermal translation.  It
changes \((b,c)\) respectively to
\((-0.0628487480926,0.0484596268825)\) and
\((-0.302091821500,0.0100817919117)\), but leaves \(a_{\rm bal}\), and hence
the exact plateau, unchanged to \(3\times10^{-16}\).  Independently,

\[
 \int (u-u_*)P(u)\,du
 \mapsto \int (u-u_*-\sigma)P(u)\,du
 =\int (u-u_*)P(u)\,du
\]

because the retained sector has \(\int P=0\).  For the two-kick profile the
moment is \(-\Delta E_1L\) for all three choices of \(u_*\), reproducing
\(-\Delta E_1L/(2C\kappa^2)\) and the expansion of (3.10).  Thus the balanced
plateau and the leading DC formula are covariant under the requested shift.

## 2. O3 — exact versus leading criterion

**Disposition: FIX VERIFIED.**  Expanding the repaired exact result gives

\[
 -{1\over\kappa}\log a
 ={1\over2C\kappa^2}\int (u-u_*)P(u)\,du+O(C^{-2}),
\]

so the moment controls only the \(O(C^{-1})\) coefficient.  The shard now
states the exact classical criterion \(a\ne1\) separately in (3.7) and
⟨1⟩5.⟨2⟩1; (4.10) attaches “at leading \(O(C^{-1})\)” directly to the moment
equivalence; and both (4.10) and the verdict say that a zero moment leaves the
\(O(C^{-2})\) answer undetermined.  A search of every remaining “if and only
if”/moment occurrence found no surviving exact moment criterion.

## 3. O4 — non-circular DC transform

**Disposition: FIX VERIFIED.**  The repaired standalone command

```text
julia --project=numerics numerics/test/test_schwarzian_memory.jl
```

returned \(96/96\) with exit code zero.

For the required RED I copied `numerics/` to
`/tmp/syk-jt-r2-o4.m6rgF5/numerics` and changed only the copy's tail
coefficient from the fitted-matrix expression back to the supplied
`late_detector`.  The same suite then exited nonzero with \(93\) pass and
\(3\) fail.  Doubling the decoy detector changed the last-frequency absolute
residue from \(1.24367768269446\times10^{-4}\) to
\(7.90454841876999\times10^{-5}\), changed the extrapolated residue from
\(1.24780408799727\times10^{-4}\) to
\(5.83348047926424\times10^{-5}\), and doubled the purported fitted tail.
Thus the regression detects precisely the circular dependency removed by the
repair.

Independently of the implementation, let
\(M=\left(\begin{smallmatrix}a&b\\c&d\end{smallmatrix}\right)\) be the fitted
right post-pulse matrix and take \(k_L=1\), \(k_R=k_f\).  Direct asymptotics of
the bilocal give

\[
 {G_{\rm pulse}\over G_{\rm eq}}
 \longrightarrow
 \left|{\det M\over a^2}\right|^\Delta,\qquad
 {\partial_TG_{\rm eq}\over G_{\rm eq}}\longrightarrow
 -\Delta(1+k_f),
\]

and hence

\[
 \Delta u_{\rm fit}
 ={|\det M/a^2|^\Delta-1\over\Delta(1+k_f)}.
\]

Re-evaluating this formula directly from every JSON matrix agrees with each
stored `fitted_mobius_tail` to at worst \(2.22\times10^{-16}\).  Its
difference from the separately evaluated \(\Delta u_{\rm rel}(40)\) is at most
\(3.47\times10^{-13}\), so the reported detector is already in the fitted
asymptotic regime without being fed into the transform.

I also independently refit the \(\omega^2\) intercept from each row's three
low-frequency residues.  The recomputed intercepts agree with the stored
values to \(4.34\times10^{-19}\).  The largest relative change from horizon
\(40\) to \(80\) is \(3.648863495\times10^{-8}\), reproducing the response
table's \(3.65\times10^{-8}\).  Across all rows I obtain
\(\mathrm{DC/late}=0.999794744\)–\(0.999974868\) and
\(\mathrm{DC/vertex}=0.997668104\)–\(1.000109979\), reproducing the rounded
report.  The fitted-matrix tail, horizon variation, and low-frequency
extrapolation therefore supply the independent controls demanded by r1 O4.

## 4. O5 — operator-dimension threading and handshake

**Disposition: FIX VERIFIED.**  The \(\Delta\) keyword is consumed by the
bilocal and its equilibrium finite difference, and is threaded through
`observable_series`, the linear vertex, `dc_identity`, campaign points,
`run_campaign`, the sample-cost exponent, and JSON metadata.  A fresh
`run_campaign(Delta=1)` produced eight finite rows with
`operator_dimension = 1.0`; \(\Delta=0\) was rejected with
`ArgumentError`.

For the repaired A1 regression matrix I independently evaluated the
\(\Delta=1\) bilocal at \(T=(2,4,8)\) and obtained

\[
 \delta G_{LR}=
 (-1.43615624488180\times10^{-3},
  -3.21934849342498\times10^{-5},
  -1.10134890245999\times10^{-8}),
\]

which agrees with the three retained analytic A1 targets within the registered
tolerance.  I also varied \(\Delta=(0.25,0.5,1,1.7)\); both pulse and
equilibrium correlators changed with the requested power, confirming that the
public parameter is used rather than merely recorded.  The regression is
correctly scoped as a correlator handshake: T2's reported \(\Delta u\) is the
linear functional \(-\delta G/\partial_TG_{\rm eq}\), whereas T1's handshake
table separately labels its \(\Delta u\) column as the exact nonlinear
\(\operatorname{arcosh}\) readout.

## 5. O6 — iterated limit, detector window, and cost

**Disposition: DOWNGRADE/FIX VERIFIED.**  T1 ⟨1⟩5.⟨2⟩5 states

\[
 C\to\infty\ {\rm first},\qquad
 1\ll\kappa(T-u_*)\ll\kappa C,
\]

forbids a fixed-\(N\) or fixed-\(C\) \(T=\infty\) conclusion, gives the
fixed-time \(O(C^{-1})+O(C^{-2})\) structure, explicitly says that the
remainder is not uniform in \(T\), and records
\(M_{\rm shots}=O(e^{4\Delta\kappa(T-u_*)}/\eta^2)\).  It does not invent a
finite-\(C\) endpoint; correspondingly its claim is only a large-\(C\)-first
susceptibility, not permanence.

T2 states the same limit and defines its finite-\(C\) *proxy* by
\(\kappa=(1+k_f)/2\) and
\(\kappa T_{\max}=\sqrt{\kappa C}\).  At fixed positive \(\kappa\),

\[
 \kappa T_{\max}=\sqrt{\kappa C}\to\infty,\qquad
 {\kappa T_{\max}\over\kappa C}={1\over\sqrt{\kappa C}}\to0,
\]

so it obeys the declared double inequality as \(C\to\infty\).  The report and
JSON both label it a conservative convention, not a uniform error theorem.

I recomputed every table entry from the JSON.  The \(C=10\) rows give
\(\kappa T_{\max}=3.16228\)–\(3.16903\) and the \(C=100\) rows give
\(10.00000\)–\(10.00215\).  Re-evaluating
\[
 e^{4\Delta\kappa T_{\max}}/
 \bigl(0.1|\Delta u_{\rm fit}|\bigr)^2
\]
reproduces all eight shot proxies exactly at stored precision, including the
reported \(3.73548\times10^{10}\) minimum and
\(7.27219\times10^{21}\) maximum.

Those numbers are not lower bounds or impossibility theorems: bounded outcomes
plus independent estimation supply the displayed scaling only up to
protocol-dependent variance and finite-difference factors.  The repaired text
does not use them to claim impossibility; it calls them estimates and concludes
only that practical permanence has not been established.  The label
“maximum usable \(T\)” must likewise be read as the declared proxy, not a
derived physical endpoint.  With those explicit scopes, I find no O6
overclaim.

## 6. O7/O8 — source pointer and Taylor typography

**O7 disposition: FIX VERIFIED.**  The repaired (0.9) and honesty ledger point
to `GravityReparametrizationsRevised.tex:586-592`, whose Lorentzian ADM
formula contains \(-C\,\operatorname{Sch}(\tilde t,\tilde u)\), and separately
to lines 921–929, which print
\([ -Q^+Q^-+(Q^0)^2]/(2C)\).  The two cited ranges now cover both halves of
the asserted equality.

**O8 disposition: FIX VERIFIED.**  Equation (3.10) now contains the required
plus sign.  Expanding (3.8) directly gives
\[
 a_{\rm bal}=1+{\delta\kappa L\over2}+O(\delta\kappa^2),\qquad
 -{\log a_{\rm bal}\over\kappa}
 =-{\delta\kappa L\over2\kappa}+O(\delta\kappa^2).
\]
As a numerical derivative check at \((\kappa,L)=(1.7,0.8)\), the quotient by
\(\delta\kappa\) converges to \(-0.235294117647059=-L/(2\kappa)\), with a
finite quadratic residual.

## 7. New changed-text objection

### Objection 9 — FATAL: T2 still promotes six unbalanced formal comparators as operational detectors

**Location.**  The changed decisive verdict at
`theory/lanes/syk-jt/t2-numeric.md:249-258\), especially “Every extracted
relative-delay detector” and “the ... observable `delta G_LR` ... at all
eight points”; compare the comparator caveat at lines 270–273 and the repaired
T1 retraction at ⟨1⟩5.⟨2⟩2.

**Independent computation.**  In `observable_series`, the claimed
equilibrium comparator for an unbalanced row is evaluated with
\(M_L=M_R=I\), \(k_L=1\), and \(k_R=k_f\).  It therefore purports to have

\[
 (E_L,E_R)=\left({C\over2},{Ck_f^2\over2}\right).
\]

Six of the eight JSON rows are unbalanced: their measured right-energy changes
are \(8.59125\times10^{-3}\), \(8.58979\times10^{-2}\),
\(8.59139\times10^{-3}\), \(8.59125\times10^{-2}\),
\(1.03836\times10^{-2}\), and \(1.03836\times10^{-2}\).  Only the two
redshift-balanced derivative-Gaussian rows have zero energy change at leading
order (their full-run residuals are \(2.83\times10^{-8}\) and
\(2.83\times10^{-9}\)).

The T2 report supplies no implementable preparation of the unequal-energy
\((M_L,M_R)=(I,I)\) two-sided reference; its own caveat says that it does not
pretend this is a new TFD.  Consequently the six corresponding differences
are differences of formal EFT kernels, not demonstrated expectation
differences between two states \(\omega_N^{\rm protocol}\) in the binding
finite-\(N\) operational algebra.  This is exactly the charge-sector defect
for which T1 retracted protocol (b).  Renaming all eight ratios “detectors” in
changed text does not repair the missing reference protocol.

**FIX DEMAND.**  Restrict the operational T2 verdict, susceptibility wording,
and practical-cost conclusion to the energy-balanced rows at the stated
leading order, and label the six unbalanced rows as formal trajectory/DC
diagnostics; alternatively, exhibit an implementable two-dot reference
protocol with the same measured unequal pair \((E_L,E_R)\) and recompute its
two-sided correlator.

**SURVIVING WEAKER STATEMENT.**  All eight formal Schwarzian series and their
non-circular fitted-matrix DC transforms are numerically reproducible; the two
energy-balanced derivative-Gaussian rows support the operational
large-\(C\)-first susceptibility/no-absolute-plateau conclusion at leading
order, while no unbalanced operational detector conclusion is licensed.

**Severity.**  FATAL.  The observable specification classifies a
frame/comparator conclusion without an implementable Layer-0/1 protocol as a
razor violation, and the changed “every/all eight” language is itself a claim
of precisely that kind.

## 8. Per-statement rulings and verbatim-ready scopes

### (i) Balanced calibrated susceptibility plus DC identity — PROMOTE

Accepted scoping sentence (copy verbatim):

> At leading one-soft/tree order \(O(C^{-1})\), for a compact energy-balanced right-boundary power pulse \(P\) of fixed width and finite first moment, with a single synchronization event \(u_*\), the large-\(C\)-first calibrated susceptibility is \(\Delta u_{\rm rel}=[2C\kappa^2]^{-1}\int (u-u_*)P(u)\,du+O(C^{-2})\) and equals at that order the \(\omega\to0\) DC residue of the same invariant bilocal soft attachment, where the late limit means \(\kappa(T-u_*)\to\infty\) with \((T-u_*)/C\to0\); the \(O(C^{-2})\) remainder is controlled here only at fixed detector time, and neither a uniform finite-\(C\) late-time bound nor practical permanence is claimed.

The exact finite-amplitude equality to a single-soft vertex remains excluded,
as required by (4.13)–(4.14).

### (ii) Butterfly-decay clause — PROMOTE

Accepted scoping sentence (copy verbatim):

> For the pure Shenker–Stanford horizon translation \(g_{\rm shock}=\left(\begin{smallmatrix}1&\alpha\\0&1\end{smallmatrix}\right)\) in the energy-balanced, \(u_*\)-synchronized Schwarzian future chart, the calibrated two-sided delay has zero plateau and obeys \(\Delta u_{\rm rel}^{\rm NL}(T)=-\alpha\kappa^{-1}e^{-\kappa(T-u_*)}+O(e^{-2\kappa(T-u_*)})\), while \(\delta G_{LR}(T)=O(e^{-(2\Delta+1)\kappa(T-u_*)})\), in the large-\(C\)-first late window.

### (iii) Absolute-correlator no-plateau statement — PROMOTE in the balanced scope below; HOLD the T2 “all eight” generalization

Accepted scoping sentence (copy verbatim):

> For every \(\Delta>0\), a compact energy-balanced pulse whose post-pulse relative Möbius matrix lies in a nonsingular future chart with \(a>0\) has the \(u_*\)-synchronized same-energy absolute correlator difference \(\delta G_{LR}(T)={\cal N}_\Delta\kappa^{2\Delta}e^{-2\Delta\kappa(T-u_*)}[a^{-2\Delta}-1+O(e^{-\kappa(T-u_*)})]\), so this allowed absolute observable has no nonzero late plateau in the large-\(C\)-first window even when its calibrated ratio approaches a nonzero susceptibility.

All r1 objections O1–O8 are disposed of in their repaired scopes.  Objection 9
prevents a joint PASS until the changed T2 verdict is restricted to its
operationally supported balanced sector or an implementable unbalanced
reference is supplied.

FAIL(9)

## r2a: Objection 9 delta adjudication

**O9 disposition: FIX VERIFIED; CLOSED.**  The revised decisive-numerical-
verdict paragraph restricts the susceptibility, absolute-correlator
no-plateau, and finite-\(C\) cost conclusions to the two
energy-balanced derivative-Gaussian rows, at the report's declared
large-\(C\)-first/leading balanced scope.  It explicitly labels all six
unbalanced rows as formal Schwarzian trajectory/DC diagnostics and denies
them any operational detector conclusion, exactly matching O9's accepted
first fix-demand branch.

Fresh evaluation of the JSON `extrapolated_vertex_ratio` values gives
\(1.000109978916786\) at \(C=10\) and \(0.999988369060947\) at \(C=100\).
Their deviations from unity are respectively \(0.010997891679\%\) and
\(0.001163093905\%\); the worst rounds to \(0.011\%\), so “0.011% or better”
is correct.

The `HEAD~1` delta adds no competing operational claim: the response says
that no implementable unequal-\((E_L,E_R)\) reference is claimed, and every
added reference to the six unbalanced rows calls them formal diagnostics or
states that they license no operational detector conclusion.  Objection 9 is
therefore discharged, superseding the historical r2 terminal line above.

PASS
