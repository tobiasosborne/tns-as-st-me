# Critic brief — D24(d)3 adjudication, round 2 (adjudication round)

Read `briefs/critic-protocol.md` first — including its **Standing checker
obligations** section — everything there binds.

**TARGET:** `theory/verdicts/d24d3-adjudication-r2.md`,
`theory/verdicts/d24d3-repair-r2-response.md`,
`theory/checks/d24d3_normalization_check.py`.
**VERDICT FILE (your only writable file):**
`theory/verdicts/d24d3-adjudication-r2-critic.md`.

**This is an ADJUDICATION round.**  Your priors are
`theory/verdicts/d24d3-adjudication-r1-critic.md` (FAIL: 3 FATAL, 7 MAJOR, 6
MINOR, 4 NOTE) and the r1 artifact.  Verify each claimed disposition by fresh
recomputation; attack what CHANGED; do not re-litigate what already passed.
**Do not churn §1 of the r1 critic verdict** — its 14 fenced VERIFIED CORRECT
items stand.

**Stakes:** if you PASS this, it merges verbatim into `definitions.md` and
`notation.md`, both L4 single sources, plus a new CONJECTURE row in
`claims/CLAIMS.md`.  The r1 attempt would have installed a contradiction with
three corpus statements.  Be correspondingly hostile.

## What the repair claims to have done

It took the **third horn**: clause 3 is SPLIT into (3a) a well-posed kinematic
hypothesis — `L` as the descendant quotient for `k ≠ 0` with a displayed `C¹`
extension — keeping the **frozen** value `−iχ/v_h`, plus (3b) a normalisation
split `L(0,h) = 𝔞_leg·(−iχ/v_h)`.  The `1/(2ρ)` is relocated into the
soft-leg amputation constant `𝔞_leg`, whose value the definition explicitly
does NOT fix; that value becomes the named open lemma **AMP**.  The matched
value survives only as a new CONJECTURE row **D24-VAL**, a conditional
implication (bridge ∧ member-exists ⇒ `𝔞_leg = 1/(2S)`) scoped to
`ρ = S ∈ {1/2,1,3/2,2}`.  Disposition count claimed: 20/20 — 18 FIXED,
1 RETRACTED (M1), 1 DOWNGRADED (M2), 0 residue.

## Attack these, in priority order

1. **Is the split honest, or does it relabel the stipulation?**  The frozen
   value stays in the kinematic factor and the correction moves into a
   constant nobody can compute.  Check that this is a genuine relocation
   forced by F2's provenance argument, and not a way to keep the number while
   moving the blame.  Specifically: does anything in the corpus now *require*
   `𝔞_leg = 1` implicitly (which would resurrect the defect), and is D24(d)'s
   class still nonvacuous as a *hypothesis class* with `𝔞_leg` free?
2. **D24-VAL as a CONJECTURE row.**  A conditional implication whose
   antecedent includes "a member exists" is at risk of being **vacuously
   true** — exactly the vacuous-truth pattern this campaign has already been
   burned by (see the S2 lane's R2-O2).  Is D24-VAL contentful?  Does its
   scoping to `ρ = S ∈ {1/2,1,3/2,2}` breach the standing fence that `ρ` is a
   DENSITY and `s` a SITE SPIN (M-IDX-density's verbatim scoping sentence, and
   the r2 objection-1 fence)?  The r1 critic's M5 faulted exactly this
   `ρ = S` register move as reversing binding adjudication §3.5 — check
   whether the repair complied or repeated it.
3. **The three FATALs.**  F1 (`0/0` at `k=0`; quantifying over a possibly
   empty class) — is the `C¹` extension real and displayed at the point of
   use, and has the reliance-fence breach gone?  F2 (provenance) — is it
   adopted in full, and does the shard now state that the corpus construction
   *forces* the frozen value?  F3 (`Z` ill-defined and colliding) — verify
   `Z_ρ`, `𝔞_leg`, `E^O_desc` are genuinely collision-free against
   `notation.md`'s overload rules, and that the missing `L` row is supplied.
4. **THE CHECKER — the standing obligations apply, and the repair claims to
   have satisfied them.  Verify that claim yourself; do not accept it.**
   It reports: green exit 0; `--red-frozen`/`--red-power`/`--red-halfpower`
   die at **C6** (the acceptance gate, now reached); `--red-ward` dies at C3;
   data mutants die at C4; and the decisive one — a **−6% uniform shift passes
   C4 (0.064 < 0.08) and dies at C6 (0.060 > 0.02)**, which is offered as
   proof the acceptance gate is no longer subsumed.  Reproduce that on a copy.
   Then go further: the repair discloses that **`ACCEPT_BAND = 0.02` is
   registered THIS round, not pre-registered** — assess honestly whether 0.02
   was chosen after seeing the data, i.e. whether the acceptance test is
   tuned to pass.  Also re-audit the rebuilt C2 (which replaced a `0 ≡ 0`
   no-op) and the sympy C6-symbolic (which replaced `lstsq(x,x)`) for the same
   disease in new clothes, and check the self-declared subsumption of C5.
5. **Lockstep and blast radius.**  r1's M6 found missed lockstep sites
   including two in the OTHER L4 single source.  Grep them all yourself:
   `ml5-universality.md`'s eight step addresses, `TRIANGLE.md`, `notation.md`,
   `paper/main.tex:244` and `:524–527`, D24(e), `ml4_check.py`, the oracle
   rows.  Confirm each claimed "does NOT change" by grep, not by assent.

## Deliverable beyond the standard format

A clause-by-clause **MERGE / HOLD** on every merge proposal —
`definitions.md` D24(c), the D24(d) preamble, 3a, 3b, clauses 1/4/5; the
`notation.md` rows for `L`, `Z_ρ`, `𝔞_leg`, `E^O_desc`; the `claims/CLAIMS.md`
ML5-B re-scope and the new D24-VAL row.  For MERGE, confirm verbatim
appliability and that the "five-condition" count and `paper/main.tex:244`
remain correct.  For any HOLD, name the missing step.  State explicitly
whether `𝒮_W` nonemptiness is still open, whether bd `tns-axg` may be
unblocked, and whether bd `tns-iu5` may now be closed or must stay open on the
AMP lemma.
