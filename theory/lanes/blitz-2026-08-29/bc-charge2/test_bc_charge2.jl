using Test
using LinearAlgebra
using Printf

include(joinpath(@__DIR__, "BcCharge2ED.jl"))
using .BcCharge2ED

# Pre-registered before the production implementation or any three-magnon run.
# D6 fixes s=1/2 and the hard bound state carries |q_hard|=2, hence Bc predicts
# |q_hard|/s = 4.  The absolute 0.35 window is deliberately wider than the
# charge-1 shard's 5% window because this first charge-2 ED oracle has both a
# finite packet and an exponentially small but nonzero channel-overlap error.
const PREDICTED_SLOPE = 4.0
const DECISION_ATOL = 0.35
const MAX_REPORTED_ERROR = 0.35
const RED = "--red" in ARGS

# Independent dense 2^N oracle, deliberately not expressed in occupation
# hopping rules.  It restricts the tensor-product spin Hamiltonian to n_down=3.
function brute_three_spectrum(N::Int, J::Float64)
    sx = ComplexF64[0 1; 1 0]/2
    sy = ComplexF64[0 -im; im 0]/2
    sz = ComplexF64[1 0; 0 -1]/2
    id = Matrix{ComplexF64}(I,2,2)
    function onsite(op,x)
        A = ones(ComplexF64,1,1)
        for y in 1:N
            A = kron(A, y == x ? op : id)
        end
        return A
    end
    xs = [onsite(sx,x) for x in 1:N]
    ys = [onsite(sy,x) for x in 1:N]
    zs = [onsite(sz,x) for x in 1:N]
    H = zeros(ComplexF64,2^N,2^N)
    for x in 1:N
        y = mod1(x+1,N)
        H .-= J .* (xs[x]*xs[y] + ys[x]*ys[y] + zs[x]*zs[y] - I/4)
    end
    idx = [m+1 for m in 0:2^N-1 if count_ones(m) == 3]
    return eigvals(Hermitian(H[idx,idx]))
end

@testset "Bc charge-2 three-magnon ED decision" begin
    @testset "O(N^3) sector layer vs dense spin oracle" begin
        N, J = 6, 0.83
        tb = three_basis(N)
        @test length(tb.states) == binomial(N,3)
        H3 = three_magnon_hamiltonian(tb,J; hopping_scale=RED ? 1.08 : 1.0)
        @test norm(H3-adjoint(H3)) < 1e-13
        @test maximum(abs.(sort(eigvals(Hermitian(Matrix(H3)))) .-
                            sort(brute_three_spectrum(N,J)))) < 1e-10
    end
    @test isapprox(fused_phase_slope(pi/2),PREDICTED_SLOPE;atol=1e-8)
    result = measured_charge2_slope()
    @test isfinite(result.slope)
    @test isfinite(result.stderr)
    @test abs(result.slope - PREDICTED_SLOPE) <= DECISION_ATOL
    @test result.stderr <= MAX_REPORTED_ERROR
    @test minimum(r.transmission for r in result.rows) > 0.95
    @test maximum(max(r.norm_drift,r.free_norm_drift) for r in result.rows) < 1e-7
    @printf("\n[Bc charge-2] ED slope = %.8f +/- %.8f; prediction 2/s = %.1f; N=%d dim=%d min_transmission=%.6f\n",
            result.slope,result.stderr,PREDICTED_SLOPE,result.rows[1].N,result.dim,
            minimum(r.transmission for r in result.rows))
    @printf("[Bc charge-2] symmetrized finite-k slopes: %.8f at |k|=.06, %.8f at |k|=.10; fused Bethe limit %.12f\n",
            result.symmetric[1],result.symmetric[2],result.bethe_slope)
end
