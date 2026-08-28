# Work order — D24(d)3 adjudication, repair round 2

You are the PROPOSER repairing the D24(d)3 ρ-normalization adjudication after
a **FAIL(F1,F2,F3,M1–M7)** verdict: 3 FATAL, 7 MAJOR, 6 MINOR, 4 NOTE.
Nothing was merged into `definitions.md`; the L4 file is still clean, and it
is your job to keep it that way until this converges.

## WRITING DISCIPLINE (non-negotiable)

Derive and **Write ONE section per response**.  Do not draft the whole
document in extended thinking before writing — that output is lost and the run
dies at the output cap.  The file on disk must be a valid partial deliverable
at every moment.

## READ FIRST, in order

1. `CLAUDE.md` (laws; **L6b Lamport**; L4 single-source; L10 honest verdicts)
2. `theory/verdicts/d24d3-adjudication-r1-critic.md` **IN FULL** — your work
   order.  Read **§1 "VERIFIED CORRECT — fence this, do not churn it"** FIRST:
   14 items are certified, including `Z = 2ρ = 2S`, the exact Ward residue
   `⟨h|Q₀†J⁻₀|h⟩ = 2i v_S(h)`, `∂δ/∂k_s = i/S`, and the ED reproduction.  Do
   not re-derive or disturb any of them.
3. `theory/verdicts/d24d3-adjudication-r1.md` (the artifact you are repairing)
   and `briefs/d24d3-adjudication.md` (its original work order)
4. `definitions.md` D24 in full; `notation.md` (the L4 symbol registry —
   **note it has NO row for `L`**, which is the real defect the r1 lane half-saw)
5. `theory/soft-index.md:161–162`, `theory/soft-current-recon.md` ⟨1⟩7,
   `theory/soft-index-b.md:808`, `paper/main.tex:524–527` — the four places
   that actually fix `L`'s provenance
6. `theory/verdicts/soft-index-adjudication-r1.md` §3.2 and §3.5 (BINDING —
   the r1 lane reversed both silently; see M5) and its ORCHESTRATOR ERRATUM
7. `claims/CLAIMS.md` rows ML5-A, ML5-B, **M-IDX-density** (whose load-bearing
   ANTISYMMETRY hypothesis the r1 merge dropped — M4), S2-2body-S

## THE STRATEGIC POINT — read this before writing anything

The critic agrees the **value** `L(0,h) = −iχ/(2ρ v_h)` is right; it
re-derived it independently.  What collapsed is the **story about where the
`1/(2ρ)` comes from**.

F2 is the finding that reorganises the whole problem: the corpus already
constructs `L` as the **reciprocal LSZ energy denominator**, in three places.
Since `v_h = ZJ sin h`, that construction *carries* `Z` and cancels it against
the residue's `Z` — so it **reproduces the frozen value** and forces the
defect.  The critic's conclusion, which you should take seriously rather than
argue with: **the missing `1/(2ρ)` does not belong to the flux factor at all.
It belongs to the soft-leg amputation** — an open lemma already named in
`soft-index-r1.md` F1(c)(i).

So the honest repair is probably NOT "derive a better flux constant".  It is:
split clause 3 into a *well-posed kinematic* half and a *named open lemma*,
and put the density where it actually lives.

The critic also names a **THIRD HORN** the original brief asked for and the r1
lane missed: *the bridge holds AND the class is empty ⇒ the matching is
vacuous ⇒ retire the value and keep 3a.*  Evaluate it seriously.  Retiring a
value and naming the open lemma is a better outcome than a fitted constant
(rk-light law 5), and `𝒮_W` nonemptiness is confirmed OPEN at every `ρ`.

## THE THREE FATALS

- **F1** — `(D24N.3)` is `0/0` at `k=0`, the only argument used; and the
  matching that supplies the value quantifies over `𝒮_W(ρ)`, which §4.4 itself
  declares possibly empty.  "Derived and not stipulated" is therefore false as
  claimed.  Fix demand: restore the `k ≠ 0` caveat, supply a genuine `C¹`
  extension to `k=0` (or admit there is none), and stop quantifying over a
  class you cannot show is inhabited.
