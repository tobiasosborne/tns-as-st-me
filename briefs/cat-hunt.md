# Work order — SPECULATIVE HUNT: categorical formulation of the soft index (fusion categories / MPO symmetry / SPT) — TJO 2026-08-29

TJO's question: the general-compact-G soft index campaign went suspiciously
smoothly — is a more general principle at work, with the result admitting a
categorical formulation via fusion categories and SPT? Your job: find the
real categorical statement, or establish honestly that none is
non-artificial. Same discipline as the DH hunt (theory/dh-hunt.md — read
it as the format exemplar): RESULT / PROGRAM / NOTHING NON-ARTIFICIAL in
the header; negative outcome ends the line, no rounds (PRD.md).

## THE SIGNAL (from today's own artifacts — start here)

1. `theory/soft-index-g-boundary.md` item 2 + gate G5-C2-FINITE: for
   finite groups the current-zero-mode identity is replaced by an exact
   string-endpoint identity (computed, residual 0.00e+00). String/endpoint
   operators ARE the MPO-symmetry register.
2. `theory/soft-index-general.md` / claims row S-IDX-G-label: the soft
   index as a character-group difference of the effective unbroken center
   — pure superselection, the part fusion categories axiomatize.
3. The campaign's SPT machinery (theory/spt-rebuild.md, rows SPT-E'/-T'/
   -D'; refs/arxiv-0802.0447, refs/arxiv-1412.5604, refs/arxiv-2011.12127
   — local TeX present, L3 quoting allowed) already extracts edge data by
   MPO intertwiners.

## THE QUESTION, sharpened

Formulate the soft index for an MPO/fusion-category symmetry C on a spin
chain (D1-class MPS vacua). Candidate shape: the charge-created string
endpoint carries a definite sector (tube algebra / Drinfeld center Z(C)
label, or endpoint-module class), and the finite soft index is the
difference of these labels — reducing to S-IDX-G-label when C = Rep(G) or
Vec_G (check BOTH reductions: the invertible/pointed case must give the
group character lattice; the Rep(G) case must give the effective-center
characters). Then confront the operator half honestly: the Gram-inverse
identity S-IDX-fin-G consumed a DERIVATIVE of the symmetry (current zero
modes). Determine whether a categorical analogue exists (conditional
expectation / Jones-Wenzl projector / weak-Hopf integral in place of the
sl_2 ladder) or whether the operator theorem is genuinely Lie — a proved
split of that kind is a RESULT, not a failure.

## THE 2+1 TARGET (TJO, same day — this is why the hunt is strategic)

The campaign's eventual 2+1D lift will have no global group in general:
sectors are anyonic, symmetry is a fusion category acting by MPO/PEPS
intertwiners, and the tube algebra / Drinfeld center is the native label
set. Write the 1D categorical statement so that its 2+1 lift is visible:
prefer formulations whose ingredients (endpoint modules, center sectors,
conditional expectations) have known PEPS/anyon counterparts, and flag
any step that is genuinely 1D-only (e.g. anything leaning on the chain
order or on a bipartition into two half-lines). A short SPECULATIVE
subsection sketching the 2+1 shape of your best candidate is in scope.

## Non-artificial test (binding)

The categorical statement must either (a) cover a case no current row
covers (finite/non-invertible symmetry with actual content), with at
least one instance computed (small-N ED or exact MPO algebra — e.g.
Vec_{Z/2} / Ising-fusion / Rep(S_3)), or (b) prove the unifying reduction
theorem that makes S-IDX-G-label, the G5 finite-group endpoint identity,
and an SPT-E' edge statement corollaries of ONE categorical theorem.
Rewriting S-IDX-G-label in categorical vocabulary with no new case and no
unification is the G3 failure mode — terminal.

## FENCES

- Do not relabel or restate existing SPT rows (SPT-E' deliberately
  disclaims deformation constancy; respect its scoping).
- Memory-side claims only if they transplant a PROVED mechanism with the
  hypotheses displayed (M-INDEX-fin's superselection proof is the donor).
- L3: quotes from refs/ TeX only.
- Honest labels; SPECULATIVE sections marked.

## LANE (writable; NOTHING else)

- theory/cat-hunt.md (CREATE)
- theory/checks/cat_hunt_check.py (CREATE only for RESULT or a PROGRAM's
  first computation; green exit 0 under python3 -O, no bare asserts,
  ≥1 red mode)
- theory/cat-hunt-notes.md (CREATE, optional)

No edits to existing files; MERGE PROPOSALS only for RESULT. No commits.

## Deliverable shape

(0) header: RESULT / PROGRAM / NOTHING NON-ARTIFICIAL + the one-sentence
version + where it would land (companion paper / discussion paragraph —
the Letter is full); (1) the hunt ledger, candidate → verdict → decisive
reason; (2) the best item worked as far as one session allows, with the
computed instance; (3) checker section if warranted; (4) MERGE PROPOSALS
if warranted. Write sections as you complete them.
