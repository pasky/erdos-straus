"""review_fsp_poly.py (R179): from-scratch F_q[T] arithmetic (q prime) for the review of FF_STERILE_PROOF.md.
Polys are tuples of ints mod q, low->high, no trailing zeros; () is 0."""
import itertools, random

class F:
    def __init__(self, q):
        self.q = q
    def norm(self, a):
        a = [x % self.q for x in a]
        while a and a[-1] == 0:
            a.pop()
        return tuple(a)
    def add(self, a, b):
        n = max(len(a), len(b))
        return self.norm([(a[i] if i < len(a) else 0) + (b[i] if i < len(b) else 0) for i in range(n)])
    def neg(self, a):
        return self.norm([-x for x in a])
    def sub(self, a, b):
        return self.add(a, self.neg(b))
    def scal(self, c, a):
        return self.norm([c * x for x in a])
    def mul(self, a, b):
        if not a or not b:
            return ()
        r = [0] * (len(a) + len(b) - 1)
        for i, x in enumerate(a):
            if x:
                for j, y in enumerate(b):
                    r[i + j] += x * y
        return self.norm(r)
    def divmod(self, a, b):
        assert b
        q = self.q
        a = list(a)
        inv = pow(b[-1], q - 2, q)
        db = len(b) - 1
        quo = [0] * max(0, len(a) - db)
        for i in range(len(a) - 1, db - 1, -1):
            c = a[i] * inv % q
            if c:
                quo[i - db] = c
                for j, y in enumerate(b):
                    a[i - db + j] = (a[i - db + j] - c * y) % q
        return self.norm(quo), self.norm(a)
    def mod(self, a, b):
        return self.divmod(a, b)[1]
    def deg(self, a):
        return len(a) - 1
    def gcd(self, a, b):
        while b:
            a, b = b, self.mod(a, b)
        return self.monic(a) if a else a
    def monic(self, a):
        return self.scal(pow(a[-1], self.q - 2, self.q), a)
    def powmod(self, a, e, m):
        r = (1,)
        a = self.mod(a, m)
        while e:
            if e & 1:
                r = self.mod(self.mul(r, a), m)
            a = self.mod(self.mul(a, a), m)
            e >>= 1
        return self.mod(r, m)
    def T(self, k=1):
        return tuple([0] * k + [1])
    def vT(self, a):
        """T-adic valuation (inf for 0)"""
        if not a:
            return 10 ** 9
        i = 0
        while a[i] == 0:
            i += 1
        return i
    def monics(self, d, const_nonzero=True):
        q = self.q
        if d == 0:
            yield (1,)
            return
        c0s = range(1, q) if const_nonzero else range(q)
        for c0 in c0s:
            for mid in itertools.product(range(q), repeat=d - 1):
                yield (c0,) + mid + (1,)
    def is_irred(self, f):
        """Rabin/Ben-Or test for monic f"""
        d = self.deg(f)
        if d <= 0:
            return False
        x = self.T()
        xp = x
        for i in range(1, d // 2 + 1):
            xp = self.powmod(xp, self.q, f)
            if self.deg(self.gcd(f, self.sub(xp, x))) > 0:
                return False
        return True
    # --- factorisation (squarefree + DDF + Cantor-Zassenhaus, odd q) ---
    def deriv(self, a):
        return self.norm([i * a[i] for i in range(1, len(a))])
    def factor(self, f):
        """returns dict monic irreducible -> multiplicity, f monic"""
        out = {}
        self._factor(self.monic(f), 1, out)
        return out
    def _factor(self, f, mult, out):
        if self.deg(f) <= 0:
            return
        df = self.deriv(f)
        if not df:  # f = g^p
            g = self.norm([f[i] for i in range(0, len(f), self.q)])
            self._factor(g, mult * self.q, out)
            return
        g = self.gcd(f, df)
        if self.deg(g) == 0:
            for p in self._sqfree_factor(f):
                out[p] = out.get(p, 0) + mult
            return
        h = self.divmod(f, g)[0]
        self._factor(h, mult, out)
        self._factor(g, mult, out)
    def _sqfree_factor(self, f):
        res = []
        x = self.T()
        xp = x
        i = 0
        while self.deg(f) > 0:
            i += 1
            if 2 * i > self.deg(f):
                res += [f]
                break
            xp = self.powmod(xp, self.q, f)
            g = self.gcd(f, self.sub(xp, x))
            if self.deg(g) > 0:
                res += self._edf(g, i)
                f = self.divmod(f, g)[0]
                xp = self.mod(xp, f) if self.deg(f) > 0 else xp
        return res
    def _edf(self, f, d):
        if self.deg(f) == d:
            return [f]
        rng = random.Random(12345 + self.deg(f))
        while True:
            a = self.norm([rng.randrange(self.q) for _ in range(self.deg(f))])
            if self.deg(a) <= 0:
                continue
            e = (self.q ** d - 1) // 2
            b = self.sub(self.powmod(a, e, f), (1,))
            g = self.gcd(f, b)
            if 0 < self.deg(g) < self.deg(f):
                return self._edf(g, d) + self._edf(self.divmod(f, g)[0], d)

def s(a):
    return ''.join(map(str, a)) if a else '0'
