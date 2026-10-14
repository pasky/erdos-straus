"""O208 memo s3_lll_lenstra: where Type II certificates sit relative to the Lenstra (s > N^{1/3}) and
Coppersmith (s > N^{1/4}) regimes. Cube point (c,d,j) with partner s: 4csdj = pj + c + s (COMPOSITION_ES Prop 5.1),
line (d,j): N = 4dj^2 p + 1 = (4cdj - 1)(4sdj - 1), modulus 4dj. Usage: s3_lenstra_regime.py PMAX"""
import sys
from collections import Counter, defaultdict
from sympy import primerange
PMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 3000
tot = Counter()
maxline = 0
minfrac_low = 1.0
for p in primerange(5, PMAX):
    lines = defaultdict(set)
    for d in range(1, p + 2):
        c = 1
        while 4 * d * c * c <= p + 2 * c:            # c <= s
            den = 4 * d * c - 1
            for s in range(max(c, p // (4 * d * c) + 1), (p + c) // den + 1):
                e = 4 * d * c * s - p
                if e > 0 and (c + s) % e == 0:
                    j = (c + s) // e
                    assert 4 * c * s * d * j == p * j + c + s
                    lines[(d, j)].add(min(4*c*d*j - 1, 4*s*d*j - 1))
            c += 1
    cnt = Counter()
    for (d, j), hs in lines.items():
        Nn = 4 * d * j * j * p + 1
        m = 4 * d * j
        reg = 'lenstra' if m ** 3 > Nn else ('copper' if m ** 4 > Nn else 'low')
        cnt[reg] += len(hs)
        if reg == 'lenstra':
            maxline = max(maxline, len(hs))
    tot.update(cnt)
    if sum(cnt.values()):
        minfrac_low = min(minfrac_low, cnt['low'] / sum(cnt.values()))
print('Type II certificate pairs {h, h*} by line regime, primes < %d:' % PMAX, dict(tot))
print('max certificates on one Lenstra-regime line:', maxline, '(Lenstra bound 11 for divisors in one class)')
print('min share of low-regime (s <= N^{1/4}) certificates at a single prime: %.3f' % minfrac_low)
