<!-- ROLE: PROPOSER's repair response, round 4 (the closing round), to
     theory/verdicts/d24d3-adjudication-r3-critic.md FAIL(F1,M1-M5).
     Companion to theory/verdicts/d24d3-adjudication-r4.md.
     Work order: briefs/d24d3-repair-r4.md.  Writable files of this lane:
     the r4 verdict, this file, theory/checks/d24d3_normalization_check.py.
     No shared file was edited; no git commit. -->

# r4 repair response — disposition of every r3-critic item

**Eighteen items: 1 FATAL, 5 MAJOR, 8 MINOR, 4 NOTE.  Disposition: 15
FIXED, 1 FIXED WITH A STATED DEVIATION from the critic's suggested
mechanism (m2), 2 NOTED with no action required (n1, n3); n2 and n4
required one sentence each and got it.  One repair goes further than
demanded and demotes a gate this lane itself shipped (M2 → the derived
exponent comparison is provably subsumed and is now DISPLAY, r4 §6.1).**

Nothing in this response contradicts r1's V1–V14, r2's W1–W18, or r3's
X1–X15; those are fenced and were not re-derived.  The r3-critic's two
rulings in this lane's favour (X7 status call; r1 M3(c)(iii) declination
accepted) are received and closed.

---

## 1. Headline answers

