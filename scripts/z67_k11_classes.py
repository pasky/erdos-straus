"""z67 K11: all ET Prop 1.9 family classes with modulus dividing a smooth level Q, filtered to the K-box.

K-box B = {pi : pi = 1 mod 840, pi_11 a non-residue mod 11}.  A primitive class r mod m meets B iff
r = 1 mod gcd(m, 840) and (if 11 | m) r is a non-residue mod 11.  Only such classes are returned.

Families (ET Prop 1.9, read in sources/elsholtz-tao-1107.1010.pdf p. 8 and Section 10):
  I-1   n = -f mod 4ad,                       f | 4a^2 d + 1
  I-2   n = -f mod 4ac, n = -c/a mod f,         (4ac, f) = 1                (modulus 4acf)
  I-3   n = -f mod 4cd, n^2 = -4c^2 d mod f,    (4cd, f) = 1                (modulus 4cdf, every root)
  I-4   n = -1/e mod 4ab,                     e | a + b, (e, 4ab) = 1
  II-1  n = -e mod 4ab,                       e | a + b, (e, 4ab) = 1
  II-2  n = -4a^2 d mod f,                    4ad | f + 1
  II-3  n = -4a^2 d - e mod 4ade,             (4ad, e) = 1
Usage (library): classes_dividing(Q_exponents) -> dict m -> set of residues r (mod m), B-compatible, primitive.
"""
from functools import lru_cache
from itertools import product
from math import gcd

import cypari2

pari = cypari2.Pari()


@lru_cache(maxsize=None)
def divisors_of(n):
    if n == 1:
        return (1,)
    return tuple(int(x) for x in pari.divisors(n))


def smooth_divisors(exps):
    """exps: dict p -> e.  All divisors of prod p^e."""
    ps = sorted(exps)
    out = [1]
    for p in ps:
        out = [d * p ** k for d in out for k in range(exps[p] + 1)]
    return sorted(out)


def is_nonres11(r):
    return pow(r % 11, 5, 11) == 10


def compatible(r, m):
    r %= m
    if gcd(r, m) != 1:
        return False
    g = gcd(m, 840)
    if r % g != 1 % g:
        return False
    if m % 11 == 0 and not is_nonres11(r):
        return False
    return True


def sqrt_mod_all(a, f):
    """All x mod f (f odd) with x^2 = a mod f and gcd(x, f) = 1."""
    a %= f
    if f == 1:
        return [0]
    fac = pari.factor(f)
    parts = []
    for i in range(len(fac[0])):
        p, e = int(fac[0][i]), int(fac[1][i])
        pe = p ** e
        if a % p == 0:
            return []
        if pow(a, (p - 1) // 2, p) != 1:
            return []
        r = int(pari.Mod(a, p).sqrt().lift())
        roots = {r % p, (-r) % p}
        # Hensel lift (p odd, a unit)
        cur = roots
        pk = p
        for _ in range(1, e):
            pk2 = pk * p
            nxt = set()
            for x in cur:
                # x^2 = a mod pk; lift x + t pk
                t = ((a - x * x) // pk) * pow(2 * x, -1, p) % p
                nxt.add((x + t * pk) % pk2)
            cur = nxt
            pk = pk2
        parts.append((pe, sorted(cur)))
    res = [0]
    mod = 1
    for pe, rs in parts:
        new = []
        for x in res:
            for y in rs:
                # CRT x mod mod, y mod pe
                z = x + mod * (((y - x) * pow(mod, -1, pe)) % pe)
                new.append(z % (mod * pe))
        res = new
        mod *= pe
    return res


def classes_dividing(exps, families=("I1", "I2", "I3", "I4", "II1", "II2", "II3"), tag=False):
    """dict m -> set(r) (or set((r, fam)) if tag) for all B-compatible family classes with m | Q."""
    Q = 1
    for p, e in exps.items():
        Q *= p ** e
    divs = smooth_divisors(exps)
    divset = set(divs)
    S = {}

    def add(r, m, fam):
        r %= m
        if compatible(r, m):
            S.setdefault(m, set()).add((r, fam) if tag else r)

    four = [m for m in divs if m % 4 == 0]
    for m in four:
        P = m // 4
        for a in divisors_of(P):
            d = P // a
            if "I1" in families:
                for f in divisors_of(4 * a * a * d + 1):
                    add(-f, m, "I1")
            if "I4" in families or "II1" in families:
                b = d
                for e in divisors_of(a + b):
                    if gcd(e, 4 * a * b) == 1:
                        if "II1" in families:
                            add(-e, m, "II1")
                        if "I4" in families:
                            add(-pow(e, -1, m), m, "I4")
            if "I2" in families or "I3" in families:
                for f in divs:
                    if f == 1 or f % 2 == 0 or gcd(f, m) != 1 or (m * f) not in divset:
                        continue
                    M = m * f
                    inv = pow(m, -1, f)
                    c1 = (-f) % m
                    tgt = []
                    if "I2" in families:                    # (a, c) = (a, d)
                        tgt.append(((-d * pow(a, -1, f)) % f, "I2"))
                    if "I3" in families:                    # (c, d) = (a, d)
                        tgt += [(x, "I3") for x in sqrt_mod_all(-4 * a * a * d, f)]
                    for c2, fam in tgt:
                        add(c1 + m * (((c2 - c1) * inv) % f), M, fam)
        if "II3" in families:
            for e in divisors_of(P):
                ad = P // e
                if gcd(4 * ad, e) != 1:
                    continue
                for a in divisors_of(ad):
                    d = ad // a
                    add(-4 * a * a * d - e, m, "II3")
    if "II2" in families:
        for f in divs:
            if (f + 1) % 4:
                continue
            P = (f + 1) // 4
            for a in divisors_of(P):
                if gcd(a, f) != 1:
                    continue
                for d in divisors_of(P // a):
                    add(-4 * a * a * d, f, "II2")
    return S


if __name__ == "__main__":
    import sys
    exps = {}
    for tok in sys.argv[1:]:
        p, e = tok.split("^")
        exps[int(p)] = int(e)
    S = classes_dividing(exps)
    print(len(S), sum(len(v) for v in S.values()))
