"""O169 §4.5-4.6: (a) direct check of Thm 4.5 on data: for n = 1 (4), A in L3(n):
    Jacobi (A/n) = -1  <=>  [4|tu-1 or 4|tv-1 or 4|t or 4|u or 4|v];
(b) lambda(p) = min HJ length r(p/A) over quadratic non-residues A, primes p = 1 (8) <= N.
Usage: PYTHONPATH=scripts uv run --with sympy python scripts/dk_qnr.py N
"""
import sys
from math import isqrt, gcd
from collections import Counter
from sympy import isprime, jacobi_symbol
from dk_dict import hj, certs_len3
N = int(sys.argv[1])
bad = 0
for n in range(5, min(N, 5000) + 1, 4):
    if isqrt(n) ** 2 == n:
        continue
    for A in certs_len3(n):
        As = pow(A, -1, n); t = (A * As - 1) // n; u = (A + 1) // t; v = (As + 1) // t
        es = (A % 4 == 0) or (As % 4 == 0) or t % 4 == 0 or u % 4 == 0 or v % 4 == 0
        if (jacobi_symbol(A, n) == -1) != es:
            bad += 1
print("Thm 4.5 direct check, non-square n=1(4) <= 5000: failures", bad)
lam = Counter(); worst = []
for p in range(17, N + 1, 8):
    if not isprime(p):
        continue
    best = 99
    # lengths 2,3 first (cheap), then brute force if needed
    if any(jacobi_symbol(b, p) == -1 for b in range(2, (p + 1) // 2 + 1) if (p + 1) % b == 0):
        best = 2
    elif any(jacobi_symbol(A, p) == -1 for A in certs_len3(p)):
        best = 3
    else:
        best = min(len(hj(p, A)) for A in range(2, p) if jacobi_symbol(A, p) == -1)
    lam[best] += 1
    if best > 3: worst.append(p)
print(f"lambda(p) distribution for primes p=1(8) <= {N}:", dict(lam), "lambda>3 at:", worst[:20])
