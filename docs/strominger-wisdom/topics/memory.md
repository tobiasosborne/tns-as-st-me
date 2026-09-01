# memory

The third corner. Pointer convention `[id @ hh:mm:ss]` and all caveats:
[../INDEX.md](../INDEX.md). Entries marked *(guest)* are from lecture 9 and are
**not** Strominger — see the lecture-9 caution in the index.

---

## What memory is measured against

- **Memory is always a *change* relative to a calibration agreed in advance; without that agreement the question is not well posed** — the example given is that "what is the phase of this electron" has no answer unless something fixes the zero. `[8Aml1ToQtt4 @ 01:50:18]` — [L9 (guest)](../lectures/09-8Aml1ToQtt4-digest.md)
- **The same warning applied to an isolated black hole:** asking for "the supertranslation of *this* black hole" is answerable only against a pre-given asymptotic structure. `[8Aml1ToQtt4 @ 01:51:20]` — [L9 (guest)](../lectures/09-8Aml1ToQtt4-digest.md)
- **The detector is defined by a protocol, not a formula:** two bodies with clocks *synchronise first*, then the wave passes, then they re-measure by exchanging light signals — the calibration step is inside the definition of the measurement. `[8Aml1ToQtt4 @ 00:05:20]` — [L9 (guest)](../lectures/09-8Aml1ToQtt4-digest.md)
- **Fixing the vacuum frame is a one-time choice:** you may gauge-fix `C=0` on the initial slice, but the constraints then determine the supertranslation frame at every later time, so the initial calibration is the *only* free choice you get. `[8Aml1ToQtt4 @ 00:32:13]` — [L9 (guest)](../lectures/09-8Aml1ToQtt4-digest.md)
- **TENSION — Strominger locates the physical content in the phase space, not in the apparatus:** pressed on the detector, he says "you don't care about experimental device … the flat connections on the sphere at infinity are physical," which is a genuinely different place to put the content from the guest lecturer's calibrated-difference view. `[F42XbX45Dzw @ 01:02:06]` — [extra-05](../lectures/extra-05-F42XbX45Dzw-digest.md). Both digests flag the disagreement; it is developed in [campaign-hooks.md](../campaign-hooks.md#h1).

## Which observables earn the name

- **Higher soft moments are not memories** — only the `n=0` moment is a boundary quantity; the rest require the whole time history, which he calls unpleasant and disqualifying. `[8Aml1ToQtt4 @ 00:18:02]` — [L9 (guest)](../lectures/09-8Aml1ToQtt4-digest.md)
- **…and the second ground is a second calibration:** the higher moments depend on an arbitrary time origin `u₀`, so two experimenters would have to agree on `u₀` as well as on the observable. `[8Aml1ToQtt4 @ 00:34:22]` — [L9 (guest)](../lectures/09-8Aml1ToQtt4-digest.md)
- **TENSION — Strominger says the opposite:** every current in the tower "has an observable memory effect", with an algorithmic way to compute it at every order. `[6kH2pl_zvMA @ 00:51:49]` — [cstq](../lectures/cstq-6kH2pl_zvMA-digest.md). This is a direct cross-source disagreement about what counts as a memory; keep both.
- **Displacement memory is frame-robust; clock desynchronisation is not** — accelerated (BMS) and freely falling observers agree on the displacement, but only the accelerated ones see clocks drift. `[8Aml1ToQtt4 @ 01:11:34]` — [L9 (guest)](../lectures/09-8Aml1ToQtt4-digest.md)
- **"Supertranslation shifts `u`" must not be read as "memory is a clock shift"** — the physical content is the residual deformation on the sphere, and for geodesic observers there is no clock effect at all. `[8Aml1ToQtt4 @ 01:14:41]` — [L9 (guest)](../lectures/09-8Aml1ToQtt4-digest.md)
- **The desynchronisation is ordinary acceleration redshift in disguise**, once you compare Fermi normal with Fermi–Walker coordinates. `[8Aml1ToQtt4 @ 01:12:37]` — [L9 (guest)](../lectures/09-8Aml1ToQtt4-digest.md)
- **Memory is a diagnostic that scattering happened at all:** if every incoming momentum equals an outgoing one the memory vanishes identically, and any genuine rearrangement makes it generically non-zero. `[8Aml1ToQtt4 @ 00:27:54]` — [L9 (guest)](../lectures/09-8Aml1ToQtt4-digest.md)
- **A live self-correction on "cumulative":** challenged from the floor, he walks back "always the same sign" to the claim he actually means — the effect is proportional to the total energy flux. `[CdFyoaNv8GI @ 00:31:25]` — [extra-01](../lectures/extra-01-CdFyoaNv8GI-digest.md)

