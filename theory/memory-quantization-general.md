<!-- ROLE: proposer proof shard for claim M-quant-G.  The claim enters at
     SKETCH and awaits its own L6 critic.  Structure follows CLAUDE.md L6b. -->

# M-quant-G — the memory law for compact `G`, injective MPS vacua, and finite range

## 0. Status and theorem

**Proposer status:** **SKETCH**, pending L6 criticism.  This shard proves a
conditional implication.  It does not prove the dynamical hypothesis D18 for
an arbitrary Hamiltonian.  The existing XXZ row M-quant remains **PROVED
conditional on D18**; no status is transferred from that converged row to this
new general row.

### THEOREM M-quant-G (general conditional memory law)

**ASSUME (H-MQG).**

1. `G` is compact and `{A_γ}_{γ∈Ω_vac}` is a `G`-covariant family of
   injective canonical MPS tensors of one common, arbitrary finite bond
   dimension `χ`, as in D1 and D2(a).  Fix `α` and
   `β=g·α≠α`; use the kink sector `𝒦_{αβ}` supplied by A2(a,c,d,f).
2. A common unbroken compact abelian subgroup lies in `H_α∩H_β`.  Choose one
   primitive circle direction `ξ` in its Lie algebra and fix, once for both
   tails, the Hermitian on-site charge `S^z:=-i q(ξ)`.  In this fixed
   convention
   `ω_α(S^z)=+s` and `ω_β(S^z)=-s`, with `s>0`.  For a higher-dimensional
   torus, the theorem is applied componentwise after choosing `ξ`; a finite
   abelian group without a circle direction is not enough for D10's current.
3. `H` is translation invariant, finite range, and `G`-invariant in the exact
   sense of D10(a); the two vacua are stationary.  Its infinite-volume
   dynamics therefore obeys G0(e), equivalently D10(b), for the selected
   charge.
4. The selected incoming state is a fixed wave packet in
   `𝒦^{(1)}_{αβ}` of D17.  Its wall coordinate is exactly the windowed
   observable `𝔛_W` of D13(a), with the charge and `s` fixed in item 2.  No
   plane wave is admitted in place of this packet.
5. **(H-AD-G)** holds for this vector.  This is shorthand, not a replacement
   definition, for all of D18(AD1)--(AD4), with one incoming left leg, one
   reflected outgoing leg, and one transmitted outgoing leg.  Their charges,
   measured relative to the vacuum supporting each leg in the single
   convention of item 2, are

   `q_in=-1`, `q_L=-1` on the reflected left leg, and `q_T=+1`.

   D18(AD2)'s transmitted-channel projection is `N_T`; D18(AD1) excludes any
   further propagating channel, and the selected vector has no bound-state
   component.

**PROVE.**  Form the infinite-volume dynamics and the wave operators first;
fix the packet; at each fixed window take the incoming and outgoing
large-time limits; only then increase `W=[a,b]` to `ℤ`, with both kink-core
distances tending to infinity.  In this order the asymptotic two-channel
displacement observable on the selected scattering space obeys

\[
 \boxed{\Delta X=-{1\over s}N_T},\qquad
 \boxed{\delta x=-{\langle N_T\rangle\over s}}.                 \tag{G.1}
\]

Consequently

\[
 \operatorname{spec}(\Delta X)\subset\{0,-1/s\},\qquad
 \operatorname{Var}(\Delta X)
 ={1\over s^2}\langle N_T\rangle(1-\langle N_T\rangle).        \tag{G.2}
\]

The outcome quantum is fixed by charge conservation: reflection transfers no
charge between the two vacuum conventions, while transmission changes the
separated leg charge by `q_T-q_in=2`.  More generally, if that difference is
some definite `ν`, the same proof gives the quantum `-ν/(2s)`.  Thus the
displayed `-1/s` includes the primitive channel normalisation in H-MQG(5); it
is not invariant under relabelling a charge-`ν` particle as charge one.

Hypothesis `(T)` is not required for (G.1).  If it is imposed, D9(d)/A2(e)
labels the fixed vacuum pair by the double coset
`𝔡(α,β)∈H_α\G/H_α`.  The scattering changes the wall coordinate inside
`𝒦_{αβ}` and does not change that label.

