# test_spins_memory.jl -- red/green tests for the spin-S kink/magnon memory
# shard (L1).  Falsifier (B) of Conjecture Bc, bd tns-8e9.
#
# Standalone except for the S = 1/2 cross-check, which confronts the new shard
# with the frozen TriangleMPS spin-1/2 sector code.
#
# PASS CRITERIA ARE FIXED HERE IN ADVANCE OF ANY PRODUCTION RUN.
#   TOL_SPEC      sector-Hamiltonian spectra vs a brute-force (2S+1)^L build
#   TOL_EXACT     estimators / conserved quantities that must be exact
#   TOL_VELOCITY  free-magnon group-velocity tolerance
#   TOL_CONSERVE  norm / energy drift over the whole evolution
#   RATIO_TOL     the memory-quantum decision window: 8%, the same criterion
#                 already fixed for the spin-1/2 scan (corner-b-draft 3.3)
#
# THE DECISION (fixed before any spin-1 number was computed).  Theorem M-quant
# gives dx = -N_T/s, i.e. -2 sites per transmitted magnon at s = 1/2.  The
# spin-1 easy-axis chain must therefore give dx/N_T = -1/s = -1.  If it returns
# -2 (or anything outside the 8% window around -1), the second leg of
# Conjecture Bc is falsified.

module TestSpinSMemory

using Test
using LinearAlgebra
using SparseArrays
using Printf

include(joinpath(@__DIR__, "..", "src", "spins_memory.jl"))
using .SpinSMemory

import TriangleMPS

const TOL_SPEC     = 1.0e-9
const TOL_EXACT    = 1.0e-10
const TOL_VELOCITY = 2.0e-2
const TOL_CONSERVE = 1.0e-9
const RATIO_TOL    = 8.0e-2
const BC_RATIO_S1  = -1.0     # -1/s at s = 1  (Conjecture Bc / Theorem M-quant)
const ALT_RATIO    = -2.0     # the s = 1/2 value, i.e. a spin-independent quantum

# --------------------------------------------------------------------------
# Brute-force reference: the FULL (2S+1)^L Hamiltonian of the easy-axis spin-S
# XXZ chain with frozen boundary spins, from dense Kronecker products.
# Written independently of src/spins_memory.jl.
# --------------------------------------------------------------------------

function bf_ops(twoS::Int)
    d = twoS + 1
    S = twoS / 2
    Sz = zeros(Float64, d, d)
    Sp = zeros(Float64, d, d)
    for n in 0:twoS
        Sz[n+1, n+1] = S - n
        n >= 1 && (Sp[n, n+1] = sqrt(n * (twoS - n + 1)))
    end
    return Sz, Sp, Matrix(transpose(Sp))
end

function bf_site(op::Matrix{Float64}, x::Int, L::Int, d::Int)
    M = Matrix{Float64}(I, 1, 1)
    for y in 1:L
        M = kron(M, y == x ? op : Matrix{Float64}(I, d, d))
    end
    return M
end

"""
H = -sum_{x=1}^{N-1} [ (Jperp/2)(S+S- + h.c.) + Jz Sz Sz ] on N = L+2 sites,
with sites 1 and N frozen at S^z = +S and (kink) -S.  Dense on the (2S+1)^L
dynamical space.
"""
function bf_chain_H(L::Int, twoS::Int, Jperp::Float64, Delta::Float64; kink::Bool=true)
    d = twoS + 1
    S = twoS / 2
    Jz = Delta * Jperp
    Sz, Sp, Sm = bf_ops(twoS)
    D = d^L
    zs = [bf_site(Sz, x, L, d) for x in 1:L]
    ps = [bf_site(Sp, x, L, d) for x in 1:L]
    ms = [bf_site(Sm, x, L, d) for x in 1:L]
    H = zeros(Float64, D, D)
    for x in 1:(L-1)                       # dynamical-dynamical bonds
        H .-= Jperp / 2 .* (ps[x] * ms[x+1] .+ ms[x] * ps[x+1])
        H .-= Jz .* (zs[x] * zs[x+1])
    end
    H .-= Jz * S .* zs[1]                                  # frozen left, S^z = +S
    H .-= Jz * (kink ? -S : S) .* zs[L]                    # frozen right
    return H
end

"Indices of the total-magnon-number = ntot eigenspace (n = S - S^z per site)."
function bf_sector(L::Int, twoS::Int, ntot::Int)
    d = twoS + 1
    idx = Int[]
    for m in 0:(d^L - 1)
        tot = 0; r = m
        for _ in 1:L
            tot += r % d; r ÷= d
        end
        tot == ntot && push!(idx, m + 1)
    end
    return idx
