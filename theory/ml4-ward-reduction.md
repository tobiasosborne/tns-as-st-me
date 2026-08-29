# ML4 — Ward/LSZ reduction and the finite-volume analytic interpolation

Status: the abstract cancellation lemma ML4-A and exact finite-sector Ward
projection (8)--(11) are **PROVED per `verdicts/corpus-r2.md` adjudication**.
The FM formulas (15)--(17) are only an **off-shell analytic interpolation** at
fixed periodic `N`: nonzero ring momenta are discrete, so `k→0` at fixed `N`
is not an on-shell ring limit.  The formerly claimed volume-uniform bound is
**retracted**: the first physical sequence `k=2π/N` makes its constant diverge.
A packet-smeared infinite-volume on-shell trace estimate is future work (bd
`tns-7ut`).
The two-hard/three-magnon channel remains open for the independent reason
recorded in ⟨1⟩5.  No closed-form S-matrix is used below.

This shard uses D3, D6--D8, D10, D12(a′), `soft-current-recon.md` (R1),
(R13)--(R15), and the complete two-magnon spectral resolution (15)--(21) of
`ml2-completeness.md`.  “Orthogonal” means the finite-ring descendant
projection, intended eventually for a genuine infinite-volume on-shell packet
limit; (15)--(17) themselves use only the off-shell interpolation.  It does
**not** mean that the zero-momentum descendant is an infinite-volume Hilbert
vector.

## ⟨1⟩1. Register, packet class, and the quantity reduced

**ASSUME.** Fix `I=[a,b]⋐(0,π)` and choose `ε_I>0` so that, for `h∈I` and
`|k|≤ε_I`, (i) `h+k∈(0,π)`, (ii) `v(h)>v(k)`, and (iii) `h+k≠π`.  On an
`N`-site ring let `ℋ_{n,N}` be the `n`-down-spin sector, let
`D_{n,N}:=Q_0|_{ℋ_{n,N}}`, and write `J^-_0` for the lowering current (R1).

Hard packets are samples of `g∈C_c^∞(I)` with norm

\[
 \|g\|_{I,N}^2={2\pi\over N}\sum_{h\in I\cap(2\pi\mathbb Z/N)}|g(h)|^2,
 \qquad \|g\|_I^2=\int_I |g(h)|^2dh .                         \tag{1}
\]

Soft packets are `f_ε(k)=ε^{-1/2}f(k/ε)`, where
`f∈C_c^∞((-1,1))`; their position profiles are rapidly decreasing and hence
belong to D12(a′), `ℓ¹∩BV`.  The product norm is `L²(dk)⊗L²(I,dh)`.

For a hard subspace on which `D_{n,N}^†D_{n,N}` is invertible, set

\[
 P_{n,N}:=D_{n,N}(D_{n,N}^\dagger D_{n,N})^{-1}D_{n,N}^\dagger,
 \qquad R_{n,N}:=(1-P_{n,N})J^-_0 .                           \tag{2}
\]

Thus `R_{n,N}` is the current component orthogonal to the **whole descendant
subspace**, not merely to one momentum vector.  For one hard magnon, momentum
conservation makes this equivalent fiber by fiber to orthogonality to
`Q_0|h⟩_N`.

Let `Γ_N(k)` be the analytic interpolation obtained by parallel-transporting
the coordinate scattering formula from total momentum `h+k` to the `k=0`
fiber.  At fixed periodic `N` it is a physical ring channel only when all
momenta satisfy the periodic quantisation conditions; it is otherwise an
off-shell analytic vector.  The corresponding interpolated orthogonal
contribution to the Ward-reduced connected numerator is

\[
 \mathcal A_{\perp,N}(k;f,g)
  :=(e^{ik}-1)\langle \Gamma_N(k)f,R_{n,N}g\rangle .           \tag{3}
\]

