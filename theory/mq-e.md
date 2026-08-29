# Mq-E — all-volume `≤3`-wall Fano reduction

**Status: PROVED** (critic theory/verdicts/blitz-mq-e-r1.md, 0F/0M).  The theorem concerns the compressed operator
`H_3=P_3H_{\rm XXZ}P_3` of `memory-quantization.md` §3, not the unprojected
XXZ Hamiltonian.  In particular, it does not remove the separate
`P_3H_{\rm XXZ}(1-P_3)≠0` full-chain leakage problem.

## 0. Statement

**ASSUME.**  The spin-`1/2` D16 Hamiltonian with `J>0`, `Δ>1`, the kink
orientation `↑` at left and `↓` at right, and a fixed integer regularised
charge label `μ`.  For a finite frozen-boundary interval
`Λ_{A,B}={A,…,B}`, assume `A≤μ-1` and `B≥μ+2`; compress the open-chain D16
Hamiltonian to product configurations with endpoint spins `(↑,↓)`, exactly
`B-μ` down spins, and one or three domain walls.  Let `C_{A,B}` be the
connected component containing the three consecutive walls
`(μ-1,μ,μ+1)`.  Let `C_∞` be the corresponding component on `ℤ` in the
finite-deviation core of `𝒦_{↑↓}`.

**PROVE.**

1. For every such finite interval,
   `C_{A,B}` consists of a truncated two-sided path and one side vertex.
2. The basis map displayed in §3 is a unitary `U_{A,B}` (and, at infinite
   volume, `U_∞`) intertwining the compressed D16 Hamiltonian with the Fano
   Jacobi operator (Mq.7).
3. The negative tail is the incoming/reflected D14 leg with charge `-1` and
   kink bond `μ+1`; the positive tail is the transmitted D14 leg with charge
   `+1` and kink bond `μ-1`; the side vertex is the sharp kink at bond `μ`.
4. Every fixed-window observable has two exact channel-tail constants plus a
   finite-support graph remainder.  After channel-kink subtraction the graph
   observable is finite-support, which is the local-observable input needed
   by D18(AD3).

The finite maps are restrictions of the infinite map along every cofinal
sequence `A→-∞`, `B→+∞`.

## 1. Quantified product-basis enumeration

For a product configuration `σ`, write its ordered wall bonds as
`w(σ)=(w_1,…,w_r)`, where bond `j` joins sites `j,j+1`.  This is only a
proof-local coordinate for the D16 `S^z` product basis.

**⟨1⟩1. PROVE.**  In the stated finite charge sector the unique one-wall
configuration has its wall at bond `μ`.

**⟨2⟩1.**  A one-wall word with wall `p` is up through site `p` and down from
site `p+1` through `B`, hence has `B-p` down spins.

*Justification.*  The two D16 product vacua and the fixed `(↑,↓)` boundary
orientation.

**⟨2⟩2.**  Equating `B-p=B-μ` gives `p=μ`; denote this word by `K_μ`.

*Justification.*  ⟨2⟩1 and the D16 conserved `S^z` sector.

**⟨2⟩3. QED.**

**⟨1⟩2. PROVE.**  Every three-wall configuration in the sector is uniquely
of the form

`w(σ)=(a,a+ℓ,μ+ℓ)`, with `A≤a≤μ-1` and
`1≤ℓ≤B-1-μ`.

**⟨2⟩1.**  For walls `a<b<c`, the down spins occupy the finite block
`a+1,…,b` and the right tail `c+1,…,B`, so their number is
`(b-a)+(B-c)`.

*Justification.*  Alternation from the D16 left vacuum `↑` to the right
vacuum `↓` across three ordered walls.

**⟨2⟩2.**  The fixed-charge equation is therefore
`a-b+c=μ`.  Setting `ℓ=b-a≥1` gives `c=μ+ℓ`.

*Justification.*  ⟨2⟩1 and the D16 fixed-`S^z` sector value `B-μ`.

**⟨2⟩3.**  The strict inequalities and finite-volume bounds are equivalent
to `A≤a≤μ-1` and `1≤ℓ≤B-1-μ`; conversely every pair in this rectangle gives
one admissible word.

*Justification.*  ⟨2⟩2 and the D16 product-basis ordering of wall bonds.

**⟨2⟩4. QED.**

**⟨1⟩3.**  Thus the entire fixed-charge `≤3`-wall space consists of `K_μ`
and the rectangle in ⟨1⟩2; no configuration has been omitted.

