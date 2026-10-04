"""Exhaustive-enumeration check (floating-point LP) of EXCEPTIONAL_KARY Theorem 2.5 on random small systems,
for the plain sequential law sigma and for the phantom variant; asserts the weighted LP value <= 1.

For each random instance (product law nu on a small grid, random unary/binary/
ternary patterns), enumerate every path omega=(c,y) of the phantom-sequential
process with its probability, then solve the LP

    max E_omega[ exp(-Phi(omega)) f(y(omega)) ]  s.t.  E_nu f = 1, f >= 0, f d-local.

Theorem 2.5 says the optimum is <= 1. Phi uses the *optimal* one-dimensional
constant B*(n,t,d) (an LP), which is <= any Lagrange constant, so this is a
stronger test than the theorem as stated. Also reports, for information,
C*(law) = max E_law f / E_nu f over d-local f >= 0, for the phantom law sigma~
and for the plain sequential law sigma (ETw Conj 6.4).

usage: kary_check.py [ninst] [seed] [dense|graph]
"""
import itertools, math, sys
from functools import lru_cache
import numpy as np
from scipy.optimize import linprog


@lru_cache(maxsize=None)
def bstar(n, t, d):
    """max Q(n) s.t. Q>=0 on {0..n}, deg Q <= d, E_{Bin(n,t)} Q = 1."""
    if n == 0:
        return 1.0
    k = min(d, n)
    K = np.arange(n + 1, dtype=float)
    x = 2 * K / n - 1                       # Chebyshev basis on [0,n] (well scaled)
    A = np.polynomial.chebyshev.chebvander(x, k)
    psi = np.array([math.exp(math.lgamma(n + 1) - math.lgamma(j + 1) - math.lgamma(n - j + 1)
                             + j * math.log(t) + (n - j) * math.log1p(-t)) for j in range(n + 1)])
    res = linprog(-A[n], A_ub=-A, b_ub=np.zeros(n + 1), A_eq=(psi @ A)[None, :], b_eq=[1.0],
                  bounds=[(None, None)] * (k + 1), method="highs")
    assert res.status == 0, res.message
    return -res.fun


def lagrange_bound(n, t, d):
    """right side of (2.1)"""
    return d * math.log(4 * math.e ** 3 * (n + 1) / t) + 0.5 * math.log(16 * n * t + 16)


DENSE = False
MODE = ""


def graph_instance(rng, m):
    """{0,1} coordinates, nu(1) in [0.1,0.25], patterns forbid all-ones on random pairs/triples."""
    nus = []
    for _ in range(m):
        p1 = 0.1 + 0.15 * rng.random()
        nus.append(np.array([1 - p1, p1]))
    pats = set()
    for _ in range(int(rng.integers(m, 3 * m))):
        k = int(rng.choice([1, 2, 2, 2, 3, 3]))
        pats.add(tuple(sorted(int(v) for v in rng.choice(m, size=k, replace=False))))
    return [2] * m, nus, [(T, (1,) * len(T)) for T in pats]


def random_instance(rng, m, q):
    if MODE == "graph":
        return graph_instance(rng, m)
    sizes = [q] * m
    nus = []
    for _ in range(m):
        w = rng.random(q) ** (1.0 if DENSE else 2.5)
        w[0] += (0.3 * rng.random() if DENSE else 2.0 * rng.random() + 0.5)
        nus.append(w / w.sum())
    pats = []
    for _ in range(rng.integers(m, 3 * m + 1)):
        k = rng.choice([1, 2, 2, 2, 3])
        T = tuple(sorted(rng.choice(m, size=k, replace=False)))
        a = tuple(int(rng.integers(1, q)) for _ in T)   # patterns avoid the heavy value 0
        pats.append((T, a))
    return sizes, nus, pats


def activated(l, pats, cand):
    """F~_l: values a at l completing a pattern with top l, lower coords from cand[i] (a set)."""
    F = set()
    for T, a in pats:
        if T[-1] != l:
            continue
        if all(a[j] in cand[i] for j, i in enumerate(T[:-1])):
            F.add(a[-1])
    return F


def paths(sizes, nus, pats, delta, phantom=True):
    """enumerate (prob, y, M, n) of the phantom (or plain) sequential process."""
    m = len(sizes)
    out = []

    def rec(l, prob, c, y, M, n):
        if l == m:
            out.append((prob, tuple(y), M, n))
            return
        cand = [({c[i], y[i]} if phantom else {y[i]}) for i in range(l)]
        F = activated(l, pats, cand)
        p = sum(nus[l][a] for a in F)
        light = p <= delta
        for cl in range(sizes[l]):
            pc = nus[l][cl]
            if pc == 0:
                continue
            if light and cl in F:
                for yl in range(sizes[l]):
                    if yl in F:
                        continue
                    rec(l + 1, prob * pc * nus[l][yl] / (1 - p), c + [cl], y + [yl],
                        M + p, n + 1)
            else:
                rec(l + 1, prob * pc, c + [cl], y + [cl], M + (p if light else 0.0), n)

    rec(0, 1.0, [], [], 0.0, 0)
    return out


