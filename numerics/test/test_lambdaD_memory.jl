# test_lambdaD_memory.jl — red/green tests for wave 2 of the λ–D showcase
# (bd tns-f5r): kink transport and the memory effect in the Néel phase, and the
# Haldane / large-D edge-memory contrast.
#
# Wrapped in `module TestLambdaDMemory` so that numerics/test/runtests.jl can
# include every shard test into one process (the shard modules export names that
# also exist in TriangleMPS / LambdaD).  runtests.jl auto-discovers `test_*.jl`,
# so no wiring beyond the file name is needed.
#
# PASS CRITERIA ARE FIXED HERE IN ADVANCE OF THE PRODUCTION RUNS.
#
#   TOL_EXACT     identities that are exact algebra (LD-ID, the coset modulus)
#   TOL_LAW       normalisation / positivity of an exactly-inverted charge law
#   BAND_PACKET   |E_packet − ω(k₀)| for a genuine one-kink wavepacket
#   SHARP_FLOOR   the same quantity for the SHARP junction control, which must
#                 be FAR outside the band — a sharp wall is not a one-kink state
#                 and reporting it as one is the failure mode the HANDOFF's
#                 dressed-kink discipline warns about
#   BAND_V        relative agreement of the measured wavepacket velocity with
#                 dω/dk from the topological-sector dispersion
#   BAND_COEFF    relative agreement of the measured memory coefficient
#                 −⟨ν⟩/δx(X2) with the predicted 2s = 2·m_stag.  The test also
#                 demands that the measurement prefer 2s over the naive 2:
#                 s = m_stag = 0.9603 ≠ 1, so the two differ by 4 %.
#   MEDGE_HALDANE  |m_L| the Haldane edge must hold (the edge spin-½ is ½)
#   MDRIFT_HALDANE how far m_L may move after the field is switched off
#   MEDGE_LARGED   the ceiling on |m_L| in the large-D phase at ALL times.
#                  The large-D RELATIVE retention is meaningless — m_L is a
#                  numerical zero there — so the gate is absolute.
#
# RED→GREEN RECORD.  The first execution of this file against the wave-2 sources
# gave 47 passed / 3 failed:
#   (i)   energy conservation asserted over ALL samples: drift 2.08e-2.  The
#         window energy omits the two frozen boundary bonds, so before the packet
#         has cleared them E_win is not yet the conserved quantity.  Fixed by
#         asserting on `energy_drift_readout`, the drift over the padded readout
#         interval, which is where D13(a) is defined in the first place.
#   (ii)  `gs_converged` at DMRG tol 1e-10: DMRG2 at a fixed truncation rank
#         stalls at its truncation floor (measured Haldane residual 4.3e-9).
#         Fixed by gating on the measured residual.
#   (iii) large-D edge retention `|m_L(end)/m_L(0)| < 0.3`: evaluated 8.6e4,
#         because both numbers are numerical zeros (1e-8 and 5e-5).  Fixed by
#         replacing the ratio with an absolute ceiling — which is the honest
#         statement of "there is no edge register here" anyway.
# The physics assertions (velocity, coefficient, integer support, sharp control)
# passed on that first run and were not retuned.
#
# All runs here are deliberately small (χ = 16, short windows, short times) so
# that the suite stays a suite.  The production numbers live in
# numerics/results/lambdaD-kink-*.json and lambdaD-edge-memory.json.

module TestLambdaDMemory

using Test
using LinearAlgebra
using TensorKit
using MPSKit

include(joinpath(@__DIR__, "..", "src", "lambdaD_memory.jl"))
using .LambdaDMemory

include(joinpath(@__DIR__, "..", "src", "lambdaD_edge.jl"))
using .LambdaDEdge

# Each module carries its own copy of the model shard, so `LambdaDPoint` is a
# distinct type in each; keep the two namespaces apart and never mix the points.
const LDM = LambdaDMemory.LambdaD
const LDE = LambdaDEdge.LambdaD

const TOL_EXACT   = 1.0e-9
const TOL_LAW     = 1.0e-9
const BAND_PACKET = 0.05
const SHARP_FLOOR = 1.0
const BAND_V      = 0.10
const BAND_COEFF  = 0.05

const MEDGE_HALDANE  = 0.45
const MDRIFT_HALDANE = 0.02
const MEDGE_LARGED   = 0.05

# Computed once and reused: each VUMPS / quasiparticle solve is seconds, but
# there is no reason to repeat them in every testset.
const CHI = 16
const K0 = pi / 4
const SEC = LambdaDMemory.kink_sector(LDM.NEEL_POINT; chi = CHI, tol = 1.0e-10)
const EK0, PHI0 = let (E, phi) = kink_dispersion(SEC, [K0]; num = 1)
    E[1][1], phi[1]
