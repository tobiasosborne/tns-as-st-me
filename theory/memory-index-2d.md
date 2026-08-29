<!-- ROLE: Lane W3 proposer shard for the 2+1 wave, work order bd tns-2p1.
     Writable lane: this file and theory/checks/memory_index_2d_check.py only.
     Donor: theory/memory-index.md, claims M-INDEX-fin/M-INDEX-spec/LR1-GEN,
     and definitions.md D26--D27.  No 1-form-symmetry or topological-order
     statement is made.  This is exclusively an on-site 0-form charge lane.

     HONEST STATUS (2026-08-29):
       * finite-window coset and TPM-increment integrality: complete proof;
       * LR1/common-subsequence clause: PROVED by the existing LR1-GEN row,
         whose three-input proof is dimension-free;
       * ordered 2D limit law: complete only as the displayed conditional
         implication (LR2_2D and first-moment tightness are not derived);
       * Goldstone interpretation: exploration plus one exact finite-volume
         one-magnon computation, not a thermodynamic theorem.
     The capped review certified M-INDEX-2D-fin at PROVED strength and held
     M-INDEX-2D-spec at SKETCH.
     The missing unconditional LR2_2D/LR3_2D instance is an open input, not a
     no-go result; no negative-result review rounds were spent.  Rounds: 0.
-->

# M-INDEX-2D — the 0-form charge-history index on a two-dimensional lattice

## 0. Honest header

| item | outcome in this shard | what does not follow |
|---|---|---|
| `M-INDEX-fin` | **Transplants cleanly.**  Every disk or annulus window charge lies in one coset of `Z`; the two readouts of the same window have the same offset, so every TPM escaped-charge outcome is in `Z`.  The proof is given leaf by leaf in §2. | No gap, channel inventory, interface coordinate, asymptotic charge operator, or limit law is produced. |
| `LR1-GEN` | **Transplants cleanly and is already PROVED.**  `Z^2` is countable, its quasi-local algebra is separable, every local charge has finite spectrum, and the donor's diagonal extraction is unchanged (§3). | It proves a common Cesàro subsequence only.  It says nothing about the nondemolition defect or spatial tightness. |
| `M-INDEX-spec` | **Its charge-law core survives conditionally.**  Under the honest 2D clauses `(LR2_2D)` and `(LR3_2D)`, every ordered limit point is a probability on `Z` and its first moment is the mean escaped 0-form charge (§4). | The 1D formula `Q_W=2s(X_W-c)` and hence the universal wall-displacement formula do not transplant.  No unconditional Goldstone-phase instance of `(LR2_2D)--(LR3_2D)` is proved. |
| genuinely 2D Goldstone question | **Finite-window integer support survives exactly.**  What replaces kink transmission is radiation of conserved spin charge through a closed curve.  The checker gives an exact one-magnon-sector 2D ferromagnet probe (§6). | It does not prove a thermodynamic long-time law, antiferromagnetic spin-wave completeness, or first-moment tightness. |

This shard is about an ordinary **on-site compact `G` 0-form symmetry** and a
selected circle charge.  It contains no result about 1-form symmetry,
topological order, loop operators, anyons, or topological charge.

The authoritative donor definitions remain D26 and D27 in `definitions.md`.
The authoritative donor proofs are `theory/memory-index.md` ⟨1⟩1 and
⟨1⟩5--⟨1⟩7; the dimension-free common-subsequence proof is
`theory/lr-d16.md` ⟨1⟩3 and the live row `LR1-GEN` in
`claims/CLAIMS.md`.  The notation below adds a superscript `(2)` only to
avoid pretending that the proposed 2D definition is already live.

---

## 1. Protocol and definitions by pointer

### ⟨1⟩1. Lattice, symmetry, and selected charge

Let `Gamma=Z^2` (the same argument works on any countable locally finite 2D
lattice) with uniformly finite on-site Hilbert spaces and quasi-local algebra
`A`.  Let a compact group `G` act on site by site.  Choose one closed
one-parameter subgroup and a Hermitian on-site generator `q_x`.  The exact
input inherited from D26 is

`exp(2 pi i q_x)=c I`, with `c=exp(2 pi i kappa)` and `kappa in [0,1)`.     **(2D-INT)**

