"""Small, stdlib-only O157 checks; run under the resource limits in the brief.
No large arrays: scalar loops, divisors/factorisations of integers below 10000.
"""
from math import gcd, isqrt


def divisors(n):
    return [d for d in range(1, n + 1) if n % d == 0]


def factors(n):
    out = []
    for r in range(2, isqrt(n) + 1):
        if n % r == 0:
            out.append(r)
            while n % r == 0:
                n //= r
    if n > 1:
        out.append(n)
    return out


def witnesses(n):
    # II: e=4abd-n and 1<=e<=a+b give a finite b interval.
    for a in range(1, n + 1):
        if 4 * a * a > n + 2 * a:
            break
        for d in range(1, (n + 2 * a) // (4 * a * a) + 1):
            lo = max(a, (n + 4 * a * d) // (4 * a * d))
            hi = (n + a) // (4 * a * d - 1)
            for b in range(lo, hi + 1):
                e = 4 * a * b * d - n
                if (a + b) % e == 0:
                    return 'II', (a, b, (a + b) // e, d, e)
    # I: b(4acd-n)=na+c; a<=b and c<=2b give 4acd<=2n+2.
    for a in range(1, (2 * n + 2) // 4 + 1):
        for c in range(1, (2 * n + 2) // (4 * a) + 1):
            for d in range(n // (4 * a * c) + 1, (2 * n + 2) // (4 * a * c) + 1):
                denom = 4 * a * c * d - n
                b, rem = divmod(n * a + c, denom)
                if not rem and b >= a and (a + b) % c == 0:
                    e = (a + b) // c
                    assert 4 * a * b * d == n * e + 1
                    return 'I', (a, b, c, d, e)
    return None


checks = 0
for n in range(2, 32):
    for a in range(1, 7):
        for b in range(1, 7):
            for d in range(1, 7):
                assert (n + 4*a*a*d)*(n + 4*b*b*d) == (n + 4*a*b*d)**2 + 4*d*n*(a-b)**2
                for c in range(1, 7):
                    assert (n + 4*a*a*d)*(4*c*c*d*n + 1) == n*(4*a*c*d-1)**2 + 4*d*(c*n+a)**2
                    checks += 1
print('C1/C2 checked:', checks, 'parameter tuples')
empty = [n for n in range(2, 401) if witnesses(n) is None]
assert empty == [n for n in range(2, 401) if isqrt(n)**2 == n or n in (288, 336)]
print('Full emptiness through 400:', empty)
print('4545 (different from the W statistic):', witnesses(4545))

# Literal class definitions overlap: prime and Q for p=13,a=1,d=1.
p, a, d = 13, 1, 1
q, N = 4*a*d, p + 4*a*a*d
assert factors(N) == [N] and not any(f % q == q-1 for f in divisors(N))
assert N % 4 == 1 and (q - 1) % 4 == 3
print('Prime/Q overlap unless priority specified:', (p, a, d, N, q), 'character chi_-4')

# On small square slices, directly enumerate all homomorphisms to F_2
# through their standard quadratic-character generators; ignore nonunits.
square_checks = 0
for m in range(3, 20, 2):
    n = m*m
    for a in range(1, isqrt(n) + 1):
        for d in range(1, (n + 2*a)//(4*a*a) + 1):
            q, N = 4*a*d, n + 4*a*a*d
            odd = [r for r in factors(q) if r != 2]
            def sign(x):
                out = [int(x % 4 == 3)]
                if q % 8 == 0:
                    out.append(int(x % 8 in (3, 5)))
                out.extend(int(pow(x % r, (r-1)//2, r) == r-1) for r in odd)
                return sum(bit << j for j, bit in enumerate(out))
            span = {0}
            for r in factors(N):
                if gcd(r, q) == 1:
                    v = sign(r)
                    span |= {x ^ v for x in span}
            assert sign(q-1) not in span
            square_checks += 1
print('Square Q checks (unit factors):', square_checks)

checks = 0
for a in range(1, 31):
    for b in range(a, 31):
        q = 4*a*b
        for e in divisors(a+b):
            if (e*e - 1) % q:
                continue
            for n in range(3, 200, 2):
                assert ((n+e) % q == 0) == ((n*e+1) % q == 0)
                checks += 1
print('Twin equivalences (all odd n, not just primes):', checks)
