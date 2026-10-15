# z19_gap_mu0.py — limit-level test of Theorem W (EXP_OPEN.md §1): constant-gap ES families at the unit-square point
# mu = 0 of n_s = c0*2^s + k (c0 odd, k = 1 mod 8, c0 + k = 4^J).  A family with 4x - n = m constant and y, z polynomial in
# Y = 2^{s/D} near mu = 0 forces: N(1) = 4^{J-1}(4^J+m) = rho1 rho2 rho3 with rho_i = 2^{e_i} a_i (a_i odd > 0,
# a1 a2 a3 = M = 4^J + m), e_i in [-2, 2J], e1+e2+e3 = 2J-2, and m | rho1 + rho2 in Z[1/2].
# This script enumerates ALL such limit-level relations for m <= MMAX (no Jacobi pruning, brute force).
# Usage: PYTHONPATH=scripts uv run python scripts/z19_gap_mu0.py c0 k MMAX
import sys
from sympy import divisors
c0, k, MMAX = map(int, sys.argv[1:4])
J = (c0 + k).bit_length() // 2
assert 4 ** J == c0 + k and k % 8 == 1 and c0 % 2 == 1
hits = []
for m in range(3, MMAX + 1, 4):          # m = 3 mod 4 forced (n = 1 mod 4)
    M = 4 ** J + m
    ds = divisors(M)
    for a1 in ds:
        for a2 in ds:
            if (M // a1) % a2: continue
            for e1 in range(-2, 2 * J + 1):
                for e2 in range(-2, 2 * J + 1):
                    e3 = 2 * J - 2 - e1 - e2
                    if not -2 <= e3 <= 2 * J: continue
                    lo = min(e1, e2)
                    if (a1 * 2 ** (e1 - lo) + a2 * 2 ** (e2 - lo)) % m == 0:
                        hits.append((m, a1, e1, a2, e2, M // (a1 * a2), e3))
print('c0=%d k=%d J=%d m<=%d: %d limit-level relations' % (c0, k, J, MMAX, len(hits)))
for h in hits[:40]: print('  m=%d  rho1=2^%d*%d  rho2=2^%d*%d  rho3=2^%d*%d' % (h[0], h[2], h[1], h[4], h[3], h[6], h[5]))
