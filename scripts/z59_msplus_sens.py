# z59 MSPLUS: sensitivity of the zero law to the log10 n term: refit model B with beta fixed to 0 on [1e6, 1e9]
# and predict the next decades by group (same Monte-Carlo as z59_msplus_zerofit.py).
# Usage: uv run --with numpy --with scipy --with sympy python z59_msplus_sens.py H_FILE COEF_FILE NSAMP
import sys, math
import numpy as np
from scipy.optimize import minimize
sys.path.insert(0, 'scripts')
import z59_msplus_zerofit as Z
rows = Z.load(sys.argv[1])
coef = {}
for line in open(sys.argv[2]):
    a, l, c1, c0 = line.split(); coef[int(a)] = (float(l), float(c1), float(c0))
cnt = np.array([r[3] for r in rows]); y = np.array([r[4] for r in rows])
m = np.array([r[6] for r in rows]); lg = np.array([(r[2] + 0.5) / 4 for r in rows]); kb = np.array([r[7] for r in rows])
X = Z.design(m, lg, kb, True)
free = [i for i in range(X.shape[1]) if i != 2]
def full(t):
    th = np.zeros(X.shape[1]); th[free] = t; return th
def nll(t):
    eta = X @ full(t); return (cnt * np.exp(eta) - y * eta).sum()
t0 = np.zeros(len(free)); t0[0] = math.log(y.sum() / cnt.sum())
res = minimize(nll, t0, method='BFGS')
th = full(res.x)
print("model B with beta=0:", ' '.join(f"{v:.3f}" for v in th), " nll diff vs free fit: see zerofit")
for lo, hi in [(10**9, 10**10), (10**10, 10**11), (10**11, 10**12), (10**12, 10**13), (10**13, 10**15)]:
    pr = Z.predict(th, coef, lo, hi, int(sys.argv[3]), withk=True)
    s = '  '.join(f"{k[0]}{k[1]}={v:.3g}" for k, v in sorted(pr.items()))
    print(f"  [{lo:.0e},{hi:.0e}] total={sum(pr.values()):.3g}: {s}")
