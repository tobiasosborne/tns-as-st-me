# pitfalls

Confusions he corrects, including his own. Pointer convention
`[id @ hh:mm:ss]` and all caveats: [../INDEX.md](../INDEX.md). Entries marked
*(guest)* are from lecture 9 and are **not** Strominger.

---

## Wrong pictures

- **The Faddeev–Kulish cloud does not travel with the particle.** Photons reach null infinity, massive charges reach timelike infinity; the cloud disperses, and its function is to satisfy a long-distance constraint. `[GpN8VAauyj8 @ 00:16:06]` — [extra-04](../lectures/extra-04-GpN8VAauyj8-digest.md)
- **"Supertranslation shifts `u`" is not "memory is a clock shift"** — for geodesic observers there is no clock effect at all. `[8Aml1ToQtt4 @ 01:14:41]` — [L9 (guest)](../lectures/09-8Aml1ToQtt4-digest.md)
- **You cannot perform a supertranslation "at `u=6`"** — a `u`-dependent shift is not a supertranslation. `[Yx7PWgfC1dw @ 01:04:16]` — [L7](../lectures/07-Yx7PWgfC1dw-digest.md)
- **Boundary conditions at scri are not like boundary conditions in a box, and the box intuition actively misleads** — scri is not a reflecting wall; radiation boils off and leaves, so you must know what behaviour to expect rather than choose it. `[OXl7IXT7_Cw @ 01:10:06]`, `[OXl7IXT7_Cw @ 01:11:14]` — [L6](../lectures/06-OXl7IXT7_Cw-digest.md)
- **The "soft factor is a number times the same amplitude" intuition is a special case that will mislead you** in the non-abelian, photino and subleading settings alike. `[OXl7IXT7_Cw @ 00:06:26]` — [L6](../lectures/06-OXl7IXT7_Cw-digest.md)
- **A student's tunnelling analogy corrected: these are transitions in *space* along the slice defining the Hilbert space, not in time.** `[WxCY-K-Jb4A @ 00:46:14]` — [L5](../lectures/05-WxCY-K-Jb4A-digest.md)
- **"Hair" means only a distinguishing feature — not structure sitting near the horizon.** `[wg-4Rm-kk70 @ 00:17:15]` — [extra-02](../lectures/extra-02-wg-4Rm-kk70-digest.md)
- **Supertranslation charges cannot label the degenerate vacua**, because the group is abelian and they all vanish. `[CdFyoaNv8GI @ 01:12:01]` — [extra-01](../lectures/extra-01-CdFyoaNv8GI-digest.md)
- **A null result from a band-limited detector says nothing about whether the effect is there: "the signal has memory, the detector does not".** `[8Aml1ToQtt4 @ 00:33:18]` — [L9 (guest)](../lectures/09-8Aml1ToQtt4-digest.md)
- **The BMS detector is not freely falling** — each element carries a rocket, and he does not know how to build one. `[8Aml1ToQtt4 @ 00:46:04]` — [L9 (guest)](../lectures/09-8Aml1ToQtt4-digest.md)
- **A horse galloping past your detector produces no memory** — the kernel vanishes at zero angular separation. `[8Aml1ToQtt4 @ 01:01:07]` — [L9 (guest)](../lectures/09-8Aml1ToQtt4-digest.md)

## Silent assumptions and hidden bases

