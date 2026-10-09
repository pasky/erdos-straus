"""O102 validation: brute-force m-representability of primes via the smallest denominator s in
(p/m, 3p/m] and the two-unit-fraction criterion A/B = 1/y+1/z  <=>  exist u, v | B with A | u+v
(gcd(A,B)=1). Compares with emn2_scan (PW Cor 2.2/2.4 sieve). Usage: emn2_brute.py MMAX PMAX"""
import sys, subprocess, os
SCAN = os.environ.get('EMN2_SCAN', '/tmp/emn2_scan')
from math import gcd
from sympy import primerange, divisors
def rep(m, p):
    for s in range(p // m + 1, 3 * p // m + 1):
        A, B = m * s - p, p * s
        if A <= 0: continue
        g = gcd(A, B); A //= g; B //= g
        ds = divisors(B)
        S = set(d % A for d in ds)
        if any(((-u) % A) in S for u in ds): return True
    return False
MMAX, PMAX = int(sys.argv[1]), int(sys.argv[2])
bad = 0; tot = 0
for m in range(4, MMAX + 1):
    exc = [p for p in primerange(2, PMAX) if m % p and not rep(m, p)]
    out = subprocess.run([SCAN, str(m), '1', str(PMAX - 1), '2'], capture_output=True, text=True).stdout.split('\n')
    scan_exc = [int(l.split()[1]) for l in out if l.startswith('E ')]
    if scan_exc != exc: bad += 1; print('MISMATCH', m, sorted(set(scan_exc) ^ set(exc))[:10])
    tot += len(exc)
print('m<=%d p<%d: per-prime mismatches in %d values of m; %d exceptional (m,p) pairs checked' % (MMAX, PMAX, bad, tot))
sys.exit(1 if bad else 0)
