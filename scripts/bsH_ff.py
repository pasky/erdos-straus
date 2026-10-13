"""Minimal F_p[T] arithmetic for the bsH_* scripts (O181). Polynomials are tuples of coefficients, low -> high,
trimmed (no trailing zeros); () is 0. p prime."""
import itertools


class FF:
    def __init__(self, p):
        self.p = p

    def trim(self, a):
        a = list(a)
        while a and a[-1] == 0:
            a.pop()
        return tuple(a)

    def add(self, a, b):
        p = self.p
        m = max(len(a), len(b))
        return self.trim([((a[i] if i < len(a) else 0) + (b[i] if i < len(b) else 0)) % p for i in range(m)])

    def neg(self, a):
        return tuple((-x) % self.p for x in a)

    def sub(self, a, b):
        return self.add(a, self.neg(b))

    def mul(self, a, b):
        p = self.p
        if not a or not b:
            return ()
        r = [0] * (len(a) + len(b) - 1)
        for i, x in enumerate(a):
            if x:
                for j, y in enumerate(b):
                    r[i + j] = (r[i + j] + x * y) % p
        return self.trim(r)

    def scal(self, c, a):
        return self.trim([(c * x) % self.p for x in a])

    def divmod(self, a, b):
        p = self.p
        a = list(a)
        inv = pow(b[-1], p - 2, p)
        db = len(b) - 1
        if len(a) - 1 < db:
            return (), self.trim(a)
        qt = [0] * (len(a) - db)
        for i in range(len(a) - 1, db - 1, -1):
            c = a[i] * inv % p
            if c:
                qt[i - db] = c
                for j in range(db + 1):
                    a[i - db + j] = (a[i - db + j] - c * b[j]) % p
        return self.trim(qt), self.trim(a[:db])

    def mod(self, a, b):
        return self.divmod(a, b)[1]

    def gcd(self, a, b):
        while b:
            a, b = b, self.mod(a, b)
        if a:
            a = self.scal(pow(a[-1], self.p - 2, self.p), a)
        return a

    def powmod(self, a, e, m):
        r = (1,)
        a = self.mod(a, m)
        while e:
            if e & 1:
                r = self.mod(self.mul(r, a), m)
            a = self.mod(self.mul(a, a), m)
            e >>= 1
        return r

    def monics(self, d):
        p = self.p
        for low in itertools.product(range(p), repeat=d):
            yield tuple(low) + (1,)

    def is_irred(self, f):
        d = len(f) - 1
        if d <= 0:
            return False
        # Rabin-free simple test: no monic factor of degree <= d/2
        for e in range(1, d // 2 + 1):
            for g in self.monics(e):
                if not self.mod(f, g):
                    return False
        return True

    def irreds(self, d):
        return [f for f in self.monics(d) if self.is_irred(f)]

    def factor(self, f):
        """monic factorisation by trial division: list of (prime, exponent)."""
        out = []
        d = 1
        while len(f) - 1 >= 2 * d:
            for g in self.monics(d):
                if len(f) - 1 < 2 * d:
                    break
                e = 0
                while True:
                    qq, r = self.divmod(f, g)
                    if r:
                        break
                    f = qq
                    e += 1
                if e:
                    out.append((g, e))
            d += 1
        if len(f) > 1:
            f = self.scal(pow(f[-1], self.p - 2, self.p), f)
            out.append((f, 1))
        return out

    def monic_divisors(self, f):
        fac = self.factor(f)
        divs = [(1,)]
        for g, e in fac:
            new = []
            for dv in divs:
                x = dv
                for _ in range(e + 1):
                    new.append(x)
                    x = self.mul(x, g)
            divs = new
        return divs

    def psym(self, x, g, k, gen):
        """k-th power residue symbol (x/g)_k for monic g, returned as exponent j mod k with value = w^j,
        w = gen^((p-1)/k). Returns None if gcd(x, g) != 1."""
        p = self.p
        w = pow(gen, (p - 1) // k, p)
        logs = {pow(w, j, p): j for j in range(k)}
        tot = 0
        for ell, e in self.factor(g):
            d = len(ell) - 1
            v = self.powmod(x, (p ** d - 1) // k, ell)
            if len(v) != 1:
                return None
            tot += e * logs[v[0]]
        return tot % k
