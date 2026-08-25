"""
memory_experiment.jl — the magnon-through-kink memory experiment (WP N2a,
Corner B of the lattice infrared triangle).

Protocol
--------
1. Put a kink at the centre of the chain: take the exact ground state of the
   S^z sector with n = L/2 down spins (a dressed kink; sharp at large Δ).
2. Add an incoming magnon far to its LEFT, in the ↑ region, with the modulated
   lowering operator of `magnon_wavepacket` (momentum k₀ > 0 ⇒ group velocity
   J_⊥ sin k₀ > 0 ⇒ the packet moves towards the kink).
3. Evolve with Krylov steps until the transmitted / reflected magnon is far
   from the wall.
4. Record ⟨S^z_x⟩, the two linear kink-position estimators X̂₁, X̂₂, the
   diagnostic X̂₃, and the operational transmission / reflection weights.
5. Fit the kink trajectory on a pre-collision and a post-collision window and
   take the difference of the two fits evaluated at the collision time.  That
   asymptotic intercept difference is δx — the memory.
"""

"""
    trajectory_offset(t, X, tc, pre, post) -> (dx, ...)

Least-squares fit X ≈ a + b t on the time windows `pre = (t₁, t₂)` and
`post = (t₃, t₄)`, then

    δx = [a_post + b_post t_c] - [a_pre + b_pre t_c].

This is the asymptotic displacement offset at the collision time t_c: any
ballistic drift of the kink (momentum transferred during the transit) is
removed by the slopes and only the permanent offset survives.
"""
function trajectory_offset(t::AbstractVector, X::AbstractVector, tc::Real,
                           pre::Tuple, post::Tuple)
    fit = function (lo, hi)
        idx = findall(i -> lo <= t[i] <= hi && isfinite(X[i]), eachindex(t))
        length(idx) >= 2 || return (NaN, NaN)
        tt = @view t[idx]
        xx = @view X[idx]
        tb = sum(tt) / length(tt)
        xb = sum(xx) / length(xx)
        num = sum((tt[i] - tb) * (xx[i] - xb) for i in eachindex(tt))
        den = sum((tt[i] - tb)^2 for i in eachindex(tt))
        b = den > 0 ? num / den : 0.0
        return (xb - b * tb, b)
    end
    (a1, b1) = fit(pre[1], pre[2])
    (a2, b2) = fit(post[1], post[2])
    dx = (a2 + b2 * tc) - (a1 + b1 * tc)
    return (dx=dx, slope_pre=b1, slope_post=b2,
            X_pre=a1 + b1 * tc, X_post=a2 + b2 * tc)
end

"""
    MemoryResult

Results record of one magnon-through-kink run: the parameters, the recorded
trajectory, and the summary numbers (δx by each estimator, T, R, trapped).
"""
struct MemoryResult
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
    tcollision::Float64
    pre_window::Tuple{Float64,Float64}
    post_window::Tuple{Float64,Float64}
    dim::Int
    leakage_init::Float64
    leakage_H::Float64
end

