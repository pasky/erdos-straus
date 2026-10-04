"""EXCEPTIONAL_NONCRT.md companion checks.

Part 1 (Lemma 2.2, Prop 2.1 identities): exact check on random small
prime-slice systems over Z/Q_tot (Q0 = 3, primes 5,7,11[,13]) with random
real combinations nu of class indicators (not necessarily majorants; Lemma
2.2 is linear and needs no positivity).

Part 2 (toy LP, EVIDENCE): Boolean hit-pattern model with m slice primes.
Minimise E nu subject to nu >= 0, nu(0) >= 1 and either
  (C) class-coefficient budget  sum_T |e_T| prod_T f_l <= B   (monomial basis x^T)
  (F) Fourier-l1 budget          sum_{S!=0} |d_S| prod_S a_l <= B  (biased Walsh basis)
where a_l = sum_{h!=0} |1_F^(h)| is the exact Fourier l1 mass of y_l.
Run: uv run --with scipy python scripts/noncrt_checks.py
"""
import itertools
import math
import random
import sys

import numpy as np


def part1(trials=40, seed=1):
    rng = random.Random(seed)
    worst = -1e9
    for t in range(trials):
        Q0 = 3
        ells = [5, 7, 11] if t % 2 else [5, 7, 11, 13]
        Q = Q0 * math.prod(ells)
        R = [1, 2]
        F = {(c, l): rng.sample(range(l), rng.randint(1, max(1, l // 4))) for c in R for l in ells}
        # random nu: combination of classes with moduli dividing Q
        nu = np.zeros(Q)
        divs = [d for d in range(1, Q + 1) if Q % d == 0]
        for _ in range(30):
            d = rng.choice(divs)
            b = rng.randrange(d)
            nu[np.arange(b, Q, d)] += rng.uniform(-3, 3)
        nuhat = np.fft.fft(nu) / Q  # nuhat[k] = E nu(n) e(-nk/Q)
        n = np.arange(Q)
        for c in R:
            fib = n[n % Q0 == c]
            p = {l: len(F[(c, l)]) / l for l in ells}
            x = {l: np.isin(fib % l, F[(c, l)]).astype(float) for l in ells}
            for r in range(1, len(ells) + 1):
                for S in itertools.combinations(ells, r):
                    yS = np.prod([x[l] - p[l] for l in S], axis=0)
                    lhs = abs(np.mean(nu[fib] * yS))  # = |d_S| prod p(1-p)
                    # A_S: frequencies a/Q0 + sum h_l/l, all h_l != 0
                    AS = 0.0
                    for a in range(Q0):
                        for hs in itertools.product(*[range(1, l) for l in S]):
                            th = a / Q0 + sum(h / l for h, l in zip(hs, S))
                            k = int(round((th % 1.0) * Q)) % Q
                            AS += abs(nuhat[k])
                    rhs = AS * math.prod(p[l] for l in S)
                    worst = max(worst, lhs - rhs)
    print(f"Part 1 (Lemma 2.2): {trials} systems, max(lhs - rhs) = {worst:.3e} (must be <= ~1e-12)")
    return worst <= 1e-9


def walsh_matrix(ps):
    """rows: points x in {0,1}^m; cols: subsets S (bitmask); entry y^S(x)."""
    m = len(ps)
    N = 1 << m
    M = np.ones((N, N))
    for xi in range(N):
        for S in range(N):
            v = 1.0
            for i in range(m):
                if S >> i & 1:
                    v *= ((xi >> i) & 1) - ps[i]
            M[xi, S] = v
    return M


def mono_matrix(m):
    N = 1 << m
    M = np.zeros((N, N))
    for xi in range(N):
        for T in range(N):
            M[xi, T] = 1.0 if (xi & T) == T else 0.0
    return M


def part2(m=8, seed=3):
    from scipy.optimize import linprog
    if m > 10:
        raise SystemExit("m > 10 needs Theta(4^m) dense storage; refusing")
    rng = random.Random(seed)
    primes = [l for l in range(5, 200) if all(l % q for q in range(2, int(l ** .5) + 1))][:m]
    fs, ps, As = [], [], []
    for l in primes:
        f = max(1, min(l // 4, int(round(l ** 0.35))))
        Fl = rng.sample(range(l), f)
        hat = np.array([sum(np.exp(-2j * np.pi * b * h / l) for b in Fl) / l for h in range(l)])
        fs.append(f); ps.append(f / l); As.append(float(np.sum(np.abs(hat[1:]))))
    N = 1 << m
    prob = np.array([math.prod(ps[i] if (x >> i) & 1 else 1 - ps[i] for i in range(m)) for x in range(N)])
    W = walsh_matrix(ps)          # nu = W d
    Mo = mono_matrix(m)           # nu = Mo e
    wF = np.array([math.prod(As[i] for i in range(m) if S >> i & 1) for S in range(N)]); wF[0] = 0.0
    wC = np.array([math.prod(fs[i] for i in range(m) if T >> i & 1) for T in range(N)])
    print(f"Part 2 toy: primes {primes}\n  f = {fs}\n  a_l = {[round(a, 2) for a in As]}")

    def solve(Mat, wts, B):
        # vars: coef (N), t (N) with t >= |coef|; nu = Mat coef >= 0, nu(0) >= 1, sum wts t <= B
        nv = 2 * N
        c = np.concatenate([prob @ Mat, np.zeros(N)])
        A, b = [], []
        A.append(np.concatenate([-Mat, np.zeros((N, N))], axis=1)); b.append(np.zeros(N))
        A.append(np.concatenate([-Mat[0:1], np.zeros((1, N))], axis=1)); b.append([-1.0])
        I = np.eye(N)
        A.append(np.concatenate([I, -I], axis=1)); b.append(np.zeros(N))
        A.append(np.concatenate([-I, -I], axis=1)); b.append(np.zeros(N))
        A.append(np.concatenate([np.zeros((1, N)), wts[None, :]], axis=1)); b.append([B])
        res = linprog(c, A_ub=np.vstack(A), b_ub=np.concatenate(b), bounds=[(None, None)] * nv, method="highs")
        if res.status != 0 or not np.isfinite(res.fun) or res.fun <= 0:
            raise RuntimeError(f"LP failed: status={res.status} fun={res.fun}")
        return res.fun

    full = -sum(math.log(1 - p) for p in ps)
    print(f"  full mass -log P(avoid) = {full:.3f}")
    print("  B        saving(C: coeff budget)  saving(F: Fourier-l1 budget)")
    for B in [2, 4, 8, 16, 32, 64, 128, 256, 1024, 4096]:
        eC = solve(Mo, wC, B); eF = solve(W, wF, B)
        print(f"  {B:<8d} {-math.log(eC):10.4f}             {-math.log(eF):10.4f}")


if __name__ == "__main__":
    ok = part1()
    part2(m=int(sys.argv[1]) if len(sys.argv) > 1 else 8)
    sys.exit(0 if ok else 1)
