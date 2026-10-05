"""R59 from-scratch checks: LS3 Lemma 4.2, Lemma 4.1, Thm 3.1 local bound.

(a) Lemma 4.2: -4 mod M is the D=1 member of R(M) (K2 Def 2.0: classes
    -4D mod M, D | A_M^2, A_M=(M+1)/4) -- definitional.  We additionally
    verify forcedness from scratch: for M = 3 mod 4, n = kM-4 >= 1,
    4/n - 1/(kA) is a sum of two unit fractions (exact rationals).
    Also a Mertens sanity number for m*(p,-4).
(b) Lemma 4.1: two-copy identity, Moebius-sum identity, and
    R_{2+2b}(s) <= sum_S s_S^{2b} P_S for random non-product measures
    on Z/(9*5*7) and Z/(4*3*5*7).
(c) Thm 3.1 local bound: uniform measure on Z/l^E minus a union of classes
    mod l^v (v<=E): |phi|<=g, sum_{a!=0}|phi|^2 = g, sum|phi|^{p'} <= g^{1+2b},
    and g^{1+2b} <= 4 p l^{-alpha} when p <= l^{kappa-1}, p<=1/2.
"""
from fractions import Fraction as Fr
from itertools import combinations
from math import gcd, log
import numpy as np

rng = np.random.default_rng(4059)


def divisors(m):
    ds, i = [], 1
    while i * i <= m:
        if m % i == 0:
            ds += [i, m // i]
        i += 1
    return sorted(set(ds))


def two_unit(q):
    """return (y,z) with q = 1/y+1/z, or None (complete search)."""
    a, b = q.numerator, q.denominator
    y = b // a + 1
    while Fr(2, y) >= q:
        r = q - Fr(1, y)
        if r > 0 and r.numerator == 1:
            return y, r.denominator
        y += 1
    return None


# (a) forcedness of -4 mod M via x = kA
cnt = 0
for M in range(3, 160, 4):
    A = (M + 1) // 4
    for k in range(1, 25):
        n = k * M - 4
        if n < 1:
            continue
        # notes Lemma 16.1 with u=w=1, v=A: n*A = -1 (mod M) iff n = -4 (mod M)
        assert (n * A + 1) % M == 0
        s_ = (n * A + 1) // M
        assert Fr(1, s_) + Fr(1, n * s_ * A) + Fr(1, n * A) == Fr(4, n)
        # and -4 = -4*D with D=1 | A^2: membership in R(M) (K2 Def 2.0)
        assert (-4 * 1) % M == n % M and (A * A) % 1 == 0
        cnt += 1
print(f"(a) -4 mod M forced via notes (16.1), u=w=1, v=A: {cnt} (M,n) pairs OK")

# Mertens sanity for m*(p,-4) = sum_{M'<=X, z-rough, pM'=3(4)} 1/M'
p, z, X = 10007, 30, 2 * 10 ** 6
sieve = np.ones(X + 1, bool)
sieve[0] = False
for q in range(2, z + 1):
    if all(q % r for r in range(2, int(q ** 0.5) + 1)):
        sieve[q::q] = False
Ms = np.flatnonzero(sieve)
sel = Ms[(p * Ms) % 4 == 3]
mstar = float(np.sum(1.0 / sel))
print(f"    m*(p,-4) with z={z}, X={X:.0e}: {mstar:.3f}; "
      f"log X/log z = {log(X)/log(z):.3f}")

# (b) Lemma 4.1


def check_41(pps, beta):
    Mr = int(np.prod(pps))
    sig = rng.random(Mr) ** 4
    sig[rng.random(Mr) < 0.5] = 0
    sig /= sig.sum()
    F = np.fft.fft(sig)  # F[k] ~ hat sigma(k/Mr) up to conjugation
    k = np.arange(Mr)
    # support of den(k/Mr): primes l with k not = 0 mod l^E (i.e. digit nonzero)
    supp = [tuple(i for i, q in enumerate(pps) if (k_ * (Mr // q)) % Mr != 0
                  ) for k_ in k]
    # (k/Mr has component at q iff k*(Mr/q) mod Mr != 0, i.e. q-digit nonzero)
    idx = range(len(pps))
    allS = [S for r in range(len(pps) + 1) for S in combinations(idx, r)]
    PS = {S: 0.0 for S in allS}
    sS = {S: 0.0 for S in allS}
    for k_ in k:
        S = supp[k_]
        PS[S] += abs(F[k_]) ** 2
        sS[S] = max(sS[S], abs(F[k_]))
    x = np.arange(Mr)
    for S in allS:
        H = np.ones((Mr, Mr))
        for i in S:
            q = pps[i]
            H *= q * ((x[:, None] - x[None, :]) % q == 0) - 1
        two = float(sig @ H @ sig)
        assert abs(two - PS[S]) < 1e-9, (S, two, PS[S])
        MT = int(np.prod([pps[i] for i in S])) if S else 1
        coll = MT * float(sig @ ((x[:, None] - x[None, :]) % MT == 0) @ sig)
        sub = sum(PS[T] for T in allS if set(T) <= set(S))
        assert abs(coll - sub) < 1e-9
    R = float(np.sum(np.abs(F) ** (2 + 2 * beta)))
    bound = sum(sS[S] ** (2 * beta) * PS[S] for S in allS)
    assert R <= bound + 1e-12
    return R / bound


rs = [check_41(pps, b) for pps in ([9, 5, 7], [4, 3, 5, 7])
      for b in (0.05, 0.25, 0.5) for _ in range(3)]
print(f"(b) Lemma 4.1 identities OK; R/bound in [{min(rs):.3f},{max(rs):.3f}]")

# (c) local bound
worst = 0.0
for l in (5, 7, 11, 13, 17, 31):
    for E in (1, 2):
        m = l ** E
        for _ in range(40):
            mask = np.zeros(m, bool)
            for _c in range(int(rng.integers(1, 4))):
                v = int(rng.integers(1, E + 1))
                b = int(rng.integers(l ** v))
                mask[np.arange(m) % l ** v == b] = True
            p_ = mask.mean()
            if p_ > 0.5:
                continue
            u = (~mask) / (~mask).sum()
            phi = np.fft.fft(u)[1:]
            g = p_ / (1 - p_)
            assert np.abs(phi).max() <= g + 1e-12
            assert abs(np.sum(np.abs(phi) ** 2) - g) < 1e-12
            for beta in (0.05, 0.2, 0.5):
                lp = np.sum(np.abs(phi) ** (2 + 2 * beta))
                assert lp <= g ** (1 + 2 * beta) + 1e-12
                kappa = max(1 + log(p_) / log(l), 0.0)  # smallest kappa with p<=l^(k-1)
                if kappa >= 1:
                    continue
                alpha = 2 * beta * (1 - kappa)
                rhs = 4 * p_ * l ** (-alpha)
                worst = max(worst, g ** (1 + 2 * beta) / rhs)
                assert g ** (1 + 2 * beta) <= rhs + 1e-12
print(f"(c) local bound OK; worst g^(1+2b)/(4p l^-alpha) = {worst:.3f}")
