<!-- ROLE: downstream audit of the ML4-Ward (9) second-display erratum.
     bd tns-uxr (P0), requirement (3).  AUDIT ONLY — no shard is repaired
     here; every fix demand is addressed to the orchestrator.
     Auditor lane: this file only. -->

# Downstream audit — ML4-Ward (9) 2nd display / (18), `n≥2`

**Date:** 2026-08-28.  **bd:** `tns-uxr` (P0).  **Work order:**
`briefs/ml4-ward-n2-audit.md`.  **Predecessor findings:**
`theory/verdicts/soft-index-b-r1.md` F1 (the refutation),
`theory/verdicts/soft-index-adjudication-r1.md` §2.2 (adjudication),
`claims/CLAIMS.md` ML4-Ward row ERRATUM, `theory/ml4-ward-reduction.md`
⟨1⟩3 ERRATUM block.

**Method.** (i) Ran the certificate green and `--red` and reproduced its
numbers.  (ii) Two additional independent computations of my own (§1.2,
§1.3) reusing the certificate's operator construction verbatim.
(iii) Transitive walk of the `claims/CLAIMS.md` depends-on DAG.
(iv) Exhaustive `grep` of the whole repo on the equation numbers
(`ML4-Ward (9)`, `ML4 (9)`, `(18)`), the identity's shape (`J^-_0`,
`J^z_0`, `Q_0`, `P_{n,N}`, `P_{2,N}`, `N-2n`, `N−4`, `2M`, `m_λ`,
`ker S^+`, `D^†D`, `highest weight`), and the claim id, across
`theory/`, `theory/checks/`, `theory/verdicts/`, `claims/`,
`definitions.md`, `notation.md`, `docs/`, `briefs/`, `paper/`,
`numerics/`, `scripts/`, `README.md`, `HANDOFF.md`.

**Headline.** **44 sites** classified: **21 DAMAGED**, **2
DAMAGED-BUT-REPAIRABLE-BY-SUBSTITUTION**, **21 SAFE/CLEAN**, **0
UNCLEAR**.  No headline claim is reached; see §5.  One **new** finding
beyond the known ⟨1⟩5 damage: **the corrected form is
register-dependent**, and the repair currently prescribed by
`soft-index-adjudication-r1.md` §3.7 collapses back into the refuted
display under the `m_λ` register the same sentence prescribes (§1.2,
site D-2).  A second new finding: **(18) is false on the very vector
⟨1⟩5.⟨2⟩1.⟨3⟩3 singles out** — the ML2 singular contact vector `|χ_π⟩`
— by 100 % relative error at `N=8` (§1.3).

---

## 1. Computations I ran

### 1.1 The certificate, re-run and confirmed

`python3 theory/checks/ml4_ward_n2_check.py` — **exit 0**:

```
C1 OK: ||[S+,J-0]-2Jz0|| = 0.00e+00
n=1: ||S+psi||=5.6e-17  eq(9) err=1.234e-16  corrected err=1.291e-16  ||J+_0 psi||=0.000e+00  ||lhs||=4.177e-01
n=2: ||S+psi||=7.7e-16  eq(9) err=2.552e-01  corrected err=6.496e-16  ||J+_0 psi||=6.589e-01  ||lhs||=9.136e-01
n=3: ||S+psi||=2.1e-15  eq(9) err=1.107e+00  corrected err=2.375e-15  ||J+_0 psi||=1.356e+00  ||lhs||=1.387e+00
CONFIRMED: F1 pattern exact
```

`python3 theory/checks/ml4_ward_n2_check.py --red` — **exit 1**
("RED: eq(9) failure detected at n>=2 as required").

Numbers **match the work order exactly**: `0.2552 / 1.107` against lhs
norms `0.9136 / 1.387` at `n=2,3`, `N=8`; corrected form `≤2.4e-15`;
`n=1` exact at `1.2e-16`; the mechanism gauge `‖J^+_0ψ‖ = 0 / 0.66 /
1.36`.  Green exit 0, red exit 1.  **Certificate confirmed.**

### 1.2 NEW — the corrected form is register-dependent (named: **UXR-R1**)

The refuted display appears in the corpus in **two different projector
registers**, and they need **different** repairs.  I recomputed both,
reusing `ml4_ward_n2_check.build`/`sector_basis` verbatim, `N=8,10`,
random highest-weight `ψ`, `n=1,2,3`:

| register | definition | correct replacement | error of the *other* register's repair |
|---|---|---|---|
| **full-sector** (ML4 (2); `notation.md` `D_{n,N}`) | `D=Q_0\|_{ℋ_{n,N}}`, `A=D^†D` on the **whole** sector, `P_{n,N}=DA^{-1}D^†` | `P_{n,N}J^-_0 = 2D_{n,N}A_n^{-1}J^z_0` (**≤2.4e-15** at every `n`) | scalar+`Π_hw` form: **1.70e-01** at `n=2`, `N=8` |
| **hw-restricted** (`soft-index.md` ⟨1⟩1 `D_λ=Q_0\|_{K_λ}`) | `D_λ=Q_0\|_{ker S^+}`, `A_λ=D_λ^†D_λ=2m_λ·1`, `P_λ=D_λA_λ^{-1}D_λ^†` | `P_λJ^-_0 = (1/m_λ)\,Q_0\,Π_{hw}J^z_0` (**≤7.6e-16** at every `n`) | `2DA^{-1}J^z_0` form: **1.70e-01** at `n=2`, `N=8` |

Raw output (`N=8`; `err(scalar)` is the refuted display,
`err(2DA^-1Jz)` the ERRATUM's form, `err(scalar+Pi_hw)` the
hw-register form):

```
 n=2  M=2.0   ||Pi_hw Jz psi - Jz psi|| = 2.690e-01
   full-sector P:   ||lhs||=9.136e-01  err(scalar)=2.552e-01  err(2DA^-1Jz)=6.496e-16  err(scalar+Pi_hw)=1.701e-01
   hw-restricted P: ||lhs||=8.976e-01  err(scalar)=4.253e-01  err(2DA^-1Jz)=1.701e-01  err(scalar+Pi_hw)=7.643e-16
 n=3  M=1.0   ||Pi_hw Jz psi - Jz psi|| = 6.780e-01
   full-sector P:   ||lhs||=1.387e+00  err(scalar)=1.107e+00  err(2DA^-1Jz)=2.375e-15  err(scalar+Pi_hw)=5.536e-01
   hw-restricted P: ||lhs||=1.271e+00  err(scalar)=1.661e+00  err(2DA^-1Jz)=5.536e-01  err(scalar+Pi_hw)=2.511e-15
```

