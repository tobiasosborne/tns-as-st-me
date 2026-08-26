"""
spins_twomagnon_collision.jl — Gaussian wavepackets, Krylov evolution, the
ring geometry planner, and the collision experiment that extracts the soft
Wigner phase slope from PURE DYNAMICS.  Shard 2 of the `SpinSTwoMagnon` module
(`spins_twomagnon.jl`); the sector machinery it stands on is
`spins_twomagnon_sector.jl`.

`collision_run` measures the soft packet's centroid displacement against a free
single-magnon reference; `soft_slope_at` symmetrises over `±k_s` and
Richardson-extrapolates in `1/σx²`; `soft_slope` extrapolates those to
`k_s = 0` in `k_s²`.  No S-matrix enters any measurement — the exact values are
carried alongside only as predictions.
"""

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
    runs = vcat(rp, rm)
    return (; slope, err = max(spread, drift), exact_symmetrised = exact,
            delta_s_plus = Δp, delta_s_minus = Δm,
            raw_plus = [r.delta_s for r in rp], raw_minus = [r.delta_s for r in rm],
            avg_plus = [r.pred_s_avg for r in rp], avg_minus = [r.pred_s_avg for r in rm],
            sigmas = σ, ks = abs(ks), kh, twoS, J,
            N = rp[end].N, dim = rp[end].dim,
            norm_drift = maximum(r.norm_drift for r in runs),
            energy_drift = maximum(r.energy_drift for r in runs),
            pre_control = maximum(abs(r.delta_s_pre) for r in runs),
            krylov_ok = all_ok(runs))
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

