<!-- ROLE: L6 critic verdict, round 1, on theory/TRIANGLE.md,
     theory/corner-b-draft.md, and theory/spt-scoping-draft.md.
     Critic: Codex. Date: 2026-08-26. -->

# Critic verdict r1 — `TRIANGLE.md` and the two reconciled drafts

Critic: Codex, adversarial pass under L6/L6b/L10.  I read `CLAUDE.md`,
`notation.md`, `definitions.md`, the claims DAG, the three targets, and the three
converged verdicts in the requested order.  I treated the Corner-A, Bethe-oracle,
and ML2 results as fixed and did not re-litigate them.  I audited every status in
`TRIANGLE.md` against both the DAG and the cited shard, independently checked the
B3 charge arithmetic and the SPT representation theory, and searched all three
targets for the negative rows `A2-orbit-r1`, `G0-soft-r1`, and the brief's
Conjecture M.

The result is not a close pass.  The frozen summary certifies several artifacts
as `PROVED` even though no L6 verdict exists for them; B3(ii), one of the two
parts advertised as proved, is false in the elementary transmitted channel; and
the SPT dichotomy rests on the invalid inference that an honest adjoint
representation cannot retain information about the projective class.  The
surviving weaker package is substantial: the converged Corner-A/oracle/ML2
results, the exact finite-window flux identity, the conditional charge
bookkeeping of M-quant, and the statement that closed contractions are invariant
under rephasing of a *fixed* projective lift.

## Checker record

I ran the required command verbatim:

```text
for f in theory/checks/*.py; do python3 -O "$f"; done
```

All seven scripts exited successfully:

1. `corner_a_check.py`: C0--C11, **ALL PASS**.
2. `crosscheck_corner_b_tk.py`: all `main-*`/`Dscan-*` rows pass; reported
   Fano/scan ratios `1.009--1.058`.
3. `ml2_completeness_check.py`: all listed sizes pass.
4. `ml4_check.py`: Ward/projection checks pass; amplitude exponent
   `1.99700--1.99988`; red exponent `0.9999`; source obstruction passes.
5. `mquant_check.py`: flux operator residue `0`, finite-time residue
   `3.366e-16`; scan certificate passes its `0.005563` budget.
6. `oracle_bethe_check.py`: O1--O10 pass.
7. `soft_current_recon_check.py`: charge/current/Ward/contact checks pass.

There is no checker for B3 or any SPT row.  The green run therefore supplies no
evidence for the objections below concerning those claims.

---

## I. `theory/TRIANGLE.md`

### T1. FATAL — the freeze launders unreviewed shards into `PROVED` statuses

**Locations.** `theory/TRIANGLE.md:2-5`, `:10-13`, `:168-209`, `:244-271`,
`:281-326`, and freeze-index rows `:482-488`; compare `CLAUDE.md:31-38`.

The document defines `PROVED` to mean “complete argument in a shard that passed
its L6 loop” (`:10-11`) and says every statement was copied from a converged
artifact (`:4`).  The complete verdict inventory contains only the Corner-A,
oracle, and ML2 r1/r2/r3 files.  There is no verdict at all for
`soft-current-recon.md`, `ml4-ward-reduction.md`, `ml5-universality.md`,
`memory-quantization.md`, `corner-b-draft.md`, or `spt-scoping-draft.md`.  The
last two explicitly say `DRAFT, pre-critic`.

The exact unlicensed positive tags are S2-2body at `:168` and `:482`;
ML4/ML4-A at `:246`, `:253`, `:258`, `:484-485`; ML5-B/ML5 at `:267` and
`:486`; M-flux at `:281` and `:487`; and M-quant at `:295`, `:311`, and `:488`.
The composite `COMPUTED` tags at `:328`, `:343`, and `:489-490` agree with the
DAG prose but use a status not permitted by L5.

The status audit is therefore:

| TRIANGLE item | DAG agreement | L6-valid under TRIANGLE's own definition? |
|---|---|---|
| IT/WI/A1/A2/G0; A2-orbit-r1/G0-soft-r1 | yes | **yes**, Corner-A r3 passed |
| O1--O10 | source passed, but there are no dedicated O1--O10 DAG rows; OR1/OR2 are instead `VERIFIED` | **yes as oracle facts**, but not row-for-row DAG-complete |
| ML2 | yes | **yes**, ML2 r2 passed |
| S2-2body | DAG says `PROVED` | **no verdict exists** |
| S-general; ML1/ML3/ML6 | DAG says `CONJECTURE`/`OPEN` | status words agree; no positive promotion is at issue |
| ML4/ML4-A | DAG says one-hard `PROVED`, higher channel `OPEN` | **no verdict exists** |
| ML5/ML5-A/ML5-B | DAG has the same composite status | **no verdict exists** |
| M-flux and M-quant | DAG has the same positive statuses | **no verdict exists** |
| t(k), soft memory zero | DAG uses `COMPUTED`/composite prose | **not an L5 status at all** |
| Bc | DAG says `CONJECTURE` | no positive promotion is at issue |
| SPT-nogo/B/E/T/D/M | DAG wording is draft `SKETCH`/`CONJECTURE` | pre-critic, correctly non-PROVED, but SPT-nogo is omitted from the freeze table |

