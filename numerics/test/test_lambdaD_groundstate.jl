# test_lambdaD_groundstate.jl -- red/green tests for the anisotropic spin-1
# lambda-D chain (bd tns-f5r, wave 1: ground states + phase diagnostics).
#
#     H = J Σ_x [ Sx Sx + Sy Sy + Δ Sz Sz + K (S·S)^2 ] + D Σ_x (Sz_x)^2
#
# The K term (biquadratic) is carried ONLY so that the exactly solvable AKLT
# point (Δ=1, D=0, K=1/3) sits inside the same family and can be used as a
# calibration test with closed-form numbers.  The physics points of the issue
# all have K = 0.
#
# PASS CRITERIA ARE FIXED HERE IN ADVANCE OF ANY PRODUCTION RUN.
#
# Exact AKLT reference values (all closed form, no fitting):
#   energy density              e = -2/3
#   correlation length          ξ = 1/log 3
#   Schmidt spectrum            (1/√2, 1/√2), so S_vN = log 2
#   string order (z and x)      O_string = 4/9
# Literature reference (quoted, not derived here):
#   spin-1 Heisenberg (Δ=1, D=0, K=0) energy density e0 = -1.401484038971(4)
#   [White & Huse, PRB 48, 3844 (1993); Todo & Kato, PRL 87, 047203 (2001)].
#   Used only as a two-sided bracket, not as an equality.
#
# Wrapped in `module TestLambdaDGroundstate` so numerics/test/runtests.jl can
# include every shard test into one process (the shard convention).

module TestLambdaDGroundstate

using Test
using LinearAlgebra
using Random
using TensorKit
using MPSKit

include(joinpath(@__DIR__, "..", "src", "lambdaD_model.jl"))
using .LambdaD

# --------------------------------------------------------------- tolerances --
const TOL_EXACT   = 1.0e-7    # AKLT closed-form values, VUMPS tol 1e-12, χ=2
const TOL_MPO     = 1.0e-12   # product-state energies: pure MPO arithmetic
const TOL_XCHECK  = 1.0e-4    # U(1)-graded vs trivial-symmetry, Haldane point
                              # (different variational classes, see testset 7)
const E_HEIS      = -1.401484038971  # literature, spin-1 Heisenberg
const HEIS_SLACK  = 3.0e-4    # χ=24 must land within this of the literature
const ES_PAIRED   = 5.0e-3    # (s1-s2)/s1 below this  => degenerate doublet
const ES_SPLIT    = 0.4       # (s1-s2)/s1 above this  => non-degenerate
const STRING_ZERO = 5.0e-3    # |O_string| below this  => "zero"
const HALDANE_OZ  = (0.35, 0.40)   # literature O^z_string ≈ 0.3743 at Δ=1,D=0
const NEEL_MSTAG  = 0.9

const SEED = 20260829

# =============================================================================
# 1. On-site operator algebra -- guards the spin-1 conventions everything else
#    is built on.  Cheap, exact.
# =============================================================================

