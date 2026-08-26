# SPT rebuild — bulk soft rigidity and quantised endpoint residue

**Status (2026-08-26): proposer artifact, pre-critic.**  This file replaces the
failed scope of `spt-scoping-draft.md` without editing it.  A complete Lamport
proof is given for the registered transfer-matrix statements.  Per L5/L6, the
merge proposals keep the rebuilt rows at **SKETCH** until an independent critic
passes this artifact.  Statements about a physical half-chain Hilbert space are
conditional on **(H-split)**; scattering and nonzero memory remain explicitly
conjectural.

The sharp result is not pointwise bulk blindness.  That is false.  The result is
the following rigidity dichotomy.

* A closed bulk insertion has no projective *failure of multiplication*: its two
  endpoint multipliers cancel exactly.  Its scalar coefficients are continuous,
  deformable transfer contractions and may retain class-correlated adjoint
  representation data.  Such raw numbers are not quantised merely by `[ω]`.
* An unpaired endpoint has a registered operator residue in an
  `ω`-projective module.  Its module class and the charge-lattice offset are
  discrete.  For the AKLT half-chain the exact finite-window residue tends to
  `-Z/2`, whereas the trivial `O(2)` large-`D` product edge has integral
  residue `0`.

This dissolves the apparent T8 contradiction: the no-go concerns a *bulk
projective multiplier/topological interpretation*, not all coefficient data;
the endpoint residue is itself a quantised coefficient.

---

## ⟨1⟩1. Ground truth and scope

**⟨2⟩1.** Definitions D1--D12 and claims WI/A1/G0 are used as frozen.  The
retyped proposals below are named `Sd1'`--`Sd10'` because D19--D23 are not edited
in this lane.  **Justification:** `definitions.md` D1--D12; claims WI/A1/G0.

**⟨2⟩2.** Finite and Lie symmetry statements are separated:

* `G_f=D_2` is used for exact projective-versus-linear endpoint modules and for
  the adjoint counterexample.  There is no fictitious `ξ` or infinitesimal soft
  limit for `D_2`.
* `G_c=O(2)=U(1)⋊ℤ_2` is used for the explicit charge-packet comparison:
  rotations about `z` supply `ξ`, and the `π` rotation about `x` pins the
  integer/half-integer offset.  The connected `SO(3)` version is stated as a
  general representation-theory corollary, but no `SO(3)`-nonsymmetric product
  state is used as its comparator.

**Justification:** critic S5; D2(e), D10 require a Lie group for `X(ξ)` and
`q_x(ξ)`.

**⟨2⟩3. Local-TeX quotations (L3).**  These are the only literature facts used.

1. `refs/arxiv-0802.0447/StringOrder-v10.tex`, Lemma 1: the modulus-one twisted
   transfer eigenvalue exists iff there are a unitary `V` and phase satisfying
   `V^\dagger \widetilde A_j=e^{i(\theta-\theta_j)}\widetilde A_jV^\dagger`.
   The same source states condition C3 as `[E,V\otimes\bar V]=0`, and Theorem 1
   requires a dressed endpoint with
   `tr(V\Lambda A_nA_m^\dagger)\ne0`.  Its AKLT example gives
   `A^0=σ_z/√3`, `A^{±1}=√(2/3)σ_±`, `V=σ_z`, and string order `-4/9`.
2. `refs/arxiv-2405.00439/MPU-DW.tex` says that for the displayed on-site
   truncated-symmetry commutator the operator is the identity and its
   expectation is `+1`; it also states that local (non-domain-wall)
   excitations transform linearly.  For noncommuting group elements an ordinary
   group commutator may of course remain; the source rules out the anomalous
   phase in its commuting/order-two route.
3. `refs/arxiv-1509.07840/Draft5.tex` derives its anomalous single-soft term
   from a massless `q^{-2}` current pole and `δΓ`, and then states that the
   anomalous extra term supplies no pole in the double-soft LSZ limit.  Neither
   mechanism exists for the gapped registered form factors below.
4. `refs/arxiv-1412.5604/SPT.tex` states that the two virtual boundaries together
   form a representation while either boundary may be projective, with inverse
   cocycles at the two ends.  For a twist it obtains a projective boundary
   action from a slant product.  This is prior art for endpoint compensation,
   not a proof of the one-dimensional statements below.

**⟨2⟩4.** Whitehead's lemma is used only for the narrow statement that the
`so(3)` Lie bracket has no central extension.  It is never used to erase the
dimension, Casimir, weights, or integrability class of a representation.
**Justification:** D4(d) caveat; critic S3.

---

## ⟨1⟩2. Retyped definitions `Sd1'`--`Sd10'` (proposal form)

### ⟨2⟩1. `Sd1'` — exact comparison tensors, parent terms, and half-chain boundaries

Use the Cartesian spin-one basis `(|x⟩,|y⟩,|z⟩)`, in which

`u(R_x)=diag(1,-1,-1)`, `u(R_y)=diag(-1,1,-1)`,
`u(R_z)=diag(-1,-1,1)`.

The spherical and Cartesian AKLT tensors are related by a physical basis change.
The exact tensors are

`A^0=Z/√3`, `A^{±1}=√(2/3)σ_±`,

or, in the Cartesian gauge, `A^a=σ_a/√3`, `a=x,y,z`.  The virtual `D_2`
operators are Pauli matrices and obey `V(R_x)V(R_z)=-V(R_z)V(R_x)`.

For a same-phase deformation used below, put

`A_b^x=a_bX`, `A_b^y=a_bY`, `A_b^z=bZ`,
`a_b:=√((1-b²)/2)`, `0<b<1`.                                      **(2.1)**

It is left canonical, injective at length two, `D_2`-symmetric with the same
Pauli projective representation, and `U(1)`-symmetric about `z`.  The isotropic
AKLT point is `b=1/√3`.

The required exact, normalised, injective, bond-dimension-two trivial tensor is

`T_t^x=[[0,t√3/2],[t/2,0]]`, `T_t^y=0`,
`T_t^z=diag(√(1-t²/4),√(1-3t²/4))`, `0<t≤1`.                       **(2.2)**

At `t=1`, `Σ_s(T^s)^†T^s=I`, the right fixed point is
`r=diag(3/4,1/4)`, the transfer spectrum is `{1,√3/2,0,0}`, and the length-two
words have rank four: `(T^z)^2=diag(3/4,1/4)` and
`(T^x)^2=(√3/4)I` span the diagonal subspace, while `T^zT^x` and `T^xT^z`
are independent off-diagonal matrices.  Thus it satisfies D1.  Let

`θ=(1,-1,-1,1)`, `V_T=(I,Z,I,Z)` for `(e,R_x,R_y,R_z)`.

Then `u(g)T=θ(g)V_T(g)^{-1}TV_T(g)` and `V_T` is an honest linear
representation.  The path `t↓0` is symmetric and tends to the product state
`|z⟩^{⊗∞}`; it is injective for every `t>0`, while the redundant `χ=2`
description becomes noninjective only at the product endpoint.  This is the
promised symmetric dressing of the product state.  Exact verification is check
**S-C1** in `theory/checks/spt_rebuild_check.py`.

There is no injective `χ=2`, spin-one, `SO(3)`-symmetric *trivial* tensor:
`SO(3)` has no nontrivial two-dimensional linear irrep, and `V=I⊕I` would make
the intertwiner support only a single physical character, contradicting
injectivity.  We therefore do not fake such a comparator.  The actual
continuous comparison uses `O(2)`: the exact trivial product tensor
`P^z=1`, `P^x=P^y=0` (`χ=1`) is invariant under `z` rotations and under the
reflection/`R_x` up to its removable one-site phase, while finite-`D_2`
same-bond-dimension comparisons use (2.2).  This separation is forced by
typing, not a change of target.

For any injective tensor `C`, define

`Γ_2^C(|i⟩⊗|j⟩):=Σ_{s,t}(C^sC^t)_{ij}|s,t⟩`,
`W_2^C:=Γ_2^C[(Γ_2^C)^†Γ_2^C]^{-1/2}`,
`h_C:=I-W_2^C(W_2^C)^†`.                                         **(2.3)**

