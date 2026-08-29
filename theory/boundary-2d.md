# 2+1 boundary battery — perimeter, loops, 1-form charge, and angular softness

**Status:** finite exact algebra/ED boundary map; no infinite-volume or proof claim.  Negative gates are binding.

| battery item | verdict | decisive computed number | standing gate |
|---|---|---:|---|
| 1. perimeter vs volume | **DIFFERENT-STATEMENT** — D10 locality survives, but the endpoint constant becomes a perimeter bound | `6x3`, `w=2`: `||i[H,Q_W]||=3.000000=|dW|/2` | **W4-C1-PERIMETER** |
| 2. no kinks | **DIFFERENT-STATEMENT** — sharp-loop charge lifts signed area, not loop position or winding | block/stripe charges `(-4,-4)`, windings `((0,0),)` / `((0,1),(0,1))` | **W4-C2-LOOP-AREA** |
| 3. 1-form charges | **FAILS** for the naive D10 transplant; a multiplicative loop/endpoint identity replaces it | `||[H,W]||=0`, but `||[H,sum_e Z_e]||=8.000000`; cross rank `0` | **W4-C3-ONE-FORM** |
| 4. Goldstone counting | **FAILS** for a scalar 1D phase slope; the finite datum is angular and multichannel | x-soft contact slopes `(2.000000,0.000000)`; channel rank `9`, mixing `2/7` | **W4-C4-ANGULAR-PHASE** |
| 5. register trap | **HOLDS** — full-sector and highest-weight registers remain inequivalent in 2D | trap coincidence `0.00e+00`; cross-register error `0.133914` | **W4-C5-REGISTER** |

`DIFFERENT-STATEMENT` means that exact finite algebra survives only after
replacing the 1D object.  `FAILS` names the stated naive transplant, not the
2D replacement.  `HOLDS` in item 5 means that the registered obstruction
persists.

Whole battery:

```bash
python3 -O theory/checks/boundary_2d_check.py
```

The recorded run ends with `ALL 2+1 BOUNDARY GATES PASS`.

## 0. Common finite registers

Items 1, 2, 4, and 5 use the spin-`1/2` square-lattice permutation
ferromagnet

\[
 H={1\over2}\sum_{\langle xy\rangle}(1-P_{xy}),
 \qquad n_x={1\over2}-S_x^z,
\]

with periodic boundary conditions.  A bond with exactly one down spin has
diagonal matrix element `1/2` and swaps it with matrix element `-1/2`.
Consequently `N_\downarrow=\sum_xn_x` is exactly conserved.  The checker uses
full matrices where they are small and fixed-magnon blocks otherwise; no
continuum extrapolation is made.

Item 3 uses the `2x2` toric code with one qubit per edge,

\[
 H_{TC}=-\sum_v A_v-\sum_p B_p,
 \qquad A_v=\prod_{e\ni v}X_e,\quad B_p=\prod_{e\in\partial p}Z_e.
\]

All displayed norms are operator norms.  Every zero below is checked with
tolerance `2e-10`; the printed residual is the value obtained in the recorded
run.

## 1. Perimeter versus volume: DIFFERENT-STATEMENT

### Computed window

On the `6 x L_y` torus take the transverse-wrapping stripe
`W={0,...,w-1} x Z_{L_y}` and `Q_W=sum_{x in W} n_x`.  The exact D10 analogue
is

\[
 C_W:=i[H,Q_W]=\sum_{\langle xy\rangle:\,x\in W,y\notin W}j_{xy}.
\]

Every vertical bond has both ends in `W` or both outside, hence contributes
zero.  The remaining current is a tensor sum of `L_y` independently ED'd
six-site row currents.  Thus its exact 2D spectrum is the Minkowski sum of
the row spectra; no truncation of the `2^(6L_y)` Hilbert space is involved.

The gate prints

| stripe width `w` | 1D comparator `L_y=1` | `6x3` torus | crossing bonds `|dW|` |
|---:|---:|---:|---:|
| 1 | `0.707107` | `2.121320` | `6` |
| 2 | `1.000000` | `3.000000` | `6` |
| 3 | `1.000000` | `3.000000` | `6` |

The internal-bond conservation residual is `0.00e+00`.  For `w>=2` and
`6-w>=2` the two cuts in each row have disjoint support and

\[
 \|C_W\|={1\over2}|\partial W|=L_y.
\]

At `w=1` the two cut currents share the sole inside spin and the coefficient
is smaller, `||C_W||=L_y/sqrt(2)`, but it still grows linearly with the
transverse perimeter.  Hence the difference already bites on the smallest
nondegenerate torus in the battery, `L_y=3`; the sharp `|dW|/2` law bites once
the stripe and its complement are at least two sites wide.

