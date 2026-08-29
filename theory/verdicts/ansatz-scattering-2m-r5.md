<!-- ROLE: r5 ADJUDICATION verdict on theory/ansatz-scattering-2m.md
     (Theorem AC-EX-2M, Lane S2) — the PROMOTION round.  Priors:
     ansatz-scattering-2m-r1.md … -r4.md.  Work order: briefs/s2-critic-r5.md
     + briefs/critic-protocol.md (incl. the 2026-08-29 standing checker
     obligations).  Writable lane: this file only.  No shard, definitions.md,
     claims/CLAIMS.md or notation.md edit; no commit. -->

# Critic verdict r5 — `theory/ansatz-scattering-2m.md` (Theorem AC-EX-2M, Lane S2)

Critic: Opus, adversarial, 2026-08-29.  **Adjudication / promotion round.**
Priors: `theory/verdicts/ansatz-scattering-2m-r1.md`, `-r2.md`, `-r3.md`,
`-r4.md` (all mine).  Claimed dispositions:
`theory/ansatz-scattering-2m-r4-response.md`.

Repair round audited: `git diff 65a6d32 365d143 --` on the two lane files —
13 hunks in `theory/ansatz-scattering-2m.md`, 200 changed lines in
`theory/checks/ansatz_scattering_2m_check.py`.  **The diff has zero hunks
between old shard lines 76 and 377**, i.e. `⟨1⟩2`–`⟨1⟩7` — the entire body of
the material proposed for promotion — is **byte-identical** to the text r4
audited.  r4 §7's fenced list is not churned.

All prototype computation in
`/tmp/claude-1000/…/scratchpad/{indep_r5.py,smat_r5.py,mut/*}`; nothing
outside this verdict file was written.

**Headline.**  R4-O1 is **fixed at the leaf**, verified by reading the
Justification line itself, and no surviving step reads the D29 identification
as available.  The independence claim underlying the row split is **TRUE**: I
walked every Justification leaf of `⟨1⟩2`–`⟨1⟩7` and **not one** cites
`(ACE2M-LSZ)`, `(ACE2M-SR)`, `(D29-den)`, `⟨1⟩8`, `⟨1⟩9`, or the D29
identification — the sole mention is `⟨1⟩7.⟨2⟩4`'s explicit *disclaimer of
use*.  **I MERGE the split**, with both rows supplied in §9 and **not** in the
prover's drafting: the prover's draft PROVED row points its `where-proved` at
`⟨1⟩2--⟨1⟩7` while one of its own clauses — *"D6 directly satisfies
D31(1)--(5)"*, which is the row's **nonvacuity certificate** — is proved only
at `⟨1⟩9.⟨2⟩4`, a step that under L6b inheritance sits beneath `⟨1⟩9`'s
ASSUME "*adjudicated D29 interface clauses 1--4*" and proves a proposition
that is not part of its parent's PROVE.  That is R5-O1, and it is a MAJOR.
It does **not** defeat the split — `⟨1⟩9.⟨2⟩4`'s justification cites no D29
clause and I re-derived its content — but the step must be hoisted, and the
draft cells must not be applied verbatim.

---

## 0. Disposition verification table (round obligation 1)

Nineteen claimed dispositions, every one verified by fresh recomputation, by
running mutants on copies, or by reading the artifact — never by reading the
response.

| id | claimed | **r5 verdict** | evidence |
|---|---|---|---|
| R4-O1 | FIXED (A) | **VERIFIED-FIXED, AND THE FIX REACHES THE LEAF** | The Justification line of `⟨1⟩9.⟨2⟩5` now reads, in full: "*Claims S2-2body and ML2, D24(b), and the exact-match computation ⟨1⟩7.⟨2⟩3.  S2-2body is proved from the two-body contact equations; no integrability hypothesis enters.*"  `⟨1⟩8.⟨2⟩1--⟨2⟩2` is **struck** — I read the leaf, not the prose.  PROVE line relabelled "*the `j`-independent infinite-chain **constructed-channel** datum*"; the new paragraph displays the `−2ik_s\|P_{12}⟩` branch term and states "*no D29 instance of `(ACE2M-SR)` is exhibited*".  `⟨1⟩7.⟨2⟩3` is a **legitimate** leaf for the object as relabelled: it is exactly where `W_+^*W_-=S_phys` is proved.  Heading renamed per the FIX DEMAND |
| — | (leaf-reach check) | **NO SURVIVING STEP READS THE IDENTIFICATION AS AVAILABLE** | I enumerated every step that touches `𝒜`, `A_j`, `A(ε)` or `S_phys`: `⟨1⟩8`'s `(SR)` display (hypothesis definition only), `⟨1⟩9.⟨2⟩1` (clause-3 bound, no identification), `⟨2⟩2` ("*the adjudicated D29 fixed-time family is not this family, so no channel identification for Lane S1 follows*"), `⟨2⟩3` (conditional on `(SR)`, `A_j` is the D29 datum, no `S_phys`), `⟨2⟩5` (now constructed-channel), `⟨2⟩6` ("*⟨2⟩5 backs no D29 claim*"), `⟨1⟩1(3)`, §8, §7.  Zero remaining reads |
| R4-O2 | RETRACTED | **VERIFIED, and the quantification is CORRECT** | §6 and the module docstring both retract.  I re-derived r4's V8 bound symbolically — both routes share denominator `‖C_{w_C}‖‖D_{w_D}‖λ̃^{d_sep}=2^{w_C+w_D−d_sep}`, minimum `2^{2−6}=1/16` (I confirmed `‖C_w‖=2^w` by SVD in a second basis) — and then **empirically**: mutant `c3` (subtraction coefficient `1→1.000001`) gives `agreement=1.000e−06` and `ratio_route=1.600e−05`, i.e. **exactly `16×`**.  The `(6.25·10^-14,10^-12]` fire-alone window follows.  Both numbers in the shard are right |
| R4-O3 | FIXED | **VERIFIED by exit path** | `--red-truth` → `RED-OK [G1,G2]`, both `1.000000e-06`; `--red-c1b-sub` → `RED-OK [G4,G5,G6]`.  G1 and G4 now have registered mutants; every one of the nine gates has one (§4.2) |
| R4-O4 | FIXED | **VERIFIED, and the r4 regression is CLOSED** | I re-ran the absurd-input battery on copies, editing only `LAMBDA_TILDE`: `−5.0` → exit 2, `1e6` → exit 2, `3.7` (registered) → exit 1, `1/3` exactly → exit 2.  All three r4 green-passers now die.  In-domain: `λ̃=0.34` → exit 2 (`cap 0.106797`), `λ̃=0.9999` → exit 0.  §6's "*the cap `0.1` is a `λ̃=1/2` statement … already fails at `λ̃=0.34`*" is exactly right |
| R4-O5 | FIXED | **VERIFIED** | `### ⟨1⟩9. Diagonal limit points and the separately scoped HR theorem`; `### ⟨1⟩8. The D29 interface block and the separate HR hypotheses`; `⟨1⟩9`'s ASSUME is now clause-specific ("*adjudicated D29 interface clauses 1--4; for ⟨2⟩2 only, … clause 5*").  The three headings and the ASSUME are the FIX DEMAND verbatim in substance |
| R4-O6 | FIXED | **VERIFIED** | `⟨1⟩1`'s ASSUME and clause 5(b) now both read "*(2M-1P) is proved for the HR family built from the adjudicated charge acting on the vacuum; what the adjudicated D29 lacks is HR admissibility*".  The over-strong "*not properties of the adjudicated D29*" is gone from both sites |
| R4-N1 | RESIDUE | **VERIFIED to the byte** | `cmp` of the shard's first `AC-EX-2M` row against `claims/CLAIMS.md`: **identical, 3943 bytes**.  And r4 §9's 703-character replacement sentence is present in `claims/CLAIMS.md` **verbatim** (exact substring match, checked programmatically).  The `ratio_route` rename demanded by R4-O2(iv) was also applied |
| R4-N2 | RESIDUE | **VERIFIED by independent recomputation** | My own AKLT in the standard spin-1 `S^z` basis (`A^{+}=√(2/3)σ^+`, `A^0=−σ^z/√3`, `A^-=−√(2/3)σ^-`, both fixed points verified before use): `monotonicity_excess = −6.5030737e−03 @ (1,2,6)`, matching to ten digits |
| R4-N3 | RESIDUE | **VERIFIED** | The two-sided-fold retraction stands in §6, the docstring and the merged row |
| R4-N4 | RESIDUE | **VERIFIED — not self-fulfilling** | `--red-truth` shifts the *independent closed-form target*, not a route, and kills the run.  I separately reproduced the target `4/3·(−1/3)^d` for `d=1..12` from a different tensor basis to `≤1.0e−15` |
| R4-N5 | RESIDUE | **VERIFIED** | `violations()` evaluates all nine gates and returns the full list; `--red-c1b-sub` prints three gates in one line.  No gate can be masked |
| R4-N6 | RESIDUE | **VERIFIED, all seven** | Violation sets: `{G2,G3}`, `{G5,G7}`, `{G6}`, `{G1,G2}`, `{G4,G5,G6}`, `{G8}`, `{G0}` — **pairwise distinct; no two red modes are bit-identical in effect** |
| R4-N7 | FIXED | **PARTIALLY-EXECUTED** | The guard exists and does kill three *different* route-collapse implementations (the registered flag; `direct := fixed`; `fixed := direct`) — I built the last two as `c1`, `c2`, both exit 2 on G8 alone.  **But its green value is `0` by algebra and it is blind to every data mutation** → **R5-O3 (MINOR)** |
| R4-N8 | RESIDUE | **VERIFIED** | No diff hunk touches `⟨1⟩8.⟨2⟩1`'s citation block or `⟨1⟩10`.  Every 1412.2970 anchor in the diff resolves to a real `\label` |
| R4-N9 | RESIDUE | **VERIFIED** | The charge-sector reading survives and its consequence is now stated precisely at clause 5(b) |
| R4-N10 | RESIDUE | **VERIFIED** | `⟨1⟩3` is **byte-identical**: zero hunks between old lines 76 and 377 |
| R4-N11 | RESIDUE | **VERIFIED** | `grep -rl` for `AC-EX-2M\|ACE2M-LSZ\|ACE2M-SR` outside the shard/verdicts/briefs returns exactly `HANDOFF.md`, `claims/CLAIMS.md`, and the lane's own checker.  **No `theory/` shard consumes this row**, so the split has zero downstream blast radius |
| R4-N12 | RESIDUE | **VERIFIED** | Shard hunks are confined to `⟨1⟩1`, `⟨1⟩8`–`⟨1⟩9`, §6, §7, §8.  `theory/checks/` also changed `ace_ld_check.py`, `d24d3_normalization_check.py` and `lr_d16_check.py` in the same orchestrator commit — those are the ACE-LD, D24(d)3 and LR-D16 lanes, **not** this one; no frozen checker was touched by S2 |
| R4-N13 | FIXED | **VERIFIED at five levels** | "one-element"/"singleton"/"constructed-channel" now appears at `⟨1⟩1(A2M.3)`, `⟨1⟩9.⟨2⟩5`, §7's mirror row, §8 **Conditional**, and in the `AC-EX-2M-D29` proposal |