The half-chain parent Hamiltonian is

`H_{C,+}:=h_{∂,C}+Σ_{x≥0}τ_x(h_C)`.                               **(2.4)**

For AKLT, `h_C=P^{(S=2)}` and `h_{∂,A}=0`; the left projective doublet is not
split.  For (2.2), let `K_T=μ|1⟩⟨1|`, `μ>0`, on the left virtual factor and set

`h_{∂,T}:=W_2^T(K_T⊗I)(W_2^T)^†`.                                 **(2.5)**

It is a positive two-site boundary term, commutes with `D_2` because
`[K_T,V_T(g)]=0`, and selects the one-dimensional trivial-character edge
`|0⟩`.  Equations (2.3)--(2.5) are the boundary Hamiltonians used in the
deciding computation.  The inverse square root is on `ran Γ_2`; injectivity
makes it well defined.  For the `χ=1` `O(2)` product comparator,
`h_P=I-|zz⟩⟨zz|` and `h_{∂,P}=0`, so the half-chain edge is uniquely trivial.

### ⟨2⟩2. `Sd2'` — fixed boundary transfer register

Let `C` be a left-canonical injective tensor with right fixed point `r>0`.
For `O` supported on the first `n` sites of the half-chain define the
matrix-valued boundary contraction

`𝒞_C^{(n)}(O):=r^{-1/2} E_O(r) r^{-1/2} ∈ End(E_C)`,
`E_C:=ℂ^χ`,                                                     **(2.6)**

where `E_O` is the D1(d) transfer contraction through those `n` sites.
Thus `𝒞_C^{(n)}(I)=I_{E_C}`.  This is an operator in the *fixed finite Hilbert
register* `E_C` before any scalar matrix element or limit is taken.  It is
unconditional finite-dimensional transfer algebra; it is not yet asserted to
be an operator on the physical GNS Hilbert space.

For a finite chain of length `N`, use the same formula with the actual right
boundary density and write `𝒞_{C,N}`.  At fixed support,
`𝒞_{C,N}(O)→𝒞_C(O)` with the D1(c) bound
`C_{λ̃}λ̃^{N-n}` for every `λ̃∈(λ_E,1)`.

### ⟨2⟩3. `Sd3'` — explicit packet/profile families and order of limits

Fix once and for all
`φ(y)=c_φ exp[-1/(1-y²)]` for `|y|<1`, `φ(y)=0` otherwise, where `c_φ>0`
normalises `∫|φ(y)|²dy=1`.

* **Bulk packet:**
  `f_{L,κ}^{bulk}(x):=Z_{L,κ}^{-1/2}φ(x/L)e^{iκx/L}` with
  `Z_{L,κ}:=Σ_x|φ(x/L)|²`; its central momentum and width are both `O(L^{-1})`.
  It is finitely supported for every `L`, so `Q[f_{L,κ}^{bulk};ξ]∈𝔄_loc`.
* **Edge packet/profile:** `f_L^{edge}(x):=1` for `0≤x<L` and `0` otherwise.
  Its Fourier width is `O(L^{-1})`, and it converges pointwise to the half-line
  step.  A smooth taper may replace the sharp cut, but is a different family
  and must not be mixed into a reported number.
* **Finite-group endpoint profile:**
  `g_L^{edge}(x):=g` for `0≤x<L`, `e` otherwise, applied with the
  model-specific normal-ordered on-site operator
  `ǔ_C(g)=e^{-iθ_C(g)}u(g)` so no extensive phase survives.

The order is:

`N→∞` at fixed `L` with `N-L→∞`; normalize the external packet states at that
fixed `L`; take scattering/time limits if present; only then take `L→∞`
(equivalently `k_L∼L^{-1}→0`).                                  **(2.7)**

No plane wave, half-string, or edge profile is declared to be an element of
`𝔄`.  For finite `G`, `𝕊(g)` is a compensated large-window endpoint/string
limit, **not** an infinitesimal momentum-soft limit.  This is consistent with
D3 and D12.

### ⟨2⟩4. `Sd4'` — operator-valued bulk and endpoint soft insertions

For fixed finite-dimensional normalized channel registers
`K_in,K_out` and packet embeddings `W_{in/out}^{N,L}` into a finite chain, put

`𝔉_{N,L}^{bulk}(ξ):=(W_{out}^{N,L})^†Q[f_{L,κ}^{bulk};ξ]W_{in}^{N,L}`
`∈Hom(K_in,K_out)`.                                               **(2.8)**

The embeddings include all tangent-space gauge fixing and Gram normalization;
their covariance and nonvanishing smallest Gram eigenvalue are hypotheses of a
multi-leg application, not consequences of D5.

On the fixed edge register put

`ℜ_{C,L}(ξ):=𝒞_C(Q[f_L^{edge};ξ])∈End(E_C)`,
`𝕊_{C,L}^{comp}(g):=` the normalized decorated contraction of
`Ǔ_{C,[0,L-1]}(g)` with `V_C(g)^{-1}` inserted on the remote cut
`(L-1|L)`, viewed on the dual left-edge register.                       **(2.9)**

Here `Ǔ` is the product of `ǔ_C(g)` from `Sd3'`; the explicit cut insertion
cancels the remote WI endpoint.  The uncompensated scalar string compression is
a different object and may decay to zero.

The registered residues are `ℜ_C(ξ):=lim_{L→∞}ℜ_{C,L}(ξ)` and
`𝕊_C(g):=lim_{L→∞}𝕊_{C,L}^{comp}(g)`, when these operator-norm limits exist in
`End(E_C)`.  Their physical edge-Hilbert-space interpretation is governed by
`Sd7'`, not built into this definition.

### ⟨2⟩5. `Sd5'` — scalar form factors

Only after (2.8)--(2.9), define normalized scalar form factors by

`F_{N,L}^{bulk}(e',e;ξ):=⟨e'|𝔉_{N,L}^{bulk}(ξ)|e⟩`,
`F_{C,L}^{edge}(e',e;ξ):=⟨e'|ℜ_{C,L}(ξ)|e⟩`,                     **(2.10)**

for unit vectors in the fixed registers.  A scalar is never declared to be
algebra-valued.  The “soft factor” is the operator limit; (2.10) is one of its
matrix elements.

### ⟨2⟩6. `Sd6'` — admissible amplitude topology and regularity

Finite-window contractions use operator norm on the finite registers.
Thermodynamic limits are uniform on compact tensor paths with a common
`λ̃<1` transfer bound.  A soft coefficient of order `p` exists only if the
`L→∞` limit in (2.8) is uniform through `p` derivatives (hypothesis
**H-soft-p**).  Scattering amplitudes additionally require the appropriate
wave operators and asymptotic completeness; transfer continuity alone does not
supply LSZ or current regularity.

### ⟨2⟩7. `Sd7'` — projective endpoint module and (H-split)

The unconditional endpoint object is the transfer register `E_C` of (2.6), or
equivalently A1(d1)'s padded-window module.  It carries `V_C(g)` with multiplier
`ω_C`.  Let `d_ω` be the minimal dimension of an `ω`-projective irrep.

**(H-split).**  The half-chain ground/low-energy subspace admits a normal split
realisation and an isometry `J_C:E_C→H_{edge}` intertwining `V_C(g)` with the
physical half-chain symmetry, such that registered local contractions converge
to the corresponding compressed physical operators.  This is exactly the
missing normality/infinite-volume Schmidt step in
`corner-a.md` ⟨1⟩4.⟨2⟩9.  Every statement about `H_edge` or scattering carries
(H-split) explicitly.  No registered transfer statement needs it.

### ⟨2⟩8. `Sd8'` — shifted charge lattice

Let the identity component of compact `G_c` contain a circle generated by `ξ`,
and let the universal cover of that component have kernel `Z`.  An
`ω`-projective representation, with its lift normalised compatibly with the
full group and the physical vacuum charge, restricts to an honest
representation of the corresponding central extension.  **Assume** this full-
group normalisation fixes a class-invariant central character
`ν_ω:Z→U(1)`.  For a lifted `2π` path ending at `z_ξ∈Z`, define
`q_ω(ξ)∈ℝ/ℤ` by

