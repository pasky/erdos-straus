"""R208: check y2_parity_involution Lemma 2 + EVIDENCE: #F(p), #F_-(p) parities at primes p = 1 (4), p < X;
fixed points of the reflection (c,m,s) -> (s,m,c) at all primes; #F_- = 0 at odd squares."""
import sys, math
from collections import defaultdict
sys.path.insert(0, 'scripts')
from review_r208_even_edge import jac
X = int(sys.argv[1]) if len(sys.argv) > 1 else 3000
F = defaultdict(int); Fm = defaultdict(int); fix = defaultdict(list)
for m in range(1, X + 3):
    for c in range(1, X + 3):
        d = m * c - 1
        if d <= 0:
            continue
        smin, smax = c // d + 1, (X + c) // d
        if smin > smax:
            if m * c - 1 > X + c:
                break
            continue
        for s in range(smin, smax + 1):
            N = m * c * s - c - s
            if N % 2 == 0:
                continue
            F[N] += 1
            if jac(m * s - 1, N) == -1:
                Fm[N] += 1
            if c == s:
                fix[N].append((c, m, s))
isp = lambda n: n > 1 and all(n % q for q in range(2, math.isqrt(n) + 1))
P = [p for p in range(5, X, 4) if isp(p)]
print("primes p=1(4), 5<=p<", X, ":", len(P), "#F odd at all:", all(F[p] % 2 for p in P),
      "#F_- even at all:", all(Fm[p] % 2 == 0 for p in P),
      "#F_- mod 4 split (0,2):", sum(Fm[p] % 4 == 0 for p in P), sum(Fm[p] % 4 == 2 for p in P))
print("primes with !=1 reflection fixed point:", [(p, fix[p]) for p in range(3, X) if isp(p) and len(fix[p]) != 1])
print("odd squares with #F_- > 0:", [M * M for M in range(1, math.isqrt(X) + 1, 2) if Fm[M * M]])
