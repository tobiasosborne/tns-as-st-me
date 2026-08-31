"""
    SchwarzianMemory

Dependency-light RK4 computation for the sourced Schwarzian equation

    C * d/du Sch(t,u) / t'(u) = -t'(u) * T_tz(u),

quoted in `GravityReparametrizationsRevised.tex:611-623`.  The Schwarzian
definition is at lines 490-496, the charges at 889-900, and the dressed
bilocal rule at 645-675.  This module is standalone and deliberately is not
included in the shared `TriangleMPS` module.
"""
module SchwarzianMemory

using LinearAlgebra
using Statistics
using JSON

export AbstractPulse, ZeroPulse, TopHatPulse, GaussianPulse,
       DerivativeGaussianPulse, Trajectory, ResultValidationError,
       thermal_tan_state, integrate_fixed, schwarzian, sl2_charges,
       simulate_pulse, normalize_sl2, relative_element, observable_series,
       compare_models, dc_identity, validation_fixture, poisoned_result,
       validate_results, write_results, run_campaign

const SUPPORT = (0.0, 0.5)
const CENTER = 0.25
const WIDTH = 0.05
const LATE_GRID = [2.0, 5.0, 10.0, 20.0, 40.0]

abstract type AbstractPulse end
struct ZeroPulse <: AbstractPulse end
struct TopHatPulse <: AbstractPulse
    epsilon::Float64
end
struct GaussianPulse <: AbstractPulse
    epsilon::Float64
end
struct DerivativeGaussianPulse <: AbstractPulse
    epsilon::Float64
end

(::ZeroPulse)(u::Real) = 0.0
(p::TopHatPulse)(u::Real) = SUPPORT[1] <= u <= SUPPORT[2] ? p.epsilon : 0.0
function (p::GaussianPulse)(u::Real)
    SUPPORT[1] <= u <= SUPPORT[2] || return 0.0
    return p.epsilon * exp(-0.5 * ((u - CENTER) / WIDTH)^2)
end
function (p::DerivativeGaussianPulse)(u::Real)
    SUPPORT[1] <= u <= SUPPORT[2] || return 0.0
    x = (u - CENTER) / WIDTH
    # `x*exp(-x^2/2)` has zero coordinate area.  The extra thermal redshift
    # exp(-2(u-u_c)) makes t'_thermal^2*T odd as well, so the ADM-energy flux
    # is balanced on the prescribed exp(u) Lorentzian saddle.
    return p.epsilon * x * exp(-0.5 * x^2 - 2 * (u - CENTER))
end

struct Trajectory
    u::Vector{Float64}
    y::Matrix{Float64}                 # columns are (t,t',t'',t''')
end

"""Exact regular-chart data for `t(u)=tan(u/2)`, with beta=2pi."""
function thermal_tan_state(u::Real)
    t = tan(u / 2)
    v = (1 + t^2) / 2
    a = t * v
    j = (1 + t^2) * (1 + 3t^2) / 4
    return [t, v, a, j]
end

thermal_exp_state(u::Real, k::Real = 1.0) = begin
    t = exp(k * u)
    [t, k * t, k^2 * t, k^3 * t]
end

"""Schwarzian from the four-component state (source lines 490-496)."""
function schwarzian(y::AbstractVector)
    _, v, a, j = y
    v > 0 || throw(DomainError(v, "t' must remain positive"))
    return j / v - 1.5 * (a / v)^2
end

"""First-order form of source equation T.1 (source lines 611-623)."""
function _rhs(y::AbstractVector, u::Real, C::Real, pulse::AbstractPulse)
    t, v, a, j = y
    v > 0 || throw(DomainError(v, "projective trajectory lost monotonicity"))
    fourth = 4a * j / v - 3a^3 / v^2 - v^3 * pulse(u) / C
    return [v, a, j, fourth]
end

