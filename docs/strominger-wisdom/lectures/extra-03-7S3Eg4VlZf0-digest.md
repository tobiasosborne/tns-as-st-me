# Digest — Asymptotic Symmetries for Gauge and Gravitational Theories in Minkowski Space

- **Title:** Asymptotic Symmetries for Gauge and Gravitational Theories in Minkowski Space
- **Speaker:** Andrew Strominger
- **Venue/date:** **not Perimeter.** The source file's header guesses PIRSA:14030087 (Perimeter, March 2014),
  but the recording opens "thank the organizers. Uh Seoul is really a wonderful city." Internal dating —
  Barnich–Troessaert's superrotation proposal is "about 3 years ago" (their papers are 2009–2011), the
  Yang–Mills asymptotic-symmetry analysis is unpublished work in progress (it appeared as arXiv:1308.0589 in
  August 2013), and the gravitational case is "kind of halfway through" — points to **mid-2013**, most likely
  **Strings 2013, Seoul (June 2013)**. Treat the venue as probable, not established.
- **Video id:** `7S3Eg4VlZf0` — https://youtu.be/7S3Eg4VlZf0
- **Duration:** 00:45:01 (talk ends ~00:33:09; the last twelve minutes are questions)
- **Source file:** `refs/strominger-videos/extra-03-7S3Eg4VlZf0.md` (auto-captions; secondary source, not L3 ground truth)
- **Written companion:** arXiv:1308.0589 (Yang–Mills asymptotic symmetries); later arXiv:1703.05448

**Arc.** This is the earliest recording in the set, and its value is that the story is not yet the story.
Strominger opens on BMS, adopts Barnich–Troessaert's superrotations, and then announces he will spend the
talk on a *toy problem*: what are the asymptotic symmetries of massless electrodynamics at $\mathcal{I}^+$?
The proposed answer is a Kac-Moody group with a level tied to $1/e^2$; the technical apparatus is a
holomorphic current $J_z$ built from the gauge field at the *future* boundary of $\mathcal{I}^+$, treated as a
holographic screen; Weinberg's soft photon theorem comes out as the current-algebra Ward identity. The
antipodal matching condition at spatial infinity — which by 2016 he calls "crucial to everything I'm going to
say" — is entirely absent; indeed he says he will *ignore* $\mathcal{I}^-$. He is candid that this is work in
progress, that he does not know how to make the charges act globally, and (given license by a questioner) that
the celestial sphere looks like it wants to be a string worldsheet. Several statements here were later revised
or replaced; they are flagged below.

---

## Insights

### 1. EARLY PERIOD, LATER REVISED — "we don't have a Hilbert space at Scri plus"
His stated reason for not building the symmetry as an operator algebra on states. Compare the mature
programme, in which the whole construction is precisely a charge $Q_\epsilon^\pm$ acting on in- and out-states
of the S-matrix. This is the clearest example in the set of an early technical judgment that the programme
later got past.

> "It can't act on a Hilbert space in this case because we don't have a Hilbert space at Scri plus. There's
> there's infinitely many Hilbert spaces, one for each different surface that ends up at Scri plus. They're
> not unitarily equivalent."

`[7S3Eg4VlZf0 @ 00:10:35]` — tags: asymptotic-symmetries, methodology, history, pitfalls

### 2. EARLY PERIOD, LATER REVISED — he is deliberately *not* constructing global charges
Asked whether BMS transformations have canonical generators, he says he has taken a different tack: currents
on a patch of the sphere, generating gauge transformations on a portion of $\mathcal{I}^+$, precisely because
he does not think the charges act naturally on slices with $S^2$ boundaries. The mature version of the
programme does exactly the thing he here declines to do.

> "I'm not I'm not trying to construct charges that globally you know, they don't I don't think the charges
> naturally act on um they don't naturally act on R3 slices with S2 boundaries. And especially if you have a
> [Kac-Moody] algebra, it you know, you need to get the central term, you need to have a circle somewhere."

