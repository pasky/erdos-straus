"""R181 from-scratch F_p[T] toolkit (p prime).  Polys = tuples of ints, low->high, no trailing zeros.
Independent of scripts/bsH_*.  Provides arithmetic, monic enumeration, Cantor-Zassenhaus factorisation,
power-residue symbols and tame symbols / local invariants of (a,b)_zeta at every place of F_p(T)."""
import itertools, random

class FF:
    def __init__(self, p):
        self.p = p
        self.inv = [0] + [pow(a, p - 2, p) for a in range(1, p)]
        # generator of F_p^*
        for g in range(2 if p > 2 else 1, p):
            if all(pow(g, (p - 1) // r, p) != 1 for r in prime_factors(p - 1)):
                self.g = g; break
        self._fcache = {}

    # --- basic arithmetic
    def norm(self, a):
        a = list(x % self.p for x in a)
        while a and a[-1] == 0: a.pop()
        return tuple(a)
    def add(self, a, b):
        n = max(len(a), len(b)); p = self.p
        return self.norm([(a[i] if i < len(a) else 0) + (b[i] if i < len(b) else 0) for i in range(n)])
    def neg(self, a): return tuple((-x) % self.p for x in a)
    def sub(self, a, b): return self.add(a, self.neg(b))
    def scal(self, c, a): return self.norm([c * x for x in a])
    def mul(self, a, b):
        if not a or not b: return ()
        p = self.p; r = [0] * (len(a) + len(b) - 1)
        for i, x in enumerate(a):
            if x:
                for j, y in enumerate(b): r[i + j] += x * y
        return self.norm(r)
    def divmod(self, a, b):
        p = self.p; a = list(a); db = len(b) - 1; ib = self.inv[b[-1]]
        q = [0] * max(len(a) - db, 0)
        for i in range(len(a) - 1, db - 1, -1):
            c = a[i] % p
            if c:
                c = c * ib % p; q[i - db] = c
                for j in range(db + 1): a[i - db + j] -= c * b[j]
        return self.norm(q), self.norm(a[:db] if db > 0 else [])
    def mod(self, a, b): return self.divmod(a, b)[1]
    def deg(self, a): return len(a) - 1
    def lc(self, a): return a[-1]
    def monic(self, a): return self.scal(self.inv[a[-1]], a)
    def gcd(self, a, b):
        while b: a, b = b, self.mod(a, b)
        return self.monic(a) if a else a
    def powmod(self, a, e, m):
        r = (1,); a = self.mod(a, m)
        while e:
            if e & 1: r = self.mod(self.mul(r, a), m)
            a = self.mod(self.mul(a, a), m); e >>= 1
        return r
    def pw(self, a, e):
        r = (1,)
        for _ in range(e): r = self.mul(r, a)
        return r
    def monics(self, d):
        for cs in itertools.product(range(self.p), repeat=d):
            yield tuple(cs) + (1,)
    def deriv(self, a): return self.norm([i * a[i] for i in range(1, len(a))])

    # --- factorisation (monic part); returns dict {monic irreducible: exponent}
    def factor(self, a):
        a = self.monic(a)
        if a in self._fcache: return self._fcache[a]
        res = {}
        self._sqf(a, 1, res)
        if len(self._fcache) < 200000: self._fcache[a] = res
        return res
    def _sqf(self, a, mult, res):
        if len(a) <= 1: return
        d = self.deriv(a)
        if not d:  # a = b(T^p)
            b = tuple(a[i] for i in range(0, len(a), self.p))
            self._sqf(b, mult * self.p, res); return
        g = self.gcd(a, d)
        # a/g squarefree part containing all primes; standard Yun-free simple approach: recurse
        s = self.divmod(a, g)[0]  # squarefree kernel (primes with exponent not divisible by p)
        for f in self._ddf(self.monic(s)):
            # exponent of f in a
            e = 0; t = a
            while True:
                q, r = self.divmod(t, f)
                if r: break
                e += 1; t = q
            res[f] = res.get(f, 0) + e * mult
            a = t
        if len(a) > 1: self._sqf(a, mult, res)
    def _ddf(self, f):
        out = []; i = 1; h = (0, 1); X = (0, 1)
        while len(f) - 1 >= 2 * i:
            h = self.powmod(h, self.p, f)
            g = self.gcd(f, self.sub(h, X))
            if len(g) > 1:
                out += self._edf(g, i); f = self.divmod(f, g)[0]; h = self.mod(h, f) if len(f) > 1 else h
            i += 1
        if len(f) > 1: out.append(self.monic(f))
        return out
    def _edf(self, f, d):
        if len(f) - 1 == d: return [self.monic(f)]
        p = self.p
        while True:
            r = self.norm([random.randrange(p) for _ in range(len(f) - 1)])
            if len(r) <= 1: continue
            g = self.gcd(f, self.sub(self.powmod(r, (p ** d - 1) // 2, f), (1,)))
            if 1 < len(g) < len(f):
                return self._edf(g, d) + self._edf(self.divmod(f, g)[0], d)
    def is_irred(self, a):
        f = self.factor(a)
        return len(f) == 1 and list(f.values())[0] == 1

    # --- valuations / residues
    def val(self, a, l):
        e = 0
        while True:
            q, r = self.divmod(a, l)
            if r: return e, a
            e += 1; a = q

    def dlog(self, z, m):
        """z in mu_m subset F_p^*; return k in Z/m with z = zeta^k, zeta = g^((p-1)/m)."""
        zeta = pow(self.g, (self.p - 1) // m, self.p); t = 1
        for k in range(m):
            if t == z: return k
            t = t * zeta % self.p
        raise ValueError("not in mu_m")

    def inv_finite(self, a, b, l, m):
        """local invariant (in Z/m) at finite prime l of (a,b)_zeta, a=(an,ad), b=(bn,bd) polys."""
        va1, an = self.val(a[0], l); va2, ad = self.val(a[1], l)
        vb1, bn = self.val(b[0], l); vb2, bd = self.val(b[1], l)
        va, vb = va1 - va2, vb1 - vb2
        # unit parts mod l
        def red(n, d, e):  # (n/d)^e mod l, n,d l-units
            if e < 0: n, d, e = d, n, -e
            num = self.powmod(n, e, l); den = self.powmod(d, e, l)
            # invert den mod l via pow
            dl = len(l) - 1
            deninv = self.powmod(den, self.p ** dl - 2, l)
            return self.mod(self.mul(num, deninv), l)
        c = self.mod(self.mul(red(an, ad, vb), red(bn, bd, -va)), l)
        if (va * vb) % 2: c = self.neg(c)
        dl = len(l) - 1
        z = self.powmod(c, (self.p ** dl - 1) // m, l)
        assert len(z) == 1, z
        return self.dlog(z[0], m)

    def inv_inf(self, a, b, m):
        def sv(fr):
            n, d = fr
            return n[-1] * self.inv[d[-1]] % self.p, (len(d) - len(n))
        sa, va = sv(a); sb, vb = sv(b)
        c = pow(sa, vb % (self.p - 1), self.p) * pow(self.inv[sb], va % (self.p - 1), self.p) % self.p
        if (va * vb) % 2: c = (-c) % self.p
        return self.dlog(pow(c, (self.p - 1) // m, self.p), m)

    def all_invariants(self, a, b, m):
        """dict place -> inv in Z/m for (a,b)_zeta; place 'inf' or monic irreducible tuple."""
        places = set()
        for poly in (a[0], a[1], b[0], b[1]):
            places |= set(self.factor(poly).keys())
        out = {l: self.inv_finite(a, b, l, m) for l in places}
        out['inf'] = self.inv_inf(a, b, m)
        return out

def prime_factors(n):
    out = []; d = 2
    while d * d <= n:
        if n % d == 0:
            out.append(d)
            while n % d == 0: n //= d
        d += 1
    if n > 1: out.append(n)
    return out

def jacobi(F, a, g, m):
    """(a/g)_m Jacobi symbol, g monic, as exponent in Z/m (via factorisation of g)."""
    tot = 0
    for l, e in F.factor(g).items():
        dl = len(l) - 1
        z = F.powmod(F.mod(a, l), (F.p ** dl - 1) // m, l)
        if not z: return None
        tot += e * F.dlog(z[0], m)
    return tot % m