function _rk4_step(y::AbstractVector, u::Real, h::Real, C::Real,
                   pulse::AbstractPulse)
    k1 = _rhs(y, u, C, pulse)
    k2 = _rhs(y .+ (h / 2) .* k1, u + h / 2, C, pulse)
    k3 = _rhs(y .+ (h / 2) .* k2, u + h / 2, C, pulse)
    k4 = _rhs(y .+ h .* k3, u + h, C, pulse)
    return y .+ (h / 6) .* (k1 .+ 2 .* k2 .+ 2 .* k3 .+ k4)
end

"""Fixed-step classical RK4, with the last step adjusted to hit `u1`."""
function integrate_fixed(y0::AbstractVector, u0::Real, u1::Real, hmax::Real,
                         C::Real, pulse::AbstractPulse)
    u1 > u0 || throw(ArgumentError("integration interval must be nonempty"))
    hmax > 0 || throw(ArgumentError("step must be positive"))
    n = ceil(Int, (u1 - u0) / hmax)
    h = (u1 - u0) / n
    us = collect(range(Float64(u0), Float64(u1); length = n + 1))
    ys = Matrix{Float64}(undef, 4, n + 1)
    ys[:, 1] = y0
    for i in 1:n
        ys[:, i + 1] = _rk4_step(view(ys, :, i), us[i], h, C, pulse)
        all(isfinite, view(ys, :, i + 1)) || error("non-finite RK4 state")
    end
    return Trajectory(us, ys)
end

"""The three charges in source lines 889-900, in order (-,0,+)."""
function sl2_charges(y::AbstractVector, C::Real)
    t, v, a, j = y
    qm = C * (j / v^2 - a^2 / v^3)
    q0 = C * (t * j / v^2 - t * a^2 / v^3 - a / v)
    qp = C * (t^2 * j / v^2 - t^2 * a^2 / v^3 - 2t * a / v + 2v)
    return [qm, q0, qp]
end

function _charge_drift(tr::Trajectory, C::Real)
    q0 = sl2_charges(view(tr.y, :, 1), C)
    return maximum(norm(sl2_charges(view(tr.y, :, i), C) - q0, Inf)
                   for i in axes(tr.y, 2))
end

function _flux(tr::Trajectory, pulse::AbstractPulse)
    n = length(tr.u)
    vals = Matrix{Float64}(undef, 3, n)
    for i in 1:n
        t, v = tr.y[1, i], tr.y[2, i]
        vals[:, i] = v * pulse(tr.u[i]) .* [1.0, t, t^2]
    end
    out = zeros(3)
    for i in 1:n-1
        out .+= (tr.u[i + 1] - tr.u[i]) .* (vals[:, i] .+ vals[:, i + 1]) ./ 2
    end
    return out
end

"""Normalize a real projective matrix to determinant one."""
function normalize_sl2(M::AbstractMatrix)
    size(M) == (2, 2) || throw(ArgumentError("expected 2x2 matrix"))
    d = det(M)
    d > 0 || throw(DomainError(d, "orientation-preserving matrix required"))
    A = Matrix{Float64}(M) / sqrt(d)
    tr(A) < 0 && (A .*= -1)
    return A
end

function _fit_mobius(tr::Trajectory, k::Real)
    n = length(tr.u)
    A = Matrix{Float64}(undef, n, 4)
    for i in 1:n
        x, t = exp(k * tr.u[i]), tr.y[1, i]
        A[i, :] = [x, 1.0, -t * x, -t]
    end
    F = svd(A)
    z = F.V[:, end]
    M = normalize_sl2([z[1] z[2]; z[3] z[4]])
    predicted = [(M[1, 1] * exp(k * u) + M[1, 2]) /
                 (M[2, 1] * exp(k * u) + M[2, 2]) for u in tr.u]
    residual = maximum(abs.(predicted .- vec(tr.y[1, :])))
    return M, residual
end

