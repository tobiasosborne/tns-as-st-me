<!-- LANE BRIEF O2: the experiments. TJO directive 2026-08-30: "If you
     cannot describe an experiment with QM that can observe or implement it,
     it is not operationally meaningful." This lane DESCRIBES THE
     EXPERIMENTS for the campaign's key quantities, at protocol level
     (measurement schemes/quenches/interferometry; circuit-level detail
     where cheap; heuristics fine, flagged). Run independently of lane O1
     (concurrent; do NOT read its output).
     Output: theory/lanes/reduction/o2-experiments.md, INCREMENTALLY. -->

# O2: explicit quantum-mechanical experiments for the campaign's key quantities

## Inputs

- `definitions.md` (the objects below); `theory/corner-a.md` (endpoint
  action, rates); `theory/memory-index.md` ⟨1⟩1/⟨1⟩5 area (TPM protocol);
  `theory/spin-s-twomagnon.md` (the slope); `refs/arxiv-0802.0447` (string
  order, LOCAL TeX, quote file+line); `claims/CLAIMS.md` rows for statuses.
- Optional context: docs/reduction-limits.md. Do not read o1-*.

## Design, for each item: preparation, operation, measurement, readout
formula, error/convergence estimate (quantitative where the campaign already
supplies rates), and what failure would look like.

1. **Measuring the projective class [ω] ∈ H²(G,U(1))** of an injective MPS
   vacuum: the string-order route (0802.0447 — quote the relevant selection
   rule) and at least one further route (e.g. endpoint-spin degeneracy /
   two-point interferometric comparison of twisted and untwisted strings),
   as protocols on physical spins only. State explicitly that the readout
   is representation-independent.
2. **Implementing/observing the boundary (endpoint) action**: the
   half-infinite truncated symmetry realized as a finite-region quench
   U_[0,L](g); quantitative statement that observables in a fixed window
   converge at rate λ̃^L (the campaign's proved rate) so the endpoint state
   is operationally preparable to accuracy ε with L = O(log 1/ε); the
   tomography of the resulting reduced state as the observation of the
   endpoint datum. Address the proved non-implementability clause (A1(b),
   non-scalar V): what it forbids (a norm-convergent global unitary) versus
   what the experiment above still delivers (window-local expectation
   values) — the operational content is the latter.
3. **The memory experiment**: the two-projective-measurement protocol as a
   laboratory protocol — what apparatus measures the windowed regularised
   charge (a windowed sum of on-site S^z: collective magnetometry /
   site-resolved quantum-gas-microscope readout), the two measurement
   times, the escaped-charge increment statistics, and what integer support
   looks like in data (histogram on ℤ with the offset cancellation). Also:
   the kink-displacement readout δx and its relation to the same data.
4. **The soft slope sgn(v_h−v_s)/S as an observable**: a two-wavepacket
   collision/interferometry protocol extracting the physical phase
   derivative at small soft momentum (time-delay/Wigner or Ramsey-type
   comparison of shifted and unshifted arms); error budget in packet widths;
   note which parts are already mirrored by the campaign's own numerics.
5. **The operational target for the reconstruction theorem (bd tns-25h)**:
   propose the boundary-algebra memory observable — e.g. the change of the
   window reduced density matrix / endpoint state across the transit,
   accessed by tomography before and after, and its candidate identity with
   the charge ledger — stated as a PROPOSED experiment + conjectured
   identity, clearly not a theorem. This is the "field-side memory made
   operational" deliverable; loose "bond data" language is banned.
6. **One honest negative**: name at least one campaign object for which you
   CANNOT describe such an experiment (candidates: a specific ansatz gauge
   datum X; a PEPS typing clause; the fixed-time D29 datum at infinite
   volume as literally defined) and say so plainly — per the directive such
   an object is not operationally meaningful and must be treated as
   scaffolding.

## Rules

Physics register; [physical argument] flags; local-TeX quotes with
file+line; statuses unchanged; protocols must involve only physical spins
and standard QM operations (unitaries, projective/POVM measurements,
tomography on reduced states); no edits outside theory/lanes/reduction/;
no bd operations; no LEDGER edits.
