"""EXCEPTIONAL_LARGESIEVE.md numerics (EVIDENCE only).

(1) Theorem 2.1: F*_w * m_w = 1 on random small class systems (two QPs;
    Farey and sparse non-conjugate-closed frequency sets; degenerate F*=0 case).
(2) Proposition 2.6: for prime-only (product) systems with full Farey
    frequencies, F*_1 = S(Q) (asserted to 1e-5).
(3) Example 5.2: twin pair system: induced prime-local system empty, but
    the composite modulus sees F* >= 1 + g.
(4) Theorem 4.1: the Hausdorff-Young/Jensen bound for R(pi) on random
    prime-slice systems, computed exactly by FFT.

Runtime: ~2 s of computation (plus uv/cvxpy start-up).
Run: PYTHONPATH=scripts uv run --with cvxpy --with numpy python scripts/ls_duality_check.py
"""
import itertools
import math
import random

import cvxpy as cp
import numpy as np


def farey(Mp, Q, dens=None):
    """frequencies a/d (reduced), d | Mp, d <= Q (or d in dens)."""
    out = []
    for d in range(1, Q + 1):
        if Mp % d:
            continue
        if dens is not None and d not in dens:
            continue
        for a in range(d):
            if math.gcd(a, d) == 1:
                out.append((a, d))
    return out


def char_matrix(Mp, thetas):
    n = np.arange(Mp)
    return np.array([np.exp(2j * np.pi * a * n / d) for a, d in thetas])  # |Theta| x Mp


def Fstar(Mp, avoid, thetas, w):
    E = char_matrix(Mp, thetas)[:, avoid]  # columns: n in A
    T = np.sqrt(w)[:, None] * E
    Tr = np.vstack([T.real, T.imag])
    pi = cp.Variable(len(avoid), nonneg=True)
    prob = cp.Problem(cp.Minimize(cp.sum_squares(Tr @ pi)), [cp.sum(pi) == 1])
    prob.solve()
    assert prob.status in ("optimal", "optimal_inaccurate"), prob.status
    return max(prob.value, 0.0)


def mstar(Mp, avoid, thetas, w):
    E = char_matrix(Mp, thetas)[:, avoid]  # g(n) = sum gamma_t e(-n t)  -> conj
    k = len(thetas)
    gr = cp.Variable(k)
    gi = cp.Variable(k)
    # Re g(n) = sum gr*cos(2pi n t) + gi*sin(2pi n t)
    C = E.real.T
    S = E.imag.T
    cons = [C @ gr + S @ gi >= 1]
    obj = cp.sum(cp.multiply(1 / w, cp.square(gr) + cp.square(gi)))
    prob = cp.Problem(cp.Minimize(obj), cons)
    prob.solve()
    if prob.status in ("infeasible", "infeasible_inaccurate"):
        return math.inf
    assert prob.status in ("optimal", "optimal_inaccurate"), prob.status
    return prob.value


def avoider(Mp, classes):
    bad = np.zeros(Mp, bool)
    n = np.arange(Mp)
    for b, G in classes:
        bad |= (n % G) == (b % G)
    return np.nonzero(~bad)[0]


def R_classes(M):
    """R(M) forced classes -4D mod M, D | A^2, gcd(D,M)=1, M = 3 mod 4."""
    A = (M + 1) // 4
    A2 = A * A
    out = set()
    for D in range(1, A2 + 1):
        if A2 % D == 0 and math.gcd(D, M) == 1:
            out.add((-4 * D) % M)
    return sorted(out)


def check1(rng):
    print("(1) duality F* * m_w = 1")
    worst = 0
    for trial in range(12):
        primes = rng.sample([3, 5, 7, 11, 13], 3)
        Mp = math.prod(primes)
        classes = []
        for _ in range(rng.randint(2, 5)):
            sub = rng.sample(primes, rng.choice([1, 2]))
            G = math.prod(sub)
            classes.append((rng.randrange(G), G))
        A = avoider(Mp, classes)
        Q = rng.choice([5, 7, 15, 21, 35])
        th = farey(Mp, Q)
        if trial % 2:  # sparse, not closed under conjugation (0 kept; without 0, F* is typically 0)
            th = [(0, 1)] + rng.sample([t for t in farey(Mp, Mp) if t[1] > 1], 5)
        w = np.array([rng.uniform(0.5, 1.5) for _ in th])
        F = Fstar(Mp, A, th, w)
        m = mstar(Mp, A, th, w)
        worst = max(worst, abs(F * m - 1))
        print(f"  M'={Mp:5d} |A|={len(A):4d} |Theta|={len(th):3d}  F*={F:.6f} m_w={m:.6f} F*m={F*m:.6f}")
    print(f"  max |F*m-1| = {worst:.2e}")
    assert worst < 1e-5
    # F* = 0 case: no classes, Theta without 0 -> uniform pi kills all; m_w = inf
    Mp = 105
    A = avoider(Mp, [])
    th = [(1, 3), (2, 7), (4, 15)]
    F = Fstar(Mp, A, th, np.ones(3))
    m = mstar(Mp, A, th, np.ones(3))
    print(f"  degenerate case: F*={F:.2e}, m_w={m}")
    assert F < 1e-8 and m == math.inf


