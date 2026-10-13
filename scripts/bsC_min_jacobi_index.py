"""O176 memo bsC_fourier_jacobi: least Jacobi index min(f, f') over Type II certificates of p (f f' = 1 + 4c^2 d p,
f = f' = -1 mod 4cd).  A fixed finite set of indices F is a congruence covering (B1).  Reports growth of
F*(p) := least such f, over primes p = 1 (mod 24) up to X.
Run: PYTHONPATH=scripts uv run python scripts/bsC_min_jacobi_index.py X
"""
import sys
from sympy import primerange, divisors


def fmin(p, cap=10**6):
    for f in range(3, cap, 4):              # f = -1 mod 4
        for M in divisors(f + 1):
            if M % 4:
                continue
            cd = M // 4
            for c in divisors(cd):
                d = cd // c
                N = 1 + 4 * c * c * d * p
                if N % f == 0 and (N // f + 1) % M == 0 and N // f >= f:
                    return f
    return None


X = int(sys.argv[1]) if len(sys.argv) > 1 else 10**5
best, rec = 0, []
for p in primerange(5, X):
    if p % 24 != 1:
        continue
    f = fmin(p)
    if f > best:
        best = f
        rec.append((p, f))
print('records (p, least f):', rec)
