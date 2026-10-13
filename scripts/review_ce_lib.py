"""R199 from-scratch library: even Clifford orders of ternary Z-lattices, exact arithmetic.

Independent of scripts/ce_*.  Elements of C(V) are dicts {bitmask: Fraction} in a Q-orthogonal basis f_1,f_2,f_3
(Gram-Schmidt of the classical Gram G).  C_0(L) has Z-basis 1, e1e2, e2e3, e1e3.
Orders are Z-lattices in the 4-dim even subalgebra, given by a 4x4 Fraction basis matrix (rows) in blade coordinates
(masks 0, 3, 6, 5).  All 2-power overorders are enumerated exactly as Lambda + H, H a subgroup of the 2-part of
Lambda^#/Lambda (Lambda^# = trace dual), so no ladder assumption is made.
"""
from fractions import Fraction as F
from itertools import product
import math

EVEN = [0, 3, 6, 5]  # 1, f1f2, f2f3, f1f3 blades


def _blade_mul(s, t, q):
    """f_S f_T = sign * prod_{i in S&T} q_i * f_{S^T}; bits: bit0 = f1, ..."""
    sign = 1
    # count swaps: for each bit in t, number of bits in s above it
    for i in range(3):
        if (t >> i) & 1:
            higher = s >> (i + 1)
            if bin(higher).count("1") % 2:
                sign = -sign
    c = F(sign)
    for i in range(3):
        if (s >> i) & 1 and (t >> i) & 1:
            c *= q[i]
    return c, s ^ t


class Cliff:
    def __init__(self, G):
        self.G = [[F(x) for x in r] for r in G]
        n = 3
        # Gram-Schmidt: f_k = e_k - sum_{j<k} mu_kj f_j ; record e_k in f-basis
        fvec = []  # f_k as combos of e
        q = []
        Ebasis = []  # e_k as combos of f
        B = lambda x, y: sum(x[i] * self.G[i][j] * y[j] for i in range(n) for j in range(n))
        for k in range(n):
            ek = [F(int(i == k)) for i in range(n)]
            v = ek[:]
            coef_f = [F(0)] * n
            for j in range(k):
                mu = B(ek, fvec[j]) / q[j]
                v = [v[i] - mu * fvec[j][i] for i in range(n)]
                coef_f[j] = mu
            coef_f[k] = F(1)
            fvec.append(v)
            q.append(B(v, v))
            Ebasis.append(coef_f)
        self.q = q
        self.e = [{1 << j: Ebasis[k][j] for j in range(n) if Ebasis[k][j] != 0} for k in range(n)]

    def mul(self, x, y):
        r = {}
        for s, a in x.items():
            for t, b in y.items():
                c, m = _blade_mul(s, t, self.q)
                r[m] = r.get(m, 0) + a * b * c
        return {m: c for m, c in r.items() if c != 0}

    def vec(self, x):
        return [F(x.get(m, 0)) for m in EVEN]

    def elt(self, v):
        return {m: F(c) for m, c in zip(EVEN, v) if c != 0}

    def c0_basis(self):
        e = self.e
        one = {0: F(1)}
        return [self.vec(one), self.vec(self.mul(e[0], e[1])), self.vec(self.mul(e[1], e[2])),
                self.vec(self.mul(e[0], e[2]))]

    def trd(self, v):
        return 2 * F(v[0])

    def conj(self, v):
        return [v[0], -v[1], -v[2], -v[3]]

    def nrd(self, v):
        x = self.elt(v)
        return F(self.mul(x, self.elt(self.conj(v))).get(0, 0))

    def vmul(self, u, v):
        return self.vec(self.mul(self.elt(u), self.elt(v)))


# ---------- exact linear algebra ----------
def det(M):
    M = [[F(x) for x in r] for r in M]
    n = len(M)
    d = F(1)
    for c in range(n):
        p = next((r for r in range(c, n) if M[r][c] != 0), None)
        if p is None:
            return F(0)
        if p != c:
            M[c], M[p] = M[p], M[c]
            d = -d
        d *= M[c][c]
        for r in range(c + 1, n):
            f = M[r][c] / M[c][c]
            M[r] = [M[r][i] - f * M[c][i] for i in range(n)]
    return d


def inv(M):
    n = len(M)
    A = [[F(x) for x in r] + [F(int(i == j)) for j in range(n)] for i, r in enumerate(M)]
    for c in range(n):
        p = next(r for r in range(c, n) if A[r][c] != 0)
        A[c], A[p] = A[p], A[c]
        pv = A[c][c]
        A[c] = [x / pv for x in A[c]]
        for r in range(n):
            if r != c and A[r][c] != 0:
                f = A[r][c]
                A[r] = [A[r][i] - f * A[c][i] for i in range(2 * n)]
    return [r[n:] for r in A]


def coords(B, v):
    """coordinates of v in row-basis B (v = c B)."""
    Bi = inv(B)
    return [sum(v[i] * Bi[i][j] for i in range(len(v))) for j in range(len(B))]


