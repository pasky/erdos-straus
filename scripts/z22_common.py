"""O250 common: exact Lemma-3.1 window certificates (CAP_DOWN Lemma 3.1) for prime p = 1 (mod 4).

Window m = 3 (mod 4), K = (p+m)/4 = x, generators: primes of 2K and p.
delta_s in [-b_s, b_s] (s | 2K), delta_p in {-1,0,1} (if usep), or for odd s | K: delta_s in b_s + 2*[1..e].
Certificate: prod s^delta_s = -1 (mod m).  cap = max (delta_s - b_s)/2 over overflowing s.
"""
from fractions import Fraction
from math import gcd, isqrt
from sympy import factorint


def exps(b, e, odd):
    D = list(range(-b, b + 1))
    if odd:
        D += list(range(b + 2, b + 2 * e + 1, 2))
    return D


def best_cap(p, m, emax, usep=True, fK=None):
    """least cap e <= emax with a certificate at window m (None if none); returns (e, vec)."""
    if (p + m) % 4 or gcd(m, p) != 1:
        return None
    K = (p + m) // 4
    if gcd(K, p) != 1:
        return None
    fs = dict(fK) if fK is not None else factorint(K)
    gens = list(fs.items())
    for e in range(emax + 1):
        R = {1 % m: ()}
        items = gens + ([(p, 1)] if usep else [])
        for s, b in items:
            D = exps(b, e, s != 2 and s != p) if s != p else [-1, 0, 1]
            sm = s % m
            if sm == 0:
                continue
            inv = pow(sm, -1, m)
            P = [(pow(sm, d, m) if d >= 0 else pow(inv, -d, m), d) for d in D]
            R2 = {}
            for r, vec in R.items():
                for pv, d in P:
                    rr = r * pv % m
                    if rr not in R2:
                        R2[rr] = vec + ((s, d),)
            R = R2
        if (m - 1) % m in R:
            return e, R[(m - 1) % m]
    return None


def verify(p, m, vec, e):
    """rebuild the ES^{(y,e)} solution from a certificate and check Def 1.1 exactly."""
    K = (p + m) // 4
    N = p * K
    num, den = N, 1
    for s, d in vec:
        if d >= 0:
            num *= s ** d
        else:
            den *= s ** (-d)
    assert num % den == 0
    D1 = num // den
    assert (N + D1) % m == 0
    x, y = K, (N + D1) // m
    z = Fraction(N * y, D1)
    assert Fraction(4, p) == Fraction(1, x) + Fraction(1, y) + 1 / z
    Dn = z.denominator
    r = isqrt(Dn)
    assert r * r == Dn and r % 2 == 1 and gcd(r, p) == 1 and y % max(1, 1) == 0
    for l, v in factorint(r).items():
        assert y % l == 0 and v <= e
    return x, y, z
