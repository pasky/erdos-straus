"""Cross-check of z52_bank_i3c.c on p < 3*10^4 by a different enumeration (loop over t,u; v from the equation),
and conversion of interior certifying words into explicit 4/p identities via the five slot formulas."""
from fractions import Fraction as Fr
from sympy import primerange
def inC(x, p): return x % 4 == 0 or (x + p) % 8 == 0
def words(p):
    out = []
    for t in range(3, p + 1):
        if 9 * t - 6 > p: break           # t*u*v - u - v >= 9t - 6 when u, v >= 3
        for u in range(3, p + 1):
            A = t * u - 1
            if 3 * A - u > p: break       # v >= 3
            if (p + u) % A == 0:
                v = (p + u) // A
                if v >= 3: out.append((t, u, v))
    return out
def slot_identity(p, t, u, v):
    A, As = t * u - 1, t * v - 1
    if t % 4 == 0: s = t // 4; return (s*u*v, p*s*u, p*s*v)
    if v % 4 == 0: w = v // 4; return (w*A, p*w*t, p*w*t*A)
    if u % 4 == 0: w = u // 4; return (w*As, p*w*t, p*w*t*As)
    if A % 4 == 0: a = A // 4; return (a*v, a*v*As, p*a*As)
    if As % 4 == 0: a = As // 4; return (a*u, a*u*A, p*a*A)
    return None
zeros = []; nid = 0
for p in primerange(5, 30000):
    if p % 4 != 1: continue
    W = [w for w in words(p) if any(inC(c, p) for c in w)]
    if not W: zeros.append(p); continue
    for (t, u, v) in W[:3]:
        xyz = slot_identity(p, t, u, v)
        assert xyz is not None, (p, t, u, v)      # LOWERTAIL Thm 1: coordinate in C_p => a slot is 0 mod 4
        assert Fr(4, p) == sum(Fr(1, c) for c in xyz), (p, t, u, v, xyz)
        nid += 1
print('I3_C zeros p < 30000 (python):', zeros, '; identities verified:', nid)
