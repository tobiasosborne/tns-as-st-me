<!-- ROLE: L6 critic verdict, round 3 focused adjudication of the corpus-r2
     repairs. Critic: Codex. Date: 2026-08-26. -->

# Critic verdict r3 — focused adjudication of the r2 repairs

Critic: Codex, adversarial review of commit `32335d0` against
`verdicts/corpus-r2.md`.  I restricted fresh attack to the repair delta and to
statements whose status changed in that delta.  I independently re-derived the
five requested mathematical repairs, compared all fifteen promotions with the
exact r2 promotion table, checked shard/DAG/TRIANGLE lockstep, reviewed D25 and
the changed SPT checker, ran all eight checkers under `python3 -O`, and ran all
documented red modes.  A prior file-mutation red test was repeated on a copy
under `/tmp`; no source file was mutated.

The fixed-tensor N1 repair is mathematically correct: `Q^H=-iQ` is Hermitian,
the endpoint generator must be centered, and the new gauge red mode really
rejects the uncentered convention.  N2, N4--N9 are also repaired.  N3 is not
fully repaired because the notation registry still defines the fixed-ring
`Gamma_N(k)` as on-shell.  More importantly, the repaired SPT-E' adds a false
deformation-rigidity claim for the *centered* charge offset.  Gauge invariance
of that offset does not make it constant along an MPS path: the Schmidt weights
in `r` can vary continuously.  The promotion sweep also attaches PROVED to a
forbidden B3 moment-map/torsor interpretation, contradicts the M-tk promotion
inside its own shard, and enlarges the exact-AKLT split by adding a comparator
that r2 did not promote.

---

## Independent re-derivations

### 1. N1: Hermiticity, centering, lift gauge, and the red test

D10 has `q_x(xi)^dagger=-q_x(xi)`, hence
`Q[f;xi]^dagger=-Q[f;xi]` for real `f`.  Therefore

`Q^H[f;xi]:=-iQ[f;xi]`

is Hermitian, as is its completely positive boundary compression.  Since
`X_C(xi)^dagger=-X_C(xi)` and `r=r^dagger`,
`tr(rX_C)` is purely imaginary.  Thus

`X_C^circ=X_C-tr(rX_C)I`,  `Q_edge=-iX_C^circ`

are respectively anti-Hermitian and Hermitian, with
`tr(rX_C^circ)=0`.  Differentiating the normal-ordered intertwiner and summing
the transfer coboundary leaves this centered generator.  The declared
dual-left orientation fixes the sign to `-iX_C^circ`; the exact AKLT
contraction below independently fixes the same sign.

Under `V(exp(epsilon xi))->exp(ia epsilon)V(exp(epsilon xi))`,

`X_C -> X_C+iaI`, `tr(rX_C)->tr(rX_C)+ia`,

so `X_C^circ` and `Q_edge` are unchanged.  The raw offset `q_omega` and
`bar q_C=-i tr(rX_C)` both shift by `a`, so
`q_{omega,C}^circ=q_omega-bar q_C mod Z` is also lift-gauge invariant.  The
spectral inclusion at a fixed tensor follows: raw weights are in
`q_omega+Z`, and centering subtracts `bar q_C` from all of them.

The new checker mode uses `X=-iZ/2`, replaces it by
`X'=X+0.37iI`, and compares the measured `-Z/2` with either
`-i(X'-tr(rX')I)=-Z/2` or the uncentered `-iX'=-Z/2+0.37I`.
The latter has norm error exactly `0.37` and exits `1`.  It therefore detects
the convention N1 required it to detect.  The checker-quality limitation in
R3-N4 below does not change this conclusion.

### 2. N2: coefficient continuity

At fixed `N,L`, the contraction is polynomial in `A(t)`, its conjugate, all
external tensors, embeddings, gauge-fixed representatives, and profiles.
The repair now assumes all of those data continuous in `t` (and `C^p` when an
order-`p` coefficient is asserted).  Uniform positivity of the Gram matrices
makes inverse square roots continuous by finite-dimensional functional
calculus.  On the compact path, continuity of `E_t` and the common spectral
separation give continuous Riesz projections and a uniform

`||E_t^m-P_t|| <= C_{tilde lambda} tilde lambda^m`.

Thus the thermodynamic limit is a uniform limit of continuous functions.
H-soft-p supplies the corresponding uniform derivative limit for soft
coefficients.  These are the missing hypotheses from r2 and they suffice for
the proof as written.

