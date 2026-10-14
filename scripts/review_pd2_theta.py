"""R210 from-scratch check of PHASE_DIAGRAM Prop 4.1 and its worked examples.

For odd n <= NMAX, e <= EMAX, k, lam <= KL, odd R <= RMAX with gcd(R, 2kn) = 1: g = 4k*lam*R - 1;
check  g | 4k^2 n + R^{2e}  <=>  g | N_e = n(2k(4k lam)^e)^2 + 1, and when it holds (and gcd(lam R, n) = 1)
build Q = lam R^{e+1}, verify the exact solution, overflow R^e, den z = R^{2e}.
Also: theta = log M / log N_e -> 1/(2e+2) for bounded lam, and -> 1/(2e) for k fixed, lam -> infinity.
"""
import sys
from fractions import Fraction as F
from math import gcd, log


def main(NMAX, EMAX, KL, RMAX):
    eq = shots = 0
    for n in range(3, NMAX + 1, 2):
        for e in range(0, EMAX + 1):
            for k in range(1, KL + 1):
                for lam in range(1, KL + 1):
                    M = 4 * k * lam
                    Ne = n * (2 * k * M ** e) ** 2 + 1
                    for R in range(1, RMAX + 1, 2):
                        if gcd(R, 2 * k * n) != 1:
                            continue
                        g = M * R - 1
                        a = (4 * k * k * n + R ** (2 * e)) % g == 0
                        b = Ne % g == 0
                        assert a == b, (n, e, k, lam, R)
                        eq += 1
                        if a and gcd(lam * R, n) == 1:
                            Q = lam * R ** (e + 1)
                            assert (n + 4 * Q * Q) % g == 0
                            K = (g + 1) // 4
                            assert Q // gcd(Q, K) == R ** e
                            x = F(n * (g + 1) + 4 * Q * Q, 4 * g)
                            y = n * (g + 1) // 4
                            z = x * y / (Q * Q)
                            assert x.denominator == 1 and F(4, n) == 1 / x + F(1, y) + 1 / z
                            assert z.denominator == R ** (2 * e)
                            shots += 1
    print(f"equivalence checked on {eq} tuples; {shots} shots verified")
    # examples
    n, e, k, lam, R = 13, 1, 5, 2, 3
    M = 4 * k * lam; g = M * R - 1; Ne = n * (2 * k * M ** e) ** 2 + 1
    print("example N_e/g =", F(Ne, g), " D =", F(4 * k * k * n + R ** (2 * e), g))
    n, Q, g = 113, 15 * 75, 59
    print("n=113 example: g | n+4Q^2:", (n + 4 * Q * Q) % g == 0, " Q0 =", gcd(Q, (g + 1) // 4))
    for e in (0, 1, 2):
        for (k, lam) in ((10 ** 6, 1), (10 ** 9, 1), (1, 10 ** 9), (1, 10 ** 30)):
            M = 4 * k * lam; Ne = 13 * (2 * k * M ** e) ** 2 + 1
            print(f"e={e} k={k:.0e} lam={lam:.0e}: logM/logN = {log(M) / log(Ne):.4f}")


if __name__ == "__main__":
    main(*[int(t) for t in sys.argv[1:5]])
