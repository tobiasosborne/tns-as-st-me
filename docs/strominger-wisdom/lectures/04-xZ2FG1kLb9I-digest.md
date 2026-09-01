# Lecture 4 digest — Massive QED, Hyperbolic Slicing, and Magnetic Soft Theorems

- **Title (as posted):** Infrared Structure of Gravity and Gauge Theory, Lecture 4 of 10
- **Video id:** `xZ2FG1kLb9I`
- **URL:** https://youtu.be/xZ2FG1kLb9I
- **Duration:** 01:53:41
- **Written companion:** arXiv:1703.05448 §2.12 (Massive QED, hyperbolic slices) and §2.13 (Magnetic charges), with
  §3 (the S-matrix as a celestial correlator) in the background
- **Source:** `refs/strominger-videos/04-xZ2FG1kLb9I.md` (auto-captions; secondary source, not L3 ground truth)

**Arc.** Two new results and a long closing reflection. The first half handles massive charged particles, which never
reach null infinity: extend the gauge parameter into the bulk in Lorenz gauge, note that the resulting Green's
function is the AdS₃ bulk-to-boundary propagator, slice Minkowski space hyperbolically, and observe that a free
massive particle asymptotes to a fixed point on the hyperboloid at timelike infinity — so the large gauge charge acts
on it by the value of the gauge parameter at that point. The second half asks whether the soft photon theorem is
exact non-perturbatively, argues that magnetic monopoles must correct it, derives the correction by a duality field
redefinition, and finds that the corresponding symmetry acts as an *imaginary* gauge transformation on the original
potential — a complexification of the gauge group. The lecture ends on the broader claim that not every asymptotic
symmetry can be presented as a subgroup of a local gauge symmetry.

**How to read this digest.** Side-channel harvest per the campaign brief: the derivations are in the written notes
and are omitted here. What is recorded is the framing, the opinions, the audience exchanges, and the places where he
says what is conjecture and what is proved. The "Deltas" section is the organizing principle.

---

## Insights

1. **A notation warning for anyone following along: he abandons the in/out superscripts partway through and adopts
   the all-outgoing convention in which incoming particles carry negated charge.** He says so cheerfully rather than
   carefully, and the change is easy to miss.
   > "there are different ways of writing this expression before I was putting superscripts out on their
   > superscripts and now they've gotten use[d] to it I'm going to drop those superscripts"; and "I guess I'm
   > getting lazier and lazier about writing all these things out"
   `[xZ2FG1kLb9I @ 00:06:33]` and `[xZ2FG1kLb9I @ 00:05:32]` — tags: pitfalls, methodology

2. **The framing that motivates the whole celestial-sphere language: standard quantum field theory is built so that
   translation invariance is manifest, but for this subject the Lorentz symmetry is what matters, and it acts simply
   on the sphere at infinity.** He points out that the flat metric wears translation invariance on its face while
   Lorentz invariance takes work to verify, and that the plane-wave basis is a choice made to serve the former.
   > "the minkowski coordinates [...] are manifestly invariant under translations [...] but if you want to verify
   > invariance under lorentz Transformations [...] it's a little more work you don't just look at it and see that
   > it's invariant [...] and all of quantum field theory in all the textbooks are developed in this kind of
   > formalism where [...] maintaining manifest translation invariance is the the Paramount consideration in
   > writing down any formula [...] now for many purposes the lorentz Symmetry is more important"
   `[xZ2FG1kLb9I @ 00:12:00]` — tags: celestial, methodology

3. **Honest calibration of what the celestial rewriting achieves: it is a change of language in which the symmetries
   become visible, not a source of new physics.** Worth pairing with the same sentiment about the Ward identities in
   §2.8 of the written notes.
   > "a lot of what we're doing now is just [re]phrasing old results in Quantum field theory in a different language
   > in which certain of its features in particular [the] symmetries become more evident"
   `[xZ2FG1kLb9I @ 00:16:18]` — tags: methodology, celestial