Equivalently, `spec q_x` is contained in `kappa+Z`.  For a genuine
period-`2 pi` linear representation one has `c=1`; the scalar form is kept
because it is exactly D26's convention.  Compactness of `G` alone is not
silently turned into a charge theorem: a circle subgroup and (2D-INT) must be
selected.  A finite or disconnected symmetry with no such generator is
outside this statement.

Let `alpha_t` be the strongly continuous infinite-volume dynamics generated,
for example, by a finite-range `G`-invariant interaction.  The finite theorem
below needs only that `alpha_t` is a `C*`-automorphism group.  A local current
interpretation additionally uses charge conservation and locality.

### ⟨1⟩2. Disk and annulus windows

For a lattice centre `z` and a fixed lattice metric, use

`B_R(z)={x in Gamma : d(x,z)<=R}`,

`A_{r,R}(z)={x in Gamma : r<d(x,z)<=R}`.                       **(2D-WIN)**

Both are finite.  A disk has one boundary component.  An annulus has an inner
and an outer component, each oriented outward from the annular region.  The
finite-window proof in §2 actually applies to every finite `W subset Gamma`;
disks and annuli are the physically declared protocol family.

For limits, a disk exhaustion `W_m=B_{R_m}(z)`, `R_m -> infinity`, exhausts
the plane.  An annular exhaustion `A_{r_0,R_m}(z)` with fixed `r_0` exhausts
the exterior of a fixed core, not all of `Z^2`; this distinction is retained
below.  Nothing is called an exhaustion unless the domain it exhausts is
stated.

### ⟨1⟩3. Honest background subtraction: SSB pair or symmetric vacuum

The measured operator is a finite sum plus a scalar counterterm:

`Qhat_W = sum_{x in W} q_x - b_W I`.                           **(2D-Q)**

There are two intended preparations.

1. **SSB pair.**  Choose zero-temperature infinite-volume vacua
   `omega_alpha,omega_beta`, a reference interface curve `C`, and the phase
   profile `gamma_C(x) in {alpha,beta}` on its two sides.  With
   `rho_gamma=omega_gamma(q_x)`, take
   `b_W=sum_{x in W}rho_{gamma_C(x)}`.  The actual state may contain an
   interface, a local defect, and Goldstone radiation.  The curve fixes only
   the normal-ordering convention; no sharp interface-position operator is
   assumed.
2. **Symmetric vacuum.**  For a translation-invariant symmetric vacuum
   `omega_0`, take `b_W=|W|rho_0`, `rho_0=omega_0(q_x)`.  There is then no
   wall coordinate.  The protocol measures charge emitted from or absorbed
   by the window.

The scalar `b_W` may be nonintegral and may change with `W`.  That is harmless
for the finite TPM theorem because the two measurements use the **same**
`W` and hence the same offset.  Unlike the donor's 1D MPS density lemma, this
shard derives no 2D density quantisation and needs none.

### ⟨1⟩4. Two-projective-measurement history law

Let `E_{W,t}` be the spectral resolution of
`Qhat_W(t)=alpha_t(Qhat_W)`.  At finite `t_-<t_+`, projectively measure
`Qhat_W` at both times.  The recorded escaped charge is positive when the
window charge decreases:

`nu := q_- - q_+ = -Delta Q_W`,

`p_{W;t_-,t_+}(nu)
  := sum_q ||E_{W,t_+}({q-nu}) E_{W,t_-}({q}) Psi||^2`.         **(2D-TPM)**

Absent spectral values contribute zero.  This is the donor convention in
`theory/memory-index.md` §0 and ⟨1⟩5, with an arbitrary 2D window in place
of `[a,b]`.  It is a sequential measurement law, not the spectral law of
the generally noncommuting operator `Qhat_W(t_-)-Qhat_W(t_+)`.

If the interaction is represented by local terms satisfying the termwise
conservation law

`[Phi(Z),sum_{x in Z}q_x]=0`,

then

`J_out(W,t):=-d Qhat_W(t)/dt`

