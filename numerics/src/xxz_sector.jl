"""
xxz_sector.jl — exact S^z-sector enumeration and sparse Hamiltonians for the
easy-axis (Δ > 1) spin-1/2 XXZ ferromagnet with frozen boundary spins.

CONVENTIONS (stated once here and in numerics/docs/kink-sector-notes.md; used
consistently everywhere in the numerics package):

    H = - Σ_{x=1}^{N-1} [ (J_⊥/2)(S⁺_x S⁻_{x+1} + S⁻_x S⁺_{x+1}) + J_z S^z_x S^z_{x+1} ]
      = - J_⊥ Σ_x (S^x_x S^x_{x+1} + S^y_x S^y_{x+1}) - J_z Σ_x S^z_x S^z_{x+1},

with J_⊥ > 0, Δ := J_z / J_⊥ > 1.  Both signs are ferromagnetic, so |↑…↑⟩ and
|↓…↓⟩ are exact ground states; the easy axis is z.

Sites x = 1…N.  Sites 1 and N carry FROZEN classical spins (this is the
boundary-field implementation of the kink boundary condition): they contribute
their Ising bonds to sites 2 and N-1 but cannot flip.  Consequently the hopping
term acts only on bonds between two dynamical sites, x = 2 … N-2, and the total
S^z of the L = N-2 dynamical sites is exactly conserved.

    boundary = :kink →  σ_1 = ↑, σ_N = ↓   (one-kink boundary condition)
    boundary = :up   →  σ_1 = σ_N = ↑      (ferromagnetic reference chain)

A dynamical configuration is a `BitVector` of length L, `true` = ↑.
"""

const _SPIN_UP = 1
const _SPIN_DOWN = -1

"""
    XXZChain(N; Jperp=1.0, Delta=2.0, boundary=:kink)

Easy-axis XXZ ferromagnet on `N` sites with frozen boundary spins.
"""
struct XXZChain
    N::Int
    Jperp::Float64
    Delta::Float64
    boundary::Symbol
    function XXZChain(N::Int; Jperp::Real=1.0, Delta::Real=2.0, boundary::Symbol=:kink)
        N >= 4 || throw(ArgumentError("need N >= 4 (two frozen + at least two dynamical sites)"))
        boundary in (:kink, :up) || throw(ArgumentError("boundary must be :kink or :up"))
        Jperp > 0 || throw(ArgumentError("Jperp must be positive"))
        new(N, float(Jperp), float(Delta), boundary)
    end
end

"Number of dynamical (flippable) sites, L = N - 2."
nsites_dynamical(ch::XXZChain) = ch.N - 2

"Ising coupling J_z = Δ J_⊥."
Jz(ch::XXZChain) = ch.Delta * ch.Jperp

"Frozen spin (±1) on site 1."
frozen_left(::XXZChain) = _SPIN_UP

"Frozen spin (±1) on site N."
frozen_right(ch::XXZChain) = ch.boundary === :kink ? _SPIN_DOWN : _SPIN_UP

"Physical site index (1…N) of dynamical site j (1…L)."
phys_site(::XXZChain, j::Int) = j + 1

"""
    magnon_dispersion(ch, k) = J_z - J_⊥ cos k

Single-magnon energy above the ferromagnetic vacuum on the all-up chain, in the
conventions above.  Gapped for Δ > 1 with gap J_⊥(Δ - 1) at k = 0.
"""
magnon_dispersion(ch::XXZChain, k::Real) = Jz(ch) - ch.Jperp * cos(k)

"""
    magnon_velocity(ch, k) = dω/dk = J_⊥ sin k

Group velocity; positive for k ∈ (0, π), i.e. e^{ikx} packets move to the right.
"""
magnon_velocity(ch::XXZChain, k::Real) = ch.Jperp * sin(k)

"Spin (±1) at physical site x for dynamical configuration `c`."
@inline function spin_at(ch::XXZChain, c::BitVector, x::Int)
    x == 1 && return frozen_left(ch)
    x == ch.N && return frozen_right(ch)
    return c[x-1] ? _SPIN_UP : _SPIN_DOWN
end

"Number of down spins among the dynamical sites."
ndown(c::BitVector) = count(!, c)