Thus agreement with `CLAIMS.md` is not enough: the DAG has itself been upgraded
in violation of L5's rule that upgrades occur only after L6 convergence.  This
is the primary summary-document failure the brief asked the critic to catch.
The D13--D24 promotion trace has the same shape: D13--D18
(`definitions.md:564-695`) feed M-flux/M-quant/M-tk/B3, D19--D23
(`definitions.md:699-793`) feed the five SPT rows, and D24
(`definitions.md:797-850`) feeds S-general/ML5.  Their package names agree
syntactically with the DAG, but D18 is not the H-AD proved by M-quant (T4), and
D24 embeds a `PROVED` criterion at `definitions.md:822-826` without an L6
verdict.  Promotion into the definitions file did not adjudicate either claim.

**Fix demand.** Downgrade every positive row without a verdict to `SKETCH` or
`DRAFT` (retaining `REFUTED` counterexamples), or run the missing L6 loops and
record their verdicts before restoring `PROVED`/`THEOREM`.

### T2. MAJOR — the freeze rule contradicts §5 and uses an uncontrolled status vocabulary

**Locations.** `theory/TRIANGLE.md:10-13`, `:378-382`, `:469-500`; compare
`CLAUDE.md:31-33` and `claims/CLAIMS.md:3-6`.

Section 5 says “DRAFT status, not frozen” and “Nothing in this section has been
through an L6 loop” (`:378-382`), while the freeze rule says changing **any
statement above** requires reopening the relevant L6 loop (`:499-500`).  There
is no relevant completed loop to reopen for §5.  The status legend also omits
statuses the freeze index actually uses: `OPEN`, `COMPUTED`, `THEOREM`, `FALSE`,
and composite “partly/conditionally proved” labels.  `CLAUDE.md` itself permits
only `PROVED | SKETCH | CONJECTURE | REFUTED`; the DAG header separately adds
`RETRACTED | OPEN | VERIFIED` but not `COMPUTED` or `THEOREM`.

**Independent check.** Reading `:378` and `:499` literally gives both “§5 is not
frozen” and “every statement in §5 is frozen.”  No interpretation of “above”
removes the contradiction.

**Fix demand.** Define one authoritative status enum, exclude §5 explicitly
from the freeze rule until its first verdict, and distinguish frozen definitions
D19--D23 from unfrozen claims built on them.

### T3. FATAL — B3(ii)'s `PROVED` formula is false in the theorem's own transmitted channel

**Locations.** `theory/TRIANGLE.md:450-452`, `:497`; source
`theory/corner-b-draft.md:606-616`; DAG `claims/CLAIMS.md:30`.

Take the advertised `s=1/2` one-magnon transmitted branch, with the cut `c`
between the wall window and the outgoing transmitted magnon.  Initially
`q_c^R=0`; finally the up magnon/hole on the down vacuum carries
`Delta q_c^R=+1`, exactly as M-quant's AD3 states.  M-quant gives
`delta x=-1/s=-2`.  B3(ii) instead gives

```text
delta x = (1/(2s)) Delta q_c^R = +1.
```

The left formula fails too: removing the incoming charge `-1` gives
`Delta q_c^L=+1`, hence B3 predicts `-1`, not `-2`.  This is a sign and factor-of-
two contradiction, not an omitted hypothesis.  The cut-dependent half-line
charge also contains a wall contribution if the cut is moved across the wall,
so the assertion “for any cut outside the leg content” cannot repair it.

The surviving event-specific transport statement is the charge bookkeeping
already proved conditionally in M-quant:
`2s delta x + (q_out-q_in)=0`; for the two-channel one-magnon event this is
`delta x=-(1/s) Delta N_T`.  It is not the displayed B3(ii) identity.

**Fix demand.** Retract B3(ii), replace it by the conserved-total-charge formula
with explicit cut geometry and leg subtraction, and re-run the B3 proof/status
loop before any promotion.

### T4. FATAL — “H-AD is proved for the projection” changes the meaning of H-AD

