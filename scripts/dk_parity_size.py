"""O169 §7: do SIZE/Dedekind-type sub-counts of the X-slice have a parity law?
E_X(p) = {(t,u,v) >= 1 : tuv-u-v = p, 4 | tu-1} (ordered; WINDMILL_REDUCTION §6), A = tu-1, A* = tv-1.
Literals: size comparisons among t,u,v,A,A*,p-quantiles, floor parities of 12 s(A,p) and of A/sqrt p etc.
Sub-count = #{x in E_X(p): L1(x) and L2(x)} for literals L1, L2 (and negations).
Report literal pairs whose sub-count is ODD for all primes p = 1 (24), p <= N (would be a parity-law candidate).
Usage: PYTHONPATH=scripts uv run python scripts/dk_parity_size.py N
"""
import sys
from math import isqrt
from itertools import combinations
N = int(sys.argv[1])

def EX(p):
    out = []
    for t in range(1, p + 3):
        if t * 1 * 1 - 2 > p: break
        for u in range(1, p + 2):
            m = t * u - 1
            if m <= 0: continue
            if m - u > p and m > 0: break
            if (tu1 := m) % 4: continue
            if (p + u) % m == 0:
                v = (p + u) // m
                if v >= 1: out.append((t, u, v))
    return out

def lits(p, t, u, v):
    A, As = t * u - 1, t * v - 1
    s12 = t + u + v - 9 + (A + As) / p  # 12 s(A,p) for interior points (formula)
    q = isqrt(p)
    L = {
        "u<v": u < v, "t<u": t < u, "t<v": t < v, "t<min": t < min(u, v), "t>max": t > max(u, v),
        "A<p/2": 2 * A < p, "A<As": A < As, "A<sqrtp": A < q, "As<sqrtp": As < q,
        "t<cbrt": t ** 3 < p, "u<cbrt": u ** 3 < p, "v<cbrt": v ** 3 < p,
        "fl12s_odd": int(s12 // 1) % 2 == 1, "fl(A+As)/p_odd": ((A + As) // p) % 2 == 1,
        "flA/sqrt_odd": (A // max(q, 1)) % 2 == 1, "fltuv_quart": (4 * A // p) % 2 == 1,
        "t^2<u": t * t < u, "t^2<v": t * t < v, "uv<t": u * v < t, "u^2<v": u * u < v,
    }
    return L

primes = [p for p in range(25, N + 1, 24) if all(p % q for q in range(2, isqrt(p) + 1))]
names = None
alive = None
for p in primes:
    pts = [lits(p, *x) for x in EX(p)]
    if names is None:
        names = list(pts[0].keys())
        L2 = [(a, sa) for a in names for sa in (True, False)]
        cands = [(x,) for x in L2] + list(combinations(L2, 2))
        alive = set(cands)
    for c in list(alive):
        cnt = sum(1 for P in pts if all(P[a] == sa for a, sa in c))
        if cnt % 2 == 0:
            alive.discard(c)
print(f"N={N}: primes p=1(24): {len(primes)}; literal (pairs) tested: {len(cands)}; constant-odd survivors: {sorted(alive)}")
