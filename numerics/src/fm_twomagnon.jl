"""
    FMTwoMagnon

Dynamical extraction of the two-magnon scattering phase of the isotropic
spin-1/2 Heisenberg *ferromagnet* from wavepacket collisions.

Model (definitions.md D6, quoted, not redefined here):
`H = -J Σ_x (S_x·S_{x+1} - 1/4) = (J/2) Σ_x (1 - P_{x,x+1})`, vacuum `|Ω⟩ = |↑↑…⟩`,
periodic ring of `N` sites.  The two-magnon sector has dimension `N(N-1)/2`.

What this module does that the Bethe oracle does *not*: it never uses the Bethe
ansatz to build a state.  It builds the sector Hamiltonian from its own
enumeration of down-spin pairs, prepares two spatially disjoint Gaussian
wavepackets (hard on the left with momentum `k_h`, soft on the right with
momentum `k_s`, arranged so `v(k_h) > v(k_s)`, i.e. the D7 incoming
configuration), evolves with `KrylovKit.exponentiate`, and reads off the
*spatial displacement* of each outgoing packet relative to a free
single-magnon reference run.

Sign convention (derived in docs/fm-twomagnon-notes.md, §2).  With
`ψ_out ∝ ∫dk_1 dk_2 g_s(k_1) g_h(k_2) S_12(k_1,k_2) e^{i(k_1 x + k_2 y)}`,
stationary phase gives

    Δ_s = -∂δ/∂k_s ,     Δ_h = -∂δ/∂k_h ,     δ = arg S_12 .

The soft packet is therefore pushed *backwards* by the leading scattering
length 2 (Δ_s ≈ -2) and the hard packet forwards by an `O(k_s^2)` amount --
exactly the hard-sphere pattern.

Only LinearAlgebra, SparseArrays, KrylovKit are used.  Standalone module: it is
included directly by numerics/test/test_fm_twomagnon.jl and is not part of
TriangleMPS.
"""
module FMTwoMagnon

using LinearAlgebra
using SparseArrays
using KrylovKit

export PairBasis, pair_basis, one_magnon_hamiltonian, two_magnon_hamiltonian,
       omega, group_velocity, smatrix, soft_phase, dphase_dk1, dphase_dk2,
       oracle_phase, oracle_dphase_dks, oracle_dphase_dkh,
       quantized_pair, bethe_vector,
       gaussian_packet, momentum_weights, packet_velocity,
       packet_average_displacement, two_magnon_product_state,
       one_body_density, centroid, windowed_centroid, chamber_positions,
       evolve, plan_geometry, collision_run, richardson, displacement_scan, SCAN_GRID

# ---------------------------------------------------------------- basis ----

"""Ordered-pair basis `{(x,y) : 0 ≤ x < y ≤ N-1}` of the two-magnon sector."""
struct PairBasis
    N::Int
    dim::Int
    pairs::Vector{Tuple{Int,Int}}
    index::Matrix{Int}          # index[x+1,y+1] = index[y+1,x+1] = basis number
end

function pair_basis(N::Integer)
    N >= 4 || throw(ArgumentError("need N ≥ 4"))
    pairs = Tuple{Int,Int}[]
    index = zeros(Int, N, N)
    n = 0
    for x in 0:N-2, y in x+1:N-1
        n += 1
        push!(pairs, (x, y))
        index[x+1, y+1] = n
        index[y+1, x+1] = n
    end
    return PairBasis(Int(N), n, pairs, index)
end

# ---------------------------------------------------- sector Hamiltonians ----

"""
One-magnon block of `H`.  Every bond adjacent to the down spin contributes
`J/2` on the diagonal and `-J/2` to the hopped configuration (D6).
"""
function one_magnon_hamiltonian(N::Integer, J::Real)
    I = Int[]; K = Int[]; V = Float64[]
    for x in 0:N-1
        push!(I, x + 1); push!(K, x + 1); push!(V, Float64(J))   # two bonds × J/2
        for d in (-1, 1)
            y = mod(x + d, N)
            push!(I, y + 1); push!(K, x + 1); push!(V, -J / 2)
        end
    end
    return sparse(I, K, V, N, N)
