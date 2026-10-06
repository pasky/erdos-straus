"""R77 from-scratch brute force for Lemma 15.1 (Jacobi dichotomy) and Prop. 15.2 of es-subexp-note v6.

Lemma 15.1: for every m-atom (M,D) (M >= 3, M = -1 mod m, M odd, D | A^2, A=(M+1)/m), with e the squarefree
part of mD, e = 2^t e_o:
 (a) every prime l | M: l does not divide mD and (-mD/l) = (-e/l)
 (b) M = 3 (4): (-mD/M) = -(2/M)^t
 (c) M = 1 (4): (-mD/M) = (2/M)^t (-1)^{(e_o-1)/2}
 (d) m = 0 (4): (-mD/M) = -1
Also re-checks the m-identity (15.1) and R_m(M) = {-u v^{-1}: uvw=A} = {-mD : D | A^2} for small M.
Prop 15.2: for m not 0 mod 4, the explicit construction gives primes l = -1 (m) whose atom classes meet both
square cosets; also lists the first such l and the example m=5, l=29.
"""
import sys
from fractions import Fraction
from sympy import factorint, divisors, isprime, jacobi_symbol as J, legendre_symbol


def sqfree(n):
    f = factorint(n)
    out = 1
    for p, k in f.items():
        if k % 2:
            out *= p
    return out


def check_lemma(mlist, Mmax):
    cnt = 0
    for m in mlist:
        M = m - 1
        while M <= Mmax:
            if M >= 3 and M % 2 == 1:
                A = (M + 1) // m
                fM = factorint(M)
                for D in divisors(A * A):
                    e = sqfree(m * D)
                    t = 1 if e % 2 == 0 else 0
                    eo = e >> t
                    s = J((-m * D) % M, M)
                    for l in fM:
                        assert (m * D) % l != 0, (m, M, D, l)
                        assert legendre_symbol((-m * D) % l, l) == legendre_symbol((-e) % l, l), (m, M, D, l)
                    j2 = J(2, M)
                    if M % 4 == 3:
                        assert s == -(j2 ** t), ("b", m, M, D)
                    else:
                        assert s == (j2 ** t) * (-1) ** ((eo - 1) // 2), ("c", m, M, D)
                    if m % 4 == 0:
                        assert s == -1, ("d", m, M, D)
                    if M % 8 == 7:
                        assert s == -1, ("M=7 mod 8 never fired", m, M, D)
                    cnt += 1
            M += m
    return cnt


def check_identity(mlist, Mmax):
    for m in mlist:
        for M in range(m - 1, Mmax + 1, m):
            if M < 3:
                continue
            A = (M + 1) // m
            Rm = {(-m * D) % M for D in divisors(A * A)}
            R2 = set()
            for u in divisors(A):
                for v in divisors(A // u):
                    w = A // (u * v)
                    if __import__("math").gcd(v, M) != 1:
                        continue
                    cls = (-u * pow(v, -1, M)) % M
                    R2.add(cls)
                    # identity for a concrete n in this class
                    n = cls if cls > 0 else M
                    s = Fraction(n * v + u, M)
                    assert s.denominator == 1 and s > 0
                    s = int(s)
                    assert Fraction(m, n) == Fraction(1, s * u * w) + Fraction(1, n * s * v * w) + Fraction(1, n * u * v * w)
            assert Rm == R2, (m, M)


def prop_fire(m, lmax):
    out = []
    for l in range(m - 1, lmax, m):
        if l < 3 or not isprime(l):
            continue
        A = (l + 1) // m
        syms = {legendre_symbol((-m * D) % l, l) for D in divisors(A * A)}
        if syms == {1, -1}:
            out.append(l)
    return out


if __name__ == "__main__":
    mlist = [4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 18, 20, 21, 22, 24, 28, 30]
    n = check_lemma(mlist, int(sys.argv[1]) if len(sys.argv) > 1 else 20000)
    print("Lemma 15.1 (a)-(d) + 'M=7(8) never fired': OK on", n, "atoms")
    check_identity(mlist, 600)
    print("identity (15.1) and R_m(M) characterisation OK for M <= 600")
    for m in mlist:
        if m % 4:
            L = prop_fire(m, 3000)
            assert L, m
            print("m=%d: first firing primes l = -1 (m):" % m, L[:6])
        else:
            assert not prop_fire(m, 3000)
    assert 29 in prop_fire(5, 100)
    print("Prop 15.2 OK (and no firing primes for m = 0 mod 4)")


def check_class_one(mlist, Mmax):
    """Thm 15.5 text: class of one is never covered: M | mD+1 impossible (archimedean, D -> A^2/D)."""
    for m in mlist:
        for M in range(m - 1, Mmax + 1, m):
            if M < 3:
                continue
            A = (M + 1) // m
            for D in divisors(A * A):
                assert (m * D + 1) % M != 0, (m, M, D)


if __name__ == "__main__":
    check_class_one(list(range(4, 41)), 20000)
    print("class of one never in R_m(M), m=4..40, M<=2e4: OK")


def check_parity_split(mmax=201, pmax=60):
    """Thm 15.7 text (odd m): n(mn-1) has fixed prime divisor 2; the split pairs have none."""
    from sympy import primerange
    for m in range(5, mmax, 2):
        assert all((n * (m * n - 1)) % 2 == 0 for n in range(2))
        for p in primerange(2, pmax):
            assert any((t * (2 * m * t - 1)) % p for t in range(p)), (m, p, "even")
            assert any(((2 * t + 1) * (m * t + (m - 1) // 2)) % p for t in range(p)), (m, p, "odd")


if __name__ == "__main__":
    check_parity_split()
    print("parity split pairs: no fixed prime divisor (odd m <= 199, p < 60): OK")
