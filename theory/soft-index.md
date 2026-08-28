<!-- ROLE: Lane-S1 proposer shard for S-INDEX.  Proposed D29/D30 text is in
     MERGE PROPOSALS.  Self-status: SKETCH until the L6 loop converges. -->

# S-INDEX — the charge-created soft law as a constraint on protocol limits

## 0. Statement

The labels **D29(PROTO)** and **D30(TGT)** mean exactly the proposals in §7;
they are not live definitions.  All older symbols retain their L4 sources.
The datum is the connected multiplier

\[
 \mathsf s_\lambda(k;h):=S^{\rm phys}_\lambda(k;h)-1,
 \qquad S^{\rm phys}_\lambda=1+\mathsf s_\lambda .           \tag{SIDX.1}
\]

Thus the Adler zero is `\mathsf s_*(0)=0`.  Since the argument of a function
with a linear zero is undefined at zero, the phase observable is necessarily

\[
 \left.\partial_k\arg(1+\mathsf s_*(k;h))\right|_{k=0},       \tag{SIDX.2}
\]

the D7/D25 convention.  No claim below uses `arg \mathsf s_*(0)`.

### THEOREM S-INDEX-spec

**ASSUME (H-SIDX).**

1. A periodic exhaustion of an `SU(2)` ferromagnetic vacuum sector has D10's
   conserved current, `Q_0=S^-`, positive real vacuum charge density `ρ`,
   and highest-weight hard packet spaces.  If their total `S^z` value is
   `m_\lambda`, then `m_\lambda/N_\lambda->ρ`.  No step assumes
   `ρ in (1/2)Z`.  D26(INT) holds, but its arithmetic is unused.
2. D29 supplies the finite ring/window/filter/packet datum and its exact
   descendant/orthogonal split.  Its measured hard Ward datum is
   `ℓ_\lambda(h)`, normalized so that the descendant current residue is
   `2iv_h ℓ_\lambda(h)` times the hard amplitude.  A primitive hard magnon
   has `ℓ_\lambda=1`.  The equality `ℓ_h=|q|` for a composite charge-`q`
   band is an additional checkable hypothesis, not a conclusion here.
3. D30 holds for the selected **actual** protocol limit point.  D30 assumes
   neither wave operators nor convergence of the full family.

**PROVE.**

- **(S-IDX.0-fin).**  In every finite highest-weight hard sector,

  \[
   D_\lambda^\dagger D_\lambda=2m_\lambda I,
   \qquad P_\lambda J^-_0={1\over m_\lambda}Q_0J^z_0.        \tag{SIDX.3}
  \]

  For D6 this is `P_{n,N}J^-_0=2Q_0J^z_0/(N-2n)`.  Pairing
  with the same descendant cancels that offset exactly.
- **(S-IDX.1-spec).**  Every D30 limit point with
  `ℓ_\lambda->ℓ_h` obeys

  \[
  \mathsf s_*(k;h)=i\,\operatorname{sgn}(v_h-v_s)
       {ℓ_h\over ρ}k+o(k),\qquad \mathsf s_*(0;h)=0,         \tag{SIDX.4}
  \]

  and

  \[
  \left.\partial_k\arg(1+\mathsf s_*)\right|_0
   =\operatorname{sgn}(v_h-v_s){ℓ_h\over ρ}.                \tag{SIDX.5}
  \]

  D30(4) makes this jet subsequence-independent without asserting a limit
  exists.  For a primitive leg `ℓ_h=1`; if separately
  `ℓ_h=|q|`, this is the advertised `sgn(v_h-v_s)|q|/ρ` law.
- **(S-IDX.2-source).**  In D24's D6 register, a source obeying both ML5-A
  zero conditions and its relative second-derivative bound uniformly along
  the protocol subsequence inherits (SIDX.4) with `M_1^O`.
- **(S-IDX.3-anchors).**  The result matches S2-2body, S2-2body-S, and, after
  additionally assuming fixed-packet wave operators and D30, the EXPLORATION
  box in `soft-current-recon.md` ⟨1⟩6.