An **ML4-admissible analytic amputation at fixed `N`** may multiply (3), on either
side, by operator families bounded and `C¹` for `|k|≤ε_I`.  This excludes a
new `1/k` pole in the reduced (`1-P`) channel at that volume.  No
volume-uniform constant is included in this definition; an infinite-volume
use must assume its own packet-trace bound.  *(bd `tns-iu5` r4: D24(b)'s
leg-normalisation convention is strictly narrower than this ML4-admissible
class — D24(b) soft-leg envelopes must have `λ(0) = 1`; conclusions drawn
here about ML4-admissible amputations do not transfer to D24(b) amplitudes
unless they respect that restriction.)*

**⟨2⟩1. PROVE.** The classes in (1) obey the function-space discipline of D3
and D12, and (3) has a norm meaning before any plane-wave limit.

**⟨3⟩1.** A compact smooth momentum packet has a rapidly decreasing Fourier
transform, so its position profile and its first difference are in `ℓ¹`.
Justification: repeated integration by parts and D12(a′).

**⟨3⟩2.** Therefore the charge/current sums smeared by these packets converge
in the D12(a′) norm register; the plane waves in (3) are only kernels inside
that smearing.
Justification: D3(a), D10(c), and D12(a′).

**⟨3⟩3.** Uniformly bounded amputators preserve every `O(k^m)` estimate in the
product `L²` norm.
Justification: the definition of the operator norm.

**⟨3⟩4. QED.**

## ⟨1⟩2. Decisive standalone lemma: on-shell descendant matching

**LEMMA ML4-A (orthogonality supplies the second soft zero).**

**ASSUME.** `U:ℋ→𝒦` is an isometry, `P=UU†`, and
`Γ:(-ε,ε)→B(ℋ,𝒦)` obeys

\[
 \Gamma(0)=U,\qquad
 \sup_{|k|<ε}\|\partial_k\Gamma(k)\|\le C_\Gamma .            \tag{4}
\]

Let `J∈B(ℋ,𝒦)`, `R=(1-P)J`, and let `b∈C¹` satisfy `b(0)=0` and
`|b(k)|≤C_b|k|`.  The same statement is allowed for channel traces rather
than bounded generalized-state maps, provided (4) is read in the trace norm
on the chosen packet class.

**PROVE.**

\[
 \|b(k)\Gamma(k)^\dagger R\|
 \le C_bC_\Gamma\|J\|\,|k|^2 .                              \tag{5}
\]

For normalized `f_ε`,

\[
 \|b(k)\Gamma(k)^\dagger Rg\,f_ε(k)\|_{L²(dk;ℋ)}
 \le C_bC_\Gamma\|J\|\,ε^2\|u^2f(u)\|_{L²(du)}\|g\| .       \tag{6}
\]

**⟨2⟩1. PROVE (5).**

**⟨3⟩1.** `U†R=U†(1-UU†)J=0`.
Justification: `U†U=1` and the definitions of `P,R`.

**⟨3⟩2.** Hence
`Γ(k)†R=[Γ(k)-Γ(0)]†R`.
Justification: (4) and ⟨3⟩1.

**⟨3⟩3.** The fundamental theorem of calculus gives
`||Γ(k)-Γ(0)||≤C_Γ|k|`, while `||R||≤||J||`.
Justification: (4) and that `1-P` is an orthogonal projection.

**⟨3⟩4.** Multiply the bounds in ⟨3⟩2--⟨3⟩3 by
`|b(k)|≤C_b|k|` to obtain (5).
Justification: submultiplicativity of the operator norm.

**⟨3⟩5. QED.**

**⟨2⟩2. PROVE (6).** Substitute `k=εu` in the squared `L²` norm and apply
(5) pointwise; the factor `ε^{-1/2}` in `f_ε` cancels the Jacobian and leaves
`ε⁴` under the square root.
Justification: (5), (1), and change of variables.  **⟨3⟩1. QED.**

**⟨2⟩3. QED.** □

**Decisive interpretation.** The Ward identity is not what kills the
orthogonal `O(k)` term.  It identifies `P J`.  The killing property is the
pair

