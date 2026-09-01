# Digest — The Black Hole Information Paradox, Revisited

- **Title:** The Black Hole Information Paradox, Revisited
- **Speaker:** Andrew Strominger
- **Venue/date:** Simons Center for Geometry and Physics seminar, given **2016-04-05** (per the source file's
  header; the recording was uploaded in 2021). Consistent with the talk's own dating — "a picture which has
  emerged over the last three years", and the recent work with Hawking and Perry (arXiv:1601.00921, January
  2016). A questioner is addressed as "Steve" (plausibly Steve Shenker — unconfirmed).
- **Video id:** `F42XbX45Dzw` — https://youtu.be/F42XbX45Dzw
- **Duration:** 01:11:26 (talk to ~00:58:42, then thirteen minutes of questions)
- **Source file:** `refs/strominger-videos/extra-05-F42XbX45Dzw.md` (auto-captions; secondary source, not L3 ground truth)
- **Written companion:** arXiv:1601.00921 (Hawking–Perry–Strominger); arXiv:1703.05448

**Arc.** A colloquium-paced version of the story for a mixed audience: the triangle in ten minutes, then the
electromagnetic case worked slowly from the Liénard–Wiechert field to antipodal matching to the infinite
family of charges to vacuum degeneracy, then a lightning review of the information paradox, and finally the
horizon soft-hair construction with Hawking and Perry. Because the pace is unhurried and the audience is
general, this is the recording where Strominger says the most about *why* the paradox matters and what he
thinks the alternatives are: an extended riff on determinism, a count of how many people he thinks have
actually accepted Hawking's conclusion, and the memorable framing of the degenerate vacuum as a storage
medium. The Q&A is the strongest part: it contains an operational protocol for measuring electromagnetic
memory, a flat statement that angular momentum has no canonical definition in general relativity, a
pointed exchange about why gravity's infrared is different from ordinary entanglement transfer, and a
concession that the Hilbert space may not factorise at all.

---

## Insights

### 1. The degenerate vacuum as a storage medium — "like a big hard drive"
The most quotable framing of vacuum degeneracy in these talks, and note that he immediately downgrades his own
claim from "perfectly possible" to "not ruled out" in the same breath.

> "the vacuum is like a big hard drive and it's perfectly possible that uh well perfectly it's not ruled out
> that ... the final state of ... the vacuum could be correlated with the hawking radiation in such a way that
> quantum purity of everything is ... maintained"

`[F42XbX45Dzw @ 00:44:58]` — tags: vacuum-degeneracy, black-holes, soft-hair, methodology

### 2. Why general relativity does not reduce to special relativity
The clearest statement of what he thinks the whole subject is really about, given in answer to a question. The
expectation that GR should reduce to SR at long distance and weak field fails because there is an infinite
amount of zero-energy structure at long distances; special relativity has no infinite vacuum degeneracy to
match it.

> "everybody thought that ... general relativity should reduce to special relativity in ... some kind of long
> distance limit where gravity is weak[.] in fact what i've just argued is there's an infinite amount of stuff
> at long distances [at] zero energy and that is why general relativity doesn't reduce [to] special
> relativity[.] special relativity doesn't have this ... infinite vacuum degeneracy in it"

`[F42XbX45Dzw @ 01:05:22]` — tags: vacuum-degeneracy, asymptotic-symmetries, methodology

### 3. An operational protocol for electromagnetic memory
Directly relevant to any attempt to say what a memory measurement *is*. The observable is a relative phase,
so it requires a quantum measurement: prepare two charges with aligned phases, separate them, let the large
gauge transformation act, bring them back and interfere. He also credits a short unpublished-style note by
Susskind using an array of SQUIDs connected by resistors as his favourite version.

> "there have been several papers on this[.] my favorite is actually a short note by lenny suskind who had an
> array of squids and connected them with resistors and showed how you could ... measure these phases[,] or
> you could just think about taking ... two electrons with their phases aligned[,] pulling them apart[,]
> waiting for the ... large gauge transformation to occur[,] and then put them back together and see if their
> ... phases are aligned or not"

