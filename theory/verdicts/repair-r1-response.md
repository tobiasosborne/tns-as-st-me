# Non-SPT summit repair — response to r1 critics

Proposer response (repair round **r1**, 2026-08-26) to
[`mquant-ml45-r1.md`](mquant-ml45-r1.md) and
[`triangle-r1.md`](triangle-r1.md).  Positive rows attacked by either FAIL
verdict remain `SKETCH` until r2; this document records repairs, not status
upgrades.

The binding strategy was downgrade-first.  ML4 is now fixed-volume/ordered
limit; Mq-AD3 is conditional on the all-volume graph isomorphism; the memory
claim is spin-`1/2` plus abstract charge arithmetic; and no virtual-bond
interpretation is attached to physical current flux.  Stronger statements are
future work listed at the end.

## M-quant / ML4 / ML5 objections

| id | disposition | exact repair |
|---|---|---|
| mq-1 | **DOWNGRADED** | `ml4-ward-reduction.md` ⟨1⟩4.⟨2⟩2--⟨2⟩4 replaces the false `N`-uniform (15)--(17) by `C_{I,N}` and the ordered limit `k→0` before `N→∞`; ⟨2⟩3 records the `k=2π/N` countersequence.  `TRIANGLE.md` §2.5 and the ML4 DAG row match it. |
| mq-2 | **FIXED** | `definitions.md` D24(c) and `ml5-universality.md` ⟨1⟩2 require **both** `M_2^O(0)=0` and `𝔠_h(O)=0`; they define `K_O(ε)=(1/2)sup‖∂_k²M_2^O‖` and state when the relative `C_I‖M_1‖` bound follows.  D24(e)/ML5-I1 records the critic's four-site intercept counterexample. |
| mq-3 | **FIXED** | `definitions.md` D24(d)(1) and `ml5-universality.md` ⟨1⟩3 hypothesis 1 state the exhaustive normed LSZ decomposition; ⟨2⟩2 invokes it before summing all remainder terms. |
| mq-4 | **FIXED** | `definitions.md` D18 is replaced by AD1--AD4 (wave operators, selected channels, charges/local decay, order of limits).  The superseded norm-mixture form and coherent `r|R⟩+t|T⟩` counterexample are recorded in D18.  `memory-quantization.md` §2 now cites rather than redefines D18. |
| mq-5 | **DOWNGRADED** | `memory-quantization.md` §3 states Mq-E as an explicit all-volume enumeration/unitary hypothesis.  Mq-AD3 proves the Kato--Rosenblum/Feshbach consequence only conditional on Mq-E; `corner-b-draft.md` §5 and `TRIANGLE.md` §§3.2--3.4 match.  Future proof: bd `tns-00l`. |
| mq-6 | **FIXED** | `memory-quantization.md` Corollary Mq-quant and `TRIANGLE.md` §3.2 state `Var(ΔX)`, not `Var(𝔛_W)`, and name the extra sharp-initial-wall/two-time conditions needed to identify the latter.  The DAG M-quant row matches. |
| mq-7 | **RETRACTED** | `TRIANGLE.md` §3.1, the M/M-flux DAG rows, and `corner-b-draft.md` §2 delete the virtual/bond-data reading.  Mq-flux is exactly physical boundary-current DC weight and depends only on D10(b), D13. |
| mq-8 | **DOWNGRADED** | `memory-quantization.md` §0 and `TRIANGLE.md` §3.2 restrict the concrete claim to D16 spin `1/2`.  The only arbitrary-`s` residue is the explicitly conditional arithmetic `2s·δx+(q_out-q_in)=0`; no higher-spin channel theorem is claimed. |
| mq-9 | **FIXED** | Active `Bd3`/`Bd4`/`A2(e′)` citations are replaced by D13/D14/A2(e) in `memory-quantization.md`; historical `Bd` labels remain only in marked history/crosswalk prose in `corner-b-draft.md`. |
| mq-10 | **FIXED** | `checks/ml4_check.py` adds ML4-Q1 at `k=2π/N`, verifies the nonuniform growth, and has a failing `--red-uniform` mutation.  It also adds ML5-I1.  The M-quant DAG row and shard §6 now describe `mquant_check.py` only as a flux/empirical certificate, not a spectral proof. |

## TRIANGLE objections

