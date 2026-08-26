# spin1_memory_run.jl — observables, states and the magnon-through-kink protocol
# for the spin-s easy-axis chain.  Included by src/spin1_memory.jl; continues
# module Spin1Memory (no module wrapper of its own — the TriangleMPS.jl shard
# convention).
#
# Protocol (identical to memory_experiment.jl, generalised in s):
#   1. kink = ground state of the sector with `nmag = s L` down-weight;
#   2. add an incoming magnon far to its LEFT with Σ_x f(x) S⁻_x, k₀ > 0;
#   3. Krylov-evolve until the outgoing amplitude is clear of the wall;
#   4. record ⟨S^z_x⟩, the wall estimators X̂₁ X̂₂ X̂₃, and the operational T/R;
#   5. δx = difference of the pre- and post-collision ballistic fits at t_c.

# ---------------------------------------------------------------------------
# Observables
# ---------------------------------------------------------------------------

"`⟨S^z_x⟩` for every physical site x = 1…N (frozen sites return ±s exactly)."
function sz_profile(b::SpinSectorBasis, ψ::AbstractVector)
    ch = b.chain
    L = nsites_dynamical(ch)
    m = zeros(Float64, ch.N)
    m[1] = ch.s - frozen_left(ch)
    m[ch.N] = ch.s - frozen_right(ch)
    for (i, c) in enumerate(b.configs)
        p = abs2(ψ[i])
        p == 0 && continue
        for j in 1:L
            m[j+1] += p * (ch.s - c[j])
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

"""
    kink_position_centroid(m; window)

Estimator X̂₁: centroid of the discrete magnetisation gradient inside `window`.
Scale-free, hence independent of `s`; contaminated by magnon density inside the
window, so it is reported as a systematic-error probe next to X̂₂.
"""
function kink_position_centroid(m::AbstractVector; window)
    r = _window_range(m, window)
    num = 0.0; den = 0.0
    for x in first(r):(last(r) - 1)
        w = m[x] - m[x+1]
        num += (x + 0.5) * w
        den += w
    end
    abs(den) < 1e-12 && return NaN
    return num / den
end

"""
    kink_position_integrated(m, s; window)

Estimator X̂₂ (the one the memory law is stated for):

    X̂₂ = (Σ_{x∈W} m(x))/(2s) + (x_a + x_b)/2 ,

the wall coordinate of the sharp step carrying the same windowed magnetisation.
Exactly linear in the state and exact on every monotone wall, sharp or not.
"""
function kink_position_integrated(m::AbstractVector, s::Real; window)
    r = _window_range(m, window)
    acc = 0.0
    for x in r
        acc += m[x]
    end
    return acc / (2s) + (first(r) + last(r)) / 2
end

"""
    kink_position_crossing(m; window)

Estimator X̂₃ (diagnostic, deliberately inequivalent): linear interpolation of
the `m = 0` crossing nearest the window centre.  Quantised on mixtures, so NOT
interchangeable with X̂₁/X̂₂ at partial transmission.
"""
function kink_position_crossing(m::AbstractVector; window)
    r = _window_range(m, window)
    mid = (first(r) + last(r)) / 2
    best = NaN; bestd = Inf
    for x in first(r):(last(r) - 1)
        (m[x] >= 0 && m[x+1] < 0) || continue
        X = x + m[x] / (m[x] - m[x+1])
        d = abs(X - mid)
        if d < bestd
            bestd = d; best = X
        end
    end
    return best
end

"""
    magnon_weights(m, s; kink_ref, buffer) -> (T, R, trapped)

Operational transmission / reflection weights.  `s − m(x)` is the magnon density
above the ↑ vacuum and `s + m(x)` the magnon density above the ↓ vacuum, so

    R = Σ_{x ≤ X_ref − buffer} (s − m(x)),
    T = Σ_{x ≥ X_ref + buffer} (s + m(x)),

both vanish identically on a clean wall of either branch, and both count magnon
NUMBER (not magnetisation) for every `s`.
"""
function magnon_weights(m::AbstractVector, s::Real; kink_ref::Real, buffer::Real = 8)
    N = length(m)
    xl = floor(Int, kink_ref - buffer)
    xr = ceil(Int, kink_ref + buffer)
    R = 0.0
    for x in 1:min(xl, N)
        R += s - m[x]
    end
    T = 0.0
    for x in max(1, xr):N
        T += s + m[x]
    end
    return (T = T, R = R, trapped = 1.0 - T - R)
end