4. **Historical judgment: Penrose's programme tried to put all of physics at null infinity and got stuck precisely
   on massive fields, and nothing useful came out of that effort.** He adds, cautiously, that he thinks the right way
   to think about it has only recently been found.
   > "way back in the 60s and 70s Penrose and his group were trying to generalize this they wanted to think of
   > everything and you know in the Twister [twistor] program and so on they wanted to think of everything in terms
   > of structure [at null] infinity and but then there's a problem when you get to massive fields [...] there were
   > in fact an interesting series of papers people trying to uh makes find different ways of dealing with this but
   > nothing nothing useful was was ever really found within that program though I think recently we we've
   > understood the the right way to think about this"
   `[xZ2FG1kLb9I @ 00:26:01]` — tags: history, open-problems, methodology

5. **He rates a competing paper above his own and names the prejudice of his that was wrong.** Two papers solved the
   massive problem; his own avoided fixing a gauge on principle, and he now thinks the gauge-fixed treatment is both
   nicer and closer to the right structures.
   > "there are two papers on this problem one by myself and Monica and Dan another by campiglian Lada [Campiglia
   > and Laddha] a lot of paper is much nicer [Laddha's paper is much nicer] so [...] our paper is uh it's kind of
   > interesting our paper is we never chose a gauge I somehow had the idea that it was a bad idea to choose a gauge
   > but sometimes that's not true [...] the way that it worked out was so nice and it highlighted a lot of kind of
   > underlying structures which I think are really the correct way to think about the problem"
   `[xZ2FG1kLb9I @ 00:30:14]` — tags: history, methodology

6. **His criterion for a good gauge choice: not correctness, which is guaranteed, but whether the answer comes out
   without large cancellations you cannot explain.** A usable test for any choice of extension or frame.
   > "one should get the same answer no matter at the end of the day you should get the same answer no matter how
   > you do this but if you do it in a nice way it [...] should come out Simply if you do it in a bad way you'll
   > have all kinds of terms which cancel each other but it's not obvious why they should do so"
   `[xZ2FG1kLb9I @ 00:32:22]` — tags: methodology, large-gauge

7. **A surprise he flags as his own: the massless wave equation has solutions that do not fall off at null infinity
   at all, and they are invisible to the standard Fourier / energy-eigenmode treatment.** These are exactly the
   solutions the large gauge parameter needs. The written notes state the fact; only the spoken version says that the
   standard basis is what hides it.
   > "there's something really weird about this because when I studied the scalar [...] wave equation the first
   > thing that you do is [a] Fourier transform and go to modes of definite frequency and then you get radiative
   > solutions [...] and you find that they fall off like 1 over r [...] and it was a surprise to me though I guess
   > some people must have known it there are solutions to the massless scalar wave equation which don't fall off at
   > null Infinity they go to [a] constant at null Infinity [...] and so you miss it when you go to energy eigen
   > modes"
   `[xZ2FG1kLb9I @ 00:40:52]` — tags: pitfalls, dressing, vacuum-degeneracy, methodology

8. **He admits he never managed the direct integral and got the Green's function another way.** A small honesty
   marker about how the result was actually obtained.
   > "here's a formula for G you could try to do the integral I think it's a hard integral to do I think it's
   > probably easier to I never succeeded well I guess after you know the answer that tells you what the int[egral]
   > is"
   `[xZ2FG1kLb9I @ 00:44:05]` — tags: methodology

9. **He is deliberate about how the slice is terminated near timelike infinity, and says the limit is where the
   simplicity comes from.** In lectures 1–3 the boundary terms at future timelike infinity were simply dropped; here
   the whole point is to take that limit carefully, in a specific order.
   > "so I'm being very precise about exactly how I'm ending my slice near time like Infinity so I'm going to start
   > with a sl[ice] like this and then I'm going to take a limit as Tau goes to infinity and something very nice is
   > going to happen in that limit"
   `[xZ2FG1kLb9I @ 00:56:41]` — tags: charges, methodology

10. **The thing he stops the lecture to make the class derive is the asymptotic value of the hyperbolic radial
    coordinate, `ρ → |p|/m`.** That is the content of the whole construction: timelike infinity resolves into
    hyperbolic three-space in the same way null infinity is a line times a sphere, and a free massive particle
    asymptotes to a fixed point on it labelled by `|p|/m` and the direction of its momentum.
    > "I'm going to give you all two minutes I want you to find out what does rho go to"; then "so rho goes to the
    > absolute value of P over m [...] asymptotically if we have a particle any particle moving with constant
    > velocity in the absence of external forces asymptotes to one of these lines now Epsilon is constant along
    > these lines"
    `[xZ2FG1kLb9I @ 00:58:49]` and `[xZ2FG1kLb9I @ 01:05:07]` — tags: charges, methodology

11. **A slogan he states out loud and the written notes never quite do: one soft theorem for every globally
    conserved quantity — electric charge, energy-momentum, magnetic charge, angular momentum, "and then some others
    that are more mysterious".** This is a compact organizing principle for the whole programme.
    > "we've seen another lesson here for every globally conserved quantity we get one soft theorem [...] one is
    > electric charge [...] we saw that we got one from energy momentum conservation that was a s[oft] gravit[on]
    > theorem here we're getting one from magnetic charge conservation we're going to get more later on from angular
    > momentum conservation and then they're going to be some others that are more mysterious"
    `[xZ2FG1kLb9I @ 01:33:38]` (the sentence runs across the caption break into `01:34:42`) — tags: soft-theorems,
    charges

12. **A long exchange pinning down when the magnetic correction actually matters physically.** His answers: only if a
    magnetically charged state can appear in the final state; or, more usefully, in a low-energy effective theory
    built on a superselection sector containing monopoles, where the correction bites if the magnetic dipole moments
    change during the scattering. He explicitly disavows the picture of monopoles running in loops.
    > "if you are at energy so low that you cannot make an outgoing state which has magnetic charge then you would
    > never have to worry about this diagram"; "no I'm not advocating that we ever write Feynman diagrams with
    > monopoles going in loops"; "so there's a low energy effective field theory in the sector of the Hilbert space
    > [...] with n magnetic monopoles [...] and if [...] the magnetic dipole moments are changing through the
    > scattering process then the soft theorem will matter"
    `[xZ2FG1kLb9I @ 01:14:57]` through `[xZ2FG1kLb9I @ 01:18:14]` — tags: soft-theorems, charges, pitfalls

13. **He corrects himself mid-sentence from "prove" to "conjecture", and names a use for the result: soft factors
    must transform correctly under duality, which may constrain the duality properties of quantum field theories.**
    The notes record the conjecture; the possible application to duality is spoken only.
    > "I'm going to write down a formula which is probably I mean let me conjecture not prove that it's a
    > non-perturbatively exact formula for [soft] photon [scattering] and that is also of interest because [...]
    > there's a lot of studies of Duality [...] and now we have soft theorems [...] and they have to transform
    > properly under Duality Transformations and that may give interesting constraints on Duality properties of
    > quantum field theories"
    `[xZ2FG1kLb9I @ 01:20:20]` — tags: soft-theorems, open-problems

14. **A candid "I always get confused by that".** The factor of `i` relating the sphere component of the field
    strength to the magnetic field comes from the index ordering under complex conjugation, and he says it trips him
    up every time.
    > "so if you have an anti-symmetric so f z z bar but the complex conjugate of this is f z bar Z and that changes
    > the index order so f[z] Bar Z is not quite the magnetic field it's I times the magnetic field that's why that
    > I is sitting there I'll always get confused by that"
    `[xZ2FG1kLb9I @ 01:36:50]` — tags: pitfalls

15. **The magnetic case has an unsolved canonical problem, and he says his group is working on it and has not
    solved it.** Without the brackets, the statement about which symmetry the magnetic charges generate is an
    educated guess from duality covariance rather than a derivation — he is explicit about the difference.
    > "Computing the [Dirac] brackets when [there's] magnetic charge present and F[zz̄] is not zero at [scri plus
    > minus] is actually a problem which hasn't been solved actually we're working on it but we haven't solved it
    > yet and so we don't know we haven't shown [canonically] what symmetry these charges generate but it's obvious
    > what they should generate"
    `[xZ2FG1kLb9I @ 01:44:19]` — tags: open-problems, charges, methodology

