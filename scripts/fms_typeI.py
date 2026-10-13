"""fms_typeI.py P — verify the Type I cube (FIXED_MODULUS_SHOTS §4).

Type I := p divides exactly one denominator.  Claim: Type I solutions <-> (v, w, f) >= 1 with
g = 4vwf - p > 0 and g | pv + f;  u = (pv+f)/g,  x = p*u*v*w, y = w*f*u, z = w*f*v.
Checks for all primes 5 <= p <= P: (converse) every brute-force Type I solution (both orders of y,z) yields
such (u,v,w,f) with integrality and the formula; (forward) all (v,w,f) with g | p^2+4wf^2, g = -p mod 4wf,
wf <= p (enumerated via the (w,f)-line) give exact Type I solutions, and the two sets coincide.
"""
import sys
from math import gcd
from fractions import Fraction
from sympy import primerange, factorint
sys.path.insert(0, "scripts")
from fms_cube import all_solutions, _divs


def main():
    P = int(sys.argv[1])
    bad = 0
    maxwf = 0
    for p in primerange(5, P + 1):
        t1 = {t for t in all_solutions(p) if sum(1 for v in t if v % p == 0) == 1}
        for t in t1:
            x = next(v for v in t if v % p == 0)
            rest = list(t); rest.remove(x)
            for y, z in ((rest[0], rest[1]), (rest[1], rest[0])):
                G = gcd(y, z); u, v = y // G, z // G
                xp = x // p
                assert xp % (u * v) == 0
                w = xp // (u * v)
                assert G % w == 0
                f = G // w
                g = 4 * v * w * f - p
                assert g > 0 and (p * v + f) % g == 0 and (p * v + f) // g == u
                maxwf = max(maxwf, w * f)
        fwd = set()
        for w in range(1, p + 1):
            for f in range(1, p // w + 1):
                N = p * p + 4 * w * f * f
                for g in _divs(factorint(N)):
                    if (g + p) % (4 * w * f):
                        continue
                    v = (g + p) // (4 * w * f)
                    if (p * v + f) % g:
                        continue
                    u = (p * v + f) // g
                    x, y, z = p * u * v * w, w * f * u, w * f * v
                    assert Fraction(1, x) + Fraction(1, y) + Fraction(1, z) == Fraction(4, p)
                    if y % p == 0 or z % p == 0:
                        continue
                    fwd.add(tuple(sorted((x, y, z))))
        if fwd != t1:
            bad += 1
            print("MISMATCH", p, len(fwd), len(t1))
    print(f"primes <= {P}: mismatches {bad}; max wf over Type I solutions {maxwf}")
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
