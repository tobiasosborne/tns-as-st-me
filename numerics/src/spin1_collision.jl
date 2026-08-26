# spin1_collision.jl — wavepacket collisions in the spin-S two-magnon sector.
#
# Included by src/spin1_twomagnon.jl; continues module Spin1TwoMagnon (no module
# wrapper of its own, the TriangleMPS.jl shard convention).
#
# Sign convention (identical to fm_twomagnon.jl, docs/fm-twomagnon-notes.md §2).
# With ψ_out ∝ ∫dk₁dk₂ g_s(k₁) g_h(k₂) S₁₂(k₁,k₂) e^{i(k₁x+k₂y)}, stationary
# phase gives
#
#     Δ_s = -∂δ/∂k_s ,   Δ_h = -∂δ/∂k_h ,   δ = arg S₁₂ ,
#
# so a soft slope of +2 shows up as a soft packet pushed BACK by two sites.
# Nothing here feeds the S-matrix into the dynamics: `collision_run` builds the
# state and the Hamiltonian from the enumeration only, and `pred_s_avg` is
# reported alongside the measurement purely for comparison.

# --------------------------------------------------------- wavepackets ----

"""
Normalised Gaussian wavepacket on the ring, centred at `X`, real-space standard
deviation `σx` of `|φ|²`, central momentum `k`.  Minimal-image Gaussian, raw
site label in the plane-wave factor (consistent while the amplitude at the seam
is negligible).
"""
function gaussian_packet(N::Integer, k::Real, X::Real, σx::Real)
    φ = Vector{ComplexF64}(undef, N)
    for x in 0:N-1
        d = x - X
        d -= N * round(d / N)
        φ[x+1] = exp(-d^2 / (4σx^2)) * cis(k * x)
    end
    return φ / norm(φ)
end

"Momentum-space weights `|⟨k|φ⟩|²` on the ring momenta `k ∈ (-π,π]`."
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

"Packet-averaged group velocity `⟨2JS sin k⟩` — the exact centroid velocity."
function packet_velocity(φ::AbstractVector, J::Real, S::Real)
    ks, w = momentum_weights(φ)
    return sum(w .* (2 * J * S .* sin.(ks)))
end

"""
Packet-averaged displacement predictions `(Δ_s, Δ_h)` from the analytic spin-`S`
S-matrix.  Because `|S₁₂| = 1`, the centroid shift of the outgoing packet is
exactly the `|g|²`-weighted average of `-∂δ/∂k`, so this removes the
finite-packet-width systematic from the comparison.  It is reported next to the
dynamical measurement, never fed into it.
"""
function packet_average_displacement(φs::AbstractVector, φh::AbstractVector, S::Real;
                                     cut::Float64 = 1e-9)
    k1s, w1 = momentum_weights(φs)
    k2s, w2 = momentum_weights(φh)
    i1 = findall(>(cut * maximum(w1)), w1)
    i2 = findall(>(cut * maximum(w2)), w2)
    Δs = 0.0; Δh = 0.0; Z = 0.0
    for a in i1, b in i2
        nn = contact_numerator(k1s[a], k2s[b], S)
        abs(nn) < 1e-10 && continue
        w = w1[a] * w2[b]
        d1, d2 = _dnum(k1s[a], k2s[b], S)
        Δs -= w * 2 * imag(d1 / nn)
        Δh -= w * 2 * imag(d2 / nn)
        Z += w
    end
    return Δs / Z, Δh / Z
end

"""
Two-boson product state on the basis `pb`: `c(x,y) = φ_L(x)φ_R(y)+φ_R(x)φ_L(y)`
off the diagonal and `c(x,x) = √2 φ_L(x)φ_R(x)` on it (the `b†²|0⟩ = √2|2⟩`
normalisation).  With spatially disjoint packets the diagonal amplitude is
exponentially small, so the state is the exact in-state up to that overlap.
"""
function two_magnon_product_state(pb::SpinPairBasis, φL::AbstractVector, φR::AbstractVector)
    ψ = Vector{ComplexF64}(undef, pb.dim)
    for (n, (x, y)) in enumerate(pb.pairs)
        ψ[n] = x == y ? sqrt(2) * φL[x+1] * φR[x+1] :
               φL[x+1] * φR[y+1] + φR[x+1] * φL[y+1]
    end
    return ψ / norm(ψ)
end

