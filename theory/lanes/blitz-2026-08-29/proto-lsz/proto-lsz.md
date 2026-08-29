<!-- ROLE: blitz-lane L6b proof shard for PROTO-LSZ.  Shared definitions and
     claims are not edited.  D29/D30 remain in their quarantined register. -->

# PROTO-LSZ on the separated spin-S protocol: LSZ-shaped scalar factorisation and the remaining component lemma

**STATUS: PARTIAL.**  For the fully polarised bilinear ferromagnet `H_S` and
the separated-preparation subclass `(D29-HS-SEP)`, the complete limiting D29
**scalar** datum has an exact one-channel Ward/LSZ-shaped factorisation.  Its scalar
LSZ quotient is uniformly `C^1` and has profile
`-i sgn(v_h-v_s)/(2S v_h)`.  This is stronger than the required scalar
`o(epsilon)` estimate.  Full `(PROTO-LSZ)` is not claimed: the existing
definitions do not yet identify this quotient with D24's independently named
descendant component or supply the three other component maps.  The exact
missing positive lemma is isolated in Section 4.

## 1. Setup by D-number

### ⟨1⟩1. Frozen registers

**ASSUME.**  Let `S in {1/2,1,3/2,...}` and let `H_S` be the fully
polarised bilinear ferromagnet, with the `S=1/2` instance D6.  Use D7's
ordered-coordinate and physical out/in convention, D8's regular hard window,
D24(b)'s delta-normalised asymptotic-leg convention, the quarantined D29
proposal, and the separated subclass `(D29-HS-SEP)` proved nonempty in claim
`S-IDX-MATCH-HS-SEP`.  Put `chi=sgn(v_h-v_s)` only as the sign already fixed
by D7 on the selected channel.

**PROVE.**  All subsequent objects stay in one register and no forbidden
identification is assumed.

**⟨2⟩1.**  Choose compact `I` away from `0` and `pi` and a sufficiently small
one-sided soft neighbourhood `K_s` such that the regularity conditions (T.1)
hold on `K_s x I` and `chi` is constant there.

*Justification.*  D8 and PROVED claim `S2-2body-S`, especially (T.1) and
(T.3)--(T.4).

**⟨2⟩2.**  Plane waves below are generalized kernels only inside the smooth
D29 packets.  The quotient below is a bounded multiplier on D24(b)'s product
packet space; (PL.4) itself is the distinct normalized D29 measure pairing.

*Justification.*  D3(a), D12(a′), D24(b), and the packet register of claim
`S-IDX-MATCH-HS-SEP`.

**⟨2⟩3.**  The full-sector Ward identity retains `A=D^dagger D` on the full
positive-weight sector; no scalar highest-weight Gram operator is substituted
for it.  The only residue used below is the primitive hard-leg value
`2 i v_h`.

*Justification.*  PROVED claims `S-IDX-fin-r2` and `S-IDX-fin-G`, including
the ML4-Ward ERRATUM.

**⟨2⟩4.**  Neither D29 nor D30 is altered, and no D29/D30 merge is proposed
in this shard.

*Justification.*  D29 and D30 are the quarantined proposals in
`theory/soft-index-r2.md` Section 7; the standing brief's hard fence 3.

**⟨2⟩5. QED.**

## 2. The LSZ-shaped scalar protocol ladder

### ⟨1⟩2. A removable one-channel quotient

**ASSUME.**  The setting of ⟨1⟩1.  For `k != 0`, put locally

`L_S^sc(k,h):=[S_phys(k,h)-1]/[(e^{ik}-1) 2 i v_h]`.          (PL.1)

The superscript `sc` means *scalar scattering witness*.  It is deliberately
not called D24's `L`, because that identification is the open component
provenance step isolated below.

**PROVE.**  `L_S^sc` has a unique uniformly `C^1` extension to `k=0` on the
compact channel and

`L_S^sc(0,h)=-i chi/(2S v_h)`.                               (PL.2)

**⟨2⟩1.**  `S_phys(k,h)` is analytic in `k` and smooth in `h` on a
neighbourhood of the selected compact rectangle, and

`S_phys(0,h)=1`,  `partial_k S_phys(0,h)=i chi/S`.            (PL.3)

*Justification.*  PROVED claim `S2-2body-S`, equations (T.2)--(T.4); its
regular denominator has a positive lower bound on the compact rectangle.

