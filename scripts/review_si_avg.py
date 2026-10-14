"""R204: from-scratch check of Lemma 2.1 averages.  Counts words with K=tuv-u-v<=X odd by sign,
fits S(X) = a X log^2 X + b X log X + c X over several X, compares a with (15/32)/2, (5/32)/2.
Usage: uv run --with numpy python scripts/review_si_avg.py XMAX"""
import sys
import numpy as np
from math import log


def jac(a, n):
    a %= n; r = 1
    while a:
        while a % 2 == 0:
            a //= 2
            if n % 8 in (3, 5): r = -r
        a, n = n, a
        if a % 4 == 3 and n % 4 == 3: r = -r
        a %= n
    return r if n == 1 else 0


X = int(sys.argv[1])
cntm = np.zeros(X + 1, dtype=np.int64); cntp = np.zeros(X + 1, dtype=np.int64)
for u in range(1, X + 3):
    if u * 1 - u - 1 > X and u > 2:
        pass
    for v in range(1, X + 3):
        # smallest n for t=1 is uv-u-v; need some t with 0<n<=X
        if u * v - u - v > X:
            break
        t = 1
        while True:
            n = t * u * v - u - v
            if n > X:
                break
            if n > 0 and n % 2 == 1:
                if jac(-(t * u - 1), n) == -1:
                    cntm[n] += 1
                else:
                    cntp[n] += 1
            t += 1
Cm = np.cumsum(cntm); Cp = np.cumsum(cntp)
xs = np.array([X // 16, X // 8, X // 4, X // 2, X])
M = np.array([[x * log(x) ** 2, x * log(x), x] for x in xs], dtype=float)
for name, C, pred in (("N-", Cm, 15 / 64), ("N+", Cp, 5 / 64)):
    coef = np.linalg.lstsq(M, C[xs].astype(float), rcond=None)[0]
    print(name, "fit a,b,c =", coef, " predicted a =", pred,
          " raw ratio at X:", C[X] / (X * log(X) ** 2))
print("ratio N-/N+ at X:", Cm[X] / Cp[X])