- **The `U=1` flat-connection assumption is one textbooks make silently** — and it is already uncomfortable, because soft gluons move you between inequivalent flat connections. `[OXl7IXT7_Cw @ 00:16:02]`, `[OXl7IXT7_Cw @ 00:17:06]` — [L6](../lectures/06-OXl7IXT7_Cw-digest.md)
- **The antipodal matching condition is implicit in Feynman propagators**, which is how fifty years of gauge theory got away without stating it. `[OXl7IXT7_Cw @ 00:52:56]` — [L6](../lectures/06-OXl7IXT7_Cw-digest.md)
- **The standard energy-eigenmode basis hides the non-decaying solutions of the massless wave equation** — exactly the ones the large gauge parameter needs. "You miss it when you go to energy eigenmodes." `[xZ2FG1kLb9I @ 00:40:52]` — [L4](../lectures/04-xZ2FG1kLb9I-digest.md)
- **The standard slogan "physical states are invariant under all gauge transformations" holds only for transformations trivial at infinity.** `[yeMZKViadhw @ 01:14:42]` — [L2](../lectures/02-yeMZKViadhw-digest.md)
- **The extra integration function `C|_{scri⁺₋}` is "the point that everybody would have missed"** — the free data are not just the radiative field. `[Yx7PWgfC1dw @ 01:08:32]` — [L7](../lectures/07-Yx7PWgfC1dw-digest.md)
- **A vanishing charge does not reliably mean the transformation is trivial**, so the standard test for the "allowed/trivial" quotient can fail. `[swrNwD0ypaE @ 00:13:01]` — [L3](../lectures/03-swrNwD0ypaE-digest.md)
- **"No corrections" always silently means "no corrections in perturbation theory".** `[xZ2FG1kLb9I @ 01:10:33]` — [L4](../lectures/04-xZ2FG1kLb9I-digest.md)
- **The memory/soft-factor dictionary quietly assumes a dominant final state** — the quantum object is an in-in expectation value. `[8Aml1ToQtt4 @ 00:54:40]` — [L9 (guest)](../lectures/09-8Aml1ToQtt4-digest.md)
- **The soft limit needs non-exceptional momenta** — raised from the floor, and he had not heard it before. `[CdFyoaNv8GI @ 00:10:02]` — [extra-01](../lectures/extra-01-CdFyoaNv8GI-digest.md)
- **Higher soft moments carry an origin-of-time ambiguity that has to be agreed separately.** `[8Aml1ToQtt4 @ 00:34:22]` — [L9 (guest)](../lectures/09-8Aml1ToQtt4-digest.md)

## Recurring technical traps

- **The linear-in-`u` divergence of subleading data is "ubiquitous"**, first met in problem set 1, again in the photino charge, again in the superrotation charge — and each time a delicate projection is needed. `[60U7_P2XJlQ @ 00:59:29]`, `[WxCY-K-Jb4A @ 01:42:17]`
- **The obvious guess for the photino charge "seems like it would be so easy that I could do it in the next five minutes" — and there is a wrinkle.** `[WxCY-K-Jb4A @ 01:41:13]`, `[WxCY-K-Jb4A @ 01:43:19]` — [L5](../lectures/05-WxCY-K-Jb4A-digest.md)
- **`A_z` is not hermitian — roughly `a_x + i a_y` — so the conjugate creates the opposite helicity at the same point.** A live slip and correction. `[yeMZKViadhw @ 01:55:46]` — [L2](../lectures/02-yeMZKViadhw-digest.md)
- **The factor of `i` between `F_{z̄z}` and the magnetic field comes from index ordering under complex conjugation — "I'll always get confused by that".** `[xZ2FG1kLb9I @ 01:36:50]` — [L4](../lectures/04-xZ2FG1kLb9I-digest.md)
- **A notation drift mid-lecture:** he drops the in/out superscripts and adopts the all-outgoing convention in which incoming particles carry negated charge, cheerfully rather than carefully. `[xZ2FG1kLb9I @ 00:06:33]`, `[xZ2FG1kLb9I @ 00:05:32]` — [L4](../lectures/04-xZ2FG1kLb9I-digest.md)
- **His charge normalisation (integers) is awkward for the field-theory conventions used later.** `[yeMZKViadhw @ 01:13:38]` — [L2](../lectures/02-yeMZKViadhw-digest.md)
- **The `4/3` and `C²` shift in the angular momentum aspect are convenience, not physics — and conventions differ across the literature.** `[60U7_P2XJlQ @ 00:03:09]` — [L8](../lectures/08-60U7_P2XJlQ-digest.md)
- **Massive fields do not simply decay exponentially at null infinity — they "do really surprising weird counter-intuitive things".** A self-correction. `[lvyyxkjwSCg @ 01:42:39]` — [L1](../lectures/01-lvyyxkjwSCg-digest.md)
- **A live sign puzzle he cannot explain: why `C` transforms with `−2D_z²f` on scri⁺ and `+2D_z²f` on scri⁻.** `[Yx7PWgfC1dw @ 01:15:19]` — [L7](../lectures/07-Yx7PWgfC1dw-digest.md)
- **A live boost-charge fumble, abandoned rather than patched — do not take that line as correct.** `[60U7_P2XJlQ @ 01:02:40]` — [L8](../lectures/08-60U7_P2XJlQ-digest.md)
- **The falloff derivation from finite energy flux is partly improvised and completed from the floor.** `[swrNwD0ypaE @ 00:22:34]` — [L3](../lectures/03-swrNwD0ypaE-digest.md)
- **Only phase *differences* were ever measurable in gauge theory** — "it wasn't really meaningful to say that the phase at this point is this". `[Yx7PWgfC1dw @ 01:05:21]` — [L7](../lectures/07-Yx7PWgfC1dw-digest.md)

