# Critic brief — D24(d)3 ρ-normalization adjudication, r1

Read `briefs/critic-protocol.md` first; everything there binds.

**TARGET:** `theory/verdicts/d24d3-adjudication-r1.md` and
`theory/checks/d24d3_normalization_check.py`.
**VERDICT FILE (your only writable file):**
`theory/verdicts/d24d3-adjudication-r1-critic.md`.

**Why you exist:** this clause has already been patched WRONGLY by two
independent prover lanes (S1-A silently redefined it; S1-B multiplied by an
undefended `1/(2ρ)`).  The adjudication under review will, if you pass it, be
merged verbatim into `definitions.md` — a **single-source, L4-protected
file** — and it moves D24(c) as well as D24(d).  A bad merge here propagates
into every future soft-index round.  Be correspondingly hostile.

**Read:** `briefs/d24d3-adjudication.md` (the work order it was given);
`definitions.md` D24 in full, D13(a), D25; `claims/CLAIMS.md` rows ML5, ML5-A,
ML5-B, S-general, S2-2body, **S2-2body-S**, **M-IDX-density**;
`theory/ml5-universality.md` in full; `theory/spin-s-twomagnon.md`;
`theory/soft-current-recon.md` (R14)/(R17)/(R18);
`theory/verdicts/soft-index-r1.md` cross-lane item 4;
`refs/arxiv-1203.0609` (the type-B Goldstone density the adjudication leans
on — check the citation against the local TeX by equation number, L3).

## The claims to attack, in priority order

1. **The root-cause claim: "`L` is never defined anywhere in the corpus."**
   This is the load-bearing premise of the whole repair — it converts D24(d)3
   from a stipulation into a derivable output.  **Verify it by exhaustive
   grep yourself.**  If `L` IS defined somewhere, the adjudication's entire
   derivation strategy is misconceived.
2. **The definition it supplies**, `L(k,h) := 𝔈ᴼ/[(e^{ik}−1)·2iv_h·M₁ᴼ]`,
   is claimed to be *forced* by clauses 1--2.  Is it forced, or merely
   consistent?  Is the denominator bounded away from zero on the hard window?
   Does the definition make clause 3's process-independence hypothesis
   nonvacuous, or does it make it a tautology?
3. **`Z := ⟨Ω|[S⁺ₓ,S⁻ₓ]|Ω⟩ = 2ρ` and the claim that the Ward residue is
   exactly linear in `Z`** (`⟨h|Q₀†J⁻₀|h⟩ = Z·2iJ sin h`, claimed to
   `4.8e-15` at `2S=1,2,3,4`).  Recompute this yourself, independently.  Then
   check the structural claim that D24(d)2 adopts the `Z`-carrying reading
   while D24(d)3's `−iχ/v_h` cancels it in full — **that single cancellation
   is claimed to BE the defect**, so verify the cancellation is real and not
   an artifact of how the adjudication chose to split the terms.
4. **The identification `Z = 2ρ = ` D13(a)'s frozen `1/(2s)` normalisation.**
   Three different symbols are being identified.  `ρ` is a DENSITY and `s` is
   a SITE SPIN — the corpus has an explicit r2 objection-1 fence against
   conflating them, and M-IDX-density's scoping sentence insists `ρ` is a
   fresh symbol with no assumed relation to the on-site dimension.  Does this
   identification breach that fence?  It may be legitimate for the fully
   polarised tail and illegitimate in general; say exactly which.
5. **The self-declared caveat.**  The adjudication concedes its
   emptiness argument rests on the corpus's identification of the D24(d)
   multiplier's jet with the two-body phase jet ((R17) / ml5 ⟨1⟩4.⟨3⟩4 / O9),
   which is **not a PROVED row**, and argues "both horns condemn the frozen
   clause".  Test that dilemma.  Is there a third horn?
6. **The refutation of both lanes' `(2ρN)^{−1/2}`** as `N`-dependent and
   jet-incapable.  A refutation of two prior lanes must itself be right;
   check it.
7. **Blast radius.**  It claims D24(c) must move too (`𝔠_h` and the ML5-A
   criterion hardwire the same `2`), that ML5-B stays PROVED with conclusion
   `i(χ/ρ)kM₁`, that eight step addresses in `ml5-universality.md` must move
   in lockstep, and that D24(e), `ml4_check.py`, `paper/main.tex` and the
   oracle rows do NOT change.  **Grep each negative claim yourself** — a
   missed lockstep site is exactly how this corpus has been damaged before.
8. **The checker.**  Green plus `--red-frozen`, `--red-power`,
   `--red-halfpower`, `--red-ward`.  It claims mutation-testing on copies via
   a `--data` path showed falsified ground truth, a moved decision band and a
   missing file each exit 1, "so the acceptance test is not self-fulfilling."
   **Verify that claim specifically** — an acceptance checker that passes its
   own repair by construction is the worst possible outcome here.  Also check
   the ED reproduction against `numerics/results/spin1-bc-falsifier.json`.

## Deliverable beyond the standard format

An explicit **MERGE / HOLD** decision on the §5 MERGE PROPOSALS, clause by
clause (D24(c), D24(d) preamble, D24(d)3a/3b, the CLAIMS ML5-B row).  For
MERGE, confirm the replacement text is verbatim-appliable and that the
"five-condition" count and `paper/main.tex:244` remain correct.  For any HOLD,
name the missing step.  State separately whether `𝒮_W` nonemptiness remains
open (the adjudication says YES, at every ρ) — and whether bd `tns-axg` may
be unblocked.