**Locations.** `theory/TRIANGLE.md:34`, `:295-318`; `definitions.md:679-695`;
source `theory/memory-quantization.md:100-147`, `:151-265`.

D18 defines H-AD as norm-closeness of the in/out **state** to a convex
combination of product configurations.  `memory-quantization.md` defines a
different H-AD: coherent Møller wave operators, an orthogonal channel
decomposition, and local decay.  The projected proof establishes the latter.
It does not establish D18's norm-mixture statement.

Indeed D18's statement is generically false for the superposed event used in
the same theorem.  If
`|psi_out> = r|R> + t|T>` with orthogonal separated channels and `rt != 0`, the
pure density matrix retains off-diagonal terms
`r conjugate(t)|R><T| + h.c.`.  Its norm distance from the convex mixture
`|r|^2|R><R|+|t|^2|T><T|` does not tend to zero; only suitable local matrix
elements can lose the cross term.  The variance claim at `:303` likewise uses
the coherent projection-valued version, not D18's convex mixture.

**Fix demand.** Replace D18 by the AD1--AD4 wave-operator/local-decay
definition, or state and prove the precise weak/local topology in which a
mixture approximation is meant; until then do not identify the projected proof
with D18.

### T5. MAJOR — M-flux is silently strengthened from physical current to virtual bond data

**Locations.** `theory/TRIANGLE.md:289-291`; source
`theory/corner-b-draft.md:267-287`; compare G0(d) at
`theory/TRIANGLE.md:128-129` and `definitions.md:483-489`.

The exact flux identity proves that the time derivative of `X_W` is the
difference of the **physical currents** `j` through the window boundaries.
G0(d) proves a different equation on the vacuum:

```text
q_x ▹ omega_alpha = (Jcal_{x|x+1}-Jcal_{x-1|x}) ▹ omega_alpha.
```

It does not say that the physical current `j` is a divergence of `Jcal`, nor
does it turn the time integral of `j` into a difference of virtual insertions.
The two glyphs were conflated.  Moreover D10(d) is explicitly unbroken-vacuum
only, while the memory event is in a broken kink sector.

The surviving proved statement is exactly Mq-flux: memory is the finite-time
DC boundary-current flux.  “Memory is a difference of virtual/bond data” remains
an unproved Corner-A-to-kink extension.

**Fix demand.** Delete the virtual/bond-data conclusion from M-flux or supply a
new kink-sector theorem relating the integrated physical current to endpoint
virtual insertions.

### T6. MAJOR — the memory theorem violates the document's own generality directive

**Locations.** `theory/TRIANGLE.md:15-18`, `:297-300`, `:311-326`; DAG
`claims/CLAIMS.md:41`; source `theory/memory-quantization.md:8-38`, `:153-159`.

The standing directive says the memory law is stated in general
`(G, injective MPS, finite-range H)` form and XXZ is only an instantiation.  The
actual theorem assumption (A2) requires evolution by `H_XXZ`/D16, and the only
unconditional projected completeness theorem is for the spin-`1/2`,
`<=3`-domain-wall graph.  Conversely, the charge-bookkeeping proof uses much
less than XXZ: a conserved `U(1)`, two asymptotic charge densities, and a
two-channel asymptotic decomposition.  The summary has neither stated the
general conditional theorem generally nor confined the unconditional theorem
to its spin-`1/2` oracle.

**Fix demand.** Split the result into (i) a general conditional charge theorem
for finite-range `U(1)`-invariant dynamics with explicit channel hypotheses and
(ii) the spin-`1/2` XXZ `H_3` verification.

### T7. MAJOR — the freeze table drops open obligations and then says A => C is closed at `n=1`

**Locations.** `theory/TRIANGLE.md:198-205`, `:231-242`, `:483`, `:495`;
compare `claims/CLAIMS.md:19`, `:45-48`.

The S-general row at `:483` lists only ML1, ML3, and ML6, omitting the same
document's open ML4 three-magnon channel and open proof that a nontrivial
microscopic source class lies in `S_W`.  Row `:495` then says A => C is “closed
at n=1,” although §2.3 itself says the process-independent statement still
needs ML3 and source-class membership and boxes the amplitude factorisation as
conditional on ML1/amputation.  `ML5-B` is an implication **for an already
assumed member of `S_W`**; it does not prove that the physical source is a
member.

**Fix demand.** List all five live obligations in the S-general and A => C
freeze rows and replace “closed at n=1” by the exact weaker statement “ML4's
orthogonal-current reduction is closed for one hard magnon.”

### T8. FATAL — §5 contains mutually contradictory claims about what an edge coefficient can see

