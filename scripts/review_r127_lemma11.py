"""R127 from-scratch check of CONDITIONAL_ES Lemma 1.1, dual form (Sec 6), remainder form (7.5),
and the claim 'S'(p)=S(p) up to O(1)'. Independent of cond_* scripts."""
from fractions import Fraction as F
import sys
N = int(sys.argv[1]) if len(sys.argv) > 1 else 400

def form2(n):  # (c,f,g): c(fg-1)-f=n, fg=1 mod 4; brute force over c,f (g determined)
    out = set()
    for c in range(1, n + 3):
        for f in range(1, n + 3):
            num = n + c + f
            if num % (c * f): continue
            g = num // (c * f)
            if (f * g) % 4 == 1: out.add((c, f, g))
    return out

def form1(n):  # (t,m): m | tn+1, 4|m, m = -1 mod t, cofactor = -1 mod t; mapped to (c,f,g)
    out = set()
    for t in range(1, n + 3):
        N1 = t * n + 1
        for m in range(4, N1 + 1, 4):
            if N1 % m == 0 and (m + 1) % t == 0:
                mm = N1 // m
                assert (mm + 1) % t == 0  # cofactor automatic
                out.add(((mm + 1) // t, (m + 1) // t, t))
    return out

def form3(n):
    out = set()
    for c in range(1, n + 3):
        for f in range(1, n + 3):
            s = n + c + f
            if s % (c * f) == 0 and (f * s // (c * f)) % 4 == 1: out.add((c, f, s // (c * f)))
    return out

def dual(n):  # exists m=0 mod4 coprime n, least pos residue g of -n^{-1} mod m divides m+1
    for m in range(4, 4 * n + 12, 4):
        from math import gcd
        if gcd(m, n) != 1: continue
        g = (-pow(n, -1, m)) % m
        if g == 0: g = m
        if (m + 1) % g == 0: return True
    return False

def remainder(n):  # m=4d, c>=1, f=cm-n>0, f | m+1
    for m in range(4, 4 * n + 12, 4):
        for c in range(n // m + 1, (n + m + 1) // m + 1):
            f = c * m - n
            if f > 0 and (m + 1) % f == 0: return True
    return False

def remainder2(n):  # c>=1, divisor f of n+c with f=-n mod 4c, f <= (n+f)/c+1
    for c in range(1, n + 3):
        s = n + c
        for f in range(1, s + 1):
            if s % f == 0 and (f + n) % (4 * c) == 0 and f <= (n + f) // c + 1: return (c, f)
    return None

bad = 0; nsol = 0; pdivc = 0; disagree_r2 = []
for n in range(1, N):
    s2 = form2(n); s1 = form1(n); s3 = form3(n)
    if not (s1 == s2 == s3): print("MISMATCH", n); bad += 1
    for (c, f, g) in s2:
        d = (f * g - 1) // 4; b = (n + c) // f
        assert (n + c) % f == 0 and b == c * g - 1 and d >= 1 and b >= 1
        assert F(4, n) == F(1, b * d * n) + F(1, c * d) + F(1, b * c * d)
        nsol += 1
        if c % n == 0 and n > 3: pdivc += 1
    if n % 2 and n > 1:
        if dual(n) != bool(s2): print("DUAL MISMATCH", n); bad += 1
        if remainder(n) != bool(s2): print("REM MISMATCH", n); bad += 1
        r2 = remainder2(n)
        if bool(r2) != bool(s2): disagree_r2.append((n, r2))
print("n<", N, "slice solutions checked:", nsol, "mismatches:", bad, "solutions with n|c (n>3):", pdivc)
print("remainder2 (divisor-of-n+c form) disagreements:", disagree_r2[:20], len(disagree_r2))
