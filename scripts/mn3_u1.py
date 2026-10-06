"""MN3 numerics: class-of-one completed sums U_1(q) (EVIDENCE only).

U_1(q) = sum over atoms (M,D), D <= A, whose largest exactly-dividing prime power is q
(i.e. M in C_q), of K^omega(M)/phi(N), N = M/gcd(M, mD+1).  Truncated at M <= X.
Also splits the mass by where q sits (q | N vs q | g) and by c = (a+b)/g.

usage: uv run python mn3_u1.py m X K
"""
import sys
from math import gcd, isqrt


def spf_sieve(n):
    s = list(range(n + 1))
    for i in range(2, isqrt(n) + 1):
        if s[i] == i:
            for j in range(i * i, n + 1, i):
                if s[j] == j:
                    s[j] = i
    return s


def factor(n, spf):
    f = {}
    while n > 1:
        p = spf[n]
        f[p] = f.get(p, 0) + 1
        n //= p
    return f


def divisors_from(f):
    ds = [1]
    for p, e in f.items():
        ds = [d * p ** k for d in ds for k in range(e + 1)]
    return ds


def phi_f(f):
    r = 1
    for p, e in f.items():
        r *= (p - 1) * p ** (e - 1)
    return r


def main():
    m, X, K = int(sys.argv[1]), int(sys.argv[2]), float(sys.argv[3])
    spf = spf_sieve(X + 2)
    U = {}      # q -> total
    Uq_in_N = {}  # q -> part with q | N
    small_c = {}  # q -> part with c < q
    M = m - 1
    while M <= X:
        if M >= 3:
            A = (M + 1) // m
            fM = factor(M, spf)
            # top prime power
            q = max(p ** e for p, e in fM.items())
            fA = factor(A, spf) if A > 1 else {}
            fA2 = {p: 2 * e for p, e in fA.items()}
            w = K ** len(fM)
            for D in divisors_from(fA2):
                if D > A:
                    continue
                P = m * D + 1
                g = gcd(M, P)
                N = M // g
                val = w / phi_f(factor(N, spf)) if N > 1 else w
                U[q] = U.get(q, 0.0) + val
                if N % q == 0:
                    Uq_in_N[q] = Uq_in_N.get(q, 0.0) + val
                # c = (a+b)/g with D = d a^2, A = d a b  =>  a+b = (A + D)/(d a) ; need d,a
                # d a = A*?  use: A + D = d a (a+b), and g | a+b; c = (A+D)/(d a g)
                # d a = gcd-structure: D = d a^2, A = d a b -> d a = gcd(A, D) when gcd(a,b)=1 not nec.
                # cheap proxy: c_proxy = (A + D) * D // (A * g * ... ) skipped; use N-size instead
                if N < q * q:
                    small_c[q] = small_c.get(q, 0.0) + val
        M += m
    qs = sorted(U)
    print("m=%d X=%d K=%g" % (m, X, K))
    print("%8s %12s %12s %12s %10s" % ("q", "U1(q)", "q*U1", "frac q|N", "frac N<q^2"))
    for q in qs:
        if q < 2 or q > X ** (1 / 3):
            continue
        u = U[q]
        print("%8d %12.5g %12.5g %12.4f %10.4f" % (q, u, q * u, Uq_in_N.get(q, 0) / u, small_c.get(q, 0) / u))


if __name__ == "__main__":
    main()
