<!-- ROLE: L3 ground-truth ledger. Every fetched source, its verified title, and
     its role. A quote in theory/ or paper/ must trace to a file under refs/. -->

# Reference ledger

Fetched 2026-08-25 from https://arxiv.org/e-print/<id> (TeX source layer).
Title verification: extracted from the TeX itself, compared to the brief's
description. All 12/12 fetched OK; no id mismatches.

| arXiv id | verified title | main tex | role |
|---|---|---|---|
| 0802.0447 | String order and symmetries in quantum spin lattices | StringOrder-v10.tex | intertwiner (IT), fundamental thm of MPS symmetries |
| 1103.2286 | Variational matrix product ansatz for dispersion relations | dispersionrelation_final.tex | excitation ansatz (brief cited it as "Haegeman et al." — this is the original ansatz paper, incl. TJO) |
| 1305.2176 | Elementary excitations in gapped quantum spin systems | (single tex) | STYLE TARGET (PRL 111, 080401) + rigorous quasiparticle context |
| 1312.6793 | S matrix from matrix product states | (single tex) | MPS S-matrix method (PRL 112, 257202) |
| 1506.01008 | Scattering particles in quantum spin chains | (tarball) | MPS S-matrix long version (PRB 92, 125136) |
| 1703.05448 | Lectures on the Infrared Structure of Gravity and Gauge Theory | soft_Arxiv_update.tex | continuum triangle (orientation only) |
| 1703.07885 | Can scalars have asymptotic symmetries? | (single tex) | Campiglia–Coito–Mizera: global-symmetry/scalar soft ↔ asymptotic charges |
| 1810.07006 | Tangent-space methods for uniform matrix product states | (tarball) | tangent-space/excitation-ansatz review |
| 1907.02474 | Real-time scattering of interacting quasiparticles in quantum spin chains | (tarball incl. supplement) | wavepacket scattering methodology |
| 2011.12127 | Matrix Product States and Projected Entangled Pair States: Concepts, Symmetries, Theorems | (tarball) | MPS review; symmetries/fund. thm |
| 2012.07243 | Collisions of false-vacuum bubble walls in a quantum spin chain | (tarball) | kink-collision MPS methodology (PRX Quantum 3, 020316) |
| 2504.10577 | Soft Theorems and Spontaneous Symmetry Breaking | (single tex) | Adler zeros / soft theorems for broken symmetries (continuum) |

## Batch 2 — sweep-surfaced must-cites (fetched 2026-08-25, 24/24 OK, titles verified)

| arXiv id | verified title | role |
|---|---|---|
| 1709.05018 | Soft pion theorem, asymptotic symmetry and new memory effect | THE direct continuum antecedent (Hamada–Sugishita) |
| 1411.5745 | Gravitational Memory, BMS Supertranslations and Soft Theorems | canonical memory↔soft edge (Strominger–Zhiboedov) |
| 2310.16683 | Fracton infrared triangle | first triangle beyond Lorentz (competitive landscape) |
| 2203.02817 | Asymptotic symmetries and soft charges of fractons | precursor to fracton triangle |
| 2203.14334 | Infrared Finite Scattering Theory in Quantum Field Theory and Quantum Gravity | rigour counterpoint (Prabhu–Satishchandran–Wald) |
| 2412.01910 | Gravitational memory and soft theorems: The local perspective | local (no null infinity) derivation — closest continuum template |
| 2107.05401 | Spin wave driven domain wall motion in easy-plane ferromagnets: a particle perspective | closest phenomenological precedent for corner B (Lan–Xiao) |
| 1406.6051 | Propulsion of a domain wall in an antiferromagnet by magnons | adjacent (steady-state driving, not memory) |
| 1712.06578 | Magnon-induced non-Markovian friction of a domain wall in a ferromagnet | adjacent (friction observable) |
| 2306.15351 | Domain wall dynamics in classical spin chains: free propagation, subdiffusive spreading, and soliton emission | background |
| 2108.03189 | On-Shell Recursion Relations for Nonrelativistic Effective Field Theories | continuum type-B Adler zeros (Mojahed–Brauner) |
| 2201.01393 | Nonrelativistic effective field theories with enhanced symmetries and soft behavior | ditto |
| 2008.12078 | Exceptional nonrelativistic effective field theories with enhanced symmetries | ditto |
| 2301.11363 | Soft Phonon Theorems | closest published condensed-matter Goldstone soft theorem |
| 1910.04766 | New Soft Theorems for Goldstone Boson Amplitudes | template if lattice soft limit is corrected, not vanishing |
| 1509.07840 | Soft theorems from anomalous symmetries | anomaly-modified soft limits (continuum) |
| 1602.08692 | Effective field theory and the scattering process for magnons in the ferromagnet, antiferromagnet, and ferrimagnet | magnon EFT, vanishing FM scattering length |
| 1412.5604 | Matrix product operators for symmetry-protected topological phases: Gauging and edge theories | core corner-A prior machinery (Williamson et al.) |
| 2203.12563 | Classifying phases protected by matrix product operator symmetries using matrix product states | MPO-symmetry classification |
| 2405.00439 | Fractional domain wall statistics in spin chains with anomalous symmetries | closest MPS treatment of domain walls + anomaly |
| 2403.04835 | Non-Invertible Symmetries, Anomalies and Scattering Amplitudes | anomaly constrains S-matrix (crossing, 1+1d) |
| 1804.10122 | Fermionic Lieb-Schultz-Mattis Theorems and Weak Symmetry-Protected Phases | LSM-as-anomaly cluster |
| 1907.08204 | Topological theory of Lieb-Schultz-Mattis theorems in quantum spin systems | LSM-as-anomaly cluster |
| 2310.10078 | Gravitational wave analogues in spin nematics and cold atoms | nearest platform claim (spin-2 analogue in a magnet) |

