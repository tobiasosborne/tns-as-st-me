#!/usr/bin/env python3
"""Standalone numerical checks for the Corner A shards (revision r2).

Backs the r1-critic objections that were CONCEDED and the repairs that replaced
them.  No repo dependency; numpy only.  Run:  python3 corner_a_check.py

Reference tensor: A = (I,X,Y,Z)/2 on d=4, chi=2.  Its transfer channel is
depolarising, so E(1)=1 (canonical form l=1), E(r)=r with r=I/2, lambda_E=0,
and one site is already injective.  Z_2 symmetry u(g)=diag(1,-1,-1,1) satisfies
D2's convention  U(g)A^s = V^{-1} A^s V  with V=Z, theta=0.

Checks (each PASS/FAIL against a tolerance fixed here, not after the fact):
  C1  WI telescopes with V^{-1} on the LEFT edge bond and V on the RIGHT edge
      bond  (confirms D2 orientation; the HANDOFF brief line 42 has it flipped).
  C2  WI FAILS on Lambda = R unless the edge insertions are allowed
      (r1 objection 1) and HOLDS once they are (D1(e) revision r2).
  C3  Lemma SBP: the summation-by-parts identity with its two boundary terms is
      exact for an arbitrary profile (r1 objection 13; replaces the false
      "Phi_k(N_k(X)) = 0" finite-window claim).
  C4  D12(a): for a decaying (c_0) profile the boundary remainder -> 0 in norm.
  C5  D12(b): for a plane wave the remainder is Theta(1) while the bulk grows
      like |Lambda|^{1/2}, so the identity holds only after |Lambda|^{-1/2}.
  C6  A1(c): omega^{M@b} = omega^{M'@b}  iff  M' in C^* M  (r1 objection 5:
      normalisation matters; phases and positive scalars are invisible).
  C7  D9(d): the double coset H\\G/H (relative angle) is the diagonal invariant
      of a vacuum pair, while g_L g_R^{-1} is NOT (r1 objection 11).
"""
import numpy as np

TOL_EXACT = 1e-12
np.random.seed(7)

I2 = np.eye(2, dtype=complex)
X = np.array([[0, 1], [1, 0]], dtype=complex)
Y = np.array([[0, -1j], [1j, 0]])
Z = np.diag([1, -1]).astype(complex)
A = [I2 / 2, X / 2, Y / 2, Z / 2]
D, CHI = 4, 2
K = -1j * Z / 2                      # anti-Hermitian virtual generator
U = np.diag([1, -1, -1, 1]).astype(complex)
V = Z

bl = np.random.randn(2) + 1j * np.random.randn(2)
br = np.random.randn(2) + 1j * np.random.randn(2)
LB = np.kron(bl.conj(), bl)
RB = np.kron(br, br.conj())
TSITE = sum(np.kron(a, a.conj()) for a in A)

results = []


def report(name, ok, detail=""):
    results.append(ok)
    print(f"{'PASS' if ok else 'FAIL'}  {name}   {detail}")


# ---------------------------------------------------------------- transfer
def slots(L, ins=None, Ml=None, Mr=None):
    """[Ml, site0, bond0, site1, bond1, ..., site_{L-1}, bond_{L-1}]."""
    out = [Ml if Ml is not None else I2]
    for x in range(L):
        out.append("site")
        m = ins[x] if (ins and x in ins) else I2
        if x == L - 1 and Mr is not None:
            m = Mr
        out.append(m)
    return out


def ov(ket, bra):
    T = np.eye(CHI * CHI, dtype=complex)
    for a1, a2 in zip(ket, bra):
        T = T @ (TSITE if isinstance(a1, str) else np.kron(a1, a2.conj()))
    return LB @ T @ RB


def nrm(terms):
    s = 0
    for ci, ki in terms:
        for cj, kj in terms:
            s += ci * np.conj(cj) * ov(ki, kj)
    return np.sqrt(max(np.real(s), 0.0))


# ---------------------------------------------- explicit small state vectors
import itertools


def vec(tensors, Ml=None, Mr=None, bondins=None):
    L = len(tensors)
    out = np.zeros(D ** L, dtype=complex)
    for idx, s in enumerate(itertools.product(range(D), repeat=L)):
        M = np.eye(CHI, dtype=complex)
        if Ml is not None:
            M = M @ Ml
        for x in range(L):
            M = M @ tensors[x][s[x]]
            if bondins and x in bondins:
                M = M @ bondins[x]
        if Mr is not None:
            M = M @ Mr
        out[idx] = bl.conj() @ M @ br
    return out


def apply_u(psi, L, sites):
    T = psi.reshape([D] * L)
    for x in sites:
        T = np.tensordot(U, T, axes=([1], [x]))
        T = np.moveaxis(T, 0, x)
    return T.reshape(-1)


