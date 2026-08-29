# Critic brief — (LR) for D16, round 2 (adjudication + promotion)

Read `briefs/critic-protocol.md` first, including Standing checker obligations.

**TARGET:** `theory/lr-d16.md`, `theory/lr-d16-r2-response.md`,
`theory/checks/lr_d16_check.py`.
**VERDICT FILE (your only writable file):** `theory/verdicts/lr-d16-r2.md`.

**Prior:** `theory/verdicts/lr-d16-r1.md` — FAIL(F1,F2,M1–M4).  Verify each
disposition by fresh recomputation; attack what changed; do not churn r1's
verified items — above all **LR1, which you confirmed PROVED unconditionally**.

## What the lane did

It took every retraction rather than defending anything:
- **F1 — (LR2′) WITHDRAWN** for D16, not patched.  Confirm the withdrawal is
  complete: no surviving step, status line, or merge row still asserts it, and
  the mislabelled escape-profile checker row is gone or honestly relabelled.
  Confirm the residue is now attributed to the **O(1) magnon**, not the
  exponentially small kink tail.
- **F2 — (NR) repaired with `sup_m`**, exactly as you specified, with the
  theorem claimed to hold at the same constant.  Verify the constant, and that
  (NR) is now honestly presented as **two clauses**.
- **M2 — the class counterexample RETRACTED**, replaced by the scoping
  requirement that actually survives.  Confirm nothing downstream still leans
  on the refutation.
- **M3 — K4-strength language removed** from §H, ⟨1⟩2's Remark and
  ⟨1⟩6.⟨2⟩4.  This is a CONTENT test, not a string test: grep for "K4" proves
  nothing.  Read those three passages and judge whether what remains is
  supported by K1+K2 alone.
- **LR1 claimed byte-identical**, SHA-256 `0c28f353…0fde7`.  Check it.

## The promotion request — MP-3, two PROVED rows

The lane now proposes **only two** PROVED rows and holds the rest:

1. **`LR1-GEN`** — and note it has been **weakened to your MP-1 form**: "every
   prescribed `T_n→∞` has a subsequence on which both Cesàro states and all
   double-Cesàro TPM laws converge simultaneously for every fixed `W`", rather
   than "one sequence `T_n` gives…".  That is your own re-proposal.  Confirm
   the weakened statement is what the proof delivers, that it is still worth a
   row, and that D27's clause-1 relationship is stated correctly — your r1
   ruling was that clause 1 existentially binds the `T_n` that clauses 2–3
   quantify over, so the content of (LR) lies in clauses 2–3.
2. **`LR-D16-EDW`** — the energy/domain-wall operator bound, PROVED, with the
   r1 `m2` caveat: check the finite open-chain dynamics now uses `H_XXZ` and
   not `H_kink` (that was the conservation error you found, `‖[H_kink,H_XXZ]‖ =
   16.6`).
3. **`LR-D16` stays HOLD.**  Confirm that is right and restate what remains.

If you approve either row, **supply its exact statement cell verbatim** for the
orchestrator to apply without paraphrase.  Promotion happens on your sentence.

## The checker

Rebuilt to **17 rows, every one claimed mutation-reachable** — against r1's 18
rows of which **10 were killed by no mode**, plus three no-ops (LRD-C1(b),
LRD-C3(a), LRD-C3(d)).  The orchestrator re-ran it: green exit 0, `--red-all`
fires, all 17 named targets fire individually, zero bare asserts.  Necessary,
not sufficient.  Re-audit the three former no-ops specifically: are they now
real numerical certificates, or renamed?  This corpus has shipped a gate whose
"replacement" was byte-identical to the original, and another whose proposed
numerical fix was *also* identically zero.

## Deliverable

Verdict line; disposition of each r1 objection; **MERGE/HOLD on MP-1, MP-3's
two rows and MP-4**, with verbatim cells for anything you promote; and an
explicit statement of what `M-INDEX-spec` still lacks — the campaign's standing
claim is that it has **no fully unconditional dynamical instance**, and this
lane's honest headline must not drift from that.
