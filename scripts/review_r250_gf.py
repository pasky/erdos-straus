"""review_r250_gf.py (R250, from scratch; nothing from zi_*): GF(q) for q in {3, 5, 7, 9} and F_q[T] arithmetic.
F_9 = F_3[i]/(i^2 + 1), element a + b i encoded as a + 3 b. Polys: tuples low -> high, trimmed (zero poly = ())."""
import itertools, random


class Field:
    def __init__(self, q):
        self.q = q
        if q in (3, 5, 7):
            self.p = q
            add = lambda x, y: (x + y) % q
            mul = lambda x, y: (x * y) % q
        elif q == 9:
            self.p = 3
            def dec(x): return x % 3, x // 3
            def enc(a, b): return (a % 3) + 3 * (b % 3)
            def add(x, y):
                a, b = dec(x); c, d = dec(y); return enc(a + c, b + d)
            def mul(x, y):
                a, b = dec(x); c, d = dec(y); return enc(a * c - b * d, a * d + b * c)  # i^2 = -1
        else:
            raise ValueError(q)
        Q = range(q)
        self.ADD = [[add(x, y) for y in Q] for x in Q]
        self.MUL = [[mul(x, y) for y in Q] for x in Q]
        self.NEG = [next(y for y in Q if self.ADD[x][y] == 0) for x in Q]
        self.INV = [None] + [next(y for y in Q if self.MUL[x][y] == 1) for x in range(1, q)]
        # field axioms (exhaustive)
        for x in Q:
            for y in Q:
                assert self.ADD[x][y] == self.ADD[y][x] and self.MUL[x][y] == self.MUL[y][x]
                for z in Q:
                    assert self.ADD[self.ADD[x][y]][z] == self.ADD[x][self.ADD[y][z]]
                    assert self.MUL[self.MUL[x][y]][z] == self.MUL[x][self.MUL[y][z]]
                    assert self.MUL[x][self.ADD[y][z]] == self.ADD[self.MUL[x][y]][self.MUL[x][z]]
        self.prime_sub = [x for x in Q if x < self.p]  # F_p inside (encoding a + 0 i)

    # ---- polynomials ----
    def trim(self, a):
        a = list(a)
        while a and a[-1] == 0:
            a.pop()
        return tuple(a)

    def add(self, a, b):
        n = max(len(a), len(b)); A = self.ADD
        return self.trim(A[a[i] if i < len(a) else 0][b[i] if i < len(b) else 0] for i in range(n))

    def neg(self, a):
        return tuple(self.NEG[x] for x in a)

    def sub(self, a, b):
        return self.add(a, self.neg(b))

    def scal(self, c, a):
        return self.trim(self.MUL[c][x] for x in a)

    def mul(self, a, b):
        if not a or not b:
            return ()
        r = [0] * (len(a) + len(b) - 1); A, M = self.ADD, self.MUL
        for i, x in enumerate(a):
            if x:
                Mx = M[x]
                for j, y in enumerate(b):
                    if y:
                        r[i + j] = A[r[i + j]][Mx[y]]
        return self.trim(r)

    def divmod(self, a, b):
        assert b, "division by zero poly"
        a = list(a); db = len(b) - 1; ib = self.INV[b[-1]]; A, M, N = self.ADD, self.MUL, self.NEG
        if len(a) - 1 < db:
            return (), self.trim(a)
        qt = [0] * (len(a) - db)
        for i in range(len(a) - 1, db - 1, -1):
            c = a[i]
            if c:
                f = M[c][ib]; qt[i - db] = f; nf = N[f]
                for j in range(db + 1):
                    if b[j]:
                        a[i - db + j] = A[a[i - db + j]][M[nf][b[j]]]
        return self.trim(qt), self.trim(a[:db])

    def mod(self, a, b):
        return self.divmod(a, b)[1]

    def divides(self, b, a):
        return not self.mod(a, b)

    def exact(self, a, b):
        qt, r = self.divmod(a, b); assert not r, "inexact division"; return qt

    def gcd(self, a, b):
        while b:
            a, b = b, self.mod(a, b)
        return self.monic(a) if a else ()

    def monic(self, a):
        return self.scal(self.INV[a[-1]], a) if a else ()

    def lc(self, a):
        return a[-1]

    def deg(self, a):
        return len(a) - 1

    def vT(self, a):
        assert a
        i = 0
        while a[i] == 0:
            i += 1
        return i

    def Tpow(self, m):
        return tuple([0] * m + [1])

    def tfree(self, a):  # prime-to-T part
        return a[self.vT(a):]

    def const(self, c):
        return (c,) if c else ()

    def monics(self, d):
        for t in itertools.product(range(self.q), repeat=d):
            yield tuple(t) + (1,)

    def monics_upto(self, D):
        for d in range(D + 1):
            yield from self.monics(d)

    def inv_mod(self, a, m):
        # extended Euclid; returns x with a x == 1 mod m
        r0, r1, s0, s1 = m, self.mod(a, m), (), (1,)
        while r1:
            qt, r = self.divmod(r0, r1)
            r0, r1 = r1, r
            s0, s1 = s1, self.sub(s0, self.mul(qt, s1))
        assert len(r0) == 1, "not invertible"
        return self.mod(self.scal(self.INV[r0[0]], s0), m)

    def crt(self, r1, m1, r2, m2):
        # x == r1 mod m1, x == r2 mod m2 (coprime); least residue mod m1 m2
        i = self.inv_mod(m1, m2)
        t = self.mod(self.mul(self.sub(r2, r1), i), m2)
        return self.mod(self.add(r1, self.mul(m1, t)), self.mul(m1, m2))

    def powmod(self, a, e, m):
        r = (1,); a = self.mod(a, m)
        while e:
            if e & 1:
                r = self.mod(self.mul(r, a), m)
            a = self.mod(self.mul(a, a), m); e >>= 1
        return r

    def irreducible(self, f):
        """Ben-Or: f monic of degree n irreducible iff gcd(x^{q^i} - x, f) = 1 for i <= n/2."""
        n = self.deg(f)
        if n <= 0:
            return False
        x = (0, 1); h = x
        for i in range(1, n // 2 + 1):
            h = self.powmod(h, self.q, f)
            if len(self.gcd(self.sub(h, x), f)) > 1:
                return False
        return True

    def irreducibles(self, d):
        if not hasattr(self, '_irr'):
            self._irr = {}
        if d not in self._irr:
            self._irr[d] = [f for f in self.monics(d) if self.irreducible(f)]
        return self._irr[d]

    def factor(self, f):
        """monic factorisation {irreducible: exponent} of nonzero f, trial division by irreducibles of degree <= deg/2."""
        f = self.monic(f); out = {}; d = 1
        while 2 * d <= self.deg(f):
            for p in self.irreducibles(d):
                while True:
                    qt, r = self.divmod(f, p)
                    if r:
                        break
                    out[p] = out.get(p, 0) + 1; f = qt
            d += 1
        if self.deg(f) > 0:
            out[f] = out.get(f, 0) + 1
        return out

    def monic_divisors(self, f):
        """all monic divisors of nonzero f (from the factorisation)."""
        divs = [(1,)]
        for p, e in self.factor(f).items():
            new = []
            for dv in divs:
                x = dv
                for _ in range(e + 1):
                    new.append(x); x = self.mul(x, p)
            divs = new
        return divs

    def monic_divisors_slow(self, f):
        f = self.monic(f); n = self.deg(f)
        return [g for d in range(n + 1) for g in self.monics(d) if self.divides(g, f)]


if __name__ == '__main__':
    for q in (3, 5, 7, 9):
        F = Field(q)
        rnd = random.Random(q)
        for _ in range(300):
            a = F.trim(rnd.randrange(q) for _ in range(rnd.randrange(8)))
            b = F.trim(rnd.randrange(q) for _ in range(1 + rnd.randrange(6)))
            if not b:
                continue
            qt, r = F.divmod(a, b)
            assert F.add(F.mul(qt, b), r) == a and len(r) < len(b)
            if len(F.gcd(b, F.Tpow(3))) == 1 and b:
                m = F.Tpow(5)
                if b[0]:
                    assert F.mod(F.mul(F.inv_mod(b, m), b), m) == (1,)
        # count irreducibles of degree 1..4 against necklace formula
        for n in range(1, 5 if q < 9 else 4):
            cnt = sum(1 for f in F.monics(n) if F.irreducible(f))
            from sympy import mobius, divisors
            exp = sum(mobius(n // d) * q ** d for d in divisors(n)) // n
            assert cnt == exp, (q, n, cnt, exp)
        for _ in range(100):
            f = F.trim(rnd.randrange(q) for _ in range(1 + rnd.randrange(7 if q < 9 else 5)))
            if f:
                assert sorted(F.monic_divisors(f)) == sorted(F.monic_divisors_slow(f))
        print("GF(%d) ok" % q)
