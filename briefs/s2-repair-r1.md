# Work order — S2 repair round r1 (codex #3, reserved budget)

You are the REPAIR prover for Theorem AC-EX-2M. Your shard
`theory/ansatz-scattering-2m.md` received critic verdict
`theory/verdicts/ansatz-scattering-2m-r1.md`: FAIL(O1–O6), 0 FATAL,
6 MAJOR (O1–O6), 9 MINOR (O7–O15), 8 NOTE (N1–N8). Your job: repair the
shard so a hostile r2 critic finds no surviving MAJOR. You are a
relentless prover: repair to the end, do not stop at a plan.

READ FIRST, in order:
1. theory/verdicts/ansatz-scattering-2m-r1.md  (the verdict — your work order)
2. briefs/soft-index-target.md (the campaign target — Lane S2)
3. theory/ansatz-scattering-2m.md (your shard, to be repaired in place)
4. briefs/s2-codex-prover.md (your original rules of engagement — still bind)
5. definitions.md (D1, D2, D12(a′), D28), notation.md, claims/CLAIMS.md
6. theory/ansatz-scattering.md (parent ACE machinery)
7. theory/ml2-completeness.md (ML2 — exact-match anchor)
8. refs/arxiv-1412.2970/Scattering_spin-AHP1.tex (cite by section/equation;
   O5's fix ports Theorem `Haag-Ruelle`'s final clause from here)

YOUR WRITABLE LANE: `theory/ansatz-scattering-2m.md` (repair in place) and
`theory/ansatz-scattering-2m-r1-response.md` (NEW: the objection-by-
objection disposition table — for each of O1–O15, N1–N8: ACCEPTED/
REBUTTED, what changed, where). Nothing else. Do not touch definitions.md,
claims/CLAIMS.md, notation.md, theory/checks/, numerics/.

## Non-negotiable constraints

- **PRESERVE VERBATIM the D31-C2 transfer-gap clustering derivation**
  (⟨1⟩3) — it survived independent recomputation and is the lane's real
  advance. Exception: apply O8's fix (replace the r^{1/2}/condition-number
  gloss in ⟨1⟩3.⟨2⟩2 by the V_w Stinespring-isometry argument, with the
  norm-equivalence clause) — that is a strengthening of the same
  derivation, not a change to its statement.
- The critic's FIX DEMANDs are the default repair; if you REBUT an
  objection instead, the rebuttal must be a computation, not prose, and
  goes in the response doc.
- Downgrade over ambition. The verdict's per-objection SURVIVING WEAKER
  STATEMENTs are your floor: never land below them, never claim above
  what you actually prove.
- Lamport L6b format throughout; every leaf cites a D-number, claim id,
  named computation, or refs/ file+location. From-memory citations FATAL.

## The six MAJORs — repair directives

- **O1 (fence parameters).** Replace ⟨1⟩2.⟨2⟩1's parameter enumeration:
  constants may depend on ε_v, ε_0, d_B, η_inel AND the Schwartz seminorms
  sup_{j≤N}‖∂^j F‖_∞ of the packet amplitudes — which is where the ε→0
  divergence lives. Display the ε^{-N} growth of C_N for f_ε once.
  While there, incorporate N2 (favourable): along k_s→0 at fixed k_h,
  d_B → J sin²(k_h/2) > 0, ε_v→|v_h|, η_inel=+∞; only ε_0 degenerates
  and ε_0 appears in no estimate.
- **O2 (interface clause 5 = smuggled soft-leg LSZ).** Split clause 5
  into (5a) interface convention (which pairing is compared) and (5b) a
  NAMED hypothesis (ACE2M-LSZ): at each fixed ε>0 the charge-created
  soft leg Q[f_ε]Ω_A equals the D31(3) filtered one-magnon vector for
  profile f_ε up to an on-shell-null remainder. PROVE (ACE2M-LSZ) on D6
  (the critic says one line: J^-[f]Ω = Σ_x f(x)|x⟩ is literally the
  one-magnon packet in the D6 bases — verify and display it). List it as
  an unproved hypothesis in the abstract D31 setting. HONEST STATUS must
  say plainly: the wave operators enter (A2M.3) only through (ACE2M-LSZ).
