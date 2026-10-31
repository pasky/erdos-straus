"""U01 Z0900: p-1 practical vs ES hardness U4(p) (p<=3e4, from data/z52b/raw/f4_all_30000.txt)."""
import sys, math, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from z52b_p1_U01_common import *
import numpy as np
def factor(n):
    f = {}; d = 2
    while d*d <= n:
        while n % d == 0: f[d] = f.get(d, 0)+1; n //= d
        d += 1
    if n > 1: f[n] = f.get(n, 0)+1
    return f
def practical(n):
    if n == 1: return True
    if n % 2: return False
    s = 1
    for q, e in sorted(factor(n).items()):
        if q > s+1: return False
        s *= (q**(e+1)-1)//(q-1)
    return True
f4 = load_counts(os.path.join(RAW, "f4_all_30000.txt"))
pr = [p for p in primes_upto(30000) if p > 5 and p in f4]
U4 = {p: f4[p][0] for p in pr}
prac = {p: practical(p-1) for p in pr}
X = np.array([math.log(p) for p in pr]); A = np.array([math.log(U4[p]+1) for p in pr])
res = A - np.polyval(np.polyfit(X, A, 2), X)
print("practical(p-1) fraction:", round(np.mean([prac[p] for p in pr]), 3), "n=", len(pr))
top = sorted(pr, key=lambda p: -U4[p])[:30]
print("top30 by U4: practical(p-1) count", sum(prac[p] for p in top))
for c in (8, 24):
    out = []
    for r in sorted(set(p % c for p in pr if p % 2 == 1)):
        idx = [i for i, p in enumerate(pr) if p % c == r]
        a = [res[i] for i in idx if prac[pr[i]]]; b = [res[i] for i in idx if not prac[pr[i]]]
        if len(a) > 20 and len(b) > 20: out.append((r, len(a), round(np.mean(a)-np.mean(b), 3)))
    print(f"within p mod {c}: (class, n_practical, mean resid diff practical-minus-not):", out)
