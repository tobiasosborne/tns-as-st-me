FAIL(MS-O1) — 0 FATAL / 1 MAJOR / 1 MINOR / 1 NOTE

# (MATCH-S) external hostile critic, round 1

## OBJECTIONS

### MS-O1 — MAJOR — C5 accepts a simultaneous reversal of both frozen P1 signs

**Exact quoted target.**  At `theory/proto-lsz-match.md`
`⟨1⟩12` the checker table says that PMLM-C5

> checks **P1 plus P2(a) only**: the two registered P1 slopes/signs and the
> D24(e) source-jet errors

and `⟨1⟩12.⟨2⟩3` says that the read values have

> common positive sign.

The implementation at `theory/checks/proto_lsz_match_check.py:193--202`
takes the absolute value of each slope and requires only
`len(set(p1_signs)) == 1`; it never requires either sign to be positive.

**Recomputation.**  I replaced both frozen P1 sign fields in memory by
`-1.0`, leaving both slope magnitudes and all P2(a) data unchanged, and called
`frozen_probe_gate(False)`.  It returned

```text
{'p1_errors': [0.003537592078453833, 0.02172648907659669],
 'p1_signs': [-1.0, -1.0],
 'p2a_errors': [4.282935914593823e-08, 5.4519119026157345e-08],
 'violated': False}
```

Thus a real D7-channel sign defect survives the advertised green gate.  The
public `--red-probe` mode does not expose this: it simultaneously changes the
P1 magnitude target and corrupts one P2(a) value, so C5 fails even though its
positive-sign subclaim is dead.  This is a checker-contract failure, not a
failure of the analytic orientation proof: PMLM-C4 independently kills
`S_phys -> S_phys^{-1}`, and the direct finite-ring recomputations reported
below select `S_phys`, not its inverse.