**Locations.** `theory/TRIANGLE.md:389-400`; definitions
`definitions.md:738-742`, `:746-764`; source
`theory/spt-scoping-draft.md:196-225`, `:281-291`.

The no-go says `[omega]` cannot appear in **any coefficient**, at any order,
even at an edge.  SPT-E then says the `k -> 0` edge residue is a half-integral
charge for AKLT and an integral charge for TRIV, acts in dimension at least
`d_omega`, and is valued in the `[omega]`-twisted lattice.  The `k -> 0` residue
is the zeroth coefficient of the form factor.  Its eigenvalues, dimension, and
selection rules are coefficient data.  Calling those differences
“representation type” does not make them cease to be data of the coefficient.

The contradiction reflects the false representation-theory inference attacked
as S2--S3 below.  The weaker defensible no-go is only: a closed contraction is
invariant under rephasing a fixed lift, and the local Lie bracket contains no
central term for compact semisimple `g`.  Neither statement proves independence
from the global projective class.

**Fix demand.** Withdraw SPT-nogo in its all-orders/all-registers form and state
only the rephasing/central-term facts until an actual pair of amplitudes has been
computed.

### T9. MAJOR — the advertised SPT deciding computation is not decisive

**Locations.** `theory/TRIANGLE.md:409-414`; source
`theory/spt-scoping-draft.md:516-532`.

An `Ad(V)`-only bulk contraction need not be `[omega]`-blind, because two
projective classes can induce inequivalent honest adjoint representations.  A
single unpaired `X` on an open virtual index, on the other hand, is already the
fundamental-theorem endpoint algebra; it does not establish a scattering soft
factor, an edge-label-changing reflection amplitude, or memory.  If the
half-infinite contraction returned `Ad(V)`, that would also not refute SPT
sensitivity for the same reason.  The two proposed branches therefore do not
decide the listed claims.

**Fix demand.** Replace the branch rule by an explicit comparison of normalized
matrix elements for fixed tensors, fixed boundary Hamiltonians, and a specified
`k`-dependent packet family, with distinct tests for bulk rephasing invariance,
edge representation data, and dynamical reflection/memory.

### T10. MINOR — the frozen document contains a duplicated, interleaved paragraph

**Locations.** `theory/TRIANGLE.md:402-410`.

“A closed route” appears twice, the first copy ends mid-sentence at “truncated,”
and the orphan text at `:408` begins with the AKLT/TRIV objects before “The one
deciding computation” starts again.  This is not merely repeated prose; the
logical order of the frozen §5 handoff is corrupted.

**Fix demand.** Remove the incomplete duplicate and restore one continuous
closed-route paragraph followed by one deciding-computation paragraph.

### T11. MINOR — the reflection soft expansion drops its remainder

**Location.** `theory/TRIANGLE.md:345-346`; source
`theory/corner-b-draft.md:451-459`.

From the displayed exact `T`, the valid pair is
`T=16(Delta-1)^2 k^2+O(k^4)` and
`R=1-16(Delta-1)^2 k^2+O(k^4)`.  The summary omits the `O(k^4)` only from `R`,
turning an asymptotic equality into a false exact one.

**Fix demand.** Add `+O(k^4)` to the `R(k)` expansion.

### T12. NOTE — the negative-row text is present only as withdrawal/history

**Locations.** `theory/TRIANGLE.md:136-141`, `:352-359`, `:459-465`,
`:479`, `:491`.

The literal strings `A2-orbit-r1`, `G0-soft-r1`, and Conjecture M occur in
TRIANGLE only in explicit negative rows or historical withdrawal clauses.  I
found no direct positive citation of any of the three.  T5 and T8 are new
overreads of surviving claims, not a textual resurrection of the old rows.

**Fix demand.** None for textual purge; retain these negative rows when the
substantive repairs above are made.

**TRIANGLE section verdict: FAIL(T1, T2, T3, T4, T5, T6, T7, T8, T9).**

---

## II. `theory/corner-b-draft.md`

### B1. FATAL — B3(ii)'s half-line-charge equation fails by sign and factor two

**Locations.** `theory/corner-b-draft.md:593-616`, status claim `:642-647`, and
summary `:752-759`.

The independent transmitted-channel calculation in T3 directly refutes the
display.  With `s=1/2` and a cut between the wall and transmitted leg,
`Delta q_R=+1` while `delta x=-2`; the draft predicts `+1`.  The equation also
cannot be independent of the cut unless the wall and leg contributions are
specified and subtracted separately.

**Fix demand.** Retract B3(ii) and replace it with
`2s delta x + q_out-q_in=0`, specializing only after fixing the cut and channel.

### B2. MAJOR — B3(i) is true-looking but its stated proof does not prove label rigidity

