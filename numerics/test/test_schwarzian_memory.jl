# test_schwarzian_memory.jl -- failing-first tests for the sourced Schwarzian
# memory computation.  Standalone; the shared test runner is intentionally
# untouched.  Thresholds are fixed before the implementation (law L1).

using Test
using LinearAlgebra
using JSON

include(joinpath(@__DIR__, "..", "src", "schwarzian_memory.jl"))
using .SchwarzianMemory

const EXACT_TOL = 1.0e-10
const CHARGE_TOL = 1.0e-8
const JUMP_TOL = 1.0e-6
const GAUGE_TOL = 1.0e-8
const ORDER_FLOOR = 3.8                 # RK4 expected order minus 0.2
const CAMPAIGN = Ref{Any}()

# Poisoned child invocations are an executable exit-code contract: each must
# terminate nonzero, and validation must occur before its requested JSON path
# can be created.
if haskey(ENV, "SCHWARZIAN_MEMORY_POISON")
    mode = Symbol(ENV["SCHWARZIAN_MEMORY_POISON"])
    out = ENV["SCHWARZIAN_MEMORY_POISON_OUT"]
    write_results(out, poisoned_result(mode))
    error("poison mode $(mode) was incorrectly accepted")
end

@testset "sourced two-sided Schwarzian memory" begin
    @testset "unsourced thermal saddle over several periods" begin
        # Each interval is a regular projective chart of tan(u/2).  Repeating
        # it in three periods checks the periodic exact map without asking a
        # floating-point affine chart to cross tan's poles.
        for period in -1:1
            u0 = -2.0 + 2pi * period
            u1 =  2.0 + 2pi * period
            tr = integrate_fixed(thermal_tan_state(u0), u0, u1, 5.0e-4,
                                 10.0, ZeroPulse())
            errs = [maximum(abs.(tr.y[:, i] .- thermal_tan_state(tr.u[i])))
                    for i in eachindex(tr.u)]
            @test maximum(errs) < EXACT_TOL
        end
    end

    @testset "equation, SL(2) charge ledger, and RK4 order" begin
        p = TopHatPulse(0.1)
        run = simulate_pulse(10.0, p; h = 2.5e-4)
        @test run.pre_charge_drift < CHARGE_TOL
        @test run.post_charge_drift < CHARGE_TOL
        # T.1 makes the Schwarzian boundary charge lose exactly the charge
        # injected into matter, so the oriented jump is Q_before-Q_after.
        @test maximum(abs.(run.charge_before .- run.charge_after .- run.flux)) < JUMP_TOL
        @test run.mobius_fit_residual < EXACT_TOL

        hs = (0.08, 0.04, 0.02, 0.01)
        errors = Float64[]
        exact = thermal_tan_state(1.6)
        for h in hs
            tr = integrate_fixed(thermal_tan_state(-1.6), -1.6, 1.6, h,
                                 10.0, ZeroPulse())
            push!(errors, norm(tr.y[:, end] - exact, Inf))
        end
        orders = log2.(errors[1:end-1] ./ errors[2:end])
        @test minimum(orders) >= ORDER_FLOOR
    end

    @testset "all prescribed profiles obey the charge cross-check" begin
        profiles = AbstractPulse[
            TopHatPulse(0.01), TopHatPulse(0.1),
            GaussianPulse(0.05), DerivativeGaussianPulse(0.05),
        ]
        for C in (10.0, 100.0), p in profiles
            run = simulate_pulse(C, p; h = 5.0e-4)
            @test !isempty(run.pulse.u)
            @test all(isfinite, run.pulse.y)
            @test run.pre_charge_drift < CHARGE_TOL
            @test run.post_charge_drift < CHARGE_TOL
            @test maximum(abs.(run.charge_before .- run.charge_after .- run.flux)) < JUMP_TOL
        end
    end

    @testset "relative frame and simultaneous-gauge invariance" begin
        run = simulate_pulse(10.0, GaussianPulse(0.05); h = 2.5e-4)
        ML = Matrix{Float64}(I, 2, 2)
        MR = run.mobius
        g = normalize_sl2([1.17 0.23; -0.11 0.83])
        rel0 = relative_element(ML, MR)
        rel1 = relative_element(g * ML, g * MR)
        @test norm(rel0 - rel1, Inf) < GAUGE_TOL

        Tgrid = [2.0, 5.0, 10.0, 20.0, 40.0]
        obs0 = observable_series(ML, MR, 1.0, run.k_final, Tgrid)
        obs1 = observable_series(g * ML, g * MR, 1.0, run.k_final, Tgrid)
        @test maximum(abs.(obs0.delta_u .- obs1.delta_u)) < GAUGE_TOL
        @test maximum(abs.(obs0.delta_g .- obs1.delta_g)) < GAUGE_TOL
        @test all(isfinite, obs0.delta_u)
        @test all(isfinite, obs0.delta_g)
    end

    @testset "bilocal model comparison and DC convergence" begin
        run = simulate_pulse(100.0, TopHatPulse(0.1); h = 2.5e-4)
        Tgrid = [2.0, 5.0, 10.0, 20.0, 40.0]
        obs = observable_series(Matrix{Float64}(I, 2, 2), run.mobius,
                                1.0, run.k_final, Tgrid)
        fit_u = compare_models(Tgrid, obs.delta_u)
        fit_g = compare_models(Tgrid, obs.delta_g)
        @test fit_u.winner in ("constant", "exponential")
        @test fit_g.winner in ("constant", "exponential")
        @test all(isfinite, (fit_u.rss_constant, fit_u.rss_exponential,
                             fit_g.rss_constant, fit_g.rss_exponential))

        dc = dc_identity(run, obs.delta_u[end])
        # Circular-DC regression: the late detector is only a comparison
        # target.  A decoy value must not enter the transform or change its
        # absolute extrapolated residue.
        decoy_late = 2 * obs.delta_u[end]
        dc_decoy = dc_identity(run, decoy_late)
        residue = dc.residue_ratio[end] * obs.delta_u[end]
        decoy_residue = dc_decoy.residue_ratio[end] * decoy_late
        @test isapprox(decoy_residue, residue; rtol = 1.0e-2)
        @test dc_decoy.extrapolated_residue == dc.extrapolated_residue
        @test dc_decoy.fitted_mobius_tail == dc.fitted_mobius_tail
        @test length(dc.omega) >= 3
        @test dc.horizon == [20.0, 40.0, 80.0]
        @test all(isfinite, dc.residue_ratio)
        @test all(isfinite, dc.soft_ratio)
        @test abs(dc.residue_ratio[end] - 1.0) < 5.0e-2
        @test abs(dc.soft_ratio[end] - 1.0) < 5.0e-2
        @test abs(dc.extrapolated_late_ratio - 1.0) < 5.0e-3
        @test dc.horizon_error < 1.0e-7 * abs(dc.extrapolated_residue)
        @test abs(dc.residue_ratio[end] - 1.0) <=
              abs(dc.residue_ratio[1] - 1.0)
    end

    @testset "operator dimension API and Delta=1 handshake" begin
        M = [1.05286503580 -0.0909883081018;
             0.0334727279376 0.946896647924]
        ts = [2.0, 4.0, 8.0]
        half = observable_series(Matrix{Float64}(I, 2, 2), M, 1.0, 1.0, ts)
        one = observable_series(Matrix{Float64}(I, 2, 2), M, 1.0, 1.0, ts;
                                Delta = 1.0)
        @test one.pulse ≈ half.pulse .^ 2 rtol = 1.0e-12
        @test one.equilibrium ≈ half.equilibrium .^ 2 rtol = 1.0e-12
        @test one.delta_g ≈ [-1.43615624490e-3, -3.21934849346e-5,
                                  -1.10134890247e-8] rtol = 2.0e-9
        @test all(isfinite, one.delta_u)
        @test_throws ArgumentError observable_series(Matrix{Float64}(I, 2, 2),
                                                      M, 1.0, 1.0, ts; Delta = 0.0)
    end

    @testset "finiteness and fail-closed output" begin
        valid_stub = validation_fixture()
        @test validate_results(valid_stub)
        for mode in (:nan, :empty, :charge)
            bad = poisoned_result(mode)
            @test_throws ResultValidationError validate_results(bad)
            path = tempname() * ".json"
            @test_throws ResultValidationError write_results(path, bad)
            @test !isfile(path)

            child_path = tempname() * ".json"
            cmd = addenv(`$(Base.julia_cmd()) --project=$(joinpath(@__DIR__, "..")) $(abspath(@__FILE__))`,
                         "SCHWARZIAN_MEMORY_POISON" => String(mode),
                         "SCHWARZIAN_MEMORY_POISON_OUT" => child_path)
            proc = run(pipeline(ignorestatus(cmd), stdout = devnull, stderr = devnull))
            @test proc.exitcode != 0
            @test !isfile(child_path)
        end
    end

    @testset "complete prescribed campaign" begin
        results = run_campaign(; h = 5.0e-4)
        @test length(results["parameter_points"]) == 8
        @test results["late_time_grid"] == [2.0, 5.0, 10.0, 20.0, 40.0]
        @test results["operator_dimension"] == 0.5
        @test haskey(results, "limit_convention")
        @test all(p -> p["detector_window"]["maximum_usable_T"] > 0,
                  results["parameter_points"])
        @test all(p -> isfinite(p["detector_window"]["sample_cost_for_10pct_late_delta"]),
                  results["parameter_points"])
        @test validate_results(results)
        CAMPAIGN[] = results
    end
end

# Reached only if the outer test set is green.  write_results validates again,
# so a later regression cannot leave a plausible-looking partial artifact.
write_results(joinpath(@__DIR__, "..", "results", "schwarzian_memory.json"),
              CAMPAIGN[])
