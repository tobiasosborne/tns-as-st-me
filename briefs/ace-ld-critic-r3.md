# Critic brief — ACE-LD round 3 (adjudication; two promotion candidates)

Read `briefs/critic-protocol.md` first, including Standing checker obligations.

**TARGET:** `theory/ace-ld.md` (1447 loc), `theory/ace-ld-r3-response.md`,
`theory/checks/ace_ld_check.py`.
**VERDICT FILE (your only writable file):** `theory/verdicts/ace-ld-r3.md`.

**Priors:** `ace-ld-r1.md` (1 FATAL, 6 MAJOR) and `ace-ld-r2.md`
(1 FATAL, 6 MAJOR, 8 MINOR, 6 NOTE).  **Do not churn r2 §5's 14-item fence.**
Verify the 21 claimed dispositions by fresh recomputation.

## 1. The FATAL was turned into content — check that the conversion is honest

r2's FATAL was that `𝒬_{c₀}` is identically D13(c)'s conserved charge, making
(K-TAIL) and D18(AD3) mutually exclusive.  The lane **retracted the bridge at
all seven sites and withdrew MP-3(ii)**, so the false claim cannot reach
`ansatz-scattering.md`.  It then promoted your refutation into:
- **THEOREM LD-ID** — `Q̂_{W,c₀} = Σ_{x∈W}(S^z_x − s_{γ_{c₀}}(x))` exactly;
  `𝒬_{c₀} = 2s(X₁−c₀)`; (K-TAIL) ⟺ "no charge escaped the core"; joint
  unsatisfiability with D18(AD3); `δx = 0` on the `ε_Q = 0` class.
- **LEMMA LD-MONO** — anchor-free window monotonicity: an assumed ε-form
  (AD3-ex) at one core-containing window propagates to every larger window up
  to a uniform `2C_Kλ̃^{d_W}/(1−λ̃)`, compatible with a leg already beyond the
  outer window.

**Attack both.**  Is LD-ID stated at the strength you proved, or beyond it?
Is LD-MONO's "compatible with a leg already beyond the outer window" clause
genuinely true — or does it smuggle back the regime LD-ID says is excluded?  Verify the
retraction is complete: grep every one of the seven sites plus MP-3.

## 2. THEOREM ACE-LD-χ — the promotion candidate you asked for

Claimed: *for a unit `φ` with `ω_φ ∈ 𝒦_{αβ}` (D9(a)) satisfying (K-TAIL), both
tail vacua are the χ=1 fully polarised `S^z`-product states and `±s ∈ spec
S^z`* — with the concrete corollary that **a spin-1 chain at `s = 1/2` admits
no (K-TAIL) kink state, by arithmetic**.  Placed in §0, HONEST STATUS and
MP-1's row.  You said in r2 this forcing was a theorem rather than the hedged
remark it was written as; check the proof now delivers exactly that, no more.

## 3. The strengthened statement (M2)

Restated, and deliberately **not** called a contrapositive: *"on any (LR) state
the mean wall transport is uniformly bounded, `sup_m |ω⁺−ω⁻|(𝔛_{W_m}) ≤
(M₀+1)/(2s)`; in particular `θ = 0`"* — O(1), with your n1 subsumption
disclosed beside it (quantitative form of D27's own existence corollary; the
claimed genuine addition is the `M₀` tightness route).  Rule on whether the
addition is genuine.

## 4. The checker — and one thing the lane did that you should verify hard

Claimed: green exit 0, `--red` RED-OK **21/21**, with a **measured**
reachability table rather than a blanket claim, plus an explicit **unreached**
list with reasons (LD-C5(e)'s floor, provably unreachable in-class; LD-C3's
green-only liveness floor).

**The item to verify hardest:** the lane says it *deliberately did not ship* an
identity-with-`𝒟` gate because it reduces to `x ≡ x` — *"would have been no-op
#7"* — and shipped a wedge gate instead, on the measured ground that the
dephasing defect saturates at `6.083` with no Cesàro decay, i.e. **D27(LR2)
genuinely fails on a straddling state**.  If that measurement is right it is a
real finding about (LR2), not just checker hygiene, and it should be fenced.
If it is wrong, a gate was withheld on a bad reason.  Also check `c6-static` —
the lane turned r2's tautology model into a detected mutant — and the corrected
`c1-leak` registration (its first red run exited 2 and caught it).

## Deliverable

Verdict line and trajectory `r1 → r2 → r3`.  Explicit rulings: may **ACE-LD-ε**
enter `claims/CLAIMS.md`, and at what status, with a verbatim cell?  May
**ACE-LD-obst′** enter as a negative row, with a verbatim cell?  May **LD-ID**
and **ACE-LD-χ** enter as their own rows?  For anything you promote, supply the
exact statement cell — promotion happens on your sentence.  And rule on MP-1
through MP-6, noting MP-3(ii) is withdrawn and MP-6 records the cross-lane
composition `(M-ESC) ⟹ (NR) fails` as an attributed composition rather than
this shard's theorem.
