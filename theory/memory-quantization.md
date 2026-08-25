<!-- ROLE: proof shard for claim M-quant.  New file only, per task constraint.
     Prover revision p1, 2026-08-25.  Structure follows CLAUDE.md L6b. -->

# Theorem M-quant — charge-quantised kink memory

## 0. Statement and honest status

**THEOREM M-quant (full easy-axis XXZ; conditional only on H-AD).**
Let `Δ>1` and let the ferromagnetic XXZ chain have on-site spin `s`, unbroken
`U(1)` charge `S^z`, and frozen asymptotic spins `+s` at the left and `-s` at
the right, selecting the kink sector `𝒦_{↑↓}`.  Prepare one right-moving
magnon on the `↑` leg and use the windowed bond-charge coordinate of **Bd3**,

\[
 \mathfrak X_W=a-1+{1\over 2s}\sum_{x=a}^{b}(S_x^z+s),\qquad W=[a,b].
\tag{Mq.1}
\]

Assume **H-AD** of §2 for this scattering state.  With the thermodynamic limit
taken before the scattering limits and then `W↑ℤ`, the asymptotic memory is

\[
 \boxed{\delta x=-{1\over s}\,\langle N_T\rangle}.                 \tag{Mq.2}
\]

Here `N_T` is the *operator* projecting onto the transmitted one-magnon
channel, transported to the interacting scattering space by the outgoing
wave operator.  Thus (Mq.2) is an operator/channel statement before it is an
expectation-value statement; it is independent of `k`, `Δ`, packet shape, and
scattering phase.  For `s=1/2`, `δx=-2⟨N_T⟩`.

**Status.** The finite-`N`, finite-time flux/DC lemma (§1) is **exact and
unconditional**.  H-AD is **proved in §3 for the `≤3`-domain-wall projected
dynamics** of the spin-`1/2` chain.  H-AD for the unprojected infinite XXZ
chain is **assumed**, not proved.  The measured `O(Δ^{-2})` leakage into
`≥5`-wall configurations is evidence for a controlled lift, but it is not a
uniform-in-time scattering estimate.  No result below uses the refuted
`A2(e)` orbit statement or the SKETCH claim `B3`.

Claim **A2(a,c,d,f)** is used only for the already-proved identification and
superselection of `𝒦_{↑↓}`; its proof is not repeated.  Claim **A2(e′)** gives
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

*Justification.* Definition **Bd3**, Eq. (Mq.1).

**⟨1⟩2. PROVE.** Its Heisenberg derivative is the boundary flux.

**⟨2⟩1.** Differentiate (Mq.1) and insert (Mq.3).

*Justification.* **D10(b)**, with the Hermitian-current convention of Bd3.

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

Fix a conserved regularised-charge sector and let `ℋ_L,ℋ_R` be the free
one-particle channel spaces for, respectively, a magnon on the `↑` leg and a
hole/magnon on the `↓` leg.  Let `ℋ_as=ℋ_L⊕ℋ_R`, with channel Hamiltonian
`H_as`, identification `J`, and projections `P_L,P_T`.

**H-AD (one-kink/one-magnon asymptotic decomposition).**

**(AD1: wave operators and completeness.)** The limits

\[
 W_\pm=\operatorname*{s-lim}_{t\to\pm\infty}
 e^{itH}J e^{-itH_{\rm as}}
\tag{Mq.5}
\]

exist as isometries and have the same range `ℋ_sc`; the physical sector
decomposes orthogonally as `ℋ=ℋ_b⊕ℋ_sc`, where `ℋ_b` contains spatially
localised bound states.  There is no further propagating channel.

**(AD2: selected scattering state.)** The state is
`Ψ=W_-(φ,0)` with `φ∈ℋ_L`, hence has no `ℋ_b` component, and
`W_+^*Ψ=(φ_R,φ_T)`.  Define

\[
 N_T:=W_+P_TW_+^*\quad\hbox{on }ℋ_{sc},\qquad
 \langle N_T\rangle=\|φ_T\|^2.                                  \tag{Mq.6}
\]

For an on-shell diagonal scattering matrix this is
`∫(dk/2π)|φ(k)|²T(k)`; it is not generally `T` at the mean momentum.

