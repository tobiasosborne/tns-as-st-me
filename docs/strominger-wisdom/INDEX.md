# The Wisdom of Strominger — index

A queryable secondary source distilled from auto-captioned video transcripts of
Andrew Strominger's infrared-structure lectures and talks, plus one guest
lecture. Built for `bd tns-t66`.

---

## 1. What this is (and what it is not)

**What it is.** Sixteen talks were transcribed (`refs/strominger-videos/`) and
harvested for the *side channel*: opinions, warnings, hesitations, historical
asides, answers to audience questions, admissions about what is proved and what
is assumed, and the framings a speaker uses out loud but does not put in a
paper. Each per-source digest deliberately does **not** restate derivations
that already appear in the written lectures, arXiv:1703.05448
(`refs/arxiv-1703.05448/`). Every digest carries a "Deltas vs the written
lectures" section recording both what is genuinely new and what was checked and
found to be already written.

**What it is not.** This database is **not L3 ground truth.** Repo law L3 says
references are quoted from local TeX in `refs/arxiv-<id>/`, never from memory —
and never, therefore, from a YouTube auto-caption. Concretely:

- No formula here is citable. Board work is invisible to the captions; index
  structure, signs and factors are routinely unrecoverable. Several digests say
  so explicitly at the line in question.
- No sentence here should be quoted in the paper as Strominger's words. Where a
  spoken remark is worth citing, find the corresponding statement in the TeX and
  cite that. See §4 for three specific traps.
- Attributions and dates are soft. ASR mangles names badly; several venues and
  collaborator names in this corpus are inferred, not established.

**What it is good for.** Locating the position a working expert takes on a
question that a paper leaves silent: what is assumed rather than derived, which
step is the hard one, which received statement he thinks is wrong, and where he
says plainly that he does not know. That is the material that helps a campaign
decide what to claim and how loudly.

---

## 2. Source inventory

Speaker is Andrew Strominger throughout **except lecture 9** — see the caution
below the table.

