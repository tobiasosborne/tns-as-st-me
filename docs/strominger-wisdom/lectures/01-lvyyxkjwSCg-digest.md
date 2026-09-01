# Lecture 1 digest — Introduction and Conserved Charges in Classical Electromagnetism

- **Title (as posted):** Infrared Structure of Gravity and Gauge Theory, Lecture 1 of 10
- **Video id:** `lvyyxkjwSCg`
- **URL:** https://youtu.be/lvyyxkjwSCg
- **Duration:** 01:49:35
- **Written companion:** arXiv:1703.05448 §1 (Introduction) and §2.1–2.5 (QED through "An Infinity of Conserved Charges")
- **Source:** `refs/strominger-videos/01-lvyyxkjwSCg.md` (auto-captions; secondary source, not L3 ground truth)

**Arc.** The first hour is motivation: the infrared triangle, its many "echoes", and five reasons to care
(connecting disparate subjects, flat-space holography, the missing definition of the gauge-theory S-matrix,
black-hole information, and the amplitude "miracles"). He then restarts from nineteenth-century Maxwell theory,
writes the Liénard–Wiechert field of a collection of charges in constant motion, sets up the Penrose diagram and
retarded/advanced Bondi coordinates, and shows by explicit limit that the leading radial electric field is
*discontinuous* at spatial infinity but obeys an antipodal matching condition. The last twenty minutes turn that
matching condition into an infinity of classically conserved charges, one for every function on the sphere, and
close on the promise that for non-constant gauge parameter the conservation law will mix matter charge with a new
field-theoretic term.

**How to read this digest.** Per the campaign brief, this is a *side-channel* harvest. Results and derivations that
the written notes already state are deliberately omitted; what is recorded here is what he says around the
mathematics — opinions, warnings, historical asides, answers to questions, and admissions about what is and is not
proved. The "Deltas" section at the end is the organizing principle, and it also records the checks where a
promising-sounding aside turned out to be in the written notes after all.

---

## Insights

1. **He dislikes the name "asymptotic symmetries" and says so at the outset.** The worry is that the word
   "asymptotic" suggests approximate; his view is that these are ordinary exact symmetries with exact conserved
   charges, and the adjective only records where they take a recognisable form.
   > "I kind of dislike this word asymptotic symmetries because it suggests that they're somehow not exact that
   > they're only true in some asymptotic sense but asymptotic symmetries are symmetries just like any other
   > Symmetry and the reason they're called asymptotic symmetries is that they typically take a simple and
   > recognizable form when you look at how they act on the asymptotic regions of space-time"
   `[lvyyxkjwSCg @ 00:01:06]` — tags: asymptotic-symmetries, methodology, charges

2. **He puts a number on how unfinished the programme is: roughly 500 possible triangles, roughly 30 papers so
   far.** The written notes say the subject is "in its infancy"; only the spoken version gives the arithmetic that
   makes that concrete.
   > "if you look at all the possibilities here there's of order 500 possibilities Each of which will require a
   > paper and maybe 30 of these papers have so far been written so this is a subject which is in its infancy which
   > I think makes it a lot of fun to talk about"
   `[lvyyxkjwSCg @ 00:07:38]` — tags: open-problems, history, methodology

3. **He flags that his own motivation has moved.** Flat-space holography is how he came into the subject but, he
   hints, not what he expects to leave with; the same disclaimer is repeated for black holes and for the amplitudes
   programme.
   > "the second motivation which is how I came into the subject maybe not how I go out of it but is I wanted to
   > understand the holographic structure of quantum gravity"
   `[lvyyxkjwSCg @ 00:10:54]` — tags: methodology, history

4. **On the symmetry group of quantum gravity in Minkowski space: the community not only did not know the answer,
   it knew it did not know, and we still do not know whether we have all of it.** His stated position is that the
   zeroth-order question is still unanswered, but that the tools now exist.
   > "not only did they did people not know it they knew that they didn't know it and now we know a lot more about
   > it we've understood something about um BMS and super translations but we also know that there are still more
   > pieces of it that we have yet to understand we know that at the very least there is an infinite dimensional
   > symmetry group but we don't know if we have the whole infinite dimensional symmetry group"
   `[lvyyxkjwSCg @ 00:11:57]` — tags: open-problems, asymptotic-symmetries

