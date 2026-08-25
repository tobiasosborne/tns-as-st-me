<!-- ROLE: mandatory pre-reading for the P4 writeup agent (law L7 exception).
     The writeup agent reads this file AND refs/arxiv-1305.2176 (the register
     target) BEFORE drafting a sentence. AUTHORED 2026-08-25 per TJO directive;
     REWRITTEN 2026-08-25 per TJO directive: every rule below is extracted from
     the five exemplars in refs/prose-exemplars/ and evidenced by quotation.
     Rules that could not be evidenced were cut (see §6). -->

# Prose guide for the PRL writeup

## 0. Where these rules come from

The register target for layout, density and citation habits stays
`refs/arxiv-1305.2176` (Haegeman–Michalakis–Nachtergaele–Osborne–Schuch–
Verstraete, PRL 111, 080401). Read several pages of it before writing.

The *prose* rules below are not style folklore. Each was extracted from five
short texts that did hard things in public and survived, stored locally:

| file | verified identity | what it teaches |
|---|---|---|
| `refs/prose-exemplars/watson-crick-1953.pdf` | Nature 171, 737 (25 Apr 1953), "Molecular Structure of Nucleic Acids: A Structure for Deoxyribose Nucleic Acid" | understatement as authority; ~1100 words |
| `refs/prose-exemplars/einstein-1905-specrel-en.pdf` | "On the Electrodynamics of Moving Bodies" (1923 Methuen transl., fourmilab ed.) | audacity introduced through humble observation; operational definitions |
| `refs/prose-exemplars/shannon-1948.pdf` | Bell System Technical Journal 27, 379–423, 623–656 (1948) | a new field opened in plain declaratives; examples before generality |
| `refs/prose-exemplars/bell-1964.pdf` | Physics 1, 195–200 (1964), "On the Einstein Podolsky Rosen Paradox" | stakes in one page; math no heavier than needed |
| `refs/prose-exemplars/darwin-origin.txt` | *On the Origin of Species*, 1859 first edition (Gutenberg #1228) | pre-emptive objections; hedging that is not weakness |

**Quote provenance.** Every quotation was checked against the local file
(page-indexed `pdftotext` for the PDFs). The scanned PDFs carry OCR damage
(split words `i s`, `h a s`; inline footnote digits); that damage is silently
repaired in the quotes below, and nothing else is altered.

## 1. Simple communication

1. **State the whole result in one sentence, early, in ordinary words.** Bell
   gives the entire content of his theorem in the third sentence of the paper:
   > "In this note that idea will be formulated mathematically and shown to be
   > incompatible with the statistical predictions of quantum mechanics."
   > — Bell 1964, p. 195
   Shannon does the same for a whole field:
   > "The fundamental problem of communication is that of reproducing at one
   > point either exactly or approximately a message selected at another point."
   > — Shannon 1948, p. 1
   Our equivalent must exist and must be findable in the first paragraph.

2. **Open the paper on something the reader already has, not on the new thing.**
   Einstein reaches the two postulates only after a paragraph about a magnet and
   a coil:
   > "Take, for example, the reciprocal electrodynamic action of a magnet and a
   > conductor." — Einstein 1905, p. 1
   > "It is known that Maxwell's electrodynamics—as usually understood at the
   > present time—when applied to moving bodies, leads to asymmetries which do
   > not appear to be inherent in the phenomena." — Einstein 1905, p. 1
   Start from the magnon and the kink, not from the triangle.

3. **Define by an operation the reader could perform.** Einstein defines time by
   a watch and a train, and length by two stated measurement procedures:
   > "If, for instance, I say, 'That train arrives here at 7 o'clock,' I mean
   > something like this: 'The pointing of the small hand of my watch to 7 and
   > the arrival of the train are simultaneous events.'" — Einstein 1905, p. 2
   Length is then "ascertained by the following two operations" (p. 4), both
   spelled out. Our charges, windows and displacements get the same treatment:
   what is measured, on what state, with which limit taken in which order.

4. **Give the elementary case before the general one, and say you are doing it.**
   > "The proof of the main result is quite simple. Before giving it, however, a
   > number of illustrations may serve to put it in perspective."
   > — Bell 1964, p. 196
   > "Firstly, there is no difficulty in giving a hidden variable account of spin
   > measurements on a single particle." — Bell 1964, p. 196
   Bell spends a full section on three worked examples first. The XXZ /
   free-magnon case earns its place ahead of the general MPS statement.

5. **Concrete nouns, itemised.** Shannon defines a channel by listing what one
   is:
   > "The channel is merely the medium used to transmit the signal from
   > transmitter to receiver. It may be a pair of wires, a coaxial cable, a band
   > of radio frequencies, a beam of light, etc." — Shannon 1948, p. 2
   Write "the magnon passes through the kink and shifts it by δx", never "a
   displacement is induced via the magnon–kink interaction mechanism".

6. **Open a paragraph or list item with its point.** Shannon's three reasons for
   the logarithm are three declaratives:
   > "1. It is practically more useful. … 2. It is nearer to our intuitive
   > feeling as to the proper measure. … 3. It is mathematically more suitable."
   > — Shannon 1948, p. 1
   A reader skimming first sentences must get the whole argument.

7. **Name a thing only after describing it, and only if the name pays rent.**
   Darwin coins in the sentence that closes the description:
   > "This preservation of favourable variations and the rejection of injurious
   > variations, I call Natural Selection." — Darwin, Ch. IV
   Shannon names the unit and credits the namer in the same breath:
   > "If the base 2 is used the resulting units may be called binary digits, or
   > more briefly bits, a word suggested by J. W. Tukey." — Shannon 1948, p. 1
   Each coinage of ours ("lattice Braginsky–Thorne relation") must be flagged as
   a coinage, defined immediately after the phenomenon, and used more than once.

8. **Push machinery out of the main text and say where it went.** Shannon states
   theorems in the body and proves them in Appendices 1–4:
   > "In Appendix 2, the following result is established" — Shannon 1948, p. 11
   Watson and Crick defer the whole apparatus in one sentence:
   > "Full details of the structure, including the conditions assumed in building
   > it, together with a set of co-ordinates for the atoms, will be published
   > elsewhere." — Watson & Crick 1953, p. 737
   Window vectors, torsors and Lamport step numbers live in the appendices or
   the repo, with one sentence in the Letter pointing there.

9. **Grade the difficulty honestly, in both directions.** Say when something is
   easy; that is what makes it credible when you say something is hard.
   > "In the teletype case where all symbols are of the same duration, and any
   > sequence of the 32 symbols is allowed the answer is easy."
   > — Shannon 1948, p. 3
   > "but as the probability of this is zero we will not make special
   > prescriptions for it" — Bell 1964, p. 196
   One clause disposes of a measure-zero technicality. Do likewise; do not build
   a subsection around a triviality, and do not call a hard step routine.

## 2. No arrogant tone

10. **State novelty once, as a fact, then never again.** Watson and Crick claim
    importance in exactly one clause and never return to it:
    > "This structure has novel features which are of considerable biological
    > interest." — Watson & Crick 1953, p. 737
    > "The novel feature of the structure is the manner in which the two chains
    > are held together by the purine and pyrimidine bases."
    > — Watson & Crick 1953, p. 737
    The second sentence is descriptive, not evaluative. No self-praise
    adjectives — "remarkable", "striking", "powerful", "surprisingly simple" —
    attach to our own results anywhere else in the Letter.

11. **Offer, do not announce.** The verbs of the exemplars are modest even when
    the content is not:
    > "We wish to suggest a structure for the salt of deoxyribose nucleic acid"
    > — Watson & Crick 1953, p. 737
    > "We will raise this conjecture (the purport of which will hereafter be
    > called the 'Principle of Relativity') to the status of a postulate"
    > — Einstein 1905, p. 1
    "We suggest", "we prove", "we extend" — never "we finally establish", never
    "for the first time".