(`N=10` reproduces the same pattern: `1.408e-01` / `2.949e-01`
cross-errors, both correct forms `≤1.7e-15`.)  At `n=1` all three
candidate forms agree to `≤2.7e-16` and the two projectors agree on
`J^-_0ψ`.

**Why this matters, and the trap.**  In the hw-restricted register
`A_λ = 2m_λ·1`, so the string "`2D A^{-1}J^z_0`" *evaluates to*
`(1/m_λ)Q_0J^z_0` — i.e. **exactly the refuted display**.  The ERRATUM's
corrected form is only correct when `D` is the **full-sector** map and
`A_n=D^†D` on all of `ℋ_{n,N}` (where `A_n` is genuinely non-scalar).
Any repair text that writes "`2D(D^†D)^{-1}J^z_0`" **must** say so.
`soft-index-adjudication-r1.md` §3.7 currently instructs the r2 shard to
state the identity "over `m_λ`, with the corrected `2D A⁻¹J^z₀` form" —
those two halves are inconsistent (site D-2 below).

Equivalently and register-freely: the honest statement is
**`P J^-_0 ψ = 2 D A^{-1} J^z_0 ψ` with `A=D^†D` on the *domain of `D`
being projected onto*, and the scalar `(2m)^{-1}` may be pulled out only
when `J^z_0ψ` lies in that domain's `ker S^+`** — which is exactly the
condition `‖Π_{hw}J^z_0ψ − J^z_0ψ‖ = 0`, measured above as
`0 / 0.269 / 0.678` at `n=1/2/3`.

### 1.3 NEW — (18) is false on the ML2 singular vector itself (named: **UXR-R2**)

`theory/ml4-ward-reduction.md` ⟨1⟩5.⟨2⟩1.⟨3⟩3 argues that the ML2
singular contact vector is highest weight and therefore "belongs to the
(18) branch".  The premise is true; the conclusion is false.  With
`|χ_π⟩ ∝ Σ_x (−1)^x |x,x+1⟩` built explicitly and `n=2`:

```
N=8 : ||S+ chi||=0.0e+00   ||J+_0 chi||=2.000   ||S+ Jz chi||=2.000
      ||lhs||=7.746e-01  ||rhs(18)||=1.4142  eq(18) err=7.746e-01  (rel 1.000)   corrected err=2.35e-16
N=10: ||lhs||=6.901e-01  ||rhs(18)||=1.0541  eq(18) err=5.040e-01  (rel 0.730)   corrected err=1.79e-16
```

So (18) is wrong by **100 % of the left-hand side** at `N=8` on the one
vector the shard names, and the full-sector corrected form is exact there
(`2.4e-16`).  The two-hard damage is not hypothetical or generic-vector:
it hits the named leaf.

### 1.4 Negative certificates (what I verified is FINE)

Same construction, `N=8,10`, `n=1,2,3`, random **general** (not
highest-weight) sector vectors:

- **(10)** `P_{n,N}J^-_0 = D_{n,N}A_n^{-1}(2J^z_0+J^-_0S^+)` — error
  `≤7.3e-16` at every `n`, on non-highest-weight inputs.  **EXACT.**
- **(9) first display** `D_{n,N}^†D_{n,N} = (N−2n)1` on `ker S^+` —
  error `≤3.6e-14` at every `n`.  **EXACT.**
- **(8)** `D^†J^-_0 = 2J^z_0 + J^-_0S^+` — implied by C1 of the
  certificate (`0.00e+00`).  **EXACT.**
- **(11)/(R15)** — `n=1`, untouched (`1.2e-16`).  **EXACT.**

---

## 2. Site table

Verdict key: **DAMAGED** = `n≥2` or unrestricted-`n` use of the refuted
display; **D-SUB** = damaged but the corrected form substitutes and the
downstream conclusion survives; **SAFE** = `n=1` only, or does not
consume (9)/(18) at all; **RECORD** = historical verdict/adjudication
text that asserts the refuted scope (annotate, do not rewrite).

### 2.1 `theory/ml4-ward-reduction.md` — the primary shard

