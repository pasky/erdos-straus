"""Z2729: Brandt matrices B(m) of B_{p,infty} (maximal order, Pizer's explicit orders) for primes 5 <= p < PMAX, m <= MMAX,
implemented from scratch (exact lattice arithmetic + Fincke-Pohst), with sanity checks:
 B(1) = I, row sums = sigma(m) (p ∤ m), B(m)B(n) = B(mn) (gcd = 1), Eichler mass sum 1/|O_i^x| = (p-1)/24.
Gross 1987 convention: B_ij(m) = #{b in I_j^{-1} I_i : nrd(b) nrd(I_j)/nrd(I_i) = m} / |O_R(I_j)^x|.
Output: per p: h, classes' unit counts, B(m) for m <= MMAX (as lists), traces.
Usage: python z52d_p2_ZF1_Z2729_brandt.py PMAX MMAX out.json [PMIN]
"""
import sys, json, math, random, itertools
from fractions import Fraction as Fr
from sympy import isprime, primerange, divisor_sigma, legendre_symbol


class Alg:
    def __init__(self, a, b):
        self.a, self.b = a, b

    def mul(self, x, y):
        a, b = self.a, self.b
        x0, x1, x2, x3 = x; y0, y1, y2, y3 = y
        return (x0 * y0 + a * x1 * y1 + b * x2 * y2 - a * b * x3 * y3,
                x0 * y1 + x1 * y0 - b * x2 * y3 + b * x3 * y2,
                x0 * y2 + x2 * y0 + a * x1 * y3 - a * x3 * y1,
                x0 * y3 + x3 * y0 + x1 * y2 - x2 * y1)

    def nrd(self, x):
        a, b = self.a, self.b
        return x[0] ** 2 - a * x[1] ** 2 - b * x[2] ** 2 + a * b * x[3] ** 2

    @staticmethod
    def conj(x):
        return (x[0], -x[1], -x[2], -x[3])


def hnf_rows(gens):
    """Z-basis (4 rows) of the lattice spanned by rational vectors gens."""
    den = 1
    for g in gens:
        for c in g:
            den = den * Fr(c).denominator // math.gcd(den, Fr(c).denominator)
    M = [[int(Fr(c) * den) for c in g] for g in gens]
    # integer row reduction to echelon form
    rows = [r[:] for r in M if any(r)]
    basis = []
    col = 0
    while rows and col < 4:
        rows = [r for r in rows if any(r)]
        piv = [r for r in rows if r[col] != 0]
        if not piv:
            col += 1; continue
        while len([r for r in rows if r[col] != 0]) > 1:
            nz = sorted([r for r in rows if r[col] != 0], key=lambda r: abs(r[col]))
            m = nz[0]
            new = [m]
            for r in nz[1:]:
                q = r[col] // m[col]
                new.append([x - q * y for x, y in zip(r, m)])
            rows = [r for r in rows if r[col] == 0] + new
        m = [r for r in rows if r[col] != 0][0]
        basis.append(m)
        rows = [r for r in rows if r is not m and any(r)]
        col += 1
    assert len(basis) == 4, basis
    return [tuple(Fr(c, den) for c in r) for r in basis]


def det4(M):
    M = [list(r) for r in M]
    n = 4; d = Fr(1)
    for i in range(n):
        piv = next((r for r in range(i, n) if M[r][i] != 0), None)
        if piv is None:
            return Fr(0)
        if piv != i:
            M[i], M[piv] = M[piv], M[i]; d = -d
        d *= M[i][i]
        for r in range(i + 1, n):
            f = M[r][i] / M[i][i]
            M[r] = [x - f * y for x, y in zip(M[r], M[i])]
    return d


def gram(A, basis):
    G = [[Fr(0)] * 4 for _ in range(4)]
    for s in range(4):
        for t in range(4):
            u, v = basis[s], basis[t]
            uv = tuple(x + y for x, y in zip(u, v))
            G[s][t] = (A.nrd(uv) - A.nrd(u) - A.nrd(v)) / 2
    return G


