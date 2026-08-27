# Orchestrator notes for the T1 synthesis/repair round (running log)

Accumulated between prover landing and synthesis brief. Items here MUST be
addressed by the synthesis worker alongside the r1 verdicts.

1. **ν-convention bug in briefs/memory-campaign-target.md:** the target's
   δx = −(1/2s)Σν p_ν together with (G-IDX.3) "supported on {0,2}" is
   inconsistent with the probe's convention-free Q_W indexing. Probe
   result: predicted support is {Q_W = 0, −2} ≡ ν = −Q_W ∈ {0,+2} ≡
   δx ∈ {0,−2} sites at s=1/2. The synthesized shard must fix ONE
   convention (recommend: index by the window-charge value Q_W, state the
   sign of the ledger identity once, and derive ν from it), and check both
   prover shards' signs against M-quant-G (G.1) before merging.
2. **Estimator tautology:** any checker validating δx must use a genuinely
   independent estimator (X̂₁ gradient centroid) — X̂₂ is ⟨Q_W⟩ + const,
   a tautological comparison. Probe already does this; keep it.
3. **Sharp-kink artifact (numerics culture):** sharp-kink preparation
   fakes a ~5% quantization violation (excitation defect radiates
   near-threshold pairs); dressed kink collapses it ×22. Any future memory
   numerics must use dressed kinks; dwmax=3 truncation is spuriously
   perfect (cannot host kink dressing) and must not be used as a control.
4. **Probe physics finding for the theory:** the extra integer mass sits in
   near-threshold two-magnon channels with zero group velocity (the soft
   endpoint degeneracy) — they never separate, yet land exactly on
   integers. This is empirical support for the channel-free formulation
   and a concrete reason G-IDX.3's two-channel reduction needs its
   inelastic-threshold fence.
5. Both T1 shards refute the operator form of G-IDX.0 by different
   mechanisms (codex: D17-fluctuation counterexample; Fable: A1(b)
   dichotomy). The synthesized shard should present BOTH refutation
   mechanisms — they bound the retreat from different sides.

## Adjudicated from memory-index-b-r1.md (codex critic, FAIL 1-6)

6. **Density quantization survives, decircularized.** Critic obj 1(b)
   contains a complete independent derivation: with a free density
   parameter ρ (NOT D13's site-spin s), the IT phase slope gives
   f_α'(0)=ω_α(S^z)=ρ, additivity+continuity+(INT)+β-tail give
   e^{4πiρ}=1, so 2ρ ∈ ℤ — using only D1, D2, (S), (INT); no cut, no
   correlation input. The synthesized shard states THIS as the
   unconditional lemma (new symbol ρ; merge proposal must NOT reuse
   D13's s) and cites the critic's derivation route. Also fold in obj 5's
   fix (tail-specific vacuum normal ordering Q_W^α, Q_W^β; keep the
   two-sided kink operator as is) and obj 6's fix (drop the one-sided
   red mutation + the parity claim; keep s→s+0.1 drift mutation; add a
   counterterm-shift or tail-covariance-phase mutation).
7. **The joint-law gap is THE synthesis problem.** Objections 2,3,4:
   (LR) marginal laws give only coupling bookkeeping; H-AD-G ⟹ (LR) is
   unproved (AD3's frozen words don't give window-marginal law
   convergence or uniform integrability — see the μ_W counterexample);
   the M-quant-G reduction must be stated as the direct channel law of
   −2sΔX (spec {0,2}, weights 1−⟨N_T⟩,⟨N_T⟩), never as a two-time
   coupling theorem. Candidate repair: the codex shard's TPM history
   protocol (outcomes ARE sequential measurement readouts; back-action
   controlled by an explicit D27 clause) — pending Critic A's verdict on
   whether THAT survives. If it does: merge = Fable's unconditional core
   (finite-window integrality, zero offset, 2ρ∈ℤ) + codex's TPM outcome
   law + both operator-form refutations + the direct-channel-law
   consistency statement.
8. **Register discipline for the merged theorem:** δx is NEVER claimed
   quantized (it is a mean); quantization claims attach to (i) finite-
   window/TPM outcome laws and (ii) the direct channel law under H-AD-G.
   The 2×2 counterexample (spec(Q_+−Q_−)={±1/√2}) goes in the shard as a
   permanent landmine exhibit.
