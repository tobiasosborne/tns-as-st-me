<!-- ROLE: L9/L6 self-audit for paper v2 (bd tns-2ze). Every claim-bearing
     sentence of the MAIN TEXT of paper/main.tex (abstract, body, theorem
     environments, figure captions) is mapped to the claims/CLAIMS.md row(s)
     that license it, with the row status at the corpus-r4 fixed point
     (theory/verdicts/corpus-r4.md). This file is the entry point for the L6
     critic pass on the paper. Appendices carry their own shard citations
     inline. Fragments are quoted just enough to be findable with grep. -->

# Paper v2 claim audit — main.tex @ 2026-08-26

Statuses cited from `claims/CLAIMS.md` at the corpus-r4 fixed point.
Rule: PROVED rows may be asserted (with their conditionality carried in the
sentence); CONJECTURE rows appear only labelled as conjectures; REFUTED rows
appear only as refutations. Background/credit sentences citing literature
are marked LIT (no claim row needed); numerical values are marked with the
committed data file that carries them.

## Abstract

| sentence fragment | license |
|---|---|
| "is formulated and proved for quantum spin chains" | WI, A1, A2, G0, S2-2body, M-flux, M-quant-G, B3, SPT-B'/E'/T'/D'/M' — all PROVED (scope carried below sentence-by-sentence) |
| "A truncated symmetry acts only at its endpoints" | WI — PROVED |
| "generating a charge algebra whose central extension is the topological index" | A1(d1),(d3) — PROVED (padded-window register; H-split caveat carried in body §Asymptotic symmetry and Appendix A) |
| "A soft magnon decouples with a universal phase slope" | S2-2body — PROVED (two-body; scope stated in body) |
| "granted a scattering hypothesis, a transmitted magnon drags a domain wall by a quantized charge step" | M-quant-G — PROVED conditional on H-AD-G; conditionality in-sentence |
| "The continuum rule that memory is the zero-frequency soft factor fails: the soft factor is a phase, the memory a charge" | M — REFUTED (printed as refutation; TJO sign-off) |
| "Bethe and matrix-product numerics verify each claim" | OR1, OR2 — PROVED; N2 — SKETCH (verification role only, no claim promoted from numerics) |

## Opening and introduction

| sentence fragment | license |
|---|---|
| "a soft magnon leaves two-body scattering with a universal phase slope" | S2-2body — PROVED |
| "acts at the ends of the chain as a concrete algebra of operators on matrix-product bond space" | A1(d1) — PROVED (window register) |
| "displaces it by a quantized charge step" | M-quant-G — PROVED conditional (the "under an explicit scattering hypothesis" qualifier appears at every load-bearing statement; here the sentence is the one-sentence summary, with the conditional stated in Theorem 2) |
| "the continuum rule ... is false here" | M — REFUTED |
| "the lattice triangle closes through charge transport, not phase accumulation" | M (REFUTED) + M-flux, M-quant (PROVED): the surviving pair framing per HANDOFF TJO sign-off |
| "three faces of one Ward identity, established for photons and gravitons" | LIT (Strominger2017, Strominger2014) |
| "Hamada and Sugishita extended the triangle" | LIT (Hamada2017; credit-before-claim, prose-guide rule 14) |
| "Dyson showed in 1956 ..." | LIT (Dyson1956; bibliographic record, nothing quoted — see refs.bib comment) |
| "Lan and Xiao described magnon-driven domain-wall displacement" | LIT (Lan2021) |
| "prove what we can, label the rest conjecture, and report one refutation as a central result" | meta-statement of L9/L10 policy |

## Setting

| sentence fragment | license |
|---|---|
| "fundamental theorem of MPS symmetries ... projective representation ... SPT index" | LIT (PerezGarcia2008, Cirac2020, Williamson2014); used as frozen input per D2 (definitions.md), Lemma IT (theory/corner-a.md ⟨1⟩2) |
| "ground truth is the repository's proof shards and machine-checked certificates" | meta (L6b) |

