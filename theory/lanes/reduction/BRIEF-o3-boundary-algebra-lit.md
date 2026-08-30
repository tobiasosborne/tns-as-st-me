<!-- LANE BRIEF O3: the boundary-observables literature (Naaijkens; Jones,
     Penneys, Wallick; Ogata; PEPS physicists) vs the campaign's boundary
     algebra. TJO 2026-08-30: this school has "somewhat advanced the theory
     of boundary observables for lattice systems" — connect it to the
     campaign's corner A and the operational directive (representation data
     are not operational; only observable/implementable quantities are; the
     injective-MPS boundary algebra passes).
     Output: theory/lanes/reduction/o3-boundary-algebra-lit.md, INCREMENTALLY. -->

# O3: the operator-algebraic boundary-observables literature and the campaign

## Fetching (L3 discipline, strict)

Fetch TeX from https://arxiv.org/e-print/<id> with 3-second waits; VERIFY
each title from the fetched TeX itself before use; store under
refs/arxiv-<id>/. Do NOT edit refs/LEDGER.md — record id, verified title,
and main tex file in YOUR OUTPUT; the orchestrator reconciles the ledger.
Ids verified by orchestrator web search 2026-08-30 (still re-verify titles):

- 2307.12552 — Jones, Naaijkens, Penneys, Wallick, "Local topological order
  and boundary algebras" (axioms via nets of local ground-state projections;
  boundary nets on Z^{k-1}; toric code and Levin-Wen instances).
- 2410.21454 — "Superselection sectors for posets of von Neumann algebras"
  (CMP 2025; verify authors from TeX).
- 2509.23734 — "Haag Duality for 2D Quantum Spin Systems".
- 2510.23790 — "On Symmetry-Compatible Superselection Structures for
  Product States in 2D Quantum Spin Systems" (claims equivalence with
  Naaijkens–Ogata constructions; verify).
- OPTIONAL, only if load-bearing for your mapping and found by title search
  (never from memory): Fiedler–Naaijkens "Haag duality for Kitaev's quantum
  double model for abelian groups"; the JMP "Boundary algebras of the
  Kitaev quantum double model"; Naaijkens 1311.2717 lecture notes;
  Cirac–Poilblanc–Schuch–Verstraete "Entanglement spectrum and boundary
  theories with projected entangled-pair states" (the physicists'
  bulk-boundary PEPS counterpart). Each must be title-verified.

Existing local refs that bear on this: the Ogata batch (refs/LEDGER.md
"OGA-*" rows — SPT index, split property, LSM), refs/arxiv-0802.0447
(string order), refs/arxiv-2011.12127 (MPS review).

## Campaign inputs

theory/corner-a.md and theory/corner-a-kinks.md (the boundary/endpoint
algebra, A1's PGL(χ)-torsor and non-implementability clause, A2's sector
theory); definitions.md D1(e,e′), D4, D9; claims/CLAIMS.md rows A1, A2,
M-INDEX-LA-folium, A-INDEX-TC-fin, A-INDEX-PEPS, SHAPE-FLAT, M-INDEX-2D-fin;
theory/anyon-label-index.md and theory/anyon-selection-hybrid.md (the 2+1
rows this literature most directly touches); docs/novelty-sweep.md (what the
original novelty sweep did and did not cover);
theory/verdicts/reduction-defs-adjudication-r1.md incl. amendment r1a; the
operational directive (bd memory tjo-2026-08-30-vital-binding).

## Tasks

1. **What they prove, precisely.** For each fetched paper: the objects
   (nets of boundary algebras from local ground-state projections; cone
   algebras; (approximate) Haag duality; DHR-type superselection categories
   for lattice systems), the hypotheses (which models, which dimensions,
   injectivity/LTO axioms), and the theorems — quoted with file+line.
2. **Operational grounding.** Their boundary algebras are built from
   physical local observables and ground-state projections — assess
   carefully whether this school supplies exactly the operational
   foundation TJO's directive demands for boundary observables (and where
   it too leans on non-operational scaffolding, if anywhere). Relate to
   the campaign's injective-MPS boundary algebra: is the campaign's
   endpoint algebra (A1) a 1D instance of, equivalent to, or genuinely
   different from their boundary-net construction? If a precise bridge is
   statable (even heuristically), state it.
3. **The DHR/sector comparison.** Corner A's A2 (double-coset vacuum-pair
   classification, weak-* sector jumps) and the folium implementer row
   versus their superselection machinery (posets of von Neumann algebras,
   Naaijkens–Ogata sectors, approximate Haag duality). What does the
   campaign's global-symmetry MPS setting add (the H² class as central
   extension of the ASYMPTOTIC symmetry; the memory/soft links), and what
   does their framework already have that corner A should cite or import
   (Haag duality as the missing rigor behind "boundary algebra = all there
   is at the cut")?
4. **The 2+1 rows.** The conditional PEPS selection row's (PT) hypotheses
   are representation-level (operational directive). Does the
   JNPW/LTO-axiom framework supply an OPERATIONAL replacement (axioms on
   ground-state projections rather than on tensors) under which the
   campaign's anyon-label and selection statements could be restated or
   even discharged? Say what a restatement would look like and what is
   missing.
5. **Novelty and citation audit.** Honestly: does anything in this
   literature anticipate a campaign claim (the endpoint-label index, the
   boundary-algebra operationality, the sector bookkeeping)? List every
   citation the labbook and the Letter now owe, per corner. The original
   novelty sweep predates this audit — flag anything it missed.
6. **Verdict:** three lines — what to import, what to cite, what (if
   anything) is threatened.

## Rules

Physics register with [physical argument] flags where you go beyond the
sources; quotes with file+line from fetched TeX; statuses unchanged; edits
only in theory/lanes/reduction/ plus new refs/arxiv-<id>/ directories; no
bd operations; no LEDGER edits (record fetches in output).
