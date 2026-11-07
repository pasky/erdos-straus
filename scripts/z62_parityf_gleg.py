import sys
from sympy import isprime, legendre_symbol, primerange
sys.path.insert(0,'scripts')
from z62_parityf_master import master
lo, hi = int(sys.argv[1]), int(sys.argv[2])
bad = 0
for p in primerange(lo, hi):
    if p % 4 != 1: continue
    rows = master(p)
    gs = {}
    for xyz, m in rows:
        g,a,b,c,eps = m
        k = eps.count(p)
        gs.setdefault((g, k), 0); gs[(g,k)] += 1
    legs = {g: legendre_symbol(g % p, p) if g % p else 0 for (g,k) in gs}
    s = ' '.join("g=%d%s:%s%d" % (g, '-'*(k), '+' if legs[g]==1 else '-', cnt) for (g,k),cnt in sorted(gs.items()))
    print(p, p % 24, s)
    if any(v == 1 for v in legs.values()): bad += 1
print("primes with some g a QR:", bad)
