"""
spins_memory_sector.jl — sector enumeration, sparse Hamiltonian, observables and
state preparation for the easy-axis spin-`S` XXZ ferromagnet with a kink.
Shard 1 of the `SpinSMemory` module (`spins_memory.jl`); the protocol itself is
shard 2, `spins_memory_run.jl`.

The spin-`S` generalisation of `numerics/src/xxz_sector.jl` +
`xxz_dynamics.jl`, written as a separate shard so the frozen `S = 1/2` results
are untouched; `test_spins_memory.jl` confronts the two at `S = 1/2`.
Falsifier (B) of Conjecture Bc (theory/TRIANGLE.md §4, bd `tns-8e9`).

CONVENTIONS (identical to `numerics/docs/kink-sector-notes.md`, extended to
spin `S`):

    H = - Σ_{x=1}^{N-1} [ (J_⊥/2)(S⁺_x S⁻_{x+1} + h.c.) + J_z S^z_x S^z_{x+1} ],
    J_⊥ > 0,  Δ := J_z/J_⊥ > 1.

Sites `x = 1…N`; sites `1` and `N` carry FROZEN classical spins `S^z = +S` and
(`:kink`) `S^z = -S`, so hopping lives on the bonds between the `L = N-2`
dynamical sites and the total magnon number is exactly conserved.  A
configuration is a `Vector{Int8}` of MAGNON NUMBERS `n_j = S - S^z_j ∈ 0…2S`,
so `n = 0` is the ↑ vacuum and `n = 2S` the ↓ vacuum.

Dispersion: `ω(k) = 2SJ_⊥(Δ - cos k)`, `v(k) = 2SJ_⊥ sin k` (both reduce to the
`S = 1/2` forms `J_z - J_⊥cos k`, `J_⊥ sin k`).

TRUNCATION.  The `S = 1/2` shard counts domain walls; the spin-`S` analogue is
the UP-VARIATION

    D(c) := Σ_{j=1}^{L-1} max(0, n_j - n_{j+1}) ,

i.e. the total variation of `⟨S^z⟩` in the direction opposite to the kink.
`D = 0` is exactly the manifold of monotone walls of any width (the spin-`S`
kink family), `D ≤ 1` adds exactly one magnon on either side of the wall, and
`D ≤ 2` two.  Because the frozen ends are `n = 0` on the left and `n = 2S` on
the right, neither boundary bond ever contributes to `D`.  At `S = 1/2`,
`D = (#domain walls − 1)/2`, so `dmax = d` ⇔ the frozen shard's `dwmax = 2d+1`
— checked in the tests.

MEASUREMENT.  The wall position estimators are the `S = 1/2` ones with the
saturation value `±S` in place of `±1/2`:

    X̂₁ = Σ_x (x+½)[m(x)−m(x+1)] / Σ_x [m(x)−m(x+1)]      (gradient centroid)
    X̂₂ = (1/2S) Σ_{x∈W} m(x) + (x_a+x_b)/2                (integrated)
    R  = Σ_{x ≤ X−buf}(S − m(x)),  T = Σ_{x ≥ X+buf}(S + m(x))

`R` and `T` count magnons because a magnon is one unit of `S^z` at any `S`.
Theorem M-quant predicts `δx = −N_T/s`, i.e. `−1` site per transmitted magnon
at `S = 1` against `−2` at `S = 1/2`.
"""

# ---------------------------------------------------------------- chain ----

"""
    SpinChain(N; twoS=2, Jperp=1.0, Delta=2.0, boundary=:kink)

Easy-axis spin-`S = twoS/2` XXZ ferromagnet on `N` sites with frozen boundary
spins (`:kink` → `+S … −S`, `:up` → `+S … +S`).
"""
struct SpinChain
    N::Int
    twoS::Int
    Jperp::Float64
    Delta::Float64
    boundary::Symbol
    function SpinChain(N::Int; twoS::Int=2, Jperp::Real=1.0, Delta::Real=2.0,
                       boundary::Symbol=:kink)
        N >= 4 || throw(ArgumentError("need N >= 4"))
        twoS >= 1 || throw(ArgumentError("need 2S >= 1"))
        boundary in (:kink, :up) || throw(ArgumentError("boundary must be :kink or :up"))
        Jperp > 0 || throw(ArgumentError("Jperp must be positive"))
        new(N, twoS, float(Jperp), float(Delta), boundary)
    end