**⟨2⟩2.**  There is an analytic function `G_S(k,h)`, uniformly `C^1` on a
possibly smaller compact rectangle, such that

`S_phys(k,h)-1=(e^{ik}-1)G_S(k,h)`

and `G_S(0,h)=chi/S`.

*Justification.*  Apply the analytic removable-factor theorem to ⟨2⟩1;
`partial_k(e^{ik}-1)|_0=i`, so (PL.3) gives
`G_S(0,h)=(i chi/S)/i=chi/S`.  This is independently exercised by named
computation **PLSZ-C1** in `proto_lsz_check.py`.

**⟨2⟩3.**  Since `v_h` is bounded away from zero on `I`, division of `G_S`
by `2 i v_h` preserves uniform `C^1` regularity and gives (PL.2).

*Justification.*  D8, ⟨2⟩2, and named computation **PLSZ-C1**.

**⟨2⟩4.**  The number `1/(2S)` in (PL.2) entered only through the derivative
in (PL.3), after the physical multiplier and its D7 branch were fixed.

*Justification.*  PROVED claim `S2-2body-S`; hard fence 1 of the standing
brief.  No leg-normalisation or regularity-only argument occurs.

**⟨2⟩5. QED.**

### ⟨1⟩3. Exact LSZ-shaped scalar factorisation of every actual separated limit point

**ASSUME.**  An actual row-measure limit point `mu_{*,epsilon}` of
`(D29-HS-SEP)` along the same outer indices as claim
`S-IDX-MATCH-HS-SEP`.  Write
`bar k_*(epsilon)=int k dmu_{*,epsilon}(k,h)`.

**PROVE.**  Its limiting connected datum obeys the exact identity

`A_*(epsilon)`
` =int (e^{ik}-1)L_S^sc(k,h)[2 i v_h]`
`       dmu_{*,epsilon}(k,h)`.                               (PL.4)

In particular,

`A_*(epsilon)=i chi bar k_*(epsilon)/S+O(epsilon^2)`.         (PL.5)

**⟨2⟩1.**  The same-limit, same-measure matching theorem gives

`A_*(epsilon)=int [S_phys(k,h)-1]dmu_{*,epsilon}(k,h)`        (PL.6)

with zero outer-limit remainder.

*Justification.*  PROVED claim `S-IDX-MATCH-HS-SEP`, not the distinct
Haag--Ruelle value row `S-IDX-HR-value-r2`.

**⟨2⟩2.**  For every point of the packet support, including `k=0` by
continuity,

`S_phys(k,h)-1=(e^{ik}-1)L_S^sc(k,h)[2 i v_h]`.              (PL.7)

*Justification.*  Equation (PL.1) for `k!=0` and the removable extension
proved in ⟨1⟩2.  Named computation **PLSZ-C2** checks (PL.7) and kills a
Ward-factor mutation.

**⟨2⟩3.**  Substitute (PL.7) into (PL.6) to obtain (PL.4).  This equality is
derived from the independently proved whole-datum match; it is not inserted
as a D29 definition.

*Justification.*  ⟨2⟩1--⟨2⟩2 and PROVED claim
`S-IDX-MATCH-HS-SEP`.

**⟨2⟩4.**  Uniform Taylor expansion of (PL.3), followed by integration over
`|k|<=c_2 epsilon`, gives (PL.5).

*Justification.*  PROVED claim `S2-2body-S`, D29's scale-tied packet support,
and named computation **PLSZ-C3**.  This reproduces, but does not strengthen,
PROVED claim `S-IDX-D29-value-HS-SEP`.

**⟨2⟩5.**  The finite-ring, incoming-tail, outgoing-tail, collision-row, and
readout approximation errors internal to the matching theorem vanish at each
fixed `epsilon` in the outer limit before `epsilon` is sent to zero.  This
does not identify or bound `(PROTO-LSZ)`'s two window-gradient components.

*Justification.*  PROVED claim `S-IDX-MATCH-HS-SEP`, equations
(PMLM.12), (PMLM.15), and (PMLM.17a), under `(SEP)` and the D29 limit order;
compare the strictly stronger component statement (SPEC.5).

**⟨2⟩6. QED.**

## 3. Interfaces and fences

### ⟨1⟩4. Supplier separation

