"""O194: T1 control for the Schinzel family m/n (m = 8, 16): at n = q^2 (q odd prime, q not dividing m) count all positive
solutions by shape at q (Type I: one v_q(u_i) >= 2, others 0; Type II: one 0, two >= 2; other).  usage: m QMAX"""
import sys
from sympy import primerange, divisors
from math import gcd


def sols(m, n):
    out = []
    for x in range(n // m + 1, 3 * n // m + 1):
        A, B = m * x - n, n * x
        if A <= 0:
            continue
        g = gcd(A, B); A //= g; B //= g
        for d in divisors(B * B):
            if d <= B and (d + B) % A == 0 and (B * B // d + B) % A == 0:
                y, z = (d + B) // A, (B * B // d + B) // A
                if y >= x:
                    assert m * x * y * z == n * (x * y + x * z + y * z)
                    out.append((x, y, z))
    return out


def v(a, q):
    k = 0
    while a % q == 0:
        a //= q; k += 1
    return k


if __name__ == '__main__':
    m, QMAX = int(sys.argv[1]), int(sys.argv[2])
    tot = {'I': 0, 'II': 0, 'other': 0}
    for q in primerange(3, QMAX + 1):
        if m % q == 0:
            continue
        for s in sols(m, q * q):
            vals = [v(u, q) for u in s]
            z0, big = vals.count(0), sum(1 for t in vals if t >= 2)
            tot['I' if (z0 == 2 and big == 1) else 'II' if (z0 == 1 and big == 2) else 'other'] += 1
    print(f"m = {m}, n = q^2, q <= {QMAX}: shapes {tot}")
