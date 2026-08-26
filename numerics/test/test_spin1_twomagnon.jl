# test_spin1_twomagnon.jl -- red/green tests for the spin-1 ferromagnet
# two-magnon soft phase slope (Conjecture Bc falsifier (A), bd tns-8e9).
#
# Standalone: includes ../src/spin1_twomagnon.jl (which itself includes
# ../src/spin1_collision.jl); touches no other module.
#
# PASS CRITERIA ARE FIXED HERE IN ADVANCE OF ANY PRODUCTION RUN.
#   TOL_ALGEBRA   su(2) commutators / Casimir, machine precision
#   TOL_SECTOR    two-magnon sector spectrum vs brute-force (2S+1)^N ED
#   TOL_BETHE     residual ‖H psi - E psi‖ of the coordinate-Bethe candidate
#   TOL_BLOCK     momentum-block spectrum vs full sector spectrum
#   TOL_PHASE     ring Bethe--Yang phase extraction vs the known spin-1/2
#                 analytic phase (validation of the extractor on an exactly
#                 solved case)
#   TOL_DISP      wavepacket displacement vs the packet-averaged prediction
#   TOL_CONSERVE  relative norm / energy drift over the whole evolution
#   BC_BAND       decision band for Conjecture Bc: the measured soft slope
#                 dδ/dk_s|_0 must sit within BC_BAND of 1 (Bc SURVIVES) or of
#                 2 (Bc FALSIFIED).  8%, matching the criterion already used
#                 for the memory-quantum scan.

# Wrapped in `module TestSpin1TwoMagnon` so that numerics/test/runtests.jl can
# include every shard test into one process: the shard modules export
# names that also exist in TriangleMPS / FMTwoMagnon, and `using` them
# all into a shared `Main` makes those names ambiguous.

module TestSpin1TwoMagnon

using Test
using LinearAlgebra
using SparseArrays
using Printf

include(joinpath(@__DIR__, "..", "src", "spin1_twomagnon.jl"))
using .Spin1TwoMagnon

const TOL_ALGEBRA  = 1.0e-12
const TOL_SECTOR   = 1.0e-9
const TOL_BETHE    = 1.0e-9
const TOL_BLOCK    = 1.0e-9
const TOL_PHASE    = 1.0e-7
const TOL_DISP     = 2.0e-2
const TOL_CONSERVE = 1.0e-9
const BC_BAND      = 0.08

# ---------------------------------------------------------------------------
# Brute-force reference: dense (2S+1)^N Hamiltonian built from Kronecker
# products of on-site spin matrices.  Deliberately independent of the sector
# enumeration in src/spin1_twomagnon.jl.
# ---------------------------------------------------------------------------

function bf_spin_ops(S::Real)
    d = Int(round(2S + 1))
    ms = [S - (i - 1) for i in 1:d]            # descending m
    Sz = Diagonal(Float64.(ms))
    Sp = zeros(Float64, d, d)
    for i in 2:d
        m = ms[i]
        Sp[i-1, i] = sqrt(S * (S + 1) - m * (m + 1))
    end
    Sm = Matrix(transpose(Sp))
    Sx = (Sp + Sm) / 2
    Sy = (Sp - Sm) / (2im)
    return (Sx = ComplexF64.(Sx), Sy = ComplexF64.(Sy), Sz = ComplexF64.(Matrix(Sz)),
            Sp = ComplexF64.(Sp), Sm = ComplexF64.(Sm), d = d)
end

"Operator `op` acting on site `j` (1-based) of an `N`-site chain."
function bf_embed(op::AbstractMatrix, j::Int, N::Int, d::Int)
    M = Matrix{ComplexF64}(I, 1, 1)
    for x in 1:N
        M = kron(M, x == j ? ComplexF64.(op) : Matrix{ComplexF64}(I, d, d))
    end
    return M
end