\[
 \boxed{\text{energy-shell channel matching }\Gamma(0)=U
 \quad+\quad C^1\text{ on-shell trace regularity}.}           \tag{7}
\]

Energy conservation and multiplicity one imply the first property in a genuine
FM two-body channel.  In the fixed-ring application below, however, (7) is
used only for the off-shell analytic interpolation.  The sign
`sgn(v_h-v_s)` only chooses which continuous wave is called outgoing; it
supplies no zero.

## ⟨1⟩3. The exact `SU(2)` Ward projection in every finite sector

> **ERRATUM (orchestrator, 2026-08-28; see `claims/CLAIMS.md` ML4-Ward row
> and bd `tns-uxr`).** The second display of (9) below holds at `n=1` ONLY
> and is REFUTED for `n≥2`: step ⟨3⟩4 applies the scalar `(N-2n)^{-1}` to
> the vector `2J^z_0ψ`, which is not in `ker S^+` for `n≥2`
> (`S^+J^z_0ψ = −J^+_0ψ ≠ 0`; at `n=1` it vanishes by momentum
> conservation). Verified correction, exact at every `n<N/2` on `ker S^+`:
> `P_{n,N}J^-_0 = 2D_{n,N}A_n^{-1}J^z_0` — i.e. use (10), whose
> `J^-_0S^+` term dies on `ker S^+`, but keep `A_n^{-1}` as the operator
> inverse. Refuting/confirming computations: soft-index-b-r1.md F1 (ED),
> the S1-B prover's own n=1 check, and
> `theory/checks/ml4_ward_n2_check.py` (independent full-space route;
> green/red). The first display of (9), (8), (10), (11), and (R15) are
> unaffected. ⟨1⟩5's ⟨3⟩2 ("put `n=2` in (9)") inherits the defect and is
> under audit (`tns-uxr`).

Let `S^±=Q_0^{\dagger},Q_0` and let `J^a_0` be the three components of the
same spin current.

**⟨2⟩1. PROVE.** On `ℋ_{n,N}`,

\[
 D_{n,N}^\dagger J^-_0=2J^z_0+J^-_0S^+ .                     \tag{8}
\]

On the highest-weight subspace `ℋ^{hw}_{n,N}:=ker S^+`, `n<N/2`,

\[
 D_{n,N}^\dagger D_{n,N}=(N-2n)1,
 \qquad
 P_{n,N}J^-_0={2\over N-2n}Q_0J^z_0\quad(\textbf{only }n=1) .   \tag{9}
\]

> **ERRATUM (2026-08-28, bd `tns-uxr`).**  The FIRST display of (9) is exact at
> every `n<N/2`.  The SECOND display is exact at `n=1` and **REFUTED for
> `n≥2`**: see ⟨3⟩4 below and `theory/checks/ml4_ward_n2_check.py`.  The form
> valid at every `n` is (10) specialised to `ker S^+`, namely
> `P_{n,N}J^-_0 = 2D_{n,N}A_n^{-1}J^z_0` with `A_n:=D_{n,N}^†D_{n,N}` taken on
> the **full** sector `ℋ_{n,N}` (where it is non-scalar).  **Register warning
> (`verdicts/ml4-ward-n2-audit.md` §1.2):** in the highest-weight-restricted
> register `D_λ:=Q_0|_{ker S^+}` one has `A_λ=(N-2n)𝟙`, so the string
> `2D A^{-1}J^z_0` collapses back to the refuted display; there the correct
> form is `(1/m_λ)Q_0Π_{hw}J^z_0` with `m_λ=(N-2n)/2`.  Any restatement of this
> identity MUST name its register.

For a general subspace on which `A_n:=D_{n,N}†D_{n,N}` is invertible,

\[
 P_{n,N}J^-_0
 =D_{n,N}A_n^{-1}(2J^z_0+J^-_0S^+).                       \tag{10}
\]

