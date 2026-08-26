"""
    SpinSMemory

Exact sparse-sector numerics for the magnon-through-kink memory effect on the
easy-axis spin-`S` XXZ ferromagnet, for arbitrary `S`.  Falsifier (B) of
Conjecture Bc (theory/TRIANGLE.md §4, bd `tns-8e9`): Theorem M-quant gives
`δx = -N_T/s`, so the spin-1 chain must return `-1` site per transmitted
magnon where spin-1/2 returns `-2`.

Two shards (L2), included here:

    spins_memory_sector.jl   chain, up-variation truncation, sector basis,
                             sparse H, wall/transmission observables, states
    spins_memory_run.jl      the wavepacket-through-kink protocol, the
                             trajectory fit, and the JSON results record

Conventions, the `D`-truncation and the estimators are documented at the top of
`spins_memory_sector.jl`; the protocol is documented at the top of
`spins_memory_run.jl`.  Nothing here is redefined from `notation.md` /
`definitions.md`.
"""
module SpinSMemory

using LinearAlgebra
using SparseArrays
using KrylovKit
using Printf

export SpinChain, nsites_dynamical, Jz_of, phys_site_s, frozen_left_s, frozen_right_s
export magnon_dispersion_s, magnon_velocity_s, updown_variation, ising_energy_s
export SectorBasisS, sector_basis_s, config, build_hamiltonian_s, truncation_leakage_s
export sz_profile_s, kink_position_centroid, kink_position_integrated,
       kink_position_crossing, magnon_weights_s, magnon_centroid
export sector_ground_state_s, monotone_kink_config, free_magnon_state_s,
       magnon_wavepacket_s, magnon_wavepacket_leakage_s, krylov_evolve
export trajectory_offset, MemoryResultS, memory_experiment_s, to_json

include("spins_memory_sector.jl")
include("spins_memory_run.jl")

end # module
