# ML6 — ordered limits and contamination control

**Lane status:** **PROVED-candidate on the D6 separated-packet class;
PARTIAL for unrestricted ML6.**  The positive theorem below uses the PROVED
`S-IDX-MATCH-HS-SEP` norm bridge.  It does not claim that unsmeared (R5)
coefficients have a uniform plane-wave limit, nor that an arbitrary D29
protocol belongs to the separated class.

## ⟨1⟩1. Theorem ML6-HS-SEP

**ASSUME.** D6--D8, `J>0`, a fixed hard interval
`I=[a,b]⋐(0,π)`, and a one-sided normalized soft packet

`f_ε(k)=ε^{-1/2}f(k/ε)`, `supp f⊂[c_1,c_2]⊂(0,∞)`.

Let `g_σ` be a normalized hard packet supported in `I`, with `σ↓0`.  For
each fixed `ε>0`, use the separated-preparation sequence
`(D29-HS-SEP)`: translate the incoming hard packet by `R_j→∞`, take a
settling time `T_j` with `d_εT_j-R_j→∞`, impose `(SEP)`, and take the ring
size sufficiently large for the thermodynamic/sampling error `η_j→0`.
The order is

`N→∞ ≺ (R,T,σ)_j→(∞,∞,0) ≺ ε↓0`.                            **(L6-order)**

**PROVE.**

1. At each fixed `ε`, the total squared (R5) coefficient of the prepared
   state outside the selected incoming real-scattering packet tends to zero.
   This includes the two-string/bound band and all real-scattering spectral
   coefficients off the selected packet support.  The analogous outgoing
   statement holds after time `T_j`.
2. Along every actual row-measure limit subsequence, the normalized connected
   readout is exactly

   `A_*(ε)=∫[S_phys(k,h)-1]dμ_{*,ε}(k,h)`.

3. With `bar k_*(ε):=∫k dμ_{*,ε}`,

   `A_*(ε)=2i bar k_*(ε)+O_I(ε²)`,

   where the remainder is uniform in the hard packet and in the actual limit
   measure.  Thus neither bound nor off-shell coefficients contaminate the
   leading real scattering channel.
4. No Cook estimate is required uniformly as `ε↓0`: the fixed-`ε` channel
   limit is completed first.  The theorem has no `a↓0` extension; this is the
   D8/O7 exclusion of the non-uniform `k_h→0` regime.

*Justification.* D6--D8; claims `ML2`, `AC-EX-2M`,
`S-IDX-MATCH-HS-SEP`, `S-IDX-D29-value-HS-SEP`, and `O7`--`O8`.

## ⟨1⟩2. Exact bound overlap and the uniform spectral fence

**ASSUME.** D6--D8 and `h∈I`.  Put

`K=h+k`, `q=(h-k)/2`, `c=cos(K/2)`.

**PROVE.**  The bound fiber is separated uniformly from the soft--hard
continuum, and its overlap with the unseparated charge-created relative wave
vanishes linearly in `k`.

**⟨2⟩1.**  The continuum/bound separation at the same total momentum is

`d(K,q):=E(K,q)-E_b(K)`

`=J(1+c²-2c cos q)=J|e^{iq}-c|²`.

At `k=0`, `d(h,h/2)=J sin²(h/2)`.  Hence compactness supplies
`ε_I>0` such that

`d(h+k,(h-k)/2)≥(J/2)sin²(a/2)>0`

for `h∈I`, `|k|≤ε_I`.

*Justification.* D6--D8 and claim `ML2`, equations (18)--(19).

**⟨2⟩2.**  The source relative wave in the `K` fiber is

`p_{Kq}(r)=e^{iqr}+e^{-iqr}`.

Pairing it with `b_K(r)=sqrt(1-c²)c^{r-1}` gives the exact coefficient

`β(K,q)=2sqrt(1-c²)(cos q-c)/(1-2c cos q+c²)`.               **(B-overlap)**

*Justification.* D6, claim `ML2`, and the geometric-series computation
certified by named computation `ml1_ml6_check.py`.

**⟨2⟩3.**  At `K=h+k`, `q=(h-k)/2`, the numerator in (B-overlap) vanishes at
`k=0`, while its denominator is `sin²(h/2)`.  Uniformly for `h∈I`,