Bound bands and extra channels are allowed.  They can remove or alter hard
data on a subsequence, but do not alter the law for a surviving limit point.

## 1. Finite-volume soft index (S-IDX.0)

### ⟨1⟩1. Exact Ward projection

**ASSUME.**  A finite H-SIDX ring and a highest-weight space
`K_\lambda \subset \ker S^+` with `S^z=m_\lambda I`, `m_\lambda>0`; put
`D_\lambda=Q_0|_{K_\lambda}=S^-|_{K_\lambda}`.

**PROVE.**  Equation (SIDX.3).

**⟨2⟩1.**  `D_\lambda^dagger D_\lambda=S^+S^-=2m_\lambda I` on
`K_\lambda`.

*Justification.*  `S^+g=0`, `[S^+,S^-]=2S^z`, and named representation
computation **SIDX-W1**; this is proved claim ML4-Ward (9) for D6.

**⟨2⟩2.**  `D_\lambda^dagger J^-_0=2J^z_0+J^-_0S^+`.

*Justification.*  `[S^+,J^-_0]=2J^z_0` for the `SU(2)` vector current; proved
claim ML4-Ward (8), from D10 and the invariant bond current.

**⟨2⟩3.**  With
`P_\lambda=D_\lambda(D_\lambda^dagger D_\lambda)^{-1}
D_\lambda^dagger`, substitution of ⟨2⟩1--⟨2⟩2 gives (SIDX.3).

*Justification.*  The range-projection computation of ML4-Ward (9)--(10).

**⟨2⟩4. QED.**

### ⟨1⟩2. The offsets cancel before the density normalization

**ASSUME.**  The hypotheses of ⟨1⟩1.

**PROVE.**  The `N-2n`, `N-2`, and `2ρ` factors enter as follows.

**⟨2⟩1.**  In D6's spin-`1/2` `n`-magnon sector,

\[
 m_{n,N}=N/2-n,\qquad D_{n,N}^\dagger D_{n,N}=N-2n,\qquad
 P_{n,N}J^-_0={2Q_0J^z_0\over N-2n}.                         \tag{SIDX.6}
\]

*Justification.*  D6 sector arithmetic and ML4-Ward (9), including
`n<N/2`.

**⟨2⟩2.**  For one nonzero hard momentum,

\[
 \|Q_0|h\rangle_N\|^2=N-2,\qquad
 P_{1,N}J^-_0|h\rangle_N={2iv_h\over N-2}Q_0|h\rangle_N,
                                                                    \tag{SIDX.7}
\]

so

\[
 \langle h|Q_0^\dagger P_{1,N}J^-_0|h\rangle_N=2iv_h.       \tag{SIDX.8}
\]

*Justification.*  `soft-current-recon.md` (R3), (R14)--(R15), equivalently
ML4-Ward (11).  Multiplication by the descendant norm `N-2` proves the last
line; named computation **SIDX-OFFSET**.

**⟨2⟩3.**  More generally, on a hard packet the normalized descendant residue
is `2iv_h ℓ_\lambda(h)`.  The charge-created vacuum leg has density norm

\[
 {1\over N}\|Q_0|Ω\rangle\|^2=2ρ .                          \tag{SIDX.9}
\]

*Justification.*  The first statement defines D29's measured Ward datum and
reduces to (SIDX.8) for a primitive magnon.  For the second,
`S^+S^-|Ω>=2S^z|Ω>` and
`<Ω|S^z|Ω>/N=ρ`; named computation **SIDX-LEGNORM**.
For every primitive spin-`S` magnon, the direct D10 bond computation
`J^z_0|h>=iv_S(h)|h>` gives `ℓ_\lambda=1` (**SIDX-W2**; its spin-`1/2`
case is the computation in R14).

**⟨2⟩4.**  D29's canonical flux factor
`L_\lambda(0,h)=-i sgn(v_h-v_s)/(2ρ_\lambda v_h)` therefore gives

