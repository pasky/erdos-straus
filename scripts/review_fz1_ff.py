"""review_fz1_ff.py (R226): tiny self-contained F_q / F_q[T] arithmetic (q = p prime, or q = 9, 27 as F_3[x]/(irred)).
Elements are ints 0..q-1 (base-p digit vectors of the F_p[x]/(m) representative); polys are tuples, low degree first,
trimmed (no trailing zeros); () is the zero polynomial. Written from scratch for the R226 review (not from fz1_*)."""
import itertools

class GF:
    def __init__(self, q):
        self.q = q
        p = next(d for d in range(2, q + 1) if q % d == 0); r = 0; x = q
        while x > 1: x //= p; r += 1
        assert p ** r == q
        self.p, self.r = p, r
        if r == 1: mod = None
        elif q == 9: mod = (1, 0, 1)          # x^2 + 1 over F_3
        elif q == 27: mod = (1, 2, 0, 1)      # x^3 + 2x + 1 = x^3 - x + 1 over F_3
        elif q == 25: mod = (2, 0, 1)         # x^2 + 2 over F_5
        else: raise ValueError(q)
        def dig(a): return [(a // p ** i) % p for i in range(r)]
        def und(v): return sum(c * p ** i for i, c in enumerate(v))
        add = [[und([(x + y) % p for x, y in zip(dig(a), dig(b))]) for b in range(q)] for a in range(q)]
        def pm(a, b):
            A, B = dig(a), dig(b); c = [0] * (2 * r)
            for i in range(r):
                for j in range(r): c[i + j] = (c[i + j] + A[i] * B[j]) % p
            if mod is not None:
                for k in range(2 * r - 1, r - 1, -1):
                    ck = c[k]
                    if ck:
                        c[k] = 0
                        for i in range(r): c[k - r + i] = (c[k - r + i] - ck * mod[i]) % p
            return und(c[:r])
        mul = [[pm(a, b) for b in range(q)] for a in range(q)]
        self.add, self.mul = add, mul
        self.neg = [next(b for b in range(q) if add[a][b] == 0) for a in range(q)]
        self.inv = [None] + [next(b for b in range(q) if mul[a][b] == 1) for a in range(1, q)]
        # field axioms (fail-closed)
        for a in range(q):
            for b in range(q):
                assert add[a][b] == add[b][a] and mul[a][b] == mul[b][a]
                for c in range(q):
                    assert mul[a][add[b][c]] == add[mul[a][b]][mul[a][c]]
                    assert mul[mul[a][b]][c] == mul[a][mul[b][c]]
        self.prime_sub = set()   # F_p inside F_q: elements c*1
        x = 0
        for _ in range(p): self.prime_sub.add(x); x = add[x][1]
        self.F3star = {1, self.neg[1]} if p == 3 else None

    # ---- polynomials ----
    def trim(self, f):
        f = list(f)
        while f and f[-1] == 0: f.pop()
        return tuple(f)
    def padd(self, f, g):
        n = max(len(f), len(g)); A = self.add
        return self.trim([A[f[i] if i < len(f) else 0][g[i] if i < len(g) else 0] for i in range(n)])
    def pneg(self, f): return tuple(self.neg[c] for c in f)
    def psub(self, f, g): return self.padd(f, self.pneg(g))
    def pmul(self, f, g):
        if not f or not g: return ()
        M, A = self.mul, self.add; c = [0] * (len(f) + len(g) - 1)
        for i, x in enumerate(f):
            if x:
                Mx = M[x]
                for j, y in enumerate(g): c[i + j] = A[c[i + j]][Mx[y]]
        return self.trim(c)
    def pscale(self, f, c): return self.trim([self.mul[c][x] for x in f])
    def pdivmod(self, f, g):
        assert g
        f = list(f); dg = len(g) - 1; il = self.inv[g[-1]]; M, A, N = self.mul, self.add, self.neg
        qt = [0] * max(0, len(f) - dg)
        for k in range(len(f) - 1, dg - 1, -1):
            c = f[k]
            if c:
                c = M[c][il]; qt[k - dg] = c; nc = N[c]
                for i, y in enumerate(g): f[k - dg + i] = A[f[k - dg + i]][M[nc][y]]
        return self.trim(qt), self.trim(f[:dg])
    def pdivides(self, g, f): return not self.pdivmod(f, g)[1]
    def deg(self, f): return len(f) - 1
    def lc(self, f): return f[-1]
    def monic(self, f): return self.pscale(f, self.inv[f[-1]])
    def T(self, k=1): return tuple([0] * k + [1])
    def const(self, c): return self.trim([c])
    def polys(self, d, monic=True, Tfree=False):
        """all polys of exact degree d (monic, or all lc), optionally with nonzero constant term"""
        q = self.q
        lcs = [1] if monic else range(1, q)
        for l in lcs:
            if d == 0:
                yield (l,); continue
            for low in itertools.product(range(q), repeat=d):
                if Tfree and low[0] == 0: continue
                yield tuple(low) + (l,)
    def pgcd(self, f, g):
        while g: f, g = g, self.pdivmod(f, g)[1]
        return self.monic(f) if f else f
