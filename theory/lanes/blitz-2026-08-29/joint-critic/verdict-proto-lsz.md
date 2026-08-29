# Joint-critic verdict: `proto-lsz`

## Scope adjudicated

The promoted object is only proposed row `S-IDX-PROTO-SCALAR-HS-SEP`, not full `(PROTO-LSZ)` or `S-IDX-spec-struct-r2`.  I recomputed the removable quotient from `S2-2body-S` (T.2)--(T.4), checked the use of `S-IDX-MATCH-HS-SEP`, and reran the green checker plus all four registered red modes under `python3 -O`.  Green exited 0; `--red-profile`, `--red-ward-factor`, `--red-slope`, and `--red-split` each exited 1.

## FATAL

None.

## MAJOR

None.

## minor

- `proto_lsz_check.py:68-81` does not numerically certify the advertised *uniform `C^1` extension*: it samples only three nonzero soft momenta and bounds the zeroth-order difference quotient by the very loose constant 25.  This does not break `proto-lsz.md:73-101`, because that step proves uniform `C^1` analytically from the regular rational multiplier on a compact rectangle.  The checker must continue to be described as corroboration, not proof of regularity.

## note

- `proto-lsz.md:118-169` is logically a corollary, not a new component theorem: (PL.4) follows exactly by substituting the definition of `L_S^sc` into the already-PROVED same-measure equality.  The shard states that limitation accurately.
- `proto-lsz.md:222-334` correctly identifies the residual obstruction as independently defining and controlling the descendant, complementary-current, direct-contact, and window-gradient terms.  It does not smuggle aggregate scalar matching into component provenance.

**Adjudication: PROMOTE-к-PROVED for `S-IDX-PROTO-SCALAR-HS-SEP`; full `(PROTO-LSZ)` remains SKETCH/open at `(COMP-HS)`.**
