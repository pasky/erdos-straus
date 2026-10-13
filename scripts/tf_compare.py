"""O194: cross-check method A (tf_exact, divisor enumeration) against method B (tf_brute, lattice brute force):
identical solution SETS for every 2-primary split prime pi with N(pi) <= NMAX (one per conjugate pair) and
inert p with p^2 <= NMAX.  usage: tf_compare.py NMAX"""
import sys
from sympy import isprime
import tf_core as C, tf_exact as A, tf_brute as Bm
NMAX = int(sys.argv[1]); nprimes = nsol = 0; zero = []
for p in range(5, NMAX + 1):
    if not isprime(p):
        continue
    if p % 3 == 1:
        pi = A.two_primary_assoc(C.prime_above(p))
    elif p * p <= NMAX:
        pi = (p, 0)
    else:
        continue
    sa, sb = A.solve(pi), Bm.solve(pi)
    assert sa == sb, (p, pi, len(sa), len(sb), sa ^ sb)
    nprimes += 1; nsol += len(sa)
    if not sa:
        zero.append(C.norm(pi))
print(f"N <= {NMAX}: {nprimes} primes, {nsol} solutions, methods A and B agree on every solution set; zero at N = {zero}")