| # | Title | Speaker | Venue / date | Duration | Digest | Transcript |
|---|---|---|---|---|---|---|
| 01 | Introduction and Conserved Charges in Classical Electromagnetism | Strominger | Harvard course, *Infrared Structure of Gravity and Gauge Theory* (10 lectures); no date on the recordings — internal evidence puts the course between the first LIGO detections (announced Feb 2016) and the written notes (arXiv:1703.05448, Mar 2017) | 1:49:35 | [01](lectures/01-lvyyxkjwSCg-digest.md) | [`01-lvyyxkjwSCg.md`](../../refs/strominger-videos/01-lvyyxkjwSCg.md) |
| 02 | Large Gauge Symmetry in Massless QED | Strominger | same course | 1:57:03 | [02](lectures/02-yeMZKViadhw-digest.md) | [`02-yeMZKViadhw.md`](../../refs/strominger-videos/02-yeMZKViadhw.md) |
| 03 | Asymptotic Symmetries and Soft Theorems | Strominger | same course | 1:48:15 | [03](lectures/03-swrNwD0ypaE-digest.md) | [`03-swrNwD0ypaE.md`](../../refs/strominger-videos/03-swrNwD0ypaE.md) |
| 04 | Massive QED, Hyperbolic Slicing, and Magnetic Soft Theorems | Strominger | same course | 1:53:41 | [04](lectures/04-xZ2FG1kLb9I-digest.md) | [`04-xZ2FG1kLb9I.md`](../../refs/strominger-videos/04-xZ2FG1kLb9I.md) |
| 05 | Infinite-Dimensional Fermionic Symmetry in Supersymmetric Gauge Theory | Strominger | same course | 1:44:20 | [05](lectures/05-WxCY-K-Jb4A-digest.md) | [`05-WxCY-K-Jb4A.md`](../../refs/strominger-videos/05-WxCY-K-Jb4A.md) |
| 06 | Large Gauge Symmetry in Non-Abelian Gauge Theory | Strominger | same course | 1:22:30 | [06](lectures/06-OXl7IXT7_Cw-digest.md) | [`06-OXl7IXT7_Cw.md`](../../refs/strominger-videos/06-OXl7IXT7_Cw.md) |
| 07 | Supertranslation Charges and Ward Identity | Strominger | same course | 1:48:05 | [07](lectures/07-Yx7PWgfC1dw-digest.md) | [`07-Yx7PWgfC1dw.md`](../../refs/strominger-videos/07-Yx7PWgfC1dw.md) |
| 08 | Superrotation Charges and Ward Identity | Strominger | same course | 1:35:42 | [08](lectures/08-60U7_P2XJlQ-digest.md) | [`08-60U7_P2XJlQ.md`](../../refs/strominger-videos/08-60U7_P2XJlQ.md) |
| 09 | Memory Effects | **guest lecturer "Sasha" — NOT Strominger** | same course | 1:51:49 | [09](lectures/09-8Aml1ToQtt4-digest.md) | [`09-8Aml1ToQtt4.md`](../../refs/strominger-videos/09-8Aml1ToQtt4.md) |
| 10 | Soft Hair on Black Holes | Strominger | same course | 1:44:14 | [10](lectures/10-H4IZ3jwTDp4-digest.md) | [`10-H4IZ3jwTDp4.md`](../../refs/strominger-videos/10-H4IZ3jwTDp4.md) |
| cstq | The Infrared Triangle in Quantum Gravity | Strominger | CSTQ colloquium (Center for SpaceTime and the Quantum), delivered remotely to Marseille; late period — the last third post-dates the written notes entirely | 1:08:23 | [cstq](lectures/cstq-6kH2pl_zvMA-digest.md) | [`cstq-6kH2pl_zvMA.md`](../../refs/strominger-videos/cstq-6kH2pl_zvMA.md) |
| extra-01 | Memory, Symmetries and Soft Theorems | Strominger | venue not stated on the recording. **Dating correction: early-to-mid 2015**, not whatever the file order suggests — he refers to "Joe's birthday last year" (Polchinski's 60th, 2014), says the spin-memory paper with "Sasha" is already written (arXiv:1502.06120, Feb 2015), and says the massive-particle generalisation is being written now | 1:23:59 | [extra-01](lectures/extra-01-CdFyoaNv8GI-digest.md) | [`extra-01-CdFyoaNv8GI.md`](../../refs/strominger-videos/extra-01-CdFyoaNv8GI.md) |
| extra-02 | Soft Hair on Black Holes | Strominger | Strings 2016, Beijing (named in the first sentence); part 1 of 2, Malcolm Perry gave part 2 | 0:30:53 | [extra-02](lectures/extra-02-wg-4Rm-kk70-digest.md) | [`extra-02-wg-4Rm-kk70.md`](../../refs/strominger-videos/extra-02-wg-4Rm-kk70.md) |
| extra-03 | Asymptotic Symmetries for Gauge and Gravitational Theories in Minkowski Space | Strominger | **Venue correction: the transcript header's guess of Perimeter, March 2014 (PIRSA:14030087) is wrong.** The recording opens "Seoul is really a wonderful city"; internal dating (Barnich–Troessaert "about 3 years ago"; the Yang–Mills analysis still unpublished work in progress) points to **mid-2013, probably Strings 2013 Seoul**. Probable, not established | 0:45:01 | [extra-03](lectures/extra-03-7S3Eg4VlZf0-digest.md) | [`extra-03-7S3Eg4VlZf0.md`](../../refs/strominger-videos/extra-03-7S3Eg4VlZf0.md) |
| extra-04 | Infrared Divergences in QED and Quantum Gravity | Strominger | Strings 2017, Tel Aviv (26–30 June 2017) | 0:34:47 | [extra-04](lectures/extra-04-GpN8VAauyj8-digest.md) | [`extra-04-GpN8VAauyj8.md`](../../refs/strominger-videos/extra-04-GpN8VAauyj8.md) |
| extra-05 | The Black Hole Information Paradox, Revisited | Strominger | Simons Center for Geometry and Physics seminar, 2016-04-05 (uploaded 2021) | 1:11:26 | [extra-05](lectures/extra-05-F42XbX45Dzw-digest.md) | [`extra-05-F42XbX45Dzw.md`](../../refs/strominger-videos/extra-05-F42XbX45Dzw.md) |

### Lecture 9 is a guest lecture — do not attribute it to Strominger

The speaker opens "my name is Sasha and today I will be talking instead of
Andy." He is most likely Alexander Zhiboedov, coauthor of the
Strominger–Zhiboedov spin-memory paper, but the transcript alone does not
confirm this. **Every opinion, hesitation, judgment and dissent in lecture 9 is
the guest lecturer's, not Strominger's.** This matters: lecture 9 contains the
sharpest statement in the corpus about calibration, and an open dissent from the
Goldstone-boson framing that Strominger and the written notes use freely. Those
are cross-source positions, not one person changing his mind. All entries
sourced from `8Aml1ToQtt4` in the topic files below are marked *(guest)*.

---

## 3. How to query

### By topic file

One file per tag with five or more entries across the corpus, in
[`topics/`](topics/):

| file | what lives there |
|---|---|
| [soft-theorems](topics/soft-theorems.md) | what a soft theorem is, how they are found, what they do and do not cover |
| [asymptotic-symmetries](topics/asymptotic-symmetries.md) | the construction, its squishy parts, what counts as a symmetry |
| [memory](topics/memory.md) | the third corner: what memory is, what it is measured against |
| [ward-identities](topics/ward-identities.md) | the A⇒C edge; what a Ward identity is when there is no S-matrix |
| [large-gauge](topics/large-gauge.md) | large gauge transformations, flat connections, phases |
| [ir-divergences](topics/ir-divergences.md) | divergences as a penalty; the missing S-matrix |
| [dressing](topics/dressing.md) | Faddeev–Kulish clouds and what they are not |
| [vacuum-degeneracy](topics/vacuum-degeneracy.md) | degenerate vacua, Goldstone language, superselection |
| [charges](topics/charges.md) | constructing charges, what they label, what they miss |
| [black-holes](topics/black-holes.md) | information, unitarity, AdS as the wrong laboratory |
| [soft-hair](topics/soft-hair.md) | the horizon construction and its stated limits |
| [celestial](topics/celestial.md) | the celestial sphere, current algebras, holography's status |
| [supertranslations](topics/supertranslations.md) | why they exist; the pulse-relabelling example |
| [superrotations](topics/superrotations.md) | the subleading corner, still unfinished |
| [methodology](topics/methodology.md) | how the work is actually done — the largest file |
| [history](topics/history.md) | BMS, Penrose, Christodoulou, attribution, sociology |
| [pitfalls](topics/pitfalls.md) | the confusions he corrects, including his own |
| [open-problems](topics/open-problems.md) | named gaps, admitted ignorance, failed attempts |
| [experiment](topics/experiment.md) | LIGO, LISA, pulsar timing, SQUIDs, the LHC |
| [nonabelian](topics/nonabelian.md) | why Yang–Mills is worse than QED or gravity |
| [susy](topics/susy.md) | the soft photino theorem and its counting argument |
| [misc](topics/misc.md) | cross-cutting entries that fit no single tag |

The single most useful file for this campaign is
[**campaign-hooks.md**](campaign-hooks.md), which maps the harvest onto the
lattice/MPS triangle, the two memory registers D32/D33, the operational razor,
the reduction program and corner A.

### By grepping tags in the digests

Every entry in a per-source digest carries a `tags:` line. To find everything
tagged `memory` across the corpus:

```
grep -n "tags:.*memory" docs/strominger-wisdom/lectures/*.md
```

Tags in use, with corpus-wide counts: methodology 205, open-problems 106,
history 91, charges 86, pitfalls 85, memory 57, soft-theorems 55,
asymptotic-symmetries 53, black-holes 41, celestial 39, large-gauge 37,
supertranslations 32, superrotations 30, vacuum-degeneracy 29,
ir-divergences 28, soft-hair 27, experiment 26, ward-identities 19,
nonabelian 17, dressing 13, susy 5.

### By video id and timestamp

Every entry carries a pointer of the form

    [<video-id> @ hh:mm:ss]

for example `[lvyyxkjwSCg @ 01:26:02]`. To jump into the recording, convert the
timestamp to seconds and append it as the `t` parameter:

    https://youtu.be/<video-id>?t=<seconds>

So `[lvyyxkjwSCg @ 01:26:02]` → `1*3600 + 26*60 + 2 = 5162` →
<https://youtu.be/lvyyxkjwSCg?t=5162>.

The same timestamps index the local transcripts: each caption block in
`refs/strominger-videos/<file>.md` is headed `**[hh:mm:ss]**`, so
`grep -n "01:26:02" refs/strominger-videos/01-lvyyxkjwSCg.md` lands on the
paragraph. Timestamps mark the *start* of the caption block containing the
remark; a sentence sometimes runs into the next block, and a few entries cite
two timestamps for that reason. Watching two or three blocks either side is
usually the fastest way to check a quote.

---

## 4. Caveats

### 4.1 ASR noise

All sixteen transcripts are auto-generated captions. Every digest ends with a
**Transcript quality notes** section listing that source's systematic
substitutions; consult it before trusting any name, number or symbol. Recurring
damage across the corpus: *scri* appears as "scry", "scribe", "sky", "Sprite",
"square plus"; *Liénard–Wiechert* as "Leonard Victor", "Leonard Beaker",
"Leonard and Vcart"; *Christodoulou* as "Chris sadulu", "Crystal dulu",
"Christ douer"; *non-abelian* as "not a billion"; *Kac–Moody* as "cat's Moody",
"katsmuti"; *symplectic* as "simplectic"; *soft photon* as "cell photon", "saw
photon"; *Goldstone boson* as "ghosts and bosons"; *Schwarzschild* as "short
Shield". Dates are mangled ("911" for 1991, "6D" for the 1960s).

Quality is uneven. The CSTQ colloquium has the best captions by a clear margin
(punctuation, capitalisation, mostly correct technical vocabulary); extra-04
(Strings 2017) is the worst, with no punctuation and heavy name damage.
Lecture 3's falloff argument around `00:22:34`–`00:24:41` is genuinely hard to
reconstruct from text and should be watched rather than read.

### 4.2 Inaudible audience questions

Blackboard and seminar recordings pick up the speaker, not the room. Several of
the most valuable entries are answers whose question survives only by
inference — lecture 5 `00:45:07`–`00:50:45`, lecture 10 `00:57:40`–`01:04:03`,
lecture 8's closing Q&A, and much of extra-01, where the captions merge
questioner and speaker without a break. Where a digest had to judge who was
talking, it says so in the entry. Board work is invisible throughout: equations
exist only as spoken words.

### 4.3 The verbatim-in-notes trap list

Three famous-sounding asides are **already in the written notes verbatim or
nearly so**. They read like off-script candour and are not. Cite the TeX, never
the video:

| aside | where it actually lives | video occurrence |
|---|---|---|
| "asymptotic symmetries is more of an art than a science" (with the joke that art may be better than science) | arXiv:1703.05448 §2.10, nearly word for word | `[swrNwD0ypaE @ 00:10:50]`. The *only* spoken delta is the extra clause "**and the rules keep changing**", which is not in the notes |
| "it would be incredibly surprising if after 90 years of QED we had found new relations — we have not; we have rediscovered known ones" | §2.8, verbatim. This is the single most useful calibration sentence in the corpus and it is a *written* sentence | lecture 2 |
| "a tricky point, which was incorrectly treated in some of the literature until recently" (care at the boundaries of scri) | §2.6, almost word for word | lecture 2, spoken as "a tricky point which a lot of people had gotten wrong in the past" |

Each per-source digest carries its own **"Checked and *not* a delta"** list of
the same kind. Read it before quoting anything that sounds quotable.

### 4.4 Unresolved attributions

- **extra-01 `[CdFyoaNv8GI @ 01:20:25]`** — he credits the symplectic-boundary-term
  result to "car and somebody … in the late 80s". *Crnkovic–Witten* is a
  plausible reading; the captions do not resolve it. **Unverified.**
- **extra-04 `[GpN8VAauyj8 @ 00:33:36]`** — two collaborator names come through as
  "honour Ilario" and "ben combats". The content matches
  Kapec–Raclariu–Strominger (arXiv:1607.07506). **Unverified.**
- **Lecture 9's speaker** — "Sasha", most likely Alexander Zhiboedov.
  **Unconfirmed.** See §2.
- **extra-01's questioner on causal diamonds and finite boxes** — plausibly Tom
  Banks (Strominger addresses a "Tom"). **Unconfirmed**, and the finite-region
  exchange is the most campaign-relevant material in the corpus, so the
  attribution matters if it is ever cited.
- **extra-03's questioner on Gross–Mende and worldsheet current algebra** —
  captions say "Karan"; content suggests Cumrun Vafa. **Unconfirmed.**
- **extra-05's questioner** — addressed as "Steve", plausibly Steve Shenker.
  **Unconfirmed.**
- **extra-01 `[CdFyoaNv8GI @ 00:45:04]` era attributions** and lecture 9's 1991
  non-linear-memory attribution are left blank or garbled by the captions.

### 4.5 Period matters

extra-03 (mid-2013) is the earliest recording and records positions the
programme later abandoned: no antipodal matching at all, scri-minus explicitly
set aside, "we don't have a Hilbert space at scri plus", and a deliberate
refusal to construct global charges. Do not read it as the mature view — read it
as evidence about how the mature view was reached. The digest flags each such
statement `EARLY PERIOD, LATER REVISED`.

---

## 5. Provenance

- Stage 1 (harvest): sixteen per-source digests, `lectures/`.
- Stage 2 (merge): this index, `topics/`, `campaign-hooks.md`.
- Transcripts: `refs/strominger-videos/`, fetched 2026-09-01.
- Written companion (the L3-citable source): arXiv:1703.05448,
  `refs/arxiv-1703.05448/soft_Arxiv_update.tex`.
- Tracking issue: `bd tns-t66`.
