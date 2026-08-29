# Joint-critic verdict: `ml1-ml6`

## Scope adjudicated

I checked the proposed `ML1`, `ML6-HS-SEP`, and `ML1-D31-kernel` rows separately.  I recomputed the half-line bound vector, continuum/bound gap, overlap derivative, scattering multiplier, and channel-map adjoint identity against `ML2`; I also reran the checker green and with `--red-bound` and `--red-unitarity`.  The exits were respectively 0, 1, and 1.

## FATAL

None.

## MAJOR

- `ml1.md:213-263` proves more than its ASSUME register licenses.  The ASSUME line at `ml1.md:213` binds only D31(1)--(2), but `ml1.md:257-263` uses the filtered-creator equality and packet-window facts of D31(3)--(4) to identify the generalized kernels with the wave-operator external legs.  The exact broken step is the inference at `ml1.md:257-261`; it is not a consequence of D31(1)--(2).  Proposed row `ML1-D31-kernel` must explicitly assume full D31 for that last identification, or split the spectral-kernel theorem from the creator-leg corollary.
- `ml1.md:213-255` chooses the global rigging `C^∞(𝕋;ℂ^m)` and then writes the transpose eigen-equation `H|k,b⟩=ω(k)|k,b⟩`.  D31(2), however, assumes globally only `ω∈C²(𝕋)` (`definitions.md:1329`); multiplication by such an `ω` need not preserve `C^∞`, so the asserted rigged action of `H` on `Φ_M=Γ_MC^∞` is not defined by the displayed construction.  Replace the global rigging by an invariant evaluation-continuous space such as `C²` (or restrict to D31(4)'s locally smooth packet neighborhoods and state a local kernel).  Until that repair, the D31-kernel row lacks a valid proof of its eigen-distribution clause.

## minor

- `ml6.md:152-164` compresses the finite-path-to-half-line spectral-projection argument into one paragraph.  The conclusion is standard at fixed packet index, but the merge should retain all three fences used there: `N→∞` first, packet-window boundaries of zero limiting spectral measure, and the singular finite-ring completion.  It must not be paraphrased as uniform convergence in the later `σ↓0` or `ε↓0` limits.

## note

- `ml1.md:57-205` validly upgrades the D6 regular-packet statement: `ML2` supplies the global stationary decomposition, while `AC-EX-2M` identifies the stationary maps with Cook limits only on the dense regular core.  No endpoint/equal-velocity Cook assertion is inferred.
- `ml6.md:118-267` uses the already-PROVED separated-preparation norm bridge at each fixed `ε`; it does not attempt to make the raw `O(ε)` bound overlap eliminate leading contamination.  That limit-order distinction is correct.
- The arithmetic checker is red-capable but, as disclosed at `ml6.md:336-338`, bears on none of the analytic wave-operator or limit-order steps.

**Adjudication: PROMOTE-к-PROVED for the scoped D6 `ML1` row and `ML6-HS-SEP`; DEMOTE-to-SKETCH for `ML1-D31-kernel` until both D31-register defects above are repaired.**
