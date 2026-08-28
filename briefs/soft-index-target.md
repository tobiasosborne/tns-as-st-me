<!-- ROLE: campaign target specification for the 2026-08-28 Corner-C
     soft-index campaign (TJO greenlight: "revisit the soft theorem at the
     new, more ambitious level of generalisation"; budget 1 Fable + 3 codex
     xhigh). All provers read THIS FIRST, then the read-order gate:
     CLAUDE.md -> definitions.md -> notation.md -> claims/CLAIMS.md ->
     theory/soft-current-recon.md -> theory/ml4-ward-reduction.md ->
     theory/ml5-universality.md -> theory/TRIANGLE.md §2 -> (T2 only)
     theory/ansatz-scattering.md + definitions.md D28. -->

# Campaign target — the channel-free soft theorem (soft-index), two lanes

## Why this campaign exists

The corpus's soft corner is S-general: a CONJECTURE whose entire missing
content sits in scattering-theoretic existence and regularity lemmas —
ML1 (two-magnon wave operators), ML3 (uniform form-factor regularity),
ML6 (limit orders), packet-smeared infinite-volume ML4. Those lemmas are
(a) proved for no model beyond finite volume, (b) exactly analogous to the
H-AD-G package that the memory-index campaign made OPTIONAL, and (c)
degenerate exactly at the soft endpoint (the k_s→0 limit commutes with
none of the volume/time/packet limits; the first physical on-shell
sequence k_s=2π/N REFUTES volume-uniformity of the fixed-N interpolation —
ML4-Q1, √N growth).

The memory-index campaign proved the restructuring pattern: *superselection
quantizes; dynamics only computes the value.* This campaign applies the
same inversion to Corner C:

  **The soft law is a symmetry CONSTRAINT on every limit point of the
  protocol amplitude data. Scattering theory is only needed to prove that
  limit points EXIST and to compute the hard amplitudes they multiply.**

Lane S1 proves the constraint half: any subsequential limit of the
windowed, packet-smeared, charge-created-soft-leg amplitude data obeys the
Adler zero and has its slope pinned to the leg charge datum — with NO wave
operators, NO completeness, NO channel inventory assumed. Lane S2 proves
the existence half in the vacuum sector: two-magnon wave operators from
exact excitation-ansatz band data (the AC-EX method transplanted to its
EASIER original setting — two particles over one translation-invariant
vacuum), which supplies nonvacuity and computes values.

Campaign register (the spine sentence): *symmetry fixes the soft law; the
ansatz supplies the kinematics; dynamics only picks the values.*

## Standing setting (cite, never redefine — L4)

All from `definitions.md` / `theory/TRIANGLE.md` §0 and §2: D6--D8 (FM
chain, two-magnon Bethe register, D8 half-zone), D3(a)/D12(a′) packet
classes, D10 (currents, continuity), D24 (source classes, contact first
jet 𝔠_h, the class 𝒮_W), D25 (the soft multiplier 𝖲), D26 (INT). The
exact identities you may take as PROVED without reproving (check the DAG
status first — L5): (R1)--(R19) of `theory/soft-current-recon.md`;
ML4-Ward (exact finite-sector Ward projection, equations (8)--(11) of
`theory/ml4-ward-reduction.md` ⟨1⟩3); ML4-A (abstract matching-plus-C¹
cancellation lemma, ⟨1⟩2 there); ML2 (complete two-magnon resolution by
Jacobi diagonalization, NO Bethe-completeness assumption); ML5-A/ML5-B
(conditional universality on D24(c)/(d) classes); S2-2body and S2-2body-S
(exact two-body slope sgn(v_h−v_s)/S for every site spin S). REFUTED rows
you must not rely on and must not contradict: ML5 (unrestricted
universality — the O_η counterexample D24(e)), S2 (superseded label),
M-INDEX-LA-strong. The fixed-N on-shell uniformity refuted by ML4-Q1 must
not be smuggled back in.