`[F42XbX45Dzw @ 01:01:02]` — tags: memory, large-gauge, experiment, dressing

### 4. …but when pressed, he locates the physics in the phase space, not in the detector
The follow-up matters as much as the protocol. Asked further about the apparatus, he brushes the apparatus
aside: the content of the claim is that a flat connection on the sphere at infinity is part of the phase
space, and two configurations differing by one are physically distinct whether or not anyone measures it.
Worth setting against the guest lecturer's insistence in Lecture 9 (`09-8Aml1ToQtt4-digest.md`, insight 1)
that memory is meaningless without a prior calibration: these are two genuinely different places to put the
physical content.

> "no you don't care about experimental device[.] what ... i'm saying is that the phase space of ... maxwell
> theory involves ... a point on the sphere[,] you have to specify a gauge transformation[,] those should not
> be regarded as physically [equivalent] ... the flat connections on the sphere at infinity are physical[,]
> you have to specify a flat connection[,] and that is a physical thing which has meaning"

`[F42XbX45Dzw @ 01:02:06]` — tags: memory, large-gauge, methodology, vacuum-degeneracy

### 5. "How do you detect a zero energy object" — the question that bothered him
The same admission as in the 2015 seminar (`extra-01-CdFyoaNv8GI`, insight 1), here stated even more
directly as a personal difficulty resolved by the memory effect. The resolution is that we measure in position
space, where the pole is a step function.

> "so this bothered me a lot before i understood the ... memory effect[:] how do you detect a zero energy
> object[?] and ... the important thing is that these soft photons[,] the amplitude has a pole in it[,] and
> the fourier transform ... of a pole is a step function[,] so when we do observations we don't really do them
> in momentum space[,] we do them in ... position space"

`[F42XbX45Dzw @ 00:59:58]` — tags: memory, soft-theorems, methodology

### 6. Angular momentum has no canonical definition in general relativity
Stated flatly, and identified as the very rock BMS ran aground on. The infinite-dimensional group has no
preferred finite-dimensional subgroup you can point at and call angular momentum.

> "angular momentum turns out to be a very subtle concept in ... general relativity ... indeed this was
> exactly where ... bms ran into trouble[.] they were trying to define what angular momentum means in ...
> general relativity because it has a very good meaning in special relativity[.] in fact there is no canonical
> definition of the [angular] momentum in general relativity ... you can only talk about that whole group[,]
> you can't point to a special subgroup of it"

`[F42XbX45Dzw @ 01:04:19]` — tags: charges, superrotations, pitfalls, history

### 7. BMS as a failed reduction
A framing of the 1962 work that makes its surprise legible: Bondi, van der Burg, Metzner and Sachs set out to
*recover* the Poincaré group in a limit and did not.

> "bondi [Metzner] and sax[s] wanted to show that somehow in general relativity you could recover it in an
> appropriate limit and they spectacularly failed[.] they found instead a much bigger infinite dimensional
> group and this is ... something which relativists have been wrestling with for the last half a century"

`[F42XbX45Dzw @ 00:05:59]` — tags: history, asymptotic-symmetries

### 8. The determinism riff — what is actually at stake
The longest piece of non-technical reasoning in the recording, and the reason he thinks the paradox is not a
matter of taste. If Hawking is right, the claim is not that some prediction fails but that there are no laws;
and one is not entitled to stop there — an alternative framework would have to be produced.

> "if this is correct[,] and this is what ... hawking argued in 1974[,] the world is not deterministic[.] now
> that's a pretty serious thing to say[.] it's saying that we can't describe the universe by laws ... we
> thought our job was to discover what the laws of nature are but it's saying that there aren't laws"

`[F42XbX45Dzw @ 00:40:46]` — tags: black-holes, methodology, open-problems

### 9. …with the alternative left genuinely open
He does not simply dismiss indeterminism. He says it should stay on the table, offers the beginning of the
universe as a reason it might be true, and rests the case on the fact that nobody has built a replacement.

