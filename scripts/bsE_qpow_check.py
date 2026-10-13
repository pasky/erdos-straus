"""bsE_qpow_check.py (O178): independent brute-force check of bsE_qpow.c on small n.
Recomputes F_I, F_II (q-power moduli, s >= 0) by naive divisor loops, and for every counted (t,a,b) /
(e,a,b) rebuilds the ES solution and checks 4/n = 1/x+1/y+1/z exactly (Fractions).
usage: PYTHONPATH=scripts uv run python scripts/bsE_qpow_check.py q NMAX   -> prints the both-empty primes."""
import sys
from fractions import Fraction as Fr
from sympy import isprime, divisors

def counts(n, q, verify=True):
    FI = FII = 0
    t = 1
    while t <= n + 2:
        if (t * n + 1) % 4 == 0:
            M = (t * n + 1) // 4
            for a in divisors(M):
                for b in divisors(M // a):
                    if (a + b) % t == 0:
                        FI += 1
                        if verify:
                            d = M // (a * b); c = (a + b) // t
                            assert Fr(4, n) == Fr(1, a*b*d*n) + Fr(1, a*c*d) + Fr(1, b*c*d)
        t *= q
    e = 1
    while e <= n:
        if (n + e) % 4 == 0:
            M = (n + e) // 4
            for a in divisors(M):
                for b in divisors(M // a):
                    if (a + b) % e == 0:
                        FII += 1
                        if verify:
                            d = M // (a * b); c = (a + b) // e
                            assert Fr(4, n) == Fr(1, a*b*d) + Fr(1, a*c*d*n) + Fr(1, b*c*d*n)
        e *= q
    return FI, FII

if __name__ == "__main__":
    q, N = int(sys.argv[1]), int(sys.argv[2])
    bad = [n for n in range(5, N + 1) if isprime(n) and counts(n, q) == (0, 0)]
    print("q=%d N=%d both-empty primes (%d):" % (q, N, len(bad)), bad)
