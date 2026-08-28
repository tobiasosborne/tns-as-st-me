# Work order — S2 repair round 4 (codex #3 of 7) — THE PROMOTION ROUND

Trajectory **6 → 2 → 1 → 1 MAJOR**, 0 FATAL throughout.  The critic said
plainly that severity did NOT fall this round; it went flat.  Your job is to
make it fall to zero, and to set up the promotion the critic says is overdue.

READ FIRST: `CLAUDE.md`; `briefs/critic-protocol.md` (**Standing checker
obligations** — five bullets); `theory/verdicts/ansatz-scattering-2m-r4.md`
IN FULL (your work order; read its §7 fenced list first and do not churn it);
priors `-r3.md`, `-r2.md`; `theory/ansatz-scattering-2m-r3-response.md`;
`claims/CLAIMS.md` (the `AC-EX-2M` row — **the orchestrator has just applied
r4 §9's replacement sentence verbatim; your §7 row must match it byte-for-byte
again**).

LANE (writable, nothing else): `theory/ansatz-scattering-2m.md`,
`theory/ansatz-scattering-2m-r4-response.md` (create),
`theory/checks/ansatz_scattering_2m_check.py`.  No commits.

## R4-O1 (the MAJOR) — one step was never touched

`⟨1⟩9.⟨2⟩5`, the **sole D6 instance of `(ACE2M-SR)`**, was not in your r3 diff
at all (the hunks jump `@@ -520 @@` → `@@ -595 @@`, straddling it).  It still
writes the D29 datum as `A(ε)(h)=∫dμ_f S_phys(εu,h)` — the constructed-channel
matrix element — and its **Justification leaf cites `⟨1⟩8.⟨2⟩1--⟨2⟩2`**, the
port whose own tail, thirty lines earlier, says the theorem does not apply to
the adjudicated D29.  The step silently assumes the branch-(i) result you
declined to prove.  The critic recomputed the gap: `1−S_12 = −2ik_s+O(k_s²)`,
`∂δ/∂k_s|_0 = 2.000000000` at every `k_h`, relative mismatch `√2·k_s`
(`1.43e−02` at `k_s=0.01`) — **the two families differ at exactly the order
⟨2⟩5's conclusion lives at.**

FIX (A), expected: relabel `⟨1⟩9.⟨2⟩5` so it states plainly which family it
instantiates (the constructed-channel one), note it is a one-element family,
and stop it backing any D29 claim.  FIX (B), only if you can close it: prove
branch (i) at `O(k_s)`.  Take (A) unless (B) is genuinely in hand.

## THE ROW SPLIT — draft it; the r5 critic adjudicates it

The critic recommends, beyond its brief, that the row be **split**, and I want
the proposal on the table.  `(A2M.1)`--`(A2M.2)` — fixed-packet Cook
existence, isometry, translation intertwining, bound/inelastic separation, the
ML2/D7 match on D6--D8, and D31-C2/C4 derived from D1 — have survived **four**
hostile rounds with 0 FATAL, are independently reproduced (D31-C2 four times,
the checker twice from different tensors), and depend on **nothing** in the
D29 interface.  They are being held at SKETCH only by an open interface clause
they do not use.

In your MERGE PROPOSALS section, draft **two** rows, complete and
verbatim-appliable:
1. **`AC-EX-2M`** at **PROVED (conditional on D31)** — `(A2M.1)`--`(A2M.2)`
   only, in `AC-EX`'s register, with an adjudicated-scoping sentence in the
   style of the existing PROVED rows.  It must claim nothing about D29.
2. **`AC-EX-2M-D29`** at **SKETCH** — the interface: `(D29-den)` diagonal
   compactness, `(ACE2M-LSZ)` creator-choice independence as a theorem about
   HR creator families, and the two named missing steps (branch (i) at
   `O(k_s)`; an `(ACE2M-SR)` instance for the family it constrains).
Do NOT edit `claims/CLAIMS.md` yourself.  Propose; the orchestrator merges
only after the r5 critic adjudicates.

## THE CHECKER — reachability, not just red exits

- **G1** (C1a direct value) and **G4** (C1b agreement) are reached by **no
  registered mutant**; the critic proved both live (`m3` ground-truth shift,
  `m13` drop the subtraction).  Add red modes that reach them.
- **Absurd inputs pass green**: `λ̃ = 3.7, −5.0, 1e6` all pass; the `0.1` cap
  already fails at `λ̃ = 0.34`.  Fix the bound or the gate.
- **`m11` — collapsing the two routes passes green**, printing `0.000e+00` for
  both agreement and `ratio_route`.  That is the campaign's pattern-#1 defect
  (two identical expressions certifying 0 by construction) sitting unguarded
  in your certificate.  Guard it.
- `ratio_route` was correctly RETRACTED rather than defended (the brief
  authorized that disjunct) — keep the retraction, keep the honest naming, and
  do not re-advertise it.
- Report the **exit path** for every red mode, and confirm every gate has a
  mutant that reaches it.

## THE FIVE MINORS AND THIRTEEN NOTES

One response row each in `ansatz-scattering-2m-r4-response.md`
(FIXED / RETRACTED / DOWNGRADED / RESIDUE + exact location).  Lockstep against
the merged row is a first-class obligation and will be checked with `cmp`.

Work fully autonomously.  Do not ask questions.  Do not stop at a plan.
