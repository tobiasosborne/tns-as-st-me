# AMP — the soft-leg amputation value is not fixed by D24

Status: **OBSTRUCTION**.

Result: D24(b)+(d) do not prove `𝔞_leg(ρ)=1/Z_ρ`, and they do not
prove its negation.  They fix the charge-created/asymptotic-leg conversion
`Z_ρ^{-1/2}` and leave the remaining nonzero scalar unconstrained.  Thus AMP
is not derivable from the current hypotheses; a new dynamical normalization
theorem is required.  This is a refutation of derivability, not of the
possible physical value `1/Z_ρ` in a future nonempty microscopic class.

**Prover conclusion (full Lamport):** relation-level underdetermination and
the one-factor accounting.  **Claim-DAG status:** no promotion before the
mandated hostile round and repair; AMP remains CONJECTURE.  Microscopic
nonemptiness and the physical value of `𝔞_leg(ρ)` are **CONJECTURE/OPEN**.

## 1. Setup (D-number register only)

Fix `ρ>0`, put `Z_ρ=2ρ`, assume `𝒮_W(ρ)≠∅`, and work in a register where
the asymptotic one-magnon kernel exists, as required by D24(d).  All
amplitudes below use D24(b)'s fixed convention: the hard leg is amputated in
the same way in `M_1^O` and `M_2^O`, while the extra soft leg of `M_2^O` is a
unit-weight, delta-normalized asymptotic magnon.  D24(b) then gives the exact
charge-created-to-asymptotic conversion `Z_ρ^{-1/2}` in the LSZ limit, with
finite-volume descendant factor `(Z_ρ-2/N)^{-1/2}`.

D24(d)1 decomposes `M_2^O` into the descendant, orthogonal-current, and
direct/contact terms.  D24(d)2 fixes the descendant current residue in the
charge-created normalization to `2iv_hM_1^O(h)`.  D24(d)3a defines

`L(k,h)=E^O_desc(k,h)/[(e^{ik}-1)2iv_hM_1^O(h)]`

for `k≠0` and assumes a process-independent uniformly `C^1` extension.
D24(d)3b requires only

`L(0,h)=𝔞_leg(ρ)(-iχ(h,0)/v_h)`, `𝔞_leg(ρ)≠0`.

D24(d)4--5 impose `O(k^2)` bounds on the other two terms.  No D24 clause
states the value of `√Z_ρ 𝔞_leg(ρ)`, which is precisely the scalar left after
the one D24(b) leg conversion has been made.

## 2. Lamport ladder

**THEOREM AMP-OBSTRUCTION (relation-level underdetermination).**

**ASSUME.**  The setup of §1 and only the hypotheses stated in D24(b)+(d).

**PROVE.**  Those hypotheses entail neither `𝔞_leg(ρ)=1/Z_ρ` nor its
negation.  Even after granting the charge-created reading of `E^O_desc`, they
supply exactly one factor `Z_ρ^{-1/2}`; the value of the remaining nonzero
factor is not constrained.

### ⟨1⟩1.  PROVE that the normalized descendant projection contains one inverse square root, not two

**⟨2⟩1.**  On a fully polarized spin-`S` tail, put `Z_ρ=2S`.  For a finite
ring and commensurate `q≠h`, let `u_N:=Q_q^-|h⟩`.  Then

`Q_k^-|Ω⟩=√Z_ρ |k⟩` per site, and `⟨u_N|u_N⟩=Z_ρN-2`.                 (AMP.1)

**Justification.**  D24(b)(i)--(ii), named computation D24N-C8.  The first
identity is exact on the vacuum; the second is exact on the descendant.

**⟨2⟩2.**  Let `R_N:=⟨u_N|w_N⟩` for the vector `w_N` to be projected onto
the descendant line.  Its orthogonal projection is

`P_Nw_N = u_N R_N/(Z_ρN-2)`.

Writing the normalized descendant as
`û_N:=u_N/√(Z_ρN-2)` gives instead

`P_Nw_N = û_N R_N/√(Z_ρN-2)`.                                (AMP.2)

**Justification.**  The rank-one orthogonal-projector formula and (AMP.1).
This equality is recomputed on the explicit spin states by AMP-C2.

**⟨2⟩3.**  Therefore the coefficient against the normalized descendant is
`R_N/√(Z_ρN-2)`.  Reading `R_N/(Z_ρN-2)` as that coefficient drops the
factor `√(Z_ρN-2)` contained in `u_N=√(Z_ρN-2)û_N` and double-counts the leg
normalization.

**Justification.**  (AMP.2).  The mutation making exactly this substitution
is registered as `amp_check.py --red-double-count` and fails AMP-C2.

**⟨2⟩4.**  After removing the common finite-ring delta-normalization, the
descendant conversion is `(Z_ρ-2/N)^{-1/2}` and hence