**(AD3: channel charge and local decay.)** The left asymptotic particle has
`S^z` charge `q_L=-1` relative to the `↑` vacuum; the transmitted right
particle has `q_T=+1` relative to the `↓` vacuum.  For every fixed window
containing the kink, free leg charge and every non-bound dressing leave the
window as `t→±∞`; the remaining local state is a kink charge eigenstate, and
the `W↑ℤ` limit of (Mq.1) exists on it.

**(AD4: order of limits.)** The infinite-volume dynamics and (Mq.5) are formed
before `t→±∞`; the fixed-window scattering limits are formed before `W↑ℤ`.

H-AD is narrower than general many-body asymptotic completeness: it concerns
one fixed-charge, one-incoming-magnon sector and explicitly permits localised
bound states, while requiring the selected vector to be orthogonal to them.
AD1--AD3 are exactly where the passage from the finite-time identity to
separated in/out charges enters.

---

## 3. H-AD for the `≤3`-wall projected dynamics

**THEOREM Mq-AD3 (projected asymptotic completeness; unconditional).**
For spin `1/2`, let `P_3` project the fixed-`S^z` kink-plus-one-magnon space
onto configurations with one or three domain walls and retain the connected
component containing the incoming magnon.  The dynamics generated by
`H_3=P_3HP_3` satisfies H-AD for every incoming packet with smooth momentum
amplitude compactly supported in `k∈(0,π)`.  A finite-dimensional bound
subspace may be present but is orthogonal to a Møller-prepared packet.

**⟨1⟩1. PROVE.** `H_3` is a finite-rank perturbation of a free Jacobi channel
plus a flat kink level.

**⟨2⟩1.** The `1-DW⊕3-DW` component is a uniform two-sided chain with hopping
`-J/2` and channel on-site energy `E_c=3JΔ/2`, plus one side vertex of energy
`E_d=E_c-JΔ=JΔ/2`, coupled to the junction by `-J/2`.

*Justification.* Named domain-wall enumeration **S1** in
`corner-b-draft.md` §5.1, independently established in
`kink-sector-notes.md` §2.

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

*Justification.* Definition (Mq.5), ⟨1⟩2, and ⟨2⟩1.

**⟨2⟩3.** S1 labels the left tail by a kink at bond `m` plus a down magnon and
the right tail by a kink at bond `m-2` plus an up hole.  Their charges are
`-1` and `+1`, respectively.

*Justification.* Named computation **S1** and **Bd4**.

**⟨2⟩4.** These statements are AD2--AD3, while ⟨1⟩3 is AD1 and the strong
limits impose AD4.

*Justification.* H-AD as stated in §2.

**⟨2⟩5. QED.**

**⟨1⟩5. QED.** □

**Why this does not yet prove full-chain H-AD.** The full Hamiltonian has
`P_3H(1-P_3)≠0`; five-wall and higher configurations are real, not absent.
The finite-time probabilities reported in `corner-b-draft.md` §5.2 are about
`0.10,0.03,0.008` at `Δ=2,4,8`, consistent with `O(Δ^{-2})`.  Promoting that
observation to H-AD requires a uniform scattering estimate (or a Feshbach/
Mourre analysis of all open channels).  A small Frobenius norm at finite `N`,
or a finite-time leakage probability, does not supply that estimate.

---

## 4. Proof of Theorem M-quant

Choose a cut `c` and define the regularised total charge on a separated kink
configuration by subtracting `+s` to the left and `-s` to the right.  A kink
whose Bd3 coordinate is `m` contributes `2s(m-c)`.

**⟨1⟩1. PROVE.** The regularised total `S^z` charge is conserved.

**⟨2⟩1.** On every finite frozen-boundary chain, the sum of `S_x^z` over the
dynamical sites commutes with `H_N`: internal bond currents cancel and the
frozen endpoints carry no hopping current.

*Justification.* Claim **G0(e)** / **D10(b)** and finite telescoping, exactly
as in Lemma Mq-flux.

**⟨2⟩2.** The fixed finite-volume charge label therefore passes to the
thermodynamic in/out channel limits.

*Justification.* H-AD(AD1,AD4), which forms the thermodynamic dynamics before
the scattering limits and keeps all channels in the chosen charge sector.

**⟨2⟩3. QED.**

**⟨1⟩2. PROVE.** The kink charge is `2s(m-c)`.

**⟨2⟩1.** For a sharp kink, every site between `c` and `m` differs from the
chosen reference step by `2s`, with the sign fixed by the ordering of `c,m`.

