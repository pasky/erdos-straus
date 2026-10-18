"""z39: holomorphic (odd, weight-1 Kronecker) part O of Thm K at near-square primes m^2 + K vs generic primes.
usage: python z39_nearsq.py M0 count K1 K2 ...  (prints mean O/2-sum and mean E/2-sum per family)"""
import sys, statistics
from sympy import divisors, isprime
M0, cnt = int(sys.argv[1]), int(sys.argv[2]); Ks = [int(x) for x in sys.argv[3:]]
def EO(n):
    E = O = 0
    for t in range(2, (n + 4) // 4 + 1):
        N = t * n + 1; dm = dp = 0
        for d in divisors(N):
            r = d % t
            if r == t - 1: dm += 1
            elif r == 1: dp += 1
        dp -= 2; E += (dm + dp) / 2; O += (dm - dp) / 2
    return E, O
for K in Ks:
    rows = []; m = M0
    while len(rows) < cnt:
        m += 1; n = m * m + K
        if isprime(n): rows.append(EO(n))
    print("K=%d mean E=%.1f mean O=%.1f sd O=%.1f" % (K, statistics.mean(r[0] for r in rows), statistics.mean(r[1] for r in rows), statistics.pstdev([r[1] for r in rows])))
