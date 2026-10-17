"""O253 helpers: complete enumeration of W(n) = {x<=y<=z : 4/n = 1/x+1/y+1/z}."""
from math import gcd, isqrt
from sympy import factorint


def divisors_from_fact(f):
    ds = [1]
    for q, e in f.items():
        ds = [d * q**k for d in ds for k in range(e + 1)]
    return ds


def two_term(A, B, ymin):
    """all (y,z), ymin<=y<=z, with A/B = 1/y + 1/z (A/B reduced)."""
    # (Ay - B)(Az - B) = B^2 ; u = Ay - B divides B^2, u <= B, u ≡ -B (mod A)
    out = []
    fB = factorint(B)
    f2 = {q: 2 * e for q, e in fB.items()}
    for u in divisors_from_fact(f2):
        if u > B:
            continue
        if (u + B) % A:
            continue
        v = B * B // u
        if (v + B) % A:
            continue
        y, z = (u + B) // A, (v + B) // A
        if y >= ymin and y <= z:
            out.append((y, z))
    return out


def W(n, num=4, limit=None):
    """all solutions x<=y<=z of num/n = 1/x+1/y+1/z."""
    sols = []
    x0 = n // num + 1
    for x in range(x0, 3 * n // num + 1):
        A, B = num * x - n, n * x
        g = gcd(A, B)
        A, B = A // g, B // g
        if A <= 0:
            continue
        for y, z in two_term(A, B, x):
            sols.append((x, y, z))
            if limit and len(sols) >= limit:
                return sols
    return sols


def has_sol(n, num=4):
    return len(W(n, num, limit=1)) > 0


if __name__ == "__main__":
    from fractions import Fraction as F
    for n in [5, 7, 25, 97]:
        s = W(n)
        assert all(F(1, x) + F(1, y) + F(1, z) == F(4, n) for x, y, z in s)
        print(n, len(s), s[:4])
