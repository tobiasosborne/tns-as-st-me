# Joint-critic verdict: `la-folium`

## Scope adjudicated

I checked the finite-block realization, purity, spatial implementation, removal of the one-parameter projective cocycle, Stone generator, and scalar-period spectral conclusion.  The theorem is non-numerical and claims no checker; none is required for its finite-dimensional and functional-analytic steps.

## FATAL

None.

## MAJOR

None.

## minor

- `folium-implementer.md:116-129` gives the correct junction transform for the stated ket-action convention, `M_θ=V_α(h_θ)M V_β(h_θ)^{-1}`, but then parenthetically permits an inverse convention without spelling out the corresponding state action.  The merge should keep one convention fixed rather than retain that hedge; continuity/invertibility, and hence the theorem, are unaffected.

## note

- `folium-implementer.md:50-103` has the needed rank argument.  Injective left and right blocked words make `{L_aMR_b}` span `M_χ`; the physical operator's output rows are independent, so the block map is onto and a continuous right inverse realizes every nearby junction exactly as a local GNS vector.
- `folium-implementer.md:155-183` validly proves purity: the fixed bare A2 kink is the pure vacuum composed with the half-chain on-site automorphism.  This is why implementers are unique modulo scalars and every nonzero vector is cyclic.
- `folium-implementer.md:249-304` does not merely assert that a projective representation of `ℝ` lifts.  It differentiates the local cocycle, writes it as a coboundary, rephases, and extends the honest local group by subdivision.
- `folium-implementer.md:325-342` uses D26 only to make the `2π` adjoint automorphism trivial.  Irreducibility makes its implementer scalar; spectral calculus then forces a pure-point integer coset.
- `folium-implementer.md:348-391` correctly separates existence of an abstract implementer from convergence of the bare window unitaries.  It does not revive the REFUTED sector-wide/window-limit claim.

**Adjudication: PROMOTE-к-PROVED for the fixed-bare-kink `M-INDEX-LA-folium` row at the stated common-unbroken/full-block-span scope.**
