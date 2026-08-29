<!-- ROLE: proposer's r4 response ledger to theory/verdicts/ace-ld-r3.md
     (FAIL(F1,M1-M3): 1 FATAL, 3 MAJOR, 8 MINOR, 6 NOTE — and three
     promotions approved on cells section 8(A)-(D), conditional on the
     section 8(E) preconditions).  Work order: briefs/ace-ld-repair-r4.md.
     One row per objection.  Lane: theory/ace-ld.md, this file,
     theory/checks/ace_ld_check.py. -->

# ACE-LD r4 — objection dispositions

All addresses below refer to the r4 `theory/ace-ld.md` unless marked (r3).
Disposition count: **18 objections — 1 FATAL, 3 MAJOR, 8 MINOR, 6 NOTE —
all addressed**: 1 adopted in full by RESTATEMENT (F1: ACE-LD-χ retired,
ACE-LD-sharp stated at the critic's §8(D) strength, the `χ=1` form
recorded as REFUTED with the counterexample), 10 fixed by construction,
4 adopted as disclosures/strengthenings (n1 additionally CLAIMED, as the
brief instructs), and 3 credits requiring no action (n4, n5, n6).  The
r3 verdict's §5 fence (17 items, incorporating r2 §5's 14) is untouched:
no fenced step was reworked — the F1 restatement rewrites exactly the
sites F1(a) enumerates, and §5 item 6 fenced precisely the clauses
(`s_γ ∈ spec S^z`, the spin-1 exclusion, zero on-site variance) that the
restatement keeps.

**The two §8(E) merge preconditions are discharged in this revision:**
(1) the F1 sharp-charge correction is applied throughout the shard — §0
(SCOPE and the theorem statement), ⟨1⟩4.⟨2⟩9(a), ⟨2⟩9(b)⟨3⟩3, the ⟨2⟩9
closing paragraph, the r1 deletion notice, HONEST STATUS (three
buckets), and MP-1 — in the same revision that carries the promotion
cells, so rows and shard cannot diverge; (2) MP-4 now binds exactly the
five §8(E) symbols (`𝒬_{c_0}`, `(K-TAIL)`, `(K-Q)`, `(M-ESC)`,
`θ_{tr}`) with **string anchors, not line numbers** (insertion point
anchored to the `δx` (asymptotic) / `Γ_K` rows of the ML4/ML5/M-quant
table; the `θ` overload flagged against the `μ_∞^α` row by content), and
is marked as a merge precondition of MP-1.