**ASSUME.**  The proof of ⟨1⟩2--⟨1⟩3 and the authoritative claims rows
named below.

**PROVE.**  The scalar theorem neither imports a value too early nor merges
the protocol, Haag--Ruelle, and D24 registers.

**⟨2⟩1. MATCH interface.**  The only bridge from the fixed-time D29 datum to
the multiplier is the norm-controlled, separated-preparation theorem
`S-IDX-MATCH-HS-SEP`.  The fixed-time vector is never declared equal to a
Haag--Ruelle creator or scattering vector.

*Justification.*  PROVED claim `S-IDX-MATCH-HS-SEP`, especially its
fixed-time-product-to-wave-operator norm bridge.

**⟨2⟩2. Value interface.**  The coefficient `1/S`, and therefore the
coefficient `1/(2S)` in (PL.2), enters only after ⟨2⟩1 through the exact
physical multiplier.

*Justification.*  PROVED claim `S2-2body-S`; ⟨1⟩2.⟨2⟩4.

**⟨2⟩3. Haag--Ruelle interface.**  No inference uses the separate row
`S-IDX-HR-value-r2`.  Fixed-packet wave operators enter only inside the
already proved norm bridge cited at ⟨2⟩1.

*Justification.*  PROVED claim `S-IDX-MATCH-HS-SEP` and the explicit
non-protocol scope of row `S-IDX-HR-value-r2`.

**⟨2⟩4. D24 interface.**  Equation (PL.2) has the same *functional profile*
as D24(d)3b with the scalar coefficient `1/(2S)`, but this observation does
not identify `L_S^sc` with D24's `L` or prove a member of
`𝒮_W(ρ)|_{ρ=S}`.

*Justification.*  D24(d)1--3b: its `L` is the quotient of an independently
identified descendant external-leg component inside an exhaustive LSZ
decomposition and is defined only for a nonempty class.

**⟨2⟩5. Normalisation interface.**  No step obtains `1/(2S)` from the exact
charge-created/asymptotic-leg conversion.  That conversion supplies only
`Z_rho^{-1/2}` in the LSZ limit.

*Justification.*  D24(b)(i)--(ii), D24(d)2--3b, and claim `AMP`'s stated
normalisation obstruction.

**⟨2⟩6. QED.**

## 4. Why the four named components do not yet follow

### ⟨1⟩5. Aggregate matching does not determine component estimates

**ASSUME.**  Only the scalar identity (PL.4), D24's existing prose names for
the descendant, orthogonal-current, and direct-contact contributions, and
the two D29 window-boundary-gradient names in `(PROTO-LSZ)`.

**PROVE.**  These data do not by themselves prove the component-level
statements (SPEC.3)--(SPEC.5).

**⟨2⟩1.**  Let `b(h)` be any nonzero bounded smooth function on `I` and put
`B(k,h)=k b(h)`.  Starting with any scalar split whose descendant and
orthogonal contributions are `E_desc` and `E_perp`, the replacement

`E_desc -> E_desc+B`,  `E_perp -> E_perp-B`                  (PL.8)

leaves their sum, hence every whole-datum equality in ⟨1⟩3, unchanged.

*Justification.*  Linear algebra and named computation **PLSZ-C4** in
`proto_lsz_check.py`.

**⟨2⟩2.**  The added orthogonal term in (PL.8) is generically `O(epsilon)`
on a scale-tied packet, not `O(epsilon^2)`.  Therefore a whole-datum match,
even an exact one, cannot certify the required orthogonal-channel bound.

*Justification.*  D29's support `|k|=Theta(epsilon)` and named computation
**PLSZ-C4**, whose live shift has norm proportional to `epsilon` while its
compensating sum is invariant.

**⟨2⟩3.**  The same ambiguity can move a linear function between the
descendant and direct-contact labels, and scalar matching contains no data
that distinguishes either finite-window boundary gradient.

*Justification.*  ⟨2⟩1 and D24(d)1,4,5; `(PROTO-LSZ)` in
`theory/soft-index-r2.md` (SPEC.3)--(SPEC.5).

**⟨2⟩4.**  Calling the exact scalar witness (PL.1) “the descendant” and
setting the other three labels to zero would therefore make exhaustiveness
true by a relabelling, precisely the move excluded by the standing brief.

