<!-- ROLE: proposer r2 response ledger to theory/verdicts/lr-d16-r1.md.
     Work order: briefs/lr-d16-repair-r2.md.  Lane: theory/lr-d16.md,
     this file, theory/checks/lr_d16_check.py.  No shared-file edits. -->

# (LR) for D16 r2 — objection dispositions

The r2 repair accepts the critic's headline exactly.  **LR1 is confirmed
PROVED unconditionally and is the round's protected result.**  The complete
⟨1⟩3 section was not edited: its pre/post SHA-256 is
`0c28f353fee526373e26fc6bbcf41d18d411f2da557409281395ee5d14c0fde7`.
LR1-GEN remains PROVED and is stated in the critic's stronger
any-sequence/then-subsequence form at ⟨1⟩6.⟨2⟩2.

| id | sev | disposition |
|---|---|---|
| F1 | FATAL | **ADOPTED — retracted, not patched.**  The r1 D16 result `(LR2′)` and its logarithmic-padding rate are withdrawn at the summary, ⟨1⟩2, ⟨1⟩4, §H, and MP-2/MP-3.  What remains proved is LRD-2-BND, `|avg Δ_{W_m}|≤4R_{W_m}√G(m)`.  Its abstract antecedent (ESC), `R_{W_m}²G(m)→0`, is stated and proved false for every (H3) state: the `C_c^∞` magnon has nonzero velocity, exits every fixed window, and contributes one to `𝒩_W`, so `G(m)≥1-o(1)`.  C2(d) now computes `𝒩_W²`, over `t∈[-40,40]`, and labels the result honestly: `G=0.990,0.965,0.950`, `η=11.9,15.7,19.5`.  The free `2‖Q̂_W‖=6` comparison is recorded; no constant is altered.  The residue in ⟨1⟩4.⟨2⟩6 is corrected from the exponentially small kink tail to the `O(1)` magnon.  Consequence: `M-INDEX-spec` is unaffected and unimproved; `M-INDEX-fin` is safe. |
| F2 | FATAL | **ADOPTED VERBATIM IN STRENGTH.**  (LRD.13) now uses `φ_q^{(m)}=E_{W_m,t_-}(q)Ψ` and says exactly what the monotonicity lemma proves: the majorising observable is fixed to `𝒩_{W_1}`, while the dephased state remains `m`-dependent.  (NR) is explicitly **two clauses, not one**; its second is `sup_m sup_{t_-<t_+}Σ_q‖α_{t_+}(𝒩_{W_1})E_{W_m,t_-}(q)Ψ‖²<∞`.  THEOREM LRD-3 then follows with the unchanged tail constant `2S_NR/M`.  C3(e) reproduces the critic's pinched terms `1.383/1.797/1.872`; freezing all pinchings to `W_1` is its exact red mutant.  The non-circularity comparison with LR3 is stated in ⟨1⟩5.⟨2⟩7. |
| M1 | MAJOR | **ADOPTED.**  MP-1 no longer says clause 1 can be demoted.  It proposes: for any `T_n→∞` a subsequence satisfies clause 1; clause 1 remains the existential binder consumed by clauses 2--3; the substantive content lies in clauses 2--3.  It also proposes that D27(LR2)'s limit be read along that same common sequence. |
| M2 | MAJOR | **ADOPTED — counterexample retracted.**  Every assertion that a gapped finite-range mobile-core model refutes the class statement is deleted.  ⟨1⟩6.⟨2⟩5 records why: no model was named and (FN)/(LRD.5) pins sharp-core position to `𝒬_0`; large `|ν|` would require wrong-phase block growth, not rigid core transit.  The surviving LR3-SCOPE statement is only that this shard uses no gap/LR velocity and `ACE-LD-obst′` independently requires a no-mean-transport clause in a future class theorem. |
| M3 | MAJOR | **ADOPTED by content.**  ⟨1⟩2's remark, ⟨1⟩5.⟨2⟩8, ⟨1⟩6, and §H now say only: every state in the closed span of the K1--K2 family is stationary.  No D16-wide group velocity, kink-manifold exhaustiveness, no-recoil, or outside-the-ballistic-class conclusion remains.  K4 is named as CONJECTURE wherever that upgrade is fenced. |
| M4 | MAJOR | **CHECKER REBUILT.**  The r1 no-ops C1(b), C3(a), and blind C3(d) are gone.  C1(b) gates raw spectral values and dies under `q_w↦q_w+0.3`; C3(a) forms `α_{t±}(Q̂_W)` as matrices on an independent `N=8` sector and dies when only the final evolution is perturbed; C3(d) gates the honest `W_m`-pinched majorant, while new C3(e) gates the real `m`-dependence and dies when pinching is frozen to `W_1`.  All 17 evidence rows have distinct registered mutants and printed exit paths.  The old subsumed C6(b) and tautological C4(c) ratio were deleted. |
| m1 | MINOR | **FIXED without a false core-invariance claim.**  ⟨1⟩1 states the common finite-deviation core for the diagonal multiplication operators, defines Heisenberg expectations as extended quadratic forms through finite truncation/monotone convergence, and says squaring is valid only because the comparisons are simultaneous-diagonal, pointwise non-negative inequalities. |
| m2 | MINOR | **FIXED.**  C4(b) evolves with `H_XXZ`, gates `H_XXZ` energy conservation (`1.11e−14` drift), and then checks `max⟨D⟩=3.053≤4.753`.  Its mutant deliberately evolves with `H_kink` and is caught by energy drift.  The proposed LR-D16-EDW row carries the infinite-volume/finite-open-chain caveat. |
| m3 | MINOR | **FIXED with F1.**  Every residue description names the `O(1)` escaped magnon, not the `q^{2d_W}` kink tail. |
| m4 | MINOR | **FIXED.**  C2(d) computes `G(m)=sup_t⟨𝒩_{W_m}²⟩`, not `Q̂_{W_m^c}²`, uses the wider `[-40,40]` grid, and captions the values as evidence that (ESC) fails. |
| m5 | MINOR | **FIXED.**  ⟨1⟩4.⟨2⟩7 says “one genuine leaf by content” and separately records that `memory-index.md` ⟨1⟩5.⟨2⟩1 cites LR2 but uses only the clause-1 TPM display.  MP-2 refers that cleanup to the owning lane. |
| m6 | MINOR | **FENCED by the explicit work order.**  The over-listed ASSUME line lies inside the critic-confirmed LR1 section, which this repair was ordered not to touch.  Its own ⟨2⟩7 already gives the exact weaker input list, and every summary/MP row uses that exact list.  No H3 dependence is claimed for LR1 outside the protected verbatim proof. |
| n1 | NOTE | **FIXED.**  C4(c) now checks the actual finite-chain calibration `⟨K|H_XXZ|K⟩=1.1456439081` against `C_K=1.1456439237`; the algebraic ratio identity is no longer presented as evidence. |
| n2 | NOTE | **FENCED by the explicit work order.**  The diagonal-selection wording is inside the protected, critic-confirmed LR1 proof and is unchanged.  LR1-GEN's class-level statement now explicitly starts with any prescribed diverging sequence and extracts a subsequence, making divergence manifest without modifying ⟨1⟩3. |
| n3 | NOTE | **RETAINED IN ITS SURVIVING FORM.**  Cross-lane consistency is now expressed only through LR3-SCOPE and `ACE-LD-obst′`; no D16 ballistic/non-ballistic classification is made. |