## Asymptotic symmetry (Corner A)

| sentence fragment | license |
|---|---|
| "collapses to two bond insertions, V(g)^{-1} on the bond entering R and V(g) on the bond leaving it" | WI — PROVED (orientation as stated in corner-a.md ⟨1⟩3; opposite to the historical brief) |
| "Everything a truncated symmetry does, it does at its two ends" | WI — PROVED |
| "(i) On states, a half-infinite symmetry string acts exactly as a single bond insertion" | A1(a) — PROVED |
| "converges strongly if and only if V(g) is a phase" | A1(b) — PROVED (iff) |
| "no strongly convergent implementer at all --- the lattice counterpart of a large gauge transformation" | A1(b) — PROVED; "counterpart" is an analogy flag, not a claim |
| "(ii) On finite windows padded around the distinguished bond, the insertions compose as the twisted group algebra C_omega[G]" | A1(d1) — PROVED (padding necessary; stated) |
| "the SPT class is precisely the central extension of the asymptotic charge algebra" | A1(d1),(d3) — PROVED |
| "a group-cohomological multiplier, not a Lie-algebra central charge ... infinitesimal cocycle gauges away while the torsion class survives" | corner-a.md ⟨1⟩4 central-extension caveat (TRIANGLE §1.3) — PROVED scope |
| "Whether these window states extend to normal states ... is an open split-property question, hypothesis H-split" | S-A1 — SKETCH, declared open (load-bearing box carried explicitly) |
| "(iii) ... only the limit --- in expectation values, never in norm --- lands in a domain-wall (kink) sector" | A2(b),(c),(d) — PROVED (weak-* only, stated) |
| "Kinks are what broken asymptotic symmetries create" | A2(f) — PROVED (every kink sector with beta in G-alpha is reached) |
| "When G acts transitively ... double coset in H\G/H" | A2(e) — PROVED under hypothesis (T), transitivity stated in-sentence |
| "the physical charge density equals the divergence of a purely virtual bond quantity" | G0(d) — PROVED |
| "exact continuity equation [H,Q_k]=(e^{ik}-1)J_k" | G0(e) — PROVED |
| "the kinematic factor ... is a property of the profile, not a soft factor" | G0-soft-r1 — REFUTED row, cited as the refutation it is |

## Soft theorem (Corner C)

| sentence fragment | license |
|---|---|
| Theorem 1 (Eq. 1: slope 2 sgn(v_h - v_s), quadratic \|v_h\|/omega_h, O(k_s^3) uniform on compact hard sets) | S2-2body — PROVED (statement matches the frozen r2 form of O7/O9, oracle-bethe-r2) |
| "The zeroth order, S_12 -> 1, is Dyson's decoupling" | OR2 — PROVED (O6) + LIT |
| "The linear coefficient is the pure number 2 ... independent of the hard momentum, of the coupling, of everything" | S2-2body (R17): hard dependence cancels — PROVED (on D8; the sign qualifier is in the same sentence) |
| "Hard data enters first at second order, through the single even invariant \|v_h\|/omega_h" | S2-2body — PROVED |
| "not a scattering length --- the ferromagnet's scattering length vanishes" | O9 (oracle, PROVED) + LIT (Gongyo2016) |
| "the soft packet exits the collision shifted by two lattice sites" | S2-2body displacement reading (D8 convention); tested in fm-displacement-scan.json |
| "The contact bond imposes one algebraic relation ... implicit function theorem ... all hard dependence cancelling" | S2-2body via soft-current-recon.md (R16)-(R18) — PROVED |
| "the residue <k_h\|Q_0^dag J_0^-\|k_h> = 2i v_h" | soft-current-recon.md (R14) — PROVED |
| "a completeness theorem for the two-magnon sector --- proved by direct diagonalization, not assumed --- makes the expansion unconditional" | ML2 — PROVED |
| "Exact diagonalization confirms the form factors to 2e-14 and the two coefficients to 3e-10" | soft_current_recon_check.py record (1.560e-14, 2.167e-10) |
| "wavepacket collisions reproduce ... the coefficient 2 to 0.2%" | numerics fm-displacement-scan (TRIANGLE §2.3 record) |
| "universality fails for unrestricted local sources ... O_eta ... shifts the linear soft coefficient by 2i eta(1-e^{-3i k_h})" | ML5 — REFUTED (unrestricted universality), cited as the refutation; D24(e) |
| "on the class of Ward-covariant, no-contact sources the soft factor is universal, and we conjecture --- Conjecture S" | ML5-A/ML5-B — PROVED conditional implications; S-general — CONJECTURE, labelled in-sentence |
| "process independence beyond it rests on three unproved lemmas" | ML1, ML3, ML6 — CONJECTURE (+ ML4 SKETCH, detailed in Appendix B) |