12. **Disagreement is allowed; editorialising is not.** The exemplars *do*
    reject prior work — in one sentence, with a reason or a pointer, then they
    move on:
    > "In our opinion, this structure is unsatisfactory for two reasons:"
    > — Watson & Crick 1953, p. 737
    > "These attempts have been examined elsewhere [4] and found wanting."
    > — Bell 1964, p. 195
    Note what they never do: attribute confusion, sloppiness or naivety to
    people. Say what is wrong with the *statement*, in one sentence, and give the
    reason or the reference. Then stop.

13. **When there is nothing useful to say, say nothing — out loud.**
    > "This structure as described is rather ill-defined, and for this reason we
    > shall not comment on it." — Watson & Crick 1953, p. 737
    Silence is stated and justified, not implied by omission.

14. **Credit before claiming, by name, precisely.** All five do this, and the
    priority is never blurred:
    > "Mr. Wallace, who is now studying the natural history of the Malay
    > archipelago, has arrived at almost exactly the same general conclusions
    > that I have on the origin of species." — Darwin, Introduction
    > "They kindly made their manuscript available to us in advance of
    > publication." — Watson & Crick 1953, p. 737
    > "In conclusion I wish to say that in working at the problem here dealt with
    > I have had the loyal assistance of my friend and colleague M. Besso"
    > — Einstein 1905, p. 23
    Ours: Hamada–Sugishita built the continuum global-symmetry triangle;
    Lan–Xiao observed the wall displacement; Dyson found the soft decoupling.
    The sentence structure must make their priority unmistakable *before* we say
    what is new here.

