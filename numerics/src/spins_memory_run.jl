"""
spins_memory_run.jl — the magnon-through-kink protocol for the easy-axis
spin-`S` XXZ ferromagnet.  Shard 2 of the `SpinSMemory` module; the sector
machinery it stands on is `spins_memory_sector.jl`.

Protocol (the spin-`S` reading of the frozen `S = 1/2` protocol in
`numerics/src/memory_experiment.jl`, so the two are directly comparable):

1. Put a kink near the centre: the exact ground state of the magnon-number
   sector `n_tot = 2S·n_z` (a dressed wall; monotone and narrow at large Δ).
2. Add an incoming magnon far to its LEFT, in the ↑ region, with the modulated
   lowering operator `O = Σ_x e^{ik₀x}e^{-(x-x₀)²/4σ²} S⁻_x` (`k₀ > 0` ⇒ group
   velocity `2SJ_⊥ sin k₀ > 0`, so the packet moves towards the wall).
3. Evolve with Krylov steps until the transmitted / reflected magnon is clear
   of the wall.
4. Record `⟨S^z_x⟩`, the wall estimators X̂₁, X̂₂, the diagnostic X̂₃, and the
   operational transmission / reflection weights `T`, `R`.
5. Fit the wall trajectory on a clean pre-collision and a clean post-collision
   window and difference the two fits at the collision time.  That asymptotic
   intercept difference is `δx`, the memory.

The quantity the falsifier reads is `δx / N_T`, which Theorem M-quant fixes at
`-1/s` — `-2` sites at `S = 1/2`, `-1` site at `S = 1`.
"""

"""
    trajectory_offset(t, X, tc, pre, post) -> (dx, ...)

Least-squares `X ≈ a + b t` on the windows `pre` and `post`, then
`δx = [a_post + b_post·t_c] - [a_pre + b_pre·t_c]`: the asymptotic intercept
difference at the collision time, with any ballistic drift removed by the
slopes.
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

"""Results record of one spin-`S` magnon-through-kink run."""
struct MemoryResultS
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
    dim_kink::Int
    leakage_init::Float64
    leakage_H::Float64
end

"""
    memory_experiment_s(; N, twoS, Delta, Jperp=1.0, k0, sigma, standoff,
                          dmax=1, dt, tmax=nothing, halfwidth, buffer,
                          kink_state=:ground, trapped_tol, obs_every, verbose)