\[
 (e^{ik}-1)L_\lambda(0,h)[2iv_h ℓ_\lambda(h)]
 =i\,\operatorname{sgn}(v_h-v_s){ℓ_\lambda(h)\over ρ_\lambda}k
  +O(k^2).                                                    \tag{SIDX.10}
\]

*Justification.*  `e^{ik}-1=ik+O(k^2)` and the exact cancellations above;
named computation **SIDX-FLUX**.  For spin `1/2`, `ρ=1/2`, giving `2`; for
the fully polarized spin-`S` family, `ρ=S`, giving `1/S`.

**⟨2⟩5. QED.**

### ⟨1⟩3. Charge and contact terms stay separate

**ASSUME.**  D6 and one hard magnon.

**PROVE.**

\[
 J^-_k|h\rangle_N=
 \underbrace{{\omega(k)\over e^{ik}-1}Q_k|h\rangle_N}_{\rm charge}
 +\underbrace{{J\over\sqrt N}(e^{ih}-1)|C_{h+k}\rangle}_{\rm contact},
 \quad {\omega(k)\over e^{ik}-1}={J\over2}(e^{-ik}-1).       \tag{SIDX.11}
\]

**⟨2⟩1.**  The charge coefficient vanishes at `k=0`, while the contact vector
is generally nonzero there and has the descendant projection (SIDX.7) plus a
nonzero orthogonal complement.

*Justification.*  Exact identities (R10), (R13)--(R15) in
`soft-current-recon.md`; claims S2-2body and ML4-Ward.

**⟨2⟩2.**  Hence neither `e^{ik}-1` nor the Ward projection alone proves an
Adler zero.

*Justification.*  ⟨2⟩1 and REFUTED claim G0-soft-r1.

**⟨2⟩3. QED.**

(S-IDX.0) used no wave operators, completeness, integrability, soft
expansion, or D26(INT).

## 2. The TGT cancellation lemma

### ⟨1⟩4. LEMMA SIDX-TGT

**ASSUME.**  Fix an outer protocol limit point before varying `k`.  D30 gives
`Gamma_*(0)=U_*`,
`||Gamma_*(k)-U_*||_tr<=C_Gamma|k|`, and
`R_*(k)=(1-U_*U_*^dagger)J_*(k)`, with
`||J_*(k)-J_*(0)||_tr<=C_J|k|`.

**PROVE.**

\[
 \|(e^{ik}-1)\Gamma_*(k)^\dagger R_*(k)\|_{tr}
 \le[C_\Gamma\|J_*(0)\|+C_J\sup_k\|\Gamma_*(k)\|]|k|^2. \tag{SIDX.12}
\]

**⟨2⟩1.**  `U_*^dagger R_*(0)=0`, so
`Gamma_*(k)^dagger R_*(0)=[Gamma_*(k)-Gamma_*(0)]^dagger R_*(0)`.

*Justification.*  The definition of `R_*`, `U_*^dagger U_*=I`, and ML4-A
⟨2⟩1--⟨2⟩2.

**⟨2⟩2.**  Split `R_*(k)=R_*(0)+[R_*(k)-R_*(0)]`, apply D30's two `C^1`
bounds, and multiply by `|e^{ik}-1|<=|k|` to obtain (SIDX.12).

*Justification.*  Submultiplicativity, `||1-U_*U_*^dagger||=1`, and proved
claim ML4-A (5), used in its allowed limit-trace register.

**⟨2⟩3. QED.**  No uniform derivative of `Gamma_N` was assumed.

## 3. Subsequential soft law (S-IDX.1)

### ⟨1⟩5. Ordered-limit proof

**ASSUME.**  H-SIDX and one D30-admissible limit point `\mathsf s_*`.

**PROVE.**  Equations (SIDX.4)--(SIDX.5).

**⟨2⟩1.**  Its descendant part is

`\mathsf s_*^\parallel(k)=i sgn(v_h-v_s)(ℓ_h/ρ)k+O(k^2)`.

