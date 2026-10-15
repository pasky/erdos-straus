"""review_r248_tree.py (R248, from scratch): Case A data (re-derived) + Case B balls (review_r248_caseB.c output)
-> survivor tree of the c-slices X_c (q=3, k=2) to depth DMAX; per depth: distinct balls, alive fraction,
sibling profile (alive parents with 0/1/2/3 children that are balls).
Case A (gamma=0, g'=1 gives the largest cylinder; a0=a1=T^al*a1', b0=b1, all monic, gcd=1):
  E F = T^al a1' + b1, E = a1' b1 K - 1, T|K  =>  z := (F+b1)/a1' poly, b1 K F = T^al + z, T|z, z != 0;
  degrees: beta, lambda <= al-1, deg z <= al-1.  Ball: u == -E (mod T^{al+2}).
usage: PYTHONPATH=scripts uv run python scripts/review_r248_tree.py CASEB_FILE DMAX [BALLDUMP]"""
import sys, itertools
from collections import defaultdict
p = 3
def trim(a):
    a = list(a)
    while a and a[-1] == 0: a.pop()
    return a
def mul(a, b):
    if not a or not b: return []
    r = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        if x:
            for j, y in enumerate(b): r[i + j] = (r[i + j] + x * y) % p
    return trim(r)
def add(a, b):
    n = max(len(a), len(b)); return trim([((a[i] if i < len(a) else 0) + (b[i] if i < len(b) else 0)) % p for i in range(n)])
def neg(a): return [(-x) % p for x in a]
def divmod_(a, b):
    a = list(a); q = [0] * max(0, len(a) - len(b) + 1); il = 1 if b[-1] == 1 else 2
    while len(a) >= len(b) and a:
        sh = len(a) - len(b); f = a[-1] * il % p; q[sh] = f
        for i, y in enumerate(b): a[i + sh] = (a[i + sh] - f * y) % p
        a = trim(a)
    return trim(q), a
def monics(d):
    for t in itertools.product(range(p), repeat=d): yield list(t) + [1]
def gcd(a, b):
    while b: a, b = b, divmod_(a, b)[1]
    return a
def monic_divisors(f):
    out = []
    for d in range(len(f)):
        for g in monics(d):
            q, r = divmod_(f, g)
            if not r: out.append(g)
    return out
def caseA(al):
    res = set()
    for zt in itertools.product(range(p), repeat=al - 1):          # z = T * (deg <= al-2 poly), nonzero
        z = trim([0] + list(zt))
        if not z: continue
        tgt = add([0] * al + [1], z)
        for b1 in monic_divisors(tgt):
            if b1[0] == 0: continue
            rest = divmod_(tgt, b1)[0]
            for K in monic_divisors(rest):
                if K[0] != 0: continue
                F = divmod_(rest, K)[0]
                a1p, r = divmod_(add(F, b1), z)
                if r or not a1p or a1p[-1] != 1 or a1p[0] == 0: continue
                if len(gcd(a1p, b1)) > 1: continue
                E = add(mul(mul(a1p, b1), K), [p - 1])
                assert mul(E, F) == add(mul([0] * al + [1], a1p), b1)
                res.add(tuple(E))
    return res
if __name__ == "__main__":
    fB, DMAX = sys.argv[1], int(sys.argv[2])
    balls = defaultdict(set); src = defaultdict(lambda: [0, 0])
    def addball(u, d, kind):
        if u[0] == 1 and u[1] != 0:
            if u not in balls[d]: src[d][kind] += 1
            balls[d].add(u)
    for line in open(fB):
        s, d, dig = line.split(); d = int(d)
        if d <= DMAX: addball(tuple(int(c) for c in dig), d, 1)
    for al in range(1, DMAX - 1):
        for E in caseA(al):
            E = list(E) + [0] * (al + 2); addball(tuple((-E[i]) % p for i in range(al + 2)), al + 2, 0)
    if len(sys.argv) > 3:
        with open(sys.argv[3], "w") as fh:
            for d in sorted(balls):
                for u in sorted(balls[d]): fh.write("%d %s\n" % (d, "".join(map(str, u))))
    for c in (1, 2):
        alive = {(1, c)}; print("c=%d" % c)
        for n in range(3, DMAX + 1):
            B = {u for u in balls[n] if u[1] == c}; prof = [0] * 4; new = set()
            for v in alive:
                ch = [v + (x,) for x in range(p)]; k = sum(w in B for w in ch); prof[k] += 1
                new.update(w for w in ch if w not in B)
            nA = sum(1 for u in B if u in balls[n])
            print(" d=%d balls=%d (mass %.4f) alive=%d (frac %.4f) prof=%s" % (n, len(B), len(B) / p ** (n - 2), len(new), len(new) / p ** (n - 2), prof))
            alive = new
    print("first-source counts per depth [caseA-only-new, caseB]:", dict(src))