is a sum of interaction-current terms crossing the oriented boundary.  For
an annulus it contains the outer and inner boundary currents with their
respective outward orientations.  The variable `nu` is the TPM two-readout
charge change.  Only its first moment is identified with the boundary-current
ledger of the initially dephased ensemble; it need not equal the unmeasured
mean charge change, and no trajectory-level full-counting-statistics identity
is asserted.  The exact difference is §4's dephasing defect.

---

## 2. Finite theorem: the 2D transplant of `M-INDEX-fin`

### ⟨1⟩5. THEOREM `M-INDEX-2D-fin`

**ASSUME.**  (2D-INT), a finite disk or annulus `W`, a real scalar `b_W`, a
unit vector `Psi` in any representation of `A`, and finite times
`t_-<t_+`.

**PROVE.**  With

`kappa_W := |W| kappa - b_W  (mod Z)`,                         **(2D.1)**

one has

`spec Qhat_W(t) subset kappa_W+Z` for every `t`;               **(2D.2)**

the law (2D-TPM) is a probability supported on `Z`.             **(2D.3)**

No commutativity between the two Heisenberg observables is assumed.

**⟨2⟩1 (one-site arithmetic).**  Choose `kappa` as in (2D-INT).  Every
`lambda in spec q_x` satisfies `lambda-kappa in Z`.

*Justification.*  This is verbatim the finite-dimensional spectral
calculation `IDX-FW.1` in the donor
`theory/memory-index.md` ⟨1⟩1.⟨2⟩1.  Dimension and window geometry do not
enter.

**⟨2⟩2 (finite 2D sum).**  The operators `{q_x:x in W}` commute because
they act on different sites, and

`Qhat_W=sum_{x in W}q_x-b_W I`.

Hence every spectral value is in `|W|kappa-b_W+Z`.

*Justification.*  Finite spectral addition, exactly the donor's
`IDX-FW.2` at ⟨1⟩1.⟨2⟩2--⟨2⟩3.  The donor's interval-dependent scalar
`s(a+b-1-2c_0)` is replaced by the declared scalar `-b_W`; no ordering of
the sites is used.

**⟨2⟩3 (same coset at every time).**  `alpha_t` preserves spectrum, so
(2D.2) holds with the same `kappa_W` at all times.

*Justification.*  The C*-automorphism argument `IDX-FW.3` in the donor
⟨1⟩1.⟨2⟩4, unchanged.

**⟨2⟩4 (TPM positivity).**  Every summand in (2D-TPM) is a squared norm,
so the law is nonnegative.

*Justification.*  Donor ⟨1⟩5.⟨2⟩1--⟨2⟩2 (`IDX-TPM.1--.2`).

**⟨2⟩5 (TPM normalisation).**  Summing first over the final outcomes and
then over the initial outcomes gives

`sum_{q_-,q_+} ||E_{W,t_+}({q_+})E_{W,t_-}({q_-})Psi||^2=||Psi||^2=1`.

*Justification.*  Sequential Parseval for the two spectral resolutions,
the same donor leaf ⟨1⟩5.⟨2⟩2.  The projections at different times need not
commute.

**⟨2⟩6 (offset cancellation).**  Every live branch has
`q_-,q_+ in kappa_W+Z`, because the observable and window are the same at the
two times.  Therefore `nu=q_- - q_+ in Z` before any time or spatial limit.

*Justification.*  ⟨2⟩2--⟨2⟩3 and donor
⟨1⟩5.⟨2⟩3.  This is not spectral arithmetic for a difference of
noncommuting operators.

**⟨2⟩7. QED.**

### ⟨1⟩6. Leaf-by-leaf transplant ledger

| donor leaf | 1D datum there | 2D replacement here | status |
|---|---|---|---|
| memory-index ⟨1⟩1.⟨2⟩1 | `spec S^z subset kappa+Z` | `spec q_x subset kappa+Z` | identical |
| ⟨1⟩1.⟨2⟩2 | interval expansion of `Qhat_{W,c_0}` | finite site sum (2D-Q) | scalar bookkeeping only |
| ⟨1⟩1.⟨2⟩3 | interval offset `kappa_{W,c_0}` | `kappa_W=|W|kappa-b_W` | identical arithmetic |
| ⟨1⟩1.⟨2⟩4 | automorphic spectrum invariance | same `alpha_t` argument | identical |
| ⟨1⟩5.⟨2⟩1 | fixed-window TPM law | (2D-TPM) | identical |
| ⟨1⟩5.⟨2⟩2 | positivity and Parseval normalisation | ⟨1⟩5.⟨2⟩4--⟨2⟩5 above | identical |
| ⟨1⟩5.⟨2⟩3 | same-window offset cancellation | ⟨1⟩5.⟨2⟩6 above | identical |

