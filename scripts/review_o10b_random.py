"""R38b: random width-k DNFs on n=14..16 bits (uniform and p-biased), many terms sharing
variables (terms drawn from a small variable pool to force overlap). usage: TRIALS SEED"""
import sys, numpy as np
from review_o10b_lib import bad_indicator, level_weights, tail_ratio
trials, seed = int(sys.argv[1]), int(sys.argv[2])
rng = np.random.default_rng(seed)
mxG = mxT = mxT2 = 0
for tr in range(trials):
    n = int(rng.choice([14, 15, 16])); k = int(rng.integers(1, 7))
    pool = int(rng.integers(k, n + 1))  # overlap control
    m = int(rng.choice([1, 2, 3, 5, 8, 13, 21, 40, 80, 200]))
    ev = []
    for _ in range(m):
        w = k if rng.random() < 0.7 else int(rng.integers(1, k + 1))
        vs = rng.choice(pool, size=w, replace=False)
        ev.append({int(v): int(rng.integers(2)) for v in vs})
    biased = rng.random() < 0.4
    probs = []
    for v in range(n):
        p = rng.uniform(0.02, 0.98) if biased else 0.5
        probs.append(np.array([1 - p, p]))
    lw = level_weights(1 - bad_indicator((2,) * n, ev), probs)
    G = sum(lw[d] * 2 ** (d / k) for d in range(n + 1))
    r, t = tail_ratio(lw, k)
    r2 = max([lw[t + 1:].sum() * 2 ** ((t + 1) / k) for t in range(2 * k - 1, n)] + [0])
    mxG, mxT, mxT2 = max(mxG, G), max(mxT, r), max(mxT2, r2)
print(f"trials={trials}: max G={mxG:.6f}  max tailratio={mxT:.6f}  max tailratio(t>=2k-1)={mxT2:.6f}")
