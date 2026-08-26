"""
    SpinSTwoMagnon

Two-magnon scattering in the spin-`S` isotropic Heisenberg FERROMAGNET, for
arbitrary `S`, by the wavepacket-collision method that
`numerics/src/fm_twomagnon.jl` uses at `S = 1/2`.  Falsifier (A) of Conjecture
Bc (theory/TRIANGLE.md §4, bd `tns-8e9`).

Model (the spin-`S` generalisation of definitions.md D6, quoted not redefined):

    H = -J Σ_x ( S_x·S_{x+1} - S² ) ,   vacuum |Ω⟩ = |S,S,…⟩ ,  periodic ring.

In the magnon-number variables `n_x := S - S^z_x ∈ 0…2S` this is

    H = 2JS Σ_x n_x - J Σ_x n_x n_{x+1}
        - (J/2) Σ_x ( S⁺_x S⁻_{x+1} + h.c. ) ,

with ladder matrix elements `⟨n-1|S⁺|n⟩ = √(n(2S-n+1))`,
`⟨n+1|S⁻|n⟩ = √((n+1)(2S-n))`.  Hence a magnon hops between two EMPTY-target
sites with amplitude `-JS`, giving `ω(k) = 2JS(1-cos k)`, while the hop that
creates (or destroys) a doubly occupied site — which exists only for `S ≥ 1` —
carries the different amplitude `-J√(S(2S-1))`.

Two-magnon basis: unordered pairs `{x,y}`, `0 ≤ x ≤ y ≤ N-1`, with `x = y`
(double occupancy, `n_x = 2`) admitted iff `2S ≥ 2`.  Dimension `N(N+1)/2` for
`S ≥ 1` and `N(N-1)/2` at `S = 1/2`.

THE CONTACT ALGEBRA (derived in this shard, checked by `bethe_residual_bulk`).
Write the free extension `Ψ(x,y) = A e^{i(k₁x+k₂y)} + B e^{i(k₂x+k₁y)}` on all
of `ℤ²` — it is NOT symmetric under `x ↔ y` — and put `ψ(x,y) = Ψ(x,y)` for
`x < y`, `ψ_d(x) = γ P^x` with `P = z₁z₂`, `z_j = e^{ik_j}`.  Two configuration
classes fail the free equation and give two contact conditions.  With
`t = JS`, `g = J√(S(2S-1))`, `a = 1+z₁z₂`, `b = z₁+z₂`, `W = A z₂ + B z₁`,
`Σ = A + B`:

    (x,x)     [double occupancy, only 2 neighbours]  ⟹  γ = (g/t) W / b ,
    (x,x+1)   [adjacent pair, Ising bond + 2 contact hops]
              ⟹  g γ (1+P) = t Σ (1+P) - J W .

Eliminating `γ` and using `g²/t = J(2S-1)`:

    W [ (2S-1) a + b ] = S Σ a b ,

whose `S = 1/2` case is the familiar `2W = Σa`.  Hence, with `μ := (2S-1)a+b`,

    S₁₂ = A/B = ( S a b - z₁ μ ) / ( z₂ μ - S a b ) ,     |S₁₂| = 1 ,

which reduces to `-(z₁z₂-2z₁+1)/(z₁z₂-2z₂+1)` at `S = 1/2`.  Expanding at
`z₁ = 1 + i k_s`, both numerator and denominator equal `S(1+z₂)(z₂-1)` at
`k_s = 0` and their derivatives differ by `i(1+z₂)(z₂-1)`, so

    dδ/dk_s|₀ = Im(i/S) = 1/S       for every S and every hard momentum k_h.

The soft Wigner phase slope is therefore `1/s` — **not** the `S`-independent
`2`.  The module never assumes this: it builds the sector Hamiltonian by
independent enumeration and the tests confront it with a brute-force
`(2S+1)^N` build and with pure wavepacket dynamics.

Sign convention is inherited verbatim from `fm_twomagnon.jl` §2:
`Δ_s = -∂δ/∂k_s`, `Δ_h = -∂δ/∂k_h`, `δ = arg S₁₂`.

Only LinearAlgebra, SparseArrays, KrylovKit are used.  Standalone module,
included directly by `numerics/test/test_spins_twomagnon.jl`.
"""
module SpinSTwoMagnon

using LinearAlgebra
using SparseArrays
using KrylovKit

export spin_matrices, PairBasisS, pair_basis_s,
       one_magnon_hamiltonian_s, two_magnon_hamiltonian_s,
       omega_s, group_velocity_s, double_amplitude_ratio,
       smatrix_s, soft_phase_s, dphase_dk1_s, dphase_dk2_s, soft_slope_exact,
       smatrix, soft_phase, dphase_dk1, dphase_dk2, quantized_pair,
       bethe_vector_s, bethe_residual_bulk,
       gaussian_packet, momentum_weights, packet_velocity,
       packet_average_displacement, two_magnon_product_state,
       one_body_density, centroid, chamber_positions,
       evolve, plan_geometry, collision_run, richardson,
       soft_slope_at, soft_slope


include("spins_twomagnon_sector.jl")
include("spins_twomagnon_collision.jl")

end # module
