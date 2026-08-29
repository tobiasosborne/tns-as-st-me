# Merge proposal (anchored edits only)

## Target: `claims/CLAIMS.md`

Anchor on the complete row beginning:

`| LR-D16-EDW | In D16, in the two-site basis`

Insert immediately after that row:

`| D51-U | For D16 let P be the <=3-domain-wall projection and Q the >=5-wall projection in the odd kink sector.  For every full-H packet Psi spectrally supported in I=[c-w,c+w] with c<(5J/2)(Delta-1), sup_t ||Q exp(-itH)Psi|| <= min{1,(w+3J/2)/[(5J/2)(Delta-1)-c]}.  Conditional on Mq-E and Delta>5/2, on the projected Fano band this gives probability at most min{1,[(5/2)/(Delta-5/2)]^2}=O(Delta^-2).  Below the five-wall threshold the Feshbach self-energy obeys ||Sigma(z)||<=9J^2/[4(a_5-Re z)] and ||partial_z Sigma(z)||<=9J^2/[4(a_5-Re z)^2].  This is uniform wall leakage for an already full-H-energy-filtered packet, not preparation from a projected packet, local decay, channel exclusion, wave-operator completeness, or D18. | SKETCH | D16, LR-D16-EDW, Mq-E (Fano specialisation only) | theory/lanes/blitz-2026-08-29/d51-lift/D51-LIFT.md | d51_check.py verifies the 3/5-wall degree constant; --red exits 1; no finite checker tests the spectral theorem |`

## Target: `theory/memory-quantization.md`

Anchor on the paragraph ending with:

`A small Frobenius norm at finite N, or a finite-time leakage probability, does not supply that estimate.`

Insert after that paragraph:

`A partial uniform estimate is supplied by lane result D51-U: for a full-H packet already spectrally localised to I=[c-w,c+w] with c below the five-wall compression floor, the >=5-wall probability is bounded for every scattering time by min{1,[(w+3J/2)/((5J/2)(Delta-1)-c)]^2}; on the Mq-E Fano band this is O(Delta^-2) for large Delta.  The estimate does not prepare that full-H spectral packet from a projected packet and does not prove D18.  The exact remaining attack is the weighted Feshbach limiting-absorption estimate (D51-M) together with exclusion or inventory of the other on-shell <=3-wall components; see theory/lanes/blitz-2026-08-29/d51-lift/D51-LIFT.md.`

No definition or notation file edit is proposed: the proof uses only temporary
block labels and the existing `P_3`, `H_3`, `N_DW` notation.