*Justification.* Direct finite sum and **Bd3**.

**⟨2⟩2.** Dressing inside the same fixed-charge kink sector does not change
this eigenvalue, and `W↑ℤ` removes the Bd3 tail error.

*Justification.* H-AD(AD3); sector identification is claim **A2(c,d)**.

**⟨2⟩3. QED.**

**⟨1⟩3. PROVE.** A reflected branch has zero displacement.

**⟨2⟩1.** Its in/out total charges are
`2s(m_i-c)-1` and `2s(m_R-c)-1`.

*Justification.* ⟨1⟩2 and H-AD(AD3), `q_L=-1`.

**⟨2⟩2.** Conservation gives `m_R=m_i`.

*Justification.* ⟨1⟩1 and ⟨2⟩1.

**⟨2⟩3. QED.**

**⟨1⟩4. PROVE.** A transmitted branch has displacement `-1/s`.

**⟨2⟩1.** Its in/out total charges are
`2s(m_i-c)-1` and `2s(m_T-c)+1`.

*Justification.* ⟨1⟩2 and H-AD(AD3), `q_T=+1`.

**⟨2⟩2.** Conservation gives `2s(m_T-m_i)=-2`, hence
`m_T-m_i=-1/s`.

*Justification.* ⟨1⟩1 and ⟨2⟩1.

**⟨2⟩3. QED.**

**⟨1⟩5.** On `ℋ_L⊕ℋ_R`, the displacement operator is therefore
`0·P_L-(1/s)P_T`; conjugating by `W_+` gives `ΔX=-(1/s)N_T` on `ℋ_sc`.

*Justification.* ⟨1⟩3, ⟨1⟩4, and H-AD(AD1--AD2).

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
 \delta x=-\langle N_T\rangle/s\in[-1/s,0].                      \tag{Mq.8}
\]

Thus the channel outcomes, not every expectation value, are quantised.  This
is the precise reading of `(1/s)·[-1,0]`: the expectation is the convex
combination selected by `⟨N_T⟩∈[0,1]`.

**⟨1⟩1.** `N_T` is an orthogonal projection, so its spectrum is contained in
`{0,1}` and its expectation in `[0,1]`.

*Justification.* H-AD(AD2).

**⟨1⟩2.** Apply Theorem M-quant.

*Justification.* (Mq.2).

**⟨1⟩3. QED.** □

For the projected dynamics, eliminating the flat side level gives the named
Fano computation of `corner-b-draft.md` §5.2,

\[
 t(k)=\left[1+{iJ^2\over4\omega(k)v(k)}\right]^{-1},\quad
 T(k)=\left[1+\left({J^2\over4\omega(k)v(k)}\right)^2\right]^{-1}, \tag{Mq.9}
\]

where `ω(k)=J(Δ-cos k)` and `v(k)=J sin k`.  Therefore

\[
 T(k)=16(Δ-1)^2k^2+O(k^4),\qquad
 \delta x(k)=-{16(Δ-1)^2\over s}k^2+O(k^4).                     \tag{Mq.10}
\]

The soft zero is unconditional for `H_3`.  For the full chain, (Mq.2) implies
`δx(k)→0` whenever the *full* transmission satisfies `T(k)→0`; (Mq.10)'s
coefficient is not promoted beyond the projection.

At finite window and finite separation it is useful to keep the theorem and
measurement errors distinct:

\[
 |\delta x_W+\langle N_T\rangle/s|
 \le \epsilon_{\rm AD}+C e^{-L/\xi_c}
     +{N_W(t_i)+N_W(t_f)\over s}+\epsilon_{\rm num}.             \tag{Mq.11}
\]

Here `ε_AD` is the charge-expectation defect in the approximate two-channel
decomposition, `N_W` is residual leg content, and `ε_num` includes estimator
and evolution errors.  All terms vanish in the exact limits of the theorem.
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

Named computation **Mq-check N1** reads the committed JSON.  On its nine clean
`N=160`, `dwmax=3`, standoff-36 rows with trapped weight below `10^{-6}`:

* the documented headline estimator has
  `max|δx_1+2T|=0.004330` sites, i.e. `0.004` at the reported precision;
* the integrated-magnetisation estimator `δx_2`, the direct Bd3 proxy, has
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
