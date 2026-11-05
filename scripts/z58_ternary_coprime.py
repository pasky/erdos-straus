# z58 TERNARY: composite (non-square) R-zeros <= 1e10 (LOGIC census) by gcd with small primorials; largest ones.
import gzip
from math import isqrt, gcd
from sympy import isprime, factorint
Z = [int(x) for x in gzip.open('data/z58/logic/zeros_1e10.txt.gz', 'rt') if x.strip() and x[0] != '#']
C = [n for n in Z if isqrt(n) ** 2 != n and not isprime(n)]
print('# composite non-square zeros <= 1e10:', len(C), 'largest', max(C))
for M, name in [(3, '3'), (15, '15'), (105, '105'), (1155, '1155'), (15015, '15015')]:
    S = [n for n in C if gcd(n, M) == 1]
    dec = {}
    for n in S: dec[len(str(n)) - 1] = dec.get(len(str(n)) - 1, 0) + 1
    print('gcd(n,%s)=1: %d zeros; largest %s; per decade %s' % (name, len(S), sorted(S)[-5:], dict(sorted(dec.items()))))
S = sorted(n for n in C if gcd(n, 105) == 1)
print('# all composite zeros coprime to 105:')
for n in S: print(n, dict(factorint(n)), 'mod840=', n % 840, 'inM' if n % 840 in (1, 121, 169, 289, 361, 529) else '')
