"""O203 Prop 4.1(b): Type II cube points (c, d, j) of p  <->  B = 1 points of V_{pd} with d | lambda.
Cube (FIXED_MODULUS_SHOTS Lemma 1.1, (c,d)-line): 3cd <= p+1, h | p + 4c^2 d, h = -1 (mod 4cd), j = (h+1)/(4cd).
V_{n'} B = 1 points (Thm 1.3 with n' = pd): t in [1, n'], D | n' + 4t^2, D = -1 (4t), j' = (D+1)/(4t),
mu = n' j' + t, lambda = mu / D; keep d | lambda; map to (c, d, j) = (lambda/d, d, j').
Usage: cp_typeii.py pmax"""
import sys
from sympy import primerange, divisors


def cube(p):
    out = set()
    for c in range(1, p + 2):
        for d in range(1, (p + 1) // (3 * c) + 1):
            M = 4 * c * d
            for h in divisors(p + 4 * c * c * d):
                if h % M == M - 1:
                    out.add((c, d, (h + 1) // M))
    return out


def vslices(p):
    out = set()
    for d in range(1, (p + 1) // 3 + 1):
        n2 = p * d
        for t in range(1, n2 + 1):
            for D in divisors(n2 + 4 * t * t):
                if D % (4 * t) == 4 * t - 1:
                    j = (D + 1) // (4 * t)
                    mu = n2 * j + t
                    assert mu % D == 0
                    lam = mu // D
                    if lam % d == 0:
                        h = 4 * lam * j - 1
                        assert (4 * d * j * j * p + 1) % h == 0
                        out.add((lam // d, d, j))
    return out


def main():
    pmax = int(sys.argv[1])
    bad = tot = 0
    for p in primerange(5, pmax + 1):
        a, b = cube(p), vslices(p)
        tot += len(a)
        if a != b:
            bad += 1
            print("MISMATCH", p, sorted(a ^ b)[:5])
    print("primes <=", pmax, "cube points", tot, "mismatching primes", bad)


if __name__ == "__main__":
    main()
