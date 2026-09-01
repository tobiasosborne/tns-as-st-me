# Lecture 2 digest — Large Gauge Symmetry in Massless QED

- **Title (as posted):** Infrared Structure of Gravity and Gauge Theory, Lecture 2 of 10
- **Video id:** `yeMZKViadhw`
- **URL:** https://youtu.be/yeMZKViadhw
- **Duration:** 01:57:03
- **Written companion:** arXiv:1703.05448 §2.5–2.8 (conserved charges, canonical electrodynamics at scri, large
  gauge symmetry, Ward identity, mode expansions)
- **Source:** `refs/strominger-videos/02-yeMZKViadhw.md` (auto-captions; secondary source, not L3 ground truth)

**Arc.** Recap of the antipodal matching condition, then the machine is built in four moves: integrate the charge
by parts using the constraint equation on null infinity to split it into a soft and a hard piece; construct the
covariant symplectic form on scri and invert it to get commutators, being careful to separate the `u`-independent
part of the gauge field; show that the charge generates angle-dependent large gauge transformations on both the
radiation field and the matter; and then convert the resulting conservation law into a Ward identity for the
S-matrix. The last half hour is a change of language — from fields on null infinity to the plane-wave creation and
annihilation operators of a standard QFT course — ending with the dictionary between the two.

**How to read this digest.** Side-channel harvest, per the campaign brief: derivations that the written notes
already contain are omitted, and what is recorded is the framing, the warnings, the audience exchanges and the
honest status labels around them. The "Deltas" section is the organizing principle and also lists the checks where
an apparent aside turned out to be in the notes.

---

## Insights

1. **He asks the class to correct his equations and says plainly that he makes a lot of mistakes.** Small, but it
   is the register in which the whole course is conducted, and it explains why several live corrections survive in
   the recording.
   > "I am very appreciative of uh corrections to my equations because I to make a lot of mistakes"
   `[yeMZKViadhw @ 00:09:23]` — tags: methodology

2. **On extending the gauge parameter into the bulk: any extension gives a true relation, but only a good one
   gives a useful relation.** This is the general shape of his method — the freedom is real, and the work is in
   spending it well rather than in checking correctness.
   > "we could integrate by parts and choose Epsilon to be anything we wanted and the relation would still be true
   > while true it wouldn't be so useful [...] it behooves us to find a nice way to extend Epsilon"
   `[yeMZKViadhw @ 00:15:40]` — tags: large-gauge, methodology

3. **The no-magnetic-monopole assumption is flagged as temporary and load-bearing, with a promise that everything
   gets corrected once it is dropped.** He is explicit that this is a simplification for the sake of studying one
   thing at a time, not a physical statement.
   > "we're going to assume this and for now we are assuming that we are describing a theory with no as[ymptotic]
   > States carrying magnetic charge [...] later on we are going to include magnetic monopoles we can no longer
   > [im]pose this assumption and in fact everything is going to get corrected in a very interesting way but I'm
   > trying to keep it simple"
   `[yeMZKViadhw @ 00:27:37]` — tags: charges, methodology, pitfalls

4. **His spoken heuristic for why the extra term deserves the name "soft": imagine inserting a factor `e^{iωu}` in
   the `u`-integral; the expression as written simply has no `ω`, so it is the zero-frequency Fourier component,
   and because it is linear in the field it creates or annihilates one photon of zero energy.** The written notes
   assert the name and defer the justification; this is the route he actually gives out loud, and it is exactly the
   DC / zero-frequency framing.
   > "if we were to put in here an e to the I Omega U this would be a Foria [Fourier] component with frequency
   > Omega of the electromagnetic field [...] but there is no Omega in this expression this term isn't there so
   > it's as if we took Omega to zero so this thing creates and annihilates soft particles"
   `[yeMZKViadhw @ 00:23:16]` — tags: soft-theorems, dressing, methodology

