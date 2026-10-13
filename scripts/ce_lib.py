"""ce_lib: even Clifford orders of ternary lattices, overorders, quaternion order invariants (O199).

Conventions. A ternary lattice is given by an integral symmetric Gram matrix G (classical: B(e_i,e_j) = G_ij,
Q(x) = B(x,x)) or more generally by a rational symmetric G; Clifford relations e_i e_j + e_j e_i = 2 G_ij.
An order is a list of 4 basis vectors (Fractions) in coordinates of the fixed algebra basis
(1, f1 = e2e3, f2 = e3e1, f3 = e1e2) of C_0(G), with structure constants computed exactly.
"""
from fractions import Fraction as Fr
from itertools import product
from math import gcd

# ---------- Clifford algebra of rank 3 on monomials (sorted index tuples) ----------


def _mono_mul(a, b, G):
    """Product of monomials a, b (tuples of increasing indices) -> dict{mono: coeff}."""
    # represent as word, straighten by bubble sort with relations
    res = {}
    stack = [(1, list(a) + list(b))]
    while stack:
        c, w = stack.pop()
        if c == 0:
            continue
        # find first adjacent pair out of order or equal
        for k in range(len(w) - 1):
            if w[k] >= w[k + 1]:
                i, j = w[k], w[k + 1]
                if i == j:  # e_i e_i = G_ii
                    stack.append((c * G[i][i], w[:k] + w[k + 2:]))
                else:  # e_i e_j = -e_j e_i + 2 G_ij  (i > j)
                    stack.append((-c, w[:k] + [j, i] + w[k + 2:]))
                    stack.append((c * 2 * G[i][j], w[:k] + w[k + 2:]))
                break
        else:
            t = tuple(w)
            res[t] = res.get(t, 0) + c
    return res


C0_BASIS = [(), (1, 2), (0, 2), (0, 1)]  # 1, e2e3, e1e3, e1e2  (0-indexed: e1=0)
C0_SIGN = [1, 1, -1, 1]  # f2 = e3e1 = -e1e3 + 2G13 (handled below exactly)


def c0_table(G):
    """Structure constants of C_0 in basis (1, f1=e2e3, f2=e3e1, f3=e1e2) -> T[i][j] = vector of 4 Fractions."""
    G = [[Fr(x) for x in row] for row in G]
    # express basis elements as dicts on monomials
    def elt(k):
        if k == 0:
            return {(): Fr(1)}
        if k == 1:
            return {(1, 2): Fr(1)}
        if k == 2:  # e3 e1 = -e1 e3 + 2 G13
            return {(0, 2): Fr(-1), (): 2 * G[0][2]}
        return {(0, 1): Fr(1)}
    basis = [elt(k) for k in range(4)]

    def mul(x, y):
        out = {}
        for ma, ca in x.items():
            for mb, cb in y.items():
                for m, c in _mono_mul(ma, mb, G).items():
                    out[m] = out.get(m, 0) + ca * cb * c
        return {m: c for m, c in out.items() if c != 0}

    def coords(x):
        # x is in C_0: monomials (), (1,2), (0,2), (0,1)
        c1 = x.get((1, 2), Fr(0))
        c2 = -x.get((0, 2), Fr(0))
        c3 = x.get((0, 1), Fr(0))
        c0 = x.get((), Fr(0)) - c2 * 2 * G[0][2]
        for m in x:
            assert m in ((), (1, 2), (0, 2), (0, 1)), m
        return [c0, c1, c2, c3]

    return [[coords(mul(basis[i], basis[j])) for j in range(4)] for i in range(4)]


# ---------- algebra operations given a structure table ----------


class Alg:
    def __init__(self, T):
        self.T = T
        # reduced trace: trd(x) = tr(left mult)/2
        self.trv = [sum(T[i][j][j] for j in range(4)) / 2 for i in range(4)]

    def mul(self, x, y):
        out = [Fr(0)] * 4
        for i in range(4):
            if x[i] == 0:
                continue
            for j in range(4):
                if y[j] == 0:
                    continue
                c = x[i] * y[j]
                Tij = self.T[i][j]
                for k in range(4):
                    out[k] += c * Tij[k]
        return out

    def trd(self, x):
        return sum(x[i] * self.trv[i] for i in range(4))

    def conj(self, x):
        t = self.trd(x)
        return [t - x[0], -x[1], -x[2], -x[3]]

    def nrd(self, x):
        y = self.mul(x, self.conj(x))
        assert all(c == 0 for c in y[1:]), y
        return y[0]


