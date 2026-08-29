# SPT dynamical deciding computation — small-ED record

**Status: PARTIAL.**  This is the dynamical T0--T3 record requested for lane
`spt-dyn`.  It does not repeat the completed static transfer checks.

## ⟨1⟩1. Scope and preregistration

**ASSUME.**  Use the spin-one open-chain family named in the lane brief, its
`D=0` Haldane representative and `D=3` large-`D` representative, and the
T0--T3 gates frozen in `theory/spt-scoping-draft.md` ⟨1⟩6.  Interpret edge
memory only with the D21--D22 register and asymptotic caveats.

**PROVE.**  The computation is a red-capable, internally validated small-size
test, and its outcome is no stronger than `PARTIAL` evidence concerning
SPT-M'-dyn.

**⟨2⟩1. Model fence.**  The `D=0` Hamiltonian tested here is the Heisenberg
Haldane representative, not D23's exact open AKLT parent Hamiltonian.  Phase
membership does not identify their reflection matrices.  Therefore even a
positive T3 outcome here would not prove the narrowly stated SPT-M'-dyn row.
**Justification:** D23; claim SPT-M'-dyn; named computation
`run_spt_dyn.py`, field `scope_fence` in `results.json`.

**⟨2⟩2. Size downgrade.**  The requested sizes were `32,48,64`.  Charge-sector
ED was completed at open-chain `L=8,10,12`, periodic `L=6,8,10,12`, and
dynamical `L=10`; the packet width was reduced from about `10` sites to
`1.35`.  No thermodynamic or scattering limit is inferred from these sizes.
**Justification:** D19 limit order; D22 (H-AD-edge); named computation
`run_spt_dyn.py`, `results.json` field `downgrade`.

**⟨2⟩3. Frozen gates.**  Before `results.json` existed, `check_spt_dyn.py`
fixed the original T0/T1/T3 thresholds, operationalised T2's unspecified word
“same” as a 10% relative intercept tolerance, and failed on the missing file.
**Justification:** named computation `check_spt_dyn.py`; recorded first failure
`red_initial.log`.

**⟨2⟩4. Observable fence.**  T0 and T3 retain the superseded draft's finite
left-window diagnostics only because the brief explicitly asks for T0--T3.
They are not silently identified with the canonical registered operators
`ℜ_C` or `ΔQ_edge`.  T2 is an explicitly normalized single-mode estimator,
not an assertion that D20's unspecified channel embeddings have been supplied.
**Justification:** D20--D22; `notation.md` row for the superseded `m_L,Δm_L`;
claim SPT-M'.

**⟨2⟩5. QED.**  Items ⟨2⟩1--⟨2⟩4 fix the scope under which the numerical
statements below may be read.  **Justification:** D19--D23; claim SPT-M'-dyn.

## ⟨1⟩2. Exact implementation and validation

**ASSUME.**  Each computation is restricted to a fixed total-`S^z` sector.

**PROVE.**  The reported finite matrices and time evolutions pass their
algebraic and numerical checks, and the checker is red-capable.

**⟨2⟩1.**  `spt_dyn_ed.py` enumerates the spin-one basis in a fixed charge
sector and constructs the bilinear exchange plus single-ion term directly;
all transitions stay in the same sector.  **Justification:** D22's conserved
charge requirement; named computation `spt_dyn_ed.py`.

**⟨2⟩2.**  Across every run, the maximum Hamiltonian Hermiticity residue is
`0`, time-evolution norm drift is `2.19e-13`, and total-charge-sector residue
is `4.39e-13`.  **Justification:** named computation `run_spt_dyn.py`,
`results.json` field `validation`; named checker `check_spt_dyn.py`.

**⟨2⟩3.**  The green checker reconstructs each T2 quotient and fit from its
stored raw complex form factor, verifies the T3 exclusive-channel algebra,
and exits zero.  The `--red` mutant adds `1e-4` to a load-bearing Hermiticity
residue and exits nonzero.  **Justification:** named computation
`check_spt_dyn.py`; `validation_green.log`; `validation_red.log`.

