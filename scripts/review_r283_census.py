"""R283 from-scratch recheck of O272 §5 census (2-group levels).
Word at level t: n = t u v - u - v, u, v >= 2  <=>  (tu-1) | n + u with (n+u)/(tu-1) >= 2   (Lemma 1.1 form).
Sieve by residue classes (slicing), NOT the author's enumeration; then independent divisor-based spot check
(d | tn+1, d = -1 mod t, d = tu-1, cofactor tv-1, u, v >= 2) on random subsets.
"""
import sys, random
import numpy as np
from sympy import primerange, divisors, isprime

F = [3, 5, 17, 257, 65537]


def T2(X):
    odds = [1]
    for f in F:
        odds += [o * f for o in odds]
    out = sorted({(1 << k) * o for o in odds for k in range(2, 40) if (1 << k) * o <= X + 2})
    return out


def sieve(levels, X):
    hit = np.zeros(X + 1, dtype=bool)
    for t in levels:
        u = 2
        while True:
            d = t * u - 1
            start = 2 * d - u  # smallest n with v = 2
            if start > X:
                break
            hit[start::d] = True
            u += 1
    return hit


def word_by_divisors(n, t):
    N = t * n + 1
    for d in divisors(N):
        if d % t == t - 1:
            e = N // d
            if e % t == t - 1 and d >= 2 * t - 1 and e >= 2 * t - 1:
                return True
    return False


def main(X, spot=150, baseline=False):
    L = T2(X)
    print(f"X={X}: |T2 levels <= X+2| = {len(L)}")
    h = sieve(L, X)
    P = np.array(list(primerange(5, X + 1)))
    fails = P[~h[P]]
    print(f"primes 5<=p<=X with no T2 word: {len(fails)} of {len(P)}; largest {fails[-3:].tolist()}")
    lo = 100
    while lo < X:
        hi = 10 * lo
        sel = (P > lo) & (P <= hi)
        print(f"  ({lo},{hi}]: {int((~h[P[sel]]).sum())}/{int(sel.sum())} = {(~h[P[sel]]).mean():.4f}")
        lo = hi
    odd = np.arange(3, X + 1, 2)
    m = np.arange(1, int(X ** 0.5) + 2, 2); sq = m * m; sq = sq[sq <= X]
    issq = np.zeros(X + 1, bool); issq[sq] = True
    nf = int(((~h[odd]) & (~issq[odd])).sum())
    print(f"odd non-squares 3<=n<=X with no T2 word: {nf}; odd squares with a T2 word: {int(h[sq].sum())}")
    # independent spot check
    random.seed(283)
    sf = random.sample(fails.tolist(), min(spot, len(fails)))
    hp = P[h[P]].tolist(); sh = random.sample(hp, spot)
    bad1 = [p for p in sf if any(word_by_divisors(p, t) for t in L if 4 * t - 4 <= p)]
    bad2 = [p for p in sh if not any(word_by_divisors(p, t) for t in L if 4 * t - 4 <= p)]
    print(f"divisor spot check: {len(sf)} failing primes, {len(bad1)} actually have a word; "
          f"{len(sh)} hit primes, {len(bad2)} actually have none")
    if baseline:
        hb = sieve(range(4, X + 3, 4), X)
        print(f"baseline all 4|t: primes failing {int((~hb[P]).sum())}; odd non-squares failing "
              f"{int(((~hb[odd]) & (~issq[odd])).sum())}; squares hit {int(hb[sq].sum())}; "
              f"T2-failing primes with some 4|t word: {int(hb[fails].sum())}")
        h8 = sieve(range(8, X + 3, 8), X)
        print(f"n=131: 8|t word {bool(h8[131])}, 4|t word {bool(hb[131])}; n=241: 8|t {bool(h8[241])}, 4|t {bool(hb[241])}")


if __name__ == "__main__":
    X = int(sys.argv[1]); main(X, baseline=(len(sys.argv) > 2))
