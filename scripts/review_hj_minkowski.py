"""R174: from-scratch check of bsA_minkowski_stern M1, M2.
M1: for 0<A<n coprime, ?(A/n) = m/2^k and r(n/A) (HJ length, direct ceiling algorithm) = popcount(m).
?(x) computed from the series ?([0;a1,a2,...]) = 2*sum_j (-1)^(j+1) 2^-(a1+...+aj)  (Salem's formula; exact big ints).
M2: for k<=13, 0<m<2^k: ?(s(m)/s(2^k+m)) = m/2^k (Stern's diatomic s), and gcd(s(m),s(2^k+m))=1.
Usage: python review_hj_minkowski.py NMAX"""
import sys
from math import gcd
NMAX = int(sys.argv[1])

def cf(a, b):                       # regular CF of a/b
    out = []
    while b: q = a // b; out.append(q); a, b = b, a - q * b
    return out

def qmark_num(A, n):                # returns integer M with ?(A/n) = M / 2^S
    a = cf(A, n)[1:]                # A/n = [0; a1, a2, ...]
    S = sum(a); M = 0; s = 0
    for j, aj in enumerate(a, 1):
        s += aj; M += (1 if j % 2 else -1) * 2 * (1 << (S - s))
    return M, S

def hjlen(x, y):
    r = 0
    while y:
        b = -(-x // y); x, y = y, b * y - x; r += 1
    return r

bad = tot = 0
for n in range(2, NMAX):
    for A in range(1, n):
        if gcd(A, n) != 1: continue
        M, S = qmark_num(A, n); tot += 1
        if bin(M).count("1") != hjlen(n, A): bad += 1; print("M1 FAIL", n, A) if bad < 5 else None
print(f"M1: {tot} coprime pairs n<{NMAX}, {bad} failures")
s = [0, 1]
for N in range(2, 2 ** 15): s.append(s[N // 2] if N % 2 == 0 else s[N // 2] + s[N // 2 + 1])
bad = tot = 0
for k in range(1, 14):
    for m in range(1, 2 ** k):
        A, n = s[m], s[2 ** k + m]; tot += 1
        M, S = qmark_num(A, n)
        if gcd(A, n) != 1 or M * 2 ** k != m * 2 ** S: bad += 1
print(f"M2: {tot} (k,m) pairs, {bad} failures")
# bsA_farey_lnr_pigeonhole Lemma 2: r(n/A) + r(n/(n-A)) = sum of regular partial quotients of n/A; Lemma 1: r(p/q) <= q
bad = tot = 0
for n in range(3, NMAX):
    for A in range(1, n):
        if gcd(A, n) != 1: continue
        tot += 1
        if hjlen(n, A) + hjlen(n, n - A) != sum(cf(n, A)): bad += 1
        if A < n and hjlen(n, A) > A: bad += 1
print(f"Lemma 2 (+ r(n/A) <= A): {tot} pairs n<{NMAX}, {bad} failures")
# Thm 3 sanity: sum_{A<p} S(A) vs (6/pi^2) p ln^2 p, and lambda(p) vs bound
import math
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
for p in (10009, 100049):
    S = sum(sum(cf(p, A)) for A in range(1, p))
    lam = min(hjlen(p, A) for A in range(1, p) if jac(A, p) == -1)
    print(p, "sum S / (p ln^2 p) =", round(S / (p * math.log(p) ** 2), 4), "(6/pi^2 = 0.6079)", "lambda =", lam)