*Justification.*  ⟨1⟩1--⟨1⟩2 and the definition of `P_3` cited in claim
Mq-AD3.

**⟨1⟩4. QED.**

## 2. Infinite-volume corollary (using the finite construction in §§4--5)

Sections 2--3 state the two consequences needed by Mq-E.  Their cited
finite-volume component and unitary premises are proved explicitly in
§§4--5 below.

Let `A→-∞` and `B→+∞` through any cofinal sequence with `μ` fixed.  The
proof-local words `L_n,R_n,K_μ` are finite deviations of a sharp D16 kink,
so each fixed word occurs unchanged in every sufficiently large interval.

**⟨1⟩1. PROVE.**  The finite maps (E.1) are compatible on overlaps and define
a unitary

`U_∞:C_∞→ℓ²(ℤ)⊕ℂ|d⟩`

by the same displayed formulas.

**⟨2⟩1.**  For fixed `n`, the wall triples defining `L_n` or `R_n` and the
wall defining `K_μ` are independent of `A,B` once they lie inside the
interval.

*Justification.*  The explicit wall formulas in §5 and the D16 product-basis
embedding of frozen-boundary chains.

**⟨2⟩2.**  Their union over the cofinal sequence is precisely the infinite
row, infinite column, and side state found by the volume-independent toggle
argument of §4.

*Justification.*  §1 ⟨1⟩2, §4 ⟨1⟩1--⟨1⟩5, and D16.

**⟨2⟩3.**  The basis map is therefore isometric with dense range and extends
to the asserted unitary.

*Justification.*  D16 product-basis orthogonality and ⟨2⟩1--⟨2⟩2.

**⟨2⟩4. QED.**

**⟨1⟩2. PROVE.**  `U_∞H_3U_∞^*` is exactly (Mq.7).

**⟨2⟩1.**  On every finitely supported vector, (E.2)--(E.3) stabilise once
both finite endpoints lie beyond its one-step graph neighbourhood.

*Justification.*  §5 ⟨1⟩2, compatibility from ⟨1⟩1, and D16.

**⟨2⟩2.**  The resulting graph operator is bounded: it has bounded diagonal
and at most three off-diagonal entries of modulus `J/2` in every row.

*Justification.*  The D16 coefficients in (E.2)--(E.3).

**⟨2⟩3.**  Equality on the dense finite-support core therefore extends to
the Hilbert-space closures.

*Justification.*  ⟨2⟩1--⟨2⟩2, the unitary of ⟨1⟩1, and D16.

**⟨2⟩4. QED.**

**⟨1⟩3.**  Consequently every cofinal finite-volume sequence has the same
strong limit, and `U_{A,B}` is literally the restriction of `U_∞` to the
corresponding truncated graph.

*Justification.*  ⟨1⟩1--⟨1⟩2 and D16.

**⟨1⟩4. QED.**

## 3. Left/right legs and charges

Set `m:=μ+1`, so the negative graph tail has a sharp background kink at the
incoming bond `m`.

**⟨1⟩1. PROVE.**  For `n≤0`, `L_n` is one down magnon at site `x=μ+n≤m-1`
on the `↑` vacuum, together with the kink at bond `m`.

**⟨2⟩1.**  The walls `(x-1,x,m)` enclose exactly the single down spin `x`
before the final `↑↓` wall at `m`.

*Justification.*  The §5 formula for `L_n` and the D16 vacua.

**⟨2⟩2.**  Its leg charge relative to the `↑` vacuum is `-1`, and as
`n→-∞` D14 assigns its separated number to the reflected/left leg.

*Justification.*  D14 and spin `1/2` in D16.

**⟨2⟩3. QED.**

**⟨1⟩2. PROVE.**  For `n≥0`, `R_n` is one up hole at site
`y=μ+n+1≥m` on the `↓` vacuum, together with the outgoing kink at bond
`μ-1=m-2`.

**⟨2⟩1.**  The walls `(μ-1,y-1,y)` enclose exactly the single up spin `y`
after the first `↑↓` wall at `μ-1`.

*Justification.*  The §5 formula for `R_n` and the D16 vacua.

**⟨2⟩2.**  Its leg charge relative to the `↓` vacuum is `+1`, and as
`n→+∞` D14 assigns its separated number to the transmitted/right leg.

*Justification.*  D14 and spin `1/2` in D16.

**⟨2⟩3. QED.**

**⟨1⟩3. PROVE.**  Both tails and the side state lie in the same regularised
charge sector.