print("Setup:", "E unital:", np.allclose(sum(a @ I2 @ a.conj().T for a in A), I2),
      "| E(r)=r:", np.allclose(sum(a @ (I2 / 2) @ a.conj().T for a in A), I2 / 2),
      "| IT holds:", all(np.allclose(sum(U[sp, s] * A[s] for s in range(D)),
                                     np.linalg.inv(V) @ A[sp] @ V) for sp in range(D)))
print()

# C1 --------------------------------------------------------------------
# The Z_2 example has V = Z = V^{-1} and is therefore BLIND to the orientation
# of the two edge insertions.  (The r1 critic's check had the same blind spot.)
# Use a U(1) symmetry with V = exp(i t Z/2), for which V != V^{-1}.
SIG = [I2, X, Y, Z]


def u_of(t):
    """u(t)_{s s'} = tr(sigma_{s'} V^{-1} sigma_s V)/2 realises D2's
    Sum_{s'} u_{s s'} A^{s'} = V(t)^{-1} A^s V(t)."""
    Vt = np.array([[np.exp(1j * t / 2), 0], [0, np.exp(-1j * t / 2)]], dtype=complex)
    Vi = np.linalg.inv(Vt)
    return np.array([[np.trace(SIG[sp] @ Vi @ SIG[s] @ Vt) / 2
                      for sp in range(4)] for s in range(4)]), Vt


TT = 0.7
UT, VT = u_of(TT)
ok_u = np.allclose(UT @ UT.conj().T, np.eye(4))
ok_it = all(np.allclose(sum(UT[s, sp] * A[sp] for sp in range(D)),
                        np.linalg.inv(VT) @ A[s] @ VT) for s in range(D))
report("C0  U(1) example: u(t) unitary and satisfies D2's (IT) with V=exp(itZ/2)",
       ok_u and ok_it, f"V != V^-1: {np.abs(VT - np.linalg.inv(VT)).max():.3f}")


def apply_ut(psi, L, sites, umat):
    T = psi.reshape([D] * L)
    for x in sites:
        T = np.tensordot(umat, T, axes=([1], [x]))
        T = np.moveaxis(T, 0, x)
    return T.reshape(-1)


L = 4
lhs = apply_ut(vec([A] * L), L, [1, 2], UT)
rhs = vec([A] * L, bondins={0: np.linalg.inv(VT), 2: VT})
flip = vec([A] * L, bondins={0: VT, 2: np.linalg.inv(VT)})
e1, e1f = np.abs(lhs - rhs).max(), np.abs(lhs - flip).max()
report("C1  WI telescoping: V^{-1} on the LEFT edge bond, V on the RIGHT",
       e1 < TOL_EXACT, f"err={e1:.2e}")
report("C1b WI with the opposite (HANDOFF line-42) orientation is WRONG",
       e1f > 1e-6, f"err={e1f:.4f}")
# the Z_2 tensor also telescopes (orientation-blind there, V=Z=V^{-1})
lhsZ = apply_u(vec([A] * L), L, [1, 2], )
report("C1c Z_2 example telescopes too (but cannot fix orientation: V=Z=V^{-1})",
       np.abs(lhsZ - vec([A] * L, bondins={0: np.linalg.inv(V), 2: V})).max() < TOL_EXACT,
       f"|V - V^-1| = {np.abs(V - np.linalg.inv(V)).max():.1f}")

# C2 --------------------------------------------------------------------
psi2 = vec([A] * 2)
lhs2 = apply_u(psi2, 2, [0, 1])
bad = np.abs(lhs2 - psi2).max()
good = np.abs(lhs2 - vec([A] * 2, Ml=np.linalg.inv(V), Mr=V)).max()
report("C2  Lambda=R: r1 form of WI FAILS ...", bad > 1e-6, f"err={bad:.4f}")
report("C2b ... and HOLDS with D1(e)-r2 edge insertions", good < TOL_EXACT,
       f"err={good:.2e}")

# C3 --------------------------------------------------------------------
def sbp(f, L=4):
    lhs = np.zeros(D ** L, dtype=complex)
    for n in range(L):
        t = [A] * L
        t[n] = [A[s] @ K - K @ A[s] for s in range(D)]
        lhs = lhs + f(n) * vec(t)
    bulk = -sum((f(m + 1) - f(m)) * vec([A] * L, bondins={m: K}) for m in range(L - 1))
    bdry = f(L - 1) * vec([A] * L, Mr=K) - f(0) * vec([A] * L, Ml=K)
    return np.abs(lhs - (bulk + bdry)).max()


k = 0.37
e3a = sbp(lambda n: np.exp(1j * k * n))
e3b = sbp(lambda n: 1.0 / (1 + n) ** 2)
report("C3  Lemma SBP exact with its two boundary terms (plane wave + generic)",
       max(e3a, e3b) < TOL_EXACT, f"err={max(e3a, e3b):.2e}")

# null direction: equals the boundary terms, NOT zero
Bn = [np.exp(1j * k) * A[s] @ K - K @ A[s] for s in range(D)]
Phi = np.zeros(D ** 4, dtype=complex)
for n in range(4):
    t = [A] * 4
    t[n] = Bn
    Phi = Phi + np.exp(1j * k * n) * vec(t)
