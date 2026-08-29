# Work order — general-G soft index, strategy G4: superselection route (bd tns-fea)

Parallel strategy 4 of 5 on the same target: the finite-volume soft index
identity (theory/soft-index-r2.md ⟨1⟩3, S-IDX-fin, currently SU(2)) for
GENERAL compact on-site symmetry. Strategies G1 (root-sl₂), G2
(intertwiner), G3 (moment map) run in parallel — take NONE of those
routes. Survivors get hybridized after critic rounds.

**Your route — the M-INDEX playbook transplanted:** the memory corner was
proved channel-free by symmetry/superselection alone (M-INDEX-fin: coset
integrality of the windowed charge, unconditional; LD-ID: the window
charge as the lift of a conserved sector datum). Do the same for the soft
index: derive the finite identity from the superselection/coset structure
of the charge-created sector — the soft datum as a difference of sector
labels, integrality from the coset lattice of the unbroken subgroup's
center (corner A's language, which is ALREADY general-G) — without
weight-sector combinatorics and without ladder operators. If this works it
is the most conceptual proof and the closest to the campaign's spine
("symmetry quantizes"). Key risk to confront honestly: the SU(2) identity
(R2.1) is an OPERATOR identity, not just an integrality statement — can
the superselection route produce the operator form, or only its spectral
consequence? If only the latter, state exactly which half of S-IDX-fin
you recover; a clean split is a hybridization-ready result, not a
failure.

Process contract: PRD.md rules; honest labels; OBSTRUCTION → sharp
header, NO rounds.

READ: PRD.md, notation.md, definitions.md; theory/soft-index-r2.md §2;
theory/memory-index.md (the playbook you are transplanting — especially
how M-INDEX-fin avoids channel inventories); theory/ace-ld.md (LD-ID);
theory/corner-a.md + corner-a-goldstone.md; CLAIMS rows M-INDEX-fin,
LD-ID, ML4-Ward (+ERRATUM).

LANE (writable, NOTHING else): theory/soft-index-g4.md (CREATE),
theory/checks/soft_index_g4_check.py (CREATE: ED on one non-SU(2)
instance; green exit 0 under python3 -O, no bare asserts, ≥1 red mode;
SU(2) reduction cross-checked against soft_index_r2_check.py numbers),
theory/soft-index-g4-notes.md (optional). No edits to existing files;
MERGE PROPOSALS section. No commits.

Deliverable: (0) status header in first ten lines — THEOREM(class) /
PARTIAL (named half of S-IDX-fin recovered) / OBSTRUCTION; (1) setup; (2)
ladder; (3) SU(2) reduction; (4) instance; (5) checker; (6) MERGE
PROPOSALS. Write sections as you complete them.