5. **He assigns Weinberg chapter 13 as reading and states flatly that there is no definition of the S-matrix in
   QED or the Standard Model.** This is the blunt spoken version of the written notes' more hedged "generically no
   IR finite S-matrix exists".
   > "one of the readings will be chapter 13 in weinberg's [...] textbook and you will see there that [...] there
   > is no definition of the S Matrix in the standard model or in QED because of the problem of [...] infrared
   > Divergence"
   `[lvyyxkjwSCg @ 00:16:13]` — tags: ir-divergences, open-problems, methodology

6. **He labels his own motivation section "BS".** A joke, but a useful signal about how he separates advocacy from
   the technical content that follows.
   > "that is kind of the the end of the section which I've entitled BS in my notes Here and now I'm about to
   > actually start to write down some equations but are there any questions about the BS"
   `[lvyyxkjwSCg @ 00:20:25]` — tags: methodology

7. **There is no canonical entry point into the subject; he chooses the earliest possible one on purpose.** The
   interconnection is the difficulty: gauge theory or gravity, soft theorems or symmetries, all are valid starting
   points, and he picks 19th-century electromagnetism as the simplest.
   > "it's an interconnection between many different things so there's a question of where you start whether I
   > start with Gauge Theory or with gravity uh with soft theorems or with symmetries and so there are many
   > different ways to present this but I think I'm gonna start in sort of the simplest context"
   `[lvyyxkjwSCg @ 00:20:25]` — tags: methodology

8. **He breaks his own habit and keeps every factor of two and pi, and gives the reason: the payoff of the subject
   is watching two very differently written objects turn out to be exactly equal.** He also invites the audience to
   check his algebra as he goes.
   > "unlike in most courses that I teach I'm actually going to try to get all the factors and everything right
   > that that I may find that challenging but I'm going to try [...] the reason for that it's so much fun to see
   > these things being exactly equal even though they're written in in such different ways"
   `[lvyyxkjwSCg @ 00:21:30]`; also "I hope everybody is checking me" `[lvyyxkjwSCg @ 01:00:09]`
   — tags: methodology

9. **The discontinuity of the Liénard–Wiechert field is something he had seen and suppressed for his whole career,
   and only noticed about a year before the course.** He calls it the bedrock of everything that follows and goes
   through it in deliberately pedantic detail for that reason.
   > "we we've all seen this formula before we've probably also all suppressed it or at least I have and I did not
   > realize until a few a few years ago really only a year ago that this formula has a very peculiar property [...]
   > this came as kind of a surprise to me though I'm sure many many people knew it but this is going to be crucial
   > this fact is going to sort of be the Bedrock of everything we do from here on so I'm going to go through it in
   > pedantic detail"
   `[lvyyxkjwSCg @ 00:35:17]` — tags: methodology, pitfalls, history, charges

10. **The 1960s–1980s literature on the large-r expansion in gravity was, in his telling, substantially wrong, and
    that wrongness is why the present story looked impossible before Christodoulou–Klainerman.** The written notes
    mention "misconceptions about asymptotic falloffs" in passing; the spoken version is much more direct about a
    body of work being incorrect and about the confusion it caused.
    > "there was a lot of discussion about it by Penrose in collaboration a lot of papers on it in this 60s 70s and
    > 80s which actually turned out to be wrong and was led to a lot of confusion in the community and it's part of
    > the reason that the story that I'm able to tell now is made sense only in light of [...] seemed manifestly
    > wrong before Christ[odoulou] [and] kleinerman [Klainerman]"
    `[lvyyxkjwSCg @ 01:22:45]` — tags: history, pitfalls, methodology

11. **His judgment on where the rigour actually is: gravity is in better shape than gauge theory.** The falloff
    behaviour has been proved for gravity but much less for electromagnetism and non-abelian gauge theory, which is
    the reverse of what one might expect from "gravity is harder".
    > "interestingly the situation in not a billion [non-abelian] gauge Theory is not as good as the situation in
    > gravity as far as how much is understood why the mathematicians chose to nail gravity to death before [...] a
    > lot of the statements have been rigorously proved for Gravity but less for electromagnetism"
    `[lvyyxkjwSCg @ 01:24:51]` — tags: methodology, open-problems

