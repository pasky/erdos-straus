"""LS5 toy checks (EVIDENCE only).

[1] Lemma 1.2 labels: for every R(M) class -4D mod M (D | A^2, A=(M+1)/4) the
    label -4D (D<=A) or -1/(4D') (D'=A^2/D<A) represents the class, and
    distinct labels congruent mod g have height product >= g/2.
[2] Covering probabilities in the product model for the FULL R(M) family
    over a pool of primes (all moduli M | P, M = 3 mod 4): exact
    P(E_S) for every S (|S| <= 4) versus the independence prediction
    prod_{l in S} P(l covered).  Ratio >> 1 would signal harmful
    correlations (failure of (CC)-type product decay).
"""
import itertools, math, sys
import numpy as np

POOL = [7, 11, 19, 23, 31, 43]  # P = 44,4 million points, exact enumeration


def divisors(n):
    ds = [1]
    m, p = n, 2
    while p * p <= m:
        if m % p == 0:
            e = 0
            while m % p == 0:
                m //= p; e += 1
            ds = [d * p ** k for d in ds for k in range(e + 1)]
        p += 1
    if m > 1:
        ds = [d * k for d in ds for k in (1, m)]
    return ds


def classes(M):
    A = (M + 1) // 4
    out = {}
    for D in divisors(A * A):
        b = (-4 * D) % M
        Dp = A * A // D
        if D <= A:
            lab = (4 * D, 1)        # -r/s with r=4D, s=1
        else:
            lab = (1, 4 * Dp)       # -1/(4D')
        r, s = lab
        assert (-(r * pow(s, -1, M))) % M == b, (M, D)
        out[b] = lab
    return out


def check_labels():
    worst = math.inf
    allc = []
    for k in range(1, len(POOL) + 1):
        for Q in itertools.combinations(POOL, k):
            M = math.prod(Q)
            if M % 4 != 3:
                continue
            for b, lab in classes(M).items():
                allc.append((M, b, lab))
    # compatibility: distinct labels, g = gcd of moduli, congruent mod g
    n = 0
    for (M1, b1, l1), (M2, b2, l2) in itertools.combinations(allc, 2):
        if l1 == l2:
            continue
        g = math.gcd(M1, M2)
        if g == 1 or b1 % g != b2 % g:
            continue
        H1, H2 = max(l1), max(l2)
        n += 1
        worst = min(worst, H1 * H2 / (g / 2))
    print(f"[1] {len(allc)} classes; labels verified; {n} congruent distinct-label "
          f"pairs; min H1*H2/(g/2) = {worst:.3f} (Lemma 1.2 needs >= 1)")
    assert worst >= 1


def cover_probs():
    P = math.prod(POOL)
    y = None
    cov = {l: np.zeros(P, dtype=bool) for l in POOL}
    ncl = 0
    for k in range(1, len(POOL) + 1):
        for Q in itertools.combinations(POOL, k):
            M = math.prod(Q)
            if M % 4 != 3:
                continue
            for b in classes(M):
                ncl += 1
                idx = np.arange(b, P, M)
                for l in Q:
                    cov[l][idx] = True
    print(f"[2] pool {POOL}, {ncl} classes, P = {P}")
    single = {l: cov[l].mean() for l in POOL}
    for l in POOL:
        print(f"    P(cov {l}) = {single[l]:.4f}   (l*P = {l*single[l]:.2f})")
    worst = 0
    for k in range(2, 5):
        for S in itertools.combinations(POOL, k):
            m = np.ones(P, dtype=bool)
            for l in S:
                m &= cov[l]
            pe = m.mean()
            ind = math.prod(single[l] for l in S)
            r = pe / ind
            worst = max(worst, r)
            print(f"    S={S}: P(E_S)={pe:.3e}  indep={ind:.3e}  ratio={r:.2f}")
    print(f"    max ratio P(E_S)/prod P(cov l) = {worst:.2f}")


if __name__ == "__main__":
    check_labels()
    cover_probs()