# ---------------------------------------------------------------------------
# States
# ---------------------------------------------------------------------------

"""
    sector_ground_state(b; tol=1e-12) -> (E, ψ)

Lowest eigenpair of `P H P`.  Dense `eigen` for small bases, Lanczos otherwise,
started deterministically from the narrowest monotone wall.
"""
function sector_ground_state(b::SpinSectorBasis; tol::Real = 1e-12, krylovdim::Int = 40)
    H = build_hamiltonian(b)
    dim = length(b)
    dim == 1 && return (H[1, 1], ComplexF64[1.0])
    if dim <= 400
        F = eigen(Symmetric(Matrix(H)))
        return (F.values[1], ComplexF64.(F.vectors[:, 1]))
    end
    x0 = zeros(Float64, dim)
    seed = get(b.index, sharp_kink_config(b.chain, b.nmag), 1)
    x0[seed] = 1.0
    for i in 1:dim
        x0[i] += 1e-3 * sin(0.7137 * i)
    end
    normalize!(x0)
    vals, vecs, info = eigsolve(H, x0, 1, :SR; ishermitian = true, tol = tol,
                                krylovdim = krylovdim, maxiter = 400)
    info.converged >= 1 || @warn "sector_ground_state: Lanczos did not converge" info
    v = ComplexF64.(vecs[1])
    normalize!(v)
    return (real(vals[1]), v)
end

"`f(x) = e^{ik₀x} e^{−(x−x₀)²/(4σ²)}`."
@inline wavepacket_amplitude(x::Real; k0::Real, x0::Real, sigma::Real) =
    cis(k0 * x) * exp(-(x - x0)^2 / (4 * sigma^2))

"""
    magnon_wavepacket(b, bkink, ψkink; k0, x0, sigma)

Act with `O = Σ_x e^{ik₀x} e^{−(x−x₀)²/(4σ²)} S⁻_x` on the kink state, project on
the target basis `b` (one more magnon) and normalise.  `S⁻` raises the on-site
magnon number with the exact `√((n+1)(2s−n))` matrix element, so for `s ≥ 1` it
can also make a doubly flipped site; with `x₀` far in the ↑ region that amplitude
is negligible, and whatever is projected away is reported by
`magnon_wavepacket_leakage`.
"""
function magnon_wavepacket(b::SpinSectorBasis, bkink::SpinSectorBasis,
                           ψkink::AbstractVector; k0::Real, x0::Real, sigma::Real)
    ch = b.chain
    b.nmag == bkink.nmag + 1 ||
        throw(ArgumentError("target basis must carry one more magnon"))
    L = nsites_dynamical(ch)
    nmax = ch.nmax
    ψ = zeros(ComplexF64, length(b))
    d = zeros(UInt8, L)
    for (i, c) in enumerate(bkink.configs)
        a = ψkink[i]
        a == 0 && continue
        for j in 1:L
            n = Int(c[j])
            n < nmax || continue
            copyto!(d, c)
            d[j] = UInt8(n + 1)
            k = get(b.index, d, 0)
            k == 0 && continue
            ψ[k] += a * sqrt((n + 1) * (2 * ch.s - n)) *
                    wavepacket_amplitude(j + 1; k0 = k0, x0 = x0, sigma = sigma)
        end
    end
    nz = norm(ψ)
    nz > 0 || throw(ArgumentError("wavepacket has zero norm — check x0 / basis"))
    return ψ ./ nz
end

"Fraction of `‖Oψ_kink‖²` that falls outside the truncated target basis `b`."
function magnon_wavepacket_leakage(b::SpinSectorBasis, bkink::SpinSectorBasis,
                                   ψkink::AbstractVector; k0::Real, x0::Real, sigma::Real)
    ch = b.chain
    L = nsites_dynamical(ch)
    nmax = ch.nmax
    full = Dict{Vector{UInt8},ComplexF64}()
    d = zeros(UInt8, L)
    for (i, c) in enumerate(bkink.configs)
        a = ψkink[i]
        a == 0 && continue
        for j in 1:L
            n = Int(c[j])
            n < nmax || continue
            copyto!(d, c)
            d[j] = UInt8(n + 1)
            key = copy(d)
            full[key] = get(full, key, 0.0 + 0im) +
                        a * sqrt((n + 1) * (2 * ch.s - n)) *
                        wavepacket_amplitude(j + 1; k0 = k0, x0 = x0, sigma = sigma)
        end
    end
    tot = sum(abs2, values(full))
    kept = 0.0
    for (key, v) in full
        haskey(b.index, key) && (kept += abs2(v))
    end
    return tot > 0 ? 1 - kept / tot : 0.0
