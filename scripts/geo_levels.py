"""O126 §5 experiment: ES at a FIXED level d (the Heegner/hyperboloid picture).
Type II at level d: exists a>=1, f | p + 4a^2 d, f = -1 (mod 4ad)        [then c=(f+1)/4ad, e=(p+4a^2d)/f].
Type I  at level d: exists a>=1, f | 4a^2 d + 1, f = -p (mod 4ad), c=(p+f)/4ad >= 1, gcd(c,p)=1.
Usage: PYTHONPATH=scripts uv run python scripts/geo_levels.py PMIN PMAX RESIDUE MOD ACAP"""
import sys
from sympy import factorint, primerange, legendre_symbol


def divisors_from(fac):
    ds = [1]
    for q, k in fac.items():
        ds = [x * q**j for x in ds for j in range(k + 1)]
    return ds


def typeII_level(p, d, acap):
    for a in range(1, acap + 1):
        m = 4 * a * d
        N = p + 4 * a * a * d
        for f in divisors_from(factorint(N)):
            if (f + 1) % m == 0:
                return a, f
    return None


def typeI_level(p, d, acap):
    for a in range(1, acap + 1):
        m = 4 * a * d
        N = 4 * a * a * d + 1
        for f in divisors_from(factorint(N)):
            if (p + f) % m == 0:
                c = (p + f) // m
                if c >= 1 and c % p:
                    return a, f
    return None


def dstar(p):
    d = 1
    while legendre_symbol((-d) % p, p) != -1 if (-d) % p else True:
        d += 1
    return d


if __name__ == "__main__":
    pmin, pmax, r, M, acap = map(int, sys.argv[1:6])
    worstII = (0, None); worstI = (0, None); failII = []; failI = []; cnt = 0
    for p in primerange(pmin, pmax):
        if p % M != r:
            continue
        cnt += 1
        s = typeII_level(p, 1, acap)
        if s is None:
            failII.append(p)
        elif s[0] > worstII[0]:
            worstII = (s[0], p)
        ds = dstar(p)
        t = typeI_level(p, ds, acap)
        if t is None:
            failI.append((p, ds))
        elif t[0] > worstI[0]:
            worstI = (t[0], (p, ds))
    print(f"primes {pmin}..{pmax} = {r} mod {M}: {cnt}; acap={acap}")
    print(f"Type II level d=1: failures {len(failII)} {failII[-15:]}; worst minimal a = {worstII}")
    print(f"Type I level d*(p): failures {len(failI)} {failI[-15:]}; worst minimal a = {worstI}")
