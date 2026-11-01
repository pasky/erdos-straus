# z53_thin15_menuB.py — certified limit-level enumeration of menu B (= II-ac, normalised c = 1) at mu = 0 of
# n = 15*2^s + 1 (Z53_THIN15.md Prop 6, 7), every root degree D, every odd prime p.
#  part 'int'   : odd integer u, E = v2(15u^p - 1) <= EMAX.  Limit equation  j j' c_o = 2^E + 16 j + j'
#                 (X = j c_o - 1, X' = j' c_o - 16), hence c_o <= 2^E + 17, 15u^p <= 1 + 2^E(2^E + 17) and
#                 u = 15^{-1/p} (mod 2^E).
#  part 'dyadic': u = r/2^i (r odd, i >= 1), e = i p <= EMAX.  c_num = 15 r^p - 2^e > 0, limit equation
#                 j j' c_num = 2^(e+4) j + j' + 1 (X = j c_num - 1, 2^e X' = j' c_num - 2^(e+4)), so c_num <= 2^(e+4)+2.
# Every limit-level solution is then passed to the exact D-independent test z53_thin15_menus.test (Y = 0 conditions with
# the Lemma-6 ratio set).  Usage: z53_thin15_menuB.py int|dyadic EMAX
import sys
from fractions import Fraction as Fr
import gmpy2
from z53_thin15_menus import test, divs
mode, EMAX = sys.argv[1], int(sys.argv[2])
def primes_upto(m):
    s = bytearray([1]) * (m + 1); s[0:2] = b'\x00\x00'
    for i in range(2, int(m ** 0.5) + 1):
        if s[i]: s[i * i::i] = bytearray(len(s[i * i::i]))
    return [i for i in range(3, m + 1) if s[i]]
def v2(x): return (x & -x).bit_length() - 1
def iroot(a, p): return int(gmpy2.iroot(gmpy2.mpz(a), p)[0]) if a > 0 else 0
nlim = 0; nexact = 0; flags = []

def limit_divisor_pairs(N, c, X_off, Xp_off, scale):
    """all X = j c - X_off (j >= 1) dividing N with N/X = j' c - Xp_off (j' >= 1); scale unused hook."""
    out = []
    t = N // c + 2
    if t <= 10 ** 6:
        for j in range(1, t + 1):
            X = j * c - X_off
            if X <= 0 or N % X: continue
            Y = N // X
            if (Y + Xp_off) % c == 0 and Y + Xp_off >= c: out.append((X, Y))
    elif N < 10 ** 70:
        for X in divs(N):
            Y = N // X
            if (X + X_off) % c == 0 and (Y + Xp_off) % c == 0 and X + X_off >= c and Y + Xp_off >= c: out.append((X, Y))
    else:
        flags.append((N, c)); print('FLAG unfactored', c, flush=True)
    return out

if mode == 'int':
    ncand = 0; RES = {}
    for E in range(1, EMAX + 1):
        M = 2 ** E; bound = 1 + M * (M + 17)          # 15 u^p <= bound
        for p in primes_upto(max(3, int(1.3 * E) + 10)):
            if E == 1: RES[p] = 1
            elif E == 2: RES[p] = 3
            elif p not in RES:      # x -> x^p is a bijection of (Z/2^E)^x (exponent 2^(E-2)), inverse x -> x^(p^-1)
                RES[p] = pow(pow(15, -1, M), pow(p, -1, 2 ** (E - 2)), M)
                assert (15 * pow(RES[p], p, M) - 1) % M == 0
            else:
                r0 = RES[p]
                RES[p] = r0 if (15 * pow(r0, p, M) - 1) % M == 0 else r0 + M // 2
                assert (15 * pow(RES[p], p, M) - 1) % M == 0
            if 15 * 3 ** p > bound and E > 1: continue
            umax = iroot(bound // 15, p)
            u = RES[p]
            while u <= umax:
                c = 15 * u ** p - 1
                if v2(c) == E:
                    ncand += 1
                    co = c >> E; N = 16 + c
                    if co <= M + 17:
                        for (X, Xp) in limit_divisor_pairs(N, co, 1, 16, None):
                            nlim += 1
                            h = test(15, Fr(c), Fr(u) ** p, menus=('B',))
                            nexact += len(h)
                            print('LIMIT-HIT E=%d p=%d u=%d X=%d Xp=%d exact-survivors=%s' % (E, p, u, X, Xp, h), flush=True)
                u += M
        if E % 250 == 0: print('.. E=%d, %d candidates' % (E, ncand), flush=True)
    print('menu B, odd integer u, E <= %d: %d candidates (E,p,u), %d limit-level solutions, %d exact survivors, %d flags'
          % (EMAX, ncand, nlim, nexact, len(flags)))
elif mode == 'dyadic':
    nw = 0
    for p in primes_upto(EMAX):
        for i in range(1, EMAX // p + 1):
            e = i * p; P2 = 2 ** e
            rmin = iroot(P2 // 15, p); rmax = iroot((17 * P2 + 2) // 15, p) + 1
            for r in range(rmin | 1, rmax + 1, 2):
                cn = 15 * r ** p - P2
                if cn <= 0 or cn > 16 * P2 + 2: continue
                nw += 1
                N = 16 * P2 + cn
                for (X, Xpp) in limit_divisor_pairs(N, cn, 1, 16 * P2, None):
                    nlim += 1
                    h = test(15, Fr(cn, P2), Fr(r, 2 ** i) ** p, menus=('B',))
                    nexact += len(h)
                    print('LIMIT-HIT p=%d i=%d r=%d X=%d 2^e X\'=%d exact-survivors=%s' % (p, i, r, X, Xpp, h), flush=True)
        print('.. p=%d done, %d windows' % (p, nw), flush=True)
    print('menu B, dyadic u = r/2^i, e = ip <= %d: %d (p,i,r) tested, %d limit-level solutions, %d exact survivors, %d flags'
          % (EMAX, nw, nlim, nexact, len(flags)))