**⟨3⟩1.** The current transforms as an `SU(2)` vector, so
`[S^+,J^-_0]=2J^z_0`.
Justification: (R1), the swap's `SU(2)` invariance, and
`[S^+,S^-]=2S^z`; this is the computation used in (R14).

**⟨3⟩2.** Expanding `S^+J^-_0` with the commutator in ⟨3⟩1 gives (8).
Justification: `[A,B]=AB-BA`.

**⟨3⟩3.** If `S^+ψ=0` in the `n`-magnon sector, then
`S^+S^-ψ=[S^+,S^-]ψ=2S^zψ=(N-2n)ψ`.
Justification: `S^z=N/2-n` on `ℋ_{n,N}`.

**⟨3⟩4.** Insert ⟨3⟩2--⟨3⟩3 in definition (2) to obtain (10); without the
highest-weight restriction, insert (8) to obtain (10).
Justification: orthogonal projection onto the range of an injective map.

> **ERRATUM (2026-08-28, bd `tns-uxr`) — this leaf is where the defect sat.**
> Passing from (10) to the scalar second display of (9) applies `A_n^{-1}` as
> the scalar `(N-2n)^{-1}` to `2J^z_0ψ`.  That is legitimate only when
> `2J^z_0ψ` lies in `ker S^+`, i.e. the subspace on which the first display
> makes `A_n` scalar.  But `[S^+,J^z_0]=-J^+_0`, so `S^+J^z_0ψ=-J^+_0ψ`, which
> vanishes at `n=1` by momentum conservation and is **nonzero for `n≥2`**
> (`‖J^+_0ψ‖ = 0 / 0.66 / 1.36` at `n=1/2/3`, `N=8`).  Measured failure of the
> scalar display at `N=8`: error `0.26 / 1.11` against `‖lhs‖ = 0.91 / 1.39` at
> `n=2/3`, versus `≤2.4e-15` for the (10) form.  Certificate:
> `theory/checks/ml4_ward_n2_check.py` (green exit 0, `--red` exit 1);
> independently reconfirmed by the orchestrator, `verdicts/ml4-ward-n2-audit.md`.

**⟨3⟩5. QED.**

**⟨2⟩2. PROVE (one hard magnon).** For every nonzero ring momentum `h`,

\[
 P_{1,N}J^-_0|h\rangle_N
 ={2iv(h)\over N-2}Q_0|h\rangle_N,                            \tag{11}
\]

and (11) holds diagonally for every packet supported away from `h=0`.

**⟨3⟩1.** `|h⟩_N` is highest weight for `h≠0`, and direct one-magnon
evaluation gives `J^z_0|h⟩_N=iv(h)|h⟩_N`.
Justification: Fourier orthogonality and the bond computation in (R14).

**⟨3⟩2.** Put `n=1` and ⟨3⟩1 into (9).
Justification: equation (9).

**⟨3⟩3.** Fourier modes diagonalize translations, so linear superposition
gives the packet statement.
Justification: translation covariance and (1).

**⟨3⟩4. QED.**

Equation (11) is exactly (R15), upgraded from one momentum vector to the
whole hard packet space.  The complementary vector remains nonzero.  Thus the
Ward identity computes the leading projection but does not establish (5).

## ⟨1⟩4. FM one-hard coordinate branch: off-shell analytic interpolation

For `h∈I`, let `k` be signed and put `K=h+k`, `q=(h-k)/2`.  In the transported
center gauge define on `0≤x<y<N`

\[
 B_N(k,h;x,y)={e^{ih(x+y)/2}\over\sqrt N}
 \{s(k,h)e^{iq(y-x)}+e^{-iq(y-x)}\},                          \tag{12}
\]

