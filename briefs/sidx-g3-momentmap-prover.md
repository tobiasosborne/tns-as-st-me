# Work order — general-G soft index, strategy G3: moment-map / geometric route (bd tns-fea)

Parallel strategy 3 of 5 on the same target: the finite-volume soft index
identity (theory/soft-index-r2.md ⟨1⟩3, S-IDX-fin, currently SU(2)) for
GENERAL compact on-site symmetry. Strategies G1 (root-sl₂) and G2
(intertwiner) run in parallel — take NEITHER route. Survivors get
hybridized after critic rounds.

**Your route — the symplectic/Kähler program (TJO's, docs/framing.md +
briefs/bta-kahler-target.md):** treat the charge data as a moment map for
the G-action on the relevant finite-dimensional state manifold (projective
space of the sector, or the MPS manifold at fixed bond dimension). The
index identity should be the statement that the soft-leg insertion shifts
the moment-map value by an exactly quantized increment — the
finite-dimensional avatar of "memory quantum = moment-map increment"
(tns-89h). Available tools: equivariant convexity (the Kirwan/GS image is
a convex polytope whose vertices are weights — connect to corner A's Weyl
walls, which the campaign already owns), and equivariant localization if
it genuinely computes the index. If the geometric statement only
REPRODUCES the algebraic identity without adding generality, say so — that
is an honest negative and stops the line (PRD negative-results rule).

Process contract: PRD.md rules; honest labels; OBSTRUCTION → sharp header,
NO rounds.

READ: PRD.md, docs/framing.md, briefs/bta-kahler-target.md, notation.md,
definitions.md; theory/soft-index-r2.md §2; theory/corner-a.md (Weyl-wall
rows); CLAIMS rows ML4-Ward (+ERRATUM), M-INDEX-fin (the memory-side index
whose geometric meaning you are after).

LANE (writable, NOTHING else): theory/soft-index-g3.md (CREATE),
theory/checks/soft_index_g3_check.py (CREATE: verify the quantized
moment-increment claim by ED on one instance beyond SU(2); green exit 0
under python3 -O, no bare asserts, ≥1 red mode), theory/soft-index-g3-notes.md
(optional). No edits to existing files; MERGE PROPOSALS section. No
commits.

Deliverable: (0) status header in first ten lines — THEOREM(class) /
OBSTRUCTION / REPRODUCTION-ONLY (the geometric route adds no generality);
(1) setup; (2) ladder; (3) SU(2) reduction; (4) instance; (5) checker;
(6) MERGE PROPOSALS. Write sections as you complete them.
