<!-- ROLE: order map + maintenance contract for the LaTeX labbook.
     TJO directive 2026-08-30. UPDATE POLICY: lockstep — see below. -->

# labbook/ — the campaign labbook (sharded LaTeX)

`labbook/main.tex` + `sections/NN_<slug>.tex` is the complete, readable,
self-contained record of every result of the campaign: all definitions
restated in full, every theorem/conjecture/refutation with a descriptive
human name, full hypotheses, honest status, and provenance. A reader needs
NO campaign acronyms: the dictionary shard glosses every identifier, and
body prose never relies on one.

- Style contract: `WRITING-GUIDE.md` (binding; read before editing any shard).
- Build: `cd labbook && make` → `main.pdf` (latexmk, pdflatex).
- Figures: `figures/make_figures.py` regenerates every plot from
  `numerics/results/*.json`; figures are committed as PDFs.
- Gate: `scripts/check-labbook.sh` — fails if any claim id or definition
  number is missing from the shards, or if a verbatim environment appears.

## Lockstep rule (may not go stale)

Any commit that

1. changes a status, adds, or rescopes a row in `claims/CLAIMS.md`,
2. adds or edits a definition in `definitions.md`, or
3. lands a new numerics result JSON

MUST update the owning shard (and the dictionary entry, and regenerate the
affected figure) **in the same commit**. Session close runs
`scripts/check-labbook.sh` alongside the git-push rule.

## Shard order (file → section label → owns)

| file | label | owns |
|---|---|---|
| `sections/00_overview.tex` | `sec:overview` | orientation, reading guide |
| `sections/01_dictionary.tex` | `sec:dictionary` | every campaign identifier |
| `sections/02_mps_setting.tex` | `sec:mps-setting` | D1, D5, D9, D11, D12 |
| `sections/03_symmetry_noether.tex` | `sec:symmetry-noether` | D2, D3, D4, D10 |
| `sections/04_corner_a.tex` | `sec:corner-a` | WI, A1, A2, G0, A2-orbit-r1, G0-soft-r1 |
| `sections/05_kink_model.tex` | `sec:kink-model` | D13–D18, K1–K4 |
| `sections/06_memory_quantization.tex` | `sec:memory-quantization` | M, M-flux, B3, M-quant, M-quant-G, Mq-E, Mq-AD3, M-tk, N2, Bc |
| `sections/07_memory_index.tex` | `sec:memory-index` | D26, D27, M-INDEX-fin/spec, M-IDX-density, M-INDEX-LA-folium/strong, LR1-GEN, M-SCOPE-center, M-INDEX-torus |
| `sections/08_local_relaxation.tex` | `sec:local-relaxation` | LR-D16-EDW/NR, M-ESC-NR, ACE-LD-*, LD-ID, AD3-ex, AC-EX, D28 |
| `sections/09_two_magnon.tex` | `sec:two-magnon` | D6–D8, ML2, S2, S2-2body(-S), OR1, OR2, N1 |
| `sections/10_wave_operators.tex` | `sec:wave-operators` | ML1(+D31-kernel), ML3, ML4(+A, Ward), ML6(+HS-SEP), AC-EX-2M(+D29), D31 |
| `sections/11_soft_index.tex` | `sec:soft-index` | S-IDX-* rows, proposed D29/D30 |
| `sections/12_universality.tex` | `sec:universality` | D24, D25, ML5(+A,B), D24-VAL, AMP, S-general |
| `sections/13_spt.tex` | `sec:spt` | D19–D23, SPT-* rows |
| `sections/14_two_plus_one.tex` | `sec:two-plus-one` | A-INDEX-TC-fin, M-INDEX-2D-fin/spec, A-INDEX-PEPS, SHAPE-FLAT |
| `sections/15_negative_results.tex` | `sec:negative-results` | refutation ledger; AMP obstruction, DH hunt, NO-CAT-SOFT |
| `sections/16_numerics.tex` | `sec:numerics` | numerics program, all figures |
| `sections/17_triangle_status.tex` | `sec:triangle-status` | edges, gap ledger, open problems |