*Justification.*  ⟨2⟩1--⟨2⟩3 and the explicit no-definitional-exhaustiveness
sentence following (SPEC.5) in `theory/soft-index-r2.md` ⟨1⟩8.

**⟨2⟩5. QED.**

### ⟨1⟩6. Exact remaining positive lemma `(COMP-HS)`

**ASSUME.**  The same finite D29 sequence and separated geometry as
`(D29-HS-SEP)`.  At finite volume use D29(5)'s exact split
`J^-_k=P_{lambda,N}J^-_k+(1-P_{lambda,N})J^-_k` and the exact Duhamel contact
defect, without replacing the full-sector Gram operator by a scalar.

**PROVE.**  Full `(PROTO-LSZ)` on this subclass would follow from the
following single model lemma:

**(COMP-HS).**  The finite Duhamel/readout functional admits four
independently defined terms, obtained respectively from the descendant-range
current projection, the complementary current projection, the direct
source/contact functional, and the two window gradients, such that on the
ordered outer limit:

1. the descendant quotient converges in D24(b)'s packet norm to a uniformly
   `C^1` multiplier `L_S^desc` with
   `L_S^desc(0,h)=L_S^sc(0,h)` (equivalently,
   `L_S^desc-L_S^sc=O(k)` uniformly on the compact rectangle);
2. the complementary-current and direct-contact terms are each
   `O(epsilon^2)` uniformly on `I`;
3. the sum of the two window-gradient terms is `o(epsilon)` under `(SEP)`;
4. the limiting descendant construction exhibits a nonzero microscopic
   member of `𝒮_W(ρ)|_{ρ=S}` in D24's source register.

**⟨2⟩1.**  Given item 1, the first term differs from the right side of
(PL.4) by `O(epsilon^2)` and has the D24(d)3b profile with coefficient
`1/(2S)`.

*Justification.*  ⟨1⟩2--⟨1⟩3, D29's scale-tied support, and
D24(d)2--3b.

**⟨2⟩2.**  Items 2--3 give (SPEC.5), with the two boundary gradients grouped
exactly as `(PROTO-LSZ)` groups them.

*Justification.*  `(PROTO-LSZ)` in `theory/soft-index-r2.md` (SPEC.3)--
(SPEC.5).

**⟨2⟩3.**  Item 4 supplies the nonemptiness antecedent needed for D24's class
constant to be defined rather than merely naming the scalar coefficient in
(PL.2).

*Justification.*  D24(d)3b and claim `ML5-B`'s explicit nonemptiness fence.

**⟨2⟩4.**  Hence `(COMP-HS)` plus ⟨1⟩2--⟨1⟩3 proves full
`(PROTO-LSZ)` for `(D29-HS-SEP)` without changing any D-number.

*Justification.*  ⟨2⟩1--⟨2⟩3 and the exact statement (SPEC.3)--(SPEC.5).

**⟨2⟩5.**  A viable attack is a two-body fibre limiting-absorption/Feshbach
estimate: insert the full-sector descendant projector before taking the
Jacobi boundary resolvent, prove a uniform reduced-resolvent bound on compact
`I`, and pass the resulting four finite functionals through the already
proved `(SEP)` norm bridge.  This directly tests items 1--3 rather than
inferring them from their sum.

*Justification.*  D29(5), PROVED claim `S-IDX-fin-r2`, D31's fixed-packet
wave-operator machinery, and the named forward attack `ML4` in
`theory/soft-current-recon.md` ⟨1⟩7.

**⟨2⟩6.**  No existing PROVED claim supplies `(COMP-HS)`: the finite Ward
theorem does not give volume-uniform reduced-channel regularity, while the
matching theorem controls only the sum after the outer limit.

*Justification.*  Claims `S-IDX-fin-r2`, `S-IDX-MATCH-HS-SEP`, and `ML5-B`;
D24(d)4 explicitly records the missing uniform implication.

**⟨2⟩7. QED.**

## 5. Checker contract

### ⟨1⟩7. Red-capable finite corroboration

**ASSUME.**  The lane-local script `proto_lsz_check.py` and its saved output
`proto_lsz_check.out`.

**PROVE.**  The computation corroborates every scalar algebraic identity used
above and certifies no component provenance.

**⟨2⟩1.**  **PLSZ-C1** checks the removable profile (PL.2) on both physical
signs for `S=1/2,1,3/2,2`; `--red-profile` doubles the target and exits one.

