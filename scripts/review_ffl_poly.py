"""R161 from-scratch F_q[T] arithmetic (no reuse of ffl_* code).

Field GF(q), q = p^r, elements are ints 0..q-1 encoding a0 + a1 x + ... (base-p digits),
with fixed minimal polynomials (same convention as the author's encoding so that certificate
strings can be parsed, but the arithmetic below is written independently):
  GF(4): x^2 + x + 1,  GF(8): x^3 + x + 1,  GF(9): x^2 + 1.
Polynomials: tuples of field ints, low degree first, no trailing zeros; () is 0.
"""
import itertools
from functools import lru_cache

MINPOLY = {4: (2, 2, (1, 1)), 8: (2, 3, (1, 1, 0)), 9: (3, 2, (1, 0))}  # p, r, low coeffs of x^r + ...


class Field:
    def __init__(self, q):
        self.q = q
        if q in MINPOLY:
            p, r, low = MINPOLY[q]
        else:
            p, r, low = q, 1, ()
            assert all(q % t for t in range(2, q)), "q must be prime or in MINPOLY"
        self.p, self.r = p, r

        def digits(a):
            return [(a // p ** i) % p for i in range(r)]

        def undig(d):
            return sum(c * p ** i for i, c in enumerate(d))

        def mulraw(a, b):
            da, db = digits(a), digits(b)
            pr = [0] * (2 * r)
            for i in range(r):
                for j in range(r):
                    pr[i + j] = (pr[i + j] + da[i] * db[j]) % p
            for t in range(2 * r - 2, r - 1, -1):
                c = pr[t]
                if c:
                    pr[t] = 0
                    for i in range(r):
                        pr[t - r + i] = (pr[t - r + i] - c * low[i]) % p
            return undig(pr[:r])

        self.add = [[undig([(x + y) % p for x, y in zip(digits(a), digits(b))]) for b in range(q)] for a in range(q)]
        self.mul = [[mulraw(a, b) for b in range(q)] for a in range(q)]
        self.neg = [next(b for b in range(q) if self.add[a][b] == 0) for a in range(q)]
        self.inv = [None] + [next(b for b in range(q) if self.mul[a][b] == 1) for a in range(1, q)]
        # sanity: field axioms (associativity of mul, distributivity) on all triples
        for a in range(q):
            for b in range(q):
                for c in range(q):
                    assert self.mul[self.mul[a][b]][c] == self.mul[a][self.mul[b][c]]
                    assert self.mul[a][self.add[b][c]] == self.add[self.mul[a][b]][self.mul[a][c]]
        self.sq = sorted({self.mul[a][a] for a in range(1, q)})


def trim(c):
    c = list(c)
    while c and c[-1] == 0:
        c.pop()
    return tuple(c)


class PolyRing:
    def __init__(self, q):
        self.F = F = Field(q)
        self.q = q
        self.one = (1,)

    def deg(self, a):
        return len(a) - 1  # deg 0 = -1

    def lc(self, a):
        return a[-1] if a else 0

    def add(self, a, b):
        F = self.F
        n = max(len(a), len(b))
        a = a + (0,) * (n - len(a))
        b = b + (0,) * (n - len(b))
        return trim(F.add[x][y] for x, y in zip(a, b))

    def neg(self, a):
        return tuple(self.F.neg[x] for x in a)

    def sub(self, a, b):
        return self.add(a, self.neg(b))

    def scal(self, c, a):
        return trim(self.F.mul[c][x] for x in a)

    def mul(self, a, b):
        if not a or not b:
            return ()
        F = self.F
        r = [0] * (len(a) + len(b) - 1)
        for i, x in enumerate(a):
            if x:
                mx = F.mul[x]
                for j, y in enumerate(b):
                    if y:
                        r[i + j] = F.add[r[i + j]][mx[y]]
        return trim(r)

    def divmod(self, a, b):
        assert b, "division by zero"
        F = self.F
        a = list(a)
        db = len(b) - 1
        ib = F.inv[b[-1]]
        qt = [0] * max(0, len(a) - db)
        for i in range(len(a) - 1, db - 1, -1):
            c = a[i]
            if c:
                f = F.mul[c][ib]
                qt[i - db] = f
                for j, y in enumerate(b):
                    a[i - db + j] = F.add[a[i - db + j]][F.neg[F.mul[f][y]]]
        return trim(qt), trim(a[:db])

    def mod(self, a, b):
        return self.divmod(a, b)[1]

    def divides(self, d, a):
        return not self.mod(a, d)

    def monic(self, a):
        return self.scal(self.F.inv[a[-1]], a) if a else a

    def gcd(self, a, b):
        while b:
            a, b = b, self.mod(a, b)
        return self.monic(a)

    def monics(self, n):
        """all monic polys of degree n"""
        for low in itertools.product(range(self.q), repeat=n):
            yield tuple(low) + (1,)

    def polys_below(self, n):
        """all polys of degree < n (incl. 0)"""
        for c in itertools.product(range(self.q), repeat=n):
            yield trim(c)

    def is_irreducible(self, f):
        """f monic; Ben-Or / Rabin style: gcd(f, T^{q^i} - T) = 1 for i <= n/2."""
        n = self.deg(f)
        if n <= 0:
            return False
        if n == 1:
            return True
        T = (0, 1)
        x = T
        for i in range(1, n // 2 + 1):
            x = self.powmod(x, self.q, f)
            if self.deg(self.gcd(f, self.sub(x, T))) > 0:
                return False
        return True

    def powmod(self, a, e, m):
        r = (1,)
        a = self.mod(a, m)
        while e:
            if e & 1:
                r = self.mod(self.mul(r, a), m)
            a = self.mod(self.mul(a, a), m)
            e >>= 1
        return r

    def irreducibles(self, n):
        return [f for f in self.monics(n) if self.is_irreducible(f)]

    def factor(self, a):
        """monic a -> list of (monic irreducible, exponent) by trial division (small degrees only)."""
        a = self.monic(a)
        res = []
        d = 1
        while self.deg(a) >= 2 * d:
            for g in self.monics(d):
                if self.deg(a) < d:
                    break
                e = 0
                while True:
                    qt, rm = self.divmod(a, g)
                    if rm:
                        break
                    a = qt
                    e += 1
                if e:
                    res.append((g, e))
            d += 1
        if self.deg(a) >= 1:
            res.append((a, 1))
        # merge (the leftover could equal an earlier factor only if deg small; trial covers that)
        return res

    def divisors(self, a):
        fac = self.factor(a)
        divs = [(1,)]
        for g, e in fac:
            new = []
            pw = (1,)
            pws = [pw]
            for _ in range(e):
                pw = self.mul(pw, g)
                pws.append(pw)
            for d in divs:
                for w in pws:
                    new.append(self.mul(d, w))
            divs = new
        return divs

    def parse(self, s):
        """author's string encoding: digits high->low, each digit a field element (q <= 10)."""
        return trim(int(ch) for ch in reversed(s))

    def show(self, a):
        return "".join(str(c) for c in reversed(a)) if a else "0"


if __name__ == "__main__":
    for q in (2, 3, 4, 5, 7, 8, 9):
        R = PolyRing(q)
        # count irreducibles vs necklace formula
        for n in range(1, 5 if q <= 5 else 4):
            cnt = len(R.irreducibles(n))
            mob = {1: 1, 2: -1, 3: -1, 4: 0}
            formula = sum(mob[n // d] * q ** d for d in range(1, n + 1) if n % d == 0 and n // d in mob) // n
            assert cnt == formula, (q, n, cnt, formula)
        # divmod round trip
        import random
        rnd = random.Random(1)
        for _ in range(200):
            a = trim(rnd.randrange(q) for _ in range(rnd.randrange(1, 9)))
            b = trim(rnd.randrange(q) for _ in range(rnd.randrange(1, 6)))
            if not b:
                continue
            qt, rm = R.divmod(a, b)
            assert R.add(R.mul(qt, b), rm) == a and R.deg(rm) < R.deg(b)
    print("poly lib self-test OK")