**Locations.** `theory/corner-b-draft.md:597-604`; DAG dependency row
`claims/CLAIMS.md:30`.

Preservation of disjointness by an automorphism proves only that distinct
sectors remain distinct under the automorphism.  It does not prove that the
automorphism fixes each label instead of permuting labels.  A global symmetry
automorphism is the immediate counterexample to that inference.  For XXZ time
evolution the desired conclusion should follow from symmetry invariance of the
vacua plus a finite-time Lieb--Robinson estimate applied to the factorized D9(a)
boundary conditions, but none of those steps is given.

**Fix demand.** Supply a Lamport proof that the finite-time dynamics fixes both
asymptotic vacuum functionals in D9(a), with the LR estimate and stationary-
vacuum hypotheses explicit; downgrade (i) until that proof passes L6.

### B3. MAJOR — the two `PROVED` B3 parts are not L6b-structured, and one cites a nonexistent result

**Locations.** `theory/corner-b-draft.md:591-647`, especially `:614-616`;
compare `CLAUDE.md:39-45`.

B3 is a block quote with roman clauses and prose “Proof” paragraphs.  It has no
hierarchical `ASSUME/PROVE` tree, no numbered leaves, and no terminal QED for the
proposition.  Part (ii) cites “Proposition N,” but no such proposition exists in
the repository.  The likely intended referent is G0(d)/D10(d), which says
something different and has the wrong register (see B4).  Hence the requested
Lamport audit fails even before the arithmetic failure B1.

**Fix demand.** Rewrite B3 as a genuine L6b proof whose leaves cite existing
D-numbers/claim ids or named computations, then submit it to an L6 critic.

### B4. MAJOR — the draft declares rigorous exactly the kink-sector extensions it lists as missing

**Locations.** `theory/corner-b-draft.md:280-287`, `:614-616`, status
`:642-647`, versus open interface requirements R1/R3 at `:653-658`.

The draft uses D10(d) to identify kink half-line charge with a virtual bond
quantity and calls B3(ii) rigorous.  But R1 explicitly says D10(d) is currently
unbroken-only and must be extended to `alpha != beta` for Eq. (2.2) and B3(ii),
while R3 asks for existence/uniqueness of that half-line charge in a kink
sector.  An argument cannot be `PROVED` while two of its own stated interface
requirements remain unsupplied.

**Fix demand.** Remove the virtual-charge identification and downgrade B3(ii),
or close R1/R3 with actual kink-sector theorems before citing them.

### B5. MAJOR — H-AD's norm-mixture formulation is not the wave-operator hypothesis that supersedes it

**Locations.** `theory/corner-b-draft.md:21-25`, Theorem M-prime assumptions
`:491-513`, and status `:558-566`; compare
`theory/memory-quantization.md:100-147`.

The header says M-prime is superseded by `memory-quantization.md`, but the draft
continues to define H-AD as norm-closeness to a convex mixture.  As shown in T4,
that excludes a generic coherent reflected/transmitted state and is not what
the projected wave-operator proof establishes.  Consequently “H-AD proved for
the projection” cannot be back-propagated to this theorem as written.

**Fix demand.** Mark this H-AD formulation obsolete and point all consumers to
one corrected AD1--AD4 definition with an explicit topology.

### B6. MAJOR — K4 is used as a theorem although the draft itself records only evidence and an open proof

**Locations.** `theory/corner-b-draft.md:144-155`, B3(iii) `:618-623`, status
`:644-645`, R5 `:659`, prediction P5 `:726-730`, and honest status `:767-770`.

K4 claims uniqueness of one zero-energy state per charge sector in the
thermodynamic limit, exact flatness, no effective mass, and no recoil.  Its
support is explicitly labelled “Evidence,” and `:155`, R5, and `:769` all admit
the thermodynamic uniqueness proof is missing.  Yet B3(iii) cites “K4: one state
per magnetisation sector,” and P5 quantifies “at any `k_0`, at any `Delta>1`” as
if K4 were proved.  `memory-quantization.md` carefully avoids this by using only
K1--K3 in the projected graph.

**Fix demand.** Keep K4/R5 and all no-recoil consequences at `CONJECTURE` (or
projected-computation scope) until thermodynamic uniqueness/flatness is proved.

### B7. MAJOR — “integer-quantised for spin s” is false at the stated quantifier

**Locations.** `theory/corner-b-draft.md:37-49`, `:618-623`, `:744-746`;
compare `theory/memory-quantization.md:32-38`, `:360-369`.