- **O3 ((SR) quantifier incoherence).** Restate (ACE2M-SR) as posed after
  operations one and two only (N→∞, t→±∞), with j an EXPLICIT index of a
  (W_j, σ_j) exhaustion sequence; replace the ⟨1⟩9.⟨2⟩2 display's
  lim_{σ↓0}lim_{W↑ℤ} by lim_j; add a clause defining A_j(0) (continuous
  extension of the fixed-j datum, stated as part of (SR)); add one
  sentence conceding (SR) is uniform in j down to ε=0 and is therefore a
  genuine (non-Cook) soft-uniformity hypothesis.
- **O4 (the D6 (SR) instance).** Follow the critic's option (ii) unless
  you can genuinely do (i): downgrade ⟨1⟩9.⟨2⟩3 to "(SR) holds for the
  j-independent infinite-chain amplitude on D6 (S2-2body's uniform-
  compact-hard C² statement); the (W,σ)-uniform version is open on every
  model, D6 included", and mark (A2M.3)'s non-vacuity claim accordingly.
  If you attempt (i) — explicit (W,σ) bookkeeping on D6 with uniform-in-j
  relative compactness + equicontinuous ∂_ε in L²(I) — time-box it; a
  failed attempt is recorded in HONEST STATUS, not left half-claimed.
- **O5 (completeness register breach).** Default repair: DELETE the word
  "entire" from ⟨1⟩7.⟨2⟩4 and state only what (A2M.2) already says (a
  fixed packet range lies in the matching part of ML2's scattering
  summand). If you instead attempt the full repair: port the final clause
  of source Theorem `Haag-Ruelle` (creator-choice independence under
  disjoint velocity supports) as a numbered step with hypotheses checked
  against D31, AND handle the chaining across non-nested window pairs AND
  the ML2 K-folding (c<0, reversed labelling, odd-r anti-periodicity).
  Partial repair is worse than deletion — the shard must not end stronger
  than its claims row. Either way ⟨2⟩4 and the claims row must agree.
- **O6 (checker scope).** In the CHECKER SPEC section: rename A2M-C1's
  certified scope to "the connected two-point transfer-matrix identity
  with fixed-point subtraction on one model"; ADD (i) a support-length
  row (w_C, w_D ∈ {1,2,3}, gate: |conn|/(‖C‖‖D‖λ̃^{d_sep}) bounded
  uniformly in w) with its own red mutation, (ii) either a model with a
  Jordan block at modulus λ_E or an explicit statement that the
  Jordan-safe form is uncertified; state that the checker must use
  raise/sys.exit, never bare assert (python3 -O strips asserts).
  You write the SPEC only — do not create files under theory/checks/.

## The MINORs and NOTEs

Apply every FIX DEMAND of O7–O15 (exponent 4−N in ⟨1⟩6.⟨2⟩2; O8 as above;
drop D17 from ⟨1⟩2.⟨2⟩1; drop or justify D2(a); fix the two claims-row
lockstep drifts of O11 IN YOUR MERGE PROPOSALS TEXT (you cannot edit
CLAIMS.md — fix the proposed row text in your shard's MERGE PROPOSALS
section); add the domain clause citing D31(3) in ⟨1⟩5.⟨2⟩1; add the
|S|=1 clause via ML2 (18); fix the O14 sentence to "no ε→0 limit is taken
inside the Cook integral; ε enters as a fixed packet parameter with
constants diverging as ε↓0"; display a_{i,b}(n)=τ_n(a_{i,b}(0)) in the
D31(3) proposal). Address N1 ("isolated within the charge-one sector"),
N3 (mark the forward reference non-circular), N4 (matrix-valued band:
either m=1 restriction where velocities are used or eigenvalue-branch
definition), N5 (rephrase the HONEST STATUS collision). N2 is folded
into O1. N6/N7/N8 need no action beyond not regressing them.

## Output contract

- Repaired shard stays 200–500 loc-ish (L2); if repairs push it over,
  prefer tightening prose over splitting mid-repair (splits are
  post-promotion hygiene).
- `theory/ansatz-scattering-2m-r1-response.md`: one table row per
  objection (id, ACCEPTED/REBUTTED, disposition, shard location of the
  fix), then any rebuttal computations in full.
- Self-status stays SKETCH; only the L6 loop promotes.
- Work fully autonomously. Never ask questions. Never wait.
