module TriangleMPS

# Campaign numerics: uniform MPS + excitation ansatz for the lattice infrared
# triangle. Shards (L2, 200-500 loc each) are included here as they land.

using LinearAlgebra
using SparseArrays
using KrylovKit
using Printf
using Dates

# --- WP N2a: exact sparse-sector numerics for the kink/magnon memory effect ---
export XXZChain, SectorBasis, sector_basis, build_hamiltonian
export domain_walls, ising_energy, sharp_kink_config, kink_position_of_sector
export magnon_dispersion, magnon_velocity, truncation_leakage
export sz_profile, kink_position, kink_position_centroid, kink_position_integrated
export kink_position_crossing, magnon_weights, krylov_evolve, evolve_trajectory
export magnon_wavepacket_leakage, density_centroid
export sector_ground_state, magnon_wavepacket, free_magnon_state
export MemoryResult, memory_experiment, trajectory_offset, to_json

include("xxz_sector.jl")
include("xxz_dynamics.jl")
include("memory_experiment.jl")

end # module
