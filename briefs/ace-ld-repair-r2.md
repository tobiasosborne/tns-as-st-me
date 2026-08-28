# Work order — ACE-LD repair round 2 (the reroute)

You are the PROPOSER repairing `theory/ace-ld.md` after **FAIL(F1,M1–M6)**:
1 FATAL, 6 MAJOR, 7 MINOR, 4 NOTE.

**Read the verdict's own framing before you despair: this round produced a
result, not a failure.**  Your obstruction SURVIVED an adversarial attack and
came back STRONGER, and the critic handed you the reroute.  The job now is to
write the true statement, not to rescue the old one.

## WRITING DISCIPLINE (non-negotiable)

Derive and **Write ONE Lamport section per response**.  Never hold more than
one section's derivation before committing it to disk.  The file must be a
valid partial deliverable at every moment.  This has killed three runs in this
campaign across two model families.

## READ FIRST

1. `CLAUDE.md`; `briefs/critic-protocol.md` (esp. **Standing checker
   obligations** — your certificate violated four of the five)
2. `theory/verdicts/ace-ld-r1.md` **IN FULL** — your work order
3. Your own `theory/ace-ld.md` and `theory/checks/ace_ld_check.py`
4. `definitions.md` **D13(a)** (the ε-version is *its* own statement — this is
   the key text), D18(AD3)/(AD4), D27(LR1–LR3), D28
5. `theory/ansatz-scattering.md` ⟨1⟩7.⟨2⟩2 — **what the ordered limit actually
   consumes**; `claims/CLAIMS.md` rows AD3-ex, AC-EX, M-INDEX-fin, M-INDEX-spec

## WHAT SURVIVED (keep, do not churn)

- **ACE-LD-abs**, the abstract N-channel lemma — verified.
- **ACE-LD-nec** — verified.
- **ACE-LD-obst** — CONFIRMED and STRENGTHENED.  The `ν = ±2s|W|` growth is
  real: `c₀` cancels identically in `q_+ − q_− = 2s(b−(a−1)) = 2s|W|`, and
  M-INDEX-fin's cancellation is what makes `ν` an *integer*, not what makes it
  *bounded*.  The critic reproduced every clause of ⟨1⟩6.⟨2⟩2 to four digits,
  including your self-declared soft spot ⟨3⟩1 at defect `2.4e-09`.

## THE FATAL AND THE REROUTE

**F1.**  `(E-TAIL)` is *equivalent* to `χ=1` `S^z`-product vacua (two-line
Cauchy--Schwarz), and D16's kink band is **exactly flat** by ED
(`‖H_kink|K(z)⟩‖ ≤ 2.5e-16`, ground energy 0 in every `S^z` sector), so
`v_K ≡ 0` and `(V-ch)` fails there.  **`(E-TAIL) ∧ (V-ch)` is EMPTY on every
instantiated model.**  Also false: ⟨1⟩6.⟨2⟩3's "on the fixed-packet class of
D28 the kink is ballistic" — D28(4) constrains only `v_M − v_K`, so D28's
class *contains* the static-kink class.
FIX DEMAND: delete both hypotheses and the ballistic sentence.  Do not
replace them with a repaired pair — see the reroute.

**M2 — your obstruction is OVER-hypothesised, and that is good news.**  LR3
failure follows from D27's own first-moment identity alone
(`LR3 ⟹ sup_m Σ|ν|p_{W_m} < ∞`), needing only the **mean tail density** — no
`(E-TAIL)`, `(V-ch)`, `(V-in)`, no `σ_L ≠ σ_T`, no ⟨3⟩1.  **Restate the
obstruction at that strength.**  It becomes cheaper, more general and harder
to dismiss.

**THE REROUTE — this is now the shard's main positive content.**  Prove
D13(a)'s own ε-version:

  `limsup_t ‖(Q̂_W − q_ch)P_chΨ_t‖ ≤ C λ̃^{d_W}`

It is compatible with LR3, and it is what `ansatz-scattering.md` ⟨1⟩7.⟨2⟩2
**actually consumes in the ordered limit** — so it does the job (AD3-ex) was
introduced to do, without being false.  The critic measured the decay on D16's
exact zero modes: `min_q ‖(Q̂_W−q)Ψ‖ > 0` at every `W`, decaying exactly like
`q^{d_W}` with ratios `0.2089, 0.2085, 0.2041` against `q = 0.208712`.  Prove
it, name it, and state precisely what it does and does not give.

**M5.**  You discharged the **vacuum**-eigenstate reading; D18(AD3) and
M-INDEX-spec use the **kink**-eigenstate reading.  Say which reading each
statement is about, at every occurrence.

**Also:** MP-1's unscoped "on D28 packets" wording would wrongly read as
pre-empting the separate (LR)-for-D16 lane (bd `tns-xf4`), which is OUTSIDE
your obstruction's class precisely because D16's kink band is flat.  Scope it
before it can be merged.

## THE CHECKER — you violated four of five standing obligations

- LD-C5 violates its own `(V-in)`, never produces the `ν=0` atom it certifies,
  and **has no red mode at all**;
- LD-C3 passes with a constant **5× smaller** than the lemma's;
- `--red-coset` is **bit-identical** to a 10× constant shrink and blind to
  cosets;
- implementing your own §5 prescription (`d_ch` from the model spectrum) makes
  `--red` exit **2**.

Rebuild it against every bullet in the protocol's standing-obligations
section: symbolic simplification, absurd inputs, **exit paths per red mode**,
data mutation, subsumption, and *every gate must have a red mode that reaches
it*.  Add a gate for the ε-version's measured decay ratio.

## LANE (writable — nothing else)

`theory/ace-ld.md`, `theory/ace-ld-r2-response.md` (create, one row per
objection), `theory/checks/ace_ld_check.py`.  No shared files; MERGE PROPOSALS
only.  Do not git commit.

## STRATEGY

The honest shard that comes out of this is: an abstract lemma, a **sharpened
negative result** about the unsubtracted window charge on ballistic classes,
and a **positive ε-version** that reroutes the edge.  That is a better
artifact than the one you set out to write.  Claim exactly it.

Work fully autonomously.  Do not ask questions.  ONE section per response.