"""
    memory_experiment(; N, Delta, Jperp=1.0, k0, sigma, standoff, dwmax=3,
                        dt=0.25, tmax=nothing, halfwidth=6, buffer=8) -> MemoryResult

Run the protocol above.  `standoff` is the distance between the initial magnon
centre and the kink wall; `tmax` defaults to the time for the packet to reach
the wall, clear the measurement window/buffer on the far side, and settle.
`trapped_tol` sets how clean the wall region must be for a time slice to enter
the pre/post trajectory fits.  `dwmax = 3` keeps the kink + one-magnon subspace of the S^z sector
(1 and 3 domain-wall configurations); `dwmax = 5` adds the kink + two-magnon
configurations and is used for truncation-convergence checks.
"""
function memory_experiment(; N::Int, Delta::Real, Jperp::Real=1.0, k0::Real,
                           sigma::Real=4.0, standoff::Real=28.0,
                           dwmax::Union{Int,Nothing}=3, dt::Real=0.25,
                           tmax::Union{Real,Nothing}=nothing,
                           halfwidth::Int=8, buffer::Real=8,
                           kink_state::Symbol=:ground, trapped_tol::Real=1e-4,
                           obs_every::Int=1, verbose::Bool=false)
    ch = XXZChain(N; Jperp=Jperp, Delta=Delta, boundary=:kink)
    L = nsites_dynamical(ch)
    n = div(L, 2)
    Xk0 = float(L - n) + 1.5              # initial wall bond, physical coordinates
    x0 = Xk0 - standoff
    x0 - 3 * sigma > 1 || throw(ArgumentError("packet too close to the left edge; " *
                                             "increase N or reduce standoff/sigma"))

    bk = kink_state === :sharp ? sector_basis(ch; ndown=n, dwmax=1) :
         sector_basis(ch; ndown=n, dwmax=dwmax)
    _, ψk = sector_ground_state(bk)
    b = sector_basis(ch; ndown=n + 1, dwmax=dwmax)
    leak0 = magnon_wavepacket_leakage(b, bk, ψk; k0=k0, x0=x0, sigma=sigma)
    ψ0 = magnon_wavepacket(b, bk, ψk; k0=k0, x0=x0, sigma=sigma)
    H = build_hamiltonian(b)
    leakH = truncation_leakage(b)

    v = magnon_velocity(ch, k0)
    tc = standoff / max(abs(v), 1e-12)            # packet centre reaches the wall
    reach = max(halfwidth, buffer) + 3 * sigma    # how far the packet must be to be "clear"
    tclear = reach / max(abs(v), 1e-12)
    settle = max(10 * dt, 2 * sigma / max(abs(v), 1e-12))
    Tmax = tmax === nothing ? tc + tclear + settle : float(tmax)
    nsteps = max(8, ceil(Int, Tmax / dt))
    Tmax = nsteps * dt
    # the outgoing packet must not reach the far end of the chain
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
        push!(X1, kink_position_centroid(m; window=window))
        push!(X2, kink_position_integrated(m; window=window))
        push!(X3, kink_position_crossing(m; window=window))
        w = magnon_weights(m; kink_ref=Xk0, buffer=buffer)
        push!(Tw, w.T); push!(Rw, w.R); push!(trp, w.trapped)
        push!(nrm, norm(ψ))
        push!(ens, real(dot(ψ, H * ψ)))
        return nothing
    end

    ψ = ComplexF64.(ψ0)
    record!(0.0, ψ)
    for s in 1:nsteps
        ψ = krylov_evolve(H, ψ, dt)
        (s % obs_every == 0 || s == nsteps) && record!(s * dt, ψ)
    end
    verbose && @printf("N=%d Δ=%.2f k0=%.3f dim=%d steps=%d T=%.4f\n",
                       N, Delta, k0, length(b), nsteps, Tw[end])

    # Fit windows, chosen from the DATA rather than from geometry alone: the
    # kink position is only meaningful while no magnon amplitude sits near the
    # wall, which is exactly the statement `trapped < trapped_tol`.  "pre" is
    # the initial clean stretch, "post" the final clean stretch.  Falls back to
    # the geometric estimate when the criterion selects too few points (e.g. a
    # deliberately short, externally supplied tmax).
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

    params = (N=N, L=L, ndown=n, Delta=float(Delta), Jperp=float(Jperp),
              k0=float(k0), sigma=float(sigma), standoff=float(standoff),
              x0=x0, Xkink0=Xk0, dwmax=(dwmax === nothing ? -1 : dwmax),
              kink_state=String(kink_state),
              dt=float(dt), tmax=tend, nsteps=nsteps,
              halfwidth=halfwidth, buffer=float(buffer),
              trapped_tol=float(trapped_tol),
              vgroup=v, omega=magnon_dispersion(ch, k0))

    return MemoryResult(params, times, X1, X2, X3, Tw, Rw, trp, nrm, ens,
                        o1.dx, o2.dx, o3.dx, o1.slope_pre, o1.slope_post,
                        Tw[end], Rw[end], trp[end], tc_used,
                        (float(pre[1]), float(pre[2])), (float(post[1]), float(post[2])),
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

"""
    to_json(res::MemoryResult; trajectory=true) -> String
    to_json(v::Vector{MemoryResult}; trajectory=true) -> String

Serialise a results record (or a scan) to JSON.  Non-finite floats become
`null` so the output is always valid JSON.
"""
function to_json(res::MemoryResult; trajectory::Bool=true)
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
    print(io, ",\"dx1_over_minus2T\":",
          _jnum(res.T_final > 1e-12 ? res.dx1 / (-2 * res.T_final) : NaN))
    print(io, ",\"norm_drift\":", _jnum(maximum(abs.(res.norms .- 1))))
    print(io, ",\"energy_drift\":", _jnum(maximum(abs.(res.energies .- res.energies[1]))))
    print(io, ",\"init_truncation_leakage\":", _jnum(res.leakage_init))
    print(io, ",\"H_truncation_leakage\":", _jnum(res.leakage_H))
    if trajectory
        print(io, ",\"times\":", _jval(res.times))
        print(io, ",\"X1\":", _jval(res.X1))
        print(io, ",\"X2\":", _jval(res.X2))
        print(io, ",\"X3\":", _jval(res.X3))
        print(io, ",\"T\":", _jval(res.Tw))
        print(io, ",\"R\":", _jval(res.Rw))
    end
    print(io, "}")
    return String(take!(io))
end

to_json(v::AbstractVector{MemoryResult}; trajectory::Bool=true) =
    "[" * join((to_json(r; trajectory=trajectory) for r in v), ",\n") * "]"
