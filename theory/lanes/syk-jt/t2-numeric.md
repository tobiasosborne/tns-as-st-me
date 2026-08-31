# T2 numeric lane: sourced two-sided Schwarzian computation

Status: **GREEN; computation complete.**  This report was updated
incrementally.  The lane created or edited only the four paths authorized by
`BRIEF-t2-numeric.md`.

## Failing-first evidence (law L1)

The complete standalone test specification was written before the production
module existed.  Its first execution was:

```text
$ julia --project=numerics numerics/test/test_schwarzian_memory.jl
ERROR: LoadError: SystemError: opening file
"/home/tobias/Projects/tns-as-st-me/numerics/src/schwarzian_memory.jl":
No such file or directory
...
in expression starting at
/home/tobias/Projects/tns-as-st-me/numerics/test/test_schwarzian_memory.jl:9
```

Exit code: **1** (RED).  The failure is the intended missing-implementation
failure, not a synthetically disabled assertion.  No result JSON existed or
was written during this run.

The first implementation-level run was also kept as a diagnostic RED:

```text
Test Summary:                                         | Pass  Error  Total
sourced two-sided Schwarzian memory                   |   72      2     74
  unsourced thermal saddle over several periods       |    3             3
  equation, SL(2) charge ledger, and RK4 order        |    5             5
  all prescribed profiles obey the charge cross-check |   40            40
  relative frame and simultaneous-gauge invariance    |    5             5
  bilocal model comparison and DC convergence         |    3      1      4
  finiteness and fail-closed output                   |   16            16
  complete prescribed campaign                        |           1      1
ERROR: LoadError: Some tests did not pass: 72 passed, 0 failed, 2 errored.
```

Exit code: **1**.  Both errors had the same cause: the Abel-transform horizon
asked the affine coordinate `exp(kT)` to represent times beyond its finite
floating-point chart.  The repair keeps a uniform-grid DFT of the computed
transient through `T=80` and integrates only the already-constant tail in
closed form.  This is a numerical chart repair, not a changed test or tolerance.

## Source equations fixed before implementation

- The Schwarzian definition
  `Sch(t,u) = -t''^2/(2t'^2) + (t''/t')'` is quoted at
  `refs/arxiv-1606.01857/GravityReparametrizationsRevised.tex:490-496`.
- The sourced equation
  `C (Sch(t,u))'/t' = -t' T_tz` is quoted at the same file's lines
  `611-623`; this fixes the sign used by the integrator.
- The three Schwarzian `SL(2)` charges are quoted at lines `889-900`.
  Lines `957-964` give the matter-plus-boundary charge ledger.  With the sign
  of the explicitly requested equation, the implemented positive injected
  matter flux is the oriented loss `Q_before-Q_after`; the TeX itself flags a
  sign check at line 965.
- The dressed bilocal kernel
  `[t'(u)t'(u')/(t(u)-t(u'))^2]^Delta` is quoted at lines `645-657`, and the
  insertion-by-insertion reparametrization rule at lines `662-675`.
- The two-sided gauge condition `Q_L^a=-Q_R^a`, hence invariance under one
  simultaneous `SL(2)` action, is stated at lines `902-909`.
- The Lorentzian finite-temperature projective coordinate `t=exp(tau)` is
  identified at line `901`.  The integrator is also independently regressed
  against the brief-mandated regular-chart saddle `tan(u/2)`.

## Test inventory (pre-registered in the RED file)

1. `tan(u/2)` regression to `1e-10` on regular projective charts in three
   periods.
2. Pre/post support charge conservation to `1e-8`, oriented charge jump versus
   independently quadratured flux to `1e-6`, and fourth-order step-halving
   floor `3.8`.
3. All exact parameter profiles, including the balanced derivative Gaussian.
4. Relative-frame and dressed-observable invariance under a simultaneous
   two-sided Möbius move to `1e-8`.
5. Constant-versus-decaying-exponential fits for both `delta G_LR(T)` and the
   extracted `Delta u_rel(T)` on `T={2,5,10,20,40}`.
6. Discrete low-frequency response residue, charge-normalized soft response,
   and convergence toward the late displacement.
7. Fail-closed validation: NaN, empty samples, and charge violation are tested
   both as thrown validation errors and as child processes with nonzero exit;
   none may create a JSON file.
8. The exact eight-point campaign grid and final all-finite JSON validation.

The final execution was:

```text
$ julia --project=numerics numerics/test/test_schwarzian_memory.jl
Test Summary:                       | Pass  Total   Time
sourced two-sided Schwarzian memory |   81     81  55.4s
```

The three explicit poison entry modes also establish the promised process exit
contract:

