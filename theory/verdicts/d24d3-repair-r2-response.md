<!-- ROLE: r2 PROPOSER response to theory/verdicts/d24d3-adjudication-r1-critic.md
     FAIL(F1,F2,F3,M1–M7).  One row per objection.  Repaired artifacts:
     theory/verdicts/d24d3-adjudication-r2.md ("r2" below) and
     theory/checks/d24d3_normalization_check.py ("checker" below).
     No shared file was edited; all shared-file text is in r2 §5. -->

# r2 repair response — D24(d)3 adjudication

**Global shape of the repair (r1-critic's own preferred outcome, and the
r2 work order's strategy directive):** the value `L(0,h) = −iχ/(2ρ v_h)` is
**retired from the definition** (third horn F1(d′) adopted); clause 3 is
split into a well-posed kinematic hypothesis (3a) and a normalisation split
(3b) that keeps the frozen kinematic value `−iχ/v_h` (the corpus's
reciprocal LSZ energy denominator, F2) and carries the density in the
**named OPEN amputation lemma AMP** (`𝔞_leg = 1/(2ρ)`, `soft-index-r1.md`
F1(c)(i)); the matched value survives only as the **conditional CONJECTURE
row `D24-VAL`**.  No layer says "derived".

**Disposition count: 20/20 objections addressed — 18 FIXED, 1 RETRACTED
(M1: r1's strawman refutation withdrawn), 1 DOWNGRADED (M2: r1's ⟨1⟩3
demoted from load-bearing to consistency check), 0 RESIDUE.**

| id | sev | disposition | what was done | where |
|---|---|---|---|---|
| F1 | FATAL | **FIXED** (third horn adopted) | The `k ≠ 0` caveat restored and the `C¹` extension displayed as the hypothesis defining `L(0,h)` (M7(c) text verbatim); the matching restated as a *conditional implication* — (bridge) ∧ (member exists) ⇒ `𝔞_leg = 1/(2S)` — which quantifies over nothing asserted to be inhabited; "derived and not stipulated" appears in NO layer; the value itself removed from `definitions.md` and carried as CONJECTURE row `D24-VAL` with both conditions displayed.  F1(d′): evaluated and **adopted** — under "bridge holds ∧ class empty" the definition (which asserts no value) is untouched and `D24-VAL` is vacuous, exactly as a conditional row should be. | r2 §2 ⟨1⟩1, ⟨1⟩3 (esp. ⟨3⟩4 "status boundary"); §5.2 clauses 3a/3b; §5.3b |
| F2 | FATAL | **FIXED** (r1 §1.5 premise RETRACTED; option (i) taken) | r1's "L is never defined anywhere" withdrawn at r2 §1.2, replaced by the two-part truth: (narrow) no `notation.md` row / no `L :=` — repaired by §5.4a — and r1's grep missed `soft-index.md:161–162`; (substantive) the three provenance sites fix `L` as the reciprocal LSZ energy denominator, which cancels `Z_ρ` and *forces* the frozen value.  Consequence executed: the `1/(2ρ)` relocated OUT of `L` into the amputation constant `𝔞_leg` (open lemma AMP), so the merged definition now *agrees with* all three provenance sites instead of contradicting them. | r2 §1.2, §1.3, §2 ⟨1⟩2; §5.2 clause 3b; §5.4a (`L` row) |
| F3 | FATAL | **FIXED** | `Z_ρ := 2ρ` defined from `notation.md`'s `ρ`-row (`ρ := ω_α(S^z)` — state language, no ket, no D6 `|Ω⟩`); the su(2) fully-polarised reading `Z_ρ = ω_α([S^+_x,S^-_x])` marked "a special case, not a membership condition" (no su(2) smuggled into the class); the α-tail state fixes the sign (no β-tail flip ambiguity); the symbol is **subscripted** so bare-`Z` overload rule 9 is untouched, and it is registered. | r2 §5.2 preamble; §5.4a (`Z_ρ` row); §0 symbol paragraph |
| M1 | MAJOR | **RETRACTED** | r1's ⟨1⟩5 deleted, not repaired: the `(2ρN)^{-1/2}` route was the S1-A *critic's* counter-analysis, not either lane's claim; lane B's operative factor is the `N`-free per-volume density `1/(2ρ)` — the invariant this adjudication itself uses.  The correct statement (what IS refuted: the S1-A critic's proposed mechanism, giving `Z_ρ^{-1/2}`) is at r2 ⟨1⟩4.⟨2⟩2.  ROLE header corrected: the r2 header states plainly that the bookkeeping home is structurally lane B's split and that r1's was structurally lane A's.  §8's `tns-v44` instruction corrected at §5.5 item 3. | r2 ROLE header; §2 ⟨1⟩4.⟨2⟩2; §6 H4(ii); §5.5.3 |
| M2 | MAJOR | **DOWNGRADED** | r1 ⟨1⟩3 demoted: the residue's `Z_ρ`-linearity is a *consistency check of clause 2* (which needs no repair); "load-bearing step / where the density actually lives" and "that single cancellation is the entire defect" struck — the cancellation is the *correct* cancellation (r2 ⟨1⟩2.⟨3⟩3).  ⟨3⟩4 (HP two-insertion count) **deleted** and restated as the open question the critic demanded: the matched power is 1, a leg normalisation would give 1/2, so the AMP mechanism is not a leg normalisation. | r2 §2 ⟨1⟩4.⟨2⟩1, ⟨2⟩3; §6 H3 |
| M3 | MAJOR | **FIXED** (all five demands) | (i) C2's soft-leg-norm gate now CONSTRUCTS `Q^-_k|Ω⟩` from `apply_lowering` (mutant `c1_nosqrt` dies there, error `1.2e+01`; r1's `sites·two_s/sites − two_s ≡ 0` no-op removed); (ii) `lstsq(x,x)` replaced by a sympy solve of `(2S)^p = 2S` at `S ∈ {1,3/2,2}` (unique root 1; mutant `c2_wronglaw` dies there; `S = 1/2` degeneracy stated, not hidden); (iii) the acceptance gate C6 has an independent failure mode: band `0.02` vs C4's pre-registered `0.08` — data mutant `m2b_shift60` **passes C4 (0.064) and dies at C6** ; (iv) `decision_band` key now REQUIRED (`m4_noband` dies at C4 with a named message); (v) §7 reports the exit PATH for every red mode and every mutant, data was mutated (6 data mutants) not only code, and a gate-subsumption audit is applied to the new checker itself (C5 and the C6 fit are declared display-not-evidence; resolving power `p ∈ [0.989, 1.017]` printed every run). | checker (rebuilt, 459 loc); r2 §7.1–7.4 |
| M4 | MAJOR | **FIXED** | (i) The value claim fenced to `ρ = S ∈ {1/2,1,3/2,2}` in one model family with extension a hypothesis (AMP) — and, stronger, removed from the definition entirely, so no clause asserts anything "for every real ρ > 0"; the preamble's `2ρ ∈ ℤ` statement is conditional on its full hypothesis set.  (ii) The ANTISYMMETRY `ω_β(S^z) = −ω_α(S^z) = −ρ` restored to the `M-IDX-density` citation, labelled load-bearing. | r2 §5.2 preamble; §5.3b (`D24-VAL` scoping); §2 ASSUME |
| M5 | MAJOR | **FIXED** | Dedicated compliance subsection: §3.2 honoured strictly (value from on-shell input, matching hypothesis named and displayed, and additionally kept out of the definition); §3.5 honoured (no fully-polarised-vacuum object in the merged D24(d); `Z_ρ` is a GNS/state datum; `H_S` appears only inside the conditional row, scoped, per the critic's own M5(d) allowance). | r2 §4.5 |
| M6 | MAJOR | **FIXED** | All five missed sites added: `notation.md:244` and `:258` (𝒮_W rename — §5.4b/c), `ml5-universality.md:158` (two-site Wigner sentence — §4.2), and the three provenance sites plus `soft-index.md:161–162` (now in §1.2 and lockstep-consistent with the merge by relocation).  New §4.2b for `notation.md` as co-equal L4 single source; full row set in §5.4. | r2 §4.2, §4.2b, §5.4 |
| M7 | MAJOR | **FIXED** | Clause 3a merged text now reads exactly per M7(c): "well defined by clauses 1–2 for `k ≠ 0` at every `h` with `M_1^O(h) ≠ 0`; the hypothesis is that it extends to a process-independent, uniformly `C¹` function on `{|k| ≤ ε} × I`, and `L(0,h)` denotes that extension's value at `k = 0`."  The `L²`-vs-pointwise zero-set gap is acknowledged at r2 ⟨1⟩1.⟨3⟩1. | r2 §5.2 clause 3a; §2 ⟨1⟩1 |
| m1 | MINOR | **FIXED** | `𝔈^O` renamed `E^O_desc` throughout (non-fraktur, per the critic's suggestion); registered in §5.4a with the collision note (`𝔈_W` CP maps). | r2 §5.2 clause 1; §5.4a |
| m2 | MINOR | **FIXED** | Clause 2 states only the model-general `2i v_h M_1^O(h)`; the spin-`S` `Z_ρ`-linearity verification is a clearly-marked parenthetical (the markdown equivalent of the demanded footnote) citing D24N-C3, explicitly scoped to "the fully polarised spin-`S` tail" — no membership condition contains `J` or `sin h`. | r2 §5.2 clause 2 |
| m3 | MINOR | **FIXED** (dissolved) | D24(c) is now parametric in `𝔞_leg` and mentions no `ρ` at all — model-agnostic again, stronger than the demanded scoping sentence; the forward reference `(c) → (d)3b` is marked deliberate with the reason (`𝔠_h` is by definition the obstruction to the factorisation (d) predicts); `𝔞_leg = 1` recovers the frozen form in which D24(e)/`ml4_check.py` test it. | r2 §5.1 |
| m4 | MINOR | **FIXED** | "Four-density over-determination" language replaced everywhere by the true statement: the exponent is pinned by the exact law at any single `2S ≠ 1` (four densities = one analytic curve from one PROVED theorem); the `S = 1/2` row is degenerate and is dropped openly from the checker's data fit and checked symbolically for degeneracy. | r2 §2 ⟨1⟩3.⟨3⟩3; §3; checker `check_exponent` |
| m5 | MINOR | **FIXED** | The WM corroboration relabelled "consistent with, not exactly": WM's normalisation is `m = ρ` not `2ρ`; the factor 2 is fixed by the matching alone; `Z_ρ`-as-type-B-density kept as the good observation it is. | r2 §2 ⟨1⟩4.⟨2⟩4; §6 H3 |
| m6 | MINOR | **FIXED** | Bridge evidence cited as (R17) and `oracle-bethe.md` O9 only; the `ml5-universality.md` ⟨1⟩4.⟨3⟩4 mis-citation removed, with the correction recorded in H5. | r2 §6 H5 |
| n1 | NOTE | **FIXED** | The mis-anchored `paper/main.tex:338–339` citation is gone: its host step (r1 ⟨1⟩4.⟨3⟩4, the D13 corroboration paragraph) was not carried into r2. | r2 §2 (absence) |
| n2 | NOTE | **FIXED** | `paper/main.tex:542–546` now listed in §4.3 (with the critic's n2 finding that it survives, since it names no value). | r2 §4.3 |
| n3 | NOTE | **FIXED** | ERRATUM pointers (not edits) proposed for `soft-index.md` and `soft-index-b.md` heads, covering `soft-index.md:161–162` and `soft-index-b.md:757–758, 808`. | r2 §4.2 (failed-lane records); §5.5.2 |
| n4 | NOTE | **FIXED** (amendment proposed) | The pre-existing `χ`-overload tension recorded and a minimal one-sentence amendment to overload rule 2 proposed for the same `notation.md` merge pass; D24 text uses the argumented `χ(h,0)` at first display. | r2 §4.2b; §5.4d |

## Notes for the r2 critic (proactive disclosure)

1. **`ACCEPT_BAND = 0.02` is registered this round, not pre-registered in
   the data file.**  It was chosen as one order above the measurement
   scatter (max rel. dev. `0.0043`) and well inside C4's pre-registered
   `0.08`; it is not tuned to any mutant (the discriminating mutant
   `m2b_shift60` was constructed after the band was fixed).  Its purpose is
   structural: to give the acceptance gate a failure mode C4 does not
   imply.
2. **The critic's `−7.99%` shift dies at C4 here (`0.0839`), not at C6**,
   because this C4 checks per-row deviations and the true rows already sit
   ≈`0.4%` below `1/S`, so the shift lands just outside the C4 band.  The
   `−6%` mutant (`m2b_shift60`) demonstrates the same non-subsumption
   cleanly: C4 passes at `0.064`, C6 kills at `0.060 > 0.02`.  Exit paths
   for all mutants in r2 §7.2–7.3.
3. **m2's "footnote"** is implemented as a marked parenthetical inside
   clause 2 (markdown definitions have no footnote apparatus); the
   membership condition itself is the model-general residue factorisation
   only.
4. **What a PASS here does and does not license.**  It licenses merging
   §5.1–5.4 (a definition that asserts strictly less than the frozen one
   plus a CONJECTURE row); it does not close `tns-iu5` (re-scope per r2
   §8), does not touch `tns-axg`, and promotes nothing.
