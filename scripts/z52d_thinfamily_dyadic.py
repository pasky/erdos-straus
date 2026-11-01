# z52d_thinfamily_dyadic.py — menu A' of Z52D_THINFAMILY.md with NON-integral u = r/2^i (i >= 1, r odd), c0 = 15:
#   c = 15 u^p - 1 = c_num / 2^e (e = i p, c_num = 15 r^p - 2^e odd > 0); limit conditions (memo §3.5):
#   X = j c_num - 16, X'' = 2^e X' = j' c_num - 2^e,  X X'' = 2^{e+4} + c_num   (j, j' >= 1),
#   equivalently  j j' c_num - 2^e j - 16 j' = 1,  which forces  c_num <= 2^e + 17, i.e. 2^e < 15 r^p <= 2^{e+1} + 17.
# Exhaustive for e = i p <= EMAX: enumerates all odd r in that window, all divisor pairs of M = 2^{e+4} + c_num, and
# then applies the exact factor-shape test (all monic proper factor products P of Y^D + u^p, D = p t, t in TL):
#   phi0 = X P(0)/P(1) must satisfy  x(0) = (1+phi0)/4,  y(0) = x(0) phi0',  z(0) = x(0) phi0'/c  in Z_(2).
# Usage: z52d_thinfamily_dyadic.py EMAX [TL]
import sys, itertools
from fractions import Fraction as Fr
import cypari2, gmpy2
pari = cypari2.Pari(); pari.allocatemem(1 * 10**9)
EMAX = int(sys.argv[1]); TL = [int(t) for t in sys.argv[2].split(',')] if len(sys.argv) > 2 else [1, 2, 3, 4]
c0, F = 15, 16
def v2(x):
    x = Fr(x)
    if x == 0: return 10 ** 9
    n, d, v = x.numerator, x.denominator, 0
    while n % 2 == 0: n //= 2; v += 1
    while d % 2 == 0: d //= 2; v -= 1
    return v
def in0(x): return Fr(x).denominator % 2 == 1
def in1(x):
    d = Fr(x).denominator
    while d % 2 == 0: d //= 2
    return d == 1
def primes(m): return [q for q in range(3, m + 1) if all(q % a for a in range(2, int(q ** .5) + 1))]
limit_hits, full_hits, nr = [], [], 0
# exponent p (odd prime, u = r/2^i, e = i p) or the Sophie-Germain case 'sg' (1 + c = 60 w^4, w = r/2^i, u^p -> 4 w^4 =
# r^4 / 2^{4i-2}, e = 4i - 2, 4 | D); in the code p = 4 encodes 'sg' (u^p is then r^4/2^e).
for p in primes(EMAX) + [4]:
    for i in range(1, EMAX // p + 2):
        e = i * p if p != 4 else 4 * i - 2
        if e > EMAX: continue
        rlo = int(gmpy2.iroot(gmpy2.mpz(2 ** e // 15), p)[0]); rhi = int(gmpy2.iroot(gmpy2.mpz((2 ** (e + 1) + 17) // 15), p)[0]) + 1
        for r in range(max(1, rlo), rhi + 1):
            if r % 2 == 0: continue
            cn = 15 * r ** p - 2 ** e
            if cn <= 0 or cn > 2 ** e + 17: continue
            nr += 1
            M = 2 ** (e + 4) + cn
            for X in (int(t) for t in pari.divisors(M)):
                X2 = M // X
                if (X + 16) % cn or (X2 + 2 ** e) % cn: continue
                u = Fr(r, 2 ** i) if p != 4 else None
                c = Fr(cn, 2 ** e); Xp = Fr(X2, 2 ** e)
                Kp = Fr(r ** p, 2 ** e)                       # = u^p (resp. 4 w^4 in the sg case)
                # D-independent shape test (memo Lemma 3.6): P(1)/P(0) = g(1)/l_g, g a primitive integer factor of
                # r^p Z^D + 2^e with positive leading coefficient l_g | r^p and g(1) | r^p + 2^e, g(1) > 0.
                anyD = []
                for A in (int(t) for t in pari.divisors(r ** p + 2 ** e)):
                    for l in (int(t) for t in pari.divisors(r ** p)):
                        phi0 = Fr(X * l, A); phi0p = c0 * Kp / phi0; x0 = (1 + phi0) / 4
                        if in0(x0) and in0(x0 * phi0p) and in0(x0 * phi0p / c): anyD.append((A, l))
                limit_hits.append((p, i, r, cn, X, X2, len(anyD)))
                print('LIMIT-HIT p=%s K=u^p=%s c=%s X=%d X\'=%s  shape(any D): %s' % (p if p != 4 else 'sg', Kp, c, X, Xp, anyD), flush=True)
                if p == 4: continue                     # explicit-D test only for odd p (the any-D test above is the proof)
                for t in TL:
                    D = p * t
                    Fz = pari('factor(Y^%d + (%s)^%d)' % (D, str(u), p))
                    fs = []
                    for a in range(len(Fz[0])):
                        pol = Fz[0][a]; co = [Fr(str(pol.polcoef(b))) for b in range(int(pol.poldegree()) + 1)]
                        fs += [[x / co[-1] for x in co]] * int(Fz[1][a])
                    for k in range(1, len(fs)):
                        for S in itertools.combinations(range(len(fs)), k):
                            P1 = Fr(1); P0 = Fr(1)
                            for b in S: P1 *= sum(fs[b]); P0 *= fs[b][0]
                            phi0 = X * P0 / P1; phi0p = c0 * u ** p / phi0
                            x0 = (1 + phi0) / 4
                            if in0(x0) and in0(x0 * phi0p) and in0(x0 * phi0p / c):
                                full_hits.append((p, D, str(u), S, X)); print('FULL-HIT', full_hits[-1], flush=True)
print("menu A', u = r/2^i, e = ip <= %d: %d (p, i, r) windows tested, %d limit-level hits (%d surviving the any-D shape "
      "test), %d full hits (explicit D = p*t, t in %s)" % (EMAX, nr, len(limit_hits), sum(1 for h in limit_hits if h[-1]),
      len(full_hits), TL))
