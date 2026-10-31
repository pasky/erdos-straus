"""z52b pass-1 batch U08, moment/tail checks on U(p) = #solutions of 4/p (f4_all_30000.txt), primes p ≡ 1 (mod 4), 100 < p <= 30000.
  Z1354  intermittency: <U^q> over dyadic ranges, q = -2..4 (log-log slope in log p)
  Z2526  fractional lower-tail moments E[U^{-s}], s = 0.5, 1, 2 (whole range)
  Z1759  annealed vs quenched gap: log E[U] - E[log U] per dyadic range (lognormal predicts sigma^2/2)
  Z1746 / Z1327  lag-1..3 autocorrelation of the log-residual along the prime sequence (residual of log U on log log p)
Output: data/z52b/pass1/U08/moments.json"""
import json, os, math
import numpy as np
from sympy import primerange
F = np.loadtxt("data/z52b/raw/f4_all_30000.txt", dtype=np.int64)
Ud = dict(zip(F[:, 0].tolist(), F[:, 1].tolist()))
ps = np.array([p for p in primerange(100, 30001) if p % 4 == 1])
U = np.array([Ud[int(p)] for p in ps], float)
out = {}
edges = [100, 300, 1000, 3000, 10000, 30000]
dy = {}
for lo, hi in zip(edges[:-1], edges[1:]):
    m = (ps > lo) & (ps <= hi)
    u = U[m]
    mom = {q: float(np.mean(u ** q)) for q in [-2, -1, 1, 2, 3, 4]}
    gap = float(math.log(u.mean()) - np.mean(np.log(u)))
    dy[f"({lo},{hi}]"] = dict(n=int(m.sum()), moments={str(q): round(v, 4) for q, v in mom.items()},
                               jensen_gap=round(gap, 4), sd_logU=round(float(np.std(np.log(u))), 4))
out["Z1354_Z1759"] = dy
# slopes of log<U^q> vs log(p) across dyadic bins: use bin centres (geometric)
cent = [math.sqrt(lo * hi) for lo, hi in zip(edges[:-1], edges[1:])]
slopes = {}
for q in [-2, -1, 1, 2, 3, 4]:
    y = [math.log(dy[k]["moments"][str(q)]) for k in dy]
    x = [math.log(c) for c in cent]
    slopes[str(q)] = round(float(np.polyfit(x, y, 1)[0]), 3)
out["Z1354_slopes_vs_logp"] = slopes
# fractional lower-tail moments (Z2526)
out["Z2526_frac_lower_moments"] = {str(s): round(float(np.mean(U ** (-s))), 6) for s in [0.5, 1, 2]}
# lag autocorrelation of log-residual along primes (Z1746, Z1327)
X = np.vstack([np.ones(len(ps)), np.log(np.log(ps))]).T
y = np.log(U)
b = np.linalg.lstsq(X, y, rcond=None)[0]
r = y - X @ b
ac = {}
for lag in [1, 2, 3]:
    a, c = r[:-lag], r[lag:]
    ac[str(lag)] = round(float(np.corrcoef(a, c)[0, 1]), 4)
out["Z1746_Z1327_lag_autocorr"] = ac
out["n_primes"] = int(len(ps))
os.makedirs("data/z52b/pass1/U08", exist_ok=True)
json.dump(out, open("data/z52b/pass1/U08/moments.json", "w"), indent=1)
print(json.dumps(out, indent=1))