end

@testset "spin-S kink/magnon memory (Bc falsifier B)" begin

    @testset "chain conventions and dispersion" begin
        for twoS in (1, 2, 3)
            ch = SpinChain(20; twoS=twoS, Jperp=1.3, Delta=2.5)
            @test nsites_dynamical(ch) == 18
            @test Jz_of(ch) ≈ 2.5 * 1.3
            for k in (0.0, 0.4, 1.2, 2.0)
                @test isapprox(magnon_dispersion_s(ch, k), twoS * 1.3 * (2.5 - cos(k));
                               atol=1e-13)
                @test isapprox(magnon_velocity_s(ch, k), twoS * 1.3 * sin(k); atol=1e-13)
            end
            @test magnon_dispersion_s(ch, 0.0) > 0          # gapped for Delta > 1
        end
    end

    @testset "up-variation D and the kink manifold" begin
        ch = SpinChain(9; twoS=2)          # L = 7
        @test updown_variation(ch, Int8[0,0,0,1,2,2,2]) == 0     # monotone wall
        @test updown_variation(ch, Int8[0,0,2,2,2,2,2]) == 0     # sharp wall
        @test updown_variation(ch, Int8[0,1,0,2,2,2,2]) == 1     # wall + one magnon
        @test updown_variation(ch, Int8[0,0,2,1,2,2,2]) == 1     # magnon on the down side
        @test updown_variation(ch, Int8[2,0,0,0,2,2,2]) == 2     # two magnons (bound)
        # every D = 0 configuration is non-decreasing
        b = sector_basis_s(ch; ntot=7, dmax=0)
        for j in 1:length(b)
            c = config(b, j)
            @test issorted(c)
        end
    end

    @testset "sector Hamiltonian vs brute-force (2S+1)^L build" begin
        for (N, twoS, ntot) in ((7, 2, 5), (7, 1, 3), (6, 3, 6))
            L = N - 2
            ch = SpinChain(N; twoS=twoS, Jperp=1.0, Delta=2.0)
            b = sector_basis_s(ch; ntot=ntot, dmax=nothing)
            Hd = bf_chain_H(L, twoS, 1.0, 2.0)
            idx = bf_sector(L, twoS, ntot)
            @test length(b) == length(idx)
            H = Matrix(build_hamiltonian_s(b))
            @test norm(H - transpose(H)) < TOL_EXACT
            a = sort(eigvals(Symmetric(Hd[idx, idx])))
            c = sort(eigvals(Symmetric(H)))
            @test maximum(abs.(a .- c)) < TOL_SPEC
            @test truncation_leakage_s(b) == 0.0
        end
    end

    @testset "S = 1/2 reduces to the frozen TriangleMPS sector shard" begin
        N, Δ = 12, 2.0
        chn = SpinChain(N; twoS=1, Jperp=1.0, Delta=Δ)
        old = TriangleMPS.XXZChain(N; Jperp=1.0, Delta=Δ, boundary=:kink)
        for (ndown, dmax) in ((5, nothing), (5, 1), (6, 1), (6, 0))
            b = sector_basis_s(chn; ntot=ndown, dmax=dmax)
            dw = dmax === nothing ? nothing : 2 * dmax + 1
            ob = TriangleMPS.sector_basis(old; ndown=ndown, dwmax=dw)
            @test length(b) == length(ob)
            A = sort(eigvals(Symmetric(Matrix(build_hamiltonian_s(b)))))
            B = sort(eigvals(Symmetric(Matrix(TriangleMPS.build_hamiltonian(ob)))))
            @test maximum(abs.(A .- B)) < TOL_SPEC
        end
    end

    @testset "kink position estimators are exact on sharp walls" begin
        for twoS in (1, 2)
            N = 16
            ch = SpinChain(N; twoS=twoS)
            S = twoS / 2
            for w in 5:10                      # wall bond between sites w and w+1
                m = [x <= w ? S : -S for x in 1:N]
                @test isapprox(kink_position_centroid(m; window=(3, N-2)), w + 0.5;
                               atol=TOL_EXACT)
                @test isapprox(kink_position_integrated(m, twoS; window=(3, N-2)),
                               w + 0.5; atol=TOL_EXACT)
                wt = magnon_weights_s(m, twoS; kink_ref=w + 0.5, buffer=2)
                @test isapprox(wt.T, 0.0; atol=TOL_EXACT)
                @test isapprox(wt.R, 0.0; atol=TOL_EXACT)
            end
        end
    end

    @testset "the memory law is charge conservation on sharp states" begin
        # A magnon moved from the up side to the down side must shift the
        # windowed wall estimator by exactly -1/s.  This is the statement the
        # dynamics has to reproduce; here it is checked on bare configurations.
        for twoS in (1, 2)          # 1/s must be an integer number of sites
            N = 24
            S = twoS / 2
            w = 12
            before = [x <= w ? S : -S for x in 1:N]
            before[4] -= 1                                   # magnon on the up side
            after = [x <= w - 1 / S ? S : -S for x in 1:N]    # wall moved left by 1/s
            after[20] += 1                                   # magnon on the down side
            @test isapprox(sum(before), sum(after); atol=TOL_EXACT)   # S^z conserved
            X0 = kink_position_integrated(before, twoS; window=(8, 17))
            X1 = kink_position_integrated(after, twoS; window=(8, 17))
            @test isapprox(X1 - X0, -1 / S; atol=TOL_EXACT)
        end
    end

    @testset "free magnon propagates at 2S J sin k (S = 1)" begin
        N, twoS, k0 = 60, 2, 1.2
        ch = SpinChain(N; twoS=twoS, Jperp=1.0, Delta=2.0, boundary=:up)
        b = sector_basis_s(ch; ntot=1, dmax=nothing)
        ψ = free_magnon_state_s(b; k0=k0, x0=20.0, sigma=4.0)
        H = build_hamiltonian_s(b)
        @test isapprox(norm(ψ), 1.0; atol=TOL_EXACT)
        x0 = magnon_centroid(b, ψ)
        T, dt = 10.0, 0.1
        for _ in 1:round(Int, T / dt)
            ψ = krylov_evolve(H, ψ, dt)
        end
        @test isapprox((magnon_centroid(b, ψ) - x0) / T, magnon_velocity_s(ch, k0);
                       atol=TOL_VELOCITY)
    end

    @testset "conservation during a spin-1 memory run" begin
        r = memory_experiment_s(N=64, twoS=2, Delta=3.0, k0=1.5, sigma=2.0,
                                standoff=12.0, dt=0.2, halfwidth=4, buffer=4,
                                obs_every=2)
        @test maximum(abs.(r.norms .- 1)) < TOL_CONSERVE
        @test maximum(abs.(r.energies .- r.energies[1])) < 1e-8
        @test isapprox(r.T_final + r.R_final + r.trapped_final, 1.0; atol=1e-8)
    end

    @testset "the protocol refuses a non-asymptotic geometry" begin
        @test_throws ArgumentError memory_experiment_s(N=64, twoS=2, Delta=3.0, k0=1.5,
                                                       sigma=2.5, standoff=8.0, dt=0.2,
                                                       halfwidth=5, buffer=5)
    end

    @testset "THE DECISION: spin-1 memory quantum is -1 (Bc) or -2 (alt)" begin
        # Geometry note (2026-08-26).  An earlier N=72/sigma=3/standoff=14 run
        # returned -1.104.  Root cause, found by dumping the trajectory: with
        # standoff - buffer < 4 sigma the packet already overlaps the
        # reflected-weight region at t = 0, so `trapped` never starts below
        # trapped_tol, the data-driven pre-window collapses to its 3-point
        # geometric fallback, and trajectory_offset extrapolates that window's
        # spurious slope over the whole interval to t_c.  The raw
        # before/after difference was -1.02 all along.  memory_experiment_s now
        # REFUSES standoff < buffer + 4 sigma (tested just above), and the run
        # below satisfies it.  The 8% criterion and the -1 vs -2 decision are
        # UNCHANGED.
        r = memory_experiment_s(N=80, twoS=2, Delta=6.0, k0=1.5, sigma=2.5,
                                standoff=18.0, dt=0.2, halfwidth=6, buffer=6,
                                obs_every=2)
        ratio = r.dx1 / r.T_final
        @test r.T_final > 0.05                       # something must transmit
        @test min(abs(ratio - BC_RATIO_S1), abs(ratio - ALT_RATIO)) <
              RATIO_TOL * abs(BC_RATIO_S1)
        @printf("\n[Bc falsifier B] spin-1 dx/N_T = %.5f (dx2 est %.5f, T = %.5f); Bc predicts %.1f, spin-independent predicts %.1f\n",
                ratio, r.dx2 / r.T_final, r.T_final, BC_RATIO_S1, ALT_RATIO)
    end

end

end # module TestSpinSMemory