---

## 1. What replaces “`χ=1` product vacuum”

The replacement list is the following.  It is deliberately separated into
structural input and the smaller arithmetic core.

1. **Product vacua are replaced by injective MPS vacua.**  D1(c) supplies the
   transfer gap and controlled contractions for exact D1(e′) two-sided MPS
   cores.  The proof never sets `χ=1`, never diagonalises a transfer matrix,
   and never assumes a sharp product wall.  For the larger D17 class the
   theorem uses summability, not an unjustified exponential rate.
2. **A product wall is replaced by an A2 sector.**  A2(a,c,d,f) constructs and
   superselects `𝒦_{αβ}` for each fixed `g` with `β=g·α`.  Under `(T)` only,
   A2(e)/D9(d) gives its double-coset vacuum-pair label.  Neither the refuted
   `A2-orbit-r1` object nor a torsor interpretation is used.
3. **Exact product asymptotics are replaced by the `ℓ¹` class.**  D17 makes the
   charge deviations from the two MPS vacua summable.  It is precisely what
   permits the regularised charge limit below; weak-* sector membership D9(a)
   alone would not suffice.
4. **A sharp-wall site count is replaced by D13(a).**  The single fixed
   physical charge has vacuum densities `+s,-s`, so D13(a) calibrates one
   lattice translation of the kink as charge `2s`.  This density jump, not
   the bond dimension, sets the denominator in (G.1).
5. **An explicit product-channel decomposition is replaced by D18.**  AD1--AD4
   provide wave operators, completeness for the selected sector, definite
   relative leg charges, local decay, and the limit order while retaining
   reflected/transmitted coherence.
6. **Microscopic XXZ conservation is replaced by finite-range `G`
   invariance.**  G0(e)/D10 gives the exact cut-current continuity equation.
   On either unbroken MPS tail G0(d) also represents the normal-ordered vacuum
   charge action as a difference of virtual bond insertions.  That bond
   potential controls MPS endpoint bookkeeping; it is not the physical
   current and is not used to infer a soft zero.

Only items 3--6, the density calibration in H-MQG(2), and the existence of the
fixed sector are load-bearing for the charge arithmetic.  Injectivity is the
sharp structural hypothesis that realises the requested vacuum family and
the A2 MPS kink register; it is not secretly used to promote every D17 state
to an exponentially local decoration.  No property special to a scalar
virtual space survives in the proof.

**Uniformity domain.**  At the general D17 level the tail error is the
state-specific omitted `ℓ¹` sum; it tends to zero as `W↑ℤ`, with no rate and
no uniformity in time, packet, or model asserted.  If the asymptotic kink core
is additionally one fixed D1(e′) two-sided MPS decoration with modifications
in a fixed bounded support, then, after fixing `α,β`, that decoration and
`λ̃∈(max{λ_{E_α},λ_{E_β}},1)`, D1(c) gives
`C_{λ̃}<∞`, independent of `W`, with tail
`C_{λ̃}λ̃^{d_W}`.  No such constant is asserted uniformly over `G`, a
continuous vacuum manifold, `α,β`, `χ`, tensors, Hamiltonians, packets,
times, core decorations, or deformations.

---

## 2. Proof

### ⟨1⟩1. The kink label is well defined and is not the memory variable

**ASSUME.** H-MQG(1), and `(T)` only for the last sentence.

**PROVE.**  The selected state has fixed asymptotic label `(α,β)`; under `(T)`
its diagonal invariant is `𝔡(α,β)`, and neither changes during the event.

**⟨2⟩1.**  The half-infinite broken transformation gives a state in
`𝒦_{αβ}`, disjoint from the vacuum sector, for each fixed `g` with
`β=g·α`.

*Justification.* Active claim A2(c,d,f) and D9(a,b).

**⟨2⟩2.**  Finite-range dynamics with stationary vacua preserves the
factorised left/right boundary functionals at every finite time.

*Justification.* Active claim B3, first clause, whose proof uses D9(a) and
finite-range Lieb--Robinson quasi-locality.

**⟨2⟩3.**  If `(T)` holds, the complete diagonal invariant is the double coset
in `H_α\G/H_α`; without `(T)` the statement is only per `G`-orbit.