**⟨2⟩1.**  Relative to a fixed cut `c`, the negative tail has total charge
`(μ+1-c)-1=μ-c`.

*Justification.*  D13(a)'s sharp-kink charge and the D14 charge `-1` from
⟨1⟩1.

**⟨2⟩2.**  The positive tail has total charge
`(μ-1-c)+1=μ-c`, while `K_μ` has charge `μ-c`.

*Justification.*  D13(a), D14, and ⟨1⟩2.

**⟨2⟩3.**  Thus transmission changes the kink bond by exactly `-2` while
changing the separated leg charge from `-1` to `+1`, and reflection stays on
the negative tail with no kink displacement.

*Justification.*  ⟨2⟩1--⟨2⟩2 and claim M-quant's charge bookkeeping.

**⟨2⟩4. QED.**

**⟨1⟩4.**  Under `U_∞`, negative-tail asymptotics are therefore the D14
incoming/reflected channel and positive-tail asymptotics are the D14
transmitted channel, with exactly the labels and charges required by Mq-E.

*Justification.*  ⟨1⟩1--⟨1⟩3 and D14.

**⟨1⟩5. QED.**

## 4. Connected-component enumeration

**⟨1⟩1. PROVE.**  If the D16 XY term exchanges the antiparallel spins at a
wall bond `r`, the new wall set is

`w(σ')=w(σ) △ {r-1,r+1}`,

with an attempted move through a frozen endpoint removed by the compression.

**⟨2⟩1.**  The exchange changes only the comparisons across bonds `r-1` and
`r+1`; the spins across bond `r` remain antiparallel.

*Justification.*  Direct action of the D16 term
`-(J/2)(S_r^+S_{r+1}^-+S_r^-S_{r+1}^+)` in its `S^z` product basis.

**⟨2⟩2.**  Each of those two neighbouring wall indicators is therefore
toggled, while every other indicator is unchanged.

*Justification.*  ⟨2⟩1 and D16.

**⟨2⟩3. QED.**

**⟨1⟩2. PROVE.**  A three-wall vertex `(a,b,c)` has a nonzero compressed
hopping edge exactly when `b=a+1` or `c=b+1`.

**⟨2⟩1.**  By ⟨1⟩1, exchanging at one of `a,b,c` retains at most three walls
only if at least one of its neighbouring bonds is already a wall; otherwise
two new walls are created and the result has five walls, which `P_3` removes.

*Justification.*  D16, ⟨1⟩1, and the `P_3` compression in claim Mq-AD3.

**⟨2⟩2.**  For three ordered walls, the neighbour condition is precisely
`b=a+1` or `c=b+1`.

*Justification.*  ⟨2⟩1, the ordered enumeration of §1, and D16.

**⟨2⟩3. QED.**

**⟨1⟩3. PROVE.**  In the rectangle `(a,ℓ)` of §1, the non-isolated
three-wall vertices are exactly its row `ℓ=1` and its column `a=μ-1`.

**⟨2⟩1.**  The condition `b=a+1` is `ℓ=1`.

*Justification.*  §1 ⟨1⟩2 and D16.

**⟨2⟩2.**  Because `c-b=(μ+ℓ)-(a+ℓ)=μ-a`, the condition `c=b+1` is
`a=μ-1`.

*Justification.*  §1 ⟨1⟩2 and D16.

**⟨2⟩3.**  Every rectangle vertex with `ℓ≥2` and `a≤μ-2` is therefore an
isolated eigenvector of the compressed operator and is not in the incoming
component.

*Justification.*  ⟨1⟩2 and ⟨2⟩1--⟨2⟩2; the independent finite-volume
falsifier is `check_mq_e.py`.

**⟨2⟩4. QED.**

**⟨1⟩4. PROVE.**  The row and column form one path and meet only at the
junction `(μ-1,μ,μ+1)`; `K_μ` is joined only to that junction.

**⟨2⟩1.**  Along `ℓ=1`, the permitted exchanges move `a` by one; along
`a=μ-1`, they move `ℓ` by one.  At their intersection both descriptions give
the three consecutive walls `(μ-1,μ,μ+1)`.

*Justification.*  D16 and the toggle identity ⟨1⟩1.

**⟨2⟩2.**  Exchanging the middle pair at the junction toggles the outer two
walls and leaves the single wall `μ`; conversely exchanging across the wall
of `K_μ` creates exactly the junction.

*Justification.*  D16, ⟨1⟩1, and §1 ⟨1⟩1.

**⟨2⟩3.**  No other edge from `K_μ` or from the row/column survives the
`≤3`-wall and frozen-boundary compressions.

