# G3-WARD-NUMERIC: finite-N Ward-defect experiment

## Scope and conventions

This is a Layer-0 calculation in the parity-even CAR algebra of two identical
finite SYK dots.  It uses the existing `numerics/src/syk_ed.jl` implementation
without modifying it.  On one dot,
\(\{\chi_i,\chi_j\}=\delta_{ij}\) and

\[
 H=-\sum_{i<j<k<l}J_{ijkl}\chi_i\chi_j\chi_k\chi_l,
 \qquad \mathbb E J_{ijkl}^2=3!J^2/N_m^3,
\]

with \(J=1\).  The right copy is the conjugate representation used by the ED
rung.  A coefficient matrix \(C\) represents
\(\sum_{ab}C_{ab}|a\rangle_L|b\rangle_R\).  Both boundary clocks evolve
forward, so the decoupled generator acts as
\(H_0 C=HC+CH\).  This convention makes the calibration identity

\[
 i[H_0,B(u,v)]=(\partial_u+\partial_v)B(u,v)
\]

an exact finite-matrix equality.

The Euclidean labels are \(\epsilon_{n,c}(\tau)=\cos(n\tau)\).  In the
real-time ED calculation the same Fourier label means the real oscillatory
profile
\(\epsilon_n(t)=\cos(\omega_n t)\),
\(\omega_n=2\pi n/\beta\), rather than the exponentially growing analytic
continuation \(\cosh(2\pi nt/\beta)\).  Thus the tested non-Möbius mode has
real frequency \(4\pi/\beta\).  Fermion endpoint dimension is fixed to the
q=4 conformal value \(\Delta_\psi=1/4\) in the target variation (4.2).

The measured Layer-1 representatives are Hermitian mixed bilocals

\[
 B_\delta(u,v)=e^{-\delta H_0}
 \left[-\frac{i}{N_m}\sum_j\chi_j^L(u)\chi_j^R(v)\right]
 e^{-\delta H_0},
\]

implemented exactly at finite size.  Only inside the heat kernel, \(H\) is
shifted by its ground energy: \(K_\delta=e^{-\delta(H-E_0)}\).  This scalar
shift changes neither Heisenberg evolution nor any commutator, prevents an
irrelevant exponential blow-up, gives \(K_0=1\), and makes
\(K_\delta\to P_0\) as \(\delta\to\infty\).  The main grid uses
\(\delta J=0.15\).

## Red-green TDD evidence

The standalone test was written and saved before the lane implementation
existed.  The first run was RED with exit code 1, and no result JSON existed:

```text
$ julia --project=numerics numerics/test/test_syk_ward.jl
ERROR: LoadError: SystemError: opening file "/home/tobias/Projects/tns-as-st-me/numerics/src/syk_ward.jl": No such file or directory
Stacktrace:
 [1] include(mapexpr::Function, mod::Module, _path::String)
   @ Base ./Base.jl:307
 [2] top-level scope
   @ ~/Projects/tns-as-st-me/numerics/test/test_syk_ward.jl:11
 [3] include(mod::Module, _path::String)
   @ Base ./Base.jl:306
 [4] exec_options(opts::Base.JLOptions)
   @ Base ./client.jl:317
 [5] _start()
   @ Base ./client.jl:550
in expression starting at /home/tobias/Projects/tns-as-st-me/numerics/test/test_syk_ward.jl:11
RED_EXIT_CODE=1
```

After implementing the already-fixed contract, the final standalone run was
GREEN:

```text
$ julia --project=numerics numerics/test/test_syk_ward.jl
Test Summary:                      | Pass  Total   Time
G3 finite-N Ward-defect experiment |   64     64  33.5s
```

The test writes `numerics/results/syk_ward.json` only after the outer test set
is green, and the writer repeats every finiteness and physics gate before
opening the output path.  Child runs poisoned with a NaN, an empty campaign,
a failed n=0 calibration, non-Hermiticity, odd parity, or failed quadrature
order all exited nonzero and left no JSON at the requested path.

## Candidate operators and measurement protocol

The fixed even Hermitian two-body operator in both families is exactly the ED
rung's operator

