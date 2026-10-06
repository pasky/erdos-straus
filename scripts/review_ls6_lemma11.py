"""R71 from-scratch check of LS6 Lemma 1.1 (prefactor in the damped-collision bound).

sigma: random probability on Z/M, M = product of distinct small primes (so coordinates
are Z/p, E_l = 1).  Fourier: sigma^(theta) = sum_x sigma(x) e(theta.x), theta in Z/M.
R_{2+2b}(sigma) = sum_theta |sigma^(theta)|^{2+2b}.
E_T R_2(sigma_T) = sum_T prod_{l in T} w_l prod_{l notin T}(1-w_l) * M_T * sum_a sigma_T(a)^2.
Lambda := smallest value making |sigma^|^{2b} <= Lambda^{2b} prod_{supp} w_l hold (and >= 1).
Check R_{2+2b} <= Lambda^{2b} E_T R_2(sigma_T).
"""
import itertools, random, cmath, math, sys

def run(seed, primes=(2, 3, 5, 7), beta=0.3):
    rng = random.Random(seed)
    M = math.prod(primes)
    # sparse-ish random law
    sig = [rng.random() ** 6 for _ in range(M)]
    s = sum(sig); sig = [v / s for v in sig]
    w = {p: rng.uniform(0.05, 1.0) for p in primes}
    # Fourier
    R = 0.0; Lam = 1.0
    for th in range(M):
        c = sum(sig[x] * cmath.exp(2j * math.pi * th * x / M) for x in range(M))
        a = abs(c)
        R += a ** (2 + 2 * beta)
        if th:
            supp = [p for p in primes if th % p]  # theta's p-component nonzero
            ws = math.prod(w[p] for p in supp)
            Lam = max(Lam, a / ws ** (1 / (2 * beta)))
    # E_T R_2(sigma_T)
    ET = 0.0
    for r in range(len(primes) + 1):
        for T in itertools.combinations(primes, r):
            pr = math.prod(w[p] if p in T else 1 - w[p] for p in primes)
            MT = math.prod(T)
            push = [0.0] * MT
            for x in range(M):
                push[x % MT] += sig[x]
            ET += pr * MT * sum(v * v for v in push)
    rhs = Lam ** (2 * beta) * ET
    assert R <= rhs * (1 + 1e-9), (seed, R, rhs)
    return R / rhs, Lam

if __name__ == "__main__":
    seeds = [int(a) for a in sys.argv[1:]] or range(1, 41)
    worst = 0
    for sd in seeds:
        r, L = run(sd)
        worst = max(worst, r)
    print("Lemma 1.1 holds on", len(list(seeds)), "seeds; max ratio", round(worst, 4))