- **F2** — the "L is never defined anywhere" premise is FALSE in substance
  (above).  Fix demand: state `L`'s actual corpus provenance, show explicitly
  that it forces the frozen value, and relocate the `1/(2ρ)` to the
  amputation.  Also: add the missing `notation.md` row for `L` — the genuine
  L4 gap the r1 lane's grep half-found by omitting `notation.md` entirely.
- **F3** — `Z := ⟨Ω|[S^+_x,S^-_x]|Ω⟩` is wrong as merged: `notation.md`'s `Ω`
  is the D6 spin-½ vacuum, so `Z ≡ 1` and the repair collapses; read generally
  it is site-dependent and equals `−2ρ` at the β tail; and bare `Z` collides
  with registered overload rule 9 (Pauli).  Fix demand: define the symbol
  correctly, at the right generality, under a name that does not collide, and
  register it in `notation.md`.

## THE SEVEN MAJORS

M1 (the refutation of both lanes is a strawman — lane B's operative factor IS
your own `1/Z`; the `(2ρN)^{-1/2}` route was the *S1-A critic's* counter-analysis,
not lane B's claim; and the ROLE header's "neither lane's workaround was
imported" is false, the repair is structurally lane A's); M2 (⟨1⟩3 carries no
load and its ⟨3⟩4 gives `Z^{-1/2}` on its own terms, contradicting ⟨1⟩5.⟨3⟩2);
**M3 (the checker — see below)**; M4 (quantifier over-reach in `ρ`; the merged
preamble drops M-IDX-density's load-bearing ANTISYMMETRY hypothesis); M5 (you
silently reversed binding §3.5 and §3.2 of the soft-index adjudication —
acknowledge both, and either comply or argue explicitly); M6 (missed lockstep
sites, including two in the OTHER L4 single source); M7 (merged 3a drops the
`k ≠ 0` caveat and asserts uniform `C¹` for a function defined only off the
zero set of `M_1^O`).

## M3 — THE CHECKER, and a standing campaign obligation

Your certificate shipped **two no-op gates** and an acceptance test that is
**deductively subsumed** by an earlier gate:
- D24N-C2's "soft-leg norm" half is `sites·two_s/sites − two_s ≡ 0` — it
  returns 0 for `two_s = 3.7`, `−5.0`, `10⁶`;
- `check_exponent_is_one` is `lstsq(x, x)` — design matrix identical to
  target, so "`p=1` to `1e-9`" is a tautology;
- D24N-C6 is implied by D24N-C4 (`|p−1| ≤ 0.0735 < 0.08`), and **all three of
  your reported mutants died at C4 and never reached the acceptance test**;
- deleting the `decision_band` key silently passes.

Read the new **"Standing checker obligations"** section at the end of
`briefs/critic-protocol.md` and satisfy every bullet: simplify each gate
symbolically, feed absurd inputs, report the exit **path** (which gate killed
each mutant, not just the exit code), mutate the **data** and not only the
code, and check for subsumption between gates.

## YOUR LANE (writable — nothing else)

- `theory/verdicts/d24d3-adjudication-r2.md` (create — the repaired adjudication)
- `theory/verdicts/d24d3-repair-r2-response.md` (create — one row per objection:
  FIXED / RETRACTED / DOWNGRADED / RESIDUE, with exact edit location)
- `theory/checks/d24d3_normalization_check.py` (repair in place)

**Do NOT edit `definitions.md`, `notation.md`, `claims/CLAIMS.md`, any shard,
or any existing verdict.**  All shared-file text goes in a MERGE PROPOSALS
section as exact replacement text — including the new `notation.md` row for
`L`.  The orchestrator merges only after a critic clears it.

## STRATEGY DIRECTIVE

Downgrade over ambition.  The best available outcome here is probably a
*smaller* claim than r1 attempted: a well-posed kinematic clause 3a, the
density relocated to a named open amputation lemma, `𝒮_W` nonemptiness
honestly still open, and the frozen constant retired rather than replaced.
That is a real result and it unblocks the corpus.  A second fitted constant is
not.

Work fully autonomously.  Do not ask questions.  ONE section per response.
