"""O257: do SIZES of source witnesses carry information about the target's witnesses?  (permutation test)
For target p and matched sources q (as z28_matched), each source witness w' = (th', a', b', c', d') offers the
size numbers D in {d', a'b'd' (= x' or x'/q), c'd'}.  Event E(p, D): p has a witness (any type) whose 'p-free
denominator' X = abd is divisible by D.  Compare the hit rate with D taken from p's own matched sources vs D taken
from the sources of a different target p* of similar size (shuffled), excluding D = 1.
Usage: z28_size_info.py k B W N   (targets: Mordell-class primes <= N, or all primes ≡ 1 mod 8 if k != 4)"""
import sys, random
random.seed(0)
from sympy import isprime, primerange
from z28_witness import reps
from z28_matched import profile_match
k, B, W, N = map(int, sys.argv[1:5])
M = {1, 121, 169, 289, 361, 529}
targets = [p for p in primerange(100, N + 1) if (p % 840 in M if k == 4 else p % 8 == 1)]
data = []
for p in targets:
    Xp = [a * b * d for (th, a, b, c, d, e, H) in reps(p, k)]
    Ds, Us = [], []
    for q in range(max(3, p - W), p + W + 1):
        if q == p or not isprime(q) or k % q == 0 or (q - p) % 8: continue
        m = profile_match(p, q, B)
        if not m and random.random() > 0.25: continue   # subsample unmatched sources (same window, same sizes)
        for (th, a, b, c, d, e, H) in reps(q, k):
            (Ds if m else Us).extend([('d', d), ('abd', a * b * d), ('cd', c * d)])
    data.append((p, Xp, [x for x in Ds if x[1] > 1], [x for x in Us if x[1] > 1]))
def rate(pairs):
    out = {}
    for Xp, Ds in pairs:
        for kind, D in Ds:
            h, n = out.get(kind, (0, 0)); out[kind] = (h + any(X % D == 0 for X in Xp), n + 1)
    return {kk: (h, n, round(h / n, 4)) for kk, (h, n) in out.items()}
real = rate([(Xp, Ds) for p, Xp, Ds, Us in data])
unm = rate([(Xp, Us) for p, Xp, Ds, Us in data])
random.seed(1)
idx = list(range(len(data))); sh = []
for i in idx:   # shuffle partner among the 10 nearest targets (similar size)
    j = random.choice([t for t in range(max(0, i - 5), min(len(data), i + 6)) if t != i] or [i])
    sh.append((data[i][1], data[j][2]))
fake = rate(sh)
print(f"k={k} B={B} W={W} N={N} targets={len(data)}\n  matched   {real}\n  unmatched {unm}\n  shuffled  {fake}")
