"""R158 from-scratch checks for INVOLUTION_ES.md §2 and Lemma 5.2.

X(n) = {(t,u,v) >= 1 : t*u*v - u - v = n},  E(n) = {4 | t*u - 1}.
Enumerate via A = t*u - 1 dividing t*n + 1 (t <= n + 2).
Checks:
 * Lemma 2.1 parity (|X(n)| vs #{u(tu-2)=n}) for odd n <= N1;
 * every E(n) element gives an explicit ES solution (CONDITIONAL_ES L1.1 formula), n <= N1;
 * E(m^2) empty for odd m <= M2, parity of |X(m^2)| (all odd primes m must be odd);
 * Lemma 5.2: for p = 1 mod 8 prime <= N1, each E element has Jacobi(delta0/p) = -1.
"""
import sys
from fractions import Fraction
from sympy import divisors, isprime, jacobi_symbol


def X(n):
    out = []
    for t in range(1, n + 3):
        N = t * n + 1
        for A in divisors(N):
            if (A + 1) % t:
                continue
            B = N // A
            if (B + 1) % t:
                continue
            out.append((t, (A + 1) // t, (B + 1) // t))
    return out


def es_from_E(n, t, u, v):
    # Lemma 1.1 of CONDITIONAL_ES with (g,f,c)=(t,u,v): d=(fg-1)/4, b=(n+c)/f
    g, f, c = t, u, v
    d = (f * g - 1) // 4
    assert (n + c) % f == 0
    b = (n + c) // f
    x, y, z = b * d * n, c * d, b * c * d
    return Fraction(1, x) + Fraction(1, y) + Fraction(1, z) == Fraction(4, n)


def main(N1, M2):
    bad = 0
    for n in range(1, N1 + 1):
        xs = X(n)
        assert all(t * u * v - u - v == n for t, u, v in xs)
        for (t, u, v) in xs:
            if (t * u - 1) % 4 == 0 and not es_from_E(n, t, u, v):
                bad += 1
        if n % 2:
            fx = sum(1 for u in divisors(n) if (n // u + 2) % u == 0)
            if len(xs) % 2 != fx % 2:
                bad += 1
                print("L2.1 fail", n)
            # unitary claim
            for u in divisors(n):
                if (n // u + 2) % u == 0 and __import__('math').gcd(u, n // u) != 1:
                    print("unitary fail", n, u); bad += 1
    print("L2.1 + E->ES check up to", N1, "bad =", bad)
    evenprimes, Enonempty, oddcount, tot = [], [], 0, 0
    for m in range(3, M2 + 1, 2):
        xs = X(m * m)
        tot += 1
        if any((t * u - 1) % 4 == 0 for t, u, v in xs):
            Enonempty.append(m)
        if len(xs) % 2:
            oddcount += 1
        elif isprime(m):
            evenprimes.append(m)
    print("odd m<=%d: E(m^2) nonempty for" % M2, Enonempty, "; |X(m^2)| odd for", oddcount, "of", tot,
          "; primes with even |X|:", evenprimes)
    viol, cnt = 0, 0
    for p in range(17, N1 + 1, 8):
        if not isprime(p):
            continue
        for (t, u, v) in X(p):
            A = t * u - 1
            if A % 4:
                continue
            cnt += 1
            d0 = A
            while d0 % 2 == 0:
                d0 //= 2
            if jacobi_symbol(d0, p) != -1:
                viol += 1
    print("Lemma 5.2: E elements", cnt, "violations", viol)


if __name__ == "__main__":
    main(int(sys.argv[1]), int(sys.argv[2]))
