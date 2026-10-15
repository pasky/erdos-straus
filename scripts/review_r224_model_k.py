import random
from collections import defaultdict
from sympy import factorint, isprime
def leg(a, p): a %= p; return 0 if a == 0 else (1 if pow(a, (p - 1) // 2, p) == 1 else -1)
rng = random.Random(2240); ps = set()
while len(ps) < 1500:
    p = rng.randrange(200001, 10 ** 6, 4)
    if isprime(p): ps.add(p)
g = defaultdict(lambda: [0, 0, 0.0]); Y = 100
for p in ps:
    for t in range(1, 31):
        f = factorint(t * p + 1)
        if not all(leg(r, p) == 1 for r in f if r <= Y): continue
        k = sum(1 for r, e in f.items() if r > Y and e % 2); s = sum(1 for r, e in f.items() if r > Y and e % 2 == 0)
        a = g[(k, s)]; a[0] += 1; a[1] += all(leg(r, p) == 1 for r in f); a[2] += 2.0 ** (-s - max(k - 1, 0))
for key in sorted(g): n, o, m = g[key]; print("k,s =", key, "levels", n, "obs %.3f model %.3f" % (o / n, m / n))
