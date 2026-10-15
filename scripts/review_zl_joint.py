"""review_zl_joint.py -- R231 (hostile review of STERILE_LOWER Lemma 3.1), FROM SCRATCH.
Per-n enumeration (own loops) of P-data (a,b,c,d,e): 4abd = n+e, a+b = ce, a<=b  [loops over (a,b,d)]
and Q-data (a,b,c,d): 4abcd = n(a+b)+c, c | a+b, a<=b  [loops over (a,c,d), b solved],
versus the joint parametrisations of Lemma 3.1:
 (i)  (a,c,d), f = 4acd-1, N == -4a^2 d (mod f), b=(Nc+a)/f, e=(N+4a^2d)/f, a<=b
 (ii) (a,d,f) with f | 4a^2d+1, c>=1, n = 4acd-f > 0, b = (na+c)/f, a<=b.
Compares the full SETS of tuples (not only counts) for every n in [X, 2X)."""
import sys
from collections import defaultdict
X = int(sys.argv[1]); Y = 2 * X

def P_per_n(n):
    S = set(); a = 1
    while 4 * a * a - 2 * a <= n:            # b>=a, d>=1, e<=a+b<=2b: 4ab-2b <= n -> with b=a
        b = a
        while 4 * a * b - 2 * b <= n:
            m = 4 * a * b
            for d in range(-(-(n + 1) // m), (n + a + b) // m + 1):
                e = m * d - n
                if 1 <= e <= a + b and (a + b) % e == 0:
                    S.add((a, b, (a + b) // e, d, e))
            b += 1
        a += 1
    return S

def Q_per_n(n):
    S = set(); a = 1
    while 4 * a - 1 <= 2 * n:                 # c(4ad-1) <= 2n
        d = 1
        while (4 * a * d - 1) <= 2 * n:
            c = 1
            while c * (4 * a * d - 1) <= 2 * n:
                f = 4 * a * c * d - n
                if f > 0 and (a * n + c) % f == 0:
                    b = (a * n + c) // f
                    if b >= a and (a + b) % c == 0:
                        assert 4 * a * b * c * d == n * (a + b) + c
                        S.add((a, b, c, d))
                c += 1
            d += 1
        a += 1
    return S

JP = defaultdict(set); JQ = defaultdict(set)
# (i) joint: N in [X,Y); need f - 4a^2 d < Y for some admissible N (N>=1 and N == -4a^2d mod f -> N >= f-4a^2d when 4a^2d<f)
a = 1
while 4 * a * a - 2 * a < Y:      # a<=b <=> cN >= 4a^2cd - 2a ; N<Y -> 4a^2 d - 2a/c < Y
    d = 1
    while 4 * a * a * d - 2 * a < Y:
        c = 1
        while 4 * a * c * d - 1 - 4 * a * a * d < Y:
            f = 4 * a * c * d - 1
            for N in range(X, Y):
                if (N + 4 * a * a * d) % f == 0 and c * N >= 4 * a * a * c * d - 2 * a:
                    b = (N * c + a) // f; e = (N + 4 * a * a * d) // f
                    assert (N * c + a) % f == 0 and 4 * a * b * d == N + e and a + b == c * e and a <= b
                    JP[N].add((a, b, c, d, e))
            c += 1
        d += 1
    a += 1
# (ii) joint: n = 4acd - f >= X, f | 4a^2d+1
a = 1
while 4 * a - 1 < 2 * Y:
    d = 1
    while 4 * a * d - 1 < 2 * Y:     # f <= ... crude: a<=b forces c(4ad-1)<=2n<2Y, c>=1
        m = 4 * a * a * d + 1
        for f in range(1, m + 1):
            if m % f: continue
            c = 1
            while 4 * a * c * d - f < Y and c * (4 * a * d - 1) < 2 * Y + 2:
                n = 4 * a * c * d - f
                if n >= X and (n * a + c) % f == 0:
                    b = (n * a + c) // f
                    if b >= a:
                        assert 4 * a * b * c * d == n * (a + b) + c and (a + b) % c == 0
                        JQ[n].add((a, b, c, d))
                elif n >= X:
                    raise SystemExit(f"Lemma 3.1(ii) divisibility fails at a={a} d={d} f={f} c={c}")
                c += 1
        d += 1
    a += 1
bad = 0; tp = tq = 0
for n in range(X, Y):
    p, q = P_per_n(n), Q_per_n(n); tp += len(p); tq += len(q)
    if p != JP[n] or q != JQ[n]: bad += 1; print("MISMATCH", n, len(p), len(JP[n]), len(q), len(JQ[n]))
print(f"X={X}: n in [{X},{Y}) P-data {tp} Q-data {tq} set-mismatches {bad}")
