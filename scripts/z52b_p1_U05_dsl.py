"""z52b pass1 U05 Z1380/Z1192/Z1191/Z1273: enumerative DSL search for ES solution formulas.
Atoms (functions of prime p): floor((p+a)/b) for b≤12, a∈[-12,24]; floor(sqrt p)+a (a∈[-3,3]); constants k≤30; p+a (a∈[-4,4]).
A pair (x,y) of atoms defines z = p·x·y/(4xy − p(x+y)); a 'hit' at p iff z is a positive integer (then 4/p=1/x+1/y+1/z).
Score: fraction of primes p≡1 (mod 4), 5<p≤1e5, with a hit; subsets: p≡1 mod 24 and p≡1 mod 840 (sample).
MDL-style portfolio (Z1191): greedy cover on the first half of the primes, evaluated on the second half, ranked by #atoms.
Length-ordered enumeration (Z1192): coverage as a function of total atom complexity."""
import numpy as np, math
from collections import Counter
out = []
def log(*a):
    s = " ".join(str(x) for x in a); print(s); out.append(s)
M = 100000
isp = np.ones(M+1, bool); isp[:2] = False
for i in range(2, int(M**.5)+1):
    if isp[i]: isp[i*i::i] = False
P = np.array([p for p in range(5, M+1) if isp[p] and p % 4 == 1], dtype=np.int64)
sq = np.floor(np.sqrt(P.astype(float))).astype(np.int64)
atoms = {}
for b in range(1, 13):
    for a in range(-12, 25):
        atoms[f"floor((p{a:+d})/{b})"] = (P + a)//b
for a in range(-3, 4):
    atoms[f"floor(sqrt p){a:+d}"] = sq + a
for k in range(1, 31):
    atoms[f"{k}"] = np.full(len(P), k, dtype=np.int64)
for a in range(-4, 5):
    atoms[f"p{a:+d}"] = P + a
names = list(atoms); V = np.array([atoms[n] for n in names])
log(f"atoms: {len(names)}; primes p≡1(4) ≤1e5: {len(P)}")
hits = {}
n_at = len(names)
best = []
Pf = P
for i in range(n_at):
    x = V[i]
    for j in range(i, n_at):
        y = V[j]
        den = 4*x*y - Pf*(x+y)
        num = Pf*x*y
        ok = (den > 0) & (num % np.where(den > 0, den, 1) == 0)
        if ok.any():
            hits[(i, j)] = ok
cover = {k: v.mean() for k, v in hits.items()}
top = sorted(cover.items(), key=lambda t: -t[1])[:8]
log(f"pairs with ≥1 hit: {len(hits)} of {n_at*(n_at+1)//2}; best coverage of p≡1(4), p≤1e5:")
for (i, j), c in top:
    log(f"   {c:.4f}  x={names[i]}, y={names[j]}")
allhit = np.zeros(len(P), bool)
for v in hits.values(): allhit |= v
log(f"union over all pairs: covers {allhit.mean():.4f} of primes (uncovered: {int((~allhit).sum())}; first {P[~allhit][:10].tolist()})")
mask24 = P % 24 == 1; mask840 = P % 840 == 1
log(f"  within p≡1(24): union covers {allhit[mask24].mean():.4f}; within p≡1(840): {allhit[mask840].mean():.4f} (n={int(mask840.sum())})")
# Z1191: greedy portfolio on first half, evaluated on second half
half = len(P)//2
tr = np.zeros(len(P), bool); tr[:half] = True
keys = list(hits)
chosen = []; covered = np.zeros(len(P), bool)
for _ in range(12):
    gains = [(np.sum(hits[k] & tr & ~covered), k) for k in keys]
    g, k = max(gains)
    if g == 0: break
    chosen.append(k); covered |= hits[k]
test_cov = np.zeros(len(P), bool)
for k in chosen: test_cov |= hits[k]
log(f"Z1191 greedy portfolio (≤12 pairs) trained on first half: train coverage {covered[tr].mean():.4f}, held-out coverage {test_cov[~tr].mean():.4f}; "
    f"atoms per pair = 2 (length-ordered): " + "; ".join(f"({names[i]},{names[j]})" for i, j in chosen[:4]))
# Z1192: coverage by complexity class (floor-type vs constant vs sqrt)
cls = Counter()
for (i, j), v in hits.items():
    kind = tuple(sorted(['floor' if 'floor((' in names[i] else ('sqrt' if 'sqrt' in names[i] else ('const' if names[i].isdigit() else 'lin')),
                         'floor' if 'floor((' in names[j] else ('sqrt' if 'sqrt' in names[j] else ('const' if names[j].isdigit() else 'lin'))]))
    cls[kind] |= 0
kinds = {}
for (i, j), v in hits.items():
    kk = tuple(sorted(['floor' if 'floor((' in names[i] else ('sqrt' if 'sqrt' in names[i] else ('const' if names[i].isdigit() else 'lin')),
                       'floor' if 'floor((' in names[j] else ('sqrt' if 'sqrt' in names[j] else ('const' if names[j].isdigit() else 'lin'))]))
    kinds[kk] = kinds.get(kk, np.zeros(len(P), bool)) | v
log("Z1192 coverage by atom-type pair (union over pairs of each type):", {k: round(v.mean(), 4) for k, v in kinds.items()})
# Sanity: known identity family (Mordell-type) should appear for p≡1 mod 24?  report hits on p≡1(24) by the best pair
open("data/z52b/pass1/U05/2nd/dsl_out.txt", "w").write("\n".join(out)+"\n")