16. **The closing reflection, and the strongest general claim of the four lectures: nobody ever promised that all
    interesting symmetries would be subgroups of some local gauge symmetry, and the magnetic example shows they are
    not.** He goes further than the written notes in two ways — he says these symmetries are *more* physical than
    gauge symmetries, and he frames the point as a revision of what "we used to think", ending with a deliberately
    open-ended note.
    > "nobody promised us [that] writing theories in terms with redundant degrees of freedom is kind of an arbitrary
    > procedure and nobody promised us that all the interesting symmetries could be understood as subgroups of some
    > particular presentation of the theory [...] that's what we used to think but now in this simple example we're
    > seeing that it's not true"; and "these symmetries the ones we're discussing are very physical they're more
    > physical than gauge symmetries they give you relationships they have [Ward] identities they give you
    > relationships between scattering amplitudes they constrain the theory [...] so the lesson here is that in many
    > cases we can get them as subgroups of local gauge symmetries but that's really only the beginning of the story"
    `[xZ2FG1kLb9I @ 01:50:44]` and `[xZ2FG1kLb9I @ 01:52:50]` — tags: asymptotic-symmetries, large-gauge,
    open-problems, charges

17. **A framing warning about a claim everyone repeats: "the soft theorem has no corrections" always means "no
    corrections in perturbation theory", and he says that is not what the words sound like.** He then observes that
    the natural non-perturbative test case is unavailable, because quantum electrodynamics does not exist as a
    theory.
    > "all the derivations you will often see in the literature of this statement that the soft theorem has no
    > corrections but when you look at it what is really meant is that it has no Corrections in perturbation Theory
    > [...] in some sense the soft theorem is exact in QED but QE[D] doesn't actually exist as a Quantum field Theory
    > because of the Landau pol[e]"
    `[xZ2FG1kLb9I @ 01:10:33]` — tags: soft-theorems, pitfalls, ir-divergences

