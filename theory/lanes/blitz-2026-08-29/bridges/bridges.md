# Structural-bridge triage

Scope: candidate statements only; no claim-status changes and no L6 promotion are proposed. Existing notation and definitions are cited rather than redefined. Exact constants and finite examples are checked by `bridge_checks.py`; saved outputs are `check-green.txt` and `check-red.txt`.

## 1. ABBV/Duistermaat--Heckman language for the SPT endpoint residue

- **Concrete statement available here.** If the centered transfer insertion has the form `B=(I-E)Y`, then `sum_{n=0}^{L-1}E^nB=(I-E^L)Y`; for the D23 AKLT path this is exactly SPT-E-AKLT, `R_L=-[1-(2b^2-1)^L]Z/2 -> -Z/2`.
- This is a discrete Stokes/coboundary identity in the finite-dimensional transfer complex. The transfer fixed point supplies normalization, while the decaying `Z` eigenchannel supplies the finite-size remainder.
- It is **not** an ABBV fixed-point formula: there is no natural compact symplectic manifold, Hamiltonian torus action, equivariantly closed integrand, or Euler-class denominator in D19--D23.
- In particular, the surviving endpoint is not a fixed locus: `Z` lies in the nonunit transfer channel and is killed by `E^L`; the residue is the primitive `Y` left by telescoping.
- An honest localization theorem would first need a natural phase space functorially attached to the MPS transfer register and an equivariant integral equal to the registered compression. No such object is present, and adding one only to reproduce the geometric sum is artificial.
- This agrees with `theory/dh-hunt.md` candidates 3--4: DH neither produces the endpoint congruence nor turns the coupling sweep into wall crossing.
- **Verdict: DEAD.** Keep “exact transfer telescoping” or “discrete Stokes,” and do not advertise the exact zero/half residue as ABBV or DH exactness.

## 2. Is S-IDX-fin-G a Fredholm/Kato/APS index theorem?

