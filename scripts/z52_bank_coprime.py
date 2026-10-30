"""§1(d): (i) N-points of V_I(n) = {4abd = ne+1, a+b = ce}, V_II(n) = {4abd = n+e, a+b = ce} (no coprimality) at the four
coprime-SQ zeros; (ii) all words (t,u,v) of n = 3985 with a slot (4 | t,u,v,A,A*) and gcd(uv, n);
(iii) the coprime Type I solution of 4/3985 from (a,b,c,d,e) = (2,67,3,171,23)."""
from fractions import Fraction as Fr
from math import gcd
def V_points(n, lim):
    out = []
    for a in range(1, lim):
        for d in range(1, lim):
            if 4 * a * d > 4 * n: break
            for b in range(a, 40 * lim):
                P = 4 * a * b * d
                if P - n > a + b: break
                e = P - n                      # V_II
                if e >= 1 and (a + b) % e == 0:
                    c = (a + b) // e; out.append(('II', a, b, c, d, e))
                if (P - 1) % n == 0:           # V_I
                    e = (P - 1) // n
                    if e >= 1 and (a + b) % e == 0:
                        c = (a + b) // e; out.append(('I', a, b, c, d, e))
    return out
for n in (105, 345, 561, 5985):
    pts = V_points(n, 60)
    T, a, b, c, d, e = pts[0]
    sol = (a*b*d*n, a*c*d, b*c*d) if T == 'I' else (a*b*d, a*c*d*n, b*c*d*n)
    assert Fr(4, n) == sum(Fr(1, s) for s in sol)
    print(f'n={n}: {len(pts)} N-points found (search box); first {T}{(a,b,c,d,e)} -> 4/{n} = ' + ' + '.join(f'1/{s}' for s in sol),
          '; gcd(n, coords) =', [gcd(n, s) for s in sol])
n = 3985
W = []
for u in range(1, 200):
    for A in range(1, n + u + 1):
        if (n + u) % A or (A + 1) % u: continue
        t, v = (A + 1) // u, (n + u) // A
        if v < u: continue
        As = t * v - 1
        if any(s % 4 == 0 for s in (t, u, v, A, As)): W.append((t, u, v, gcd(u * v, n)))
print('n=3985 five-slot words (u<=v):', W)
a, b, c, d, e = 2, 67, 3, 171, 23
assert 4 * a * b * d == n * e + 1 and a + b == c * e
x, y, z = a*b*d*n, a*c*d, b*c*d
print('coprime Type I at 3985:', (x, y, z), Fr(4, n) == Fr(1, x) + Fr(1, y) + Fr(1, z), 'gcd(n,yz)=', gcd(n, y*z))