## Memory (Corner B)

| sentence fragment | license |
|---|---|
| "Its change over the event is an exact operator identity, no hypotheses: the time-integrated U(1) current through the two boundary bonds" | M-flux — PROVED |
| "Memory is the DC component of a current at the edge of the observation window" | M-flux — PROVED; continuum comparison LIT (Strominger2014, DeLuca2024) |
| Theorem 2 (general register; "Assume the scattering hypothesis H-AD"; Delta X = -(1/s) N_T; spectrum; Bernoulli variance) | M-quant-G — PROVED as conditional implication (mquant-g-r2.md); conditionality inside the theorem statement |
| "quantized by charge conservation alone: it does not depend on momentum, anisotropy, packet shape, or any scattering phase" | M-quant — PROVED conditional on D18 (channel statement independent of k, Delta, packet, phase) |
| "a transmission changes the separated leg charge by 2, and the wall must absorb it at 2s per site" | M-quant-G ⟨1⟩2-⟨1⟩4 (G.3)-(G.4) — PROVED conditional |
| "the two vacua must carry opposite charge density ... a bare abelian symmetry cannot produce such a kink pair" | M-quant-G §3 Remark (Weyl-element criterion) — PROVED scope of the shard's remark |
| "H-AD itself we prove only for the dominant domain-wall sector ... conditional on an explicitly stated sector-reduction hypothesis; for the full chain it remains an assumption" | Mq-AD3 — PROVED conditional on Mq-E; Mq-E — CONJECTURE; full-chain D18 open (tns-d51). Honesty sentence |
| "numerics on chains of 160 sites confirm delta x = -2<N_T> ... to 0.004 sites" | N2 — SKETCH (empirical); memory-scan-1.json; presented as numerical confirmation, not proof |
| "In the reduced sector ... t(k)=[1+iJ^2/4 omega v]^{-1}" | M-tk — PROVED conditional on Mq-E ("In the reduced sector" carries the condition) |
| "measured reflection matches this over Delta in [1.5,12] to 0.9-5.8% ... criterion 8%, fixed in advance" | crosscheck_corner_b_tk.py + memory-scan-1.json (TRIANGLE §3.3 record) |
| Eq. (3): T = 16(Delta-1)^2 k^2 + O(k^4) | M-tk — PROVED conditional on Mq-E for the displayed graph (follows "In the reduced sector") |
| "Whether the zero's coefficient is universal ... remains a conjecture" | TRIANGLE §3.4 universality — CONJECTURE, labelled |
| "That statement is false in the XXZ chain, twice over" | M — REFUTED (both counterexample reasons from memory-quantization.md / TRIANGLE §3.5) |
| "The soft factor is a phase; the memory quantum is a charge" | M — REFUTED framing (TRIANGLE §3.5 verbatim content) |
| "What survives --- and is proved --- is the pair above" | M-flux (PROVED) + M-quant (PROVED conditional) |
| "the vacuum-pair label of the kink sector is rigid at finite times" | B3 — PROVED (first clause) |
| "2s delta x + (q_out - q_in) = 0 within that fixed sector" | B3 — PROVED (second clause) |
| "That the memory reconstructs the asymptotic transformation which acted remains open" | B => A edge — SKETCH; the named HOLD reason, stated as open |

