"""
Three-magnon exact-diagonalisation oracle for a soft magnon scattering from
the charge-two Bethe bound state of the spin-1/2 Heisenberg ferromagnet (D6).

The production measurement uses only the enumerated three-magnon Hamiltonian
and wavepacket evolution. The fused Bethe phase is carried separately as an
analytic comparison and is never used to evolve or fit the ED data.
"""
module BcCharge2ED

using LinearAlgebra
using SparseArrays
using KrylovKit

export ThreeBasis, three_basis, three_magnon_hamiltonian,
       PairBasis, pair_basis, two_magnon_hamiltonian,
       one_magnon_hamiltonian, bound_energy, bound_velocity,
       fused_smatrix, fused_phase_slope, collision_row,
       spectral_collision, measured_charge2_slope

struct ThreeBasis
    N::Int
    states::Vector{NTuple{3,Int}}
    index::Dict{NTuple{3,Int},Int}
end

struct PairBasis
    N::Int
    states::Vector{Tuple{Int,Int}}
    index::Matrix{Int}
end

function pair_basis(N::Integer)
    states = Tuple{Int,Int}[]
    index = zeros(Int, N, N)
    for x in 0:N-2, y in x+1:N-1
        push!(states, (x,y))
        i = length(states)
        index[x+1,y+1] = i
        index[y+1,x+1] = i
    end
    return PairBasis(Int(N), states, index)
end

"""All hard-core three-magnon configurations on an N-site ring."""
function three_basis(N::Integer)
    N >= 6 || throw(ArgumentError("need N >= 6"))
    states = NTuple{3,Int}[]
    sizehint!(states, binomial(N, 3))
    for x in 0:N-3, y in x+1:N-2, z in y+1:N-1
        push!(states, (x, y, z))
    end
    index = Dict(s => i for (i, s) in enumerate(states))
    return ThreeBasis(Int(N), states, index)
end

@inline adjacent_ring(x::Int, y::Int, N::Int) = mod(x-y, N) in (1, N-1)

"""
The D6 Hamiltonian in the three-down-spin sector, independently enumerated:
diagonal J per magnon minus J per occupied bond, and hopping -J/2 to an empty
nearest neighbour. This is an O(N^3) basis with at most seven entries/column.
"""
function three_magnon_hamiltonian(tb::ThreeBasis, J::Real = 1.0;
                                  hopping_scale::Real = 1.0)
    N = tb.N
    rows = Int[]; cols = Int[]; vals = Float64[]
    sizehint!(rows, 7length(tb.states)); sizehint!(cols, 7length(tb.states))
    sizehint!(vals, 7length(tb.states))
    for (col, state) in enumerate(tb.states)
        occ = Set(state)
        nbonds = adjacent_ring(state[1], state[2], N) +
                 adjacent_ring(state[1], state[3], N) +
                 adjacent_ring(state[2], state[3], N)
        push!(rows, col); push!(cols, col); push!(vals, J * (3 - nbonds))
        for a in state, d in (-1, 1)
            b = mod(a + d, N)
            b in occ && continue
            moved = collect(state)
            moved[findfirst(==(a), moved)] = b
            sort!(moved)
            target = (moved[1], moved[2], moved[3])
            push!(rows, tb.index[target]); push!(cols, col)
            push!(vals, -J * hopping_scale / 2)
        end
    end
    return sparse(rows, cols, vals, length(tb.states), length(tb.states))
end

function one_magnon_hamiltonian(N::Integer, J::Real = 1.0)
    rows = Int[]; cols = Int[]; vals = Float64[]
    for x in 0:N-1
        push!(rows, x+1); push!(cols, x+1); push!(vals, J)
        for d in (-1, 1)
            push!(rows, mod(x+d, N)+1); push!(cols, x+1); push!(vals, -J/2)
        end
    end
    return sparse(rows, cols, vals, N, N)
end

function two_magnon_hamiltonian(pb::PairBasis, J::Real = 1.0)
    N = pb.N
    rows = Int[]; cols = Int[]; vals = Float64[]
    for (col, (x,y)) in enumerate(pb.states)
        nadj = adjacent_ring(x,y,N)
        push!(rows,col); push!(cols,col); push!(vals,J*(2-nadj))
        for a in (x,y), d in (-1,1)
            b = mod(a+d,N)
            b == x && continue
            b == y && continue
            other = a == x ? y : x
            p,q = minmax(other,b)
            push!(rows,pb.index[p+1,q+1]); push!(cols,col); push!(vals,-J/2)
        end
    end
    return sparse(rows,cols,vals,length(pb.states),length(pb.states))
end

velocity(k::Real, J::Real = 1.0) = J * sin(k)
bound_energy(K::Real, J::Real = 1.0) = J * sin(K/2)^2
bound_velocity(K::Real, J::Real = 1.0) = J * sin(K) / 2

