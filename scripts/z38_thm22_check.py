"""z38_thm22_check.py: the sub-family lower bound of Thm 2.2 (u odd <= p^delta, B = 2B', B' <= p/(8u), gcd(B',u)=1, weight 1/(4uB))
against the proved asymptotic constants and the exact M_BM; numbers only (sanity of the positivity argument)."""
import sys, math
from math import gcd
def leg_table(p):
    t = [0] * p
    for x in range(1, p): t[x * x % p] = 1
    return [1 if t[k] else -1 for k in range(p)]
for p in map(int, sys.argv[1:]):
    leg = leg_table(p); L = math.log(p)
    for delta in (0.25, 0.5):
        X = int(p ** delta); S = 0.0
        for u in range(1, X + 1, 2):
            Y = p // (8 * u); e = leg[(-2 * u) % p]
            for Bp in range(1, Y + 1):
                if gcd(Bp, u) == 1:
                    S += (1 - e * leg[Bp % p]) / (8 * u * Bp)
        S *= 2
        print(f"p={p} delta={delta}: subfamily {S:.3f} = {S/L**2:.4f} L^2  (proved asymptotic: {1/(32*math.pi**2) if delta==0.25 else 3/(16*math.pi**2):.4f} L^2)")
