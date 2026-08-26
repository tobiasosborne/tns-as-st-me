"""
    Spin1Memory

Kink + magnon memory experiment on the **spin-s** easy-axis XXZ ferromagnet,
written to test prediction P8 of `corner-b-draft.md` §9 — the second, independent
falsifier of Conjecture Bc (`theory/TRIANGLE.md` §4, bd `tns-8e9`).

Conventions are exactly those of `xxz_sector.jl` / `xxz_dynamics.jl`, generalised
from `s = 1/2` to arbitrary `s`:

    H = - Σ_{x=1}^{N-1} [ (J_⊥/2)(S⁺_x S⁻_{x+1} + S⁻_x S⁺_{x+1}) + J_z S^z_x S^z_{x+1} ],
    J_⊥ > 0,  Δ := J_z/J_⊥ > 1,  sites x = 1…N, sites 1 and N FROZEN
    (`:kink` → `S^z_1 = +s`, `S^z_N = −s`;  `:up` → both `+s`).

A dynamical configuration is a `Vector{UInt8}` of length `L = N−2` holding the
on-site magnon number `n_x = s − S^z_x ∈ 0…2s`.  Total `Σ n_x` is conserved.

**Truncation.**  `xxz_sector.jl` truncates by domain-wall count, which is a
spin-1/2 notion.  The invariant generalisation used here is the number of
*excitations above a pure wall*,

    D(n) := Σ_x max(0, n_x − n_{x+1})   (frozen ends included),

i.e. the total upward variation of `S^z` left to right.  A monotone (pure kink)
configuration has `D = 0`; a kink plus one magnon, on either side, has `D = 1`;
`D` counts a doubly flipped site as two magnons.  For `s = 1/2`,
`D = (domain walls − 1)/2`, so `dmax = 1` is exactly `dwmax = 3` and `dmax = 2`
is `dwmax = 5` — the frozen spin-1/2 bases are reproduced configuration for
configuration (tested).

**The observable.**  `X̂₂` of `xxz_dynamics.jl` generalises to

    X̂₂ = (Σ_{x∈W} ⟨S^z_x⟩)/(2s) + (x_a + x_b)/2 ,

the wall coordinate of the sharp step carrying the same windowed magnetisation.
`S^z` bookkeeping then makes the memory law an exact statement: with `R + T = 1`,
`Σ_W ⟨S^z⟩` changes by `−2T` across the collision, hence

    δx = −T/s = −N_T/s ,

`−2` sites per transmitted magnon at `s = 1/2` and `−1` at `s = 1`.
"""
module Spin1Memory

using LinearAlgebra
using SparseArrays
using KrylovKit
using Printf

import TriangleMPS: trajectory_offset, krylov_evolve

export SpinChain, nsites_dynamical, Jz, frozen_left, frozen_right, sz_at,
       tv_excitations, SpinSectorBasis, sector_basis, build_hamiltonian,
       truncation_leakage, sharp_kink_config,
       magnon_dispersion, magnon_velocity,
       sz_profile, kink_position_centroid, kink_position_integrated,
       kink_position_crossing, magnon_weights,
       sector_ground_state, magnon_wavepacket, magnon_wavepacket_leakage,
       free_magnon_velocity, SpinMemoryResult, memory_experiment, to_json,
       trajectory_offset, krylov_evolve

# ---------------------------------------------------------------------------
# Chain
# ---------------------------------------------------------------------------

"""
    SpinChain(N; s=1.0, Jperp=1.0, Delta=2.0, boundary=:kink)

Easy-axis spin-`s` XXZ ferromagnet on `N` sites with frozen boundary spins.
"""
struct SpinChain
    N::Int
    s::Float64
    nmax::Int              # 2s, the maximum on-site magnon number
    Jperp::Float64
    Delta::Float64
    boundary::Symbol
    function SpinChain(N::Int; s::Real = 1.0, Jperp::Real = 1.0, Delta::Real = 2.0,
                       boundary::Symbol = :kink)
        N >= 4 || throw(ArgumentError("need N >= 4"))
        boundary in (:kink, :up) || throw(ArgumentError("boundary must be :kink or :up"))
        Jperp > 0 || throw(ArgumentError("Jperp must be positive"))
        nmax = Int(round(2s))
        nmax == 2s || throw(ArgumentError("s must be a half-integer"))
        new(N, float(s), nmax, float(Jperp), float(Delta), boundary)
    end
