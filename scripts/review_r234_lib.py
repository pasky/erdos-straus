"""R234 from-scratch lattice toolkit (independent of z9_lib / ce_* scripts).

Conventions: a lattice is given by an integer Gram matrix of the *doubled* bilinear form when
half-integral forms are needed; for classical (integer-Gram) lattices we use the Gram of B directly.
Everything exact (ints / Fractions); floats only for enumeration bounds, with exact filtering.
"""
from fractions import Fraction as Fr
from itertools import product
import math


def det3(G):
    (a, b, c), (d, e, f), (g, h, i) = G
    return a * (e * i - f * h) - b * (d * i - f * g) + c * (d * h - e * g)


def qf(G, x):
    n = len(G)
    return sum(G[i][j] * x[i] * x[j] for i in range(n) for j in range(n))


def bf(G, x, y):
    return sum(G[i][j] * x[i] * y[j] for i in range(3) for j in range(3))


def short_vectors(G, B):
    """All integer x != 0 with x^T G x <= B (G positive definite, rational entries ok).
    Fincke-Pohst with float bounds + slack, exact filter. Returns list of (Q, x) with x up to sign
    NOT identified (both signs returned)."""
    n = len(G)
    Gf = [[float(G[i][j]) for j in range(n)] for i in range(n)]
    # LDL^T: Q(x) = sum_i d_i (x_i + sum_{j>i} mu_ij x_j)^2
    d = [0.0] * n
    mu = [[0.0] * n for _ in range(n)]
    A = [row[:] for row in Gf]
    for i in range(n):
        d[i] = A[i][i]
        for j in range(i + 1, n):
            mu[i][j] = A[i][j] / d[i]
        for j in range(i + 1, n):
            for k in range(i + 1, n):
                A[j][k] -= d[i] * mu[i][j] * mu[i][k]
    out = []
    Bf = float(B) * (1 + 1e-9) + 1e-9
    x = [0] * n

    def rec(i, rem):
        if i < 0:
            if any(x):
                q = qf(G, x)
                if q <= B:
                    out.append((q, tuple(x)))
            return
        c = -sum(mu[i][j] * x[j] for j in range(i + 1, n))
        r = math.sqrt(max(rem, 0) / d[i])
        lo, hi = math.ceil(c - r - 1e-9), math.floor(c + r + 1e-9)
        for xi in range(lo, hi + 1):
            x[i] = xi
            rem2 = rem - d[i] * (xi - c) ** 2
            if rem2 >= -1e-7:
                rec(i - 1, rem2)
        x[i] = 0

    rec(n - 1, Bf)
    return out


def rep_counts(G, M):
    """r_G(m) for 1 <= m <= M (G integer or rational Gram, Q(x) = x^T G x)."""
    r = [0] * (M + 1)
    for q, x in short_vectors(G, M):
        if q == int(q) and 1 <= q <= M:
            r[int(q)] += 1
    return r


def gram_of(G, basis):
    return [[bf(G, u, v) for v in basis] for u in basis]


def canon(G):
    return canon_full(G)[0]


def canon_full(G):
    """Canonical form of a positive definite ternary Gram (rational entries) up to isometry:
    lexicographically minimal (g11,g22,g33,g12,g13,g23) over all bases attaining the successive minima
    (in dim 3 every lattice has such a basis, and the set of such bases is isometry-invariant)."""
    # successive minima: enumerate up to growing bound
    B = max(G[i][i] for i in range(3))
    sv = short_vectors(G, B)
    sv.sort()
    # lambda1
    vecs = [x for q, x in sv]
    l1 = sv[0][0]
    V1 = [x for q, x in sv if q == l1]
    # lambda2: least Q of a vector independent of V1[0] -- need independence from *some* v1 attaining l1;
    # successive minima are basis-independent: lambda2 = min{Q(y): y indep of some l1-vector}... use the rank definition.
    # greedy (matroid) computation of successive minima over vectors sorted by norm
    lam = []
    indep = []
    for q, x in sv:
        if len(indep) == 0:
            ok = True
        elif len(indep) == 1:
            y = indep[0]
            ok = any(x[a] * y[b] - x[b] * y[a] for a in range(3) for b in range(3))
        else:
            ok = det3([indep[0], indep[1], list(x)]) != 0
        if ok:
            indep.append(list(x)); lam.append(q)
            if len(lam) == 3:
                break
    assert len(lam) == 3
    L = [[x for qq, x in sv if qq == lam[i]] for i in range(3)]
    best = None
    allb = []
    for v1 in L[0]:
        for v2 in L[1]:
            if v2 == v1:
                continue
            for v3 in L[2]:
                M = [v1, v2, v3]
                if abs(det3(M)) != 1:
                    continue
                H = gram_of(G, M)
                key = (H[0][0], H[1][1], H[2][2], H[0][1], H[0][2], H[1][2])
                if best is None or key < best:
                    best = key
                    allb = [M]
                elif key == best:
                    allb.append(M)
    assert best is not None
    return best, allb