Order of limits, ALWAYS: infinite-volume dynamics first, then t→±∞ /
on-shell filtering at fixed window and fixed packet width, then window→ℤ
and packet-width→0 in the order YOUR theorem states explicitly, and
k_s→0 (equivalently soft-packet scale ε→0) STRICTLY LAST. The soft limit
commutes with nothing; every statement must name its limit order.

New hypotheses may be introduced ONLY as numbered proposals (D29, D30, …)
in a MERGE PROPOSALS section of your shard; definitions.md is not your
lane.

## Lane S1 — THEOREM S-INDEX (the soft law as a constraint on limit points)

### The structural move (understand this before writing anything)

Memory dodged H-AD-G by making the OBSERVABLE protocol-explicit (the TPM
window charge). The soft corner dodges ML5 by making the SOFT LEG
protocol-explicit: the soft insertion is the smeared broken charge current
itself — the leg created by `Q[f_ε]` / `J^-[f_ε]` with `f_ε(k)=ε^{-1/2}f(k/ε)`
a fixed rescaled soft packet — not an arbitrary local source. The O_η
counterexample (D24(e)) deforms the SOURCE of the soft leg; a
charge-created leg has no such freedom. Process-independence then
quantifies over the HARD process only, and the Ward identity is exactly
the statement that constrains charge-created insertions (R14, ML4-Ward).
Arbitrary sources re-enter only through the PROVED bridge ML5-A: a source
inherits the law iff its contact first jet vanishes (`𝔠_h(O)=0` and
`M_2^O(0,·)=0`). Do not try to beat the O_η counterexample; route around
it exactly as stated.

### Target statement (template — sharpen, weaken, or split as the proof demands)

**ASSUME (H-SIDX).**
1. D6--D8 register for the concrete anchor; but state the theorem at the
   abstract level wherever you honestly can: a U(1)-broken/SU(2) FM vacuum
   with magnon band, D26(INT), vacuum tail density ρ (= site spin s in the
   fully polarized case; carry ρ, do not assume s∈½ℤ — the M-IDX-density
   row is the precedent for keeping ρ free).
2. **(PROTO — the protocol object; formulate as D29.)** Define the
   finite-volume, finite-window, packet-smeared soft amplitude datum
   𝒜_{N,W,σ}(ε): the connected on-shell pairing between (hard packet data
   g, prepared and resolved in the window W with width parameter σ) with
   and without one charge-created soft leg Q[f_ε], normalized as a
   multiplier in the D24(b) norm. Building D29 so that (i) it is
   computable in finite volume (the falsifier probes it), (ii) it does not
   presuppose wave operators, and (iii) its ε→0 asymptotics are meaningful
   on every subsequence, is HALF THE THEOREM'S VALUE. The ML4-Q1 √N
   refutation tells you the unsmeared object diverges — the smearing and
   the window discipline are load-bearing, not cosmetic.
3. **(TGT — tightness/regularity, the (LR)-analogue; formulate as D30.)**
   The weakest hypothesis you can state on the family {𝒜} making the
   subsequential first-order jet at ε=0 well-defined — e.g. uniform local
   boundedness + equicontinuity of the rescaled family, or tightness of
   an associated spectral family. NO convergence assumed; NO existence of
   a scattering theory assumed. Formulating the WEAKEST sufficient (TGT)
   is the other half of the value.

**PROVE.**
(S-IDX.0) *Finite-volume index identity (UNCONDITIONAL — this is the
   analogue of M-INDEX-fin; get it airtight, it alone is publishable).*
   In every finite sector, for every hard packet in ker S^+, the
   descendant-channel component of the charge-created soft amplitude is
   EXACTLY the charge datum: the Ward projection (ML4-Ward (9)--(11))
   pins P_{n,N}J^-_0 = 2Q_0J^z_0/(N−2n) — no dynamics, no k_s expansion,
   valid for every N, every n<N/2, every packet. Restate this as a
   finite-volume soft-index identity for the D29 object: the descendant
   part of 𝒜 at ε=0 equals (leg-charge datum)×(hard velocity datum) with
   the kinematic factor (e^{ik_s}−1) separated explicitly (R10 does the
   separation; keep its two terms distinct in public). The offset/
   normalization bookkeeping (N−2n vs N−2 vs 2ρ) must be done in public —
   this is where the critic will attack first.
