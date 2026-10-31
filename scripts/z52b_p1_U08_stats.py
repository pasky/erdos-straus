"""z52b pass-1 batch U08 statistics on the U(n) = #solutions of 4/n data (data/z52b/raw/f4_all_30000.txt, n <= 30000).

Items:
  Z0809  is U(p)/log^2 p approximately lognormal?  (residual skew/kurtosis, lower tail P(U<=5) vs normal prediction)
  Z0883  lower envelope of U(p): window minima vs Gumbel scaling
  Z2604  Sarnak-type disjointness: correlation of a 'low-U' indicator at primes p ≡ 1 (4) with mu((p-1)/4)
  Z0333  random thinning of denominators: failure fraction vs exp(-rho^3 U) (uses enumeration from z52b_p1_U08_enum)

Memory: a few MB; the thinning part enumerates solutions for ~100 primes only.
Run: uv run --with numpy --with sympy python scripts/z52b_p1_U08_stats.py
"""
import json, math, os, random
import numpy as np
from sympy import primerange, mobius, factorint
import importlib.util

OUT = "data/z52b/pass1/U08"
os.makedirs(OUT, exist_ok=True)
F = np.loadtxt("data/z52b/raw/f4_all_30000.txt", dtype=np.int64)
Ud = dict(zip(F[:, 0].tolist(), F[:, 1].tolist()))
primes = [p for p in primerange(1000, 30001) if p % 4 == 1]
U = np.array([Ud[p] for p in primes], float)
P = np.array(primes, float)
lp = np.log(P)
res = {}

# --- Z0809: lognormal-ness of the residual of log U against log log p ---
X = np.vstack([np.ones_like(lp), np.log(lp)]).T
y = np.log(U)
b = np.linalg.lstsq(X, y, rcond=None)[0]
r = y - X @ b
m, s = r.mean(), r.std(ddof=1)
skew = float(((r - m) ** 3).mean() / s ** 3)
kurt = float(((r - m) ** 4).mean() / s ** 4 - 3)
# lower tail: observed count with U <= K vs normal prediction on the residual scale
pred_fracs = {}
for K in [2, 5, 10, 20]:
    thr = math.log(K) - X @ b  # per-prime threshold on residual scale
    pred = float(np.mean(0.5 * (1 + np.array([math.erf((t - m) / (s * math.sqrt(2))) for t in thr]))))
    obs = float(np.mean(U <= K))
    pred_fracs[K] = dict(obs=round(obs, 5), normal_pred=round(pred, 5))
res["Z0809"] = dict(n=len(primes), slope_loglog=round(float(b[1]), 4), resid_sd=round(float(s), 4),
                    resid_skew=round(skew, 4), resid_excess_kurt=round(kurt, 4), lower_tail=pred_fracs,
                    min_U=int(U.min()), argmin_p=int(P[U.argmin()]))

# --- Z0883: window minima of U/log^3 p over windows of N consecutive primes (≡1 mod 4) ---
Nw = 100
z = np.log(U / lp ** 3)
mins = [float(z[i:i + Nw].min()) for i in range(0, len(z) - Nw + 1, Nw)]
med = float(np.median(z))
sig = float(z.std(ddof=1))
pred_min = med - sig * math.sqrt(2 * math.log(Nw))  # crude Gumbel-type scale for the minimum
res["Z0883"] = dict(window=Nw, n_windows=len(mins), median_logUnorm=round(med, 4), sd=round(sig, 4),
                    mean_window_min=round(float(np.mean(mins)), 4), gumbel_crude_pred=round(pred_min, 4),
                    global_min_logUnorm=round(float(z.min()), 4), global_argmin_p=int(P[z.argmin()]))

# --- Z2604: Sarnak-style disjointness of the low-U indicator and mu((p-1)/4) ---
def mu(n):
    return int(mobius(n))
mus = np.array([mu((p - 1) // 4) for p in primes], float)
q = float(np.quantile(z, 0.1))
ind = (z <= q).astype(float)
ind_c = ind - ind.mean()
corr = float(np.dot(ind_c, mus - mus.mean()) / (np.linalg.norm(ind_c) * np.linalg.norm(mus - mus.mean())))
rng = random.Random(1)
null = []
for _ in range(2000):
    perm = mus.copy()
    rng.shuffle(perm)
    pc = perm - perm.mean()
    null.append(float(np.dot(ind_c, pc) / (np.linalg.norm(ind_c) * np.linalg.norm(pc))))
null = np.array(null)
res["Z2604"] = dict(n=len(primes), corr_lowU_mu=round(corr, 5), null_sd=round(float(null.std()), 5),
                    z_score=round(corr / float(null.std()), 3), mean_mu=round(float(mus.mean()), 4))

# --- Z0333: random thinning ---
spec = importlib.util.spec_from_file_location("enum", "scripts/z52b_p1_U08_enum.py")
en = importlib.util.module_from_spec(spec); spec.loader.exec_module(en)
ps = [p for p in primerange(1000, 3001) if p % 4 == 1]
rng = random.Random(7)
th = {}
sols_by_p = {p: en.reps(4, p) for p in ps}
for rho in [0.5, 0.3, 0.2]:
    fails, preds = [], []
    for p in ps:
        sols = sols_by_p[p]
        T = 400
        f = 0
        for _ in range(T):
            kept = {}
            ok = False
            for (x, yy, zz) in sols:
                good = True
                for d in (x, yy, zz):
                    if d not in kept:
                        kept[d] = rng.random() < rho
                    if not kept[d]:
                        good = False
                        break
                if good:
                    ok = True
                    break
            f += (not ok)
        fails.append(f / T)
        preds.append(math.exp(-(rho ** 3) * len(sols)))
    th[rho] = dict(mean_fail_obs=round(float(np.mean(fails)), 4), mean_poisson_pred=round(float(np.mean(preds)), 4),
                   n_primes=len(ps))
res["Z0333"] = th
json.dump(res, open(os.path.join(OUT, "stats.json"), "w"), indent=1)
print(json.dumps(res, indent=1))
