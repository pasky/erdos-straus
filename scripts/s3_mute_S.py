"""O208: fixed mute set S = {3,5,7,11}: every failing (M, p) of the M/p census (M = 8..24, 4 | M) has an
M^{(S)} shot solution (Q in <S>, g | p + M Q^2, g = -1 mod M), verified exactly. Usage: ... s3_mute_S.py [QBOUND]"""
import sys
from fractions import Fraction
from math import gcd
from sympy import divisors
sys.path.insert(0, 'scripts')
from s3_numerator_blind import fails, shot_solution  # noqa: E402  (module prints its own report on import)
B = int(sys.argv[1]) if len(sys.argv) > 1 else 10**5
S = (3, 5, 7, 11)
units = [1]
for q in S:
    units = sorted({u * q**k for u in units for k in range(40) if u * q**k <= B})
miss, worst = [], 0
for M in (8, 12, 16, 20, 24):
    for p in fails(M):
        if M % p == 0 or p in S:
            continue
        found = None
        for Q in units:
            if Q == 1 or gcd(Q, p) > 1:
                continue
            for g in divisors(p + M * Q * Q):
                if g > 1 and (g + 1) % M == 0:
                    x, y, z = shot_solution(M, p, g, Q)
                    assert z.denominator % 2 == 1 and gcd(z.denominator, p) == 1
                    found = (Q, g)
                    break
            if found:
                break
        if found is None:
            miss.append((M, p))
        else:
            worst = max(worst, found[0])
print('M^(S), S={3,5,7,11}: misses', miss, '; largest least-Q used', worst)
