"""
testutils.jl — brute-force reference implementations used by the shard tests.

Everything here is deliberately written INDEPENDENTLY of `src/xxz_sector.jl`
(dense, exponential, obviously-correct) so that agreement is a real check and
not a restatement of the production code.
"""

using LinearAlgebra

"All 2^L spin configurations of the dynamical sites as BitVectors (true = up)."
function bf_all_configs(L::Int)
    out = Vector{BitVector}()
    for m in 0:(2^L - 1)
        c = falses(L)
        for j in 1:L
            c[j] = ((m >> (j - 1)) & 1) == 1
        end
        push!(out, c)
    end
    return out
end

"Full physical spin string (±1) for frozen boundary spins sL, sR and dynamical config."
function bf_spins(c::BitVector, sL::Int, sR::Int)
    s = Vector{Int}(undef, length(c) + 2)
    s[1] = sL
    s[end] = sR
    for j in 1:length(c)
        s[j+1] = c[j] ? 1 : -1
    end
    return s
end

bf_ndown(c::BitVector) = count(!, c)

function bf_domain_walls(c::BitVector, sL::Int, sR::Int)
    s = bf_spins(c, sL, sR)
    return count(x -> s[x] != s[x+1], 1:(length(s)-1))
end

"Ising (diagonal) energy  -J_z * sum_x S^z_x S^z_{x+1}  with S^z = s/2."
function bf_ising(c::BitVector, sL::Int, sR::Int, Jz::Float64)
    s = bf_spins(c, sL, sR)
    e = 0.0
    for x in 1:(length(s)-1)
        e -= Jz * (s[x] / 2) * (s[x+1] / 2)
    end
    return e
end

"""
Dense Hamiltonian on the full 2^L dynamical Hilbert space, frozen ends sL, sR.
Hopping lives only on bonds between two dynamical sites.
"""
function bf_dense_H(L::Int, sL::Int, sR::Int, Jperp::Float64, Delta::Float64)
    Jz = Delta * Jperp
    cfgs = bf_all_configs(L)
    idx = Dict(c => i for (i, c) in enumerate(cfgs))
    n = length(cfgs)
    H = zeros(Float64, n, n)
    for (i, c) in enumerate(cfgs)
        H[i, i] += bf_ising(c, sL, sR, Jz)
        for j in 1:(L-1)
            if c[j] != c[j+1]
                d = copy(c)
                d[j], d[j+1] = c[j+1], c[j]
                H[idx[d], i] -= Jperp / 2
            end
        end
    end
    return H, cfgs, idx
end
