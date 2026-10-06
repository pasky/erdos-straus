"""R68b from-scratch check of POINTWISE_OMEGA17 Lemma 5.2 (capped planting), exact rationals.

Builds nu = mu + P0 * sum_{|J|=k+1} w_J sigma_J by explicit summation over J (O14 Lemma 1.1),
checks: nu(0)=0, all <=k marginals equal, nu>=0, and max_{y!=0}|dnu/dmu-1| <= s-1 whenever
R >= k r* + (k+1)/(s-1), 1<s<=2.  Uses the tightest s := 1+(k+1)/(R-k r*) (when <=2).
Also reports how tight the bound is (observed max dev vs s-1).
"""
import itertools, random
from fractions import Fraction as Fr


def check(r, k):
    n = len(r)
    P0 = Fr(1)
    for ri in r:
        P0 /= (1 + ri)  # p=r/(1+r), 1-p = 1/(1+r)
    mu = {}
    for bits in itertools.product((0, 1), repeat=n):
        v = P0
        for b, ri in zip(bits, r):
            if b:
                v *= ri
        mu[bits] = v
    Js = list(itertools.combinations(range(n), k + 1))
    wraw = {}
    for J in Js:
        w = Fr(1)
        for i in J:
            w *= r[i]
        wraw[J] = w
    ek1 = sum(wraw.values())
    if ek1 == 0:
        return None
    nu = dict(mu)
    for J in Js:
        wJ = wraw[J] / ek1
        for sz in range(k + 2):
            for y in itertools.combinations(J, sz):
                bits = tuple(1 if i in y else 0 for i in range(n))
                nu[bits] += P0 * wJ * (-1) ** (sz + 1)
    assert nu[(0,) * n] == 0
    assert all(v >= 0 for v in nu.values()), "negative"
    for K in itertools.chain.from_iterable(itertools.combinations(range(n), a) for a in range(k + 1)):
        for pat in itertools.product((0, 1), repeat=len(K)):
            a = sum(v for b, v in mu.items() if all(b[i] == p for i, p in zip(K, pat)))
            c = sum(v for b, v in nu.items() if all(b[i] == p for i, p in zip(K, pat)))
            assert a == c, (K, pat)
    dev = max(abs(nu[b] / mu[b] - 1) for b in mu if any(b))
    return dev


random.seed(68)
tot = 0
worst = Fr(0)
for trial in range(400):
    n = random.randint(3, 8)
    k = random.randint(0, min(3, n - 1))
    r = [Fr(random.randint(1, 40), random.randint(1, 40)) for _ in range(n)]
    R, rs = sum(r), max(r)
    if R - k * rs <= 0:
        continue
    s = 1 + Fr(k + 1) / (R - k * rs)
    if s > 2:
        continue
    dev = check(r, k)
    tot += 1
    assert dev <= s - 1, (r, k, dev, s)
    worst = max(worst, dev / (s - 1))
print("instances satisfying hypothesis:", tot, " max dev/(s-1):", float(worst))
# boundary: equal odds, R exactly k r* + (k+1)/(s-1) with s=2
for n, k in [(4, 1), (5, 2), (6, 2), (7, 3), (8, 3)]:
    # r_i = c, R = n c = k c + k + 1  -> c = (k+1)/(n-k)
    c = Fr(k + 1, n - k)
    dev = check([c] * n, k)
    print(f"equal odds n={n} k={k} c={c}: s-1=1, max dev={dev} ({float(dev):.4f})")