15. **Explain a choice in one sentence, then return to work.**
    > "I hope that I may be excused for entering on these personal details, as I
    > give them to show that I have not been hasty in coming to a decision."
    > — Darwin, Introduction

## 3. Cautious scientific optimism

16. **Label the evidential status of every claim, in the same sentence.**
    > "it must be regarded as unproved until it has been checked against more
    > exact results" — Watson & Crick 1953, p. 737
    > "I am convinced that Natural Selection has been the main but not exclusive
    > means of modification." — Darwin, Introduction
    "We prove", "we verify to 10⁻¹⁵", "numerics at N ≤ 200 are consistent with",
    "we conjecture" — and a conjecture is called a conjecture in the breath it is
    stated. "the main but not exclusive" is the model for our SPT claim.

17. **State the strongest objection against yourself, at full strength, before
    answering it.** This is Darwin's central move and the campaign's register:
    > "That many and grave objections may be advanced against the theory of
    > descent with modification through natural selection, I do not deny. I have
    > endeavoured to give to them their full force." — Darwin, Ch. XIV
    > "seems, I freely confess, absurd in the highest possible degree"
    > — Darwin, Ch. VI
    Note the shape: full-strength objection, then *"but"*, then the argument. The
    confession never becomes an apology and never stands alone.

18. **Name the condition under which you would be wrong.** Bell hands the reader
    the escape route from his own theorem:
    > "Of course, the situation is different if the quantum mechanical
    > predictions are of limited validity." — Bell 1964, p. 199
    Validity domains, the ansatz-vs-model gap, weak-* convergence and the
    nearest-neighbour hypothesis each get one such sentence — in the Letter or
    the appendices, briefly, without self-flagellation.

19. **Admit what a result does not do, especially your own.**
    > "This theorem, and the assumptions required for its proof, are in no way
    > necessary for the present theory." — Shannon 1948, p. 11
    > "The real justification of these definitions, however, will reside in their
    > implications." — Shannon 1948, p. 11
    If a lemma is decoration rather than load-bearing, say so and keep it.
    Darwin opens the same way: "This Abstract, which I now publish, must
    necessarily be imperfect." (Introduction).

20. **Optimism is a concrete next experiment or a bounded possibility.**
    > "In that connection, experiments of the type proposed by Bohm and Aharonov
    > [6], in which the settings are changed during the flight of the particles,
    > are crucial." — Bell 1964, p. 199
    > "In the distant future I see open fields for far more important
    > researches." — Darwin, Ch. XIV
    Higher dimensions, other symmetry classes, cold-atom realisation: stated as
    possibility ("suggests", "may extend"), in the outlook, never in the abstract.

21. **One sentence of reach, at the very end, and only after the caution.** Two
    famous closing sentences, both unhedged, both earned by pages of hedging:
    > "It has not escaped our notice that the specific pairing we have postulated
    > immediately suggests a possible copying mechanism for the genetic
    > material." — Watson & Crick 1953, p. 737
    > "from so simple a beginning endless forms most beautiful and most wonderful
    > have been, and are being, evolved." — Darwin, Ch. XIV
    We are permitted exactly one such sentence. It goes last. If the SPT
    prediction survives only partially, the abstract reflects the proved part and
    this sentence is clearly marked as hope.