## Batch 3 (fetched 2026-08-25)

| arXiv id | verified title | role |
|---|---|---|
| 1203.0609 | Unified Description of Nambu--Goldstone Bosons without Lorentz Invariance | type-A/type-B counting (Watanabe–Murayama) |

Still non-local (paywalled; TIB VPN via TJO if they become load-bearing):
Dyson, Phys. Rev. 102, 1217 (1956); Nielsen–Chadha, Nucl. Phys. B 105, 445 (1976).

## Prose exemplars

Fetched 2026-08-25 per TJO directive; stored in `refs/prose-exemplars/`. Not
physics sources — the extraction base for `docs/prose-guide.md`. Identity below
verified from each file's own header/masthead text (PDFs via `pdftotext`),
5/5 OK. The three scanned PDFs carry OCR damage (split words `i s`, `h a s`;
inline footnote digits); quotes in the prose guide repair that damage only.

| file | verified identity (from the file's own text) | role |
|---|---|---|
| `prose-exemplars/watson-crick-1953.pdf` | masthead "No. 4356 April 25, 1953 NATURE 737"; "MOLECULAR STRUCTURE OF NUCLEIC ACIDS / A Structure for Deoxyribose Nucleic Acid"; signed J. D. WATSON, F. H. C. CRICK, Cavendish Laboratory | prose exemplar: understatement as authority; novelty claimed once; ~1100 words |
| `prose-exemplars/einstein-1905-specrel-en.pdf` | "ON THE ELECTRODYNAMICS OF MOVING BODIES / By A. EINSTEIN / June 30, 1905"; colophon: fourmilab ed. (J. Walker) of the 1923 Methuen English translation of *Zur Elektrodynamik bewegter Körper*, Ann. Phys. 17:891 (1905) | prose exemplar: audacious result entered through humble observation; operational definitions |
| `prose-exemplars/shannon-1948.pdf` | "Reprinted with corrections from The Bell System Technical Journal, Vol. 27, pp. 379–423, 623–656, July, October, 1948"; "A Mathematical Theory of Communication / By C. E. SHANNON" | prose exemplar: new field opened in plain declaratives; elementary examples before generality; proofs in appendices |
| `prose-exemplars/bell-1964.pdf` | "Physics Vol. 1, No. 3, pp. 195—200, 1964"; "ON THE EINSTEIN PODOLSKY ROSEN PARADOX / J. S. BELL", Univ. of Wisconsin, received 4 November 1964 | prose exemplar: stakes in one page; minimal apparatus; candour about what is easy vs hard |
| `prose-exemplars/darwin-origin.txt` | Gutenberg header "Title: On the Origin of Species By Means of Natural Selection / Author: Charles Darwin / eBook #1228"; ebook table identifies #1228 as the 1859 First Edition | prose exemplar: pre-emptive strongest objections; systematic hedging; cautious-optimism register |

Note: `docs/prose-guide.md` is the derived artifact; every quote in it was
re-checked against these files by page-indexed extraction (36/37 block quotes
matched mechanically; the Watson–Crick "It has not escaped our notice…" sentence
matches modulo two OCR character errors in the scan).

Notes:
- 1907.02474 title read from the supplement file; matches the brief.
- Additional sources found by the novelty sweep get appended here when fetched.
- Paywalled non-arXiv items (e.g. Dyson, Phys. Rev. 102, 1217 (1956)): ask TJO
  for TIB VPN access if the full text becomes load-bearing.

## Batch 3 — memory-index campaign (fetched 2026-08-27, titles verified from TeX)

| arXiv id | verified title | main tex | role |
|---|---|---|---|
| 1810.07351 | A many-body index for quantum charge transport | Index_Re.tex | BBDF many-body transport index — template for the M-INDEX quantization route |
| 1412.2970 | Lieb-Robinson bounds, Arveson spectrum and Haag-Ruelle scattering theory for gapped quantum spin systems | Scattering_spin-AHP1.tex | rigorous lattice Haag-Ruelle existence — template for AC-EX (T2) |

**Mismatch record (L3):** 1708.02120 was fetched on a guessed id for
Bachmann-Dybalski-Naaijkens; its TeX title is "Chirality induced Interface
Currents in the Chalker Coddington Model" — WRONG paper, directory deleted,
id must not be cited. Correct id is 1412.2970 (verified above).

## Batch 4 — 2+1 recon (fetched 2026-08-29)

Lane W5 of the 2+1 recon wave (bd tns-7pp). 13/13 fetched OK; every title
below extracted from the local TeX and compared to the arXiv listing. No id
mismatches. Digest: `docs/2p1-antecedents.md`.

| arXiv id | verified title | main tex | role |
|---|---|---|---|
| 2411.13633 | Soft gravitons in three dimensions | arXiv_v1.tex | THE 2+1 antecedent: a complete IR triangle in 3d (soft graviton theorem + BMS3 + memory) with no propagating graviton |
| 1703.01833 | Canonical Realization of (2+1)-dimensional Bondi-Metzner-Sachs symmetry | main.tex | bms3 realized canonically on a free 2+1 Klein-Gordon field — matter-only asymptotic charges, closest to a lattice-field corner A |
| 2503.20173 | Asymptotic symmetry and confinement in three-dimensional QED | arxiv_v1.tex | WARNING: 3d log-confinement makes asymptotic-symmetry action on states trivial and kills the 3d EM memory effect |
| 1712.00873 | Memory effect for particle scattering in odd spacetime dimensions | PRD_final_odd_Memory.tex | the d=3 memory verdict: no gravitational memory; scalar/EM give an *infinite momentum* memory, not a displacement memory |
| 1702.00095 | The Memory Effect for Particle Scattering in Even Spacetime Dimensions | main.tex | companion even-d computation (no memory for d>4) — fixes what "memory" means dimension by dimension |
| 1901.05942 | The Asymptotic Behavior of Massless Fields and the Memory Effect | main.tex | radiative vs Coulombic order, null vs ordinary memory split; odd-d total Coulombic memory vanishes (d>=4 analysis) |
| 1707.08016 | Color Memory | main.tex | memory as a holonomy/parallel-transport rotation of test charges — the observable shape a lattice topological memory should copy |
| 2211.09570 | A Goldstone theorem for continuous non-invertible symmetries | draft07.tex | only existing Goldstone theorem for a non-invertible symmetry — the gapless-mode input any categorical soft theorem needs |
| 2205.05086 | Non-invertible Global Symmetries in the Standard Model | QED_draft.tex | non-invertible symmetry -> selection rules on amplitudes; recasts the soft-pion/ABJ story as a generalized-symmetry matching |
| 2305.05774 | Fusion Surface Models: 2+1d Lattice Models from Fusion 2-Categories | main.tex | the concrete 2+1 lattice models carrying fusion 2-category symmetry — the arena for the lift |
| 1511.08090 | Anyons and matrix product operator algebras | AnyonsPEPS.tex | PEPS/MPO-injectivity <-> fusion category dictionary; anyon sectors as central idempotents (corner-A machinery in 2+1) |
| 1703.04748 | Edge modes and corner ambiguities in 3d Chern-Simons theory and gravity | Boundary.tex | boundary/edge symmetry of 3d CS as Kac-Moody; the classic "asymptotic symmetry = edge mode" statement |
| 1601.04744 | Local subsystems in gauge theory and gravity | symplectic.tex | Donnelly-Freidel extended phase space — why a 2+1 region boundary carries physical charge dof at all |

Not fetched, recorded honestly: Barnich-Compere gr-qc/0610130 (the founding
bms3 central-extension paper). The old-style id contains a slash, which
`scripts/fetch_refs.sh` would turn into a nested `refs/arxiv-gr-qc/0610130`
directory, breaking the naming convention. bms3 ground truth for this batch
is 2411.13633 + 1703.01833; fetch 0610130 separately if a bms3 quote becomes
load-bearing.

## Batch 5 — Ogata cluster (fetched 2026-08-29, session 8; requested by TJO Ogata deep-dive)

Fetched via scripts/fetch_refs.sh; every title extracted from the TeX itself
and checked against the ogata blitz lane's expected attribution
(theory/lanes/blitz-2026-08-29/ogata/ogata-map.md §2). 9/9 OK, no mismatches.

| arXiv id | verified title | main tex | role |
|---|---|---|---|
| 2110.04671 | Classification of symmetry protected topological phases in quantum spin chains | (single tex) | OGA-SURVEY: split ⇒ type-I half-chain, projective H^2 class, stability |
| 1810.01045 | A Z_2-index of symmetry protected topological phases with time reversal symmetry for quantum spin chains | (single tex) | OGA-INDEX: original SPT-index stability |
| 1908.08621 | A classification of pure states on quantum spin chains satisfying the split property with on-site finite group symmetries | (single tex) | OGA-SPLIT-CLASS: completeness of the H^2 class |
| 1906.05479 | Automorphic equivalence within gapped phases in the bulk | (single tex) | OGA-AUTO |
| 1407.3924 | C^1-Classification of gapped parent Hamiltonians of quantum spin chains | (single tex) | OGA-PARENT (no symmetry) |
| 1602.08839 | C^1-Classification of gapped parent Hamiltonians of quantum spin chains with local symmetry | (single tex) | OGA-PARENT (local symmetry) |
| 2004.06458 | General Lieb-Schultz-Mattis type theorems for quantum spin chains | OgataTachikawaTasaki.tex | OGA-LSM (on-site symmetry, split-state no-go) |
| 1808.08740 | Lieb-Schultz-Mattis type theorems for quantum spin chains without continuous symmetry | main.tex | OGA-LSM (no continuous symmetry) |
| 1301.5737 | Normal states of type III factors | (single tex) | OGA-TYPEIII: general type-III normal-state results |

## Batch 6 — continuum-reduction lane (fetched 2026-08-30, R1--R4 directive)

One id, title verified from its own TeX before use. Consumed by
`docs/reduction-limits.md` §3.1 and `labbook/sections/18_continuum_reduction.tex`.

| arXiv id | verified title | main tex | role |
|---|---|---|---|
| 1106.4382 | All-magnonic spin-transfer torque and domain wall propagation | swstt.tex | R3 reduction: the accepted continuum magnon-driven domain-wall statement (Yan--Wang--Xia, PRL 107, 177207). Load-bearing quotes: reflectionless Pöschl--Teller spin-wave equation (L.163--172), "a magnon changes its spin by 2ħ … absorbed by the DW" (L.81--84), spin-current reversal (L.213--217), and `V_DW = −(ρ²/2)V_g` (L.219--222). |

**MISMATCH RECORD (L3).** The reduction directive named arXiv:1108.5570 for
Yan--Wang--Xia. That id was fetched, and its TeX is a mathematics paper on
submanifolds and constrained variational calculus (`\documentclass{amsart}`,
Spanish-language macros) — an outright title mismatch. It was NOT retained and
no file under `refs/` carries it. The correct id, 1106.4382, was located by an
arXiv title query and then verified against `\title{}` in its own fetched TeX
before any quotation.
