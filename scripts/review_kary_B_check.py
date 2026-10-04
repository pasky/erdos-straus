"""Review check of Lemma 2.3 / (2.1) / (3.1): B* (LP) <= B_Lagrange-min <= bounds,
and a direct random test of g(1) <= B* E_Bern(t) g for nonneg multilinear g of degree d
(g built as random nonneg combos of products of (rho_i) and (1-rho_i), plus squares)."""
import math, itertools, random
import numpy as np
from review_kary_bruteforce import Bstar, Blagrange
worst21 = -1e9; worst31 = -1e9; worst_order = 0
for n in range(0, 15):
    for t in [0.01, 0.03, 0.1, 0.2, 0.25]:
        for d in range(1, 5):
            bs = Bstar(n, t, d); bl = Blagrange(n, t, d)
            worst_order = max(worst_order, bs / bl)
            b21 = d * math.log(4 * math.e**3 * (n + 1) / t) + 0.5 * math.log(16 * n * t + 16)
            b31 = d * math.log(2 * math.exp(4.31) * max(1 / t, math.sqrt(n / (t * d)))) + 0.5 * math.log(22 * n * t + 22) + 3
            worst21 = max(worst21, math.log(bl) - b21); worst31 = max(worst31, math.log(bl) - b31)
print("max B*/B_lagrange (must be <= 1):", worst_order)
print("max log B_lagrange - (2.1):", worst21, "  max log B_lagrange - (3.1):", worst31)
# direct test with random nonneg degree-d multilinear g on {0,1}^n
rng = random.Random(7); worst = 0
for trial in range(3000):
    n = rng.randint(1, 9); d = rng.randint(1, min(3, n)); t = rng.choice([0.05, 0.1, 0.25])
    pts = list(itertools.product([0, 1], repeat=n))
    def rand_g():
        terms = []
        for _ in range(rng.randint(1, 4)):
            # square of a random degree-floor(d/2) poly (nonneg), or product of literals of size <= d
            if d >= 2 and rng.random() < 0.5:
                S = rng.sample(range(n), d // 2) if d // 2 <= n else []
                co = {T: rng.gauss(0, 1) for k in range(d // 2 + 1) for T in itertools.combinations(S, k)}
                terms.append(lambda x, co=co: sum(v * math.prod(x[i] for i in T) for T, v in co.items()) ** 2)
            else:
                S = rng.sample(range(n), rng.randint(0, d)); sg = [rng.random() < .5 for _ in S]
                terms.append(lambda x, S=S, sg=sg: math.prod(x[i] if s else 1 - x[i] for i, s in zip(S, sg)))
        return lambda x: sum(f(x) for f in terms)
    g = rand_g()
    Eg = sum(g(x) * math.prod(t if xi else 1 - t for xi in x) for x in pts)
    if Eg > 1e-14:
        worst = max(worst, g((1,) * n) / (Bstar(n, t, d) * Eg))
print("max g(1)/(B* E g) over random nonneg g (must be <= 1):", worst)
