# z52d_thinfamily_Ap.py — menu A' in full generality (Z52D_THINFAMILY.md §3.5), at mu = 0 of n = c0*2^s + 1:
#   B' = lam2*n + lam1 = f*h  (lam1, lam2 coprime positive integers; f = 4x - n, h non-constant),
#   x = (n+f)/4,  y = x*h/lam2,  z = n*x*h/lam1.
# Capelli: K := (lam1+lam2)/(c0*lam2) is u^p (p odd prime | D) or 4w^4 (4 | D); generated as K = (r/v)^p resp. 4(r/v)^4.
# D-independent necessary test: for every monic proper factor P of Y^D + K (any D),  P(1)/P(0) = g(1)/l_g with g a
# primitive integer factor of A Z^D + Bd (K = A/Bd), l_g | A, 0 < g(1) | A + Bd.  So phi0 = f(0) = X l_g/g(1).
# Exact conditions tested: x, y, z in Z[1/2] at Y = 1 (n = F = 4^J), in Z_(2) at Y = 0 (n = 1), with X = f(1),
# H = h(1) = (F lam2 + lam1)/X, eta = h(0) = (lam1 + lam2)/phi0.
# Usage: z52d_thinfamily_Ap.py c0 RV TMAX PMAX       (r, v <= RV coprime; lam2 = t * v^p / gcd(c0, v^p) ... t <= TMAX)
import sys
from fractions import Fraction as Fr
from math import gcd
import cypari2
pari = cypari2.Pari(); pari.allocatemem(1 * 10**9)
c0 = int(sys.argv[1]); RV = int(sys.argv[2]); TMAX = int(sys.argv[3]); PMAX = int(sys.argv[4])
F = c0 + 1; J = F.bit_length() // 2; assert 4 ** J == F
def in0(x): return Fr(x).denominator % 2 == 1
def in1(x):
    d = Fr(x).denominator
    while d % 2 == 0: d //= 2
    return d == 1
def v2(x):
    x = Fr(x); n, d, v = x.numerator, x.denominator, 0
    if n == 0: return 10 ** 9
    while n % 2 == 0: n //= 2; v += 1
    while d % 2 == 0: d //= 2; v -= 1
    return v
def odd(n):
    while n % 2 == 0: n //= 2
    return n
def divs(n): return [int(t) for t in pari.divisors(n)]
primes = [q for q in range(3, PMAX + 1) if all(q % a for a in range(2, q))]
hits = []; ntest = 0; seenK = set()
for e in primes + ['sg']:
    for r in range(1, RV + 1):
        for v in range(1, RV + 1):
            if gcd(r, v) != 1: continue
            K = Fr(4 * r ** 4, v ** 4) if e == 'sg' else Fr(r ** e, v ** e)
            # lam1 + lam2 = c0 lam2 K, lam1 > 0  =>  c0 K > 1;  lam2 must make c0 lam2 K an integer
            if c0 * K <= 1: continue
            base = (c0 * K).denominator
            for t in range(1, TMAX + 1):
                lam2 = base * t; lam1 = int(c0 * lam2 * K) - lam2
                if lam1 <= 0 or gcd(lam1, lam2) != 1: continue
                if (lam1, lam2) in seenK: continue
                seenK.add((lam1, lam2))
                A, Bd = K.numerator, K.denominator
                M = F * lam2 + lam1; q = odd(lam1) * odd(lam2)
                for g1 in divs(A + Bd):
                    for l in divs(A):
                        a = v2(Fr(g1, l))
                        for Xo in divs(odd(M)):
                            X = Fr(Xo) * Fr(2) ** a
                            ntest += 1
                            if not in1((X + F) / q): continue          # X = -F mod q (odd prime powers)
                            phi0 = X * l / g1
                            x0 = (1 + phi0) / 4
                            if not in0(x0): continue
                            H = Fr(M) / X; eta = Fr(lam1 + lam2) / phi0
                            x1 = (F + X) / 4
                            ok = (in1(x1) and in1(x1 * H / lam2) and in1(F * x1 * H / lam1)
                                  and in0(x0 * eta / lam2) and in0(x0 * eta / lam1))
                            if ok:
                                hits.append((e, str(K), lam1, lam2, str(X), g1, l))
                                print('HIT', hits[-1], flush=True)
print("c0=%d menu A' general: %d (lam1, lam2) pairs, %d (pair, shape, X) tests, %d D-independent hits"
      % (c0, len(seenK), ntest, len(hits)))
