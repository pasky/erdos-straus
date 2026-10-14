"""y6_fibres.py — which fibres x (odd, 3 <= x <= X, gcd(x, n) = 1) of W_n carry a point with c = x/E >= 3?
f_x(a, B) = 4na^2 - x aB + B^2 = -E, E | x, E = 3 mod 4. Since E <= x/3 < sqrt(x^2 - 16n)/2 (x large enough), every
primitive representation of -E/h^2 is a convergent value of a root of f_x (Lagrange), so we scan one full period of the
continued fractions of both roots omega = (x + sqrt D)/2, omega' = (x - sqrt D)/2 (D = x^2 - 16n, non-square) and
record values m < 0 with h^2|m| = E | x, E = 3 mod 4, x/E >= 3 (side conditions of Thm 1.1 on (a, B) ignored).
Usage: y6_fibres.py X n1 n2 ..."""
import sys
from math import isqrt, gcd
X = int(sys.argv[1])
def cf_values(P, Q, d, f):
    # convergents of (P + sqrt d)/Q, Q | d - P^2 (sign of Q arbitrary); yield f(q_k, p_k) over one period (+ preperiod)
    seen = set(); p0, p1, q0, q1 = 0, 1, 1, 0; s = isqrt(d)
    for _ in range(10**6):
        a = (P + s)//Q if Q > 0 else (P + s + 1)//Q   # floor((P+sqrt d)/Q), d non-square
        p0, p1 = p1, a*p1 + p0; q0, q1 = q1, a*q1 + q0
        yield f(q1, p1)
        P = a*Q - P; Q = (d - P*P)//Q
        if (P, Q) in seen: return
        seen.add((P, Q))
for n in map(int, sys.argv[2:]):
    good = []
    for x in range(3, X+1, 2):
        if gcd(x, n) != 1: continue
        d = x*x - 16*n
        if d <= 0 or isqrt(d)**2 == d: continue
        f = lambda a, B: 4*n*a*a - x*a*B + B*B
        Es = set()
        for (P, Q) in ((x, 2), (-x, -2)):   # omega and omega' = (x - sqrt d)/2 -> (-x + sqrt d)/(-2)
            for m in cf_values(P, Q, d, f):
                if m < 0:
                    for h in range(1, isqrt(x) + 1):
                        E = -m*h*h
                        if E > x: break
                        if x % E == 0 and E % 4 == 3 and x//E >= 3: Es.add(E)
        if Es: good.append((x, sorted(Es)))
    print(f"n={n}: fibres x<={X} with a c>=3 point: {len(good)}; first: {good[:12]}")
    import collections
    print("   per octave of x:", dict(collections.Counter(x.bit_length() for x, _ in good)))
