using Test
using LinearAlgebra
using TriangleMPS

# Pass/fail criteria are fixed before each run and documented inline.  Where a
# criterion was REVISED after a first run refuted the physical expectation
# behind it, that is said explicitly and recorded in
# numerics/docs/kink-sector-notes.md §4 (per L10, honest verdicts).

@testset "memory_experiment" begin

    @testset "trajectory_offset on synthetic ballistic trajectories" begin
        t = collect(0.0:0.5:40.0)
        tc = 20.0
        # before: X = 10 + 0.1 t ; after: X = 10 + 0.1 t - 1.7  (offset -1.7 at tc)
        X = [tt < tc ? 10 + 0.1tt : 10 + 0.1tt - 1.7 for tt in t]
        r = trajectory_offset(t, X, tc, (0.0, 12.0), (28.0, 40.0))
        @test r.dx ≈ -1.7 atol = 1e-10
        @test r.slope_pre ≈ 0.1 atol = 1e-10
        @test r.slope_post ≈ 0.1 atol = 1e-10
        # a degenerate (empty) window must not silently return a number
        @test isnan(trajectory_offset(t, X, tc, (100.0, 200.0), (28.0, 40.0)).dx)
    end

    @testset "(a) Ising limit J_perp -> 0: no propagation, no transmission, no memory" begin
        res = memory_experiment(N=100, Delta=3.0, Jperp=1e-8, k0=1.2, sigma=4.0,
                                standoff=28.0, dt=1.0, tmax=30.0, kink_state=:sharp)
        @test res.T_final < 1e-10          # the magnon cannot pass
        @test res.R_final > 1 - 1e-6       # all of it is still on the up side
        @test abs(res.dx1) < 1e-8          # ... hence no memory
        @test abs(res.dx2) < 1e-8
        @test abs(res.dx3) < 1e-8
    end

    @testset "(a') strong easy axis: the kink is TRANSPARENT and delta x -> -2" begin
        # REVISED CRITERION.  The pre-registered expectation was T -> 0 at large
        # Delta (an opaque, energetically deep kink).  The first run refuted it:
        # transmission is a first-order process inside the 3-domain-wall manifold
        # and the merge channel that produces reflection costs one magnon gap, so
        # R = O(Delta^-2) and the kink becomes MORE transparent as Delta grows.
        # The revised, still falsifiable criteria are below.
        r2 = memory_experiment(N=100, Delta=2.0, k0=1.2, sigma=4.0, standoff=28.0)
        r24 = memory_experiment(N=100, Delta=24.0, k0=1.2, sigma=4.0, standoff=28.0)
        @test r24.T_final > 0.99
        @test r24.R_final < r2.R_final          # reflection dies with Delta
        @test r24.R_final < 0.01
        @test abs(r24.dx1 - (-2.0)) < 0.15      # the memory saturates its quantum
    end

    @testset "(b) delta x is finite and converges in N" begin
        p = (Delta=2.0, k0=1.2, sigma=4.0, standoff=28.0, dt=0.25)
        r1 = memory_experiment(; N=100, p...)
        r2 = memory_experiment(; N=150, p...)
        @test isfinite(r1.dx1) && isfinite(r2.dx1)
        @test abs(r1.dx1) > 1e-3               # a nonzero memory effect exists
        @test abs(r1.dx1 - r2.dx1) < 0.05      # N-convergence
        @test abs(r1.T_final - r2.T_final) < 0.01
    end

    @testset "(c) both linear estimators agree; sum rule; unitarity" begin
        res = memory_experiment(N=100, Delta=2.0, k0=1.2, sigma=4.0, standoff=28.0)
        @test abs(res.dx1 - res.dx2) < 0.10    # X1 vs X2 systematic
        @test abs(res.T_final + res.R_final + res.trapped_final - 1) < 1e-10
        @test maximum(abs.(res.norms .- 1)) < 1e-12
        @test maximum(abs.(res.energies .- res.energies[1])) < 1e-10
        # the kink does not drift ballistically before or after the collision
        @test abs(res.slope_pre1) < 5e-3
        @test abs(res.slope_post1) < 5e-3
    end

    @testset "(d) quantised memory: delta x tracks -2T once the packet separates" begin
        # The operational prediction of the S^z bookkeeping (notes §4): a
        # transmitted magnon moves the wall by exactly -2 sites, a reflected one
        # by 0, hence delta x = -2 T, and |delta x| can never exceed the quantum 2.
        # Criterion applies where the packet has actually separated from the wall
        # (trapped_final < 1e-3); the small-k0 failure of that condition is a
        # wavepacket-resolution effect, tested separately in (e).
        for k0 in (1.2, 1.8)
            res = memory_experiment(N=100, Delta=2.0, k0=k0, sigma=4.0, standoff=28.0)
            @test res.trapped_final < 1e-3
            @test abs(res.dx1) <= 2 + 0.05                 # quantisation bound
            @test abs(res.dx1 - (-2 * res.T_final)) < 0.08
            @test abs(res.dx2 - (-2 * res.T_final)) < 0.05 # X2 is the cleaner estimator
        end
    end

    @testset "(e) small-k0 residual trapping is a wavepacket-resolution effect" begin
        # At small k0 the Gaussian packet of width sigma has momentum spread
        # 1/(2 sigma) comparable to k0 itself, so its slowest components
        # (v_g = J_perp sin k) never leave the wall region in the allotted time.
        # Fixed in advance: narrowing the packet in k (larger sigma) must reduce
        # the residual trapped weight at fixed k0.
        broad_k = memory_experiment(N=120, Delta=2.0, k0=0.6, sigma=3.0, standoff=26.0)
        narrow_k = memory_experiment(N=120, Delta=2.0, k0=0.6, sigma=6.0, standoff=26.0)
        @test narrow_k.trapped_final < broad_k.trapped_final
        @test abs(narrow_k.dx1 - (-2 * narrow_k.T_final)) <
              abs(broad_k.dx1 - (-2 * broad_k.T_final))
    end

    @testset "state preparation: dressed vs sharp initial kink agree" begin
        a = memory_experiment(N=100, Delta=2.0, k0=1.2, sigma=4.0, standoff=28.0,
                              kink_state=:ground)
        b = memory_experiment(N=100, Delta=2.0, k0=1.2, sigma=4.0, standoff=28.0,
                              kink_state=:sharp)
        @test b.leakage_init == 0.0            # sharp kink: no projection loss
        @test a.leakage_init > 0.0             # dressed kink: some, and it is reported
        @test abs(a.dx1 - b.dx1) < 1e-3
        @test abs(a.T_final - b.T_final) < 1e-4
    end

    @testset "geometry guards" begin
        @test_throws ArgumentError memory_experiment(N=40, Delta=2.0, k0=1.2,
                                                     sigma=6.0, standoff=30.0)
        @test_throws ArgumentError memory_experiment(N=60, Delta=2.0, k0=1.2,
                                                     sigma=6.0, standoff=20.0)
    end

    @testset "JSON serialisation" begin
        res = memory_experiment(N=100, Delta=3.0, k0=1.2, sigma=4.0, standoff=28.0)
        s = to_json(res; trajectory=false)
        @test occursin("\"dx1\"", s)
        @test occursin("\"k0\"", s)
        @test occursin("\"transmission\"", s)
        @test !occursin("NaN", s)              # NaN/Inf must be emitted as null
        @test !occursin("Inf", s)
        s2 = to_json([res]; trajectory=false)
        @test startswith(strip(s2), "[")
        st = to_json(res; trajectory=true)
        @test occursin("\"times\"", st) && occursin("\"X1\"", st)
    end
end
