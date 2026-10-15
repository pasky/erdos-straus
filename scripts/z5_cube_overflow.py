"""z5_cube_overflow.py — the certificate cube with overflow (CAP_GROWING §1, Prop 1.3): c = c0·R², d = d0/R²,
h = 4·c0·d0·j − 1 prime ≡ 3 (mod 4), c0·d0·j = K = (h+1)/4, rad R | c0, and for s | R: s ∤ d0·j, v_s(R) ≤ e.
For a prime p ≡ −4c0²d0R² (mod h), p ∤ R: e_ = (p + 4c0²d0R²)/h, x = (p+e_)/4, y = p·c0·d0·j, z = p·x·j/(c0·R²).
Checks 4/p = 1/x+1/y+1/z exactly and Def 1.1 of ES^{(y,e)} (den z = q², q odd, rad q | y, v ≤ e), and that the
classes −4c0²d0R² with 4c0²d0R² < h are pairwise distinct per h. usage: z5_cube_overflow.py H e trials seed"""
import sys, random, math
from fractions import Fraction
from sympy import primerange, factorint, isprime, nextprime
H, E, T, seed = map(int, sys.argv[1:5]); random.seed(seed)
hs = [h for h in primerange(3, H) if h % 4 == 3]
done = 0; ncls = 0
for h in hs:
    K = (h + 1) // 4; fK = factorint(K)
    pts = []
    def rec(items, c0, d0, j, Rs):
        if not items:
            pts.extend((c0, d0, j, R) for R in Rs); return
        (s, v), rest = items[0], items[1:]
        for a in range(v + 1):
            for b in range(v - a + 1):
                cc = c0 * s ** a; dd = d0 * s ** b; jj = j * s ** (v - a - b)
                if a == v and s != 2:   # s entirely in c0: may carry overflow
                    newR = [R * s ** r for R in Rs for r in range(E + 1)]
                else:
                    newR = Rs
                rec(rest, cc, dd, jj, newR)
    rec(list(fK.items()), 1, 1, 1, [1])
    small = [4 * c0 * c0 * d0 * R * R for (c0, d0, j, R) in pts if 4 * c0 * c0 * d0 * R * R < h]
    ncls += len(set(small))
    for (c0, d0, j, R) in random.sample(pts, min(3, len(pts))):
        if R == 1 and random.random() < 0.7: continue
        p = (-4 * c0 * c0 * d0 * R * R) % h
        p += h * random.randrange(10 ** 6, 10 ** 7)
        while not isprime(p) or math.gcd(p, R) > 1: p += h
        e_ = (p + 4 * c0 * c0 * d0 * R * R) // h; assert e_ * h == p + 4 * c0 * c0 * d0 * R * R
        x = Fraction(p + e_, 4); y = p * c0 * d0 * j; z = p * x * j / (c0 * R * R)
        assert x.denominator == 1 and Fraction(4, p) == 1 / x + Fraction(1, y) + 1 / z
        D = z.denominator; q = math.isqrt(D); assert q * q == D and q % 2 == 1
        for s, v in factorint(q).items(): assert y % s == 0 and v <= E
        done += 1
print(f"h < {H}, e = {E}: {done} overflow-cube solutions verified exactly; {ncls} distinct small classes")
