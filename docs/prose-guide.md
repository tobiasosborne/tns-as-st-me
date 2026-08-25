<!-- ROLE: mandatory pre-reading for the P4 writeup agent (law L7 exception).
     The writeup agent reads this file AND refs/arxiv-1305.2176 (the register
     target) BEFORE drafting a sentence. AUTHORED 2026-08-25 per TJO directive. -->

# Prose guide for the PRL writeup

The register target is refs/arxiv-1305.2176 (Haegeman–Michalakis–Nachtergaele–
Osborne–Schuch–Verstraete, PRL 111, 080401): precise statements carried by
plain declarative prose, mathematics stated exactly once, no theatrics. Read
several pages of it before writing. Then obey the following.

## Simple communication

1. One idea per sentence. If a sentence needs a second reading, split it.
2. Prefer the concrete noun and the active verb. "The magnon passes through
   the kink and shifts it by δx" — not "a displacement is induced via the
   magnon–kink interaction mechanism".
3. Every symbol earns its place: introduce it once, use it, or cut it. The
   Letter is not the repo; most internal machinery (window vectors, torsors,
   Lamport step numbers) stays in the appendices or the repo.
4. The reader is a busy physicist, not a referee to be impressed. Orwell's
   rule applies: never use a long word where a short one does; cut every word
   that does no work.
5. Paragraphs open with their point. A reader skimming first sentences should
   get the whole argument.
6. No coinage without necessity. Each coined term ("lattice Braginsky–Thorne
   relation") must be flagged as a coinage and used only if it pays rent.

## No arrogant tone

7. Never disparage prior work. The continuum literature is the shoulders we
   stand on, not a mess we fixed. Forbidden framings: "we clarify the
   confusion in…", "unlike previous heuristic treatments…". Allowed: "on the
   lattice these statements become finite and checkable."
8. No self-praise adjectives: "remarkable", "striking", "powerful", "elegant",
   "surprisingly simple" are banned for our own results. State the result; if
   it is remarkable the reader will notice.
9. Credit precisely: Hamada–Sugishita built the continuum global-symmetry
   triangle; Lan–Xiao observed the wall displacement; Dyson found the soft
   decoupling. Our sentence structure must make their priority unmistakable
   before stating what is new here.

## Cautious scientific optimism

10. Claim exactly what is proved, in the tense of proof: "we prove", "we
    verify to 10⁻¹⁵", "numerics at N ≤ 200 are consistent with". Conjectures
    are labelled conjectures in the same breath they are stated.
11. Every limitation the repo knows (validity domains, the ansatz-vs-model
    gap, weak-* only convergence, nearest-neighbour hypotheses) appears in the
    Letter or its appendices — briefly, without self-flagellation. One honest
    sentence beats a defensive paragraph.
12. Optimism lives in the outlook: what the result opens up (higher
    dimensions, other symmetry classes, experiments) is stated as possibility
    ("suggests", "may extend"), never as promise.
13. If the SPT prediction survives only partially, the abstract reflects the
    proved part; the hope goes in the final paragraph, clearly marked as hope.

## Mechanics

14. Abstract ≤ 600 characters, no symbols that need definitions, one sentence
    each: setting, result, verification, why it matters.
15. The three figure captions carry the story on their own (law L9): a reader
    who sees only figures + captions should learn the triangle, the soft
    theorem's content, and the memory effect's magnitude.
16. Cite from paper/refs.bib only (L3-verified); no citation from memory.
17. Passive voice only when the actor is genuinely irrelevant.
18. Final check before handing back: read the draft aloud once; any sentence
    you stumble on gets rewritten.