| id | disposition | exact repair |
|---|---|---|
| T1 | **DOWNGRADED** | `TRIANGLE.md` header, §§2.3--3.4, §6, and §7 plus `claims/CLAIMS.md` mark every r1-attacked positive row at most `SKETCH`.  Only Corner A, oracle facts, and ML2 retain `PROVED`. |
| T2 | **FIXED** | `TRIANGLE.md` defines only the four L5 statuses, renames §7 the status index, and freezes only PASS-backed rows.  §5 is explicitly pre-r2/under rebuild while D19--D23 remain unchanged.  `claims/CLAIMS.md` uses the same enum. |
| T3 | **RETRACTED** | The false B3(ii) half-line equation is removed from `TRIANGLE.md` §6.3, the B3 DAG row, and `corner-b-draft.md` §7.  It is replaced by `2s·δx+(q_out-q_in)=0` with `c∈W` and leg subtraction. |
| T4 | **FIXED** | Same D18 repair as mq-4; all projected claims now consume AD1--AD4 and are conditional on Mq-E. |
| T5 | **RETRACTED** | Same physical-current-only repair as mq-7. |
| T6 | **DOWNGRADED** | `TRIANGLE.md` standing directive and §3.2 separate the spin-`1/2` D16 application from abstract charge arithmetic and explicitly track the general `(G, injective MPS, finite-range)` theorem as bd `tns-zw2`. |
| T7 | **FIXED** | `TRIANGLE.md` §§2.4 and 6.1 plus S-general in the DAG list ML1, ML3/`k=Θ(1/N)`, ML4 at `n≥2`, exhaustive LSZ, microscopic `𝒮_W` membership, and ML6.  “Closed at n=1” is deleted. |
| T8 | **DEFERRED-TO-REBUILD** | Status-only lane repair: `TRIANGLE.md` §5 and the SPT-nogo DAG row mark the all-orders/all-registers form REFUTED/withdrawn pending the scoped rebuild in `theory/spt-rebuild.md`. |
| T9 | **DEFERRED-TO-REBUILD** | `TRIANGLE.md` §5 marks the deciding-computation design UNDER REBUILD; substantive redesign belongs solely to `theory/spt-rebuild.md`. |
| T10 | **DEFERRED-TO-REBUILD** | Accepted duplicated-paragraph defect, but editing §5 substance would violate the lane boundary.  The rebuild agent owns the clean replacement. |
| T11 | **FIXED** | `corner-b-draft.md` (5.3) and `TRIANGLE.md` §3.4 now write `R(k)=1-16(Δ-1)^2k^2+O(k^4)`. |
| T12 | **RESIDUE** | Accepted note: negative rows remain only as explicit history/withdrawal and are retained. |

## Corner-B objections

| id | disposition | exact repair |
|---|---|---|
| B1 | **RETRACTED** | `corner-b-draft.md` §7 removes the false half-line equation and proves only the explicit-cut, leg-subtracted conservation formula in ⟨1⟩2. |
| B2 | **FIXED** | B3 ⟨1⟩1 supplies the missing finite-time Lamport argument from Lieb--Robinson quasi-locality, translation covariance, stationary vacua, and D9(a)'s factorised limits.  Status remains SKETCH pending r2. |
| B3 | **FIXED** | `corner-b-draft.md` §7 is rewritten as an L6b ASSUME/PROVE tree with numbered leaves, existing D-number/named-theorem citations, and terminal QEDs.  The nonexistent “Proposition N” citation is deleted. |
| B4 | **RETRACTED** | `corner-b-draft.md` §§2,7,8 removes the kink virtual-charge identification from active Mq-flux/B3 and relegates R1/R3 to optional future virtual interpretation. |
| B5 | **FIXED** | D18 and all consumers use coherent AD1--AD4; the norm-mixture formulation is explicitly superseded. |
| B6 | **DOWNGRADED** | K4 is renamed `Conjecture K4`; §1.2, §3, §7, P5, §8, and §10 no longer use flatness/uniqueness/no recoil as a theorem. |
| B7 | **DOWNGRADED** | Header/summary, M′, P4/P8, §10, DAG, and TRIANGLE say channel spectrum `{0,-1/s}`, continuous expectation, and concrete spin-`1/2` scope.  Higher spin is a conjectural falsifier. |
| B8 | **FIXED** | `definitions.md` D13(a), `memory-quantization.md` (Mq.11), and `corner-b-draft.md` §§2,3,6,9 replace bare `λ_E^L`/`e^{-L/ξ_c}` errors by `C_{λ̃}λ̃^{d_W}`, `λ̃∈(λ_E,1)`, with core-to-edge distance `d_W`. |
| B9 | **FIXED** | `corner-b-draft.md` §10 lists B3 and all positive Corner-B work as SKETCH pending r2; it no longer places B3(i)--(iv) under “proved.” |
| B10 | **RESIDUE** | Accepted note: historical negative citations remain explicitly marked as withdrawals. |

## SPT lane dispositions

| ids | disposition | exact status-only action |
|---|---|---|
| S1--S8 | **DEFERRED-TO-REBUILD** | `TRIANGLE.md` §5, `claims/CLAIMS.md`, and the D19--D23 preface carry **UNDER REBUILD — r1 verdict S1--S8; rebuild in `theory/spt-rebuild.md` (in progress)**.  No D19--D23 or `spt-scoping-draft.md` claim content was rewritten. |
| S9--S10 | **DEFERRED-TO-REBUILD** | Accepted as rebuild-lane model/regularity cleanup; no non-SPT-lane content edit made. |

## Future work deliberately not attempted

- Packet-smeared infinite-volume ML4/ML3 control, including `k=Θ(1/N)`: bd
  `tns-7ut`.
- ML4-3, exhaustive LSZ derivation, and microscopic `𝒮_W` membership: bd
  `tns-axg`.
- All-volume projected Fano enumeration/unitary Mq-E: bd `tns-00l`.
- Full-chain D18 for XXZ: bd `tns-d51`.
- General `(G, injective MPS, finite-range H)` memory theorem: bd `tns-zw2`.

## Checker contract

The required optimized-mode suite is

```text
for f in theory/checks/*.py; do python3 -O "$f" || echo "FAIL $f"; done
```

`ml4_check.py --red-uniform` is required to fail.  The final run record is
reported in the proposer handoff after all edits.