def _solve(Bm, v):
    """Solve sum c_i Bm[i] = v over Q (Bm 4x4 rows); return c."""
    n = 4
    M = [[Bm[i][j] for i in range(n)] + [v[j]] for j in range(n)]  # columns = basis vectors
    for col in range(n):
        piv = next(r for r in range(col, n) if M[r][col] != 0)
        M[col], M[piv] = M[piv], M[col]
        pv = M[col][col]
        M[col] = [x / pv for x in M[col]]
        for r in range(n):
            if r != col and M[r][col] != 0:
                f = M[r][col]
                M[r] = [a - f * b for a, b in zip(M[r], M[col])]
    return [M[r][n] for r in range(n)]


def is_order(alg, Bm):
    for x in Bm:
        for y in Bm:
            c = _solve(Bm, alg.mul(x, y))
            if any(ci.denominator != 1 for ci in c):
                return False
    return True


def det4(M):
    M = [row[:] for row in M]
    n = len(M)
    d = Fr(1)
    for c in range(n):
        piv = next((r for r in range(c, n) if M[r][c] != 0), None)
        if piv is None:
            return Fr(0)
        if piv != c:
            M[c], M[piv] = M[piv], M[c]
            d = -d
        d *= M[c][c]
        for r in range(c + 1, n):
            f = M[r][c] / M[c][c]
            M[r] = [a - f * b for a, b in zip(M[r], M[c])]
    return d


def discrd(alg, Bm):
    D = det4([[alg.trd(alg.mul(x, y)) for y in Bm] for x in Bm])
    D = abs(D)
    # discrd = sqrt(|disc|)
    from math import isqrt
    assert D.denominator == 1
    r = isqrt(D.numerator)
    assert r * r == D.numerator, D
    return r


def hnf_key(Bm):
    """Canonical key of the Z-lattice spanned by Bm (rows) -- via scaling to integers and HNF."""
    den = 1
    for row in Bm:
        for x in row:
            den = den * x.denominator // gcd(den, x.denominator)
    rows = [[int(x * den) for x in row] for row in Bm]
    H = hnf(rows)
    return (den, tuple(tuple(r) for r in H))


def hnf(rows):
    """Row HNF of integer matrix (full rank 4)."""
    A = [r[:] for r in rows]
    m, n = len(A), len(A[0])
    r = 0
    for c in range(n):
        # gcd-eliminate column c among rows r..
        while True:
            nz = [i for i in range(r, m) if A[i][c] != 0]
            if not nz:
                break
            i0 = min(nz, key=lambda i: abs(A[i][c]))
            A[r], A[i0] = A[i0], A[r]
            done = True
            for i in range(r + 1, m):
                if A[i][c]:
                    q = A[i][c] // A[r][c]
                    A[i] = [a - q * b for a, b in zip(A[i], A[r])]
                    if A[i][c]:
                        done = False
            if done:
                break
        if r < m and A[r][c] != 0:
            if A[r][c] < 0:
                A[r] = [-a for a in A[r]]
            for i in range(r):
                q = A[i][c] // A[r][c]
                A[i] = [a - q * b for a, b in zip(A[i], A[r])]
            r += 1
    return [row for row in A if any(row)]


def overorders_index2(alg, Bm):
    """All orders O' with O ⊂ O' of index 2."""
    out = []
    for e in product((0, 1), repeat=4):
        if not any(e):
            continue
        x = [sum(Fr(e[i], 2) * Bm[i][k] for i in range(4)) for k in range(4)]
        # new lattice basis: replace a basis vector with nonzero e-coefficient
        i0 = max(i for i in range(4) if e[i])
        Bn = [row for row in Bm]
        Bn = Bn[:i0] + [x] + Bn[i0 + 1:]
        if is_order(alg, Bn):
            out.append(Bn)
    return out


def maximal_overorders_2(alg, Bm, depth=4):
    """All 2-power-index overorders reachable (BFS); returns dict key -> (basis, discrd)."""
    seen = {hnf_key(Bm): Bm}
    frontier = [Bm]
    for _ in range(depth):
        nf = []
        for B in frontier:
            for B2 in overorders_index2(alg, B):
                k = hnf_key(B2)
                if k not in seen:
                    seen[k] = B2
                    nf.append(B2)
        frontier = nf
        if not frontier:
            break
    return {k: (B, discrd(alg, B)) for k, B in seen.items()}


def path_gram(t, u, v):
    return [[v, -1, 0], [-1, t, -1], [0, -1, u]]


def ident_basis():
    return [[Fr(int(i == j)) for j in range(4)] for i in range(4)]
