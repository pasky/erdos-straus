"""R268: (1) Lemma 2.2(a)(b) numerically from scratch; (2) per-j b=1 statistics (F_j: jp+1 has a divisor w = -1 mod 4j)
for all primes p = 1 (4) <= 1e6, j <= 24: failure rates, pairwise joint/product ratios, all-j failures vs independence;
(3) odd-prime support-1 (Fp_j) at odd j >= 3."""
import itertools
import numpy as np
from sympy import primerange, divisors, jacobi_symbol, factorint
from sympy.ntheory import legendre_symbol


def kron_m4d(d, n):
    # Kronecker symbol (-4d / n) for odd n > 0: equals Jacobi (-4d/n) = (-1/n)(d/n)
    return jacobi_symbol(-1, n) * jacobi_symbol(d % n, n) if n > 1 else 1


# (1) Lemma 2.2
bad_a = bad_b = hits = lev = 0
for p in primerange(5, 4000):
    if p % 4 != 1: continue
    for d in range(1, (p + 3) // 8 + 1):
        if d % p == 0: continue
        N = p + 4 * d
        for w in divisors(N):
            if w < N and w % (4 * d) == 4 * d - 1:
                hits += 1
                if jacobi_symbol(w, p) != -1: bad_a += 1
        if legendre_symbol(d % p, p) == -1:
            lev += 1
            if kron_m4d(d, N) != -1: bad_b += 1
print(f"(1) Lemma 2.2(a): {hits} divisor-form hits p<4000, exceptions {bad_a}; (b): {lev} levels (d/p)=-1, exceptions {bad_b}")

# (2) per-j
J = 24
ps = [p for p in primerange(5, 10**6 + 1) if p % 4 == 1]
F = np.zeros((len(ps), J + 1), dtype=bool)   # F[i, j] = True if FAIL at j
Fp_odd_ok = 0
for i, p in enumerate(ps):
    for j in range(1, J + 1):
        n = j * p + 1; m = 4 * j
        F[i, j] = not any(w % m == m - 1 for w in divisors(n))
        if j % 2 == 1 and j >= 3:
            # odd prime support-1: prime s | jp+1, s = 3j-1 (mod 4j)
            if any(s % m == (3 * j - 1) % m and s > 2 for s in factorint(n)): Fp_odd_ok += 1
rate = F[:, 1:].mean(axis=0)
print("(2) primes:", len(ps), " failure rates j=1..24:", " ".join(f"{r:.3f}" for r in rate))
ratios = []
for j, k in itertools.combinations(range(1, J + 1), 2):
    ratios.append((F[:, j] & F[:, k]).mean() / (rate[j - 1] * rate[k - 1]))
ratios = np.array(ratios)
jk = list(itertools.combinations(range(1, J + 1), 2))[int(ratios.argmax())]
print(f"    pairwise joint/product: mean {ratios.mean():.4f}, max {ratios.max():.3f} at {jk}, min {ratios.min():.3f}")
allf = int(F[:, 1:].all(axis=1).sum())
print(f"    all 24 fail: {allf}; independence prediction {len(ps) * np.prod(rate):.2f}")
print("(3) odd j>=3 odd-prime support-1 successes:", Fp_odd_ok)
