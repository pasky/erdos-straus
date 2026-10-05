"""OMEGA10 Conjecture Q1: for a hypergraph H with nonempty edges on n vertices,
Q1(H) := sum_V tauhat(V)^2 <= min_E (2^|E| - 1), tau = transversal indicator.
Random search + hill-climb on ratio Q1/min.  Usage: omega10_q1.py seed trials nmax"""
import sys, numpy as np
seed, trials, nmax = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])
rng = np.random.default_rng(seed)
def Q1(n, edges):
    N = 1 << n; R = np.arange(N); tau = np.ones(N, dtype=np.int64)
    for e in edges:
        m = sum(1 << v for v in e); tau *= ((R & m) != 0)
    t = tau.copy()
    for i in range(n):
        b = 1 << i; idx = R[(R & b) != 0]; t[idx] -= t[idx ^ b]
    return int(np.sum(t * t)), int(np.abs(t).max())
def ratio(n, edges):
    q, mx = Q1(n, edges)
    return q / min(2 ** len(e) - 1 for e in edges), q, mx
def redge(n, kmax):
    r = int(rng.integers(1, kmax + 1)); return tuple(sorted(rng.choice(n, r, replace=False).tolist()))
worst = 0
for tr in range(trials):
    n = int(rng.integers(2, nmax + 1)); kmax = int(rng.integers(1, n + 1))
    edges = [redge(n, kmax) for _ in range(int(rng.integers(1, 2 * n)))]
    best = ratio(n, edges)[0]
    for s in range(60):   # hill climb
        new = list(edges); r = rng.random()
        if r < 0.4: new.append(redge(n, kmax))
        elif r < 0.6 and len(new) > 1: new.pop(rng.integers(len(new)))
        else: new[rng.integers(len(new))] = redge(n, kmax)
        rr = ratio(n, new)[0]
        if rr >= best: edges, best = new, rr
    rr, q, mx = ratio(n, edges)
    if rr > worst:
        worst = rr; print(f"ratio={rr:.4f} Q1={q} max|tauhat|={mx} n={n} edges={edges}", flush=True)