`exp(2πiq_ω(ξ))=ν_ω(z_ξ)`.                                      **(2.11)**

The Hermitian endpoint charge `Q_edge(ξ):=-iX_C(ξ)` has weights in
`q_ω(ξ)+ℤ`.  For `SO(3)`, the two lifts give `q_ω=1/2` and `0`.  In the explicit
`O(2)` comparison, the disconnected reflection pins the same two offsets:
AKLT has `V(2π)=-I` and `q_ω=1/2`, while the large-`D` product has
`V(2π)=I` and `q_ω=0`.  The offset is absolute only after the full global group
and the `2π` loop are fixed; `U(1)` alone does not protect it.

### ⟨2⟩9. `Sd9'` — twist endpoints and compensation

A finite `g`-twist is a string on `[a,b]` and therefore has *two* registered
endpoints.  A single endpoint is a bookkeeping factor `V(g)`; the physical
pair carries `V(g)` and its inverse/dual, so all gauge phases cancel globally.
For a measurable endpoint statement assume **(H-dress)**: endpoint operators
`O_a,O_b` have nonzero transfer overlap with the relevant virtual sectors and
the endpoint separation tends to infinity before other limits.  This is the
one-dimensional version of the nonzero dressed-end condition in Theorem 1 of
`refs/arxiv-0802.0447`.

### ⟨2⟩10. `Sd10'` — protected memory terminology

Let `Q_edge` be the registered Hermitian endpoint charge and let a half-chain
scattering process satisfy **(H-AD-edge)**: asymptotic wave operators exist,
bulk packets separate from the edge, and total `U(1)` charge decomposes as
`Q_tot=Q_edge+Q_bulk` on each channel.  Define the edge memory operator on the
scattering space by

`ΔQ_edge:=W_+^*Q_edgeW_+-W_-^*Q_edgeW_-`.                        **(2.12)**

“Protected” means that a nontrivial projective endpoint module cannot be
replaced by a unique symmetric edge state under a symmetric gapped deformation.
“Quantised” means channel eigenvalues of (2.12), not arbitrary expectations.
“Permanent” additionally requires that after the packet leaves, the isolated
edge dynamics preserves the recorded charge sector.  None of these words means
that a particular reflection matrix element is forced to be nonzero.

---

## ⟨1⟩3. THEOREM SPT-B' — closed-bulk multiplier no-go and coefficient rigidity

**ASSUME.**

* (B1) A compact path `t∈I↦A(t)` of D1 injective canonical tensors, all
  covariant under the same on-site `G`, with a common transfer bound
  `sup_t λ_E(t)<λ̃<1`.
* (B2) Every external leg is in a fixed normalized bulk register, with no
  string endpoint; Gram matrices stay uniformly positive.
* (B3) Profiles are the bulk packets of `Sd3'`, or any finite-support/no-net-jump
  profiles.  If a soft coefficient is asserted, (H-soft-p) is assumed.

**PROVE.**

(i) Any projective multiplier extracted from ordered *closed bulk* symmetry
insertions is identically trivial.  Closed bulk amplitudes are invariant under
rephasing a fixed lift `V(g)↦λ(g)V(g)`.

(ii) Every finite-window normalized scalar coefficient, and every thermodynamic
or soft coefficient covered by the stated uniform hypotheses, is continuous in
`t` (and `C^p` when the data and H-soft-p are `C^p`).

(iii) Therefore a bulk scalar coefficient is an SPT invariant only if it is
separately shown to be locally constant on every symmetric injective component.
The multiplier cancellation alone does **not** provide that proof.  Bulk
numbers may distinguish inequivalent `Ad(V)` representation types and may
correlate with `[ω]` through deformable non-universal data.

### ⟨2⟩1. PROVE (i): the only universal bulk no-go

**⟨3⟩1.** A finite on-site symmetry string on a bulk interval leaves exactly
`V(g)^{-1}` and `V(g)` at its two boundary bonds.  **Justification:** WI,
`corner-a.md` ⟨1⟩3; D2(b).

**⟨3⟩2.** In a closed contraction the two factors occur in the doubled action
`V(g)⊗\bar V(g)`, equivalently `Ad(V(g))`.  Rephasing `V(g)` changes neither.
**Justification:** ⟨3⟩1; condition C3 quoted from
`refs/arxiv-0802.0447/StringOrder-v10.tex`.

**⟨3⟩3.** Ordered multiplication gives
`(V(h)⊗\bar V(h))(V(g)⊗\bar V(g))`
`=ω(h,g)\barω(h,g)V(hg)⊗\bar V(hg)`
`=V(hg)⊗\bar V(hg)`.  Hence the projective failure of multiplication is
exactly one.  **Justification:** D2(c); `|ω|=1`.

**⟨3⟩4.** The same conclusion holds before any tensor contraction because the
physical truncated on-site operators themselves multiply honestly, with no
projective scalar.  In the commuting/order-two truncated-commutator route of
the cited model the commutator is the identity; for noncommuting elements only
the ordinary group commutator can remain.  **Justification:** D3(b); the on-site
identity quoted from `refs/arxiv-2405.00439/MPU-DW.tex`.

**⟨3⟩5. QED.**  A bulk cocycle representative and a bulk projective
multiplication anomaly are absent.  This proves (i), but says nothing about the
isomorphism type of the honest representation `Ad(V)`.

### ⟨2⟩2. PROVE (ii): transfer continuity

**⟨3⟩1.** At finite `N,L`, an unnormalised contraction is polynomial in the
entries of `A(t)`, its conjugate, the external tensors, and the fixed profile.
**Justification:** D1(b),(d),(e); definitions (2.8)--(2.10).

**⟨3⟩2.** Normalisation multiplies by inverse square roots of finite Gram
matrices.  These are continuous (respectively `C^p`) while their smallest
eigenvalue is bounded away from zero by (B2).  **Justification:** continuous
functional calculus on positive matrices; (B2).

**⟨3⟩3.** On the compact path, the isolated fixed-point projection `P_t` and
the complementary resolvent are continuous.  The common spectral separation
in (B1) gives a uniform bound
`||E_t^m-P_t||≤C_{λ̃}λ̃^m`.  Therefore thermodynamic contractions converge
uniformly in `t`.  **Justification:** D1(c); compactness and continuity of
finite-dimensional spectral projections.

**⟨3⟩4.** A uniform limit of continuous functions is continuous.  Under
(H-soft-p), the same argument applies to the first `p` derivatives and the
soft coefficients.  **Justification:** (B3), `Sd6'`; the elementary uniform
limit theorem.

**⟨3⟩5. QED.**  This proves (ii).

### ⟨2⟩3. PROVE (iii), and exhibit actual deformation

**⟨3⟩1.** `[ω(t)]` is locally constant along (B1), whereas (ii) only makes a
coefficient continuous.  Continuity does not imply local constancy.
**Justification:** A1(g), `corner-a.md` ⟨1⟩4.⟨2⟩7; elementary topology.

**⟨3⟩2.** The inference “`Ad(V)` has no multiplier, hence contains no
class-correlated data” is false.  For `D_2`, Pauli conjugation on `M_2`
decomposes into all four one-dimensional characters once, while conjugation by
the scalar trivial representation is four copies of the trivial character.
The closed scalar `Tr Ad(V(R_x))` is respectively `0` and `4`.
**Justification:** named computation **S-C2**, checker output; direct Pauli
conjugation.

**⟨3⟩3.** A natural bulk soft-charge coefficient actually changes inside one
fixed nontrivial phase.  With the *specified* packet of `Sd3'`, let

`C_bulk(b):=lim_{L→∞}`
` ⟨Q[f_{L,κ}^{bulk};S^z]^†Q[f_{L,κ}^{bulk};S^z]⟩_c`
` / Σ_x|f_{L,κ}^{bulk}(x+1)-f_{L,κ}^{bulk}(x)|²`.                 **(3.1)**

Equivalently, writing the distributional kernel
`S_{zz}^{(b)}(k):=Σ_{n∈ℤ}e^{ikn}⟨S_0^zS_n^z⟩_c`, concentration of the packet at
zero gives `C_bulk(b)=lim_{k→0}S_{zz}^{(b)}(k)/[2(1-cos k)]`.

