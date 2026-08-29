"""
    LambdaD

Uniform-MPS ground states of the **anisotropic spin-1 λ–D chain**

    H = J Σ_x [ S^x_x S^x_{x+1} + S^y_x S^y_{x+1} + Δ S^z_x S^z_{x+1}
                + K (S_x·S_{x+1})^2 ]
      + D Σ_x (S^z_x)^2 ,

the showcase model of bd `tns-f5r`.  With `K = 0` the (Δ, D) plane contains the
three phases the campaign needs inside ONE Hamiltonian:

* **Néel** (Δ ≳ 1.19 at D = 0) — Z₂ spontaneous symmetry breaking, kinks;
* **Haldane** (Δ ≈ 1, D ≲ 0.97) — SPT, edge spin-½, ω ≠ 0;
* **large-D** (Δ ≈ 1, D ≳ 0.97) — trivial comparison partner.

`K` is carried only so that the exactly solvable **AKLT point**
(Δ = 1, D = 0, K = 1/3) lies inside the same family and can serve as a
calibration with closed-form numbers (e = −2/3, ξ = 1/log 3, S = log 2,
string order 4/9).  Every physics point of the issue has `K = 0`.

Conventions
-----------
* `S = 1`, ħ = 1, so `S^z` has eigenvalues `{+1, 0, −1}` (NOT `±1/2`; this
  differs from `xxz_sector.jl`, which is a spin-½ shard).
* Trivial-symmetry physical basis order is `m = +1, 0, −1`.  For the U(1)
  graded space TensorKit fixes its own sector order; `basis_charges` returns
  whatever order is in force, and every operator is built from it, so nothing
  downstream depends on the choice.
* The **string unitaries** are `U_z = exp(iπ S^z)` and `U_x = exp(iπ S^x)`.
  `U_x` is not charge conserving, hence unavailable in the `:u1` code path.

Two tensor backends
-------------------
`symmetry = :none` uses `ComplexSpace(3)` (works for every diagnostic).
`symmetry = :u1` uses `U1Space` and additionally resolves the entanglement
spectrum by `S^z_total` charge, at the cost of losing `O^x_string`.
The two backends are independent representations of the same Hamiltonian and
are cross-checked against one another in `test_lambdaD_groundstate.jl`.

Shards: this file (model + ground-state driver) plus `lambdaD_diagnostics.jl`
(observables + records), which continues this module.
"""
module LambdaD

using LinearAlgebra
using Random
using Printf
using Logging
using TensorKit
using MPSKit

export LambdaDPoint, spin1_ops, hamiltonian, find_gs, diagnose, record,
       GroundStateResult, NEEL_POINT, HALDANE_POINT, LARGED_POINT, AKLT_POINT

# ===========================================================================
# The parameter point
# ===========================================================================

"""
    LambdaDPoint(; J=1.0, Delta=1.0, D=0.0, K=0.0, label="")

One point of the λ–D family.  `K` is the biquadratic coupling (AKLT calibration
only); all physics points have `K = 0`.
"""
struct LambdaDPoint
    J::Float64
    Delta::Float64
    D::Float64
    K::Float64
    label::String
end

function LambdaDPoint(; J::Real = 1.0, Delta::Real = 1.0, D::Real = 0.0,
                      K::Real = 0.0, label::AbstractString = "")
    return LambdaDPoint(Float64(J), Float64(Delta), Float64(D), Float64(K),
                        String(label))
end

const NEEL_POINT    = LambdaDPoint(; Delta = 2.5, D = 0.0, label = "Neel")
const HALDANE_POINT = LambdaDPoint(; Delta = 1.0, D = 0.0, label = "Haldane")
const LARGED_POINT  = LambdaDPoint(; Delta = 1.0, D = 2.5, label = "largeD")
const AKLT_POINT    = LambdaDPoint(; Delta = 1.0, D = 0.0, K = 1/3, label = "AKLT")

# ===========================================================================
# Spin-1 operators, in both tensor backends
# ===========================================================================

"Physical space for the requested backend."
function physical_space(symmetry::Symbol)
    symmetry === :none && return ComplexSpace(3)
    symmetry === :u1   && return U1Space(1 => 1, 0 => 1, -1 => 1)
    throw(ArgumentError("symmetry must be :none or :u1, got $symmetry"))
end

"""
    basis_charges(symmetry) -> Vector{Int}

The `S^z` value carried by each index of the physical space, in TensorKit's
index order.  Everything else is built from this, so the code never assumes a
particular ordering.
"""
function basis_charges(symmetry::Symbol)
    symmetry === :none && return [1, 0, -1]
    P = physical_space(symmetry)
    return [Int(c.charge) for c in sectors(P)]
end

