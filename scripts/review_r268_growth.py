"""R268: growth of the mean b = 1 count (number of (a, c, d)) over primes p = 1 (4) at several scales; compare with log^2 p."""
import random, math
import numpy as np
from sympy import isprime


def b1_count(p):
    t = np.arange(1, (p + 1) // 3 + 1, dtype=np.int64)
    g = (-p) % (4 * t)
    return int(((t + 1) % g == 0).sum())

random.seed(1)
for e in range(3, 9):
    ps = []
    while len(ps) < (300 if e < 8 else 80):
        p = random.randrange(10**e, 2 * 10**e) | 1
        if p % 4 == 1 and isprime(p): ps.append(p)
    v = np.array([b1_count(p) for p in ps]); L = math.log(1.5 * 10**e)
    print(f"p ~ 1.5e{e}: n={len(v)} mean {v.mean():.2f} (SE {v.std(ddof=1)/math.sqrt(len(v)):.2f}); mean/log p {v.mean()/L:.3f}; mean/log^2 p {v.mean()/L**2:.4f}", flush=True)