---

## Structure of the argument (thin skeleton)

- `00:00:02–00:11:00` — Recap: asymptotic symmetry method, the soft photon theorem in standard form, conventions.
  (Written notes §2.9–2.10.)
- `00:11:00–00:17:25` — Manifest translation invariance versus manifest Lorentz invariance; scattering as a
  correlation function on the celestial sphere. (§3.)
- `00:17:25–00:24:55` — Recap of the diagrammatic derivation; gauge invariance implying charge and momentum
  conservation. (§2.9.)
- `00:24:55–00:33:26` — The massive problem stated: massive particles reach timelike infinity, not null infinity;
  the two papers and the choice to follow the gauge-fixed one. (§2.12.)
- `00:33:26–00:44:05` — Lorenz gauge, the harmonic condition on the parameter, the Green's function, and the
  non-decaying solutions of the wave equation. (§2.12.)
- `00:45:06–00:55:37` — Hyperbolic slicing; the Green's function as an AdS₃ bulk-to-boundary propagator; the
  parameter is independent of the slice. (§2.12, "Hyperbolic Slices".)
- `00:56:41–01:09:32` — Free massive worldlines asymptote to fixed points on the hyperboloid; the hard charge acts
  by the bulk parameter evaluated there; the soft theorem follows. (§2.12, "Soft Theorem".)
- `01:10:33–01:21:25` — Is the soft theorem non-perturbatively exact? Monopoles must correct it; the long question
  period about when this matters. (§2.13.)
- `01:21:25–01:34:42` — Duality as a field redefinition; the corrected soft factor; one soft theorem per conserved
  quantity. (§2.13.)
- `01:34:42–01:48:30` — The second infinity of charges; duality is local on scri and acts by multiplication by `i`;
  the unsolved bracket problem; complexified gauge group. (§2.13.)
- `01:48:30–01:52:50` — Closing reflection on asymptotic symmetries that are not gauge subgroups; forward pointer to
  the soft photino theorem. (§2.13–2.14.)

---

## Deltas vs the written lectures (arXiv:1703.05448)

**Present in the video, absent from the written notes:**

- The manifest-translation-invariance versus manifest-Lorentz-invariance framing (insight 2). Section 3 of the
  notes says the celestial correlator description is "computationally and conceptually more convenient" and that
  Lorentz acts as the global conformal group, but never explains the move as a choice about *which symmetry the
  formalism is built to make obvious*. This is the clearest statement of why the whole reformulation is worth doing.
- "Just rephrasing old results in a different language in which the symmetries become more evident" (insight 3),
  said of the celestial reformulation specifically. The notes' §3 says instead "no assumptions are being made here;
  we are simply rewriting the S-matrix in a different notation", which is the same idea in a flatter register.
- The account of Penrose's programme failing on massive fields, and that nothing useful came of that effort
  (insight 4). The notes cite one reference "for discussion" and say nothing about the history.
