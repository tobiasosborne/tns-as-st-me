<!-- ROLE: L6 critic verdict, round 3 (adjudication), on the revised Corner-A package.
     Critic: Codex. Date: 2026-08-25. -->

# Critic verdict r3 — Corner A (adjudication)

Critic: Codex, adversarial adjudication under L6/L6b.  I treated
[`corner-a-r1.md`](corner-a-r1.md) and [`corner-a-r2.md`](corner-a-r2.md) as my
own prior verdicts and checked the nine r2 dispositions against the revised
`definitions.md`, `notation.md`, `claims/CLAIMS.md`, and all four Corner-A
shards.  I independently re-derived the two requested bug repairs, probed the
descent in D9(c′)2, audited the negative rows and the two deliberately untouched
drafts, and re-ran `python3 theory/checks/corner_a_check.py`: all **18** named
checks C0, C1, C1b, C1c, C2, C2b, C3, C3b, and C4--C11 pass.

The r3 revision reaches a fixed point.  The padding hypothesis is sufficient
and its injectivity proof is valid; G0(c) now has the missing right-edge
coefficient; D12 separates remainder convergence, summable packets, and
delta-normalised plane waves; and D9(c′)2 really does descend.  No retracted or
refuted result has re-entered a PROVED row.  The residue is limited to several
overstatements in summary/notation prose and one harmless conjugation typo in
the CP proof.  None invalidates WI, A1 on its stated padded windows, A2, or G0.

## Independent recomputations

### Padding and injectivity (r2 objection 1)

Let `p` and `q` be the numbers of sites to the left and right of the chosen
bond.  If `p,q >= n_0` and `b_l,b_r != 0`, then `iota(M)=0` says

`b_l^dagger P(s) M Q(t)b_r=0`

for every pair of physical words.  The length-`p` and length-`q` words each
span `M_chi`; bilinear extension therefore gives `v^dagger M w=0` for all rows
`v^dagger` and columns `w`, because `{b_l^dagger P}` and `{Qb_r}` exhaust the
two dual spaces.  Thus `M=0`, so `iota` is injective and
`iota o L_N o iota^{-1}` is a well-defined linear operator.  No invariance of
a nonzero kernel is being assumed.

I also reproduced the adversarial tensor from r2.  With one site on each side,
`iota(N)=0` while `||iota(ZN)||_infty=4`; with the sufficient `2|2` padding its
rank is `4=chi^2`.  Check C8b additionally reports rank `4` already for `2|1`.
Consequently padding on both sides is a **sufficient uniform hypothesis**, not
a logically necessary condition for every particular tensor/window.  This is
the minor wording defect recorded below; it does not affect A1(d1), which
assumes the sufficient hypothesis.

### Boundary-term-corrected G0(c) (r2 objection 3)

Put `q=e^{ik}` and `X=X_alpha(xi)`.  From

`B_G=N_k(X)+(1-q)A_alpha X`

and Lemma SBP(ii), direct finite reindexing gives

```
Phi_k^Lambda(B_G)
 = (1-q) sum_{m=a}^{b} q^m |psi;X@m>
   + q^(b+1)|psi;X@b> - q^a|psi;X@(a-1)>.
```

The coefficient on the right edge is
`(1-q)q^b+q^(b+1)=q^b`, so the equivalent combined form is exactly

```
(1-q) sum_{m=a}^{b-1} q^m |psi;X@m>
 + q^b|psi;X@b> - q^a|psi;X@(a-1)>.
```

These are the two r3 displays.  On the Pauli tensor with `L=4`, `k=0.37`, and
`X=K`, I again obtain the old discrepancy `0.4505862126`, equal to the norm of
the omitted `(1-q)q^b|psi;X@b>` term, while the corrected and combined forms
have errors `5.89e-17` and `3.9e-17`.  The repair is exact.

## Disposition of the nine r2 repairs

| r2 # | r3 adjudication |
|---|---|
| 1 | **FIXED in substance.** D4(a1)--(a4) gives a sufficient padding hypothesis, proves `iota` injective by two independent word spans, and transports left multiplication to the physical window-vector space.  The unpadded counterexample is genuine.  Only the universal word “necessary”/“iff” is too strong (minor 1). |
| 2 | **FIXED.** A1(d3) and D9(c′)3 now say exactly that `[omega_alpha]` obstructs rephasing the projective lift into an honest `G -> U(chi)` homomorphism; it does not obstruct the always-existing projective window action. |
| 3 | **FIXED.** Both uncombined and combined finite-window forms of G0(c) have the correct `m=b` contribution and right-edge coefficient, as re-derived above. |
| 4 | **FIXED in substance.** D12(a) is remainder-only for `c_0`; D12(a′) uses `ell^1 cap BV` for absolute wave-packet tails; D12(b) uses only the `O(1)` boundary upper bound after `|Lambda|^{-1/2}` normalisation.  The false bulk `Theta(sqrt(|Lambda|))` lower/growth assertion and the fixed-`k`/`c_0` conflation are gone.  Some summary prose still overstates the common norm register (minor 3). |
| 5 | **FIXED in substance.** A1 carries the scalar iff, A2 carries (T), G0 separates the finite-window, packet, and current quantifiers, and B3 no longer depends on the refuted `A2-orbit-r1` label.  Two compressed-row phrases are not literally quantifier-exact (minors 1--2). |
| 6 | **CONCEDED and correctly recorded.** The two out-of-scope drafts remain untouched and are precisely tabulated in corner-a-pitfalls.md Flag 6.  Their stale uses are not imported back into a Corner-A PROVED claim. |
| 7 | **FIXED.** D9(c) contains only the endpoint set and representative formula; D9(c′) records consequences of A1, and A1 does not assume those consequences.  The invited descent probe succeeds below. |
| 8 | **FIXED in substance.** The finite restriction is a positive CP contraction, not a rank-one boundary-vector state; consistency uses the two fixed environments.  C11 passes.  The displayed definition of `T` misses a complex conjugate, but the positivity argument itself is valid (minor 4). |
| 9 | **FIXED.** The old `V(g)^{-1}` and `mathcal A`-as-group conventions are visibly marked superseded, and the active notation points to `V(g)` and `mathcal A_eff`/the double-coset classification. |

