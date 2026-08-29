"""
    LambdaDMemory

Kink transport and the **memory effect** in the Néel phase of the anisotropic
spin-1 λ–D chain (`src/lambdaD_model.jl`, bd `tns-f5r`, wave 2).

The model point is `Δ = 2.5, D = 0, K = 0`: Z₂ spontaneously broken, so the two
translation-symmetry-broken uniform MPS `ψ_A` (staggered density `+s`) and
`ψ_B = ψ_A` shifted by one site (`−s`) are two distinct vacua and a domain wall
between them is a **topologically nontrivial excitation** — it cannot be created
by any local operator on either vacuum.

What this module does, in order:

1. `neel_vacua`      — orient the Néel ground state and produce the Z₂ partner.
2. `kink_dispersion` — MPSKit `QuasiparticleAnsatz` in the *topological* sector
                       (`left_gs = ψ_A`, `right_gs = ψ_B`), giving `ω(k)` and,
                       by central differences, the group velocity `dω/dk`.
3. `kink_packet`     — a Gaussian kink **wavepacket** as a `WindowMPS` whose
                       left/right infinite environments are `ψ_A`/`ψ_B`.  The
                       wall amplitude is carried by the *optimised* excitation
                       tensor of step 2, so the packet is a dressed kink, not a
                       sharp junction.  (`dressing = :sharp` reproduces the
                       sharp junction as a deliberately-bad control: HANDOFF's
                       dressed-kink discipline — sharp walls fake violations.)
4. `memory_experiment` — window-TDVP transport of that packet past a fixed
                       measurement window `W`, recording the D13(a) wall
                       coordinate, two `s`-free wall estimators, and the full
                       counting statistics of the windowed staggered charge.

Conventions (nothing here is redefined from `definitions.md` / `notation.md`).

* **Staggered density** `n_x := (−1)^{x+1} S^z_x`.  `ψ_A` is oriented so that
  `⟨n_x⟩ = +s` on it; then `⟨n_x⟩ = −s` on `ψ_B`.  This is exactly D13(a)'s
  `s_α = +s` at `−∞`, `s_β = −s` at `+∞`.
* **The calibration `s`** is the measured tail density `s = m_stag` (H-MQG(2)
  fixes the D13(a) parameter to be the tail density, `s = ρ`).  At `Δ = 2.5` it
  is `s ≈ 0.96034` — **not** `1`, and not a half-integer.  Every formula below
  uses the measured value, and the run record carries it.
* **D13(a) wall coordinate** `𝔛_W = a − 1 + (2s)^{-1} Σ_{x∈W}(n_x + s)`.
* **Windowed charge** `Q̂_{W,c₀} = 2s(𝔛_W − c₀)`; by LD-ID this equals
  `Σ_{x∈W}(n_x − s_γ(x))`, i.e. the *integer-spectrum* operator
  `Q^int_W := Σ_{x∈W} n_x` shifted by the c-number `−s(2c₀−a−b+1)`.  The
  identity is asserted numerically in the test shard.
* **Escaped charge** `ν := q(t_-) − q(t_+)` (D27's ordering), so that
  `δx = −(2s)^{-1}Σ_ν ν p_ν` is the same displacement as `𝔛_W(t_+) − 𝔛_W(t_-)`.

Shards (L2): this file (module + kink sector) and `lambdaD_memory_run.jl`
(protocol, observables, record).  The edge-memory contrast of the same issue is
a separate module, `src/lambdaD_edge.jl`.

WHAT THIS IS AND IS NOT A MEASUREMENT OF.  The protocol transports a kink past
a window and reads the charge ledger.  It therefore measures the **bookkeeping**
half of the memory statement — M-INDEX-fin's integer support and M-INDEX-spec's
`δx = −(2s)^{-1}Σ_ν ν p_ν` relating an integer-valued escaped charge to a
continuous wall displacement, with the coefficient `2s` fixed by the measured
tail density.  It does **not** exhibit a memory in the "transient perturbation
leaves a permanent offset" sense: nothing here scatters off the wall, so the
displacement is just ballistic transport.  The soft-theorem memory of D16 — a
magnon crossing the wall and leaving it shifted — needs a second excitation in
the window and is not attempted in this shard.  `src/lambdaD_edge.jl` does
exhibit a genuine transient-in / permanent-out memory, on the SPT side.

HONEST SCOPE.  The TDVP window has **frozen** infinite environments: nothing in
the run is trustworthy after the packet reaches the window edge, and the driver
records `edge_leak`, the wall-density weight within `edge_guard` sites of either
end, so that the reader can see it.  The ordered TPM law of D27 with a genuine
first projective measurement is *not* computed here: what is recorded is the
exact single-time law of `Q̂_{W,c₀}` at every sampled time (the windowed-charge
history) and the mean escaped charge.  These coincide with the TPM law's support
and first moment only if D27(LR2) holds; that is stated, not assumed proved.
"""
module LambdaDMemory