end

nsites_dynamical(ch::SpinChain) = ch.N - 2
Jz_of(ch::SpinChain) = ch.Delta * ch.Jperp
spin_of(ch::SpinChain) = ch.twoS / 2
"Frozen magnon number on site 1 (the ↑ vacuum)."
frozen_left_s(::SpinChain) = 0
"Frozen magnon number on site N."
frozen_right_s(ch::SpinChain) = ch.boundary === :kink ? ch.twoS : 0
"Physical site index (1…N) of dynamical site j (1…L)."
phys_site_s(::SpinChain, j::Int) = j + 1

"`ω(k) = 2SJ_⊥(Δ − cos k)`; gapped for Δ > 1."
magnon_dispersion_s(ch::SpinChain, k::Real) = ch.twoS * ch.Jperp * (ch.Delta - cos(k))
"`v(k) = dω/dk = 2SJ_⊥ sin k`."
magnon_velocity_s(ch::SpinChain, k::Real) = ch.twoS * ch.Jperp * sin(k)

"`⟨n−1|S⁺|n⟩ = √(n(2S−n+1))`."
@inline _raise(n::Integer, twoS::Integer) = sqrt(n * (twoS - n + 1))
"`⟨n+1|S⁻|n⟩ = √((n+1)(2S−n))`."
@inline _lower(n::Integer, twoS::Integer) = sqrt((n + 1) * (twoS - n))

"Magnon number at physical site `x` for the dynamical configuration `c`."
@inline function n_at(ch::SpinChain, c::AbstractVector{Int8}, x::Int)
    x == 1 && return frozen_left_s(ch)
    x == ch.N && return frozen_right_s(ch)
    return Int(c[x-1])
end

"""
    updown_variation(ch, c) = Σ_j max(0, n_j − n_{j+1})

The up-variation `D`: `0` on the monotone kink manifold, `+1` per magnon.
The frozen ends never contribute (left `n = 0`, right `n = 2S`), so only the
dynamical bonds enter.
"""
function updown_variation(::SpinChain, c::AbstractVector{Int8})
    d = 0
    @inbounds for j in 1:(length(c)-1)
        v = Int(c[j]) - Int(c[j+1])
        v > 0 && (d += v)
    end
    return d
end

"""    ising_energy_s(ch, c) = −J_z Σ_x S^z_x S^z_{x+1}  (frozen bonds included)."""
function ising_energy_s(ch::SpinChain, c::AbstractVector{Int8})
    jz = Jz_of(ch)
    S = spin_of(ch)
    e = 0.0
    for x in 1:(ch.N-1)
        e -= jz * (S - n_at(ch, c, x)) * (S - n_at(ch, c, x + 1))
    end
    return e
end

"""The monotone (`D = 0`) configuration with `nz` sites at `n = 2S` on the right."""
function monotone_kink_config(ch::SpinChain, nz::Int)
    L = nsites_dynamical(ch)
    0 <= nz <= L || throw(ArgumentError("nz out of range"))
    c = zeros(Int8, L)
    for j in (L-nz+1):L
        c[j] = Int8(ch.twoS)
    end
    return c
end

# ----------------------------------------------------------------- basis ----

"""
Ordered basis of the fixed-magnon-number sector, optionally truncated to
`D ≤ dmax` (`dmax = nothing` ⇒ the full, exact sector).  Configurations are
stored column-wise in `cols::Matrix{Int8}` (L × dim) for cache-friendly
observables; `index` is the inverse map.
"""
struct SectorBasisS
    chain::SpinChain
    ntot::Int
    dmax::Union{Int,Nothing}
    cols::Matrix{Int8}
    index::Dict{Vector{Int8},Int}
end

Base.length(b::SectorBasisS) = size(b.cols, 2)
"Configuration `j` of the basis, as a view into the storage matrix."
config(b::SectorBasisS, j::Integer) = @view b.cols[:, j]

