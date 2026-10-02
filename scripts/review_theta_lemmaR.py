"""Numeric sanity check of the reviewer's Lemma R (coefficient budget => level).

Take a small prime-slice CRT system, expand an even-degree Bonferroni majorant
Q_r(H) = sum_{j<=r} (-1)^j sum_{|B|=j} 1[n in all classes of B] into class
indicators (one term per compatible set of atoms), apply the coarsening of
Lemma R at level lam, and verify:  nu' >= nu pointwise, nu' >= 1 on the avoider
set, level(nu') <= lam, E nu' <= E nu + T e^{Lambda0 - lam}.

Run: PYTHONPATH=scripts uv run python scripts/review_theta_lemmaR.py
"""
import itertools
import math
import random

import numpy as np

Q0 = 4
P = [5, 7, 11, 13, 17]
QT = Q0 * math.prod(P)
n = np.arange(QT)


def run(seed, r, lam):
    rng = random.Random(seed)
    atoms = []  # (q0, a mod q0, l, b mod l)
    for l in P:
        for _ in range(rng.randint(1, max(1, l // 4))):
            q = rng.choice([1, 2, 4])
            atoms.append((q, rng.randrange(q), l, rng.randrange(l)))
    ind = [((n % q) == a) & ((n % l) == b) for (q, a, l, b) in atoms]
    H = np.sum(ind, axis=0)
    avoid = H == 0
    terms = []  # (coef, modulus-dict {prime_or_Q0: residue})
    for j in range(r + 1):
        for B in itertools.combinations(range(len(atoms)), j):
            # CRT-intersect; skip incompatible
            mask = np.ones(QT, bool)
            for i in B:
                mask &= ind[i]
            if not mask.any():
                continue
            primes = sorted(set(atoms[i][2] for i in B))
            terms.append(((-1) ** j, mask, primes, B))
    nu = sum(c * m for c, m, _, _ in terms)
    assert (nu >= 0).all() and (nu[avoid] >= 1).all()
    T = sum(abs(c) for c, _, _, _ in terms)
    Lam0 = math.log(max(P))
    nu2 = np.zeros(QT)
    for c, mask, primes, B in terms:
        lev = sum(math.log(l) for l in primes)
        if lev <= lam + 1e-12:
            nu2 += c * mask
            continue
        if c < 0:
            continue  # drop
        keep, s = [], 0.0
        for l in primes:  # ascending
            if s + math.log(l) <= lam + 1e-12:
                keep.append(l); s += math.log(l)
            else:
                break
        # coarsened class: same residues mod Q0-part and kept primes
        rep = int(np.argmax(mask))
        q0 = math.lcm(1, *[atoms[i][0] for i in B])  # small part of the term's modulus
        cm = (n % q0) == (rep % q0)
        for l in keep:
            cm &= (n % l) == (rep % l)
        assert (cm >= mask).all()  # genuine coarsening
        nu2 += c * cm
    ok = (nu2 >= nu - 1e-9).all() and (nu2[avoid] >= 1 - 1e-9).all()
    bound = nu.mean() + T * math.exp(Lam0 - lam)
    print(f"seed={seed} r={r} lam=log{math.exp(lam):.0f}: #terms={len(terms)} T={T} "
          f"E nu={nu.mean():.4f} E nu'={nu2.mean():.4f} bound={bound:.3g} "
          f"{'ok' if ok and nu2.mean() <= bound + 1e-12 else 'FAIL'}")
    assert ok and nu2.mean() <= bound + 1e-12


if __name__ == "__main__":
    for seed in range(4):
        for r in [2, 4]:
            for lam in [math.log(17), math.log(77), math.log(221)]:
                run(seed, r, lam)
