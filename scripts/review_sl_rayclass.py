"""R175: from-scratch check of bsB_rayclass_norm_pullback item 3 (genus product formula on norms).
For t = 3 mod 4 squarefree, p = 1 mod 4 prime, p not | t: every m coprime to tp represented by a primitive form
of discriminant -tp has (m/t)_Jacobi = (m/p); hence m = +-1 mod t  =>  (m/p) = +-1."""
from math import gcd, isqrt
def jac(a, n):
    a %= n; s = 1
    while a:
        while a % 2 == 0:
            a //= 2
            if n % 8 in (3, 5): s = -s
        a, n = n, a
        if a % 4 == 3 and n % 4 == 3: s = -s
        a %= n
    return s if n == 1 else 0
def sqfree(n): return all(n % (q*q) for q in range(2, isqrt(n) + 1))
def isprime(n): return n > 1 and all(n % q for q in range(2, isqrt(n) + 1))
def forms(D):  # reduced primitive forms disc D<0
    out = []
    a = 1
    while 3 * a * a <= -D:
        for b in range(-a + 1, a + 1):
            if (b * b - D) % (4 * a) == 0:
                c = (b * b - D) // (4 * a)
                if c >= a and gcd(gcd(a, abs(b)), c) == 1 and not (b < 0 and (a == c)):
                    out.append((a, b, c))
        a += 1
    return out
viol = tested = pm = 0
for t in [3, 7, 11, 15, 19, 23, 31, 35, 39, 43]:
    if not sqfree(t): continue
    for p in [5, 13, 17, 29, 37, 41, 53, 61]:
        if t % p == 0: continue
        D = -t * p
        for (a, b, c) in forms(D):
            for x in range(-30, 31):
                for y in range(-30, 31):
                    m = a*x*x + b*x*y + c*y*y
                    if m <= 0 or gcd(m, t * p) != 1: continue
                    tested += 1
                    if jac(m, t) != jac(m, p): viol += 1
                    if m % t in (1, t - 1):
                        pm += 1
                        if jac(m, p) != (1 if m % t == 1 else -1): viol += 1
print("represented m tested", tested, "of which m=+-1 mod t:", pm, "violations", viol)