| id | sev | disposition |
|---|---|---|
| F1 | FATAL | **ADOPTED IN FULL — THEOREM ACE-LD-χ is RETIRED and restated as THEOREM ACE-LD-sharp** (the critic's §8(D) cell is the target text; the id `ACE-LD-χ` is not reused).  The conclusion is now sharp on-site charge — `ω_γ((S^z_x−s_γ)²) = 0`, equivalently `ω_γ(Π_x^{(s_γ)}) = 1`, at every site — hence `±s ∈ spec S^z`; the spin-1-at-`s=1/2` exclusion and the exclusion of every nonzero-variance vacuum (generic injective MPS) survive unchanged, exactly as F1(d) certifies.  The unqualified `χ=1` clause is recorded as **REFUTED under H-MQG(1)--(2) alone**, with the critic's `ℂ²⊗ℂ³` counterexample (`S^z = σ^z/2 ⊗ 𝟙_3`, `|↑⟩/|↓⟩ ⊗ AKLT` vacua, injective, `χ=2`, transfer gap `1/3`, `D_xφ ≡ 0` so (K-TAIL) at `C_K = 0`) quoted in §0 and in HONEST STATUS "Refuted / withdrawn"; the surviving conditional (simple `s_γ` ⟹ `χ=1` product vacua) is kept as a corollary, not the theorem.  Applied at every F1(a) site: §0 THEOREM statement; §0 ACE-LD-ε SCOPE; ⟨1⟩4.⟨2⟩9(a) (the equivalence is with sharp on-site charge; the product-state continuation is marked correct only under simplicity); ⟨2⟩9(b) proof head and ⟨3⟩3 (rewritten, with the retired clause quoted and struck); the ⟨2⟩9 closing "corner" paragraph; the header status item 4; the r1 deletion notice's `(E-TAIL)` equivalence (corrected with a note that the emptiness argument is unaffected — every instantiated model has simple `s_γ`); HONEST STATUS "Proved" bullet (now ACE-LD-sharp), "Proved conditionally" forced-scope clause, and a new "Refuted / withdrawn" entry; MP-1's eps row now carries the r3 §8(A) cell (the r2 §8(A) sentence, withdrawn by its own author, is gone).  Applied in the same revision as the promotion cells — §8(E) precondition 1. |
| M1 | MAJOR | **FIXED — the quantifier is restored in both places.**  MP-3(ii) now reads "propagates … to every larger window `W'` whose annulus `W'∖W` carries no escaped charge — equivalently, every `W'` the leg has already passed beyond — …; at the first `W'` that reaches the leg the difference is exactly the leg charge (LD-ID ⟨3⟩3), so the transport is not available past that window" — M1(c) verbatim in substance — with a note recording that the r3 compression was refuted by the shard's own ⟨3⟩3 (`2s = 1.0000` measured against an asserted `4.25e-22`).  ⟨2⟩7's LEMMA LD-MONO closing PROVE gloss takes the same quantifier, so the gloss now matches its own ASSUME (which fixes one `W'` with the (K-TAIL) bound on the annulus).  The lemma itself is untouched — M1(d) fences it as correct as ASSUMEd.  Clauses (i), (iii), (iv) of MP-3 are unchanged. |
| M2 | MAJOR | **FIXED — LD-C5b is re-anchored at D27(LR2)'s own quantity and the finding is republished at the corrected number.**  The wedge gate (`6.0832` at `(t_-,t_+) = (0,300)`) is kept but relabelled: it certifies ONLY that `𝒟` acts (the r3 inference "wedge ⟹ LR2 fails" is recorded as invalid — the `V_0 = 0` straddling packet has `t_-=0` defect `−8.3868`, passes the wedge gate, and satisfies LR2 exactly).  NEW gate: the **double-Cesàro defect** — mean of `⟨𝒟_{W,t_-}(Q̂_W(t_+))⟩ − ⟨Q̂_W(t_+)⟩` over `9×9` grids on `[T,2T]×[−2T,−T]` — measured **`−3.3592` at `T = 20` and `T = 40`** (reproducing r3 M2(b) to every digit; the proposer also reproduced `−3.3592` at `T = 80`, and the `t_-=0` values `−6.0832`/`−8.3868`, in an independent scratch run before repairing the gate), gated at floor `3.0` keyed to `3.359` with a `T`-stability gate at `0.02` (measured spread `~3e-5`).  The mechanism is named and logged with measured values: the backward-evolved packet stays split across three window-charge branches `0.8563/0.0170/0.1267`, identical at `t_- = −80` and `−400`; the bound state is not the cause (r3 M2(b): `−3.4116` with it projected out).  The green log line "LR2 fails pointwise AND on average here (measured)" is DELETED — the average is now actually computed and quoted instead.  `--red-c5b-nobarrier` registers the `V_0 = 0` straddling model against the corrected gate: it passes the wedge and dies at the double-Cesàro gate (`−1.997e-04` at `T=20`), which is exactly the separation of "`𝒟` acts" from "LR2 fails".  Corrected number propagated to §5, HONEST STATUS "Merely evidence", and the checker docstring; the r3-response row M4(v)'s "measured before gating" framing is superseded by this row. |
| M3 | MAJOR | **FIXED — all three demands.**  (i) §5's unreached list is now a COMPLETE enumeration (10 items), each with its shadowing gate or guard status named — including the two the critic fired on a copy: LD-C7(e)'s profile-ratio sub-gate (shadowed by the `C_K` gate; teeth per r3 M3(b)) and LD-C6's first moment (now REACHED, see (ii), so it moved from the list to the table); also the LD-C5 transit-atom, off-atom-mass, and transmit-weight-half sub-gates, LD-C2's monotone-decrease sub-gate, and the three construction/protocol guards.  (ii) `check_c6` reordered: the first-moment gate is evaluated BEFORE the support gate, and `--red-c6-moving` now exits there at `12.4024 > 1.2` at `|W|=17` — the critic's shadow-disabled figure, now a registered exit path; NEW mode `--red-c6-weaktransit` (`V_0 = 10`, `|t|² ≈ 0.037`) passes the moment gate (`0.6361`) and dies at SUPPORT (`3.742e-02`), keeping that gate armed post-reorder.  (iii) `C6_MOM_BOUND` raised to `1.2`, above the recorded `t_+`-sweep maximum, and the sweep itself is now a gate: `Σ|ν|p ≤ 1.2` at every window at every `t_+ ∈ {4, 20, 40, 200}` — measured maximum `1.0712` at `t_+ = 20`, `W = [3,8]` (the critic's firing value, reproduced independently), full sweep recorded in §5.  Support/liveness stay at the protocol time; disclosed in §5 and in the gate docstring. |
| m1 | MINOR | **FIXED.**  LD-ID's theorem-level ASSUME now lists the per-clause hypotheses (⟨3⟩1: H-MQG(1)--(2) only; ⟨3⟩2: + limit existence ((K-TAIL) suffices) and D13(c); ⟨3⟩3: + D18(AD3) and `t`-independent (K-TAIL); ⟨3⟩4: + (K-Q) at `ε_Q = 0`, `t`-uniform data, D27's `δx`), and the HONEST STATUS bullet is split into the unconditional and conditional halves accordingly — matching cell §8(C)'s status line. |
| m2 | MINOR | **FIXED (L6b).**  ⟨3⟩3's justification now displays the leaf: `‖Σ_{x∉W}D_xΨ_t‖ ≥ |⟨Ψ_t, Σ_{x∉W}D_xΨ_t⟩| = |Σ_{x∉W}ω_{Ψ_t}(D_x)|` by Cauchy--Schwarz, with D18(AD3) sending the mean to `q_leg`. |
| m3 | MINOR | **FIXED.**  The `θ_{tr} = 0` fence now names its condition in all the places this lane can write: §0 obst′ Scope, ⟨1⟩5.⟨2⟩6(iii), and MP-6 each say M-quant-G's conclusion is PROVED **conditional on H-AD-G, i.e. D18(AD1)--(AD4) for that vector** (open for D16, bd `tns-d51`; `AD3-ex` CONJECTURE), and each adds the disjoint-classes sentence (D18(AD3) jointly unsatisfiable with (K-TAIL) by LD-ID ⟨3⟩3, so the fence and the ε-theorems concern a kink--magnon D17 packet under H-AD-G versus a magnon-free (K-TAIL) state).  MP-1's obst row is cell §8(B), which carries m3's wording verbatim. |
| m4 | MINOR | **FIXED.**  The depends-on stays as the critic rules (M-INDEX-spec on no row); the sub-step qualification travels in cell §8(B) ("the first-moment identity is consumed at the level of MI ⟨1⟩7.⟨2⟩1--⟨2⟩2, whose leaf justifications carry only D27(LR1)--(LR2) and (IDX.1)") and is repeated in MP-1's register note. |
| m5 | MINOR | **FIXED.**  MP-6 is re-cited: the composition `(M-ESC) ⟹ ¬(NR)` now follows DIRECTLY from `theory/lr-d16.md` ⟨1⟩5.⟨2⟩7 THEOREM (LRD-3) (`(NR) ⟹ D27(LR3)`, tail `2S_{NR}/M`; `(NR)` in its repaired two-clause `sup_m` form, `theory/verdicts/lr-d16-r2.md`) composed with ACE-LD-obst′(b); the appeal to lr-d16 ⟨1⟩5.⟨2⟩4's monotonicity remark is dropped as superseded, ⟨1⟩5.⟨2⟩6(iv) re-derives the route the same way, and the no-witness disclosure (lr-d16-r2 M4(b)3 + ace-ld-r2 m7) travels inside MP-6's constraint paragraph.  HONEST STATUS's (M-ESC) bullet cites both lr-d16 verdicts. |
| m6 | MINOR | **FIXED by cell substitution.**  MP-1's eps row is cell §8(A) verbatim, whose incompatibility clause carries "with `t`-independent `(K, C_K, λ̃)`" exactly as m6(c) demands (the r3 row, which dropped it, is gone). |
| m7 | MINOR | **FIXED.**  The L2 self-report now states the measured count (1785 lines at r4, with the r3 miscount 1447-vs-~1200 recorded) and MP-5 remains the requested split, endorsed a third time by r3 §9. |
| m8 | MINOR | **FIXED.**  The checker docstring no longer advertises `--table`; it states that the reachability table and the complete unreached list live in §5 of the shard.  No phantom flag remains (`--table` was never implemented; the sentence is deleted rather than the flag added, since §5's table carries measured exit paths a registry dump could not reproduce). |
| n1 | NOTE | **ADOPTED AND CLAIMED** (per the work order).  The equivalence of (K-TAIL)'s off-diagonal and on-site clauses (Cauchy--Schwarz on self-adjoint `D_x`) is stated in §0's (K-TAIL) box, with the consequence that **LD-C7(e) certifies (K-TAIL) in full** claimed in §0, §5's (e) bullet (citing the critic's measured off-diagonal ratio `1.0000` on the diagonal), HONEST STATUS, and MP-4's (K-TAIL) row; (K-TAIL) is described as an on-site tail-decay hypothesis, not clustering; ⟨2⟩2(i) carries the triangle-inequality remark without reworking the fenced derivation. |
| n2 | NOTE | **ADOPTED.**  §0 obst′'s disclosure now says the `M_0` route is a STRICT strengthening of D27's existence corollary — full-sequence convergence needs D27's optional convenience clause, otherwise only an (LR3) subsequence, whereas ⟨2⟩3 is `sup` over all `m` with neither — matching cell §8(B)'s wording. |
| n3 | NOTE | **ADOPTED.**  §5 marks wall clocks as machine-local (green 50 s, red 99 s on the shipping machine after the r4 gates). |
| n4 | NOTE | Credit for `--red-c6-static`; no action.  The mode and its exit path (`1−p_0 = −2.220e-16`) are unchanged in r4 and reproduce. |
| n5 | NOTE | Credit for the corrected `c1-leak` registration; no action.  Exit paths unchanged and reproduced. |
| n6 | NOTE | Credit — the refusal of the seventh no-op stands and is now doubly recorded (§5 design decision (i) cites the r3 n6 certification).  What the substitute gate measures is repaired under M2. |

