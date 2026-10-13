"""review_da_rgen.py (R178, from scratch): r-generic boxes of the seven ET Prop 1.9 families for general primes r,
checked against the box description used by DEPTH_ASPECT Thm 3.1 (MORDELL17 Lemmas 1.1, 2.1-2.3 with 17 -> r).

Brute force (truncated, parameters <= L): every class of ET Prop 1.9 (read off the statement, arXiv 1107.1010 p. 8)
that meets the r-generic line {x_q = 1 for q != r, x_r = u} gives a box (level k, residue mod r^k).
Predicted superset (from the theorem's proof), at level k:
  Q/Q^-1 : -y/z mod r^k for ordered solutions (x,y,z) of 4/r^k with r ∤ yz      (MORDELL17 Lemma 2.1 + 5.1(i))
  sqrtQ  : roots of n^2 = -y/z mod r^k                                           (MORDELL17 Lemma 1.1, empty by 1.3)
  U/U^-1 : -e, -1/e with e = x/y + x/z (when a unit)                              (MORDELL17 Lemma 2.2)
  P      : -f, -f* mod r^{ceil(K/2)} for N-points of Sigma^II_{r^K} (r ∤ cd), K <= 2k   (MORDELL17 Lemma 2.3)
Check: every brute-force box of level 1 <= k <= KMAX is contained in a predicted box of level <= k; no level-0 box.
usage: uv run --with sympy python scripts/review_da_rgen.py r L KMAX
"""
import sys
from math import gcd
from sympy import divisors

r, L, KMAX = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])


def vr(n):
    k = 0
    while n % r == 0:
        n //= r; k += 1
    return k


def rfree(n):
    while n % r == 0:
        n //= r
    return n


def inv(x, m):
    return pow(x % m, -1, m)


brute = set(); level0 = []


def add(k, res, tag):
    if k == 0:
        level0.append(tag)
    elif k <= KMAX:
        brute.add((k, res % r**k, tag[0]))


for a in range(1, L + 1):
    for d in range(1, L + 1):
        ad = a * d; kad = vr(ad); adp = rfree(ad)
        # I1: n = -f mod 4ad, f | 4a^2 d + 1;  r-generic: 4(ad)' | f+1; box -f mod (ad)_r
        if 1 <= kad <= KMAX:
            for f in divisors(4 * a * a * d + 1):
                if (f + 1) % (4 * adp) == 0:
                    add(kad, -f, ("I1", a, d, f))
        # II2: -4a^2 d mod f, 4ad | f+1; r-generic: f' | 4a^2 d + 1; box mod f_r
        # II3: -4a^2 d - e mod 4ade, (4ad, e) = 1; r-generic: 4(ad)' | e+1, e' | 4a^2 d + 1
        # I3 (with c := a): {n = -f mod 4cd} ∩ {n^2 = -4c^2 d mod f}, (4cd, f) = 1; 4(cd)' | f+1, f' | 4c^2 d+1
        for g in divisors(4 * a * a * d + 1):
            for k in range(0, KMAX + 1):
                f = g * r**k
                if (f + 1) % (4 * ad) == 0:                     # II2 (needs r ∤ ad automatically)
                    add(k, -4 * a * a * d, ("II2", a, d, f))
                if gcd(4 * ad, f) == 1 and (f + 1) % (4 * adp) == 0:
                    tag = ("II3", a, d, f)
                    lev = kad + k
                    if lev <= KMAX:
                        add(lev, -4 * a * a * d - f, tag)
                    # I3 with c = a
                    if kad > 0 and k == 0:
                        add(kad, -f, ("I3", a, d, f))
                    elif k > 0 and kad == 0:
                        m = r**k; t = (-4 * a * a * d) % m
                        for n in range(m):
                            if (n * n - t) % m == 0:
                                add(k, n, ("I3sq", a, d, f))
                    elif k == 0 and kad == 0:
                        add(0, 0, ("I3", a, d, f))

