"""Independent confirmation of S1-B verdict F1 against ML4-Ward (9).

Full 2^N Hilbert space, spin-1/2 XXX ring, operators built directly from
Pauli matrices (independent of theory/checks/ml4_check.py's sector blocks
and of the critic's scratch script).

Convention (from the corpus checker / D10): bond current density
  j^a_x = (J/2)(S^a_{x+1} - S^a_x) P_{x,x+1},   J^a_0 = sum_x j^a_x.
Q_0 = S^- (total lowering).  D_{n,N} = S^- restricted to the n-magnon
sector; P_{n,N} = orthogonal projection onto ran D_{n,N} in the (n+1)-
magnon sector.

Claims tested, for random highest-weight psi in sector n:
  (C1) [S^+, J^-_0] = 2 J^z_0                       (eq (8) commutator - sanity)
  (C2) S^+ J^z_0 psi = -J^+_0 psi; zero iff n=1     (the F1 mechanism)
  (C3) eq (9):  P J^-_0 psi = (2/(N-2n)) S^- J^z_0 psi   -- expected FALSE n>=2
  (C4) corrected: P J^-_0 psi = 2 D A^{-1} J^z_0 psi with A = D†D on the
       FULL n-sector                                 -- expected TRUE all n
Exit 0 iff the F1 pattern is confirmed exactly (C3 holds at n=1, fails at
n>=2; C4 holds at all n).  --red flips (9) into the test that must fail.
"""
import sys
import numpy as np

J = 1.0


def kron_at(op, site, n_sites):
    mats = [np.eye(2)] * n_sites
    mats[site] = op
    out = np.array([[1.0]])
    for m in mats:
        out = np.kron(out, m)
    return out


def build(n_sites):
    sp = np.array([[0, 1], [0, 0]], dtype=complex)   # S^+
    sm = sp.T.conj()
    sz = np.diag([0.5, -0.5]).astype(complex)
    dim = 2 ** n_sites
    Sp = sum(kron_at(sp, i, n_sites) for i in range(n_sites))
    Sm = Sp.T.conj()
    Sz = sum(kron_at(sz, i, n_sites) for i in range(n_sites))
    # swap P_{x,x+1} = 2 S_x.S_{x+1} + 1/2
    def swap(x):
        y = (x + 1) % n_sites
        sdots = (kron_at(sp, x, n_sites) @ kron_at(sm, y, n_sites)
                 + kron_at(sm, x, n_sites) @ kron_at(sp, y, n_sites)) / 2.0 \
                + kron_at(sz, x, n_sites) @ kron_at(sz, y, n_sites)
        return 2.0 * sdots + 0.5 * np.eye(dim)
    Jm = np.zeros((dim, dim), dtype=complex)
    Jz = np.zeros((dim, dim), dtype=complex)
    Jp = np.zeros((dim, dim), dtype=complex)
    for x in range(n_sites):
        y = (x + 1) % n_sites
        P = swap(x)
        Jm += (J / 2.0) * (kron_at(sm, y, n_sites) - kron_at(sm, x, n_sites)) @ P
        Jz += (J / 2.0) * (kron_at(sz, y, n_sites) - kron_at(sz, x, n_sites)) @ P
        Jp += (J / 2.0) * (kron_at(sp, y, n_sites) - kron_at(sp, x, n_sites)) @ P
    # number operator n = N/2 - S^z
    num = n_sites / 2.0 * np.eye(dim) - Sz
    return Sp, Sm, Sz, Jm, Jz, Jp, num


def sector_basis(num, n):
    vals = np.round(np.diag(num).real).astype(int)
    return np.where(vals == n)[0]


def main():
    red = "--red" in sys.argv
    rng = np.random.default_rng(20260828)
    n_sites = 8
    Sp, Sm, Sz, Jm, Jz, Jp, num = build(n_sites)
    dim = Sp.shape[0]

    # (C1) commutator sanity
    c1 = np.linalg.norm(Sp @ Jm - Jm @ Sp - 2.0 * Jz)
    if c1 > 1e-12:
        print(f"FAIL C1: [S+,J-0]-2Jz0 norm {c1:.2e}")
        sys.exit(1)
    print(f"C1 OK: ||[S+,J-0]-2Jz0|| = {c1:.2e}")

    pattern_ok = True
    for n in (1, 2, 3):
        idx_n = sector_basis(num, n)
        idx_n1 = sector_basis(num, n + 1)
        # hw subspace: ker S+ within sector n
        Sp_n = Sp[:, idx_n]
        ns = np.linalg.svd(Sp_n)  # null space via svd of the map from sector n
        # columns of V spanning null space of Sp restricted
        u, s, vh = np.linalg.svd(Sp[:, idx_n], full_matrices=True)
        rank = np.sum(s > 1e-10)
        hw = vh[rank:].conj().T           # (len(idx_n), n_hw)
        n_hw = hw.shape[1]
        if n_hw == 0:
            print(f"n={n}: no hw states, skip")
            continue
        # random hw vector, embedded in full space
        coeff = rng.normal(size=n_hw) + 1j * rng.normal(size=n_hw)
        psi_sec = hw @ coeff
        psi_sec /= np.linalg.norm(psi_sec)
        psi = np.zeros(dim, dtype=complex)
        psi[idx_n] = psi_sec
        # verify hw
        assert_hw = np.linalg.norm(Sp @ psi)
        # D on full sector n: matrix of S^- from sector n to n+1
        D = Sm[np.ix_(idx_n1, idx_n)]
        A = D.conj().T @ D
        P = D @ np.linalg.solve(A, D.conj().T)   # projection onto ran D
        lhs_full = Jm @ psi
        lhs = P @ lhs_full[idx_n1]
        jzpsi = (Jz @ psi)[idx_n]
        rhs9 = (2.0 / (n_sites - 2 * n)) * (D @ jzpsi)
        rhs10 = 2.0 * (D @ np.linalg.solve(A, jzpsi))
        e9 = np.linalg.norm(lhs - rhs9)
        e10 = np.linalg.norm(lhs - rhs10)
        mech = np.linalg.norm((Sp @ Jz - Jz @ Sp) @ psi + Jp @ psi)
        leak = np.linalg.norm(Jp @ psi)
        print(f"n={n}: ||S+psi||={assert_hw:.1e}  eq(9) err={e9:.3e}  "
              f"corrected err={e10:.3e}  ||[S+,Jz]psi+J+psi||={mech:.1e}  "
              f"||J+_0 psi||={leak:.3e}  ||lhs||={np.linalg.norm(lhs):.3e}")
        if red:
            # red mode: pretend (9) is fine at every n -> must fail
            if n >= 2 and e9 > 1e-10:
                print("RED: eq(9) failure detected at n>=2 as required")
                sys.exit(1)
        else:
            if n == 1 and (e9 > 1e-10 or e10 > 1e-10):
                pattern_ok = False
            if n >= 2 and (e9 < 1e-6 or e10 > 1e-10 or leak < 1e-6):
                pattern_ok = False
        if mech > 1e-12:
            pattern_ok = False

    if red:
        print("RED FAILED: no eq(9) violation found")
        sys.exit(0)
    if pattern_ok:
        print("CONFIRMED: F1 pattern exact — (9) holds n=1, fails n>=2 via "
              "S+ Jz psi = -J+ psi != 0; corrected 2D A^{-1} Jz form holds all n")
        sys.exit(0)
    print("NOT CONFIRMED: pattern deviates from F1 claim")
    sys.exit(1)


if __name__ == "__main__":
    main()