"""
    sector_basis_s(ch; ntot, dmax=nothing)

Enumerate every configuration with `Σ_j n_j = ntot` and up-variation
`D ≤ dmax`.  Depth-first with two prunes — the remaining magnon capacity and
`D` itself — so the cost is `O(dim · L)`, never `O((2S+1)^L)`.
"""
function sector_basis_s(ch::SpinChain; ntot::Int, dmax::Union{Int,Nothing}=nothing)
    L = nsites_dynamical(ch)
    twoS = ch.twoS
    0 <= ntot <= twoS * L || throw(ArgumentError("ntot must lie in 0:$(twoS*L)"))
    dcap = dmax === nothing ? typemax(Int) : dmax
    dcap >= 0 || throw(ArgumentError("dmax must be ≥ 0"))
    out = Vector{Vector{Int8}}()
    cur = zeros(Int8, L)
    function rec(j::Int, s::Int, d::Int)
        if j > L
            s == ntot && push!(out, copy(cur))
            return
        end
        rem = L - j                                   # sites after this one
        for v in 0:twoS
            s2 = s + v
            s2 > ntot && break                        # s2 grows with v
            ntot - s2 > twoS * rem && continue        # cannot reach ntot any more
            d2 = j > 1 ? d + max(0, Int(cur[j-1]) - v) : d
            d2 > dcap && continue
            cur[j] = Int8(v)
            rec(j + 1, s2, d2)
        end
        return
    end
    rec(1, 0, 0)
    sort!(out)
    dim = length(out)
    cols = Matrix{Int8}(undef, L, dim)
    index = Dict{Vector{Int8},Int}()
    sizehint!(index, dim)
    for (i, c) in enumerate(out)
        cols[:, i] .= c
        index[c] = i
    end
    return SectorBasisS(ch, ntot, dmax, cols, index)
end

# ---------------------------------------------------------- Hamiltonian ----

"Apply the hop `j -> j+dir` to `c` in place, returning the amplitude (0 if illegal)."
@inline function _hop!(d::Vector{Int8}, c::AbstractVector{Int8}, j::Int, dir::Int,
                       twoS::Int, Jperp::Float64)
    t = j + dir
    na = Int(c[j]); nb = Int(c[t])
    (na == 0 || nb == twoS) && return 0.0
    amp = -(Jperp / 2) * _raise(na, twoS) * _lower(nb, twoS)
    copyto!(d, c)
    d[j] = Int8(na - 1)
    d[t] = Int8(nb + 1)
    return amp
end

"""
    build_hamiltonian_s(b) -> SparseMatrixCSC{Float64,Int}

Sparse `H` restricted to `b`.  Exact on an untruncated basis; on a truncated
one it is the Hermitian projection `P H P`, so unitarity and energy
conservation of the evolution stay exact.
"""
function build_hamiltonian_s(b::SectorBasisS)
    ch = b.chain
    L = nsites_dynamical(ch)
    twoS = ch.twoS
    dim = length(b)
    rows = Int[]; cols = Int[]; vals = Float64[]
    sizehint!(rows, 3 * dim); sizehint!(cols, 3 * dim); sizehint!(vals, 3 * dim)
    d = zeros(Int8, L)
    for i in 1:dim
        c = config(b, i)
        push!(rows, i); push!(cols, i); push!(vals, ising_energy_s(ch, c))
        for j in 1:L, dir in (-1, 1)
            (j + dir < 1 || j + dir > L) && continue
            amp = _hop!(d, c, j, dir, twoS, ch.Jperp)
            amp == 0.0 && continue
            k = get(b.index, d, 0)
            k == 0 && continue                 # truncated away: P H P drops it
            push!(rows, k); push!(cols, i); push!(vals, amp)
        end
    end
    return sparse(rows, cols, vals, dim, dim)
end

"""Frobenius norm of the matrix elements a truncated basis discards."""
function truncation_leakage_s(b::SectorBasisS)
    b.dmax === nothing && return 0.0
    ch = b.chain
    L = nsites_dynamical(ch)
    twoS = ch.twoS
    d = zeros(Int8, L)
    acc = 0.0
    for i in 1:length(b)
        c = config(b, i)
        for j in 1:L, dir in (-1, 1)
            (j + dir < 1 || j + dir > L) && continue
            amp = _hop!(d, c, j, dir, twoS, ch.Jperp)
            amp == 0.0 && continue
            haskey(b.index, d) || (acc += amp^2)
        end
    end
    return sqrt(acc)
end

# ---------------------------------------------------------- observables ----

