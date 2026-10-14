"""review_fs2_brute.py (R218, from scratch): brute-force enumeration of Case B tuples (B) of FF_STERILE_PUSH
directly from the definition
    m'wC = T^s + v,  w + C = g'v,  T || w, T || C, T not| m'g',  v != 0,  m', g', w, C monic
over F_p (p = 3, 5, 7), all degree splits, and checks
  * Lemma 1.1: y + t = max(a, b); E v = T^s + m'w^2; E'v = T^s + m'C^2; T^2 || v ... (v1(0) != 0), gcd(w1, T v1) = 1;
  * Lemma 1.6: per pattern (s; a, z, y, t) with a <= b, exact count <= min over routes (review_fs2_bounds.py),
    and each individual route bound (reports the tightest ratio count/route for every route).
usage: uv run --with python-flint python scripts/review_fs2_brute.py p SMAX"""
import sys
from itertools import product
from collections import Counter, defaultdict
import flint
sys.path.insert(0, 'scripts')
from review_fs2_bounds import make

p, SMAX = int(sys.argv[1]), int(sys.argv[2])
P = lambda c: flint.nmod_poly(c, p)
T = P([0, 1])


def monic(d, cond):
    """monic polys of degree d (coeff list low->high) with condition on the constant/linear coeffs."""
    for low in product(range(p), repeat=d):
        c = list(low) + [1]
        if cond(c):
            yield P(c)


notT = lambda c: c[0] != 0                 # T does not divide
Tex = lambda c: c[0] == 0 and c[1] != 0    # T exactly divides (needs degree >= 1)
B = make(p)
viol = 0
allcnt = Counter()
from fractions import Fraction
for s in range(3, SMAX + 1):
    Ts = T**s
    cnt = Counter()
    for a in range(1, s):
        for b in range(1, s - a + 1):
            z = s - a - b
            Ms = list(monic(z, notT)) if z > 0 else [P([1])]
            Ws = list(monic(a, Tex)) if a >= 1 else []
            Cs = list(monic(b, Tex)) if b >= 1 else []
            for m in Ms:
                for w in Ws:
                    mw = m * w
                    for C in Cs:
                        v = mw * C - Ts
                        if v == 0:
                            continue
                        g, rem = divmod(w + C, v)
                        if rem != 0 or g.degree() < 0 or int(g.coeffs()[-1]) != 1 or int(g.coeffs()[0]) == 0:
                            continue
                        y, t = g.degree(), v.degree()
                        # Lemma 1.1 checks
                        assert y + t == max(a, b), (s, a, b, y, t)
                        L = g * m
                        E, Ep = L * w - 1, L * C - 1
                        assert E * v == Ts + m * w * w and Ep * v == Ts + m * C * C
                        vc = v.coeffs()
                        assert int(vc[0]) == 0 and int(vc[1]) == 0 and int(vc[2]) != 0
                        v1 = P(vc[2:]); w1 = P(w.coeffs()[1:])
                        assert (T * v1).gcd(w1).degree() == 0
                        allcnt[s] += 1
                        if a <= b:
                            cnt[(a, z, y, t)] += 1
    # compare with route bounds
    worst = 0.0
    for (a, z, y, t), c in cnt.items():
        e = B['routes'](s, a, z, y, t)
        mn = min(e.values())
        if c > mn:
            viol += 1
            print("VIOLATION", p, s, (a, z, y, t), c, mn, e)
        worst = max(worst, c / mn)
    # also patterns with no tuples are fine; check enumeration of patterns covers all observed
    pats = set(B['patterns'](s))
    assert set(cnt) <= pats, set(cnt) - pats
    tot = sum(cnt.values())
    print(f"p={p} s={s}: tuples(a<=b)={tot} patterns_hit={len(cnt)} max count/minbound={worst:.3f}", flush=True)
print("violations:", viol)
print("all tuples per s:", dict(allcnt))
print("census sum_s count(s) p^(1-ceil(s/2)) =", sum(Fraction(c, p**((s + 1) // 2 - 1)) for s, c in allcnt.items()))