`lim_{N→∞}(Z_ρ-2/N)^{-1/2}=Z_ρ^{-1/2}`.                       (AMP.3)

There is no second `N`-independent factor in this limit.

**Justification.**  Divide numerator and denominator of the square root in
(AMP.2) by `N`; then use continuity of `x↦x^{-1/2}` at `Z_ρ>0`.  Named
computation AMP-C3 also checks the `O(N^{-1})` approach.

**⟨2⟩5. QED.**

### ⟨1⟩2.  PROVE that none of the four named operations fixes the missing factor

**⟨2⟩1 (descendant projection).**  The orthogonal descendant projection is
already exhausted by (AMP.2).  Its inverse norm squared is a coefficient on
the *unnormalized* vector; converting that vector to D24(b)'s normalized leg
returns one square root.  It therefore yields (AMP.3), not `1/Z_ρ`.

**Justification.**  ⟨1⟩1 and D24(b)'s unit soft-leg convention.

**⟨2⟩2 (windowed-charge smearing).**  D24(b) fixes delta-normalized kernels,
the D12(a′) packet register, and soft envelopes with value `1` at `k=0`.
The smearing integral is linear and supplies no density-dependent scalar.  A
constant envelope `Z_ρ^{-1/2}` would change its value at zero and hence would
be a forbidden second leg rescaling, not a new mechanism.

**Justification.**  D3(a), D12(a′), and D24(b)'s explicit requirement
`λ(0)=1`.

**⟨2⟩3 (the two normalization anchors).**  D24(b) removes the covariance
`M_1↦cM_1`, `M_2↦c′M_2` by fixing `c′(0)/c=1`.  D24(d)2 then imposes the
Ward residue as a membership condition.  Removing a rescaling freedom makes
the already-computed value of `L` meaningful, but neither anchor evaluates
`L(0,h)`; that value is assumed only in the form of D24(d)3b with an arbitrary
nonzero `𝔞_leg(ρ)`.

**Justification.**  D24(b)'s covariance paragraph and D24(d)2--3.  No
normalization change is made in this step.

**⟨2⟩4 (finite `N`).**  The exact descendant factor expands as

`(Z_ρ-2/N)^{-1/2}=Z_ρ^{-1/2}[1+1/(Z_ρN)+O(N^{-2})]`.           (AMP.4)

Thus its mismatch is a vanishing finite-size correction, not a surviving
factor `Z_ρ^{-1/2}`.

**Justification.**  Taylor expansion of `(1-x)^{-1/2}` at `x=0`, with
`x=2/(Z_ρN)`, and D24N-C8's exact descendant norm.

**⟨2⟩5 (the unspecified descendant propagation).**  D24(d)1 says that an
`E^O_desc` summand exists and D24(d)3a assumes that its quotient has a
process-independent `C^1` extension.  It does not define a propagation map
whose normalized residue could be evaluated.  Consequently this is the only
place a genuinely new second mechanism could be proved, but the required
value is absent from the present hypotheses.

**Justification.**  D24(d)1 and D24(d)3a--3b.  This is an obstruction, not an
assertion that all microscopic descendant maps have arbitrary residues.

**⟨2⟩6. QED.**

### ⟨1⟩3.  PROVE directly that the displayed D24 relations admit every nonzero constant

**⟨2⟩1. ASSUME.**  Fix a compact hard window on which `v_h≠0` and the channel
sign `χ` is constant.  Choose a nonzero `m∈L²(I)`.  For any number
`a∈ℂ\{0}`, consider the following one-dimensional, source-linear *formal
amplitude package*:

`M_1^{cO_0}(h):=c m(h)`,

`R^{cO_0}(h):=c 2iv_hm(h)`,

`L_a(k,h):=a(-iχ/v_h)`,

`E_{desc,a}^{cO_0}(k,h):=(e^{ik}-1)L_a(k,h)R^{cO_0}(h)`,

`M_{2,a}^{cO_0}:=E_{desc,a}^{cO_0}`,

with orthogonal-current and direct/contact terms both zero.

**Justification.**  This line defines a witness for the relations stated in
D24(b)+(d).  It does not assert that `O_0` has been constructed as a
microscopic local operator.

**⟨2⟩2.**  Clause D24(d)1 holds exactly and D24(d)4--5 hold with zero
remainder.

**Justification.**  `M_{2,a}=E_{desc,a}+0+0` by definition; the zero function
obeys every required `O(k²)` bound.

**⟨2⟩3.**  D24(d)2 holds because the bracketed Ward residue is
`R^{cO_0}=c2iv_hm=2iv_hM_1^{cO_0}`.

**Justification.**  The first two definitions in ⟨2⟩1.

