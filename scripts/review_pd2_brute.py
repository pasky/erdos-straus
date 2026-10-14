"""R210 from-scratch brute force of ES^{[2]} shots (independent of pd_* scripts).

Enumerate odd Q <= QMAX with gcd(Q, n) = 1 and every divisor g = 3 (mod 4) of n + 4Q^2.
Build the shot solution x = (n(g+1) + 4Q^2)/(4g), y = n(g+1)/4, z = x*y/Q^2 directly,
verify 4/n = 1/x + 1/y + 1/z with Fractions, and classify ES^{[2]} DIRECTLY by
den(z) | y^2 (not via Q1 | Q0).  Then test Thm 2.1 (a) wall, (b) band, Prop 1.1 normal
form, and Prop 1.3 duality.  Usage: review_pd2_brute.py NMAX QMAX
"""
import sys
from fractions import Fraction as F
from math import gcd, isqrt
from sympy import factorint


def divisors_from(fac):
    ds = [1]
    for p, e in fac.items():
        ds = [d * p ** i for d in ds for i in range(e + 1)]
    return ds


def main():
    NMAX, QMAX = int(sys.argv[1]), int(sys.argv[2])
    nshots = n2 = viol_a = viol_b = viol_nf = 0
    worst_a = F(0)
    worst_b = F(0)
    bigQ1 = {}
    for n in range(3, NMAX + 1, 2):
        for Q in range(1, QMAX + 1, 2):
            if gcd(Q, n) != 1:
                continue
            N = n + 4 * Q * Q
            for g in divisors_from(factorint(N)):
                if g % 4 != 3:
                    continue
                x = F(n * (g + 1) + 4 * Q * Q, 4 * g)
                y = n * (g + 1) // 4
                z = x * y / (Q * Q)
                assert x.denominator == 1 and F(4, n) == 1 / x + F(1, y) + 1 / z
                nshots += 1
                K = (g + 1) // 4
                Q0 = gcd(Q, K)
                Q1 = Q // Q0
                k = K // Q0
                dz = z.denominator
                if (y * y) % dz != 0:
                    continue  # not ES^{[2]}
                n2 += 1
                # normal form (1.1) with a = Q0, b = (m+n)/(4Q0)
                m = N // g
                assert (m + n) % (4 * Q0) == 0
                a, b = Q0, (m + n) // (4 * Q0)
                if not (k * (4 * a * b - n) == b + a * Q1 * Q1 and gcd(Q1, k) == 1 and Q1 % 2 == 1):
                    viol_nf += 1
                # duality
                D = (4 * k * k * n + Q1 * Q1) // g
                assert D * g == 4 * k * k * n + Q1 * Q1 and (D + Q1 * Q1) % (4 * k) == 0
                W = F(16 * k ** 3 * n + 1, 4 * k - 1)
                if Q1 > W:
                    viol_a += 1
                    print("WALL (a) VIOLATED", n, Q, g, k, Q1)
                worst_a = max(worst_a, Q1 / W)
                if 2 * Q1 > n + 1:
                    if not (2 * k < Q1 * Q1):
                        viol_b += 1
                        print("BAND (b) VIOLATED", n, Q, g, k, Q1)
                    worst_b = max(worst_b, F(k, Q1 * Q1))
                bigQ1.setdefault(n, []).append((Q1, k, g, dz == Q1 * Q1))
    print(f"shots={nshots} ES2={n2} viol_a={viol_a} viol_b={viol_b} viol_nf={viol_nf}")
    print(f"max Q1/W(k)={float(worst_a):.4f}  max k/Q1^2 (Q1>(n+1)/2)={float(worst_b):.4f}")
    for n in sorted(bigQ1):
        L = sorted(bigQ1[n], reverse=True)[:4]
        print(n, "count", len(bigQ1[n]), "largest (Q1,k,g,denz==Q1^2):", L)


if __name__ == "__main__":
    main()
