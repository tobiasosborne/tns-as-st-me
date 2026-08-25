# test_fm_twomagnon.jl -- red/green tests for the FM two-magnon wavepacket
# scattering-displacement extraction (L1).
#
# Standalone: includes ../src/fm_twomagnon.jl directly; touches no other module.
#
# PASS CRITERIA ARE FIXED HERE IN ADVANCE OF ANY PRODUCTION RUN.
#   TOL_DISP      absolute displacement tolerance in lattice sites, both packets
#   TOL_VELOCITY  free-propagation group-velocity tolerance
#   TOL_CONSERVE  relative norm / energy drift over the whole evolution
# Rationale for TOL_DISP = 2e-2: 1% of the leading FM scattering length 2
# (oracle O7/O9).  The realised error bar is estimated a posteriori from
# packet-scale (and hence N-) convergence and reported in the notes; the test
# threshold does not move.

using Test
using LinearAlgebra
using Printf

include(joinpath(@__DIR__, "..", "src", "fm_twomagnon.jl"))
using .FMTwoMagnon

const TOL_DISP     = 2.0e-2
const TOL_VELOCITY = 5.0e-3
const TOL_CONSERVE = 1.0e-9
# Truncation gap allowed between the exact lattice S-matrix derivative and the
# O(k_s^2) oracle expansion at the finite |k_s| ≤ 0.3 used here.  Fixed a priori
# from the size of the first neglected term, ~|k_s|^2 · |∂_k^3 δ| ≲ 0.2.
const TOL_ORACLE_TRUNC = 2.0e-1

