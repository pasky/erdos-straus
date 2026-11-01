"""Pass-2 SK2 statistics. Inputs (regenerate with the C programs in scripts/z52d_p2_SK2_*.c):
  /tmp/z52d_p2_SK2/c8.txt   : './cmin 100000000 3000 1 0'  (p, C-form Cmin capped at 3000; 0 = none <= 3000)
  /tmp/z52d_p2_SK2/p7_all.txt : profile to 1e7 (p R Cmin R_le2 R_le20 R_le500 Z1.01 Z1.1 Z1.5 Z2)
  /tmp/z52d_p2_SK2/prof_all.txt : profile to 1e6 (same format)
  /tmp/z52d_p2_SK2/pairs_*.txt : winning (p,C) pairs, C<=500, p<=1e5: p C phi(4C) omega(4Cp+1) ratio R_C
Output: data/z52b/pass2/SK2/stats.json
Memory: < 1 GB.  Run: ulimit -v 8000000; uv run --with numpy python scripts/z52d_p2_SK2_stats.py
"""
import json, subprocess, glob, math
import numpy as np
D = "/tmp/z52d_p2_SK2/"
out = {}
# ---- exact C_min distribution up to 1e8 (p = 1 mod 4) ----
rows = np.loadtxt(D + "c8.txt", dtype=np.int64)
p, cm = rows[:, 0], rows[:, 1]
zeros = p[cm == 0]
strag = p[cm == 0]  # capped-zeros: resolve exactly
res = subprocess.run(["/tmp/z52d_p2_SK2/starcmin"], input="\n".join(map(str, strag)) + "\n",
                     capture_output=True, text=True, check=True).stdout.split("\n")
exact = {}
for line in res:
    if line.strip():
        a = list(map(int, line.split()))
        exact[a[0]] = a[1]
cm2 = cm.copy()
for i in np.where(cm == 0)[0]:
    cm2[i] = exact[int(p[i])]
N = len(p)
out["census_1e8"] = {
    "n_primes_1mod4": int(N), "n_star_zero": int(np.sum(cm2 == 0)),
    "star_zero_primes": [int(x) for x in p[cm2 == 0]],
    "max_Cmin": int(cm2.max()), "argmax_p": int(p[np.argmax(cm2)]),
    "mean_Cmin": float(cm2[cm2 > 0].mean()),
    "P_Cmin_eq": {str(c): float(np.mean(cm2 == c)) for c in [1, 2, 3, 4, 5, 10]},
    "P_Cmin_le": {str(c): float(np.mean((cm2 <= c) & (cm2 > 0))) for c in [1, 2, 5, 10, 20, 50, 100, 1000]},
    "quantiles": {q: int(np.quantile(cm2[cm2 > 0], q)) for q in [0.5, 0.9, 0.99, 0.999]},
    "stragglers_exact_gt3000": {str(int(x)): int(exact[int(x)]) for x in strag if exact[int(x)] > 3000},
}
# records of Cmin (record-setters) with p
recs = []; best = 0
for pi, ci in zip(p, cm2):
    if ci > best:
        best = int(ci); recs.append((int(pi), best))
out["census_1e8"]["records"] = recs
# mod 24 split of P(Cmin<=2)
m24 = p % 24
out["census_1e8"]["P_Cmin_le2_by_mod24"] = {str(r): float(np.mean(cm2[(m24 == r)] <= 2)) for r in [1, 13, 17, 5]}
# P(Cmin > K) for K = log p, by decade
dec = {}
for lo in [1e4, 1e5, 1e6, 1e7]:
    sel = (p >= lo) & (p < 10 * lo)
    K = np.log(p[sel])
    dec[str(int(lo))] = {"frac_Cmin_gt_logp": float(np.mean(cm2[sel] > K)),
                         "frac_Cmin_gt_logp2": float(np.mean(cm2[sel] > K * K)),
                         "frac_Cmin_gt_10": float(np.mean(cm2[sel] > 10)),
                         "n": int(sel.sum())}
