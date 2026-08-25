"""
xxz_dynamics.jl — Krylov real-time evolution, magnon wavepackets, and kink
position estimators for the sparse S^z sectors built in `xxz_sector.jl`.

Coordinates.  Everything is expressed in PHYSICAL site coordinates x = 1…N
(frozen boundary sites included).  A kink position `X` is the coordinate of the
domain-wall BOND: `X = x + 1/2` means the wall sits between sites x and x+1.
The sharp kink with `n` down spins therefore has X = (N-2) - n + 3/2.

Two inequivalent kink-position estimators are provided (both exact on sharp
kinks, both linear in the state, but with different sensitivity to magnon
density leaking into the measurement window), plus a deliberately inequivalent
median estimator used as a systematic-error probe.  See
numerics/docs/kink-sector-notes.md for the definitions in prose.
"""

# ---------------------------------------------------------------------------
# Observables
# ---------------------------------------------------------------------------

"""
    sz_profile(b::SectorBasis, ψ) -> Vector{Float64}

⟨S^z_x⟩ for every physical site x = 1…N (frozen sites return ±1/2 exactly).
"""
function sz_profile(b::SectorBasis, ψ::AbstractVector)
    ch = b.chain
    L = nsites_dynamical(ch)
    m = zeros(Float64, ch.N)
    m[1] = frozen_left(ch) / 2
    m[ch.N] = frozen_right(ch) / 2
    for (i, c) in enumerate(b.configs)
        p = abs2(ψ[i])
        p == 0 && continue
        for j in 1:L
            m[j+1] += c[j] ? 0.5p : -0.5p
        end
    end
    return m
end

"Clamp a window `(xa, xb)` to the chain and return it as an integer range."
@inline function _window_range(m::AbstractVector, window)
    xa = max(1, Int(window[1]))
    xb = min(length(m), Int(window[2]))
    xa < xb || throw(ArgumentError("empty measurement window"))
    return xa:xb
end

"""
    kink_position_centroid(m; window) -> Float64

Estimator X̂₁: centroid of the discrete magnetisation gradient inside `window`,

    X̂₁ = Σ_x (x + 1/2) [m(x) - m(x+1)] / Σ_x [m(x) - m(x+1)],

the sum running over bonds x with both endpoints in the window.  Exact on any
sharp kink; for a mixture of sharp kinks it returns the weighted mean position.
Contaminated by magnon density inside the window (a magnon contributes a
gradient dipole that cancels in the denominator but not in the numerator).
"""
function kink_position_centroid(m::AbstractVector; window)
    r = _window_range(m, window)
    num = 0.0
    den = 0.0
    for x in first(r):(last(r)-1)
        w = m[x] - m[x+1]
        num += (x + 0.5) * w
        den += w
    end
    abs(den) < 1e-12 && return NaN
    return num / den
end

"""
    kink_position_integrated(m; window) -> Float64

Estimator X̂₂: the position at which the integrated magnetisation inside the
window crosses the half-way value between the two saturated values ±1/2.
Equivalently, the wall position of the sharp step that carries the same total
magnetisation over the window:

    X̂₂ = Σ_{x ∈ W} m(x) + (x_a + x_b)/2 .

Exact on sharp kinks and exactly linear in the state, but weighted differently
from X̂₁ (uniformly over the window rather than by the local gradient), so the
two disagree precisely when magnon density is still inside the window.  The
difference X̂₁ - X̂₂ is therefore used as the systematic-error estimate.
"""
function kink_position_integrated(m::AbstractVector; window)
    r = _window_range(m, window)
    s = 0.0
    for x in r
        s += m[x]
    end
    return s + (first(r) + last(r)) / 2
end

"""
    kink_position_crossing(m; window) -> Float64

Estimator X̂₃ (diagnostic, deliberately inequivalent): the point where the
magnetisation profile crosses the half-way value between its two saturated
values, i.e. where m(x) changes sign, obtained by linear interpolation on the
sign-changing bond closest to the window centre.  Exact on sharp kinks, but for
a mixture of two sharp kinks it is *quantised*: it jumps discontinuously from
one branch to the other as the branch weights cross 1/2.  X̂₃ is therefore NOT
interchangeable with X̂₁/X̂₂ at partial transmission; it is reported so that the
estimator-dependence of "the" kink position is visible in the results record.
"""
function kink_position_crossing(m::AbstractVector; window)
    r = _window_range(m, window)
    mid = (first(r) + last(r)) / 2
    best = NaN
    bestd = Inf
    for x in first(r):(last(r)-1)
        (m[x] >= 0 && m[x+1] < 0) || continue
        X = x + m[x] / (m[x] - m[x+1])
        d = abs(X - mid)
        if d < bestd
            bestd = d
            best = X
        end
    end
    return best
