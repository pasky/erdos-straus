"""KARY2 numerics (EVIDENCE only).

(1) Lemma 3.4: tau(n) <= 8 * max_{d|n, d<=n^{1/4}} tau(d)^7 for all n <= NMAX
    (asserted); also reports the smallest exponent e with
    tau(n) <= 8 * max tau(d)^e that would have sufficed.
(2) Remark 3.8: truncated smooth first moment of R(M) classes,
    S(y, X) = sum_{M<=X, M=3 (4), P(M)<=y} tau(A_M^2)/M, against (log y)^3,
    for X = XMAX/10 and XMAX (stability in X shows the tail is small).
Usage: python kary2_moments.py [NMAX XMAX]
"""
import sys, math
import numpy as np

def tau_array(n):
    t = np.zeros(n + 1, dtype=np.int64)
    for d in range(1, n + 1):
        t[d::d] += 1
    return t

def lpf_array(n):
    """largest prime factor"""
    P = np.zeros(n + 1, dtype=np.int32)
    is_p = np.ones(n + 1, dtype=bool); is_p[:2] = False
    for p in range(2, int(n ** 0.5) + 1):
        if is_p[p]:
            is_p[p * p::p] = False
    for p in np.nonzero(is_p)[0]:
        P[p::p] = p
    return P, is_p

def tau_sq_array(n, is_p):
    """tau(a^2) for a <= n, as float"""
    t = np.ones(n + 1)
    for p in np.nonzero(is_p[:n + 1])[0]:
        q, k = int(p), 1
        while q <= n:
            t[q::q] *= (2 * k + 1) / (2 * k - 1)
            q *= int(p); k += 1
    return t

def main():
    NMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 10 ** 6
    XMAX = int(sys.argv[2]) if len(sys.argv) > 2 else 10 ** 7
    # (1)
    t = tau_array(NMAX)
    best = np.ones(NMAX + 1, dtype=np.int64)
    d = 2
    while d ** 4 <= NMAX:
        idx = np.arange(d, NMAX + 1, d)
        idx = idx[idx >= d ** 4]
        best[idx] = np.maximum(best[idx], t[d])
        d += 1
    ok = t[1:] <= 8 * best[1:] ** 7
    assert ok.all()
    # smallest e that works: tau <= 8*best^e
    need = 0.0
    m = best[1:] > 1
    r = np.log(np.maximum(t[1:] / 8.0, 1.0))
    need = max(need, float((r[m] / np.log(best[1:][m])).max()))
    assert (t[1:][~m] <= 8).all()
    print(f"(1) Lemma 3.4 holds for all n <= {NMAX}; exponent actually needed <= {need:.3f} (lemma: 7)")
    # (2)
    P, is_p = lpf_array(XMAX)
    ts = tau_sq_array(XMAX // 4 + 1, is_p)
    M = np.arange(3, XMAX + 1, 4)
    A = (M + 1) // 4
    w = ts[A] / M
    print(f"(2) S(y,X) = sum_(M<=X, M=3(4), P(M)<=y) tau(A^2)/M")
    print(f"{'y':>6} {'S(y,X/10)':>12} {'S(y,X)':>12} {'(log y)^3':>10} {'S/(log y)^3':>12}")
    for y in [20, 50, 100, 200, 500, 1000, 3000]:
        sel = P[M] <= y
        s_full = w[sel].sum()
        sel10 = sel & (M <= XMAX // 10)
        s_10 = w[sel10].sum()
        L3 = math.log(y) ** 3
        print(f"{y:>6} {s_10:>12.3f} {s_full:>12.3f} {L3:>10.1f} {s_full / L3:>12.4f}")

if __name__ == "__main__":
    main()
