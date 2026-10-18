"""O267 §3: build n-lists for z37_rss.c: generic primes, near-square primes m^2+K, odd squares. Writes /tmp/z37/set_*.txt"""
from sympy import isprime
import os
os.makedirs('/tmp/z37', exist_ok=True)
lo, hi = 400000, 4000000
g = [p for p in range(1000001, 1060000, 4) if isprime(p)]
open('/tmp/z37/set_generic.txt', 'w').write('\n'.join(map(str, g)) + '\n')
for K in (1, 4, 9, 16, 24, 25, 36, 49, 64, 2, 8, 12, -3, -4, -8, -15, -24):
    L = []
    m = int(lo ** .5)
    while m * m + K <= hi:
        p = m * m + K
        if p % 4 == 1 and isprime(p): L.append(p)
        m += 1
    open(f'/tmp/z37/set_K{K}.txt', 'w').write('\n'.join(map(str, L)) + '\n')
    print(K, len(L))
sq = [m * m for m in range(633, 2000, 2) if (m * m) % 4 == 1]
open('/tmp/z37/set_sq.txt', 'w').write('\n'.join(map(str, sq)) + '\n')
print('generic', len(g), 'squares', len(sq))
