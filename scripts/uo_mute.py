"""O186: unit-orbit mechanism for the q-mute variant ES^(S) (UNIT_ORBIT_ES.md §2).
For each n (coprime to 2S) find Q in <S> (increasing) and a prime r = 3 mod 4 dividing n + 4Q^2;
build x = (n+e)/4, y = n(r+1)/4, z = n x (r+1)/(4Q^2), e = (n+4Q^2)/r, and verify exactly:
4/n = 1/x+1/y+1/z, x,y in Z_{>0}, z in Z[1/S] with even negative q-valuations, Type II shape (gcd(x,n)=1, n|y, n|num z).
usage: uo_mute.py NMAX QMAX mode(primes|all) S..."""
import sys, numpy as np
from fractions import Fraction
from math import gcd, isqrt
NMAX, QMAX, mode = int(sys.argv[1]), int(sys.argv[2]), sys.argv[3]
S = [int(s) for s in sys.argv[4:]]
Qs = [1]
for q in S:
    Qs = sorted({a * q**k for a in Qs for k in range(40) if a * q**k <= QMAX})
LIM = NMAX + 4 * QMAX**2 + 1
spf = np.zeros(LIM, dtype=np.int32)
for i in range(2, isqrt(LIM) + 1):
    if spf[i] == 0:
        blk = spf[i*i::i]; blk[blk == 0] = i
spf_is0 = spf == 0
def factor3(a):
    while a > 1:
        r = a if spf_is0[a] else int(spf[a])
        if r % 4 == 3: return r
        while a % r == 0: a //= r
    return None
def vq(N, q):
    k = 0
    while N % q == 0: N //= q; k += 1
    return k
def check(n, Q, r):
    a = n + 4*Q*Q; e = a // r
    assert a % r == 0 and (n + e) % 4 == 0
    x = (n + e)//4; y = n*(r+1)//4; z = Fraction(n*x*(r+1), 4*Q*Q)
    assert Fraction(4, n) == Fraction(1, x) + Fraction(1, y) + 1/z and x > 0 and y > 0 and z > 0
    den = z.denominator
    for q in S:
        k = vq(den, q); den //= q**k; assert k % 2 == 0
    assert den == 1 and gcd(x, n) == 1 and y % n == 0 and z.numerator % n == 0
bad = 0; hist = {}; cnt = 0; sq_hits = 0
isprime = lambda m: m > 1 and spf_is0[m]
for n in range(3, NMAX, 2):
    if any(n % q == 0 for q in S): continue
    if mode == 'primes' and not isprime(n): continue
    issq = isqrt(n)**2 == n
    found = None
    for Q in Qs:
        r = factor3(n + 4*Q*Q)
        if r: found = (Q, r); break
    if issq:
        sq_hits += found is not None; continue
    cnt += 1
    if found is None: bad += 1; print("FAIL", n); continue
    check(n, *found); hist[found[0]] = hist.get(found[0], 0) + 1
print(f"S={S} mode={mode} n<{NMAX}: tested {cnt} non-squares, failures {bad}; squares with a hit: {sq_hits}")
print("smallest Q distribution:", sorted(hist.items())[:25])
