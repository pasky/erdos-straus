"""R130: independent brute force of 4/p = 1/x+1/y+1/z (x<=y<=z), split into Type I (p divides exactly
one denominator) / Type II (exactly two), compared with the parameter enumerations used in the review:
 Type I : tuples (a<=b,c,d) from review_quat_hilbert.sols, triple (abdp, acd, bcd)
 Type II: 4abd = p+e, e | a+b, triple (abd, acdp, bcdp)   (Prop 3.2 form: e, m=(p+e)/4d, a | m, e | a+m/a)
Usage: review_quat_brute.py PMAX
"""
import sys
from fractions import Fraction
from sympy import primerange, divisors
from review_quat_hilbert import sols


def egypt(p):
    out = set()
    q = Fraction(4, p)
    for x in range(p // 4 + 1, 3 * p // 4 + 1):
        r = q - Fraction(1, x)
        if r <= 0:
            continue
        ymin = max(x, int(1 / r) + 1)
        ymax = int(2 / r)
        for y in range(ymin, ymax + 1):
            s = r - Fraction(1, y)
            if s > 0 and s.numerator == 1 and s.denominator >= y:
                out.add((x, y, s.denominator))
    return out


def typeII_prop32(p):
    out = set()
    # e <= a+b <= m+1 = (p+e)/(4d)+1  =>  e <= (p+4d)/(4d-1);  4d <= 4abd = p+e  => d <= (p+e)/4
    for d in range(1, p + 2):
        emax = (p + 4 * d) // (4 * d - 1)
        if 4 * d > p + emax:
            break
        for e in range(1, emax + 1):
            if (p + e) % (4 * d):
                continue
            m = (p + e) // (4 * d)
            for a in divisors(m):
                b = m // a
                if (a + b) % e == 0:
                    c = (a + b) // e
                    out.add(tuple(sorted((a * b * d, a * c * d * p, b * c * d * p))))
    return out


def main():
    P = int(sys.argv[1])
    for p in primerange(3, P):
        S = egypt(p)
        tI = {t for t in S if sum(v % p == 0 for v in t) == 1}
        tII = {t for t in S if sum(v % p == 0 for v in t) == 2}
        pI = {tuple(sorted((a * b * d * p, a * c * d, b * c * d))) for (a, b, c, d, e) in sols(p)}
        ntup = len(sols(p))
        pII = typeII_prop32(p)
        print(p, "typeI triples", len(tI), "param", len(pI), "tuples", ntup, pI == tI,
              "| typeII", len(tII), len(pII), pII == tII)


if __name__ == "__main__":
    main()