"""Integrate pre-pulse, pulse, and post-pulse pieces without straddling jumps."""
function simulate_pulse(C::Real, pulse::AbstractPulse; h::Real = 5e-4)
    pre = integrate_fixed(thermal_exp_state(-0.5), -0.5, 0.0, h, C, ZeroPulse())
    active = integrate_fixed(pre.y[:, end], 0.0, 0.5, h, C, pulse)
    post = integrate_fixed(active.y[:, end], 0.5, 1.25, h, C, ZeroPulse())
    qbefore = sl2_charges(active.y[:, 1], C)
    qafter = sl2_charges(active.y[:, end], C)
    Sfinal = schwarzian(active.y[:, end])
    Sfinal < 0 || error("post-pulse solution is not on the Lorentzian thermal orbit")
    kfinal = sqrt(-2Sfinal)
    M, residual = _fit_mobius(post, kfinal)
    return (C = Float64(C), source = pulse, pre = pre, pulse_segment = active,
            pulse = active, post = post, charge_before = qbefore,
            charge_after = qafter, flux = _flux(active, pulse),
            pre_charge_drift = _charge_drift(pre, C),
            post_charge_drift = _charge_drift(post, C),
            final_schwarzian = Sfinal, final_energy = -C * Sfinal,
            energy_change = -C * (Sfinal + 0.5), k_final = kfinal,
            mobius = M, mobius_fit_residual = residual)
end

relative_element(ML::AbstractMatrix, MR::AbstractMatrix) = inv(ML) * MR

_mobius(M, x) = (M[1, 1] * x + M[1, 2]) / (M[2, 1] * x + M[2, 2])
_mobius_derivative(M, x, xp) = det(M) * xp / (M[2, 1] * x + M[2, 2])^2

"""Lorentzian two-sided continuation of the dressed kernel, lines 645-675."""
function _bilocal(ML, MR, kL::Real, kR::Real, T::Real; Delta::Real = 0.5)
    xL, xR = -exp(-kL * T), exp(kR * T)
    dxL, dxR = -kL * xL, kR * xR
    tL, tR = _mobius(ML, xL), _mobius(MR, xR)
    dtL = _mobius_derivative(ML, xL, dxL)
    dtR = _mobius_derivative(MR, xR, dxR)
    kernel = abs(dtL * dtR) / abs2(tL - tR)
    kernel >= 0 && isfinite(kernel) || error("invalid dressed bilocal")
    return kernel^Delta
end

function observable_series(ML::AbstractMatrix, MR::AbstractMatrix,
                           kL::Real, kR::Real, times::AbstractVector;
                           Delta::Real = 0.5)
    isempty(times) && throw(ArgumentError("late-time sample set is empty"))
    Delta > 0 && isfinite(Delta) || throw(ArgumentError("Delta must be finite and positive"))
    gp = [_bilocal(ML, MR, kL, kR, T; Delta = Delta) for T in times]
    ge = [_bilocal(ML, ML, kL, kR, T; Delta = Delta) for T in times]
    dg = gp .- ge
    du = Vector{Float64}(undef, length(times))
    for (i, T) in enumerate(times)
        h = 1e-5
        dge = (_bilocal(ML, ML, kL, kR, T + h; Delta = Delta) -
               _bilocal(ML, ML, kL, kR, T - h; Delta = Delta)) / (2h)
        du[i] = -dg[i] / dge
    end
    return (pulse = gp, equilibrium = ge, delta_g = dg, delta_u = du)
end

