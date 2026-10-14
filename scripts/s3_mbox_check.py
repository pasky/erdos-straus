"""O208 triple-check of Thm 1.1(a): M^box(n) via the Dirichlet shot, for M in {4,8,12,16,20,24}, all primes p <= PMAX
coprime to M and all odd non-squares n <= NMAX coprime to M; exact rational verification. Squares: Thm 1.1(b) control
in s3_numerator_blind.py. Usage: s3_mbox_check.py PMAX NMAX"""
import sys
from math import isqrt
from sympy import primerange
sys.argv, args = sys.argv[:1] + ['1'], sys.argv[1:]
from s3_numerator_blind import dirichlet_cert   # noqa: E402  (dirichlet_cert verifies the identity and den(z))
PMAX = int(args[0]) if args else 10**6
NMAX = int(args[1]) if len(args) > 1 else 10**5
from math import gcd                              # noqa: E402
for M in (4, 8, 12, 16, 20, 24):
    gmax = 0
    cnt = 0
    for p in primerange(3, PMAX):
        if M % p == 0:
            continue
        g = dirichlet_cert(M, p)[0]
        gmax = max(gmax, g)
        cnt += 1
    cntc = 0
    for n in range(3, NMAX, 2):
        if gcd(n, M) > 1 or isqrt(n) ** 2 == n:
            continue
        dirichlet_cert(M, n)
        cntc += 1
    print('M=%d: %d primes <= %d and %d odd non-squares <= %d certified; max g over primes %d' % (
        M, cnt, PMAX, cntc, NMAX, gmax))
