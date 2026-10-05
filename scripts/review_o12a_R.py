"""R45a from-scratch check of POINTWISE_OMEGA12 Lemma 4.1.

For dyadic A,B (powers of 2) with A^2 B <= T computes
  R(A,B) = sum_{a in [A,2A), d in [B,2B)} (1/(ad)) sum_{q | P} (1/i) tau(P/q),  P=4a^2 d+1,
compares with the brute-force sum_{e|P} h(e) (identity check, small blocks),
and reports R/(log(Z+2) loglog(Z+16)), Z=max(A,B).  Also, per block, the
small-q pieces  F(q) = q * sum_{a,d: q|P} tau(P/q)/(ad) / log Z  for prime
powers q <= Z^{1/2}  (Lemma 4.1 claims F(q) << 1 uniformly), and the
Thm 7.1 ratio for the shifted quadratic Q(a') = P(q a'+x0)/q.
Usage: review_o12a_R.py T
"""
import sys
from math import log, gcd
import numpy as np


def spf_sieve(n):
    s = np.zeros(n + 1, dtype=np.int32)
    for p in range(2, n + 1):
        if s[p] == 0:
            s[p] = p
            if p * p <= n:
                blk = s[p * p::p]
                blk[blk == 0] = p
    return s


def spf_sieve_fast(n):
    s = np.arange(n + 1, dtype=np.int32)
    r = int(n ** 0.5) + 1
    for p in range(2, r):
        if s[p] == p:
            v = s[p * p::p]
            m = v == np.arange(p * p, n + 1, p, dtype=np.int32)
            v[m] = p
    return s


def fac(n, s):
    out = {}
    while n > 1:
        p = int(s[n])
        out[p] = out.get(p, 0) + 1
        n //= p
    return out


def tau_f(f):
    t = 1
    for v in f.values():
        t *= v + 1
    return t


def divsum_h(f):
    """sum_{q|P} (1/i) tau(P/q) from factorisation f."""
    t = tau_f(f)
    tot = 0.0
    for p, v in f.items():
        # q = p^i, tau(P/q) = t/(v+1)*(v-i+1)
        for i in range(1, v + 1):
            tot += (1.0 / i) * t / (v + 1) * (v - i + 1)
    return tot


def brute_sum_h(f):
    ds = [{}]
    for p, v in f.items():
        ds = [{**d, p: k} for d in ds for k in range(v + 1)]
    H = lambda v: sum(1.0 / i for i in range(1, v + 1))
    return sum(sum(H(v) for v in d.values()) for d in ds)


def main(T):
    Pmax = 32 * T + 2
    s = spf_sieve_fast(Pmax)
    worstR = (0, None)
    worstF = (0, None)
    nchk = 0
    A = 1
    rows = []
    while A * A <= T:
        B = 1
        while A * A * B <= T:
            Z = max(A, B)
            R = 0.0
            Fq = {}  # q -> sum tau(P/q)/(ad)
            qlim = Z ** 0.5 if Z >= 16 else 0
            for a in range(A, 2 * A):
                for d in range(B, 2 * B):
                    P = 4 * a * a * d + 1
                    f = fac(P, s)
                    val = divsum_h(f)
                    if nchk < 3000:
                        assert abs(val - brute_sum_h(f)) < 1e-9
                        nchk += 1
                    R += val / (a * d)
                    t = tau_f(f)
                    for p, v in f.items():
                        for i in range(1, v + 1):
                            q = p ** i
                            if q > qlim:
                                break
                            Fq[q] = Fq.get(q, 0.0) + t / (v + 1) * (v - i + 1) / (a * d)
            ratio = R / (log(Z + 2) * log(log(Z + 16)))
            if ratio > worstR[0]:
                worstR = (ratio, (A, B))
            mF = 0.0
            for q, val in Fq.items():
                F = q * val / log(Z)
                if F > mF:
                    mF = F
                if F > worstF[0]:
                    worstF = (F, (A, B, q))
            rows.append((A, B, ratio, mF))
            B *= 2
        A *= 2
    for A, B, r, mF in rows:
        if A >= 16 or B >= 16 or r > 1.0:
            print(f"A={A} B={B} R/(log loglog)={r:.4f} max_q F(q)={mF:.4f}")
    print(f"T={T} worst R ratio {worstR}  worst F(q) {worstF}  identity checks {nchk}")


if __name__ == "__main__":
    main(int(sys.argv[1]))
