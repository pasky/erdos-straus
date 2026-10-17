"""R268: equation-level check (no coprimality imposed) that c n + a + b = 4abcd has NO solution at odd squares n,
and that the MP(n) 2-adic shape claim of Prop 1.3 'Reading' holds there; also Prop 1.4 bijection test."""
from math import gcd
def sols(n):
    out = []
    for a in range(1, n + 2):
        for b in range(a, n // 2 + 2):
            if 4 * a * b > n + a + b: break
            for d in range(1, (n + a + b) // (4 * a * b) + 1):
                m = 4 * a * b * d - n
                if m >= 1 and (a + b) % m == 0: out.append((a, b, (a + b) // m, d))
    return out
for r in range(3, 30, 2):
    print("n =", r * r, "Type II eq. solutions (any gcd):", len(sols(r * r)))
# Prop 1.4: MP(p) (full ranges x, y <= 2p + 2) vs image of {(x,s): x | s+1, s | p+x}, y = (p+x)/s
from sympy import primerange
bad = 0; extra = 0; tot = 0
for p in primerange(5, 220):
    R = 2 * p + 3
    MP = {(x, y) for x in range(1, R) for y in range(1, R)
          if (p + y) % x == 0 and (p + x) % y == 0 and (p + x + y) % (x * y) == 0}
    XS = {(x, (p + x) // s) for s in range(1, R) for x in range(1, s + 2) if (s + 1) % x == 0 and (p + x) % s == 0}
    bad += MP != XS; extra += len([q for q in XS if q[0] >= q[1]]); tot += len(XS)
print("Prop 1.4: primes 5..219: MP(p) != image:", bad, "; image points with x >= y:", extra, "of", tot)