> "alternatives to deterministic ... everything should always be on the table and maybe the universe isn't
> deterministic[.] if there was nothing before the big bang indeed it's hard to see how it could be ... so
> maybe determinism is not exact[,] like other things we believed to be true and then turned out to be
> corrected[.] but ... nobody has come up with an alternative"

`[F42XbX45Dzw @ 00:41:48]` — tags: methodology, open-problems, black-holes

### 10. A head count of the field, and Hawking's own change of mind
A sociological observation offered as evidence about where the community landed, with the number stated as his
own impression.

> "of the hundreds or thousands of people that have thought about ... this paradox ... i believe there are now
> only two ... who have admitted to believing that what happens is that the universe isn't deterministic[,]
> and hawking himself long ago ... said i don't know how this works but ... it doesn't seem like throwing out
> determinism is ... a good thing to do"

`[F42XbX45Dzw @ 00:42:50]` — tags: history, black-holes, methodology

### 11. The no-hair theorem is correct; its physical interpretation was not
His standing position on the theorem, stated as a distinction between a mathematical result and the reading
imposed on it — the diffeomorphisms it quotients by include ones that change the physical state.

> "there is something called the no hair theorem and the no hair theorem is a correct mathematical theorem but
> i'm arguing it was misinterpreted[.] the ... physical interpretation of it was ... incorrect"

`[F42XbX45Dzw @ 00:36:29]` — tags: black-holes, soft-hair, pitfalls, history

### 12. Why a black hole cannot be indifferent to these charges — the plain-language argument
Not a computation: a Gauss's-law observation. Whatever surface you use, some of the charge sits outside the
horizon and charge density crosses it, so there is no consistent picture in which the black hole ignores the
charges.

> "if we had a black hole in our space-time and we used gauss's law to fill in the ... surface ... there will
> be portions of the charge outside the black hole and portions of the charge density can move in and out of
> the black hole[,] and there is no way for the black hole to be sort of impervious to such charges"

`[F42XbX45Dzw @ 00:47:03]` — tags: black-holes, charges, soft-hair

### 13. Four constraints versus infinitely many — the counting argument in plain words
The cleanest statement of why the energy-momentum correlations everyone already accepts do not help, and why
the infinite family might.

> "these four constraints we have always presumed we must put in as constraints by hand ... now four
> constraints isn't enough to help with the information problem because ... it could be a lot of information
> [in] a phd thesis and just four bits of information won't take care of it[,] but now all of a sudden we've
> got an infinite number of constraints"

`[F42XbX45Dzw @ 00:49:12]` — tags: black-holes, charges, soft-hair, methodology

### 14. Why the gravitational case was found first — his second explanation
In the 2015 seminar the answer is a joke about relativists. Here he gives a physical reason: in an abelian
gauge theory the symmetry acts by phases, so detecting the effect needs a quantum interference measurement,
whereas the gravitational effect is a displacement you can watch.

> "this is an odd difference between the electromagnetic and the gravity case and perhaps why the gravity case
> was discovered before the electromagnetic case is that in a[belian] gauge theories the ... symmetries are
> just phases ... and we know that we need to do some kind of quantum experiment to detect relative phases"

`[F42XbX45Dzw @ 01:01:02]` — tags: history, memory, large-gauge, experiment

### 15. …and he calls the ordering bizarre
Said of the memory/soft-theorem Fourier relation: gravity got there ahead of Maxwell theory, which is not how
these things normally go.

> "this is a bizarre instance in which gravity was ... ahead of ... the maxwell theory"

`[F42XbX45Dzw @ 00:35:28]` — tags: history, memory

### 16. The quantum-computer exchange: why is gravity's infrared special?
A sharp challenge from the floor. Entanglement build-up and transfer is familiar from ordinary quantum systems
where nobody expects a large modification; what makes the black hole different? Strominger's first answer is
one line, the questioner immediately refuses it, and the exchange is worth reading in full because Strominger
ends up conceding that the difference is not that the conservation laws fail elsewhere — it is that elsewhere
there is nothing to solve.

