"""O40: rigorous refutation test of BDW(A) at N.
g = sum_{2<=d<=D} d*E_d(x mod d), E_d(b) = c(b,d) - N/d.  E g = 0 over Z/L0, so
E[g^+] = E|g|/2 <= sqrt(E g^2)/2, hence any BDW constant A >= window_avg(g) / (sqrt(E g^2)/2).
E g^2 = sum_{d,d'} d d' E[E_d E_d'] computed exactly (each term over Z/lcm(d,d')) in exact rationals
via integer arithmetic (scaled by d*d').
usage: spw_bdw_l2bound.py N [N ...]
"""
import sys
from math import gcd, isqrt
from fractions import Fraction
import numpy as np

def cnt_arr(d, N):
    b = np.arange(d)
    first = np.where(b >= 1, b, d)
    return np.where(first > N, 0, (N - first) // d + 1)

def run(N):
    D = N // 2
    # d*E_d(b) = d*c(b,d) - N  : integer arrays
    I = {d: d * cnt_arr(d, N).astype(np.int64) - N for d in range(2, D + 1)}
    # g = sum_d d*E_d = sum_d I_d ; E g^2 = sum_{d,d'} E[I_d I_d']
    tot = Fraction(0)
    for d in range(2, D + 1):
        for e in range(d, D + 1):
            l = d * e // gcd(d, e)
            x = np.arange(l)
            s = int(np.dot(I[d][x % d], I[e][x % e]))
            tot += Fraction(s * (1 if d == e else 2), l)
    win = Fraction(sum(int(I[d][n % d]) for d in range(2, D + 1) for n in range(1, N + 1)), N)
    eg2 = tot
    # ratio lower bound = win / (sqrt(eg2)/2) = 2 win / sqrt(eg2)
    # rigorous: A >= 2 win / sqrt(eg2); round DOWN: largest k/10^4 with (k/10^4)^2 * eg2 <= 4 win^2
    k = isqrt(int((4 * win * win / eg2) * 10**8))
    while Fraction(k + 1, 10**4) ** 2 * eg2 <= 4 * win * win: k += 1
    while Fraction(k, 10**4) ** 2 * eg2 > 4 * win * win: k -= 1
    r = k / 10**4
    Astar = max(Fraction(int(c) * d, N) for d in range(1, D + 1) for c in cnt_arr(d, N))
    print(f"N={N}: window avg g = {float(win):.4f}, E g^2 = {float(eg2):.3f}, "
          f"rigorous lower bound for BDW constant: A >= {r:.4f}   (A* = {float(Astar):.4f})", flush=True)

if __name__ == "__main__":
    for N in map(int, sys.argv[1:]):
        run(N)
