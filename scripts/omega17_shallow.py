"""O68 / POINTWISE_OMEGA17 §3: shallow planting in the symmetric Poisson model (EVIDENCE).

N ~ Poisson(R) (number of big events on). A *shallow fake of degree d* is a polynomial density
psi(j) = sum_{i=1..d} c_i (j)_i / R^i  (psi(0)=0 automatically), psi(j) >= 0 for j >= 1, with
E[psi(N) C(N,t)] = E[C(N,t)] for t = 0..k  (same first k factorial moments as Poisson(R)).
Degree d in the event indicators = level T^d (classes mod products of <= d big moduli).
Scaled constraint: sum_i c_i G[t][i] = 1 with G[t][i] = sum_s C(i,s) C(t,s) s! R^{-s}.
We report the least d for which an LP finds such psi (positivity checked on j <= Jmax), and the
least d with additionally psi <= Lambda on j <= Jmax (box).
Usage: uv run --with scipy python scripts/omega17_shallow.py
"""
import math
import sys

import numpy as np
from scipy.optimize import linprog


def G(t, i, R):
    return sum(math.comb(i, s) * math.comb(t, s) * math.factorial(s) * R ** (-s)
               for s in range(min(i, t) + 1))


def basis(j, i, R):
    # (j)_i / R^i
    v = 1.0
    for a in range(i):
        v *= (j - a) / R
    return v


def feasible(R, k, d, Jmax, Lam=None):
    A_eq = np.array([[G(t, i, R) for i in range(1, d + 1)] for t in range(k + 1)])
    b_eq = np.ones(k + 1)
    js = range(1, Jmax + 1)
    Bm = np.array([[basis(j, i, R) for i in range(1, d + 1)] for j in js])
    A_ub = [-Bm]
    b_ub = [np.zeros(len(Bm))]
    if Lam is not None:
        A_ub.append(Bm)
        b_ub.append(np.full(len(Bm), Lam))
    # objective: minimise max deviation is awkward; just minimise sum psi at j<=Jmax (any feasible)
    res = linprog(np.zeros(d), A_ub=np.vstack(A_ub), b_ub=np.concatenate(b_ub), A_eq=A_eq,
                  b_eq=b_eq, bounds=[(None, None)] * d, method="highs")
    return res.status == 0, (res.x if res.status == 0 else None)


def main():
    out = []
    for R in [4, 8, 16, 32]:
        Jmax = int(R + 12 * math.sqrt(R) + 40)
        for k in range(0, 9):
            dmin = dbox = None
            for d in range(k + 1, 4 * k + 30):
                ok, _ = feasible(R, k, d, Jmax)
                if ok and dmin is None:
                    dmin = d
                if dmin is not None:
                    okb, _ = feasible(R, k, d, Jmax, Lam=4.0)
                    if okb:
                        dbox = d
                        break
            line = f"R={R:3d} k={k:2d}  d_min={dmin}  d_min(psi<=4)={dbox}"
            print(line, flush=True)
            out.append(line)
    return out


if __name__ == "__main__":
    main()
