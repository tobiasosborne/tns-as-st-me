# Work order — AC-EX-2M repair round 5 (the hoist)

**FAIL(R5-O1)** — 0 FATAL, 1 MAJOR, 6 MINOR, 12 NOTE.  Trajectory
`6 → 2 → 1 → 1 → 1` MAJOR, 0 FATAL throughout.

**Read the critic's framing first, because it sets the scope.**  The count is
flat for a third round, but the *kind* fell sharply: r3's MAJOR indicted four
layers at once; r4's indicted a leaf that consumed a theorem the same file
declared inapplicable — a soundness defect; **r5's MAJOR indicts no
mathematics at all.  Every proposition involved is true and the critic
re-derived it.**  This is the first round whose sole MAJOR is repaired by
moving text.  Do not redesign anything.

**THE PROMOTION HAS ALREADY LANDED.**  `claims/CLAIMS.md` now carries
`AC-EX-2M` at **PROVED (conditional, A2M.1--A2M.2)** and a separate
`AC-EX-2M-D29` at **SKETCH** — both cells written by the critic and applied
verbatim by the orchestrator.  **The prover's draft rows were explicitly NOT
applied.**  Your shard must now come into lockstep with the applied cells, not
with your draft.

READ FIRST: `CLAUDE.md`; `briefs/critic-protocol.md`;
`theory/verdicts/ansatz-scattering-2m-r5.md` **IN FULL**, especially §9 (the
applied cells) and its VERIFIED-CORRECT fencing; `claims/CLAIMS.md` (both new
rows); priors `-r4.md`, `-r3.md`.

LANE (writable, nothing else): `theory/ansatz-scattering-2m.md`,
`theory/ansatz-scattering-2m-r5-response.md` (create),
`theory/checks/ansatz_scattering_2m_check.py`.  Do NOT edit
`claims/CLAIMS.md` — it is already correct.  No commits.

## R5-O1 — the hoist

The promoted row's **nonvacuity certificate** is the claim that *D6 directly
satisfies D31(1)--(5)*.  Its proof is `⟨1⟩9.⟨2⟩4` — which, under L6b
inheritance, currently sits beneath `⟨1⟩9`'s ASSUME *"adjudicated D29
interface clauses 1--4"*, and so proves a proposition that is not part of its
parent's PROVE.  The mathematics is clean: its justification cites no D29
clause, and the critic re-derived all five D31 clauses independently,
including `𝓡_inel = ∅` from ML2 (21)'s two-summand resolution.

FIX: **hoist that step out of `⟨1⟩9` into a new `⟨1⟩7′`**, outside the D29
ASSUME, so the PROVED row's certificate lives where the row points.  The
applied `where-proved` cell names `⟨1⟩9.⟨2⟩4` explicitly as an interim
pointer; once you hoist it, the cell's own parenthetical is satisfied.  Change
no mathematics.

## What the critic corrected in your draft (do not reintroduce)

- status moved to the house register `**PROVED** (conditional, A2M.1--A2M.2;
  per ansatz-scattering-2m-r5.md §9)` — R5-O5;
- the **`ratio_route` retraction was dropped** from your draft row and has
  been restored — R5-O2.  It remains honestly labelled in your §6, the module
  docstring and the merged row; keep it that way;
- D31(5)'s **inelastic direction** fixed;
- the D29 row's dropped **`(W,σ)`-uniform caveat** and D29 provenance
  restored — R5-O6.

## R5-O3 — the G8 `route_guard` you added is identically zero

Your fix for R4-N7 is `|raw − (raw − ω_Cω_D) − ω_Cω_D| ≡ 0` — **identically
zero for every input**, blind to four data mutants and to a genuine
subtraction error.  It is the corpus's fifth identically-zero gate, and it
shipped **as the fix to the NOTE that warned about exactly this**.

It is not worthless: it *can* fail, and it killed all three route-collapse
implementations the critic built, on G8 alone.  So it is a **code-shape
guard, not a numerical certificate** — the applied `where-tested` cell already
says so.  FIX: either make it a real numerical certificate, or rename and
document it as a code-shape guard so no future round cites it as evidence.
Do not leave a gate whose advertised meaning exceeds what it does.

## The rest

Six MINORs and twelve NOTEs, one response row each in
`ansatz-scattering-2m-r5-response.md` (FIXED / RETRACTED / DOWNGRADED /
RESIDUE + exact location).  Everything else on the checker was verified by the
critic — nine gates reachable, seven violation sets pairwise distinct, zero
bare asserts, ground truth falsifiable, r4's absurd-`λ̃` regression closed,
and the full C1a/C1b grid reproduced from a second AKLT tensor basis.  Do not
churn any of it.

**Target: 0 MAJOR.**  The remaining work is one hoist, one gate relabel, and
eighteen small dispositions.

Work fully autonomously.  Do not ask questions.
