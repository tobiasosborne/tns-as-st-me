# Joint-critic cross-consistency

## 1. `proto-lsz` residual versus the ML3 reconciliation

They identify the same obstruction only in part, and the distinction must be preserved.

- `ml3/reconciliation.md:57-100` names uniform packet-smeared regularity of the orthogonal-current component at `k_s=0`, including `k_s=Θ(1/N)`, sufficient to exclude a physical `1/k_s` pole and obtain the required `O(ε²)` component bound.
- `proto-lsz/proto-lsz.md:266-334` names the strictly larger `(COMP-HS)` package: descendant-projector provenance and profile matching; complementary-current `O(ε²)`; direct-contact `O(ε²)`; grouped window-gradient `o(ε)`; and microscopic nonempty D24 source-class membership.

Thus ML3's surviving burden is exactly the complementary/orthogonal-current sub-obligation of `(COMP-HS)`, not the whole residual gap.  The lanes are consistent because `ml3/reconciliation.md:76-80` calls it the “analogous burden” and does not claim to discharge the other components.  The narrow whole-datum D29 value needs neither; the Ward-derived component theorem needs all of `(COMP-HS)`.

## 2. D31 one-magnon kernel versus the Mq-E enumeration

The registers are compatible but disjoint.

- `ml1-ml6/ml1.md:207-271` concerns a delta-normalized generalized kernel for an exact translation-invariant one-magnon band over one D31 vacuum, with packet measure `dk/(2π)` and no kink sector.
- `mq-e/mq-e-proof.md:93-221,313-385` concerns the fixed-regularized-charge kink-plus-leg component of the easy-axis D16 model after `P_3` compression, unitarily mapped to a two-sided Jacobi path plus a side vertex.

The Mq-E tails have the ordinary Fourier/Jacobi `dk/(2π)` normalization and dispersions compatible with exact vacuum one-particle legs, but Mq-E neither assumes D31 nor turns its vacuum-band kernel into a kink-sector completeness theorem.  Conversely the D31 row says nothing about frozen-boundary wall enumeration.  No register, charge, measure, or DAG conflict occurs.  The two MAJOR defects in `verdict-ml1-ml6.md` affect only the proposed proof of `ML1-D31-kernel`, not Mq-E.

## 3. `scope-g` versus `spt-tpm`: windows, cuts, and D27 strength

The conventions are compatible specializations, not identical ledgers.

- `scope-g/compact-g-memory-scope.md:90-110,127-176` uses one fixed two-tail window `W=[a,b]`, one cut `c_0`, the same backgrounds at both times, and charges `Q_W^(j)=Σ_xC_{j,x}+s_j(a+b-1-2c_0)`.  It converts charge history to wall displacement by `δx_j=-(2s_j)^{-1}E[ν_j]`.
- `spt-tpm/spt-tpm.md:41-103,107-170` uses the boundary window `[0,L-1]` and the same unshifted normal-ordered charge `Q_L^∂=Σ_xS_x^z` at both times.  Its memory variable is charge change itself, `m=-ν`, so no wall-calibration factor appears.

Both use same-observable/same-window affine-offset cancellation before the spatial limit.  `scope-g` explicitly strengthens scalar D27 to a joint PVM, joint-dephasing, `ℓ¹`-tight vector law; it also says scalar D27 supplies only marginals.  `spt-tpm` proposes a single-charge boundary analogue in D22 and assumes E-LR2--E-LR3, using LR1-GEN only for the common sequence.  Neither silently edits live D27 or claims that scalar D27, H-AD-G, H-AD-edge, or phase stability supplies the stronger relaxation clauses.

## 4. `la-folium` implementer versus the Ogata separation claim

They are consistent and concern different spatial implementations.

- `la-folium/folium-implementer.md:107-344` constructs the global selected-circle implementer in the irreducible GNS representation of one fixed bare A2 kink by proving local normality of its circle orbit.  It needs neither a split half-chain factor nor a gapped invariant ground state.
- `ogata/ogata-map.md:75-101` separates that whole-chain/folium level from the split half-chain projective implementer and the finite MPS edge register.  Its map is `u_R(g)→V_C(g)→Q_edge` under H-split, explicitly not `u_R(g)=exp(iθQ̂_{W,c_0})`.

