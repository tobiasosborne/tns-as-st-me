# Joint-critic verdict: `mq-e`

## Scope adjudicated

I recomputed the fixed-charge wall enumeration, toggle rule, row/column component, graph Hamiltonian, leg charges, Fano multiplier, and local-observable decomposition.  I reran `check_mq_e.py` green and `--red` in both ordinary and optimized Python.  Ordinary exits were 0 and 1.  Optimized exits were also 0 and 1, but with the checker limitation below.

## FATAL

None.

## MAJOR

None on the analytic theorem.

## minor

- `check_mq_e.py:108-121,136-168` implements every green invariant with bare `assert`.  Under `python3 -O` those checks vanish; the registered red still exits 1 only because the mutated dictionary later causes a `KeyError` at `check_mq_e.py:145`, not because the advertised component/edge assertions execute.  Thus the saved ordinary run is red-capable, but there is no meaningful optimized certificate.  Replace the asserts with an explicit `require`/failure path before installing this as a repository checker; do not describe the current optimized run as evidence.
- `mq-e-proof.md:3-6` contains a malformed control character in the TeX-like `H_{rm XXZ}` strings.  Repair those strings when copying the shard; the mathematical scope is nevertheless clear from the surrounding `H_3=P_3H_{XXZ}P_3` text.

## note

- `mq-e-proof.md:59-91,223-311` exhausts the fixed-charge sector before selecting the incoming component.  Rectangle-interior vertices are isolated after compression; the proof does not falsely identify the whole `O(N²)` sector with the `O(N)` graph.
- `mq-e-proof.md:315-385` yields exactly `E_c=3JΔ/2`, `E_d=JΔ/2`, hopping/coupling `-J/2`.  Eliminating the side level gives `U(k)=J²/[4J(Δ-cos k)]` and hence the frozen `M-tk` multiplier and quadratic soft zero.
- `mq-e-proof.md:387-477` repairs the prior locality overclaim.  An unsubtracted local observable has two channel-tail constants; only the channel-subtracted remainder is finite graph support.  That is exactly the form Jacobi local decay can consume channel by channel.
- The infinite map is first defined on the stable product basis and the Hamiltonian equality on finite support, then extended using boundedness; no boundary convention or cofinal-sequence dependence remains.
- Full-chain leakage through `P_3H(1-P_3)` remains outside every promoted statement.

**Adjudication: PROMOTE-к-PROVED for projected-component `Mq-E`; this discharges the sole open premise of the already-proved conditional `Mq-AD3` and `M-tk` rows, so promote their projected-component readings while leaving every unprojected/full-chain claim open.**
