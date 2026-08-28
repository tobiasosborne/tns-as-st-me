<!-- ROLE: orchestrator adjudication of the soft-index campaign r1 critic
     round (all three lanes). Inputs: ansatz-scattering-2m-r1.md +
     ansatz-scattering-2m-r1-response.md + ansatz-scattering-2m-r2.md
     (S2), soft-index-r1.md (S1-A), soft-index-b-r1.md (S1-B).
     Adjudicator: orchestrator (Fable main thread), 2026-08-28. -->

# Soft-index campaign — r1 adjudication (all lanes)

> **ORCHESTRATOR ERRATUM — appended 2026-08-28, bd `tns-uxr`.  The frozen
> adjudication below is NOT rewritten; this annotation corrects one binding
> instruction in it.**
>
> §3.7 (and the register note in §2.2) instructs the r2 unified shard to state
> the projected-current identity "over `m_λ`, with the corrected
> `2D A⁻¹J^z₀` form".  **Those two halves are mutually inconsistent** and, if
> followed literally, re-inject the very defect this round found — for the
> third time.  Reason (`verdicts/ml4-ward-n2-audit.md` §1.2, UXR-R1;
> independently reconfirmed by the orchestrator): the correction is
> REGISTER-DEPENDENT.
>
> * **Full-sector register** (`D_{n,N}=Q_0|_{ℋ_{n,N}}`, `A_n=D^†D` on the whole
>   sector, where `A_n` is non-scalar): the correct form is
>   `P_{n,N}J^-_0 = 2D_{n,N}A_n^{-1}J^z_0` (exact `≤2.4e-15` at every `n`).
> * **Highest-weight-restricted register** (`D_λ=Q_0|_{ker S^+}`): here
>   `A_λ=(N-2n)𝟙` is SCALAR — by the PROVED first display of (9) — so the
>   string `2D A^{-1}J^z_0` *evaluates to* `2Q_0J^z_0/(N-2n)`, i.e. exactly the
>   REFUTED display.  The correct form in this register is
>   `(1/m_λ)Q_0Π_{hw}J^z_0`, `m_λ=(N-2n)/2` (exact `≤7.6e-16` at every `n`).
>
> Cross-register substitution is wrong by `O(1)`: `1.7e-01` at `n=2`, `N=8`.
> **Binding correction for the r2 shard (`tns-v44`): pick ONE register and name
> it at the point of statement.**  Either full-sector with `2D_{n,N}A_n^{-1}J^z_0`,
> or hw-restricted with `(1/m_λ)Q_0Π_{hw}J^z_0`.  Never "over `m_λ`" together
> with `2DA^{-1}J^z_0`.



## 0. Verdict summary

| Lane | Shard | Verdict | FATAL | MAJOR | Trajectory |
|---|---|---|---|---|---|
| S2 r1→repair→r2 | ansatz-scattering-2m.md | FAIL(R2-O1,R2-O2) | 0 | 2 | 6→2 MAJOR, converging |
| S1-A r1 | soft-index.md | FAIL(F1,M1–M8) | 1 | 8 | first round |
| S1-B r1 | soft-index-b.md | FAIL(F1,F2,M1–M7) | 2 | 7 | first round |

**No lane converged; NO merge of D29/D30/D31 into definitions.md /
CLAIMS.md is performed** (lane discipline: merge only after critic
convergence). All MERGE PROPOSALS stay quarantined in the shards.

## 1. What the round established despite the FAILs

1. **The law itself keeps surviving.** The S1-A critic mounted two fresh
   falsification attempts INSIDE the hypothesis class (spin-1/2 + NNN
   coupling; spin-S + biquadratic deformation — both change the contact
   algebra, keep `2ρ` and `2iv_h`): measured slope `1/ρ` exactly, both
   cases. Together with the pre-registered probe (P1 green, out-of-sample
   S=1) the empirical position of S-INDEX is stronger after r1 than
   before it.
2. **(S-IDX.0) survives in corrected form.** The finite-volume Ward
   package — `‖Q₀ψ‖²=2m`, the velocity datum `⟨h|J^z₀|h⟩=iv(h)`, residue
   `2iv_h` (ρ-independent, verified S=1/2,1,3/2), the corrected
   projection `P J⁻₀ = 2D A⁻¹J^z₀` — is verified by both critics across
   deformations. The unconditional rung is real; both shards' write-ups
   of it need the n≥2 repair below.
3. **The S2 core is one objection from convergence.** (A2M.1)–(A2M.2)
   (Cook existence + isometry + ML2 exact match + derived clustering
   D31-C2) stand with 0 FATAL through two hostile rounds; only the
   nonvacuity bridge (A2M.3) is still open (R2-O1/R2-O2).
4. **The two-prover design paid for itself again** (memory-campaign
   precedent repeated): the lanes disagreed exactly where the target is
   soft, and the disagreements are adjudicable (see §3).

## 2. Corpus damage register (findings that reach OUTSIDE the campaign)