*Justification.*  ⟨1⟩1--⟨1⟩3.  Exhaustive checks over the recorded finite
range are supplied by `check_mq_e.py` and `CHECK_OUTPUT.md`.

**⟨2⟩4. QED.**

**⟨1⟩5.**  Hence `C_{A,B}` is exactly the row union column union `{K_μ}`;
the rest of the `O(|Λ|^2)` three-wall sector is a direct sum of isolated
vertices.

*Justification.*  §1 ⟨1⟩3, ⟨1⟩3--⟨1⟩4, and D16.

**⟨1⟩6. QED.**

## 5. Explicit finite-volume unitary and Hamiltonian

Put `I_{A,B}={A+1-μ,…,B-μ-2}`.  For `n≤0` and `n≥0`, respectively, let the
following symbols denote the already-enumerated product words:

`w(L_n)=(μ+n-1,μ+n,μ+1)`,

`w(R_n)=(μ-1,μ+n,μ+n+1)`.

The two formulas agree at `n=0`; call that common word `J_0`.  Define on the
orthonormal product basis of `C_{A,B}`

\[
 U_{A,B}L_n=|n\rangle\quad(n\le0),\qquad
 U_{A,B}R_n=|n\rangle\quad(n\ge0),\qquad
 U_{A,B}K_\mu=|d\rangle .                                      \tag{E.1}
\]

Only labels with `n∈I_{A,B}` occur.

**⟨1⟩1. PROVE.**  Equation (E.1) extends uniquely to a unitary
`C_{A,B}→ℓ²(I_{A,B})⊕ℂ|d⟩`.

**⟨2⟩1.**  The negative labels enumerate the row, the positive labels
enumerate the column, `n=0` is their unique intersection, and `d` is the
unique one-wall state.

*Justification.*  §4 ⟨1⟩3--⟨1⟩5 and D16.

**⟨2⟩2.**  Distinct D16 `S^z` product words are orthonormal, and the graph
vectors on the right of (E.1) are an orthonormal basis of the target.

*Justification.*  D16 and §4 ⟨1⟩5.

**⟨2⟩3. QED.**

**⟨1⟩2. PROVE.**  With missing neighbours at the ends of `I_{A,B}` omitted,

\[
 U_{A,B}H_3U_{A,B}^*|n\rangle
 ={3J\Delta\over2}|n\rangle-{J\over2}(|n-1\rangle+|n+1\rangle)
 -{J\over2}\mathbf1_{n=0}|d\rangle,                            \tag{E.2}
\]

\[
 U_{A,B}H_3U_{A,B}^*|d\rangle
 ={J\Delta\over2}|d\rangle-{J\over2}|0\rangle .              \tag{E.3}
\]

**⟨2⟩1.**  In D16, each antiparallel bond contributes diagonal energy
`JΔ/2`, so every path vertex has energy `3JΔ/2` and `K_μ` has energy
`JΔ/2`.

*Justification.*  Direct two-site matrix of the D16 bond term.

**⟨2⟩2.**  Every surviving exchange in §2 has matrix element `-J/2`, and
there are no other compressed edges.

*Justification.*  The D16 XY coefficient and §4 ⟨1⟩4--⟨1⟩5.

**⟨2⟩3.**  Applying the basis unitary (E.1) gives (E.2)--(E.3).

*Justification.*  ⟨1⟩1, ⟨2⟩1--⟨2⟩2, and D16.

**⟨2⟩4. QED.**

**⟨1⟩3.**  Equations (E.2)--(E.3) are the finite-interval compression of
(Mq.7): a uniform Jacobi path with on-site energy `E_c=3JΔ/2`, hopping
`-J/2`, and a side level `E_d=JΔ/2` coupled at `0` by `-J/2`.

*Justification.*  Claim Mq-AD3, equation (Mq.7), and ⟨1⟩2.

**⟨1⟩4. QED.**

## 6. Exact local-observable map

Fix a finite site window `W` and `O∈𝔄_W`.  Write `P_C` for the projection
onto `C_∞`.  Let `K_{μ+1}` and `K_{μ-1}` be the sharp D16 kink words on the
left and right channel backgrounds, and put

`o_L(O)=⟨K_{μ+1}|O|K_{μ+1}⟩`,
`o_R(O)=⟨K_{μ-1}|O|K_{μ-1}⟩`.

These are evaluations of the already-fixed D16 product vacua/kinks, not new
memory observables.