end

"""
Two-magnon block of `H`, built by direct enumeration.  For a configuration
`{x,y}` a bond contributes iff exactly one of its two sites is occupied; each
such bond is in bijection with a single-particle hop onto a *free* neighbour,
so we enumerate the (at most four) legal hops.  Doubly occupied bonds are
annihilated by `1 - P` and contribute nothing -- this is the entire interaction.
"""
function two_magnon_hamiltonian(pb::PairBasis, J::Real)
    N = pb.N
    I = Int[]; K = Int[]; V = Float64[]
    sizehint!(I, 5 * pb.dim); sizehint!(K, 5 * pb.dim); sizehint!(V, 5 * pb.dim)
    for (col, (x, y)) in enumerate(pb.pairs)
        diag = 0.0
        for (site, other) in ((x, y), (y, x))
            for d in (-1, 1)
                t = mod(site + d, N)
                t == other && continue          # doubly occupied bond: no term
                diag += J / 2
                row = pb.index[min(t, other)+1, max(t, other)+1]
                push!(I, row); push!(K, col); push!(V, -J / 2)
            end
        end
        push!(I, col); push!(K, col); push!(V, diag)
    end
    return sparse(I, K, V, pb.dim, pb.dim)
end

# ------------------------------------------------- exact Bethe quantities ----

omega(k::Real, J::Real) = J * (1 - cos(k))
group_velocity(k::Real, J::Real) = J * sin(k)

"""D7 coefficient ratio `S_12 = A_12/A_21`, oracle equation (6)."""
function smatrix(k1::Real, k2::Real)
    z1, z2 = cis(k1), cis(k2)
    return -(z1 * z2 - 2z1 + 1) / (z1 * z2 - 2z2 + 1)
end

"""Continuous phase branch `δ = arg S_12` with `δ(0,k_h) = 0` (D7)."""
soft_phase(k1::Real, k2::Real) = angle(smatrix(k1, k2))

# ∂ log S_12 with z1' = i z1 etc.; |S| = 1 makes it purely imaginary.
function _dlogS(k1::Real, k2::Real)
    z1, z2 = cis(k1), cis(k2)
    num = z1 * z2 - 2z1 + 1
    den = z1 * z2 - 2z2 + 1
    d1 = im * z1 * (z2 - 2) / num - im * z1 * z2 / den
    d2 = im * z1 * z2 / num - im * z2 * (z1 - 2) / den
    return d1, d2
end

"""`∂δ/∂k_1` from the exact S-matrix (no soft truncation)."""
dphase_dk1(k1::Real, k2::Real) = imag(_dlogS(k1, k2)[1])
"""`∂δ/∂k_2` from the exact S-matrix (no soft truncation)."""
dphase_dk2(k1::Real, k2::Real) = imag(_dlogS(k1, k2)[2])

# Oracle soft expansion, O7:  δ = 2 k_s + cot(k_h/2) k_s^2 + O(k_s^3).
oracle_phase(ks::Real, kh::Real) = 2ks + cot(kh / 2) * ks^2
oracle_dphase_dks(ks::Real, kh::Real) = 2 + 2 * cot(kh / 2) * ks
oracle_dphase_dkh(ks::Real, kh::Real) = -ks^2 / (2 * sin(kh / 2)^2)

"""
Bethe--Yang quantisation on the ring: solve
`N k_1 = 2π n_1 + δ`, `N k_2 = 2π n_2 - δ` by fixed-point iteration.
Used only for the Hamiltonian-vs-Bethe unit test.
"""
function quantized_pair(N::Integer, n1::Integer, n2::Integer;
                        iters::Int = 400, tol::Float64 = 1e-14)
    k1 = 2π * n1 / N
    k2 = 2π * n2 / N
    for _ in 1:iters
        d = soft_phase(k1, k2)
        nk1 = (2π * n1 + d) / N
        nk2 = (2π * n2 - d) / N
        done = abs(nk1 - k1) < tol && abs(nk2 - k2) < tol
        k1, k2 = nk1, nk2
        done && break
    end
    return k1, k2
