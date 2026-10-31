"""z52b pass1 U05 Z1581/Z1628: forensics of the C-form at p=409 (controls 401, 433).
win(C): some divisor of N=4Cp+1 is ≡ -1 (mod 4C). Repo lemma: any certificate divisor is a QNR mod p.
Reciprocity: for prime q | N, p ≡ -1/(4C) (mod q), so (q/p) = (-C/q) (p≡1 mod 4).
Records, for each C<=CMAX: win?, #QNR prime factors mod p, whether ALL prime factors are QR mod p."""
import sys
from collections import Counter
CMAX = 2000
def factor(n):
    f = Counter(); d = 2
    while d*d <= n:
        while n % d == 0: f[d] += 1; n //= d
        d += 1
    if n > 1: f[n] += 1
    return f
def divisors(f):
    ds = [1]
    for q, e in f.items():
        ds = [d*q**k for d in ds for k in range(e+1)]
    return ds
def leg(a, p):
    a %= p
    return 1 if pow(a, (p-1)//2, p) == 1 else -1
for p in [409, 401, 433]:
    wins = []; allQR = 0; reasons = Counter(); fails = 0
    for C in range(1, CMAX+1):
        m = 4*C; N = m*p+1; fac = factor(N)
        w = any(d % m == m-1 for d in divisors(fac))
        if w: wins.append(C); continue
        fails += 1
        syms = [leg(q, p) for q in fac]
        if all(s == 1 for s in syms): allQR += 1
        reasons[('some QNR' if -1 in syms else 'all QR')] += 1
    print(f"p={p}: wins for C<={CMAX}: {len(wins)} first={wins[:8]}; fails={fails}; "
          f"fails with ALL prime factors QR mod p: {allQR}; fails with some QNR factor: {reasons['some QNR']}")
