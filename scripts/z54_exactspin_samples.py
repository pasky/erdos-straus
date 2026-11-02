# z54 EXACTSPIN sample generator (seeded). Writes data/z54/exactspin/samples/*.txt
# random primes p = 1 (24) in [10^k, 2*10^k]; near-squares p = m^2 + k0 (p = 1 mod 4 prime, k0 in {4,16,36,64,100});
# odd squares m^2 (m odd) near 10^k.
import random, os, sys
from sympy import isprime
random.seed(5400)
out = 'data/z54/exactspin/samples'; os.makedirs(out, exist_ok=True)
def rp(k, cnt):
    s = set()
    while len(s) < cnt:
        x = random.randrange(10**k, 2 * 10**k); x -= x % 24; x += 1
        if isprime(x): s.add(x)
    return sorted(s)
cfg = {9: 2000, 10: 2000, 11: 2000, 12: 1500, 13: 800, 14: 300}
for k, c in cfg.items():
    open(f'{out}/rand_1e{k}.txt', 'w').write('\n'.join(map(str, rp(k, c))) + '\n')
for k in (10, 12, 14):
    ns = []; m = int((10**k) ** 0.5)
    while len(ns) < 200:
        for k0 in (4, 16, 36, 64, 100):
            p = m * m + k0
            if p % 4 == 1 and isprime(p): ns.append(p)
        m += 1
    open(f'{out}/nearsq_1e{k}.txt', 'w').write('\n'.join(map(str, ns[:200])) + '\n')
    sq = []; m = int((10**k) ** 0.5) | 1
    while len(sq) < 200: sq.append(m * m); m += 2
    open(f'{out}/squares_1e{k}.txt', 'w').write('\n'.join(map(str, sq)) + '\n')