```text
poison=nan    exit=1 json_created=no
poison=empty  exit=1 json_created=no
poison=charge exit=1 json_created=no
```

## What was implemented

The 472-line standalone module is within the brief's 200--500 line L2 bound.
With state `y=(t,v,a,j)=(t,t',t'',t''')`, differentiating the quoted
Schwarzian and imposing T.1 gives

```text
t'''' = 4 t'' t'''/t' - 3 t''^3/t'^2 - t'^3 T_tz/C.
```

This first-order system and classical RK4 are at
`numerics/src/schwarzian_memory.jl:77-116`; pre/source/post segmentation keeps
RK stages from straddling the top-hat discontinuities (`:173-192`).  The charge
formulas and independent trapezoidal flux integral are at `:118-145`.

The final Schwarzian fixes `k_f=sqrt(-2 Sch_f)` and
`E_f=-C Sch_f`.  A homogeneous SVD fit determines the determinant-one matrix
`M_R` in `t_R=(a exp(k_f u)+b)/(c exp(k_f u)+d)` (`:147-192`).  I fix the one
simultaneous two-sided gauge by `M_L=I` and retain only
`M_rel=M_L^{-1}M_R` (`:194`).  Both `M_rel` and the bilocal were tested after
the simultaneous move `(M_L,M_R)->(gM_L,gM_R)`.

The Lorentzian two-sided continuation of the cited dressed kernel, with
operator dimension `Delta=1/2`, is at `:199-225`.  The reported relative delay
is extracted only from the observable,
`Delta u_rel=-delta G_LR/(partial_T G_LR^eq)`.  Constant and pure decaying
exponential models are fitted with an AIC penalty (`:227-247`).  Raw values are
kept at all five prescribed times; the model comparison uses the settled late
tail `T={5,10,20,40}` because the small projective coefficient can still be
turning on at `T=2`.

T.3 uses an Abel-damped direct DFT (`eta=omega^2`, uniform `dt=0.02`) of the
computed response through `T=80`, followed by the analytic transform of its
already-constant tail (`:294-328`).  Its soft-side comparison is independent:
linearizing `t=exp(u+epsilon)` gives
`epsilon''''-epsilon''=-exp(2u)T_tz/C`; `:249-292` solves that equation and
attaches the infinitesimal dressed-bilocal vertex, normalized by the measured
three-component injected-charge norm rather than a fit.

Finally, `:331-382` recursively rejects every non-finite or required-empty
value and any charge violation before opening the output path.  Campaign
assembly and its second validation are at `:397-472`.

## Results

### Numerical controls

- Maximum `tan(u/2)` regular-chart error over three periods:
  `4.047e-12` (required `<1e-10`).
- Step-halving errors for `h={0.08,0.04,0.02,0.01}`:
  `{3.184e-4,1.763e-5,1.042e-6,6.338e-8}`; measured orders
  `{4.175,4.081,4.039}` (required `>=3.8`).
- Worst pre-pulse / post-pulse charge drift across all eight rows:
  `6.66e-14 / 6.04e-12` (required `<1e-8`).
- Worst charge-jump quadrature error: `2.18e-8` (required `<1e-6`).
- Worst late Möbius-fit residual: `4.89e-15`.
- The redshift-balanced derivative Gaussian leaves only
  `Delta E=2.83e-8` at `C=10` and `2.83e-9` at `C=100`, versus
  `O(10^-2)` for the ordinary Gaussian.

Here `RSS u c/e` and `RSS G c/e` are constant/exponential residual sums on
`T={5,10,20,40}`.  `DC/late` is
`Re[-i omega delta u(omega)]/Delta u_rel(40)` at the smallest sampled
`omega=0.05`; `DC/vertex` uses the independent charge-normalized linear soft
vertex.

