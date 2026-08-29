STATUS: PROVED-candidate

Proved exhaustion-by-exhaustion `(M-ESC) => not-(NR)` by composing exact rows `ACE-LD-obst-prime` and proposed `LR-D16-NR` against D27(LR3).
The Lamport proof fixes one common `Psi`, cut, clause-1 sequence, laws, and padded exhaustion, so no quantifier or limit-order switch is hidden.
Ownership: `theory/lr-d16.md`, where `(NR)` is defined and consumed; `theory/ace-ld.md` must cite `LRD-MESC-NR`, not restate it.
The conclusion is only that at least one of the two repaired `(NR)` clauses fails; it does not identify which one.
No `(M-ESC)` model/state is known, so this is a conditional incompatibility, not a D16 counterexample.
`PATCH.md` targets `theory/lr-d16.md`, `claims/CLAIMS.md`, and `theory/ace-ld.md`; complete patched copies are lane-local.
Remaining: orchestrator applies the anchored patch and adjudicates the two new DAG rows; both are left `SKETCH` pending that step.
