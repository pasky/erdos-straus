"""R195 from-scratch GF(q) and GF(q)[T] arithmetic (q any prime power) for the review of FF_MUTE.md.
Field elements: ints 0..q-1 (base-p digits = coefficients of alpha^i, alpha root of a fixed irreducible).
Polynomials: tuples of field elements, low degree first, no trailing zeros; () is zero.
Independent of scripts/fm_*.py."""
import itertools


def _int_irred_poly(p, r):
    # find monic irreducible of degree r over F_p by brute force (r <= 4)
    for tail in itertools.product(range(p), repeat=r):
        c = list(tail) + [1]
        if c[0] == 0:
            continue
        # no roots in F_{p^j} for j<=r/2: test by brute-force factor search over monic polys of deg <= r//2
        ok = True
        for dd in range(1, r // 2 + 1):
            for t2 in itertools.product(range(p), repeat=dd):
                g = list(t2) + [1]
                # remainder of c mod g over F_p
                rem = c[:]
                for i in range(len(rem) - 1, dd - 1, -1):
                    co = rem[i]
                    if co:
                        for j in range(dd + 1):
                            rem[i - dd + j] = (rem[i - dd + j] - co * g[j]) % p
                if all(x == 0 for x in rem[:dd]):
                    ok = False
                    break
            if not ok:
                break
        if ok:
            return c
    raise ValueError


class GF:
    def __init__(self, q):
        p = None
        for cand in range(2, q + 1):
            if q % cand == 0:
                p = cand
                break
        r = 0
        t = q
        while t > 1:
            assert t % p == 0
            t //= p
            r += 1
        self.q, self.p, self.r = q, p, r
        digs = lambda x: [(x // p ** i) % p for i in range(r)]
        und = lambda v: sum(v[i] * p ** i for i in range(r))
        self.add = [[und([(a + b) % p for a, b in zip(digs(x), digs(y))]) for y in range(q)] for x in range(q)]
        self.neg = [und([(-a) % p for a in digs(x)]) for x in range(q)]
        if r == 1:
            self.mul = [[(x * y) % p for y in range(q)] for x in range(q)]
        else:
            m = _int_irred_poly(p, r)
            self.modpoly = m

            def pm(x, y):
                a, b = digs(x), digs(y)
                pr = [0] * (2 * r - 1)
                for i in range(r):
                    for j in range(r):
                        pr[i + j] = (pr[i + j] + a[i] * b[j]) % p
                for i in range(2 * r - 2, r - 1, -1):
                    co = pr[i]
                    if co:
                        for j in range(r + 1):
                            pr[i - r + j] = (pr[i - r + j] - co * m[j]) % p
                return und(pr[:r])
            self.mul = [[pm(x, y) for y in range(q)] for x in range(q)]
        self.inv = [None] + [next(y for y in range(1, q) if self.mul[x][y] == 1) for x in range(1, q)]
        self.sub = [[self.add[x][self.neg[y]] for y in range(q)] for x in range(q)]
        self.one = 1
        self.minus_one = self.neg[1]
        # sanity: field axioms on small sample
        for x in range(q):
            for y in range(q):
                assert self.mul[x][y] == self.mul[y][x]
                for z in range(q):
                    assert self.mul[x][self.add[y][z]] == self.add[self.mul[x][y]][self.mul[x][z]]
        assert all(self.inv[x] is not None for x in range(1, q))
        # multiplicative generator
        for g in range(1, q):
            seen, x = set(), 1
            for _ in range(q - 1):
                x = self.mul[x][g]
                seen.add(x)
            if len(seen) == q - 1:
                self.gen = g
                break

    # ---- polynomials ----
    @staticmethod
    def trim(a):
        a = list(a)
        while a and a[-1] == 0:
            a.pop()
        return tuple(a)

    def padd(self, a, b):
        n = max(len(a), len(b))
        A = self.add
        return self.trim([A[a[i] if i < len(a) else 0][b[i] if i < len(b) else 0] for i in range(n)])

    def psub(self, a, b):
        n = max(len(a), len(b))
        S = self.sub
        return self.trim([S[a[i] if i < len(a) else 0][b[i] if i < len(b) else 0] for i in range(n)])

    def pscale(self, c, a):
        M = self.mul[c]
        return self.trim([M[x] for x in a])

    def pmul(self, a, b):
        if not a or not b:
            return ()
        res = [0] * (len(a) + len(b) - 1)
        A, M = self.add, self.mul
        for i, x in enumerate(a):
            if x:
                Mx = M[x]
                for j, y in enumerate(b):
                    if y:
                        res[i + j] = A[res[i + j]][Mx[y]]
        return self.trim(res)

    def pdivmod(self, a, b):
        assert b
        a = list(a)
        db = len(b) - 1
        ilc = self.inv[b[-1]]
        if len(a) - 1 < db:
            return (), self.trim(a)
        qt = [0] * (len(a) - db)
        S, M = self.sub, self.mul
        for i in range(len(a) - 1, db - 1, -1):
            co = a[i]
            if co:
                c = M[co][ilc]
                qt[i - db] = c
                Mc = M[c]
                for j in range(db + 1):
                    a[i - db + j] = S[a[i - db + j]][Mc[b[j]]]
        return self.trim(qt), self.trim(a[:db])

    def pmod(self, a, b):
        return self.pdivmod(a, b)[1]

    def ppowmod(self, a, e, m):
        res = (1,)
        a = self.pmod(a, m)
        while e:
            if e & 1:
                res = self.pmod(self.pmul(res, a), m)
            e >>= 1
            if e:
                a = self.pmod(self.pmul(a, a), m)
        return res if len(m) > 1 else ()

    def ppow(self, a, e):
        res = (1,)
        for _ in range(e):
            res = self.pmul(res, a)
        return res

    def pgcd(self, a, b):
        while b:
            a, b = b, self.pmod(a, b)
        return self.pscale(self.inv[a[-1]], a) if a else a

    @staticmethod
    def deg(a):
        return len(a) - 1

    def monics(self, n):
        for tail in itertools.product(range(self.q), repeat=n):
            yield tuple(tail) + (1,)

    def is_irred(self, f):
        n = len(f) - 1
        if n <= 0:
            return False
        if n == 1:
            return True
        T = (0, 1)
        # Rabin: T^{q^n} = T mod f and gcd(T^{q^{n/r}} - T, f) = 1 for primes r | n
        x = T
        pows = {}
        for i in range(1, n + 1):
            x = self.ppowmod(x, self.q, f)
            pows[i] = x
        if self.psub(pows[n], T) != ():
            return False
        for r in set(pr for pr in range(2, n + 1) if n % pr == 0 and all(pr % t for t in range(2, pr))):
            g = self.pgcd(f, self.psub(pows[n // r], T))
            if len(g) > 1:
                return False
        return True

    def irreds(self, n):
        return [f for f in self.monics(n) if self.is_irred(f)]

    def factor(self, a):
        """monic irreducible factorisation by trial division (small degrees only). returns dict."""
        a = self.pscale(self.inv[a[-1]], a)
        res = {}
        d = 1
        while len(a) - 1 >= 2 * d:
            for g in self.irreds_cached(d):
                while True:
                    qt, r = self.pdivmod(a, g)
                    if r:
                        break
                    res[g] = res.get(g, 0) + 1
                    a = qt
            d += 1
        if len(a) > 1:
            res[a] = res.get(a, 0) + 1
        return res

    _ic = None

    def irreds_cached(self, d):
        if self._ic is None:
            self._ic = {}
        if d not in self._ic:
            self._ic[d] = self.irreds(d)
        return self._ic[d]

    # ---- residue symbols by direct definition ----
    def const_val(self, a):
        assert len(a) <= 1
        return a[0] if a else 0

    def power_symbol_prime(self, a, f, ell):
        """(a/f)_ell := a^{(q^d-1)/ell} mod f in mu_ell subset F_q (f monic irreducible, ell | q-1). 0 if f|a."""
        d = len(f) - 1
        assert (self.q - 1) % ell == 0
        v = self.ppowmod(a, (self.q ** d - 1) // ell, f)
        assert len(v) <= 1
        return self.const_val(v)

    def jacobi(self, a, b, ell=2):
        """generalised symbol (a/b)_ell for monic b: product over prime factors; returns field element (0 if not coprime)."""
        val = 1
        for g, e in self.factor(b).items():
            s = self.power_symbol_prime(a, g, ell)
            for _ in range(e):
                val = self.mul[val][s]
        return val

    def chi_const(self, c, ell=2):
        """c^{(q-1)/ell} in F_q"""
        x = 1
        for _ in range((self.q - 1) // ell):
            x = self.mul[x][c]
        return x