"""
Dense `H = -J Σ_x (S_x·S_{x+1} - S²)` on a periodic ring of `N` sites.
"""
function bf_ring_H(N::Int, S::Real, J::Real)
    o = bf_spin_ops(S)
    d = o.d
    D = d^N
    H = zeros(ComplexF64, D, D)
    for x in 1:N
        y = mod1(x + 1, N)
        Sxx, Sxy = bf_embed(o.Sx, x, N, d), bf_embed(o.Sx, y, N, d)
        Syx, Syy = bf_embed(o.Sy, x, N, d), bf_embed(o.Sy, y, N, d)
        Szx, Szy = bf_embed(o.Sz, x, N, d), bf_embed(o.Sz, y, N, d)
        H .-= J .* (Sxx * Sxy + Syx * Syy + Szx * Szy - S^2 * Matrix{ComplexF64}(I, D, D))
    end
    return H
end

"Diagonal of total S^z on the `d^N` product basis."
function bf_total_sz(N::Int, S::Real)
    o = bf_spin_ops(S)
    d = o.d
    ms = [real(o.Sz[i, i]) for i in 1:d]
    tot = zeros(Float64, d^N)
    for idx in 0:(d^N - 1)
        s = 0.0
        r = idx
        for _ in 1:N
            s += ms[(r % d) + 1]
            r ÷= d
        end
        tot[idx+1] = s
    end
    return tot
end