\[
 A_2=\frac{\sum_{i<j}k_{ij},i\chi_i\chi_j}
 {\left\|\sum_{i<j}k_{ij},i\chi_i\chi_j\right\|},
\]

where the independent Gaussian \(k_{ij}\) stream is fixed by the disorder
seed plus the ED rung's offset 10,000,019.  No matrix element in this lane is
used to tune its coefficients or its normalization.

For \(\sigma=w\beta/(2\pi)\), let
\(g_\sigma(t)=e^{-t^2/(2\sigma^2)}\), truncated at
\(|t|\le4\sigma\).  Every integral below is divided by
\(\int_{-4\sigma}^{4\sigma}g_\sigma(t)dt\) and evaluated with the
composite trapezoid rule.

1. **Frequency-filtered bilinear.**
   \[
   q_N^{\rm filt}(n,w)=
   \frac{\int dt\,g_\sigma(t)\cos(\omega_nt)A_2(t)}
        {\int dt\,g_\sigma(t)},\qquad
   Q_N^{\rm filt}=q_N^{\rm filt,L}+\overline{q_N^{\rm filt}}{}^{R}.
   \]
   The main scan uses \(w=0.5,1,2\), so its frequency width changes by a
   factor four.  This is the requested width study.
2. **Naive EFT-dictionary ledger.**  The finite operator chosen for the
   brief's \((i/2)\epsilon'\)-correction is
   \[
   q_N^{\rm led}(n,w)=
   \frac{\int dt\,g_\sigma(t)\left[
      \epsilon_n(t)H+\frac{i}{2}\epsilon_n'(t)[H,A_2(t)]
   \right]}{\int dt\,g_\sigma(t)},\qquad
   Q_N^{\rm led}=q_N^{\rm led,L}+\overline{q_N^{\rm led}}{}^{R}.
   \]
   Every term is a finite matrix.  The commutator is anti-Hermitian, so its
   displayed \(i/2\) multiple is Hermitian.  This is an explicitly declared
   naive dictionary, not a derived microscopic Schwarzian charge.

The three observables are \(B_\delta(0,0)\),
\(B_\delta(0,\beta/8)\), and
\(B_\delta(-\beta/10,\beta/10)\).  For each one, the comparison is made on
three normalized TFD-sector vectors: the TFD itself and two states obtained
with one regulated bilocal insertion.  Thus the insertion count is uniformly
bounded by one.  The JSON retains the complete \(3\times3\) complex matrix
of both \(i[Q_N,B]\) and \(\delta_\epsilon^{\rm biloc}B\) in every row.

The reported relative defect is exactly the projected matrix-element
mismatch requested in the brief:

\[
 d_N=\frac{\|M_N^{\rm cand}-M_N^{\rm target}\|_F}
 {\max\{\|M_N^{\rm cand}\|_F,\|M_N^{\rm target}\|_F\}},
 \quad
 (M_N^{\rm cand})_{ab}=\langle\Psi_a,i[Q_N,B]\Psi_b\rangle .
\]

The target matrix replaces \(i[Q_N,B]\) by
\(\delta_\epsilon^{\rm biloc}B\).  The denominator is symmetric between the
candidate and target and does not divide by a possibly vanishing individual
matrix element.  No amplitude is fitted.  The JSON also reports the stronger
unprojected action-norm defect on all three ket vectors.  With either
normalization, zero is exact agreement and an \(O(1)\) number is an \(O(1)\)
Ward mismatch.

## Numerical verdict

Neither candidate supplies a controlled \(r_N\to0\) on the accessible
sizes.  Across all 216 n=2 main rows, the projected matrix defect lies in
\([0.550069,1.012437]\), while the stronger action-norm defect lies in
\([0.645496,1.413977]\).  Both are unambiguously \(O(1)\).

The naive ledger selects the constant model at both temperatures.  Its mean
defect changes only \(0.80295\to0.80099\) at \(\beta J=5\) and
\(0.78739\to0.78603\) at \(\beta J=10\) from \(N_m=8\) to 12, far from a
decay toward zero.

