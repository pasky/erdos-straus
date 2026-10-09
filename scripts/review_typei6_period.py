"""R99: independent CF-period check for Prop 2.1(c): d = c_o(c_o delta^2 + T), c_o = 7."""
from math import isqrt
def period(d):
    a0 = isqrt(d); m, q, a, n = 0, 1, a0, 0
    while True:
        m = a*q - m; q = (d - m*m)//q; a = (a0 + m)//q; n += 1
        if a == 2*a0: return n
for L in (5, 6, 7, 8):
    T = 2**(L-4); co = 7
    out = []
    for lo, hi in ((1, 101), (101, 401), (401, 1201)):
        out.append(max(period(co*(co*de*de+T)) for de in range(lo, hi, 2)))
    print(f"L={L}: max period for odd delta in [1,101),[101,401),[401,1201): {out}")
