"""O109 (POINTWISE_TYPEI7.md Thm 2.4): certificates F = 71^e, c = 2^alpha*7*(F+1)/8, k = 2^gamma approximating x̂_9.
For m = 4..MMAX: least odd e with 71^e = -9 (mod 2^m); least L >= 7 with 7*2^(L-1) = -1 (mod 71^e) (discrete log,
Pohlig-Hellman via sympy); verify F | N = 1 + 2^(L+2)*7*c' by modular exponentiation, the congruences of TYPEI2 (2.2),
and report v_2(F+9) (>= m) versus t_min = 2 + ceil(L/2) (the certificate is at x̂_9 iff v_2(F+9) >= t for its split).
Usage: typei7_dense71.py MMAX"""
import sys
from sympy.ntheory import discrete_log


def v2(x):
    return (x & -x).bit_length() - 1


MMAX = int(sys.argv[1])
for m in range(4, MMAX + 1):
    e = next(e for e in range(1, 2**m, 2) if (pow(71, e, 2**m) + 9) % 2**m == 0)
    F = 71**e
    cp = (F + 1) // 8
    assert (F + 1) % 8 == 0 and cp % 2 == 1 and cp % 7 != 0 and (F - 1) % 7 == 0
    target = (-pow(7, -1, F)) % F
    o = 35 * 71**(e - 1)
    assert pow(2, o, F) == 1
    j = discrete_log(F, target, 2)          # 2^j = -1/7 (mod F)
    L = (j + 1) % o
    while L < 7:
        L += o
    assert (1 + pow(2, L + 2, F) * 7 * cp) % F == 0          # F | N
    assert (F + 1) % cp == 0 and (F - 1) % 7 == 0               # F = -1 mod c'k', F = 1 mod 7^{v_7(ck)}
    tmin = 2 + (L + 1) // 2
    print(f"m={m} e={e} F=71^{e} ({F.bit_length()} bits) v2(F+9)={v2(F+9)} v2(9F+1)={v2(9*F+1)} "
          f"L={L if L < 10**12 else '~2^%d' % L.bit_length()} t_min={'%d' % tmin if L < 10**12 else '~2^%d' % (tmin.bit_length())} "
          f"at_x9={v2(F+9) >= tmin}", flush=True)