end

"""
    free_magnon_velocity(; N, s, Delta, k0, sigma, x0, T, dt)

Measured centroid velocity of a single magnon packet on the all-up chain.  Used
as an independent check of `magnon_velocity` (test of the dispersion, not of the
kink physics).
"""
function free_magnon_velocity(; N::Int, s::Real = 1.0, Jperp::Real = 1.0,
                              Delta::Real = 2.0, k0::Real, sigma::Real,
                              x0::Real, T::Real, dt::Real = 0.25)
    ch = SpinChain(N; s = s, Jperp = Jperp, Delta = Delta, boundary = :up)
    b = sector_basis(ch; nmag = 1, dmax = 1)
    H = build_hamiltonian(b)
    ψ = zeros(ComplexF64, length(b))
    for (i, c) in enumerate(b.configs)
        j = findfirst(!=(0x00), c)
        ψ[i] = wavepacket_amplitude(j + 1; k0 = k0, x0 = x0, sigma = sigma)
    end
    normalize!(ψ)
    dens(v) = begin
        m = sz_profile(b, v)
        num = 0.0; den = 0.0
        for x in eachindex(m)
            w = ch.s - m[x]
            num += x * w; den += w
        end
        num / den
    end
    c0 = dens(ψ)
    nst = max(1, round(Int, T / dt))
    h = T / nst
    for _ in 1:nst
        ψ = krylov_evolve(H, ψ, h)
    end
    return (dens(ψ) - c0) / T
end

# ---------------------------------------------------------------------------
# The experiment
# ---------------------------------------------------------------------------

"Results record of one magnon-through-kink run at spin `s`."
struct SpinMemoryResult
    params::NamedTuple
    times::Vector{Float64}
    X1::Vector{Float64}
    X2::Vector{Float64}
    X3::Vector{Float64}
    Tw::Vector{Float64}
    Rw::Vector{Float64}
    trapped::Vector{Float64}
    norms::Vector{Float64}
    energies::Vector{Float64}
    dx1::Float64
    dx2::Float64
    dx3::Float64
    slope_pre1::Float64
    slope_post1::Float64
    T_final::Float64
    R_final::Float64
    trapped_final::Float64
    T_init::Float64
    R_init::Float64
    ratio1::Float64
    ratio2::Float64
    ratio2_sub::Float64
    tcollision::Float64
    pre_window::Tuple{Float64,Float64}
    post_window::Tuple{Float64,Float64}
    dim::Int
    leakage_init::Float64
    leakage_H::Float64
end

