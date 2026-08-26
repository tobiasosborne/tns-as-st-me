<!-- ROLE: L6 proposer response to theory/verdicts/corpus-r2.md.
     Date: 2026-08-26.  This is not a critic verdict. -->

# Proposer repair response — corpus r2

This round applies exactly the promotions adjudicated in `corpus-r2.md`,
repairs N1--N7, sweeps N8--N10, and leaves every adjudicated HOLD at its prior
L5 status.  The parent SPT rows remain SKETCH awaiting focused critic r3; only
the two narrow critic-requested SPT splits are promoted.

## Objection dispositions

| id | disposition | repair and evidence |
|---|---|---|
| **N1** | **REPAIRED** | D20 now defines the Hermitian partial charge `Q^H=-iQ`; the dual-left orientation gives the centered residue `Q_edge=-i[X_C-tr(rX_C)I]`.  D21 restates the spectrum as `q_{ω,C}^∘+ℤ`, invariant under lift rephasing.  S-C6 checks anti-Hermiticity/Hermiticity and centering.  `--red-gauge` uses `V(exp εξ)→e^{0.37iε}V(exp εξ)` and exits `1` with an uncentered error `0.370`. |
| **N2** | **REPAIRED** | D20, `Sd4'`/`Sd6'`, and SPT-B' B2 now require external tensors, channel embeddings, tangent gauge fixes, Gram normalizations, and differentiated profiles to be continuous, respectively `C^p`, in the path parameter.  The parent remains SKETCH awaiting r3. |
| **N3** | **REPAIRED** | ML4 (15)--(17) are explicitly an off-shell analytic interpolation at fixed periodic `N`.  The formal inner `k→0` limit is not called on-shell.  The physical packet-smeared infinite-volume estimate remains open at `tns-7ut`; ML4 stays SKETCH. |
| **N4** | **REPAIRED** | D19--D21 distinguish the Schmidt/edge register `E_C=ℂ^χ` from the padded-window matrix module `𝓜_χ(C)≅M_χ(ℂ)≅E_C⊗E_C^*`.  Left multiplication acts on the first factor, hence `𝓜_χ(C)` is exactly `χ` copies of the `E_C` projective action.  H-split is formulated only for `E_C`; the `d_ω` bound is retained. |
| **N5** | **REPAIRED** | D4, SPT-D', CLAIMS, and TRIANGLE now say that the infinitesimal central cocycle is cohomologically trivial and can be gauged away.  The ordinary bracket is displayed only in the phase convention where the coboundary has been removed; no claim of section-independent vanishing remains. |
| **N6** | **REPAIRED** | Each SPT DAG cell contains one L5 status.  Every physical SPT-D' surface carries both H-split and H-dress.  D23 narrows the dynamical conjecture to `H_{A,+}^{dyn}=Σ_{x≥0}P^{(S=2)}_{x,x+1}` and identifies the exact boundary-magnon term `h_{mag-edge}=P^{(S=2)}_{0,1}`.  SPT-M'-dyn remains CONJECTURE with wave operators, H-AD-edge, the on-shell matrix, and nonvanishing still missing. |
| **N7** | **REPAIRED** | TRIANGLE §6.2 now says exactly: “whether the zero and coefficient are universal remains CONJECTURE.”  C⇒B remains a SKETCH at conditional bookkeeping scope. |
| **N8** | **REPAIRED** | Notation overload 8 now distinguishes bare SPT transfer `E_b` from the bound energy `E_b(K)` by argument/scope.  Overload 11 makes D7/ML2-local separation `r:=y-x` the sole exception to bare transfer fixed-point `r`; reflection remains `r(k)`. |
| **N9** | **REPAIRED** | B3 ⟨1⟩1 now approximates both `α_t(D)` and `α_t(O)` by local observables, gives the two-factor norm estimate, takes the D9(a) factorized limit, and only then removes the approximation.  B3 is promoted as adjudicated. |
| **N10** | **ACCEPTED NOTE, scope recorded** | The new S-C6 covers Hermiticity and phase-gauge centering.  ML4-Q1 continues to expose the nonuniform physical sequence.  The checkers still do not prove H-split, H-AD-edge, Mq-E, full-chain leakage control, or an infinite-volume on-shell ML4 theorem; no row claims that they do. |

