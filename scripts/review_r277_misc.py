"""R277 from-scratch checks: Lemma 5.1 (log-simplex main term), Prop 6.1(b),(c), Lemma 5.2 small exceptions."""
import math, cmath
from math import gcd, log


def lemma51(p, a0, a1, b0, b1):
    L = log(p)
    tot = 0.0
    u = 1
    while 3 * u - 1 <= p:
        if p ** a0 <= u <= p ** a1:
            Bmax = min((p + u) // (4 * u - 1), int(p ** b1))
            Bmin = max(1, math.ceil(p ** b0))
            if Bmax >= Bmin:
                # sum_{B=Bmin}^{Bmax} 1/B via digamma-ish: harmonic differences
                H = lambda n: (math.log(n) + 0.5772156649015329 + 1 / (2 * n) - 1 / (12 * n * n)) if n > 0 else 0.0
                tot += (H(Bmax) - H(Bmin - 1)) / (4 * u)
        elif u > p ** a1:
            break
        u += 1
    # area of [a0,a1]x[b0,b1] cut by a+b<=1, numerically
    n = 2000
    area = 0.0
    for i in range(n):
        a = a0 + (a1 - a0) * (i + 0.5) / n
        hi = min(b1, 1 - a)
        if hi > b0:
            area += (hi - b0) * (a1 - a0) / n
    main = L * L / 4 * area
    return tot, main, (tot - main) / L


for p in (10 ** 6, 10 ** 7, 10 ** 8):
    for box in ((0, 1, 0, 1), (0.2, 0.4, 0.1, 0.5), (0.3, 0.35, 0.3, 0.35)):
        t, m, e = lemma51(p, *box)
        print(f"Lemma 5.1 p=1e{round(log(p, 10))} box={box}: sum={t:.3f} main={m:.3f} (sum-main)/log p={e:+.3f}")


def kloost(m, n, c):
    return sum(cmath.exp(2j * math.pi * (m * a + n * pow(a, -1, c)) / c) for a in range(c) if gcd(a, c) == 1)


for c in (4, 8, 12, 20, 24):
    v = sum(cmath.exp(2j * math.pi * (m + n) / c) * kloost(m, n, c) for m in range(c) for n in range(c)) / c ** 2
    print(f"Prop 6.1(b) c={c}: c^-2 sum e((m+n)/c) S(m,n;c) = {v.real:.6f}{v.imag:+.6f}i")

# 6.1(c): S g S^-1 for a sample matrix
def mm(X, Y):
    return ((X[0][0] * Y[0][0] + X[0][1] * Y[1][0], X[0][0] * Y[0][1] + X[0][1] * Y[1][1]),
            (X[1][0] * Y[0][0] + X[1][1] * Y[1][0], X[1][0] * Y[0][1] + X[1][1] * Y[1][1]))
S = ((0, -1), (1, 0)); Si = ((0, 1), (-1, 0))
g = ((7, 9), (10, 13))  # det 91-90 = 1
print("Prop 6.1(c) S g S^-1 =", mm(mm(S, g), Si), " expected (d, -c; -b, a) =", ((13, -10), (-9, 7)))

# Lemma 5.2 hypothesis G^2 = {1} for q = 4uB: which admissible pairs?
ex = []
for u in range(1, 40):
    for B in range(1, 40):
        if gcd(u, B) == 1 and (u + B) % 2:
            q = 4 * u * B
            if all(x * x % q == 1 for x in range(1, q) if gcd(x, q) == 1):
                ex.append((u, B, q))
print("admissible pairs with (Z/q)^x of exponent 2 (genus = full indicator):", ex)
