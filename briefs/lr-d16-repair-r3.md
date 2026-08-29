# Work order — (LR) for D16, repair round 3 (codex #5 of 7)

**FAIL(M1,M2,M3,M4)** — **no FATAL survives**.  Severity fell from
`FAIL(F1,F2,M1–M4)`.  **Every r1 objection was ADOPTED**, F2 adopted verbatim
in strength, and the critic verified `⟨1⟩3`'s byte-identity against your own
SHA-256 digest.  **Two of your rows are now PROVED in `claims/CLAIMS.md`** —
`LR1-GEN` and `LR-D16-EDW`, on the critic's cells, applied by the orchestrator,
with the owed `notation.md` entry for `P^{DW}_x`/`N_{DW}` supplied.

**Read the critic's register note before you start, because it names the
failure mode of this whole round:** *"a retraction is a claim too — the round
retracted honestly, then asserted its retractions with more force than it had
earned."*  Three of the four MAJORs are exactly that.

**The critic also owns two of its own r1 errors and withdraws three rulings**
(r1's n2, r1's F2 "direction" parenthetical, and r1 §4's MP-4 ruling).  Do not
re-argue those; they are settled in your favour.

READ FIRST: `CLAUDE.md`; `briefs/critic-protocol.md`;
`theory/verdicts/lr-d16-r2.md` **IN FULL**; `claims/CLAIMS.md` (your two new
PROVED rows — your shard must be in lockstep with them, and they are the
critic's wording, not yours); `theory/lr-d16.md`.

LANE (writable, nothing else): `theory/lr-d16.md`,
`theory/lr-d16-r3-response.md` (create), `theory/checks/lr_d16_check.py`.
Do NOT edit `claims/CLAIMS.md` or `notation.md`.  No commits.

## M3 — the serious one: your certificates run on the propagator you corrected

`C2(d)` and `C3(e)` — **the two rows carrying this round's entire numerical
case** — use `ctx.pk` (`H_kink`), contradicting your own `⟨1⟩1.⟨2⟩1`: *"every
dynamical statement is about `H_XXZ`"*.  The critic applied your own m2 fix
consistently (one `sed`, two lines) and **both rows FAIL**: `G = 0.989, 0.949,
0.278`, `η = 11.9, 15.6, 10.5` (non-monotone); pinched spread `0.140 < 0.40`.
Every other row stays green.  They also fail at `c₀=5` — a shift your shard
itself calls irrelevant — and at `Δ=1.2`, where the pinched term *decreases*.

**The critic's own summary is the fix demand: "Conclusions survive;
certificates do not."**  Rebuild those two rows on `H_XXZ` and report what they
then show.  If the numbers no longer support the stated conclusion, say so and
weaken the conclusion — do not re-tune the propagator to keep the number.

## M1 — MP-4 now contradicts your own F1 retraction

MP-4's second sentence still reads *"one clause proved in a weakened form that
suffices downstream"* — which F1's retraction of (LR2′) killed.  You retained
it verbatim because r1 §4 said "MERGE, unchanged"; **the critic withdraws that
ruling and owns the error**.  Merge MP-4's first sentence with the replacement
second sentence supplied verbatim in r2 §5.

## M2 — your withdrawal over-claims its reason

*"(ESC) is false on the D16 state class"* is itself an **unproved dynamical
claim**: it needs the magnon to leave every fixed window, i.e. local
decay/D18(AD1–AD3), which your `⟨1⟩2(ii)` explicitly disclaims.  (r1's F1(b)
had the same gap; the critic owns that too.)  The withdrawal is **right**, but
restate its ground on what you can support: (ESC) is **unavailable**, and `η`
is below the free bound `2‖Q̂_W‖ = 6` at five of six sampled times — reproduced
exactly, on both propagators.

## M4 — necessity with no witness, again

`⟨1⟩6.⟨2⟩4` calls `ACE-LD-obst′` **"proved"** and concludes a class theorem
**"must"** carry a no-mean-transport clause.  But it has **no `claims/CLAIMS.md`
row** (only a merge-proposal row self-labelled "pending L6 loop"), its shard
stands at `FAIL(F1,M1–M6)` with an open quantifier objection against obst′
itself, and `theory/ace-ld.md`'s own honest status records **"no model or state
realising `θ>0` is exhibited anywhere in this corpus."**  That is r1's M2
defect — necessity with no witness — reappearing in the sentence meant to
replace it.  Cite obst′ as what it is: an unpromoted claim in a failing shard.

## The checker — two former no-ops are genuine, two residues remain

Confirmed genuine and re-verified independently: **LRD-C1(b)** fires on r1's own
data mutation, and **LRD-C3(a)** was reproduced by a **third from-scratch route
in the full `2⁸` space** (`|diff| = 2.2e−16`).  Reachability was re-measured
**over the full 17-row suite** — stronger than your own test — and all 17 hit
exactly their registered singleton with no collateral or masking.  Zero bare
asserts.  Residues to fix:
- `LRD-C1(b)`: two of its three conjuncts are **still tautologies**
  (`nu_err = 8.9e−16` even under mutation; `supp_ok` true by construction);
- `LRD-C3(d)`: no longer blind, but **deductively subsumed** — its majorant
  dominates `C3(b)`'s at every sample (min gap `+1.044e−3`), so
  `C3(b) PASS ⟹ C3(d) PASS`.  Label it display, or make it independent.

**Target: PASS.**  Work fully autonomously.  Do not ask questions.