## Detectors: what they must be, what they cannot see

- **The signal has memory; the instrument does not** — a null result from a band-limited detector says nothing about whether the effect is there. `[8Aml1ToQtt4 @ 00:33:18]` — [L9 (guest)](../lectures/09-8Aml1ToQtt4-digest.md)
- **Why LIGO is blind to memory, mechanistically:** suspended mirrors impose a sensitivity band around 100 Hz and memory is a zero-frequency effect, so the published waveforms are already missing it by construction of the instrument. `[8Aml1ToQtt4 @ 00:12:45]` — [L9 (guest)](../lectures/09-8Aml1ToQtt4-digest.md)
- **Strominger makes the same separation more briefly:** memory is "a DC effect … *if they are inertial detectors*", distinct from the oscillating signal LIGO reported. `[wg-4Rm-kk70 @ 00:03:18]` — [extra-02](../lectures/extra-02-wg-4Rm-kk70-digest.md)
- **The "BMS detector" is an admitted fiction:** its elements sit at fixed `(z,z̄)` in a chosen Bondi frame, which requires acceleration — "each of the BMS detector carries a little rocket" — and he does not know how to build one. `[8Aml1ToQtt4 @ 00:46:04]` — [L9 (guest)](../lectures/09-8Aml1ToQtt4-digest.md)
- **Free-flying detectors are the natural home for a DC observable**, i.e. a space-based constellation. `[8Aml1ToQtt4 @ 00:13:48]` — [L9 (guest)](../lectures/09-8Aml1ToQtt4-digest.md)
- **Measuring electromagnetic memory is *harder* than gravitational**, because a phase is a quantum measurement while a displacement is something you watch. `[8Aml1ToQtt4 @ 01:50:18]` — [L9 (guest)](../lectures/09-8Aml1ToQtt4-digest.md); Strominger says the same and draws a historical moral from it at `[F42XbX45Dzw @ 01:01:02]` — [extra-05](../lectures/extra-05-F42XbX45Dzw-digest.md)
- **An operational protocol for electromagnetic memory:** align two charges' phases, separate them, let the large gauge transformation act, bring them back and interfere; his favourite version is a short Susskind note using SQUIDs connected by resistors. `[F42XbX45Dzw @ 01:01:02]` — [extra-05](../lectures/extra-05-F42XbX45Dzw-digest.md)
- **Detection optimism with a mechanism:** he expects gravitational memory to be measured, probably by pulsar timing arrays, because the `1/R` suppression is survivable when the flux is that large. `[CdFyoaNv8GI @ 00:30:22]` — [extra-01](../lectures/extra-01-CdFyoaNv8GI-digest.md); late-period status naming LIGO and pulsar timing arrays at `[6kH2pl_zvMA @ 00:21:00]` and `[6kH2pl_zvMA @ 00:30:30]` — [cstq](../lectures/cstq-6kH2pl_zvMA-digest.md)
- **Spin memory is out of reach for distant sources** — one extra power of `1/R` removes distant galaxies; he speculates about nearby sources and says he does not know. `[CdFyoaNv8GI @ 00:32:27]` — [extra-01](../lectures/extra-01-CdFyoaNv8GI-digest.md)
- **The practical obstruction to spin memory:** it is `O(1/R²)` against a leading `O(1/R)` contaminant, so the loop must be held in a BMS frame to a precision set by the larger effect. `[8Aml1ToQtt4 @ 01:42:53]` — [L9 (guest)](../lectures/09-8Aml1ToQtt4-digest.md)
- **The LHC as a spin-memory detector — the obstruction is the frame, not the clock:** counter-circulating proton beams are a pair of clocks, but "LHC is not a BMS observer, they haven't built it properly". `[8Aml1ToQtt4 @ 01:38:37]` — [L9 (guest)](../lectures/09-8Aml1ToQtt4-digest.md); Strominger independently reports the same hope and says it did not pan out at `[6kH2pl_zvMA @ 00:52:53]` — [cstq](../lectures/cstq-6kH2pl_zvMA-digest.md)
- **Open: would free-falling satellites see spin memory at all?** The spin-memory ring was built from BMS observers, LISA-like constellations follow geodesics, and he says the literature has not answered it. `[8Aml1ToQtt4 @ 01:37:36]` — [L9 (guest)](../lectures/09-8Aml1ToQtt4-digest.md)