The only change is the finite-window poset: intervals containing a cut are
replaced by disks/annuli (or all finite subsets) in `Z^2`.  Every leaf sees
only one fixed finite set, its cardinality, or countability of the family.
No leaf sees spatial dimension, boundary length, a spectral gap, or a
scattering channel.

---

## 3. The common time subsequence: `LR1-GEN` is dimension-free

### ⟨1⟩7. COROLLARY `LR1-GEN-2D`

For every prescribed sequence `S_n -> infinity` there is a subsequence
`T_n=S_{n_j}` along which, simultaneously for every finite disk/annulus `W`,
the two Cesàro states converge weak-* on all of `A` and every double-Cesàro
TPM weight converges.  At each fixed `W` the limiting law is a probability
supported in the finite set

`spec Qhat_W-spec Qhat_W subset Z`.

**Proof, transplanted leaf by leaf from `theory/lr-d16.md` ⟨1⟩3.**

**⟨2⟩1 (separability).**  `Z^2` is countable.  Its finite subsets are a
countable union of countable sets, and each local algebra is finite
dimensional.  Rational local words form a countable norm-dense subset of
`A`.  Strong continuity of `alpha_t` is assumed.  This is the 2D version of
donor leaf ⟨1⟩3.⟨2⟩1 (`LRD-SEP`).

**⟨2⟩2 (Cesàro states).**  Continuity and
`|<Psi,alpha_t(A)Psi>|<=||A||` make the integrals well defined; positivity
and unitality hold pointwise and survive averaging.  The Cesàro state does
not actually depend on `W`.  This is donor leaf ⟨2⟩2 unchanged.

**⟨2⟩3 (two weak-* extractions).**  The state space of the separable unital
C*-algebra is weak-* compact and metrizable.  Sequential compactness first
extracts the positive-time state and then the negative-time state.  One
subsequence works for every local observable and hence every window.  This
is donor leaf ⟨2⟩3 (`LRD-COMPACT`) unchanged.

**⟨2⟩4 (finite TPM range).**  At fixed `W`, `Qhat_W` has finite spectrum.
The TPM integrand is a finite sum of jointly continuous functions, is in
`[0,1]`, and vanishes outside the fixed finite difference set
`spec Qhat_W-spec Qhat_W subset Z`.  This is donor leaf ⟨2⟩4 (`LRD-TPM`),
using §2 in place of the interval formula.

**⟨2⟩5 (one diagonal sequence).**  The set of pairs `(W,nu)` is countable
for the disk/annulus family (indeed for all finite subsets of `Z^2`).
Successive Bolzano--Weierstrass extractions and the Cantor diagonal sequence
make every TPM weight converge without losing the two state limits.  This is
donor leaf ⟨2⟩5 (`LRD-DIAG`) with only the window enumeration changed.

**⟨2⟩6 (no fixed-window mass loss).**  Each fixed-`W` law lives on one fixed
finite set, so its pointwise limit still has total mass one and integer
support.  This is donor leaf ⟨2⟩6 unchanged.

**⟨2⟩7 (input audit).**  Exactly the same three inputs are consumed:

1. separability of `A`;
2. strong continuity of `alpha_t`;
3. finite spectrum of each fixed local `Qhat_W`.

No gap, Lieb--Robinson velocity, ergodicity, scattering, completeness, or
property of `Psi` beyond normalisation occurs.  Thus the live `LR1-GEN` row
already proves this corollary: its statement says “a countable lattice,” not
“a chain.”  **QED.**

Clause 1 remains useful as the binder for the single subsequence on which the
next clauses are evaluated.  Calling it automatic does not permit deleting
that quantifier.

---

## 4. The honest 2D D27 analogue and limit-law audit