*Justification.*  D29's exact split, (SIDX.8)--(SIDX.10), and D30(2)--(3);
named computation **SIDX-JET**.  No derivative crosses an outer limit.

**⟨2⟩2.**  Its orthogonal part is `O(k^2)` in the D24(b) norm.

*Justification.*  D29 contains no arbitrary-source contact term and
(SIDX.12) controls the exhaustive remaining component.

**⟨2⟩3.**  Adding the components proves (SIDX.4).  The zero uses both

\[
 \underbrace{\omega(k)/(e^{ik}-1)}_{O(k)}Q_k,
 \qquad \underbrace{\Gamma_*(k)^\dagger(1-P_*)J_*}_{O(k)},  \tag{SIDX.13}
\]

the latter accompanied by `e^{ik}-1`.

*Justification.*  (SIDX.11)--(SIDX.12); this is the current/contact
cancellation, not G0-soft-r1's bare-factor inference.

**⟨2⟩4.**  Taking the imaginary part of
`log(1+\mathsf s_*)=i sgn(v_h-v_s)(ℓ_h/ρ)k+o(k)` proves
(SIDX.5).

*Justification.*  (SIDX.4) and D7's continuous physical phase branch.

**⟨2⟩5.**  The derivative is strictly last:

\[
 \boxed{k\to0\;\text{after}\;ς\downarrow0\;\text{after}\;
 σ\downarrow0\;\text{after}\;W\uparrow\mathbb Z\;\text{after}\;
 T\to\infty\;\text{after}\;N\to\infty}.                    \tag{SIDX.14}
\]

*Justification.*  D29(6) and D30(1).

**⟨2⟩6.**  The ML4-Q1 sequence is excluded in one line:

\[
 \boxed{\lim_{k\to0}\lim_{ς}\lim_{σ}\lim_W\lim_T\lim_N
 \ne\lim_{N\to\infty}[\,\cdot\,]_{k=2\pi/N};\quad
 k\text{ is fixed while }N\to\infty .}                     \tag{SIDX.15}
\]

*Justification.*  D29(6); named countercomputation ML4-Q1 applies to the
right-hand joint finite-ring interpolation only.

**⟨2⟩7.**  D30(4) makes the coefficient common to all component cluster
points but makes no sequence converge.

*Justification.*  (SIDX.4) contains only D30's common `ρ`, `ℓ_h`, and
orientation, mirroring D27's convenience-clause discipline.

**⟨2⟩8. QED.**

### ⟨1⟩6. Vacuous-truth fence

**ASSUME.**  The theorem setting.

**PROVE.**  Its nonvacuous and conditional parts are explicit.

**⟨2⟩1.**  (S-IDX.0) has instances on every D6 ring with `N>3`, every
`n<N/2`, and every highest-weight packet; S2-2body and S2-2body-S give exact
stationary multiplier instances on compact regular hard domains.

*Justification.*  D6, ML4-Ward, and the two PROVED anchor claims.

**⟨2⟩2.**  If another model has no D30-admissible limit point, (S-IDX.1) has
no instance there.

*Justification.*  ML1, ML3, and ML6 remain CONJECTURE; D30 is a closure
property, not an existence hypothesis.

**⟨2⟩3. QED.**

## 4. Source bridge (S-IDX.2)

### ⟨1⟩7. COROLLARY SIDX-source

**ASSUME.**  D6--D8 and a D24(a) source `O`.  Along the selected protocol
subsequence assume

\[
 M_{2,j}^O(0)=0,
 \quad \mathfrak c_{h,j}(O)=0,
 \quad \sup_j{K_{O,j}(\epsilon_0)\over\|M_{1,j}^O\|_{L^2(I)}}<\infty,    \tag{SIDX.16}
\]

with nonzero denominators.

**PROVE.**

\[
 M_2^O(k,h)=2i\operatorname{sgn}(v_h-v_s)kM_1^O(h)
             +O_{L^2(I)}(k^2).                              \tag{SIDX.17}
\]

