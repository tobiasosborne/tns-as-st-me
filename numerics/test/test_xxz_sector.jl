using Test
using LinearAlgebra
using SparseArrays
using TriangleMPS

include(joinpath(@__DIR__, "testutils.jl"))

@testset "xxz_sector" begin

    @testset "conventions / chain construction" begin
        ch = XXZChain(10; Jperp=1.0, Delta=3.0, boundary=:kink)
        @test ch.N == 10
        @test TriangleMPS.nsites_dynamical(ch) == 8
        @test TriangleMPS.frozen_left(ch) == 1     # sigma_1 = up
        @test TriangleMPS.frozen_right(ch) == -1   # sigma_N = down
        @test TriangleMPS.Jz(ch) ≈ 3.0
        up = XXZChain(10; Jperp=1.0, Delta=3.0, boundary=:up)
        @test TriangleMPS.frozen_right(up) == 1
    end

    @testset "domain walls and Ising energy vs brute force" begin
        L = 6
        ch = XXZChain(L + 2; Jperp=1.0, Delta=2.5, boundary=:kink)
        for c in bf_all_configs(L)
            @test domain_walls(ch, c) == bf_domain_walls(c, 1, -1)
            @test ising_energy(ch, c) ≈ bf_ising(c, 1, -1, 2.5)
        end
    end

    @testset "full-sector enumeration matches brute force" begin
        L = 8
        ch = XXZChain(L + 2; Jperp=1.0, Delta=2.0, boundary=:kink)
        for n in 0:L
            b = sector_basis(ch; ndown=n)
            ref = sort([c for c in bf_all_configs(L) if bf_ndown(c) == n])
            @test length(b) == binomial(L, n)
            @test sort(b.configs) == ref
            # index map is a genuine inverse
            for (i, c) in enumerate(b.configs)
                @test b.index[c] == i
            end
        end
    end

    @testset "domain-wall-truncated enumeration matches brute force" begin
        L = 9
        ch = XXZChain(L + 2; Jperp=1.0, Delta=2.0, boundary=:kink)
        for n in 0:L, dwmax in (1, 3, 5)
            b = sector_basis(ch; ndown=n, dwmax=dwmax)
            ref = sort([c for c in bf_all_configs(L)
                        if bf_ndown(c) == n && bf_domain_walls(c, 1, -1) <= dwmax])
            @test sort(b.configs) == ref
        end
        # kink chain: exactly one 1-domain-wall configuration per S^z sector
        for n in 0:L
            @test length(sector_basis(ch; ndown=n, dwmax=1)) == 1
            @test sector_basis(ch; ndown=n, dwmax=1).configs[1] == sharp_kink_config(ch, n)
        end
        # up chain, one flipped spin = L single-magnon position states
        up = XXZChain(L + 2; Jperp=1.0, Delta=2.0, boundary=:up)
        @test length(sector_basis(up; ndown=1, dwmax=2)) == L
    end

    @testset "3-domain-wall dimension is O(N^2) and matches the closed formula" begin
        # counting argument recorded in numerics/docs/kink-sector-notes.md
        for L in (8, 9, 12), n in 1:(L-1)
            ch = XXZChain(L + 2; Jperp=1.0, Delta=2.0, boundary=:kink)
            b = sector_basis(ch; ndown=n, dwmax=3)
            ref = count(c -> bf_ndown(c) == n && bf_domain_walls(c, 1, -1) <= 3,
                        bf_all_configs(L))
            @test length(b) == ref
            @test length(b) <= 1 + n * (L - n)
        end
    end

    @testset "Hamiltonian is Hermitian and real" begin
        ch = XXZChain(12; Jperp=1.0, Delta=2.0, boundary=:kink)
        for dwmax in (3, 5, nothing)
            b = sector_basis(ch; ndown=5, dwmax=dwmax)
            H = build_hamiltonian(b)
            @test H isa SparseMatrixCSC{Float64,Int}
            @test size(H) == (length(b), length(b))
            @test norm(H - transpose(H)) < 1e-14
        end
    end

    @testset "sector H equals the projection of the dense H (S^z conservation)" begin
        L = 8
        ch = XXZChain(L + 2; Jperp=1.0, Delta=2.3, boundary=:kink)
        Hd, cfgs, idx = bf_dense_H(L, 1, -1, 1.0, 2.3)
        for n in 0:L
            b = sector_basis(ch; ndown=n)
            rows = [idx[c] for c in b.configs]
            @test Matrix(build_hamiltonian(b)) ≈ Hd[rows, rows]
            # no leakage out of the sector: H maps the sector into itself
            other = setdiff(1:size(Hd, 1), rows)
            @test norm(Hd[other, rows]) < 1e-14
        end
    end

    @testset "spectrum vs dense ED, N <= 12" begin
        for (N, Δ) in ((10, 2.0), (12, 3.0))
            L = N - 2
            ch = XXZChain(N; Jperp=1.0, Delta=Δ, boundary=:kink)
            Hd, _, _ = bf_dense_H(L, 1, -1, 1.0, Δ)
            dense_spec = sort(eigvals(Symmetric(Hd)))
            sector_spec = Float64[]
            for n in 0:L
                b = sector_basis(ch; ndown=n)
                append!(sector_spec, eigvals(Symmetric(Matrix(build_hamiltonian(b)))))
            end
            sort!(sector_spec)
            @test maximum(abs, dense_spec .- sector_spec) < 1e-9
        end
    end

    @testset "ground state at large Delta is the sharp kink" begin
        N = 14
        L = N - 2
        n = 6
        for Δ in (4.0, 8.0, 16.0)
            ch = XXZChain(N; Jperp=1.0, Delta=Δ, boundary=:kink)
            b = sector_basis(ch; ndown=n)
            H = Matrix(build_hamiltonian(b))
            F = eigen(Symmetric(H))
            gs = F.vectors[:, 1]
            ov = abs2(gs[b.index[sharp_kink_config(ch, n)]])
            @test ov > 1 - 3.0 / Δ^2
            # kink energy above the (unbroken) ferromagnetic vacuum -> J_z/2
            e_fm = -TriangleMPS.Jz(ch) * (N - 1) / 4
            @test abs((F.values[1] - e_fm) - TriangleMPS.Jz(ch) / 2) < 3.0 / Δ
            # every S^z sector of the kink chain hosts exactly one kink ground
            # state, degenerate across sectors up to O(J_perp^2/J_z)
            b2 = sector_basis(ch; ndown=n + 2)
            e2 = eigvals(Symmetric(Matrix(build_hamiltonian(b2))))[1]
            @test abs(e2 - F.values[1]) < 3.0 / Δ
        end
    end

    @testset "single magnon on the all-up chain: exact open-chain dispersion" begin
        N = 14
        L = N - 2
        ch = XXZChain(N; Jperp=1.3, Delta=2.0, boundary=:up)
        b = sector_basis(ch; ndown=1, dwmax=2)
        H = Matrix(build_hamiltonian(b))
        bvac = sector_basis(ch; ndown=0)
        e0 = eigvals(Symmetric(Matrix(build_hamiltonian(bvac))))[1]
        ω = sort(eigvals(Symmetric(H)) .- e0)
        Jzz = TriangleMPS.Jz(ch)
        exact = sort([Jzz - 1.3 * cos(π * m / (L + 1)) for m in 1:L])
        @test maximum(abs, ω .- exact) < 1e-10
        # magnon_dispersion / magnon_velocity helpers agree with the same convention
        @test magnon_dispersion(ch, 0.7) ≈ Jzz - 1.3 * cos(0.7)
        @test magnon_velocity(ch, 0.7) ≈ 1.3 * sin(0.7)
    end
end
