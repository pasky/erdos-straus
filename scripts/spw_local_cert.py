"""O40: exact rational certificate for the local SPW bound at (N, C, e).

Solve the local LP (spw_local_lp), take its dual: g = sum_{d|e, d<=D, maximal} y_{d,b} 1[x=b mod d],
patch weights z_s >= 0 on classes mod e' | e, e' > CN.  Round y to rationals; keep coarse z rounded and
clipped >= 0; then put point-level patches (e' = e) z_x := max(0, g(x) - sum coarse z covering x), so
sum_s z_s 1_s >= g holds EXACTLY.  For any SPW(C, sigma) measure R at N (projected to Z/e):
   sum_{n<=N} g(n) = <g, R> <= sum_s z_s R(s) <= (1 - sigma) sum_s z_s,
hence sigma <= 1 - (sum_{n<=N} g(n)) / (sum_s z_s).   (Fractions; PROVED once the script prints it.)
usage: spw_local_cert.py N C e
"""
import sys
from fractions import Fraction as Fr
import numpy as np
from scipy.optimize import linprog
from scipy.sparse import coo_matrix

def cnt(b, d, N):
    b %= d
    first = b if b >= 1 else d
    return 0 if first > N else (N - first) // d + 1

def main(N, C, e, den=10**6):
    C = Fr(C)  # exact: classes mod e' are 'large' iff e' > C*N exactly
    D = N // 2
    assert e > C * N
    x = np.arange(e)
    divs = [d for d in range(1, e + 1) if e % d == 0]
    small = [d for d in divs if d <= D]
    smax = [d for d in small if not any(m % d == 0 and m != d for m in small)]
    big = [d for d in divs if d > C * N]  # exact Fraction comparison
    er, ec, beq, eqlab = [], [], [], []
    r = 0
    for d in smax:
        er.append(x % d + r); ec.append(x); beq += [cnt(b, d, N) for b in range(d)]
        eqlab += [(d, b) for b in range(d)]; r += d
    Aeq = coo_matrix((np.ones(e * len(smax)), (np.concatenate(er), np.concatenate(ec))), shape=(r, e + 1)).tocsr()
    ur, uc, ulab = [], [], []
    q = 0
    for d in big:
        ur.append(x % d + q); uc.append(x); ulab += [(d, b) for b in range(d)]; q += d
    ur = np.concatenate(ur); uc = np.concatenate(uc)
    rows = np.concatenate([ur, np.arange(q)]); cols = np.concatenate([uc, np.full(q, e)])
    Aub = coo_matrix((np.ones(len(rows)), (rows, cols)), shape=(q, e + 1)).tocsr()
    c = np.zeros(e + 1); c[-1] = -1
    res = linprog(c, A_ub=Aub, b_ub=np.ones(q), A_eq=Aeq, b_eq=np.array(beq, float),
                  bounds=[(0, None)] * e + [(None, None)], method="highs")
    assert res.status == 0
    sig_lp = -res.fun
    # duals (HiGHS sign conventions: for min problem, eq marginals y, ineq marginals <= 0)
    y = res.eqlin.marginals; z = -res.ineqlin.marginals
    # g(x) = -sum y_{d,b}  (sign chosen so that the certificate inequality works; we try both signs)
    best = None
    for sgn in (1, -1):
        gy = {lab: Fr(sgn * float(v)).limit_denominator(den) for lab, v in zip(eqlab, y) if abs(v) > 1e-12}
        g = [Fr(0)] * e
        for (d, b), v in gy.items():
            for t in range(b, e, d):
                g[t] += v
        zc = {}
        cover = [Fr(0)] * e
        for (d, b), v in zip(ulab, z):
            if d == e or v <= 1e-12:
                continue
            fv = Fr(float(v)).limit_denominator(den)
            zc[(d, b)] = fv
            for t in range(b, e, d):
                cover[t] += fv
        zp = [max(Fr(0), g[t] - cover[t]) for t in range(e)]
        Z = sum(zc.values()) + sum(zp)
        Wsum = sum(g[n % e] for n in range(1, N + 1))
        if Z > 0:
            bound = 1 - Wsum / Z
            if best is None or bound < best[0]:
                best = (bound, sgn, Wsum, Z)
    bound, sgn, Wsum, Z = best
    import math
    up = math.ceil(bound * 10**6) / 10**6  # outward (upward) rounding of the exact rational bound
    print(f"N={N} C={C} e={e}: LP sigma_loc={sig_lp:.6f}; exact certificate verified: sigma <= {up:.6f} "
          f"(exact rational, denominator has {len(str(bound.denominator))} digits)")
    return bound

if __name__ == "__main__":
    main(int(sys.argv[1]), Fr(sys.argv[2]), int(sys.argv[3]))
