"""U01 fingerprint checks on existing raw m/p counts (p<=1e5, m=5..48). Usage: python3 scripts/z52b_p1_U01_fingerprint.py"""
import sys, math, collections, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from z52b_p1_U01_common import *
import numpy as np
ms = list(range(5, 49)); U = {m: load_m(m) for m in ms}; P = sorted(U[5])
F = {m: set(p for p in P if U[m][p] == 0) for m in ms}
# Z0730 both directions of divisibility monotonicity
sub = sum(1 for m in ms for k in range(2, 49) if m*k <= 48 and F[m*k] <= F[m])
sup = sum(1 for m in ms for k in range(2, 49) if m*k <= 48 and F[m] <= F[m*k])
tot = sum(1 for m in ms for k in range(2, 49) if m*k <= 48)
print("Z0730 pairs m|mk:", tot, "F(mk)<=F(m):", sub, "F(m)<=F(mk):", sup)
# Z0731 regress H(p) on Legendre symbols (q/p), q<=30 odd primes-ish, plus p mod 8,9,16,25 classes
H = {p: sum(1 for m in ms if p in F[m]) for p in P if p > 5}
pp = sorted(H)
def leg(a, p):
    a %= p
    if a == 0: return 0
    return 1 if pow(a, (p-1)//2, p) == 1 else -1
qs = [q for q in range(2, 31) if all(q % r for r in range(2, q))]
X = [[1] + [leg(q, p) for q in qs] + [int(p % 8 == j) for j in (1, 3, 5)] + [int(p % 9 == j) for j in (1, 4, 7)] for p in pp]
X = np.array(X, float); y = np.array([H[p] for p in pp], float)
b = np.linalg.lstsq(X, y, rcond=None)[0]; r2 = 1 - ((y - X@b)**2).sum()/((y - y.mean())**2).sum()
print("Z0731 R2 (Legendre q<=30 primes + mod8,mod9):", round(r2, 3), "n=", len(pp), "p>5 hardness mean", round(y.mean(), 2))