**⟨2⟩4. QED.**  The finite-size numbers below are reproducible numerical
outputs rather than unchecked run traces.  **Justification:** named
computations `run_spt_dyn.py`, `analyze_results.py`, and `check_spt_dyn.py`.

## ⟨1⟩3. T0 and T1 — finite edge register diagnostics

**ASSUME.**  A right boundary field `0.20` selects an edge orientation while
preserving total `S^z`; the left diagnostic window is the first half-chain.
For T1 the `M=1` partner is retained only when its energy lies within `0.25`
of the selected `M=0` state.

**PROVE.**  The trivial-side diagnostic is clean at these sizes, while the
Haldane-side sequences do not meet the frozen largest-size gates and are not
converged.

**⟨2⟩1. T0.**  At `L=8,10,12`, the Haldane values are respectively
`-0.18149,-0.58166,-0.27724`; the large-`D` values are
`-1.115e-4,-3.787e-5,-1.277e-5`.  Thus the `D=3` half of the `<0.05` gate is
clean, but the `D=0,L=12` magnitude is outside `[0.45,0.50]` and the sequence
has strong finite-size/parity drift.  **Justification:** D21 endpoint-charge
caveat; named computation `analyze_results.py`, `analysis.json` T0.

**⟨2⟩2. T1.**  The projected Haldane `|F^+(0)|` sequence is
`0.60448,1.17224,0.74884`; at `L=12` it misses the `>0.9` gate.  The large-`D`
ground-register value is zero because its lowest `M=1` state lies `1.4762`
above the ground state and is excluded by the preregistered `0.25` edge window;
its unprojected bulk-state matrix element is `0.25083` and is not called an
edge form factor.  **Justification:** D20 scalar-form-factor typing; D21 edge
register; named computation `run_spt_dyn.py`, `results.json` T1 fields.

**⟨2⟩3. QED.**  T0 and T1 are **unresolved at the downgraded sizes**, not
negative evidence against SPT-E': the original thresholds were stated at
`L=48`, whereas neither Haldane sequence is converged by `L=12`.
**Justification:** claim SPT-E'; D19 order of limits; named computation
`analyze_results.py`.

## ⟨1⟩4. T2 — model-to-model quotient test

**ASSUME.**  On each periodic chain, apply the modulated conserved `S^z`
charge to the normalized ground state, normalize the resulting single-mode
state, and evaluate its commutator form factor.  Compare the imaginary soft
coefficient of the quotient by `exp(ik)-1` at the smallest momentum for each
size, fitting linearly in `k^2`.

**PROVE.**  This operational T2 estimator fails the preregistered
model-to-model agreement gate; this does not refute SPT-B'.

**⟨2⟩1.**  For `L=6,8,10,12`, the Haldane quotient coefficients are
`2.35771,2.68661,2.92358,3.12591`; the large-`D` coefficients are
`2.67077,3.16878,3.58638,3.95284`.  **Justification:** D20 bulk insertion
typing; named computation `run_spt_dyn.py`, `results.json` T2 points.

**⟨2⟩2.**  The all-size `k^2` intercepts are `3.30643` and `4.22712`, a
relative difference `0.24442 > 0.10`.  Removing the smallest sizes increases
the relative differences to `0.27029` and `0.28668`, so the failure is not
caused solely by the `L=6` point.  **Justification:** named computation
`analyze_results.py`, `analysis.json` T2.

**⟨2⟩3.**  SPT-B' proves cancellation of a projective multiplier and
continuity/deformability of normalized bulk coefficients; it explicitly does
not prove equality of arbitrary coefficients between different Hamiltonians.
Therefore T2 falsifies the old numerical agreement gate for this estimator,
not claim SPT-B'.  **Justification:** claims SPT-B-mult and SPT-B'; D20.

**⟨2⟩4. QED.**  T2 is a clean **NEGATIVE** for the frozen comparator.  A
viable replacement is to compare a fixed registered contraction along a
same-phase path, or to match external channel data/`Ad(V)` data before asking
for equality; merely choosing `D=0` and `D=3` does neither.
**Justification:** claim SPT-B'; D20; named computation `analyze_results.py`.

## ⟨1⟩5. T3 — reflection, edge-label change, and memory

