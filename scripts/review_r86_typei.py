"""R86 from-scratch: Thm 4.1 (C(5)=10) census, ckmin>=n_p, and Prop 4.5(b)/residue-one cover."""
import sys
from sympy import primerange, legendre_symbol as L, divisors, factorint
from math import gcd

def n_p(p):
    q = 2
    while True:
        if L(q % p, p) == -1: return q
        q += 1

def ckmin(p, cap=200):
    best = None
    for h in range(1, cap+1):          # height h = c*k in increasing order
        for k in range(1, h+1):
            if h % k: continue
            c = h // k
            if k > (2*p)//3 or c > (2*p+k)//(4*k) or gcd(p, c*k) != 1: continue
            N = p*p + 4*c*k*k; m = 4*c*k
            if any((D + p) % m == 0 for D in divisors(N)): return h
    return None

lim = int(sys.argv[1]) if len(sys.argv) > 1 else 300000
mx = 0; bad = 0; cnt = 0
for p in primerange(29, lim):
    if p % 24 != 1 or n_p(p) != 5: continue
    v = ckmin(p); cnt += 1
    assert v is not None and v >= 5
    if p % 5 == 2: assert v == 5, p
    mx = max(mx, v)
print("hard n_p=5 primes <", lim, ":", cnt, "max ckmin", mx, "ckmin(193)", ckmin(193))
# ckmin >= n_p on a sample of hard primes
for p in primerange(29, 60000):
    if p % 24 == 1:
        assert ckmin(p, 2000) >= n_p(p), p
print("ckmin >= n_p checked for hard p < 60000")