def dlocal_matrix(sizes, d):
    """columns: indicators 1[y_T = b] for |T|<=d; rows: all points of the grid."""
    m = len(sizes)
    pts = list(itertools.product(*[range(s) for s in sizes]))
    cols = []
    for k in range(d + 1):
        for T in itertools.combinations(range(m), k):
            for b in itertools.product(*[range(sizes[i]) for i in T]):
                cols.append((T, b))
    A = np.zeros((len(pts), len(cols)))
    for j, (T, b) in enumerate(cols):
        for i, x in enumerate(pts):
            if all(x[t] == bb for t, bb in zip(T, b)):
                A[i, j] = 1.0
    return pts, A


def lp_max(A, obj_w, nu_w):
    """max obj_w . (A z) s.t. nu_w . (A z) = 1, A z >= 0."""
    res = linprog(-(obj_w @ A), A_ub=-A, b_ub=np.zeros(A.shape[0]), A_eq=(nu_w @ A)[None, :],
                  b_eq=[1.0], bounds=[(None, None)] * A.shape[1], method="highs")
    if res.status == 3:
        return math.inf
    assert res.status == 0, res.message
    return -res.fun


def main():
    ninst = int(sys.argv[1]) if len(sys.argv) > 1 else 30
    seed = int(sys.argv[2]) if len(sys.argv) > 2 else 1
    global DENSE
    DENSE = len(sys.argv) > 3 and sys.argv[3] == "dense"
    global MODE
    MODE = sys.argv[3] if len(sys.argv) > 3 else ""
    rng = np.random.default_rng(seed)
    M0 = 4.0
    worst = 0.0
    print("inst m q d delta  EM  En  max weighted LP over {phantom,plain}x{Thm2.5,Rem2.7} (<=1)  logC*(phantom)  logC*(plain)  E[Phi]  E[Phi_(2.1)]")
    for inst in range(ninst):
        m = int(rng.integers(3, 6)) if MODE != "graph" else int(rng.integers(5, 9))
        q = int(rng.integers(2, 4))
        d = int(rng.integers(1, min(m, 3) + 1))
        delta = float(rng.choice([0.25, 0.15, 0.08])) if not DENSE else 0.25
        sizes, nus, pats = random_instance(rng, m, q)
        pts, A = dlocal_matrix(sizes, d)
        idx = {x: i for i, x in enumerate(pts)}
        nu_w = np.array([math.prod(nus[l][x[l]] for l in range(m)) for x in pts])
        P = paths(sizes, nus, pats, delta, phantom=True)
        tot = sum(p for p, *_ in P)
        assert abs(tot - 1) < 1e-9, tot
        obj = np.zeros(len(pts)); law = np.zeros(len(pts))
        EM = En = EPhi = EPhi21 = 0.0
        for p, y, M, n in P:
            t = 1.0 / (M + M0)
            phi = math.log(bstar(n, round(t, 12), d)) + (4 / 3) * math.log(1 + M / M0)
            obj[idx[y]] += p * math.exp(-phi)
            law[idx[y]] += p
            EM += p * M; En += p * n; EPhi += p * phi
            EPhi21 += p * (lagrange_bound(n, t, d) + (4 / 3) * math.log(1 + M / M0))
        Pp = paths(sizes, nus, pats, delta, phantom=False)
        assert abs(sum(p for p, *_ in Pp) - 1) < 1e-9
        vals = [lp_max(A, obj, nu_w)]
        # Theorem 2.5 (constant t = d/(EM+4d), weight exp(-(4/3)tM)) for the phantom law
        # and for the plain sequential law sigma (frozen-path coupling, §2)
        for PP in (P, Pp):
            EMp = sum(p * M for p, y, M, n in PP)
            tc = d / (EMp + 4 * d)
            o1 = np.zeros(len(pts)); o2 = np.zeros(len(pts))
            for p, y, M, n in PP:
                o1[idx[y]] += p * math.exp(-math.log(bstar(n, round(tc, 12), d)) - (4 / 3) * tc * M)
                t = 1.0 / (M + M0)
                o2[idx[y]] += p * math.exp(-math.log(bstar(n, round(t, 12), d)) - (4 / 3) * math.log(1 + M / M0))
            vals += [lp_max(A, o1, nu_w), lp_max(A, o2, nu_w)]
        val = max(vals)
        assert val <= 1 + 1e-7, (inst, vals)
        cph = lp_max(A, law, nu_w)
        lawp = np.zeros(len(pts))
        for p, y, M, n in Pp:
            lawp[idx[y]] += p
        cpl = lp_max(A, lawp, nu_w)
        worst = max(worst, val)
        print(f"{inst:3d} {m} {q} {d} {delta:.2f} {EM:.3f} {En:.3f}  {val:.6f}  "
              f"{math.log(cph):.4f}  {math.log(cpl):.4f}  {EPhi:.3f}  {EPhi21:.3f}")
    print(f"max weighted LP value = {worst:.9f}  (theorem: <= 1)")


if __name__ == "__main__":
    main()