The filtered result is even sharper: all six width/temperature scans select
the constant model, and every aggregated mean is within 0.0021 of one.  The
requested width change by a factor four therefore does not uncover a
decreasing defect.  The \(N_m=14,\beta J=10\), seed-3101 confirmation is
also \(O(1)\): 1.0006, 1.0006, 1.0034 for the filtered \(w=1\) candidate
and 0.8653, 0.9402, 0.5667 for the ledger.

| N_m=14 candidate | equal | unequal | symmetric |
|:---|---:|---:|---:|
| filtered, w=1 | 1.000644 | 1.000573 | 1.003378 |
| ledger, w=1 | .865337 | .940200 | .566663 |

This is evidence against these two explicit constructions, not a no-go
theorem for every parity-even finite-N approximant.  The sizes also do not
open a parametric conformal window: \(1\ll\beta J\ll N_m\) is not satisfied
uniformly.  The limit order tested is fixed \(\beta J\), fixed regulated
times in units of \(\beta\), then increasing \(N_m=8,10,12\), with a single
\(N_m=14\) check.  No late-time or strict Schwarzian limit is inferred.

## Scaling fits and fluctuation bands

At each \((N_m,\beta J,\text{candidate},w)\), the band is the mean and sample
standard deviation across three disorder seeds and three observables
(nine values).  The constant fit has one parameter.  The power fit
\(aN_m^{-p}\) has two, with \(p>0\).  Both use
\(\mathrm{AIC}=n\log(\mathrm{RSS}/\sum y^2)+2k\) on the same three means.
The AIC winner is reported even when the finite-size extrapolation is not
controlled.

| βJ | candidate | w | N=8 mean ± sd | N=10 | N=12 | AIC const | AIC power | p | reading |
|---:|:---|---:|:---|:---|:---|---:|---:|---:|:---|
| 5 | filtered | 0.5 | 1.0000 ± .0000 | 1.0001 ± .0002 | 1.0002 ± .0004 | -54.18 | -24.69 | .050 floor | saturation |
| 5 | filtered | 1 | 1.0000 ± .0000 | 1.0001 ± .0004 | .9998 ± .0007 | -52.24 | -24.79 | .050 floor | saturation |
| 5 | filtered | 2 | 1.0000 ± .0000 | 1.0000 ± .0001 | .9999 ± .0002 | -58.13 | -24.77 | .050 floor | saturation |
| 5 | ledger | 1 | .8029 ± .1878 | .8024 ± .1865 | .8010 ± .1870 | -39.28 | -25.50 | .050 floor | saturation |
| 10 | filtered | 0.5 | 1.0000 ± .0000 | 1.0006 ± .0012 | 1.0009 ± .0018 | -45.06 | -24.48 | .050 floor | saturation |
| 10 | filtered | 1 | 1.0000 ± .0000 | 1.0006 ± .0027 | .9993 ± .0042 | -43.52 | -24.93 | .050 floor | saturation |
| 10 | filtered | 2 | 1.0000 ± .0000 | 1.0013 ± .0042 | .9979 ± .0069 | -37.44 | -25.27 | .050 floor | saturation |
| 10 | ledger | 1 | .7874 ± .1719 | .7877 ± .1709 | .7860 ± .1729 | -40.04 | -25.24 | .050 floor | saturation |

The best-fit power exponent sitting at `.050 floor` means the power search
hit its lowest allowed positive exponent; the constant is already preferred.

## Control rows and numerical gates

The exact n=0 generator is \(Q_N=H_L+H_R\), passed through the same three
observables and three-state measurement pipeline at every main-grid point.
Its maximum defect is \(2.064995\times10^{-16}\), almost six orders of
magnitude below the required \(10^{-10}\) calibration line.

| N_m | max d0 at βJ=5 | max d0 at βJ=10 |
|---:|---:|---:|
| 8 | 2.065e-16 | 1.423e-16 |
| 10 | 1.655e-16 | 1.802e-16 |
| 12 | 1.692e-16 | 1.975e-16 |

The n=1 control uses the same candidate formulas at \(w=1\).  It is not an
exact finite-N charge gate, but it checks whether the expected conformal
constraint structure is already numerically visible.  The filtered family
remains at one.  The ledger is smaller, but stays \(O(0.38\)--0.48)
with no meaningful decrease from \(N_m=8\) to 12, so even this control does not show a
small microscopic Möbius defect on the available window.