The formula gives a channel displacement `-1/s`.  For general site spin this is
not an integer (for example `s=3/2` gives `-2/3`).  The projected completeness
proof exists only for spin `1/2`; the spin-1 item is a proposed numerical test,
not a theorem; and no higher-spin channel analysis shows that a one-magnon
event stays within a pure translated-kink torsor.  Moreover the expectation
`-<N_T>/s` is continuous even for `s=1/2`; only the spectral channel outcomes
are discrete.

**Fix demand.** Say “channel-quantised with spectrum `{0,-1/s}`” and restrict
the proved projected statement to spin `1/2`; treat higher spin as a conjectural
charge-bookkeeping extension with channel existence owed.

### B8. MAJOR — the tail error uses the forbidden bare transfer rate

**Locations.** `theory/corner-b-draft.md:251-265`, `:323-328`,
Theorem M-prime `:527-531`; promoted form `definitions.md:584-590`; compare
`definitions.md:47-54`.

The draft repeatedly uses `O(exp(-L/xi_c)) = O(lambda_E^L)`.  D1(c) explicitly
says this bare rate is false in the presence of a Jordan block at modulus
`lambda_E`; the valid uniform statement is: for every
`lambda_tilde in (lambda_E,1)` there is a constant with
`O(lambda_tilde^distance)`.  The distance must also be the core-to-boundary
padding, not automatically the full window length `b-a`.

**Fix demand.** Replace every bare `exp(-L/xi_c)` theorem error by the D1(c)
`C_lambda_tilde lambda_tilde^d` bound with `d` the minimum core-to-window-edge
distance.

### B9. MAJOR — §10 contradicts the shard's own B3 split status

**Locations.** `theory/corner-b-draft.md:642-647` versus `:752-759`.

Section 7 says (i),(ii) rigorous and (iii),(iv) SKETCH.  Section 10 lists
“Proposition B3 (i)--(iv)” under **What is proved**.  This is an exact status
mismatch even before B1--B4 show that (i),(ii) are not proved either.

**Fix demand.** Move B3 out of “What is proved” and list each clause with its
actual post-critique status.

### B10. NOTE — the withdrawn A2/O7 phrasing is textually purged

**Locations.** `theory/corner-b-draft.md:9-18`, `:55-62`, `:475-483`,
`:597-601`, `:625-640`, `:770-779`.

Every occurrence of `A2-orbit-r1` is a dated withdrawal; the active B3 wording
uses the vacuum pair/double coset.  O7 is quoted with
`2 sgn(v_h-v_s) k_s` and the number `2` is explicitly restricted to D8.  The
brief's Conjecture M is carried only as a refutation.  No stale textual reliance
survives.  The failures B1--B9 are independent new defects.

**Fix demand.** None for the textual purge.

**Corner-B section verdict: FAIL(B1, B2, B3, B4, B5, B6, B7, B8, B9).**

---

## III. `theory/spt-scoping-draft.md`

### S1. FATAL — the central soft object is ill-typed and its limit is undefined

**Locations.** `theory/spt-scoping-draft.md:102-124`; promoted definitions
`definitions.md:722-742`.

`F_f` is defined as a matrix element, hence a complex scalar.  Sd7/D20 then
declares its limit to be an element of the twisted group algebra acting on
virtual data.  A scalar matrix element cannot simultaneously be the
operator/algebra element represented between the legs.  The draft must choose
an operator-valued endpoint insertion first and only then take its matrix
elements.

The notation `lim_{k->0} F_f` is also undefined: no family `f_k` (or `f_L` with
`L->infinity`) and no `k`-dependent external states are specified.  The edge
profile `1_[0,infinity)` has no `k` parameter at all.  These are definition-level
failures in D19--D20, so none of SPT-B/E/T/D/M is presently a well-posed soft
claim.

**Fix demand.** Define an operator-valued amplitude in a fixed Hilbert/register,
specify the packet/profile family and order of limits, and define scalar form
factors only as its matrix elements.

### S2. FATAL — “only `Ad(V)` enters” does not imply `[omega]`-independence

**Locations.** `theory/spt-scoping-draft.md:159-190`, SPT-B statement
`:244-261`, proof `:363-381`; DAG `claims/CLAIMS.md:31`.

Phase cancellation proves that `Ad(V)` is an honest linear representation and
is invariant under rephasing a fixed lift.  It does **not** prove that its
isomorphism type is independent of the projective class.  The draft confuses
“the multiplier cancels from the multiplication law” with “no information
correlated with the multiplier remains.”

