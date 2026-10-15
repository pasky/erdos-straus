"""zi_gf.py (O244): F_q[T] arithmetic for q = p^r <= 27 via tables. Field elements are ints 0..q-1 (base-p digits =
coefficients of the F_p-basis 1, x, x^2 of F_p[x]/(m(x))). Polys are lists low->high, trimmed. q prime: plain mod p."""
import itertools

MODS = {4: (2, [1, 1, 1]), 8: (2, [1, 1, 0, 1]), 9: (3, [1, 0, 1]), 25: (5, [2, 0, 1]), 27: (3, [1, 2, 0, 1])}
# x^2+1 over F_3, x^3-x-1 = x^3+2x+1? (27: [1,2,0,1] = 1 + 2x + x^3 = x^3 - x + 1), 25: x^2+2


class GF:
    def __init__(self, q):
        self.q = q
        if q in MODS:
            p, m = MODS[q]
            r = len(m) - 1
        else:
            p, m, r = q, None, 1
        self.p, self.r = p, r

        def tovec(a):
            return [(a // p ** i) % p for i in range(r)]

        def fromvec(v):
            return sum((v[i] % p) * p ** i for i in range(r))

        def vmul(u, v):
            w = [0] * (2 * r - 1)
            for i in range(r):
                for j in range(r):
                    w[i + j] += u[i] * v[j]
            if m is not None:
                for d in range(2 * r - 2, r - 1, -1):
                    c = w[d] % p
                    if c:
                        for i in range(r + 1):
                            w[d - r + i] -= c * m[i]
            return [x % p for x in w[:r]]
        self.A = [[fromvec([x + y for x, y in zip(tovec(a), tovec(b))]) for b in range(q)] for a in range(q)]
        self.M = [[fromvec(vmul(tovec(a), tovec(b))) for b in range(q)] for a in range(q)]
        self.N = [fromvec([-x for x in tovec(a)]) for a in range(q)]
        self.I = [None] * q
        for a in range(1, q):
            for b in range(1, q):
                if self.M[a][b] == 1:
                    self.I[a] = b
        assert all(self.I[a] is not None for a in range(1, q)), "not a field"
        # axioms spot check
        for a in range(q):
            for b in range(q):
                assert self.M[a][b] == self.M[b][a]
                for c in range(q):
                    assert self.M[a][self.A[b][c]] == self.A[self.M[a][b]][self.M[a][c]]
        self.prime_sub = [a for a in range(q) if a < p]  # F_p inside (digits 0..p-1)

    # polynomial ops
    def trim(self, a):
        a = list(a)
        while a and a[-1] == 0:
            a.pop()
        return a

    def add(self, a, b):
        n = max(len(a), len(b))
        A = self.A
        return self.trim([A[a[i] if i < len(a) else 0][b[i] if i < len(b) else 0] for i in range(n)])

    def neg(self, a):
        return [self.N[x] for x in a]

    def sub(self, a, b):
        return self.add(a, self.neg(b))

    def scal(self, c, a):
        return self.trim([self.M[c][x] for x in a])

    def mul(self, a, b):
        if not a or not b:
            return []
        r = [0] * (len(a) + len(b) - 1)
        A, M = self.A, self.M
        for i, x in enumerate(a):
            if x:
                Mx = M[x]
                for j, y in enumerate(b):
                    if y:
                        r[i + j] = A[r[i + j]][Mx[y]]
        return self.trim(r)

    def divmod(self, a, b):
        a = list(a)
        b = self.trim(b)
        assert b
        inv = self.I[b[-1]]
        q = [0] * max(0, len(a) - len(b) + 1)
        A, M, N = self.A, self.M, self.N
        while len(a) >= len(b) and a:
            c = M[a[-1]][inv]
            s = len(a) - len(b)
            q[s] = c
            for j, y in enumerate(b):
                a[s + j] = A[a[s + j]][N[M[c][y]]]
            a = self.trim(a)
        return self.trim(q), a

    def mod(self, a, b):
        return self.divmod(a, b)[1]

    def exact(self, a, b):
        q, r = self.divmod(a, b)
        return q if not r else None

    def monic(self, a):
        return self.scal(self.I[a[-1]], a) if a else a

    def gcd(self, a, b):
        a, b = self.trim(a), self.trim(b)
        while b:
            a, b = b, self.mod(a, b)
        return self.monic(a)

    def monics(self, d):
        for co in itertools.product(range(self.q), repeat=d):
            yield list(co) + [1]

    def inv_series(self, u, n):
        u = list(u) + [0] * n
        r = [0] * n
        i0 = self.I[u[0]]
        r[0] = i0
        for m in range(1, n):
            s = 0
            for j in range(1, m + 1):
                s = self.A[s][self.M[u[j]][r[m - j]]]
            r[m] = self.M[self.N[s]][i0]
        return r

    def factor(self, f):
        """monic irreducible factorisation by trial division (small degrees): list of (g, e)"""
        f = self.monic(f)
        out = []
        d = 1
        while len(f) - 1 >= 2 * d:
            for g in self.monics(d):
                e = 0
                while True:
                    qq = self.exact(f, g)
                    if qq is None:
                        break
                    f, e = qq, e + 1
                if e:
                    out.append((g, e))
            d += 1
        if len(f) > 1:
            # remaining f irreducible (or a power already removed)
            for i, (g, e) in enumerate(out):
                if g == f:
                    out[i] = (g, e + 1)
                    break
            else:
                out.append((f, 1))
        return out

    def divisors(self, fac):
        divs = [[1]]
        for g, e in fac:
            new = []
            for d in divs:
                x = d
                for _ in range(e + 1):
                    new.append(x)
                    x = self.mul(x, g)
            divs = new
        return divs

    def is_irred(self, f):
        fac = self.factor(f)
        return len(fac) == 1 and fac[0][1] == 1


def T(n):
    return [0] * n + [1]


def vT(a):
    v = 0
    while v < len(a) and a[v] == 0:
        v += 1
    return v


def show(a):
    return "".join(map(str, reversed(a))) if a else "0"
