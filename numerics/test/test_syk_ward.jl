# test_syk_ward.jl -- failing-first contract for lane G3-WARD-NUMERIC.
#
# This test is intentionally standalone.  It includes the existing SYK ED
# implementation through the lane module, but neither edits nor extends it.

using Test
using LinearAlgebra
using Random
using JSON

include(joinpath(@__DIR__, "..", "src", "syk_ward.jl"))
using .SYKWard

const EXACT_TOL = 1.0e-10
const ORDER_FLOOR = 1.70
const MAIN_N = [8, 10, 12]
const BETAS = [5.0, 10.0]
const SEEDS = [3101, 3102, 3103]
const CAMPAIGN = Ref{Any}()

# Child processes make the nonzero-exit/no-artifact rule executable.
if haskey(ENV, "SYK_WARD_POISON")
    mode = Symbol(ENV["SYK_WARD_POISON"])
    out = ENV["SYK_WARD_POISON_OUT"]
    write_results(out, poisoned_result(mode))
    error("poison mode $(mode) was incorrectly accepted")
end

@testset "G3 finite-N Ward-defect experiment" begin
    @testset "n=0 exactness is the calibration line" begin
        model = build_syk(8; J = 1.0, seed = 101)
        tfd = prepare_tfd(model, 5.0)
        observables = campaign_observables(model, 5.0; delta = 0.15)
        states = tfd_sector_states(tfd, observables)
        q0 = exact_hamiltonian_candidate(model)

        @test hermiticity_error(q0) < EXACT_TOL
        @test parity_error(q0, model) < EXACT_TOL
        for observable in observables
            row = ward_metrics(q0, observable, states, 0, 5.0)
            @test row.relative_defect < EXACT_TOL
            @test row.maximum_imaginary_part < EXACT_TOL
        end
    end

    @testset "heat-kernel regulator has both controlled limits" begin
        model = build_syk(8; J = 1.0, seed = 103)
        raw = bilocal_observable(model, 0.23, -0.31; delta = 0.0,
                                 label = "limit probe")
        zero = bilocal_observable(model, 0.23, -0.31; delta = 0.0,
                                  label = "zero regulator")
        large = bilocal_observable(model, 0.23, -0.31; delta = 1.0e5,
                                   label = "large regulator")
        rng = MersenneTwister(7)
        C = randn(rng, ComplexF64, size(model.H))
        C ./= norm(C)

        @test norm(apply_observable(zero, C) - apply_observable(raw, C)) < EXACT_TOL

        # H is shifted by its ground energy only inside exp[-delta(H-E0)],
        # which leaves all commutators unchanged.  The large-delta limit is
        # therefore the exact ground-space compression P0 A P0.
        P0 = ground_projector(model)
        projected = P0 * apply_observable(raw, P0 * C * P0) * P0
        @test norm(apply_observable(large, C) - projected) < 1.0e-8
        @test observable_adjoint_error(zero; seed = 11) < EXACT_TOL
        @test observable_adjoint_error(large; seed = 13) < EXACT_TOL
    end

    @testset "candidate operators are even, Hermitian, and nontrivial" begin
        model = build_syk(8; J = 1.0, seed = 107)
        for candidate in (
            frequency_filtered_candidate(model, 5.0, 2;
                                         width_cycles = 1.0, steps = 96),
            ledger_candidate(model, 5.0, 2;
                             width_cycles = 1.0, steps = 96),
        )
            @test hermiticity_error(candidate) < EXACT_TOL
            @test parity_error(candidate, model) < EXACT_TOL
            @test opnorm(candidate.local_q) > 1.0e-12
        end
    end

    @testset "finite time quadratures show second-order convergence" begin
        model = build_syk(8; J = 1.0, seed = 109)
        for family in (:filtered, :ledger)
            convergence = quadrature_convergence(
                model, 5.0, 2, family;
                width_cycles = 1.0, steps = (24, 48, 96),
            )
            @test convergence.observed_order >= ORDER_FLOOR
            @test convergence.fine_difference < convergence.coarse_difference
            @test all(isfinite, (convergence.observed_order,
                                 convergence.coarse_difference,
                                 convergence.fine_difference))
        end
    end

    @testset "finiteness and fail-closed output" begin
        @test validate_results(validation_fixture())
        for mode in (:nan, :empty, :calibration, :hermiticity, :parity, :order)
            bad = poisoned_result(mode)
            @test_throws ResultValidationError validate_results(bad)
            path = tempname() * ".json"
            @test_throws ResultValidationError write_results(path, bad)
            @test !isfile(path)

            child_path = tempname() * ".json"
            cmd = addenv(
                `$(Base.julia_cmd()) --project=$(joinpath(@__DIR__, "..")) $(abspath(@__FILE__))`,
                "SYK_WARD_POISON" => String(mode),
                "SYK_WARD_POISON_OUT" => child_path,
            )
            proc = run(pipeline(ignorestatus(cmd), stdout = devnull,
                                stderr = devnull))
            @test proc.exitcode != 0
            @test !isfile(child_path)
        end
    end

    @testset "complete prescribed campaign" begin
        results = run_campaign(
            Ns = MAIN_N,
            betas = BETAS,
            seeds = SEEDS,
            include_n14 = true,
            steps = 96,
        )
        @test results["main_grid"] == Dict(
            "Nm" => MAIN_N,
            "betaJ" => BETAS,
            "seeds" => SEEDS,
        )
        @test results["n0_control"]["maximum_relative_defect"] < EXACT_TOL
        @test length(results["main_rows"]) ==
              length(MAIN_N) * length(BETAS) * length(SEEDS) * 3 * 4
        @test length(results["n1_control_rows"]) ==
              length(MAIN_N) * length(BETAS) * length(SEEDS) * 3 * 2
        @test length(results["fits"]) == length(BETAS) * 4
        @test length(results["n14_confirmation"]) == 6
        @test all(row -> row["relative_defect"] >= 0,
                  results["main_rows"])
        @test all(row -> row["hermiticity_error"] < EXACT_TOL &&
                         row["parity_error"] < EXACT_TOL,
                  results["main_rows"])
        @test validate_results(results)
        CAMPAIGN[] = results
    end
end

# Reached only after the full green suite.  write_results validates again.
write_results(joinpath(@__DIR__, "..", "results", "syk_ward.json"),
              CAMPAIGN[])
