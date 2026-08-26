<!-- ROLE: proof shard for claim M-quant.  Repaired after L6 r1 FAIL.
     Prover revision r1-repair, 2026-08-26.  Structure follows CLAUDE.md L6b. -->

# M-quant — conditional charge bookkeeping for kink memory

## 0. Statement and honest status

**Status:** M-flux is **PROVED**, M-quant is **PROVED conditional on D18**,
Mq-AD3 is **PROVED conditional on Mq-E**, and the displayed Fano formula/soft
zero is **PROVED conditional on Mq-E for the displayed graph**, all per
`verdicts/corpus-r2.md` adjudication.  In particular, the projected result is conditional on
the stated all-volume sector enumeration/unitary isomorphism; the repository
currently contains only a finite `N=14` enumeration.

**M-quant statement (spin-`1/2` easy-axis XXZ; conditional on D18).**
Let `Δ>1` and take the spin-`1/2` Hamiltonian of D16, with unbroken `U(1)`
charge `S^z` and asymptotic spins `+1/2` at the left and `-1/2` at the right,
selecting `𝒦_{↑↓}`.  Prepare one right-moving magnon on the `↑` leg and use
the windowed wall coordinate `𝔛_W` of **D13(a)**; it is not redefined here.

Assume **(H-AD)** of D18 for this scattering vector.  With D18(AD4)'s limit
order, the asymptotic memory is

\[
 \boxed{\delta x=-{1\over s}\,\langle N_T\rangle}.                 \tag{Mq.2}
\]

Here and below the formulas retain `s` to expose the charge arithmetic, but
the concrete D16 application has `s=1/2`, hence `δx=-2⟨N_T⟩`.  `N_T` is the
D18(AD2) transmitted-channel projection.  The channel statement is
independent of `k`, `Δ`, packet shape, and scattering phase.

**Abstract arithmetic corollary (not a general MPS theorem).**  For any
finite-range `U(1)`-invariant dynamics satisfying D18 with vacuum jump `2s`,
incoming/outgoing separated leg charges `q_in,q_out`, and a kink coordinate
whose regularised charge is `2s(m-c)`, conservation gives only

`2s·δx + (q_out−q_in) = 0`.

This algebraic implication does not establish the required channels for a
higher-spin XXZ chain or for general `(G, injective MPS, finite-range H)`.
That generality gap is tracked as bd `tns-zw2` and is not attempted here.

The finite-`N`, finite-time flux/DC lemma (§1) is PROVED per corpus-r2.  D18 is
assumed for the unprojected chain.  Section 3 verifies its spectral consequences **only if** the sector
reduction hypothesis Mq-E is supplied.  The measured `O(Δ^{-2})` leakage into
`≥5`-wall configurations is evidence for a controlled lift, not a
uniform-in-time scattering estimate.  No result below uses the refuted
`A2-orbit-r1` row or claim B3.

Claim **A2(a,c,d,f)** is used only for the already-proved identification and
superselection of `𝒦_{↑↓}`; its proof is not repeated.  Claim **A2(e)** gives
the corrected vacuum-pair classification and is not load-bearing here.

---

## 1. Exact finite-volume flux/DC lemma

**LEMMA Mq-flux (finite `N`, finite time).**

**ASSUME.** A finite open chain, any state `ρ(t)`, any interior window
`W=[a,b]`, and the local continuity equation

\[
 {d\over dt}S_x^z=j_{x-1|x}-j_{x|x+1}.                            \tag{Mq.3}
\]

**PROVE.** For every finite `t_i<t_f`,

\[
 \rho_{t_f}(\mathfrak X_W)-\rho_{t_i}(\mathfrak X_W)
 ={1\over2s}\int_{t_i}^{t_f}\!dt\,
 [\rho_t(j_{a-1|a})-\rho_t(j_{b|b+1})].                          \tag{Mq.4}
\]

Equivalently, the right side is the difference of the two finite-time current
Fourier transforms at zero frequency.  No kink, spectral, large-time, or
asymptotic-completeness hypothesis is used.

**⟨1⟩1.** `𝔛_W` is a bounded local observable at every finite `N`.

*Justification.* Definition **D13(a)**.

**⟨1⟩2. PROVE.** Its Heisenberg derivative is the boundary flux.

**⟨2⟩1.** Differentiate D13(a)'s finite sum and insert (Mq.3).

