"""y2_even_edge_random: random large-N test of FRIEZE_ES Thm 1.2 + square control.
(a) T random words, letters log-uniform up to 10^4 (N up to ~10^12), N odd;
(b) square control: for odd M <= MMAX, all words at N = M^2 with m <= 60 via divisors of mN+1 (sympy).
usage: y2_even_edge_random.py T MMAX SEED"""
import sys, random
from math import isqrt
from sympy import divisors
from y2_even_edge import jacobi
T, MMAX, seed = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]); random.seed(seed)
fails = 0; done = 0
def check(c, m, s, N):
    q = (m * s - 1, c, m, s, c * m - 1)
    ev = [i for i in range(5) if q[i] % 2 == 0]
    if len(ev) != 2 or (ev[1] - ev[0]) % 5 not in (1, 4): return False
    ee = q[ev[0]] * q[ev[1]]
    return jacobi(q[0], N) == jacobi(N - 1, N) * (-1 if ee % 8 == 0 else 1)
while done < T:
    c, m, s = (int(10 ** random.uniform(0, 4)) for _ in range(3))
    N = m * c * s - c - s
    if N <= 1 or N % 2 == 0: continue
    done += 1; fails += not check(c, m, s, N)
sqw = 0
for M in range(3, MMAX + 1, 2):
    N = M * M
    for m in range(1, 61):
        for h in divisors(m * N + 1):
            if (h + 1) % m == 0 and ((m * N + 1) // h + 1) % m == 0:
                c, s = (h + 1) // m, ((m * N + 1) // h + 1) // m
                sqw += 1; fails += not check(c, m, s, N)
                q = (m * s - 1, c, m, s, h)
                fails += any(x % 4 == 0 for x in q)
print("random words:", T, "square-control words:", sqw, "FAILURES:", fails); sys.exit(1 if fails else 0)
