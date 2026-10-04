"""Independent checks for reviews/exceptional-largesieve-review.md (EVIDENCE).

(a) Cor 2.2: g* from the dual QP; nu* = |g*|^2 is >= 0 on Z/M', >= 1 on A,
    E nu* = sum|gamma|^2, and its spectrum lies in {theta'-theta}; with a
    *genuine* Montgomery-Vaughan system (w = 1/(N-1+Q^2), operator norm
    verified numerically) the bound 1/F* >= N E nu*.
(b) Thm 4.1 final inequality F_w(pi) <= (R(pi)/N)^{1/(1+beta)} for the
    product measure, on a genuine N-large-sieve Farey system.
(c) Thm 6.2: (W-h)/(D*-h) >= (W-h)/((W-h)/N + X(pi)) for Gallagher kernels
    on small mixtures (D* by QP).
Run: PYTHONPATH=scripts uv run --with cvxpy --with numpy --with scipy python reviews/exceptional-largesieve-review-check.py
"""
import math
import random

import cvxpy as cp
import numpy as np


def farey(Mp, Q):
    return [(a, d) for d in range(1, Q + 1) if Mp % d == 0 for a in range(d) if math.gcd(a, d) == 1]


def avoider(Mp, classes):
    n = np.arange(Mp)
    bad = np.zeros(Mp, bool)
    for b, G in classes:
        bad |= (n % G) == (b % G)
    return np.nonzero(~bad)[0]


def ls_norm(thetas, w, N):
    """largest eigenvalue of sum_theta w_theta v_theta v_theta^*, v_theta=(e(n theta))_{n<N}."""
    n = np.arange(N)
    V = np.array([np.sqrt(wt) * np.exp(2j * np.pi * a * n / d) for (a, d), wt in zip(thetas, w)])
    return np.linalg.norm(V, 2) ** 2


def Fstar(Mp, A, th, w):
    n = np.arange(Mp)
    E = np.array([np.exp(2j * np.pi * a * n / d) for a, d in th])[:, A]
    T = np.sqrt(w)[:, None] * E
    pi = cp.Variable(len(A), nonneg=True)
    pr = cp.Problem(cp.Minimize(cp.sum_squares(np.vstack([T.real, T.imag]) @ pi)), [cp.sum(pi) == 1])
    pr.solve()
    assert pr.status == "optimal"
    return pr.value, pi.value


def dual(Mp, A, th, w):
    n = np.arange(Mp)
    E = np.array([np.exp(-2j * np.pi * a * n / d) for a, d in th])  # g(n)=sum gamma e(-n theta)
    gr, gi = cp.Variable(len(th)), cp.Variable(len(th))
    reg = E.real.T @ gr - E.imag.T @ gi
    pr = cp.Problem(cp.Minimize(cp.sum(cp.multiply(1 / w, cp.square(gr) + cp.square(gi)))), [reg[A] >= 1])
    pr.solve()
    assert pr.status == "optimal"
    gam = gr.value + 1j * gi.value
    g = E.T @ gam
    return pr.value, gam, g


def check_a(rng):
    print("(a) Cor 2.2 with genuine MV systems")
    for t in range(6):
        primes = rng.sample([3, 5, 7, 11], 3)
        Mp = math.prod(primes)
        classes = []
        for _ in range(rng.randint(3, 6)):
            G = math.prod(rng.sample(primes, rng.choice([1, 2])))
            classes.append((rng.randrange(G), G))
        A = avoider(Mp, classes)
        Q = rng.choice([5, 7, 15])
        th = farey(Mp, Q)
        N = rng.choice([8, 20, 50])
        w = np.full(len(th), 1.0 / (N - 1 + Q * Q))
        nrm = ls_norm(th, w, N)
        F, _ = Fstar(Mp, A, th, w)
        m, gam, g = dual(Mp, A, th, w)
        nu = np.abs(g) ** 2
        Enu = nu.mean()
        ok = (nrm <= 1 + 1e-9 and nu.min() >= -1e-9 and nu[A].min() >= 1 - 1e-5
              and abs(Enu - np.sum(np.abs(gam) ** 2)) < 1e-8 and 1 / F >= N * Enu * (1 - 1e-5)
              and abs(F * m - 1) < 1e-5)
        print(f"  M'={Mp} |A|={len(A)} N={N} Q={Q} ||LS||={nrm:.3f} 1/F*={1/F:.4f} m={m:.4f} "
              f"N*Enu*={N*Enu:.4f} min nu on A={nu[A].min():.4f} ok={ok}")
        assert ok


