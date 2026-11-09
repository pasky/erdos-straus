"""z69 NL7 common helpers: U7 words, letter tests.
U7 word of n: positive (x,y,z), x*y*z - x - z = n, 8 | x*y.
"""
from math import gcd, isqrt
from sympy import divisors, isprime, factorint

def lcm(a, b):
    return a // gcd(a, b) * b

def words_brute(n):
    """All U7 words of n by the f-loop: f = xy-1 ≡ 7 (8), r = -n mod f, r | f+1 (x = r < f),
    plus the y = 1 words (x = f+1, f | n+1).  O(n)."""
    out = []
    f = 7
    while f <= 2 * n + 1:
        r = (-n) % f
        if r > 0 and (f + 1) % r == 0:
            x, y, z = r, (f + 1) // r, (n + r) // f
            assert x * y * z - x - z == n and (x * y) % 8 == 0
            out.append((x, y, z))
            if r == 1:  # the y = 1 word with x = f+1 (x >= f is not seen as a residue)
                out.append((f + 1, 1, (n + 1) // f + 1))
        f += 8
    return out

def words_with_x(n, L, divs=None):
    """U7 words with x = L: divisors f of n+L, f ≡ -1 mod lcm(8,L)."""
    M = lcm(8, L)
    out = []
    for f in (divs if divs is not None else divisors(n + L)):
        if f % M == M - 1:
            out.append((L, (f + 1) // L, (n + L) // f))
    return out

def words_with_z(n, L, divs=None):
    """U7 words with z = L: e = yL-1 | n+L, x = (n+L)/e, 8 | xy."""
    out = []
    for e in (divs if divs is not None else divisors(n + L)):
        if (e + 1) % L == 0:
            y = (e + 1) // L
            x = (n + L) // e
            if (x * y) % 8 == 0:
                out.append((x, y, L))
    return out

def words_with_y(n, L, divs=None):
    """U7 words with y = L: F | Ln+1, F ≡ -1 mod lcm(8,L); x=(F+1)/L, z=(G+1)/L."""
    M = lcm(8, L)
    N = L * n + 1
    out = []
    for F in (divs if divs is not None else divisors(N)):
        if F % M == M - 1:
            G = N // F
            assert (G + 1) % L == 0
            out.append(((F + 1) // L, L, (G + 1) // L))
    return out

def words_with_letter(n, L):
    d1 = divisors(n + L)
    return words_with_x(n, L, d1) + words_with_z(n, L, d1) + words_with_y(n, L)

def two_squares(p):
    """p ≡ 1 (4) prime -> (a,b), a odd, b even, a^2+b^2=p."""
    # Cornacchia
    r = None
    for g in range(2, p):
        if pow(g, (p - 1) // 2, p) == p - 1:
            r = pow(g, (p - 1) // 4, p)
            break
    a, b = p, r
    while b * b > p:
        a, b = b, a % b
    c = isqrt(p - b * b)
    assert b * b + c * c == p
    return (b, c) if b % 2 == 1 else (c, b)
