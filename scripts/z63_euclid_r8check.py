#!/usr/bin/env python3
"""z63 EUCLID: (S) at the R8 zeros near 1e10 — find an interior length-3 word (v,t,u), u,v,t >= 2, with (A/p) = -1.
Search u = 2..U: divisors d of p+u with d ≡ -1 (mod u), d >= 2u-1, v = (p+u)/d >= 2; A = d = tu-1."""
import sys
from sympy import factorint, divisors, jacobi_symbol
for line in open(sys.argv[1]):
    if line.startswith('#') or not line.strip():
        continue
    p = int(line.split()[0])
    found = None
    for u in range(2, 400):
        for d in divisors(p + u):
            if d % u == u - 1 and d >= 2 * u - 1 and (p + u) // d >= 2:
                if jacobi_symbol(d, p) == -1:
                    found = ((p + u) // d, (d + 1) // u, u, d)
                    break
        if found:
            break
    v, t, u, A = found
    assert t * u * v - u - v == p and A == t * u - 1
    print(p, "word (v,t,u) =", (v, t, u), "A =", A, "(A/p) = -1")
