"""Minimal F_p[T] arithmetic (p prime) for FF_MUTE (O195). Polys = tuples of ints, low -> high, trimmed."""
import itertools


class Fp:
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

    def scal(self, c, a):
        return self.trim([c * x % self.p for x in a])

    def mul(self, a, b):
        if not a or not b:
            return ()
        p = self.p
        r = [0] * (len(a) + len(b) - 1)
        for i, x in enumerate(a):
            if x:
                for j, y in enumerate(b):
                    r[i + j] += x * y
        return self.trim([c % p for c in r])

    def divmod(self, a, b):
        p = self.p
        a = list(a)
        inv = pow(b[-1], p - 2, p)
        db = len(b) - 1
        qt = [0] * max(len(a) - db, 0)
        for i in range(len(a) - 1, db - 1, -1):
            c = a[i] * inv % p
            if c:
                qt[i - db] = c
                for j in range(db + 1):
                    a[i - db + j] = (a[i - db + j] - c * b[j]) % p
        return self.trim(qt), self.trim(a[:db])

    def mod(self, a, b):
        return self.divmod(a, b)[1]

    def mulmod(self, a, b, m):
        return self.mod(self.mul(a, b), m)

    def powmod(self, a, e, m):
        r = (1,)
        a = self.mod(a, m)
        while e:
            if e & 1:
                r = self.mulmod(r, a, m)
            a = self.mulmod(a, a, m)
            e >>= 1
        return self.mod(r, m)

    def gcd(self, a, b):
        while b:
            a, b = b, self.mod(a, b)
        if a:
            a = self.scal(pow(a[-1], self.p - 2, self.p), a)
        return a

    def egcd_inv(self, a, m):
        """inverse of a mod m (assumes coprime)"""
        r0, r1 = m, self.mod(a, m)
        s0, s1 = (), (1,)
        while r1:
            qt, r = self.divmod(r0, r1)
            r0, r1 = r1, r
            s0, s1 = s1, self.sub(s0, self.mul(qt, s1))
        c = pow(r0[-1], self.p - 2, self.p)
        assert len(r0) == 1
        return self.mod(self.scal(c, s0), m)

    def deg(self, a):
        return len(a) - 1

    def monics(self, d):
        for low in itertools.product(range(self.p), repeat=d):
            yield tuple(low) + (1,)

    def is_irred(self, f):
        """Rabin/Ben-Or style: f monic of degree d irreducible iff gcd(T^{p^i}-T, f)=1 for i<=d/2."""
        d = len(f) - 1
        if d <= 0:
            return False
        if d == 1:
            return True
        x = (0, 1)
        t = x
        for i in range(1, d // 2 + 1):
            t = self.powmod(t, self.p, f)
            g = self.gcd(f, self.sub(t, x))
            if len(g) > 1:
                return False
        return True

    def irreducibles(self, d):
        for f in self.monics(d):
            if self.is_irred(f):
                yield f

    def val(self, a, s):
        v = 0
        while True:
            qt, r = self.divmod(a, s)
            if r:
                return v
            a = qt
            v += 1


def parse(sx):
    """'1021' (high->low digits) -> tuple low->high"""
    return tuple(int(c) for c in reversed(sx))


def show(a):
    return ''.join(str(c) for c in reversed(a)) if a else '0'