| # | address | line | `n` in play | verdict | note / fix demand |
|---|---|---|---|---|---|
| A-1 | header "Status:" | 3–4 | all | **DAMAGED** | "(8)--(11) are PROVED" unqualified, 158 lines above the ERRATUM. **Fix:** "(8), (10), (11) and the norm identity in (9) are PROVED; the second display of (9) is scoped to `n=1` — see the ERRATUM at ⟨1⟩3." |
| A-2 | (9) 1st display `D^†D=(N−2n)1` | 189 | all | **SAFE** | verified exact all `n` (§1.4). |
| A-3 | **(9) 2nd display** | 191 | `n<N/2` | **DAMAGED** | the defect. **Fix:** `P_{n,N}J^-_0 = 2D_{n,N}A_n^{-1}J^z_0`, with `A_n=D^†D` on the **whole** sector said out loud (§1.2). **Surviving weaker statement:** the display is exact on `ker S^+ ∩ ℋ_{1,N}` (every one-magnon packet away from `h=0`, error `1.2e-16`). |
| A-4 | (10) | 196–199 | all | **SAFE** | verified exact on general vectors (§1.4). |
| A-5 | ⟨1⟩3.⟨2⟩1.⟨3⟩3 | 209–211 | all | **SAFE** | the `2S^z=(N−2n)` step is right; the error is downstream of it. |
| A-6 | ⟨1⟩3.⟨2⟩1.**⟨3⟩4** | 213–215 | all | **DAMAGED** | the defective leaf: "insert ⟨3⟩2--⟨3⟩3 in definition (2) to obtain (9)". **Fix:** the leaf proves (10); (9)'s scalar form needs the extra hypothesis `J^z_0ψ∈ker S^+`, true iff `n=1` (by momentum conservation). |
| A-7 | ⟨1⟩3.⟨2⟩2, (11), ⟨3⟩1–⟨3⟩4 | 219–239 | **1** | **SAFE** | "Put `n=1` and ⟨3⟩1 into (9)". Untouched. |
| A-8 | ⟨1⟩4 (all of it), (12)–(17), ML4-Q1 | 243–412 | **1** | **SAFE** | `P_{1,N}` throughout; `r_N(h)=(1−P_{1,N})J^-_0|h⟩_N`. |
| A-9 | ⟨1⟩5.⟨2⟩1 + **(18)** | 416–424 | **2** | **DAMAGED** | `P_{2,N}J^-_0=2Q_0J^z_0/(N−4)` is the `n=2` instance of the refuted display; refuted at `N=8` by `0.2552` vs lhs `0.9136`. **Fix:** delete (18); the exact two-hard statement is (10), or `2D_{2,N}A_2^{-1}J^z_0` on `ker S^+`. **Surviving weaker statement:** *every* finite-ring hard state in `ℋ_{2,N}` has an exact descendant projection given by (10) — the sentence immediately before (18) is true and is all that ⟨1⟩5 needs. |
| A-10 | ⟨1⟩5.⟨2⟩1.**⟨3⟩2** | 430–432 | **2** | **DAMAGED** | "Put `n=2` in (9) on `ker S^+`" — the work order's known starting point, **confirmed**. **Fix:** "use (10) on all of `ℋ_{2,N}`; on `ker S^+` its `J^-_0S^+` term drops but `A_2^{-1}` stays an operator inverse." |
| A-11 | ⟨1⟩5.⟨2⟩1.**⟨3⟩3** | 434–437 | **2** | **DAMAGED** | "It therefore belongs to the (18) branch" — **newly refuted on that exact vector**, rel. error `1.000` at `N=8` (§1.3). **Fix:** the ML2 singular vector *is* highest weight (that half is verified: `‖S^+χ_π‖=0`), but highest weight no longer buys the scalar form; it too needs `A_2^{-1}`. **Surviving weaker statement:** `S^+|χ_π⟩=0`, so the `J^-_0S^+` term of (10) drops on it — nothing more. |
| A-12 | ⟨1⟩5 EXPLORATION ML4-3 | 442–454 | 2→3 | **SAFE** | statement of an obstruction; consumes neither (9) nor (18). |
| A-13 | ⟨1⟩5.⟨2⟩2 conditional two-hard | 456–471 | **2** | **SAFE** | uses `Γ_3(0)=Q_0(D_{2,N}^†D_{2,N})^{-1/2}` (polar, operator-valued) + ML4-A + (2). Never touches (9)/(18). **This is the only load-bearing two-hard conclusion in the shard and it survives intact.** |
| A-14 | ⟨1⟩6 numerical certificate | 477–496 | **1** | **SAFE** | `ml4_check.py` is one-magnon (§2.6). |
| A-15 | ⟨1⟩7 verdict item **1** | 503–505 | **2** | **DAMAGED** | "…including arbitrary one-hard packets **and all finite-ring ML2 two-hard states**". **Fix:** "…arbitrary one-hard packets; for `n≥2` the exact projection is (10)/`2DA^{-1}J^z_0`, not the scalar form." |
| A-16 | ⟨1⟩7 items 2–5 | 506–521 | — | **SAFE** | ML4-A, the off-shell interpolation HOLD, and the two open conjectures are unaffected. |

### 2.2 Corpus single-source files (L4)

| # | address | line | `n` | verdict | note |
|---|---|---|---|---|---|
| B-1 | `notation.md` `J^z_0, S^±` row | 255 | all | **DAMAGED** | carries the refuted display verbatim as the *symbol-table definition of what `J^z_0` is for*. **Fix:** replace with `P_{n,N}J^-_0 = 2D_{n,N}A_n^{-1}J^z_0` on `ker S^+`, or scope to `n=1`. This is the highest-leverage single edit: L4 says shards cite here and never redefine. |
| B-2 | `notation.md` `D_{n,N},P_{n,N},R_{n,N}` row | 252 | — | **SAFE** | correct definitions; **and it is these definitions that fix the full-sector register** of §1.2. Worth citing in the repair. |
| B-3 | `theory/TRIANGLE.md` §2.5 | 282–284 | `n<N/2` | **DAMAGED** | second half of the sentence is the refuted display; `D^†D=(N−2n)𝟙` and the `n=1` consequence in the same paragraph are SAFE. |
| B-4 | `theory/TRIANGLE.md` §2.4 ML4 row, §6.1 | 268, 519–521 | 2 | **SAFE** | already say the two-hard/three-body statement is future work. |
| B-5 | `definitions.md` (whole file) | — | — | **CLEAN** | no consumer. D24(d)2 "Ward covariance" states the residue `2iv_hM_1^O(h)` as an **assumed hypothesis** at one hard leg; it never invokes (9). No edit needed for *this* defect (D24(d)3 has its own separate problem, `tns-iu5`, out of scope). |
| B-6 | `claims/CLAIMS.md` ML4-Ward row | 38 | — | **CLEAN** | already scoped with the ERRATUM. One wording nit: it writes the correction as `2D_{n,N}A_n^{-1}J^z_0` without saying `A_n` is the full-sector `D^†D`; §1.2 shows that omission is exploitable. |
| B-7 | `claims/CLAIMS.md` ML4 row | 36 | 1 | **SAFE, pointer needs scoping** | the row's *statement* is one-hard only, so its SKETCH status survives; but its "proved in" cell points at `⟨1⟩4--⟨1⟩5`, and `⟨1⟩5`'s ⟨2⟩1 is damaged. **Fix:** narrow to `⟨1⟩4` + `⟨1⟩5.⟨2⟩2`. |

### 2.3 `theory/soft-index.md` (S1 lane A, self-status SKETCH, r1 FAIL)

