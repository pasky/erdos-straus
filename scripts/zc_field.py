"""zc_field.py (O226): small finite fields F_q, q in {3,5,7,9,25,27,49,81} with element codes as in fz1_enum.c
(F_9 = F_3[i]/(i^2+1), code a + 3b; F_27 = F_3[x]/(x^3 - x - 1), code c0 + 3c1 + 9c2; F_81 = F_3[x]/(x^4 + x + 2)
... prime-power fields beyond 27 use the given modulus, codes = base-p digits low->high) and polynomial helpers
(coefficient lists low->high)."""
from functools import lru_cache

MODULI = {9: (3, [1, 0, 1]), 27: (3, [-1, -1, 0, 1]), 81: (3, [2, 1, 0, 0, 1]), 25: (5, [2, 0, 1]), 49: (7, [1, 0, 1]),
          243: (3, [1, 2, 0, 0, 0, 1])}


class GF:
    def __init__(self, q):
        self.q = q
        if q in MODULI:
            p, mod = MODULI[q]
        else:
            p, mod = q, [0, 1]
        self.p = p
        r = len(mod) - 1
        self.r = r
        mod = [c % p for c in mod]
        def dec(x):
            return [(x // p**i) % p for i in range(r)]
        def enc(v):
            return sum((c % p) * p**i for i, c in enumerate(v))
        def pm(u, v):
            prod = [0] * (2 * r - 1)
            for i, a in enumerate(u):
                for j, b in enumerate(v):
                    prod[i + j] += a * b
            for k in range(2 * r - 2, r - 1, -1):
                c = prod[k] % p
                if c:
                    for i in range(r + 1):
                        prod[k - r + i] -= c * mod[i]
            return enc(prod[:r])
        self.ADD = [[enc([a + b for a, b in zip(dec(x), dec(y))]) for y in range(q)] for x in range(q)]
        self.MUL = [[pm(dec(x), dec(y)) for y in range(q)] for x in range(q)]
        self.NEG = [enc([-a for a in dec(x)]) for x in range(q)]
        self.INV = [0] * q
        for x in range(1, q):
            for y in range(1, q):
                if self.MUL[x][y] == 1:
                    self.INV[x] = y
        # axioms (fail closed)
        for x in range(q):
            assert self.MUL[x][1] == x and self.ADD[x][0] == x
            if x:
                assert self.MUL[x][self.INV[x]] == 1
        nz = [x for x in range(1, q) if all(self.MUL[x][y] for y in range(1, q))]
        assert len(nz) == q - 1, "not a field"
        self.prime_sub = set(enc([c]) for c in range(p))

    def pw(self, x, e):
        r = 1
        e %= (self.q - 1) if x else 10**9
        for _ in range(e):
            r = self.MUL[r][x]
        return r

    # polynomials
    def trim(self, a):
        a = list(a)
        while a and a[-1] == 0:
            a.pop()
        return a

    def padd(self, a, b):
        n = max(len(a), len(b))
        return self.trim([self.ADD[a[i] if i < len(a) else 0][b[i] if i < len(b) else 0] for i in range(n)])

    def pneg(self, a):
        return [self.NEG[c] for c in a]

    def pmul(self, a, b):
        if not a or not b:
            return []
        r = [0] * (len(a) + len(b) - 1)
        for i, x in enumerate(a):
            if x:
                for j, y in enumerate(b):
                    r[i + j] = self.ADD[r[i + j]][self.MUL[x][y]]
        return self.trim(r)

    def pdivmod(self, a, b):
        a = self.trim(a); b = self.trim(b)
        inv = self.INV[b[-1]]
        qt = [0] * max(1, len(a) - len(b) + 1)
        while len(a) >= len(b) and a:
            f = self.MUL[a[-1]][inv]; sh = len(a) - len(b); qt[sh] = f
            for i, x in enumerate(b):
                a[sh + i] = self.ADD[a[sh + i]][self.NEG[self.MUL[f][x]]]
            a = self.trim(a)
        return self.trim(qt), a
