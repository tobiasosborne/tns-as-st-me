"""
    Spin1TwoMagnon

Two-magnon sector of the **spin-S** isotropic Heisenberg *ferromagnet*, built to
falsify Conjecture Bc (theory/TRIANGLE.md §4, corner-b-draft.md §10) at `s = 1`.

Model (the spin-S generalisation of definitions.md D6, quoted not redefined):

    H = -J Σ_x ( S_x·S_{x+1} - S² ) ,   J > 0 ,   |Ω⟩ = |S,S,…⟩ ,  periodic ring.

With `n_x := S - S^z_x` the on-site magnon number,

    diagonal  = 2JS Σ_x n_x - J Σ_bonds n_x n_{x+1}
    hop a→b   = -(J/2) √(n_a(2S-n_a+1)) · √((n_b+1)(2S-n_b))

so the free hop is `-JS`, the hop that creates or destroys a doubly occupied
site is `-J g` with `g = √(S(2S-1))` (`g = 0` at `S = 1/2`: hard core), and the
adjacency energy is `-J`.  For `S ≥ 1` the two-magnon basis therefore carries
`N` extra doubly-occupied configurations on top of the `N(N-1)/2` hard-core ones.

**The question.**  Theorem S2-2body (FROZEN) gives, for `s = 1/2`,
`dδ_phys/dk_s|_0 = 2 sgn(v_h−v_s)`.  Conjecture Bc asserts this coefficient is
`|q_hard|/s`, hence `1` at `s = 1`.  This module measures it at `s = 1` three
independent ways:

1. `bethe_vector` — the coordinate-Bethe eigenvector built from the spin-`S`
   contact solution (`contact_numerator`).  Its residual `‖H₂ψ − Eψ‖` at
   Bethe--Yang quantised momenta is a machine-precision test of that solution.
2. `ring_phase_shift` / `soft_slope_rings` — **ansatz-free**: exact momentum-block
   spectra of the sector on rings up to a few hundred sites, converted to a
   phase shift by Bethe--Yang quantisation.  The only inputs are ED eigenvalues,
   the one-magnon dispersion, and the asymptotic two-free-magnon form.
3. `collision_run` (in `spin1_collision.jl`) — wavepacket dynamics, the same
   protocol as `fm_twomagnon.jl`, reading the soft packet's spatial displacement
   `Δ_s = -∂δ/∂k_s`.

The answer, from all three: `dδ/dk_s|_0 = 1/S`, i.e. `2` at `s = 1/2` (the
frozen value) and `1` at `s = 1`.  A first attempt at the contact algebra, which
treated the free extension `Ψ` as symmetric at the diagonal, gave a
spin-independent `2` and was **refuted by these numerics** before the algebra
was redone; the record is kept in `docs/spin1-twomagnon-notes.md`.

Only LinearAlgebra, SparseArrays, KrylovKit are used.  Standalone module,
included directly by numerics/test/test_spin1_twomagnon.jl; not part of
TriangleMPS.
"""
module Spin1TwoMagnon

using LinearAlgebra
using SparseArrays
using KrylovKit

export spin_ops, SpinPairBasis, pair_basis, pair_index,
       one_magnon_hamiltonian, two_magnon_hamiltonian,
       omega, group_velocity, double_hop, max_occupation,
       contact_numerator, smatrix, soft_phase, dphase_dk1, dphase_dk2,
       soft_slope_prediction,
       quantized_pair, bethe_vector,
       momentum_block, ring_phase_shift, soft_slope_rings,
       gaussian_packet, momentum_weights, packet_velocity,
       packet_average_displacement, two_magnon_product_state,
       one_body_density, centroid, chamber_positions,
       evolve, plan_geometry, collision_run, richardson,
       soft_slope_dynamical

# ------------------------------------------------------------ spin algebra ----

"""
    spin_ops(S) -> (Sx, Sy, Sz, Sp, Sm, d)

On-site spin-`S` matrices in the descending-`m` basis, `d = 2S+1`.
"""
function spin_ops(S::Real)
    d = Int(round(2S + 1))
    d == 2S + 1 || throw(ArgumentError("S must be a half-integer"))
    ms = [S - (i - 1) for i in 1:d]
    Sz = ComplexF64.(Diagonal(Float64.(ms)))
    Sp = zeros(ComplexF64, d, d)
    for i in 2:d
        m = ms[i]
        Sp[i-1, i] = sqrt(S * (S + 1) - m * (m + 1))
    end
    Sm = Matrix(adjoint(Sp))
    return (Sx = (Sp + Sm) / 2, Sy = (Sp - Sm) / (2im), Sz = Matrix(Sz),
            Sp = Sp, Sm = Sm, d = d)