using LinearAlgebra
using Printf
using Logging
using TensorKit
using MPSKit

include(joinpath(@__DIR__, "lambdaD_model.jl"))
using .LambdaD

export neel_vacua, kink_dispersion, group_velocity, kink_packet, vacuum_window,
       staggered_profile, wall_estimators, window_charge_law, coset_certificate,
       window_energy, KinkSector, kink_sector,
       MemoryResult, memory_experiment, memory_record, trajectory_velocity

# ===========================================================================
# The two Néel vacua
# ===========================================================================

"""
    neel_vacua(psi) -> (psiA, psiB, s)

Orient a converged two-site-cell Néel uMPS so that the staggered density
`n_x = (−1)^{x+1}⟨S^z_x⟩` is **positive** on `psiA`, and return the Z₂ partner
`psiB` (the same state shifted by one site, on which `n_x` is negative) together
with the measured tail density `s = |n_x|`.

The orientation matters: VUMPS picks one of the two broken vacua at random from
the seed, and every sign convention below (D13(a)'s `s_α = +s` at `−∞`) is tied
to `psiA` being the `+s` one.
"""
function neel_vacua(psi::InfiniteMPS)
    length(psi) == 2 || throw(ArgumentError("Néel vacua need a two-site unit cell"))
    ops = LambdaD.spin1_ops(:none)
    sz = [real(expectation_value(psi, i => ops.Sz)) for i in 1:2]
    shifted = InfiniteMPS([psi.AL[2], psi.AL[3]])
    psiA, psiB = sz[1] >= 0 ? (psi, shifted) : (shifted, psi)
    szA = [real(expectation_value(psiA, i => ops.Sz)) for i in 1:2]
    s = (szA[1] - szA[2]) / 2                     # = ⟨n_x⟩ on psiA, both sites
    s > 0 || throw(ArgumentError("orientation failed: staggered density $s ≤ 0"))
    return psiA, psiB, s
end

"""
    KinkSector

Everything the transport protocol needs about the topological sector: the two
vacua, their environments, the measured tail density `s`, and the vacuum bond
energy used to zero the window energy.
"""
struct KinkSector
    point::LambdaD.LambdaDPoint
    chi::Int
    psiA::InfiniteMPS
    psiB::InfiniteMPS
    H::Any
    envA::Any
    envB::Any
    s::Float64
    e_bond::Float64
    h2::Any
end

"""
    kink_sector(point; chi, tol=1e-10, seed=20260829) -> KinkSector

Ground state at `point` on a two-site cell (trivial-symmetry backend, because
the window construction needs both vacua in the *same* virtual spaces), oriented
by [`neel_vacua`](@ref).
"""
function kink_sector(point::LambdaD.LambdaDPoint = LambdaD.NEEL_POINT;
                     chi::Int = 16, tol::Real = 1.0e-10, seed::Int = 20260829,
                     maxiter::Int = 800)
    res = LambdaD.find_gs(point; chi = chi, unitcell = 2, symmetry = :none,
                          seed = seed, tol = tol, maxiter = maxiter)
    res.converged || @warn "kink_sector: ground state not converged" ε = res.galerkin
    psiA, psiB, s = neel_vacua(res.psi)
    H = res.H
    ops = LambdaD.spin1_ops(:none)
    P = ops.P
    h2d = point.J .* (ops.XXd .+ point.Delta .* ops.ZZd)
    point.K == 0 || throw(ArgumentError("kink transport is defined for K = 0 only"))
    point.D == 0 || throw(ArgumentError("kink transport is defined for D = 0 only"))
    h2 = TensorMap(copy(h2d), P ⊗ P ← P ⊗ P)
    e_bond = real(expectation_value(psiA, (1, 2) => h2))
    envA = environments(psiA, H)
    envB = environments(psiB, H)
    return KinkSector(point, chi, psiA, psiB, H, envA, envB, s, e_bond, h2)
