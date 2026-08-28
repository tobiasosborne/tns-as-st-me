<!-- ROLE: proposer's r2 response ledger to theory/verdicts/ace-ld-r1.md
     (FAIL(F1,M1-M6): 1 FATAL, 6 MAJOR, 7 MINOR, 4 NOTE).  Work order:
     briefs/ace-ld-repair-r2.md.  One row per objection.  Lane:
     theory/ace-ld.md, this file, theory/checks/ace_ld_check.py. -->

# ACE-LD r2 — objection dispositions

All addresses below refer to the r2 `theory/ace-ld.md` unless marked (r1).
Disposition count: 18 objections — 1 FATAL, 6 MAJOR, 7 MINOR, 4 NOTE — all
addressed; 10 fixed by construction, 4 fixed by the F1 deletion (moot), 2
adopted as strengthenings, 1 partially deferred by lane (m7, split endorsed
via MERGE PROPOSAL), 1 flagged to the owning lane (n1).

| id | sev | disposition |
|---|---|---|
| F1 | FATAL | **ADOPTED IN FULL — deleted, not repaired.**  `(E-TAIL)`, `(V-ch)`, `(V-in)`, PROPOSITION ACE-LD-esc, COROLLARY ACE-LD, and r1's ACE-LD-obst are withdrawn (header deletion notice; HONEST STATUS "Refuted / withdrawn").  The false sentence "on the fixed-packet class of D28 the kink is ballistic" is deleted; everywhere D28 is mentioned it is now stated that D28(4) constrains only `v_M−v_K` and CONTAINS the static-kink class (header; ⟨1⟩5.⟨2⟩6(iii); MP-3(iv)).  No repaired hypothesis pair replaces the route: the positive content is rerouted through (AD3-ex-ε) per the work order.  The `(E-TAIL) ⟺ χ=1` equivalence that drives the emptiness is recorded once, with the two-line Cauchy–Schwarz proof, at ⟨1⟩4.⟨2⟩9(a).  D16's exact band flatness is re-certified independently (checker LD-C7, all 13 sectors, max `\|E_0\| = 8.2e-17`). |
| M1 | MAJOR | **Subsumed by the F1 deletion; the surviving content adopted.**  The scope sentence it attacked is gone.  The equivalence `(E-TAIL) ⟺ χ=1 S^z`-product vacua is stated AS an equivalence with proof (⟨2⟩9(a)); the same boundary is imposed on the new route as an explicit scope statement: (K-TAIL) families with vacuum-relaxing tails have `χ=1` product tail vacua, so the ε-version is claimed for the sharp-tail corner only, never for generic MPS vacua (⟨2⟩9(b); ACE-LD-eps row's not-claimed clause).  The `χ>1` refutation of (A4) is moot — (A4) is no longer claimed on any MPS class.  The out-of-class AKLT illustration is deleted (see n3). |
| M2 | MAJOR | **ADOPTED AS THE ROUND'S NEGATIVE RESULT.**  ACE-LD-obst′ (§0 + ⟨1⟩5) is the critic's (d)-statement verbatim in strength: hypotheses H-MQG(1)–(3), D26(INT), D27(LR1)–(LR2), and (M-ESC) (mean tail transport `θ>0`) ONLY — no `(E-TAIL)`, `(V-ch)`, `(V-in)`, `σ_L≠σ_T`, `⟨3⟩1`, no channel structure, no D28.  Proof route = the critic's: D27's own first-moment identity (MI ⟨1⟩7.⟨2⟩1–⟨2⟩2, cited) + the `M_0` bound (LD-M0) + LD-ESC-MEAN (`θ = p_tr` from means alone).  The two-atom law is demoted to numerically exhibited evidence (⟨2⟩6(ii)), not a theorem — its r1 hypothesis class was empty. |
| M3 | MAJOR | **FIXED — LD-C5 rebuilt on a genuine scattering configuration.**  Barrier model (`N=2048`, dense eigh), incoming packet from the left: the `ν=0` atom is PRODUCED (measured `p_0 = 0.2704`), weights match independently measured `\|r\|²,\|t\|²` to `1e-3`, the incoming-concentration defect is gated (`<1e-4`), and the MI ⟨1⟩7.⟨2⟩2 identity is certified directly against the state (`1e-4` agreement at all four windows).  Three registered red modes reach LD-C5 (`--red-c5-nobarrier` → atom gate, `--red-c5-meanshift` → identity gate (data mutation), `--red-c5-inwindow` → concentration gate).  The demanded static contrast exists: LD-C6 certifies `p_W = δ_0` with LR3 tail `0`, red-armed by `--red-c6-moving`. |
| M4 | MAJOR | **FIXED.**  r1's MP-2 (compound non-status) is withdrawn.  The `AD3-ex` row stays **CONJECTURE**; the regime split is recorded in row prose only (MP-2), exactly as the adjudicated rows record theirs.  All MP-1 statuses are bare L5 values; every proposed row closes with a not-claimed enumeration (register comparison of verdict §6 adopted). |
| M5 | MAJOR | **FIXED — reading named at every occurrence.**  What r2 supplies is the KINK-eigenstate reading of D18(AD3), ε-weakened to norm form (⟨2⟩8, first bullet); the vacuum-eigenstate reading appears nowhere (its route was deleted).  Explicitly NOT supplied: D18(AD3)'s weak-\* clause and M-INDEX-spec's reduction clause, whose adjudicated scoping is untouched (⟨2⟩8(iii); MP-3(iii); ACE-LD-eps row). |
| M6 | MAJOR | **FIXED.**  (i) The "tests the CONSTANT" claim is deleted; LD-C3 now reports and gates the informative statistic `max_t lhs/rhs` (measured `0.168`; green-only liveness floor `0.10`) and its docstring states what it does and does not certify.  (ii) The constant-shrink mutation is renamed `--red-gap`; `--red-coset` is now a TRUE coset mutation (edge eigenvalue `+ (√2−1)`, gap preserved `≥1`) registered so that LD-C1's coset gate breaks and **LD-C3 survives** — certifying that (LD.3) consumes the gap, not the coset.  (iii) §5 now states the constant is ASSERTED at `1` per ⟨1⟩1.⟨2⟩3, not computed from the spectrum; implementing §5 verbatim reproduces the shipped code (`--red` exit 1 verified). |
| m1 | MINOR | **FIXED.**  `--red-halfspace` (real-space half-line channels) is registered and fires LD-C1's commutation gate at `[P_+,H] = 5.3e-01` — the critic's own mutation, now armed; LD-C2/C3/C4 registered to survive and do. |
| m2 | MINOR | **MOOT by deletion.**  The misaddressed pointer (§0 esc PROVE → ⟨1⟩5.⟨2⟩3) was in deleted text; no uniqueness claim (LD-UNIQUE) survives in r2 (noted at ⟨1⟩3.⟨2⟩5). |
| m3 | MINOR | **FIXED.**  `w_1 > 0` is in ACE-LD-nec's §0 ASSUME, with a marker naming ⟨1⟩3.⟨2⟩4 as the consuming step. |
| m4 | MINOR | **FIXED — spec/code lockstep.**  §5 states `N = 8192` (FREE), no detune (removed from spec AND absent in code), and the asserted (not computed) constant; every quoted number in §5 is from the shipped run. |
| m5 | MINOR | **FIXED.**  ACE-LD-abs row carries no depends-on (unconditional given ASSUME; M-INDEX-fin cited in the instance rows only).  M-INDEX-spec appears on no proposed row. |
| m6 | MINOR | **FIXED.**  MP-4 introduces only `𝒬_{c_0}φ`, `(K-TAIL)`, `(K-Q)`, `(M-ESC)`, `θ` — grep-checked against `notation.md` (no hits); the colliding `q_±(W,c_0)`/`σ_ch` rows died with the r1 route. |
| m7 | MINOR | **PARTIAL (lane-limited).**  The obstruction split into its own shard is ENDORSED and requested via MP-5, but `theory/` shard creation is outside this lane's writable set.  The overrun (~1030 lines) is self-reported in HONEST STATUS. |
| n1 | NOTE | **FLAGGED to the owning lane.**  The `ν`-orientation flip in AS ⟨1⟩7.⟨2⟩1 vs the frozen `ν = q_- − q_+` is flagged at ⟨1⟩4.⟨2⟩7 and in MP-3's closing parenthesis; r2 uses only the frozen convention (LD-C5 computes `ν = q − q'`) and consumes only `\|ν\|` from AS. |
| n2 | NOTE | **MOOT / re-formed.**  The ill-formed `sup_m`-with-free-`m` display was in deleted text; ACE-LD-obst′(b) quantifies per-`M`: `sup_m Σ_{\|ν\|>M}(1+\|ν\|)p_{W_m} = ∞` for every `M`, derived via `Σ_{\|ν\|>M}(1+\|ν\|)p ≥ \|Σνp\| − M`. |
| n3 | NOTE | **MOOT by deletion.**  The out-of-class (`s=0`) AKLT illustration is gone; no in-class substitute is needed since no (E-TAIL)-style hypothesis survives. |
| n4 | NOTE | **MOOT by deletion.**  `C_a` and `2M_W'` lived in the deleted r1 ⟨1⟩4; no constant in r2 mixes operator and vector norms (the only constants are `C_K`, `ε_Q`, `M_0`). |

## Checker verification record (this round)

- `python3 -O theory/checks/ace_ld_check.py` → **exit 0**, LD-C1..LD-C7
  all pass (61 s).
- `python3 -O theory/checks/ace_ld_check.py --red` → **exit 1, RED-OK**,
  13/13 modes reproduce their registered patterns, with per-mode exit
  paths logged.  Gate reachability (exit path per mode): LD-C1 gap ←
  `gap`; LD-C1 coset ← `coset`; LD-C1 commutation ← `halfspace`; LD-C2 ←
  `merged`, `dup`; LD-C3 ← `gap` (and survives `coset`, `halfspace`,
  `merged`, `dup` as registered); LD-C4 ← `merged`, `dup`; LD-C5 atom ←
  `c5-nobarrier`; LD-C5 identity ← `c5-meanshift`; LD-C5 concentration ←
  `c5-inwindow`; LD-C6 ← `c6-moving`; LD-C7 rate ← `c7-delta`; LD-C7
  coset ← `c7-mixed`; LD-C7 defect-positivity ← `c7-product`; LD-C7
  flat-band ← `c7-noboundary`.  No gate is unreachable; no red mode is
  bit-identical in effect to another (the `coset`/`gap` pair differ in
  which gates break, by registration).
