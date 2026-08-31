"""
    SYKWard

Finite-N Ward-defect experiment for the first non-Mobius thermal Fourier
mode.  This lane-local module includes, but does not modify, `syk_ed.jl`.
All operators are represented exactly on the one-dot Hilbert space; two-dot
operators act on TFD coefficient matrices without forming a dense d^2-by-d^2
matrix.
"""
module SYKWard

using LinearAlgebra
using Random
using Statistics
using JSON

include(joinpath(@__DIR__, "syk_ed.jl"))
using .SYKED: SYKModel, TFDData, build_syk, prepare_tfd

export SYKModel, TFDData, build_syk, prepare_tfd,
       BilocalObservable, CandidateOperator, ResultValidationError,
       bilocal_observable, apply_observable, bilocal_variation,
       campaign_observables, tfd_sector_states, ground_projector,
       observable_adjoint_error, exact_hamiltonian_candidate,
       frequency_filtered_candidate, ledger_candidate,
       hermiticity_error, parity_error, commutator_action, ward_metrics,
       quadrature_convergence, scaling_comparison, validation_fixture,
       poisoned_result, validate_results, write_results, run_campaign

const ENDPOINT_DIMENSION = 0.25
const HEAT_DELTA = 0.15
const QUADRATURE_ORDER_FLOOR = 1.70
const EXACT_GATE = 1.0e-10

struct ResultValidationError <: Exception
    message::String
end
Base.showerror(io::IO, e::ResultValidationError) = print(io, e.message)

"""A finite sum `factor * sum_j left[j] * C * right[j]`."""
struct BilocalObservable
    label::String
    u::Float64
    v::Float64
    delta::Float64
    factor::ComplexF64
    left::Vector{Matrix{ComplexF64}}
    right::Vector{Matrix{ComplexF64}}
    du_left::Vector{Matrix{ComplexF64}}
    dv_right::Vector{Matrix{ComplexF64}}
end

"""One-dot `q`; the physical two-dot candidate is q_L + conjugate(q)_R."""
struct CandidateOperator
    family::String
    mode::Int
    beta::Float64
    width_cycles::Float64
    steps::Int
    local_q::Matrix{ComplexF64}
end

