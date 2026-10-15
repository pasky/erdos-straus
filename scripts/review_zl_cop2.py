"""review_zl_cop2.py -- R231, FROM SCRATCH: Lemma 1.1 (l2-Minkowski form of (Cop)).
(1) mu_w = 2 sqrt(w) Gamma(w/2+1)^{1/w}/sqrt(pi): values, mu_w < w for w >= 2.
(2) random tests: whenever (Cop2) holds (checked with 60-digit mpmath and a 1e-30 relative margin), the number of divisors E of n
    with D0 <= E <= D1, E == sigma (mod s) is <= w-1.  Counts tight cases."""
import random, math
from mpmath import mp, mpf, gamma, sqrt, pi, log
mp.dps = 60
random.seed(2311)
mu = lambda w: 2 * sqrt(w) * gamma(mpf(w) / 2 + 1) ** (mpf(1) / w) / sqrt(pi)
print("mu_w:", {w: float(mu(w)) for w in (1, 2, 3, 10, 24, 40, 63)})
assert all(mu(w) < w for w in range(2, 200)) and abs(mu(1) - 1) < 1e-50
print("mu_w/w at w=63:", float(mu(63) / 63), " limit sqrt(2/(e pi)) =", float(sqrt(2 / (math.e * pi))))
def divisors(n):
    ds = [1]; m = n; p = 2
    while p * p <= m:
        k = 0
        while m % p == 0: m //= p; k += 1
        if k: ds = [d * p ** i for d in ds for i in range(k + 1)]
        p += 1
    if m > 1: ds = ds + [d * m for d in ds]
    return ds
smooth = [2, 3, 5, 7, 11, 13, 17, 19, 23]
tests = tight = holds = 0
for it in range(4000):
    n = 1
    while n < 10 ** 6: n *= random.choice(smooth)
    if n > 10 ** 13: continue
    ds = divisors(n)
    s = random.randint(1, 3000); E0 = random.choice(ds)
    if math.gcd(E0, s) != 1: continue
    sigma = E0 % s
    D0 = max(1, E0 - random.randint(0, 5 * s)); D1 = D0 + random.randint(0, 40 * s)
    X = mpf(D1 - D0) / (2 * s) + mpf(1) / 2
    cnt = sum(1 for E in ds if D0 <= E <= D1 and E % s == sigma)
    for w in range(1, 25):
        for m in range(1, w + 1):
            lhs = w * log(mu(w)) + mpf(m * (m + 1)) / 2 * log(n) + mpf(w * (w - 1)) / 2 * log(X)
            rhs = m * w * log(D0)
            if lhs < rhs * (1 - mpf(10) ** -30) - mpf(10) ** -30:
                holds += 1
                assert cnt <= w - 1, (n, s, sigma, D0, D1, w, m, cnt)
                tight += (cnt == w - 1)
    tests += 1
print(f"{tests} random (n, s, sigma, window) instances; (Cop2) held in {holds} (w,m) cases; 0 violations; tight {tight}")
