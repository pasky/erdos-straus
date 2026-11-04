#!/usr/bin/env python3
"""z56 K4CHEN: continuous optimisation (Nelder-Mead, multi-start) of the pure-switching margin
  fvec(s1,s2) - T1 - K*M_{>=r+2}(zeta)   (see z56_k4chen_switch.py), over th1, zeta, s1 and the T1 split a.
Usage: python z56_k4chen_opt.py r theta lamsw pen"""
import math, sys, os
import numpy as np
from scipy.optimize import minimize
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import z55_p415_sieve as P
from z56_k4chen_mass import masses
from z56_k4chen_switch import Lsw
Fv, fv, fvec, B = P.Fv, P.fv, P.fvec, P.B
F1 = Fv(1.0)
_M = {}
CAP = os.environ.get('K4CAP', '0') == '1'   # P415's extra constraint a <= th1 (not needed, see memo)

def Mge(k, zeta):
    jm = max(18, k + 4); key = (round(zeta, 5), jm)
    if key not in _M: _M[key] = masses(key[0], jmax=jm, n=1500)
    m = _M[key]; return sum(m[j] for j in range(k, len(m)) if j % 2 == 0)


def parts(x, r, theta, lamsw, pen):
    th1, zeta, s1, a = x
    if not (0.26 < th1 < 0.4999 and 0.002 < zeta < 0.4999 and s1 >= 1 and 0.05 < a < lamsw and (a <= th1 or not CAP)): return None
    s2 = (theta - s1 * th1) / zeta
    if s2 < 1: return None
    b = lamsw - a
    T1 = pen * (2 / a) * Fv(b / zeta) * B(th1)
    TC = pen * Lsw(lamsw) * F1 * math.sqrt(th1) * Mge(r + 2, zeta)
    M = fvec(s1, s2)
    return M - T1 - TC, dict(th1=th1, zeta=zeta, s1=s1, s2=s2, a=a, main=M, T1=T1, TC=TC)


def opt(r, theta=0.5, lamsw=0.5, pen=1.0):
    best = (-1e9, None)
    for th1 in (0.36, 0.40, 0.44):
        for zeta in (0.006, 0.015, 0.03, 0.06):
            s1 = 1 + 0.5 * max(0.0, (theta - 2.5 * zeta) / th1 - 1)
            x0 = [th1, zeta, s1, min(0.45, lamsw * 0.9, th1)]
            f = lambda x: -(parts(x, r, theta, lamsw, pen) or (-1e9,))[0]
            res = minimize(f, x0, method='Nelder-Mead', options=dict(xatol=1e-5, fatol=1e-7, maxiter=3000))
            p = parts(res.x, r, theta, lamsw, pen)
            if p and p[0] > best[0]: best = p
    return best


if __name__ == "__main__":
    r = int(sys.argv[1]); theta = float(sys.argv[2]); lamsw = float(sys.argv[3]); pen = float(sys.argv[4])
    v, d = opt(r, theta, lamsw, pen)
    print(f"r={r} theta={theta} lamsw={lamsw} pen={pen}: margin={v:.5f}", {k: round(float(x), 5) for k, x in d.items()} if d else d, flush=True)