Transfer contraction gives

`⟨(S_0^z)^2⟩=1-b²`,
`⟨S_0^zS_n^z⟩=-(1-b²)²(2b²-1)^{n-1}` for `n≥1`,
`C_bulk(b)=b²/[4(1-b²)]`.                                        **(3.2)**

Thus `C_bulk(1/√3)=1/8`, while `C_bulk(0.7)=0.240196078431…`, although
`V(R_x),V(R_z)` remain the same anticommuting Pauli pair and `[ω]` is fixed.
**Justification:** geometric summation of the transfer eigenchannel; named
computation **S-C3** (`0.125000023426` and `0.240196083171` at `k=10^{-3}`).

**⟨3⟩4.** Therefore (3.1) is not topological, and no other raw coefficient is
promoted merely because it is written using `Ad(V)`.  A separately proved
locally constant representation invariant remains possible; (i) only excludes
a closed-bulk projective multiplier.  **Justification:** ⟨3⟩1--⟨3⟩3.

**⟨3⟩5. QED.**  This proves (iii), hence SPT-B'.  □

**Scope boundary.**  SPT-B' neither asserts equality of AKLT and TRIV bulk
amplitudes nor says that complete bulk tomography cannot identify the phase.
It says exactly what survives S2: closed on-site soft insertions have no
projective anomaly, and their ordinary coefficients are continuous data unless
a separate rigidity proof quantises them.

---

## ⟨1⟩4. THEOREM SPT-E' — registered endpoint residue and shifted lattice

**ASSUME.**  D1/D2 in the unbroken case, normal ordering, and `Sd1'`--`Sd8'`.
For the Lie-charge clauses assume (S) and operator-norm convergence of (2.9).
For a statement on a physical edge Hilbert space additionally assume
(H-split).  For deformation rigidity assume a continuous symmetric injective
path with discrete `H²(G,U(1))`.

**PROVE.**

(i) In the fixed transfer register, the **compensated** endpoint group residue
is (up to the fixed left/right convention) `𝕊_C(g)=V_C(g)`, and the Lie residue is
`ℜ_C(ξ)=Q_edge(ξ)=-iX_C(ξ)`.  Scalar edge form factors are its matrix elements.

(ii) Every irreducible summand of the endpoint is `ω_C`-projective, hence a
protected summand has dimension at least `d_ω`; if `[ω_C]≠0` then `d_ω>1`.

(iii) Under `Sd8'`, `spec Q_edge(ξ)⊂q_ω(ξ)+ℤ`.  The offset and projective module
are constant under the stated symmetric gapped deformation.

(iv) For (2.1), including AKLT, the finite-window result is exactly

`ℜ_{A_b,L}(S^z)=-½[1-(2b²-1)^L]Z → -Z/2`.                       **(4.1)**

Thus the residue spectrum is `{−1/2,+1/2}` throughout this nontrivial path,
while the bulk coefficient (3.2) varies.  The `O(2)`-trivial product tensor has
the integral residue `0`.

### ⟨2⟩1. PROVE (i): endpoint telescoping in a fixed register

**⟨3⟩1.** Applying the normal-ordered `Ǔ_[0,L-1](g)` pulls through the tensor string and leaves
`V(g)^{-1}` at the physical boundary and `V(g)` at the remote cut.
**Justification:** WI, with its fixed D2 orientation; D1(e).

**⟨3⟩2.** In `𝕊_{C,L}^{comp}(g)`, the prescribed `V(g)^{-1}` cut insertion
cancels the remote WI factor exactly.  The only remaining factor acts at the
left boundary; choosing the dual left-edge register fixes it as `V_C(g)` rather
than `V_C(g)^{-1}`.  No such conclusion is asserted for the uncompensated
string overlap.  **Justification:** ⟨3⟩1; definition (2.9); D4(a4).

**⟨3⟩3.** For the Lie residue the derivative at the identity is taken at every
fixed `L` first, producing the physical partial charge
`Q[f_L^{edge};ξ]`; only then is `L→∞` taken.  Differentiating WI at fixed `L`
and using the transfer bound leaves `X_C(ξ)` at the edge, so the Hermitian
residue is `-iX_C(ξ)`.  This derivative-before-window order need not commute
with taking an uncompensated finite `g` string to infinite length.
**Justification:** D2(e), D10(c), G0(d), (S), `Sd3'`, and D1(c).

**⟨3⟩4.** Equation (2.10) now gives scalar form factors as ordinary matrix
elements of this fixed operator.  **Justification:** `Sd5'`.

**⟨3⟩5. QED.**  This proves (i) in the transfer register.  Under (H-split),
`J_C𝕊_C(g)J_C^†` and `J_Cℜ_C(ξ)J_C^†` give the corresponding physical edge
operators.  **Justification:** `Sd7'`.

### ⟨2⟩2. PROVE (ii): module dimension

**⟨3⟩1.** Endpoint multiplication is
`V(h)V(g)=e^{iω(h,g)}V(hg)`.  Hence every invariant irreducible block is an
`ω`-projective irrep.  **Justification:** D2(c); A1(d1) on padded windows; ⟨2⟩1.

**⟨3⟩2.** By definition its dimension is at least `d_ω`.  If a projective irrep
were one-dimensional, its scalar multiplier would be the coboundary of that
one-dimensional lift; therefore a nontrivial class has no one-dimensional
projective irrep.  **Justification:** definition of `d_ω`; elementary group
cohomology.

**⟨3⟩3. QED.**  This proves (ii).  It protects the module/degeneracy, not a
chosen nonzero transition amplitude.

### ⟨2⟩3. PROVE (iii): shifted weights and rigidity

**⟨3⟩1.** On a `Q_edge(ξ)` eigenvector of weight `q`, the lifted `2π` loop acts
as `e^{2πiq}`.  The same loop is the central element `z_ξ`, which acts as
`ν_ω(z_ξ)`.  Thus `q-q_ω(ξ)∈ℤ`.  **Justification:** definition (2.11) and the
spectral theorem in finite dimension.

**⟨3⟩2.** A1(g) makes `[ω]`, hence `ν_ω` and `q_ω mod ℤ`, constant along the
symmetric injective path.  Eigenvalues can move only within their shifted
integer sectors unless levels are added or removed in symmetry-compatible
blocks.  **Justification:** A1(g); (2.11).

**⟨3⟩3.** For `SO(3)`, the nontrivial lift to `SU(2)` sends the nontrivial
central element to `-1`, so `q_ω=1/2 mod ℤ`; the trivial lift sends it to `+1`,
so `q_ω=0 mod ℤ`.  For the explicit `O(2)` pair the same conclusion follows
directly from `V_A(2π)=-I`, `V_P(2π)=I`; the reflection is part of the group
that makes this offset invariant.  **Justification:** `Sd8'`; the defining
double cover `SU(2)→SO(3)`; the displayed AKLT and product virtual actions.

**⟨3⟩4. QED.**  This proves (iii).

### ⟨2⟩4. PROVE (iv): exact AKLT-family contraction

**⟨3⟩1.** For (2.1), `r=I/2` and the charge insertion at the boundary is
`E_{S^z}(r)=-(1-b²)Z/2`; the charge transfer channel obeys
`E_b(Z)=(2b²-1)Z`.  **Justification:** direct multiplication of Pauli matrices;
named computation **S-C4**.

**⟨3⟩2.** Summing sites `0,…,L-1` and applying the register normalisation
`r^{-1/2}(·)r^{-1/2}=2(·)` gives the geometric sum
`-(1-b²)Σ_{n=0}^{L-1}(2b²-1)^nZ=-½[1-(2b²-1)^L]Z`.
**Justification:** ⟨3⟩1; `|2b²-1|<1`.

**⟨3⟩3.** At the isotropic point the convergence factor is `(-1/3)^L`; the
eigenvalues tend to `±1/2`.  At `b=0.7` the same limit holds although (3.2)
has changed.  The product tensor has `S_x^z|z⟩=0` at every site and hence zero
residue.  **Justification:** (4.1); `Sd1'`; named computation **S-C4**.