**Nothing regressed in the shard.**  Eighteen of nineteen dispositions verify;
one (R4-N7) is partially executed.  The single MAJOR of this round is *not* in
the repaired text at all — it is in the **row split the prover drafted beyond
the diff**.

---

## 1. What I independently recomputed (obligation: recompute, never referee)

| # | object | independent method | outcome |
|---|---|---|---|
| **W1** | **the independence walk** — the whole basis of the split | extracted **every** `*Justification.*` leaf in `⟨1⟩2`–`⟨1⟩7` (21 leaves) and classified each citation | Leaves cite only: D1(c,d), D3(a), D6–D8, D7, D12(a′), D31(1)–(5), (D31-C2), ML2 (15),(17)–(21), `theory/ml2-completeness.md ⟨1⟩5`, `refs/arxiv-1412.2970` labels, named computations (**MPS-2M-cluster**, **ACE-filter**, **2M-Cook**, **ACE-SP**, **2M-Gram**), earlier steps *inside* `⟨1⟩2`–`⟨1⟩7`, and `briefs/soft-index-target.md`.  **Zero citations of `(ACE2M-LSZ)`, `(ACE2M-SR)`, `(D29-den)`, `⟨1⟩8`, `⟨1⟩9`, or the D29 identification.**  The only textual mention of the port in the range is `⟨1⟩7.⟨2⟩4`'s "*is **not needed** to compare or exhaust different packet-window ranges here*" — a disclaimer of use, not a use.  **INDEPENDENCE CONFIRMED** |
| **W2** | `⟨1⟩3.⟨2⟩1–⟨2⟩2` (D31-C2), from scratch | re-derived the Stinespring chain: `V_w^†V_w=1` needs D1(c)'s `l=𝟙` gauge (I verified `Σ_s (A^s)^†A^s=𝟙` numerically before use); `‖Ψ_D(r)‖_1≤‖D‖‖r‖_1=‖D‖`; `\|tr Ψ_C(Z)\|≤‖C‖‖Z‖_1`; `⟨𝟙,E_C P E_D(r)⟩=ω_A(C)ω_A(D)` uses trace preservation | `\|ω_A(CD)−ω_A(C)ω_A(D)\| ≤ ‖C‖‖D‖·‖E^{d_sep}−P‖_{1→1}`.  **Correct, and the bounding factor contains no reference to `C`, `D` or their lengths** — support-length independence is trivial, as §6 now says.  D1(c) delivers exactly "*for every `λ̃∈(λ_E,1)` there is `C_λ̃` with `‖E^m−P‖≤C_λ̃λ̃^m`*", so `⟨1⟩3`'s every-`λ̃` quantifier **is** the one the proof delivers (fifth survival) |
| **W3** | the D31-C2 target, from a **different tensor basis** | standard spin-1 `S^z` AKLT; both fixed points checked; `d=1..12` | `ω_A((I+S^z)_0(I+S^z)_d)−ω_A(I+S^z)^2 = 4/3·(−1/3)^d` to `≤1.04e−15` at every `d`.  The checker's ground truth is independently right |
| **W4** | the C1b grid, from that same different basis | full 27-point recomputation | `agreement 5.92e−16`; `max_ratio 0.04938271604938 @ (1,1,2)`; `ratio_route @ (1,1,6)`; `monotonicity_excess −6.5030737e−03 @ (1,2,6)`.  And a **closed form**: `ratio(1,1,2)=\|4/3·(−1/3)^3\|/2^{1+1−2}=4/81=0.049382716`, exactly the reported maximum.  `‖C_w‖=2^w` confirmed by SVD |
| **W5** | (R8)+(R19) from ML2 (18), **two algebraic routes** | `S(K,q)=(c−e^{−iq})/(e^{iq}−c)` with `K=k_s+k_h`, `q=(k_h−k_s)/2`, `c=cos(K/2)`, versus r4's rational form `−(e^{i(k_s+k_h)}−2e^{ik_s}+1)/(e^{i(k_s+k_h)}−2e^{ik_h}+1)` | The two forms agree to `≤5.7e−16`; `\|S_{12}\|=1.000000000000` (so `⟨1⟩7.⟨2⟩3`'s adjoint step is valid); `S_{12}(0,k_h)=1` exactly; `Re[(1−S)/(−2ik_s)] → 1` as `1.0000917, 1.0000092, …` at `k_h=0.4,1.0,2.0,3.0`.  **`1−S_{12}=−2ik_s+O(k_s²)` reproduced** |
| **W6** | the size of the R8 obstruction in `⟨2⟩5`'s own units | `‖Q_{k_s}\|k_h⟩−\|B^{in}⟩‖/‖\|B^{in}⟩‖ = \|1−S_{12}\|/√(\|S_{12}\|²+1)` | `1.5487e−01, 1.4272e−02, 1.4155e−03` at `k_s=10^{-1},10^{-2},10^{-3}` — `√2·k_s(1+O(k_s))`, reproducing r4's V4 to five digits.  The constructed and adjudicated families **still** differ at exactly the order `⟨2⟩5` reports; the relabel is therefore the *honest* disposition, not a cosmetic one |
| **W7** | `⟨1⟩9.⟨2⟩5`'s Taylor, on a fresh grid | `f` supported on `[1,2]`, `‖f‖_2=1`, `m_1=1.5`; `I=[0.5,2.5]` on 401 points; `A(ε)(h)=∫dμ_f(u)S(εu,h)` | `‖A(ε)−A(0)−εm_1∂_{k_s}S(0,·)‖_{L²(I)}/ε² = 9.92, 8.59, 8.48` at `ε=10^{-1},10^{-2},10^{-3}` — a **stable `O(ε²)` remainder, no hidden `ε^{-1}`**.  Same conclusion as r4's V5 with a different constant because a different grid; the mathematics is right |
| **W8** | `⟨1⟩2.⟨2⟩3`'s bound-band fence — a **PROVED-row clause** | from ML2 (18)–(19): `E_sc−E_b=J(2−2c\cos q)−J(1−c²)=J(1+c²−2c\cos q)=J\|e^{iq}−c\|²` | Identity exact; the only zero needs `e^{iq}=c∈[0,1]`, i.e. `q=0, c=1, K=0`, excluded by D31(4).  Numerically `E_sc−E_b → J\sin²(k_h/2)` as `k_s↓0` (`0.9949961777` vs `0.9949962483` at `k_h=3, k_s=10^{-6}`).  **`d_B>0` on compact packets: CORRECT** |
| **W9** | `⟨1⟩9.⟨2⟩4`'s D6⊨D31 — the row's **nonvacuity certificate** | read D1, ML2 `⟨1⟩5.⟨2⟩4`, and the shard's argument | (1) `ker H=ℂΩ` in the GNS space: the ferromagnetic zero modes other than `Ω` are the constant-coordinate waves, not in `ℓ²` — correct; gaplessness is no obstruction since the `k→0` magnon is non-normalizable.  (2) `Γ_M` isometric with `HΓ_M=Γ_Mω`, and in charge one it is the *entire* sector, so "isolated within the charge-one sector" is trivially true.  (5) **ML2 (21) resolves the identity into exactly two summands with "no remaining spectral subspace"** — so `𝓡_inel=∅`, `Θ_inel=η_inel=+∞`, and `d_B>0` by W8.  **The certificate is sound and uses no D29 clause.**  Its *placement* is R5-O1 |
| **W10** | `⟨1⟩5.⟨2⟩4`'s Cook majorant | recounted the cone sum: `‖F_t‖_{ℓ¹}=O(\|t\|²)` on the product cones times `⟨ε_v\|t\|/2⟩^{-N}`, plus `O(\|t\|^{2−N})` off-cone | `O(\|t\|^{2−N})`; `N≥5` gives `C\|t\|^{-3}`, integrable.  Arithmetic correct.  `⟨1⟩6.⟨2⟩2`'s `O(\|t\|^{4−N})` is the same count with four creators |
| **W11** | reliance audit (obligation 5) | grepped the shard against `claims/CLAIMS.md` statuses | `S2-2body` **PROVED**, `ML2` **PROVED**; `ML1/ML3/ML6` named only as CONJECTURE/open.  **No `ML4`, no `ML4-Ward`, no `ML5`, no `𝒮_W`.**  Every bare `S2` token (lines 1, 98, 541) is the *lane name* "Lane S2", never the REFUTED claim id.  `Bethe`/`integrab` occur three times, all as explicit disclaimers.  **CLEAN, fifth consecutive round** |
| **W12** | lockstep of §7's mirror row | `cmp` on the extracted lines | **IDENTICAL, 3943 bytes.**  Second consecutive round in which the prover's central lockstep claim is literally true |

