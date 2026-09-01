<!-- LANE BRIEF: large-p Liouville rung of the microscopic ladder (bd tns-7wd).
     YOUR LANE (create/edit ONLY): theory/lanes/syk-jt/liouville-rung-report.md,
     plus (only if a computation genuinely needs code)
     numerics/src/syk_liouville*.jl, numerics/test/test_syk_liouville.jl,
     numerics/results/syk_liouville.json. No bd operations; shared-file
     edits only as MERGE PROPOSALS in your report. Work fully autonomously.
     If you write code: red-green TDD (L1), failing tests FIRST, shown
     failing. No network — all references are local TeX under refs/ (L3). -->

# Liouville rung: the decisive computation beyond the Schwarzian truncation

The Schwarzian-EFT results to test are the adjudicated claims **JT-B-susc /
JT-bfly-decay / JT-noplat-abs** in `claims/CLAIMS.md` (read the three rows
plus the verdict scoping in `theory/verdicts/syk-jt-joint-critic-r2.md` §8).
The question this rung answers, and only this rung can answer: **do the
calibrated-ratio plateau and the DC soft-residue identity survive when the
Schwarzian truncation is lifted** — i.e. in the large-p SYK collective
(Liouville) theory, where the full bilocal dynamics is retained at leading
order in 1/p — and at what order do corrections enter?

Read first, in order (all binding):

1. `theory/lanes/syk-jt/observables-spec.md` — the 3-layer C*-algebra
   observable spec; your detector must live in Layer 1 (uniform bilocals,
   E_L, E_R); iterated-limit convention C→∞ first, 1 ≪ κT ≪ κC.
2. `theory/lanes/syk-jt/t1-analytic.md` and `repair-r2-response.md` — the
   settled conventions you inherit: single synchronization event u_*,
   energy-balanced pulse as the claim-bearing protocol (unbalanced =
   formal diagnostic only), the equal-(E_L,E_R) reference discipline.
3. `theory/lanes/syk-jt/ed-rung-report.md` — the sibling rung's honest
   negative (window non-overlap at accessible N); your rung sits between
   ED and Schwarzian on the ladder.
4. `refs/arxiv-2412.14799` `Main.tex:291-311` — the Bucca–Mezei large-p
   embedding of the Schwarzian into the Liouville collective theory.
   Quote it from the local TeX, never from memory (L3).

## The computation

- Set up the two-dot large-p SYK problem in collective fields: TFD at
  inverse temperature β, coupled/uncoupled as the decisive computation
  requires, Liouville equation for the bilocal g(t1,t2) with its known
  large-p solution; state your normalization and the map to the
  Schwarzian regime explicitly (matching the Bucca–Mezei window).
- Pulse protocol: the energy-balanced pulse translated into the
  collective-field language (a sourced perturbation of the right dot with
  net right-energy change zero at the declared order); single u_*.
- Detector: the Layer-1 two-sided bilocal G_LR(T) and its equal-time
  grid; compute the absolute difference δG_LR(T) and the calibrated
  ratio Δu_rel(T) = −δG_LR/∂_T G^eq_LR in linear response.
- **Q1 (survival).** In the strict large-p limit: does Δu_rel(T) plateau
  and does the plateau equal the DC soft residue (the JT-B-susc
  identity), with the Schwarzian result recovered in the appropriate
  window? Derive, do not assume; the truncation-lifting terms are the
  point.
- **Q2 (correction order).** First correction: identify the leading
  parameter (1/p, 1/(βJ), 1/C — state the ordering of limits you use and
  why it is compatible with the C→∞-first convention) and whether it
  erodes the plateau (drift, decay, or preserved).
- **Q3 (butterfly register).** Does the JT-bfly-decay verdict (zero
  plateau for the Shenker–Stanford shift — transient, NOT memory)
  persist at large p? A sign that it does not would be a MAJOR result;
  treat with corresponding rigor.

Both outcomes of each question are results (L10). If the honest answer in
some window is "the large-p theory does not cleanly separate the scales,"
say so precisely — the ED rung's window non-overlap is the precedent.

## Form of the argument

Rigorous steps in Lamport structured style (L6b): numbered ⟨1⟩1, ⟨1⟩2, …
with ASSUME/PROVE, terminal QED, every leaf citing a D-number from
`definitions.md`, a claim id, or a named computation displayed in the
report. Physics-level steps (EFT matching, saddle evaluation) are
permitted where flagged as such — mark them [physical argument], never
silently.

## Output

`theory/lanes/syk-jt/liouville-rung-report.md`: conventions (every one
stated), the Lamport derivation, Q1–Q3 verdicts with honest window
discussion, structural comparison to the three JT-* claim rows and to the
ED rung's negative, MERGE PROPOSALS (if any) for CLAIMS.md rows — you do
not edit CLAIMS.md yourself. If you wrote code: standalone green
`julia --project=numerics numerics/test/test_syk_liouville.jl`, modules
200–500 loc, JSON through a finiteness gate (nonzero exit on NaN; never
write JSON on a failing run).