end

"""Coordinate Bethe vector `ψ(x,y) = S_12 e^{i(k_1x+k_2y)} + e^{i(k_2x+k_1y)}`."""
function bethe_vector(pb::PairBasis, k1::Real, k2::Real)
    S = smatrix(k1, k2)
    v = [S * cis(k1 * x + k2 * y) + cis(k2 * x + k1 * y) for (x, y) in pb.pairs]
    return v / norm(v)
end

# --------------------------------------------------------- wavepackets ----

"""
Normalised Gaussian wavepacket on the ring, centred at `X` with real-space
standard deviation `σx` of `|φ|²` and central momentum `k`.  The Gaussian uses
the minimal-image distance; the plane-wave factor uses the raw site label, which
is consistent as long as the amplitude is negligible at the seam `x = 0`.
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

"""Momentum-space weights `|⟨k|φ⟩|²` on the ring momenta `k ∈ (-π,π]`."""
function momentum_weights(φ::AbstractVector)
    N = length(φ)
    ks = Vector{Float64}(undef, N)
    w  = Vector{Float64}(undef, N)
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

"""Packet-averaged group velocity `⟨J sin k⟩` -- the exact centroid velocity."""
function packet_velocity(φ::AbstractVector, J::Real)
    ks, w = momentum_weights(φ)
    return sum(w .* (J .* sin.(ks)))
end

"""
Packet-averaged displacement predictions.  Because `|S_12| = 1`, the centroid
shift of the outgoing packet is *exactly* the `|g|²`-weighted average of
`-∂δ/∂k` (see notes §2), so this removes the finite-packet-width systematic.
Returns `(Δ_s, Δ_h)`.
"""
function packet_average_displacement(φs::AbstractVector, φh::AbstractVector;
                                     cut::Float64 = 1e-9)
    k1s, w1 = momentum_weights(φs)
    k2s, w2 = momentum_weights(φh)
    # The plane-wave factor of a packet at non-quantised k is discontinuous at
    # the ring seam, which leaves a 1/n Fourier tail of total weight ~1e-11.
    # `cut` removes it; without the cut the tail reaches the (k1,k2)=(0,0)
    # singularity of S_12 where ∂δ is undefined.
    i1 = findall(>(cut * maximum(w1)), w1)
    i2 = findall(>(cut * maximum(w2)), w2)
    Δs = 0.0; Δh = 0.0; Z = 0.0
    for a in i1, b in i2
        z1, z2 = cis(k1s[a]), cis(k2s[b])
        (abs(z1 * z2 - 2z1 + 1) < 1e-10 || abs(z1 * z2 - 2z2 + 1) < 1e-10) && continue
        w = w1[a] * w2[b]
        d1, d2 = _dlogS(k1s[a], k2s[b])
        Δs -= w * imag(d1)
        Δh -= w * imag(d2)
        Z += w
    end
    return Δs / Z, Δh / Z
end

"""
Chamber position expectations `(⟨x⟩, ⟨y⟩)` of a two-magnon vector: the mean
position of the *left* and of the *right* down spin.  This is the estimator used
for the displacement -- it needs no spatial window, hence no window-boundary
artefact, and the residual mis-ordering bias cancels against the free reference.
"""
function chamber_positions(pb::PairBasis, ψ::AbstractVector)
    sx = 0.0; sy = 0.0; z = 0.0
    @inbounds for (m, (x, y)) in enumerate(pb.pairs)
        p = abs2(ψ[m])
        sx += x * p; sy += y * p; z += p
    end
    return sx / z, sy / z
end

"""
Symmetrised two-boson product state restricted to the chamber `x < y`:
`ψ(x,y) = φ_L(x) φ_R(y) + φ_R(x) φ_L(y)`.  With spatially disjoint packets this
is the exact in-state up to exponentially small overlap.
"""
function two_magnon_product_state(pb::PairBasis, φL::AbstractVector, φR::AbstractVector)
    ψ = [φL[x+1] * φR[y+1] + φR[x+1] * φL[y+1] for (x, y) in pb.pairs]
    return ψ / norm(ψ)
end

"""Single-particle density `n(x) = Σ_{y≠x} |ψ(x,y)|²` (total mass 2)."""
function one_body_density(pb::PairBasis, ψ::AbstractVector)
    n = zeros(Float64, pb.N)
    @inbounds for (m, (x, y)) in enumerate(pb.pairs)
        p = abs2(ψ[m])
        n[x+1] += p
        n[y+1] += p
    end
    return n
end

centroid(n::AbstractVector) = sum((0:length(n)-1) .* n) / sum(n)

"""Centroid of `n` over the inclusive 0-based site window `lo:hi`."""
function windowed_centroid(n::AbstractVector, lo::Integer, hi::Integer)
    lo = max(lo, 0); hi = min(hi, length(n) - 1)
    num = 0.0; den = 0.0
    @inbounds for x in lo:hi
        num += x * n[x+1]
        den += n[x+1]
    end
    return num / den
end

"""One `exponentiate` step of `exp(-iH dt)`; also returns the Krylov info."""
function step(H, ψ::AbstractVector, dt::Real; krylovdim::Int = 40, tol::Real = 1e-12)
    w, info = exponentiate(H, -im * dt, ψ; ishermitian = true,
                           krylovdim = krylovdim, tol = tol, eager = true)
    return w, info
end

"""Evolve for total time `T` in steps of `dt` (test helper)."""
function evolve(H, ψ::AbstractVector, T::Real; dt::Real = 2.0, kwargs...)
    ψ = ComplexF64.(ψ)
    nst = max(1, round(Int, T / dt))
    h = T / nst
    for _ in 1:nst
        ψ, _ = step(H, ψ, h; kwargs...)
    end
    return ψ
end

# ---------------------------------------------------------- geometry ----

"""
Lay out a collision that fits inside a ring and stays away from the seam.