**⟨2⟩4.**  For `k≠0` and `m(h)≠0`, the D24(d)3a quotient of
`E_{desc,a}^{cO_0}` is exactly `L_a`.  It is uniformly `C^1`, and

`iv_hL_a(0,h)/χ=a`,

so D24(d)3b holds for the chosen arbitrary nonzero value `a`.

**Justification.**  Cancellation in the definitions of ⟨2⟩1.  AMP-C1 checks
the cancellation symbolically without substituting a value for `a`.

**⟨2⟩5.**  Choosing two distinct nonzero values of `a` leaves `M_1`, the Ward
residue, the packet measure, and the D24(b) leg convention unchanged while
changing `L` and `M_2`.  It is therefore not a normalisation covariance
transformation.

**Justification.**  All quantities named as unchanged in ⟨2⟩1 are independent
of `a`; `L_a` depends injectively on `a` because `χ/v_h≠0`.  AMP-C1 evaluates
two such packages with zero anchor change.

**⟨2⟩6.**  Hence the algebraic and analytic relations displayed in
D24(b)+(d) do not determine `𝔞_leg`.  Any restriction to actual microscopic
amplitudes capable of selecting a value is an additional theorem about those
amplitudes, not a consequence written in D24.

**Justification.**  ⟨2⟩1--⟨2⟩5.  The limitation to a relation-level witness
is explicit and is why the verdict is OBSTRUCTION rather than a physical
counterexample.

**⟨2⟩7. QED.**

### ⟨1⟩4.  PROVE the honest disposition of AMP

**⟨2⟩1.**  Granting the charge-created reading, factor the class datum as

`𝔞_leg(ρ)=Z_ρ^{-1/2}[√Z_ρ 𝔞_leg(ρ)]`.                         (AMP.5)

D24(b) fixes the first bracket-free factor.  D24(d) requires the square
bracket in (AMP.5) only to be nonzero and process independent.

**Justification.**  ⟨1⟩1, D24(b), and D24(d)3a--3b.

**⟨2⟩2.**  AMP is equivalent to the additional equation

`√Z_ρ 𝔞_leg(ρ)=Z_ρ^{-1/2}`.                                  (AMP.6)

The needed second mechanism would therefore be a **post-conversion
descendant-propagation/LSZ residue theorem** proving (AMP.6) after both sides
are already expressed against D24(b)'s same delta-normalized soft leg.  Such
a theorem would not be a leg normalization; no present D24 clause supplies
it.

**Justification.**  Multiply AMP's proposed `𝔞_leg=1/Z_ρ` by `√Z_ρ` and use
(AMP.5); then apply ⟨1⟩2.⟨2⟩5.

**⟨2⟩3.**  Therefore AMP is neither proved nor physically refuted here.  What
is proved is that it is undecidable from the current D24(b)+(d) relations,
beyond `𝔞_leg(ρ)≠0`; nonemptiness and a microscopic evaluation of the missing
residue remain open.

**Justification.**  ⟨1⟩1--⟨1⟩3 and D24(d)'s explicit nonemptiness fence.

**⟨2⟩4. QED.**

**⟨1⟩5. QED.**  Theorem AMP-OBSTRUCTION.

## 3. D24N-C8 double-count check

The exact finite-volume accounting is

\[
 \|u_N\|^2=Z_\rho N-2,
 \qquad
 P_Nw_N={u_N\langle u_N,w_N\rangle\over Z_\rho N-2}
        ={u_N\over\sqrt{Z_\rho N-2}}
         {\langle u_N,w_N\rangle\over\sqrt{Z_\rho N-2}}.
 \tag{AMP.7}
\]

The first square-root denominator in the last expression normalizes the
*vector*.  Only the second is the amplitude coefficient against that
normalized vector.  Counting both as amplitude factors changes registers
mid-equation.

| Route | finite-`N` amplitude factor | LSZ limit | disposition |
|---|---:|---:|---|
| exact normalized leg | `(Z_ρ-2/N)^{-1/2}` | `Z_ρ^{-1/2}` | PROVED by (AMP.7) / D24N-C8 |
| projector denominator misread as normalized coefficient | `(Z_ρ-2/N)^{-1}` | `Z_ρ^{-1}` | REFUTED as a register double-count by AMP-C2 |
| AMP target | not fixed at finite `N` by D24 | `Z_ρ^{-1}` | requires the independent residue (AMP.6) |

The ansatz-free comparison is a separate, conditional falsifier.  Under both
the charge-created reading of `E^O_desc` and the jet-identification bridge
(α), a pure-leg proof predicts the ML5 jet `2/√(2S)`.  At the
**pre-registered `0.08` band**, its scaled deviations are

`0.0004 / 0.4158 / 0.7347 / 1.0033`

