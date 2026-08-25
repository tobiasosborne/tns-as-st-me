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

Notes:
- 1907.02474 title read from the supplement file; matches the brief.
- Additional sources found by the novelty sweep get appended here when fetched.
- Paywalled non-arXiv items (e.g. Dyson, Phys. Rev. 102, 1217 (1956)): ask TJO
  for TIB VPN access if the full text becomes load-bearing.