"""⟨S^z_x⟩ for every physical site `x = 1…N` (frozen sites return ±S exactly)."""
function sz_profile_s(b::SectorBasisS, ψ::AbstractVector)
    ch = b.chain
    L = nsites_dynamical(ch)
    S = spin_of(ch)
    m = zeros(Float64, ch.N)
    m[1] = S - frozen_left_s(ch)
    m[ch.N] = S - frozen_right_s(ch)
    cols = b.cols
    @inbounds for i in 1:length(b)
        p = abs2(ψ[i])
        p == 0 && continue
        for j in 1:L
            m[j+1] += p * (S - cols[j, i])
        end
    end
    return m
end

@inline function _window_range(m::AbstractVector, window)
    xa = max(1, Int(window[1]))
    xb = min(length(m), Int(window[2]))
    xa < xb || throw(ArgumentError("empty measurement window"))
    return xa:xb
end

"""X̂₁: centroid of the magnetisation gradient inside `window` (scale-free in S)."""
function kink_position_centroid(m::AbstractVector; window)
    r = _window_range(m, window)
    num = 0.0; den = 0.0
    for x in first(r):(last(r)-1)
        w = m[x] - m[x+1]
        num += (x + 0.5) * w
        den += w
    end
    abs(den) < 1e-12 && return NaN
    return num / den
end

"""X̂₂ = (1/2S) Σ_{x∈W} m(x) + (x_a+x_b)/2 — exact on any sharp wall, linear in ψ."""
function kink_position_integrated(m::AbstractVector, twoS::Integer; window)
    r = _window_range(m, window)
    s = 0.0
    for x in r
        s += m[x]
    end
    return s / twoS + (first(r) + last(r)) / 2
end

"""X̂₃ (diagnostic): the magnetisation zero crossing nearest the window centre."""
function kink_position_crossing(m::AbstractVector; window)
    r = _window_range(m, window)
    mid = (first(r) + last(r)) / 2
    best = NaN; bestd = Inf
    for x in first(r):(last(r)-1)
        (m[x] >= 0 && m[x+1] < 0) || continue
        X = x + m[x] / (m[x] - m[x+1])
        d = abs(X - mid)
        d < bestd && (bestd = d; best = X)
    end
    return best
end

"""
    magnon_weights_s(m, twoS; kink_ref, buffer) -> (T, R, trapped)

`R = Σ_{x ≤ X−buf}(S − m(x))` counts magnons still on the ↑ side, `T =
Σ_{x ≥ X+buf}(S + m(x))` those that crossed to the ↓ side.  Both vanish
identically on a clean wall of either branch, at any `S`.
"""
function magnon_weights_s(m::AbstractVector, twoS::Integer; kink_ref::Real, buffer::Real=8)
    N = length(m)
    S = twoS / 2
    xl = floor(Int, kink_ref - buffer)
    xr = ceil(Int, kink_ref + buffer)
    R = 0.0
    for x in 1:min(xl, N)
        R += S - m[x]
    end
    T = 0.0
    for x in max(1, xr):N
        T += S + m[x]
    end
    return (T=T, R=R, trapped=1.0 - T - R)
end

"""Centre of mass of the magnon density `Σ_x n(x)` (used on the all-up chain)."""
function magnon_centroid(b::SectorBasisS, ψ::AbstractVector)
    ch = b.chain
    S = spin_of(ch)
    m = sz_profile_s(b, ψ)
    num = 0.0; den = 0.0
    for x in eachindex(m)
        w = S - m[x]
        num += x * w
        den += w
    end
    return num / den
end

# --------------------------------------------------------------- states ----

"""Lowest eigenpair of `P H P` on `b` (dense for small bases, Lanczos otherwise)."""
function sector_ground_state_s(b::SectorBasisS; tol::Real=1e-12, krylovdim::Int=40)
    H = build_hamiltonian_s(b)
    dim = length(b)
    if dim == 1
        return (H[1, 1], ComplexF64[1.0])
    elseif dim <= 400
        F = eigen(Symmetric(Matrix(H)))
        return (F.values[1], ComplexF64.(F.vectors[:, 1]))
    end
    x0 = zeros(Float64, dim)
    ch = b.chain
    twoS = ch.twoS
    seed = get(b.index, monotone_kink_config(ch, div(b.ntot, twoS)), 1)
    x0[seed] = 1.0
    for i in 1:dim
        x0[i] += 1e-3 * sin(0.7137 * i)
    end
    normalize!(x0)
    vals, vecs, info = eigsolve(H, x0, 1, :SR; ishermitian=true, tol=tol,
                                krylovdim=krylovdim, maxiter=400)
    info.converged >= 1 || @warn "sector_ground_state_s: Lanczos did not converge" info
    v = ComplexF64.(vecs[1])
    normalize!(v)
    return (real(vals[1]), v)