(S-IDX.1) *Subsequential soft law (conditional on D29+D30; the heart).*
   For ANY subsequential limit point 𝖲*(·) of the rescaled datum family
   (any subsequence of (N,W,σ,ε) respecting the stated limit order):
   (i) Adler zero: 𝖲*(0)=0;
   (ii) slope rigidity: ∂𝖲*|_0 exists along the subsequence and equals
        the universal charge datum — for a single hard magnon leg of
        charge q over tail density ρ:
            ∂_{k_s} arg 𝖲*|_0 = sgn(v_h−v_s)·|q|/ρ,
        anchored: = 2 on D8 at ρ=1/2, = 1/S for the spin-S family
        (S2-2body-S — an exact-match obligation, see (S-IDX.3));
   (iii) the value is subsequence-independent (the law, not the limit,
        is unique) — if your (TGT) buys uniqueness of the jet, say
        exactly what clause buys it, mirroring D27's convenience clause.
   NO claim that limit points exist; NO channel inventory; bound states
   and extra bands ALLOWED — they may make some subsequences empty or
   carry different hard data, they do not break the constraint.
(S-IDX.2) *Source bridge (cheap; cite, do not reprove).* Any D24(a)
   source with M_2^O(0,·)=0 and 𝔠_h(O)=0 inherits (S-IDX.1) with M_1^O
   in place of the charge-created hard amplitude — this is ML5-A applied
   to the limit-point formulation; state it as a corollary and check the
   hypotheses actually port (the D24 norms are per-(N,W,σ) here — say
   how they enter the subsequence).
(S-IDX.3) *Consistency anchors (any mismatch is a FATAL bug in your
   proof).* (a) On the D6--D8 FM chain, where ML1-free finite-volume data
   are exact, the law reduces to S2-2body's boxed (R17)--(R18). (b) For
   the spin-S family, to S2-2body-S's slope 1/S. (c) If two-magnon wave
   operators are ASSUMED (ML1 as a hypothesis, not proved), the limit
   points exist and (S-IDX.1) reproduces the S2 EXPLORATION box of
   soft-current-recon.md ⟨1⟩6 — i.e. the old conjecture becomes the
   value-computation corollary of the new theorem, exactly as M-quant-G
   became the value-computation corollary of M-INDEX-spec.

### Known landmines (the critic WILL attack exactly here)

- **The vacuous-truth attack.** A constraint on limit points of a family
  with NO limit points is empty. You must either (a) exhibit one nonempty
  instance (finite-volume exact data suffice if your D29 is honest), or
  (b) state explicitly that nonvacuity is Lane S2's/the probe's burden
  and scope the claim as conditional. Silence here is a MAJOR objection.
- **Limit-order smuggling.** Every ε-derivative must be taken AFTER the
  (N,W,σ) subsequence is fixed. If your proof needs an interchange, prove
  it or put it in (TGT) explicitly. The ML4-Q1 √N counterexample is the
  red test: your formulation must be demonstrably immune to it — say in
  one displayed line why k_s=2π/N at fixed N does not refute you.
- **The kinematic-factor conflation (REFUTED row G0-soft-r1).**
  (e^{ik_s}−1) from the profile alone is NOT a soft factor. The Adler
  zero of 𝖲* must come from the current structure (R10's ω(k_s)/(z_s−1)
  coefficient and the contact cancellation), not from the bare difference
  factor. TRIANGLE.md §1.5's negative row is the fence; cite it.