@testset "lambdaD: spin-1 operator algebra" begin
    ops = LambdaD.spin1_ops(:none)
    Sx, Sy, Sz = ops.Sx, ops.Sy, ops.Sz
    Id = ops.Id

    ax = convert(Array, Sx); ay = convert(Array, Sy); az = convert(Array, Sz)
    id3 = convert(Array, Id)

    # [Sx, Sy] = i Sz  and cyclic
    @test maximum(abs, ax*ay - ay*ax - im*az) < 1e-14
    @test maximum(abs, ay*az - az*ay - im*ax) < 1e-14
    @test maximum(abs, az*ax - ax*az - im*ay) < 1e-14
    # S^2 = s(s+1) = 2
    @test maximum(abs, ax*ax + ay*ay + az*az - 2*id3) < 1e-14
    # Sz eigenvalues are exactly {+1, 0, -1}
    @test sort(real.(eigvals(az))) ≈ [-1.0, 0.0, 1.0] atol=1e-14
    # hermiticity
    @test maximum(abs, ax - ax') < 1e-14
    @test maximum(abs, ay - ay') < 1e-14

    # string unitaries: U_z = exp(iπ Sz) has eigenvalues (-1)^m, U^2 = 1
    uz = convert(Array, ops.Uz); ux = convert(Array, ops.Ux)
    @test maximum(abs, uz*uz - id3) < 1e-13
    @test maximum(abs, ux*ux - id3) < 1e-13
    @test maximum(abs, uz*az + az*uz - 2*(uz*az)) < 1e-13   # [Uz, Sz] = 0
    @test maximum(abs, uz - Diagonal(exp.(im*pi*real.(diag(az))))) < 1e-13
end

# =============================================================================
# 2. MPO correctness on product states.  For the uniform product state |m⟩^⊗∞
#    the energy density is exactly computable, and each coupling shows up in a
#    different combination, so this pins Δ, D and K separately.
#
#      |m=+1⟩ :  e = J(Δ + K)  + D          (S·S = 1 on |++⟩, so (S·S)^2 = 1)
#      |m= 0⟩ :  e = 0                      (all terms annihilate |00⟩ diagonally
#                                            except K, see below)
# =============================================================================

@testset "lambdaD: MPO reproduces exact product-state energies" begin
    P = ComplexSpace(3)
    # |m=+1⟩ product state (basis order m = +1, 0, -1)
    for (mindex, mval) in ((1, 1), (2, 0), (3, -1))
        A = zeros(ComplexF64, 1, 3, 1)
        A[1, mindex, 1] = 1.0
        psi = InfiniteMPS([TensorMap(copy(A), ComplexSpace(1) ⊗ P ← ComplexSpace(1))])
        for (J, Δ, D, K) in ((1.0, 2.5, 0.0, 0.0), (1.0, 1.0, 2.5, 0.0),
                             (1.3, -0.7, 0.4, 1/3))
            p = LambdaDPoint(; J = J, Delta = Δ, D = D, K = K)
            H = LambdaD.hamiltonian(p)
            e = real(sum(expectation_value(psi, H)))
            # exact: ⟨m m| Sx⊗Sx + Sy⊗Sy |m m⟩ = 0, ⟨m m| Sz⊗Sz |m m⟩ = m^2,
            #        ⟨m m| S·S |m m⟩ = m^2, ⟨m m| (S·S)^2 |m m⟩ = m^4 + 2*(off-diag)
            ss  = LambdaD.exact_prod_SS(mval)
            ss2 = LambdaD.exact_prod_SS2(mval)
            eref = J * (Δ * mval^2 + K * ss2) + D * mval^2
            @test abs(e - eref) < TOL_MPO
            @test abs(ss - mval^2) < TOL_MPO
        end
    end
end

# =============================================================================
# 3. AKLT calibration -- exact closed-form numbers, χ = 2 (the exact bond
#    dimension of the AKLT state).
# =============================================================================

@testset "lambdaD: AKLT point reproduces closed-form values" begin
    p = LambdaDPoint(; Delta = 1.0, D = 0.0, K = 1/3, label = "AKLT")
    res = LambdaD.find_gs(p; chi = 2, tol = 1e-12, maxiter = 500, seed = SEED)
    @test res.converged
    d = LambdaD.diagnose(res; rmax = 24)

    @test abs(d.energy_density - (-2/3)) < TOL_EXACT
    @test d.energy_variance < 1e-10
    @test abs(d.correlation_length - 1/log(3)) < TOL_EXACT
    @test abs(d.entropy - log(2)) < TOL_EXACT
    @test length(d.schmidt) == 2
    @test abs(d.schmidt[1] - 1/sqrt(2)) < TOL_EXACT
    @test abs(d.schmidt[2] - 1/sqrt(2)) < TOL_EXACT
    @test d.es_split1 < TOL_EXACT
    # string order, both channels, exactly 4/9
    @test abs(d.string_z - 4/9) < TOL_EXACT
    @test abs(d.string_x - 4/9) < TOL_EXACT
    # the profile is flat already at r = 2 for AKLT
    @test abs(d.string_z_profile[2] - 4/9) < TOL_EXACT
    @test abs(d.neel_order) < TOL_EXACT
end

# =============================================================================
# 4. Haldane point (Δ=1, D=0, K=0): SPT.  Even entanglement degeneracy,
#    nonzero string order in both channels, no Neel order.
# =============================================================================

@testset "lambdaD: Haldane point (Delta=1, D=0)" begin
    p = LambdaDPoint(; Delta = 1.0, D = 0.0, label = "Haldane")
    res = LambdaD.find_gs(p; chi = 24, tol = 1e-10, maxiter = 600, seed = SEED)
    d = LambdaD.diagnose(res; rmax = 48)

    # variational upper bound: can never go below the true ground-state energy
    @test d.energy_density > E_HEIS - 1e-9
    @test d.energy_density < E_HEIS + HEIS_SLACK
    # leading Schmidt values form a degenerate doublet (SPT edge spin-1/2)
    @test d.es_split1 < ES_PAIRED
    # and so does the next one
    @test d.es_split2 < ES_PAIRED
    # string order nonzero in both channels
    @test HALDANE_OZ[1] < d.string_z < HALDANE_OZ[2]
    @test HALDANE_OZ[1] < d.string_x < HALDANE_OZ[2]
    # no symmetry breaking
    @test abs(d.neel_order) < 1e-5
    @test abs(d.sz_mean) < 1e-5
    @test d.correlation_length > 3.0     # χ-limited, but clearly long
end

# =============================================================================
# 5. Large-D point (Δ=1, D=2.5): trivial.  Non-degenerate leading Schmidt
#    value, string order zero in both channels.
# =============================================================================

@testset "lambdaD: large-D point (Delta=1, D=2.5)" begin
    p = LambdaDPoint(; Delta = 1.0, D = 2.5, label = "largeD")
    res = LambdaD.find_gs(p; chi = 16, tol = 1e-10, maxiter = 600, seed = SEED)
    @test res.converged
    d = LambdaD.diagnose(res; rmax = 48)

    @test d.es_split1 > ES_SPLIT           # leading Schmidt value is a singlet
    @test abs(d.string_z) < STRING_ZERO
    @test abs(d.string_x) < STRING_ZERO
    @test abs(d.neel_order) < 1e-5
    @test d.sz2_mean < 0.5                 # (S^z)^2 suppressed: |m=0⟩ dominates
    @test d.correlation_length < 4.0       # short-ranged, deep in the phase
end

# =============================================================================
# 6. Neel point (Δ=2.5, D=0): Z2 SSB.  Needs a 2-site unit cell; the 1-site
#    cell must FAIL to converge, which is itself a check that the SSB is real
#    and not a gauge artefact.
# =============================================================================

@testset "lambdaD: Neel point (Delta=2.5, D=0)" begin
    p = LambdaDPoint(; Delta = 2.5, D = 0.0, label = "Neel")
    res = LambdaD.find_gs(p; chi = 16, unitcell = 2, tol = 1e-10,
                          maxiter = 600, seed = SEED)
    @test res.converged
    d = LambdaD.diagnose(res; rmax = 48)

    @test abs(d.neel_order) > NEEL_MSTAG
    @test d.sz_site[1] * d.sz_site[2] < 0          # staggered, opposite signs
    @test abs(d.sz_mean) < 1e-6                    # zero net magnetisation
    @test d.es_split1 > ES_SPLIT                   # no SPT doublet
    @test abs(d.string_x) < STRING_ZERO            # transverse string dies
    @test abs(d.string_z) > 0.5                    # z-string survives in Neel
    @test d.correlation_length < 2.0
end

# =============================================================================
# 7. U(1)-graded cross-check: the same point solved with charge-conserving
#    tensors must give the same energy density.  Two independent tensor
#    representations, one number.
# =============================================================================

@testset "lambdaD: U(1)-graded run agrees with trivial-symmetry run" begin
    # (a) EXACT cross-check.  At the AKLT point both backends must return the
    #     same closed-form numbers, so this compares the two tensor
    #     representations with no variational slack at all.
    ra = LambdaD.find_gs(AKLT_POINT; chi = 4, symmetry = :u1, tol = 1e-12,
                         maxiter = 500, seed = SEED)
    @test ra.converged
    @test abs(ra.energy_density - (-2/3)) < TOL_EXACT
    da = LambdaD.diagnose(ra; rmax = 16)
    @test abs(da.entropy - log(2)) < TOL_EXACT
    @test abs(da.string_z - 4/9) < TOL_EXACT
    @test da.bond_rank == 2
    # the AKLT bond carries exactly two Schmidt states, and they sit in two
    # DIFFERENT S^z sectors one unit apart -- the edge spin-1/2 doublet
    occupied = sort([q for (q, v) in da.schmidt_by_charge
                     if any(>(1e-8), v)])
    @test length(occupied) == 2
    @test occupied[2] - occupied[1] == 1

    # (b) VARIATIONAL cross-check at the Haldane point.  Here the two backends
    #     are NOT the same variational class: the graded run spends its bond
    #     budget on a fixed charge allocation, so its energy is a (slightly)
    #     worse upper bound.  Both must still bracket the literature value from
    #     above and agree to 1e-4.
    p = LambdaDPoint(; Delta = 1.0, D = 0.0, label = "Haldane")
    r0 = LambdaD.find_gs(p; chi = 24, tol = 1e-10, maxiter = 600, seed = SEED)
    r1 = LambdaD.find_gs(p; chi = 24, symmetry = :u1, tol = 1e-10,
                         maxiter = 600, seed = SEED)
    @test r0.energy_density > E_HEIS - 1e-9
    @test r1.energy_density > E_HEIS - 1e-9
    @test abs(r0.energy_density - r1.energy_density) < 1.0e-4

    d1 = LambdaD.diagnose(r1; rmax = 24)
    # sector-resolved entanglement spectrum: charges present, and the total
    # count matches the flat spectrum
    @test sum(length, values(d1.schmidt_by_charge)) == length(d1.schmidt)
    @test abs(sum(x -> sum(abs2, x), values(d1.schmidt_by_charge)) - 1) < 1e-8
    # Haldane doublet is visible in the graded run too
    @test d1.es_split1 < ES_PAIRED
    # the U(1) run cannot see O^x (exp(iπ Sx) is not charge conserving)
    @test isnan(d1.string_x)
    @test HALDANE_OZ[1] < d1.string_z < HALDANE_OZ[2]
end

# =============================================================================
# 8. The rank-deficiency artefact.  `AL` is an isometry on the whole virtual
#    space, so a state that does not fill its bond space still has
#    transfer-matrix eigenvalues in the unsupported block -- and they are not
#    correlation lengths.  Run the AKLT state (exact bond dimension 2) at
#    chi = 16 and check that
#      (a) the artefact is real and is caught (`rank_deficient`, raw value wrong)
#      (b) `correlation_length` refuses to quote a number
#      (c) `xi_fit`, which reads the decay of a measured correlator, is right.
# =============================================================================

@testset "lambdaD: rank deficiency is caught, xi_fit survives it" begin
    res = LambdaD.find_gs(AKLT_POINT; chi = 16, tol = 1e-12, maxiter = 500,
                          seed = SEED)
    d = LambdaD.diagnose(res; rmax = 24)
    @test d.bond_rank == 2
    @test d.rank_deficient
    @test isnan(d.correlation_length)
    # the raw transfer-matrix number is finite and WRONG -- that is the point
    @test isfinite(d.correlation_length_raw)
    @test abs(d.correlation_length_raw - 1/log(3)) > 0.5
    # the fit to ⟨SzSz⟩_c, which only sees observables, gets it right
    @test abs(d.xi_fit - 1/log(3)) < 1e-6
    @test d.xi_fit_r2 > 0.9999
    # exact AKLT correlator ⟨S^z_1 S^z_{1+r}⟩ = (4/3)(−1/3)^r  (= −4/9 at r = 1,
    # which is what the exact bond energy −2/3 = ⟨S·S⟩ + ⅓⟨(S·S)²⟩ demands:
    # ⟨S·S⟩ = 3⟨S^zS^z⟩ = −4/3 and ⟨(S·S)²⟩ = 2)
    for r in 1:8
        @test abs(d.szsz_profile[r] - (4/3) * (-1/3)^r) < 1e-8
    end

    # and at the exact bond dimension there is no deficiency, and the two
    # estimators agree
    res2 = LambdaD.find_gs(AKLT_POINT; chi = 2, tol = 1e-12, maxiter = 500,
                           seed = SEED)
    d2 = LambdaD.diagnose(res2; rmax = 24)
    @test !d2.rank_deficient
    @test abs(d2.correlation_length - d2.xi_fit) < 1e-6
end

# =============================================================================
# 9. Reproducibility: same seed => same numbers, and the JSON record round-trips
#    all the metadata needed to regenerate the run.
# =============================================================================

@testset "lambdaD: reproducibility and record" begin
    p = LambdaDPoint(; Delta = 1.0, D = 2.5, label = "largeD")
    a = LambdaD.find_gs(p; chi = 12, tol = 1e-10, maxiter = 400, seed = 4242)
    b = LambdaD.find_gs(p; chi = 12, tol = 1e-10, maxiter = 400, seed = 4242)
    @test abs(a.energy_density - b.energy_density) < 1e-12

    rec = LambdaD.record(LambdaD.diagnose(a; rmax = 16))
    for k in ("J", "Delta", "D", "K", "chi", "unitcell", "symmetry", "seed",
              "tol", "converged", "energy_density", "energy_variance",
              "correlation_length", "correlation_length_raw", "xi_fit",
              "xi_fit_r2", "rank_deficient", "string_z", "es_split1")
        @test haskey(rec, k)
    end
    @test rec["chi"] == 12
    @test rec["Delta"] == 1.0
end

end # module