at `S=1/2,1,3/2,2`, hence margins `5.2×/9.2×/12.5×` at the three
nondegenerate spins.  AMP-C4 reproduces these values.  Without either stated
hypothesis, the comparison does not identify the two quantities and is not a
refutation of AMP; the relation-level obstruction above does not use (α).

## 4. Checker certificate and limits

Run:

```text
python3 -O theory/checks/amp_check.py
python3 -O theory/checks/amp_check.py --red-double-count
python3 -O theory/checks/amp_check.py --red-pure-leg
```

The green run exits `0`; each registered red run exits `1` through an explicit
`SystemExit(1)`.  There are no bare assertions.

- **AMP-C1 (PROVED, relation level)** symbolically cancels the descendant
  quotient while leaving `a_leg` free, checks its jet
  `2i a_leg χ M_1`, and evaluates two fixed-anchor packages with different
  nonzero constants.  It certifies that D24's displayed relations do not fix
  the constant.  It does **not** construct a local microscopic source or
  prove `𝒮_W(ρ)≠∅`.

- **AMP-C2 (PROVED, exact finite volume)** independently constructs the
  spin-`S` ladder states and verifies the D24N-C8 vacuum and descendant
  norms.  It then checks the normalized rank-one projection (AMP.7).
  `--red-double-count` replaces the normalized coefficient by the
  unnormalized projector coefficient and dies at AMP-C2.  The gate does
  **not** compute the dynamical value of `L`.

- **AMP-C3 (PROVED, algebraic limit)** verifies that the exact finite-`N`
  factor approaches `Z_ρ^{-1/2}` with `O(N^{-1})` correction.  It certifies
  that the finite-size mismatch supplies no persistent second factor.  It
  does **not** establish any separate LSZ existence theorem beyond the D24
  register assumed in §1.

- **AMP-C4 (conditional falsifier only)** reads the data file's
  pre-registered `0.08` band and reproduces the pure-leg deviations and
  margins in §3.  `--red-pure-leg` registers a proposed proof whose only
  mechanism is D24N-C8 leg rescaling and dies at AMP-C4.  This gate tests
  neither the charge-created reading of `E^O_desc`, bridge (α), class
  membership, nor `L`; therefore its numerical disagreement is binding only
  when the first two are assumed.

Passing the checker proves no physical value for `𝔞_leg`.  Its green content
is the obstruction and its red content is the no-double-count fence.

## 5. MERGE PROPOSALS

No change is proposed to `definitions.md` or `notation.md`.

1. **Keep claim `AMP` at CONJECTURE.**  Append to its statement:

   > `theory/amp.md` proves a relation-level OBSTRUCTION: D24(b)+(d) fix only
   > the one D24N-C8 factor `Z_ρ^{-1/2}` and otherwise constrain
   > `𝔞_leg(ρ)` only by nonvanishing/process independence.  AMP is neither
   > proved nor physically refuted.  Any proof requires an additional
   > post-conversion descendant-propagation/LSZ residue theorem fixing
   > `√Z_ρ𝔞_leg(ρ)=Z_ρ^{-1/2}`; the descendant projector, packet measure,
   > D24(b) anchors, and finite-`N` mismatch do not supply it.

   Add `theory/checks/amp_check.py` to `where-tested`, naming AMP-C2 and
   AMP-C4 and preserving the two-hypothesis fence on the latter.

2. **Add an obstruction row `AMP-OBS`, initially at SKETCH.**  Promote it to
   PROVED only if the mandated hostile round and repair leave no open
   FATAL/MAJOR on the displayed statement:

   | id | statement | status | depends-on | where-proved | where-tested |
   |---|---|---|---|---|---|
   | AMP-OBS | In the D24(b) convention, the algebraic/analytic relations of D24(b)+(d) do not determine `𝔞_leg(ρ)` beyond `𝔞_leg(ρ)≠0`.  D24N-C8 supplies exactly one factor `Z_ρ^{-1/2}` on the charge-created reading; the normalized descendant projection returns no second factor.  Formal fixed-anchor D24 relation packages exist for every nonzero constant, so selecting `1/Z_ρ` requires an additional microscopic descendant-propagation/LSZ residue theorem.  This is not a microscopic counterexample and does not decide physical AMP. | SKETCH (prover pass; promotion gated on critic/repair) | D24(b), D24(d) | theory/amp.md | theory/checks/amp_check.py AMP-C1--C3; `--red-double-count`; AMP-C4 and `--red-pure-leg` are conditional on the displayed comparison hypotheses |

3. `D24-VAL`, `ML5-B`, and `S2-2body-S` require no status or statement
   change.  `D24-VAL` remains the proved conditional implication using (α);
   ML5-B remains constant-agnostic; `S2-2body-S` remains the ansatz-free data
   source for the conditional AMP-C4 fence.
