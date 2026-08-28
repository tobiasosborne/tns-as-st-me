# Critic brief — AC-EX-2M round 5 (adjudication; the promotion round)

Read `briefs/critic-protocol.md` first, **including Standing checker
obligations**.

**TARGET:** `theory/ansatz-scattering-2m.md`,
`theory/ansatz-scattering-2m-r4-response.md`,
`theory/checks/ansatz_scattering_2m_check.py`.
**VERDICT FILE (your only writable file):**
`theory/verdicts/ansatz-scattering-2m-r5.md`.

**Priors:** `-r1` … `-r4`.  Trajectory **6 → 2 → 1 → 1 MAJOR**, 0 FATAL
throughout.  r4 said severity had gone FLAT.  Scope with `git diff`; verify
the 19 claimed dispositions (R4-O1…O6, R4-N1…N13) by fresh recomputation; do
not re-litigate settled text or churn r4 §7's fenced list.

## 1. R4-O1 — the step that was never touched

`⟨1⟩9.⟨2⟩5`, the sole D6 instance of `(ACE2M-SR)`, was skipped by the r3 diff
entirely and still backed a D29 claim through a leaf citing the port that
disclaims D29.  The prover reports it now separates the constructed-channel
singleton explicitly from D29.  **Verify the fix reaches the leaf**, not just
the surrounding prose: read the Justification line itself, and confirm no
surviving step reads the D29 identification as available.  r4 measured the gap
at relative order `ε` (`√2·k_s`, `1.43e−02` at `k_s=0.01`); confirm the shard
now says which family it instantiates everywhere it matters.

## 2. THE ROW SPLIT — the deliverable of this round

r4 recommended, beyond its brief, splitting the row, and the prover has
drafted both.  You decide.

- **`AC-EX-2M` at PROVED (conditional on D31)** for `(A2M.1)`–`(A2M.2)`:
  fixed-packet Cook existence, isometry, translation intertwining,
  bound/inelastic separation, the ML2/D7 match on D6–D8, and D31-C2/C4 derived
  from D1.  r4's grounds: four hostile rounds, 0 FATAL, independently
  reproduced (D31-C2 four times, the checker twice from different tensors),
  and depending on **nothing** in the D29 interface.
- **`AC-EX-2M-D29` at SKETCH** for the interface.

**Test the independence claim yourself — it is the whole basis of the split.**
Walk `(A2M.1)`–`(A2M.2)`'s proof and confirm no step, however incidental,
consumes `(ACE2M-LSZ)`, `(ACE2M-SR)`, `(D29-den)` or the D29 identification.
One such consumption and the split is invalid.

If you approve, supply **both rows' exact statement cells verbatim**, in the
adjudicated-scoping register of the existing PROVED rows, for the orchestrator
to apply without paraphrase.  If you do not, name what would change your mind.
Promotion to PROVED is a ratchet move; it happens on your sentence, not on the
prover's.

## 3. Checker

Claimed: nine gates, **all reachable** via seven registered mutants;
route-collapse guarded (r4's `m11`, which passed green printing `0.000e+00` —
the campaign's pattern-#1 defect); absurd-`λ̃` regression guarded (r4 found
`3.7`, `−5.0`, `1e6` all passing, and the `0.1` cap failing already at `0.34`).
The orchestrator re-ran green plus all seven modes: all fire, zero bare
asserts, and the shard's §7 row is byte-identical to `claims/CLAIMS.md`'s.
Necessary, not sufficient.  Apply every standing obligation: reachability per
gate, subsumption, data-vs-code mutation, and whether any two red modes are
bit-identical in effect.  `ratio_route` remains a retracted advertisement —
confirm it is still honestly labelled and has not quietly regained a claim.

## Deliverable

Verdict line; the r5 MAJOR count against `6 → 2 → 1 → 1 → ?` with an explicit
statement on monotonicity; a **MERGE/HOLD ruling on the row split** with both
verbatim statement cells if you approve; and, for `AC-EX-2M-D29`, the named
missing steps that keep it at SKETCH.