`[7S3Eg4VlZf0 @ 00:43:42]` — tags: charges, asymptotic-symmetries, history, methodology

### 3. EARLY PERIOD — $\mathcal{I}^-$ is set aside, and there is no antipodal matching
He notes an obstruction to his gauge condition when charge flux crosses $\mathcal{I}^-$ and simply excludes
that case. The 2016–2017 talks build everything on the antipodal identification between $\mathcal{I}^+_-$ and
$\mathcal{I}^-_+$; here the past boundary is a nuisance to be avoided.

> "it turns out there's actually an ... obstruction to doing this if there ... is charged flux coming through
> Scri minus. So, for now, I'm just going to I I want to ignore Scri minus."

`[7S3Eg4VlZf0 @ 00:17:01]` — tags: charges, history, methodology

### 4. EARLY PERIOD — the holographic screen sits at the *future* boundary of $\mathcal{I}^+$
The current $J_z$ is defined from the gauge field at the far future of $\mathcal{I}^+$, on the assumption that
everything has decayed to vacuum there, and that sphere is called the holographic screen. In the mature
framing the charges live at $\mathcal{I}^+_-$, the *past* boundary, matched antipodally to $\mathcal{I}^-_+$.
The physics is not contradictory, but the location of the structure — and hence the picture one carries
around — changed.

> "now I want to ... define a current JZZ which lives up here, which in this problem is playing the role[,]
> this two sphere up here is playing the role of the holographic screen."

`[7S3Eg4VlZf0 @ 00:22:22]` — tags: charges, celestial, history, large-gauge

### 5. EARLY PERIOD — the Kac-Moody level conjecture, $k = 2/e^2$
Proposed twice, once in the outline and once with the computation sketched: the current is not gauge
invariant, and the coefficient of the violation is read as a level. He is careful to say the analysis is
compromised by his gauge choice. The written record does not carry this formula; the level that appears there
is determined instead by the cusp anomalous dimension (Nande–Pate–Strominger, cited at
`soft_Arxiv_update.tex` l. 942).

> "so if you're current which is not gauge invariant the coefficient of the violation of gauge invariance can
> be identified with the level of the [Kac-Moody] symmetry. So we can compute that and it works out to be uh
> 2 over e squared ... However, the way I've set up the problem so far is hard to analyze this because it
> turns out that my gauge choice ... is not invariant under the conformal symmetry and there's ...
> consequently some holomorphic subleading terms which I don't understand."

`[7S3Eg4VlZf0 @ 00:26:49]`, `[7S3Eg4VlZf0 @ 00:27:51]` — tags: celestial, large-gauge, open-problems, history

### 6. The methodological credo: an asymptotic symmetry group has to earn its keep
The most transferable statement in the talk, and the one most directly useful to anyone defining such a group
in a new setting. The definition is not canonical; it changes with the application; and the criterion for a
good one is that it relates measurable quantities you did not previously know were related.

> "the notion of an asymptotic symmetry group is of course extremely useful. But what exactly you mean by it
> changes with every new application. And so, part of this problem is to say what exactly we mean by this
> asymptotic symmetry group ... And my point of view is that it should be useful. In other words, it should
> tell us relationships between physical quantities that we can measure that we didn't know about before."

`[7S3Eg4VlZf0 @ 00:10:35]` — tags: asymptotic-symmetries, methodology

### 7. Provenance: the clue came from an unpublished note of Maldacena's
The origin story of the QED corner, stated plainly. Later in the Q&A he repeats the credit — the observation
that the rewritten soft theorem "looks like a U(1) Kac-Moody algebra" is Maldacena's.

> "there's a very important clue which was my second important um motivation for for this work which was
> something that was explained to me by uh Maldacena a couple years ago and he wrote a note on it which he
> didn't publish, but he very kindly shared with me."

`[7S3Eg4VlZf0 @ 00:12:45]` — tags: history, soft-theorems, celestial

### 8. The whole QED corner began as an admitted toy problem
Worth recording because the QED case later becomes the pedagogical entry point to the entire subject. It
started as a simplification chosen because the gravitational question was too hard, and because nobody
appeared to have asked it.