"Dense `S^z`, `S^+`, `S^-` in the basis order `ms`."
function dense_spin_matrices(ms::Vector{Int})
    d = length(ms)
    Sz = zeros(ComplexF64, d, d)
    Sp = zeros(ComplexF64, d, d)
    for j in 1:d
        Sz[j, j] = ms[j]
        m = ms[j]
        c = 2 - m * (m + 1)          # s(s+1) − m(m+1) with s = 1
        c <= 0 && continue
        i = findfirst(==(m + 1), ms)
        i === nothing && continue
        Sp[i, j] = sqrt(c)
    end
    return Sz, Sp, Matrix(adjoint(Sp))
end

"""
    spin1_ops(symmetry) -> NamedTuple

Spin-1 operators as TensorKit maps.  Fields: `P` (physical space), `ms`
(basis charges), `Id`, `Sz`, `Sz2`, `Uz`, `SS` (two-site `S·S`), and — for
`:none` only — `Sx`, `Sy`, `Ux`.  Charge-violating entries are `nothing` in
the `:u1` backend.
"""
function spin1_ops(symmetry::Symbol)
    P = physical_space(symmetry)
    ms = basis_charges(symmetry)
    Szm, Spm, Smm = dense_spin_matrices(ms)
    Sxm = (Spm + Smm) / 2
    Sym = (Spm - Smm) / (2im)
    Idm = Matrix{ComplexF64}(I, 3, 3)

    site(M) = TensorMap(copy(ComplexF64.(M)), P ← P)
    # two-site tensor from a dense 4-index array, index order (out1,out2,in1,in2)
    function two(A::Array{ComplexF64,4})
        return TensorMap(copy(A), P ⊗ P ← P ⊗ P)
    end
    function kron4(A, B)
        C = zeros(ComplexF64, 3, 3, 3, 3)
        for a in 1:3, b in 1:3, c in 1:3, e in 1:3
            C[a, b, c, e] = A[a, c] * B[b, e]
        end
        return C
    end

    SSd = kron4(Sxm, Sxm) + kron4(Sym, Sym) + kron4(Szm, Szm)
    SS = two(SSd)

    charged = symmetry === :none
    return (P = P, ms = ms, Id = site(Idm), Sz = site(Szm),
            Sz2 = site(Szm * Szm), Uz = site(exp(im * pi * Szm)),
            Sx = charged ? site(Sxm) : nothing,
            Sy = charged ? site(Sym) : nothing,
            Ux = charged ? site(exp(im * pi * Sxm)) : nothing,
            SS = SS,
            XXd = kron4(Sxm, Sxm) + kron4(Sym, Sym),
            ZZd = kron4(Szm, Szm),
            SSd = SSd)
end

# ---------------------------------------------------------------------------
# Closed-form product-state matrix elements (used by the MPO test, and cheap
# enough to keep as production helpers).
# ---------------------------------------------------------------------------

"⟨m m| S·S |m m⟩ for the uniform spin-1 product state."
exact_prod_SS(m::Integer) = Float64(m)^2

"⟨m m| (S·S)² |m m⟩ for the uniform spin-1 product state."
function exact_prod_SS2(m::Integer)
    cp = sqrt(max(0.0, 2 - m * (m + 1)))     # ⟨m+1|S⁺|m⟩
    cm = sqrt(max(0.0, 2 - m * (m - 1)))     # ⟨m−1|S⁻|m⟩
    # S·S |mm⟩ = m²|mm⟩ + ½ cp cm |m+1,m−1⟩ + ½ cm cp |m−1,m+1⟩
    return Float64(m)^4 + 0.5 * (cp * cm)^2
end

# ===========================================================================
# Hamiltonian
# ===========================================================================

"""
    hamiltonian(p::LambdaDPoint; unitcell=1, symmetry=:none) -> InfiniteMPOHamiltonian

Translation-invariant MPO for `H` on a `unitcell`-site cell.  A cell longer
than one site changes nothing about `H`; it only enlarges the variational
class so that translation-symmetry-broken states (the Néel phase) can be
represented.
"""
function hamiltonian(p::LambdaDPoint; unitcell::Int = 1, symmetry::Symbol = :none)
    unitcell >= 1 || throw(ArgumentError("unitcell must be >= 1"))
    ops = spin1_ops(symmetry)
    P = ops.P
    h2d = p.J .* (ops.XXd .+ p.Delta .* ops.ZZd)
    h2 = TensorMap(copy(h2d), P ⊗ P ← P ⊗ P)
    if p.K != 0
        h2 = h2 + (p.J * p.K) * (ops.SS * ops.SS)
    end
    h1 = p.D * ops.Sz2

    lattice = fill(P, unitcell)
    terms = Any[]
    for i in 1:unitcell
        push!(terms, (i, i + 1) => h2)
        p.D == 0 || push!(terms, i => h1)
    end
    return InfiniteMPOHamiltonian(lattice, terms)
end

# ===========================================================================
# Initial states
# ===========================================================================

