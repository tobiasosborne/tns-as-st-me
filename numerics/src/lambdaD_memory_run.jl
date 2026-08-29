# lambdaD_memory_run.jl — the kink-transport / memory protocol.  Shard 2 of
# `LambdaDMemory`; included by src/lambdaD_memory.jl (no module wrapper of its
# own, the TriangleMPS.jl shard convention).
#
# PROTOCOL (λD-KINK-MEM).  Everything is at Δ = 2.5, D = 0, on the two-site
# Néel cell.
#
#   1. `kink_sector` — the two Z₂ vacua ψ_A (staggered density +s) and ψ_B (−s),
#      and the measured tail density s = m_stag.
#   2. `group_velocity` — the kink band ω(k) at k₀ ± dk in the *topological*
#      sector, giving v = dω/dk.  Fixed BEFORE the dynamics: the measured packet
#      velocity is tested against it, not fitted to it.
#   3. `kink_packet`  — a Gaussian kink wavepacket at (x₀, σ, k₀), dressed by the
#      optimised quasiparticle tensor.
#   4. window-TDVP — TDVP2 on the WindowMPS with ψ_A / ψ_B frozen outside.
#   5. at every sample: the staggered profile, the three wall estimators, the
#      exact law of the windowed staggered charge on the fixed measurement
#      window W, the window energy, and the wall weight within `edge_guard`
#      sites of either end (`edge_leak` — the honest end of the run).
#
# WHAT IS TESTED, and why each is not a tautology.
#
#   (a) integer support.  `charge_modulus = |⟨e^{2πiQ̂_{W,c₀}}⟩| = 1` and the
#       phase equals 2πκ_{W,c₀}: the windowed charge lies in ONE coset of ℤ, so
#       every escaped-charge outcome ν = q(t_-) − q(t_+) is an integer
#       (M-INDEX-fin).  The *red control* in the same call is
#       `position_modulus = |⟨e^{2πi𝔛_W}⟩| < 1`: the wall coordinate is not
#       quantised.  Same state, same window, opposite verdict.
#   (b) the coefficient.  δx measured by the s-FREE centroid estimator X2 is
#       compared with −(2s)^{-1}⟨ν⟩ from the charge history.  s enters the right
#       side only; agreement is a measurement of the coefficient 2s, and the
#       naive value 2 (which is what "spin-1 ⇒ 2s = 2" would give) is off by
#       4 % here because s = m_stag = 0.9603, not 1.  `coefficient_measured`
#       reports −⟨ν⟩/δx(X2) as measured.
#   (c) group velocity.  dX2/dt against dω/dk.
#   (d) energy conservation and norm, as TDVP quality gates.
#
# WHAT IS NOT DONE (stated, not hidden).  The ordered TPM law of D27 with a
# genuine first projective measurement at t_- is NOT computed: doing it needs
# one TDVP run per charge branch.  What is recorded is the exact single-time law
# at each sample and the mean escaped charge ⟨ν⟩ = ⟨Q̂_W⟩(t_-) − ⟨Q̂_W⟩(t_+).
# That equals the TPM first moment iff D27(LR2) holds — an assumption, recorded
# as such in the JSON under `caveats`.

"""One sample of the kink-transport run."""
struct MemorySample
    t::Float64
    X1::Float64
    X2::Float64
    X3::Float64
    wall_weight::Float64
    Q_int::Float64
    Q_hat::Float64
    energy::Float64
    norm::Float64
    edge_leak::Float64
    charge_law::Vector{Float64}
    profile::Vector{Float64}
end

"""Result of one `memory_experiment` run."""
struct MemoryResult
    params::NamedTuple
    s::Float64
    omega0::Float64
    v_theory::Float64
    samples::Vector{MemorySample}
    charge_values::Vector{Int}
    cert_initial::NamedTuple
    cert_final::NamedTuple
    packet_energy::Float64
    v_measured::Float64
    v_fit_window::Tuple{Float64, Float64}
    dx_X1::Float64
    dx_X2::Float64
    dx_X3::Float64
    energy_drift_readout::Float64
    nu_mean::Float64
    dx_from_charge::Float64
    coefficient_measured::Float64
    t_minus::Float64
    t_plus::Float64
    readout_index::Tuple{Int, Int}
end

"""
    trajectory_velocity(ts, X, window) -> Float64

Least-squares slope of `X` against `t` over `window = (lo, hi)`.  Same estimator
as `spins_memory_run.jl`'s trajectory fit, restricted to one clean interval.
"""
function trajectory_velocity(ts::AbstractVector, X::AbstractVector, window::Tuple)
    idx = findall(i -> window[1] <= ts[i] <= window[2] && isfinite(X[i]), eachindex(ts))
    length(idx) >= 2 || return NaN
    tt = ts[idx]; xx = X[idx]
    tb = sum(tt) / length(tt); xb = sum(xx) / length(xx)
    den = sum((t - tb)^2 for t in tt)
    den > 0 || return NaN
    return sum((tt[i] - tb) * (xx[i] - xb) for i in eachindex(tt)) / den
