"""R123 from-scratch checks of POINTWISE_SPECTRAL Lemmas 2.1-2.4 (independent of scripts/spec_*).

Route 1 (param, ET (2.x)): enumerate (a,c,d) with acd < 2N/3, f | 4a^2 d + 1, n = 4acd - f.
Route 2 (Lemma 2.1(iii)): for each n, c,d with cd < 2n/3, divisors f of n^2+4c^2 d, f = -n mod 4cd.
Route 3 (raw ES brute force, primes <= PMAX): all 4/p = 1/x+1/y+1/z, p|x, p∤y,z, y<=z.
Type II: raw brute force vs. factorisations c q p + 1 = (aq-1)(bq-1), q = 4cd.
"""
import sys
from fractions import Fraction
from math import gcd, isqrt
from collections import defaultdict

N = int(sys.argv[1]) if len(sys.argv) > 1 else 3000
PMAX = int(sys.argv[2]) if len(sys.argv) > 2 else 400


def divisors(m):
    ds, i = [], 1
    while i * i <= m:
        if m % i == 0:
            ds.append(i)
            if i * i != m:
                ds.append(m // i)
        i += 1
    return ds


def kron(D, n):
    """Kronecker symbol (D/n), n > 0, from scratch."""
    if n == 0:
        return 1 if abs(D) == 1 else 0
    res = 1
    while n % 2 == 0:
        n //= 2
        if D % 2 == 0:
            return 0
        res *= 1 if D % 8 in (1, 7) else -1
    # Jacobi (D/n), n odd
    a, m = D % n, n
    while a:
        while a % 2 == 0:
            a //= 2
            if m % 8 in (3, 5):
                res = -res
        a, m = m, a
        if a % 4 == 3 and m % 4 == 3:
            res = -res
        a %= m
    return res if m == 1 else 0


def isprime(n):
    return n > 1 and all(n % q for q in range(2, isqrt(n) + 1))


# ---- Route 1 ----
sols1 = defaultdict(set)   # n -> set of (a,c,d,f) with a<=b, gcd(c,n)=1 (=> Type I)
bad = 0
nonprim = defaultdict(int)
for a in range(1, N):
    for d in range(1, N):
        if 3 * a * d >= 2 * N:
            break
        F = 4 * a * a * d + 1
        for f in divisors(F):
            for c in range(1, N):
                if 3 * a * c * d >= 2 * N:
                    break
                n = 4 * a * c * d - f
                if n < 1 or n > N:
                    continue
                if gcd(c, n) != 1:
                    continue
                e = F // f
                if (a * n + c) % f:
                    bad += 1; continue
                b = (a * n + c) // f
                if a > b:
                    continue
                assert (a + b) == c * e and 4 * a * b * d - n * e == 1
                x, y, z = a * b * d * n, a * c * d, b * c * d
                assert Fraction(4, n) == Fraction(1, x) + Fraction(1, y) + Fraction(1, z)
                assert gcd(a * b * c * d, n) == 1
                if gcd(gcd(a, b), c) != 1:
                    nonprim[n] += 1      # dilate of a primitive quadruple: SAME (x,y,z)
                    continue
                g = (n * n + 4 * c * c * d)
                assert g % f == 0 and g // f == 4 * b * c * d - n
                # Lemma 2.2
                assert 4 * a * d * b - n * e == 1
                # Q'(X,Y) = Q-(X + 2bd Y, n Y), Q- = [f,-4ad,de], Q' = [f,4cd,d g/f]
                for X, Y in ((1, 0), (0, 1), (1, 1), (2, -3)):
                    u, v = X + 2 * b * d * Y, n * Y
                    assert f*u*u - 4*a*d*u*v + d*e*v*v == f*X*X + 4*c*d*X*Y + d*(g//f)*Y*Y
                sols1[n].add((a, c, d, f))
print("route1 done; (ii) divisibility failures:", bad, "; non-primitive quadruples (a<=b) for primes:", sum(v for k, v in nonprim.items() if isprime(k)), "e.g.", [(k, v) for k, v in sorted(nonprim.items()) if isprime(k)][:5])

# ---- Route 2: Lemma 2.1(iii), primes only (lemma hypothesis p prime, p ∤ cd) ----
mism = 0
for n in range(5, N + 1):
    if not isprime(n):
        continue
    s2 = set()
    for c in range(1, n):
        if 3 * c >= 2 * n:
            break
        for d in range(1, n):
            if 3 * c * d >= 2 * n:
                break
            if (c * d) % n == 0:
                continue
            M = n * n + 4 * c * c * d
            for f in divisors(M):
                if (f + n) % (4 * c * d) == 0 and f * f <= M:  # f <= g  <=> a <= b
                    a = (f + n) // (4 * c * d)
                    b = (a * n + c) // f
                    if gcd(gcd(a, b), c) == 1:
                        s2.add((a, c, d, f))
    if s2 != sols1[n]:
        mism += 1
        print("Lemma2.1 mismatch", n, sorted(s2 ^ sols1[n])[:5])
print("route2 (Lemma 2.1(iii)) mismatches over primes <=", N, ":", mism)

# ---- Lemma 2.4 genus: all odd n <= N, all quadruples with gcd(n,2cd)=1 ----
viol = 0; tot = 0; sq_hits = 0
for n, S in sols1.items():
    if n % 2 == 0:
        continue
    r = isqrt(n)
    for (a, c, d, f) in S:
        if gcd(n, 2 * c * d) != 1:
            continue
        tot += 1
        if kron(-4 * d, (-n) % (4 * d) or 4 * d) != 1:
            viol += 1
        if r * r == n:
            sq_hits += 1
print("Lemma 2.4: quadruples", tot, "violations", viol, "odd-square hits", sq_hits)
# also: any Type I at all for odd squares (incl. gcd(m,cd)>1 is excluded by gcd(c,n)=1?)
print("odd squares with a route-1 quadruple:", [n for n in sols1 if n % 2 and isqrt(n)**2 == n][:10])

# ---- Lemma 2.3(a) a=1 slice ----
for n in range(5, N + 1):
    if not isprime(n):
        continue
    A1 = {q for q in sols1[n] if q[0] == 1}
    T = set()
    for t in range(1, 4 * n):  # t=e; (tu-1)(tv-1)=tn+1, u=c, v=f, tv = 1 mod 4
        M = t * n + 1
        for X in divisors(M):
            if X % t == t - 1 or (t == 1):
                Y = M // X
                if (X + 1) % t or (Y + 1) % t:
                    continue
                u, v = (X + 1) // t, (Y + 1) // t
                if u < 1 or v < 1 or (t * v) % 4 != 1:
                    continue
                d = (t * v - 1) // 4
                if d < 1 or gcd(u, n) != 1:
                    continue
                b = u * t - 1
                if b >= 1:
                    T.add((1, u, d, v))
    if A1 != T:
        print("a=1 mismatch", n, sorted(A1 ^ T)[:4]); break
else:
    print("Lemma 2.3(a): a=1 slice matches for all primes <=", N)


# ---- Route 3: raw brute force, Type I and Type II, primes <= PMAX ----
def raw(p):
    t1 = t2 = 0
    for u in range(p // 4 + 1, 3 * p // 4 + 1):     # u <= v <= w, 4/p - 1/u = A/B
        A, B = 4 * u - p, p * u
        if A <= 0:
            continue
        for v in range(max(u, B // A + 1), 2 * B // A + 1):
            num, den = A * v - B, B * v                # 1/w = num/den
            if num > 0 and den % num == 0 and den // num >= v:
                w = den // num
                k = (u % p == 0) + (v % p == 0) + (w % p == 0)
                if k == 1:
                    t1 += 1
                elif k == 2:
                    t2 += 1
    return t1, t2


def typeII_fact(p):
    """Lemma 2.3(b): c q p + 1 = (aq-1)(bq-1), q = 4cd, a<=b, gcd(a,b,c)=1, p∤abd."""
    cnt = 0
    for c in range(1, 2 * p):
        for d in range(1, 2 * p):
            q = 4 * c * d
            for a in range(1, 2 * p):
                if a * c * d > 2 * p:
                    break
                M = c * q * p + 1
                if M % (a * q - 1):
                    continue
                Y = M // (a * q - 1)
                if (Y + 1) % q:
                    continue
                b = (Y + 1) // q
                if b < a or gcd(gcd(a, b), c) != 1 or (a * b * d) % p == 0:
                    continue
                assert 4 * a * b * c * d == a + b + c * p
                cnt += 1
            if c * d > 2 * p:
                break
    return cnt


m1 = m2 = 0
for p in range(5, PMAX + 1):
    if not isprime(p):
        continue
    t1, t2 = raw(p)
    if t1 != len(sols1[p]):
        m1 += 1; print("TypeI raw mismatch", p, t1, len(sols1[p]))
    if t2 != typeII_fact(p):
        m2 += 1; print("TypeII mismatch", p, t2, typeII_fact(p))
print("raw ES brute force: TypeI mismatches", m1, "(p<=%d); TypeII-factorisation mismatches" % PMAX, m2, "(p<=%d)" % PMAX)
