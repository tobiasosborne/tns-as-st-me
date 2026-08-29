# Anchored merge instructions for SPT-TPM

All edits below target live files outside this lane and must be applied by the
orchestrator.  Do not use line numbers.

## 1. Add the proof shard

Copy this lane's `spt-tpm.md` verbatim to the new live file
`theory/spt-tpm.md`.  This is the ground-truth Lamport proof for the proposed
`SPT-M'-TPM-fin` and `SPT-M'-TPM-spec` claims.

## 2. Extend `definitions.md` D22

Anchor: in `## D22 (twists, ordered endpoint products, and edge memory)`,
find the exact sentence ending the endpoint-product paragraph:

> Ordered endpoint-soft operators obey
> `𝕊(h)𝕊(g)=e^{iω(h,g)}𝕊(hg)` in the registered module.

Insert immediately after it:

```markdown

For the channel-free operational register, use D19's boundary windows
`f_L^{edge}=1_[0,L-1]` and D20's local Hermitian charge
`Q_L^∂:=Q^H[f_L^{edge};ξ]`.  Let `E_{L,t}` be the spectral resolution of
`α_t^+(Q_L^∂)`.  The boundary two-projective-measurement (TPM) law records
`ν=q_-−q_+` and the edge-memory change `m=q_+−q_-=-ν` with
`p_{L;t_-,t_+}(ν):=Σ_q||E_{L,t_+}({q−ν})E_{L,t_-}({q})Ψ||²`.
Hypothesis **(E-LR)** means: (1) one common sequence `T_n→∞` gives, for every
fixed `L`, weak-* limits of the positive/negative Cesàro states and limits of
all double-Cesàro TPM weights; (2) with
`𝒟_{L,t_-}(A):=Σ_qE_{L,t_-}({q})AE_{L,t_-}({q})`, the double-Cesàro average
of `⟨Ψ,[𝒟_{L,t_-}(Q_L^∂(t_+))−Q_L^∂(t_+)]Ψ⟩` tends to zero for every fixed
`L`; and (3), writing `p_L` for the fixed-window time limit,
`lim_{M→∞}sup_LΣ_{|ν|>M}(1+|ν|)p_L(ν)=0`.  Optionally one may require
`p_L⇒p`; this selects a unique limit law and first moment.  Dynamics is formed
first, fixed-`L` time limits second, and `L→∞` last.  This operational law is
distinct from the channel operator below and assumes no wave operator or
channel inventory.
```

Anchor: the next paragraph begins exactly:

> Under (H-AD-edge), asymptotic total charge decomposes as

Keep that paragraph, but append this exact sentence to its end:

```markdown
This is an optional channel corollary; neither (H-AD-edge) nor this channel
operator is part of the operational TPM theorem SPT-M'.
```

## 3. Extend `notation.md`

Anchor: the row beginning exactly:

> | `ΔQ_edge`, **(H-dress)**, **(H-AD-edge)** |

Insert immediately before it:

```markdown
| `Q_L^∂`, `p_L(ν)`, `r_L(m)`, **(E-LR)** | D19 boundary-window Hermitian charge; escaped-charge TPM law; reflected edge-memory-change law `m=-ν`; common-Cesàro/dephasing/first-moment-tight boundary relaxation | definitions.md D22, theory/spt-tpm.md |
```

## 4. Replace the current theorem in `theory/spt-rebuild.md`

Start anchor:

> ### ⟨2⟩1. Conditional charge-bookkeeping theorem

End anchor (exclusive):

> ### ⟨2⟩2. What “protected edge magnon memory” can honestly mean

Replace the entire block between those anchors with:

```markdown
### ⟨2⟩1. Channel-free boundary TPM theorem

**ASSUME.**  D19's boundary windows, D20's Hermitian normal-ordered charge,
D26(INT), strongly continuous half-chain automorphic dynamics, a unit
preparation, and D22(E-LR) for the ordered-limit clause.

**PROVE.**  At every finite `L`, the explicit TPM protocol measuring the same
`Q_L^∂` at both times has memory outcome `m=q_+−q_-∈ℤ`.  Under (E-LR), every
ordered limit-point law `r` is a probability on `ℤ` and, along that
subsequence,
`Σ_m m r(m)=lim_j[ω^+_{L_j}(Q_{L_j}^∂)−ω^-_{L_j}(Q_{L_j}^∂)]`.
No commutativity of the two Heisenberg observables, H-split, H-AD-edge,
wave operator, channel inventory, definite channel charge, or charge
conservation is used.  D21(H-split)+SPT-E' add only the physical
projective-edge/capacity interpretation; D10 conservation optionally
interprets the mean as current flow.  Expectations need not be integers.

**⟨3⟩1.**  The finite support statement is `theory/spt-tpm.md` ⟨1⟩1.
**Justification:** D19--D20, D26, M-INDEX-fin.

**⟨3⟩2.**  The ordered law and mean ledger are `theory/spt-tpm.md`
⟨1⟩3--⟨1⟩4.  **Justification:** D22(E-LR), M-INDEX-spec, LR1-GEN.

**⟨3⟩3.**  The hypothesis deletion and SPT interpretation are
`theory/spt-tpm.md` ⟨1⟩6--⟨1⟩7.  **Justification:** D21--D22 and SPT-E'.

**⟨3⟩4. QED.**  The former H-AD-edge bookkeeping theorem is retained as the
following optional channel corollary, not as SPT-M'.

**OPTIONAL COROLLARY `SPT-M'-ch` (the former `SPT-M'`, unchanged in
strength).  ASSUME** H-split, H-AD-edge, conservation of the chosen `U(1)`
charge, and asymptotic channels with definite bulk and edge charges.
**PROVE** on every channel
`ΔQ_edge=-(Q_bulk,out-Q_bulk,in)`; its fixed-system channel differences are
integral, and for the restricted AKLT doublet they lie in `{-1,0,+1}`.

**⟨3⟩1.**  By H-AD-edge,
`Q_tot=Q_edge+Q_bulk` on both asymptotic channel spaces.
**Justification:** D22(H-AD-edge).

**⟨3⟩2.**  Conservation and rearrangement give the identity.
**Justification:** D10(a)--(b) and the assumed `U(1)` conservation law.

**⟨3⟩3.**  Both edge eigenvalues lie in
`q_{ω,C}^∘+ℤ`, whose difference is integral; restricting to the AKLT
doublet gives `{-1,0,+1}`.  **Justification:** SPT-E'(iii).

**⟨3⟩4. QED.**  This is exactly the former proof and retains its PROVED
conditional status.

```

In the immediately following `SPT-M'-dyn` paragraph, replace the exact
two-line string:

> reflection matrix element is nonzero on an open momentum interval, and the
> post-selected memory obeys (6.1).  The exact missing step is a half-chain

with:

> reflection matrix element is nonzero on an open momentum interval, and the
> resulting boundary-window history is tested by the SPT-M' TPM protocol.
> H-AD-edge remains a separate conjectural input for the scattering-channel
> identification.  The exact missing step is a half-chain

## 5. Replace the `claims/CLAIMS.md` row `SPT-M'`

Anchor: the complete table row beginning exactly `| SPT-M' | Given H-split,`
and ending with `| dynamical follow-on tns-cpq |`.

Replace it with this single row:

```markdown
| SPT-M' | For D19's boundary windows and D20's Hermitian normal-ordered charge, D26(INT) implies that the explicit TPM memory change `m=q_+−q_-` is in `ℤ` at every finite `L`, because the same-window spectral offset cancels; no commutativity of the two Heisenberg observables is assumed.  Under additionally D22(E-LR2--E-LR3), with the common sequence supplied by LR1-GEN, every ordered limit-point law is a probability on `ℤ` and its first moment is the ordered boundary-window charge change along that subsequence.  D21(H-split)+SPT-E' add the physical projective-edge/capacity interpretation only.  No H-AD-edge, wave operator, channel inventory, definite channel charge, nonzero amplitude, or permanence is assumed or proved; conservation is needed only for current-flow semantics. | SKETCH | D19--D22, D26, M-INDEX-fin, M-INDEX-spec, LR1-GEN, SPT-E' | theory/spt-tpm.md ⟨1⟩1--⟨1⟩7; PROVED-candidate pending capped L6 | finite arithmetic inherited from the red-capable M-INDEX-fin checker; no gate bears on E-LR2--E-LR3 |
```

Insert immediately after that replacement row:

```markdown
| SPT-M'-ch | Given H-split, H-AD-edge, charge conservation, and definite channel charges, `ΔQ_edge=-(Q_bulk,out-Q_bulk,in)` and fixed-system channel differences are integral; for the restricted AKLT doublet they lie in `{-1,0,+1}`.  This is the former SPT-M' statement, retained unchanged as an optional channel corollary. | PROVED | SPT-E', D22, M-quant bookkeeping | theory/spt-rebuild.md ⟨1⟩6.⟨2⟩1 optional corollary; conditional status inherited from corpus-r3.md adjudication of former SPT-M' | dynamical follow-on tns-cpq |
```

Do not change the `SPT-M'-dyn` status.  Its explicit `H-AD-edge` dependency
remains because it is a scattering/nonvanishing conjecture, whereas the new
`SPT-M'` is the operational charge-history theorem.
