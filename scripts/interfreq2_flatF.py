"""O25: search for a 'flat' spread-spectrum minorant F (EXCEPTIONAL_INTERFREQ2 §5).
F supported on [-L, N+L];  (F1) F <= 1 on [1,N], F <= 0 outside;
(F2) sum_{n = b (d)} F = M/d for d <= N/2  (M = t N fixed);
(F3/F4) for d > C N:  F(b mod d) >= M/d - (1 - c(b,d)) + s ,  s maximised;
moduli in (N/2, C N] unconstrained; reports max |F(s) - M/d| over them.
Usage: python interfreq2_flatF.py N L t C [out.npy|-] [med]
  med: also impose the sign conditions (margin 0) for N/2 < d <= N;
       then only (N, CN] is exempt (Delta measured there)."""
import sys
import numpy as np
import scipy.sparse as sp
from scipy.optimize import linprog

N, L, t, C = int(sys.argv[1]), int(sys.argv[2]), float(sys.argv[3]), float(sys.argv[4])
pts = np.arange(-L, N + L + 1); span = len(pts); M = t * N
inside = (pts >= 1) & (pts <= N)
nv = span + 1
re, ce, ve, beq = [], [], [], []
ru, cu, vu, bub = [], [], [], []
ke = ku = 0
for d in range(1, N // 2 + 1):
    for b in range(d):
        idx = np.nonzero((pts - b) % d == 0)[0]
        re += [ke] * len(idx); ce += list(idx); beq.append(M / d); ke += 1
dmin = int(np.floor(C * N)) + 1
MED = len(sys.argv) > 6 and sys.argv[6] == "med"
if MED:
    # sign conditions with margin on N/2 < d < N, exact at d = N (Thm 5.3 variant)
    for d in range(N // 2 + 1, N + 1):
        for b in range(d):
            idx = np.nonzero((pts - b) % d == 0)[0]
            c = int(inside[idx].sum())
            u, l = -(-N // d), N // d
            m = 0.0  # no margin needed for medium moduli (level <= log N)
            if c == u:   # right positive: F >= M/d + s ; wrong negative: F <= M/d + 1
                ru += [ku] * len(idx) + [ku]; cu += list(idx) + [span]; vu += [-1.0] * len(idx) + [m]
                bub.append(-M / d); ku += 1
                ru += [ku] * len(idx); cu += list(idx); vu += [1.0] * len(idx); bub.append(M / d + (0 if d == N else 1)); ku += 1
            if c == l:   # right negative: F <= M/d - s ; wrong positive: F >= M/d - 1
                ru += [ku] * len(idx) + [ku]; cu += list(idx) + [span]; vu += [1.0] * len(idx) + [m]
                bub.append(M / d); ku += 1
                ru += [ku] * len(idx); cu += list(idx); vu += [-1.0] * len(idx); bub.append(-(M / d - (0 if d == N else 1))); ku += 1
for d in range(dmin, span + 1):
    for b in range(d):
        idx = np.nonzero((pts - b) % d == 0)[0]
        c = int(inside[idx].sum())
        # -F(s) + s <= -(M/d - (1-c))
        ru += [ku] * len(idx) + [ku]; cu += list(idx) + [span]; vu += [-1.0] * len(idx) + [1.0]
        bub.append(-(M / d - (1 - c))); ku += 1
# points (d > span)
dd = span + 1
for i in range(span):
    c = int(inside[i])
    ru += [ku, ku]; cu += [i, span]; vu += [-1.0, 1.0]; bub.append(-(M / dd - (1 - c))); ku += 1
Aeq = sp.csr_matrix((np.ones(len(re)), (re, ce)), shape=(ke, nv))
Aub = sp.csr_matrix((vu, (ru, cu)), shape=(ku, nv))
bounds = [(None, 1.0 if inside[i] else 0.0) for i in range(span)] + [(None, 1.0)]
cost = np.zeros(nv); cost[-1] = -1
res = linprog(cost, A_ub=Aub, b_ub=bub, A_eq=Aeq, b_eq=beq, bounds=bounds, method="highs")
if res.status != 0:
    print(f"N={N} L={L} t={t} C={C}: {res.message}"); sys.exit()
F = res.x[:span]; s = res.x[-1]
dev = 0.0
for d in range(N + 1 if MED else N // 2 + 1, dmin):
    for b in range(d):
        idx = np.nonzero((pts - b) % d == 0)[0]
        dev = max(dev, abs(F[idx].sum() - M / d))
if len(sys.argv) > 5 and sys.argv[5] != '-':
    np.save(sys.argv[5], np.vstack([pts, F]))
print(f"N={N} L={L} t={t} C={C}: margin s={s:.4f}  min F[1,N]={F[inside].min():.4f} "
      f"min F out={F[~inside].min():.4f}  max|F(s)-M/d| on (N/2,CN]={dev:.3f}")
