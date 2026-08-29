# General-`G` soft index, strategy G5 — boundary map and falsifier

**Status:** finite ED boundary map; no proof claim. Negative gates are binding.

| battery item | finding | decisive computed number | gate |
|---|---|---:|---|
| 1. `G=U(1)^k` | **DEGENERATE** — the root-indexed statement is empty; a broken orbit is different | charge-created rank `0`; broken-`U(1)` tangent norm `0.866025` | **G5-C1-ABELIAN** |
| 2. finite groups | **DIFFERENT-STATEMENT** — string endpoints replace a current zero mode | `rank(P_-U_gP_+)=0`; endpoint residual `0.00e+00` | **G5-C2-FINITE** |
| 3. `SO(3)`/`SU(2)` and `O(2)` | **DIFFERENT-STATEMENT** — global form changes allowed sectors or pairs them, not the local Lie identity | centres `(+I,-I)` to `(7.35e-16,3.67e-16)`; `O(2)` paired-spectrum error `8.88e-16` | **G5-C3-GLOBAL-FORM** |
| 4. `SU(3)→SU(2)×U(1)` | **FAILS** for the naive scalar per-root rule; matrix Gram inverse survives | scalar error `6.155367` (relative `1.685717`); exact error `1.42e-15` | **G5-C4-SU3-H-MULT** |
| 5. rank-two register trap | **FAILS** — full and highest-weight registers are not interchangeable | `spec A_full={1×5,4×4,9×1}`; cross error `2.051789` | **G5-C5-SU3-REGISTER** |

`DEGENERATE` means there is no root/ladder row to evaluate.  `DIFFERENT-STATEMENT`
means the computed finite replacement is group-valued rather than a Lie-algebra
soft identity.  `FAILS` names a falsified generalization, not a failure of the
matrix Gram-inverse formula.

Whole battery:

```bash
python3 -O theory/checks/soft_index_g_boundary_check.py
```

The recorded run ends with `ALL GENERAL-G BOUNDARY GATES PASS`.

## 0. Common finite register

For the Lie-algebra tests, the checker uses the current convention

\[
 J_X=-\sum_x[h_x,X_x].
\]

For a root `β`, `D_β=Q_{-β}|_{\mathcal H_\mu}`,
`A_β=D_β^\dagger D_β`, and
`P_β=D_βA_β^{-1}D_β^\dagger`.  With Chevalley normalization
`[Q_β,J_{-β}]=J_{H_β}`, the three finite expressions tested below are

\[
\begin{aligned}
 \text{full:}&\quad P_βJ_{-β}\psi=D_βA_β^{-1}J_{H_β}\psi,\\
 \text{restricted:}&\quad
 P_{β,\mathrm{hw}}J_{-β}\psi
 =D_{β,\mathrm{hw}}A_{β,\mathrm{hw}}^{-1}
   \Pi_{\mathrm{hw}}J_{H_β}\psi,\\
 \text{naive scalar:}&\quad
 P_βJ_{-β}\psi\stackrel{?}{=}h_β^{-1}D_βJ_{H_β}\psi,
 \qquad h_β=\mu(H_β).
\end{aligned}
\]

The last line is the registered falsification target.  It silently combines
the full-sector projection on the left with the scalar Gram operator from the
highest-weight domain on the right.

## 1. Abelian `G=U(1)^k`: DEGENERATE

### Computed model

The finite witness is the `N=3`, `d=3` periodic permutation chain
`H=Σ_x(I-P_{x,x+1})`, viewed only with its `U(1)^2` Cartan symmetry.  The
on-site generators are

\[
 H_1=\operatorname{diag}(1,-1,0),\qquad
 H_2=\operatorname{diag}(0,1,-1).
\]

On the product vacuum `|0,0,0⟩`, both global charges are vacuum-normal-ordered.
The comparison states are the two normalized one-colour waves at
`k=2π/3`.

### ED output and finite finding

`G5-C1-ABELIAN` measures

- `||[H_1,H_2]||_max = 0.00e+00` and
  `max_a ||[H,Q_a]||_max = 0.00e+00`;
- `rank{(Q_a-⟨Q_a⟩)|Ω⟩}_{a=1,2}=0`;
- maximum overlap with either normalized one-colour wave `0.00e+00`;
- distance of either wave from the charge-created zero subspace `1.000000`.

A second finite comparator keeps only `U(1)_z` of the `N=3` spin-`1/2`
permutation ferromagnet and chooses the exact equatorial product ground state
`|+x⟩^{⊗3}`.  Here the vacuum-normal-ordered orbit tangent
`(Q_z-⟨Q_z⟩)|+x⟩^{⊗3}` has norm `√3/2=0.866025`, is orthogonal to the vacuum,
and has energy residual `0.00e+00`.

