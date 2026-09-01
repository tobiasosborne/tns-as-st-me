# Lecture 3 digest — Asymptotic Symmetries and Soft Theorems

- **Title (as posted):** Infrared Structure of Gravity and Gauge Theory, Lecture 3 of 10
- **Video id:** `swrNwD0ypaE`
- **URL:** https://youtu.be/swrNwD0ypaE
- **Duration:** 01:48:15
- **Written companion:** arXiv:1703.05448 §2.8–2.10 (Ward identity, soft theorems, Feynman diagrammatics,
  asymptotic symmetries), with a forward glance at §5.2 (supertranslations)
- **Source:** `refs/strominger-videos/03-swrNwD0ypaE.md` (auto-captions; secondary source, not L3 ground truth)

**Arc.** Three movements. First, a ten-minute preview of the gravitational analogue — the Bondi mass aspect in place
of the electric field, supertranslations in place of angle-dependent gauge transformations — used mainly to draw a
contrast about observability. Second, the traditional asymptotic-symmetry-group method presented as an alternative
and less rigorous route to the same large gauge transformations, with its history (ADM, Brown–Henneaux, BMS) and its
soft spots. Third, the completion of the previous lecture's programme: rewrite the Ward identity with the special
gauge parameter `1/(z−w)`, compare it with Weinberg's soft photon theorem, and then review the standard Feynman
diagram derivation of both the soft photon and soft graviton theorems, ending on the observation that gauge
invariance of the soft factor is equivalent to global charge (respectively momentum) conservation.

**How to read this digest.** Side-channel harvest per the campaign brief. Derivations that the written notes contain
are omitted; what is recorded is the framing, the judgments, the history and the honest status labels. The "Deltas"
section is the organizing principle and lists both what is new and what was checked and found already written.

---

## Insights

1. **He could have given the entire course in gravity, and notes an oddity: gravity has more indices but the
   concepts are more familiar there.** Half a century of BMS work means the gravitational versions of these ideas
   had names before the electromagnetic ones did.
   > "even though electromagnetism is simpler than gravity there's fewer indices oddly a lot of the concepts that
   > we talk about are sort of more familiar in gravity than in electromagnetism"; and later, "it's kind of odd
   > that the symmetry of gravity was at least partially understood 50 years ago whereas [...] electromagnetism was
   > only understood in this language in the last few years"
   `[swrNwD0ypaE @ 00:01:19]` and `[swrNwD0ypaE @ 00:08:45]` — tags: history, methodology

2. **The sharpest observability contrast in the course: in electromagnetism the large gauge action is on phases, so
   you need quantum interference to see it; in gravity the same structure is an angle-dependent shift of time
   itself, which has classical consequences.** This bears directly on the question of what counts as an observable
   in each corner of the triangle.
   > "a gauge transformation a phase on a on a state in classical electromagnetism the phases are unobservable
   > so in order to talk about [...] observable consequences of these angle dependent gauge transformation we have
   > to talk about [...] Quantum interference and here [...] we have a an actual physical time translation so if we
   > start moving things around translating them forward or backward at time it different in [an] angle dependent
   > way on the sphere that is something which has a classically observable consequence"
   `[swrNwD0ypaE @ 00:06:37]` — tags: memory, large-gauge, methodology

3. **He states plainly that there are more symmetries and more soft theorems in electromagnetism than he has shown,
   and that the sequencing is a limitation of exposition, not of the subject.**
   > "the subject sprawls out in so many different directions there are more symmetries in electromagnetism than
   > what I've told you about they're more soft theorems they're more symmetries and I'm going to tell you about
   > them later but I can only do one thing at a time"
   `[swrNwD0ypaE @ 00:09:45]` — tags: open-problems, methodology

4. **"Asymptotic symmetries is more of an art than a science" — and, spoken only, "the rules keep changing".** The
   written notes keep the art/science line, including the joke that art may be better than science; they do not keep
   the admission that the rules of the method are unstable.
   > "I like to say that this subject is more of an art than a science but it's been in the rules keep changing um
   > however despite the fact that [...] this way of thinking about things is not very rigorous it's been
   > extraordinarily fruitful"
   `[swrNwD0ypaE @ 00:10:50]` — tags: asymptotic-symmetries, methodology, pitfalls

