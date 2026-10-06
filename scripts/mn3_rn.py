"""MN3 numerics: R(N) = #{atoms (M,D), D<=A : M/gcd(M,mD+1) = N}  (EVIDENCE only).

Enumerates O12-tuples (a,c,d,f): P = m a^2 d + 1, f | P, e = P/f, b = c e - a >= a,
N = m a d c - f, keeping exact atoms (d squarefree, gcd(M,P) = e).  All tuples with N <= X
satisfy a c d <= N, so a d <= X and the enumeration is complete for N <= X.

usage: uv run python mn3_rn.py m X
"""
import sys
from math import gcd
from sympy import factorint, divisors


def squarefree(n):
    return all(e == 1 for e in factorint(n).values())


def main():
    m, X = int(sys.argv[1]), int(sys.argv[2])
    R = [0] * (X + 1)
    for a in range(1, X + 1):
        for d in range(1, X // a + 1):
            if not squarefree(d):
                continue
            P = m * a * a * d + 1
            for f in divisors(P):
                if f > (m - 1) * X:
                    break
                e = P // f
                c0 = max(1, -(-f // ((m - 1) * a * d)))  # N >= a c d  <=>  c >= f/((m-1)ad)
                c = c0
                while True:
                    N = m * a * d * c - f
                    if N > X:
                        break
                    if N >= 1:
                        b = c * e - a
                        M = e * N
                        if b >= a and gcd(M, P) == e:
                            R[N] += 1
                    c += 1
    tot = 0
    print("m=%d X=%d" % (m, X))
    mx = 0
    for N in range(1, X + 1):
        tot += R[N]
        if R[N] > mx:
            mx = R[N]
            print("new max R(%d) = %d" % (N, R[N]))
    import math
    for Y in [10, 100, 1000, 10 ** 4, 10 ** 5]:
        if Y <= X:
            s = sum(R[1:Y + 1])
            h = sum(R[N] / N for N in range(1, Y + 1))
            print("Y=%d sum R = %d  mean = %.3f  (logY)^3=%.1f  sum R/N = %.2f (logY)^4=%.1f"
                  % (Y, s, s / Y, math.log(Y) ** 3, h, math.log(Y) ** 4))


if __name__ == "__main__" and len(sys.argv) == 3:
    main()


def moments(m, X):
    """second moment and prime values of R (EVIDENCE)."""
    import math
    from sympy import isprime
    import io, contextlib
    R = [0] * (X + 1)
    for a in range(1, X + 1):
        for d in range(1, X // a + 1):
            if not squarefree(d):
                continue
            P = m * a * a * d + 1
            for f in divisors(P):
                if f > (m - 1) * X:
                    break
                e = P // f
                c = max(1, -(-f // ((m - 1) * a * d)))
                while True:
                    N = m * a * d * c - f
                    if N > X:
                        break
                    if N >= 1 and c * e - a >= a and gcd(e * N, P) == e:
                        R[N] += 1
                    c += 1
    for Y in [10 ** 3, 3 * 10 ** 3, 10 ** 4, 3 * 10 ** 4, 10 ** 5]:
        if Y > X:
            break
        s1 = sum(R[1:Y + 1]); s2 = sum(r * r for r in R[1:Y + 1])
        pr = [R[p] for p in range(Y // 2, Y + 1) if isprime(p)]
        print("Y=%6d  S1/Y=%7.2f  S2/Y=%9.1f  S2/(Y log^6 Y)=%.4f  primes in (Y/2,Y]: mean R=%.2f max R=%d"
              % (Y, s1 / Y, s2 / Y, s2 / (Y * math.log(Y) ** 6), sum(pr) / len(pr), max(pr)))


if __name__ == "__main__" and len(sys.argv) > 3 and sys.argv[3] == "moments":
    moments(int(sys.argv[1]), int(sys.argv[2]))