- **Descendant vs orthogonal contact.** The Ward projection computes the
  descendant part ONLY; the complementary vector is NONZERO (R15 and the
  line after it). Your (S-IDX.1) must control the orthogonal part via
  D30/ML4-A-style regularity of the LIMIT family, not by assuming it
  away. If you cannot control it, the honest fallback is a law for the
  descendant-projected datum — state it as such, prominently.
- **ML5.** Nothing you prove may imply unrestricted source universality;
  O_η (D24(e)) survives every formulation. If your statement quantifies
  over sources anywhere, the D24(c) zero conditions must appear as
  hypotheses.
- **s>0 is a real number** (ρ free); nothing may assume ρ∈½ℤ. 2ρ∈ℤ is a
  THEOREM (M-IDX-density) under its own hypotheses, not an assumption.
- **δ vs S normalization.** Slope of arg S_phys vs multiplier 𝖲: keep
  D25's normalization and the D7 out/in convention; the sgn(v_h−v_s)
  labelling subtlety (oracle r2 residue 4) must be carried, not dropped.
- Fallback ladder (L5-honest): S-IDX-full (jet convergence proved from
  clustering/band data) > S-IDX-spec (constraint under explicit (TGT)) >
  S-IDX-fin only (finite-volume index identity — nearly free given
  ML4-Ward; landing ONLY this is a FAILURE of the campaign, say so
  honestly if it happens).

### Ground truth you may cite (L3 — only these, only from refs/)

Everything already in theory/ at its DAG status (L5 — check
claims/CLAIMS.md before leaning on any row). refs/arxiv-1412.2970
(Haag-Ruelle for gapped spin systems — for the shape of packet/velocity
estimates only; S1 must NOT assume its conclusions), refs/arxiv-1103.2286
and refs/arxiv-1810.07006 (excitation ansatz), refs/arxiv-1305.2176
(style/statement register). Citing a result from memory without a refs/
file = FATAL objection.

## Lane S2 — THEOREM AC-EX-2M (two-magnon wave operators from ansatz bands)

### Target statement (template)

**ASSUME (H-ACE2M — formulate as D31, modelled on D28 but STRICTLY over
one translation-invariant vacuum).** D1/D2(a) injective covariant vacuum;
an isolated magnon band k↦ω(k), C^∞ on the packet support, given by an
EXACT excitation-ansatz band map (exactness is a hypothesis, as in D28(3));
two D12(a′) packets with disjoint compactly separated group-velocity
supports, both velocities nonzero, total energy below every inelastic
threshold expressible in band data (display the inequalities); a
two-sided clustering inequality analogous to (D28-C) — for the
translation-invariant vacuum this should FOLLOW from D2/transfer-matrix
gap rather than be assumed; derive it if you can (that alone upgrades the
lane), assume it displayed if you cannot.

**PROVE.**
(A2M.1) Cook existence: the two-magnon precursor states converge as
   t→±∞. This is refs/arxiv-1412.2970's actual setting (two particles,
   one translation-invariant vacuum) — the work is to run it from EXACT
   ansatz-band hypotheses instead of their spectral assumptions, reusing
   the ACE machinery (momentum-filtered creators, ACE-tail, ACE-SP named
   computations of theory/ansatz-scattering.md) wherever it genuinely
   ports. Identify explicitly which steps are VERBATIM ports (cite shard
   + step), which are new, and which of 1412.2970's hypotheses the exact
   ansatz bands replace.
(A2M.2) W_± are isometries on the packet domain; the constructed
   in/out two-magnon spaces carry the D7 labels on the Bethe model
   (consistency: on D6--D8 the constructed channel matches ML2's Jacobi
   spectral decomposition — an exact-match obligation, ML2 is PROVED).