5. **He stops the lecture and makes the class compute the coefficient of the soft-photon pairing in the symplectic
   form.** Of everything on the board, the step he judges worth two minutes of everyone's attention is the pairing
   of the soft photon mode `N` with the boundary field that is the *sum* of the endpoint values of the gauge field.
   > "what this equation says is that the components of a that have a fo[urier] transform are paired with each
   > other in the simplec[tic] form and the soft Photon mode is paired with this field C that it's the sum of the
   > boundary [values] [...] I want you to try to compute what this number is and you should compare with your
   > neighbor"
   `[yeMZKViadhw @ 00:50:44]`, answer given at `[yeMZKViadhw @ 00:55:49]` — tags: methodology, vacuum-degeneracy,
   dressing

6. **A student supplies the physical picture for the antipodal map, and he endorses it: a free particle that flies
   through the middle enters at one angle and leaves at the opposite one.** This is the one-sentence intuition for
   why the matching is antipodal rather than identical, and it is not in the written notes.
   > student: "if you like consider one particle without [interaction] just fly through the center right just the
   > in the past you count the charges from that angle in the fut[ure] goes to [the opposite] point"; reply:
   > "yeah yeah it's not surprising when you think about it the right way"
   `[yeMZKViadhw @ 01:12:34]` — tags: charges, asymptotic-symmetries, methodology

7. **He admits that his own charge normalisation, chosen so charges come out as integers, is awkward for the field
   theory half of the course.** Useful warning for anyone transcribing his formulas into standard conventions.
   > "these qks are not the conventional electric charges these qks are integers [...] this is the simplest
   > convention for this though for field Theory which I'm going to discuss in a few minutes it's an awkward
   > convention"
   `[yeMZKViadhw @ 01:13:38]` — tags: pitfalls, methodology

8. **The standard slogan "physical states are invariant under all gauge transformations" is only true for gauge
   transformations that are trivial at infinity.** He states this as the conceptual crux: large gauge symmetries
   act non-trivially on the Hilbert space precisely because they do not die off.
   > "you usually you would think that states in a gauge Theory are annihilated by all inv[ariant] under all gauge
   > Transformations but that's only true when the gauge Transformations are behaving trivially at infinity and in
   > some cases there are large gauge symmetries that act non-trivially on the Hilbert space"
   `[yeMZKViadhw @ 01:14:42]` — tags: large-gauge, pitfalls, vacuum-degeneracy

9. **He describes the route by which he actually discovered these symmetries: gauge-fix, look at what residual
   gauge transformations survive, do an asymptotic expansion, and see what is left over.** The written notes say
   the symmetries were first found this way but do not give the recipe.
   > "indeed that was how I originally found these symmetries you might try to find them by just by doing some
   > gauge fixing and looking at what the residual gauge Transformations are and doing an as[ymptotic] expansion
   > and seeing what what what it what is left over"
   `[yeMZKViadhw @ 01:15:48]` — tags: history, methodology, large-gauge

10. **His working definition of a Ward identity, given twice in response to questions: the charge commutes with the
    S-matrix, which (since `S = lim exp(iHT)`) is the same as commuting with the Hamiltonian; and more loosely, any
    relationship between objects implied by a symmetry.** Worth having because the campaign uses the term in a
    lattice setting where the S-matrix framing does not transfer directly.
    > "the word identity are just the dynamical consequences from the fact that the conserved charges commute with
    > the S Matrix or in other words since the S Matrix can be thought of as the exponential of I HT [...] it's the
    > same as the statement that the charges commute with the hamiltonian"; and later, "ward identity is a pretty
    > general term which means relationships between objects that are [im]plied by symmetries"
    `[yeMZKViadhw @ 01:16:52]` and `[yeMZKViadhw @ 01:20:08]` — tags: ward-identities, methodology

11. **The plainest possible statement of what the conservation law asserts, given when he exponentiates the
    charge: if in-state X evolves to out-state Y, then the large-gauge transform of X evolves to the large-gauge
    transform of Y.** No indices, no soft factors — this is the content.
    > "if we exponentiate the charge to get a generator of the finite symmetry it's just the statement that if you
    > have some instate X that evolves to an outstate Y and then you do a large gauge transformation on the instate
    > X it will evolve to a large gauge transformation on the outstate Y"
    `[yeMZKViadhw @ 01:17:55]` — tags: ward-identities, large-gauge