bt = np.exp(1j * k * 4) * vec([A] * 4, Mr=K) - vec([A] * 4, Ml=K)
report("C3b Phi_k(N_k(X)) equals the 2 boundary terms and is NONZERO",
       np.abs(Phi - bt).max() < TOL_EXACT and np.linalg.norm(Phi) > 1e-6,
       f"||Phi||={np.linalg.norm(Phi):.4f}, match={np.abs(Phi - bt).max():.2e}")

# C4 / C5 ---------------------------------------------------------------
print("\n  L   |  c_0 profile (1+|n-c|)^-3        |  plane wave k=0.37")
print("      |  ||bdry||   ||bulk||   ratio     |  ||bdry||   ||bulk||   ratio")
ratios_c0, bdry_pw, bulk_pw = [], [], []
for L in (4, 8, 16, 32):
    c = (L - 1) / 2
    f = lambda n, c=c: 1.0 / (1 + abs(n - c)) ** 3
    bulk = [(-(f(m + 1) - f(m)), slots(L, ins={m: K})) for m in range(L - 1)]
    bdry = [(f(L - 1), slots(L, Mr=K)), (-f(0), slots(L, Ml=K))]
    nb, nk = nrm(bdry), nrm(bulk)
    ratios_c0.append(nb / nk)
    g = lambda n: np.exp(1j * k * n)
    bulkg = [(-(g(m + 1) - g(m)), slots(L, ins={m: K})) for m in range(L - 1)]
    bdryg = [(g(L - 1), slots(L, Mr=K)), (-g(0), slots(L, Ml=K))]
    nbg, nkg = nrm(bdryg), nrm(bulkg)
    bdry_pw.append(nbg)
    bulk_pw.append(nkg)
    print(f"  {L:3d} |  {nb:.3e}  {nk:.3e}  {nb/nk:.3e} |  {nbg:7.4f}  {nkg:8.4f}  {nbg/nkg:.4f}")

report("C4  D12(a): c_0 profile -> boundary remainder vanishes in norm",
       ratios_c0[-1] < 1e-2 and ratios_c0[-1] < ratios_c0[0] / 100,
       f"ratio {ratios_c0[0]:.2e} -> {ratios_c0[-1]:.2e}")
report("C5  D12(b): plane wave -> boundary Theta(1), bulk grows ~ sqrt(L)",
       max(bdry_pw) < 5 and bulk_pw[-1] > 2.5 * bulk_pw[0] / 2.5,
       f"bdry in [{min(bdry_pw):.2f},{max(bdry_pw):.2f}], bulk {bulk_pw[0]:.2f} -> {bulk_pw[-1]:.2f}")

# C6 --------------------------------------------------------------------
L = 9


def fid(M, Mp):
    a, b = slots(L, ins={4: M}), slots(L, ins={4: Mp})
    return abs(ov(a, b)) ** 2 / (np.real(ov(a, a)) * np.real(ov(b, b)))


ok6 = (abs(fid(I2, 2.9j * I2) - 1) < 1e-10 and abs(fid(Z, 0.4 * Z) - 1) < 1e-10
       and fid(I2, Z) < 1e-10 and fid(I2, X) < 1e-10 and fid(Z, X) < 1e-10
       and abs(fid(Z, X + 2 * Z) - 1) > 1e-3)
report("C6  A1(c): omega^{M@b}=omega^{M'@b} iff M' in C^* M", ok6,
       f"fid(I,cI)={fid(I2, 2.9j*I2):.6f}, fid(I,Z)={fid(I2, Z):.2e}, "
       f"fid(Z,0.4Z)={fid(Z, 0.4*Z):.6f}, fid(Z,X+2Z)={fid(Z, X+2*Z):.4f}")

# C7 --------------------------------------------------------------------
rng = np.random.default_rng(3)


def rand_su2():
    a = rng.normal(size=4)
    a /= np.linalg.norm(a)
    return a[0] * I2 + 1j * (a[1] * X + a[2] * Y + a[3] * Z)


def nvec(g):
    return np.array([np.real(np.trace(g @ Z @ g.conj().T @ P)) / 2 for P in (X, Y, Z)])


gL, gR, h = rand_su2(), rand_su2(), rand_su2()
c1 = np.dot(nvec(gL), nvec(gR))
c2 = np.dot(nvec(h @ gL), nvec(h @ gR))
w = gL @ np.linalg.inv(gR)
noninv = np.abs(w - h @ w @ np.linalg.inv(h)).max()
report("C7  D9(d): relative angle (double coset) IS diagonal-invariant, "
       "g_L g_R^{-1} is NOT",
       abs(c1 - c2) < 1e-12 and noninv > 1e-3,
       f"|cos1-cos2|={abs(c1-c2):.1e}, |w - hwh^-1|={noninv:.4f}")

print()
print("ALL PASS" if all(results) else "SOME CHECKS FAILED")
raise SystemExit(0 if all(results) else 1)