function _heisenberg(model::SYKModel, A::AbstractMatrix, time::Real)
    V, E = model.eigenvectors, model.energies
    Ae = V' * A * V
    phases = cis.(Float64(time) .* (E .- E'))
    return Matrix{ComplexF64}(V * (phases .* Ae) * V')
end

function _heat_kernel(model::SYKModel, delta::Real)
    delta >= 0 || throw(ArgumentError("heat-kernel delta must be nonnegative"))
    weights = exp.(-Float64(delta) .* (model.energies .- minimum(model.energies)))
    return Matrix{ComplexF64}(model.eigenvectors * Diagonal(weights) *
                             model.eigenvectors')
end

"""Spectral projector onto the possibly degenerate one-dot ground space."""
function ground_projector(model::SYKModel)
    e0 = minimum(model.energies)
    tolerance = 100 * eps(Float64) * max(1.0, maximum(abs, model.energies))
    mask = abs.(model.energies .- e0) .<= tolerance
    V0 = model.eigenvectors[:, mask]
    return Matrix{ComplexF64}(V0 * V0')
end

"""
Construct the regulated Hermitian mixed bilocal.

The coefficient-matrix representation is an anti-representation on the
right.  Therefore a right operator at forward boundary time `v` is carried
by the one-dot multiplier `chi(-v)`.  This is precisely what makes
`i[H_L+H_R,B]=(partial_u+partial_v)B`.
"""
function bilocal_observable(model::SYKModel, u::Real, v::Real;
                            delta::Real = HEAT_DELTA,
                            label::AbstractString = "mixed LR")
    K = _heat_kernel(model, delta)
    left = Matrix{ComplexF64}[]
    right = Matrix{ComplexF64}[]
    du_left = Matrix{ComplexF64}[]
    dv_right = Matrix{ComplexF64}[]
    H, P = model.H, model.parity
    for chi in model.majoranas
        xu = _heisenberg(model, chi, u)
        # Right coefficient multipliers reverse physical products and time.
        xv = _heisenberg(model, chi, -v)
        dxu = im .* (H * xu - xu * H)
        dxv = -im .* (H * xv - xv * H)
        push!(left, K * (xu * P) * K)
        push!(right, K * xv * K)
        push!(du_left, K * (dxu * P) * K)
        push!(dv_right, K * dxv * K)
    end
    return BilocalObservable(String(label), Float64(u), Float64(v),
                             Float64(delta), -im / model.Nm,
                             left, right, du_left, dv_right)
end

function apply_observable(observable::BilocalObservable, C::AbstractMatrix)
    out = zeros(ComplexF64, size(C))
    for j in eachindex(observable.left)
        out .+= observable.factor .* observable.left[j] * C * observable.right[j]
    end
    return out
end

_epsilon(mode::Int, beta::Real, t::Real) =
    mode == 0 ? 1.0 : cos(2pi * mode * Float64(t) / Float64(beta))
_epsilon_prime(mode::Int, beta::Real, t::Real) =
    mode == 0 ? 0.0 : -(2pi * mode / Float64(beta)) *
                           sin(2pi * mode * Float64(t) / Float64(beta))

"""Action of the target bilocal variation (memo equation (4.2))."""
function bilocal_variation(observable::BilocalObservable, mode::Int,
                           beta::Real, C::AbstractMatrix;
                           Delta::Real = ENDPOINT_DIMENSION)
    mode >= 0 || throw(ArgumentError("mode must be nonnegative"))
    beta > 0 || throw(ArgumentError("beta must be positive"))
    Delta > 0 || throw(ArgumentError("endpoint dimension must be positive"))
    eu, ev = _epsilon(mode, beta, observable.u),
             _epsilon(mode, beta, observable.v)
    deu, dev = _epsilon_prime(mode, beta, observable.u),
               _epsilon_prime(mode, beta, observable.v)
    out = zeros(ComplexF64, size(C))
    for j in eachindex(observable.left)
        L, R = observable.left[j], observable.right[j]
        dL, dR = observable.du_left[j], observable.dv_right[j]
        out .+= observable.factor .* (
            eu .* dL * C * R + ev .* L * C * dR +
            Delta * (deu + dev) .* L * C * R
        )
    end
    return out
end

function campaign_observables(model::SYKModel, beta::Real;
                              delta::Real = HEAT_DELTA)
    return [
        bilocal_observable(model, 0.0, 0.0; delta = delta,
                           label = "equal LR (0,0)"),
        bilocal_observable(model, 0.0, beta / 8; delta = delta,
                           label = "unequal LR (0,beta/8)"),
        bilocal_observable(model, -beta / 10, beta / 10; delta = delta,
                           label = "symmetric LR (-beta/10,beta/10)"),
    ]
end

function _normalize_state(C)
    n = norm(C)
    n > 100 * eps(Float64) || error("bilocal insertion annihilated the TFD")
    return Matrix{ComplexF64}(C ./ n)
end

"""TFD plus two normalized one-bilocal-insertion vectors."""
function tfd_sector_states(tfd::TFDData,
                           observables::AbstractVector{BilocalObservable})
    length(observables) >= 2 || throw(ArgumentError("need two insertion operators"))
    C0 = _normalize_state(tfd.coefficient)
    return [C0,
            _normalize_state(apply_observable(observables[1], C0)),
            _normalize_state(apply_observable(observables[2], C0))]
end

function observable_adjoint_error(observable::BilocalObservable; seed::Int = 1)
    rng = MersenneTwister(seed)
    X = randn(rng, ComplexF64, size(first(observable.left)))
    Y = randn(rng, ComplexF64, size(first(observable.left)))
    lhs = dot(X, apply_observable(observable, Y))
    rhs = dot(apply_observable(observable, X), Y)
    return abs(lhs - rhs) /
           max(norm(X) * norm(Y), abs(lhs), abs(rhs), eps(Float64))
end

function exact_hamiltonian_candidate(model::SYKModel)
    return CandidateOperator("exact Hamiltonian", 0, 1.0, 0.0, 0,
                             copy(model.H))
end

function _quadrature_nodes(beta::Real, width_cycles::Real, steps::Int)
    beta > 0 || throw(ArgumentError("beta must be positive"))
    width_cycles > 0 || throw(ArgumentError("width must be positive"))
    steps >= 8 || throw(ArgumentError("quadrature needs at least eight steps"))
    sigma = Float64(width_cycles) * Float64(beta) / (2pi)
    bound = 4sigma
    ts = collect(range(-bound, bound; length = steps + 1))
    h = 2bound / steps
    weights = fill(h, steps + 1)
    weights[1] /= 2
    weights[end] /= 2
    envelope = exp.(-0.5 .* (ts ./ sigma) .^ 2)
    normalization = dot(weights, envelope)
    return ts, weights .* envelope ./ normalization
end

function _quadrature_candidate(model::SYKModel, beta::Real, mode::Int,
                               family::Symbol; width_cycles::Real,
                               steps::Int)
    mode >= 1 || throw(ArgumentError("filtered candidates require mode >= 1"))
    family in (:filtered, :ledger) || throw(ArgumentError("unknown family"))
    ts, weights = _quadrature_nodes(beta, width_cycles, steps)
    H, A2 = model.H, model.pulse_operator
    q = zeros(ComplexF64, size(H))
    for (t, weight) in zip(ts, weights)
        At = _heisenberg(model, A2, t)
        epsilon = _epsilon(mode, beta, t)
        if family == :filtered
            q .+= weight .* epsilon .* At
        else
            correction = (im / 2) * _epsilon_prime(mode, beta, t) .*
                         (H * At - At * H)
            q .+= weight .* (epsilon .* H + correction)
        end
    end
    # Roundoff-only symmetrization; no fitted coefficient is introduced.
    q = Matrix{ComplexF64}(Hermitian((q + q') / 2))
    name = family == :filtered ? "frequency-filtered bilinear" :
                                 "naive EFT ledger"
    return CandidateOperator(name, mode, Float64(beta), Float64(width_cycles),
                             steps, q)
end

function frequency_filtered_candidate(model::SYKModel, beta::Real, mode::Int;
                                      width_cycles::Real = 1.0,
                                      steps::Int = 96)
    return _quadrature_candidate(model, beta, mode, :filtered;
                                 width_cycles = width_cycles, steps = steps)
end

function ledger_candidate(model::SYKModel, beta::Real, mode::Int;
                          width_cycles::Real = 1.0, steps::Int = 96)
    return _quadrature_candidate(model, beta, mode, :ledger;
                                 width_cycles = width_cycles, steps = steps)
end

function hermiticity_error(candidate::CandidateOperator)
    q = candidate.local_q
    return norm(q - q', Inf) / max(opnorm(q), eps(Float64))
end

function parity_error(candidate::CandidateOperator, model::SYKModel)
    q, P = candidate.local_q, model.parity
    return norm(P * q - q * P, Inf) / max(opnorm(q), eps(Float64))
end

function _candidate_action(candidate::CandidateOperator, C::AbstractMatrix)
    q = candidate.local_q
    return q * C + C * q
end

"""Action of `i[Q_L+Q_R,A]` in coefficient-matrix form."""
function commutator_action(candidate::CandidateOperator,
                           observable::BilocalObservable,
                           C::AbstractMatrix)
    AC = apply_observable(observable, C)
    return im .* (_candidate_action(candidate, AC) -
                  apply_observable(observable, _candidate_action(candidate, C)))
end

"""
Ward mismatch on the three-dimensional TFD/one-insertion test sector.
`relative_defect` is the Frobenius-relative mismatch of all 3x3 matrix
elements.  The stronger unprojected action mismatch is returned separately.
"""
function ward_metrics(candidate::CandidateOperator,
                      observable::BilocalObservable,
                      states::AbstractVector, mode::Int, beta::Real)
    actual_actions = [commutator_action(candidate, observable, C) for C in states]
    target_actions = [bilocal_variation(observable, mode, beta, C) for C in states]
    residual_norm = sqrt(sum(abs2(norm(a - b)) for (a, b) in
                             zip(actual_actions, target_actions)))
    target_norm = sqrt(sum(abs2(norm(b)) for b in target_actions))
    actual_norm = sqrt(sum(abs2(norm(a)) for a in actual_actions))
    action_scale = max(target_norm, actual_norm, 100 * eps(Float64))
    actual_elements = ComplexF64[dot(bra, action)
        for action in actual_actions for bra in states]
    target_elements = ComplexF64[dot(bra, action)
        for action in target_actions for bra in states]
    matrix_scale = max(norm(actual_elements), norm(target_elements),
                       100 * eps(Float64))
    matrix_residual = norm(actual_elements - target_elements)
    diagonal_actual = ComplexF64[dot(states[k], actual_actions[k])
                                  for k in eachindex(states)]
    diagonal_target = ComplexF64[dot(states[k], target_actions[k])
                                  for k in eachindex(states)]
    max_imag = maximum(abs, imag.(vcat(diagonal_actual, diagonal_target)))
    return (relative_defect = matrix_residual / matrix_scale,
            action_relative_defect = residual_norm / action_scale,
            matrix_residual_norm = matrix_residual,
            residual_norm = residual_norm,
            target_action_norm = target_norm,
            actual_action_norm = actual_norm,
            actual_matrix_elements = actual_elements,
            target_matrix_elements = target_elements,
            maximum_imaginary_part = max_imag)
end

function quadrature_convergence(model::SYKModel, beta::Real, mode::Int,
                                family::Symbol; width_cycles::Real = 1.0,
                                steps = (24, 48, 96))
    length(steps) == 3 || throw(ArgumentError("need three step counts"))
    steps[2] == 2steps[1] && steps[3] == 2steps[2] ||
        throw(ArgumentError("step counts must successively double"))
    maker = family == :filtered ? frequency_filtered_candidate :
            family == :ledger ? ledger_candidate :
            throw(ArgumentError("unknown family"))
    qs = [maker(model, beta, mode; width_cycles = width_cycles,
                steps = n).local_q for n in steps]
    coarse = norm(qs[1] - qs[2])
    fine = norm(qs[2] - qs[3])
    fine > 0 || throw(ResultValidationError("zero quadrature difference"))
    order = log2(coarse / fine)
    return (observed_order = order, coarse_difference = coarse,
            fine_difference = fine, steps = collect(Int, steps))
end

"""Constant-versus-power-law AIC comparison on positive defect means."""
function scaling_comparison(Ns::AbstractVector, values::AbstractVector)
    length(Ns) == length(values) >= 3 || throw(ArgumentError("bad scaling data"))
    N, y = Float64.(Ns), Float64.(values)
    all(x -> x >= 0 && isfinite(x), y) || throw(ArgumentError("invalid defects"))
    constant = mean(y)
    rss_constant = sum(abs2, y .- constant)
    best = (rss = Inf, amplitude = NaN, exponent = NaN)
    for exponent in range(0.05, 8.0; length = 2400)
        basis = N .^ (-exponent)
        amplitude = dot(basis, y) / dot(basis, basis)
        rss = sum(abs2, y .- amplitude .* basis)
        rss < best.rss &&
            (best = (rss = rss, amplitude = amplitude, exponent = exponent))
    end
    scale = max(sum(abs2, y), floatmin(Float64))
    n = length(y)
    aic_constant = n * log(max(rss_constant / scale, eps(Float64))) + 2
    aic_power = n * log(max(best.rss / scale, eps(Float64))) + 4
    winner = aic_power < aic_constant ? "power" : "constant"
    return (winner = winner, rss_constant = rss_constant,
            rss_power = best.rss, aic_constant = aic_constant,
            aic_power = aic_power, constant = constant,
            amplitude = best.amplitude, exponent = best.exponent)
end

_complex_dict(z) = Dict("real" => real(z), "imag" => imag(z))

function _row(model, beta, candidate, observable, states, mode, convergence)
    metrics = ward_metrics(candidate, observable, states, mode, beta)
    return Dict(
        "Nm" => model.Nm,
        "betaJ" => Float64(beta * model.J),
        "seed" => model.seed,
        "mode" => mode,
        "candidate" => candidate.family,
        "width_cycles" => candidate.width_cycles,
        "quadrature_steps" => candidate.steps,
        "observable" => observable.label,
        "u" => observable.u,
        "v" => observable.v,
        "heat_delta" => observable.delta,
        "relative_defect" => metrics.relative_defect,
        "action_relative_defect" => metrics.action_relative_defect,
        "matrix_residual_norm" => metrics.matrix_residual_norm,
        "residual_norm" => metrics.residual_norm,
        "target_action_norm" => metrics.target_action_norm,
        "actual_action_norm" => metrics.actual_action_norm,
        "actual_matrix_elements" => _complex_dict.(metrics.actual_matrix_elements),
        "target_matrix_elements" => _complex_dict.(metrics.target_matrix_elements),
        "maximum_imaginary_part" => metrics.maximum_imaginary_part,
        "hermiticity_error" => hermiticity_error(candidate),
        "parity_error" => parity_error(candidate, model),
        "quadrature" => Dict(
            "observed_order" => convergence.observed_order,
            "coarse_difference" => convergence.coarse_difference,
            "fine_difference" => convergence.fine_difference,
            "steps" => convergence.steps,
        ),
    )
end

function _exact_row(model, beta, observable, states)
    candidate = exact_hamiltonian_candidate(model)
    convergence = (observed_order = 2.0, coarse_difference = 0.0,
                   fine_difference = 0.0, steps = Int[])
    return _row(model, beta, candidate, observable, states, 0, convergence)
end

function _candidate_specs(model, beta, mode, steps; all_widths::Bool)
    specs = Tuple{CandidateOperator,NamedTuple}[]
    widths = all_widths ? (0.5, 1.0, 2.0) : (1.0,)
    step_tuple = (steps ÷ 4, steps ÷ 2, steps)
    for width in widths
        convergence = quadrature_convergence(model, beta, mode, :filtered;
            width_cycles = width, steps = step_tuple)
        candidate = frequency_filtered_candidate(model, beta, mode;
            width_cycles = width, steps = steps)
        push!(specs, (candidate, convergence))
    end
    convergence = quadrature_convergence(model, beta, mode, :ledger;
        width_cycles = 1.0, steps = step_tuple)
    candidate = ledger_candidate(model, beta, mode;
        width_cycles = 1.0, steps = steps)
    push!(specs, (candidate, convergence))
    return specs
end

function _fit_dict(fit)
    return Dict("winner" => fit.winner,
                "rss_constant" => fit.rss_constant,
                "rss_power" => fit.rss_power,
                "aic_constant" => fit.aic_constant,
                "aic_power" => fit.aic_power,
                "constant" => fit.constant,
                "amplitude" => fit.amplitude,
                "exponent" => fit.exponent)
end

function _campaign_fits(rows, Ns, betas)
    out = Any[]
    families = [
        ("frequency-filtered bilinear", 0.5),
        ("frequency-filtered bilinear", 1.0),
        ("frequency-filtered bilinear", 2.0),
        ("naive EFT ledger", 1.0),
    ]
    for beta in betas, (family, width) in families
        means, bands = Float64[], Any[]
        for N in Ns
            selected = filter(r -> r["Nm"] == N && r["betaJ"] == beta &&
                                   r["candidate"] == family &&
                                   r["width_cycles"] == width, rows)
            defects = Float64[r["relative_defect"] for r in selected]
            isempty(defects) && error("empty scaling cell")
            push!(means, mean(defects))
            push!(bands, Dict("Nm" => N, "count" => length(defects),
                              "mean" => mean(defects), "std" => std(defects),
                              "minimum" => minimum(defects),
                              "maximum" => maximum(defects)))
        end
        fit = scaling_comparison(Ns, means)
        # A three-size AIC preference with p close to zero is not evidence for
        # r_N -> 0, especially when the width scan reverses the preference.
        # Preserve the mechanical AIC winner and label the extrapolation
        # separately instead of promoting a shallow finite-size slope.
        verdict = fit.winner == "constant" ?
                  "saturating on accessible sizes" :
                  fit.exponent >= 0.5 ?
                  "power decay on accessible sizes; extrapolation unproved" :
                  "shallow-power AIC winner; no controlled r_N-to-zero evidence"
        push!(out, Dict("betaJ" => Float64(beta), "candidate" => family,
                        "width_cycles" => width, "bands" => bands,
                        "fit" => _fit_dict(fit), "verdict" => verdict))
    end
    return out
end

function run_campaign(; Ns = [8, 10, 12], betas = [5.0, 10.0],
                      seeds = [3101, 3102, 3103],
                      include_n14::Bool = true, steps::Int = 96)
    steps >= 32 && steps % 4 == 0 ||
        throw(ArgumentError("steps must be a multiple of four and >=32"))
    main_rows, n1_rows, n0_rows = Any[], Any[], Any[]
    for N in Ns, seed in seeds
        model = build_syk(N; J = 1.0, seed = seed)
        for beta in betas
            tfd = prepare_tfd(model, beta)
            observables = campaign_observables(model, beta; delta = HEAT_DELTA)
            states = tfd_sector_states(tfd, observables)
            append!(n0_rows, [_exact_row(model, beta, A, states) for A in observables])
            for (candidate, convergence) in
                    _candidate_specs(model, beta, 2, steps; all_widths = true)
                append!(main_rows, [_row(model, beta, candidate, A, states, 2,
                                         convergence) for A in observables])
            end
            for (candidate, convergence) in
                    _candidate_specs(model, beta, 1, steps; all_widths = false)
                append!(n1_rows, [_row(model, beta, candidate, A, states, 1,
                                       convergence) for A in observables])
            end
        end
    end

    n14 = Any[]
    if include_n14
        model = build_syk(14; J = 1.0, seed = first(seeds))
        beta = maximum(betas)
        tfd = prepare_tfd(model, beta)
        observables = campaign_observables(model, beta; delta = HEAT_DELTA)
        states = tfd_sector_states(tfd, observables)
        for (candidate, convergence) in
                _candidate_specs(model, beta, 2, steps; all_widths = false)
            append!(n14, [_row(model, beta, candidate, A, states, 2,
                               convergence) for A in observables])
        end
    end

    results = Dict(
        "schema_version" => 1,
        "conventions" => Dict(
            "majoranas" => "{chi_i,chi_j}=delta_ij; existing SYKED JW convention",
            "hamiltonian" => "q=4 SYK, variance 3!*J^2/Nm^3, J=1",
            "two_dot_action" => "H0*C=H*C+C*H; right coefficient multipliers reverse products",
            "thermal_modes" => "epsilon_n(t)=cos(2*pi*n*t/beta), real oscillatory Lorentzian convention",
            "endpoint_dimension" => ENDPOINT_DIMENSION,
            "heat_kernel" => "exp[-delta*(H-E0)] on both sides of each insertion",
            "heat_delta" => HEAT_DELTA,
            "state_family" => "TFD plus two normalized one-bilocal insertion vectors",
            "relative_defect" => "Frobenius norm of the projected 3x3 Ward-matrix residual divided by max(target-matrix norm, candidate-matrix norm)",
            "fit" => "constant (k=1) versus a*Nm^(-p) (k=2), AIC=n*log(RSS/sum(y^2))+2k",
        ),
        "candidate_definitions" => Dict(
            "frequency-filtered bilinear" =>
                "normalized Gaussian-window quadrature of cos(omega_n*t)*A2(t); A2 is SYKED's fixed norm-one random even Hermitian bilinear",
            "naive EFT ledger" =>
                "normalized Gaussian-window quadrature of epsilon_n(t)*H + (i/2)*epsilon_n'(t)*[H,A2(t)]",
            "window" => "sigma=width_cycles*beta/(2*pi), truncated at |t|=4sigma; composite trapezoid",
        ),
        "observables" => [Dict("label" => A.label, "u_over_beta" => A.u / 5.0,
                                "v_over_beta" => A.v / 5.0)
                          for A in campaign_observables(build_syk(8; seed = 1), 5.0)],
        "main_grid" => Dict("Nm" => collect(Ns), "betaJ" => collect(betas),
                            "seeds" => collect(seeds)),
        "main_rows" => main_rows,
        "n1_control_rows" => n1_rows,
        "n0_control" => Dict(
            "threshold" => EXACT_GATE,
            "maximum_relative_defect" => maximum(r["relative_defect"] for r in n0_rows),
            "rows" => n0_rows,
        ),
        "fits" => _campaign_fits(main_rows, Ns, betas),
        "n14_confirmation" => n14,
    )
    validate_results(results)
    return results
end

function _all_finite(x)
    x isa AbstractFloat && return isfinite(x)
    x isa Number && return true
    x isa AbstractDict && return all(_all_finite(k) && _all_finite(v)
                                     for (k, v) in x)
    x isa AbstractArray && return all(_all_finite, x)
    return true
end

function validation_fixture()
    row = Dict(
        "relative_defect" => 0.8,
        "actual_matrix_elements" => [Dict("real" => 0.1, "imag" => 0.0)],
        "target_matrix_elements" => [Dict("real" => 0.2, "imag" => 0.0)],
        "hermiticity_error" => 1.0e-14,
        "parity_error" => 1.0e-14,
        "quadrature" => Dict("observed_order" => 2.0),
    )
    control = deepcopy(row)
    control["relative_defect"] = 1.0e-14
    return Dict(
        "main_rows" => [row],
        "n1_control_rows" => [deepcopy(row)],
        "n0_control" => Dict("threshold" => EXACT_GATE,
                             "maximum_relative_defect" => 1.0e-14,
                             "rows" => [control]),
        "fits" => [Dict("fit" => Dict("winner" => "constant"))],
    )
end

function poisoned_result(mode::Symbol)
    out = deepcopy(validation_fixture())
    mode == :nan && (out["main_rows"][1]["relative_defect"] = NaN)
    mode == :empty && (out["main_rows"] = Any[])
    mode == :calibration && (out["n0_control"]["maximum_relative_defect"] = 1.0e-4)
    mode == :hermiticity && (out["main_rows"][1]["hermiticity_error"] = 1.0e-4)
    mode == :parity && (out["main_rows"][1]["parity_error"] = 1.0e-4)
    mode == :order && (out["main_rows"][1]["quadrature"]["observed_order"] = 1.0)
    return out
end

function validate_results(results)
    _all_finite(results) || throw(ResultValidationError("non-finite result"))
    main = get(results, "main_rows", Any[])
    isempty(main) && throw(ResultValidationError("empty Ward campaign"))
    controls = get(get(results, "n0_control", Dict()), "rows", Any[])
    isempty(controls) && throw(ResultValidationError("empty n=0 calibration"))
    maximum_defect = get(results["n0_control"], "maximum_relative_defect", Inf)
    threshold = get(results["n0_control"], "threshold", EXACT_GATE)
    maximum_defect < threshold ||
        throw(ResultValidationError("n=0 exactness gate violated"))
    rows = vcat(main, get(results, "n1_control_rows", Any[]), controls,
                get(results, "n14_confirmation", Any[]))
    for row in rows
        row["relative_defect"] >= 0 ||
            throw(ResultValidationError("negative relative defect"))
        isempty(get(row, "actual_matrix_elements", Any[])) &&
            throw(ResultValidationError("empty matrix-element sample"))
        isempty(get(row, "target_matrix_elements", Any[])) &&
            throw(ResultValidationError("empty target sample"))
        row["hermiticity_error"] < EXACT_GATE ||
            throw(ResultValidationError("hermiticity gate violated"))
        row["parity_error"] < EXACT_GATE ||
            throw(ResultValidationError("parity gate violated"))
        row["quadrature"]["observed_order"] >= QUADRATURE_ORDER_FLOOR ||
            throw(ResultValidationError("quadrature order gate violated"))
    end
    isempty(get(results, "fits", Any[])) &&
        throw(ResultValidationError("empty scaling fits"))
    return true
end

function write_results(path::AbstractString, results)
    validate_results(results)
    open(path, "w") do io
        JSON.print(io, results, 2)
        println(io)
    end
    return path
end

end # module
