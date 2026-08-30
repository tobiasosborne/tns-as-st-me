<!-- LANE BRIEF Q4: ADVERSARIAL definitional audit. TJO directive
     2026-08-30: TJO is suspicious of the project's definitions. Your job is
     to be the hostile referee: hunt for definitions that do NOT correspond
     to the accepted continuum objects under any reasonable limit sequence.
     Finding a rat is success; finding none after a genuine hunt is also a
     result. No deference to the campaign's framing. Output:
     theory/lanes/reduction/q4-adversarial-defs.md, INCREMENTALLY. -->

# Q4: Hostile audit — which campaign definitions FAIL to connect to the accepted continuum objects?

## Inputs

- `definitions.md` IN FULL (D1–D31; read in chunks). `notation.md`.
- `claims/CLAIMS.md` — note which definitions carry proved theorems (those
  matter most; a bad definition under a PROVED label is the worst case).
- `refs/arxiv-1703.05448/soft_Arxiv_update.tex` (QED canon),
  `refs/arxiv-1411.5745` (memory), `refs/arxiv-1709.05018` (soft pion),
  `refs/arxiv-2201.01393` (type-B soft) — LOCAL TeX, quote with file+line.
- The four existing reduction analyses: theory/lanes/reduction/r1-smatrix.md,
  r3-wall.md, r2r4-ward.md and docs/reduction-limits.md — do not repeat
  their findings; go where they did not.

## Task

For EACH definition family below, attempt to break the correspondence: find
either (i) a limit-sequence obstruction (no sequence of limits takes the
discrete definition to the accepted continuum one), (ii) a wrong-object
identification (the discrete definition converges, but to something other
than what the continuum community means by that name), or (iii) a
degenerate-instance problem (the definition is nonvacuous only in regimes
with no continuum counterpart). Where you cannot break it, say what you
tried.

1. **D13's wall coordinate and its dresses.** Is the "windowed wall
   position" the discretization of ANY accepted continuum observable
   (soliton collective coordinate? Bondi-type falloff coefficient?), or a
   lattice-native bookkeeping device? The D13(c) trap paragraph (exact
   conservation of the first moment) is a known subtlety — does the
   continuum analogue of that trap exist (a conserved center-of-charge
   forbidding memory), and does the continuum literature evade it the same
   way (windowing/ordering) or differently?
2. **D26/D27 as a package.** The proved memory-index theorems consume
   D26(INT) + D27(LR). Adversarial question: is there any accepted
   continuum memory statement whose hypotheses discretize to (INT)+(LR),
   or are these hypotheses native to the lattice with the continuum
   analogue assumed silently? In particular: D27's double-Cesàro structure
   — exhibit a continuum system (free radiation) where the accepted memory
   exists but a naive transplant of D27 fails or is vacuous, if you can.
3. **D24's universality class.** The class 𝒮_W was engineered after the
   universality refutation. Does ANY accepted continuum soft theorem carry
   an analogous state-class restriction (the continuum papers' smooth
   wavepacket/compact-support assumptions), or is 𝒮_W doing work with no
   continuum counterpart — i.e., is the lattice soft "theorem" scoped to a
   class the continuum would consider unnatural? Quote the continuum
   papers' own state-class assumptions and compare honestly.
4. **D5/D12: the excitation ansatz as the definition of "particle".** The
   accepted soft theorems are about asymptotic Fock states. The campaign's
   legs are ansatz states, exact only for special models. Is there a
   definitional circularity risk — theorems about ansatz-defined objects
   that decouple from the model's true asymptotic states in exactly the
   regimes where the continuum comparison lives? The ansatz-vs-model gap
   is acknowledged in the brief (§5.2); your job is to say whether any
   PROVED row's definitional scope silently crosses it.
5. **The 3+1 QED stress test, definitional edition.** Pick the two
   campaign definitions you judge most load-bearing (suggested: D4's bond
   implementers, D26's circle charge) and transplant them to compact
   Hamiltonian lattice QED yourself (independent of lanes Q1–Q3, which run
   concurrently — do not read their outputs): does the transplant produce
   the objects QED people accept (boundary Gauss charges, integer electric
   fields), or something subtly different? Flag any mismatch of quotient
   structure (what is modded out), locality, or spectrum.

Close with a ranked list: every definitional rat found (severity: FATAL to
the continuum claim / MAJOR caveat / minor wording), and the definitions
that survived the hunt with a one-line reason each.

## Rules

Physics register; [physical argument]/[textbook] flags; quotes from local
TeX with file+line; you may NOT change any status or definition — you
report; no edits outside theory/lanes/reduction/; no bd operations; no
LEDGER edits.
