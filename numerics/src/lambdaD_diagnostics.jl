# lambdaD_diagnostics.jl — phase diagnostics for the λ–D chain.  Included by
# src/lambdaD_model.jl; continues module LambdaD (no module wrapper of its own,
# the TriangleMPS.jl shard convention).
#
# What each diagnostic is FOR (bd tns-f5r, wave 1):
#
#   string_z, string_x   den Nijs–Rommelse string order,
#                            O^α = − lim_{r→∞} ⟨S^α_1 (∏ e^{iπ S^α}) S^α_{1+r}⟩.
#                        O^z ≠ 0 in Haldane AND in Néel, = 0 in large-D.
#                        O^x ≠ 0 in Haldane only (Néel and large-D kill it).
#                        The pair therefore separates all three phases.
#   es_split1            (s₁−s₂)/s₁ of the entanglement spectrum.  ≈ 0 in the
#                        Haldane phase (the protected edge doublet), O(1) in
#                        large-D and in Néel.  This is the rigidity diagnostic:
#                        an exact degeneracy that cannot drift.
#   neel_order           staggered ⟨S^z⟩, the Z₂ SSB order parameter.
#   correlation_length   from the largest sub-unimodular transfer-matrix
#                        eigenvalue, per SITE (the unit-cell length is divided
#                        out).  This is the maximum over ALL channels, so it is
#                        the LONGEST correlation length in the state.
#                        χ-limited near a transition — always read it together
#                        with `chi` and `rank_deficient`.
#   xi_fit               the LONGITUDINAL correlation length only: an
#                        exponential fit to the measured connected ⟨S^z S^z⟩.
#                        These two are NOT the same number unless the state is
#                        SU(2) symmetric.  Measured here: at the Haldane point
#                        they agree (5.05 vs 5.01 at χ=32); in the large-D
#                        phase the transfer estimate is ≈ 2.8 and the
#                        longitudinal fit ≈ 1.23, because the longest channel
#                        there is the transverse (ΔS^z = ±1) one.  Quote
#                        `correlation_length` for "the" correlation length and
#                        `xi_fit` for the S^z channel; quote `xi_fit` alone
#                        when `rank_deficient` is set.
#   schmidt_by_charge    S^z-resolved entanglement spectrum (`:u1` runs only):
#                        the charge structure of the entanglement cut.
#
# Honest-reporting rules kept here:
#   * a quantity that the backend cannot represent is `NaN`, never 0;
#   * `rank_deficient` flags a bond whose numerical rank is below χ — the
#     transfer spectrum (hence ξ) then contains null-space junk;
#   * `string_z_tail` is the change of the string correlator over the last two
#     sites of the profile, i.e. evidence that the "plateau" is a plateau.

"Relative floor below which a Schmidt value counts as null-space noise."
const RANK_FLOOR = 1.0e-7

# ---------------------------------------------------------------------------
# String / two-point correlators along an infinite uniform MPS
# ---------------------------------------------------------------------------

"""
    string_correlator(psi, O1, U, O2, rmax) -> Vector{Float64}

`⟨O1_1 · U_2 ⋯ U_r · O2_{1+r}⟩` for `r = 1 … rmax`, on an `InfiniteMPS` in
mixed canonical form: `AC` at site 1 (left environment is then the identity,
because everything to its left is left-canonical) and `AR` afterwards (right
environment likewise the identity).  Passing `U = Id` gives the plain two-point
function.
"""
function string_correlator(psi::InfiniteMPS, O1, U, O2, rmax::Int)
    rmax >= 1 || throw(ArgumentError("rmax must be >= 1"))
    AC = psi.AC[1]
    @tensor v[-1; -2] := AC[1 3; -2] * O1[4; 3] * conj(AC[1 4; -1])
    out = Vector{Float64}(undef, rmax)
    for r in 1:rmax
        j = 1 + r
        AR = psi.AR[j]
        g = @tensor v[1; 2] * AR[2 3; 4] * O2[5; 3] * conj(AR[1 5; 4])
        out[r] = real(g)
        r == rmax && break
        @tensor vnew[-1; -2] := v[1; 2] * AR[2 3; -2] * U[4; 3] * conj(AR[1 4; -1])
        v = vnew
    end
    return out
end

