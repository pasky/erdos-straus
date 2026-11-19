"""Finite residue/valuation stress tests, not simulations of field embeddings.

Run: uv run --no-project python scripts/z73_adelic_rows.py
"""

from fractions import Fraction as F
from math import gcd, isqrt, prod


def primes(n):
    return [q for q in range(2, n + 1) if all(q % d for d in range(2, isqrt(q) + 1))]


def integral(x, q):
    return F(x).denominator % q != 0


def exceptional_rows():
    # P=1 in the residue field. First a Dirichlet task Q=1+Y, then
    # (P-1)U+Y(Y-1)V=1, then (P-1)W+(V-1)X=1. The second row is
    # generically feasible at P=1, but can depend on the first row's lift.
    failures = [[], []]
    for q in primes(199):
        first, second = set(), set()
        for y in range(q):
            if (1 + y) % q == 0:
                continue
            b = y * (y - 1) % q
            if b:
                first.add(y)
                v = pow(b, -1, q)
                if (v - 1) % q:
                    second.add(y)
                    x = pow(v - 1, -1, q)
                    assert b * v % q == (v - 1) * x % q == 1
        if not first:
            failures[0].append(q)
        if not second:
            failures[1].append(q)
        if q == 5:
            assert first == {2, 3} and second == {2}
    assert failures == [[2, 3], [2, 3]]
    print('Two successive row prefixes with Q=1+Y: exceptional primes', failures)


def denominator_repair():
    # Where integral inputs are both nonunits, a field solution need not
    # be integral. Normalize by the ideal content, not by a unit scale of H.
    # H=q^2 and Y chosen locally; the rank-one generator h=H itself has
    # positive valuation everywhere tested, but the residual pair (H,Y)
    # has common content only at 2 and 3.
    qs = primes(199)
    gamma = 6
    for q in qs:
        h = q**2
        y = q if q in (2, 3) else 2
        a, b = h*h, h*y
        f, g = F(a, gamma*h), F(b, gamma*h)
        assert integral(f, q) and integral(g, q)
        assert integral(1/f, q) or integral(1/g, q)

    # An old solution to 2u+3v=1 contaminated at two different primes.
    # Correct by ONE parameter; its q-parts need not equal a chosen global
    # annihilator of the contamination.
    u, v = F(1, 2) + 3*F(1, 90), -2*F(1, 90)
    assert 2*u + 3*v == 1
    bad = [q for q in qs if not (integral(u, q) and integral(v, q))]
    assert bad == [3, 5]
    targets = {3: v/2, 5: -u/3}  # f=2 is a unit at 3; g=3 a unit at 5.
    D = prod(t.denominator for t in targets.values())
    # D may include other primes; forbid new poles there. CRT in local
    # coordinates, using mod q^ord_q(D) rather than just mod q.
    k, M = 0, 1
    for q in primes(D):
        m = 1
        while D % (q*m) == 0:
            m *= q
        if m == 1:
            continue
        t = D * targets.get(q, F(0))
        assert gcd(t.denominator, m) == 1
        r = t.numerator * pow(t.denominator, -1, m) % m
        k += M * ((r-k) * pow(M, -1, m) % m)
        M *= m
    tau = F(k, D)
    U, V = u+3*tau, v-2*tau
    assert U.denominator == V.denominator == 1 and 2*U+3*V == 1
    print(f'CRT: ({u}, {v}) + ({3*tau}, {-2*tau}) = ({U}, {V})')


if __name__ == '__main__':
    exceptional_rows()
    denominator_repair()