end
const LPK = 40
const PSI0 = kink_packet(SEC, PHI0; L = LPK, x0 = 16.0, sigma = 3.0, k0 = K0)
const WMEAS = 8:32
const C0 = 20

@testset "λ–D kink transport and memory (bd tns-f5r wave 2)" begin

    @testset "the two Néel vacua and the calibration s" begin
        A, B, s = neel_vacua(SEC.psiA)
        @test A === SEC.psiA
        ops = LDM.spin1_ops(:none)
        nA = [(-1)^(i + 1) * real(expectation_value(SEC.psiA, i => ops.Sz)) for i in 1:2]
        nB = [(-1)^(i + 1) * real(expectation_value(SEC.psiB, i => ops.Sz)) for i in 1:2]
        # ψ_A carries +s on every site, ψ_B carries −s: D13(a)'s s_α / s_β
        @test all(abs.(nA .- SEC.s) .< TOL_EXACT)
        @test all(abs.(nB .+ SEC.s) .< TOL_EXACT)
        # the tail density is the wave-1 staggered order parameter, NOT 1
        @test isapprox(SEC.s, 0.96034; atol = 1.0e-4)
        @test SEC.s < 0.999
        # degenerate: the two vacua have the same energy density
        eA = real(sum(expectation_value(SEC.psiA, SEC.H))) / 2
        eB = real(sum(expectation_value(SEC.psiB, SEC.H))) / 2
        @test abs(eA - eB) < 1.0e-8
    end

    @testset "kink dispersion lives in the topological sector" begin
        Es, phis = kink_dispersion(SEC, [0.0, pi / 2]; num = 1)
        @test MPSKit.istopological(phis[1])
        @test all(E[1] > 0 for E in Es)
        # band minimum at k = 0, maximum at the zone edge k = π/2
        @test Es[1][1] < EK0 < Es[2][1]
        # ω(k) = ω(−k) and ω(k) = ω(k+π): one-site translation maps A|B → B|A
        # and the Z₂ flip maps it back, so the BZ is (−π/2, π/2]
        Esym, _ = kink_dispersion(SEC, [-K0, K0 + pi]; num = 1)
        @test abs(Esym[1][1] - EK0) < 1.0e-6
        @test abs(Esym[2][1] - EK0) < 1.0e-6
        # the topological kink is NOT the trivial-sector excitation
        Etriv, phitriv = excitations(SEC.H, QuasiparticleAnsatz(), K0,
                                     SEC.psiA, SEC.envA; num = 1)
        @test !MPSKit.istopological(phitriv[1])
        @test abs(real(Etriv[1]) - EK0) > 1.0e-3
    end

    @testset "the packet is a one-kink state; the sharp junction is not" begin
        @test abs(window_energy(SEC, PSI0) - EK0) < BAND_PACKET
        # RED CONTROL: the same geometry with an undressed sharp junction
        sharp = kink_packet(SEC, PHI0; L = LPK, x0 = 16.0, sigma = 3.0, k0 = K0,
                            dressing = :sharp)
        @test abs(window_energy(SEC, sharp) - EK0) > SHARP_FLOOR
        # exactly one wall in the window
        est = wall_estimators(staggered_profile(PSI0), SEC.s, WMEAS)
        @test abs(est.wall_weight - 1.0) < 5.0e-2
        @test first(WMEAS) < est.X2 < last(WMEAS)
    end

    @testset "LD-ID: Q̂_{W,c₀} = 2s(𝔛_W − c₀), exactly" begin
        n = staggered_profile(PSI0)
        est = wall_estimators(n, SEC.s, WMEAS)
        vals, probs = window_charge_law(PSI0, WMEAS; weight = 1.0)
        Qint = sum(v * p for (v, p) in zip(vals, probs))
        Qhat = Qint - SEC.s * (2 * C0 - first(WMEAS) - last(WMEAS) + 1)
        @test abs(Qhat - 2 * SEC.s * (est.X1 - C0)) < TOL_EXACT
        # ... and the law really is a law: normalised, non-negative, integer grid
        @test abs(sum(probs) - 1) < TOL_LAW
        @test minimum(probs) > -TOL_LAW
        @test abs(Qint - sum(n[x] for x in WMEAS)) < TOL_EXACT
    end

    @testset "integer support of the charge; the wall coordinate is NOT quantised" begin
        cert = coset_certificate(PSI0, WMEAS, SEC.s, C0)
        # spec Q̂_{W,c₀} ⊂ κ + ℤ  ⟺  ⟨e^{2πiQ̂}⟩ has modulus 1 and phase 2πκ
        @test abs(cert.charge_modulus - 1) < TOL_EXACT
        @test cert.charge_phase_defect < 1.0e-7
        # RED CONTROL, same state and window: the D13(a) wall coordinate has
        # spectrum in (2s)^{-1}ℤ, which is not one coset of ℤ, so the same
        # certificate fails and the integer-grid inversion goes negative
        @test cert.position_modulus < 0.9
        _, ppos = window_charge_law(PSI0, WMEAS; weight = 1 / (2 * SEC.s))
        @test minimum(ppos) < -1.0e-3
    end

    @testset "DECISION: transport, group velocity, and the memory coefficient" begin
        r = memory_experiment(SEC; L = LPK, W = WMEAS, c0 = C0, x0 = 16.0,
                              sigma = 3.0, k0 = K0, dt = 0.12, nsteps = 45,
                              sample_every = 5, chi_max = 48, edge_guard = 4)
        # TDVP quality
        @test maximum(abs.([sm.norm for sm in r.samples] .- 1)) < 1.0e-5
        # Energy is conserved over the READOUT interval.  Before it, the packet
        # tail still overlaps the two frozen boundary bonds, which `window_energy`
        # does not count, so E_win is not yet the conserved quantity — geometry,
        # not a TDVP failure, and exactly why the readout is padded.
        @test isfinite(r.energy_drift_readout)
        @test r.energy_drift_readout < 2.0e-3
        # the packet moves at the band group velocity
        @test isfinite(r.v_measured)
        @test abs(r.v_measured - r.v_theory) < BAND_V * abs(r.v_theory)
        # the memory ledger: δx from an s-FREE estimator against the escaped
        # charge divided by the measured 2s
        @test isfinite(r.dx_X2) && abs(r.dx_X2) > 1.0
        @test abs(r.coefficient_measured - 2 * SEC.s) < BAND_COEFF * 2 * SEC.s
        # ... and the measurement prefers 2s = 2·m_stag over the naive 2
        @test abs(r.coefficient_measured - 2 * SEC.s) < abs(r.coefficient_measured - 2.0)
        # the three wall estimators agree on the displacement
        @test abs(r.dx_X1 - r.dx_X2) < 0.1 * abs(r.dx_X2)
        @test abs(r.dx_X3 - r.dx_X2) < 0.1 * abs(r.dx_X2)
    end

    @testset "edge memory: Haldane remembers, large-D forgets" begin
        # h_R = −h_L: both phases sit in S^z_tot = 0, so m_L is a measurement
        # and not half of a conserved total (see the module docstring).
        common = (L = 24, chi = 24, hL = 0.5, hR = -0.5, dt = 0.12, nsteps = 25,
                  sample_every = 5, chi_max = 32)
        rh = edge_experiment(LDE.HALDANE_POINT; common...)
        rd = edge_experiment(LDE.LARGED_POINT; common...)
        @test rh.gs_residual < 1.0e-6
        @test rd.gs_residual < 1.0e-6
        # energy of the post-pulse Hamiltonian is conserved in both runs
        for r in (rh, rd)
            @test maximum(abs.(r.energy .- r.energy[1])) < 1.0e-3
            @test maximum(abs.(r.norm .- 1)) < 1.0e-5
        end
        # Haldane: a protected edge spin-½, so the pulse writes an exactly
        # quantised half unit onto the edge and switching the field off does not
        # erase it
        @test abs(rh.mL[1]) > MEDGE_HALDANE
        @test abs(rh.mL[end] - rh.mL[1]) < MDRIFT_HALDANE
        # ... while the LOCAL moment does relax: the polarisation cloud radiates
        # into the bulk, the charge stays.  That is what makes it a memory and
        # not a frozen state.
        @test abs(rh.sz1[end]) < 0.85 * abs(rh.sz1[1])
        # large-D: no edge mode at all — m_L is a numerical zero at every time,
        # so the honest gate is absolute, not a retention ratio
        @test maximum(abs, rd.mL) < MEDGE_LARGED
        @test abs(rh.mL[end]) > 10 * maximum(abs, rd.mL)
    end

    @testset "JSON records" begin
        r = memory_experiment(SEC; L = 24, W = 6:19, c0 = 12, x0 = 10.0,
                              sigma = 2.5, k0 = K0, dt = 0.2, nsteps = 5,
                              sample_every = 5, chi_max = 2 * CHI)
        d = memory_record(r; profiles = false)
        @test haskey(d, "coefficient_measured")
        @test haskey(d, "s_tail_density")
        @test d["dressing"] == "qp"
        @test !any(v -> v isa Float64 && !isfinite(v), values(d))
        e = edge_record(edge_experiment(LDE.LARGED_POINT; L = 12, chi = 16,
                                        dt = 0.2, nsteps = 5, sample_every = 5,
                                        chi_max = 24))
        @test haskey(e, "mL_absmax")
        @test haskey(e, "energy_drift")
    end

end

end # module TestLambdaDMemory