## 4. Moves to steal

22. Sentence-level patterns lifted directly from the five, for reuse:
    - **Result-first passive.** "The main result will now be proved."
      (Bell, p. 197); "But it will be shown that this is not possible."
      (Bell, p. 196). Use the passive when the *result* is the subject; use the
      active when a person or a computation acts.
    - **Hypothesis-with-a-shrug.** "Now we make the hypothesis [2], and it seems
      one at least worth considering" (Bell, p. 195).
    - **The closing loop.** Answer, in the last section, the exact question the
      first paragraph raised: "Furthermore it is clear that the asymmetry
      mentioned in the introduction as arising when we consider the currents
      produced by the relative motion of a magnet and a conductor, now
      disappears." (Einstein, p. 15).
    - **Section-opening question that admits a debt.** "How will the struggle for
      existence, discussed too briefly in the last chapter, act in regard to
      variation?" (Darwin, Ch. IV).
    - **Scope fence.** "These semantic aspects of communication are irrelevant
      to the engineering problem." (Shannon, p. 1) — declare what is out of
      scope; do not apologise for not covering it.
    - **Enumerated payoff.** "We will now enumerate the properties of the motion
      of the electron which result from the system of equations (A), and are
      accessible to experiment." (Einstein, p. 23) — then a numbered list of
      testable consequences. The template for our predictions section.
    - **Figure caption that stands alone.** "This figure is purely diagrammatic.
      The two ribbons symbolize the two phosphate-sugar chains, and the
      horizontal rods the pairs of bases holding the chains together."
      (Watson & Crick, p. 737 caption).

## 5. Mechanics (campaign)

23. Abstract ≤ 600 characters, no symbols that need definitions, one sentence
    each: setting, result, verification, why it matters. The model for the
    result sentence is Bell's p. 195 sentence quoted in rule 1.
24. Length discipline. Watson–Crick announce the structure of DNA in ~1100
    words; Bell gives stakes, three illustrations, theorem and experimental
    consequence in six pages. 4 pages of main text is not tight.
25. The three figure captions carry the story on their own (law L9): figures +
    captions alone must teach the triangle, the soft theorem, and the memory
    effect's magnitude. Caption pattern: rule 22.
26. Cite from `paper/refs.bib` only (L3-verified); no citation from memory. Note
    that Watson–Crick cite six items and Bell seven — a Letter cites what it
    uses, not what it has read.
27. Every statement in the Letter traces to a PROVED claim in `claims/CLAIMS.md`
    or is labelled a conjecture (L9). Rule 16 is how the labelling is worded.
28. Notation and definitions come from `notation.md` / `definitions.md` and are
    never redefined in the paper (L4).

## 6. Rules cut in the 2026-08-25 rewrite

- *"Orwell's rule applies…"* — folklore; Orwell is not one of the five.
  Concision survives as rules 5, 8 and 24, evidenced by what the exemplars do.
- *"Never disparage prior work; forbidden: 'we clarify the confusion in…'"* —
  contradicted (Watson–Crick p. 737, Bell p. 195, Darwin on the *Vestiges of
  Creation*, Introduction). Replaced by rule 12: the editorialising is
  forbidden, the disagreement is not.
- *"No self-praise adjectives"* as an absolute — contradicted by "considerable
  biological interest" (Watson–Crick p. 737) and "There is grandeur in this view
  of life, with its several powers, having been originally breathed into a few
  forms or into one" (Darwin, Ch. XIV). Replaced by rules 10 and 21: one factual
  novelty claim, one closing sentence of reach, nothing in between.
- *"Passive voice only when the actor is genuinely irrelevant."* — contradicted;
  Bell, Shannon and Einstein use the result-first passive constantly (rule 22).
- *"Read the draft aloud once."* — a process tip with no support in the five
  texts. The final check is now rule 6: read only the first sentence of each
  paragraph and confirm the argument is complete.
