<!-- ROLE: proposer's r3 response ledger to theory/verdicts/ace-ld-r2.md
     (FAIL(F1,M1-M6): 1 FATAL, 6 MAJOR, 8 MINOR, 6 NOTE).  Work order:
     briefs/ace-ld-repair-r3.md.  One row per objection.  Lane:
     theory/ace-ld.md, this file, theory/checks/ace_ld_check.py. -->

# ACE-LD r3 — objection dispositions

All addresses below refer to the r3 `theory/ace-ld.md` unless marked (r2).
Disposition count: **21 objections — 1 FATAL, 6 MAJOR, 8 MINOR, 6 NOTE —
all addressed**: 1 adopted in full by RETRACTION (F1: the bridge is
withdrawn, not repaired), 1 adopted as a new THEOREM (M1 → ACE-LD-χ),
12 fixed by construction, 5 adopted as disclosures/strengthenings,
1 partial by lane limits (m8: the L2 split stays a MERGE PROPOSAL), and
1 handled by renaming in merge text only (n2).  The r2 verdict's §5
fence (items 1--14) is untouched: no fenced step was reworked.

| id | sev | disposition |
|---|---|---|
| F1 | FATAL | **ADOPTED IN FULL — the bridge is RETRACTED, not repaired.**  The r2 claim that ACE-LD-ε-x supplies what AS ⟨1⟩7.⟨2⟩2 consumes is withdrawn as FALSE everywhere it stood: §0 item 3 (rewritten), the r2 ⟨1⟩4.⟨2⟩7 (deleted whole), ⟨1⟩4.⟨2⟩8's first bullet (rewritten; new bullet (vi) states the retraction), MP-1's `ACE-LD-eps` row (now the verdict's §8(A) adjudicated scoping sentence VERBATIM, with the AS-supply and "Compatible with D27(LR3)" clauses gone), and **MP-3(ii) is WITHDRAWN** (MP-3 now says so explicitly and states the true relationship instead).  The critic's identification is adopted as THEOREM LD-ID (new ⟨1⟩4.⟨2⟩7): `Q̂_{W,c_0} = Σ_{x∈W}(S^z_x − s_{γ_{c_0}}(x))` exactly (⟨3⟩1); `𝒬_{c_0} = 2s(X_1−c_0)` is D13(c)'s exactly conserved charge and (K-TAIL) is "no charge escaped the core" (⟨3⟩2); joint unsatisfiability with D18(AD3)'s escaping-leg clause, hence NO instance on the AS ⟨1⟩7 channel class and no `q_L ≠ q_T` within one D18 sector (⟨3⟩3); `δx = 0` on the `ε_Q = 0` class (⟨3⟩4).  The true relationship is stated in the header retraction notice, at ⟨2⟩7, in §0, and in HONEST STATUS: **the ε-version is a theorem about states whose charge has NOT escaped; the ordered-limit consumer needs the opposite regime.**  The verdict's F1(d) survivors are both kept: the ε-theorems stand as conditional implications on their own ASSUME blocks, and the window-monotonicity LEMMA LD-MONO (anchor-free, uniform in `W'`, compatible with an escaped leg — the honest offering to the AS lane) is proved at ⟨2⟩7 and offered via MP-3(ii)'s replacement text. |
| M1 | MAJOR | **ADOPTED AS A THEOREM.**  New THEOREM ACE-LD-χ (§0): (K-TAIL) + D9 kink-class membership FORCES `χ=1` `S^z`-product tail vacua with `s ∈ spec S^z`; proof in Lamport form at ⟨1⟩4.⟨2⟩9(b) (⟨3⟩1--⟨3⟩3), with D9(a) supplying the weak-\* tail relaxation — the r2 "if the far tails relax" hedge is gone, as is the remark-level status.  The `s ∈ spec S^z` consequence (spin-1 at `s = 1/2` excluded by arithmetic) is stated in the theorem.  Placed in ALL THREE demanded locations: §0 (SCOPE clause of THEOREM ACE-LD-ε, in M1(c)'s words: "(K-TAIL) entails `χ=1` `S^z`-product tail vacua with `s ∈ spec S^z`; the theorem is claimed for that corner only"), HONEST STATUS ("Proved conditionally" bullet, verbatim clause), and MP-1's `ACE-LD-eps` row (the §8(A) sentence carries it in its not-claimed-adjacent clause). |
| M2 | MAJOR | **FIXED — the stronger true statement, not called a contrapositive.**  In all three places (§0 PROPOSITION ACE-LD-obst′(c); ⟨1⟩5.⟨2⟩4's closing; MP-1 `ACE-LD-obst-prime` row) the closing statement is now M2(c) verbatim: "⟨2⟩3 gives directly: on any (LR) state the mean wall transport is uniformly bounded, `sup_m|ω^+_{W_m}(𝔛_{W_m})−ω^-_{W_m}(𝔛_{W_m})| ≤ (M_0+1)/(2s)`; in particular `θ = 0`" — `O(1)`, not `o(\|W_m\|)`, and the word "contrapositive" is deleted (the liminf quantifier slip is named in §0's replacement note).  The n1 subsumption disclosure sits beside it in all three places. |
| M3 | MAJOR | **FIXED — LD-C6 rebuilt on a battery whose dynamics does NOT commute with `Q̂_W`.**  New LD-C6: the D16 battery with one magnon added (`S^-` at site 10 on the half-filled kink ground state, evolved in the `n_↓ = 7` sector, `t_+ = 4`).  Measured: `1 − p_0 = 0.017/0.402/0.423/0.453` across the four windows (liveness gate `≥ 0.02` at the largest — the r2 tautology CANNOT pass this); TPM support bounded (`\|ν\| ≤ 3`, out-mass `≤ 9.1e-13 < 1e-9`); `Σ\|ν\|p ≤ 0.453 ≤ 1.0`, non-extensive — the demanded static-kink contrast against LD-C5's `ν = −\|W\|` transit atom.  Two mutations OF THAT gate registered: `--red-c6-static` runs the new gates on the r2 LD-C6's own position-diagonal model class and dies at the LIVENESS gate (`1−p_0 = 0`) — the sixth no-op is now itself a detected mutant — and `--red-c6-moving` (transit model) dies at the SUPPORT gate (mass `0.73` at `\|ν\| > 3`). |
| M4 | MAJOR | **FIXED.**  (i) §5's blanket reachability sentence and the "independent computations" / "no other gate pair is deductively linked" notes are DELETED; §5 now publishes the per-mode reachability TABLE (measured exit paths) plus an explicit "honest unreached rows" list.  (ii) Disclosed: C5(d) is implied by C5(a) (gap `~4e-11`, tracking the concentration defect — the r2 `1e-4` framing is gone); C5(e)'s floor is implied by (b)+(c) (`1 > 0.9`); both are demoted to consistency lines, not evidence (HONEST STATUS and MP-1 cells updated to match — r2 §8(B) adopted).  (iii) Gates (c) and (e-growth) now REACHED: `--red-c5-weights` (data mutation of the measured `\|r\|²`; fires the weight gate) and `--red-c5-fixedwin` (degenerate exhaustion; fires the tail-growth gate).  The floor clause of (e) is provably unreachable in-class (any mutation breaking it breaks (b)/(c) first) and is listed as such — disclosed, not blanket-claimed.  (iv) LD-C1's orthogonality and resolution sub-gates armed: `--red-c1-overlap` (orthogonality, `6.455e-02`) and `--red-c1-leak` (resolution, `8.068e-02`), measured patterns registered.  (v) The two-branch demand: MI ⟨1⟩7.⟨2⟩2 is NOT certified by a two-branch identity gate — that would be `x ≡ x` against the same branch decomposition (no-op pattern; deliberately not shipped, recorded in §5) — instead NEW gate LD-C5b certifies the dephasing WEDGE in a straddling configuration: `Σνp = +0.368` vs unpinched `⟨Q̂⟩_-−⟨Q̂⟩_+ = −5.716`, wedge `6.083` — measured proof that `𝒟` acts, that D27(LR2) genuinely FAILS on a two-branch state (the defect saturates; it does not Cesàro-decay — measured before gating, and the planned decay gate was discarded for certifying a falsehood), and hence that C5(d)'s agreement is due to gate (a).  Armed by `--red-c5b-flat` and `--red-c5b-concentrated`. |
| M5 | MAJOR | **FIXED — justification replaced in all four places** (⟨1⟩5.⟨2⟩6(iii); §0 obst′ Scope; MP-1 obst row not-claimed clause; MP-6), each now per M5(c): every state in the closed span of the K1--K2 family is exactly stationary (K1+K2 PROVED; `ker H_kink` exhaustion is **K4, CONJECTURE**), kink--magnon mean wall transport is bounded by `⟨N_T⟩/s` (M-quant-G's conclusion, not band flatness), so `θ = 0`; LD-C7(a) certifies only the sector ground energies at `L = 12`.  The same K4-strength upgrade inside ⟨1⟩4.⟨2⟩4 ("true because the band is exactly flat") is fixed the same way, and the surviving r2 deletion-notice paragraph carries an r3 register note.  The conclusion `θ = 0` for D16 STANDS on the corrected support. |
| M6 | MAJOR | **FIXED.**  MP-2 and its three companions (⟨1⟩4.⟨2⟩8(i); HONEST STATUS "Refuted/withdrawn"; MP-3(i)) rewritten per M6(c): D16's exact kink states are never `Q̂_{W,c_0}` eigenvectors at finite `W` (defect `4.45e-02 … 4.05e-04`, decaying as `q^{d_W}`), so D18(AD3)'s eigenstate clause can hold at fixed `W` only in ε-form; the measured state is a magnon-free zero mode, NOT an (AD3-ex) vector; **the exact display is not refuted, it is unavailable**, and no in-class vector is exhibited.  MP-2 additionally carries the verdict's §8(E) regime split (by escaped charge, not velocity class).  `AD3-ex` stays CONJECTURE. |
| m1 | MINOR | **FIXED.**  ⟨2⟩9(c) now carries §5's correct figures (`4.453e-02, 9.305e-03, 1.942e-03, 4.046e-04`; ratios `0.2089, 0.2087, 0.2083`) with a note that the r1-inherited digits (`3.96e-04` / `0.2085, 0.2041`) were stale. |
| m2 | MINOR | **FIXED.**  The ℤ₂ conjugation is stated explicitly at ⟨2⟩9(c) ("↓ at −∞, ↑ at +∞ — the ℤ₂-image of D13(a)'s orientation; (K-TAIL) instantiated with the conjugated assignment") and in §5's D16 battery description; the §8(A) row sentence carries it.  The checker's LD-C7(e) computes the profile in the flipped orientation, and `--red-c7-orientation` certifies the flip is load-bearing: under D13(a)'s literal assignment the gate fires at `C_K = 2525 > 0.3`. |
| m3 | MINOR | **FIXED (L4).**  MP-4's `𝒬_{c_0}φ` row now reads "the vector-valued lift of D13(c)'s conserved `X_1`: `𝒬_{c_0} = 2s(X_1−c_0)`"; the identification is also in §0's (K-Q) display and proved at LD-ID ⟨3⟩2. |
| m4 | MINOR | **FIXED.**  All three LD-C1 sub-gates the objection concerns are armed: commutation (`--red-halfspace`, already), orthogonality (`--red-c1-overlap`), resolution (`--red-c1-leak`).  The r2-response's premature "FIXED" is superseded by this row with measured exit paths. |
| m5 | MINOR | **FIXED.**  The unused `ε_W < δ` clause is deleted from ACE-LD-ε-x's ASSUME, with a note that the conclusion is valid (merely uninformative) when `ε_W ≥ δ`. |
| m6 | MINOR | **FIXED.**  ⟨1⟩4.⟨2⟩4's "exists trivially" is withdrawn: finite volume is stated as finite volume, and infinite-volume existence is cited as **M-INDEX-LA-folium, CONJECTURE**, named as the only route this shard offers to (K-Q)'s `t`-uniformity in infinite volume; same fix in HONEST STATUS's "(K-Q) for all `t`" bullet. |
| m7 | MINOR | **FIXED.**  "No model or state realising `(M-ESC)` is exhibited anywhere in this corpus" now appears in MP-1's obst row (with the lr-d16-r1 M2(b)1 cross-confirmation) and in HONEST STATUS. |
| m8 | MINOR | **PARTIAL (lane-limited), unchanged in kind.**  The shard is now ~1450 lines (the retraction, LD-ID/LD-MONO, and the honest checker spec grew it); the MP-5 split (obstruction into `theory/ace-ld-obst.md`) is endorsed by both critics and remains the requested merge action; shard creation is outside this lane. |
| n1 | NOTE | **ADOPTED.**  The subsumption ("boundedness under (LR3) is the quantitative form of D27's own existence corollary; the genuine addition is the `M_0` tightness argument") is disclosed at §0 obst′(c)'s replacement note and in MP-1's obst row. |
| n2 | NOTE | **FIXED in merge text.**  MP-4's merged symbol is `θ_{tr}` with the overload flagged (twist variable `θ`, notation.md line 271); MP-1/MP-6 merge text uses `θ_{tr}`; inside the shard `θ` remains local and HONEST STATUS flags the collision.  The r2-response's false "no hits" grep claim is superseded. |
| n3 | NOTE | **ADOPTED.**  §5 counts MODES (21), not firings, and says so. |
| n4 | NOTE | **ADOPTED.**  LD-C1's coset sub-gate now carries the arithmetic-certificate disclosure (docstring + §5), mirroring `memory_index_probe.py` P2's. |
| n5 | NOTE | **FIXED.**  New gate LD-C7(e) measures (K-TAIL) itself: `‖D_xφ‖ = 4.36e-02 … 8.27e-05`, per-site ratios `0.20871` both sides, `C_K = 0.209 ≤ 0.30` — the critic's §0(iii) figures, now certified; MP-1's eps row attributes hypothesis-certification to (e) and conclusion-rate to (b)--(c). |
| n6 | NOTE | **FIXED.**  ⟨1⟩5.⟨2⟩2 now says WHY the citation is sound inside a proof by contradiction against LR3: the cited sub-steps' leaf justifications carry only LR1--LR2 + (IDX.1), strictly weaker than MI ⟨1⟩7's theorem-level ASSUME. |

## Cross-lane items (verdict §7, adopted as instructed)

- **`(M-ESC) ⟹ (NR) fails`** is recorded at ⟨1⟩5.⟨2⟩6(iv) and MP-6 as
  the COMPOSITION of the ace-ld and lr-d16 critic passes — attributed,
  not asserted as this shard's theorem, per the work order.
- The `θ = 0` fence for D16 keeps its conclusion on M5's corrected
  support (K1+K2 stationarity + M-quant-G bound; K4 CONJECTURE named).

## Checker verification record (this round)

- `python3 -O theory/checks/ace_ld_check.py` → **exit 0**, LD-C1..LD-C7
  (incl. new LD-C5b) all pass (118 s).
- `python3 -O theory/checks/ace_ld_check.py --red` → **exit 1, RED-OK,
  21/21** modes reproduce their registered patterns (80 s), per-mode
  exit paths logged.
- Reachability (exit path per mode; NO blanket claim — this table plus
  the unreached list below IS the reachability statement):
  LD-C1 gap ← `gap`; LD-C1 coset ← `coset`; LD-C1 commutation ←
  `halfspace`; LD-C1 **orthogonality** ← `c1-overlap` (NEW); LD-C1
  **resolution** ← `c1-leak` (NEW); LD-C2 ← `merged`, `dup`,
  `c1-overlap`, `c1-leak`; LD-C3 ← `gap` (survives `coset`,
  `halfspace`, `merged`, `dup`, `c1-overlap`, `c1-leak` as registered);
  LD-C4 ← `merged`, `dup`, `c1-overlap`, `c1-leak`; LD-C5
  concentration ← `c5-inwindow`; LD-C5 atom ← `c5-nobarrier`; LD-C5
  **weights** ← `c5-weights` (NEW, data); LD-C5 identity line ←
  `c5-meanshift` (data; liveness only — line disclosed as subsumed by
  gate (a)); LD-C5 **tail growth** ← `c5-fixedwin` (NEW); LD-C5b wedge
  ← `c5b-flat`, `c5b-concentrated` (NEW); LD-C6 **liveness** ←
  `c6-static` (NEW — the r2 tautology model, now a detected mutant);
  LD-C6 support ← `c6-moving`; LD-C7 sector energies ←
  `c7-noboundary`; LD-C7 defect-positivity ← `c7-product`; LD-C7 rate
  ← `c7-delta`; LD-C7 coset ← `c7-mixed`; LD-C7 **(K-TAIL)** ←
  `c7-orientation` (NEW).
- **Unreached, disclosed:** LD-C5(e)'s FLOOR clause (deductively
  subsumed by (b)+(c) — no in-class mutation can reach it without
  firing (b)/(c) first; consistency line, not evidence); LD-C3's
  green-only liveness floor (by design evaluated on no mutant).
- One registration was corrected against measurement during the round:
  `c1-leak` was first registered to break LD-C3 and pass LD-C2; the
  measured truth (position-space ringing from the hard momentum cutoff)
  is the reverse, and the registered pattern now matches the
  measurement (first `--red` run exit 2 caught it; second run exit 1).
