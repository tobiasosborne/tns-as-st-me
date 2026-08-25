# Generates the space-time data for Fig. 3(a): a magnon wavepacket crossing
# the XXZ kink, recorded as sz_profile(x,t) + the crossing-estimator wall
# trajectory. Parameters mirror the committed scan run main-D3.0-k1.2
# (numerics/results/memory-scan-1.json) so the figure shows a run whose
# delta-x and T are independently on record.
using Pkg; Pkg.activate(joinpath(@__DIR__, "..", "..", "numerics"))
using TriangleMPS
using LinearAlgebra

N, Delta, Jperp, k0, sigma, standoff, dwmax = 160, 3.0, 1.0, 1.2, 8.0, 36.0, 3
dt, obs_every = 0.4, 2

ch = XXZChain(N; Jperp=Jperp, Delta=Delta, boundary=:kink)
L = N - 2
n = div(L, 2)
Xk0 = float(L - n) + 1.5
x0 = Xk0 - standoff

bk = sector_basis(ch; ndown=n, dwmax=dwmax)
_, psik = sector_ground_state(bk)
b = sector_basis(ch; ndown=n + 1, dwmax=dwmax)
psi0 = magnon_wavepacket(b, bk, psik; k0=k0, x0=x0, sigma=sigma)
H = build_hamiltonian(b)

v = magnon_velocity(ch, k0)
tc = standoff / abs(v)
nsteps = ceil(Int, 2.6 * tc / dt)

frames = Vector{Vector{Float64}}()
walls = Float64[]
times = Float64[]
step = Ref(0)
evolve_trajectory(H, ComplexF64.(psi0), dt, nsteps) do t, psi
    if step[] % obs_every == 0
        m = sz_profile(b, psi)
        push!(frames, m)
        push!(walls, kink_position_crossing(m; window=(Int(round(Xk0)) - 40):(Int(round(Xk0)) + 40)))
        push!(times, t)
    end
    step[] += 1
    nothing
end

open(joinpath(@__DIR__, "profile-D3.0-k1.2.json"), "w") do io
    write(io, "{\n\"params\": {\"N\": $N, \"Delta\": $Delta, \"Jperp\": $Jperp, \"k0\": $k0, \"sigma\": $sigma, \"standoff\": $standoff, \"dwmax\": $dwmax, \"dt\": $dt, \"obs_every\": $obs_every, \"x0\": $x0, \"Xkink0\": $Xk0, \"tcollision\": $tc},\n")
    write(io, "\"t\": [" * join(times, ",") * "],\n")
    write(io, "\"wall\": [" * join(walls, ",") * "],\n")
    write(io, "\"sz\": [")
    for (i, m) in enumerate(frames)
        write(io, "[" * join(round.(m; digits=6), ",") * "]")
        i < length(frames) && write(io, ",")
    end
    write(io, "]\n}\n")
end
println("wrote ", length(frames), " frames, tc=", tc, ", nsteps=", nsteps)