"""
    domain_walls(ch, c)

Number of bonds (x, x+1), x = 1…N-1, across which the spin flips (frozen
boundary spins included).  For `boundary = :kink` this is always odd.
"""
function domain_walls(ch::XXZChain, c::BitVector)
    w = 0
    for x in 1:(ch.N-1)
        spin_at(ch, c, x) == spin_at(ch, c, x + 1) || (w += 1)
    end
    return w
end

"""
    ising_energy(ch, c) = -J_z Σ_x S^z_x S^z_{x+1}

Diagonal part of `H` on configuration `c` (frozen bonds included).
"""
function ising_energy(ch::XXZChain, c::BitVector)
    jz = Jz(ch)
    e = 0.0
    for x in 1:(ch.N-1)
        e -= jz * (spin_at(ch, c, x) / 2) * (spin_at(ch, c, x + 1) / 2)
    end
    return e
end

"""
    sharp_kink_config(ch, n)

The unique single-domain-wall configuration with `n` down spins on a `:kink`
chain: dynamical sites 1…L-n up, L-n+1…L down.  The wall sits on the bond
between physical sites (L-n+1, L-n+2), i.e. at kink coordinate `L - n` in the
dynamical labelling used by the position estimators.
"""
function sharp_kink_config(ch::XXZChain, n::Int)
    L = nsites_dynamical(ch)
    0 <= n <= L || throw(ArgumentError("ndown out of range"))
    c = trues(L)
    for j in (L-n+1):L
        c[j] = false
    end
    return c
end

"""
    kink_position_of_sector(ch, n) = L - n

Dynamical coordinate of the sharp kink in the `n`-down-spin sector.  Because a
single-domain-wall configuration is unique inside each S^z sector, the sharp
kink position is rigidly tied to the sector label; every dynamical displacement
of the kink is therefore accompanied by a rearrangement of magnon content.
"""
kink_position_of_sector(ch::XXZChain, n::Int) = nsites_dynamical(ch) - n

# ---------------------------------------------------------------------------
# Basis enumeration
# ---------------------------------------------------------------------------

"""
    SectorBasis

Ordered basis of the S^z eigenspace with `ndown` down spins, optionally
truncated to configurations with at most `dwmax` domain walls
(`dwmax = nothing` ⇒ the full, exact sector).  `configs` is sorted so the basis
is deterministic; `index` is the inverse map.
"""
struct SectorBasis
    chain::XXZChain
    ndown::Int
    dwmax::Union{Int,Nothing}
    configs::Vector{BitVector}
    index::Dict{BitVector,Int}
end

Base.length(b::SectorBasis) = length(b.configs)

"All configurations of L dynamical sites with exactly n down spins."
function _enumerate_full(L::Int, n::Int)
    out = Vector{BitVector}()
    c = trues(L)
    function rec(j::Int, remaining::Int)
        if remaining == 0
            push!(out, copy(c))
            return
        end
        L - j + 1 < remaining && return
        for p in j:(L-remaining+1)
            c[p] = false
            rec(p + 1, remaining - 1)
            c[p] = true
        end
        return
    end
    rec(1, n)
    return out
end

"""
Block-wise recursive enumeration of configurations with a fixed number of down
spins and at most `dwmax` domain walls.  Complexity is O(#configs · L) rather
than O(2^L): blocks are laid down left to right and the running down-spin count
prunes branches that can no longer reach the target.
"""
function _enumerate_dw(ch::XXZChain, n::Int, dwmax::Int)
    N = ch.N
    L = N - 2
    sL = frozen_left(ch)
    sR = frozen_right(ch)
    out = Vector{BitVector}()
    spins = Vector{Int}(undef, N)

    # down-spin count contributed by dynamical sites in x1:x2 with spin s
    @inline function block_downs(s::Int, x1::Int, x2::Int)
        s == _SPIN_UP && return 0
        lo = max(x1, 2)
        hi = min(x2, N - 1)
        return max(0, hi - lo + 1)
    end

    @inline function emit!()
        c = falses(L)
        for j in 1:L
            c[j] = spins[j+1] == _SPIN_UP
        end
        push!(out, c)
        return
    end

    # sites 1..x-1 already written; the block starting at x has spin s
    function rec(x::Int, s::Int, downs::Int, walls::Int)
        # closing option: run this block all the way to site N
        if s == sR
            d = downs + block_downs(s, x, N)
            if d == n
                for y in x:N
                    spins[y] = s
                end
                emit!()
            end
        end
        walls == dwmax && return
        # otherwise end the block at e < N and place a wall on bond (e, e+1);
        # the block is grown one site at a time so each node costs O(1)
        for e in x:(N-1)
            spins[e] = s
            d = downs + block_downs(s, x, e)
            rem = max(0, (N - 1) - e)          # dynamical sites still to come
            need = n - d
            need < 0 && break                  # d only grows with e
            need > rem && continue
            rec(e + 1, -s, d, walls + 1)
        end
        return
    end

    spins[1] = sL
    rec(1, sL, 0, 0)
    return out