## One invariant, read out twice (Conjecture B)

| sentence fragment | license |
|---|---|
| "We conjecture --- Conjecture B --- that both equal \|q_hard\|/s" | Bc — CONJECTURE, labelled in-sentence |
| "The conjecture was built to fail at s != 1/2 ... it survived" | Bc row falsifier record (2026-08-26) |
| "measured the phase slope = 1/s across s in {1/2,1,3/2,2} and the memory quantum = -1/s across s in {1/2,1,3/2}, within pre-registered 8% bands (deviations <= 1% at clean kinematics)" | spin1-bc-falsifier.json (A_ring_summary: max abs deviation 0.0028; B_runs k>=1.2 rows) + spin1-bc-crosscheck.json (A_dynamics, B_runs k1.5 rows). Memory s-range stated honestly as {1/2,1,3/2} (no s=2 memory run exists) |
| "an exact two-magnon contact computation gives the slope 1/s in closed form" | evidence only, NOT a promoted row (tns-c8q pending); flagged in Appendix B as "counted as evidence, not theorem" |
| "The \|q_hard\| factor is untested ... next falsifier" | Bc row: explicitly untested; honesty sentence |

## Where the SPT index lives

| sentence fragment | license |
|---|---|
| "The answer is a rigidity dichotomy, and it is proved" | SPT-B-mult, SPT-B', SPT-E', SPT-E-AKLT — PROVED |
| "a closed symmetry insertion has two endpoints whose projective multipliers cancel exactly" | SPT-B-mult — PROVED |
| "every normalized soft coefficient is a continuous function along symmetric gapped deformation paths" | SPT-B' — PROVED (common-gap path, continuous external data hypotheses carried in Appendix D) |
| "nothing bulk is a topological invariant without a separate local-constancy proof" | SPT-B'(iii) — PROVED |
| "a natural bulk soft-charge coefficient moves from 0.125 to 0.240 with the SPT class fixed" | spt-rebuild.md (3.2) + S-C3 record (0.125 -> 0.240196) |
| "the compensated soft residue is an operator on the chi-dimensional edge register whose centered charge has spectrum in the [omega]-shifted lattice ... dimension at least ..." | SPT-E'(i)-(iii) — PROVED (registered/fixed-tensor statement; physical reading behind H-split, next sentence) |
| "For the AKLT half-chain the residue is exactly -1/2[1-(2b^2-1)^L]Z -> -Z/2 along the entire path" | SPT-E-AKLT — PROVED (exact formula (4.1)) |
| "The topological data of soft physics concentrates at the boundary" | summary of the dichotomy (SPT-B' + SPT-E'), both PROVED |
| "Physical edge statements carry the hypothesis H-split" | S-A1 SKETCH / Sd7' (H-split) — open, stated |
| "charge bookkeeping then quantizes edge-memory outcomes ... capacity ... not any particular amplitude" | SPT-M' — PROVED as conditional implication; protection scope exactly per spt-rebuild.md ⟨1⟩6 |
| "That an AKLT boundary magnon actually writes to it, we state as a conjecture" | SPT-M'-dyn — CONJECTURE, labelled |

## Outlook

| sentence fragment | license |
|---|---|
| "concentrates in a boundary soft algebra ... structural parallel to the celestial program" | one-sentence outlook (a); "structural parallel" is analogy, no claim row; A1 supplies C_omega[G] |
| "The symplectic origin ... deferred to forthcoming work" | one-sentence outlook (b); no claim made (bd tns-89h) |
| "the wall is a broken asymptotic symmetry made visible" | A2(f) — PROVED |
| "the magnon's soft phase and the wall's memory measure one conserved charge crossing an observer" | closing-loop sentence; licensed as the *conjectured* content of Bc read together with S2-2body + M-quant; phrased as the dissolution of the opening picture, immediately after Bc was labelled a conjecture |
| "fits on a chain of spins, where every step of it can be checked" | permitted single sentence of reach (prose-guide rule 21) |

