"""
spins_twomagnon_sector.jl — on-site spin-`S` operators, the two-magnon pair
basis, the sector Hamiltonians, and the exact spin-`S` two-magnon S-matrix.
Shard 1 of the `SpinSTwoMagnon` module (`spins_twomagnon.jl`); the wavepacket
collision experiment is shard 2, `spins_twomagnon_collision.jl`.

The model, the contact algebra that fixes `S_12`, and the resulting
`dδ/dk_s|₀ = 1/S` are documented in the module docstring of
`spins_twomagnon.jl`.
"""

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

