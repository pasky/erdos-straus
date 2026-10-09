"""R117 from-scratch check of EXCEPTIONAL_MN4 Lemma 1.1 and identities (1.1).

For 4<=m<=13 and n in [2, NMAX]: enumerate ALL ordered Type I m-solutions
m/n = 1/x+1/y+1/z, n|x, gcd(n,yz)=1 (exact rationals), and compare with
W = sum_c w_{c,m}(n), w = #{(a,d,f): f | m a^2 d + 1, n = macd - f, 0<f<=2n}.
Checks: f_I <= 2W; (f_I>0) <=> (W>0) [for primes]; converse map of every w-tuple gives a
solution satisfying (1.1) with b >= a/2.
"""
from fractions import Fraction as Fr
from math import gcd, isqrt
import itertools, sys

def type1_solutions(m, n):
    r0 = Fr(m, n)
    sols = set()
    # sorted u<=v<=w ; u in [ceil(n/m), 3n/m]
    u = max(1, -(-n // m))
    while Fr(3, u) >= r0:
        r1 = r0 - Fr(1, u)
        if r1 > 0:
            v = max(u, int(1 / r1) + 0)
            if v < 1: v = 1
            while v >= u and Fr(2, v) >= r1:
                r2 = r1 - Fr(1, v)
                if r2 > 0 and r2.numerator == 1 and r2.denominator >= v:
                    w = r2.denominator
                    for p in set(itertools.permutations((u, v, w))):
                        x, y, z = p
                        if x % n == 0 and gcd(n, y * z) == 1:
                            sols.add(p)
                v += 1
        u += 1
    return sols

def w_tuples(m, n):
    out = []
    for c in range(1, 3 * n + 1):
        for a in range(1, 3 * n // (m * c) + 2):
            for d in range(1, 3 * n // (m * a * c) + 2):
                f = m * a * c * d - n
                if 0 < f <= 2 * n and (m * a * a * d + 1) % f == 0:
                    out.append((c, a, d, f))
    return out

def isprime(k):
    return k > 1 and all(k % p for p in range(2, isqrt(k) + 1))

NMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 90
bad = 0; checked = 0; conv = 0; withsol = 0
for m in range(4, 14):
    for n in range(2, NMAX + 1):
        if gcd(n, m) > 1:  # Type I needs (n,m)=1? record anyway
            pass
        S = type1_solutions(m, n)
        T = w_tuples(m, n)
        checked += 1
        if len(S) > 2 * len(T):
            bad += 1; print("FAIL f_I<=2W", m, n, len(S), len(T))
        if isprime(n) and ((len(S) > 0) != (len(T) > 0)):
            bad += 1; print("FAIL existence", m, n, len(S), len(T))
        if S: withsol += 1
        for (c, a, d, f) in T:
            e, r = divmod(m * a * a * d + 1, f)
            assert r == 0
            b = c * e - a
            ok = (b > 0 and m * a * b * d == n * e + 1 and c * e == a + b and m * a * c * d == n + f
                  and e * f == m * a * a * d + 1 and b * f == n * a + c and 2 * b >= a)
            x, y, z = n * d * a * b, d * a * c, d * b * c
            ok = ok and Fr(m, n) == Fr(1, x) + Fr(1, y) + Fr(1, z)
            if not ok:
                bad += 1; print("FAIL converse", m, n, (c, a, d, f))
            conv += 1
print(f"m=4..13, n=2..{NMAX}: {checked} (m,n) pairs, {withsol} with Type I sols, {conv} w-tuples checked; failures={bad}")
sys.exit(1 if bad else 0)
