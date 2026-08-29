FAIL — 0 FATAL / 4 MAJOR / 1 MINOR

# Hostile critic: scalar PROTO-LSZ partial

## C1 — MAJOR — algebraic quotient is not yet an LSZ component

The header and several section labels call the exact quotient an “LSZ
factorisation.”  Since the proof itself correctly says that component
provenance is missing, this nomenclature risks smuggling in the very
identification withheld at (PL.1).  Repair every positive label to
“LSZ-shaped scalar factorisation” or “scalar scattering quotient.”

## C2 — MAJOR — packet norm and D29 probability pairing are conflated

⟨1⟩1.⟨2⟩2 says all integral equalities are in D24(b)'s product packet norm.
The D29 datum is a normalized probability-measure pairing.  The multiplier
is bounded on D24's packet space, but (PL.4) is a scalar pairing, not a norm
identity.  State the two registers separately.

## C3 — MAJOR — matching errors are not PROTO boundary gradients

⟨1⟩3.⟨2⟩5 lists “window errors” as vanishing by the MATCH proof.  That proof
controls its tail, collision, sampling, and readout errors, but does not
identify the two window-boundary-gradient components in (SPEC.5).  Replace
the sentence by “approximation errors internal to the matching theorem” and
explicitly deny an inference about `A^partial`.

## C4 — MAJOR — `(COMP-HS)` item 1 is stronger than needed

Requiring the independent descendant quotient to equal `L_S^sc` exactly
would force the remaining components to cancel exactly because (PL.4)
already exhausts the scalar total.  Full PROTO needs only an independent
uniformly `C^1` quotient with the same zero profile; its `O(k)` difference
from `L_S^sc` produces an allowed `O(epsilon^2)` scalar difference.  Weaken
the lemma and its consequence accordingly.

## C5 — MINOR — inaccurate fence pointer

⟨1⟩5.⟨2⟩4 calls the no-relabel rule “hard fence 3”; hard fence 3 is the
D29/D30 no-merge rule.  Cite the explicit exhaustiveness sentence following
(SPEC.5) instead.

## Verdict

The positive scalar identities are valid consequences of PROVED
`S-IDX-MATCH-HS-SEP` and `S2-2body-S`, and all four red mutations are live.
After C1--C5, the honest status remains PARTIAL and no full PROTO row is
promotable.

## Mechanical repair record

- C1 repaired: all positive headline language now says “LSZ-shaped”; D24's
  component name remains reserved.
- C2 repaired: the packet-multiplier and normalized-measure registers are
  stated separately.
- C3 repaired: MATCH approximation errors are explicitly not identified with
  `(PROTO-LSZ)` window-gradient components.
- C4 repaired: `(COMP-HS)` now asks only for the same zero profile and an
  `O(k)` quotient difference.
- C5 repaired: the proof cites the no-definitional-exhaustiveness sentence,
  not hard fence 3.

The orchestrator can verify these five text changes directly against
`proto-lsz.md`.  No second hostile round is requested by the capped process.
