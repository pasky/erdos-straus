"""R223: from-scratch test of Lemma 1.3 / Cor 1.4 (Coppersmith-by-Minkowski class-divisor count).
For random (n, s, sigma, D0, D1) with n highly composite, compute the least J(w-1) over (m, k, J) for which (Cop)
holds EXACTLY (integer arithmetic, X_J = (D1-D0)/(2sJ) + 1/2 as a Fraction) and compare with the true number of
divisors E of n, D0 <= E <= D1, E ≡ sigma (mod s).  Also a deliberately adversarial family: n = product of many
numbers ≡ sigma (mod s) in the window (so the class is crowded), to probe tightness.
Usage: uv run python scripts/review_se2_cop.py [trials] [seed]"""
import sys, random, math
from fractions import Fraction as Fr
from itertools import combinations

def divisors(n):
    ds = [1]; m = n; p = 2
    while p * p <= m:
        if m % p == 0:
            e = 0
            while m % p == 0: m //= p; e += 1
            ds = [d * p ** i for d in ds for i in range(e + 1)]
        p += 1 if p == 2 else 2
    if m > 1: ds = [d * q for d in ds for q in (1, m)]
    return ds

def cop_holds(n, s, D0, D1, J, m, k):
    w = m + k
    X = Fr(D1 - D0, 2 * s * J) + Fr(1, 2)
    D0 = Fr(D0)
    ww = w * (w - 1) // 2
    lhs = w ** w * n ** (m * (m + 1) // 2) * X.numerator ** ww * D0.denominator ** (m * w)
    rhs = D0.numerator ** (m * w) * X.denominator ** ww
    return lhs < rhs

def best_bound(n, s, D0, D1, Wmax=14):
    best = (D1 - D0) // s + 1                       # trivial
    for w in range(2, Wmax + 1):
        for m in range(1, w + 1):
            k = w - m
            # smallest J with (Cop): (Cop) is monotone in J, binary search
            lo, hi = 1, max(1, (D1 - D0) // s + 1)
            if not cop_holds(n, s, D0, D1, hi, m, k): continue
            while lo < hi:
                mid = (lo + hi) // 2
                if cop_holds(n, s, D0, D1, mid, m, k): hi = mid
                else: lo = mid + 1
            best = min(best, lo * (w - 1))
    return best

def trial(rng, crowded):
    if crowded:
        s = rng.randint(2, 60); sigma = rng.choice([x for x in range(1, s + 1) if math.gcd(x, s) == 1])
        D0 = rng.randint(50, 3000); D1 = D0 + rng.randint(s, 40 * s)
        cands = [E for E in range(D0, D1 + 1) if E % s == sigma % s]
        rng.shuffle(cands); n = 1
        for E in cands[:rng.randint(2, 6)]: n = n * E // math.gcd(n, E)
    else:
        n = 1
        for _ in range(rng.randint(3, 9)): n *= rng.choice([2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37])
        s = rng.randint(2, 200); sigma = rng.randrange(s)
        while math.gcd(sigma, s) != 1: sigma = rng.randrange(s)
        D0 = rng.randint(1, max(2, int(n ** 0.6))); D1 = D0 + rng.randint(0, max(1, int(n ** 0.5)))
    true = sum(1 for E in divisors(n) if D0 <= E <= D1 and (E - sigma) % s == 0)
    return n, s, D0, D1, true, best_bound(n, s, D0, D1)

if __name__ == '__main__':
    T = int(sys.argv[1]) if len(sys.argv) > 1 else 300
    rng = random.Random(int(sys.argv[2]) if len(sys.argv) > 2 else 223)
    viol = tight = nontriv = 0
    for i in range(T):
        n, s, D0, D1, true, bd = trial(rng, crowded=(i % 2 == 1))
        if bd < (D1 - D0) // s + 1: nontriv += 1
        if true > bd: viol += 1; print("VIOLATION", n, s, D0, D1, true, bd)
        if true == bd: tight += 1
    print(f"{T} trials: violations {viol}, tight {tight}, Coppersmith beat trivial in {nontriv}")