**⟨2⟩1.**  ML5-A and D24(c) give (SIDX.17) at every regulator with a
subsequence-independent relative constant, and the estimate passes to each
D30 limit point.

*Justification.*  Proved claim ML5-A, Banach-space Taylor remainder, and the
third condition in (SIDX.16).

**⟨2⟩2.**  `O_eta` and `V_int` are excluded respectively by the nonzero first
jet and nonzero intercept.

*Justification.*  D24(e) and REFUTED claim ML5.

**⟨2⟩3. QED.**  This bridge is only D24's frozen spin-`1/2` criterion; no
generalized source theorem is implied.

## 5. Consistency anchors (S-IDX.3)

### ⟨1⟩8. Exact two-body anchors

**ASSUME.**  The indicated exact regular channel.

**PROVE.**  Both anchors match.

**⟨2⟩1.**  On D6--D8, `ρ=1/2`, `ℓ_h=1`, and the sign is `+1`; hence
(SIDX.4) is `\mathsf s_*=2ik+o(k)`.  More exactly,

`S_phys-1=2ik+[i cot(h/2)-2]k^2+O_I(k^3)` and
`arg S_phys=2k+cot(h/2)k^2+O_I(k^3)`.

*Justification.*  D8, (R17)--(R18), and PROVED claim S2-2body.

**⟨2⟩2.**  In the fully polarized spin-`S` family, `ρ=S` and
`ℓ_h=1`; (SIDX.5) is `sgn(v_h-v_s)/S`, hence `1/S` on D8.

*Justification.*  PROVED claim S2-2body-S (T.3)--(T.4) and
**SIDX-LEGNORM**.

**⟨2⟩3. QED.**

### ⟨1⟩9. Value-computation corollary

**ASSUME.**  Additionally assume ML1's fixed-packet wave operators for the
selected real channel and D30's soft closure.

**PROVE.**  On D6,

\[
 M_2(k,h)=2ikM_1(h)+R_{S2}(k,h),
 \quad \|R_{S2}(k)\|_{L^2(I)}\le C_Ik^2\|M_1\|_{L^2(I)},    \tag{SIDX.18}
\]

the EXPLORATION box of `soft-current-recon.md` ⟨1⟩6.

**⟨2⟩1.**  ML1 supplies fixed-packet in/out values; D30, not ML1, supplies
soft trace regularity; (SIDX.10) and (SIDX.12) give the leading and remainder
terms.

*Justification.*  Claims ML1 and ML4-A, and the ML3/ML6 scope in
`soft-current-recon.md` ⟨1⟩7.

**⟨2⟩2. QED.**  ML1 alone is not claimed to imply D30.

## 6. CHECKER SPEC

### ⟨1⟩10. SIDX-C1/C2

**ASSUME.**  A future writable checker lane.

**PROVE (machine-checkable specification).**

1. For D6 rings `N in {8,10,12,14,16}` and `n in {1,2}`, assemble sector
   matrices from `(J/2)(1-P)`.  Require, without `assert`, operator residuals
   below `1e-12` for (SIDX.6), and below `1e-12` for (SIDX.7)--(SIDX.8) at
   every nonzero hard ring momentum in `[pi/4,3pi/4]`.
2. Assemble both terms of (SIDX.11); require their sum to match `J^-_k|h>`
   below `1e-12` and require a `k=0` orthogonal-contact norm above `1e-6` for
   one hard momentum.  Mutating `N-2n` to `N`, or deleting the contact term,
   must exit nonzero.
3. At `h=2pi/5` and `N` divisible by five, reproduce ML4-Q1's raw
   `k=2pi/N` growth while the fixed-window normalized D29 packet datum stays
   bounded as `N->infinity`.  A mutation exchanging the limits in
   (SIDX.15) must exit nonzero.

*Justification.*  Expected values are ML4-Ward (8)--(11), R10, and named
computation ML4-Q1.  The mutations hit the offset, contact, and limit-order
steps.

