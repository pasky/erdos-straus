# z52d_thinfamily_menuA.py — certified limit-level enumeration for the irreducible-x menus A and A' (Z52D_THINFAMILY.md
# Thms 3.3, 3.4) at mu = 0 of n = c0*2^s + 1, c0 = F - 1, F = 4^J, for INTEGER u, every odd prime p and every
# 2-adic valuation E = v2(c0 u^p - 1) <= EMAX.
#   c = c0 u^p - 1 = 2^E c_o (c_o odd),  N = F + c = c0 (1 + u^p),  X X' = N,  X, X' positive integers.
#   menu A : c_o | (F + X)(1 + X')   <=>  X + F X' + 2F = k c_o (k >= 1);  forces
#            k^2 c_o <= Q + (Q^2 + 1)/2,  Q = 2F(k + 2^E)           (Thm 3.3; k = 1 gives the global bound CA(E))
#   menu A': c_o | X' + 1  <=>  X = j c_o - F, X' = j' c_o - 1, j j' c_o - j - F j' = 2^E;  forces c_o <= 2^E + F + 1.
# For each E the admissible u satisfy c0 u^p <= 1 + 2^E * CA(E) and u = c0^{-1/p} (mod 2^E) (x -> x^p is a bijection
# of (Z/2^E)^x for odd p), so the enumeration over (E, p, u) is finite and complete for E <= EMAX.
# Output: every (E, p, u) passing the limit-level test of A or A' (necessary conditions; a hit is then fed to the exact
# factor-shape test of z52d_thinfamily_binom.py).  Positive controls: c0 = 63 (Thm 2.3 family, u = 3, p = 3),
# c0 = 3 (u = 3, p = 3, c = 80).
# Usage: z52d_thinfamily_menuA.py c0 EMAX
import sys
from math import isqrt
import cypari2, gmpy2
pari = cypari2.Pari(); pari.allocatemem(1 * 10**9)
c0 = int(sys.argv[1]); EMAX = int(sys.argv[2])
F = c0 + 1; J = F.bit_length() // 2; assert 4 ** J == F

def iroot(a, p):            # floor(a^(1/p)) for a >= 0 (exact, gmpy2)
    if a <= 0: return 0
    return int(gmpy2.iroot(gmpy2.mpz(a), p)[0])
def primes_upto(m):
    s = bytearray([1]) * (m + 1); s[0:2] = b'\x00\x00'
    for i in range(2, isqrt(m) + 1):
        if s[i]: s[i * i::i] = bytearray(len(s[i * i::i]))
    return [i for i in range(3, m + 1) if s[i]]
def v2(x):
    return (x & -x).bit_length() - 1

def CA(E):                   # Thm 3.3 bound at k = 1:  c_o <= Q + (Q^2+1)/2, Q = 2F(1 + 2^E)
    Q = 2 * F * (1 + 2 ** E); return Q + (Q * Q + 1) // 2
def CAp(E): return 2 ** E + F + 1

def testA(u, p, E, co, N):
    """all X with X X' = N, c_o | (F+X)(1+X'); returns list of (X, X')."""
    out = []
    if N < 10 ** 40 or (co < 10 ** 12 and N < 10 ** 60):          # direct: all divisors of N
        for X in (int(t) for t in pari.divisors(N)):
            Xp = N // X
            if ((F + X) * (1 + Xp)) % co == 0: out.append((X, Xp))
        return out
    if 2 * F * 2 ** E > 10 ** 7 * isqrt(co): raise RuntimeError('k-range too large at %s' % ((u, p, E),))
    k = 1
    while True:
        Q = 2 * F * (k + 2 ** E)
        if k * k * co > Q + (Q * Q + 1) // 2 or k * co > F * N + 2 * F + 1: break
        D = co * (k * k * co - 4 * F * (k + 2 ** E))
        if D >= 0:
            W = isqrt(D)
            if W * W == D:
                for sg in (1, -1):
                    a2 = k * co - 2 * F + sg * W       # = 2X
                    b2 = k * co - 2 * F - sg * W       # = 2 F X'
                    if a2 > 0 and a2 % 2 == 0 and b2 > 0 and b2 % (2 * F) == 0:
                        X, Xp = a2 // 2, b2 // (2 * F)
                        if X * Xp == N: out.append((X, Xp))
        k += 1
    return out

