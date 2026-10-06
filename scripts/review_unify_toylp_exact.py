"""R60 exact re-check of CEILINGS_UNIFIED §4.4 (EVIDENCE) via the dual moment LP,
solved by a from-scratch exact rational simplex (Bland's rule).
n i.i.d. bits, p = P/n, K = #ones.  Symmetric order-k functions = deg<=k polys in K.
LP duality:
  max{E B : B<=1[K=0], deg B<=k} = min{ nu(0) : nu>=0 on {0..n}, sum_K nu(K) C(K,j) = C(n,j) p^j, j<=k }
  min{E G : G>=1[K=0], deg G<=k} = max{ nu(0) : same constraints }
"""
from fractions import Fraction as Fr
from math import comb, log


def simplex_eq(A, b, c, maximize=False):
    """optimise c.x s.t. A x = b, x >= 0 (exact). Two-phase, Bland. Returns optimum."""
    m, n = len(A), len(A[0])
    A = [row[:] for row in A]; b = b[:]
    for i in range(m):
        if b[i] < 0:
            A[i] = [-v for v in A[i]]; b[i] = -b[i]
    # tableau with artificials
    T = [A[i] + [Fr(1) if j == i else Fr(0) for j in range(m)] + [b[i]] for i in range(m)]
    basis = [n + i for i in range(m)]
    N = n + m

    def pivot(r, col):
        pv = T[r][col]
        T[r] = [v / pv for v in T[r]]
        for i in range(m):
            if i != r and T[i][col] != 0:
                f = T[i][col]
                T[i] = [a - f * bb for a, bb in zip(T[i], T[r])]
        basis[r] = col

    def run(cost, allowed):
        while True:
            # reduced costs (minimisation)
            cb = [cost[j] for j in basis]
            enter = None
            for j in range(N):
                if j in basis or not allowed(j):
                    continue
                rc = cost[j] - sum(cb[i] * T[i][j] for i in range(m))
                if rc < 0:
                    enter = j; break
            if enter is None:
                return
            best = None
            for i in range(m):
                if T[i][enter] > 0:
                    ratio = T[i][-1] / T[i][enter]
                    if best is None or ratio < best[0] or (ratio == best[0] and basis[i] < basis[best[1]]):
                        best = (ratio, i)
            if best is None:
                raise ValueError("unbounded")
            pivot(best[1], enter)

    cost1 = [Fr(0)] * n + [Fr(1)] * m
    run(cost1, lambda j: True)
    if sum(T[i][-1] for i in range(m) if basis[i] >= n) != 0:
        return None  # infeasible
    # drive artificials out
    for i in range(m):
        if basis[i] >= n:
            for j in range(n):
                if T[i][j] != 0:
                    pivot(i, j); break
    cost2 = [(-v if maximize else v) for v in c] + [Fr(0)] * m
    run(cost2, lambda j: j < n)
    val = sum(cost2[basis[i]] * T[i][-1] for i in range(m))
    return -val if maximize else val


def solve(n, p, k):
    A = [[Fr(comb(K, j)) for K in range(n + 1)] for j in range(k + 1)]
    b = [Fr(comb(n, j)) * p ** j for j in range(k + 1)]
    c = [Fr(1)] + [Fr(0)] * n
    lo = simplex_eq(A, b, c, maximize=False)  # = max E B
    hi = simplex_eq(A, b, c, maximize=True)   # = min E G
    return lo, hi


if __name__ == "__main__":
    n = 40
    for P in (2, 4, 6, 8):
        p = Fr(P, n)
        EF = (1 - p) ** n
        L = log(1 / float(EF))
        kB = kG = None
        row = []
        for k in range(0, 20):
            lo, hi = solve(n, p, k)
            r = float(lo / EF); s = log(1 / float(hi))
            row.append(f"{k}:{r:.3f},{s:.3f}")
            if kB is None and lo > 0:
                kB = k
            if kG is None and s >= 0.9 * L:
                kG = k
            if kB is not None and kG is not None:
                break
        print(f"P={P} log(1/EF)={L:.4f} least k with max E B>0: {kB}; least k with saving>=0.9 log(1/EF): {kG}")
        print("   " + " ".join(row), flush=True)
