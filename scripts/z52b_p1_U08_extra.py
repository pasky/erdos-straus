"""z52b pass-1 batch U08, extra checks for Z1142 (degree-preserving null) and Z2583 (BDH-type class variance).
Z1142: the family-prime incidence matrix (Type I families, ad <= 60, p ≡ 1 mod 4 sample of 40) vs checkerboard-swap nulls
       that preserve BOTH row and column sums.   Z2583: sum over residue classes a mod q of (sum_{p ≡ a} (U(p)-Ubar))^2
       against the independent-class prediction, U = #solutions of 4/p for primes 101 < p <= 30000 (f4 data)."""
import json, math, os
import numpy as np
from sympy import divisors, primerange
from z52b_p1_U08_core import load_U, primes_1mod4
OUT = "data/z52b/pass1/U08"
rng = np.random.default_rng(13)
fams = []
for a in range(1, 61):
    for d in range(1, 61):
        if a * d > 60: continue
        for f in divisors(4 * a * a * d + 1):
            if f <= 4 * a * d:
                fams.append((4 * a * d, (-f) % (4 * a * d)))
ps = primes_1mod4(101, 30000)
sample = [int(x) for x in rng.choice(ps, size=40, replace=False)]
M = np.array([[(p % m) == r for (m, r) in fams] for p in sample], dtype=np.int64)
def swaps(M, nsw=20000):
    M = M.copy(); R, C = M.shape; done = 0
    for _ in range(nsw * 5):
        i, j = rng.integers(R, size=2)
        if i == j: continue
        cols = np.where((M[i] == 1) & (M[j] == 0))[0]
        cols2 = np.where((M[i] == 0) & (M[j] == 1))[0]
        if len(cols) and len(cols2):
            a = rng.choice(cols); b = rng.choice(cols2)
            M[i, a] = 0; M[j, a] = 1; M[i, b] = 1; M[j, b] = 0; done += 1
            if done >= nsw: break
    return M
sv = np.linalg.svd(M.astype(float), compute_uv=False)[:3]
top_null = []
for _ in range(30):
    Mz = swaps(M, 3000)
    top_null.append(np.linalg.svd(Mz.astype(float), compute_uv=False)[0])
z1142 = dict(top3=[round(float(x), 3) for x in sv], checkerboard_null_top1_mean=round(float(np.mean(top_null)), 3),
             checkerboard_null_top1_sd=round(float(np.std(top_null)), 3), row_sums_preserved=True)
# Z2583
Ud = load_U()
P = [p for p in primes_1mod4(101, 30000)]
U = np.array([Ud[p] for p in P], float)
Ub = U.mean(); dev = U - Ub
z2583 = {}
for q in [5, 7, 8, 12, 24, 13]:
    cls = np.array([p % q for p in P])
    tot = 0.0
    for a in np.unique(cls):
        tot += dev[cls == a].sum() ** 2
    # independent-class prediction: each class sum has variance ~ n_a * var
    pred = float(np.sum(dev ** 2) * np.sum([1 for _ in np.unique(cls)]) / len(P)) if False else float(np.sum(np.array([np.sum(dev[cls == a] ** 2) for a in np.unique(cls)])))
    z2583[q] = dict(classes=int(len(np.unique(cls))), between_class_sum_sq_ratio=round(tot / pred, 4) if pred else None)
os.makedirs(OUT, exist_ok=True)
json.dump(dict(Z1142=z1142, Z2583=z2583), open(f"{OUT}/redo_extra.json", "w"), indent=1)
print(json.dumps(dict(Z1142=z1142, Z2583=z2583), indent=1))