| βJ | candidate | N=8 mean ± sd | N=10 | N=12 |
|---:|:---|:---|:---|:---|
| 5 | filtered | 1.0000 ± .0000 | 1.0000 ± .0001 | 1.0001 ± .0002 |
| 5 | ledger | .4758 ± .2391 | .4731 ± .2351 | .4704 ± .2318 |
| 10 | filtered | 1.0000 ± .0000 | 1.0001 ± .0004 | 1.0009 ± .0017 |
| 10 | ledger | .3849 ± .1132 | .3889 ± .1184 | .3904 ± .1205 |

The heat-kernel tests check \(\delta=0\) against the unregulated operator to
\(10^{-10}\), and \(\delta=10^5\) against the explicit ground-space
compression \(P_0AP_0\) to \(10^{-8}\).  Over main, n=1, and n=14 rows,
the maximum Hermiticity error is zero after roundoff-only symmetrization, the
maximum parity commutator is \(1.953\times10^{-14}\), and the largest
imaginary part of a nominally real diagonal matrix element is
\(1.735\times10^{-17}\).  Step doubling 24→48→96 gives observed quadrature
orders 1.876–2.050 (gate 1.70); the largest fine difference is
\(9.407\times10^{-6}\).

## Per-seed n=2 defect tables

Each entry is the relative Ward defect \(d_N\).  `equal`, `unequal`, and
`symmetric` refer respectively to the three regulated bilocals listed above.
The complete JSON additionally contains all nine complex matrix elements,
action norms, residual norms, and gate diagnostics for each row.

### Filtered, w=0.5, βJ=5

| N_m | seed | equal | unequal | symmetric |
|---:|---:|---:|---:|---:|
| 8 | 3101 | 1.000000 | 1.000000 | 1.000000 |
| 8 | 3102 | 1.000000 | 1.000000 | 1.000000 |
| 8 | 3103 | 1.000000 | 1.000000 | 1.000000 |
| 10 | 3101 | 1.000070 | 1.000007 | 1.000692 |
| 10 | 3102 | 1.000013 | 1.000003 | 1.000277 |
| 10 | 3103 | 1.000008 | 1.000002 | 1.000033 |
| 12 | 3101 | .999955 | .999979 | 1.000848 |
| 12 | 3102 | 1.000065 | 1.000016 | 1.000135 |
| 12 | 3103 | 1.000020 | .999997 | 1.000868 |

### Filtered, w=1, βJ=5

| N_m | seed | equal | unequal | symmetric |
|---:|---:|---:|---:|---:|
| 8 | 3101 | 1.000000 | 1.000000 | 1.000000 |
| 8 | 3102 | 1.000000 | 1.000000 | 1.000000 |
| 8 | 3103 | 1.000000 | 1.000000 | 1.000000 |
| 10 | 3101 | 1.000115 | 1.000007 | 1.001110 |
| 10 | 3102 | .999962 | 1.000000 | .999645 |
| 10 | 3103 | 1.000032 | 1.000006 | 1.000336 |
| 12 | 3101 | .999764 | .999969 | .998275 |
| 12 | 3102 | 1.000123 | 1.000017 | 1.000938 |
| 12 | 3103 | .999933 | .999990 | .999592 |

### Filtered, w=2, βJ=5

| N_m | seed | equal | unequal | symmetric |
|---:|---:|---:|---:|---:|
| 8 | 3101 | 1.000000 | 1.000000 | 1.000000 |
| 8 | 3102 | 1.000000 | 1.000000 | 1.000000 |
| 8 | 3103 | 1.000000 | 1.000000 | 1.000000 |
| 10 | 3101 | 1.000031 | 1.000001 | 1.000305 |
| 10 | 3102 | .999995 | 1.000000 | .999946 |
| 10 | 3103 | 1.000004 | 1.000001 | 1.000041 |
| 12 | 3101 | .999929 | .999992 | .999386 |
| 12 | 3102 | 1.000025 | 1.000003 | 1.000208 |
| 12 | 3103 | .999981 | .999997 | .999839 |

### Ledger, w=1, βJ=5