The draft's own D2 example is a counterexample.  For the nontrivial projective
class take `V(R_x)=sigma_x`, `V(R_z)=sigma_z`.  Conjugation on
`M_2 = span{I,sigma_x,sigma_y,sigma_z}` is an honest D2 representation, but it
decomposes into four one-dimensional character sectors.  For the stated
trivial representative `V=I`, `Ad(V)` is the trivial representation.  Closed
contractions can distinguish these adjoint data even though both adjoint
actions have zero multiplier.

The surviving weaker theorem is only invariance under
`V(g)->lambda(g)V(g)` for a fixed projective representation.  The much stronger
sentence “identical for any two MPS with the same Ad data” is tautological and
does not imply that AKLT and TRIV have the same Ad data.

**Fix demand.** Downgrade SPT-B to rephasing invariance of a fixed lift and test
whether the actual adjoint representations/amplitudes of an explicit SPT/trivial
pair coincide; do not infer class-independence from linearity alone.

### S3. FATAL — the all-orders no-go misuses Whitehead's lemma and contradicts SPT-E

**Locations.** `theory/spt-scoping-draft.md:194-225`, SPT-E `:281-291`, verdict
`:502-505`; DAG `claims/CLAIMS.md:36`.

`H^2(so(3),R)=0` says the **Lie bracket has no central extension**.  It does not
say that infinitesimal representation matrices cannot distinguish integer from
half-integer representations: the spin-1/2 and spin-1 generators have different
dimension, Casimir, weights, and matrix elements even though both obey the same
uncentrally-extended Lie algebra.  Which Lie-algebra representation integrates
to SO(3), rather than only to SU(2), is precisely global information.

For finite D2 the premise is worse: there are no derivatives at the identity,
so the assertion that every coefficient is made from such derivatives does not
apply.  Finally SPT-E explicitly proposes a half-integral versus integral
`k=0` edge residue.  That residue is a coefficient and would distinguish the
two classes, directly contradicting the no-go.

**Fix demand.** Replace the no-go by the correct narrow statements: no
Lie-algebra central term for compact semisimple `g`, and no cocycle
*representative* in a paired contraction; leave global representation data open.

### S4. FATAL — the proposed deciding computation cannot decide either branch

**Locations.** `theory/spt-scoping-draft.md:414-424`, `:516-535`; comparison
pair `:41-57`.

The bulk criterion “returns an `Ad(V)`-only coefficient” does not establish
SPT-B by S2.  The edge criterion “returns one unpaired `X` on the open index” is
essentially D2/A1 endpoint algebra and does not establish any dynamical soft
limit, nonzero edge scattering matrix element, or memory.  The alleged
self-refutation branch (“if it collapses to `Ad(V)`, `[omega]` drops out
everywhere”) is false for the same reason: `Ad(V)` can retain class-correlated
representation data.

The computation is not executable as written either.  Sd1 supplies exact AKLT
tensors but no explicit normalized injective TRIV tensor; “any injective MPS”
and the approximate product `|0>^tensor` do not determine a transfer
contraction.  Requiring `chi=2` while taking `V=I` does not turn the chi-1 product
state into an injective chi-2 tensor.

**Fix demand.** Specify an exact trivial tensor and boundary Hamiltonian, compute
normalized scalar matrix elements for a defined packet family, and use decision
criteria that compare actual numbers/representations rather than the word
`Ad(V)`.

### S5. MAJOR — the finite-group and Lie-group soft constructions are conflated

**Locations.** `theory/spt-scoping-draft.md:41-57`, `:80-124`, `:167-171`, and
the pre-check `:414-420`; promoted D19/D20 at `definitions.md:706-742`.

The falsification pair fixes `G=D2`, a finite group with no `xi`, no `X(xi)`,
and no continuously modulated `f(x/L)g`.  Yet the deciding calculation is
`Q[f;xi]` and expects `X(xi)=i sigma_xi/2`, which belongs to a Lie-group
extension such as SO(3) or O(2).  For a finite group, the half-string step is a
valid discrete operation but there is no continuous `k->0` family obtained by
scaling a group element with a real profile.  For a Lie group, the global
projective class and the domain of the representation must be stated
separately.

**Fix demand.** Split the project into (i) Lie-group momentum-soft form factors
with a specified continuous group and (ii) finite-group endpoint/string
selection rules with no fictitious infinitesimal `k` limit.

### S6. MAJOR — symmetry protects an edge multiplet, not a nonzero flip amplitude at every momentum

**Locations.** `theory/spt-scoping-draft.md:221-225`, SPT-E `:263-291`, SPT-M
`:329-340`; DAG `claims/CLAIMS.md:32`, `:35`.

