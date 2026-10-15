# R224: independent recomputation of the §2 clean-level law and coin model.
# usage: review_r224_model.py SEED|FILE NPRIMES T
import sys, random
from collections import defaultdict
from sympy import factorint, isprime
def leg(a, p): a %= p; return 0 if a == 0 else (1 if pow(a, (p - 1) // 2, p) == 1 else -1)
src, NP, T = sys.argv[1], int(sys.argv[2]), int(sys.argv[3])
if src.isdigit():
    rng = random.Random(int(src)); ps = set()
    while len(ps) < NP:
        p = rng.randrange(200001, 10 ** 6, 4)
        if isprime(p): ps.add(p)
    ps = sorted(ps)
else:
    ps = [int(l.split()[0]) for l in open(src)][:NP]
Ys = (30, 100, 300)
g = defaultdict(lambda: defaultdict(float))
for p in ps:
    q = 2
    while leg(q, p) == 1: q += 1
    key = (p % 8, min(q, 17))
    for t in range(1, T + 1):
        f = factorint(t * p + 1); a = g[key]
        a["n"] += 1; a["obs"] += all(leg(r, p) == 1 for r in f)
        for Y in Ys:
            small = all(leg(r, p) == 1 for r in f if r <= Y)
            k = sum(1 for r, e in f.items() if r > Y and e % 2); s = sum(1 for r, e in f.items() if r > Y and e % 2 == 0)
            pc = 2.0 ** (-s - max(k - 1, 0)) if small else 0.0      # constrained coins (author's formula, re-derived)
            pu = 2.0 ** (-s - k) if small else 0.0                  # unconstrained coins
            a["c%d" % Y] += pc; a["u%d" % Y] += pu
            a["det%d" % Y] += (pc in (0.0, 1.0))
            if pc not in (0.0, 1.0):   # the random part only
                a["rn%d" % Y] += 1; a["ro%d" % Y] += all(leg(r, p) == 1 for r in f); a["rc%d" % Y] += pc
        # rank-one-forced clean levels (Lemma 1.2(c) with exact small part = primes < q)
tot = defaultdict(float)
for a in g.values():
    for x, y in a.items(): tot[x] += y
g["ALL"] = tot
for key in sorted(g, key=str):
    a = g[key]; n = a["n"]
    print(key, int(n), "obs %.3f" % (a["obs"] / n), " ".join("Y=%d: model %.3f uncon %.3f det %.2f | random part n=%d obs %.3f model %.3f" % (Y, a["c%d" % Y] / n, a["u%d" % Y] / n, a["det%d" % Y] / n, a["rn%d" % Y], a["ro%d" % Y] / max(1, a["rn%d" % Y]), a["rc%d" % Y] / max(1, a["rn%d" % Y])) for Y in Ys))