def legendre(a, p):
    a %= p
    if a == 0:
        return 0
    return 1 if pow(a, (p - 1) // 2, p) == 1 else -1


def aniso_at_p(G, p):
    """For a classical integer Gram G with p || det G: True iff L (x) Q_p anisotropic.
    L mod p has 1-dim radical; the nondegenerate binary quotient has determinant d (mod p);
    anisotropic iff -d is a non-square mod p."""
    # find radical vector of G mod p
    rad = None
    for x in product(range(p), repeat=3) if p < 8 else []:
        pass
    # solve G x = 0 mod p via adjugate: any nonzero row of adj(G) mod p spans the radical (rank 2)
    adj = [[0] * 3 for _ in range(3)]
    for i in range(3):
        for j in range(3):
            m = [[G[r][c] for c in range(3) if c != j] for r in range(3) if r != i]
            adj[j][i] = (-1) ** (i + j) * (m[0][0] * m[1][1] - m[0][1] * m[1][0])
    for col in range(3):
        r = [adj[i][col] % p for i in range(3)]
        if any(r):
            rad = r
            break
    assert rad is not None
    # complete rad to a basis mod p and compute the binary quotient form on two other vectors
    std = [(1, 0, 0), (0, 1, 0), (0, 0, 1)]
    for a_ in range(3):
        for b_ in range(a_ + 1, 3):
            M = [rad, list(std[a_]), list(std[b_])]
            if det3(M) % p:
                u, v = std[a_], std[b_]
                d = (qf(G, u) * qf(G, v) - bf(G, u, v) ** 2) % p
                return legendre(-d, p) == -1
    raise RuntimeError


def classes_det_p(p):
    """All isometry classes of positive classical ternary lattices of determinant p (canonical keys).
    Enumerates Minkowski-type reduced Grams a<=b<=c, |2f|<=a, |2e|<=a, |2d|<=b (necessary for
    Minkowski reduction), computes c from det, canonicalises."""
    keys = set()
    amax = int(round((2 * p) ** (1 / 3))) + 2
    for a in range(1, amax + 1):
        for b in range(a, int(math.isqrt(2 * p // a)) + 2):
            for f in range(-(a // 2), a // 2 + 1):
                if a * b - f * f <= 0:
                    continue
                for e in range(-(a // 2), a // 2 + 1):
                    for d in range(-(b // 2), b // 2 + 1):
                        num = p + a * d * d - 2 * f * d * e + b * e * e
                        den = a * b - f * f
                        if num % den:
                            continue
                        c = num // den
                        if c < b:
                            continue
                        G = [[a, f, e], [f, b, d], [e, d, c]]
                        if det3(G) != p:
                            continue
                        keys.add(canon(G))
    return keys


def key_to_gram(k):
    a, b, c, f, e, d = k
    return [[a, f, e], [f, b, d], [e, d, c]]


# ---------- sublattice / overlattice machinery (bases as rational 3x3 matrices, rows = vectors) ----------

def hnf_basis(vectors):
    """Z-basis (rows, Fractions) of the lattice spanned by given rational vectors in Q^3."""
    den = 1
    for v in vectors:
        for c in v:
            den = den * Fr(c).denominator // math.gcd(den, Fr(c).denominator)
    import sympy
    M = sympy.Matrix([[int(Fr(c) * den) for c in v] for v in vectors])
    from sympy.matrices.normalforms import hermite_normal_form
    H = hermite_normal_form(M.T).T  # rows basis
    rows = [list(H.row(i)) for i in range(H.rows) if any(H.row(i))]
    assert len(rows) == 3, rows
    return [[Fr(int(c), den) for c in r] for r in rows]


def gram_basis(G, Bs):
    return [[sum(Fr(G[i][j]) * u[i] * v[j] for i in range(3) for j in range(3)) for v in Bs] for u in Bs]


# ---------- edges / vertices / words ----------

def iso_classes_mod4(G):
    """Nonzero x in {0,1}^3 with Q(x) = 0 mod 4 (the isotropic classes of L/2L)."""
    return [x for x in product((0, 1), repeat=3) if any(x) and qf(G, x) % 4 == 0]


def overlattices(G):
    """The two vertex lattices F = L + Z x/2 (as Gram matrices of B, rational) of an edge lattice G."""
    out = []
    E = [[Fr(int(i == j)) for j in range(3)] for i in range(3)]
    for x in iso_classes_mod4(G):
        Bs = hnf_basis(E + [[Fr(c, 2) for c in x]])
        out.append((x, Bs, gram_basis(G, Bs)))
    return out


def divisors(n):
    ds, i = [], 1
    small = []
    while i * i <= n:
        if n % i == 0:
            small.append(i)
            if i * i != n:
                ds.append(n // i)
        i += 1
    return small + ds[::-1]


def words(n):
    """All (t,u,v), letters >= 1, with t*u*v - u - v = n."""
    W = []
    for t in range(1, n + 3):
        N = t * n + 1
        for A in divisors(N):
            if (A + 1) % t:
                continue
            As = N // A
            if (As + 1) % t:
                continue
            u, v = (A + 1) // t, (As + 1) // t
            if u >= 1 and v >= 1 and t * u * v - u - v == n:
                W.append((t, u, v))
    return W


def path_gram(w):
    t, u, v = w
    return [[v, -1, 0], [-1, t, -1], [0, -1, u]]


def primes_1mod4(lo, hi):
    import sympy
    return [p for p in sympy.primerange(lo, hi + 1) if p % 4 == 1]