12. **He labels his own bracket computation semi-classical and outsources the quantum question.** The Ward identity
    as derived holds provided the charges are conserved quantum mechanically and free of anomalies; the actual
    verification is deferred to Feynman diagrams rather than attempted in the scri language. This is a candid
    statement of what is and is not established at this point in the argument.
    > "this was really kind of a semi-classical discussion and now this is the Quantum version of the statement
    > that the charge is conserved"; and, answering a question about loops, "you could say if these charges are
    > conserved in the quantum theory and don't have anomalies then this will be true we can check what the quantum
    > version of this statement is and we can verify directly using [Feynman] diagrams as we'll see that it is true"
    `[yeMZKViadhw @ 01:19:06]` and `[yeMZKViadhw @ 01:22:17]` — tags: ward-identities, open-problems, methodology

13. **Asked whether one could define these charges on intermediate slices rather than only at the boundaries, he
    says yes and admits he does not know whether anything is to be learned from it — though the black-hole work did
    something of the kind.** An honest "don't know" about a natural generalisation.
    > "you could also if you wanted take surfaces like this and Define charges at intermediate times it's
    > especially it's I don't know if there's more to be learned from that or not well in fact when we were
    > applying this to black holes we were doing thing[s] like that"
    `[yeMZKViadhw @ 00:35:19]` — tags: charges, black-holes, open-problems

14. **Why pushing the Cauchy surface all the way up to null infinity is legitimate, in his words: the symplectic
    form does not depend on the slice ("there's a million papers on that"), and at scri everything has spread out
    and become weak, so the theory there is essentially free.** He also concedes that the resulting commutators
    look nothing like the textbook ones — "it's not at all obvious that these are the same" — even though they are.
    > "it's straightforward to show that this simplec[tic] form does not depend on the surface Sigma [...] there's
    > a million papers on that"; and "it's not at all obvious that these are the same as what you've seen in
    > [Physics] 253 but of course they are"
    `[yeMZKViadhw @ 01:35:16]` — tags: methodology

15. **Before proving anything, he says the identity already "looks very suspicious" — both sides relate an
    amplitude to the same amplitude with a soft photon inserted.** A small but characteristic move: name the
    structural coincidence first, then do the work to make it an equality.
    > "it's already looking very suspicious because indeed those soft theorems relate give a relationship between
    > any S Matrix element and the same S Matrix element with a soft Photon inserted"
    `[yeMZKViadhw @ 01:33:08]` — tags: soft-theorems, methodology

16. **A live slip and correction about hermiticity of the transverse gauge field.** Not deep, but it flags a
    genuinely easy confusion: `A_z` is not hermitian — roughly `a_x + i a_y` — so the conjugate operator creates the
    opposite helicity at the same point.
    > "yeah okay so if we were to actually no of course this isn't [hermitian] sorry of course this isn't
    > [hermitian] because AZ is not real AZ is roughly ax plus I a y [...] sorry I said something wrong there if we
    > took the Herm[itian] conjugate of this we would get a z bar which would do the opposite thing"
    `[yeMZKViadhw @ 01:55:46]` — tags: pitfalls

---

## Structure of the argument (thin skeleton)

- `00:00:47–00:10:24` — Recap: five infinities, retarded/advanced coordinates, antipodal matching. (Written notes
  §2.2–2.4.)
- `00:11:24–00:20:02` — Charge in components; constraint equation on scri; integrate by parts; split into soft and
  hard terms. (§2.5.)
- `00:23:16–00:31:56` — Why the first term is a soft photon; Bianchi identity plus no-monopole assumption gives
  `N` real; `N` is the shift in `A_z` across scri. (§2.5–2.6.)
- `00:36:23–00:49:38` — Covariant symplectic form; separating the `u`-independent piece of `A_z`; the pairing
  exercise. (§2.6.)
