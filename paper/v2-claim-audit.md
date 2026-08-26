<!-- ROLE: L9/L6 self-audit for paper v2.1 (bd tns-2ze/tns-o9o). Every
     claim-bearing sentence of the MAIN TEXT of paper/main.tex (abstract, body,
     theorem environments, figure captions) is mapped to the claims/CLAIMS.md
     row(s) that license it, with the row status at the post-r4 state
     INCLUDING the S2-2body-S promotion (theory/verdicts/spin-s-r1.md PASS).
     This file is the entry point for the L6 critic pass on the paper.
     Appendices carry their own shard citations inline. Fragments are quoted
     just enough to be findable with grep.

     This revision repairs the row-map errors found by
     theory/verdicts/paper-v2-r1.md (objections 1-17): no aggregation row is
     used as a license, no conditional row licenses an unconditional sentence,
     and every number is the one the committed data file actually contains.
     Round 2 (theory/verdicts/paper-v2-r2.md, FATAL 1,11,21; MAJOR 8,13;
     MINOR 19) is repaired on top: model/domain fences on every S2-2body-S
     assertion surface (abstract, main paragraph, Fig. 1), the D17 l1 packet
     class inside Theorem 2's display, C^p in the main SPT sentence,
     self-contained Fig. 1/Fig. 2 captions, and the A=>C edge stated as
     Conjecture S at every order (rows 101, 123, 132, 156-159 and the
     abstract rows updated in lockstep).
     Round 3 (theory/verdicts/paper-v2-r3.md, FATAL 1,11) closes the three
     remaining fence surfaces: the abstract's slope sentence ENUMERATES the
     fence (model, regular two-magnon domain, fixed hard momentum inside the
     band, unit charge -- the fixed-channel, band-edge and equal-velocity
     clauses are ENTAILED by "fixed hard momentum inside the band" at the
     soft point per spin-s-r1.md sec. 3); the opening "whole result"
     sentence is WEAKENED to a non-claim-bearing signpost ("in an exactly
     solved two-magnon problem ... (Theorem 1)"); Fig. 1's Corner-C gloss
     enumerates the full fence. Rows for the abstract, opening, and Fig. 1
     Corner C updated in lockstep. -->

# Paper v2.1 claim audit — main.tex @ 2026-08-26 (post-repair)

Statuses cited from `claims/CLAIMS.md` (post-r4 + spin-s-r1 promotion).
Rule: PROVED rows may be asserted with their conditionality carried **in the
same sentence** -- either by enumerating the fence, or by clauses that
provably entail it (entailment checked against the promotion sentence, cited
in the row), or by weakening the sentence to an indexical signpost that
points at the fenced theorem and claims no breadth of its own; CONJECTURE
rows appear only labelled as conjectures; REFUTED
rows appear only as refutations. Background/credit sentences citing
literature are marked LIT; numerical values are marked with the committed
data file that carries them.

## Abstract

| sentence fragment | license |
|---|---|
| "comes to quantum spin chains" | framing only; no theorem claim (the proved/conditional/conjectural split follows sentence-by-sentence) |
| "Proved: a truncated symmetry acts only at its endpoints" | WI, A1(a) — PROVED |
| "its charge algebra centrally extended by the topological index" | A1(d1),(d3) — PROVED (padded-window register; H-split carried in body and Appendix A) |
| "in the bilinear isotropic ferromagnet---regular two-magnon domain, fixed hard momentum inside the band, unit charge---the soft phase slope is universal" | S2-2body, S2-2body-S — PROVED; fence ENUMERATED in-sentence: model, regular domain (T.1), fixed hard momentum interior to (0,π), unit charge. The remaining promotion-sentence clauses are entailed by the printed ones at the soft point (spin-s-r1.md sec. 3): band-edge exclusion = "inside the band"; fixed channel = sgn(v_h−v_s) constant in a small two-sided soft neighborhood for fixed allowed k_h; equal-velocity exclusion = v_h=v_s outside a sufficiently small soft neighborhood for fixed allowed k_h. Uniformity over compact hard subsets is not claimed (r3 obj. 1 repaired) |
| "granted a scattering hypothesis, a quantized wall step per transmitted magnon" | M-quant-G — PROVED as conditional implication; conditionality in-sentence |
| "Its edges stay conjectures" | edge ledger: A⇒C CONJECTURE, C⇒B SKETCH, B⇒A SKETCH — stated as unproved (SKETCH edges are *a fortiori* not asserted) |
| "The continuum rule, memory as zero-frequency soft factor, fails: the soft factor is a phase, the memory a charge" | M — REFUTED (printed as refutation) |
| (no "numerics verify each claim" sentence) | deliberately absent — the false v2 claim (verdict obj. 2) is removed; verification scope is stated in the body with named checks |

## Opening and introduction

| sentence fragment | license |
|---|---|
| "in an exactly solved two-magnon problem a soft magnon exits with a universal phase slope (Theorem 1)" | signpost, not a claim surface (r3 strategy (b)): the sentence is indexical---it asserts the existence of the fenced Theorem 1 and points at it, claiming no model breadth, domain, or charge scope of its own; the fence lives in Theorem 1/Appendix B (r3 obj. 1 repaired) |
| "acts at the ends of the chain as a concrete algebra of operators on matrix-product bond space" | A1(d1) — PROVED (window register) |
| "granted the scattering hypothesis H-AD-G stated below, a magnon that crosses a domain wall displaces it by a quantized charge step" | M-quant-G — PROVED conditional; hypothesis named **in the same sentence** (verdict obj. 3 repaired) |
| "the continuum rule ... is false here" | M — REFUTED |
| "what survives, and is proved, is a current-flux identity and charge bookkeeping---charge transport, not phase accumulation" | M-flux (PROVED) + M-quant/M-quant-G (PROVED conditional); no "triangle closes" claim (verdict obj. 3 repaired) |
| "three faces of one Ward identity, established for photons and gravitons" | LIT (Strominger2017, Strominger2014) |
| "Hamada and Sugishita extended the triangle" | LIT (Hamada2017; credit-before-claim) |
| "soft-magnon decoupling and the Adler zeros ... are by now systematic" | LIT (WatanabeMurayama2012, Mojahed2021, Cheung2023, Gongyo2016 — all L3-local). The former Dyson1956 priority attribution is REMOVED: no local source exists (verdict obj. 15) |
| "Lan and Xiao described magnon-driven domain-wall displacement" | LIT (Lan2021) |
| "we supply one, prove what we can, label the rest conjecture, and report one refutation" | meta-statement of L9/L10 policy |

## Setting

| sentence fragment | license |
|---|---|
| "fundamental theorem of MPS symmetries ... projective representation ... SPT index" | LIT (PerezGarcia2008, Cirac2020, Williamson2014; titles verbatim from local TeX per obj. 16); frozen input per D2, Lemma IT |
| "ground truth is the repository's proof shards and machine-checked certificates" | meta (L6b) |

## Asymptotic symmetry (Corner A)

| sentence fragment | license |
|---|---|
| "collapses to two bond insertions, V(g)^{-1} ... V(g) ..." | WI — PROVED |
| "Everything a truncated symmetry does, it does at its two ends" | WI — PROVED |
| "(i) On states, a half-infinite symmetry string acts exactly as a single bond insertion; ... converges strongly if and only if V(g) is a phase---otherwise there is no strongly convergent implementer at all" | A1(a),(b) — PROVED (iff); "counterpart" is an analogy flag |
| "(ii) ... compose as the twisted group algebra C_omega[G]" | A1(d1) — PROVED (padding stated in Appendix A) |
| "the SPT class is precisely the central extension of the asymptotic charge algebra---a group-cohomological multiplier, not a Lie-algebra central charge (Appendix D)" | A1(d1),(d3) — PROVED; multiplier-vs-central-charge scope per corner-a.md ⟨1⟩4 / SPT-D' |
| "Whether these window states extend to normal states ... is open---hypothesis H-split; no statement below uses it silently" | S-A1 — SKETCH, declared open |
| "(iii) ... every finite truncation remains in the vacuum folium (it carries a kink--antikink pair at its two ends), and only the limit---in expectation values, never in norm---lands in a domain-wall (kink) sector" | A2(a),(b),(c),(d) — PROVED. Repaired wording (verdict obj. 4): sector/folium membership plus the locally detectable kink--antikink decoration; the false "locally a vacuum" is gone |
| "Kinks are what broken asymptotic symmetries create" | A2(f) — PROVED |
| "When G acts transitively ... double-coset invariant in H\G/H" | A2(e) — PROVED under hypothesis (T), transitivity in-sentence |
| "on the vacuum, for a normal-ordered **unbroken** generator, the physical charge density equals the divergence of a purely virtual bond quantity" | G0(d) — PROVED, quantifier restored (verdict obj. 5) |
| "separately, for **any** generator and any finite-range invariant H ... [H,Q_k]=(e^{ik}-1)J_k" | G0(e) — PROVED (stated as a separate clause; the two quantifiers are no longer joined) |
| "The kinematic factor ... is a property of the profile, not a soft factor" | G0-soft-r1 — REFUTED row, cited as the refutation it is |

## Soft theorem (Corner C)

| sentence fragment | license |
|---|---|
| Theorem 1 (Eq. 1) | S2-2body — PROVED (frozen r2 form of O7/O9) |
| "The zeroth order, S_12 -> 1, is soft-magnon decoupling (a zero-momentum magnon is a symmetry rotation of the vacuum)" | OR2 — PROVED (O6 limit) + A2/G0 state-level reading. No Dyson attribution (obj. 15) |
| "independent of the hard momentum and of the coupling on the stated compact domain" | S2-2body (R17) — PROVED; scope literal, "of everything" removed (obj. 20) |
| "Hard data enters first at second order ..." | S2-2body — PROVED |
| "not a scattering length --- the ferromagnet's scattering length vanishes" | O9 (PROVED) + LIT (Gongyo2016) |
| "the soft packet exits the collision shifted by two lattice sites" | S2-2body displacement reading (D8); fm-displacement-scan.json |
| "The contact bond imposes one algebraic relation ... implicit function theorem ..." | S2-2body via soft-current-recon.md (R16)-(R18) — PROVED |
| "the residue <k_h|Q_0^dag J_0^-|k_h> = 2i v_h" | soft-current-recon.md (R14) — PROVED |
| "a directly diagonalized two-magnon completeness theorem---not assumed---makes the expansion unconditional" | ML2 — PROVED |
| "form factors to 2e-14 ... coefficients to 3e-10 ... coefficient 2 to 0.2%" | soft_current_recon_check.py record (1.560e-14, 2.167e-10); fm-displacement-scan |
| "universality fails for unrestricted local sources---an explicit four-site operator O_eta ..." | ML5 — REFUTED (unrestricted), cited as refutation; D24(e) |
| Conjecture S: "sources in the five-condition Ward-covariant no-contact class S_W of Appendix B, M_{n+1}=S(k_s)M_n+o(k_s) ... S depending only on the legs' asymptotic charges and velocities, linear at leading order" | S-general — CONJECTURE, labelled in-sentence; multiplier and class exactly per D25 and D24(d) (verdict obj. 6 repaired: no fixed "2i" beyond two-body, no invented row) |
| "Theorem 1 is its proved two-body instance, S = 2i k_s" | S2-2body — PROVED specialization only |
| "All else is open---wave operators, form-factor regularity, the soft-limit interchange, two or more hard legs, membership of any microscopic source in S_W; Appendix B states the complete list" | ML1, ML3, ML6 CONJECTURE; ML4 SKETCH; S-general obligations. No false "three lemmas" count (verdict obj. 7 repaired); the exhaustive list is in Appendix B |

## Memory (Corner B)

| sentence fragment | license |
|---|---|
| "Its change over the event is an exact operator identity, no hypotheses ..." | M-flux — PROVED |
| "the zero-frequency weight of the physical boundary current---the lattice image ..." | M-flux — PROVED; continuum comparison LIT |
| Theorem 2: one fixed kink-magnon wavepacket "whose charge deviations from the two vacua are summable---the ℓ¹ kink class (no plane wave)"; H-AD-G named; wave operators exist and complete; exactly one reflected + one transmitted channel; charges q_in=q_L=-1, q_T=+1; no further propagating channel; no bound-state component; local decay; limit order (volume, time, window) | M-quant-G — PROVED as conditional implication (mquant-g-r2.md). The D17 ℓ¹/summable-charge-deviation packet class (load-bearing per memory-quantization-general.md items 1,3: weak-* membership alone does not make the regularized charge converge) and all D18(AD1-AD4) clauses are INSIDE the displayed statement (r1 obj. 8, r2 obj. 8 repaired) |
| "quantized by charge conservation alone: it does not depend on momentum, anisotropy, packet shape, or any scattering phase" | M-quant / M-quant-G — PROVED conditional (channel statement) |
| "The proof is charge bookkeeping (Appendix C)" | M-quant-G (G.3)-(G.4) — PROVED conditional |
| "the two vacua must carry opposite charge density along one unbroken direction; ... a bare abelian symmetry cannot" | M-quant-G §3 Remark (Weyl-element criterion) — PROVED scope |
| "H-AD-G itself we prove only for the dominant domain-wall sector ... conditional on ... sector-reduction hypothesis; for the full chain it remains an assumption" | Mq-AD3 — PROVED conditional on Mq-E; Mq-E CONJECTURE; full-chain D18 open (tns-d51) |
| "confirm delta x = -2<N_T> at s=1/2 to 0.064 sites across the momentum scan ... and to 0.005 sites on the nine rows with trapped weight below 10^-6" | N2 — SKETCH (empirical); memory-scan-1.json. Honest numbers (verdict obj. 9 repaired): full-scan max \|dx2+2T\| = 0.0636 (dx1: 0.0754, both at Delta=3, k0=0.4, trapped ≈ 4.2e-3); gated nine rows (N=160, standoff 36, dwmax 3, trapped<1e-6): max dx1 residual 0.00433, max dx2 residual 0.00123 — both ≤ 0.005 |
| "In the reduced sector ... t(k)=[1+iJ^2/4 omega v]^{-1}" | M-tk — PROVED conditional on Mq-E ("In the reduced sector" carries it) |
| "matches this over Delta in [1.5,12] to 0.9-5.8% ... criterion 8%, fixed in advance" | crosscheck_corner_b_tk.py + memory-scan-1.json |
| Eq. (3) soft zero | M-tk — PROVED conditional on Mq-E for the displayed graph |
| "Whether the zero's coefficient is universal we have not established; that remains a conjecture" | TRIANGLE §3.4 — CONJECTURE, labelled |
| "That statement is false in the XXZ chain, twice over" | M — REFUTED |
| "What survives---and is proved---is the pair above ... charge transport, not phase accumulation" | M-flux (PROVED) + M-quant (PROVED conditional); replaces v2's "lattice sharpening / third corner closes" (verdict objs. 3, 20 repaired) |
| "The remaining edge is bookkeeping, and only that: ... rigid at finite times ... 2s delta x + (q_out - q_in) = 0" | B3 — PROVED (both clauses) |
| "That the memory reconstructs the asymptotic transformation which acted remains open" | B⇒A edge — SKETCH; named HOLD reason, stated as open |

## One invariant, read out twice (Conjecture B)

| sentence fragment | license |
|---|---|
| "We conjecture---Conjecture B---that both equal \|q_hard\|/s" | Bc — CONJECTURE, labelled in-sentence |
| "The conjecture was built to fail at s != 1/2 ... it survived" | Bc row falsifier record (2026-08-26) |
| "phase slope = 1/s across s in {1/2,1,3/2,2} and the memory quantum = -1/s across s in {1/2,1,3/2}, within pre-registered 8% bands (every gated run within 2.7%, and within 1% at the cleanest kinematics)" | spin1-bc-falsifier.json + spin1-bc-crosscheck.json. Under the documented trapped<1e-2 gate (spin1-twomagnon-notes.md), the worst gated deviation is 2.69% (s=1, k0=0.8); k>=1.2/1.5 rows are within 1%. Memory s-range honestly {1/2,1,3/2} (no s=2 memory run) |
| "An exact two-magnon computation now proves the slope half for the bilinear isotropic ferromagnet at every site spin: on the regular two-magnon domain, at each fixed hard momentum in (0,π) and fixed channel, ∂δ/∂k_s|_0 = sgn(v_h−v_s)/s ... ---the unit-charge two-body slope only, with band edges and equal velocities excluded" | **S2-2body-S — PROVED** (theory/spin-s-twomagnon.md; verdict theory/verdicts/spin-s-r1.md PASS). The main-paragraph sentence now mirrors the promotion sentence's full fence: bilinear isotropic FM, every S, regular two-body domain, fixed 0<\|k_h\|<π and fixed channel, endpoint/equal-velocity excluded, unit charge only; the remaining exclusions (spin-S Bethe completeness, Conjecture S, memory half, \|q\|>1, Conjecture B) are in the adjacent sentences and Appendix B (r2 obj. 11 repaired) |
| "The memory half remains conditional on H-AD-G; the \|q_hard\| factor is untested ... next falsifier" | Bc row: explicitly untested; honesty sentence (verdict obj. 12: identification never restated as fact) |

## Where the SPT index lives

| sentence fragment | license |
|---|---|
| "The answer, proved in Appendix D, is a rigidity dichotomy" | SPT-B-mult, SPT-B', SPT-E', SPT-E-AKLT — PROVED |
| "projective multipliers cancel exactly" | SPT-B-mult — PROVED |
| "every normalized bulk coefficient is continuous along common-gap symmetric deformation paths with continuously varying external data (a coefficient reached through a soft limit or p derivatives needs in addition C^p external data and the uniformity hypothesis H-soft-p, Appendix D)" | SPT-B' — PROVED; common gap, continuous external data, C^p external data for soft-limit/derivative coefficients, and H-soft-p are ALL in the main-text sentence (r2 obj. 13 repaired) |
| "nothing bulk is a topological invariant without a separate local-constancy proof" | SPT-B'(iii) — PROVED |
| "bulk soft-charge coefficient moves from 0.125 to 0.240" | spt-rebuild.md (3.2) + S-C3 record |
| "the compensated soft residue is an operator on the chi-dimensional edge register ... [omega]-shifted lattice ... dimension at least ..." | SPT-E'(i)-(iii) — PROVED (registered statement; physical reading behind H-split) |
| "For the AKLT half-chain the residue is exactly -1/2[1-(2b^2-1)^L]Z -> -Z/2" | SPT-E-AKLT — PROVED |
| "Physical edge statements carry the hypothesis H-split above; granted in addition an edge-resolved scattering hypothesis H-AD-edge, charge conservation, and definite channel charges, charge bookkeeping quantizes edge-memory outcomes" | SPT-M' — PROVED as conditional implication; ALL four hypotheses now in the claim-bearing main sentence (verdict obj. 14 repaired) |
| "what is protected is the memory's capacity ... not any particular amplitude" | SPT-M' protection scope, exactly per spt-rebuild.md ⟨1⟩6 |
| "That an AKLT boundary magnon actually writes to it, we state as a conjecture" | SPT-M'-dyn — CONJECTURE, labelled |

## Outlook

| sentence fragment | license |
|---|---|
| "concentrates in a boundary soft algebra ... structural parallel to the celestial program" | outlook sentence (a); "structural parallel" is analogy; A1 supplies C_omega[G] |
| "its symplectic origin is deferred to forthcoming work" | outlook (b); no claim (bd tns-89h) |
| "The wall is a broken asymptotic symmetry made visible" | A2(f) — PROVED |
| "and---if Conjecture B holds---the magnon's soft phase and the wall's memory read out one conserved charge" | Bc — CONJECTURE; conditional label in the same clause (verdict obj. 12 repaired) |
| "fits on a chain of spins" | permitted single closing sentence of reach (prose-guide rule 21); the false "where every step of it can be checked" is deleted (obj. 12) |

## Figure captions

| fragment | license |
|---|---|
| Fig 1 "Corner A (asymptotic symmetry, proved)" | WI, A1, A2 — PROVED | — caption states the padded-window register ("on windows padded about a bond"), matching A1(d1); restored after r4 objection 22 (a compression had dropped "on windows", silently upgrading to the open H-split physical-edge reading). |
| Fig 1 "Corner C (soft theorem, proved for two-body scattering in the bilinear isotropic ferromagnet on its regular two-magnon domain---fixed hard momentum inside (0,π), fixed channel, unit charge; band edges and equal velocities excluded) ... (1/s at site spin s)" | S2-2body + S2-2body-S — PROVED; the COMPLETE promotion fence is enumerated in-caption: model, regular two-magnon domain, fixed hard momentum inside (0,π), fixed channel, unit charge, band-edge and equal-velocity exclusions (r3 obj. 11 repaired) |
| Fig 1 "Corner B (memory, proved conditional on the scattering hypothesis H-AD-G: complete kink--magnon wave operators for a fixed packet with no bound component, one reflected and one transmitted channel of definite charges ∓1, local decay, limits taken in the order volume, time, window)" | M-quant-G — PROVED conditional; the H-AD-G gloss now names the no-bound-component, local-decay, and limit-order clauses in-caption (r2 obj. 19 repaired) |
| Fig 1 "No edge is a theorem: the A⇒C edge remains Conjecture S at every order---Corner C itself is proved two-body; C⇒B ...; B⇒A ..." | edge ledger: A⇒C is CONJECTURE at EVERY order (CLAIMS.md: the edge is not supplied by Corner A; G0(e) gives no Adler zero or universality). The caption no longer assigns any proved sector to the edge; the proved object is the Corner-C two-body amplitude (S2-2body/-S), stated as a corner, not an edge (r2 obj. 21 repaired) |
| Fig 2 (a) "vanishes quadratically for each hard momentum k_h in a compact subset of (0,π) ... through the magnon frequency omega_h=J(1-cos k_h) and velocity v_h=J sin k_h" | S2-2body — PROVED; the compact-subset fence and the definitions of omega_h, v_h are in-caption (r2 obj. 19 repaired; "every hard momentum"/"all k_h" removed) |
| Fig 2 (b) "passes through -2 sites ... coefficient 2 to 0.2%" | S2-2body + fm-displacement-scan.json |
| Fig 2 "within two-body scattering; beyond is Conjecture S, unproved" | scope statement in-caption (obj. 19; replaces "see the text") |
| Fig 3 (a) "steps back by two sites and stays" (single event) | memory-scan-1.json main-D3.0-k1.2 record (dx2 = -1.978) — data description |
| Fig 3 (a) "Across the plotted scan ... holds to 0.064 sites (worst: slowest packets, trapped weight ≈ 4e-3); on the nine rows with trapped weight <1e-6, to 0.002 sites" | memory-scan-1.json, recomputed honestly (obj. 9): plotted estimator dx2, full-scan max 0.0636; gated nine-row dx2 max 0.00123. <N_T> defined in-caption (obj. 19) |
| Fig 3 (c) "collapse ... 0.9-5.8%", omega and v defined in caption | M-tk conditional + crosscheck record; obj. 19 |
| Fig 3 (c) "as k_0 -> 0 transmission vanishes quadratically" | M-tk — PROVED conditional on Mq-E |
| Fig 3 inset "every physical wavepacket run with trapped weight < 1e-2, the record's quality gate; controls excluded" | selection rule now MECHANICAL and disclosed (obj. 10 repaired): make_figures.py applies the documented gate (numerics/docs/spin1-twomagnon-notes.md, trapped < 1e-2) to all physical grid rows of both JSONs; no momentum-label filter. This admits the formerly excluded clean k0=0.8 rows (deviations 2-3%) and mechanically excludes s1-D2.0-k1.8 (trapped 5.5e-2) and the k0=0.8 cross-check rows (trapped ≈ 4e-2). 17 points, all within the 8% band |
| Fig 3 inset "Both are consistent with 1/s, excluding the constant 2; that both measure one charge datum \|q_hard\|/s is Conjecture B" | data description + explicit conjecture label (obj. 12 repaired) |

## Verdict-driven repairs not visible in the row map

1. Obj. 15: `Dyson1956` removed from refs.bib and both citation sites;
   no priority attribution without a local L3 source. NielsenChadha1976
   remains an uncited, explicitly marked stub.
2. Obj. 16: `Cirac2020` and `Williamson2014` titles copied verbatim from
   refs/arxiv-2011.12127/TN-Review-main.tex and refs/arxiv-1412.5604/SPT.tex;
   the stale "non-local 1203.0609" comment repaired.
3. Obj. 17: Appendix E now says TEN checkers, all passing, with red mutation
   modes on exactly the five that document them (ml4_check --red-uniform,
   mquant_check --red, mquant_general_check --red, spin_s_slope_check --red,
   spt_rebuild_check --red/--red-gauge). No "each with red" claim.
4. Obj. 18: latexmk build is warning-clean (no stuck floats, no
   underfull/overfull boxes); the BibTeX empty-journal warnings for
   eprint-only entries are documented as deliberate in refs.bib.
5. Obj. 10: figures regenerated by paper/figures/make_figures.py only; the
   inset point set changed accordingly (13 label-selected -> 17 gate-selected
   points).
6. Obj. 20: "learned the hard way", "of everything", "not a technicality",
   "lattice sharpening" all replaced by literal scope.

## Claims I wanted to make but could NOT license (deliberately absent)

1. The whole triangle as a theorem — edges are CONJECTURE/SKETCH; the
   abstract and opening state the split.
2. "Numerics verify each claim" — false; removed. Only the named checks are
   claimed, with their committed records.
3. Unconditional (process-independent) soft theorem beyond two bodies —
   S-general is CONJECTURE; ML5 refuted the unrestricted form.
4. Universality of the memory soft-zero coefficient — CONJECTURE, said so.
5. Unconditional memory law for the full XXZ chain — full-chain D18/H-AD-G
   open (tns-d51); Mq-E CONJECTURE; Theorem 2 conditional, Fano results
   scoped "in the reduced sector".
6. "Measuring the memory identifies the asymptotic transformation that
   acted" — B⇒A reconstruction open; bookkeeping-only statement (B3).
7. The charge algebra acting on the physical (GNS/edge) Hilbert space —
   H-split SKETCH; scoped to padded windows or flagged.
8. Bc's |q_hard| dependence — untested (all legs |q|=1); said so, everywhere
   it appears.
9. Memory quantum at s=2 — no committed run; slope across {1/2,1,3/2,2},
   memory across {1/2,1,3/2}.
10. Var as a one-time observable — only the two-channel Bernoulli variance
    inside Theorem 2.
11. K4 (Z-torsor/flat kink family) — CONJECTURE; Appendix C only.
12. A2 uniformity over a continuous vacuum manifold — SKETCH; Appendix A
    records the gap.
13. Endpoint/equal-velocity limits, spin-S Bethe completeness, |q_hard|>1 —
    all outside S2-2body-S's promoted scope; excluded explicitly in
    Appendix B's scope sentence.
