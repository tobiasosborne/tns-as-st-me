# Corner A — response to critic verdict r2

Prover response (revision **r3**, 2026-08-25) to
[`verdicts/corner-a-r2.md`](verdicts/corner-a-r2.md), verdict
FAIL(A1,A2,G0,B3): 6 MAJOR, 3 MINOR, 1 NOTE.  Round-1 disposition:
[`corner-a-r1-response.md`](corner-a-r1-response.md).

**Method, as before.** Every objection was re-derived independently before
disposition.  New evidence is in
[`checks/corner_a_check.py`](checks/corner_a_check.py), checks **C8--C11**
(ALL PASS with C0--C7).

**Outcome: no rebuttals this round.**  All six MAJORs and all three MINORs are
conceded and repaired; two of them (1 and 3) were *bugs*, not presentation
defects, and both were reproduced numerically before repair.  Objection 6 is
outside this package's scope and is recorded rather than fixed, as instructed.

---

## Disposition table

| # | sev | subject | disposition | where repaired |
|---|---|---|---|---|
| 1 | MAJOR | `𝒱_b` not well defined on `𝒲_{Λ,b}` | **CONCEDED — bug; FIXED** by the padding hypothesis + injectivity lemma | D4(a1)--(a4); corner-a.md ⟨1⟩4(d1), ⟨2⟩4.⟨3⟩0; checks **C8**, **C8b** |
| 2 | MAJOR | (d3) calls the twisted action the lift `[ω]` obstructs | **CONCEDED — FIXED**: `[ω_α]` obstructs *removing the multiplier* | corner-a.md ⟨1⟩4(d3), ⟨2⟩4.⟨3⟩3; D9(c′)3 |
| 3 | MAJOR | G0(c) drops the `m=b` bulk term | **CONCEDED — bug; FIXED**, both exact forms displayed | corner-a-goldstone.md G0(c), ⟨2⟩3.⟨3⟩2--⟨3⟩4; check **C9** |
| 4 | MAJOR | D12 over-quantified and conflated | **CONCEDED — FIXED**: remainder-only (a), `ℓ¹∩BV` (a′), upper-bound-only (b) | D12 rewritten; SBP (iv),(v); check **C10** |
| 5 | MAJOR | claims DAG quantifiers | **CONCEDED — FIXED** for A1, A2, G0 **and B3** | `claims/CLAIMS.md` |
| 6 | MAJOR | retracted content used in two drafts | **CONCEDED — RECORDED, not fixed** (out of scope; drafts untouched) | corner-a-pitfalls.md **Flag 6** |
| 7 | MINOR | D9(c) mixes definition with theorem | **CONCEDED — FIXED**: D9(c) definition-only, D9(c′) corollaries; A1 no longer depends on D9(c) | D9(c)/(c′); corner-a.md ⟨1⟩4 ASSUME |
| 8 | MINOR | D1(e′) positivity justification wrong | **CONCEDED — FIXED**: CP contraction `tr[l_α T r_β T^†] ≥ 0` | D1(e′) Lemma; check **C11** |
| 9 | MINOR | notation.md keeps the rejected inverse/group conventions | **CONCEDED — FIXED**: rows marked SUPERSEDED in place | `notation.md` |
| 10 | NOTE | endpoint torsor and D1(e′) are not vacuous | **ACCEPTED** | — |

---

## The two bugs, reproduced

### Objection 1 — the ill-defined window action

`𝒲_{Λ,b}` is a space of *physical vectors*, so `ι(M) ↦ ι(NM)` is an operator
only if `ker ι` is invariant under `L_N`.  It need not be.  Reproducing the
critic's counterexample exactly:

```
A^0 = diag(1,2),  A^1 = X,  u(g) = diag(1,-1),  V = Z,
b_l = (sqrt2, 1),  b_r = (1, 0),   one site each side of the bond,
N   = [[-sqrt2, 0], [1, 0]]
  ->  |ι(N)|_inf = 4.4e-16       (i.e. N in ker ι)
      |ι(ZN)|_inf = 4.0          (i.e. ZN not in ker ι)
```

The tensor really is admissible: transfer spectrum `{4.303, 3, 1, 0.697}` with a
unique top eigenvalue (so `λ_E = 0.697` after rescaling), length-2 words of rank
`4`, and `Z^{-1}A^0Z = A^0`, `Z^{-1}A^1Z = −A^1`, so (IT) holds with the stated
`u, V`.  So r2's A1(d1) — and its PROVED row — were **false as written**.

**Repair, and why it is the right one.** On a window with `≥ n_0` sites on each
side of the bond and `b_l, b_r ≠ 0`, the coefficient `b_l^† P M Q b_r` is
linear in `P` and in `Q` separately, each of which ranges over a spanning set of
`M_χ(ℂ)` (D1(c)); with `b_l ≠ 0` the row vectors `b_l^†P` exhaust `(ℂ^χ)^*` and
with `b_r ≠ 0` the columns `Qb_r` exhaust `ℂ^χ`, so `ι` is injective and
`𝒱_b := ι ∘ L_M ∘ ι^{-1}` is well defined by transport of structure.  Measured
ranks of `ι` on the counterexample:

