"""R245: certificate-independent brute-force ES search for n = 4^s + 105, small s; and T1 (non-square) checks of the ET classes."""
import json
from math import isqrt
def es(n):
    for x in range(n // 4 + 1, n + 1):
        p, q = 4 * x - n, n * x
        for y in range(max(x, q // p + 1), 2 * q // p + 1):
            num = p * y - q
            if num > 0 and (q * y) % num == 0:
                return x, y, q * y // num
for s in range(0, 9):
    n = 4**s + 105; sol = es(n)
    x, y, z = sol; assert 4 * x * y * z == n * (x * y + y * z + z * x)
    print(s, n, sol)
# T1: each non-divisor class r mod M contains no odd square (r non-residue mod M)
J = json.load(open('data/s6_cert105_et.json'))
for C in J['classes']:
    M, r = C['M'], C['r']
    sq = {t * t % M for t in range(M)}
    print(C['fam'], M, r, 'square-free class' if r not in sq else 'CONTAINS SQUARES' + (' (divisor class, fine)' if r == 0 else ''))