"""Fused 1-string/2-string phase, kept separate from the ED measurement."""
function fused_smatrix(ks::Real, K::Real)
    lambda_s = 0.5 / tan(ks/2)
    lambda_b = 1.0 / tan(K/2)
    u = lambda_s - lambda_b
    return ((u + 0.5im) * (u + 1.5im)) /
           ((u - 0.5im) * (u - 1.5im))
end

function fused_phase_slope(K::Real; h::Real = 1e-6)
    return imag(log(fused_smatrix(h, K) / fused_smatrix(-h, K))) / (2h)
end

function gaussian_packet(N::Int, k::Real, X::Real, sigma::Real)
    phi = [exp(-(x-X)^2/(4sigma^2)) * cis(k*x) for x in 0:N-1]
    return phi / norm(phi)
end

"""
Localized two-string packet. The q quadrature superposes exact infinite-line
relative waves cos((K+q)/2)^(r-1), rather than freezing their decay length.
The packet is placed far enough from the seam that omitted periodic images
are below the reported preparation leakage.
"""
function bound_packet_matrix(N::Int, K::Real, X::Real, sigma::Real;
                             nq::Int = 61, qmax::Real = 0.85)
    B = zeros(ComplexF64, N, N)
    for x in 0:N-2, y in x+1:N-1
        C = (x+y)/2
        r = y-x
        a = zero(ComplexF64)
        for q in range(-qmax, qmax; length=nq)
            Kq = K + q
            w = exp(-sigma^2*q^2)
            a += w * cis(K*C + q*(C-X)) * cos(Kq/2)^(r-1)
        end
        B[x+1,y+1] = a
        B[y+1,x+1] = a
    end
    return B / norm(B)
end

function product_state(tb::ThreeBasis, soft::AbstractVector, bound::AbstractMatrix)
    psi = Vector{ComplexF64}(undef, length(tb.states))
    for (i, (x,y,z)) in enumerate(tb.states)
        psi[i] = soft[x+1]*bound[y+1,z+1] +
                 soft[y+1]*bound[x+1,z+1] +
                 soft[z+1]*bound[x+1,y+1]
    end
    return psi / norm(psi)
end

pair_vector(pb::PairBasis, B::AbstractMatrix) =
    normalize!([B[x+1,y+1] for (x,y) in pb.states])

function evolve(H, psi::AbstractVector, T::Real; chunk::Real = 8.0,
                krylovdim::Int = 50, tol::Real = 2e-10)
    u = ComplexF64.(psi)
    nstep = max(1, ceil(Int, abs(T)/chunk))
    dt = T/nstep
    for _ in 1:nstep
        u, _ = exponentiate(H, -im*dt, u; ishermitian=true,
                            krylovdim=krylovdim, tol=tol, eager=true)
    end
    return u
end

centroid(prob::AbstractVector) = sum((0:length(prob)-1) .* prob) / sum(prob)

"""
Read the transmitted channel after the collision. In ordered coordinates
x<y<z the right two-string has gap z-y smaller than y-x; the isolated soft
magnon is x. The returned channel weight makes this classifier auditable.
"""
function transmitted_soft_position(tb::ThreeBasis, psi::AbstractVector)
    mass = 0.0; xpos = 0.0
    for (i, (x,y,z)) in enumerate(tb.states)
        p = abs2(psi[i])
        if z-y < y-x
            mass += p
            xpos += x*p
        end
    end
    return xpos/mass, mass
end

"""One ED wavepacket collision; no Bethe phase enters the measured shift."""
function collision_row(H3, H1, tb::ThreeBasis; ks::Real, K::Real=pi/2,
                       J::Real=1.0, sigma::Real=3.5, Xb::Real=8.0,
                       separation::Real=18.0)
    Xs = Xb + separation
    vb = bound_velocity(K, J)
    vs = velocity(ks, J)
    vb > vs || throw(ArgumentError("bound packet must overtake soft packet"))
    T = 2separation/(vb-vs)
    soft = gaussian_packet(tb.N, ks, Xs, sigma)
    bound = bound_packet_matrix(tb.N, K, Xb, sigma)
    psi0 = product_state(tb, soft, bound)
    psi = evolve(H3, psi0, T)
    soft_free = evolve(H1, soft, T)
    xsoft, transmission = transmitted_soft_position(tb, psi)
    xfree = centroid(abs2.(soft_free))
    shift = xsoft - xfree
    return (N=tb.N, ks=Float64(ks), K=Float64(K), T=T,
            shift=shift, slope=-shift, transmission=transmission,
            norm_drift=abs(norm(psi)-1), free_norm_drift=abs(norm(soft_free)-1))
end