- **Concrete separating statement.** The normalized Ward pairing of S-IDX-fin-G can equal `1` while every natural analytic index built from the same finite-sector map is `0`.
- Take one represented root doublet, `J_0(X)=Q(X)`, and its positive-weight vector. Then `D=Q(F)` is an isomorphism between one-dimensional weight spaces, so `ind D=0`, while (H.17) gives the normalized Ward pairing `1`.
- Likewise, `P=proj(ran D)` equals the target-sector projector in this example, so the relative index of that projection pair is `0`, not the Ward value. In general the pair index measures a rank defect, whereas (H.10) is a state-dependent normalized matrix element.
- APS/eta or spectral-flow language would require a self-adjoint Fredholm path (or a bulk Dirac operator with spectral boundary conditions); S-IDX-fin-G supplies a fixed finite-dimensional lowering map and no such path or boundary spectrum.
- The exact value comes from adjoint covariance, `D^dagger J_0(F)psi=J_0(H)psi`, followed by normalization. It is algebraic and not a homotopy-stable kernel-minus-cokernel count.
- The separate S-IDX-G-label theorem *is* an integral/torsion representation label, but it is a character difference, not an APS eta pairing.
- Reference fence: the [pair-of-projections index](https://doi.org/10.1006/jfan.1994.1031) counts projection defects, and the [abstract APS theorem](https://arxiv.org/abs/2004.01085) identifies an APS Fredholm index with spectral flow; neither datum occurs in (H.8)--(H.10).
- **Verdict: DEAD.** Retain the qualified name “normalized Ward index”; do not claim a Fredholm, Kato-pair, spectral-flow, or APS theorem.

## 3. Schwinger-model theta vacua as a second triangle model

- **Concrete statement available here.** On a finite open Kogut--Susskind chain, the physical-space Gauss law `L_n-L_{n-1}=Q_n` implies `sum_{n=a}^b Q_n=L_b-L_{a-1}` exactly, with `L_n` integer-valued.
- With background `alpha=theta/(2pi)`, the physical electric field is proportional to `L_n+alpha`; therefore a same-link two-time electric-flux increment is integral in gauge-coupling units because the fixed theta offset cancels. This is a clean M-INDEX-fin-style memory statement.
- Theta is consequently a vacuum/background offset, not itself the memory increment. A theta quench may create flux dynamics, but its late-time distribution still needs a specified TPM protocol and a relaxation/tightness theorem analogous to D27.
- Gauge-invariant MPS and real-time electric-field quenches are established numerically in [Buyens et al.](https://arxiv.org/abs/1312.6654), and theta-dependent vacuum observables have been computed with MPS in [Funcke--Jansen--Kuehn](https://arxiv.org/abs/1908.00551).
- The full triangle fails: gauge symmetry is a constraint rather than the global asymptotic symmetry of D2/D10, and the Schwinger mechanism removes the massless photon (the pre-existing fence in `HANDOFF_MPS_SOFT_THEOREM.md` section 5.1).
- At `theta=pi` the critical point is Ising-like ([Ohata](https://arxiv.org/abs/2311.04738)); its soft critical Majorana mode is not a charged Goldstone leg, and the critical state also exits the exact finite-bond injective-MPS regime.
- What would be needed is a gauge-invariant flux TPM implementation plus an explicit charge/domain-wall scattering protocol, followed by a separate soft statement; Gauss law alone supplies only the memory corner.
- **Verdict: PARK.** It is numerics-friendly as a memory-only comparator or companion-paper model, but it is not a second showcase of the same infrared triangle and has no slot in the current Letter skeleton.

## 4. Kitaev/Majorana chains with only fermion parity

- **Concrete negative statement.** For `G=Z_2^F`, `Lie(G)=0`; there is no root triple, no `Q(F_alpha)`, and no adjoint-covariant Lie-current row. Thus S-IDX-fin-G has no fermion-parity instance, exactly as its finite-group fence says.
- Parity-preserving Hamiltonians and physical currents are even. An edge Majorana is odd and intertwines the two parity sectors, so it supplies a selection label/edge operator rather than the Ward current entering (H.8)--(H.10).
- **Concrete replacement.** For a quadratic chain `H=(i/4)gamma^T A gamma` with real antisymmetric invertible `A`, the relative ground-state parity between two gapped endpoints is the sign change of `Pf(A)`; along a path it changes only through zero modes. This is a genuine mod-two spectral-flow invariant.
- The replacement captures the parity-opposite edge doublet of the topological chain described by [Kitaev](https://arxiv.org/abs/cond-mat/0010440), but it has no normalized current residue and no Adler/soft-momentum statement.
- Extending it beyond free fermions would require a graded CAR/fMPS version of the endpoint algebra, a parity-flux or boundary-condition path, and a mod-two index stable under even interactions; ordinary bosonic D1--D10 cannot simply be reused.
- The interacting classification already changes the available invariant (for example the BDI reduction studied by [Fidkowski--Kitaev](https://arxiv.org/abs/1008.4138)), reinforcing that parity alone does not determine the present Ward index.
- **Verdict: PARK (replacement only); the direct bridge is DEAD.** A fermionic companion could use mod-two spectral flow/parity pumping, but the current soft index does not survive after replacing a Lie symmetry by `Z_2^F`.

## 5. Added candidate: memory quantization as an exact full-counting-statistics periodicity

- **Concrete statement.** For the D27 finite-window TPM law define `chi_W(lambda)=sum_nu p_W(nu) exp(i lambda nu)`. M-INDEX-fin is equivalent to `chi_W(lambda+2pi)=chi_W(lambda)` and in particular `chi_W(2pi)=1`.
- The converse is exact for any probability law on the real line: `chi(2pi)=1` forces `exp(2pi i nu)=1` almost surely, hence the law is supported on the integers.
- Under D27 first-moment tightness, every subsequential limiting law retains the periodicity, and uniform integrability gives `chi'(0)=i sum_nu nu p_nu=-2is delta x` along the same subsequence.
- This packages support quantization and the memory expectation in one directly measurable generating function; it introduces no channel inventory and respects the fixed-window offset-cancellation mechanism of M-INDEX-fin.
- Numerically, evaluating `chi_W` avoids histogram bin-edge choices and supplies two sharp diagnostics: periodicity for quantization and the derivative at the origin for the displacement.
- What is needed is only a lightweight corollary/checker against existing D16 and lambda--D TPM data; no new theorem hypothesis is required.
- **Verdict: PURSUE.** This can improve the Section 4 presentation and Fig. 2 diagnostics without changing the theorem or opening a new proof program.

## Triage order

1. Pursue the FCS corollary as a paper/figure diagnostic.
2. Park Schwinger as a memory-only comparator and Majorana parity as a different mod-two companion program.
3. Close the ABBV/DH and APS-index language: both exact values already have simpler algebraic mechanisms, and the required geometric/analytic-index data are absent.