### 3. N3: off-shell relabel

The shard, DAG, and TRIANGLE now correctly say that continuous `k` in
(12)--(17) at fixed periodic `N` is an off-shell analytic interpolation.  A
fixed ring has no nonzero sequence of allowed momenta tending to zero, while
the physical sequence `k_N=2pi/N` is the already-recorded nonuniform one.
However, `notation.md` line 241 still calls `Gamma_N(k)` an “outgoing on-shell
channel map.”  Because the notation registry is an active consumer and points
precisely to (3),(12), the relabel is not honest everywhere.

### 4. N4 and N5: module multiplicity and Whitehead

Padded-window injectivity gives

`mathcal M_chi(C) ~= M_chi(C) ~= E_C tensor E_C^*`.

Under left multiplication, `V(g)` acts as `V(g) tensor I`.  Since the spectator
factor has dimension `chi`, the padded module is exactly `chi` copies of the
Schmidt/edge module `E_C`; it is not equivalent to one copy.  D19--D21 and the
SPT shard now state this correctly, and H-split is formulated only for `E_C`.

For the Lie algebra, a section change `X'(xi)=X(xi)+i ell(xi)I` changes the
displayed central term by the coboundary proportional to `ell([xi,zeta])`.
Whitehead's second lemma says its cohomology class vanishes for semisimple
`g`; it does not say the term vanishes in every section.  D4 and SPT-D' now say
exactly that it can be gauged away and display the ordinary bracket only in
that chosen section.  This is correct.

### 5. The two r2-promotable splits

For a closed string,

`(V(h) tensor bar V(h))(V(g) tensor bar V(g))`
`=omega(h,g)bar omega(h,g)V(hg) tensor bar V(hg)`
`=V(hg) tensor bar V(hg)`.

This proves only multiplier and lift-rephasing cancellation.  The current
SPT-B-mult statement preserves that boundary and does not claim that
`Ad(V)` is class-blind.

For the AKLT family, with `lambda=2b^2-1`,

`E_{S^z}(r)=-(1-b^2)Z/2`, `E_b(Z)=lambda Z`.

The register normalization is multiplication by `2`, hence

`2 sum_{n=0}^{L-1} E_b^n(E_{S^z}(r))`
`=-(1-b^2)(1-lambda^L)/(1-lambda) Z`
`=-1/2[1-(2b^2-1)^L]Z`.

The formula and its `-Z/2` limit are exact.  The promoted row is nevertheless
not the *exact narrow split* authorized in r2 because it additionally promotes
the trivial `O(2)` product residue; see R3-N3.

### 6. New counterexample to deformation rigidity of the centered offset

Gauge invariance is not path rigidity.  An explicit symmetric injective path
already exists for `G=U(1)`.  Put

`V(phi)=diag(1,e^{iphi})`,
`A^{ij}=sqrt(W_{ij}) E_{ij}`,
`W(a,b)=[[1-a,b],[a,1-b]]`, with `0<a,b<1`,

and let the four physical basis vectors carry charges `j-i`.  Then
`u(phi)A=V(phi)^{-1}AV(phi)`, the four matrices span `M_2`, and the tensor is
left canonical because the columns of `W` sum to one.  Its transfer spectrum is
`{1,1-a-b,0,0}` and

`r=diag(b/(a+b),a/(a+b))`.

Along, for example, `(a,b)=(0.2,0.4)->(0.3,0.4)`, there is a common transfer
gap and the projective class and virtual representation are fixed.  With
`X=i diag(0,1)` and `q_omega=0`, however,

`bar q_C=a/(a+b)`, `q_{omega,C}^circ=-a/(a+b) mod Z`,

which changes from `2/3` to `4/7` modulo integers.  Equivalently, the centered
charge spectra change from `{-1/3,2/3}` to `{-3/7,4/7}`.  This is consistent
with D21's own caveat that `U(1)` alone does not protect the offset.  It refutes
SPT-E'(iii)'s general statement that the centered offset is constant under the
stated symmetric gapped deformation.

---

## Objection-by-objection adjudication

