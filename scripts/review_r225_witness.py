# R225 from-scratch check of Lemmas 1.1 / 1.3 (witness dictionary).
# Enumerates ALL N-points of Sigma^I_n, Sigma^II_n (both orientations a<=b and a>b, via direct
# enumeration with generous bounds), checks: Type I: Jacobi(-4d/n) = -1 (n odd);
# Type II, n = 1 mod 4: (f/n) = -1; (de/n) = -1 when gcd(n,2ad)=1.
import sys
from math import gcd
def jac(a, n):
    assert n > 0 and n % 2 == 1
    a %= n; r = 1
    while a:
        while a % 2 == 0:
            a //= 2
            if n % 8 in (3, 5): r = -r
        a, n = n, a
        if a % 4 == 3 and n % 4 == 3: r = -r
        a %= n
    return r if n == 1 else 0
N = int(sys.argv[1])
cnt1 = cnt2 = bad = 0
for n in range(3, N, 2):
    # Type I: from Lemma-2.8-free enumeration: 4acd = n + f, f>0; need all a,c,d with acd bounded.
    # Without a<=b, bf = na + c with b>=1 gives f <= na+c; we bound acd <= n (a<=b) and also enumerate reflection.
    sols1 = set()
    for a in range(1, n + 1):
        for c in range(1, n // a + 1):
            for d in range(1, n // (a * c) + 1):
                f = 4 * a * c * d - n
                if f <= 0: continue
                if (n * a + c) % f or (4 * a * a * d + 1) % f: continue
                b = (n * a + c) // f; e = (4 * a * a * d + 1) // f
                if c * e != a + b or 4 * a * b * d != n * e + 1: continue
                sols1.add((a, b, c, d, e, f)); sols1.add((b, a, c, d, e, 4 * b * c * d - n))
    for (a, b, c, d, e, f) in sols1:
        assert f > 0 and e * f == 4 * a * a * d + 1 and b * f == n * a + c
        cnt1 += 1
        if jac(-4 * d, n) != -1: bad += 1; print("TypeI fail", n, (a, b, c, d, e, f))
    if n % 4 != 1: continue
    sols2 = set()
    for a in range(1, n + 1):
        for c in range(1, n // a + 1):
            for d in range(1, n // (a * c) + 1):
                f = 4 * a * c * d - 1
                if (n + 4 * a * a * d) % f: continue
                e = (n + 4 * a * a * d) // f; b = c * e - a
                if b <= 0 or 4 * a * b * d != n + e: continue
                f2 = (4 * c * c * d * n + 1)
                assert f2 % f == 0
                sols2.add((a, b, c, d, e, f)); sols2.add((b, a, c, d, e, f2 // f))
    for (a, b, c, d, e, f) in sols2:
        assert 4 * a * c * d == f + 1 and e * f == n + 4 * a * a * d
        cnt2 += 1
        if jac(f, n) != -1: bad += 1; print("TypeII f fail", n, (a, b, c, d, e, f))
        if gcd(n, 2 * a * d) == 1 and jac(d * e, n) != -1: bad += 1; print("TypeII de fail", n, (a, b, c, d, e, f))
print("TypeI", cnt1, "TypeII", cnt2, "bad", bad)