12. **Answering a question, he says the antipodal matching condition has, as far as he knows, no first-principles
    proof — it is an observed property of a 120-year-old formula, verified in every example, and derivable from the
    quantum soft photon theorem, which he finds backwards.** This is the sharpest open-problem statement in the
    lecture and is directly relevant to any attempt to give the matching condition an independent derivation.
    > "I've never seen this matching condition discussed it's a property of the Leonard Victor [Liénard–Wiechert]
    > potential and that's been sitting there for 130 years [...] you can derive it Quantum mechanically from the
    > soft Photon theorem the soft Photon theorem implies it but it seems like uh pretty weird to be using Quantum
    > field Theory to preserve proof of [i.e. to prove] results relevant to 19th century electromagnetism [...] I
    > would think that there would be some set of assumptions and some some way to uh prove it make it into a
    > mathematical theorem but I I haven't I haven't seen that"
    `[lvyyxkjwSCg @ 01:26:02]` — tags: open-problems, charges, methodology

13. **His stated bet, hedged: it is probably not hard to prove that antipodal matching is the *only* Lorentz
    invariant boundary condition, but he has not tried; and some such condition is mandatory, because otherwise the
    scattering problem is not defined.** The "you need to define what you are doing all the way out at infinity"
    framing is the practical reason the condition cannot simply be dropped.
    > "I believe it would not be hard to prove that this is the only Lorenzen variant [Lorentz-invariant] boundary
    > condition though though I haven't tried to do it"; and "if you want to solve a scattering problem you need to
    > Define what you're doing all the way out at Infinity so you need to know your starting point for integrating
    > the constraints"
    `[lvyyxkjwSCg @ 01:28:42]` — tags: open-problems, charges, methodology

14. **He prefers the formulation "the fields are constant along the generators of null infinity, including where
    they cross spatial infinity" because it is the one that will survive into quantum gravity.** Saying "same value
    at the two ends of a light ray" will not survive curvature and caustics. He adds that the condition surprised
    him at first and has grown more natural with use.
    > "when we go to quantum gravity which we will later on it doesn't make a lot of sense to describe it by saying
    > that the parameters take the same value at the beginning [and] the end [of] the light Ray because the space
    > will be curved and the light rays will be funny things and there will be caustics"; and "it surprised me a lot
    > when I first realized it but as you work with it it seems more and more natural"
    `[lvyyxkjwSCg @ 01:33:58]` — tags: charges, methodology, black-holes

15. **He suspects the subleading soft photon theorem is the same thing the SCET community calls reparameterization
    invariance of jets, and says only a few things are understood about it.** The written notes gesture at SCET but
    never name reparameterization invariance.
    > "there is Lowe's [Low's] sub leading soft Photon theorem [...] this I believe is also related to something
    > that the the scat [SCET] people call re-parameterization variants [invariance] of the Jets [...] a few things
    > are understood about it"
    `[lvyyxkjwSCg @ 01:20:39]` — tags: soft-theorems, open-problems

16. **His working method is explicit divide-and-conquer, and he names each thing being deferred: massive charges,
    magnetic charges, the boundary at future timelike infinity, black holes.** In passing he corrects himself about
    massive fields at null infinity — not simply exponential decay, but something stranger.
    > "for now we're divide and conquer we're going to isolate the issues one at a time and for now we're going to
    > ignore all issues associated with I plus"; and, on massive fields, "they die exponentially near or actually
    > they do really surprising weird counter-intuitive things at null Infinity"
    `[lvyyxkjwSCg @ 01:41:37]` and `[lvyyxkjwSCg @ 01:42:39]` — tags: methodology, pitfalls

17. **The antipodally-twisted definition of the sphere coordinate on past null infinity is a deliberate trade: he
    considered the alternative and judged it worse.** Worth knowing when reading his formulas, since the sign
    conventions are load-bearing and not forced.
    > "I might have called this W here and then said that W is just minus 1 over z bar but that again it would
    > introduce its own notational complexities"
    `[lvyyxkjwSCg @ 00:58:03]` — tags: pitfalls, methodology

---

## Structure of the argument (thin skeleton)

- `00:00:02–00:20:25` — Motivation: the three corners, the echoes, five applications. (Written notes §1.)
- `00:21:30–00:27:50` — Maxwell action, conventions with `1/e²` out front so charges are integers. (§2.1.)
- `00:28:52–00:35:17` — Liénard–Wiechert solution for charges in constant motion. (§2.1.)
- `00:36:20–00:58:03` — Penrose diagram, the five infinities, retarded/advanced Bondi coordinates and the
  antipodal `z` convention. (§2.2, §2.4.)
- `00:59:06–01:14:25` — The two limits to spatial infinity computed side by side; discontinuity; antipodal
  matching. (§2.3.)
- `01:20:39–01:35:09` — Question period: higher orders, first-principles derivations, rigour in gravity vs gauge
  theory, the conformal-cylinder picture.
