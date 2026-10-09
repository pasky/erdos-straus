"""O99 (POINTWISE_TYPEI6.md, Prop 2.1 check): CF period length of sqrt(d), d = c_o(c_o*delta^2 + T),
along delta in an arithmetic progression; L <= 6 bounded (Richaud-Degert), L >= 7 growing (Schinzel)."""
from math import isqrt
def period(d):
    a0 = isqrt(d); m, q, a, n = 0, 1, a0, 0
    while True:
        m = a*q - m; q = (d - m*m)//q; a = (a0 + m)//q; n += 1
        if a == 2*a0: return n
for L in (5, 6, 7, 8, 10):
    T = 2**(L-4)
    for co in (7, 21):
        ps = [period(co*(co*dl*dl + T)) for dl in range(1, 4002, 2) if isqrt(co*(co*dl*dl+T))**2 != co*(co*dl*dl+T)]
        print(f"L={L} c_o={co}: max period over delta<1000 / delta<4002 (odd): {max(ps[:500])} / {max(ps)}")
