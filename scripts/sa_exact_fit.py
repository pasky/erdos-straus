"""O167 §9.1: do cubic-certificate counts W(n) = sum over (g,u,v)>=1 with g*u*v-u-v = n of weight
have a closed form in Eisenstein-type functions of n, n+1, n+2 (unshifted + small shifts)?
Least squares on train range, residual on test range (odd n).  Exact integer data; numpy only."""
import sys, numpy as np
N = int(sys.argv[1]) if len(sys.argv) > 1 else 10000
W = {k: np.zeros(N + 3) for k in ["all", "all_m", "typeII", "typeII_m", "u>1", "u>1_m"]}
for u in range(1, N + 3):
    for v in range(u, N + 3):
        if (u - 1) * (v - 1) > N + 1: break
        uv = u * v
        # n = g*uv - u - v, g >= 1
        g0 = 1
        for g in range(g0, (N + u + v) // uv + 1):
            n = g * uv - u - v
            if n < 1: continue
            if n > N: break
            for (a, b) in ((u, v),) if u == v else ((u, v), (v, u)):
                m = g * a - 1
                W["all"][n] += 1; W["all_m"][n] += m
                if a > 1: W["u>1"][n] += 1; W["u>1_m"][n] += m
                if g % 2 == 1 and m % 4 == 0: W["typeII"][n] += 1; W["typeII_m"][n] += m
# basis
def sig(k, chi, psi, n):
    s = 0
    for d in range(1, int(n**0.5) + 1):
        if n % d == 0:
            e = n // d
            s += chi(d) * psi(e) * d**k
            if e != d: s += chi(e) * psi(d) * e**k
    return s
one = lambda x: 1
c4 = lambda x: 0 if x % 2 == 0 else (1 if x % 4 == 1 else -1)
c3 = lambda x: 0 if x % 3 == 0 else (1 if x % 3 == 1 else -1)
c8 = lambda x: 0 if x % 2 == 0 else (1 if x % 8 in (1, 7) else -1)
chars = [one, c4, c3, c8]
ns = np.arange(5, N + 1, 2)
cols, names = [], []
for sh in (0, 1, 2):
    for k in (0, 1):
        for i, ch in enumerate(chars):
            for j, ps in enumerate(chars):
                if k == 0 and j > i: continue
                cols.append([sig(k, ch, ps, n + sh) for n in ns]); names.append(f"s{k}[{i}{j}](n+{sh})")
for e in range(3):
    for r in range(24):
        cols.append([(n**e if n % 24 == r else 0) for n in ns]); names.append(f"n^{e}[n={r} mod 24]")
A = np.array(cols, dtype=float).T
A /= np.maximum(np.abs(A).max(axis=0), 1)
tr = ns <= N // 2; te = ~tr
for key, w in W.items():
    y = w[ns].astype(float)
    coef, *_ = np.linalg.lstsq(A[tr], y[tr], rcond=None)
    pred = A @ coef
    r_tr = np.abs(pred[tr] - y[tr]).max(); r_te = np.abs(pred[te] - y[te]).max()
    sq = [n for n in ns if int(round(n**.5))**2 == n]
    print(f"{key:9s} basis={A.shape[1]} max|res| train={r_tr:.3g} test={r_te:.3g} "
          f"mean|y| test={np.abs(y[te]).mean():.3g}  min over odd squares={min(w[sq]):.0f}")