where `s(k,h)` is the solution analytic at zero of the single contact
equation (R16).  Formula (12) only identifies neighboring total-momentum
fibers; undoing the transport replaces `h` in the center phase by `K` and
gives the infinite-volume ML2 generalized scattering wave.  At fixed periodic
`N`, continuous nonzero `k` generally violates the ring boundary condition;
thus (12) is the declared off-shell analytic interpolation, not an on-shell
ring state.  The channel map used in (3) is
the normalized `Γ_N(k)|h⟩:=B_N(k,h)/sqrt(N-2)`; the unnormalized `B_N` is
retained below because its trace estimate is stronger.

**⟨2⟩1. PROVE (zero-soft matching and analytic simplicity).** Uniformly for `h∈I`,

\[
 B_N(0,h)=Q_0|h\rangle_N,\qquad
 \Gamma_N(0)|h\rangle={Q_0|h\rangle_N\over\sqrt{N-2}},
 \qquad s(0,h)=1,                                             \tag{13}
\]

and the infinite-volume energy-conserving ML2 coordinate branch through (13)
is a unique `C¹` branch.  At fixed ring size its continuous parameter is the
off-shell interpolation just declared.  The ML2 bound band and singular class
do not meet the branch.

**⟨3⟩1.** At `k=0`, (R16) has the unique solution `s=1` because
`e^{ih}-1≠0`; substituting in (12) gives
`N^{-1/2}(e^{ihx}+e^{ihy})`, the coordinate formula (R3) for `Q_0|h⟩_N`.
Justification: (R3), (R16), and `h∈I⋐(0,π)`.

**⟨3⟩2.** In ML2 variables the scattering energy is
`E(K,q)=J[2-2cos(K/2)cos q]`; at `(K,q)=(h,h/2)`,
`∂_qE=J sin h=v(h)`, bounded below by `min_I v>0`.
Justification: ML2 (18), differentiation, and compactness of `I`.

**⟨3⟩3.** The implicit-function theorem therefore gives one uniform `C¹`
energy-shell branch near the soft point.
Justification: ⟨3⟩2 and compactness.

**⟨3⟩4.** At `k=0`, the bound energy is `J sin²(h/2)` while the scattering
energy is `ω(h)=2J sin²(h/2)`; their gap is at least
`J sin²(a/2)>0`.  The finite-ring singular state requires `K=π`, excluded by
the choice of `ε_I`.  Even before that exclusion its charge overlap is the
regular ML2 coefficient `2i cos((h-k)/2)`, not a hidden soft pole.
Justification: ML2 (19), O1, ML2 (12), ML2 (24), and the assumptions in
⟨1⟩1.

**⟨3⟩5. QED.**

**⟨2⟩2. PROVE (fixed-volume off-shell trace regularity).** Let

\[
 r_N(h):=(1-P_{1,N})J^-_0|h\rangle_N .                        \tag{14}
\]

For every fixed `N` there is `C_{I,N}<∞` such that for allowed ring momenta
`h∈I` and sufficiently small real interpolation parameter `|k|`,

\[
 |\langle B_N(k,h),r_N(h)\rangle|\le C_{I,N}|k| .             \tag{15}
\]

**⟨3⟩1.** The left side vanishes at `k=0` by (13) and the definition of the
orthogonal projection in (14).
Justification: (2), (13), and (14).

**⟨3⟩2.** At fixed `N`, the implicit solution of (R16) and every coordinate of
`B_N(k,h)` are analytic near `k=0` because `e^{ih}-1≠0` for `h∈I`.
Justification: the analytic implicit-function theorem, (12), and `h∈I`.

**⟨3⟩3.** Differentiating the finite coordinate pairing reduces it to the
finite geometric sums `Σe^{ihr}` and `Σr e^{ihr}`.  For a ring momentum
`h≠0`,

\[
 \left|\sum_{r=1}^{M}e^{ihr}\right|\le {2\over|1-e^{ih}|},\quad
 \left|\sum_{r=1}^{M}r e^{ihr}\right|
 \le {M\over|1-e^{ih}|}+{2\over|1-e^{ih}|^2}.                \tag{16}
\]

