"""pd_band2.py — the k-direction wall for ES^[2] (PHASE_DIAGRAM.md §2): for odd n <= NMAX, odd B <= BMAX with
B > (n+1)/2, and k <= 2 B^2, list divisors g ≡ -1 (mod 4kB) of 4k^2 n + B^2; assert k < B^2/2; report max k/B^2.
Usage: pd_band2.py NMAX BMAX"""
import sys
from math import gcd
from sympy import divisors
NMAX, BMAX = map(int, sys.argv[1:3])
best = (0, None); cnt = 0
for n in range(3, NMAX + 1, 2):
    for B in range(1, BMAX + 1, 2):
        if 2 * B <= n + 1 or gcd(B, n) != 1:
            continue
        for k in range(1, 2 * B * B + 1):
            if gcd(B, k) != 1:
                continue
            for g in divisors(4 * k * k * n + B * B):
                if (g + 1) % (4 * k * B) == 0:
                    cnt += 1
                    assert 2 * k < B * B, (n, k, B, g)
                    if k / B**2 > best[0]:
                        best = (k / B**2, (n, k, B, g))
print("shots", cnt, "max k/B^2", best)
