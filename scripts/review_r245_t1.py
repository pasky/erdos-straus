"""R245: (1) 4^s+105 is a square only for s in {2,3,4} (factor pairs of 105); (2) 256u^3+105 non-square for u = 32+151t, t < T."""
import sys
from math import isqrt
sq = [s for s in range(0, 400) if isqrt(4**s + 105)**2 == 4**s + 105]
pairs = [(a, 105 // a) for a in range(1, 11) if 105 % a == 0]
print('squares 4^s+105, s<400:', sq, ' factor-pair differences:', [(b - a) for a, b in pairs])
T = int(sys.argv[1]) if len(sys.argv) > 1 else 10**6
bad = [t for t in range(T) if isqrt(N := 256 * (32 + 151 * t)**3 + 105)**2 == N]
print(f'256u^3+105 squares with u=32+151t, t<{T}:', bad)
# gcd(K, n) = 1 and 151 does not divide d = 2(u^2-u+1) on the class (hypotheses of CAP_DOWN T1)
assert (2 * (32*32 - 32 + 1)) % 151 != 0
