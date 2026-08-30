<!-- LANE BRIEF Q2: definitional audit, corner B (memory) vs 3+1 lattice QED.
     TJO directive 2026-08-30: the definitions themselves are under audit —
     show quantitatively what the discrete and continuous memory DEFINITIONS
     say about each other under an appropriate sequence of limits. Heuristics
     ok. Output: theory/lanes/reduction/q2-memory-defs.md, INCREMENTALLY. -->

# Q2: Do the campaign's memory DEFINITIONS discretize the accepted electromagnetic memory?

## Inputs

- `definitions.md` D13 (windowed wall position and its dresses), D26
  (circle-integral on-site charge, the (INT) clause), D27 (the
  two-projective-measurement protocol and local relaxation, clauses LR1–LR3).
- `claims/CLAIMS.md` rows M-INDEX-fin, M-INDEX-spec, M-flux for what is
  proved about these definitions.
- `refs/arxiv-1703.05448/soft_Arxiv_update.tex` (LOCAL TeX): the
  electromagnetic memory section — the memory field, the velocity kick
  Δv = (e/m)∫dt E, the relation to the DC gauge-potential jump ΔA at null
  infinity. Quote with file+line.
- `refs/arxiv-1411.5745/memory_4.tex`: the operational detector definition.
- Kogut–Susskind compact U(1) from standard knowledge, [textbook]-flagged.
  In the Hamiltonian formulation the link variable is an ANGLE θ_ℓ (compact)
  with conjugate integer electric field E_ℓ ∈ ℤ. Do not fetch ids from
  memory; verify any fetched title from its own TeX.

## Task

1. **The lattice-QED memory observable, defined honestly.** In compact
   Hamiltonian lattice QED the natural memory observables are (i) the net
   change of the link angle θ_ℓ (the time-integrated electric force — the
   discretization of ΔA, the accepted memory field), and (ii) the velocity/
   momentum kick of a charged test particle. Work out: because the gauge
   group is compact, θ_ℓ is circle-valued and its conjugate E_ℓ has INTEGER
   spectrum. Compare clause by clause with the campaign's D26 (circle
   charge, spectrum in κ+ℤ): is D26 exactly the compactness statement,
   transplanted? Show the correspondence quantitatively (the spectrum
   statements, the coset structure, the role of the background/offset).
2. **Quantized vs continuous memory across the limit.** The accepted
   continuum EM memory ΔA is ℝ-valued and continuous. Trace exactly how the
   circle-valued/integer lattice structure becomes ℝ-valued: the weak-
   coupling/decompactification limit (e → 0 with physical fields fixed, the
   angle θ = a e A with a → 0), including where the integer quantization of
   the campaign's escaped-charge law goes (per-quantum units vanishing vs
   charge quantization surviving). This is the direct "what the discrete
   and continuous definitions say about each other" deliverable.
3. **The TPM protocol vs the operational definition.** The accepted memory
   is operational: compare detector data before and after the radiation
   epoch. The campaign's D27 protocol is: measure the windowed charge
   projectively at early and late Cesàro times. Argue quantitatively
   (heuristics fine) that D27 is a discretization of the accepted
   operational definition — or identify exactly where it differs (Cesàro
   vs pointwise; projective charge measurement vs position/velocity
   readout; window vs local detector) and what each difference does in the
   continuum limit. The known Tauberian gap (bd tns-94g) may be cited.
4. **Verdict per definition** (D13, D26, D27): same thing under the stated
   limits / same up to listed gaps / different objects (and then what the
   campaign's object corresponds to in QED language, if anything).

## Rules

Physics register; [physical argument]/[textbook] flags; continuum quotes
from local TeX with file+line; statuses unchanged; no edits outside
theory/lanes/reduction/; no bd operations; no LEDGER edits.