Thus this root-indexed finite identity has **no rows** for the abelian algebra:
there is no `Q_{-β}`, no target weight sector, and no `A_β` to invert.  Calling
that a nonzero soft identity would add structure not present in the computed
model.  The correct boundary entry is **empty/degenerate**, not “a scalar
formula that happens to equal zero.”  The second computation also rules out
the opposite overstatement that a broken abelian charge does nothing: it makes
a nonzero zero-mode orbit tangent.  That tangent requires a genuinely different
finite statement because the Cartan generator does not shift a weight sector.

Reproduce only this item:

```bash
python3 -O theory/checks/soft_index_g_boundary_check.py --gate G5-C1-ABELIAN
```

## 2. Finite groups: DIFFERENT-STATEMENT

### Computed model

The checker constructs the exact `N=4` transverse-field Ising ring

\[
 H=-\sum_x Z_xZ_{x+1}-0.37\sum_xX_x,
 \qquad U_g=X^{\otimes4},
\]

with `Z_2` charge projectors `P_±=(I±U_g)/2`.  The direct analogue of a
charge-lowering map would have to contain the cross-sector block
`D=P_-U_gP_+`.

### ED output and finite finding

`G5-C2-FINITE` gives

- `||[H,U_g]||_max=0.00e+00`;
- `rank D=0` and `||D^†D||_F=0.00e+00`, so the Gram inverse required by the
  soft-index formula does not exist;
- for the finite string `U_R=X_1X_2`,

  \[
  U_R^\dagger H U_R-H=2(Z_0Z_1+Z_2Z_3)
  \]

  with maximum-entry residual `0.00e+00`.

The group element is block diagonal in discrete charge and cannot be a ladder
between `P_+` and `P_-`.  What survives is the exact **finite-string endpoint
identity** displayed above.  It is the finite-group replacement for this
model; it has no infinitesimal `J^z_0`, no root-soft momentum row, and no
finite soft index of the SU(2) form.

Reproduce only this item:

```bash
python3 -O theory/checks/soft_index_g_boundary_check.py --gate G5-C2-FINITE
```

## 3. Global form: `SO(3)` versus `SU(2)`, and disconnected `O(2)`

### `SO(3)`/`SU(2)` centre and sector lattice

Two `N=3` periodic Heisenberg chains are diagonalized.  The first has on-site
spin `1`, so its action factors through `SO(3)`.  The second is the
`SU(2)`-only spin-`1/2` comparator.  State degeneracies in the total-Casimir
sectors are

| on-site representation | ED total-spin content | lifted `2π` centre |
|---|---|---|
| spin `1` (`SO(3)`) | `{J=0:1, J=1:9, J=2:10, J=3:7}` | `+I`, error `7.35e-16` |
| spin `1/2` (`SU(2)` only) | `{J=1/2:4, J=3/2:4}` | `-I`, error `3.67e-16` |

The maximum commutator of either Hamiltonian with its total Casimir is
`1.78e-15`.  On a **fixed** physical spin-1 chain, passing to the `SU(2)` lift
does not create half-integer sectors: the centre remains trivial.  The sector
lattice changes only when the allowed on-site/global representation is changed
to an `SU(2)`-only one.  Hence a root identity using only `su(2)` matrices is
blind to `π_1`; the global form enters as an admissible-sector fence.

### Disconnected `O(2)`

The comparator is an `N=3` spin-1 anisotropic ring with `U(1)` charge
`Q=Σ_xS_x^z` and reflection `F` swapping local `m=+1` and `m=-1`.  ED gives

- maximum `U(1)`/reflection symmetry residual `0.00e+00`;
- `||FQF+Q||_max=0.00e+00`;
- maximum mismatch between the spectra in every `Q=m` and `Q=-m` pair
  `8.88e-16`.

The identity component has the one-dimensional abelian Lie algebra already
covered by item 1.  The disconnected component is visible through the
finite transformation `F` and its exact `m↔-m` pairing, but not through a
derivative at the identity.  This is again a **different statement**, not a
modified local root coefficient.

Reproduce both global-form tests:

```bash
python3 -O theory/checks/soft_index_g_boundary_check.py --gate G5-C3-GLOBAL-FORM
```

## 4. Central experiment: `SU(3)` broken to nonabelian `H`

### Model and registered state

The model is the `N=5` fundamental-qutrit permutation ferromagnet

\[
 H=\sum_x(I-P_{x,x+1}),\qquad |Ω⟩=|1⟩^{\otimes5}.
\]