**⟨3⟩4. QED.**  This proves (iv), hence SPT-E' in the registered sense.  □

**What remains conditional.**  The operator on a *physical* half-chain edge
space is conditional on (H-split).  A nonzero magnon-to-edge transition matrix
element is not implied by this theorem.  The theorem supplies a quantised
residue spectrum and selection rules, not dynamics.

---

## ⟨1⟩5. SPT-T' and SPT-D' — twists and ordered endpoint-soft products

### ⟨2⟩1. THEOREM SPT-T' (registered twist/slant product)

**ASSUME.** `Sd9'`; a normalized cocycle convention
`V(h)V(g)=e^{iω(h,g)}V(hg)`; and `h∈C_G(g)` for the slant-product clause.
For a physical observable additionally assume (H-split) and (H-dress).

**PROVE.**  On one registered endpoint,

`V(h)V(g)V(h)^{-1}`
`=e^{i[ω(h,g)-ω(hgh^{-1},h)]}V(hgh^{-1})`.                       **(5.1)**

For commuting `g,h`, this is

`V(h)V(g)V(h)^{-1}=e^{i[ω(h,g)-ω(g,h)]}V(g)`,                    **(5.2)**

the `H²` commutator/slant character.  The other endpoint carries the inverse
phase, so only a relative two-endpoint charge or a dressed string correlator is
gauge invariant.

**⟨3⟩1.** `V(h)V(g)=e^{iω(h,g)}V(hg)`.  Also
`V(hgh^{-1})V(h)=e^{iω(hgh^{-1},h)}V(hg)`.  Eliminating `V(hg)` gives (5.1).
**Justification:** D2(c); associativity.

**⟨3⟩2.** If `[g,h]=e`, then `hgh^{-1}=g`, giving (5.2).
**Justification:** ⟨3⟩1.

**⟨3⟩3.** A finite physical twist has two endpoints, and the combined action
is honest; hence the second endpoint has the inverse multiplier.  An endpoint
matrix element is physical only when its dressing has nonzero transfer overlap.
**Justification:** WI; `Sd9'`; Theorem 1 quote from
`refs/arxiv-0802.0447/StringOrder-v10.tex`; the two-boundary structure quoted
from `refs/arxiv-1412.5604/SPT.tex`.

**⟨3⟩4. QED.**  SPT-T' is proved in the registered two-endpoint form.  The old
unqualified general-group one-endpoint formula is withdrawn.  □

### ⟨2⟩2. THEOREM SPT-D' (ordered double endpoint-soft limit)

**ASSUME.**  The finite-group profiles `g_L^{edge},h_L^{edge}` and compensated
endpoint contractions (2.9); take the thermodynamic limit, then `L→∞`, while
retaining the fixed endpoint register.  For a physical edge operator assume
(H-split) and (H-dress).

**PROVE.**

`𝕊_C(h)𝕊_C(g)=e^{iω_C(h,g)}𝕊_C(hg)` in `End(E_C)`.               **(5.3)**

The invariant information is the projective module (or relative endpoint
composition), not a gauge-invariant phase of one scalar matrix element.  For a
compact semisimple Lie group, differentiating (5.3) near the identity yields
the ordinary Lie bracket with no central term; the torsion class survives only
in finite/large transformations and global integrability data.

**⟨3⟩1.** Each single endpoint-soft limit is `V_C(·)` by SPT-E'(i).
**Justification:** ⟨1⟩4.⟨2⟩1.

**⟨3⟩2.** Their ordered product is (5.3) by the defining projective
multiplication law.  **Justification:** D2(c).

**⟨3⟩3.** Rephasing changes `ω` by a coboundary and conjugates no physical
two-endpoint observable; the class/module is invariant.  **Justification:**
Lemma IT(ii), `corner-a.md` ⟨1⟩2.

**⟨3⟩4.** Whitehead's lemma removes only an infinitesimal central term; it does
not identify half-integer and integer modules.  **Justification:** D4(d)
caveat; SPT-E'(iii).

**⟨3⟩5. QED.**  This proves SPT-D' in the ordered registered sense.  It is not
the continuum double-soft scattering theorem of arXiv:1509.07840.  □

---

## ⟨1⟩6. SPT-M' — protected edge memory, with the dynamical gap exposed

### ⟨2⟩1. Conditional charge-bookkeeping theorem

**ASSUME.**  (H-split), (H-AD-edge), conservation of the chosen `U(1)` charge,
and asymptotic channels with definite bulk and edge charges.

**PROVE.**  On every channel,

`ΔQ_edge=-(Q_bulk,out-Q_bulk,in)`.                               **(6.1)**

Consequently the channel spectrum lies in
`(q_ω+ℤ)-(q_ω+ℤ)=ℤ` (or the corresponding finite set after restricting the edge
multiplet).  For the AKLT doublet it is contained in `{-1,0,+1}`.  Expectations
are convex combinations and need not be integers.

**⟨3⟩1.** By (H-AD-edge), `Q_tot=Q_edge+Q_bulk` on both asymptotic channel
spaces.  **Justification:** `Sd10'`.

**⟨3⟩2.** Conservation gives `Q_tot,out-Q_tot,in=0`; rearrangement gives (6.1).
**Justification:** the assumed `U(1)` symmetry; exact charge bookkeeping, the
same mechanism as M-quant but with edge charge replacing wall position.

**⟨3⟩3.** SPT-E'(iii) puts edge eigenvalues in `q_ω+ℤ`; taking differences
gives the stated channel lattice.  **Justification:** ⟨1⟩4.⟨2⟩3.

**⟨3⟩4. QED.**  The bookkeeping theorem is conditional exactly where M-quant
is conditional on its asymptotic decomposition.  □

### ⟨2⟩2. What “protected edge magnon memory” can honestly mean

**PROVED in the registered/H-split setting:** a nontrivial `[ω]` protects the
existence of a projective edge module and hence a memory *capacity* of dimension
at least `d_ω`; symmetric local edge terms cannot replace it by a unique
symmetric state.  **Justification:** SPT-E'(ii); Schur's lemma.

**CONJECTURE SPT-M'-dyn:** for the specified AKLT parent Hamiltonian and an
explicit boundary-magnon coupling, at least one symmetry-allowed edge-changing
reflection matrix element is nonzero on an open momentum interval, and the
post-selected memory obeys (6.1).  The exact missing step is a half-chain
scattering calculation establishing (H-AD-edge), the on-shell reflection
matrix, and nonvanishing of that matrix element.

The following statements are **not** claimed:

* nonzero edge-changing reflection at every momentum;
* vanishing memory for every trivial boundary (accidental trivial edge modes
  can store memory);
* quantisation of an unconditioned expectation value;
* permanence without an isolated charge-preserving edge after the packet has
  departed.

This is the precise S6-safe boundary between topological protection and
model-dependent dynamics.

---

## ⟨1⟩7. Executable deciding computation for `bd tns-cpq`

### ⟨2⟩1. Frozen inputs and tolerances

The exact stage is implemented in
`theory/checks/spt_rebuild_check.py`.  Run:

```text
python3 -O theory/checks/spt_rebuild_check.py
python3 -O theory/checks/spt_rebuild_check.py --red
```

The green command must exit `0`; the red mutant reverses the edge-residue sign
and must exit nonzero.  Tolerances were fixed in the checker before execution:
`2×10^{-12}` for exact algebra and `2×10^{-7}` for the `k=10^{-3}` limit.

Exact tensors and quantities:

1. **AKLT/path:** (2.1), at `b=1/√3` and `b=0.7`; `r=I/2`.
2. **TRIV₂:** (2.2) at `t=1`; `r=diag(3/4,1/4)`; boundary splitting (2.5).
3. **TRIV₁:** `P^z=1`, used for the `O(2)` integral-charge comparison.
4. **Bulk normalized scalar:** the packet matrix element (3.1).  The exact
   checker evaluates its equivalent Fourier kernel
   `S_zz(k)/[2(1-cos k)]` at `k=10^{-3}` and also the direct bump packet at
   `L=2048,κ=1.3`, comparing both to (3.2).
