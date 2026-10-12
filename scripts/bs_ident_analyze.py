"""O145 (a): do non-congruence invariants predict ES lottery counts on Mordell-hard primes?
Input: TSV from bs_ident_features (cols p n_p h logeps q2 c2 c3 eII eI SII SI).
Regress y = log(1+SII+SI) (and eII, eI) on a congruence baseline
(log p, indicators of p mod small primes 11..43 being QR, n_p bucket)
and report the extra explained variance / t-stat of each non-congruence invariant:
  hn = h(-4p)/sqrt(p), rn = log(eps)/sqrt(p), q2, c2, c3.
Also a permutation null (shuffle the invariant within the n_p bucket) for the t-stats."""
import sys, numpy as np
D = np.loadtxt(sys.argv[1], dtype=float)
p, np_, h, le, q2, c2, c3, eII, eI, SII, SI = D.T
rng = np.random.default_rng(1)
import sympy
QMAX = int(sys.argv[2]) if len(sys.argv) > 2 else 43
smallq = list(sympy.primerange(11, QMAX + 1))
def qr(a, q): return pow(int(a), (q - 1) // 2, q) == 1
X0 = [np.ones_like(p), np.log(p)]
for q in smallq:
    X0.append(np.array([1.0 if qr(x % q, q) else 0.0 for x in p]))
X0 = np.array(X0).T
inv = {"h/sqrtp": h / np.sqrt(p), "logeps/sqrtp": le / np.sqrt(p),
       "q2(2 quartic)": q2, "c2(2 cubic)": c2, "c3(3 cubic)": c3}
targets = {"log(1+S)": np.log1p(SII + SI), "log eII_min": np.log(np.where(eII > 0, eII, 400)),
           "log eI_min": np.log(np.where(eI > 0, eI, 400))}
def fit(X, y):
    b, *_ = np.linalg.lstsq(X, y, rcond=None); r = y - X @ b; return b, r
print(f"n={len(p)} primes, p<= {int(p.max())}")
for tn, y in targets.items():
    _, r0 = fit(X0, y)
    R2 = 1 - r0.var() / y.var()
    print(f"\n[{tn}] baseline (log p + QR-pattern mod 11..{QMAX}) R^2 = {R2:.3f}")
    for name, z in inv.items():
        m = z >= 0
        X = np.column_stack([X0[m], z[m]]); b, r = fit(X, y[m])
        s2 = r.var() * len(r) / (len(r) - X.shape[1])
        cov = s2 * np.linalg.inv(X.T @ X); t = b[-1] / np.sqrt(cov[-1, -1])
        # permutation null
        ts = []
        for _ in range(200):
            zz = rng.permutation(z[m]); Xp = np.column_stack([X0[m], zz]); bp, rp = fit(Xp, y[m])
            s2p = rp.var() * len(rp) / (len(rp) - Xp.shape[1]); covp = s2p * np.linalg.inv(Xp.T @ Xp)
            ts.append(bp[-1] / np.sqrt(covp[-1, -1]))
        ts = np.abs(ts); pv = (1 + (ts >= abs(t)).sum()) / (1 + len(ts))
        print(f"  {name:14s} n={m.sum():5d} t={t:+.2f}  perm-p={pv:.3f}")
