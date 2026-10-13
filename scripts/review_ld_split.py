"""R177 from-scratch check of LDP_DEEP §A.4 EVIDENCE (split-supported Type II certificates).

Type II certificate of p in slice (c,d), M = 4cd: an unordered pair {f, f'} with f*f' = N = 1 + 4c^2 d p and
f = f' = -1 (mod M).  Each certificate is turned into an explicit ES solution and verified with Fractions:
a = (f+1)/M, b = (f'+1)/M, then 4/p = 1/(abd) + 1/(acdp) + 1/(bcdp).

Two notions of 'f is an F-norm' (F = Q(zeta_M)^+):
  S1 (author's 'split-supported'): every prime l | f has l = +-1 (mod M)            [sufficient]
  S2 (exact): f = N_{F/Q}(a) for an ideal a of O_F  <=>  for every l^v || f, the residue degree
      g_l = order of l in (Z/M)^x/{+-1} divides v                                      [necessary and sufficient]
Run: PYTHONPATH=scripts uv run python scripts/review_ld_split.py X C
"""
import sys
from fractions import Fraction
from math import gcd
from sympy import factorint, primerange

X = int(sys.argv[1]); C = int(sys.argv[2])


def ordpm(l, M):
    x, g = l % M, 1
    while x not in (1, M - 1):
        x = x * l % M; g += 1
    return g


def is_norm_S1(fac, M):
    return all(l % M in (1, M - 1) for l in fac)


def is_norm_S2(fac, M):
    return all(v % ordpm(l, M) == 0 for l, v in fac.items())


def divisors_from(fac):
    ds = [(1, {})]
    for l, v in fac.items():
        ds = [(d * l ** k, {**fd, **({l: k} if k else {})}) for d, fd in ds for k in range(v + 1)]
    return ds


def certs(p):
    out = []
    for cd in range(1, C + 1):
        for c in range(1, cd + 1):
            if cd % c: continue
            d = cd // c; M = 4 * cd; N = 1 + 4 * c * c * d * p
            fac = factorint(N)
            for f, ff in divisors_from(fac):
                fp = N // f
                if f > fp or (f + 1) % M or (fp + 1) % M: continue
                ffp = {l: v - ff.get(l, 0) for l, v in fac.items() if v - ff.get(l, 0)}
                a, b = (f + 1) // M, (fp + 1) // M
                assert Fraction(4, p) == Fraction(1, a * b * d) + Fraction(1, a * c * d * p) + Fraction(1, b * c * d * p)
                out.append((c, d, f, fp, is_norm_S1(ff, M), is_norm_S1(ffp, M), is_norm_S2(ff, M), is_norm_S2(ffp, M),
                            len(ff) == 1 and sum(ff.values()) == 1, len(ffp) == 1 and sum(ffp.values()) == 1))
    return out


ps = [p for p in primerange(5, X) if p % 24 == 1]
noA = []; noB1 = []; noB2 = []; noBb1 = 0; noBb2 = 0
tot = dict(A=0, B1=0, B2=0, prime=0)
for p in ps:
    cs = certs(p)
    if not cs: noA.append(p)
    b1 = [x for x in cs if x[4] or x[5]]; b2 = [x for x in cs if x[6] or x[7]]
    if not b1: noB1.append(p)
    if not b2: noB2.append(p)
    noBb1 += not any(x[4] and x[5] for x in cs); noBb2 += not any(x[6] and x[7] for x in cs)
    tot['A'] += len(cs); tot['B1'] += len(b1); tot['B2'] += len(b2); tot['prime'] += sum(1 for x in cs if x[8] or x[9])
print('primes p=1 (24) <', X, ':', len(ps), ' cd <=', C)
print('no Type II cert:', len(noA), noA[:20])
print('no cert with f or f\' in S1 (all l = +-1 mod M):', len(noB1), noB1[:20])
print('no cert with f or f\' in S2 (exact F-ideal norm):', len(noB2), noB2[:20])
print('no cert with both sides S1:', noBb1, ' both sides S2:', noBb2)
print('totals', tot, ' frac S1', round(tot['B1'] / tot['A'], 4), ' frac S2', round(tot['B2'] / tot['A'], 4),
      ' frac with f or f\' prime', round(tot['prime'] / tot['A'], 4))
# T1 control: odd squares
sq = 0
for m in range(3, int(4e4 ** 0.5) + 1, 2):
    n = m * m
    for cd in range(1, C + 1):
        for c in range(1, cd + 1):
            if cd % c: continue
            d = cd // c; M = 4 * cd; N = 1 + 4 * c * c * d * n
            sq += sum(1 for f, _ in divisors_from(factorint(N)) if (f + 1) % M == 0)
print('odd squares < 4e4: Type II divisor hits (cd <=', C, '):', sq)
