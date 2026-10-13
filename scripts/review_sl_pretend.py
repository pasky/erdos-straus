"""R175: correlation of W(p) (Type I slice a=1) with log L_y(1, chi_p), y = 50, primes p = 1 mod 4 in [A, B).
Uses W array from review_sl_wcount.py (np.save)."""
import sys, numpy as np, math
from review_sl_rayclass import jac
W = np.load(sys.argv[1]); A, B, y = int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4])
sv = np.ones(B, bool); sv[:2] = False
for i in range(2, int(B ** .5) + 1):
    if sv[i]: sv[i*i::i] = False
ells = [l for l in range(2, y + 1) if sv[l]]
ps = [p for p in range(A, B) if sv[p] and p % 4 == 1]
logL = np.array([sum(-math.log(1 - (jac(l, p) if l > 2 else (1 if p % 8 == 1 else -1)) / l) for l in ells) for p in ps])
w = np.array([W[p] for p in ps], float); wn = w / np.array([math.log(p) ** 2 for p in ps])
print("primes", len(ps), "corr(W, logL)", round(float(np.corrcoef(w, logL)[0, 1]), 3), "corr(W/log^2, logL)", round(float(np.corrcoef(wn, logL)[0, 1]), 3))
o = np.argsort(logL); k = len(ps) // 10
print("mean W/log^2 p: bottom decile", round(float(wn[o[:k]].mean()), 3), "top decile", round(float(wn[o[-k:]].mean()), 3))