- `00:55:49–01:06:01` — Commutators; the charge generates angle-dependent large gauge transformations. (§2.6.1,
  §2.7.)
- `01:09:14–01:15:48` — The hard term generates the matter transformation; the two together are the symmetry.
  (§2.7.)
- `01:16:52–01:31:02` — Ward identity for the S-matrix; hard side becomes a sum of charges weighted by ε at the
  entry angles. (§2.8.)
- `01:34:11–01:56:46` — Change of language to plane waves; the dictionary between scri fields and creation and
  annihilation operators. (§2.8, Mode Expansions.)

---

## Deltas vs the written lectures (arXiv:1703.05448)

**Present in the video, absent from the written notes:**

- The ω-insertion heuristic for the word "soft" (insight 4). The notes name the term and promise the justification
  later; the spoken version gives the reasoning at the point of naming.
- The student's fly-through-the-middle picture for the antipodal map and his endorsement of it (insight 6). This is
  the best short intuition in the lecture and has no counterpart in the notes.
- The recipe by which the symmetries were originally found — gauge-fix, residual transformations, asymptotic
  expansion (insight 9). The notes state only *that* they were first found this way, in §2.10.
- The two definitions of "Ward identity" given in response to questions (insight 10), and the state-to-state
  statement of what the conservation law asserts (insight 11). The notes derive the identity but never phrase it
  this way.
- The explicit semi-classical label on the bracket computation, and the conditional "provided there are no
  anomalies" caveat before handing verification to Feynman diagrams (insight 12).
- The "could we define charges on intermediate slices? I don't know if there's more to be learned" exchange
  (insight 13).
- The judgment that the no-monopole assumption is temporary and that "everything is going to get corrected"
  (insight 3) — the notes impose the boundary condition without the foreshadowing.
- The admission that his charge normalisation is awkward for field theory (insight 7).
- The classroom material: the request for corrections (insight 1), the two-minute pairing exercise and its answer
  (insight 5), the "million papers" aside and the "not at all obvious that these are the same" concession
  (insight 14), the live hermiticity correction (insight 16).
- The "already looking very suspicious" pre-proof observation (insight 15).

**Checked and *not* a delta:**

- "A tricky point which a lot of people had gotten wrong in the past", about care at the boundaries of scri — the
  notes say this almost word for word in §2.6 ("a tricky point, which was incorrectly treated in some of the
  literature until recently").
- The Fourier-transform argument for why the `u`-independent mode must be separated out, and the statement that
  without it the soft photon has no symplectic partner — §2.6.
- The `f(z,z̄) + g(w,w̄)` integration-function ambiguity in the boundary commutator and the decision to ignore it —
  §2.6.1.
- The "guess the mode expansion from locality and helicity" argument at `01:50:29` — §2.8 gives exactly this
  argument, including "what else could it do" reasoning about rotations about the point.
- "It would be incredibly surprising if after 90 years of QED we had found new relations — we have not; we have
  rediscovered known ones." This is *verbatim* in §2.8 of the notes, so despite sounding like an off-script
  honesty remark it is not a delta. (It remains the single most useful calibration sentence in the lecture, and it
  is worth quoting from the notes rather than the video.)
- That the theory at scri is essentially free because everything disperses — §2.6.

**Transcript quality.** Slightly noisier than lecture 1 in the algebra, mostly through symbol names. Normalisations:
"scry" / "scri" / "scrip" / "SC minus" = scri (null infinity); "simplec form" / "simplectric" = symplectic form;
"Foria" / "fored" / "48 transform" = Fourier transform; "bian identity" = Bianchi identity; "koshy" = Cauchy;
"nether construction" = Noether construction; "ailan" / "a billion" = abelian; "Herm Mission" = Hermitian;
"ficity" = helicity; "Makowski" / "mowy" = Minkowski; "physics 253" is the Harvard QFT course; "direct brackets" =
Dirac brackets. The field called `C` in the video is `φ` in the written notes — a genuine notational divergence to
watch. Several `[Music]` markers and one long silent gap during the class exercise (`00:51:59–00:55:49`).
