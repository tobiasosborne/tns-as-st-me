# Work order — 2+1 wave, lane W1: is the operator theorem dimension-free? (bd tns-2p1)

The cheapest possible 2+1 theorem. `theory/soft-index-general.md` /
claims row S-IDX-fin-G proves the projected-current Ward identity on a
finite periodic RING via weight-sector algebra: sl2 triples per root,
Gram operator A = D†D, both registers. Hypothesis to test: **no step uses
one-dimensionality** — the proof should hold verbatim on any finite
G-symmetric lattice (2D torus, arbitrary finite graph with finite-range
G-invariant Hamiltonian and a displayed current zero mode).

Your job: (a) walk the proof of S-IDX-fin-G step by step; for each leaf,
verify dimension-independence or name the 1D-only input; (b) if
dimension-free, state and prove the general-lattice theorem (minimal
diff from the existing ladder — cite its steps, do not recopy them);
(c) ED-verify on a small 2D instance (e.g. SU(2) Heisenberg on a 2x3 or
3x3 torus, and one SU(3) 2x2 instance), reproducing the register split
and the Ward residue; (d) also check the label theorem S-IDX-G-label for
dimension-independence (expected: trivially yes — say so in one line if
so, per the hygiene rule).

Process: PRD.md. THEOREM → capped loop later; a genuine 1D-only
obstruction → sharp OBSTRUCTION header, no rounds. Honest labels.

READ: PRD.md; theory/soft-index-general.md; theory/soft-index-g.md;
theory/soft-index-r2.md §2; claims rows S-IDX-fin-G, S-IDX-G-label;
definitions.md D10 (the current-zero-mode register — check whether ITS
definition is 1D-bound and, if so, what the honest 2D replacement is;
that is the most likely hiding place for a 1D assumption).

LANE (writable, NOTHING else): theory/soft-index-2d.md (CREATE),
theory/checks/soft_index_2d_check.py (CREATE: 2D ED instances, green
exit 0 under python3 -O, no bare asserts, ≥1 structural red mode),
theory/soft-index-2d-notes.md (optional). No edits to existing files;
MERGE PROPOSALS section. No commits.

Deliverable: (0) header THEOREM(any finite lattice)/OBSTRUCTION(the 1D
input, named) in ten lines; (1) the leaf-by-leaf dimension audit as a
table; (2) the general statement + proof-by-citation; (3) the 2D ED
instances; (4) checker; (5) MERGE PROPOSALS. Write sections as done.
