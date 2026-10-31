#!/usr/bin/env python3
"""U07 Z2849: Honda weights. For primes p ≤ PMAX (capped 2000), HJ expansion p/A = [[v,t,u]] (length 3, digits ≥2),
W±(p) = Σ over A with (A/p)=±1 of (v-1)(t-1)(u-1). Same HJ recursion as bsA_hjlen.hj_direct."""
import resource; resource.setrlimit(resource.RLIMIT_AS, (1_000_000_000, 1_000_000_000))
from sympy import primerange, jacobi_symbol
def hj_digits(n, A):
    d = []
    while A > 0:
        b = -(-n // A); d.append(b); n, A = A, b * A - n
        if len(d) > 4: break
    return d
out = []
for p in primerange(5, 2001):
    Wp = Wm = 0; cnt = 0
    for A in range(1, p):
        d = hj_digits(p, A)
        if len(d) != 3: continue
        cnt += 1
        w = (d[0]-1)*(d[1]-1)*(d[2]-1)
        if jacobi_symbol(A, p) == 1: Wp += w
        else: Wm += w
    out.append((p, cnt, Wp, Wm))
print("sample (p, #A with length 3, W+, W-):", out[:8])
print("p=1009:", [o for o in out if o[0] == 1009], " p=1999:", [o for o in out if o[0] == 1999])
# closed-form check candidates: W+ - W- and W+ + W- vs p
import math
diffs = [(p, Wp - Wm) for p, c, Wp, Wm in out if p % 4 == 1][:12]
print("W+ - W- for p≡1 (4), first 12:", diffs)
