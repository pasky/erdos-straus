#!/usr/bin/env python3
"""Numerical check of Z55_TDF Lemma 1 (Farey expansion), Lemma 4 (bound for G) and Theorem LS.

c(m,s) = 1[U^2<m<=4U^2, 2U<s<=4U, s^2-4m>=1] e(h sqrt(s^2-4m)).
T_n(h) = sum_{m,s} c(m,s) 1[n = -s mod m]
Gamma(b/d) = sum_{m = 0 mod d} (1/m) sum_s c(m,s) e(s b/d)          (d <= 4U^2, gcd(b,d)=1)
Lemma 1: T_n(h) = sum_{d<=4U^2} sum*_b e(n b/d) Gamma(b/d).
G := sum_d sum*_b |Gamma(b/d)|^2 ;  Lemma 4: G <= 2700 h^4 U + 32 U log(2U).
Theorem LS: sum_{M<n<=M+N} |T_n(h)|^2 <= (N + 16 U^4) G.
Usage: python z55_tdf_farey_check.py U h N
"""
import sys, math, cmath
import numpy as np
from math import gcd

def main():
    U = int(sys.argv[1]); h = int(sys.argv[2]); N = int(sys.argv[3])
    Q = 4*U*U
    # coefficient table c(m,s)
    ms = []  # (m, s, c)
    for m in range(U*U+1, 4*U*U+1):
        for s in range(2*U+1, 4*U+1):
            D = s*s - 4*m
            if D >= 1:
                ms.append((m, s, cmath.exp(2j*math.pi*h*math.sqrt(D))))
    # Gamma(b/d) for all reduced b/d, d <= Q
    # A_{d,r} = sum_{m=0 (d)} (1/m) sum_{s = r (d)} c(m,s)
    G = 0.0
    gam = {}  # (b,d) -> Gamma
    for d in range(1, Q+1):
        A = np.zeros(d, dtype=complex)
        for (m, s, c) in ms:
            if m % d == 0:
                A[s % d] += c / m
        if not A.any():
            continue
        # Gamma(b/d) = sum_r e(r b/d) A_r  -> DFT
        Gam = np.fft.ifft(A) * d  # ifft gives (1/d) sum_r A_r e(+2pi i r b/d)
        for b in range(d):
            if gcd(b, d) == 1:
                gam[(b, d)] = Gam[b]
                G += abs(Gam[b])**2
    bound = 2700*h**4*U + 32*U*math.log(2*U)
    print(f"U={U} h={h}: #coeffs={len(ms)}  G={G:.4f}  Lemma4 bound={bound:.1f}  ratio={G/bound:.2e}")
    # Lemma 1 check at a few n, and Theorem LS
    def T_direct(n):
        return sum(c for (m, s, c) in ms if (-n) % m == s)
    def T_farey(n):
        return sum(g * cmath.exp(2j*math.pi*n*b/d) for (b, d), g in gam.items())
    maxerr = 0.0
    for n in (U**4, U**4 + 7, 3*U**4 + 1, 16*U**4 - 3):
        a = T_direct(n); f = T_farey(n)
        maxerr = max(maxerr, abs(a - f))
    print(f"Lemma 1 max |T_direct - T_farey| over 4 test n: {maxerr:.2e}")
    M = U**4
    S = sum(abs(T_direct(n))**2 for n in range(M+1, M+N+1))
    print(f"Theorem LS: sum_(M<n<=M+N)|T_n|^2 = {S:.2f}  <=  (N+16U^4) G = {(N+16*U**4)*G:.2f}   ratio={S/((N+16*U**4)*G):.3e}")
    print(f"  (mean |T_n|^2 = {S/N:.3f}, mean |E1+| = {sum(1 for n in range(M+1,M+N+1) for (m,s,c) in ms if (-n)%m==s)/N:.3f})")

if __name__ == '__main__':
    main()
