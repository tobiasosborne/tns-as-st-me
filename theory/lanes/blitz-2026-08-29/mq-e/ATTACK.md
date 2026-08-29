# Hostile pass on `mq-e-proof.md`

## Verdict before repair: MAJOR, repairable

1. **MAJOR — literal locality overclaim.**  The standing Mq-E hypothesis in
   `memory-quantization.md` says fixed-window observables become
   finite-support graph observables.  This is false without channel
   subtraction: `S^z` near the kink and `𝔛_W` have different nonzero constants
   on the two remote tails.  Required repair: prove the exact
   `o_LΠ_-+o_RΠ_++F_W` decomposition and state that only the channel-subtracted
   remainder is finite-support.
2. **MAJOR — “all volume” could hide a boundary convention.**  A finite open
   kink chain is not specified by D16 alone.  Required repair: quantify frozen
   endpoint spins, fixed down-spin count, the compression, admissible
   `(A,B,μ)`, and compatibility along every cofinal sequence.
3. **MAJOR — the `O(N²)` sector must not be identified wholesale with the
   `O(N)` graph.**  Required repair: enumerate the full rectangle of three-wall
   states and prove its interior vertices are isolated under `P_3HP_3`; only
   the incoming cyclic component is the row/column union.
4. **MINOR — junction double counting.**  The left and right coordinate
   formulae coincide at `n=0`; the unitary must say this explicitly.
5. **MINOR — charge labels need a conserved-sector check.**  Show
   `(μ+1-c)-1=(μ-1-c)+1=μ-c`, not merely the signs of the two legs.
6. **MINOR — infinite operator hygiene.**  Establish boundedness on the graph
   and equality first on the finite-support core, then extend by continuity.

## Mechanical gates

- Green enumeration/locality run: `check_mq_e.py`, exit `0`.
- Red mutation (right wall pair shifted one bond): exit `1`, `RED-OK`.
- Recorded output: `CHECK_OUTPUT.md`.

## Post-repair adjudication

All six findings are addressed in `mq-e-proof.md` §§0--6.  No FATAL or MAJOR
remains on the projected incoming-component theorem.  The full-chain lift
remains outside this claim because `P_3H(1-P_3)≠0`.
