# Work order — 2+1 wave, lane W6: WHAT IS the 2+1 soft theorem? (bd tns-7pp; the wave's highest-value lane)

TJO's assessment of the 2+1 fusion-cat setting: asymptotic symmetries are
essentially understood (the fusion category / tube-algebra sector theory
IS that corner), memory should be tractable (superselection transplants),
and **the soft theorem is the corner with no good read**. Your job is
open-ended exploration: formulate candidate 2+1 soft theorems in the
fusion-categorical / topological setting, and kill or develop them. This
is a hunt (RESULT / PROGRAM / NOTHING NON-ARTIFICIAL header; negative →
no rounds), but the bar for PROGRAM is "the right OBJECT identified and
its first computation done" — in a corner with no good read, finding the
correct question is the result.

## THE 1D PLAYBOOK (transplant the LOGIC, not the formulas)

The campaign's winning inversion (PRD; HANDOFF): the soft law is a
symmetry CONSTRAINT on every limit point of a charge-created,
windowed/smeared protocol datum; scattering only supplies existence and
values. In 1D the charge-created datum was a magnon soft leg pinned to
the charge; in the 2+1 fusion-cat setting the charge-created object is a
STRING ENDPOINT with a fusion-channel datum (theory/cat-hunt.md RESULT —
read in full). So the transplanted question: what is the soft
deformation of a charge-created string, and what does symmetry force on
its limit points?

## CANDIDATE FORMULATIONS (develop or kill, add your own)

1. **Soft string modulation.** Deform the string operator by a slowly
   varying phase/tension modulation of wavelength 1/k; the soft limit is
   k→0. Does covariance + the fusion channel force an Adler-type zero /
   universal linear response of the endpoint amplitude? Toric code is
   exactly computable: string with modulated phase, endpoint pair
   amplitude, expand in k. If the leading term is forced by the sector
   datum alone, that IS a soft theorem.
2. **Edge soft modes.** For a phase with gapless edge (or a gapped edge
   chosen boundary condition), soft = long-wavelength edge excitation;
   the soft theorem would be the edge Ward identity constraining bulk
   string-endpoint amplitudes (bulk-boundary: the tube algebra acts on
   the edge). State the finite-lattice version; compute an instance on
   a thin cylinder (exactly, for toric code / Ising string-net).
3. **Gapped = trivial soft?** Adversarial candidate: in a fully gapped
   topological phase with gapped boundary there may be NO nontrivial
   soft limit — every response is O(k) with model-dependent
   coefficient, no universality. If true, prove a sharp finite version
   on toric code: the honest statement "the 2+1 soft theorem lives ONLY
   where something is gapless (SSB Goldstone, gapless edge, or
   deconfined gauge field)" would itself be the corner's map.
4. **2D SSB Goldstone route.** The direct transplant: 2D ferromagnet,
   two-magnon physics, but k is now a VECTOR — the 1D scalar slope
   cannot be the datum. Identify the correct 2D soft datum (angular
   average? the coefficient of |k|? a 1-form on the k-sphere?) and
   compute it exactly for the 2D spin-S ferromagnet two-magnon problem
   on a small patch (the 2D analogue of S2-2body's separated/adjacent
   equations). If a clean object exists here, the corner has a concrete
   anchor independent of topological order.
5. **Non-invertible soft.** If the symmetry is a genuine fusion category
   (non-invertible), the 1D Ward identity had no analogue (cat-hunt:
   the operator half is Lie). Is there a REPLACEMENT constraint at
   small k — e.g. from the pulling-through/defect commutation relations
   — that plays the Ward role in the soft limit? Even identifying the
   precise obstruction ("no local current ⟹ no soft factorization of
   type X, but constraint Y survives") maps the corner.

## FENCES

- cat-hunt ledger stands (no naive label subtraction; operator half is
  Lie — any soft constraint you find for non-invertible symmetry must
  not covertly assume a current zero mode).
- dh-hunt verdicts stand.
- Nothing here touches the 1D CLAIMS rows.
- L3: quotes from refs/ local TeX only. Mark SPECULATIVE sections.

## LANE (writable, NOTHING else)

- theory/soft-2d-hunt.md (CREATE)
- theory/checks/soft_2d_hunt_check.py (CREATE for any computed instance:
  green exit 0 under python3 -O, no bare asserts, ≥1 red mode)
- theory/soft-2d-hunt-notes.md (optional)

No edits to existing files; MERGE PROPOSALS only for RESULT. No commits.

## Deliverable

(0) header + the one-sentence best answer to "what is the 2+1 soft
theorem"; (1) formulation ledger with verdicts; (2) the best candidate
worked to a computation (toric code / thin cylinder / 2D two-magnon —
whatever your route needs); (3) checker if warranted; (4) MERGE
PROPOSALS if warranted. Write sections as you complete them.