`β(h+k,(h-k)/2)=2k+O_I(k²)`,

and in particular `|β|≤C_I|k|` for `|k|≤ε_I`.

*Justification.* D8, (B-overlap), and named computation
`ml1_ml6_check.py`.

**⟨2⟩4.**  If `F` is a normalized packet supported at `|k|≤ε`, its bound
coefficient in each total-momentum fiber is the `q`-integral of `βF`.
Cauchy--Schwarz on `0<q<π` therefore gives

`||P_b I F||≤C'_I ε||F||`.

Thus the raw bound probability is `O_I(ε²)`.

*Justification.* Claim `ML2`, its direct-integral resolution (21), and
⟨2⟩3.

**⟨2⟩5.**  The `O(ε)` raw bound amplitude in ⟨2⟩4 is the same order as the
connected scattering law and by itself would not exclude contamination.
The decisive input is instead the ordered separated-preparation norm limit
proved below, which removes the bound projection at fixed `ε` before
`ε↓0`.

*Justification.* Claims `S2-2body` and `S-IDX-MATCH-HS-SEP`.

**⟨2⟩6. QED.**

## ⟨1⟩3. All contaminating (R5) coefficients vanish collectively

**ASSUME.** Fix `ε>0` and use the sequence in ⟨1⟩1.  Let
`F_j=f_ε⊗g_{σ_j}` including the relative translation `R_j`, and suppress the
common charge/leg scalar that cancels from the normalized readout.

**PROVE.** Bound and off-selected real coefficients vanish before the soft
limit.

**⟨2⟩1.**  In the infinite-chain ML2 representation define

`P_cont,j:=P_b+𝒰_sc^*1_{𝒞∖supp F_j}𝒰_sc`.

Then `P_cont,j W_-F_j=0`, and, because `P_cont,j` is an orthogonal
projection,

`||P_cont,j I F_j||≤||I F_j-W_-F_j||`.                       **(C-in)**

*Justification.* Claims `ML2`, `AC-EX-2M`, and the exact D6 matching in
`S-IDX-MATCH-HS-SEP`.

**⟨2⟩2.**  The separated incoming Cook-tail estimate gives, for some
`M≥8`,

`||I F_j-W_-F_j||`

`≤C_{M,ε}s_M(f_ε)s_M(g_{σ_j})(1+R_j)^{3-M}→0`.

The outgoing tail gives the analogous comparison with
`W_+M_{S_phys}F_j` after the settling time `T_j`.

*Justification.* Claim `S-IDX-MATCH-HS-SEP`, specifically its norm bridge
and separated-preparation condition `(SEP)`.

**⟨2⟩3.**  On the finite ring, claim `ML2` makes (R5), with its singular
completion, a complete Parseval expansion.  Embed each finite relative
Jacobi path into `ℓ²(ℕ)`.  On every finitely supported vector its matrix
agrees, for all sufficiently large `N`, with the half-line matrix at the
sampled `K`; the matrices are uniformly bounded.  They therefore converge
strongly, hence their spectral projections converge strongly on the bound
gap and on packet windows whose boundaries have zero ML2 spectral measure.
After the center-momentum Riemann sum, the packet-smeared sum of `|c_B|²`
over the finite-ring bound states and off-window real roots converges to
`||P_cont,jIF_j||²`.

*Justification.* D6 and claim `ML2`: finite fibers (4), infinite fiber (16),
absolute continuity and resolution (21), and Parseval expansion (23)--(24).

**⟨2⟩4.**  Combining ⟨2⟩1--⟨2⟩3 yields

`Σ_{B∈cont,j}|c_{B,j}^{(R5,packet)}|²`

`≤[C_{M,ε}s_M(f_ε)s_M(g_{σ_j})(1+R_j)^{3-M}+o_N(1)]²→0`,

where `N→∞` is taken first and
`c_{B,j}^{(R5,packet)}` is (R5) smeared with the normalized soft/hard packet,
not an individual plane-wave coefficient.

The set `cont,j` may contain the finite-ring string/singular representatives
and every real root outside the selected packet window; hence no
coefficient-by-coefficient root labelling or principal-value cancellation is
needed.

