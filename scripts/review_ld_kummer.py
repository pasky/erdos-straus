"""R177 independent Kummer-signal test (cf. bsD_frobenius_closure 'Cheap numerics' / LDP_DEEP A.5).
For slices (c,d) with 4cd in {4,8,12,20,28,36} and Type I / Type II separately, test whether slice occupancy
(existence of a divisor certificate) depends on Kummer data of p (2 a cube, 3 a cube [p = 1 mod 3], 2 a 4th power
[p = 1 mod 4... restricted to p = 1 mod 8 where 2 is a QR]), stratified by the full residue p mod 4cd (and by the
relevant congruence class).  Cochran-Mantel-Haenszel z per test.
Run: PYTHONPATH=scripts uv run python scripts/review_ld_kummer.py X
"""
import sys
from math import sqrt
from collections import defaultdict
from sympy import primerange, factorint

X = int(sys.argv[1])


def divs(n):
    ds = [1]
    for l, v in factorint(n).items():
        ds = [d * l ** k for d in ds for k in range(v + 1)]
    return ds


SL = [(c, d) for cd in (1, 2, 3, 5, 7, 9) for c in range(1, cd + 1) if cd % c == 0 for d in [cd // c]]
KUM = {'2cube': (lambda p: p % 3 == 1, lambda p: pow(2, (p - 1) // 3, p) == 1),
       '3cube': (lambda p: p % 3 == 1, lambda p: pow(3, (p - 1) // 3, p) == 1),
       '2quart': (lambda p: p % 8 == 1, lambda p: pow(2, (p - 1) // 4, p) == 1)}
ps = list(primerange(11, X))
occ = {}
for c, d in SL:
    M = 4 * c * d
    for p in ps:
        if M % p == 0: continue
        occ[(c, d, 'I', p)] = any((f + p) % M == 0 for f in divs(p * p + 4 * c * c * d))
        occ[(c, d, 'II', p)] = any((f + 1) % M == 0 for f in divs(1 + 4 * c * c * d * p))
zs = []
for c, d in SL:
    M = 4 * c * d
    for typ in ('I', 'II'):
        for name, (elig, kum) in KUM.items():
            strata = defaultdict(lambda: [0, 0, 0, 0])  # n1 (kummer true), hits among n1, n0, hits among n0
            for p in ps:
                if M % p == 0 or not elig(p): continue
                s = strata[(p % M, p % 24)]
                h = occ[(c, d, typ, p)]
                if kum(p): s[0] += 1; s[1] += h
                else: s[2] += 1; s[3] += h
            O = E = V = 0.0
            for n1, a, n0, b in strata.values():
                n = n1 + n0; m = a + b
                if n < 2 or n1 == 0 or n0 == 0: continue
                O += a; E += n1 * m / n; V += n1 * n0 * m * (n - m) / (n * n * (n - 1))
            if V > 0:
                z = (O - E) / sqrt(V); zs.append(z)
                print(f'(c,d)=({c},{d}) M={M:3d} Type {typ:2s} {name:6s} z={z:+.2f}')
print('informative tests', len(zs), ' max |z|', round(max(abs(z) for z in zs), 2))
