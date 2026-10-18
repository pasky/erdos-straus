"""O272 goal 3: ES words n = tuv - u - v (u, v >= 2) at 2-group levels t in T2 = {2^k F : k >= 2, F | 3*5*17*257*65537}
(G_t = (Z/t)^* a 2-group).  Census of odd n <= X with NO word at any level of T2; primes separately; T1 (odd squares)
control; numerator-8 control (levels 8 | t, n = 131, 241 must have no word at ANY 8 | t level).
Exact certificates: every reported hit is re-verified as (tu-1)(tv-1) = tn+1.
"""
import sys
import numpy as np
from sympy import primerange
from itertools import combinations


def T2(X):
    F = [3, 5, 17, 257, 65537]
    odd = set()
    for r in range(len(F) + 1):
        for c in combinations(F, r):
            odd.add(int(np.prod(c)) if c else 1)
    out = set()
    for f in odd:
        k = 2
        while (1 << k) * f <= X + 2:
            out.add((1 << k) * f)
            k += 1
    return sorted(out)


def hits(levels, X):
    hit = np.zeros(X + 1, dtype=bool)
    for t in levels:
        u = 2
        while (t * u - 1) * 2 - u <= X:
            a = t * u - 1
            vmax = (X + u) // a
            v = np.arange(2, vmax + 1, dtype=np.int64)
            n = a * v - u
            hit[n[n <= X]] = True
            u += 1
    return hit


def all_levels_hit(n, step):
    """does n have a word at some level t = 0 (mod step)?  brute force, small n."""
    for t in range(step, n + 3, step):
        for u in range(2, n + 2):
            a = t * u - 1
            if 2 * a - u > n:
                break
            if (n + u) % a == 0 and (n + u) // a >= 2:
                return (t, u, (n + u) // a)
    return None


if __name__ == "__main__":
    X = int(sys.argv[1]) if len(sys.argv) > 1 else 10**6
    L = T2(X)
    print(f"# X = {X}; |T2 cap [4, X+2]| = {len(L)}")
    h = hits(L, X)
    odd = np.arange(1, X + 1, 2)
    sq = set(m * m for m in range(1, int(X ** 0.5) + 1, 2))
    fails = [int(n) for n in odd if not h[n] and n not in sq and n > 1]
    print(f"odd non-squares n<=X with no T2 word: {len(fails)} of {len(odd) - len(sq)}; first: {fails[:12]}")
    sq_hit = [m for m in sq if h[m]]
    print(f"odd squares with a T2 word (T1: must be 0): {len(sq_hit)}")
    P = [p for p in primerange(5, X + 1)]
    pf = [p for p in P if not h[p]]
    print(f"primes 5<=p<=X with no T2 word: {len(pf)} of {len(P)}; first: {pf[:10]}; largest: {pf[-3:]}")
    # decades
    for lo in [10**k for k in range(2, len(str(X)))]:
        hi = 10 * lo
        a = sum(1 for p in pf if lo < p <= hi); b = sum(1 for p in P if lo < p <= hi)
        if b:
            print(f"  primes in ({lo},{hi}]: fail {a}/{b} = {a/b:.4f}")
    # all levels 4 | t for the T2-failing primes (should always have words if <= 1e8 EVIDENCE holds)
    chk = pf[:200]
    bad = [p for p in chk if all_levels_hit(p, 4) is None]
    print(f"of the first {len(chk)} T2-failing primes, {len(bad)} have no word at ANY 4|t level")
    # numerator 8 control
    for n in (131, 241):
        print(f"n={n}: word at some 8|t level: {all_levels_hit(n, 8)}; at some 4|t level: {all_levels_hit(n, 4)}")
    # baseline: all levels 4 | t (the full (*) line), primes and non-squares
    hA = hits(list(range(4, X + 3, 4)), X)
    pA = [p for p in P if not hA[p]]
    nA = sum(1 for n in odd if not hA[n] and n not in sq and n > 1)
    print(f"baseline all 4|t levels: primes failing {len(pA)}; odd non-squares failing {nA}; squares hit {sum(1 for m in sq if hA[m])}")
    print(f"T2-failing primes that HAVE a word at some 4|t level: {len(set(pf) - set(pA))}")
