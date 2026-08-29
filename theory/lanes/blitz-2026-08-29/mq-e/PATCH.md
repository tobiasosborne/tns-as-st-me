# Orchestrator patch instructions (string anchors only)

Apply only after accepting the `PROVED-candidate` in `mq-e-proof.md`.

## 1. Install the proof and falsifier

- Copy this lane's `mq-e-proof.md` to `theory/mq-e.md`.
- Copy this lane's `check_mq_e.py` to `theory/checks/mq_e_check.py`.
- Preserve `CHECK_OUTPUT.md` with the proof verdict or rerun both green and
  `--red` commands after the copy.

## 2. `claims/CLAIMS.md`

Replace the complete row beginning with the exact anchor `| Mq-E |` by:

```markdown
| Mq-E | For D16's spin-`1/2` model, on every admissible frozen-boundary interval and at infinite volume, the fixed-charge incoming component of `H_3=P_3H_{XXZ}P_3` is explicitly unitarily equivalent to the Fano graph (Mq.7).  The negative/positive tails are respectively the incoming/reflected charge-`-1` leg with kink bond `m` and the transmitted charge-`+1` leg with kink bond `m-2`; every fixed-window observable is two channel-kink constants plus a finite-support graph remainder.  This is a theorem about the projected component, not the unprojected full chain. | **PROVED** | D14, D16 | theory/mq-e.md | theory/checks/mq_e_check.py (finite-volume falsifier; `--red` shifts the right wall pair and exits 1) |
```

Replace the complete row beginning with `| Mq-AD3 |` by:

```markdown
| Mq-AD3 | The projected D16 incoming `≤3`-wall component satisfies D18 by Mq-E's explicit unitary/local-observable map, Kato--Rosenblum, Feshbach/Weyl analysis, and Jacobi local decay.  This does not prove D18 for the unprojected full chain. | **PROVED** | D18, D16, Mq-E | theory/memory-quantization.md §3; theory/mq-e.md | theory/checks/mq_e_check.py tests the sector reduction, not the spectral theorems |
```

Replace the complete row beginning with `| M-tk |` by:

```markdown
| M-tk | On D16's projected incoming `≤3`-wall component, `t(k)=[1+iJ²/(4ωv)]^{-1}`, `T=|t|²`, and `T(k)=16(Δ-1)²k²+O(k⁴)` as `k→0`.  The projected statement is unconditional by Mq-E.  `O(Δ^{-2})` full-chain leakage is measured; the unprojected formula and universality of the zero/coefficient remain CONJECTURE. | **PROVED** | D15, D16, Mq-E, Mq-AD3 | theory/corner-b-draft.md §5; theory/memory-quantization.md §3; theory/mq-e.md | theory/checks/mq_e_check.py; crosscheck_corner_b_tk.py remains an empirical full-chain cross-check only |
```

## 3. `theory/memory-quantization.md`

At the exact anchor `**Status:** M-flux is`, replace the first status
paragraph through `currently contains only a finite N=14 enumeration.` with:

```markdown
**Status:** M-flux is **PROVED**, M-quant is **PROVED conditional on D18**,
Mq-E and Mq-AD3 are **PROVED for the projected incoming `≤3`-wall
component**, and the displayed Fano formula/soft zero is consequently
**PROVED unconditionally for that projected component**.  The unprojected
full-chain lift remains open because `P_3H(1-P_3)≠0`.
```

Under the exact anchor
`**ASSUME Mq-E (all-volume enumeration/isomorphism).**`, replace that heading
and its four numbered clauses, ending at the sentence whose exact anchor is
`The N=14 enumeration S1 in corner-b-draft.md is evidence for Mq-E, not a proof of this quantified assumption.`, by:

```markdown
**USE Mq-E (all-volume enumeration/isomorphism; PROVED in
`theory/mq-e.md`).**  For every admissible frozen-boundary volume and at
infinite volume, its explicit unitary intertwines `H_3` with (Mq.7), labels
the negative/positive tails as the D14 reflected/transmitted channels with
charges `-1/+1`, and maps every fixed-window observable to its two
channel-kink constants plus a finite-support remainder.  Thus the
channel-subtracted observable needed for Jacobi local decay has finite graph
support.  The former `N=14` enumeration is now only one check of the proved
all-volume formula.
```

