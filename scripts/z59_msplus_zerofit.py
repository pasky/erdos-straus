# z59 MSPLUS: fit a zero law  P(R(n) = 0) = exp(alpha + kappa*m(n) + beta*log10 n)  (Poisson GLM on the binned census
# from scripts/z59_msplus_strat2.c, non-squares only, n >= 10^6), report per-group goodness of fit, and predict the
# expected number of zeros per group in later ranges by Monte-Carlo over n (same m(n) as strat2.c, QMAX = 2000).
#   Model A: covariates (1, m, log10 n).  Model B: + dummies for kb = bucket of k(n) (least odd prime l with (n/l) = -1,
#   l !| n; kb 1:5 2:7 3:11 4:13 5:17-23 6:29-47 7:>47/none, base kb = 1).  Cells with k(n) = 3 are excluded: n = 2 (3)
#   gives the hit d = 3 (R >= 1, PROVED).
# Usage: uv run --with numpy --with scipy --with sympy python z59_msplus_zerofit.py H_FILE COEF_FILE [NSAMP]
import sys, math, random
import numpy as np
from scipy.optimize import minimize
from sympy import isprime, primerange

def load(fn, bmin=24, bmax=99):
    rows = []
    for line in open(fn):
        t = line.split()
        if t[0] != 'H' or t[1] == 'S': continue
        cat, g, b, mb, kb = t[1], int(t[2]), int(t[3]), int(t[4]), int(t[5])
        cnt, z, r2, sR, sm = map(float, t[6:11])
        if b < bmin or b > bmax or kb == 0: continue
        rows.append((cat, g, b, cnt, z, r2, sm / cnt, kb))
    return rows

def design(m, lg, kb, withk):
    cols = [np.ones_like(m), m, lg]
    if withk:
        for j in range(2, 8): cols.append((kb == j).astype(float))
    return np.stack(cols, 1)

def fit(rows, col=4, withk=False):
    cnt = np.array([r[3] for r in rows]); y = np.array([r[col] for r in rows])
    m = np.array([r[6] for r in rows]); lg = np.array([(r[2] + 0.5) / 4 for r in rows])
    kb = np.array([r[7] for r in rows])
    X = design(m, lg, kb, withk)
    def nll(th):
        eta = X @ th; mu = cnt * np.exp(eta)
        return (mu - y * eta).sum()
    def grad(th):
        eta = X @ th; mu = cnt * np.exp(eta)
        return X.T @ (mu - y)
    th0 = np.zeros(X.shape[1]); th0[0] = math.log(max(y.sum(), 1) / cnt.sum())
    res = minimize(nll, th0, jac=grad, method='BFGS')
    H = (X * (cnt * np.exp(X @ res.x))[:, None]).T @ X
    se = np.sqrt(np.diag(np.linalg.inv(H)))
    return res.x, se, X, cnt, y

GN = {0: 'M', 1: 'unit', 3: 'g3', 5: 'g5', 7: 'g7', 15: 'g15', 21: 'g21', 35: 'g35', 105: 'g105'}
MSET = {1, 121, 169, 289, 361, 529}
PRIMES = list(primerange(11, 2001))
FAC = {q: (q * q - q + 1) / (q * q + 1) for q in PRIMES}

def mval(n, coef):
    a = n % 840; lead, c1, c0 = coef[a]
    K = 1.0
    for q in PRIMES:
        if n % q == 0: K *= FAC[q]
    L = math.log(n / 4)
    return lead * K * L * L + c1 * L + c0

def grp(n):
    if n % 840 in MSET: return 0
    return math.gcd(n, 105)

KP = [3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
def kbucket(n):
    for l in KP:
        if n % l and pow(n % l, (l - 1) // 2, l) == l - 1:
            return {3: 0, 5: 1, 7: 2, 11: 3, 13: 4}.get(l, 5 if l <= 23 else 6)
    return 7

def predict(th, coef, lo, hi, nsamp, seed=1, withk=False):
    rnd = random.Random(seed)
    tot = (hi - lo) // 4
    acc = {}
    for _ in range(nsamp):
        n = lo + 4 * rnd.randrange(tot); n -= (n - 1) % 4
        r = math.isqrt(n)
        if r * r == n: continue
        cat = 'P' if isprime(n) else 'C'
        kb = kbucket(n)
        if kb == 0: continue
        x = design(np.array([mval(n, coef)]), np.array([math.log10(n)]), np.array([kb]), withk)[0]
        p0 = math.exp(x @ th)
        k = (cat, GN[grp(n)])
        acc[k] = acc.get(k, 0.0) + p0
    return {k: v * tot / nsamp for k, v in acc.items()}

if __name__ == '__main__':
    rows = load(sys.argv[1])
    coef = {}
    for line in open(sys.argv[2]):
        a, l, c1, c0 = line.split(); coef[int(a)] = (float(l), float(c1), float(c0))
    nsamp = int(sys.argv[3]) if len(sys.argv) > 3 else 200000
    THS = {}
    for col, name, withk in [(4, 'R=0', False), (4, 'R=0', True), (5, 'R=2', True)]:
        th, se, X, cnt, y = fit(rows, col, withk)
        print(f"fit {name} model {'B' if withk else 'A'}: " + ' '.join(f"{t:.3f}±{e:.3f}" for t, e in zip(th, se)) +
              f"  total obs={y.sum():.0f}  (coefs: alpha, kappa(m), beta(log10 n), [kb=2..7 dummies])")
        pred = cnt * np.exp(X @ th)
        bygrp = {}
        for r, p in zip(rows, pred):
            k = (r[0], GN[r[1]], r[2] // 4)
            G = bygrp.setdefault(k, [0, 0]); G[0] += r[col]; G[1] += p
        for k in sorted(bygrp):
            o, p = bygrp[k]
            if o > 0 or p > 0.5: print(f"   {k[0]} {k[1]:5s} dec{k[2]}  obs={o:5.0f}  pred={p:8.2f}")
        if col == 4: THS[withk] = th
    for withk in (False, True):
        print(f"out-of-sample / extrapolated expected zeros (R=0 law, model {'B' if withk else 'A'}):")
        for lo, hi in [(10**9, 10**10), (10**10, 10**11), (10**11, 10**12), (10**12, 10**13), (10**13, 10**15)]:
            pr = predict(THS[withk], coef, lo, hi, nsamp, withk=withk)
            s = '  '.join(f"{k[0]}{k[1]}={v:.3g}" for k, v in sorted(pr.items()))
            print(f"  [{lo:.0e},{hi:.0e}] total={sum(pr.values()):.3g}: {s}")