- Rating Campiglia and Laddha's paper above his own, and disowning his own instinct that fixing a gauge is a bad
  idea (insight 5). The notes say only "despite making a specific gauge choice, the discussion of the second paper
  is more illuminating".
- The criterion for a good gauge choice — no unexplained cancellations (insight 6).
- That the standard energy-eigenmode treatment hides the non-decaying solutions, and that this surprised him
  (insight 7). The notes state that such solutions exist and have no Fourier transform, without the warning about
  what the standard basis conceals.
- The admission that he never did the Green's function integral (insight 8).
- The emphasis on how the slice is terminated and the limit taken (insight 9).
- The slogan "one soft theorem for every globally conserved quantity", with the list and the tail "and then some
  others that are more mysterious" (insight 11). The phrase does not occur in the notes; the individual cases do.
- The entire question period on when the magnetic correction is physically relevant — final-state monopoles,
  superselection sectors, changing magnetic dipole moments, and the disavowal of monopoles in loops (insight 12).
  The notes state the correction and its conjectured exactness without any discussion of its regime of relevance.
- The self-correction from "prove" to "conjecture", and the suggestion that soft theorems may constrain dualities
  (insight 13). The notes record the conjecture but not the application.
- "I'll always get confused by that", about the factor of `i` (insight 14).
- That his group is actively working on the magnetic bracket problem and has not solved it, and the explicit
  labelling of the magnetic symmetry statement as a guess from duality covariance (insight 15). The notes state the
  problem is open; they do not say it is being worked on or flag the guess as a guess in the same way.
- The closing riff's two extra moves: that these symmetries are "more physical than gauge symmetries", and that the
  gauge-subgroup expectation is a belief being revised rather than a fact being reported (insight 16). The written
  §2.13 makes the logical point but not the epistemic one.
- The framing warning that "no corrections" always silently means "in perturbation theory" (insight 17).
- The notation-drift warning (insight 1) — the notes adopt the all-outgoing convention cleanly in a footnote, so a
  reader of the notes never faces the mid-stream switch a viewer does.

**Checked and *not* a delta:**

- That Lorenz gauge "knows about" the antipodal map, and the hindsight remark that this is unsurprising because both
  the gauge condition and the matching are Lorentz invariant — §2.12 says this explicitly.
- That the Green's function is the AdS₃ bulk-to-boundary propagator and that we are "beginning to see the holographic
  structure of AdS₃ echoing in Minkowski space" — §2.12.
- That other conformal weights would bring `τ`-dependence — §2.12.
- That massive particles have no definite point on the celestial sphere and must be smeared — §3.
- That duality here is a field redefinition and not an assumed symmetry of the theory — §2.13.
- That the duality relation is non-local in the bulk but becomes local on scri, acting by multiplication by `i` —
  §2.13.
- That QED does not exist because of the Landau pole, and that all known non-perturbative completions he is aware of
  contain monopoles — §2.13.
- That the magnetic Dirac brackets are an important open problem — §2.13 (the delta is only the "we're working on
  it" and the guess-labelling).
- That the `N=1` soft photino theorem implies infinitely many fermionic symmetries which cannot be a subgroup of the
  four supersymmetries — §2.14.

**Transcript quality.** The weakest passage is the two-minute class exercise at `00:59:50–01:03:59`, which is mostly
dead air and side chatter ("which are yours can I borrow one") with the derivation happening on the blackboard; the
result is recovered at `01:03:59` but the working is not in the text. The names in insight 5 are mangled: "Monica
and Dan" are Monica Pate and Daniel Kapec, and "campiglian Lada" / "Kim Piggly a lot of" is Campiglia and Laddha —
the ASR renders the latter three different ways within two minutes, and at `01:09:32` "Kim Piggly a lot of were
advocating" should read "Campiglia and Laddha were advocating". Other normalisations: "Twister program" = twistor
programme; "ashdikar" = Ashtekar; "decider" / "anti-decider" = de Sitter / anti-de Sitter; "Roe" = rho; "hjj duel" =
Hodge dual; "lse" / "LSC reduction" = LSZ reduction; "Manton" (in "like the Manton where you have monopole
scattering") = Manton, i.e. monopole moduli-space scattering; "gut theories" = GUTs; "direct quantization condition"
= Dirac quantization condition; "sulfotino" / "softino" = soft photino. Several `[Music]` markers mask a few seconds
each.