Replace the heading anchored by
`**Mq-AD3 (PROVED conditional on Mq-E per corpus-r2 adjudication).**` with:

```markdown
**Mq-AD3 (PROVED for the projected component, using Mq-E).**
```

Replace the exact sentence `**PROVE.**  Under Mq-E, H_3 satisfies D18` by
`**PROVE.**  By Mq-E, H_3 satisfies D18` (retaining the rest of that sentence).

At the exact anchor `**Why this is conditional even before the full-chain lift.**`,
replace that paragraph heading and its first two sentences, through the
sentence ending `only after Mq-E is assumed.`, by:

```markdown
**Why this still does not prove the full-chain lift.**  Mq-E now proves the
all-volume unitary for the compressed incoming component, so the projected
Kato--Rosenblum and Feshbach conclusions are unconditional.  Separately, the
full Hamiltonian has
```

Retain the following existing sentence beginning
`P_3H(1-P_3)≠0; five-wall and higher configurations are real` and the rest of
that scope paragraph.

## 4. `theory/corner-b-draft.md`

- Replace the exact sentence under `## 5` beginning `This is the dynamical
  model computation.  The Fano solution is exact **if**` and ending at the
  `memory-quantization.md §3 holds.` anchor by:

```markdown
This is the dynamical model computation.  Mq-E (`theory/mq-e.md`) proves the
all-volume sector enumeration/isomorphism for the projected incoming
component, so the Fano solution below is exact on that component.
```

- Replace the block beginning
  `**Finite-enumeration hypothesis S1 (not an all-volume lemma).**` and ending
  with the sentence `with no free parameter.` by a short theorem summary
  citing `theory/mq-e.md` §§1--6.  Preserve the old `N=14` histogram only as a
  falsifier example, not as the basis of the claim.
- Replace the exact anchor `Assuming Mq-E, the effective one-body problem` by
  `By Mq-E, the effective one-body problem`.
- In the `**Scope.**` paragraph, replace `conditional on Mq-E identifying`
  by `because Mq-E identifies` and retain the full-chain leakage warning.
- In §6's status table, replace the Mq-E-conditional label for `T(k)` by
  `PROVED for the projected incoming component by Mq-E`; do not alter the
  `O(Δ^{-2})` full-chain caveat.

## 5. Lockstep status surfaces

In `theory/TRIANGLE.md`, anchor the paragraph at `**Projected spectral scope.**`
and replace its Mq-E-conditional discussion by a citation to `theory/mq-e.md`,
while preserving the full-chain `P_3H(1-P_3)≠0` caveat.  Change the exact
headings

- `### 3.3 Fano t(k) — **PROVED conditional on Mq-E for the displayed graph**`
- `### 3.4 The soft memory zero — **PROVED conditional on Mq-E for the displayed graph; universality CONJECTURE**`

to say `PROVED for the projected incoming component` (and retain
`universality CONJECTURE` in §3.4).

In `paper/main.tex`, replace the paragraph anchored by
`\emph{Sector reduction and the Fano level.}` through the sentence ending
`no singular-continuous spectrum.` with text stating that Mq-E is proved by
the explicit all-volume row/column enumeration and unitary, while the
unprojected full-chain H-AD-G remains assumed.  In the preceding ground-truth
paragraph, replace `Mq-AD3 PROVED conditional on the sector-reduction
hypothesis Mq-E` by `Mq-E and Mq-AD3 PROVED for the projected incoming
component`.

In `paper/v2-claim-audit.md`, update only the three rows anchored by
`H-AD-G itself we prove only for the dominant domain-wall sector`,
`In the reduced sector`, and `Eq. (3) soft zero`: Mq-E is PROVED and the last
two are unconditional within the projected incoming component; all three
must continue to state that full-chain D18/formula and universality are open.
