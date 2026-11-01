# z52d_thinfamily_binom.py — exact limit test for the two "irreducible-x" moving-gap menus A and A' of Z52D_THINFAMILY.md
# at the unit-square point mu = 0 of n = c0*2^s + 1 (c0 = 4^J - 1), root degree D, Y = 2^{s/D}, n = c0 Y^D + 1.
#
#   B := n + c = f f'  (c > 0 constant, f, f' non-constant, positive leading coefficients),  f = 4x - n (the gap)
#   menu A : x = (n+f)/4, y = n(1+f')/4,  z = n x (1+f')/c      (generalises II-ad / (BI): c = 4a^2 d)
#   menu A': x = (n+f)/4, y = x f',       z = n x f'/c          (generalises I-ac)
# Capelli: B = c0 (Y^D + u^p), u^p = (1+c)/c0, p | D odd prime (4 | D, -4w^4 impossible: u^p > 0).
# A family is valid near mu = 0 iff x, y, z take Z[1/2]-values at Y = 1 and Z_(2)-values at Y = 0
# (MENU_LADDER Lemma 2.1); positivity is automatic (B has no root in [0, oo), kappa > 0).
# f = kappa*P, P a monic product of a proper non-empty subset of the irreducible factors of Y^D + u^p.
# 2-adic: x(0) in Z_(2) forces phi0 := f(0) to be a 2-adic unit with phi0 = 3 mod 4, so v2(X) = v2(P(1)) - v2(P(0)),
# X := f(1); its odd part runs over the odd divisors of N := B(1) = c0 (1 + u^p).
# u = r / 2^i allowed (i <= IMAX); for menu A such u are impossible (proof in memo) but are tested anyway.
# Usage: z52d_thinfamily_binom.py c0 PMAX UMAX3 DMULT IMAX   (u-range for prime p: UMAX3^(3/p); D = p*t, t | DMULT-list)
import sys, itertools
from fractions import Fraction as Fr
import cypari2
pari = cypari2.Pari(); pari.allocatemem(2 * 10**9)
c0 = int(sys.argv[1]); PMAX = int(sys.argv[2]); U3 = int(sys.argv[3])
TL = [int(t) for t in sys.argv[4].split(',')]; IMAX = int(sys.argv[5]) if len(sys.argv) > 5 else 0
J = (c0 + 1).bit_length() // 2; assert 4 ** J == c0 + 1; FJ = 4 ** J

def v2(x):
    x = Fr(x)
    if x == 0: return 10 ** 9
    n, d, v = x.numerator, x.denominator, 0
    while n % 2 == 0: n //= 2; v += 1
    while d % 2 == 0: d //= 2; v -= 1
    return v
def in1(x):
    d = Fr(x).denominator
    while d % 2 == 0: d //= 2
    return d == 1
def in0(x): return Fr(x).denominator % 2 == 1                                          # Z_(2)
def odd(n):
    n = abs(n)
    while n and n % 2 == 0: n //= 2
    return n

def primes_upto(m):
    s = bytearray([1]) * (m + 1); s[0:2] = b'\x00\x00'
    for i in range(2, int(m ** 0.5) + 1):
        if s[i]: s[i * i::i] = bytearray(len(s[i * i::i]))
    return [i for i in range(m + 1) if s[i]]

hits, ntest = [], 0
factcache = {}
def factors(D, u):          # monic irreducible factors over Q of Y^D + u^p, as lists of Fraction coefficients
    key = (D, u)
    if key in factcache: return factcache[key]
    F = pari('factor(Y^%d + (%s)^%d)' % (D, str(u), p))
    out = []
    for i in range(len(F[0])):
        pol = F[0][i]; mult = int(F[1][i])
        co = [Fr(str(pol.polcoef(j))) for j in range(int(pol.poldegree()) + 1)]
        lc = co[-1]; co = [x / lc for x in co]
        out += [co] * mult
    factcache[key] = out
    return out
def ev(co, y): return sum(cf * y ** j for j, cf in enumerate(co))

for p in [q for q in primes_upto(PMAX) if q >= 3]:
    UM = max(3, int(round(U3 ** (3.0 / p))))
    for i in range(IMAX + 1):
        for r in range(1, UM + 1):
            if i and r % 2 == 0: continue
            u = Fr(r, 2 ** i)
            c = c0 * u ** p - 1
            if c <= 0: continue
            N = FJ + c                                   # = c0 (1 + u^p) = B(1)
            No = odd(N.numerator)
            # odd divisors of N via PARI
            divs = [int(t) for t in pari.divisors(No)]
            for t in TL:
                D = p * t
                fs = factors(D, u)
                if len(fs) < 2: continue
                idx = range(len(fs)); seen = set()
                for k in range(1, len(fs)):
                    for S in itertools.combinations(idx, k):
                        key = tuple(sorted(tuple(fs[j]) for j in S))
                        if key in seen: continue
                        seen.add(key)
                        P1 = Fr(1); P0 = Fr(1)
                        for j in S: P1 *= ev(fs[j], 1); P0 *= ev(fs[j], 0)
                        e = v2(P1) - v2(P0)
                        for w in divs:
                            X = Fr(w) * Fr(2) ** e
                            Xp = N / X
                            ntest += 1
                            phi0 = X * P0 / P1; phi0p = c0 * u ** p / phi0
                            x1 = (FJ + X) / 4; x0 = (1 + phi0) / 4
                            if not (in1(x1) and in0(x0) and in1(Xp)): continue
                            for menu in ('A', "A'"):
                                if menu == 'A':
                                    vals1 = (FJ * (1 + Xp) / 4, FJ * x1 * (1 + Xp) / c)
                                    vals0 = ((1 + phi0p) / 4, x0 * (1 + phi0p) / c)
                                else:
                                    vals1 = (x1 * Xp, FJ * x1 * Xp / c)
                                    vals0 = (x0 * phi0p, x0 * phi0p / c)
                                if all(in1(v) for v in vals1) and all(in0(v) for v in vals0):
                                    h = (menu, c0, p, D, str(u), str(c), S, str(X), str(Xp), str(phi0))
                                    hits.append(h); print('HIT', h, flush=True)
print('c0=%d p<=%d U3=%d D-mults=%s IMAX=%d: %d (shape, X) tested, %d hits' % (c0, PMAX, U3, TL, IMAX, ntest, len(hits)))
