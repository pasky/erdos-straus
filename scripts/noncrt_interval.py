"""EXCEPTIONAL_NONCRT.md §8.3 (EVIDENCE): interval [1,N] vs CRT model for
hit-count majorants of the prime-modulus Case-B family.

Family: primes l = 3 (mod 4), F_l = {-4D mod l : D | ((l+1)/4)^2} (forced
classes, notes Lemma 18.1). H_Y(n) = #{l <= Y : n mod l in F_l}.
CRT model: H_Y ~ sum of independent Bern(|F_l|/l).
For degree k = 0..KMAX, solve the LP  min E[P(H)]  over real polynomials P
of degree <= k with P >= 0 on {0..HCAP} and P(0) >= 1, once for the
empirical law of H_Y on [1,N] and once for the CRT law. Also print void
fractions P(H=0).  By Lemma 8.2, classes with l > M0 = 8*floor((N+1)/3)^2
never hit [1,N].

Run: uv run --with scipy python scripts/noncrt_interval.py N Ymax [all|nonsquare|prime]
"""
import math
import sys

import numpy as np
from scipy.optimize import linprog


def spf_sieve(m):
    spf = np.zeros(m + 1, dtype=np.int64)
    for i in range(2, int(m ** 0.5) + 1):
        if spf[i] == 0:
            blk = spf[i * i::i]
            blk[blk == 0] = i
    idx = np.nonzero(spf == 0)[0]
    spf[idx] = idx
    return spf


def divisors_of_square(a, spf):
    ds = [1]
    while a > 1:
        p = int(spf[a]); e = 0
        while a % p == 0:
            a //= p; e += 1
        ds = [d * p ** j for d in ds for j in range(2 * e + 1)]
    return ds


def lp_min(w, k, hcap):
    """min sum_h w[h] P(h), deg P <= k, P>=0 on 0..hcap, P(0)>=1. Chebyshev basis."""
    hs = np.arange(hcap + 1)
    t = 2 * hs / hcap - 1
    B = np.polynomial.chebyshev.chebvander(t, k)          # (hcap+1, k+1)
    ww = np.zeros(hcap + 1); ww[:len(w)] = w[:hcap + 1]
    c = ww @ B
    A_ub = np.vstack([-B, -B[0:1]])
    b_ub = np.concatenate([np.zeros(hcap + 1), [-1.0]])
    res = linprog(c, A_ub=A_ub, b_ub=b_ub, bounds=[(None, None)] * (k + 1), method="highs")
    if res.status != 0 or not np.isfinite(res.fun):
        raise RuntimeError(f"LP failed k={k}: {res.message}")
    return res.fun


def main(N, Ymax, mode="all", KMAX=10, HCAP=80):
    M0 = 8 * ((N + 1) // 3) ** 2
    Ymax = min(Ymax, M0)
    spf = spf_sieve((Ymax + 1) // 4 + 1)
    isp = np.ones(Ymax + 1, dtype=bool); isp[:2] = False
    for i in range(2, int(Ymax ** 0.5) + 1):
        if isp[i]:
            isp[i * i::i] = False
    primes = [int(l) for l in np.nonzero(isp)[0] if l % 4 == 3]
    thresholds = sorted({int(round(N ** e)) for e in (0.5, 1.0, 1.5)} | {Ymax})
    thresholds = [y for y in thresholds if y <= Ymax]
    H = np.zeros(N + 1, dtype=np.int64)           # index n = 0..N, use 1..N
    pmf = np.zeros(HCAP + 1); pmf[0] = 1.0
    mass = 0.0; ti = 0; rows = []
    nn = np.arange(N + 1)
    if mode == "all":
        sel = nn >= 1
    elif mode == "nonsquare":
        sel = (nn >= 1) & (np.round(np.sqrt(nn)) ** 2 != nn)
    elif mode == "prime":
        ip = np.ones(N + 1, dtype=bool); ip[:2] = False
        for i in range(2, int(N ** 0.5) + 1):
            if ip[i]:
                ip[i * i::i] = False
        sel = ip
    else:
        raise SystemExit("mode: all | nonsquare | prime")
    nsel = int(sel.sum())
    for l in primes + [Ymax + 10 ** 9]:
        while ti < len(thresholds) and l > thresholds[ti]:
            emp = np.bincount(H[sel], minlength=HCAP + 1)[:HCAP + 1] / nsel
            rows.append((thresholds[ti], mass, emp.copy(), pmf.copy()))
            ti += 1
        if l > Ymax:
            break
        A = (l + 1) // 4
        F = {(-4 * d) % l for d in divisors_of_square(A, spf)}
        p = len(F) / l
        mass += p
        pmf[1:] = pmf[1:] * (1 - p) + pmf[:-1] * p; pmf[0] *= (1 - p)
        if l <= N:
            for r in F:
                H[r::l] += 1
        else:
            for r in F:
                if 1 <= r <= N:
                    H[r] += 1
    print(f"N={N}  mode={mode} ({nsel} integers)  M0={M0}  Ymax={Ymax}  #primes(3 mod 4)<=Ymax: {len(primes)}")
    for Y, mu, emp, crt in rows:
        print(f"\nY={Y}: CRT mass mu={mu:.3f}  E_int H={np.dot(np.arange(HCAP+1), emp):.3f}"
              f"  void int={emp[0]:.5f}  void CRT={crt[0]:.3e}  (exp(-mu)={math.exp(-mu):.3e})")
        print("  k   -log LP_int   -log LP_CRT")
        for k in range(0, KMAX + 1):
            try:
                vi = lp_min(emp, k, HCAP); vc = lp_min(crt, k, HCAP)
            except RuntimeError as e:   # report, do not mask: printed as FAIL row
                print(f"  {k:<3d} LP FAIL ({e})"); continue
            print(f"  {k:<3d} {-math.log(max(vi,1e-300)):10.4f}   {-math.log(max(vc,1e-300)):10.4f}")


if __name__ == "__main__":
    main(int(sys.argv[1]), int(float(sys.argv[2])), sys.argv[3] if len(sys.argv) > 3 else "all")
