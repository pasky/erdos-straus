"""O259: prime samples for the heuristic model (B1_LINE.md §3).
usage: PYTHONPATH=scripts uv run python scripts/z29_samples.py X M COUNT  -> first COUNT primes p >= X with p = 1 (mod M)
(M = 24: the nontrivial class; M = 72, 1800, 176400, 64033200: p = 1 mod M_sigma, sigma = 3, 5, 7, 11).
"""
import sys
from sympy import isprime
X, M, C = int(float(sys.argv[1])), int(sys.argv[2]), int(sys.argv[3])
p = X - (X - 1) % M + M
out = 0
while out < C:
    if isprime(p):
        print(p); out += 1
    p += M
