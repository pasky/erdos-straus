"""O141(c): W(p) (congruence-table search) vs Tf(p) (one factorisation per slice t) on primes that are
square-mimicking: p = 1 mod L_y, L_y = 8*prod_{3<=l<=y} l.  Reports mean/median/max over a sample.
Usage: bs_logic_mimic.py SAMPLE MMAX TMAX y1 y2 ...
"""
import sys, statistics, random
from sympy import isprime, divisors, primerange
SAMPLE, MMAX, TMAX = map(int, sys.argv[1:4]); YS = list(map(int, sys.argv[4:]))
R = {}
for M in range(3, MMAX + 1, 4):
    A = (M + 1) // 4
    R[M] = frozenset((-4 * D) % M for D in divisors(A * A))
def W(p):
    for M in range(3, MMAX + 1, 4):
        if p % M in R[M]:
            return M
    return MMAX + 1  # censored
def Tf(p):
    for t in range(1, TMAX + 1):
        N = t * p + 1
        for m in divisors(N):
            if m % 4 == 0 and (m + 1) % t == 0 and (N // m + 1) % t == 0:
                return t
    return TMAX + 1
random.seed(1)
for y in YS:
    L = 8
    for l in primerange(3, y + 1): L *= l
    ps = []; k = random.randrange(10, 1000)
    while len(ps) < SAMPLE:
        p = k * L + 1
        if isprime(p): ps.append(p)
        k += 1
    ws = [W(p) for p in ps]; ts = [Tf(p) for p in ps]
    print(f"y={y} L={L:.3g} p~{ps[0]:.3g}: W mean {statistics.mean(ws):.0f} med {statistics.median(ws)} max {max(ws)} | "
          f"Tf mean {statistics.mean(ts):.0f} med {statistics.median(ts)} max {max(ts)}", flush=True)