"""
    string_order(psi, O, U, rmax) -> (profile, value, tail)

`profile[r] = −⟨O_1 U ⋯ U O_{1+r}⟩`, sign chosen so that the Haldane / AKLT
value is `+4/9`.  `value` is the profile at the largest EVEN separation (even,
so that a two-site unit cell is sampled at the same sublattice offset), and
`tail = profile[r] − profile[r−2]` there, the plateau evidence.
"""
function string_order(psi::InfiniteMPS, O, U, rmax::Int)
    prof = .-string_correlator(psi, O, U, O, rmax)
    rlast = iseven(rmax) ? rmax : rmax - 1
    rlast >= 2 || throw(ArgumentError("need rmax >= 2"))
    tail = rlast >= 4 ? prof[rlast] - prof[rlast - 2] : NaN
    return prof, prof[rlast], tail
end

# ---------------------------------------------------------------------------
# Entanglement spectrum
# ---------------------------------------------------------------------------

"Schmidt values on bond 0, sorted descending, together with the U(1)-resolved split."
function schmidt_data(psi::InfiniteMPS)
    es = entanglement_spectrum(psi, 0)
    flat = sort(collect(Float64, es); rev = true)
    bycharge = Dict{Int, Vector{Float64}}()
    if sectortype(typeof(es)) !== Trivial
        for c in keys(es)
            bycharge[Int(c.charge)] = sort(collect(Float64, es[c]); rev = true)
        end
    end
    return flat, bycharge
end

"von Neumann entropy from Schmidt values (singular values, not squares)."
function vn_entropy(s::AbstractVector{<:Real})
    S = 0.0
    for x in s
        p = x^2
        p > 1e-30 || continue
        S -= p * log(p)
    end
    return S
end

"Relative splitting of the Schmidt pair (2k−1, 2k); `NaN` if absent."
function pair_split(s::AbstractVector{<:Real}, k::Int)
    i = 2k - 1
    length(s) >= i + 1 || return NaN
    s[i] > 1e-14 || return NaN
    return (s[i] - s[i + 1]) / s[i]
end

# ---------------------------------------------------------------------------
# Correlation length
# ---------------------------------------------------------------------------

"""
    correlation_length_maxmod(psi; num_vals=12) -> (xi, moduli)

Correlation length in SITES from the largest sub-unimodular transfer-matrix
eigenvalue, `ξ = −n / log|λ₂|` with `n` the unit-cell length.  This differs
from `MPSKit.correlation_length`, which restricts to the dominant complex
phase; the maximum-modulus definition is the one that reproduces the AKLT
value `1/log 3` and is what the diagnostics table quotes.

CAVEAT (measured, not hypothetical).  `AL` is an isometry on the WHOLE virtual
space, so if the state does not fill its bond space the transfer matrix still
has eigenvalues in the unsupported block.  Those are not correlation lengths of
anything: at the AKLT point (exact bond dimension 2) run at χ = 16 they return
ξ ≈ 1.82 instead of 1/log 3 ≈ 0.91.  `diagnose` therefore reports this number
as `NaN` whenever `rank_deficient` is set, keeping the raw value separately,
and quotes `xi_fit` (below) instead.
"""
function correlation_length_maxmod(psi::InfiniteMPS; num_vals::Int = 12)
    n = length(psi)
    spec = with_logger(NullLogger()) do
        transfer_spectrum(psi; num_vals = num_vals)
    end
    mods = sort(abs.(spec); rev = true)
    sub = filter(x -> x < 1 - 1e-8, mods)
    isempty(sub) && return Inf, mods
    lam = first(sub)
    lam <= 0 && return 0.0, mods
    return -n / log(lam), mods
end