end

"""
    kink_position(m; window, estimator=:centroid)

Dispatch helper; `estimator ∈ (:centroid, :integrated, :crossing)`.
"""
function kink_position(m::AbstractVector; window, estimator::Symbol=:centroid)
    estimator === :centroid && return kink_position_centroid(m; window=window)
    estimator === :integrated && return kink_position_integrated(m; window=window)
    estimator === :crossing && return kink_position_crossing(m; window=window)
    throw(ArgumentError("unknown estimator $estimator"))
end

"""
    density_centroid(m) -> Float64

Centre of mass of the down-spin density Σ_x (1/2 - m(x)) over the whole chain.
Used for the free-magnon (all-up chain) tests, where it is the magnon position.
"""
function density_centroid(m::AbstractVector)
    num = 0.0
    den = 0.0
    for x in eachindex(m)
        w = 0.5 - m[x]
        num += x * w
        den += w
    end
    return num / den
end

"""
    magnon_weights(m; kink_ref, buffer) -> (T, R, trapped)

Operational transmission / reflection weights.  With frozen ↑ on the left and
↓ on the right, any *down*-spin density strictly to the left of the kink is a
magnon that stayed on the up side (reflected), and any *up*-spin density
strictly to the right is a magnon that crossed to the down side (transmitted):

    R = Σ_{x ≤ X_ref - buffer} (1/2 - m(x)),
    T = Σ_{x ≥ X_ref + buffer} (1/2 + m(x)),
    trapped = 1 - T - R.

Both integrals vanish identically on a clean kink of either branch, so T and R
are unambiguous once the buffer excludes the wall region.  `trapped` measures
amplitude still bound to / dressing the kink.
"""
function magnon_weights(m::AbstractVector; kink_ref::Real, buffer::Real=8)
    N = length(m)
    xl = floor(Int, kink_ref - buffer)
    xr = ceil(Int, kink_ref + buffer)
    R = 0.0
    for x in 1:min(xl, N)
        R += 0.5 - m[x]
    end
    T = 0.0
    for x in max(1, xr):N
        T += 0.5 + m[x]
    end
    return (T=T, R=R, trapped=1.0 - T - R)
end

# ---------------------------------------------------------------------------
# States
# ---------------------------------------------------------------------------

"""
    sector_ground_state(b; tol=1e-12) -> (E, ψ)

Lowest eigenpair of `P H P` on the basis `b`.  Dense `eigen` for small bases,
Lanczos (KrylovKit) otherwise, started deterministically from the sharp-kink
configuration so results are reproducible.
"""
function sector_ground_state(b::SectorBasis; tol::Real=1e-12, krylovdim::Int=40)
    H = build_hamiltonian(b)
    dim = length(b)
    if dim == 1
        return (H[1, 1], ComplexF64[1.0])
    elseif dim <= 400
        F = eigen(Symmetric(Matrix(H)))
        return (F.values[1], ComplexF64.(F.vectors[:, 1]))
    end
    x0 = zeros(Float64, dim)
    seed = get(b.index, sharp_kink_config(b.chain, b.ndown), 1)
    x0[seed] = 1.0
    for i in 1:dim                      # tiny deterministic perturbation
        x0[i] += 1e-3 * sin(0.7137 * i)
    end
    normalize!(x0)
    vals, vecs, info = eigsolve(H, x0, 1, :SR; ishermitian=true, tol=tol,
                                krylovdim=krylovdim, maxiter=400)
    info.converged >= 1 || @warn "sector_ground_state: Lanczos did not converge" info
    v = ComplexF64.(vecs[1])
    normalize!(v)
    return (real(vals[1]), v)
end

"""
    wavepacket_amplitude(x; k0, x0, sigma)

f(x) = exp(i k₀ x) exp(-(x-x₀)²/(4σ²)).  With this normalisation |f|² is a
Gaussian of standard deviation σ in position and the momentum distribution has
standard deviation 1/(2σ).
"""
@inline wavepacket_amplitude(x::Real; k0::Real, x0::Real, sigma::Real) =
    cis(k0 * x) * exp(-(x - x0)^2 / (4 * sigma^2))

"""
    free_magnon_state(b; k0, x0, sigma) -> Vector{ComplexF64}

Single-magnon Gaussian wavepacket on the all-up chain (`boundary = :up`,
`ndown = 1` sector), normalised.
"""
function free_magnon_state(b::SectorBasis; k0::Real, x0::Real, sigma::Real)
    b.ndown == 1 || throw(ArgumentError("free_magnon_state needs the ndown = 1 sector"))
    ch = b.chain
    ψ = zeros(ComplexF64, length(b))
    for (i, c) in enumerate(b.configs)
        j = findfirst(!, c)
        ψ[i] = wavepacket_amplitude(phys_site(ch, j); k0=k0, x0=x0, sigma=sigma)
    end
    normalize!(ψ)
    return ψ
