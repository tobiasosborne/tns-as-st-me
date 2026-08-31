<!-- ORCHESTRATOR SCAFFOLDING for the syk-jt lanes and their joint critic.
     TJO directive 2026-08-31 (operational razor, restated for SYK/JT):
     "this question cannot be correctly answered unless you specify the
     physically allowed observables clearly. until then you will get
     nonsense." This file is the lane-scoped observable specification.
     It creates no claims and defines no campaign symbols (L4: campaign
     definitions live in definitions.md only). -->

# Allowed observables for the SYK/JT decisive computation (tns-62n)

Microscopic system: two SYK dots (one disorder realization J), Hilbert
space H_L ⊗ H_R, prepared in the thermofield double; the pulse is a
compactly supported source coupling on the right dot.

## The algebra (exhaustive — nothing else is operational)

1. **One-sided observables** A_L, A_R: bounded-degree polynomials in the
   Majoranas of one dot, as expectations over repeated preparations.
2. **Joint two-sided correlators**: finite-order mixed correlators, e.g.
   G_LR(t1,t2) = (1/N) Σ_i ⟨ψ_i^L(t1) ψ_i^R(t2)⟩, and their finite-order
   generalizations (OTO orderings included). Implementable because both
   copies are built.
3. **Exactly conserved charges**: E_L, E_R (and discrete structure such
   as fermion parity). These are the ONLY exactly conserved allowed
   charges after the pulse.
4. **Implementable operations**: TFD preparation, Hamiltonian evolution,
   compactly supported sources, measurement of 1–3.

## Explicitly NOT observables (scaffolding only)

- The collective/reparametrization field f(u) or t(u), any representative
  thereof, and any relative Möbius/SL(2) "frame label".
- The Schwarzian SL(2) charges Q^a beyond the energy: EFT bookkeeping,
  quasi-conserved in the conformal window with 1/(βJ), 1/N corrections;
  no microscopic measurement protocol has been exhibited. Any lane or
  critic statement of the form "the charge ledger records the transition"
  must either exhibit an allowed-observable proxy or be struck.

## Consequences the critic must enforce

- "Physically distinct states" MEANS: separated by some observable in
  1–3. The one-side-shifted TFD family is exactly invisible to A_L and
  A_R separately and degenerate in (E_L, E_R); its distinctness is
  carried ENTIRELY by class-2 correlators.
- "A vacuum transition happened" has NO meaning beyond: late-time values
  of allowed observables under (pulse protocol) differ from (equilibrium
  protocol at the same measured E_f). The plateau computation (T.2) is
  constitutive of the transition, not a check on a pre-existing label.
- "Permanent" requires a declared limit order: N → ∞ (equivalently
  tree-level large C) FIRST, then detector time large WITHIN the stated
  EFT-validity window; the window must be stated quantitatively.
- Any conclusion phrased in frame/label language that does not reduce to
  1–3 is a razor violation: FATAL-class objection.
