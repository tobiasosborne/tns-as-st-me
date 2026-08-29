# Merge instructions for M-INDEX-LA-folium

## 1. `theory/memory-index.md`

Use the string anchor

`### ⟨1⟩3b. CONJECTURE M-INDEX-LA-folium (the surviving restricted candidate)`

and replace through the terminal sentence

`**Status: CONJECTURE.**  Claim row: \`claims/CLAIMS.md\` M-INDEX-LA-folium (live since 2026-08-28).`

with:

```markdown
### ⟨1⟩3b. THEOREM M-INDEX-LA-folium (fixed-kink implementer)

Let `ϱ_0=ϱ_x^{(g)}` be the fixed bare A2/D1(e′) kink, and let the selected
circle be common-unbroken, `h_θ∈H_α∩H_β`, with (S) at both tails and
D26(INT).  In the GNS representation of `ϱ_0`, the circle automorphisms are
implemented by a strongly continuous unitary group `U(θ)=e^{iθQ̂}` with
`e^{2πiQ̂}∈ℂ𝟙`; hence `Q̂` is pure point with spectrum in one coset of `ℤ`.

Proof: `theory/lanes/blitz-2026-08-29/la-folium/folium-implementer.md`
⟨1⟩1--⟨1⟩6.  Injectivity turns every nearby circle-rotated junction matrix
into a continuously varying local vector in the fixed kink GNS folium;
irreducibility then gives a locally `C¹` projective implementer, whose scalar
cocycle is removed explicitly on the one-dimensional parameter group.

This is the implementer route, not a strong-resolvent limit of
`Q̂_{W,c_0}`.  For nonscalar `V_θ`, ⟨1⟩12 still proves that those bare window
unitaries are not Cauchy; the compatibility is proved in the folium shard
⟨1⟩7.  The theorem covers the fixed bare A2 kink (and finite-core variants
whose padded blocked tensors span `M_χ(ℂ)`), not arbitrary D1(e′) finite-core
modifications.  **Status: PROVED-candidate pending the normal promotion gate.**
```

Also make these two anchored edits:

- In §9 item 2, replace the paragraph beginning
  `2. **Refuted:** the operator form of the requested L-A`
  and ending
  `its reach (L10).`
  with the same paragraph through the sentence ending
  `on the folium (⟨1⟩12).`, followed by:
  `The fixed-A2-folium implementer theorem is proved in ⟨1⟩3b by the separate implementer route, so the REFUTED row remains restricted to the sector-wide/window-limit statement (L10).`
- In §9 item 8, replace the exact anchored substring
  `M-INDEX-LA-folium is **CONJECTURE**; M-INDEX-LA-strong is **REFUTED**`
  with
  `M-INDEX-LA-folium is **PROVED-candidate** pending promotion; M-INDEX-LA-strong is **REFUTED**`.

## 2. `claims/CLAIMS.md`

Use the anchor `| M-INDEX-LA-folium |` and replace that entire table row with:

```markdown
| M-INDEX-LA-folium | Let `ϱ_0=ϱ_x^{(g)}` be the FIXED bare A2/D1(e′) kink with invertible junction `V_α(g)^{-1}`.  Let the selected circle be common-unbroken (`h_θ∈H_α∩H_β`), satisfy (S) at both tails, and obey D26(INT).  Then in the GNS representation of `ϱ_0` the circle automorphisms are implemented by a strongly continuous unitary group `U(θ)=e^{iθQ̂}`; D26 and irreducibility give `e^{2πiQ̂}∈ℂ𝟙`, hence `Q̂` is pure point with spectrum in one coset of `ℤ`.  This is a folium-equivalence/implementer theorem, NOT a strong-resolvent limit of window charges: for nonscalar `V_θ`, the bare window unitaries remain non-Cauchy by memory-index.md ⟨1⟩12.  Scope: the bare A2 kink, plus only those finite-core D1(e′) variants whose padded blocked tensors span `M_χ(ℂ)`; no assertion for arbitrary D1(e′) modifications. | **PROVED** (after the normal promotion gate) | A2, WI, D1(c,e′), D2(b,e), D26 | theory/lanes/blitz-2026-08-29/la-folium/folium-implementer.md ⟨1⟩1--⟨1⟩7 | exact finite-dimensional and functional-analytic proof; no numerical claim and no checker required |
```

Leave the adjacent `M-INDEX-LA-strong` row unchanged.

## 3. No other targets

No edit to `definitions.md` or `notation.md` is required; the proof imports all
symbols and hypotheses from their existing live entries.