end

"Maximum magnon occupation of one site: `n_max = 2S`."
max_occupation(S::Real) = Int(round(2S))

"Amplitude prefactor `g = √(S(2S-1))` of the double-occupancy hop."
double_hop(S::Real) = sqrt(S * (2S - 1))

"One-magnon dispersion `ω(k) = 2JS(1 - cos k)` (spin-S generalisation of O1)."
omega(k::Real, J::Real, S::Real) = 2 * J * S * (1 - cos(k))

"Group velocity `dω/dk = 2JS sin k`."
group_velocity(k::Real, J::Real, S::Real) = 2 * J * S * sin(k)

# ------------------------------------------------------------------ basis ----

"""
Two-magnon configuration basis on a ring of `N` sites: unordered pairs
`{x,y}`, `0 ≤ x ≤ y ≤ N-1`, with `x = y` (double occupancy) present iff
`2S ≥ 2`.  `index[x+1,y+1]` is the basis number, `0` when the configuration is
absent.
"""
struct SpinPairBasis
    N::Int
    S::Float64
    dim::Int
    pairs::Vector{Tuple{Int,Int}}
    index::Matrix{Int}
end

function pair_basis(N::Integer, S::Real)
    N >= 4 || throw(ArgumentError("need N ≥ 4"))
    doubles = max_occupation(S) >= 2
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
    return SpinPairBasis(Int(N), float(S), n, pairs, index)
end

pair_index(b::SpinPairBasis, x::Integer, y::Integer) = b.index[x+1, y+1]

# ------------------------------------------------- sector Hamiltonians ----

"""
One-magnon block: on-site energy `2JS`, hop `-JS` on each bond.
"""
function one_magnon_hamiltonian(N::Integer, J::Real, S::Real)
    I0 = Int[]; K0 = Int[]; V0 = Float64[]
    for x in 0:N-1
        push!(I0, x + 1); push!(K0, x + 1); push!(V0, 2 * J * S)
        for d in (-1, 1)
            y = mod(x + d, N)
            push!(I0, y + 1); push!(K0, x + 1); push!(V0, -J * S)
        end
    end
    return sparse(I0, K0, V0, N, N)
end

"Occupation of site `t` in the configuration `(x,y)`."
@inline _occ(x::Int, y::Int, t::Int) = (t == x ? 1 : 0) + (t == y ? 1 : 0)

"""
    two_magnon_hamiltonian(pb, J, S)

Two-magnon block by direct enumeration from the on-site `S^±` matrix elements.
No Bethe input of any kind: the diagonal is
`4JS - J Σ_bonds n_a n_b` and every hop carries
`-(J/2)√(n_a(2S-n_a+1))√((n_b+1)(2S-n_b))`.
"""
function two_magnon_hamiltonian(pb::SpinPairBasis, J::Real, S::Real)
    N = pb.N
    nmax = max_occupation(S)
    I0 = Int[]; K0 = Int[]; V0 = Float64[]
    sizehint!(I0, 5 * pb.dim); sizehint!(K0, 5 * pb.dim); sizehint!(V0, 5 * pb.dim)
    for (col, (x, y)) in enumerate(pb.pairs)
        # diagonal: 4JS minus J for every bond with both endpoints occupied
        diag = 4 * J * S
        if x != y && (mod(y - x, N) == 1 || mod(x - y, N) == 1)
            diag -= J * 1 * 1
        end
        push!(I0, col); push!(K0, col); push!(V0, diag)
        # hops: loop over DISTINCT occupied sites, moving one magnon
        sites = x == y ? ((x, 2),) : ((x, 1), (y, 1))
        for (a, na) in sites
            for d in (-1, 1)
                b = mod(a + d, N)
                nb = _occ(x, y, b)
                nb >= nmax && continue                     # site b is full
                amp = -(J / 2) * sqrt(na * (2S - na + 1)) * sqrt((nb + 1) * (2S - nb))
                # target configuration: one magnon moved from a to b
                rest = (a == x && a == y) ? a : (a == x ? y : x)
                t1, t2 = minmax(rest, b)
                row = pb.index[t1+1, t2+1]
                row == 0 && continue
                push!(I0, row); push!(K0, col); push!(V0, amp)
            end
        end
    end
    return sparse(I0, K0, V0, pb.dim, pb.dim)
end

# ------------------------------------------- the S-matrix under test ----