def lll(A, basis, delta=Fr(3, 4)):
    """exact LLL reduction w.r.t. the norm form nrd (positive definite)."""
    b = [tuple(v) for v in basis]
    def ip(u, v):
        uv = tuple(x + y for x, y in zip(u, v))
        return (A.nrd(uv) - A.nrd(u) - A.nrd(v)) / 2
    n = len(b)
    def gso(b):
        bs = []; mu = [[Fr(0)] * n for _ in range(n)]
        for i in range(n):
            v = list(b[i])
            for j in range(i):
                mu[i][j] = ip(b[i], bs[j]) / ip(bs[j], bs[j])
                v = [x - mu[i][j] * y for x, y in zip(v, bs[j])]
            bs.append(tuple(v))
        return bs, mu
    k = 1
    bs, mu = gso(b)
    while k < n:
        for j in range(k - 1, -1, -1):
            q = round(mu[k][j])
            if q:
                b[k] = tuple(x - q * y for x, y in zip(b[k], b[j]))
                bs, mu = gso(b)
        if ip(bs[k], bs[k]) >= (delta - mu[k][k - 1] ** 2) * ip(bs[k - 1], bs[k - 1]):
            k += 1
        else:
            b[k], b[k - 1] = b[k - 1], b[k]
            bs, mu = gso(b)
            k = max(k - 1, 1)
    return b


def count_vectors(A, basis, targets):
    """number of lattice vectors with nrd == T for each T in targets (Fincke-Pohst on exact Gram, LLL-reduced)."""
    basis = lll(A, basis)
    G = gram(A, basis)
    Tmax = max(targets)
    # Cholesky (floats) q(x) = sum_i q_ii (x_i + sum_{j>i} q_ij x_j)^2
    n = 4
    Q = [[float(G[i][j]) for j in range(n)] for i in range(n)]
    q = [[0.0] * n for _ in range(n)]
    for i in range(n):
        for j in range(i, n):
            q[i][j] = Q[i][j]
    for i in range(n):
        for j in range(i + 1, n):
            q[j][i] = q[i][j]
            q[i][j] = q[i][j] / q[i][i]
        for k in range(i + 1, n):
            for l in range(k, n):
                q[k][l] -= q[k][i] * q[i][l]
    cnt = {T: 0 for T in targets}
    Gi = [[G[i][j] for j in range(n)] for i in range(n)]
    x = [0] * n
    eps = 1e-9

    def rec(i, rem):
        c = -sum(q[i][j] * x[j] for j in range(i + 1, n))
        r = math.sqrt(max(rem, 0) / q[i][i]) + eps
        lo, hi = math.ceil(c - r), math.floor(c + r)
        for xi in range(lo, hi + 1):
            x[i] = xi
            used = q[i][i] * (xi - c) ** 2
            if i == 0:
                val = sum(Gi[s][t] * x[s] * x[t] for s in range(n) for t in range(n))
                if val in cnt:
                    cnt[val] += 1
            else:
                rec(i - 1, rem - used)
        x[i] = 0

    rec(n - 1, Tmax + 1e-6)
    return cnt


def pizer(p):
    if p % 4 == 3:
        A = Alg(-1, -p)
        O = [(1, 0, 0, 0), (0, 1, 0, 0), (Fr(1, 2), 0, Fr(1, 2), 0), (0, Fr(1, 2), 0, Fr(1, 2))]
    elif p % 8 == 5:
        A = Alg(-2, -p)
        O = [(Fr(1, 2), 0, Fr(1, 2), Fr(1, 2)), (0, Fr(1, 4), Fr(1, 2), Fr(1, 4)), (0, 0, 1, 0), (0, 0, 0, 1)]
    else:
        q = next(q for q in primerange(3, 10 ** 6) if q % 4 == 3 and legendre_symbol(p % q, q) == -1)
        c = next(c for c in range(q) if (c * c * p + 1) % q == 0)
        A = Alg(-p, -q)
        O = [(Fr(1, 2), 0, Fr(1, 2), 0), (0, Fr(1, 2), 0, Fr(1, 2)), (0, 0, Fr(1, q), Fr(c, q)), (0, 0, 0, 1)]
    O = hnf_rows(O + [(1, 0, 0, 0)])
    # checks: closed under multiplication, reduced discriminant p
    prods = [A.mul(x, y) for x in O for y in O]
    assert hnf_rows(O + prods) == O, "not an order"
    D = det4([[Fr(2) * g for g in row] for row in gram(A, O)])   # det of trd(x_i conj x_j)
    assert abs(D) == p * p, (p, D)
    return A, O


def left_ideal(A, O, gens):
    return hnf_rows([A.mul(o, g) for o in O for g in gens])