5. **Edge normalized scalar matrix elements:** for `Z|±⟩=±|±⟩`,
   `F_{A,L}^{edge}(±,±;S^z)=∓½[1-(2b²-1)^L]`; off-diagonal elements vanish.
   The operator eigenvalues are also checked directly for `L=1,2,4,8,24,64`.
6. **Finite-group representation data:** the four character multiplicities of
   `Ad(V)`, the closed scalar `Tr Ad(V(R_x))`, and the compensated `R_z`
   endpoint contraction.  The checker also verifies that the uncompensated
   AKLT string overlap decays rather than being mistaken for `V(R_z)`.

### ⟨2⟩2. Numerical record (run now)

```text
TRIV: length-2 rank=4; transfer={1,0.866025403784,0,0};
      canonical residue=1.11e-16; D2 covariance residue=0
D2 Ad multiplicities: Pauli-projective=(1,1,1,1);
                      scalar-trivial=(4,0,0,0)
closed Tr Ad(Rx): 0 versus 4
explicit TRIV2 Ad multiplicities=(2,0,2,0);
closed Tr Ad(Ry): 4 versus projective 0
bulk C: 0.125000000000 -> 0.240196078431
         (k=1e-3: 0.125000023426, 0.240196083171)
packet L=2048, kappa=1.3: 0.125000135674, 0.240196105387
edge: max finite-window formula error=1.665e-16;
      limit error=2.220e-16; |q_edge|=0.500000000000
compensated AKLT Rz endpoint: exact Z through L=8;
uncompensated norm at L=8: (1/3)^8 = 1.5241579e-4
red mutant: FAIL, finite-window edge-residue error=1.333e+00
```

### ⟨2⟩3. Pass/fail matrix and claim disposition

| test | criterion fixed in advance | observed | effect of failure / success |
|---|---|---|---|
| **S-C1 TRIV typing** | canonical/covariance errors `<2e-12`, word rank `4`, unique peripheral eigenvalue | pass | failure invalidates `Sd1'`, all AKLT/TRIV comparisons, and the numerical spec; success establishes an exact comparison tensor, not an SPT theorem |
| **S-C2 critic counterexample** | Pauli `Ad` multiplicities `(1,1,1,1)`, scalar-trivial `(4,0,0,0)`, explicit TRIV₂ `(2,0,2,0)`, and the named closed scalars `0`/`4` | pass | failure would undermine critic S2; success permanently falsifies old SPT-B's pointwise-blindness inference and is required by SPT-B'(iii) |
| **S-C3 bulk deformation** | Fourier-kernel and direct `L=2048,κ=1.3` packet coefficients each within `2e-7` of (3.2), and endpoint values differ by `>0.1` | pass | failure falsifies formula (3.2)/the displayed example; success confirms this bulk coefficient is non-topological and supports SPT-B' |
| **S-C4 edge residue** | (4.1) error `<2e-12`; at `L=64`, `||ℜ+Z/2||∞<2e-12` for both path points | pass | failure falsifies SPT-E'(iv); success proves the exact registered AKLT residue, but not a scattering amplitude |
| **S-C5 module/boundary** | Pauli anticommutator, physical parent/boundary commutators, `[K_T,V_T(g)]`, and compensated endpoint errors `<2e-12`; uncompensated `L=8` norm `<2e-3` | pass | failure invalidates projective/linear boundary assignments or endpoint compensation; success confirms the fixed registered/boundary inputs |

### ⟨2⟩4. Dynamical follow-on (still `tns-cpq`, not silently counted as done)

Use (2.3)--(2.5) on open chains `N∈{48,64,96}`.  Construct normalized incoming
one-magnon packets with the fixed `φ` of `Sd3'`, centers at least `12ξ_c` from
the edge, momentum width `≤0.04`, and norm error `<10^{-8}`.  Extract the
reflection matrix `R_{e'e}(k)` only after the outgoing packet is again at least
`12ξ_c` from the boundary.

Pre-registered gates:

* probability conservation defect `<5×10^{-3}`;
* edge charge budget
  `|ΔQ_edge+(Q_bulk,out-Q_bulk,in)|<5×10^{-3}` per post-selected channel;
* finite-size drift of a reported nonzero channel `<10%` from `N=64` to `96`;
* call a channel “nonzero on an interval” only if its probability exceeds
  `25×` the combined truncation/finite-size error at three adjacent momenta.

A passing charge budget confirms only the conditional theorem's hypotheses for
that numerical instance.  A robust nonzero AKLT edge-changing channel confirms
SPT-M'-dyn for that Hamiltonian on the tested interval; a zero channel refutes
that model-specific conjecture, **not** SPT-E'.  A nonzero TRIV₂ channel shows
accidental boundary memory and refutes any revived “trivial implies zero” claim.

---

## ⟨1⟩8. Merge proposals (exact text; not applied in this lane)

### ⟨2⟩1. Replacement text for D19--D23

