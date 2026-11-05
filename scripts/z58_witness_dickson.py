"""z58 WITNESS Prop 3.1 (CONDITIONAL on Dickson) — numerical instances.
For S >= 1 let L_S = lcm(840, 4u(u+1) (u <= S), 4C(4C+1) (C <= S)). For p = 1 + L_S k, if all of
  p,  (p+u)/(u+1) (1 <= u <= S),  (4Cp+1)/(4C+1) (1 <= C <= S)
are prime then every (★) solution of p has min(u, B, C) > S.  This script finds the least k >= 1 for S = 1..SMAX and
prints p (then verify with z58_witness_scan: u_min > S and C_min > S).
Usage: uv run --with sympy python z58_witness_dickson.py SMAX KMAX"""
import sys
from math import lcm
from sympy import isprime
SMAX, KMAX = int(sys.argv[1]), int(sys.argv[2])
for S in range(1, SMAX + 1):
    L = 840
    for u in range(1, S + 1):
        L = lcm(L, 4 * u * (u + 1), 4 * u * (4 * u + 1))
    found = 0
    for k in range(1, KMAX + 1):
        p = 1 + L * k
        if not isprime(p):
            continue
        ok = all(isprime((p + u) // (u + 1)) for u in range(1, S + 1)) and \
             all(isprime((4 * C * p + 1) // (4 * C + 1)) for C in range(1, S + 1))
        if ok:
            print(S, L, k, p, flush=True); found += 1
            if found >= 3:
                break
    if not found:
        print(S, L, 'none with k <=', KMAX, flush=True)
