# O89 (POINTWISE_TYPEI4.md §2): d-graded engine for fibre certificates.
# For level L, c_o = 7^a c' (a odd, c' odd, 7∤c'), delta odd: d = c_o (c_o delta^2 + 2^(L-4)).
# Every fibre certificate with these (L, c_o, delta) is a norm-1 unit A + 8 k_o sqrt(d) of Z[sqrt d]
# (Prop 1.2), i.e. eps^m, eps = fundamental norm-1 unit of Z[sqrt d]. We test m = 1..mmax:
#   8 | B,  k_o = B/8,  A ≡ -1 (mod 32 c' k'),  A ≡ 1 (mod 7^(a+b))   (k' = 7-free part of k_o, b = v_7(k_o)).
# Usage: typei4_dgraded.py Lmin Lmax  CDmax  [mmax]     (all c_o, delta with c_o*delta <= CDmax)
import sys
from math import isqrt

def fund(d):
    a0 = isqrt(d); m, dd, a = 0, 1, a0; p0, p1 = 1, a0; q0, q1 = 0, 1
    while p1 * p1 - d * q1 * q1 not in (1, -1):
        m = dd * a - m; dd = (d - m * m) // dd; a = (a0 + m) // dd
        p0, p1 = p1, a * p1 + p0; q0, q1 = q1, a * q1 + q0
    if p1 * p1 - d * q1 * q1 == -1:
        p1, q1 = p1 * p1 + d * q1 * q1, 2 * p1 * q1
    return p1, q1

def v7(x):
    e = 0
    while x % 7 == 0: x //= 7; e += 1
    return e, x

def run(Lmin, Lmax, CD, mmax=6, out=print):
    hits = []
    for co in range(7, CD + 1, 2):
        a, cp = v7(co)
        if a % 2 == 0: continue
        for dl in range(1, CD // co + 1, 2):
            for L in range(Lmin, Lmax + 1):
                d = co * (co * dl * dl + 2 ** (L - 4))
                A0, B0 = fund(d); A, B = A0, B0
                for m in range(1, mmax + 1):
                    if B % 8 == 0 and (B // 8) % 2 == 1:
                        ko = B // 8; b, kp = v7(ko)
                        if (A + 1) % (32 * cp * kp) == 0 and (A - 1) % 7 ** (a + b) == 0:
                            n = co * ko; F, e = A - 8 * n * dl, A + 8 * n * dl
                            hits.append((L, co, dl, m, ko, F, e)); out(L, co, dl, 'm', m, 'k_o', ko, 'F', F, 'e', e)
                    A, B = A * A0 + d * B * B0, A * B0 + B * A0
    return hits

if __name__ == '__main__':
    Lmin, Lmax, CD = map(int, sys.argv[1:4]); mmax = int(sys.argv[4]) if len(sys.argv) > 4 else 6
    h = run(Lmin, Lmax, CD, mmax)
    print('# hits', len(h))
