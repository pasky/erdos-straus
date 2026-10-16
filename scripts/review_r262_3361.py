"""R262 from-scratch: ALL Type II solutions of 4/p = 1/x + 1/y + 1/z (p | y, p | z, p ∤ x).

Completeness: y, z >= p (multiples of p) => 1/y + 1/z <= 2/p => 1/x >= 2/p => x <= p/2; and 1/x < 4/p => x > p/4.
Write y = p*Y, z = p*Z: (4x - p)/x = 1/Y + 1/Z.  With m = 4x - p >= 1:
(mY - x)(mZ - x) = x^2, and mY - x > 0 (since 1/Y < m/x).  So every solution has
delta := mY - x a positive divisor of x^2 with delta = -x (mod m) and (x^2/delta) = -x (mod m).
We loop over ALL x in (p/4, p/2] and ALL divisors delta of x^2 -> complete list of ordered (x, Y, Z).
Then for each slice g = 4Y - 1 and D = 4Z - 1 decide whether -p is a square mod it (by full factorisation).
"""
import sys
from fractions import Fraction
from sympy import factorint, divisors


def is_sq_mod(r, n):
    """is r a square modulo n (n odd >= 1), allowing gcd(r, n) > 1 handled exactly by brute force per prime power"""
    for l, e in factorint(n).items():
        q = l ** e
        rr = r % q
        assert q < 10**6
        if not any((t * t - rr) % q == 0 for t in range(q)):
            return False
    return True


def type2(p):
    sols = set()
    for x in range(p // 4 + 1, p // 2 + 1):
        if x % p == 0:
            continue
        m = 4 * x - p
        if m <= 0:
            continue
        for de in divisors(x * x):
            if (x + de) % m == 0 and (x + x * x // de) % m == 0:
                Y, Z = (x + de) // m, (x + x * x // de) // m
                assert Fraction(1, x) + Fraction(1, p * Y) + Fraction(1, p * Z) == Fraction(4, p)
                sols.add((x, min(Y, Z), max(Y, Z)))
    return sorted(sols)


if __name__ == "__main__":
    p = int(sys.argv[1]) if len(sys.argv) > 1 else 3361
    S = type2(p)
    print("p =", p, "#unordered Type II solutions:", len(S))
    for x, Y, Z in S:
        g, D = 4 * Y - 1, 4 * Z - 1
        print(f"x={x} y={p}*{Y} z={p}*{Z}  slices g={g} {factorint(g)} -p sq? {is_sq_mod(-p, g)} gcd(g,p)={__import__('math').gcd(g,p)};"
              f" D={D} {factorint(D)} -p sq? {is_sq_mod(-p, D)}")