- `01:35:09–01:49:11` — Infinity of conserved charges from matching alone; Gauss law rewriting; the constant-ε
  case reduces to ordinary charge conservation. (§2.5.)

---

## Deltas vs the written lectures (arXiv:1703.05448)

**Present in the video, absent from the written notes:**

- The "I dislike the term asymptotic symmetries" opinion (insight 1). In the TeX source this survives only as a
  *commented-out* footnote at the corresponding place in §1.1, so it does not appear in the published notes at all.
  The spoken version is the only place it is actually asserted.
- The quantitative estimate of the programme's size — about 500 triangles, about 30 papers written (insight 2).
  The notes say "in its infancy" without the count.
- "How I came into the subject, maybe not how I go out of it" (insight 3). The notes keep "This is how I came into
  the subject" and drop the second clause.
- The Weinberg-chapter-13 reading assignment and the flat claim that the S-matrix has no definition (insight 5).
- The personal history of the Liénard–Wiechert discontinuity: seen, suppressed, noticed only a year earlier
  (insight 9). The notes present the discontinuity as a straightforward calculation.
- The claim that a body of 1960s–1980s work on the large-r expansion was wrong and confused the community
  (insight 10). The notes' one clause about "misconceptions about asymptotic falloffs" is far milder and appears in
  the gravity context only.
- The comparison of rigour between gravity, electromagnetism and non-abelian gauge theory (insight 11).
- The whole exchange on whether antipodal matching can be derived from first principles, including "I've never seen
  this matching condition discussed", the 130-years remark, the discomfort at using QFT to prove a 19th-century
  fact, and the hedged bet about uniqueness among Lorentz-invariant conditions (insights 12, 13). The notes assert
  Lorentz and CPT invariance and move on. This is the single largest delta in the lecture and the most directly
  usable one.
- The caustics argument for preferring the "constant along the generators of scri" phrasing over "same value at the
  two ends of a light ray" (insight 14). The notes give the conformal-cylinder picture but not this motivation.
- The suggested identification of the subleading soft theorem with SCET reparameterization invariance (insight 15).
  The string "reparameteriz" does not occur anywhere in the written notes.
- The self-corrected remark that massive fields do "weird counter-intuitive things" at null infinity rather than
  simply decaying (insight 16).
- Methodological asides: the factor-keeping policy and its stated reason (insight 8), the "BS" label (insight 6),
  the acknowledgement that the notation choice was a trade-off (insight 17).

**Checked and *not* a delta** (these sound like asides but are in the written notes, so they are not recorded as
insights above):

- The dipole-moment warning about the `1/r²` term — written out at length in §2.3.
- "Almost anything, even Maxwell electromagnetism with one point particle, is singular at spatial infinity" — §2.2.
- Lorentz transformations being singular at `i⁰` and a boost toward the north pole in the future being a boost away
  from it in the past — §2.3.
- The preference for the two-points-per-sphere Penrose diagram because of the antipodal map — §2.2.
- The remark that the extra term in the non-constant-ε conservation law is "mysterious" — the word "mysterious" is
  literally in §2.5.
- The decision not to consider `u`-dependent ε because nothing new comes of it — §2.5 ("turns out not to yield
  anything new"). The *reason* is only given in lecture 3; see that digest.
- That radiative modes must die off at early and late times for finite energy, and that adding them does not
  disturb the Coulombic matching — §2.3.
- That Feynman diagrammatics implicitly assume the matching condition — §2.3.

**Transcript quality.** Good overall; the mathematics is followable. Recurrent ASR substitutions to normalise:
"nether's theorem" = Noether's theorem; "block and nordsick" = Bloch and Nordsieck; "Leonard v card" / "Leonard
Beaker" / "Leonard Victor" = Liénard–Wiechert; "Christa dulu and kleinerman" = Christodoulou and Klainerman;
"scribe plus" / "scry" / "Sky Plus" / "scram minus" = scri (null infinity); "koshy surface" = Cauchy surface;
"not a billion gauge theory" = non-abelian gauge theory; "lorentz" and "Lorenz" are interchanged throughout;
"Lowe" = Low; "scat" = SCET; "pancreay group" / "plank array group" = Poincaré group; "in typically" = antipodally;
"anti-decider space" = anti-de Sitter space. Two `[Music]` markers mask a few seconds each around `01:44:59` and
`00:01:48`. Nothing load-bearing appears to be lost.
