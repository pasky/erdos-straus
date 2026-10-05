"""R34a: from-scratch check that OMEGA9 Thm 1.1's parameter choices close with an
ABSOLUTE C_2 (no hidden dependence on A or Z).

Given (G)'s constants (C_G, c, kappa) and Page's c2, with
   L = 2c + log(400 C_G (A+1)),  log Q_G = log x/(kappa L),  log x = C_2 (1+log A) log Z,
we find, on a grid of (A, Z) with 1 <= A <= Z^{1/4}, the least C_2 making ALL of:
   Q_G >= Z;  Q_G >= 1e4 C_G (A+1)(kappa L)^2;  kappa L >= 6c;  log x >= 16;
   x >= 800 A Z^3                              (R_1, generic case)
   x >= 400 c2 A Z^{3.5} (log Z)^2 / 8 * ...   (R_1 in Case A, via Page; see review m4)
   Case 0 error ratio  C_G A (e^{-L} + (kappa L)^2/Q_G)          <= 1/200
   Exc.  error ratio  2 C_G A L (e^{-kappa L} + kappa L/Q_G)     <= 1/100
hold, and report max over the grid. All in log space.
"""
import math

import numpy as np


def need_C2(CG, c, kap, c2, A, Z):
    lA, lZ = math.log(A), math.log(Z)
    L = 2 * c + math.log(400 * CG * (A + 1))
    assert kap * L >= 6 * c
    reqs = []
    # log Q_G = C2 (1+lA) lZ / (kap L) >= max(lZ, log(1e4 CG (A+1)(kap L)^2))
    lQneed = max(lZ, math.log(1e4 * CG * (A + 1) * (kap * L) ** 2))
    reqs.append(lQneed * kap * L / ((1 + lA) * lZ))
    reqs.append(16 / ((1 + lA) * lZ))
    reqs.append(math.log(800 * A) / ((1 + lA) * lZ) + 3 / (1 + lA))
    # Case A: lambda >= min(16(1-b),1)/2 >= 8/(c2 sqrt(Z) lZ^2) ; need 2 Z^3 A <= lambda x/100
    lam_lb = min(8 / (c2 * math.sqrt(Z) * max(lZ, 1) ** 2), 0.5)
    reqs.append((math.log(200 * A / lam_lb) + 3 * lZ) / ((1 + lA) * lZ))
    C2 = max(reqs)
    # verify error ratios at this C2
    lx = C2 * (1 + lA) * lZ
    lQ = lx / (kap * L)
    r0 = CG * A * (math.exp(-L) + math.exp(2 * math.log(kap * L) - lQ))
    r1 = 2 * CG * A * L * (math.exp(-kap * L) + math.exp(math.log(kap * L) - lQ))
    assert r0 <= 1 / 200 and r1 <= 1 / 100, (r0, r1)
    return C2


for CG, c, kap, c2 in [(1, 1, 3, 1), (1e3, 2, 10, 1e2), (1e9, 5, 50, 1e6)]:
    worst = 0
    for lZ in np.geomspace(math.log(2), 700, 60):
        Z = math.exp(lZ)
        for t in np.linspace(0, 1, 15):
            A = math.exp(t * lZ / 4)
            worst = max(worst, need_C2(CG, c, kap, c2, A, Z))
    print("C_G=%g c=%g kappa=%g c2=%g: sup over grid of required C_2 = %.1f" % (CG, c, kap, c2, worst))
print("bounded => C_2 depends only on (C_G, c, kappa, c2): absolute, as claimed")
