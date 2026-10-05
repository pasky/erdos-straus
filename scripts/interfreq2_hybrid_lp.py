"""O25 toy LPs: hybrid optimum H* versus exact count and capped comparators.

Family: Q = product of the given primes; for each odd prime p a forced set
F_p of residues mod p (default: the quadratic non-residues r with r <= k_p,
or random); A = {n mod Q : n mod p not in F_p for all p}.  N = window length.
All classes b mod d with d | Q are available (Q' = Q).

Values (all are minima over majorants nu >= 1_A on Z/Q):
  exact : #(A cap [1,N])
  Hstar : sum_{n<=N} nu_small + sum_large beta*(a,d)     (hybrid, Def 1.2)
  Vsmall: sum_{n<=N} nu, only classes with d <= N/2       (IF Cor 2.3 regime)
  VT    : sum_{n<=N} nu + sum_{d>N/2} |a|                 (IF Thm 2.5, c = 1)
  Vcrt  : N*E nu, classes with d <= N only                (CRT mean, level log N)
Usage: python interfreq2_hybrid_lp.py N primes(comma) mode [seed] [Qextra]
  mode: qnr  -> F_p = all quadratic non-residues mod p (squares avoid)
        rand<f> -> F_p random of size round(f*p)
  Qextra: optional extra prime(s) (comma) adjoined to Q' only (no forced classes)
"""
import sys, itertools, random
import numpy as np
import scipy.sparse as sp
from scipy.optimize import linprog


def divisors(primes):
    ds = [1]
    for p in primes:
        ds = ds + [d * p for d in ds]
    return sorted(ds)


def build_family(primes, mode, seed):
    rng = random.Random(seed)
    F = {}
    for p in primes:
        if p == 2:
            continue
        if mode == "qnr":
            sq = {(x * x) % p for x in range(p)}
            F[p] = sorted(set(range(1, p)) - sq)
        elif mode.startswith("rand"):
            f = float(mode[4:])
            k = max(1, round(f * p))
            F[p] = sorted(rng.sample(range(p), k))
    return F


def lp_value(Q, N, A, classes, cost_fn, split_large, Nhalf):
    """classes: list of (b,d). cost_fn(b,d) -> (cost_pos, cost_neg) per unit
    of positive / negative coefficient. Returns optimum."""
    rows, cols, cpos = [], [], []
    nvar = 0
    cost = []
    for (b, d) in classes:
        cp, cn = cost_fn(b, d)
        pts = np.arange(b, Q, d)
        # positive part
        rows.append(pts); cols.append(np.full(len(pts), nvar)); cpos.append(np.ones(len(pts)))
        cost.append(cp); nvar += 1
        # negative part
        rows.append(pts); cols.append(np.full(len(pts), nvar)); cpos.append(-np.ones(len(pts)))
        cost.append(-cn); nvar += 1
    r = np.concatenate(rows); c = np.concatenate(cols); v = np.concatenate(cpos)
    M = sp.csr_matrix((v, (r, c)), shape=(Q, nvar))
    rhs = A.astype(float)
    res = linprog(np.array(cost), A_ub=-M, b_ub=-rhs, bounds=[(0, None)] * nvar,
                  method="highs")
    assert res.status == 0, res.message
    lp_value.last = (res.x, classes)
    return res.fun


def main():
    N = int(sys.argv[1])
    primes = [int(x) for x in sys.argv[2].split(",")]
    mode = sys.argv[3]
    seed = int(sys.argv[4]) if len(sys.argv) > 4 else 0
    extra = [int(x) for x in sys.argv[5].split(",")] if len(sys.argv) > 5 else []
    F = build_family(primes, mode, seed)
    Qf = 1
    for p in primes:
        Qf *= p
    allp = primes + extra
    Q = Qf
    for p in extra:
        Q *= p
    n = np.arange(Q)
    A = np.ones(Q, dtype=bool)
    for p, Fp in F.items():
        A &= ~np.isin(n % p, Fp)
    lamN = np.zeros(Q)
    for m in range(1, N + 1):
        lamN[m % Q] += 1
    def cnt(b, d):
        return lamN[b::d].sum()
    divs = divisors(allp)
    def cls(pred):
        return [(b, d) for d in divs if pred(d) for b in range(d)]
    exact = int(sum(A[m % Q] for m in range(1, N + 1)))
    allc = cls(lambda d: True)
    def hyb(b, d):
        if 2 * d <= N:
            c = cnt(b, d); return (c, c)
        return (-(-N // d), N // d)
    Hs = lp_value(Q, N, A, allc, hyb, True, N / 2)
    x, cl = lp_value.last
    small_cnt = Wplus = Tm_right = Twrong = 0.0
    for k, (b, d) in enumerate(cl):
        a = x[2 * k] - x[2 * k + 1]
        if abs(a) < 1e-12:
            continue
        c = cnt(b, d)
        if 2 * d <= N:
            small_cnt += a * c
            continue
        u, l = -(-N // d), N // d
        full, sparse = (c == u), (c == l)
        right = (a > 0 and full) or (a < 0 and sparse)
        if not right:
            Twrong += abs(a)
        elif d > N:
            if a > 0:
                Wplus += a
        else:
            Tm_right += abs(a)
    decomp = (small_cnt, Wplus, Tm_right, Twrong)
    small = cls(lambda d: 2 * d <= N)
    Vs = lp_value(Q, N, A, small, lambda b, d: (cnt(b, d), cnt(b, d)), False, N / 2)
    def vt(b, d):
        c = cnt(b, d)
        if 2 * d <= N:
            return (c, c)
        return (c + 1, c - 1)
    VT = lp_value(Q, N, A, allc, vt, False, N / 2)
    crt = cls(lambda d: d <= N)
    Vc = lp_value(Q, N, A, crt, lambda b, d: (N / d, N / d), False, N / 2)
    dens = A.mean()
    print(f"N={N} Q={Q} (family {Qf}, extra {extra}) mode={mode} seed={seed} "
          f"density={dens:.4f} N*dens={N*dens:.2f}")
    print(f"  exact={exact}  Hstar={Hs:.4f}  Vsmall={Vs:.4f}  VT={VT:.4f}  Vcrt={Vc:.4f}")
    print("  H* optimum: small-part count %.3f, W+ (pos full, d>N) %.3f, right medium mass %.3f, wrong-sign mass %.3f" % decomp)


if __name__ == "__main__":
    main()