| N_m | seed | equal | unequal | symmetric |
|---:|---:|---:|---:|---:|
| 8 | 3101 | .864625 | .982554 | .561916 |
| 8 | 3102 | .864625 | .982838 | .561916 |
| 8 | 3103 | .864625 | .981519 | .561916 |
| 10 | 3101 | .864888 | .978042 | .564457 |
| 10 | 3102 | .864531 | .981040 | .560950 |
| 10 | 3103 | .864694 | .980211 | .562678 |
| 12 | 3101 | .864030 | .978403 | .556853 |
| 12 | 3102 | .864897 | .976898 | .564182 |
| 12 | 3103 | .864441 | .978818 | .560371 |

### Filtered, w=0.5, βJ=10

| N_m | seed | equal | unequal | symmetric |
|---:|---:|---:|---:|---:|
| 8 | 3101 | 1.000000 | 1.000000 | 1.000000 |
| 8 | 3102 | 1.000000 | 1.000000 | 1.000000 |
| 8 | 3103 | 1.000000 | 1.000000 | 1.000000 |
| 10 | 3101 | 1.000474 | 1.000030 | 1.003550 |
| 10 | 3102 | 1.000106 | 1.000170 | 1.001511 |
| 10 | 3103 | .999997 | 1.000029 | .999864 |
| 12 | 3101 | .999763 | .999998 | 1.004381 |
| 12 | 3102 | 1.000230 | 1.000152 | .999786 |
| 12 | 3103 | 1.000221 | 1.000064 | 1.003885 |

### Filtered, w=1, βJ=10

| N_m | seed | equal | unequal | symmetric |
|---:|---:|---:|---:|---:|
| 8 | 3101 | 1.000000 | 1.000000 | 1.000000 |
| 8 | 3102 | 1.000000 | 1.000000 | 1.000000 |
| 8 | 3103 | 1.000000 | 1.000000 | 1.000000 |
| 10 | 3101 | 1.000844 | 1.000187 | 1.007234 |
| 10 | 3102 | .999753 | .999960 | .997310 |
| 10 | 3103 | .999809 | 1.000308 | .999664 |
| 12 | 3101 | .998456 | .999308 | .989904 |
| 12 | 3102 | 1.000860 | 1.000429 | 1.006394 |
| 12 | 3103 | .999796 | .999805 | .998960 |

### Filtered, w=2, βJ=10

| N_m | seed | equal | unequal | symmetric |
|---:|---:|---:|---:|---:|
| 8 | 3101 | 1.000000 | 1.000000 | 1.000000 |
| 8 | 3102 | 1.000000 | 1.000000 | 1.000000 |
| 8 | 3103 | 1.000000 | 1.000000 | 1.000000 |
| 10 | 3101 | 1.001364 | 1.000285 | 1.012437 |
| 10 | 3102 | .999929 | .999944 | .998804 |
| 10 | 3103 | .999751 | 1.000264 | .999034 |
| 12 | 3101 | .997659 | .998857 | .981046 |
| 12 | 3102 | 1.000786 | 1.000449 | 1.006350 |
| 12 | 3103 | .999651 | .999650 | .996851 |

### Ledger, w=1, βJ=10

| N_m | seed | equal | unequal | symmetric |
|---:|---:|---:|---:|---:|
| 8 | 3101 | .864625 | .936750 | .561916 |
| 8 | 3102 | .864625 | .937445 | .561916 |
| 8 | 3103 | .864625 | .932701 | .561916 |
| 10 | 3101 | .865425 | .930519 | .569048 |
| 10 | 3102 | .864450 | .938404 | .559841 |
| 10 | 3103 | .864449 | .935232 | .561498 |
| 12 | 3101 | .863092 | .935832 | .550069 |
| 12 | 3102 | .865305 | .930591 | .567369 |
| 12 | 3103 | .864385 | .937629 | .559964 |

## MERGE PROPOSALS

None.  The result should remain linked as candidate-specific Layer-0
evidence: both tested n=2 families have an \(O(1)\), saturating Ward defect
on the accessible grid.  It neither constructs the G3
charge nor proves that every possible finite-N construction is obstructed, so
no campaign definition, theorem row, or status label should change from this
lane alone.
