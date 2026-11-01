"""z52d avenue Q03 (Z0969): is the U(p) ~ U((p+3)/4) residual correlation the shared local factor?
p = 4q - 3 gives p - 1 = 4(q - 1), so p == 1 (mod l) <=> q == 1 (mod l) for odd l: the 'p-1 smooth' axis
(RESIDUE_HARDNESS) is inherited. Partial out a crude local proxy S(n) = sum_{l | n-1, 3<=l<=50 prime} log l/(l-1)."""
import sys, math, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from z52b_p1_U01_common import *
import numpy as np
f4 = load_counts(os.path.join(RAW, "f4_all_30000.txt"))
P = set(primes_upto(30000))
pairs = [(p, (p+3)//4) for p in sorted(P) if p > 20 and (p+3) % 4 == 0 and (p+3)//4 in P and (p+3)//4 > 5 and p in f4 and (p+3)//4 in f4]
def resid(ns):
    X = np.array([math.log(n) for n in ns]); A = np.array([math.log(f4[n][0]+1) for n in ns])
    return A - np.polyval(np.polyfit(X, A, 2), X)
smallp = [l for l in primes_upto(50) if l >= 3]
def S(n): return sum(math.log(l)/(l-1) for l in smallp if (n-1) % l == 0) + (0.5 if (n-1) % 8 == 0 else 0)
ps = [a for a, b in pairs]; qs = [b for a, b in pairs]
ra, rb = resid(ps), resid(qs)
print("pairs", len(pairs), "resid corr", round(np.corrcoef(ra, rb)[0, 1], 3))
def partial(r, s):
    s = np.array(s); X = np.vstack([np.ones_like(s), s]).T
    return r - X @ np.linalg.lstsq(X, r, rcond=None)[0]
sa = [S(p) for p in ps]; sb = [S(q) for q in qs]
print("corr(S(p),S(q))", round(np.corrcoef(sa, sb)[0, 1], 3), " corr(resid p, S(p))", round(np.corrcoef(ra, sa)[0, 1], 3))
pa, pb = partial(ra, sa), partial(rb, sb)
print("resid corr after partialling S", round(np.corrcoef(pa, pb)[0, 1], 3))
# richer proxy: least-squares on indicators 1[l^k | n-1] for prime powers l^k <= 125 (k>=1, l odd) and 2^k, k<=6
pp = sorted({l**k for l in primes_upto(125) for k in range(1, 8) if l**k <= 128})
def F(ns): return np.array([[1.0] + [1.0 if (n-1) % d == 0 else 0.0 for d in pp] for n in ns])
def partialF(r, ns):
    X = F(ns); return r - X @ np.linalg.lstsq(X, r, rcond=None)[0]
pa2, pb2 = partialF(ra, ps), partialF(rb, qs)
print(len(pp), "features; resid corr after partialling p-1 / q-1 divisibility indicators:", round(np.corrcoef(pa2, pb2)[0, 1], 3))
# same features fitted on ALL primes (avoid overfitting on 270 pairs)
allp = [p for p in sorted(P) if p > 5 and p in f4]
rall = resid(allp); X = F(allp); beta = np.linalg.lstsq(X, rall, rcond=None)[0]
fit = dict(zip(allp, X @ beta)); ra_all = dict(zip(allp, rall))
a = np.array([ra_all[p] - fit[p] for p in ps]); b = np.array([ra_all[q] - fit[q] for q in qs])
print("R^2 of divisibility model on all primes:", round(1 - np.var(rall - X @ beta)/np.var(rall), 3), "; pair corr of out-of-model residuals:", round(np.corrcoef(a, b)[0, 1], 3))