Hard packet starts on the left at `Xh` with velocity `v_h`, soft packet on the
right at `Xs = Xh + D` with velocity `v_s < v_h` (D7 incoming configuration).
`D = sep_factor·σx`; the run stops at `T = 2D/(v_h - v_s)`, i.e. one separation
`D` *after* the crossing time `t_c = T/2`.
"""
function plan_geometry(; J::Real, ks::Real, kh::Real, σx::Real,
                       sep_factor::Real = 10.0, pad_factor::Real = 8.0)
    vs = group_velocity(ks, J)
    vh = group_velocity(kh, J)
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

# ------------------------------------------------------ the experiment ----

"""
    collision_run(; J, ks, kh, σx, sep_factor, dt, krylovdim, tol)

Full dynamical extraction.  Three evolutions are run in lockstep on the same
ring: the interacting two-magnon state, and two free single-magnon reference
states (one per packet).  At each recorded time the ring is split at the
midpoint of the two *reference* centroids; the displacement of each packet is
its windowed centroid minus its reference centroid.

Before the crossing time the left window holds the hard packet (control:
displacement ≈ 0); after it, the left window holds the soft packet.

Returns a NamedTuple with the measured displacements, the exact and
oracle predictions, and conservation / convergence diagnostics.
"""
function collision_run(; J::Real = 1.0, ks::Real, kh::Real, σx::Real = 8.0,
                       sigma_x::Union{Nothing,Real} = nothing,
                       sep_factor::Real = 10.0, dt::Real = 2.0,
                       krylovdim::Int = 40, tol::Real = 1e-12)
    σx = sigma_x === nothing ? σx : sigma_x
    geo = plan_geometry(; J = J, ks = ks, kh = kh, σx = σx, sep_factor = sep_factor)
    N = geo.N
    pb = pair_basis(N)
    H2 = two_magnon_hamiltonian(pb, J)
    H1 = one_magnon_hamiltonian(N, J)

    φs = gaussian_packet(N, ks, geo.Xs, σx)
    φh = gaussian_packet(N, kh, geo.Xh, σx)
    ψ  = two_magnon_product_state(pb, φh, φs)

    n0 = norm(ψ)
    E0 = real(dot(ψ, H2 * ψ))

    us = ComplexF64.(φs)
    uh = ComplexF64.(φh)

    nst = max(4, round(Int, geo.T / dt))
    h = geo.T / nst

    ts = Float64[]; ds = Float64[]; dh = Float64[]
    dsw = Float64[]; dhw = Float64[]          # secondary windowed estimator
    normdrift = 0.0; energydrift = 0.0
    krylov_ok = true

    function record!(t)
        # primary estimator: chamber marginals against the free product state
        xi, yi = chamber_positions(pb, ψ)
        ref = two_magnon_product_state(pb, uh, us)
        xf, yf = chamber_positions(pb, ref)
        # secondary estimator: one-body density split at the reference midpoint
        nn = one_body_density(pb, ψ)
        cs = centroid(abs2.(us)); ch = centroid(abs2.(uh))
        mlo = floor(Int, (cs + ch) / 2)
        left  = windowed_centroid(nn, 0, mlo)
        right = windowed_centroid(nn, mlo + 1, N - 1)
        push!(ts, t)
        if t < geo.tc          # hard on the left (coordinate x), soft on the right
            push!(dh, xi - xf); push!(ds, yi - yf)
            push!(dhw, left - ch); push!(dsw, right - cs)
        else                   # soft on the left, hard on the right
            push!(ds, xi - xf); push!(dh, yi - yf)
            push!(dsw, left - cs); push!(dhw, right - ch)
        end
    end

    record!(0.0)
    for j in 1:nst
        ψ, i2 = step(H2, ψ, h; krylovdim = krylovdim, tol = tol)
        us, ia = step(H1, us, h; krylovdim = krylovdim, tol = tol)
        uh, ib = step(H1, uh, h; krylovdim = krylovdim, tol = tol)
        krylov_ok &= (i2.converged > 0 && ia.converged > 0 && ib.converged > 0)
        normdrift = max(normdrift, abs(norm(ψ) - n0))
        energydrift = max(energydrift, abs(real(dot(ψ, H2 * ψ)) / n0^2 - E0) / max(E0, eps()))
        record!(j * h)
    end

    # asymptotic (final-time) values and the late-window spread
    late = findall(t -> t >= geo.tc + 0.6 * (geo.T - geo.tc), ts)
    pre  = findall(t -> t <= 0.4 * geo.tc, ts)
    δs_final, δh_final = ds[end], dh[end]
    δs_spread = maximum(ds[late]) - minimum(ds[late])
    δh_spread = maximum(dh[late]) - minimum(dh[late])
    δs_pre = isempty(pre) ? NaN : sum(ds[pre]) / length(pre)
    δh_pre = isempty(pre) ? NaN : sum(dh[pre]) / length(pre)

    pas, pah = packet_average_displacement(φs, φh)
    σs_final = sqrt(max(0.0, sum(abs2.(us) .* ((0:N-1) .- centroid(abs2.(us))).^2)))
    σh_final = sqrt(max(0.0, sum(abs2.(uh) .* ((0:N-1) .- centroid(abs2.(uh))).^2)))
    sep_final = centroid(abs2.(uh)) - centroid(abs2.(us))
    resolution = sep_final / sqrt(σs_final^2 + σh_final^2)

    return (; N, dim = pb.dim, J, ks, kh, σx, sep_factor,
            T = geo.T, tc = geo.tc, dt = h, nsteps = nst,
            Xh = geo.Xh, Xs = geo.Xs, vs = geo.vs, vh = geo.vh,
            delta_s = δs_final, delta_h = δh_final,
            delta_s_spread = δs_spread, delta_h_spread = δh_spread,
            delta_s_pre = δs_pre, delta_h_pre = δh_pre,
            pred_s_exact = -dphase_dk1(ks, kh),
            pred_h_exact = -dphase_dk2(ks, kh),
            pred_s_avg = pas, pred_h_avg = pah,
            oracle_s = -oracle_dphase_dks(ks, kh),
            oracle_h = -oracle_dphase_dkh(ks, kh),
            norm_drift = normdrift, energy_drift = energydrift,
            krylov_ok = krylov_ok,
            delta_s_window = dsw[end], delta_h_window = dhw[end],
            sigma_s_final = σs_final, sigma_h_final = σh_final,
            sep_final = sep_final, resolution = resolution,
            times = ts, traj_s = ds, traj_h = dh)
end

"""
    richardson(σa, va, σb, vb)