def check_b(rng):
    print("(b) Thm 4.1 chain F_w(pi) <= (R/N)^{1/(1+beta)} (genuine LS system)")
    for t in range(5):
        Q0, R, sp = 4, [1, 3], [5, 7, 11]
        Mp = Q0 * math.prod(sp)
        Fb = {(c, l): rng.sample(range(l), rng.randint(1, l // 2)) for c in R for l in sp}
        beta = rng.choice([0.1, 0.25, 0.5])
        pi = np.zeros(Mp)
        for n in range(Mp):
            c = n % Q0
            if c in R and not any(n % l in Fb[(c, l)] for l in sp):
                pi[n] = 1 / len(R) / math.prod(l - len(Fb[(c, l)]) for l in sp)
        hat = np.fft.fft(pi)
        Rpi = np.sum(np.abs(hat) ** (2 + 2 * beta))
        Q = rng.choice([7, 11, 20])
        th = farey(Mp, Q)
        N = rng.choice([10, 30])
        w = np.full(len(th), 1.0 / (N - 1 + Q * Q))
        assert ls_norm(th, w, N) <= 1 + 1e-9
        idx = [(a * (Mp // d)) % Mp for a, d in th]
        Fw = float(np.sum(w * np.abs(np.conj(hat[idx])) ** 2))
        rhs = (Rpi / N) ** (1 / (1 + beta))
        print(f"  beta={beta} N={N} Q={Q}: F_w(pi)={Fw:.5f} <= (R/N)^(1/(1+b))={rhs:.5f}  ok={Fw <= rhs}")
        assert Fw <= rhs + 1e-12


def check_c(rng):
    print("(c) Thm 6.2 Gallagher kernel: CRT optimum vs chi^2 bound")
    for t in range(5):
        primes = [3, 5, 7]
        Mp = 9 * 25 * 7
        classes = []
        for _ in range(rng.randint(2, 5)):
            G = rng.choice([3, 5, 7, 9, 15, 21, 35, 25])
            classes.append((rng.randrange(G), G))
        A = avoider(Mp, classes)
        S = [q for q in [3, 9, 5, 25, 7] ]
        Lam = {3: math.log(3), 9: math.log(3), 5: math.log(5), 25: math.log(5), 7: math.log(7)}
        N = rng.choice([4, 6])
        W = sum(Lam.values())
        h = max(sum(Lam[q] for q in S if m % q == 0) for m in range(1, N))
        # D(pi) = sum_q w(q) coll_q(pi): QP over pi on A
        pi = cp.Variable(len(A), nonneg=True)
        terms = []
        for q in S:
            Mq = np.zeros((q, len(A)))
            Mq[A % q, np.arange(len(A))] = 1
            terms.append(Lam[q] * cp.sum_squares(Mq @ pi))
        pr = cp.Problem(cp.Minimize(sum(terms)), [cp.sum(pi) == 1])
        pr.solve()
        Dstar = pr.value
        # X(pi) at uniform pi on A
        u = np.full(len(A), 1 / len(A))
        X = sum(Lam[q] / q * (q * sum(np.bincount(A % q, weights=u, minlength=q) ** 2) - 1) for q in S)
        if Dstar <= h:
            print(f"  N={N}: D*={Dstar:.4f} <= h={h:.4f}: no bound (vacuous)")
            continue
        B = (W - h) / (Dstar - h)
        lb = (W - h) / ((W - h) / N + X)
        print(f"  N={N} |A|={len(A)}: B*={B:.4f} >= (W-h)/((W-h)/N+X)={lb:.4f} ok={B >= lb - 1e-6}")
        assert B >= lb - 1e-6


if __name__ == "__main__":
    rng = random.Random(2024)
    check_a(rng)
    check_b(rng)
    check_c(rng)
    print("all checks passed")