"""
    contact_numerator(k1, k2, S)

The single complex number that carries the whole spin-`S` contact problem,

    n(k₁,k₂;S) = 2Sc·cos q − e^{iq}[(2S−1)c + cos q] ,
    c = cos((k₁+k₂)/2) ,   q = (k₁−k₂)/2 .

Derivation (`docs/spin1-twomagnon-notes.md`).  Take the **unsymmetrised** free
solution `Ψ(x,y) = A z₁^x z₂^y + B z₂^x z₁^y` on all of `ℤ²` (it solves the free
two-magnon equation everywhere), identify `ψ = Ψ` only on the physical chamber
`x < y`, and let `ψ_d(x) = ρ w^x`, `w = z₁z₂`, be the doubly-occupied amplitude.
The doubly-occupied equation fixes `ρ = g P e^{−iK/2}/(2S cos q)` with
`P = A z₂ + B z₁`; the adjacent-pair equation then fixes

    (A e^{−iq} + B e^{iq})[(2S−1)c + cos q] = 2Sc·cos q·(A+B) ,

so that `S₁₂ = A/B = n/(−n̄)`.  Note the contact condition is **not**
spin-independent: at `S = 1/2` it collapses to the hard-core condition of the
frozen oracle, at `S ≥ 1` the doubly-occupied channel contributes the extra
`(2S−1)c` term.
"""
@inline function contact_numerator(k1::Real, k2::Real, S::Real)
    c = cos((k1 + k2) / 2)
    q = (k1 - k2) / 2
    return 2S * c * cos(q) - cis(q) * ((2S - 1) * c + cos(q))
end

"""
    smatrix(k1, k2, S)

Two-magnon coefficient ratio `S₁₂ = A₁₂/A₂₁ = n/(−n̄)`, `|S₁₂| = 1`, satisfying
`S₁₂(k₁,k₂)S₁₂(k₂,k₁) = 1`.  At `S = 1/2` it equals the frozen oracle formula
`−(z₁z₂−2z₁+1)/(z₁z₂−2z₂+1)` (checked in the tests).
"""
function smatrix(k1::Real, k2::Real, S::Real)
    n = contact_numerator(k1, k2, S)
    return -n / conj(n)
end

"Continuous phase branch `δ = arg S₁₂` with `δ(0,k_h) = 0` (D7)."
soft_phase(k1::Real, k2::Real, S::Real) = angle(smatrix(k1, k2, S))

"`∂n/∂k₁`, `∂n/∂k₂` of `contact_numerator`."
function _dnum(k1::Real, k2::Real, S::Real)
    K2 = (k1 + k2) / 2
    q = (k1 - k2) / 2
    c, cd = cos(K2), -sin(K2) / 2
    cq, sq = cos(q), sin(q)
    e = cis(q)
    br = (2S - 1) * c + cq                      # bracket
    out = ntuple(2) do j
        qd = j == 1 ? 0.5 : -0.5
        2S * cd * cq - 2S * c * sq * qd - im * qd * e * br -
            e * ((2S - 1) * cd - sq * qd)
    end
    return out
end

"""
`∂δ/∂k₁` (argument 1 is the SOFT leg, matching D7/O7).  Since
`δ = 2 arg n − π`, this is `2 Im(∂₁n / n)`.
"""
dphase_dk1(k1::Real, k2::Real, S::Real) =
    2 * imag(_dnum(k1, k2, S)[1] / contact_numerator(k1, k2, S))
"`∂δ/∂k₂` (argument 2 is the HARD leg)."
dphase_dk2(k1::Real, k2::Real, S::Real) =
    2 * imag(_dnum(k1, k2, S)[2] / contact_numerator(k1, k2, S))

"""
    soft_slope_prediction(S) = 1/S

Analytic soft slope `dδ/dk_s|_{k_s→0}` of the spin-`S` FM two-magnon phase.
Expanding `contact_numerator` at `k_s = 0` (with `h = k_h/2`, `γ = cos h`,
`σ = sin h`) gives `n = 2Sγ·iσ` and `n' = −σγ + i[σ²(1−S) − Sγ²]`, whence
`Im(n'/n) = 1/(2S)` — **all hard dependence cancels**, exactly as in the `s=1/2`
argument of Theorem S2-2body, and the coefficient is `1/S`.
"""
soft_slope_prediction(S::Real) = 1 / S

