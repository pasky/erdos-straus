#!/usr/bin/env python3
"""z60 DYNAMICS — rates vs target measure on the Kloosterman orbit O_p.

Modes:
  weil p1 p2 ...   : exact Fourier data of the target T_p on F_p^2 (2-D FFT, p <= ~4000):
                     main = (p-1)*hat(0), L1 = sum_{xi != 0} |hat(xi)|, Weil error bound 2*sqrt(p)*L1,
                     exact error = R_o - main, max_{xi!=0}|K(xi)| (Kloosterman), and the Prop 3 threshold
                     |T| >= 2 p^{5/2}/(p-1+2 sqrt p) versus the actual |T|.
  hj n1 n2 ...     : check R_o(n) = #{A in [1,n-1] : n/A has HJ (minus) continued fraction [[c, m, s]] of length 3
                     with c, s >= 2 and 4 | m}   (Farey-point / Hecke-point dictionary, LENGTH_THREE Prop 1.1).
  disc lo hi       : for primes p = 1 (4) in [lo, hi]: D = R_o(p) - (p-1)|T_p|/p^2; prints summary stats
                     (EVIDENCE: the actual discrepancy on T_p is O(log p), far below any proved rate).
"""
import sys
from math import gcd, log, sqrt

sys.path.insert(0, __file__.rsplit('/', 1)[0])
from z60_dynamics_orbit import orbit_hits, target_size  # noqa: E402


def target_array(p):
    import numpy as np
    T = np.zeros((p, p), dtype=np.float64)
    c = 4
    while c <= p - 2:
        x = c - 1
        while x <= p - 1:
            ylo = max(1, -(-(c * p + 1) // x))
            yhi = min(p - 1, ((c + 1) * p) // x)
            if yhi >= ylo:
                T[x, ylo:yhi + 1] = 1.0
            x += c
        c += 4
    return T


def weil(p):
    import numpy as np
    T = target_array(p)
    size = int(T.sum())
    F = np.fft.fft2(T) / p**2          # hat(h,k) = p^-2 sum T(x,y) e(-(hx+ky)/p)
    main = (p - 1) * F[0, 0].real
    L1 = np.abs(F).sum() - abs(F[0, 0])
    Ro = len(orbit_hits(p))
    # Kloosterman sums K(h,1) for h != 0, via FFT over x of e(xbar/p)
    xs = np.arange(1, p)
    xb = np.array([pow(int(x), -1, p) for x in xs])
    v = np.zeros(p, dtype=complex)
    v[xs] = np.exp(2j * np.pi * xb / p)
    K = np.fft.fft(v)                   # K[h] = sum_x e(xbar/p) e(-hx/p) = K(-h,1)
    Kmax = np.abs(K[1:]).max()
    thr = 2 * p**2.5 / (p - 1 + 2 * sqrt(p))
    print(f"p={p} |T|={size} R_o={Ro} main=(p-1)hat0={main:.3f} exact_err={Ro - main:+.3f} "
          f"L1(hat,xi!=0)={L1:.1f} Weil_bound=2sqrt(p)L1={2 * sqrt(p) * L1:.1f} "
          f"ratio_bound/main={2 * sqrt(p) * L1 / main:.1f} max|K(h,1)|/sqrt(p)={Kmax / sqrt(p):.3f} "
          f"Prop3_threshold|T|>={thr:.0f} (actual {size}, ratio {size / thr:.4f})")


def hj(n, A):
    """minus continued fraction n/A = c1 - 1/(c2 - 1/...), all c_i >= 2 for 1 <= A < n."""
    out = []
    a, b = n, A
    while b:
        c = -(-a // b)
        out.append(c)
        a, b = b, c * b - a
    return out


def hjcheck(n):
    cnt = 0
    for A in range(1, n):
        if gcd(A, n) != 1:
            continue
        w = hj(n, A)
        if len(w) == 3 and w[1] % 4 == 0:
            cnt += 1
    Ro = len(orbit_hits(n))
    print(f"n={n} R_o={Ro} HJlen3_mid0mod4={cnt} {'OK' if cnt == Ro else 'FAIL'}")


def isprime(n):
    if n < 2:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True


def disc(lo, hi):
    Ds, Ms = [], []
    for p in range(lo | 1, hi + 1, 2):
        if p % 4 != 1 or not isprime(p):
            continue
        M = (p - 1) * target_size(p) / p**2
        D = len(orbit_hits(p)) - M
        Ds.append(D)
        Ms.append(M)
    k = len(Ds)
    mD = sum(Ds) / k
    sD = sqrt(sum((d - mD) ** 2 for d in Ds) / k)
    mM = sum(Ms) / k
    print(f"primes p=1(4) in [{lo},{hi}]: count={k} mean N*mu={mM:.2f} mean D={mD:+.2f} std D={sD:.2f} "
          f"max|D|={max(abs(d) for d in Ds):.2f} sqrt(N*mu)={sqrt(mM):.2f} sqrt(p)={sqrt(hi):.0f} "
          f"zeros(R_o=0)={sum(1 for d, m in zip(Ds, Ms) if abs(d + m) < 1e-9)}")


if __name__ == "__main__":
    mode = sys.argv[1]
    args = list(map(int, sys.argv[2:]))
    if mode == "weil":
        for p in args:
            weil(p)
    elif mode == "hj":
        for n in args:
            hjcheck(n)
    elif mode == "disc":
        disc(args[0], args[1])
