"""O153 W2: does ES-hardness (f_II(p)/log^3 p) track the small-prime profile of chi_p (i.e. L(1,chi_p))?
Input: lines "p f_II(p)" for primes p = 1 (mod 24) (from scripts/review_r128b_count.c with the dump option).
Usage: PYTHONPATH=scripts uv run python scripts/bs_wild_hardness.py /tmp/o153_fII.txt PMIN
"""
import sys
import numpy as np
from sympy import primerange

def main():
    fn = sys.argv[1]; pmin = int(sys.argv[2])
    data = np.loadtxt(fn, dtype=np.int64)
    data = data[data[:, 0] >= pmin]
    P = data[:, 0]; F = data[:, 1].astype(float)
    r = F / np.log(P.astype(float)) ** 3
    lr = np.log(r)
    print(f"n={len(P)} primes p=1(24) in [{pmin},{P.max()}]; mean r={r.mean():.4f} min r={r.min():.4f}")
    qs = list(primerange(2, 3001))
    chi = np.empty((len(qs), len(P)), dtype=np.int8)
    for i, q in enumerate(qs):
        if q == 2:
            chi[i] = 1  # p = 1 (mod 8)
        else:
            chi[i] = np.where(np.array([pow(int(x % q), (q - 1) // 2, q) for x in P]) == 1, 1, -1)
    qa = np.array(qs, dtype=float)
    for y in (10, 50, 300, 3000):
        sel = qa <= y
        logL = -(np.log1p(-chi[sel] / qa[sel, None])).sum(axis=0)
        c = np.corrcoef(logL, lr)[0, 1]
        slope, icpt = np.polyfit(logL, lr, 1)
        resid = lr - (slope * logL + icpt)
        print(f"y={y:5d}: corr(log L_y, log r)={c:+.3f}  slope kappa={slope:+.3f}  R^2={c*c:.3f}  resid sd={resid.std():.3f} (raw sd {lr.std():.3f})")
    # binned view at y=300
    sel = qa <= 300
    logL = -(np.log1p(-chi[sel] / qa[sel, None])).sum(axis=0)
    qsb = np.quantile(logL, np.linspace(0, 1, 11))
    print("deciles of log L_300 -> mean r, min r, count")
    for k in range(10):
        m = (logL >= qsb[k]) & (logL <= qsb[k + 1])
        print(f"  [{qsb[k]:+.2f},{qsb[k+1]:+.2f}]  mean r={r[m].mean():.4f}  min r={r[m].min():.4f}  n={m.sum()}")
    # hardest primes
    idx = np.argsort(r)[:8]
    print("hardest:", [(int(P[i]), int(F[i]), round(float(r[i]), 4), round(float(logL[i]), 2)) for i in idx])
    # least nonresidue
    first_neg = np.argmax(chi[1:] == -1, axis=0) + 1
    npq = qa[first_neg]
    for t in sorted(set(npq.tolist()))[:8]:
        m = npq == t
        print(f"  least nonresidue prime {int(t):3d}: n={m.sum():6d} mean r={r[m].mean():.4f} min r={r[m].min():.4f}")

if __name__ == "__main__":
    main()


def congruence_fit(fn, pmin, mods):
    """R^2 of an additive model log r ~ sum_q onehot(p mod q): the congruence-explained share of log-variance.
    Fit on even-indexed primes, evaluate on odd-indexed (out of sample)."""
    data = np.loadtxt(fn, dtype=np.int64)
    data = data[data[:, 0] >= pmin]
    P = data[:, 0]; lr = np.log(data[:, 1] / np.log(P.astype(float)) ** 3)
    cols = [np.ones(len(P))]
    for q in mods:
        res = P % q
        for a in range(q):
            m = (res == a)
            if m.any():
                cols.append(m.astype(float))
    A = np.stack(cols, axis=1)
    tr = np.arange(len(P)) % 2 == 0
    coef, *_ = np.linalg.lstsq(A[tr], lr[tr], rcond=None)
    pred = A[~tr] @ coef
    r2 = 1 - ((lr[~tr] - pred) ** 2).mean() / lr[~tr].var()
    print(f"mods={mods}: out-of-sample R^2={r2:.3f}, resid sd={np.sqrt(((lr[~tr]-pred)**2).mean()):.3f}")
