# Critic brief — D24(d)3, round 3 (adjudication)

Read `briefs/critic-protocol.md` first, **including Standing checker
obligations** (five bullets).

**TARGET:** `theory/verdicts/d24d3-adjudication-r3.md` (1333 loc),
`theory/verdicts/d24d3-repair-r3-response.md`,
`theory/checks/d24d3_normalization_check.py` (559 loc).
**VERDICT FILE (your only writable file):**
`theory/verdicts/d24d3-adjudication-r3-critic.md`.

**Priors:** `-r1-critic.md` (3 FATAL/7 MAJOR) and `-r2-critic.md` (1 FATAL/5
MAJOR).  Trajectory `3/7/6/4 → 1/5/8/5 → ?`.  Verify dispositions by fresh
recomputation, attack what changed, do not re-litigate settled text, and do
not churn either prior verdict's fenced VERIFIED-CORRECT lists.

**Stakes:** a PASS merges into `definitions.md` AND `notation.md` — two L4
single sources — plus `claims/CLAIMS.md` row changes, **as one commit**.  Two
prior attempts would have installed defects.  This round claims to have
repaired all five r2 HOLD items.

## Attack in this order

1. **§5.0, the amputation convention — the FATAL's repair.**  It is offered
   as a **choice**, and ⟨1⟩0.⟨3⟩6 names the alternative it refuses (a
   convention making the D24 ratio *be* the physical soft factor, which would
   make `D24-VAL` a tautology).  Is the chosen convention (a) well defined,
   (b) consistent with every existing corpus use of "amputated", and (c) the
   one that keeps `D24-VAL` contentful?  Does fixing `c′(0)/c = 1` actually
   make `𝔞_leg` a number, or does it merely move the arbitrariness?
2. **The withdrawal.**  The lane WITHDREW its r2 claim that the density can
   only live in `𝔞_leg`, conceding your r2 point.  Check the withdrawal is
   complete — that no downstream sentence still relies on the withdrawn
   argument — and that (3b)'s residual membership content (the `h`-profile:
   `v_h L(0,h)/χ` is `h`-independent) is a real, checkable condition.
3. **The new sharp result — verify it independently.**  `Q^-_k|Ω⟩ =
   √(Z_ρ)·|k⟩` **exactly** (gate D24N-C8, claimed residual `1.8e-15` against
   `H_S`'s own one-magnon eigenvector), whence leg conversion alone gives
   `𝔞_leg = Z_ρ^{-1/2}`, which the data **refutes** at the pre-registered
   `0.08` band with margin 5--12×.  Recompute both halves.  If it stands, AMP
   is true only if a second `Z_ρ^{-1/2}` arises from something that is not a
   leg normalisation — a genuinely useful narrowing.  If the identity is only
   approximate, the narrowing evaporates.
4. **ML5-B stays PROVED with a number-free conclusion.**  The argument: `2`
   was never a consequence of ML5-B, only of ML5-B *plus* the retired
   stipulation, so the proof survives reparametrisation.  Test that.  Then
   check the re-sourcing claim by grep: that every corpus display of `2` now
   traces to the contact/oracle route (`main.tex:515–520`, O7–O9), which never
   used D24(d).  And rule on the mechanics: `corpus-r2.md:174–178`, the
   promotion record, is **annotated rather than erratum'd**, with
   where-proved still pointing at it — is that acceptable, given the
   annotation ships in the same commit?
5. **The checker, third pass.**  It now claims **no acceptance constant at
   all**: the band is derived at runtime as `max_rows |error|·S = 0.0479` from
   the data's own quoted error.  **Is deriving the band from the data
   self-fulfilling in a new way?**  Check the guards (zero, missing,
   over-wide error columns).  Confirm the `−3%` mutant you rejected in r2 now
   correctly passes, that `--red-ladder` (your `cA_deepladder`) now dies at
   C2, and that `--red-legfactor` reaches C8.  The lane declares its own
   remaining gaps — C1 symbolic with no runtime red mode, C5/C7 display, C6
   = C4 at a tighter band with only ≈1.7× exponent gain (correcting r2's
   claimed 3.5×), no gate touching `L`/`E^O_desc`/membership, C2's margin now
   one decade.  Verify each declaration is accurate and complete; an accurate
   self-declared gap list is worth more than a clean bill.
6. **Merge coherence.**  §5.0–§5.5 is offered as ONE commit with
   descending-line-order mechanics for three adjacent `definitions.md` spans
   and all anchors re-verified.  Apply the spans yourself in a scratch copy
   and confirm they apply cleanly, in that order, without overlap — the
   orchestrator will not hand-patch an L4 file.
7. **The two deviations, both declared:** r1's M3(c)(iii) DECLINED with reason
   (building the jet from a constructed `E^O_desc` needs a class member, which
   would settle `tns-axg`), and `D24-VAL` given plain `PROVED` rather than a
   parenthesised status because the CLAIMS header forbids qualifier-bearing
   statuses, with `CONJECTURE` moved to a new `AMP` row.  Rule on both.

## Deliverable

Clause-by-clause **MERGE / HOLD** on every proposal in §5.0–§5.5, including
the `notation.md` rows and the CLAIMS row changes.  State whether the merge
may proceed **as one commit**.  State whether `𝒮_W(ρ)` nonemptiness is still
open, whether `tns-axg` may move, and whether `tns-iu5` may now close or which
of its three sub-tasks remain.
