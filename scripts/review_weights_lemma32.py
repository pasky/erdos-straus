"""R81: brute-force Lemma 3.2 (one-prime anti-concentration) and Lemma 3.1 / Thm 3.3 chain.

Lemma 3.2: l odd prime, l !| N, F subset Z/l, |F|=k, k/l <= 1/4:
    1 - |phi_l(N)| >= 9/(256 k^2),  phi_l(N) = sum_{h!=0} |1hat_F(h)| e(Nh/l) / a_l.
phi depends on F only up to translation, so we enumerate F containing 0.
Exhaustive for l <= 31; random samples for 37..61.

Lemma 3.1 + Thm 3.3 chain on products of 2-3 small primes:
    M_S^w (w=|S_N|) >= (1/2) A_S (1-|prod phi|)        (Lemma 3.1, c0=1)
    and  prod_S 2p(1-p) <= (512/9) M_S^w e^{-s(S)} with s_l = log(l/(2k^3)) (good) or log(1/(2p)),
    whenever S contains a good prime l0 !| N  (the per-S tail inequality of Thm 3.3).
"""
import itertools
import math
import numpy as np

rng = np.random.default_rng(8181)


def phis_for_sets(l, sets):
    """sets: (m,k) int array. Return (m, l-1) array of phi(N), N=1..l-1."""
    m = sets.shape[0]
    ind = np.zeros((m, l))
    np.put_along_axis(ind, sets, 1.0, axis=1)
    F = np.abs(np.fft.fft(ind, axis=1)) / l  # |1hat(h)|
    F[:, 0] = 0
    a = F.sum(axis=1, keepdims=True)
    h = np.arange(l)
    Ns = np.arange(1, l)
    C = np.cos(2 * np.pi * np.outer(h, Ns) / l)  # (l, l-1)
    return (F @ C) / a, a[:, 0]


def lemma32():
    print("Lemma 3.2: min over F,N of (1-|phi|) / (9/(256k^2))   [must be >= 1]")
    worst = math.inf
    for l in [5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 61]:
        for k in range(1, l // 4 + 1):
            ncomb = math.comb(l - 1, k - 1)
            if ncomb <= 700_000:
                sets = np.array([(0,) + c for c in itertools.combinations(range(1, l), k - 1)], dtype=int)
                mode = "all"
            else:
                sets = np.array([np.concatenate([[0], rng.choice(np.arange(1, l), k - 1, replace=False)]) for _ in range(20000)])
                mode = "rand"
            out = []
            for chunk in np.array_split(sets, max(1, len(sets) // 100000)):
                ph, a = phis_for_sets(l, chunk)
                out.append((1 - np.abs(ph)).min())
            r = min(out) / (9 / (256 * k * k))
            worst = min(worst, r)
            print(f"  l={l:2d} k={k:2d} ({mode}, {len(sets)} sets): min(1-|phi|)={min(out):.4f}  ratio={r:9.2f}")
    print(f"overall worst ratio = {worst:.3f}")


def fourier_abs(l, F):
    ind = np.zeros(l)
    ind[list(F)] = 1
    return np.abs(np.fft.fft(ind)) / l


def chain():
    print("Lemma 3.1 / Thm 3.3 per-S chain on random systems (w = |S_N|, c0 = 1):")
    worst31 = math.inf
    worst33 = math.inf
    primes = [5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
    for trial in range(400):
        r = rng.integers(1, 4)
        S = sorted(rng.choice(primes, r, replace=False).tolist())
        Fs = {}
        for l in S:
            k = int(rng.integers(1, l // 4 + 1))
            Fs[l] = rng.choice(l, k, replace=False)
        Q = int(np.prod(S))
        N = int(rng.integers(1, 3 * Q))
        # m_S on Theta_S via CRT: theta = sum h_l / l
        grids = np.meshgrid(*[np.arange(1, l) for l in S], indexing="ij")
        theta = sum(g / l for g, l in zip(grids, S)) % 1.0
        mS = np.ones_like(theta)
        for g, l in zip(grids, S):
            mS = mS * fourier_abs(l, Fs[l])[g]
        sN = np.abs(np.sin(np.pi * N * theta) / np.sin(np.pi * theta))
        M = (mS * sN).sum()
        A = mS.sum()
        prodphi = 1.0
        for l in S:
            fa = fourier_abs(l, Fs[l]); fa[0] = 0
            prodphi *= (fa * np.cos(2 * np.pi * N * np.arange(l) / l)).sum() / fa.sum()
        lb31 = 0.5 * A * (1 - abs(prodphi))
        if lb31 > 0:
            worst31 = min(worst31, M / lb31)
        # Thm 3.3 tail inequality, s_* = log 2: good iff k^3 <= l/4
        good = [l for l in S if len(Fs[l]) ** 3 <= l / 4]
        cand = [l for l in good if N % l != 0]
        if not cand:
            continue
        k0 = len(Fs[cand[0]])
        s = 0.0
        lhs = 1.0
        for l in S:
            k = len(Fs[l]); p = k / l
            s += math.log(l / (2 * k ** 3)) if l in good else math.log(1 / (2 * p))
            lhs *= 2 * p * (1 - p)
        rhs = (512 / 9) * M * math.exp(-s)
        worst33 = min(worst33, rhs / lhs)
    print(f"  min M_S / [(1/2)A_S(1-|prod phi|)] = {worst31:.4f}  [>= 1 required]")
    print(f"  min (512/9) M_S e^-s(S) / prod 2p(1-p) = {worst33:.4f}  [>= 1 required]")


if __name__ == "__main__":
    lemma32()
    chain()
