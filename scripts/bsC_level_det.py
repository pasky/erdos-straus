"""O176 DIFF_DEEP §2: Type II as a 'level vs determinant' condition on a pair of special endomorphisms.
Claim (Thm 2.1): for a prime p, the Type II tuples (a,b,c,d) (a <= b) of p are in bijection with triples (f, f', c),
f <= f', with  f f' = 1 (mod p),  h := (f f' - 1)/p,  G := gcd(f+1, f'+1),  4c^2 | h  and  h | cG
(then d = h/(4c^2), M = 4cd | G, a = (f+1)/M, b = (f'+1)/M).  Equivalently some c exists iff 4h | gcd(h,G)^2.
Brute-force check for primes p <= X: enumerate all (f, f') with f f' <= B_p (B_p = max f f' over the tuples of p,
times 1) and compare counts with the tuple enumerator.  Also T1 control at odd squares n (same arithmetic with p -> n).
Run: PYTHONPATH=scripts uv run python scripts/bsC_level_det.py X
"""
import sys
from math import gcd, isqrt
from sympy import isprime, divisors
from bsC_common import typeII_all

X = int(sys.argv[1]) if len(sys.argv) > 1 else 400


def count_pairs(n, B):
    tot = 0
    for f in range(1, isqrt(B) + 1):
        if gcd(f, n) != 1:
            continue
        r = pow(f, -1, n)
        fp = r
        while fp < f:
            fp += n
        while f * fp <= B:
            h = (f * fp - 1) // n
            if h > 0:
                G = gcd(f + 1, fp + 1)
                for c in divisors(h):
                    if h % (4 * c * c) == 0 and (c * G) % h == 0:
                        tot += 1
            fp += n
    return tot


II = typeII_all(X)
bad = checked = 0
for n in range(5, X + 1, 2):
    L = II.get(n, [])
    if not (isprime(n) or (isqrt(n) ** 2 == n)):
        continue
    B = max([(4 * a * c * d - 1) * (4 * b * c * d - 1) for a, b, c, d, e in L], default=50 * n * n)
    cnt = count_pairs(n, B)
    checked += 1
    if cnt != len(L):
        bad += 1
        print('mismatch', n, cnt, len(L))
print('n checked (primes and odd squares <=', X, '):', checked, ' mismatches:', bad)
