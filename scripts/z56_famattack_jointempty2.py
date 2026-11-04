# Joint emptiness vs conditional independence given richer strata: p mod M x quantile bins of the L-proxies
# (log truncated Euler products for chi_p incl. l=2, and chi_{-4p}; l < 20000). Same design as _jointempty.py.
import sys, numpy as np
sys.path.insert(0, 'scripts')
from z56_famattack_assoc import load
from z56_famattack_lcontrol import logL
rng = np.random.default_rng(56)
for fn in sys.argv[1:]:
    p, R, g = load(fn); N = len(p); Z = (g.reshape(N, 25) == 0)
    L1 = logL(p, 20000); L2 = logL(p, 20000, True)
    rates = Z.mean(0); ok = np.where((rates >= 0.05) & (rates <= 0.95))[0]
    for M, nb in ((840, 1), (120, 3), (840, 3), (24, 5)):
        b1 = np.digitize(L1, np.quantile(L1, np.linspace(0, 1, nb + 1)[1:-1]))
        b2 = np.digitize(L2, np.quantile(L2, np.linspace(0, 1, nb + 1)[1:-1]))
        strata = (p % M) * 100 + b1 * 10 + b2
        us, sidx = np.unique(strata, return_inverse=True)
        cnt = np.bincount(sidx); ws = cnt / N
        Ps = np.zeros((len(us), 25))
        for j in range(25): Ps[:, j] = np.bincount(sidx, weights=Z[:, j]) / cnt
        line = []
        for k in (2, 4, 6, 8):
            O = E = 0.0
            for _ in range(300):
                S = rng.choice(ok, size=k, replace=False)
                O += Z[:, S].all(1).sum(); E += N * (ws * Ps[:, S].prod(1)).sum()
            line.append(f"k={k}: {O/E:.3f}")
        print(f"{fn} strata p mod {M} x {nb}x{nb} L-bins ({len(us)} strata, median size {int(np.median(cnt))}): " + "  ".join(line), flush=True)
