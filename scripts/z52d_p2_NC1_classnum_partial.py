# z52d pass2 NC1 Z1686 follow-up: partial correlation of h(-4p)/sqrt p with R(p)/log^2 p for primes p ≡ 1 mod 4, p<1e5,
# controlling for log p, p mod 840 (class dummies) and Legendre symbols (p/q), q = 11..47 (small primes not in 840).
import math, json, sys
import numpy as np
from sympy import primerange, legendre_symbol
sys.path.insert(0, 'scripts')
def h_neg(D):
    h = 0; Dn = -D; a = 1
    while 3*a*a <= Dn:
        for b in range(-a+1, a+1):
            if (b*b + Dn) % (4*a): continue
            c = (b*b + Dn)//(4*a)
            if c < a or math.gcd(math.gcd(a, abs(b)), c) != 1: continue
            if c == a and b < 0: continue
            h += 1
        a += 1
    return h
def R(p):
    tot = 0
    for C in range(1, 51):
        N = 4*C*p+1; m = 4*C; d = m-1
        while d*d <= N:
            if N % d == 0: tot += 1
            d += m
    return tot
qs = [11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
rows = []
for p in primerange(5, 100000):
    if p % 4 != 1: continue
    rows.append((p, h_neg(-4*p)/math.sqrt(p), R(p)/math.log(p)**2))
P = np.array([r[0] for r in rows]); X1 = np.array([r[1] for r in rows]); Y = np.array([r[2] for r in rows])
classes = sorted(set(int(p % 840) for p in P))
D = np.array([[1.0 if int(p % 840) == c else 0.0 for c in classes[1:]] for p in P])
L = np.array([[legendre_symbol(int(p), q) for q in qs] for p in P], dtype=float)
Z = np.column_stack([np.ones(len(P)), np.log(P), L, D])
def resid(v):
    beta, *_ = np.linalg.lstsq(Z, v, rcond=None); return v - Z @ beta
rx, ry = resid(X1), resid(Y)
pc = float(np.corrcoef(rx, ry)[0, 1])
raw = float(np.corrcoef(X1, Y)[0, 1])
# baseline: correlation with only log p and class dummies (no Legendre)
Z0 = np.column_stack([np.ones(len(P)), np.log(P), D])
def resid0(v):
    beta, *_ = np.linalg.lstsq(Z0, v, rcond=None); return v - Z0 @ beta
pc0 = float(np.corrcoef(resid0(X1), resid0(Y))[0, 1])
# permutation null: shuffle Y within classes of p mod 840 (keeps class), recompute partial corr (500 draws)
rng = np.random.default_rng(0); null = []
for _ in range(200):
    Ys = Y.copy()
    for c in classes:
        idx = np.where(P % 840 == c)[0]
        Ys[idx] = Y[rng.permutation(idx)]
    null.append(float(np.corrcoef(resid(X1), resid(Ys))[0, 1]))
print(json.dumps({'n_primes': len(P), 'raw_pearson': round(raw, 4), 'partial_given_logp_mod840': round(pc0, 4),
                  'partial_given_logp_mod840_and_legendre_11..47': round(pc, 4),
                  'null_within_class_shuffle_mean': round(float(np.mean(null)), 4),
                  'null_within_class_shuffle_sd': round(float(np.std(null)), 4)}, indent=1))
