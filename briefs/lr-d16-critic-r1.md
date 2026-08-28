# Critic brief — (LR) for D16, r1

Read `briefs/critic-protocol.md` first; everything there binds.

**TARGET:** `theory/lr-d16.md` and `theory/checks/lr_d16_check.py`.
**VERDICT FILE (your only writable file):** `theory/verdicts/lr-d16-r1.md`.

**Prior context you must read:** `briefs/lr-d16-prover.md` (what was asked);
`definitions.md` **D27 verbatim** (LR1, LR2, LR3 and the convenience clause),
D26(INT), D16, D17, D13(a); `claims/CLAIMS.md` rows M-INDEX-spec (its
adjudicated scoping sentence is the register), M-INDEX-fin, K1--K4 (**K4 is
CONJECTURE — flag any reliance on it**), and the REFUTED M-INDEX-LA-strong;
`theory/memory-index.md` ⟨1⟩5 and ⟨1⟩7.⟨2⟩2; `theory/corner-b-draft.md` §1.2;
`theory/checks/memory_index_probe.py` (dressed-kink discipline: sharp kinks
FAKE a 5% violation, `dwmax=3` is spuriously perfect).

**Attack these surfaces first:**

1. **LR2 is first-moment only.**  D27 clause 2 is a first-moment
   nondemolition condition and explicitly does NOT assume operator asymptotic
   commutativity.  Check the proof does not smuggle in the operator statement
   — that would be strictly stronger and would make the result circular with
   what M-INDEX-spec is trying to avoid.  This is the single most likely
   defect.
2. **The frozen limit order.**  Infinite-volume dynamics FIRST, fixed-window
   time limits SECOND, spatial exhaustion LAST.  Hunt for any interchange,
   including implicit ones inside a Cesàro estimate that is uniform in `W`.
3. **LR3 uniformity.**  Tightness is `sup_m`, uniform over the exhaustion.
   Check the bound really is uniform in `m` and not merely fixed-`m` decay
   with an `m`-dependent constant.  This is where a plausible-looking proof
   usually fails.
4. **LR1's chosen sequence.**  The prover may choose `T_n`.  Check the SAME
   sequence works for every fixed `W` simultaneously, as D27 requires ("one
   sequence `T_n→∞` such that, for every fixed `W`…"), rather than a
   `W`-dependent subsequence — a diagonal argument needs the exhaustion to be
   countable and the extraction order to respect item 2.
5. **Integrability leakage.**  D16 is easy-axis XXZ.  Bethe is an ORACLE
   ONLY.  Flag any use of closed Bethe factorisation or of structure beyond
   two-body contact.
6. **The stretch section.**  If a general "gap + Lieb--Robinson ⟹ (LR)"
   statement is claimed, attack it as a separate artifact and be ruthless
   about whether the D16 proof's constants really only used those inputs.  If
   it is marked CONJECTURE, check that no earlier step borrows its strength.
7. **The checker.**  ED certificates must use dressed kinks; a sharp-kink
   initial state is a known artifact generator.  Verify the red modes fire
   for the stated reason, on copies.

**Deliverable beyond the standard format:** state explicitly, clause by
clause, whether LR1 / LR2 / LR3 are proved unconditionally for D16 — because
if all three are, M-INDEX-spec gains its **first unconditional dynamical
instance**, which is a headline. Do not certify that lightly, and say plainly
if only a subset survives.