Two-point extrapolation of a measured displacement to zero packet width.
The finite-width bias of the centroid shift is `⟨-∂δ⟩ - (-∂δ)|_center =
(σ_k²/2)·∂³δ + O(σ_k⁴)` with `σ_k = 1/(2σ_x)`, i.e. it is linear in `1/σ_x²`.
Fitting `v = A + B/σ_x²` and returning `A` removes it using measured data only
-- no S-matrix input.
"""
function richardson(σa::Real, va::Real, σb::Real, vb::Real)
    ua, ub = 1 / σa^2, 1 / σb^2
    B = (va - vb) / (ua - ub)
    return va - B * ua
end

# ------------------------------------------------------------ the scan ----

_jnum(x::Real) = isfinite(x) ? string(round(Float64(x), sigdigits = 12)) : "null"
_jnum(x::Integer) = string(x)
_jnum(x::Bool) = x ? "true" : "false"

function _jobj(io, pairs; indent = "    ")
    print(io, "{")
    first = true
    for (k, v) in pairs
        first || print(io, ",")
        first = false
        print(io, "\n", indent, "\"", k, "\": ", v isa AbstractString ? "\"$v\"" : _jnum(v))
    end
    print(io, "\n", indent[1:end-2], "}")
end

"""
Default scan grid: `(k_s, k_h)` pairs.  The last entry deliberately violates the
D8 requirement `|k_s| ≪ k_h` and is kept as a truncation stress test.
"""
const SCAN_GRID = [(0.30, 1.5), (-0.30, 1.5), (0.15, 1.5), (-0.15, 1.5),
                   (0.15, 0.8), (-0.15, 0.8), (0.30, 2.4), (-0.30, 2.4),
                   (-0.20, 3.0), (0.15, 0.4)]

"""
    displacement_scan(path; grid, sigmas, J, sep_factor, dt)

