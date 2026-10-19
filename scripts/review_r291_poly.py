"""R291: tiny exact polynomial arithmetic over Q (from scratch) + root-rule checker.

A root rule: Y = 2^{E(s)}, E(s) = (A*s - B)/C, defined for s with C | A*s-B and E(s) >= 0.
Coordinates x,y,z in Q[Y].  We check
  (i)  4xyz = n(Y)(xy+yz+zx) identically, and n(Y) = n_s numerically,
  (ii) the exact set of s (in one full period beyond a threshold) where x,y,z are positive
       integers (and optional extra 'parameter' polynomials are integers),
  (iii) exact solutions numerically for s <= SMAX.
"""
from fractions import Fraction as F
from math import gcd, lcm


def P(*c):
    return trim([F(x) for x in c])


def trim(p):
    p = list(p)
    while p and p[-1] == 0:
        p.pop()
    return p


def add(p, q):
    r = [F(0)] * max(len(p), len(q))
    for i, c in enumerate(p):
        r[i] += c
    for i, c in enumerate(q):
        r[i] += c
    return trim(r)


def neg(p):
    return [-c for c in p]


def sub(p, q):
    return add(p, neg(q))


def mul(p, q):
    if not p or not q:
        return []
    r = [F(0)] * (len(p) + len(q) - 1)
    for i, a in enumerate(p):
        for j, b in enumerate(q):
            r[i + j] += a * b
    return trim(r)


def smul(c, p):
    return trim([F(c) * x for x in p])


def divmod_(p, q):
    p = list(p)
    out = [F(0)] * max(1, len(p) - len(q) + 1)
    while len(p) >= len(q) and p:
        c = p[-1] / q[-1]
        k = len(p) - len(q)
        out[k] = c
        for i, b in enumerate(q):
            p[i + k] -= c * b
        p = trim(p)
    return trim(out), p


def exdiv(p, q):
    a, r = divmod_(p, q)
    assert not r, 'not divisible'
    return a


def ev(p, y):
    r = F(0)
    for c in reversed(p):
        r = r * y + c
    return r


def Ypow(k):
    return [F(0)] * k + [F(1)]


def den(p):
    d = 1
    for c in p:
        d = lcm(d, c.denominator)
    return d


def ordmod(b, m):
    if m == 1:
        return 1
    x, o = b % m, 1
    while x != 1:
        x = x * b % m
        o += 1
    return o


def cauchy(p):
    """all real roots have |y| < bound"""
    lc = p[-1]
    return 1 + max((abs(c / lc) for c in p[:-1]), default=0)


class Rule:
    def __init__(self, name, A, B, C, n_poly, coords, params=(), nfun=None):
        self.name, self.A, self.B, self.C = name, A, B, C
        self.n, self.coords, self.params = n_poly, coords, list(params)
        self.nfun = nfun
        x, y, z = coords
        lhs = smul(4, mul(mul(x, y), z))
        rhs = mul(n_poly, add(add(mul(x, y), mul(y, z)), mul(z, x)))
        assert sub(lhs, rhs) == [], f'identity fails for {name}'

    def E(self, s):
        num = self.A * s - self.B
        if num < 0 or num % self.C:
            return None
        return num // self.C

    def applies(self, s):
        """exact check at s (big integers)"""
        e = self.E(s)
        if e is None:
            return False
        Y = 2 ** e
        if self.nfun and ev(self.n, Y) != self.nfun(s):
            raise AssertionError(f'n(Y) != n_s at s={s} for {self.name}')
        vals = [ev(c, Y) for c in self.coords]
        if any(v <= 0 or v.denominator != 1 for v in vals):
            return False
        if any(ev(p, Y).denominator != 1 for p in self.params):
            return False
        n = ev(self.n, Y)
        assert sum(1 / v for v in vals) == 4 / n
        return True

    def period_set(self):
        """returns (Pi, thr, set of s mod Pi valid for s >= thr) using modular arithmetic"""
        polys = list(self.coords) + self.params
        Dn = 1
        for p in polys:
            Dn = lcm(Dn, den(p))
        a2, Do = 0, Dn
        while Do % 2 == 0:
            Do //= 2; a2 += 1
        Cp = self.C // gcd(self.A, self.C)
        Pi = Cp * ordmod(2, Do)
        # threshold: E >= a2 and all coordinate numerators positive (Y > Cauchy bound)
        Ybound = max(cauchy(p) for p in self.coords)
        thr = 0
        while True:
            e = self.E(thr)
            if e is not None and e >= a2 and 2 ** e > Ybound and all(
                    p[-1] > 0 for p in self.coords):
                break
            thr += 1
            if thr > 10 ** 4:
                return Pi, None, set()
        S = set()
        for s in range(thr, thr + Pi):
            e = self.E(s)
            if e is None:
                continue
            ok = True
            for p in polys:
                d = den(p)
                num = [int(c * d) for c in p]
                y = pow(2, e, d)
                v = 0
                for c in reversed(num):
                    v = (v * y + c) % d
                if v:
                    ok = False
                    break
            if ok:
                S.add(s % Pi)
        return Pi, thr, S