```markdown
# SPT soft rigidity and endpoint residue — D19--D23

## D19 (soft profiles, fixed registers, and limit order)

Let `C` be a D1 injective left-canonical tensor with right fixed point `r>0`.
For an operator `O` on the first `n` sites of a half-chain define its normalized
boundary transfer compression
`𝒞_C^{(n)}(O):=r^{-1/2}E_O(r)r^{-1/2}∈End(E_C)`, `E_C:=ℂ^χ`; hence
`𝒞_C^{(n)}(I)=I`.  This fixed finite-dimensional transfer register is defined
before scalar matrix elements or limits.  Its identification with a physical
edge Hilbert space is hypothesis (H-split) of D21.

Fix `φ(y)=c_φe^{-1/(1-y²)}` for `|y|<1` and zero otherwise, with
`∫|φ|²=1`.  The bulk family is
`f_{L,κ}^{bulk}(x)=Z_{L,κ}^{-1/2}φ(x/L)e^{iκx/L}` with
`Z_{L,κ}=Σ_x|φ(x/L)|²`; the edge family is
`f_L^{edge}=1_{[0,L-1]}`.  For a finite group use
`g_L^{edge}(x)=g` on `[0,L-1]` and `e` otherwise, with the normal-ordered
on-site operator `ǔ_C(g)=e^{-iθ_C(g)}u(g)`.  Every finite-`L` object is local.
Limits are ordered: `N→∞` at fixed `L` with `N-L→∞`; normalize packet
states; take scattering/time limits if present; then `L→∞` (`k_L∼L^{-1}→0`).
For finite `G` the last operation is only a large-window endpoint/string limit,
not an infinitesimal group or momentum-soft limit.

## D20 (operator-valued soft insertions and scalar form factors)

For fixed normalized finite-dimensional bulk channel registers and embeddings
`W_{in/out}^{N,L}`, define
`𝔉_{N,L}^{bulk}(ξ)=(W_out^{N,L})†Q[f_{L,κ}^{bulk};ξ]W_in^{N,L}`.
On the edge transfer register define
`ℜ_{C,L}(ξ)=𝒞_C(Q[f_L^{edge};ξ])` and
`𝕊_{C,L}^{comp}(g)` as the decorated contraction of
`Ǔ_{C,[0,L-1]}(g)` with `V_C(g)^{-1}` on the remote cut, viewed on the dual
left-edge register.  The compensation cancels the far WI endpoint; an
uncompensated string overlap may decay.  Soft residues are operator-norm limits
after the D19 order.  Scalar form factors are only their matrix elements, e.g.
`F_{C,L}^{edge}(e',e;ξ)=⟨e'|ℜ_{C,L}(ξ)|e⟩`; a scalar is never algebra-valued.

Thermodynamic limits are uniform only on compact tensor paths with a common
transfer bound.  A coefficient through order `p` carries hypothesis (H-soft-p):
the soft limit is uniform through `p` derivatives.  Scattering statements also
carry the required wave-operator/asymptotic-completeness hypotheses.

## D21 (endpoint module, shifted charge lattice, and physical-edge hypothesis)

The unconditional endpoint object is `E_C` (equivalently A1(d1)'s padded-window
module), carrying the projective action `V_C(g)` with multiplier `ω_C`.
`d_ω` is the minimal dimension of an `ω`-projective irrep.  A nontrivial class
has `d_ω>1` because a one-dimensional multiplier is a coboundary.

**(H-split):** the half-chain ground/low-energy subspace has a normal split
realisation and an isometry `J_C:E_C→H_edge` intertwining `V_C` with the
physical half-chain symmetry, and registered local contractions converge to
the corresponding compressed physical operators.  This is the explicit
hypothesis replacing the SKETCH box `corner-a.md` ⟨1⟩4.⟨2⟩9.

If the identity component of compact `G` contains a circle, let the universal
cover of that component have kernel `Z`.  Assume a lift normalised compatibly
with the full group and the physical vacuum charge fixes a class-invariant
central character `ν_ω:Z→U(1)`.  If the lifted `2π` path of a
circle generator `ξ` ends at `z_ξ∈Z`, define
`e^{2πiq_ω(ξ)}=ν_ω(z_ξ)`.  Then the Hermitian endpoint charge
`Q_edge(ξ)=-iX_C(ξ)` has spectrum in `q_ω(ξ)+ℤ`.  For `SO(3)`, the two classes
give `q_ω=1/2` and `0 mod ℤ`.  For the explicit `O(2)` pair, reflection pins the
same alternatives: AKLT has `V(2π)=-I`, the large-`D` product `V(2π)=I`.  The
full global group and loop are part of this statement; `U(1)` alone does not
protect the offset.

## D22 (twists, ordered endpoint products, and edge memory)

A finite `g`-twist has two endpoints.  A single registered endpoint carries
`V(g)`, while the other carries the inverse/dual multiplier; a physical
endpoint observable requires (H-split) and (H-dress), meaning nonzero dressed
endpoint transfer overlaps with endpoint separation taken first.  For commuting
`g,h`, conjugation at one endpoint is
`V(h)V(g)V(h)^{-1}=e^{i[ω(h,g)-ω(g,h)]}V(g)`; the other endpoint compensates
the phase.  Ordered endpoint-soft operators obey
`𝕊(h)𝕊(g)=e^{iω(h,g)}𝕊(hg)` in the registered module.

Under (H-AD-edge), asymptotic total charge decomposes as
`Q_tot=Q_edge+Q_bulk`.  Define
`ΔQ_edge=W_+†Q_edgeW_+-W_-†Q_edgeW_-`.  “Protected” refers to the projective
edge module/degeneracy, “quantised” to channel eigenvalues, and “permanent”
additionally requires isolated charge-preserving edge dynamics.  Protection
does not force a particular reflection matrix element to be nonzero.

## D23 (exact comparison tensors and boundary Hamiltonians)

In the Cartesian spin-one basis, the AKLT tensor is
`A^a=σ_a/√3`, equivalently `A^0=Z/√3`,
`A^{±1}=√(2/3)σ_±`.  Its `D₂` virtual operators are Pauli matrices and carry
the nontrivial class.  The symmetric same-phase path is
`A_b^x=a_bX`, `A_b^y=a_bY`, `A_b^z=bZ`,
`a_b=√((1-b²)/2)`, `0<b<1`.

The exact normalized injective `χ=2` trivial tensor is
`T_t^x=[[0,t√3/2],[t/2,0]]`, `T_t^y=0`,
`T_t^z=diag(√(1-t²/4),√(1-3t²/4))`, `0<t≤1`, with
`θ=(1,-1,-1,1)` and `V_T=(I,Z,I,Z)` on `(e,R_x,R_y,R_z)`.
At `t=1`, `r=diag(3/4,1/4)`, transfer spectrum `{1,√3/2,0,0}`, and length-two
word rank four.  As `t↓0` it tends symmetrically to `|z⟩^{⊗∞}`.  The `O(2)`
Lie-charge trivial comparator is the `χ=1` product tensor `P^z=1`; it is not an
`SO(3)` comparator.

For any such tensor `C`, set
`Γ_2^C(|i⟩⊗|j⟩)=Σ_{s,t}(C^sC^t)_{ij}|s,t⟩`,
`W_2^C=Γ_2^C[(Γ_2^C)†Γ_2^C]^{-1/2}`,
`h_C=I-W_2^C(W_2^C)†`, and
`H_{C,+}=h_{∂,C}+Σ_{x≥0}τ_x(h_C)`.
For AKLT, `h_C=P^(S=2)` and `h_{∂,A}=0`.  For `T=T_1`,
`h_{∂,T}=W_2^T(μ|1⟩⟨1|⊗I)(W_2^T)†`, `μ>0`; it is `D₂`-symmetric and selects
the one-dimensional trivial-character edge.  For the `χ=1` `O(2)` product
comparator, `h_P=I-|zz⟩⟨zz|` and `h_{∂,P}=0`.
```

### ⟨2⟩2. Replacement SPT rows for `claims/CLAIMS.md`

```markdown
| SPT-B-r1 | Old claim that `Ad(V)`-only closed contractions are pointwise `[ω]`-blind | **REFUTED**: Pauli-projective `Ad` has four distinct `D₂` characters, scalar-trivial `Ad` has four trivial copies; closed `Tr Ad(R_x)=0` vs `4` | — | disproved in theory/spt-rebuild.md ⟨1⟩3.⟨2⟩3 | spt_rebuild_check.py S-C2 |
| SPT-nogo | Old all-orders claim that `[ω]` cannot appear in any coefficient, including an edge residue | **REFUTED** (Whitehead removes only a Lie central term; edge weights/dimension remain) | — | theory/spt-rebuild.md ⟨1⟩4 | S-C4 |
| SPT-B' | Closed-bulk multiplier no-go and rigidity: paired on-site endpoint multipliers cancel exactly; normalized bulk coefficients are continuous under common-gap symmetric injective paths and are topological only if separately proved locally constant; class-correlated `Ad(V)` data are allowed | **SKETCH** (complete proposer proof; L6 critic pending) | WI, A1(g), D19-D23 | theory/spt-rebuild.md ⟨1⟩3 | spt_rebuild_check.py S-C2,S-C3 |
| SPT-E' | Registered half-chain residue is `V(g)` / `Q_edge=-iX`; endpoint modules have dimension `≥d_ω` and charge weights in `q_ω+ℤ`; AKLT-family residue is exactly `-½[1-(2b²-1)^L]Z→-Z/2`, while the `O(2)` trivial product residue is `0` | **SKETCH** in transfer register (complete proposer proof; L6 pending); **CONJECTURE conditional on H-split** as a physical edge-Hilbert statement | A1(d1,g), D19-D23 | theory/spt-rebuild.md ⟨1⟩4 | spt_rebuild_check.py S-C4,S-C5 |
| SPT-T' | At a registered twist endpoint, `V(h)V(g)V(h)^{-1}` is proportional to `V(hgh^{-1})`; for commuting `g,h` the phase is `e^{i[ω(h,g)-ω(g,h)]}`; the second endpoint compensates, so the observable is relative and requires H-dress | **SKETCH** registered (L6 pending); physical observable conditional on H-split/H-dress | SPT-E', WI, D22 | theory/spt-rebuild.md ⟨1⟩5.⟨2⟩1 | — |
| SPT-D' | Ordered endpoint-soft operators satisfy `𝕊(h)𝕊(g)=e^{iω(h,g)}𝕊(hg)` in the fixed register; for semisimple Lie groups the infinitesimal bracket has no central term, while the global module remains projective | **SKETCH** registered (L6 pending); physical edge statement conditional on H-split | SPT-E', D22 | theory/spt-rebuild.md ⟨1⟩5.⟨2⟩2 | S-C5 |
| SPT-M' | Given H-split and H-AD-edge, channel charge bookkeeping is `ΔQ_edge=-(Q_bulk,out-Q_bulk,in)` and channel outcomes are quantised; `[ω]` protects memory capacity/module, not a nonzero amplitude | **SKETCH conditional theorem** (L6 pending) | SPT-E', D22, M-quant bookkeeping | theory/spt-rebuild.md ⟨1⟩6.⟨2⟩1 | dynamical follow-on tns-cpq |
| SPT-M'-dyn | For the specified AKLT parent/boundary coupling, an edge-changing magnon reflection amplitude is nonzero on an open momentum interval and leaves the post-selected charge memory of SPT-M' | **CONJECTURE**; missing half-chain wave operators, on-shell reflection matrix, and nonvanishing proof | SPT-M', H-AD-edge | theory/spt-rebuild.md ⟨1⟩6.⟨2⟩2 | tns-cpq follow-on |
```

### ⟨2⟩3. Exact replacement for `TRIANGLE.md` §5

```markdown
## §5. SPT soft rigidity — bulk deformability versus endpoint quantisation

Rebuilt shard: `theory/spt-rebuild.md`; definitions D19--D23.  Status is
SKETCH pending the shard's L6 critic.  The old pointwise bulk-blindness theorem
and the all-orders edge no-go are REFUTED.

**Dichotomy.**  A closed on-site bulk string has two virtual endpoints.  Their
projective multipliers cancel, so no projective multiplication anomaly can be
extracted from a closed bulk soft insertion.  This does not erase the honest
adjoint representation: Pauli-projective conjugation and scalar-trivial
conjugation are distinguishable (`Tr Ad(R_x)=0` versus `4`).  Normalized bulk
coefficients are continuous transfer data under a common-gap symmetric MPS
path and become topological only after a separate local-constancy proof.

An unpaired half-chain endpoint instead carries a fixed registered projective
module.  Its residue spectrum lies in the `[ω]`-shifted charge lattice.  On the
anisotropic AKLT path,
`C_bulk(b)=b²/[4(1-b²)]` changes from `1/8` to `0.240196...`, while
`ℜ_L(S^z)=-½[1-(2b²-1)^L]Z→-Z/2` is unchanged.  This is the rigid topological
content.  A physical edge-Hilbert interpretation carries hypothesis H-split.

| id | rebuilt statement | honest status |
|---|---|---|
| SPT-B' | Closed-bulk endpoint multipliers cancel exactly; coefficients are continuous/deformable and may retain class-correlated `Ad(V)` data | SKETCH, complete proposer proof; L6 pending |
| SPT-E' | Registered residue is the endpoint charge in an `ω`-projective module, `dim≥d_ω`, `spec Q_edge⊂q_ω+ℤ`; AKLT residue `±1/2`, trivial `O(2)` product residue `0` | SKETCH registered; physical edge statement conditional on H-split |
| SPT-T' | For commuting `g,h`, one twist endpoint carries the slant/commutator phase `e^{i[ω(h,g)-ω(g,h)]}` and the other compensates; measurable only relatively with dressed endpoints | SKETCH registered; H-split/H-dress physically |
| SPT-D' | Ordered endpoint-soft products realise the cocycle globally; no semisimple Lie central term is claimed | SKETCH registered; H-split physically |
| SPT-M' | Conditional channel bookkeeping quantises edge-charge changes and the projective module protects memory capacity; topology does not force a nonzero reflection amplitude | SKETCH given H-split/H-AD-edge; nonzero AKLT channel CONJECTURE |

**Exact deciding computation.** `spt_rebuild_check.py` fixes all tensors and
tolerances.  It verifies the explicit injective `χ=2` TRIV tensor, the critic's
`D₂` adjoint decomposition, the varying bulk coefficient, and the rigid AKLT
edge residue; its red mutant fails.  The remaining `tns-cpq` work is the
half-chain scattering calculation.  A zero AKLT edge-changing amplitude would
refute only SPT-M'-dyn, not the registered endpoint theorem.

**Closed route.**  The commuting/order-two truncated-symmetry commutator used
to diagnose the MPU anomaly is the identity for an on-site symmetry (a
noncommuting group can retain only its ordinary group commutator).  SPT
information here is therefore a projective endpoint module, a relative dressed
two-endpoint response, or a quantised edge residue—not an anomalous closed-bulk
commutator phase.
```

---

## ⟨1⟩9. Self-audit against the r1 adversary

| objection | rebuilt answer |
|---|---|
| **S1 (FATAL, type/limit)** | `Sd2'` fixes `E_C=ℂ^χ`; (2.8)--(2.9) define operator-valued insertions first; (2.10) defines scalars later. `Sd3'` fixes `f_{L,κ}^{bulk}`, `f_L^{edge}`, and the exact order `N→∞`, normalization/scattering, then `L→∞`. |
| **S2 (FATAL, `Ad` inference)** | Conceded and made a theorem boundary. SPT-B'(i) proves only multiplier/rephasing cancellation. SPT-B'(iii) explicitly computes the `D₂` decompositions `(1,1,1,1)` versus `(4,0,0,0)` and closed scalars `0` versus `4`. Pointwise blindness is REFUTED. |
| **S3 (FATAL, Whitehead/T8)** | Whitehead is confined to “no Lie central term.” SPT-E' proves that global module dimension and weights survive and that the zeroth edge coefficient is half-integral for AKLT. The old all-orders no-go is REFUTED. |
| **S4 (FATAL, non-executable test)** | (2.1)--(2.5) give exact AKLT, exact normalized injective `χ=2` TRIV, fixed points, parent and boundary Hamiltonians. §7 names scalar numbers and a priori tolerances; the green and red runs are recorded. |
| **S5 (finite/Lie conflation)** | `G_f=D₂` is used only for finite endpoint/module tests; the explicit Lie-charge comparison uses `O(2)`, under which both AKLT and the `χ=1` large-`D` product are symmetric. The impossibility of a trivial `SO(3)`-linear injective `χ=2` spin-one tensor is stated, and the product is explicitly not called `SO(3)`-symmetric. |
| **S6 (protection versus amplitude)** | SPT-E' protects module/degeneracy only. SPT-M' separates exact conditional charge bookkeeping from SPT-M'-dyn, whose nonzero reflection amplitude is CONJECTURE. Trivial accidental memory is allowed. |
| **S7 (slant scope)** | SPT-T' gives the correct general conjugation (5.1), restricts the ratio (5.2) to commuting elements, fixes the cocycle convention, and makes two-endpoint compensation plus H-dress explicit. |
| **S8 (theorem language with gaps)** | Every assumption is in the theorem headers. Registered proofs are complete but merge status remains SKETCH until L6. H-split and dynamical scattering are never promoted. |
| **T8 (edge coefficient contradiction)** | The bulk no-go is now about projective multiplication/topological interpretation, not all coefficient data. The edge residue is explicitly allowed—and proved—to be a quantised zeroth coefficient. |
| **T9 (deciding computation not decisive)** | The new computation no longer compares words. It tests exact normalized scalars, representation multiplicities, finite-window residue eigenvalues, and two points of a fixed-class path. Each failure is mapped to a specific row; endpoint algebra is not misreported as scattering or memory. |

### ⟨2⟩1. Additional hostile checks

* **Hidden endpoints:** SPT-B' assumes bulk registers with no string endpoint;
  a hidden string violates (B2) and is an edge/twist amplitude by definition.
* **Accidental constancy:** SPT-B' does not say every coefficient varies.  A
  locally constant bulk representation invariant may exist; it needs its own
  proof.  This prevents continuity from being over-read.
* **Gap along paths:** only compact subpaths with a common transfer bound are
  used.  The `T_t` path loses injectivity at `t=0`, and no theorem crosses that
  endpoint.
* **Boundary locality:** (2.5) is an explicit two-site physical term built from
  the injective range map, not an unexplained virtual penalty.
* **Charge-offset gauge:** the explicit half/integer statement fixes `O(2)`,
  including its reflection, and the `2π` loop.  The connected `SO(3)` corollary
  fixes its double cover separately.  No protected half charge is attributed
  to `U(1)` alone.
* **Expectations versus outcomes:** SPT-M' quantises post-selected channel
  eigenvalues; superposed or mixed expectations remain continuous, as in
  M-quant.

**⟨2⟩2. QED of the rebuild audit.**  All four fatal defects are removed rather
than weakened by wording: the object is typed, the false inference is refuted
numerically and algebraically, the bulk/edge boundary is consistent, and the
test compares fixed numbers.  The remaining open step is named exactly:
half-chain scattering/nonvanishing for SPT-M'-dyn, plus (H-split) if the paper
wants a physical edge-Hilbert theorem rather than the unconditional registered
transfer theorem.  □