A nontrivial projective class can enforce a degenerate/projective edge
representation.  It does not force a particular charge operator to have a
nonzero off-diagonal matrix element, and it certainly does not force a magnon
reflection amplitude to change the edge label at **all** momenta.  Symmetry may
allow a channel while its matrix element vanishes by an additional selection
rule, fine tuning, or decoupling.  Likewise a trivial edge can have an
accidental low-energy boundary degree of freedom and nonzero memory; “gappable”
does not imply “is zero for the Hamiltonian under study.”

The honest surviving SPT-M seed is weaker: a projective edge multiplet is
symmetry-protected, so edge-changing channels may exist and obey projective
selection rules.  Quantized permanent memory requires a dynamical theorem and
an observable normalization, neither supplied here.

**Fix demand.** Replace “nonzero at all momenta” by a symmetry-allowed channel
statement and make nonzero reflection/memory a separately computed,
model-dependent conjecture.

### S7. MAJOR — SPT-T's formula is missing its abelian/gauge scope

**Locations.** `theory/spt-scoping-draft.md:304-316`; DAG
`claims/CLAIMS.md:33`.

`V(h)V(g)V(h)^{-1}` is proportional to `V(g)` only when `g` and `h` commute.
For a general group it is proportional to `V(hgh^{-1})`.  The ratio
`omega(h,g)/omega(g,h)` is the familiar commutator/slant phase for commuting
elements and depends on the cocycle convention; it is not the displayed
general endpoint identity.  The concrete D2 pair is abelian, but the claim and
D21 setup are written for general `G`.

**Fix demand.** Restrict SPT-T to commuting `g,h` (in particular D2), state the
normalization/cocycle convention, and formulate the observable as the relative
two-endpoint charge already required by the compensation caveat.

### S8. MAJOR — the shard calls SPT-B a theorem while retaining three proof obligations

**Locations.** `theory/spt-scoping-draft.md:28-35`, `:244-261`, proof gaps
`:356-360`, `:383-391`, and verdict `:487-505`; compare DAG
`claims/CLAIMS.md:31` (`SKETCH`).

The header says `[omega]` is “provably invisible”; `:256` calls SPT-B a
“genuine theorem”; and the verdict says items 1--2 are true.  The same shard
lists N1--N3 as open and says N3 can make SPT-B fail.  Even if the central
inference S2 were valid, those sentences would silently strengthen a SKETCH
row.  With S2 false, the theorem language is doubly untenable.

**Fix demand.** Use `SKETCH` consistently and state the surviving rephasing
lemma separately as the only presently proved algebraic step.

### S9. MINOR — the model-family prose conflates the AKLT point with the Heisenberg point

**Locations.** `theory/spt-scoping-draft.md:401-405`, pre-check `:414-420`.

`H(D)` at `D=0` is the spin-1 Heisenberg chain in the Haldane phase, not the
exact AKLT parent Hamiltonian of the tensors used in the proposed hand
contraction.  Phase equivalence makes both useful representatives, but it does
not make an exact AKLT contraction a calculation in the stated one-parameter
Hamiltonian family.

**Fix demand.** Call AKLT a fixed-point representative of the same phase and
separate its exact tensor test from the `H(D)` dynamical scan.

### S10. NOTE — the named retracted row is textually purged, but T2 retains an unproved regularity target

**Locations.** `theory/spt-scoping-draft.md:3-15`, `:143-165`, `:281-299`,
test T2 `:407-420`, verdict `:493-501`.

Every literal occurrence of `G0-soft-r1` is a withdrawal or warning, and the
draft no longer calls `(e^{ik}-1)` an Adler zero.  However T2 still demands that
`F(k)/(e^{ik}-1)` be bounded and smooth.  That is a new regularity hypothesis of
the ML3 type, not a consequence of G0.  It may be tested, but must not be cited
as already proved.

**Fix demand.** Label boundedness/smoothness in T2 as the additional hypothesis
being tested, not as an exact consequence of the kinematic factor.

**SPT section verdict: FAIL(S1, S2, S3, S4, S5, S6, S7, S8).**

---

## Whole-verdict disposition

The three previously converged packages remain untouched: Corner A, the Bethe
oracle, and ML2 still pass.  The exact Mq-flux identity also survives this
attack as a mathematical statement, as does the conditional conserved-charge
bookkeeping `2s delta x + q_out-q_in=0` and the projected Fano computation as a
computation.  What does not survive is the frozen certification of the later
summit shards, B3(ii), the virtual-bond reading of physical memory flux, or the
SPT paired/unpaired dichotomy in its claimed `[omega]`-blind form.

**OVERALL: FAIL(T1, T2, T3, T4, T5, T6, T7, T8, T9; B1, B2, B3, B4, B5, B6,
B7, B8, B9; S1, S2, S3, S4, S5, S6, S7, S8).**