| # | address | line | `n` | verdict | note / fix demand |
|---|---|---|---|---|---|
| C-1 | §0 (S-IDX.0-fin) (SIDX.3) + gloss | 44–54 | general `m_λ`; explicit `n` | **DAMAGED** | states `P_λJ^-_0=(1/m_λ)Q_0J^z_0` "in every finite highest-weight hard sector", then "For D6 this is `P_{n,N}J^-_0=2Q_0J^z_0/(N−2n)`". **Fix (hw register, §1.2):** `P_λJ^-_0=(1/m_λ)Q_0Π_{hw}J^z_0`; the `Π_{hw}` is the identity iff `n=1`. **Surviving weaker statement:** exact for one hard magnon / one-magnon packet, every `S`, `ρ` free (independently verified by the S1-A critic at `S∈{1/2,1,3/2}` with `m_λ=NS−1`). |
| C-2 | ⟨1⟩1 ASSUME | 86–90 | general | **DAMAGED** (quantifier) | `K_λ⊂ker S^+`, `S^z=m_λ`, no `n=1` restriction. |
| C-3 | ⟨1⟩1.⟨2⟩1 | 93–98 | all | **SAFE** | norm identity `D_λ^†D_λ=2m_λ`. (Citation nit: calls it "ML4-Ward (9)" — it is (9)'s **first** display; worth disambiguating.) |
| C-4 | ⟨1⟩1.⟨2⟩2 | 99–102 | all | **SAFE** | equation (8). |
| C-5 | ⟨1⟩1.**⟨2⟩3** | 104–108 | all | **DAMAGED** | "substitution of ⟨2⟩1--⟨2⟩2 gives (SIDX.3)" — the same defective leaf as A-6, in the hw-restricted register. |
| C-6 | ⟨1⟩2.⟨2⟩1 **(SIDX.6)** | 118–125 | general `n` | **DAMAGED** | the refuted display verbatim, justified by "ML4-Ward (9), including `n<N/2`". |
| C-7 | ⟨1⟩2.⟨2⟩2 (SIDX.7)–(SIDX.8) | 127–142 | **1** | **SAFE** | cites (11)/(R15). |
| C-8 | ⟨1⟩2.⟨2⟩3–⟨2⟩4 (SIDX.9)–(SIDX.10) | 143–176 | **1** | **SAFE** | the `ℓ_λ` datum is D29-*defined*, not derived from (9); its primitive-magnon reduction is (SIDX.8), `n=1`. (Its own separate defect — the `2ρ` stipulation — is S1-A F1, out of scope.) |
| C-9 | ⟨1⟩3 | 180–200 | **1** | **SAFE** | ASSUME is literally "D6 and one hard magnon". |
| C-10 | ⟨1⟩4, ⟨1⟩5, ⟨1⟩7, ⟨1⟩8, ⟨1⟩9 | 206–398 | — | **SAFE** | ML4-A-style limit algebra, source bridge, anchors. No (9) consumption; ⟨1⟩5.⟨2⟩1 rides on (SIDX.8)/(SIDX.10), i.e. `n=1`. |
| C-11 | ⟨1⟩6.⟨2⟩1 vacuity fence | 310–316 | **every `n<N/2`** | **DAMAGED** | "(S-IDX.0) has instances on every D6 ring with `N>3`, **every `n<N/2`**, and every highest-weight packet". **Fix:** restrict to `n=1`, or restate over the corrected form. **Surviving weaker statement:** with the corrected form, nonvacuity at every `n<N/2` is restored — the corrected identity has the same instance set. |
| C-12 | ⟨1⟩10 CHECKER SPEC item 1 | 414–423 | **`n∈{1,2}`** | **DAMAGED (spec)** | demands "operator residuals below `1e-12` for (SIDX.6)" at `n∈{1,2}`. A checker built to this spec **must exit nonzero at `n=2`** (measured residual `2.55e-01`). **Fix:** either target the corrected form, or keep `n=2` and *invert* the expectation — the latter would fold `ml4_ward_n2_check.py` into the S1 checker as a standing red test. Note the mutation "`N−2n → N`" prescribed on line 422 is a *weaker* red than reality. |
| C-13 | §7.1 D29(4) merge text | 455–460 | — | **SAFE** | `P_λ=D_λ(D_λ^†D_λ)^{-1}D_λ^†` — the operator-inverse form, no scalar. Correct as written. |
| C-14 | §7.2 proposed row `S-INDEX-fin` | 464 | general `m` | **DAMAGED** (proposed, **unmerged**) | "`PJ^-_0=Q_0J^z_0/m`". Not in `claims/CLAIMS.md`; the adjudication merged nothing. Blocks the r2 merge until corrected. |
| C-15 | §8 HONEST STATUS 1 | 476–478 | general | **DAMAGED** | "(SIDX.3) and the `N-2n → N-2 → 2ρ` cancellation are unconditional". (SIDX.3) is not unconditional; it is `n=1`. |

### 2.4 `theory/soft-index-b.md` (S1 lane B, self-status SKETCH, r1 FAIL)

| # | address | line | `n` | verdict | note / fix demand |
|---|---|---|---|---|---|
| E-1 | §0 THEOREM (S-IDX.0) bullet | 78–88 | **every finite sector** | **DAMAGED** | "In every finite sector `ℋ_{n,N}` with `M:=ρN−n\|q\|>0`, for every hard packet `ψ∈ker S^+` … `P_{n,N}J^-_0ψ=(2/(2M))Q_0J^z_0ψ`". This is the theorem's headline unconditional rung. |
| E-2 | ⟨1⟩2 ASSUME | 315–326 | "every `n` with `M>0`, every packet" | **DAMAGED** (quantifier) | the "for all `n`" hiding in the preamble. |
| E-3 | ⟨1⟩2.⟨2⟩1 (vector Ward commutator) | 328–340 | all | **SAFE** | `[S^+,J^-_0]=2J^z_0` in the abstract D10(a) register; certificate C1 gives `0.00e+00`. |
| E-4 | **(B4)** 1st display `D^†D=2M·1` | 344 | all | **SAFE** | verified exact all `n` (§1.4). |
| E-5 | **(B4)** 2nd display | 345–347 | all | **DAMAGED** | `P_{n,N}J^-_0=(1/M)Q_0J^z_0` on `ℋ^{hw}_{n,N}` — the S1-B critic's F1 target. Register note: the shard uses ML4's `D_{n,N}` symbol (full-sector, per `notation.md`) but the hw-restricted proof; both readings fail, with **different** repairs (§1.2). The orchestrator must pick one register explicitly. |
| E-6 | ⟨1⟩2.⟨2⟩2.⟨3⟩1 | 358–362 | all | **SAFE** | `‖Q_0ψ‖²=2M‖ψ‖²`. |
| E-7 | ⟨1⟩2.⟨2⟩2.**⟨3⟩2** | 364–368 | all | **DAMAGED** | "inserting into the projection `P=D(D^†D)^{-1}D^†` with ⟨3⟩1 gives (B4)" — the defective leaf, third instance. |
| E-8 | ⟨1⟩2.⟨2⟩3 **(B5)** + ⟨3⟩1–⟨3⟩3 | 370–412 | **1** | **SAFE** | "Insert `n=1` in (B4)". `⟨h\|J^z_0\|h⟩=iv(h)` derived independently from G0(e), not from (9). |
| E-9 | ⟨1⟩2.⟨2⟩4 (B6)–(B7) | 413–466 | — | **SAFE w.r.t. this defect** | the `k=0` fiber / Duhamel separation consumes neither (9) nor (B4). (It carries its own independent defect, S1-B critic F2 — out of scope here.) |
| E-10 | ⟨1⟩3, ⟨1⟩4 | 472–732 | **1** | **SAFE** | admissible index set, ML4-Q1 immunity, spin-`S` anchor. No (B4) at `n≥2`. |
| E-11 | ⟨1⟩5 ASSUME | 745 | general | **D-SUB** | imports "the finite-volume identities (B4)--(B9)" wholesale. Only the `n=1` content is used downstream (E-13). **Fix:** cite (B5) + the corrected (B4). **Conclusion survives; no constant changes.** |
| E-12 | ⟨1⟩5.⟨2⟩1 clause (2) | 769–771 | "every sector" | **D-SUB** | "the descendant current residue … factorizes as `2i v(h)M_1(h)` — this is (B4)--(B5), PROVED in ⟨1⟩2 for every `N`, **every sector**, `ρ` free". The residue actually used is the one-hard `2iv_h`, i.e. (B5). **Fix:** delete "every sector". **Conclusion survives; no constant changes.** |
| E-13 | ⟨1⟩5.⟨2⟩2 **(B14)** + ⟨3⟩1 | 788–838 | **1** | **SAFE** | the jet bookkeeping consumes `2iv_h` (one-hard, from (B5)), the leg norm `2ρN`, the flux `L(0,h)`, and `e^{ik}−1`. `n=1` throughout. **The lane's headline jet is NOT reached by this defect.** (It is separately attacked by S1-B critic M4 and the `ρ`-derivation cross-finding — out of scope.) |
| E-14 | ⟨1⟩5.⟨2⟩3, ⟨1⟩6, ⟨1⟩7 | 840–962 | 1 | **SAFE** | ML4-A on the limit family; ML5-A bridge; anchors. |
| E-15 | ⟨1⟩8.6 landmine audit | 1000–1002 | general | **DAMAGED** (citation) | "`ρ` enters only through the sector weight `M=ρN−n` ((B4))" — cites (B4) at general `n` as settled. |
| E-16 | CHECKER SPEC SIB-C0…C3 | 1038–1073 | 1 | **SAFE / CLEAN** | none of the four proposed checkers tests (B4) at `n≥2`. SIB-C3 tests the leg norm and the one-hard residue. **Negative result: the lane-B checker spec would not have caught F1 — an independent reason to fold `ml4_ward_n2_check.py` into the r2 spec.** |
| E-17 | §M3 proposed row `S-IDX-fin-B` | 1144 | general | **DAMAGED** (proposed, **unmerged**) | "on `ker S^+` with `M=ρN−n>0`, `D†D=2M` and `P_{n,N}J^-_0=Q_0J^z_0/M`". Blocks the r2 merge until corrected. |
| E-18 | §M4 proposed `notation.md` row for `M` | 1152 | — | **SAFE** | defines the sector weight only. |
| E-19 | HONEST STATUS bullet 1 | 1161–1166 | general | **DAMAGED** | "(S-IDX.0): the finite-volume soft-index identity (B4)--(B7) … These steps are unconditional finite-volume algebra; **I believe they are airtight** and they are the lane's rung-0 deliverable." |

### 2.5 Verdicts and adjudications (the record)

| # | address | line | verdict | note |
|---|---|---|---|---|
| D-1 | `soft-index-b-r1.md` F1 + "NOTE for the orchestrator" | 57–105 | **SAFE / authoritative** | the refutation. Its NOTE already names both (9) and (18) as inheriting. Its proposed fix at L86 (`P_{n,N}J^-_0=2D_{n,N}(D^†D)^{-1}J^z_0`) is the **full-sector** form and is correct in that register — §1.2 confirms — but the same paragraph immediately re-uses the hw language, so the register caveat applies. |
| D-2 | `soft-index-adjudication-r1.md` §2.2 and §3.7 | 31–35, 94–97 | **DAMAGED (register)** | §3.7: "the r2 unified shard states it once, **over `m_λ`**, with the corrected **`2D A⁻¹J^z₀`** form". Per §1.2 these two halves are mutually inconsistent: in the `m_λ` register `A=2m_λ·1` and `2DA^{-1}J^z_0` **is** the refuted display. **Fix demand (highest priority for the r2 brief):** state either (i) full-sector register + `2D_{n,N}A_n^{-1}J^z_0`, or (ii) hw register + `(1/m_λ)Q_0Π_{hw}J^z_0`. Do not mix. |
| D-3 | `soft-index-r1.md` (C-d) | 29–37 | **DAMAGED (over-broad clearance)** | the S1-A critic verified `‖PJ^-_0 − Q_0J^z_0/m_λ‖ ≤ 1.2e−15` **only at `m_λ=NS−1`, i.e. `n=1`**, then concluded "**(S-IDX.0)'s algebra is correct and does generalise as the shard says**". The verification is sound; the generalisation is not. |
| D-4 | `soft-index-r1.md` §5 preamble | 493–495 | **DAMAGED (over-broad clearance)** | "A and B agree on the finite-volume index identity (A: `PJ^-_0=Q_0J^z_0/m_λ`; B: … ) — **the same statement, both correct, both verified by me**." Directly contradicted by S1-B's F1 and by §1.1 here. **Fix:** an ERRATUM stanza in this verdict, otherwise a future session will cite it as a clearance. |
| D-5 | `soft-index-r1.md` M6(d) surviving-weaker-statement | 328–331 | **DAMAGED (over-broad)** | lists `P_λJ^-_0=Q_0J^z_0/m_λ` among four things "unconditional … all four independently verified here". Three of the four are; this one is `n=1` only. |
| D-6 | `soft-index-r1.md` M7 | 336–340 | **SAFE** | says item 1 of the S1-A checker spec is redundant because it is "already PROVED (ML4-Ward) and already covered by `ml4_check.py`". Both halves are now false at `n=2` — but the objection's *conclusion* (the spec certifies nothing novel) stands. Annotate only. |
| D-7 | `corpus-r2.md` promotion table | 506 | **RECORD** | "exact finite-sector Ward projection (8)--(11) — **PROMOTE to PROVED** … Direct SU(2) commutator and polar/projection algebra". The promotion that missed it. **Annotate in place; do not rewrite a frozen adjudication.** |
| D-8 | `corpus-r3.md` faithfulness table | 195 | **RECORD** | "ML4-Ward — FAITHFUL — the split is exactly finite-sector projection (8)--(11)". |
| D-9 | `corpus-r4.md` PROVED roster | 78 | **RECORD** | lists ML4-Ward unqualified. |
| D-10 | `repair-r2-response.md` | 35 | **RECORD** | "ML4-Ward — PROVED — New DAG split for exact finite-sector projection (8)--(11)". |
| D-11 | `mquant-ml45-r1.md` (whole) | — | **SAFE / CLEAN** | attacks ML4's uniform constant and (11)'s interpretation; never uses (9) at `n≥2`. |
| D-12 | `ansatz-scattering-2m-r2.md` | 135 | **SAFE** | cites `ML4-Ward`'s `J^-_0` only as an example of a fixed-time insertion. |

### 2.6 Code — all CLEAN

| # | file | verdict | evidence |
|---|---|---|---|
| F-1 | `theory/checks/ml4_check.py` | **CLEAN** | the projection test at L220 is `expected_projection = 2j*velocity*descendant/(n_sites - 2)` — literally `N−2`, i.e. `n=1`. The hard state is `one_magnon(...)`; `descendant = charge @ hard_state`. No `n≥2` path exists. Its recorded residuals `8.899e-16` / `3.473e-15` certify (11), not (9) at `n≥2`. |
| F-2 | `theory/checks/soft_index_probe.py` | **CLEAN** | L434–452: `descendant = q0 @ hard_vec` with `hard_vec` one-magnon; the projection is formed **numerically** as a rank-1 Gram projection, never via the scalar. `n=1`. |
| F-3 | `theory/checks/*.py` (all others) | **CLEAN** | no Ward-projection use: `corner_a`, `mquant*`, `memory_index*`, `ml2_completeness`, `oracle_bethe`, `soft_current_recon`, `spin_s_slope`, `spt_rebuild`, `ansatz_scattering`, `crosscheck_corner_b_tk`. |
| F-4 | `numerics/` (all Julia + results) | **CLEAN** | zero hits for `Ward`, `J^z`, `N-2n`. The memory-effect numerics are structurally disjoint from ML4. |
| F-5 | `theory/checks/ml4_ward_n2_check.py` | **CLEAN / authoritative** | green exit 0, `--red` exit 1, reproduced (§1.1). |

### 2.7 Paper — CLEAN

| # | address | verdict | evidence |
|---|---|---|---|
| G-1 | `paper/main.tex:508` | **SAFE (one-word scope)** | a ground-truth pointer list, "rows ML4-A, ML4-Ward, ML5-A/B PROVED as conditional implications". No display of (9) or (18) anywhere in `main.tex` or `supplement.tex`. Suggest "(ML4-Ward scoped to `n=1` for the projection display)". |
| G-2 | `paper/main.tex:251` | **CLEAN — actively protective** | the Letter already lists "**two or more hard legs**" among what is open. Cross-checked against `paper/v2-claim-audit.md:114`. |
| G-3 | `paper/supplement.tex` | **CLEAN** | zero hits on ML4/Ward-projection patterns. |

### 2.8 Briefs — the forward-injection point

| # | address | line | verdict | note |
|---|---|---|---|---|
| H-1 | `briefs/soft-index-target.md` | 118–127 | **DAMAGED — ROOT CAUSE** | the campaign target brief *instructs* provers: "(S-IDX.0) … In every finite sector, for every hard packet in `ker S^+` … the Ward projection (ML4-Ward (9)--(11)) **pins `P_{n,N}J^-_0 = 2Q_0J^z_0/(N−2n)`** — … valid for every `N`, **every `n<N/2`**, every packet." **Both S1 lanes executed this faithfully.** Until this is corrected the r2 unified shard will reproduce the defect a third time. **Highest-priority non-corpus fix.** |
| H-2 | `briefs/soft-index-target.md` | 53–55 | **DAMAGED** | lists "ML4-Ward … equations (8)--(11)" among identities "you may take as PROVED without reproving". |
| H-3 | `briefs/soft-index-target.md` | 198–200 | **DAMAGED (mild)** | "S-IDX-fin only (finite-volume index identity — **nearly free given ML4-Ward**)". It was not free; it was wrong at `n≥2`. |
| H-4 | `briefs/s1-codex-prover.md:19`, `briefs/s1-fable-prover.md:19` | — | **DAMAGED (advisory)** | read-lists citing "ML4-Ward (8)--(11)" unscoped. Spent briefs; scope them if reused for r2. |
| H-5 | `briefs/s2-repair-r2.md:84`, `briefs/ace-ld-prover.md:119`, `briefs/lr-d16-prover.md:120`, `briefs/critic-protocol.md:41` | — | **SAFE** | all four already carry the ERRATUM and the corrected form. Add the §1.2 register clause when next touched. |

### 2.9 Narrative files — CLEAN

`README.md:83,124`, `HANDOFF.md:34,49`, `docs/assets/adversarial-loop-{light,dark}.svg:66`,
`docs/assets/make_readme_diagrams.py:285` — all **describe** the erratum
correctly and post-date it.  `docs/framing.md`, `docs/novelty-sweep.md`,
`docs/continuum-antecedents.md`, `docs/report-memory-index/*`,
`docs/prose-guide.md` — **zero hits**.  `scripts/prompts/ml4-ml5.md` —
the original generating prompt; historical, no fix.

---

## 3. DAG section

Transitive walk of the `depends on` column, then the prose citations that
carry no DAG edge (the latter found only by grep, as the work order
warned).

### 3.1 Rows that reach ML4-Ward through the DAG

| row | status | path | survives? | deciding step |
|---|---|---|---|---|
| **ML4-Ward** | PROVED | — | **survives as-is; already scoped** | `theory/ml4-ward-reduction.md` ⟨1⟩3 ERRATUM + the row's own ERRATUM. Everything it now asserts — (8), the `(N−2n)` norm identity, (10), (11)/(R15) — is verified exact at every `n` (§1.4). **No demotion.** One wording fix: name `A_n` as the full-sector `D^†D` (§1.2). |
| **ML4** | SKETCH | `ML4 → ML4-Ward` | **survives; needs pointer scoping** | the row's *statement* is one-hard-magnon `(15)--(17)`, entirely `n=1`. Its "proved in" cell reaches `⟨1⟩5`, whose ⟨2⟩1 is damaged (A-9/A-10/A-11); its ⟨2⟩2 (the only two-hard *conclusion*) is SAFE (A-13). **Fix:** narrow the cell to `⟨1⟩4` + `⟨1⟩5.⟨2⟩2`; leave the status at SKETCH. |
| **S-general** | CONJECTURE | `S-general → ML4 → ML4-Ward` | **survives as-is** | the row already names "**ML4 at `n≥2`**" among its live obligations. The erratum makes that obligation *sharper*, not newly true. No status change. |

**That is the whole DAG-transitive set.**  No other row lists ML4-Ward,
ML4, or S-general in its `depends on`.

### 3.2 Rows that reach it only through prose (no DAG edge)

| row | status | prose edge | survives? | deciding step |
|---|---|---|---|---|
| **ML5-B** | PROVED (conditional) | `ml5-universality.md:12` "uses ML4-A and the **FM Ward residue (11)**"; `⟨1⟩3.⟨2⟩1.⟨3⟩1` justification "hypothesis 2 and **ML4 equation (11)**" | **survives as-is** | (11) is the `n=1` consequence, untouched. Its ⟨2⟩1 display (6) carries the one-hard residue `2iv_hM_1^O(h)`. `ml5-universality.md:201` explicitly says "For two hard magnons one additionally needs ML4-3". **No scoping needed.** |
| **ML5-A**, **ML5** | PROVED / REFUTED | via D24(c)/(e) | **survives** | no Ward-projection content. |
| **S2-2body**, **S2-2body-S**, **OR1**, **OR2**, **Bc** | PROVED / CONJECTURE | `soft-current-recon.md` (R14)/(R15), one hard magnon | **survive** | (R15) `= P_{D_h}J^-_0\|k_h⟩_N = (2iv_h/(N−2))Q_0\|k_h⟩_N` is `n=1`; `⟨3⟩3` divides by `⟨D_h\|D_h⟩=N−2`. Verified `1.2e-16`. |
| **M-quant**, **M-quant-G**, **M-INDEX-\***, **AC-EX**, **AD3-ex**, **B3**, **M-flux**, **SPT-\*** | various | none | **survive** | the memory/Corner-B/SPT half of the corpus never touches the Ward projection. Zero grep hits. |

### 3.3 Proposed-but-unmerged rows (blockers for the r2 merge)

None of these is in `claims/CLAIMS.md`; the adjudication merged nothing.
All four **must be corrected before merge**:

- `soft-index.md` §7.2 **`S-INDEX-fin`** — "`PJ^-_0=Q_0J^z_0/m`" — **DAMAGED**.
- `soft-index-b.md` §M3 **`S-IDX-fin-B`** — "`P_{n,N}J^-_0=Q_0J^z_0/M`" — **DAMAGED**.
- `soft-index.md` §7.2 `S-INDEX-spec` / `S-INDEX-source`,
  `soft-index-b.md` §M3 `S-IDX-spec-B` / `S-IDX-desc-B` / `S-IDX-src-B` —
  **SAFE w.r.t. this defect** (they consume the `n=1` residue only), though
  `S-IDX-desc-B` depends on `S-IDX-fin-B` and inherits its wording.

---

## 4. What I checked and found CLEAN (negative results)

Recorded so the next session does not re-audit them.

1. **`theory/checks/ml4_check.py` is `n=1` everywhere.** The descendant
   projection test hard-codes `/(n_sites - 2)` on a one-magnon state.
   Its green run certifies (11); it neither tests nor could have caught
   (9) at `n≥2`. No mutation needed.
2. **`theory/checks/soft_index_probe.py` never uses the closed form.**
   It builds the rank-1 descendant projection numerically at `n=1`.
   The frozen probe results are unaffected by the erratum.
3. **All other `theory/checks/*.py` and the whole of `numerics/`**: zero
   Ward-projection content.
4. **`definitions.md`**: no consumer. D24(d)2 states the Ward-covariance
   *hypothesis* at one hard leg; it does not import (9).
5. **`paper/main.tex` and `paper/supplement.tex`**: no display of (9) or
   (18), and `main.tex:251` already lists "two or more hard legs" as
   open. **The Letter is not exposed.**
6. **ML5-B / ML5-A** cite (11) only. **Not damaged.**
7. **`soft-current-recon.md` (R1)–(R19)**: (R14)/(R15) are one-magnon.
   **Not damaged.**
8. **`ml4-ward-reduction.md` ⟨1⟩1, ⟨1⟩2 (ML4-A), ⟨1⟩4 (the whole
   off-shell interpolation branch, (12)–(17), ML4-Q1), ⟨1⟩5.⟨2⟩2, ⟨1⟩6**:
   all `n=1` or projector-free. **Not damaged.**
9. **(8), (10), (11), and the first display of (9)**: independently
   re-verified exact at `n=1,2,3`, `N=8,10`, on general and on
   highest-weight vectors (§1.4). The corrected-form claim in the
   `CLAIMS.md` ERRATUM is sound in the full-sector register.
10. **The memory/Corner-B/SPT half of the corpus** (M-quant, M-quant-G,
    M-INDEX-\*, AC-EX, B3, SPT-\*, K1–K4, Mq-\*): structurally disjoint,
    zero grep hits on every pattern searched.
11. **`soft-index-b.md` CHECKER SPEC (SIB-C0…C3)**: none tests (B4) at
    `n≥2`. Clean, but also **would not have caught F1** — noted as a spec
    gap, not a defect.
12. **`docs/`, `README.md`, `HANDOFF.md`, the README SVGs**: all
    post-erratum and accurate.
13. **No UNCLEAR sites.** Every hit resolved to a definite `n` by
    reading the surrounding ASSUME/quantifier, or by computation.

---

## 5. Blast-radius verdict

**The damage is contained, but it is wider than "the two-hard-magnon
Ward part", and it does not reach a headline claim.**  The refuted
display is *load-bearing for a conclusion* in exactly one place in the
proved corpus — `ml4-ward-reduction.md` ⟨1⟩5.⟨2⟩1, where (18) and its
leaves ⟨3⟩2/⟨3⟩3 are the entire "exact two-hard Ward part", now shown
false even on the single ML2 vector the shard names (§1.3) — and that
conclusion is asserted a second time in the shard's own verdict ⟨1⟩7.1.
Everywhere else the display is *stated* at general `n` but *used* only at
`n=1`: both S1 shards (`soft-index.md` (SIDX.3)/(SIDX.6),
`soft-index-b.md` (B4)) carry it as their advertised "unconditional
rung-0 deliverable", yet every downstream step of both lanes consumes
only the one-hard specialization (SIDX.7)/(SIDX.8) and (B5) — so their
headline jets `sgn(v_h−v_s)ℓ_h/ρ` and (B14) are untouched by *this*
defect, and both shards are in any case SKETCH and r1-FAILED for
independent reasons.  Upward, `ML4` is SKETCH and its statement is
one-hard; `S-general` is CONJECTURE and already lists "ML4 at `n≥2`" as
a live obligation; `ML4-Ward` itself survives as PROVED under the scoping
already applied, since (8), (10), (11) and the `(N−2n)` norm identity are
each verified exact at every `n`.  The Letter is clean and already hedges
"two or more hard legs" as open.  The two things that make this more than
a local erratum are **contamination of the single-source files**
(`notation.md:255` and `TRIANGLE.md:283` define the symbol and summarise
the theorem *by* the refuted display, so every future reader inherits it)
and **forward injection** (`briefs/soft-index-target.md:118–127` instructs
provers to prove it at "every `n<N/2`", which is why two independent
lanes wrote it down; and `soft-index-adjudication-r1.md` §3.7's repair
instruction is register-inconsistent, so the r2 unified shard would
reproduce the defect a third time if followed literally).  Repairing
those three lines — notation, TRIANGLE, target brief — plus deleting (18)
and scoping the adjudication's register, closes the blast radius.

---

## 6. Fix demands, ordered (for the orchestrator)

1. **`briefs/soft-index-target.md` L118–127** — correct the instruction
   before any S1 r2 round is launched. (Root cause; without this the
   defect returns.)
2. **`soft-index-adjudication-r1.md` §3.7 / §2.2** — fix the register:
   either full-sector + `2D_{n,N}A_n^{-1}J^z_0`, or hw + `(1/m_λ)Q_0Π_{hw}J^z_0`.
   Never "over `m_λ`, with `2DA^{-1}J^z_0`" (§1.2).
3. **`notation.md:255`** — the symbol table is the L4 single source.
4. **`theory/TRIANGLE.md:283`** — the campaign summary.
5. **`theory/ml4-ward-reduction.md`** — L191 (9) 2nd display, L213–215
   ⟨3⟩4, L419–424 delete (18), L430–437 ⟨3⟩2/⟨3⟩3, L503–505 ⟨1⟩7.1,
   L3–4 header.
6. **`claims/CLAIMS.md`** — ML4 row "proved in" cell → `⟨1⟩4` +
   `⟨1⟩5.⟨2⟩2`; ML4-Ward row: name `A_n` as the full-sector `D^†D`.
7. **`soft-index.md` / `soft-index-b.md`** — the eight DAMAGED statement
   sites and the two proposed claim rows; both shards are pre-r2, so this
   can fold into the unified r2 rewrite rather than being edited twice.
8. **`soft-index-r1.md`** — ERRATUM stanza on (C-d) and §5 (an
   over-broad clearance in a verdict is worse than a defect in a shard,
   because it is what the next session will cite).
9. **`corpus-r2.md:506`** and the three other RECORD rows — annotate in
   place; do not rewrite frozen adjudications.
10. **Checker spec** — `soft-index.md` ⟨1⟩10 item 1 must not demand a
    `<1e-12` residual for (SIDX.6) at `n=2`; fold
    `ml4_ward_n2_check.py` into the r2 spec as a standing red test, since
    neither lane's proposed checker would have caught F1.

---

## 7. Reproduction

`theory/checks/ml4_ward_n2_check.py` (in repo; green exit 0, `--red`
exit 1) certifies §1.1.  §1.2 (**UXR-R1**) and §1.3 (**UXR-R2**) and the
negative certificates of §1.4 were computed by importing
`ml4_ward_n2_check.build` and `sector_basis` unchanged and adding: the
hw-restricted projector `P_λ = D_λ(D_λ^†D_λ)^{-1}D_λ^†` with
`D_λ = D·hw`; the hw projector `Π_{hw} = hw·hw^†`; the explicit vector
`|χ_π⟩ ∝ Σ_x(−1)^x|x,x+1⟩`; and general (non-highest-weight) random
sector vectors for (10).  Sizes `N=8,10`, sectors `n=1,2,3`,
seed-independent (checked at two seeds).  These three computations
belong in `theory/checks/` as extensions of the existing certificate —
filing that is the orchestrator's call, as it is outside the audit lane.