> "well quantum computers don't involve gravity usually" — "yeah well yes they do because they live in the
> real world ... gravity can be ignored[,] that's a tiny effect[,] so why is it a big effect here for [a]
> black hole"
> … "i'm sure those situations are all subject to these conservation laws and obey them ... there's no
> information puzzle with a quantum computer[,] well there's nothing we need to solve there"

`[F42XbX45Dzw @ 01:07:26]`, `[F42XbX45Dzw @ 01:08:28]` — tags: black-holes, methodology, pitfalls, open-problems

### 17. …and the concession underneath it: the Hilbert space may not factorise
The most consequential admission in the Q&A, and one he volunteers rather than defends against. He can write
infinitely many correlations between inside and outside "to the extent that we can separate them" — and then
says that separation is itself a big issue.

> "it's not obvious that you can factorize the hilbert space[.] so ... if you're asking me[,] steve[,] how do
> i ... get from here to a complete solution of the information paradox[,] the answer is i don't know"

`[F42XbX45Dzw @ 01:07:26]` — tags: open-problems, black-holes, methodology, pitfalls

### 18. Closing status: soft hair is unlikely to be the whole story
A clear self-assessment at the end of the talk, given before any question forced it.

> "i think it's unlikely that ... they store all of the information[,] that this is ... the end of the
> story[.] there are many more things that we need to take into account[,] other kinds of symmetries ... the
> structure of infinity and so on ... but we're very far from that"

`[F42XbX45Dzw @ 00:58:42]` — tags: soft-hair, black-holes, open-problems, methodology

### 19. Hedging the Goldstone language, on semantic grounds
Asked whether a soft photon really is a Goldstone boson, he calls the question semantic, explains that
strictly only the zero mode transforms, notes that the usual terminology promotes the whole field anyway, and
says he does not know whether that terminology is good. Worth pairing with the guest lecturer's much stronger
dissent in Lecture 9.

> "that's really a question of semantics ... the terminology is that when the zero mode of a field transforms
> under the symmetry — i don't know if it's a good terminology or not but ... [it's] what people use — ... we
> call the whole field the goldstone boson of the spontaneous symmetry breaking[.] in the same sense i could
> have said the photon itself is the goldstone boson of spontaneous large gauge symmetry even though it's only
> the zero mode part of it that enters"

`[F42XbX45Dzw @ 01:10:31]` — tags: vacuum-degeneracy, methodology, pitfalls

### 20. Another admission that the key fact was hiding in a century-old formula
Same admission as in the Strings 2016 talk, phrased slightly differently, and followed by an explicit
statement that he is going to belabour it because everything rests on it.

> "the peculiar thing[,] which i suppose maxwell must have known but i didn't realize until the last few
> years[,] is that ... the radial component of the electric field is actually not well defined at spatial
> infinity[,] and this ... fact is going to be crucial to everything that i'm going to say[,] so i'm going to
> ... belabor it a little bit"

`[F42XbX45Dzw @ 00:11:16]` — tags: history, charges, methodology

### 21. "Asymptotic" is a misleading word — again
The same terminology complaint as in the Strings 2016 talk, made in almost identical words. Its recurrence is
itself the datum: he expects this confusion in every audience.

> "when you say asymptotic symmetries you might think i'm talking about symmetries which are only exact
> symmetries in some limit but in fact asymptotic symmetries are exact symmetries just like all the symmetries
> we usually talk about"

`[F42XbX45Dzw @ 00:04:54]` — tags: asymptotic-symmetries, pitfalls, methodology

---

## Structure of the argument (thin skeleton)

- `00:02:48` The three-way equivalence, introduced as something that "has emerged over the last three years".
- `00:10:13` The static and boosted point charge; the field is not single valued at spatial infinity; antipodal
  matching.
- `00:15:30` Infinitely many conservation laws; constant $\epsilon$ gives charge conservation, general
  $\epsilon$ adds a soft photon term.
- `00:20:53` Quantum version: the charge commutes with the S-matrix; equivalence to Weinberg 1965.
- `00:24:59` The symmetry: large gauge transformations acting non-trivially; the boosted black hole as the
  motivating example of a physical diffeomorphism.
- `00:28:08` Vacuum degeneracy, soft hair, Goldstone bosons; the same story in gravity and its relation to
  memory.
- `00:36:29` Lightning review of the information paradox; the no-hair reinterpretation; determinism.
- `00:51:17` Work with Hawking and Perry: the conservation law with the surface deformed around the horizon;
  soft photons/gravitons on the horizon; the evaporation identity.
- `00:59:58` Q&A: detecting zero-energy quanta, SQUIDs and electron interference, angular momentum in GR,
  quantum computers and factorisation, Goldstone semantics.

---

## Deltas vs the written sources (arXiv:1601.00921, arXiv:1703.05448)

- **The determinism argument (insights 8–10) is spoken only.** `determinis*` occurs zero times in
  `soft_Arxiv_update.tex`. The written record states the paradox technically; the talk states why he thinks the
  stakes are "there are no laws", keeps indeterminism formally on the table, and reports his own count of how
  many researchers accept it. That last is a historical datum with no paper equivalent.
- **"The vacuum is like a big hard drive" (insight 1)** — the phrase does not occur in the notes, and the
  self-correction from "perfectly possible" to "not ruled out" inside a single sentence is exactly the sort of
  hedging that papers smooth away.
- **The electromagnetic memory protocol (insight 3) and the Susskind SQUID note (also insight 3)** have no
  counterpart in the written lectures — `SQUID` occurs zero times, and Susskind is cited three times for
  unrelated work. This is the most operationally specific thing Strominger says about measuring an
  electromagnetic memory anywhere in this set of recordings.
- **The phase-space-versus-detector move (insight 4) is a framing delta with campaign relevance.** Strominger
  places the physical content in the phase space (a flat connection on the sphere is data you must specify);
  the Lecture 9 guest lecturer places it in a calibrated difference between measurements. Neither position is
  in the written notes in these terms, and the two are in tension.
- **"General relativity does not reduce to special relativity" (insight 2)** is a compact statement of the
  programme's punchline that the notes never make this baldly.
- **Angular momentum's lack of a canonical definition (insight 6)** appears in the notes only obliquely (the
  superrotation section notes that the global conformal Killing vectors give the BORT centre of mass). The flat
  statement that you cannot point to a preferred subgroup is spoken.
