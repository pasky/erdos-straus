"""Z0665 one level beyond z52b_dividing_indep.py: is the strong positive correlation between certificate families
explained by the quadratic-character (sign) pattern of N? Stratify the residue-model sample by the Legendre vector
((N/q))_{q in QS} and compare observed survivors with the within-stratum independent product."""
import numpy as np, sys
from sympy import divisors, primerange, legendre_symbol
X_MAX = int(sys.argv[1]) if len(sys.argv) > 1 else 316
NS = int(sys.argv[2]) if len(sys.argv) > 2 else 200000
QS = [11, 13, 17, 19, 23, 29, 31]
rng = np.random.default_rng(2)
N = 840 * rng.integers(2**50, 2**51, size=NS * 3, dtype=np.int64) + rng.choice([1, 121, 169, 289, 361, 529], size=NS * 3)
for q in primerange(11, 200):
    N = N[N % q != 0]
N = N[:NS]
key = np.zeros(len(N), dtype=np.int64)
for i, q in enumerate(QS):
    qr = np.zeros(q, dtype=bool); qr[[(x * x) % q for x in range(1, q)]] = True
    key |= (~qr[N % q]).astype(np.int64) << i       # bit set = non-residue
fams = []
for a in range(1, X_MAX + 1):
    for d in range(1, X_MAX // a + 1):
        fams.append((a * d, 4 * a * d, {(-f) % (4 * a * d) for f in divisors(4 * a * a * d + 1)}))
for a in range(1, X_MAX + 1):
    for b in range(a, X_MAX // a + 1):
        fams.append((a * b, 4 * a * b, {(-e) % (4 * a * b) for e in divisors(a + b)}))
fams.sort(key=lambda t: (t[0], t[1]))
strata = np.unique(key)
idx = {k: np.where(key == k)[0] for k in strata}
alive = np.ones(len(N), dtype=bool)
logp_glob = 0.0
logp = {k: 0.0 for k in strata}
for s, m, res in fams:
    tab = np.zeros(m, dtype=bool); tab[list(res)] = True
    hit = tab[N % m]
    r = hit.mean(); logp_glob += np.log1p(-r) if r < 1 else -np.inf
    for k in strata:
        rk = hit[idx[k]].mean()
        logp[k] += np.log1p(-rk) if rk < 1 else -np.inf
    alive &= ~hit
obs = alive.mean()
pred_strat = sum(len(idx[k]) * np.exp(logp[k]) for k in strata) / len(N)
print(f"X={X_MAX} NS={len(N)} strata={len(strata)} (Legendre vector at {QS})")
print(f"observed survivors {obs:.3e}; global-independent {np.exp(logp_glob):.3e} (ratio {obs/np.exp(logp_glob):.1f}); "
      f"stratified-independent {pred_strat:.3e} (ratio {obs/pred_strat:.2f})")
# per-number-of-nonresidues summary
nb = np.array([bin(k).count('1') for k in key])
for j in range(len(QS) + 1):
    sel = nb == j
    if sel.sum() == 0: continue
    pk = sum(len(idx[k]) * np.exp(logp[k]) for k in strata if bin(k).count('1') == j) / sel.sum()
    print(f"  #QNR among QS = {j}: n={sel.sum():6d} observed={alive[sel].mean():.3e} strat-indep={pk:.3e}")
