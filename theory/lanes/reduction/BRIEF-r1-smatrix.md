<!-- LANE BRIEF: R1 — continuum reduction of the exact two-magnon soft theorem.
     TJO directive 2026-08-30: reconciliation must REDUCE, in the right limits,
     to what the community actually accepts (EFT soft theorems). Physics rigor
     (perturbation theory / EFT matching / LSZ) suffices; honesty is mandatory:
     a trivial, non-commuting, or mismatched limit is a FINDING, report it
     plainly. No marketing language. Output: theory/lanes/reduction/r1-smatrix.md,
     written INCREMENTALLY section by section. -->

# R1: does the lattice two-magnon soft theorem reduce to the accepted continuum soft theorem?

## Inputs (read first)

- `theory/spin-s-twomagnon.md` — the PROVED exact spin-S regular-channel ratio
  `S_12 = (Sab − z_1 μ)/(z_2 μ − Sab)`, `μ = (2S−1)a + b` (symbol definitions
  inside the shard), and the proved slope `∂_{k_s} δ_phys|_0 = sgn(v_h−v_s)/S`.
- `theory/oracle-bethe.md` + `definitions.md` D6–D8 (conventions: physical
  in/out ratio, half-zone, hard momentum fixed in (0,π)).
- `refs/arxiv-2201.01393/manuscript.tex` and `refs/arxiv-2108.03189/main.tex`
  (LOCAL TeX, L3): type-B Goldstone soft scaling σ ≥ min(2m, n+1); the §4.1
  current-conservation pole-cancellation derivation of the Adler zero
  (the ACCEPTED route). Quote equations with file+line.
- `docs/continuum-antecedents.md` §5 for orientation.

## Tasks

1. **The naive continuum limit.** Physical momenta p = k/a, lattice spacing
   a → 0 at fixed p_1, p_2. Expand the EXACT S_12 (start spin-1/2 via the
   Bethe rapidity λ = (1/2)cot(k/2); then general S from the shard's ratio).
   Determine what S_12 converges to. Test the hypothesis that the limit is
   FREE (S → 1; Dyson's vanishing magnon interaction — the two-body
   interaction is irrelevant for ω ∝ k² in 1d). Display the expansions.
2. **Commutation of limits.** Compare lim_{k_s→0} lim_{a→0} against
   lim_{a→0} lim_{k_s→0} on the exact S_12. Find the uniform/crossover
   description: S_12 as a function of the physical momenta and a — identify
   the scaling variable that controls the crossover, and state exactly in
   which regime the lattice slope 1/S is visible. Non-commutation, if found,
   is a headline finding, not an embarrassment.
3. **EFT matching (the accepted comparison).** Write the leading-order
   magnon EFT for the spin-S Heisenberg ferromagnet (Schrödinger field,
   effective mass from the lattice dispersion, contact + leading derivative
   interactions). Match the couplings from the lattice at leading order in a.
   Compute the EFT two-body S-matrix (1d Schrödinger scattering) and check
   it against the a-expansion of the exact lattice S_12 order by order.
   Then derive the EFT's soft behavior by the ACCEPTED route (the 2201.01393
   §4.1 pole-cancellation mechanism, or equivalently standard effective-range
   reasoning) and state precisely which matched Wilson coefficient carries
   the lattice's 1/S — i.e. exhibit the physical combination (spin density
   S/a? scattering length ∝ a/S?) that survives, with units displayed.
4. **The soft-scaling bound.** Where does the proved lattice slope sit
   relative to σ ≥ min(2m, n+1) with m = 1 (type B₂)? Confirmed, saturated,
   or outside scope — say which and why.
5. **Verdict** (one of): REDUCES CLEANLY / REDUCES WITH CAVEATS (list) /
   DOES NOT REDUCE (why, and what it means for the paper's framing).

## Rules

- Physics register; every continuum equation quoted from local TeX with
  file+line; every lattice input cited by claim id (S2-2body, S2-2body-S,
  OR2) WITHOUT changing its recorded status.
- Every step you assert on physical grounds without proof: flag inline as
  [physical argument].
- Do NOT edit claims/CLAIMS.md, definitions.md, refs/LEDGER.md, or any file
  outside theory/lanes/reduction/. Do NOT close or claim any bd issue.