```
padding 1|1 -> rank 2   (ill defined)      2|1 -> rank 4
        1|2 -> rank 2                      2|2 -> rank 4  (well defined)
```

Note the asymmetry: the critic's `b_l` is adversarial (`b_l^†A^0` and
`b_l^†A^1` are parallel), which is exactly what the `n_0`-padding hypothesis
rules out.

### Objection 3 — the dropped edge term in G0(c)

From `B_G = 𝒩_k(X) + (1−e^{ik})A_αX` and Lemma SBP(ii), the bulk sum
`Φ_k^Λ(A_αX) = Σ_{m=a}^{b} e^{ikm}|ψ;X@m⟩` runs to **`b`**.  r2 truncated it at
`b−1` while keeping the *uncombined* SBP coefficient `e^{ik(b+1)}`, losing
`(1−e^{ik})e^{ikb}|ψ;X@b⟩`.  Reproduced on the script's Pauli tensor,
`L=4`, `k=0.37`, `X=K`:

```
|| LHS - r2 display ||                       = 0.4505862126399518
|| (1-e^{ik}) e^{ikb} |psi;X@b> ||           = 0.4505862126399517
|| LHS - corrected display  ||               = 5.9e-17
|| LHS - combined display   ||               = 3.9e-17
```

matching the critic's independently obtained `0.4505862126399518` and
`6.25e-17`.  Both corrected forms are now displayed in G0(c).  The error was a
mismatch of two summation ranges in a single step, and it did not propagate:
G0(d), G0(e), the FM/O1 result and Lemma SBP itself are untouched.

---

## Notes on the remaining objections

**4.** Three separate over-quantifications, all conceded. (i) `c_0 ⊄ ℓ¹`, so
"the identity holds exactly for `f ∈ c_0`" is unwarranted — D12(a) now claims
only that the **remainder** vanishes, and the new D12(a′) supplies `ℓ¹ ∩ BV` as
the class in which both sides converge absolutely. (ii) The `Θ(|Λ|^{1/2})` bulk
claim is false: for `χ=1`, `A_αX ∝ A_α` and the plane-wave sum is bounded by
`2C_∂/|1−e^{ik}|` for every `Λ` (check C10, `|Σ e^{ikn}| ≤ 5.436` for
`L` up to 128).  The δ-normalised conclusion needs only the boundary *upper*
bound, which is what the proof now uses. (iii) A fixed-`k` display may not carry
a `c_0` hypothesis; D12 now states this as an explicit type discipline.

**5.** A1(b) is now stated as an **iff** (with the converse proved: scalar
`V_α(g)` makes the two boundary insertions cancel, so the strings stabilise
exactly).  A2 and D9(d) carry hypothesis **(T)** explicitly, with the per-orbit
fallback stated.  G0's row carries `ξ ∈ 𝔥_α` + normal ordering on (a)--(d) and
"any `ξ ∈ 𝔤`, finite range" on (e).  **B3** was rewritten: it cited the refuted
`𝒜`-orbit language and contradicted the amendment note in its own file.  (B3 is
outside the four rows originally assigned; it is edited here only because it is
an internal contradiction inside a file this package owns, and the edit is
confined to replacing refuted language — its status stays SKETCH.)

**7.** A1's ASSUME clause no longer lists D9(c) as a source of content, and the
DAG dependency was dropped: A1 uses only the *names* `E_b^α` and `⋆`, and
proves the bijection/torsor/orbit statements, which D9(c′) now records as
corollaries.  This makes the definition→theorem direction acyclic.

**8.** The correct positivity argument is the CP one: with `T := Σ_s c_s P_W(s)`,
`⟨c|ϱ̃_W|c⟩ = tr[l_α T r_β T^†] = ‖l_α^{1/2}Tr_β^{1/2}‖_2^2 ≥ 0`.  Verified
Hermitian to `0.0` with `min eig = −1.4·10^{-16}` and `tr = 3.45 > 0`
(check C11).  As the critic notes, A2's weak-* limit supplies positivity
independently, so this is a convenience lemma.

---

## Residual gaps after r3 (unchanged in substance from r2)

1. Normality/split property for `ω_α^{M@b}` — blocks `docs/framing.md`'s
   state-space charge algebra (corner-a.md ⟨1⟩4.⟨2⟩9).  **SKETCH, load-bearing.**
2. Uniformity of A2 over a continuous `Ω_vac` — blocks Corner B on M1
   (corner-a-kinks.md ⟨1⟩10.⟨2⟩3).  **SKETCH, load-bearing.**
3. The passage from the continuity equation to a soft theorem — Corner C's
   entire content (corner-a-goldstone.md ⟨1⟩6.⟨2⟩7).  **RETRACTED from Corner A.**
4. Completeness of `[ω_α]` as a phase invariant — cited, not proved.
5. Propagation of items 1--3 into `spt-scoping-draft.md` and
   `corner-b-draft.md` — **not this package's edit**; tabulated in
   corner-a-pitfalls.md Flag 6 for freeze reconciliation.

None of 1--4 is claimed as PROVED anywhere in the package.
