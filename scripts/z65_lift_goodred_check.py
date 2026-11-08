#!/usr/bin/env python3
"""z65 LIFT — brute-force check of the arithmetic half of Theorem G (good-reduction classification).

For every prime p (default 5 <= p <= 600) and EVERY 3-term representation 4/p = 1/x + 1/y + 1/z
(x <= y <= z), test whether the multiset {x, y, z} of cone orders admits a 'cluster partition'
satisfying the necessary conditions derived in Z65_LIFT.md §3 (Lemmas G1–G3) for a curve with
G-action having potentially good reduction at p:
  * each cluster is attached to one branch point tau of X_k -> X_k/G with inertia I = P x| C_m;
  * a TAME cluster (P = 1) is a single cone point of order prime to p;
  * a WILD cluster (P != 1) has >= 2 cone points, all but at most one of which are pure powers p^b
    (b >= 1); (if m = 1 all are pure powers and there are >= 2 of them);
  * at least one cluster is wild (forced since p | lcm(x, y, z)).
Theorem G predicts: a partition exists iff p = 3m - 1 and {x, y, z} = {m, p, p m}.
Also records whether any representation has p^2 dividing a denominator (for the memo).

Usage: python3 scripts/z65_lift_goodred_check.py [PMAX]
"""
import sys
from fractions import Fraction


def primes_upto(n):
    s = bytearray([1]) * (n + 1)
    s[0:2] = b"\x00\x00"
    for i in range(2, int(n ** 0.5) + 1):
        if s[i]:
            s[i * i:: i] = bytearray(len(s[i * i:: i]))
    return [i for i in range(n + 1) if s[i]]


def reps(p):
    """All x <= y <= z with 4/p = 1/x + 1/y + 1/z."""
    out = []
    t = Fraction(4, p)
    x = p // 4 + 1
    while Fraction(3, x) >= t:
        r = t - Fraction(1, x)
        if r > 0:
            ylo = max(x, -(-r.denominator // r.numerator))  # ceil(1/r)
            y = ylo
            while Fraction(2, y) >= r:
                s = r - Fraction(1, y)
                if s > 0 and s.numerator == 1 and s.denominator >= y:
                    out.append((x, y, s.denominator))
                y += 1
        x += 1
    return out


def is_ppow(e, p):
    if e < p:
        return False
    while e % p == 0:
        e //= p
    return e == 1


def cluster_ok(triple, p):
    pts = list(triple)
    n = len(pts)
    # enumerate set partitions of 3 labelled points
    parts = [[[0], [1], [2]], [[0, 1], [2]], [[0, 2], [1]], [[1, 2], [0]], [[0, 1, 2]]]
    good = []
    for part in parts:
        ok = True
        nwild = 0
        for c in part:
            es = [pts[i] for i in c]
            if len(es) == 1:
                if es[0] % p == 0:
                    ok = False  # a single p-divisible cone point cannot be a whole cluster
                    break
            else:
                nonpure = [e for e in es if not is_ppow(e, p)]
                if len(nonpure) > 1:
                    ok = False
                    break
                nwild += 1
        if ok and nwild >= 1:
            good.append(part)
    return good


def main():
    pmax = int(sys.argv[1]) if len(sys.argv) > 1 else 600
    nrep = 0
    p2 = []
    survivors = []
    for p in primes_upto(pmax):
        if p < 5:
            continue
        for tr in reps(p):
            nrep += 1
            if any(e % (p * p) == 0 for e in tr):
                p2.append((p, tr))
            g = cluster_ok(tr, p)
            if g:
                survivors.append((p, tr, g))
    print(f"primes 5..{pmax}: {nrep} representations of 4/p checked")
    print(f"representations with p^2 | some denominator: {len(p2)}; first few: {p2[:5]}")
    print(f"triples admitting a good-reduction cluster partition: {len(survivors)}")
    bad = []
    for p, tr, g in survivors:
        m = (p + 1) // 3
        pred = (p % 3 == 2) and sorted(tr) == sorted((m, p, p * m))
        if not pred:
            bad.append((p, tr, g))
        print(f"  p={p} triple={tr} partitions={g} mordell={pred}")
    mord_primes = [p for p in primes_upto(pmax) if p >= 5 and p % 3 == 2]
    got = sorted(set(p for p, _, _ in survivors))
    print(f"primes p=2 mod 3 in range: {len(mord_primes)}; primes with a survivor: {len(got)}; equal: {got == mord_primes}")
    print(f"NON-MORDELL SURVIVORS (would kill Theorem G arithmetic): {len(bad)}")
    for b in bad[:20]:
        print("   ", b)


if __name__ == "__main__":
    main()