end

@inline wavepacket_amplitude(x::Real; k0::Real, x0::Real, sigma::Real) =
    cis(k0 * x) * exp(-(x - x0)^2 / (4 * sigma^2))

"""Single-magnon Gaussian packet on the all-up chain (`ntot = 1` sector)."""
function free_magnon_state_s(b::SectorBasisS; k0::Real, x0::Real, sigma::Real)
    b.ntot == 1 || throw(ArgumentError("free_magnon_state_s needs the ntot = 1 sector"))
    ch = b.chain
    L = nsites_dynamical(ch)
    ψ = zeros(ComplexF64, length(b))
    for i in 1:length(b)
        c = config(b, i)
        j = findfirst(!=(Int8(0)), c)
        ψ[i] = wavepacket_amplitude(phys_site_s(ch, j); k0=k0, x0=x0, sigma=sigma)
    end
    normalize!(ψ)
    return ψ
end

"""
    magnon_wavepacket_s(b, bkink, ψkink; k0, x0, sigma)

Act on the dressed kink with `O = Σ_x e^{ik₀x} e^{−(x−x₀)²/4σ²} S⁻_x`, project
onto the target basis `b` (one more magnon) and normalise.  Identical recipe to
the `S = 1/2` shard, with the spin-`S` ladder factor `√((n+1)(2S−n))`.
"""
function magnon_wavepacket_s(b::SectorBasisS, bkink::SectorBasisS, ψkink::AbstractVector;
                             k0::Real, x0::Real, sigma::Real)
    ch = b.chain
    b.ntot == bkink.ntot + 1 || throw(ArgumentError("target basis needs one more magnon"))
    L = nsites_dynamical(ch)
    twoS = ch.twoS
    ψ = zeros(ComplexF64, length(b))
    d = zeros(Int8, L)
    for i in 1:length(bkink)
        a = ψkink[i]
        a == 0 && continue
        c = config(bkink, i)
        for j in 1:L
            n = Int(c[j])
            n == twoS && continue
            copyto!(d, c)
            d[j] = Int8(n + 1)
            k = get(b.index, d, 0)
            k == 0 && continue
            ψ[k] += a * _lower(n, twoS) *
                    wavepacket_amplitude(phys_site_s(ch, j); k0=k0, x0=x0, sigma=sigma)
        end
    end
    nz = norm(ψ)
    nz > 0 || throw(ArgumentError("wavepacket has zero norm — check x0 / basis"))
    return ψ ./ nz
end

"""Fraction of `‖O ψkink‖²` that falls outside the truncated target basis."""
function magnon_wavepacket_leakage_s(b::SectorBasisS, bkink::SectorBasisS,
                                     ψkink::AbstractVector; k0::Real, x0::Real, sigma::Real)
    ch = b.chain
    L = nsites_dynamical(ch)
    twoS = ch.twoS
    full = Dict{Vector{Int8},ComplexF64}()
    d = zeros(Int8, L)
    for i in 1:length(bkink)
        a = ψkink[i]
        a == 0 && continue
        c = config(bkink, i)
        for j in 1:L
            n = Int(c[j])
            n == twoS && continue
            copyto!(d, c)
            d[j] = Int8(n + 1)
            key = copy(d)
            full[key] = get(full, key, 0.0 + 0im) + a * _lower(n, twoS) *
                        wavepacket_amplitude(phys_site_s(ch, j); k0=k0, x0=x0, sigma=sigma)
        end
    end
    tot = sum(abs2, values(full))
    kept = 0.0
    for (key, v) in full
        haskey(b.index, key) && (kept += abs2(v))
    end
    return tot > 0 ? 1 - kept / tot : 0.0
end

"""One Krylov step of `exp(-iH dt)ψ`."""
function krylov_evolve(H, ψ::AbstractVector, dt::Real; tol::Real=1e-14, krylovdim::Int=40)
    w, info = exponentiate(H, -im * dt, ComplexF64.(ψ);
                           ishermitian=true, tol=tol, krylovdim=krylovdim, maxiter=200)
    info.converged >= 1 || @warn "krylov_evolve: Krylov step did not converge" info
    return w
end
