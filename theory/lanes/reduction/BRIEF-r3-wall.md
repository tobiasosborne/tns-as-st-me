<!-- LANE BRIEF: R3 — continuum reduction of the memory corner (kink model).
     TJO directive 2026-08-30: must reduce, with physical arguments, to what
     the community accepts as memory: (a) magnon-driven domain-wall motion in
     Landau–Lifshitz (magnonics literature), (b) the Strominger–Zhiboedov
     "DC memory = ω→0 residue" chain. Honesty mandatory; a genuine mismatch is
     a finding. Output: theory/lanes/reduction/r3-wall.md, written
     INCREMENTALLY section by section. -->

# R3: does the lattice memory result reduce to accepted continuum memory?

## Inputs (read first)

- `definitions.md` D13–D16 (memory observables; the easy-axis XXZ kink model
  with boundary field, parameter q = Δ − √(Δ²−1)).
- `theory/corner-b-draft.md` §5, `theory/memory-quantization.md`,
  `theory/mq-e.md` — the PROVED rows: flux identity
  δx = (1/2s)[ȷ̃(0)_{left} − ȷ̃(0)_{right}] (M-flux); δx = −⟨N_T⟩/s and the
  ledger 2s·δx + (q_out − q_in) = 0 (M-quant / B3); the projected
  transmission t(k) = [1 + iJ²/(4ωv)]^{-1}, T(k) = 16(Δ−1)²k² + O(k⁴) (M-tk).
- `refs/arxiv-1411.5745/memory_4.tex` (LOCAL TeX): the Fourier-residue chain,
  esp. the falloff assumption at L.692–695.
- `refs/arxiv-1709.05018/draft1004.tex`: memory in the SUBLEADING falloff
  coefficient when the soft theorem has no 1/ω pole (L.639–814).
- `docs/continuum-antecedents.md` §§1,3 for orientation.
- If the magnonics domain-wall paper is needed (recommended):
  arXiv:1108.5570 (Yan–Wang–Xia, "All-magnonic spin-transfer torque and
  domain wall propagation", PRL 107, 177207 (2011)). Check refs/ first; if
  absent, fetch TeX from https://arxiv.org/e-print/1108.5570 (wait 3 s,
  VERIFY the title from the TeX before using). Do NOT edit refs/LEDGER.md —
  record the fetch and title-verification in your own output file; the
  orchestrator will reconcile the ledger.

## Tasks

1. **The continuum limit of the kink model.** What continuum field theory
   does the easy-axis ferromagnetic XXZ chain approach, and in which scaling
   regime (Δ → 1⁺ with what held fixed)? Identify the domain-wall solution
   (easy-axis Landau–Lifshitz / Walker wall) and its width in lattice units.
   State clearly that at FIXED Δ > 1 the D16 wall is one lattice site wide
   (deep Ising regime) and what that means for which limit is meaningful.
2. **The transmission puzzle — resolve it honestly.** Continuum easy-axis
   LL magnon–wall scattering is famously REFLECTIONLESS (Pöschl–Teller;
   T = 1 at every k — derive or quote it). The lattice theorem gives
   T(k) = 16(Δ−1)²k² → 0 at k → 0: perfect REFLECTION. These cannot both
   describe the same limit. Sort out the resolution with the actual
   scalings: is the sharp lattice wall's k→0 reflection a lattice-scale
   (wall-width ≪ wavelength vs ≫) statement that crosses over to the
   reflectionless regime as Δ → 1⁺? Exhibit the crossover variable
   (k·width?) and the two regimes of T. State which regime the PROVED
   lattice statement lives in and which regime the magnonics literature
   lives in. If they genuinely disagree in overlapping regimes, say so —
   that is the rat TJO smells, and finding it is the job.
3. **The displacement formula.** Derive, by angular-momentum conservation in
   the continuum LL wall (physics level), the wall displacement per
   transmitted magnon; express in magnetization density M₀ = s/a. Show
   whether the lattice δx = −N_T/s (in sites) with δx_phys = a·δx becomes
   exactly the accepted magnonics formula, constants included. Any factor-of-2
   discrepancy must be chased, not waved off.
4. **The Fourier-residue chain.** Express the proved lattice DC-flux
   identity as the lattice image of "DC memory = ω→0 residue" (1411.5745
   L.680–701): what plays the role of the falloff assumption "field
   approaches finite but different values as u → ±∞"? Map it to the named
   lattice hypotheses (local decay / local relaxation clauses — cite claim
   ids). Note where 1709.05018's subleading-falloff warning bites: which
   lattice observable corresponds to which falloff coefficient.
5. **Verdict** per sub-item (2), (3), (4): REDUCES CLEANLY / REDUCES WITH
   CAVEATS (list) / DOES NOT REDUCE (why, and what it means for the paper).

## Rules

- Physics register; continuum equations quoted from local TeX with file+line;
  lattice inputs cited by claim id and status, statuses unchanged.
- Flag every unproved physical step inline as [physical argument].
- Do NOT edit claims/CLAIMS.md, definitions.md, refs/LEDGER.md, or any file
  outside theory/lanes/reduction/ (a fetched refs/arxiv-1108.5570/ directory
  is allowed). Do NOT close or claim any bd issue.
