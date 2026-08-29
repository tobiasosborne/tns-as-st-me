# Joint-critic verdict: `scope-g`

## Scope adjudicated

I checked `SG-CENTRE`, finite and ordered `SG-TORUS-TPM`, the Weyl-pair criterion, and the finite-group/semisimple exclusions against D2, D10, D13, D26, D27 and the cited claims.  I reran `scope_g_check.py` green and with `--red`; green exited 0, while the registered mutation exited 1 after independently firing both SG-C1 and SG-C2.

## FATAL

None.

## MAJOR

None.

## minor

- `compact-g-memory-scope.md:145-152` overattributes the affine joint charge torsor to `S-IDX-G-label`.  That claim concerns central-character sector shifts of represented charge/current components and explicitly gives a trivial label for a central component; it does not state the on-site joint charge spectrum used here.  The needed conclusion is nevertheless valid directly: the commuting primitive-circle generators in `compact-g-memory-scope.md:96-101` each obey D26(INT), so their joint spectrum lies in one affine coset of `ℤ^r`, and same-window TPM cancels that common offset.  Repair the citation, not the theorem.

## note

- `compact-g-memory-scope.md:41-75` is the standard invariant-functional argument: differentiating `Ad(H_α)` invariance annihilates `[𝔥_α,𝔥_α]`, while invariance under disconnected components restricts the representing vector to `Lie Z(H_α)^0` (possibly a proper subspace).  No semisimple density survives.
- `compact-g-memory-scope.md:104-110,178-219` does not silently strengthen scalar D27.  It explicitly assumes joint-PVM LR1, componentwise joint-dephasing LR2, and vector first-moment tightness; the text correctly says scalar D27 proves only marginals.
- `compact-g-memory-scope.md:319-324` quotients only the *tail-density jump* by scalar on-site directions.  It does not falsely claim that each individual vacuum density vanishes on the scalar kernel.
- SG-C2 uses different same-window joint eigenbases at the two times, exercises cross-time noncommutation, and the red background shift breaks the lattice gate; this is not a no-op gate.

**Adjudication: PROMOTE-к-PROVED for `M-SCOPE-center` and the finite `M-INDEX-torus` theorem, with the ordered formula remaining explicitly conditional on the displayed joint-D27 strengthening.**