These bounds prove finiteness at each `N`; they do **not** give the formerly
claimed volume-uniform derivative after the transported relative-coordinate
phase is varied on separations of order `N`.
Justification: differentiation of a finite geometric series, (12)--(14), and
the explicit `N` dependence in (16).

**⟨3⟩4.** The derivative is continuous on a compact sufficiently small
`k`-interval at fixed `N`; call its maximum `C_{I,N}`.  Integrating from zero
and using ⟨3⟩1 gives (15).
Justification: ⟨3⟩1--⟨3⟩3 and the fundamental theorem of calculus.

**⟨3⟩5. QED.**

**⟨2⟩3. PROVE (the retracted uniform statement has an explicit
countersequence).**  Put `h=2π/5`, take ring sizes divisible by five, set
`k_N=2π/N`, and write
`F_N(k):=⟨B_N(k,h),(1-P_{1,N})J^-_0|h⟩_N⟩`.

**⟨3⟩1.**  The low-frequency relative-coordinate sum obeys

`lim_{N→∞} N^{-1}⟨B_N(c/N,h),B_N(0,h)⟩ = 8[1−cos(c/2)]/c²`.

At `c=2π` this is `4/π²`, rather than the `c=0` value `1`.
Justification: exact summation of the two finite geometric series in (12),
named computation **ML4-Q1** in `checks/ml4_check.py`.

**⟨3⟩2.**  The contact term changes by `o(1)` while the descendant subtraction
is fixed by (11), hence
`lim_{N→∞}|F_N(2π/N)| = 2|v(h)|(1−4/π²) > 0`.
Justification: (11)--(14), ⟨3⟩1, and named computation **ML4-Q1**.

**⟨3⟩3.**  Consequently `|F_N(k_N)|/|k_N|` grows linearly in `N`, while
`|(e^{ik_N}−1)F_N(k_N)|/(sqrt(N−2)k_N²)` grows as `sqrt(N)`.
Justification: ⟨3⟩2, `k_N=2π/N`, and the normalization below (12).

**⟨3⟩4.**  Thus no `N`-independent version of (15) or (17) holds on this
finite-ring transported trace.
Justification: ⟨3⟩3.  **⟨3⟩5. QED.**

**⟨2⟩4. PROVE (surviving fixed-volume off-shell interpolation).** For arbitrary
incoming and outgoing hard packets `g,f∈C_c^∞(I)` and every fixed `N`, the
orthogonal contribution (3) obeys

\[
 |\mathcal A_{\perp,N}(k;f,g)|
 \le C'_{I,N}|k|^2\|f\|_{I,N}\|g\|_{I,N}.                    \tag{17}
\]

Its normalized soft-packet norm is `O_N(ε²)`.  In particular,

`lim_{N→∞} lim_{k→0} 𝒜_{⊥,N}(k;f,g)/k = 0`,

where the inner limit is the off-shell analytic limit, not a physical on-shell
ring limit.  No statement about the reversed or joint limit is made.

**⟨3⟩1.** At fixed `N`, equations (13)--(15) are the trace-norm hypotheses of
ML4-A, while
`|e^{ik}-1|≤|k|`.
Justification: ⟨2⟩1--⟨2⟩2 and the sine bound.

**⟨3⟩2.** Apply ML4-A fiberwise and use Cauchy--Schwarz in the finite discrete
hard-packet norm to get (17), with constant `C'_{I,N}`.
Justification: ML4-A (5) and (1).

**⟨3⟩3.** Divide (17) by `|k|` and take `k→0` at fixed `N`; the result is zero.
The subsequent `N→∞` limit of this zero sequence is zero.
Justification: (17) and the stated order of limits.

**⟨3⟩4.** Apply ML4-A (6) at fixed `N` for the soft packet statement.  Bounded
`C¹` fixed-volume analytic amputators preserve the estimate by
⟨1⟩1.⟨2⟩1.
Justification: (6) and (17).

