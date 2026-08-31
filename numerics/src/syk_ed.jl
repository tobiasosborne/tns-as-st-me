"""
Finite-N exact diagonalization for two identical q=4 SYK dots.

The convention is {chi_i,chi_j}=delta_ij,
H=i^(q/2) sum J_ijkl chi_i chi_j chi_k chi_l, and
E[J_ijkl^2]=3! J^2/Nm^3; the two-dot dimension is 2^Nm.
This standalone module intentionally is not included in TriangleMPS.
"""
module SYKED

using LinearAlgebra
using Random
using Statistics
using JSON
export SYKModel, TFDData, PulseProfile, ResultValidationError,
       build_syk, zero_model, bilinear_operator, prepare_tfd,
       thermal_expectation, expect_left, expect_right,
       reference_coefficient, pulsed_coefficient, reference_observables,
       detector_stats, detector_series, profile_integral, pulse_unitary,
       relative_energy_change, tune_balanced_pulse, integrator_convergence,
       model_comparison, validation_fixture, poisoned_result,
       validate_results, write_results, run_campaign
struct SYKModel
    Nm::Int
    J::Float64
    seed::Int
    coupling_variance::Float64
    majoranas::Vector{Matrix{ComplexF64}}
    parity::Matrix{ComplexF64}
    H::Matrix{ComplexF64}
    pulse_operator::Matrix{ComplexF64}
    energies::Vector{Float64}
    eigenvectors::Matrix{ComplexF64}
end
struct TFDData
    beta::Float64
    rho::Matrix{ComplexF64}
    coefficient::Matrix{ComplexF64}
    energy_relation_residual::Float64
end

struct PulseProfile
    kind::Symbol
    start::Float64
    stop::Float64
    center::Float64
    width::Float64
    amplitude::Float64
end

struct ResultValidationError <: Exception
    message::String
end
Base.showerror(io::IO, e::ResultValidationError) = print(io, e.message)

function _gamma_action(index::Int, basis::Int)
    mode = (index + 1) ÷ 2
    bit = (basis >> (mode - 1)) & 1
    mask = (1 << (mode - 1)) - 1
    z = isodd(count_ones(basis & mask)) ? -1.0 : 1.0
    phase = isodd(index) ? complex(z) : z * (bit == 0 ? im : -im)
    return xor(basis, 1 << (mode - 1)), phase
end

function _gamma_matrix(index::Int, Nm::Int)
    d = 1 << (Nm ÷ 2)
    G = zeros(ComplexF64, d, d)
    for basis in 0:d-1
        out, phase = _gamma_action(index, basis)
        G[out + 1, basis + 1] = phase
    end
    return G
end

function _monomial_action(indices, basis::Int)
    out, phase = basis, 1.0 + 0.0im
    for index in reverse(indices)
        out, p = _gamma_action(index, out)
        phase *= p
    end
    return out, phase
end