function compare_models(times::AbstractVector, values::AbstractVector)
    length(times) == length(values) > 0 || throw(ArgumentError("bad fit samples"))
    y = Float64.(values)
    c = mean(y)
    rssc = sum(abs2, y .- c)
    tau = Float64.(times) .- first(times)
    best = (rss = Inf, amplitude = NaN, rate = NaN)
    for rate in exp.(range(log(1e-4), log(5.0); length = 2400))
        basis = exp.(-rate .* tau)
        amp = dot(basis, y) / dot(basis, basis)
        rss = sum(abs2, y .- amp .* basis)
        rss < best.rss && (best = (rss = rss, amplitude = amp, rate = rate))
    end
    scale = max(sum(abs2, y), floatmin(Float64))
    scorec = length(y) * log(max(rssc / scale, eps(Float64))) + 2
    scoree = length(y) * log(max(best.rss / scale, eps(Float64))) + 4
    winner = scorec <= scoree ? "constant" : "exponential"
    return (winner = winner, rss_constant = rssc, rss_exponential = best.rss,
            constant = c, amplitude = best.amplitude, decay_rate = best.rate,
            aic_constant = scorec, aic_exponential = scoree)
end

# Independent linear soft leg about t=exp(u): writing t=exp(u+epsilon),
# delta Sch = epsilon'''-epsilon', hence epsilon''''-epsilon''=-exp(2u)T/C.
function _linear_segment(z0, u0, u1, hmax, C, pulse)
    n = ceil(Int, (u1 - u0) / hmax)
    h = (u1 - u0) / n
    us = collect(range(u0, u1; length = n + 1))
    z = Matrix{Float64}(undef, 4, n + 1); z[:, 1] = z0
    f(q, u) = [q[2], q[3], q[4], q[3] - exp(2u) * pulse(u) / C]
    for i in 1:n
        q, u = view(z, :, i), us[i]
        k1 = f(q, u); k2 = f(q + h/2 * k1, u + h/2)
        k3 = f(q + h/2 * k2, u + h/2); k4 = f(q + h * k3, u + h)
        z[:, i + 1] = q + h/6 * (k1 + 2k2 + 2k3 + k4)
    end
    return us, z
end

function _linear_vertex_prediction(run; h = 5e-4, Delta = 0.5)
    _, zpre = _linear_segment(zeros(4), -0.5, 0.0, h, run.C, ZeroPulse())
    up, zp = _linear_segment(zpre[:, end], 0.0, 0.5, h, run.C, run.source)
    uo, zo = _linear_segment(zp[:, end], 0.5, 1.25, h, run.C, ZeroPulse())
    y = Matrix{Float64}(undef, 4, length(uo))
    for i in eachindex(uo)
        e, ep, epp, eppp = zo[:, i]; x = exp(uo[i])
        y[:, i] = x .* [1 + e, 1 + e + ep,
                        1 + e + 2ep + epp,
                        1 + e + 3ep + 3epp + eppp]
    end
    Slin = -0.5 + zo[4, end] - zo[2, end]
    klin = sqrt(-2Slin)
    Mlin, _ = _fit_mobius(Trajectory(Float64.(uo), y), klin)
    lambda = 1e-2
    Mvertex = normalize_sl2(Matrix{Float64}(I, 2, 2) + lambda *
                            (Mlin - Matrix{Float64}(I, 2, 2)))
    kvertex = 1 + lambda * (klin - 1)
    duvertex = observable_series(Matrix{Float64}(I, 2, 2), Mvertex,
                                 1.0, kvertex, [40.0]; Delta = Delta).delta_u[1] / lambda
    qlin = zeros(3)
    for i in 1:length(up)-1
        f(u) = exp(u) * run.source(u) .* [1.0, exp(u), exp(2u)]
        qlin += (up[i + 1] - up[i]) * (f(up[i]) + f(up[i + 1])) / 2
    end
    return duvertex * norm(run.flux) / norm(qlin)
