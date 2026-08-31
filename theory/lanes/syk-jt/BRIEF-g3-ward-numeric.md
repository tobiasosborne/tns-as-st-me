<!-- LANE BRIEF G3-WARD-NUMERIC (bd tns-cru). YOUR LANE (create/edit
     ONLY): numerics/src/syk_ward.jl (may split syk_ward_*.jl),
     numerics/test/test_syk_ward.jl, numerics/results/syk_ward.json,
     theory/lanes/syk-jt/g3-ward-report.md. You may `include` and CALL
     numerics/src/syk_ed.jl (read it first; reuse its model builders,
     TFD, evolution) but MUST NOT edit it — needed changes go as MERGE
     PROPOSALS in your report. No bd operations. Red-green TDD (L1):
     failing tests first, RED output kept. Work fully autonomously. -->

# G3-ward-numeric: measure the Ward defect of candidate n=2 charges at Layer 0

Context: problem **G3** and estimate shape **G6** of
`theory/lanes/syk-jt/corner-a-precision.md` (read §4.1, G3, G6;
binding frame `theory/lanes/syk-jt/observables-spec.md`). Question: for
candidate parity-even finite-N charges Q_N[ε_{2,c}] (ε_{2,c}=cos 2τ on
the thermal circle, i.e. frequency 2·(2π/β) in real time — state your
Euclidean/Lorentzian frequency convention explicitly), does the Ward
defect

  D_N(A,Ψ) := ⟨Ψ, ( i[H_N, Q_N] · acting-as-δ-mismatch ) Ψ⟩

— more precisely: the mismatch between i[Q_N, A] matrix elements and the
target bilocal variation δ^biloc_{ε_{2,c}} A of memo eq. (4.2), on
TFD-sector states with a bounded number of bilocal insertions — decay
with N (a candidate r_N → 0) or stay O(1)? You are BLIND to the two
analytic lanes; your independence is the point.

## Candidate families (implement at least these two; add a third if cheap)

1. **Frequency-filtered bilinear**: Q_N^{(1)} := ∫ dt w(t) e^{iHt} A_2
   e^{−iHt} with A_2 a fixed even hermitian 2-body bilinear (state it;
   use the ED lane's operator conventions) and w a smooth window whose
   Fourier content is concentrated at the mode-2 thermal frequency;
   state the window and its width, and study defect vs width.
2. **EFT-dictionary candidate**: the discretized Schwarzian-ledger
   expression for the n=2 mode with H substituted for the energy
   density — the naive ε(t)H + (i/2)(ε'-correction) form evaluated as a
   finite time-quadrature of Heisenberg-evolved even operators; make
   every term an explicit finite-N operator.

For each: (i) verify parity-evenness and hermiticity (test); (ii)
measure i[Q_N, A] vs δ^biloc A for 2–3 regulated bilocal observables A
(equal-time and unequal-time two-sided fermion bilocals, heat-kernel
regulated per memo (4.3) — implement the e^{−δH} smearing exactly);
(iii) tabulate the relative Ward defect across N_m ∈ {8,10,12}
(N_m=14 confirmation if runtime allows), βJ ∈ {5,10}, ≥3 disorder
seeds; (iv) fit defect vs N_m (decaying? power? saturating?) with the
same AIC discipline as prior lanes; (v) CONTROL ROWS: run the identical
pipeline for the Möbius modes ε_0 = 1 (where Q_N = H is exact and the
defect must vanish to machine precision — this is your calibration red
line) and ε_{1,c} = cos τ (where the constraint structure should make
the defect small in the conformal window) — a candidate family whose
n=0 control fails is a broken pipeline, not a physics result.

## Tests (RED first)

n=0 exactness gate (defect < 1e-10); hermiticity/parity gates;
heat-kernel regulator correctness (δ → 0 and δ → ∞ limits sane, state
and test both); step/quadrature convergence for the time integrals
(order gate); finiteness/exit discipline (nonzero exit on NaN/empty/
gate violations; never write JSON on a failing run). Standalone green:
`julia --project=numerics numerics/test/test_syk_ward.jl`.

## Output

`theory/lanes/syk-jt/g3-ward-report.md`: conventions (all stated), RED
evidence, defect tables per (candidate, A, N_m, βJ, seed), the
decay-vs-saturation verdict per candidate with fluctuation bands,
control-row results, honest window discussion, MERGE PROPOSALS. JSON
through the finiteness gate. Both outcomes are results: a saturating
defect feeds the obstruction case; a decaying one feeds the
construction case. NO claims, NO statuses.
