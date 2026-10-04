"""O18 (EXCEPTIONAL_INTERFREQ §3; EVIDENCE, floating-point HiGHS LPs).

Exact-interval LP versus CRT LP for *hit-pattern* majorants (all of them,
not only count polynomials) of a prime-modulus Case-B family.

Family: the m smallest primes l = 3 (mod 4) (from LMIN on),
F_l = {-4D mod l : D | ((l+1)/4)^2}.  x(n) in {0,1}^m is the hit pattern.
A level-Q majorant is G(x) = sum_T c_T x^T over subsets T with prod_T l <= Q,
G >= 0 on the whole cube (= nu >= 0 on Z, by CRT), G(0) >= 1.
V(law, Q) = min E_law G.  Laws:
  int  : empirical law of x(n), n in the chosen set inside [1,N] (exact count)
  crt  : product Bern(p_l), p_l = |F_l|/l (all n) or |F_l|/(l-1) (primes)
  prodI: product Bern(p'_l) with the interval marginals p'_l (isolates the
         correlation effect from the thinning of the marginals)
Printed: savings -log V.  Q = inf means all 2^m monomials (V = law(0)).

Run: uv run --with scipy python scripts/interfreq_hitpattern_lp.py N m [all|prime] [LMIN] [OFFSET]
Memory: sparse matrix with <= 3^m nonzeros (m <= 14: < 5e6); < 2 GB.
Q = inf uses the closed form V = law(0).  Prime mode skips Q = N^3 (slow LPs
on ~300-point empirical laws).  Large OFFSET in prime mode sieves to OFFSET+N.
"""
import math
import sys

import numpy as np
import scipy.sparse as sp
from scipy.optimize import linprog


def primes_upto(n):
    s = np.ones(n + 1, bool); s[:2] = False
    for i in range(2, int(n ** 0.5) + 1):
        if s[i]:
            s[i * i::i] = False
    return np.nonzero(s)[0]


def divisors_of_square(a):
    ds = [1]; p = 2
    while p * p <= a:
        if a % p == 0:
            e = 0
            while a % p == 0:
                a //= p; e += 1
            ds = [d * p ** j for d in ds for j in range(2 * e + 1)]
        p += 1
    if a > 1:
        ds = [d * a ** j for d in ds for j in range(3)]
    return ds


def forced(l):
    return sorted({(-4 * D) % l for D in divisors_of_square((l + 1) // 4)})


def monomials(ls, Q):
    """all subsets (as bitmasks) with prod <= Q."""
    out = []
    def rec(i, mask, prod):
        out.append(mask)
        for j in range(i, len(ls)):
            if prod * ls[j] <= Q:
                rec(j + 1, mask | (1 << j), prod * ls[j])
    rec(0, 0, 1)
    return out


def solve(monos, m, mom):
    """min sum_T c_T mom[T] s.t. sum_{T subset x} c_T >= 0 for all x, c_0 >= 1."""
    X = np.arange(1 << m)
    rows, cols = [], []
    for j, T in enumerate(monos):
        xs = X[(X & T) == T]
        rows.append(xs); cols.append(np.full(len(xs), j))
    rows = np.concatenate(rows); cols = np.concatenate(cols)
    A = sp.csr_matrix((-np.ones(len(rows)), (rows, cols)), shape=(1 << m, len(monos)))
    b = np.zeros(1 << m)
    bounds = [(None, None)] * len(monos)
    bounds[monos.index(0)] = (1.0, None)
    c = np.array([mom(T) for T in monos])
    res = linprog(c, A_ub=A, b_ub=b, bounds=bounds, method="highs")
    assert res.status == 0, res.message
    G = -(A @ res.x)
    assert G.min() > -1e-7, G.min()
    return res.fun


def main():
    N = int(sys.argv[1]); m = int(sys.argv[2])
    mode = sys.argv[3] if len(sys.argv) > 3 else "prime"
    LMIN = int(sys.argv[4]) if len(sys.argv) > 4 else 3
    OFF = int(sys.argv[5]) if len(sys.argv) > 5 else 0   # interval [OFF+1, OFF+N]
    assert m <= 14, "memory bound advertised for m <= 14"
    ls = [int(l) for l in primes_upto(10 ** 6) if l % 4 == 3 and l >= LMIN][:m]
    Fs = [set(forced(l)) for l in ls]
    if mode == "prime":
        ns = primes_upto(OFF + N); ns = ns[ns > max(OFF, max(ls))]  # avoid n = l
    else:
        ns = np.arange(OFF + 1, OFF + N + 1, dtype=np.int64)
    pat = np.zeros(len(ns), np.int64)
    for j, (l, F) in enumerate(zip(ls, Fs)):
        r = ns % l
        hit = np.isin(r, list(F))
        pat |= hit.astype(np.int64) << j
    cnt = np.bincount(pat, minlength=1 << m).astype(float) / len(ns)
    # moments E x^T for the empirical law: sum over x superset of T (zeta transform)
    zeta = cnt.copy()
    for j in range(m):
        bit = 1 << j
        idx = np.arange(1 << m)
        lo = idx[(idx & bit) == 0]
        zeta[lo] += zeta[lo | bit]
    pc = [len(F) / (l if mode == "all" else l - 1) for l, F in zip(ls, Fs)]
    pi = [zeta[1 << j] for j in range(m)]
    def mom_prod(p):
        return lambda T: math.prod(p[j] for j in range(m) if T >> j & 1)
    print(f"N={N} offset={OFF} mode={mode} m={m} #n={len(ns)} primes={ls}")
    print("p_crt  =", [round(x, 4) for x in pc])
    print("p_int  =", [round(float(x), 4) for x in pi])
    print(f"void: int {cnt[0]:.5f}  crt {math.prod(1 - x for x in pc):.5f}  "
          f"prodI {math.prod(1 - x for x in pi):.5f}")
    print("Q        #mono  sav_int  sav_crt  sav_prodI")
    exps = [0.5, 0.75, 1.0, 1.25, 1.5, 2.0] + ([3.0] if mode == "all" else []) + [None]
    for e in exps:
        if e is None:   # full level: V = law(0) exactly (G = 1_{x=0})
            monos = monomials(ls, float("inf"))
            vi = cnt[0]
            vc = math.prod(1 - x for x in pc)
            vp = math.prod(1 - x for x in pi)
        else:
            monos = monomials(ls, N ** e)
            vi = solve(monos, m, lambda T: zeta[T])
            vc = solve(monos, m, mom_prod(pc))
            vp = solve(monos, m, mom_prod(pi))
        lab = f"N^{e}" if e is not None else "inf"
        print(f"{lab:8s} {len(monos):6d}  {-math.log(vi):7.4f}  {-math.log(vc):7.4f}  {-math.log(vp):7.4f}",
              flush=True)


if __name__ == "__main__":
    main()
