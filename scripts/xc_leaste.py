"""O200 numerics: least exponent overflow e for ES^{(y,e)} in the S={s} shot family.
For each n in the input list, j=0..J: factor N_j = n + 4 s^{2j} (GNU `factor`), every divisor g = 3 mod 4 is a shot
(Q = s^j).  kappa = v_s((g+1)/4).  j=0: ES (e=0).  j>=1: need kappa>=1 (s | y), overflow e = max(0, j-kappa).
Outputs per n: least e, (j, g, kappa) attaining it (least j), least e among PRIME g, and exact verification.
Completeness: by EXPONENT_CAP Thm 2.1 proof, Q0 <= Q1^2 n/2 + Q1^2/2 + 1, so overflow <= t is searched completely
when s^{J-t} > s^{2t} n/2 + s^{2t}/2 + 1.
usage: xc_leaste.py s J nmin nmax {primes|squares} outfile"""
import sys, subprocess
from fractions import Fraction as F
from math import gcd
from sympy import primerange

s, J, nmin, nmax, kind, out = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]), sys.argv[5], sys.argv[6]
if kind == 'primes':
    ns = [p for p in primerange(max(nmin, 3), nmax) if p != s]
else:
    ns = [m * m for m in range(3, int(nmax ** .5) + 2, 2) if m * m >= nmin and m * m < nmax and m % s]

def vs(x):
    c = 0
    while x % s == 0: x //= s; c += 1
    return c

def divisors_from(fac):
    ds = [1]
    for q, a in fac.items():
        ds = [d * q**i for d in ds for i in range(a + 1)]
    return ds

def complete_upto(n):
    t = 0
    while s ** (J - t - 1) > s ** (2 * (t + 1)) * n / 2 + s ** (2 * (t + 1)) / 2 + 1: t += 1
    return t if s ** (J - t) > s ** (2 * t) * n / 2 + s ** (2 * t) / 2 + 1 else -1

def verify(n, j, g):
    Q = s ** j; a = n + 4 * Q * Q; assert a % g == 0 and g % 4 == 3
    m = a // g; assert (n + m) % 4 == 0
    x = (n + m) // 4; y = n * (g + 1) // 4; z = F(n * x * (g + 1), 4 * Q * Q)
    assert x > 0 and F(4, n) == F(1, x) + F(1, y) + 1 / z
    d = z.denominator; t = 0
    while d % (s * s) == 0: d //= s * s; t += 1
    assert d == 1 and (t == 0 or y % s == 0)
    return t

CH = 4000
res = []
with open(out, 'w') as fo:
    for c0 in range(0, len(ns), CH):
        chunk = ns[c0:c0 + CH]
        inp = '\n'.join(str(n + 4 * s ** (2 * j)) for n in chunk for j in range(J + 1))
        lines = subprocess.run(['factor'], input=inp, capture_output=True, text=True, check=True).stdout.split('\n')
        it = iter(lines)
        for n in chunk:
            best = None; bestprime = None
            for j in range(J + 1):
                N, fs = next(it).split(':'); N = int(N); fac = {}
                for q in map(int, fs.split()): fac[q] = fac.get(q, 0) + 1
                assert N == n + 4 * s ** (2 * j)
                for g in divisors_from(fac):
                    if g % 4 != 3: continue
                    kap = vs((g + 1) // 4)
                    if j >= 1 and kap == 0: continue
                    e = max(0, j - kap)
                    key = (e, j)
                    if best is None or key < best[0]: best = (key, g, kap)
                    if g in fac and (bestprime is None or key < bestprime[0]): bestprime = (key, g, kap)
            if best is not None:
                assert verify(n, best[0][1], best[1]) == best[0][0]
            cu = complete_upto(n)
            fo.write(f"{n} {best[0][0] if best else -1} {best[0][1] if best else -1} {best[1] if best else -1} "
                     f"{best[2] if best else -1} {bestprime[0][0] if bestprime else -1} {cu}\n")
        fo.flush()