*Justification.* Claims `ML2` and `S-IDX-MATCH-HS-SEP`, together with
⟨2⟩1--⟨2⟩3.

**⟨2⟩5.**  The estimate is deliberately collective.  Individual
plane-wave (R5) coefficients may carry volume-dependent delta/principal-value
normalizations, but Parseval and the norm bridge show that their entire
contaminating projection vanishes on packets.

*Justification.* D3(a), D12(a′), claim `ML2`, and ⟨2⟩4.

**⟨2⟩6. QED.**

## ⟨1⟩4. The limit order closes without a soft-uniform Cook estimate

**ASSUME.** ⟨1⟩1--⟨1⟩3.  **PROVE.** The order (L6-order) exists on the
stated class and gives the real-channel multiplier before `ε↓0`.

**⟨2⟩1.**  Hold `(ε,σ_j,R_j,T_j)` fixed.  Finite-range thermodynamic
convergence and Plancherel sampling allow `N→∞`; equivalently one may choose
`N_j` after the tuple so that `η_j≤1/j`.  This is a diagonal realization of
the first precedence in (L6-order), not an interchange with later limits.

*Justification.* Claim `S-IDX-MATCH-HS-SEP`.

**⟨2⟩2.**  At fixed `ε`, choose for example
`R_j=ceil(σ_j^{-2})` and `T_j=2R_j/d_ε`.  The separated-preparation bound
then sends both Cook tails and the finite-ring error to zero as `j→∞`, even
though the fixed-packet seminorms diverge as `σ_j↓0`.

*Justification.* Claim `S-IDX-MATCH-HS-SEP`, including the verified nonempty
choice satisfying `(SEP)`.

**⟨2⟩3.**  Along every actual row-measure limit subsequence the normalized
readout consequently obeys the exact identity

`A_*(ε)=∫[S_phys(k,h)-1]dμ_{*,ε}(k,h)`.

At this point the bound and off-selected projections of ⟨1⟩3 are already
zero in norm.

*Justification.* Claim `S-IDX-MATCH-HS-SEP` and ⟨1⟩3.

**⟨2⟩4.**  Only after ⟨2⟩3 is established for every fixed `ε` is
`ε↓0` taken.  Therefore the `ε^{-M}` growth of fixed-packet Cook constants
never enters a soft-limit dominated-convergence argument.

*Justification.* D8 and claims `AC-EX-2M`, `S-IDX-MATCH-HS-SEP`.

**⟨2⟩5. QED.**

## ⟨1⟩5. The soft expansion is taken only after channel purification

**ASSUME.** The exact fixed-`ε` identity of ⟨1⟩4.⟨2⟩3.  **PROVE.** Its
leading term is the physical real-scattering term alone.

**⟨2⟩1.**  On `h∈I` and `|k|≤c_2ε` with `ε` small, O8 gives uniformly

`S_phys(k,h)-1=2ik+[i cot(h/2)-2]k²+O_I(|k|³)`.

The D7 sign is `+` throughout D8 because `v_h>v_s` for the fixed compact
hard interval and sufficiently small signed soft momentum.

*Justification.* D7--D8 and claims `O7`--`O8`.

**⟨2⟩2.**  Integrating ⟨2⟩1 against the probability measure in
⟨1⟩4.⟨2⟩3 gives

`A_*(ε)=2i bar k_*(ε)+R_*(ε)`, `|R_*(ε)|≤C_I ε²`.

The constant is independent of the hard width and of the chosen actual row
measure limit point.

*Justification.* D8, claim `O8`, and the scale-tied support in ⟨1⟩1.

**⟨2⟩3.**  Because the contaminating projection was sent to zero at each
fixed `ε` in ⟨1⟩3--⟨1⟩4, it contributes exactly zero to `A_*(ε)`, hence
cannot supply an additional term proportional to `ε` in ⟨2⟩2.

*Justification.* Claim `S-IDX-MATCH-HS-SEP` and ⟨1⟩3.⟨2⟩4.

**⟨2⟩4.**  The raw estimate `||P_bIF||=O_I(ε)` from ⟨1⟩2 is therefore only
a diagnostic.  Orthogonality plus the fixed-`ε` separated limit, not that
power count, is what excludes leading bound contamination.