| C | pulse, epsilon | Delta u_rel at T=2,5,10,20,40 | u verdict; RSS c/e | delta G verdict; RSS c/e | DC/late | DC/vertex |
|---:|---|---|---|---|---:|---:|
| 10 | top-hat, .01 | `3.684e-7, 1.18731e-4, 1.24763e-4, 1.24803e-4, 1.24803e-4` | constant; `2.754e-11/2.971e-11` | exponential; `4.764e-13/1.553e-23` | .98610 | .98588 |
| 10 | top-hat, .1 | `1.093e-5, 1.17189e-3, 1.23022e-3, 1.23061e-3, 1.23061e-3` | constant; `2.575e-9/2.783e-9` | exponential; `4.535e-11/6.278e-21` | .98620 | .98408 |
| 100 | top-hat, .01 | `2.941e-8, 1.18887e-5, 1.24939e-5, 1.24980e-5, 1.24980e-5` | constant; `2.772e-13/2.991e-13` | exponential; `4.788e-15/5.719e-25` | .98609 | .98607 |
| 100 | top-hat, .1 | `3.684e-7, 1.18731e-4, 1.24763e-4, 1.24803e-4, 1.24803e-4` | constant; `2.754e-11/2.971e-11` | exponential; `4.764e-13/1.553e-23` | .98610 | .98588 |
| 10 | Gaussian, .05 | `-1.549e-5, 1.24925e-4, 1.32079e-4, 1.32127e-4, 1.32127e-4` | constant; `3.873e-11/4.144e-11` | exponential; `5.271e-13/8.808e-22` | .98473 | .98466 |
| 10 | balanced dGaussian, .05 | `2.40285e-5, 2.57422e-5, 2.58297e-5, 2.58303e-5, 2.58303e-5` | constant; `5.791e-15/1.685e-14` | exponential; `2.246e-14/3.288e-26` | .99671 | .99684 |
| 100 | Gaussian, .05 | `-1.561e-6, 1.25133e-5, 1.32316e-5, 1.32365e-5, 1.32365e-5` | constant; `3.904e-13/4.177e-13` | exponential; `5.304e-15/1.985e-23` | .98472 | .98471 |
| 100 | balanced dGaussian, .05 | `2.40280e-6, 2.57412e-6, 2.58287e-6, 2.58293e-6, 2.58293e-6` | constant; `5.788e-17/1.685e-16` | exponential; `2.246e-16/3.257e-28` | .99671 | .99672 |

The DFT ratios converge monotonically as `omega={0.2,0.1,0.05}`.  Across the
ordinary top-hat/Gaussian rows, `DC/late` moves from `0.777--0.798` through
`0.940--0.946` to `0.9847--0.9862`; balanced rows move from `0.9500` through
`0.9870` to `0.9967`.  The independent soft-vertex ratios have the same
convergent range and differ nontrivially from `DC/late` at finite amplitude.

**Decisive numerical verdict.**  Every extracted relative delay approaches a
nonzero constant, and its DC residue agrees with the independently normalized
soft vertex at the 0.3--1.6% level at `omega=0.05`.  Nevertheless, the raw
final-energy-subtracted observable `delta G_LR` is exponentially decaying at
all eight points, with exponential RSS many orders below constant RSS.  Thus
this computation finds a permanent *relative-frame/time-delay parameter* but
no nonzero late plateau in the specified two-sided correlator.  Under the
strict operational T.2 criterion in the reconstruction memo, this is a clean
negative result for B rather than a completed SYK/JT triangle.

## Caveats

- The requested exact saddle `tan(u/2)` is an Euclidean/projective-circle
  representative with affine poles, whereas the cited source explicitly uses
  `t=exp(tau)` for Lorentzian finite-temperature computations at line 901.
  Therefore the regression uses three regular tan charts, while the sourced
  two-sided observable uses the pole-free Lorentzian exponential chart.
- The primary dimension was not specified; the run fixes `Delta=1/2` and
  records it in JSON.  Absolute correlator amplitudes depend on this choice.
- “Equilibrium at final energy” means the left ruler retains its unsourced
  `k_L=1`, while the right equilibrium comparator has the measured `k_f` but
  no relative Möbius transform.  This isolates the frame effect from the right
  temperature change without pretending the post-pulse state is a new TFD.
- The source-sign ambiguity is real: T.1 as printed makes
  `Q_before-Q_after=integral t'T(1,t,t^2)`, while lines 963-965 print the
  opposite derivative sign and contain `FIXSIGNS AND FACTORS`.  No sign was
  silently changed.
- The Gaussian profiles are truncated at `[0,0.5]`; their endpoint value is
  exponentially small but nonzero.  Segmented integration prevents this from
  lowering RK4 order at the support boundary.
- The balanced pulse is the derivative Gaussian multiplied by the known
  thermal redshift `exp[-2(u-0.25)]`, so the physically relevant
  `t'^2 T_tz` flux, rather than merely `integral T_tz`, is balanced.  Its tiny
  residual energy is nonlinear/numerical, not fitted away.
- The `omega->0` result uses Abel damping and a constant-tail completion; it is
  not an FFT-bin extrapolation.  The three-frequency convergence is explicit,
  but a continuum analytic Ward identity remains the role of the independent
  analytic lane.

## MERGE PROPOSALS

No shared edit is required for standalone reproducibility.  The existing
`numerics/test/runtests.jl` already auto-discovers every `test_*.jl`, including
this lane test.  If maintainers want a public package API, they may optionally
include/export `SchwarzianMemory` from `TriangleMPS.jl`; the lane deliberately
did not make that shared-file change.