@testset "spin-1 FM two-magnon soft slope (Bc falsifier A)" begin

    @testset "on-site spin matrices satisfy su(2)" begin
        for S in (0.5, 1.0, 1.5)
            o = bf_spin_ops(S)
            d = o.d
            Id = Matrix{ComplexF64}(I, d, d)
            @test norm(o.Sx * o.Sy - o.Sy * o.Sx - im * o.Sz) < TOL_ALGEBRA
            @test norm(o.Sy * o.Sz - o.Sz * o.Sy - im * o.Sx) < TOL_ALGEBRA
            @test norm(o.Sz * o.Sx - o.Sx * o.Sz - im * o.Sy) < TOL_ALGEBRA
            @test norm(o.Sx^2 + o.Sy^2 + o.Sz^2 - S * (S + 1) * Id) < TOL_ALGEBRA
            # the module must expose exactly the same matrices
            m = spin_ops(S)
            @test norm(m.Sp - o.Sp) < TOL_ALGEBRA
            @test norm(m.Sz - o.Sz) < TOL_ALGEBRA
        end
    end

    @testset "pair basis with double occupancy" begin
        for N in (6, 11, 18)
            b12 = pair_basis(N, 0.5)
            @test b12.dim == N * (N - 1) ÷ 2                # hard core
            b1 = pair_basis(N, 1.0)
            @test b1.dim == N * (N - 1) ÷ 2 + N             # + one diagonal per site
            for (n, (x, y)) in enumerate(b1.pairs)
                @test 0 <= x <= y <= N - 1
                @test pair_index(b1, x, y) == n
                @test pair_index(b1, y, x) == n
            end
        end
    end

    @testset "one-magnon dispersion  ω = 2JS(1-cos k)" begin
        N, J = 24, 1.37
        for S in (0.5, 1.0)
            H1 = one_magnon_hamiltonian(N, J, S)
            @test H1 ≈ transpose(H1)
            for n in 0:N-1
                k = 2π * n / N
                k = k > π ? k - 2π : k
                v = [cis(k * x) for x in 0:N-1] / sqrt(N)
                @test norm(H1 * v - omega(k, J, S) * v) < 1e-12
                @test isapprox(group_velocity(k, J, S), 2J * S * sin(k); atol = 1e-14)
            end
        end
    end

    @testset "two-magnon sector vs brute-force (2S+1)^N ED" begin
        # The sector enumeration must reproduce the S^z = NS-2 block of the
        # full ring Hamiltonian, eigenvalue by eigenvalue.
        for (N, S) in ((8, 0.5), (6, 1.0))
            J = 1.37
            H2 = Matrix(two_magnon_hamiltonian(pair_basis(N, S), J, S))
            @test norm(H2 - transpose(H2)) < TOL_ALGEBRA
            Hf = bf_ring_H(N, S, J)
            tot = bf_total_sz(N, S)
            idx = findall(x -> abs(x - (N * S - 2)) < 1e-9, tot)
            @test length(idx) == size(H2, 1)
            ef = sort(real.(eigvals(Hermitian(Hf[idx, idx]))))
            e2 = sort(eigvals(Symmetric(H2)))
            @test maximum(abs.(ef .- e2)) < TOL_SECTOR
        end
    end

    @testset "spin-S S-matrix: unitarity, swap, s=1/2 reduction" begin
        for (k1, k2) in ((0.30, 1.5), (-0.30, 1.5), (0.15, 0.8), (0.7, 2.4))
            # at S = 1/2 the contact solution must collapse to the FROZEN
            # oracle formula -(z1 z2 - 2 z1 + 1)/(z1 z2 - 2 z2 + 1)
            z1, z2 = cis(k1), cis(k2)
            ref = -(z1 * z2 - 2z1 + 1) / (z1 * z2 - 2z2 + 1)
            @test isapprox(smatrix(k1, k2, 0.5), ref; atol = 1e-12)
            for S in (0.5, 1.0, 1.5, 2.0)
                @test isapprox(abs(smatrix(k1, k2, S)), 1.0; atol = 1e-12)
                @test isapprox(smatrix(k1, k2, S) * smatrix(k2, k1, S), 1.0; atol = 1e-12)
                h = 1e-5
                fd1 = (soft_phase(k1 + h, k2, S) - soft_phase(k1 - h, k2, S)) / (2h)
                fd2 = (soft_phase(k1, k2 + h, S) - soft_phase(k1, k2 - h, S)) / (2h)
                @test isapprox(dphase_dk1(k1, k2, S), fd1; atol = 1e-7)
                @test isapprox(dphase_dk2(k1, k2, S), fd2; atol = 1e-7)
            end
        end
        # the analytic soft slope: dδ/dk_s|_0 = 1/S, hard dependence cancelling
        for S in (0.5, 1.0, 1.5, 2.0), kh in (0.37, 0.8, 1.5, 2.4, 3.0)
            @test isapprox(dphase_dk1(0.0, kh, S), soft_slope_prediction(S); atol = 1e-10)
            @test isapprox(dphase_dk2(0.0, kh, S), 0.0; atol = 1e-10)
        end
    end

    @testset "coordinate-Bethe vector is an exact eigenvector (all S)" begin
        # Machine-precision test of the whole contact derivation: the vector
        # built from `contact_numerator` (plus the doubly-occupied amplitude ρ)
        # must diagonalise the enumerated sector Hamiltonian at Bethe--Yang
        # quantised momenta, with energy ω(k1)+ω(k2).
        # Quantum numbers must be non-degenerate: for n1 = n2 the Bethe-Yang
        # fixed point lands on the singular pair, and the vector is not an
        # eigenvector at ANY S (it fails at s = 1/2 with the frozen oracle
        # S-matrix too).  That is a property of the ansatz, not of the contact
        # derivation, so it is excluded here rather than papered over.
        N, J = 18, 1.37
        for S in (0.5, 1.0, 1.5, 2.0), (n1, n2) in ((1, 4), (2, 7), (1, 8))
            pb = pair_basis(N, S)
            H2 = two_magnon_hamiltonian(pb, J, S)
            k1, k2 = quantized_pair(N, n1, n2, S)
            ψ = bethe_vector(pb, k1, k2, S)
            E = omega(k1, J, S) + omega(k2, J, S)
            @test norm(H2 * ψ - E * ψ) < TOL_BETHE
        end
    end

    @testset "momentum blocks reproduce the full sector spectrum" begin
        for (N, S) in ((10, 0.5), (8, 1.0), (9, 1.0))
            J = 0.83
            full = sort(eigvals(Symmetric(Matrix(two_magnon_hamiltonian(pair_basis(N, S), J, S)))))
            blk = Float64[]
            for m in 0:N-1
                M = momentum_block(N, S, m; J = J)
                @test norm(M - M') < 1e-11
                append!(blk, real.(eigvals(Hermitian(M))))
            end
            sort!(blk)
            @test length(blk) == length(full)
            @test maximum(abs.(blk .- full)) < TOL_BLOCK
        end
    end

    @testset "ring phase extraction on the exactly-solved spin-1/2 case" begin
        # Validation of the ansatz-free extractor against the frozen analytic
        # spin-1/2 phase (oracle O2/O3).  Uses only ED eigenvalues and the
        # one-magnon dispersion, never the S-matrix.
        for N in (60, 120), khtarget in (0.8, 1.5)
            r = ring_phase_shift(N, 0.5, khtarget; J = 1.0)
            @test r.n_soft == 1
            @test isapprox(r.delta, soft_phase(r.ks, r.kh, 0.5); atol = TOL_PHASE)
        end
    end

    @testset "ring phase extraction for spin-1 and spin-3/2" begin
        for S in (1.0, 1.5), N in (60, 120), khtarget in (0.8, 1.5)
            r = ring_phase_shift(N, S, khtarget; J = 1.0)
            @test r.n_soft == 1
            @test r.ks > 0
            @test isapprox(r.delta, soft_phase(r.ks, r.kh, S); atol = TOL_PHASE)
        end
    end

    @testset "norm and energy conservation (spin-1 collision)" begin
        run = collision_run(; S = 1.0, J = 1.0, ks = 0.30, kh = 1.5, sigma_x = 6.0,
                            sep_factor = 8.0, dt = 1.0)
        @test run.krylov_ok
        @test run.norm_drift < TOL_CONSERVE
        @test run.energy_drift < TOL_CONSERVE
    end

    @testset "spin-1 displacement matches the packet-averaged prediction" begin
        for (ks, kh) in ((0.30, 1.5), (-0.30, 1.5))
            run = collision_run(; S = 1.0, J = 1.0, ks = ks, kh = kh, sigma_x = 8.0,
                                sep_factor = 8.0, dt = 1.0)
            @test abs(run.delta_s - run.pred_s_avg) < TOL_DISP
            @test abs(run.delta_s_pre) < TOL_DISP
            @test sign(run.delta_s) == -1
        end
    end

    @testset "DECISION: soft phase slope for spin-1" begin
        # Ansatz-free: exact ring spectra only.  slope := dδ/dk_s|_{k_s→0}.
        # The decision band BC_BAND and the two hypotheses (1 = Bc survives,
        # 2 = Bc falsified) were fixed before any number was produced.
        # Control first: the extractor must return the FROZEN value 2 at s=1/2.
        ctrl = soft_slope_rings(0.5; kh_target = 1.5, Ns = (60, 90, 120, 180, 240),
                                J = 1.0)
        @test abs(ctrl.slope - 2.0) < BC_BAND

        res = soft_slope_rings(1.0; kh_target = 1.5, Ns = (60, 90, 120, 180, 240),
                               J = 1.0)
        @test res.err < BC_BAND / 2
        bc_survives  = abs(res.slope - 1.0) < BC_BAND
        bc_falsified = abs(res.slope - 2.0) < BC_BAND
        @test bc_survives != bc_falsified          # exactly one verdict
        @info "spin-1 soft slope" slope = res.slope err = res.err bc_survives bc_falsified
        @test bc_survives
        # and the general law behind it: dδ/dk_s|_0 = 1/S
        for S in (0.5, 1.0, 1.5)
            r = soft_slope_rings(S; kh_target = 1.5, Ns = (90, 120, 180, 240), J = 1.0)
            @test isapprox(r.slope, 1 / S; atol = BC_BAND)
        end
    end

end

end # module TestSpin1TwoMagnon
