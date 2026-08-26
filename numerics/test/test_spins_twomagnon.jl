# test_spins_twomagnon.jl -- red/green tests for the spin-S two-magnon
# scattering shard (L1).  Falsifier (A) of Conjecture Bc, bd tns-8e9.
#
# Standalone: includes ../src/spins_twomagnon.jl and (for the S = 1/2
# cross-check) ../src/fm_twomagnon.jl.  Touches no other module.
#
# PASS CRITERIA ARE FIXED HERE IN ADVANCE OF ANY PRODUCTION RUN.
#   TOL_ALG       su(2) algebra / operator identities
#   TOL_SPEC      sector-Hamiltonian spectra against a brute-force (2S+1)^N build
#   TOL_BETHE     residual of the coordinate-Bethe ansatz on bulk configurations
#   TOL_DISP      absolute displacement tolerance in lattice sites (same 2e-2 as
#                 the S = 1/2 shard: 1% of the S = 1/2 scattering length 2)
#   TOL_CONSERVE  norm / energy drift over the whole evolution
#   VERDICT_TOL   the Bc decision window, see below
#
# THE DECISION (fixed before any spin-1 number was computed).  Theorem S2-2body
# gives, at S = 1/2, a soft Wigner phase slope  d(delta)/d k_s|_0 = 2.
# Conjecture Bc (theory/TRIANGLE.md 4) says this coefficient is |q_hard|/s,
# hence 1 for the spin-1 ferromagnet.  The competing hypothesis is that the
# two-magnon S-matrix is spin-INDEPENDENT, hence a slope of 2 at every S.
# The measured slope must land within VERDICT_TOL = 0.05 of one of {1, 2};
# anything else is INCONCLUSIVE and this test goes red.
#
# Verdict recorded when this shard landed: the exact spin-S contact algebra
# gives d(delta)/d k_s|_0 = 1/S at every hard momentum, and the spin-1 dynamics
# reproduces it.  Conjecture Bc SURVIVES.

module TestSpinSTwoMagnon

using Test
using LinearAlgebra
using SparseArrays
using Printf

include(joinpath(@__DIR__, "..", "src", "spins_twomagnon.jl"))
using .SpinSTwoMagnon

include(joinpath(@__DIR__, "..", "src", "fm_twomagnon.jl"))
const FM = FMTwoMagnon

const TOL_ALG      = 1.0e-12
const TOL_SPEC     = 1.0e-9
const TOL_BETHE    = 1.0e-10
const TOL_DISP     = 2.0e-2
const TOL_CONSERVE = 1.0e-9
const VERDICT_TOL  = 5.0e-2
const BC_SLOPE     = 1.0     # Conjecture Bc prediction for s = 1
const ALT_SLOPE    = 2.0     # spin-independent-S-matrix prediction

# --------------------------------------------------------------------------
# Brute-force reference: the FULL (2S+1)^N Hamiltonian of the spin-S isotropic
# Heisenberg ferromagnet on a ring, built from dense Kronecker products.  This
# is written independently of src/spins_twomagnon.jl so that agreement is a
# real check and not a restatement of the production code.
# --------------------------------------------------------------------------

function bf_spin_ops(twoS::Int)
    d = twoS + 1
    Sspin = twoS / 2
    Sz = zeros(Float64, d, d)
    Sp = zeros(Float64, d, d)
    for n in 0:twoS                              # n = S - m, magnon number
        Sz[n+1, n+1] = Sspin - n
        n >= 1 && (Sp[n, n+1] = sqrt(n * (twoS - n + 1)))
    end
    return Sz, Sp, Matrix(transpose(Sp))
end

function bf_kron_site(op::Matrix{Float64}, x::Int, N::Int, d::Int)
    M = Matrix{Float64}(I, 1, 1)
    for y in 1:N
        M = kron(M, y == x ? op : Matrix{Float64}(I, d, d))
    end
    return M
end

"H = -J sum_x (S_x . S_{x+1} - S^2) on a ring of N spin-S sites, dense."
function bf_ring_H(N::Int, twoS::Int, J::Float64)
    d = twoS + 1
    Sspin = twoS / 2
    Sz, Sp, Sm = bf_spin_ops(twoS)
    zs = [bf_kron_site(Sz, x, N, d) for x in 1:N]
    ps = [bf_kron_site(Sp, x, N, d) for x in 1:N]
    ms = [bf_kron_site(Sm, x, N, d) for x in 1:N]
    H = zeros(Float64, d^N, d^N)
    for x in 1:N
        y = mod1(x + 1, N)
        H .-= J .* (0.5 .* (ps[x] * ms[y] .+ ms[x] * ps[y]) .+ zs[x] * zs[y]
                    .- Sspin^2 .* Matrix{Float64}(I, d^N, d^N))
    end
    return H, zs
end

"Indices of the total-S^z = N*S - nmag eigenspace of the dense ring."
function bf_sector_indices(N::Int, twoS::Int, nmag::Int)
    d = twoS + 1
    idx = Int[]
    for m in 0:(d^N - 1)
        tot = 0
        r = m
        for _ in 1:N
            tot += r % d
            r ÷= d
        end
        tot == nmag && push!(idx, m + 1)
    end
    return idx
