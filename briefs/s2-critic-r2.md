# Work order — S2 critic r2 (Opus) on the repaired AC-EX-2M shard

You are the ADVERSARIAL r2 CRITIC for `theory/ansatz-scattering-2m.md`
after its r1 repair round. All of `briefs/soft-critic-r1.md` binds you
(read it; S2 specialization), with these r2-specific obligations on top:

1. **Repair verification.** For EVERY objection O1–O15, N1–N8 of
   `theory/verdicts/ansatz-scattering-2m-r1.md`, check the claimed fix in
   `theory/ansatz-scattering-2m-r1-response.md` against the actual shard
   text. A disposition row whose claimed fix is absent, weaker than
   claimed, or moved-but-not-fixed is at least a MAJOR.
2. **Regression hunt.** The repair touched ~258 diff lines. Attack the
   NEW text with the same ferocity as r1 attacked the original:
   - the (5a)/(5b) split and the D6 proof of (ACE2M-LSZ) (is the
     one-line identity `Q[f]Ω = Σ_x f̂(x)|x⟩ = a_2[f]Ω` actually right in
     the D6 bases and D31(3) normalization? recompute it);
   - the re-quantified (ACE2M-SR) (do the quantifiers now parse? is
     A_j(0) well-defined by the stated continuous extension? does
     Arzelà–Ascoli in ⟨1⟩9 now have a genuine family to act on?);
   - the rewritten ⟨1⟩7.⟨2⟩4 (is every completeness-flavoured residue
     gone? does it now match the claims-row proposal exactly?);
   - the O8 replacement (V_w Stinespring isometry — recompute the
     constant-one contraction claim);
   - the corrected exponents in ⟨1⟩6.⟨2⟩2 (recount the four-fold sum).
3. **Lockstep audit r2.** MERGE PROPOSALS (D31 text, claims row,
   notation rows, (ACE2M-LSZ)/(ACE2M-SR) rows) vs proof text vs
   `briefs/soft-index-target.md` Lane S2 vs the adjudicated AC-EX register
   in claims/CLAIMS.md. Re-run the register-comparison table of r1 §5 on
   the repaired shard.
4. **Checker audit.** Implement the REPAIRED A2M-C1 spec (including the
   new support-length gate A2M-C1a/C1b) on a copy in /tmp exactly as
   specified; run green and red under python3 -O; report whether the spec
   as written is implementable and red-capable. Do not create anything
   under theory/checks/.
5. D31-C2 (⟨1⟩3) was verified CORRECT in r1 and ordered preserved; check
   it was not damaged by the O8 edit, but do not re-litigate what r1
   already confirmed unless the text changed.

OUTPUT: `theory/verdicts/ansatz-scattering-2m-r2.md` — same format as r1
(numbered objections, independent computation, FIX DEMAND, SURVIVING
WEAKER STATEMENT, FATAL/MAJOR/MINOR/NOTE, final line PASS or FAIL(ids)),
PLUS a leading table: r1 objection id → VERIFIED-FIXED / PARTIALLY-FIXED /
NOT-FIXED / REGRESSED. Your writable lane: that verdict file ONLY.
Work fully autonomously; never ask questions.