*Justification.* **D10(b)**, with the Hermitian-current convention of D13(a).

**⟨2⟩2.** The sum over `x=a,…,b` telescopes exactly to
`j_{a-1|a}-j_{b|b+1}`.

*Justification.* Finite telescoping sum; no boundary limit is taken.

**⟨2⟩3. QED.**

**⟨1⟩3.** Integrating ⟨1⟩2 from `t_i` to `t_f` proves (Mq.4); setting the
Fourier frequency to zero gives the DC form.

*Justification.* Fundamental theorem of calculus and the definition of a
finite-time Fourier transform.

**⟨1⟩4. QED.** □

The independent computation **Mq-check F1** constructs the frozen-boundary
XXZ Hamiltonian in fixed-`S^z` configuration bases and verifies both the
operator identity and (Mq.4); see §6.

---

## 2. The sole full-chain hypothesis

**(H-AD) is D18.**  This shard does not redefine it.  In the D16 channel used
here, D18(AD3)'s charges are `q_in=-1` on the `↑` leg and `q_out=+1` on the
transmitted `↓`-vacuum leg (or `q_out=-1` on reflection).  D18(AD2) defines

\[
 N_T=W_+P_TW_+^*\quad\hbox{on }ℋ_{sc},\qquad
 \langle N_T\rangle=\|φ_T\|^2.                                  \tag{Mq.6}
\]

The former norm-mixture version of H-AD is superseded in D18.  In particular,
a coherent state `r|R⟩+t|T⟩` is not replaced in norm by its diagonal mixture;
the operator `N_T` and the displacement variance below retain that coherence.

---

## 3. Conditional H-AD verification for the `≤3`-wall graph

**Mq-AD3 (PROVED conditional on Mq-E per corpus-r2 adjudication).**  For spin
`1/2`, let `P_3` project the fixed-`S^z`
kink-plus-one-magnon space onto configurations with one or three domain walls
and retain the connected component containing the incoming magnon.

**ASSUME Mq-E (all-volume enumeration/isomorphism).**  For every volume in a
cofinal open-chain sequence, and in the infinite-volume limit, there is an
explicit unitary from that incoming cyclic component to `ℓ²(ℤ)⊕ℂ|d⟩` which:

1. intertwines `H_3=P_3HP_3` with (Mq.7);
2. identifies the two tails with the D14 reflected/transmitted leg channels;
3. assigns relative charges `-1` to the incoming/reflected tail and `+1` to
   the transmitted tail; and
4. carries fixed-window observables to finite-support graph observables, so
   Jacobi local decay implies D18(AD3).

The `N=14` enumeration S1 in `corner-b-draft.md` is evidence for Mq-E, not a
proof of this quantified assumption.

**PROVE.**  Under Mq-E, `H_3` satisfies D18 for every incoming packet with
smooth momentum amplitude compactly supported in `k∈(0,π)`.  A
finite-dimensional bound subspace may be present but is orthogonal to a
Møller-prepared packet.

**⟨1⟩1. PROVE.** `H_3` is a finite-rank perturbation of a free Jacobi channel
plus a flat kink level.

**⟨2⟩1.** Under Mq-E, the `1-DW⊕3-DW` component is a uniform two-sided chain with hopping
`-J/2` and channel on-site energy `E_c=3JΔ/2`, plus one side vertex of energy
`E_d=E_c-JΔ=JΔ/2`, coupled to the junction by `-J/2`.

*Justification.* Hypothesis Mq-E(1); finite computation S1 is explicitly not
used as an all-volume theorem.

**⟨2⟩2.** Hence, on `ℓ²(ℤ)⊕ℂ|d⟩`,

\[
 H_0=\left[E_c-{J\over2}(T+T^*)\right]\oplus E_d,
\quad H_3-H_0=-{J\over2}(|0\rangle\langle d|+|d\rangle\langle0|). \tag{Mq.7}
\]

The second operator has rank at most two and is trace class.

*Justification.* ⟨2⟩1 and direct graph-to-matrix identification.

**⟨2⟩3.** The side vertex is the fixed-charge representative of the exactly
flat zero-energy kink family after the telescoping kink boundary field is
restored.

*Justification.* Named computations **K1--K3** in `corner-b-draft.md` §1.2;
only existence and degeneracy of the constructed family are used, not K4's
thermodynamic uniqueness claim.

