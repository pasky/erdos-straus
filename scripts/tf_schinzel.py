"""O194 side check: m/p = 1/x + 1/y + 1/z in POSITIVE integers (Schinzel family; BL Remark 1.10: T1-type law
prod_{q | 2nm} (-u1/u3, -u2/u3)_q = -1).  Complete search (x <= y <= z, p/m < x <= 3p/m, divisor pairs of (px)^2).
usage: tf_schinzel.py m PMAX  -> primes p <= PMAX (p not dividing 2m) with no solution, and odd squares k^2 <= SQMAX."""
import sys
from sympy import primerange, factorint, divisors
from math import gcd


def count(m, n, stop_at_first=True):
    c = 0
    for x in range(n // m + 1, 3 * n // m + 1):
        A = m * x - n
        if A <= 0:
            continue
        B = n * x
        g = gcd(A, B); A //= g; B //= g
        # (A y - B)(A z - B) = B^2 with y <= z: d = A y - B <= B
        for d in divisors(B * B):
            if d > B:
                continue
            if (d + B) % A == 0 and (B * B // d + B) % A == 0:
                y = (d + B) // A
                if y >= x:
                    c += 1
                    if stop_at_first:
                        return c
    return c


if __name__ == '__main__':
    m, PMAX = int(sys.argv[1]), int(sys.argv[2])
    fails = [p for p in primerange(3, PMAX + 1) if (2 * m) % p and count(m, p) == 0]
    print(f"m = {m}: primes p <= {PMAX} with NO positive solution: {fails}")
    SQ = int(sys.argv[3]) if len(sys.argv) > 3 else 0
    if SQ:
        sq = [k * k for k in range(3, int(SQ ** 0.5) + 1, 2) if gcd(k, 2 * m) == 1 and count(m, k * k) == 0]
        print(f"   odd squares k^2 <= {SQ} (gcd(k,2m)=1) with no solution: {sq}")
