"""R190 reviewer-2: from-scratch check of UNIT_ORBIT_ES Thm 5.1 (V_phi, K = Q(sqrt5)).

(1) Local criterion: odd n is orbit-solved iff for some prime q of O (q not | 2) some a_k = n + 4 phi^{2k+1} is
    divisible by q with (n/q) = -1. For split l (l = +-1 mod 5) and each root f of t^2 - t - 1 mod l:
    S_q = {n mod l : -n/4 in f^{odd}, (n/l) = -1}; for q = (sqrt5): phi = 3 mod sqrt5. Sieve odd n <= X by all
    q with l <= L and compare the survivors with T = {m^2, 5m^2}.
(2) Mechanism quantities: for split l <= L2, fraction of 'good' q, and |S_q| vs ord_q(phi)/2 on good q.
Usage: PYTHONPATH=scripts uv run --with sympy --with numpy python scripts/review_uo2_phi.py X L L2
"""
import sys
from math import isqrt
import numpy as np
from sympy import primerange, sqrt_mod, n_order, legendre_symbol

X, L, L2 = (int(t) for t in sys.argv[1:4])


def S_q(l, f):
    inv4 = pow(4, -1, l)
    m = n_order(f, l)
    f2 = f * f % l
    C, c = set(), f
    for _ in range(m):
        C.add(c)
        c = c * f2 % l
    S = set()
    for c in C:
        nres = (-4 * c) % l
        if legendre_symbol(nres, l) == -1:
            S.add(nres)
    return S, C, m


solved = np.zeros(X + 1, dtype=bool)
ns = np.arange(X + 1)
# q = (sqrt5): residue field F_5, phi = 3
C5 = {pow(3, 2 * k + 1, 5) for k in range(2)}
S5 = {(-4 * c) % 5 for c in C5 if legendre_symbol((-4 * c) % 5, 5) == -1}
for s in S5:
    solved |= (ns % 5 == s)
for l in primerange(7, L + 1):
    if l % 5 not in (1, 4):
        continue
    for f in sqrt_mod(5, l, all_roots=True):
        f = (1 + f) * pow(2, -1, l) % l   # root of t^2 - t - 1
        S, _, _ = S_q(l, f)
        mask = np.zeros(l, dtype=bool)
        mask[list(S)] = True
        solved |= mask[ns % l]
odd = [n for n in range(3, X + 1, 2) if not solved[n]]
T = sorted(set([m * m for m in range(3, isqrt(X) + 1, 2)] + [5 * m * m for m in range(1, isqrt(X // 5) + 1, 2)]))
T = [t for t in T if t >= 3]
print(f"X={X}, L={L}: odd unsolved n = {len(odd)}; |T∩[3,X]| = {len(T)}; equal: {odd == T}; "
      f"extra: {sorted(set(odd) - set(T))[:20]}; T solved?: {sorted(set(T) - set(odd))[:5]}")

good = total = 0
worst = 10.0
for l in primerange(7, L2 + 1):
    if l % 5 not in (1, 4):
        continue
    for f in sqrt_mod(5, l, all_roots=True):
        f = (1 + f) * pow(2, -1, l) % l
        total += 1
        lf = legendre_symbol(f, l)
        is_good = (l % 4 == 1 and lf == -1) or (l % 4 == 3 and lf == 1)
        if is_good:
            good += 1
            S, C, m = S_q(l, f)
            assert len(S) == len(C) >= m / 2, (l, f)
            worst = min(worst, len(S) / (l ** 0.5 / (2 * np.log(l))))
print(f"split q with l <= {L2}: {total}, good: {good} ({good/total:.3f}); "
      f"min over good q of |S_q| / (l^(1/2)/(2 log l)) = {worst:.2f}")
