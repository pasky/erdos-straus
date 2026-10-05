"""R38b: high-precision recheck (mpmath) of review_o10b_sharp.py where float cancellation bites."""
import math, mpmath as mp
mp.mp.dps = 60
def tail(k, p, m, t):
    p = mp.mpf(p); pi = p ** k
    B = [(1 - pi) ** 2] + [pi ** 2 * math.comb(k, d) * ((1 - p) / p) ** d for d in range(1, k + 1)]
    def mul(a, b):
        c = [mp.mpf(0)] * min(len(a) + len(b) - 1, t + 1)
        for i, x in enumerate(a):
            for j, y in enumerate(b):
                if i + j <= t: c[i + j] += x * y
        return c
    res, base, e = [mp.mpf(1)], B[: t + 1], m
    while e:
        if e & 1: res = mul(res, base)
        base = mul(base, base); e >>= 1
    return (1 - pi) ** m - sum(res)
for (k, p, j) in [(3, 1e-3, 30), (3, 1e-3, 20), (1, 1e-3, 30)]:
    t = j * k - 1; pi = p ** k
    best = max(tail(k, p, int(S * j / pi), t) * mp.mpf(2) ** ((t + 1) / k) for S in [0.4, 0.45, 0.5, 0.55, 0.6])
    print(f"k={k} p={p} j={j}: max ratio {float(best):.4f}, x sqrt(2 pi j) = {float(best)*math.sqrt(2*math.pi*j):.3f}", flush=True)
