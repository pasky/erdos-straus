"""R89: is the certificate unit eps = A + 8k_o sqrt(d) the fundamental unit?  For each HIT line of
review_typei4_jsearch, compute d, A, and (from scratch, continued fractions) the fundamental solution of
x^2 - d y^2 = +-1 (unit of Z[sqrt d]).
Report the exponent m with eps = eta^m.  Usage: cat hits | python3 scripts/review_typei4_fundunit.py"""
import sys
from math import isqrt
def fund(D, rhs_set):
    # smallest x+y sqrt(D) > 1 with x^2 - D y^2 in rhs_set, via CF of sqrt(D) (rhs +-1) -- brute small for +-4
    a0 = isqrt(D); m, dd, a = 0, 1, a0
    p0, p1, q0, q1 = 1, a0, 0, 1
    while p1 * p1 - D * q1 * q1 not in rhs_set:
        m = dd * a - m; dd = (D - m * m) // dd; a = (a0 + m) // dd
        p0, p1 = p1, a * p1 + p0; q0, q1 = q1, a * q1 + q0
    return p1, q1
# d = 1 mod 8 (L>=7): 2 splits, so Z[sqrt d] has unit index 1 in O_K; eta is also the O_K fundamental unit.
for line in sys.stdin:
    if not line.startswith("HIT"): continue
    d_ = dict(kv.split("=") for kv in line.split()[1:])
    L, a, b, c, k, F, e = (int(d_[x]) for x in ("L", "a", "b", "c'", "k'", "F", "e"))
    co, ko = 7 ** a * c, 7 ** b * k
    delta = (e - F) // (16 * co * ko)
    d = co * (co * delta ** 2 + 2 ** (L - 4))
    A, B = (F + e) // 2, 8 * ko
    assert A * A - d * B * B == 1
    x, y = fund(d, {1, -1})
    nrm = x * x - d * y * y
    # exponent: multiply eta until reaching (A,B)
    m, X, Y = 1, x, y
    while (X, Y) != (A, B) and X <= A:
        X, Y = X * x + d * Y * y, X * y + Y * x; m += 1
    print(f"L={L} a={a} b={b} d={d} d%8={d%8} norm(eta)={nrm} eps=eta^{m if (X,Y)==(A,B) else '?'}")
