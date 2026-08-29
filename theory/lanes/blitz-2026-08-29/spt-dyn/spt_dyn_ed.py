#!/usr/bin/env python3
"""Charge-sector exact diagonalization for the spin-1 lambda-D chain.

Only small-chain evidence is claimed.  The implementation keeps exact total
S^z sectors, constructs the spin-1 Hamiltonian directly, and exposes the local
operators needed by the T0--T3 lane tests.
"""

from __future__ import annotations

from dataclasses import dataclass
from functools import lru_cache
from itertools import product

import numpy as np
import scipy.sparse as sp
import scipy.sparse.linalg as spla


SQRT2 = np.sqrt(2.0)


@dataclass(frozen=True)
class Sector:
    length: int
    magnetization: int
    states: np.ndarray
    codes: np.ndarray
    index: dict[int, int]
    powers: np.ndarray

    @property
    def dim(self) -> int:
        return int(self.states.shape[0])


@lru_cache(maxsize=None)
def sector(length: int, magnetization: int) -> Sector:
    rows = [m for m in product((-1, 0, 1), repeat=length) if sum(m) == magnetization]
    states = np.asarray(rows, dtype=np.int8)
    powers = np.asarray([3**x for x in range(length)], dtype=np.int64)
    codes = ((states.astype(np.int64) + 1) * powers[None, :]).sum(axis=1)
    return Sector(
        length=length,
        magnetization=magnetization,
        states=states,
        codes=codes,
        index={int(code): i for i, code in enumerate(codes)},
        powers=powers,
    )


def hamiltonian(
    sec: Sector,
    single_ion_D: float,
    *,
    periodic: bool = False,
    right_field: float = 0.0,
) -> sp.csr_matrix:
    """Return H=sum S.S + D sum Sz^2 - right_field Sz_(L-1)."""
    length = sec.length
    bonds = [(x, x + 1) for x in range(length - 1)]
    if periodic:
        bonds.append((length - 1, 0))

    diagonal = single_ion_D * np.sum(sec.states.astype(float) ** 2, axis=1)
    diagonal -= right_field * sec.states[:, -1]
    row: list[int] = list(range(sec.dim))
    col: list[int] = list(range(sec.dim))
    val: list[complex] = list(diagonal.astype(complex))

    for source, state in enumerate(sec.states):
        code = int(sec.codes[source])
        for left, right in bonds:
            ml = int(state[left])
            mr = int(state[right])
            val[source] += ml * mr
            if ml < 1 and mr > -1:
                target_code = code + int(sec.powers[left]) - int(sec.powers[right])
                row.append(sec.index[target_code])
                col.append(source)
                val.append(0.5 * np.sqrt(2 - ml * (ml + 1)) * np.sqrt(2 - mr * (mr - 1)))
            if ml > -1 and mr < 1:
                target_code = code - int(sec.powers[left]) + int(sec.powers[right])
                row.append(sec.index[target_code])
                col.append(source)
                val.append(0.5 * np.sqrt(2 - ml * (ml - 1)) * np.sqrt(2 - mr * (mr + 1)))

    matrix = sp.coo_matrix((val, (row, col)), shape=(sec.dim, sec.dim), dtype=complex)
    return matrix.tocsr()


def ground_state(matrix: sp.csr_matrix, *, tolerance: float = 2.0e-11) -> tuple[float, np.ndarray]:
    values, vectors = spla.eigsh(matrix, k=1, which="SA", tol=tolerance, maxiter=20000)
    state = vectors[:, 0]
    state /= np.linalg.norm(state)
    return float(values[0].real), state


def lowest_states(
    matrix: sp.csr_matrix, count: int = 2, *, tolerance: float = 2.0e-11
) -> tuple[np.ndarray, np.ndarray]:
    values, vectors = spla.eigsh(matrix, k=count, which="SA", tol=tolerance, maxiter=30000)
    order = np.argsort(values.real)
    return values[order].real, vectors[:, order]


def apply_raising(
    source: Sector,
    target: Sector,
    vector: np.ndarray,
    weights: np.ndarray,
) -> np.ndarray:
    if target.magnetization != source.magnetization + 1:
        raise ValueError("S+ target sector must have magnetization M+1")
    out = np.zeros(target.dim, dtype=complex)
    for source_i, state in enumerate(source.states):
        amplitude = vector[source_i]
        if amplitude == 0:
            continue
        code = int(source.codes[source_i])
        for x, weight in enumerate(weights):
            m = int(state[x])
            if weight != 0 and m < 1:
                target_i = target.index[code + int(source.powers[x])]
                out[target_i] += weight * np.sqrt(2 - m * (m + 1)) * amplitude
    return out


def apply_sz(sec: Sector, vector: np.ndarray, weights: np.ndarray) -> np.ndarray:
    diagonal = sec.states.astype(float) @ np.asarray(weights, dtype=complex)
    return diagonal * vector


def sz_profile(sec: Sector, vector: np.ndarray) -> np.ndarray:
    probabilities = np.abs(vector) ** 2
    return probabilities @ sec.states.astype(float)


def sz2_profile(sec: Sector, vector: np.ndarray) -> np.ndarray:
    probabilities = np.abs(vector) ** 2
    return probabilities @ (sec.states.astype(float) ** 2)


def expectation_diagonal(sec: Sector, vector: np.ndarray, weights: np.ndarray) -> float:
    return float(np.dot(sz_profile(sec, vector), np.asarray(weights).real))


def hermiticity_residue(matrix: sp.csr_matrix) -> float:
    defect = matrix - matrix.getH()
    return 0.0 if defect.nnz == 0 else float(np.max(np.abs(defect.data)))


def normalized(vector: np.ndarray) -> tuple[np.ndarray, float]:
    norm = float(np.linalg.norm(vector))
    if norm < 1.0e-14:
        raise ValueError("cannot normalize a zero vector")
    return vector / norm, norm


def gaussian_weights(
    length: int,
    center: float,
    sigma: float,
    momentum: float,
    *,
    support: tuple[int, int] | None = None,
) -> np.ndarray:
    x = np.arange(length, dtype=float)
    weights = np.exp(-0.5 * ((x - center) / sigma) ** 2 + 1j * momentum * x)
    if support is not None:
        lo, hi = support
        weights[:lo] = 0.0
        weights[hi:] = 0.0
    return weights


def evolve(matrix: sp.csr_matrix, vector: np.ndarray, times: np.ndarray) -> np.ndarray:
    if len(times) < 2 or abs(times[0]) > 1.0e-15:
        raise ValueError("times must start at zero and contain at least two points")
    return spla.expm_multiply(
        -1j * matrix,
        vector,
        start=0.0,
        stop=float(times[-1]),
        num=len(times),
        endpoint=True,
        traceA=complex(matrix.diagonal().sum()),
    )


def orthonormal_columns(vectors: np.ndarray, tolerance: float = 1.0e-10) -> np.ndarray:
    if vectors.size == 0:
        return np.zeros((vectors.shape[0], 0), dtype=complex)
    u, singular, _ = np.linalg.svd(vectors, full_matrices=False)
    keep = singular > tolerance * singular[0]
    return u[:, keep]


def exclusive_channel(primary: np.ndarray, candidate: np.ndarray) -> np.ndarray:
    """Candidate channel with its overlap with ``primary`` removed."""
    q_primary = orthonormal_columns(primary)
    residual = candidate - q_primary @ (q_primary.conj().T @ candidate)
    return orthonormal_columns(residual)
