"""fms_cube.py P — verify the certificate cube (FIXED_MODULUS_SHOTS §1).

For every prime 5 <= p <= P:
  * brute force: all solutions 4/p = 1/x+1/y+1/z (x<=y<=z) via the divisor method;
    Type II := p divides exactly two of x, y, z.
  * cube: all (c,d,j) >= 1 with h = 4cdj-1 | p+4c^2 d (equivalently h | pj+c), 3cd <= p+1;
    solution x=(p+e)/4, y=p*c*d*j, z=p*x*j/c with e=(p+4c^2 d)/h.
  * checks: the three divisibilities h | p+4c^2d, h | pj+c, h | 4dj^2p+1 agree; every cube triple is
    an exact Type II solution; the set of cube solutions equals the brute-force Type II set.
"""
import sys
from fractions import Fraction
from sympy import primerange, divisors, factorint


def all_solutions(p):
    sols = set()
    for x in range(p // 4 + 1, 3 * p // 4 + 1):
        E, X = 4 * x - p, p * x
        if E <= 0:
            continue
        # 1/y + 1/z = E/X, y <= z, y >= x: (E y - X)(E z - X) = X^2
        fx = factorint(X)
        fx2 = {q: 2 * a for q, a in fx.items()}
        for D in _divs(fx2):
            if (D + X) % E:
                continue
            y = (D + X) // E
            D2 = X * X // D
            if (D2 + X) % E:
                continue
            z = (D2 + X) // E
            if y > z or y < x:
                continue
            sols.add((x, y, z))
    return sols


def _divs(f):
    ds = [1]
    for q, a in f.items():
        ds = [d * q ** k for d in ds for k in range(a + 1)]
    return ds


def cube_solutions(p):
    out = set()
    ncert = 0
    # every cube point has 3cd <= 4cd - c <= p + 1 (from h <= pj + c)
    for c in range(1, (p + 1) // 3 + 1):
        for d in range(1, (p + 1) // (3 * c) + 1):
            N = p + 4 * c * c * d
            m = 4 * c * d
            for h in _divs(factorint(N)):
                if (h + 1) % m:
                    continue
                j = (h + 1) // m
                assert 4 * h <= (p + 1) * (p + 5) - 4  # Prop 6.1
                assert (p * j + c) % h == 0 and (4 * d * j * j * p + 1) % h == 0
                e = N // h
                assert (p + e) % 4 == 0
                x = (p + e) // 4
                assert (x * j) % c == 0
                y, z = p * c * d * j, p * x * j // c
                assert Fraction(1, x) + Fraction(1, y) + Fraction(1, z) == Fraction(4, p)
                assert x % p and y % p == 0 and z % p == 0
                out.add(tuple(sorted((x, y, z))))
                ncert += 1
    return out, ncert


def main():
    P = int(sys.argv[1])
    tot = bad = 0
    for p in primerange(5, P + 1):
        s = all_solutions(p)
        t2 = {t for t in s if sum(1 for v in t if v % p == 0) == 2}
        cs, nc = cube_solutions(p)
        tot += 1
        if cs != t2:
            bad += 1
            print("MISMATCH", p, len(cs), len(t2), sorted(cs ^ t2)[:5])
    print(f"primes checked: {tot}, mismatches: {bad}")
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