5. **Both halves of the definition ASG = allowed / trivial are, in his word, "squishy" — and the natural fix does
   not always work.** Constructing charges to decide triviality is often impractical, and even when you can, a
   vanishing charge does not reliably mean the transformation is trivial.
   > "both of those the top and the bottom are a little bit squishy because how do you decide what you're going to
   > allow what kind of behavior you're going to allow at Infinity [...] one way to do that but it's not always done
   > this way is to construct some kind of charges but in practice that's often extremely difficult to do and then
   > if the charges vanish you might say they're trivial but that also turns out not to always be exactly right"
   `[swrNwD0ypaE @ 00:13:01]` — tags: asymptotic-symmetries, pitfalls, charges

6. **How Brown and Henneaux calibrated their boundary conditions: they already knew three-dimensional black holes
   existed and made the conditions just weak enough to admit them.** The method needs a known physical target to be
   aimed at; the written notes report the Virasoro result without this detail about how the input was fixed.
   > "they wanted to put the boundary conditions so that it was already known that there were black holes in
   > three-dimensional anti-de[ ]sitter space they wanted to have weak enough boundary conditions so that you could
   > allow all the black hole Solutions and so they made them just weak enough to allow that and then they
   > constructed some charges"
   `[swrNwD0ypaE @ 00:17:11]` — tags: asymptotic-symmetries, history, methodology

7. **Asked why he does not allow a `u`-dependent gauge parameter, he gives the reason the written notes withhold:
   you can, but after a long analysis the charge turns out to depend only on the value at the past boundary of
   future null infinity, and the difference between two such parameters generates a charge that vanishes
   identically.** The notes say only that nothing new comes of it and redirect to the subleading-soft literature.
   > "the answer is I could have but then after a long analysis I would have eventually found what we found earlier
   > that the charge in the end depends only on the value of Epsilon down here"; and "if you have two epsilons which
   > take the same value at scribe plus minus but differ elsewhere [...] the associated charges would be equal [...]
   > the difference between the two things would be trivial the charge would always vanish"
   `[swrNwD0ypaE @ 00:28:52]` and `[swrNwD0ypaE @ 00:30:53]` — tags: large-gauge, charges, methodology

8. **BMS never managed to construct the charges, and for a long time there were rival candidate groups with no way
   to decide between them.** He names the Newman–Unti group as a contender and says the resolution required more
   work than the quick-and-dirty method could supply.
   > "BMS did null Infinity but they were never able to construct they were not able to construct the charges [...]
   > there were variations on BMS the simplest idea they got it right but we now know they got it right but there
   > were contenders along the way of other groups the new manuity [Newman–Unti] group and so on and you couldn't
   > tell which the real group was without doing more work"
   `[swrNwD0ypaE @ 00:31:57]` — tags: history, asymptotic-symmetries, charges

9. **The strongest open-problem statement of the lecture: nobody knows how to do loop corrections in a formalism
   whose basic variables are fields on null infinity.** This is his stated reason for abandoning the scri language
   at exactly this point and translating everything into plane waves, where a century of quantum electrodynamics can
   be reused.
   > "one could try to see if these equations have Loop corrections but that would entail understanding in this
   > language how to do Loop Corrections where your basic variables are fields on [scri] nobody's really ever worked
   > that out so instead what we're going to do is we're going to rewrite these things in terms of [...] plane wave
   > Fields [...] and then we can use the Hundred Years of development of quantum electrodynamics"
   `[swrNwD0ypaE @ 00:37:21]` — tags: open-problems, methodology, ward-identities, ir-divergences

