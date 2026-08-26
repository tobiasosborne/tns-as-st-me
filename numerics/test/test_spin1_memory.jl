# test_spin1_memory.jl -- red/green tests for the spin-1 easy-axis memory
# quantum (Conjecture Bc falsifier (B), bd tns-8e9; corner-b-draft.md §9 P8).
#
# Standalone shard test: includes ../src/spin1_memory.jl.  It also loads
# TriangleMPS, but only to CROSS-CHECK the new general-spin code against the
# frozen spin-1/2 implementation (identical bases, identical spectra) -- the
# spin-1 numbers never touch it.
#
# PASS CRITERIA ARE FIXED HERE IN ADVANCE OF ANY PRODUCTION RUN.
#   TOL_XCHECK   agreement with the frozen spin-1/2 sector code
#   TOL_BF       agreement with a brute-force dense (2s+1)^L Hamiltonian
#   TOL_CONSERVE norm / energy drift over the whole evolution
#   RATIO_BAND   8% band on the measured ratio delta x / N_T, the SAME
#                criterion already used for numerics/results/memory-scan-1.json.
#                Conjecture Bc predicts -1/s: -2 at s = 1/2, -1 at s = 1.

# Wrapped in `module TestSpin1Memory` so that numerics/test/runtests.jl can
# include every shard test into one process: the shard modules export
# names that also exist in TriangleMPS / FMTwoMagnon, and `using` them
# all into a shared `Main` makes those names ambiguous.

module TestSpin1Memory

using Test
using LinearAlgebra
import TriangleMPS

include(joinpath(@__DIR__, "..", "src", "spin1_memory.jl"))
using .Spin1Memory

const TOL_XCHECK   = 1.0e-10
const TOL_BF       = 1.0e-9
const TOL_CONSERVE = 1.0e-10
const RATIO_BAND   = 0.08

# ---------------------------------------------------------------------------
# Brute-force reference: dense (2s+1)^L Hamiltonian for the frozen-boundary
# easy-axis chain, built from Kronecker products.  Independent of the sector
# enumeration in src/spin1_memory.jl.
# ---------------------------------------------------------------------------

function bf_ops(s::Real)
    d = Int(round(2s + 1))
    ms = [s - (i - 1) for i in 1:d]
    Sz = ComplexF64.(Diagonal(Float64.(ms)))
    Sp = zeros(ComplexF64, d, d)
    for i in 2:d
        m = ms[i]
        Sp[i-1, i] = sqrt(s * (s + 1) - m * (m + 1))
    end
    return (Sz = Matrix(Sz), Sp = Sp, Sm = Matrix(adjoint(Sp)), d = d, ms = ms)
end

function bf_embed(op, j, L, d)
    M = Matrix{ComplexF64}(I, 1, 1)
    for x in 1:L
        M = kron(M, x == j ? ComplexF64.(op) : Matrix{ComplexF64}(I, d, d))
    end
    return M
end

"""
Dense `H` on the `L = N-2` dynamical sites with frozen spins `σL`, `σR`
(values of `S^z`, i.e. `±s`) on the two ends.
"""
function bf_chain_H(L::Int, s::Real, Jperp::Real, Delta::Real, σL::Real, σR::Real)
    o = bf_ops(s)
    d = o.d
    D = d^L
    Jz = Delta * Jperp
    H = zeros(ComplexF64, D, D)
    Z = [bf_embed(o.Sz, j, L, d) for j in 1:L]
    P = [bf_embed(o.Sp, j, L, d) for j in 1:L]
    M = [bf_embed(o.Sm, j, L, d) for j in 1:L]
    H .-= Jz .* σL .* Z[1]                       # frozen bond (1,2)
    H .-= Jz .* σR .* Z[L]                       # frozen bond (N-1,N)
    for j in 1:(L-1)
        H .-= (Jperp / 2) .* (P[j] * M[j+1] + M[j] * P[j+1])
        H .-= Jz .* (Z[j] * Z[j+1])
    end
    return H, o
end

"Total magnon number `Σ_j (s - S^z_j)` on the `d^L` product basis."
function bf_total_nmag(L::Int, s::Real)
    o = bf_ops(s)
    d = o.d
    out = zeros(Float64, d^L)
    for idx in 0:(d^L - 1)
        acc = 0.0
        r = idx
        for _ in 1:L
            acc += s - o.ms[(r % d) + 1]
            r ÷= d
        end
        out[idx+1] = acc
    end
    return out
end

