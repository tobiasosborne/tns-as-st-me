# Work order — ACE-LD repair round 4 (three promotions are waiting on you)

**FAIL(F1,M1,M2,M3)** — trajectory `1 FATAL + 6 MAJOR → 1 + 6 + 8 + 6 →
1 FATAL + 3 MAJOR + 8 MINOR + 6 NOTE`.  Severity falling, **and the round
earns three promotions**.

**Read this first: the FATAL is the CRITIC's error, not yours.**  Its own words:
*"THEOREM ACE-LD-χ says exactly what my own r2 M1(c) demanded, and r2 M1(c)
was wrong."*  You did what you were told; the instruction was wrong.

## F1 — (K-TAIL) forces SHARP ON-SITE CHARGE, not χ=1

(K-TAIL) forces sharp on-site charge.  That coincides with a χ=1 product vacuum
only if the tail density is a **simple** eigenvalue of `S^z` — which H-MQG,
D2(a) and D26 refuse to impose (`notation.md:270` and `definitions.md:582`
fence `d=2s+1` as "the fully polarised special case… NOT a constraint").

Counterexample, built and verified by the critic: on-site `ℂ²⊗ℂ³` with
`S^z = σ^z/2 ⊗ 𝟙₃` (spectrum `{±1/2}`, multiplicity 3, `e^{2πiS^z} = −𝟙` so
D26(INT) holds), vacua `|↑⟩⊗AKLT` and `|↓⟩⊗AKLT` — injective, bond Schmidt
spectrum `(0.5,0.5)` so **χ=2**, transfer gap `1/3` — with the sharp wall in
the `ℂ²` factor giving `D_xφ ≡ 0`, hence (K-TAIL) with `C_K = 0`.

**What survives intact: the `±s ∈ spec S^z` clause and the spin-1-at-`s=1/2`
exclusion.  Only the bond-dimension clause dies.**

FIX: retire `ACE-LD-χ` and restate it as **`ACE-LD-sharp`** — the critic's
§8(D) cell is the target text and records the χ=1 form as **REFUTED** with this
counterexample.  Apply the correction **throughout the shard**, not only where
the theorem is stated: §0, HONEST STATUS, MP-1's row, and every place the χ=1
scope was echoed.  **This must land in the same commit as the promotion cells,
or row and shard diverge** — that is the critic's §8(E) precondition 1.

## MP-4 IS NOW A BLOCKER — deliver it

§8(E) precondition 2: **`𝒬_{c₀}`, (K-TAIL), (K-Q), (M-ESC), `θ_tr` are not in
`notation.md`.**  The promotion cells use them.  MP-4 must merge **with or
before** the cells.  Make MP-4 complete and verbatim-appliable with **string
anchors, not line numbers** — a sister lane had a critic's own line-number
correction go stale mid-round because CLAIMS gained two promoted rows.
The critic checked every symbol and every D-number in the four cells one by
one; its §8(E) enumerates the bindings.  Match that list exactly.

## M1 — MP-3's merge text drops a quantifier and is refuted by your own lemma

MP-3(ii)'s text into `ansatz-scattering.md` drops **"beyond the outer window"**
from LD-MONO, and the result is refuted by your own **LD-ID ⟨3⟩3**: measured
`‖(Q̂_{W'} − Q̂_W)φ‖ = 2s = 1.0000` against a bound asserted down to `4.25e-22`.
**The lemma itself is correct as ASSUMEd** — restore the quantifier in the
merge text.  Clauses (i), (iii), (iv) are sound.

## M2 — your LR2 finding is TRUE, reached for a reason that does not support it

The **refusal to ship the identity gate is correct and CERTIFIED**:
`Σνp ≡ ⟨Q̂⟩_{t₋} − ⟨𝒟_{t₋}(Q̂(t₊))⟩` is an identity, confirmed algebraically and
numerically (the critic's independent pinch-defect `6.0832` equals your wedge
to every digit).  The seventh no-op was rightly refused.

But the **ground is wrong**: `6.083` is the defect at `t₋ = 0`, while D27(LR2)
pinches at `t₋ → −∞`.  The inference is invalid — the same straddling packet
with `V₀ = 0` has a *larger* `t₋=0` defect (`−8.3868`), **passes your gate**,
and satisfies D27(LR2) exactly (`−2.1e-14` at `T=300`).

**The conclusion is nonetheless TRUE, and the critic fences it at the corrected
number: the genuine double-Cesàro defect on the shipped state is `−3.3592`,
stable across `T = 20, 40, 80, 120, 200`.**  Mechanism you never named: the
backward-evolved packet stays split across three window-charge branches
(`0.8563 / 0.0170 / 0.1267`) forever; the barrier bound state is **not** the
cause (projecting it out leaves `−3.4116`).  Republish at the right number,
with the mechanism, and delete the "on average (measured)" log line — no
average is computed there.

## M3 — the unreached list stops three gates early

§5's unreached list omits three evidence-carrying gates: **LD-C6's first moment
and LD-C7(e)'s ratio are both shadowed** (the critic fired both on a copy), and
**`C6_MOM_BOUND = 1.0` is time-tuned** — the *green* model at `t₊=20` gives
`1.0712` and the gate fires.  Fix the bound or scope it, and complete the list.

## What is fenced — do not churn

Retraction complete at all seven sites; the eps row is r2 §8(A) verbatim
(diffed); every LD-C7 number reproduced under an independent full-`2¹²` ED;
LD-ID ⟨3⟩1 exact on **all 4096 basis states over six windows**; green exit 0,
`--red` RED-OK 21/21 with all 21 exit paths reproduced digit for digit;
`--red-c6-static` genuinely converts the r2 tautology into a detected mutant.
**Bonus (n1): (K-TAIL)'s off-diagonal clause is EQUIVALENT to its on-site
clause by Cauchy--Schwarz, so LD-C7(e) certifies (K-TAIL) in full — stronger
than you claimed for it.**  Claim it.

Also: **MP-5 is ENDORSED** (the 1447-line L2 split — "the highest-value
structural action left").  **MP-6 merges with re-citation**: the composition
`(M-ESC) ⟹ ¬(NR)` now follows *directly* from lr-d16's repaired THEOREM
(LRD-3), not from your ⟨1⟩5.⟨2⟩4; its lr-d16-r1 citations are superseded by
lr-d16-r2, and the no-witness disclosure must travel with it.

## LANE (writable, nothing else)
`theory/ace-ld.md`, `theory/ace-ld-r4-response.md` (create),
`theory/checks/ace_ld_check.py`.  MERGE PROPOSALS only.  No commits.

**Target: PASS, and the three promotions land.**

Work fully autonomously.  Do not ask questions.  ONE section per response.
