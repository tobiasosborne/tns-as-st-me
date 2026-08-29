# Anchored merge proposals

Apply only after the proof candidate receives the repository's required
adjudication.  No shared file was edited by this lane.

## 1. `claims/CLAIMS.md` — replace the ML1 row

**Exact anchor to replace**

`| ML1 | Conjectured two-magnon wave operators and channel norm on packets away from equal velocities and endpoints (future work). | CONJECTURE | D6--D8 | — | — |`

**Replacement**

`| ML1 | For D6--D8, center-momentum fibering and ML2's exact half-line Jacobi Plancherel transform give the canonical decomposition 𝓗₂=𝓗_sc⊕𝓗_b, with one bound eigenvector in every K≠0 relative fiber and a threshold resonance at K=0.  The incoming/outgoing maps W_-=𝒰_sc^* and W_+=𝒰_sc^*M_{S_phys^{-1}} are isometries onto the same scattering summand, intertwine joint translations, and obey W_+^*W_-=M_{S_phys}.  On every smooth compact packet supported away from equal velocities and one-particle/fiber endpoints they coincide with the AC-EX-2M strong Cook limits.  The compatible regular-packet union is dense, so the maps glue canonically; no endpoint/equal-velocity time-dependent assertion or incoming bound-pair channel is claimed. | PROVED | D6--D8, ML2, AC-EX-2M | theory/lanes/blitz-2026-08-29/ml1-ml6/ml1.md ⟨1⟩1--⟨1⟩7 | theory/lanes/blitz-2026-08-29/ml1-ml6/ml1_ml6_check.py checks only explicit fiber arithmetic, not wave-operator existence |`

## 2. `claims/CLAIMS.md` — insert a scoped ML6 row after the existing ML6 row

Do **not** promote or delete the existing general `ML6` CONJECTURE row.

**Insertion anchor**

`| ML6 | Conjectured control of `N→∞`, packet-width and `k_s→0` limit order and bound/off-shell channels (future work). | CONJECTURE | ML1, ML2 | — | — |`

**Insert immediately after it**

`| ML6-HS-SEP | On D6 and the separated primitive packet class (D29-HS-SEP), with hard support I⋐(0,π), the order N→∞ ≺ (R,T,σ)→(∞,∞,0) ≺ ε↓0 removes at each fixed ε the full packet-smeared Parseval weight of the (R5) bound/string and off-selected real-root coefficients.  Every actual row-measure limit then equals ∫(S_phys−1)dμ and obeys 2i bar k+O_I(ε²).  The proof needs no ε-uniform Cook estimate and makes no individual unsmeared-coefficient, arbitrary-D29, endpoint, equal-velocity, or incoming bound-channel claim. | PROVED | D6--D8, ML1, ML2, AC-EX-2M, S-IDX-MATCH-HS-SEP, O7, O8 | theory/lanes/blitz-2026-08-29/ml1-ml6/ml6.md ⟨1⟩1--⟨1⟩9 | theory/lanes/blitz-2026-08-29/ml1-ml6/ml1_ml6_check.py and ml1_ml6_check.out: green exit 0; --red-bound and --red-unitarity exit 1; arithmetic only |`

## 3. `claims/CLAIMS.md` — insert the conditional external-kernel row

**Insertion anchor:** the replacement `ML1` row from §1.

**Insert immediately after it**

`| ML1-D31-kernel | Under D31(1)--(2), transporting the C∞ rigging through the Gram-normalized exact band isometry Γ_M defines generalized kernels \|k,b⟩ with Γ_Mf=Σ_b∫f_b(k)\|k,b⟩dk/(2π), ⟨k,b\|k',b'⟩=2πδ(k−k')δ_bb', and H\|k,b⟩=ω(k)\|k,b⟩.  D31(3)--(4) identifies their packets with the exact filtered creator packets and D24(b)'s unit-weight external legs.  This is conditional on D31 and says nothing about a merely variational band. | PROVED | D24(b), D31 | theory/lanes/blitz-2026-08-29/ml1-ml6/ml1.md ⟨1⟩6 | — |`

## 4. `definitions.md` — narrow the D24(b) kernel-existence sentence

**Exact anchor to replace**

`in any other register the existence of the asymptotic one-magnon kernel is claim `ML1` (CONJECTURE), and every`

**Replacement**

`in a D31 exact-band register the asymptotic one-magnon kernel is constructed by claim ML1-D31-kernel, while outside the fully polarised and D31 registers its existence remains open; every`

## 5. `theory/TRIANGLE.md` §2.4 table

**ML1 row:** replace its status with `PROVED` and use the scoped statement in
PATCH §1, including the endpoint/equal-velocity and no-bound-channel caveats.

**ML6 row:** keep status `CONJECTURE`; append: `The D6 separated-packet
subclass is PROVED as ML6-HS-SEP; unrestricted coefficientwise/arbitrary
protocol control remains open.`

## 6. `notation.md` — add rows near the existing D31 notation block

`| 𝒞, Σ_bad, 𝓗_ch, 𝓗_sc, 𝓗_b | ML2 canonical (K,q) chart, excluded regular-packet set, channel space, real-scattering summand, and bound-band summand | theory/lanes/blitz-2026-08-29/ml1-ml6/ml1.md |`

`| β(K,q), P_cont,j, (L6-order) | normalized D6 bound-fiber overlap with the charge-created relative wave, contaminating spectral projection, and the ML6-HS-SEP limit precedence | theory/lanes/blitz-2026-08-29/ml1-ml6/ml6.md |`
