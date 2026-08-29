# Work order — 2+1 wave, lane W2: the anyonic label index (bd tns-2p1)

Transplant the label side of the campaign to genuinely 2+1 topological
order, where `theory/cat-hunt.md` (RESULT, read in full) says the datum
lives: a string-operator endpoint in a 2D lattice model carries a fusion
channel; the index should be a Drinfeld-center (anyon) sector datum.

Your job: state and prove a FINITE-LATTICE selection-rule theorem for
string-operator endpoints in an exactly computable 2+1 model, in the
shape of the campaign's label theorems: (i) the endpoint datum is a
definite anyon sector; (ii) a charge-created TPM-style protocol
measuring flux through a boundary circle has outcomes quantized in the
sector lattice; (iii) the invertible/abelian case gives a group-valued
index (toric code: Z/2 x Z/2 e-m lattice), the non-abelian case
(S3 quantum double or Ising string-net) gives the fusion-channel datum
with the universal-grading shadow of cat-hunt §4. Prove what is exactly
provable in the chosen model (toric code string algebra is exact — use
it); label the model-general statement honestly (likely SKETCH with the
PEPS pulling-through hypothesis displayed).

Process: PRD.md; RESULT/PROGRAM/OBSTRUCTION header; negative → no
rounds. Fences: cat-hunt ledger items 1 and 8 are binding (no naive
center-label subtraction; no packaging theorem). Do not touch 1D rows.

READ: PRD.md; theory/cat-hunt.md IN FULL; theory/soft-index-general.md
(the label theorem being transplanted); claims rows S-IDX-G-label,
M-INDEX-fin (the TPM coset-integrality mechanism — its donor proof);
refs/arxiv-2011.12127 (PEPS symmetries, local TeX; L3 for any quote).

LANE (writable, NOTHING else): theory/anyon-label-index.md (CREATE),
theory/checks/anyon_label_check.py (CREATE: exact toric-code
computation on a small torus — string endpoints, braiding phases, the
protocol outcome lattice; green exit 0 under python3 -O, no bare
asserts, ≥1 red mode e.g. wrong-sector mutation), notes file optional.
No edits to existing files; MERGE PROPOSALS. No commits.

Deliverable: (0) header + the one-sentence theorem; (1) setup (model,
registers); (2) the exact toric-code theorem, full proof; (3) the
non-abelian instance as far as one session allows; (4) the honest
model-general SKETCH; (5) checker; (6) MERGE PROPOSALS. Write as done.