end

# ===========================================================================
# Kink dispersion in the topological sector
# ===========================================================================

"""
    kink_dispersion(sec, ks; num=1) -> (energies, states)

`ω(k)` for the domain-wall excitation, from MPSKit's `QuasiparticleAnsatz` with
`left_gs = ψ_A` and `right_gs = ψ_B`.  Because the two ground states differ, the
ansatz is in the topologically nontrivial sector and the returned state is a
kink, not a magnon.

`momentum` is per SITE in MPSKit's convention (the transfer systems carry
`exp(i k n_cell)` with `n_cell` the cell length).  For this model `ω` has period
`π`: a one-site translation maps the `A|B` sector to `B|A`, and the Z₂ spin flip
maps it back, so `ω(k) = ω(k+π)` exactly.  The Brillouin zone is `(−π/2, π/2]`.
"""
function kink_dispersion(sec::KinkSector, ks::AbstractVector{<:Real}; num::Int = 1)
    Es = Vector{Vector{Float64}}(undef, length(ks))
    states = Vector{Any}(undef, length(ks))
    for (i, k) in enumerate(ks)
        E, phi = with_logger(NullLogger()) do
            excitations(sec.H, QuasiparticleAnsatz(), Float64(k),
                        sec.psiA, sec.envA, sec.psiB, sec.envB; num = num)
        end
        Es[i] = real.(collect(E))[1:num]
        states[i] = phi[1]
    end
    return Es, states
end

"""
    group_velocity(sec, k0; dk=0.02) -> (v, ω0)

Central-difference `dω/dk` at `k0` from three `QuasiparticleAnsatz` solves, in
SITES per unit time.  This is the number the measured wavepacket velocity is
tested against.
"""
function group_velocity(sec::KinkSector, k0::Real; dk::Real = 0.02)
    Es, _ = kink_dispersion(sec, [k0 - dk, k0, k0 + dk]; num = 1)
    v = (Es[3][1] - Es[1][1]) / (2dk)
    return v, Es[2][1]
end

# ===========================================================================
# The kink wavepacket, as a WindowMPS
# ===========================================================================

function _dense3(t)
    a = convert(Array, t)
    return reshape(a, size(a, 1), size(a, 2), :)
end

"""
    kink_packet(sec, phi; L, x0, sigma, k0, dressing=:qp) -> WindowMPS

A Gaussian kink wavepacket on a window of `L` sites, with `ψ_A` frozen to its
left and `ψ_B` frozen to its right.

The construction is the standard block form of a one-particle superposition,

    T[x] = [ A[x]   g(x)·B[x] ;
             0      Bvac[x]   ] ,   g(x) = e^{−(x−x0)²/4σ²} e^{i k₀ x},

with `A = ψ_A.AL`, `Bvac = ψ_B.AR`, and `B` the **variationally optimised**
excitation tensor of the quasiparticle solution `phi` at momentum `k₀`
(`dressing = :qp`).  The left boundary of the window is forced into the `A`
block and the right boundary into the `B` block, so the wall is created exactly
once, with amplitude `g(x)`; the bond dimension is `2χ`.

`dressing = :sharp` replaces `B[x]` by `Bvac[x]` — the *sharp junction*, i.e. a
step from one vacuum straight to the other with no dressing at all.  It is kept
because it is the control the HANDOFF's dressed-kink discipline demands: a sharp
wall is not a one-kink state (its energy is far above the band) and reporting it
as one fakes agreement.  Never use it for physics.
"""
function kink_packet(sec::KinkSector, phi; L::Int, x0::Real, sigma::Real,
                     k0::Real, dressing::Symbol = :qp)
    dressing in (:qp, :sharp) ||
        throw(ArgumentError("dressing must be :qp or :sharp, got $dressing"))
    L >= 4 || throw(ArgumentError("window too short"))
    chi = dim(left_virtualspace(sec.psiA, 1))
    P = LambdaD.spin1_ops(:none).P
    A = [convert(Array, sec.psiA.AL[i]) for i in 1:2]
    Bv = [convert(Array, sec.psiB.AR[i]) for i in 1:2]
    Bq = dressing === :qp ? [_dense3(phi[i]) for i in 1:2] : Bv
    g(x) = exp(-(x - x0)^2 / (4 * sigma^2)) * cis(k0 * x)

    Vc = ComplexSpace(chi)
    V2 = ComplexSpace(2chi)
    tens = map(1:L) do x
        c = mod1(x, 2)
        if x == 1
            T = zeros(ComplexF64, chi, 3, 2chi)
            T[:, :, 1:chi] .= A[c]
            T[:, :, (chi + 1):2chi] .= g(x) .* Bq[c]
            TensorMap(T, Vc ⊗ P ← V2)
        elseif x == L
            T = zeros(ComplexF64, 2chi, 3, chi)
            T[1:chi, :, :] .= g(x) .* Bq[c]
            T[(chi + 1):2chi, :, :] .= Bv[c]
            TensorMap(T, V2 ⊗ P ← Vc)
        else
            T = zeros(ComplexF64, 2chi, 3, 2chi)
            T[1:chi, :, 1:chi] .= A[c]
            T[(chi + 1):2chi, :, (chi + 1):2chi] .= Bv[c]
            T[1:chi, :, (chi + 1):2chi] .= g(x) .* Bq[c]
            TensorMap(T, V2 ⊗ P ← V2)
        end
    end
    psi = WindowMPS(sec.psiA, FiniteMPS(tens), sec.psiB)
    normalize!(psi)
    return psi
