# Work order — general-G soft index, strategy G2: intrinsic intertwiner route (bd tns-fea)

Parallel strategy 2 of 5 on the same target: the finite-volume soft index
identity (theory/soft-index-r2.md ⟨1⟩3, S-IDX-fin, currently SU(2)) for
GENERAL compact on-site symmetry. Strategy G1 (root-sl₂ reduction,
briefs/sidx-general-g-prover.md) runs in parallel — do NOT take that
route; your value is an INDEPENDENT attack. Survivors get hybridized
after critic rounds.

**Your route — top-down representation theory, no sl₂ reduction:**
formulate the projected-current identity intrinsically. The current zero
modes span (a copy of) 𝔤 acting on the sector; the soft-leg insertion is
an intertwiner between isotypic components of the G-module decomposition
of the finite chain. State and prove the identity as: the projected
current equals an explicit intertwiner, with the SU(2) operator
`A = D†D` replaced by the canonical positive operator on the multiplicity
space of the relevant isotypic component (Schur orthogonality does the
work the su(2) ladder algebra did). If Frobenius reciprocity / the
Clebsch–Gordan structure of (on-site rep)⊗N forces extra hypotheses,
display them minimally.

Process contract: PRD.md rules. Theorem → capped critic loop later;
OBSTRUCTION → sharp header + surviving weaker statement, NO rounds.
Honest labels per step.

READ: PRD.md, notation.md, definitions.md; theory/soft-index-r2.md §2
(what you must reduce to at G=SU(2)); theory/corner-a.md +
corner-a-goldstone.md (reuse their general-G registers); CLAIMS rows
ML4-Ward (+ERRATUM — check whether your intrinsic form has the
full-sector vs highest-weight register split; name both if so).

LANE (writable, NOTHING else): theory/soft-index-g2.md (CREATE),
theory/checks/soft_index_g2_check.py (CREATE: ED-verify your identity on
one non-SU(2) instance — SU(3) fundamental chain or SU(2)×U(1) — small N,
green exit 0 under python3 -O, no bare asserts, ≥1 structural red mode;
verify the G=SU(2) reduction numerically against soft_index_r2_check.py's
certified numbers), theory/soft-index-g2-notes.md (optional). No edits to
any existing file; MERGE PROPOSALS section for proposed rows. No commits.

Deliverable: (0) status header THEOREM(class)/OBSTRUCTION in first ten
lines; (1) setup; (2) L6b ladder; (3) SU(2) reduction check; (4) the
non-SU(2) instance; (5) checker section; (6) MERGE PROPOSALS. Write
sections as you complete them.
