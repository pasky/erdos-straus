"""R56 from-scratch check of the planting Lemma 10.1 (es-subexp-note v4):
build nu exactly as in the proof, check nonnegativity, nu(0)=0, k-wise marginals.
Also probe the hypothesis boundary: random p with R just above (k+1)+(2k+1)r*."""
import itertools, random
from fractions import Fraction as Fr
from math import prod

def esym(vals, a):
    return sum(prod(c) for c in itertools.combinations(vals, a)) if a >= 0 else 0

def build(p, k):
    N = len(p); r = [pi / (1 - pi) for pi in p]
    P0 = prod(1 - pi for pi in p)
    ek1 = esym(r, k + 1)
    nu = {}
    for x in itertools.product((0, 1), repeat=N):
        nu[x] = prod(p[i] if x[i] else 1 - p[i] for i in range(N))
    for J in itertools.combinations(range(N), k + 1):
        wJ = prod(r[i] for i in J) / ek1
        for a in range(k + 2):
            for y in itertools.combinations(J, a):
                x = tuple(1 if i in y else 0 for i in range(N))
                nu[x] += P0 * wJ * (-1) ** (a + 1)
    return nu, r

def check(p, k):
    N = len(p)
    nu, r = build(p, k)
    assert nu[tuple([0] * N)] == 0
    mn = min(nu.values())
    for K in itertools.combinations(range(N), min(k, N)):
        for z in itertools.product((0, 1), repeat=len(K)):
            m = sum(v for x, v in nu.items() if all(x[K[t]] == z[t] for t in range(len(K))))
            t = prod(p[K[t]] if z[t] else 1 - p[K[t]] for t in range(len(K)))
            assert m == t
    return mn

def run(trials, seed=7):
    rng = random.Random(seed)
    n = 0; worst = None
    for _ in range(trials):
        N = rng.randint(3, 9); k = rng.randint(0, min(3, N - 1))
        p = [Fr(rng.randint(1, 60), 100) for _ in range(N)]
        r = [pi / (1 - pi) for pi in p]
        if sum(r) < (k + 1) + (2 * k + 1) * max(r):
            continue
        mn = check(p, k); n += 1
        assert mn >= 0, (p, k, mn)
        worst = mn if worst is None else min(worst, mn)
    print("instances satisfying (10.1):", n, "min nu mass", float(worst))

if __name__ == "__main__":
    run(3000)