out["census_1e8"]["tail_by_decade"] = dec
# ---- profile statistics ----
pr = np.loadtxt(D + "p7_all.txt")
P, R, Cmn, R2, R20, R500 = pr[:, 0], pr[:, 1], pr[:, 2], pr[:, 3], pr[:, 4], pr[:, 5]
Zs = pr[:, 6:10]
sel = (P > 1e5) & (P < 1e7)
Rp = R[sel]
out["profile_1e7"] = {
    "n": int(sel.sum()),
    "share_R_from_C_le_2_mean": float(np.mean(R2[sel] / np.maximum(Rp, 1))),
    "share_R_from_C_le_20_mean": float(np.mean(R20[sel] / np.maximum(Rp, 1))),
    "share_R_from_C_le_500_mean": float(np.mean(R500[sel] / np.maximum(Rp, 1))),
    "R_zero_primes_le_1e7": [int(x) for x in P[R == 0]],
}
# R^2 of regression log R ~ a + b log R_le20 (and log R_le2), over p in (1e5,1e7), R>0 everywhere in the sample
ok = sel & (R2 > 0) & (R20 > 0) & (R > 0)
x1 = np.log(R20[ok]); x2 = np.log(R2[ok]); y = np.log(R[ok])
def r2(X, y):
    X1 = np.column_stack([np.ones(len(y)), X]); b, *_ = np.linalg.lstsq(X1, y, rcond=None)
    res = y - X1 @ b; return float(1 - res.var() / y.var()), b.tolist()
out["profile_1e7"]["R2_logR_on_logR_le20"], out["profile_1e7"]["coef_le20"] = r2(x1[:, None], y)
out["profile_1e7"]["R2_logR_on_logR_le2"], out["profile_1e7"]["coef_le2"] = r2(x2[:, None], y)
out["profile_1e7"]["corr_R_vs_Rle20_ratio_log"] = float(np.corrcoef(np.log(R20[ok] / R[ok]), y)[0, 1])
# Z_p(s) concentration over p = 1 mod 24 in (1e5,1e6) and (1e5,1e7): CV and lower-tail fraction
m24b = (P % 24 == 1)
zc = {}
for j, s in enumerate(["1.01", "1.1", "1.5", "2"]):
    z = Zs[sel & m24b, j]
    zc[s] = {"n": int(z.size), "mean": float(z.mean()), "cv": float(z.std() / z.mean()),
             "frac_Z_below_0.1mean": float(np.mean(z < 0.1 * z.mean())),
             "frac_Z_below_1": float(np.mean(z < 1.0)), "min": float(z.min())}
out["profile_1e7"]["Z_concentration_p1mod24"] = zc
# ---- winning pairs (p <= 1e5, C <= 500) ----
pairs = np.vstack([np.loadtxt(fn, dtype=float, ndmin=2) for fn in sorted(glob.glob(D + "pairs_*.txt"))])
pp, cc, phi, om, ratio, rc = pairs.T
out["pairs_1e5_C500"] = {
    "n_winning_pairs": int(len(pp)),
    "ratio_phi4C_over_2^omega_quantiles": {str(q): float(np.quantile(ratio, q)) for q in [0.01, 0.1, 0.25, 0.5, 0.75, 0.9, 0.99]},
    "frac_ratio_le_1": float(np.mean(ratio <= 1.0)),
}
# win rate per C (over all p = 1 mod 4 <= 1e5) vs phi(4C)
primes_1e5 = p[(p <= 1e5)]
ncount = len(primes_1e5)
win = np.bincount(cc.astype(int), minlength=501)[:501].astype(float)
Cs = np.arange(1, 501)
w = win[1:501] / ncount
top = np.argsort(-w)[:8] + 1
out["pairs_1e5_C500"]["win_rate_top_C"] = {str(int(c)): float(win[c] / ncount) for c in top}
phi4 = np.array([sum(1 for k in range(1, 4 * c + 1) if math.gcd(k, 4 * c) == 1) for c in Cs])
ok2 = w > 0
out["pairs_1e5_C500"]["corr_log_winrate_vs_log_phi4C"] = float(np.corrcoef(np.log(w[ok2]), np.log(phi4[ok2]))[0, 1])
out["pairs_1e5_C500"]["mean_winrate_C_le_2"] = float(np.mean(w[:2]))
out["pairs_1e5_C500"]["n_primes_1mod4_le_1e5"] = int(ncount)
json.dump(out, open("data/z52b/pass2/SK2/stats.json", "w"), indent=1)
print(json.dumps({k: out[k] for k in ["census_1e8"]}, indent=0)[:3000])
print(json.dumps(out["profile_1e7"], indent=0)[:2500])
print(json.dumps(out["pairs_1e5_C500"], indent=0)[:1500])