end

"Vacuum window (`ψ_A` everywhere, no wall) — the energy reference."
function vacuum_window(sec::KinkSector, L::Int)
    tens = [sec.psiA.AL[mod1(x, 2)] for x in 1:L]
    return WindowMPS(sec.psiA, FiniteMPS(tens), sec.psiA)
end

# ===========================================================================
# Window observables
# ===========================================================================

"`⟨n_x⟩ = (−1)^{x+1}⟨S^z_x⟩` on every site of the window."
function staggered_profile(psi)
    Sz = LambdaD.spin1_ops(:none).Sz
    return [(-1)^(x + 1) * real(expectation_value(psi, x => Sz)) for x in 1:length(psi)]
end

"""
    wall_estimators(n, s, W) -> NamedTuple

Three wall-position estimators from one staggered profile `n`, in the spirit of
`spins_memory_sector.jl`'s `X̂₁/X̂₂/X̂₃`:

* `X1` — D13(a) exactly: `a − 1 + (2s)^{-1}Σ_{x∈W}(n_x + s)` on the measurement
  window `W = a:b`.  Uses `s`; **saturates** at `a−1` and `b` once the wall
  leaves `W`, which is why D13(a) demands the core padded from both edges.
* `X2` — centroid of the wall density `w_x = (n_x − n_{x+1})/2s` over the whole
  TDVP window.  The normalisation `Σw` divides out, so `X2` is **independent of
  `s`**: this is the estimator that makes the `δx = −(2s)^{-1}⟨ν⟩` coefficient
  test a test and not an identity.
* `X3` — linear-interpolated zero crossing of `n_x`, also `s`-free.

`wall_weight` is `Σ_x w_x` — one for a single wall fully inside the window.
"""
function wall_estimators(n::AbstractVector{<:Real}, s::Real, W::AbstractUnitRange{Int})
    a, b = first(W), last(W)
    X1 = a - 1 + sum(n[x] + s for x in W) / (2s)
    w = [(n[x] - n[x + 1]) / (2s) for x in 1:(length(n) - 1)]
    tot = sum(w)
    X2 = abs(tot) > 1e-8 ? sum((x + 0.5) * w[x] for x in eachindex(w)) / tot : NaN
    X3 = NaN
    for x in 1:(length(n) - 1)
        if n[x] > 0 >= n[x + 1]
            X3 = x + n[x] / (n[x] - n[x + 1])
            break
        end
    end
    return (X1 = X1, X2 = X2, X3 = X3, wall_weight = tot, wall_density = w)
end