10. **An unusually candid exchange about attribution of the soft theorem.** Low 1958 is the usual citation, but
    Bloch and Nordsieck predate quantum electrodynamics, Low apparently used dispersion methods rather than Feynman
    diagrams, the modern diagrammatic form is Weinberg's, and Weinberg may have been the first to treat a single
    soft photon rather than an in–out pair. He also deflects the question of credit as ill-posed.
    > "I would say they don't care about references [...] I mean it evolves right I mean in some [sense] you could
    > also credit it to Maxwell I don't know [...] block [and] Nordic [Bloch and Nordsieck] was before QED [...]
    > interestingly enough I don't think Lowe [Low] really used [Feynman] diagrams he used some kind of dispersion
    > [...] the modern way that we think of it in terms of [Feynman] diagrams is due to Weinberg [...] those other
    > people [...] had something which was equivalent but it involved both incoming and outgoing photons and I think
    > Weinberg was the first one to talk about just one photon"
    `[swrNwD0ypaE @ 00:58:31]` — tags: history, soft-theorems

11. **Choosing the gauge parameter `ε = 1/(z−w)` costs no generality.** He says explicitly that if the identity
    holds for that family for every `w`, a few lines give it for arbitrary `ε`. The notes make the substitution
    without commenting that it is without loss of generality.
    > "this formula is true for any Epsilon but it's not very hard to show that if it's true for that special form
    > of Epsilon for any W [...] then it's just a few lines to show that it's true for any Epsilon so effectively
    > taking Epsilon equals one over Z minus w is equivalent to taking an arbitrary function"
    `[swrNwD0ypaE @ 01:12:36]` — tags: ward-identities, methodology

