"""R27b from-scratch test of the inequality chain in LARGESIEVE2 Thm 9.1.

Thm 9.1's proof uses only property (1.1) of pi: E_pi f <= e^S E_U f for all
f >= 0 in V_D, with D = {1} u {lcm(q,q'): q,q' in S_<} u {q° : q in S_>=}.
Here we take ARBITRARY sets A ⊂ Z/Q and ARBITRARY pi on A, compute the
*exact* best S for that pi and that D by an LP, build random kernels
(moduli | Q, some >= N), and check

   D(pi) - h <= (W_K - h)/N + e^S (h + W_K/N)                       (*)
   (W_K - h)/(D(pi) - h) >= (N/2) e^{-S} / (1 + N h/(W_K - h))      (**)

(W = 1, i.e. every prime counts; q° = shortest prefix >= N of q built from
its prime powers in increasing order.)
"""
import math, random, itertools
import numpy as np
from scipy.optimize import linprog
from scipy.sparse import lil_matrix

PRIMES = [2, 3, 5, 7, 11]
Q = 4 * 9 * 5 * 7 * 11  # 13860


def factor(q):
    f = {}
    for p in PRIMES:
        while q % p == 0:
            f[p] = f.get(p, 0) + 1
            q //= p
    assert q == 1
    return f


def prefix(q, N):
    cur = 1
    for p, e in sorted(factor(q).items()):
        cur *= p**e
        if cur >= N:
            return cur
    return cur


def best_S(pi, Dset):
    Dset = sorted(set(Dset))
    cols = [(d, b) for d in Dset for b in range(d)]
    idx = {c: j for j, c in enumerate(cols)}
    M = lil_matrix((Q, len(cols)))
    for x in range(Q):
        for d in Dset:
            M[x, idx[(d, x % d)]] = 1.0
    M = M.tocsr()
    # maximise E_pi f s.t. f >= 0, E_U f = 1
    obj = -(pi @ M)
    eU = np.asarray(M.mean(axis=0)).ravel()
    res = linprog(obj, A_ub=-M, b_ub=np.zeros(Q), A_eq=eU[None, :], b_eq=[1.0],
                  bounds=[(None, None)] * len(cols), method="highs")
    assert res.status == 0, res.message
    return math.log(-res.fun)


def coll(pi, q):
    s = np.bincount(np.arange(Q) % q, weights=pi, minlength=q)
    return float(np.sum(s**2))


def main():
    rng = random.Random(5)
    divs = [d for d in range(1, Q + 1) if Q % d == 0]
    worst = math.inf
    trials = 0
    for t in range(40):
        N = rng.choice([6, 10, 15, 25, 40])
        # random A and pi (sometimes concentrated)
        dens = rng.choice([0.3, 0.6, 0.9])
        A = np.array([rng.random() < dens for _ in range(Q)])
        w = np.array([rng.random()**rng.choice([1, 4]) for _ in range(Q)]) * A
        pi = w / w.sum()
        S_mod = rng.sample([d for d in divs if d > 1], rng.randint(2, 6))
        wq = {q: rng.random() for q in S_mod}
        S_lt = [q for q in S_mod if q < N]
        S_ge = [q for q in S_mod if q >= N]
        Dset = {1} | {math.lcm(a, b) for a in S_lt for b in S_lt} | {prefix(q, N) for q in S_ge}
        S = max(0.0, best_S(pi, Dset))
        WK = sum(wq.values())
        h = max(sum(wq[q] for q in S_mod if m % q == 0) for m in range(1, N))
        Dpi = sum(wq[q] * coll(pi, q) for q in S_mod)
        if WK <= h or Dpi <= h:
            continue
        trials += 1
        lhs = Dpi - h
        rhs = (WK - h) / N + math.exp(S) * (h + WK / N)
        B = (WK - h) / (Dpi - h)
        Bcap = (N / 2) * math.exp(-S) / (1 + N * h / (WK - h))
        worst = min(worst, rhs / lhs, B / Bcap)
        if lhs > rhs + 1e-9 or B < Bcap - 1e-9:
            print("VIOLATION", N, S_mod, S, lhs, rhs, B, Bcap)
    print(f"Thm 9.1 chain: {trials} nontrivial trials, min slack ratio = {worst:.3f} (>=1 means OK)")


if __name__ == "__main__":
    main()
