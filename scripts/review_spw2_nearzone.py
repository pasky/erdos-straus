"""R53 from-scratch checks: SPW2 Lemma 2.2 (near zone invisible) and the
IF2 Lemma 9.3 remark ('disappears once K >= 3/2').  Exact integer arithmetic."""
from fractions import Fraction as Fr
import math, sys

def check_22(N, C):
    # all moduli e > CN (up to a cutoff), all n0 in [1,N]: points n0 + j e in Z?
    lo, hi = N - C*N, C*N + 1
    emin = math.floor(C*N) + 1
    bad = 0
    for e in range(emin, emin + 3*N):
        for n0 in range(1, N+1):
            for j in (-3, -2, -1, 1, 2, 3):
                x = n0 + j*e
                if (lo <= x <= 0) or (N+1 <= x <= hi):
                    bad += 1
    return bad

def worst_93(N, C):
    # class b mod q (q <= D) with c = c(b,q) points in [1,N], k = floor(CN/q)+1 lifts
    # mod kq: c full lifts, k-c sparse.  RSPW-feasibility of this local system at eta=1
    # needs (k-c)K >= c*eta. Return max over q,b of c/(k-c).
    D = N//2; w = Fr(0); arg = None
    for q in range(1, D+1):
        k = math.floor(C*N/q) + 1
        for b in range(1, q+1):
            c = (N - b)//q + 1
            full = sum(1 for j in range(k) if 1 <= b + j*q <= N)
            assert full == c and k*q > C*N
            if k - c <= 0:
                return None, (q, b)
            r = Fr(c, k - c)
            if r > w: w, arg = r, (q, b, c, k)
    return w, arg

if __name__ == "__main__":
    for C in (Fr(3,2), Fr(2), Fr(5,2), Fr(3)):
        for N in (5, 12, 13, 30, 31, 57):
            assert check_22(N, C) == 0, (N, C)
    print("Lemma 2.2: no class of modulus e>CN through [1,N] meets Z (C in 1.5..3, N<=57)")
    for C in (Fr(3,2), Fr(2), Fr(3)):
        print("C =", C, [(N, str(worst_93(N, C)[0]), worst_93(N, C)[1]) for N in (12, 30, 60, 101, 200)])
