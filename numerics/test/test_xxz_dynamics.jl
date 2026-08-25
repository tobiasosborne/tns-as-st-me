using Test
using LinearAlgebra
using SparseArrays
using TriangleMPS

@testset "xxz_dynamics" begin

    @testset "sz_profile on basis states" begin
        ch = XXZChain(12; Jperp=1.0, Delta=3.0, boundary=:kink)
        b = sector_basis(ch; ndown=4)
        c = sharp_kink_config(ch, 4)
        ψ = zeros(ComplexF64, length(b)); ψ[b.index[c]] = 1.0
        m = sz_profile(b, ψ)
        @test length(m) == ch.N
        @test m[1] ≈ 0.5              # frozen left
        @test m[end] ≈ -0.5           # frozen right
        L = TriangleMPS.nsites_dynamical(ch)
        @test all(m[x] ≈ 0.5 for x in 1:(L-4+1))
        @test all(m[x] ≈ -0.5 for x in (L-4+2):ch.N)
        @test sum(m) ≈ 0.5 * ch.N - (4 + 1)   # frozen right site is down too
    end

    @testset "position estimators are exact on sharp kinks" begin
        ch = XXZChain(24; Jperp=1.0, Delta=5.0, boundary=:kink)
        L = TriangleMPS.nsites_dynamical(ch)
        for n in 4:(L-4)
            c = sharp_kink_config(ch, n)
            b = sector_basis(ch; ndown=n, dwmax=1)
            ψ = zeros(ComplexF64, 1); ψ[1] = 1.0
            m = sz_profile(b, ψ)
            X0 = L - n + 1.5                    # wall bond, physical coordinates
            w = (max(1, floor(Int, X0) - 6), min(ch.N, ceil(Int, X0) + 6))
            @test kink_position_centroid(m; window=w) ≈ X0
            @test kink_position_integrated(m; window=w) ≈ X0
            @test kink_position_crossing(m; window=w) ≈ X0
        end
    end

    @testset "estimators on a two-branch kink mixture are linear in the weights" begin
        # synthetic profile: incoherent mixture of a sharp kink at bond a+0.5
        # and one at bond a-1.5, with weights 1-p and p.
        N = 40; a = 20
        step(X) = [x < X ? 0.5 : -0.5 for x in 1:N]
        w = (a - 8, a + 8)
        for p in (0.0, 0.2, 0.5, 0.9, 1.0)
            m = (1 - p) .* step(a + 0.5) .+ p .* step(a - 1.5)
            @test kink_position_centroid(m; window=w) ≈ (a + 0.5) - 2p
            @test kink_position_integrated(m; window=w) ≈ (a + 0.5) - 2p
        end
        # the zero-crossing estimator is deliberately inequivalent: it is quantised
        m = 0.4 .* step(a + 0.5) .+ 0.6 .* step(a - 1.5)
        @test abs(kink_position_crossing(m; window=w) - (a - 1.5)) < 0.51   # quantised: jumps to the transmitted branch
    end

    @testset "magnon transmission / reflection weights" begin
        ch = XXZChain(40; Jperp=1.0, Delta=3.0, boundary=:kink)
        L = TriangleMPS.nsites_dynamical(ch)
        n = 19
        # reflected branch: kink at L-n, one extra down spin far to the left
        c = sharp_kink_config(ch, n); c[5] = false
        b = sector_basis(ch; ndown=n + 1, dwmax=3)
        ψ = zeros(ComplexF64, length(b)); ψ[b.index[c]] = 1.0
        m = sz_profile(b, ψ)
        Xref = L - n + 1.5
        tw = magnon_weights(m; kink_ref=Xref, buffer=6)
        @test tw.R ≈ 1.0 atol = 1e-12
        @test tw.T ≈ 0.0 atol = 1e-12
        # transmitted branch: kink two sites left, one up spin far to the right
        c2 = sharp_kink_config(ch, n + 2); c2[L-4] = true
        @test count(!, c2) == n + 1
        ψ2 = zeros(ComplexF64, length(b)); ψ2[b.index[c2]] = 1.0
        m2 = sz_profile(b, ψ2)
        tw2 = magnon_weights(m2; kink_ref=Xref, buffer=6)
        @test tw2.T ≈ 1.0 atol = 1e-12
        @test tw2.R ≈ 0.0 atol = 1e-12
        # and the kink really did move by -2
        w = (round(Int, Xref) - 6, round(Int, Xref) + 6)
        @test kink_position_centroid(m2; window=w) ≈ Xref - 2
    end

    @testset "free magnon wavepacket moves at the group velocity" begin
        ch = XXZChain(120; Jperp=1.0, Delta=2.0, boundary=:up)
        b = sector_basis(ch; ndown=1)
        @test length(b) == ch.N - 2
        H = build_hamiltonian(b)
        for k0 in (0.6, 1.0, 1.8)
            ψ0 = free_magnon_state(b; k0=k0, x0=30.0, sigma=8.0)
            @test abs(norm(ψ0) - 1) < 1e-14
            X0 = TriangleMPS.density_centroid(sz_profile(b, ψ0))
            @test abs(X0 - 30.0) < 0.05
            T = 40.0
            ψT = krylov_evolve(H, ψ0, T)
            XT = TriangleMPS.density_centroid(sz_profile(b, ψT))
            v = magnon_velocity(ch, k0)
            @test abs((XT - X0) - v * T) < 0.02 * abs(v * T)
        end
    end

    @testset "norm and energy conservation" begin
        ch = XXZChain(80; Jperp=1.0, Delta=2.5, boundary=:kink)
        L = TriangleMPS.nsites_dynamical(ch)
        n = div(L, 2)
        bk = sector_basis(ch; ndown=n, dwmax=3)
        _, ψk = sector_ground_state(bk)
        b = sector_basis(ch; ndown=n + 1, dwmax=3)
        ψ0 = magnon_wavepacket(b, bk, ψk; k0=1.1, x0=15.0, sigma=6.0)
        @test abs(norm(ψ0) - 1) < 1e-13
        H = build_hamiltonian(b)
        E0 = real(dot(ψ0, H * ψ0))
        rec = evolve_trajectory(H, ψ0, 0.5, 40) do t, ψ
            (t=t, nrm=norm(ψ), E=real(dot(ψ, H * ψ)))
        end
        @test length(rec) == 41
        @test maximum(abs(r.nrm - 1) for r in rec) < 1e-12
        @test maximum(abs(r.E - E0) for r in rec) < 1e-10
    end

    @testset "wavepacket recipe: momentum content and localisation" begin
        ch = XXZChain(80; Jperp=1.0, Delta=2.5, boundary=:kink)
        L = TriangleMPS.nsites_dynamical(ch)
        n = div(L, 2)
        bk = sector_basis(ch; ndown=n, dwmax=3)
        _, ψk = sector_ground_state(bk)
        b = sector_basis(ch; ndown=n + 1, dwmax=3)
        k0, x0, σ = 1.2, 14.0, 6.0
        ψ0 = magnon_wavepacket(b, bk, ψk; k0=k0, x0=x0, sigma=σ)
        m = sz_profile(b, ψ0)
        Xk = L - n + 1.5
        tw = magnon_weights(m; kink_ref=Xk, buffer=8)
        @test tw.R > 0.99                     # magnon starts entirely on the up side
        # its energy sits within the one-magnon band above the bare kink energy
        H = build_hamiltonian(b)
        E = real(dot(ψ0, H * ψ0))
        Ek, _ = sector_ground_state(sector_basis(ch; ndown=n + 1, dwmax=1))
        ω = E - Ek
        @test abs(ω - magnon_dispersion(ch, k0)) < 0.25
    end
end
