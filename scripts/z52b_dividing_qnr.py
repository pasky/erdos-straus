"""Does least certificate-family size s(p) correlate with the least quadratic non-residue n(p)? (lane dividing, z52b)"""
import numpy as np, sys
from sympy import divisors, primerange, legendre_symbol
P = int(sys.argv[1]) if len(sys.argv) > 1 else 10**7
X_MAX = 3000
ps = np.array([p for p in primerange(2, P) if p % 840 in (1, 121, 169, 289, 361, 529)], dtype=np.int64)
fams = []
for a in range(1, X_MAX + 1):
    for d in range(1, X_MAX // a + 1):
        fams.append((a * d, 4 * a * d, {(-f) % (4 * a * d) for f in divisors(4 * a * a * d + 1)}))
for a in range(1, X_MAX + 1):
    for b in range(a, X_MAX // a + 1):
        fams.append((a * b, 4 * a * b, {(-e) % (4 * a * b) for e in divisors(a + b)}))
fams.sort(key=lambda t: (t[0], t[1]))
least = np.zeros(len(ps), dtype=np.int64); idx = np.arange(len(ps))
for s, m, res in fams:
    if len(idx) == 0: break
    tab = np.zeros(m, dtype=bool); tab[list(res)] = True
    hit = tab[ps[idx] % m]
    least[idx[hit]] = s; idx = idx[~hit]
small = list(primerange(2, 400))
def nqr(p):
    for l in small:
        if legendre_symbol(l % p, p) == -1: return l
    return 999
nq = np.array([nqr(int(p)) for p in ps])
print("corr(log s, log n(p)) =", np.corrcoef(np.log(least), np.log(nq))[0, 1])
for lo, hi in [(11, 13), (13, 20), (20, 30), (30, 50), (50, 1000)]:
    m = (nq >= lo) & (nq < hi)
    if m.sum(): print(f"n(p) in [{lo},{hi}): count={m.sum():6d} median s={np.median(least[m]):.0f} q90={np.quantile(least[m],0.9):.0f} max={least[m].max()}")
top = np.argsort(-least)[:15]
print("top s with n(p):", [(int(ps[i]), int(least[i]), int(nq[i])) for i in top])