### ⟨1⟩8. Proposed definition `(LR_2D)`

Fix a unit vector `Psi`, a declared disk exhaustion
`W_m=B_{R_m}(z) up Z^2` (or an annular exhaustion of a separately declared
exterior domain), and the operators (2D-Q).  Infinite-volume dynamics is
formed first, fixed-window time limits second, and the spatial exhaustion
last.

1. **`(LR1_2D)` — common Cesàro subsequence.**  There is one
   `T_n -> infinity` such that for every fixed admissible `W`,

   `omega^+_{W,n}(A)=T_n^{-1} int_{T_n}^{2T_n}<Psi,alpha_t(A)Psi>dt`,

   `omega^-_{W,n}(A)=T_n^{-1} int_{-2T_n}^{-T_n}<Psi,alpha_t(A)Psi>dt`

   converge weak-* (indeed they may be read as states on all of `A`), and
   the double-Cesàro TPM weights

   `p_{W,n}(nu)=T_n^{-2} int_{T_n}^{2T_n}dt_+
                  int_{-2T_n}^{-T_n}dt_-
                  sum_q ||E_{W,t_+}({q-nu})E_{W,t_-}({q})Psi||^2`

   converge for every `nu`.  The sum is over `spec Qhat_W` and absent
   spectral values contribute zero.
   By §3 this clause is a theorem, but it retains the common-sequence binder.

2. **`(LR2_2D)` — first-moment nondemolition.**  With

   `D_{W,t_-}(A)=sum_q E_{W,t_-}({q}) A E_{W,t_-}({q})`,

   the double-Cesàro average of

   `<Psi,[D_{W,t_-}(Qhat_W(t_+))-Qhat_W(t_+)]Psi>`

   tends to zero for every fixed `W`, along the same sequence.  This is a
   scalar first-moment condition, not operator asymptotic commutativity.

3. **`(LR3_2D)` — first-moment tightness on the declared 2D exhaustion.**
   If `p_W` is the fixed-window time limit, require

   `lim_{M->infinity} sup_m sum_{|nu|>M}(1+|nu|)p_{W_m}(nu)=0`. **(2D-LR3)**

   Optionally require `p_{W_m}` to converge weakly to a probability.  As in
   D27, this optional clause buys uniqueness of the limiting law and its
   first moment; it is not needed to say that every limit point has integer
   support.

The natural memory observable supplied by this definition is the **charge
memory**

`M_Q(p):=sum_{nu in Z} nu p(nu)`,                              **(2D-MEM)**

defined per `(LR3_2D)` subsequence, or uniquely under the optional full-law
convergence.  There is no definition of a universal scalar displacement.

### ⟨1⟩9. THEOREM `M-INDEX-2D-spec` (conditional charge form)

**ASSUME.**  (2D-INT) and `(LR1_2D)--(LR3_2D)`.

**PROVE.**  Every ordered spatial limit point `p` is a probability supported
on `Z`, and along its subsequence

`M_Q(p)=lim_j [omega^-_{W_{m_j}}(Qhat_{W_{m_j}})
               -omega^+_{W_{m_j}}(Qhat_{W_{m_j}})]`.          **(2D.4)**

Under the optional convergence clause the law and the value are unique.

**⟨2⟩1 (finite-window TPM mean).**  For finite times,

`sum_nu nu p_{W;t_-,t_+}(nu)
 = <Qhat_W(t_-)>-<D_{W,t_-}(Qhat_W(t_+))>`.                    **(2D.5)**

*Justification.*  Expand the two measured values and use the final spectral
resolution.  This is exactly donor Lemma L-D,
`theory/memory-index.md` ⟨1⟩6 (`IDX-TPM.3--.4`); no geometry enters.

**⟨2⟩2 (remove the dephasing defect).**  Double-Cesàro average (2D.5) and
apply `(LR2_2D)` to obtain, at each fixed `W`,

`sum_nu nu p_W(nu)=omega^-_W(Qhat_W)-omega^+_W(Qhat_W)`.       **(2D.6)**

*Justification.*  Donor ⟨1⟩7.⟨2⟩1, verbatim.

