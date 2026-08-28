# Work order — (LR) for D16, repair round 2 (codex #4 of 7)

**FAIL(F1,F2,M1,M2,M3,M4)**.  Read the good news first, because it decides
what you protect: **LR1 is CONFIRMED PROVED UNCONDITIONALLY**, the critic
re-derived the diagonal extraction and agrees it delivers ONE sequence for
every fixed `W`, and **LR1-GEN is correct**.  That is the round's real result
and it is not in dispute.  Do not touch it, do not re-argue it, do not let the
repairs weaken it.

READ FIRST: `CLAUDE.md`; `briefs/critic-protocol.md` (**Standing checker
obligations**, five bullets); `theory/verdicts/lr-d16-r1.md` **IN FULL** —
your work order; `theory/lr-d16.md`; `definitions.md` D27, D13(a);
`theory/memory-index.md` ⟨1⟩5.⟨2⟩1 and ⟨1⟩7.⟨2⟩1;
`claims/CLAIMS.md` (K1–K4, M-INDEX-fin, M-INDEX-spec);
`theory/corner-b-draft.md` §1.2.

LANE (writable, nothing else): `theory/lr-d16.md`,
`theory/lr-d16-r2-response.md` (create), `theory/checks/lr_d16_check.py`.
No shared-file edits — MERGE PROPOSALS only.  No commits.

## F1 — LR2′ is EMPTY for D16.  Retract or replace; do not defend.

`⟨1⟩4.⟨2⟩5` fires only if `R²_{W_m}G(m) → 0`.  That is FALSE for every state
satisfying your own (H3): the `C_c^∞` magnon has `v(k) = J sin k ≠ 0`, leaves
every fixed window, and contributes exactly 1 to `𝒩_W`, so `G(m) ≥ 1−o(1)` at
every `m`.  Measured over `t ∈ [−40,40]`: `G = 0.990, 0.965, 0.950`, hence
`η_m = 4R√G = 11.9, 15.7, 19.5` — **increasing, not vanishing**.  And
`4R_Wε_W(t_-) ≈ 10–12` **exceeds the free bound** `2‖Q̂_W‖ = 6` at five of six
sampled times, so `⟨1⟩4.⟨2⟩3` is weaker than the trivial bound exactly where
it is needed.

Two further errors travel with it, and both must be fixed by name:
- **Your own checker row LRD-C2(d) prints these numbers and mislabels them**
  "escape profile falls with padding".  The apparent fall is a 6% finite-size
  artefact of the outside region shrinking from 6 sites to 2.  Relabel it
  honestly or delete it.
- `⟨1⟩4.⟨2⟩6` misdiagnoses the residue as the exponentially small kink tail
  (`q = 0.209`); it is the **O(1) magnon**.
- `⟨1⟩2`'s "logarithmically faster padding" rate is unsupported and
  contradicted by the measurement.

FIX DEMAND: retract (LR2′) as a D16 result, or state the genuinely true
weaker thing and prove it.  **Do not patch the bound to make the number come
out.**  The honest outcome — LR2 open, (LR2′) withdrawn, and the reason stated
as the O(1) magnon rather than the kink tail — is a fine result and keeps the
shard's credibility.  Note the mitigation's consequence is already settled:
`M-INDEX-spec` is unaffected either way, and `M-INDEX-fin` is safe.

## F2 — LR3: the repair is named, apply it

The monotonicity lemma `𝒩_{W'} ⪯ 𝒩_W` is **correct** and survives.  The gap is
that (LRD.13) is not `m`-independent: its second term is a fixed operator in an
`m`-dependent **dephased** state, and pinchings raise expectations of
non-commuting positives.  Measured at `(t_-,t_+) = (−8,+9)`: pinched term
`1.383 / 1.797 / 1.873` against RHS `2.078 / 2.493 / 2.568` — 24% spread,
increasing.  What the lemma removes is the `m`-dependence of the majorising
**observable**, not of the majorising **state**.