| r2 id | result | independent adjudication |
|---|---|---|
| **N1** | **RESOLVED** | `Q^H=-iQ` is Hermitian; `X_C^circ` is anti-Hermitian and centered; `Q_edge=-iX_C^circ` is Hermitian and lift-gauge invariant.  The dual-left sign agrees with the exact AKLT contraction, and `--red-gauge` detects the uncentered `0.37I` shift. |
| **N2** | **RESOLVED** | The newly continuous/`C^p` external tensors, embeddings, gauge fixes, Gram normalizations, and profiles close the finite-contraction step; the common gap and H-soft-p close the two uniform-limit steps. |
| **N3** | **UNRESOLVED** | The shard/DAG/TRIANGLE relabel is correct, but `notation.md:241` still defines the fixed-ring `Gamma_N(k)` as on-shell.  The false label therefore remains in an active consumer. |
| **N4** | **RESOLVED** | `M_chi(C) ~= E_C tensor E_C^*`, and left multiplication is `V tensor I`, hence exactly `chi` copies.  H-split is confined to `E_C`. |
| **N5** | **RESOLVED** | The repaired text says “cohomologically trivial and can be gauged away,” and states the zero-cocycle bracket only after choosing that phase section. |
| **N6** | **RESOLVED** | Every active SPT row has one L5 status; H-split/H-dress are present on all physical SPT-D'/T' surfaces; D23 fixes the dynamical Hamiltonian and identifies `P^(S=2)_{0,1}` as its first boundary bond. |
| **N7** | **RESOLVED** | TRIANGLE section 6.2 now says exactly that universality of the zero and coefficient remains CONJECTURE and keeps C=>B at SKETCH. |
| **N8** | **RESOLVED** | Overload 8 distinguishes bare transfer `E_b` from energy `E_b(K)`; overload 11 gives the D7/ML2-local separation exception for `r`. |
| **N9** | **RESOLVED** | B3 now approximates both evolved factors and gives the correct two-factor norm estimate before applying D9(a) and sending the approximation error to zero. |
| **N10** | **RESOLVED as a scope note** | The new gauge mode covers the previously untested uncentered convention, while the text still says that no checker proves H-split, H-AD-edge, Mq-E, full-chain leakage control, or an infinite-volume on-shell ML4 theorem. |

---

## Promotion fidelity and lockstep

“Faithful” below means no conclusion stronger than the exact r2 promotion and
the same status/scope in the proof shard, `claims/CLAIMS.md`, and
`theory/TRIANGLE.md`.

| promoted row/item | fidelity | comparison with the r2-adjudicated statement |
|---|---|---|
| **S2-2body** | **FAITHFUL** | Exact two-body multiplier/phase expansion with compact-hard cubic remainder only; S-general and process independence remain unpromoted. |
| **ML4-A** | **FAITHFUL** | Only the abstract matching-plus-`C^1` cancellation lemma is PROVED. |
| **ML4-Ward** | **FAITHFUL** | The split is exactly finite-sector projection (8)--(11), including the polar/general-sector and one-hard packet consequences. |
| **ML5-A** | **FAITHFUL** | The two necessary-and-sufficient conditions, `K_O` bound, and separate relative bound are preserved. |
| **ML5-B** | **FAITHFUL** | PROVED only as the five-hypothesis conditional implication; nonemptiness and microscopic membership remain open. |
| **M-flux** | **FAITHFUL** | Exact finite-time physical-boundary-current identity only; no virtual-potential reading. |
| **K1** | **FAITHFUL** | Positive `2x2` block, spectrum, and kernel only. |
| **K2** | **FAITHFUL** | Bondwise annihilation of the displayed product family only. |
| **K3** | **FAITHFUL** | Telescoping invisibility to the quasi-local derivation only. |
| **B3** | **NOT FAITHFUL** | The DAG and TRIANGLE are narrow, but `corner-b-draft.md:53-57` puts a “moment map of the residual translation torsor” interpretation inside the PROVED B3 summary.  R2 expressly withheld torsor reconstruction, and the shard itself contradicts this at lines 689--690. |
| **Mq-AD3** | **FAITHFUL** | PROVED only conditional on the full all-volume/unitary Mq-E assumption; full-chain D18 remains open. |
| **M-quant** | **FAITHFUL** | Spin-`1/2` theorem conditional on D18, with only the abstract charge arithmetic stated generally. |
| **M-tk** | **NOT LOCKSTEP** | DAG/TRIANGLE and the shard at line 691 promote the Fano formula and quadratic zero conditional on Mq-E, but the same shard lines 694--698 calls the calculation SKETCH and says the zero is not promoted. |
| **SPT-B-mult** | **FAITHFUL** | Exactly closed-register multiplier/rephasing cancellation; no `Ad(V)` blindness is added. |
| **SPT-E-AKLT** | **NOT FAITHFUL** | The authorized split was the exact AKLT-family contraction.  The PROVED DAG/TRIANGLE rows also include the trivial `O(2)` product residue `0`, an additional conclusion not in the r2 split. |