---

## 2. FATAL

None.  **Fifth consecutive round with none.**

---

## 3. MAJOR

### R5-O1 (MAJOR) — the PROVED row's nonvacuity certificate is proved at `⟨1⟩9.⟨2⟩4`, outside the `where-proved` range the draft row declares, and beneath an ASSUME that grants the D29 interface

**(a) Location.**
`theory/ansatz-scattering-2m.md` §7, **ROW SPLIT proposal**, the `AC-EX-2M`
row: its statement clause "*D6 directly satisfies D31(1)--(5)*" together with
its `where-proved` cell "*theory/ansatz-scattering-2m.md ⟨1⟩2--⟨1⟩7*".  The
step at issue is `⟨1⟩9.⟨2⟩4` ("**[NEW — D6 satisfies D31]**"), sitting under
`⟨1⟩9`'s "**ASSUME.** D31 and adjudicated D29 interface clauses 1--4 … **PROVE.**
(A2M.3)".

**(b) My computation.**  Four parts.

*(i) The clause's only proof is outside the declared range.*  `grep` for
`D31(1)--(5)` in the shard returns exactly two proof-side hits: line 591
(`⟨1⟩9.⟨2⟩4`'s PROVE, "*D6 is a nonempty instance of D31(1)--(5)*") and the
row cells themselves.  Nothing in `⟨1⟩2`–`⟨1⟩7` proves D6 ⊨ D31; `⟨1⟩2.⟨2⟩3`
supplies only clause (5)'s `d_B>0` and `Θ_inel=+∞`.  So the draft
`where-proved` cell **points at a range that does not contain the proof of one
of its own statement clauses**.

*(ii) The clause is load-bearing, not decorative.*  `AC-EX-2M` at PROVED is a
*conditional implication* from D31.  Without D6 ⊨ D31 the implication has no
exhibited model, and the campaign's own landmine applies verbatim
(`briefs/soft-index-target.md`: "*A constraint on limit points of a family
with NO limit points is empty … Silence here is a MAJOR objection*").  The
nearest PROVED sibling, `AC-EX`, is scrupulous on exactly this axis — it says
outright "*(D28-C) is the load-bearing hypothesis and **is unverified on any
model***".  `AC-EX-2M` is in the *better* position (D31 **is** instantiated),
which is precisely why the row must cite the instantiation correctly.

*(iii) Under L6b the step inherits a D29 hypothesis, and it is an orphan.*
Lamport discipline: a `⟨2⟩` step is proved under its parent's ASSUME, and its
PROVE must contribute to the parent's PROVE.  `⟨1⟩9.⟨2⟩4` violates both.  Its
parent assumes "*adjudicated D29 interface clauses 1--4*", i.e. `(D29-den)`;
and its PROVE — "*D6 is a nonempty instance of D31(1)--(5)*" — is **not part
of (A2M.3)**, which is the diagonal-compactness/HR statement.  So an auditor
applying L6b to the split's own question ("does the PROVED half consume the
D29 interface?") gets the answer "yes: its nonvacuity certificate does",
*even though the mathematics does not*.  In a round whose entire basis is
D29-independence, that is not a formatting complaint.

*(iv) The mathematics itself is fine, and I verified it.*  `⟨1⟩9.⟨2⟩4`'s
Justification cites "*D1, D6's positive swap form, proposed D31, ML2
equations (17)--(21), and the Plancherel resolution ML2 (21)*" — **no D29
clause**.  W9 above re-derives every one of its five claims independently,
including the decisive one: ML2 (21) resolves the identity into exactly the
scattering and bound summands with "*no remaining spectral subspace*", so
D31(5)'s inelastic inventory is empty on D6 and `η_inel=+∞`.

**(c) FIX DEMAND.**  Hoist the step: move `⟨1⟩9.⟨2⟩4` verbatim out of `⟨1⟩9`
to a new top-level step — `### ⟨1⟩7′. D6 is a nonempty instance of D31`, placed
after `⟨1⟩7` — with "**ASSUME.** D6 and fixed compact packets obeying D31(4).
**PROVE.** D6 satisfies D31(1)--(5)", and add one sentence: "*This step uses
no D29 interface clause; it is stated here so that `(A2M.1)`--`(A2M.2)`'s
conditional implication carries its own nonvacuity certificate.*"  Renumber
`⟨1⟩9`'s remaining sub-steps.  Until the hoist lands, apply **my**
`where-proved` cell (§9), which names `⟨1⟩9.⟨2⟩4` explicitly and records that
its justification cites no D29 clause.  Do **not** apply the prover's draft
cells.

**(d) SURVIVING WEAKER STATEMENT.**  Everything the clause asserts is true and
independently verified (W8, W9): *D6 satisfies D31(1)--(5) — one D1 injective
translation-invariant vacuum with `ker H=ℂΩ_A`, an exact charge-one band map
that is the whole charge-one sector, covariant filtered creators, compact
separated packets, one isolated charge-two bound band with `d_B>0` on those
packets, and an empty alternative-propagating inventory (`Θ_inel=η_inel=+∞`)
by ML2 (21) — and this uses no D29 clause.*  The independence of
`(A2M.1)`--`(A2M.2)` from the D29 interface (W1) is **untouched** by this
objection; the split stands, on my cells.

---

## 4. Checker audit (obligation 4 + all 2026-08-29 standing obligations)

All runs `python3 -O` from the repository root, on the committed file.
Mutants on copies in a temp dir, never in place.

### 4.1 Exit **path** per registered mode

| run | gates fired | decisive numbers | exit |
|---|---|---|---|
| green | — | `C1a direct 3.354e-15 route 3.243e-15 ratio 5.605e-10`; `C1b agreement 1.128e-16, max_ratio 0.049383@(1,1,2), ratio_route 1.187e-15@(1,1,6), route_guard 0.000e+00@(1,1,2), monotonicity −6.503e-03@(1,2,6)` | **0** |
| `--red-lambda` | **G0** | `λ̃=3.7 ∉ (1/3,1)` | 1 |
| `--red-truth` | **G1,G2** | both `1.000000e-06` | 1 |
| `--red-c1a` | **G2,G3** | `1.000000e+00`, `2.400000e+00` | 1 |
| `--red-c1b-sub` | **G4,G5,G6** | `1.000e+00`, `15.990245@(1,1,6)`, `1.598049e+01` | 1 |
| `--red-c1b` | **G5,G7** | `1.404664@(3,2,2)`, `6.145405e-01@(3,2,2)` | 1 |
| `--red-supportfold` | **G6** | `1.646091e-02@(2,2,2)` | 1 |
| `--red-route-collapse` | **G8** | `1.000000e+00@(1,1,2)`; `agreement` and `ratio_route` both print `0.000e+00` | 1 |

`grep -cE '^\s*assert\b'` → **0**.  `violations()` returns *all* fired gates
before `main` exits, so no gate is masked (`--red-c1b-sub` demonstrates three
in one line).

### 4.2 Gate reachability — complete

G0 λ̃-domain · G1 C1a direct · G2 C1a route · G3 C1a ratio · G4 C1b agreement ·
G5 C1b cap · G6 C1b `ratio_route` · G7 C1b monotonicity · G8 `route_guard`.

**Every one of the nine has a registered reaching mutant** (table above).
r4's R4-O3 hole (G1, G4 unreached) is closed.

### 4.3 Red-mode specificity — no two are bit-identical

Violation sets `{G0}`, `{G1,G2}`, `{G2,G3}`, `{G4,G5,G6}`, `{G5,G7}`, `{G6}`,
`{G8}` are pairwise distinct.  ✔

### 4.4 Data mutation, not only code (standing obligation)

| mutant | what is falsified | result |
|---|---|---|
| `--red-truth` (registered) | the **independent closed-form ground truth**, `+1e-6` | exit 1, G1+G2.  **Not self-fulfilling** ✔ |
| `d1` — `A^a=σ_a/√3 → σ_a/2` | tensor normalization | exit 2 (G1,G2,G3,G5) |
| `d2` — `RIGHT_FIXED → diag(0.6,0.4)` | transfer fixed point | exit 2 (G1,G2,G3,G5) |
| `d3` — `C=I+2S^z` | the observable | exit 2 (G1,G2) |
| `d4` — `block_operator_norm → 1.0` | the SVD norms | exit 2 (G5, `cap 0.197531`) |
| `c3` — subtraction coefficient `1 → 1.000001` | a **genuine route error** | exit 2, `agreement 1.000e-06`, `ratio_route 1.600e-05` — the `16×` factor, confirmed |
| `L` — `LAMBDA_TILDE ∈ {−5.0, 1e6, 1/3}` | absurd/boundary domain | exit 2 in all three (r4's R4-O4 regression **closed**) |

### 4.5 Deductive subsumption

- **G6 ⊆ 16·G4**, exactly, on this grid — re-derived symbolically and
  confirmed by `c3` (`1e-6 → 1.6e-5`).  G6 can fire alone only for pointwise
  agreement in `(6.25e-14, 1e-12]`.  §6 and the merged row both say so.
- **G1/G2** are not mutually subsumed (they test different routes against the
  same target); together they subsume any C1a route-agreement gate, which is
  why none exists.
- **G8 is subsumed by nothing and subsumes nothing — because in green it is
  identically zero for every input.**  See R5-O3.

---

## 5. MINOR

### R5-O2 (MINOR) — the draft PROVED row silently drops the r3-adjudicated `ratio_route` retraction, and replaces it with a coverage advertisement my §4 contradicts

**(a)** `theory/ansatz-scattering-2m.md` §7, ROW SPLIT proposal, the
`AC-EX-2M` row's `where-tested` cell.

**(b)** Direct answer to the brief's question: in the **shard §6**, the
**module docstring** and the **currently merged row**, `ratio_route` is still
honestly labelled a retracted advertisement — I checked all three, and the
merged row carries "*the `ratio_route` gate (formerly `profile-agreement`) is
a rescaled duplicate of the agreement gate and does **NOT** certify that a
support-length factor is absent*".  It has **not** quietly regained a claim
there.  But the *draft split row* drops that adjudicated caveat entirely, and
substitutes "*green plus seven registered red modes … **every gate has a named
exit path***".  The blanket sentence that replaces it ("*corroborates only the
D31-C2 transfer computation*") is not false, so nothing is re-claimed — but an
adjudicated retraction disappearing from a row **at the moment its status
ratchets up** is exactly the drift this method exists to catch, and the
coverage sentence overstates G8 (R5-O3).  This is MINOR **only because I am
supplying the corrected cell**; applied as drafted it would be MAJOR.

**(c) FIX DEMAND.**  Use §9's `where-tested` cell, which restores the
`ratio_route` retraction with its `16×`/`(6.25e-14,1e-12]` quantification,
adds the `λ̃=1/2` cap caveat, and states G8's true status.

**(d) SURVIVING WEAKER STATEMENT.**  The certificate genuinely establishes, on
AKLT: the connected two-point function equals `4/3·(−1/3)^d` for `d=1..12` by
two routes agreeing to `1.1e−16`; the normalized ratio is `≤0.049383<0.1`
over the 27-point grid at `λ̃=1/2`; it is strictly decreasing in both support
lengths at every `d_sep` (margin `−6.503e−03`).  All independently reproduced
from a different tensor basis.

### R5-O3 (MINOR) — G8 `route_guard` is `0` by algebra in green and blind to every data mutation: a code-shape guard, not a route-independence test

**(a)** `theory/checks/ansatz_scattering_2m_check.py`, `check_c1b`, the
`probe_direct, probe_fixed = connected_routes(…, drop_fixed_subtraction=True,
…)` block and `probe_error = abs((probe_fixed − probe_direct) − one_c*one_d)`;
§6's "*must then fail the route-independence gate*".

**(b)** Simplify it symbolically, per the standing obligation.  With
`drop_fixed_subtraction=True`, `connected_routes` returns
`direct = raw − ω_Cω_D` and `fixed = raw` **from the same `raw`**.  Hence

`probe_error = \|raw − (raw − ω_Cω_D) − ω_Cω_D\| ≡ 0`,

for **every** tensor, fixed point, observable, separation and support length.
The green run prints exactly `route_guard=0.000e+00`, and I confirmed
data-blindness empirically: mutants `d1` (wrong tensor), `d2` (wrong fixed
point), `d3` (wrong observable), `d4` (wrong norms) and the whole `λ̃` battery
all leave `route_guard=0.000e+00` while other gates scream.  A genuine route
error (`c3`) also leaves it at `0`.  This is the campaign's **pattern-#3**
shape (`sites·two_s/sites − two_s ≡ 0`) recurring for the fifth time — with
one honest difference from patterns 1–4: **it can fail.**  It killed all three
route-collapse implementations I built (`--red-route-collapse`;
`direct := fixed`; `fixed := direct`), each on G8 alone.  So it is a *live
assertion about the shape of the code*, and zero evidence about AKLT, D31-C2,
or anything the row claims.

**(c) FIX DEMAND.**  Either (α) make it a sensitivity probe with content —
recompute the fixed route with `subtracted = propagated − (1+δ)·fixed_projection(right)`
for a fixed `δ=10^{-6}` and require the response to equal `δ·ω_Cω_D` to
`10^{-12}`, which does move under data mutation — or (β) keep it and rename it
honestly in §6 and in the row: "*`route_guard` is an algebraic identity in
green (`≡0` for every input); it guards the *shape* of the two route
expressions against a future collapse and certifies no number.*"  §9's
`where-tested` cell takes (β).

**(d) SURVIVING WEAKER STATEMENT.**  G8 does what R4-N7 asked for: a future
edit that makes the two C1b routes the same expression is now caught rather
than silently printing `0.0` on both G4 and G6.  Route *agreement* itself is
certified by G4 (`1.128e-16`), which `c3` shows is live and sharp at `1e-6`.

### R5-O4 (MINOR) — "*a one-element `(ACE2M-SR)` instance for the constructed-channel family*" names an object `(ACE2M-SR)` does not define

**(a)** `⟨1⟩9.⟨2⟩5`'s new paragraph; `⟨1⟩1(A2M.3)`; §8 **Conditional**; the
merged row; and the draft `AC-EX-2M-D29` row ("*The only current `(SR)`
instance …*").

**(b)** `(ACE2M-SR)` is defined at `⟨1⟩8` as a condition on
`A_j(ε):=lim_{t→±∞}lim_{N→∞}𝒜_{N,W_j,σ_j,t}(ε)`, where `𝒜` is fixed by
interface clauses 1 and 3 as **the adjudicated D29 datum**.  There is no
`(ACE2M-SR)` for any other family, so "an `(ACE2M-SR)` instance for the
constructed-channel family" is, read literally, an instance of a condition
whose subject is a different object.  What `⟨2⟩5` actually establishes is:
*the conditions displayed in `(SR)` — `C¹` extension to `ε=0`, relative
compactness of the jet, and the `j`-uniform equicontinuity — hold for the
constructed-channel datum `A(ε)(h)=∫dμ_f(u)S_phys(εu,h)`.*  Additionally, the
"existence of the `N,t` limits" clause of `(SR)` is not *satisfied* by `⟨2⟩5`
but **bypassed**: `⟨2⟩5` never forms an `N` or a `(W,σ)` family at all (it is
"exhaustion-free, infinite-chain"), so calling every uniformity clause
"trivially satisfied" is right only for the two uniformity clauses, not for
the limit-existence clause.  The direction of the error is *harmless* — it
attributes **less** to D29, not more — but L4 forbids a symbol meaning two
things.

**(c) FIX DEMAND.**  In `⟨1⟩8`, add one sentence after `(SR)`: "*Read as a
condition schema, `(SR)[X]` denotes the same three clauses with `A_j` replaced
by any `ε`-family `X` in `L²(I)`; `(ACE2M-SR)` is `(SR)[A_j]` for the D29
datum.*"  Then say "`(SR)[A]` holds for the constructed-channel datum" at
`⟨2⟩5` and in both rows.  §9's `AC-EX-2M-D29` cell already avoids the abuse by
saying "*the only datum for which the `(SR)` conditions have been verified*".

**(d) SURVIVING WEAKER STATEMENT.**  The mathematics is right and reproduced
(W7): `A∈C¹([0,ε_★];L²(I))` with `A(ε)=A(0)+εm_1∂_{k_s}S_phys(0,·)+O_{L²(I)}(ε²)`,
`m_1=∫u\,dμ_f`, no hidden `ε^{-1}`, and a one-element family is trivially
relatively compact with an equicontinuous jet.

### R5-O5 (MINOR) — two register defects in the draft PROVED row: an off-house status cell, and D31(5)'s inelastic clause stated backwards

**(a)** The draft's status cell "`**PROVED** (conditional on D31)`", and its
statement clause "*avoid every D31-listed fiberwise-isolated charge-two bound
band and inventoried inelastic channel below threshold*".

**(b)** *(i)* The house register for a conditional promotion is fixed by the
two nearest PROVED rows: `AC-EX` uses "`**PROVED** (conditional, ACE.1--ACE.2;
per memory-index-r3.md §4 amended sentence)`" and `M-INDEX-spec` uses
"`**PROVED** (conditional, per memory-index-r2.md §4, gates cleared
memory-index-r3.md)`".  Both name the sub-claims and/or the adjudicating
verdict.  "(conditional on D31)" names neither, so the DAG would not record
*which* verdict ratcheted the row.  *(ii)* D31(5) requires
`ω(k_1)+ω(k_2)+η_inel < θ_r(k_1+k_2)`: the inventoried channels sit **above**
`Θ_inel` and it is `ran W_±` that sits **below**.  "*inventoried inelastic
channel below threshold*" reads as if the channels were below it.  On D6 the
clause is vacuous anyway (`𝓡_inel=∅`, W9), which is exactly why a sloppy
reading would go unnoticed.

**(c) FIX DEMAND.**  Use §9's cells: status
"`**PROVED** (conditional, A2M.1--A2M.2; per ansatz-scattering-2m-r5.md §9)`",
and "*orthogonal to every alternative propagating channel in D31(5)'s
inventory `𝓡_inel`, whose joint energies exceed `sup_{I_2}E+η_inel`*".

**(d) SURVIVING WEAKER STATEMENT.**  The mathematical content is right:
`⟨1⟩7.⟨2⟩2`'s joint-spectral argument does give `P_BW_±=0` from `d_B>0` and
orthogonality to every inventoried channel, because `W_±` intertwines the
joint `(H,P)` action and `ran W_±` lies in the joint spectral set `I_2`.

### R5-O6 (MINOR) — the draft `AC-EX-2M-D29` row drops two scoping items the merged row carries

**(a)** The draft `AC-EX-2M-D29` statement cell, versus `claims/CLAIMS.md`
l.782.

**(b)** Two losses, both in the direction of *less* disclosure.  (1) The
merged row says "*its full `(W,σ)`-uniform version is open on every model*";
the draft omits it, so a reader of the split has no record that even the
constructed-channel `(SR)` is unproved in its uniform form on D6 (`⟨1⟩9.⟨2⟩6`
still says so in the shard, but the DAG row would not).  (2) The merged row
names the provenance — "*`theory/soft-index.md` §7.1 D29(2) and
`theory/soft-index-b.md` §M1, the latter adopted by
`theory/verdicts/soft-index-adjudication-r1.md` §3.1*" — which was R3-N7's
fix; the draft replaces it with a bare description of the object.  Nothing
false is stated, but auditability regresses.

**(c) FIX DEMAND.**  Restore both; §9's `AC-EX-2M-D29` cell does.

**(d) SURVIVING WEAKER STATEMENT.**  The draft's positive content — the two
separated statements, the "does NOT apply" sentence, the R8 mismatch, and the
two named missing steps — is correct and correctly quantified.

### R5-O7 (MINOR) — `⟨1⟩2.⟨2⟩2`'s non-circularity sentence is false as written

**(a)** `⟨1⟩2.⟨2⟩2`'s Justification: "*This is a forward reference without
circularity: **none of `⟨1⟩3`--`⟨1⟩7` uses `⟨1⟩2`**, so the dependency chain
closes independently.*"

**(b)** `⟨1⟩5.⟨2⟩4` does use `⟨1⟩2`: "*Here `C_N=C_N(ε_v,s_N(F))` has the
packet-seminorm dependence and soft-family divergence **displayed in
`⟨1⟩2.⟨2⟩1`***".  The blanket sentence is therefore false, and it matters
because the promoted row's `where-proved` is `⟨1⟩2--⟨1⟩7` and the
forward-referencing step `⟨1⟩2.⟨2⟩2` proves a *statement clause* of that row
(bound-band avoidance).  The correct argument survives at finer granularity
and I checked it: `⟨1⟩2.⟨2⟩1`'s own justification cites only D3(a), D12(a′),
D31(4) and the brief — **no forward reference** — and only `⟨1⟩2.⟨2⟩2` points
forward, to `⟨1⟩7.⟨2⟩2`, which nothing in `⟨1⟩3`–`⟨1⟩7` uses.  So the
dependency graph is acyclic at step granularity; the sentence just states the
wrong reason.  (`⟨1⟩5.⟨2⟩4`'s reference is a scope annotation, not a premise:
the `C\|t\|^{-3}` majorant holds at fixed packets regardless.)

**(c) FIX DEMAND.**  Replace with: "*This is a forward reference without
circularity: `⟨1⟩2.⟨2⟩1` cites nothing later, and `⟨1⟩2.⟨2⟩2` is the only step
of `⟨1⟩2` that points forward — to `⟨1⟩7.⟨2⟩2`, which no step of
`⟨1⟩3`--`⟨1⟩7` uses.  `⟨1⟩5.⟨2⟩4` refers to `⟨1⟩2.⟨2⟩1` for scope only, not as
a premise.*"

**(d) SURVIVING WEAKER STATEMENT.**  There is no circularity: the step-level
dependency graph of `⟨1⟩2`--`⟨1⟩7` is acyclic, as I verified leaf by leaf
(W1).

---

## 6. NOTE

**R5-N1 — the fix reached the leaf, and I say so unprompted.**  r4's R4-O1 was
the sharpest objection of four rounds and the repair is exact: the
Justification line lost `⟨1⟩8.⟨2⟩1--⟨2⟩2`, kept the one leaf that genuinely
licenses the object (`⟨1⟩7.⟨2⟩3`, where `W_+^*W_-=S_phys` is proved), and the
new disclaimer displays the obstruction quantitatively.  Fix (A) executed as
written.

**R5-N2 — the promoted material is byte-frozen.**  `⟨1⟩2`--`⟨1⟩7` has zero
diff hunks across the r3→r4 and r4→r5 repairs.  The text going to PROVED has
been attacked in four rounds and edited in none of the last two.

**R5-N3 — the prover quarantined its own proposal.**  §7 keeps the merged row
byte-identical as an explicitly labelled "*audit mirror … Do not reapply it*",
and files the split beneath it as a proposal, with "*No edit to
`claims/CLAIMS.md` was made*".  Correct lane discipline under an instruction
to draft rows it cannot merge.

**R5-N4 — `--red-supportfold` is still a self-fulfilling mutant** (r4's
R4-O2(iii)): it multiplies `ratio` and not `direct_ratio` *after*
`agreement_error` is recorded, so the only gate it can reach is the one that
compares those two.  Unchanged, and correctly retracted rather than defended.

**R5-N5 — the `16×` amplification is now confirmed three ways**: symbolically
(shared denominator `2^{w_C+w_D−d_sep}`, min `1/16`), by the reported green
maximum sitting at `(1,1,6)` where the amplification is attained, and by
mutant `c3` (`agreement 1e-6 → ratio_route 1.6e-5` exactly).

**R5-N6 — no downstream blast radius, second confirmation.**  Nothing under
`theory/` consumes `AC-EX-2M`.  The split can be applied and, if wrong,
reverted, at zero cost to the corpus.

**R5-N7 — `\|S_phys\|=1` is load-bearing and true.**  `⟨1⟩7.⟨2⟩3`'s adjoint
step `W_+^*W_-=S_{12}` needs `\bar S^{-1}=S`.  ML2 (18) gives it because `c`
is real, and I confirmed `\|S_{12}\|=1.000000000000` numerically over the
whole grid.

**R5-N8 — the ML2/D7 anchor's velocity-ordering caveat is in the shard but not
in the draft row.**  `⟨1⟩7.⟨2⟩3` ends "*If the velocity order is reversed, the
same computation gives `S_{21}`*".  §9's cell carries it.

**R5-N9 — L3 citation discipline clean.**  Every reference in the diff
resolves to a real `\label` in `refs/arxiv-1412.2970/Scattering_spin-AHP1.tex`
or to a numbered equation in `theory/ml2-completeness.md` that I opened and
read (18), (19), (21).  No from-memory citation.

**R5-N10 — the D6 `d_B>0` computation is exact, not asymptotic.**
`E_sc−E_b=J\|e^{iq}−c\|²` is an identity, not an estimate, and its unique zero
is excluded by D31(4).  This is the cleanest single step in the shard.

**R5-N11 — `⟨1⟩8` clause 3 is honest about what it assumes.**  "*Both
displayed inequalities are assumptions; Cauchy--Schwarz … is the model for the
numerator assumption, **not a derivation of it in this shard***".  Unchanged
from r4 and still the right register.

**R5-N12 — the `λ̃` domain gate is a domain gate only.**  G0 rejects
`λ̃∉(1/3,1)` but the `0.1` cap is still a single-point statement: `λ̃=0.9999`
passes green, `λ̃=0.34` fails.  §6 discloses this; no gate certifies
`⟨1⟩3`'s every-`λ̃` quantifier, which is proved analytically instead (W2).

---

## 7. VERIFIED CORRECT — fenced, do not churn

r3 §7 and r4 §7 remain in force and were not re-litigated.  New or
re-confirmed this round:

- **The R4-O1 repair at the leaf** — `⟨1⟩9.⟨2⟩5`'s Justification line, PROVE
  line, and disclaimer paragraph; and the absence of any surviving step that
  reads the D29 identification as available (nine sites checked).
- **The independence of `(A2M.1)`--`(A2M.2)` from the D29 interface** (W1) —
  21 Justification leaves in `⟨1⟩2`--`⟨1⟩7`, zero D29 citations.  *This is the
  finding the split rests on; it is settled.*
- **`⟨1⟩3.⟨2⟩1--⟨2⟩2` (D31-C2)** — chain identity, `1→1` bound, support-length
  independence, and the every-`λ̃` quantifier matching D1(c) (W2).  Fifth
  survival.
- **The D31-C2 target and the whole C1b grid, reproduced from a second tensor
  basis** (W3, W4), including the closed form `ratio(1,1,2)=4/81`.
- **`\|S_{12}\|=1`, `1−S_{12}=−2ik_s+O(k_s²)`, and the `√2·k_s` relative
  mismatch** — two independent algebraic forms of `S(K,q)` (W5, W6).
- **`⟨1⟩9.⟨2⟩5`'s Taylor arithmetic** on a fresh grid: stable `O(ε²)`
  remainder, no hidden `ε^{-1}` (W7).  *Fenced as mathematics; its filing is
  now correct too.*
- **`⟨1⟩2.⟨2⟩3`'s `E_sc−E_b=J\|e^{iq}−c\|²` fence and the `k_s↓0` limit**
  `d_B→J\sin²(k_h/2)` (W8).
- **`⟨1⟩9.⟨2⟩4`'s D6 ⊨ D31(1)--(5) content**, including `𝓡_inel=∅` from ML2
  (21)'s two-summand resolution (W9).  *The content is fenced; its placement
  is R5-O1.*
- **`⟨1⟩5.⟨2⟩4` / `⟨1⟩6.⟨2⟩2`'s cone counting** — `O(\|t\|^{2−N})` and
  `O(\|t\|^{4−N})`, `N≥5` integrable (W10).
- **Checker hygiene and coverage**: zero bare `assert`; green exits 0; all
  seven red modes exit 1; all nine gates reachable; all seven violation sets
  distinct; `violations()` masks nothing; the ground truth is falsifiable;
  four data mutants and the `λ̃` battery all die.
- **Byte-for-byte lockstep** of §7's mirror row with `claims/CLAIMS.md`
  (3943 bytes), and presence of r4 §9's 703-character replacement sentence
  verbatim (W12).
- **Reliance audit** (W11): no REFUTED row, no ML4-Ward `n≥2`, no ML5, no
  `𝒮_W`, no Bethe/integrability hypothesis.  Every bare `S2` is the lane name.

---

## 8. Register comparison against the nearest PROVED rows

Nearest sibling: **`AC-EX`** (this lane's predecessor, a conditional PROVED
row).  Nearest adjudicated conditional with a named open interface:
**`M-INDEX-spec`**.

| item | `AC-EX` / `M-INDEX-spec` register | draft `AC-EX-2M` (r5) | verdict |
|---|---|---|---|
| conditionality at the point of statement | "*proved **only** as the conditional implication*" | same words, same place | **in register** |
| hypotheses flagged as assumed, not derived | "*(D28-C) … is assumed, not derived*" | "*D31(1)--(5)'s exact band, creator, covariance and threshold data are hypotheses, not consequences of a variational ansatz*" | **in register** |
| **the load-bearing hypothesis's instantiation status** | `AC-EX`: "*(D28-C) is the load-bearing hypothesis and **is unverified on any model***" | draft asserts "*D6 directly satisfies D31(1)--(5)*" but points `where-proved` at a range not containing the proof | **BREACH → R5-O1** (repaired in §9: D31 *is* instantiated, and the row now says where) |
| negative inventory | long, explicit, closes with completeness | present and complete | **in register** |
| status cell form | "`**PROVED** (conditional, ACE.1--ACE.2; per <verdict>)`" | "`**PROVED** (conditional on D31)`" | minor breach → R5-O5 |
| checker caveats carried into the row | "*Neither certificate touches (D28-C)*"; dead-mutation disclosure | adjudicated `ratio_route` retraction **dropped** | minor breach → R5-O2 |
| the inapplicable neighbour named inside the row | `M-INDEX-spec`: "*its unconditional existence is **REFUTED***" | `AC-EX-2M-D29`: "**This theorem does NOT apply to the adjudicated D29**" + the displayed `−2ik_s\|P_{12}⟩` | **in register** |

After §9's cells are applied, `AC-EX-2M` is in `AC-EX`'s register on every
axis — and on the instantiation axis it is **stronger**, since D31 has a model
and (D28-C) does not.

---

## 9. MERGE / HOLD (deliverable)

### The row split — **MERGE**

The independence claim is **TRUE** and I tested it the way the brief demanded,
by walking the proof rather than reading the response: every Justification
leaf of `⟨1⟩2`–`⟨1⟩7` (W1), zero consumption of `(ACE2M-LSZ)`, `(ACE2M-SR)`,
`(D29-den)` or the D29 identification, the only mention being an explicit
disclaimer of use.  `(A2M.1)`--`(A2M.2)` have now survived five hostile rounds
with **0 FATAL**, their text has been byte-frozen through the last two repairs,
D31-C2 has been independently reproduced four times and the checker twice from
different tensors, D31 is instantiated on a model, and no shard downstream
depends on the row.  Keeping this hostage to an open interface clause is not
honest conservatism; it is mis-filing.

**`AC-EX-2M-D29` stays at SKETCH.**  Named missing steps, unchanged from r4
and re-verified this round:
1. **Branch (i)** — prove at `O(k_s)`, with a displayed uniform remainder,
   that the `T→∞` D29 readout's connected packet-amputated on-shell pairing
   equals the constructed-channel one, despite the PROVED mismatch
   `Q_{k_s}\|k_h⟩−\|B^{in}⟩=−2ik_s\|P_{12}⟩+O(k_s²)`, whose *relative* size
   `√2·k_s` I reproduced this round (W6) at exactly the order the first jet
   reports.
2. **An `(ACE2M-SR)` instance for the family `(SR)` constrains** — the
   fixed-time D29 datum `A_j(ε)` — including existence of its `N,t` limits.
   The only verified instance is the one-element constructed-channel datum
   (`⟨1⟩9.⟨2⟩5`), which by (1) backs no D29 claim.
3. *(recorded, not new)* `(D29-den)`'s two displayed bounds remain
   assumptions with no model verification, and the `(W,σ)`-uniform form of
   `(SR)` is open on every model including D6.

### The two rows, verbatim — apply without paraphrase

These **replace** §7's lockstep mirror row in `claims/CLAIMS.md` (and, by the
lockstep obligation, in the shard's §7).  They are my cells, not the prover's:
the draft's `where-proved`, status, `where-tested` and two statement clauses
are corrected per R5-O1, O2, O5, O6 and N8.  Both parse to six columns, like
`AC-EX`; every literal pipe is escaped.

**Row 1 — statement cell is column 2.**

| AC-EX-2M | Under D31/H-ACE2M over one D1 injective translation-invariant MPS vacuum, an exact momentum-filtered magnon band and two compact packet supports with velocity separation `ε_v>0` give the fixed-packet Cook limits `W_±` on the smooth product core `𝒟_{12}`; the limits are isometries, extend uniquely to the packet-domain closure, and intertwine joint time/space translations.  Their ranges are annihilated by the sum `P_B` of the D31-listed fiberwise-isolated charge-two bound-band projections (`d_B>0`) and are orthogonal to every alternative propagating channel in D31(5)'s inventory `𝓡_inel`, whose joint energies exceed `sup_{I_2}E+η_inel`.  D1's transfer gap derives (D31-C2) — for every `λ̃∈(λ_E,1)`, with a constant independent of both support lengths — and, with D31(3)'s uniform almost-locality, (D31-C4); no independent clustering hypothesis is assumed.  On D6--D8 a fixed packet range lies in the matching part of ML2's Jacobi scattering summand and is orthogonal to its two-string summand, with `W_+^*W_-` exactly multiplication by D7's `S_phys` (`S_{21}` under the opposite velocity ordering; `\|S_phys\|=1` by ML2 (18)).  **Adjudicated scoping (verbatim):** (A2M.1)--(A2M.2) are proved only as the conditional implication: D31/H-ACE2M (one D1 vacuum; an exact charge-one band map `Γ_M` with `HΓ_M=Γ_Mω`, isolated within the charge-one sector on the packet neighbourhoods; momentum-filtered uniformly almost-local creators; two compact packet supports with `dist(V_1,V_2)≥ε_v>0`; and the displayed bound/inelastic spectral inventory with margins `d_B>0`, `η_inel>0`) ⟹ the fixed-packet Cook limits exist on `𝒟_{12}`, are isometries, intertwine joint translations, and have the stated D31-listed spectral separation.  D31(1)--(5)'s exact band, creator, covariance and threshold data are hypotheses, not consequences of a variational ansatz; only D31-C2/C4 are derived, and they are derived from D1.  D31 is the load-bearing hypothesis and, unlike AC-EX's (D28-C), it is instantiated: D6 satisfies D31(1)--(5) (⟨1⟩9.⟨2⟩4 with ⟨1⟩2.⟨2⟩3, whose justifications cite no D29 clause), so the implication is not vacuous.  D31(4)'s `ε_0>0` clause enters no estimate in this row; only `ε_v` does.  Every estimate is at fixed packets: Cook and Gram constants carry the packet Schwartz seminorms `s_N(F)` and diverge like `ε^{-N}` along a soft rescaling `f_ε(k)=ε^{-1/2}f(k/ε)`, so nothing here is `ε`-uniform.  This row asserts nothing about the D29 interface, which lives entirely in `AC-EX-2M-D29` and is consumed by no step of ⟨1⟩2--⟨1⟩7.  No endpoint or equal-velocity construction, no soft-uniform Cook bound, no bound-state wave operator, no compatibility or range exhaustion across packet windows, and no asymptotic completeness is claimed. | **PROVED** (conditional, A2M.1--A2M.2; per ansatz-scattering-2m-r5.md §9) | D1, D3(a), D6--D8, D12(a′), D31, ML2 | theory/ansatz-scattering-2m.md ⟨1⟩2--⟨1⟩7, plus ⟨1⟩9.⟨2⟩4 for the D6 instance of D31 (r5 R5-O1 requires that step be hoisted out of ⟨1⟩9's D29 ASSUME; its justification cites no D29 clause) | theory/checks/ansatz_scattering_2m_check.py A2M-C1a/C1b: green exit 0 and seven registered red modes exit 1 under `python3 -O`, with exit paths `--red-lambda{G0}`, `--red-truth{G1,G2}`, `--red-c1a{G2,G3}`, `--red-c1b-sub{G4,G5,G6}`, `--red-c1b{G5,G7}`, `--red-supportfold{G6}`, `--red-route-collapse{G8}`; zero bare `assert`; all nine gates evaluated before exit.  The certificate corroborates ONLY the D31-C2 transfer identity on AKLT (`4/3·(-1/3)^d`, `d=1..12`; reproduced independently in a second tensor basis, ansatz-scattering-2m-r5.md §1).  It tests no Cook limit, exact band, spectral separation, or ML2/D7 identification.  **Gate caveats:** the `ratio_route` gate (formerly `profile-agreement`) is the agreement gate rescaled — bounded by `16×` it on this grid and able to fire alone only for pointwise agreement in `(6.25·10^-14,10^-12]` — and does NOT certify that a two-sided support-length factor is absent; support-length independence is proved analytically at ⟨1⟩3.⟨2⟩2, not numerically.  The `0.1` cap is a `λ̃=1/2` statement that already fails at `λ̃=0.34` and does not certify ⟨1⟩3's every-`λ̃` quantifier.  The `route_guard` gate (G8) is identically `0` for every input by algebra — a code-shape guard against route collapse, not a numerical certificate (r5 R5-O3) |

**Row 2 — statement cell is column 2.**

| AC-EX-2M-D29 | For Lane S1's adjudicated fixed-time D29 interface the shard establishes only two separated statements.  (1) *Diagonal compactness, conditional on (D29-den):* if the selected-hard-packet bounds `ess inf_α ess inf_{h∈I}\|𝒟_α(h)\|≥d_I>0` and `sup_α‖𝒝_α‖_{L²(I)}≤C_I<∞` hold for every allowed full index tuple `α`, then `sup_α‖𝒜_α‖_{L²(I)}≤C_I/d_I`, so every full-index sequence respecting (D29-order) `N→∞ ≺ t→±∞ ≺ (W↑ℤ,σ↓0)_j ≺ ε↓0` with `ε↓0` has a weakly convergent `L²(I)` subsequence.  This is Banach--Alaoglu on assumed bounds: both displayed inequalities are assumptions, not derivations, and no iterated-order datum is asserted to exist.  (2) *Creator-choice independence, `(ACE2M-LSZ)`, a THEOREM about Haag--Ruelle creator families:* at fixed `ε>0`, a soft creator family that is admissibly Haag--Ruelle, satisfies (2M-1P), and has velocity support disjoint from the hard packet (D31(4)) may be replaced by `a_{2,b}` without changing any connected on-shell `t→±∞` pairing (ported from `refs/arxiv-1412.2970` Theorem `Haag-Ruelle`, final clause).  **This theorem does NOT apply to the adjudicated D29.**  Both D29 proposals on record — `theory/soft-index.md` §7.1 D29(2) and `theory/soft-index-b.md` §M1, the latter adopted by `theory/verdicts/soft-index-adjudication-r1.md` §3.1 — specify a fixed-time insertion `Q[f_ε]ψ` on an already prepared hard vector, which is not a Haag--Ruelle creator family; (2M-1P) itself is proved on D6 for the HR family built from that charge acting on the vacuum (⟨1⟩8.⟨2⟩1), so what the adjudicated D29 fails is HR admissibility, not (2M-1P).  For the adjudicated datum the PROVED row S2-2body gives `Q_{k_s}\|k_h⟩−\|B^{in}⟩=(1−S_{12})\|P_{12}⟩=−2ik_s\|P_{12}⟩+O(k_s²)` (R8, R19) — relative size `√2·k_s(1+O(k_s))`, nonzero at the soft law's own linear order — and the identification of the D29 datum with the constructed `W_±^{(ε)}` channel is **OPEN**.  Statements (1) and (2) concern different families and are not composed.  **Two named steps are missing:** **(i)** prove at `O(k_s)`, with a displayed uniform remainder, that the `T→∞` D29 readout's connected packet-amputated on-shell pairing equals the constructed-channel one despite that mismatch; **(ii)** exhibit an `(ACE2M-SR)` instance for the fixed-time D29 family that `(SR)` constrains, including existence of its `N,t` limits.  The only datum for which the `(SR)` conditions have been verified is the one-element, exhaustion-free, infinite-chain **constructed-channel** family `A(ε)(h)=∫dμ_f(u)S_phys(εu,h)` on D6 (⟨1⟩9.⟨2⟩5), for which every uniformity clause of `(SR)` is trivially satisfied and which therefore backs no D29 claim; the `(W,σ)`-uniform form of `(SR)` is open on every model, D6 included.  `(ACE2M-SR)` is a hypothesis with no verified D29 instance.  No fixed-time charge/channel identification, no fixed-time charge/scattering-vector equality, and no D29 first-jet theorem is claimed. | SKETCH | AC-EX-2M, D3(a), D6--D8, D10(c), D12(a′), D24(b), D31, ML2, S2-2body | theory/ansatz-scattering-2m.md ⟨1⟩8--⟨1⟩9, excluding ⟨1⟩9.⟨2⟩4 (which belongs to AC-EX-2M) | No certificate exists for this row.  theory/checks/ansatz_scattering_2m_check.py tests none of (D29-den), HR admissibility, branch (i), the `N,t` limits, or `(ACE2M-SR)`, and is out of scope for this interface row |

### Conditions on the merge

1. Apply **both** rows above verbatim, replacing §7's lockstep mirror row and
   `claims/CLAIMS.md` l.782; keep the shard's §7 mirror byte-identical to the
   merged pair thereafter.
2. Execute **R5-O1's hoist** in the same repair pass, and then simplify the
   `where-proved` cell to "`theory/ansatz-scattering-2m.md ⟨1⟩2--⟨1⟩7′`".
   The merge is valid before the hoist — the cell names the step and the
   D29-freeness of its justification — but the shard should not stay in a
   state where an auditor must take my word for it.
3. Close R5-O2..O7 in the same pass; none of them requires new mathematics.

---

## 10. Summary and trajectory

- **FATAL 0** (0 in r1, r2, r3, r4, r5).
- **MAJOR 1** — R5-O1 (the nonvacuity certificate is filed under the D29
  ASSUME and outside the declared `where-proved`).
- **MINOR 6** — R5-O2 … R5-O7.
- **NOTE 12** — R5-N1 … R5-N12.

**Trajectory: 6 → 2 → 1 → 1 → 1 MAJOR, 0 FATAL throughout.  The count is FLAT
for the third consecutive round.  I will not dress that up.**  What has fallen
is the *kind*:

- r3's MAJOR indicted an interface clause, a theorem statement, a HONEST
  STATUS paragraph and a merge row at once.
- r4's MAJOR indicted a **leaf that consumed a theorem the same file declared
  inapplicable** — a soundness defect: a DAG clause with no honest backing.
- r5's MAJOR indicts **no mathematics at all.**  Every proposition involved is
  true and I re-derived it; the defect is that a correct step is filed in the
  wrong place and a proposed cell points at the wrong range.  This is the
  first round whose sole MAJOR is repaired by *moving text*, and the first
  round in which I promote.

Two further measurable facts.  Eighteen of nineteen dispositions verified by
fresh recomputation, nothing regressed, the lockstep is literally true to the
byte for the second round running, and `⟨1⟩2`--`⟨1⟩7` — the promoted material
— has not been edited since r3.  Against that: the fifth shipped instance of
the corpus's identically-zero-gate pattern (R5-O3), this time as the *fix* to
the NOTE that warned about it.  That pattern is now a reflex in this codebase
and deserves a standing pre-commit rule, not another verdict paragraph.

The row split is **MERGED** on my sentence, with the two cells in §9.
`AC-EX-2M-D29` **HOLDS at SKETCH** on branch (i) and the missing `(SR)`
instance.

**FAIL(R5-O1)**
