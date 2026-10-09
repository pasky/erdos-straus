"""O109 (POINTWISE_TYPEI7.md Thm 2.1): build the explicit fibre certificates with v_2(F+9) >= m,
F = 7^s + 2^i, c' = (F+1)/8, c_o = 7c', k_o = 7^b, L = 1 - i mod ord_F(2), and verify each with the
independent stand-alone checker typei3_verify.check (split gamma = floor(L/2), alpha = L mod 2, plus one other split).
Usage: typei7_unbounded.py MMAX"""
import sys
from sympy.ntheory import n_order
from typei3_verify import check


def v2(x):
    return (x & -x).bit_length() - 1


MMAX = int(sys.argv[1])
for m in range(4, MMAX + 1):
    s = next(s for s in range(1, 2**m, 2) if (pow(7, s, 2**m) + 9) % 2**m == 0)
    b = (s - 1) // 2
    step = 3 * 7**b
    i = step * ((m + step - 1) // step)
    F = 7**s + 2**i
    cp = (F + 1) // 8
    o = n_order(2, F)
    L = (1 - i) % o
    while L < 7:
        L += o
    for (al, ga) in ((L % 2, L // 2), (L % 2 + 2, L // 2 - 1)):
        c, k = 2**al * 7 * cp, 2**ga * 7**b
        w = -F % 2**(2 + al + ga)
        ok, info = check(7, w, c, k, F)
        assert all(ok.values()), (m, ok)
    print(f"m={m} s={s} b={b} i={i} F={F} v2(F+9)={v2(F+9)} ord_F(2)={o} L={L} t_min={2+(L+1)//2} OK")