**ASSUME.**  At `L=10`, launch charge-`+1` Gaussian packets at three adjacent
momenta `π-0.45,π-0.60,π-0.75`.  Define the candidate edge-flip tangent
subspace from centered bulk `S^z` insertions on the `M=1` edge partner and
orthogonalize it against the no-flip `S^+` tangent subspace.  Track combined
changes in local `S^z` and `(S^z)^2` to detect turnaround.

**PROVE.**  A sizeable edge-label-changing finite-chain component is present,
but neither asymptotic separation nor the frozen memory gate is established.

**⟨2⟩1. Reflection.**  All six model/momentum packets turn around after
approaching the left boundary.  Initial exclusive flip probabilities are
below `1.4e-30`, so the later signal is not initial channel overlap.
**Justification:** D22's channel distinction; named computations
`run_spt_dyn.py` and `check_spt_dyn.py`, `results.json` momentum scans.

**⟨2⟩2. Edge-label-changing component.**  On the Haldane representative the
three post-window exclusive amplitudes are `0.44112,0.44430,0.44527`.  They
are nonzero and stable across the three tested momenta at this fixed size.
The corresponding large-`D` raw tangent-subspace amplitudes are
`0.26785,0.26569,0.41036`, but that model has no eligible low-energy edge
partner; its `M=1` state is a bulk excitation, so these numbers are leakage
controls and not edge-flip amplitudes.  **Justification:** D21 register typing;
claim SPT-M'-dyn; named computation `analyze_results.py`, `analysis.json` T3.

**⟨2⟩3. Missing asymptotic gate.**  None of the three Haldane packets reached
the declared post-separation condition before `t=12`; only one of three
large-`D` packets did.  No `L=8→10` dynamical drift or truncation/finite-size
error was obtained.  Hence the stronger D23 rule “greater than `25×` combined
error at three adjacent momenta” cannot be invoked, despite the raw nonzero
values.  **Justification:** D19 limit order; D22 (H-AD-edge); claim
SPT-M'-dyn; named computation `analyze_results.py`.

**⟨2⟩4. Memory ledger.**  In the Haldane postselected label assignment, the
left-window edge change is `1.05234` and the bulk label change is `-1`, giving
a `0.05234` budget defect.  This exceeds the `5e-3` asymptotic target.  The
unconditioned finite-window memory signals are `0.70420` and `0.23857`, whose
ratio is `2.9518 < 10`; therefore the frozen T3 payoff gate fails.
**Justification:** D22; claim SPT-M'; named computations `run_spt_dyn.py` and
`analyze_results.py`.

**⟨2⟩5. QED.**  T3 supplies finite-`L` evidence for a symmetry-allowed
edge-label-changing component in the Haldane representative, but it does not
establish (H-AD-edge), persistent quantised memory, the requested finite-size
stability, or the exact-AKLT-parent SPT-M'-dyn conjecture.
**Justification:** D22--D23; claims SPT-M' and SPT-M'-dyn.

## ⟨1⟩6. Disposition and forward attack

**⟨2⟩1.**  The scientific gate vector is
`T0=false,T1=false,T2=false,T3=false`.  T0/T1 are finite-size unresolved; T2
is a negative for the old comparator; T3 is positive small-size channel
evidence but asymptotically unresolved and fails the original memory ratio.
**Justification:** named checker `check_spt_dyn.py`; `validation_green.log`.

**⟨2⟩2.**  The next viable attack is an MPS/TDVP run at `L=32,48,64` with
separate left-edge and outgoing-packet windows, explicit postselection on the
Schmidt/edge register, and a second run for D23's exact AKLT parent.  T2 should
be replaced by a matched-register or same-path test consistent with SPT-B',
not the refuted cross-model equality gate.  **Justification:** D19--D23;
claims SPT-B' and SPT-M'-dyn.

**⟨2⟩3. QED.**  The honest lane status is **PARTIAL**.  No claim status is
promoted or refuted by this small-ED record.  **Justification:** claims SPT-B',
SPT-E', SPT-M', and SPT-M'-dyn; named computation `check_spt_dyn.py`.
