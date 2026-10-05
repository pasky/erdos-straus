"""OMEGA10 Conjecture Q hill-climb: maximise Q = sum_V mu^V tauhat(V)^2 over hypergraphs and
weights normalised so max_E prod_{v in E}(1+mu_v) = 2.  Usage: omega10_qhc.py seed trials n"""
import sys, numpy as np
seed, trials, n = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])
rng = np.random.default_rng(seed)
N = 1 << n; R = np.arange(N)
bits = ((R[:, None] >> np.arange(n)) & 1).astype(float)
def tauhat(edges):
    tau = np.ones(N)
    for e in edges:
        m = sum(1 << v for v in e); tau *= ((R & m) != 0)
    t = tau.copy()
    for i in range(n):
        b = 1 << i; idx = R[(R & b) != 0]; t[idx] -= t[idx ^ b]
    return t
def Q(edges, a):
    s = max(sum(a[v] for v in e) for e in edges)
    if s <= 0: return 0.0
    mu = 2 ** (a / s) - 1
    with np.errstate(divide="ignore"):
        lmu = np.log(mu)
    lw = bits @ np.where(mu > 0, lmu, -1e9)
    t = tauhat(edges)
    return float(np.sum(np.exp(lw) * t * t))
def redge(kmax):
    r = int(rng.integers(1, kmax + 1)); return tuple(sorted(rng.choice(n, r, replace=False).tolist()))
worst = 0
for tr in range(trials):
    kmax = int(rng.integers(1, n + 1))
    edges = [redge(kmax) for _ in range(int(rng.integers(1, 2 * n)))]
    a = rng.random(n); best = Q(edges, a)
    for s in range(150):
        ne, na = list(edges), a.copy(); r = rng.random()
        if r < 0.25: ne.append(redge(kmax))
        elif r < 0.4 and len(ne) > 1: ne.pop(rng.integers(len(ne)))
        elif r < 0.55: ne[rng.integers(len(ne))] = redge(kmax)
        else: na[rng.integers(n)] = rng.random() * rng.choice([0, 1, 1, 3])
        v = Q(ne, na)
        if v >= best: edges, a, best = ne, na, v
    if best > worst:
        worst = best; print(f"Q={best:.6f} edges={edges} a={np.round(a,3).tolist()}", flush=True)
