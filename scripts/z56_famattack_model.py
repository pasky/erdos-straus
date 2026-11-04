# Poisson-model expected tail count of zero primes: T(x) = ∫_x^∞ exp(-c log^2 t) / (2 log t) dt  (primes ≡ 1 mod 4 density 1/(2 log t)).
# Substituting t = e^L: T = ∫_{L0}^∞ exp(L - c L^2) / (2L) dL. Report L0 (and log10 x) where T = 1, and the total expected zeros.
import sys
from mpmath import mp, quad, exp, inf, findroot, log
mp.dps = 30
def T(c, L0):
    f = lambda L: exp(L - c * L * L) / (2 * L)
    s = 1 / (2 * c)
    return quad(f, [L0, s, inf]) if L0 < s else quad(f, [L0, inf])
for c in map(float, sys.argv[1:]):
    tot = T(c, log(5))  # zero primes counted from t = 5
    lo, hi = 1 / (2 * c), 10 / c
    for _ in range(80):
        mid = (lo + hi) / 2
        lo, hi = (mid, hi) if T(c, mid) > 1 else (lo, mid)
    L0 = mp.mpf(lo)
    print(f"c = {c:.5f}: total expected zero primes ≈ {mp.nstr(tot, 4)}; tail count = 1 at p ≈ 10^{mp.nstr(L0 / log(10), 4)}")