"""
    virtual_space(chi, symmetry; qmax=4)

Bond space of (approximate) dimension `chi`.  For `:u1` the budget is spread
over the `S^z_total` charges `−qmax:qmax` with a Gaussian profile, each charge
getting at least one state.  The resulting dimension is the nearest achievable
value ≥ `chi` — the exact value is reported in the run record as `chi_actual`.
"""
function virtual_space(chi::Int, symmetry::Symbol; qmax::Int = 4)
    symmetry === :none && return ComplexSpace(chi)
    qs = -qmax:qmax
    σ = max(1.0, qmax / 2)
    w = [exp(-q^2 / (2σ^2)) for q in qs]
    w ./= sum(w)
    dims = [max(1, round(Int, chi * wi)) for wi in w]
    return U1Space(q => d for (q, d) in zip(qs, dims))
end

"""
    initial_state(p; chi, unitcell, symmetry, seed) -> InfiniteMPS

Random uniform MPS seeded deterministically, so a run is reproducible from the
record alone.
"""
function initial_state(; chi::Int, unitcell::Int, symmetry::Symbol, seed::Int,
                       qmax::Int = 4)
    Random.seed!(seed)
    P = physical_space(symmetry)
    V = virtual_space(chi, symmetry; qmax = qmax)
    return InfiniteMPS(fill(P, unitcell), fill(V, unitcell))
end

# ===========================================================================
# Ground-state search
# ===========================================================================

"""
    GroundStateResult

Everything needed to reproduce and to judge a uMPS ground-state search.
`galerkin` is the VUMPS convergence measure ε (the tangent-space gradient
norm); `converged` means `galerkin ≤ tol`, nothing weaker.
"""
struct GroundStateResult
    point::LambdaDPoint
    unitcell::Int
    chi::Int
    chi_actual::Int
    symmetry::Symbol
    seed::Int
    tol::Float64
    maxiter::Int
    psi::InfiniteMPS
    H::Any
    envs::Any
    energy_density::Float64
    energy_variance::Float64
    galerkin::Float64
    converged::Bool
    elapsed::Float64
    rounds::Int
end

"""
    find_gs(p; chi, unitcell=1, symmetry=:none, seed=20260829,
            tol=1e-10, maxiter=600, rounds=2, verbosity=0, qmax=4,
            grassmann_fallback=true)

VUMPS ground-state search.  If a round stops at `galerkin > tol` the search is
restarted from the stalled state, up to `rounds` times, and then handed to
`GradientGrassmann` once.  `converged` reports the honest final verdict, never
a relaxed one.
"""
function find_gs(p::LambdaDPoint; chi::Int, unitcell::Int = 1,
                 symmetry::Symbol = :none, seed::Int = 20260829,
                 tol::Real = 1.0e-10, maxiter::Int = 600, rounds::Int = 2,
                 verbosity::Int = 0, qmax::Int = 4,
                 grassmann_fallback::Bool = true)
    H = hamiltonian(p; unitcell = unitcell, symmetry = symmetry)
    psi = initial_state(; chi = chi, unitcell = unitcell, symmetry = symmetry,
                        seed = seed, qmax = qmax)
    chi_actual = dim(left_virtualspace(psi, 1))

    alg = VUMPS(; tol = tol, maxiter = maxiter, verbosity = verbosity)
    gs = psi
    envs = nothing
    eps = Inf
    used = 0
    quiet(f) = with_logger(f, verbosity > 0 ? current_logger() : NullLogger())
    t = @elapsed begin
        for r in 1:max(1, rounds)
            used = r
            gs, envs, eps = quiet() do
                find_groundstate(gs, H, alg)
            end
            eps <= tol && break
        end
        # VUMPS occasionally stalls above tol on a perfectly good state (seen at
        # Δ=1, D=2.5, χ=32).  Riemannian gradient descent on the same state is a
        # different descent direction and usually finishes the job; if it throws
        # or does no better we keep the VUMPS result and report it as measured.
        if eps > tol && grassmann_fallback
            try
                gs2, envs2, eps2 = quiet() do
                    find_groundstate(gs, H,
                        GradientGrassmann(; tol = tol, maxiter = 400,
                                          verbosity = max(0, verbosity - 1)))
                end
                if eps2 < eps
                    gs, envs, eps = gs2, envs2, eps2
                    used += 1
                end
            catch err
                @debug "Grassmann fallback failed" err
            end
        end
    end

    e = real(sum(expectation_value(gs, H, envs))) / unitcell
    v = abs(real(variance(gs, H, envs)))
    return GroundStateResult(p, unitcell, chi, chi_actual, symmetry, seed,
                             Float64(tol), maxiter, gs, H, envs, e, v,
                             Float64(eps), eps <= tol, t, used)
end

include(joinpath(@__DIR__, "lambdaD_diagnostics.jl"))

end # module LambdaD