**FIX DEMAND.**  Require the two frozen signs to equal the registered positive
sign, and give the P1-sign and P2(a)-datum mutations independently reachable
red paths (or otherwise demonstrate each subcheck's survivor control).  Rerun
green and every public red under `python3 -O`.

**SURVIVING WEAKER STATEMENT.**  Current C5 certifies the two P1 slope
magnitudes, equality of their signs, and the two P2(a) source-jet errors.  It
does not certify that the common P1 sign is positive.  PMLM-C4 and the
analytic proof still establish the physical-channel orientation used by the
two proposed theorem rows.

### MS-O2 — MINOR — the shard mislabels its internal self-critique as the hostile round

**Exact quoted target.**  `theory/proto-lsz-match.md:12--13` says:

> The one hostile critic returned four MAJOR repair demands and no FATAL.

**Recomputation.**  The binding work order identifies those four demands as
an **internal self-critic** performed in the proposer's own context and says
explicitly that it does not count as the independent hostile round.  This
file is that independent round.  The four repaired proof steps were
nevertheless recomputed below and survive.

**FIX DEMAND.**  Replace “one hostile critic” by “internal self-critic” and
leave adjudication of this external verdict to the orchestrator.

**SURVIVING WEAKER STATEMENT.**  Four internal MAJOR repair demands were
incorporated before the independent critic round; this provenance correction
changes no theorem.

### MS-O3 — NOTE — the merge commentary says the bridge row cites a row it does not cite

**Exact quoted target.**  `theory/proto-lsz-match.md:799--801` says:

> The proposed bridge row cites it only as the on-shell endpoint whose
> connection has now been proved on `(D29-HS-SEP)`.

Here “it” is `S-IDX-HR-value-r2`, but the proposed
`S-IDX-MATCH-HS-SEP` cell at line 788 neither names that row nor includes it
in its dependency cell.

**Recomputation.**  This omission is actually the honest dependency graph.
The proof builds the model-specific two-body wave operators at `⟨1⟩3`, then
derives the fixed-time norm bridge at `⟨1⟩4`; it does not obtain the bridge by
re-labelling `S-IDX-HR-value-r2`.  At `S=1/2` both constructions reach D7's
same multiplier, while for `S>=1` the half-line Jacobi construction is new
model-specific work.  The proposed cell accurately cites the proof it uses.

**FIX DEMAND.**  Say that the *discussion* compares with the separate HR row,
not that the proposed row cites it.

**SURVIVING WEAKER STATEMENT.**  `S-IDX-HR-value-r2` remains separate and
unchanged; the new bridge theorem independently connects the D29 subclass to
the same on-shell multiplier.

## VERIFIED CORRECT

### 1. `(D29-HS-SEP)` does not beg `(MATCH-S)`

The load-bearing work done by `(SEP)` is spatial, not spectral.  The
hypothesis controls packet seminorms times the incoming and outgoing
collision-tail powers.  It contains `S_phys` only through bounded derivatives
needed for the ordinary multiplier estimate
`s_M(M_{S_phys}F) <= C(1+B_{M,epsilon})s_M(F)`; it contains no equality of a
D29 readout with an on-shell coefficient.

Independently recomputing the bridge gives the following chain.

1. `H_S I_S-I_SH_0` is supported on `r<=1`, because the separated
   two-magnon equation is free and the adjacent/double equations exhaust the
   remaining rows.
2. Incoming separation gives an integrable Cook tail, hence
   `I_SF_R-W_-^SF_R -> 0`.  Outgoing separation gives
   `e^{-iH_ST}W_+^SM_SF_R-I_SU_0(T)M_SF_R -> 0`.
3. `(W_+^S)^*W_-^S=M_{S_phys}` and equality of the selected scattering
   ranges give `W_-^SF_R=W_+^SM_SF_R`.  The triangle inequality therefore
   gives (PMLM.12), from the fixed-time charge vector to the outgoing
   multiplier.  No such equality is an assumption of `(SEP)`.
4. After the finite-ring approximation, the two independent errors satisfy
   `e_j^in,e_j^out=o(1)`.  With the ideal selected mass `D_j^0=1/2`, expansion
   of both numerator and denominator gives
   `|r_j-<x_j^0,y_j^0>/D_j^0| <=
   C(||e_j^in||+||e_j^out||)`.  The common free and translation phases cancel,
   leaving `int S_phys dnu_j`; total-variation control replaces `nu_j` by the
   actual D29 measure.  This is the constructed identification required by
   hard fence 4.

The finite-separation vector is never declared to be an HR creator or an
incoming eigenwave.  In particular the nonzero plane-wave branch mismatch is
retained.

### 2. The “exact” statement has the licensed ordered-limit scope

At finite `N_j`, (PMLM.17a) has a nonzero error bounded by the two Cook tails
and `eta_j`; the shard does **not** assert finite-ring equality.  At each
fixed `epsilon`, D29's outer limit sends `sigma_j,R_j,T_j,N_j` in the displayed
order/diagonal and makes that error zero.  Weak convergence of the same row
measures then gives

`A_*(epsilon)=int[S_phys-1]dmu_{*,epsilon}`.

Only after this equality is obtained for every fixed soft scale is
`epsilon downarrow0` taken.  Hence the difference is the zero function of
`epsilon`, which is indeed `o(epsilon)`.  No limit is interchanged and no
soft-uniform Cook bound is used.  This is exactly the outer-then-soft order
that proposed D29(6) actually takes.

### 3. The subclass is nonempty at finite parameters

A concrete uniform regular rectangle is available for every allowed `S`:
take `h_0=pi/2`, a standard nonzero `C_c^infty` bump for `g` supported in a
small neighbourhood of `h_0`, and the prescribed one-sided bump for `f` near
zero.  At `(k_s,h)=(0,pi/2)`, the regular-domain factors are
`a=b=1+i`, `ab=2i`, and

`z_2 mu-Sab=-2S != 0`.

Shrinking the supports preserves regularity and gives a positive velocity
gap.  Put `sigma_j=1/j`, `R_j=ceil(j^2)`, and
`T_j=2R_j/d_epsilon`.  For `M=8`, the `(SEP)` quantity is
`O_epsilon(j^{-3/2})`.  For each such finite packet/time tuple, fixed-time
thermodynamic convergence lets one choose a finite `N_j` satisfying the
sampling inequality, recollision bound, and `eta_j<=1/j`.  Thus the class
contains an explicit finite-ring sequence; its nonemptiness does not rest on
the conclusion being proved.

### 4. All four internal repairs survive recomputation

- **Finite-ring `eta_j`.**  The packet, translation, and time are fixed before
  `N_j` is chosen.  Plancherel periodization and finite-range dynamics then
  converge strongly, while the coordinate map and selected-row projection
  are contractions.  A diagonal finite `N_j` with `eta_j<=1/j` exists.
- **Canonical `J_S/Y_S` normalization.**  Direct ladder algebra gives physical
  off-diagonal coefficient `f_xg_y+f_yg_x` and double coefficient
  `sqrt((2S-1)/S)f_xg_x`.  The D29 coordinate map divides each of the two
  off-diagonal labels by `sqrt(2)`.  Therefore `I_S-J_S` and `C_SJ_S-Y_S`
  have exactly the separately tracked collision-row supports; neither error
  is silently identified with the other.
- **Cook constants and `(SEP)`.**  Differentiation gives
  `s_M(g_sigma)=O(sigma^{-M-1/2})`.  With `R=sigma^{-2}` and `L=R`, multiplication
  by the tail `R^{3-M}` gives `sigma^{M-13/2}`, which tends to zero at
  `M>=8`.  The constants may diverge with the soft scale because `epsilon` is
  fixed during this limit.
- **Two-error readout.**  Expanding
  `<x^0+e^in,y^0+e^out>/||x^0+e^in||^2` with
  `||x^0||^2=1/2` and the eventual lower bound `||x||^2>=1/4` yields the
  displayed linear bound in both errors.  The total-variation estimate for
  normalized square densities uses the same denominator lower bound.

### 5. Supplier and register fences are respected

- `S2-2body-S` supplies only the exhaustive two-body contact equations, the
  exact regular multiplier, its unitarity, and—only in `⟨1⟩10`—the unit-charge
  slope `sgn(v_h-v_s)/S`.  No endpoint, equal-velocity, composite-charge,
  many-body, or Bethe-completeness statement is consumed.
- The number `1/S` first enters after (PMLM.18), through (T.3)--(T.4).  The
  charge normalization `sqrt(2S)` cancels and is never read as
  `a_leg`; the AMP obstruction remains intact.
- No refuted ML4-Ward scalar formula is used.  The bridge uses neither the
  full-sector nor the highest-weight projection identity; the shard merely
  records their distinct registers.
- D29/D30 remain in MERGE PROPOSALS.  `(PROTO-LSZ)`, D24 class membership,
  microscopic `S_W(rho)` nonemptiness, and `a_leg` remain open.

### 6. Independent channel and checker runs

As an additional orientation check, I assembled the finite-ring Hamiltonian
directly from the local occupation equations, evolved separated charge
packets, and applied the D29 Fourier pairing.  At `S=1/2`, `N=256`, the
readout differed from the packet average of `S_phys` by `1.93e-3`, while its
difference from the inverse channel was `1.04`.  At `S=1`, `N=192`, the two
errors were `1.66e-3` and `5.94e-1`; the selected free mass was `0.4999` in
both runs.  This independently confirms the normalization and D7 orientation
used in (PMLM.17).

The advertised optimized checker runs were reproduced:

| run | exit | detecting gate |
|---|---:|---|
| green | 0 | none; `PMLM PASS` |
| `--red-charge-map` | 1 | PMLM-C1 |
| `--red-separation` | 1 | PMLM-C2 |
| `--red-readout` | 1 | PMLM-C3 |
| `--red-channel` | 1 | PMLM-C4 |
| `--red-probe` | 1 | PMLM-C5 |

The green metrics match the shard to rounding: C1 `7.85e-17`, C2 ratio
`6.37696e-3` and outgoing norm `1.89282e-5`, C3 `7.98e-17`, and C4
`2.53916e-5`.  Each registered red models a real defect.  C5 reads only the
P1 and P2(a) fields; `protocol_eta_diff` and `protocol_slope` from the known
P2(b) no-op path are never read.  MS-O1 is the only failed data-mutation
audit.

### 7. Merge-proposal lockstep

The `S-IDX-MATCH-HS-SEP` statement is exactly (PMLM.18): same finite-ring D29
readout, same row measure, and equality only after the fixed-`epsilon` outer
limit.  The `S-IDX-D29-value-HS-SEP` statement is exactly
(PMLM.19)--(PMLM.20), with the number supplied only by `S2-2body-S`.  Neither
cell claims finite-`N` equality, `(PROTO-LSZ)`, D24 membership, `a_leg`, an
HR-creator equality, or a result outside the displayed subclass.  There is no
silent strengthening in either direction.

The general rows `S-IDX-spec-struct-r2` and `S-IDX-spec-r2` must remain
**SKETCH**: the former still lacks `(PROTO-LSZ)`, and the latter still carries
the D24-VAL membership antecedent and quantifies beyond this subclass.
`S-IDX-HR-value-r2` also remains separate and unchanged.

## PROMOTABLE NOW

The analytic proof has no open FATAL or MAJOR.  After the mechanical MS-O1
checker repair is applied and rerun, and together with installation of the
displayed `(D29-HS-SEP)` refinement of the still-quarantined D29 proposal, the
following are the verbatim licensed cells.

```markdown
| S-IDX-MATCH-HS-SEP | For the fully polarised bilinear ferromagnet `H_S` at every `2S in N`, on the primitive regular two-magnon channel and the displayed separated-preparation subclass `(D29-HS-SEP)`, along every actual row-measure limit subsequence the fixed-time charge-created finite-ring D29 readout converges to `int S_phys dmu` for that same D29 row measure.  Thus `(MATCH-S)` holds with zero remainder (hence through `o(epsilon)`).  The proof uses a norm bridge from the fixed-time product to the incoming wave operator and then to the outgoing multiplier; it does not identify the finite-separation vector with an HR creator, does not require a soft-uniform Cook estimate, and proves no `(PROTO-LSZ)` component decomposition. | **PROVED** | D6--D8, D24(b), D29, S2-2body-S | theory/proto-lsz-match.md ⟨1⟩1--⟨1⟩6 | theory/checks/proto_lsz_match_check.py PMLM-C1--C5; finite corroboration only, with no wave-operator certificate |
| S-IDX-D29-value-HS-SEP | Under `(D29-HS-SEP)`, along every actual row-measure limit subsequence the primitive fixed-time D29 scalar datum obeys `A_*(epsilon)=i sgn(v_h-v_s)bar k_*(epsilon)/S+O(epsilon^2)` and phase slope `sgn(v_h-v_s)/S`.  The value enters only after S-IDX-MATCH-HS-SEP through PROVED `S2-2body-S`.  This row makes no claim about `a_leg`, D24 class membership, `(PROTO-LSZ)`, endpoints, equal velocities, composite charges, or other protocol classes. | **PROVED** | S-IDX-MATCH-HS-SEP, S2-2body-S | theory/proto-lsz-match.md ⟨1⟩10 | theory/checks/proto_lsz_match_check.py PMLM-C4 plus frozen P1+P2(a)-only C5 |
```

No promotion of `S-IDX-spec-struct-r2`, general `S-IDX-spec-r2`, or
`S-IDX-HR-value-r2` is licensed by this round.

## REPAIR ORDER

1. Repair PMLM-C5 exactly as MS-O1 demands: enforce the registered positive
   P1 sign and independently exercise the P1-sign and P2(a)-datum rejection
   paths.  Verify a simultaneous negative-sign data mutation exits nonzero,
   and verify each survivor control exits zero rather than being masked by a
   second mutation.
2. Rerun the checker green and all repaired public reds under `python3 -O`;
   preserve the P1+P2(a)-only fence and do not read any P2(b) field.
3. Correct the two sentence-level lockstep items MS-O2 and MS-O3.  Make no
   change to `(SEP)`, the wave-operator bridge, the ordered-limit argument,
   the value chain, D24/AMP, or the scopes of the three existing spectral/HR
   rows.
4. The orchestrator may then install `(D29-HS-SEP)` and merge only the two
   PROVED cells above.  Keep `(PROTO-LSZ)` and the general D29 law at SKETCH.

FAIL(MS-O1)
