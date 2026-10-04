"""Hostile-review check of EXCEPTIONAL_NONCRT Lemma 2.2 beyond the author's test:
moduli with prime powers (25, 49) and an extra non-slice prime (2), Q0 = 9 (prime power),
and dense random nu.  Reports max ratio lhs/rhs (must be <= 1) and how many (c,S) are non-degenerate."""
import itertools, math, random
import numpy as np

def run(trials=30, seed=7):
    rng = random.Random(seed)
    worst_ratio, worst_diff, nondeg = 0.0, -1e9, 0
    for t in range(trials):
        Q0 = 9
        ells = [5, 7, 11] if t % 2 else [5, 7]
        extra = 2 * (5 if t % 3 == 0 else 1) * (7 if t % 2 == 0 else 1)   # 2, and l^2 powers
        Q = Q0 * math.prod(ells) * extra
        R = [c for c in range(Q0) if c % 3]  # selector-like
        F = {(c, l): rng.sample(range(l), rng.randint(1, max(1, l // 4))) for c in R for l in ells}
        divs = [d for d in range(1, Q + 1) if Q % d == 0]
        nu = np.zeros(Q)
        for _ in range(rng.choice([20, 200])):
            d = rng.choice(divs); b = rng.randrange(d)
            nu[np.arange(b, Q, d)] += rng.uniform(-3, 3)
        nuhat = np.fft.fft(nu) / Q
        n = np.arange(Q)
        for c in R:
            fib = n[n % Q0 == c]
            p = {l: len(F[(c, l)]) / l for l in ells}
            x = {l: np.isin(fib % l, F[(c, l)]).astype(float) for l in ells}
            for r in range(1, len(ells) + 1):
                for S in itertools.combinations(ells, r):
                    yS = np.prod([x[l] - p[l] for l in S], axis=0)
                    lhs = abs(np.mean(nu[fib] * yS))
                    AS = 0.0
                    for a in range(Q0):
                        for hs in itertools.product(*[range(1, l) for l in S]):
                            k = (a * (Q // Q0) + sum(h * (Q // l) for h, l in zip(hs, S))) % Q
                            AS += abs(nuhat[k])
                    rhs = AS * math.prod(p[l] for l in S)
                    worst_diff = max(worst_diff, lhs - rhs)
                    if rhs > 1e-9:
                        nondeg += 1
                        worst_ratio = max(worst_ratio, lhs / rhs)
    print(f"Lemma 2.2 extended: max(lhs-rhs)={worst_diff:.3e}, max lhs/rhs={worst_ratio:.4f} over {nondeg} non-degenerate (c,S)")

run()