end
"""Abel DFT with a fitted-Mobius tail, followed by an omega^2 intercept."""
function dc_identity(run, late_detector::Real; Delta::Real = 0.5)
    omegas, horizons = [0.2, 0.1, 0.05, 0.025], [20.0, 40.0, 80.0]
    charge_norm = norm(run.flux)
    charge_norm > 0 || error("DC normalization needs nonzero injected charge")
    isfinite(late_detector) && late_detector != 0 ||
        error("late detector comparison must be finite and nonzero")
    soft_prediction = _linear_vertex_prediction(run; Delta = Delta)
    ML = Matrix{Float64}(I, 2, 2)
    # This coefficient comes only from the independently fitted post-pulse
    # matrix: G_pulse/G_eq -> |det(M)/M_11^2|^Delta.
    asymptotic_ratio = abs(det(run.mobius) / run.mobius[1, 1]^2)^Delta
    fitted_tail = (asymptotic_ratio - 1) / (Delta * (1 + run.k_final))
    residues = Matrix{Float64}(undef, length(horizons), length(omegas))
    dt = 0.02
    for (ih, horizon) in enumerate(horizons)
        ts = collect(0.5:dt:horizon)
        response = observable_series(ML, run.mobius, 1.0, run.k_final, ts;
                                     Delta = Delta).delta_u
        for (iw, omega) in enumerate(omegas)
            s = im * omega - omega^2
            weights = exp.(s .* (ts .- 0.5))
            finite = dt * (sum(response .* weights) -
                     (response[1] * weights[1] + response[end] * weights[end]) / 2)
            tail = -fitted_tail * exp(s * (horizon - 0.5)) / s
            residues[ih, iw] = real(-im * omega * (finite + tail))
        end
    end
    # The low three frequencies exhibit the even Abel correction.  Fit the
    # intercept before comparing it with either independent target.
    X = hcat(ones(3), omegas[2:end].^2)
    extrapolated = [(X \ vec(residues[i, 2:end]))[1] for i in eachindex(horizons)]
    final = extrapolated[end]
    return (omega = omegas, horizon = horizons, residue = vec(residues[end, :]),
            residue_by_horizon = residues,
            residue_ratio = vec(residues[end, :]) / late_detector,
            soft_ratio = vec(residues[end, :]) / soft_prediction,
            extrapolated_by_horizon = extrapolated, extrapolated_residue = final,
            extrapolated_late_ratio = final / late_detector, extrapolated_vertex_ratio = final / soft_prediction,
            horizon_error = abs(extrapolated[end] - extrapolated[end - 1]),
            fitted_mobius_tail = fitted_tail, late_detector = Float64(late_detector),
            injected_charge_norm = charge_norm, vertex_soft_prediction = soft_prediction)
end
struct ResultValidationError <: Exception
    message::String
end
Base.showerror(io::IO, e::ResultValidationError) = print(io, e.message)
function _finite_tree(x)
    x isa Number && return isfinite(x)
    x isa AbstractDict && return all(_finite_tree(v) for v in values(x))
    x isa AbstractArray && return !isempty(x) && all(_finite_tree, x)
    x isa Tuple && return all(_finite_tree, x)
    return true
end
function validate_results(results::AbstractDict)
    _finite_tree(results) || throw(ResultValidationError("non-finite or empty result data"))
    points = get(results, "parameter_points", Any[])
    isempty(points) && throw(ResultValidationError("empty parameter-point set"))
    isempty(get(results, "late_time_grid", Any[])) &&
        throw(ResultValidationError("empty late-time sample set"))
    for p in points
        get(p, "charge_jump_error", Inf) <= 1e-6 ||
            throw(ResultValidationError("charge jump tolerance violated"))
        max(get(p, "pre_charge_drift", Inf), get(p, "post_charge_drift", Inf)) <= 1e-8 ||
            throw(ResultValidationError("outside-support charge conservation violated"))
        isempty(get(p, "delta_u_rel", Any[])) &&
            throw(ResultValidationError("empty displacement samples"))
    end
    return true
end
function validation_fixture()
    point = Dict("charge_jump_error" => 0.0, "pre_charge_drift" => 0.0,
                 "post_charge_drift" => 0.0, "delta_u_rel" => [1.0])
    return Dict("late_time_grid" => [2.0], "parameter_points" => [point])