end

"""
    memory_experiment(sec; L, W, c0, x0, sigma, k0, dt, nsteps, sample_every,
                      chi_max, edge_guard, dk, dressing, verbose) -> MemoryResult

Run the λD-KINK-MEM protocol on the sector `sec`.

Arguments that fix the geometry: `L` window sites, measurement window
`W = a:b ⊂ 1:L` with cut `c0 ∈ W`, packet centre `x0`, width `sigma`, momentum
`k0`.  `t_minus` / `t_plus` are chosen as the first and last sample at which the
wall (estimator `X1`) is padded from both edges of `W` by at least `sigma`, so
that D13(a)'s padding requirement holds at both readout times; if no such pair
exists the run reports `NaN` displacements rather than a number computed outside
the definition's scope.
"""
function memory_experiment(sec::KinkSector; L::Int = 64, W::AbstractUnitRange{Int} = 12:52,
                           c0::Union{Int, Nothing} = nothing, x0::Real = 20.0,
                           sigma::Real = 4.0, k0::Real = pi / 4, dt::Real = 0.1,
                           nsteps::Int = 100, sample_every::Int = 5,
                           chi_max::Int = 48, edge_guard::Int = 6, dk::Real = 0.02,
                           leak_tol::Real = 1.0e-3, dressing::Symbol = :qp,
                           verbose::Bool = false)
    first(W) >= 1 && last(W) <= L || throw(ArgumentError("W must lie inside 1:L"))
    cut = c0 === nothing ? (first(W) + last(W)) ÷ 2 : c0
    cut in W || throw(ArgumentError("c0 must lie in W"))

    v_theory, omega0 = group_velocity(sec, k0; dk = dk)
    _, phis = kink_dispersion(sec, [k0]; num = 1)
    psi = kink_packet(sec, phis[1]; L = L, x0 = x0, sigma = sigma, k0 = k0,
                      dressing = dressing)
    s = sec.s
    alg = TDVP2(; trscheme = truncrank(chi_max))
    envs = environments(psi, sec.H)

    vals = collect(-length(W):length(W))
    samples = MemorySample[]
    function sample!(t)
        n = staggered_profile(psi)
        est = wall_estimators(n, s, W)
        _, p = window_charge_law(psi, W; weight = 1.0)
        Qint = sum(v * pv for (v, pv) in zip(vals, p))
        Qhat = Qint - s * (2cut - first(W) - last(W) + 1)
        leak = sum(abs, est.wall_density[1:min(edge_guard, end)]) +
               sum(abs, est.wall_density[max(1, end - edge_guard + 1):end])
        push!(samples, MemorySample(t, est.X1, est.X2, est.X3, est.wall_weight,
                                    Qint, Qhat, window_energy(sec, psi), norm(psi),
                                    leak, p, n))
        verbose && @printf("t=%6.2f X1=%8.3f X2=%8.3f Q=%9.4f E=%9.5f leak=%.2e\n",
                           t, est.X1, est.X2, Qhat, samples[end].energy, leak)
        return nothing
    end

    cert_i = coset_certificate(psi, W, s, cut)
    packet_E = window_energy(sec, psi)
    sample!(0.0)
    for step in 1:nsteps
        psi, envs = timestep(psi, sec.H, 0.0, dt, alg, envs)
        step % sample_every == 0 && sample!(step * dt)
    end
    cert_f = coset_certificate(psi, W, s, cut)

    ts = [sm.t for sm in samples]
    X1 = [sm.X1 for sm in samples]
    X2 = [sm.X2 for sm in samples]
    X3 = [sm.X3 for sm in samples]

    # readout times: wall padded from both edges of W by ≥ 2σ (D13(a) demands the
    # kink core padded from both edges; 2σ leaves ~5 % of the packet outside),
    # and the packet not yet leaking into the frozen boundary
    pad = max(2 * sigma, 3.0)
    ok = [first(W) - 1 + pad <= X1[i] <= last(W) - pad && samples[i].edge_leak < leak_tol
          for i in eachindex(samples)]
    idx = findall(ok)
    if length(idx) >= 2
        i0, i1 = first(idx), last(idx)
        tm, tp = ts[i0], ts[i1]
        dx1 = X1[i1] - X1[i0]; dx2 = X2[i1] - X2[i0]; dx3 = X3[i1] - X3[i0]
        nu = samples[i0].Q_hat - samples[i1].Q_hat
        dxq = -nu / (2s)
        coeff = abs(dx2) > 1e-9 ? -nu / dx2 : NaN
        vmeas = trajectory_velocity(ts, X2, (tm, tp))
        vwin = (tm, tp)
        Er = [samples[i].energy for i in i0:i1]
        edrift = maximum(abs.(Er .- Er[1]))
    else
        i0 = i1 = 0
        tm = tp = NaN
        dx1 = dx2 = dx3 = nu = dxq = coeff = NaN
        vmeas = NaN
        vwin = (NaN, NaN)
        edrift = NaN
    end

    params = (point = sec.point, chi = sec.chi, L = L, W = (first(W), last(W)),
              c0 = cut, x0 = Float64(x0), sigma = Float64(sigma), k0 = Float64(k0),
              dt = Float64(dt), nsteps = nsteps, sample_every = sample_every,
              chi_max = chi_max, edge_guard = edge_guard, dk = Float64(dk),
              leak_tol = Float64(leak_tol), dressing = dressing)
    return MemoryResult(params, s, omega0, v_theory, samples, vals, cert_i, cert_f,
                        packet_E, vmeas, vwin, dx1, dx2, dx3, edrift, nu, dxq,
                        coeff, tm, tp, (i0, i1))
