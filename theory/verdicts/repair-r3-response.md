# Repair r3 response

| item | exact edit |
|---|---|
| r3 promotions | Promoted SPT-B', registered SPT-T'/SPT-D', and the exactly scoped SPT-M' conditional implication in `claims/CLAIMS.md` and `theory/TRIANGLE.md`; kept physical T'/D' use conditional on H-split/H-dress and M' conditional on H-split, H-AD-edge, charge conservation, and definite channel charges.  SPT-E' remains SKETCH and is marked “repaired, awaiting r4.” |
| N3 | Relabelled fixed-ring `Γ_N(k)` in `notation.md` as an off-shell analytic interpolation at fixed periodic `N`. |
| R3-N1 | Deleted deformation constancy of `q_{ω,C}^∘` from SPT-E'.  The theorem now retains only fixed-tensor spectral congruence and lift-gauge invariance; SPT-M' consumes only that congruence. |
| R3-N2 | Deleted the moment-map/torsor sentence from the PROVED B3 summary.  Section 10 now leaves the displayed-graph Fano formula and quadratic zero PROVED conditional on Mq-E, while only full-chain accuracy and universality remain SKETCH/CONJECTURE. |
| R3-N3 | Restricted SPT-E-AKLT to equation (4.1) and its AKLT-family limit.  The trivial `O(2)` product residue is labelled checked supporting comparison, outside the promoted row. |
| R3-N4 | Rebuilt S-C6's partial charge independently from the anti-Hermitian one-site generator `-iS^z` through `inserted_transfer`; its dual-left compression is compared with `i*measured`, and `-iQ` with `measured`. |

Verification: all eight checkers pass under `python3 -O`.  The four documented
red modes exit `1`: M-quant continuity residue `2.340e+00`, ML4 false-uniform
scaling, SPT edge-sign error `1.333e+00`, and SPT uncentered-gauge error
`3.700e-01`.
