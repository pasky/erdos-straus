#!/usr/bin/env python3
"""z56 K4CHEN: mixed scheme = weights on N2 (Richert/Kuhn family) + Chen-type switching for the configurations the
weights do not kill.  Assessment-level model (units X G W(z1) W(z2)).

margin = fvec(s1,s2) - T1 - Cost_w - K * Unc(w),   K = L(lamsw) F(1) sqrt(th1)
  Cost_w = (1/2) int_zeta^y w(al) U(theta - al) dal/al      (upper vector sieve for p with q | N2)
  Unc(w) = mass of z2-rough parity-even configurations with j >= r+2 Q-factors and sum_i w(al_i) < 1
           (Monte Carlo over j-1 log-uniform factors, last factor integrated by quadrature; validated vs masses()).
Weights: 'richert': w = lam (1 - al/y)_+ ; 'kuhn': w = lam 1[al < y].
"""
import math, sys, os
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import z55_p415_sieve as P
from z56_k4chen_lp import Uup
from z56_k4chen_switch import Lsw
Fv, fvec, best_upper, B = P.Fv, P.fvec, P.best_upper, P.B
F1 = Fv(1.0)
NT = 48  # quadrature points for the last factor


class Configs:
    """MC sample of configurations for given zeta: for each even j, arrays of factors and quadrature weights."""
    def __init__(self, zeta, jmin, jmax=None, nsamp=200000, seed=1):
        rng = np.random.default_rng(seed)
        jmax = jmax or min(int(1 / zeta), 24)
        self.zeta = zeta; self.data = []
        L = math.log(1 / zeta)
        for j in range(jmin, jmax + 1):
            if j % 2: continue
            al = zeta * np.exp(rng.random((nsamp, j - 1)) * L)     # log-uniform on [zeta,1]
            sig = al.sum(axis=1)
            ok = sig < 1 - zeta
            al = al[ok]; sig = sig[ok]
            T = np.sqrt(1 - sig - zeta)
            # Gauss-Legendre on t in [0,T]
            xg, wg = np.polynomial.legendre.leggauss(NT)
            t = (xg[None, :] + 1) / 2 * T[:, None]
            last = 1 - sig[:, None] - t * t                          # last factor a(t)
            qw = (wg[None, :] / 2 * T[:, None]) * 2 / last           # 2 dt / a
            pref = L ** (j - 1) / (2 ** j * math.factorial(j)) * F1 * math.sqrt(zeta) / nsamp
            self.data.append((j, al, last, qw, pref))

    def mass(self, wfun=None):
        """total mass (wfun None) or uncovered mass: sum_i w(al_i) < 1."""
        tot = 0.0
        for j, al, last, qw, pref in self.data:
            if wfun is None:
                tot += pref * qw.sum(); continue
            s = wfun(al).sum(axis=1)[:, None] + wfun(last)
            tot += pref * (qw * (s < 1)).sum()
        return tot


def wfam(kind, lam, y):
    if kind == 'richert': return lambda a: lam * np.clip(1 - a / y, 0, None)
    return lambda a: lam * (a < y)


def cost_w(kind, lam, y, th1, zeta, theta, n=200):
    tot = 0.0; hi = min(y, theta - 1e-3)
    if hi <= zeta: return 0.0
    # log-spaced midpoint rule
    e = np.linspace(math.log(zeta), math.log(hi), n + 1)
    for i in range(n):
        a = math.exp((e[i] + e[i + 1]) / 2)
        w = lam * (max(0.0, 1 - a / y) if kind == 'richert' else 1.0)
        if w == 0: continue
        tot += 0.5 * w * Uup(theta - a, th1, zeta, n=40) * (e[i + 1] - e[i])
    return tot


def best_main(th1, zeta, theta, ns=60):
    smax = (theta - zeta) / th1; best = -1e9; arg = None
    for i in range(ns + 1):
        s1 = 1 + i * (smax - 1) / ns
        s2 = (theta - s1 * th1) / zeta
        if s2 < 1: continue
        v = fvec(s1, s2)
        if v > best: best, arg = v, (s1, s2)
    return best, arg


def run(r, theta=0.5, lamsw=0.5, pen=1.0, th1s=None, zetas=None, kinds=('richert', 'kuhn'), nsamp=100000):
    th1s = th1s or [0.38, 0.40, 0.42, 0.44]
    zetas = zetas or [0.01, 0.015, 0.02, 0.03, 0.04]
    Ls = Lsw(lamsw)
    best = (-1e9, None)
    for zeta in zetas:
        C = Configs(zeta, r + 2, nsamp=nsamp)
        for th1 in th1s:
            if theta - zeta <= th1: continue
            M, arg = best_main(th1, zeta, theta)
            if arg is None: continue
            T1 = best_upper(zeta, lamsw, th1, pen) * B(th1)
            K = pen * Ls * F1 * math.sqrt(th1)
            if M - T1 <= best[0]: continue
            base = (M - T1 - K * C.mass(), dict(kind='none'))
            loc = base
            for kind in kinds:
                for y in [0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4]:
                    if y <= zeta: continue
                    for lam in [0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.4, 0.5]:
                        cw = cost_w(kind, lam, y, th1, zeta, theta)
                        if M - T1 - cw <= loc[0]: continue
                        unc = C.mass(wfam(kind, lam, y))
                        v = M - T1 - cw - K * unc
                        if v > loc[0]: loc = (v, dict(kind=kind, lam=lam, y=y, cost=round(cw, 4), unc=unc, KU=round(K * unc, 4)))
            v, d = loc
            d.update(th1=th1, zeta=zeta, s1=round(arg[0], 4), s2=round(arg[1], 4), main=round(M, 4), T1=round(T1, 4))
            if v > best[0]: best = (v, d)
            print(f"  r={r} zeta={zeta} th1={th1}: {v:.4f} {d}", flush=True)
    return best


if __name__ == "__main__":
    mode = sys.argv[1]
    if mode == 'validate':
        from z56_k4chen_mass import masses
        for z in (0.01, 0.03):
            m = masses(z, jmax=16, n=2000)
            for k in (4, 6, 8):
                C = Configs(z, k, nsamp=100000)
                print(z, k, 'MC', C.mass(), 'grid', sum(m[j] for j in range(k, len(m)) if j % 2 == 0))
    else:
        r = int(mode); theta = float(sys.argv[2]); lamsw = float(sys.argv[3]); pen = float(sys.argv[4])
        print("BEST", r, theta, lamsw, pen, run(r, theta, lamsw, pen))