@testset "spin-1 easy-axis memory quantum (Bc falsifier B)" begin

    @testset "configuration encoding and the excitation count D" begin
        ch = SpinChain(10; s = 1.0, Delta = 2.0, boundary = :kink)
        L = nsites_dynamical(ch)
        @test L == 8
        # monotone (pure wall) configurations have D = 0
        @test tv_excitations(ch, UInt8[0, 0, 0, 1, 2, 2, 2, 2]) == 0
        @test tv_excitations(ch, UInt8[0, 0, 0, 0, 2, 2, 2, 2]) == 0
        @test tv_excitations(ch, UInt8[0, 0, 1, 1, 1, 2, 2, 2]) == 0
        # one magnon on the up side / on the down side: D = 1
        @test tv_excitations(ch, UInt8[0, 1, 0, 0, 2, 2, 2, 2]) == 1
        @test tv_excitations(ch, UInt8[0, 0, 0, 0, 2, 2, 1, 2]) == 1
        # a doubly-flipped site in the up sea counts as two magnons
        @test tv_excitations(ch, UInt8[0, 2, 0, 0, 2, 2, 2, 2]) == 2
        # for s = 1/2 the count is (domain walls - 1)/1 exactly
        c12 = SpinChain(10; s = 0.5, Delta = 2.0, boundary = :kink)
        tri = TriangleMPS.XXZChain(10; Delta = 2.0, boundary = :kink)
        for bits in Iterators.product(ntuple(_ -> (false, true), 8)...)
            bv = BitVector(collect(bits))
            cfg = UInt8[b ? 0x00 : 0x01 for b in bv]
            @test tv_excitations(c12, cfg) == (TriangleMPS.domain_walls(tri, bv) - 1) ÷ 2
        end
    end

    @testset "sector basis reproduces the frozen spin-1/2 enumeration" begin
        for (N, nd, dmax) in ((12, 5, 1), (12, 5, 2), (14, 6, 1))
            ch = SpinChain(N; s = 0.5, Delta = 2.0, boundary = :kink)
            tri = TriangleMPS.XXZChain(N; Delta = 2.0, boundary = :kink)
            b = sector_basis(ch; nmag = nd, dmax = dmax)
            bt = TriangleMPS.sector_basis(tri; ndown = nd, dwmax = 2 * dmax + 1)
            mine = Set(BitVector([c == 0x00 for c in cfg]) for cfg in b.configs)
            theirs = Set(bt.configs)
            @test mine == theirs
            @test length(b) == length(bt)
            # ... and the same operator, up to basis ordering
            e1 = sort(eigvals(Symmetric(Matrix(build_hamiltonian(b)))))
            e2 = sort(eigvals(Symmetric(Matrix(TriangleMPS.build_hamiltonian(bt)))))
            @test maximum(abs.(e1 .- e2)) < TOL_XCHECK
        end
    end

    @testset "spin-1 Hamiltonian vs brute-force dense ED" begin
        N, s, Jp, Δ = 8, 1.0, 1.0, 2.3
        L = N - 2
        ch = SpinChain(N; s = s, Jperp = Jp, Delta = Δ, boundary = :kink)
        Hbf, _ = bf_chain_H(L, s, Jp, Δ, s, -s)
        tot = bf_total_nmag(L, s)
        for nm in (L - 1, L, L + 1)
            b = sector_basis(ch; nmag = nm, dmax = nothing)      # untruncated
            idx = findall(x -> abs(x - nm) < 1e-9, tot)
            @test length(b) == length(idx)
            e1 = sort(eigvals(Symmetric(Matrix(build_hamiltonian(b)))))
            e2 = sort(real.(eigvals(Hermitian(Hbf[idx, idx]))))
            @test maximum(abs.(e1 .- e2)) < TOL_BF
        end
    end

    @testset "single-magnon dispersion and packet velocity" begin
        for s in (0.5, 1.0)
            ch = SpinChain(120; s = s, Delta = 2.0, boundary = :up)
            # ω(k) = 2 s J_⊥ (Δ - cos k),  v = 2 s J_⊥ sin k
            @test isapprox(magnon_dispersion(ch, 0.0), 2s * (2.0 - 1.0); atol = 1e-12)
            @test isapprox(magnon_velocity(ch, 1.2), 2s * sin(1.2); atol = 1e-12)
            v = free_magnon_velocity(; N = 120, s = s, Delta = 2.0, k0 = 1.2,
                                     sigma = 5.0, x0 = 40.0, T = 12.0, dt = 0.25)
            @test isapprox(v, magnon_velocity(ch, 1.2); rtol = 0.03)
        end
    end

    @testset "spin-1/2 control: the frozen memory quantum -2 is reproduced" begin
        r = memory_experiment(; N = 100, s = 0.5, Delta = 2.0, k0 = 1.2, sigma = 4.0,
                              standoff = 28.0, dmax = 1, dt = 0.4)
        @test r.trapped_final < 1e-3
        @test maximum(abs.(r.norms .- 1)) < TOL_CONSERVE
        @test maximum(abs.(r.energies .- r.energies[1])) < 1e-9
        # the initial state really is one magnon, all of it on the up side
        @test abs(r.Rw[1] - 1.0) < 1e-6
        @test abs(r.Tw[1]) < 1e-6
        @test abs(r.ratio2 - (-2.0)) < RATIO_BAND * 2
    end

    @testset "DECISION: spin-1 memory quantum" begin
        # Fixed in advance: the ratio δx/N_T must equal -1/s.  For s = 1 that is
        # -1 (Conjecture Bc survives) rather than -2 (Bc falsified).
        r = memory_experiment(; N = 100, s = 1.0, Delta = 3.0, k0 = 1.2, sigma = 4.0,
                              standoff = 28.0, dmax = 1, dt = 0.4)
        @test r.trapped_final < 1e-2
        @test maximum(abs.(r.norms .- 1)) < TOL_CONSERVE
        @test abs(r.Rw[1] - 1.0) < 1e-6
        @test abs(r.Tw[1]) < 1e-6
        bc_survives  = abs(r.ratio2 - (-1.0)) < RATIO_BAND * 1
        bc_falsified = abs(r.ratio2 - (-2.0)) < RATIO_BAND * 2
        @info "spin-1 memory ratio" ratio = r.ratio2 T = r.T_final dx = r.dx2 bc_survives bc_falsified
        @test bc_survives != bc_falsified
        @test bc_survives
    end

    @testset "JSON serialisation" begin
        r = memory_experiment(; N = 80, s = 1.0, Delta = 3.0, k0 = 1.2, sigma = 3.0,
                              standoff = 16.0, dmax = 1, dt = 0.5, halfwidth = 5,
                              buffer = 5)
        js = to_json(r; trajectory = false)
        @test occursin("\"dx2\"", js)
        @test occursin("\"spin\"", js)
        @test occursin("\"ratio_dx2_over_T\"", js)
        @test !occursin("NaN", js) && !occursin("Inf", js)
    end

end

end # module TestSpin1Memory
