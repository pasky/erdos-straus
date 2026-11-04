#!/usr/bin/env python3
"""z56 K4CHEN: deterministic numerical witness for Theorem K6 (C(6)) in the pure-switching form (tau = 0, no direct
term), with all switched main terms inflated by pen, explicit level slack eps, grid-refined masses and a tail bound.
  margin = fvec(s1,s2) - pen*(2/a)F(b/zeta)B(th1) - pen*L(lam)F(1)sqrt(th1)*M_{>=8}(zeta),
  th1 s1 + zeta s2 = 1/2 - eps,  a + b = lam = 1/2 - eps.
Floating point (sieve functions by the P415 DDE solver, step 1e-4); not interval-certified."""
import math, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import z55_p415_sieve as P
from z56_k4chen_mass import masses
Fv, fvec, B = P.Fv, P.fvec, P.B
F1 = Fv(1.0)


def tail(zeta, j0):
    L = math.log(1 / zeta)
    return sum(math.exp(math.log(F1 / math.sqrt(zeta)) + (j - 1) * math.log(L / 2) - math.lgamma(j + 1))
               for j in range(j0, j0 + 300))


def witness(r, th1, zeta, pen, eps=1e-3, ns=400, jmax=26):
    lam = 0.5 - eps; k = r + 2
    T1 = min(pen * (2 / a) * Fv((lam - a) / zeta) * B(th1) for a in [lam * i / 4000 for i in range(1, 4000)])
    Lsw = min((2 / a) / math.sqrt(lam - a) for a in [lam * i / 4000 for i in range(1, 4000)])
    out = []
    for n in (2000, 4000, 8000):
        m = masses(zeta, jmax=jmax, n=n)
        M = sum(m[j] for j in range(k, jmax + 1) if j % 2 == 0) + tail(zeta, jmax + 1)
        out.append((n, M, sum(m[0::2])))
    M = max(o[1] for o in out)          # most pessimistic of the refinements
    TC = pen * Lsw * F1 * math.sqrt(th1) * M
    best = (-1e9, None)
    smax = (lam - zeta) / th1
    for i in range(ns + 1):
        s1 = 1 + i * (smax - 1) / ns; s2 = (lam - s1 * th1) / zeta
        if s2 < 1: continue
        v = fvec(s1, s2) - T1 - TC
        if v > best[0]: best = (v, s1, s2, fvec(s1, s2))
    return best, T1, TC, Lsw, out


if __name__ == "__main__":
    for (r, th1, zeta, pen) in [(6, 0.45, 0.008, 2.35), (6, 0.46, 0.006, 2.35), (6, 0.44, 0.006, 1.5), (6, 0.42, 0.006, 1.0),
                                (4, 0.40, 0.02, 1.0), (4, 0.39, 0.02, 1.0), (8, 0.46, 0.003, 2.35)]:
        (v, s1, s2, M), T1, TC, Lsw, out = witness(r, th1, zeta, pen)
        print(f"r={r} th1={th1} zeta={zeta} pen={pen} eps=1e-3: margin={v:.5f} s1={s1:.6f} s2={s2:.6f} "
              f"main={M:.5f} T1={T1:.5f} TC={TC:.5f} L={Lsw:.4f}; masses M_>=k (n, M, sum_even): "
              + "; ".join(f"({n}, {Mk:.6e}, {se:.6f})" for n, Mk, se in out), flush=True)