end

# ---------------------------------------------------------------------------
# Serialisation
# ---------------------------------------------------------------------------

_c(x::Real) = isfinite(x) ? Float64(x) : nothing
_c(v::AbstractVector{<:Real}) = [_c(x) for x in v]

"""
    memory_record(r::MemoryResult; profiles=true) -> Dict{String,Any}

JSON-ready record with every parameter needed to regenerate the run and every
measured number, non-finite floats as `null`.
"""
function memory_record(r::MemoryResult; profiles::Bool = true)
    p = r.params
    d = Dict{String, Any}(
        "protocol" => "lambdaD-kink-memory",
        "J" => p.point.J, "Delta" => p.point.Delta, "D" => p.point.D,
        "K" => p.point.K, "label" => p.point.label,
        "chi" => p.chi, "L" => p.L, "W" => collect(p.W), "c0" => p.c0,
        "x0" => p.x0, "sigma" => p.sigma, "k0" => p.k0, "dt" => p.dt,
        "nsteps" => p.nsteps, "sample_every" => p.sample_every,
        "chi_max" => p.chi_max, "edge_guard" => p.edge_guard, "dk" => p.dk,
        "leak_tol" => p.leak_tol,
        "dressing" => String(p.dressing),
        "s_tail_density" => _c(r.s),
        "omega_k0" => _c(r.omega0), "packet_energy" => _c(r.packet_energy),
        "v_theory_dwdk" => _c(r.v_theory), "v_measured" => _c(r.v_measured),
        "v_fit_window" => [_c(r.v_fit_window[1]), _c(r.v_fit_window[2])],
        "t_minus" => _c(r.t_minus), "t_plus" => _c(r.t_plus),
        "readout_index" => collect(r.readout_index),
        "dx_X1_D13a" => _c(r.dx_X1), "dx_X2_centroid" => _c(r.dx_X2),
        "dx_X3_crossing" => _c(r.dx_X3),
        "energy_drift_readout" => _c(r.energy_drift_readout),
        "nu_mean_escaped_charge" => _c(r.nu_mean),
        "dx_from_charge" => _c(r.dx_from_charge),
        "coefficient_measured" => _c(r.coefficient_measured),
        "coefficient_predicted_2s" => _c(2 * r.s),
        "charge_values" => r.charge_values,
        "cert_initial" => Dict(String(k) => _c(v) for (k, v) in pairs(r.cert_initial)),
        "cert_final" => Dict(String(k) => _c(v) for (k, v) in pairs(r.cert_final)),
        "times" => _c([sm.t for sm in r.samples]),
        "X1" => _c([sm.X1 for sm in r.samples]),
        "X2" => _c([sm.X2 for sm in r.samples]),
        "X3" => _c([sm.X3 for sm in r.samples]),
        "wall_weight" => _c([sm.wall_weight for sm in r.samples]),
        "Q_hat" => _c([sm.Q_hat for sm in r.samples]),
        "Q_int" => _c([sm.Q_int for sm in r.samples]),
        "energy" => _c([sm.energy for sm in r.samples]),
        "norm" => _c([sm.norm for sm in r.samples]),
        "edge_leak" => _c([sm.edge_leak for sm in r.samples]),
    )
    if profiles
        d["charge_law"] = [_c(sm.charge_law) for sm in r.samples]
        d["staggered_profile"] = [_c(sm.profile) for sm in r.samples]
    end
    return d
end