FIX (the critic's own, verbatim): **restore `sup_m` in (NR)'s second clause**;
the theorem then holds with the same constant `2S_NR/M`.  Also state plainly
that (NR) is **two clauses, not one** — the critic confirms it is genuine and
non-circular, so say what it is accurately.

## M2 — the class counterexample does NOT stand.  Retract it.

`⟨1⟩6.⟨2⟩5` names, constructs and cites **no model**, and its stated mechanism
("a charge-carrying core transits ballistically") is excluded by **your own**
(LRD.5): under (FN) the sharp-wall position equals `𝒬_0` and is pinned, so
`|ν| ≍ 2s|W_m|` requires unbounded **block** growth, not core transit.  The
corpus supplies no witness either — `theory/ace-ld.md` explicitly WITHDREW
"the kink is ballistic" as false.

So the campaign does **not** have a refutation of "gap + Lieb--Robinson ⟹
(LR)".  What survives, and what you should state instead: no gap and no
Lieb--Robinson velocity is used anywhere in this shard (the critic verified
that), and `ace-ld.md`'s ACE-LD-obst′ independently shows a no-transport clause
is **necessary** — a **scoping requirement**, not a refutation.  Downgrade the
claim to exactly that.

## M3 — K4 discipline: the violation is by CONTENT, not by citation

`⟨1⟩5.⟨2⟩8` is clean; the critic re-derived the `2×2` kernel (`a = qb`, both
equations close) and confirms it is K1+K2 only.  But **§H**, **⟨1⟩2's Remark**
and **⟨1⟩6.⟨2⟩4's (C-imm)** upgrade it to "the D16 core has no group velocity
/ the kink **manifold** is degenerate / D16 sits outside the ballistic class"
— those are **K4-strength claims**, and `corner-b-draft.md` §1.2 forbids them.
Scope all three to what K1+K2 actually give.  Grepping for the string "K4" is
not the test; the test is whether the sentence asserts K4-strength content.

## M4 — the checker: three no-ops and 10 unreachable rows

- **LRD-C1(b) is a no-op**: a non-integer reference density `0.3 / −0.7`
  leaves it PASS (`|allowed| = 11`).
- **LRD-C3(a) is a no-op**: both sides regroup the same weights, so a
  **non-unitary** propagator giving `Σp = 2.52` still PASSes at `1.8e−15`.
  (The critic verified the real (LRD.11) separately by building
  `α_{t±}(Q̂_W)` as matrices: `0.5483368101` both ways — so the identity is
  true; your gate simply does not test it.)
- **LRD-C3(d) is blind to its advertised claim**: a mutant implementing the
  shard's actual `W_1`-pinched reading returns the **identical** slack
  `−0.1211`.
- **10 of 18 rows are killed by no red mode.**  `--red-monotone` reaches
  C3(c) only, though its docstring claims C3(c,d).  C6(b) is subsumed by
  C5(a) and prints a value against itself.
- **m2**: C4(b) evolves with `H_kink` but treats `⟨H_XXZ⟩` as conserved —
  `‖[H_kink,H_XXZ]‖ = 16.6` at `N = 12`, with drift reaching `−0.62`.

Rebuild against all five standing obligations, and report the **exit path** per
mode plus a row-by-row reachability table.  Every row that carries evidence
needs a mutant that kills it.

## MERGE PROPOSALS

- **MP-1 — re-propose as the critic dictates**: D27 clause 1 existentially
  binds the `T_n` that clauses 2–3 quantify over, so "a theorem, not a
  hypothesis" is true of the clause in isolation and misleading about (LR).
  New form: *for any `T_n → ∞` there is a subsequence along which clause 1
  holds, so the content of (LR) lies entirely in clauses 2–3.*
- **MP-3**: draft `LR1-GEN` and `LR-D16-EDW` as **PROVED** rows (the critic
  cleared both, with the m2 caveat carried); `LR-D16` stays HOLD.
- **MP-4**: unchanged — the critic says it is "more right than the shard knew".
- **MP-2**: HOLD.

Work fully autonomously.  Do not ask questions.  Do not stop at a plan.