## Promotions applied

All `proved in` cells in the DAG record “PROVED per corpus-r2.md
adjudication,” and TRIANGLE §7 is synchronized.

| claim/item | applied status | scope preserved |
|---|---|---|
| S2-2body | **PROVED** | Exact two-body multiplier/phase expansion only; S-general untouched. |
| ML4-A | **PROVED** | Abstract matching-plus-`C^1` cancellation lemma. |
| ML4-Ward | **PROVED** | New DAG split for exact finite-sector projection (8)--(11). |
| ML5-A | **PROVED** | Two-condition Banach-Taylor iff with stated norm hypotheses. |
| ML5-B | **PROVED** | Conditional implication only; microscopic membership/nonemptiness stays open. |
| M-flux | **PROVED** | Exact finite-time physical-current identity. |
| K1 | **PROVED** | Positive `2×2` block and kernel. |
| K2 | **PROVED** | Product factors lie in K1's kernel. |
| K3 | **PROVED** | Boundary field is invisible to the quasi-local derivation. |
| B3 | **PROVED** | Finite-time label rigidity plus D18 event bookkeeping; no torsor reconstruction. |
| Mq-AD3 | **PROVED** | Conditional on Mq-E. |
| M-quant | **PROVED** | Conditional on D18. |
| M-tk | **PROVED** | Conditional on Mq-E for the displayed Fano graph; universality/full-chain accuracy unproved. |
| SPT-B-mult | **PROVED** | Critic-requested split: closed multiplier cancellation only. |
| SPT-E-AKLT | **PROVED** | Critic-requested split: exact AKLT-family contraction only. |

## Holds retained

| item | status retained | named missing step |
|---|---|---|
| ML4 one-hard application | SKETCH | On-shell packet-smeared infinite-volume estimate; fixed-ring formulas are off-shell. |
| N2 empirical scan | SKETCH | Numerical evidence is not a spectral theorem. |
| SPT-B' | SKETCH | N2 repaired; focused critic r3 has not verified the parent. |
| SPT-E' | SKETCH | N1/N4 repaired; focused critic r3 has not verified the parent. |
| SPT-T' | SKETCH | Repaired endpoint convention and physical hypothesis lockstep await r3. |
| SPT-D' | SKETCH | Whitehead/H-dress repairs await r3. |
| SPT-M' | SKETCH | The repaired centered SPT-E' charge input awaits r3. |
| SPT-M'-dyn | CONJECTURE | Half-chain wave operators, H-AD-edge, on-shell reflection matrix, and nonvanishing. |
| C⇒B | SKETCH | Conditional graph/bookkeeping only; universality remains conjectural. |
| B⇒A | SKETCH | B3 is proved, but memory has not been shown to reconstruct an asymptotic-symmetry action/classifying datum. |
| S-general | CONJECTURE | ML1, ML3, infinite-volume ML4, ML4-3, microscopic `𝒮_W` membership, and ML6. |

## L4 and checker sweep

Corner-C `𝖲` now has the numbered single-source home D25; notation and
S-general point to it.  The SPT merge snapshot inside `spt-rebuild.md` is
explicitly marked superseded/non-normative.

Optimized green suite:

```text
for checker in theory/checks/*.py; do python3 -O "$checker"; done
8/8 scripts exited 0
```

Red mutations:

```text
mquant_check.py --red                 exit 1  (continuity residue 2.340e+00)
ml4_check.py --red-uniform            exit 1  (k=2π/N nonuniformity detected)
spt_rebuild_check.py --red            exit 1  (edge sign error 1.333e+00)
spt_rebuild_check.py --red-gauge      exit 1  (uncentered gauge error 3.700e-01)
```

`rg` finds no bare Python `assert` in `theory/checks/`, and `git diff --check`
passes.
