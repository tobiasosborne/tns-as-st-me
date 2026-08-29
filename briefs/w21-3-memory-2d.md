# Work order — 2+1 wave, lane W3: the 2D memory index (bd tns-2p1)

Transplant the MEMORY corner to 2D. The donor is M-INDEX-fin
(unconditional finite-window coset integrality of the TPM escaped-charge
law, claims row + theory/memory-index.md — read the proof, it is
channel-free superselection and should not care about dimension) and
M-INDEX-spec (the conditional limit law).

Your job: (a) state the 2D TPM protocol honestly — window = disk/annulus
on a 2D lattice with on-site compact G (0-form) symmetry, SSB vacuum
pair or symmetric vacuum, escaped charge through the boundary; (b) prove
the 2D M-INDEX-fin analogue (expected: the donor proof transplants with
the window poset changed — do the transplant explicitly, leaf by leaf,
citing the donor); (c) identify what changes in the LIMIT law: in 2D the
(LR)/tightness clauses live on a 2D exhaustion, boundary terms scale
like the perimeter — state the honest 2D D27-analogue and which clauses
survive; (d) the genuinely 2D question, treat as exploration: for a 2D
SSB phase with gapless Goldstone modes (2D ferromagnet/antiferromagnet),
does the escaped-charge law still have integer support at finite window
(it must, by superselection) and what replaces the kink transport
picture — spin-wave radiation memory? One small ED or exact spin-wave
computation probing this is worth more than prose.

Process: PRD.md; honest header; negative → no rounds. Do not claim any
1-form-symmetry or topological-order result — that is lane W2's turf;
this lane is 0-form symmetry in 2D.

READ: PRD.md; theory/memory-index.md (donor); claims rows M-INDEX-fin,
M-INDEX-spec, LR1-GEN (its three-input proof is dimension-free on its
face — check and say so); definitions.md D26, D27.

LANE (writable, NOTHING else): theory/memory-index-2d.md (CREATE),
theory/checks/memory_index_2d_check.py (CREATE: small 2D ED, green exit
0 under python3 -O, no bare asserts, ≥1 red mode), notes optional. No
edits to existing files; MERGE PROPOSALS. No commits.

Deliverable: (0) header: which rows transplant clean / which change /
what is genuinely open in 2D; (1) protocol + definitions by pointer;
(2) the transplanted finite theorem; (3) the limit-law audit; (4) the
Goldstone-memory probe; (5) checker; (6) MERGE PROPOSALS. Write as done.
