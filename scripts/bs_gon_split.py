"""O148 brainstorm: checks for BRAINSTORM/gon_fermat_certificates.md Lemma 3.1.

(1) symbolic: ET Type I/II (c,d)-slices are split binary level sets XY = N.
(2) brute force, small p: the bijection between (c,d)-slice witnesses and divisor-in-class events,
    compared against a direct ES(p) Type I/II enumeration in ET coordinates.
"""
import sympy as sp
from sympy import primerange, divisors

a, b, c, d, p = sp.symbols('a b c d p', positive=True, integer=True)
# Type I: p*e+1 = 4abd, a+b = c e  => p(a+b) = c(4abd-1)
lhs1 = sp.expand((4*a*c*d - p) * (4*b*c*d - p) - (p**2 + 4*c**2*d))
rel1 = p*(a + b) - c*(4*a*b*d - 1)
print("Type I residue mod relation:", sp.simplify(lhs1 + 4*c*d*rel1))
# Type II: p+e = 4abd, a+b = c e  => c p = 4abcd - a - b
lhs2 = sp.expand((4*a*c*d - 1) * (4*b*c*d - 1) - (4*c**2*d*p + 1))
rel2 = c*p - (4*a*b*c*d - a - b)
print("Type II residue mod relation:", sp.simplify(lhs2 + 4*c*d*rel2))


def direct(pp, T):
    """ET coordinates (a<=b,c,d,e) for prime pp, Type T, by e-slices.
    Bounds: Type II e <= (p+4)/3 (ab >= a+b-1 >= e-1, ab <= N); Type I e <= a+b <= 2N/1 with
    the slice bound (see via_slices) giving e <= p^2 + 4p (generous)."""
    out = set()
    emax = pp + 4 if T == 'II' else pp * pp + 4 * pp
    for e in range(1, emax + 1):
        M = pp + e if T == 'II' else pp * e + 1
        if M % 4:
            continue
        N = M // 4
        for aa in divisors(N):
            for bb in divisors(N // aa):
                if aa <= bb and (aa + bb) % e == 0:
                    out.add((aa, bb, (aa + bb) // e, N // (aa * bb), e))
    return out


def via_slices(pp, T):
    """Bounds: Type I needs 4cd - 2c*sqrt(d) <= 2p (both factors >= 4cd - p); we loop cd <= 2p.
    Type II needs 4d <= p + 1 (both factors >= 4cd - 1) and c <= (p+5)/4."""
    out = set()
    cmax = 2 * pp if T == 'I' else (pp + 5) // 4
    for cc in range(1, cmax + 1):
        dmax = (2 * pp) // cc if T == 'I' else (pp + 1) // 4
        for dd in range(1, dmax + 1):
            q = 4 * cc * dd
            N = pp * pp + 4 * cc * cc * dd if T == 'I' else 4 * cc * cc * dd * pp + 1
            r = (-pp) % q if T == 'I' else q - 1
            s = pp if T == 'I' else 1
            for X in divisors(N):
                Y = N // X
                if X <= Y and X % q == r and Y % q == r:
                    aa, bb = (X + s) // q, (Y + s) // q
                    e = (4 * aa * bb * dd - 1) // pp if T == 'I' else 4 * aa * bb * dd - pp
                    out.add((aa, bb, cc, dd, e))
    return out


if __name__ == "__main__":
    for pp in primerange(5, 60):
        for T in ('I', 'II'):
            A, B = direct(pp, T), via_slices(pp, T)
            assert A == B, (pp, T, sorted(A ^ B)[:5])
    print("slice bijection checked for primes 5..59, both types")
