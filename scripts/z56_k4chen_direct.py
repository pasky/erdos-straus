#!/usr/bin/env python3
"""z56 K4CHEN: bad N2-configurations (>= k = r+2 Q-factors >= z2) covered by
  (D) a DIRECT upper sieve when the k-1 smallest factors have product Q <= x^tau:  count p with Q | N2 (p in a class
      mod Q), N1 z1-rough, N2/Q z2-rough; N2/Q then has odd Q-parity, so >= 1 further factor is automatic.
      Cost D(tau) = (1/((k-1)! 2^(k-1))) int_{al_i>=zeta, sum<=tau} prod dal_i/al_i  U(theta - sum al)
  (S) Chen-type SWITCHING for the rest (k-1 smallest have sum > tau): cost K * Unc(tau), K = pen L(lamsw) F(1) sqrt(th1).
margin = fvec - T1 - D - K*Unc.  Assessment-level model; units X G W(z1) W(z2).
Usage: python z56_k4chen_direct.py r theta lamsw pen"""
import math, sys, os
import numpy as np
from scipy.optimize import minimize
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import z55_p415_sieve as P
from z56_k4chen_lp import Uup
from z56_k4chen_switch import Lsw
Fv, fvec, B = P.Fv, P.fvec, P.B
F1 = Fv(1.0)
NT = 40
NS = int(os.environ.get('K4NS', '60000'))


class Model:
    def __init__(self, r, zeta, th1, theta, seed=1):
        self.k = k = r + 2; self.zeta = zeta; self.th1 = th1; self.theta = theta
        rng = np.random.default_rng(seed); L = math.log(1 / zeta)
        # direct part: (k-1)-tuples
        al = zeta * np.exp(rng.random((NS, k - 1)) * L)
        self.Dsum = al.sum(axis=1); self.Dpref = L ** (k - 1) / (math.factorial(k - 1) * 2 ** (k - 1)) / NS
        lg = np.linspace(1e-4, theta, 400)
        self.Ugrid = (lg, np.array([Uup(l, th1, zeta, n=60) for l in lg]))
        # switched part: j-configs, j >= k even
        xg, wg = np.polynomial.legendre.leggauss(NT)
        self.sw = []
        for j in range(k, min(int(1 / zeta), 26) + 1):
            if j % 2: continue
            a = zeta * np.exp(rng.random((NS, j - 1)) * L)
            sig = a.sum(axis=1); ok = sig < 1 - zeta; a = np.sort(a[ok], axis=1); sig = sig[ok]
            T = np.sqrt(1 - sig - zeta)
            t = (xg[None, :] + 1) / 2 * T[:, None]
            last = 1 - sig[:, None] - t * t
            qw = (wg[None, :] / 2 * T[:, None]) * 2 / last
            cs = np.concatenate([np.zeros((len(a), 1)), np.cumsum(a, axis=1)], axis=1)
            Skm1 = cs[:, k - 1] if j - 1 >= k - 1 else np.full(len(a), np.inf)
            Skm2 = cs[:, k - 2]
            small = np.minimum(Skm1[:, None], Skm2[:, None] + last)   # sum of k-1 smallest of all j factors
            pref = L ** (j - 1) / (2 ** j * math.factorial(j)) * F1 * math.sqrt(zeta) / NS
            self.sw.append((small, qw, pref))

    def U(self, lam):
        lg, ug = self.Ugrid
        return np.where(lam > lg[0], np.interp(lam, lg, ug), np.inf)

    def D(self, tau):
        m = self.Dsum <= tau
        if not m.any(): return 0.0
        return float(self.Dpref * self.U(self.theta - self.Dsum[m]).sum())

    def Unc(self, tau):
        return float(sum(pref * (qw * (small > tau)).sum() for small, qw, pref in self.sw))


def best_main(th1, zeta, theta, ns=80):
    smax = (theta - zeta) / th1; best = (-1e9, None)
    for i in range(ns + 1):
        s1 = 1 + i * (smax - 1) / ns; s2 = (theta - s1 * th1) / zeta
        if s2 < 1: continue
        v = fvec(s1, s2)
        if v > best[0]: best = (v, (s1, s2))
    return best


def T1of(th1, zeta, lamsw, pen):
    best = 1e18
    for i in range(1, 200):
        a = lamsw * i / 200; b = lamsw - a
        best = min(best, pen * (2 / a) * Fv(b / zeta) * B(th1))
    return best


def evaluate(r, th1, zeta, theta, lamsw, pen, taus=None):
    M, arg = best_main(th1, zeta, theta)
    if arg is None: return (-1e9, None)
    T1 = T1of(th1, zeta, lamsw, pen)
    if M - T1 < -0.5: return (-1e9, None)
    mod = Model(r, zeta, th1, theta)
    K = pen * Lsw(lamsw) * F1 * math.sqrt(th1)
    best = (-1e9, None)
    for tau in (taus or np.linspace(0, min(theta - 0.02, 1.0), 49)):
        Dv = mod.D(tau); U = mod.Unc(tau)
        v = M - T1 - Dv - K * U
        if v > best[0]: best = (v, dict(th1=th1, zeta=zeta, s1=round(arg[0], 4), s2=round(arg[1], 4), main=round(M, 4), T1=round(T1, 4), tau=round(float(tau), 4), D=round(Dv, 4), KU=round(K * U, 4)))
    return best


if __name__ == "__main__":
    r = int(sys.argv[1]); theta = float(sys.argv[2]); lamsw = float(sys.argv[3]); pen = float(sys.argv[4])
    th1s = [float(a) for a in os.environ.get('K4TH1', '0.34,0.36,0.38,0.40,0.42,0.44').split(',')]
    zetas = [float(a) for a in os.environ.get('K4ZETA', '0.006,0.01,0.015,0.02,0.03,0.04,0.06,0.08,0.1').split(',')]
    best = (-1e9, None)
    for zeta in zetas:
        for th1 in th1s:
            if theta - zeta <= th1: continue
            v = evaluate(r, th1, zeta, theta, lamsw, pen)
            if v[0] > best[0]: best = v
            print(f"  zeta={zeta} th1={th1}: {v[0]:.4f} {v[1]}", flush=True)
    print(f"BEST r={r} theta={theta} lamsw={lamsw} pen={pen}: {best[0]:.5f} {best[1]}")
