# z58 TERNARY: brute-force check of Lemma D(a),(b): Type II solutions (a,b,c,d) of 4abcd = a + b + n c  <->
# triples (C=d, a, f) with f = -1 (mod 4aC), f | n + 4 C a^2  <->  forms [f, 2beta, g], fg - beta^2 = C n, beta = 2aC,
# 2beta | f+1.  Compares the three counts for every n <= NMAX (n >= 1).
import sys
NMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 1500
def direct(n):
    # 4abcd = a + b + nc  <=>  c (4abd - n) = a + b ; needs 4abd > n and c = (a+b)/(4abd-n) <= a + b
    S = set()
    for a in range(1, n + 2):
        for b in range(1, 2 * n + 4):
            for d in range(1, n + 2):
                k = 4 * a * b * d - n
                if k <= 0: continue
                if k > a + b: break
                if (a + b) % k == 0: S.add((a, b, (a + b) // k, d))
    return S
def via_div(n):
    S = set()
    for C in range(1, n + 2):
        for a in range(1, n + 2):
            m = 4 * a * C
            if m - 1 > n + 4 * C * a * a: break
            N = n + 4 * C * a * a
            f = m - 1
            while f <= N:
                if N % f == 0:
                    c = (f + 1) // m; b = (n * c + a) // f
                    assert (n * c + a) % f == 0
                    S.add((a, b, c, C))
                f += m
    return S
def via_forms(n):
    cnt = 0
    for C in range(1, n + 2):
        for a in range(1, n + 2):
            beta = 2 * a * C
            if 2 * beta - 1 > beta * beta + C * n: break
            M = beta * beta + C * n          # f g = M
            f = 2 * beta - 1
            while f <= M:
                if M % f == 0: cnt += 1
                f += 2 * beta
    return cnt
bad = 0
for n in range(1, NMAX + 1):
    A = direct(n); B = via_div(n); c = via_forms(n)
    if A != B or len(A) != c: bad += 1; print('MISMATCH', n, len(A), len(B), c)
print('checked n <= %d, mismatches: %d' % (NMAX, bad))
sys.exit(1 if bad else 0)
