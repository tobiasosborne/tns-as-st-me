# Bc charge-two falsifier, round 2

**STATUS: PARTIAL.** The pre-registered primary falsifier survives: the
three-magnon ED measurement is `4.07001 +/- 0.08981`, versus Bc's `2/s = 4`
for `s=1/2` and `|q_hard|=2`. This is evidence for, not a proof of, claim Bc.
A fixed-hard-momentum projection diagnostic remains estimator-sensitive, so
an `N`/packet-width convergence study is still required before strengthening
the label. (Named computations: `test_bc_charge2.jl`, `green.log`.)

## Structured experimental argument

**⟨1⟩1. ASSUME.** Use the periodic D6 spin-`1/2` Heisenberg ferromagnet at
`J=1`, D7's outgoing/incoming phase convention, a charge-two bound state at
`K=pi/2`, and signed soft momenta tending to zero as in D8.

Justification: D6--D8 and claim ML2 (the complete two-magnon resolution and
its bound band).

**⟨1⟩2. PROVE.** The prediction tested by this lane is `2/s=4`.

  **⟨2⟩1.** The hard composite contains two spin flips, hence
  `|q_hard|=2`, while D6 has site spin `s=1/2`.

  Justification: D6 and the Bc row of `claims/CLAIMS.md`.

  **⟨2⟩2.** Substitution in Bc's proposed `|q_hard|/s` law gives `4`.

  Justification: ⟨2⟩1 and claim Bc.

  **⟨2⟩3. QED.**

**⟨1⟩3. PROVE.** The computation is an independent three-magnon ED oracle.

  **⟨2⟩1.** `BcCharge2ED.jl` enumerates every ordered hard-core triple
  `0 <= x < y < z < N`, giving `binomial(N,3)` states, and constructs D6's
  Hamiltonian from its diagonal occupied-bond energy and nearest-neighbour
  hopping. At production size `N=100`, the dimension is `161700`.

  Justification: named computation `BcCharge2ED.jl`; D6.

  **⟨2⟩2.** At `N=6`, the sector spectrum agrees to `<1e-10` with an
  independently assembled dense tensor-product spin Hamiltonian; Hermiticity
  is also tested.

  Justification: named computation `test_bc_charge2.jl`, green row
  `O(N^3) sector layer vs dense spin oracle` in `green.log`.

  **⟨2⟩3.** The initial hard packet superposes ML2's geometric bound fibers,
  while the soft packet is Gaussian. Interacting three-magnon and free
  one-magnon states are propagated independently; the isolated outgoing
  magnon's chamber centroid minus its free centroid measures
  `Delta_s=-partial(delta)/partial(k_s)` in D7's convention.

  Justification: claim ML2, D7, and named computation `collision_row` in
  `BcCharge2ED.jl`.

  **⟨2⟩4. QED.**

**⟨1⟩4. PROVE.** The measured zero-soft-momentum slope is
`4.07000839 +/- 0.08981226`.

  **⟨2⟩1.** At `|k_s|=0.06`, the `+/-` average is `4.15982065`; at
  `|k_s|=0.10`, it is `4.31948688`. The four transmitted-channel weights are
  at least `0.96755585`, and all interacting/free norm drifts are below
  `8.1e-9`.

  Justification: named computation `test_bc_charge2.jl`; exact rows in
  `RESULT.json` and the green decision line in `green.log`.

  **⟨2⟩2.** A linear extrapolation in `k_s^2`,
  `(a_1 k_2^2-a_2 k_1^2)/(k_2^2-k_1^2)`, gives `4.07000839`. The quoted
  uncertainty `0.08981226` is the absolute shift from the softer finite-`k`
  value to the extrapolated value.

  Justification: named computation `measured_charge2_slope` in
  `BcCharge2ED.jl` and `green.log`.

  **⟨2⟩3.** The result differs from `4` by `0.07000839`, below both the quoted
  fit-shift error and the pre-registered absolute decision window `0.35`.

  Justification: ⟨2⟩2 and constants in `test_bc_charge2.jl`.

  **⟨2⟩4. QED.**

**⟨1⟩5. PROVE.** The checker is red-capable.

  **⟨2⟩1.** Before implementation, the zero-valued stub failed the value gate
  (`4.0 > 0.35`) and exited `1`.

  Justification: named computation `red-stub.log`.

  **⟨2⟩2.** After implementation, `--red` scales sector hopping by `1.08`;
  the independent dense-spectrum oracle detects a `0.1246977` discrepancy
  and the suite exits `1`.

  Justification: named computation `red-mutation.log`.

  **⟨2⟩3. QED.**

**⟨1⟩6. PROVE.** The result is evidence only and does not promote Bc.

  **⟨2⟩1.** The uncertainty above measures the two-point `k_s^2` fit shift;
  it does not include an independent `N` or `sigma_x` extrapolation.

  Justification: named computation `measured_charge2_slope` in
  `BcCharge2ED.jl`.

  **⟨2⟩2.** A non-decision fixed-`K` projection diagnostic gave
  `3.57977 +/- 0.07494`; its ordering projection clips dispersive tails and
  was not asymptotically controlled. This discrepancy is a named reason to
  retain `PARTIAL` despite the primary decision test passing.

  Justification: named computation `spectral_collision` in
  `BcCharge2ED.jl`, with raw output in `spectral-diagnostic.log`.

  **⟨2⟩3.** No kink-memory simulation was performed, so the predicted
  charge-two memory displacement `-2/s` remains untested here.

  Justification: scope of named computations `BcCharge2ED.jl` and
  `test_bc_charge2.jl`; claim Bc.

  **⟨2⟩4. QED.**

**⟨1⟩7. QED.** The primary charge-two slope falsifier survives at the stated
finite-volume/finite-packet scope; Bc remains CONJECTURE.