**⟨2⟩4. QED.**

**⟨1⟩2. PROVE.** The wave operators for `(H_3,H_0)` exist and are complete on
the absolutely continuous subspace.

**⟨2⟩1.** `H_3-H_0` is trace class by ⟨1⟩1.

**⟨2⟩2.** The Kato--Rosenblum theorem therefore gives `W_±` and
`Ran W_±=ℋ_ac(H_3)`.

*Justification.* Kato--Rosenblum trace-class scattering theorem applied to
(Mq.7).

**⟨2⟩3. QED.**

**⟨1⟩3. PROVE.** `H_3` has no singular-continuous spectrum, and its remaining
spectrum is a finite set of localised eigenstates outside the channel band.

**⟨2⟩1.** Reflection about the junction splits off an odd free channel; the
even channel together with `|d⟩` is a half-line Jacobi matrix differing from
the constant-coefficient one at finitely many entries.

*Justification.* (Mq.7) and parity decomposition.

**⟨2⟩2.** With
`m_0(z)=⟨0|(z-E_c+J(T+T*)/2)^{-1}|0⟩
=[(z-E_c)^2-J^2]^{-1/2}`, every cyclic resolvent entry of the even-plus-side
block is a rational function of `z` and `m_0(z)`, with denominator
`z-E_d-(J²/4)m_0(z)`.

*Justification.* Schur-complement (Feshbach) computation for (Mq.7).

**⟨2⟩3.** On the interior of `[E_c-J,E_c+J]`, `m_0(E+i0)` has nonzero
imaginary part, so that denominator has no real zero; its spectral measure is
absolutely continuous there.  Outside the band its zeros are isolated and
finite; at the two thresholds the Jacobi solutions are constant/linear (up
to `(-1)^n`) and are not in `ℓ²`.

*Justification.* Boundary values of the displayed square root and the
constant-coefficient Jacobi recurrence.

**⟨2⟩4.** Thus `ℋ=ℋ_b⊕Ran W_±`, with `dim ℋ_b<∞`.

*Justification.* ⟨2⟩1--⟨2⟩3 and ⟨1⟩2.

**⟨2⟩5. QED.**

**⟨1⟩4. PROVE.** The two scattering tails obey AD2--AD3.

**⟨2⟩1.** Fourier transformation diagonalises the free chain.  A smooth
packet supported away from `k=0,π` leaves every finite set as
`t→±∞`.

*Justification.* Riemann--Lebesgue/stationary-phase computation for
`E(k)=E_c-J cos k`.

**⟨2⟩2.** The wave-operator limits transfer this local decay to `H_3`; the
left and right tails are the reflected and transmitted channels.

*Justification.* D18(AD1), ⟨1⟩2, and ⟨2⟩1.

**⟨2⟩3.** Mq-E labels the left tail by a kink at bond `m` plus a down magnon and
the right tail by a kink at bond `m-2` plus an up hole.  Their charges are
`-1` and `+1`, respectively.

*Justification.* Hypothesis Mq-E(2)--(3) and D14.

**⟨2⟩4.** These statements are AD2--AD3, while ⟨1⟩3 is AD1 and the strong
limits impose AD4.

*Justification.* D18 and hypothesis Mq-E(4).

**⟨2⟩5. QED.**

**⟨1⟩5. QED.** □

**Why this is conditional even before the full-chain lift.**  The cited S1
support is one `N=14` enumeration, not the all-volume unitary Mq-E.  The
Kato--Rosenblum and Feshbach steps prove the spectral conclusion only after
Mq-E is assumed.  Separately, the full Hamiltonian has
`P_3H(1-P_3)≠0`; five-wall and higher configurations are real, not absent.
The finite-time probabilities reported in `corner-b-draft.md` §5.2 are about
`0.10,0.03,0.008` at `Δ=2,4,8`, consistent with `O(Δ^{-2})`.  Promoting that
observation to H-AD requires a uniform scattering estimate (or a Feshbach/
Mourre analysis of all open channels).  A small Frobenius norm at finite `N`,
or a finite-time leakage probability, does not supply that estimate.

---

## 4. Proof of the conditional M-quant implication