end
function poisoned_result(mode::Symbol)
    r = validation_fixture()
    mode == :nan && (r["parameter_points"][1]["delta_u_rel"][1] = NaN)
    mode == :empty && (r["parameter_points"][1]["delta_u_rel"] = Float64[])
    mode == :charge && (r["parameter_points"][1]["charge_jump_error"] = 1e-2)
    mode in (:nan, :empty, :charge) || throw(ArgumentError("unknown poison mode"))
    return r
end
function write_results(path::AbstractString, results::AbstractDict)
    validate_results(results)
    open(path, "w") do io
        JSON.print(io, results, 2)
        write(io, '\n')
    end
    return path
end
_profile_name(::TopHatPulse) = "top_hat"
_profile_name(::GaussianPulse) = "gaussian"
_profile_name(::DerivativeGaussianPulse) = "derivative_gaussian_balanced"
_epsilon(p::AbstractPulse) = p.epsilon
_fit_dict(f) = Dict("winner" => f.winner, "rss_constant" => f.rss_constant,
                    "rss_exponential" => f.rss_exponential,
                    "constant" => f.constant, "amplitude" => f.amplitude,
                    "decay_rate" => f.decay_rate,
                    "aic_constant" => f.aic_constant,
                    "aic_exponential" => f.aic_exponential)

function _point(C::Real, pulse::AbstractPulse, h::Real, Delta::Real)
    run = simulate_pulse(C, pulse; h = h)
    obs = observable_series(Matrix{Float64}(I, 2, 2), run.mobius,
                            1.0, run.k_final, LATE_GRID; Delta = Delta)
    # T=2 can precede the small-c projective crossover.  Fit the late tail
    # T>=5, while retaining and reporting all five prescribed samples.
    fitrange = 2:length(LATE_GRID)
    fu = compare_models(LATE_GRID[fitrange], obs.delta_u[fitrange])
    fg = compare_models(LATE_GRID[fitrange], obs.delta_g[fitrange])
    dc = dc_identity(run, obs.delta_u[end]; Delta = Delta)
    kappa = (1 + run.k_final) / 2
    max_T = sqrt(C / kappa) # geometric-mean cutoff: kappa*T=sqrt(kappa*C)
    at_max = observable_series(Matrix{Float64}(I, 2, 2), run.mobius, 1.0,
                               run.k_final, [max_T]; Delta = Delta).delta_u[1]
    cost_factor = exp(4Delta * kappa * max_T)
    target_error = 0.1abs(dc.fitted_mobius_tail)
    jump_error = norm(run.charge_before - run.charge_after - run.flux, Inf)
    return Dict(
        "C" => Float64(C), "profile" => _profile_name(pulse),
        "epsilon" => _epsilon(pulse), "final_energy" => run.final_energy,
        "energy_change" => run.energy_change, "k_final" => run.k_final,
        "mobius" => [run.mobius[i, j] for i in 1:2, j in 1:2],
        "mobius_fit_residual" => run.mobius_fit_residual,
        "charge_before" => run.charge_before, "charge_after" => run.charge_after,
        "injected_charge" => run.flux, "charge_jump_error" => jump_error,
        "pre_charge_drift" => run.pre_charge_drift,
        "post_charge_drift" => run.post_charge_drift,
        "G_pulse" => obs.pulse, "G_equilibrium_final_energy" => obs.equilibrium,
        "delta_G_LR" => obs.delta_g, "delta_u_rel" => obs.delta_u,
        "fit_time_grid" => LATE_GRID[fitrange],
        "delta_u_model" => _fit_dict(fu), "delta_G_model" => _fit_dict(fg),
        "detector_window" => Dict("kappa_effective" => kappa, "maximum_usable_T" => max_T,
            "kappa_T_at_max" => kappa * max_T, "T_over_C_at_max" => max_T / C,
            "delta_u_at_max" => at_max,
            "sample_cost_model" => "M_shots ~ exp(4 Delta kappa T)/eta^2",
            "sample_cost_exponential_factor" => cost_factor, "sample_cost_target_eta" => target_error,
            "sample_cost_for_10pct_late_delta" => cost_factor / target_error^2),
        "dc" => Dict("omega" => dc.omega, "residue_ratio" => dc.residue_ratio,
                     "soft_ratio" => dc.soft_ratio, "horizon" => dc.horizon,
                     "residue_by_horizon" => [vec(dc.residue_by_horizon[i, :]) for i in axes(dc.residue_by_horizon, 1)],
                     "extrapolated_by_horizon" => dc.extrapolated_by_horizon,
                     "extrapolated_residue" => dc.extrapolated_residue,
                     "extrapolated_late_ratio" => dc.extrapolated_late_ratio,
                     "extrapolated_vertex_ratio" => dc.extrapolated_vertex_ratio,
                     "horizon_error" => dc.horizon_error, "fitted_mobius_tail" => dc.fitted_mobius_tail,
                     "late_detector" => dc.late_detector,
                     "fourier_convention" => "sum exp(+i omega t), Abel eta=omega^2",
                     "omega_extrapolation" => "linear intercept in omega^2 on 0.1,0.05,0.025",
                     "uniform_dt" => 0.02,
                     "injected_charge_norm" => dc.injected_charge_norm,
                     "vertex_soft_prediction" => dc.vertex_soft_prediction))