## The memory ↔ soft-theorem dictionary

- **The dictionary is a semiclassical statement:** memory is an in-in expectation value, and it collapses to a ratio of amplitudes — hence to the soft factor — only when a single final state dominates. `[8Aml1ToQtt4 @ 00:54:40]` — [L9 (guest)](../lectures/09-8Aml1ToQtt4-digest.md)
- **Memory is *how you measure* a soft graviton, and that had been bothering him** — the objection "you cannot measure a zero-energy particle" is what the memory effect answers, and it is why he finds soft particles physical. `[CdFyoaNv8GI @ 00:34:36]` — [extra-01](../lectures/extra-01-CdFyoaNv8GI-digest.md)
- **…restated a year later with the mechanism:** the soft amplitude has a pole, the Fourier transform of a pole is a step function, and we observe in position space, not momentum space. `[F42XbX45Dzw @ 00:59:58]` — [extra-05](../lectures/extra-05-F42XbX45Dzw-digest.md)
- **IR divergences are the bookkeeping telling you the memory was ignored** — expand around Fock states that pretend no memory occurred and the loops punish you; no systematic cure is known. `[8Aml1ToQtt4 @ 01:00:04]` — [L9 (guest)](../lectures/09-8Aml1ToQtt4-digest.md)
- **The equivalence claim is meant at full strength:** three literatures were not analogous or related but "exactly the same thing". `[6kH2pl_zvMA @ 00:06:20]` — [cstq](../lectures/cstq-6kH2pl_zvMA-digest.md)
- **Radiation through null infinity is a domain wall between BMS-inequivalent vacua**, flat on either side, related by an explicit BMS transformation. `[CdFyoaNv8GI @ 01:01:17]` — [extra-01](../lectures/extra-01-CdFyoaNv8GI-digest.md)
- **The two corners share a Green's function:** the kernel inverting `D²(D²+2)` on the sphere for the supertranslating shock wave is the same one relating stress-energy flux to memory. `[H4IZ3jwTDp4 @ 01:22:40]` — [L10](../lectures/10-H4IZ3jwTDp4-digest.md)
- **"The geometry really remembers a lot"** — the delta-function reading of the charge is energy conservation at every angle, so the out-state remembers infinitely much about the in-state. `[Yx7PWgfC1dw @ 01:43:27]` — [L7](../lectures/07-Yx7PWgfC1dw-digest.md)
- **Energy going out to infinity *induces* a supertranslation** — the one-sentence version of memory, dropped three lectures before it is treated. `[Yx7PWgfC1dw @ 01:04:16]`, continuing `[Yx7PWgfC1dw @ 01:05:21]` — [L7](../lectures/07-Yx7PWgfC1dw-digest.md)

## Where the effect lives

