# Work order — ACE-LD repair round 3

**FAIL(F1,M1–M6)**: 1 FATAL, 6 MAJOR, 8 MINOR, 6 NOTE.

**Read this before you plan: the FATAL kills the BRIDGE, not the THEOREM.**
The critic states plainly that **ACE-LD-ε may enter `claims/CLAIMS.md` at
PROVED (conditional)** once F1 and M1 are repaired, that the theorem is
correct, and that its class is genuinely inhabited — it rebuilt the D16 ED
from scratch and verified (K-TAIL) directly (`‖D_xφ‖` falls by exactly
`0.2087` per site, both sides, four steps).  **The verbatim scoping sentence
you must adopt is in §8(A) of the verdict.**  Likewise **ACE-LD-obst′ may
enter as a negative row**.  Your job is to remove one false bridge and place
two admissions correctly — not to rebuild.

## WRITING DISCIPLINE
ONE section per response, written to disk before you think about the next.

## READ FIRST
`CLAUDE.md`; `briefs/critic-protocol.md`;
`theory/verdicts/ace-ld-r2.md` **IN FULL** (your work order — read its
verified/fenced items first); `definitions.md` **D13(a) and D13(c)**, D18(AD3);
`theory/memory-index.md` ⟨1⟩1.⟨2⟩2 and ⟨1⟩3;
`theory/ansatz-scattering.md` ⟨1⟩7.⟨2⟩2; your own `theory/ace-ld.md`.

## F1 — the bridge is false, and it must be retracted, not repaired

`𝒬_{c₀} := lim_n Q̂_{W_n,c₀}` is **identically the exactly conserved charge of
the frozen D13(c) trap**.  From D13(a) + MI ⟨1⟩1.⟨2⟩2 the critic derived
`Q̂_{W,c₀} = Σ_{x∈W}(S^z_x − s_{γ_{c₀}}(x))` exactly — verified symbolically
and on a 201-site lattice, **and reached independently by the LR-D16 critic in
a different lane** — hence `𝒬_{c₀} = 2s(X_1 − c₀)`.

Therefore **(K-TAIL) is the hypothesis "no charge escaped the core" and
D18(AD3) is the hypothesis "the leg charge left the window": they are mutually
exclusive.**  Three independent confirmations:
1. on an escaping magnon the escaped tail sum saturates at exactly `2s = 1` at
   every padding, while the minimal admissible `C_K` grows as `λ̃^{−vt}`
   (`10^{+79.8}` at `t = 64`);
2. an explicit ledger shows conservation forces the wall shift `−2`,
   reproducing the frozen `ΔQ_W = −2`, `ν = +2`, while `𝒬_{c₀} = −1` in
   **both** channels — so `q_L ≠ q_T` is unavailable and `ε_Q ≥ 1` per channel;
3. even granting the hypotheses, (LD.4) plus conservation force **`δx = 0`** —
   no memory at all.

FIX DEMAND: **retract the claim that ACE-LD-ε-x supplies what
`ansatz-scattering.md` ⟨1⟩7.⟨2⟩2 consumes, and withdraw MP-3(ii)**, which
would have written that false claim into another shard.  Do not attempt to
rescue the bridge.  State the true relationship: the ε-version is a theorem
about states whose charge has NOT escaped, and the ordered-limit consumer needs
the opposite regime.  That is a real and publishable distinction; say it.

## M1 — the χ=1 admission is true, understated, and in the wrong place

The class is still effectively `χ=1`, and **worse than you admitted**: D9(a)
*supplies* the tail relaxation, so the χ=1 forcing is a **theorem, not a
hedged remark**, and it additionally forces `s ∈ spec S^z`.  Your admission
exists but sits in the weakest available location and is **absent from §0,
from HONEST STATUS, and from MP-1's not-claimed clause**.  Prove it as a
theorem, and put it in all three places.

## M2 — your contrapositive is weaker than your own proof

You state (M-ESC)'s contrapositive as "LR3 forces mean wall transport
`o(|W_m|)`", with a liminf/lim quantifier slip.  Your own ⟨2⟩3 gives
`sup_m |ω⁺−ω⁻|(𝔛_{W_m}) ≤ (M₀+1)/(2s)` — that is **O(1), not o(|W_m|)**.
Fix the quantifier and state the stronger true thing.  Note also (n1): it is
the quantitative contrapositive of D27's own existence corollary.

## What SURVIVED (fence it, do not churn)

- **LD-TAIL survives the M-INDEX-LA-strong test**: no sector-wide operator is
  built, and the refuting state (MI ⟨1⟩3, `ω(D_{−n}²) = 1/(n+1)`) is
  polynomially decaying and excluded from (K-TAIL) by exactly the margin it
  demands.  (But ⟨2⟩4's "exists trivially" sector-wide operator **is**
  M-INDEX-LA-folium, CONJECTURE, uncited — fix that citation, m6.)
- ACE-LD-obst′'s minimal-hypothesis claim is TRUE; all three claims re-derived.
- `--red-coset` and `--red-gap` **are** genuinely distinct in mechanism, and
  §5's 6×-tolerance honesty clause is accurate.  r1's M6 is properly fixed.

## M3/M6 — the checker, sixth no-op of the campaign

- **LD-C6 is a tautology**: `p_W = δ₀`, tail 0, for *every* state and every
  position-diagonal `H` — uniform, random and far-outside-window states all
  give 1.0.
- **LD-C5(d) is implied by LD-C5(a)** (agreement is `4e−11`, not `1e−4`, and
  tracks the concentration defect).
- **LD-C5(e) reduces to `1 > 0.9`.**
- Gates C5(c), C5(e) and LD-C1's orthogonality and resolution sub-gates are
  reached by **no** registered mode — which falsifies §5's blanket reachability
  claim.  Do not make a blanket reachability claim again; publish the table.

## CROSS-LANE — a result neither lane has alone

The critic notes that composing this lane with the (LR)-for-D16 lane yields
**(M-ESC) ⟹ (NR) fails**.  Record it as such, attributed to the composition,
and do NOT assert it as this shard's own theorem without proving it here.
Also: your reason for `θ = 0` in D16 ("flat band ⟹ θ = 0") is the very
K4-strength upgrade the parallel critic just ruled MAJOR in that other lane,
and it concerns **bare kinks** while `θ` concerns **kink+magnon** states.  Fix
the reason; the conclusion `θ = 0` may stand if you can support it honestly.

## LANE (writable, nothing else)
`theory/ace-ld.md`, `theory/ace-ld-r3-response.md` (create),
`theory/checks/ace_ld_check.py`.  MERGE PROPOSALS only.  No commits.

Work fully autonomously.  Do not ask questions.  ONE section per response.
