"""R38b from-scratch library: exact Efron-Stein level weights for event systems
on arbitrary finite product probability spaces (no reuse of author code)."""
import numpy as np


def grid(dims):
    """list of coordinate arrays (broadcastable) for product space with given alphabet sizes."""
    return np.meshgrid(*[np.arange(q) for q in dims], indexing="ij")


def bad_indicator(dims, events):
    """events: list of dicts {var: value}. Returns h = 1[some event holds] as float array."""
    X = grid(dims)
    h = np.zeros(dims, dtype=bool)
    for ev in events:
        m = np.ones(dims, dtype=bool)
        for v, c in ev.items():
            m &= X[v] == c
        h |= m
    return h.astype(float)


def level_weights(F, probs):
    """F: array over prod space; probs: list of prob vectors per axis.
    Returns w[d] = sum_{|U|=d} ||F^{=U}||^2 under the product measure."""
    n = F.ndim
    A = np.zeros((n + 1,) + F.shape)
    A[0] = F
    for v in range(n):
        p = probs[v]
        shp = [1] * (n + 1)
        shp[v + 1] = len(p)
        M = (A * p.reshape(shp)).sum(axis=v + 1, keepdims=True)
        D = A - M
        B = np.zeros_like(A)
        B += np.broadcast_to(M, A.shape)
        B[1:] += D[:-1]
        A = B
    # measure weights
    W = np.ones(F.shape)
    for v in range(n):
        shp = [1] * n
        shp[v] = len(probs[v])
        W = W * probs[v].reshape(shp)
    return np.array([(A[d] ** 2 * W).sum() for d in range(n + 1)])


def G_weighted(F, probs, lam):
    """G_F(lambda) = <F, prod_v (I+(lam_v-1)L_v) F> under product measure."""
    n = F.ndim
    A = F.copy()
    for v in range(n):
        p = probs[v]
        shp = [1] * n
        shp[v] = len(p)
        M = (A * p.reshape(shp)).sum(axis=v, keepdims=True)
        A = A + (lam[v] - 1.0) * (A - M)
    W = np.ones(F.shape)
    for v in range(n):
        shp = [1] * n
        shp[v] = len(probs[v])
        W = W * probs[v].reshape(shp)
    return float((F * A * W).sum())


def tail_ratio(lw, k):
    """max_t energy(t) * 2^{(t+1)/k}, energy(t)=sum_{d>t} lw[d], t>=0. Cor 4.1 claims <=1."""
    n = len(lw) - 1
    best, arg = 0.0, None
    for t in range(0, n):
        e = lw[t + 1:].sum()
        r = e * 2 ** ((t + 1) / k)
        if r > best:
            best, arg = r, t
    return best, arg