end

nsites_dynamical(ch::SpinChain) = ch.N - 2
Jz(ch::SpinChain) = ch.Delta * ch.Jperp
frozen_left(ch::SpinChain) = 0                                   # n = 0, S^z = +s
frozen_right(ch::SpinChain) = ch.boundary === :kink ? ch.nmax : 0

"Magnon number at physical site `x` (1…N) for the dynamical configuration `c`."
@inline function occ_at(ch::SpinChain, c::AbstractVector{UInt8}, x::Int)
    x == 1 && return frozen_left(ch)
    x == ch.N && return frozen_right(ch)
    return Int(c[x-1])
end

"`⟨S^z_x⟩ = s − n_x` at physical site `x`."
@inline sz_at(ch::SpinChain, c::AbstractVector{UInt8}, x::Int) = ch.s - occ_at(ch, c, x)

"""
    tv_excitations(ch, c) = Σ_x max(0, n_x − n_{x+1})

Number of excitations above a pure wall (frozen ends included).  Zero exactly on
monotone configurations; `1` for a kink plus one magnon on either side.
"""
function tv_excitations(ch::SpinChain, c::AbstractVector{UInt8})
    d = 0
    for x in 1:(ch.N - 1)
        a = occ_at(ch, c, x)
        b = occ_at(ch, c, x + 1)
        a > b && (d += a - b)
    end
    return d
end

"""
    ising_energy(ch, c) = -J_z Σ_x S^z_x S^z_{x+1}   (frozen bonds included)
"""
function ising_energy(ch::SpinChain, c::AbstractVector{UInt8})
    jz = Jz(ch)
    e = 0.0
    for x in 1:(ch.N - 1)
        e -= jz * sz_at(ch, c, x) * sz_at(ch, c, x + 1)
    end
    return e
end

"""
    sharp_kink_config(ch, nmag)

The narrowest monotone configuration with total magnon number `nmag`:
`0…0 r (2s)…(2s)` with at most one intermediate site.
"""
function sharp_kink_config(ch::SpinChain, nmag::Int)
    L = nsites_dynamical(ch)
    0 <= nmag <= ch.nmax * L || throw(ArgumentError("nmag out of range"))
    c = zeros(UInt8, L)
    b, r = divrem(nmag, ch.nmax)
    for j in (L - b + 1):L
        c[j] = UInt8(ch.nmax)
    end
    r > 0 && (c[L-b] = UInt8(r))
    return c
end

"Single-magnon energy `ω(k) = 2s J_⊥(Δ − cos k)` above the all-up vacuum."
magnon_dispersion(ch::SpinChain, k::Real) = 2 * ch.s * ch.Jperp * (ch.Delta - cos(k))

"Group velocity `dω/dk = 2s J_⊥ sin k`."
magnon_velocity(ch::SpinChain, k::Real) = 2 * ch.s * ch.Jperp * sin(k)

# ---------------------------------------------------------------------------
# Basis enumeration
# ---------------------------------------------------------------------------

"""
    SpinSectorBasis

Ordered basis of the fixed-`Σn` sector, optionally truncated to `D ≤ dmax`
(`dmax = nothing` ⇒ the full, exact sector).
"""
struct SpinSectorBasis
    chain::SpinChain
    nmag::Int
    dmax::Union{Int,Nothing}
    configs::Vector{Vector{UInt8}}
    index::Dict{Vector{UInt8},Int}
end

Base.length(b::SpinSectorBasis) = length(b.configs)