"""
Momentum-resolved ED readout. A zero-centred soft packet collides with the
two-string. The final state is projected on the independently propagated
bound packet in the right chamber. For each ring momentum, the phase of the
ratio to the independently propagated soft packet is the measured scattering
phase up to a momentum-independent projection phase. Symmetric differences
at the first two nonzero ring momenta are extrapolated in k^2 to k=0.
"""
function spectral_collision(; N::Int=100, J::Real=1.0, K::Real=pi/2,
                            sigma::Real=8.0, Xb::Real=10.0,
                            separation::Real=28.0,
                            hopping_scale::Real=1.0)
    tb = three_basis(N)
    pb = pair_basis(N)
    H3 = three_magnon_hamiltonian(tb,J; hopping_scale=hopping_scale)
    H2 = two_magnon_hamiltonian(pb,J)
    H1 = one_magnon_hamiltonian(N,J)
    Xs = Xb + separation
    # Two crossing times: the packets recover their initial centre separation.
    # The broad sigma=8 soft packet suppresses quadratic dispersive clipping.
    T = 2separation/bound_velocity(K,J)
    soft = gaussian_packet(N,0.0,Xs,sigma)
    B = bound_packet_matrix(N,K,Xb,sigma)
    bound = pair_vector(pb,B)
    psi0 = product_state(tb,soft,B)
    psi = evolve(H3,psi0,T)
    bfree = evolve(H2,bound,T)
    sfree = evolve(H1,soft,T)

    # Project only the outgoing ordering soft | bound-bound, at fixed hard
    # momentum K.  The fixed-K two-string propagation phase is a k-independent
    # constant and therefore drops out of the soft phase derivative.  Using
    # the freely propagated localized packet here would mix in hard recoil.
    decay = cos(K/2)
    bK = ComplexF64[cis(K*(y+z)/2) *
         (decay^(z-y-1) + cis(-K*N/2)*decay^(N-(z-y)-1))
         for (y,z) in pb.states]
    normalize!(bK)
    bK_residual = norm(H2*bK-bound_energy(K,J)*bK)
    sout = zeros(ComplexF64,N)
    projected_norm = 0.0
    for x in 0:N-3
        a = zero(ComplexF64)
        for y in x+1:N-2, z in y+1:N-1
            a += conj(bK[pb.index[y+1,z+1]]) * psi[tb.index[(x,y,z)]]
        end
        sout[x+1] = a
        projected_norm += abs2(a)
    end

    function fourier_at(v,k)
        return sum(v[x+1]*cis(-k*x) for x in 0:N-1) / sqrt(N)
    end
    phase = Dict{Int,Float64}()
    ratio_abs = Dict{Int,Float64}()
    for n in -2:2
        k = 2pi*n/N
        ratio = fourier_at(sout,k)/fourier_at(sfree,k)
        phase[n] = angle(ratio)
        ratio_abs[n] = abs(ratio)
    end
    # Branch-safe relative phases centered at n=0.
    rel(n) = angle(cis(phase[n]-phase[0]))
    k1 = 2pi/N; k2 = 4pi/N
    d1 = (rel(1)-rel(-1))/(2k1)
    d2 = (rel(2)-rel(-2))/(2k2)
    slope = (d1*k2^2-d2*k1^2)/(k2^2-k1^2)
    stderr = max(abs(slope-d1), abs(d1-d2)/3)
    return (slope=slope, stderr=stderr, derivatives=(d1,d2),
            momenta=(k1,k2), phase=phase, ratio_abs=ratio_abs,
            projected_norm=projected_norm, N=N, dim=length(tb.states), T=T,
            bK_residual=bK_residual,
            norm_drift=abs(norm(psi)-1), bound_norm_drift=abs(norm(bfree)-1),
            free_norm_drift=abs(norm(sfree)-1),
            bethe_slope=fused_phase_slope(K))
end

"""
Measured charge-2 slope. Symmetrising +/-ks removes the first odd correction;
the two |ks| values are extrapolated linearly in ks^2. The quoted uncertainty
is conservative: the larger of the fit shift at the softer point and half the
unsymmetrised spread, combined in quadrature.
"""
function measured_charge2_slope(; N::Int=100, J::Real=1.0, K::Real=pi/2,
                                kmags=(0.06,0.10), sigma::Real=8.0,
                                Xb::Real=10.0, separation::Real=28.0,
                                hopping_scale::Real=1.0)
    tb = three_basis(N)
    H3 = three_magnon_hamiltonian(tb,J; hopping_scale=hopping_scale)
    H1 = one_magnon_hamiltonian(N,J)
    rows = NamedTuple[]
    symmetric = Float64[]
    for k in kmags
        rp = collision_row(H3,H1,tb;ks=k,K=K,J=J,sigma=sigma,
                           Xb=Xb,separation=separation)
        rm = collision_row(H3,H1,tb;ks=-k,K=K,J=J,sigma=sigma,
                           Xb=Xb,separation=separation)
        push!(rows,rp); push!(rows,rm)
        push!(symmetric,(rp.slope+rm.slope)/2)
    end
    x1,x2 = kmags[1]^2,kmags[2]^2
    slope = (symmetric[1]*x2-symmetric[2]*x1)/(x2-x1)
    stderr = abs(slope-symmetric[1])
    return (slope=slope,stderr=stderr,rows=rows,symmetric=symmetric,
            bethe_slope=fused_phase_slope(K),dim=length(tb.states))
end

end
