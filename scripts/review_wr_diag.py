"""R164 from-scratch check of WINDMILL_REDUCTION §7(ii): diagonal Type II  p = k^2 - 4 g b^2, 4gb | k+1.
Counts primes p = 1 (24) < N with no diagonal certificate; T1 control on odd squares n = m^2 (coprime: gcd(m, k g b) = 1);
also checks the k-range and that p > 4g (= disc/4), i.e. p is never a river face of x^2 - 4g y^2.
"""
import sys
from math import isqrt, gcd
from review_wr_zagier import primes


def diag_certs(n):
    out = []
    k = isqrt(n) + 1
    while 3 * k * k - 2 * k - 1 <= 4 * n:   # (k+1)^2 >= 4(k^2 - n) necessary
        M = k * k - n
        if M % 4 == 0:
            m4 = M // 4
            b = 1
            while b * b <= m4:
                if m4 % (b * b) == 0:
                    g = m4 // (b * b)
                    if (k + 1) % (4 * g * b) == 0:
                        out.append((k, g, b))
                b += 1
        k += 1
    # sanity: no solution beyond the range
    for kk in range(k, k + 50):
        M = kk * kk - n
        if M % 4 == 0:
            m4 = M // 4
            for b in range(1, isqrt(m4) + 1):
                if m4 % (b * b) == 0 and (kk + 1) % (4 * (m4 // (b * b)) * b) == 0:
                    raise AssertionError((n, kk, b))
    return out


if __name__ == "__main__":
    N = int(sys.argv[1])
    P = [p for p in primes(N) if p % 24 == 1]
    no = 0; facebad = 0
    for p in P:
        cs = diag_certs(p)
        no += not cs
        facebad += any(p <= 4 * g for (k, g, b) in cs)
    print(f"{len(P)} primes p=1(24) < {N}: no diagonal certificate for {no}; certs with p <= 4g: {facebad}")
    sq = [m for m in range(3, isqrt(N) + 1, 2) if any(gcd(m, k * g * b) == 1 for (k, g, b) in diag_certs(m * m))]
    print("odd squares < N with a coprime diagonal certificate:", sq)
