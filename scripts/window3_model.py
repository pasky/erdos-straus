#!/usr/bin/env python3
"""POINTWISE_WINDOW3 §2 -- discrete two-window model with cell-integrated true law.

Bins: K log-spaced cells [e_k, e_{k+1}] of [eps, 1].  A window configuration is a
multiplicity vector m (|m| even).  mu(m) = exact integral over the cell of the
continuum law  prod dt_i/(2 t_i) / m! * (1 - sum t)^(-1/2) * 1[sum t < 1],
computed on a uniform sub-grid of step 1/N (sum distribution by convolution;
cofactor weight integrated exactly per sub-cell).  mu(empty) = 1.
Visible one-window S (any parity): convention
  rep   : sum of geometric centres <= theta
  inner : max cell sum (upper edges) <= theta    (less information than reality)
  outer : min cell sum (lower edges) <  theta    (more information)
Joint visibility uses the same convention on (S3, S7) together.
"""
import itertools
from math import comb, factorial, log, exp
import numpy as np


def edges(eps, K):
    return np.exp(np.linspace(log(eps), 0.0, K + 1))


def window_configs(e, parity=0):
    """multiplicity vectors with min cell sum < 1 and |m| = parity mod 2."""
    K = len(e) - 1
    lo = e[:-1]
    out = []

    def rec(k, cur, s):
        if k == K:
            if sum(cur) % 2 == parity:
                out.append(tuple(cur))
            return
        m = 0
        while s + m * lo[k] < 1 - 1e-12:
            cur.append(m); rec(k + 1, cur, s + m * lo[k]); cur.pop(); m += 1
    rec(0, [], 0.0)
    return out


class Law:
    def __init__(self, eps, K, N=4000):
        self.e = e = edges(eps, K)
        self.K, self.N = K, N
        h = 1.0 / N
        self.h = h
        # single-point pdf (prob mass on sub-grid) for each bin; density prop. to 1/t
        self.w = 0.5 * np.log(e[1:] / e[:-1])
        grid = np.arange(N + 1) * h
        self.single = []
        for k in range(K):
            a, b = e[k], e[k + 1]
            # mass of [g_j - h/2, g_j + h/2] ∩ [a,b] under dt/t, normalised
            lo = np.clip(grid - h / 2, a, b); hi = np.clip(grid + h / 2, a, b)
            p = np.log(hi / lo); p /= p.sum()
            self.single.append(p)
        self.pow = {}
        # cofactor weight averaged over a sub-cell of the sum: sum at grid j is spread on [j h - h/2, j h + h/2]
        jj = np.arange(N + 1) * h
        a = np.clip(jj - h / 2, 0, 1); b = np.clip(jj + h / 2, 0, 1)
        self.cof = np.where(b > a, 2 * (np.sqrt(1 - a) - np.sqrt(1 - b)) / np.maximum(b - a, 1e-300), 0.0)
        self.cof[0] = 1.0  # empty sum: weight exactly 1
        self.cofw = self.cof * np.where(b > a, (b - a) / h, 0.0)  # fraction of sub-cell below 1
        self.cofw[0] = 1.0

    def sumdist(self, k, m):
        key = (k, m)
        if key not in self.pow:
            if m == 0:
                v = np.zeros(self.N + 1); v[0] = 1
            else:
                v = np.convolve(self.sumdist(k, m - 1), self.single[k])[: self.N + 1]
            self.pow[key] = v
        return self.pow[key]

    def mu(self, m):
        d = np.zeros(self.N + 1); d[0] = 1
        coef = 1.0
        for k, mk in enumerate(m):
            if mk:
                d = np.convolve(d, self.sumdist(k, mk))[: self.N + 1]
                coef *= self.w[k] ** mk / factorial(mk)
        return coef * float(d @ self.cofw)


def visible_one(e, theta, conv):
    K = len(e) - 1
    g = np.sqrt(e[:-1] * e[1:])
    val = {"rep": g, "inner": e[1:], "outer": e[:-1]}[conv]
    out = []

    def rec(k, cur, s):
        if k == K:
            out.append(tuple(cur)); return
        m = 0
        while (s + m * val[k] <= theta + 1e-12) if conv != "outer" else (s + m * val[k] < theta - 1e-12):
            cur.append(m); rec(k + 1, cur, s + m * val[k]); cur.pop(); m += 1
    rec(0, [], 0.0)
    sums = {S: float(np.dot(S, val)) for S in out}
    return out, sums


def emb(S, C):
    v = 1
    for s, c in zip(S, C):
        if s > c:
            return 0
        v *= comb(c, s)
    return v
