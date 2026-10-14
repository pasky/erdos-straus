"""O212 (BRAINSTORM/y4_mordell_witness): for which A is "A = tu - 1 = A" a UNIVERSAL chi = -1 certificate?

A word with first slot A exists at the prime p iff some t | A + 1 has t*p = -1 (mod A) (then u = (A+1)/t,
A* = (tp+1)/A = -1 (mod t) automatically when gcd(t, A) = 1, v = (A*+1)/t).  By (J)32 Thm 3.1 the word is an ES
certificate iff (-A/p) = -1.  Claim: for prime A = q this is automatic on {(-q/p) = -1} iff q in {2, 3, 5, 7}
(tau(q+1) - 1 >= (q-1)/2 is needed); checked here for all primes p <= PMAX, every word built and the slice solution
verified exactly.
Usage: PYTHONPATH=scripts uv run python scripts/y4_witness.py [PMAX]
"""
import sys
from fractions import Fraction
from sympy import primerange, divisors, jacobi_symbol as J, isprime
sys.path.insert(0, 'scripts')
from y4_oddslice_cells import slice_sols


def word_with_A(p, A):
    for t in divisors(A + 1):
        if (t * p + 1) % A == 0:
            u = (A + 1) // t
            As = (t * p + 1) // A
            if As % t == t - 1 % t or t == 1:
                v = (As + 1) // t
                if v >= 1 and t * u * v - u - v == p:
                    return t, u, v
    return None


if __name__ == '__main__':
    PMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 100000
    for A in [q for q in range(2, 60) if isprime(q)] + [15, 21, 35]:
        tot = miss = 0
        for p in primerange(3, PMAX):
            if A % p == 0 or p == A:
                continue
            if J((-A) % p, p) != -1:
                continue
            tot += 1
            w = word_with_A(p, A)
            if w is None:
                miss += 1
                continue
            t, u, v = w
            sols = list(slice_sols(p, t, u, v))
            assert sols, (p, A, w)
            for _, _, (x, y, z) in sols:
                assert Fraction(4, p) == Fraction(1, x) + Fraction(1, y) + Fraction(1, z)
        print(f'A={A}: primes with (-A/p)=-1: {tot}, no word with this A: {miss}  (tau(A+1)-1={len(divisors(A+1))-1})')


def universal_exact(A):
    """exact class criterion (Dirichlet: every class r mod lcm(8,A), r = 1 mod 4, gcd(r,A)=1, contains primes):
    A is a universal chi=-1 witness on p = 1 (mod 4) iff for every such r with (-A/r) = -1, -r^{-1} mod A
    is the residue of a divisor of A+1."""
    from math import gcd, lcm
    s, Ao = 0, A
    while Ao % 2 == 0:
        Ao //= 2
        s += 1
    D = {t % A for t in divisors(A + 1)}
    L = lcm(8, A)
    for r in range(1, L, 4):
        if gcd(r, A) != 1:
            continue
        chi = (J(2, r) ** s) * (J(r % Ao, Ao) if Ao > 1 else 1)   # (-A/p) = (A/p) for p = 1 mod 4
        if chi == -1 and (-pow(r, -1, A)) % A not in D:
            return False
    return True


def exact_scan(AMAX):
    return [A for A in range(2, AMAX + 1) if universal_exact(A)]