@testset "FM two-magnon wavepacket scattering" begin

    @testset "pair basis" begin
        for N in (6, 11, 18)
            pb = pair_basis(N)
            @test length(pb.pairs) == N * (N - 1) ÷ 2
            @test pb.dim == N * (N - 1) ÷ 2
            for (n, (x, y)) in enumerate(pb.pairs)
                @test 0 <= x < y <= N - 1
                @test pb.index[x+1, y+1] == n
                @test pb.index[y+1, x+1] == n
            end
        end
    end

    @testset "one-magnon dispersion (O1)" begin
        N, J = 24, 1.37
        H1 = one_magnon_hamiltonian(N, J)
        @test H1 ≈ transpose(H1)
        for n in 0:N-1
            k = 2π * n / N
            k = k > π ? k - 2π : k
            v = [cis(k * x) for x in 0:N-1] / sqrt(N)
            @test norm(H1 * v - omega(k, J) * v) < 1e-12
            @test isapprox(group_velocity(k, J), J * sin(k); atol = 1e-14)
        end
    end

    @testset "two-magnon Hamiltonian vs coordinate Bethe (O2/O3)" begin
        # Independent enumeration must reproduce the Bethe scattering
        # eigenvector for a periodicity-quantised momentum pair.
        N, J = 18, 1.37
        pb = pair_basis(N)
        H2 = two_magnon_hamiltonian(pb, J)
        @test H2 ≈ transpose(H2)
        k1, k2 = quantized_pair(N, 1, 4)
        S = smatrix(k1, k2)
        @test isapprox(abs(S), 1.0; atol = 1e-12)
        psi = bethe_vector(pb, k1, k2)
        E = omega(k1, J) + omega(k2, J)
        @test norm(H2 * psi - E * psi) < 1e-10
    end

    @testset "analytic phase derivatives vs finite differences" begin
        h = 1e-5
        for (ks, kh) in ((0.30, 1.5), (-0.30, 1.5), (0.15, 0.8), (0.30, 2.4), (-0.20, 3.0))
            fd1 = (soft_phase(ks + h, kh) - soft_phase(ks - h, kh)) / (2h)
            fd2 = (soft_phase(ks, kh + h) - soft_phase(ks, kh - h)) / (2h)
            @test isapprox(dphase_dk1(ks, kh), fd1; atol = 1e-7)
            @test isapprox(dphase_dk2(ks, kh), fd2; atol = 1e-7)
        end
    end

    @testset "exact S-matrix reproduces the oracle soft expansion (O7/O9)" begin
        for kh in (0.37, 0.8, 1.10, 1.5, 2.40, 3.00)
            @test isapprox(dphase_dk1(0.0, kh), 2.0; atol = 1e-12)
            @test isapprox(dphase_dk2(0.0, kh), 0.0; atol = 1e-12)
            for ks in (1e-4, -1e-4)
                @test isapprox(dphase_dk1(ks, kh), oracle_dphase_dks(ks, kh); atol = 1e-6)
                @test isapprox(dphase_dk2(ks, kh), oracle_dphase_dkh(ks, kh); atol = 1e-8)
                @test isapprox(soft_phase(ks, kh), oracle_phase(ks, kh); atol = 1e-9)
            end
        end
    end

    @testset "free propagation velocity" begin
        N, J = 200, 1.0
        for k in (0.3, -0.3, 1.5)
            phi = gaussian_packet(N, k, 100.0, 8.0)
            @test isapprox(norm(phi), 1.0; atol = 1e-12)
            vbar = packet_velocity(phi, J)
            H1 = one_magnon_hamiltonian(N, J)
            x0 = centroid(abs2.(phi))
            psi = ComplexF64.(phi)
            T = 40.0
            psi = evolve(H1, psi, T; dt = 2.0)
            x1 = centroid(abs2.(psi))
            @test isapprox((x1 - x0) / T, vbar; atol = TOL_VELOCITY)
            @test isapprox(vbar, J * sin(k); atol = 2e-2)
        end
    end

    @testset "norm and energy conservation (two-magnon)" begin
        run = collision_run(; J = 1.0, ks = 0.30, kh = 1.5, sigma_x = 6.0,
                            sep_factor = 8.0, dt = 2.0)
        @test run.norm_drift < TOL_CONSERVE
        @test run.energy_drift < TOL_CONSERVE
    end

    @testset "displacement extraction vs Bethe oracle" begin
        # Soft packet: Delta_s = -d(delta)/d k_s  ~ -2 at leading order.
        # Hard packet: Delta_h = -d(delta)/d k_h  = +k_s^2/(2 sin^2(k_h/2)).
        for (ks, kh) in ((0.30, 1.5), (-0.30, 1.5), (0.15, 0.8))
            run = collision_run(; J = 1.0, ks = ks, kh = kh, sigma_x = 10.0,
                                sep_factor = 10.0, dt = 2.0)
            @test run.krylov_ok
            # sharp test: the dynamics must reproduce the packet-averaged
            # exact-S prediction, which is what the centroid shift equals.
            @test abs(run.delta_s - run.pred_s_avg) < TOL_DISP
            @test abs(run.delta_h - run.pred_h_avg) < TOL_DISP
            # pre-collision control: no displacement before the packets meet
            @test abs(run.delta_s_pre) < TOL_DISP
            @test abs(run.delta_h_pre) < TOL_DISP
            # signs: soft pushed backwards, hard pushed forwards (hard-sphere)
            @test sign(run.delta_s) == -1
            @test sign(run.delta_h) == +1
            # the oracle soft expansion, up to its own O(k_s^2) truncation
            @test abs(run.delta_s - run.oracle_s) < TOL_ORACLE_TRUNC
            @test abs(run.delta_h - run.oracle_h) < TOL_ORACLE_TRUNC
        end
    end

    @testset "zero-width extrapolation reproduces d(delta)/dk exactly" begin
        # Pure dynamics -> point-value scattering derivative, with no S-matrix
        # input: the finite-packet bias is linear in 1/sigma_x^2.
        ks, kh = 0.30, 1.5
        a = collision_run(; J = 1.0, ks = ks, kh = kh, sigma_x = 8.0,
                          sep_factor = 10.0, dt = 2.0)
        b = collision_run(; J = 1.0, ks = ks, kh = kh, sigma_x = 12.0,
                          sep_factor = 10.0, dt = 2.0)
        Δs = richardson(8.0, a.delta_s, 12.0, b.delta_s)
        Δh = richardson(8.0, a.delta_h, 12.0, b.delta_h)
        @test abs(Δs - a.pred_s_exact) < TOL_DISP
        @test abs(Δh - a.pred_h_exact) < TOL_DISP
        @test abs(Δs + 2.0) < 1.0            # leading scattering length is 2
    end

    @testset "displacement is independent of J" begin
        a = collision_run(; J = 1.0, ks = 0.30, kh = 1.5, sigma_x = 6.0,
                          sep_factor = 8.0, dt = 2.0)
        b = collision_run(; J = 0.7, ks = 0.30, kh = 1.5, sigma_x = 6.0,
                          sep_factor = 8.0, dt = 2.0 / 0.7)
        @test isapprox(a.delta_s, b.delta_s; atol = 1e-6)
        @test isapprox(a.delta_h, b.delta_h; atol = 1e-6)
    end

end
