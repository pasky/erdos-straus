"""OMEGA10: q=2 adversarial search for C-min / C-1 with Walsh-Hadamard.
ratio = sum_S lam^|S| hhat(S)^2 / (lam^k E h)  (h = OR of width<=k terms).
Usage: omega10_bool.py n k steps seed [lamexp]"""
import sys, numpy as np
n, k, steps, seed = map(int, sys.argv[1:5])
lamexp = float(sys.argv[5]) if len(sys.argv) > 5 else 1.0   # lam^k = 2^lamexp
lam = 2 ** (lamexp / k)
rng = np.random.default_rng(seed)
N = 1 << n
pc = np.array([bin(i).count("1") for i in range(N)])
X = (np.arange(N)[:, None] >> np.arange(n)) & 1
def wht(a):
    a = a.copy(); hh = 1
    while hh < N:
        a = a.reshape(-1, 2, hh); a = np.stack([a[:, 0] + a[:, 1], a[:, 0] - a[:, 1]], 1).reshape(N); hh *= 2
    return a / N
def hfun(terms):
    h = np.zeros(N, bool)
    for T in terms:
        m = np.ones(N, bool)
        for c, v in T: m &= X[:, c] == v
        h |= m
    return h.astype(float)
def score(terms):
    h = hfun(terms); Eh = h.mean()
    if Eh == 0: return 0.0, 0.0
    c = wht(h); G = (lam ** pc * c * c).sum()
    GF = 1 - 2 * Eh + G
    wmin = np.full(N, np.inf)
    for T in terms:
        m = np.ones(N, bool)
        for cc, v in T: m &= X[:, cc] == v
        wmin = np.where(m, np.minimum(wmin, lam ** len(T)), wmin)
    return G / (h * np.where(h > 0, wmin, 0)).mean(), GF
def rterm():
    r = rng.integers(1, k + 1); cs = rng.choice(n, r, replace=False)
    return tuple((int(c), int(rng.integers(2))) for c in cs)
terms = [rterm() for _ in range(4)]
best, gf = score(terms); bestGF = gf
for s in range(steps):
    new = list(terms); r = rng.random()
    if r < 0.4 or not new: new.append(rterm())
    elif r < 0.6 and len(new) > 1: new.pop(rng.integers(len(new)))
    else: new[rng.integers(len(new))] = rterm()
    sc, gf = score(new); bestGF = max(bestGF, gf)
    if sc >= best or rng.random() < 0.01:
        terms, best = new, sc
print(f"n={n} k={k} lam^k=2^{lamexp}: best Cmin ratio={best:.5f} maxG_F seen={bestGF:.5f} terms={len(terms)}")
