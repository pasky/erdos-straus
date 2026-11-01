"""z52d pass2 TO0b Z0108: for numerators m = a*p + b (small a, b), which are 3-term representable (m/p = sum of 3 unit
fractions) for ALL primes p = 1 mod 4 in [5, 2000]? Only m = 0 mod 4 matter for ES (divisor closure: m in M(p), 4 | m
-> 4 in M(p)). Also records the representable fraction for the rest. Brute force over x,y (exact Fractions)."""
from fractions import Fraction as Fr
def isprime(n):
    if n < 2: return False
    i = 2
    while i * i <= n:
        if n % i == 0: return False
        i += 1
    return True
def has3(a, b):
    """a/b = 1/x+1/y+1/z, x<=y<=z, some solution?  (a,b>0)"""
    r = Fr(a, b)
    if r <= 0: return False
    for x in range(int(1 / r) + 1, int(3 / r) + 2):
        r1 = r - Fr(1, x)
        if r1 <= 0: continue
        for y in range(max(x, int(1 / r1) + 1), int(2 / r1) + 2):
            r2 = r1 - Fr(1, y)
            if r2 > 0 and r2.numerator == 1 and r2.denominator >= y:
                return True
    return False
P1 = [p for p in range(5, 2001) if isprime(p) and p % 4 == 1]
P3 = [p for p in range(3, 2001) if isprime(p) and p % 4 == 3]
res = []
for a in range(1, 7):
    for b in range(-4, 5):
        if b == 0 and a == 0: continue
        if (a + b) % 4 != 0: continue  # m = a p + b = 0 mod 4 for p = 1 mod 4
        ok = 0; tot = 0
        for p in P1:
            m = a * p + b
            if m <= 0: continue
            tot += 1
            if has3(m, p): ok += 1
        if tot and ok == tot:
            res.append((a, b, ok, tot))
        if tot: print(f"m={a}p{b:+d} (0 mod 4 for p=1 mod4): representable {ok}/{tot}", flush=True)
print("ALWAYS representable (all p=1 mod 4, 5..2000) with 4|m:", res)
