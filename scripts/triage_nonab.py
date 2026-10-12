"""Small independent counterchecks for O157 part 5; standard library only.

Run under the brief's memory/time limits. Largest enumeration: 5^3 points;
no large arrays, external data, or parallelism.
"""
from fractions import Fraction
from itertools import permutations, product


def field_ops(q):
    if q != 4:
        return (lambda a, b: (a + b) % q,
                lambda a, b: (a * b) % q)

    def mul(a, b):
        v = 0
        while b:
            if b & 1:
                v ^= a
            a <<= 1
            if a & 4:
                a ^= 7  # F_2[t]/(t^2+t+1)
            b >>= 1
        return v

    return (lambda a, b: a ^ b), mul


for q in (2, 3, 4, 5):
    add, mul = field_ops(q)
    four = 0 if q in (2, 4) else 4 % q
    for n in (0, 1):
        count = sum(
            mul(four, mul(x, mul(y, z)))
            == mul(n, add(add(mul(x, y), mul(y, z)), mul(z, x)))
            for x, y, z in product(range(q), repeat=3)
        )
        corrected = ((q**3 if n == 0 else q**2) if q in (2, 4)
                     else (3*q*q - 3*q + 1 if n == 0 else q*q + 1))
        assert count == corrected
        print(f"F_{q}, n={n}: {count} points")

# D2's proposed natural prime-square extension of Frobenius uses g -> g^2.
# A_5 has trivial abelianisation but its double transpositions are not squares.
a5 = [g for g in permutations(range(5))
      if sum(g[i] > g[j] for i in range(5) for j in range(i+1, 5)) % 2 == 0]
squares = {tuple(g[g[i]] for i in range(5)) for g in a5}
double_transposition = (1, 0, 3, 2, 4)
assert double_transposition in a5 and double_transposition not in squares
print(f"A5: {len(a5)} elements, {len(squares)} square images; (01)(23) is not a square")

# F5: exact polynomial identity, checked off as well as on the ES surface.
checks = 0
for n in range(1, 10):
    for x, y, z in product(range(-2, 5), repeat=3):
        lhs = ((4*x-n)*y-n*x)*((4*x-n)*z-n*x)-(n*x)**2
        rhs = (4*x-n)*(4*x*y*z-n*(x*y+x*z+y*z))
        assert lhs == rhs
        checks += 1
print(f"F5 expansion verified on {checks} tuples")

# H1 is Type I, not II: ef-4da^2=1, c=(f+p)/(4da).
p, a, d, e, f = 7, 1, 1, 1, 5
assert e*f - 4*d*a*a == 1
assert (f+p) % (4*d*a) == 0
c = (f+p)//(4*d*a)
b = c*e-a
xyz = (a*b*d*p, a*c*d, b*c*d)
assert sum(Fraction(1, t) for t in xyz) == Fraction(4, p)
assert sum(t % p == 0 for t in xyz) == 1
print(f"H1 example p={p}: denominators {sorted(xyz)} are Type I")
