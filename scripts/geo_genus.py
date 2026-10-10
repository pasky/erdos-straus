"""O126 §5 checks: BL's Brauer class on Type I/II solutions = genus theory of the binary forms [f, 4ad, de].
Type I : form disc -4d,  claim (-d/p) = -1 (equivalently Kronecker(-4d, p) = -1).
Type II: form disc -4dp, claim (f/p) = -(-1/p), Jacobi(-d, f) = -1, and BL's symbol ((-a b)/p) = -1.
Also: the hyperboloid picture: (e,f,a) on e f - 4 d a^2 = 1 (Type I) and the pencil kappa=(f+p)/(4da) in Z.
Run: PYTHONPATH=scripts uv run python scripts/geo_genus.py"""
from math import gcd
from sympy import isprime, jacobi_symbol, legendre_symbol
from sympy.ntheory import factorint
from geo_common import es_solutions
import math


def kron(D, n):
    """Kronecker symbol (D/n) for n>0."""
    J = jacobi_symbol
    r = 1
    while n % 2 == 0:
        n //= 2
        if D % 2 == 0:
            return 0
        r *= 1 if D % 8 in (1, 7) else -1
    return r * (J(D % n, n) if n > 1 else 1)


def abcd(N, X, Y, Z):
    d = gcd(gcd(X, Y), Z); x_, y_, z_ = X//d, Y//d, Z//d
    abc = math.isqrt(x_*y_*z_); assert abc*abc == x_*y_*z_
    return abc//z_, abc//y_, abc//x_, d


nI = nII = 0
for p in range(5, 2500):
    if not isprime(p):
        continue
    for sol in es_solutions(p):
        for perm in [(0, 1, 2), (1, 0, 2), (2, 0, 1)]:
            for sw in (False, True):
                x, y, z = [sol[k] for k in perm]
                if sw:
                    y, z = z, y
                if x % p == 0 and y % p and z % p:          # Type I
                    a, b, c, d = abcd(p, x//p, y, z)
                    e = (a+b)//c; f = 4*a*c*d - p
                    assert e*f - 4*a*a*d == 1
                    assert kron(-4*d, p) == -1 and legendre_symbol((-d) % p, p) == -1
                    assert legendre_symbol((-a*b) % p, p) == -1          # BL Cor 1.3
                    nI += 1
                if x % p and y % p == 0 and z % p == 0:     # Type II
                    a, b, c, d = abcd(p, x, y//p, z//p)
                    e = (a+b)//c; f = 4*a*c*d - 1
                    assert e*f - 4*a*a*d == p and (f+1) % (4*a*d) == 0
                    assert legendre_symbol(f % p, p) == -legendre_symbol(p-1, p)
                    assert jacobi_symbol((-d) % f, f) == -1 if f > 1 else True
                    assert legendre_symbol((-a*b) % p, p) == -1
                    nII += 1
print(f"Type I: (-d/p) = -1 on all {nI} (ordered) solutions;  Type II: (f/p) = -(-1/p), (-d/f) = -1 on all {nII}")