**⟨3⟩5. QED.** □

This is a fixed-volume analytic-interpolation result for arbitrary packet
samples, plus the displayed formal ordered limit.  It is **not** an on-shell
fixed-ring theorem and is **not** a packet-smeared infinite-volume trace theorem.
Obtaining the latter requires new control of the `kN=Θ(1)` regime; ML2
completeness alone does not supply it.

## ⟨1⟩5. Two hard magnons: exact Ward part and the remaining obstruction

**⟨2⟩1. PROVE.** Every finite-ring hard state in `ℋ_{2,N}` has the complete
ML2 expansion, and (10) gives its exact descendant projection:

\[
 P_{2,N}J^-_0 = 2D_{2,N}A_2^{-1}J^z_0 ,
 \qquad A_2:=D_{2,N}^\dagger D_{2,N}\ \text{on all of}\ ℋ_{2,N} .  \tag{18}
\]

For ML2 descendants the extra `J^-_0S^+` term in (10) is mandatory.

> **ERRATUM (2026-08-28, bd `tns-uxr`) — (18) formerly read
> `P_{2,N}J^-_0=\frac{2}{N-4}Q_0J^z_0` and was REFUTED.**  It is false already
> on the ML2 **singular contact vector** `|χ_π⟩ ∝ Σ_x(-1)^x|x,x+1⟩` — the very
> vector ⟨3⟩3 below names — by `100%` of the left-hand side: at `N=8`,
> `‖lhs‖=0.775`, `‖rhs_old‖=1.414`, error `0.775` (rel `1.000`); at `N=10`,
> error `0.504` (rel `0.730`).  The displayed corrected form is exact there
> (`≤2.4e-16`).  Independently recomputed twice
> (`verdicts/ml4-ward-n2-audit.md` §1.3 and the orchestrator's re-run).
> The two-hard Ward part therefore survives only in the (10)/(18) full-sector
> form; no scalar `(N-4)^{-1}` version of it is available.

**⟨3⟩1.** ML2 (14), including its singular contact vector, is an orthonormal
basis of `ℋ_{2,N}`.
Justification: Theorem ML2 and its equation (14).

**⟨3⟩2.** Put `n=2` in (9) on `ker S^+`; use (10) on its orthogonal
descendant multiplets.
Justification: ⟨1⟩3.⟨2⟩1.

**⟨3⟩3.** The ML2 singular vector is highest weight: applying `S^+` to its
alternating contact sum gives at each one-magnon site the two coefficients
`(-1)^x+(-1)^{x-1}=0`.  It therefore belongs to the (18) branch, whereas the
explicit zero-root descendants require (10).
Justification: ML2 (12), direct action of `S^+`, and ML2 ⟨1⟩3.⟨2⟩6.

**⟨3⟩4. QED.**

> **EXPLORATION ML4-3 (sharp obstruction).**
>
> To infer `O(k²)` for `R_{2,N}` one still needs a three-magnon outgoing
> channel `Γ_3(k)` satisfying the two hypotheses in (7), in a packet trace
> norm uniform in volume.  ML2 resolves the **input** two-magnon state but says
> nothing about the three-magnon target.  Unlike the two-body half-line
> Jacobi fiber, a three-body fixed-energy shell can have multiple open
> channels.  Energy conservation alone then does not force every zero-soft
> channel into `ran Q_0`; an orthogonal degenerate channel can contribute at
> `O(k)` after the single lattice difference.  Proving channel matching needs
> three-body wave operators plus a limiting-absorption/trace estimate;
> excluding the unwanted multiplicity is the sharp missing hypothesis.
> Closed Bethe factorization would hide this issue and is forbidden here.

**⟨2⟩2. PROVE (conditional two-hard statement).** If a selected
three-magnon soft-attached channel has a uniformly `C¹` trace and
`Γ_3(0)=Q_0(D_{2,N}†D_{2,N})^{-1/2}` on each fixed `SU(2)` multiplet, while
the reduced LSZ map has no `1/k` pole, then its orthogonal contribution is
`O(k²)` in the product packet norm.

**⟨3⟩1.** On each multiplet the displayed zero-soft map is an isometry and
its range projection is (2).
Justification: polar decomposition of `D_{2,N}`.

**⟨3⟩2.** The remaining assumptions are exactly ML4-A (4) in trace norm.
Justification: comparison with ML4-A.

**⟨3⟩3.** Apply ML4-A (5)--(6).
Justification: Lemma ML4-A.  **⟨3⟩4. QED.**

The conditional implication is algebraic; establishing its channel hypotheses
is a **CONJECTURE/future-work item**.  If “`n=2`” counts the final hard-plus-soft two-magnon sector rather
than two hard input magnons, it is already the proved theorem ⟨1⟩4.

## ⟨1⟩6. Numerical certificate

**⟨2⟩1. PROVE.** `theory/checks/ml4_check.py` passes normally and under
`python3 -O` for the fixed-volume Taylor probes `N=12,14,16,18,20`, and runs
the joint-scaling probe `k=2π/N` for `N=40,80,120,160`.

**⟨3⟩1.** The checker assembles `Q_0`, `J^-_0`, and `J^z_0` directly from
`(J/2)(1-P)`, solves the one contact equation for (12), and tests (11)--(15).
Justification: inspection of the checker.

**⟨3⟩2.** The fixed-volume fitted exponent of the raw orthogonal trace is
`0.99700--0.99988`; after multiplication by `e^{ik}-1` it is
`1.99700--1.99988`.  Omitting the projection is the built-in red mutation and
returns exponent `0.99991--0.99997`, so the test detects the claimed defect.
Maximum Ward/projection residuals are `8.899e-16` and `3.473e-15`.
Justification: the recorded optimized-mode run.

**⟨3⟩3.**  Named computation **ML4-Q1** verifies that the normalized
`k=2π/N` ratio grows rather than remaining bounded.  Its `--red-uniform`
mutation reinstates the retracted uniform claim and exits nonzero.
Justification: inspection and the recorded optimized-mode run of
`checks/ml4_check.py`.

**⟨3⟩4. QED.** □

## ⟨1⟩7. ML4 verdict

1. **PROVED per `corpus-r2.md` adjudication, SCOPED 2026-08-28 (bd `tns-uxr`):**
   exact sector Ward projection (8), the norm identity (first display of (9)),
   the general-sector polar formula (10), the corrected two-hard form (18), and
   the one-hard consequence (11)/(R15) — including arbitrary one-hard packets.
   **The scalar second display of (9) is PROVED only at `n=1` and REFUTED for
   `n≥2`**; the claim "all finite-ring ML2 two-hard states" is retained only in
   the (10)/(18) full-sector register, never in the scalar one.
2. **PROVED per `corpus-r2.md` adjudication:** the standalone cancellation lemma ML4-A.  The property that
   kills the orthogonal `O(k)` contribution is energy-shell descendant
   matching plus `C¹` trace regularity; the Ward identity computes the
   descendant residue, and the velocity sign merely labels the physical
   branch.
3. **SKETCH / HOLD per `corpus-r2.md`:** for one hard FM magnon and arbitrary
   smooth compact hard packet samples, (15)--(17) hold only for the off-shell
   analytic interpolation at each fixed volume.  A fixed periodic ring has no
   nonzero on-shell `k→0` sequence; the first physical joint sequence also
   refutes uniformity by ML4-Q1.  The missing on-shell infinite-volume result
   is bd `tns-7ut`.
4. **CONJECTURE / future work:** a packet-smeared infinite-volume trace bound
   controlling `k=Θ(1/N)` (bd `tns-7ut`).
5. **CONJECTURE / future work:** two hard magnons followed by a genuine three-magnon channel,
   because ML2 is input completeness, not three-body channel completeness.
   The exact missing statement is EXPLORATION ML4-3.