## Invited probe — D9(c′)2 descends

There is no adversarial example analogous to r2 objection 1.  By A1(c), the
fibres of `GL(chi) -> E_b^alpha` are **exactly** scalar lines:
`M ~ M'` iff `M'=cM`, `c != 0`.  Therefore

`V_alpha(g)M' = c V_alpha(g)M`,

so left multiplication preserves every fibre.  Rephasing the chosen virtual
representative, `V_alpha(g) -> lambda(g)V_alpha(g)`, also changes the result
only by a scalar.  Finally,

`h star (g star [M]) = [V_alpha(h)V_alpha(g)M] = [V_alpha(hg)M]`

by Lemma IT; the cocycle phase disappears in the projective class, and the
identity acts trivially because `[V_alpha(e)]=[1]`.  Thus `star` is a genuine
well-defined `G`-action on `E_b^alpha`, with kernel precisely `N_alpha`.  The
r2 window disease involved a larger, non-invariant kernel of `iota`; here the
only equivalence is scalar, and scalar lines are invariant under all left
multiplications.

## Retraction and quantifier audits

The in-scope search for “Adler zero”, “universal soft”, “contact term”,
“A-orbit”, and edge-Hilbert-space language finds those expressions only in
historical corrections, explicit negative statements, conditional targets, or
the REFUTED/RETRACTED rows.  `A2-orbit-r1` remains REFUTED and `G0-soft-r1`
remains RETRACTED.  B3 is SKETCH, requires (T), and uses the vacuum-pair/double-
coset statement.  The known stale statements in `spt-scoping-draft.md` and
`corner-b-draft.md` remain quarantined by Flag 6 as the proposer promised.

WI and A2 match their proofs quantifier-for-quantifier.  A1's operative theorem
quantifiers also match once “padded” is read as its stated sufficient
hypothesis.  G0's detailed theorem and its finite-window formula match.  The
following summary-row wording should be cleaned up, but it does not change the
proved theorem statements.

## Numbered r3 residue

### 1. MINOR — “padded iff/necessary” is stronger than the proof and its own check

**Locations:** A1(d1), the A1 claims row, D4(a3), `notation.md` row for `iota`.

The proof establishes `p,q >= n_0` as a sufficient tensor-independent
hypothesis.  It does not establish necessity.  Indeed C8b itself gives
`rank(2|1)=4` with `n_0=2`: that window is not padded on both sides but `iota`
is injective.  Replace “padding is necessary”, “the unpadded action is ill
defined”, and “injective iff padded” by “without padding, injectivity is not
guaranteed; the displayed counterexample is ill defined”.  A1(d1)'s restricted
positive assertion remains proved.

### 2. MINOR — the compressed G0 row does not scope part (b) literally

**Location:** `claims/CLAIMS.md` row G0.

The row prefixes “(a),(b)” by `xi in h_alpha, normal ordered`.  The proof's
quantifiers are instead: (a), (c), and (d) use `xi in h_alpha` and normal
ordering; (b) quantifies over `xi in g` and says
`B_G(xi) in ran N_0 + C A_alpha` iff `xi in h_alpha`; (e) uses every
`xi in g`.  The row's parenthetical broken-case language signals the intended
statement, but it should split (b) out explicitly to be quantifier-exact.

### 3. MINOR — D12 summary prose still blurs the common norm register

**Locations:** D12(a′), corner-a-pitfalls.md section 5.2(ii), `notation.md`
rows for `c_0` and `ell^1 cap BV`.

D12(a) correctly proves only `||B_Lambda|| -> 0` for `c_0`.  The notation row
still calls `c_0` “the class in which the gauge identity is exact”, and the
pitfall shard says the identities hold “exactly in norm” for `c_0`, contrary to
the new remainder-only qualification.  For `ell^1 cap BV`, the triangle
inequality gives absolute tail control once all insertion vectors have been
placed in a common GNS/sequence space; finite-window vectors for varying
`Lambda` do not themselves form one normed space.  D12(a) acknowledges that
the GNS/split register is still SKETCH, so D12(a′)'s title “norm-convergent”
should either state that register/assumption or be phrased as a uniform
absolute-tail estimate.  This does not affect the exact finite-window SBP
identity, the corrected G0(c) display, or D12(b)'s normalised remainder bound.

### 4. MINOR — the CP positivity proof defines `T` with the wrong conjugation

**Location:** D1(e′), positivity leaf.

For the displayed density-matrix convention,
`c^dagger rho c = tr[l T r T^dagger]` with
`T = sum_s conjugate(c_s) P_W(s)`, not `T = sum_s c_s P_W(s)`.  Since complex
conjugation is a bijection on the coefficient vectors, the Gram/CP positivity
conclusion is unchanged; this is a literal formula typo, not a defect in the
construction.

## Surviving r3 result

The package proves WI with the corrected edge/window quantifier; A1's endpoint
bijection, state action, stabiliser/orbit, and twisted-algebra action on the
stated padded windows; A2's pointwise weak-* sector jump and its (T)-qualified
double-coset classification; and G0's corrected finite-window identity,
normalised remainder statement, and finite-range continuity equation.  The
GNS charge-algebra realisation, continuum-vacuum uniformity, and soft theorem
remain explicitly SKETCH/RETRACTED and are not silently used.

PASS
