"""R237 from-scratch recheck of PM-SQ_± (CAP_GROWING Lemma 3.1): for non-square n = 1 (mod 8), least |u| such that some
odd prime l | n+u has (|u| | l+1 or |u| | l-1) and Legendre(-u, l) = -1.  Also checks every hit by the explicit word
(t, u, v): A = +-l, t = (A+1)/u, v = (n+u)/A, t*u*v - u - v = n, Jacobi(-A, n) = -1.
Usage: review_r237_pmsq.py NMAX"""
import sys, math
import numpy as np
from sympy import jacobi_symbol

NMAX = int(sys.argv[1]); UMAX = 200
L = NMAX + UMAX + 2
spf = np.zeros(L, dtype=np.int32)
for i in range(2, int(L**0.5) + 1):
    if spf[i] == 0:
        blk = spf[i*i::i]; m = blk == 0; blk[m] = i; spf[i*i::i] = blk
def oddprimes(m):
    out = set()
    while m > 1:
        q = int(spf[m]) or m
        out.add(q)
        while m % q == 0: m //= q
    out.discard(2); return out
def leg(a, l):
    r = pow(a % l, (l - 1) // 2, l); return -1 if r == l - 1 else r
def least_u(n):
    for au in range(1, UMAX + 1):
        for u in (au, -au):
            if u == -n: continue
            for l in oddprimes(n + u):
                if ((l + 1) % au == 0 or (l - 1) % au == 0) and leg(-u, l) == -1:
                    A = l if (l + 1) % u == 0 else -l
                    t, v = (A + 1) // u, (n + u) // A
                    assert (A + 1) % u == 0 and (n + u) % A == 0 and t * u * v - u - v == n
                    assert jacobi_symbol(-A, n) == -1
                    return au, (t, u, v, A)
    return None, None
hist = {}; rec = []; best = 0; nsq = 0; unf_sq = 0
for n in range(9, NMAX + 1, 8):
    r = math.isqrt(n)
    if r * r == n:
        nsq += 1
        # T1 check: squares should never fire
        if least_u(n)[0] is not None: unf_sq += 1
        continue
    au, w = least_u(n)
    if au is None: print("EXCEPTION", n); continue
    hist[au] = hist.get(au, 0) + 1
    if au > best: best = au; rec.append((n, au, w))
print(f"NMAX={NMAX}: non-squares {sum(hist.values())}, squares {nsq} (fired: {unf_sq})")
print("hist", dict(sorted(hist.items())))
print("records", rec)
