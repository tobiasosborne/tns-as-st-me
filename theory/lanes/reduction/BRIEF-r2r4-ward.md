<!-- LANE BRIEF: R2+R4 — asymptotic-symmetry reduction and the edge
     correspondence. TJO directive 2026-08-30: physical arguments suffice;
     the lattice structures must specialize/reduce to the accepted continuum
     constructions, not merely resemble them. No marketing. Output:
     theory/lanes/reduction/r2r4-ward.md, written INCREMENTALLY. -->

# R2+R4: do the lattice asymptotic symmetry and the triangle edges reduce to the accepted continuum constructions?

## Inputs (read first)

- `theory/corner-a.md`, `theory/corner-a-kinks.md` — the PROVED corner-A
  statements (claim ids WI, A1, A2, G0): 𝒜_eff = G/N_α, the double-coset
  classification of vacuum pairs, bond implementers, the H²(G,U(1)) class,
  the lattice Noether pair.
- `refs/arxiv-1709.05018/draft1004.tex` (LOCAL TeX): the soft/hard charge
  split Q^soft + Q^hard and [Q,S] = 0 (L.356–414), and the demonstrated
  equivalence with the ordinary broken-current Ward–Takahashi identity via
  LSZ + soft limit (L.438–464) — the cleanest accepted A⇒C precedent.
- `refs/arxiv-1703.05448/soft_Arxiv_update.tex`: the canonical triangle
  logic (§1.1, L.308–341) and the QED derivation pattern.
- `refs/arxiv-2504.10577/Letter.tex`: soft theorem ⇔ Ward identity ⇔ SSB.
- `refs/arxiv-2201.01393/manuscript.tex` §4.1: the R^μ(p) regularity
  assumption flagged "does not automatically follow" (L.433–439).
- `refs/arxiv-1411.5745/memory_4.tex`: the falloff assumption (L.692–695).
- `docs/continuum-antecedents.md` for the digest with line numbers.
- `claims/CLAIMS.md` rows for the lattice hypothesis names you will map to:
  the proto-LSZ hypothesis (S-IDX-spec-struct-r2 row), local decay (AD3-ex,
  D18), local relaxation (D27/LR rows), ML3/ML4 regularity obligations.

## Tasks

1. **Dimensional specialization (R2).** The continuum asymptotic-symmetry
   construction assigns one charge per function on the celestial sphere. In
   1+1d the celestial sphere is S⁰ = two points, so the would-be continuum
   group is Maps(S⁰, G)/G_diag = (G_L×G_R)/G_diag. Work through this
   specialization at physics level and compare with the PROVED lattice
   corner A: where they coincide (finite-dimensionality is forced by d, not
   by the lattice), where the lattice statement is finer (𝒜_eff = G/N_α,
   the double coset in the broken case, the H² class), and — honestly —
   whether anything the continuum community counts as essential (one charge
   per angle, infinite tower) is simply ABSENT in 1d by geometry. Also state
   plainly: which parts of corner A are standard superselection-sector
   theory (DHR-style bookkeeping) and which are genuinely new statements.
2. **The soft/hard split (R2).** Identify, at physics level, the lattice
   decomposition of the modulated charge Q[f; ξ] into a soft part (k → 0
   Goldstone creation on the vacuum) and a hard part (action on hard legs),
   mirroring 1709.05018's Q^soft + Q^hard, and write the lattice analogue of
   [Q^soft + Q^hard, S] = 0 — stating exactly which PROVED lattice rows
   supply which piece and what remains conjectural (the proto-LSZ gap).
3. **The edge correspondence (R4).** Two-column table, stated as plain fact:
   each silent/assumed step of the accepted continuum derivations (R^μ
   regularity; the u → ±∞ falloff; hyperbolic-slice falloffs 1709.05018
   L.559–576; no surface terms) ↔ the corresponding NAMED lattice hypothesis
   (claim id, current status). Then show at physics level that the lattice
   edge derivations become the continuum ones in the limit: Ward + LSZ →
   soft factorization (the 1709.05018 L.438–464 pattern); soft → memory via
   Fourier residue (1411.5745). Where the lattice edge is conditional and
   the continuum edge is "accepted", say whether the continuum acceptance
   rests on the very assumption the lattice names — as an observation, not
   a boast.
4. **Verdict** for R2 and R4 separately: REDUCES CLEANLY / REDUCES WITH
   CAVEATS (list) / DOES NOT REDUCE (why, and what it means for the paper).

## Rules

- Physics register; continuum equations quoted from local TeX with
  file+line; lattice inputs by claim id, statuses unchanged.
- Flag unproved physical steps inline as [physical argument].
- Do NOT edit claims/CLAIMS.md, definitions.md, refs/LEDGER.md, or anything
  outside theory/lanes/reduction/. Do NOT close or claim any bd issue.
