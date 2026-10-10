"""O128 step 1: verify the Type II parametrisations of POINTWISE_TYPEII_SPECTRAL.md §1-2.

For every prime p < PMAX:
  (i)   brute-force Type II solutions of 4/p = 1/x+1/y+1/z (p | y, p | z, p ∤ x), ordered (y,z);
  (ii)  ET quadruples (a,b,c,d): 4abcd = a+b+pc, gcd(a,c)=1  (equivalently gcd(a,b,c)=1);
  (iii) SL2 form: f=4acd-1, f'=4bcd-1, f f' - 4c^2 d p = 1;   det-p form: e f - 4a^2 d = p;
  (iv)  (a,b)-residue form: e = 4abd - p is the least positive residue of -p mod 4ab and e | a+b;
  (v)   divisibility duality: (4acd-1) | (a+pc);
  (vi)  separation: for fixed (p,d) the forms [f, 4cdp, dp f'] (disc -4dp) have
        cosh dist >= 3/2 pairwise (TYPEI_LOGLOG Lemma 2.2 with d -> dp);
  (vii) hypercycle incidence: w = (-2a + i sqrt(p/d))/f  [det-p coordinates, z/d] satisfies
        Re w = -(1 + Im(w) sqrt(dp)) / (2 d c)   (Prop 2.4).
Prints a summary; exits nonzero on any mismatch.
"""
import math, sys
from fractions import Fraction
from sympy import primerange

PMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 400


def brute(p):
    sols = set()
    for x in range(p // 4 + 1, p // 2 + 1):
        if x % p == 0:
            continue
        r = Fraction(4, p) - Fraction(1, x)  # = 1/y + 1/z
        if r <= 0:
            continue
        # y <= z: 1/y >= r/2 -> y <= 2/r ; 1/y < r -> y > 1/r
        ylo = int(1 / r) + 1
        yhi = int(2 / r)
        for y in range(ylo, yhi + 1):
            s = r - Fraction(1, y)
            if s > 0 and s.numerator == 1:
                z = s.denominator
                if y % p == 0 and z % p == 0:
                    sols.add((x, y, z)); sols.add((x, z, y))
    return sols


def et_quads(p):
    out = []
    # 4abcd = a+b+pc ; b(4acd-1) = a+pc ; acd <= p (since e>=1: 4abd = p+e and b>=?), crude bound
    for a in range(1, p + 1):
        for c in range(1, p + 1):
            if 4 * a * c - 1 > a + p * c:
                break
            if math.gcd(a, c) != 1:
                continue
            for d in range(1, p + 1):
                f = 4 * a * c * d - 1
                if f > a + p * c:
                    break
                if (a + p * c) % f == 0:
                    out.append((a, (a + p * c) // f, c, d))
    return out


bad = 0
tot = 0
for p in primerange(5, PMAX):
    B = brute(p)
    Q = et_quads(p)
    img = {(a * b * d, a * c * d * p, b * c * d * p) for (a, b, c, d) in Q}
    if img != B or len(Q) != len(B):
        bad += 1; print("MISMATCH brute", p, len(B), len(Q))
    byd = {}
    for (a, b, c, d) in Q:
        tot += 1
        f, fp = 4 * a * c * d - 1, 4 * b * c * d - 1
        e = (a + b) // c
        ok = ((a + b) % c == 0 and f * fp - 4 * c * c * d * p == 1 and e * f - 4 * a * a * d == p
              and (4 * a * b * d - p) == e and (a + p * c) % f == 0)
        # least positive residue check (e <= a+b < 4ab except tiny cases)
        lpr = (-p) % (4 * a * b)
        if e != lpr and not (e > 4 * a * b):
            ok = False
        if e > 4 * a * b:
            print('note: e > 4ab at', p, (a, b, c, d))
        # (vii) in the dilated coordinates w2 = z2/(dp), z2 root of [f,4cdp,dpf']: w2 = (-2c + i/sqrt(dp))/f
        X2, Y2 = -2 * c / f, 1 / (f * math.sqrt(d * p))
        # incidence (Prop 2.4): Re w2 = -(1 + Im(w2) sqrt(dp)) / (2 a d)
        if abs(X2 + (1 + Y2 * math.sqrt(d * p)) / (2 * a * d)) > 1e-12:
            ok = False
        # det-p coordinates w1 = (-2a + i sqrt(p/d))/f: Re w1 = -(1 + Im(w1) sqrt(d/p)) / (2 c d)
        X1, Y1 = -2 * a / f, math.sqrt(p / d) / f
        if abs(X1 + (1 + Y1 * math.sqrt(d / p)) / (2 * c * d)) > 1e-12:
            ok = False
        if not ok:
            bad += 1; print("IDENTITY FAIL", p, (a, b, c, d))
        byd.setdefault(d, []).append((f, 4 * c * d * p, d * p * fp))
    for d, forms in byd.items():
        D = 4 * d * p
        for i in range(len(forms)):
            for j in range(i + 1, len(forms)):
                (A, Bq, C), (A2, B2, C2) = forms[i], forms[j]
                disc = (Bq - B2) ** 2 - 4 * (A - A2) * (C - C2)
                ch = 1 + Fraction(disc, 2 * D)
                if ch < Fraction(3, 2) and (A, Bq, C) != (A2, B2, C2):
                    bad += 1; print("SEPARATION FAIL", p, d, forms[i], forms[j], ch)
print(f"primes 5..{PMAX}: {tot} Type II solutions checked, failures = {bad}")
if bad: sys.exit(1)


def genus_check(PM):
    """Lemma 6.1: every Type II solution has (p/f) = (p/f') = -1 (Jacobi), f=4acd-1, f'=4bcd-1."""
    from sympy import jacobi_symbol
    bad = 0; n = 0
    for p in primerange(5, PM):
        for (a, b, c, d) in et_quads(p):
            for g in (4 * a * c * d - 1, 4 * b * c * d - 1):
                if math.gcd(g, p) == 1:
                    n += 1
                    if jacobi_symbol(p, g) != -1:
                        bad += 1; print("GENUS FAIL", p, (a, b, c, d), g)
    print(f"genus lemma: {n} moduli checked, failures = {bad}")
    return bad


if genus_check(PMAX):
    sys.exit(1)
