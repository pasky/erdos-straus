"""R165 from-scratch checks of PARITY_FIXED_P.md Lemmas 1.1, 1.2, 1.3 and the (*) / hyperbola forms (3.3, 3.4).
Independent enumeration; does not import any pf_* code."""
import sys
from math import gcd, isqrt


def divisors(N):
    out = []
    for i in range(1, isqrt(N) + 1):
        if N % i == 0:
            out.append(i)
            if i * i != N:
                out.append(N // i)
    return out


def primes_upto(n):
    s = bytearray([1]) * (n + 1); s[0:2] = b"\0\0"
    for i in range(2, isqrt(n) + 1):
        if s[i]:
            s[i * i::i] = bytearray(len(s[i * i::i]))
    return [i for i in range(n + 1) if s[i]]


def kron_odd(a, l):  # Legendre/Jacobi (a/l), l odd positive
    a %= l; r = 1
    while a:
        while a % 2 == 0:
            a //= 2
            if l % 8 in (3, 5): r = -r
        a, l = l, a
        if a % 4 == 3 and l % 4 == 3: r = -r
        a %= l
    return r if l == 1 else 0


def lemma11(n):
    # Independent a-priori bounds (from a(4dhk-1)=hn+k): a,d <= n+2, h,k <= n+1.  RHS is enumerated in a
    # LARGER box a,d <= 2n+6 so that any RHS element outside the LHS box shows up as a mismatch.
    rhs = set()
    for a in range(1, 2 * n + 7):
        for d in range(1, 2 * n + 7):
            N = n + 4 * a * a * d; q = 4 * a * d
            for f in divisors(N):
                if (f + 1) % q == 0:
                    rhs.add((a, d, f))
    lhs = set()
    for d in range(1, n + 3):
        for h in range(1, n + 2):
            for k in range(1, n + 2):
                m = 4 * d * h * k - 1
                if m > h * n + k: break
                if (h * n + k) % m == 0:
                    a = (h * n + k) // m
                    lhs.add((a, d, 4 * a * d * h - 1))
    return lhs == rhs, len(lhs), len(rhs)


def lemma12(p, B):
    # LHS (d,k,f): f | 4dk^2+1, 4dk | f+p, p∤f ;   RHS (c,d,f): f | p^2+4c^2 d, f ≡ -p mod 4cd, p∤f.
    lhs = set(); rhs = set()
    for d in range(1, B):
        for k in range(1, B):
            if d * k > B: break
            for f in divisors(4 * d * k * k + 1):
                if (f + p) % (4 * d * k) == 0 and f % p:
                    lhs.add(((f + p) // (4 * d * k), d, f))
    for c in range(1, B + p // 4 + 3):
        for d in range(1, B + 1):
            for f in divisors(p * p + 4 * c * c * d):
                if (f + p) % (4 * c * d) == 0 and f % p:
                    k = (f + p) // (4 * c * d)
                    if d * k <= B:  # compare inside common box dk<=B
                        rhs.add((c, d, f))
    return lhs == rhs, len(lhs), len(rhs)


def spin(P, A, D):
    viol = inst = 0
    for p in P:
        for a in range(1, A):
            for d in range(1, D):
                N = p + 4 * a * a * d
                for l in [x for x in divisors(N) if x > 2 and all(x % y for y in range(2, isqrt(x) + 1))]:
                    if (2 * p * a * d) % l == 0: continue
                    inst += 1
                    if kron_odd(-4 * d, l) != kron_odd(l, p): viol += 1
                N2 = p * p + 4 * a * a * d  # Type I with c=a
                for l in [x for x in divisors(N2) if x > 2 and all(x % y for y in range(2, isqrt(x) + 1))]:
                    if (2 * p * a * d) % l == 0: continue
                    inst += 1
                    if kron_odd(-4 * d, l) != 1: viol += 1
    return inst, viol


def star(p):
    # R1 = #{(j,f): f | p+j, f ≡ -1 mod 4j};  R2 = #{b>=3: 4*(-p mod b) | b+1};  R3 = #{(A,B,C): 4ABC-A-B=p}
    R1 = 0
    for j in range(1, p + 1):
        for f in divisors(p + j):
            if (f + 1) % (4 * j) == 0: R1 += 1
    R2 = 0
    for b in range(3, 2 * p + 2):
        j = (-p) % b
        if j and (b + 1) % (4 * j) == 0: R2 += 1
    R3 = 0; H = 0
    for A in range(1, p + 1):
        for C in range(1, p + 1):
            x = 4 * A * C - 1
            if x > p + A: break
            if (p + A) % x == 0: R3 += 1
    # hyperbola: x y ≡ 1 mod 4p, C=(xy-1)/4p>=1, 4C | x+1, 4C | y+1, x,y>=1
    for x in range(3, 4 * p * p, 4):  # x ≡ -1 mod 4C forces x ≡ 3 mod 4
        if x % p == 0: continue
        for C in divisors((x + 1) // 4):
            if (4 * C * p + 1) % x == 0:
                y = (4 * C * p + 1) // x
                if (y + 1) % (4 * C) == 0: H += 1
    return R1, R2, R3, H


if __name__ == "__main__":
    bad = 0
    for n in range(1, 121):
        ok, a, b = lemma11(n); bad += not ok
        if not ok: print("L1.1 FAIL", n, a, b)
    print("Lemma 1.1 n<=120 failures:", bad)
    bad = 0
    for p in primes_upto(60)[1:]:
        ok, a, b = lemma12(p, 40); bad += not ok
        if not ok: print("L1.2 FAIL", p, a, b)
    print("Lemma 1.2 (box dk<=40), odd p<=60 failures:", bad)
    P1 = [p for p in primes_upto(400) if p % 4 == 1]
    print("spin lemma (instances, violations):", spin(P1, 6, 30))
    for p in primes_upto(80)[1:]:
        r = star(p)
        if len(set(r)) != 1: print("STAR mismatch", p, r)
    print("(*) R1=R2=R3=hyperbola checked for odd p<80")