The la-folium theorem upgrades the concurrent candidate mentioned at `ogata-map.md:58`, but it does not prove Ogata's external literature premises, H-split, an SPT `H²` classification, D27, or convergence of window charges.  Its restriction to the one-parameter group is rephased to an honest `ℝ` representation; this does not trivialize a full-group half-chain SPT cocycle.  Both lanes retain the REFUTED bare-window/sector-wide route.

## 5. PATCH anchor audit on the current live tree

All string anchors not listed below match exactly once in their stated target.  No anchor double-matches.  `scope-g` has no `PATCH.md`.  Proposed new destinations `theory/spt-tpm.md`, `theory/mq-e.md`, and `theory/checks/mq_e_check.py` are absent, as required for copy/install steps.

### Misses or non-current anchors

- `ml1-ml6/PATCH.md:30`: the replacement `ML1` row used as the next insertion anchor has count 0 at the current tree; it becomes unique only after PATCH §1 is applied.  This is transactionally valid only if the orchestrator applies the sections in order.
- `ml1-ml6/PATCH.md:46-59`: the `theory/TRIANGLE.md` ML1/ML6 edits and the notation insertion say only “ML1 row”, “ML6 row”, and “near the existing D31 notation block”; they supply no exact string anchor.  The live obligation rows are at `theory/TRIANGLE.md:265,270`, and an exact neighboring notation row must be named before mechanical application.
- `m-esc-nr/PATCH.md:58`: exact endpoint `and is not proved in this shard.` has count 0.  The live paragraph ends with the unique `not proved in this shard.` at `theory/ace-ld.md:1154` (without “and”).
- `la-folium/PATCH.md:11`: the full terminal sentence has count 0 as a contiguous string because the live target wraps it between `theory/memory-index.md:305-306`.  Use the unique start `**Status: CONJECTURE.**  Claim row:` plus the following separator, or a multiline-aware anchor.
- `mq-e/PATCH.md:35`: `currently contains only a finite N=14 enumeration.` has count 0; live text contains code markup around ``N=14`` at `theory/memory-quantization.md:13`.
- `mq-e/PATCH.md:48`: the asserted exact Mq-E-assumption endpoint has count 0; live text wraps the sentence and code-quotes both ``N=14`` and ``corner-b-draft.md`` at `theory/memory-quantization.md:146-147`.
- `mq-e/PATCH.md:69`: exact sentence `**PROVE.**  Under Mq-E, H_3 satisfies D18` has count 0 because live text code-quotes ``H_3`` at `theory/memory-quantization.md:149`.
- `mq-e/PATCH.md:74`: `only after Mq-E is assumed.` has count 0 as a contiguous string because it is split across `theory/memory-quantization.md:261-262`.
- `mq-e/PATCH.md:84`: retained-sentence anchor `P_3H(1-P_3)≠0; five-wall and higher configurations are real` has count 0 because live text code-quotes only the formula at `theory/memory-quantization.md:263`.
- `mq-e/PATCH.md:91`: endpoint `memory-quantization.md §3 holds.` has count 0 because the live sentence code-quotes only the filename and spans `theory/corner-b-draft.md:282-284`.
- `mq-e/PATCH.md:101`: `with no free parameter.` has count 0 as a contiguous string because it is split across `theory/corner-b-draft.md:311-313`.
- `mq-e/PATCH.md:106`: `conditional on Mq-E identifying` has count 0 as a contiguous string because the phrase is split across `theory/corner-b-draft.md:356-357`.
- `mq-e/PATCH.md:108-110`: the instruction to replace the Mq-E-conditional label in the §6 status table supplies no exact string anchor.
- `mq-e/PATCH.md:119`: the claimed exact heading `### 3.3 Fano t(k) — ...` has count 0; the live heading uses code formatting, ``### 3.3 Fano `t(k)` — ...``, at `theory/TRIANGLE.md:374`.
- `mq-e/PATCH.md:130-132`: the preceding-ground-truth replacement anchor has count 0 in its displayed multiline form; the live phrase is split differently across `paper/main.tex:581-582`.

These are anchor-hygiene failures only; none changes the mathematical adjudications.  They must be corrected before a blind patch application.