**Finite statement.**  The algebraic support/telescoping estimate survives:
only bonds crossing `dW` occur, so the triangle bound is `O(|dW|)`.  What does
not survive is the 1D inference that a finite window produces an `O(1)`
boundary constant independent of transverse size.  For square windows this
is an `O(linear size)` term, not an `O(1)` term and not an `O(area)` term.

Reproduce:

```bash
python3 -O theory/checks/boundary_2d_check.py --gate W4-C1-PERIMETER
```

## 2. No kink coordinate: the charge is signed area

### Exact `4x4` sharp-loop identity

Use the all-up vacuum as reference and let `D` be the set of down spins in a
computational-basis configuration.  Then, on every one of the `2^16`
configurations,

\[
 Q_{rel}:=\sum_x(S_x^z-1/2)=-|D|.
\]

The maximum identity error is exactly `0`.  This is the literal 2D analogue
of the algebraic part of LD-ID: a window gives `-|D intersect W|`, and the
whole torus gives the signed area of the down-spin region.  It does not give
a coordinate of any component of `dD`.

Three configurations with the same charge isolate what is lost:

| down-spin domain | `Q_rel` | wall perimeter | dual-loop winding `(wx,wy)` |
|---|---:|---:|---|
| `2x2` block | `-4` | `8` | `((0,0),)` |
| one-column stripe | `-4` | `8` | `((0,1),(0,1))` |
| four isolated sites | `-4` | `16` | four contractible loops |

Thus the charge sees neither perimeter nor winding: even equal area and equal
perimeter do not distinguish a contractible loop from two noncontractible
loops.  Nearest-neighbour exchange changes total area by exactly `0` over all
allowed moves, while a move across the boundary of the half-torus window
changes the window area by `1`.

**Finite statement.**  In the sharp-domain register of a `U(1)`-conserving
ferromagnet, the conserved geometric datum is total signed area relative to a
chosen vacuum.  Individual loop position, shape, and winding are not lifted.
Window area is not conserved.  For quantum superpositions the statement is
only the diagonal charge/area operator identity; it does not manufacture a
sharp loop observable.  This is not a 2D version of D13(c)'s wall coordinate.

Reproduce:

```bash
python3 -O theory/checks/boundary_2d_check.py --gate W4-C2-LOOP-AREA
```

## 3. Toric-code 1-form charge: the D10 transplant FAILS

Take the noncontractible two-edge Wilson loop
`W_Z=product_{e in gamma} Z_e` on the `2x2` torus.  Exact ED gives

- `||[H_TC,W_Z]||=0.00e+00`;
- `rank(P_- W_Z P_+)=0`, where `P_+/-=(1+/-W_Z)/2`;
- for the additive would-be D10 charge `Q_gamma=sum_{e in gamma}Z_e`,
  `||[H_TC,Q_gamma]||=8.000000`;
- an open one-edge string has two endpoint stars, commutator norm `4.000000`,
  and exact endpoint residual `0.00e+00` in

  \[
  [H_{TC},W_Z(\gamma_{open})]
   =-2(A_{v_1}+A_{v_2})W_Z(\gamma_{open}).
  \]

The closed product is conserved by even anticommutation parity at every
vertex.  The corresponding sum of single-edge `Z_e` operators is not
conserved and its terms do not cancel as a D10 divergence.  Moreover the
`Z_2` 1-form symmetry is discrete: there is no infinitesimal on-site density
`q_x`, modulated charge `Q_k`, or complex-linear current zero mode to place in
the S-IDX-fin-G register.  The vanishing cross block confirms that the loop
generator itself is block diagonal in its own `+/-` sectors, not a ladder
between them.

**Binding negative.**  Replacing a D10 additive 0-form charge by a Wilson
loop does not produce a 2D current-zero-mode row.  What survives here is a
multiplicative closed-loop conservation law and a finite open-string endpoint
identity.  Any 1-form soft statement needs link/plaquette cochains and higher
currents as new definitions; D10 cannot be reused verbatim.

Reproduce:

```bash
python3 -O theory/checks/boundary_2d_check.py --gate W4-C3-ONE-FORM
```

## 4. Goldstone two-body data: scalar slope FAILS

### Directional contact equations

The 1D S2-2body contact equation R16, applied to an adjacency with normal
`mu in {x,y}`, would demand a coefficient `s_mu` satisfying

\[
 (2z_{h,\mu}-z_{s,\mu}z_{h,\mu}-1)s_\mu
 +(2z_{s,\mu}-z_{s,\mu}z_{h,\mu}-1)=0.
\]

In one dimension there is one such equation.  In two dimensions a single
two-plane-wave coefficient would have to solve both.  With
`k_h=(0.9,1.2)`, `k_s=epsilon n`, and the phase branch through `s_mu(0)=1`,
the five-point derivatives are