"""
Bethe--Yang quantisation on the ring: `N k_1 = 2π n_1 + δ`, `N k_2 = 2π n_2 - δ`
by fixed-point iteration.  Used only to build a test eigenvector.
"""
function quantized_pair(N::Integer, n1::Integer, n2::Integer, S::Real;
                        iters::Int = 400, tol::Float64 = 1e-14)
    k1 = 2π * n1 / N
    k2 = 2π * n2 / N
    for _ in 1:iters
        d = soft_phase(k1, k2, S)
        nk1 = (2π * n1 + d) / N
        nk2 = (2π * n2 - d) / N
        done = abs(nk1 - k1) < tol && abs(nk2 - k2) < tol
        k1, k2 = nk1, nk2
        done && break
    end
    return k1, k2
end

"""
    bethe_vector(pb, k1, k2, S)

Coordinate-Bethe eigenvector of the spin-`S` two-magnon sector,

    Ψ(x,y) = A z₁^x z₂^y + B z₂^x z₁^y ,  A = S₁₂ , B = 1 ,
    ψ(x,y) = Ψ(x,y)   (x < y) ,
    ψ_d(x) = ρ w^x ,  ρ = g (A z₂ + B z₁) e^{−iK/2} / (2S cos q) ,  w = z₁z₂ .

For `S = 1/2` the diagonal is absent (`g = 0`) and this is the standard FM Bethe
vector.  Its residual `‖H₂ψ − Eψ‖` is a machine-precision test of the whole
contact derivation.
"""
function bethe_vector(pb::SpinPairBasis, k1::Real, k2::Real, S::Real)
    A = smatrix(k1, k2, S)
    B = 1.0 + 0im
    z1, z2 = cis(k1), cis(k2)
    K = k1 + k2
    q = (k1 - k2) / 2
    g = double_hop(S)
    ρ = g == 0 ? 0.0 + 0im :
        g * (A * z2 + B * z1) * cis(-K / 2) / (2S * cos(q))
    v = Vector{ComplexF64}(undef, pb.dim)
    for (n, (x, y)) in enumerate(pb.pairs)
        v[n] = x == y ? ρ * cis(K * x) :
               A * cis(k1 * x + k2 * y) + B * cis(k2 * x + k1 * y)
    end
    return v / norm(v)
end

# --------------------------------------- momentum blocks (ansatz-free) ----

"Canonical translation label of the pair `{a,b}`: `r = min(d, N-d)`, `d=(b-a) mod N`."
@inline function _orbit_label(N::Int, a::Int, b::Int)
    d = mod(b - a, N)
    return min(d, N - d)
end

"Translation `t` with `{a,b} = T^t {0,r}`, `r` the canonical label."
@inline function _orbit_shift(N::Int, a::Int, b::Int, r::Int)
    return mod(b - a, N) == r ? a : b
end

"Period of the translation orbit of the representative `{0,r}`."
@inline _orbit_period(N::Int, r::Int) = (2r == N) ? N ÷ 2 : N

"""
    momentum_block(N, S, m; J=1.0) -> Matrix{ComplexF64}

The total-momentum `K = 2πm/N` block of the two-magnon sector, in the basis of
translation-orbit representatives `{0,r}`, `r = 0…⌊N/2⌋` (`r = 0` only for
`S ≥ 1`; `r = N/2` only when `K·N/2 ≡ 0 mod 2π`).  Built by acting with the same
enumerated Hamiltonian used in real space, so it inherits no extra assumptions.
The union of the block spectra over `m` equals the full sector spectrum (tested).
"""
function momentum_block(N::Integer, S::Real, m::Integer; J::Real = 1.0)
    N = Int(N)
    K = 2π * m / N
    nmax = max_occupation(S)
    rmin = nmax >= 2 ? 0 : 1
    rs = Int[]
    for r in rmin:(N ÷ 2)
        p = _orbit_period(N, r)
        # the momentum state exists only if e^{iKp} = 1
        abs(cis(K * p) - 1) < 1e-9 && push!(rs, r)
    end
    pos = Dict(r => i for (i, r) in enumerate(rs))
    dim = length(rs)
    M = zeros(ComplexF64, dim, dim)
    for (col, r) in enumerate(rs)
        a, b = 0, r
        pr = _orbit_period(N, r)
        # diagonal
        diag = 4 * J * S
        if a != b && (mod(b - a, N) == 1 || mod(a - b, N) == 1)
            diag -= J
        end
        M[col, col] += diag
        # hops out of the representative
        sites = a == b ? ((a, 2),) : ((a, 1), (b, 1))
        for (site, na) in sites
            for d in (-1, 1)
                tgt = mod(site + d, N)
                nb = _occ(a, b, tgt)
                nb >= nmax && continue
                amp = -(J / 2) * sqrt(na * (2S - na + 1)) * sqrt((nb + 1) * (2S - nb))
                rest = (site == a && site == b) ? site : (site == a ? b : a)
                c1, c2 = minmax(rest, tgt)
                rp = _orbit_label(N, c1, c2)
                haskey(pos, rp) || continue
                t = _orbit_shift(N, c1, c2, rp)
                prp = _orbit_period(N, rp)
                M[pos[rp], col] += sqrt(pr / prp) * amp * cis(-K * t)
            end
        end
    end
    return M
