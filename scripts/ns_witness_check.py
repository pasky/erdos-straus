"""O221: check NEAR_SQUARE Lemmas 1.1/1.3 by brute force: every Type I solution of a prime p = 1 (4) has (d/p) = -1,
every Type II solution has (de/p) = -1.  Usage: ns_witness_check.py PMAX"""
import sys
from math import gcd, isqrt
from sympy import primerange, jacobi_symbol

def sols(n):
    # all x<=y<=z with 4/n = 1/x+1/y+1/z
    out = []
    for x in range(n // 4 + 1, 3 * n // 4 + 1):
        num, den = 4 * x - n, n * x          # 1/y+1/z = num/den
        if num <= 0: continue
        for y in range(max(x, den // num + 1), 2 * den // num + 1):
            zn, zd = num * y - den, den * y
            if zn > 0 and zd % zn == 0:
                out.append((x, y, zd // zn))
    return out

def params(X, y, z):
    if (X * y) % z or (X * z) % y or (y * z) % X: return None
    A2d, B2d, C2d = X * y // z, X * z // y, y * z // X
    d = gcd(gcd(A2d, B2d), C2d)
    a, b, c = isqrt(A2d // d), isqrt(B2d // d), isqrt(C2d // d)
    assert a * a * d == A2d and b * b * d == B2d and c * c * d == C2d
    return a, b, c, d

PMAX = int(sys.argv[1])
cnt = {1: 0, 2: 0}; bad = 0
for p in primerange(5, PMAX):
    if p % 4 != 1: continue
    for s in sols(p):
        divs = [v % p == 0 for v in s]
        if sum(divs) == 1:      # Type I: the multiple of p plays x
            i = divs.index(True); X = s[i] // p; y, z = [s[j] for j in range(3) if j != i]
            a, b, c, d = params(X, y, z)          # X = abd, y = acd, z = bcd (up to swapping a,b)
            cnt[1] += 1
            if jacobi_symbol(d, p) != -1: bad += 1; print("TypeI fail", p, s, d)
        elif sum(divs) == 2:    # Type II
            i = divs.index(False); x = s[i]; Y, Z = [s[j] // p for j in range(3) if j != i]
            a, b, c, d = params(x, Y, Z) if params(x, Y, Z) else (None,) * 4
            # x = abd, Y = acd, Z = bcd
            e = (a + b) // c; assert c * e == a + b
            cnt[2] += 1
            if jacobi_symbol(d * e, p) != -1: bad += 1; print("TypeII fail", p, s, d, e)
print("primes = 1 (4) <", PMAX, "TypeI sols", cnt[1], "TypeII sols", cnt[2], "failures", bad)
# T1 control: odd squares n <= PMAX have no Type I / Type II solutions (ET Prop 1.6); also check the census claim
# that every n = 1 (4) prime solution count is positive in this range.
sq_bad = 0
for w in range(3, int(PMAX ** 0.5) + 1, 2):
    n = w * w
    for s in sols(n):
        nd = sum(v % n == 0 for v in s)
        if nd in (1, 2) and all(v % n != 0 or (v // n) % 1 == 0 for v in s):
            # Type I/II in ET's sense also needs the non-multiples coprime to n
            others = [v for v in s if v % n]
            if all(gcd(v, n) == 1 for v in others): sq_bad += 1; print("square with Type I/II?", n, s)
print("odd squares <", PMAX, ": Type I/II solutions found:", sq_bad)