(A2M.3) *Nonvacuity bridge to Lane S1:* on the constructed channels, the
   D29 protocol datum (as proposed by S1 — you may cite its INTENDED
   interface: the connected on-shell pairing with one charge-created
   soft leg; if S1's final D29 differs, the merge is the orchestrator's
   burden, state your interface assumptions in one place) has limit
   points along the stated limit order, for hard packets in the
   constructed domain and soft scale ε→0 LAST; i.e. Lane S1's (TGT) holds
   on ran W_±-vectors. State this as conditional on precisely-named
   regularity of the constructed wave operators in the soft parameter if
   you need it (the AC-EX precedent: fixed-packet only, NO soft-uniform
   claims — the soft limit is taken on the AMPLITUDE data, never inside
   the wave-operator construction).

### S2 landmines

- The soft limit k_s→0 violates every velocity-separation hypothesis;
  A2M is a FIXED-packet theorem. The composition with S1 works because
  ε→0 is taken on the datum family, not inside Cook estimates. Keep this
  order visible in every display; the critic will hunt for one place
  where ε enters a Cook integral.
- ML1 asked for MORE than you need: channel norms, endpoint behavior,
  bound-state isolation. Do not claim to close ML1. Claim exactly
  (A2M.1)--(A2M.3); state in HONEST STATUS which ML1 sub-items remain
  open (endpoint packets, equal velocities, the bound band — the
  two-string is PRESENT on D6 (ML2), so your velocity separation must
  explicitly exclude/isolate it: say how, D28's P_T precedent).
- Exactness register: if ansatz states are exact band eigenstates say
  EXACT (D28's discipline); if approximate, the error enters Cook's
  integral quantitatively — choose one register and keep it.
- 1412.2970 citation discipline: cite file + section/equation from
  refs/arxiv-1412.2970/Scattering_spin-AHP1.tex; a from-memory citation
  is FATAL.

## Pre-registered falsifier (orchestrator lane; frozen BEFORE proofs land)

`theory/checks/soft_index_probe.py` (ED, D6 register + spin-1 where
feasible), criteria frozen in this brief:
- **P1 (slope law):** windowed packet-smeared charge-created datum on
  rings N≤20, extrapolated slope of arg 𝖲 must land within 5% of
  sgn(v_h−v_s)/S for S∈{1/2,1} on D8-interior packets. FAIL kills
  (S-IDX.1)(ii) as stated.
- **P2 (protocol dodge, decisive):** with the O_η-created soft leg the
  measured slope must SHIFT by the D24(e) prediction 2iη(1−e^{−3ih})
  within 8%; with the charge-created leg it must be η-INDEPENDENT to
  1e-10. FAIL of the second half kills the D29 design.
- **P3 (limit-order discipline):** at fixed N the raw on-shell sequence
  k_s=2π/N must REPRODUCE the ML4-Q1 √N growth (the probe must be able
  to see the disease), while the D29-smeared datum at the same N stays
  bounded. This is the red-capability certificate of the probe itself.
- **P4 (exploratory, non-gating):** two-string (charge-2) hard leg —
  record the measured slope against |q|/ρ=2/ρ; pre-registered as
  EVIDENCE for the Bc |q|>1 factor (tns-ebh), not as a gate on S1.
Mutation discipline: every P-row gets a --red mode with nonzero exit;
no bare asserts; runs under python3 -O.

## Output contract (all lanes; L6b)

Your ONLY writable file: your shard (stated in your lane brief) — Lamport
hierarchical proofs (⟨1⟩1, ⟨2⟩3, ASSUME/PROVE per nontrivial step, QED
steps, every leaf citing a D-number, a claim id, a named computation, or a
refs/ file+location), plus a final section: (i) MERGE PROPOSALS (exact
replacement text for definitions.md D29/D30/D31, claims/CLAIMS.md new
rows at status SKETCH, notation.md rows if needed); (ii) CHECKER SPEC — a
concrete machine-checkable certificate for at least one load-bearing step
(what to compute, on what model, expected value, and a mutation that must
fail); (iii) HONEST STATUS — what you proved, what you assumed, what
broke. Self-status is SKETCH; only the L6 loop promotes. Do not edit any
shared file. Do not touch numerics/ or theory/checks/. Work fully
autonomously; never ask questions.
