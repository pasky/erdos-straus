"""Aggregate z9_tes_words over split primes N(pi) <= bound: P(v_lambda(T) >= k | chi3) and per-prime target counts."""
import sys
from collections import Counter
from sympy import isprime
from tf_core import prime_above, mul, two_primary, UNITS
from z9_tes_words import analyse

bound = int(sys.argv[1])
FAIL = {7, 13, 19, 61, 79, 97, 103, 151, 193, 211, 367, 409, 769}
agg = Counter()
for N in range(7, bound + 1):
    if not isprime(N) or N % 3 != 1:
        continue
    P = prime_above(N)
    pi = next(mul(u, P) for u in UNITS if two_primary(mul(u, P)))
    n, h, s, tgt = analyse(pi)
    for ch, vl, so in tgt:
        for k in range(0, 5):
            if vl >= k:
                agg[(ch, k)] += 1
    t4 = sum(1 for ch, vl, so in tgt if ch == 2 and vl >= 4)
    print(N, "F" if N in FAIL else ".", "words", n, "target", h[2], "target&lam4", t4, "sols", dict(s), flush=True)
for ch in range(3):
    print("chi3", ch, [round(agg[(ch, k)] / agg[(ch, 0)], 4) for k in range(5)])
