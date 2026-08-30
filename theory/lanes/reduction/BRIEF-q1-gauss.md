<!-- LANE BRIEF Q1: definitional audit, corner A vs 3+1 lattice QED.
     TJO directive 2026-08-30: "I am suspicious of the definitions... until
     there is a somewhat compelling quantitative analytic argument that the
     definitions have something to do with the accepted continuum limit under
     an appropriate sequence of limits I am unhappy. The most compelling
     argument would be to connect to 3+1 QED on the lattice. Heuristic
     arguments are ok, but I want to see what the discrete vs continuous
     definitions say about each other."
     Output: theory/lanes/reduction/q1-gauss.md, written INCREMENTALLY. -->

# Q1: Do the campaign's asymptotic-symmetry DEFINITIONS instantiate correctly in 3+1 lattice QED?

## Inputs

- `definitions.md` D1–D4 (window vectors; on-site symmetry and intertwiners;
  D3 truncated/modulated symmetry operations with admissible profiles; D4
  bond implementers, effective asymptotic symmetry, charge algebra) and D10
  (lattice Noether pair). `claims/CLAIMS.md` rows WI, A1, A2 for what is
  proved about these definitions.
- `refs/arxiv-1703.05448/soft_Arxiv_update.tex` (LOCAL TeX — the canon):
  the QED chapters — large gauge transformations, the asymptotic charges
  Q_ε = Q_soft + Q_hard, antipodal matching, the Ward identity ⇔ Weinberg
  soft theorem. Quote every continuum definition you use with file+line.
- `docs/framing.md` (the potential-is-fundamental viewpoint).
- Hamiltonian (Kogut–Susskind) compact-U(1) lattice gauge theory may be
  stated from standard knowledge, flagged [textbook]; note that 3+1 compact
  U(1) has a Coulomb phase at weak coupling so the photon and the Weinberg
  pole are meaningful targets. Do NOT fetch arXiv ids from memory; if you
  fetch anything, verify its title from its own TeX first.

## Task

Build the three-column definitional dictionary, quantitatively:

1. **Campaign definition, instantiated.** The campaign's setting is a GLOBAL
   on-site symmetry. Transplant each definition to lattice QED: what is the
   truncated symmetry U_R(g) when the symmetry is gauged? Show that the
   Gauss law G_x = (div E)_x − ρ_x makes the truncated transformation on a
   region R act as boundary operators on ∂R links — the gauge-theory avatar
   of the proved telescoping identity (WI): charge in a region is a boundary
   observable. Make the parallel exact: campaign bond implementer V(g) on
   the cut bond ↔ which lattice-QED boundary operator (e^{iε E_ℓ} on
   boundary links)? The campaign's endpoint algebra / effective asymptotic
   group ↔ the boundary gauge group Maps(∂Λ, U(1)) modulo which subgroup?
   Where the analogy is NOT exact (a global symmetry has no local
   constraint; the campaign's virtual/bond space is not a gauge edge mode),
   say so precisely — the differences are as much the deliverable as the
   matches.
2. **Limit sequence.** State an explicit sequence of limits (lattice spacing
   a → 0, volume → ∞, boundary sphere radius → ∞, profile ε_x → ε(ẑ)
   angle-dependent) under which the lattice boundary charges converge,
   heuristically but quantitatively (write the Riemann-sum-to-flux-integral
   convergence explicitly), to the accepted continuum asymptotic charge
   Q_ε = (1/e²)∮ d²z γ_{z z̄} ε F_ru + hard part as defined in 1703.05448.
   Identify which campaign definitional clauses (D3's admissible-profile
   classes, D4's padding) are the finite-a shadows of which continuum
   falloff/smoothness conditions on ε.
3. **Verdict per definition** (D3, D4, D10, WI-as-definition): the discrete
   and continuous definitions DO / DO NOT say the same thing under the
   stated limits, with the precise sense and the residual gaps.

## Rules

Physics register; [physical argument]/[textbook] flags on unproved steps;
continuum quotes from local TeX with file+line; campaign statuses unchanged;
no edits outside theory/lanes/reduction/; no bd operations; no LEDGER edits.