> "in most of this talk, I'm not going to uh talk directly about BMS, but I'm going to talk about a much
> simpler uh toy problem ... this is a question which is the exact analog of the question BMS asked in the
> '60s, but in a much simpler theory, um massless electrodynamics, and it's a question which seems to not
> really have been addressed."

`[7S3Eg4VlZf0 @ 00:08:30]` — tags: history, methodology, large-gauge

### 9. Fifty years of neglect, stated as the puzzle that motivated him
He frames the entire programme as a response to an anomaly in the literature rather than to a technical
opportunity: a group this large ought to have constrained every scattering process in Minkowski space, and
did not.

> "this is 50 years ago and you would have expected that this group would play a central role in the study of
> all scattering processes in Minkowski space, and indeed it should even constrain not only gravity theories
> ... but any theory which can be coupled to gravity ... Yet, uh we've we've heard very little about it."

`[7S3Eg4VlZf0 @ 00:02:13]` — tags: history, asymptotic-symmetries, methodology

### 10. Forty years between the BMS algebra and the BMS charges
A historical judgment with a methodological moral: knowing the symmetry algebra and being able to write
generators for it are very different achievements, and the gap here was four decades.

> "the BMS group itself was discovered in 1962. And and then there's a question of whether you can write down
> charges which generate the BMS algebra. And perhaps you know better than me, but my understanding of that
> is that there were many difficulties ... I think it was finally accomplished by Wald and Zupancic [Zoupas]
> something like 10 years ago. So, it was 40 years between the algebra and the construction of the charges.
> It's ... They're not the same thing. It's very hard to go from one to the other."

`[7S3Eg4VlZf0 @ 00:42:39]` — tags: history, charges, asymptotic-symmetries, methodology

### 11. …and Barnich–Troessaert's attempt at the extended charges hit divergences he could not repair
Immediately after, and stated without polemic: he does not know whether that programme can be completed. This
is the state of the superrotation charge question in 2013.

> "Barnich and Troos[saert] tried to do the same thing for the extended BMS group ... But um I've taken a
> different tact here ... And they ran they ran into some problems. There were some divergences and I don't
> know if that program can be completed or not"

`[7S3Eg4VlZf0 @ 00:42:39]` — tags: superrotations, charges, open-problems, history

### 12. "Maybe what we're learning here is that quantum gravity is string theory"
The speculative high point, drawn out of him by a question (from a questioner he calls "Karan" — the captions
are unreliable and the content suggests Cumrun Vafa) about Gross–Mende scattering and worldsheet current
algebra. He first says the transparency on this was cut for being too speculative, then makes the leap and
immediately checks himself against the level formula, which differs from the string relation by $g_s^2$.

> "there's a sense in which this conformal sphere looks like it wants to be the string world sheet ... so,
> maybe what we're learning here is that quantum gravity is string theory. You know, it always has to be ...
> But then, there's the formula for the level."

`[7S3Eg4VlZf0 @ 00:38:26]` — tags: celestial, open-problems, methodology

### 13. …and an aside about what gets cut from a talk
A small window into how he calibrates a public claim. He had prepared the string-worldsheet slide and removed
it, and says so.

> "that's a great question ... and I had a transparency on this, but it was just too speculative, so I I I I
> took it out, but now you've given me the license to to to say something about it."

`[7S3Eg4VlZf0 @ 00:37:21]` — tags: methodology, history

### 14. A named route to testing the level formula against string theory
He identifies the closest known analogue — Giveon–Kutasov–Seiberg lifting a worldsheet SU(2) current algebra
to a spacetime one in AdS$_3\times S^3$, with a $g_s^2$ in the relation — and states the hope as a concrete
open problem.

> "the closest analog of this is an old paper by Giveon, Kutasov, and Seiberg ... And that formula[,] the
> relationship between the ... spacetime current algebra and the world sheet current algebra[,] has exactly
> a factor of G string squared in it. So, so the hope would be that there would be some stringy derivation of
> this"