def hnf_key(B):
    """canonical key of the Z-lattice spanned by rows of B (Fraction): integer HNF of D*B."""
    D = 1
    for r in B:
        for x in r:
            D = D * x.denominator // math.gcd(D, x.denominator)
    M = [[int(x * D) for x in r] for r in B]
    M = hnf(M)
    return (D, tuple(tuple(r) for r in M))


def hnf(M):
    M = [r[:] for r in M]
    m, n = len(M), len(M[0])
    row = 0
    for col in range(n):
        # gcd-reduce column col among rows >= row
        while True:
            nz = [r for r in range(row, m) if M[r][col] != 0]
            if not nz:
                break
            piv = min(nz, key=lambda r: abs(M[r][col]))
            M[row], M[piv] = M[piv], M[row]
            done = True
            for r in range(row + 1, m):
                if M[r][col]:
                    f = M[r][col] // M[row][col]
                    M[r] = [M[r][i] - f * M[row][i] for i in range(n)]
                    if M[r][col]:
                        done = False
            if done:
                break
        if row < m and M[row][col] != 0:
            if M[row][col] < 0:
                M[row] = [-x for x in M[row]]
            for r in range(row):
                f = M[r][col] // M[row][col]
                M[r] = [M[r][i] - f * M[row][i] for i in range(n)]
            row += 1
    return [r for r in M if any(r)]


def lattice_basis_from_gens(gens):
    """Z-basis (Fraction rows) of the lattice generated by gens (full rank 4)."""
    D = 1
    for r in gens:
        for x in r:
            D = D * F(x).denominator // math.gcd(D, F(x).denominator)
    M = hnf([[int(F(x) * D) for x in r] for r in gens])
    return [[F(x, D) for x in r] for r in M]


# ---------- orders ----------
def is_order(C, B):
    Bi = inv(B)
    one = [F(1), F(0), F(0), F(0)]
    c1 = [sum(one[i] * Bi[i][j] for i in range(4)) for j in range(4)]
    if any(x.denominator != 1 for x in c1):
        return False
    for u in B:
        for v in B:
            w = C.vmul(u, v)
            c = [sum(w[i] * Bi[i][j] for i in range(4)) for j in range(4)]
            if any(x.denominator != 1 for x in c):
                return False
    return True


def discrd(C, B):
    T = [[C.trd(C.vmul(u, v)) for v in B] for u in B]
    d = abs(det(T))
    r = math.isqrt(int(d))
    assert d.denominator == 1 and r * r == d, d
    return r


def two_power_overorders(C, B):
    """all orders O with B <= O <= B^#, [O:B] a power of 2.  Returns list of (index, basis)."""
    T = [[C.trd(C.vmul(u, v)) for v in B] for u in B]
    Ti = inv(T)
    # dual basis rows: d_i = sum_j Ti[i][j] B_j
    dual = [[sum(Ti[i][j] * B[j][k] for j in range(4)) for k in range(4)] for i in range(4)]
    disc = int(abs(det(T)))
    odd = disc
    while odd % 2 == 0:
        odd //= 2
    gens2 = [[odd * x for x in d] for d in dual]  # generates 2-part of dual/B (mod B)
    Bi = inv(B)

    def red(v):  # coordinates mod 1 w.r.t. B
        c = [sum(v[i] * Bi[i][j] for i in range(4)) for j in range(4)]
        return tuple(x - (x.numerator // x.denominator) for x in c)

    G = {tuple([F(0)] * 4)}
    frontier = list(G)
    gc = [red(g) for g in gens2]
    while frontier:
        nf = []
        for a in frontier:
            for g in gc:
                s = tuple((x + y) - ((x + y).numerator // (x + y).denominator) for x, y in zip(a, g))
                if s not in G:
                    G.add(s)
                    nf.append(s)
        frontier = nf
    Gl = sorted(G)
    zero = tuple([F(0)] * 4)

    def add(a, b):
        return tuple((x + y) - ((x + y).numerator // (x + y).denominator) for x, y in zip(a, b))

    def span(gs):
        S = {zero}
        fr = [zero]
        while fr:
            nf = []
            for a in fr:
                for g in gs:
                    s = add(a, g)
                    if s not in S:
                        S.add(s)
                        nf.append(s)
            fr = nf
        return frozenset(S)

    subs = {frozenset([zero])}
    frontier = [frozenset([zero])]
    while frontier:
        nf = []
        for H in frontier:
            for g in Gl:
                if g not in H:
                    H2 = span(list(H) + [g])
                    if H2 not in subs:
                        subs.add(H2)
                        nf.append(H2)
        frontier = nf
    out = []
    for H in subs:
        gens = [list(r) for r in B] + [[sum(c[i] * B[i][k] for i in range(4)) for k in range(4)] for c in H if c != zero]
        Bo = lattice_basis_from_gens(gens)
        if is_order(C, Bo):
            out.append((len(H), Bo))
    return out
