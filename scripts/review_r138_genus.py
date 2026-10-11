"""R138 from-scratch: genus set G^-_d(n) (classes of primitive positive forms of disc -4dn with chi_{-4d}=-1)
and Type II level-d counts F_d(p).  Checks paper Prop 6.13 (a),(b) and the 19/40 evidence."""
from math import gcd, isqrt
from sympy import isprime
from sympy.ntheory import jacobi_symbol

def kron(D, k):  # Kronecker symbol (D/k), k>0
    r = 1
    while k % 2 == 0:
        k //= 2
        if D % 2 == 0: return 0
        r *= 1 if D % 8 in (1, 7) else -1
    return r * jacobi_symbol(D % k, k) if k > 1 else r

def reduced_forms(D):
    out = []
    a = 1
    while 3 * a * a <= -D:
        for b in range(-a + 1, a + 1):
            if (b * b - D) % (4 * a): continue
            c = (b * b - D) // (4 * a)
            if c < a or (c == a and b < 0): continue
            if gcd(gcd(a, abs(b)), c) != 1: continue
            out.append((a, b, c))
        a += 1
    return out

def chi_form(Q, d, n):
    a, b, c = Q
    for s in range(1, 60):
        for x in range(-s, s + 1):
            for y in (s - abs(x), -(s - abs(x))):
                k = a*x*x + b*x*y + c*y*y
                if k > 0 and gcd(k, 4 * d * n) == 1: return kron(-4 * d, k)
    raise RuntimeError

def Gminus(d, n):
    F = reduced_forms(-4 * d * n)
    return sum(1 for Q in F if chi_form(Q, d, n) == -1), len(F)

# (a) odd squares
for m in range(3, 60, 2):
    for d in range(1, 13):
        if gcd(m, 2 * d) == 1:
            assert Gminus(d, m * m)[0] == 0, (m, d)
# (b) primes p = 1 mod 4, p not dividing 2d
for p in [q for q in range(5, 700) if isprime(q) and q % 4 == 1]:
    for d in range(1, 13):
        if d % p == 0: continue
        g, h = Gminus(d, p)
        assert 2 * g == h, (p, d, g, h)
print("Prop 6.13 (a) m<60 odd, (b) p<700, d<=12: OK")

def Fd(p, d):
    cnt = 0
    for a in range(1, p + 2):
        if 4 * a * d - p > a + 1 and a > (p + 1): break
        for b in range(1, p + 2):
            e = 4 * a * b * d - p
            if e > a + b: break
            if e > 0 and (a + b) % e == 0: cnt += 1
    return cnt

zero = 0; gm = []
for p in (1009, 2689, 4729, 9601, 10009):
    assert p % 120 in [r*r % 120 for r in range(120) if gcd(r,120)==1]
    for d in range(1, 9):
        g, _ = Gminus(d, p); gm.append(g)
        if Fd(p, d) == 0: zero += 1
print("F_d(p)=0 in", zero, "of 40 pairs; #G^- range", min(gm), max(gm))
