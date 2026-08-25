# Critic verdict ml2-r2 — `theory/ml2-completeness.md` (+ `theory/checks/ml2_completeness_check.py`)

Critic: Opus (L6 adversarial loop, round 2). Date 2026-08-25.
Predecessor: `theory/verdicts/ml2-r1.md` — `FAIL(M1, M2, M3)`.
Artifact status at review time: "R1 MAJORS REPAIRED; L6 r2 critic pending".

**SUMMARY: PASS**

All three r1 MAJORs are substantively repaired, and I verified each one myself
rather than taking the prover's word. No new MAJOR was introduced. The residue
is MINOR/NOTE only — mostly r1 items the prover chose not to touch, plus four
small blemishes introduced by the fix itself. None of them affects the truth of
Theorem ML2 or of the (24) expansion.

---

## 0. What I ran this round

All independent of the repo checker (`J=0.8137`, not the checker's `1.271`).
Scratchpad: `r2.py`, `r2b.py`, `mut2/`.

- **R1** Revised checker, normal and `python3 -O`: byte-identical output, exit 0,
  zero `assert` statements in the file.
- **R2** Ten-mutant battery on **copies**, including both mutants that survived
  in r1 and the 1→7 mutation the coordinator asked me to re-verify.
- **R3** Exhaustive sweep of the (24) singular coefficient over **all `N²`
  ordered ring-momentum pairs** for `N=6,8,10,12,14,16,18` — on-fiber value and
  off-fiber vanishing both, which is strictly more than the checker probes.
- **R4** End-to-end reconstruction test of (24) at the `K=π` fiber.
- **R5** Direct test of whether (R5) really supplies the first sum of (24),
  at a real-pair fiber, at a **string** fiber (complex conjugate momenta), and
  at the `K=0` **double descendant** — the one place where (R5)'s applicability
  was still open after r1.
- **R6** Re-ran my independent ED classification against the checker's new
  parity-aware analytic formulas.

---

## M1 — REPAIRED (verified). The singular class and its coefficient

The revision adds ⟨1⟩6.⟨2⟩2 with (23)--(24), rewrites ⟨1⟩1 PROVE-3, and adds a
red-capable checker leaf. I checked the substance, not just the presence.

**(a) The closed form is right, and the off-fiber vanishing is right.** (R3) I
swept every ordered pair of ring momenta — not just the `k_s+k_h=π` line the
checker walks, and not just the single off-fiber probe at `soft_label+1`:

| `N` | on-fiber pairs | max err vs `e^{ik_h}+e^{ik_s}` | off-fiber pairs | max abs overlap |
|---|---|---|---|---|
| 6 | 6 | 1.6e-15 | 30 | 1.7e-15 |
| 10 | 10 | 3.2e-15 | 90 | 2.8e-15 |
| 12 | 12 | 3.7e-15 | 132 | 4.1e-15 |
| 14 | 14 | 1.6e-14 | 182 | 1.1e-14 |
| 18 | 18 | 1.8e-14 | 306 | 6.8e-15 |

So `⟨χ_π|Q_{k_s}|k_h⟩` is `e^{ik_h}+e^{ik_s} = 2i\cos((k_h−k_s)/2)` on the fiber
and **identically zero off it**, exactly as the `\mathbf 1_{\mathscr X_K≠∅}`
indicator in (24) asserts.

I also re-derived ⟨3⟩2 by hand and it is correct, including the part that is
easy to get wrong: the wrap pair `{N−1,0}` contributes the *same* value as the
other `N−1` only because **two** sign flips cancel — `(−1)^{N−1}=−1` (needs `N`
even) and `e^{-ik_h}+e^{-ik_s}=\overline{e^{ik_h}+e^{ik_s}}=−(e^{ik_h}+e^{ik_s})`
(needs `e^{ikN}=1`). See m14 below: the step names only the second.

The caveat "on this branch choose the congruent representatives with
`k_s+k_h=π`" in ⟨2⟩2 is **necessary and correctly placed** — the `\cos` form is
representative-dependent while the overlap is not. At `N=12`, `k_h=2π/12`:
overlap `+1.000000i`; `2i\cos((k_h−k_s)/2) = +1.000000i`; but
`2i\cos((k_h−(k_s+2π))/2) = −1.000000i`. Good that the shard says which
representative it means, and good that ⟨3⟩2 also records the invariant form.

**(b) (24) reconstructs the state exactly.** (R4) I built the `K=π` fiber my own
way, split off the singular direction, expanded the rest, and reassembled (24):

| | `‖(24) − Q_{k_s}\|k_h⟩‖` | Parseval in fiber | singular share |
|---|---|---|---|
| `N=12, k_h=2π/12` | 5.0e-15 | 10.0000000000 (`=N−2`) | 10.0% |
| `N=12, k_h=4π/12` | 6.7e-15 | 10.0000000000 | 30.0% |
| `N=16, k_h=6π/16` | 7.9e-15 | 14.0000000000 (`=N−2`) | 24.4% |

(24) is exact, Parseval is exact, and the singular leaf carries 10--30% of the
norm — i.e. the r1 objection was real and the repair actually recovers what was
missing.

**(c) (R5) really does supply the first sum — including at the `K=0` double
descendant.** This was the one point I left open in r1 ("(R5) applies … stating
that choice explicitly would still help"). (R5) is a formula in
`(k_1,k_2,A_{12},A_{21},\mathcal N_B)`; at `k_1=k_2=0` the contact equation
degenerates to `0=0`, so the representative is not forced. I implemented (R5)
verbatim from `soft-current-recon.md` ⟨2⟩2 and compared against direct inner
products in the `K=0` fiber at `N=10`, `k_h=6π/10`, `k_s=−k_h`:

```
      E/J    X=cos q   |c_B| direct   |c_B| via (R5)        err   class
 0.000000   1.000000    0.471404521      0.471404521   1.2e-15   DESCENDANT (S^-)^2|Om>
 0.467911   0.766044    0.762792753      0.762792753   0.0e+00   real pair
 1.652704   0.173648    1.385039088      1.385039088   2.2e-16   real pair
 3.000000  -0.500000    2.284700655      2.284700655   1.3e-15   real pair
 3.879385  -0.939693    0.240280324      0.240280324   5.0e-16   real pair
 Parseval: sum|c_B|^2 = 8.0000000000 = ||Q|k_h>||^2 = N-2
```

With `(A_{12},A_{21})=(1/2,1/2)` the descendant's (R5) coefficient is
`0.471404521 = \sqrt{2/(N−1)}`, matching both the direct inner product and the
closed form I gave in r1. And (R5) survives **complex** momenta too — at `N=12`
string roots `k_{1,2}=1.0472∓0.6939i` and `1.3090∓1.3516i` it agrees with the
direct overlap to 1.3e-13 and 3.6e-11 (my own forward evaluation of large
complex exponentials, not a discrepancy). So `\mathscr B_K^{D7}` really is
(R5)-computable throughout, and (24) is complete as stated. The only residue is
that the descendant's representative is still not written down (m11).

---

## M2 — REPAIRED (verified). The coincident-zero test is no longer a tautology

`coincident_zero_audit` (lines 168--193) now evaluates the D7 amplitude
`−(z²−2z+1)/(z²−2z+1)` — the `oracle-bethe.md` (6) fraction specialized to
`k_1=k_2=k` — builds the actual coordinate vector, takes its norm, and
**counts** the zero vectors; line 354 prints `coincident_zero_count`, not the
literal `n_sites`. Both r1 complaints are gone.

(R2) The 1→7 mutation the coordinator flagged now dies exactly as reported:
`FAIL: coincident zero-vector count N=6: 0 != 6`, exit 1. I also confirmed the
test is genuinely evaluating D7 rather than a rearranged identity: dropping the
leading minus sign on `outgoing_amplitude` (mutant `d7_sign`) also goes red,
`0 != 6`. Division by zero is impossible here — `(z−1)²=0` needs
`z=e^{i(2n+1)π/N}=1`, i.e. odd/integer even, which cannot happen.

Residual cosmetic point only (n6): the two exponentials are written
`exp(1j*momentum*(x+y))` and `exp(1j*momentum*(y+x))`, which are the same
expression; writing them as `k_1*x+k_2*y` and `k_2*x+k_1*y` would make the
specialization visible and would let a `k_1↔k_2` mutation be caught. Not a
correctness issue.

---

## M3 — REPAIRED (verified). Coverage and parity

`SIZES = (6, 10, 11, 12, 13, 14, 16, 18, 20, 22, 26)` — odd `N` (11, 13),
`N≡2 mod 4` (6, 10, 14, 18, 22, 26), `N≡0 mod 4` (12, 16, 20). Line 271
`expected_singular = 1 if n_sites % 2 == 0 else 0` and lines 289--291
`expected_pi_degenerate = 0` for odd `N` make (14) row 3 and the `L−3` branch
parity-aware. My r1 suggestion n4 (add `N=22`, the string-threshold case) was
taken.

**(R2) Both r1 survivors are now killed:**
- `r1_signflip` (`block[-1,-1] -= …` → `+=`, the odd-`N` reflection endpoint):
  `FAIL: missing descendant N=11, m=-5`, exit 1.
- `r1_pideg` (`expected_pi_degenerate = length − 2`, deleting the `L−3` branch):
  `FAIL: analytic class formula mismatch N=6: … expected real=5, … pi_degenerate=1`,
  exit 1.

Full battery — **10 mutants, 10 killed, 0 survivors**:

| mutant | what it breaks | result |
|---|---|---|
| `r1_signflip` | odd-`N` `2−σ_m c_m` endpoint | red (N=11) |
| `r1_pideg` | `L−3` branch of (13) | red (N=6) |
| `taut_1to7` | incoming amplitude 1→7 | red, `0 != 6` |
| `d7_sign` | sign of the D7 fraction | red, `0 != 6` |
| `sing_coef` | `\cos((k_h−k_s)/2)` → `\cos((k_h+k_s)/2)` | red, 1.732 |
| `sing_i` | drops the factor `i` in (24) | red, 2.449 |
| `sing_norm` | drops `(−1)^x` in (12) | red, 1.732 |
| `sing_wrap` | drops the wrap pair from (12) | red, normalization |
| `offfiber` | disables the off-fiber probe | red, 1.732 |
| `parity` | `expected_singular = 1` always | red (N=11) |

**(R1)** Normal and `-O` runs are byte-identical, exit 0; no bare `assert`s.
**(R6)** The checker's new parity-aware formulas are **identical** to the
formula I wrote independently in r1, for every `N=4…40`; and my independent ED
(translation-projector fibering, SU(2) descendant criterion, eigenspace-wise so
the degenerate `K=π` level is handled correctly) reproduces the checker's counts
for all eleven `SIZES` and, from the r1 sweep re-run here, for every `N=4…28`.
Every `desc/string/real/singular/pi-deg` figure the checker prints matches my ED
exactly.

**Quoted magnitudes in ⟨1⟩6.⟨2⟩1 all verified to the digit:** spectral mismatch
`8.882e-15` (N=16, 22), eigenvector residual `4.044e-14` (N=26), projector error
`4.640e-14` (N=26), singular-overlap error `6.280e-15` (N=26).

---

## MINOR (residue)

Carried over from r1 and **not addressed** — the prover repaired only the three
MAJORs. I am not re-arguing them; see `ml2-r1.md` for the reasoning. They remain
open and should be swept before the shard feeds the paper:

- **m1** ⟨1⟩1 PROVE-2 still cites "(15)--(20)"; the resolution of the identity is
  **(21)**. (PROVE-3 *was* updated to cite (23)--(24), so the neighbouring
  reference is now inconsistent with the unfixed one.)
- **m2** ⟨1⟩1 PROVE-1 cross-reference should be ⟨1⟩3--⟨1⟩4 (the `K=π` waves are
  classified in ⟨1⟩4, and ⟨1⟩3.⟨2⟩1 assumes `c>0`).
- **m3** ⟨1⟩3.⟨2⟩3.⟨3⟩3's converse is false at the single root `X=1, m=0`.
- **m4** ⟨1⟩5.⟨2⟩3 "almost every `K≠0`" should be "every `K≠0`".
- **m5** ⟨1⟩5.⟨2⟩4.⟨3⟩2: absence of singular continuous spectrum is still
  asserted rather than derived; the needed Jacobians sit unused in the next step.
  Of the whole residue this is the one a referee is most likely to stop on.
- **m6** ⟨1⟩5.⟨2⟩3.⟨3⟩3 still states `Σ_r \overline{w_q}w_{q'}=2πδ(q−q')` without
  noting that a regular remainder must (and does) cancel.
- **m7** ⟨1⟩4.⟨2⟩2.⟨3⟩2's "finite sine/cosine orthogonality" is still the only
  hand-wave covering the one orthogonality that is not automatic.
- **m8** L6b: still no top-level `⟨1⟩7. QED`; ⟨1⟩5.⟨2⟩2, ⟨1⟩6.⟨2⟩1 still lack
  sub-proofs/QED; ⟨1⟩6.⟨2⟩1 is still a `PROVE` step whose content is a script run.
- **m9** L4 collisions with `notation.md` (`U`, `S(·)`, `X`) unchanged.
- **m10** D7 tie-in for `t`, `η` still missing.
- **m11** The `K=0` double descendant's D7 representative `(A_{12},A_{21})=(1/2,1/2)`
  is still not stated, even though (24) now depends on (R5) covering it. I have
  verified (R5) *does* cover it with that choice (M1(c)) — one clause in
  ⟨1⟩3.⟨2⟩6.⟨3⟩2 or in ⟨1⟩6.⟨2⟩2 closes it.

New, introduced by the repair:

- **m12** **L6b regression.** The new leaves ⟨1⟩6.⟨2⟩2.⟨3⟩1, ⟨3⟩2 and ⟨3⟩3 carry
  **no `Justification:` line at all** — they are the only leaves in the shard
  without one. L6b requires every leaf justified by a definition, a claim id, or
  a named computation. Add: ⟨3⟩1 → (12) and D6; ⟨3⟩2 → (R3), (12), and
  `e^{ik N}=1`; ⟨3⟩3 → ⟨1⟩4.⟨2⟩3 and Parseval.
- **m13** `\mathscr E_K` is defined in (23) and then never used again — (24) sums
  over `\mathscr B_K^{D7}` and the indicator. Either use it or drop it.
- **m14** ⟨1⟩6.⟨2⟩2.⟨3⟩2's "periodicity makes the wrap pair contribute the same"
  names only one of the two cancelling sign flips (see M1(a)). Since this is
  precisely where a sign error would hide, spell out both: `(−1)^{N−1}=−1` for
  `N` even, and `e^{ikN}=1` turning the wrap coefficient into the complex
  conjugate.
- **m15** ⟨1⟩6.⟨2⟩1 now says the checker runs "for `SIZES=(6,10,11,12,13,14,16,18,20,22,26)`"
  while (22) tabulates only `N=12,16,20`, described as "representative". That is
  honest, but the four quoted error magnitudes are maxima over the **whole**
  eleven-size run (`4.044e-14` and `4.640e-14` are `N=26`, `6.280e-15` is `N=26`),
  which the sentence does not say. One clause, so the numbers can be reproduced.

## NOTE

- **n6** (checker cosmetics) `coincident_zero_audit` writes both plane waves with
  the identical exponent `(x+y)`/`(y+x)`. Correct, but writing `k_1*x+k_2*y` and
  `k_2*x+k_1*y` would make the coincident specialization visible and testable.
- **n7** r1's n1--n5 (the ML1/wave-operator disclaimer, the two meanings of
  "real" in (14) vs (22), the anti-periodic center gauge, and the observation
  that `|χ_π⟩` is just the `K=π` member of the infinite-chain bound band) are
  all still open. They are presentation, not correctness.
- **n8** For the record, everything I verified in r1 about ⟨1⟩2--⟨1⟩5 still
  holds: those sections are textually unchanged in this revision, so the r1
  confirmations (inventory for `N=4…28`, the `N=20` vs `N=22` string threshold,
  simplicity, `X≥−1`, (11), (20) to 2.9e-15, (21) and the three Jacobians,
  onto-ness of the fiber transform) carry over unmodified.

---

## Verdict

The three MAJORs are genuinely fixed, not merely marked fixed: the singular
coefficient is correct on-fiber and vanishes off-fiber under an exhaustive
sweep; (24) reconstructs the charge-created state to 1e-14 with exact Parseval
and a singular share of 10--30%; (R5) demonstrably covers every remaining
member of `\mathscr B_K^{D7}`, strings and the `K=0` double descendant included;
the coincident test now evaluates D7 and dies under two independent mutations;
and the certificate now exercises odd `N`, `N≡2 mod 4`, and `N≡0 mod 4`, with
both of r1's surviving mutants killed and a 10/10 mutation kill rate. The
residue is fifteen MINORs and three NOTEs, all presentation or L6b hygiene, none
touching the truth of the theorem.

Per the r2 adjudication rule (MINOR/NOTE residue only ⇒ pass), and under **L10**
(honest verdicts — this one holds, so I pass it):

**SUMMARY: PASS**

Recommended before the shard feeds the paper: sweep m1--m15, prioritising **m5**
(the singular-continuous-spectrum leaf), **m12** (the three unjustified new
leaves), and **m11** (the descendant's D7 representative, on which (24) now
silently depends).