"""
    sector_basis(ch; nmag, dmax=1)

Enumerate the sector with total magnon number `nmag`, keeping only
configurations with `tv_excitations ≤ dmax`.  Built left to right with pruning
on both the running excitation count and the reachable magnon budget, so the
cost is proportional to the number of surviving configurations, not to
`(2s+1)^L`.
"""
function sector_basis(ch::SpinChain; nmag::Int, dmax::Union{Int,Nothing} = 1)
    L = nsites_dynamical(ch)
    nmax = ch.nmax
    0 <= nmag <= nmax * L || throw(ArgumentError("nmag must lie in 0:$(nmax*L)"))
    cap = dmax === nothing ? typemax(Int) : dmax
    nR = frozen_right(ch)
    out = Vector{Vector{UInt8}}()
    cur = zeros(UInt8, L)

    # site index x runs over the DYNAMICAL sites 1…L; `prev` is the occupation
    # of the site to the left (physical x, i.e. dynamical x-1 or the frozen end)
    function rec(j::Int, prev::Int, d::Int, acc::Int)
        if j > L
            dd = d + max(0, prev - nR)               # closing frozen bond
            dd <= cap && acc == nmag && push!(out, copy(cur))
            return
        end
        rem = L - j + 1
        for n in 0:nmax
            acc + n > nmag && break                  # acc only grows with n
            nmag - (acc + n) > nmax * (rem - 1) && continue
            dn = d + max(0, prev - n)
            dn > cap && continue
            cur[j] = UInt8(n)
            rec(j + 1, n, dn, acc + n)
        end
        return
    end

    rec(1, frozen_left(ch), 0, 0)
    sort!(out)
    index = Dict{Vector{UInt8},Int}()
    sizehint!(index, length(out))
    for (i, c) in enumerate(out)
        index[c] = i
    end
    return SpinSectorBasis(ch, nmag, dmax, out, index)
end

# ---------------------------------------------------------------------------
# Sparse Hamiltonian
# ---------------------------------------------------------------------------

"Hop amplitude for moving one magnon from occupation `na` onto occupation `nb`."
@inline function _hop_amp(Jperp::Float64, s::Float64, na::Int, nb::Int)
    return -(Jperp / 2) * sqrt(na * (2s - na + 1)) * sqrt((nb + 1) * (2s - nb))
end

"""
    build_hamiltonian(b) -> SparseMatrixCSC{Float64,Int}

`H` restricted to `b`.  Exact on an untruncated basis; on a `dmax`-truncated
basis it is the projection `P H P`, still Hermitian, so unitarity and energy
conservation of the evolution stay exact.
"""
function build_hamiltonian(b::SpinSectorBasis)
    ch = b.chain
    L = nsites_dynamical(ch)
    s = ch.s
    nmax = ch.nmax
    rows = Int[]; cols = Int[]; vals = Float64[]
    sizehint!(rows, 4 * length(b)); sizehint!(cols, 4 * length(b))
    sizehint!(vals, 4 * length(b))
    d = zeros(UInt8, L)
    for (i, c) in enumerate(b.configs)
        push!(rows, i); push!(cols, i); push!(vals, ising_energy(ch, c))
        for j in 1:(L - 1)
            for (a, bb) in ((j, j + 1), (j + 1, j))
                na = Int(c[a]); nb = Int(c[bb])
                (na >= 1 && nb < nmax) || continue
                copyto!(d, c)
                d[a] = UInt8(na - 1); d[bb] = UInt8(nb + 1)
                k = get(b.index, d, 0)
                k == 0 && continue          # truncated away: P H P drops it
                push!(rows, k); push!(cols, i); push!(vals, _hop_amp(ch.Jperp, s, na, nb))
            end
        end
    end
    return sparse(rows, cols, vals, length(b), length(b))
end

"""
    truncation_leakage(b) -> Float64

Frobenius norm of the matrix elements discarded because the target
configuration falls outside a truncated basis.
"""
function truncation_leakage(b::SpinSectorBasis)
    b.dmax === nothing && return 0.0
    ch = b.chain
    L = nsites_dynamical(ch)
    nmax = ch.nmax
    acc = 0.0
    d = zeros(UInt8, L)
    for c in b.configs
        for j in 1:(L - 1)
            for (a, bb) in ((j, j + 1), (j + 1, j))
                na = Int(c[a]); nb = Int(c[bb])
                (na >= 1 && nb < nmax) || continue
                copyto!(d, c)
                d[a] = UInt8(na - 1); d[bb] = UInt8(nb + 1)
                haskey(b.index, d) || (acc += _hop_amp(ch.Jperp, ch.s, na, nb)^2)
            end
        end
    end
    return sqrt(acc)
end

include("spin1_memory_run.jl")

end # module