| approach direction `n` | `d_epsilon arg(s_x)` | `d_epsilon arg(s_y)` |
|---|---:|---:|
| `(1,0)` | `2.000000` | `0.000000` |
| `(0,1)` | `0.000000` | `2.000000` |
| `(1,1)/sqrt(2)` | `1.414214` | `1.414214` |
| `(1,-1)/sqrt(2)` | `1.414214` | `-1.414214` |

The numerical derivative error against the exact directional rule
`2 n_mu` is below `2e-9`.  Equality on the positive diagonal is accidental;
the axial and anti-diagonal spreads are `2` and `2sqrt(2)` respectively.

### Independent `4x4` ED multichannel witness

At total momentum `K=(pi,pi)`, every free two-magnon channel on the `4x4`
torus has energy `4`.  The ten symmetrised momentum-pair labels span a
rank-`9` hard-core channel space.  In normalized channel vectors `phi_a`, ED
gives

\[
 \max_{a\ne b}|\langle\phi_a,(H-4)\phi_b\rangle|
 ={2\over7}=0.285714,
\]

so contact scattering mixes angular channels.  The control
`Q_0|K=(pi,pi)>` remains an exact SU(2) descendant with energy `4`, residual
`2.45e-16`; the failure is at nonzero vector soft momentum, not at the global
charge zero mode.

**Binding negative.**  There is no well-defined scalar 2D analogue of
`partial_{k_s} delta_phys|_0` before choosing an approach direction and an
incoming/outgoing angular channel.  The candidate replacement is an angular
scattering kernel (or its eigenphase matrix) with directional derivatives in
the vector `k_s`.  D7--D8 and S2-2body currently define only a scalar ordered
channel, so a 2D soft-value corner does not exist in the present vocabulary.

Reproduce:

```bash
python3 -O theory/checks/boundary_2d_check.py --gate W4-C4-ANGULAR-PHASE
```

## 5. The register trap survives: HOLDS

The checker independently builds the horizontal current zero mode of the
`3x3` periodic XXX ferromagnet and works in the `n=2` sector.  The full source
sector has dimension `C(9,2)=36`; `ker S^+` has dimension `27`.  For the
deterministic state selected with seed `20260829`, putting
`D=S^-: H_2 -> H_3` gives

| quantity | ED value |
|---|---:|
| `||A_hw-5 I||`, `A_hw=(D Pi_hw)^dagger(D Pi_hw)` | `9.69e-15` |
| corrected full-register residual | `3.51e-16` |
| corrected highest-weight-register residual | `5.11e-16` |
| `||naive_hw(no Pi)-refuted_display||` | `0.00e+00` |
| full result versus highest-weight result | `0.133914` |
| refuted scalar display versus full result | `0.187479` |

This reproduces `ml4_ward_n2_check.py`'s trap literally: because
`A_hw=5 I`, reading the restricted scalar Gram operator in the full sector
and dropping `Pi_hw` gives the refuted display exactly.  Each corrected
formula is exact in its own register, but the two projected results differ by
`0.133914`.

**Finite statement.**  The full-sector/highest-weight distinction is
representation algebra and is insensitive to spatial dimension.  A 2D
current component satisfying the same SU(2) covariance inherits the same
trap; no scalar substitution across registers is allowed.

Reproduce:

```bash
python3 -O theory/checks/boundary_2d_check.py --gate W4-C5-REGISTER
```

## 6. Gates imposed on the 2+1 prover lanes

1. Replace every 1D `O(1)` window-boundary estimate by an explicit
   `O(|dW|)` estimate.  A volume-normalized statement must show how the
   perimeter/area ratio is taken to zero; this battery supplies no such
   limit theorem.
2. Do not call 2D relative charge a domain-wall coordinate.  In the sharp
   `U(1)` register it is signed area; it is blind to loop winding and shape,
   and only the full-system area is conserved.
3. Do not place a discrete 1-form Wilson loop in D10 or S-IDX-fin-G.  Use a
   separately defined cochain/higher-current register and retain the finite
   endpoint law.
4. Do not state a 2D scalar soft phase slope.  First define angular channels,
   a scattering matrix/kernel, its phase convention, and the directional
   `k_s` limit.
5. Retain the full-sector Gram inverse or explicitly insert the
   highest-weight projection.  The register fence is unchanged in 2D.

These are finite boundary statements only.  Passing the battery proves no
thermodynamic limit, no 2D scattering completeness, and no 2D soft theorem.
The nonzero perimeter, additive-loop, angular-splitting, and cross-register
numbers are unconditional falsifiers of the corresponding naive finite
transplants.