Choose a cut `c` and define the regularised total charge on a separated kink
configuration by subtracting `+s` to the left and `-s` to the right.  A kink
whose D13(a) coordinate is `m` contributes `2s(m-c)`.

**⟨1⟩1. PROVE.** The regularised total `S^z` charge is conserved.

**⟨2⟩1.** On every finite frozen-boundary chain, the sum of `S_x^z` over the
dynamical sites commutes with `H_N`: internal bond currents cancel and the
frozen endpoints carry no hopping current.

*Justification.* Claim **G0(e)** / **D10(b)** and finite telescoping, exactly
as in Lemma Mq-flux.

**⟨2⟩2.** The fixed finite-volume charge label therefore passes to the
thermodynamic in/out channel limits.

*Justification.* D18(AD1,AD4), which forms the thermodynamic dynamics before
the scattering limits and keeps all channels in the chosen charge sector.

**⟨2⟩3. QED.**

**⟨1⟩2. PROVE.** The kink charge is `2s(m-c)`.

**⟨2⟩1.** For a sharp kink, every site between `c` and `m` differs from the
chosen reference step by `2s`, with the sign fixed by the ordering of `c,m`.

*Justification.* Direct finite sum and **D13(a)**.

**⟨2⟩2.** Dressing inside the same fixed-charge kink sector does not change
this eigenvalue, and `W↑ℤ` removes the D13(a) tail error.

*Justification.* D18(AD3); sector identification is claim **A2(c,d)**.

**⟨2⟩3. QED.**

**⟨1⟩3. PROVE.** A reflected branch has zero displacement.

**⟨2⟩1.** Its in/out total charges are
`2s(m_i-c)-1` and `2s(m_R-c)-1`.

*Justification.* ⟨1⟩2 and D18(AD3), `q_L=-1`.

**⟨2⟩2.** Conservation gives `m_R=m_i`.

*Justification.* ⟨1⟩1 and ⟨2⟩1.

**⟨2⟩3. QED.**

**⟨1⟩4. PROVE.** A transmitted branch has displacement `-1/s`.

**⟨2⟩1.** Its in/out total charges are
`2s(m_i-c)-1` and `2s(m_T-c)+1`.

*Justification.* ⟨1⟩2 and D18(AD3), `q_T=+1`.

**⟨2⟩2.** Conservation gives `2s(m_T-m_i)=-2`, hence
`m_T-m_i=-1/s`.

*Justification.* ⟨1⟩1 and ⟨2⟩1.

**⟨2⟩3. QED.**

**⟨1⟩5.** On `ℋ_L⊕ℋ_R`, the displacement operator is therefore
`0·P_L-(1/s)P_T`; conjugating by `W_+` gives `ΔX=-(1/s)N_T` on `ℋ_sc`.

*Justification.* ⟨1⟩3, ⟨1⟩4, and D18(AD1--AD2).

**⟨1⟩6.** Taking the expectation in `Ψ` proves (Mq.2).

*Justification.* ⟨1⟩5 and definition (Mq.6).

**⟨1⟩7. QED.** □

H-AD enters only at ⟨1⟩2.⟨2⟩2 and ⟨1⟩3--⟨1⟩5, where interacting late-time
states are replaced by separated channels.  The flux lemma and charge
arithmetic do not use it.

---

## 5. Quantisation, soft zero, and finite-window budget

**COROLLARY Mq-quant.** For one incoming magnon,

\[
 \operatorname{spec}(\Delta X)\subset\{-1/s,0\},\qquad
 \delta x=-\langle N_T\rangle/s\in[-1/s,0],\qquad
 \operatorname{Var}_\Psi(\Delta X)
 ={1\over s^2}\langle N_T\rangle(1-\langle N_T\rangle).        \tag{Mq.8}
\]

Thus the channel outcomes, not every expectation value, are quantised.  This
is the precise reading of `(1/s)·[-1,0]`: the expectation is the convex
combination selected by `⟨N_T⟩∈[0,1]`.

**⟨1⟩1.** `N_T` is an orthogonal projection, so its spectrum is contained in
`{0,1}` and its expectation in `[0,1]`.

*Justification.* D18(AD2).

**⟨1⟩2.** Since `ΔX=-(1/s)N_T` and `N_T²=N_T`,
`⟨(ΔX)²⟩=s^{-2}⟨N_T⟩`; subtracting `⟨ΔX⟩²` gives the variance in (Mq.8).