**⟨2⟩1. QED.**

## 7. MERGE PROPOSALS

### 7.1 Exact replacement text for `definitions.md` (append D29--D30)

> ## D29 (PROTO: finite charge-created soft-leg datum)
>
> 1. Fix D10's complexified broken charge/current, `I=[a,b]\Subset(0,\pi)`, normalized `\eta,f\in C_c^\infty` with `\int\eta=1` and `\|f\|_2=1`, and regulators `\lambda=(N,W,T,\sigma,\varsigma)`: periodic ring, seam-separated finite window, on-shell filter, hard-packet width, and soft-resolution width.  The hard packet has carrier `h\in I` and width `\sigma`.  The finite filter is `\Pi_{N,T}(E)=\int T^{-1}\eta(t/T)e^{it(H_N-E)}dt`.  Window-local preparation/resolution matrices, followed by `\Pi_{N,T}` and the momentum filters, give `L^2(I)` connected pairings `M_{1,\lambda}^{(h)}` and `M_{2,\lambda}^{(h)}(k)` in D24(b)'s norm.  No wave operator or completeness is presupposed.
>
> 2. The only soft insertion is `Q_W[f_{k,\varsigma}]=\sum_{x\in W}\widehat f_{k,\varsigma}(x)q_x^-`, with `f_{k,\varsigma}(p)=\varsigma^{-1/2}f((p-k)/\varsigma)`.  It is local for finite `W`; the continuous carrier is used only inside this packet.  D10's exact summation by parts, including both boundary gradients of the truncated profile, defines its current-reduced pairing; no boundary term is dropped.
>
> 3. Put `\mathsf s_\lambda(k;h)=\langle M_{1,\lambda}^{(h)},M_{2,\lambda}^{(h)}(k)\rangle_{L^2(I)}/\|M_{1,\lambda}^{(h)}\|_{L^2(I)}^2` when the denominator is nonzero, and `S_\lambda^{phys}=1+\mathsf s_\lambda`.  This norm projection, not pointwise division, is the multiplier normalization.
>
> 4. On a finite highest-weight hard space set `D_\lambda=Q_0`, `P_\lambda=D_\lambda(D_\lambda^\dagger D_\lambda)^{-1}D_\lambda^\dagger`, and `R_\lambda(k)=(1-P_\lambda)J^-_k`.  The finite preparation/resolution maps determine `\Gamma_\lambda(k)`.  The pairing is, by definition of PROTO, the exact sum of its descendant and `R_\lambda(k)` components; there is no arbitrary direct soft-source contact.  Separately record both R10 terms `J^-_k=[\omega(k)/(e^{ik}-1)]Q_k+C_k`.
>
> 5. Let `\rho_\lambda` be fixed by `N^{-1}\|Q_0|\Omega\rangle\|^2=2\rho_\lambda`, and let the real `\ell_\lambda(h)` satisfy: the descendant residue is `2iv_h\ell_\lambda(h)M_{1,\lambda}^{(h)}`.  Normalizing the Goldstone leg by this `2\rho_\lambda` norm fixes, independently of the hard process, `L_\lambda(0,h)=-i\operatorname{sgn}(v_h-v_s)/(2\rho_\lambda v_h)`.  PROTO records, rather than assumes, whether a composite band has `\ell=|q|`.
>
> 6. Limits are ordered: `N\to\infty` at fixed other regulators; then `T\to\infty`; then `W\uparrow\mathbb Z`; then `\sigma\to0`; then `\varsigma\to0` at fixed nonzero carrier `k`; and `k\to0` strictly last.  The joint ring sequence `k=2\pi/N` is not a PROTO limit.  Every finite-regulator datum is a computable finite matrix.
>
> ## D30 (TGT: matched-jet tightness)
>
> Fix D29.  TGT is a closure property and asserts no limit-point existence.
>
> 1. Whenever `\mathsf s_\lambda` has a D24(b)-topology limit point on a punctured soft neighborhood, its nonzero hard denominators and component data have a further cluster point on the same subsequence.
> 2. Every component cluster point obeys `\rho_\lambda\to\rho>0`, `\ell_\lambda\to\ell_h`, and has a `C^1` limiting external flux with D29(5)'s value at zero.
> 3. Every component cluster point has an isometry `U_*`, channel trace `\Gamma_*(k)`, and reduced current `R_*(k)=(1-U_*U_*^\dagger)J_*(k)`, with `\Gamma_*(0)=U_*`, `\|\Gamma_*(k)-U_*\|_{tr}\le C_\Gamma|k|`, and `\|J_*(k)-J_*(0)\|_{tr}\le C_J|k|`.  This is imposed only after all D29 outer limits; no volume-uniform fixed-ring interpolation bound is assumed.
> 4. Optional convenience clause: `\rho`, `\ell_h`, and `\operatorname{sgn}(v_h-v_s)` are common to all component cluster points.  It buys uniqueness of the first jet, not existence or uniqueness of a multiplier limit.