**⟨2⟩3 (spatial compactness and first moments).**  `(2D-LR3)` prevents loss
of mass and loss of first moment.  Prokhorov extraction on the closed set
`Z` gives a further weakly convergent subsequence from every subsequence;
uniform integrability passes the first moment.  Every limit remains
supported on `Z` because every finite-window law already is.

*Justification.*  Donor ⟨1⟩7.⟨2⟩3, with `W_m subset Z^2` replacing padded
intervals.  The possibly drifting `kappa_{W_m}` was cancelled at each fixed
window in §2 before this limit.

**⟨2⟩4 (ledger).**  Taking the same subsequence in (2D.6) gives (2D.4).
Under optional full-law convergence it gives one value.  **QED.**

### ⟨1⟩10. What changes from D27

| D27 ingredient | 2D verdict | geometric issue |
|---|---|---|
| LR1 common subsequence | survives and is PROVED by `LR1-GEN` | none; countability replaces interval enumeration |
| LR2 scalar dephasing defect | survives verbatim as a hypothesis | it is still not implied by symmetry or by a Lieb--Robinson bound |
| LR3 first-moment tightness | survives verbatim on a declared exhaustion | proving the `sup_m` bound must control a growing closed boundary |
| optional weak convergence | survives verbatim | it still buys uniqueness only |
| integer support of every limit point | survives | offset cancellation occurs before the spatial limit |
| `delta x=-(2s)^{-1}E nu` | **does not survive generally** | a 2D interface has shape modes and swept area, not one canonical coordinate |
| H-AD-G two-kink-channel reduction | not transplanted | reflection/transmission of a point kink is a 1D channel picture |

If a separate model supplies an exact affine observable
`Qhat_W=chi X_W+constant` for a chosen collective interface coordinate, then
one may infer `Delta X=-(1/chi)M_Q`.  For a nearly straight wall, a normal
shift changes charge in proportion to the swept area, and a displacement
per unit interface length requires an additional thermodynamic
normalisation.  None of those geometric inputs follows from 0-form
superselection, so none is included in `M-INDEX-2D-spec`.

### ⟨1⟩11. Perimeter audit

For a finite-range interaction `H=sum_Z Phi(Z)`, choose a termwise
charge-conserving decomposition

`[Phi(Z),sum_{x in Z}q_x]=0`.

(For a compact symmetry, a symmetry-averaged local decomposition may be
chosen.)  Then every term wholly inside or wholly outside `W` cancels and

`d Qhat_W(t)/dt
 = i alpha_t(sum_{Z: Z meets W and W^c}[Phi(Z),sum_{x in W}q_x])`. **(2D.7)**

Only a finite-range collar of the boundary contributes.  On a disk of radius
`R`, the number of such terms is `O(|partial W|)=O(R)`, rather than the `O(1)`
two-endpoint boundary of an interval.  On `A_{r,R}` it is `O(r+R)` because
both boundary components contribute.  With `q_*=sup_x||q_x||`,

`||d Qhat_W(t)/dt||`
` <= 2q_* sum_(Z: Z meets W and W^c) |Z cap W| ||Phi(Z)||`
` <= C_(Phi,q,r)|partial_r W|`.                            **(2D.8)**

The last inequality uses bounded degree and a uniformly bounded finite-range
interaction.  Thus the norm estimate is perimeter-sized.  A Lieb--Robinson estimate localises
the terms but does not by itself cancel that perimeter factor or prove
`(LR2_2D)`/`(LR3_2D)`.

The total, unnormalised TPM charge retains exact integer support.  Dividing it
by `|partial W|` would give support in
`|partial W|^{-1}Z`, a different density law; it must not be advertised as
the integer-valued memory index.  Useful sufficient inputs for the
unnormalised limit could include a fixed finite-charge sector, a uniform
bound on radiated selected charge, or quantitative local decay strong enough
to beat the boundary growth.  None is derived here.

---

## 5. Goldstone-memory audit

### ⟨1⟩12. What superselection still says

At every finite disk or annulus, **yes**: the escaped-charge TPM law has
integer support in a 2D SSB phase with gapless Goldstone modes.  The proof is
§2 and uses neither a spectral gap nor exponential clustering.  Gaplessness
can change probabilities, relaxation, and tightness; it cannot move a
same-window TPM branch off `Z` while (2D-INT) holds.

