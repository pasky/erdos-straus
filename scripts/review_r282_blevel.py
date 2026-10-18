"""R282 from-scratch: evaluate Bright–Loughran's alpha = (-x/z, -y/z) (BM_CORRECTED_COUNT §1 / BL Thm 1.6) at the
level-slicing points P(t, delta): C = t/4, u = (delta+1)/t, v = (N/delta+1)/t, (x,y,z) = (u v C, n v C, n u C), N = t p + 1,
delta | N.  Then alpha(P) = (-v/n, -v/u).  Compute inv_p by the explicit odd-p Hilbert symbol and compare with
chi_{-t}(delta) (SPARKS9 claim) and with -chi_{t}(delta)."""
from fractions import Fraction as F
from sympy import divisors, primerange
import sys

def leg(a, p):
    a %= p
    if a == 0: return 0
    return 1 if pow(a, (p-1)//2, p) == 1 else -1

def vp(x, p):
    x = F(x); n, d = x.numerator, x.denominator; k = 0
    while n % p == 0: n //= p; k += 1
    while d % p == 0: d //= p; k -= 1
    return k, F(n, d)

def hilbert_odd(a, b, p):
    al, u = vp(a, p); be, w = vp(b, p)
    um = u.numerator * pow(u.denominator, -1, p) % p
    wm = w.numerator * pow(w.denominator, -1, p) % p
    s = (-1) ** (al*be*((p-1)//2) % 2)
    return s * leg(um, p)**(be % 2) * leg(wm, p)**(al % 2)

def kron(a, n):
    r = 1; v = 0
    while n % 2 == 0: n //= 2; v += 1
    if v:
        if a % 2 == 0: return 0
        if v % 2 and a % 8 in (3, 5): r = -r
    a %= n
    while a:
        while a % 2 == 0:
            a //= 2
            if n % 8 in (3, 5): r = -r
        a, n = n, a
        if a % 4 == 3 and n % 4 == 3: r = -r
        a %= n
    return r if n == 1 else 0

PB, TB = int(sys.argv[1]), int(sys.argv[2])
stats = {1: [0, 0, 0, 0], 3: [0, 0, 0, 0]}  # [total, agree chi_{-t}, agree -chi_t, nongeneric]
for p in primerange(5, PB):
    for t in range(4, TB+1, 4):
        N = t*p + 1
        for d in divisors(N):
            if (d + 1) % p == 0:
                stats[p % 4][3] += 1; continue
            u = F(d + 1, t); v = F(N//d + 1, t)
            inv = hilbert_odd(-v/p, -v/u, p)
            s = stats[p % 4]; s[0] += 1
            s[1] += (inv == kron(-t, d)); s[2] += (inv == -kron(t, d))
for r in (1, 3):
    s = stats[r]
    print(f"p=={r} mod 4: points={s[0]}  inv_p==chi_(-t)(d): {s[1]}  inv_p==-chi_t(d): {s[2]}  skipped p|d+1: {s[3]}")
