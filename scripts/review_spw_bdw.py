"""R40 from-scratch check of Prop 2.3 (BDW constant A(N) >= c sqrt N).
g = sum_{2<=d<=D} d E_d(x mod d), E_d(b) = c(b,d) - N/d.
(i) brute-force on Z/L0 for small N: E g = 0, E[dE_d d'E_d'] = r_g0 (g0 - r_g0),
    sum_{n<=N} d E_d(n) = r_d (d - r_d);   also the exact E g^+ and the true ratio.
(ii) exact lower bound A(N) >= W / (sqrt(Eg2)/2),  W = (1/N) sum_d r_d(d-r_d)."""
import sys
from fractions import Fraction as Fr
from math import gcd, lcm, isqrt
from functools import reduce

def c(b, d, N):
    return sum(1 for n in range(1, N + 1) if n % d == b % d)

def brute(N):
    D = N // 2
    L0 = reduce(lcm, range(1, D + 1), 1)
    E = {d: [Fr(c(b, d, N)) - Fr(N, d) for b in range(d)] for d in range(2, D + 1)}
    for d in E:
        r = N % d
        assert sum(d * E[d][n % d] for n in range(1, N + 1)) == r * (d - r)
        for d2 in E:
            g0 = gcd(d, d2); r0 = N % g0
            # E over Z/L0 of product depends only on x mod lcm(d,d2)
            m = lcm(d, d2)
            val = Fr(sum(d * E[d][x % d] * d2 * E[d2][x % d2] for x in range(m)), m)
            assert val == r0 * (g0 - r0), (d, d2)
    g = [sum(d * E[d][x % d] for d in E) for x in range(L0)]
    assert sum(g) == 0
    Wside = Fr(sum(g[n % L0] for n in range(1, N + 1)), N)
    Egp = Fr(sum(v for v in g if v > 0), L0)
    return L0, Wside, Egp

for N in [12, 14, 16, 18]:
    L0, W, Egp = brute(N)
    print(f"brute N={N} L0={L0}: (1/N)sum_W g = {float(W):.4f}, E g+ = {float(Egp):.4f}, ratio = {float(W/Egp):.4f}")

def lower(N):
    D = N // 2
    W = Fr(sum((N % d) * (d - N % d) for d in range(2, D + 1)), N)
    Eg2 = 0
    for d in range(2, D + 1):
        for d2 in range(2, D + 1):
            g0 = gcd(d, d2); r0 = N % g0
            Eg2 += r0 * (g0 - r0)
    # A >= W / (sqrt(Eg2)/2) = 2W/sqrt(Eg2); return exact-floor decimal with 4 digits
    # largest k with k/10^4 <= 2W/sqrt(Eg2)  <=>  (k/10^4)^2 Eg2 <= 4 W^2
    lo, hi = 0, 10**7
    while lo < hi:
        k = (lo + hi + 1) // 2
        if Fr(k, 10**4) ** 2 * Eg2 <= 4 * W * W:
            lo = k
        else:
            hi = k - 1
    return Fr(lo, 10**4), D

for N in [int(a) for a in sys.argv[1:]] or [150, 200, 300, 400]:
    a, D = lower(N)
    print(f"N={N}: A(N) >= {float(a):.4f} (rounded down);  A*(N) = {float(Fr(3,2)-Fr(3,N)):.4f};  A/sqrt(N) >= {float(a)/N**0.5:.4f}")