end

@testset "spin-S two-magnon scattering (Bc falsifier A)" begin

    @testset "su(2) algebra of the on-site operators" begin
        for twoS in (1, 2, 3, 4)
            Sx, Sy, Sz, Sp, Sm = spin_matrices(twoS)
            Sspin = twoS / 2
            d = twoS + 1
            @test opnorm(Sx * Sy - Sy * Sx - im * Sz) < TOL_ALG
            @test opnorm(Sy * Sz - Sz * Sy - im * Sx) < TOL_ALG
            @test opnorm(Sz * Sx - Sx * Sz - im * Sy) < TOL_ALG
            @test opnorm(Sx^2 + Sy^2 + Sz^2 - Sspin * (Sspin + 1) * I(d)) < TOL_ALG
            @test opnorm(Sp - (Sx + im * Sy)) < TOL_ALG
            @test opnorm(Sm - (Sx - im * Sy)) < TOL_ALG
            @test opnorm(Sp - Matrix(Sm')) < TOL_ALG
        end
    end

    @testset "two-magnon basis" begin
        for N in (6, 11)
            @test pair_basis_s(N, 1).dim == N * (N - 1) ÷ 2       # no double occupancy
            @test pair_basis_s(N, 2).dim == N * (N + 1) ÷ 2       # doubles allowed
            @test pair_basis_s(N, 3).dim == N * (N + 1) ÷ 2
            pb = pair_basis_s(N, 2)
            for (n, (x, y)) in enumerate(pb.pairs)
                @test 0 <= x <= y <= N - 1
                @test pb.index[x+1, y+1] == n
                @test pb.index[y+1, x+1] == n
            end
        end
    end

    @testset "one-magnon dispersion omega = 2SJ(1-cos k)" begin
        N, J = 20, 1.37
        for twoS in (1, 2, 3)
            H1 = one_magnon_hamiltonian_s(N, J, twoS)
            @test H1 ≈ transpose(H1)
            for n in 0:N-1
                k = 2π * n / N
                k = k > π ? k - 2π : k
                v = [cis(k * x) for x in 0:N-1] / sqrt(N)
                @test norm(H1 * v - omega_s(k, J, twoS) * v) < 1e-12
                @test isapprox(omega_s(k, J, twoS), twoS * J * (1 - cos(k)); atol = 1e-14)
                @test isapprox(group_velocity_s(k, J, twoS), twoS * J * sin(k); atol = 1e-14)
            end
        end
    end

    @testset "sector Hamiltonian vs brute-force (2S+1)^N build" begin
        J = 0.83
        for (N, twoS) in ((5, 1), (6, 2), (5, 3))
            Hfull, _ = bf_ring_H(N, twoS, J)
            idx = bf_sector_indices(N, twoS, 2)
            Hsec = Hfull[idx, idx]
            pb = pair_basis_s(N, twoS)
            @test pb.dim == length(idx)
            H2 = Matrix(two_magnon_hamiltonian_s(pb, J, twoS))
            @test norm(H2 - transpose(H2)) < TOL_ALG
            a = sort(eigvals(Symmetric(Hsec)))
            b = sort(eigvals(Symmetric(H2)))
            @test maximum(abs.(a .- b)) < TOL_SPEC
            # single-magnon block too
            idx1 = bf_sector_indices(N, twoS, 1)
            a1 = sort(eigvals(Symmetric(Hfull[idx1, idx1])))
            b1 = sort(eigvals(Symmetric(Matrix(one_magnon_hamiltonian_s(N, J, twoS)))))
            @test maximum(abs.(a1 .- b1)) < TOL_SPEC
        end
    end

    @testset "S = 1/2 reduces to the frozen fm_twomagnon shard" begin
        N, J = 10, 1.11
        pb = pair_basis_s(N, 1)
        pbf = FM.pair_basis(N)
        A = sort(eigvals(Symmetric(Matrix(two_magnon_hamiltonian_s(pb, J, 1)))))
        B = sort(eigvals(Symmetric(Matrix(FM.two_magnon_hamiltonian(pbf, J)))))
        @test maximum(abs.(A .- B)) < TOL_SPEC
        for (k1, k2) in ((0.3, 1.5), (-0.4, 2.2), (0.9, 1.1))
            @test smatrix_s(k1, k2, 1) ≈ FM.smatrix(k1, k2)
            @test isapprox(dphase_dk1_s(k1, k2, 1), FM.dphase_dk1(k1, k2); atol = 1e-12)
            @test isapprox(dphase_dk2_s(k1, k2, 1), FM.dphase_dk2(k1, k2); atol = 1e-12)
        end
    end

    @testset "S-matrix is unimodular and its derivatives are correct" begin
        for twoS in (1, 2, 3, 4)
            h = 1e-5
            for (k1, k2) in ((0.3, 1.5), (-0.4, 2.2), (0.9, 1.1), (0.15, 0.8))
                @test isapprox(abs(smatrix_s(k1, k2, twoS)), 1.0; atol = TOL_ALG)
                fd1 = (soft_phase_s(k1 + h, k2, twoS) - soft_phase_s(k1 - h, k2, twoS)) / 2h
                fd2 = (soft_phase_s(k1, k2 + h, twoS) - soft_phase_s(k1, k2 - h, twoS)) / 2h
                @test isapprox(dphase_dk1_s(k1, k2, twoS), fd1; atol = 1e-7)
                @test isapprox(dphase_dk2_s(k1, k2, twoS), fd2; atol = 1e-7)
            end
        end
    end

    @testset "coordinate-Bethe ansatz solves the bulk equations at every S" begin
        # The analytic core of falsifier (A).  The two CONTACT conditions
        #   gamma = (g/t) W / b            [double occupancy]
        #   g gamma (1+P) = t Sigma (1+P) - J W   [adjacent pair]
        # must reproduce H2 psi = (omega1 + omega2) psi on every configuration
        # away from the ring seam -- for ARBITRARY (k1,k2), so no quantisation
        # is involved and the test is a pure statement about the S-matrix.
        N, J = 24, 1.0
        for twoS in (1, 2, 3, 4)
            for (k1, k2) in ((0.4, 1.7), (-0.3, 2.1), (0.9, 1.2), (0.15, 0.8))
                r = bethe_residual_bulk(N, J, twoS, k1, k2; margin = 3)
                @test r < TOL_BETHE
            end
        end
    end

    @testset "Bethe-Yang quantised ring eigenvector" begin
        for twoS in (1, 2, 3)
            N, J = 18, 1.37
            pb = pair_basis_s(N, twoS)
            H2 = two_magnon_hamiltonian_s(pb, J, twoS)
            k1, k2 = quantized_pair(N, 1, 4, twoS)
            ψ = bethe_vector_s(pb, k1, k2, twoS)
            E = omega_s(k1, J, twoS) + omega_s(k2, J, twoS)
            @test norm(H2 * ψ - E * ψ) < 1e-9
        end
    end

    @testset "exact soft slope is 1/S at every hard momentum" begin
        for twoS in (1, 2, 3, 4)
            for kh in (0.37, 0.8, 1.1, 1.5, 2.4, 3.0)
                @test isapprox(soft_slope_exact(kh, twoS), 2 / twoS; atol = 1e-10)
                @test isapprox(dphase_dk2_s(0.0, kh, twoS), 0.0; atol = 1e-10)
            end
        end
    end

    @testset "free propagation velocity (S = 1)" begin
        N, J, twoS = 200, 1.0, 2
        H1 = one_magnon_hamiltonian_s(N, J, twoS)
        for k in (0.3, 1.5)
            φ = gaussian_packet(N, k, 100.0, 8.0)
            @test isapprox(norm(φ), 1.0; atol = 1e-12)
            x0 = centroid(abs2.(φ))
            T = 20.0
            ψ = evolve(H1, ComplexF64.(φ), T; dt = 1.0)
            @test isapprox((centroid(abs2.(ψ)) - x0) / T, packet_velocity(φ, J, twoS);
                           atol = 5.0e-3)
        end
    end

    @testset "norm and energy conservation (S = 1 collision)" begin
        run = collision_run(; J = 1.0, twoS = 2, ks = 0.30, kh = 1.5,
                            sigma_x = 6.0, sep_factor = 8.0, dt = 1.0)
        @test run.norm_drift < TOL_CONSERVE
        @test run.energy_drift < TOL_CONSERVE
        @test run.krylov_ok
    end

    @testset "displacement extraction reproduces the exact S-matrix (S = 1)" begin
        for (ks, kh) in ((0.30, 1.5), (-0.30, 1.5))
            run = collision_run(; J = 1.0, twoS = 2, ks = ks, kh = kh,
                                sigma_x = 10.0, sep_factor = 10.0, dt = 1.0)
            @test abs(run.delta_s - run.pred_s_avg) < TOL_DISP
            @test abs(run.delta_h - run.pred_h_avg) < TOL_DISP
            @test abs(run.delta_s_pre) < TOL_DISP     # pre-collision control
            @test abs(run.delta_h_pre) < TOL_DISP
        end
    end

    @testset "THE DECISION: spin-1 soft phase slope is 1 (Bc) or 2 (alt)" begin
        # Slope from PURE DYNAMICS: at each k_s average the +k_s and -k_s runs
        # (which kills the O(k_s) term exactly) and Richardson-extrapolate in
        # packet width; then extrapolate the two k_s values to k_s = 0 in k_s^2.
        r = soft_slope(; J = 1.0, twoS = 2, kss = (0.30, 0.20), kh = 1.5,
                       sigmas = (6.0, 8.0), sep_factor = 9.0, dt = 1.0)
        @test r.krylov_ok
        @test min(abs(r.slope - BC_SLOPE), abs(r.slope - ALT_SLOPE)) < VERDICT_TOL
        @printf("\n[Bc falsifier A] spin-1 soft phase slope = %.5f +- %.5f (Bc predicts %.1f, spin-independent predicts %.1f)\n",
                r.slope, r.err, BC_SLOPE, ALT_SLOPE)
    end

end

end # module TestSpinSTwoMagnon