"""
    memory_experiment(; N, s, Delta, Jperp=1.0, k0, sigma, standoff, dmax=1,
                        dt=0.4, tmax=nothing, halfwidth=8, buffer=8,
                        kink_state=:ground, trapped_tol=1e-4, obs_every=1)

Run the protocol.  Returns a `SpinMemoryResult`; `ratio2 = δx₂/N_T` is the
number Conjecture Bc is about (`−1/s` if the memory quantum is the asymptotic
charge datum).
"""
function memory_experiment(; N::Int, s::Real = 1.0, Delta::Real, Jperp::Real = 1.0,
                           k0::Real, sigma::Real = 4.0, standoff::Real = 28.0,
                           dmax::Union{Int,Nothing} = 1, dt::Real = 0.4,
                           tmax::Union{Real,Nothing} = nothing,
                           halfwidth::Int = 8, buffer::Real = 8,
                           kink_state::Symbol = :ground, trapped_tol::Real = 1e-4,
                           obs_every::Int = 1, verbose::Bool = false)
    ch = SpinChain(N; s = s, Jperp = Jperp, Delta = Delta, boundary = :kink)
    L = nsites_dynamical(ch)
    iseven(L) || throw(ArgumentError("need an even number of dynamical sites"))
    nk = ch.nmax * (L ÷ 2)                 # sharp kink centred on the chain
    Xk0 = float(L ÷ 2) + 1.5               # wall bond, physical coordinates
    x0 = Xk0 - standoff
    x0 - 3 * sigma > 1 || throw(ArgumentError("packet too close to the left edge; " *
                                             "increase N or reduce standoff/sigma"))

    bk = kink_state === :sharp ? sector_basis(ch; nmag = nk, dmax = 0) :
         sector_basis(ch; nmag = nk, dmax = dmax)
    _, ψk = sector_ground_state(bk)
    b = sector_basis(ch; nmag = nk + 1, dmax = dmax)
    leak0 = magnon_wavepacket_leakage(b, bk, ψk; k0 = k0, x0 = x0, sigma = sigma)
    ψ0 = magnon_wavepacket(b, bk, ψk; k0 = k0, x0 = x0, sigma = sigma)
    H = build_hamiltonian(b)
    leakH = truncation_leakage(b)

    v = magnon_velocity(ch, k0)
    tc = standoff / max(abs(v), 1e-12)
    reach = max(halfwidth, buffer) + 3 * sigma
    tclear = reach / max(abs(v), 1e-12)
    settle = max(10 * dt, 2 * sigma / max(abs(v), 1e-12))
    Tmax = tmax === nothing ? tc + tclear + settle : float(tmax)
    nsteps = max(8, ceil(Int, Tmax / dt))
    Tmax = nsteps * dt
    if tmax === nothing
        Xk0 + abs(v) * (Tmax - tc) + 3 * sigma > N - 1 &&
            throw(ArgumentError("chain too short: the outgoing packet would hit the " *
                                "right boundary; increase N or reduce standoff/sigma"))
    end
    window = (max(1, round(Int, Xk0) - halfwidth), min(N, round(Int, Xk0) + halfwidth))

    times = Float64[]; X1 = Float64[]; X2 = Float64[]; X3 = Float64[]
    Tw = Float64[]; Rw = Float64[]; trp = Float64[]
    nrm = Float64[]; ens = Float64[]

    record! = function (t, ψ)
        m = sz_profile(b, ψ)
        push!(times, t)
        push!(X1, kink_position_centroid(m; window = window))
        push!(X2, kink_position_integrated(m, ch.s; window = window))
        push!(X3, kink_position_crossing(m; window = window))
        w = magnon_weights(m, ch.s; kink_ref = Xk0, buffer = buffer)
        push!(Tw, w.T); push!(Rw, w.R); push!(trp, w.trapped)
        push!(nrm, norm(ψ))
        push!(ens, real(dot(ψ, H * ψ)))
        return nothing
    end

    ψ = ComplexF64.(ψ0)
    record!(0.0, ψ)
    for st in 1:nsteps
        ψ = krylov_evolve(H, ψ, dt)
        (st % obs_every == 0 || st == nsteps) && record!(st * dt, ψ)
    end
    verbose && @printf("N=%d s=%.1f Δ=%.2f k0=%.3f dim=%d steps=%d T=%.5f\n",
                       N, ch.s, Delta, k0, length(b), nsteps, Tw[end])

    tend = times[end]
    tc_used = clamp(tc, 0.0, tend)
    geo_pre = (0.0, clamp(tc - tclear, 2 * dt, 0.45 * tend))
    geo_post = (clamp(tc + tclear, 0.55 * tend, tend - 2 * dt), tend)
    ipre = something(findfirst(i -> trp[i] > trapped_tol, eachindex(trp)),
                     length(trp) + 1) - 1
    ipost = something(findlast(i -> trp[i] > trapped_tol, eachindex(trp)), 0) + 1
    pre = (ipre >= 5) ? (0.0, times[ipre]) : geo_pre
    post = (ipost <= length(times) - 4) ? (times[ipost], tend) : geo_post
    o1 = trajectory_offset(times, X1, tc_used, pre, post)
    o2 = trajectory_offset(times, X2, tc_used, pre, post)
    o3 = trajectory_offset(times, X3, tc_used, pre, post)

    params = (N = N, L = L, spin = ch.s, nmag = nk + 1, Delta = float(Delta),
              Jperp = float(Jperp), k0 = float(k0), sigma = float(sigma),
              standoff = float(standoff), x0 = x0, Xkink0 = Xk0,
              dmax = (dmax === nothing ? -1 : dmax), kink_state = String(kink_state),
              dt = float(dt), tmax = tend, nsteps = nsteps,
              halfwidth = halfwidth, buffer = float(buffer),
              trapped_tol = float(trapped_tol),
              vgroup = v, omega = magnon_dispersion(ch, k0),
              prediction_ratio = -1 / ch.s)

    # T and R are read against the INITIAL state, not against a bare vacuum: on a
    # truncation that admits virtual pairs (dmax ≥ 2) the dressed kink already
    # carries a little weight on both sides, and the memory law is about the
    # CHANGE in transmitted magnon number.  At dmax = 1 the initial weights are
    # exactly (T,R) = (0,1) and the subtraction is a no-op.
    Tf = Tw[end]
    dT = Tf - Tw[1]
    r1 = Tf > 1e-12 ? o1.dx / Tf : NaN
    r2 = Tf > 1e-12 ? o2.dx / Tf : NaN
    r2s = abs(dT) > 1e-12 ? o2.dx / dT : NaN
    return SpinMemoryResult(params, times, X1, X2, X3, Tw, Rw, trp, nrm, ens,
                            o1.dx, o2.dx, o3.dx, o1.slope_pre, o1.slope_post,
                            Tf, Rw[end], trp[end], Tw[1], Rw[1], r1, r2, r2s, tc_used,
                            (float(pre[1]), float(pre[2])),
                            (float(post[1]), float(post[2])),
                            length(b), leak0, leakH)