def S_of_Q(omega, Q):
    ps = sorted(omega)
    tot = 0.0
    for r in range(len(ps) + 1):
        for sub in itertools.combinations(ps, r):
            s = math.prod(sub)
            if s <= Q:
                tot += math.prod(omega[p] / (p - omega[p]) for p in sub)
    return tot


def check2(rng):
    print("(2) prime-only systems: F*_1 = S(Q) (Prop 2.6)")
    worst = 0.0
    for trial in range(8):
        primes = [3, 5, 7, 11]
        Mp = math.prod(primes)
        omega = {p: rng.randint(1, (p - 1) // 2) for p in primes}
        classes = []
        for p in primes:
            for b in rng.sample(range(p), omega[p]):
                classes.append((b, p))
        A = avoider(Mp, classes)
        Q = rng.choice([7, 15, 21, 35])
        th = farey(Mp, Q)
        F = Fstar(Mp, A, th, np.ones(len(th)))
        S = S_of_Q(omega, Q)
        worst = max(worst, abs(F - S))
        print(f"  Q={Q:2d} omega={omega}  F*={F:.5f}  S(Q)={S:.5f}")
    print(f"  max |F*-S| = {worst:.2e}")
    assert worst < 1e-5


def check3():
    print("(3) Example 5.2: pairs 5*7=35, 11*13=143 (m = 3 mod 4); emptiness checked directly (both violate the crude omega<l sufficient condition; conclusion still holds)")
    pairs = [(5, 7), (11, 13)]
    Mp = 35 * 143
    classes = []
    for l1, l2 in pairs:
        m = l1 * l2
        assert m % 4 == 3
        for b in R_classes(m):
            classes.append((b, m))
    A = avoider(Mp, classes)
    for p in [5, 7, 11, 13]:
        assert len(set((A % p).tolist())) == p
    print("  induced prime-local system: empty (all residues mod 5,7,11,13 occur)")
    for l1, l2 in pairs:
        m = l1 * l2
        om = len(R_classes(m))
        th = farey(Mp, m, dens={d for d in (1, l1, l2, m)})
        F = Fstar(Mp, A, th, np.ones(len(th)))
        print(f"  m={m}: omega={om}, 1+g={m/(m-om):.6f}, F*(div m)={F:.6f}")
        assert F >= m / (m - om) - 1e-6


def check4(rng):
    print("(4) Theorem 4.1: R(pi) <= (Q0/|R|) E_R prod(1+sum|phi|^p')")
    for trial in range(6):
        Q0 = 4
        R = [1, 3]
        slice_primes = [5, 7, 11]
        Mp = Q0 * math.prod(slice_primes)
        F = {(c, l): rng.sample(range(l), rng.randint(1, l // 2)) for c in R for l in slice_primes}
        beta = rng.choice([0.1, 0.25, 0.5])
        pp = 2 + 2 * beta
        pi = np.zeros(Mp)
        for n in range(Mp):
            c = n % Q0
            if c not in R:
                continue
            if any(n % l in F[(c, l)] for l in slice_primes):
                continue
            pi[n] = 1.0 / len(R) / math.prod(l - len(F[(c, l)]) for l in slice_primes)
        assert abs(pi.sum() - 1) < 1e-12
        hat = np.fft.fft(pi)  # pi_hat(-k/Mp); modulus is what matters
        Rpi = np.sum(np.abs(hat) ** pp)
        bound = 0.0
        for c in R:
            prod = 1.0
            for l in slice_primes:
                f = F[(c, l)]
                s = 0.0
                for a in range(1, l):
                    phi = abs(sum(np.exp(2j * np.pi * a * b / l) for b in f)) / (l - len(f))
                    s += phi ** pp
                prod *= 1 + s
            bound += prod / len(R)
        bound *= Q0 / len(R)
        print(f"  beta={beta}: R(pi)={Rpi:.5f}  bound={bound:.5f}  ok={Rpi <= bound + 1e-9}")
        assert Rpi <= bound + 1e-9


if __name__ == "__main__":
    rng = random.Random(17)
    check1(rng)
    check2(rng)
    check3()
    check4(rng)
