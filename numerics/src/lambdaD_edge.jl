"""
    LambdaDEdge

Edge memory in the **Haldane** phase against the **large-D** phase of the same
λ–D Hamiltonian (`src/lambdaD_model.jl`, bd `tns-f5r`, wave 2, deliverable 2).

The two points are `Δ = 1, D = 0` (Haldane, SPT) and `Δ = 1, D = 2.5` (large-D,
trivial).  They have the same symmetry and the same bulk order parameters up to
smooth drift; what separates them is the **protected edge spin-½** of the
Haldane phase, which is what this shard measures — dynamically, as a memory.

PROTOCOL (λD-EDGE-MEM).

  1. Open chain of `L` sites.  A **permanent** field `h_R S^z_L` pins the right
     edge for the whole run, so that whatever the left edge does is unambiguous.
     The default is `h_R = −h_L`: the two edges are then pinned OPPOSITELY, the
     run sits in the `S^z_tot = 0` sector in **both** phases, and `m_L` is a
     genuine measurement rather than half of a conserved total.  (With
     `h_R = +h_L` the preparation is reflection symmetric and `m_L = S^z_tot/2`
     identically — a symmetry artifact, not a measurement.  Do not use that
     setting to claim a contrast.)
  2. Preparation: the DMRG ground state of `H + h_L S^z_1 + h_R S^z_L`.  This is
     the `t < 0` half of a boundary field pulse, applied adiabatically.
  3. At `t = 0` the left field is switched off.  Everything after that is
     evolution under `H + h_R S^z_L` alone.
  4. Readout: `m_L(t) = Σ_{x=1}^{ℓ}⟨S^z_x⟩` over the left half (`ℓ = L÷2`) —
     a windowed charge, and the natural "did the edge remember?" observable,
     since `S^z_tot` is conserved and the right edge is pinned.  Also recorded:
     the on-site `⟨S^z_1⟩` and the whole profile.

WHAT THE CONTRAST IS.  In the Haldane phase the left edge carries a free
spin-½; the pulse selects one of its two states, and after the field is gone
that choice is (up to the exponentially small edge–edge splitting `∼e^{−L/ξ}`)
a conserved label.  `m_L` therefore stays put, near `∓½`.  In the large-D phase
there is no edge mode: the field only polarises the boundary linearly, and once
it is switched off the induced moment radiates into the bulk and `m_L` decays.
The record reports `m_L(0)`, `m_L(t_end)`, the retention `m_L(t_end)/m_L(0)`
and `mL_absmax`.  The honest reading of the measured contrast is the ABSOLUTE
one: in the Haldane phase `m_L` sits at `−½` and stays there; in the large-D
phase `m_L` never leaves `≈ 0`, so its *relative* retention is a ratio of two
numerical zeros and means nothing.  `mL_initial`, `mL_final` and `mL_absmax`
are the numbers to quote; `retention` is kept only because it is meaningful on
the Haldane side.

The local moment tells the same story from the other side: `⟨S^z_1⟩` relaxes
substantially in BOTH phases once the field is off (the polarisation cloud
radiates into the bulk).  What distinguishes them is that in the Haldane phase
the *windowed* charge `m_L` does not follow it down — the half unit stays on
the edge — whereas in large-D there was never a half unit to lose.

HONEST SCOPE.  A finite open chain has an exponentially small edge–edge
splitting, so Haldane retention is exact only up to times `∼e^{L/ξ}`; `L`, `ξ`
and the run time are all in the record.  `chi_max` truncation and TDVP2 error
are reported through the energy drift of the post-pulse Hamiltonian, which is
conserved exactly in the continuum protocol.
"""
module LambdaDEdge

using LinearAlgebra
using Printf
using Logging
using TensorKit
using MPSKit

include(joinpath(@__DIR__, "lambdaD_model.jl"))
using .LambdaD

export finite_hamiltonian, EdgeResult, edge_experiment, edge_record

"""
    finite_hamiltonian(p, L; hL=0.0, hR=0.0) -> FiniteMPOHamiltonian

Open chain of `L` spin-1 sites carrying the λ–D Hamiltonian of `p` plus boundary
fields `hL·S^z_1` and `hR·S^z_L`.  Same two-site and on-site terms as
`LambdaD.hamiltonian`; only the boundary conditions and the two fields differ,
so nothing is redefined.
"""
function finite_hamiltonian(p::LambdaD.LambdaDPoint, L::Int; hL::Real = 0.0,
                            hR::Real = 0.0)
    L >= 4 || throw(ArgumentError("need L ≥ 4"))
    ops = LambdaD.spin1_ops(:none)
    P = ops.P
    h2d = p.J .* (ops.XXd .+ p.Delta .* ops.ZZd)
    h2 = TensorMap(copy(h2d), P ⊗ P ← P ⊗ P)
    p.K == 0 || (h2 = h2 + (p.J * p.K) * (ops.SS * ops.SS))
    lattice = fill(P, L)
    terms = Any[(x, x + 1) => h2 for x in 1:(L - 1)]
    if p.D != 0
        for x in 1:L
            push!(terms, x => p.D * ops.Sz2)
        end
    end
    hL == 0 || push!(terms, 1 => hL * ops.Sz)
    hR == 0 || push!(terms, L => hR * ops.Sz)
    return FiniteMPOHamiltonian(lattice, terms)
end

