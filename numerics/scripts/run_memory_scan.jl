# run_memory_scan.jl — WP N2a first physics scan.
#
#   julia --project=numerics numerics/scripts/run_memory_scan.jl
#
# Writes numerics/results/memory-scan-1.json, rewriting the file after EVERY run
# so that a partial scan is still a usable artifact.  See
# numerics/docs/kink-sector-notes.md for conventions and for the definitions of
# every quantity recorded here.

using TriangleMPS
using Printf
using Dates

const OUT = joinpath(@__DIR__, "..", "results", "memory-scan-1.json")

const runs = Tuple{String,MemoryResult}[]

function write_results()
    open(OUT, "w") do io
        println(io, "{")
        println(io, "\"generated\": \"", Dates.format(now(), "yyyy-mm-ddTHH:MM:SS"), "\",")
        println(io, "\"work_package\": \"N2a\",")
        println(io, "\"model\": \"easy-axis spin-1/2 XXZ ferromagnet, frozen boundary spins (up on site 1, down on site N); H = -sum_x [ (Jperp/2)(S+S- + h.c.) + Jz Sz Sz ], Delta = Jz/Jperp > 1, Jperp = 1\",")
        println(io, "\"notes\": \"see numerics/docs/kink-sector-notes.md for all definitions; kink positions are physical-site BOND coordinates x+1/2; dx1 = windowed gradient centroid, dx2 = windowed integrated magnetisation, dx3 = magnetisation zero crossing (quantised, diagnostic only)\",")
        println(io, "\"nruns\": ", length(runs), ",")
        println(io, "\"runs\": [")
        for (i, (label, r)) in enumerate(runs)
            print(io, "{\"label\": \"", label, "\", \"result\": ", to_json(r; trajectory=false), "}")
            println(io, i == length(runs) ? "" : ",")
        end
        j = findfirst(x -> x[1] == "main-D2.0-k1.2", runs)
        if j === nothing
            println(io, "]")
        else
            println(io, "],")
            println(io, "\"trajectory_example\": ", to_json(runs[j][2]; trajectory=true))
        end
        println(io, "}")
    end
end

function run!(label; kwargs...)
    t = @elapsed r = memory_experiment(; kwargs...)
    push!(runs, (label, r))
    @printf("%-22s N=%3d D=%5.2f k0=%.2f dw=%d dim=%6d dx1=%+7.4f dx2=%+7.4f dx3=%+7.4f T=%.5f R=%.5f trap=%.2e |dx1+2T|=%.4f (%.0f s)\n",
            label, r.params.N, r.params.Delta, r.params.k0, r.params.dwmax, r.dim,
            r.dx1, r.dx2, r.dx3, r.T_final, r.R_final, r.trapped_final,
            abs(r.dx1 + 2 * r.T_final), t)
    flush(stdout)
    write_results()
    return r
end

# ---- main scan: Delta = 2 and 3, N = 160, four momenta --------------------
# sigma is chosen so the packet's momentum spread 1/(2 sigma) stays well below
# k0 itself; otherwise the slow (small-k) components never leave the wall.
const KS = ((0.4, 8.0), (0.8, 6.0), (1.2, 6.0), (1.8, 6.0))
for Δ in (2.0, 3.0), (k0, σ) in KS
    run!("main-D$(Δ)-k$(k0)"; N=160, Delta=Δ, k0=k0, sigma=σ,
         standoff=36.0, dt=0.4, obs_every=2)
end

# ---- N-convergence at fixed physics ---------------------------------------
for N in (120, 160, 200)
    run!("Nconv-$(N)"; N=N, Delta=2.0, k0=1.2, sigma=6.0,
         standoff=30.0, dt=0.4, obs_every=2)
end

# ---- Delta dependence at fixed k0 (Delta = 2 is in the main scan) ----------
for Δ in (1.5, 3.0, 6.0, 12.0)
    run!("Dscan-$(Δ)"; N=160, Delta=Δ, k0=1.2, sigma=6.0,
         standoff=36.0, dt=0.4, obs_every=2)
end

# ---- state-preparation check: sharp vs dressed (main-D2.0-k1.2) kink ------
run!("prep-sharp"; N=160, Delta=2.0, k0=1.2, sigma=6.0, standoff=36.0,
     dt=0.4, obs_every=2, kink_state=:sharp)

# ---- Ising limit ----------------------------------------------------------
run!("ising-Jperp0"; N=160, Delta=3.0, Jperp=1e-8, k0=1.2, sigma=6.0,
     standoff=36.0, dt=1.0, tmax=40.0, obs_every=2, kink_state=:sharp)

# ---- truncation check: dwmax = 3 vs 5 (expensive; run last) ---------------
for dw in (3, 5), Δ in (2.0, 3.0)
    run!("trunc-dw$(dw)-D$(Δ)"; N=56, Delta=Δ, k0=1.2, sigma=2.5,
         standoff=14.0, dt=0.25, dwmax=dw, halfwidth=5, buffer=5,
         kink_state=:sharp, obs_every=2, trapped_tol=1e-3)
end

@printf("\nwrote %s (%d runs)\n", OUT, length(runs))