### 7.2 Exact rows for `claims/CLAIMS.md`

> | S-INDEX-fin | Finite highest-weight identity `D^\dagger D=2mI`, `PJ^-_0=Q_0J^z_0/m`; the `N-2n` offset cancels against the descendant norm, leaving Ward residue `2iv_h\ell_h` before the `2\rho` soft-leg normalization. | SKETCH | D10, ML4-Ward, D29 | theory/soft-index.md ⟨1⟩1--⟨1⟩3 | SIDX-C1 |
> | S-INDEX-spec | Under H-SIDX, D29, and D30, every actual ordered limit point obeys `\mathsf s_*=i\operatorname{sgn}(v_h-v_s)(\ell_h/\rho)k+o(k)` and `\partial_k\arg(1+\mathsf s_*)|_0=\operatorname{sgn}(v_h-v_s)\ell_h/\rho`; no existence, unrestricted sources, or composite `\ell=|q|` is claimed. | SKETCH | S-INDEX-fin, D24, D25, D30, ML4-A | theory/soft-index.md ⟨1⟩4--⟨1⟩6 | SIDX-C1,C2 |
> | S-INDEX-source | D6/D24 sources obeying both ML5-A zeros and a subsequence-uniform relative remainder inherit S-INDEX; unrestricted ML5 remains refuted. | SKETCH | S-INDEX-spec, ML5-A | theory/soft-index.md ⟨1⟩7 | D24(e) negative controls |

### 7.3 Exact rows for `notation.md`

> | `\mathsf s_\lambda`, `S_\lambda^{phys}` | D29 connected protocol multiplier and physical multiplier `1+\mathsf s_\lambda`; the phase belongs to the latter | proposed D29 |
> | `\lambda=(N,W,T,\sigma,\varsigma)` | D29 ring, window, on-shell, hard-width, and soft-resolution regulators | proposed D29 |
> | `\rho_\lambda`, `\ell_\lambda` | soft-leg density and measured hard Ward datum; no half-integrality or composite `\ell=|q|` is assumed | proposed D29--D30 |

## 8. HONEST STATUS

1. (SIDX.3) and the `N-2n -> N-2 -> 2ρ` cancellation are unconditional.
   D29+D30 imply the full limit-point jet, but D30's ordered infinite-volume
   matching/regularity is assumed, not proved; ML1/ML3/ML6 remain open.
2. The target's `partial arg \mathsf s_*` was replaced by the defined physical
   quantity `partial arg(1+\mathsf s_*)`.  The `|q|>1` factor was weakened to
   the measured datum `ℓ_h`; asserting more would contradict open claim Bc.
3. ML5's `O_eta` counterexample survives.  The source bridge is only ML5-A in
   D24's frozen register.  R10's two terms remain separate, and ML4-Q1's
   `k=2pi/N` order is explicitly excluded.
4. `ρ` is a free positive real density; D26(INT) and M-IDX-density are not
   used.  Overall L5 self-status: **SKETCH** pending independent criticism.