1. **Which horn of the trilemma?**  None of the three as stated — the
   critic's own FIX DEMAND, adopted in full: clause (d)2's residue is
   declared, in displayed text, to be quoted in the **charge-created**
   normalisation (`ml4-ward-reduction.md` (11), D24N-C3), while the
   amplitudes and `E^O_desc` stay in (b)'s; the "mixed reading" is
   promoted from a forbidden accident to the convention's two-anchor
   structure.  Costs paid and displayed (r4 §1.4): the one-convention
   preamble is struck as false; clause 2's invariance is retracted
   (clauses 1, 4, 5 invariant; clause 2 transforms as `c′/c` and is the
   convention's second anchor); and `Z_ρ^{-1/2}`-from-leg-conversion
   stops being an "independent mechanism" — it is the convention's own
   mismatch, derived in one step (r4 §1.3).  The literal horn (class
   provably empty again), the shape horn (r2-F1 resurrected) and the
   normalisation-fixing horn (`𝔞_leg = 1` by construction, frozen clause
   restored) are each refused with the critic's stated cost quoted.
2. **Does the `Q^-_k|Ω⟩ = √(Z_ρ)|k⟩` narrowing survive?**  **Yes, and no
   longer conditionally.**  The critic's X2 fence made the narrowing
   conditional on exactly the reading r4 now adopts explicitly, so the
   conditional discharges: AMP's residual content is a second
   `Z_ρ^{-1/2}` from a non-leg mechanism.  Its one soft spot (m1) is
   closed: the descendant leg's `‖Q^-_q|h⟩‖² = Z_ρN − 2` is now a gate
   (D24N-C8(ii)), with the r3 overclaim shipped as its red mode
   (`--red-descnorm`, dies with error exactly `2.000e+00`).
3. **What happened to `EXPONENT_FIT_BAND`?**  Deleted.  The band is
   derived from the same quoted-error column
   (`0.8805·log(1/(1−0.0479)) = 0.0432`), the four "no acceptance
   constant" layers are retracted and superseded (r4 §0.2), and the
   derivation turned out to be a subsumption proof: a fitted-exponent
   gate calibrated to the data's own error can never fire on data that
   passes the calibrated acceptance gate, so the comparison is demoted
   to DISPLAY (the C5/X11 treatment) and the symbolic pin remains the
   gated content.  `m_shift34` and `m_shift40` — both inside the data's
   stated uncertainty, both rejected by r3 — now pass; `m_shift45` dies
   at the acceptance gate at the critic's own boundary number
   (`0.0482 > 0.0479`).

---

## 2. Disposition table

| id | severity | disposition | where |
|---|---|---|---|
| **F1** | FATAL | **FIXED** — the residue's normalisation stated in displayed text in clause (d)2 AND in §5.0′; preamble blanket sentence deleted; invariance list corrected (1, 4, 5; clause 2 as `c′/c`, the second anchor); ⟨1⟩4 re-derived in one step from the numerator/denominator mismatch; trilemma resolved explicitly with each horn's cost; the narrowing's survival stated under the adopted reading | r4 §1, §5.0′, §5.2′ |
| **M1** | MAJOR | **FIXED** — D12(b) citation struck; kernel construction cited to D24N-C8 in the spin-`S` register; `ML1` (CONJECTURE) named as the gap off that family, in the definition AND in the `𝔞_leg(ρ)` row; the two `D24(b)` citation sites (ml4-ward:63–68 wider-freedom; ansatz-scattering-2m ⟨2⟩5 `S_phys`-valued) added to the blast radius with same-commit notes; §5.0′ says it narrows the ML4-admissible class; the honest sentence recorded ("consistent … only because every existing use sits at `ρ = 1/2`") | r4 §2, §5.0′, §5.4a′, §5.5′ item 12 |
| **M2** | MAJOR | **FIXED, further than demanded** — the critic offered derive-or-declare; r4 derives, retracts all four layers, AND demotes: the derived band proves the fitted-exponent comparison deductively subsumed by the acceptance gate (a finding on this lane's own artifact, reported per the standing obligations), so it is DISPLAY now.  Declared-constants inventory in the docstring | r4 §6.1; checker |
| **M3** | MAJOR | **FIXED** — the `0 ≡ 0` orthogonality sub-gate and the constant-true `require(len(...) >= 3)` deleted; replaced by the critic's suggested "test that can fail": two-magnon SAME-total-momentum overlap `= −2N·Z_ρ` (closed form derived on paper, ladder-free integer vs ladder-dependent measurement; moved by `--red-ladder` at `2S ≥ 2`, killed by sign-flip mutant `c4_overlapsign`); `cB_onek` honestly recorded as not catchable as wrongness (coverage shrink); r3's "all three closed" retracted — m4(ii) closed only now | r4 §6.2; checker C2 |
| **M4** | MAJOR | **FIXED** — all 18 sites enumerated with per-site disposition (5 TRIANGLE renames as ruled MERGE; 13 licensed bare by the critic's own cheapest fix, one clause in the `𝒮_W(ρ)` row); `definitions.md`/`notation.md` mutually consistent after the commit | r4 §3, §5.4b′, §5.5′ item 10 |
| **M5** | MAJOR | **FIXED** — AMP restated per the critic's (c): scoped to `𝒮_W(ρ) ≠ ∅` AND kernel-existence (currently the spin-`S` family); "UNCONDITIONALLY — without assuming a class member" struck; D24-VAL's vacuous-or-unknown sentence added; the ⟨1⟩4 fence kept verbatim with the §1.3 one-step pointer; what still distinguishes AMP from D24-VAL (drops (α)) stated, per the critic's own record | r4 §4, §5.3c′ |
| **m1** | MINOR | **FIXED** — ⟨1⟩4.⟨3⟩1 superseded: exact on the vacuum leg; descendant leg `Z_ρ − 2/N` per site, `√Z_ρ` only in the LSZ limit, correction `≤ 1/(Z_ρN) ≈ 10^{-2}` at `N = 60` vs `5–12×` margins; AND the identity gated (D24N-C8(ii)) with red mode `--red-descnorm` | r4 §1.3 ⟨3⟩1, §6.3 |
| **m2** | MINOR | **FIXED WITH A STATED DEVIATION** — the one-sided guard is now two-sided via a per-row corrupted-entry guard (declared multiplier `ROW_BAND_SANITY = 3.0`, guard-only, true-data margin `2.29×` vs `3×`); the critic's mutant dies at `3.78×` with the ratio in the message.  The critic's per-spin-band mechanism was NOT taken, with the reason recorded: it would reject the `−3 %` calibration mutant at `S = 1` (own error `2.4 %`), reversing behaviour r2-critic M3(b)(iii) demanded and X13 certified.  Residual (a `< 3×` inflation still loosens proportionally) stated, with why no conclusion is exposed | r4 §6.4; checker `derive_accept_band` |
| **m3** | MINOR | **FIXED** — explicit `notation.md` application order supplied (b′, a′ at 258; c at 244; f after 145; e at 123–130; d at 91–98 — descending), with the note of why the r3 written order broke two anchors; `claims/CLAIMS.md` order also stated | r4 §5 Mechanics, §5.5′ item 11 |
| **m4** | MINOR | **FIXED** — both sites added to the blast radius with same-commit citation notes; §5.0′ carries the narrows-ML4 sentence; the critic's honest sentence quoted verbatim | r4 §2, §5.5′ item 12 |
| **m5** | MINOR | **FIXED** — "every gate is reachable" superseded by "every gate offered as evidence (C2, C3, C4, C6-part-1, C6-pin, C8) is reachable; C1, C5, C7 and the two DISPLAY lines are labelled GUARD/DISPLAY precisely because they are not" | r4 §6.5 |
| **m6** | MINOR | **FIXED** — the H8 price list gains the `𝔠_h`-undecidability sentence (every `M_1^O ≠ 0` source's ML5-A test undecidable until AMP or `tns-axg` closes); D24(e) decidability preserved (W14) noted | r4 §7 (H8), §5.5′ item 14 |
| **m7** | MINOR | **FIXED** — one character: `n ≤ 2S` → `n ≤ 2S−1` in the superseded r3 §0 prose (`n = 2S` is `S^-\|{-S}⟩ = 0`); code was always right | r4 §0.2, §6.5 |
| **m8** | MINOR | **FIXED** — `TRIANGLE.md:216–218` added to the same-commit list with the one-clause scoping the paper's `:524–527` gets (`2` in the D6 register; `2𝔞_leg(ρ)` on the general class, OPEN) | r4 §5.5′ item 13 |
| **n1** | NOTE | **NOTED, no action** — "the sharpest thing in the round is generous" is accepted; r4 does not re-inflate D24N-C8's novelty and describes its content as the critic did (direction + standard diagonalisation; the *use* is what is new) | — |
| **n2** | NOTE | **FIXED (one sentence)** — §4.3 item 3 now records that `main.tex:244–249`'s identification silently needs `𝔞_leg(1/2) = 1`, supplied by no L4 file, and why the Letter nevertheless stands (contact route, X9) | r4 §7 |
| **n3** | NOTE | **NOTED, no action** — the `1e-10` thresholds stand; the critic's own computation (residuals `1e-15`, nearest competitor `O(1)`) is cited in the declared-constants inventory | checker docstring |
| **n4** | NOTE | **FIXED by the M2 repair** — the `−3.4 %` neighbour no longer dies on an undeclared constant, so `m6_shift30`'s demonstration now proves exactly what §7.2 said it did; both mutants and `m_shift40` are in the r4 mutant table | r4 §6.5 |

---

## 3. The one deviation, in full (m2)

The critic's fix demand for m2 was "per-spin band from the rows at that
spin, aggregated to match the gated statistic; and cap or flag any band
more than (say) 2× the median".  r4 takes the cap (at `3×`, per-row) and
not the per-spin banding, and the reason is a direct conflict with an
already-certified behaviour: under per-spin bands, the `−3 %` uniform
shift (`m6_shift30`) dies at `S = 1`, whose own quoted error is `2.4 %`.
That mutant's PASSING is the demonstrated calibration fix that r2-critic
M3(b)(iii) demanded, r3 shipped, and the r3 critic certified (X13:
"passes exactly as §7.2 says and for exactly the stated reason").  A
repair that un-fixes a certified fix to close a MINOR is the wrong
trade; the corruption channel the critic actually exhibited (one
inflated entry, silent `1.65×` loosening) is closed by the per-row guard,
which kills the critic's exact mutant at `3.78×` the median with the
ratio printed.  The choice of `3×` over the critic's "(say) 2×" is
forced by the true data itself: the genuine worst row is already `2.29×`
the median (the `S = 2`, `k_h = 2.4` row), so a `2×` cap rejects the
shipped data.  `3.0` is declared in the constants inventory as a guard
multiplier that can only reject.  If the r5 critic prefers the per-spin
mechanism WITH a recalibrated `m6` expectation, that is a coherent
alternative — but it must be adjudicated as a reversal of X13, not
slipped in.

---

## 4. Found by this lane, on itself (volunteered)

1. **The derived exponent gate is provably a no-gate.**  Deriving the
   exponent band per the critic's M2 demand yields a two-line proof that
   the fitted-exponent `require` could never fire on data that reaches
   it (r4 §6.1).  r3's version did fire — because it was miscalibrated.
   Rather than ship a fifth gate-that-cannot-fail (the corpus is at
   five), the comparison is demoted to DISPLAY with the proof printed in
   the docstring, and the symbolic pin keeps C6 part 2 falsifiable
   (`c2_wronglaw` dies there).  What would restore an independent
   exponent gate: a fifth density, or a tighter error column.
2. **The two-magnon overlap's momentum pairing is load-bearing.**  The
   replacement gate works only because `k` and `k + π` give the SAME
   total momentum `2k mod 2π`; any distinct-total-momentum pairing
   reproduces the r3 no-op by translation invariance.  This is stated in
   the code comment so the next editor cannot "generalise" it back into
   a tautology.
3. **`m2_shift799` label.**  r4's mutant table reproduces r3's `−7.99 %`
   mutant under the name `m2_shift799`; it dies at C4 with the same
   `0.0839` (W4/X13 continuity).
4. **Checker length.**  727 loc, 227 over the L2 guideline (r3: 559,
   disclosed).  The excess is the retraction-bearing docstring and the
   two new sub-gates; the algebra/data split remains the right refactor
   and remains filed rather than done, because this round's brief is to
   close, not redesign.

---

## 5. What an r5 critic (if any) should attack first

1. §1.1's claim that the two-anchor convention is consistent — i.e. that
   clause 2 read charge-created plus §5.0′'s `c′(0)/c = 1` fixes the
   bookkeeping without over- or under-determining it.  The lane believes
   this is now airtight (clause 2 involves no asymptotic soft leg, so
   the two fixings act on different objects); it is the round's one new
   structural claim.
2. The subsumption proof in `derive_exponent_band` (three lines; if the
   inequality chain has a hole, the demotion was premature — though the
   gate would then need its OWN calibration defense, which is M2 again).
3. The two-magnon closed form's combinatorics (`−2N·Z_ρ`), §6.2 — one
   sign error there and C2(v) is certifying the wrong integer (the
   sign-flip mutant dies, so the code and the form at least agree
   against mutation).
4. Whether the licensing clause (§5.4b′) is too permissive — it legalises
   bare `𝒮_W` in five files; if the critic judges any of the 13 sites
   density-MATERIAL, that site needs the rename instead.