"""
    fit_correlation_length(zz_connected; rmin=4, floor=1e-11) -> (xi, r2, window)

Correlation length from the measured decay of a connected two-point function:
least squares of `log|C(r)|` against `r` over the window `rmin ≤ r ≤ r_last`,
where `r_last` is the last separation with `|C(r)| > floor`.  `r2` is the
coefficient of determination — a value near 1 says the decay really is a single
exponential over the window, which is what makes the number meaningful.

Unlike the transfer-matrix estimate this uses only an observable, so it is
immune to the unsupported-block artefact described above.  It is the number to
quote when `rank_deficient` is set.
"""
function fit_correlation_length(C::AbstractVector{<:Real}; rmin::Int = 4,
                                floor::Float64 = 1.0e-11)
    idx = [r for r in rmin:length(C) if abs(C[r]) > floor]
    length(idx) >= 4 || return NaN, NaN, (0, 0)
    # keep the leading contiguous run, so a sign change or a numerical floor
    # part-way along the profile does not get fitted through
    stop = length(idx)
    for k in 2:length(idx)
        if idx[k] != idx[k - 1] + 1
            stop = k - 1
            break
        end
    end
    idx = idx[1:stop]
    length(idx) >= 4 || return NaN, NaN, (0, 0)
    x = Float64.(idx)
    y = [log(abs(C[r])) for r in idx]
    x̄ = sum(x) / length(x); ȳ = sum(y) / length(y)
    sxx = sum((x .- x̄) .^ 2)
    sxy = sum((x .- x̄) .* (y .- ȳ))
    sxx > 0 || return NaN, NaN, (0, 0)
    slope = sxy / sxx
    resid = y .- (ȳ .+ slope .* (x .- x̄))
    syy = sum((y .- ȳ) .^ 2)
    r2 = syy > 0 ? 1 - sum(resid .^ 2) / syy : NaN
    slope < 0 || return Inf, r2, (first(idx), last(idx))
    return -1 / slope, r2, (first(idx), last(idx))
end

# ---------------------------------------------------------------------------
# The diagnostics record
# ---------------------------------------------------------------------------

"""
    diagnose(res::GroundStateResult; rmax=48, num_vals=12) -> NamedTuple

All wave-1 diagnostics for one converged (or honestly-not-converged) point.
Quantities the backend cannot represent are `NaN`.
"""
function diagnose(res::GroundStateResult; rmax::Int = 48, num_vals::Int = 12)
    psi = res.psi
    n = res.unitcell
    ops = spin1_ops(res.symmetry)

    sz_site = [real(expectation_value(psi, i => ops.Sz)) for i in 1:n]
    sz2_site = [real(expectation_value(psi, i => ops.Sz2)) for i in 1:n]
    sz_mean = sum(sz_site) / n
    sz2_mean = sum(sz2_site) / n
    neel = sum((-1)^(i + 1) * sz_site[i] for i in 1:n) / n

    prof_z, string_z, tail_z = string_order(psi, ops.Sz, ops.Uz, rmax)
    if ops.Sx === nothing
        prof_x, string_x, tail_x = Float64[], NaN, NaN
    else
        prof_x, string_x, tail_x = string_order(psi, ops.Sx, ops.Ux, rmax)
    end
    zz = string_correlator(psi, ops.Sz, ops.Id, ops.Sz, rmax)
    # connected: in the Néel phase ⟨S^z⟩ ≠ 0 and alternates with the sublattice
    zzc = [zz[r] - sz_site[1] * sz_site[mod1(1 + r, n)] for r in 1:rmax]

    flat, bycharge = schmidt_data(psi)
    # RANK_FLOOR: a Schmidt value this far below the leading one is null-space
    # noise, not physics.  1e-7 (relative), not machine epsilon: a VUMPS run at
    # tol 1e-12 still leaves ~1e-8 residue in genuinely empty directions (seen
    # at the AKLT point, where the exact rank is 2).
    rank = count(>(RANK_FLOOR * first(flat)), flat)
    deficient = rank < res.chi_actual
    xi_raw, mods = correlation_length_maxmod(psi; num_vals = num_vals)
    xi = deficient ? NaN : xi_raw
    xi_fit, xi_fit_r2, xi_fit_window = fit_correlation_length(zzc)

    return (point = res.point, unitcell = n, chi = res.chi,
            chi_actual = res.chi_actual, symmetry = res.symmetry,
            seed = res.seed, tol = res.tol, maxiter = res.maxiter,
            rounds = res.rounds, elapsed = res.elapsed,
            converged = res.converged, galerkin = res.galerkin,
            energy_density = res.energy_density,
            energy_variance = res.energy_variance,
            correlation_length = xi, correlation_length_raw = xi_raw,
            xi_fit = xi_fit, xi_fit_r2 = xi_fit_r2,
            xi_fit_window = xi_fit_window,
            transfer_moduli = mods,
            schmidt = flat, schmidt_by_charge = bycharge,
            bond_rank = rank, rank_deficient = deficient,
            entropy = vn_entropy(flat),
            es_split1 = pair_split(flat, 1), es_split2 = pair_split(flat, 2),
            es_split3 = pair_split(flat, 3),
            sz_site = sz_site, sz2_site = sz2_site,
            sz_mean = sz_mean, sz2_mean = sz2_mean, neel_order = neel,
            string_z = string_z, string_z_tail = tail_z,
            string_z_profile = prof_z,
            string_x = string_x, string_x_tail = tail_x,
            string_x_profile = prof_x,
            szsz_profile = zz, szsz_connected = zzc, rmax = rmax)
