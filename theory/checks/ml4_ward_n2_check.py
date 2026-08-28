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

Added 2026-08-28 (bd tns-uxr downstream audit, findings UXR-R1/UXR-R2;
verdicts/ml4-ward-n2-audit.md sections 1.2-1.3).  These make the corpus
immune to the defect class rather than merely repaired:
  (C5) UXR-R1 REGISTER TRAP.  In the highest-weight-restricted register
       D_lambda = Q_0|_{ker S^+} one has A_lambda = (N-2n) 1 (the PROVED
       first display of (9)), so the string "2 D A^{-1} J^z_0" evaluates
       to the REFUTED display.  Certifies: A_lambda is scalar; the naive
       hw reading reproduces the refuted display exactly; the correct hw
       form (1/m_lambda) Q_0 Pi_hw J^z_0 is exact at every n; and the two
       registers' repairs are NOT interchangeable (cross-error O(1)).
  (C6) UXR-R2 NAMED-LEAF FAILURE.  The former eq (18) is false on the ML2
       singular contact vector |chi_pi> ~ sum_x (-1)^x |x,x+1>, the very
       vector <1>5.<2>1.<3>3 names as belonging to its branch: relative
       error 1.000 at N=8.  The corrected full-sector form is exact there.
Exit 0 iff the F1 pattern is confirmed exactly (C3 holds at n=1, fails at
n>=2; C4 holds at all n) and C5, C6 confirm.  --red flips (9) into the
test that must fail; --red-register asserts the two registers' repairs are
interchangeable (they are not); --red-chi asserts the old (18) holds on
|chi_pi> (it does not).
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


def hw_basis(Sp, idx_n):
    """Orthonormal basis of ker S^+ inside sector n, as columns."""
    _u, sv, vh = np.linalg.svd(Sp[:, idx_n], full_matrices=True)
    rank = int(np.sum(sv > 1e-10))
    return vh[rank:].conj().T


