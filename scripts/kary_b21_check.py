"""Check of (2.1) for the explicit node sets used in EXCEPTIONAL_KARY §3:
log max_y |l_y(n)|/psi(y) <= d log(4e^3(n+1)/t) + 0.5 log(16nt+16), psi = Bin(n,t).
Exact log-space arithmetic; also the LP optimum B* for small n as a cross-check (B* <= B)."""
import math
from kary_check import bstar


def logpsi(n, t, y):
    return (math.lgamma(n + 1) - math.lgamma(y + 1) - math.lgamma(n - y + 1)
            + y * math.log(t) + (n - y) * math.log1p(-t))


def nodes(n, t, d):
    if n <= d:
        return list(range(n + 1))
    m0 = n * t
    if m0 <= 2 * d:
        return list(range(d + 1))
    h = int(math.floor(math.sqrt(m0 / d)))
    a = math.ceil(m0) - (d * h) // 2
    return [a + i * h for i in range(d + 1)]


def logB(n, t, d):
    Y = nodes(n, t, d)
    assert all(0 <= y <= n for y in Y) and len(set(Y)) == len(Y)
    if n in Y:                       # case (i): l_y(n) = [y == n]
        return -logpsi(n, t, n)
    best = -1e300
    for i, yi in enumerate(Y):
        num = sum(math.log(abs(n - yj)) for j, yj in enumerate(Y) if j != i)
        den = sum(math.log(abs(yi - yj)) for j, yj in enumerate(Y) if j != i)
        best = max(best, num - den - logpsi(n, t, yi))
    return best


worst = -1e9
worst31 = -1e9
cnt = 0
for n in list(range(1, 60)) + [80, 120, 200, 500, 1000, 5000, 10**5]:
    for t in [0.25, 0.2, 0.1, 0.05, 0.03, 0.01, 0.003, 1e-3, 1e-4]:
        for d in range(1, 13):
            lb = logB(n, t, d)
            rhs = d * math.log(4 * math.e ** 3 * (n + 1) / t) + 0.5 * math.log(16 * n * t + 16)
            worst = max(worst, lb - rhs); cnt += 1
            C1 = 2 * math.e ** 4.31
            uni = d * math.log(C1 * max(1 / t, math.sqrt(n / (t * d)))) + 0.5 * math.log(22 * n * t + 22) + 3
            worst31 = max(worst31, lb - uni)
            if n <= 20 and d <= 3 and t >= 0.01:
                assert math.log(bstar(n, t, d)) <= lb + 1e-6, (n, t, d)
print(f"max [log B - (3.1)] = {worst31:.3f} (must be <= 0)")
print(f"{cnt} cases; max [log B(explicit nodes) - (2.1)] = {worst:.3f} (must be <= 0); B* <= B on small n: ok")