- **The horse in the desert:** a horse galloping past your detector produces no memory, because the kernel vanishes at zero angular separation — the memory you see is dominated by enormous fluxes at large angles. `[8Aml1ToQtt4 @ 01:01:07]` (continues `01:02:09`) — [L9 (guest)](../lectures/09-8Aml1ToQtt4-digest.md)
- **The soft quantum, not the hard particles, redistributes energy around the sphere** — Bhabha scattering appears to move energy to new angles, and the emitted soft graviton is what restores the angle-by-angle balance. `[CdFyoaNv8GI @ 00:50:45]` — [extra-01](../lectures/extra-01-CdFyoaNv8GI-digest.md)
- **Soft gravitons can carry locally negative energy, but the contribution is a total derivative that integrates to zero on the sphere** — that is what "soft" means energetically. `[Yx7PWgfC1dw @ 01:46:33]` — [L7](../lectures/07-Yx7PWgfC1dw-digest.md)
- **Gravitational wave energy at null infinity is unambiguous, and LIGO is the proof** — it moved the mirrors. `[Yx7PWgfC1dw @ 00:54:26]` — [L7](../lectures/07-Yx7PWgfC1dw-digest.md)
- **The observability contrast that organises the whole corner:** electromagnetic large gauge action is on phases, so it needs quantum interference; the gravitational version is an angle-dependent shift of time itself, which has classical consequences. `[swrNwD0ypaE @ 00:06:37]` — [L3](../lectures/03-swrNwD0ypaE-digest.md); also at `[Yx7PWgfC1dw @ 01:02:09]` ("phases are slippery") and `[F42XbX45Dzw @ 01:01:02]`
- **In non-abelian gauge theory the same structure is classical**, because whether something is in a colour singlet is a classical question requiring parallel transport around the sphere — the seed of colour memory. `[OXl7IXT7_Cw @ 00:49:47]`, with the discomfort flagged early at `[OXl7IXT7_Cw @ 00:17:06]` — [L6](../lectures/06-OXl7IXT7_Cw-digest.md)
- **"Untethered":** the angles at null infinity are not tied to one another, which makes vacuum change cheap and the problem behave like 1+1 dimensions. `[WxCY-K-Jb4A @ 00:52:52]`, also `[WxCY-K-Jb4A @ 00:41:44]` — [L5](../lectures/05-WxCY-K-Jb4A-digest.md)
- **The extra integration function `C|_{scri⁺₋}` is "the point that everybody would have missed"** — specifying the news is not enough, and the missing datum is exactly where the vacuum label lives. `[Yx7PWgfC1dw @ 01:08:32]` — [L7](../lectures/07-Yx7PWgfC1dw-digest.md)

## History and naming

- **The two literatures were separated by nothing but notation** — "Weinberg was scattering particles, Braginsky and Thorne were scattering stars" — and the similarity was missed for three or four decades. `[CdFyoaNv8GI @ 00:27:09]`, with the "hard to miss" remark at `[CdFyoaNv8GI @ 00:25:01]` — [extra-01](../lectures/extra-01-CdFyoaNv8GI-digest.md)
- **Universality is why neither side could see the other:** the soft factor does not care whether the emitter is massive or massless, a graviton or a star. `[8Aml1ToQtt4 @ 00:57:55]` — [L9 (guest)](../lectures/09-8Aml1ToQtt4-digest.md)
- **The linear/non-linear split is an artefact of which community you came from** — it has no counterpart on the amplitudes side, where the soft factor is blind to what the external legs are. `[8Aml1ToQtt4 @ 00:45:04]`, with the mild dislike of the terminology stated at `[8Aml1ToQtt4 @ 00:25:44]` — [L9 (guest)](../lectures/09-8Aml1ToQtt4-digest.md)
- **How the effect got its name:** "Christodoulou in 1991, who as the last person to write an important paper on the subject got his name attached to it". `[CdFyoaNv8GI @ 00:14:15]` — [extra-01](../lectures/extra-01-CdFyoaNv8GI-digest.md)
- **Forty years of memory literature sit behind the gravitational side**, which is why the gauge-theory phase story took so long to be recognised as the same thing. `[Yx7PWgfC1dw @ 01:06:26]` — [L7](../lectures/07-Yx7PWgfC1dw-digest.md)
- **Mild surprise that electromagnetism had an undiscovered memory effect**, with a refusal to make much of it. `[8Aml1ToQtt4 @ 01:15:44]` — [L9 (guest)](../lectures/09-8Aml1ToQtt4-digest.md)
- **He calls the ordering bizarre:** gravity got there ahead of Maxwell theory, which is not how these things normally go. `[F42XbX45Dzw @ 00:35:28]` — [extra-05](../lectures/extra-05-F42XbX45Dzw-digest.md)
- **Christodoulou–Klainerman's `|u|^{-3/2}` news falloff is what made `C` well defined at the edges of scri — "which was crucial"**, and he is specific that this, not the global existence theorem, is the part that mattered for him. `[Yx7PWgfC1dw @ 01:30:33]` — [L7](../lectures/07-Yx7PWgfC1dw-digest.md)
