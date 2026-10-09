"""R111 from-scratch check of Prop 7.1 ((K_a), fixed a):
S_a(q) = sum_{e,f>=1, ef = 1 (m), q | n} W1(e/E) W2(d/D),  m = 4a^2, d = (ef-1)/m, n = 4acd - f,
vs g'(q) S_a(1), g'(l) = (l-1)/l^2 (l∤c), 1/l (l|c).  Claimed error O(L^C tau(a)^C q a) + rel. O(1/E+1/F).
"""
import sys, math
import numpy as np

def bump(x):
    # smooth bump supported on (1,2)
    out = np.zeros_like(x, dtype=float)
    m = (x > 1) & (x < 2)
    t = x[m]
    out[m] = np.exp(4.0 - 1.0/((t-1)*(2-t)))   # max 1
    return out

def S(a, c, E, D, qs):
    m = 4*a*a
    res = {q: 0.0 for q in (1,) + tuple(qs)}
    for e in range(max(1, E), 2*E + 1):
        if math.gcd(e, m) != 1: continue
        w1 = bump(np.array([e/E]))[0]
        if w1 == 0: continue
        f0 = pow(e, -1, m)
        # d in (D, 2D): f in ((mD+1)/e, (2mD+1)/e)
        lo = (m*D + 1)//e; hi = (2*m*D + 1)//e + 1
        k0 = (lo - f0)//m
        f = f0 + m*np.arange(k0, (hi - f0)//m + 2, dtype=np.int64)
        f = f[(f >= 1)]
        d = (e*f - 1)//m
        w = w1*bump(d/D)
        n = 4*a*c*d - f
        for q in res:
            res[q] += w[(n % q) == 0].sum() if q > 1 else w.sum()
    return res

def gp(q, c):
    out = 1.0
    for l in [p for p in range(2, q+1) if q % p == 0 and all(p % r for r in range(2, int(p**.5)+1))]:
        out *= 1/l if c % l == 0 else (l-1)/l**2
    return out

if __name__ == "__main__":
    qs = (5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41)
    for (a, c, E, D) in [(3, 1, 3000, 200000), (3, 5, 3000, 200000), (7, 1, 400, 200000),
                         (7, 1, 30000, 20000), (10, 1, 2000, 100000), (1, 1, 3, 100000)]:
        if math.gcd(a, 2) != 1 and False: pass
        r = S(a, c, E, D, qs)
        F = 4*a*a*D/E
        print(f"a={a} c={c} E={E} D={D} F~{F:.0f} m={4*a*a}  S(1)={r[1]:.1f}")
        print("   " + "  ".join(f"q={q}: dev={(r[q]-gp(q,c)*r[1]):+.1f} (dev/(q a)={(r[q]-gp(q,c)*r[1])/(q*a):+.2f})"
                             for q in qs if math.gcd(q, 2*a) == 1))
