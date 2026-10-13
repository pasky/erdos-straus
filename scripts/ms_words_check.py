"""O197 independent check of Thm 3.1 on actual words (not cells): for all odd n in [3, N] and all words
(t,u,v) >= 1 with tuv-u-v = n, gcd(A,n) = 1 (A = tu-1 >= 1): compare slice membership S_m with chi = (-A/n) (sympy).
Also verifies each S_m word's explicit solution in exact rationals (Fractions).  usage: ms_words_check.py N"""
import sys
from fractions import Fraction as Fr
from math import gcd
from sympy import jacobi_symbol

N = int(sys.argv[1])
stats = {m: {(1, True): 0, (1, False): 0, (-1, True): 0, (-1, False): 0} for m in (4, 5, 8, 12)}
for n in range(3, N + 1, 2):
    for t in range(1, n + 3):
        for u in range(1, n + 2):
            A = t * u - 1
            if A < 1: continue
            if A > n + u: break
            if (n + u) % A: continue
            v = (n + u) // A
            if gcd(A, n) != 1: continue
            chi = jacobi_symbol((-A) % n, n)
            As = t * v - 1
            for m in stats:
                sols = []
                if A % m == 0: d = A // m; sols.append((As * d * n, v * d, As * v * d))
                if As % m == 0: d = As // m; sols.append((A * d * n, u * d, A * u * d))
                if t % m == 0: c = t // m; sols.append((u * v * c, u * c * n, v * c * n))
                if u % m == 0: w = u // m; sols.append((w * As, t * n * w, t * n * w * As))
                if v % m == 0: w = v // m; sols.append((w * A, t * n * w, t * n * w * A))
                for s in sols:
                    assert all(s) and sum(Fr(1, q) for q in s) == Fr(m, n), (m, n, t, u, v, s)
                stats[m][(chi, bool(sols))] += 1
for m, s in stats.items():
    print(f"m={m:2d}: chi=-1 words in S_m {s[(-1, True)]}, not {s[(-1, False)]}; chi=+1 words in S_m {s[(1, True)]}, not {s[(1, False)]}")
