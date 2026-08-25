You are the prover on a rigorous physics campaign. Read CLAUDE.md (laws), HANDOFF_MPS_SOFT_THEOREM.md (the brief, esp. §1.4, §3, §5.1), notation.md, definitions.md, docs/framing.md.

TASK: produce `theory/oracle-bethe.md` — the exact-oracle document that any lattice soft theorem in this campaign must match. Everything from first principles; this file becomes ground truth.

Required content, each part Lamport-structured (hierarchical numbered steps ⟨1⟩1, ⟨2⟩1, ASSUME/PROVE, explicit QED; every leaf justified by a definition, algebra, or a named prior step) per law L6b:

1. **Setup.** Isotropic spin-1/2 Heisenberg ferromagnet on the chain, H = −J Σ_x (S_x·S_{x+1} − 1/4), J > 0, vacuum |↑…↑⟩. One-magnon states and exact dispersion ω(k) = J(1 − cos k) (prove it). Group velocity v(k).

2. **Exact two-magnon problem.** Bethe-ansatz solution in the two-down-spin sector: derive the exact two-magnon S-matrix S(k₁,k₂) in LATTICE MOMENTUM variables (not just rapidities) — the standard result equivalent to S = −(e^{i(k₁+k₂)} − 2e^{ik₁} + 1)/(e^{i(k₁+k₂)} − 2e^{ik₂} + 1) — derived, not quoted, with your conventions for ordering/incoming-outgoing stated explicitly and consistently. Include the relation to rapidity variables λ(k) = (1/2)cot(k/2) and S = (λ₁−λ₂−i)/(λ₁−λ₂+i) as a cross-check. Also treat bound states (string solutions) only insofar as needed to state where the expansion below is valid.

3. **THE SOFT EXPANSION (the core deliverable).** Fix a "hard" magnon momentum k_h in (0, π); let the soft momentum k_s → 0⁺ (and also k_s → 0⁻ — state whether the limit is direction-dependent). Expand S(k_s, k_h) = exp(iδ(k_s,k_h)) to SECOND order in k_s:
   - verify soft decoupling S → 1 (Dyson's k → 0 magnon decoupling);
   - give the exact coefficient of the O(k_s) term of the phase δ as a function of k_h, and REWRITE it in terms of physically invariant data of the hard magnon (group velocity v(k_h), energy ω(k_h), etc.) — find the form that looks universal (candidate forms to test: cot(k_h/2), 1/v, ω/v², …). Identify which rewriting is most natural and note all equivalent forms;
   - give the O(k_s²) coefficient too;
   - state precisely in which variable the expansion is regular (k_s vs ω_s = ω(k_s) ~ J k_s²/2 — this matters: quadratic dispersion, brief §5.1) and give the expansion in ω_s as well;
   - carefully discuss the order of limits / non-uniformity near k_h → 0 and k_h → π, and near the bound-state threshold.

4. **Numerical cross-check.** Write and run a small standalone script (julia or python, your choice; put it in `theory/checks/oracle_bethe_check.(jl|py)`) that (a) checks the two-magnon Bethe energies/S-matrix against exact diagonalization of H on a ring of N ≈ 16–20 sites in the two-magnon sector, and (b) checks your soft-expansion coefficients against numerical differentiation of the exact S. Record the outputs (numbers, tolerances) in the .md. If any check fails, fix the derivation, not the check.

5. **Summary table.** "Oracle facts" — the numbered list of exact statements (O1, O2, …) that Conjecture S must reproduce, each with its formula and validity domain.

Constraints: quote literature only from local TeX under refs/ (cite file paths) or derive from scratch; no web access needed. ≤ 500 lines for the .md (shard law L2) — if you need more, split into oracle-bethe.md + oracle-bethe-appendix.md. Write files to disk BEFORE finishing. Finish by printing a 10-line summary of the oracle facts.