This remains true when the chosen broken vacuum is not an eigenstate of the
window charge.  In that case the first measurement resolves an initially
broad integral distribution and dephases the state.  The law may have many
integer atoms, but no fractional ones.

### ⟨1⟩13. What replaces the kink picture

The natural 2D picture is **spin-charge radiation through a closed curve**.
A local disturbance launches Goldstone wave packets.  The disk TPM record
counts their net selected 0-form charge across the circumference; an annulus
records the signed balance across its inner and outer boundaries.  Angular
profiles, multipoles, and neutral Goldstone pairs are invisible to the
single total-charge record unless additional observables are measured.

For a Heisenberg ferromagnet, a single spin flip is an exact magnon and its
position amplitude obeys a 2D lattice Schrödinger equation with quadratic
Goldstone dispersion.  Its disk law is Bernoulli: the magnon stayed or it
escaped.  With interactions and multiple magnons, the law becomes a general
probability distribution on `Z`.

For a zero-temperature antiferromagnet, the conserved TPM observable is a
selected **uniform** spin generator.  Staggered magnetisation is an order
parameter, not the conserved charge, and must not be substituted into this
theorem.  Linear Goldstone modes and their infrared clouds can make the
large-window/long-time analysis delicate; finite-window integrality remains
exact, while `(LR2_2D)--(LR3_2D)` and a useful thermodynamic radiation law are
open here.

Thus “spin-wave radiation memory” is a viable operational replacement for
kink transport, but only in the modest sense of the distribution of net
conserved 0-form charge crossing a chosen curve.  It is not asserted to be a
complete phase invariant.

---

## 6. Exact 2D spin-wave/ED probe

The checker `theory/checks/memory_index_2d_check.py` uses the spin-`1/2`
nearest-neighbour ferromagnet

`H=J sum_{<xy>}(1/4-S_x.S_y)`

on a `9 x 9` open square.  The fully polarised state is an exact ground
state.  The one-spin-flip sector is also exact, with

`H_1=(J/2)L_square`,

and infinite-square dispersion
`epsilon(k)=J(2-cos k_x-cos k_y)=J|k|^2/2+O(|k|^4)`.  The measured integral
charge is magnon number `n_x=1/2-S^z_x`, whose on-site spectrum is `{0,1}`.
The computation is therefore a small exact diagonalisation of a genuine
Goldstone sector, not a semiclassical approximation.  Finite volume has an
exact zero mode and a measured first excitation gap `0.0603074`; that finite
gap is not used as evidence for a thermodynamic gap.

At `J=1` and `t=2.75`, starting with one magnon at the centre:

| window | exact TPM law | integrated outward current | residue |
|---|---|---:|---:|
| disk `x^2+y^2<=4` (13 sites) | `p(nu=0)=0.1761882522`, `p(nu=1)=0.8238117478` | `0.8238117478` | `8.88e-16` |
| annulus `1<x^2+y^2<=9` (24 sites) | `p(nu=0)=0.3087287945`, `p(nu=-1)=0.6912712055` | `-0.6912712055` | `4.55e-15` |

The annular sign is informative: the annulus is initially empty, so magnon
entry gives a negative escaped increment.  Its current is the oriented sum
over both boundary components.

An independent seeded state, chosen to straddle the disk boundary, probes
the genuinely noncommuting two-time TPM construction at
`t_-=-0.37,t_+=1.41`.  A common irrational scalar offset
`sqrt(3)/11=0.157459...` is added to both readouts.  The measured law is

`p(-1)=0.0971892004, p(0)=0.8224412578, p(1)=0.0803695418`,

with normalisation residue `0` and TPM mean/dephasing-identity residue
`4.86e-17`.  The irrational offset cancels exactly as §2 predicts.

The square-lattice geometry gate records disk triples
`(R,|W|,|partial_E W|)=(1,5,12),(2,13,20),(3,29,28)` and annulus boundary
size `40`, exhibiting the perimeter rather than two-endpoint boundary
battery.

Run record under optimisation:

```text
python3 -O theory/checks/memory_index_2d_check.py
    M2D-C1--C4 PASS; ALL GREEN; exit 0

python3 -O theory/checks/memory_index_2d_check.py --red fractional-charge
    RED-OK; noninteger distance 0.414214 at nu=+-sqrt(2); exit 1
```

The red mutation changes the local charge spacing from `1` to `sqrt(2)` and
therefore breaks (2D-INT).  TPM normalisation and the dephasing identity stay
green; the integer-support gate alone catches the mutation.  There are no
bare assertions.  The checker establishes no infinite-volume time limit,
SSB construction, antiferromagnetic result, or `(LR3_2D)` bound.
In particular, this finite `9x9`, finite-time ED is not a witness for
`(LR2_2D)` or `(LR3_2D)`, and therefore is not a nonzero instance of
`M-INDEX-2D-spec`.

---

## 7. MERGE PROPOSALS

No proposal below is applied in this lane.

### MP-1 -> `definitions.md`

Keep D26 unchanged: it is already dimension-free.  Add a new 2D definition
(next available D-number) consisting of §1's disk/annulus protocol and
§4's `(LR1_2D)--(LR3_2D)`, including:

- a declared domain and exhaustion (disk for `Z^2`, or annulus for an
  exterior domain);
- `Qhat_W=sum_{x in W}q_x-b_W I` with either SSB-profile or symmetric-vacuum
  scalar background;
- the same-window TPM sign `nu=q_- - q_+`;
- the fixed order: infinite-volume dynamics, fixed-window Cesàro time limit,
  spatial exhaustion;
- charge memory `M_Q`, not an assumed scalar wall displacement;
- the perimeter warning and the optional-convergence scope.

### MP-2 -> `claims/CLAIMS.md`

| proposed id | proposed statement | proposed status | dependencies | proof/check |
|---|---|---|---|---|
| `M-INDEX-2D-fin` | Under D26/(2D-INT), every finite disk/annulus charge (2D-Q) has spectrum in one coset of `Z`, invariant under `alpha_t`; its same-window TPM escaped increment is integer-valued by offset cancellation. | `PROVED`; capped review complete | D26, `M-INDEX-fin` | §2; checker M2D-C2 |
| `LR1-GEN-2D` | The live `LR1-GEN` theorem applies to `Z^2`; one subsequence works for all finite disks/annuli and their TPM weights. | no new status row needed; corollary of existing `PROVED` row | `LR1-GEN`, `M-INDEX-2D-fin` | §3 |
| `M-INDEX-2D-spec` | `(2D-INT)+(LR1_2D)--(LR3_2D)` imply that every ordered limit point is a probability on `Z` and obeys the charge ledger (2D.4); optional full-law convergence gives uniqueness. | `SKETCH`; no nonzero model instance of `(LR2_2D)--(LR3_2D)` is known | `M-INDEX-2D-fin`, `LR1-GEN`, proposed 2D definition | §4; no numerical gate for the limit |

The scoping sentence for `M-INDEX-2D-spec` must say verbatim in substance:
`(LR2_2D)` and `(LR3_2D)` are assumed, not derived; boundary terms are
perimeter-sized; no scalar interface displacement, channel completeness,
unconditional Goldstone instance, 1-form-symmetry result, or topological
order result is claimed.

### MP-3 -> checker registration

Register `theory/checks/memory_index_2d_check.py` only as finite-volume
evidence for the exact spin-wave radiation interpretation and as an
arithmetic regression guard for the finite theorem.  Its green run proves
nothing about `(LR2_2D)--(LR3_2D)`; its red run is binding only if the
statement or implementation ceases to detect nonintegral on-site charge.

## 8. Final status

The 2D finite-window theorem is a clean, channel-free **PROVED** transplant.
The probability-theoretic part of the donor limit proof also transplants once the
2D nondemolition and first-moment-tightness clauses are assumed.  What does
not transplant is the 1D conversion from escaped charge to a unique kink
position.  In a 2D Goldstone phase the honest observable is instead the
integer-valued history of net conserved spin charge radiated through a
chosen closed boundary; obtaining its unconditional ordered limit remains
open, so `M-INDEX-2D-spec` remains **SKETCH**.