## Checker verification record (this round)

- `python3 -O theory/checks/ace_ld_check.py` → **exit 0** (50 s,
  machine-local), LD-C1..LD-C7 all pass, including the NEW LD-C5b
  double-Cesàro gate (measured `−3.3592` at `T = 20` and `T = 40`,
  spread `< 1e-4`, branch weights `0.8563/0.0170/0.1267` at
  `t_- = −80` and `−400`) and the NEW LD-C6 sweep gate (max `Σ|ν|p =
  1.0712` at `t_+ = 20`, `W = [3,8]`, bound `1.2`).
- `python3 -O theory/checks/ace_ld_check.py --red` → **exit 1, RED-OK,
  23/23** (99 s), per-mode exit paths logged.  All 21 r3 exit paths
  reproduce digit for digit except the one the r3 verdict's own fix
  demand changes: `c6-moving` now exits at the FIRST-MOMENT gate
  (`12.4024 > 1.2` at `|W|=17` — the critic's shadow-disabled figure)
  instead of the support gate.  New modes: `c5b-nobarrier` (passes the
  wedge at `8.3868`, dies at the double-Cesàro gate, `−1.997e-04` at
  `T=20`) and `c6-weaktransit` (moment `0.6361` passes, dies at
  SUPPORT, mass `3.742e-02`).
- Independent pre-repair reproduction (proposer scratch, before any
  gate was written — red-green discipline): double-Cesàro defect
  `−3.3592` at `T = 20, 40, 80` on the shipped state; `−2.0e-04`,
  `−1.7e-06`, `−3.2e-09` on the `V_0 = 0` state; `t_-=0` defects
  `−6.0832` / `−8.3868`; branch weights `0.8563/0.0170/0.1267`; sweep
  `1.0712` at `t_+=20, W=[3,8]` — every figure of r3 M2(b)/M3(b)
  confirmed to the printed digit before being keyed into a gate.

## Promotion readiness (ace-ld-r3 §8)

- MP-1 carries cells §8(A)--(D) VERBATIM (machine-transplanted from the
  verdict; pipe-escaping only), as rows `ACE-LD-eps`,
  `ACE-LD-obst-prime`, `LD-ID`, `ACE-LD-sharp`.
- §8(E) precondition 1 (F1 applied shard-wide, same commit): DONE in
  this revision.
- §8(E) precondition 2 (MP-4 binds `𝒬_{c_0}`, (K-TAIL), (K-Q),
  (M-ESC), `θ_{tr}`; merges with or before the rows): MP-4 is
  string-anchored, complete, and marked as MP-1's precondition.  Its
  deltas from the r3 draft the critic approved, disclosed: (i) the
  `line 271` reference is replaced by the `μ_∞^α`-row content anchor
  and an explicit insertion-point anchor is added (the r4 brief's
  string-anchor requirement); (ii) the (K-TAIL) row gains the n1
  on-site-equivalence parenthetical; (iii) a preamble reproduces the
  §8(E) symbol audit (already-bound vs cell-inline symbols) so the
  merge is self-checking.  No frozen row is touched and no new symbol
  beyond the five is bound.
- Two tested-in sentences inside cells (A) and (B) describe the r3
  checker run (21/21; the r3 M3 caveats); the r4 delta notes under MP-1
  ask the critic to bless updated wording — the cells are otherwise
  merge-ready untouched.
