"""R172 from-scratch check of KUDLA_ES §2 (Props 2.2, 2.3, 2.4) and §3 item 3 (Q-part).

Slices (c,d) with cd <= CD, primes 5 <= p < P.  N = 1 + 4c^2 d p, T'_f = [[f,1],[1,N/f]] for f | N.
  ES = #{f | N : f = -1 mod 4cd},  G = #{f | N : Diff(T'_f) subset Odd(p) = {p}}  (Diff via Gram route, own Hilbert).
  Prop 2.2(c) formula checked against the Gram route for every f.
  Q = #{f | N : -f in (Z/M)^x2} / |(Z/M)^x2|, M = 4cd;  compare Q with tau(N)/phi(M) and tau(N) 2^omega(M)/phi(M).
  Prop 2.3 construction checked for every p.
  Prop 2.4: GL2(Z)-classes (Gauss reduction) of the forms [f, 2, N/f]: do classes mix certificate and non-certificate f?
Run: PYTHONPATH=scripts uv run --with sympy python scripts/review_kud_genus.py 3000 12
"""
import sys
from math import gcd, isqrt
from collections import Counter, defaultdict
from sympy import divisors, primerange, totient, factorint
from review_kud_tuples import diff_from_gram, hil, leg

P = int(sys.argv[1]) if len(sys.argv) > 1 else 3000
CD = int(sys.argv[2]) if len(sys.argv) > 2 else 12


def reduce_form(a, b, c):
    """Gauss reduction of positive definite ax^2+bxy+cy^2 to the unique reduced rep (proper SL2(Z) class)."""
    while True:
        if c < a:
            a, b, c = c, -b, a
        if b > a or b <= -a:
            k = (a - b) // (2 * a)
            # replace b by b + 2ka in (-a, a]
            b2 = b + 2 * k * a
            c = (b2 * b2 - (b * b - 4 * a * c)) // (4 * a)
            b = b2
            continue
        if a == c and b < 0:
            b = -b
        return (a, b, c)


def gl2_class(a, b, c):
    r1, r2 = reduce_form(a, b, c), reduce_form(a, -b, c)
    return min(r1, r2)


def genus_symbol(f, D):
    """Cox Thm 3.15 assigned characters of a primitive form of disc D = -4m representing f, gcd(f, 2D) = 1."""
    m = -D // 4
    sym = [leg(f, l) for l in sorted(factorint(m)) if l != 2]
    dl = 1 if f % 4 == 1 else -1
    ep = 1 if f % 8 in (1, 7) else -1
    r = m % 8
    if r in (1, 5, 4):
        sym.append(dl)
    elif r == 2:
        sym.append(dl * ep)
    elif r == 6:
        sym.append(ep)
    elif r == 0:
        sym += [dl, ep]
    return tuple(sym)


def formula_22c(f, d, n):
    X = 4 * d * n
    out = {l for l, k in factorint(d * n).items() if l != 2 and k % 2 == 1 and leg(-f, l) == -1}
    if hil(-f, -f * X, 2) == -1:
        out.add(2)
    return frozenset(out)


slices = [(c, d) for c in range(1, CD + 1) for d in range(1, CD + 1) if c * d <= CD]
S = Counter()
ratio1, ratio2 = [], []
for p in primerange(5, P):
    # Prop 2.3
    if p % 4 == 3:
        c, f = 1, 1
    else:
        q = next(q for q in primerange(3, 10**6) if q % 4 == 3 and leg(q, p) == -1)
        c = next(c for c in range(1, q) if (1 + 4 * c * c * p) % q == 0)
        f = q
    N = 1 + 4 * c * c * p
    S['2.3 ok'] += (N % f == 0 and diff_from_gram(f, 2, N // f) == {p})
    for (c, d) in slices:
        N, M = 1 + 4 * c * c * d * p, 4 * c * d
        sqM = {x * x % M for x in range(M) if gcd(x, M) == 1}
        es = g = qn = 0
        cls = defaultdict(set)
        fcls = defaultdict(set)
        gen = defaultdict(set)
        for f in divisors(N):
            Df = diff_from_gram(f, 2, N // f)
            S['2.2c formula ok'] += (Df == formula_22c(f, d, p))
            S['2.2c checked'] += 1
            cert = (f % M == M - 1)
            es += cert
            g += (Df <= {p})
            qn += ((-f) % M in sqM)
            K = gl2_class(f, 2, N // f)
            cls[K].add(cert)
            fcls[K].add(min(f, N // f))
            gen[genus_symbol(f, 4 - 4 * N)].add(cert)
        S['ES'] += es
        S['G'] += g
        S['viol ES>G'] += (es > g)
        S['slices ES>0'] += (es > 0)
        S['slices G>0'] += (g > 0)
        S['slices'] += 1
        S['viol Q-count>G'] += (qn > g)
        S['classes mixed cert/noncert'] += sum(1 for v in cls.values() if len(v) == 2)
        S['classes with a cert'] += sum(1 for v in cls.values() if True in v)
        S['classes with >1 swap-pair {f,N/f}'] += sum(1 for v in fcls.values() if len(v) > 1)
        S['genera mixed cert/noncert'] += sum(1 for v in gen.values() if len(v) == 2)
        S['genera with a cert'] += sum(1 for v in gen.values() if True in v)
        t, ph = len(divisors(N)), int(totient(M))
        om = len(factorint(M))
        ratio1.append((qn / len(sqM), t / ph))
        ratio2.append((qn / len(sqM), t * 2 ** om / ph))
for k, v in S.items():
    print(k, v)
sQ = sum(x for x, _ in ratio1)
print('sum Q =', round(sQ, 1), ' sum tau/phi =', round(sum(y for _, y in ratio1), 1),
      ' sum tau 2^omega/phi =', round(sum(y for _, y in ratio2), 1))
# odd squares
sq = Counter()
for m in range(3, isqrt(20 * P) + 1, 2):
    n = m * m
    for (c, d) in slices:
        N, M = 1 + 4 * c * c * d * n, 4 * c * d
        for f in divisors(N):
            sq['ES'] += (f % M == M - 1)
            Df = diff_from_gram(f, 2, N // f)
            sq['G'] += (Df <= {l for l, k in factorint(n).items() if k % 2})
print('odd squares m^2 <=', 20 * P, dict(sq))