"""Result of one `edge_experiment` run."""
struct EdgeResult
    params::NamedTuple
    times::Vector{Float64}
    mL::Vector{Float64}
    sz1::Vector{Float64}
    energy::Vector{Float64}
    norm::Vector{Float64}
    profile0::Vector{Float64}
    profile_end::Vector{Float64}
    E_prep::Float64
    gs_converged::Bool
    gs_residual::Float64
end

"""
    edge_experiment(p; L, chi, hL, hR, dt, nsteps, sample_every, chi_max,
                    edge_window=nothing, verbose=false) -> EdgeResult

Run λD-EDGE-MEM at the parameter point `p`.  `edge_window` defaults to `1:L÷2`.
"""
function edge_experiment(p::LambdaD.LambdaDPoint; L::Int = 40, chi::Int = 48,
                         hL::Real = 0.5, hR::Real = -0.5, dt::Real = 0.1,
                         nsteps::Int = 200, sample_every::Int = 10,
                         chi_max::Int = 64, edge_window = nothing,
                         gs_tol::Real = 1.0e-8, gs_maxiter::Int = 300,
                         verbose::Bool = false)
    ops = LambdaD.spin1_ops(:none)
    P = ops.P
    Wl = edge_window === nothing ? (1:(L ÷ 2)) : edge_window
    Hprep = finite_hamiltonian(p, L; hL = hL, hR = hR)
    Hrun = finite_hamiltonian(p, L; hL = 0.0, hR = hR)

    psi0 = FiniteMPS(rand, ComplexF64, L, P, ComplexSpace(chi))
    quiet(f) = with_logger(f, verbose ? current_logger() : NullLogger())
    psi, envs, eps = quiet() do
        find_groundstate(psi0, Hprep,
                         DMRG2(; tol = gs_tol, maxiter = gs_maxiter, verbosity = 0,
                               trscheme = truncrank(chi)))
    end
    E_prep = real(expectation_value(psi, Hprep))
    converged = eps <= gs_tol

    alg = TDVP2(; trscheme = truncrank(chi_max))
    renvs = environments(psi, Hrun)
    ts = Float64[]; mL = Float64[]; sz1 = Float64[]; en = Float64[]; nm = Float64[]
    prof(st) = [real(expectation_value(st, x => ops.Sz)) for x in 1:L]
    profile0 = prof(psi)
    function sample!(t)
        pr = prof(psi)
        push!(ts, t)
        push!(mL, sum(pr[x] for x in Wl))
        push!(sz1, pr[1])
        push!(en, real(expectation_value(psi, Hrun, renvs)))
        push!(nm, norm(psi))
        verbose && @printf("t=%6.2f  mL=%+8.5f  sz1=%+8.5f  E=%12.7f\n",
                           t, mL[end], sz1[end], en[end])
        return nothing
    end
    sample!(0.0)
    for step in 1:nsteps
        psi, renvs = timestep(psi, Hrun, 0.0, dt, alg, renvs)
        step % sample_every == 0 && sample!(step * dt)
    end

    params = (point = p, L = L, chi = chi, hL = Float64(hL), hR = Float64(hR),
              dt = Float64(dt), nsteps = nsteps, sample_every = sample_every,
              chi_max = chi_max, edge_window = (first(Wl), last(Wl)))
    return EdgeResult(params, ts, mL, sz1, en, nm, profile0, prof(psi),
                      E_prep, converged, Float64(eps))
end

_c(x::Real) = isfinite(x) ? Float64(x) : nothing
_c(v::AbstractVector{<:Real}) = [_c(x) for x in v]

"""
    edge_record(r::EdgeResult) -> Dict{String,Any}

JSON-ready record: parameters, the `m_L` history, and the three summary numbers
`mL_initial`, `mL_final`, `retention`.
"""
function edge_record(r::EdgeResult)
    p = r.params
    m0 = r.mL[1]; m1 = r.mL[end]
    return Dict{String, Any}(
        "protocol" => "lambdaD-edge-memory",
        "label" => p.point.label, "J" => p.point.J, "Delta" => p.point.Delta,
        "D" => p.point.D, "K" => p.point.K,
        "L" => p.L, "chi" => p.chi, "chi_max" => p.chi_max,
        "hL" => p.hL, "hR" => p.hR, "dt" => p.dt, "nsteps" => p.nsteps,
        "sample_every" => p.sample_every,
        "edge_window" => collect(p.edge_window),
        "gs_converged" => r.gs_converged, "gs_residual" => _c(r.gs_residual),
        "E_prep" => _c(r.E_prep),
        "times" => _c(r.times), "mL" => _c(r.mL), "sz1" => _c(r.sz1),
        "energy" => _c(r.energy), "norm" => _c(r.norm),
        "energy_drift" => _c(maximum(abs.(r.energy .- r.energy[1]))),
        "mL_initial" => _c(m0), "mL_final" => _c(m1),
        "mL_absmax" => _c(maximum(abs, r.mL)),
        "mL_drift" => _c(m1 - m0),
        "retention" => _c(abs(m0) > 1e-6 ? m1 / m0 : NaN),
        "sz1_initial" => _c(r.sz1[1]), "sz1_final" => _c(r.sz1[end]),
        "profile_initial" => _c(r.profile0),
        "profile_final" => _c(r.profile_end),
    )
end

end # module LambdaDEdge
