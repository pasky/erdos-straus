"""R65 from-scratch check of the single-modulus SPW certificates quoted in v5 §14.9
(sigma <= 72/185 at N=300, e=630; sigma <= 0.381133 at N=1150, e=2310; C=2).

Exact weak-duality bound: for any g = sum_{d|e, d<=N/2} y_{d,b} 1[x = b mod d] on Z/e,
and any R with (P1) (class sums mod d<=N/2 equal the window counts) and (P2) (every class of
modulus e > CN has R-mass <= 1-sigma; only modulus e itself is used here):
   sum_{n<=N} g(n) = <g,R> <= sum_x g(x)^+ R(x mod e) <= (1-sigma) sum_x g(x)^+ .
So sigma <= 1 - sum_W g / sum_x g^+ exactly, for ANY rational g of that form.  g is obtained
from the LP dual (scipy HiGHS), rounded to rationals, and the bound evaluated in Fractions.
Note: the paper's certificates use patches on classes mod e'|e, e'>CN; for e=630, 2310 and
CN = 600, 2300 the only such e' is e itself, so pointwise patches are all there is.
"""
import sys
from fractions import Fraction
import numpy as np
from scipy.optimize import linprog
from scipy.sparse import lil_matrix


def run(N, C, e):
    D = N // 2
    divs = [d for d in range(1, D + 1) if e % d == 0]
    assert [d for d in range(C * N + 1, e + 1) if e % d == 0] == [e]
    rows = [(d, b) for d in divs for b in range(d)]
    A = lil_matrix((len(rows), e + 1))
    rhs = np.zeros(len(rows))
    for i, (d, b) in enumerate(rows):
        for x in range(b, e, d):
            A[i, x] = 1
        rhs[i] = sum(1 for n in range(1, N + 1) if n % d == b)
    # rho_x + sigma <= 1
    Aub = lil_matrix((e, e + 1))
    for x in range(e):
        Aub[x, x] = 1; Aub[x, e] = 1
    c = np.zeros(e + 1); c[e] = -1
    res = linprog(c, A_ub=Aub.tocsr(), b_ub=np.ones(e), A_eq=A.tocsr(), b_eq=rhs,
                  bounds=[(0, None)] * (e + 1), method="highs")
    assert res.status == 0
    lp = -res.fun
    y = res.eqlin.marginals
    best = None
    for den in (10**4, 10**6, 10**8, 10**10, 10**12):
        yq = [Fraction(round(v * den), den) for v in y]
        g = [Fraction(0)] * e
        for (d, b), v in zip(rows, yq):
            if v:
                for x in range(b, e, d):
                    g[x] += v
        # sign convention: try both g and -g
        for s in (1, -1):
            gw = sum(s * g[n % e] for n in range(1, N + 1))
            gp = sum(max(s * v, 0) for v in g)
            if gp > 0:
                bnd = 1 - gw / gp
                if best is None or bnd < best:
                    best = bnd
    return lp, best


for N, C, e, claim in [(300, 2, 630, Fraction(72, 185)), (1150, 2, 2310, Fraction(381133, 10**6))]:
    lp, best = run(N, C, e)
    print(f"N={N} e={e}: LP optimum sigma* = {lp:.6f}; exact rational certificate sigma <= {float(best):.7f}"
          f" (= {best if best.denominator < 10**6 else '...'}); paper claims <= {claim} = {float(claim):.6f}:",
          "CONSISTENT" if best <= claim + Fraction(1, 10**6) else "NOT REPRODUCED")
