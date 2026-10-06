"""R82 from-scratch checks for POINTWISE_MN3 (m fixed).

(1) Brute-force all atoms (M,D), M <= MMAX, M = -1 mod m, D | A^2, D <= A;
    compute O12 coordinates (a,b,c,d,e,f,N) from scratch and verify
    Lemma 2.1 identities, N >= acd, f <= (m-1)N, the bound f <= N+1 claimed in MN3 §5,
    the involution invariance of g, and that M never divides mD+1 (N != 1).
(2) R(N) for N <= NMAX: (i) from the brute atom list (complete for N <= NMAX because
    M = eN <= N*(m*N^3+1) is guaranteed below MMAX when NMAX is small), (ii) via the
    (a,c,d) count of Lemma 2.1 (both the 'upper bound' count and the validated count).
Usage: review_mn3_atoms.py m MMAX NMAX
"""
import sys
from math import gcd, isqrt
from collections import Counter

m, MMAX, NMAX = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])

def factor(n):
    f = {}
    p = 2
    while p * p <= n:
        while n % p == 0:
            f[p] = f.get(p, 0) + 1
            n //= p
        p += 1
    if n > 1:
        f[n] = f.get(n, 0) + 1
    return f

def divisors_from(fac):
    ds = [1]
    for p, k in fac.items():
        ds = [x * p ** i for x in ds for i in range(k + 1)]
    return ds

def sqfree(n):
    return all(k == 1 for k in factor(n).values())

def split_D(D):
    # D = d a^2, d squarefree
    fac = factor(D)
    a = 1; d = 1
    for p, k in fac.items():
        a *= p ** (k // 2); d *= p ** (k % 2)
    return a, d

R_brute = Counter()
viol = Counter()
fN2 = []
n_atoms = 0
for M in range(m - 1, MMAX + 1, m):
    A = (M + 1) // m
    facA = factor(A)
    fac2 = {p: 2 * k for p, k in facA.items()}
    for D in divisors_from(fac2):
        if D > A:
            continue
        n_atoms += 1
        P = m * D + 1
        g = gcd(M, P)
        N = M // g
        if N == 1:
            viol['N=1'] += 1
        # involution
        D2 = A * A // D
        if gcd(M, m * D2 + 1) != g:
            viol['involution'] += 1
        a, d = split_D(D)
        if A % (d * a):
            viol['A not d a b'] += 1; continue
        b = A // (d * a)
        if b < a: viol['b<a'] += 1
        e = g; f = P // e
        if (a + b) % e: viol['e !| a+b'] += 1; continue
        c = (a + b) // e
        if N != m * a * c * d - f: viol['N formula'] += 1
        if N < a * c * d: viol['N<acd'] += 1
        if f > (m - 1) * N: viol['f>(m-1)N'] += 1
        if f > N + 1: fN2.append((M, D, N, f, e))
        if f * b != a * N + c: viol['fb'] += 1
        if c * M != N * (a + b): viol['cM'] += 1
        if (N * N + m * c * c * d) % f: viol['f|N^2+mc^2d'] += 1
        if M <= MMAX and N <= NMAX:
            R_brute[N] += 1

print(f"m={m} atoms(D<=A, M<={MMAX}) = {n_atoms}; violations: {dict(viol)}")
print(f"#atoms with f > N+1: {len(fN2)}; first few (M,D,N,f,e): {fN2[:5]}")

# (2) (a,c,d) counts
def R_acd(N, validate):
    cnt = 0
    for a in range(1, N + 1):
        for c in range(1, N // a + 1):
            for d in range(1, N // (a * c) + 1):
                f = m * a * c * d - N
                if f < 1: continue
                P = m * a * a * d + 1
                if P % f: continue
                if not validate:
                    cnt += 1; continue
                if not sqfree(d): continue
                e = P // f
                b = c * e - a
                if b < a: continue
                M = e * N
                if gcd(M, P) != e: continue
                cnt += 1
    return cnt

# completeness: need max possible M for N<=NMAX below MMAX
need = NMAX * (m * NMAX ** 3 + 1)
print(f"brute complete for N<={NMAX} iff MMAX>={need}: {MMAX >= need}")
bad = 0
for N in range(1, NMAX + 1):
    rv = R_acd(N, True); ru = R_acd(N, False)
    if rv != R_brute[N] or ru < rv:
        bad += 1
        print("MISMATCH", N, R_brute[N], rv, ru)
print("R(N) N<=%d: brute vs validated (a,c,d) mismatches: %d" % (NMAX, bad))
print("R(N), N=1..%d:" % NMAX, [R_brute[N] for N in range(1, NMAX + 1)])
print("upper-bound count, N=1..%d:" % NMAX, [R_acd(N, False) for N in range(1, NMAX + 1)])
