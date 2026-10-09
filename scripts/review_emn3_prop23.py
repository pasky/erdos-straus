"""R108 from-scratch checks of EXCEPTIONAL_MN3 Prop 2.3 (coprimality-gain ET Prop 1.4).

(1) pointwise: rho_{ka}(m0) <= 1[(m0,k)=1] * sum_{q|m0} (-ka/q)  for odd m0 (brute-force roots)
(2) rho(2^j) <= 4
(3) the sum S(k,A,B) = sum_{a<=A,b<=B} tau(k a b^2 + 1) normalised by (phi(k)/k) A B log B * Lam,
    over many k incl. primorials and k with many small primes, and small-A (Lambda~log k) regimes.
"""
import math, sys
from sympy import factorint, jacobi_symbol, totient, primerange


def tau(n):
    r = 1
    for e in factorint(n).values():
        r *= e + 1
    return r


def rho(K, m):  # roots b mod m of K b^2 + 1
    return sum(1 for b in range(m) if (K * b * b + 1) % m == 0)


def check_pointwise(kmax=40, amax=12, mmax=400):
    bad = 0
    for k in range(1, kmax + 1):
        for a in range(1, amax + 1):
            K = k * a
            for m0 in range(1, mmax + 1, 2):
                lhs = rho(K, m0)
                if math.gcd(m0, k) != 1:
                    rhs = 0
                else:
                    rhs = sum(jacobi_symbol(-K % q, q) if q > 1 else 1
                              for q in range(1, m0 + 1) if m0 % q == 0)
                if lhs > rhs:
                    bad += 1
                    print("POINTWISE FAIL", k, a, m0, lhs, rhs)
    for K in range(1, 200):
        for j in range(1, 9):
            if rho(K, 2 ** j) > 4:
                bad += 1
                print("rho(2^j) FAIL", K, j)
    print("pointwise checks done, failures:", bad)


def S(k, A, B):
    return sum(tau(k * a * b * b + 1) for a in range(1, A + 1) for b in range(1, B + 1))


def Lam(k, A):
    return 1 + min(math.log(1 + k), k ** (1 / 6) * math.log(2 * k * A) / A ** 0.5)


def check_sums():
    prim = 1
    ks = [1, 2, 3, 4, 6]
    for p in primerange(2, 30):
        prim *= p
        ks.append(prim)
    ks += [101, 1009, 10007, 100003, 2 * 3 * 1009, 4 * 1009 * 1013, 2 ** 10, 3 ** 8]
    print(f"{'k':>12} {'A':>4} {'B':>5} {'phi/k':>6} {'S/(ABlogB)':>11} {'/phi':>7} {'/(phi*Lam)':>10} {'ET:/log(1+k)':>12}")
    for k in ks:
        for (A, B) in [(2, 3000), (6, 1000), (40, 150), (150, 40)]:
            s = S(k, A, B)
            ph = int(totient(k)) / k
            base = A * B * math.log(max(A, B))
            r = s / base
            print(f"{k:>12} {A:>4} {B:>5} {ph:6.3f} {r:11.3f} {r/ph:7.3f} {r/ph/Lam(k, A):10.3f} {r/math.log(2+k):12.3f}")
        sys.stdout.flush()


if __name__ == "__main__":
    check_pointwise()
    check_sums()