Thus twelve promotions are faithfully applied.  Three need a textual/status
repair before the ledger is lockstep.

---

## D25 adjudication

| check | result |
|---|---|
| Object and factorization | **EXACT** — D25 defines the same `mathsf S(k_s;{q_i,v_i})` in `M_{n+1}=mathsf S M_n+R_{S2}` used by S-general and TRIANGLE section 2.4. |
| Arguments | **EXACT** — asymptotic charges/velocities plus the same kink vacuum-pair and collective-coordinate data. |
| Universality class | **EXACT** — independence only within D24(d)'s `mathcal S_W`; unrestricted universality remains REFUTED. |
| Soft behavior and remainder | **EXACT** — `mathsf S->0`, conjecturally linear, and `R_{S2}=o(mathsf S)` in the D24(b) packet norm, exactly as TRIANGLE section 2.4. |
| Status | **NO STRENGTHENING** — D25 explicitly says existence, factorization, and universality remain S-general (CONJECTURE), and distinguishes all SPT/Bethe glyphs. |

D25 therefore closes the Corner-C glyph's L4 naming gap without changing a
claim status or theorem quantifier.

---

## Checker and red-mutation audit

All eight scripts passed under optimization:

| optimized green run | result |
|---|---|
| `corner_a_check.py` | exit `0` |
| `crosscheck_corner_b_tk.py` | exit `0` |
| `ml2_completeness_check.py` | exit `0` |
| `ml4_check.py` | exit `0` |
| `mquant_check.py` | exit `0` |
| `oracle_bethe_check.py` | exit `0` |
| `soft_current_recon_check.py` | exit `0` |
| `spt_rebuild_check.py` | exit `0` |

Every current documented red mode was killed under `python3 -O`:

| red test | result |
|---|---|
| `mquant_check.py --red` | exit `1`, continuity residue `2.340e+00` |
| `ml4_check.py --red-uniform` | exit `1`, the `k=2pi/N` false-uniform claim is detected |
| `spt_rebuild_check.py --red` | exit `1`, edge-sign error `1.333e+00` |
| `spt_rebuild_check.py --red-gauge` | exit `1`, uncentered error `3.700e-01` |

I also copied `spt_rebuild_check.py` to
`/tmp/tns-corpus-r3-checks.I5lMhg/manual-mutants/`, changed only the independent
bulk formula denominator `4->8`, and ran the copy under `-O`.  It exited `1`
with measured `0.125000023426` versus mutant `0.0625`.  `git diff --check`
passes on the repair delta, and no checker contains a bare Python `assert`.

The off-shell logic is correctly tested as a negative uniformity result, but
the active notation row remains inconsistent as recorded under N3.  The gauge
red mode is genuinely red-capable for the uncentered convention.

---

## New objections

### R3-N1. MAJOR — gauge invariance is incorrectly promoted to deformation rigidity

**Location:** `theory/spt-rebuild.md:527-528,585-608`, especially
`594-599`; consumed by the SPT-E' theorem.  Compare `definitions.md:822-843`,
whose last sentence already says `U(1)` alone does not protect the offset.

**Independent computation.**  The explicit `U(1)`-covariant injective path in
section 6 above has fixed `V`, fixed cocycle, fixed physical representation,
and a common transfer gap, but varying right fixed point.  Consequently
`q_{omega,C}^circ` changes from `2/3` to `4/7`.  The inference at lines
594--599 uses only that `[omega]` is constant and the centered combination is
gauge invariant; neither condition fixes `tr(rX_C)` along the path.

**Fix demand:** delete deformation constancy of the centered offset, or add a
hypothesis that fixes `tr(rX_C)` (for example an irreducible/weight-balanced
endpoint register); retain only fixed-tensor spectral congruence and gauge
invariance in general.

### R3-N2. MAJOR — B3 and M-tk promotions are not lockstep inside the Corner-B shard

**Location:** `theory/corner-b-draft.md:53-57,566-572,689-698`; compare
`claims/CLAIMS.md:44,66` and `theory/TRIANGLE.md:476-500,525,528`.

