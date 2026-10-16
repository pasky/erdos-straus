"""R261: CAP_DOWN Prop 4.1(a) setting (K = (p+q)/4 an odd prime, primitive mod q, q prime = 3 (4), (q/p) = -1):
slice (delta_p = 0) least cap vs full Lemma-3.1 least cap. Usage: PMAX"""
import sys
from collections import Counter
from sympy import primerange, isprime, jacobi_symbol
from sympy.ntheory import n_order
from review_r261_windows import least_cap
PMAX = int(sys.argv[1])
n = 0; c = Counter(); ex = []
for q in primerange(11, 84):
    if q % 4 != 3: continue
    for p in primerange(5, PMAX):
        if p % 4 != 1 or (p + q) % 4: continue
        K = (p + q) // 4
        if K % 2 == 0 or not isprime(K) or n_order(K, q) != q - 1: continue
        s = least_cap(p, q, q, use_p=False)[0]
        f = least_cap(p, q, q)[0]
        n += 1
        assert s == (q - 3) // 4, (p, q, s)
        if f < s:
            c[q] += 1
            if len(ex) < 5: ex.append((p, q, K, s, f))
print('cases', n, 'slice cap = (q-3)/4 in all; full family strictly smaller in', sum(c.values()), dict(c), 'examples', ex)