*Justification.* D9(d) and active claim A2(e).

**⟨2⟩4.**  Hence `δx` below is motion within a fixed sector, not a change of
vacuum-pair label.

*Justification.* ⟨2⟩1--⟨2⟩3 and D13(a), which defines `δx` as a difference of
windowed wall coordinates.  **⟨2⟩5. QED.**

### ⟨1⟩2. The exact finite-window charge identity

**ASSUME.** H-MQG(2,4), a finite `W=[a,b]`, and a cut `c∈W`.

**PROVE.**  The charge in `W`, regularised against the step vacuum at `c`, is

\[
 \sum_{x=a}^{c}(S_x^z-s)+\sum_{x=c+1}^{b}(S_x^z+s)
 =2s(\mathfrak X_W-c).                                         \tag{G.3}
\]

**⟨2⟩1.**  The scalar terms on the left sum to
`s(a+b-1-2c)`.

*Justification.* Direct finite sum over the displayed integer intervals.

**⟨2⟩2.**  Expanding D13(a)'s right side gives
`Σ_{x=a}^b S_x^z+s(a+b-1-2c)`.

*Justification.* D13(a) and finite algebra.

**⟨2⟩3.**  The two expansions coincide exactly, for arbitrary states and
arbitrary `χ`.

*Justification.* ⟨2⟩1--⟨2⟩2.  **⟨2⟩4. QED.**

### ⟨1⟩3. The regularised charge exists and is conserved

**ASSUME.** H-MQG(1--4).

**PROVE.**  Equation (G.3) has the required increasing-window limit on the
selected in/out kink states, and the total of kink plus separated leg charge
is conserved.

**⟨2⟩1.**  The two tail series obtained by subtracting `+s` on the left and
`-s` on the right converge absolutely for the fixed packet and its finite-time
evolution.

*Justification.* D17, including its finite-time preservation statement.  The
packet is fixed before any soft limit by H-MQG(4).

**⟨2⟩2.**  For the finite window, the Heisenberg derivative of its charge is
the difference of the two physical cut currents; internal currents telescope
for every finite interaction range.

*Justification.* G0(e), equivalently D10(a,b), and active claim M-flux.  The
Hermitian equation is obtained from D10's anti-Hermitian convention by the
fixed multiplication by `-i` in H-MQG(2).

**⟨2⟩3.**  The total conserved charge label passes to the scattering channels
only after the infinite-volume dynamics and wave operators are formed.

*Justification.* D18(AD1,AD3,AD4) as assumed in H-AD-G.

**⟨2⟩4.**  The residual core-tail charge omitted by `W` tends to zero.  No
rate is needed.  Under the additional fixed-decoration condition stated in
§1, it is instead bounded by `C_{λ̃}λ̃^{d_W}` on exactly that fixed data.

*Justification.* D17 for the general `ℓ¹` limit; D1(c) and D13(a) for the
optional fixed-decoration rate.  G0(d) gives the compatible virtual
bond-difference form on each unbroken tail, but does not replace the
physical-current argument of ⟨2⟩2.

**⟨2⟩5.**  Thus the ordered D18 limits give a conserved sum of the limiting
quantity `2s(𝔛_W-c)` and the stated separated leg charge.

*Justification.* (G.3), ⟨2⟩1--⟨2⟩4, and D18(AD3--AD4).
**⟨2⟩6. QED.**

### ⟨1⟩4. Charge conservation fixes each channel displacement

**ASSUME.** H-AD-G and the conclusion of ⟨1⟩3.

**PROVE.**  Reflection has displacement `0`, and transmission has displacement
`-1/s`.

**⟨2⟩1.**  In a channel with outgoing relative charge `q_out`, equality of
the in/out total charges gives

\[
 2s\,\delta x+(q_{\rm out}-q_{\rm in})=0.                     \tag{G.4}
\]

*Justification.* ⟨1⟩3.⟨2⟩5 and subtraction of the common cut `c`; this is
also active claim B3, second clause.

**⟨2⟩2.**  On reflection, `q_out=q_L=q_in=-1`, so (G.4) gives `δx_R=0`.

*Justification.* H-MQG(5) and ⟨2⟩1.

