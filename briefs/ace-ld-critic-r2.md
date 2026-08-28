# Critic brief — ACE-LD round 2 (adjudication)

Read `briefs/critic-protocol.md` first, **including Standing checker
obligations** (five bullets).

**TARGET:** `theory/ace-ld.md` (1033 loc), `theory/ace-ld-r2-response.md`,
`theory/checks/ace_ld_check.py` (718 loc).
**VERDICT FILE (your only writable file):** `theory/verdicts/ace-ld-r2.md`.

**Prior:** `theory/verdicts/ace-ld-r1.md` — FAIL(F1,M1–M6), 1 FATAL, 6 MAJOR,
7 MINOR, 4 NOTE.  Verify the 18 claimed dispositions by fresh recomputation;
attack what changed; do not churn r1's fenced VERIFIED-CORRECT items.

The lane took the reroute you handed it.  Two artifacts now carry the shard,
and both are new since your last pass.

## 1. ACE-LD-ε — the positive result (attack the class first)

Claimed (⟨1⟩4, (LD.4)): under **(K-TAIL)** (confined-core exponential tail
clustering) and **(K-Q)** (sharp relative charge, `‖𝒬_{c₀}φ − q_φφ‖ ≤ ε_Q`),
`‖(Q̂_{W,c₀} − q_φ)φ‖ ≤ ε_Q + (2C_K/(1−λ̃))·λ̃^{d_W}`.  Corollaries
ACE-LD-ε-t (the work order's display, `ε_Q=0`, compatible with D27(LR3)) and
ACE-LD-ε-x (ordered-limit cross-term vanishing at `O(λ̃^{d_W})`, claimed to be
**exactly what `theory/ansatz-scattering.md` ⟨1⟩7.⟨2⟩2 consumes**).

- **Is the class INHABITED, and by what?**  r1's FATAL was an empty class.
  The lane now claims D16 static-kink sector states inhabit it, with (K-Q)
  exact and the (K-TAIL) rate `q = 0.208712` certified.  Verify both, and
  determine whether the class is *still* effectively `χ=1` — the lane states
  the χ=1 scope boundary openly at ⟨2⟩9, so the question is not whether it
  admits it but whether the admission is complete and correctly placed.
- **LD-TAIL (⟨1⟩4.⟨2⟩2) is the step to break.**  It claims the limit vector
  `𝒬_{c₀}φ := lim_n Q̂_{W_n,c₀}φ` **exists on every (K-TAIL) state**, and that
  this respects the REFUTED row M-INDEX-LA-strong because no sector-wide
  operator is built.  Check that distinction rigorously.  If the construction
  smuggles in a sector-wide charge on the folium, it collides with a REFUTED
  row and the shard fails.
- **The ⟨1⟩7.⟨2⟩2 claim is about ANOTHER shard.**  Read
  `ansatz-scattering.md` ⟨1⟩7.⟨2⟩2 yourself and decide whether the ε-version
  really supplies what it consumes, at the rate claimed, in the ordered limit.
- **Reading discipline (your M5).**  The lane says this is the *kink*-
  eigenstate reading, ε-weakened, and that M-INDEX-spec's weak-* reduction
  clause is explicitly NOT supplied (⟨2⟩8).  Confirm no step drifts back.

## 2. ACE-LD-obst′ — the negative result at minimal strength

Claimed (⟨1⟩5): under H-MQG(1)–(3), D26(INT), D27(LR1)–(LR2) and **(M-ESC)
alone** — `θ := liminf_m |ω⁺−ω⁻|(𝔛_{W_m})/|W_m| > 0` — the TPM first moments
diverge, **D27(LR3) fails along every padded exhaustion**, and `δx` is
undefined.  Proof = D27's own first-moment identity + the `M₀` bound.  No
(E-TAIL), (V-ch), (V-in), `σ_L≠σ_T`, channels or D28.

- Verify the minimal-hypothesis claim by rederiving it.  A negative result
  this cheap is either a real structural fact or an error.
- **The contrapositive is the valuable part**: "LR3 forces mean wall transport
  `o(|W_m|)`".  Is that right, and is it as general as stated?
- **Scoping**: the lane claims D16 sits at `θ = 0`, so bd `tns-xf4` is not
  pre-empted.  Verify — and note a **separate lane has just proved LR3 for
  D16 from a named input (NR)** (`theory/lr-d16.md` ⟨1⟩5, under critique in
  parallel).  Say explicitly whether ACE-LD-obst′ and that LR3 result are
  consistent.  Two lanes now make claims about D16's `|ν|` growth; if they
  conflict, say which you believe.

## 3. What was deleted, and whether the deletion is complete

(E-TAIL), (V-ch), (V-in), ACE-LD-esc, COROLLARY ACE-LD, r1's ACE-LD-obst, and
the false "on D28 packets the kink is ballistic" sentence are all deleted; the
(E-TAIL)⟺χ=1 equivalence is recorded once with proof; r1's MP-2 compound
status is withdrawn and **AD3-ex stays CONJECTURE**.  Grep for orphans — a
deleted hypothesis still cited by a surviving step is a MAJOR.

## 4. Checker

Claimed: green exit 0; **13 red modes**, each with its exit path named, every
gate and evidence-carrying sub-gate reached by a named mode; LD-C5 now
produces the `ν=0` atom (`p₀ = 0.2704 = |r|²`); LD-C3's constant is
**asserted-not-computed** with the ratio statistic reported and the sharpness
claim deleted; `--red-coset` now a true coset break distinct from `--red-gap`.
The orchestrator independently re-ran green plus 14 modes: all fire, zero bare
asserts.  That is necessary and not sufficient — apply every standing
obligation, especially subsumption and whether `--red-coset` and `--red-gap`
are genuinely distinct in mechanism rather than merely in registered pattern.

## Deliverable

Verdict line; whether ACE-LD-ε may enter `claims/CLAIMS.md` and at what status
with an exact verbatim scoping sentence if so; whether ACE-LD-obst′ may enter
as a negative row; an explicit ruling on MP-1–MP-6; and whether AD3-ex's
CONJECTURE row should now carry the regime split.
