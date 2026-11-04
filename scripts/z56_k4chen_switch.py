#!/usr/bin/env python3
"""z56 K4CHEN: Chen-type switching for the bad configurations of N2 = 4p+1 (Assessment-level model).

Target C(r): #{p: N1 in S, N2 z2-rough, Omega_Q(N2) <= r} >= main - T1 - TC,
  main = fvec(s1,s2)   (s1 th1 + s2 zeta = theta, s_i >= 1)         [Nath-Xie vector lower sieve]
  T1   = pen (2/a1) F(b1/zeta) B(th1), a1+b1 = lamsw                [P415 switching, N1 = m q q']
  TC   = pen * L(lamsw) * F(1) sqrt(th1) * M_{>=r+2}(zeta)            [switching on N2 = s q_1...q_j, j >= r+2]
  L(lam) = min_{a+b=lam} (2/a) (1/sqrt b)   (linear upper sieve for (n-1)/4 prime at level x^a; semi-linear upper
           sieve for (n+15)/4 in S at level x^b, relative to its truth F(1)sqrt(th1)); L(1/2) = 14.697 at a = 1/3.
  M_{>=k}(zeta) = sum_{j>=k, j even} d_j(1)   (z56_k4chen_mass.py).
Units X G W(z1) W(z2).  Usage: python z56_k4chen_switch.py [r-list] [theta] [lamsw] [pen]"""
import math, sys, os
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import z55_p415_sieve as P
from z56_k4chen_mass import masses

Fv, fvec, best_upper, B = P.Fv, P.fvec, P.best_upper, P.B


def Lsw(lam):
    best = 1e18
    for i in range(1, 2000):
        a = lam * i / 2000; b = lam - a
        if b <= 0: continue
        best = min(best, (2 / a) / math.sqrt(b))
    return best


_MC = {}
def Mge(k, zeta):
    key = round(zeta, 6)
    if key not in _MC: _MC[key] = masses(zeta, jmax=max(16, k + 4), n=2000)
    m = _MC[key]
    return sum(m[j] for j in range(k, len(m)) if j % 2 == 0)


def margin(r, th1, zeta, theta=0.5, lamsw=0.5, pen=1.0, ns=60):
    T1 = best_upper(zeta, lamsw, th1, pen) * B(th1)
    TC = pen * Lsw(lamsw) * Fv(1) * math.sqrt(th1) * Mge(r + 2, zeta)
    smax = (theta - zeta) / th1
    best = (-1e9, None)
    if smax <= 1: return best
    for i in range(ns + 1):
        s1 = 1 + i * (smax - 1) / ns
        s2 = (theta - s1 * th1) / zeta
        if s2 < 1: continue
        v = fvec(s1, s2) - T1 - TC
        if v > best[0]: best = (v, dict(th1=th1, zeta=zeta, s1=round(s1, 4), s2=round(s2, 4), main=round(fvec(s1, s2), 4), T1=round(T1, 4), TC=round(TC, 5)))
    return best


def scan(r, theta=0.5, lamsw=0.5, pen=1.0):
    best = (-1e9, None)
    for th1 in np.arange(0.30, 0.495, 0.01):
        for zeta in [0.004, 0.006, 0.008, 0.01, 0.0125, 0.015, 0.02, 0.025, 0.03, 0.04, 0.05, 0.06, 0.08, 0.1]:
            v = margin(r, th1, zeta, theta, lamsw, pen)
            if v[0] > best[0]: best = v
    return best


if __name__ == "__main__":
    rs = [int(a) for a in (sys.argv[1] if len(sys.argv) > 1 else "8,6,4,2").split(',')]
    theta = float(sys.argv[2]) if len(sys.argv) > 2 else 0.5
    lamsw = float(sys.argv[3]) if len(sys.argv) > 3 else 0.5
    pen = float(sys.argv[4]) if len(sys.argv) > 4 else 1.0
    print(f"# theta={theta} lamsw={lamsw} pen={pen} L(lamsw)={Lsw(lamsw):.4f}")
    for r in rs:
        print(f"r={r}:", scan(r, theta, lamsw, pen), flush=True)
