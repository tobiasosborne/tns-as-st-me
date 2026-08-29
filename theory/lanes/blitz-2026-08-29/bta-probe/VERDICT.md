# BTA pre-registered moment probe — binding reading

**STATUS: NEGATIVE.**  The product-family moment-map picture survived, but the
pre-registered nonscalar-`V_θ` period prediction did not.

**Provenance constraint — binding.**  The observation that TNS variational
classes carry a Kähler structure and that TDVP is the associated Hamiltonian
flow originated with Tobias Osborne, who communicated it to Jutho Haegeman,
who made it work.  Do not state this in any paper without TJO's explicit
sign-off.

The current Letter is not presumed to be the destination for this result; no
paper-scope decision is made here.

## Structured verdict

⟨1⟩1. **ASSUME** the six gates and thresholds pre-registered in
`briefs/bta-kahler-target.md` §6.2.  **PROVE** the gate verdicts of the real
families.

⟨2⟩1. P1 **PASS**: the minimum fitted potential-growth exponent is
`1.7894055864` over the entire registered `x_0` grid, and the largest
`L=40→80` curvature change is
`1.7764e-15 ≤ 1e-10`.

*Justification.* Named computation `bta_moment_probe.py::evaluate`, recorded
in `bta_moment_probe_results.json` gate P1; the reproduced `Δ=1.5`, `S=1/2`,
`x_0=0.3` values are `𝔨_W = 113.0315, 417.1574, 1602.8633, 6284.0919` and
`Ω_W = 0.9995539415, 0.9995539449, 0.9995539449, 0.9995539449`.

⟨2⟩2. P2 **PASS**: the independent norm-Hessian and charge-probability routes
give maximum relative residue `1.6126e-15 ≤ 1e-12` on F-A/F-B.

*Justification.* Named computations
`bta_moment_probe.py::omega_from_norm_hessian` and
`bta_moment_probe.py::mu_prime_from_probabilities`, recorded in
`bta_moment_probe_results.json` gate P2; the observable is D13(a), and the
family is D16/F-B.

⟨2⟩3. P3 **PASS** and P4 **PASS**: `(area/2π)` equals
`1,2,3,4 = 2S` across the recorded grid to maximum error `2.6646e-15`,
while the no-fit `ν=2` comparison has
maximum error `5.6069e-12 ≤ 1e-8` and all 22 frozen ED prediction rows agree
to `3.3340e-13`.

*Justification.* Named computations `bta_moment_probe.py::area_per_lattice_period`,
`bta_moment_probe.py::phase_slope`, and `bta_moment_probe.py::frozen_json_error`,
recorded in `bta_moment_probe_results.json` gates P3/P4; the charge calibration
is D13(a).

⟨2⟩4. P5 **PASS**: both non-eigen deformations `q'/q=0.8,1.25` obey P2, with
maximum relative residue `7.5319e-16 ≤ 1e-12`.

*Justification.* Named computation `bta_moment_probe.py::evaluate`, recorded
in `bta_moment_probe_results.json` gate P5; no Hamiltonian or eigenfamily
property enters that computation.

⟨2⟩5. P6 **FAILS its F-D clause**, while its F-A kill-shot does **not** fire.
Every scalar-family period is zero, including `Per_W(F-A)=0`.  The F-D period
is also zero, despite `max|Ω|=1.00355`, nonscalar distance `0.71483`, and
injective-tail transfer gaps `0.42917` and `0.17633`.

*Justification.* Named computation `bta_moment_probe.py::fd_curvature_and_period`,
recorded in `bta_moment_probe_results.json` gate P6; the tensors reuse the
charge-diagonal `χ=2` construction of `memory_index_check.py` IDX-C7(ii).

⟨2⟩6. The failure is structural for the registered loop: on the orbit tangent
`ξ^♯`, `(ι_{ξ^♯}ϖ)(ξ^♯)=ϖ(ξ^♯,ξ^♯)=0` by antisymmetry of the D32(c) two-form,
so integrating this one-form along the same `φ`-orbit always gives zero.

*Justification.* D32(c), D34(c), and the direct two-form contraction in named
computation `bta_moment_probe.py::fd_curvature_and_period`.

⟨2⟩7. The registered mutations are live: `--red` makes P2/P3/P4 fail;
`--red-fs` makes P1/P2 fail; and `--selftest` catches a mutation at every gate
P1--P6.

*Justification.* Named computation `bta_moment_probe.py` modes `--red`,
`--red-fs`, and `--selftest`, recorded in the three corresponding JSON files.

⟨2⟩8. **QED.**

## Plain-prose ladder reading

L1 survives this falsifier: P1--P4 pass and the fatal F-A period kill-shot is
absent.  This is numerical survival, not a proof or status promotion.

The geometric core of L2 survives P5: the identity is not an accident of the
exact eigenfamily.  The proposed L2.c/D34(c) diagnostic “zero period iff
scalar `V_θ`” dies as stated, because its specified orbit period is identically
zero even for the nontrivial F-D family.  This does not prove a global moment
map on a thermodynamic `χ>1` family; it removes this proposed obstruction test.

L3 is not directly tested and receives no status advance.  L4's product-family
normalisation survives P3/P4, but its higher-dimensional DH clause is untested.
L5 is outside this probe.

The named forward attack is to evaluate `[ι_{ξ^♯}ϖ]∈H¹(ℳ)` on closed cycles
transverse to the generating orbit (a basis of actual `H_1(ℳ)`), rather than
on the `ξ^♯` orbit itself.  A family with an independent closed cycle is needed;
on the present cylinder-like two-coordinate families the registered orbit
integral cannot diagnose nonscalar `V_θ`.
