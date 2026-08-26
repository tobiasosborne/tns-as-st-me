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

# ------------------------------------------------------------- operators ----

"""
    spin_matrices(twoS) -> (Sx, Sy, Sz, Sp, Sm)

Dense on-site spin operators for `S = twoS/2` in the MAGNON-NUMBER basis
`n = S - m = 0…2S` (so `|n=0⟩` is the ferromagnetic vacuum).
"""
function spin_matrices(twoS::Integer)
    twoS >= 1 || throw(ArgumentError("need 2S ≥ 1"))
    d = Int(twoS) + 1
    S = twoS / 2
    Sz = zeros(ComplexF64, d, d)
    Sp = zeros(ComplexF64, d, d)
    for n in 0:twoS
        Sz[n+1, n+1] = S - n
        n >= 1 && (Sp[n, n+1] = sqrt(n * (twoS - n + 1)))   # ⟨n-1|S⁺|n⟩
    end
    Sm = Matrix(Sp')
    Sx = (Sp + Sm) / 2
    Sy = (Sp - Sm) / (2im)
    return Sx, Sy, Sz, Sp, Sm
end

"`⟨n-1|S⁺|n⟩ = √(n(2S-n+1))`."
@inline raise_coeff(n::Integer, twoS::Integer) = sqrt(n * (twoS - n + 1))
"`⟨n+1|S⁻|n⟩ = √((n+1)(2S-n))`."
@inline lower_coeff(n::Integer, twoS::Integer) = sqrt((n + 1) * (twoS - n))

"""
    double_amplitude_ratio(k1, k2, twoS) -> γ/1

Coefficient `γ` of the doubly occupied amplitude `ψ_d(x) = γ P^x`, `P = z₁z₂`,
of the two-plane-wave Bethe state normalised to `B = 1` (i.e. `A = S₁₂`).  From
the `(x,x)` contact condition, `γ = (g/t)·W/b` with `g/t = √((2S-1)/S)`,
`W = A z₂ + B z₁`, `b = z₁+z₂`.  Zero at `S = 1/2` (no double occupancy).
"""
function double_amplitude_ratio(k1::Real, k2::Real, twoS::Integer)
    twoS == 1 && return zero(ComplexF64)
    S = twoS / 2
    z1, z2 = cis(k1), cis(k2)
    A = smatrix_s(k1, k2, twoS)
    W = A * z2 + z1
    return sqrt((twoS - 1) / S) * W / (z1 + z2)
end

# ----------------------------------------------------------------- basis ----

"""Unordered-pair basis `{(x,y) : 0 ≤ x ≤ y ≤ N-1}` (`x = y` only if `2S ≥ 2`)."""
struct PairBasisS
    N::Int
    twoS::Int
    dim::Int
    pairs::Vector{Tuple{Int,Int}}
    index::Matrix{Int}
end

function pair_basis_s(N::Integer, twoS::Integer)
    N >= 4 || throw(ArgumentError("need N ≥ 4"))
    twoS >= 1 || throw(ArgumentError("need 2S ≥ 1"))
    doubles = twoS >= 2
    pairs = Tuple{Int,Int}[]
    index = zeros(Int, N, N)
    n = 0
    for x in 0:N-1, y in x:N-1
        (x == y && !doubles) && continue
        n += 1
        push!(pairs, (x, y))
        index[x+1, y+1] = n
        index[y+1, x+1] = n
    end
    return PairBasisS(Int(N), Int(twoS), n, pairs, index)
end

# --------------------------------------------------- sector Hamiltonians ----

"Single-magnon energy `ω(k) = 2JS(1-cos k) = twoS·J(1-cos k)`."
omega_s(k::Real, J::Real, twoS::Integer) = twoS * J * (1 - cos(k))
"Group velocity `dω/dk = 2JS sin k`."
group_velocity_s(k::Real, J::Real, twoS::Integer) = twoS * J * sin(k)

"""
One-magnon block: on-site energy `2JS` and hopping `-JS` on a ring of `N`
sites; the unique nontrivial spin-`S` input is the ladder product
`√(2S)·√(2S) = 2S`.
"""
function one_magnon_hamiltonian_s(N::Integer, J::Real, twoS::Integer)
    t = J * twoS / 2                      # = J S
    I_ = Int[]; K = Int[]; V = Float64[]
    for x in 0:N-1
        push!(I_, x + 1); push!(K, x + 1); push!(V, 2 * t)
        for d in (-1, 1)
            y = mod(x + d, N)
            push!(I_, y + 1); push!(K, x + 1); push!(V, -t)
        end
    end
    return sparse(I_, K, V, N, N)
end

"Occupancy of site `b` in the configuration `(x,y)`."
@inline _occ(b::Int, x::Int, y::Int) = (b == x ? 1 : 0) + (b == y ? 1 : 0)

"""
Two-magnon block of `H`, by direct enumeration of the pair basis.  Diagonal
`4JS - J·Σ_bond n n`, hopping amplitude
`-(J/2)√(n_a(2S-n_a+1))·√((n_b+1)(2S-n_b))` for moving one magnon from an
occupied site `a` to an adjacent site `b`.  Distinct occupied sites only: the
bosonic factor `√(n_a(2S-n_a+1))` already carries the multiplicity.
"""
function two_magnon_hamiltonian_s(pb::PairBasisS, J::Real, twoS::Integer)
    twoS == pb.twoS || throw(ArgumentError("basis built for a different 2S"))
    N = pb.N
    S = twoS / 2
    I_ = Int[]; K = Int[]; V = Float64[]
    sizehint!(I_, 5 * pb.dim); sizehint!(K, 5 * pb.dim); sizehint!(V, 5 * pb.dim)
    for (col, (x, y)) in enumerate(pb.pairs)
        # diagonal: 2JS per magnon, minus J for each bond carrying both
        nn = 0
        if x != y
            (mod(y - x, N) == 1 || mod(x - y, N) == 1) && (nn += 1)
        end
        push!(I_, col); push!(K, col); push!(V, 4 * J * S - J * nn)
        sites = x == y ? ((x, 2),) : ((x, 1), (y, 1))
        for (a, na) in sites
            for d in (-1, 1)
                b = mod(a + d, N)
                nb = _occ(b, x, y)
                nb >= twoS && continue                    # target already full
                amp = -(J / 2) * raise_coeff(na, twoS) * lower_coeff(nb, twoS)
                amp == 0 && continue
                # move one magnon a -> b
                other = (x == y) ? x : (a == x ? y : x)
                p, q = minmax(other, b)
                row = pb.index[p+1, q+1]
                row == 0 && continue
                push!(I_, row); push!(K, col); push!(V, amp)
            end
        end
    end
    return sparse(I_, K, V, pb.dim, pb.dim)
end

# ------------------------------------------------- exact Bethe quantities ----

"""
    smatrix_s(k1, k2, twoS)

Two-magnon coefficient ratio `S₁₂ = A₁₂/A₂₁` for spin `S = twoS/2`:

    S₁₂ = (S a b - z₁ μ)/(z₂ μ - S a b),
    a = 1+z₁z₂,  b = z₁+z₂,  μ = (2S-1)a + b.

`|S₁₂| = 1` for real momenta; at `S = 1/2` it reduces to the frozen
`-(z₁z₂-2z₁+1)/(z₁z₂-2z₂+1)`.
"""
function smatrix_s(k1::Real, k2::Real, twoS::Integer)
    S = twoS / 2
    z1, z2 = cis(k1), cis(k2)
    a = 1 + z1 * z2
    b = z1 + z2
    μ = (twoS - 1) * a + b
    return (S * a * b - z1 * μ) / (z2 * μ - S * a * b)
end

"""Continuous phase branch `δ = arg S₁₂` with `δ(0,k_h) = 0` (D7)."""
soft_phase_s(k1::Real, k2::Real, twoS::Integer) = angle(smatrix_s(k1, k2, twoS))

"`∂ log S₁₂` with respect to `k₁` and `k₂`; purely imaginary since `|S₁₂| = 1`."
function _dlogS_s(k1::Real, k2::Real, twoS::Integer)
    S = twoS / 2
    z1, z2 = cis(k1), cis(k2)
    a = 1 + z1 * z2
    b = z1 + z2
    μ = (twoS - 1) * a + b
    a1 = im * z1 * z2; b1 = im * z1; μ1 = (twoS - 1) * a1 + b1
    a2 = im * z1 * z2; b2 = im * z2; μ2 = (twoS - 1) * a2 + b2
    P = S * a * b
    P1 = S * (a1 * b + a * b1)
    P2 = S * (a2 * b + a * b2)
    num = P - z1 * μ
    den = z2 * μ - P
    num1 = P1 - (im * z1 * μ + z1 * μ1)
    den1 = z2 * μ1 - P1
    num2 = P2 - z1 * μ2
    den2 = im * z2 * μ + z2 * μ2 - P2
    return (num1 / num - den1 / den, num2 / num - den2 / den)
end

dphase_dk1_s(k1::Real, k2::Real, twoS::Integer) = imag(_dlogS_s(k1, k2, twoS)[1])
dphase_dk2_s(k1::Real, k2::Real, twoS::Integer) = imag(_dlogS_s(k1, k2, twoS)[2])

"""Soft Wigner phase slope `dδ/dk_s` at `k_s = 0`; analytically `1/S`."""
soft_slope_exact(kh::Real, twoS::Integer) = dphase_dk1_s(0.0, kh, twoS)

# `S = 1/2` aliases, kept so the frozen conventions of fm_twomagnon.jl read the same.
smatrix(k1::Real, k2::Real) = smatrix_s(k1, k2, 1)
soft_phase(k1::Real, k2::Real) = soft_phase_s(k1, k2, 1)
dphase_dk1(k1::Real, k2::Real) = dphase_dk1_s(k1, k2, 1)
dphase_dk2(k1::Real, k2::Real) = dphase_dk2_s(k1, k2, 1)

"""Bethe--Yang quantisation on the ring by fixed-point iteration."""
function quantized_pair(N::Integer, n1::Integer, n2::Integer, twoS::Integer = 1;
                        iters::Int = 400, tol::Float64 = 1e-14)
    k1 = 2π * n1 / N
    k2 = 2π * n2 / N
    for _ in 1:iters
        d = soft_phase_s(k1, k2, twoS)
        nk1 = (2π * n1 + d) / N
        nk2 = (2π * n2 - d) / N
        done = abs(nk1 - k1) < tol && abs(nk2 - k2) < tol
        k1, k2 = nk1, nk2
        done && break
    end
    return k1, k2
end

"Unnormalised coordinate-Bethe amplitudes on the pair basis (`B = 1`, `A = S₁₂`)."
function _bethe_amplitudes(pb::PairBasisS, k1::Real, k2::Real, twoS::Integer)
    A = smatrix_s(k1, k2, twoS)
    γ = double_amplitude_ratio(k1, k2, twoS)
    K = k1 + k2
    v = Vector{ComplexF64}(undef, pb.dim)
    for (m, (x, y)) in enumerate(pb.pairs)
        v[m] = x == y ? γ * cis(K * x) :
               A * cis(k1 * x + k2 * y) + cis(k2 * x + k1 * y)
    end
    return v
end

"""
Coordinate-Bethe vector for spin `S`: `Ψ(x,y) = S₁₂ e^{i(k₁x+k₂y)} +
e^{i(k₂x+k₁y)}` on `x < y`, and `ψ_d(x) = γ e^{i(k₁+k₂)x}`.
"""
function bethe_vector_s(pb::PairBasisS, k1::Real, k2::Real, twoS::Integer)
    v = _bethe_amplitudes(pb, k1, k2, twoS)
    return v / norm(v)
end

"""
    bethe_residual_bulk(N, J, twoS, k1, k2; margin)

Largest `|(H₂ψ - Eψ)_m|` over configurations whose two sites both lie in
`[margin, N-1-margin]`, with `ψ` the (unnormalised) coordinate-Bethe vector and
`E = ω(k₁)+ω(k₂)`.  No quantisation is imposed, so this tests ONLY the
boundary condition and the double-occupancy weight — the analytic content of
falsifier (A).  Normalised by `max|ψ|` on the same configurations.
"""
function bethe_residual_bulk(N::Integer, J::Real, twoS::Integer,
                             k1::Real, k2::Real; margin::Int = 3)
    pb = pair_basis_s(N, twoS)
    H2 = two_magnon_hamiltonian_s(pb, J, twoS)
    ψ = _bethe_amplitudes(pb, k1, k2, twoS)
    E = omega_s(k1, J, twoS) + omega_s(k2, J, twoS)
    r = H2 * ψ - E * ψ
    lo, hi = margin, N - 1 - margin
    worst = 0.0
    scale = 0.0
    for (m, (x, y)) in enumerate(pb.pairs)
        (lo <= x <= hi && lo <= y <= hi) || continue
        worst = max(worst, abs(r[m]))
        scale = max(scale, abs(ψ[m]))
    end
    return worst / max(scale, eps())
end

# ------------------------------------------------------------ wavepackets ----

"""Normalised Gaussian packet on the ring, `|φ|²` of width `σx`, momentum `k`."""
function gaussian_packet(N::Integer, k::Real, X::Real, σx::Real)
    φ = Vector{ComplexF64}(undef, N)
    for x in 0:N-1
        d = x - X
        d -= N * round(d / N)
        φ[x+1] = exp(-d^2 / (4σx^2)) * cis(k * x)
    end
    return φ / norm(φ)
end

"""Momentum-space weights `|⟨k|φ⟩|²` on the ring momenta `k ∈ (-π,π]`."""
function momentum_weights(φ::AbstractVector)
    N = length(φ)
    ks = Vector{Float64}(undef, N)
    w = Vector{Float64}(undef, N)
    for n in 0:N-1
        k = 2π * n / N
        k = k > π ? k - 2π : k
        ks[n+1] = k
        a = zero(ComplexF64)
        @inbounds for x in 0:N-1
            a += φ[x+1] * cis(-k * x)
        end
        w[n+1] = abs2(a) / N
    end
    return ks, w ./ sum(w)
end

"Packet-averaged group velocity `⟨2JS sin k⟩`."
function packet_velocity(φ::AbstractVector, J::Real, twoS::Integer)
    ks, w = momentum_weights(φ)
    return sum(w .* (twoS .* J .* sin.(ks)))
end

"""
Packet-averaged displacement predictions `(Δ_s, Δ_h)` from the exact S-matrix.
Because `|S₁₂| = 1` the centroid shift is exactly the `|g|²`-weighted average
of `-∂δ/∂k`, so this removes the finite-width systematic.
"""
function packet_average_displacement(φs::AbstractVector, φh::AbstractVector,
                                     twoS::Integer; cut::Float64 = 1e-9)
    k1s, w1 = momentum_weights(φs)
    k2s, w2 = momentum_weights(φh)
    i1 = findall(>(cut * maximum(w1)), w1)
    i2 = findall(>(cut * maximum(w2)), w2)
    Δs = 0.0; Δh = 0.0; Z = 0.0
    for a in i1, b in i2
        d1, d2 = _dlogS_s(k1s[a], k2s[b], twoS)
        (isfinite(d1) && isfinite(d2)) || continue
        w = w1[a] * w2[b]
        Δs -= w * imag(d1)
        Δh -= w * imag(d2)
        Z += w
    end
    return Δs / Z, Δh / Z
end

"""
Two-magnon in-state from two spatially disjoint single-particle packets: the
symmetrised product on `x < y`, and zero double-occupancy amplitude.  The
neglected diagonal weight is bounded by the packet overlap
`max_x |φ_L(x)φ_R(x)| ≲ e^{-D²/(4σ²)}` (`< 10^{-10}` at the separations used
here) and is regenerated dynamically during the collision.
"""
function two_magnon_product_state(pb::PairBasisS, φL::AbstractVector, φR::AbstractVector)
    ψ = Vector{ComplexF64}(undef, pb.dim)
    for (m, (x, y)) in enumerate(pb.pairs)
        ψ[m] = x == y ? zero(ComplexF64) :
               φL[x+1] * φR[y+1] + φR[x+1] * φL[y+1]
    end
    return ψ / norm(ψ)
end

"""Single-particle density `n(x)`, total mass 2 (a double counts twice)."""
function one_body_density(pb::PairBasisS, ψ::AbstractVector)
    n = zeros(Float64, pb.N)
    @inbounds for (m, (x, y)) in enumerate(pb.pairs)
        p = abs2(ψ[m])
        n[x+1] += p
        n[y+1] += p
    end
    return n
end

centroid(n::AbstractVector) = sum((0:length(n)-1) .* n) / sum(n)

"""Chamber positions `(⟨x⟩, ⟨y⟩)`: mean position of the left / right magnon."""
function chamber_positions(pb::PairBasisS, ψ::AbstractVector)
    sx = 0.0; sy = 0.0; z = 0.0
    @inbounds for (m, (x, y)) in enumerate(pb.pairs)
        p = abs2(ψ[m])
        sx += x * p; sy += y * p; z += p
    end
    return sx / z, sy / z
end

# ------------------------------------------------------------- evolution ----

function step(H, ψ::AbstractVector, dt::Real; krylovdim::Int = 40, tol::Real = 1e-12)
    w, info = exponentiate(H, -im * dt, ψ; ishermitian = true,
                           krylovdim = krylovdim, tol = tol, eager = true)
    return w, info
end

function evolve(H, ψ::AbstractVector, T::Real; dt::Real = 1.0, kwargs...)
    ψ = ComplexF64.(ψ)
    nst = max(1, round(Int, T / dt))
    h = T / nst
    for _ in 1:nst
        ψ, _ = step(H, ψ, h; kwargs...)
    end
    return ψ
end

"""Ring layout for a collision; identical geometry rule to `fm_twomagnon.jl`."""
function plan_geometry(; J::Real, twoS::Integer, ks::Real, kh::Real, σx::Real,
                       sep_factor::Real = 10.0, pad_factor::Real = 8.0)
    vs = group_velocity_s(ks, J, twoS)
    vh = group_velocity_s(kh, J, twoS)
    vrel = vh - vs
    vrel > 0 || throw(ArgumentError("D7 requires v(k_h) > v(k_s); got vh=$vh vs=$vs"))
    D = sep_factor * σx
    T = 2D / vrel
    pad = ceil(Int, pad_factor * σx) + 2
    lo = min(0.0, vh * T, D, D + vs * T)
    hi = max(0.0, vh * T, D, D + vs * T)
    Xh = pad - lo
    N = ceil(Int, hi + Xh + pad) + 1
    return (N = N, Xh = Xh, Xs = Xh + D, T = T, tc = T / 2,
            vs = vs, vh = vh, vrel = vrel, D = D, pad = pad)
end

"""
    collision_run(; J, twoS, ks, kh, sigma_x, sep_factor, dt, ...)

Dynamical extraction of the two-magnon displacement at spin `S = twoS/2`: the
interacting pair and two free single-magnon references are evolved in lockstep
and the chamber marginals of the interacting state are compared with those of
the free product state.  No S-matrix enters the measurement.
"""
function collision_run(; J::Real = 1.0, twoS::Integer = 2, ks::Real, kh::Real,
                       sigma_x::Real = 8.0, sep_factor::Real = 10.0,
                       dt::Real = 1.0, krylovdim::Int = 40, tol::Real = 1e-12)
    σx = sigma_x
    geo = plan_geometry(; J = J, twoS = twoS, ks = ks, kh = kh, σx = σx,
                        sep_factor = sep_factor)
    N = geo.N
    pb = pair_basis_s(N, twoS)
    H2 = two_magnon_hamiltonian_s(pb, J, twoS)
    H1 = one_magnon_hamiltonian_s(N, J, twoS)

    φs = gaussian_packet(N, ks, geo.Xs, σx)
    φh = gaussian_packet(N, kh, geo.Xh, σx)
    ψ = two_magnon_product_state(pb, φh, φs)

    n0 = norm(ψ)
    E0 = real(dot(ψ, H2 * ψ))
    us = ComplexF64.(φs)
    uh = ComplexF64.(φh)

    nst = max(4, round(Int, geo.T / dt))
    h = geo.T / nst

    ts = Float64[]; ds = Float64[]; dh = Float64[]
    normdrift = 0.0; energydrift = 0.0; krylov_ok = true

    function record!(t)
        xi, yi = chamber_positions(pb, ψ)
        ref = two_magnon_product_state(pb, uh, us)
        xf, yf = chamber_positions(pb, ref)
        push!(ts, t)
        if t < geo.tc
            push!(dh, xi - xf); push!(ds, yi - yf)
        else
            push!(ds, xi - xf); push!(dh, yi - yf)
        end
    end

    record!(0.0)
    for j in 1:nst
        ψ, i2 = step(H2, ψ, h; krylovdim = krylovdim, tol = tol)
        us, ia = step(H1, us, h; krylovdim = krylovdim, tol = tol)
        uh, ib = step(H1, uh, h; krylovdim = krylovdim, tol = tol)
        krylov_ok &= (i2.converged > 0 && ia.converged > 0 && ib.converged > 0)
        normdrift = max(normdrift, abs(norm(ψ) - n0))
        energydrift = max(energydrift,
                          abs(real(dot(ψ, H2 * ψ)) / n0^2 - E0) / max(abs(E0), eps()))
        record!(j * h)
    end

    late = findall(t -> t >= geo.tc + 0.6 * (geo.T - geo.tc), ts)
    pre = findall(t -> t <= 0.4 * geo.tc, ts)
    pas, pah = packet_average_displacement(φs, φh, twoS)

    return (; N, dim = pb.dim, J, twoS, ks, kh, σx, sep_factor,
            T = geo.T, tc = geo.tc, dt = h, nsteps = nst,
            vs = geo.vs, vh = geo.vh,
            delta_s = ds[end], delta_h = dh[end],
            delta_s_spread = maximum(ds[late]) - minimum(ds[late]),
            delta_h_spread = maximum(dh[late]) - minimum(dh[late]),
            delta_s_pre = isempty(pre) ? NaN : sum(ds[pre]) / length(pre),
            delta_h_pre = isempty(pre) ? NaN : sum(dh[pre]) / length(pre),
            pred_s_exact = -dphase_dk1_s(ks, kh, twoS),
            pred_h_exact = -dphase_dk2_s(ks, kh, twoS),
            pred_s_avg = pas, pred_h_avg = pah,
            norm_drift = normdrift, energy_drift = energydrift,
            krylov_ok = krylov_ok, times = ts, traj_s = ds, traj_h = dh)
end

"""Two-point extrapolation to zero packet width (bias is linear in `1/σx²`)."""
function richardson(σa::Real, va::Real, σb::Real, vb::Real)
    ua, ub = 1 / σa^2, 1 / σb^2
    B = (va - vb) / (ua - ub)
    return va - B * ua
end

"""
    soft_slope_at(; J, twoS, ks, kh, sigmas, sep_factor, dt)

Symmetrised soft phase slope AT FINITE `k_s`, from pure dynamics.  Runs `±k_s`
at each packet width, Richardson-extrapolates each in `1/σx²`, then takes
`slope(k_s) = -(Δ_s(+k_s) + Δ_s(-k_s))/2`.  The `±` average cancels the `O(k_s)`
term of `dδ/dk_s` exactly, leaving `slope(k_s) = dδ/dk_s|₀ + O(k_s²)`.
"""
function soft_slope_at(; J::Real = 1.0, twoS::Integer = 2, ks::Real = 0.30,
                       kh::Real = 1.5, sigmas = (8.0, 11.0),
                       sep_factor::Real = 10.0, dt::Real = 1.0)
    σ = collect(float.(sigmas))
    length(σ) >= 2 || throw(ArgumentError("need ≥ 2 packet widths"))
    rp = [collision_run(; J = J, twoS = twoS, ks = abs(ks), kh = kh, sigma_x = s,
                        sep_factor = sep_factor, dt = dt) for s in σ]
    rm = [collision_run(; J = J, twoS = twoS, ks = -abs(ks), kh = kh, sigma_x = s,
                        sep_factor = sep_factor, dt = dt) for s in σ]
    Δp = richardson(σ[end-1], rp[end-1].delta_s, σ[end], rp[end].delta_s)
    Δm = richardson(σ[end-1], rm[end-1].delta_s, σ[end], rm[end].delta_s)
    slope = -(Δp + Δm) / 2
    pp = [richardson(σ[i], rp[i].delta_s, σ[j], rp[j].delta_s)
          for i in 1:length(σ)-1 for j in i+1:length(σ)]
    pm = [richardson(σ[i], rm[i].delta_s, σ[j], rm[j].delta_s)
          for i in 1:length(σ)-1 for j in i+1:length(σ)]
    spread = max(maximum(pp) - minimum(pp), maximum(pm) - minimum(pm))
    drift = max(rp[end].delta_s_spread, rm[end].delta_s_spread)
    exact = (dphase_dk1_s(abs(ks), kh, twoS) + dphase_dk1_s(-abs(ks), kh, twoS)) / 2
    all = vcat(rp, rm)
    return (; slope, err = max(spread, drift), exact_symmetrised = exact,
            delta_s_plus = Δp, delta_s_minus = Δm,
            raw_plus = [r.delta_s for r in rp], raw_minus = [r.delta_s for r in rm],
            avg_plus = [r.pred_s_avg for r in rp], avg_minus = [r.pred_s_avg for r in rm],
            sigmas = σ, ks = abs(ks), kh, twoS, J,
            N = rp[end].N, dim = rp[end].dim,
            norm_drift = maximum(r.norm_drift for r in all),
            energy_drift = maximum(r.energy_drift for r in all),
            pre_control = maximum(abs(r.delta_s_pre) for r in all),
            krylov_ok = all_ok(all))
end

all_ok(rs) = reduce(&, (r.krylov_ok for r in rs); init = true)

"""
    soft_slope(; J, twoS, kss, kh, sigmas, sep_factor, dt)

The soft Wigner phase slope `dδ/dk_s|₀` from PURE DYNAMICS: `soft_slope_at` at
each `k_s ∈ kss`, then a linear fit of `slope(k_s)` against `k_s²` extrapolated
to `k_s = 0`.  `err` is the larger of (i) the spread of the pairwise `k_s²`
extrapolations and (ii) the largest per-`k_s` error bar.
"""
function soft_slope(; J::Real = 1.0, twoS::Integer = 2, kss = (0.30, 0.20),
                    kh::Real = 1.5, sigmas = (8.0, 11.0),
                    sep_factor::Real = 10.0, dt::Real = 1.0)
    ks = collect(float.(kss))
    length(ks) >= 2 || throw(ArgumentError("need ≥ 2 soft momenta"))
    pts = [soft_slope_at(; J = J, twoS = twoS, ks = k, kh = kh, sigmas = sigmas,
                         sep_factor = sep_factor, dt = dt) for k in ks]
    m = [p.slope for p in pts]
    u = ks .^ 2
    ext(i, j) = m[i] - (m[i] - m[j]) / (u[i] - u[j]) * u[i]
    cand = [ext(i, j) for i in 1:length(ks)-1 for j in i+1:length(ks)]
    slope0 = ext(argmax(u), argmin(u))
    err = max(maximum(cand) - minimum(cand), maximum(p.err for p in pts))
    return (; slope = slope0, err = err, points = pts, kss = ks, kh, twoS, J,
            slopes_at = m, exact_at = [p.exact_symmetrised for p in pts],
            exact_limit = soft_slope_exact(kh, twoS),
            krylov_ok = reduce(&, (p.krylov_ok for p in pts); init = true))
end

end # module
