"""pd_k1s.py — EVIDENCE for the k = 1 slice of ES^{(y)} with S = {3} (PHASE_DIAGRAM.md §3, Prop 3.1):
for every prime 5 <= p < PMAX (and odd squares m^2 < PMAX, 3 ∤ m, as T1 control) find the least a <= AMAX such that
4p + 9^a has a divisor g ≡ -1 (mod 12) (a >= 1; a = 0: divisor ≡ 3 mod 4 of 4p+1, i.e. ES's k = 1 shot).
k = 1 shot: Q1 = 3^a, Q0 = (g+1)/4, Q = Q0*Q1; solution verified exactly (den z = 9^a; 3 | y when a >= 1). GNU factor.
Usage: pd_k1s.py PMAX AMAX"""
import sys, subprocess
from fractions import Fraction
from itertools import product
from math import gcd
from sympy import primerange
PMAX, AMAX = int(sys.argv[1]), int(sys.argv[2])
def factor_many(nums):
    out = subprocess.run(["factor"], input="\n".join(map(str, nums)), capture_output=True, text=True, check=True).stdout
    res = []
    for line in out.strip().split("\n"):
        ps = list(map(int, line.split(":")[1].split()))
        d = {}
        for q in ps: d[q] = d.get(q, 0) + 1
        res.append(d)
    assert len(res) == len(nums) and all(int(l.split(':')[0]) == v for l, v in zip(out.strip().split('\n'), nums))
    return res
def divs(f):
    ds = [1]
    for q, e in f.items():
        ds = [d * q**i for d in ds for i in range(e + 1)]
    return ds
def verify(n, Q, g, Q1):
    m = (n + 4 * Q * Q) // g; assert (n + 4 * Q * Q) % g == 0 and (n + m) % 4 == 0
    x = (n + m) // 4; y = n * (g + 1) // 4; z = Fraction(n * x * (g + 1), 4 * Q * Q)
    assert Fraction(4, n) == Fraction(1, x) + Fraction(1, y) + 1 / z
    if gcd(Q, n) == 1: assert z.denominator == Q1 * Q1 and (Q1 == 1 or y % 3 == 0)
targets = [p for p in primerange(5, PMAX)]
sq = [m * m for m in range(5, int(PMAX**0.5) + 1, 2) if m % 3]
hist = {}; unsolved = []; sqhits = 0
for label, ns in (("primes", targets), ("squares", sq)):
    pending = list(ns)
    best = {}
    for a in range(0, AMAX + 1):
        if not pending: break
        fs = factor_many([4 * n + 9**a for n in pending])
        nxt = []
        for n, f in zip(pending, fs):
            mod = 4 if a == 0 else 12
            hit = None
            for g in sorted(divs(f)):
                if (g + 1) % mod == 0 and g % 4 == 3:
                    Q0 = (g + 1) // 4; Q = Q0 * 3**a
                    if gcd(Q, n) == 1: hit = g; break
            if hit:
                verify(n, (hit + 1) // 4 * 3**a, hit, 3**a); best[n] = a
            else:
                nxt.append(n)
        pending = nxt
    if label == "primes":
        for a in best.values(): hist[a] = hist.get(a, 0) + 1
        unsolved = pending
        print("primes:", len(ns), "least-a histogram", dict(sorted(hist.items())), "unsolved", len(unsolved), unsolved[:10])
    else:
        print("odd squares (3∤m):", len(ns), "with a k=1 shot:", len(best))