## Figure captions

| fragment | license |
|---|---|
| Fig 1 "Corner A (asymptotic symmetry, proved)" | WI, A1, A2 — PROVED |
| Fig 1 "Corner C (soft theorem, proved for two-body scattering)" | S2-2body — PROVED, scope in caption |
| Fig 1 "Corner B (memory, proved conditional on the scattering hypothesis H-AD)" | M-quant / M-quant-G — PROVED conditional, condition in caption |
| Fig 1 "edge labels name the mechanisms; their present status is uneven" | A=>C CONJECTURE / C=>B SKETCH / B=>A SKETCH per TRIANGLE §6, stated |
| Fig 2 (a) "vanishes quadratically ... coefficient v_h/omega_h" | S2-2body — PROVED; checker 2.167e-10 (quoted as 3e-10) |
| Fig 2 (b) "passes through -2 sites ... coefficient 2 to 0.2%" | S2-2body + fm-displacement-scan.json |
| Fig 2 "for what it takes to drop the last qualifier, see the text" | honesty pointer to S-general CONJECTURE |
| Fig 3 (a) "steps back by two sites ... permanent record"; "delta x = -2<N_T> to 0.004 sites" | N2 (SKETCH, empirical) + memory-scan-1.json; single-event record is data |
| Fig 3 (c) "collapses onto R=[1+(4 omega v/J^2)^2]^{-1} ... 0.9-5.8%" | M-tk conditional + crosscheck record |
| Fig 3 (c) "as k_0 -> 0 transmission vanishes quadratically" | M-tk — PROVED conditional on Mq-E (displayed-graph statement; caption ties to Eq. (3)) |
| Fig 3 inset "Soft phase slope ... and memory quantum ... against the single line 1/s ... Both follow the charge datum, not the constant 2" | Bc falsifier record (both JSONs); "follow" is a data description, the identification remains Conjecture B in the text |

## Claims I wanted to make but could NOT license (deliberately absent)

1. Unconditional (process-independent) soft theorem beyond two bodies — S-general
   is CONJECTURE; ML5 refuted the unrestricted form. Stated as Conjecture S only.
2. Universality of the memory soft-zero coefficient 16(Delta-1)^2 — CONJECTURE
   (TRIANGLE §3.4). The text says so explicitly.
3. Unconditional memory law for the full XXZ chain — full-chain D18/H-AD is open
   (tns-d51); Mq-E is CONJECTURE. Theorem 2 stays conditional; Fano results are
   scoped "in the reduced sector".
4. "Measuring the memory identifies the asymptotic transformation that acted"
   (v1 sentence) — B=>A reconstruction is the named open half of that edge;
   sentence deleted, replaced by the bookkeeping-only statement (B3).
5. The spin-s slope law d delta/d k_s = 1/s as a THEOREM — exact analytics exist
   in the falsifier record but have not passed an L6 loop (tns-c8q); presented
   as evidence for Conjecture B.
6. The charge algebra acting on the physical (GNS/edge) Hilbert space — S-A1 is
   SKETCH (H-split); all such statements are scoped to padded windows or
   flagged with H-split.
7. Bc's |q_hard| dependence — untested (all legs |q|=1); said so.
8. Dynamical SPT edge memory (nonzero edge-changing amplitude) — SPT-M'-dyn is
   CONJECTURE; stated as such with its deciding computation named.
9. Memory quantum measured at s=2 — no committed run exists; the text and
   caption say slope across {1/2,1,3/2,2}, memory across {1/2,1,3/2}.
10. Var(X_W) as a one-time observable variance — only the two-channel
    Var(Delta X) is licensed (M-quant); the Letter states the Bernoulli variance
    inside Theorem 2 only.
11. K4 (Z-torsor / unique flat kink family in the thermodynamic limit) —
    CONJECTURE; mentioned only in Appendix C as a conjecture.
12. A2 uniformity over a continuous vacuum manifold (S-A2) — SKETCH; Appendix A
    records the gap, the main text never uses g-uniform statements.
