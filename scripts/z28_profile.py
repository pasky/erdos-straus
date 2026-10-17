"""O257: local profile of numerator-model exceptions E_k (from logs/z28_Ek_primes_*.txt).
For each exceptional prime p > 3k: p mod k, least quadratic non-residue q0(p), v2(p-1), factorisation of p-1,
and the 'visibility' set V(p) = {odd primes l <= 30 : (p/l) = -1}."""
import sys
from sympy import factorint, legendre_symbol, primerange

def lqnr(p):
    for q in primerange(2, 1000):
        if q == 2:
            if p % 8 in (3, 5):
                return 2
            continue
        if p % q and legendre_symbol(p % q, q) == -1:
            return q
    return None

for line in open(sys.argv[1]):
    k = int(line.split(':')[0][2:])
    ks = [int(k) for k in sys.argv[2:]] if len(sys.argv) > 2 else None
    if ks and k not in ks:
        continue
    ps = [int(t) for t in line.split(':')[1].split() if not t.startswith('#')]
    print(f"k={k}")
    for p in ps:
        if p <= 3 * k:
            continue
        f = factorint(p - 1)
        V = [l for l in primerange(3, 31) if p % l and legendre_symbol(p % l, l) == -1]
        print(f"  {p}: p%k={p % k} lqnr={lqnr(p)} p-1={'*'.join(f'{q}^{e}' if e > 1 else str(q) for q, e in f.items())} V={V}")