end

function _integrator_diagnostics()
    hs = [0.08, 0.04, 0.02, 0.01]
    exact = thermal_tan_state(1.6)
    errors = [norm(integrate_fixed(thermal_tan_state(-1.6), -1.6, 1.6, h,
                                   10.0, ZeroPulse()).y[:, end] - exact, Inf)
              for h in hs]
    orders = log2.(errors[1:end-1] ./ errors[2:end])
    regression_error = 0.0
    for period in -1:1
        u0, u1 = -2.0 + 2pi * period, 2.0 + 2pi * period
        tr = integrate_fixed(thermal_tan_state(u0), u0, u1, 5e-4,
                             10.0, ZeroPulse())
        regression_error = max(regression_error,
            maximum(maximum(abs.(tr.y[:, i] - thermal_tan_state(tr.u[i])))
                    for i in eachindex(tr.u)))
    end
    return Dict("step_sizes" => hs, "terminal_errors" => errors,
                "measured_orders" => orders,
                "tan_three_period_chart_max_error" => regression_error)
end

function run_campaign(; h::Real = 5e-4, Delta::Real = 0.5)
    jobs = Tuple{Float64,AbstractPulse}[]
    for C in (10.0, 100.0), epsilon in (0.01, 0.1)
        push!(jobs, (C, TopHatPulse(epsilon)))
    end
    for C in (10.0, 100.0)
        push!(jobs, (C, GaussianPulse(0.05)))
        push!(jobs, (C, DerivativeGaussianPulse(0.05)))
    end
    points = [_point(C, pulse, h, Delta) for (C, pulse) in jobs]
    results = Dict(
        "schema_version" => 2, "beta" => 2pi, "operator_dimension" => Float64(Delta),
        "late_time_grid" => LATE_GRID,
        "limit_convention" => Dict("order" =>
            "C -> infinity first; then kappa*T -> infinity with T/C -> 0",
            "window" => "1 << kappa*T << kappa*C",
            "finite_C_cutoff" => "kappa*T_max = sqrt(kappa*C)",
            "status" => "conservative scaling convention, not a uniform finite-C error bound"),
        "integration_method" => "fixed-step classical RK4",
        "source_equation" => "GravityReparametrizationsRevised.tex:611-623",
        "charge_equations" => "GravityReparametrizationsRevised.tex:889-900",
        "bilocal_rule" => "GravityReparametrizationsRevised.tex:645-675",
        "charge_jump_orientation" => "Q_before-Q_after = integral t' T (1,t,t^2)",
        "integrator_diagnostics" => _integrator_diagnostics(),
        "parameter_points" => points)
    validate_results(results)
    return results
end

end # module
