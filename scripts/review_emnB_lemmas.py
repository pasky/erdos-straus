"""R94 review B, from scratch: Lemma 1.1 identity (exhaustive small ranges) and
Lemma 2.1 (a)-(d) for S_m, h_m, including m with many small primes.
Usage: PYTHONPATH=scripts uv run python scripts/review_emnB_lemmas.py [Kmax]
"""
import sys
from fractions import Fraction
from math import gcd, log

def phi_sieve(n):
    ph = list(range(n + 1))
    for p in range(2, n + 1):
        if ph[p] == p:
            for k in range(p, n + 1, p):
                ph[k] -= ph[k] // p
    return ph

def check_identity():
    fails = 0; cnt = 0
    for m in range(4, 40):
        for k in range(1, 30):
            for l in range(1, 60):
                N = k * l + 1
                if N % m:
                    continue
                A = N // m
                # all factorizations A = u v w
                for u in range(1, A + 1):
                    if A % u: continue
                    for v in range(1, A // u + 1):
                        if (A // u) % v: continue
                        w = A // (u * v)
                        # classes n v = -u mod kl ; inverse of v mod kl exists
                        if gcd(v, k * l) != 1:
                            fails += 1; continue
                        for n in range(1, 3 * k * l + 1):
                            if (n * v + u) % (k * l): continue
                            s = (n * v + u) // (k * l)
                            cnt += 1
                            if Fraction(1, s*u*w) + Fraction(1, n*s*v*w) + Fraction(1, n*u*v*w) != Fraction(m, n):
                                fails += 1
    print(f"Lemma 1.1: {cnt} instances, {fails} failures")
    return fails

def check_h(Kmax):
    ph = phi_sieve(Kmax)
    sum_p2 = 0.4522474200410654
    ms = list(range(4, 301)) + [2*3*5*7, 2*3*5*7*11, 30030, 510510 // 17, 4 * 9 * 25 * 49]
    fails = 0; ratios = []; hs = []
    for m in ms:
        cop = [k for k in range(1, Kmax + 1) if gcd(k, m) == 1]
        # prefix sums of 1/k over coprime k (S_m) and phi(k)/k^2 (h_m)
        S = {}; acc = 0.0; idx = 0
        Svals = [0.0] * (Kmax + 1); hvals = [0.0] * (Kmax + 1)
        a1 = 0.0; a2 = 0.0; j = 0
        cs = set(cop)
        for x in range(1, Kmax + 1):
            if x in cs:
                a1 += 1.0 / x; a2 += ph[x] / x / x
            Svals[x] = a1; hvals[x] = a2
        fm = ph[m] / m if m <= Kmax else None
        if fm is None:
            # compute phi(m)/m directly
            r = 1.0; mm = m; p = 2
            while p * p <= mm:
                if mm % p == 0:
                    r *= 1 - 1 / p
                    while mm % p == 0: mm //= p
                p += 1
            if mm > 1: r *= 1 - 1 / mm
            fm = r
        # (a) for x >= m^2 (test all x in [m^2, Kmax] on a grid)
        if m * m <= Kmax:
            for x in range(m * m, Kmax + 1, max(1, (Kmax - m * m) // 2000 or 1)):
                if Svals[x] < fm * log(x) - 1e-12:
                    fails += 1; print("(a) fail", m, x)
        # (b) at all K on grid
        for K in range(1, Kmax + 1, 97):
            if hvals[K] < (1 - sum_p2) * Svals[K] - 1e-12:
                fails += 1; print("(b) fail", m, K)
        # (c) for primes p not dividing m
        for p in [2, 3, 5, 7, 11, 13, 101]:
            if m % p == 0: continue
            sub = sum(ph[k] / k / k for k in cop if k % p == 0)
            if sub > Svals[Kmax] / p + 1e-12:
                fails += 1; print("(c) fail", m, p)
        # (d) ratio S_m(K)/((phi/m) log K) for K >= m
        if m <= Kmax:
            ratios.append(Svals[Kmax] / (fm * log(Kmax)))
        hs.append(hvals[Kmax] / Svals[Kmax])
    print(f"Lemma 2.1: {len(ms)} values of m, Kmax={Kmax}, failures={fails}")
    print(f"  S_m(K)/((phi(m)/m) log K) in [{min(ratios):.3f},{max(ratios):.3f}]  (m<=Kmax)")
    print(f"  h_m/S_m in [{min(hs):.3f},{max(hs):.3f}]")
    return fails

if __name__ == "__main__":
    Kmax = int(sys.argv[1]) if len(sys.argv) > 1 else 200000
    f = check_identity() + check_h(Kmax)
    sys.exit(1 if f else 0)
