"""O31 (POINTWISE_TYPEI.md §5, EVIDENCE): for given hard primes p, count the unforced slices
(c,k) with ck < ck_min(p) (all of which vanish) and the model mass sum log p/(ck) over them."""
import sys, math
from sympy import factorint, legendre_symbol, primerange
sys.path.insert(0, 'scripts')
from typei_ratio import ckmin, least_qnr, sf, chi_minus_s

for p in map(int, sys.argv[1:]):
    n = least_qnr(p)
    cm = ckmin(p, 5000)
    nres = [q for q in primerange(n, cm) if legendre_symbol(q, p) == -1]
    U = 0
    mass = 0.0
    for P in range(1, cm):
        for c in range(1, P + 1):
            if P % c:
                continue
            k = P // c
            s = sf(c)
            if s in (1, 2, 3, 6):
                continue
            if chi_minus_s(s, p) == -1:
                U += 1
                mass += math.log(p) / P
    print(f"p={p} n_p={n} ck_min={cm} ratio={cm/n:.2f} log p={math.log(p):.2f} "
          f"#nonres primes in [n_p,ck_min)={len(nres)} #unforced vanishing slices={U} sum log p/ck={mass:.1f}")
