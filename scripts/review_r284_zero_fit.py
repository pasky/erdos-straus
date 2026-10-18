"""R284: refit -log P = A M^beta from the published bin table of logs/z42_zero_law_m8_1e9.txt (bin midpoints),
weights (log P)^2/rel^2 (rel = Poisson(Z) + binomial(f, 40000)), and simple sensitivity variants."""
import numpy as np
lo = np.arange(10, 30, 2); Z = np.array([144083,137776,10660,5928,6320,1780,934,560,395,425])
f = np.array([.08013,.15857,.02385,.03363,.08082,.04238,.04398,.06085,.08575,.20550])
N = 2.49995e8; P = Z/(N*f); rel = np.sqrt(1/Z + (1-f)/(40000*f))
def fit(M, P, rel, mask):
    y = np.log(-np.log(P[mask])); x = np.log(M[mask]); w = (np.log(P[mask])**2)/rel[mask]**2
    A = np.vstack([np.ones_like(x), x]).T * np.sqrt(w)[:, None]
    c, res, *_ = np.linalg.lstsq(A, y*np.sqrt(w), rcond=None)
    chi2 = float(((A@c - y*np.sqrt(w))**2).sum())
    return c[1], np.exp(c[0]), chi2, mask.sum()-2
mid = lo + 1.0
for name, M, mask in [("midpoints [10,30]", mid, np.ones(10, bool)), ("left edges", lo+0.0, np.ones(10, bool)),
                      ("midpoints [16,30]", mid, lo >= 16), ("midpoints [20,30]", mid, lo >= 20), ("midpoints [10,20]", mid, lo < 20)]:
    b, A, chi2, dof = fit(M, P, rel, mask)
    print(f"{name:20s} beta={b:.3f} A={A:.3f} chi2={chi2:.1f}/{dof}")
print("P:", np.array2string(P, precision=3), "\nP/exp(-mid/2):", np.round(P/np.exp(-mid/2), 2))