## Checker verification record

- `python3 -O theory/checks/lr_d16_check.py` → **exit 0**, 17/17 green.
- `python3 -O theory/checks/lr_d16_check.py --red-all` → **exit 1,
  RED-OK 17/17**.  Every mode reached exactly one registered row:

| mode | exit path |
|---|---|
| `c1-nonunitary` | C1(a) |
| `c1-noninteger` | C1(b) |
| `c2-unequal-time` | C2(a) |
| `c2-small-constant` | C2(b) |
| `c2-mismatched-complement` | C2(c) |
| `c2-delete-outside-data` | C2(d) |
| `c3-perturb-final-evolution` | C3(a) |
| `c3-mismatched-complement` | C3(b) |
| `c3-signed-majorant` | C3(c) |
| `c3-delete-majorant` | C3(d) |
| `c3-freeze-pinching` | C3(e) |
| `c4-wrong-gap` | C4(a) |
| `c4-kink-propagator` | C4(b) |
| `c4-sharp-calibration` | C4(c) |
| `c5-wrong-root` | C5(a) |
| `c5-overstrong-field` | C5(b) |
| `c6-identify-sharp-dressed` | C6(a) |

Each individual `--red MODE` evaluates its row group directly and requires
the failed-row list to equal the registered singleton; missed or collateral
paths exit 2.  Thus every row is reachable, no earlier gate masks a later
one, and no two mutants are bit-identical in effect.

## Merge-proposal disposition

- MP-1: re-proposed in the critic's binder/subsequence form.
- MP-2: HOLD; D16 does not satisfy its antecedent.
- MP-3: `LR1-GEN` and `LR-D16-EDW` proposed as PROVED; `LR-D16` stays HOLD.
- MP-4: retained unchanged, as ordered; it remains a shared-file proposal
  only and no shared file was edited.