- **Q&A concessions:** that the Hilbert space may not factorise (17), that he does not know how to get from
  here to a solution (17), that soft hair is unlikely to be the whole story (18), and the hedge on Goldstone
  terminology (19). The first two are the kind of thing that only survives in a recording.
- **Reverse delta (in the notes, absent here):** the memory effect gets one paragraph and no formula; there is
  no Faddeev–Kulish or infrared-divergence discussion, no superrotations beyond the passing remark on angular
  momentum, no colour memory, and no massive-particle case.

---

## Transcript quality notes

Poor to middling, and worst at the start: the first ninety seconds are the host's introduction and are largely
garbage ("really strength here can serve as a fight theory of also mental forces" for, apparently, string
theory as a theory of fundamental forces; "caviar multiplication" for Kaluza–Klein compactification;
"griffaffa 95" for the Strominger–Vafa 1996 entropy counting; "quantum graphics" for quantum gravity). In the
body: "a billion" for abelian throughout, "short shoulder"/"short shield" for Schwarzschild,
"diphymorphism"/"dipheomorphism" for diffeomorphism, "vacuor"/"vacuola"/"vacuole" for vacua, "gold stone" for
Goldstone, "zeldovacin palmarov" for Zeldovich and Polnarev, "sasha jabot" for Sasha Zhiboedov, "bondi medster
and sax" for Bondi–Metzner–Sachs, "u1 cat smoothie" for U(1) Kac-Moody, "word identity" for Ward identity,
"lenny suskind" for Lenny Susskind (correct enough), "hawking" reliable. Sentence casing and punctuation are
absent throughout, so the bracketing in the quotes above does more work than usual. Audience questions are
transcribed with no speaker changes; the exchange in insight 16 in particular had to be segmented by content,
and one questioner is identified only because Strominger says "steve". Slides are not recoverable.