*Justification.* Claims `ML2`, `S-IDX-MATCH-HS-SEP`, and ⟨1⟩2.⟨2⟩4--⟨2⟩5.

**⟨2⟩5. QED.**

## ⟨1⟩6. The `k_h→0` non-uniformity is not interchanged with ML6

**ASSUME.** `I=[a,b]⋐(0,π)` remains fixed.  **PROVE.** Every constant used
above is uniform on the theorem's domain and no endpoint limit is hidden.

**⟨2⟩1.**  The bound/continuum fence is at least
`(J/2)sin²(a/2)`; the coefficient in (B-overlap) is bounded through a
denominator whose `k=0` value is `sin²(h/2)`.

*Justification.* D8 and ⟨1⟩2.⟨2⟩1--⟨2⟩3.

**⟨2⟩2.**  O7's cubic remainder constant grows as `O(a^{-2})` when
`a↓0`, and the quadratic coefficient `cot(h/2)` diverges.  The velocity and
bound gaps also collapse in a joint hard/soft threshold limit.

*Justification.* D8 and claims `O7`--`O9`.

**⟨2⟩3.**  Therefore the proof fixes `a>0` before every operation in
(L6-order).  Taking `a↓0`, taking `k_h` jointly soft, or approaching equal
velocities would be a different theorem and is not a corollary.

*Justification.* D7--D8 and claims `O7`--`O9`.

**⟨2⟩4. QED.**

## ⟨1⟩7. Honest boundary

**⟨2⟩1.**  The theorem controls the finite/infinite, hard-width,
scattering-time, and soft limits on `(D29-HS-SEP)`.  It proves no uniform
pointwise limit of individual (R5) coefficients; their packet-smeared
contaminating sum is controlled by Parseval and a norm estimate.

*Justification.* D3(a), D12(a′), claims `ML2` and
`S-IDX-MATCH-HS-SEP`.

**⟨2⟩2.**  The theorem constructs no incoming bound-pair wave operator and
does not promote general D29, ML3, ML4, ML5, or S-general.  It only proves
that the bound summand and off-selected real summand do not enter the stated
primitive real-channel readout.

*Justification.* Claims `S-general`, `ML2`, `ML3`, `ML4`, and
`S-IDX-MATCH-HS-SEP`.

**⟨2⟩3.**  Steps ⟨1⟩2--⟨1⟩3 isolate and remove the contaminating spectral
coefficients, ⟨1⟩4 fixes their order of removal, ⟨1⟩5 takes the soft limit in
the purified channel, and ⟨1⟩6 enforces the D8/O7 endpoint fence.  Theorem
ML6-HS-SEP is proved at exactly the stated scope.

*Justification.* D6--D8 and claims `ML2`, `S-IDX-MATCH-HS-SEP`, and `O7`--`O8`.

## ⟨1⟩8. Red-capable arithmetic certificate

**⟨2⟩1.**  Named computation `ml1_ml6_check.py` independently compares
(B-overlap) with a 6000-term geometric sum, differentiates it at the soft
point, checks `|S_phys|=1`, and samples the positive continuum/bound gap.

*Justification.* Named computation `ml1_ml6_check.py`; recorded output
`ml1_ml6_check.out`.

**⟨2⟩2.**  The optimized green run exits zero.  Mutation `--red-bound`
changes `cos q-c` to `cos q+c` and exits one at the overlap-zero,
geometric-sum, and derivative gates.  Mutation `--red-unitarity` changes the
scattering denominator and exits one at the unitarity gate.

*Justification.* Named computation `ml1_ml6_check.py`; recorded output
`ml1_ml6_check.out`.

**⟨2⟩3.**  This certificate tests none of wave-operator existence,
finite-volume spectral convergence, `(SEP)`, or the limit order; those are
the analytic/PROVED-claim inputs above.

*Justification.* Named computation `ml1_ml6_check.py` and its module
docstring.

**⟨2⟩4. QED.**

## ⟨1⟩9. QED

Theorem ML6-HS-SEP follows from the spectral fence ⟨1⟩2, collective
coefficient estimate ⟨1⟩3, ordered limit ⟨1⟩4, physical soft expansion
⟨1⟩5, and endpoint fence ⟨1⟩6, with the exact scope in ⟨1⟩7.  QED.
