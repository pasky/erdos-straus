#!/usr/bin/env python3
"""O21 (EXCEPTIONAL_TUPLES.md §5): empirical order-j witness correlation sums
S_j(N) = sum_{n<=N} binom(f_y(n), j) for the prime family vs the CRT values
N*e_j(p), plus the Bonferroni bounds of Theorem 2.1 and the share of the
CRT mass e_j carried by j-sets of primes with product > N.

usage: tuples_moments.py N y1[,y2,...] [mode=all|prime] [Jmax] [family=es|rand|randqnr] [seed]
family rand: F_l replaced by a random set of the same size (nonzero residues);
randqnr: random set of quadratic NON-residues of the same size (keeps the
Mordell/Jacobi structure of R(l), destroys the divisor structure).
Memory: O(N) int32/int16 arrays (N=1e7: < 300 MB).
"""
import sys
from math import comb, log, exp

import numpy as np


def primes_upto(x):
    s = np.ones(x + 1, dtype=bool)
    s[:2] = False
    for i in range(2, int(x ** 0.5) + 1):
        if s[i]:
            s[i * i::i] = False
    return np.nonzero(s)[0]


def divisors_of_square(a):
    # divisors of a^2
    fac = {}
    m, q = a, 2
    while q * q <= m:
        while m % q == 0:
            fac[q] = fac.get(q, 0) + 1
            m //= q
        q += 1
    if m > 1:
        fac[m] = fac.get(m, 0) + 1
    ds = [1]
    for q, e in fac.items():
        ds = [d * q ** k for d in ds for k in range(2 * e + 1)]
    return ds


def R_set(ell):
    A = (ell + 1) // 4
    return sorted({(-4 * D) % ell for D in divisors_of_square(A)})


def esym(ps, J):
    """elementary symmetric e_0..e_J of ps (float64)."""
    e = np.zeros(J + 1)
    e[0] = 1.0
    for p in ps:
        e[1:] = e[1:] + p * e[:-1]
    return e


def mass_below(ps, logs, J, L, step=0.01):
    """sum over j-sets with sum(floor(log l/step)) <= L/step of prod p;
    floor => overestimates the below-N mass (conservative)."""
    B = int(L / step)
    dp = np.zeros((J + 1, B + 1))
    dp[0, 0] = 1.0
    for p, lg in zip(ps, logs):
        w = int(lg / step)
        if w > B:
            continue
        dp[1:, w:] = dp[1:, w:] + p * dp[:-1, :B + 1 - w]
    return dp.sum(axis=1)


def main():
    N = int(float(sys.argv[1]))
    ys = [int(float(t)) for t in sys.argv[2].split(',')]
    mode = sys.argv[3] if len(sys.argv) > 3 else 'all'
    Jmax = int(sys.argv[4]) if len(sys.argv) > 4 else 40
    family = sys.argv[5] if len(sys.argv) > 5 else 'es'
    rng = np.random.default_rng(int(sys.argv[6]) if len(sys.argv) > 6 else 1)
    if mode == 'all':
        ns = np.arange(1, N + 1, dtype=np.int64)
    else:
        ns = primes_upto(N).astype(np.int64)
        ns = ns[ns > max(ys)]
    M = len(ns)
    print(f"# N={N} mode={mode} family={family} sample={M} log N={log(N):.3f}")
    P = [int(l) for l in primes_upto(max(ys)) if l % 4 == 3]
    f = np.zeros(M, dtype=np.int16)
    done = 0
    for y in ys:
        ps, logs, Fs = [], [], []
        for l in P:
            if l > y:
                break
            Rl = R_set(l)
            if family == 'rand':
                Rl = sorted(rng.choice(np.arange(1, l), size=len(Rl), replace=False).tolist())
            elif family == 'randqnr':
                qnr = np.array([r for r in range(1, l) if pow(r, (l - 1) // 2, l) == l - 1])
                Rl = sorted(rng.choice(qnr, size=len(Rl), replace=False).tolist())
            if l > done:
                tab = np.zeros(l, dtype=np.int16)
                tab[Rl] = 1
                f += tab[ns % l]
            den = l if mode == 'all' else l - 1  # prime n: uniform on nonzero residues
            ps.append(len(Rl) / den)
            logs.append(log(l))
            Fs.append(len(Rl))
        done = y
        mu = sum(ps)
        J = Jmax
        e = esym(ps, J)
        eF = esym([float(F) for F in Fs], J)
        below = mass_below(ps, logs, J, log(N))
        hist = np.bincount(f)
        S = np.array([sum(int(hist[v]) * comb(v, j) for v in range(j, len(hist))) if j < len(hist) else 0
                      for j in range(J + 1)], dtype=float) / M
        avoid = hist[0] / M
        crt0 = float(np.prod([1 - p for p in ps]))
        print(f"\n## y={y} primes={len(ps)} mu={mu:.4f} E_int f={f.mean():.4f} "
              f"avoid_int={avoid:.4e} avoid_CRT={crt0:.4e} max f={f.max()}")
        print("# j  S_j/N   e_j   ratio  aboveN_share(e_j)  termwise_bound/(N e_j)   "
              "Bonf_int(j even)  Bonf_CRT")
        bi = bc = 0.0
        for j in range(J + 1):
            bi += (-1) ** j * S[j]
            bc += (-1) ** j * e[j]
            ab = 1 - below[j] / e[j] if e[j] > 1e-300 else float('nan')
            tw = eF[j] / (M * e[j]) if e[j] > 0 else float('nan')
            r = S[j] / e[j] if e[j] > 0 else float('nan')
            bon = f"{bi:+.4e} {bc:+.4e}" if j % 2 == 0 else ""
            print(f"{j:3d} {S[j]:.4e} {e[j]:.4e} {r:.4f} {ab:.3f} {tw:.2e} {bon}")
        print("# TC check: K  eta(K)=max_{j<=K}|S_j/N-e_j|  eta_K=exp(-K/e^2)/K  "
              "mu<=K/e^2?  TC(N;K,y,eta_K) holds?")
        for K in range(2, J + 1, 2):
            eta = max(abs(S[j] - e[j]) for j in range(K + 1))
            thr = exp(-K / exp(2)) / K
            print(f"#TC {K:3d} {eta:.3e} {thr:.3e} {mu <= K / exp(2)} {eta <= thr}")


if __name__ == '__main__':
    main()
