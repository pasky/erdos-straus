# z68_sign_graph_check.py — independent small-n check of the move-graph edge count of z68_sign_graph.c.
# Moves generated directly from Lemma 2 by brute force over cuts and ALL k, building target words by concatenation.
import sys, subprocess, re
from math import gcd
def hj(N, D):
    w = []
    while D > 0:
        b = -(-N // D); w.append(b); N, D = D, b * D - N
    return w
def K(w):
    a, b = 1, 0
    for x in w: a, b = x * a - b, a
    return a
def edges(n):
    E = 0
    for A in range(1, n):
        if gcd(A, n) != 1: continue
        w = hj(n, A); r = len(w)
        for j in range(r):
            L, b, Rt = w[:j], w[j], w[j + 1:]
            X, Xp = K(L[::-1]), (K(L[::-1][1:]) if L else 0)      # X/X' = [[b_j..b_1]]
            Y, Yp = K(Rt), (K(Rt[1:]) if Rt else 0)
            for k in range(2, b // 2 + 1):
                if b % k: continue
                # right move
                if Xp >= 1 and Yp % k == 0 and gcd(k, Xp) == 1:
                    nw = hj(k * X, Xp)[::-1] + [b // k] + (hj(Y, Yp // k) if Yp else [])
                    assert K(nw) == n and min(nw) >= 2; E += 1
                if Yp >= 1 and Xp % k == 0 and gcd(k, Yp) == 1:
                    nw = (hj(X, Xp // k)[::-1] if Xp else []) + [b // k] + hj(k * Y, Yp)
                    assert K(nw) == n and min(nw) >= 2; E += 1
    return E
ns = [17, 41, 89, 97, 113, 225, 289, 409, 1089]
out = subprocess.run(['/tmp/z68g'] + [str(n) for n in ns], capture_output=True, text=True).stdout
cE = {int(m.group(1)): int(m.group(2)) for m in re.finditer(r'n=(\d+) V=\d+ E=(\d+)', out)}
for n in ns:
    e = edges(n); print(n, e, cE[n], 'OK' if e == cE[n] else 'MISMATCH'); assert e == cE[n]