| Finding | Where found | Status | Tracker |
|---|---|---|---|
| ML4-Ward (9) 2nd display false for `n≥2` (PROVED row) | S1-B F1 | CONFIRMED ×3 (critic ED, analytic mechanism, `ml4_ward_n2_check.py`); CLAIMS row scoped + shard ERRATUM added this session; ⟨1⟩5 two-hard step damaged, downstream audit open | tns-uxr (P0) |
| Frozen probe P2(b) η-gate is a code no-op (`proto` ≡ `proto_dressed`) | BOTH S1 critics, independently | The a0728bd "protocol dodge certified both ways" headline must be quoted as **P2(a)-only** until an unfreeze + honest re-run | tns-9z4 (P1) |
| D24(d)3 + ML5-B force slope 2 at every ρ ⇒ frozen `𝒮_W` empty for ρ≠1/2 | S1-A cross-lane 4 | Vacuity, not falsity; blocks any D29/D30 merge; the ρ-dependence of the flux normalization must be adjudicated ONCE in definitions.md | tns-iu5 (P1) |
| P3's "smeared datum" is the ML4 orthogonal trace, not the protocol datum; P3 varies h with N | both S1 critics (notes) | Record-only for now; fold into the tns-9z4 unfreeze if opened | tns-9z4 note |

## 3. Cross-lane adjudication (binding for the r2 unified shard)

The two S1 critics' cross-lane sections agree on the facts and assign
blame consistently. Adjudicated design decisions:

1. **D29 (protocol datum): S1-B's design wins.** Concrete finite
   linear-algebra object, computable at every finite index, already
   implemented (modulo the M4/probe-matching corrections) by the frozen
   probe readout. S1-A's abstract pairing was never instantiated
   anywhere — it loses on the vacuous-truth criterion, the campaign's
   own first landmine. CARRY from S1-A into the unified D29: the
   carrier+width structure (`ς` separate from `k`) IF AND ONLY IF the
   r2 prover can state it without un-smearing the soft leg (S1-A's
   `ς→0` before `k→0` order contradicted the load-bearing-smearing
   principle and P3; the r2 default is B's scale-only datum with the
   profile-averaged slope stated honestly as such).
2. **D30/(TGT): value-fixing by hypothesis is DEAD.** S1-A's D30(2)
   (fixes the jet value) is the inversion of the campaign spine and is
   struck. S1-B's negative claim is upgraded: the S1-A critic PROVED
   constructively (Möbius shift `𝒜 ↦ (1+𝒜)(1+icε)−1` preserves every
   regularity clause, moves the jet arbitrarily) that **no
   regularity-only (TGT) can pin the jet value**. Binding consequence:
   the r2 statement takes the value from on-shell input — the PROVED
   spin-S contact algebra (S2-2body-S) route — and (TGT) supplies
   compactness/equicontinuity ONLY. The slope-law theorem is therefore
   conditional on an on-shell matching hypothesis, named and displayed,
   or it is a theorem about the descendant-projected datum only.
3. **The `1/(2ρ)` factor: NEITHER lane's treatment survives.** S1-A's
   silent redefinition of frozen D24(d)3 is forbidden (F1); S1-B's
   undefended multiplication is M-level. Resolution belongs to the
   corpus (tns-iu5), not to either shard; the r2 prover states the
   factor as an explicit displayed hypothesis pending tns-iu5.
4. **Charge scoping: S1-A's register wins.** `ℓ_h` carried abstractly,
   `ℓ_h=|q|` only where proved (|q|=1); no `|q|/ρ` in any box until
   tns-ebh. S1-B's boxes are re-scoped accordingly.
5. **Sector register: S1-A's `m_λ` (actual magnetization, `m_λ/N→ρ`)
   wins** for the free-ρ discipline; S1-B's `M=ρN−n` presupposes
   `ρ=S∈½ℤ` through the fully-polarized vacuum — exactly what the
   target forbade.
6. **LSZ-exhaustiveness: S1-B's register wins** (carried as hypothesis,
   not definitional); mirrors the S2 R2-O1 adjudication below.
7. **(S-IDX.0): one identity, one write-up.** Both shards prove the same
   thing; the r2 unified shard states it once, over `m_λ`, with the
   corrected `2D A⁻¹J^z₀` form and the n=1 specialization displayed.

## 4. Work orders opened

- **S2 round-2 repair (tns-s5e, budget-gated):** R2-O1 — port
  refs/arxiv-1412.2970 Thm `Haag-Ruelle` final clause (creator-choice
  independence) to prove (ACE2M-LSZ) as an operator statement (upgrades
  the hypothesis to a theorem; the critic verified the two hypotheses
  are already owned). R2-O2 — scope (A2M.3) to the diagonal-order
  statement actually proved, restore interface clause 3's packet
  qualifier, bound the `L²(I)` denominator. Plus 9 MINOR (incl. restore
  "connected" in A2M-C1a; tolerance on the ratio gate).
- **S1 round-2: ONE unified shard** (successor to both lanes) under the
  §3 adjudicated design; the two r1 shards become lane records. Repair
  ingredients are all named: corrected Ward form (F1), honest Adler
  anchor replacing (B6) (F2 — the `Q₀`-created-state computation, which
  IS exactly 1, stated for the object it is true of), S1-A's F1
  resolved per §3.2 (value from S2-2body-S matching, not stipulation).
  Not yet filed as an issue: sequencing (and prover budget) is TJO's
  call alongside tns-s5e.
- **Corpus:** tns-uxr (P0, ML4-Ward n≥2 downstream audit), tns-9z4
  (probe P2(b)), tns-iu5 (D24(d)3/ρ).

## 5. DAG consequences applied this session

- ML4-Ward row: scoped (ERRATUM), stays PROVED for its surviving
  clauses; `ml4_ward_n2_check.py` added as the red-capable certificate.
- No soft-index rows enter CLAIMS.md; S1-A/S1-B/AC-EX-2M shard rows stay
  quarantined in their MERGE PROPOSALS at self-status SKETCH.
- The a0728bd probe headline is re-quoted (HANDOFF) as: P1 green,
  P2(a) green, P2(b) VOID (tns-9z4), P3 green-with-caveat, P4
  exploratory.