end

"""
    ring_phase_shift(N, S, kh_target; J=1.0)

**Ansatz-free** extraction of the two-magnon phase shift at the smallest
non-zero soft momentum available on an `N`-site ring.

Method.  Pick the total-momentum block `K = 2πm/N` with `m = round(k_h N/2π) + 1`,
diagonalise it exactly, and keep the eigenvalues inside the two-magnon continuum
`|E - 4JS| ≤ 4JS|cos(K/2)|`.  Each such `E` is inverted through
`E = ω(k_1)+ω(k_2)`, `k_1+k_2 = K` — i.e. only the *asymptotic two-free-magnon*
form is assumed, never a wavefunction ansatz — and the Bethe--Yang condition
`N k_s = 2π n_s + δ` then gives `δ`.  The level with `n_s = 1` is returned.
"""
function ring_phase_shift(N::Integer, S::Real, kh_target::Real; J::Real = 1.0,
                          band_tol::Real = 1e-9)
    N = Int(N)
    m = round(Int, kh_target * N / (2π)) + 1
    K = 2π * m / N
    A = 4 * J * S * cos(K / 2)
    E0 = 4 * J * S
    M = momentum_block(N, S, m; J = J)
    evs = real.(eigvals(Hermitian(M)))
    best = nothing
    for E in evs
        abs(E - E0) <= abs(A) + band_tol || continue        # outside the continuum
        c = clamp((E0 - E) / A, -1.0, 1.0)
        q = acos(c)
        ks = K / 2 - q
        kh = K / 2 + q
        kh = kh > π ? kh - 2π : kh
        n_soft = round(Int, N * ks / (2π))
        n_soft == 1 || continue
        δ = N * ks - 2π * n_soft
        best = (N = N, S = float(S), J = float(J), m = m, K = K, E = E,
                ks = ks, kh = kh, delta = δ, n_soft = n_soft,
                slope = δ / ks, nlevels = length(evs))
    end
    best === nothing && throw(ErrorException(
        "no continuum level with n_soft = 1 at N=$N, S=$S, kh≈$kh_target"))
    return best
end

"""
    soft_slope_rings(S; kh_target, Ns, J=1.0)

The soft phase slope `dδ/dk_s|_{k_s→0}` from exact ring spectra.  For each `N`
in `Ns` the extractor gives `(k_s, δ)` with `k_s ≈ 2π/N`; the ratios `δ/k_s` are
extrapolated to `k_s = 0` by a straight-line least-squares fit in `k_s` (the
leading correction is `O(k_s)`, from the `cot(k_h/2)k_s²` term of the phase).
The reported error is the larger of the fit residual scale and the spread of the
two-point extrapolations from consecutive `N`, so it is a *measured* uncertainty
and not a quoted tolerance.
"""
function soft_slope_rings(S::Real; kh_target::Real = 1.5,
                          Ns = (60, 90, 120, 180, 240), J::Real = 1.0)
    rows = [ring_phase_shift(N, S, kh_target; J = J) for N in Ns]
    x = [r.ks for r in rows]
    y = [r.slope for r in rows]
    n = length(x)
    xb = sum(x) / n; yb = sum(y) / n
    den = sum((x .- xb) .^ 2)
    b = den > 0 ? sum((x .- xb) .* (y .- yb)) / den : 0.0
    a = yb - b * xb
    resid = sqrt(sum((y .- (a .+ b .* x)) .^ 2) / max(1, n - 2))
    pairwise = Float64[]
    for i in 1:n-1, j in i+1:n
        x[i] == x[j] && continue
        push!(pairwise, y[i] - (y[j] - y[i]) / (x[j] - x[i]) * x[i])
    end
    spread = isempty(pairwise) ? 0.0 : maximum(pairwise) - minimum(pairwise)
    return (slope = a, err = max(resid, spread), fit_slope = b,
            resid = resid, spread = spread, rows = rows,
            kh_target = float(kh_target), S = float(S))
end

include("spin1_collision.jl")

end # module