**⟨2⟩3.**  On transmission, `q_out=q_T=+1` and `q_in=-1`, so (G.4) gives
`2s δx_T+2=0`, hence `δx_T=-1/s`.

*Justification.* H-MQG(5), `s>0` from H-MQG(2), and ⟨2⟩1.

**⟨2⟩4. QED.**

### ⟨1⟩5. Channel superposition gives (G.1)--(G.2)

**ASSUME.** D18(AD1--AD2) and ⟨1⟩4.

**PROVE.**  The operator, expectation, spectrum, and variance statements of
the theorem hold without replacing a coherent outgoing state by a mixture.

**⟨2⟩1.**  On the two outgoing channel space the displacement is
`0·P_L-(1/s)P_T`.

*Justification.* ⟨1⟩4.⟨2⟩2--⟨2⟩3 and D18(AD1), which excludes another
propagating channel for the selected sector.

**⟨2⟩2.**  Conjugation to the physical scattering space gives
`ΔX=-(1/s)W_+P_TW_+^*=-(1/s)N_T`.

*Justification.* D18(AD2) and ⟨2⟩1.

**⟨2⟩3.**  In `Ψ=W_-(φ,0)`, taking the expectation gives
`δx=-‖φ_T‖²/s=-⟨N_T⟩/s`.

*Justification.* D18(AD2) and ⟨2⟩2.

**⟨2⟩4.**  Since `N_T` is an orthogonal projection,
`spec(ΔX)⊆{0,-1/s}` and
`Var(ΔX)=s^{-2}⟨N_T⟩(1-⟨N_T⟩)`.

*Justification.* D18(AD2), `N_T^2=N_T`, and ⟨2⟩2.

**⟨2⟩5. QED.**  Equations (G.1)--(G.2) follow. □

---

## 3. XXZ instantiation and consistency check

Take D16 with `G=U(1)⋊ℤ₂`, `α=↑`, `β=↓`, and `s=1/2`.  The two tensors are
injective product tensors with `χ=1`, so H-MQG(1--4) is the special case of
the general hypotheses in which every transfer-tail error vanishes exactly.
The unbroken circle is generated by the same physical `S^z` on both tails;
the broken spin flip reaches `𝒦_{↑↓}` by A2(f).

D18(AD3) assigns `q_in=q_L=-1` and `q_T=+1`.  Therefore (G.1)--(G.2) become

\[
 \Delta X=-2N_T,\quad \delta x=-2\langle N_T\rangle,\quad
 \operatorname{spec}(\Delta X)\subset\{0,-2\},\quad
 \operatorname{Var}(\Delta X)=4\langle N_T\rangle(1-\langle N_T\rangle).
\]

These are exactly the frozen M-quant numbers in
`memory-quantization.md` (Mq.2),(Mq.8).  If Mq-E is additionally assumed, the
active implication Mq-AD3 supplies D18 for the displayed `≤3`-wall Fano graph;
then (G.1) recovers the projected corollary.  For the full XXZ chain, D18 is
still an explicit hypothesis.  Nothing here upgrades Mq-E or full-chain D18.

The SU(2) ferromagnetic family broken to `U(1)` gives another compatible
example.  A compatible rank-two example needs a nonabelian ambient group:
take

\[
 G=(U(1)^2)\rtimes\mathbb Z_2,qquad
 r:(z_1,z_2)\longmapsto(z_1^{-1},z_2),
\]

and on `\mathbb C^2` set

\[
 Q_1=\begin{pmatrix}1&0\\0&-1\end{pmatrix},\quad
 Q_2=2I,\quad
 u(\theta,\phi)=e^{i\theta Q_1}e^{i\phi Q_2},\quad
 u(g)=r=\begin{pmatrix}0&1\\1&0\end{pmatrix}.
\]