end

"""
    sector_basis(ch; ndown, dwmax=nothing)

Enumerate the S^z sector with `ndown` down spins on the dynamical sites.  With
`dwmax` given, keep only configurations with at most that many domain walls
(`dwmax = 1`: the bare kink; `dwmax = 3`: kink + one magnon; `dwmax = 5`:
kink + two magnons).  The truncation is a projection, never an approximation to
the enumeration itself — see the notes file for its physical justification.
"""
function sector_basis(ch::XXZChain; ndown::Int, dwmax::Union{Int,Nothing}=nothing)
    L = nsites_dynamical(ch)
    0 <= ndown <= L || throw(ArgumentError("ndown must lie in 0:$L"))
    configs = if dwmax === nothing
        _enumerate_full(L, ndown)
    else
        _enumerate_dw(ch, ndown, dwmax)
    end
    sort!(configs)
    index = Dict{BitVector,Int}()
    sizehint!(index, length(configs))
    for (i, c) in enumerate(configs)
        index[c] = i
    end
    return SectorBasis(ch, ndown, dwmax, configs, index)
end

# ---------------------------------------------------------------------------
# Sparse Hamiltonian
# ---------------------------------------------------------------------------

"""
    build_hamiltonian(b::SectorBasis) -> SparseMatrixCSC{Float64,Int}

Sparse matrix of `H` restricted to `b`.  For an untruncated basis this is exact
(the sector is invariant under `H`).  For a `dwmax`-truncated basis it is the
projected operator `P H P`, which is still Hermitian, so unitarity and energy
conservation of the time evolution are exact.
"""
function build_hamiltonian(b::SectorBasis)
    ch = b.chain
    L = nsites_dynamical(ch)
    dim = length(b)
    rows = Int[]
    cols = Int[]
    vals = Float64[]
    sizehint!(rows, 3 * dim)
    sizehint!(cols, 3 * dim)
    sizehint!(vals, 3 * dim)
    hop = -ch.Jperp / 2
    d = falses(L)
    for (i, c) in enumerate(b.configs)
        push!(rows, i); push!(cols, i); push!(vals, ising_energy(ch, c))
        for j in 1:(L-1)
            c[j] == c[j+1] && continue
            copyto!(d, c)
            d[j], d[j+1] = c[j+1], c[j]
            k = get(b.index, d, 0)
            k == 0 && continue          # truncated away: P H P drops the element
            push!(rows, k); push!(cols, i); push!(vals, hop)
        end
    end
    return sparse(rows, cols, vals, dim, dim)
end

"""
    truncation_leakage(b::SectorBasis) -> Float64

Frobenius norm of the matrix elements that `build_hamiltonian` discards because
the target configuration falls outside a truncated basis.  Zero for an
untruncated basis; a direct diagnostic of how much of `H` the `dwmax` cut
removes.
"""
function truncation_leakage(b::SectorBasis)
    b.dwmax === nothing && return 0.0
    ch = b.chain
    L = nsites_dynamical(ch)
    acc = 0.0
    d = falses(L)
    for c in b.configs
        for j in 1:(L-1)
            c[j] == c[j+1] && continue
            copyto!(d, c)
            d[j], d[j+1] = c[j+1], c[j]
            haskey(b.index, d) || (acc += (ch.Jperp / 2)^2)
        end
    end
    return sqrt(acc)
end