*Justification.* D18(AD2) and M-quant ⟨1⟩5.

**⟨1⟩3.** Apply the M-quant implication to obtain the expectation and
spectrum.

*Justification.* (Mq.2).

**⟨1⟩4. QED.** □

This is `Var(ΔX)`, the two-channel displacement observable.  It is not the
one-time variance `Var(𝔛_W)` unless a sharp initial-wall eigenstate and an
explicit two-time measurement convention are additionally imposed.

Under Mq-E, eliminating the flat side level gives the named Fano computation
of `corner-b-draft.md` §5.2,

\[
 t(k)=\left[1+{iJ^2\over4\omega(k)v(k)}\right]^{-1},\quad
 T(k)=\left[1+\left({J^2\over4\omega(k)v(k)}\right)^2\right]^{-1}, \tag{Mq.9}
\]

where `ω(k)=J(Δ-cos k)` and `v(k)=J sin k`.  Therefore

\[
 T(k)=16(Δ-1)^2k^2+O(k^4),\qquad
 \delta x(k)=-{16(Δ-1)^2\over s}k^2+O(k^4).                     \tag{Mq.10}
\]

The soft zero follows for the Fano graph **conditional on Mq-E**.  For the full chain, (Mq.2) implies
`δx(k)→0` whenever the *full* transmission satisfies `T(k)→0`; (Mq.10)'s
coefficient is not promoted beyond the projection.

At finite window and finite separation it is useful to keep the theorem and
measurement errors distinct:

\[
 |\delta x_W+\langle N_T\rangle/s|
 \le \epsilon_{\rm AD}+C_{\tilde\lambda}\tilde\lambda^{d_W}
     +{N_W(t_i)+N_W(t_f)\over s}+\epsilon_{\rm num}.             \tag{Mq.11}
\]

Here `λ̃∈(λ_E,1)`, `d_W` is the minimum kink-core-to-window-edge distance
(D13(a)), `ε_AD` is an *empirical local charge-decomposition defect* when the
exact D18 channels are approximated numerically, `N_W` is residual leg
content, and `ε_num` includes estimator and evolution errors.  All terms
vanish in the exact conditional limits.  `ε_AD` is not a return to the
superseded norm-mixture definition of D18.
An `O(Δ^{-2})` projection error is added only when replacing the full
`⟨N_T⟩` by the Fano value from (Mq.9); it is **not** an error in (Mq.2).

---

## 6. Numerical certificate and empirical error budget

Run:

```text
python3 -O theory/checks/mquant_check.py
python3 -O theory/checks/mquant_check.py --red   # deliberately FAILS
```

Named computation **Mq-check F1** independently builds two frozen-boundary
fixed-`S^z` Hamiltonians (`N=7,8`) and their bond currents.  It obtains zero
operator residue in (Mq.3) and `3.37×10^{-16}` finite-time residue in (Mq.4).
It does **not** construct wave operators, prove Mq-E, exclude
singular-continuous spectrum, or test `spec(ΔX)`.

Named computation **Mq-check N1** reads the committed JSON.  On its nine clean
`N=160`, `dwmax=3`, standoff-36 rows with trapped weight below `10^{-6}`:

* the documented headline estimator has
  `max|δx_1+2T|=0.004330` sites, i.e. `0.004` at the reported precision;
* the integrated-magnetisation estimator `δx_2`, the direct D13(a) proxy, has
  `max|δx_2+2T|=0.001233` sites;
* the largest estimator spread is `0.005563` sites and the largest possible
  trapped-charge term is `2(8.862×10^{-7})` sites; the maximum *per-row*
  combined budget is `0.005563` at six decimals, so both residuals lie inside
  the scan's own budget;
* norm and energy drifts in these rows are at most `7.75×10^{-13}` and
  `6.08×10^{-10}`, respectively, subleading to measurement geometry.

The `dwmax=3` versus `5` comparison in `kink-sector-notes.md` §5.3 shifts the
robust integrated estimator by `0.0096` sites at `Δ=2,N=56` (about `0.5%`).
Together with the measured `O(Δ^{-2})` higher-wall probability, this supports
but does not prove the full-chain lifting part of H-AD.  The empirical
`0.004` agreement is therefore consistent with the exact conditional theorem;
it is not advertised as a proof of H-AD.