def covol(L):
    return abs(det4(L))


def ideal_norm(O, I):
    r = covol(I) / covol(O)
    s = Fr(math.isqrt(r.numerator), math.isqrt(r.denominator))
    assert s * s == r
    return s


def prod_lattice(A, I, J):
    return hnf_rows([A.mul(x, y) for x in I for y in J])


def conj_lat(A, I):
    return [A.conj(x) for x in I]


def brandt(p, MMAX, seed=1):
    A, O = pizer(p)
    rnd = random.Random(seed)
    ell = 2 if p != 2 else 3
    classes = []   # (I, nI, units)
    mass_target = Fr(p - 1, 24)

    def units_of(I, nI):
        L = prod_lattice(A, conj_lat(A, I), I)        # = nrd(I) * O_R(I)
        return count_vectors(A, L, [nI * nI])[nI * nI]

    def same_class(I, nI, J, nJ):
        L = prod_lattice(A, conj_lat(A, J), I)        # J-bar I
        return count_vectors(A, L, [nI * nJ])[nI * nJ] > 0

    def add(I):
        nI = ideal_norm(O, I)
        for (J, nJ, u) in classes:
            if same_class(I, nI, J, nJ):
                return False
        classes.append((I, nI, units_of(I, nI)))
        return True

    add(O)
    mass = sum(Fr(1, c[2]) for c in classes)
    # BFS over the ell-neighbour graph (connected): sub-ideals J = O alpha + ell I of index ell^2
    queue = [0]
    while queue and mass < mass_target:
        I, nI, _ = classes[queue.pop(0)]
        for xs in itertools.product(range(ell), repeat=4):
            if not any(xs):
                continue
            alpha = tuple(sum(xs[s_] * I[s_][t] for s_ in range(4)) for t in range(4))
            if (A.nrd(alpha) / nI) % ell != 0:
                continue
            J = hnf_rows([A.mul(o, alpha) for o in O] + [tuple(ell * c for c in v) for v in I])
            if ideal_norm(O, J) != ell * nI:
                continue
            if add(J):
                queue.append(len(classes) - 1)
                mass = sum(Fr(1, c[2]) for c in classes)
                if mass >= mass_target:
                    break
    assert mass == mass_target, (p, mass, mass_target)
    h = len(classes)
    # Brandt matrices
    B = {m: [[0] * h for _ in range(h)] for m in range(1, MMAX + 1)}
    for i, (Ii, ni, ui) in enumerate(classes):
        for j, (Ij, nj, uj) in enumerate(classes):
            L = prod_lattice(A, conj_lat(A, Ij), Ii)
            targets = [m * ni * nj for m in range(1, MMAX + 1)]
            cnt = count_vectors(A, L, targets)
            for m in range(1, MMAX + 1):
                c = cnt[m * ni * nj]
                assert c % uj == 0
                B[m][i][j] = c // uj
    return h, [c[2] for c in classes], B


def matmul(X, Y):
    n = len(X)
    return [[sum(X[i][k] * Y[k][j] for k in range(n)) for j in range(n)] for i in range(n)]


def main():
    PMAX, MMAX = int(sys.argv[1]), int(sys.argv[2])
    PMIN = int(sys.argv[4]) if len(sys.argv) > 4 else 5
    out = {}
    for p in primerange(PMIN, PMAX):
        h, units, B = brandt(p, MMAX)
        checks = dict(B1_identity=B[1] == [[int(i == j) for j in range(h)] for i in range(h)],
                      rowsum_sigma=all(sum(B[m][i]) == divisor_sigma(m) for m in range(1, MMAX + 1) if m % p
                                       for i in range(h)),
                      multiplicative=all(matmul(B[m], B[n]) == B[m * n] for m in range(2, MMAX + 1)
                                         for n in range(2, MMAX // m + 1) if math.gcd(m, n) == 1 and m * n <= MMAX))
        out[p] = dict(h=h, units=units, checks=checks,
                      trace=[sum(B[m][i][i] for i in range(h)) for m in range(1, MMAX + 1)],
                      B={m: B[m] for m in range(1, MMAX + 1)})
        print(p, h, units, checks, out[p]['trace'][:12], flush=True)
    json.dump(out, open(sys.argv[3], 'w'))


if __name__ == '__main__':
    main()
