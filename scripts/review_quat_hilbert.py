"""R130 from-scratch check of QUATERNION_ES Prop 1.3.
Enumerate all Type I solutions (a<=b,c,d) of 4/p via (a,c,d): f=4acd-p>0, f | 4a^2 d+1,
e=(4a^2d+1)/f, b=ce-a (need b>=a, gcd(c,p)=1).  Bound: a<=b => 4acd <= 2p+2.
For each, compute Hilbert symbols of (-d, -d(4dm-1)), m=ab, at EVERY prime dividing 2dpe
(including 2, directly) and at infinity.  Also check p does not divide e, 4dm-1 = pe,
and the K-factorisation identity.  Usage: review_quat_hilbert.py PMAX
"""
import sys
from sympy import primerange, factorint


def val(n, l):
    k = 0
    while n % l == 0:
        n //= l; k += 1
    return k, n


def leg(a, l):  # Legendre, l odd prime, l !| a
    r = pow(a % l, (l - 1) // 2, l)
    return 1 if r == 1 else -1


def hilbert(a, b, l):
    """(a,b)_l for nonzero integers a,b, prime l (incl. 2); Serre's formulas."""
    al, u = val(a, l)
    be, v = val(b, l)
    if l != 2:
        s = (-1) ** (al * be * ((l - 1) // 2) % 2)
        return s * leg(u, l) ** be * leg(v, l) ** al
    eps = lambda x: ((x - 1) // 2) % 2
    om = lambda x: ((x * x - 1) // 8) % 2
    u %= 8; v %= 8
    ex = eps(u) * eps(v) + al * om(v) + be * om(u)
    return (-1) ** (ex % 2)


def sols(p):
    out = []
    amax = (2 * p + 2) // 4
    for a in range(1, amax + 1):
        for c in range(1, (2 * p + 2) // (4 * a) + 1):
            for d in range(1, (2 * p + 2) // (4 * a * c) + 1):
                f = 4 * a * c * d - p
                if f <= 0:
                    continue
                N = 4 * a * a * d + 1
                if N % f:
                    continue
                e = N // f
                b = c * e - a
                if b < a or c % p == 0:
                    continue
                out.append((a, b, c, d, e))
    return out


def main():
    P = int(sys.argv[1])
    tot = bad = pe_div = 0
    for p in primerange(3, P):
        for (a, b, c, d, e) in sols(p):
            tot += 1
            m = a * b
            assert 4 * d * m - 1 == p * e and a + b == c * e
            # K-factorisation: (1+2a w)(1+2b w) = 1-4abd + 2(a+b) w = e(2c w - p)
            assert 1 - 4 * a * b * d == -e * p and 2 * (a + b) == 2 * c * e
            if e % p == 0:
                pe_div += 1
            A, B = -d, -d * (4 * d * m - 1)
            primes = set(factorint(2 * d * p * e)) | {2}
            ram = {l for l in primes if hilbert(A, B, l) == -1}
            ram_inf = (A < 0 and B < 0)
            if ram != {p} or not ram_inf:
                bad += 1
                print("BAD", p, a, b, c, d, e, ram)
    print(f"PMAX={P} TypeI solutions (a<=b)={tot} bad={bad} p|e cases={pe_div}")


if __name__ == "__main__":
    main()
