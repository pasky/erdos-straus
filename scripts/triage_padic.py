"""Small independent counterexample checks for O157 part 6; no campaign imports.

Run under ulimit -v 4000000 and timeout 600. Polynomial lists have degree <= 12;
all loops here are finite, streamed and single-threaded.
"""
from fractions import Fraction
from itertools import product
from math import isqrt


def prime(n):
    return n >= 2 and all(n % d for d in range(2, isqrt(n) + 1))


# Prop B's parenthetical confuses n-divisibility with ET coprimality.
assert sum(Fraction(1, u) for u in (3, 12, 36)) == Fraction(4, 9)
assert sum(u % 9 == 0 for u in (3, 12, 36)) == 1
print("Odd square n=9: (3,12,36) has exactly one denominator divisible by n.")

# Finite illustration of the Dirichlet sequence p_k -> -7 in Z_2.
# The proof uses Dirichlet for every k, not this finite list.
previous = 1
sequence = []
for k in range(3, 14):
    modulus = 2**k
    candidate = -7 + ((previous + 7) // modulus + 1) * modulus
    while not prime(candidate):
        candidate += modulus
    assert candidate > previous and (candidate + 7) % modulus == 0
    assert candidate % 8 == 1
    sequence.append(candidate)
    previous = candidate
print("Primes converging toward -7, k=3..13:", sequence)


# From-scratch finite-field chart: numerator T^2, square denominator R^2.
def trim(a, q):
    a = [x % q for x in a]
    while len(a) > 1 and a[-1] == 0:
        a.pop()
    return tuple(a)


def add(a, b, q, sign=1):
    return trim([(a[i] if i < len(a) else 0)
                 + sign * (b[i] if i < len(b) else 0)
                 for i in range(max(len(a), len(b)))], q)


def mul(a, b, q):
    c = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            c[i + j] += x * y
    return trim(c, q)


def divmod_poly(a, b, q):
    assert b != (0,)
    r = list(a)
    quotient = [0] * max(1, len(a) - len(b) + 1)
    while tuple(r) != (0,) and len(r) >= len(b):
        shift = len(r) - len(b)
        factor = r[-1] * pow(b[-1], -1, q) % q
        quotient[shift] = factor
        for j, coefficient in enumerate(b):
            r[j + shift] -= factor * coefficient
        r = list(trim(r, q))
    return trim(quotient, q), tuple(r)


def monics(degree, q):
    return (tuple(c) + (1,) for c in product(range(q), repeat=degree))


def irreducible_quadratic(r, q):
    return all(sum(c * x**i for i, c in enumerate(r)) % q for x in range(q))


def square_witness(q):
    A = (0, 0, 1)
    for R in monics(2, q):
        if not irreducible_quadratic(R, q):
            continue
        P = mul(R, R, q)
        for da in range(3):
            for db in range(3 - da):
                dd = 2 - da - db
                for a, b, d in product(monics(da, q), monics(db, q), monics(dd, q)):
                    x = mul(mul(a, b, q), d, q)
                    e = add(mul(A, x, q), P, q, -1)
                    if e == (0,):
                        continue
                    c, remainder = divmod_poly(add(a, b, q), e, q)
                    if remainder != (0,) or c == (0,) or c[-1] != 1:
                        continue
                    # Ensure the ET coprimality condition, not merely P nondivisibility.
                    if divmod_poly(x, R, q)[1] == (0,):
                        continue
                    y = mul(mul(mul(a, c, q), d, q), P, q)
                    z = mul(mul(mul(b, c, q), d, q), P, q)
                    lhs = mul(A, mul(mul(x, y, q), z, q), q)
                    rhs = mul(P, add(add(mul(x, y, q), mul(y, z, q), q),
                                     mul(z, x, q), q), q)
                    assert lhs == rhs
                    assert all(u[-1] == 1 for u in (x, y, z))
                    assert all(len(u) - 1 >= len(P) - len(A) for u in (x, y, z))
                    assert divmod_poly(y, P, q)[1] == (0,)
                    assert divmod_poly(z, P, q)[1] == (0,)
                    return R, P, a, b, c, d, (x, y, z)
    return None


for q in (5, 7):
    witness = square_witness(q)
    if q == 5:
        assert witness is not None, "Expected the explicit square counterexample over F_5"
    print(f"F_{q}[T], numerator T^2, Type-II square witness (ascending coefficients):", witness)
    if witness is not None:
        R, P, a, b, c, d, denominators = witness
        print(f"  R={R}, P=R^2={P}, (a,b,c,d)={(a,b,c,d)}, (X,Y,Z)={denominators}")
print("All exact counterexample checks passed.")
