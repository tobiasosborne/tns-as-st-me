# Joint-critic verdict: `spt-tpm`

## Scope adjudicated

I checked the finite TPM support theorem, the fixed-window first-moment identity, the E-LR ordered limit, and the separation between generic charge arithmetic and SPT interpretation.  This lane introduces no checker; it cites the frozen M-INDEX donor arithmetic.  I reran `theory/checks/memory_index_check.py` green and `--red`: green exited 0 and all ten registered mutations were caught with exit 1.

## FATAL

None.

## MAJOR

None.

## minor

- `spt-tpm.md:414-418` says the “actual boundary-window memory outcomes” remain integral under the SPT corollary.  This is true, but their integrality is completely independent of the projective module.  Any merged prose must retain `spt-tpm.md:459-460` verbatim in substance: the TPM support theorem is generic circle-charge arithmetic and is not itself an SPT diagnostic.  Otherwise the replacement would misattribute D26 offset cancellation to topology.

## note

- `spt-tpm.md:121-168` correctly derives one affine coset for the same finite observable at both times and normalizes the sequential law without commuting the two spectral resolutions.  It never treats the spectrum of an operator difference as the TPM law.
- The sign chain is consistent: with `ν=q_-−q_+` and `m=-ν`, `spt-tpm.md:204-210` gives the dephased finite-time identity, E-LR2 yields `Σνp_L=ω^-_L(Q)-ω^+_L(Q)`, and reflection gives equation (E.8).
- `spt-tpm.md:249-284` uses LR1-GEN only for the common sequence and explicitly assumes E-LR2--E-LR3.  No AKLT relaxation, nonzero transition, channel inventory, or H-AD-edge implication is smuggled in.
- `spt-tpm.md:394-424` keeps D21(H-split)+`SPT-E'` separate: they identify a protected physical edge module/capacity but neither confine the full TPM law to the edge multiplet nor force a nonzero outcome.  The proposed `SPT-M'-ch` row properly preserves the old conditional channel theorem rather than deleting it.

**Adjudication: PROMOTE-к-PROVED for `SPT-M'-TPM-fin` and for `SPT-M'-TPM-spec` as an implication conditional on E-LR2--E-LR3; retain the former channel theorem separately as `SPT-M'-ch`.**
