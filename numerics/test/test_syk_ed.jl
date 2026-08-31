# test_syk_ed.jl -- failing-first contract for the finite-N SYK ED rung.
#
# This file is intentionally standalone: the shared runner is outside this
# lane.  Thresholds and the campaign grid were fixed before syk_ed.jl existed.

using Test
using LinearAlgebra
using JSON

include(joinpath(@__DIR__, "..", "src", "syk_ed.jl"))
using .SYKED

const EXACT_TOL = 1.0e-10
const ENERGY_REL_TOL = 1.0e-6
const ORDER_FLOOR = 1.75
const MAIN_N = [8, 10, 12]
const BETAS = [5.0, 10.0]
const SEEDS = [1701, 1702, 1703, 1704, 1705]
const CAMPAIGN = Ref{Any}()

# Child processes make the nonzero-exit/no-artifact rule executable.
if haskey(ENV, "SYK_ED_POISON")
    mode = Symbol(ENV["SYK_ED_POISON"])
    out = ENV["SYK_ED_POISON_OUT"]
    write_results(out, poisoned_result(mode))
    error("poison mode $(mode) was incorrectly accepted")
end

@testset "finite-N two-dot SYK ED rung" begin
    @testset "Clifford representation and q=4 normalization" begin
        model = build_syk(8; J = 1.0, seed = 11)
        d = 2^(model.Nm ÷ 2)
        @test size(model.H) == (d, d)
        @test norm(model.H - model.H', Inf) < EXACT_TOL
        @test norm(model.parity^2 - I, Inf) < EXACT_TOL
        for i in 1:model.Nm, j in 1:model.Nm
            target = i == j ? Matrix{ComplexF64}(I, d, d) : zeros(ComplexF64, d, d)
            @test norm(model.majoranas[i] * model.majoranas[j] +
                       model.majoranas[j] * model.majoranas[i] - target, Inf) < EXACT_TOL
        end
        @test model.coupling_variance == 6 / model.Nm^3
    end

    @testset "TFD thermal marginals and exact energy relation" begin
        model = build_syk(8; J = 1.0, seed = 23)
        tfd = prepare_tfd(model, 5.0)
        named = [
            "Hamiltonian H" => model.H,
            "fermion parity P" => model.parity,
            "bilinear iχ₁χ₂" => bilinear_operator(model, 1, 2),
        ]
        for (_, observable) in named
            thermal = thermal_expectation(tfd, observable)
            @test isapprox(expect_left(tfd.coefficient, observable), thermal;
                           atol = EXACT_TOL, rtol = EXACT_TOL)
            @test isapprox(expect_right(tfd.coefficient, observable), thermal;
                           atol = EXACT_TOL, rtol = EXACT_TOL)
        end
        # With Theta=exp(i*pi*P/4)K and H_R=conj(H), this is an exact vector
        # identity, not merely equality of mean energies.
        @test tfd.energy_relation_residual < EXACT_TOL
        @test isapprox(norm(tfd.coefficient), 1.0; atol = EXACT_TOL)
    end

    @testset "reference conservation and analytic free check" begin
        model = build_syk(8; J = 1.0, seed = 31)
        tfd = prepare_tfd(model, 10.0)
        initial = reference_observables(model, tfd, 0.0)
        for T in (0.7, 1.9, 4.3)
            obs = reference_observables(model, tfd, T)
            @test abs(obs.energy_left - initial.energy_left) < EXACT_TOL
            @test abs(obs.energy_right - initial.energy_right) < EXACT_TOL
            @test abs(obs.total_parity - initial.total_parity) < EXACT_TOL
        end

        # For H=0 the parity-twisted fermionic maximally entangled state is
        # stabilized by every -i*chi_i^L*chi_i^R, so G_LR(T)=1/2 exactly.
        free = zero_model(4)
        free_tfd = prepare_tfd(free, 7.0)
        for T in (0.0, 0.6, 3.0)
            C = reference_coefficient(free, free_tfd, T)
            @test isapprox(detector_stats(free, C).mean, 0.5;
                           atol = EXACT_TOL, rtol = EXACT_TOL)
        end
    end

    @testset "right pulse, energy balance, and exact left-blindness" begin
        model = build_syk(8; J = 1.0, seed = 47)
        tfds = [prepare_tfd(model, beta) for beta in BETAS]
        profile, tuning = tune_balanced_pulse(model, tfds; dt = 0.01)
        @test profile.kind == :derivative_gaussian
        @test profile.amplitude > 0
        @test tuning.maximum_relative_energy_change < ENERGY_REL_TOL
        Uright = pulse_unitary(model, profile; dt = 0.01)
        @test norm(Uright' * Uright - I, Inf) < EXACT_TOL

        for tfd in tfds
            Cref = reference_coefficient(model, tfd, 2.4)
            Cpulse = pulsed_coefficient(model, tfd, Uright, 2.4)
            for observable in (model.H, model.parity,
                               bilinear_operator(model, 3, 6))
                @test isapprox(expect_left(Cpulse, observable),
                               expect_left(Cref, observable);
                               atol = EXACT_TOL, rtol = EXACT_TOL)
            end
            @test norm(Cpulse * Cpulse' - Cref * Cref', Inf) < EXACT_TOL
            @test relative_energy_change(model, tfd, Uright) < ENERGY_REL_TOL
        end

        control = PulseProfile(:gaussian, 0.0, 1.0, 0.5, 0.12,
                               profile.amplitude)
        @test abs(profile_integral(control)) > 1.0e-5 * profile.amplitude
    end

    @testset "integrator step-halving and detector statistics" begin
        model = build_syk(8; J = 1.0, seed = 59)
        tfd = prepare_tfd(model, 5.0)
        profile, _ = tune_balanced_pulse(model, [tfd]; dt = 0.01)
        convergence = integrator_convergence(model, profile)
        @test convergence.observed_order >= ORDER_FLOOR
        @test convergence.fine_difference < 2.0e-5
        @test convergence.maximum_unitarity_error < EXACT_TOL

        Uright = pulse_unitary(model, profile; dt = 0.01)
        series = detector_series(model, tfd, Uright,
                                 [1.5, 2.0, 2.5, 3.0])
        @test length(series.times) == 4
        @test all(isfinite, series.delta_abs)
        @test all(isfinite, series.delta_u_rel)
        @test all(x -> x >= -EXACT_TOL, series.variance_pulse)
        @test all(x -> x >= -EXACT_TOL, series.variance_reference)
        @test all(x -> x >= 1, series.shots_for_10pct_delta)
        @test model_comparison(series.times, series.delta_abs).winner in
              ("constant", "exponential")
    end

    @testset "finiteness and fail-closed output" begin
        @test validate_results(validation_fixture())
        for mode in (:nan, :empty_window, :energy_gate, :order_gate)
            bad = poisoned_result(mode)
            @test_throws ResultValidationError validate_results(bad)
            path = tempname() * ".json"
            @test_throws ResultValidationError write_results(path, bad)
            @test !isfile(path)

            child_path = tempname() * ".json"
            cmd = addenv(`$(Base.julia_cmd()) --project=$(joinpath(@__DIR__, "..")) $(abspath(@__FILE__))`,
                         "SYK_ED_POISON" => String(mode),
                         "SYK_ED_POISON_OUT" => child_path)
            proc = run(pipeline(ignorestatus(cmd), stdout = devnull,
                                stderr = devnull))
            @test proc.exitcode != 0
            @test !isfile(child_path)
        end
    end

    @testset "complete prescribed campaign" begin
        results = run_campaign(; Ns = MAIN_N, betas = BETAS, seeds = SEEDS,
                               include_n14 = true, dt = 0.01)
        @test results["main_grid"] == Dict("Nm" => MAIN_N,
                                           "betaJ" => BETAS,
                                           "seeds" => SEEDS)
        @test length(results["parameter_points"]) ==
              length(MAIN_N) * length(BETAS) * length(SEEDS)
        @test length(results["n14_confirmation"]) == 1
        @test all(row -> row["balanced_energy_gate"]["relative_change"] <
                         ENERGY_REL_TOL, results["parameter_points"])
        @test all(row -> length(row["times"]) == 8,
                  results["parameter_points"])
        @test length(results["self_averaging"]) == length(MAIN_N) * length(BETAS)
        @test validate_results(results)
        CAMPAIGN[] = results
    end
end

# Reached only after the full green suite.  write_results validates again.
write_results(joinpath(@__DIR__, "..", "results", "syk_ed.json"), CAMPAIGN[])
