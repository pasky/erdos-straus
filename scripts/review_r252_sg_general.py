"""R252: SG window menu at mu = 0 of c*2^s+1 (c+1 = 4^i) with GENERAL constant factor lambda.

Window m = 4ct^4 - 1 (j = 2), X = 2^{(s-4)/4} -> rho = 1/2 at odd places, 0 at 2.
K = c(4X^4 + t^4) = c f+ f-, f± = 2X^2 ± 2tX + t^2;  f±(1/2) = g±/2, g± = 2t^2 ± 2t + 1.
Window rule: d = lambda f+^x f-^y (lambda in Q_{>0}), d | K^2 on the class, m | K + d.
Near mu = 0: d -> D * 2^{-(x+y)} with D an (odd) divisor of (c g+ g-)^2 (any such D is realisable on a
neighbourhood of mu = 0 by choosing lambda with q-adic support on primes of c g+ g- and the class modulus
fixing X mod q^k). Firing condition: D == -4^{i-1} 2^{x+y} (mod m), x+y in {1,3} (Prop 4.1: v2 odd) --
we test x+y in {0..4} anyway.
The author's Prop 4.3 menu only allows lambda supported on primes of c (D = c-part * g+^x g-^y).
"""
import sys
from sympy import factorint, divisors
from math import gcd

c = int(sys.argv[1]); T = int(sys.argv[2])
i = 0
while 4**i < c + 1:
    i += 1
assert 4**i == c + 1
for t in range(1, T + 1):
    m = 4*c*t**4 - 1
    if gcd(m, 2*c) != 1:
        continue
    gp, gm = 2*t*t + 2*t + 1, 2*t*t - 2*t + 1
    F = factorint(c*c*gp*gp*gm*gm)
    divs = [1]
    for q, e in F.items():
        divs = [d*q**k for d in divs for k in range(e + 1)]
    hits = []
    for e2 in range(0, 5):
        target = (-pow(4, i - 1, m) * pow(2, e2, m)) % m
        for D in divs:
            if D % m == target:
                # check whether D is of the author's restricted form c_part * gp^x gm^y with x+y = e2
                restricted = any(
                    D % (gp**x * gm**y) == 0 and all(p in factorint(c) for p in factorint(D // (gp**x * gm**y)))
                    and (c*c) % (D // (gp**x * gm**y)) == 0
                    for x in range(3) for y in range(3) if x + y == e2)
                hits.append((e2, D, 'restricted' if restricted else 'GENERAL'))
    if hits:
        print(f"c={c} t={t} m={m} g+={gp} g-={gm}: {hits[:6]}")
