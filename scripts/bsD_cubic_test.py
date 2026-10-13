"""O177 (bsD_): does slice occupancy depend on a CUBIC character of p beyond the quadratic ones?
For slices (c,d) with 7 | 4cd or 9 | 4cd, compare hit rates of Type I (f | p^2+4c^2 d, f = -p mod 4cd) and
Type II (f | 1+4c^2 d p, f = -1 mod 4cd) among primes p < X split by the cubic class of p mod 7 (resp. mod 9),
holding all quadratic data mod 4cd fixed (we stratify by p mod 4cd's quadratic-character vector).
Run: PYTHONPATH=scripts uv run python scripts/bsD_cubic_test.py X
"""
import sys
from collections import defaultdict
from sympy import primerange, divisors

X = int(sys.argv[1]) if len(sys.argv) > 1 else 2 * 10**5


def hitI(p, c, d):
    M = 4 * c * d
    return any((f + p) % M == 0 for f in divisors(p * p + 4 * c * c * d))


def hitII(p, c, d):
    M = 4 * c * d
    return any((f + 1) % M == 0 for f in divisors(1 + 4 * c * c * d * p))


def qvec(p, M):
    """quadratic data of p mod M: p mod 8 (if 8|M) / mod 4, and Legendre symbols at odd primes of M"""
    v = [p % (8 if M % 8 == 0 else 4)]
    for q in (3, 5, 7, 11, 13):
        if M % q == 0:
            v.append(pow(p, (q - 1) // 2, q))
    return tuple(v)


for (c, d, q, cub) in [(1, 7, 7, lambda p: pow(p, 2, 7) == 1), (7, 1, 7, lambda p: pow(p, 2, 7) == 1),
                       (1, 9, 9, lambda p: p % 9 in (1, 8)), (3, 3, 9, lambda p: p % 9 in (1, 8)),
                       (2, 7, 7, lambda p: pow(p, 2, 7) == 1)]:
    M = 4 * c * d
    for typ, hit in (('I', hitI), ('II', hitII)):
        tab = defaultdict(lambda: [0, 0, 0, 0])  # qvec -> [n_cube, hit_cube, n_noncube, hit_noncube]
        for p in primerange(11, X):
            if M % p == 0:
                continue
            t = tab[qvec(p, M)]
            k = 0 if cub(p) else 2
            t[k] += 1
            t[k + 1] += hit(p, c, d)
        # pooled stratified difference
        num = den = 0.0
        rows = []
        for key, (a, b, e, g) in sorted(tab.items()):
            if a and e:
                r1, r2 = b / a, g / e
                w = a * e / (a + e)
                num += w * (r1 - r2)
                den += w
                rows.append((key, round(r1, 3), round(r2, 3), a, e))
        # z-score under binomial null (approx)
        var = 0.0
        for key, (a, b, e, g) in tab.items():
            if a and e:
                pr = (b + g) / (a + e)
                w = a * e / (a + e)
                var += w * w * pr * (1 - pr) * (1 / a + 1 / e)
        z = (num / den) / ((var ** 0.5) / den) if var > 0 else float('nan')
        print(f'slice c={c} d={d} M={M} type {typ}: stratified (cube - noncube) hit-rate diff {num/den:+.4f}, z={z:+.2f}')
        for r in rows[:6]:
            print('    stratum', r)

# ---- Part A: the Type I effect above is a CONGRUENCE effect: hit rate by full residue p mod 7 (slice c=1,d=7)
print('Part A: Type I slice (1,7), hit rate by p mod 7 (cubes mod 7 = {1,6}):')
cnt = defaultdict(lambda: [0, 0])
for p in primerange(11, X):
    t = cnt[p % 7]
    t[0] += 1
    t[1] += hitI(p, 1, 7)
print('   ', {r: round(h / n, 3) for r, (n, h) in sorted(cnt.items())})

# ---- Part B: Kummer (non-abelian) cubic/quartic data of p, stratified by the FULL residue p mod M
def kummer_test(name, pred, primefilter, S):
    for (c, d) in S:
        M = 4 * c * d
        for typ, hit in (('I', hitI), ('II', hitII)):
            tab = defaultdict(lambda: [0, 0, 0, 0])
            for p in primerange(11, X):
                if not primefilter(p) or M % p == 0:
                    continue
                t = tab[p % M]
                k = 0 if pred(p) else 2
                t[k] += 1
                t[k + 1] += hit(p, c, d)
            num = den = var = 0.0
            for key, (a, b, e, g) in tab.items():
                if a and e:
                    w = a * e / (a + e)
                    num += w * (b / a - g / e)
                    den += w
                    pr = (b + g) / (a + e)
                    var += w * w * pr * (1 - pr) * (1 / a + 1 / e)
            z = num / var ** 0.5 if var > 0 else float('nan')
            print(f'  {name}: slice ({c},{d}) M={M} type {typ}: diff {num/den:+.4f}  z={z:+.2f}')


print('Part B: Kummer data stratified by p mod 4cd')
kummer_test('2 cubic res mod p', lambda p: pow(2, (p - 1) // 3, p) == 1, lambda p: p % 3 == 1,
            [(1, 1), (1, 2), (2, 1), (1, 3), (1, 7), (3, 3)])
kummer_test('3 cubic res mod p', lambda p: pow(3, (p - 1) // 3, p) == 1, lambda p: p % 3 == 1,
            [(1, 1), (1, 2), (1, 7)])
kummer_test('2 quartic res mod p', lambda p: pow(2, (p - 1) // 4, p) == 1, lambda p: p % 8 == 1,
            [(1, 1), (1, 2), (2, 1), (1, 3), (1, 5)])