end

"""
    magnon_wavepacket(b, bkink, ψkink; k0, x0, sigma) -> Vector{ComplexF64}

RECIPE (the one used throughout WP N2a).  Take the exact ground state `ψkink`
of the S^z sector with `n` down spins (the dressed kink — sharp at large Δ,
broadened at moderate Δ), and act with the modulated lowering operator

    O = Σ_x e^{i k₀ x} e^{-(x-x₀)²/(4σ²)} S⁻_x ,

then project onto the target basis `b` (the sector with n+1 down spins) and
normalise.  x₀ is chosen far to the left of the kink, in the ↑ region, so O
creates a genuine magnon rather than moving the wall.  The projection onto a
`dwmax`-truncated `b` discards the small amplitude in which S⁻ generates a
configuration with more domain walls than the truncation keeps; the discarded
weight is returned by `magnon_wavepacket_leakage`.
"""
function magnon_wavepacket(b::SectorBasis, bkink::SectorBasis, ψkink::AbstractVector;
                           k0::Real, x0::Real, sigma::Real)
    ch = b.chain
    b.ndown == bkink.ndown + 1 ||
        throw(ArgumentError("target basis must carry one more down spin"))
    L = nsites_dynamical(ch)
    ψ = zeros(ComplexF64, length(b))
    d = falses(L)
    for (i, c) in enumerate(bkink.configs)
        a = ψkink[i]
        a == 0 && continue
        for j in 1:L
            c[j] || continue                    # S⁻ needs an up spin
            copyto!(d, c)
            d[j] = false
            k = get(b.index, d, 0)
            k == 0 && continue
            ψ[k] += a * wavepacket_amplitude(phys_site(ch, j); k0=k0, x0=x0, sigma=sigma)
        end
    end
    nz = norm(ψ)
    nz > 0 || throw(ArgumentError("wavepacket has zero norm — check x0 / basis"))
    return ψ ./ nz
end

"""
    magnon_wavepacket_leakage(b, bkink, ψkink; k0, x0, sigma) -> Float64

Fraction of ‖O ψkink‖² that falls outside the truncated target basis `b`.
"""
function magnon_wavepacket_leakage(b::SectorBasis, bkink::SectorBasis,
                                   ψkink::AbstractVector; k0::Real, x0::Real, sigma::Real)
    ch = b.chain
    L = nsites_dynamical(ch)
    full = Dict{BitVector,ComplexF64}()
    d = falses(L)
    for (i, c) in enumerate(bkink.configs)
        a = ψkink[i]
        a == 0 && continue
        for j in 1:L
            c[j] || continue
            copyto!(d, c)
            d[j] = false
            key = copy(d)
            full[key] = get(full, key, 0.0 + 0im) +
                        a * wavepacket_amplitude(phys_site(ch, j); k0=k0, x0=x0, sigma=sigma)
        end
    end
    tot = sum(abs2, values(full))
    kept = 0.0
    for (key, v) in full
        haskey(b.index, key) && (kept += abs2(v))
    end
    return tot > 0 ? 1 - kept / tot : 0.0
end

# ---------------------------------------------------------------------------
# Time evolution
# ---------------------------------------------------------------------------

"""
    krylov_evolve(H, ψ, dt; tol=1e-14, krylovdim=40) -> ψ'

One Krylov step of exp(-i H dt) ψ via `KrylovKit.exponentiate`.
"""
function krylov_evolve(H, ψ::AbstractVector, dt::Real; tol::Real=1e-14, krylovdim::Int=40)
    w, info = exponentiate(H, -im * dt, ComplexF64.(ψ);
                           ishermitian=true, tol=tol, krylovdim=krylovdim, maxiter=200)
    info.converged >= 1 || @warn "krylov_evolve: Krylov step did not converge" info
    return w
end

"""
    evolve_trajectory(observer, H, ψ0, dt, nsteps; kwargs...) -> Vector

Evolve `ψ0` for `nsteps` steps of size `dt`, calling `observer(t, ψ)` at t = 0
and after every step; returns the vector of observer values (length nsteps+1).
Written to be used with `do`-block syntax.
"""
function evolve_trajectory(observer, H, ψ0::AbstractVector, dt::Real, nsteps::Int;
                           tol::Real=1e-14, krylovdim::Int=40)
    ψ = ComplexF64.(ψ0)
    out = Any[observer(0.0, ψ)]
    for s in 1:nsteps
        ψ = krylov_evolve(H, ψ, dt; tol=tol, krylovdim=krylovdim)
        push!(out, observer(s * dt, ψ))
    end
    return [o for o in out]
end