Run the protocol above at spin `S = twoS/2`.  `dmax = 1` keeps the
kink + one-magnon subspace (up-variation `D ≤ 1`); `dmax = 2` adds the
two-magnon configurations and is used for truncation-convergence checks.
`standoff` is the distance from the initial packet centre to the wall.
"""
function memory_experiment_s(; N::Int, twoS::Int=2, Delta::Real, Jperp::Real=1.0,
                             k0::Real, sigma::Real=4.0, standoff::Real=20.0,
                             dmax::Union{Int,Nothing}=1, dt::Real=0.2,
                             tmax::Union{Real,Nothing}=nothing,
                             halfwidth::Int=8, buffer::Real=8,
                             kink_state::Symbol=:ground, trapped_tol::Real=1e-4,
                             obs_every::Int=1, verbose::Bool=false)
    ch = SpinChain(N; twoS=twoS, Jperp=Jperp, Delta=Delta, boundary=:kink)
    L = nsites_dynamical(ch)
    nz = div(L, 2)                       # sites in the ↓ vacuum
    ntot = twoS * nz
    Xk0 = float(L - nz) + 1.5            # wall bond, physical coordinates
    x0 = Xk0 - standoff
    # The asymptotic region has to be genuinely asymptotic: at t = 0 the packet
    # must sit entirely inside the reflected-weight region, otherwise `trapped`
    # never starts below `trapped_tol`, the data-driven pre-window degenerates
    # to its geometric fallback, and the trajectory fit extrapolates a spurious
    # slope over the whole interval to t_c.  4σ leaves 3·10⁻⁵ of the packet
    # outside, an order of magnitude below the default tolerance.
    standoff >= buffer + 4 * sigma ||
        throw(ArgumentError("standoff = $standoff is too small: the protocol needs " *
                            "standoff ≥ buffer + 4σ = $(buffer + 4 * sigma) so that the " *
                            "packet is asymptotic at t = 0"))
    x0 - 4 * sigma > 1 || throw(ArgumentError("packet too close to the left edge; " *
                                             "increase N or reduce standoff/sigma"))

    bk = kink_state === :monotone ? sector_basis_s(ch; ntot=ntot, dmax=0) :
         sector_basis_s(ch; ntot=ntot, dmax=dmax)
    _, ψk = sector_ground_state_s(bk)
    b = sector_basis_s(ch; ntot=ntot + 1, dmax=dmax)
    leak0 = magnon_wavepacket_leakage_s(b, bk, ψk; k0=k0, x0=x0, sigma=sigma)
    ψ0 = magnon_wavepacket_s(b, bk, ψk; k0=k0, x0=x0, sigma=sigma)
    H = build_hamiltonian_s(b)
    leakH = truncation_leakage_s(b)

    v = magnon_velocity_s(ch, k0)
    tc = standoff / max(abs(v), 1e-12)
    reach = max(halfwidth, buffer) + 4 * sigma      # symmetric with the 4σ standoff rule
    tclear = reach / max(abs(v), 1e-12)
    settle = max(10 * dt, 2 * sigma / max(abs(v), 1e-12))
    Tmax = tmax === nothing ? tc + tclear + settle : float(tmax)
    nsteps = max(8, ceil(Int, Tmax / dt))
    Tmax = nsteps * dt
    if tmax === nothing
        Xk0 + abs(v) * (Tmax - tc) + 4 * sigma > N - 1 &&
            throw(ArgumentError("chain too short: the outgoing packet would hit the " *
                                "right boundary; increase N or reduce standoff/sigma"))
    end
    window = (max(1, round(Int, Xk0) - halfwidth), min(N, round(Int, Xk0) + halfwidth))

    times = Float64[]; X1 = Float64[]; X2 = Float64[]; X3 = Float64[]
    Tw = Float64[]; Rw = Float64[]; trp = Float64[]
    nrm = Float64[]; ens = Float64[]

    record! = function (t, ψ)
        m = sz_profile_s(b, ψ)
        push!(times, t)
        push!(X1, kink_position_centroid(m; window=window))
        push!(X2, kink_position_integrated(m, twoS; window=window))
        push!(X3, kink_position_crossing(m; window=window))
        w = magnon_weights_s(m, twoS; kink_ref=Xk0, buffer=buffer)
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
    verbose && @printf("N=%d 2S=%d Δ=%.2f k0=%.3f dim=%d steps=%d T=%.4f\n",
                       N, twoS, Delta, k0, length(b), nsteps, Tw[end])

    # Fit windows chosen from the DATA: the wall position is only meaningful
    # while no magnon amplitude sits on it, i.e. `trapped < trapped_tol`.
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

    params = (N=N, L=L, twoS=twoS, spin=twoS / 2, ntot=ntot + 1, nz=nz,
              Delta=float(Delta), Jperp=float(Jperp), k0=float(k0),
              sigma=float(sigma), standoff=float(standoff), x0=x0, Xkink0=Xk0,
              dmax=(dmax === nothing ? -1 : dmax), kink_state=String(kink_state),
              dt=float(dt), tmax=tend, nsteps=nsteps, halfwidth=halfwidth,
              buffer=float(buffer), trapped_tol=float(trapped_tol),
              vgroup=v, omega=magnon_dispersion_s(ch, k0))

    return MemoryResultS(params, times, X1, X2, X3, Tw, Rw, trp, nrm, ens,
                         o1.dx, o2.dx, o3.dx, o1.slope_pre, o1.slope_post,
                         Tw[end], Rw[end], trp[end], tc_used,
                         (float(pre[1]), float(pre[2])), (float(post[1]), float(post[2])),
                         length(b), length(bk), leak0, leakH)
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
    to_json(res::MemoryResultS; trajectory=true) -> String

Serialise a results record (or a vector of them) to JSON.  `dx1_over_T` is the
falsifier's observable: Theorem M-quant predicts `-1/s`.
"""
function to_json(res::MemoryResultS; trajectory::Bool=true)
    s = res.params.spin
    io = IOBuffer()
    print(io, "{\"params\":", _jval(res.params))
    print(io, ",\"dim\":", res.dim)
    print(io, ",\"dim_kink\":", res.dim_kink)
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
    print(io, ",\"memory_quantum_prediction\":", _jnum(-1 / s))
    print(io, ",\"dx1_over_T\":",
          _jnum(res.T_final > 1e-12 ? res.dx1 / res.T_final : NaN))
    print(io, ",\"dx2_over_T\":",
          _jnum(res.T_final > 1e-12 ? res.dx2 / res.T_final : NaN))
    print(io, ",\"dx1_over_prediction\":",
          _jnum(res.T_final > 1e-12 ? res.dx1 / (-res.T_final / s) : NaN))
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

to_json(v::AbstractVector{MemoryResultS}; trajectory::Bool=true) =
    "[" * join((to_json(r; trajectory=trajectory) for r in v), ",\n") * "]"
