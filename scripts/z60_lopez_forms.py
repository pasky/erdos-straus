"""z60 LOPEZ: check equivalent forms of the López/U_II predicate for odd n <= N.
 (iii) CONV2 Lemma 1(iii): exists T>=1: Tn+1 has a divisor f ≡ -1 (mod L_T), L_T = T if 4|T else 4T.
 (J)   exists f ≡ 3 (mod 4), f <= 2n+1, with Jacobi (n/f) = -1 and r := (-n mod f) dividing f+1.
 (X)   n = x*y*z - x - z with x,y,z >= 1 and (4|x or 4|y or 4|z).
 (P)   exists a>=1: n+a or n+4a has a divisor ≡ -1 (mod 4a).
Usage: python3 z60_lopez_forms.py N
"""
import sys, math
def jacobi(a, n):
    a %= n; t = 1
    while a:
        while a % 2 == 0:
            a //= 2
            if n % 8 in (3, 5): t = -t
        a, n = n, a
        if a % 4 == 3 and n % 4 == 3: t = -t
        a %= n
    return t if n == 1 else 0
def divisors(m):
    ds = []
    i = 1
    while i * i <= m:
        if m % i == 0:
            ds.append(i)
            if i * i != m: ds.append(m // i)
        i += 1
    return ds
def U_iii(n):
    # T up to ... a witness (T,f): f | Tn+1, f ≡ -1 mod L_T, so cofactor g ≡ -1 mod L_T too when 4|T; bound T <= 4n+4 suffices
    for T in range(1, 4 * n + 5):
        L = T if T % 4 == 0 else 4 * T
        N = T * n + 1
        for f in divisors(N):
            if (f + 1) % L == 0: return True
    return False
def U_J(n):
    for f in range(3, 2 * n + 2, 4):
        if math.gcd(n, f) != 1: continue
        if jacobi(n, f) != -1: continue
        r = (-n) % f
        if r and (f + 1) % r == 0: return True
    return False
def U_X(n, N):
    return n in XS
def U_P(n):
    for a in range(1, n + 2):
        for y in (a, 4 * a):
            for f in divisors(n + y):
                if (f + 1) % (4 * a) == 0: return True
    return False
N = int(sys.argv[1])
XS = set()
# enumerate xyz - x - z <= N with x <= z (symmetric), x,y,z >= 1
for y in range(1, N + 3):
    for x in range(1, N + 3):
        if x * y * x - 2 * x > N and x * y - 1 > 0 and x > 1: break
        z = x
        while True:
            v = x * y * z - x - z
            if v > N: break
            if v >= 1 and (x % 4 == 0 or y % 4 == 0 or z % 4 == 0): XS.add(v)
            z += 1
            if x * y - 1 <= 0: 
                if z > N + 5: break
        if x * y - 1 <= 0 and x > N: break
    if y > 2 and y * 1 * 1 - 2 > N: break
bad = 0; zeros = []
for n in range(1, N + 1, 2):
    a = U_iii(n); b = U_J(n); c = n in XS; d = U_P(n)
    if not (a == b == c == d):
        bad += 1; print("MISMATCH", n, a, b, c, d)
    if not a: zeros.append(n)
sq = [n for n in zeros if math.isqrt(n) ** 2 == n]
print("N", N, "mismatches", bad, "zeros", len(zeros), "non-square zeros", [n for n in zeros if n not in sq])