*Justification.*  Named computation **PLSZ-C1** in `proto_lsz_check.py` and
the recorded optimized run in `proto_lsz_check.out`.

**⟨2⟩2.**  **PLSZ-C2** checks the exact pointwise factor (PL.7);
`--red-ward-factor` drops the Ward factor two and exits one.

*Justification.*  Named computation **PLSZ-C2** and the saved output.

**⟨2⟩3.**  **PLSZ-C3** checks packet aggregation and the `1/S` first jet;
`--red-slope` changes it to `1/(S+1)` and exits one.

*Justification.*  Named computation **PLSZ-C3** and the saved output.

**⟨2⟩4.**  **PLSZ-C4** checks that a live `O(epsilon)` transfer between two
untyped components leaves their sum invariant; `--red-split` removes the
compensation and exits one.

*Justification.*  Named computation **PLSZ-C4** and the saved output.

**⟨2⟩5.**  Green exits zero under `python3 -O`; all four registered red modes
exit one.  The script contains no bare `assert`.

*Justification.*  `proto_lsz_check.out` and inspection of
`proto_lsz_check.py`.

**⟨2⟩6.**  The gates test no thermodynamic limit, wave operator, D24 source
membership, descendant projector limit, orthogonal-current estimate,
direct-contact estimate, or window-boundary estimate.

*Justification.*  The declared scope of `proto_lsz_check.py`; analytic input
for the scalar outer-limit bridge is PROVED claim `S-IDX-MATCH-HS-SEP`.

**⟨2⟩7. QED.**

## 6. MERGE PROPOSALS

No existing file is edited by this lane.  The following row is a proposal
only and deliberately stays at `SKETCH` pending the campaign's capped hostile
review/adjudication:

> | S-IDX-PROTO-SCALAR-HS-SEP | On the fully polarised bilinear ferromagnet `H_S`, `2S in N`, and the separated-preparation subclass `(D29-HS-SEP)`, every actual D29 row-measure limit point has the exact scalar factorisation `A_*=int(e^{ik}-1)L_S^sc(k,h)[2iv_h]dmu_*`, where `L_S^sc=[S_phys-1]/[(e^{ik}-1)2iv_h]` has a uniformly `C^1` extension `L_S^sc(0,h)=-i sgn(v_h-v_s)/(2Sv_h)`.  The coefficient comes only from `S-IDX-MATCH-HS-SEP` followed by `S2-2body-S`.  This row does not identify `L_S^sc` with D24's descendant quotient, prove microscopic `𝒮_W` membership, or prove the orthogonal-current/direct-contact/window component bounds of `(PROTO-LSZ)`. | SKETCH | S-IDX-MATCH-HS-SEP, S2-2body-S, D24(b) | `theory/lanes/blitz-2026-08-29/proto-lsz/proto-lsz.md` ⟨1⟩1--⟨1⟩7 | `theory/lanes/blitz-2026-08-29/proto-lsz/proto_lsz_check.py` PLSZ-C1--C4; scalar algebra only |

Do not promote `S-IDX-spec-struct-r2`: `(COMP-HS)` remains open.  Do not
alter `S-IDX-MATCH-HS-SEP`, `S-IDX-D29-value-HS-SEP`,
`S-IDX-HR-value-r2`, D24, D29, or D30.

### ⟨1⟩8. Final status

**ASSUME.**  The complete ladder above.

**PROVE.**  The result is honestly labelled.

**⟨2⟩1.**  Positive result: the LSZ-shaped scalar protocol factorisation,
including its uniform quotient profile and exact packet identity, is proved
on `(D29-HS-SEP)`.

*Justification.*  ⟨1⟩2--⟨1⟩3 and PROVED claims
`S-IDX-MATCH-HS-SEP`, `S2-2body-S`.

**⟨2⟩2.**  Remaining result: full `(PROTO-LSZ)` is not proved because
`(COMP-HS)` items 1--4 have not been established for independently defined
components.

*Justification.*  ⟨1⟩5--⟨1⟩6 and D24(d)1--5.

**⟨2⟩3.**  Therefore the lane status is **PARTIAL**, not
`PROVED-candidate`.

*Justification.*  PRD.md goal 2 and the blitz rules' honest-label contract.

**⟨2⟩4. QED.**
