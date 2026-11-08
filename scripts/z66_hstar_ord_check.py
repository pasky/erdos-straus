#!/usr/bin/env python3
"""z66 HSTAR — KT1: brute-force check of Lemma Ord (Z66_HSTAR.md §3).

Lemma Ord (claim): for a prime p >= 5, p = 1 (mod 4), every representation 4/p = 1/x + 1/y + 1/z
contains an entry x = p*k with k >= 2 and p not dividing k (Mordell's triple {m, p, p*m} included:
its entry p*m has k = m >= 2).  Hence every ES signature forces an element of order p*k, k >= 2,
in the group of any ES pair (X, G).  (The checkpoint-1 draft wrongly expected Mordell exceptions;
the script still reports them separately: there must be 0.)

For every prime 5 <= p <= PMAX with p = 1 (mod 4) we enumerate ALL representations (divisor method,
exact integers; enumerator reused from scripts/z65_lift_goodred_check.py) and record
  * reps without an entry p*k (k >= 2, p ∤ k)  -> must be none;
  * reps with p^2 | some entry                 -> must be none (Lemma P of Z65_LIFT).

Usage: python3 scripts/z66_hstar_ord_check.py [PMAX]
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from z65_lift_goodred_check import primes_upto, reps  # noqa: E402


def main():
    pmax = int(sys.argv[1]) if len(sys.argv) > 1 else 1500
    nrep = nprime = 0
    bad = []        # reps lacking a p*k entry that are not Mordell
    mordell = 0     # Mordell exceptions found
    psq = 0
    by_class = {1: 0, 5: 0}
    for p in primes_upto(pmax):
        if p < 5 or p % 4 != 1:
            continue
        nprime += 1
        for (x, y, z) in reps(p, 4):
            nrep += 1
            ent = (x, y, z)
            if any(e % (p * p) == 0 for e in ent):
                psq += 1
            has = any(e % p == 0 and (e // p) >= 2 and (e // p) % p != 0 for e in ent)
            if not has:
                m = (p + 1) // 3
                if (p + 1) % 3 == 0 and sorted(ent) == sorted((m, p, p * m)):
                    mordell += 1
                else:
                    bad.append((p, ent))
            else:
                by_class[p % 12] += 1
    print(f"primes p=1 (4), 5<=p<={pmax}: {nprime}; representations: {nrep}")
    print(f"reps with an entry p*k (k>=2, p∤k): p=1 (12): {by_class[1]}, p=5 (12): {by_class[5]}")
    print(f"reps WITHOUT such an entry that are Mordell triples (m,p,pm), 3m-1=p: {mordell}")
    print(f"reps WITHOUT such an entry, NOT Mordell (Lemma Ord counterexamples): {len(bad)}")
    for b in bad[:20]:
        print("   ", b)
    print(f"reps with p^2 | an entry: {psq}")
    ok = not bad and mordell == 0 and psq == 0
    print("KT1:", "PASSED" if ok else "FIRED")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