end

# ---------------------------------------------------------------------------
# Minimal JSON emitter (no external dependency; NaN/Inf -> null)
# ---------------------------------------------------------------------------

_jnum(x::Real) = isfinite(x) ? (isinteger(x) && abs(x) < 1e15 ?
                                string(Int(round(x))) : @sprintf("%.12g", x)) : "null"
_jnum(x::Integer) = string(x)
_jval(x::Real) = _jnum(x)
_jval(x::Integer) = string(x)
_jval(x::AbstractString) = "\"" * replace(String(x), "\\" => "\\\\", "\"" => "\\\"") * "\""
_jval(x::Symbol) = _jval(String(x))
_jval(v::AbstractVector) = "[" * join(_jval.(v), ",") * "]"
_jval(nt::NamedTuple) = "{" * join(["\"$k\":" * _jval(getfield(nt, k)) for k in keys(nt)], ",") * "}"

"Serialise a `SpinMemoryResult` (or a vector of them) to JSON."
function to_json(res::SpinMemoryResult; trajectory::Bool = true)
    io = IOBuffer()
    print(io, "{\"params\":", _jval(res.params))
    print(io, ",\"dim\":", res.dim)
    print(io, ",\"tcollision\":", _jnum(res.tcollision))
    print(io, ",\"pre_window\":[", _jnum(res.pre_window[1]), ",", _jnum(res.pre_window[2]), "]")
    print(io, ",\"post_window\":[", _jnum(res.post_window[1]), ",", _jnum(res.post_window[2]), "]")
    print(io, ",\"dx1\":", _jnum(res.dx1))
    print(io, ",\"dx2\":", _jnum(res.dx2))
    print(io, ",\"dx3\":", _jnum(res.dx3))
    print(io, ",\"dx_estimator_spread\":", _jnum(abs(res.dx1 - res.dx2)))
    print(io, ",\"kink_slope_pre\":", _jnum(res.slope_pre1))
    print(io, ",\"kink_slope_post\":", _jnum(res.slope_post1))
    print(io, ",\"transmission\":", _jnum(res.T_final))
    print(io, ",\"reflection\":", _jnum(res.R_final))
    print(io, ",\"trapped\":", _jnum(res.trapped_final))
    print(io, ",\"transmission_initial\":", _jnum(res.T_init))
    print(io, ",\"reflection_initial\":", _jnum(res.R_init))
    print(io, ",\"ratio_dx1_over_T\":", _jnum(res.ratio1))
    print(io, ",\"ratio_dx2_over_T\":", _jnum(res.ratio2))
    print(io, ",\"ratio_dx2_over_deltaT\":", _jnum(res.ratio2_sub))
    print(io, ",\"norm_drift\":", _jnum(maximum(abs.(res.norms .- 1))))
    print(io, ",\"energy_drift\":", _jnum(maximum(abs.(res.energies .- res.energies[1]))))
    print(io, ",\"init_truncation_leakage\":", _jnum(res.leakage_init))
    print(io, ",\"H_truncation_leakage\":", _jnum(res.leakage_H))
    if trajectory
        print(io, ",\"times\":", _jval(res.times))
        print(io, ",\"X1\":", _jval(res.X1))
        print(io, ",\"X2\":", _jval(res.X2))
        print(io, ",\"T\":", _jval(res.Tw))
        print(io, ",\"R\":", _jval(res.Rw))
    end
    print(io, "}")
    return String(take!(io))
end

to_json(v::AbstractVector{SpinMemoryResult}; trajectory::Bool = true) =
    "[" * join((to_json(r; trajectory = trajectory) for r in v), ",\n") * "]"