12. **Asked to do the algebra, he declines and explains what he checks instead: that the coupling constants cancel
    and that the pole structure matches on both sides.** A compact statement of what he counts as adequate evidence
    for an identity short of a full derivation — relevant to anyone deciding how much of a verification to demand.
    > "it's just tedious algebra I could make you do it on a homework set if you [wish] but I think what I tried to
    > sketch [is] the plausibility of this working right because we saw that the e[']s canceled we saw that the
    > pol[e]s were in the right place you can see the general feature[s] work out without checking all the details"
    `[swrNwD0ypaE @ 01:13:51]` — tags: methodology, soft-theorems

13. **He abandons factor-precision for the Feynman diagram section, and says why.** This is the explicit opposite of
    his lecture 1 policy, and the boundary between the two regimes is worth knowing when using his formulas.
    > "it's a couple lectures to just to spell out your conventions for Feynman diagrams I don't want to do that so
    > I am just gonna write down formulas that are true in a standard set the twos and the pies and so on are
    > correct in some standard set of conventions"
    `[swrNwD0ypaE @ 01:15:56]` — tags: methodology, pitfalls

14. **What makes the diagrammatic derivation powerful is that the interior is a black box: the argument works for
    any theory containing a photon.** Only the external-leg propagator and the vertex matter; nothing needs to be
    said about the interactions in the middle.
    > "this of course is equal to the sum of an infinite number of terms whose detailed form depends on what I
    > haven't even said now what theory I'm talking about except that we have a photon that's one of the beaut[ies]
    > of this thing it applies to every theory that has a photon in it"
    `[swrNwD0ypaE @ 01:20:11]` — tags: soft-theorems, methodology

15. **The two derivations of the soft theorem have opposite difficulty profiles with respect to mass.** In the
    diagrammatic proof the mass hardly enters at all — the original authors were mostly interested in the massive
    case — whereas in the asymptotic-symmetry derivation massive and massless are qualitatively different problems,
    because massive particles never reach null infinity.
    > "when you prove [it] [...] in this asymptotic description it's qualitatively different for massive and
    > massless particles but in the standard proofs of the soft theorem they were actually mostly interested in the
    > massive particle case and it hardly matters at all I mean it doesn't even really the mass doesn't even really
    > appear"
    `[swrNwD0ypaE @ 01:24:33]` — tags: soft-theorems, methodology, charges

16. **Gauge invariance of the soft factor is equivalent to global charge conservation, and he attributes something
    close to this argument to Low in 1958.** The soft factor is only defined up to shifts of the polarization by the
    photon momentum; demanding invariance under those shifts collapses the expression to the total charge.
    > "charge conservation Global charge conservation guarantees that this soft factor is gauge invariant and that
    > can be used to or that was used I think really that was part of how low argued for this Francis low argued for
    > this formula in 1958"
    `[swrNwD0ypaE @ 01:33:11]` — tags: soft-theorems, charges, history, ward-identities

17. **He suspects Weinberg never did the general-spin case, and offers a uniqueness argument instead of a
    calculation: the soft factor is the only expression with the right dimensions that is invariant under those
    polarization shifts.** A symmetry-plus-dimensions argument standing in for a case-by-case derivation.
    > "I've only worked it out here for the case of a scalar if you do a fermion or some other kind of charged
    > particle it's a little more complicated but it works out to be the same thing [...] I don't think Weinberg did
    > it in his original paper but [...] one way of seeing it is from the fact that this is the only formula that is
    > invariant with the right dimensions and so on that is invariant under these shifts of Q"
    `[swrNwD0ypaE @ 01:35:18]` — tags: soft-theorems, methodology

18. **Closing question from the floor, left open: the graviton version looks like the Ward identity of a stress
    tensor in a two-dimensional conformal theory on the celestial sphere, but he says those statements are much less
    investigated than the `U(1)` current-algebra case.**
    > "this also looks like [a] ward identity in a [...] C[FT] and the one that is related to Super rotations and is
    > this stress tensor the ward identity for the stress energy tensor in a [...] CFT but those statements haven't
    > been [as] fully investigated as the one for the [...] U1 [current]"
    `[swrNwD0ypaE @ 01:45:55]` — tags: celestial, open-problems, soft-theorems

19. **A live wobble on the falloff conditions, resolved from the floor.** He derives the `1/r²` behaviour of the
    long-range electric field from finite energy flux, gets stuck on the corresponding statement for the magnetic
    component, and a student supplies the missing constraint — that a `1/r` long-range field would give infinite
    charge as well as infinite energy. Worth recording because the falloffs are the input to everything downstream
    and their justification here is partly improvised.
    > "similarly frz should also go like 1 over r squared um I guess that's the magnetic yeah that's the wait yeah
    > that's the okay I don't remember what why that's the right Behavior"; then, after the exchange, "if we have a
    > long range electric field which is going like one over R the energy will be infinite [...] and the charge will
    > be infinite yeah yeah just by G[auss's law]"
    `[swrNwD0ypaE @ 00:22:34]` — tags: pitfalls, asymptotic-symmetries, methodology

---

## Structure of the argument (thin skeleton)

- `00:01:19–00:09:45` — Gravity preview: Bondi mass aspect, antipodal matching, supertranslations; the
  observability contrast with electromagnetism. (Written notes §5.2.)
- `00:10:50–00:19:22` — The asymptotic-symmetry-group method: definition, its two soft spots, ADM and
  Brown–Henneaux as the two historical exemplars. (§2.10.)
- `00:20:26–00:27:51` — Falloffs at scri from finiteness of the energy flux; the allowed gauge transformations are
  functions of the sphere only. (§2.10.)
- `00:27:51–00:32:57` — Question period: why not `u`-dependent parameters; what BMS could and could not do.
- `00:33:01–00:41:44` — Recap of the previous lecture's definitions and the Ward identity; the loop-correction
  admission and the decision to change language. (§2.6–2.8.)
- `00:42:49–00:56:24` — Mode expansion; the special parameter `1/(z−w)`; the current-algebra teaser. (§2.8.)
- `00:58:31–01:11:30` — Weinberg's soft photon theorem in standard form; matching the pole structure; the
  equivalence. (§2.8.)
- `01:15:56–01:35:18` — Feynman diagram derivation for the photon; the gauge-invariance-implies-charge-conservation
  observation. (§2.9.)
- `01:35:18–01:46:56` — Same derivation for the graviton; momentum conservation as the analogous consistency
  condition; closing question about a celestial stress tensor. (§2.9.)

---

## Deltas vs the written lectures (arXiv:1703.05448)

**Present in the video, absent from the written notes:**

- The electromagnetic-versus-gravitational observability contrast, stated as a contrast (insight 2). The notes
  mention Aharonov–Bohm interference for the electromagnetic memory effect in §2.10 and the gravitational memory in
  §6, but never set the two side by side as "phases need interference, time shifts do not".
- "The rules keep changing" (insight 4) — the notes keep the rest of the art/science passage almost verbatim but not
  this clause.
- The warning that a vanishing charge does not reliably mean a trivial transformation (insight 5). The notes say the
  criteria are subtle; they do not say the standard test can fail.
- How Brown and Henneaux fixed their boundary conditions by requiring the known black holes to be admitted
  (insight 6).
- The actual answer to "why not `u`-dependent ε": the difference of two such parameters carries identically
  vanishing charge (insight 7). The notes say only that nothing new results, and point instead at the subleading
  soft theorem literature.
- BMS's failure to construct charges, and Newman–Unti as a live rival group that could not be excluded without more
  work (insight 8). Newman–Unti appears in the notes only in §5.2, as an alternative gauge convention, not as a
  historical contender.
- The statement that nobody has worked out how to do loop corrections with fields on null infinity as the basic
  variables (insight 9). This does not appear anywhere in the notes and is arguably the most consequential delta of
  the four lectures: it is the stated reason the whole argument is routed through plane waves.
- The entire attribution discussion — Bloch–Nordsieck predating QED, Low's use of dispersion rather than diagrams,
  Weinberg's single-photon formulation, "you could also credit it to Maxwell" (insight 10). The notes give a clean
  citation list with dates and no commentary.
- The remark that `ε = 1/(z−w)` is without loss of generality (insight 11).
- The account of what he checks in place of the algebra — cancellation of couplings, agreement of pole structure
  (insight 12). The notes state that the pole structures agree and relegate the algebra to an exercise; the
  methodological point about sufficiency of such checks is spoken only.
- The explicit abandonment of factor-precision for the diagrammatic section (insight 13).
- The "one of the beauties of this thing" universality remark about the black box (insight 14).
- The opposite-difficulty-profile observation about mass in the two derivations (insight 15).
- The attribution of the gauge-invariance argument to Low's 1958 reasoning (insight 16), and the uniqueness argument
  standing in for the general-spin calculation (insight 17).
- The closing exchange about a celestial stress tensor being much less investigated than the current algebra
  (insight 18).
- The improvised falloff derivation and the student's correction (insight 19).

**Checked and *not* a delta:**

- "More of an art than a science [...] maybe art is better than science" — in §2.10 nearly word for word.
- That one cannot choose boundary conditions freely at a null boundary the way one can at a timelike one — §2.10.
- That the `ω→0` limit of `ω·a` is not identically zero because the S-matrix elements have compensating poles —
  §2.8 makes exactly this point, including the "one might think it is just identically zero" framing.
- The symmetric `e^{iωu} + e^{-iωu}` prescription and its hermiticity justification — §2.8.
- That it is easier to go from the plane-wave form to the sphere form than the reverse — §2.8 ("it is easier and
  equivalent to proceed in reverse").
- The current-algebra teaser and the Kac–Moody identification — §2.8 and §4.
- ADM recovering the Poincaré group and BMS finding an infinite-dimensional group instead — §2.10.

**Transcript quality.** The worst stretch is the falloff argument around `00:22:34–00:24:41`, where the audio,
the blackboard and his own hesitation combine and the reasoning is genuinely hard to reconstruct from text alone;
the substance is recoverable but a viewer should watch that segment rather than read it. The attribution exchange at
`00:58:31` is partly cross-talk and some student words are lost. Normalisations: "Lowe" = Low; "block in Nordic" /
"block of Nordic" = Bloch and Nordsieck; "fundament diagrams" / "findman" / "Fineman" = Feynman; "varosaur group" =
Virasoro group; "new manuity group" = Newman–Unti group; "arnowit desert and misner" = Arnowitt, Deser and Misner;
"brown and Hano" = Brown and Henneaux; "cat's Moody" = Kac–Moody; "Carl CFT" is ambiguous — from context either
celestial or Carrollian CFT; "bjorkan and Drell" = Bjorken and Drell; "pelicity" / "velocity" (in "positive velocity
polarization") = helicity; "sulf"/"saw"/"cell" photon = soft photon.