Run the whole `(k_s,k_h)` scan at several packet widths, extrapolate to zero
width, and write the record as JSON to `path`.  Returns the vector of per-grid
summaries.
"""
function displacement_scan(path::AbstractString; grid = SCAN_GRID,
                           sigmas = (8.0, 11.0, 14.0), J::Real = 1.0,
                           sep_factor::Real = 10.0, dt::Real = 2.0,
                           verbose::Bool = true)
    summaries = Any[]
    runs_json = String[]
    for (ks, kh) in grid
        rs = [collision_run(; J = J, ks = ks, kh = kh, σx = σ,
                            sep_factor = sep_factor, dt = dt) for σ in sigmas]
        ms = collect(sigmas)
        Rs = [richardson(ms[i], rs[i].delta_s, ms[j], rs[j].delta_s)
              for i in 1:length(ms)-1 for j in i+1:length(ms)]
        Rh = [richardson(ms[i], rs[i].delta_h, ms[j], rs[j].delta_h)
              for i in 1:length(ms)-1 for j in i+1:length(ms)]
        Δs = richardson(ms[end-1], rs[end-1].delta_s, ms[end], rs[end].delta_s)
        Δh = richardson(ms[end-1], rs[end-1].delta_h, ms[end], rs[end].delta_h)
        errs = max(maximum(Rs) - minimum(Rs), rs[end].delta_s_spread)
        errh = max(maximum(Rh) - minimum(Rh), rs[end].delta_h_spread)
        ex_s, ex_h = rs[end].pred_s_exact, rs[end].pred_h_exact
        or_s, or_h = rs[end].oracle_s, rs[end].oracle_h
        push!(summaries, (; ks, kh, Δs, Δh, errs, errh, ex_s, ex_h, or_s, or_h,
                          resolution = rs[end].resolution,
                          Nmax = rs[end].N, dimmax = rs[end].dim,
                          norm_drift = maximum(r.norm_drift for r in rs),
                          energy_drift = maximum(r.energy_drift for r in rs),
                          pre_s = rs[end].delta_s_pre, pre_h = rs[end].delta_h_pre))
        for (σ, r) in zip(sigmas, rs)
            push!(runs_json, sprint(io -> _jobj(io, Pair{String,Any}[
                "k_s" => ks, "k_h" => kh, "sigma_x" => σ, "N" => r.N,
                "dim" => r.dim, "T" => r.T, "dt" => r.dt, "nsteps" => r.nsteps,
                "resolution" => r.resolution,
                "delta_s" => r.delta_s, "delta_h" => r.delta_h,
                "delta_s_window" => r.delta_s_window,
                "delta_h_window" => r.delta_h_window,
                "delta_s_pre" => r.delta_s_pre, "delta_h_pre" => r.delta_h_pre,
                "delta_s_spread" => r.delta_s_spread,
                "delta_h_spread" => r.delta_h_spread,
                "packet_avg_s" => r.pred_s_avg, "packet_avg_h" => r.pred_h_avg,
                "norm_drift" => r.norm_drift, "energy_drift" => r.energy_drift,
                "krylov_ok" => r.krylov_ok]; indent = "        ")))
        end
        verbose && println("done (k_s,k_h)=($ks,$kh)  Δs=$(round(Δs,digits=6)) ",
                           "exact=$(round(ex_s,digits=6))  Δh=$(round(Δh,digits=6)) ",
                           "exact=$(round(ex_h,digits=6))")
    end
    sums_json = [sprint(io -> _jobj(io, Pair{String,Any}[
        "k_s" => s.ks, "k_h" => s.kh,
        "displacement_soft_measured" => s.Δs, "displacement_soft_error" => s.errs,
        "displacement_soft_exact_S" => s.ex_s, "displacement_soft_oracle" => s.or_s,
        "deviation_soft_vs_exact" => s.Δs - s.ex_s,
        "deviation_soft_vs_oracle" => s.Δs - s.or_s,
        "displacement_hard_measured" => s.Δh, "displacement_hard_error" => s.errh,
        "displacement_hard_exact_S" => s.ex_h, "displacement_hard_oracle" => s.or_h,
        "deviation_hard_vs_exact" => s.Δh - s.ex_h,
        "deviation_hard_vs_oracle" => s.Δh - s.or_h,
        "precollision_control_soft" => s.pre_s,
        "precollision_control_hard" => s.pre_h,
        "resolution" => s.resolution, "N_max" => s.Nmax, "dim_max" => s.dimmax,
        "norm_drift" => s.norm_drift, "energy_drift" => s.energy_drift];
        indent = "        ")) for s in summaries]
    mkpath(dirname(path))
    open(path, "w") do io
        println(io, "{")
        println(io, "  \"experiment\": \"FM two-magnon wavepacket scattering displacement\",")
        println(io, "  \"model\": \"H = -J sum (S.S - 1/4), spin-1/2 isotropic Heisenberg ferromagnet, periodic ring\",")
        println(io, "  \"convention\": \"Delta_s = -d(delta)/d k_s, Delta_h = -d(delta)/d k_h, delta = arg S_12(k_s,k_h) (D7)\",")
        println(io, "  \"oracle\": \"theory/oracle-bethe.md O7/O9: delta = 2 k_s + cot(k_h/2) k_s^2 + O(k_s^3)\",")
        println(io, "  \"J\": ", _jnum(J), ",")
        println(io, "  \"sep_factor\": ", _jnum(sep_factor), ",")
        println(io, "  \"sigma_x_values\": [", join(_jnum.(collect(sigmas)), ", "), "],")
        println(io, "  \"extrapolation\": \"Richardson in 1/sigma_x^2 on the two largest widths; error = spread over all width pairs, floored by the late-time drift\",")
        println(io, "  \"summary\": [\n    ", join(sums_json, ",\n    "), "\n  ],")
        println(io, "  \"runs\": [\n    ", join(runs_json, ",\n    "), "\n  ]")
        println(io, "}")
    end
    return summaries
end

end # module