`[7S3Eg4VlZf0 @ 00:40:32]` — tags: celestial, open-problems, history

### 15. "Boundary photons" — a name that did not survive
His term at the time for the pure-gauge configurations generated by large gauge transformations, proposed by
analogy with boundary gravitons in AdS$_3$. Later this role is played by the Goldstone mode of the broken
large gauge symmetry.

> "I'm going to call these large gauge transformations and the gauge fields that were created, I'm going to
> call it boundary photons ... I want to propose that we can ... regard them as the analog of the boundary
> gravitons in ADS3. They're pure gauge, but they have interesting consequences and they live on the boundary
> of Minkowski space."

`[7S3Eg4VlZf0 @ 00:18:05]`, `[7S3Eg4VlZf0 @ 00:19:10]` — tags: large-gauge, history, celestial

### 16. An open invitation, not a result
He says outright that the talk is unfinished work and asks for help. Registered here because it marks the tone
of the programme at its start — three years before the same material is presented as an exact equivalence.

> "Now, this is a work in progress. Uh my understanding of many points is is is is incomplete and I'm
> presenting this in part I'm I'm I'm hoping someone in in the audience will have some some something
> interesting to add ... and I welcome your input."

`[7S3Eg4VlZf0 @ 00:11:38]` — tags: methodology, open-problems, history

### 17. Electromagnetic duality: an answer, and a reason not to push it
Asked about duality, he gives the formal answer (magnetic charges complexify $q_k \to q_k + i b_k$) and then
declines to make more of it, on the physical ground that theories with both massless electric and massless
magnetic states reaching $\mathcal{I}^+$ do not really exist.

> "my understanding is that there aren't really theories which have both massless electric and mass[less]
> magnetic uh particles which can reach uh scri[be] plus. And so it's a little awkward to talk about uh
> duality in this ... context."

`[7S3Eg4VlZf0 @ 00:36:20]` — tags: large-gauge, open-problems, charges

### 18. Why the gauge-theory question was never asked, in one line
The asymmetry of the two literatures, put as a joke about index counts and notation.

> "nobody ever paid attention to the asymptotic analysis at Scri plus for QED or Yang-Mills theory, but for
> gravity there are thousands of papers on it. Um but all in a different notation, of course."

`[7S3Eg4VlZf0 @ 00:28:53]` — tags: history, methodology

### 19. The van der Burg joke
His opening. A joke, and also a small act of restitution toward a name that fell out of the acronym.

> "I think there's an important lesson here that transcends all fields of physics. And that is you should
> never have a last name without a clear initial. Otherwise, you will go 50 years and you will be completely
> forgotten"

`[7S3Eg4VlZf0 @ 00:00:09]` — tags: history

---

## Structure of the argument (thin skeleton)

- `00:00:09` BMS as diffeomorphisms preserving asymptotic structure modulo trivial ones; only $\mathcal{I}^+$
  is considered.
- `00:04:21` Barnich–Troessaert: admit local (meromorphic) conformal Killing vectors; two Virasoros on the
  celestial sphere; the BPZ analogy.
- `00:08:30` The toy problem — massless QED at $\mathcal{I}^+$ — and the Kac-Moody conjecture with a level.
- `00:12:45` Maldacena's clue: Weinberg's theorem rewritten in position space on the sphere is a current-algebra
  Ward identity.
- `00:15:59` Temporal gauge, residual holomorphic gauge symmetry, "boundary photons"; $\mathcal{I}^-$ excluded.
- `00:19:10` Final-data analysis; the current $J_z$ at the future of $\mathcal{I}^+$; $\partial_{\bar z}J_z = \sum_k q_k \delta^2$,
  i.e. $J_z \sim \sum q_k/(z-z_k)$ — the soft theorem.
- `00:26:49` The level: gauge non-invariance of $J_z$, $k = 2/e^2$, and the caveats.
- `00:28:53` Gravity: Bondi expansion, the analogous current from the lapse, supertranslation Ward identity;
  superrotations still to come.
