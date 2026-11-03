#!/usr/bin/env python3
"""z55 TDF numerics.

T_n(h) := sum_{(k,m): n+2U < km <= n+4U, U^2 < m <= 4U^2, (km-n)^2-4m >= 1} e(h sqrt((km-n)^2-4m)).

Equivalently, with s := (-n) mod m, the sum over m in (U^2, 4U^2] with 2U < s <= 4U and s^2-4m >= 1
of e(h sqrt(s^2-4m)). (For each m at most one s, since m > 2U.)

Modes:
  point  : |T_n(h)| for a few primes n ~ U^4 and h=1..H, compared with sqrt(|E1+|).
  meansq : (1/#n) sum_n |T_n(h)|^2 over n in an interval, all integers and primes separately,
           compared with the large-sieve bound (N+16U^4)*G/N and with |E1+| (square-root size).
Usage: python z55_tdf_numerics.py point U H ;  python z55_tdf_numerics.py meansq U H N0 N
"""
import sys, math
import numpy as np

def T_all(n, U, H):
    m = np.arange(U*U+1, 4*U*U+1, dtype=np.int64)
    s = (-n) % m
    mask = (s > 2*U) & (s <= 4*U)
    m = m[mask]; s = s[mask]
    D = s*s - 4*m
    mask2 = D >= 1
    D = D[mask2]
    w = np.sqrt(D.astype(np.float64))
    E1 = int(mask.sum()); E1p = int(mask2.sum())
    out = []
    for h in range(1, H+1):
        z = np.exp(2j*np.pi*h*w).sum()
        out.append(z)
    return E1, E1p, out

def isprime(n):
    if n < 2: return False
    if n % 2 == 0: return n == 2
    r = int(math.isqrt(n))
    for q in range(3, r+1, 2):
        if n % q == 0: return False
    return True

def main():
    mode = sys.argv[1]; U = int(sys.argv[2]); H = int(sys.argv[3])
    if mode == 'point':
        # primes near U^4 * c for a few c in [1, 16] (fourth-root range)
        for c in (1.0, 2.5, 6.0, 16.0):
            n = int(c*U**4) | 1
            while not isprime(n): n += 2
            E1, E1p, Ts = T_all(n, U, H)
            print(f"p={n} U={U} |E1|={E1} |E1+|={E1p} sqrt(E1+)={math.sqrt(E1p):.1f}")
            print("   |T(h)| h=1..:", " ".join(f"{abs(z):.1f}" for z in Ts))
    elif mode == 'meansq':
        N0 = int(sys.argv[4]); N = int(sys.argv[5])
        acc = np.zeros(H); accp = np.zeros(H); cnt = 0; cntp = 0; E1sum = 0; E1psum = 0
        for n in range(N0+1, N0+N+1):
            E1, E1p, Ts = T_all(n, U, H)
            a = np.array([abs(z)**2 for z in Ts])
            acc += a; cnt += 1; E1sum += E1; E1psum += E1p
            if isprime(n):
                accp += a; cntp += 1
        print(f"U={U} N0={N0} N={N} #n={cnt} #primes={cntp} mean|E1|={E1sum/cnt:.2f} mean|E1+|={E1psum/cnt:.2f}")
        print("mean_n |T_n(h)|^2      :", " ".join(f"{x:.1f}" for x in acc/cnt))
        if cntp:
            print("mean_p |T_p(h)|^2 (p) :", " ".join(f"{x:.1f}" for x in accp/cntp))
        print(f"large-sieve bound factor (N+16U^4)/N = {(N+16*U**4)/N:.2f}; 2U log4 = {2*U*math.log(4):.1f}")

if __name__ == '__main__':
    main()