"""
    window_charge_law(psi, W; weight=1.0) -> (values, probs)

The law of `Σ_{x∈W} weight·n_x` on `psi`, obtained by exact discrete Fourier
inversion of the characteristic function
`χ(θ) = ⟨∏_{x∈W} e^{iθ·weight·n_x}⟩` on the integer grid `−|W| … |W|`.

`weight = 1` is the windowed staggered charge `Q^int_W = Σ_{x∈W}n_x`, and the
inversion is then **exact**: `Q^int_W` is a sum of commuting on-site operators
with integer spectrum, so the grid is its whole spectrum and the returned
`probs` is a genuine probability distribution.  The D13(a) charge
`Q̂_{W,c₀} = Σ_{x∈W}(n_x − s_γ(x))` is `Q^int_W` shifted by a c-number
(row LD-ID), so this is its law up to that shift.

`weight = 1/(2s)` is the **red control**: it returns the same inversion applied
to the D13(a) wall coordinate `𝔛_W` (up to a shift), whose spectrum is in
`(2s)^{-1}ℤ` and therefore *not* in one coset of `ℤ`.  The inversion is then an
aliased signed measure and acquires negative entries.  The wall displacement is
not quantised; the charge is.  That contrast is the numerical content of
M-INDEX-fin here, and `min(probs)` is the number that carries it.
"""
function window_charge_law(psi, W::AbstractUnitRange{Int}; weight::Real = 1.0)
    nw = length(W)
    M = 2nw + 1
    thetas = [2pi * j / M for j in 0:(M - 1)]
    cf = [_phase_expectation(psi, W, th, weight) for th in thetas]
    vals = collect(-nw:nw)
    probs = [real(sum(cis(-th * v) * c for (th, c) in zip(thetas, cf))) / M
             for v in vals]
    return vals, probs
end

"""
    coset_certificate(psi, W, s, c0) -> NamedTuple

`⟨e^{2πiQ̂_{W,c₀}}⟩` and `⟨e^{2πi𝔛_W}⟩` measured on `psi`.

The first has modulus 1 and phase `2πκ_{W,c₀}` — equivalently
`⟨e^{2πiQ^int_W}⟩ = 1`, which is what `charge_phase_defect` measures — with
`κ_{W,c₀} = −s(2c₀−a−b+1)`, which is exactly "`spec Q̂_{W,c₀}` lies in one coset
of `ℤ`" (M-INDEX-fin's (G-IDX.0), certified arithmetically).  The second has
modulus **strictly below 1** whenever `2s ∉ ℤ`: the wall coordinate itself is
not quantised.  `charge_modulus`, `charge_phase_defect` and `position_modulus`
are the three numbers the test shard asserts on.
"""
function coset_certificate(psi, W::AbstractUnitRange{Int}, s::Real, c0::Int)
    a, b = first(W), last(W)
    kappa = -s * (2c0 - a - b + 1)
    zq = _phase_expectation(psi, W, 2pi, 1.0) * cis(2pi * kappa)
    zx = _phase_expectation(psi, W, 2pi, 1 / (2s))
    d = angle(zq) - 2pi * kappa
    phase_defect = abs(d - 2pi * round(d / (2pi)))
    return (charge_modulus = abs(zq), charge_phase_defect = phase_defect,
            kappa = kappa, position_modulus = abs(zx))
end

"⟨∏_{x∈W} exp(iθ·w·n_x)⟩, contracted directly along the window."
function _phase_expectation(psi, W::AbstractUnitRange{Int}, theta::Real, w::Real)
    ops = LambdaD.spin1_ops(:none)
    P = ops.P
    szdiag = diag(convert(Array, ops.Sz))
    u(x) = TensorMap(ComplexF64.(diagm(cis.(theta * w * (-1)^(x + 1) .* szdiag))), P ← P)
    a = first(W)
    AC = psi.AC[a]
    ua = u(a)
    @tensor v[-1; -2] := AC[1 3; -2] * ua[4; 3] * conj(AC[1 4; -1])
    for x in (a + 1):last(W)
        AR = psi.AR[x]
        ux = u(x)
        @tensor vn[-1; -2] := v[1; 2] * AR[2 3; -2] * ux[4; 3] * conj(AR[1 4; -1])
        v = vn
    end
    return @tensor v[1; 1]
end

"""
    window_energy(sec, psi) -> Float64

`Σ_{x=1}^{L−1}⟨h_{x,x+1}⟩ − (L−1)e_bond`: the energy carried by the window
relative to the vacuum.  At `D = 0` the Hamiltonian has no on-site term, so this
is the whole of it apart from the two frozen boundary bonds, whose drift is the
honest measure of when the packet has reached the edge.
"""
function window_energy(sec::KinkSector, psi)
    L = length(psi)
    e = sum(real(expectation_value(psi, (x, x + 1) => sec.h2)) for x in 1:(L - 1))
    return e - (L - 1) * sec.e_bond
end

include(joinpath(@__DIR__, "lambdaD_memory_run.jl"))

end # module LambdaDMemory