## Terminology that has caused real confusion

- **Calling the whole field the Goldstone boson, rather than just the zero mode, "caused a lot of confusion".** `[WxCY-K-Jb4A @ 00:28:53]`, `[WxCY-K-Jb4A @ 00:35:26]` — [L5](../lectures/05-WxCY-K-Jb4A-digest.md); hedged again at `[F42XbX45Dzw @ 01:10:31]`; and dissented from outright at `[8Aml1ToQtt4 @ 01:43:55]` — [L9 (guest)](../lectures/09-8Aml1ToQtt4-digest.md)
- **"Asymptotic" suggests approximate, and these symmetries are exact** — a complaint he makes in at least four talks. `[lvyyxkjwSCg @ 00:01:06]`, `[wg-4Rm-kk70 @ 00:02:14]`, `[F42XbX45Dzw @ 00:04:54]`, `[WxCY-K-Jb4A @ 00:18:08]`
- **The linear/non-linear memory terminology is disliked and used only because the literature does.** `[8Aml1ToQtt4 @ 00:25:44]` — [L9 (guest)](../lectures/09-8Aml1ToQtt4-digest.md)
- **He abuses "Bondi mass" for "Bondi mass aspect" out of impatience, and warns you.** `[Yx7PWgfC1dw @ 00:06:30]` — [L7](../lectures/07-Yx7PWgfC1dw-digest.md)
- **The no-hair theorem is correct; its physical interpretation was not.** `[F42XbX45Dzw @ 00:36:29]` — [extra-05](../lectures/extra-05-F42XbX45Dzw-digest.md)
- **"The S-matrix doesn't exist in non-abelian gauge theory" is, in his view, the wrong phrasing** — nobody has constructed it, and nobody tried to prove impossibility. `[OXl7IXT7_Cw @ 00:53:59]` — [L6](../lectures/06-OXl7IXT7_Cw-digest.md)
- **The word "soft" in "soft photons are the Goldstone bosons" is optional — "it's a free world".** `[WxCY-K-Jb4A @ 00:34:24]` — [L5](../lectures/05-WxCY-K-Jb4A-digest.md)

## The verbatim-in-notes trap

Three famous-sounding asides are already in the written notes and must be cited
from the TeX, not from the video: the art/science line (§2.10), the "90 years of
QED … we have rediscovered known ones" calibration (§2.8), and "a tricky point,
incorrectly treated in some of the literature" (§2.6). Full table and pointers:
[../INDEX.md §4.3](../INDEX.md#43-the-verbatim-in-notes-trap-list). Each digest
carries its own **"Checked and *not* a delta"** list of the same kind.
