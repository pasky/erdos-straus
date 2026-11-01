# z52d pass2 NC1 Z1377/Z1309: k-kernel rank test for g(n) = least C ≥1 with a divisor d ≡ -1 (mod 4C) of 4Cn+1 (all n ≡ 1 mod 4,
# n ≤ M; g capped at 200, 0 if none). A k-regular sequence has a finite k-kernel (span of g(k^e n + r) over r<k^e, e≥0);
# we measure the Q-rank (mod a large prime) of the set {g(k^e n + r) restricted to n in [1, N)} as e grows.
import numpy as np, sys
P = 2**31 - 1
M = 2**21
def g_of(n, cap=200):
    for C in range(1, cap+1):
        N = 4*C*n+1; m = 4*C; d = m-1; ok = False
        while d*d <= N:
            if N % d == 0: ok = True; break
            d += m
        if ok: return C
    return 0
def rank_mod_p(rows):
    A = np.array(rows, dtype=np.int64) % P
    r = 0; nrows, ncols = A.shape
    for c in range(ncols):
        piv = None
        for i in range(r, nrows):
            if A[i, c] != 0: piv = i; break
        if piv is None: continue
        A[[r, piv]] = A[[piv, r]]
        inv = pow(int(A[r, c]), P-2, P)
        A[r] = (A[r]*inv) % P
        for i in range(nrows):
            if i != r and A[i, c] != 0:
                A[i] = (A[i] - A[i, c]*A[r]) % P
        r += 1
        if r == nrows: break
    return r
# all n ≤ M/2^E need values; compute g on [0, M)
g = np.zeros(M+1, dtype=np.int64)
for n in range(1, M+1):
    if n % 4 == 1: g[n] = g_of(n)
    else: g[n] = -1  # not used (we restrict to n ≡ 1 mod 4 only through the sequence on all n; see below)
# Use the full integer sequence g(n) for all n (define g for all n with the same rule)
for n in range(1, M+1):
    if g[n] == -1: g[n] = g_of(n)
out = []
for k in [2, 3]:
    for E in range(1, (7 if k == 2 else 6)):
        N = 700  # length of each subsequence (n in [1,N])
        rows = []
        for e in range(0, E+1):
            for r in range(k**e):
                row = []
                for n in range(1, N+1):
                    idx = k**e * n + r
                    row.append(int(g[idx]) if idx <= M else 0)
                rows.append(row)
        rk = rank_mod_p(rows)
        out.append((k, E, len(rows), rk))
        print(f'k={k} E={E} subsequences={len(rows)} rank={rk}', flush=True)