for a in range(1, L + 1):
    for b in range(1, L + 1):
        ab = a * b; kab = vr(ab); abp = rfree(ab)
        for e in divisors(a + b):
            # I4 / II1: e | a+b, (e, 4ab) = 1; r-generic: 4(ab)' | e+1 ; boxes -1/e, -e mod (ab)_r
            if gcd(e, 4 * ab) == 1 and (e + 1) % (4 * abp) == 0:
                if kab <= KMAX:
                    add(kab, -inv(e, r**max(kab, 1)), ("I4", a, b, e))
                    add(kab, -e, ("II1", a, b, e))
            # I2 (c := b): {n = -f mod 4ac} ∩ {n = -c/a mod f}, (4ac, f) = 1; r-generic: 4(ac)' | f+1, f' | a+c
            for k in range(0, KMAX + 1):
                f = e * r**k
                if gcd(4 * ab, f) == 1 and (f + 1) % (4 * abp) == 0:
                    if k == 0:
                        if kab <= KMAX:
                            add(kab, -f, ("I2", a, b, f))
                    elif kab == 0:
                        m = r**k
                        add(k, -b * inv(a, m), ("I2f", a, b, f))

# ---------------- predicted superset
import os
pred = set()


def sols(F):
    """ordered solutions of 4/F = 1/x + 1/y + 1/z (all orders)."""
    out = []
    for x in range(F // 4 + 1, 3 * F // 4 + 1):
        num, den = 4 * x - F, F * x               # 1/y + 1/z = num/den
        if num <= 0:
            continue
        for y in range(max(x, den // num + 1), 2 * den // num + 1):
            zn = num * y - den
            if zn > 0 and (den * y) % zn == 0:
                z = den * y // zn
                if z >= y:
                    for p in {(x, y, z), (x, z, y), (y, x, z), (y, z, x), (z, x, y), (z, y, x)}:
                        out.append(p)
    return set(out)


for k in (range(1, KMAX + 1) if not os.environ.get('SKIP_QU') else []):
    m = r**k
    for (x, y, z) in sols(m):
        if y % r and z % r:
            q = -y * inv(z, m) % m
            pred.add((k, q))
            for n in range(m):
                if (n * n - q) % m == 0:
                    pred.add((k, n))
        if y % r == 0 or z % r == 0:
            pass
        # U: e = x/y + x/z as an r-adic number
        num, den = x * (y + z), y * z
        while num % r == 0 and den % r == 0:
            num //= r; den //= r
        if den % r:
            e = num * inv(den, m) % m
            pred.add((k, -e % m))
            if e % r:
                pred.add((k, -inv(e, m) % m))

import os
for K in (range(1, 2 * KMAX + 1) if not os.environ.get('SKIP_P') else []):
    N = r**K; h = (K + 1) // 2; m = r**h
    a = 1
    while a * a <= N:
        for b in range(a, N // a + 1):
            e = (-N) % (4 * a * b)
            if e == 0 or (a + b) % e:
                continue
            c = (a + b) // e; d = (N + e) // (4 * a * b)
            assert 4 * a * b * c * d == a + b + N * c
            if (c * d) % r == 0:
                continue
            pred.add((h, -(4 * a * c * d - 1) % m)); pred.add((h, -(4 * b * c * d - 1) % m))
        a += 1


def covered(k, res):
    return any((kk, res % r**kk) in pred for kk in range(1, k + 1))


missing = [(k, res, t) for (k, res, t) in brute if not covered(k, res)]
nr = {u for u in range(1, r) if pow(u, (r - 1) // 2, r) == r - 1}
inc = sorted({(k, res) for (k, res, t) in brute if res % r in nr})
print("r=%d L=%d KMAX=%d: brute boxes %d (types %s), level-0 hits %d, NOT in predicted superset: %d %s" % (
    r, L, KMAX, len(brute), sorted({t for _, _, t in brute}), len(level0), len(missing), missing[:5]))
print("  brute boxes meeting non-residue cells:", len(inc), "predicted boxes:", len(pred))