"Single-particle density `n(x)` (total mass 2), double occupancy counted twice."
function one_body_density(pb::SpinPairBasis, ψ::AbstractVector)
    n = zeros(Float64, pb.N)
    @inbounds for (m, (x, y)) in enumerate(pb.pairs)
        p = abs2(ψ[m])
        n[x+1] += p
        n[y+1] += p
    end
    return n
end

centroid(n::AbstractVector) = sum((0:length(n)-1) .* n) / sum(n)

"""
Chamber position expectations `(⟨x⟩, ⟨y⟩)`: the mean position of the left and of
the right magnon.  Needs no spatial window, hence no window-boundary artefact;
the residual mis-ordering bias cancels against the free reference.
"""
function chamber_positions(pb::SpinPairBasis, ψ::AbstractVector)
    sx = 0.0; sy = 0.0; z = 0.0
    @inbounds for (m, (x, y)) in enumerate(pb.pairs)
        p = abs2(ψ[m])
        sx += x * p; sy += y * p; z += p
    end
    return sx / z, sy / z
end

# ------------------------------------------------------------ evolution ----

function _step(H, ψ::AbstractVector, dt::Real; krylovdim::Int = 40, tol::Real = 1e-12)
    w, info = exponentiate(H, -im * dt, ψ; ishermitian = true,
                           krylovdim = krylovdim, tol = tol, eager = true)
    return w, info
end

"Evolve for total time `T` in steps of `dt` (test helper)."
function evolve(H, ψ::AbstractVector, T::Real; dt::Real = 2.0, kwargs...)
    ψ = ComplexF64.(ψ)
    nst = max(1, round(Int, T / dt))
    h = T / nst
    for _ in 1:nst
        ψ, _ = _step(H, ψ, h; kwargs...)
    end
    return ψ
end

# ------------------------------------------------------------- geometry ----

"""
Lay out a collision that fits inside a ring and stays away from the seam: hard
packet on the left at `Xh` with velocity `v_h`, soft packet on the right at
`Xs = Xh + D`, `v_s < v_h` (the D7 incoming configuration).  The run stops one
separation after the crossing time.
"""
function plan_geometry(; J::Real, S::Real, ks::Real, kh::Real, σx::Real,
                       sep_factor::Real = 10.0, pad_factor::Real = 8.0)
    vs = group_velocity(ks, J, S)
    vh = group_velocity(kh, J, S)
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

# -------------------------------------------------------- the experiment ----

"""
    collision_run(; S, J, ks, kh, sigma_x, sep_factor, dt, krylovdim, tol)

Dynamical extraction of the soft displacement in the spin-`S` two-magnon sector.
Three evolutions run in lockstep on the same ring: the interacting two-magnon
state and two free single-magnon references.  The displacement of each packet is
its chamber-marginal position minus the corresponding free reference.
"""
function collision_run(; S::Real = 1.0, J::Real = 1.0, ks::Real, kh::Real,
                       sigma_x::Real = 8.0, sep_factor::Real = 10.0,
                       dt::Real = 1.0, krylovdim::Int = 40, tol::Real = 1e-12)
    σx = float(sigma_x)
    geo = plan_geometry(; J = J, S = S, ks = ks, kh = kh, σx = σx,
                        sep_factor = sep_factor)
    N = geo.N
    pb = pair_basis(N, S)
    H2 = two_magnon_hamiltonian(pb, J, S)
    H1 = one_magnon_hamiltonian(N, J, S)

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
    normdrift = 0.0; energydrift = 0.0
    krylov_ok = true

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
        ψ, i2 = _step(H2, ψ, h; krylovdim = krylovdim, tol = tol)
        us, ia = _step(H1, us, h; krylovdim = krylovdim, tol = tol)
        uh, ib = _step(H1, uh, h; krylovdim = krylovdim, tol = tol)
        krylov_ok &= (i2.converged > 0 && ia.converged > 0 && ib.converged > 0)
        normdrift = max(normdrift, abs(norm(ψ) - n0))
        energydrift = max(energydrift,
                          abs(real(dot(ψ, H2 * ψ)) / n0^2 - E0) / max(abs(E0), eps()))
        record!(j * h)
    end

    late = findall(t -> t >= geo.tc + 0.6 * (geo.T - geo.tc), ts)
    pre = findall(t -> t <= 0.4 * geo.tc, ts)
    δs_spread = maximum(ds[late]) - minimum(ds[late])
    δh_spread = maximum(dh[late]) - minimum(dh[late])
    δs_pre = isempty(pre) ? NaN : sum(ds[pre]) / length(pre)
    δh_pre = isempty(pre) ? NaN : sum(dh[pre]) / length(pre)
    pas, pah = packet_average_displacement(φs, φh, S)

    return (; S = float(S), N, dim = pb.dim, J, ks, kh, σx, sep_factor,
            T = geo.T, tc = geo.tc, dt = h, nsteps = nst,
            vs = geo.vs, vh = geo.vh,
            delta_s = ds[end], delta_h = dh[end],
            delta_s_spread = δs_spread, delta_h_spread = δh_spread,
            delta_s_pre = δs_pre, delta_h_pre = δh_pre,
            pred_s_exact = -dphase_dk1(ks, kh, S),
            pred_h_exact = -dphase_dk2(ks, kh, S),
            pred_s_avg = pas, pred_h_avg = pah,
            norm_drift = normdrift, energy_drift = energydrift,
            krylov_ok = krylov_ok, times = ts, traj_s = ds, traj_h = dh)
