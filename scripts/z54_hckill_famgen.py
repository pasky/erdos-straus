# z54 HCKILL: generate the primes p = 80 s^2 + 1 <= N (Theorem Q family p = 5m^2+1, 4 | m), one per line.
# Usage: uv run --with sympy python z54_hckill_famgen.py 1000000000000 > data/z54/hckill/fam_5m2p1_primes_1e12.txt
import sys
from sympy import isprime
N = int(sys.argv[1]); s = 1
while 80*s*s + 1 <= N:
    if isprime(80*s*s + 1): print(80*s*s + 1)
    s += 1