- `00:34:15` Q&A: duality; the string worldsheet; canonical generators for BMS.

---

## Deltas vs the written sources (arXiv:1703.05448 and the later papers)

This is the early-period recording, so the section is mostly a list of things that later changed. Statements
that were subsequently revised are the point of the transcript.

- **No antipodal matching, no spatial infinity, no $\mathcal{I}^-$.** In the 2016–2017 talks the
  non-single-valuedness of the Liénard–Wiechert field at $i^0$ is "crucial to everything I'm going to say"
  and the matching condition is the first slide. Here it does not appear at all, and $\mathcal{I}^-$ is
  explicitly set aside as a complication (insight 3). The conservation laws of the mature programme are
  statements relating $\mathcal{I}^+_-$ to $\mathcal{I}^-_+$; the 2013 construction has no such relation.
- **The structure lives at the wrong end of $\mathcal{I}^+$.** The current is defined at the *future* boundary
  and that sphere is called the holographic screen (insight 4); the mature charges are integrals over the
  *past* boundary. Anyone comparing this talk with the written notes should expect the picture to have flipped.
- **Charges: from "I am deliberately not constructing them" to the centrepiece.** Insights 1, 2 and 11 record a
  2013 position in which global charges are thought unnatural (no Hilbert space at $\mathcal{I}^+$; no circle
  for a central term; Barnich–Troessaert's divergences unresolved), and the chosen alternative is local
  currents on a patch. The written lectures construct $Q^\pm_\epsilon$ and $Q^\pm_Y$ directly and build
  everything on them.
- **The level $k=2/e^2$ (insight 5) is not in the written record.** The lectures instead cite a level determined
  by the cusp anomalous dimension. His own caveats here — a gauge choice that breaks conformal invariance,
  unexplained holomorphic subleading terms — are the sort of thing a paper would not preserve.
- **The string-worldsheet speculation (insights 12–14) is spoken only, and is a recognisable precursor to
  celestial holography.** The written lectures do make the celestial-CFT suggestion, but soberly and without
  the worldsheet identification, the $g_s^2$ discrepancy, or the Giveon–Kutasov–Seiberg route. `worldsheet`
  and `world sheet` occur zero times in `soft_Arxiv_update.tex`.
- **Provenance the papers do not record (insight 7).** That the QED corner traces to an unpublished note
  Maldacena shared with him is the kind of fact only a talk carries.
- **Tone.** In 2013 this is "a work in progress ... I welcome your input" and "I probably will raise more
  questions than answers"; by 2016 the same material is introduced as "an exact mathematical equivalence
  between three phenomena". Nothing dishonest happened in between — but the change in register is itself
  evidence about how confidence in the programme was built.
- **Reverse delta (in the notes, absent here):** memory (the third corner is never mentioned — this talk has
  only two corners), vacuum degeneracy and Goldstone bosons, soft hair and black holes, infrared divergences,
  the massive-particle generalisation, and colour memory.

---

## Transcript quality notes

These captions have evidently been cleaned up relative to the others in the set — punctuation and sentence
casing are present — but the proper nouns are still damaged: "Barnich and Troost" for Barnich and Troessaert,
"cat moody" / "Kac-Moody" (inconsistently), "Linebarger's theorem" for Weinberg's theorem, "Wan" for Juan
(Maldacena), "Karan" for the questioner (content suggests Cumrun Vafa; unconfirmed), "Wald and Zupancic" for
Wald and Zoupas, "Argers Douglas" for Argyres–Douglas, "scribe plus" for scri-plus, "billion"/"a billion" for
abelian, "masslic" for massless, "worksheet" for worldsheet, "dzdv" and similar index strings garbled
throughout. The venue attribution in the source file's header contradicts the recording (see above) and
should be corrected. Slides are not recoverable, and one question at `00:34:15` is transcribed almost
verbatim in the questioner's voice with no speaker change marked, which makes the duality exchange hard to
segment.