**Independent audit.**  R2 promoted B3 only as finite-time label rigidity plus
`2s delta x+(q_out-q_in)=0` and explicitly denied torsor reconstruction.  The
new PROVED summary nevertheless calls `delta x` the moment map of a residual
translation torsor.  Conversely, r2 promoted the displayed-graph Fano formula
*and quadratic zero* conditional on Mq-E, but lines 694--698 classify them
under SKETCH and say the zero was not promoted.  Both contradictions occur in
the same shard that elsewhere states the correct scopes.

**Fix demand:** remove the moment-map/torsor sentence from the PROVED B3
summary, and change the section-10 M-tk bullet to PROVED conditional on Mq-E
for the displayed graph while leaving only full-chain accuracy/universality at
SKETCH/CONJECTURE.

### R3-N3. MAJOR — the exact-AKLT promoted split contains an unadjudicated extra conclusion

**Location:** `claims/CLAIMS.md:49`, `theory/TRIANGLE.md:423,533`, and
`theory/spt-rebuild.md:624-629`.

**Independent audit.**  Corpus r2 authorized a split for “the exact AKLT
formula.”  The resulting PROVED SPT-E-AKLT row also asserts that the trivial
`O(2)` product residue is `0`.  That assertion is elementary and the checker
confirms it, but it was not part of the narrow promotion adjudicated in r2;
adding a true statement is still a silent strengthening of the promoted row.

**Fix demand:** restrict SPT-E-AKLT to equation (4.1) and its AKLT-family limit;
leave the product comparator as checked supporting text unless separately
adjudicated.

### R3-N4. MINOR — S-C6's Hermiticity subtest is tautological

**Location:** `theory/checks/spt_rebuild_check.py:319-339`.

**Independent audit.**  The checker first computes the Hermitian `measured`
operator from `S^z`, then defines `antihermitian_partial=1j*measured`.  The two
subsequent type checks therefore hold by construction and do not exercise a
D10 anti-Hermitian insertion.  The separate centered/uncentered gauge branch
at lines 341--365 is effective and does fail by `0.37`.

**Fix demand:** construct the partial charge independently using the
anti-Hermitian one-site generator `-iS^z` through `inserted_transfer`, then
compare its compression with `i*measured` and `-iQ` with `measured`.

---

## Promotion decisions for the repaired SPT parents

| row | decision | repaired promotable statement or exact missing step |
|---|---|---|
| **SPT-B'** | **PROMOTE to PROVED** | Under the common-gap path and the newly continuous/`C^p` external data, normalized finite/thermodynamic/soft coefficients are continuous (with H-soft-p for derivative limits) and become topological only after a separate local-constancy proof.  This is distinct from the already-PROVED multiplier split. |
| **SPT-E'** | **HOLD** | Clauses (i), (ii), the fixed-tensor spectral inclusion in (iii), and the AKLT computation are correct.  The exact missing repair is to retract or properly hypothesize constancy of `q_{omega,C}^circ` under deformation (R3-N1). |
| **SPT-T'** | **PROMOTE to PROVED** | In the registered endpoint, (5.1) follows by eliminating `V(hg)` and (5.2) follows for commuting `g,h`; the second endpoint compensates.  A physical observable remains conditional on H-split and H-dress. |
| **SPT-D'** | **PROMOTE to PROVED** | Ordered registered endpoint products realize the cocycle; for compact semisimple Lie algebra the infinitesimal cocycle is a coboundary and is removed only in the stated phase section.  Physical edge use remains conditional on H-split/H-dress. |
| **SPT-M'** | **PROMOTE to PROVED as a conditional implication** | Given H-split, H-AD-edge, charge conservation, and definite channel charges, `Delta Q_edge=-(Q_bulk,out-Q_bulk,in)` and fixed-system channel differences are integral.  This uses only the valid fixed-tensor congruence, not the false deformation constancy in R3-N1.  Protection is capacity/module protection, not nonzero amplitude. |
| **SPT-M'-dyn** | **CONJECTURE (unchanged)** | The specific open AKLT Hamiltonian is now named, but half-chain wave operators, H-AD-edge, the on-shell reflection matrix, and nonvanishing on an open interval remain missing. |

---

## Final disposition

N1's centered Hermitian endpoint charge, N2's external-data continuity, the
module multiplicity, Whitehead repair, physical-hypothesis lockstep, B3 density
leaf, D25, and the new gauge red mode all survive.  The package still fails
because one active consumer retains the false fixed-ring on-shell label, the
centered offset is incorrectly claimed deformation-rigid, and three promotion
surfaces are not faithful to the r2 ledger.

FAIL(N3, R3-N1, R3-N2, R3-N3)
