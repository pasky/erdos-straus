"""R281 from-scratch checks for EXP_15 §1 (Lemma 1.1, Lemma 1.2, unit-square points of 2^a3^b+1).
Does not import any author script."""
from fractions import Fraction as F
from math import isqrt, gcd
import sympy as sp

X = sp.symbols('X')
n = 48 * X**4 + 1
fp, fm = 2 * X**2 + 2 * X + 1, 2 * X**2 - 2 * X + 1
K = 3 * fp * fm
# Theorem C(a) table: (a,b,c) per s mod 40; X = 2^((s-4)/4)
table = {0: (0, 2, 1), 8: (0, 0, 2), 12: (0, 2, 1), 16: (0, 2, 0), 20: (0, 1, 2), 28: (0, 2, 0), 32: (0, 1, 2), 36: (0, 0, 2)}
assert sp.expand(fp * fm - (4 * X**4 + 1)) == 0
rule_for_class = {}
for s, (a, b, c) in table.items():
    j = ((s - 4) // 4) % 10
    r = pow(2, j, 11)
    d = 3**a * fp**b * fm**c
    x, y, z = K, n * (K + d) / 11, n * K * (K + d) / (11 * d)
    assert sp.simplify(4 / n - 1 / x - 1 / y - 1 / z) == 0
    # integrality on the class X = r mod 11: numerators must be integer polys, and value at X=r divisible by 11
    yn = sp.Poly(sp.expand(n * (K + d)), X)
    zn = sp.cancel(n * K * (K + d) / d)
    zp = sp.Poly(sp.expand(zn), X)  # must be a polynomial
    assert all(cf.is_integer for cf in yn.all_coeffs()) and all(cf.is_integer for cf in zp.all_coeffs())
    assert yn.eval(r) % 11 == 0 and zp.eval(r) % 11 == 0
    rule_for_class[r] = (a, b, c, yn, zp)
    print(f"s≡{s} (40): j≡{j} (10), X≡{r} (11), rule {(a,b,c)}: identity+integrality OK")
assert sorted(rule_for_class) == list(range(2, 10)), sorted(rule_for_class)
# numeric: every X = 2^t 3^t', t,t' <= 25, X mod 11 not in {0,1,10}
cnt = skipped = 0
for t in range(26):
    for tp in range(26):
        Xv = 2**t * 3**tp
        r = Xv % 11
        if r in (1, 10):
            skipped += 1
            continue
        a, b, c, yn, zp = rule_for_class[r]
        nv = 48 * Xv**4 + 1
        assert nv == 2**(4 * t + 4) * 3**(4 * tp + 1) + 1
        xv = 3 * (4 * Xv**4 + 1)
        yv, zv = yn.eval(Xv), zp.eval(Xv)
        assert yv % 11 == 0 and zv % 11 == 0
        yv //= 11; zv //= 11
        assert xv > 0 and yv > 0 and zv > 0
        assert F(4, nv) == F(1, xv) + F(1, int(yv)) + F(1, int(zv))
        cnt += 1
print(f"Lemma 1.1 numeric: {cnt} Pierpont X verified exactly, {skipped} with X≡±1 (11) skipped")
# X -> limit at (a,b)->(0,1): t -> -1, t' -> 0: X -> 1/2 = 6 mod 11
print("limit X mod 11 at (0,1):", pow(2, -1, 11))

# Lemma 1.2 numeric: odd p | gcd(a,b), descent
from itertools import product
def es_small(m, lim=None):
    # brute force 4/m = 1/x+1/y+1/z, return a solution
    fr = F(4, m)
    for x in range(m // 4 + 1, 3 * m // 4 + 2):
        r1 = fr - F(1, x)
        if r1 <= 0: continue
        for y in range(max(x, int(1 / r1) ), int(2 / r1) + 2):
            r2 = r1 - F(1, y)
            if r2 > 0 and r2.numerator == 1 and r2.denominator >= y:
                return (x, y, r2.denominator)
    return None
ok = 0
for a in range(0, 13):
    for b in range(0, 10):
        if a == b == 0: continue
        g = gcd(a, b)
        for p in (3, 5, 7, 11):
            if g % p: continue
            Z = 2**(a // p) * 3**(b // p)
            nv = 2**a * 3**b + 1
            assert nv % (Z + 1) == 0 and 3 <= Z + 1 < nv
            sol = es_small(Z + 1)
            r = nv // (Z + 1)
            assert F(4, nv) == sum(F(1, v * r) for v in sol)
            ok += 1
print("Lemma 1.2 descent checks:", ok)
# integer squares 2^a3^b+1 (a,b<=60) and their 'unit' status
for a in range(61):
    for b in range(41):
        v = 2**a * 3**b + 1
        if isqrt(v)**2 == v:
            print("square:", (a, b), v, "=", isqrt(v), "^2", sp.factorint(isqrt(v)))
