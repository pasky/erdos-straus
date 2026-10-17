"""O259: check B1_LINE.md Prop 4.1 on primes p = 1 (mod M_sigma), sigma = 7 (M = 176400) and sigma = 11 (M = 64033200).
For each shift 3 <= s <= sigma: pairs (Lemma 1.1: t > s, t | p+s, s | (p+s)/t + 1, 4 | st) == divisors t > s of p+s with
t = -1 (mod s) and 4 | st; and Q_s prime => no pair.
usage: PYTHONPATH=scripts uv run python scripts/z29_freeze_check.py 20000000
"""
import sys
from math import log
from sympy import isprime, divisors, primerange

def M_of(sig):
    M = 1
    for l in primerange(2, sig + 2):
        M *= l ** (int(log(sig + 1, l) + 1e-9) + 1)
    return M

X = int(sys.argv[1])
for sig in (7, 11):
    M = M_of(sig)
    nprimes = bad = qprime = qprime_bad = pairs = 0
    for p in range(1 + M, X, M):
        if not isprime(p):
            continue
        nprimes += 1
        for s in range(3, sig + 1):
            n = p + s
            assert n % (1 + s) == 0 and (n // (1 + s)) % s == 1
            A = {t for t in divisors(n) if t > s and ((n // t) + 1) % s == 0 and (s * t) % 4 == 0}
            B = {t for t in divisors(n) if t > s and (t + 1) % s == 0 and (s * t) % 4 == 0}
            pairs += len(A)
            if A != B: bad += 1
            if isprime(n // (1 + s)):
                qprime += 1
                if A: qprime_bad += 1
    print(f"sigma={sig} M={M}: primes p=1 (M) < {X}: {nprimes}; shift-s pairs {pairs}; mismatches {bad}; "
          f"(s, p) with Q_s prime: {qprime}, of which with a pair: {qprime_bad}")
