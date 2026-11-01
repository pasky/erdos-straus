"""z52d pass2 TO0b: exact small-q engine for ES_q(A,P) over F_p[T] (p prime), via FUNCTIONFIELD_ES.md Lemma 1.3.

Lemma 1.3 (PROVED in the repo): for P monic irreducible, P not dividing A, n = deg P >= k = deg A, ES_q(A,P) holds iff
there is a monic X of degree n-k and monic a, b dividing P*X with E := A*X - P dividing a+b != 0 and lc(a+b) = lc(E).
Then Y = kappa*P*X/a, Z = kappa*P*X/b, kappa = (a+b)/E, give A/P = 1/X+1/Y+1/Z.
Count returned = number of unordered {Y,Z} pairs (a<=b) over all such X, i.e. number of solution multisets {X,Y,Z}.

Polynomials: tuples of ints mod p, low degree first. Factorisation of X by trial division (X has degree n-k <= ~8).
usage as module: from z52d_p2_TO0b_ff import count_solutions, monic_irreducibles
"""
import itertools
from functools import lru_cache


def trim(a):
    a = list(a)
    while a and a[-1] == 0:
        a.pop()
    return tuple(a)


class F:
    def __init__(self, p):
        self.p = p

    def add(self, a, b):
        m = max(len(a), len(b))
        p = self.p
        return trim([((a[i] if i < len(a) else 0) + (b[i] if i < len(b) else 0)) % p for i in range(m)])

    def neg(self, a):
        return tuple((-x) % self.p for x in a)

    def mul(self, a, b):
        if not a or not b:
            return ()
        p = self.p
        r = [0] * (len(a) + len(b) - 1)
        for i, x in enumerate(a):
            if x:
                for j, y in enumerate(b):
                    r[i + j] = (r[i + j] + x * y) % p
        return trim(r)

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
        return trim(qt), trim(a[:db])

    def monics(self, d):
        for low in itertools.product(range(self.p), repeat=d):
            yield tuple(low) + (1,)

    def factor_monic(self, f):
        """Return list of (irreducible monic g, multiplicity) with product = f (f monic, deg>=0)."""
        out = []
        rem = f
        d = 1
        while 2 * d <= len(rem) - 1:
            for g in self.monics(d):
                e = 0
                while True:
                    q, r = self.divmod(rem, g)
                    if r:
                        break
                    rem = q
                    e += 1
                if e:
                    out.append((g, e))
            d += 1
        if len(rem) > 1:
            out.append((rem, 1))
        return out

    def is_irreducible(self, f):
        return len(f) > 1 and len(self.factor_monic(f)) == 1 and self.factor_monic(f)[0][1] == 1

    def monic_divisors(self, factors):
        """All monic divisors of product of prime powers given as [(g,e)]."""
        divs = [(1,)]
        for g, e in factors:
            new = []
            for d in divs:
                cur = d
                for _ in range(e + 1):
                    new.append(cur)
                    cur = self.mul(cur, g)
            divs = new
        return divs


def monic_irreducibles(p, n):
    """Monic irreducible polynomials of degree n over F_p."""
    f = F(p)
    out = []
    for P in f.monics(n):
        if f.is_irreducible(P):
            out.append(P)
    return out


def count_solutions(p, A, P):
    """A, P: tuples low->high, A monic deg k>=1, P monic irreducible deg n>=k, P not dividing A.
    Returns (number of distinct solution triples {X,Y,Z} (monic, X the unique denominator of degree n-k),
    one witness triple or None).  Lemma 1.3 gives (a,b) with Y = kappa*P*X/a, Z = kappa*P*X/b, but kappa is free
    (any monic kappa with a,b | PX works for the same {Y,Z}), so the (a,b) enumeration over-counts: we dedupe on
    the triple itself.  Existence is unaffected."""
    f = F(p)
    n = len(P) - 1
    k = len(A) - 1
    assert n >= k >= 1
    seen = set()
    witness = None
    for X in f.monics(n - k):
        E = f.add(f.mul(A, X), f.neg(P))
        if not E:
            continue
        fac = f.factor_monic(X) if len(X) > 1 else []
        fac = fac + [(P, 1)]
        divs = f.monic_divisors(fac)
        lcE = E[-1]
        PX = f.mul(P, X)
        for i, a in enumerate(divs):
            for b in divs[i:]:
                s = f.add(a, b)
                if not s or s[-1] != lcE:
                    continue
                _, r = f.divmod(s, E)
                if r:
                    continue
                kappa, _ = f.divmod(s, E)
                Y, _ = f.divmod(f.mul(kappa, PX), a)
                Z, _ = f.divmod(f.mul(kappa, PX), b)
                key = (X,) + tuple(sorted([Y, Z]))
                seen.add(key)
                if witness is None:
                    witness = (X, Y, Z)
    return len(seen), witness


def s2str(poly):
    return "".join(str(c) for c in reversed(poly))


def str2poly(s):
    return trim(tuple(int(c) for c in reversed(s)))


def exists_general(p, A, P, H=None, return_witness=False):
    """Lemma-free existence test: A/P = 1/X+1/Y+1/Z with X,Y,Z nonzero, leading coefficients in H (subset of F_p^*,
    default all units => 'free' leading coefficients), P nonzero (P need not be irreducible).
    Complete: by the ultrametric bound some denominator X has deg X <= deg P - deg A (any lc), and we enumerate all such X.
    For each X: r/s = (A X - P)/(P X) reduced, s monic; (rY - s)(rZ - s) = s^2 => D = rY - s is a unit times a monic
    divisor of s^2. Returns True/False (and a witness if requested)."""
    f = F(p)
    if H is None:
        H = set(range(1, p))
    n = len(P) - 1
    k = len(A) - 1
    assert n >= k >= 0
    for d in range(0, n - k + 1):
        for Xm in f.monics(d):
            for cX in H:
                X = tuple((cX * c) % p for c in Xm)
                num = f.add(f.mul(A, X), f.neg(P))
                den = f.mul(P, X)
                if not num:
                    continue
                g = gcd_poly(f, num, den)
                r, _ = f.divmod(num, g)
                s, _ = f.divmod(den, g)
                inv = pow(s[-1], p - 2, p)
                s = tuple((c * inv) % p for c in s)
                r = tuple((c * inv) % p for c in r)
                # now r/s with s monic; equation 1/Y+1/Z = r/s
                if len(r) == 0:
                    continue  # impossible for irreducible P (A X = P); degenerate otherwise
                fac = f.factor_monic(s) if len(s) > 1 else []
                fac2 = [(g_, 2 * e) for g_, e in fac]
                divs = f.monic_divisors(fac2)
                s2 = f.mul(s, s)
                for delta in divs:
                    for u in range(1, p):
                        D = tuple((u * c) % p for c in delta)
                        t1 = f.add(D, s)  # rY = D + s
                        if not t1:
                            continue
                        Yq, rr = f.divmod(t1, r)
                        if rr or not Yq:
                            continue
                        Dinv_s2, rem = f.divmod(s2, D)
                        if rem:
                            continue
                        t2 = f.add(Dinv_s2, s)
                        Zq, rr2 = f.divmod(t2, r)
                        if rr2 or not Zq:
                            continue
                        if Yq[-1] in H and Zq[-1] in H:
                            if return_witness:
                                return True, (X, Yq, Zq)
                            return True
    return (False, None) if return_witness else False


def gcd_poly(f, a, b):
    while b:
        _, rem = f.divmod(a, b)
        a, b = b, rem
    inv = pow(a[-1], f.p - 2, f.p)
    return tuple((c * inv) % f.p for c in a)