end

# ---------------------------------------------------------------------------
# Serialisation
# ---------------------------------------------------------------------------

_clean(x::Real) = isfinite(x) ? Float64(x) : nothing
_clean(v::AbstractVector{<:Real}) = [_clean(x) for x in v]

"""
    record(d) -> Dict{String,Any}

Flat, JSON-ready record of one diagnosed point.  Carries every parameter needed
to regenerate the run (`J, Delta, D, K, chi, unitcell, symmetry, seed, tol,
maxiter`) alongside the measured numbers.  Non-finite floats become `null`.
"""
function record(d)
    p = d.point
    r = Dict{String, Any}(
        "label" => p.label,
        "J" => p.J, "Delta" => p.Delta, "D" => p.D, "K" => p.K,
        "chi" => d.chi, "chi_actual" => d.chi_actual,
        "unitcell" => d.unitcell, "symmetry" => String(d.symmetry),
        "seed" => d.seed, "tol" => d.tol, "maxiter" => d.maxiter,
        "rounds" => d.rounds, "elapsed_s" => _clean(d.elapsed),
        "converged" => d.converged, "galerkin" => _clean(d.galerkin),
        "energy_density" => _clean(d.energy_density),
        "energy_variance" => _clean(d.energy_variance),
        "correlation_length" => _clean(d.correlation_length),
        "correlation_length_raw" => _clean(d.correlation_length_raw),
        "xi_fit" => _clean(d.xi_fit),
        "xi_fit_r2" => _clean(d.xi_fit_r2),
        "xi_fit_window" => collect(d.xi_fit_window),
        "transfer_moduli" => _clean(d.transfer_moduli),
        "schmidt" => _clean(d.schmidt),
        "bond_rank" => d.bond_rank, "rank_deficient" => d.rank_deficient,
        "entropy" => _clean(d.entropy),
        "es_split1" => _clean(d.es_split1),
        "es_split2" => _clean(d.es_split2),
        "es_split3" => _clean(d.es_split3),
        "sz_site" => _clean(d.sz_site), "sz2_site" => _clean(d.sz2_site),
        "sz_mean" => _clean(d.sz_mean), "sz2_mean" => _clean(d.sz2_mean),
        "neel_order" => _clean(d.neel_order),
        "string_z" => _clean(d.string_z),
        "string_z_tail" => _clean(d.string_z_tail),
        "string_z_profile" => _clean(d.string_z_profile),
        "string_x" => _clean(d.string_x),
        "string_x_tail" => _clean(d.string_x_tail),
        "string_x_profile" => _clean(d.string_x_profile),
        "szsz_profile" => _clean(d.szsz_profile),
        "szsz_connected" => _clean(d.szsz_connected),
        "rmax" => d.rmax,
    )
    if !isempty(d.schmidt_by_charge)
        r["schmidt_by_charge"] =
            Dict(string(q) => _clean(v) for (q, v) in d.schmidt_by_charge)
    end
    return r
end

"""
    summary_line(d) -> String

One fixed-width line per point, for the run log / the report table.
"""
function summary_line(d)
    return @sprintf(
        "%-10s Δ=%5.2f D=%5.2f n=%d χ=%3d%s conv=%d ε=%.1e  e=%+.8f var=%.1e  ξ=%7.3f ξfit=%7.3f(R²=%.4f)  s1s2=%.2e  Oz=%+.5f  Ox=%+.5f  mstag=%+.5f",
        p_label(d), d.point.Delta, d.point.D, d.unitcell, d.chi_actual,
        d.rank_deficient ? "*" : " ",
        d.converged ? 1 : 0, d.galerkin, d.energy_density, d.energy_variance,
        d.correlation_length, d.xi_fit, d.xi_fit_r2,
        isnan(d.es_split1) ? -1.0 : d.es_split1,
        d.string_z, isnan(d.string_x) ? NaN : d.string_x, d.neel_order)
end

p_label(d) = isempty(d.point.label) ? "point" : d.point.label
