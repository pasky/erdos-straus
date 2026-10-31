"""z52b Pass-1 U03 Z0800: analytic rank of the quadratic twist E^(p): p*y^2 = x^3 - x (equiv. y^2 = x^3 - p^2 x), via PARI
ellanalyticrank (cypari2). For primes p = 1 mod 4, p <= PMAX. Correlate rank with log1p R_K(p) (from feat data).
Usage: uv run --with cypari2 --with numpy python scripts/z52b_p1_U03_twistrank.py PMAX"""
import sys, json, numpy as np, cypari2
PMAX = int(sys.argv[1]); pari = cypari2.Pari(); pari.allocatemem(2 * 10**9)
d = np.load("data/z52b/pass1/U03/feat_P100000_K100.npz")
pr = d["primes"]; RK = d["R"].astype(np.int64).sum(1)
rows = []
for i, p in enumerate(pr):
    p = int(p)
    if p > PMAX: break
    r, L = pari(f"ellanalyticrank(ellinit([0,0,0,{-p*p},0]),1)")[0:2] if False else (None, None)
    v = pari(f"ellanalyticrank(ellinit([0,0,0,{-p*p},0]))")
    rows.append((p, int(v[0]), float(v[1]), int(RK[i])))
rank = np.array([r[1] for r in rows]); RKs = np.array([r[3] for r in rows])
print("p<=%d: n=%d; rank distribution:" % (PMAX, len(rows)), {int(k): int((rank == k).sum()) for k in np.unique(rank)})
print("corr(rank, log1p R_K) =", round(float(np.corrcoef(rank, np.log1p(RKs))[0, 1]), 4))
print("mean R_K by rank:", {int(k): round(float(RKs[rank == k].mean()), 2) for k in np.unique(rank)})
json.dump(rows, open("data/z52b/pass1/U03/twistrank.json", "w"))