**⟨1⟩1. PROVE.**  There is a finite graph set `S_W⊂ℤ∪{d}` such that

\[
 U_\infty P_CO P_CU_\infty^*
 =o_L(O)\Pi^-_W+o_R(O)\Pi^+_W+F_W,                              \tag{E.4}
\]

where `Π^-_W` and `Π^+_W` project onto sufficiently remote negative and
positive tails, respectively, and `F_W=P_{S_W}F_WP_{S_W}`.

**⟨2⟩1.**  For all sufficiently negative `n`, the moving down spin of `L_n`
lies outside `W`, and the restriction of `L_n` to `W` equals that of
`K_{μ+1}`.  For all sufficiently positive `n`, the moving up spin of `R_n`
lies outside `W`, and its restriction equals that of `K_{μ-1}`.

*Justification.*  The explicit leg coordinates in §3 and the D16 product
basis.

**⟨2⟩2.**  A `W`-local operator has zero matrix element between two product
words that differ at any site outside `W`.  Hence each sufficiently remote
tail row and column is diagonal, with diagonal value `o_L(O)` or `o_R(O)`.

*Justification.*  Local tensor-product action in the D16 product basis.

**⟨2⟩3.**  Only finitely many graph words have their moving spin in `W`; add
those labels, the junction neighbourhood, and `d` to `S_W`.  Subtracting the
two remote diagonal constants then leaves a matrix supported on `S_W`.

*Justification.*  ⟨2⟩1--⟨2⟩2; the exhaustive product-word locality falsifier
is `check_mq_e.py`, with recorded green/red result in `CHECK_OUTPUT.md`.

**⟨2⟩4. QED.**

**⟨1⟩2. PROVE.**  Equation (E.4) supplies the local-observable statement
needed for D18(AD3).

**⟨2⟩1.**  The two tail constants are precisely the local expectations of
the remaining left/right kink charge eigenstates; after subtracting the
appropriate channel constant, the graph observable is `F_W`, which has
finite support.

*Justification.*  D18(AD3) and ⟨1⟩1.

**⟨2⟩2.**  Jacobi local decay therefore removes the free leg and non-bound
dressing from every fixed window without discarding coherent reflected/
transmitted superpositions.

*Justification.*  Claim Mq-AD3 and the finite-support remainder in ⟨2⟩1.

**⟨2⟩3. QED.**

**⟨1⟩3. PROVE.**  For a window containing the three kink bonds and with the
separated leg outside it, D13(a)'s wall observable has tail values
`o_L(𝔛_W)=μ+1`, `o_R(𝔛_W)=μ-1`, and side value
`⟨K_μ|𝔛_W|K_μ⟩=μ`.

**⟨2⟩1.**  D13(a) equals the wall bond on every sharp kink with no other
content in the window.

*Justification.*  D13(a).

**⟨2⟩2.**  The channel kink bonds and side bond are those established in §3.

*Justification.*  §3 ⟨1⟩1--⟨1⟩3, D14, and D16.

**⟨2⟩3.**  Thus the local-observable map records exactly zero reflected
displacement and transmitted displacement `-2`.

*Justification.*  ⟨2⟩1--⟨2⟩2, D13(a), and D14.

**⟨2⟩4. QED.**

**⟨1⟩4.**  The literal statement “every fixed-window observable maps to a
finite-support graph observable” must be read with channel-kink subtraction:
without subtraction, the exact mapping is the two-constant formula (E.4).

*Justification.*  ⟨1⟩1--⟨1⟩3 and D18(AD3).

**⟨1⟩5. QED.**

## 7. Claim closure

**⟨1⟩1. PROVE.**  Mq-E holds with all data required in its claim row.

**⟨2⟩1.**  Enumeration/component, finite unitary, infinite compatibility,
labels/charges, and observables are proved in §§1--6, respectively.

*Justification.*  §§1--6 and D14--D16.  **⟨2⟩2. QED.**

**⟨1⟩2. PROVE.**  On the projected incoming component, M-tk is unconditional:
`t(k)=[1+iJ²/(4ω(k)v(k))]^{-1}` and
`T(k)=16(Δ-1)²k²+O(k⁴)`.

**⟨2⟩1.**  M-tk and Mq-AD3 prove these consequences conditional only on the
Mq-E premise, which ⟨1⟩1 discharges.

*Justification.*  D15--D16 and claims M-tk, Mq-AD3.  The claim scope leaves
the unprojected formula and universality open.  **⟨2⟩2. QED.**

**⟨1⟩3. QED.** □