The stabilizer is globally `U(2)≅(SU(2)×U(1))/Z_2`, with Lie algebra
`su(2)⊕u(1)` acting on colours `2,3`.  ED checks the full `SU(3)` symmetry at
`0.00e+00`; the largest vacuum tangent from the unbroken `su(2)` generators is
`0.00e+00`, whereas each broken tangent `Q_{21}|Ω⟩` and `Q_{31}|Ω⟩` has norm
`√5=2.236068`.

The source sector has colour counts `(n_1,n_2,n_3)=(3,2,0)`, dimension `10`.
Its simultaneous kernel of `Q_{12},Q_{13},Q_{23}` has dimension `5`: this is
the nontrivial highest-weight multiplicity register.  The witness is the exact
momentum `k=-4π/5`, energy `1.763932` state in that register.  Its
highest-weight error is `3.41e-16` and energy-eigenvector residual is
`5.15e-16`.

### Per-root result

For the broken root `α_{12}` (`D=Q_{21}`, `h_{12}=n_1-n_2=1`):

- the full Gram-inverse identity has error `1.42e-15`;
- the naive scalar replacement has absolute error `6.155367`, relative to the
  projected left side by `1.685717`;
- the Cartan current compressed to the five-dimensional multiplicity register
  differs from its best scalar multiple by Frobenius norm `6.666667`.

For the second broken root `α_{13}` (`D=Q_{31}`, `h_{13}=3`), both the full
identity and scalar expression happen to agree to `1.93e-16`.  The two roots
therefore provide an internal negative/control pair in the same Hamiltonian,
vacuum, and exact hard eigenstate.

**Binding negative.**  A general-`G` theorem which replaces `A_β^{-1}` by the
scalar `1/h_β` in the full sector is false already for this `SU(3)` chain.  The
nonabelian stabilizer does not collapse the multiplicity-space current action
to a scalar.  The finite matrix Gram-inverse formula survives this experiment;
the scalar per-root formula does not.

Reproduce the central experiment:

```bash
python3 -O theory/checks/soft_index_g_boundary_check.py --gate G5-C4-SU3-H-MULT
```

## 5. Rank-two register trap

The same `α_{12}` witness isolates the exact analogue of the SU(2) register
trap.  On the full ten-dimensional weight sector,

\[
 \operatorname{spec}(A_{\rm full})
 =\{1\ (5\text{ times}),\ 4\ (4\text{ times}),\ 9\ (1\text{ time})\},
\]

and `||A_full-I||_F=10.000000`.  On the separately restricted
five-dimensional highest-weight domain,
`||A_hw-I||_F=1.38e-15`.  Nevertheless the Cartan current does not stay in
that domain:

\[
 ||(I-\Pi_{\rm hw})J_{H_{12}}\psi||=4.103578.
\]

The three decisive residuals are

| expression | residual |
|---|---:|
| corrected full-sector Gram inverse | `1.42e-15` |
| corrected highest-weight form with `Π_hw` | `1.40e-15` |
| naive scalar substitution in the full expression | `6.155367` |

The full projected result and the restricted projected result themselves
differ by `2.051789`.  They are both exact in their own codomains, but they are
not interchangeable.

**Binding negative.**  Rank two reproduces the register trap, now with a
nontrivial five-dimensional highest-weight multiplicity.  Any proposed
generalization must keep `A_β^{-1}` as an operator on the full weight sector,
or explicitly change register and insert `Π_hw` before using the scalar root
weight.  A bare substitution `A_β→h_β I` across those registers is killed by
this gate.

Reproduce the rank-two certificate:

```bash
python3 -O theory/checks/soft_index_g_boundary_check.py --gate G5-C5-SU3-REGISTER
```

## 6. Boundary map for the prover lanes

The battery leaves only the following finite target alive:

1. Work in the identity component of a compact Lie group and choose an actual
   root ladder.  Abelian factors contribute conserved Cartan Ward identities,
   but no rows to this root-indexed index.
2. In a positive root-weight sector, retain the full operator
   `A_β=D_β^†D_β` and its inverse.  Do not replace it by a weight scalar.
3. If a highest-weight-restricted register is desired, change both the domain
   and range projection and keep `Π_hw J_{H_β}`.  It is a different identity.
4. Treat the global form (`SO(3)` versus `SU(2)`) as a sector-lattice input and
   disconnected/finite components through finite strings or endpoint
   operators.  Neither is encoded by the local root commutator.

These are finite ED boundaries only.  Passing the surviving matrix identity is
not evidence for an infinite-volume soft limit; the two nonzero SU(3)
residuals are, however, unconditional falsifiers of the corresponding scalar
claims.