function _spectral_model(Nm::Int, J::Real, seed::Int, H, O, gammas, parity,
                         coupling_variance::Real)
    Hh = Matrix{ComplexF64}(Hermitian((H + H') / 2))
    Oh = Matrix{ComplexF64}(Hermitian((O + O') / 2))
    F = eigen(Hermitian(Hh))
    return SYKModel(Nm, Float64(J), seed, Float64(coupling_variance), gammas,
                    parity, Hh, Oh, F.values, F.vectors)
end

"""Construct one q=4 dot and one fixed, norm-one random even bilinear."""
function build_syk(Nm::Int; J::Real = 1.0, seed::Int = 1701)
    Nm >= 4 && iseven(Nm) || throw(ArgumentError("Nm must be even and >=4"))
    d = 1 << (Nm ÷ 2)
    gammas = [_gamma_matrix(i, Nm) / sqrt(2) for i in 1:Nm]
    parity = zeros(ComplexF64, d, d)
    for b in 0:d-1
        parity[b + 1, b + 1] = isodd(count_ones(b)) ? -1 : 1
    end
    variance = 6 * Float64(J)^2 / Nm^3
    rng = MersenneTwister(seed)
    H = zeros(ComplexF64, d, d)
    for i in 1:Nm-3, j in i+1:Nm-2, k in j+1:Nm-1, l in k+1:Nm
        coupling = sqrt(variance) * randn(rng)
        for basis in 0:d-1
            out, phase = _monomial_action((i, j, k, l), basis)
            H[out + 1, basis + 1] += -coupling * phase / 4
        end
    end
    orng = MersenneTwister(seed + 10_000_019)
    O = zeros(ComplexF64, d, d)
    for i in 1:Nm-1, j in i+1:Nm
        coefficient = randn(orng)
        for basis in 0:d-1
            out, phase = _monomial_action((i, j), basis)
            O[out + 1, basis + 1] += im * coefficient * phase / 2
        end
    end
    O ./= opnorm(Hermitian(O))
    return _spectral_model(Nm, J, seed, H, O, gammas, parity, variance)
end

"""Exactly free dot, used for the analytic fermionic-TFD check."""
function zero_model(Nm::Int)
    iseven(Nm) || throw(ArgumentError("Nm must be even"))
    d = 1 << (Nm ÷ 2)
    gammas = [_gamma_matrix(i, Nm) / sqrt(2) for i in 1:Nm]
    parity = Diagonal(ComplexF64[isodd(count_ones(b)) ? -1 : 1 for b in 0:d-1]) |> Matrix
    H = zeros(ComplexF64, d, d)
    O = im * gammas[1] * gammas[2]
    O ./= opnorm(O)
    return _spectral_model(Nm, 1.0, 0, H, O, gammas, parity, 0.0)
end

bilinear_operator(model::SYKModel, i::Int, j::Int) =
    im * model.majoranas[i] * model.majoranas[j]

"""
Fermionic TFD convention Theta=exp(i*pi*P/4)K.  The parity twist is the
Klein phase which makes -i chi_i^L chi_i^R a nonzero even detector.  We use
H_R=conj(H), so (H_L-H_R)|TFD>=0 exactly.
"""
function prepare_tfd(model::SYKModel, beta::Real)
    beta >= 0 || throw(ArgumentError("beta must be nonnegative"))
    shifted = model.energies .- minimum(model.energies)
    weights = exp.(-Float64(beta) .* shifted)
    probabilities = weights / sum(weights)
    V = model.eigenvectors
    rho = V * Diagonal(probabilities) * V'
    rhohalf = V * Diagonal(sqrt.(probabilities)) * V'
    S = cos(pi / 4) * I + im * sin(pi / 4) * model.parity
    C = Matrix{ComplexF64}(rhohalf * S)
    residual = norm(model.H * C - C * model.H, Inf)
    return TFDData(Float64(beta), rho, C, residual)
end

thermal_expectation(tfd::TFDData, A) = tr(tfd.rho * A)
expect_left(C, A) = tr(C' * A * C)
expect_right(C, A) = tr(C' * C * A)

_unitary(values, vectors, time) =
    vectors * Diagonal(cis.(-values .* time)) * vectors'
_left_free(model, time) = _unitary(model.energies, model.eigenvectors, time)
_right_free(model, time) =
    _unitary(model.energies, conj(model.eigenvectors), time)

function reference_coefficient(model::SYKModel, tfd::TFDData, T::Real)
    T >= 0 || throw(ArgumentError("time must be nonnegative"))
    return _left_free(model, T) * tfd.coefficient * transpose(_right_free(model, T))
end

function pulsed_coefficient(model::SYKModel, tfd::TFDData, Uright, T::Real)
    T >= 1 || throw(ArgumentError("detector time must follow pulse support"))
    Ur = _right_free(model, T - 1) * Uright
    return _left_free(model, T) * tfd.coefficient * transpose(Ur)
end

function reference_observables(model::SYKModel, tfd::TFDData, T::Real)
    C = reference_coefficient(model, tfd, T)
    return (energy_left = real(expect_left(C, model.H)),
            energy_right = real(expect_right(C, model.H)),
            total_parity = real(tr(C' * model.parity * C * model.parity)))
end

function (p::PulseProfile)(t::Real)
    p.start <= t <= p.stop || return 0.0
    x = (t - p.center) / p.width
    shape = p.kind == :derivative_gaussian ? x * exp(-x^2 / 2) :
            p.kind == :gaussian ? exp(-x^2 / 2) :
            throw(ArgumentError("unknown pulse kind $(p.kind)"))
    return p.amplitude * shape
end

function profile_integral(p::PulseProfile; n::Int = 2000)
    h = (p.stop - p.start) / n
    return h * (sum(p(p.start + k * h) for k in 1:n-1) +
                (p(p.start) + p(p.stop)) / 2)
end

"""Unitary, midpoint Strang integrator for H_R+f(t)O_R (global order two)."""
function pulse_unitary(model::SYKModel, p::PulseProfile; dt::Real = 0.01)
    duration = p.stop - p.start
    n = ceil(Int, duration / dt)
    h = duration / n
    VR = conj(model.eigenvectors)
    Ehalf = _unitary(model.energies, VR, h / 2)
    FO = eigen(Hermitian(conj(model.pulse_operator)))
    U = Matrix{ComplexF64}(I, size(model.H)...)
    for step in 1:n
        tm = p.start + (step - 0.5) * h
        Esource = _unitary(FO.values, FO.vectors, p(tm) * h)
        U = Ehalf * Esource * Ehalf * U
    end
    return U
end

function relative_energy_change(model::SYKModel, tfd::TFDData, Uright)
    rhoR = transpose(tfd.coefficient' * tfd.coefficient)
    HR = conj(model.H)
    before = real(tr(rhoR * HR))
    after = real(tr(Uright * rhoR * Uright' * HR))
    return abs(after - before) / max(abs(before), eps(Float64))
end

function tune_balanced_pulse(model::SYKModel, tfds; dt::Real = 0.01)
    amplitude = 0.1
    for attempt in 1:30
        p = PulseProfile(:derivative_gaussian, 0.0, 1.0, 0.5, 0.12, amplitude)
        U = pulse_unitary(model, p; dt = dt)
        changes = [relative_energy_change(model, tfd, U) for tfd in tfds]
        maximum(changes) < 8.0e-7 &&
            return p, (maximum_relative_energy_change = maximum(changes),
                       attempts = attempt, per_beta = changes)
        amplitude /= 2
    end
    error("could not tune a nonzero pulse through the energy gate")
end

function integrator_convergence(model::SYKModel, profile::PulseProfile)
    U1 = pulse_unitary(model, profile; dt = 0.04)
    U2 = pulse_unitary(model, profile; dt = 0.02)
    U3 = pulse_unitary(model, profile; dt = 0.01)
    coarse, fine = norm(U1 - U2, Inf), norm(U2 - U3, Inf)
    order = log2(coarse / fine)
    ident = Matrix{ComplexF64}(I, size(model.H)...)
    unitary_error = maximum(norm(U' * U - ident, Inf) for U in (U1, U2, U3))
    return (observed_order = order, coarse_difference = coarse,
            fine_difference = fine, maximum_unitarity_error = unitary_error)
end

function _detector_action(model::SYKModel, C)
    out = zeros(ComplexF64, size(C))
    for chi in model.majoranas
        out .+= -im .* (chi * model.parity) * C * chi
    end
    return out / model.Nm
end

"""Mean and exact pure-state variance of the Hermitian -i G_LR detector."""
function detector_stats(model::SYKModel, C)
    DC = _detector_action(model, C)
    mean_value = real(dot(C, DC))
    variance = max(0.0, real(dot(DC, DC)) - mean_value^2)
    return (mean = mean_value, variance = variance)
end

function _reference_derivative(model::SYKModel, C)
    Cdot = -im .* (model.H * C + C * model.H)
    return 2 * real(dot(Cdot, _detector_action(model, C)))
end

function detector_series(model::SYKModel, tfd::TFDData, Uright,
                         times::AbstractVector; eta::Real = 0.1)
    isempty(times) && throw(ArgumentError("detector window is empty"))
    all(T -> T >= 1, times) || throw(ArgumentError("window overlaps pulse"))
    gp, ge, delta, derivative = Float64[], Float64[], Float64[], Float64[]
    vp, ve, shots = Float64[], Float64[], Float64[]
    for T in times
        Cp = pulsed_coefficient(model, tfd, Uright, T)
        Ce = reference_coefficient(model, tfd, T)
        sp, se = detector_stats(model, Cp), detector_stats(model, Ce)
        dg = sp.mean - se.mean
        slope = _reference_derivative(model, Ce)
        abs(slope) > 1.0e-14 || error("calibration derivative vanished at T=$T")
        push!(gp, sp.mean); push!(ge, se.mean); push!(delta, dg)
        push!(derivative, slope); push!(vp, sp.variance); push!(ve, se.variance)
        cost = (sp.variance + se.variance) /
               (eta^2 * max(abs2(dg), 1.0e-300))
        push!(shots, max(1.0, cost))
    end
    return (times = Float64.(times), g_pulse = gp, g_reference = ge,
            delta_signed = delta, delta_abs = abs.(delta),
            equilibrium_derivative = derivative,
            delta_u_rel = -delta ./ derivative,
            variance_pulse = vp, variance_reference = ve,
            shots_for_10pct_delta = shots)
end

"""Constant versus one-exponential least-squares comparison with AIC."""
function model_comparison(times::AbstractVector, values::AbstractVector)
    length(times) == length(values) > 2 || throw(ArgumentError("bad fit window"))
    y, tau = Float64.(values), Float64.(times) .- first(times)
    constant = mean(y)
    rssc = sum(abs2, y .- constant)
    best = (rss = Inf, amplitude = NaN, rate = NaN)
    for rate in exp.(range(log(1.0e-3), log(8.0); length = 1600))
        basis = exp.(-rate .* tau)
        amplitude = dot(basis, y) / dot(basis, basis)
        rss = sum(abs2, y .- amplitude .* basis)
        rss < best.rss && (best = (rss = rss, amplitude = amplitude, rate = rate))
    end
    scale = max(sum(abs2, y), floatmin(Float64))
    n = length(y)
    aicc = n * log(max(rssc / scale, eps(Float64))) + 2
    aice = n * log(max(best.rss / scale, eps(Float64))) + 4
    return (winner = aicc <= aice ? "constant" : "exponential",
            rss_constant = rssc, rss_exponential = best.rss,
            aic_constant = aicc, aic_exponential = aice,
            constant = constant, amplitude = best.amplitude,
            decay_rate = best.rate)
end

_fit_dict(f) = Dict("winner" => f.winner,
    "rss_constant" => f.rss_constant, "rss_exponential" => f.rss_exponential,
    "aic_constant" => f.aic_constant, "aic_exponential" => f.aic_exponential,
    "constant" => f.constant, "amplitude" => f.amplitude,
    "decay_rate" => f.decay_rate)

function _point(model, tfd, profile, Uright, Ucontrol, convergence, times)
    energy_change = relative_energy_change(model, tfd, Uright)
    energy_change < 1.0e-6 || error("balanced pulse failed energy gate")
    convergence.observed_order >= 1.75 || error("integrator order gate failed")
    series = detector_series(model, tfd, Uright, times)
    control = detector_series(model, tfd, Ucontrol, times)
    fit_g = model_comparison(times, series.delta_abs)
    fit_u = model_comparison(times, series.delta_u_rel)
    tail = (length(times) - 3):length(times)
    tail_u, tail_g = series.delta_u_rel[tail], series.delta_abs[tail]
    verdict = fit_g.winner == "exponential" && fit_u.winner == "constant" ?
              "echo" : fit_g.winner == "exponential" ? "partial_echo" : "conflict"
    Cp = pulsed_coefficient(model, tfd, Uright, times[2])
    Ce = reference_coefficient(model, tfd, times[2])
    left_blind = norm(Cp * Cp' - Ce * Ce', Inf)
    return Dict(
        "Nm" => model.Nm, "betaJ" => tfd.beta * model.J, "seed" => model.seed,
        "one_dot_dimension" => size(model.H, 1),
        "two_dot_dimension" => size(model.H, 1)^2,
        "pulse_amplitude" => profile.amplitude,
        "balanced_energy_gate" => Dict("relative_change" => energy_change,
                                        "threshold" => 1.0e-6),
        "integrator" => Dict("observed_order" => convergence.observed_order,
            "coarse_difference" => convergence.coarse_difference,
            "fine_difference" => convergence.fine_difference,
            "maximum_unitarity_error" => convergence.maximum_unitarity_error),
        "left_blindness_max" => left_blind, "times" => series.times,
        "g_reference" => series.g_reference, "g_pulse" => series.g_pulse,
        "delta_g_signed" => series.delta_signed,
        "delta_g_absolute" => series.delta_abs,
        "equilibrium_derivative" => series.equilibrium_derivative,
        "delta_u_rel" => series.delta_u_rel,
        "fluctuation_band" => Dict("delta_g_tail_mean" => mean(tail_g),
            "delta_g_tail_std" => std(tail_g), "delta_g_tail_min" => minimum(tail_g),
            "delta_g_tail_max" => maximum(tail_g), "delta_u_tail_mean" => mean(tail_u),
            "delta_u_tail_std" => std(tail_u), "delta_u_tail_min" => minimum(tail_u),
            "delta_u_tail_max" => maximum(tail_u)),
        "fits" => Dict("delta_g_absolute" => _fit_dict(fit_g),
                         "delta_u_rel" => _fit_dict(fit_u)),
        "q1_verdict" => verdict,
        "estimator" => Dict("eta" => 0.1,
            "variance_pulse" => series.variance_pulse,
            "variance_reference" => series.variance_reference,
            "shots_for_relative_error_in_delta_g" => series.shots_for_10pct_delta),
        "unbalanced_control" => Dict("scope" => "formal diagnostic only",
            "relative_energy_change" => relative_energy_change(model, tfd, Ucontrol),
            "delta_g_absolute" => control.delta_abs,
            "delta_u_rel" => control.delta_u_rel))
end

function _self_averaging(points, Ns, betas)
    out = Any[]
    for N in Ns, beta in betas
        rows = filter(r -> r["Nm"] == N && r["betaJ"] == beta, points)
        plateaus = [r["fluctuation_band"]["delta_u_tail_mean"] for r in rows]
        magnitudes = abs.(plateaus)
        verdicts = [r["q1_verdict"] for r in rows]
        push!(out, Dict("Nm" => N, "betaJ" => beta,
            "seeds" => [r["seed"] for r in rows], "verdicts" => verdicts,
            "verdict_stable" => length(unique(verdicts)) == 1,
            "plateau_mean" => mean(plateaus), "plateau_std" => std(plateaus),
            "magnitude_mean" => mean(magnitudes), "magnitude_std" => std(magnitudes),
            "worst_case_magnitude" => maximum(magnitudes),
            "exponential_delta_g_fraction" =>
                mean(r["fits"]["delta_g_absolute"]["winner"] == "exponential"
                     for r in rows)))
    end
    return out
end

function run_campaign(; Ns = [8, 10, 12], betas = [5.0, 10.0],
                      seeds = [1701, 1702, 1703, 1704, 1705],
                      include_n14::Bool = true, dt::Real = 0.01)
    times = collect(1.5:0.5:5.0)
    points = Any[]
    for N in Ns, seed in seeds
        model = build_syk(N; J = 1.0, seed = seed)
        tfds = [prepare_tfd(model, beta) for beta in betas]
        profile, _ = tune_balanced_pulse(model, tfds; dt = dt)
        convergence = integrator_convergence(model, profile)
        Uright = pulse_unitary(model, profile; dt = dt)
        control = PulseProfile(:gaussian, 0.0, 1.0, 0.5, 0.12,
                               profile.amplitude)
        Ucontrol = pulse_unitary(model, control; dt = dt)
        for tfd in tfds
            push!(points, _point(model, tfd, profile, Uright, Ucontrol,
                                 convergence, times))
        end
    end
    confirmation = Any[]
    if include_n14
        model = build_syk(14; J = 1.0, seed = first(seeds))
        tfd = prepare_tfd(model, maximum(betas))
        profile, _ = tune_balanced_pulse(model, [tfd]; dt = dt)
        convergence = integrator_convergence(model, profile)
        Uright = pulse_unitary(model, profile; dt = dt)
        control = PulseProfile(:gaussian, 0.0, 1.0, 0.5, 0.12, profile.amplitude)
        push!(confirmation, _point(model, tfd, profile, Uright,
              pulse_unitary(model, control; dt = dt), convergence, times))
    end
    results = Dict(
        "schema_version" => 1,
        "conventions" => Dict(
            "majoranas" => "{chi_i,chi_j}=delta_ij; JW Clifford on Nm/2 qubits per dot",
            "hamiltonian" => "H=i^(q/2) sum J_ijkl chi_i chi_j chi_k chi_l, q=4",
            "couplings" => "mean zero, variance 3!*J^2/Nm^3, J=1",
            "right_dot" => "same realization; H_R=conj(H_L)",
            "theta" => "Theta=exp(i*pi*P/4)K",
            "detector" => "reported real G_LR=-i/Nm sum <chi_i^L chi_i^R>",
            "pulse_operator" => "fixed seed-derived random Hermitian bilinear, operator norm one",
            "synchronization" => "single u_*=1 at pulse end; no later resynchronization", "window" => "T in [1.5,5] J^-1 after support [0,1]; short diagnostic, recurrences not excluded",
            "limit_scope" => "no finite-N permanence claim; compare only structurally to large-C-first EFT"),
        "main_grid" => Dict("Nm" => collect(Ns), "betaJ" => collect(betas),
                            "seeds" => collect(seeds)),
        "late_time_grid" => times, "parameter_points" => points,
        "self_averaging" => _self_averaging(points, Ns, betas),
        "n14_confirmation" => confirmation)
    validate_results(results)
    return results
end

function _all_finite(x)
    x isa AbstractFloat && return isfinite(x)
    x isa Number && return true
    x isa AbstractDict && return all(_all_finite(k) && _all_finite(v) for (k, v) in x)
    x isa AbstractArray && return all(_all_finite, x)
    return true
end
function validation_fixture()
    row = Dict("times" => [1.5, 2.0, 2.5],
        "balanced_energy_gate" => Dict("relative_change" => 1.0e-8,
                                        "threshold" => 1.0e-6),
        "integrator" => Dict("observed_order" => 2.0))
    return Dict("parameter_points" => [row], "late_time_grid" => row["times"])
end
function poisoned_result(mode::Symbol)
    out = deepcopy(validation_fixture())
    mode == :nan && (out["parameter_points"][1]["x"] = NaN)
    mode == :empty_window && (out["parameter_points"][1]["times"] = Float64[])
    mode == :energy_gate &&
        (out["parameter_points"][1]["balanced_energy_gate"]["relative_change"] = 2.0e-6)
    mode == :order_gate &&
        (out["parameter_points"][1]["integrator"]["observed_order"] = 1.2)
    return out
end
function validate_results(results)
    _all_finite(results) || throw(ResultValidationError("non-finite result"))
    points = get(results, "parameter_points", Any[])
    isempty(points) && throw(ResultValidationError("empty campaign"))
    for row in points
        isempty(get(row, "times", Any[])) && throw(ResultValidationError("empty window"))
        gate = row["balanced_energy_gate"]
        gate["relative_change"] < gate["threshold"] ||
            throw(ResultValidationError("balanced-energy gate violated"))
        row["integrator"]["observed_order"] >= 1.75 ||
            throw(ResultValidationError("integrator order gate violated"))
    end
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