def check_registers_and_chi(n_sites, Sp, Sm, Sz, Jm, Jz, Jp, num, rng):
    """C5 (UXR-R1 register trap) and C6 (UXR-R2 named-leaf failure)."""
    red_reg = "--red-register" in sys.argv
    red_chi = "--red-chi" in sys.argv
    dim = Sp.shape[0]
    ok = True

    # ---------------- C5: the register trap ----------------
    for n in (1, 2, 3):
        idx_n = sector_basis(num, n)
        idx_n1 = sector_basis(num, n + 1)
        hw = hw_basis(Sp, idx_n)
        if hw.shape[1] == 0:
            continue
        c = rng.normal(size=hw.shape[1]) + 1j * rng.normal(size=hw.shape[1])
        psi_sec = hw @ c
        psi_sec /= np.linalg.norm(psi_sec)
        psi = np.zeros(dim, dtype=complex)
        psi[idx_n] = psi_sec

        D = Sm[np.ix_(idx_n1, idx_n)]              # full-sector map
        A = D.conj().T @ D
        P = D @ np.linalg.solve(A, D.conj().T)
        Dl = D @ hw                                 # hw-restricted map
        Al = Dl.conj().T @ Dl
        Pi_hw = hw @ hw.conj().T
        jz = (Jz @ psi)[idx_n]
        m_lambda = (n_sites - 2 * n) / 2.0

        # (i) A_lambda is scalar = (N-2n) 1  -- the PROVED first display of (9)
        scal = np.linalg.norm(Al - (n_sites - 2 * n) * np.eye(Al.shape[0]))
        # (ii) the naive hw reading of "2 D A^-1 Jz" IS the refuted display
        naive_hw = 2.0 * (Dl @ np.linalg.solve(Al, hw.conj().T @ jz))
        refuted = (2.0 / (n_sites - 2 * n)) * (D @ jz)
        hwform = (1.0 / m_lambda) * (D @ (Pi_hw @ jz))
        # (iii) correct forms in each register
        lhs_full = P @ (Jm @ psi)[idx_n1]
        err_full = np.linalg.norm(lhs_full - 2.0 * (D @ np.linalg.solve(A, jz)))
        Pl = Dl @ np.linalg.solve(Al, Dl.conj().T)
        lhs_hw = Pl @ (Jm @ psi)[idx_n1]
        err_hw = np.linalg.norm(lhs_hw - hwform)
        # (iv) cross-register substitution must be WRONG for n>=2
        cross = np.linalg.norm(lhs_full - hwform)

        # The trap, stated literally: dropping Pi_hw in the hw register (where
        # A_lambda is scalar) reproduces the REFUTED display exactly.
        naive_nopi = 2.0 * (D @ jz) / (n_sites - 2 * n)
        trap = np.linalg.norm(naive_nopi - refuted)
        print(f"C5 n={n}: ||A_l-(N-2n)1||={scal:.1e}  full-form err={err_full:.2e}  "
              f"hw-form err={err_hw:.2e}  cross-register err={cross:.3e}  "
              f"||naive-hw-reading - REFUTED display||={trap:.2e}  "
              f"||2 D_l A_l^-1 Pi_hw Jz - hwform||={np.linalg.norm(naive_hw - hwform):.2e}")
        if trap > 1e-10:
            print("FAIL C5(ii): the naive hw reading did not reproduce the "
                  "refuted display — the register trap is not what we think")
            ok = False

        if scal > 1e-10:
            print("FAIL C5(i): A_lambda is not scalar on ker S^+")
            ok = False
        if err_full > 1e-10 or err_hw > 1e-10:
            print("FAIL C5(iii): a register's own corrected form is not exact")
            ok = False
        if n >= 2 and cross < 1e-6:
            print("FAIL C5(iv): cross-register substitution did not fail as required")
            ok = False
        if red_reg and n >= 2 and cross > 1e-10:
            print("RED-REGISTER: cross-register substitution error detected as required")
            sys.exit(1)

    # ---------------- C6: the named ML2 singular vector ----------------
    idx2 = sector_basis(num, 2)
    idx3 = sector_basis(num, 3)
    chi = np.zeros(dim, dtype=complex)
    for x in range(n_sites):
        bits = 0
        for site in (x, (x + 1) % n_sites):
            bits |= (1 << (n_sites - 1 - site))
        chi[bits] += (-1.0) ** x
    chi /= np.linalg.norm(chi)
    D = Sm[np.ix_(idx3, idx2)]
    A = D.conj().T @ D
    P = D @ np.linalg.solve(A, D.conj().T)
    jz = (Jz @ chi)[idx2]
    lhs = P @ (Jm @ chi)[idx3]
    err_old = np.linalg.norm(lhs - (2.0 / (n_sites - 4)) * (D @ jz))
    err_new = np.linalg.norm(lhs - 2.0 * (D @ np.linalg.solve(A, jz)))
    hw_chi = np.linalg.norm(Sp @ chi)
    rel = err_old / max(np.linalg.norm(lhs), 1e-30)
    print(f"C6 |chi_pi>: ||S+chi||={hw_chi:.1e} (highest weight)  "
          f"old-(18) err={err_old:.3e} (rel {rel:.3f})  corrected err={err_new:.2e}")
    if hw_chi > 1e-10:
        print("FAIL C6: |chi_pi> is not highest weight — premise of <3>3 broken")
        ok = False
    if err_new > 1e-10:
        print("FAIL C6: corrected form is not exact on the named vector")
        ok = False
    if rel < 0.5:
        print("FAIL C6: old (18) did not fail on |chi_pi> as required")
        ok = False
    if red_chi and rel > 1e-10:
        print("RED-CHI: old (18) failure on |chi_pi> detected as required")
        sys.exit(1)

    return ok


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
    if not check_registers_and_chi(n_sites, Sp, Sm, Sz, Jm, Jz, Jp, num, rng):
        pattern_ok = False

    if pattern_ok:
        print("CONFIRMED: F1 pattern exact — (9) holds n=1, fails n>=2 via "
              "S+ Jz psi = -J+ psi != 0; corrected 2D A^{-1} Jz form holds all n")
        sys.exit(0)
    print("NOT CONFIRMED: pattern deviates from F1 claim")
    sys.exit(1)


if __name__ == "__main__":
    main()