Thus `r^\dagger Q_1r=-Q_1`, `[r,Q_2]=0`, and
`r u(\theta,\phi)r=u(-\theta,\phi)`, so these matrices represent the stated
semidirect action.  Choose the product-MPS rays
`\alpha=[(1,0)^T]` and `\beta=g\cdot\alpha=[(0,1)^T]`.  The same selected
torus stabilises both rays because
`u(\theta,\phi)(1,0)^T=e^{i(\theta+2\phi)}(1,0)^T` and
`u(\theta,\phi)(0,1)^T=e^{i(-\theta+2\phi)}(0,1)^T`.  Its vacuum-density
vectors are `(1,2)` and `(-1,2)`: the selected `Q_1` direction has
`(+s,-s)` with `s=1`, while `Q_2` is preserved as a spectator.  With
`q_{\rm in}=(-1,2)` and `q_{\rm out}=(1,2)`, componentwise conservation is
`(2,0)\,\delta x+(2,0)=0`, hence `\delta x=-1` and zero spectator change.

**Remark.** A bare abelian ambient group, or a selected central factor, is
excluded: `\operatorname{Ad}_{g^{-1}}\xi=\xi` would make covariance give
`\omega_\beta(Q_1)=\omega_\alpha(Q_1)`, so one orbit cannot have the required
opposite vacuum densities.

The checker constructs both compatible examples and verifies this
representation and arithmetic.  It does not prove their H-AD-G hypotheses;
for the continuous SU(2) vacuum orbit, A2's result is only pointwise in the
chosen pair because the active S-A2 uniformity box is still SKETCH.

---

## 4. Limit discipline, conventions, and limitations

1. **D18 remains conditional.**  Compact symmetry, injectivity, and finite
   range do not imply wave-operator existence, asymptotic completeness, local
   decay, absence of extra channels, or the charge assignments in H-MQG(5).
   Establishing those facts is model-specific.
2. **No general sector reduction is claimed.**  Mq-E is relevant only to the
   XXZ `≤3`-wall graph and remains CONJECTURE.  There is no hidden general-MPS
   analogue in this proof.
3. **The order is sequential, not uniform.**  Infinite volume and wave
   operators precede time limits; time limits at fixed `W` precede
   `W↑ℤ`; a normalisable packet is fixed before any `k→0` limit.  No estimate
   covers `k=Θ(1/N)`, and no constant is uniform in volume or momentum.  The
   general D17 tail convergence has no rate; the optional exponential rate of
   §1 applies only to the fixed D1(e′) decoration stated there.
4. **The charge convention is fixed.**  The shared physical generator, its
   vacuum values `±s`, and the primitive leg charges `±1` are fixed before the
   comparison.  A common additive charge offset cancels, and changing the cut
   shifts both asymptotic coordinates equally, but an absolute uncentred
   charge or wall origin is not invariant.  Rescaling the generator rescales
   both `s` and all `q` values; only `-(q_out-q_in)/(2s)` is convention
   covariant.
5. **A finite abelian symmetry alone is insufficient.**  Without a circle
   generator there is only a modular charge label, not D10's local continuous
   current or the real-valued D13 displacement law.  The abelian-factor form
   means a compact torus (possibly accompanied by finite factors) with one
   selected primitive circle direction.
6. **No soft theorem follows.**  G0(d) is a virtual bond-potential identity on
   an unbroken vacuum and G0(e) is physical continuity.  Neither asserts an
   Adler zero, a transmission law, a scattering phase, or universality.  If a
   separate result shows `⟨N_T⟩→0`, then (G.1) transfers that zero to memory.
7. **No torsor or deformation invariant is inferred.**  The double coset, when
   `(T)` holds, labels the unchanged vacuum pair.  The measured displacement
   is charge bookkeeping inside that sector; it is not a moment map, a flat
   kink torsor, an SPT index, or a deformation-independent absolute charge.

---

## 5. Checker scope

Run

```text
python3 -O theory/checks/mquant_general_check.py
python3 -O theory/checks/mquant_general_check.py --red  # deliberately FAILS
```

Named computation **MqG-check C1** performs the symbolic general-`s` charge
subtraction, guards that `s` remains a positive free symbol, and evaluates it
at `s=1` and `s=3/2`.  **C2** checks the fixed-pair `SU(2)→U(1)` arithmetic
and constructs the two-dimensional `(U(1)^2)\rtimes\mathbb Z_2`
representation above, including conservation of the spectator component.
**C3** substitutes the frozen spin-`1/2` XXZ values and the soft coefficient
already present in M-quant.  The checker tests representation and arithmetic
only: it does not construct MPS tensors, wave operators, or a proof of
H-AD-G.
