"""Reviewer's independent check of POINTWISE_OMEGA2 Lemma 8.1 (atom <-> ET Type I point).
Atoms: brute force over all M = m r <= r^3 + r, M = 3 (4), D | A^2 with m | 4D+1, D <= A
(Lemma 9.1 of PO gives m <= r^2+1; we enumerate m up to r^2+1 and also assert nothing beyond).
Points: brute force over (a,c,d), 4acd > n, f = 4acd - n, f | 4a^2 d + 1, b=(na+c)/f integer,
a <= b, all nine identities re-checked; acd <= n (Lemma 2.8 gives <= 3n/4; we search to n).
Compare (a,b,d) <-> (r',k,s) with d squarefree; also count points with d non-squarefree."""
import sys
from math import isqrt
def factor(n):
    f = {}; p = 2
    while p * p <= n:
        while n % p == 0: f[p] = f.get(p, 0) + 1; n //= p
        p += 1
    if n > 1: f[n] = f.get(n, 0) + 1
    return f
def sqf_split(D):  # D = s r'^2, s squarefree
    s = rp = 1
    for p, e in factor(D).items():
        rp *= p ** (e // 2); s *= p ** (e % 2)
    return s, rp
def atoms(r):
    out = set()
    for m in range(1, r * r + 2):
        M = m * r
        if M % 4 != 3: continue
        A = (M + 1) // 4
        divs = [1]
        for p, e in factor(A).items():
            divs = [x * p ** k for x in divs for k in range(2 * e + 1)]
        for D in divs:
            if D <= A and (4 * D + 1) % m == 0:
                s, rp = sqf_split(D); k = A // (s * rp)
                assert s * rp * k == A
                out.add((rp, k, s))
    return out
def points(n):
    out = set(); nonsq = 0
    for a in range(1, n + 1):
        for c in range(1, n // a + 1):
            for d in range(1, n // (a * c) + 1):
                f = 4 * a * c * d - n
                if f <= 0 or (4 * a * a * d + 1) % f or (n * a + c) % f: continue
                e = (4 * a * a * d + 1) // f; b = (n * a + c) // f
                if a > b: continue
                assert 4*a*b*d == n*e+1 and c*e == a+b and b*f == n*a+c
                if all(p_e == 1 for p_e in factor(d).values()): out.add((a, b, d))
                else: nonsq += 1
    return out, nonsq
R = int(sys.argv[1]); bad = 0; tot = 0; tns = 0
for r in range(3, R + 1, 2):
    A_, (P_, ns) = atoms(r), points(r)
    tot += len(A_); tns += ns
    if A_ != P_: bad += 1; print("MISMATCH", r, sorted(A_ ^ P_)[:5])
print(f"odd r<= {R}: atoms={tot}, mismatching r={bad}, extra points with d non-squarefree={tns}")
