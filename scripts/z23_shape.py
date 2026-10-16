"""O251: does the d-shape Type II line fire?  For prime p = 1 (4) <= P, find the least k such that
4 k^2 d p + 1 has a divisor g = -1 (mod 4k) (then the cofactor is also = -1 mod 4k... only for d = 1; for general d
the certificate is FIXED_MODULUS_SHOTS Lemma 1.1 with c arbitrary: g = 4cdj - 1 | 4 d j^2 p + 1).
Here: d = 1 shape (ASTRA_BRIDGE Thm 3.4 (c)): g | 4k^2 p + 1, 4k | g + 1.  Report primes with no k <= KM,
and the distribution of the least k.  Odd squares as T1 control (must all fail).
Usage: z23_shape.py P KM
"""
import sys
import numpy as np
from sympy import primerange
from math import isqrt


def least_k(n, KM):
    for k in range(1, KM + 1):
        N = 4 * k * k * n + 1
        J = (isqrt(N) + 1) // (4 * k) + 1
        g = 4 * k * np.arange(1, J + 1, dtype=np.int64) - 1
        if np.any(N % g == 0):
            return k
    return None


if __name__ == "__main__":
    P, KM = int(sys.argv[1]), int(sys.argv[2])
    fails, hist = [], {}
    for p in primerange(5, P + 1):
        if p % 4 != 1:
            continue
        k = least_k(p, KM)
        if k is None:
            fails.append(p)
        else:
            hist[k] = hist.get(k, 0) + 1
    print('primes: fails (no k<=%d):' % KM, len(fails), fails[:30])
    print('least-k histogram (top):', sorted(hist.items())[:12], 'max k', max(hist))
    t1 = [a * a for a in range(3, isqrt(P) + 1, 2) if least_k(a * a, KM) is not None]
    print('odd squares that fire (must be none):', t1)