def testAp(u, p, E, co, N):
    out = []
    if N < 10 ** 40 or co <= F:
        for X in (int(t) for t in pari.divisors(N)):
            Xp = N // X
            if ((F + X) * Xp) % co == 0: out.append((X, Xp))
        return out
    jp = 1
    while True:
        den = jp * co - 1
        if den > 2 ** E + F * jp: break         # then j < 1
        num = 2 ** E + F * jp
        if den > 0 and num % den == 0:
            j = num // den; X, Xp = j * co - F, jp * co - 1
            if X > 0 and X * Xp == N: out.append((X, Xp))
        jp += 1
    return out

from fractions import Fraction as Fr
def fv2(x):
    x = Fr(x); n, d, v = x.numerator, x.denominator, 0
    if n == 0: return 10 ** 9
    while n % 2 == 0: n //= 2; v += 1
    while d % 2 == 0: d //= 2; v -= 1
    return v
def in0(x): return Fr(x).denominator % 2 == 1
def shape_any_D(menu, u, p, c, X, Xp):
    """D-independent 2-adic shape test (memo Lemma 3.6): every monic proper factor P of Y^D + u^p (any D) lies in Z[Y],
    so P(1) is a positive divisor of 1 + u^p and P(0) a signed divisor of u^p; phi0 = X P(0)/P(1).  Returns the list
    of (P(1), P(0)) value pairs passing the Y = 0 conditions of the menu (empty => the limit hit is dead for every D)."""
    ok = []
    for A in (int(t) for t in pari.divisors(1 + u ** p)):
        for l0 in (int(t) for t in pari.divisors(u ** p)):
            for l in (l0, -l0):
                phi0 = Fr(X) * l / A; phi0p = Fr(c0 * u ** p) / phi0
                if phi0 <= 0 and X > 0 and l > 0: continue
                x0 = (1 + phi0) / 4
                if menu == 'A': vals = (x0, (1 + phi0p) / 4, x0 * (1 + phi0p) / c)
                else: vals = (x0, x0 * phi0p, x0 * phi0p / c)
                if all(in0(v) for v in vals): ok.append((A, l))
    return ok
hits = []; ncand = 0; maxp_used = 0
for E in range(1, EMAX + 1):
    M = 2 ** E
    Ubound = 1 + M * CA(E)                    # c0 u^p <= Ubound
    pmax = 3
    while 3 ** (pmax + 1) * c0 <= Ubound: pmax += 1
    for p in primes_upto(max(pmax, 3)):
        if c0 * 3 ** p > Ubound: break
        maxp_used = max(maxp_used, p)
        umax = iroot(Ubound // c0, p)
        # residue r = c0^{-1/p} mod 2^E
        if E <= 2:
            rs = [r for r in range(1, M, 2) if (c0 * pow(r, p, M) - 1) % M == 0] if M > 1 else [1]
        else:
            inv = pow(c0, -1, M); pp = pow(p, -1, 2 ** (E - 2)); rs = [pow(inv, pp, M)]
        for r in rs:
            u = r
            while u <= umax:
                if u >= 1 and u % 2 == 1:
                    c = c0 * u ** p - 1
                    if v2(c) == E:
                        ncand += 1
                        co = c >> E; N = F + c
                        if co <= CA(E):
                            for (X, Xp) in testA(u, p, E, co, N):
                                hits.append(('A', E, p, u, c, X, Xp)); print('LIMIT-HIT', hits[-1], 'shape(any D):', shape_any_D('A', u, p, c, X, Xp), flush=True)
                        if co <= CAp(E):
                            for (X, Xp) in testAp(u, p, E, co, N):
                                hits.append(("A'", E, p, u, c, X, Xp)); print('LIMIT-HIT', hits[-1], 'shape(any D):', shape_any_D("A'", u, p, c, X, Xp), flush=True)
                u += M
    if E % 100 == 0: print('.. E = %d done, %d candidates so far' % (E, ncand), flush=True)
print('c0=%d EMAX=%d: %d candidates (E, p, u) tested (p up to %d), %d limit-level hits' %
      (c0, EMAX, ncand, maxp_used, len(hits)))