end

"""
    richardson(σa, va, σb, vb)

Two-point extrapolation of a measured displacement to zero packet width.  The
finite-width bias of the centroid shift is linear in `1/σ_x²`, so fitting
`v = A + B/σ_x²` and returning `A` removes it using measured data only.
"""
function richardson(σa::Real, va::Real, σb::Real, vb::Real)
    ua, ub = 1 / σa^2, 1 / σb^2
    B = (va - vb) / (ua - ub)
    return va - B * ua
end

"""
    soft_slope_dynamical(; S, J, kh, ks_values, sigmas, sep_factor, dt)

The soft phase slope from wavepacket dynamics alone.  For each `k_s` the
displacement is measured at several packet widths and Richardson-extrapolated to
zero width, giving `Δ_s(k_s) = -∂δ/∂k_s`.  A straight-line fit of `-Δ_s` against
`k_s` is extrapolated to `k_s = 0`; the intercept is `dδ/dk_s|_0`.  The reported
error is the larger of the fit residual and the spread of the width-pair
extrapolations.
"""
function soft_slope_dynamical(; S::Real = 1.0, J::Real = 1.0, kh::Real = 1.5,
                              ks_values = (0.10, 0.15, 0.20, 0.30),
                              sigmas = (8.0, 11.0, 14.0), sep_factor::Real = 10.0,
                              dt::Real = 1.0, verbose::Bool = false)
    xs = Float64[]; ys = Float64[]; errs = Float64[]; rows = Any[]
    for ks in ks_values
        rs = [collision_run(; S = S, J = J, ks = ks, kh = kh, sigma_x = σ,
                            sep_factor = sep_factor, dt = dt) for σ in sigmas]
        ms = collect(sigmas)
        ext = [richardson(ms[i], rs[i].delta_s, ms[j], rs[j].delta_s)
               for i in 1:length(ms)-1 for j in i+1:length(ms)]
        Δs = richardson(ms[end-1], rs[end-1].delta_s, ms[end], rs[end].delta_s)
        e = max(maximum(ext) - minimum(ext), rs[end].delta_s_spread)
        push!(xs, ks); push!(ys, -Δs); push!(errs, e)
        push!(rows, (; ks = ks, kh = float(kh), S = float(S),
                     minus_delta_s = -Δs, err = e,
                     raw = [r.delta_s for r in rs], sigmas = collect(sigmas),
                     N = rs[end].N, dim = rs[end].dim,
                     pred_avg = rs[end].pred_s_avg,
                     pred_exact = rs[end].pred_s_exact,
                     norm_drift = maximum(r.norm_drift for r in rs),
                     energy_drift = maximum(r.energy_drift for r in rs),
                     pre_control = rs[end].delta_s_pre))
        verbose && println("  ks=$ks  -Δs=$(round(-Δs, digits=6))  err=$(round(e, digits=6))")
    end
    n = length(xs)
    xb = sum(xs) / n; yb = sum(ys) / n
    den = sum((xs .- xb) .^ 2)
    b = den > 0 ? sum((xs .- xb) .* (ys .- yb)) / den : 0.0
    a = yb - b * xb
    resid = sqrt(sum((ys .- (a .+ b .* xs)) .^ 2) / max(1, n - 2))
    return (slope = a, err = max(resid, maximum(errs)), fit_slope = b,
            resid = resid, rows = rows, kh = float(kh), S = float(S))
end
